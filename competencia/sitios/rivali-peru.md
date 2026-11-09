# Rivali Perú

| Dato | Valor |
|---|---|
| Sitio | https://rivaliperu.com/ |
| Segmento | Importador y distribuidor |
| Razón social citada en el sitio | Rivali Perú E.I.R.L. |
| Fecha del rastreo | 9 de noviembre de 2026 |
| Estado del rastreo | ok, 40 páginas con datos en 41 solicitudes HTTP |
| PageSpeed móvil | n/d (la API respondió HTTP 429, `rateLimitExceeded`) |
| Datos de origen | `Report/competencia/datos/rivali-peru.json` |

Todo lo que no lleva la marca **Inferencia** se observó en el HTML público o en el JSON del rastreo.

## Resumen

Rivali es un catálogo WooCommerce amplio y multimaterial, con fuerte peso en sistemas contra incendios y conexiones. Coincide con FUNDIGSAC en válvulas y conexiones de hierro dúctil, pero en las páginas revisadas no aparece tubería de hierro dúctil y marcos y tapas se reduce a una ficha de fierro fundido.

Su punto débil es el contenido técnico y el SEO de categorías: ninguna de las 14 fichas revisadas mostró atributos técnicos estructurados, 23 de 24 categorías tienen el título vacío antes de la marca, y no se detectó ninguna norma técnica salvo las menciones UL y FM en nombres de producto.

## Alcance y límites

- El rastreo se detuvo en el tope de 40 páginas y dejó 184 URL pendientes.
- No se visitaron `/contactenos/`, `/nosotros/`, `/blog/`, `/categoria-producto/valvulas/`, `/categoria-producto/brida/`, `/categoria-producto/medidores/` ni `/categoria-producto/accesorios/`. Lo que se afirma sobre contacto y empresa se limita a las 40 páginas revisadas.
- El catálogo PDF enlazado no se descargó.
- El extractor de especificaciones lee tablas de dos columnas y listas con formato "atributo: valor". Datos técnicos en párrafos, imágenes o PDF no quedan registrados.
- El extractor de normas no incluye UL ni FM. Esas menciones se tomaron de los nombres de producto.
- Se guardaron títulos y encabezados, no el texto de botones ni el cuerpo de las páginas. La lectura de experiencia de usuario parte del HTML y no de una revisión visual.
- robots.txt respondió 200, publica `sitemap_index.xml`, no fija `crawl-delay` y no excluyó ninguna URL solicitada.

## Cobertura del catálogo y familias

Se observaron 173 fichas de producto distintas y 169 nombres de producto. Es un mínimo, porque solo se leyó la primera página de cada listado.

| Categoría | Productos en la primera página | Páginas de listado | Tamaño estimado (**Inferencia**, 12 por página) |
|---|---|---|---|
| Válvulas de hierro dúctil | 12 | 2 | 13 a 24 |
| Válvulas ranuradas | 8 | 1 | 8 |
| Válvulas de bronce | 12 | 2 | 13 a 24 |
| Válvulas de PVC | 7 | 1 | 7 |
| Válvulas inoxidables | 2 | 1 | 2 |
| Sistema contra incendio (padre) | 12 | 4 | 37 a 48 |
| Accesorios contra incendio | 12 | 3 | 25 a 36 |
| Mangueras contra incendio | 2 | 1 | 2 |
| Hidrantes contra incendio | 1 | 1 | 1 |
| Conexiones (padre) | 12 | 10 | 109 a 120 |
| Conexiones de hierro dúctil | 12 | 2 | 13 a 24 |
| Conexiones ranuradas | 12 | 2 | 13 a 24 |
| Conexiones de PVC | 12 | 2 | 13 a 24 |
| Conexiones inoxidables | 12 | 2 | 13 a 24 |
| Conexiones HDPE | 12 | 2 | 13 a 24 |
| Conexiones galvanizadas | 11 | 1 | 11 |
| Conexiones de fierro negro | 8 | 1 | 8 |
| Conexiones al carbono | 5 | 1 | 5 |
| Conexiones soldables | 4 | 1 | 4 |
| Conexiones de bronce | 1 | 1 | 1 |
| Abrazaderas | 9 | 1 | 9 |
| Tuberías contra incendio | 7 | 1 | 7 |
| Marcos y tapas | 1 | 1 | 1 |
| Uniones | 0 | 1 | 0 |

