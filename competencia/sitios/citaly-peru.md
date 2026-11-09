# Citaly Perú

| Campo | Valor |
|---|---|
| Sitio | https://citalyperu.com/ |
| Segmento | Importador |
| Fecha de la revisión | 9 de noviembre de 2026 |
| Estado del rastreo | ok |
| Páginas con datos | 40 de 40 permitidas (26 fichas de producto y 14 listados) |
| PageSpeed móvil | n/d (cuota de la API agotada) |
| Datos en bruto | `Report/competencia/datos/citaly-peru.json` |

## Resumen

Citaly es una tienda WooCommerce con 53 URL de producto y marca propia C-Italy. Su oferta se concentra en válvulas de hierro dúctil, accesorios para unir tubería PVC y HDPE, conexiones bridadas y una línea de bronce. Su mejor recurso de posicionamiento son los nombres de producto que indican la tubería compatible, como "para tubería PVC" o "para tubería HDPE".

Sus debilidades son claras en lo que se pudo medir: ninguna norma citada en las 40 páginas, ninguna ficha con H1, sin marcado `Product` ni de empresa, y especificaciones técnicas solo en 6 de 26 fichas. Marcos y tapas, la línea por la que entró en el listado de competidores, tiene un solo producto.

## Alcance y límites

Los datos describen lo que se pudo observar. Cada ausencia indicada abajo vale solo para las páginas y campos revisados.

- El tope de 40 páginas se alcanzó y quedaron 30 URL sin visitar. Se visitaron 26 de las 53 fichas de producto.
- No se visitaron `/nosotros/` ni `/contactanos/`, porque el rastreador prioriza categorías y productos. Tampoco la ficha de marco y tapa D400.
- `robots.txt` existe, no declara `Crawl-delay` y no excluyó ninguna de las URL solicitadas. Publica el mapa `wp-sitemap.xml`, que no se descargó.
- No se abrieron los PDF, por lo que su contenido técnico se desconoce.
- El rastreador no guarda enlaces externos. No se puede afirmar si hay WhatsApp o redes sociales.
- Tampoco guarda el texto completo ni precios. El sitio se leyó como HTML, sin renderizar, así que no hay evaluación visual.
- El detector de normas busca códigos como `ISO 2531` o `EN 124` en el texto visible. No detecta afirmaciones libres como "producto certificado".

## KPI medidos

| Indicador | Resultado |
|---|---|
| PageSpeed móvil, rendimiento y SEO | n/d |
| Páginas con título | 40 de 40 |
| Títulos de más de 60 caracteres | 3 de 40; el de portada tiene 217 |
| Títulos duplicados | 1 caso, en dos fichas |
| Páginas con meta descripción | 10 de 40, todas fichas de producto |
| Meta descripciones de más de 160 caracteres | 10 de 10 |
| Páginas con H1 | 14 de 14 listados; 0 de 26 fichas |
| Páginas con canónica | 26 de 26 fichas; 1 de 14 listados (solo portada) |
| Páginas con JSON-LD | 26 de 40, solo `BreadcrumbList` |
| Páginas con normas citadas | 0 de 40 |
| Fichas con especificaciones extraídas | 17 de 26 |
| Fichas con rango DN concreto | 6 de 26 |
| Fichas con presión nominal | 10 de 26 |
| Fichas con enlace a PDF técnico | 2 de 26 |
| Peso del HTML | 130 KB de media; 195 KB la portada |

El rastreador usa `og:description` cuando falta la meta descripción, de modo que algunas de las 10 pueden proceder de esa etiqueta.

## Cobertura de catálogo y familias

La tienda se pagina en 5 páginas y enlaza 53 URL de producto con 51 nombres distintos. La diferencia se debe a nombres repetidos, como el adaptador brida para HDPE, que tiene dos URL con el mismo título.

| Familia | Ruta | Nombres listados | Productos |
|---|---|---|---|
| Válvulas de hierro dúctil | `/product-category/valvulas-hierro-ductil/` | 11 | Compuerta bridada, Luflex embone, para PVC, tipo dado para HDPE y C-Italy Premium; mariposa con palanca, con timón y con brida loca PVC; aire triple efecto; reductora de presión (2) |
| Accesorios de hierro dúctil | `/product-category/accesorios-hierro-ductil/` | 9 | Adaptadores brida para PVC y HDPE, adaptador brida universal, adaptador rápido HDPE, adaptador brida acerrojado HDPE, acerrojado, acople 995, unión de desmontaje autoportante, unión Dresser |
| Conexiones de hierro dúctil | `/product-category/conexiones-hierro-ductil/` | 8 | Yee, cruz, niple, reducción, tee, tee con reducción, codos 45° y 90°, todos bridados |
| Línea de bronce | `/product-category/linea-de-bronce/` | 9 | Válvulas esférica, compuerta, flotador y check; caños de jardín y lavandería |
| Medidores | `/product-category/medidores/` | 3 | Tipo Waltman (así escrito), chorro único, chorro múltiple |
| Fierro galvanizado | `/product-category/fierro-galvanizado/` | 2 | Unión espiga, niple rosca escama |
| Hidrantes | `/product-category/hidrantes/` | 1 | Hidrante de cuerpo húmedo |
| Marcos y tapas | `/product-category/marcos-y-tapas/` | 1 | Marco y tapa de buzón D400 con doble seguro |

