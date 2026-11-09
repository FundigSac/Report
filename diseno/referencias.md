# Bibliotecas de componentes animados

Revisión del 2026-11-09 en Chrome, con ventana de 1568×773 px.

Alcance y límites de esta revisión:

- Se revisaron la portada y las páginas principales de cada sitio, con desplazamiento y lectura de texto.
- Los tamaños son estimaciones hechas sobre capturas. No se inspeccionó el CSS.
- El movimiento se dedujo comparando capturas sucesivas. Las duraciones describen la sensación observada y no son valores medidos.
- No se probaron estados hover, salvo el efecto que quedó activo bajo la posición del cursor.
- Algunos componentes solo se vieron por su nombre en el catálogo. Se indica en cada caso.
- Se extraen principios. No se copió código ni recursos gráficos.

## Criterio de adopción: KPI en verde

Requisito del responsable del proyecto: cada corrección se mide contra todos los KPI y debe quedar en verde antes de darse por terminada. Esto incluye la incorporación de cualquier patrón de este documento.

Los objetivos son los de la sección 22 de `Report/README.md`:

| Indicador | Objetivo |
|---|---:|
| LCP | ≤2,5 s |
| INP | ≤200 ms |
| CLS | ≤0,1 |
| Lighthouse Performance | ≥90 |
| Lighthouse Accessibility | ≥95, con revisión manual |
| Lighthouse SEO | ≥95 |
| Carga inicial móvil de portada | ~1,5 MB o menos |
| JS comprimido inicial | ~150 KB o menos |

Medir en inicio, catálogo, ficha y contacto, en móvil y escritorio. Un patrón que deje un indicador fuera de objetivo se retira o se simplifica. Todo movimiento debe respetar `prefers-reduced-motion` y no puede retrasar la lectura del contenido principal.

Esta revisión no modificó código, por lo que no generó mediciones nuevas.

## magicui.design

**Layout.** Franja de anuncio a todo el ancho, navegación fija y hero centrado con pastilla de novedad, título en dos líneas, subtítulo en tres líneas y dos CTA de igual ancho (~295 px). Contenedor de ~1350 px. Le siguen un carrusel horizontal con bordes desvanecidos, testimonios en mampostería de cuatro columnas con corte desvanecido y botón "Show More", y un bloque de video asimétrico de proporción ~2:1. La documentación usa tres columnas: menú, contenido de ~710 px y riel derecho de índice.

**Escala tipográfica.** H1 de ~60 px, seminegrita, interletraje muy cerrado e interlineado ~1,1. H2 de ~44 px. H1 de documentación de ~32 px. Cuerpo de 16 a 18 px. Etiquetas de menú de 14 px.

**Color.** Blanco con tinta casi negra y grises para texto secundario. El color saturado se concentra en la franja superior, en halos muy tenues bajo los CTA y en insignias pequeñas (lima para "New", naranja para "Pro").

**Espaciado.** ~145 px entre secciones. Separación de 15 px entre tarjetas. Relleno interno de ~19 px. Radios de 12 a 16 px y bordes de 1 px de bajo contraste.

**Movimiento.**

- El carrusel avanza de forma continua, en el orden de 100 px/s según dos capturas. Es lineal y constante.
- El contador numérico sube una vez al mostrarse y se detiene en el valor final.
- En Animated Beam, un pulso recorre líneas curvas entre nodos fijos y conecta orígenes con un centro y destinos.
- En Border Beam, un segmento de luz recorre el borde de la tarjeta en bucle.

**Componentes a adaptar.**

- Contador numérico de una sola pasada, para años de operación, capacidad o toneladas.
- Bento Grid para capacidades técnicas, con iconos propios y sin efectos de fondo.
- Animated Beam reducido a un diagrama de proceso, de materia prima a inspección, en un solo color y sin bucle permanente.
- Marquee de logos de clientes con bordes desvanecidos y pausa al pasar el cursor. Si los clientes son pocos, usar una fila estática.
- Dotted Map para mostrar cobertura o exportación (visto solo por nombre).
- Grid Pattern o Noise Texture como textura de fondo muy baja (vistos solo por nombre).

**No conviene para una marca industrial B2B.** Halos multicolor, texto arcoíris o aurora, meteoros, confeti, destellos, texto de cómic, cursores personalizados, testimonios tomados de redes sociales y franja promocional permanente. Comunican producto de software para desarrolladores, no solidez de fabricante.

## smoothui.dev

**Layout.** Tema oscuro. La navegación en tres partes se contrae en una sola píldora flotante al desplazar. Hero centrado con dos CTA y una línea de comando. Le sigue una demostración enmarcada con pestañas, entre bandas de imagen con trama de semitono. Las rejillas son de tres columnas de ~360 px en un contenedor de ~1116 px. Las secciones de ventajas combinan una tarjeta grande con imagen a la izquierda y dos o tres menores a la derecha. La ficha de componente divide la pantalla: documentación a la izquierda y vista previa fija a la derecha.

**Escala tipográfica.** H1 de ~60 px con interlineado ~1,2. H2 de ~36 px. Cuerpo de 16 a 18 px. Monoespaciada para comandos. Microetiquetas en mayúsculas con interletraje amplio.

