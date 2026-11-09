# Inccosac

| Campo | Valor |
|---|---|
| Sitio | https://inccosac.com/ |
| Segmento asignado en `COMPETIDORES.md` | Importador y distribuidor |
| Cómo se presenta el propio sitio | "Fabricante y proveedor de SEDAPAL en el Perú" |
| Fecha de la revisión | 9 de noviembre de 2026 |
| Estado del rastreo | ok |
| Páginas solicitadas | 26 (18 con datos, 5 con error 404, 3 redirecciones 301) |
| Páginas omitidas por robots.txt | 0 |
| PageSpeed móvil | n/d (cuota diaria de la API agotada) |
| Datos en bruto | `Report/competencia/datos/inccosac.json` |

## Resumen

Inccosac anuncia cuatro familias de producto, pero en el HTML público solo aparece una ficha: el marco y tapa D400 de material compuesto. Las listas de tuberías, marcos y tapas de hierro dúctil e hidrantes responden sin productos. La ficha de tubería que `COMPETIDORES.md` tenía registrada ahora responde 404.

Su mensaje comercial descansa en tres afirmaciones: proveedor de SEDAPAL, fabricación en Perú y certificación ISO 9001, 14001 y 45001. Ninguna se verificó en fuentes externas. Los enlaces "Política del SIG" y "Objetivos del SIG" de su portada terminan en 404.

Su debilidad más aprovechable es la estructura: solo una familia tiene página indexable propia, el H1 es igual en todas las páginas y hay enlaces rotos en toda la navegación.

## Cobertura de catálogo y familias

| Familia | Dónde aparece | Productos visibles en el HTML |
|---|---|---|
| Productos de material compuesto | Menú y `/categoria-producto/productos-material-compuesto/` | 1 |
| Tuberías de hierro dúctil | Menú, filtro `f_category` | 0 |
| Marcos y tapas de hierro dúctil | Menú, filtro `f_category` | 0 |
| Hidrantes contra incendios de hierro dúctil | Menú, filtro `f_category` | 0 |

Otras líneas se mencionan solo en encabezados o descripciones de la portada, sin página propia encontrada:

- Productos termoplásticos para agua potable y para alcantarillado.
- Hierro dúctil y fundición gris.
- Codo de hierro dúctil.
- Válvulas y concreto prefabricado, citados en la meta descripción de la portada.

Único producto con ficha: **Marco y Tapa de Material Compuesto D400** (`/producto/marco-y-tapa-de-material-compuesto-d400/`).

Comprobación adicional: `COMPETIDORES.md` citaba `/producto/tuberia-de-hierro-ductil/`, con DN80 a DN2000. Se solicitó esa página con el mismo rastreador y una sola solicitud, y respondió 404. Ese resultado se guardó solo como archivo temporal y no forma parte de `inccosac.json`.

Inferencias:

- El catálogo público pudo reducirse o estar en reconstrucción. Al combinar filtros, el servidor sí devuelve el producto de material compuesto, lo que indica que las listas se generan en el servidor y que las otras tres familias no tienen productos publicados.
- No se puede descartar que Inccosac siga vendiendo esas líneas fuera de la web. Su marca aparece en marcos y tapas vendidos por terceros, según `COMPETIDORES.md`.
- La imagen del producto está en `/wp-content/uploads/2026/08/`, lo que sugiere que la línea de material compuesto se publicó hacia agosto de 2026.

## Profundidad de especificaciones

La ficha de material compuesto tiene 18 pares de atributo y valor. No todos son especificaciones:

| Tipo | Cantidad | Ejemplos |
|---|---|---|
| Beneficios comerciales | 7 | Alta durabilidad, Antirrobo, Liviano y fácil de instalar |
| Atributos técnicos o de diseño | 11 | Material, Clase de resistencia D400, Cota de paso 600 mm, No conductor de electricidad |

Dentro de los 11 hay repeticiones: "Norma de Referencia" y "Norma de Fabricación" tienen el mismo valor, y la clase de resistencia figura dos veces.

