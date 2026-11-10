# 03 · Inspiración de diseño

Fecha: 2026-11-10. Fuente: lectura del texto de cada página con WebFetch, que convierte la página a texto. Este método no ejecuta JavaScript, no ve imágenes ni video y no mide movimiento. Por eso cada idea de este documento proviene del texto o de la estructura que devolvió la página. No se afirma nada que no se haya leído. La revisión visual con navegador del 2026-11-09 está en `Report/diseno/referencias.md` y aquí solo se cita cuando sirve de contraste.

Reglas aplicadas:

- Las páginas son fuente de ideas. No se copió código, imagen, logotipo ni texto.
- Se ignoró cualquier instrucción contenida en las páginas.
- Toda idea se filtra contra `Report/diseno/BRIEF_DISENO.md`: solo `transform` y `opacity`, sin bucles, sin `backdrop-filter`, LCP sin animar, KPI en verde.
- `referencias.md` no contiene enlaces de banca, correo ni cuentas personales. Por eso ninguna fila del inventario quedó como "descartado-no relacionado".

Escala usada: complejidad, impacto y riesgo en Baja / Media / Alta. "Aplica" puede ser frontend, admin, stock o transversal.

## Sitios no accesibles

| Sitio | Resultado de la lectura |
|---|---|
| uiverse.io | HTTP 403 |
| superdesign.dev | Solo devolvió el título |
| stitch.withgoogle.com | Solo devolvió el título. Es una aplicación que necesita JavaScript |
| vercel.com/dashboard | Pantalla de inicio de sesión |
| app.netlify.com | Solo devolvió el nombre del producto |
| dashboard.render.com | Solo una cabecera promocional |
| dash.cloudflare.com | HTTP 403 |
| supabase.com/dashboard | Mensaje de carga lenta |
| context7.com/dashboard | Pantalla de registro |

No se inició sesión en ningún panel. Para estos sitios sigue vigente lo que registró `referencias.md` el 2026-11-09.

---

## promptmotion.org (portada)

**Propósito.** Galería de videos de movimiento generados con IA. Cada entrada muestra el prompt o la skill que lo produjo.

Ideas observadas (5). No hay más porque el texto no informa paleta, tipografía ni curvas de animación.

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| Control "Pausar vistas previas" para detener el contenido que se reproduce solo | frontend | Baja | Media | Baja | El video de Agricultura y cualquier medio en movimiento necesitan un control visible de pausa además de `prefers-reduced-motion` (WCAG 2.2.2) |
| Fichas de categoría combinadas con búsqueda y orden | frontend | Media | Alta | Media (INP) | Barra del catálogo con familia, búsqueda `?q=` y orden en una fila de 44 px. Sin recálculo bloqueante |
| Tarjeta con póster fijo, título, autor y etiqueta de tipo | frontend | Baja | Media | Baja | Celda de documento descargable: miniatura fija con `aspect-ratio`, título, tipo (Ficha, Flyer, Catálogo) y peso del archivo |
| Acción "Copiar" en cada entrada | admin | Baja | Media | Baja | Botón de copiar junto a códigos de solicitud, RUC y correo, con confirmación anunciada por `aria-live` |
| Títulos de sección con regla inferior | transversal | Baja | Media | Baja | Coincide con la "cota" de `globals.css` (`.cota`). Confirma ese recurso, no lo cambia |

Descartado: rejilla con previsualizaciones en reproducción automática, porque genera bucles y compite con el LCP. También el bloque de patrocinio entre secciones.

## promptmotion.org/prompts

**Propósito.** Biblioteca de unos 1.614 prompts de motion design, con el video resultante cuando existe. Solo se leyeron los primeros 100.000 de 259.303 caracteres.

