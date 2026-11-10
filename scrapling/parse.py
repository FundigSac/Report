"""Funciones puras de análisis para el estudio de competencia de FUNDIGSAC.

Nada de este módulo hace solicitudes de red, lee el reloj ni escribe en disco.
Reciben un `scrapling.parser.Selector` (o texto, bytes y URL) y devuelven datos.
Así se pueden probar con HTML sintético (ver `test_parse.py` y `fixtures/`).
"""
from __future__ import annotations

import json
import re
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit

MAX_H2 = 30
MAX_PRODUCTOS_PAGINA = 100
MAX_CATEGORIAS_PAGINA = 60
MAX_ESPECIFICACIONES = 40
MAX_ENLACES_PAGINA = 80

EXTENSIONES_NO_HTML = (
    ".pdf", ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico", ".bmp", ".zip", ".rar", ".7z", ".gz",
    ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".dwg", ".mp4", ".mp3", ".avi", ".mov", ".webm",
    ".css", ".js", ".json", ".xml", ".txt", ".woff", ".woff2", ".ttf", ".eot",
)
EXTENSIONES_DOCUMENTO = (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".dwg")

# Rutas que implican sesión, transacción o búsqueda. Nunca se solicitan.
# Respecto de la versión del 9-nov se añaden `sesion` y `carrito<N>` (pendiente 4 del informe).
RUTA_EXCLUIDA = re.compile(
    r"(^|/)(wp-admin|wp-login(\.php)?|wp-json|xmlrpc\.php|cgi-bin|admin|administrator|login|logout|signin|sign-in|"
    r"signup|sign-up|register|registro|acceder|ingresar|iniciar-sesion|sesion|my-account|mi-cuenta|cuenta|account|"
    r"cart|carrito\d*|carro|checkout|finalizar-compra|pago|wishlist|lista-de-deseos|compare|comparar|search|"
    r"buscar|busqueda|feed|comments|trackback)(/|\.php|\.html|$)",
    re.IGNORECASE,
)
PARAMETROS_EXCLUIDOS = re.compile(
    r"^(s|q|search|buscar|busqueda|query|term|add-to-cart|add_to_wishlist|orderby|order|sort|min_price|max_price|"
    r"filter_.*|replytocom|share|action|login|logout|redirect_to|return_url|wc-ajax|rating_filter|view)$",
    re.IGNORECASE,
)
PARAMETROS_SEGUIMIENTO = re.compile(r"^(utm_.*|gclid|fbclid|msclkid|_ga|mc_cid|mc_eid)$", re.IGNORECASE)

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
# Ficha de producto. A diferencia de la versión del 9-nov, `/productos/categoria/...` y `/productos/page/N` no cuentan como ficha.
RUTA_DE_PRODUCTO = re.compile(
    r"(/productos?/(?!categor|category/|page/)[^/?#]+|/products?/(?!categor|category/|page/)[^/?#]+|producto\.php)",
    re.IGNORECASE,
)
HREF_CATEGORIA = re.compile(r"(categoria-producto|product-category|/categorias?/|/category/|categoria\.php)", re.IGNORECASE)

# Normas con mayúsculas exactas para no confundir la preposición "en" con la norma EN.
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

# Solo buzones genéricos de empresa. Un correo con nombre de persona se descarta.
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
SELECTORES_CATEGORIA = (".posted_in a", ".product_cat a", ".woocommerce-breadcrumb a", ".breadcrumb a", ".breadcrumbs a")
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


# --------------------------------------------------------------------------- utilidades de texto y URL

def limpiar(valor, maximo: int = 200) -> str:
    return " ".join(str(valor or "").split())[:maximo]


def unicos(valores, maximo: int | None = None) -> list:
    """Quita vacíos y duplicados (sin distinguir mayúsculas) conservando el orden."""
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
    """URL http(s) sin fragmento ni parámetros de seguimiento, o None si no es válida."""
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


