# Inspiración: marcadores 11–20

Auditoría del 2026-11-10. Las ideas parten de lo que se vio en cada sitio y se adaptan a los diseños restaurados de FUNDIGSAC, sin reemplazarlos:

- **frontend**: hero fotográfico con carrusel de válvulas, CTA naranja #f26a1b y navy.
- **admin**: estilo "industrial ledger", con sidebar de 9 secciones, KPIs, tablas densas e IBM Plex.
- **stock**: Fraunces + Archivo, paleta Slab #f1f2f4/#0e0f11/#d7261e, tarjetas con sombra y bottom nav móvil.

**Método.** Las capturas de escritorio se tomaron con Claude in Chrome a 1568×773 px de ventana efectiva. La ventana compartida no aceptó el redimensionado, así que las de teléfono se tomaron en el navegador integrado con emulación de 390×844. En cada sitio se probaron hover, clics y filtros. No se inició sesión, no se enviaron formularios y no se descargaron archivos.

**Leyenda.** Impacto de 0 a 5. Esfuerzo S/M/L. "Perf" indica el coste de rendimiento estimado.

**Contrastes calculados (WCAG).**

| Color | Sobre blanco | Sobre #0e0f11 |
|---|---|---|
| #f26a1b | 3,06:1 | 6,26:1 |
| #BF5720 | 4,57:1 | 4,20:1 |
| #d7261e | 5,02:1 | 3,82:1 |

---

## 11. Superdesign — https://superdesign.dev/

- **Estado:** OK. El generador y la opción "Use prompt" piden login; no se usaron.
- **Páginas visitadas:** `/` (inicio con galería), `/library?selected=…&category=style` (vista maestro-detalle), `/library?selected=warm-industrial-gray-style`, `/design-systems` (biblioteca design.md) y `/design-systems/railway` (detalle de tokens).
- **Viewports:** escritorio y 390×844. En móvil, los chips de categoría se desplazan en horizontal y las tarjetas forman una grilla de 2 columnas.
- **Descripción:** generador de UI con IA y biblioteca de prompts de estilo. También reúne sistemas de diseño en formato DESIGN.md, con vista previa de los tokens.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Imp. | Esf. | Perf | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B11-1 | /design-systems/railway | Cada token de color muestra nombre, hex y una frase sobre su rol, por ejemplo "fondo de página" o "divisores finos". Los tokens se agrupan en Surfaces y Text, junto a un panel de colores y tipografía. | Las tres apps tienen paletas restauradas, pero no existe un documento que explique qué color se usa en cada caso. Eso favorece regresiones de diseño. | Crear un `DESIGN.md` por app con tokens, rol en una línea, tipografías, espaciado y contraste medido. Añadir una página interna `/admin/estilo` que lo renderice como muestrario vivo. | Transversal: `DESIGN.md` de frontend, admin y stock | 4 | S | Ninguno (documentación) | Incluir el ratio de contraste de cada par texto/fondo | Aprovechar: bajo coste y protege las restauraciones |
| B11-2 | /library | Lista izquierda con miniatura, título, contador y tags. A la derecha, una vista previa grande con selector Mobile/Tablet/Desktop. | En admin, quien edita una ficha de producto no ve cómo quedará en la web pública. | Al editar un producto en admin, dividir la pantalla: formulario a la izquierda y un iframe con la ficha pública a la derecha. El iframe tendría conmutador móvil/escritorio (390/1280 px). | admin: Productos, editor de ficha | 4 | M | Iframe con carga diferida | El conmutador debe ser `role="radiogroup"` con etiquetas | Adaptar |
| B11-3 | / (galería) | Al pasar el cursor por una tarjeta aparecen los botones "Use prompt" y copiar sobre la miniatura. | Las tarjetas de producto obligan a entrar a la ficha para cotizar. | Al pasar el cursor por una tarjeta del catálogo, mostrar "Cotizar" (naranja) y "Ficha PDF". En táctil, los botones quedan siempre visibles bajo la imagen. | frontend: tarjeta de producto del catálogo | 3 | S | CSS puro | Los botones también deben aparecer con `:focus-within`, no solo con hover | Adaptar |
| B11-4 | / (móvil) | Fila de chips (New, Style, Animation…) con desplazamiento horizontal y el chip activo relleno. | En móvil, los filtros por familia ocupan mucho alto. | Fila de chips con `overflow-x:auto` y `scroll-snap`: Válvulas, Accesorios HDPE, Acoples, Tubería. El chip activo va en navy relleno. | frontend: catálogo móvil · stock: filtro por categoría de EPP | 4 | S | Ninguno | Usar `aria-pressed` y dejar ver parte del chip siguiente como pista de desplazamiento | Aprovechar |
| B11-5 | /library?selected=warm-industrial-gray-style | Estilo "Warm Industrial": etiquetas monoespaciadas pequeñas ("SYSTEM 01"), numeración editorial y un titular gigante con texto en contorno. | Las secciones largas de la home no marcan bien el ritmo entre ellas. | Añadir eyebrows numerados en monoespaciada ("01 / Agua potable", "02 / Saneamiento") encima de cada H2 de sector. Se descarta el texto en contorno porque se lee mal sobre foto. | frontend: encabezados de sección de la home | 3 | S | Ninguno, o una fuente mono ya cargada | Esconder la numeración del lector de pantalla (`aria-hidden`) | Adaptar (solo los eyebrows) |
| B11-6 | /design-systems | Fila de 4 indicadores (164 Systems, 1572 Colors…) y, al pie de la grilla, "Showing 24 of 164 · Load more". | La paginación numerada del catálogo no informa cuánto falta por ver. | Mostrar "Mostrando 24 de 132 productos" con un botón "Cargar más" y mantener `?page=` en la URL para SEO. | frontend: catálogo · admin: listados largos | 3 | S | Menos peso inicial | Anunciar el nuevo total con `aria-live="polite"` | Aprovechar |