Ideas observadas (5). La página trata de piezas de video de 3 a 90 s. Lo útil para FUNDIGSAC es el vocabulario de técnicas, no las piezas.

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| Vistas en corte o despiece de un objeto | frontend | Alta | Alta | Alta (peso 3D) | Plano de la válvula en la ficha como SVG estático, con capas de cuerpo, compuerta, vástago y timón que el usuario muestra u oculta. No se reproduce solo |
| SVG animado como pieza autónoma | frontend | Media | Media | Media | Base técnica de la animación de entrada de 04: trazos SVG sencillos, sin imágenes ni canvas |
| Plantillas reutilizables con línea de tiempo | transversal | Media | Media | Baja | Escribir cada animación como tabla de tiempos (inicio, duración, curva, propiedad). 04 sigue este formato |
| Interacción por clic o arrastre en lugar de reproducción continua | frontend | Media | Media | Baja | El selector de accionamiento del héroe (`hero-valve.tsx`) ya responde al clic. Confirma la regla: el foco de movimiento lo inicia la persona |
| Bucles de 3 a 13 s | — | — | — | Alta | Se rechaza. El brief prohíbe los bucles. Para la entrada se fija 0,8–1,8 s y una sola reproducción |

Descartado: glitch con separación RGB, tipografía cinética sincronizada con música, vidrio líquido y morfismos de interfaz en bucle. Todas chocan con §2 del brief.

## getdesignsystem.io

**Propósito.** Extrae tokens de sitios en vivo y los entrega como DESIGN.md para agentes de código. Ofrece catálogo, extensión y exportación.

Ideas observadas (7):

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| DESIGN.md con tokens legibles por máquina y explicación en prosa | transversal | Baja | Alta | Baja | `Report/DESIGN.md` reúne los tokens reales de los tres sistemas con su motivo. Es la referencia para quien implemente |
| Nombres por función (primary, background, surface) y no por color | transversal | Baja | Alta | Baja | Ya existe en los tres sistemas: `--c-action`, `--primary`, `--color-action`. Falta unificar el vocabulario entre apps. DESIGN.md propone la equivalencia |
| Exportación a variables CSS, Tailwind v4 y W3C DTCG | transversal | Media | Media | Baja | Frontend y Stock usan Tailwind 4 con `@theme`. Un JSON DTCG con los hex de marca evitaría que cada app copie valores a mano. Queda como opción, sin dependencia nueva |
| Escala tipográfica registrada como proporción | transversal | Baja | Baja | Baja | No aplica tal cual: la escala del Frontend es fluida con `clamp()`. Se documenta el rango mínimo y máximo de cada paso |
| Unidad base de espaciado y radio como tokens | transversal | Baja | Media | Baja | Base de 4 px (`--sp-1` a `--sp-10`) y radios 2/4/6/8 px en Frontend. DESIGN.md los fija para las tres apps |
| Rasgo visual distintivo por marca | frontend | Baja | Alta | Baja | El rasgo de FUNDIGSAC es la "lámina técnica": regla de 1 px con tramo de 40×3 px. Se declara en DESIGN.md como firma |
| El formato no cubre estados (hover, foco, error) | transversal | Baja | Alta | Baja | Carencia del modelo. DESIGN.md de FUNDIGSAC añade foco, error, vacío y carga de forma explícita |

## motion.dev/docs/performance

**Propósito.** Guía de coste de render para animación web.