Otros 7 nombres aparecen en la tienda y en ninguna de las 8 categorías rastreadas: tubería HDPE línea roja y azul, tee, reducción, codo 45° y codo 90° en HDPE (rotulados "Exclusivo C-italy"), y válvula check paleta de bronce "Nacional".

No figura ningún producto llamado tubería de hierro dúctil ni válvula check de hierro dúctil. Las válvulas check listadas son de bronce. El título de portada anuncia "tuberías y conexiones en PVC", pero ningún producto listado es tubería o conexión de PVC; PVC aparece solo como compatibilidad.

Inferencia: Citaly no compite hoy en tubería de hierro dúctil y su fuerza está en la válvula con extremos adaptados a PVC y HDPE, un mercado de obra de agua potable y riego.

Inferencia: el catálogo se mantiene activo. De los 28 archivos enlazados en `wp-content/uploads`, 5 son de 2026, con los más recientes en agosto.

## Profundidad de especificaciones

Las 26 fichas revisadas se dividen en cuatro niveles.

| Nivel | Fichas | Detalle |
|---|---|---|
| Datos técnicos con DN | 6 | Ver tabla siguiente |
| Presión sin diámetro concreto | 4 | Unión de desmontaje, unión Dresser, adaptador rápido HDPE y adaptador brida universal: PN10 y PN16, con "variedad de diámetros" |
| Solo beneficios o usos | 7 | Compuerta para PVC, compuerta tipo dado HDPE, reductora para PVC, 3 adaptadores brida, acerrojado |
| Sin atributos extraídos | 9 | Yee, cruz, reductora de presión, medidor Waltman, esférica cromada, compuerta Premium, unión espiga, niple rosca, acople 995 |

| Producto | DN | PN | Temperatura |
|---|---|---|---|
| Mariposa con palanca | DN50 a DN1200 | PN10, PN16 | -10 a +80 °C |
| Mariposa con timón | DN50 a DN1200 | PN10, PN16 | -10 a +80 °C |
| Mariposa con brida loca PVC | DN50 a DN300 | PN6, PN10 | -10 a +60 °C |
| Compuerta Luflex embone | DN50 a DN600 | PN10, PN16 | -10 a +80 °C |
| Compuerta bridada | DN50 a DN600 | PN10, PN16 | -10 a +80 °C |
| Aire triple efecto | DN50 a DN300 | PN10, PN16 | -10 a +80 °C |

El rastreador lee pares atributo-valor en tablas y listas. Si un dato está en un párrafo o en una imagen no se cuenta, de modo que estas cifras son un mínimo.

No se extrajeron dimensiones, materiales por componente ni tablas por diámetro. Las fichas enlazan dos PDF, publicados en mayo de 2026: compuerta Luflex y unión Dresser de gran rango.

Inferencia: parte del texto técnico es genérico. La mariposa con palanca y la de timón repiten los mismos rangos, incluido DN1200, un diámetro poco habitual para accionamiento por palanca.

## Normas y certificaciones citadas

No se encontró ningún código de norma en las 40 páginas revisadas: ni ISO, EN, AWWA, NTP o ASTM. Tampoco aparece SEDAPAL en títulos, descripciones, encabezados o nombres de producto.

La única referencia normativa indirecta es "D400" en el nombre del marco y tapa.

Inferencia: D400 alude a la clase de carga de EN 124, aunque el sitio no cite la norma en las páginas revisadas. La ficha de ese producto y los dos PDF no se leyeron, así que pueden incluir más información.

## Palabras clave objetivo

Toda esta sección es inferencia a partir de títulos, encabezados y nombres de producto. No se dispone de datos de posición ni de volumen de búsqueda.