---

## 12. Uiverse — https://uiverse.io/

- **Estado:** OK. Los elementos son de la comunidad y cada uno lleva **licencia MIT**, visible en la página de detalle. "Create" y "Save to favorites" piden cuenta; no se usaron.
- **Páginas visitadas:** `/`, `/loaders`, `/cards`, `/radio-buttons`, `/tooltips`, el detalle `/Deri-Kurniawan/hot-bullfrog-96` y `/toggle-switches`, que da 404 y sirvió para ver su página de error.
- **Viewports:** escritorio y 390×844. En móvil, el hero queda apilado con un buscador ancho y dos CTA a todo el ancho.
- **Descripción:** biblioteca abierta de componentes en HTML/CSS y Tailwind, con filtros por tag, tecnología, orden y tema.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Imp. | Esf. | Perf | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B12-1 | /Deri-Kurniawan/hot-bullfrog-96 | Skeleton loader con un círculo y dos barras que usan `animate-pulse` (MIT, 6 líneas de código). | Las listas de stock y las tablas de admin se ven vacías o saltan mientras responde Supabase. | Tarjeta esqueleto con la misma altura y sombra que la tarjeta real de EPP en stock, y filas esqueleto en las tablas de admin. Usar `#e3e5e8` sobre la superficie `#f1f2f4`. | stock: lista de EPP y entregas · admin: tablas | 4 | S | CSS puro y menos CLS | `aria-busy="true"` en el contenedor; `prefers-reduced-motion` desactiva el pulso | Aprovechar (MIT) |
| B12-2 | /radio-buttons | Radios en forma de tarjeta con icono y texto (Bicycle, Motorbike, Car); la elegida lleva borde de acento. | Elegir el tipo de movimiento o el sector con un `<select>` en móvil es lento. | En stock, tarjetas-radio grandes para el tipo de movimiento (Entrega, Devolución, Ajuste). En el formulario de cotización del frontend, para el sector (Agua, Saneamiento, Agricultura, Minería), cada una con icono. | stock: formulario de movimiento · frontend: formulario de cotización | 4 | S | CSS puro | `<input type=radio>` nativo, área táctil mínima de 44 px y foco visible | Adaptar |
| B12-3 | /radio-buttons | Control segmentado de 3 opciones (Yes/No/Idk y Silver/Gold/Platinum) con la opción activa resaltada. | Los filtros de estado y de período usan selects o enlaces sueltos. | Control segmentado para Todos/Activos/Borrador en las tablas de admin y para Hoy/Semana/Mes en el resumen de stock. | admin: barra de tabla · stock: resumen | 3 | S | CSS puro | `fieldset` y `legend`, navegable con flechas | Aprovechar |
| B12-4 | /cards | Tarjeta "Commits" en línea de tiempo vertical: icono en la línea, título, autor, fecha, texto y "Show more". | No hay una vista clara del historial de una cotización ni de los movimientos de un EPP. | Línea de tiempo vertical en el detalle de cotización de admin (creada, enviada, aprobada) y en el detalle de EPP de stock (entregas y devoluciones). Usar fechas en Plex Mono. | admin: detalle de cotización · stock: detalle de EPP | 4 | M | Ninguno | Lista ordenada `<ol>` con `<time datetime>` | Adaptar |
| B12-5 | /toggle-switches (404) | La página 404 conserva el sidebar de navegación y muestra icono, "404", "Not Found" y un enlace de vuelta. | Un 404 aislado hace que se pierda al visitante que llega desde un enlace roto de catálogo. | El 404 del frontend conserva header y footer y añade un buscador de productos y accesos a las 4 familias, además de WhatsApp de ventas. | frontend: página 404 | 3 | S | Ninguno | H1 claro y foco inicial en el buscador | Adaptar |
| B12-6 | /loaders | La barra de herramientas reúne en una sola fila los tags rápidos, el toggle Tailwind/CSS, "Sort", "Any Theme" y una búsqueda inline. | Las tablas de admin reparten los filtros en varias filas. | Una sola barra sobre cada tabla con búsqueda, chips de filtro, orden y densidad, alineada a la derecha y con altura fija de 40 px. | admin: cabecera de tablas | 3 | S | Ninguno | Cada control con etiqueta visible o `aria-label` | Adaptar |
| B12-7 | /tooltips | Varios tooltips de hover sobre botones y chips (por ejemplo, "Project Structure" con icono). | En las tablas densas de admin y en las fichas aparecen siglas técnicas (DN, PN, SDR) sin explicación. | Tooltip corto para las siglas técnicas en las cabeceras de tabla y en las fichas ("PN16: presión nominal de 16 bar"). | admin: cabeceras · frontend: tabla de especificaciones | 3 | S | CSS más JS mínimo | Debe abrirse también con foco, cerrarse con Esc y usar `aria-describedby` | Aprovechar |

