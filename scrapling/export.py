#!/usr/bin/env python3
"""Exporta los JSON del rastreador a CSV y a un JSON consolidado.

Uso:
    python export.py salida/datos salida/export

Genera en la carpeta de destino:
    sitios.csv     una fila por sitio: estado, páginas, fichas, normas, documentos y robots
    paginas.csv    una fila por página con datos
    productos.csv  una fila por nombre de producto y sitio
    consolidado.json  lo mismo que los tres CSV, en un solo archivo, con la fecha de exportación

Solo usa la biblioteca estándar. Las funciones `filas_*` son puras y se prueban en `test_parse.py`.
"""
from __future__ import annotations

import csv
import glob
import json
import os
import sys
from datetime import datetime, timezone

SEPARADOR = " | "

COLUMNAS_SITIOS = (
    "host", "url_inicial", "estado", "motivo", "fecha_utc", "robots_http", "paginas_con_datos", "fichas_producto",
    "fichas_con_especificaciones", "paginas_con_normas", "normas_citadas", "documentos_enlazados", "productos_distintos",
    "solicitudes_red", "aciertos_cache", "version_rastreador",
)
COLUMNAS_PAGINAS = (
    "host", "url", "http_status", "titulo", "h1", "meta_descripcion", "canonica", "es_ficha_producto",
    "n_productos", "n_especificaciones", "normas_citadas", "tipos_jsonld", "documentos_enlazados", "bytes_html",
    "desde_cache", "fecha_captura",
)
COLUMNAS_PRODUCTOS = ("host", "producto")


def _paginas_utiles(datos: dict) -> list[dict]:
    return [p for p in datos.get("paginas", []) if "titulo" in p]


def fila_sitio(datos: dict) -> dict:
    utiles = _paginas_utiles(datos)
    fichas = [p for p in utiles if p.get("es_ficha_producto")]
    resumen = datos.get("resumen", {})
    traza = datos.get("trazabilidad", {})
    return {
        "host": datos.get("host", ""),
        "url_inicial": datos.get("url_inicial", ""),
        "estado": datos.get("estado", ""),
        "motivo": datos.get("motivo", ""),
        "fecha_utc": datos.get("fecha_utc", ""),
        "robots_http": datos.get("robots", {}).get("http_status", ""),
        "paginas_con_datos": len(utiles),
        "fichas_producto": len(fichas),
        "fichas_con_especificaciones": sum(1 for p in fichas if p.get("especificaciones")),
        "paginas_con_normas": sum(1 for p in utiles if p.get("normas_citadas")),
        "normas_citadas": SEPARADOR.join(resumen.get("normas_citadas", [])),
        "documentos_enlazados": len(resumen.get("documentos_enlazados", [])),
        "productos_distintos": len(resumen.get("productos", [])),
        "solicitudes_red": traza.get("solicitudes_red", datos.get("solicitudes_http", "")),
        "aciertos_cache": traza.get("aciertos_cache", ""),
        "version_rastreador": traza.get("version_rastreador", "1.0"),
    }


def filas_paginas(datos: dict) -> list[dict]:
    host = datos.get("host", "")
    filas = []
    for p in _paginas_utiles(datos):
        traza = p.get("traza", {})
        filas.append({
            "host": host,
            "url": p["url"],
            "http_status": p.get("http_status", ""),
            "titulo": p.get("titulo", ""),
            "h1": SEPARADOR.join(p.get("h1", [])),
            "meta_descripcion": p.get("meta_descripcion", ""),
            "canonica": p.get("canonica", ""),
            "es_ficha_producto": "si" if p.get("es_ficha_producto") else "no",
            "n_productos": len(p.get("productos", [])),
            "n_especificaciones": len(p.get("especificaciones", [])),
            "normas_citadas": SEPARADOR.join(p.get("normas_citadas", [])),
            "tipos_jsonld": SEPARADOR.join(p.get("tipos_jsonld", [])),
            "documentos_enlazados": len(p.get("documentos_enlazados", [])),
            "bytes_html": p.get("bytes_html", ""),
            "desde_cache": "si" if traza.get("desde_cache") else "no",
            "fecha_captura": traza.get("fecha_utc", datos.get("fecha_utc", "")),
        })
    return filas


def filas_productos(datos: dict) -> list[dict]:
    host = datos.get("host", "")
    return [{"host": host, "producto": n} for n in datos.get("resumen", {}).get("productos", [])]


def escribir_csv(ruta: str, columnas, filas: list[dict]) -> None:
    # utf-8-sig para que Excel en Windows abra bien las tildes.
    with open(ruta, "w", encoding="utf-8-sig", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(columnas), extrasaction="ignore")
        escritor.writeheader()
        escritor.writerows(filas)


def cargar(origen: str) -> list[dict]:
    rutas = sorted(glob.glob(os.path.join(origen, "*.json"))) if os.path.isdir(origen) else [origen]
    conjuntos = []
    for ruta in rutas:
        if os.path.basename(ruta).startswith("_"):
            continue  # _ejecucion.json y similares no son datos de un sitio
        with open(ruta, encoding="utf-8") as archivo:
            conjuntos.append(json.load(archivo))
    return conjuntos


def exportar(origen: str, destino: str) -> dict:
    conjuntos = cargar(origen)
    sitios = [fila_sitio(d) for d in conjuntos]
    paginas = [f for d in conjuntos for f in filas_paginas(d)]
    productos = [f for d in conjuntos for f in filas_productos(d)]
    os.makedirs(destino, exist_ok=True)
    escribir_csv(os.path.join(destino, "sitios.csv"), COLUMNAS_SITIOS, sitios)
    escribir_csv(os.path.join(destino, "paginas.csv"), COLUMNAS_PAGINAS, paginas)
    escribir_csv(os.path.join(destino, "productos.csv"), COLUMNAS_PRODUCTOS, productos)
    consolidado = {
        "fecha_exportacion_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "origen": os.path.abspath(origen),
        "sitios": sitios, "paginas": paginas, "productos": productos,
    }
    with open(os.path.join(destino, "consolidado.json"), "w", encoding="utf-8") as archivo:
        json.dump(consolidado, archivo, ensure_ascii=False, indent=2)
    return {"sitios": len(sitios), "paginas": len(paginas), "productos": len(productos), "destino": destino}


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2:
        print("Uso: python export.py ORIGEN(carpeta o .json) DESTINO", file=sys.stderr)
        return 2
    print(json.dumps(exportar(argv[0], argv[1]), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
