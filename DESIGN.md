# DESIGN.md · Sistema de diseño FUNDIGSAC

Versión del 2026-11-10. Reúne los valores que existen hoy en el código de los tres sistemas. No inventa colores. Si algo contradice `Report/diseno/BRIEF_DISENO.md`, manda el brief.

**Firma: "Lámina técnica".** Papel blanco, tinta petróleo, reglas de 1 px y producto real. Un solo color de acción. La línea sustituye a la sombra. El naranja y el rojo solo existen dentro del logotipo.

Fuentes de los valores:

- `Frontend/src/app/globals.css` y `Frontend/src/shared/motion/motion.css`
- `Admin/src/styles/tokens.css` y `Admin/src/styles/motion.css`
- `Stock-Web-Automate/src/index.css` y `Stock-Web-Automate/index.html`
- `Frontend/public/brand/fundigsac.svg` y `fundigsac-icon.svg`

---

## 1. Marca

### 1.1 Logotipo

| Archivo | Uso |
|---|---|
| `Frontend/public/brand/fundigsac.svg` (viewBox 707,92×158,95) | Logotipo completo |
| `Frontend/public/brand/fundigsac-icon.svg` (viewBox −6 −10,5 181 181) | Icono |
| `Admin/public/brand/fundigsac.svg`, `Admin/public/brand/fundigsac-icon.svg` | Copias idénticas (mismo SHA-256) |
| `Frontend/public/media/fundigsac-logo.svg` | Copia idéntica del logotipo completo |
| `Stock-Web-Automate/public/icons/icon-192.png`, `icon-512.png`, `icon-512-maskable.png`, `apple-touch-icon.png` | Iconos PWA en PNG. No se inspeccionó su contenido |

Colores que contiene el logotipo:

| Hex | Dónde aparece |
|---|---|
| `#0972a1` | Relleno plano (`.cls-8`) |
| `#f09f1f` → `#ec2024` | Degradado naranja a rojo |
| `#3476bb` → `#53c4ce` | Degradado azul a cian |

Reglas:

- El logotipo no se recolorea, no se filtra y no se anima.
- Sobre fondo oscuro, si el contraste no alcanza, se coloca sobre una placa blanca.
- Los degradados solo existen dentro del archivo del logotipo.

### 1.2 Colores de marca en interfaz

| Rol | Hex | Token Frontend | Token Admin | Token Stock |
|---|---|---|---|---|
| Petróleo (acción, títulos) | `#004257` | `--c-primary`, `--c-action` | `--primary` | `--color-action` |
| Petróleo hover | `#00303f` | `--c-primary-hover`, `--c-action-hover` | `--primary-hover` | — |
| Petróleo profundo (héroe, pie) | `#002b3a` | `--c-primary-deep` | — | — |
| Azul logotipo (enlaces, datos) | `#0972a1` | `--c-logo-blue`, `--c-link` | `--accent`, `--focus`, `--chart-1` | `--color-info` |
| Celeste (acción sobre oscuro) | `#9bcee7` | `--c-sky` | — | — |
| Celeste suave | `#e3f0f9` | `--c-sky-soft` | `--accent-soft` es `#e5f1f7` | — |
| Foco (Frontend) | `#145b9b` | `--c-focus` | — | — |

`theme-color` de Stock: `#004257`.

---

## 2. Tokens

### 2.1 Color: Frontend, tema claro

| Grupo | Tokens |
|---|---|
| Superficie | `--c-background` `#ffffff` · `--c-surface-container-low` `#f3f7f9` · `--c-surface-container` `#e3f0f9` · `--c-surface-container-high` `#ddeaf4` · `--c-surface-container-highest` `#d7e4ee` |
| Texto | `--c-on-surface` `#111d24` · `--c-on-surface-variant` `#41484c` · `--c-text-secondary` `#52616b` · `--c-text-muted` `#56646e` |
| Línea | `--c-border` `#dce3e6` · `--c-outline` `#71787d` (borde de control) · `--c-outline-variant` `#c0c7cc` |
| Estado | `--c-success` `#206b48` · `--c-warning` `#8b5a15` · `--c-danger` y `--c-error` `#ba1a1a` · `--c-error-container` `#ffdad6` · `--c-on-error-container` `#93000a` |
| Sobre oscuro (`.on-dark`, `.lp-hero`) | Acción `#9bcee7` · texto sobre acción `#00303f` · acción hover `#bee9ff` · borde `rgb(255 255 255 / 16%)` |
| Tema oscuro (`html[data-lp-theme="dark"]`) | Fondo `#11181c` · superficie `#1a2329` · texto `#f2f5f6` · borde `#33414a` · acción `#9bcee7` · error `#ff8a93` · éxito `#5fd19b` · aviso `#e9b04a` |

