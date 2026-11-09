# M&L Negofer SAC

| Campo | Valor |
|---|---|
| Sitio | https://mylnegofersac.com/ |
| Segmento | Distribuidor nacional |
| Fecha de la revisión | 9 de noviembre de 2026 |
| Estado del rastreo | ok |
| Páginas con datos | 40 de 40 solicitadas (tope del estudio) |
| Solicitudes HTTP | 41, incluida robots.txt |
| URL descubiertas sin visitar | 226 |
| PageSpeed móvil | n/d (cuota de la API agotada) |
| Datos en bruto | `Report/competencia/datos/negofer.json` |

## Resumen

M&L Negofer tiene un catálogo amplio y bien enlazado. Se vieron al menos 212 URL de producto distintas y cubre las cuatro líneas de FUNDIGSAC, además de HDPE, PVC, medidores e hidrantes. Su punto débil es la información técnica: de las 15 fichas revisadas, solo 2 dejaron algún par atributo-valor legible, ninguna citó una norma y el catálogo descargable es de 2020. Ahí FUNDIGSAC puede diferenciarse.

Convención de este informe: lo que no lleva marca es un hecho observado en los datos del rastreo. Lo que se deduce de esos hechos va marcado como **Inferencia**.

## Alcance y limitaciones

- Se visitaron la portada, 24 páginas de categoría y 15 fichas de producto. El tope de 40 páginas se agotó antes de revisar la mayor parte del catálogo.
- De la categoría Válvulas solo se visitó la primera de sus 11 páginas. Tampoco se visitó la ficha de la tubería K-7 y K-9. Lo que no aparece en este informe puede existir en páginas no visitadas.
- El rastreo usa HTTP simple, sin renderizar JavaScript. No se evaluó el aspecto visual, los botones flotantes ni el comportamiento en móvil.
- El rastreador no guarda precios, texto de botones ni enlaces externos, como los de WhatsApp.
- El PDF del catálogo no se descargó.
- robots.txt está presente, sin demora de rastreo y sin rutas omitidas para este estudio. Declara `wp-sitemap.xml`. No hubo respuestas 403 o 429, captcha ni página de desafío.

## PageSpeed móvil

La API pública respondió HTTP 429 (`RESOURCE_EXHAUSTED`, `rateLimitExceeded`) en la primera y única llamada. Se registra **n/d**. No se midió ningún KPI de rendimiento ni de SEO con esta herramienta.

Como dato aparte, que no sustituye a PageSpeed, el HTML pesa 228 KB de media por página y 468 KB en la portada. **Inferencia:** ese peso apunta a un maquetador de WordPress con mucho código en línea, lo que tiende a perjudicar el rendimiento en móvil.

## Catálogo y familias

El menú presente en las 40 páginas enlaza 13 categorías: Abrazaderas, Accesorios, Acoples y Juntas Mecánicas, Bridas (rompe agua y ciegas), Canastillas y Filtro, Griferías, Grifos contra Incendio, Línea HDPE, Línea PVC, Marco y Tapas, Medidores, Tuberías y Válvulas. Existe además una categoría de marca, M&L Negofer SAC.

| Categoría | Páginas de listado | Observación |
|---|---|---|
| Válvulas | 11 | La mayor. Solo se revisó la primera página |
| Accesorios | 7 | 59 productos listados |
| Acoples y Juntas Mecánicas | 5 | Dresser, autoportantes, adaptadores, electrofusión |
| Línea HDPE | 4 | Termofusión, electrofusión, marca Plasson |
| Marco y Tapas | 4 | Buzón, medidor, telecomunicaciones D400 |
| Bridas, Rompe Agua, Ciegas | 3 | ISO PN16, ANSI 150 lb |
| Medidores | 3 | Elster, Zenner, BMeters |
| Abrazaderas | 2 | De toma, reparación, hierro dúctil |
| Línea PVC | 2 | UF, válvulas PVC, Concyssa |
| Tuberías | 2 | Hierro dúctil K-7 y K-9, SCH-40, HDPE, PVC |
| Canastillas y Filtro | 1 | 7 productos |
| Grifos contra Incendio | 1 | 5 productos |
| Griferías | 1 | Sin productos listados |

