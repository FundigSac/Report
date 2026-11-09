# Informe de competencia de FUNDIGSAC en Perú

Fecha: 9 de noviembre de 2026.

Documentos complementarios: `Report/competencia/PLAN_SEO.md` y `Report/competencia/FUENTES.md`, que reúne los resultados de las búsquedas, el estado del rastreo por sitio y los controles de esta revisión.

## 1. Resumen

FUNDIGSAC tiene una base técnica sólida en su sitio nuevo, pero hoy no compite en buscadores. El sitio nuevo sigue en `noindex` por decisión del proyecto, y lo que Google conoce es el WordPress anterior de `fundigsac.com`. En las 20 búsquedas de esta revisión, `fundigsac.com` solo apareció en la búsqueda de su propia marca. ICOFESA apareció en 14 de las 19 búsquedas sin marca.

Los tres hallazgos que más condicionan el plan son estos:

1. **El catálogo público es mucho más corto que el catálogo real.** Solo hay 10 fichas indexables y todas son de válvulas. Tubería de hierro dúctil, marcos y tapas, válvula mariposa y válvula de aire no tienen ninguna ficha indexable, aunque la lista de precios de FUNDIGSAC sí las incluye. De las 69 referencias de `src/lib/catalog.ts` y `src/lib/catalog-pdf.ts`, 61 no tienen URL pública (recuento propio).
2. **La mayor debilidad observada en el mercado es la información técnica, y ahí FUNDIGSAC puede ganar.** En las muestras revisadas, solo FUMOSAC combina normas, medidas y PDF por ficha. La muestra no incluye ninguna ficha de Collaval y solo una de ICOFESA. Cinco competidores no citan ninguna norma en las páginas revisadas y Negofer solo lo hace en 3 de 40. Esa ventaja solo vale si FUNDIGSAC respalda cada norma con un documento.
3. **Los KPI no están en verde.** Con la indexación activada en una compilación local, SEO, accesibilidad y buenas prácticas cumplen en las 14 rutas medidas. El rendimiento móvil falla en las 14 rutas: LCP de 3.535 a 5.256 ms frente a un máximo de 2.500 ms. Detalle en la sección 9.

**Hallazgo que requiere revisión inmediata:** la dirección que FUNDIGSAC publica (`Jirón Pacasmayo Mz. E Lt. 12, Cercado de Lima`) es idéntica a la que M&L Negofer declara en su `LocalBusiness` (`Jr. Pacasmayo Mz. E Lt. 12, Cercado de Lima`, en `datos/negofer.json`). Este estudio no permite saber si es un error de datos, un local compartido o un vínculo entre empresas. Ver V-02.

Advertencia sobre `src/modules/catalog/data.ts`: su propia cabecera lo declara dataset de maqueta. Sus SKU, rangos, normas y homologaciones (SEDAPAL, OTASS, WRAS) y frases como "Stock Lurín" o "Despacho 24h" no son datos verificados. Varias fichas de competidores lo citan como catálogo de FUNDIGSAC; aquí no se usa como evidencia.

Convención: lo que no lleva marca es un hecho observado en el rastreo, en el código o en la búsqueda. Lo marcado como **Inferencia** es interpretación. Las declaraciones de los competidores sobre normas, certificados, marcas o aprobaciones no se verificaron.

## 2. Alcance y método

| Fuente | Qué se usó | Límite principal |
|---|---|---|
| 12 fichas de `Report/competencia/sitios` y 12 JSON de `Report/competencia/datos` | Catálogo, normas, metadatos, JSON-LD, enlazado | Tope de 40 páginas por sitio, HTTP sin JavaScript. Válvulas Perú sin datos por NXDOMAIN |
| `Frontend/src/modules/catalog`, `src/app/sitemap.ts`, `src/lib/catalog-pdf.ts` y rutas | Estado real del sitio nuevo | El código no es prueba de que los datos sean correctos |
| 20 búsquedas de compradores con WebSearch, modo `extended` | Quién aparece por consulta | Herramienta con salida desde Estados Unidos. No es Google Perú |
| Compilación local con indexación activada, rastreo propio de 31 páginas y `scripts/perf/kpi-gate.mjs` | KPI de FUNDIGSAC | Local, sin CDN ni red real. No sustituye la medición en producción |

**Bloqueos del rastreo: ninguno.** Ningún sitio respondió 403, 429, captcha o página de desafío, y `robots.txt` no excluyó ninguna URL solicitada. `leoneblusac.com` no publica `robots.txt` (HTTP 404). El único sitio sin datos es Válvulas Perú, por NXDOMAIN, que no es un bloqueo. Cobertura parcial: ICOFESA perdió 17 de sus 40 solicitudes en redirecciones 302 y no visitó sus categorías de válvulas y tubería; Collaval no visitó ninguna ficha; 5 URL de Inccosac y 3 de Collaval respondieron 404. El detalle está en la sección 2 de `FUENTES.md`.

No se accedió a producción ni a bases de datos. No se hizo scraping de Google. PageSpeed de competidores: **n/d** en los 12 casos porque la API respondió HTTP 429 sin clave, así que no existe comparación de rendimiento real con ningún competidor. El peso del HTML que aparece abajo es solo un indicio.

Sobre las búsquedas: las cinco primeras se ejecutaron antes en modo `standard` y devolvieron sobre todo resultados extranjeros, por lo que se repitieron en modo `extended`. Solo cuentan los resultados de `extended`. El orden es el de la respuesta de la herramienta y **no equivale a una posición en Google.pe**. No hay datos de volumen de búsqueda, clics ni enlaces entrantes.

## 3. Mapa del mercado

