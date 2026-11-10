# 01 · Historial y regresiones del rediseño del 2026-11-09

Fecha del análisis: 2026-11-10. Se trabajó solo en modo lectura, con `git log`, `git diff` y `git show <sha>:<ruta>`. No se cambió ningún repositorio. Las marcas usadas son estas:

- **Eliminado**: no aparece en HEAD; se buscó con `grep` antes de afirmarlo.
- **Movido**: existe en HEAD, pero en otro lugar o detrás de un clic más.
- **Reestilizado**: misma función con otro aspecto.
- **[no verificado]**: no se confirmó en el código ni en el navegador.

No se abrió ninguna URL de producción. El análisis compara solo código.

## 1. Commits de referencia y HEAD

| Sistema | Referencia (última versión antes del rediseño) | Inicio del rediseño | HEAD analizado |
|---|---|---|---|
| Stock-Web-Automate | `7816f51` 2026-10-30 17:52 (diseño original). `5996fa2` 2026-11-09 16:01 añade la parte offline y es la base funcional | `9b6106a` 2026-11-09 18:44 "redesign the field app around one question per screen" | `9b6106a` |
| Admin | `ef54f47` 2026-10-20 13:38 | `7463455` 2026-11-09 16:48 (luego `dd17017`, `89b5f6b`, `dec1a04`, `be34e83`, `c61170c`) | `da75561` 2026-11-10 09:47 (incluye cambios de API y correo del 11-10, ajenos al diseño) |
| Frontend | `35f0576` 2026-11-04 11:20 | `07dc408` 2026-11-09 13:14 "technical sheet foundation", y 18 commits más hasta `165cee6` | `165cee6` 2026-11-09 18:42 |

Volumen de cambios:

- **Stock**: `5996fa2..HEAD` toca 57 archivos (+4086 / −2442). `7816f51..HEAD` toca 109 archivos, pero la mayor parte es offline y tests.
- **Admin**: `ef54f47..HEAD` toca 104 archivos (+12338 / −3944).
- **Frontend**: `35f0576..HEAD` toca 170 archivos (+16870 / −28038).

En Stock, el commit `5996fa2` (offline, hora original de la foto, fotos dentro de los PDF y migraciones aplicadas) es funcional y debe conservarse. Las pérdidas de diseño vienen casi todas de `9b6106a`. La única excepción es la campana del reporte semanal con isla animada, que ya se quitó en `5996fa2`.

## 2. Inventario por sistema

### 2.1 Stock-Web-Automate (PWA de campo)

**Navegación y pantallas**

- La app ya no abre en **Resumen**: ahora abre en **Registrar** (`App.tsx`, `useState<Vista>("registrar")`).
- **Movido.** En el celular, Resumen ya no se puede abrir. `NAV_MOVIL = ["registrar","stock","respaldo","mas"]` no lo incluye, y `views/Mas.tsx` solo enlaza Movimientos, Trabajadores e Informes PDF. En escritorio sigue en `NAV_LATERAL`. Antes, la barra inferior del celular tenía Resumen, Stock, Movimientos y Trabajadores (`App.tsx@7816f51`, constante `NAV`).
- **Movido.** Movimientos y Trabajadores pasaron a la sección "Más" en el celular, que suma un toque.
- **Movido.** El botón "PDF" de la cabecera pasó a Más, en la fila "Informes PDF".
- **Movido.** El selector de empresa de la cabecera se muestra ahora solo en las vistas `POR_EMPRESA`, y también dentro de Más.
- **Movido.** La píldora de conexión de la cabecera ("En vivo / Conectado / Revisar conexión") pasó a `BandaEstado.tsx`, una banda fija de 56 px.
- **Eliminado.** Botón flotante "Registrar" en el celular. Registrar es ahora la pantalla inicial.
- **Movido.** El botón flotante del asistente IA quedó como botón secundario en Registrar y se desactiva sin conexión (`BotonAsistente` se sigue montando en `App.tsx:512`).
- **Eliminado en `5996fa2`.** Campana del reporte semanal con "isla" animada: `CampanaReporte` y `EspacioReporte`, con resorte de framer-motion. La reemplazó `AvisoReporte`, que ahora está dentro de Más.

