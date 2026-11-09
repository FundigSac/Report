# Leoneblu SAC

| Campo | Valor |
|---|---|
| Sitio | https://leoneblusac.com/ |
| Segmento | Distribuidor nacional |
| Fecha de la revisión | 9 de noviembre de 2026 |
| Estado del rastreo | ok |
| Páginas con datos | 40 de 40 permitidas (1 portada, 24 de categoría, 15 fichas de producto) |
| Solicitudes HTTP | 41, incluida robots.txt |
| Bloqueos | Ninguno. Sin 403, 429, captcha ni desafío |
| PageSpeed móvil | n/d (cuota de la API agotada) |
| Datos en bruto | `Report/competencia/datos/leoneblu.json` |

## Resumen

Leoneblu tiene un catálogo muy amplio para agua, saneamiento e industria, con 75 categorías numeradas en su menú. Su base técnica en la web es débil: en las 40 páginas rastreadas no hay ninguna norma citada, ninguna tabla de especificaciones, ningún dato estructurado JSON-LD ni URL canónica. La portada conserva como meta descripción el texto de una plantilla.

Inferencia: compite por amplitud de surtido y cercanía comercial, y no por información técnica. Esa es la brecha que FUNDIGSAC puede ocupar.

## KPI medidos

| KPI | Resultado | Valoración |
|---|---|---|
| PageSpeed móvil: rendimiento | n/d | Sin medir |
| PageSpeed móvil: SEO | n/d | Sin medir |
| PageSpeed móvil: accesibilidad | n/d | Sin medir |
| PageSpeed móvil: buenas prácticas | n/d | Sin medir |
| Páginas con título | 40/40 | Correcto en presencia; poco descriptivo en portada |
| Páginas con meta descripción útil | 0/40 | Deficiente |
| Páginas con H1 | 15/40 (solo fichas) | Deficiente |
| Páginas con URL canónica | 0/40 | Deficiente |
| Páginas con JSON-LD | 0/40 | Deficiente |
| Páginas con idioma correcto | 0/40 (`lang="en"` en un sitio en español) | Deficiente |
| Páginas con normas citadas | 0/40 | Deficiente |
| Fichas con atributos técnicos en tabla o lista | 0/15 | Deficiente |
| robots.txt | HTTP 404 | No existe |
| Sitemap declarado | Ninguno | No hay robots.txt que lo declare; no se comprobó `/sitemap.xml` |
| Peso del HTML | Portada 275.748 bytes; categoría 96.988 de media; ficha 87.356 de media | Alto para HTML sin imágenes |

La API pública de PageSpeed respondió HTTP 429 (`RESOURCE_EXHAUSTED`, `rateLimitExceeded`, límite diario 0 para el proyecto anónimo). Se pidieron las cuatro categorías en una sola llamada y no se reintentó. Sin esos cuatro valores no se puede afirmar nada sobre el rendimiento real de este sitio.

## Cobertura de catálogo y familias

El menú enlaza 75 categorías numeradas (`categorias.php?cat=N`, identificadores del 51 al 132 con huecos). Se visitaron 22 y sus nombres son:

| Criterio | Categorías |
|---|---|
| Válvulas | VALVULAS BRIDADA, VALVULAS PVC, VALVULAS HDPE, VALVULAS RANURADAS, VALVULAS CAMPANA HD |
| Tubería | TUBERIA HDPE, TUBERÍAS PPR, TUBERIA ACERO |
| Conexiones | CONEXIONES, CONEXIONES DUCTIL, CONEXIONES GALVANIZADO, CONEXIONES BRONCE, CONEXIONES ACERO, JUNTAS, VITAULIC |
| Marcos y tapas | MARCOS Y TAPAS |
| Por material o rubro | ACERO, HIERRO DUCTIL, INDUSTRIAL, GASFITERIA |
| Otros | BIDON, MANGAS DE PLASTICO |

Las otras 53 categorías no se visitaron porque se agotó el cupo de 40 páginas. Quedaron 111 URL pendientes.