**Color.** Base casi negra, superficies gris muy oscuro y bordes de 1 px apenas visibles. Un único acento rosa, reservado para CTA, pestaña activa, indicador activo y logotipo. La disciplina de un solo acento es lo más aprovechable del sitio.

**Espaciado.** 170 a 200 px entre secciones. ~80 px del título a la rejilla. Relleno de ~22 px. Separación de 15 px entre tarjetas.

**Movimiento.**

- Difuminado progresivo en los bordes superior e inferior de la ventana: el contenido se desenfoca al pasar bajo la navegación.
- Contracción de la navegación al desplazar, rápida.
- Number Flow: los dígitos ruedan por separado en casillas.
- Scroll Reveal Paragraph: el párrafo pasa de atenuado a legible por palabras al entrar en pantalla.
- El sitio declara resortes y compatibilidad con movimiento reducido.

**Componentes a adaptar.**

- Ficha con dos paneles para producto: datos técnicos con desplazamiento a la izquierda e imagen fija a la derecha.
- Bloque de ventajas con una tarjeta dominante y fotografía real de planta.
- Microetiqueta en mayúsculas como encabezado de sección, por ejemplo "Procesos" o "Certificaciones".
- Revelado de párrafo una sola vez, por línea, en el texto institucional.
- Dígitos rodantes para indicadores que cambian.
- Trama de semitono sobre fotografía de planta, como recurso de marca. Dither Image, vista solo por nombre, es la referencia.
- Clip Corners Button y SVG Draw On Scroll (vistos solo por nombre). El corte de esquina evoca pieza mecanizada y el trazado sirve para planos técnicos.

**No conviene para una marca industrial B2B.** Acento rosa, transiciones con shaders, efectos gooey, metal líquido, lámina holográfica, orbes, control flotante de sonido y barra inferior fija. El difuminado con `backdrop-filter` en toda la ventana se debe descartar si afecta INP o fluidez en móvil.

## animate-ui.com

**Layout.** Fondo negro y contenedor de ~1060 px. Hero centrado con selector React/Vue, caja de comando con pestañas y dos CTA. La sección central se fija durante varias pantallas: un logotipo grande rodeado de tarjetas inclinadas que terminan ordenadas en una rejilla de 3×3. Cierra con un panel doble de conversación y resultado.

**Escala tipográfica.** Sans geométrica. H1 de ~52 px y H2 de ~44 a 56 px, en peso medio. Parte del título va en gris para jerarquizar sin añadir color. Etiquetas de 12 a 14 px. Cifras con ancho uniforme.

**Color.** Negro, blanco y grises, sin acento de marca. Botón primario blanco sólido y secundario gris oscuro. Bordes gruesos de ~3 px con muy poco contraste.

**Espaciado.** Separación de ~15 px en rejilla. Radios de ~16 px. Separaciones verticales muy amplias, superiores a 250 px.

**Movimiento.**

- El desplazamiento controla la rotación del logotipo y la trayectoria de las tarjetas en perspectiva, con avance suavizado que continúa un momento después de detener el desplazamiento.
- Demostraciones en bucle: interruptor, casillas que tachan el texto, toast apilado, progreso con dígitos rodantes. Cada estado dura pocos cientos de milisegundos y se percibe con resorte corto.

**Componentes a adaptar.**

- Microinteracciones de formulario construidas sobre primitivas accesibles (Radix, Base UI, React Aria): casilla, radio, acordeón y pestañas con indicador deslizante. Aplican al formulario de cotización y conservan foco y teclado.
- Toast de confirmación con estado claro.
- Altura automática al abrir acordeones de especificaciones, sin saltos de diseño.
- Zoom de imagen para fotografías de piezas (visto solo por nombre).
- Gris dentro del título para jerarquizar sin sumar colores.

**No conviene para una marca industrial B2B.** Secciones fijadas durante varias pantallas, que retrasan la llegada a la información; logotipo giratorio grande; tarjetas inclinadas en perspectiva; botón líquido, partículas, efecto magnético e inclinación 3D. Las demostraciones en bucle permanente distraen en una página de decisión de compra.

## 21st.dev (componentes de comunidad)

**Layout.** Aplicación con menú lateral fijo de ~220 px, con categorías y conteos, y barra superior. Filas por categoría con carrusel horizontal. Las páginas de categoría muestran cuatro columnas, con orden por recomendados, descargas, guardados o recientes. Celdas separadas por líneas finas y sin espacio entre ellas.

**Escala tipográfica.** Interfaz funcional de 14 px con títulos de fila de 16 px. Las miniaturas tienen escalas propias. Las de mayor impacto usan titulares muy grandes en mayúsculas sobre fotografía.

**Color.** Interfaz casi negra con azul reservado al CTA principal. Las miniaturas mezclan claro y oscuro. Las más sobrias usan monocromo con un solo acento.

**Espaciado.** Retícula de líneas finas sin separación, con 18 a 35 px de margen alrededor de cada miniatura.

**Movimiento.** En el catálogo se observó un brillo de tarjeta que responde al cursor. Las miniaturas se revisaron como imágenes fijas, por lo que no se evaluó el movimiento de cada componente.

**Patrones a adaptar del catálogo.**