La familia `--c-tertiary*` (marrón) no se usa en código nuevo.

### 2.2 Color: Admin

| Grupo | Claro | Oscuro |
|---|---|---|
| Marco y hoja | `--chrome` `#f1f2f3` · `--surface` `#ffffff` · `--raised` `#f5f6f7` · `--active` `#e9ebed` | `#0b0c0d` · `#141617` · `#1c1f21` · `#262a2d` |
| Líneas | `--border` `#e1e4e7` · `--rule` `#eceef0` · `--rule-strong` `#1b262e` · `--control` `#c6ccd1` | `#24282b` · `#1d2023` · `#c9ced2` · `#3e4448` |
| Texto | `--text` `#0e1820` · `--muted` `#47535c` · `--faint` `#5d6871` | `#f2f4f5` · `#b6bcc0` · `#969ca1` |
| Acción | `--primary` `#004257` y texto `#ffffff` | `#f2f4f5` y texto `#0b0c0d` |
| Datos y foco | `--accent` y `--focus` `#0972a1` | `#4fb3e3` |
| Estado | `--positive` `#247b50` · `--negative` `#c4242a` · `--warning` `#92400e` | `#3fc07a` · `#ef6b7b` · `#e5a93b` |
| Pastillas | Positiva `#dcfae5`/`#04250e` · negativa `#ffedea`/`#831c1e` · aviso `#fff4d6`/`#7a3a06` · neutra `#edf1f4`/`#33424d` | Ver `tokens.css` |

### 2.3 Color: Stock

`--color-ground` `#f1f5f7` · `--color-surface` `#ffffff` · `--color-ink` `#0b1d26` · `--color-ink-2` `#1b2b35` · `--color-muted` `#3f4f59` · `--color-faint` `#56646e` · `--color-line` `#c9d3d9` · `--color-line-2` `#dfe6ea` · `--color-action` `#004257` · `--color-info` `#0972a1` · `--color-red` `#b3261e` / `--color-red-soft` `#fdecea` · `--color-ok` `#14663f` / `--color-ok-soft` `#e4f4ec` · `--color-warn` `#7a4a00` / `--color-warn-soft` `#fff4d6` · banda sin conexión `#ffc247` con texto `#2b1a00`.

### 2.4 Tipografía

| Sistema | Familias | Escala |
|---|---|---|
| Frontend | IBM Plex Sans variable con eje de ancho (`--font-sans`). IBM Plex Mono 400 (`--font-mono`) solo para códigos, medidas y normas | `--fs-display` 36–64 px · `--fs-h1` 32–48 · `--fs-h2` 26–36 · `--fs-h3` 20–22 · lead 18/28 · body 16/26 · small 14/22 · label 13/18 · data 14/20 mono. Títulos H1 y H2 con `font-stretch: 85%`, peso 600 |
| Admin | IBM Plex Sans (`--font-plex`). Plex Mono 500 solo para códigos, RUC/DNI y horas | `--fs-title` 24 · `--fs-section` 17 · `--fs-kpi` 28 · `--fs-lead-figure` 34 · `--fs-body` 15 · `--fs-label` 13 · `--fs-small` 13 |
| Stock | `system-ui` y fuentes del sistema, 0 KB | Body 18 px con interlínea 1,4444. Títulos 24. Botón de registro 22/28 en peso 600. Banda 17. Mínimo 14 |

Reglas:

- Mínimo de 13 px en Frontend y Admin, y de 14 px en Stock.
- `text-wrap: balance` en títulos y `pretty` en párrafos.
- Largo de línea máximo `--measure: 68ch`.
- Cifras con `tabular-nums`.
- El texto corrido va justificado en Frontend y Stock, por decisión vigente del responsable.

### 2.5 Espaciado

Base de 4 px. Frontend: `--sp-1` 4 · `--sp-2` 8 · `--sp-3` 12 · `--sp-4` 16 · `--sp-5` 24 · `--sp-6` 32 · `--sp-7` 48 · `--sp-8` 64 · `--sp-9` 96 · `--sp-10` 128.

- Secciones: 64 px en móvil y 96 px desde 860 px.
- Contenedor: hasta 1360 px, con gutter `clamp(20px, 5vw, 64px)`.

Admin: `--pad` 32 · `--gap` 16 · `--section-gap` 36 · `--card-pad` 20 (16 en compacto) · `--inset` 8.

Stock: objetivos de 56 px, acción principal de 64 px y 12 px entre objetivos.

### 2.6 Radio

