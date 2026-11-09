# Mecka SAC

| Campo | Valor |
|---|---|
| Sitio | https://meckasacperu.com/ |
| Segmento | Importador y distribuidor |
| Fecha de la revisión | 9 de noviembre de 2026 |
| Estado del rastreo | ok |
| Páginas con datos | 40 de 40 solicitadas (tope del estudio) |
| Solicitudes HTTP | 41 (robots.txt y 40 páginas), en 140,8 segundos |
| Rutas omitidas por robots.txt | 0 |
| Páginas enlazadas sin visitar | 14, por alcanzar el tope |
| PageSpeed móvil | n/d (cuota de la API agotada) |
| Datos en bruto | `Report/competencia/datos/mecka.json` |

Las afirmaciones sin marca son hechos observados en los datos del rastreo. Las deducciones llevan la etiqueta "Inferencia".

## Resumen

Mecka tiene un catálogo amplio en válvulas y accesorios bridados, con 41 URL de producto repartidas en 8 familias. Su punto débil para competir con FUNDIGSAC está en las líneas de hierro dúctil: la página de tuberías no enlaza ningún producto y marcos y tapas tiene una sola ficha. Las fichas usan el tipo `Article` en lugar de `Product`, y varias tienen errores de contenido. Sus principales ventajas son la cobertura de válvulas por aplicación (minería, aguas residuales) y el número de normas citadas en algunas fichas.

## PageSpeed móvil

La API pública respondió HTTP 429 (`RESOURCE_EXHAUSTED`, límite diario de consultas). Se hizo una sola llamada y se registra **n/d**. No hay puntuación de rendimiento ni de SEO de este sitio. El único dato de peso disponible es el HTML: entre 69 y 98 KB por página, con media de 78,5 KB, sin contar imágenes, CSS ni JavaScript.

## Cobertura de catálogo y familias

El menú principal se repite en las 40 páginas. Las familias y sus productos, según los enlaces de cada página de familia:

| Familia | URL de producto | Visitadas | Productos |
|---|---|---|---|
| Válvulas | 18 | 18 | Ver desglose siguiente |
| Bridas | 5 | 5 | Ciega de acero, rompeagua de acero, welding neck, para roscar, slip on ANSI |
| Tapas y marco | 1 | 1 | Marco y tapa de hierro dúctil para buzón |
| Tuberías | 0 | 0 | La página no enlaza ningún producto |
| Filtros | 2 | 2 | Tipo Y bridado, bridado tipo canasta |
| Uniones | 2 | 1 | Autoportante de 3 bridas, flexible escalonada (sin visitar) |
| Abrazaderas | 2 | 1 | Tapping de acero con derivación bridada, abrazadera de reparación o clamp (sin visitar) |
| Bombas | 7 | 0 | Aguas residuales tipo buceo, multicelular horizontal y vertical, para lodo, para lodo de alto rendimiento, sumergible para aguas residuales, sumergible para lodo |
| Metal mecánica | 4 | 1 | Tee bridada de hierro dúctil, codo bridado, niple de acero bridado, reducción de acero bridado (las tres últimas sin visitar) |
| **Total** | **41** | **29** | |

Desglose de válvulas:

| Tipo | Cantidad | Fichas |
|---|---|---|
| Compuerta | 7 | Bridada, bridada con elastómero, bridada WCB norma API, campana, de bronce bridada, de bronce roscada, "de bronce globo" |
| Check y retención | 5 | Swing bridada FLOWRAM, cierre silencioso, Duocheck Wafer, desagüe Elastocheck, Check Swing Elastocheck para minería |
| Aire | 3 | Doble efecto, aguas residuales o desagüe, minera |
| Mariposa | 2 | Bridada, tipo wafer |
| Reductora de presión | 1 | Reductora de presión |

- La página `/tuberias/` solo contiene los 13 enlaces del menú, no tiene meta descripción y sus H2 repiten los de la portada. En el texto de esa página no se detectó ninguna norma.
- Marcas mencionadas en títulos, meta descripciones o H2: FLOWRAM en 6 páginas (5 válvulas y el marco y tapa) y BUFFALO en la válvula de aire para minera.
- Inferencia: FLOWRAM funciona como marca principal de la línea. El rastreo no permite confirmar si es marca propia, como indica `COMPETIDORES.md`.
- Sin visitar por el tope: `/somos/`, `/mantenimiento/` y las 12 fichas indicadas en la tabla.
- Inferencia: las líneas que comparte con FUNDIGSAC son válvulas compuerta, mariposa, check y aire, y un único marco y tapa. Los bronces, las bridas de acero y las bombas amplían su oferta hacia industria general.