| Grupo | Términos probables |
|---|---|
| Genéricos | válvulas de hierro dúctil, válvulas industriales, importadores de válvulas |
| Compuerta | válvula compuerta de hierro dúctil, válvula compuerta para tubería PVC, válvula compuerta tipo dado para tubería HDPE, válvula compuerta tipo Luflex embone |
| Mariposa | válvula mariposa con palanca, válvula mariposa con timón, válvula mariposa con brida loca PVC |
| Control | válvula de aire triple efecto, válvula reductora de presión |
| Unión | adaptador brida para PVC y HDPE, unión Dresser, unión de desmontaje autoportante, acople 995, acerrojado |
| Conexiones | yee, cruz, tee, codo y reducción bridados de hierro dúctil |
| Saneamiento | marco y tapa de buzón D400 con doble seguro, hidrante de cuerpo húmedo |
| Medición | medidor de agua, chorro único, chorro múltiple |
| Marca | Citaly, C-Italy |

Los títulos siguen el patrón "Nombre de producto – CITALY". No añaden ciudad, marca técnica ni tipo de obra. El término más diferenciador es la compatibilidad con la tubería.

## Marcado de esquema

- Solo se detectan `BreadcrumbList` y `ListItem`, en las 26 fichas.
- Portada, categorías y tienda no tienen JSON-LD.
- No hay `Product`, `Offer`, `Organization`, `LocalBusiness`, `WebSite` ni `FAQPage`.
- La sección "Comentarios y reseñas de clientes" aparece en 14 páginas sin marcado de reseña.

## Enlazado interno

Se observaron 172 rutas internas: 53 de producto, 8 de categoría, 5 de paginación, 4 de navegación, 28 archivos subidos y 74 variantes con `?add-to-cart=`.

| Destino | Páginas que lo enlazan, de 40 |
|---|---|
| `/`, `/nosotros/`, `/shop/`, `/contactanos/` | 40 |
| Válvulas de hierro dúctil | 25 |
| Accesorios de hierro dúctil | 23 |
| Medidores | 15 |
| Línea de bronce | 15 |
| Hidrantes | 13 |
| Marcos y tapas | 13 |
| Conexiones de hierro dúctil | 3 |
| Fierro galvanizado | 3 |

Cada ficha tiene entre 8 y 15 enlaces internos: navegación, miga de categoría y de 1 a 4 productos relacionados. El producto más enlazado de la muestra es `/product/valvula-reductora-de-presion/`, en 11 páginas.

No hay rutas de blog, guías, proyectos, sectores o normas entre las 172 observadas.

Inferencia: la arquitectura es plana y no acumula autoridad temática. Las 74 variantes `add-to-cart` generan ruido de rastreo, y conexiones y galvanizado quedan relegadas por su poco enlazado.

## Llamadas a la acción

| Llamada | Observación |
|---|---|
| "Añadir al carrito" | Enlaces directos para 17 identificadores de producto |
| "Ver válvulas" | Enlace de portada hacia la categoría de válvulas |
| "Descargar ficha técnica" | Texto presente en la descripción de 2 fichas con PDF |
| Contacto | `/contactanos/` en el menú de las 40 páginas |
| Promoción | "Discount up to 35% for first purchase only this month." como H2 en 13 listados |

No hay ruta interna de cotización entre las observadas. No se detectaron enlaces `tel:`. Los enlaces a correos se guardan solo si son buzones genéricos, por lo que su ausencia no es concluyente.

Inferencia: el sitio se orienta a compra directa en lote pequeño más que a cotización de proyecto. El banner en inglés parece texto de plantilla sin editar.

## Señales de SEO local

| Señal | Resultado |
|---|---|
| "Lima" o "Perú" en títulos, descripciones, encabezados y nombres | 0 apariciones; la marca geográfica está solo en el dominio y en un emoji de bandera |
| Idioma del documento | `es`, sin variante `es-PE` |
| JSON-LD de empresa con dirección o teléfono | No |
| Enlaces `tel:` | 0 en 40 páginas |
| Páginas por ciudad o región | No observadas |

La página de contacto no se rastreó y el texto de pie de página no se guarda, de modo que dirección y teléfono pueden existir ahí.

Inferencia: Citaly depende de su marca y del dominio para las búsquedas locales, y no trabaja la intención geográfica de forma explícita.

## Experiencia de usuario

La revisión se basa en la estructura HTML, sin observación visual.

Fortalezas:

- Taxonomía simple, con 8 categorías por material o función.
- Nombres que indican compatibilidad con PVC o HDPE, lo que ayuda a elegir sin asesoría.
- Migas de pan y productos relacionados en las fichas.
- Compra directa con carrito para 17 productos.
- Fichas clave de válvulas con DN, PN y temperatura, y dos PDF descargables.

Debilidades:

- Ningún H1 en las fichas; el nombre del producto está en H2.
- Texto de plantilla en inglés y H1 "Shop" en una tienda en español.
- Errores visibles: "duçtil", "aguatipo WALTMAN", "timon".
- Mayúsculas inconsistentes en los nombres de producto.
- URL poco cuidadas: `-copia`, `-2` y `/product/706/`.
- Tuberías HDPE y sus accesorios sin categoría observada.
- 9 fichas sin atributos extraídos y solo 2 con PDF.
- Título de portada de 217 caracteres y sin meta descripción.

## Oportunidades para FUNDIGSAC

Son recomendaciones propias, es decir, inferencias a partir de los datos anteriores. Las referencias a FUNDIGSAC proceden de `Frontend/src`. Su sitio publicado no se midió en esta revisión.

1. **Normas visibles en cada ficha, con respaldo.** Citaly no cita ninguna, así que es una diferenciación disponible. Las normas de `modules/catalog/data.ts` son textos de maqueta, según la cabecera de ese archivo, y `valve-sheets.ts` no publica certificaciones. FUNDIGSAC debe aportar certificados o ensayos reales antes de citar una norma.
2. **Marcos y tapas D400.** Citaly lista un producto con doble seguro. La lista de precios en `lib/catalog-pdf.ts` tiene dos variantes D400 de 600 mm: pesada con 2 seguros (60 kg) y liviana con 1 seguro (38 kg). Una página por variante, con peso y seguros visibles, permite competir por "marco y tapa de buzón D400". La ficha de Citaly no se leyó, de modo que la comparación técnica queda pendiente.
3. **Válvula por tipo de tubería.** La ficha de Citaly para HDPE solo muestra dos atributos y ningún DN. FUNDIGSAC ya tiene una tabla DN y diámetro de tubo HDPE en `valvula-compuerta-acerrojada`. Falta una página equivalente para PVC y títulos con "para tubería PVC" y "para tubería HDPE".
4. **Válvula check de hierro dúctil.** Citaly solo lista check de bronce. FUNDIGSAC tiene check swing y flex, que pueden capturar esa búsqueda.
5. **Tubería de hierro dúctil.** Citaly no lista este producto, de modo que ahí no compite. Conviene priorizar el esfuerzo frente a otros competidores.
6. **Ficha PDF en todas las válvulas.** Citaly la ofrece en 2 de 26 fichas. Una descarga uniforme, con tabla por diámetro, es una ventaja directa para proyectistas y compras públicas.
7. **Esquema `Product` más rico.** Citaly no tiene `Product`. FUNDIGSAC ya lo emite, con nombre, descripción, imagen, SKU y marca. Se puede añadir `additionalProperty` para DN, PN y material, y la norma solo cuando esté respaldada, sin inventar precios ni reseñas.
8. **Contenido por sector.** Citaly no tiene guías ni páginas de sector. FUNDIGSAC tiene `/industrias`. Conviene enlazar en ambos sentidos cada sector con las fichas que usa.
9. **Intención local.** Citaly no menciona Lima ni Perú en sus campos SEO. FUNDIGSAC ya declara `Organization` con dirección en Lima y `es-PE`. Se puede llevar "Lima" y "Perú" a títulos y descripciones de categorías comerciales.
10. **Vacíos de catálogo por evaluar.** No se encontró hidrante, unión Dresser, línea de bronce ni fierro galvanizado en `lib/catalog.ts` y `lib/catalog-pdf.ts`. Incorporarlos es una decisión comercial, y bronce y galvanizado parecen de ticket bajo.

Cualquier corrección en los sitios de FUNDIGSAC derivada de esta lista debe medir todos los KPI y dejarlos en verde antes de darse por terminada.

## Acciones pendientes

1. Repetir PageSpeed móvil cuando exista cuota. Sin ese dato no se puede comparar rendimiento.
2. Revisar `/nosotros/`, `/contactanos/` y la ficha del marco y tapa D400 en un rastreo aparte, dentro del tope de 40 páginas por sitio.
3. Leer los dos PDF técnicos para confirmar qué normas citan.
4. Determinar si existe vínculo societario con Collaval Import, que comparte la marca C-Italy.

## Notas de método

- El rastreo se ejecutó una sola vez con la imagen `fundig-scrapling`, con Fetcher HTTP simple y el User-Agent `FundigsacMarketResearch/1.0`: 41 solicitudes en 142 segundos, incluida `robots.txt`.
- El sitio no respondió con bloqueos, captcha ni páginas de desafío.
- PageSpeed respondió HTTP 429 (`RESOURCE_EXHAUSTED`, `rateLimitExceeded`, con un límite diario de 0 para la API sin clave). Se hizo una sola llamada y se registra **n/d**.
- Esta revisión no incluyó correcciones en los sitios de FUNDIGSAC, por lo que no hubo KPI propios que medir.