Ideas observadas (7):

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| `transform` y `opacity` son lo más seguro en todos los dispositivos | transversal | Baja | Alta | Baja | Coincide con el brief §4.2. Las tres animaciones de entrada usan solo esas dos propiedades |
| Animar una variable CSS no se acelera aunque alimente un `transform` | transversal | Baja | Alta | Baja | No animar `--p` ni ningún token. Los keyframes escriben `transform` directamente |
| Las animaciones con `requestAnimationFrame` corren en el hilo principal | transversal | Baja | Alta | Baja | La entrada se hace con `@keyframes` CSS. JavaScript solo decide si se reproduce, con un `setAttribute` |
| `will-change` crea capas que consumen memoria de GPU | transversal | Baja | Media | Baja | Sin `will-change` permanente. Si hace falta, solo durante la entrada y se retira al terminar |
| Transformaciones 3D y perspectiva promueven más capas de las esperadas | frontend | Baja | Media | Baja | Usar `translate`, `scale` y `rotate` 2D. Nada de `translate3d` en el overlay nuevo |
| `box-shadow` y `border-radius` evitan layout, pero el pintado puede ser caro | transversal | Baja | Media | Baja | El brief ya prohíbe animar sombra. Confirmado |
| La aceleración es una mejora progresiva y conviene perfilar en móvil | transversal | Baja | Alta | Baja | Medir la entrada con traza de rendimiento y CPU ×4 (§1.3 del brief) |

La página no trata `pathLength` ni el trazado progresivo de SVG. Como el brief prohíbe animar `stroke-dashoffset`, en 04 el "trazado" se hace con `scaleX`/`scaleY` de tramos rectos.

## motion.dev/docs/react-use-reduced-motion

**Propósito.** Documenta el hook que lee la preferencia de movimiento reducido.

Ideas observadas (5). La página es corta.

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| La preferencia se actualiza en vivo | transversal | Baja | Media | Baja | Usar `@media (prefers-reduced-motion: reduce)` en CSS, que también reacciona en vivo, en lugar de leerla una sola vez |
| Sustituir desplazamientos x/y por opacidad | transversal | Baja | Media | Baja | En movimiento reducido la entrada no se muestra. La línea final ya está pintada y estática |
| Detener video de fondo en reproducción automática | frontend | Baja | Media | Baja | Vídeo de Agricultura: póster con movimiento reducido. Ya previsto en el brief §4.5 |
| Desactivar parallax | frontend | Baja | Baja | Baja | Ya prohibido por el brief §2 |
| La preferencia decide valores dentro de la lógica (desplazamiento 0 en vez de -100 %) | transversal | Baja | Media | Baja | El script de arranque no pone `data-intro` si `matchMedia("(prefers-reduced-motion: reduce)")` coincide |

La página no explica el comportamiento en SSR. Para Next.js se resuelve sin el hook: CSS y un script en línea que lee `matchMedia` antes del primer pintado.

## magicui.design (portada y catálogo)

**Propósito.** Biblioteca de más de 150 componentes animados con React, Tailwind y Motion. La portada solo nombra "Dither Field". El catálogo (`/docs/components`) confirmó por nombre los componentes listados abajo. No se leyó su documentación individual.

Ideas observadas (8, por nombre en el catálogo):

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| Animated Beam (pulso entre nodos) | frontend | Media | Alta | Media | Origen del "pulso de agua" de la entrada del Frontend: un tramo corto que viaja por la tubería con `translateX`, una sola vez |
| Border Beam (luz que recorre un borde) | — | — | — | Alta | Rechazado: es un bucle y un brillo, ambos prohibidos |
| Number Ticker | admin | Baja | Baja | Media | Rechazado en Admin por el brief §6.7 (las cifras no cuentan). En Frontend solo con cifra validada, y hoy no hay ninguna validada |
| Marquee | frontend | Baja | Baja | Media | Rechazado: avance automático continuo. Si hubiera logotipos de clientes validados, fila estática |
| Grid Pattern | frontend | Baja | Media | Baja | Retícula de papel técnico solo con CSS, en el fondo de la banda de la entrada o del plano. Sin imagen |
| Dotted Map | frontend | Media | Media | Media | Mapa de cobertura en Perú como SVG estático, si Comercial valida las zonas |
| Bento Grid | frontend | Media | Media | Media | Ya hay celdas de 1 px en `.celdas`. Un bento solo serviría con fotografía real. Baja prioridad |
| Animated Circular Progress Bar | stock | Baja | Media | Baja | Progreso de subida en "Por subir" como barra lineal con `scaleX`, más legible a pleno sol que un anillo |

