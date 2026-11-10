# Auditoría de referencias de diseño: bookmarks 01 a 10

Fecha de visita: 2026-11-10. Navegador: Claude in Chrome, en una pestaña propia (cerrada al terminar). No se inició sesión, no se enviaron formularios ni se descargaron archivos. En getdesign.md se rechazaron las cookies no esenciales.

**Nota sobre viewports.** Todas las portadas se capturaron en escritorio (ventana de 1440 px; el marco de captura real fue de 1568 px). La orden `resize_window` 390x844 devolvió éxito, pero el viewport siguió en 1568 px porque la ventana de Chrome está maximizada y la comparten otros agentes. Por eso el ancho de teléfono **no se verificó directamente**. Donde el propio sitio ofrecía una vista móvil (selector de dispositivo en SmoothUI, maqueta de teléfono en designdotmd y vista de prototipo en Stitch), esa fue la evidencia móvil. Al terminar, la ventana volvió a 1440x900.

Las ideas se pensaron para encajar en los diseños restaurados: `frontend` (2026-11-04: hero fotográfico con carrusel de válvulas, CTA naranja #f26a1b, navy, tipografía tipo Archivo), `admin` (2026-10-20: "libro mayor industrial", sidebar de 9 secciones, dashboard de KPI, tablas densas, IBM Plex) y `stock` (2026-10-30: Fraunces + Archivo, paleta "Slab" #f1f2f4/#0e0f11/#d7261e, tarjetas con sombra y navegación inferior móvil). Son mejoras dentro de esos diseños, no reemplazos. Siempre que se pueda, se implementan con CSS, SVG o dependencias que ya existen. No se propone copiar código propietario, logotipos, imágenes ni textos.

Escalas: impacto 0–5; esfuerzo S (menos de 1 día), M (1–3 días), L (más de 3 días).

---

## 1. Stitch (Google)

- **URL:** https://stitch.withgoogle.com/
- **Estado:** visitado. El navegador ya tenía una sesión del usuario abierta. Solo se miraron la galería de inspiración y un prototipo público; no se creó ni se editó nada.
- **Páginas visitadas:** portada (prompt y carrusel "Need inspiration?"); prototipo "Auralis SaaS Landing Page" (https://stitch.withgoogle.com/projects/3907361547178343444), en modo Preview, recorrido con scroll.
- **Viewports:** escritorio. A 390 px no se pudo comprobar (ver nota). El prototipo tiene una barra lateral con selector de dispositivo.
- **Descripción:** generador de interfaces con IA. Las ideas útiles salen de los ejemplos de la galería, no de la herramienta.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Impacto | Esfuerzo | Coste rendimiento | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B1-1 | Prototipo Auralis | Sección bento: una tarjeta grande con degradado, una secundaria y debajo una fila de 4 chips con icono (Music, SFX, Voices, Image & Video). | La portada lista las familias de producto con el mismo peso, así que la línea principal (válvulas de hierro dúctil) no destaca. | Bento "Líneas de producto": tarjeta grande con foto de válvula y CTA, tarjeta secundaria para accesorios HDPE y fila de chips (Acoplamientos, Tuberías, Repuestos, Servicio técnico). CSS grid, sin librerías. | frontend / sección Productos de la home | 4 | M | Bajo (CSS grid; fotos con `loading="lazy"`) | Chips como enlaces de 44 px o más con texto visible; orden de lectura igual al visual | aprovechar |
| B1-2 | Prototipo Auralis | Pill tipo eyebrow ("Auralis Studio", "Auralis Agents") sobre cada título de sección. | Las secciones largas no dicen de un vistazo a qué sector o línea pertenecen. | Eyebrow en pill navy claro con el sector ("Saneamiento", "Minería", "Riego") sobre el H2. | frontend / encabezados de sección | 2 | S | Nulo | El eyebrow es texto real dentro del flujo; no se usa como único heading | aprovechar |
| B1-3 | Prototipo Auralis | Hero tipográfico: titular grande a la izquierda, párrafo corto alineado a la derecha y un par de CTA (relleno + outline). | En el carrusel del hero, el texto compite con la foto y el CTA secundario se pierde. | Sin tocar la foto ni el carrusel: titular a la izquierda, bloque de especificaciones (normas, rango DN) a la derecha y par de CTA naranja + outline blanco. | frontend / hero con carrusel de válvulas | 3 | S | Nulo | Contraste del texto sobre la foto con overlay de al menos 4.5:1 | adaptar |
| B1-4 | Prototipo (rail derecho) | Rail vertical con selector desktop/móvil para previsualizar la pantalla. | El staff edita fichas y banners sin ver cómo quedan en el teléfono. | Botón "Vista previa" en el editor de fichas del admin, con alternancia escritorio/móvil (iframe a 390 px). | admin / editor de producto y contenidos | 3 | M | Bajo (iframe solo cuando se abre) | Toggle como `radiogroup` con etiquetas | adaptar |
| B1-5 | Portada | Chips de prompts sugeridos bajo el campo ("A mobile leaderboard…", "Make a catalog page…"). | Quien busca en el catálogo no sabe qué términos funcionan (DN, PN, tipo de unión). | Chips de búsquedas frecuentes bajo el buscador: "Válvula compuerta DN100", "Acople HDPE 110 mm", "Brida PN16". | frontend / buscador del catálogo | 3 | S | Nulo | Chips como botones con nombre accesible; navegables con teclado | aprovechar |
| B1-6 | Prototipo Auralis | Al hacer scroll rápido, una sección quedó en blanco hasta que terminó su animación de entrada. | Riesgo de que el contenido quede invisible si falla el JS o la animación tarda. | Regla: ninguna sección se oculta con `opacity:0` sin fallback; animar solo `transform` y mostrar el contenido con `prefers-reduced-motion`. | transversal / animaciones de entrada | 2 | S | Mejora (menos repintado) | Evita contenido invisible para lectores de pantalla y conexiones lentas | descartar el patrón (sirve como lección) |

---

## 2. v0 (Vercel)

- **URL:** https://v0.dev/chat (redirige a https://v0.app/)
- **Estado:** visitado. La galería se ve sin iniciar sesión. La vista previa de "Shopify Ecommerce Template" mostró "Server Error" y https://v0.app/templates/e-commerce devolvió "Not Found".
- **Páginas visitadas:** portada; https://v0.app/templates; https://v0.app/templates/salesops-dashboard-9q2Mfgu6cDi (preview recorrido con scroll); https://v0.app/templates/shopify-ecommerce-template-XmzC9oi7g4m (preview roto).
- **Viewports:** escritorio. 390 px no verificado (ver nota).
- **Descripción:** generador de apps con IA y galería de plantillas de la comunidad. Lo más útil para FUNDIGSAC es la plantilla de dashboard comercial.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Impacto | Esfuerzo | Coste rendimiento | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B2-1 | SalesOps Dashboard | KPI con icono en esquina y chip de variación con flecha (+12,5 % verde, −5 rojo). | Los KPI del dashboard no dicen si el número mejora o empeora. | Añadir a cada KPI del admin la variación frente al periodo anterior, con flecha, signo y texto ("+8 % vs. oct."), usando los colores del ledger. | admin / tarjetas KPI del dashboard | 4 | S | Nulo (una consulta agregada más) | La variación no depende solo del color: lleva signo, flecha y `aria-label` | aprovechar |
| B2-2 | SalesOps Dashboard | "Pipeline Stages": barras horizontales por etapa con conteo y % y, al pie, "Total Pipeline Value". | No hay una vista del embudo de cotizaciones de B2B. | Panel "Embudo de cotizaciones": Solicitada → Cotizada → Negociación → Ganada, con barras CSS, conteo, % y total en S/ al pie. | admin / dashboard, módulo Cotizaciones | 5 | M | Bajo (barras en CSS, sin librería de gráficos) | Barras con texto numérico visible; tabla oculta equivalente para lectores de pantalla | aprovechar |
| B2-3 | SalesOps Dashboard | "Recent Deals": avatar con inicial, cliente, responsable y hora relativa, monto, pill de estado con icono (Won/Pending) y "View all". | Las últimas cotizaciones exigen entrar al módulo. | Lista "Últimas cotizaciones" en el dashboard: razón social, vendedor, hace X h, monto y estado con icono y texto; enlace "Ver todas". | admin / dashboard | 4 | S | Nulo | Estado con icono y texto; fila completa como enlace | aprovechar |
| B2-4 | SalesOps Dashboard | Selector "Last 30 days" junto al título Overview. | Los KPI no indican a qué periodo corresponden. | Selector de periodo global (7 d / 30 d / trimestre / año) en la cabecera del dashboard, aplicado a todos los widgets. | admin / cabecera del dashboard | 3 | S | Nulo | `select` nativo o listbox accesible con etiqueta | aprovechar |
| B2-5 | /templates | Tarjetas de categoría con mosaico de 2x2 miniaturas. | Las categorías del catálogo se muestran con una sola imagen o solo con texto. | Tarjeta de categoría con mosaico 2x2 de fotos de productos reales (válvula, brida, acople, tubería). | frontend / índice de categorías del catálogo | 3 | M | Medio (4 imágenes por tarjeta: usar miniaturas WebP de unos 200 px) | `alt` vacío en el mosaico decorativo; nombre de la categoría como texto | adaptar |
| B2-6 | SalesOps Dashboard | Ranking "Top Performers" con medalla 1-2-3 y ventas por persona. | — | No aplica: un ranking público de vendedores no es prioridad y expone el rendimiento de personas. | admin | 1 | S | — | — | descartar |

---

## 3. Magic UI

- **URL:** https://magicui.design/
- **Estado:** visitado.
- **Páginas visitadas:** portada (hero, showcase, muro de testimonios); /docs/components/number-ticker; /docs/components/bento-grid (hover sobre una tarjeta); /docs/components/marquee.
- **Viewports:** escritorio. 390 px no verificado (ver nota).
- **Descripción:** biblioteca de componentes animados para React, Tailwind y Motion. El repositorio público declara licencia MIT; hay que verificarla en el repo antes de copiar. También tiene una línea Pro de pago, que queda excluida.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Impacto | Esfuerzo | Coste rendimiento | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B3-1 | /number-ticker | Número que cuenta hasta el valor final. | Las cifras de trayectoria (años, obras, km instalados) se leen como texto plano. | Franja de cifras con conteo al entrar en el viewport (IntersectionObserver y unas 20 líneas de JS). El HTML trae ya el valor final. | frontend / franja "FUNDIGSAC en cifras" | 3 | S | Bajo | Valor final en el DOM; sin animación con `prefers-reduced-motion`; `tabular-nums` | adaptar (implementación propia, sin dependencia) |
| B3-2 | /marquee | Dos filas de tarjetas que se desplazan en sentidos opuestos, con bordes desvanecidos por máscara. | Los clientes, certificaciones y normas (ISO, AWWA, NTP) no tienen un lugar visible. | Marquesina de logos de clientes y sellos de norma, animada con CSS, con `mask-image` en los bordes y pausa al pasar el puntero o enfocar. | frontend / franja de confianza bajo el hero | 3 | S | Bajo (solo CSS) | Pausa con hover y foco; estática con reduced motion; lista duplicada con `aria-hidden` | adaptar |
| B3-3 | /bento-grid | Tarjetas bento con icono, título, descripción, "Learn more →" y una mini vista previa animada (pila de notificaciones). | La sección de sectores (agua, saneamiento, agro, minería) es plana. | Bento de sectores: cada tarjeta muestra una foto de obra o un pictograma SVG y "Ver soluciones →"; el hover sube la tarjeta 2 px y aumenta la sombra. | frontend / sección Sectores | 3 | M | Bajo | Toda la tarjeta enlazada con un solo foco; el hover no es necesario para leer | adaptar |
| B3-4 | Portada | Pill de anuncio sobre el H1 ("Introducing Dither Field >"). | Novedades como un catálogo nuevo o una línea nueva no se anuncian en la portada. | Pill sobre el titular del hero: "Nuevo: catálogo técnico 2026 →", que enlaza a la página de descargas. | frontend / hero | 3 | S | Nulo | Enlace con texto descriptivo; contraste sobre la foto | aprovechar |
| B3-5 | Portada | Muro de testimonios en masonry, con tarjetas de tweets. | Faltan pruebas sociales verificables. | Cambiar los tweets por "Obras referenciales": tarjeta con foto, cliente, ubicación y producto suministrado. | frontend / sección Proyectos | 2 | M | Medio (imágenes) | Texto real, sin capturas de texto | adaptar |
| B3-6 | Sidebar de docs | Etiquetas "New" y "Pro" junto a los ítems del menú lateral. | El staff no detecta qué módulos del admin son nuevos. | Badge "Nuevo" temporal (30 días) junto a la sección correspondiente del sidebar de 9 secciones. | admin / sidebar | 2 | S | Nulo | Badge con texto, no solo un punto de color | aprovechar |

---

## 4. SmoothUI

- **URL:** https://smoothui.dev/
- **Estado:** visitado.
- **Páginas visitadas:** portada (pestañas de demo Landing/Dashboard; clic en KPI "Error rate"); /docs/components (índice de 181 primitivas); /docs/components/animated-stepper; /docs/components/svg-draw-on-scroll (scroll dentro del panel); /docs/components/content-skeleton (con selector de vista móvil).
- **Viewports:** escritorio; vista móvil mediante el selector de dispositivo del propio preview.
- **Descripción:** componentes animados para shadcn/ui (Motion, GSAP, Tailwind). Repositorio público educlopez/smoothui; la página no muestra la licencia, así que hay que verificarla en el repo antes de copiar.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Impacto | Esfuerzo | Coste rendimiento | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B4-1 | Portada, demo Dashboard | "Click a KPI to filter": al pulsar "Error rate", la tarjeta se invierte (fondo claro), el gráfico cambia a esa métrica, la actividad se filtra y aparece "Reset". | Los KPI del dashboard son solo de lectura; para profundizar hay que ir a otra sección. | KPI como filtros: al pulsar "Cotizaciones pendientes" o "Stock bajo mínimo", el gráfico y la lista de actividad muestran ese subconjunto; enlace "Quitar filtro". | admin / dashboard | 5 | M | Bajo (filtrado en el cliente sobre datos ya cargados) | KPI como `button` con `aria-pressed`; el cambio se anuncia en una región `aria-live` | aprovechar |
| B4-2 | Portada, demo Dashboard | "Recent activity": icono de estado por evento (desplegado, fallo en rojo) con origen y hora. | Al abrir la app de stock no se ven los últimos movimientos de EPP. | Feed "Actividad reciente" en la home de stock: entrega, devolución, ingreso; icono, trabajador o área y hace X min; el estado de error con icono y texto. | stock / inicio | 3 | S | Nulo | Iconos con texto; lista semántica `ul` | aprovechar |
| B4-3 | /svg-draw-on-scroll | Trazo SVG que se dibuja al hacer scroll con un punto en la punta; se borra al subir; opción `once`. | "Cómo trabajamos" (fundición, mecanizado, prueba hidráulica, despacho) es una lista estática. | Línea de "tubería" en SVG que une las etapas y se dibuja una sola vez al hacer scroll (`stroke-dashoffset`), con el punto naranja #f26a1b en la punta. | frontend / sección Proceso | 4 | M | Bajo (un path SVG; scroll-driven animation de CSS con fallback) | Con reduced motion se muestra completa; las etapas son texto en lista ordenada | aprovechar |
| B4-4 | /animated-stepper | Asistente horizontal de 4 pasos con línea de progreso, números o check y botones Previous/Next. | El formulario de cotización es largo y de un solo paso. | Cotización en pasos: Producto → Cantidades y medidas → Datos de empresa → Confirmar, con línea de progreso navy y CTA naranja. | frontend / formulario de cotización | 4 | M | Bajo | `aria-current="step"`; foco al encabezado de cada paso; errores junto al campo | adaptar |
| B4-5 | /content-skeleton | Skeleton con la forma del contenido final, pulso suave y ARIA; insignia de peso (~7.3 kB). | Mientras carga Supabase, la app de stock muestra la pantalla vacía o un spinner. | Skeletons con la forma exacta de las tarjetas "Slab" (título, cantidad, chip), color #e3e5e8 sobre #f1f2f4. | stock / listas de EPP e inventario | 3 | S | Nulo (CSS) | `aria-busy="true"` en el contenedor; sin pulso con reduced motion | aprovechar |
| B4-6 | /docs/components | Índice filtrable por categorías (Patterns, Navigation, Data Viz, Loaders…) con contador ("181 primitives"). | — | Ya está cubierto por B6-4 y B10-5 (filtros con conteo en el catálogo). | frontend | 2 | S | — | — | descartar (duplicado) |

---

## 5. Animate UI

- **URL:** https://animate-ui.com/
- **Estado:** visitado. La URL adivinada /docs/components/animate/bottom-navigation dio 404; la ruta correcta es la de abajo.
- **Páginas visitadas:** portada ("Every primitive, alive": switch, tabs, accordion, checkbox, sliding number, toast, progress); /docs/primitives/texts/sliding-number; /docs/primitives/radix-ui/tabs (clic en "Reports"); /docs/primitives/animate-ui/bottom-navigation (scroll y clic).
- **Viewports:** escritorio. El demo de navegación inferior viene en un marco con forma de teléfono. 390 px no verificado (ver nota).
- **Descripción:** primitivas animadas sobre Radix, Base UI y React Aria. La página dice "source code is available on GitHub" pero no indica la licencia; hay que verificarla antes de copiar.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Impacto | Esfuerzo | Coste rendimiento | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B5-1 | /bottom-navigation | Barra inferior en pill: el resaltado se desliza al ítem elegido, hay un botón "+" separado (accessory) y la barra puede encogerse o esconderse al bajar. | La navegación inferior de stock es estática y la acción principal (registrar entrega) queda a la misma altura que el resto. | Mejorar la nav inferior actual: indicador #0e0f11 que se desliza (`transform`), botón "+" circular aparte en rojo #d7261e para "Registrar entrega", y la barra se oculta al bajar y vuelve al subir. | stock / navegación inferior móvil | 5 | M | Bajo (solo `transform`; listener de scroll pasivo) | Objetivos de 44 px o más; `aria-current="page"`; con reduced motion no se oculta | aprovechar |
| B5-2 | /tabs (Radix) | Tabs con pill de fondo que se desliza entre Overview, Analytics, Reports y Settings, y contenido en tarjeta. | Las pestañas de detalle (producto en admin, trabajador en stock) cambian de golpe y se pierde dónde se está. | Indicador deslizante para las tabs existentes (ficha, stock, movimientos), con CSS y la posición calculada en JS. | admin / ficha de producto; stock / detalle de trabajador | 3 | S | Nulo | Patrón ARIA de tabs, flechas de teclado; el cambio de contenido es inmediato | aprovechar |
| B5-3 | /sliding-number | Número tipo odómetro: los dígitos ruedan hasta el nuevo valor ("12,480 installs this week"). | Tras una entrega, el stock disponible cambia sin ninguna señal. | Al confirmar un movimiento, la cantidad de la tarjeta rueda al nuevo valor (máscara CSS por dígito). | stock / tarjeta de EPP y KPI de inicio | 3 | S | Bajo | Valor final anunciado en `aria-live="polite"`; `tabular-nums` | aprovechar |
| B5-4 | Portada (Progress) | Barra "Uploading" con porcentaje que cambia de forma animada. | Al subir fichas técnicas PDF o fotos no se ve el progreso. | Barra de progreso fina navy con porcentaje en tabular-nums para cada archivo subido. | admin / carga de fichas y galería | 3 | S | Nulo | `progress` nativo o `role="progressbar"` con valores | aprovechar |
| B5-5 | Portada (Toast) | Toast compacto "… saved" con botón cerrar. | No hay confirmación visible tras guardar o registrar. | Toast inferior (sobre la nav en stock) "Entrega registrada · Deshacer", que desaparece a los 5 s. | stock / confirmaciones; admin / guardado | 3 | S | Nulo | `role="status"`; sin cierre automático si contiene una acción | adaptar |
| B5-6 | Portada (Accordion) | Acordeón FAQ animado que mantiene la accesibilidad de Radix. | Las dudas técnicas (presión de trabajo, normas, compatibilidad) se resuelven por teléfono. | FAQ técnico por familia de producto con `details/summary` nativo y transición de altura en CSS. | frontend / ficha de producto y página FAQ | 2 | S | Nulo | `details/summary` nativo, accesible por defecto | adaptar |

---

## 6. 21st.dev (Community components)

- **URL:** https://21st.dev/community/components
- **Estado:** visitado. El navegador tenía sesión del usuario; no se usó ni se guardó nada. El archivo Component.tsx de algunos componentes aparece con candado.
- **Páginas visitadas:** /community/components (modal de preview "Contour line Mountain"); /community/components/s/comparison; /community/components/s/table; https://21st.dev/@arunachalam/components/animated-table (con scroll y lectura del Usage).
- **Viewports:** escritorio. 390 px no verificado (ver nota).
- **Descripción:** marketplace de componentes de la comunidad. La licencia depende de cada autor y debe revisarse componente por componente.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Impacto | Esfuerzo | Coste rendimiento | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B6-1 | Preview "Contour line Mountain" | Fondo de curvas de nivel en línea fina, marcadores con nombre y altitud, y tarjeta de detalle (nombre, descripción, cifra, "Learn more"). | No se ve en qué lugares del país hay obras con productos FUNDIGSAC. | "Obras en el Perú": SVG estilizado con curvas de nivel navy al 10 %, marcadores naranjas por obra y tarjeta con proyecto, región, producto y DN. Arte propio. | frontend / sección Proyectos o Cobertura | 4 | L | Medio (SVG optimizado, de unos 30 kB o menos) | Lista de obras equivalente en HTML; marcadores como botones con nombre | adaptar |
| B6-2 | Animated Table | Tabla semántica con `tfoot` "Total Stock 320", `caption` y aparición de filas escalonada al montar. | Las tablas de stock y admin no muestran totales ni un caption que diga qué se ve. | Fila de total en `tfoot` (unidades, S/) y `caption` visible ("Stock de EPP por talla, almacén Lima"). Escalonado solo en la primera carga. | stock / tabla de inventario; admin / tablas de pedidos | 4 | S | Nulo | `caption`, `th scope`, `tfoot` semánticos | aprovechar (el patrón; el código no es necesario) |
| B6-3 | /s/comparison | Comparadores de dos columnas ("Choose X / Choose Y") con lista de checks y tablas de comparación por característica. | El cliente duda entre opciones técnicas (válvula de compuerta o mariposa; electrofusión o termofusión) y llama para preguntar. | Bloque "¿Cuál elegir?" en la ficha y en la guía: dos columnas con uso recomendado, rango DN/PN, ventajas y CTA a cada ficha. | frontend / ficha de producto y guías | 4 | M | Nulo | Tabla real con encabezados; los checks llevan texto ("Sí"/"No") | aprovechar |
| B6-4 | Sidebar /community | Categorías con contador (Backgrounds 345, Borders 63, Calls to Action 101…). | Los filtros del catálogo no dicen cuántos productos hay en cada uno. | Contador por categoría y por filtro (Válvulas 42, Acoplamientos 18…) que se actualiza al combinar filtros. | frontend / filtros del catálogo | 3 | S | Bajo (conteo en la consulta) | Conteo dentro del nombre accesible ("Válvulas, 42 productos") | aprovechar |
| B6-5 | Modal de preview | Preview en modal con "See similar" y "Scroll down to find components like this one". | Desde una ficha no se llega a productos relacionados. | Bloque "Productos similares" (misma familia o mismo DN) al final de la ficha. | frontend / ficha de producto | 3 | M | Bajo | Encabezado propio; tarjetas como lista | adaptar |
| B6-6 | /s/table | Muchas plantillas de pricing en tres columnas. | — | No aplica: FUNDIGSAC cotiza y no publica precios. | frontend | 0 | S | — | — | descartar |

---

## 7. Refero Styles

- **URL:** https://styles.refero.design/?sort=popular
- **Estado:** visitado. No se usó el buscador.
- **Páginas visitadas:** portada (orden Popular, scroll por la galería); https://styles.refero.design/style/90ce5883-bb24-4466-93f7-801cd617b0d1 (Linear: swatches y pestañas DESIGN.md / CSS Variables).
- **Viewports:** escritorio. 390 px no verificado (ver nota).
- **Descripción:** biblioteca de más de 2.000 sistemas de diseño extraídos de sitios reales, en formato DESIGN.md, Tailwind v4, CSS variables y tokens. Sirve como método de documentación, no como estética para copiar.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Impacto | Esfuerzo | Coste rendimiento | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B7-1 | Estilo Linear | Cada swatch lleva nombre, hex y regla de uso con prohibición ("use as a supporting accent, not as a status color"). | Los colores de marca se usan sin regla: el naranja aparece en estados y el rojo de stock como decoración. | Página interna de estilo con swatches y reglas: #f26a1b solo para CTA y enlaces de acción (frontend); #d7261e solo para alertas y stock crítico (stock); navy para estructura. | transversal / guía de estilo (ruta interna del admin o `docs/`) | 4 | M | Nulo | Cada regla incluye el par de contraste verificado | aprovechar |
| B7-2 | Estilo Linear | Una misma fuente exportada en pestañas: DESIGN.md, Tailwind v4, CSS Variables y Design Tokens. | Las tres apps definen los colores y radios por separado, y van divergiendo. | Un archivo de tokens por app (JSON o CSS) que genere las `:root` CSS variables, más un DESIGN.md corto que lo explique, para personas y agentes. | transversal / tokens de frontend, admin y stock | 4 | M | Nulo | Tokens de foco y contraste incluidos | aprovechar |
| B7-3 | Estilo Linear | Escala de superficies con nombres de rol (void → carbon → obsidian → graphite → smoke) y el uso de cada una. | En el admin los grises y navys se eligen a ojo, y los niveles de tabla, panel y sidebar no se distinguen. | Escala navy del ledger con roles: `--surface-canvas`, `--surface-panel`, `--surface-row-alt`, `--border-hairline`, `--border-strong`. | admin / variables de tema | 3 | S | Nulo | Las diferencias entre niveles no son lo único que transmite estructura | aprovechar |
| B7-4 | Galería | Las tarjetas rotan entre varias capturas del mismo sitio. | Cada tarjeta de obra o proyecto muestra una sola foto. | Al pasar el puntero o enfocar, la tarjeta pasa por 2–3 fotos de la obra (fundido CSS). | frontend / tarjetas de proyecto | 2 | S | Medio (imágenes extra con carga diferida) | Sin rotación automática; con reduced motion, solo la primera foto | adaptar |
| B7-5 | Estilo Linear | Lema de una línea que define el sistema ("midnight precision instrument"). | Cada cambio nuevo puede desviarse del carácter de cada app. | Un lema por app en su DESIGN.md: admin "libro mayor industrial", stock "Slab de campo", frontend "catálogo fotográfico de fundición". | transversal / documentación | 2 | S | Nulo | — | aprovechar |

---

## 8. getdesign.md

- **URL:** https://getdesign.md/
- **Estado:** visitado. Se rechazaron las cookies no esenciales ("Reject Non-Essential"). No se descargó nada ni se ejecutó el comando npx.
- **Páginas visitadas:** portada (catálogo de más de 550 marcas); https://getdesign.md/dji/design-md (paleta, tipografía y variantes de botón, recorrido con scroll).
- **Viewports:** escritorio. 390 px no verificado (ver nota).
- **Descripción:** colección de DESIGN.md basados en marcas conocidas. Las marcas son de terceros y no se reutilizan; solo se toma el método.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Impacto | Esfuerzo | Coste rendimiento | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B8-1 | DJI, "Button Variants" | Catálogo de botones con nombre, medidas y regla de composición ("the store pair always sits side by side, cart first"). | Cada pantalla combina los botones de forma distinta. | Catálogo propio: `btn-primary` naranja (Cotizar), `btn-outline` navy (Ficha técnica), `btn-ghost-photo` (sobre el hero). Regla: "Ficha técnica" va siempre junto a "Cotizar", con el secundario a la izquierda. | transversal / componentes de botón | 4 | S | Nulo | Foco visible común a todas las variantes; tamaño mínimo de 44 px | aprovechar |
| B8-2 | DJI | `button-hero-ghost` en pill con contorno blanco sobre fotografía oscura. | En el hero con foto, el CTA secundario no contrasta. | CTA secundario del carrusel con contorno blanco de 1,5 px, texto blanco y fondo translúcido navy al 30 %, junto al CTA naranja. | frontend / hero con carrusel | 3 | S | Nulo | Contraste de al menos 4.5:1 contra la zona de foto (garantizado por el overlay) | aprovechar |
| B8-3 | DJI, paleta | "Tier Orange" para eyebrows de rango de producto, "Badge Orange" para badges de esquina, "Error" para Out of Stock. | Las tarjetas de producto no muestran a primera vista la norma, la presión ni la disponibilidad. | Tarjeta de producto con eyebrow ("PN16 · AWWA C509"), badge de esquina "Stock inmediato" o "A pedido" (texto e icono) y nombre debajo. | frontend / tarjeta de producto del catálogo | 4 | S | Nulo | La disponibilidad se indica con texto, no solo con color | aprovechar |
| B8-4 | DJI, tipografía | Tabla de roles tipográficos con medidas (product-name 24/400, price 20/600, option-title 18/600, body 16/400). | No hay una escala tipográfica documentada para fichas, precios referenciales ni opciones. | Escala tipográfica por rol para el frontend (estilo Archivo): `product-name`, `spec-label`, `spec-value`, `section-eyebrow`, `body`. | frontend / tokens tipográficos | 3 | S | Nulo | Interlineado de 1,5 o más en cuerpo; tamaño mínimo de 16 px | aprovechar |
| B8-5 | DJI | "Compare Options" como botón de 8 px de radio con icono ⊕. | No se pueden comparar varias válvulas o medidas. | Botón "Comparar" en la tarjeta y la ficha que añade el producto a un comparador de hasta 3 (con B6-3). | frontend / catálogo y ficha | 3 | M | Bajo (estado en localStorage) | Estado "añadido" anunciado; contador accesible | adaptar |
| B8-6 | DJI, superficies | Escala de grises claros con uso asignado (canvas, canvas-soft, panel, fog, announce). | Las secciones de la home no tienen ritmo visual entre bloques. | Alternar bandas `canvas` (#fff) y `canvas-soft` (gris muy claro) entre secciones, reservando el navy para el footer y las bandas de CTA. | frontend / ritmo de secciones de la home | 2 | S | Nulo | No depender de la diferencia de fondo para separar contenido | aprovechar |

---

## 9. UI Skills

- **URL:** https://www.ui-skills.com/
- **Estado:** visitado. El formulario de newsletter no se usó.
- **Páginas visitadas:** portada (catálogo de skills y DESIGN.md); https://www.ui-skills.com/playbook/use-tabular-nums-for-data (toggle Default/Tabular); https://www.ui-skills.com/playbook (índice de 48 lecciones); lección "Preview the next item in scroll lists".
- **Viewports:** escritorio. 390 px no verificado (ver nota).
- **Descripción:** catálogo de skills para agentes y un playbook de reglas de detalle de interfaz con demos interactivas. Es la fuente con más reglas aplicables de inmediato.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Impacto | Esfuerzo | Coste rendimiento | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B9-1 | /playbook/use-tabular-nums-for-data | Demo con toggle: con dígitos por defecto el número "baila"; con tabular-nums queda fijo. | En las tablas densas del admin y en las cantidades de stock las columnas no alinean. | `font-variant-numeric: tabular-nums` en celdas numéricas, KPI y contadores de las tres apps (IBM Plex y Archivo lo soportan). | transversal / tablas y KPI | 4 | S | Nulo | Mejora la lectura y comparación de cifras | aprovechar |
| B9-2 | /playbook ("Never use color alone for status") | Regla: el estado nunca se indica solo con color; lleva texto o icono. | En stock, el rojo #d7261e marca "crítico" sin texto; en el admin hay badges de color sin etiqueta. | Todos los estados de stock (OK / Bajo / Crítico / Agotado) y de cotización con icono y texto. | stock / tarjetas de EPP; admin / badges de estado | 5 | S | Nulo | Cumple WCAG 1.4.1 | aprovechar |
| B9-3 | /playbook ("Use 44px touch targets") | Regla: objetivos táctiles de al menos 44x44 px. | En campo se usa el móvil con guantes; los botones +/− y los ítems de la nav pueden quedarse cortos. | Auditar y subir a 44 px o más (48 px con guantes) los steppers de cantidad, la nav inferior, los chips de talla y las acciones de tarjeta. | stock / steppers, nav, chips | 5 | S | Nulo | WCAG 2.5.8; uso con guantes | aprovechar |
| B9-4 | Lección "Preview the next item in scroll lists" y "Fade the edges of scrollable lists" | Mostrar 16–32 px del siguiente ítem y desvanecer los bordes con `mask-image`. | Los carruseles horizontales (productos relacionados, chips de talla) no dejan ver que hay más contenido. | Carriles horizontales con `scroll-snap`, el siguiente ítem asomando 24 px y bordes desvanecidos con máscara CSS. | frontend / carriles de productos; stock / chips de talla y categoría | 3 | S | Nulo | Desplazable con teclado; botones prev/next opcionales | aprovechar |
| B9-5 | /playbook ("Limit each view to one accent color", "Reserve brand colors for links and actions") | Un solo acento por vista; los encabezados neutros y el color de marca solo para acciones. | El naranja #f26a1b aparece también en titulares y decoraciones, y pierde fuerza como CTA. | Regla del frontend: naranja solo en CTA y enlaces de acción; titulares en navy o negro. Comprobarlo en la revisión visual. | frontend / global | 4 | S | Nulo | Las acciones se reconocen mejor | aprovechar |
| B9-6 | /playbook ("Add scale feedback to pressed buttons") | Respuesta al pulsar con `:active { transform: scale(.96) }`. | En stock no se nota si un toque se registró, sobre todo con mala señal. | `:active` con escala 0,97 y transición de 100 ms en los botones y tarjetas pulsables de stock. | stock / botones y tarjetas | 3 | S | Nulo | Sin efecto con reduced motion | aprovechar |
| B9-7 | /playbook ("Use solid modal backdrops instead of blur") | Fondo de modal sólido en lugar de blur, porque el blur es costoso en pantalla completa. | En móviles de gama baja, los modales con `backdrop-filter` van con tirones. | Fondo de modal sólido (#0e0f11 al 60 %) en stock y admin; quitar `backdrop-filter` de los overlays a pantalla completa. | stock y admin / modales | 3 | S | Mejora | Foco atrapado en el modal; Esc para cerrar | aprovechar |
| B9-8 | /playbook ("Show form errors next to each field", "Add visible labels to every form field") | Error debajo de cada campo y etiqueta siempre visible (el placeholder no sirve de etiqueta). | El formulario de cotización usa placeholders como etiqueta y muestra los errores arriba. | Etiquetas visibles y errores en línea bajo cada campo (RUC, correo, cantidad), unidos con `aria-describedby`. | frontend / cotización y contacto | 4 | S | Nulo | WCAG 3.3.1 y 3.3.2 | aprovechar |

---

## 10. designdotmd.directory

- **URL:** https://designdotmd.directory/
- **Estado:** visitado.
- **Páginas visitadas:** portada (filtros por estilo, "This week's standouts", directorio de 256 entradas); https://designdotmd.directory/d/freight-logistics (preview "Kitchen sink" y "Ecommerce", con scroll hasta tokens y radios).
- **Viewports:** escritorio. La página de cada estilo muestra el mismo contenido en navegador de escritorio y en maqueta de teléfono a la vez, y esa fue la evidencia móvil.
- **Descripción:** directorio comunitario de archivos DESIGN.md con preview en varios tipos de página. El estilo "Freight Logistics" (gris acero, naranja de seguridad, códigos en mono, IBM Plex Sans/Mono) es muy cercano al ADN de FUNDIGSAC.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Impacto | Esfuerzo | Coste rendimiento | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B10-1 | /d/freight-logistics | "Steel grey, safety orange, tracking numbers in mono": etiquetas en IBM Plex Mono a 0,72 rem con tracking de 0,06 em. | Los códigos (n.º de cotización, lote, SKU, guía) se confunden con el texto corriente. | Códigos en IBM Plex Mono (ya está en el admin): `COT-2026-0412`, `LOTE 25-118`, `SKU VC-DN100-PN16`, con tracking leve. En el frontend, solo SKU y normas. | admin / tablas y detalle; frontend / ficha (SKU) | 4 | S | Nulo (fuente ya cargada en admin; en frontend, subset de unos 15 kB) | Mono legible a 12 px o más; permite copiar | aprovechar |
| B10-2 | /d/freight-logistics, "Ecommerce" | Ficha con chips de variante (Finish con punto de color), stepper de cantidad, aviso "Only 3 left at this finish", CTA naranja a todo el ancho con el total y miniaturas. | La ficha no permite elegir DN, PN o tipo de unión ni pasar directamente a cotizar esa combinación. | Ficha: chips para DN (100/150/200…), PN (10/16/25) y unión (brida/junta mecánica), stepper de cantidad, aviso "Stock inmediato en Lima" y CTA naranja "Agregar a cotización". | frontend / ficha de producto | 5 | M | Bajo | Chips como `radiogroup`; el stepper es un input numérico con botones de 44 px; el aviso es texto | aprovechar |
| B10-3 | /d/freight-logistics | Mismo estilo mostrado a la vez en escritorio y teléfono, con selector "try on: Kitchen sink / Landing page / Ecommerce / Event". | Los cambios de estilo se revisan solo en escritorio. | Página interna "kitchen sink" por app (botones, tarjetas, tablas, formularios) renderizada en un iframe de escritorio y otro de 390 px lado a lado. | transversal / guía de estilo interna | 2 | M | Nulo (solo en desarrollo) | Sirve para revisar foco y contraste de un vistazo | adaptar |
| B10-4 | /d/freight-logistics, tokens | Radios pequeños (sm 2 px, md 4 px, lg 6 px) y espaciado de 8/16/32. | El admin denso mezcla radios grandes de librerías con el aspecto de ledger. | Fijar en el admin los radios 2/4/6 px y el espaciado en múltiplos de 8, para reforzar el carácter de libro mayor. | admin / tokens de radio y espaciado | 3 | S | Nulo | — | aprovechar |
| B10-5 | Portada | Chips de filtro por estilo y categoría con conteo total ("256 results"). | El catálogo no permite filtrar por sector de aplicación. | Chips de sector (Agua potable, Saneamiento, Riego, Minería) sobre el listado, con "N productos" actualizado. | frontend / catálogo | 3 | S | Bajo | Chips `aria-pressed`; el conteo se anuncia en `aria-live` | aprovechar |
| B10-6 | /d/freight-logistics | Eyebrow en mono, mayúsculas y separado por puntos medios ("TECHNICAL · CORPORATE · BOLD · COOL") en naranja. | Las fichas no resumen el uso y el rango antes del título. | Eyebrow en las fichas y tarjetas: "AGUA POTABLE · PN16 · DN 100–300", en mono naranja sobre fondo claro (comprobar el contraste o usar navy). | frontend / ficha y tarjetas | 3 | S | Nulo | Si el naranja no llega a 4.5:1 en texto pequeño, usar navy | adaptar |

---

## Resumen por sitio

| # | Sitio | Estado | Ideas | Aprovechar / adaptar / descartar |
|---|---|---|---|---|
| 1 | Stitch | visitado (sesión del usuario ya abierta; solo lectura) | 6 | 3 / 2 / 1 |
| 2 | v0 | visitado (un preview roto, una URL 404) | 6 | 4 / 1 / 1 |
| 3 | Magic UI | visitado | 6 | 2 / 4 / 0 |
| 4 | SmoothUI | visitado | 6 | 4 / 1 / 1 |
| 5 | Animate UI | visitado | 6 | 4 / 2 / 0 |
| 6 | 21st.dev | visitado (algún código con candado) | 6 | 3 / 2 / 1 |
| 7 | Refero Styles | visitado | 5 | 4 / 1 / 0 |
| 8 | getdesign.md | visitado (cookies no esenciales rechazadas) | 6 | 5 / 1 / 0 |
| 9 | UI Skills | visitado | 8 | 8 / 0 / 0 |
| 10 | designdotmd.directory | visitado | 6 | 4 / 2 / 0 |

Total: 61 ideas.
