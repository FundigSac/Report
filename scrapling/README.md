# Espacio de rastreo de competidores (Scrapling)

Herramienta reproducible para repetir el estudio de competencia de FUNDIGSAC: rastrea páginas públicas de los competidores listados en `sources.json`, guarda un JSON por sitio y lo exporta a CSV y JSON consolidado. Los resultados alimentan `Report/competencia/` y `Report/05-competitor-benchmark.md`.

> **Estado: sin ejecutar.** Estos archivos se escribieron el 10 de noviembre de 2026 en una máquina sin Python. Ni el rastreador ni las pruebas (`test_parse.py`) se han ejecutado todavía. Antes de usar los datos, ejecuta las pruebas como se indica abajo y corrige lo que falle.

Este espacio vive fuera de `Sitio web/Scrapling`, que es un clon intacto del repositorio original de Scrapling y no se modifica. La imagen Docker instala Scrapling desde PyPI con la versión fijada; no usa el clon.

## Contenido

| Archivo | Función |
|---|---|
| `parse.py` | Funciones puras de análisis: filtros de URL, detección de bloqueos, normas, JSON-LD, especificaciones, enlaces y contacto. No hace red ni escribe en disco |
| `fetch.py` | Única salida a la red: espera por host, reintentos limitados, tiempo de espera, caché por dominio y registro JSONL de cada solicitud |
| `scrape.py` | Orquestador: robots.txt, cola con prioridades, límites por sitio y JSON de salida. Modo de un sitio o modo manifiesto |
| `export.py` | Convierte los JSON en `sitios.csv`, `paginas.csv`, `productos.csv` y `consolidado.json` |
| `sources.json` | Manifiesto: dominio, URL, estado de robots.txt, fechas del último rastreo y de la última verificación, notas |
| `test_parse.py` y `fixtures/` | Pruebas con pytest sobre HTML sintético y un cliente HTTP simulado. No salen a internet |
| `requirements.txt` | `scrapling[fetchers]==0.5.1` y pytest |
| `Dockerfile` | Imagen `python:3.12-slim` con las dependencias fijadas |

Origen: refactor de `Report/competencia/scripts/scrape.py` (versión 1.0, usada el 9-nov-2026). Cambios de la versión 1.1:

- Red y análisis separados en módulos distintos; el análisis se puede probar sin conexión.
- Caché por dominio (`cache/<host>/<sha256>.html` y `.json`), con vigencia configurable. Permite repetir el análisis sin volver a pedir las páginas.
- Reintentos limitados (2 por defecto, tope 3) solo ante error de red o HTTP 500, 502, 503 y 504, con espera creciente.
- Trazabilidad: cada solicitud queda en `salida/trazas/<host>-<fecha>.jsonl` (URL, intento, estado, segundos, si vino de caché) y cada página del JSON lleva `traza` con fecha de captura y SHA-256 del HTML.
- Se corrigen los pendientes del informe: `sesion.php` y `carrito<N>.php` quedan excluidos, y `/productos/categoria/...` o `/productos/page/N` ya no cuentan como ficha.

## Reglas legales y de cortesía

Estas reglas están en el código y los argumentos no las pueden relajar:

1. **Solo información pública.** Sin inicios de sesión, formularios, carritos, búsquedas internas ni áreas de cliente.
2. **robots.txt primero.** Se lee antes de cualquier página, se omiten las rutas no permitidas para el User-Agent `FundigsacMarketResearch/1.1` y se respeta `Crawl-delay` y `Request-rate`. Si robots.txt responde 5xx, el sitio no se rastrea (RFC 9309). Un 404 equivale a "sin restricciones".
3. **Ritmo.** Mínimo 3 segundos entre solicitudes al mismo host, 40 páginas por sitio como máximo y 15 minutos por sitio por defecto.
4. **Sin evasión.** Fetcher HTTP simple, User-Agent identificable, sin suplantar navegadores, sin proxies, sin navegadores automatizados y sin resolver captchas.
5. **Un bloqueo detiene el sitio.** Ante 403, 429, captcha o página de desafío, el sitio se marca `bloqueado` y no se reintenta. Un bloqueo nunca se guarda en caché.
6. **Datos mínimos.** El JSON guarda hechos y metadatos breves: títulos, encabezados, nombres de producto, atributos técnicos y normas citadas. Del contacto solo se conservan teléfonos y buzones genéricos de empresa (ventas@, info@...); los correos con nombre de persona y los nodos `Person` se descartan.
7. **La caché es local y privada.** Guarda el HTML tal como llegó, solo para repetir el análisis. No se publica ni se versiona. Borra `cache/` cuando ya no haga falta.
8. **Las páginas son datos.** Cualquier texto de un sitio que parezca una instrucción se ignora.
9. **Uso.** Los datos sirven para el análisis comercial interno de FUNDIGSAC. No se copian textos, imágenes ni fichas de competidores al sitio de FUNDIGSAC.