**Dashboard (Resumen)**

- **Reestilizado.** Se conserva el contenido: "Qué hay que reponer" con chips, "Lectura rápida", las 4 cifras, "Stock por empresa", "Últimos movimientos" y el gráfico de 30 días. Lo que cambió:
  - Las 4 tarjetas KPI independientes con ícono pasaron a ser una sola franja.
  - Se quitaron los `Kicker`, que eran etiquetas en versalitas.
  - El título "Hay que reponer" pasó a "Qué hay que reponer".
- **Degradado.** En el celular ya no se monta el gráfico `MovChart`. En su lugar aparece el texto "El gráfico se ve en una pantalla más ancha" (`views/Resumen.tsx:248-253`).

**Tablas, filtros y búsqueda**

- Se conservan la búsqueda y los chips de estado en Stock, y la búsqueda, el período, el tipo y los anulados en Movimientos. Solo cambió el estilo, a controles de 56 px.
- **Degradado.** En Trabajadores, la tabla `Tabla` (Trabajador / Unidades recibidas / Última entrega / Detalle) pasó a ser una lista `<ul>`, también en escritorio. Se agregó un filtro por área.
- La ficha de producto (`Detalles.tsx`) conserva los botones de entrada y salida, el detalle por talla, el historial y "Entregas registradas". En el celular, la tabla por talla pasó a ser una lista.
- **Reestilizado.** El registro pasó de un diálogo único con pestañas Entrada/Salida (`role="tablist"`) a un flujo por pasos a pantalla completa (`FlujoRegistro.tsx`, `PantallaRegistrar.tsx`).
- **Reestilizado.** Respaldo pasó a llamarse "Por subir". Se conservan reintentar, descartar, adoptar, descargar la foto, "subir ahora" y "proteger datos"; las filas se movieron a `FilaPorSubir.tsx`.

**Estilo (`src/index.css`)**

- **Fuentes**: Archivo (texto) y Fraunces (títulos `.display`) pasaron a `system-ui`. Se quitaron `@fontsource/archivo`, `@fontsource/fraunces` y `framer-motion` de `package.json`.
- **Paleta**: la paleta "Slab" (gris frío `#f1f2f4`, tinta `#0e0f11`, rojo laca `#d7261e`) pasó a una paleta de campo:
  - fondo `#f1f5f7`
  - tinta `#0b1d26`
  - acción `#004257`
  - rojo `#b3261e`
  - banda sin conexión `#ffc247`
- **Radios**: Tailwind usaba sus valores por defecto (`rounded-xl` 12 px, `2xl` 16 px, `3xl` 24 px). Ahora quedan fijos en 6–8 px.
- **Sombras**: se eliminaron `--shadow-card` y `--shadow-pop`; hay 0 usos en `src/`.
- **Animación**: se eliminaron la entrada escalonada, el cambio de vista con `AnimatePresence`, el `whileHover` de los KPI y el resorte de la isla. Ahora solo hay transiciones CSS cortas.
- **Texto**: todo `p` y `li` va justificado.

### 2.2 Admin (panel del personal)

**Rutas.** Son las mismas páginas, `ef54f47` contra HEAD; solo se añadió `src/app/api/v1/[...path]/route.ts` el 11-10. El único archivo borrado es `src/components/cases/case-list.tsx`, reemplazado por `src/components/requests/request-list.tsx`. Este conserva pestañas o etapas con conteo, búsqueda, orden, tabla y paginador.

**Navegación**