- Hero con fotografía a sangre, capa oscura y titular grande en mayúsculas. Es el formato más cercano a una planta industrial.
- Rejilla de 3×2 con líneas finas: icono, título corto y una frase. Sirve para capacidades.
- Lista a la izquierda con panel de imagen a la derecha, para procesos o líneas de producto.
- Filas alternas con cifras (Alternating Rows With Stats, visto solo por nombre).
- Tabla comparativa de especificaciones o materiales.
- Cifra dominante con tres métricas secundarias en una fila, para la sección de indicadores.
- Línea de tiempo vertical con pasos numerados y estados, para el proceso de pedido.
- Líneas de contorno topográfico sobre fondo oscuro, como textura de carácter técnico.

**No conviene para una marca industrial B2B.** Vidrio líquido, escenas 3D embebidas, agujeros negros, shaders de portada, líneas de tiempo orbitales, botones de neón y cursores decorativos. Los componentes más populares del catálogo son los de desplazamiento espectacular, de modo que la popularidad no sirve como criterio. Las secciones de precios se sustituyen por solicitud de cotización.

## uiverse.io

**Layout.** Tema oscuro. Hero centrado con buscador protagonista y muro de elementos a todo el ancho. Trío de cifras con icono. Nube de etiquetas en panel redondeado. Cierre en bento con comunidad, Figma, repositorio y blog. La galería usa menú lateral de 12 categorías y rejilla de cuatro columnas, con barra de etiquetas, tecnología, orden, tema y búsqueda.

**Escala tipográfica.** H1 de ~60 px en peso ligero y sans geométrica. Cifras de ~56 px también en peso ligero. Cuerpo de 14 a 16 px.

**Color.** Casi negro con índigo y violeta como acento en CTA. Cada celda de galería tiene fondo neutro propio, gris claro o gris oscuro, para aislar el elemento.

**Espaciado.** ~12 px entre celdas de galería. ~200 px entre secciones de portada.

**Movimiento.** La galería muestra sobre todo CSS y estados de pequeña escala. Los cargadores corren en bucle y la nube de etiquetas tiene bordes desvanecidos. La calidad varía mucho entre autores.

**Componentes a adaptar.**

- Barra de filtros combinada para catálogo: etiquetas rápidas, orden y búsqueda.
- Celda de producto con fondo neutro uniforme, para que piezas de distintas fotos se vean como una serie.
- Toast de éxito o error con icono, título, descripción y cierre.
- Microestados resueltos solo con CSS, sin coste de JavaScript. Es el enfoque más favorable para los KPI.
- Trío de cifras con etiqueta breve.

**No conviene para una marca industrial B2B.** Neumorfismo, degradados llamativos, cargadores lúdicos, tarjetas decorativas e ilustraciones humorísticas. El código de comunidad no garantiza foco visible, semántica ni movimiento reducido, por lo que nada debe incorporarse sin revisión de accesibilidad.

## Síntesis para la marca

1. Usar un solo acento de color, reservado a acciones y estados.
2. Revelar contenido una sola vez, con transiciones cortas. Evitar bucles permanentes.
3. Animar cifras reales una vez, con dígitos de ancho uniforme.
4. Mostrar fotografía real de planta y producto. Usar líneas finas, retícula y texturas técnicas en lugar de brillos.
5. Aplicar movimiento donde explique algo: proceso, estado de formulario, apertura de especificaciones.
6. Preferir CSS y primitivas accesibles. Cargar bajo demanda cualquier efecto pesado.
7. No fijar secciones durante el desplazamiento ni bloquear el acceso al contenido.
8. Medir todos los KPI tras cada incorporación y mantenerlos en verde.

# Galerías de sistemas de diseño y generadores con IA

Revisión del 2026-11-09 en Chrome. Las capturas tienen un marco de 1568×773 px y el navegador informó una ventana real de 1707×842 px.

Alcance y límites de esta revisión:

- Se revisaron la portada de cada sitio y algunas páginas principales, con desplazamiento y lectura de texto.
- Los tamaños marcados con "~" son estimaciones sobre capturas, en el marco de 1568 px. Los valores reales en CSS serían cerca de un 9 % mayores. No se inspeccionó el CSS.
- Los valores indicados como "ficha publicada" provienen del texto de cada sitio. Son análisis de terceros y no especificaciones oficiales de las marcas citadas.
- El movimiento se dedujo comparando capturas separadas por alrededor de un segundo. No se midieron duraciones ni se probaron estados hover.
- No se pulsó ningún control que cambie estado, no se inició sesión y no se aceptaron cookies ni términos.
- Se extraen principios. No se copió código ni recursos gráficos.
- El criterio de la sección "Criterio de adopción: KPI en verde" se aplica también a estos patrones. Esta revisión no modificó código, por lo que no generó mediciones nuevas.

## styles.refero.design

Páginas vistas: portada y una ficha de estilo (Ramp).

**Layout.** Tema oscuro con cabecera mínima y ruta de migas. Hero centrado con pastilla de estado, título, subtítulo de tres líneas, buscador de ~690 px y ocho sugerencias en dos filas. Galería de tres columnas: tarjetas de ~440 px con separación de ~29 px y captura interior con ~45 px de margen. Debajo de cada tarjeta van logotipo, nombre y una frase descriptiva. La ficha se divide en dos paneles con desplazamiento independiente: a la izquierda vista previa, paleta, escala tipográfica, espaciado, radios y lista de hacer y evitar; a la derecha, panel fijo con el documento técnico y pestañas de formato.