| Segmento | Empresas | Cómo compiten | Amenaza para FUNDIGSAC |
|---|---|---|---|
| Distribuidores multimarca con precio o carrito | ICOFESA, Leoneblu, The Atlantic, Valvoline Perú | Volumen de fichas, precios en soles, compra concentrada | Alta en visibilidad y en compras pequeñas |
| Importadores con marca propia o exclusiva | M&L Negofer (M&L), Collaval y Citaly (C-Italy), Hi Perú (Mafusa), Mecka (FLOWRAM), Rivali, EATHISA, A.C. Trading | Amplitud por familia y transición a HDPE y PVC | Alta en válvulas y conexiones |
| Fabricantes nacionales declarados | FUMOSAC, Inccosac | Fabricación local, normas por familia, mensaje de proveedor de SEDAPAL | Alta ante EPS y expedientes técnicos |
| Tubería y grandes proyectos | Grupo Hidráulica, PATMO Perú, Romicorp, Hi Perú (tubería), productos PAM en ICOFESA | Tubería K9 y C40 con ficha o pliego técnico | Alta en tubería |
| Especialistas por sector | Tecval y valvulasmineras.com (minería), Termofusión y Riego (agricultura), Fiorella (contra incendios UL/FM), Rivali (contra incendios) | Conocimiento de la aplicación | Media; alta si FUNDIGSAC quiere minería de relaves |
| Minoristas | Sodimac, Falabella, Mercado Libre, Rotoplas | Precio visible y marketplace | Baja en proyectos; ocupan espacio en consultas con "precio" |
| Documentación | SEDAPAL, gob.pe, Scribd, Studocu, Slideshare | Especificaciones y normas | No compiten en venta, pero dominan la consulta normativa |

Empresas que `COMPETIDORES.md` no tenía como competidor principal y que aparecieron en dos o más búsquedas: Fiorella Representaciones (6), Valvoline Perú (5), Orbe (3), Asocie Perú (3), Roalcom (3), valvulasperu.com.pe (3), Redline Perú (2), Grupo Hidráulica (2) y Romicorp (2). Todas constan ya en la tabla de empresas no incluidas de `COMPETIDORES.md`, con sus apariciones, pero **ninguna se rastreó**. Conviene analizar al menos Fiorella, Valvoline Perú y Grupo Hidráulica.

**Inferencia:** ICOFESA, Leoneblu y The Atlantic comparten el patrón de URL `producto.php?id=`, lo que apunta a una misma plataforma de tienda. No se comprobó si existe vínculo entre ellas.

`valvulasperu.pe` no resuelve en DNS desde el rastreo, pero la herramienta de búsqueda todavía lo devolvió en 3 consultas. **Inferencia:** es un índice desactualizado. Falta decidir si se sustituye por `valvulasperu.com.pe` o se retira del listado.

## 4. Quién aparece en las 20 búsquedas

Cada fila lista los dominios distintos en el orden de la respuesta.

| Id | Búsqueda | Dominios en orden de aparición |
|---|---|---|
| Q1 | válvula compuerta hierro dúctil Perú precio | sodimac.com.pe, falabella.com.pe, valvoline-peru.com, agromax.pe, rivaliperu.com, fitflowretail.com, icofesa.com |
| Q2 | válvula compuerta bridada PN16 Lima proveedor | fiorellarepre.com.pe, hiperusac.com.pe, leoneblusac.com, tecnototalperu.com, icofesa.com |
| Q3 | válvula mariposa hierro dúctil Perú | fiorellarepre.com.pe, adolphus.pe, orbe.com.pe, icofesa.com |
| Q4 | válvula check hierro dúctil Lima venta | redlineperu.pe, fiorellarepre.com.pe, icofesa.com |
| Q5 | válvula de aire triple efecto agua potable Perú | slideshare.net, gob.pe, kallpa-peru.com, hidroplast.net, studocu.com, asocieperu.com, icofesa.com |
| Q6 | tubería hierro dúctil K9 Perú proveedor | scribd.com, web.eathisa.com.pe, patmoperu.com, grupohidraulica.com, hiperusac.com.pe, romicorp.com.pe, icofesa.com |
| Q7 | tubería hierro dúctil ISO 2531 Lima precio | made-in-china.com, inteco.org, quiminet.com, studocu.com, icofesa.com, alibaba.com |
| Q8 | marco y tapa de buzón D400 hierro dúctil Lima | valvulasperu.pe, fumosac.com.pe, grupohidraulica.com, mylnegofersac.com, roalcomperu.com, collavalimport.com, leoneblusac.com, meckasacperu.com, citalyperu.com |
| Q9 | tapa de buzón hierro dúctil precio Perú | theatlantic.pe, roalcomperu.com, leoneblusac.com, wikipedia.org, icofesa.com |
| Q10 | rejilla pluvial sumidero hierro dúctil Perú | scribd.com, compraspublicas.gob.ec, saludarequipa.gob.pe, minfraestructura.com.ar, equihersas.com, fundiec.com, tapasyregistros.com, prefabricadoscifa.com, gob.pe, colfergroup.com |
| Q11 | válvula reductora de presión hierro dúctil Perú proveedor | hiperusac.com.pe, roalcomperu.com, orbe.com.pe, fullcontrolperu.com, valvoline-peru.com, icofesa.com, asocieperu.com |
| Q12 | válvula compuerta para tubería HDPE acerrojada Perú | valvulasperu.com.pe, valvulasperu.pe, hiperusac.com.pe, collavalimport.com, tuberiaspvc.pe, fimaca.com, asocieperu.com |
| Q13 | conexiones bridadas hierro dúctil tee codo Perú | redlineperu.pe, orbe.com.pe, valvoline-peru.com, confundsac.com, citalyperu.com, icofesa.com |
| Q14 | válvulas para minería relaves Perú proveedor hierro dúctil | facebook.com, tecval.pe, collavalimport.com, valvoline-peru.com, valvulasmineras.com, corsaflex.com, icofesa.com, fiorellarepre.com.pe |
| Q15 | válvulas hierro dúctil riego agrícola Perú | termofusion-riego.com, valmevm.com, rivaliperu.com, fuentejardin.com, sidertecnica.com.ec, icofesa.com |
| Q16 | proveedor válvulas agua potable SEDAPAL especificación técnica hierro dúctil | sedapal.com.pe, scribd.com, gob.pe, slideshare.net |
| Q17 | importador válvulas hierro dúctil Perú distribuidor | hiperusac.com.pe, valvulasperu.pe, collavalimport.com, rivaliperu.com, valvulasperu.com.pe, fiorellarepre.com.pe, valvoline-peru.com, icofesa.com |
| Q18 | válvula flotadora bridada control de nivel Perú | mercadolibre.com.pe, rotoplas.com.pe, vts.com.pe, icofesa.com, dudesign.pe |
| Q19 | válvulas y tuberías hierro dúctil Arequipa Trujillo Piura proveedor | quiminet.com, valvulasperu.com.pe, koplastindustrial.com, romicorp.com.pe, vaneco.com.pe, fiorellarepre.com.pe, acorsaperu.com, eurotubo.com.pe |
| Q20 | FUNDIGSAC válvulas hierro dúctil | tubacero.com.uy, bundorvalve.es, fundigsac.com, confundsac.com |