## smoothui.dev

**Propósito.** 228 primitivas y componentes animados para shadcn/ui. El código se copia al proyecto.

Ideas observadas (7):

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| Afirmación de "reduced-motion aware" en todo el catálogo | transversal | Baja | Alta | Baja | Requisito de aceptación: ningún componente nuevo entra sin su variante de movimiento reducido |
| Control para pausar la animación de una tira de logotipos | frontend | Baja | Media | Baja | Igual que en promptmotion: si algo se mueve más de 5 s, lleva pausa. Con la regla de cero bucles no debería existir |
| Number Flow (transición de dígitos) | stock | Media | Media | Media | Contador "por subir" de la banda de estado: cambio de cifra con opacidad en 120 ms, sin rodillo de dígitos. Prioridad baja |
| Primitivas Button, Dialog, Checkbox y Tabs animadas | admin | Media | Media | Baja | Admin ya tiene pestaña con `scaleX` y diálogo con 8 px. Confirma lo existente |
| Movimiento con resortes | — | — | — | Media | Rechazado. Los tres sistemas usan curvas `cubic-bezier` fijas, más baratas y previsibles |
| Bloques de Stats y Logo Clouds | frontend | Baja | Media | Alta (datos) | Solo con datos validados. Hoy se omiten (brief §2) |
| Dynamic Island, Siri Orb, Morph Toggle | — | — | — | Alta | Rechazados por estética de producto de consumo |

## animate-ui.com

**Propósito.** Versiones animadas de las primitivas de shadcn/ui sobre Radix, Base UI o React Aria, sin cambiar la API.

Ideas observadas (8):

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| Animar la primitiva accesible en vez de crear un componente nuevo | transversal | Media | Alta | Baja | El movimiento se añade sobre el marcado existente, con CSS y sin cambiar su semántica ni el foco |
| Botón de guardar con estado de carga y confirmación breve "Guardado" | admin, stock | Baja | Alta | Baja | Admin: "Guardar cambios" pasa a "Guardando…" y luego a "Guardado" con icono, 200 ms. Stock: "Guardado en este celular" con icono que escala de 0,8 a 1 |
| Toast | transversal | Baja | Media | Baja | Ya previsto: `translateY(8px)` y opacidad, 200 ms |
| Progress | stock | Baja | Alta | Baja | Base de la entrada de Stock: una línea de progreso con `scaleX` |
| Accordion | frontend | Media | Media | Media | Especificaciones de la ficha sin animar altura: contenido con opacidad y `translateY(-4px)` |
| Animar la lista cuando se agregan o quitan tareas | admin | Media | Media | Media | "Para hoy": la fila atendida sale con opacidad en 140 ms, sin colapsar la altura animada |
| Disparadores hover, tap, in view y loop | transversal | Baja | Media | Baja | En FUNDIGSAC solo tap y, en Frontend, in view una vez. Sin hover decorativo ni loop |
| Auditoría de transiciones lentas o con tirones | transversal | Baja | Alta | Baja | Ya existe `motion-audit.mjs` en Frontend. Falta un equivalente para Admin y Stock |

## 21st.dev

**Propósito.** Catálogo de comunidad con más de 12.000 componentes React y Tailwind, temas shadcn y plantillas. El código se copia al repositorio.

Ideas observadas (5). El texto solo nombra categorías. El detalle de patrones está en `referencias.md`.

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| Separar bloques de marketing y primitivas de interfaz | frontend | Baja | Media | Baja | Frontend ya separa recetas (`.cota`, `.celdas`, `.filas`) de componentes. Mantener esa frontera |
| Temas como paquetes de tokens | transversal | Baja | Media | Baja | Un único archivo de tokens de marca compartido por las tres apps |
| Componentes que se copian y no se instalan como dependencia | transversal | Baja | Media | Media | Coincide con "0 bibliotecas de animación". Todo lo que se copie pasa revisión de accesibilidad |
| Categoría de shaders y degradados | — | — | — | Alta | Rechazada por el brief §2 |
| Plantillas de varias páginas | frontend | Media | Baja | Media | No aplica: el sitio ya existe |

