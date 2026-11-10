#!/usr/bin/env python3
"""Rastreador de datos públicos para el estudio de competencia de FUNDIGSAC (versión 1.1).

Refactor de `Report/competencia/scripts/scrape.py` (9-nov-2026). Separa la red (`fetch.py`) del análisis
(`parse.py`) y añade caché por dominio, reintentos limitados y registro de trazabilidad.

Uso:
    python scrape.py URL_INICIAL salida/sitio.json
    python scrape.py --manifiesto sources.json --salida-dir salida/

Reglas que aplica el programa y que los argumentos no pueden relajar:
  - Solo páginas públicas: sin inicios de sesión, formularios, carritos ni búsquedas.
  - Lee robots.txt antes de cualquier página y omite las rutas no permitidas. Respeta Crawl-delay.
  - Máximo una solicitud cada 3 segundos por host y 40 páginas por sitio.
  - Ante 403, 429, captcha o página de desafío detiene el sitio, registra "bloqueado" y no reintenta.
  - Guarda hechos y metadatos breves. No guarda texto completo, imágenes ni datos personales en el JSON.
    La caché sí guarda el HTML tal como llegó, solo en local, para poder repetir el análisis sin volver a pedirlo.

Estados posibles: ok, bloqueado, robots_denegado, robots_no_disponible, redireccion_externa, sin_paginas, error.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import time
from collections import Counter
from datetime import datetime, timezone
from urllib.parse import urljoin, urlsplit, urlunsplit

import fetch
import parse

VERSION = "1.1.0"
MAX_PAGINAS = 40
TIEMPO_MAXIMO_POR_DEFECTO = 900
MAX_ERRORES_SEGUIDOS = 3
MAX_SALTOS_ROBOTS = 5
MAX_BYTES_ROBOTS = 500 * 1024
MAX_OMITIDAS = 200
MAX_DOCUMENTOS = 100
MAX_CONTACTOS = 10
REDIRECCIONES = (301, 302, 303, 307, 308)


class SitioBloqueado(Exception):
    """El sitio respondió con un bloqueo; se detiene sin reintentar."""


class Detencion(Exception):
    def __init__(self, estado: str, motivo: str):
        super().__init__(motivo)
        self.estado = estado
        self.motivo = motivo


def version_scrapling() -> str:
    try:
        from importlib.metadata import version

        return version("scrapling")
    except Exception:  # noqa: BLE001
        return "desconocida"


def a_selector(respuesta: fetch.Respuesta):
    from scrapling.parser import Selector

    return Selector(content=respuesta.body, url=respuesta.url)


class Rastreador:
    def __init__(self, inicio: str, cliente: fetch.Cliente, max_paginas: int, max_segundos: int):
        self.inicio = inicio
        partes = urlsplit(inicio)
        self.esquema, self.netloc = partes.scheme, partes.netloc
        self.cliente = cliente
        self.max_paginas = max(1, min(max_paginas, MAX_PAGINAS))
        self.max_segundos = max_segundos
        self.robots = None
        self.info_robots: dict = {}
        self.pedidas = 0
        self.pendientes: dict[str, int] = {}
        self.vistas: set[str] = set()
        self.por_seccion: Counter = Counter()
        self.paginas: list[dict] = []
        self.omitidas: list[str] = []
        self.externas: list[str] = []
        self.enlaces_externos: list[str] = []
        self.documentos: list[str] = []
        self.contacto = {"telefonos": [], "correos": [], "direcciones": [], "empresas": []}
        self.errores_seguidos = 0
        self.truncado_por_tiempo = False
        self.inicio_reloj = time.monotonic()

    # ------------------------------------------------------------------ robots.txt

    def misma_web(self, url: str) -> bool:
        return parse.es_variante_www(urlsplit(url).netloc, self.netloc)

    def cargar_robots(self) -> None:
        from protego import Protego

        url = urlunsplit((self.esquema, self.netloc, "/robots.txt", "", ""))
        for _ in range(MAX_SALTOS_ROBOTS + 1):
            try:
                respuesta = self.cliente.obtener(url)
            except fetch.ErrorRed as error:
                raise Detencion("error", f"No se pudo leer robots.txt: {error}") from error
            motivo = parse.detectar_bloqueo(respuesta.status, respuesta.headers, respuesta.body)
            if motivo:
                self.info_robots = {"url": url, "http_status": respuesta.status}
                raise SitioBloqueado(f"robots.txt: {motivo}")
            if respuesta.status in REDIRECCIONES:
                destino = parse.normalizar_url(urljoin(url, respuesta.headers.get("location", "")))
                if not destino or not self.misma_web(destino):
                    raise Detencion("robots_no_disponible", "robots.txt redirige fuera del sitio")
                url = destino
                continue
            self.info_robots = {"url": url, "http_status": respuesta.status, "presente": respuesta.status == 200,
                                "desde_cache": respuesta.desde_cache}
            if respuesta.status >= 500:
                # RFC 9309: robots.txt inaccesible por error del servidor equivale a prohibición total.
                raise Detencion("robots_no_disponible", f"robots.txt respondió HTTP {respuesta.status}")
            texto = respuesta.body[:MAX_BYTES_ROBOTS].decode("utf-8", errors="ignore") if respuesta.status == 200 else ""
            self.robots = Protego.parse(texto)
            demora = self.robots.crawl_delay(fetch.USER_AGENT)
            tasa = self.robots.request_rate(fetch.USER_AGENT)
            self.cliente.ajustar_intervalo(float(demora) if demora else None)
            if tasa and tasa.requests:
                self.cliente.ajustar_intervalo(float(tasa.seconds) / tasa.requests)
            self.info_robots.update({"crawl_delay": float(demora) if demora else None,
                                     "sitemaps": list(self.robots.sitemaps)[:20]})
            return
        raise Detencion("robots_no_disponible", "robots.txt con demasiadas redirecciones")

    def permitido(self, url: str) -> bool:
        return self.robots.can_fetch(url, fetch.USER_AGENT)

    # ------------------------------------------------------------------ cola

    def encolar(self, url: str) -> None:
        if url not in self.vistas and url not in self.pendientes:
            self.pendientes[url] = parse.puntaje_base(url)

    def siguiente(self) -> str:
        # Cada página visitada en una sección resta un punto, para no agotar el cupo en una sola rama.
        url = max(self.pendientes, key=lambda u: self.pendientes[u] - self.por_seccion[parse.seccion_de(u)])
        del self.pendientes[url]
        return url

    def registrar_omitida(self, url: str) -> None:
        if len(self.omitidas) < MAX_OMITIDAS:
            self.omitidas.append(url)

    # ------------------------------------------------------------------ páginas

    def manejar_redireccion(self, url: str, cabeceras: dict, es_primera: bool) -> None:
        destino = parse.normalizar_url(urljoin(url, cabeceras.get("location", "")))
        if not destino:
            return
        if not self.misma_web(destino):
            self.externas.append(destino)
            if es_primera:
                raise Detencion("redireccion_externa", f"La URL inicial redirige a otro dominio: {destino}")
            return
        partes = urlsplit(destino)
        if es_primera and (partes.netloc != self.netloc or partes.scheme != self.esquema):
            cambia_host = partes.netloc != self.netloc
            self.esquema, self.netloc = partes.scheme, partes.netloc
            if cambia_host:
                self.cargar_robots()  # el nuevo host tiene su propio robots.txt
        canonica = urlunsplit((self.esquema, self.netloc, partes.path, partes.query, ""))
        if parse.admisible(canonica):
            self.encolar(canonica)
            if canonica in self.pendientes:
                self.pendientes[canonica] += 200  # no perder la portada tras la redirección

    def procesar(self, url: str, es_primera: bool) -> None:
        self.pedidas += 1
        self.por_seccion[parse.seccion_de(url)] += 1
        try:
            respuesta = self.cliente.obtener(url)
        except fetch.ErrorRed as error:
            self.errores_seguidos += 1
            self.paginas.append({"url": url, "error": str(error)})
            if es_primera or self.errores_seguidos >= MAX_ERRORES_SEGUIDOS:
                raise Detencion("error", f"Fallo de red: {error}") from error
            return
        traza = {"desde_cache": respuesta.desde_cache, "fecha_utc": respuesta.fecha_utc, "sha256": respuesta.sha256}
        motivo = parse.detectar_bloqueo(respuesta.status, respuesta.headers, respuesta.body)
        if motivo:
            self.paginas.append({"url": url, "http_status": respuesta.status, "bloqueo": motivo, **traza})
            raise SitioBloqueado(motivo)
        if respuesta.status in REDIRECCIONES:
            self.errores_seguidos = 0
            self.manejar_redireccion(url, respuesta.headers, es_primera)
            return
        if respuesta.status != 200:
            self.errores_seguidos += 1
            self.paginas.append({"url": url, "http_status": respuesta.status, **traza})
            if respuesta.status >= 500 and self.errores_seguidos >= MAX_ERRORES_SEGUIDOS:
                raise Detencion("error", f"{self.errores_seguidos} errores seguidos del servidor")
            return
        self.errores_seguidos = 0
        tipo = respuesta.headers.get("content-type", "").lower()
        if tipo and "html" not in tipo:
            self.paginas.append({"url": url, "http_status": 200, "omitida": f"Contenido no HTML: {tipo[:60]}", **traza})
            return
        pagina, extras = parse.parsear_pagina(
            a_selector(respuesta), url, 200, len(respuesta.body), self.esquema, self.netloc
        )
        pagina["traza"] = traza
        self.paginas.append(pagina)
        self.documentos.extend(pagina["documentos_enlazados"])
        self.enlaces_externos.extend(extras["externas"])
        for clave in self.contacto:
            self.contacto[clave].extend(extras[clave])
        for candidata in extras["candidatas"]:
            self.encolar(candidata)

    def ejecutar(self) -> tuple[str, str]:
        try:
            self.cargar_robots()
            if not self.permitido(self.inicio):
                self.registrar_omitida(self.inicio)
                return "robots_denegado", "robots.txt no permite la URL inicial"
            self.pendientes[self.inicio] = 0
            primera = True
            while self.pendientes and self.pedidas < self.max_paginas:
                if time.monotonic() - self.inicio_reloj > self.max_segundos:
                    self.truncado_por_tiempo = True
                    break
                url = self.siguiente()
                self.vistas.add(url)
                if not self.permitido(url):
                    self.registrar_omitida(url)
                    continue
                print(f"[{self.pedidas + 1}/{self.max_paginas}] {url}", file=sys.stderr)
                self.procesar(url, primera)
                primera = not self.paginas  # sigue siendo la primera mientras solo haya redirecciones
        except SitioBloqueado as bloqueo:
            return "bloqueado", str(bloqueo)
        except Detencion as detencion:
            return detencion.estado, detencion.motivo
        if not any(p.get("http_status") == 200 and "titulo" in p for p in self.paginas):
            return "sin_paginas", "No se obtuvo ninguna página HTML"
        return "ok", ""

    def resultado(self, estado: str, motivo: str, ruta_registro: str | None) -> dict:
        utiles = [p for p in self.paginas if "titulo" in p]
        return {
            "url_inicial": self.inicio,
            "host": self.netloc,
            "esquema": self.esquema,
            "user_agent": fetch.USER_AGENT,
            "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "estado": estado,
            "motivo": motivo,
            "limites": {"max_paginas": self.max_paginas, "intervalo_segundos": self.cliente.intervalo,
                        "max_intentos": self.cliente.max_intentos, "timeout_segundos": self.cliente.timeout},
            "trazabilidad": {
                "version_rastreador": VERSION,
                "version_scrapling": version_scrapling(),
                "registro_solicitudes": ruta_registro,
                "solicitudes_red": self.cliente.solicitudes_red,
                "aciertos_cache": self.cliente.aciertos_cache,
            },
            "robots": self.info_robots,
            "paginas_solicitadas": self.pedidas,
            "paginas_con_datos": len(utiles),
            "truncado_por_tiempo": self.truncado_por_tiempo,
            "pendientes_sin_visitar": len(self.pendientes),
            "omitidas_por_robots": self.omitidas,
            "redirecciones_externas": parse.unicos(self.externas, 50),
            "enlaces_externos": parse.unicos(self.enlaces_externos, 100),
            "duracion_segundos": round(time.monotonic() - self.inicio_reloj, 1),
            "resumen": {
                "productos": parse.unicos((n for p in utiles for n in p["productos"]), 400),
                "categorias": parse.unicos((n for p in utiles for n in p["categorias"]), 150),
                "normas_citadas": sorted(parse.unicos(n for p in utiles for n in p["normas_citadas"])),
                "tipos_jsonld": dict(Counter(t for p in utiles for t in p["tipos_jsonld"]).most_common()),
                "secciones": dict(Counter(parse.seccion_de(p["url"]) for p in utiles).most_common()),
                "documentos_enlazados": parse.unicos(self.documentos, MAX_DOCUMENTOS),
                "contacto_empresa": {
                    "nombres": parse.unicos(self.contacto["empresas"], MAX_CONTACTOS),
                    "telefonos": parse.unicos(self.contacto["telefonos"], MAX_CONTACTOS),
                    "correos": parse.unicos(self.contacto["correos"], MAX_CONTACTOS),
                    "direcciones": parse.unicos(self.contacto["direcciones"], MAX_CONTACTOS),
                },
            },
            "paginas": self.paginas,
        }


def guardar_json(ruta: str, datos: dict) -> None:
    carpeta = os.path.dirname(os.path.abspath(ruta))
    os.makedirs(carpeta, exist_ok=True)
    descriptor, temporal = tempfile.mkstemp(dir=carpeta, suffix=".tmp")
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)
        os.replace(temporal, ruta)
    except BaseException:
        if os.path.exists(temporal):
            os.unlink(temporal)
        raise


def rastrear_sitio(url: str, salida: str, args) -> dict:
    inicio = parse.normalizar_url(url)
    if not inicio:
        raise SystemExit(f"URL no válida: {url}")
    marca = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    ruta_registro = os.path.join(args.dir_trazas, f"{urlsplit(inicio).netloc}-{marca}.jsonl")
    cliente = fetch.Cliente(
        intervalo=args.intervalo,
        timeout=args.timeout,
        max_intentos=args.max_intentos,
        dir_cache=None if args.sin_cache else args.dir_cache,
        ttl_cache_horas=args.cache_ttl_horas,
        ruta_registro=ruta_registro,
    )
    rastreador = Rastreador(inicio, cliente, args.max_paginas, args.max_segundos)
    estado, motivo = rastreador.ejecutar()
    datos = rastreador.resultado(estado, motivo, ruta_registro)
    guardar_json(salida, datos)
    return {"url": inicio, "estado": estado, "motivo": motivo, "paginas_con_datos": datos["paginas_con_datos"],
            "solicitudes_red": cliente.solicitudes_red, "aciertos_cache": cliente.aciertos_cache, "salida": salida}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Rastrea datos públicos de sitios de competidores y los guarda en JSON.")
    p.add_argument("url_inicial", nargs="?", help="URL http(s) donde empieza el rastreo (modo de un sitio)")
    p.add_argument("salida", nargs="?", help="Archivo JSON de salida (modo de un sitio)")
    p.add_argument("--manifiesto", help="sources.json: rastrea las entradas con \"rastrear\": true")
    p.add_argument("--salida-dir", default="salida/datos", help="Carpeta de salida en modo manifiesto")
    p.add_argument("--max-paginas", type=int, default=MAX_PAGINAS, help="Páginas por sitio; nunca supera 40")
    p.add_argument("--intervalo", type=float, default=fetch.INTERVALO_MINIMO, help="Segundos entre solicitudes; mínimo 3")
    p.add_argument("--timeout", type=int, default=fetch.TIEMPO_ESPERA_HTTP, help="Tiempo de espera HTTP en segundos")
    p.add_argument("--max-intentos", type=int, default=2, help="Intentos por URL ante error de red o 5xx; tope 3")
    p.add_argument("--max-segundos", type=int, default=TIEMPO_MAXIMO_POR_DEFECTO, help="Tiempo máximo por sitio")
    p.add_argument("--dir-cache", default="cache", help="Caché por dominio")
    p.add_argument("--cache-ttl-horas", type=float, default=24.0, help="Vigencia de la caché")
    p.add_argument("--sin-cache", action="store_true", help="No leer ni escribir caché")
    p.add_argument("--dir-trazas", default="salida/trazas", help="Registros JSONL de cada solicitud")
    args = p.parse_args(argv)

    resultados = []
    if args.manifiesto:
        with open(args.manifiesto, encoding="utf-8") as archivo:
            fuentes = json.load(archivo)["fuentes"]
        for fuente in fuentes:
            if not fuente.get("rastrear"):
                continue
            salida = os.path.join(args.salida_dir, f"{fuente['id']}.json")
            resultados.append({"id": fuente["id"], **rastrear_sitio(fuente["url"], salida, args)})
        guardar_json(os.path.join(args.salida_dir, "_ejecucion.json"), {
            "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "version_rastreador": VERSION, "version_scrapling": version_scrapling(), "resultados": resultados,
        })
    elif args.url_inicial and args.salida:
        resultados.append(rastrear_sitio(args.url_inicial, args.salida, args))
    else:
        p.error("Indica URL_INICIAL y SALIDA, o --manifiesto")
    print(json.dumps(resultados, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