## Profundidad de especificaciones

Los campos `productos` y `especificaciones` del JSON están vacíos en todas las páginas. Esto es una limitación del rastreador y no indica falta de datos: las fichas de Mecka están en la raíz del dominio y no coinciden con las rutas de producto que el programa reconoce. La lista de productos se obtuvo de los H1 y de los enlaces de cada familia.

Lo que sí se observa en las meta descripciones y en los archivos enlazados:

- Las fichas siguen una estructura común: una pregunta de apertura y una lista de "Características clave".
- Los datos citados en los extractos son sobre todo cualitativos. Hay materiales concretos en algunas fichas, como hierro nodular ASTM A-536 o elastómero EPDM.
- Cada ficha enlaza fotografías JPG. Tres tienen nombres de archivo con la palabra `dimenciones` (compuerta bridada, check swing y filtro tipo Y) y dos con la palabra `listado` (compuerta bridada y check swing).
- Inferencia: las tablas de dimensiones y listas de partes se publican como imágenes. Si es así, no son indexables como texto ni se pueden copiar. Conviene confirmarlo revisando una ficha a mano.
- El único documento enlazado en las 40 páginas es el catálogo general `/images/catalogo/catalogo-meckasac.pdf`, y solo desde la portada. No hay fichas técnicas PDF por producto.

## Normas y certificaciones citadas

Se detectaron 23 referencias en el texto visible. Se concentran en 10 de las 29 fichas visitadas.

| Ficha | Normas citadas |
|---|---|
| Válvula compuerta bridada | ASTM A-536, DIN 3202, ISO 5752, ISO 7005, ISO 7259 |
| Válvula compuerta campana | ASTM A536, ISO 4422, ISO 7259, NTP 350.064, NTP-ISO 7259 |
| Válvula compuerta de bronce bridada | EN 12266-1, EN ISO 9001 |
| Check Swing Elastocheck para minería | ANSI B16.10 |
| Válvula de aire para aguas residuales | ANSI B16.5 |
| Válvula de aire para minera | ANSI B16.10, ASTM A27 |
| Marco y tapa de hierro dúctil | ASTM A-536, EN 124 |
| Filtro tipo Y bridado | ASTM A-536, ISO 2531 |
| Tapping de acero | ASTM A-283, ASTM A-36 |
| Tee bridada de hierro dúctil | ASTM A-105, ASTM A-53, ASTM A123, ISO 7005-1 |

- La cita de ISO 9001 aparece como norma de fabricación de una válvula de bronce. No se encontró ningún certificado enlazado.
- AWWA y NSF no aparecen en el texto de ninguna de las 40 páginas.
- La única cita de ISO 2531 está en el filtro tipo Y. No aparece en la página de tuberías.
- Las 19 fichas restantes no citan normas en su texto. Podrían hacerlo dentro de las imágenes, que el rastreo no lee.
- La clase D400 no figura en los campos guardados del marco y tapa. El rastreador no busca esa clase en el texto, por lo que no se puede afirmar que falte.

## Palabras clave objetivo

Todo este apartado es inferencia a partir de títulos, H1 y H2.

| Intención | Términos probables |
|---|---|
| Producto, válvulas | válvula compuerta bridada, válvula compuerta con elastómero, válvula compuerta campana, válvula compuerta WCB norma API, válvula compuerta de bronce, válvula check swing bridada, válvula check de cierre silencioso, válvula de retención wafer, válvula de aire doble efecto, válvula mariposa bridada, válvula mariposa wafer, válvula reductora de presión |
| Producto por aplicación | válvula de aire para aguas residuales, válvula de aire para minera, válvula check minería, válvula desagüe |
| Accesorios | brida ciega, brida rompeagua, brida welding neck, brida slip on ANSI, brida para roscar, filtro tipo Y bridado, filtro canasta, unión autoportante, tapping de acero, tee bridada de hierro dúctil |
| Hierro dúctil, buzones | marco y tapa de hierro dúctil para buzón |
| Informativa | qué es una válvula y para qué sirve, tipos de válvulas, qué es una brida, cuándo usar bridas, tipos de bombas de agua |
| Marca | Mecka SAC, Meckasac Perú |