- **Movido.** El menú lateral de 9 entradas en 3 grupos (`app-shell.tsx@ef54f47`, `NAV`) pasó a 4 secciones: Inicio, Solicitudes, Cuentas y Ajustes (`shell/nav.ts`). Las colas quedan como pestañas dentro de Solicitudes; Roles y Actividad, dentro de Ajustes.
- **Movido.** Los contadores por cola del menú lateral (`nav-count`) ahora se muestran por sección con `count(sectionWaiting(s))`.
- **Eliminado del panel.** Los botones de tema claro/oscuro (`ThemeToggle`) e idioma (`LangToggle`) ya no están en la barra superior ni en el menú lateral. Siguen en `/login` (`auth-shell.tsx`) y en Ajustes (`settings-view.tsx`). El componente `shell/pref-toggles.tsx` sigue en HEAD. El modo oscuro no se perdió: `tokens.css` mantiene `:root[data-theme="dark"]`.
- **Mejorado.** La búsqueda rápida Ctrl K se conserva y ahora también encuentra solicitudes por código.

**Inicio (dashboard)**

- **Movido detrás de un clic.** KPIs, la tendencia de altas por día (`ColumnChart` con opción de verla como tabla), el embudo de alta a cotización, la mezcla por método y "Últimos" ahora viven en `panel/month-numbers.tsx`. Ese bloque está dentro de un `<details>` cerrado que carga al abrirse (`overview-view.tsx:304-317`). Antes eran la vista principal (`overview-view.tsx@ef54f47`: `Kpis`, `TrendCard`, `FunnelCard`, `MixCard`).
- **Eliminado.** La columna derecha con "Pendientes de verificación" tenía un botón "Reenviar" por persona, que llamaba a `useResendVerification`. Hoy solo hay un atajo a `/usuarios?estado=pending`, y el reenvío existe solo dentro de la ficha de cada usuario.
- **Reestilizado.** `DueList` (plazos legales) pasó a la lista de tareas "Para hoy", ordenada por plazo legal.

**Cuentas, Roles y Actividad**

- Cuentas conserva la tabla TanStack con selección, orden, filtros, acciones masivas y exportar CSV. El menú por fila pasó a ser un botón "Abrir".
- Roles conserva la matriz de comparación y añade "elegir persona".
- Actividad conserva la búsqueda, el filtro por tipo y la exportación.

**Ajustes**

- **Eliminado.** El selector de densidad (`id="pref-density"`). El código fuerza `setDensity("comfortable")` en `settings-view.tsx:76`.
- **Eliminado.** La vista previa del correo de alertas (`mail-preview`), los interruptores de correo por persona y las sesiones de dispositivo. Según el commit `89b5f6b`, los interruptores y las sesiones eran ficticios. **[no verificado]** si la vista previa también lo era.

**Estilo**

- Se mantienen la fuente IBM Plex Sans/Mono y los radios 10/6/4.
- `--primary` cambió de `#12222d` (grafito) a `#004257` (petróleo).
- Los controles crecieron de 34 a 40 px, y a 48 px en el teléfono.
- Las filas crecieron de 52 a 56 px y el texto de 14 a 15 px.
- `motion.css` perdió 127 líneas: entrada escalonada `.stagger`/`.route`, `grow-x`/`grow-y` (dibujo de líneas), subrayado de pestaña animado y cascada de "Para hoy".
- `AnimatedNumber` ya no cuenta: pinta la cifra directamente.

### 2.3 Frontend (sitio público)

**Rutas**

- Se eliminó `industrias/_sector/sector-page.tsx`, reemplazado por `sector-kit.tsx`.
- Se añadieron `productos/accesorios-hdpe`, `conexiones-y-fittings`, `equipos-termofusion` y `medidores`.
- Ninguna URL pública desapareció.

**Portada (`src/app/page.tsx`)**