Recuento aproximado por palabra clave en las 212 URL de producto vistas. Una URL puede contar en varias familias.

| Familia | URL |
|---|---|
| Bridados | 60 |
| Válvulas (todas) | 43 |
| Uniones, acoples y adaptadores | 40 |
| HDPE | 32 |
| Hierro dúctil (por nombre: HD, Luflex, Push-On) | 29 |
| Tuberías | 19 |
| PVC | 10 |
| Medidores | 9 |
| Marcos y tapas | 8 |
| Válvulas de aire | 5 |
| Hidrantes y grifos | 5 |

Marcas visibles en los nombres de producto: M&L (propia), FUMOSAC, PAM, Plasson, Zenner, Elster, BMeters, Concyssa, Yasel, VAE Italy, A.R.I., Netafim, Cimval y Maxifit.

**Inferencia:** es un distribuidor multimarca con marca blanca M&L. Compite por amplitud de catálogo, y su fuerza está en las conexiones y uniones para obra.

Las válvulas mariposa no aparecen en ninguna de las URL ni títulos vistos, pero faltan 10 páginas de la categoría. No puede afirmarse que no las venda. Tampoco aparecen en la muestra la ventosa trifuncional ni la C40, que `COMPETIDORES.md` sí registra, lo que confirma que la muestra es incompleta.

## Profundidad de especificaciones

- Solo 2 de las 15 fichas dieron pares atributo-valor: presión PN10 o PN16 y accionamiento por volante o dado. El extractor solo lee tablas y listas con formato "atributo: valor", así que puede haber datos en párrafos que no capturó.
- 12 de las 15 fichas tienen un encabezado descriptivo propio, por lo que sí incluyen algo de texto. Las 3 restantes, de la familia Luflex Embone, no lo tienen.
- Los datos técnicos aparecen sobre todo en los nombres: DN50 a DN600, PN-6 a PN-16, S25 y S20, K-7 y K-9, SCH-40, D400, SDR11 y ANSI 150 lb.

**Inferencia:** el comprador técnico no encuentra en la ficha una tabla comparable de diámetros, presiones, materiales y recubrimientos, y debe pedir la información por cotización.

## Normas y certificaciones

| Norma | Dónde aparece |
|---|---|
| EN 124 | Categoría Marco y Tapas |
| ISO 2531 | Nombres de productos en Accesorios (páginas 3 y 5) |

- Solo 3 de las 40 páginas citan alguna norma, y ninguna de ellas es una ficha de producto.
- El rastreador buscó en el texto visible completo y no detectó NTP, AWWA, EN 545, ISO 4179, NSF ni ISO 9001.
- No aparece SEDAPAL en títulos, encabezados ni enlaces. Esa comprobación no cubre el texto completo.
- El catálogo PDF de 2020 no se revisó y podría citar más normas.

## Palabras clave objetivo

Todo este apartado es **inferencia** a partir de títulos, descripciones y encabezados.

| Intención | Términos |
|---|---|
| Marca y categoría principal | válvulas y acoples de hierro dúctil Perú, importadores ferreteros, válvulas industriales |
| Categorías trabajadas a mano | válvulas de compuerta, check y aire en Perú; tubería y accesorios HDPE en Perú; marcos y tapas para buzón y medidor en Perú |
| Categorías con plantilla | abrazaderas en Perú, tuberías en Perú, medidores en Perú, grifos contra incendio en Perú |
| Cola larga de producto | válvula de aire triple efecto, válvula compuerta bridada con adaptador HDPE, balde de prueba hidráulica, codo luflex embone |
| Sectores en portada | minería, saneamiento, agricultura, construcción, industria |

