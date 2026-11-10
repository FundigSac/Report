"""Pruebas de las funciones puras de `parse.py`, del exportador y de las reglas de red de `fetch.py`.

Usan HTML sintético de `fixtures/` y un cliente HTTP simulado: ninguna prueba sale a internet.
Ejecutar desde esta carpeta:  python -m pytest -q

NOTA: estas pruebas se escribieron el 10-nov-2026 en una máquina sin Python y NO se han ejecutado todavía.
"""
from __future__ import annotations

from pathlib import Path

import pytest

import export
import fetch
import parse

FIXTURES = Path(__file__).parent / "fixtures"
URL_FICHA = "https://www.ejemplo.pe/producto/valvula-compuerta-dn100/"
URL_CATEGORIA = "https://www.ejemplo.pe/categoria-producto/valvulas/"
HOST = "www.ejemplo.pe"


def selector(nombre: str, url: str):
    from scrapling.parser import Selector

    return Selector(content=(FIXTURES / nombre).read_text(encoding="utf-8"), url=url)


@pytest.fixture(scope="module")
def ficha():
    return selector("ficha_producto.html", URL_FICHA)


@pytest.fixture(scope="module")
def categoria():
    return selector("categoria.html", URL_CATEGORIA)


# --------------------------------------------------------------------------- URL y filtros

def test_normalizar_url_quita_seguimiento_y_fragmento():
    assert parse.normalizar_url("HTTPS://Ejemplo.PE/a?utm_source=x&id=3#arriba") == "https://ejemplo.pe/a?id=3"
    assert parse.normalizar_url("https://ejemplo.pe") == "https://ejemplo.pe/"


@pytest.mark.parametrize("url", ["mailto:info@ejemplo.pe", "tel:+51100", "javascript:void(0)", "ftp://ejemplo.pe/", ""])
def test_normalizar_url_rechaza_esquemas_no_http(url):
    assert parse.normalizar_url(url) is None


@pytest.mark.parametrize(
    "url, esperado",
    [
        ("https://x.pe/producto/valvula/", True),
        ("https://x.pe/catalogo.pdf", False),
        ("https://x.pe/carrito/", False),
        ("https://x.pe/carrito8.php", False),
        ("https://x.pe/sesion.php", False),
        ("https://x.pe/wp-admin/", False),
        ("https://x.pe/?s=valvula", False),
        ("https://x.pe/tienda/?orderby=price", False),
        ("https://x.pe/categoria-producto/valvulas/?page=2", True),
    ],
)
def test_admisible(url, esperado):
    assert parse.admisible(url) is esperado


@pytest.mark.parametrize(
    "url, esperado",
    [
        ("https://x.pe/producto/valvula-a/", True),
        ("https://x.pe/productos/valvula-a", True),
        ("https://x.pe/producto.php?id=5", True),
        ("https://x.pe/productos/categoria/valvulas/", False),
        ("https://x.pe/productos/page/2/", False),
        ("https://x.pe/product-category/valvulas/", False),
        ("https://x.pe/productos/", False),
    ],
)
def test_es_ficha_producto(url, esperado):
    assert parse.es_ficha_producto(url) is esperado


def test_puntaje_prioriza_categorias_y_rebaja_blog():
    assert parse.puntaje_base("https://x.pe/categoria-producto/valvulas/") == 100
    assert parse.puntaje_base("https://x.pe/producto/valvula/") == 90
    assert parse.puntaje_base("https://x.pe/blog/valvulas/") == 10  # 60 por "valvula" menos 50 por "blog"
    assert parse.puntaje_base("https://x.pe/otra/") == 0


def test_unicos_ignora_mayusculas_y_vacios():
    assert parse.unicos(["A", "a", "", None, "B", "b", "C"], maximo=2) == ["A", "B"]


# --------------------------------------------------------------------------- bloqueos

