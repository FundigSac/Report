# Collaval Import

| Campo | Valor |
|---|---|
| Sitio | https://collavalimport.com/ |
| Segmento | Importador |
| Fecha de la revisión | 9 de noviembre de 2026 |
| Estado del rastreo | ok |
| Páginas solicitadas | 40 (límite del estudio) |
| Páginas con datos | 36: portada, 31 categorías y 4 páginas del catálogo |
| PageSpeed móvil | n/d (cuota de la API agotada) |
| Datos en bruto | `Report/competencia/datos/collaval-import.json` |

robots.txt está publicado, no fija demora de rastreo y no impidió ninguna URL. Declara `sitemap_index.xml`.

## Alcance y limitaciones

- **No se visitó ninguna ficha de producto.** El cupo de 40 páginas se agotó en categorías y catálogo. Quedaron 147 URL pendientes, entre ellas las 115 fichas detectadas. No se pidieron más páginas para respetar el límite.
- Por eso la profundidad de especificaciones, las normas en fichas y el schema `Product` **no se pudieron medir**. Un cero en esta revisión se refiere solo a portada, categorías y catálogo.
- El JSON cuenta 145 productos, pero 31 son títulos de categoría. El rastreador trata las rutas `/productos/categoria/` como fichas y añade su H1 a la lista. Los nombres reales de producto son 114, repartidos en 115 URL. Las categorías con 0 especificaciones tampoco son fichas.
- El rastreador no guarda enlaces externos, botones ni texto de formularios. WhatsApp, redes sociales y formularios no se pudieron evaluar.
- Solo se usó HTTP simple, sin ejecutar JavaScript. El contenido que el sitio cargue por script no aparece en estos datos.

## KPI medidos

La revisión no incluye ninguna corrección, porque el sitio es de un tercero. Los KPI describen a Collaval Import y no miden a FUNDIGSAC. El objetivo es la referencia de buena práctica con la que conviene comparar.

| KPI | Resultado | Objetivo | Estado |
|---|---|---|---|
| Rendimiento móvil (PageSpeed) | n/d | 90 o más | Sin medir |
| SEO móvil (PageSpeed) | n/d | 90 o más | Sin medir |
| Páginas con meta descripción | 15 de 36 (42 %) | 100 % | Rojo |
| Títulos que no son la plantilla "archivos" | 19 de 36 (53 %) | 100 % | Rojo |
| Páginas con exactamente un H1 | 31 de 36 (86 %) | 100 % | Rojo |
| Canónica autorreferente | 36 de 36 | 100 % | Verde |
| `BreadcrumbList` en JSON-LD | 36 de 36 | 100 % | Verde |
| Enlaces rotos en la navegación común | 3 URL con 404, enlazadas en 36 de 36 páginas | 0 | Rojo |
| Redirecciones en la navegación común | 1 URL con 301, enlazada en 36 de 36 páginas | 0 | Rojo |
| Normas citadas en páginas visitadas | 0 de 36 | Al menos una en páginas técnicas | Rojo |
| Documentos enlazados (PDF, DWG, etc.) | 0 | Al menos una ficha o catálogo | Rojo |
| Especificaciones y `Product` en fichas | Fichas no visitadas | Presentes | Sin medir |

Tamaño del HTML por página: de 298 a 347 KB, con mediana de 331 KB. No se le asigna estado, porque sin PageSpeed no se conoce su efecto real.

## Cobertura del catálogo y familias

El catálogo general indica 11 páginas. Las visitadas muestran 12 productos cada una. Inferencia: el total estaría entre 121 y 132 productos, frente a los 115 enlaces observados.

La taxonomía combina tres ejes: material o línea, tipo de pieza y marca.