Se descartan los loaders 3D, neón o con mascotas (el hámster, por ejemplo) porque no encajan con el tono industrial.

---

## 13. CSSFX — https://cssfx.netlify.app/

- **Estado:** OK. Es de código abierto con **licencia MIT**, según la propia portada.
- **Páginas visitadas:** la portada de una sola página con sus secciones Buttons, Inputs, Loaders y Text. Se pasó el cursor sobre los efectos Bubble, Slide, Highlight y Underline y se abrió el modal de código de "Underline".
- **Viewports:** escritorio y 390×844. En móvil, la grilla pasa a 2 columnas.
- **Descripción:** efectos CSS de copiar y pegar, con un marcado mínimo.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Imp. | Esf. | Perf | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B13-1 | / (Text, "Underline") | Subrayado con `::before` de 2 px que pasa de `scaleX(0)` a `scaleX(1)` con `transform-origin` de derecha a izquierda, en 0,5 s. Se vio en el modal de código. | La navegación del header no da respuesta al pasar el cursor más allá del cambio de color. | Subrayado naranja animado en los enlaces del header y del footer, en 0,25 s. El ítem activo lleva el subrayado fijo. | frontend: header y footer | 3 | S | Solo `transform` | Con `prefers-reduced-motion` no hay transición; el estado activo usa `aria-current` | Aprovechar (MIT) |
| B13-2 | / (Text, "Highlight") | Al pasar el cursor, un fondo de color rellena el texto por detrás. | Los enlaces dentro de párrafos largos (políticas, fichas) se distinguen poco. | Enlaces en párrafos con un subrayado permanente y un realce suave al pasar el cursor (naranja-100 de la escala B18). | frontend: texto corrido | 2 | S | CSS puro | Mantener el subrayado siempre, no solo en hover | Adaptar |
| B13-3 | / (Inputs: Outline, Trace, Underline) | Campos con borde que se dibuja ("Trace") o línea inferior que crece al recibir foco. | Los formularios de cotización y de stock tienen un foco poco visible. | Al recibir foco, el borde se traza en navy en el frontend y en tinta #0e0f11 en stock, junto a un anillo de foco estático de 2 px. | frontend: formularios de cotización y contacto · stock: formularios | 3 | S | CSS puro | El anillo estático es obligatorio; la animación es solo un adorno | Adaptar |
| B13-4 | / (Loaders) | Spinners mínimos de puntos y anillos, sin imágenes. | Al pulsar "Registrar entrega" el usuario no sabe si se está guardando y puede tocar dos veces. | Spinner de 3 puntos dentro del botón mientras se envía, con el botón deshabilitado y el texto "Guardando…". | stock: botones de envío · admin: guardar | 3 | S | CSS puro | `aria-live` con el estado; el spinner va con `aria-hidden` | Aprovechar |
| B13-5 | / (Buttons, "Slide") | Botón cuyo fondo se desliza a otro color al pasar el cursor; se vio el cambio a magenta. | Con texto blanco, el CTA #f26a1b da 3,06:1, que no cumple AA para texto normal. | Hover del CTA que desliza el fondo a naranja-900 #BF5720 (4,57:1 con blanco). Ver también B18-1. | frontend: botones CTA "Cotizar" | 3 | S | Solo `transform` en un pseudo-elemento | Mejora el contraste en hover | Adaptar |
| B13-6 | / (modal de código) | Modal con bloques HTML y CSS, cada uno con su botón "COPY". | Copiar en admin el código de producto o el número de cotización se hace a mano y genera errores. | Botón copiar junto a SKU, N.º de cotización y RUC en admin, con el mensaje "Copiado" durante 1,5 s. | admin: detalle de producto y de cotización | 3 | S | Ninguno | Botón con `aria-label` y anuncio del resultado con `aria-live` | Adaptar |