Presencia en las 19 búsquedas sin marca (Q1 a Q19):

| Dominio | Búsquedas | Dónde |
|---|---:|---|
| icofesa.com | 14 | Q1 a Q7, Q9, Q11, Q13, Q14, Q15, Q17, Q18 |
| fiorellarepre.com.pe | 6 | Q2, Q3, Q4, Q14, Q17, Q19 |
| valvoline-peru.com | 5 | Q1, Q11, Q13, Q14, Q17 |
| hiperusac.com.pe | 5 | Q2, Q6, Q11, Q12, Q17 |
| collavalimport.com | 4 | Q8, Q12, Q14, Q17 |
| rivaliperu.com | 3 | Q1, Q15, Q17 |
| leoneblusac.com | 3 | Q2, Q8, Q9 |
| orbe.com.pe, asocieperu.com, roalcomperu.com, valvulasperu.com.pe, valvulasperu.pe | 3 cada uno | Ver tabla anterior |
| citalyperu.com, redlineperu.pe, grupohidraulica.com, romicorp.com.pe | 2 cada uno | Ver tabla anterior |
| mylnegofersac.com, fumosac.com.pe, meckasacperu.com, web.eathisa.com.pe | 1 cada uno | Q8; Q8; Q8; Q6 |
| inccosac.com | 0 | Su marca aparece solo en fichas de The Atlantic en Q9 |
| **fundigsac.com** | **0** | Solo en la búsqueda de marca Q20 |

Lectura de los resultados:

- **Los huecos más claros son Q10 y Q16.** En Q10 ningún resultado fue un vendedor con dominio peruano. En Q16 solo apareció documentación pública y ningún proveedor. La de Q16 solo se puede aprovechar con cumplimiento documentado. Q10 no significa que no haya competencia: FUMOSAC tiene `/rejillas-pluviales/` e ICOFESA una categoría `rejilla-186`, solo que no aparecieron en esa búsqueda.
- **SEDAPAL publica sus especificaciones.** La búsqueda devolvió CTPS-ET-013 (compuerta), CTPS-ET-017 y CTPS-ET-018 (aire), CTPS-ET-019 (reductora), CTPS-ET-034 (filtro tipo cesto) y CTPS-ET-041 (control de bomba). Son la referencia con la que se compara un comprador de EPS.
- **Marcos y tapas es la consulta más disputada entre competidores directos:** 9 dominios en Q8.
- **La marca FUNDIGSAC se confunde con Confundsac** en Q20 (confundsac.com, otra empresa).
- **Inferencia:** ICOFESA gana por número de fichas con URL propia, no por calidad técnica: en sus 23 páginas rastreadas no se detectó ninguna norma.

## 5. Estado real de FUNDIGSAC

Datos del código y de una compilación local con indexación activada.

| Línea | Fichas indexables | Situación |
|---|---:|---|
| Compuerta | 5 | Bridada H-ITALY, FUNDIGSAC, garantía extendida, acerrojada HDPE, Luflex |
| Check | 2 | Swing y flex |
| Regulación | 3 | Reductora, alivio, flotadora |
| Mariposa | 0 | `/productos/valvulas/valvula-mariposa` es referencia con `noindex`. La lista de precios tiene 6 modelos |
| Aire | 0 | La tarjeta lleva a `/contacto`. La lista de precios tiene VDAP y VDAR |
| Tubería de hierro dúctil | 0 | `/tuberia-tyton` es referencia con `noindex`. `/productos/tuberias` no enlaza ninguna ficha. La lista de precios tiene THD C40, K9 y K7 |
| Marcos y tapas | 0 | `/marco-tapa-d400` es referencia con `noindex`. La lista de precios tiene 2SEG y 1SEG |
| Conexiones, acoples, bridas, filtros | 0 | Referencias con código y medidas en `catalog-pdf.ts`, sin URL pública |
| HDPE, equipos, medidores | 0 | Referencias en `catalog-pdf.ts`, sin URL pública |

Rastreo propio de 31 páginas (28 del sitemap y 3 de referencia). Los recuentos se repitieron en esta revisión; ver sección 4 de `FUENTES.md`:

- Título único, meta descripción, un solo H1 y canónica correcta en 31 de 31.
- `Organization` y `WebSite` en 31 de 31. `BreadcrumbList` en 16. `Product` en 10, sin `offers`, reseñas ni valoraciones.
- No hay `LocalBusiness`. El `PostalAddress` omite la calle a propósito.
- Enlaces `tel:` en 31 de 31 y enlace de WhatsApp en la mayoría.
- `/` enlaza 0 fichas. Cada `/industrias/*` enlaza 1. `/productos/tuberias` enlaza 0. `/productos/marcos-y-tapas` enlaza 1, y es una referencia `noindex`. `/productos` enlaza 5, de las que 2 son referencias `noindex`.
- Cuatro títulos de ficha superan los 60 caracteres, con un máximo de 62.
- En `next.config.ts`, la regla `/product/:slug` envía la mariposa excéntrica y la guillotina del WordPress anterior al listado de válvulas. Esas dos URL pierden su equivalente hasta que exista ficha.
- `env.ts` cita un archivo `SEO-GOOGLE-LAUNCH.md` que no existe en el repositorio.

## 6. Matriz comparativa

### 6.1 Cobertura por línea

Sí: hay productos visibles. Parcial: oferta mínima o mencionada sin ficha. No: no se vio en la muestra. Una ausencia vale solo para las páginas revisadas. Las cifras cuentan productos con ese nombre y, salvo indicación, pueden incluir otros materiales. Rejillas, filtros, acoples, medidores y equipos no tienen columna; constan en las fichas de `sitios/`.

| Empresa | Compuerta HD | Mariposa | Check | Aire | Tubería HD | Conexiones HD | Marcos y tapas | Hidrantes | HDPE |
|---|---|---|---|---|---|---|---|---|---|
| **FUNDIGSAC (público)** | Sí, 5 | No (6 en lista) | Sí, 2 | No (2 en lista) | No (en lista) | No (en lista) | No (2 en lista) | No | Solo compuerta acerrojada |
| M&L Negofer | Sí | No vista, faltan 10 páginas | Sí | Sí, 5 | Sí, K-7 y K-9 | Sí, amplia | Sí, 8 | Sí, 5 | Sí, 32 |
| ICOFESA | Sí | Sí (Q3) | Sí (Q4) | Sí | Sí, K9 | Sí, amplia | Sí, 186 declarados | Sí, 7 | Parcial |
| FUMOSAC | Sí, 4 | No | Sí, 1 | Sí, 1 | No | Parcial, 1 página | Sí, 4 | Sí, 4 | Parcial |
| Collaval Import | Sí, 8 | Solo PVC | Sí, 1 en HD | Sí | No | Sí, 6 | Parcial, 1 | No | Sí |
| Mecka | Sí, 7 (incluye 3 de bronce y 1 WCB) | Sí, 2 | Sí, 5 | Sí, 3 | No | Parcial | Parcial, 1 | No | No |
| Leoneblu | Sí | Sí | Sí | Sí | Sí | Sí | Sí | Sin datos | Sí |
| EATHISA | Sí, 2 | Sí, 1 | Sin etiqueta | Sin etiqueta | Sí | Parcial | Parcial, 1 | No | No |
| Hi Perú | Sí, 13 con cuchilla | Sí, 5 | Sí, 7 | Sí, 4 | Parcial, 1 | Parcial | No | No | Sí, 49 |
| Rivali | Sí, 11 | Sí, 7 | Sí, 14 | Sí, 2 | No | Sí | Parcial, 1 en fierro fundido | Parcial, 1 | Sí |
| Inccosac | Solo mencionadas | No | No | No | Mención, ficha 404 | Mención | Parcial, 1 compuesto | Mención | Mención |
| Citaly | Sí | Sí, 3 | Solo bronce | Sí, 1 | No | Sí, 8 | Parcial, 1 | Parcial, 1 | Parcial |
| Válvulas Perú | Sin datos | Sin datos | Sin datos | Sin datos | Sin datos | Sin datos | Sin datos | Sin datos | Sin datos |

### 6.2 Comparación por dimensión

Las valoraciones Alta, Media y Baja son criterio del analista sobre los datos citados. El peso de HTML es la media por página en KiB (1.024 bytes); algunas fichas de `sitios/` lo dan en KB (1.000 bytes) o como mediana, y por eso sus cifras difieren un poco.