def test_detectar_bloqueo_por_estado():
    assert "429" in parse.detectar_bloqueo(429, {}, b"")
    assert "403" in parse.detectar_bloqueo(403, {}, b"<html></html>")


def test_detectar_bloqueo_pagina_de_desafio():
    cuerpo = (FIXTURES / "desafio.html").read_bytes()
    motivo = parse.detectar_bloqueo(200, {}, cuerpo)
    assert motivo is not None and "_cf_chl_opt" in motivo


def test_detectar_bloqueo_cabecera_cloudflare():
    assert parse.detectar_bloqueo(200, {"cf-mitigated": "challenge"}, b"<html></html>") is not None


def test_pagina_normal_no_es_bloqueo():
    cuerpo = (FIXTURES / "ficha_producto.html").read_bytes()
    assert parse.detectar_bloqueo(200, {}, cuerpo) is None


# --------------------------------------------------------------------------- normas

def test_extraer_normas_distingue_preposicion_y_anios():
    texto = "Según EN 1074-2, NTP 350.064 y AWWA C509. En 2019 cambió. EN 2019 no es norma. Bridas ISO 7005-2."
    assert parse.extraer_normas(texto) == ["AWWA C509", "EN 1074-2", "ISO 7005-2", "NTP 350.064"]


# --------------------------------------------------------------------------- JSON-LD

def test_analizar_jsonld_tolera_bloque_roto_y_omite_personas(ficha):
    datos = parse.extraer_jsonld(ficha)
    assert {"Product", "BreadcrumbList", "LocalBusiness", "Organization"} <= set(datos["tipos"])
    assert datos["productos"] == ["Válvula compuerta bridada DN100"]
    assert datos["migas"] == ["Inicio", "Válvulas"]
    assert datos["correos"] == ["ventas@ejemplo.pe"]
    assert datos["direcciones"] == ["Av. Prueba 123, Lima, PE"]
    assert all("persona" not in c for c in datos["correos"])


# --------------------------------------------------------------------------- ficha de producto

def test_especificaciones_de_ficha(ficha):
    assert parse.extraer_especificaciones(ficha, es_producto=True) == [
        {"atributo": "Diámetro", "valor": "DN100"},
        {"atributo": "Presión", "valor": "PN16"},
        {"atributo": "Material", "valor": "Hierro dúctil"},
    ]


def test_enlaces_clasificados(ficha):
    enlaces = parse.extraer_enlaces(ficha, URL_FICHA, "https", HOST)
    assert enlaces["documentos"] == ["https://www.ejemplo.pe/docs/ficha-dn100.pdf"]
    assert enlaces["candidatas"] == [
        "https://www.ejemplo.pe/categoria-producto/valvulas/",
        "https://www.ejemplo.pe/producto/valvula-check/",
    ]
    assert enlaces["externas"] == ["https://otro.pe/"]
    assert "/carrito/" in enlaces["internos"]  # se cuenta como enlace interno, pero nunca como candidata


def test_contacto_solo_buzones_de_empresa(ficha):
    contacto = parse.extraer_contacto(ficha, parse.extraer_jsonld(ficha))
    assert contacto["correos"] == ["info@ejemplo.pe", "ventas@ejemplo.pe"]
    assert contacto["telefonos"] == ["+5110000000", "+51 1 000 0000"]


def test_parsear_pagina_completa(ficha):
    pagina, extras = parse.parsear_pagina(ficha, URL_FICHA, 200, 2146, "https", HOST)
    assert pagina["es_ficha_producto"] is True
    assert pagina["titulo"] == "Válvula compuerta bridada DN100 | Ejemplo"
    assert pagina["idioma"] == "es"
    assert pagina["canonica"] == URL_FICHA
    assert pagina["h1"] == ["Válvula compuerta bridada DN100"]
    assert pagina["h2"] == ["Descripción"]
    assert pagina["productos"] == ["Válvula compuerta bridada DN100"]
    assert pagina["categorias"] == ["Inicio", "Válvulas"]
    assert pagina["normas_citadas"] == ["EN 1074-2", "ISO 7005-2"]
    assert pagina["meta_descripcion"].startswith("Válvula compuerta de hierro dúctil")
    assert len(extras["candidatas"]) == 2