Se descartan Bubble y Jelly porque son demasiado juguetones para un fabricante B2B.

---

## 14. SVGL — https://svgl.app/

- **Estado:** OK. El sitio avisa de que los logos pertenecen a sus marcas y que hace falta permiso para usarlos, así que no se propone copiar ninguno.
- **Páginas visitadas:** `/`, `/?search=whatsapp`, `/directory/payment` y `/api`.
- **Viewports:** escritorio y 390×844. En móvil, las tarjetas quedan en 1 columna con su fila de acciones y las categorías pasan a un menú hamburguesa; algunos logos no cargaron a tiempo.
- **Descripción:** buscador de logos SVG con categorías, favoritos, una API pública y tema claro u oscuro.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Imp. | Esf. | Perf | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B14-1 | / | Cada tarjeta lleva icono, nombre, chip de categoría y una fila de 4 acciones (copiar, descargar, enlace, guía de marca). Un indicador marca si hay variante clara u oscura. | Las fichas técnicas PDF y las imágenes de producto están dispersas en admin. | En la biblioteca de medios de admin, tarjeta por archivo con tipo (PDF, JPG), producto vinculado y acciones (copiar enlace público, abrir, reemplazar). | admin: medios y fichas técnicas | 3 | S | Ninguno | Botones de icono con `aria-label` y tooltip | Adaptar |
| B14-2 | / (sidebar) | El sidebar lista categorías con un contador a la derecha (AI 73, Database 24…). | El catálogo no indica cuántos productos hay en cada familia antes de entrar. | Sidebar o filtro de familias con contador (Válvulas 48, HDPE 36…) en el catálogo de escritorio; en móvil se usan los chips de B11-4. | frontend: catálogo · admin: filtro de productos | 4 | S | El contador viene de la consulta | Incluir el contador en el nombre accesible ("Válvulas, 48 productos") | Aprovechar |
| B14-3 | / y /?search=whatsapp | Búsqueda fija arriba con la pista `⌘K` y el término guardado en la URL (`?search=`). | Encontrar un producto o una cotización en admin exige pasar por varias secciones. | Búsqueda global en admin con `Ctrl+K` (productos, cotizaciones, clientes). En el frontend, `?q=` en la URL para compartir resultados por WhatsApp. | admin: topbar · frontend: buscador del catálogo | 4 | M | Consulta con debounce de 250 ms | `role="combobox"` con `aria-activedescendant` y atajo documentado | Aprovechar |
| B14-4 | /?search=whatsapp | El logo de WhatsApp está en el catálogo, pero el banner insiste en el permiso de marca. | El botón flotante de WhatsApp del frontend debe usar el logo oficial. | Usar el recurso oficial de WhatsApp siguiendo su guía de marca, no una copia de un tercero, y servirlo como SVG inline optimizado. | frontend: botón flotante de WhatsApp | 2 | S | SVG inline de menos de 1 KB | `aria-label="Escribir a ventas por WhatsApp"` | Adaptar (solo fuente oficial) |
| B14-5 | / (header) | Conmutador de tema claro/oscuro en el header. | Ningún requisito de FUNDIGSAC pide modo oscuro. | No implementar por ahora: duplicaría el QA visual de las tres apps restauradas. | admin | 1 | M | — | — | Descartar: sin demanda y alto coste de QA |

---

## 15. Component Party — https://component-party.dev/