Los productos se repiten entre categorías, por lo que estas cifras no se pueden sumar.

### Coincidencia con las líneas de FUNDIGSAC

| Línea | Presencia en Rivali |
|---|---|
| Válvula compuerta | Sí. 11 nombres, entre ellos bridada de hierro dúctil, UF, con adaptador universal, con stub HDPE y con brida fija UF PVC |
| Válvula mariposa | Sí. 7 nombres: wafer con timón, wafer con palanca, bridada, ranurada con volante, con switch y PVC |
| Válvula check | Sí. 14 nombres: dúo check, vertical, paleta, cortina, swing y canastilla |
| Válvula de aire | Sí, oferta corta: triple efecto de hierro dúctil y triple función Bermad |
| Conexiones de hierro dúctil | Sí. Codos 45 y 90, tee, yee, cruceta, reducción, niples, brida rompe agua y abrazaderas |
| Tubería de hierro dúctil | No se encontró. Cero coincidencias de K7, K9 o C40. Las tuberías vistas son de acero al carbono, inoxidable y galvanizado |
| Marcos y tapas | Una ficha: "Marco para Buzón de Fierro Fundido". No se vio hierro dúctil, D400 ni tapas como producto propio |

Otras familias sin equivalente directo en las líneas analizadas: sistemas contra incendios, HDPE por termofusión y electrofusión, PVC inyectado y medidores de agua.

Marcas o fabricantes citados en nombres de producto: Bermad, Potter, Giacomini, Cifunsa, Mech, CIM, ERA y Kepler. **Inferencia:** el modelo es multimarca. No se verificó ninguna relación comercial con estos fabricantes.

## Profundidad de especificaciones

- Las 14 fichas revisadas registraron cero pares atributo-valor.
- DN y PN no aparecen en títulos, H1, H2 ni en los 173 identificadores de ficha.
- Los datos técnicos visibles están en el nombre del producto: material, tipo de unión (bridada, wafer, ranurada, UF, SP, termofusión, electrofusión, compresión), cédula (SCH 10, 40, 80) y rosca NPT.
- Las fichas tienen `Product`, `Offer` y `UnitPriceSpecification` en JSON-LD. El valor del precio no se guardó.
- Todas las páginas enlazan `CATALOGO-ACTUALIZADO-2025-RIVALI-PERU-min.pdf`.

**Inferencia:** los datos técnicos se concentran en el PDF o en imágenes. Esto no se comprobó.

## Normas y certificaciones citadas

- El detector de normas devolvió cero resultados en las 40 páginas. No hay menciones de ISO, AWWA, NTP ni EN 124 en títulos, encabezados o meta descripciones.
- UL y FM figuran en nombres de producto: Válvula Compuerta OSY UL FM, Cheque Cortina HD Flanchado UL FM, Filtro Yee HD Flanchado UL-FM, Tubo ranurado rojo UL/FM SCH10 – 40, Tapón Ranurado UL FM. FM aparece solo en Válvula Angular Reductora FM Hembra Macho, y "Listada" en Válvula OSY Listada.
- La categoría contra incendios afirma ofrecer "productos certificados" en su meta descripción, sin indicar organismo ni número de certificado.

Estas son declaraciones comerciales y no se verificaron.

## Palabras clave objetivo

**Inferencia** a partir de títulos y encabezados:

| Grupo | Términos |
|---|---|
| Marca y posicionamiento | Rivali Perú, válvulas industriales, sistemas contra incendios |
| Válvulas de hierro dúctil | válvula compuerta bridada hierro dúctil, válvula de aire triple efecto hierro dúctil, válvula dúo check hierro dúctil, válvula mariposa wafer, filtro yee bridado |
| Contra incendios | tubo ranurado rojo UL/FM SCH10, válvula OSY UL FM, cheque cortina UL FM, manguera contra incendio, grifo contra incendio |
| Conexiones | codo 90 bridado hierro dúctil, tee bridado hierro dúctil, conexiones HDPE termofusión, codo electrofusión, PVC ERA inyectado |
| Sectores (solo como H2 de portada) | minería, saneamiento, agricultura, construcción, industria |

Las categorías, que son las páginas con mayor intención comercial, no compiten por sus términos porque su título está vacío. El peso de palabras clave recae en las fichas.

## Marcado de esquema

| Tipo JSON-LD | Páginas |
|---|---|
| WebSite, SearchAction, Organization, BreadcrumbList, ImageObject | 40 de 40 |
| CollectionPage | 24 (categorías) |
| WebPage, ReadAction | 16 |
| Product, Offer, UnitPriceSpecification | 14 (todas las fichas) |

- `Organization` trae el nombre, pero no se registró teléfono, correo de empresa ni dirección.
- No aparecieron `LocalBusiness`, `FAQPage`, `ItemList` ni `Review`.
- **Inferencia:** el conjunto de tipos corresponde a WooCommerce con un complemento SEO del estilo de Yoast.

## SEO en página

| Señal | Resultado |
|---|---|
| Título vacío antes de "\| Rivali Perú" | 23 de 40 páginas (23 de las 24 categorías; solo "Válvulas de PVC" tiene nombre) |
| Sin meta descripción | 37 de 40 páginas. Solo la tienen portada, `/productos/` y sistema contra incendio |
| Sin H1 en el HTML | 26 de 40 páginas: portada, `/productos/` y las 24 categorías. Las 14 fichas sí tienen H1 |
| URL canónica | Presente y propia en las 40 páginas |
| Idioma | `es` |
| Peso del HTML | Promedio 171 KB, máximo 225 KB |

## Enlazado interno

- Estructura en dos niveles: `/categoria-producto/{padre}/{hija}/` y `/producto/{slug}/`.
- El menú global repite 34 enlaces en las 40 páginas. Incluye todas las subcategorías, el PDF, `/carrito/`, `/blog/`, `/nosotros/` y `/contactenos/`.
- Cada ficha enlaza cuatro productos relacionados. **Inferencia:** la relación es automática, porque aparecen mezclas como Tee Mecánica Ranurada con Tee HDPE y Unión PVC.
- Las categorías añaden barra lateral "Categorías" y bloque "Últimas novedades".
- Se contaron 242 enlaces `?add-to-cart=` en las páginas revisadas. No se comprobó si robots.txt los excluye.
- La categoría `/categoria-producto/uniones/` está en el menú de todas las páginas y no muestra productos.
- Hay categorías de un solo producto: hidrantes, conexiones de bronce y marcos y tapas.
- Cinco fichas tienen sufijo numérico: `tee-de-acero-inoxidable-2`, `reduccion-copa-ranurada-rosca-2`, `acople-reductor-ranurado-2`, `adaptador-brida-ranurado-2` y `medidor-de-agua-chorro-multiple-kepler-3`. **Inferencia:** son productos recreados o duplicados.
- Hay nombres casi duplicados, como Válvula Compuerta Pesada de Bronce y Válvula Compuerta Pesada Bronce, o Válvula Check Canastilla de PVC y Válvula Check Canastilla PVC.

## Llamadas a la acción

- Carrito WooCommerce: botón de añadir en listados y enlace a `/carrito/` en el menú.
- Catálogo PDF 2025 en el menú global.
- Widget Joinchat detectado en listados. **Inferencia:** es el botón de WhatsApp.
- Enlace "Ver nuestros productos" en portada, `/contactenos/` en el menú y secciones "Datos de contacto" y "Síguenos en las redes sociales" en el pie.
- "Cotiza" y "precio" no aparecen en títulos ni encabezados. Los botones no se extrajeron, así que esto no descarta un botón de cotización.

## Señales de SEO local