**Escala tipográfica.** H1 con serifa de ~60 px, interletraje cerrado. Títulos de sección en la ficha de ~20 px. Nombre de tarjeta de ~18 px. Descriptor de 13 a 14 px. Etiquetas de sección de ~12 px en mayúsculas. Monoespaciada para valores y documento técnico.

**Color.** Casi negro azulado, superficies apenas más claras y un botón blanco como única acción fuerte. El color lo aportan las capturas. Cada muestra de la paleta se presenta con nombre, valor y función.

**Espaciado.** ~88 px entre filas de galería, incluido el pie de tarjeta. Radios exteriores de ~30 px.

**Movimiento.**

- Las miniaturas cambian entre capturas, lo que indica video o animación en bucle.
- El icono dentro del botón de conexión rota entre varios logotipos.
- No se apreció animación de entrada al desplazar.

**Referencia útil dentro del catálogo: Ramp (ficha publicada).** Un solo acento reservado a acciones y contadores, bordes de 1 px en lugar de sombras, un único peso tipográfico, alineación a la izquierda, escala de 64, 40, 28, 24, 20, 18 y 16 px, unidad base de 4 px, ancho máximo de 1200 px, 64 a 128 px entre secciones, 20 a 24 px de relleno en tarjetas y radios de 6 a 16 px.

**Componentes a adaptar.**

- Paleta documentada por función, con lista de hacer y evitar, para `Report/diseno`.
- Ficha de dos paneles para producto: imagen y explicación con desplazamiento, datos técnicos fijos.
- Tarjeta con imagen inserta sobre superficie neutra, para que fotografías distintas se lean como serie.
- Frase descriptiva de una línea bajo cada producto o proceso.

**No conviene para una marca industrial B2B.** Título con serifa sobre negro, miniaturas en video dentro de un catálogo, descriptores poéticos y clonar la identidad de una marca real, que es el uso que propone el sitio.

## getdesign.md

Páginas vistas: portada, catálogo y una ficha (IBM). El aviso de cookies quedó abierto y tapó la parte inferior de la ventana.

**Layout.** Tema oscuro con menú lateral fijo de ~227 px y barra superior. Hero partido por una línea vertical fina: a la izquierda título, dos CTA y fila de compatibilidad; a la derecha una lista numerada del 01 al 05 con vista previa asociada. La portada continúa con una lista densa de ~1200 px y filas de ~38 px: logotipo, nombre, descripción, insignia y dos columnas numéricas alineadas a la derecha. El catálogo usa pestañas con conteo y rejilla de cuatro columnas.

**Escala tipográfica.** H1 sans seminegrita de ~36 px. Título de ficha en monoespaciada de ~30 px. Filas de 13 a 14 px. Etiquetas en monoespaciada, mayúsculas e interletraje amplio. Cifras en monoespaciada.

**Color.** Casi negro con CTA ámbar. Rosa en el logotipo y en una palabra del título. El bloque de patrocinio lima rompe el sistema.

**Espaciado.** Filas compactas separadas por líneas finas. La densidad es alta y sigue siendo legible porque cada columna mantiene su alineación.

**Movimiento.** Muy reducido. Se observó solo un icono que cambia dentro de una frase, parcialmente oculto por el aviso de cookies. No se probó si la vista previa cambia con la lista numerada.

**Referencias útiles dentro del catálogo.** IBM es la más cercana: lienzo blanco, un solo azul, esquinas de 0 a 4 px, título de peso ligero de ~72 px y par de botones unidos, uno sólido y otro con contorno. Por su descripción, DJI (mosaicos de producto en estudio), HashiCorp y SpaceX merecen una segunda revisión. No se abrieron.

**Componentes a adaptar.**

- Lista densa con cifras alineadas a la derecha, para catálogo técnico, normas o documentos descargables.
- Lista numerada con panel asociado, para sectores o etapas del proceso.
- Hero dividido por una línea fina, con el mensaje a la izquierda y la evidencia a la derecha.
- Etiqueta monoespaciada en mayúsculas para códigos de pieza y encabezados técnicos.

**No conviene para una marca industrial B2B.** Franja promocional, bloque patrocinado, contador de estrellas, palabra rosa en el título, menú lateral en un sitio público y aviso de cookies de gran altura.

## designdotmd.directory

Páginas vistas: portada, Freight Logistics y Architect Blueprint.

**Layout.** Tema claro con rieles laterales de patrocinio de ~183 px y zona central de ~1058 px. Barra fija con filtros en píldoras de desplazamiento horizontal, buscador y comando. Bloque destacado 2:1, con una tarjeta grande y dos apiladas. Directorio de tres columnas con tarjetas de ~340 px y ~19 px de separación. Cada tarjeta muestra una miniatura de la página real y un pie con nombre y tres muestras de color. La ficha aplica el sistema a cuatro plantillas (muestrario, landing, comercio y evento) y presenta escritorio y móvil lado a lado.

**Escala tipográfica.** Títulos de ~38 px en sans. Interfaz de 13 a 14 px. Etiquetas monoespaciadas en mayúsculas, en terracota. Cada miniatura usa su propia escala.

