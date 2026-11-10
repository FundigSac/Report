# 05b · Fuentes y rastreos de competencia (Scrapling)

Ejecución real del 10/11/2026 con `Report/scrapling/` (Scrapling 0.5.1, Python 3.12.10, entorno virtual aislado). Pruebas del parser: 44/44.

Comando: `python scrape.py --manifiesto sources.json --salida-dir salida/datos --dir-cache cache --dir-trazas salida/trazas --max-paginas 40 --intervalo 3`
Reglas aplicadas: `robots.txt` obedecido, al menos 3 s entre páginas del mismo sitio, máximo 40 páginas por sitio, reintentos solo ante errores de red o de servidor (nunca ante 403/429), sin modo sigiloso, proxies ni resolución de CAPTCHA. Se guardan solo metadatos públicos (rutas, categorías, nombres de producto, campos técnicos visibles, normas citadas, documentos enlazados), sin datos personales.

| Sitio | Estado | Páginas con datos | Fichas de producto | Fichas con especificaciones | Normas citadas | Documentos | Productos distintos |
| --- | --- | --- | --- | --- | --- | --- | --- |
| avkvalvulas.com | **robots_denegado** (robots.txt no permite la URL) | 0 | — | — | — | — | — |
| bermad.com (2 entradas) | **bloqueado** (HTTP 403) | 0 | — | — | — | — | — |
| saint-gobain.com.pe | **bloqueado** (HTTP 403) | 0 | — | — | — | — | — |
| citalyperu.com | ok | 40 | 26 | 17 | 0 | 2 | 51 |
| collavalimport.com | ok | 36 | 0 | 0 | 0 | 0 | 114 |
| web.eathisa.com.pe | ok | 22 | 0 | 0 | 22 | 0 | 0 |
| fumosac.com.pe | ok | 34 | 0 | 0 | 29 | 16 | 0 |
| hiperusac.com.pe | ok | 39 | 14 | 2 | 7 | 2 | 126 |
| icofesa.com | ok | 23 | 1 | 0 | 0 | 0 | 1 |
| inccosac.com | ok | 18 | 1 | 1 | 3 | 0 | 3 |
| leoneblusac.com | ok | 40 | 15 | 15 | 0 | 2 | 46 |
| meckasacperu.com | ok | 40 | 0 | 0 | 10 | 1 | 0 |
| mylnegofersac.com | ok | 40 | 15 | 2 | 4 | 1 | 234 |
| rivaliperu.com | ok | 40 | 14 | 0 | 0 | 1 | 183 |

Totales: 15 entradas, 12 rastreadas con éxito, 372 páginas, 758 productos distintos. Los 3 sitios bloqueados no se forzaron; se revisaron a mano en Claude in Chrome (`03c-external-design-discovery.md`, X1–X4).

Artefactos: `scrapling/salida/datos/*.json` (por sitio), `scrapling/salida/export/{sitios,paginas,productos}.csv` y `consolidado.json`, traza `scrapling/salida/trazas/`, registro `scrapling/salida/rastreo-2026-11-10.log`.

## Lectura para FUNDIGSAC

- Solo Leoneblu (15/15) y Citaly (17/26) publican especificaciones en la ficha; el resto lista productos sin datos técnicos. Una ficha con DN/PN/material/norma verificados y PDF propio es una diferencia real.
- Fumosac es el único con muchos documentos enlazados (16) y normas citadas (29): es el referente en documentación.
- Negofer (234), Rivali (183) y Hi Perú (126) tienen catálogos amplios pero con poca especificación: competir con claridad técnica, no con cantidad.
- Ninguno combina filtros técnicos + ficha con especificaciones + PDF + cotización por producto: es la posición que busca FUNDIGSAC (ideas X1-1, X1-2, X2-1 en código).
