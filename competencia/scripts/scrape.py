#!/usr/bin/env python3
"""Rastreador de datos públicos para el estudio de competencia de FUNDIGSAC.

Uso:
    python scrape.py URL_INICIAL RUTA_SALIDA.json

Reglas que aplica el programa y que los argumentos no pueden relajar:
  - Solo páginas públicas: sin inicios de sesión, formularios ni búsquedas.
  - Lee robots.txt antes de cualquier página y omite las rutas no permitidas.
  - Máximo una solicitud cada 3 segundos por host y 40 páginas por sitio.
  - Solo Fetcher HTTP simple de Scrapling, con User-Agent identificable.
    No usa suplantación de navegador, proxies ni navegadores automatizados.
  - Ante 403, 429, captcha o página de desafío detiene el sitio, registra
    el estado "bloqueado" y no reintenta.
  - Guarda hechos y metadatos breves. No guarda el texto completo de las
    páginas, imágenes ni datos personales.

Estados posibles del campo "estado":
    ok, bloqueado, robots_denegado, robots_no_disponible, redireccion_externa,
    sin_paginas, error
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import time
from collections import Counter
from datetime import datetime, timezone
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit

from protego import Protego
from scrapling.fetchers import Fetcher

USER_AGENT = "FundigsacMarketResearch/1.0"
CABECERAS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.5",
}

INTERVALO_MINIMO = 3.0
MAX_PAGINAS = 40
TIEMPO_ESPERA_HTTP = 30
TIEMPO_MAXIMO_POR_DEFECTO = 900
MAX_ERRORES_SEGUIDOS = 3
MAX_SALTOS_ROBOTS = 5
MAX_BYTES_ROBOTS = 500 * 1024

MAX_H2 = 30
MAX_PRODUCTOS_PAGINA = 100
MAX_CATEGORIAS_PAGINA = 60
MAX_ESPECIFICACIONES = 40
MAX_ENLACES_PAGINA = 80
MAX_CONTACTOS = 10
MAX_OMITIDAS = 200
MAX_DOCUMENTOS = 100

EXTENSIONES_NO_HTML = (
    ".pdf", ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico", ".bmp", ".zip", ".rar", ".7z", ".gz",
    ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".dwg", ".mp4", ".mp3", ".avi", ".mov", ".webm",
    ".css", ".js", ".json", ".xml", ".txt", ".woff", ".woff2", ".ttf", ".eot",
)
EXTENSIONES_DOCUMENTO = (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".dwg")

# Rutas que implican sesión, transacción o búsqueda. Nunca se solicitan.
RUTA_EXCLUIDA = re.compile(
    r"(^|/)(wp-admin|wp-login(\.php)?|wp-json|xmlrpc\.php|cgi-bin|admin|administrator|login|logout|signin|sign-in|"
    r"signup|sign-up|register|registro|acceder|ingresar|iniciar-sesion|my-account|mi-cuenta|cuenta|account|"
    r"cart|carrito|carro|checkout|finalizar-compra|pago|wishlist|lista-de-deseos|compare|comparar|search|"
    r"buscar|busqueda|feed|comments|trackback)(/|\.php|\.html|$)",
    re.IGNORECASE,
)
PARAMETROS_EXCLUIDOS = re.compile(
    r"^(s|q|search|buscar|busqueda|query|term|add-to-cart|add_to_wishlist|orderby|order|sort|min_price|max_price|"
    r"filter_.*|replytocom|share|action|login|logout|redirect_to|return_url|wc-ajax|rating_filter|view)$",
    re.IGNORECASE,
)
PARAMETROS_SEGUIMIENTO = re.compile(r"^(utm_.*|gclid|fbclid|msclkid|_ga|mc_cid|mc_eid)$", re.IGNORECASE)

# Prioridad de rastreo: primero categorías, luego productos, después páginas del rubro.
REGLAS_PRIORIDAD = (
    (re.compile(r"(categoria-producto|product-category|/categorias?(/|\.php|$)|/category(/|$)|/lineas?(/|$))", re.I), 100),
    (re.compile(r"(/productos?(/|\.php|\.html|$)|/products?(/|\.php|\.html|$)|producto\.php)", re.I), 90),
    (re.compile(r"(catalogo|catalog|tienda|shop|store)", re.I), 70),
    (re.compile(r"(valvula|tuberia|hierro|ductil|marco|tapa|conexion|accesorio|saneamiento|mineria|agro|riego|hidrante|grifo|brida)", re.I), 60),
    (re.compile(r"(certific|norma|calidad|ficha|nosotros|empresa|quienes|about|servicio|solucion|proyecto|cliente|contacto)", re.I), 30),
)
RUTA_BAJA_PRIORIDAD = re.compile(
    r"(blog|noticia|news|evento|prensa|galeria|trabaja|empleo|careers|politica|privacidad|privacy|terminos|condiciones|reclamaciones|cookies)",
    re.IGNORECASE,
)
RUTA_DE_PRODUCTO = re.compile(r"(/productos?/[^/]+|/products?/[^/]+|producto\.php)", re.IGNORECASE)
HREF_CATEGORIA = re.compile(r"(categoria-producto|product-category|/categorias?/|/category/|categoria\.php)", re.IGNORECASE)

# Las normas se buscan con mayúsculas exactas para no confundir la preposición "en" con la norma EN.
PATRONES_NORMA = (
    re.compile(r"\bNTP[- ]?ISO[- ]?\d{3,5}(?:[-:]\d+)*"),
    re.compile(r"\bNTP[- ]?\d{3}\.\d{3}(?:[-:]\d+)*"),
    re.compile(r"\b(?:UNE[- ])?EN[- ]ISO[- ]?\d{2,5}(?:[-:]\d+)*"),
    re.compile(r"\bISO[- ]?\d{3,5}(?:[-:]\d+)*"),
    re.compile(r"\b(?:UNE[- ])?EN[- ]?\d{2,5}(?:[-:]\d+)*"),
    re.compile(r"\bAWWA[- ]?C\d{3}(?:[-:]\d+)*"),
    re.compile(r"\bASTM[- ]?[A-G][- ]?\d{1,4}M?"),
    re.compile(r"\bNSF(?:/ANSI)?[- ]?\d{2,3}"),
    re.compile(r"\bANSI[- /]?(?:NSF[- ]?\d{2,3}|B\d{1,2}\.\d{1,2})"),
    re.compile(r"\bBS[- ]?\d{3,5}"),
    re.compile(r"\bDIN[- ]?\d{3,5}"),
    re.compile(r"\bAPI[- ]?\d{3}[A-Z]?\b"),
)
ANIO_COMO_NORMA = re.compile(r"^EN[- ]?(19|20)\d{2}$")

# Solo se conservan buzones genéricos de la empresa; un buzón con nombre de persona se descarta.
CORREO_DE_EMPRESA = re.compile(
    r"^(ventas?|info|informes|informacion|contacto|contact|comercial|administracion|atencion|atencionalcliente|"
    r"cotizacion|cotizaciones|soporte|servicios?|servicioalcliente|logistica|marketing|facturacion|postventa|"
    r"gerencia|general|pedidos|hola)([._-]?[a-z0-9]{0,12})?@",
    re.IGNORECASE,
)
CLAVE_ESPEC = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ][A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9 ./()°-]{1,40}$")
CLAVE_NO_ESPEC = re.compile(
    r"(tel[eé]fono|celular|whatsapp|correo|e-?mail|direcci[oó]n|horario|contacto|asesor|vendedor|encargad|nombre|dni|ruc)",
    re.IGNORECASE,
)
ESPEC_EN_LISTA = re.compile(r"^([^:]{2,40}):\s*(.{1,120})$")

SELECTORES_PRODUCTO = (
    ".product_title", "h1.product-title", ".woocommerce-loop-product__title", ".wc-block-grid__product-title",
    ".product-title", ".product-name", "ul.products li.product h2", "ul.products li.product h3",
)
SELECTORES_CATEGORIA = (
    ".posted_in a", ".product_cat a", ".woocommerce-breadcrumb a", ".breadcrumb a", ".breadcrumbs a",
)
TIPOS_EMPRESA = {
    "organization", "corporation", "localbusiness", "store", "hardwarestore", "homeandconstructionbusiness",
    "professionalservice", "onlinestore", "wholesalestore",
}

MARCAS_DESAFIO = (
    "_cf_chl_opt", "cf-browser-verification", "cf_chl_", "/.well-known/sgcaptcha", "sgcaptcha", "ddos-guard",
    "_incapsula_resource", "incapsula incident", "sucuri website firewall", "px-captcha",
    "access to this site has been limited", "access denied by imunify360", "imunify360-webshield",
    "checking your browser", "verify you are human", "verifica que eres humano", "compruebe que es humano",
)
TITULOS_DESAFIO = (
    "just a moment", "un momento", "attention required", "access denied", "acceso denegado", "security check",
    "robot check", "are you a robot", "verificación de seguridad", "captcha",
)


class SitioBloqueado(Exception):
    """El sitio respondió con un bloqueo y se debe detener sin reintentar."""


class Detencion(Exception):
    """El rastreo termina con un estado distinto de bloqueado."""

    def __init__(self, estado: str, motivo: str):
        super().__init__(motivo)
        self.estado = estado
        self.motivo = motivo


def limpiar(valor, maximo: int = 200) -> str:
    return " ".join(str(valor or "").split())[:maximo]


def unicos(valores, maximo: int | None = None) -> list:
    vistos, salida = set(), []
    for valor in valores:
        if not valor:
            continue
        clave = valor.casefold() if isinstance(valor, str) else valor
        if clave not in vistos:
            vistos.add(clave)
            salida.append(valor)
        if maximo is not None and len(salida) >= maximo:
            break
    return salida


def normalizar_url(url: str) -> str | None:
    """Devuelve una URL http(s) sin fragmento ni parámetros de seguimiento, o None si no es válida."""
    try:
        partes = urlsplit((url or "").strip())
        puerto = partes.port
    except ValueError:
        return None
    if partes.scheme not in ("http", "https") or not partes.hostname:
        return None
    netloc = partes.hostname.lower() + (f":{puerto}" if puerto else "")
    parametros = [(k, v) for k, v in parse_qsl(partes.query, keep_blank_values=True) if not PARAMETROS_SEGUIMIENTO.match(k)]
    return urlunsplit((partes.scheme, netloc, partes.path or "/", urlencode(parametros), ""))


def es_variante_www(a: str, b: str) -> bool:
    return a == b or a == f"www.{b}" or b == f"www.{a}"


def admisible(url: str) -> bool:
    """Descarta recursos no HTML y toda ruta de sesión, transacción o búsqueda."""
    partes = urlsplit(url)
    if partes.path.lower().endswith(EXTENSIONES_NO_HTML) or RUTA_EXCLUIDA.search(partes.path):
        return False
    return not any(PARAMETROS_EXCLUIDOS.match(clave) for clave, _ in parse_qsl(partes.query, keep_blank_values=True))


def seccion_de(url: str) -> str:
    segmentos = [s for s in urlsplit(url).path.split("/") if s]
    return segmentos[0].lower() if segmentos else "/"


def puntaje_base(url: str) -> int:
    partes = urlsplit(url)
    objetivo = f"{partes.path}?{partes.query}"
    puntos = max((valor for patron, valor in REGLAS_PRIORIDAD if patron.search(objetivo)), default=0)
    return puntos - 50 if RUTA_BAJA_PRIORIDAD.search(partes.path) else puntos


def detectar_bloqueo(status: int, cabeceras: dict, cuerpo: bytes) -> str | None:
    """Devuelve el motivo si la respuesta es un bloqueo, captcha o página de desafío."""
    if status in (403, 429):
        return f"El sitio respondió HTTP {status}"
    if "challenge" in str(cabeceras.get("cf-mitigated", "")).lower():
        return "Cabecera de desafío cf-mitigated"
    muestra = cuerpo[:20000].decode("utf-8", errors="ignore").lower()
    for marca in MARCAS_DESAFIO:
        if marca in muestra:
            return f"Página de desafío detectada ({marca})"
    coincidencia = re.search(r"<title[^>]*>(.*?)</title>", muestra, re.DOTALL)
    titulo = " ".join(coincidencia.group(1).split()) if coincidencia else ""
    if any(titulo.startswith(marca) or (marca == "captcha" and marca in titulo) for marca in TITULOS_DESAFIO):
        return f"Título de página de desafío: {titulo[:80]}"
    # Un captcha en una página pequeña es un muro; en una página completa suele ser un formulario de contacto.
    if len(cuerpo) < 8000 and "captcha" in muestra:
        return "Captcha detectado en una página mínima"
    return None


def nodos_jsonld(dato):
    """Recorre un bloque JSON-LD y entrega cada objeto con @type o nombre."""
    if isinstance(dato, list):
        for elemento in dato:
            yield from nodos_jsonld(elemento)
    elif isinstance(dato, dict):
        yield dato
        for valor in dato.values():
            if isinstance(valor, (dict, list)):
                yield from nodos_jsonld(valor)


def tipos_de(nodo: dict) -> list[str]:
    tipo = nodo.get("@type")
    if isinstance(tipo, str):
        return [tipo]
    return [t for t in tipo if isinstance(t, str)] if isinstance(tipo, list) else []


def direccion_a_texto(direccion) -> str:
    if isinstance(direccion, str):
        return limpiar(direccion)
    if isinstance(direccion, dict):
        campos = ("streetAddress", "addressLocality", "addressRegion", "addressCountry")
        return limpiar(", ".join(str(direccion[c]) for c in campos if isinstance(direccion.get(c), str)))
    return ""


def extraer_jsonld(respuesta) -> dict:
    tipos, productos, migas, telefonos, correos, direcciones, empresas = [], [], [], [], [], [], []
    for bloque in respuesta.css('script[type="application/ld+json"]::text').getall():
        try:
            dato = json.loads(str(bloque), strict=False)
        except ValueError:
            tipos.extend(re.findall(r'"@type"\s*:\s*"([^"]+)"', str(bloque)))
            continue
        for nodo in nodos_jsonld(dato):
            tipos_nodo = tipos_de(nodo)
            tipos.extend(tipos_nodo)
            minusculas = {t.lower() for t in tipos_nodo}
            if "product" in minusculas:
                productos.append(limpiar(nodo.get("name")))
            if "breadcrumblist" in minusculas:
                for elemento in nodo.get("itemListElement") or []:
                    if isinstance(elemento, dict):
                        item = elemento.get("item")
                        nombre = elemento.get("name") or (item.get("name") if isinstance(item, dict) else None)
                        migas.append(limpiar(nombre, 120))
            # Solo datos a nivel de empresa. Los nodos Person no se leen.
            if minusculas & TIPOS_EMPRESA:
                empresas.append(limpiar(nodo.get("name"), 160))
                telefonos.append(limpiar(nodo.get("telephone"), 40))
                correo = limpiar(nodo.get("email"), 120).removeprefix("mailto:")
                if CORREO_DE_EMPRESA.match(correo):
                    correos.append(correo.lower())
                direcciones.append(direccion_a_texto(nodo.get("address")))
    return {
        "tipos": unicos(tipos), "productos": unicos(productos), "migas": unicos(migas), "telefonos": unicos(telefonos),
        "correos": unicos(correos), "direcciones": unicos(direcciones), "empresas": unicos(empresas),
    }


def extraer_normas(texto: str) -> list[str]:
    encontradas = []
    for patron in PATRONES_NORMA:
        for coincidencia in patron.findall(texto):
            norma = " ".join(coincidencia.split())
            if not ANIO_COMO_NORMA.match(norma):
                encontradas.append(norma)
    return sorted(unicos(encontradas))


def textos(respuesta, selector: str, maximo: int = 200) -> list[str]:
    return [limpiar(e.get_all_text(separator=" ", strip=True), maximo) for e in respuesta.css(selector)]


def extraer_especificaciones(respuesta, es_producto: bool) -> list[dict]:
    """Lee pares atributo-valor de tablas de atributos y, en fichas de producto, de tablas y listas."""
    filas = list(respuesta.css("table.shop_attributes tr, table.woocommerce-product-attributes tr"))
    if es_producto:
        filas += list(respuesta.css("table tr"))
    pares = []
    for fila in filas:
        celdas = [limpiar(c.get_all_text(separator=" ", strip=True), 120) for c in fila.css("th, td")]
        if len(celdas) == 2 and all(celdas) and CLAVE_ESPEC.match(celdas[0]) and not CLAVE_NO_ESPEC.search(celdas[0]):
            pares.append((celdas[0], celdas[1]))
    if es_producto:
        for elemento in respuesta.css("li"):
            coincidencia = ESPEC_EN_LISTA.match(limpiar(elemento.get_all_text(separator=" ", strip=True), 170))
            if coincidencia and CLAVE_ESPEC.match(coincidencia[1]) and not CLAVE_NO_ESPEC.search(coincidencia[1]):
                pares.append((coincidencia[1].strip(), coincidencia[2].strip()))
    salida, vistos = [], set()
    for clave, valor in pares:
        if (clave.casefold(), valor.casefold()) not in vistos:
            vistos.add((clave.casefold(), valor.casefold()))
            salida.append({"atributo": clave, "valor": valor})
        if len(salida) >= MAX_ESPECIFICACIONES:
            break
    return salida


def extraer_productos(respuesta, es_producto: bool, h1: list[str], jsonld: dict) -> list[str]:
    nombres = list(jsonld["productos"])
    for selector in SELECTORES_PRODUCTO:
        nombres.extend(textos(respuesta, selector))
    if es_producto and h1:
        nombres.insert(0, h1[0])
    return unicos(nombres, MAX_PRODUCTOS_PAGINA)


def extraer_categorias(respuesta, jsonld: dict) -> list[str]:
    nombres = list(jsonld["migas"])
    for selector in SELECTORES_CATEGORIA:
        nombres.extend(textos(respuesta, selector, 120))
    for enlace in respuesta.css("a[href]"):
        if HREF_CATEGORIA.search(str(enlace.attrib.get("href", ""))):
            nombres.append(limpiar(enlace.get_all_text(separator=" ", strip=True), 120))
    return unicos(nombres, MAX_CATEGORIAS_PAGINA)


class Rastreador:
    def __init__(self, inicio: str, max_paginas: int, intervalo: float, max_segundos: int):
        self.inicio = inicio
        partes = urlsplit(inicio)
        self.esquema, self.netloc = partes.scheme, partes.netloc
        self.max_paginas = max(1, min(max_paginas, MAX_PAGINAS))
        self.intervalo = max(intervalo, INTERVALO_MINIMO)
        self.max_segundos = max_segundos
        self.robots: Protego | None = None
        self.info_robots: dict = {}
        self.ultima_solicitud: float | None = None
        self.solicitudes = 0
        self.pedidas = 0
        self.pendientes: dict[str, int] = {}
        self.vistas: set[str] = set()
        self.por_seccion: Counter = Counter()
        self.paginas: list[dict] = []
        self.omitidas: list[str] = []
        self.externas: list[str] = []
        self.documentos: list[str] = []
        self.telefonos: list[str] = []
        self.correos: list[str] = []
        self.direcciones: list[str] = []
        self.empresas: list[str] = []
        self.errores_seguidos = 0
        self.truncado_por_tiempo = False
        self.inicio_reloj = time.monotonic()

    def solicitar(self, url: str):
        """Única salida a la red. Espera el intervalo, un solo intento y sin seguir redirecciones."""
        if self.ultima_solicitud is not None:
            restante = self.intervalo - (time.monotonic() - self.ultima_solicitud)
            if restante > 0:
                time.sleep(restante)
        self.solicitudes += 1
        try:
            return Fetcher.get(
                url,
                headers=dict(CABECERAS),
                impersonate=None,
                stealthy_headers=False,
                follow_redirects=False,
                retries=1,
                timeout=TIEMPO_ESPERA_HTTP,
            )
        finally:
            self.ultima_solicitud = time.monotonic()

    @staticmethod
    def cabeceras_de(respuesta) -> dict:
        return {str(k).lower(): v for k, v in (respuesta.headers or {}).items()}

    def misma_web(self, url: str) -> bool:
        partes = urlsplit(url)
        return partes.netloc == self.netloc or es_variante_www(partes.netloc, self.netloc)

    def canonizar(self, url: str) -> str:
        partes = urlsplit(url)
        return urlunsplit((self.esquema, self.netloc, partes.path, partes.query, ""))

    def cargar_robots(self) -> None:
        url = urlunsplit((self.esquema, self.netloc, "/robots.txt", "", ""))
        for _ in range(MAX_SALTOS_ROBOTS + 1):
            try:
                respuesta = self.solicitar(url)
            except Exception as error:  # noqa: BLE001 - un fallo de red termina el sitio sin reintentos
                raise Detencion("error", f"No se pudo leer robots.txt: {type(error).__name__}") from error
            status, cabeceras, cuerpo = respuesta.status, self.cabeceras_de(respuesta), bytes(respuesta.body or b"")
            motivo = detectar_bloqueo(status, cabeceras, cuerpo)
            if motivo:
                self.info_robots = {"url": url, "http_status": status}
                raise SitioBloqueado(f"robots.txt: {motivo}")
            if status in (301, 302, 303, 307, 308):
                destino = normalizar_url(urljoin(url, str(cabeceras.get("location", ""))))
                if not destino or not self.misma_web(destino):
                    raise Detencion("robots_no_disponible", "robots.txt redirige fuera del sitio")
                url = destino
                continue
            self.info_robots = {"url": url, "http_status": status, "presente": status == 200}
            if status >= 500:
                # RFC 9309: si robots.txt no está disponible por error del servidor se asume prohibición total.
                raise Detencion("robots_no_disponible", f"robots.txt respondió HTTP {status}")
            self.robots = Protego.parse(cuerpo[:MAX_BYTES_ROBOTS].decode("utf-8", errors="ignore") if status == 200 else "")
            self.aplicar_demoras()
            return
        raise Detencion("robots_no_disponible", "robots.txt con demasiadas redirecciones")

    def aplicar_demoras(self) -> None:
        demora = self.robots.crawl_delay(USER_AGENT)
        tasa = self.robots.request_rate(USER_AGENT)
        if demora:
            self.intervalo = max(self.intervalo, float(demora))
        if tasa and tasa.requests:
            self.intervalo = max(self.intervalo, float(tasa.seconds) / tasa.requests)
        self.info_robots.update(
            {
                "crawl_delay": float(demora) if demora else None,
                "sitemaps": [s for s in self.robots.sitemaps][:20],
            }
        )

    def permitido(self, url: str) -> bool:
        return self.robots.can_fetch(url, USER_AGENT)

    def encolar(self, url: str) -> None:
        if url not in self.vistas and url not in self.pendientes:
            self.pendientes[url] = puntaje_base(url)

    def siguiente(self) -> str:
        # Cada página ya visitada en una sección resta un punto, para no agotar el cupo en una sola rama.
        url = max(self.pendientes, key=lambda u: self.pendientes[u] - self.por_seccion[seccion_de(u)])
        del self.pendientes[url]
        return url

    def registrar_omitida(self, url: str) -> None:
        if len(self.omitidas) < MAX_OMITIDAS:
            self.omitidas.append(url)

    def manejar_redireccion(self, url: str, cabeceras: dict, es_primera: bool) -> None:
        destino = normalizar_url(urljoin(url, str(cabeceras.get("location", ""))))
        if not destino:
            return
        if not self.misma_web(destino):
            self.externas.append(destino)
            if es_primera:
                raise Detencion("redireccion_externa", f"La URL inicial redirige a otro dominio: {destino}")
            return
        partes = urlsplit(destino)
        if es_primera and (partes.netloc != self.netloc or partes.scheme != self.esquema):
            # La URL inicial se traslada a https o a la variante www. El nuevo host requiere su propio robots.txt.
            cambia_host = partes.netloc != self.netloc
            self.esquema, self.netloc = partes.scheme, partes.netloc
            if cambia_host:
                self.cargar_robots()
        canonica = self.canonizar(destino)
        if admisible(canonica):
            self.encolar(canonica)
            # La página de destino hereda prioridad para no perder la portada tras la redirección.
            if canonica in self.pendientes:
                self.pendientes[canonica] += 200

    def extraer_pagina(self, url: str, respuesta, cuerpo: bytes) -> dict:
        es_producto = bool(RUTA_DE_PRODUCTO.search(url))
        jsonld = extraer_jsonld(respuesta)
        h1 = unicos(textos(respuesta, "h1"), 5)
        descripcion = (
            respuesta.css('meta[name="description"]::attr(content)').get()
            or respuesta.css('meta[name="Description"]::attr(content)').get()
            or respuesta.css('meta[property="og:description"]::attr(content)').get()
        )
        internos: list[str] = []
        for href in respuesta.css("a::attr(href)").getall():
            absoluta = normalizar_url(urljoin(url, str(href)))
            if not absoluta or not self.misma_web(absoluta):
                continue
            canonica = self.canonizar(absoluta)
            partes = urlsplit(canonica)
            ruta = partes.path + (f"?{partes.query}" if partes.query else "")
            internos.append(ruta)
            if partes.path.lower().endswith(EXTENSIONES_DOCUMENTO):
                self.documentos.append(canonica)
            elif admisible(canonica):
                self.encolar(canonica)
        enlaces_unicos = unicos(internos)
        for telefono in respuesta.css('a[href^="tel:"]::attr(href)').getall():
            self.telefonos.append(limpiar(str(telefono).removeprefix("tel:"), 40))
        for correo in respuesta.css('a[href^="mailto:"]::attr(href)').getall():
            direccion = limpiar(str(correo).removeprefix("mailto:").split("?")[0], 120)
            if CORREO_DE_EMPRESA.match(direccion):
                self.correos.append(direccion.lower())
        self.telefonos.extend(jsonld["telefonos"])
        self.correos.extend(jsonld["correos"])
        self.direcciones.extend(jsonld["direcciones"])
        self.empresas.extend(jsonld["empresas"])
        texto_visible = str(respuesta.get_all_text(separator=" ", strip=True))
        return {
            "url": url,
            "http_status": respuesta.status,
            "titulo": limpiar(respuesta.css("title::text").get(), 300),
            "meta_descripcion": limpiar(descripcion, 500),
            "canonica": limpiar(respuesta.css('link[rel="canonical"]::attr(href)').get(), 500),
            "idioma": limpiar(respuesta.css("html::attr(lang)").get(), 20),
            "h1": h1,
            "h2": unicos(textos(respuesta, "h2"), MAX_H2),
            "es_ficha_producto": es_producto,
            "productos": extraer_productos(respuesta, es_producto, h1, jsonld),
            "categorias": extraer_categorias(respuesta, jsonld),
            "especificaciones": extraer_especificaciones(respuesta, es_producto),
            "normas_citadas": extraer_normas(f"{texto_visible} {respuesta.css('title::text').get() or ''}"),
            "tipos_jsonld": jsonld["tipos"],
            "total_enlaces_internos": len(enlaces_unicos),
            "enlaces_internos": enlaces_unicos[:MAX_ENLACES_PAGINA],
            "bytes_html": len(cuerpo),
        }

    def procesar(self, url: str, es_primera: bool) -> None:
        self.pedidas += 1
        self.por_seccion[seccion_de(url)] += 1
        try:
            respuesta = self.solicitar(url)
        except Exception as error:  # noqa: BLE001 - se registra y no se reintenta
            self.errores_seguidos += 1
            self.paginas.append({"url": url, "error": type(error).__name__})
            if es_primera or self.errores_seguidos >= MAX_ERRORES_SEGUIDOS:
                raise Detencion("error", f"Fallo de red: {type(error).__name__}") from error
            return
        status, cabeceras, cuerpo = respuesta.status, self.cabeceras_de(respuesta), bytes(respuesta.body or b"")
        motivo = detectar_bloqueo(status, cabeceras, cuerpo)
        if motivo:
            self.paginas.append({"url": url, "http_status": status, "bloqueo": motivo})
            raise SitioBloqueado(motivo)
        if status in (301, 302, 303, 307, 308):
            self.errores_seguidos = 0
            self.manejar_redireccion(url, cabeceras, es_primera)
            return
        if status != 200:
            self.errores_seguidos += 1
            self.paginas.append({"url": url, "http_status": status})
            if status >= 500 and self.errores_seguidos >= MAX_ERRORES_SEGUIDOS:
                raise Detencion("error", f"{self.errores_seguidos} errores seguidos del servidor")
            return
        self.errores_seguidos = 0
        tipo = str(cabeceras.get("content-type", "")).lower()
        if tipo and "html" not in tipo:
            self.paginas.append({"url": url, "http_status": status, "omitida": f"Contenido no HTML: {tipo[:60]}"})
            return
        self.paginas.append(self.extraer_pagina(url, respuesta, cuerpo))

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
                # Sigue siendo "primera" mientras la URL inicial solo encadene redirecciones (http, https, www).
                primera = not self.paginas
        except SitioBloqueado as bloqueo:
            return "bloqueado", str(bloqueo)
        except Detencion as detencion:
            return detencion.estado, detencion.motivo
        if not any(p.get("http_status") == 200 and "titulo" in p for p in self.paginas):
            return "sin_paginas", "No se obtuvo ninguna página HTML"
        return "ok", ""

    def resultado(self, estado: str, motivo: str) -> dict:
        utiles = [p for p in self.paginas if "titulo" in p]
        return {
            "url_inicial": self.inicio,
            "host": self.netloc,
            "esquema": self.esquema,
            "user_agent": USER_AGENT,
            "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "estado": estado,
            "motivo": motivo,
            "limites": {"max_paginas": self.max_paginas, "intervalo_segundos": self.intervalo},
            "robots": self.info_robots,
            "solicitudes_http": self.solicitudes,
            "paginas_solicitadas": self.pedidas,
            "paginas_con_datos": len(utiles),
            "truncado_por_tiempo": self.truncado_por_tiempo,
            "pendientes_sin_visitar": len(self.pendientes),
            "omitidas_por_robots": self.omitidas,
            "redirecciones_externas": unicos(self.externas, 50),
            "duracion_segundos": round(time.monotonic() - self.inicio_reloj, 1),
            "resumen": {
                "productos": unicos((n for p in utiles for n in p["productos"]), 400),
                "categorias": unicos((n for p in utiles for n in p["categorias"]), 150),
                "normas_citadas": sorted(unicos(n for p in utiles for n in p["normas_citadas"])),
                "tipos_jsonld": dict(Counter(t for p in utiles for t in p["tipos_jsonld"]).most_common()),
                "secciones": dict(Counter(seccion_de(p["url"]) for p in utiles).most_common()),
                "documentos_enlazados": unicos(self.documentos, MAX_DOCUMENTOS),
                "contacto_empresa": {
                    "nombres": unicos(self.empresas, MAX_CONTACTOS),
                    "telefonos": unicos(self.telefonos, MAX_CONTACTOS),
                    "correos": unicos(self.correos, MAX_CONTACTOS),
                    "direcciones": unicos(self.direcciones, MAX_CONTACTOS),
                },
            },
            "paginas": self.paginas,
        }


def guardar(ruta: str, datos: dict) -> None:
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


def main() -> int:
    analizador = argparse.ArgumentParser(description="Rastrea datos públicos de un sitio y los guarda en JSON.")
    analizador.add_argument("url_inicial", help="URL http(s) donde empieza el rastreo")
    analizador.add_argument("salida", help="Ruta del archivo JSON de salida")
    analizador.add_argument("--max-paginas", type=int, default=MAX_PAGINAS, help="Páginas por sitio; nunca supera 40")
    analizador.add_argument("--intervalo", type=float, default=INTERVALO_MINIMO, help="Segundos entre solicitudes; nunca menos de 3")
    analizador.add_argument("--max-segundos", type=int, default=TIEMPO_MAXIMO_POR_DEFECTO, help="Tiempo máximo por sitio")
    argumentos = analizador.parse_args()

    inicio = normalizar_url(argumentos.url_inicial)
    if not inicio:
        analizador.error("La URL inicial debe ser http o https")

    rastreador = Rastreador(inicio, argumentos.max_paginas, argumentos.intervalo, argumentos.max_segundos)
    estado, motivo = rastreador.ejecutar()
    datos = rastreador.resultado(estado, motivo)
    guardar(argumentos.salida, datos)
    print(
        json.dumps(
            {
                "estado": estado,
                "motivo": motivo,
                "paginas_con_datos": datos["paginas_con_datos"],
                "solicitudes_http": datos["solicitudes_http"],
                "salida": argumentos.salida,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