**Color.** Blanco y gris muy claro, botón negro y terracota limitado a marca y etiquetas. Tres puntos de color bastan para resumir cada sistema.

**Espaciado.** Separación de ~20 px en rejilla, radios de ~18 px y relleno de ~16 px en el pie de tarjeta.

**Movimiento.** La barra de filtros es fija y desenfoca el contenido que pasa debajo. No se observaron otras animaciones.

**Referencias útiles dentro del catálogo (ficha publicada).**

- Freight Logistics: gris acero, casi negro y naranja de seguridad como único acento. Título condensado en negrita de 72 px, cuerpo sans de ~15 px, etiquetas monoespaciadas de ~11,5 px para referencias y plazos, radios de 2 a 6 px, sin degradados y una acción principal por pantalla.
- Architect Blueprint: azul de plano, radios de 0 a 2 px, etiquetas monoespaciadas con interletraje amplio. El título de aspecto decorativo no conviene, pero sí la disciplina de retícula y líneas.

**Componentes a adaptar.**

- Validar los tokens en varias plantillas, escritorio y móvil, antes de aplicarlos al sitio.
- Títulos condensados con cuerpo neutro y monoespaciada para datos de producto.
- Filtros fijos en píldoras para catálogo móvil, sin desenfoque si afecta INP.
- Resumen de tres muestras para acabados o materiales.

**No conviene para una marca industrial B2B.** Rieles de patrocinio, favoritos con corazón, galerías con páginas embebidas por su coste de carga y los estilos lúdicos o de videojuego.

## ui-skills.com

Página vista: portada. La ruta `/learn` devolvió 404. Las tarjetas de aprendizaje se leyeron en la portada.

**Layout.** Columna central de ~668 px dentro de un marco más ancho. Sin hero visual: título de dos líneas, dos tarjetas de acceso y lista de filas de ~65 px con imagen pequeña, nombre, autor y descripción truncada a una línea. Tira de logotipos, cuatro tarjetas de aprendizaje en 2×2 y pie de cinco columnas. Tarjeta de patrocinio flotante abajo a la derecha.

**Escala tipográfica.** H1 de ~34 px en peso medio. Filas de ~14 px. Texto secundario en gris. Rótulos de sección de ~13 px con flecha pequeña.

**Color.** Blanco, tinta casi negra y grises, sin acento. Un botón negro en la cabecera. El color lo aportan las imágenes de perfil.

**Espaciado.** Líneas finas entre filas, sin tarjetas. ~60 a 100 px entre secciones.

**Movimiento.** No se observó movimiento en carga ni al desplazar. El catálogo sí lista efectos pesados en Canvas y WebGL. Se vieron solo por nombre.

**Componentes a adaptar.**

- Cuatro reglas publicadas que afectan directamente a los KPI: `aspect-ratio` en imágenes para reservar espacio, `text-balance` en títulos y `text-pretty` en párrafos, `tabular-nums` en tablas, y objetivos táctiles de 44 px.
- Filas sin tarjeta para certificados, fichas técnicas y descargas.
- Página 404 mínima con dos salidas claras.
- Separar auditoría y ejecución, como proponen las herramientas `improve-*`: primero un plan priorizado y después el cambio medido.

**No conviene para una marca industrial B2B.** Portada solo de texto, tarjeta flotante permanente y tipografía cinética en Canvas o WebGL, por coste de JavaScript y por tono.

## superdesign.dev

Páginas vistas: portada y biblioteca, sin sesión.

**Layout.** Fondo negro y cabecera en tres partes. Hero centrado con caja de instrucción de ~662 px y atajos. Galería en mampostería de tres columnas, con pestañas de categoría y carga progresiva. La biblioteca divide la pantalla: lista de ~470 px con buscador, pestañas y etiquetas, y a la derecha una vista previa grande con selector móvil, tableta y escritorio.

**Escala tipográfica.** H1 de ~32 px, pequeño para un hero, porque la protagonista es la caja de instrucción. Títulos de galería de ~20 px. Títulos de tarjeta de ~14 px.

**Color.** Negro puro, botón blanco y píldoras gris oscuro. El color proviene de las miniaturas.

**Espaciado.** ~15 px entre tarjetas y ~10 px de marco interior.

**Movimiento.**

- La palabra central del título cambia y se desplaza verticalmente.
- La galería muestra indicador de carga y bloques grises que luego se rellenan.
- En la plantilla Portal Hero, el desplazamiento separa el logotipo en dos mitades y descubre una imagen a sangre. La secuencia se comprobó en dos capturas.

**Referencias útiles dentro del catálogo.** Mosaic Grid Architecture, con líneas divisorias, microetiquetas y fotografía técnica en gris. Una plantilla sobre piedra clara con volumen de hormigón. Otra con cabecera en retícula de líneas y titular negro con una sola palabra azul.

**Componentes a adaptar.**

- Lista con vista previa grande, útil para explorar familias de producto en escritorio.
- Selector de vista para planos o dimensiones de producto.
- Bloques de carga con altura reservada, siempre con espacio definido para evitar CLS.
- Retícula de líneas con microetiquetas, para portada y secciones de capacidades.