def es_ficha_producto(url: str) -> bool:
    """True si la ruta parece una ficha. Las páginas de categoría o de paginación no cuentan."""
    return bool(RUTA_DE_PRODUCTO.search(urlsplit(url).path))


def seccion_de(url: str) -> str:
    segmentos = [s for s in urlsplit(url).path.split("/") if s]
    return segmentos[0].lower() if segmentos else "/"


def puntaje_base(url: str) -> int:
    partes = urlsplit(url)
    objetivo = f"{partes.path}?{partes.query}"
    puntos = max((valor for patron, valor in REGLAS_PRIORIDAD if patron.search(objetivo)), default=0)
    return puntos - 50 if RUTA_BAJA_PRIORIDAD.search(partes.path) else puntos


def detectar_bloqueo(status: int, cabeceras: dict, cuerpo: bytes) -> str | None:
    """Motivo si la respuesta es un bloqueo, captcha o página de desafío; None en otro caso."""
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


def extraer_normas(texto: str) -> list[str]:
    encontradas = []
    for patron in PATRONES_NORMA:
        for coincidencia in patron.findall(texto):
            norma = " ".join(coincidencia.split())
            if not ANIO_COMO_NORMA.match(norma):
                encontradas.append(norma)
    return sorted(unicos(encontradas))


# --------------------------------------------------------------------------- JSON-LD

def nodos_jsonld(dato):
    """Recorre un bloque JSON-LD y entrega cada objeto anidado."""
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


def analizar_jsonld(bloques: list[str]) -> dict:
    """Tipos, productos, migas y contacto de empresa a partir de los textos de los bloques JSON-LD."""
    tipos, productos, migas, telefonos, correos, direcciones, empresas = [], [], [], [], [], [], []
    for bloque in bloques:
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
            # Solo datos de empresa. Los nodos Person no se leen.
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


# --------------------------------------------------------------------------- extracción sobre un Selector

def textos(sel, selector: str, maximo: int = 200) -> list[str]:
    return [limpiar(e.get_all_text(separator=" ", strip=True), maximo) for e in sel.css(selector)]


def extraer_jsonld(sel) -> dict:
    return analizar_jsonld([str(b) for b in sel.css('script[type="application/ld+json"]::text').getall()])


def extraer_especificaciones(sel, es_producto: bool) -> list[dict]:
    """Pares atributo-valor de tablas de atributos y, en fichas de producto, de tablas y listas."""
    filas = list(sel.css("table.shop_attributes tr, table.woocommerce-product-attributes tr"))
    if es_producto:
        filas += list(sel.css("table tr"))
    pares = []
    for fila in filas:
        celdas = [limpiar(c.get_all_text(separator=" ", strip=True), 120) for c in fila.css("th, td")]
        if len(celdas) == 2 and all(celdas) and CLAVE_ESPEC.match(celdas[0]) and not CLAVE_NO_ESPEC.search(celdas[0]):
            pares.append((celdas[0], celdas[1]))
    if es_producto:
        for elemento in sel.css("li"):
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


def extraer_productos(sel, es_producto: bool, h1: list[str], jsonld: dict) -> list[str]:
    nombres = list(jsonld["productos"])
    for selector in SELECTORES_PRODUCTO:
        nombres.extend(textos(sel, selector))
    if es_producto and h1:
        nombres.insert(0, h1[0])
    return unicos(nombres, MAX_PRODUCTOS_PAGINA)


def extraer_categorias(sel, jsonld: dict) -> list[str]:
    nombres = list(jsonld["migas"])
    for selector in SELECTORES_CATEGORIA:
        nombres.extend(textos(sel, selector, 120))
    for enlace in sel.css("a[href]"):
        if HREF_CATEGORIA.search(str(enlace.attrib.get("href", ""))):
            nombres.append(limpiar(enlace.get_all_text(separator=" ", strip=True), 120))
    return unicos(nombres, MAX_CATEGORIAS_PAGINA)