| Sistema | Valores |
|---|---|
| Frontend | `--r-badge` 2 · `--r-control` 4 · `--r-cell` 6 · `--r-media` 8 px. Píldoras solo en filtros |
| Admin | `--radius-sheet` 10 · `--radius-card` 6 · `--radius-control` 4 px |
| Stock | 6 px en controles, 8 px en bloques |

### 2.7 Sombra

- La jerarquía sale de la línea, no de la sombra.
- Frontend: `--shadow-overlay` `0 12px 32px -8px rgb(0 43 58 / 20%)`, solo en menús, carrito y diálogos. Las clases pequeñas de Tailwind no dibujan sombra.
- Admin: `--shadow-float`, solo en capas flotantes.
- Stock: sin sombras.

### 2.8 Capas (z-index)

Valores en uso hoy. El código nuevo debe usar estos niveles y no crear otros.

| Nivel | Frontend | Admin | Stock |
|---:|---|---|---|
| 1–2 | Apilado local | Apilado local | — |
| 20 | Barras pegajosas de página (catálogo, anclas) | Barras de ajustes | — |
| 30–45 | — | Menú lateral y barra inferior (`shell.css`), componentes | `z-40`, `z-[45]` |
| 50 | Cabecera `.lp-header` | Capa de componente | `z-50` |
| 55–56 | Animación de entrada `.fx-intro` (propuesta, 55) | — | Banda de estado `z-[55]`. Línea de entrada propuesta en 56 |
| 60–61 | Botones flotantes, asistente | — | `z-[60]` |
| 80 | Banner de cookies | Componente flotante | — |
| 85–95 | Panel del asistente, carrito | — | — |
| 100 | Enlace "saltar al contenido" | `base.css` | — |
| 200 | Visor de la ficha | — | — |
| 1000 | `NavProgress` | — | — |

### 2.9 Puntos de corte

| Sistema | Valores |
|---|---|
| Frontend | 480 · 720 (tablas apiladas) · 860 (cabecera móvil a 72 px, secciones a 96 px) · 1024 (12 columnas) · 1261 (cabecera de escritorio, 4 celdas) · 1440 px |
| Admin | 600 (controles de 48 px) · 720/721 (tabla a tarjetas) |
| Stock | Puntos de corte por defecto de Tailwind 4, sin redefinir en `index.css`. No se verificó en qué punto aparece el menú lateral de escritorio |

Para pruebas se usan estos anchos: 320, 390, 768, 1024, 1261, 1440 y 1920 px.

### 2.10 Movimiento

| Sistema | Curvas | Duraciones |
|---|---|---|
| Frontend | `--mo-ease` `cubic-bezier(0.2, 0.7, 0.2, 1)` · `--mo-ease-out` `(0.16, 1, 0.3, 1)` · `--mo-ease-in` `(0.4, 0, 1, 1)` · `--mo-ease-in-out` `(0.65, 0, 0.35, 1)` | press 100 · fast 140 · base 200 · overlay 280 (salida 180) · reveal 420 · media 520 · focal 640 ms. Recorridos de 16 y 8 px, con pasos de 50 ms |
| Admin | `--ease` `(0.22, 1, 0.36, 1)` · `--ease-out` `(0.16, 1, 0.3, 1)` · `--ease-in` · `--ease-in-out` | 120 · 150 · 200 · 320 ms |
| Stock | `cubic-bezier(0.16, 1, 0.3, 1)` | Paso 160 ms · presión 100 ms · confirmación 200 ms |

Reglas de movimiento:

- Solo se animan `transform` y `opacity`.
- Sin bucles, salvo un indicador de carga durante una petición.
- Sin animación ligada al desplazamiento, sin `backdrop-filter` y sin `pointermove`.
- El elemento LCP no se anima.
- La salida dura entre el 60 y el 70 % de la entrada.
- Con `prefers-reduced-motion: reduce` todo es inmediato.
- Entrada: una por sesión, de 0,8 a 1,8 s (ver `04-design-decisions.md`).

---

## 3. Estados