| Empresa | Catálogo | Especificaciones | Normas y certificaciones | Rendimiento | SEO | UX y conversión |
|---|---|---|---|---|---|---|
| **FUNDIGSAC (local)** | Baja: 10 fichas | Alta en esas 10: tablas HTML, DN, PN y material; 3 PDF y 2 folletos | Media: citadas solo en 3 fichas de compuerta, sin certificado enlazado y pendientes de validar | Móvil 80 a 91; escritorio 96 a 100 | Alta en lo técnico; hoy en `noindex` | Alta: cotización, teléfono y WhatsApp |
| M&L Negofer | Alta: 212 URL | Baja: 2 de 15 fichas con atributos | Baja: 3 páginas, EN 124 e ISO 2531 | n/d; HTML 223 KB | Media-alta | Media: paginación de hasta 11 páginas |
| ICOFESA | Alta: 7.528 declarados | Baja: 1 ficha revisada, sin atributos | Baja: 0 detectadas en la muestra | n/d; HTML 120 KB | Media: portada con Lima; categorías de una palabra | Alta: cotización, carrito, crédito, envíos |
| FUMOSAC | Media: 20 fichas | Alta: 14 con medidas, 17 con PDF | Alta: normas por familia, ISO 9001 sin verificar | n/d; HTML 48 KB | Baja: 1 título en 34 páginas, sin JSON-LD | Baja: sin `tel:`, sin paso de cotización |
| Collaval Import | Alta: 115 URL | Sin medir, 0 fichas visitadas | Baja: 0 en categorías | n/d; HTML 321 KB | Media-baja: 21 de 36 sin meta, 3 enlaces 404 globales | Media: navegación por material y marca |
| Mecka | Media: 41 URL | Baja: tablas en imagen (**Inferencia**) | Media: 10 fichas con normas | n/d; HTML 77 KB | Media: fichas marcadas como `Article` | Baja: dos teléfonos distintos, sin `tel:` |
| Leoneblu | Alta: 75 categorías | Baja: 0 de 15 | Baja: 0 citadas, dice "certificados" | n/d; HTML 96 KB | Baja: sin canónica, sin JSON-LD, `lang="en"` | Media: cotizar visible, `tel:#` roto |
| EATHISA | Baja: 16 entradas | Media: datos en texto | Media: lista amplia con erratas | n/d; HTML 140 KB | Baja: blog sin JSON-LD | Baja: sin cotización, sitio con poco mantenimiento |
| Hi Perú | Alta: 126 productos | Baja: 2 de 14 | Media: EN 1074, EN 593, ISO 2531, EN 545 | n/d; HTML 165 KB | Media-baja: 0 H1 en categorías | Media |
| Rivali | Alta: 173 fichas | Baja: 0 de 14 | Baja: solo UL y FM en nombres | n/d; HTML 167 KB | Media-baja: títulos vacíos en 23 categorías | Media: carrito y Joinchat |
| Inccosac | Baja: 1 ficha visible | Media en 1 ficha | Media: ISO y SEDAPAL declarados, enlaces del SIG en 404 | n/d; HTML 196 KB | Baja: H1 repetido | Baja: familias vacías |
| Citaly | Media: 53 URL | Baja: DN en 6 de 26 | Baja: 0 citadas | n/d; HTML 127 KB | Baja: 0 H1 en fichas | Media: carrito |
| Válvulas Perú | Sin datos | Sin datos | Sin datos | n/d | Sin datos | Sin datos |

### 6.3 Indicadores comparables

Calculados sobre las páginas con respuesta 200 de cada JSON. FUNDIGSAC se mide en local y con la indexación activada, así que su fila no representa lo que Google ve hoy.

| Empresa | Páginas | Títulos únicos | Con meta | Con un solo H1 | Canónica | Con JSON-LD | Product | LocalBusiness o Store | BreadcrumbList | Páginas con normas | Documentos |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **FUNDIGSAC (local)** | 31 | 31 | 31 | 31 | 31 | 31 | 10 | 0 | 16 | 4 | 5 |
| M&L Negofer | 40 | 40 | 40 | 40 | 40 | 19 | 15 | 1 | 16 | 3 | 1 |
| ICOFESA | 23 | 23 | 23 | 22 | 21 | 2 | 1 | 1 | 0 | 0 | 0 |
| FUMOSAC | 34 | 1 | 34 | 20 | 34 | 0 | 0 | 0 | 0 | 29 | 16 |
| Collaval Import | 36 | 36 | 15 | 31 | 36 | 36 | 0 | 0 | 36 | 0 | 0 |
| Mecka | 40 | 40 | 38 | 39 | 40 | 40 | 0 | 0 | 40 | 10 | 1 |
| Leoneblu | 40 | 39 | 25 (0 útiles) | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| EATHISA | 22 | 22 | 20 | 21 | 22 | 0 | 0 | 0 | 0 | 22 (*) | 0 |
| Hi Perú | 39 | 39 | 21 | 15 | 39 | 39 | 0 | 0 | 39 | 7 | 2 |
| Rivali | 40 | 18 | 3 | 14 | 40 | 40 | 14 | 0 | 40 | 0 | 1 |
| Inccosac | 18 | 6 | 18 | 17 | 18 | 18 | 1 | 0 | 0 | 3 | 0 |
| Citaly | 40 | 40 | 10 | 14 | 27 | 26 | 0 | 0 | 26 | 0 | 2 |

(*) En EATHISA, ISO 2531 aparece en las 22 páginas por un enlace lateral. No indica que cada página cite la norma.

## 7. Dónde gana y dónde pierde FUNDIGSAC

### Dónde gana

Estas ventajas existen en el código y deben confirmarse tras el lanzamiento.

| Frente | Evidencia | Contra quién |
|---|---|---|
| Datos técnicos en HTML | Tablas con DN, PN, material y montaje en 10 fichas | Negofer 2 de 15, Hi Perú 2 de 14, Rivali 0 de 14, Leoneblu 0 de 15 |
| Base de SEO técnico | Título, meta, H1 y canónica en 31 de 31 | Solo Negofer iguala estos cuatro indicadores |
| `Product` sin datos inventados | 10 fichas con marcado honesto | FUMOSAC, Mecka, Leoneblu, EATHISA, Hi Perú y Citaly no tienen `Product` en las fichas revisadas |
| Ruta de contacto en móvil | `tel:` en todas las páginas, `/cotizar` con producto preseleccionado | FUMOSAC, Mecka, Hi Perú, Rivali, Citaly, EATHISA, Collaval e Inccosac sin `tel:` en la muestra |
| Páginas por sector | `/industrias/saneamiento`, `/mineria`, `/agricultura` | Ningún competidor analizado cubre los tres sectores con página propia en la muestra |
| Compuerta para HDPE | Tabla de DN frente a diámetro de tubo en `valvula-compuerta-acerrojada` | Citaly lo tiene con dos atributos y sin DN en su ficha. Collaval, Negofer y FUMOSAC también lo ofrecen, pero sus datos no se compararon |
| Rendimiento en escritorio | 96 a 100 en 14 rutas | Sin comparación posible: competidores n/d |