- **Estado:** OK.
- **Páginas visitadas:** `/`, `/?f=react-svelte5-vue3` (al activar Vue 3) y `#component-composition` (salto desde el índice). Se probó el botón Play, que abrió el playground de Svelte en una pestaña nueva; se cerró sin usarlo.
- **Viewports:** escritorio y 390×844. En móvil, la barra de frameworks se desplaza en horizontal y los paneles de código quedan en 1 columna con scroll horizontal propio.
- **Descripción:** comparador lado a lado de la misma tarea en distintos frameworks, con un índice lateral fijo.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Imp. | Esf. | Perf | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B15-1 | /?f=react-svelte5-vue3 | Chips para elegir qué columnas comparar; la selección queda en la URL (`?f=`) y la vista se reordena sola. | El cliente B2B duda entre modelos parecidos (compuerta o mariposa, PN10 o PN16) y ventas compara a mano. | Comparador de 2 a 3 productos con la selección en `?comparar=sku1,sku2` para compartirla. Las filas de especificaciones van alineadas y se resaltan las diferencias. | frontend: comparador del catálogo | 4 | M | Datos ya disponibles | Tabla con `<th scope>` real, no divs | Adaptar |
| B15-2 | /#component-composition | Cada tarjeta de código tiene pestañas de archivo (App.jsx, UserProfile.jsx). | La ficha de producto muestra todas las especificaciones en una sola lista larga. | Pestañas dentro de la tarjeta de especificaciones: Dimensiones, Materiales, Normas y Presiones. | frontend: ficha de producto | 4 | S | Ninguno | Patrón ARIA tabs con flechas; sin JS, se ve todo apilado | Adaptar |
| B15-3 | / (sidebar) | Índice lateral fijo con secciones agrupadas (Reactivity, Templating…) que resalta la sección visible. | Las fichas largas y la página de Configuración de admin obligan a desplazarse sin orientación. | Índice fijo con scrollspy (IntersectionObserver) en la ficha técnica larga del frontend y en Configuración de admin. | frontend: ficha técnica · admin: Configuración | 4 | S | IntersectionObserver, barato | Usar `aria-current="true"` en la sección activa | Aprovechar |
| B15-4 | / (títulos con "#") | Cada H2 y H3 tiene un ancla "#" para enlazarlo directamente. | Ventas no puede mandar por WhatsApp un enlace directo a "Presiones de trabajo". | Anclas en los H2 de la ficha; el "#" aparece al pasar el cursor o con foco y copia el enlace. | frontend: ficha de producto | 3 | S | Ninguno | El ancla con texto oculto "Enlace a esta sección" | Aprovechar |
| B15-5 | / (móvil) | Los bloques de código largos se desplazan en horizontal dentro de su tarjeta, sin romper la página. | En móvil, las tablas densas de admin desbordan toda la página. | Contenedor con `overflow-x:auto` propio, primera columna fija (sticky) y sombra lateral que indica que hay más contenido. | admin: tablas en móvil · frontend: tabla de especificaciones | 3 | S | CSS puro | Contenedor enfocable (`tabindex=0`) con `aria-label` | Adaptar |

---

## 16. Google Fonts — Material Symbols — https://fonts.google.com/icons