No aparecen en los datos extraídos peso, dimensiones exteriores, altura del marco, tipo de cierre, tablas por DN, ni fichas técnicas descargables. El rastreo no encontró ningún PDF enlazado.

## Normas y certificaciones citadas

| Referencia | Tipo | Dónde |
|---|---|---|
| ISO 9001, ISO 14001, ISO 45001 | Sistemas de gestión | Portada; meta descripción de Quiénes Somos |
| EN 124, EN 124-1, EN 124-2, EN 124-5 | Producto, marcos y tapas | Ficha de material compuesto |
| NTP 339.701-2 | Producto | Ficha de material compuesto |
| CTPS-ET-035 de SEDAPAL | Especificación del cliente | Ficha de material compuesto |

`COMPETIDORES.md` registró además ISO 2531, EN 545, ISO 4179 e ISO 8179-1 en la ficha de tubería. Esa ficha ya no está disponible, por lo que esas citas no se pudieron confirmar en esta revisión.

Son declaraciones de la empresa. No se verificaron certificados ni la condición de proveedor de SEDAPAL. El sitio no enlaza ningún certificado en PDF.

## Palabras clave objetivo (inferidas de títulos y encabezados)

Todo este apartado es inferencia.

| Intención | Evidencia |
|---|---|
| productos para saneamiento y alcantarillado | Título de la portada y H2 "fabricados en el Perú" |
| proveedor de SEDAPAL | Título y H2 de Quiénes Somos, meta de la portada |
| fabricante certificado ISO de agua potable y saneamiento | Meta de Quiénes Somos |
| marco y tapa D400 material compuesto | Título y meta de la ficha |
| tapa antirrobo, no conductiva | Meta de la ficha |
| saneamiento en Lima Perú | Título de Contacto |

Las familias de tuberías, tapas de hierro dúctil e hidrantes no tienen título ni descripción propios. Sus URL de filtro muestran "Productos - Inccosac" y canonizan a `/productos/`, así que no compiten por esas búsquedas con una página específica.

## Marcado de esquema (JSON-LD)

| Tipo | Páginas (de 18) |
|---|---|
| Organization | 18 |
| WebSite | 18 |
| CollectionPage | 14 |
| ImageObject | 4 |
| WebPage | 3 |
| Person | 3 |
| Article | 3 |
| SearchAction | 1 |
| ItemPage | 1 |
| Product | 1 |

No se detectaron `BreadcrumbList`, `LocalBusiness`, `FAQPage` ni `Offer`. El nodo Organization no aportó teléfono, correo genérico ni dirección.

Inferencia: el marcado parece generado por un complemento SEO de WordPress con su configuración por defecto, porque `Article` y `Person` aparecen en páginas institucionales y las listas conservan el texto "Productos Archive".

## Enlazado interno

- Cada página tiene entre 12 y 17 enlaces internos únicos. Es una estructura plana y casi idéntica en todo el sitio.
- Menú, deducido del orden de los enlaces: Inicio, Quiénes Somos, cuatro familias de producto y Contacto.
- Tres de las cuatro familias apuntan a URL con parámetro. Solo material compuesto tiene ruta `/categoria-producto/`.
- No hay blog, recursos técnicos ni enlaces cruzados entre productos.

Defectos observados:

| URL | Resultado | Presencia |
|---|---|---|
| `/tienda/` | 404 | Todas las páginas con datos |
| `/nosotros/` | 404 | Todas las páginas con datos |
| `/politica-del-sig/` | 404 | Portada |
| `/objetivos-del-sig/` | 404 | Portada |
| `/inicio`, `/quienes-somos`, `/contacto` | 301 | Menú de todas las páginas |

La URL `/cdn-cgi/l/email-protection` también respondió 404 al rastreador. No se cuenta como defecto: es el mecanismo de ofuscación de correos de Cloudflare y funciona con JavaScript en un navegador normal.

Otros problemas:

- El H1 "Grupo Inccosac" se repite en las 18 páginas. La ficha de producto tiene dos H1.
- La canónica de `/quienes-somos/` apunta a `/quienes-somos`, que redirige de vuelta. La canónica de `/contacto/` sí es coherente.
- Las URL de filtro canonizan a `/productos/`. Esto evita duplicados, pero deja sin indexar las familias.
- La lista general usa la meta descripción "Productos Archive - Inccosac", un residuo en inglés.

## Llamadas a la acción

El rastreador no guarda el texto de los botones. Lo siguiente sale de metadatos y enlaces:

- "Cotiza ahora" en la meta de la portada y "Cotiza en INCCOSAC" en la meta de la ficha.
- La meta de Contacto ofrece WhatsApp, correo y ubicación.
- La cotización es el único objetivo de conversión observable, y la ruta `/tienda/` responde 404. El rastreador no captura precios, así que no se puede afirmar si el sitio los publica.
- Un H2 de Quiénes Somos promete asesoramiento durante la compra y hasta el despacho.
- No se detectaron enlaces `tel:` ni descargas de fichas.

Inferencia: la conversión depende de WhatsApp o de un formulario, sin pasos intermedios como descargar una ficha o armar una lista de cotización.

## Señales de SEO local

- Título de Contacto con "Lima Perú" y meta de Contacto con "Puente Piedra".
- Portada con "Inccosac Perú" en el título y "fabricados en el Perú" en un H2.
- Mención reiterada de SEDAPAL. Inferencia: refuerza la relevancia para Lima.
- `lang="es"`, sin variante regional.
- Sin `LocalBusiness`, y sin teléfono ni dirección en el marcado.
- Sin páginas por ciudad, región o cliente.

## Experiencia de usuario

El análisis se basa en HTML y metadatos. No se revisó el sitio en un navegador, así que los puntos de diseño visual quedan fuera.

Fortalezas:

- Mensaje de confianza claro y temprano: SEDAPAL, fabricación nacional e ISO.
- Filtro de productos con selección múltiple.
- La ficha de material compuesto combina beneficios y datos técnicos, y responde a un problema concreto del comprador: el robo de tapas.
- Títulos y descripciones cuidados en portada, Quiénes Somos, Contacto y la ficha.

Debilidades:

- Tres de cuatro familias del menú llevan a una lista vacía. Es el fallo de mayor impacto para un comprador.
- Enlaces rotos en todas las páginas y dentro de la sección que respalda la certificación.
- Sin fichas descargables para especificadores o licitaciones.
- HTML pesado: de 180 KB a 297 KB por página, con mediana cercana a 191 KB. Inferencia: es probable que penalice el rendimiento móvil, pero sin dato de PageSpeed no se puede afirmar.

## Oportunidades para FUNDIGSAC

**Advertencia:** las normas de FUNDIGSAC citadas en esta sección proceden de `Frontend/src/modules/catalog/data.ts`, cuya cabecera lo declara dataset de maqueta. No son datos verificados y no deben publicarse sin documento (informe, sección 10, V-12).

La base de comparación es `Frontend/src/modules/catalog/data.ts`, con 19 productos: 11 válvulas, 4 tuberías y 4 de marcos, tapas y rejillas. La prioridad y el impacto son inferencias.