La portada expone 46 nombres de producto, repartidos así (clasificación propia):

| Familia | Cantidad | Ejemplos |
|---|---|---|
| Válvulas | 16 | Mariposa de hierro dúctil, compuerta bridada, compuerta OS&Y, duo check, de aire de hierro dúctil, reductora de presión, control de nivel, cuchilla, pinch |
| Conexiones y accesorios | 9 | Abrazaderas, brida partida ranurada, unión adaptador brida, junta de expansión, codo de acero |
| Maquinaria y herramientas | 6 | Termofusión HDPE y PPR, electrofusión, soldadora de geomembrana, balde de prueba hidráulica |
| Plásticos, químicos y otros | 6 | Geomembrana HDPE 1,5 mm, cilindro de 100 litros, hipoclorito de sodio, dosificador de cloro gas, gabinete contra incendio |
| Tubería y manguera | 4 | Tubo de hierro dúctil, tubo HDPE, tubo PVC desagüe, manguera HDPE |
| Medición | 3 | Chorro múltiple, bridado, electromagnético de flujo |
| Marcos y tapas | 2 | Marco y tapa de buzón, marco y tapa de buzón PVC HDPE |

Solapamiento con FUNDIGSAC: válvulas compuerta, mariposa, check y de aire, tubo de hierro dúctil, conexiones de hierro dúctil y marcos y tapas.

Inferencia: la taxonomía mezcla tipo de producto, material y unión (por ejemplo "ACERO" junto a "VALVULAS BRIDADA"), lo que apunta a un catálogo que creció por acumulación y no a una estructura pensada para el comprador técnico.

`COMPETIDORES.md` indica que vende marcos y tapas D400 y que revende la marca FUMOSAC. El rastreo no confirmó ninguno de los dos datos, porque "D400" y "FUMOSAC" no aparecen en los títulos ni encabezados obtenidos y las fichas citadas allí no estuvieron entre las 40 páginas.

## Profundidad de especificaciones

- Ninguna de las 15 fichas tiene atributos técnicos en tablas ni listas. El único par detectado es el horario de atención del pie de página, que el extractor tomó por error como especificación.
- Los títulos de producto no incluyen DN, PN, presión ni norma, salvo casos sueltos ("GEOMEMBRANA HDPE = 1.5MM", "BALDE DE PRUEBA HIDRAULICA 150 PSI", "CILINDRO PLASTICO 100 LITROS").
- 14 de las 15 fichas enlazan a `/ficha/0`. Solo una enlaza a un archivo real con nombre, y es una imagen (`/ficha/CILINDRO.jpg`).
- Inferencia: `/ficha/0` es un valor vacío del sistema, de modo que casi ninguna ficha tendría documento técnico. No se verificó porque esa ruta quedó fuera del cupo.
- El sitio enlaza dos catálogos en PDF de 2026. No se descargaron, y podrían contener especificaciones que aquí no constan.

## Normas y certificaciones citadas

No se encontró ninguna norma (ISO, NTP, EN, AWWA, ASTM, NSF u otra) en las 40 páginas. La portada usa el encabezado "PRODUCTOS CERTIFICADOS Y HOMOLAGADOS" (con ese error de escritura), sin indicar qué norma, certificado ni organismo respalda la afirmación. No se revisaron las páginas `nosotros.php` y `contacto.php` ni los PDF, así que no se descarta que los mencionen allí.

## Palabras clave objetivo

Inferencia a partir de títulos y encabezados:

- Válvulas: "válvula mariposa hierro dúctil", "válvula compuerta bridada", "válvula compuerta OS&Y bridada", "válvula de aire hierro dúctil", "válvula duo check", "válvula reductora de presión", "válvula control de nivel hierro dúctil", "válvula cuchilla", "válvula pinch".
- Tubería y conexiones: "tubo hierro dúctil", "tubo HDPE polietileno", "abrazadera hierro dúctil", "brida partida ranurada", "junta de expansión flexible".
- Saneamiento: "marco y tapa buzón".
- Fuera de las líneas de FUNDIGSAC: "geomembrana HDPE", "máquina termofusión HDPE", "medidor electromagnético de flujo".