- **Estado:** OK. Los iconos llevan **licencia Apache 2.0**, indicada en la tarjeta de la portada. No se descargó ningún SVG ni PNG.
- **Páginas visitadas:** `/icons`, `?icon.query=valve`, `?icon.query=helmet` y el panel de detalle del icono "Valve", donde se movieron los ejes de grosor y relleno (wght 700, FILL 1).
- **Viewports:** escritorio y 390×844. En móvil aparece una bottom nav de 5 ítems con una píldora tras el icono activo y los filtros se reducen a un botón "Filters".
- **Descripción:** catálogo de iconos con fuente variable (FILL, wght, GRAD, opsz), búsqueda por sinónimos y fragmentos de código.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Imp. | Esf. | Perf | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B16-1 | ?icon.query=valve / helmet | Existen iconos `valve`, `plumbing`, `faucet`, `fire_hydrant` y `engineering` (casco). El fragmento de código permite cargar solo esos iconos con `icon_names`. | Faltan iconos coherentes para los sectores y los EPP. | Un set mínimo de 10 a 15 iconos exportados a SVG inline (sprite), o la fuente subconjunto con `icon_names`, para los sectores del frontend y las categorías de stock. | Transversal: iconos de sector y categoría | 4 | S | Subconjunto pequeño; el sprite SVG no bloquea | Iconos decorativos con `aria-hidden` y siempre con texto al lado | Aprovechar (Apache 2.0) |
| B16-2 | panel "Valve" | Activar Fill cambia el icono de contorno a relleno en tiempo real (eje FILL 0 a 1). | En la bottom nav de stock, la pestaña activa se distingue sobre todo por el color. | Pestaña activa con icono relleno (FILL 1) e inactivas en contorno, con transición de `font-variation-settings` de 150 ms. | stock: bottom nav | 3 | S | Ninguno si ya hay fuente variable | Así el estado no depende solo del color; añadir `aria-current="page"` | Aprovechar |
| B16-3 | /icons (Customize) | Deslizadores de Weight (100–700), Grade (-25 a 200) y Optical size (20–48 px). | Los iconos actuales no acompañan el grosor de cada tipografía. | Ajustar los ejes por app: admin con wght 300 (Plex fino), stock con wght 500–600 (Archivo) y GRAD -25 sobre el navy del hero del frontend para que no se vean gruesos. | Transversal: tokens de icono | 3 | S | Ninguno | Mantener al menos 20 px en táctil | Adaptar |
| B16-4 | /icons (móvil) | Bottom nav con la etiqueta siempre visible y una píldora redondeada de color tras el icono activo. | La bottom nav de stock comunica poco cuál es la pestaña activa. | Píldora de 56×32 px tras el icono activo con rojo Slab al 12 % y el icono en #0e0f11. La etiqueta siempre visible en Archivo 12 px. | stock: bottom nav | 4 | S | CSS puro | Destino táctil de 48 px; con la etiqueta, no depende del color | Adaptar |
| B16-5 | panel "Valve" | Panel lateral con vista previa grande, tags, selector de tamaño y color, botones de exportación y pestañas Web/Android/Apple. | Para ver el detalle de un producto en admin hay que cambiar de página y se pierde la lista. | Panel lateral derecho (drawer) al hacer clic en una fila de producto: imagen, tags, stock y precio, con pestañas Datos/Medios/Historial. | admin: tabla de productos | 3 | M | Carga diferida del contenido | Gestión de foco del diálogo y cierre con Esc | Adaptar |
| B16-6 | ?icon.query=valve | Buscar "valve" encuentra Plumbing, Faucet y Fire Hydrant gracias a sus tags (controller, faucet, pipe, water…). | El buscador no encuentra "gate valve", "compuerta" ni "válvula de cuña" si no aparece el nombre exacto. | Campo `sinonimos[]` por producto (en ES y EN, nombres comerciales y normas) usado por el buscador del frontend y de admin. | frontend: buscador · admin: productos | 4 | M | Índice local o de Supabase | Mostrar "Resultados para…" con el término equivalente | Adaptar |

---

## 17. CSS Grid Generator — https://cssgridgenerator.io/

- **Estado:** OK.
- **Páginas visitadas:** la herramienta de una sola página. Se arrastró el ítem 1 hasta ocupar 3×3 celdas, se añadió el ítem 2 y se revisó el HTML y CSS generados.
- **Viewports:** escritorio y 390×844. En móvil el editor queda muy abajo y la grilla no se adapta.
- **Descripción:** generador visual de `grid-template` con arrastrar y redimensionar.
- **Por qué hay menos de 5 ideas:** es una herramienta de un solo propósito y sus patrones de interfaz no aportan más casos útiles.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Imp. | Esf. | Perf | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B17-1 | / | Al arrastrar el asa, un ítem pasa a ocupar 3 columnas y 3 filas y genera una distribución tipo bento con `grid-area`. | El panel de KPIs de admin es una fila uniforme y no jerarquiza qué importa más. | Bento de 4 columnas: gráfico de ventas en 2×2, KPIs en 1×1 y alertas de stock bajo en 1×2. La herramienta sirve solo para maquetar; el código final es CSS propio. | admin: Dashboard | 4 | S | CSS puro | El orden del DOM sigue el orden de lectura, no el visual | Adaptar |
| B17-2 | / | La misma composición asimétrica con un bloque grande y varios pequeños. | La sección de sectores de la home tiene tarjetas iguales. | Bento de sectores: Agua potable grande con foto y Saneamiento, Agricultura y Minería en tarjetas menores con CTA naranja. | frontend: sección Sectores | 3 | S | Fotos con `loading=lazy` y tamaños fijos | Texto sobre foto con velo ≥ 4,5:1 | Adaptar |
| B17-3 | / (salida de código) | El código usa `.div1`, `.div2` y `repeat(5,1fr)` en filas fijas, sin breakpoints; en móvil no se adapta. | Si se copia tal cual, rompe el diseño móvil y queda sin nombres claros. | Reescribir la grilla con `grid-template-areas` con nombre (kpi, chart, alerts) y una columna única por debajo de 768 px. | Transversal: grillas | 3 | S | Ninguno | — | Aprovechar como pauta técnica |

---

## 18. Kigen Color — https://kigen.design/color