Los títulos siguen el patrón `Nombre del producto - Mecka Sac Peru` en las 40 páginas. No incluyen ciudad, norma, diámetro ni clase de presión. El título de la portada es `Meckasacperu - Mecka Sac Peru`, sin ningún término de producto. La portada tiene tres H1, uno de ellos "Nuestros Clientes". Las otras 39 páginas tienen uno.

Las 40 páginas incluyen un H2 con el nombre de la empresa. De las 38 meta descripciones presentes, 37 terminan en "[…]" y 27 repiten fórmulas como "¿Estás buscando…" o "¿Buscas…". Inferencia: son extractos automáticos del primer párrafo y no textos escritos para buscadores.

## Marcado de esquema (JSON-LD)

| Tipo | Páginas |
|---|---|
| WebPage, ReadAction, ImageObject, BreadcrumbList, ListItem, WebSite, SearchAction, EntryPoint, Organization | 40 |
| Article, CommentAction, Person | 29 (las fichas de producto) |
| Product, Offer, FAQPage, LocalBusiness | 0 |

- Las fichas de producto se declaran como `Article`, por lo que no pueden optar a resultados enriquecidos de producto.
- Del nodo `Organization` se obtuvo el nombre "Mecka Sac Peru", sin teléfono ni dirección.
- Inferencia: el sitio es un WordPress con un plugin de SEO que genera este grafo por defecto, y los productos son entradas de blog. Lo apoyan la ruta `wp-content`, el archivo `sitemap_index.xml` declarado en robots.txt y los nodos `CommentAction`.

## Enlazado interno

- Hay un menú de 13 enlaces en todas las páginas: inicio, 9 familias, `/mantenimiento/`, `/somos/` y `/contactos/`.
- Las páginas de familia enlazan sus productos. Es una estructura plana de dos niveles, con todas las URL en la raíz del dominio.
- Cada ficha recibe enlace solo desde su familia y desde sí misma. No hay enlaces entre productos relacionados ni desde la portada hacia fichas concretas.
- Las fichas tienen entre 16 y 17 enlaces internos, que son el menú, la propia URL y sus imágenes.
- La URL de la brida slip on contiene un carácter de control (`/brida-slip-on-%c2%96-ansi/`).

## Llamadas a la acción

- Portada: "Llámanos al [celular omitido] o escríbenos: gerencia@meckasacperu.com" y "Ver Catálogo", que lleva al PDF.
- Contactos: "Envíanos un Correo", dirección, teléfono, Facebook y una indicación para buscarlos en Google.
- Fichas de producto: no tienen enlace interno propio a cotización o contacto, solo el del menú.
- Ninguna de las 40 páginas tiene enlaces `tel:`, así que el número no se marca con un toque en móvil.
- El rastreo no guarda enlaces externos, por lo que no se puede evaluar si hay botón de WhatsApp. Tampoco se analizó el formulario de contacto.
- Los celulares no coinciden: el de la portada y el de la página de contactos difieren en dos dígitos. Por inferencia, uno de los dos está mal escrito.

## Señales de SEO local

- Idioma declarado `es-PE` en las 40 páginas.
- La dirección Av. Óscar R. Benavides 2004, Lima figura en `/contactos/`. No está en JSON-LD y no se detectó en otras páginas.
- No hay `LocalBusiness`, y ningún título menciona Lima. "Peru" solo aparece como parte del nombre comercial.
- Referencia a Facebook y a la presencia en Google en la página de contactos.
- Inferencia: el sitio depende de su marca y de la coincidencia exacta con el nombre del producto, sin intención geográfica.

## Experiencia de usuario

Fortalezas:

- Navegación simple y constante, con las familias visibles en el menú.
- URL descriptivas y canónicas presentes en todas las páginas.
- Páginas de familia con contenido explicativo, como qué es una válvula o cuándo usar bridas.
- Catálogo descargable en portada y varias fotografías por producto.
- Fichas específicas por aplicación: minería, aguas residuales y desagüe.

Debilidades:

- La ficha de check swing FLOWRAM presenta en su H2 y meta descripción el texto de la válvula de aire doble efecto.
- La ficha de tee bridada de hierro dúctil describe "tubería de acero" bajo ASTM A-53.
- La ficha "válvula compuerta de bronce globo" mezcla dos tipos de válvula en el nombre. Inferencia: puede confundir a un especificador.
- Errores de escritura en textos visibles: "indrustriales", "distribucion", "desague" y "para minera".
- `/tuberias/` y `/metal-mecanica/` no tienen meta descripción, y tuberías no muestra productos.
- Sin precios estructurados, filtros por DN o PN ni comparadores en las rutas observadas. Inferencia: la selección técnica obliga a consultar por teléfono o correo.
- Todas las 72 imágenes enlazadas están en `wp-content/uploads/2023/01/`. Inferencia: el contenido se cargó de una vez en enero de 2023 y ha tenido poco mantenimiento.
- `/bombas/` incluye un H2 sobre la mejor bomba "para tu hogar". Inferencia: desvía el mensaje del público de obra e industria.

## Oportunidades para FUNDIGSAC

Todas las recomendaciones son inferencias basadas en lo observado.

1. **Ocupar el espacio de tubería de hierro dúctil.** Mecka no tiene fichas en esa familia. FUNDIGSAC puede posicionar páginas por clase (C40, K9, K7), DN y unión Tyton, citando ISO 2531, NTP ISO 2531 y EN 545 en texto.
2. **Abrir marcos y tapas en varias fichas.** Mecka concentra la línea en una sola URL. FUNDIGSAC ya distingue en su catálogo modelos D400 de uno y dos seguros, medida y peso. Conviene una página por variante, con la clase EN 124 en título y H1.
3. **Publicar especificaciones como texto.** Mantener DN, PN, materiales, pesos y normas en tablas HTML. Esto da ventaja en búsquedas largas si se confirma que Mecka las publica como imagen.
4. **Conservar y completar `Product`.** El frontal de FUNDIGSAC ya genera `Product` en sus fichas y `Organization` con teléfono. Mecka usa `Article` y no declara contacto. Añadir dirección estructurada y `LocalBusiness` reforzaría la diferencia.
5. **Crear fichas o guías por aplicación.** Mecka cubre válvula de aire para aguas residuales y para minería, y check para minería. FUNDIGSAC puede competir con páginas por sector, explicando qué válvula corresponde a agua potable, desagüe o minería.
6. **Citar normas por producto y sustentarlas.** Mecka no menciona AWWA ni NSF y no enlaza certificados. FUNDIGSAC puede publicar fichas técnicas PDF y certificados por producto, solo con los documentos que tenga vigentes.
7. **Títulos con intención completa.** Mecka no incluye norma, medida ni ciudad. Títulos como "Válvula compuerta hierro dúctil PN16 DN50-DN300 en Lima" cubren consultas que sus títulos no atienden, siempre que el rango sea real.
8. **Facilitar el contacto móvil desde cada ficha.** Enlaces `tel:` y botón de cotización por producto, frente a un competidor sin marcación directa y con dos teléfonos distintos.
9. **Enlazar productos relacionados.** Mecka no enlaza entre fichas. Unir válvula, brida, unión y marco por aplicación mejora el rastreo y ayuda a armar una cotización completa.
10. **Disputar las consultas informativas con contenido técnico.** Mecka responde qué es una válvula y qué es una brida con textos generales. Guías sobre golpe de ariete, selección de válvula de aire o clases de carga EN 124 tendrían más valor para ingenieros y compradores.

## Limitaciones y acciones pendientes

1. Repetir PageSpeed móvil cuando se recupere la cuota. Hasta entonces no hay comparación de rendimiento con este competidor.
2. Revisar a mano una ficha para confirmar si las tablas están en imágenes y si existe botón de WhatsApp.
3. No se visitaron `/somos/`, `/mantenimiento/` ni 12 fichas de producto, incluidas todas las bombas.
4. El rastreo usa HTTP simple y no ejecuta JavaScript. No se leyó el sitemap ni el contenido del catálogo PDF.
5. `COMPETIDORES.md` cita URL con `www` y terminación `.html`. No se comprobó si siguen activas ni cómo redirigen.

## Notas de método

- El rastreo se ejecutó una sola vez, dentro de la imagen `fundig-scrapling`, con el User-Agent `FundigsacMarketResearch/1.0`. Se leyó robots.txt antes de cualquier página y no hubo bloqueos.
- El JSON guarda hechos y metadatos. No incluye datos de personas: los nodos `Person` no se leen y el único correo es un buzón genérico de empresa.
- Esta revisión no incluyó correcciones en los sitios de FUNDIGSAC, por lo que no hubo KPI propios que medir.