### Dónde pierde

| Frente | Evidencia | Prioridad |
|---|---|---|
| Visibilidad actual | 0 de 19 búsquedas sin marca; sitio nuevo en `noindex` | Crítica |
| Catálogo publicado | 10 fichas frente a 20 de FUMOSAC y 41 a 212 URL de los importadores | Crítica |
| Líneas centrales sin ficha | Tubería, marcos y tapas, mariposa y aire | Crítica |
| Rendimiento móvil | 14 de 14 rutas fallan LCP; 13 de 14 fallan también la puntuación | Crítica |
| Evidencia técnica | FUMOSAC tiene PDF en 17 de 20 fichas y normas por familia; FUNDIGSAC tiene 3 fichas PDF | Alta |
| Argumento SEDAPAL | Inccosac, EATHISA y Hi Perú lo usan como reclamo (sin verificar); FUNDIGSAC no puede hacerlo sin documento | Alta, condicionada |
| Datos de empresa | Sin calle en datos estructurados, RUC sin validar, dos correos | Alta |
| Precios | ICOFESA, Leoneblu y The Atlantic publican precios; FUNDIGSAC decidió cotizar | Decisión tomada, no es un defecto |
| Hidrantes | FUMOSAC tiene 4 fichas y Negofer 5; FUNDIGSAC no tiene | Decisión comercial |
| Conexiones y HDPE | Negofer, Collaval, Citaly y Hi Perú tienen líneas amplias | Media |
| Autoridad externa | No medida. FUNDIGSAC arranca con dominio antiguo en WordPress | Por medir en Search Console |

## 8. Acciones priorizadas

La prioridad combina impacto esperado (**Inferencia**) y dependencia. Las URL, títulos y marcados concretos están en `PLAN_SEO.md`.

### Prioridad 0: antes de activar la indexación

| # | Acción | Responsable | Depende de |
|---|---|---|---|
| 1 | Completar la lista de validación de la sección 10 | FUNDIGSAC | Documentos de la empresa |
| 2 | Retirar o sustentar frases sin respaldo: "Productos certificados y de calidad", "Stock disponible para proyectos", conformidad WRAS, "fabricado según la norma EN 124" | Desarrollo y FUNDIGSAC | Acción 1 |
| 3 | Corregir LCP móvil hasta dejar las 14 rutas en verde | Desarrollo | Medición con `kpi-gate` |
| 4 | Publicar fichas de tubería C40, K9 y K7, marco y tapa D400 de 1 y 2 seguros, mariposa y válvula de aire | Desarrollo e Ingeniería | Revisión técnica de cada dato |
| 5 | Corregir enlaces: `/productos/tuberias` a sus fichas; quitar enlaces a referencias `noindex` | Desarrollo | Acción 4 |
| 6 | Añadir `LocalBusiness` y calle en `PostalAddress` | Desarrollo | Dirección, horario y atención validados |
| 7 | Ejecutar el corte de dominio, los 301 y Search Console | TI | Control de DNS |
| 8 | Reclamar la ficha de Google Business Profile | FUNDIGSAC | Dirección verificable |

### Prioridad 1: primeras semanas tras el lanzamiento

| # | Acción | Razón |
|---|---|---|
| 9 | Crear `/productos/conexiones` y fichas de tee y yee bridados | Q13 y debilidad frente a Negofer y Citaly |
| 10 | Crear fichas de acoples y adaptadores para PVC y HDPE | Transición a HDPE, punto fuerte de Collaval y Citaly |
| 11 | Publicar rejilla pluvial con ficha propia | Q10 no mostró ningún vendedor con dominio peruano; FUMOSAC e ICOFESA sí tienen esa línea |
| 12 | Crear guías técnicas: K7, K9 y C40; clases EN 124; válvula de aire; compuerta para HDPE | Ningún competidor directo lo cubre con profundidad |
| 13 | Enlazar cada sector con sus fichas | Hoy cada sector enlaza una sola ficha |
| 14 | Publicar PDF de ficha por producto | FUMOSAC 17 de 20; FUNDIGSAC 3 |
| 15 | Publicar condiciones de despacho a regiones | Base de la cobertura nacional |

### Prioridad 2: según resultados y decisión comercial

| # | Acción | Condición |
|---|---|---|
| 16 | Tablas de conformidad con CTPS-ET de SEDAPAL | Solo con ensayo o aprobación documentada |
| 17 | Páginas por región o EPS | Solo con entregas u obras reales que se puedan publicar |
| 18 | Categorías HDPE, equipos y medidores | Decisión comercial y datos revisados |
| 19 | Hidrantes y tapas de material compuesto | Decisión comercial |
| 20 | Casos de obra | Autorización del cliente |

No se recomienda competir en contra incendios UL/FM sin listado demostrable, ni en número de referencias frente a ICOFESA.

## 9. KPI de FUNDIGSAC

Requisito del usuario: toda corrección debe medir todos los KPI y quedar en verde antes de darse por terminada. Esta tarea produjo solo documentos y no cambió el código del sitio. Se midió el estado actual para fijar la línea de base.

**Resultado: los KPI no están en verde.** No hay 14 de 14 en móvil. La tabla coincide con las medianas de las 84 corridas (control en `FUENTES.md`). La medición se hizo el 9 de noviembre entre las 12:41 y las 12:53, hora de Lima. La revisión posterior de estos documentos tampoco cambió el sitio; cualquier cambio en `Frontend` obliga a repetirla.