- **Eliminado.** `HeroCarousel` (`_landing/hero-carousel.tsx`), con dos variantes de válvula, autoplay y pausa. Lo reemplaza `HomeHero` + `hero-valve.tsx`, que conserva el selector de accionamiento pero sin autoplay (0 coincidencias de autoplay o intervalo).
- **Eliminado.** `ComponentsCarousel`: un carrusel de familias con arrastre y barra de avance. Lo reemplaza la cuadrícula `FamiliesSection`.
- **Eliminado.** `SectorsBand`: tres franjas diagonales que se ensanchaban al apuntar, con carrusel de puntos en el celular. Lo reemplaza `SectorsSection`.
- **Eliminado.** `SmoothScroll` (Lenis en anclas). El paquete `lenis` sigue en `package.json` sin uso **[no verificado: otros imports]**.
- **Eliminado.** `words.tsx`, la entrada de títulos palabra por palabra.
- **Eliminado.** El anillo de progreso del botón "subir" en `floating-actions.tsx`. WhatsApp se conserva.
- Se mantienen Respaldo, Documentos, Ubicación y los botones flotantes.

**Catálogo**

- **Eliminado.** `screens/islands/w03-valvulas*`: tarjetas de compuertas con carrusel de fotos reales, inclinación 3D hacia el cursor, flechas anterior/siguiente y rango de diámetros. Corresponde al trabajo del 10-27 (`65db9ab`, `c13042d`, `3c81f25`).
- **Eliminado.** `w04-tuberias*` y `w05-marcos*`, las páginas de familia con diseño propio.
- **Eliminado.** `w02-catalog*`, el listado con filtros.
- Todo lo anterior pasó a las vistas genéricas `productos/_catalog/catalog-view.tsx` y `family-view.tsx`. La búsqueda `?q=`, la familia `?familia=`, el orden, la comparación, los documentos y los beneficios se conservan.
- **Eliminado.** `valve-sheet.tsx`, la ficha propia de las 7 válvulas del 11-04. Lo reemplaza `SheetView`, que incluye relacionados.
- Las pantallas `w07`, `w08` y `w09` ya no se enrutan, pero eran plantillas con "Pendiente de validación" y su pérdida no es relevante.
- `w06-ficha` (compuerta) conserva el 3D, el plano, la galería con lightbox, las descargas y el carrito.

**Industrias, Nosotros y páginas legales**

- **Eliminado.** `agricultura/hero-motion.tsx`: hero con shader WebGL de rocío y gotas en canvas. Lo reemplaza `hero-video.tsx`.
- **Eliminado.** Los CSS propios de agricultura y minería.
- **Eliminado.** Las fotos hero de Términos, Cookies, Libro de reclamaciones y del 404 (`_legal/images.ts`). El 404 perdió la foto de fondo y las tarjetas con miniatura; hoy solo tiene enlaces.
- **Eliminado.** `nosotros/icons.tsx`. Nosotros cambió sus secciones: antes "highlights", historia y esencia; ahora sectores, historia, esencia y datos.

**Asistente IA**

- **Eliminado.** El fondo animado "aurora" con partículas del chat: keyframes `ai-aurora` y `ai-motes`, del commit `d70c368`.

**Estilo**

- **Fuentes**: Plus Jakarta Sans (títulos) + Inter pasaron a IBM Plex Sans (con eje de ancho) + IBM Plex Mono (`layout.tsx`).
- **Color**:
  - Acento naranja `--lp-orange #f26a1b` → `var(--c-action)` = `#004257`. Los botones `.lp-btn--solid` y los acentos dejaron de ser naranjas.
  - Azul marino `--lp-navy #0b2244` → `--c-primary-deep #002b3a`.
  - Fondo cálido `--c-background #fbfaf7` → `#ffffff`.
- **Radios**: sin cambio (`--radius 0.125rem`).
- **Modo oscuro**: se conserva (`html[data-lp-theme="dark"]`).
- **Cabecera**: conserva la búsqueda, el idioma, el tema, el carrito y la cuenta. Añade un acceso al Libro de reclamaciones.
- **Rendimiento**: los commits `c238834`, `3f29850`, `191cdf8`, `b29d194` y `53b8906` optimizaron el LCP. Recuperar carruseles, fuentes o fotos hero va en contra de esa medición.

## 3. Tabla de decisiones