| Familia | Productos observados | Notas |
|---|---|---|
| Válvulas de hierro dúctil | 12 en la primera página; hay página 2 | Compuertas embonadas y bridadas, aire, check, filtro en Y |
| Conexiones bridadas de hierro dúctil | 6 | Codos 45 y 90, tee, tee con reducción, yee, reducción |
| Accesorios de hierro dúctil | 4 | Adaptadores rápido, acerrojado y universal; barra para varilla de desatoro |
| Marcos y tapas | 1 | Marco y tapa de buzón D400 |
| Válvulas de PVC | 9 | Marcas Era, Sanking y Citaly |
| Conexiones de PVC | 12 en la primera página; hay página 2 | SP y UF inyectadas |
| Válvulas de bronce | 12 en la primera página; hay página 2 | Citaly y Cim |
| Conexiones de bronce | 2 | Codos liviano y pesado |
| Conexiones HDPE | 12 en la primera página; hay página 2 | Termofusión y electrofusión |
| Conexiones galvanizadas | 7 | |
| Abrazaderas | 9 | Incluye toma en carga y reparación rápida |
| Uniones | 6 | Dresser, autoportante, acoples |
| Bridas | 3 | Soldable PN16, acero inoxidable, UF PVC |
| Medidores de agua | 2 | Chorro único y múltiple |
| Mallas, canastillas y filtros | 3 | Fuera del rubro de redes en el caso de las mallas |

Marcas con página propia: C-Italy (Citaly), Era, Cim Valve, Sanking, Concyssa, Fumosac y Mapache.

### Comparación con las líneas de FUNDIGSAC

| Línea | Presencia en Collaval | Lectura |
|---|---|---|
| Válvula compuerta de hierro dúctil | 8 productos | Competidor directo y con variedad de uniones |
| Válvula de aire | 5 productos en hierro dúctil, PVC y bronce | Competidor directo |
| Válvula check | 7 productos, solo 1 de hierro dúctil | Fuerte en bronce y PVC; débil en hierro dúctil |
| Válvula mariposa | 2 productos, ambos de PVC | No se observó mariposa de hierro dúctil |
| Conexiones bridadas | 6 productos | Línea básica |
| Marcos y tapas | 1 producto | Oferta mínima |
| Tubería de hierro dúctil | Ninguna entre los 114 nombres | La meta de la línea anuncia "tuberías", sin producto visible |
| Hidrantes | Ninguno entre los 114 nombres | La misma meta los anuncia, sin producto visible |

La página de marca Fumosac promete "válvulas, conexiones, buzones y tuberías", pero no lista ningún producto. Inferencia: el canal existe como reventa bajo pedido o la página quedó sin completar.

## Profundidad de especificaciones

No medida en fichas. Lo único observable son los nombres de producto, que indican:

- Tipo de unión: embonada, bridada, stub end, brida loca, adaptador rápido, universal o acerrojado.
- Tecnología de unión en plástico: termofusión, electrofusión, SP y UF.
- Clase o presión en casos aislados: D400 y PN16.

Los nombres no indican DN, PN ni material de cierre. Ninguna de las 36 páginas expone tablas de atributos ni documentos técnicos enlazados.

## Normas y certificaciones citadas

No se detectó ninguna norma (ISO, EN, NTP, AWWA, ASTM) en título, encabezados ni texto de las 36 páginas. D400 aparece como clase, sin mencionar EN 124.

La portada describe sus productos como "certificados" sin indicar norma ni certificado. Tampoco se detectaron SEDAPAL ni documentos descargables. Las fichas pueden contener más datos.

Las metas de las líneas hablan de "tecnología italiana" y "calidad italiana". En la muestra no hay evidencia del origen ni del fabricante.

Collaval se declara importador exclusivo de Citaly, y `COMPETIDORES.md` registra a Citaly Perú con la misma marca. La exclusividad no se pudo verificar.

## Palabras clave objetivo (inferencia)

Inferidas de títulos, metas, H1, H2 y rutas.