def extraer_enlaces(sel, url: str, esquema: str, host: str) -> dict:
    """Clasifica los enlaces: rutas internas, documentos, candidatas a visitar y externas.

    `esquema` y `host` son los del sitio rastreado; los enlaces a la variante con o sin `www` cuentan como internos
    y se reescriben con ese esquema y host.
    """
    internos, documentos, candidatas, externas = [], [], [], []
    for href in sel.css("a::attr(href)").getall():
        absoluta = normalizar_url(urljoin(url, str(href)))
        if not absoluta:
            continue
        partes = urlsplit(absoluta)
        if not es_variante_www(partes.netloc, host):
            externas.append(absoluta)
            continue
        canonica = urlunsplit((esquema, host, partes.path, partes.query, ""))
        internos.append(partes.path + (f"?{partes.query}" if partes.query else ""))
        if partes.path.lower().endswith(EXTENSIONES_DOCUMENTO):
            documentos.append(canonica)
        elif admisible(canonica):
            candidatas.append(canonica)
    return {
        "internos": unicos(internos), "documentos": unicos(documentos),
        "candidatas": unicos(candidatas), "externas": unicos(externas),
    }


def extraer_contacto(sel, jsonld: dict) -> dict:
    """Teléfonos y buzones genéricos de empresa. Los correos personales se descartan."""
    telefonos = [limpiar(str(t).removeprefix("tel:"), 40) for t in sel.css('a[href^="tel:"]::attr(href)').getall()]
    correos = []
    for correo in sel.css('a[href^="mailto:"]::attr(href)').getall():
        direccion = limpiar(str(correo).removeprefix("mailto:").split("?")[0], 120)
        if CORREO_DE_EMPRESA.match(direccion):
            correos.append(direccion.lower())
    return {
        "telefonos": unicos(telefonos + jsonld["telefonos"]),
        "correos": unicos(correos + jsonld["correos"]),
        "direcciones": jsonld["direcciones"],
        "empresas": jsonld["empresas"],
    }


def parsear_pagina(sel, url: str, status: int, bytes_html: int, esquema: str, host: str) -> tuple[dict, dict]:
    """Analiza una página HTML. Devuelve (registro de página, extras para el agregado del sitio)."""
    es_producto = es_ficha_producto(url)
    jsonld = extraer_jsonld(sel)
    h1 = unicos(textos(sel, "h1"), 5)
    descripcion = (
        sel.css('meta[name="description"]::attr(content)').get()
        or sel.css('meta[name="Description"]::attr(content)').get()
        or sel.css('meta[property="og:description"]::attr(content)').get()
    )
    enlaces = extraer_enlaces(sel, url, esquema, host)
    titulo = sel.css("title::text").get() or ""
    texto_visible = str(sel.get_all_text(separator=" ", strip=True))
    pagina = {
        "url": url,
        "http_status": status,
        "titulo": limpiar(titulo, 300),
        "meta_descripcion": limpiar(descripcion, 500),
        "canonica": limpiar(sel.css('link[rel="canonical"]::attr(href)').get(), 500),
        "idioma": limpiar(sel.css("html::attr(lang)").get(), 20),
        "h1": h1,
        "h2": unicos(textos(sel, "h2"), MAX_H2),
        "es_ficha_producto": es_producto,
        "productos": extraer_productos(sel, es_producto, h1, jsonld),
        "categorias": extraer_categorias(sel, jsonld),
        "especificaciones": extraer_especificaciones(sel, es_producto),
        "normas_citadas": extraer_normas(f"{texto_visible} {titulo}"),
        "tipos_jsonld": jsonld["tipos"],
        "total_enlaces_internos": len(enlaces["internos"]),
        "enlaces_internos": enlaces["internos"][:MAX_ENLACES_PAGINA],
        "documentos_enlazados": enlaces["documentos"],
        "bytes_html": bytes_html,
    }
    extras = {"candidatas": enlaces["candidatas"], "externas": enlaces["externas"], **extraer_contacto(sel, jsonld)}
    return pagina, extras