| sistema | commit referencia | qué se perdió o cambió | archivo(s) en la referencia | riesgo de recuperarlo | recomendación |
|---|---|---|---|---|---|
| Stock | `5996fa2` | Resumen inaccesible en el celular | `src/App.tsx` (`NAV`) | Bajo | recuperar (fila en Más o 5.º ítem) |
| Stock | `5996fa2` | Gráfico de 30 días oculto en el celular | `src/views/Resumen.tsx`, `src/components/MovChart.tsx` | Bajo–medio (descarga recharts en el celular) | recuperar con carga diferida |
| Stock | `5996fa2` | Tabla de Trabajadores pasó a lista | `src/views/Trabajadores.tsx` | Bajo | combinar (tabla en `lg`, lista en el celular) |
| Stock | `7816f51` | Tipografía Archivo/Fraunces, paleta Slab, radios 12–24 px, sombras | `src/index.css`, `package.json` | Medio (contraste y peso de fuentes; el rediseño buscaba uso con guantes y a pleno sol) | combinar (Fraunces solo en títulos, sombras suaves; mantener tamaños y contraste) |
| Stock | `7816f51` | Animaciones framer-motion | `src/App.tsx`, `src/views/*.tsx` | Medio (+~40 kB, conflicto con todas las vistas) | mantener actual |
| Stock | `7816f51` | Campana con isla animada | `src/components/CampanaReporte.tsx` | Alto (reescrito dos veces) | mantener actual |
| Stock | `5996fa2` | Registro en diálogo con pestañas | `src/components/Registrar.tsx` | Alto | mantener actual |
| Admin | `ef54f47` | Tema e idioma fuera de la barra superior del panel | `src/components/shell/app-shell.tsx` (líneas 155, 200) | Bajo (el componente existe) | recuperar |
| Admin | `ef54f47` | Dashboard visible por defecto (KPIs, tendencia, embudo, mezcla) | `src/app/(panel)/panel/overview-view.tsx`, `overview.css` | Bajo–medio | combinar (`<details open>` en escritorio o la tendencia visible) |
| Admin | `ef54f47` | Lista de pendientes de verificación con "Reenviar" en Inicio | `overview-view.tsx` (`PendingList`) | Bajo | recuperar dentro de "Para hoy" |
| Admin | `ef54f47` | Densidad compacta | `src/app/(panel)/configuracion/settings-view.tsx` (`pref-density`) | Bajo (la preferencia sigue en `lib/prefs.tsx`) | recuperar |
| Admin | `ef54f47` | Vista previa del correo de alertas | `settings-view.tsx` (`mail-preview`) | Bajo | combinar solo si refleja el correo real **[no verificado]** |
| Admin | `ef54f47` | Menú de 9 entradas en 3 grupos | `app-shell.tsx` | Medio | mantener actual (rutas intactas) |
| Admin | `ef54f47` | Animaciones (stagger, conteo, líneas, subrayado) | `src/styles/motion.css`, `src/components/ui/animated-number.tsx` | Bajo | mantener actual (decisión explícita del brief §6.7) |
| Admin | `ef54f47` | Primario grafito `#12222d` | `src/styles/tokens.css` | Bajo | mantener actual (alinea con el petróleo del sitio) |
| Frontend | `35f0576` | Acento naranja `#f26a1b` en CTA | `src/app/landing.css` (`--lp-orange`, `.lp-btn--solid`) | Medio (muchos CSS; contraste AA de texto blanco sobre naranja **[no verificado]**) | combinar (naranja solo en el CTA principal; decisión de marca) |
| Frontend | `35f0576` | Tarjetas de válvulas con carrusel de fotos, inclinación y flechas | `src/screens/islands/w03-valvulas.tsx`, `w03-valve-media.tsx`, `w03-valvulas.module.css`, `w03-valvulas-copy.ts` | Medio–alto (LCP, dos sistemas de estilos) | combinar (portar `w03-valve-media` como celda opcional en `family-view`) |
| Frontend | `35f0576` | Carrusel de familias y franjas diagonales de sectores | `src/app/_landing/components-carousel.tsx`, `sectors-band.tsx`, `words.tsx`, `src/app/home.css` | Alto (LCP de portada) | mantener actual o recuperar solo la banda de sectores bajo el pliegue |
| Frontend | `35f0576` | Fotos hero de páginas legales y 404 con miniaturas | `src/app/_legal/images.ts`, `not-found-view.tsx`, `legal.css` | Bajo–medio | recuperar el 404; legales opcional |
| Frontend | `35f0576` | Fondo aurora del chat IA | `src/shared/assistant/assistant-panel.css` (`ai-aurora`, `ai-motes`) | Bajo (solo CSS, se carga al abrir) | recuperar con `prefers-reduced-motion` |
| Frontend | `35f0576` | Anillo de progreso del botón subir | `src/app/_landing/floating-actions.tsx` | Bajo | recuperar |
| Frontend | `35f0576` | Hero WebGL de agricultura | `src/app/industrias/agricultura/hero-motion.tsx`, `agricultura.css` | Alto | mantener actual |
| Frontend | `35f0576` | Fuentes Jakarta/Inter | `src/app/layout.tsx` | Medio (afecta LCP y todo el CSS) | mantener actual (decisión de marca pendiente) |

