# Inspiración: marcadores 21–30

Auditoría del 2026-11-10 hecha con Claude in Chrome, en una pestaña propia que se cerró al terminar. No se inició sesión, no se enviaron formularios ni se descargaron archivos. En Mobbin se rechazaron las cookies no esenciales. En Awwwards el banner solo ofrecía "GOT IT" y quedó sin aceptar.

**Limitación de viewport.** El escritorio se capturó a ~1440 px (marco real de 1568×773). `resize_window` a 390×844 respondió "ok" en todos los sitios, pero la ventana es compartida con otras pestañas y no bajó del ancho de escritorio: las capturas "móviles" salieron iguales a las de escritorio (se comprobó en prompt-motion.com y en ui.gradientdeck.com). Por eso no hay evidencia propia a 390 px. Las notas de móvil que siguen se deducen del diseño observado y hay que validarlas con DevTools o con el navegador integrado.

Apps destino: **frontend** (sitio comercial: hero fotográfico, carrusel de válvulas, CTA naranja #f26a1b, navy), **admin** ("industrial ledger": IBM Plex, sidebar de 9 secciones, tablas densas, motion en CSS), **stock** (EPP de campo: Fraunces + Archivo, paleta Slab #f1f2f4/#0e0f11/#d7261e, tarjetas con sombra, bottom nav móvil). Toda idea debe modernizar el diseño actual sin reemplazarlo. El motion usa framer-motion/motion (frontend y stock) o CSS (admin) y siempre respeta `prefers-reduced-motion`. No se copia código, imágenes, logos ni textos de terceros.

Leyenda: Impacto 0–5 · Esfuerzo S/M/L · Decisión: aprovechar / adaptar / descartar.

---

## 21 · Anime.js — https://animejs.com/

- **Estado:** OK, público.
- **Páginas visitadas:** `/` (hero y scroll hasta la vista explosionada 3D), `/easing-editor/spring/default`, `/documentation/svg/createdrawable`, `/documentation/utilities/stagger`.
- **Viewports:** escritorio 1440. Móvil no aplicado (ver limitación).
- **Descripción:** sitio oscuro de una librería de animación. El hero es un dial con anillo segmentado y marcas de graduación. Al hacer scroll aparece un motor 3D que se separa en piezas a lo largo de su eje. Hay un editor de easings con presets de spring (default, snappy, bouncy, strong) que se ajustan con `bounce` y `duration`, y una documentación con demos vivas de dibujo de líneas SVG y stagger desde el centro de una grilla.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Coste perf. | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B21-1 | / (scroll) | Ensamble mecánico que se "explosiona" en piezas a lo largo de su eje mientras se hace scroll | El cliente no ve qué hay dentro de una válvula (cuerpo, cuña, vástago, bonete, sellos) ni por qué la de FUNDIGSAC es mejor | Sección "Anatomía" en la ficha de válvula: 4–6 capas PNG/SVG propias que se separan en el eje con `useScroll` + `useTransform` de framer-motion y etiquetas que aparecen por pieza. Sin WebGL | frontend · ProductDetail > `ValveAnatomy` | 5 | M | Medio: imágenes por capa en AVIF/WebP y solo `transform` | Con reduced motion se muestra la vista explosionada estática. Etiquetas como texto real con lista equivalente | adaptar (2.5D por capas, no 3D) |
| B21-2 | /documentation/svg/createdrawable | Trazos SVG que se dibujan (`draw 0→1`), también ligados al scroll | Las aplicaciones (redes de agua, riego, relaves) se explican con fotos y nada muestra el sistema | Diagrama SVG de red (tubería HDPE → acople → válvula) que se dibuja al entrar en vista con `pathLength` de framer-motion, 800–1200 ms con ease-out | frontend · Sectores > `NetworkDiagram` | 4 | S | Bajo | Reduced motion: trazo completo sin animar. `<title>`/`<desc>` en el SVG | aprovechar |
| B21-3 | /documentation/utilities/stagger | Stagger de valores y tiempos desde el centro de una grilla | En el dashboard las tarjetas KPI aparecen de golpe y no hay jerarquía de lectura | Stagger CSS con `--i` y `animation-delay: calc(var(--i)*35ms)`, en orden de lectura (no desde el centro) | admin · Dashboard > grilla KPI | 3 | S | Muy bajo | Desactivar con `@media (prefers-reduced-motion)` | adaptar |
| B21-4 | /easing-editor | Presets de spring con nombre (default/snappy/bouncy/strong) parametrizados por bounce y duración, exportables a JS y CSS | Cada app anima con curvas distintas y sin criterio común | Tokens de motion compartidos: `spring.default` (bounce 0.1, 400 ms) y `spring.snappy` (bounce 0, 250 ms). Para admin, equivalentes CSS con `linear()`. Sin preset bouncy (ver B28-2) | transversal · `motion-tokens` | 4 | S | Nulo | Un solo punto donde aplicar reduced motion | aprovechar |
| B21-5 | / (sección Scope) | Animaciones que cambian según media query (orientación) con un único scope | Stock en móvil vertical arrastra las mismas animaciones que en escritorio | Hook `useMotionScope()` que junta `matchMedia` (orientación, `pointer: coarse`) y reduced motion y devuelve variantes reducidas en campo | stock · hook global | 2 | S | Nulo | Mejora el control de reduced motion | adaptar |
| B21-6 | / (hero) | Dial circular con anillo segmentado y marcas de graduación | No hay una lectura rápida de cobertura de stock por categoría de EPP | Gauge SVG de cobertura (días de stock) por categoría, con ticks y un segmento crítico en #d7261e. Nada de arcoíris: paleta Slab | stock · Inicio > `CoverageGauge` | 3 | M | Bajo | Valor numérico visible y `aria-label`. El color no es la única señal | adaptar |

---

## 22 · Mobbin — https://mobbin.com/discover/apps/ios/latest

- **Estado:** parcial. La URL redirige a la home de marketing (`/?redirect_to=…`) porque la biblioteca pide cuenta. No se inició sesión.
- **Páginas visitadas:** home de marketing (scroll completo con el demo embebido de Apps/Sites) y `/pricing`.
- **Viewports:** escritorio 1440. Móvil no aplicado.
- **Descripción:** marketing claro, tipografía grotesca muy grande. Incluye un demo de la app con un mega-índice en columnas (Categorías, Pantallas, UI Elements, Flows) y una búsqueda que se "escribe" sola. El texto se revela de gris a negro con el scroll, el CTA aparece en el header sticky después del hero y pricing usa un toggle Yearly/Quarterly.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Coste perf. | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B22-1 | home (demo embebido) | Mega-índice de 4 columnas tituladas (Categories / Sections / Styles…) con enlaces en tipografía grande | El catálogo cruza líneas y sectores, y el menú actual obliga a navegar a ciegas | Mega-menú "Productos" con 3 columnas: Líneas (Válvulas, Fittings HDPE, Acoples, Tuberías), Sectores (Agua, Saneamiento, Agro, Minería) y Recursos (Fichas, Certificados) | frontend · Header > `MegaMenu` | 4 | M | Bajo | Patrón disclosure con botón, `aria-expanded` y cierre con Esc. Ítems tabulables | adaptar |
| B22-2 | home | Párrafo que pasa de gris a tinta línea por línea con el scroll | La sección "Nosotros" se lee como un bloque plano | Manifiesto de 3 líneas con `animation-timeline: view()` en CSS y fallback a color final | frontend · Nosotros > `Manifesto` | 2 | S | Muy bajo (CSS nativo) | El contraste final cumple AA. El gris inicial es decorativo y el texto siempre es legible | adaptar |
| B22-3 | home (header) | El botón "Join for free" aparece en el header sticky solo después de pasar el hero | El CTA naranja de cotizar se pierde al bajar por la página | Botón "Cotizar" #f26a1b que entra al header (fade + 8 px) cuando el CTA del hero sale de vista, vía IntersectionObserver | frontend · Header > `StickyQuoteCTA` | 4 | S | Muy bajo | Está siempre en el DOM y en el orden de tabulación. Sin desplazar layout | aprovechar |
| B22-4 | home | Consulta de ejemplo que se escribe sola ("Joyful onboarding") y luego muestra un rail de resultados | Los usuarios no saben qué buscar ni con qué nomenclatura (DN, PN, mm) | Placeholder rotativo con consultas reales ("válvula compuerta DN200", "electrofusión 110 mm") cada 3 s, en pausa mientras el campo tiene foco | frontend · Catálogo > `SearchBox` | 3 | S | Muy bajo | `<label>` real; el placeholder no lo reemplaza. Detenido con reduced motion | adaptar |
| B22-5 | /pricing | Toggle segmentado Yearly/Quarterly con nota de ahorro | El dashboard de admin no deja comparar periodos en un clic | Control segmentado Mes / Trimestre / Año con delta frente al periodo anterior | admin · Dashboard > `PeriodSegmented` | 2 | S | Nulo | `radiogroup` con flechas de teclado | adaptar |

Solo 5 ideas: el contenido principal (pantallas iOS) está detrás de login.

---

## 23 · React Bits — https://reactbits.dev/

- **Estado:** OK, público.
- **Páginas visitadas:** `/`, `/text-animations/count-up`, `/components/spotlight-card` (con hover), `/components/animated-list`.
- **Viewports:** escritorio 1440. Móvil no aplicado.
- **Descripción:** catálogo oscuro de unos 216 componentes animados. Cada página tiene preview, panel "Customize" (preset, trigger, easing, duración), toggles de dispositivo y "Copy for AI".

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Coste perf. | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B23-1 | /text-animations/count-up | Contador con trigger "in view", easing, separador, decimales y prefijo/sufijo configurables | Las cifras de confianza (años, km instalados, clientes) y los KPI se ven estáticos | `CountUp` propio con `animate()` de framer-motion e `Intl.NumberFormat('es-PE')`, 900 ms ease-out, una sola vez al entrar en vista | frontend · Home > franja de cifras; admin · KPI (versión CSS/JS mínima) | 4 | S | Muy bajo | El valor final va en el DOM con `aria-label` y la animación es `aria-hidden`. Reduced motion muestra el valor final | aprovechar |
| B23-2 | /components/spotlight-card | Luz suave que sigue al puntero, ilumina el borde y alcanza a las tarjetas vecinas | Las tarjetas de familia de producto no reaccionan al hover y se sienten planas | Radial-gradient navy al 6–8 % que sigue el puntero con variables CSS `--mx`/`--my`, solo con `(hover:hover) and (pointer:fine)` | frontend · Catálogo > `FamilyCard` | 3 | S | Bajo (sin re-render de React) | Puramente decorativo. El foco tiene su propio anillo visible | adaptar |
| B23-3 | /components/animated-list | Filas que entran con spring, selección que se desliza entre filas y navegación con flechas | Listas largas de movimientos y entregas sin foco claro ni teclado | Lista de movimientos con resaltado deslizante (`layoutId`) y flechas arriba/abajo. Entrada con spring snappy limitada a las primeras 10 filas | stock · Movimientos; admin · tablas (resaltado CSS) | 4 | M | Bajo si se limita la entrada | `aria-activedescendant` o roving tabindex. Contraste del resaltado ≥ 3:1 | adaptar |
| B23-4 | /components/* (toolbar) | Toggles de preview escritorio/tablet/móvil dentro de la página | El staff publica fichas sin ver cómo se ven en el teléfono del cliente | Vista previa de ficha de producto en admin con toggle 1440 / 768 / 390 (iframe con ancho fijo) | admin · Productos > `PreviewFrame` | 3 | M | Bajo | Toggles como `radiogroup` | adaptar |
| B23-5 | / (hero) | Fondo WebGL "GradientWaves" con presets de color | Ninguno: no encaja con la estética industrial | — | — | 1 | M | Alto (WebGL continuo) | Movimiento permanente | descartar (decorativo, coste GPU, ajeno al lenguaje B2B) |

---

## 24 · 21st.dev — https://21st.dev/

- **Estado:** OK. El navegador ya tenía una sesión iniciada de antes; no se usó para ninguna acción.
- **Páginas visitadas:** `/` (Top today, New & noteworthy, índice de categorías), `/community/components/s/stat`, `/community/components/s/empty-state`, `/@dhxwhy/components/product-rail-gallery`.
- **Viewports:** escritorio 1440. Móvil no aplicado.
- **Descripción:** marketplace oscuro de componentes. Rails horizontales con ranking numerado, un índice de categorías con conteos (Stats & KPIs 153, Empty States 77, Tables 313…) y páginas de componente con demo viva.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Coste perf. | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B24-1 | /@dhxwhy/components/product-rail-gallery | Prendas colgadas de una barra con etiqueta de precio. Al hover giran, se deslizan por la barra y se levantan | Elegir el diámetro (DN) en una lista desplegable es abstracto | "Rack por DN": un tramo de tubería como barra con válvulas de la misma familia colgadas por tamaño (DN50…DN600) y etiqueta DN/PN. Al hover o foco la pieza sube 8 px y muestra la ficha corta. Fotos propias | frontend · Familia de producto > `SizeRail` | 4 | M | Medio (imágenes; usar lazy y `sizes`) | Botones reales por tamaño y alternativa en tabla. Sin física en reduced motion | adaptar |
| B24-2 | /community/components/s/stat | Tiles KPI oscuros con % grande y mini barra de progreso. Variante con "10B+" y métricas secundarias | Los KPI de admin no muestran avance contra la meta | Tarjeta KPI con valor (IBM Plex Mono), delta y barra de 2 px contra la meta mensual | admin · Dashboard > `KpiCard` | 4 | S | Nulo | La barra lleva `role="meter"` con valores. El delta usa ícono + signo, no solo color | aprovechar |
| B24-3 | /community/components/s/empty-state | Estados vacíos con ícono, título, una línea y 1–2 acciones ("No Notifications" + Refresh; "Access denied" + Back / Request access; 404 con dos acciones) | En admin y stock aparecen tablas vacías o errores de permiso sin salida | Componente `EmptyState` con variantes: sin datos (acción "Registrar"), sin permiso ("Volver" + "Solicitar acceso") y error de red ("Reintentar") | admin + stock · `EmptyState` | 4 | S | Nulo | Título como heading. El foco va a la acción principal cuando se reemplaza contenido | aprovechar |
| B24-4 | / (índice de categorías) | Índice de categorías agrupado (Marketing blocks, UI components, Data and feedback…) con conteo por categoría | El catálogo no dice cuánto hay en cada línea | Índice del catálogo agrupado por línea con conteo de productos ("Válvulas · 48") | frontend · Catálogo > `CategoryIndex` | 3 | S | Nulo | Lista semántica; el conteo se lee junto al nombre | aprovechar |
| B24-5 | / (Top today) | Rail "Top today" con numerales gigantes 1–10 detrás de cada tarjeta | Faltan señales de qué piden otros clientes | Rail "Más cotizados este mes" con numerales en navy al 10 % | frontend · Home > `TopQuotedRail` | 2 | S | Bajo | Numeral decorativo `aria-hidden`; orden en una lista ordenada | adaptar (solo si hay datos reales de cotizaciones) |

---

## 25 · Dribbble — https://dribbble.com/

- **Estado:** OK, búsqueda pública sin login. Se cerró el modal de promoción, sin aceptar nada.
- **Páginas visitadas:** `/search/dashboard-inventory`, `/search/industrial-website`, `/search/admin-panel` (con zoom a shots concretos).
- **Viewports:** escritorio 1440. Móvil no aplicado.
- **Descripción:** grillas de shots. Los de inventario coinciden en el patrón "valor total + barra de salud de stock + tabla con píldoras de estado". Los industriales usan foto de planta con overlay cálido, eyebrow con punto y cifras dentro del hero.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Coste perf. | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B25-1 | /search/dashboard-inventory (shot "Fixoria sales") | "Total Asset Value" junto a una barra segmentada de salud de stock (in stock / low stock / out of stock con conteos) sobre la tabla | En stock y admin no se ve de un vistazo cuántos ítems están en riesgo | `StockHealthBar`: barra segmentada OK / Bajo / Agotado con conteos clicables que filtran la tabla. En stock: #0e0f11 / ámbar / #d7261e | stock · Inventario; admin · Productos | 5 | S | Nulo | Cada segmento es un botón con texto ("Bajo: 355"). Patrón además de color | aprovechar |
| B25-2 | idem | Tabla de inventario con SKU, categoría, entrante, stock, precio, píldora de estado y menú de acciones. Toolbar con Import, Export, "+ Add Product", rango de fechas y filtros | La tabla de productos de admin no separa entrante de disponible | Agregar columnas "Entrante" (OC abiertas) y "Disponible", píldora de estado y toolbar con rango de fechas | admin · Productos > `InventoryTable` | 4 | M | Bajo (paginación del servidor) | `<table>` real, encabezados con `scope`, `aria-sort` | adaptar |
| B25-3 | idem (shot "Quantara") | Heatmap calendario de movimientos por semana/mes, panel de historial y mapa de ruta | No hay vista temporal de cuándo se entregan más EPP | Heatmap semanal de entregas por categoría (12 semanas) con escala Slab monocroma | stock · Reportes > `DeliveryHeatmap` | 3 | M | Bajo (SVG) | Tabla equivalente y tooltip con teclado | adaptar |
| B25-4 | idem (shot "Invendor") | Tarjetas KPI con chip de delta y frase "Compared to $111,000 last month" | El delta sin referencia absoluta engaña | Debajo del KPI, la línea "vs S/ 111 000 el mes anterior" en texto secundario | admin · Dashboard > `KpiCard` | 3 | S | Nulo | Texto legible por lector de pantalla | aprovechar |
| B25-5 | /search/industrial-website (shot "Precision in every process") | Foto de planta con overlay cálido, eyebrow "Built to perform" con punto naranja, titular y dos CTA (sólido + ghost) | El hero del frontend puede ganar jerarquía sin cambiar la foto | Eyebrow con punto #f26a1b ("Fundición dúctil · Perú") sobre el titular del hero actual. Se mantienen el carrusel y los CTA | frontend · Hero > `Eyebrow` | 3 | S | Nulo | Contraste del texto sobre foto ≥ 4.5:1 con overlay | aprovechar |
| B25-6 | idem (shot "ELIOS logistics") | Cifras en cajas con borde fino dentro del hero (98 %, 24/7) | La prueba de confianza está lejos del primer pliegue | 2–3 "proof chips" dentro del hero (años, normas ISO/NTP, despacho nacional) con borde 1 px blanco al 30 % | frontend · Hero > `ProofStats` | 4 | S | Nulo | Texto real, no imagen | aprovechar |
| B25-7 | /search/admin-panel (shot "Rebates List") | Lista densa con píldoras de estado, acción primaria naranja "+ Add…", rango de fechas en el header y paginación numerada con la página actual en naranja | Encaja casi tal cual con el admin "industrial ledger" | Paginación numerada con página actual en #f26a1b y acción primaria naranja en la cabecera de cada tabla | admin · `TableHeader` / `Pagination` | 3 | S | Nulo | `aria-current="page"`. Revisar el contraste del naranja con texto blanco | aprovechar |

---

## 26 · Awwwards — https://www.awwwards.com/

- **Estado:** OK. El banner de cookies solo ofrecía "GOT IT" y no se pulsó.
- **Páginas visitadas:** `/` (Site of the Day del 10/11/2026), `/websites/industrial/` (filtros y nominados), `/sites/the-industry-5-0-index` (detalle).
- **Viewports:** escritorio 1440. Móvil no aplicado.
- **Descripción:** portada con un titular enorme en mayúsculas y una fila de meta (Site of the Day, fecha, score). El listado tiene una barra de filtros con badge de conteo y Reset. El detalle usa una pill nav flotante inferior (Info, Elements, Votes, Visit Site destacado) y muestra la gráfica de líneas onduladas de "Industry 5.0 Index".

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Coste perf. | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B26-1 | /sites/the-industry-5-0-index | Pill nav flotante inferior: logo, 3 secciones y una acción final destacada en color | La bottom nav de stock reparte el mismo peso entre navegar y "Entregar EPP" | Bottom nav flotante redondeada con 3–4 destinos y la acción "Entregar" destacada en #d7261e. Respeta `env(safe-area-inset-bottom)` | stock · `BottomNav` | 4 | S | Nulo | Objetivos ≥ 44 px, `aria-current`, etiqueta visible en cada ítem | adaptar |
| B26-2 | /websites/industrial/ | Barra de filtros (Awards, Category, Tag, Technology, Country, Font, Color), badge con número de filtros activos y "Reset filters" | En el catálogo no se ve cuántos filtros hay aplicados ni cómo limpiarlos | Barra de filtros del catálogo (Línea, DN, PN, Norma, Material) con badge de activos y "Limpiar filtros" | frontend · Catálogo > `FilterBar` | 4 | M | Bajo | Estado anunciado con `aria-live="polite"` ("12 productos") | aprovechar |
| B26-3 | /sites/the-industry-5-0-index | Cinta de cientos de líneas onduladas en degradé de azul a naranja | Las secciones oscuras del frontend son planas | Fondo SVG estático de líneas de contorno ("flujo de agua") de navy a naranja con opacidad baja. Deriva opcional de 20 s | frontend · Sectores > fondo de sección | 3 | M | Bajo si es SVG estático; evitar canvas | Decorativo `aria-hidden`. Deriva desactivada con reduced motion | adaptar |
| B26-4 | / | Fila de meta: etiqueta "Site of the Day", chip de fecha y score | La ficha técnica no muestra vigencia ni norma de un vistazo | Fila de meta en la ficha: "Norma ISO 2531 · PN16 · Ficha actualizada 10/2026" con chips | frontend · ProductDetail > `MetaRow` | 2 | S | Nulo | Texto plano | adaptar |
| B26-5 | / y listado | Banner de cookies con un solo botón "GOT IT" | Antipatrón: no da opción de rechazar | No copiar. Si el frontend usa banner, debe tener "Rechazar" con el mismo peso que "Aceptar" | frontend · CookieBanner | 2 | S | Nulo | — | descartar (antipatrón) |

---

## 27 · Behance — https://www.behance.net/

- **Estado:** OK, galería pública sin login.
- **Páginas visitadas:** `/search/projects/industrial%20web%20design` y el proyecto "Industrial Website Design for a Manufacturing Company" (`/gallery/256406953/…`), recorrido con scroll por introducción, alcance, etapas y página de servicios.
- **Viewports:** escritorio 1440. Móvil no aplicado.
- **Descripción:** caso de estudio de una web de manufactura de precisión (marca ficticia del autor). Etiquetas de sección con un ícono de mira y una tabla clave/valor con filetes finos (Year, Industry, Scope). Las filas de servicios combinan foto de máquina y mini tabla de especificaciones (Tolerance, Envelope, Materials, Lead time), y el proceso se muestra en un timeline vertical de 5 etapas.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Coste perf. | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B27-1 | proyecto · "Services page" | Fila partida: foto a la izquierda y, a la derecha, chip de categoría, titular, una línea y una mini tabla de 4 specs (Tolerance, Envelope, Materials, Lead time) | Las familias de producto muestran foto y nombre, pero el comprador técnico busca DN, PN, material y plazo | `FamilyRow`: foto propia + chip ("Válvulas de compuerta") + titular + specs: Rango DN, PN, Material/recubrimiento, Norma, Plazo de entrega. Filas que alternan claro y navy | frontend · Catálogo/Home > `FamilyRow` | 5 | S | Bajo | Specs como `<dl>`. Contraste AA en la variante navy | aprovechar |
| B27-2 | proyecto · "Introduction" | Lista clave/valor con filetes de 1 px (Year / Industry / Scope of work) alineada a la derecha | Las fichas técnicas se ven como párrafos | Lista de especificaciones con filetes en la ficha de producto, y el mismo patrón en el panel de detalle de admin | frontend · ProductDetail; admin · `DetailPanel` | 3 | S | Nulo | `<dl>` semántico | aprovechar |
| B27-3 | proyecto · "Scope of work" | Timeline vertical de etapas con nodos y conector ("Stage 4 · UI design", "Stage 5 · Development") | No se explica el proceso de compra técnica | "Cómo trabajamos": Cotización → Ingeniería → Fabricación → Pruebas hidrostáticas → Despacho, con la línea dibujándose al hacer scroll (ver B21-2) | frontend · Nosotros/Home > `ProcessTimeline` | 4 | S | Muy bajo | Lista ordenada `<ol>`. La animación de la línea es opcional | aprovechar |
| B27-4 | proyecto · etiquetas de sección | Etiqueta pequeña con ícono de mira antes de cada bloque ("Introduction", "Scope of work", "Services page") | Las secciones largas no tienen marcadores | Eyebrows de sección con un glifo propio (por ejemplo, la sección de una brida) en navy | frontend · `SectionLabel` | 2 | S | Nulo | Glifo `aria-hidden` | adaptar |
| B27-5 | /search/projects/… | Chips de búsquedas relacionadas en la parte superior (b2b website, corporate website, construction…) | Cuando una búsqueda del catálogo da pocos resultados, el usuario no sabe cómo seguir | Chips de "búsquedas relacionadas" debajo del buscador del catálogo ("acople reparación", "tee HDPE") | frontend · Catálogo > `RelatedQueries` | 2 | S | Nulo | Enlaces reales | adaptar |

---

## 28 · Prompt Motion — https://prompt-motion.com/ (marcador del dueño, revisión en profundidad)

- **Estado:** OK, público. Se cerró el modal de suscripción sin introducir email. `/templates/3d` devuelve 404: la URL fue adivinada y el enlace real no se resolvió.
- **Páginas visitadas (12):** `/` (galería y filtros), `/?tag=charts`, `/?tag=diagrams`, `/?tag=phone`, `/twoclipping-5cba86` (Shape morphing through UI states), `/twoclipping-d89be5` (Landing page 3D scroll), `/lexnlin-f9b3bd8` (TasteSkill dashboard, tipo Skill), `/viktoroddy-98c1d8` (MotionSites one million visitors), `/linearuncle-5d2bae` (Derivative explainer, Manim), `/chatgptastra-0d95c7` (Motion principles showreel), `/kloss-xyz-fe0c31` (History of AI timeline), `/dale-vaz-cc612a` (Sahi trading terminal reveal), `/templates`, `/templates/showreel`.
- **Viewports:** escritorio 1440. Móvil no aplicado.
- **Descripción:** galería curada de videos de motion hechos con Claude, con el prompt o skill de cada uno. Filtros Prompt/Skill, chips de categoría con conteo (Product UI 105, Phone 22, Charts 34, Diagrams 31, Kinetic type 98, Shapes 43, Particles 43…), orden "Popular" y un botón global **"Pause previews"**. Cada ficha muestra el video, las etiquetas, el prompt con "Customize"/"Copy" y metadatos (modelo, stack, iteraciones, fecha). Los prompts más elaborados tienen bloques `<direction>`, `<structure>`, `<build>` y `<gotchas>` con reglas de timing explícitas.
- **Patrones de motion y timing observados:**
  - "Springs everywhere, a tiny overshoot at most"; bouncy easing prohibido.
  - Lista de prohibidos: particle bursts, glows, lens flares, camera shake, RGB split, crossfades, degradados genéricos, holds de más de 0.5 s.
  - Grilla de ritmo a 120 BPM (un beat = 500 ms) donde "something happens on every beat".
  - Una sola forma que se transforma entre estados de UI (button → loader → check → island → player → slider → toggle → tabs → chart → ⌘K → toast → button), con el contenido intercambiado mediante un blur corto y entrada/salida con tiempos propios.
  - Indicador de tabs con dos bordes en springs distintos: el borde delantero se estira antes que el trasero.
  - Drags de manipulación directa que al soltarse vuelven con spring desde donde estaban.
  - Revelado de titular palabra a palabra: cada palabra sube 16 px desde un blur de 12 px en 0.34 s, con stagger de 0.05–0.06 s.
  - Piezas que "despegan" con sombra proporcional a la altura: offset (0.10z, 4+0.36z), blur 7+0.5z, opacidad 26 %, color #1a2133.
  - Gotchas: no usar `will-change` en lo que la cámara escala porque el texto queda borroso; el último frame debe ser igual al primero para que el loop no tartamudee; revisar un frame por beat antes del render final.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Coste perf. | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B28-1 | /twoclipping-5cba86 | Una sola forma que se transforma: botón → loader → check → toast, sin cortes, cambiando tamaño, radio y color | Al enviar la cotización hoy hay un spinner genérico y luego un aviso separado, y se pierde la continuidad | Botón "Solicitar cotización" #f26a1b que se convierte en loader circular (radio 999, 48 px), luego en check y luego en una pill "Enviado · te contactamos en 24 h". Con `layout` de framer-motion y spring sin rebote (bounce ≤ 0.1, ~350 ms) | frontend · Formulario de cotización > `SubmitMorphButton` | 5 | M | Muy bajo | `aria-live="polite"` anuncia "Enviando…" y "Enviado". El botón conserva el foco. Con reduced motion los estados cambian sin morph | aprovechar |
| B28-2 | /twoclipping-5cba86 y /templates/showreel | Reglas explícitas: springs con overshoot mínimo; prohibidos bouncy, glows, particle bursts, camera shake, crossfades y holds > 0.5 s | Sin guía, cada app acumula efectos distintos | Guía de motion FUNDIGSAC con lista de "permitido / prohibido" y tokens: `spring.ui` (bounce 0.1, 350 ms), `ease.exit` (ease-in 160 ms), `dur.micro` 120 ms, `dur.base` 240 ms, `dur.section` 600 ms. En admin, equivalentes CSS | transversal · `motion-tokens` + guía | 5 | S | Nulo | Reduced motion definido en un solo lugar | aprovechar |
| B28-3 | /twoclipping-5cba86 (`<build>` 3) | Indicador de tabs con dos bordes en springs distintos: el borde delantero se estira antes que el trasero | Las tabs de admin y el control segmentado de stock saltan sin transición | Indicador con `left` y `right` animados por separado. Admin en CSS: `transition: left 180ms, right 260ms` según la dirección. Stock: dos `useSpring` | admin · `Tabs`; stock · `Segmented` | 3 | S | Muy bajo | Patrón tabs de ARIA. El indicador es decorativo | aprovechar |
| B28-4 | /twoclipping-5cba86 (`<gotchas>`) | El contenido que se intercambia dentro de un contenedor en transformación sale con un blur corto y tiene su propio tiempo de entrada y salida para no solaparse | Al cambiar de periodo o actualizar cantidades, los números se superponen o parpadean | Cambio de valor en KPI y en cantidades de stock: sale con `opacity` 0 + `blur(4px)` en 100 ms y entra en 140 ms con 40 ms de desfase (`AnimatePresence mode="popLayout"`) | admin · `KpiCard`; stock · `QtyDisplay` | 3 | S | Bajo (blur corto y en área pequeña) | El valor final se anuncia una sola vez | aprovechar |
| B28-5 | /twoclipping-5cba86 (`<build>` 4) | Drag de manipulación directa: mientras se sostiene, el valor sigue al cursor; al soltar vuelve con spring desde donde estaba | En campo, ajustar la cantidad de EPP con +/− es lento | Selector de cantidad arrastrable (slider horizontal) en "Entregar EPP" con `drag="x"` y spring al soltar, más botones +/− | stock · Entrega > `QtyScrubber` | 3 | M | Bajo | Siempre con alternativa de botones e input numérico. `role="slider"` con flechas | adaptar |
| B28-6 | /twoclipping-d89be5 (`<structure>` 10.12–10.36 s) | Título que entra palabra por palabra: cada palabra sube 16 px desde un blur de 12 px en 0.34 s, con 0.05–0.06 s entre palabras | El titular del hero aparece de golpe y compite con el carrusel | Titular del hero con revelado por palabra (y 16 → 0, blur 8 → 0 px, 340 ms, stagger 50 ms) solo en la primera carga, sin retrasar el LCP: el texto se pinta visible y la animación se aplica por encima | frontend · Hero > `HeadlineReveal` | 4 | S | Bajo. Cuidado con el LCP: no usar `opacity: 0` inicial en SSR | Texto completo en el DOM. Con reduced motion no se anima | adaptar |
| B28-7 | /twoclipping-d89be5 (`<build>` 5) | Sombras de piezas elevadas como función de la altura z: offset (0.10z, 4+0.36z), blur 7+0.5z, 26 %, color #1a2133 | Las sombras de stock (Slab) y las del frontend no siguen una escala | Escala de elevación derivada de la fórmula para z = 4, 8, 16, 24 (e1–e4), con color de sombra navy en frontend y #0e0f11 en stock. Hover de tarjeta = subir un nivel | stock · `Card`; frontend · `FamilyCard` | 4 | S | Bajo (box-shadow estático; animar `transform`, no la sombra) | Sin impacto | aprovechar |
| B28-8 | /templates/showreel (`<structure>`) | Coreografía sobre grilla de 120 BPM: algo ocurre en cada beat, holds ≤ 0.5 s y el último frame coincide con el primero para el loop | Las transiciones del carrusel de válvulas tienen tiempos arbitrarios y el loop "salta" | Cronometrar el carrusel del hero en una grilla de 250 ms: salida de imagen 250 ms, entrada 500 ms, caption +250 ms, intervalo 6 s. El estado final es igual al inicial | frontend · Hero > `ValveCarousel` | 3 | S | Nulo | Pausa obligatoria (ver B28-9). Sin autoplay con reduced motion | adaptar |
| B28-9 | / (galería) | Botón global "Pause previews" que congela todos los videos de la galería | El carrusel del hero y los videos se mueven sin control del usuario (WCAG 2.2.2) | Botón visible "Pausar animación" en el hero del frontend que detiene carrusel y videos y se recuerda en `localStorage`. En reduced motion arranca pausado | frontend · Hero > `MotionPauseToggle` | 5 | S | Nulo | Cumple WCAG 2.2.2 (pausar, detener, ocultar). `aria-pressed` | aprovechar |
| B28-10 | /twoclipping-5cba86 (`<gotchas>`) y /templates/showreel (`<build>` 5) | Gotchas: no usar `will-change` en lo que se escala porque el texto queda borroso; revisar un frame por beat antes del render final | Animaciones que se ven bien en dev y mal en producción, sin pruebas | Checklist de motion en PR: sin `will-change` permanente; capturas Playwright en t = 0, mitad y final de cada animación clave (morph de cotizar, carrusel) comparadas con baseline | transversal · QA/Playwright | 3 | S | Nulo | Incluir una corrida con `reducedMotion: 'reduce'` | aprovechar |

Descartadas de forma explícita en este sitio: la fly-over WebGL2 con profundidad de campo por píxel (`/twoclipping-d89be5`), las partículas de los showreels y la cámara que hace zoom entre escalas (`/dale-vaz-cc612a`). Las tres tienen coste alto y van en contra de la guía B28-2.

---

## 29 · Cult UI — https://www.cult-ui.com/

- **Estado:** OK, público.
- **Páginas visitadas:** `/`, `/docs/components/shift-card`, `/docs/components/kanban-board`, `/docs/components/expandable`.
- **Viewports:** escritorio 1440. Móvil no aplicado.
- **Descripción:** extensión de shadcn/ui con 154 componentes animados. La documentación es oscura, con preview/código, "Updated" con fecha y badges "new/updated/recent" en el sidebar. Componentes de app como Kanban con columnas, conteos, tags, avatares y fechas.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Coste perf. | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B29-1 | /docs/components/kanban-board | Kanban con columnas Backlog / In flight / Launched, conteo por columna, tags de color, avatar y fecha. Drag-and-drop con animación de layout | El staff sigue las cotizaciones en una tabla y no ve el embudo | Vista Kanban opcional de cotizaciones: Nueva / En evaluación / Enviada / Ganada / Perdida, con conteo y monto por columna. Al cambiar de estado, transición CSS de altura | admin · Cotizaciones > `QuoteBoard` | 4 | L | Medio (virtualizar columnas largas) | Mover también por menú "Cambiar estado" con teclado. Anunciar el movimiento | adaptar |
| B29-2 | /docs/components/expandable | Tarjeta compacta con badge rojo de urgencia ("In 15 mins") y hora, que se expande para mostrar el detalle | En stock las tarjetas de EPP por vencer muestran todo o nada | Tarjeta de entrega o EPP con badge "Vence en 7 d" en #d7261e que se expande (layout spring) con trabajador, talla y firma | stock · `ExpiringCard` | 3 | M | Bajo | `button` con `aria-expanded` y foco gestionado | adaptar |
| B29-3 | /docs/components/shift-card | Tarjeta que al hover o foco desplaza el header para mostrar más contenido, pensada para grillas de producto | La grilla de productos esconde datos técnicos | Al hover o foco sobre la tarjeta de producto, la imagen sube 24 px y aparecen 2 specs (DN, PN). En táctil se muestran siempre | frontend · Catálogo > `ProductCard` | 3 | S | Muy bajo | Disparar también con `:focus-within`. No ocultar información esencial | adaptar |
| B29-4 | /docs/* (sidebar) | Badges "new" / "updated" / "recent" en cada entrada del sidebar y "Updated Oct 1, 2026" en cada página | En admin no se ve qué secciones tienen novedades | Badge numérico de pendientes en el sidebar de 9 secciones (Cotizaciones 3, Mensajes 2) | admin · `Sidebar` | 2 | S | Nulo | El badge se incluye en el nombre accesible ("Cotizaciones, 3 pendientes") | adaptar |
| B29-5 | / (Landing Pages) | Heroes "Dithering", "Liquid Metal", "Heatmap" y fondos de textura | Ninguno | — | — | 1 | M | Alto | Movimiento continuo | descartar (ajeno al hero fotográfico) |

---

## 30 · GradientDeck UI — https://ui.gradientdeck.com/

- **Estado:** OK, público y sin cuenta.
- **Páginas visitadas:** `/`, búsqueda "industrial" (0 resultados, estado vacío), búsqueda "engineering", `/styles/teenage-engineering` (DESIGN.md).
- **Viewports:** escritorio 1440. Móvil no aplicado; se probó resize y la ventana no bajó del ancho de escritorio.
- **Descripción:** biblioteca de 1295 archivos DESIGN.md sacados de webs reales. Cada ficha resume el estilo en una frase y documenta los colores con nombre, hex, rol y frecuencia de uso, más un probador de contraste entre pares (AA, AA large, AAA). Filtros All/Light/Dark/Mixed con conteos.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Coste perf. | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B30-1 | /styles/teenage-engineering | DESIGN.md por sitio: tagline del estilo, colores con nombre y rol ("texto principal, filetes…"), tipografía y forma | Los rediseños se pierden al restaurar: hubo tres restauraciones (frontend 04/11, admin 20/10, stock 30/10) | Un `DESIGN.md` por app (frontend, admin, stock) que fije tokens, roles, tipografías, radios, sombras (B28-7) y reglas de motion (B28-2), para que personas y agentes no se desvíen | transversal · `docs/DESIGN.md` × 3 | 5 | S | Nulo | Incluye los pares de contraste aprobados | aprovechar |
| B30-2 | /styles/teenage-engineering ("Try a pairing") | Probador de pares fondo/texto con ratio y resultado AA / AA large / AAA | El naranja #f26a1b con texto blanco ronda 3:1, así que solo sirve para texto grande o negrita ≥ 18.66 px. Hay que medirlo | Test automático (Vitest) que calcula el contraste de los pares declarados en DESIGN.md y falla bajo 4.5:1 (o 3:1 si el par está marcado como "large") | transversal · test de tokens | 4 | S | Nulo | Evita regresiones de contraste | aprovechar |
| B30-3 | / (búsqueda "industrial") | Estado vacío "Nothing matches" con sugerencia y dos acciones: "Clear the search" y "Request a site" | Si un producto no aparece en el catálogo, se pierde el lead | Sin resultados en el catálogo: "No encontramos «…»" + "Limpiar búsqueda" + "Pedir cotización de este producto", que abre el formulario con la consulta ya escrita | frontend · Catálogo > `SearchEmpty` | 5 | S | Nulo | Foco al título del estado vacío y conteo anunciado en `aria-live` | aprovechar |
| B30-4 | / (resultados) | Segmentado All / Light / Dark / Mixed con conteos junto al buscador | Duplica B26-2 | Fusionar con B26-2: segmentado por línea con conteo junto al buscador | frontend · Catálogo | 2 | S | Nulo | `radiogroup` | adaptar (fusionar con B26-2) |
| B30-5 | /styles/teenage-engineering | Principio de estilo: "el producto es el único objeto rico de la página y todo lo demás susurra" (UI neutra, filetes, foto de estudio) | Las fichas compiten entre decoración y producto | Regla para la ficha de producto del frontend: fondo neutro, foto de válvula sobre fondo continuo y UI en filetes. Un solo acento naranja por vista (el CTA) | frontend · ProductDetail (regla de diseño) | 3 | S | Nulo | Menos ruido visual | aprovechar |
| B30-6 | / (hero) | Muro inclinado de capturas en perspectiva | Ninguno | — | — | 1 | M | Medio-alto (muchas imágenes) | — | descartar (no hay material equivalente y pesa) |

---

## Resumen de estado

| # | Sitio | Estado | Ideas |
|---|---|---|---|
| 21 | animejs.com | OK | 6 |
| 22 | mobbin.com | Parcial (login para la biblioteca) | 5 |
| 23 | reactbits.dev | OK | 5 (1 descartada) |
| 24 | 21st.dev | OK | 5 |
| 25 | dribbble.com | OK (búsqueda pública) | 7 |
| 26 | awwwards.com | OK | 5 (1 descartada) |
| 27 | behance.net | OK (galería pública) | 5 |
| 28 | prompt-motion.com | OK (12 páginas) | 10 |
| 29 | cult-ui.com | OK | 5 (1 descartada) |
| 30 | ui.gradientdeck.com | OK | 6 (1 descartada, 1 fusionada) |

**Total: 59 ideas.** Las capturas a 390 px no se obtuvieron en ningún sitio por la limitación de ventana compartida.