| Corrida | `Frontend/scripts/perf/kpi-gate.mjs`, Lighthouse 13.5.0, 3 corridas por ruta y factor, mediana |
|---|---|
| Compilación | Local y temporal, con `SITE_INDEXABLE=true` y `NEXT_PUBLIC_SITE_URL=http://127.0.0.1`, ya eliminada |
| Umbrales | Puntuaciones de 90 o más; LCP hasta 2.500 ms; CLS hasta 0,1; TBT hasta 200 ms; FCP hasta 1.800 ms; SI hasta 3.400 ms |
| Registro | `Report/kpi/fundigsac-indexable.jsonl`, 84 corridas |

| Ruta | Móvil: rendimiento | Móvil: LCP (ms) | Móvil: estado | Escritorio: rendimiento | Escritorio: estado |
|---|---:|---:|---|---:|---|
| `/` | 82 | 4.815 | Falla | 98 | Verde |
| `/productos` | 85 | 4.361 | Falla | 96 | Verde |
| `/productos/valvulas` | 83 | 4.641 | Falla | 98 | Verde |
| `/productos/tuberias` | 88 | 3.989 | Falla | 99 | Verde |
| `/productos/marcos-y-tapas` | 80 | 5.256 | Falla | 98 | Verde |
| `/productos/valvulas/valvula-compuerta-fundigsac` | 82 | 4.968 | Falla | 98 | Verde |
| `/productos/valvulas/valvula-check-swing` | 88 | 3.987 | Falla | 100 | Verde |
| `/industrias` | 88 | 3.912 | Falla | 99 | Verde |
| `/industrias/saneamiento` | 85 | 4.334 | Falla | 99 | Verde |
| `/industrias/mineria` | 84 | 4.537 | Falla | 99 | Verde |
| `/industrias/agricultura` | 85 | 4.287 | Falla | 98 | Verde |
| `/nosotros` | 87 | 4.029 | Falla | 100 | Verde |
| `/contacto` | 86 | 4.088 | Falla | 99 | Verde |
| `/cotizar` | 91 | 3.535 | Falla (solo LCP) | 100 | Verde |

En las 14 rutas y ambos factores, SEO da 100, buenas prácticas 100 y CLS 0. Accesibilidad da 100, salvo 94 en `/productos/valvulas` en escritorio, que cumple el umbral pero conviene revisar. TBT, FCP y SI cumplen.

Notas de lectura:

- El SEO 69 registrado en `Report/kpi/fundigsac.jsonl` se debe a la cabecera `X-Robots-Tag: noindex` en cualquier host distinto del canónico y al `noindex` previo al lanzamiento. Con indexación activa y host canónico coincidente, el resultado local fue 100. No indica un defecto de SEO, pero tampoco es una medición de producción.
- El elemento LCP medido en `/` es la foto del hero y en `/productos/marcos-y-tapas` es la sección del hero. La causa exacta no se investigó.
- Lighthouse aplica red móvil simulada. Hace falta repetir la medición en producción, con PageSpeed y clave de API.

## 10. Requiere validación de FUNDIGSAC

Nada de esta lista debe publicarse o mantenerse publicado sin el documento indicado.

| Id | Dato | Dónde aparece | Qué se necesita |
|---|---|---|---|
| V-01 | RUC 20601839281. No pasa el dígito verificador de SUNAT: con esos 10 primeros dígitos el último debería ser 9 | `shared/config/site.ts` | Ficha RUC |
| V-02 | Dirección Jirón Pacasmayo Mz. E Lt. 12, Cercado de Lima. El código indica que las webs publican direcciones distintas. **Es la misma dirección que M&L Negofer declara en su `LocalBusiness`** | `site.ts`, `location.ts`, `site-info.ts`, `datos/negofer.json` | Dirección fiscal y dirección de atención, y aclarar la coincidencia con Negofer |
| V-03 | Correo oficial: `cotizaciones@` frente a `ventas@` | `site.ts`, `site-info.ts` | Decisión de la empresa |
| V-04 | Horario "Todos los días, de 08:00 a 19:00" | `site-info.ts` | Confirmación |
| V-05 | Si el local atiende público o solo reparte | Requisito de Business Profile | Confirmación |
| V-06 | Envíos a regiones: alcance, plazos y transportistas | Texto antiguo del WordPress | Condiciones comerciales |
| V-07 | ¿Fabricante, importador o ambos? La búsqueda de marca muestra descripciones distintas y dos denominaciones de la empresa | `fundigsac.com`, fichas | Definición y sustento |
| V-08 | Normas en fichas de compuerta: EN 1074-2, EN 1171, ISO 7259, DIN 3352 F4, AWWA C509 y otras | `valve-sheets`, `w06-ficha-data` | Certificado, ensayo o ficha del fabricante |
| V-09 | "En conformidad con WRAS" en la ficha de garantía extendida | Ficha FT-HD N.° 002-2024 | Certificado WRAS vigente |
| V-10 | Garantía extendida: plazo y condiciones | Ficha de garantía | Documento de garantía |
| V-11 | "Productos certificados y de calidad" y "Stock disponible para proyectos" | `/productos/valvulas` | Sustento o retiro |
| V-12 | Dataset `modules/catalog/data.ts`: SKU, rangos, SEDAPAL, OTASS, WRAS, "Stock Lurín", "Despacho 24h", "Fabricación 72h". Lo usan asistente, carrito y buscador | `assistant/*`, `cart-products.ts`, `search.ts` | Sustituir por catálogo oficial |
| V-13 | Tubería C40, K9, K7, EN 545 PN16, ISO 2531, DN80 a DN600 | Lista de precios, marcada para revisión técnica | Revisión de Ingeniería y certificado |
| V-14 | Marco y tapa D400 (2SEG 60 kg y 1SEG 38 kg, 600 mm) y "fabricado según la norma EN 124" | Lista de precios, `w05-marcos-copy` | Informe de ensayo |
| V-15 | NTP 350.085 frente a NTP 350.106 y NTP 350.064, que cita FUMOSAC | `data.ts` | Revisión técnica de cada norma |
| V-16 | Relación y autorización para usar la marca H-ITALY | Ficha `valvula-compuerta` | Autorización |
| V-17 | Mariposa, guillotina y aire: el WordPress antiguo y la lista de precios no coinciden | `fundigsac.com/product/*`, `catalog-pdf.ts` | Definir la versión vigente |
| V-18 | Tubería HDPE: la categoría la anuncia, y en `catalog-pdf.ts` solo figuran accesorios HDPE | `registry.tsx`, `w04-tuberias-copy` | Confirmar si se vende |
| V-19 | Cualquier relación con SEDAPAL, OTASS o EPS y cumplimiento de CTPS-ET-013, 017, 018 o 019 | Propuestas de contenido | Aprobación o protocolo de ensayo |
| V-20 | Clientes, obras, cifras y años de experiencia | No publicados hoy | Autorización de cada cliente |
| V-21 | Fotografías de producto reales y autorizadas | `imageIllustrative`, recortes | Revisión de medios |
| V-22 | Titularidad de la ficha de Google Maps "FUNDIGSAC" enlazada en `location.ts` | `location.ts` | Acceso de la empresa |
| V-23 | Uso en minería: "pulpas", "condiciones abrasivas" y "minería a gran escala" para la válvula de compuerta | `industrias/mineria/copy.ts` | Respaldo técnico o retiro. Sin él no se publica contenido de pulpas o relaves |
| V-24 | Tarjetas sin código ni ficha: tubería con bridas, con revestimiento, con mortero, unión junta y unión mecánica; tapa circular, tapa para válvula, marco rectangular y tapa de registro | `w04-tuberias-copy`, `w05-marcos-copy` | Confirmar si se venden y con qué datos |
| V-25 | "Brida ISO 2351 PN16" (BISO, BCIEGA). **Inferencia:** posible errata de ISO 2531 | `catalog-pdf.ts` | Revisar la lista de precios y la norma correcta |

