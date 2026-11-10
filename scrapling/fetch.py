"""Única salida a la red del rastreador: espera por host, reintentos limitados, tiempo de espera,
caché por dominio y registro de trazabilidad en JSONL.

Reglas que no se pueden relajar con argumentos:
  - Mínimo 3 segundos entre solicitudes al mismo host.
  - Como mucho 3 intentos por URL, y solo ante error de red o HTTP 500, 502, 503 o 504.
  - Nunca se reintenta un 403, un 429 ni una página de desafío: el rastreador detiene el sitio.
  - Fetcher HTTP simple de Scrapling, sin suplantación de navegador, sin proxies y sin seguir redirecciones.
"""
from __future__ import annotations

import hashlib
import json
import os
import tempfile
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from urllib.parse import urlsplit

USER_AGENT = "FundigsacMarketResearch/1.1"
CABECERAS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.5",
}
INTERVALO_MINIMO = 3.0
MAX_INTENTOS_TOPE = 3
TIEMPO_ESPERA_HTTP = 30
STATUS_REINTENTABLE = {500, 502, 503, 504}
# Respuestas que se guardan en caché. 403 y 429 nunca se guardan, para no fijar un bloqueo.
STATUS_CACHEABLE = {200, 301, 302, 303, 307, 308, 404, 410}
CABECERAS_GUARDADAS = ("content-type", "location", "cf-mitigated", "last-modified", "etag", "retry-after")


class ErrorRed(Exception):
    """Fallo de red tras agotar los intentos permitidos."""


@dataclass
class Respuesta:
    url: str
    status: int
    headers: dict
    body: bytes
    desde_cache: bool
    fecha_utc: str
    intentos: int = 0
    sha256: str = field(default="")


def _ahora_utc() -> datetime:
    return datetime.now(timezone.utc)


def _escribir_atomico(ruta: str, datos: bytes) -> None:
    carpeta = os.path.dirname(ruta)
    os.makedirs(carpeta, exist_ok=True)
    descriptor, temporal = tempfile.mkstemp(dir=carpeta, suffix=".tmp")
    try:
        with os.fdopen(descriptor, "wb") as archivo:
            archivo.write(datos)
        os.replace(temporal, ruta)
    except BaseException:
        if os.path.exists(temporal):
            os.unlink(temporal)
        raise


class CacheDominio:
    """Caché en disco: `<raiz>/<host>/<sha256(url)[:32]>.html` y `.json` con metadatos."""

    def __init__(self, raiz: str | None, ttl_horas: float):
        self.raiz = raiz
        self.ttl = timedelta(hours=ttl_horas)

    def _rutas(self, url: str) -> tuple[str, str]:
        host = urlsplit(url).netloc.replace(":", "_") or "_"
        clave = hashlib.sha256(url.encode("utf-8")).hexdigest()[:32]
        base = os.path.join(self.raiz, host, clave)
        return base + ".html", base + ".json"

    def leer(self, url: str) -> Respuesta | None:
        if not self.raiz:
            return None
        ruta_cuerpo, ruta_meta = self._rutas(url)
        if not (os.path.exists(ruta_cuerpo) and os.path.exists(ruta_meta)):
            return None
        with open(ruta_meta, encoding="utf-8") as archivo:
            meta = json.load(archivo)
        fecha = datetime.fromisoformat(meta["fecha_utc"])
        if _ahora_utc() - fecha > self.ttl:
            return None
        with open(ruta_cuerpo, "rb") as archivo:
            cuerpo = archivo.read()
        return Respuesta(
            url=meta["url"], status=meta["status"], headers=meta.get("headers", {}), body=cuerpo,
            desde_cache=True, fecha_utc=meta["fecha_utc"], intentos=0, sha256=meta.get("sha256", ""),
        )

    def guardar(self, respuesta: Respuesta) -> None:
        if not self.raiz or respuesta.status not in STATUS_CACHEABLE:
            return
        ruta_cuerpo, ruta_meta = self._rutas(respuesta.url)
        _escribir_atomico(ruta_cuerpo, respuesta.body)
        meta = {
            "url": respuesta.url, "status": respuesta.status, "headers": respuesta.headers,
            "fecha_utc": respuesta.fecha_utc, "sha256": respuesta.sha256, "bytes": len(respuesta.body),
        }
        _escribir_atomico(ruta_meta, json.dumps(meta, ensure_ascii=False, indent=2).encode("utf-8"))