# --------------------------------------------------------------------------- listado de categoría

def test_listado_no_es_ficha_y_no_lee_listas_como_especificacion(categoria):
    pagina, extras = parse.parsear_pagina(categoria, URL_CATEGORIA, 200, 500, "https", HOST)
    assert pagina["es_ficha_producto"] is False
    assert pagina["productos"] == ["Válvula A DN50", "Válvula B DN80"]
    assert pagina["especificaciones"] == []
    assert "https://www.ejemplo.pe/productos/page/2/" in extras["candidatas"]
    assert not any("carrito" in u or "sesion" in u for u in extras["candidatas"])


# --------------------------------------------------------------------------- exportador

DATOS_SINTETICOS = {
    "host": "www.ejemplo.pe",
    "url_inicial": "https://www.ejemplo.pe/",
    "estado": "ok",
    "motivo": "",
    "fecha_utc": "2026-11-10T00:00:00+00:00",
    "robots": {"http_status": 200},
    "trazabilidad": {"version_rastreador": "1.1.0", "solicitudes_red": 3, "aciertos_cache": 1},
    "resumen": {"productos": ["Válvula A", "Válvula B"], "normas_citadas": ["EN 124"], "documentos_enlazados": ["https://www.ejemplo.pe/a.pdf"]},
    "paginas": [
        {"url": "https://www.ejemplo.pe/", "http_status": 200, "titulo": "Inicio", "h1": ["Inicio"], "productos": [],
         "especificaciones": [], "normas_citadas": [], "tipos_jsonld": ["Organization"], "es_ficha_producto": False,
         "traza": {"desde_cache": True, "fecha_utc": "2026-11-09T12:00:00+00:00"}},
        {"url": "https://www.ejemplo.pe/producto/a/", "http_status": 200, "titulo": "A", "h1": ["A"], "productos": ["Válvula A"],
         "especificaciones": [{"atributo": "DN", "valor": "100"}], "normas_citadas": ["EN 124"], "tipos_jsonld": ["Product"],
         "es_ficha_producto": True},
        {"url": "https://www.ejemplo.pe/roto/", "http_status": 404},
    ],
}


def test_exportador_filas():
    sitio = export.fila_sitio(DATOS_SINTETICOS)
    assert sitio["paginas_con_datos"] == 2
    assert sitio["fichas_producto"] == 1
    assert sitio["fichas_con_especificaciones"] == 1
    assert sitio["paginas_con_normas"] == 1
    assert sitio["documentos_enlazados"] == 1
    paginas = export.filas_paginas(DATOS_SINTETICOS)
    assert [p["es_ficha_producto"] for p in paginas] == ["no", "si"]
    assert paginas[0]["desde_cache"] == "si" and paginas[0]["fecha_captura"] == "2026-11-09T12:00:00+00:00"
    assert paginas[1]["fecha_captura"] == "2026-11-10T00:00:00+00:00"
    assert export.filas_productos(DATOS_SINTETICOS) == [
        {"host": "www.ejemplo.pe", "producto": "Válvula A"},
        {"host": "www.ejemplo.pe", "producto": "Válvula B"},
    ]


def test_exportador_escribe_csv_y_json(tmp_path):
    import json

    origen = tmp_path / "datos"
    origen.mkdir()
    (origen / "ejemplo.json").write_text(json.dumps(DATOS_SINTETICOS), encoding="utf-8")
    (origen / "_ejecucion.json").write_text("{}", encoding="utf-8")
    resumen = export.exportar(str(origen), str(tmp_path / "export"))
    assert resumen == {"sitios": 1, "paginas": 2, "productos": 2, "destino": str(tmp_path / "export")}
    for nombre in ("sitios.csv", "paginas.csv", "productos.csv", "consolidado.json"):
        assert (tmp_path / "export" / nombre).exists()