| Estado | Regla común | Frontend | Admin | Stock |
|---|---|---|---|---|
| Foco | Siempre visible con `:focus-visible`, sin quitar el `outline` | 2 px `--c-focus` `#145b9b` con separación de 2 px. Sobre oscuro, `#9bcee7` | `--focus` `#0972a1`, y `#4fb3e3` en oscuro | `src/index.css` no define un token de foco. Propuesta: anillo de 2 px en `--color-info` `#0972a1` |
| Error | Texto que diga qué pasó y qué hacer, más icono. Nunca solo color | Bajo el campo, `--c-error` `#ba1a1a`, aparece con `mo-pop` en 200 ms | `--negative` `#c4242a` y pastilla `#ffedea`/`#831c1e` | `--color-red` `#b3261e` sobre `#fdecea`. Lo escrito no se pierde |
| Vacío | Misma altura mínima que el estado con datos. Una frase y como máximo una acción | Mensaje y enlace al catálogo | "Todo al día. No tienes nada pendiente.", sin botón | "Todo subido. No hay nada pendiente en este celular." |
| Carga | Altura reservada (`aspect-ratio` o `min-height`), sin brillo ni pulso | Bloque fijo en `--c-surface-container-low` | Bloques con altura reservada, sin inventar cifras | `.skeleton`: `--color-line-2`, radio 8, estático |
| Éxito | Icono y texto, anunciado con `role="status"` | `--c-success` `#206b48` | `--positive` `#247b50` | `--color-ok` `#14663f` |
| Aviso | Icono y texto | `--c-warning` `#8b5a15` | `--warning` `#92400e` | `--color-warn` `#7a4a00`. Sin conexión: `#ffc247`/`#2b1a00` |
| Deshabilitado | Opacidad 0,4 y `cursor: default`. El motivo se escribe si no es obvio | `.lp-arrow:disabled` | Botón principal de Ajustes, activo solo si hay cambios | El asistente sin conexión dice "Necesita conexión" |

---

## 4. Componentes

| Componente | Regla |
|---|---|
| Botón principal | Uno por pantalla. Fondo petróleo `#004257` con texto blanco (10,96:1). Hover `#00303f`. Al presionar, `translateY(1px)` en Frontend y Admin, y `scale(0.98)` en Stock. Alto de 48 px en Frontend (52 en el héroe), 40/48 px en Admin y 64 px en Stock |
| Botón secundario | Sin fondo, borde de 1 px en el color de contorno y texto en acción |
| Enlace | `#0972a1`, subrayado con `text-underline-offset: 3px` |
| Cota de sección | Regla de 1 px a todo el ancho y tramo de 40×3 px en acción, 24 px sobre el H2 (`.cota`). Sustituye a las etiquetas en mayúsculas |
| Celda de producto | Imagen `aspect-ratio: 1` con `contain` sobre `#f3f7f9`, separada por líneas de 1 px y sin hueco |
| Fila técnica | Tabla semántica. Números a la derecha con mono y `tabular-nums`, filas de 48 px. Por debajo de 720 px, pares rótulo-valor apilados |
| Campo | Rótulo visible arriba, alto de 48 px, borde de 1 px y error debajo. Letra de 16 px o más en táctil |
| Tabla de Admin | Cabeceras visibles y filas de 56 px. Hasta 720 px cada fila es una tarjeta con como máximo 4 datos. Botón "Abrir" en lugar de menú kebab |
| Estado en tabla | Punto o icono más texto, nunca solo color |
| Banda de estado de Stock | 56 px, fija y con `role="status"`. Gana el primer estado que coincida: por revisar, sin conexión, subiendo, por subir o al día |
| Iconos | `lucide-react` en Frontend y Stock. `@phosphor-icons/react` en Admin. Trazo uniforme y sin emojis |
| Objetivo táctil | 44×44 px como mínimo en Frontend y Admin, y 56 px en Stock |

Prohibido en los tres sistemas: halos, brillos, vidrio, aurora, partículas, inclinación 3D, cursores propios, carruseles automáticos, degradados decorativos y datos comerciales sin validar.

---

## 5. Notas por sistema

### Frontend: comercial

- Cada plantilla tiene un elemento LCP pintado en su estado final y una sola acción principal.
- Héroe oscuro en `#002b3a` con acción en celeste.
- Fotografía real sobre superficie neutra. El velo sobre foto es plano: `rgb(0 43 58 / 68%)`.
- La entrada "Línea de presión" solo se muestra en `/`.
- Tema oscuro con `html[data-lp-theme="dark"]`.

### Admin: datos densos

- Responde a "qué tengo que hacer ahora".
- Marco gris, hoja blanca y regla de tinta `#1b262e`.
- El azul `#0972a1` marca solo datos, la pestaña activa y el foco. El petróleo es el único botón relleno.
- Las pantallas llegan quietas. La única entrada es "Regla de tinta", una vez por sesión.
- Mono solo para lo que se copia o se compara carácter a carácter.

### Stock: campo y móvil

- Se usa con guantes, a pleno sol y con mala señal.
- Una pregunta por pantalla y el pulgar primero.
- Guardar nunca depende de la red.
- Fuentes del sistema y ningún recurso remoto en el primer pintado.
- La entrada "Línea de flujo" vive en `index.html` y en CSS local, y funciona en modo avión.
- Presupuesto de JS inicial: ≤ 150 KB, con objetivo de 120 KB.