**No conviene para una marca industrial B2B.** Glassmorfismo, aurora, estética noir, manos rojas, ASCII, tipografía desenfocada y el portal controlado por desplazamiento, que retrasa el contenido y compromete LCP.

## v0.app

Páginas vistas: portada y plantillas, sin sesión.

**Layout.** Fondo negro y navegación alineada a la izquierda. Hero con caja de instrucción de ~633 px y atajos. Rejilla de plantillas de tres columnas, cortada con desvanecido y un botón "Browse all" centrado. Bento de nueve tarjetas iguales de ~362×377 px, cada una con título, frase e ilustración recortada en la parte inferior. Tira de logotipos. La página de plantillas añade categorías con mosaico de cuatro miniaturas y filas con carrusel.

**Escala tipográfica.** H1 seminegrita de ~32 px. Titular del bento de ~44 px con interletraje muy cerrado. Títulos de tarjeta de 18 a 20 px. Cuerpo de 15 a 16 px. Monoespaciada dentro de los diagramas.

**Color.** Negro, botón blanco y bordes de 1 px apenas visibles. El color aparece dentro de las ilustraciones.

**Espaciado.** ~15 px entre tarjetas y ~30 px de relleno interno.

**Movimiento.**

- La tira de logotipos avanza de forma continua.
- Las miniaturas de plantillas están vivas: una completa su titular y otra cambia una palabra.
- No se observaron entradas animadas en el bento.

**Componentes a adaptar.**

- Rejilla cortada con desvanecido y un botón para ver el catálogo completo.
- Tarjetas iguales con diagrama pequeño y etiquetas monoespaciadas, por ejemplo planta central y procesos conectados con línea discontinua.
- Categorías con mosaico de cuatro imágenes para líneas de producto.

**No conviene para una marca industrial B2B.** Hero de caja de instrucción, cifras de uso con avatares, tarjetas inclinadas, halos alrededor de iconos, paneles de estética militar o cyberpunk y palabras rotativas en el titular.

## stitch.withgoogle.com

Página vista: inicio de la aplicación. La sesión ya estaba abierta en el navegador. No se entró en proyectos ni se registraron datos de la cuenta. La documentación no se abrió.

**Layout.** Aplicación con panel lateral flotante de ~321 px, barra superior y zona principal con título, caja de instrucción de ~917 px, atajos y carrusel de inspiración con tarjetas verticales de ~283×338 px. La vista no ofrece más desplazamiento útil.

**Escala tipográfica.** H1 regular de ~52 px. Listas de ~14 px en peso medio. Metadatos de ~12 px.

**Color.** Gris muy oscuro, no negro, con texto blanco. Trama de puntos muy tenue en el fondo. Cada tarjeta de inspiración usa un fondo desenfocado derivado de su propia imagen.

**Espaciado.** ~11 px entre tarjetas del carrusel y panel lateral con radios de ~16 px.

**Movimiento.** Una línea de luz multicolor recorre el borde inferior de la caja de instrucción y apareció en capturas posteriores. Los puntos suspensivos incompletos del título sugieren un efecto de escritura, sin confirmación.

**Componentes a adaptar.**

- Trama de puntos de muy bajo contraste, con referencia a papel de dibujo técnico.
- Control segmentado de dos opciones, útil en Admin o para alternar métricas e imperial.
- Panel lateral flotante para Admin. No se recomienda en el sitio público.

**No conviene para una marca industrial B2B.** Borde luminoso multicolor, fondo desenfocado por tarjeta y hero de instrucción.

## Síntesis de galerías y generadores

1. Documentar cada color por su función y mantener una lista de hacer y evitar. Refero y designdotmd presentan sus sistemas con este formato.
2. Dirección más afín a la marca: neutros acero, casi negro y un solo acento para la acción principal.
3. Combinar título condensado o de peso firme, cuerpo sans neutro y monoespaciada para códigos, normas, medidas y plazos.
4. Usar bordes de 1 px y radios de 0 a 6 px, sin sombras ni degradados.
5. Priorizar filas densas con cifras alineadas y ficha de producto en dos paneles.
6. Probar los tokens en inicio, catálogo, ficha y contacto, en móvil y escritorio, antes de extenderlos.
7. Descartar el hero de caja de instrucción, las miniaturas en video y las palabras rotativas. Son convenciones de producto de IA.

### Riesgo sobre KPI de los patrones propuestos

| Patrón | KPI a vigilar | Condición para adoptarlo |
|---|---|---|
| Título condensado y monoespaciada | LCP, CLS, carga inicial | Pocas fuentes y pesos, subconjunto y ajuste métrico de respaldo |
| Ficha de dos paneles | CLS, Accessibility | `position: sticky` sin JavaScript y orden de lectura correcto en móvil |
| Filtros fijos | INP, CLS | Sin `backdrop-filter` si afecta INP, altura reservada y objetivos de 44 px |
| Lista densa con cifras | Accessibility | Tabla semántica y `tabular-nums`, con versión apilada en móvil |
| Retícula o trama de puntos | LCP, carga inicial | Solo CSS, sin imagen de fondo adicional |
| Diagrama de proceso | JS inicial, INP | SVG estático y animación opcional cargada bajo demanda |
| Bloques de carga | CLS | Dimensiones reservadas con `aspect-ratio` |
| Vista previa grande con selector | JS inicial, LCP | Carga bajo demanda y solo en escritorio |