- **Estado:** OK. El plugin de Figma y la licencia Pro no se usaron.
- **Páginas visitadas:** `/color`, donde se introdujo #f26a1b, se probaron los algoritmos Tailwind y Radix UI y la salida en OKLCH, y la portada `/`.
- **Viewports:** escritorio y 390×844. En móvil los controles se recogen en una píldora flotante "Controls" al pie.
- **Descripción:** generador de escalas de color con varios algoritmos y exportación a CSS, Tailwind, Tailwind 4 y tokens, en HEX, RGBA, HSL u OKLCH.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Imp. | Esf. | Perf | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B18-1 | /color (Radix, #f26a1b) | Con el algoritmo Radix, #f26a1b queda exacto en el paso 800; el 900 es #BF5720 y el 950 #7D2100. | El texto blanco sobre #f26a1b da 3,06:1 (no cumple AA para texto normal) y los enlaces naranjas sobre blanco tampoco. | Mantener #f26a1b como fondo de CTA con texto de al menos 18,66 px en negrita (AA para texto grande). Usar #BF5720 (4,57:1) para enlaces, hover y texto naranja sobre blanco. | frontend: CTA, enlaces y precios destacados | 5 | S | Ninguno | Corrige un fallo de contraste en toda la marca | Aprovechar |
| B18-2 | /color (pestaña CSS, OKLCH) | Exporta `:root{--orange-50…950}` en OKLCH; también ofrece Tailwind 4 y tokens. | Los tonos derivados del naranja y del navy se eligen a ojo en cada componente. | Archivo `tokens.css` por app con las escalas `--fd-orange-50…950` y `--fd-navy-*` en OKLCH con respaldo en HEX, documentado en B11-1. | Transversal: tokens | 4 | S | Unos pocos cientos de bytes | — | Aprovechar |
| B18-3 | /color | La misma lógica aplicada a cualquier color base. | Stock usa #d7261e, que con blanco da 5,02:1, pero sobre #0e0f11 solo 3,82:1. | Escala del rojo Slab: tonos 50/100 para el fondo de alertas de "stock bajo" y el rojo base solo para texto sobre claro. Nunca rojo como texto sobre tinta. | stock: alertas, chips de estado y badges | 4 | S | Ninguno | El estado se indica también con icono y texto, no solo con color | Aprovechar |
| B18-4 | /color (móvil) | Los controles se recogen en una píldora flotante "Controls" que abre un panel. | En móvil, los filtros de stock ocupan la mitad de la pantalla. | Botón flotante "Filtros (n)" sobre la bottom nav que abre una hoja inferior con los filtros. | stock: listados | 3 | M | JS mínimo | Diálogo modal con foco atrapado y cierre con Esc | Adaptar |
| B18-5 | /color | Selectores de patrón de nombres (50…900) y de número de tonos (11). | Los nombres de color cambian de una app a otra. | Capa semántica sobre la escala: `--accent`, `--accent-hover`, `--accent-subtle`, `--danger-subtle`, con los mismos nombres en las 3 apps aunque cambie el valor. | Transversal: tokens | 3 | S | Ninguno | — | Adaptar |

---

## 19. Good Design Tools — https://www.gooddesign.tools/category/best-figma-plugins

- **Estado:** **BLOQUEADO / caído.** Chrome mostró una página de error tanto con la URL pedida como con la raíz. El navegador integrado rechazó la navegación. `curl` falló en el handshake TLS: `SEC_E_ILLEGAL_MESSAGE (0x80090326)`. El DNS sí resuelve (198.202.211.1).
- **Páginas visitadas:** ninguna se pudo cargar.
- **Viewports:** no aplica.
- **Ideas:** 0. Conviene reintentar más adelante o buscar el contenido en una copia archivada.

---

## 20. MotionSites — https://motionsites.ai/

- **Estado:** OK en la parte pública. Los prompts son de pago ("Go Unlimited") y su código no se puede copiar ni se propone copiarlo.
- **Páginas visitadas:** `/` con hover sobre tarjetas, `/?prompt=zenith-realty-landing` (detalle expandido), el filtro Dashboards y `/dashboards`, que da 404 porque la sección es un filtro.
- **Viewports:** escritorio y 390×844. En móvil, el hero queda apilado, hay chips más un botón de filtro y una grilla de 2 columnas.
- **Descripción:** galería de prompts para landings y paneles con mucho movimiento y vistas previas en vídeo.

| ID | Página | Observado | Problema FUNDIGSAC | Propuesta adaptada | App / componente | Imp. | Esf. | Perf | Accesibilidad | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| B20-1 | / (filtro Dashboard, "Robot Jellyfish") | Producto técnico en el centro rodeado de paneles de datos (valores, barras, etiquetas) con acento naranja, como una ficha técnica tipo HUD. | La ficha de válvula muestra la foto y los datos por separado y no transmite ingeniería. | Foto de la válvula al centro con 4 a 6 indicaciones SVG unidas por líneas finas a sus partes (DN, PN16, hierro dúctil, recubrimiento epoxi, junta EPDM) en Plex Mono y naranja. En móvil pasan a ser una lista numerada bajo la foto. | frontend: cabecera de la ficha de producto | 5 | M | SVG inline sin JS | Los datos van también en una lista accesible; el SVG es decorativo | Adaptar |
| B20-2 | / (tarjetas) | Al pasar el cursor, la vista previa de la tarjeta reproduce un vídeo. También hay un contador de likes. | La galería de obras y proyectos es estática. | Solo en escritorio y en la galería de obras: clip corto en hover con `preload="none"` y póster. Nada en el catálogo ni en móvil. | frontend: galería de proyectos | 2 | M | Alto: vídeo, limitado por `preload` | Sin autoplay con sonido; respetar `prefers-reduced-motion` | Adaptar con límites |
| B20-3 | /?prompt=zenith-realty-landing | La tarjeta se abre dentro de la grilla como un panel de 2 columnas, con vista previa desplazable, metadatos y CTA. El resto de tarjetas sigue alrededor y la URL guarda el ítem. | Abrir cada ficha hace perder la posición en el catálogo. | Vista rápida dentro del catálogo con imagen, 5 especificaciones clave y botones "Cotizar" y "Ver ficha", usando `?p=sku` para enlazarla. | frontend: catálogo | 4 | M | Carga del detalle bajo demanda | Al abrir, el foco pasa al panel; al cerrar, vuelve a la tarjeta | Adaptar |
| B20-4 | / (tarjeta "Acreage Farming") | Sección oscura de agricultura de precisión con 4 cifras grandes (500K+, 99,8 %, 50+, 15+) junto a una foto de cultivo. | La página del sector Agricultura no muestra cifras de respaldo. | Bloque navy con 3 a 4 cifras reales de FUNDIGSAC (años, proyectos, hectáreas regadas, diámetros disponibles) en números tabulares junto a una foto de riego. | frontend: página del sector Agricultura | 3 | S | Ninguno | Solo cifras verificadas; texto blanco sobre navy | Adaptar |
| B20-5 | / (barra de filtros) | Chips de categoría con flecha para desplazar, "Clear all" visible cuando hay un filtro activo y un desplegable "Pricing" aparte. En móvil, los chips van con un botón de filtro. | Al combinar filtros en el catálogo no hay forma rápida de quitarlos todos. | Mostrar "Limpiar filtros" en cuanto haya uno activo, junto a los chips de B11-4, y un desplegable aparte para "Norma" o "Presión". | frontend: catálogo | 3 | S | Ninguno | Anunciar el nuevo total de resultados | Aprovechar |
| B20-6 | / (Forecast Center, Fitness, Finance) | Mini sparklines en una franja horaria, KPIs con barritas de tendencia y un medidor radial del 68 %. | Los KPIs de admin muestran el número sin tendencia y stock no muestra el nivel respecto al mínimo. | En admin, KPIs con una sparkline SVG de las últimas 12 semanas. En stock, un medidor radial pequeño del stock actual frente al mínimo por EPP. | admin: KPIs del Dashboard · stock: tarjeta de EPP | 4 | M | SVG inline sin librería | Valor en texto junto al gráfico; el gráfico va con `aria-hidden` | Adaptar |
| B20-7 | / (banner superior) | Banner de precio por paridad adaptado al país del visitante (Perú). | — | No aplica: FUNDIGSAC no vende online con precios por país. | — | 0 | — | — | — | Descartar |

---

## Resumen por sitio

| # | Sitio | Estado | Ideas |
|---|---|---|---|
| 11 | superdesign.dev | OK (generador con login, no usado) | 6 |
| 12 | uiverse.io | OK (MIT) | 7 |
| 13 | cssfx.netlify.app | OK (MIT) | 6 |
| 14 | svgl.app | OK (logos con permiso de marca) | 5 (1 descartada) |
| 15 | component-party.dev | OK | 5 |
| 16 | fonts.google.com/icons | OK (Apache 2.0) | 6 |
| 17 | cssgridgenerator.io | OK | 3 (herramienta de un solo propósito) |
| 18 | kigen.design/color | OK | 5 |
| 19 | gooddesign.tools | Bloqueado (fallo TLS) | 0 |
| 20 | motionsites.ai | OK (prompts de pago, no copiados) | 7 (1 descartada) |