## 4. Cómo recuperar cada ítem "recuperar"

Ningún ítem permite un `git cherry-pick` de commit completo: los commits del rediseño tocan decenas de archivos a la vez. Lo seguro es traer archivos o fragmentos con `git show <ref>:<ruta>` e integrarlos a mano en HEAD.

**Stock 1 · Resumen en el celular.**

- Referencia: `src/App.tsx@5996fa2`, constante `NAV`.
- HEAD:
  - Opción A: añadir `"resumen"` a `NAV_MOVIL` (`src/App.tsx:103`). La barra queda en 5 ítems.
  - Opción B: añadir `<Fila icono={LayoutDashboard} texto="Resumen" onClick={() => irA("resumen")} />` en `src/views/Mas.tsx:45`.
  - En cualquiera de las dos, añadir `"resumen"` a `DENTRO_DE_MAS` (`App.tsx:105`) para que aparezca el botón "Volver a Más".
- Conflictos: ninguno de código. Hay que actualizar `tests/e2e/regresion.spec.ts` si cuenta los ítems de la barra.

**Stock 2 · Gráfico en el celular.**

- Referencia: `src/views/Resumen.tsx@5996fa2` (bloque `MovChart`).
- HEAD: `src/views/Resumen.tsx:248-253` condiciona el gráfico a `useEsEscritorio()`. Basta con quitar la condición y dejar `MovChartDiferido` cargando a demanda.
- Conflicto: el comentario de rendimiento ("recharts no se descarga en el celular"). Hay que medir el peso antes de decidir.

**Stock 3 · Tabla de Trabajadores (combinar).**

- Referencia: `src/views/Trabajadores.tsx@5996fa2`, líneas 132-177 (`<Tabla etiqueta="Trabajadores y unidades recibidas">`).
- HEAD: `src/views/Trabajadores.tsx` (la lista `<ul aria-label="Trabajadores y unidades recibidas">`).
- Conflictos: `th` y `td` en `components/ui.tsx` cambiaron de tamaño (14 px, `h-14`), y se eliminó `Kicker` de esta vista. Hay que mantener el filtro por área nuevo.

**Admin 1 · Tema e idioma en la barra superior.**

- Referencia: `src/components/shell/app-shell.tsx@ef54f47`, líneas 155 y 196-200 (`<ThemeToggle />`, `LangToggle`).
- HEAD: `src/components/shell/app-shell.tsx`, junto al botón de ayuda (~línea 152). `pref-toggles.tsx` no cambió de API.
- Conflictos:
  - Las clases `icon-btn` y `topbar__*` cambiaron en `shell.css`; hay que revisar la altura de 60 px.
  - En el teléfono, la barra inferior (`--tabbar-h`) no tiene espacio: conviene ponerlo en el menú de la cuenta.

**Admin 2 · Pendientes de verificación con Reenviar.**