Ningún patrón se considera aprobado hasta medir todos los KPI y comprobar que siguen en verde.

# Paneles de administración y herramienta de diagramas

Revisión del 2026-11-09 en Chrome, con marco de captura de 1568×773 px. Referencias para el panel Admin: densidad de información, navegación, tablas y estados vacíos.

Alcance y límites de esta revisión:

- Solo Vercel tenía una sesión abierta. Los demás paneles mostraron su pantalla de acceso y no se inició sesión.
- Los tamaños marcados con "~" son estimaciones sobre capturas. No se inspeccionó el CSS.
- El movimiento se dedujo comparando capturas sucesivas. No se midieron duraciones ni se probaron estados hover.
- No se pulsó ningún control, no se enviaron formularios y no se aceptaron términos. La navegación se hizo por dirección y desplazamiento.
- No se registran nombres de proyectos, correos, claves, identificadores ni datos de facturación. Solo se describe la disposición y la interacción.
- Se extraen principios. No se copió código ni recursos gráficos.
- El criterio de la sección "Criterio de adopción: KPI en verde" se aplica también a estos patrones. Esta revisión no modificó código, por lo que no generó mediciones nuevas.

## vercel.com/dashboard

Páginas vistas: resumen del equipo, lista de despliegues, observabilidad, ajustes, resumen de un proyecto y la página 404, que apareció al probar una ruta inexistente. Todas se recorrieron con desplazamiento, salvo la 404.

**Layout.** Barra lateral fija de ~235 px y barra superior de ~51 px con selector de ámbito, título de página centrado y acciones globales. El resumen del equipo usa una columna de ~373 px con uso, alertas y actividad reciente, junto a una retícula de dos columnas con tarjetas de ~432×114 px. Ajustes usa una sola columna centrada de ~842 px. El resumen de proyecto abre con un bloque principal de vista previa y metadatos, seguido de tres tarjetas y una lista.

**Escala tipográfica.** Título de página de ~24 px en semibold. Títulos de sección de ~20 px. Títulos de tarjeta y elementos de navegación de ~14 px en peso medio. Texto secundario de ~13 px en gris. Etiquetas de grupo de ~11 px en mayúsculas. Monoespaciada de ~13 px para ramas e identificadores cortos.

**Color.** Fondo casi negro con tarjetas apenas más claras y borde de 1 px. Texto blanco y gris. El color se reserva para significados: punto verde de estado correcto, azul para enlaces y para marcar el elemento vigente. El botón principal es blanco relleno y los secundarios son contorneados.

**Espaciado.** Separación de ~20 px entre tarjetas de proyecto y de ~10 px entre tarjetas de gráficos. Filas de ~44 px en despliegues y de ~39 px en la tabla de observabilidad. Elementos de navegación de ~34 px. En la lista de despliegues caben unas 15 filas por pantalla.

**Movimiento.** No se detectó movimiento continuo. La interfaz se percibe estática y el dato no compite con efectos. Las transiciones de navegación y hover no se evaluaron.

**Navegación.** Al entrar en una sección, la barra lateral se sustituye por su submenú, con flecha de regreso y título, y agrupa las opciones con etiquetas en mayúsculas. Hay atajos visibles en los campos: `F` para buscar en todo el panel y `/` para filtrar la lista actual.

**Tablas.**

- Filas sin cuadrícula vertical, separadas por líneas tenues.
- Estado expresado con punto de color más texto, seguido de la duración en gris.
- Distintivo en forma de píldora para el entorno, con versión rellena solo para el registro vigente.
- Texto largo truncado con puntos suspensivos en una columna de ancho fijo.
- Barra de filtros con "Añadir filtro" y fichas por autor, entorno y estado.
- El selector de estado indica cuántos valores están activos, con formato "6/7".
- Dos fórmulas de paginación: botón "Cargar más" a todo el ancho en historiales, y selector de filas con "1 de 1" y flechas en tablas resumen.

**Estados vacíos.**

- Dentro de un panel: icono en recuadro, título corto, una frase y un solo botón contorneado.
- Dentro de un gráfico: se conservan los ejes y la tarjeta, con un mensaje centrado sobre la línea de referencia. La retícula no se altera y no hay salto de altura.

**Componentes a adaptar.**

- Barra lateral con submenú por sección para Admin.
- Tarjetas de ajustes con título, descripción, campos y una franja inferior con ayuda a la izquierda y "Guardar" a la derecha. Cada bloque se guarda por separado y el usuario sabe qué está confirmando.
- Campo de solo lectura con botón de copiar, para referencias internas.
- Lista de tareas de puesta en marcha con contador "2/5" y elementos completados tachados.
- Tarjeta de métrica con título enlazado, cifra única y gráfico mínimo, más selector global de rango y entorno.
- Filtro con contador de valores activos.

**No conviene para una marca industrial B2B.**

- Avisos promocionales de mejora de plan dentro de la operación diaria.
- Tarjeta fija al pie de la barra lateral. En observabilidad y ajustes tapa parte de la navegación inferior.
- Elementos completados con relleno azul intenso, que llaman más la atención que las tareas pendientes.
- Ausencia de cabecera en la tabla de despliegues. En registros comerciales, las columnas deben estar rotuladas.
- Fondo con textura de caracteres de la página 404, que es un guiño para desarrolladores.