| Grupo | Términos |
|---|---|
| Principal | válvulas de hierro dúctil Perú, válvula compuerta bridada, válvula compuerta embone |
| Transición a HDPE | válvula compuerta stub end HDPE, adaptador brida acerrojado HDPE, adaptador brida universal, adaptador rápido HDPE |
| Aire y conexiones | válvula de aire triple efecto bridado, conexiones bridadas hierro dúctil, codo 90 hierro dúctil bridado |
| Saneamiento | marco y tapa de buzón hierro dúctil D400, medidores de agua chorro único y múltiple, abrazadera toma en carga |
| Plásticos y bronce | conexiones HDPE termofusión y electrofusión, válvulas de PVC, válvulas de bronce |
| Marca | Citaly, C-Italy, importadores marca Era, distribuidores Cim Valve, Sanking, Concyssa, Fumosac |
| Informativas (blog) | cómo elegir válvula de compuerta, ventajas de válvulas tipo lug, adaptadores de brida universales |

La marca se escribe de cuatro formas: C-Italy, C-ITALY, C Italy y Citaly. Inferencia: esto dispersa la señal de búsqueda.

## Marcado de datos

| Tipo JSON-LD | Páginas |
|---|---|
| `Organization`, `WebSite`, `SearchAction`, `BreadcrumbList`, `ImageObject` | 36 de 36 |
| `CollectionPage` | 31 |
| `WebPage` y `ReadAction` | 5 |
| `Product`, `LocalBusiness`, `FAQPage` | 0 en las páginas visitadas |

`Organization` declara el teléfono `123-456-7890`, un valor de ejemplo que nunca se reemplazó. No declara dirección y no se capturó correo.

Inferencia: la combinación de tipos y la plantilla "archivos" apuntan a WordPress con Yoast SEO. Es posible que el catálogo use WooCommerce, lo que no se pudo confirmar.

## Enlazado interno

- 187 rutas internas únicas. Cada página tiene entre 41 y 64 enlaces, con mediana de 50.
- Un bloque común de 41 enlaces aparece en al menos el 90 % de las páginas. Da acceso a las categorías y marcas desde casi cualquier página.
- La portada enlaza 8 fichas destacadas y 3 artículos. El resto de las fichas queda a dos clics o detrás de paginación.
- Cada ficha recibe entre 1 y 5 enlaces dentro de la muestra.
- Tres enlaces comunes devuelven 404: `/productos/categoria/valvulas/valvula-hierro-ductil/`, `/productos/categoria/conexiones-hdpe/` y `/productos/categoria/valvulas/valvula-de-bronce/`.
- `/web/catalogo-de-productos/` redirige con 301 a `/catalogo-de-productos/`.

Inferencia: el sitio se trasladó desde la carpeta `/web/` y reorganizó su taxonomía sin actualizar la navegación común.

Otros indicios de mantenimiento: la ruta `/nosotros-2/` y el duplicado `/productos/union-autoportante/` y `/productos/union-autoportante-2/`.

## Llamadas a la acción

- Anclas "VER PRODUCTOS" hacia categorías. Una está escrita "VER PRODUCTOIS".
- `/contacto/` en la navegación común.
- Bloques en portada: productos destacados, marcas, línea exclusiva Citaly, servicios y noticias.
- La meta de la línea de bronce ofrece "precios especiales para distribuidores". Es el único mensaje dirigido a ese canal.
- "Cotización" no aparece en títulos, metas ni encabezados.
- No se capturó ningún teléfono real mediante enlaces `tel:` ni ningún correo genérico de empresa.

Inferencia: la conversión depende de la página de contacto o de canales que el rastreador no registra, como WhatsApp.

## SEO local

- "Lima" no aparece en títulos, metas ni encabezados de ninguna de las 36 páginas.
- En esos mismos campos, "Perú" aparece en 2 páginas y "nacional" en 4. El mensaje es de cobertura nacional sin anclaje geográfico.
- No hay `LocalBusiness` ni dirección estructurada, y el teléfono estructurado es un valor de ejemplo.
- No se observaron páginas por ciudad, región, EPS ni sector, aunque la portada menciona minería, construcción y saneamiento.