- "Lima" aparece cero veces en títulos, H1, H2 y meta descripciones.
- "Perú" aparece como parte de la marca y una vez en la meta de contra incendios.
- JSON-LD sin dirección ni teléfono. No se usa `LocalBusiness`.
- No se detectó ningún enlace `tel:` ni correo genérico `mailto:` en las 40 páginas.
- No se vieron páginas por ciudad o región.
- `/contactenos/` no se visitó, por lo que la dirección puede figurar allí.

## Fortalezas y debilidades de experiencia de usuario

Fortalezas:

- Catálogo extenso con navegación por material y tipo de unión.
- Fichas con H1 propio, migas de pan y productos relacionados.
- URL legibles con términos de producto.
- Catálogo PDF accesible desde cualquier página.
- Contacto rápido por Joinchat (**Inferencia** sobre su función).
- Línea contra incendios definida, con referencias UL y FM.

Debilidades:

- Las fichas no muestran atributos técnicos estructurados, lo que obliga a abrir el PDF o a consultar.
- Los títulos de categoría vacíos perjudican la lectura en pestañas y en resultados de búsqueda.
- Una categoría vacía y varias de un solo producto en el menú global.
- Un menú de 34 enlaces repetido en todas las páginas.
- Modelo de carrito que puede encajar mal con compras por licitación o proyecto (**Inferencia**).
- Segmentos minería, saneamiento y agricultura solo como encabezados de portada, sin página propia entre las rutas observadas.
- Nombres duplicados que dificultan elegir el producto correcto.

## Oportunidades para FUNDIGSAC

**Advertencia:** las normas de FUNDIGSAC citadas en esta sección proceden de `Frontend/src/modules/catalog/data.ts`, cuya cabecera lo declara dataset de maqueta. No son datos verificados y no deben publicarse sin documento (informe, sección 10, V-12).

1. **Tubería de hierro dúctil.** Rivali no la muestra. Reforzar `/productos/tuberias` con K7, K9, C40 e ISO 2531 para ocupar términos que este competidor no atiende.
2. **Marcos y tapas.** Rivali tiene una ficha de fierro fundido. FUNDIGSAC ya cita EN 124 en su catálogo y tiene `/productos/marcos-y-tapas`. Conviene destacar clase D400, seguro, dimensiones y material en cada ficha.
3. **Especificaciones en HTML.** Publicar DN, PN, material, tipo de unión y norma en una tabla legible por buscadores en cada ficha. Es la diferencia más clara frente a las 14 fichas revisadas.
4. **Normas visibles.** El catálogo de FUNDIGSAC menciona EN 124, EN 1074, EN 1092, ISO 2531 y NTP ISO 7259. Conviene mostrarlas en títulos y fichas, y respaldarlas con certificados vigentes antes de publicarlas.
5. **Títulos, meta y H1 por categoría.** Rivali deja esto sin resolver. Cada categoría de FUNDIGSAC debe tener título, descripción y H1 únicos con término y DN o norma cuando aplique.
6. **Páginas por industria.** FUNDIGSAC ya tiene `/industrias/saneamiento`, `/mineria` y `/agricultura`. Enlazarlas desde las fichas pertinentes refuerza una ventaja que Rivali no tiene en las rutas observadas.
7. **SEO local.** FUNDIGSAC ya declara `PostalAddress` en Cercado de Lima y `ContactPoint`. Mantenerlos e incluir "Lima" o "Perú" en títulos de categoría y en Google Business Profile.
8. **Relación técnica entre productos.** Sustituir relacionados automáticos por compatibilidades reales: válvula bridada con niple, brida y empaque del mismo DN.
9. **Cotización por proyecto.** Frente a un carrito genérico, priorizar cotización por lista de partidas con plazo y certificados adjuntos. `/cotizar` ya existe.
10. **Contra incendios.** **Inferencia:** es el terreno más fuerte de Rivali. No conviene disputarlo sin productos con listado UL o FM demostrable.
11. **Marcado Product.** Rivali declara `Offer`. FUNDIGSAC debe incluir `Offer` solo donde exista un precio real, para no generar datos inexactos.