| # | Oportunidad | Base | Cómo verificarla |
|---|---|---|---|
| 1 | Reforzar `/productos/tuberias` con DN, clases, ISO 2531 y EN 545, ahora que Inccosac no tiene ficha activa de tubería | Lista vacía y ficha 404 | Título, meta y H1 únicos; página indexable; Lighthouse SEO |
| 2 | Ocupar "válvulas para saneamiento": Inccosac las nombra, pero sin familia en el menú ni ficha | Meta de portada frente a menú | Una página por tipo de válvula con normas y DN |
| 3 | Mantener rutas propias por familia, con contenido específico, en lugar de filtros por parámetro | Solo 1 de 4 familias de Inccosac es indexable | Canónica propia y presencia en el sitemap |
| 4 | Publicar una comparación técnica de tapas de hierro dúctil y de material compuesto (EN 124-2 y EN 124-5), con el robo como tema central | Inccosac centra su argumento en el antirrobo | Página publicada con normas citadas y revisión técnica |
| 5 | Ampliar las fichas PDF por producto: Inccosac no enlaza ninguna y FUNDIGSAC ya tiene `Frontend/src/app/docs/` y `catalog-pdf.ts` | 0 documentos enlazados | Enlace de descarga en cada ficha, sin 404 |
| 6 | Citar especificaciones de SEDAPAL por producto, solo con respaldo documental propio | Inccosac cita CTPS-ET-035; FUNDIGSAC ya registra SEDAPAL AP-02 en un producto | Revisión del área técnica antes de publicar |
| 7 | Mostrar certificados verificables, si la empresa los tiene | Los enlaces del SIG de Inccosac terminan en 404 | Enlaces válidos a documentos reales |
| 8 | Completar el SEO local con dirección y teléfono en el marcado, y valorar `LocalBusiness` | Inccosac no publica esos datos en JSON-LD | Validación de datos estructurados |
| 9 | Decidir comercialmente si conviene sumar hidrantes o tapas de material compuesto | Inccosac las anuncia; no figuran en `data.ts` | Decisión de negocio, no de la web |

Requisito para cualquier corrección derivada de esta tabla: se deben medir todos los KPI y dejarlos en verde antes de darla por terminada. El último registro local, en `Report/kpi/fundigsac.jsonl`, muestra SEO 69 en `/` y en `/productos`, y rendimiento móvil de 82 y 85. Accesibilidad y buenas prácticas están en 100. Es una sola corrida sobre `127.0.0.1`. La causa del SEO 69 y la medición completa están en la sección 9 del informe.

Conviene vigilar que FUNDIGSAC no repita los defectos de Inccosac: H1 único por página, canónicas coherentes y ningún enlace del menú a una lista vacía.

## PageSpeed móvil

La API pública respondió HTTP 429 (`RESOURCE_EXHAUSTED`, `rateLimitExceeded`, cuota de consultas por día). Se hizo una sola llamada y se registra **n/d**. No hay datos de rendimiento ni de SEO de Lighthouse para este sitio.

## Limitaciones y notas de método

- El rastreo usó la imagen `fundig-scrapling`, con el Fetcher HTTP simple y el User-Agent `FundigsacMarketResearch/1.0`. No hubo 403, 429 ni páginas de desafío.
- Hubo 27 solicitudes HTTP en el rastreo principal y 2 en la comprobación de la ficha de tubería (robots.txt y la página). El total de páginas de contenido solicitadas al sitio fue 27, dentro del límite de 40.
- El rastreo agotó los enlaces alcanzables, sin llegar al límite. El sitemap declarado en robots.txt (`/sitemap_index.xml`) no se leyó, porque el rastreador solo procesa HTML. Puede contener fichas sin enlace desde el menú.
- Si el catálogo se cargara con JavaScript después de abrir la página, el Fetcher HTTP no lo vería. La comprobación de filtros reduce esa posibilidad, pero no la descarta.
- En el JSON, `resumen.productos` incluye "Grupo Inccosac" y `resumen.categorias` incluye textos de la interfaz como "Mostrar ( 1 )" o "Cancelar". Son falsos positivos del extractor. También lo es `es_ficha_producto: true` en las URL de filtro bajo `/productos/`.
- Esta revisión no incluyó correcciones en los sitios de FUNDIGSAC, por lo que no se midieron KPI propios.

## Acciones pendientes

1. Repetir la medición de PageSpeed cuando se recupere la cuota.
2. Revisar el sitemap de Inccosac si se autoriza una lectura de XML dentro de las reglas del estudio.
3. Actualizar en `COMPETIDORES.md` la referencia a la ficha de tubería, que hoy responde 404, y revisar el segmento asignado, ya que el sitio se presenta como fabricante.