- Referencia: `src/app/(panel)/panel/overview-view.tsx@ef54f47`, función `PendingList` (~líneas 415-470), y las clases del rail en `overview.css@ef54f47`.
- HEAD: `overview-view.tsx`, dentro de "Para hoy" o de `Shortcuts` (línea 272).
- Conflictos:
  - Los textos estaban en `t.overview` (diccionario global) y ahora van en `home-copy.ts`.
  - El rail `overview__rail` ya no existe en `overview.css`.
  - `useResendVerification` sigue en `lib/api/queries`.

**Admin 3 · Densidad compacta.**

- Referencia: `src/app/(panel)/configuracion/settings-view.tsx@ef54f47`, bloque `id="pref-density"`.
- HEAD: hay que quitar el forzado `if (density !== "comfortable") setDensity("comfortable")` en `settings-view.tsx:76` y añadir una opción `Choice`.
- Conflictos:
  - `settings-copy.ts` necesita los textos.
  - Hay que verificar que `tokens.css` todavía tenga el bloque de densidad compacta (`--row-h: 48px` sí está).
  - Con controles de 48 px en el teléfono, conviene limitar la opción a escritorio.

**Frontend 1 · 404 con foto y miniaturas.**

- Referencia: `src/app/_legal/not-found-view.tsx@35f0576`, las reglas `lg-nf__*` en `src/app/_legal/legal.css@35f0576` y los recursos `public/media/legal/404/*`.
- Antes de copiar, hay que confirmar que esos recursos siguen en HEAD **[no verificado]**.
- HEAD: `not-found-view.tsx` (usa `sheet.css`).
- Conflicto: `legal.css` perdió unas 2700 líneas. Hay que portar solo el bloque `lg-nf`.

**Frontend 2 · Aurora del chat.**

- Referencia: `src/shared/assistant/assistant-panel.css@35f0576` (`@keyframes ai-aurora`, `ai-motes` y sus selectores), más el marcado que los usa en el componente del panel. Hay que identificarlo con `git show d70c368 --stat`.
- HEAD: `assistant-panel.css`, que fue reestilizado (−239/+ líneas).
- Conflictos: los colores de la aurora usan el modo oscuro "grafito" (`5bdfa94`). Hay que revisarlo contra la paleta petróleo actual.

**Frontend 3 · Anillo de progreso del botón subir.**

- Referencia: `src/app/_landing/floating-actions.tsx@35f0576` (`topRef`, `--p`, `<svg className="lp-float__ring">`) y `.lp-float__ring` en `landing.css@35f0576`.
- HEAD: `floating-actions.tsx`, un diff de unas 10 líneas.
- Conflicto: `landing.css` fue reescrito; hay que portar solo la regla del anillo.

**Ítems "combinar" con más valor**

- **Admin · dashboard.** `<details className="numbers">` en `overview-view.tsx:308` puede abrirse por defecto en escritorio. No hace falta código de la referencia, porque `month-numbers.tsx` ya contiene `Figures`, `Trend`, `Funnel`, `Mix` y `Latest`.
- **Frontend · válvulas.** Hay que portar `w03-valve-media.tsx@35f0576` (carrusel e inclinación) como variante de `productos/_catalog/product-cell.tsx`, solo para `family.slug === "valvulas"`.
  - Conflictos: `public-catalog.ts` define las imágenes de cada celda; las fotos de compuerta y los blur venían de `@/shared/media/blur-valvulas` (hay que confirmar que existe en HEAD **[no verificado]**); y `use-new-cells.ts` limita las celdas en el primer pintado (`b29d194`).
- **Frontend · naranja.** Hay que redefinir en `src/app/landing.css` HEAD (líneas 11-12) `--lp-orange` y `--lp-orange-dark` a `#f26a1b` y `#b84508` solo para `.lp-btn--solid`, y mantener `--c-action` en el resto. Falta verificar el contraste AA (texto blanco sobre `#f26a1b`) y el modo oscuro (`globals.css:191-192`).