El patrón es `NOMBRE DEL PRODUCTO | Leone Blu`, en mayúsculas y casi siempre sin tilde. Ningún título ni encabezado obtenido incluye Lima, Perú, "precio", "proveedor" ni una medida comercial. Inferencia: no hay una estrategia deliberada de palabras clave y su posicionamiento depende del nombre del producto.

## Marcado de esquema

Sin JSON-LD en ninguna de las 40 páginas. No hay `Organization`, `LocalBusiness`, `Product` ni `BreadcrumbList`. El rastreador no evalúa microdatos ni RDFa, por lo que estos dos formatos quedan sin comprobar.

## Enlazado interno

- Plantilla común en todas las páginas: cotizar, nosotros, categorías, contacto, inicio, carrito, visión, misión, sesión y reclamaciones, más el menú completo de categorías.
- Enlaces internos por página: portada 153, categoría 88, ficha 90. La mayor parte proviene del menú.
- En las páginas de categoría, los 80 enlaces guardados (de 88) son de navegación o de otras categorías, y ninguno lleva a una ficha. El tamaño es casi idéntico en las 24 páginas (96.945 a 97.189 bytes) y el extractor no halló productos en ellas.
- Inferencia: el listado de productos de cada categoría se carga con JavaScript o no se entrega en el HTML inicial. Las fichas quedarían enlazadas sobre todo desde la portada, lo que limita su rastreo e indexación. El rastreador no ejecuta JavaScript y por eso no puede confirmarlo.
- Las URL usan parámetros (`producto.php?id=`, `categorias.php?cat=`) sin términos descriptivos.
- Posibles duplicados sin canónica: `/` e `/index.php`; `categorias.php` y `categorias.php?cat=0`, con el mismo título. Hay también dos productos casi iguales: "VALVULA COMPUERTA BRIDADA" y "VÁLVULA COMPUERTA BRIDADA".
- Los PDF del catálogo tienen espacios en el nombre: `CATALOGO 2026 LEONE BLU .pdf` y `CATALOGO 2026 LEONE BLU 2.pdf`.

## Llamadas a la acción

- `cotizar.php` en el menú principal de todas las páginas.
- `carrito8.php` y `sesion.php`, propios de una tienda con cuenta de usuario. No se visitaron.
- Dos catálogos PDF de 2026 enlazados desde la portada.
- Sección de comentarios en cada ficha: entre 1 y 5 por producto, 24 en las 15 fichas.
- Enlace al libro de reclamaciones (`reclamaciones.php`).

`COMPETIDORES.md` indica que publica precios. El rastreador no extrae precios, así que este punto no se confirmó.

## Señales de SEO local

| Señal | Hallazgo |
|---|---|
| Ciudad o región en títulos y encabezados | Ninguna |
| `LocalBusiness` o dirección estructurada | No existe |
| Enlace telefónico | Un único `tel:` cuyo valor es `#`, sin número |
| Correo genérico en `mailto:` | No se capturó ninguno |
| Horario | Visible en las fichas: 8:30 a. m. a 6:30 p. m. |
| Etiqueta de idioma | `en`, con contenido en español |
| Coherencia de marca | "LEONEBLU SAC" en portada y "Leone Blu" en fichas |

`contacto.php` no se visitó, por lo que allí podría figurar dirección, teléfono o mapa.

## Experiencia de usuario

No se evaluó el aspecto visual, porque el rastreo solo lee HTML.

Fortalezas:

- Surtido muy amplio, con compra concentrada en un solo proveedor. Inferencia: atractivo para contratistas pequeños.
- Cada categoría está a un clic desde cualquier página.
- Cotización siempre visible en el menú.
- Catálogos descargables actualizados a 2026.
- Comentarios en las fichas y horario de atención visible.