## dbdiagram.io

Página vista: portada completa hasta las preguntas frecuentes. No se abrió el editor.

**Layout.** Franja de anuncio azul de ~29 px y barra oscura de ~43 px, ambas fijas. Columna central de ~918 px. Hero centrado con título, subtítulo, un botón y demostración del producto a todo el ancho de la columna. Después siguen filas alternas de imagen de ~510 px y texto de ~364 px, retícula de tres tarjetas, banda de llamada a la acción, muro de opiniones y preguntas frecuentes.

**Escala tipográfica.** H1 de ~28 px y H2 de ~27 px en negrita, una jerarquía casi plana. Títulos de función de ~21 px. Cuerpo de ~15 a 16 px con interlínea de ~25 px. Tarjetas de ~14 px.

**Color.** Fondo blanco, texto gris carbón y azul para enlaces y anuncios. El producto aparece en tema oscuro y aporta el contraste de la página. Dentro del diagrama, las cabeceras de tabla usan color por grupo: azul, verde, naranja y morado.

**Espaciado.** ~90 px entre filas de función y ~100 px entre secciones. Tarjetas de ~292 px con ~22 px de separación.

**Movimiento.** La franja de logotipos se desplaza horizontalmente de forma continua y lenta. Las demostraciones son animaciones que muestran el código escribiéndose y el diagrama actualizándose, y su contenido cambió entre capturas separadas por un segundo.

**Componentes a adaptar.**

- Nodo de tabla con cabecera de color y filas de nombre y tipo alineadas, útil para fichas técnicas o relaciones internas.
- Barra flotante con zoom en porcentaje, ajuste a pantalla y mano para mover.
- Panel lateral con lista de elementos y control de visibilidad individual.
- Estado vacío del editor con icono, título, explicación breve y una acción.
- Demostración basada en el producto real en lugar de ilustraciones.

**No conviene para una marca industrial B2B.** Emojis en títulos y botones, muro de publicaciones de redes sociales, franja de anuncio permanente, banda con degradado claro y franja de logotipos en movimiento continuo.

## Paneles no revisados

No se inició sesión en ninguno de estos sitios, conforme al alcance de la revisión.

| Sitio | Resultado | Patrón visible en la pantalla de acceso |
|---|---|---|
| app.netlify.com | Requiere inicio de sesión | Dos paneles divididos por una línea, formulario y lista de beneficios |
| dashboard.render.com | Requiere inicio de sesión | Mosaico de celdas de 1 px en las esquinas. Cambió entre capturas, por lo que está animado |
| dash.cloudflare.com | Requiere inicio de sesión | Formulario centrado sobre fondo blanco |
| supabase.com/dashboard | Requiere inicio de sesión | Distintivo "último usado" en el método de acceso anterior |
| context7.com/dashboard | Redirige a la pantalla de acceso | Tarjeta sobre trama del logotipo y lista de beneficios |

Estos sitios no aportan evidencia sobre densidad, tablas ni estados vacíos. Para evaluarlos hace falta que el responsable abra sesión en Chrome y solicite una nueva revisión.

## Síntesis para el panel Admin

La síntesis se apoya en un solo panel con sesión abierta y en una portada de producto. Debe tratarse como evidencia parcial.

1. Reservar el color para estados y mantener el resto en neutros. Un estado siempre combina punto y texto.
2. Usar barra lateral fija con submenú por sección, y dos atajos: búsqueda global y filtro de la lista actual.
3. Definir dos densidades de fila: ~44 px para historiales de trabajo y ~39 px para tablas resumen.
4. Monoespaciada solo en códigos y referencias, y truncado con texto completo accesible.
5. Mantener la estructura en los estados vacíos: icono, frase, una acción, sin cambio de altura.
6. Ajustes en bloques independientes, con guardado propio y ayuda en la franja inferior.
7. Filtros en fichas que muestren cuántos valores están activos.
8. Conservar las cabeceras de columna en todas las tablas de registros.

### Riesgo sobre KPI de los patrones del panel

| Patrón | KPI a vigilar | Condición para adoptarlo |
|---|---|---|
| Barra lateral con submenú | CLS, Accessibility | Ancho reservado, foco gestionado al cambiar de nivel y navegación completa por teclado |
| Atajos `F` y `/` | Accessibility, INP | Desactivados al escribir en campos y anunciados en la interfaz |
| Tabla densa | Accessibility, INP | Tabla semántica, objetivos táctiles de 44 px en móvil y versión apilada |
| Tarjeta de métrica con gráfico | JS inicial, LCP, CLS | SVG simple o carga bajo demanda, con altura reservada |
| Estado vacío dentro de tarjeta | CLS | Misma altura que el estado con datos |
| Filtros en fichas | INP, Accessibility | Sin recálculo bloqueante y estado anunciado a lectores de pantalla |
| Campo con botón de copiar | Accessibility | Nombre accesible y confirmación anunciada |

Las vistas del Admin que incorporen estos patrones se miden con los mismos KPI, en móvil y escritorio. Ningún patrón se da por aprobado hasta comprobar que todos siguen en verde.