## 11. Pendientes del estudio

1. Medir PageSpeed de competidores con clave de API. Hasta entonces no hay comparación real de rendimiento.
2. Decidir el tratamiento de Válvulas Perú y `valvulasperu.com.pe`.
3. Rastrear a Fiorella, Valvoline Perú y Grupo Hidráulica. Ya constan en `COMPETIDORES.md`, sin ficha ni datos propios.
4. Revisar en `scrape.py` la expresión `RUTA_DE_PRODUCTO`, que marca `/productos/categoria/` como ficha, y añadir `sesion.php` y `carrito8.php` al filtro de rutas excluidas.
5. Completar las muestras parciales: categorías de válvulas y tubería de ICOFESA, fichas de Collaval y páginas 2 a 11 de válvulas de Negofer.
6. Obtener datos reales de Search Console tras el lanzamiento. Sustituyen a la búsqueda usada aquí.

## 12. Fuentes de las búsquedas

La lista completa de resultados de las 31 búsquedas está en `FUENTES.md`.

Especificaciones públicas: [CTPS-ET-013](https://cdn.www.gob.pe/uploads/document/file/5976787/5295689-ctps-et-013-valvula-de-compuerta-de-fierro-fundido-ductil-para-agua-potable.pdf?v=1709664884), [CTPS-ET-017](https://www.sedapal.com.pe/storage/objects/ctps-et-017-valvula-de-hierro-ductil-3-funciones-ap.pdf), [CTPS-ET-018](https://cdn.www.gob.pe/uploads/document/file/5976798/5295689-ctps-et-018-rev-02.pdf?v=1712781111), [CTPS-ET-019](https://www.sedapal.com.pe/storage/objects/ctps-et-019-valvula-reductora-presion-hidraulica.pdf), [CTPS-ET-034](https://www.sedapal.com.pe/storage/objects/ctps-et-034-filtro-tipo-cesto.pdf), [CTPS-ET-041](https://www.sedapal.com.pe/storage/objects/ctps-et-041-valvula-de-control-de-bomba-para-agua-potable.pdf), [CE.040 Drenaje pluvial](https://cdn.www.gob.pe/uploads/document/file/2366728/CE.040%20DRENAJE%20PLUVIAL_RM%20126-2021-VIVIENDA.pdf).

Competidores y otros resultados: [ICOFESA](https://icofesa.com/), [Fiorella Representaciones](https://www.fiorellarepre.com.pe/), [Valvoline Perú](https://www.valvoline-peru.com/), [Hi Perú](https://www.hiperusac.com.pe/), [Collaval Import](https://collavalimport.com/), [Rivali Perú](https://rivaliperu.com/), [Leoneblu](https://leoneblusac.com/producto.php?id=13566), [Grupo Hidráulica](https://grupohidraulica.com/producto/marco-y-tapa-de-buzon-hd-d400-nf-en124/), [Orbe](https://orbe.com.pe/producto/tee-bridado-hierro-ductil/), [Redline Perú](https://redlineperu.pe/producto/tee-bridado-de-hierro-ductil/), [PATMO Perú](https://patmoperu.com/tuberias/hierro-ductil/), [Romicorp](https://romicorp.com.pe/hierro-ductil-accesorio.html), [The Atlantic](https://theatlantic.pe/producto.php?id=21117), [Tecval](https://tecval.pe/division-suministros/), [Termofusión y Riego](https://termofusion-riego.com/categoria-producto/hierro-ductil/), [FUNDIGSAC, WordPress anterior](https://fundigsac.com/).