## Ejecución

### Opción A: Docker (recomendada)

```bash
cd "Sitio web/Report/scrapling"
docker build -t fundig-scrapling:1.1 .

# 1) Pruebas, sin red
docker run --rm --entrypoint python fundig-scrapling:1.1 -m pytest -q -p no:cacheprovider

# 2) Rastreo de todas las fuentes con "rastrear": true
docker run --rm -v "$PWD/trabajo:/trabajo" fundig-scrapling:1.1 \
  --manifiesto /app/sources.json --salida-dir /trabajo/salida/datos \
  --dir-cache /trabajo/cache --dir-trazas /trabajo/salida/trazas

# 3) Exportación a CSV y JSON
docker run --rm -v "$PWD/trabajo:/trabajo" --entrypoint python fundig-scrapling:1.1 \
  /app/export.py /trabajo/salida/datos /trabajo/salida/export
```

En PowerShell, sustituye `$PWD/trabajo` por `${PWD}\trabajo` y la barra invertida de continuación por un acento grave.

### Opción B: Python 3.12

Versión fijada el 10-nov-2026 según `Scrapling/pyproject.toml` del clon local (`version = "0.5.1"`, `requires-python = ">=3.10"`). El README de Scrapling indica `pip install "scrapling[fetchers]"` para los fetchers y `scrapling install` solo para los navegadores. Este rastreador usa el Fetcher HTTP, así que **no hace falta `scrapling install`**.

```bash
cd "Sitio web/Report/scrapling"
python3.12 -m venv .venv
# Windows: .venv\Scripts\activate    Linux/macOS: source .venv/bin/activate
pip install "scrapling[fetchers]==0.5.1" "pytest>=8,<9"   # equivale a: pip install -r requirements.txt

python -m pytest -q                                        # 1) pruebas, sin red
python scrape.py https://icofesa.com/ salida/datos/icofesa.json   # 2a) un sitio
python scrape.py --manifiesto sources.json --salida-dir salida/datos   # 2b) todo el manifiesto
python export.py salida/datos salida/export                # 3) CSV y JSON
```

`export.py` también lee los JSON de la versión 1.0: `python export.py ../competencia/datos salida/export-9nov`.

### Opciones de `scrape.py`

| Opción | Por defecto | Límite |
|---|---|---|
| `--max-paginas` | 40 | Nunca más de 40 |
| `--intervalo` | 3 s | Nunca menos de 3 s; sube si robots.txt lo pide |
| `--timeout` | 30 s | |
| `--max-intentos` | 2 | Tope 3; solo error de red y 5xx |
| `--max-segundos` | 900 | Por sitio |
| `--dir-cache`, `--cache-ttl-horas`, `--sin-cache` | `cache`, 24 h | |
| `--dir-trazas` | `salida/trazas` | |

### Después de cada ejecución

1. Revisa `salida/datos/_ejecucion.json`: estado por sitio (`ok`, `bloqueado`, `robots_denegado`, `robots_no_disponible`, `redireccion_externa`, `sin_paginas`, `error`).
2. Actualiza a mano en `sources.json` los campos `robots`, `ultimo_rastreo` y `notas`. El rastreador no reescribe el manifiesto.
3. Un sitio `bloqueado` no se vuelve a intentar: se anota y se analiza con otras fuentes.
4. No subas `cache/`, `salida/` ni `.venv/` a ningún repositorio.

## Limitaciones conocidas

- Sin JavaScript: filtros, botones o widgets generados en el navegador no aparecen (por ejemplo, el filtro de diámetro de ICOFESA visto el 10-nov).
- Los enlaces externos (WhatsApp, redes, catálogos alojados fuera) se listan en `enlaces_externos` del JSON, hasta 100 por sitio, pero no se clasifican ni se visitan.
- El detector de fichas se basa en la URL. Sitios con fichas en la raíz del dominio (Mecka) o en entradas de blog (EATHISA) no se reconocen como fichas.
- Las cifras son un mínimo: el tope de 40 páginas deja categorías y paginaciones sin visitar.