Títulos: 40 únicos; 3 superan los 60 caracteres (máximo 77). Descripciones: 30 únicas, porque las 10 páginas paginadas repiten la de su categoría; 2 superan los 160 caracteres.

**Inferencia:** Válvulas, HDPE y Marcos y Tapas, junto con la ficha del balde de prueba, recibieron un trabajo de SEO reciente. Sus títulos son específicos, invitan a pedir precio por WhatsApp y llevan FAQ, mientras que el resto sigue una plantilla "X en Perú".

## Marcado de esquema

| Tipo | Páginas | Dónde |
|---|---|---|
| Product | 15 | Todas las fichas visitadas |
| WebPage, BreadcrumbList, ImageObject | 16 | Portada y fichas |
| FAQPage | 4 | Válvulas, HDPE, Marcos y Tapas, ficha del balde |
| Organization, LocalBusiness, WebSite, SearchAction | 1 | Solo portada |

- 21 de las 24 páginas de categoría no tienen ningún JSON-LD. Las otras 3 solo tienen FAQPage. Ninguna tiene BreadcrumbList ni ItemList.
- Los datos de migas contienen una entidad mal codificada: `M&amp;#038;L`.
- El rastreador no guarda las propiedades internas de Product, por lo que no se comprobó si incluye precio, marca o disponibilidad.

## Enlazado interno

- Las 40 páginas enlazan la portada, la tienda, las 13 categorías y las páginas legales. La cobertura hacia las categorías es total.
- Cada ficha enlaza 4 productos relacionados. Algunas enlazan a etiquetas de producto; se vieron 4.
- Las páginas de listado usan paginación numerada.
- No se vieron enlaces a Nosotros, Contacto, Proyectos, Blog ni páginas de sector en ninguna de las 40 páginas. Quiénes somos y Contacto son secciones de la portada.
- La categoría Griferías recibe enlaces desde las 40 páginas y no lista productos.

**Inferencia:** los productos relacionados se eligen de forma casi aleatoria entre familias. Por ejemplo, una Yee bridada enlaza a un kit de varillas de desatoro. Esto reparte autoridad, pero aporta poco al usuario.

## Llamadas a la acción

- Las descripciones repiten "Solicita tu cotización", y en fichas, "cotización y ficha técnica".
- Las categorías trabajadas invitan a pedir precio y ficha técnica por WhatsApp.
- En la portada hay accesos del tipo "Ver Válvulas" y "Ver Marcos y Tapas", el catálogo 2020 descargable y una invitación a formar parte de su red de distribuidores.
- En las fichas hay un bloque para compartir el producto.

**Inferencia:** el modelo es de cotización asistida por WhatsApp, sin compra en línea, y la red de distribuidores indica que también busca el canal mayorista.

## Señales de SEO local

- LocalBusiness con dirección en Jr. Pacasmayo Mz. E Lt. 12, Cercado de Lima, y horario, solo en la portada. Es la misma dirección que publica FUNDIGSAC; el rastreo no explica la coincidencia (informe, V-02).
- Tres teléfonos móviles con prefijo +51 y un correo genérico de ventas.
- "en Perú" en los títulos y "envíos nacionales" en las descripciones.
- Libro de reclamaciones enlazado en las 40 páginas.
- No se vieron páginas por ciudad o región.

## Experiencia de usuario

Solo se evaluó lo que se deduce de la estructura. No hubo revisión visual.

Fortalezas:

- Navegación por categorías constante en todo el sitio, con una ruta clara de portada a categoría y a ficha.
- Títulos únicos y URL legibles en todas las páginas revisadas.
- Vía directa hacia la cotización.

Debilidades:

- Los listados muestran 9 productos por página, lo que obliga a recorrer hasta 11 páginas en Válvulas. **Inferencia:** el rastreo no detectó filtros por diámetro o presión, aunque podrían no ser visibles sin JavaScript.
- Productos casi duplicados: "Tee HDPE Termo fusión" y "Tee termo fusión HDPE", o nombres con sufijo como "Unión tipo Dresser Maxifit 2".
- Errores en el contenido: "DESCATADOS", "Boncre", "Dreser", "Vitaulic", "Linea PVC".
- Catálogo de 2020 todavía destacado en portada, e imágenes de fichas subidas sobre todo en 2021. **Inferencia:** el contenido base lleva años sin revisión.
- Categoría Griferías vacía, y una categoría de marca mezclada con las de producto.
- El H1 de la portada es "VÁLVULAS INDUSTRIALES", más estrecho que su oferta real.

## Oportunidades para FUNDIGSAC

Todas son **inferencias** y recomendaciones. Las normas de FUNDIGSAC citadas abajo salen de `Frontend/src/modules/catalog/data.ts`, cuya cabecera lo declara dataset de maqueta. No son datos verificados y antes de citarlas hacen falta documentos vigentes (informe, sección 10, V-12).

1. **Ganar en la ficha técnica.** Mantener en cada producto la tabla de DN, PN, material y recubrimiento, con PDF descargable. Es la mayor brecha frente a Negofer.
2. **Citar normas por producto.** FUNDIGSAC declara EN 1074, EN 1171, DIN 3202, EN 593 y NTP. Negofer solo muestra EN 124 e ISO 2531 en 3 páginas. Conviene agregar certificados o informes de ensayo descargables.
3. **Superar en marcos y tapas.** Negofer ya trabaja esa categoría con EN 124. Una página con clase D400, carga de ensayo, dimensiones y seguro, comparando los modelos, puede competir directamente por "marco y tapa D400 Perú".
4. **Válvulas mariposa.** Antes de priorizar, comprobar las páginas restantes de Válvulas. Si Negofer sigue sin ofrecerlas, es una categoría donde FUNDIGSAC llega sin competencia directa de este rival.
5. **Filtros por DN, PN y unión.** Ayudan justo donde Negofer obliga a paginar. También permiten comparar frente a su lista de 11 páginas.
6. **Contenido técnico.** No se vio blog ni guías en Negofer. Temas de valor: K7 frente a K9, cómo elegir una válvula de aire, clases de EN 124, ventajas de la unión autoportante.
7. **Páginas por sector.** Negofer nombra cinco sectores en portada sin páginas propias vistas. FUNDIGSAC ya tiene la ruta `/industrias` y puede profundizarla con casos de minería y saneamiento.
8. **Schema en categorías.** Agregar BreadcrumbList e ItemList a los listados, que Negofer no tiene. No conviene esperar mucho de FAQPage, porque Google limitó esos resultados enriquecidos desde 2023.
9. **Cola larga de combinaciones.** Negofer tiene fichas de válvula con adaptador HDPE. Si FUNDIGSAC puede suministrarlas, conviene crear páginas para esas combinaciones.
10. **Cobertura regional.** Negofer no tiene páginas por región. Solo conviene crearlas donde FUNDIGSAC pueda demostrar entregas o proyectos reales.
11. **Catálogo vigente.** Publicar un catálogo fechado y actualizado frente al de 2020 de Negofer.

## Acciones pendientes

1. Repetir la medición de PageSpeed móvil cuando se recupere la cuota.
2. Revisar las páginas 2 a 11 de Válvulas y la ficha K-7 y K-9 en una ronda posterior, dentro del tope de páginas.

## Notas de método

- El rastreo se ejecutó una sola vez dentro de la imagen `fundig-scrapling`, con el Fetcher HTTP simple y el User-Agent del estudio. Un primer intento falló por un error de argumentos antes de hacer ninguna solicitud.
- Esta revisión no incluyó correcciones en los sitios de FUNDIGSAC, por lo que no hubo KPI propios que medir.