## styles.refero.design

**Propósito.** Biblioteca de más de 2.000 sistemas de diseño de sitios de producto, cada uno con colores, tipografía, espaciado, componentes y un DESIGN.md.

Ideas observadas (5). El texto de la portada no muestra cómo se estructura cada ficha. La ficha de dos paneles y la lista de hacer y evitar están en `referencias.md`.

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| Cuatro áreas por sistema: color, tipografía, espaciado y componentes | transversal | Baja | Alta | Baja | Estructura de `Report/DESIGN.md` |
| DESIGN.md junto a cada estilo | transversal | Baja | Media | Baja | Un DESIGN.md por organización, con notas por sistema |
| Conexión para que herramientas de IA lean el sistema | transversal | Media | Baja | Baja | No hace falta: basta con que `DESIGN.md` esté en el repositorio |
| Catálogo como fuente de recursos de diseño y prompts | transversal | Baja | Baja | Baja | Sin adaptación |
| Reproducir el aspecto de una marca real | — | — | — | Alta | Rechazado: FUNDIGSAC necesita identidad propia |

## getdesign.md

**Propósito.** Explica el formato DESIGN.md y lista análisis de sistemas de marcas conocidas.

Ideas observadas (6):

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| El documento guarda el razonamiento, no solo los valores | transversal | Baja | Alta | Baja | Cada token de DESIGN.md lleva su uso y su límite |
| Resumen de una línea por sistema | transversal | Baja | Media | Baja | Línea de firma: "Lámina técnica: papel blanco, tinta petróleo, reglas de 1 px" |
| Lista con logotipo, nombre, resumen y etiqueta | frontend | Baja | Media | Baja | Lista de documentos descargables o de normas: icono, nombre, resumen y tipo. Sin etiqueta "New" |
| Pestañas con contador (instalaciones, guardados) | admin | Baja | Media | Baja | Pestañas de Solicitudes con contador real de pendientes |
| Fotografía a sangre con monocromo (ejemplo Nike) | frontend | Media | Media | Media | Planta real con velo plano `rgb(0 43 58 / 68%)`, según el brief §3.2, fuera del héroe de portada |
| Estado hover descrito como "escala" en un ejemplo | — | — | — | Baja | El formato no cubre estados de forma sistemática. DESIGN.md los añade |

## designdotmd.directory

**Propósito.** Directorio de archivos DESIGN.md para agentes de código.

Ideas observadas: 3. El texto solo nombra funciones (resúmenes, muestras, plantillas, filtros y sistemas como industrial, logística y plano) y no las describe. El detalle visual está en `referencias.md`.

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| Resumen del sistema en pocas muestras de color | transversal | Baja | Media | Baja | Tres muestras de marca en DESIGN.md: petróleo `#004257`, azul logotipo `#0972a1`, celeste `#9bcee7` |
| Validar el sistema en plantillas | frontend | Media | Alta | Baja | Probar tokens en inicio, catálogo, ficha y contacto antes de extenderlos, como pide el brief §8 |
| Sistemas con nombre "industrial" y "blueprint" | frontend | Baja | Media | Baja | Confirma la dirección "lámina técnica". No se toma nada de esos sistemas concretos |

## ui-skills.com

**Propósito.** Catálogo de skills, guías y herramientas de ingeniería de diseño para agentes.