Debilidades:

- Portada sin H1 y con la meta descripción "Porto - Bootstrap eCommerce Template". Inferencia: plantilla comprada y sin terminar de configurar.
- Categorías sin H1 ni H2, con meta descripción igual al título.
- Fichas sin meta descripción.
- Errores de escritura visibles: "HOMOLAGADOS", y "VITAULIC" en lugar de Victaulic.
- Enlace telefónico sin número, que falla al pulsarlo en un móvil.
- Fichas técnicas ausentes o reducidas a una imagen.
- HTML pesado por el menú repetido.

## Oportunidades para FUNDIGSAC

**Advertencia:** las normas de FUNDIGSAC citadas en esta sección proceden de `Frontend/src/modules/catalog/data.ts`, cuya cabecera lo declara dataset de maqueta. No son datos verificados y no deben publicarse sin documento (informe, sección 10, V-12).

Las siguientes recomendaciones son inferencias basadas en los hallazgos anteriores.

1. **Convertir la norma en argumento de venta.** Leoneblu dice "certificados" sin citar ninguna norma. FUNDIGSAC ya tiene en su catálogo referencias como EN 1074 y AWWA C530. Conviene mostrarlas en el título, en el H1 o en un bloque visible de cada ficha, con el certificado descargable.
2. **Dar tablas de especificaciones en HTML.** Incluir DN, PN, material, recubrimiento, tipo de unión y presión de prueba. Ningún dato de este tipo aparece en las 15 fichas rastreadas de Leoneblu.
3. **Atacar búsquedas específicas.** Sus títulos no contienen medidas ni ubicación. Hay espacio para consultas como "válvula compuerta bridada PN16 DN100 Lima" o "marco y tapa D400 EN 124 Perú".
4. **Publicar fichas técnicas en PDF con URL descriptiva**, frente a `/ficha/0`. FUNDIGSAC ya tiene una en `public/docs/ficha-tecnica-valvula-compuerta-bridada.pdf`; el modelo puede extenderse a todas las referencias.
5. **Asegurar que categorías y productos lleguen en el HTML inicial,** con texto propio por categoría y enlaces directos a las fichas.
6. **Cubrir el marcado estructurado.** `Frontend/src/shared/seo/json-ld.tsx` emite `BreadcrumbList`. Conviene comprobar que cada ficha publique también `Product` y que exista `LocalBusiness` con dirección, teléfono y horario.
7. **Aprovechar el SEO local.** Con dirección estructurada, teléfono funcional y referencias a Lima y a regiones atendidas se supera una señal que Leoneblu casi no trabaja.
8. **No competir en amplitud.** Leoneblu cubre geomembrana, PPR, químicos y maquinaria. FUNDIGSAC gana más con profundidad técnica en sus cuatro líneas y con una navegación por norma, DN y aplicación.
9. **Ofrecer el catálogo PDF con términos buscables**, y enlazarlo desde cada categoría, como respuesta directa a los dos PDF de la portada de Leoneblu.

## Limitaciones

- La API de PageSpeed no devolvió datos, por lo que no hay ningún KPI de Lighthouse de este sitio.
- El cupo de 40 páginas se agotó en categorías y fichas. No se visitaron `nosotros.php`, `contacto.php`, `cotizar.php`, `vision.php`, `mision.php` ni 53 categorías.
- El tope de 80 enlaces guardados por página impide ver la lista completa de la portada (153) y los últimos 8 de cada categoría.
- No se ejecutó JavaScript ni se abrieron los PDF. Lo que dependa de ellos no consta aquí.
- El extractor de especificaciones solo lee tablas y listas. Si las fichas describen datos técnicos en párrafos, no quedan registrados.
- Nota de método: el filtro de rutas de `scrape.py` no contempla `sesion.php` ni `carrito8.php`. No se solicitaron en este rastreo porque el cupo se agotó antes, pero convendría añadirlas si se repite con otro orden de prioridad.