## Experiencia de usuario

Fortalezas:

- La navegación por material, tipo y marca permite llegar por varios caminos.
- La variedad de válvulas para transición entre hierro dúctil, HDPE y PVC responde a un problema real de obra.
- Las páginas de marca tienen título y meta propios.
- Ofrece catálogo amplio, artículos y sección de videos.
- Migas y canónicas están bien aplicadas.

Debilidades:

- 3 enlaces rotos visibles en todas las páginas.
- 21 de 36 páginas sin meta descripción y 17 con título automático "archivos".
- El título de la portada es solo "Collaval Import".
- La portada tiene 3 H1 y las páginas del catálogo no tienen ninguno.
- Encabezado "Categories" en inglés en páginas en español, y erratas como "PRODUCTOIS", "chek" y "Ultimas".
- Cada producto del listado es un H2, lo que diluye la jerarquía de encabezados.
- Sin normas ni documentos técnicos en las páginas revisadas.
- HTML pesado para páginas de listado (mediana de 331 KB).

## Oportunidades para FUNDIGSAC

**Advertencia:** las normas de FUNDIGSAC citadas en esta sección proceden de `Frontend/src/modules/catalog/data.ts`, cuya cabecera lo declara dataset de maqueta. No son datos verificados y no deben publicarse sin documento (informe, sección 10, V-12).

Las referencias a FUNDIGSAC proceden del código de `Frontend`. No se midió su sitio publicado en esta revisión.

1. **Convertir las normas en la ventaja visible.** Collaval no cita ninguna en estas páginas. FUNDIGSAC ya registra normas por producto, como ISO 2531, EN 545, EN 1074, AWWA C530, EN 124 D400 y NTP 350.085. Conviene mostrarlas en listados y categorías, no solo en fichas.
2. **Ocupar tubería de hierro dúctil.** Collaval la anuncia sin mostrar producto. Una página por tipo de unión y rango DN, con ISO 2531 y EN 545, ataca un hueco concreto.
3. **Profundizar marcos y tapas.** Collaval tiene un solo producto. Una categoría con clase, forma, dimensiones y sistema de seguro puede captar las búsquedas de "marco y tapa D400".
4. **Publicar mariposa y check de hierro dúctil con datos.** Collaval solo muestra mariposa de PVC y una check de hierro dúctil.
5. **Responder a la transición hierro dúctil a HDPE.** Es su punto más diferenciado. Conviene publicar una guía de conexión a HDPE y, si FUNDIGSAC suministra esas piezas, incluirlas en catálogo. La disponibilidad debe confirmarse con la empresa.
6. **Publicar evidencia descargable.** Collaval dice "certificados" sin documentos enlazados. Fichas PDF y certificados por producto marcan la diferencia ante un comprador técnico. Solo debe mencionarse SEDAPAL si existe aprobación documentada.
7. **Ganar en señal local.** Collaval no menciona Lima y su teléfono estructurado es un valor de ejemplo. FUNDIGSAC ya declara dirección en Cercado de Lima. Puede añadir datos completos de `LocalBusiness` y páginas por sector.
8. **Destacar la cotización por DN y PN.** Collaval no usa "cotización" en encabezados. Una llamada a cotizar visible en cada ficha cubre esa intención de compra.
9. **Competir en contenido técnico.** Sus artículos sobre válvulas de compuerta y tipo lug muestran qué dudas considera rentables. Se pueden publicar guías más completas, con normas y tablas de selección.
10. **Mantener la calidad básica.** Títulos y metas únicos por categoría, un solo H1 y cero enlaces rotos bastan para superar a este competidor en SEO técnico. Debe verificarse con los KPI del propio sitio, que no se midieron aquí.

## PageSpeed móvil

La API pública respondió HTTP 429 por cuota diaria agotada (`rateLimitExceeded`). Se hizo una sola llamada y se registra **n/d**. Por eso no hay puntuación de rendimiento ni de SEO, ni métricas de carga de este sitio.