# --------------------------------------------------------------------------- reglas de red (sin red)

class RespuestaFalsa:
    def __init__(self, status: int, body: bytes = b"<html></html>"):
        self.status = status
        self.headers = {"Content-Type": "text/html"}
        self.body = body


class ClienteFalso(fetch.Cliente):
    """Sustituye la descarga por una cola de respuestas o excepciones y usa un reloj simulado."""

    def __init__(self, cola, **kwargs):
        self.reloj_simulado = [0.0]
        self.esperas: list[float] = []

        def dormir(segundos):
            self.esperas.append(round(segundos, 3))
            self.reloj_simulado[0] += segundos

        super().__init__(reloj=lambda: self.reloj_simulado[0], dormir=dormir, **kwargs)
        self.cola = list(cola)

    def _descargar(self, url):
        elemento = self.cola.pop(0)
        if isinstance(elemento, Exception):
            raise elemento
        return elemento


def test_limites_no_se_pueden_relajar():
    cliente = fetch.Cliente(intervalo=0.5, max_intentos=10)
    assert cliente.intervalo == fetch.INTERVALO_MINIMO
    assert cliente.max_intentos == fetch.MAX_INTENTOS_TOPE


def test_reintenta_5xx_con_espera_creciente():
    cliente = ClienteFalso([RespuestaFalsa(503), RespuestaFalsa(200)], max_intentos=2)
    respuesta = cliente.obtener("https://x.pe/")
    assert respuesta.status == 200 and respuesta.intentos == 2
    assert cliente.esperas == [6.0]  # 3 s de intervalo x 2


def test_no_reintenta_429():
    cliente = ClienteFalso([RespuestaFalsa(429), RespuestaFalsa(200)], max_intentos=3)
    respuesta = cliente.obtener("https://x.pe/")
    assert respuesta.status == 429 and respuesta.intentos == 1
    assert cliente.esperas == []
    assert cliente.solicitudes_red == 1


def test_error_de_red_agota_intentos():
    cliente = ClienteFalso([ConnectionError("a"), ConnectionError("b")], max_intentos=2)
    with pytest.raises(fetch.ErrorRed):
        cliente.obtener("https://x.pe/")
    assert cliente.solicitudes_red == 2


def test_espera_entre_solicitudes_al_mismo_host():
    cliente = ClienteFalso([RespuestaFalsa(200), RespuestaFalsa(200)])
    cliente.obtener("https://x.pe/a")
    cliente.obtener("https://x.pe/b")
    assert cliente.esperas == [3.0]


def test_cache_por_dominio_evita_segunda_solicitud(tmp_path):
    cliente = ClienteFalso([RespuestaFalsa(200, b"<html>hola</html>")], dir_cache=str(tmp_path),
                           ruta_registro=str(tmp_path / "traza.jsonl"))
    primera = cliente.obtener("https://x.pe/a")
    segunda = cliente.obtener("https://x.pe/a")
    assert primera.desde_cache is False and segunda.desde_cache is True
    assert segunda.body == b"<html>hola</html>" and segunda.sha256 == primera.sha256
    assert cliente.solicitudes_red == 1 and cliente.aciertos_cache == 1
    assert (tmp_path / "x.pe").is_dir()
    assert len((tmp_path / "traza.jsonl").read_text(encoding="utf-8").splitlines()) == 2


def test_no_guarda_en_cache_un_bloqueo(tmp_path):
    cliente = ClienteFalso([RespuestaFalsa(403), RespuestaFalsa(200)], dir_cache=str(tmp_path))
    assert cliente.obtener("https://x.pe/a").status == 403
    assert cliente.obtener("https://x.pe/a").status == 200
    assert cliente.solicitudes_red == 2