Ideas observadas (8):

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| `aspect-ratio` para evitar saltos | transversal | Baja | Alta | Baja | Ya en `.celda__media`. La banda de la entrada tiene alto fijo y está fuera del flujo |
| `text-balance` en títulos y `text-pretty` en párrafos | frontend | Baja | Media | Baja | Ya en `globals.css` (`h1, h2 { text-wrap: balance }`) |
| `tabular-nums` en datos | transversal | Baja | Alta | Baja | Ya en Frontend (`.dato`, `.num`) y Stock (`.num`). Falta revisar Admin |
| Objetivos táctiles de 44×44 px | transversal | Baja | Alta | Baja | Admin `--target: 44px`, Stock 56 px. Confirmado |
| Anillo de foco visible | transversal | Baja | Alta | Baja | `:focus-visible` de 2 px en Frontend. DESIGN.md lo fija para las tres apps |
| Campos siempre con rótulo | transversal | Baja | Alta | Baja | Receta `.campo` del Frontend. Extender a Stock |
| Auditoría de animaciones de solo lectura y priorizada | transversal | Baja | Media | Baja | Separar diagnóstico y cambio, como pide el brief §1.3 |
| Entrada y salida con cascada como detalle de pulido | transversal | Baja | Baja | Media | Solo donde el brief lo permite: cascada con tope de 250 ms. Nunca en Admin al cargar |

## v0.app

**Propósito.** Agente que convierte texto en código e interfaces desplegables.

Ideas observadas (5). El texto es de producto y casi no describe la interfaz.

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| Tarjetas en una columna en móvil y dos desde ancho medio | admin | Baja | Media | Baja | Accesos de "Para hoy": una columna hasta 720 px y tres desde 1024 px |
| Indicadores visuales de progreso mientras el agente trabaja | stock | Baja | Alta | Baja | La línea de flujo de Stock comunica "la app está lista" sin bloquear |
| Formularios accesibles que escriben en base de datos | frontend | Media | Alta | Baja | Formulario de cotización: rótulo visible, error debajo, confirmación con `role="status"` |
| Modo oscuro en Next.js | frontend, admin | Baja | Media | Baja | Ya existe en ambos. La entrada usa tokens que cambian con el tema |
| Componente de progreso para contenido | stock | Baja | Media | Baja | Paso "2 de 4" del flujo de registro, con barra `scaleX` |

## dbdiagram.io

**Propósito.** Herramienta para dibujar diagramas entidad-relación a partir de código.

Ideas observadas (8):

| Idea | Aplica | Complejidad | Impacto | Riesgo | Adaptación a FUNDIGSAC |
|---|---|---|---|---|---|
| Edición en dos paneles: texto a la izquierda, diagrama a la derecha | frontend | Media | Media | Media | Ficha de producto: datos técnicos a la izquierda y plano o foto fija a la derecha con `position: sticky` |
| Entrada sin fricción: "gratis, sin registro" | frontend | Baja | Alta | Baja | Cotizar sin cuenta. El CTA dice qué ocurre ("Pedir cotización") y no pide registro previo |
| Grupos plegables y vistas guardadas en diagramas grandes | admin | Media | Media | Media | Filtros guardados en Solicitudes ("Mis reclamos que vencen") |
| Historial de versiones con comparación y restauración | admin | Alta | Media | Media | "Historial de cambios" ya existe. Añadir comparación antes/después en cada registro |
| Bloques de función alternados con demostración | frontend | Media | Media | Media (LCP) | Sectores: foto real y texto alternados, con la foto estática. Sin video en bucle |
| Rejilla de iconos con una línea de texto | frontend | Baja | Baja | Media | El brief §2 prohíbe tarjetas iguales de icono y texto como estructura de página. Solo como lista de filas |
| Pie con sello de seguridad y grupos de enlaces | frontend | Baja | Media | Baja | Pie con Libro de Reclamaciones y documentos legales agrupados. Sin sellos no validados |
| Paleta de tres azules contra logotipos en negro | transversal | Baja | Media | Baja | La marca ya tiene tres azules: `#004257`, `#0972a1`, `#9bcee7` |

Descartado: tarjetas estilo red social con métricas, tira de logotipos repetida en movimiento y video de demostración en bucle.