class Cliente:
    """Cliente HTTP con espera por host, reintentos limitados, caché y registro de cada solicitud."""

    def __init__(
        self,
        intervalo: float = INTERVALO_MINIMO,
        timeout: int = TIEMPO_ESPERA_HTTP,
        max_intentos: int = 2,
        dir_cache: str | None = None,
        ttl_cache_horas: float = 24.0,
        ruta_registro: str | None = None,
        reloj=time.monotonic,
        dormir=time.sleep,
    ):
        self.intervalo = max(float(intervalo), INTERVALO_MINIMO)
        self.timeout = int(timeout)
        self.max_intentos = max(1, min(int(max_intentos), MAX_INTENTOS_TOPE))
        self.cache = CacheDominio(dir_cache, ttl_cache_horas)
        self.ruta_registro = ruta_registro
        self._reloj = reloj
        self._dormir = dormir
        self._ultima_por_host: dict[str, float] = {}
        self.solicitudes_red = 0
        self.aciertos_cache = 0

    def ajustar_intervalo(self, segundos: float | None) -> None:
        """Sube el intervalo si robots.txt pide más espera (Crawl-delay o Request-rate). Nunca lo baja."""
        if segundos:
            self.intervalo = max(self.intervalo, float(segundos))

    def _esperar_turno(self, host: str) -> None:
        ultima = self._ultima_por_host.get(host)
        if ultima is not None:
            restante = self.intervalo - (self._reloj() - ultima)
            if restante > 0:
                self._dormir(restante)

    def _registrar(self, evento: dict) -> None:
        if not self.ruta_registro:
            return
        os.makedirs(os.path.dirname(os.path.abspath(self.ruta_registro)), exist_ok=True)
        with open(self.ruta_registro, "a", encoding="utf-8") as archivo:
            archivo.write(json.dumps(evento, ensure_ascii=False) + "\n")

    def _descargar(self, url: str):
        from scrapling.fetchers import Fetcher  # import tardío: parse.py y las pruebas no necesitan red

        return Fetcher.get(
            url,
            headers=dict(CABECERAS),
            impersonate=None,
            stealthy_headers=False,
            follow_redirects=False,
            retries=1,
            timeout=self.timeout,
        )

    def obtener(self, url: str) -> Respuesta:
        """Devuelve la respuesta de caché si está vigente; si no, la descarga con las reglas del módulo."""
        en_cache = self.cache.leer(url)
        if en_cache is not None:
            self.aciertos_cache += 1
            self._registrar({"ts": _ahora_utc().isoformat(timespec="seconds"), "url": url, "status": en_cache.status,
                             "desde_cache": True, "fecha_original": en_cache.fecha_utc, "sha256": en_cache.sha256})
            return en_cache

        host = urlsplit(url).netloc
        ultimo_error: Exception | None = None
        respuesta = None
        intento = 0
        for intento in range(1, self.max_intentos + 1):
            self._esperar_turno(host)
            inicio = self._reloj()
            self.solicitudes_red += 1
            try:
                respuesta = self._descargar(url)
                ultimo_error = None
            except Exception as error:  # noqa: BLE001 - se registra y se decide si se reintenta
                ultimo_error = error
                respuesta = None
            finally:
                self._ultima_por_host[host] = self._reloj()
            duracion = round(self._reloj() - inicio, 3)
            status = getattr(respuesta, "status", None)
            self._registrar({"ts": _ahora_utc().isoformat(timespec="seconds"), "url": url, "intento": intento,
                             "status": status, "error": type(ultimo_error).__name__ if ultimo_error else None,
                             "segundos": duracion, "desde_cache": False})
            reintentar = ultimo_error is not None or status in STATUS_REINTENTABLE
            if not reintentar or intento == self.max_intentos:
                break
            # Espera creciente antes del siguiente intento: 2x y 4x el intervalo.
            self._dormir(self.intervalo * (2 ** intento))

        if respuesta is None:
            raise ErrorRed(f"{type(ultimo_error).__name__} tras {intento} intento(s)") from ultimo_error

        cabeceras = {str(k).lower(): str(v) for k, v in (respuesta.headers or {}).items()}
        cuerpo = bytes(respuesta.body or b"")
        resultado = Respuesta(
            url=url,
            status=int(respuesta.status),
            headers={k: v for k, v in cabeceras.items() if k in CABECERAS_GUARDADAS},
            body=cuerpo,
            desde_cache=False,
            fecha_utc=_ahora_utc().isoformat(timespec="seconds"),
            intentos=intento,
            sha256=hashlib.sha256(cuerpo).hexdigest(),
        )
        self.cache.guardar(resultado)
        return resultado
