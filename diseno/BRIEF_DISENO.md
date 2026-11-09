# Brief de diseño FUNDIGSAC

Fuente única de verdad para quienes implementan el sitio público (`Frontend`), el panel interno (`Admin`) y la app de campo (`Stock-Web-Automate`). Versión del 2026-11-09.

Si este documento contradice un archivo anterior, manda este documento. Hay tres excepciones que mandan sobre él: la decisión de indexación ADR-001, los textos legales aprobados y cualquier dato técnico de producto validado por Ingeniería.

Reglas de trabajo: no se hace commit, push ni despliegue. No se tocan sistemas ni bases de datos de producción. No se imprimen ni se guardan secretos.

Fuentes revisadas: `Report/diseno/referencias.md`, `Report/README.md` §11.4, §18 y §22, `Frontend/.claude/contexto-agentes.md`, `Frontend/docs/MOTION_REPORT.md`, `Frontend/src/app/globals.css`, `Frontend/src/app/landing.css`, `Frontend/src/shared/motion/`, `Admin/.taste-skill/direction.json`, `Admin/src/styles/tokens.css`, `Stock-Web-Automate/src/` y las skills `impeccable` y `ui-ux-pro-max`.

---

## 1. Regla de cierre: KPI en verde en cada corrección

Requisito del responsable del proyecto: **toda corrección, por pequeña que sea, se mide contra todos los KPI y debe quedar en verde antes de darse por terminada.** Una corrección con un KPI en rojo no está terminada. Se simplifica, se retira o se corrige hasta que pase.

### 1.1 Objetivos

| KPI | Verde | Dónde se mide | Herramienta |
|---|---:|---|---|
| LCP | ≤ 2,5 s | Móvil y escritorio | `kpi-gate.mjs` |
| CLS | ≤ 0,1 | Móvil y escritorio | `kpi-gate.mjs` |
| INP | ≤ 200 ms | Interacciones de §1.3 | Traza de rendimiento con CPU ×4 |
| TBT, indicador de laboratorio de INP | ≤ 200 ms | Móvil y escritorio | `kpi-gate.mjs` |
| FCP | ≤ 1,8 s | Móvil y escritorio | `kpi-gate.mjs` |
| Speed Index | ≤ 3,4 s | Móvil y escritorio | `kpi-gate.mjs` |
| Lighthouse Performance | ≥ 90 | Móvil y escritorio | `kpi-gate.mjs` |
| Lighthouse Accessibility | ≥ 95 y revisión manual | Móvil y escritorio | `kpi-gate.mjs` más teclado |
| Lighthouse Best Practices | ≥ 90 | Móvil y escritorio | `kpi-gate.mjs` |
| Lighthouse SEO | ≥ 95 | Build indexable local, solo en `Frontend` | `kpi-gate.mjs` |
| Peso total inicial, móvil | ≤ 1,5 MB en portada | Móvil | `total-byte-weight` de Lighthouse |
| JS inicial comprimido | ≤ 150 KB | Móvil | Suma de `transferSize` de recursos `Script` |

`kpi-gate.mjs` aprueba desde 90 en todas las categorías. **Accessibility y SEO se leen contra 95**, aunque la línea del script diga `OK`.

### 1.2 Cómo medir

Se mide siempre sobre un build de producción, nunca sobre `next dev`, y sin otros procesos pesados en marcha.

`Frontend`, con build indexable local. Esto no cambia ADR-001 ni afecta a producción:

```bash
cd Frontend
node scripts/build-image-variants.mjs
SITE_INDEXABLE=true NEXT_DIST_DIR=.next-kpi node_modules/.bin/next build
SITE_INDEXABLE=true NEXT_DIST_DIR=.next-kpi node_modules/.bin/next start --hostname 127.0.0.1 --port 3102
node scripts/perf/kpi-gate.mjs --app fundigsac-indexable --base http://127.0.0.1:3102 \
  --routes /,/productos,/productos/valvulas/valvula-compuerta-fundigsac,/contacto,<ruta-corregida>
```

`Admin`, desde la carpeta `Frontend`, con el servidor ya levantado en el puerto 3100:

```bash
node scripts/perf/kpi-gate.mjs --app admin --base http://127.0.0.1:3100 --routes /login --no-seo
```

`Stock-Web-Automate`, con `npx vite preview --host 127.0.0.1 --port 4173` en marcha:

```bash
node scripts/perf/kpi-gate.mjs --app stock --base http://127.0.0.1:4173 --routes / --runs 5 --no-seo
```

Las vistas de `Admin` que exigen sesión se miden con la cuenta de demostración local y una auditoría Lighthouse sobre la pestaña ya autenticada, por ejemplo con la herramienta `lighthouse_audit` de Chrome DevTools. Nunca se usa una cuenta real.

Movimiento en `Frontend`:

```bash
node scripts/qa/motion-audit.mjs --base http://127.0.0.1:3102 --routes <rutas> --widths 320,390,768,1024,1261,1440,1920
```

El resultado debe indicar 0 bloques invisibles, 0 desbordes horizontales y 0 errores de consola nuevos.

### 1.3 Procedimiento para cada corrección

1. Medir la ruta afectada antes del cambio y guardar la línea.
2. Aplicar el cambio.
3. Ejecutar tipos, lint, pruebas unitarias y build.
4. Ejecutar `kpi-gate.mjs` en las rutas de §1.2 más la ruta tocada. Son 3 corridas por defecto y se juzga la mediana.
5. Medir INP con traza de rendimiento y CPU ×4 en las interacciones de la pantalla tocada: abrir menú móvil, filtrar catálogo, cambiar pestaña de ficha, escribir en un campo de formulario, abrir un diálogo.
6. Comprobar teclado, foco visible y `prefers-reduced-motion`.
7. Anotar en el cierre la tabla antes y después. Si hay un KPI en rojo, la corrección queda abierta.

En local no existe dato de campo. Los valores locales demuestran verde de laboratorio. El P75 real de `Report/README.md` §22 solo se confirma después de un despliegue autorizado.

### 1.4 Línea base medida el 2026-11-09

Fuente: `Report/kpi/fundigsac-indexable.jsonl`, una corrida por ruta. Son los valores de partida y **hoy no están en verde en móvil**.

| Ruta | Factor | Perf | A11y | SEO | LCP | CLS | TBT |
|---|---|---:|---:|---:|---:|---:|---:|
| `/` | Móvil | 82 | 100 | 100 | 4,82 s | 0 | 18 ms |
| `/` | Escritorio | 98 | 100 | 100 | 1,05 s | 0 | 0 ms |
| `/productos` | Móvil | 85 | 100 | 100 | 4,36 s | 0 | 11 ms |
| `/productos` | Escritorio | 99 | 100 | 100 | 0,85 s | 0 | 0 ms |
| `/productos/valvulas` | Móvil | 83 | 100 | 100 | 4,71 s | 0 | 12 ms |
| `/productos/valvulas` | Escritorio | 99 | **94** | 100 | 0,93 s | 0 | 0 ms |
| `/productos/marcos-y-tapas` | Móvil | 80 | 100 | 100 | 5,26 s | 0 | 13 ms |
| Ficha compuerta FUNDIGSAC | Móvil | 82 | 100 | 100 | 4,97 s | 0 | 19 ms |
| `/industrias` | Móvil | 88 | 100 | 100 | 3,91 s | 0 | 14 ms |

Lecturas para quien implementa:

- El rojo está en LCP y Performance móvil. El JS medía entre 211 y 231 KB comprimidos por ruta el 2026-10-20 (`MOTION_REPORT.md` §7), por encima del objetivo de 150 KB.
- El movimiento por sí solo no resuelve ese rojo. `MOTION_REPORT.md` §9 atribuye el LCP móvil al JS del framework y a las fotos del héroe. Por eso este brief convierte islas cliente en componentes de servidor, deja una sola imagen prioritaria y difiere cabecera, asistente y carrito todo lo posible.
- CLS y TBT ya están en verde y no pueden empeorar.
- SEO da 69 en el build normal porque el sitio es `noindex` por ADR-001. En el build indexable local da 100.

---

## 2. Prohibiciones globales

Valen para `Frontend`, `Admin` y `Stock-Web-Automate`.

- Estética genérica de IA: tarjetas iguales de icono, título y texto como estructura de página, etiquetas en mayúsculas sobre cada título, pastillas de novedad, halos, brillos, vidrio, aurora y partículas.
- Degradados decorativos. Se admiten solo los del archivo original del logotipo.
- Efectos recargados: inclinación 3D, cursores propios, efecto magnético, parallax, secciones fijadas al desplazar, carruseles con avance automático y bucles permanentes.
- Datos comerciales inventados: cifras de clientes, años, toneladas, plazos, precios, testimonios, certificaciones, logotipos de clientes y folios. Si un dato no está validado, se escribe "Por confirmar" o no se muestra.
- Fotografías o modelos 3D físicamente distintos del producto real.
- Variaciones del logotipo. El logotipo es `Frontend/public/brand/fundigsac.svg` y su icono `fundigsac-icon.svg`, sin filtros ni recoloreado. El ajuste `filter: brightness(1.35) saturate(1.1)` del pie se retira y, si el contraste sobre petróleo no alcanza, se coloca sobre una placa blanca.
- Emojis como iconos. Los iconos son `lucide-react` en `Frontend` y `Stock-Web-Automate`, y `@phosphor-icons/react` en `Admin`, con trazo uniforme.
- Color como único portador de un estado. Todo estado lleva texto y, cuando cabe, icono.

---

## 3. Frontend: dirección visual

### 3.1 Concepto: "Lámina técnica"

El sitio se lee como la lámina de un catálogo de ingeniería: papel blanco, tinta petróleo, líneas de 1 px y producto real sobre superficie limpia.

- **Un solo color de acción.** Azul petróleo sobre fondos claros y celeste sobre fondos oscuros. El naranja y el rojo solo existen dentro del logotipo.
- **Línea en lugar de sombra.** La jerarquía sale del tamaño, el peso y las reglas de 1 px.
- **Recurso propio, la "cota".** Cada título de sección descansa bajo una regla de 1 px a todo el ancho, con un tramo inicial de 40×3 px en color de acción. Sustituye a las etiquetas en mayúsculas sobre los títulos.
- **Fotografía real.** Producto sobre superficie neutra y planta real. Nada de ilustraciones.

Cambio respecto a lo actual: el botón naranja `#f26a1b` con texto blanco tiene contraste 3,06:1 y no cumple AA. Pasa a petróleo. El azul marino `#0b2244` y `#0b1a2e` pasa a petróleo profundo.

### 3.2 Tokens de color

Reemplazar en `Frontend/src/app/globals.css`. Los tokens `--c-*` no listados conservan su valor actual. La familia terciaria marrón (`--c-tertiary*`) no se usa en código nuevo.

```css
:root {
  /* Marca */
  --c-primary: #004257;           /* se mantiene: títulos de marca */
  --c-primary-hover: #00303f;
  --c-primary-deep: #002b3a;      /* héroe, pie y bandas de cierre */
  --c-primary-container: #245a70; /* se mantiene */
  --c-logo-blue: #0972a1;
  --c-sky: #9bcee7;
  --c-sky-soft: #e3f0f9;

  /* Acción: lo único que usan botones, enlaces y foco */
  --c-action: #004257;
  --c-on-action: #ffffff;
  --c-action-hover: #00303f;
  --c-link: #0972a1;
  --c-focus: #145b9b;

  /* Superficies */
  --c-background: #ffffff;
  --c-surface: #ffffff;
  --c-surface-elevated: #ffffff;
  --c-surface-container-low: #f3f7f9;
  --c-surface-container: #e3f0f9;

  /* Texto y líneas: se mantienen */
  --c-on-surface: #111d24;
  --c-on-surface-variant: #41484c;
  --c-text-secondary: #52616b;
  --c-text-muted: #56646e;
  --c-border: #dce3e6;
  --c-outline: #71787d;           /* borde de controles */

  /* Estados */
  --c-success: #206b48;
  --c-warning: #8b5a15;
  --c-danger: #ba1a1a;
  --c-error: #ba1a1a;

  /* Sombra: solo menús, carrito y diálogos */
  --shadow-overlay: 0 12px 32px -8px rgb(0 43 58 / 20%);
}

/* Zonas oscuras en tema claro: héroe, pie, bandas de cierre */
.on-dark {
  --c-action: #9bcee7;
  --c-on-action: #00303f;
  --c-action-hover: #bee9ff;
  --c-link: #9bcee7;
  --c-focus: #9bcee7;
  color: #ffffff;
}

html[data-lp-theme="dark"] {
  --c-background: #11181c;
  --c-surface: #1a2329;
  --c-surface-elevated: #222d34;
  --c-surface-bright: #2b3840;
  --c-surface-dim: #0d1316;
  --c-surface-container-lowest: #161f24;
  --c-surface-container-low: #161f24;
  --c-surface-container: #222d34;
  --c-surface-container-high: #2b3840;
  --c-surface-container-highest: #223c4c;
  --c-surface-variant: #223c4c;
  --c-on-surface: #f2f5f6;
  --c-on-background: #f2f5f6;
  --c-on-surface-variant: #c2cbd1;
  --c-text-secondary: #c2cbd1;
  --c-text-muted: #a3aeb6;
  --c-secondary: #c2cbd1;
  --c-outline: #7c8a93;
  --c-outline-variant: #44525b;
  --c-border: #33414a;
  --c-action: #9bcee7;
  --c-on-action: #00303f;
  --c-action-hover: #bee9ff;
  --c-link: #9bcee7;
  --c-focus: #9bcee7;
  --c-danger: #ff8a93;
  --c-error: #ff8a93;
  --c-success: #5fd19b;
  --c-warning: #e9b04a;
}
```

Puente para no reescribir `landing.css`. Sustituye a las variables `--lp-navy` a `--lp-soft` de su primer bloque y a los valores de las redefiniciones de tema oscuro `html[data-lp-theme="dark"] .lp-header` y `html[data-lp-theme="dark"] .lp`. En tema oscuro `--lp-navy` funciona como color de texto, por eso se invierte:

```css
.lp, .lp-header, .lp-footer {
  --lp-navy: var(--c-primary-deep);
  --lp-ink: var(--c-on-surface);
  --lp-text: var(--c-on-surface-variant);
  --lp-orange: var(--c-action);
  --lp-orange-dark: var(--c-action-hover);
  --lp-line: var(--c-border);
  --lp-soft: var(--c-surface-container-low);
  --lp-gutter: max(clamp(20px, 5vw, 64px), calc((100vw - 1360px) / 2));
}

html[data-lp-theme="dark"] .lp,
html[data-lp-theme="dark"] .lp-header {
  --lp-navy: var(--c-on-surface);
}
```

Se elimina también la redefinición `.x-page .lp-btn { --lp-orange: … }` de `styles/pages.css`. `.lp-footer` pasa a `background: var(--c-primary-deep)` y el fondo oscuro de `.lp` y `.lp-header` a `var(--c-background)`.

Contrastes calculados con la fórmula WCAG 2:

| Par | Relación | Uso |
|---|---:|---|
| Blanco sobre `#004257` | 10,96:1 | Botón principal |
| `#00303f` sobre `#9bcee7` | 8,28:1 | Botón sobre fondo oscuro |
| `#9bcee7` sobre `#002b3a` | 8,80:1 | Enlace y foco sobre oscuro |
| `#0972a1` sobre blanco | 5,34:1 | Enlace |
| `#0972a1` sobre `#f3f7f9` | 4,95:1 | Enlace sobre superficie suave |
| `#0972a1` sobre `#e3f0f9` | 4,60:1 | Enlace en elemento seleccionado |
| `#111d24` sobre blanco | 17,14:1 | Texto |
| `#56646e` sobre `#f3f7f9` | 5,66:1 | Texto secundario |
| `#71787d` sobre blanco | 4,48:1 | Borde de control, mínimo 3:1 |
| Blanco al 72 % sobre `#002b3a` | 8,37:1 | Texto del pie |
| `#a3aeb6` sobre `#1a2329` | 7,06:1 | Texto secundario en oscuro |

Velos sobre fotografía: color plano `rgb(0 43 58 / 68%)`, sin degradado. Con el peor caso, una foto blanca, el texto blanco da 5,37:1. Con 62 % da 4,44:1 y no cumple, así que 68 % es el mínimo.

### 3.3 Tipografía

Hoy se cargan Inter con 3 pesos y Plus Jakarta Sans con 5. Ambas son la opción por defecto de la estética genérica y su coste compite con el LCP. Se sustituyen por **IBM Plex Sans variable**, con ejes de peso y de ancho (75 a 100), un solo archivo y la misma familia que ya usa `Admin`.

```ts
// Frontend/src/app/layout.tsx
import { IBM_Plex_Sans } from "next/font/google";
const plex = IBM_Plex_Sans({ subsets: ["latin"], axes: ["wdth"], variable: "--font-sans", display: "swap" });
```

- Se retira `adjustFontFallback: false`: el ajuste métrico de respaldo evita saltos de diseño.
- `IBM_Plex_Mono`, peso 400, `preload: false`, solo en familias y fichas, con variable `--font-mono`. Se usa únicamente para códigos de pieza, medidas, normas y referencias.
- Presupuesto: fuentes precargadas ≤ 80 KB en total. Si el archivo variable lo supera, se usa `IBM_Plex_Sans` en 400 y 600 más `IBM_Plex_Sans_Condensed` en 600.
- `Material Symbols` (`material-symbols-v3.woff2`, 26 KB, `font-display: block`) se retira de cada plantilla al rediseñarla, con `lucide-react` en su lugar. Sigue presente en 23 archivos, y la `@font-face` se borra al quitar el último uso.

Escala, en `:root` de `globals.css`. Los títulos usan `font-stretch: 85%`.

| Token | Tamaño | Interlínea | Interletraje | Peso | Ancho | Uso |
|---|---|---:|---:|---:|---:|---|
| `--fs-display` | `clamp(2.25rem, 1.55rem + 3.1vw, 4rem)` (36 a 64 px) | 1,05 | -0,02 em | 600 | 85 % | H1 de portada |
| `--fs-h1` | `clamp(2rem, 1.62rem + 1.7vw, 3rem)` (32 a 48 px) | 1,1 | -0,015 em | 600 | 85 % | H1 interior |
| `--fs-h2` | `clamp(1.625rem, 1.42rem + 0.9vw, 2.25rem)` (26 a 36 px) | 1,15 | -0,01 em | 600 | 85 % | H2 |
| `--fs-h3` | `clamp(1.25rem, 1.18rem + 0.3vw, 1.375rem)` (20 a 22 px) | 1,25 | 0 | 600 | 100 % | H3, nombre de pieza |
| `--fs-lead` | 18 px | 28 px | 0 | 400 | 100 % | Entradilla |
| `--fs-body` | 16 px | 26 px | 0 | 400 | 100 % | Texto |
| `--fs-small` | 14 px | 22 px | 0 | 400 | 100 % | Texto de apoyo, pie |
| `--fs-label` | 13 px | 18 px | 0,02 em | 600 | 100 % | Rótulos, en minúscula normal |
| `--fs-data` | 14 px, monoespaciada | 20 px | 0 | 400 | n/a | Códigos y medidas, `tabular-nums` |

Reglas: nada por debajo de 13 px en el sitio público. `text-wrap: balance` en títulos y `text-wrap: pretty` en párrafos. Largo de línea máximo de 68 caracteres. Campos con 16 px o más en táctil. Los títulos usan solo peso, tamaño y ancho para destacar, nunca color de texto degradado.

### 3.4 Espaciado, retícula y forma

| Token | Valor | | Token | Valor |
|---|---:|---|---|---:|
| `--sp-1` | 4 px | | `--sp-6` | 32 px |
| `--sp-2` | 8 px | | `--sp-7` | 48 px |
| `--sp-3` | 12 px | | `--sp-8` | 64 px |
| `--sp-4` | 16 px | | `--sp-9` | 96 px |
| `--sp-5` | 24 px | | `--sp-10` | 128 px |

- Separación entre secciones: 64 px en móvil, 96 px desde 860 px.
- Título de sección a contenido: 32 px en móvil, 48 px desde 860 px.
- Contenedor: `width: min(100% - 2 * clamp(20px, 5vw, 64px), 1360px)`. Modifica `.lp-shell`.
- Retícula: 12 columnas desde 1024 px con separación de 24 px. 4 columnas con separación de 16 px en móvil.
- Puntos de corte: 480, 860, 1024, 1261 (cabecera de escritorio) y 1440 px.
- Radios: 2 px en distintivos, 4 px en controles, 6 px en celdas, 8 px en imágenes grandes. No se usan píldoras salvo en los filtros.
- Bordes: 1 px `--c-border`. Sin sombras, salvo `--shadow-overlay` en capas flotantes.

### 3.5 Componentes base

| Componente | Especificación |
|---|---|
| Botón principal | Fondo `--c-action`, texto `--c-on-action`, radio 4 px, alto mínimo 48 px (52 px en héroe), 15/20 peso 600, sin sombra. Capa `::after` con `--c-action-hover` que pasa de opacidad 0 a 1 en hover. Al presionar, `translateY(1px)` |
| Botón secundario | Sin fondo, borde 1 px `--c-outline`, texto `--c-action`. Sobre oscuro, borde blanco al 60 % y texto blanco |
| Enlace | `--c-link`, subrayado con `text-underline-offset: 3px`. El cambio de hover es inmediato |
| Cota de sección | Bloque con `border-top: 1px solid var(--c-border)` y `::before` de 40×3 px en `--c-action`, 24 px sobre el H2 |
| Celda de producto | Imagen `aspect-ratio: 1`, `object-fit: contain` sobre `--c-surface-container-low`. Debajo, nombre en `--fs-h3` y una frase en `--fs-small`. Las celdas se separan por líneas de 1 px, sin hueco |
| Fila técnica | Tabla semántica. Celdas numéricas alineadas a la derecha con `tabular-nums`. Filas de 48 px. Desde 720 px hacia abajo pasa a bloques apilados de rótulo y valor |
| Campo | Rótulo visible arriba, 48 px de alto, borde 1 px `--c-outline`, radio 4 px. El error va debajo del campo, con icono y texto |
| Foco | `:focus-visible { outline: 2px solid var(--c-focus); outline-offset: 2px; }` en todo. Se elimina el foco naranja del bloque `:focus-visible` de `landing.css` |
| Objetivo táctil | 44×44 px como mínimo, con 8 px entre objetivos |
| Bloque de carga | Altura reservada con `aspect-ratio` o `min-height`, sin efecto de brillo |
| Banda de cierre | `.on-dark`, fondo `--c-primary-deep`, H2 y un solo botón. Sin foto de fondo. Se usa solo si el `copy` ya tiene ese título; si no, se omite |

Todas las imágenes declaran `width` y `height` o `aspect-ratio`. Fuera del primer pantallazo, `loading="lazy"`.

### 3.6 Recetas por plantilla

Cada plantilla define **un solo elemento LCP**, pintado en su estado final desde el primer fotograma, y **una sola acción principal**. El texto sale del `copy` existente. Quien implementa no redacta afirmaciones comerciales nuevas.

Next 16 marcó `priority` como obsoleto en favor de `preload`, y su documentación indica que en la mayoría de los casos se prefiera `loading="eager"` o `fetchPriority="high"`. Antes de tocar `next/image` se lee `node_modules/next/dist/docs/01-app/03-api-reference/02-components/image.md`.

#### Inicio (`/`, `src/app/page.tsx`)

LCP: la válvula del héroe o el H1, según el ancho. Acción principal: **Explorar catálogo**.

| Orden | Sección | Móvil | Escritorio desde 1024 px |
|---|---|---|---|
| 1 | Héroe "Lámina" (`.on-dark`, fondo `--c-primary-deep` plano) | `padding-top: 72px`. H1, entradilla, botón, enlace y válvula con `aspect-ratio: 578/1030` y alto `min(52svh, 400px)`. Debajo, selector de variante | `padding-top: 84px`, porque el héroe sube detrás de la cabecera. Texto en columnas 1 a 7, válvula en 8 a 12, línea vertical de 1 px blanca al 16 % entre ambas. Alto `min(840px, 100svh)` |
| 2 | Familias, título existente "Lo que necesita tu obra…" | 2 columnas de celdas de producto, la quinta ocupa las 2 | 5 columnas con líneas de 1 px |
| 3 | Sectores | Tres bloques apilados con foto 16:9, velo plano y título | Tres franjas con su corte diagonal estático, foto y velo plano |
| 4 | Respaldo | Foto real, H2 y tres filas separadas por línea | Foto real en columnas 1 a 7. H2 y tres filas en 8 a 12 |
| 5 | Documentación | H2, frase, botón secundario e imagen | Lista a la izquierda, lámina de ficha a la derecha |
| 6 | Ubicación | Datos y fachada del mapa | Datos en 1 a 5, mapa en 6 a 12. El mapa carga al pulsar, con el consentimiento existente |

Cambios obligatorios en el héroe:

- Se divide `hero-carousel.tsx` en un componente de servidor (texto y primera válvula) y una isla cliente pequeña (selector de variante).
- Se retiran `lp-hero__photo`, velo, `lp-eyebrow`, `lp-hero__rule`, `lp-hero__shadow`, inclinación con `pointermove`, flotación, avance automático, flechas, contador, barras de progreso, reproducción y pausa. La foto de planta pasa a Respaldo con carga diferida.
- El H1 es texto plano. Se retira `Words`, que parte el título por palabras.
- Primera válvula: `loading="eager"`, `fetchPriority="high"`, `sizes="(max-width: 860px) 60vw, 34vw"`, sin `filter: drop-shadow`. Es la única imagen con prioridad de la página.
- Selector: dos botones de 44 px con la etiqueta de `h.variants[i].label` y `aria-pressed`. La segunda válvula se monta tras el evento `load` o al primer `pointerenter` o foco en el selector, con `fetchPriority="low"`.

Cambios en el resto:

- `ComponentsCarousel` pasa a rejilla estática de servidor, sin avance automático.
- `SectorsBand` pasa a componente de servidor. En móvil no hay carrusel.
- Se elimina `SmoothScroll` y la dependencia `lenis`. Las anclas usan el desplazamiento nativo.
- `FloatingActions` conserva WhatsApp sin el pulso `lp-wa-pulse`.

#### Catálogo (`/productos`, `W02Catalog`)

LCP: el H1. Acción principal: **Agregar a cotización** en cada celda. Se conservan `?familia=` y `?q=`.

1. Migas, H1 y una frase. Sin imagen de cabecera.
2. Barra de filtros `position: sticky; top: 84px` (72 px en móvil), fondo sólido sin `backdrop-filter`, alto reservado de 64 px. Buscador y filtros por familia en píldoras con desplazamiento horizontal propio, y orden. Filtros de 44 px.
3. Contador de resultados con `aria-live="polite"` y altura reservada.
4. Rejilla de celdas: 2 columnas en móvil, 3 desde 860 px, 4 desde 1261 px. Las primeras 4 imágenes con `loading="eager"` y `fetchPriority="low"`, el resto diferidas. Sin precios.
5. Estado vacío: frase, y botón **Ver todo el catálogo**. Conserva la altura de la rejilla.

#### Familia (`/productos/valvulas`, `/tuberias`, `/marcos-y-tapas`)

LCP: el H1, sin foto de cabecera. Acción principal: **Solicitar cotización**.

1. Migas, H1, frase y acceso **Pedir documentación**.
2. Filtros o pestañas de línea: un solo nivel, de 44 px, con indicador `scaleX`.
3. Rejilla de celdas, o lista densa con fila técnica cuando haya cifras validadas. Código en `--fs-data`.
4. Documentos: filas sin tarjeta con nombre, formato y acción. Solo documentos reales.
5. Beneficios: máximo tres filas separadas por línea. Solo afirmaciones ya presentes en el `copy`.
6. Banda de cierre.

#### Ficha de producto (`/productos/[categoria]/[producto]`)

LCP: la primera foto de la galería. Acción principal: **Agregar a cotización**.

En el DOM el orden es siempre: migas, H1, galería, panel de decisión, tabla técnica, plano, documentos, relacionados. Ese es el orden de lectura en móvil.

Desde 1024 px, dos paneles con `grid-template-areas: "galeria titulo" "galeria panel" "detalle panel"`, `grid-template-rows: auto auto 1fr` y columnas 7 y 5:

- Izquierda: galería, y debajo descripción, tabla técnica y plano, con desplazamiento normal.
- Derecha: código en `--fs-data` y H1 arriba. Debajo, panel de decisión con `position: sticky; top: 96px; align-self: start`, sin JavaScript. Contiene configurador, **Agregar a cotización** y **Descargar ficha técnica** en secundario.

Reglas:

- El dato sin validar muestra "Por confirmar" y mantiene la lista `pending` existente. Las fotos referenciales conservan su rótulo.
- Las pestañas de especificaciones no animan altura.
- `@google/model-viewer` y los GLB se cargan solo al pulsar **Ver en 3D**, con `dynamic import` y altura reservada.
- La galería cambia de foto con opacidad, sin carrusel automático.

#### Industria (`/industrias` y `/industrias/saneamiento`, `/agricultura`, `/mineria`)

LCP: la foto del héroe, con `loading="eager"` y `fetchPriority="high"`. Acción principal: **Ver productos del sector**.

1. Héroe `.on-dark`: foto real, velo plano al 68 %, H1, frase y botón. Alto `min(640px, 80svh)`. Se retiran `sa-hero__glint` y los velos con degradado.
2. Destacado: foto y texto en columnas 1 a 6 y 7 a 12.
3. Aplicaciones: filas alternas o rejilla de 3 con foto. Los números 01, 02, 03 se retiran porque no indican un orden.
4. Línea de productos: celdas de producto.
5. Documentación: filas.
6. Banda de cierre, sin foto.

`/industrias` usa los puntos 1, 3 y 6, con un bloque por sector. `/nosotros` sigue esta misma plantilla, sin el botón de sector.

En Agricultura el vídeo nunca es LCP: se pinta el póster y el vídeo arranca solo tras `load`, desde 1024 px, sin ahorro de datos y sin movimiento reducido. Se usa un solo elemento `<video>`, sin `loop` y sin el lienzo de `hero-motion.tsx`. Se reproduce una vez y se queda en el último fotograma.

#### Formulario (`/cotizar`, `/contacto`, formulario de `/reclamaciones`, `/carrito`)

LCP: el H1. Una sola acción principal: **Enviar solicitud** o **Registrar reclamo**.

1. Migas, H1 y una frase que diga qué ocurre al enviar. Si el canal es correo o WhatsApp, se dice.
2. Una columna de 640 px como máximo. Desde 1024 px, resumen de la solicitud fijo con `position: sticky` en las columnas 9 a 12.
3. Secciones separadas por cota. Sin tarjetas anidadas.
4. Validación al salir del campo. Al enviar con errores, resumen arriba con enlaces a cada campo, y foco en el resumen.
5. Durante el envío, el botón muestra indicador y texto, y conserva su ancho.
6. Confirmación: solo se muestra "enviado" si el guardado ocurrió. Nunca se inventa un folio. La confirmación usa `role="status"`.

#### Legal (`/terminos`, `/privacidad`, `/cookies`, `/mapa-del-sitio`, `/eliminar-cuenta`, `/reclamaciones`)

LCP: el H1. Acción principal: ninguna en textos legales, **Registrar reclamo** en `/reclamaciones` y el envío de la solicitud en `/eliminar-cuenta`.

1. Migas, H1 y fecha de última actualización solo si existe en el `copy`.
2. Desde 1024 px, índice fijo en columnas 1 a 3 y texto de 68 caracteres en columnas 5 a 12. En móvil, índice plegable arriba.
3. Tablas legales con cabecera real.
4. Se retiran las fotos de cabecera y las bandas de cierre con foto (`src/app/_legal/images.ts`). Esto reduce el peso y deja el H1 como LCP.
5. `/reclamaciones` muestra el formulario tras una introducción de dos frases. No exige cuenta.

Los textos legales no se reescriben sin aprobación del área legal.

#### Acceso (`/login`, `/registro`, `/recuperar`, `/restablecer`, `/verificar-correo`)

LCP: el H1. Una acción principal por paso.

- Móvil: una columna de 400 px como máximo, logotipo, H1 y formulario.
- Desde 1024 px: formulario a la izquierda en 440 px y panel plano `--c-primary-deep` a la derecha con el logotipo y la frase existente. Sin foto.
- Campos de 48 px. El botón de mostrar contraseña es de 44 px.
- Los errores se escriben en lenguaje claro, junto al campo, sin revelar si una cuenta existe.
- `Google` y `Facebook` van debajo del formulario como botones secundarios.

---

## 4. Frontend: movimiento

No existe un archivo llamado "prompt motion". Esta sección es esa dirección y se construye sobre `src/shared/motion`. No se añaden dependencias.

### 4.1 Tesis: "Compuerta"

El movimiento imita al mecanismo que FUNDIGSAC fabrica: recorrido vertical corto, frenado firme y parada limpia.

- **Momento focal único:** en portada, el timón que baja por el vástago de la válvula al cambiar de variante.
- **Continuidad:** lo que entra sube una distancia corta y se asienta. El contenido no entra de lado. La única capa lateral es el cajón del carrito.
- **Respuesta:** toda acción confirma en 200 ms o menos.

### 4.2 Reglas duras

1. **Solo se animan `transform` y `opacity`.** Tampoco se animan `width`, `height`, `top`, `left`, `margin`, `padding`, `gap`, `max-*`, `filter`, `backdrop-filter`, `clip-path`, `mask`, `box-shadow`, `background-position`, `stroke-dashoffset` ni propiedades personalizadas. Color, fondo y borde cambian al instante.
2. **El elemento LCP nunca se anima**, ni el H1, ni la imagen principal. Se pintan con opacidad 1, sin `animation`, sin `transition` y sin retraso.
3. **Sobre el pliegue la opacidad es 1 desde el primer fotograma.** Los elementos de apoyo solo pueden asentarse con `transform`. Ningún texto visible al cargar empieza en opacidad 0 ni 0,01.
4. **Sin bucles.** Solo gira un indicador de carga mientras hay una petición en curso.
5. **Sin animación ligada al desplazamiento.** Se retiran todas las de `animation-timeline`, que además no existen en Firefox.
6. **Sin `backdrop-filter`** en todo el sitio público. Cabeceras y barras fijas usan fondo sólido.
7. **Sin `pointermove`** para efectos.
8. El movimiento se interrumpe: un clic nuevo cancela el anterior. La salida dura entre el 60 y el 70 % de la entrada.
9. Sin JavaScript, sin `IntersectionObserver` o con movimiento reducido, todo el contenido queda visible.

### 4.3 Tokens y cambios en `motion.css`

```css
:root {
  --mo-ease: cubic-bezier(0.2, 0.7, 0.2, 1);       /* se mantiene */
  --mo-ease-out: cubic-bezier(0.16, 1, 0.3, 1);    /* llegadas, se mantiene */
  --mo-ease-in: cubic-bezier(0.4, 0, 1, 1);        /* salidas */
  --mo-ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);/* momento focal, se mantiene */
  --mo-press: 100ms;
  --mo-fast: 140ms;
  --mo-base: 200ms;
  --mo-overlay: 280ms;
  --mo-overlay-out: 180ms;
  --mo-reveal: 420ms;
  --mo-media: 520ms;
  --mo-focal: 640ms;
  --mo-rise: 16px;
  --mo-settle: 8px;
  --mo-step: 50ms;
}
```

| Elemento | Cambio |
|---|---|
| `--mo-side` y `data-reveal="left"` / `"right"` | Se retiran. En marcado existente, ambos usan `mo-up` |
| `@keyframes mo-media` | `from { opacity: 0; transform: translate3d(0, var(--mo-rise), 0); }`. Sin `clip-path` ni `scale` |
| Cascada `data-reveal="stagger"` | Tope en el 6.º hijo: `calc(min(var(--i, 0), 5) * var(--mo-step))`. Retraso máximo de 250 ms |
| `data-enter` | Se reemplaza por `@keyframes mo-enter { from { transform: translate3d(0, var(--mo-settle), 0); } }`, con `--mo-reveal`, `--mo-ease-out` y pasos de 50 ms. Sin opacidad |
| `data-enter > h1` y `[data-lcp]` | `animation: none`. Se elimina `mo-enter-lcp`. El atributo `data-lcp` se coloca en el contenedor de la imagen LCP |
| `@keyframes mo-pop` | `from { opacity: 0; transform: translate3d(0, var(--mo-settle), 0); }`. Sin `scale` |
| `data-results` | `mo-pop` en 200 ms con `--mo-ease-out`, pasos de 25 ms, tope en 100 ms |
| Avisos `role=alert` y `role=status` | `mo-pop` en 200 ms |
| `.mo-progress` | Fondo sólido `--c-sky` sobre `--c-primary-deep`, sin degradado ni sombra. Sigue usando `scaleX` |
| Motor `motion-root.tsx` | Se conserva tal cual: 1,3 KB comprimidos, un solo observador, sin parpadeo sobre el pliegue |

Hover de botones y celdas: capa `::after` con `opacity` en `--mo-fast`. Imagen de celda: `transform: scale(1.02)` en `--mo-base`, solo con `@media (hover: hover)`.

Selector de variante del héroe, solo con `transform`. El contenedor de la válvula entrante tiene `overflow: hidden` y una máscara estática de borde suave. El contenedor recorre `translateY(-100%)` hasta 0 mientras la imagen interior recorre `translateY(100%)` hasta 0, ambos en `--mo-focal` con `--mo-ease-in-out`. El cuerpo es idéntico al píxel en las dos fotos, de modo que solo se percibe el accionamiento superior.

### 4.4 Prompt motion por pantalla

Cada fila es la instrucción completa. "Fijo" significa que el elemento se pinta en su estado final desde el primer fotograma y no se anima.

Clave de recetas:

| Receta | Duración | Curva | Propiedades | Cascada |
|---|---:|---|---|---|
| `mo-up` | 420 ms | `--mo-ease` | Opacidad y `translateY(16px)` a 0 | n/a |
| `mo-media` | 520 ms | `--mo-ease-out` | Opacidad y `translateY(16px)` a 0 | n/a |
| `stagger` | 420 ms | `--mo-ease` | Igual que `mo-up` | 50 ms, tope 250 ms |
| `data-enter` | 420 ms | `--mo-ease-out` | Solo `translateY(8px)` a 0 | 50 ms |
| `data-results` | 200 ms | `--mo-ease-out` | Opacidad y `translateY(8px)` a 0 | 25 ms, tope 100 ms |
| `mo-pop` | 200 ms | `--mo-ease-out` | Opacidad y `translateY(8px)` a 0 | n/a |

| Pantalla | Al cargar | Al desplazar | Al interactuar | Foco |
|---|---|---|---|---|
| Cabecera | Sin animación | Se oculta y vuelve con `translateY`, `--mo-base`, `--mo-ease`. Fondo sólido por opacidad de `::before` en `--mo-fast` | Submenú: opacidad y `translateY(-4px)` a 0, `--mo-base`, salida `--mo-fast`. Subrayado con `scaleX` en `--mo-fast`. El buscador abre un panel propio de 64 px, opacidad y `translateY`, `--mo-base`, sin animar anchos | Ninguno |
| Menú móvil | n/a | n/a | Panel `translateY(-8px)` a 0 con opacidad, `--mo-overlay`, grupos en cascada de 30 ms con tope 150 ms. Salida `--mo-overlay-out`. Icono X con `rotate(90deg)` en `--mo-base` | Ninguno |
| Pie | Sin animación | Sin animación | Libro de Reclamaciones: capa `::after` en `--mo-fast` | Ninguno |
| Inicio | H1, válvula y entradilla fijos. Botones con `data-enter`, solo `transform` | Familias con `stagger`. Sectores: texto con `mo-up`, pasos 90 ms, foto fija. Respaldo y Documentación: foto `mo-media`, texto `mo-up` | Selector de variante según §4.3. Celda: `::after` e imagen 1,02 | Timón por el vástago, 640 ms, solo al pulsar |
| Catálogo | H1 y barra de filtros fijos | Celdas bajo el pliegue con `stagger` | Al filtrar: `data-results`, 200 ms, solo las celdas nuevas. Agregar a cotización: icono de confirmación con `scale(0.8)` a 1 y opacidad, `--mo-base` | Ninguno |
| Familia | H1 fijo. Pestañas con `data-enter` | Celdas y filas con `stagger`, documentos con `mo-up` | Pestaña con indicador `scaleX` en `--mo-base`. Contenido nuevo con `mo-pop` | Ninguno |
| Ficha | H1 y primera foto fijos. Panel de decisión con `data-enter` | Tabla técnica y plano con `mo-up`, una vez | Galería: opacidad cruzada en `--mo-base`. Especificaciones: opacidad y `translateY(-4px)`, sin animar altura. Configurador: cambio de texto inmediato con `mo-pop` en el resumen. Plano: líneas con opacidad, sin trazo progresivo | Ninguno |
| Industria | H1 y foto fijos. Botones con `data-enter` | Destacado: foto `mo-media`, texto `mo-up`. Aplicaciones y línea con `stagger` | Celda: `::after` e imagen 1,02 | Ninguno |
| Nosotros | H1 fijo | Bloques con `mo-up`. Línea de tiempo: cada hito con opacidad y `translateY`, pasos de 90 ms | Ninguna especial | Ninguno |
| Contacto | H1 fijo | Mapa y datos con `mo-up`. Se retiran la cortina y el mapa con `clip-path` | Campos sin animación | Ninguno |
| Cotizar | H1 fijo. Pasos con `data-enter` | Secciones con `mo-up` | Error con `mo-pop`. Botón: indicador giratorio solo durante el envío | Ninguno |
| Confirmación y carrito | H1 fijo | Sin animación | Cajón del carrito: `translateX(100%)` a 0, `--mo-overlay`, salida `--mo-overlay-out`. Fila retirada: opacidad en `--mo-fast`, sin colapsar altura animada | Ninguno |
| Reclamaciones | H1 fijo | Formulario sin animación | Error y confirmación con `mo-pop` | Ninguno |
| Legales | H1 fijo | Sin revelado. El texto legal está visible desde el inicio | Índice: resaltado inmediato | Ninguno |
| Eliminar cuenta | H1 fijo | Sin revelado | Confirmación: icono con opacidad y `scale`, `--mo-base`. Sin trazos ni anillos | Ninguno |
| Acceso | H1 fijo. Formulario con `data-enter` | n/a | Error con `mo-pop`. Botón con indicador durante el envío. Sin `ac-pop` | Ninguno |
| 404 | H1 fijo. Enlaces con `data-enter` | n/a | Ninguna especial | Ninguno |
| Asistente | Lanzador sin bucles ni halo | n/a | Panel `translateY(8px)` y opacidad, `--mo-overlay`. La mascota solo se anima con el panel abierto y nunca durante la carga inicial | Ninguno |
| Banner de cookies | Sin animación. Espacio fijo fuera del flujo | n/a | Salida con opacidad, `--mo-overlay-out` | Ninguno |
| Toast | n/a | n/a | `translateY(8px)` y opacidad, `--mo-base`. Salida `--mo-fast` | Ninguno |
| Navegación entre páginas | `NavProgress` tras 140 ms, igual que hoy | n/a | Sin `ViewTransition`. Se descartó el 2026-10-16 porque fundía a blanco | Ninguno |

`LegalMotion` y sus coreografías (`main.lg`) se retiran de `/terminos`, `/privacidad`, `/cookies`, `/mapa-del-sitio`, `/eliminar-cuenta` y `/reclamaciones`. `/nosotros` y `/contacto` pasan al sistema común.

### 4.5 Movimiento reducido

Se conserva la regla global de `globals.css`, ya verificada en 31 rutas por 4 anchos con 0 desplazamientos.

| Elemento | Con `prefers-reduced-motion: reduce` |
|---|---|
| Revelados | El motor no se arma: todo visible |
| `data-enter` | Sin movimiento |
| Selector de variante | Cambio inmediato de imagen |
| Menú, submenú, cajón, diálogo | Aparecen sin recorrido |
| Indicador de carga | Sin giro. Se muestra texto "Enviando…" |
| Confirmaciones y errores | Visibles de inmediato, con icono y texto |
| `NavProgress` | Línea fija al 70 % de opacidad, como hoy |
| Vídeo de Agricultura | No se reproduce, queda el póster |
| Movimiento de la cabecera al desplazar | Sin recorrido: permanece visible |
| Mascota del asistente | Estática |
| Hover | Cambio inmediato |

### 4.6 Presupuesto de movimiento

| Límite | Valor | Comprobación |
|---|---:|---|
| JavaScript nuevo para movimiento | 0 KB | Sigue solo `motion-root.tsx` |
| CSS de movimiento por ruta | ≤ 3 KB comprimidos | Peso del CSS |
| Bibliotecas de animación | 0 | `package.json` |
| Duración máxima | 640 ms en foco, 520 ms en foto, 420 ms en revelado, 200 ms en interfaz | `motion.css` |
| Retraso máximo de cascada | 250 ms | `motion.css` |
| Animaciones vivas a los 250 ms de cargar, 1440 px | ≤ 8 por ruta | `motion-audit.mjs` (hoy 48 en portada) |
| Animaciones infinitas al cargar | 0 | `motion-audit.mjs` |
| Propiedades animadas | Solo `transform` y `opacity` | Comandos de §4.7 |
| Contribución del movimiento al CLS | 0 | `kpi-gate.mjs` |
| Retraso sobre el elemento LCP | 0 ms | Inspección de CSS y traza |
| Respuesta visible a una acción | ≤ 100 ms desde la entrada | Traza con CPU ×4 |

### 4.7 Deuda que se retira al rediseñar

Medido en `Frontend/src` el 2026-11-09: 30 `@keyframes` con propiedades no permitidas y 200 de 300 declaraciones `transition` fuera de `transform` y `opacity`. Hay bucles infinitos en 11 hojas: `landing.css`, `home-motion.css`, `sector.css`, `agricultura.css`, `deletion.css`, `access.css`, `w03-valvulas.module.css`, `assistant-panel.css`, `assistant.css`, `cart.css` y `pages.css`.

**Cada plantilla rediseñada sale con cero excepciones.** Comprobación sobre las hojas tocadas:

```bash
grep -nE "transition(-property)?:[^;]*(width|height|top|left|right|margin|padding|max-|gap|filter|box-shadow|background|border|color|clip-path|mask)" <hojas>
grep -nE "animation-timeline|backdrop-filter|infinite|clip-path:.*inset|linear-gradient|radial-gradient" <hojas>
```

Ambos comandos deben devolver cero líneas, salvo el giro de un indicador de carga. Una máscara estática sin animar es válida.

Prioridad por efecto en LCP: `home-motion.css` (entrada del héroe, palabras con `filter`, `lp-kenburns`, `lp-float`, `lp-shutter`, `lp-curtain`, derivas ligadas al scroll), `landing.css` (`backdrop-filter`, `lp-wa-pulse`, búsqueda con `max-width`), `motion.css` (`mo-media`), `contact.css`, `industrias.css`, `sector.css`, `w06-ficha.module.css`, `pages.css`, `deletion.css`, `assistant-panel.css`.

---

## 5. Libro de Reclamaciones

Objetivo: que cualquier persona lo identifique y llegue a `/reclamaciones` en un paso desde cualquier página, sin cuenta. Este diseño no es una interpretación jurídica. El área legal debe validar ubicación, denominación y contenido (`Report/README.md` §11.4 y §18).

### 5.1 Icono

Archivo nuevo `Frontend/src/shared/ui/libro-reclamaciones-icon.tsx`. Libro abierto con lomo y tres líneas por página. Se comprobó su lectura a 20, 24, 40, 64 y 150 px sobre blanco y sobre `#002b3a`.

```tsx
export function LibroReclamacionesIcon({ size = 24 }: { size?: number }) {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 48 48" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true" focusable="false">
      <path d="M24 12.5C20 9 13.5 8 5 8.5v29.8c8.5-.5 15 .5 19 4 4-3.5 10.5-4.5 19-4V8.5c-8.5-.5-15 .5-19 4Z" />
      <path d="M24 12.5v29.8" />
      <path d="M11 16.2c3.2 0 5.8.5 8 1.6" />
      <path d="M11 23c3.2 0 5.8.5 8 1.6" />
      <path d="M11 29.8c3.2 0 5.8.5 8 1.6" />
      <path d="M37 16.2c-3.2 0-5.8.5-8 1.6" />
      <path d="M37 23c-3.2 0-5.8.5-8 1.6" />
      <path d="M37 29.8c-3.2 0-5.8.5-8 1.6" />
    </svg>
  );
}
```

### 5.2 Nombre

El nombre oficial se muestra siempre en español y con mayúsculas: **Libro de Reclamaciones**. Cambios en `home-copy.ts`:

| Clave | Español | Inglés |
|---|---|---|
| `footer.complaints` | `Libro de Reclamaciones` | `Libro de Reclamaciones` |
| `footer.complaintsHint`, nueva | `Registra tu reclamo o queja` | `Complaints book` |

El mismo nombre se aplica en `src/app/_legal/sitemap-copy.ts`.

### 5.3 Pie: ubicación principal

En `LandingFooter`, dentro de `.lp-footer__brand-column`, debajo del párrafo. Se retira el enlace de `.lp-footer__legal` para no duplicarlo.

```tsx
<IntentLink className="lp-claims" href="/reclamaciones">
  <LibroReclamacionesIcon size={40} />
  <span>
    <strong>{f.complaints}</strong>
    <small>{f.complaintsHint}</small>
  </span>
</IntentLink>
```

```css
.lp-footer a.lp-claims {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  max-width: 320px;
  min-height: 72px;
  margin-top: 20px;
  padding: 12px 16px;
  border-radius: 6px;
  background: #ffffff;
  color: #004257;
  font-size: 16px;
  text-decoration: none;
  transition: none;
}
.lp-footer a.lp-claims:hover { color: #004257; }
.lp-claims svg { flex: none; }
.lp-claims strong { display: block; font-size: 16px; line-height: 22px; font-weight: 600; }
.lp-claims small { display: block; font-size: 14px; line-height: 20px; color: #41484c; }
.lp-claims:hover strong { text-decoration: underline; text-underline-offset: 3px; }
```

La placa es blanca sobre `--c-primary-deep` en ambos temas. El texto petróleo sobre blanco da 10,96:1, y el texto de apoyo `#41484c` sobre blanco da 9,31:1. En móvil ocupa el ancho completo.

### 5.4 Cabecera de escritorio

Desde 1261 px, botón de icono en `.lp-header__actions`, inmediatamente después de `.lp-search`:

```tsx
const { complaints } = useHome().footer; // dentro de LandingHeader

<IntentLink href="/reclamaciones" className="lp-icon-btn lp-claims-btn" aria-label={complaints} title={complaints}>
  <LibroReclamacionesIcon size={24} />
</IntentLink>
```

`.lp-claims-btn` fija `height: 44px; min-width: 44px` y se oculta por debajo de 1261 px. Mismo tratamiento de color que los otros iconos. Para hacer espacio, el enlace **Inicio** sale de la navegación de escritorio, porque el logotipo ya lleva a la portada. Se conserva en el menú móvil. Se comprueba que no haya desborde a 1261, 1366 y 1440 px.

### 5.5 Menú móvil

En `.lp-mobile`, inmediatamente antes de `.lp-mobile__prefs`. Fila de enlace con icono de 24 px, 16/24 peso 600, alto de 56 px, líneas de 1 px arriba y abajo, y color `--c-action`. Texto: `Libro de Reclamaciones`.

### 5.6 Aceptación

- Visible con icono y nombre en el pie de todas las rutas.
- Accesible en un toque desde el menú móvil y en un clic desde la cabecera de escritorio.
- El enlace funciona sin sesión y lleva a `/reclamaciones`.
- Nombre accesible correcto en los tres puntos, y foco visible.
- Contraste de 4,5:1 o más en texto y 3:1 o más en el icono, en temas claro y oscuro.
- KPI en verde según §1.

---

## 6. Admin: dirección

Modo de trabajo: operar. Las personas son del personal comercial, legal y de catálogo, sin perfil técnico. El panel responde a una pregunta: **qué tengo que hacer ahora**.

Se conserva la dirección "registro industrial" de `Admin/src/styles/tokens.css`, elegida por el usuario el 2026-10-20, junto con su marco gris, hoja blanca y regla de tinta. De `direction.json` se conservan las medidas de hoja, las filas y la disposición móvil. La lista de KPI con gráfico y riel lateral de esa plantilla deja de ser la portada.

### 6.1 Arquitectura

Pasa de 9 elementos en 3 grupos a **4 elementos sin grupos**. Las rutas existentes no cambian, solo su lugar en el menú. Cada persona ve solo lo que su rol permite, según `src/data/permissions.ts`.

| Menú | Ruta inicial | Contenido | Permiso |
|---|---|---|---|
| **Inicio** | `/panel` | Lista de tareas del día | Todo el personal |
| **Solicitudes** | `/cotizaciones` | Pestañas: Cotizaciones (`/cotizaciones`), Consultas (`/consultas`), Reclamos (`/reclamaciones`), Datos personales (`/privacidad`) | Pestañas según `quote:read`, `inquiry:read`, `complaint:read`, `privacy:read` |
| **Cuentas** | `/usuarios` | Clientes y personal | `users:manage` |
| **Ajustes** | `/configuracion` | Mis preferencias para todos. Solo administración: Avisos, Qué puede hacer cada persona (`/roles`), Historial de cambios (`/actividad`) | Según rol |

Barra superior, de izquierda a derecha: título de la pantalla, campo **Buscar por nombre, correo o código** y **Ayuda**.

Se retiran de la vista principal: etiqueta `Ctrl K` (la paleta sigue disponible por teclado), selector de idioma y tema (pasan a Mis preferencias), densidad compacta y `InfoTip` sobre cifras.

En teléfono no hay menú lateral: barra inferior fija con los 4 elementos, 64 px de alto, icono de 24 px y etiqueta de 13 px, con `env(safe-area-inset-bottom)`.

### 6.2 Lenguaje

Se aplica en `src/lib/i18n/es.ts` y `cases-es.ts`.

| Actual | Nuevo |
|---|---|
| Resumen | Inicio |
| Usuarios | Cuentas |
| Atención, Casos | Solicitudes |
| Reclamaciones (menú) | Reclamos |
| Privacidad (menú) | Datos personales |
| Actividad | Historial de cambios |
| Roles y permisos | Qué puede hacer cada persona |
| Configuración | Ajustes |
| Pendiente (cuenta) | Falta confirmar correo |
| Suspendido | Bloqueada |
| Activo | Activa |
| Método | Cómo se registró |
| Rol (columna) | Puesto |
| Reenviar | Reenviar correo |
| `catalog:read` y demás claves | Frase: "Puede ver el catálogo" |

Reglas de redacción: frases cortas en segunda persona, verbos concretos en los botones, y ni jerga técnica ni siglas sin explicar (RUC y DNI se mantienen). Cada error dice qué pasó y qué hacer.

### 6.3 Una acción principal por pantalla

| Pantalla | Botón principal, único con fondo petróleo |
|---|---|
| Inicio | Atender lo más urgente |
| Solicitudes, lista | Atender la siguiente |
| Solicitud, detalle | Responder, o el siguiente paso de su estado |
| Cuentas, lista | Agregar persona |
| Cuenta, detalle | Según estado: Reenviar correo, Reactivar cuenta o Guardar cambios |
| Ajustes | Guardar cambios, fijo al pie y activo solo si hay cambios |
| Acceso | Enviar código, y luego Entrar |

Las demás acciones son secundarias o van en un menú. Las irreversibles exigen confirmación, con la consecuencia escrita. Bloquear una cuenta usa el color de error y nunca es el botón principal.

### 6.4 Inicio orientado a tareas

`overview-view.tsx`, de arriba hacia abajo:

1. H1 **Para hoy** y una frase con plantilla: `Tienes {n} cosas por atender.` o `Tienes 1 cosa por atender.`. El número sale de `useQueueCounts`.
2. Botón **Atender lo más urgente**, que abre el primer elemento.
3. Lista ordenada: primero los plazos legales que vencen en 3 días hábiles o menos, después lo más antiguo. Máximo 7 filas y enlace **Ver todas**. Cada fila tiene una frase con el dato real (`Reclamo {código}, vence en {n} días hábiles`), un estado con marca y texto, y el botón **Atender**. Filas de 64 px.
4. Tres accesos con cifra real: Cotizaciones nuevas, Consultas sin responder, Cuentas por verificar. Solo los que el rol puede usar.
5. `<details>` **Ver números del mes**, cerrado por defecto. Contiene los KPI y gráficos actuales, cargados con `dynamic import` al abrir.

Estado vacío: "Todo al día. No tienes nada pendiente.", sin botón y con la misma altura mínima que la lista. No se inventan cifras: mientras cargan, bloques con altura reservada.

### 6.5 Tablas que pasan a tarjetas

Desde 721 px, tabla semántica con cabeceras visibles y filas de 56 px. Se quitan las columnas que estén vacías en todas las filas. El menú `kebab` se sustituye por el botón **Abrir**.

Hasta 720 px, cada fila es una tarjeta, sin duplicar el DOM. Sustituye a las reglas actuales de lista de dos líneas y aplica a `.table`, usada en `users-table.tsx` y `case-list.tsx`:

```css
@media (max-width: 720px) {
  .table, .table tbody { display: block; }
  .table thead { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
  .table tr {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 4px 12px;
    padding: 16px;
    border: 1px solid var(--border);
    border-radius: var(--radius-card);
    margin-bottom: 8px;
  }
  .table td { display: block; padding: 0; }
  .table td[data-primary] { grid-column: 1 / -1; font-size: 16px; font-weight: 600; }
  .table td[data-label]::before { content: attr(data-label) ": "; color: var(--muted); }
  .table td[data-action] { grid-column: 1 / -1; margin-top: 8px; }
  .table td[data-action] .btn { width: 100%; min-height: 48px; }
}
```

Al usar `display` distinto de tabla se conservan `role="table"`, `row`, `columnheader` y `cell` en el marcado. Cada tarjeta muestra como máximo 4 datos: identidad, estado, fecha o plazo, y un dato propio de la lista. Filtros en una fila con desplazamiento propio, de 44 px.

### 6.6 Tokens que cambian

En `Admin/src/styles/tokens.css`, tema claro:

```css
--primary: #004257;
--primary-hover: #00303f;
--fs-title: 24px;
--fs-label: 13px;
--fs-body: 15px;
--fs-small: 13px;
--control-h: 40px;
--row-h: 56px;
```

- En teléfono, `--control-h: 48px`.
- Se retira `:root[data-density="compact"]`.
- Área táctil mínima de 44 px, por encima de los 36 px actuales.
- El tema oscuro conserva sus valores.

### 6.7 Movimiento

| Elemento | Receta |
|---|---|
| Carga de pantalla | Sin animación. Se retiran `.route` y `.stagger` |
| Cifras | Sin conteo. Se retira `AnimatedNumber` |
| Gráficos | Sin crecimiento animado |
| Pestañas | Indicador `scaleX`, 150 ms, `--ease` |
| Diálogo | Opacidad y `translateY(8px)`, 200 ms. Salida 140 ms |
| Toast | Opacidad y `translateY(8px)`, 200 ms |
| Botón al presionar | `translateY(1px)`, 120 ms |
| Movimiento reducido | Todo inmediato |

Solo `transform` y `opacity`. KPI en verde según §1, con móvil y escritorio.

---

## 7. Stock-Web-Automate: dirección

App de campo para registrar entradas y salidas de EPP desde el celular, con guantes, a pleno sol y con mala señal. Debe poder usarse sin leer instrucciones.

### 7.1 Principios

1. Una pregunta por pantalla.
2. Pulgar primero: la acción principal va abajo, al alcance.
3. El estado de conexión y lo que falta subir se ven siempre.
4. Guardar en el celular nunca depende de la red.

### 7.2 Banda de estado

Fija arriba, **56 px, a todo el ancho, visible en todas las pantallas**, también durante un registro. Altura reservada desde el primer pintado. `role="status"`. Al tocarla abre **Por subir**. Los datos salen de `useEnLinea()` y `useRespaldo()`, ya existentes. No se usa `navigator.onLine` solo.

Se aplica el primer caso que coincida:

| Prioridad | Condición | Fondo y texto | Icono | Mensaje |
|---:|---|---|---|---|
| 1 | Hay registros `porRevisar` | `#b3261e`, blanco (6,54:1) | `AlertTriangle` | `{n} por revisar` |
| 2 | Sin conexión y `faltaSubir` > 0 | `#ffc247`, `#2b1a00` (10,44:1) | `WifiOff` | `Sin conexión · {n} por subir` |
| 3 | Sin conexión y nada por subir | `#ffc247`, `#2b1a00` | `WifiOff` | `Sin conexión · Puedes seguir registrando` |
| 4 | En línea y subiendo | `#0972a1`, blanco (5,34:1) | `UploadCloud` | `Subiendo {n}…` |
| 5 | En línea y `faltaSubir` > 0 | `#0972a1`, blanco | `UploadCloud` | `{n} por subir · Subir ahora` |
| 6 | En línea y nada por subir | `#14663f`, blanco (7,00:1) | `CheckCircle2` | `En línea · Todo subido` |

Texto de 17 px, peso 600, cifras con `tabular-nums`.

### 7.3 Navegación móvil

Barra inferior de 4 elementos, 72 px más `env(safe-area-inset-bottom)`, fondo sólido sin desenfoque, etiqueta de 14 px, icono de 28 px.

| Elemento | Contenido |
|---|---|
| **Registrar** | Pantalla inicial |
| **Stock** | Buscar cuánto queda de un producto y talla |
| **Por subir** | Registros de este celular. Distintivo con el número, siempre visible si es mayor que 0 |
| **Más** | Movimientos, Trabajadores, Informes PDF, Reporte semanal, Cuenta, Empresa |

Se retiran en móvil: botón flotante **Registrar**, botón flotante del asistente y campana en la cabecera. El asistente pasa a un botón secundario en **Registrar**. Sin conexión aparece desactivado con el texto "Necesita conexión". Resumen y gráficos solo en escritorio, cargados bajo demanda. En escritorio se mantiene la barra lateral.

### 7.4 Pantalla Registrar

Título "¿Qué vas a registrar?". Dos botones a todo el ancho, de **120 px de alto**, con icono de 40 px y texto de 22 px, peso 600:

- **Entregar a un trabajador** (salida), fondo `#004257`, texto blanco.
- **Ingresar a almacén** (entrada), fondo blanco, borde de 2 px `#004257`, texto `#004257`.

Debajo, los últimos 3 registros de este celular, con su estado.

### 7.5 Flujo por pasos

Pantalla completa, sin diálogos encimados. Arriba: botón **Atrás** de 56 px y "Paso 2 de 4". Abajo, fijo: un solo botón de 64 px. Es el único botón principal de la pantalla.

| Paso de salida | Pregunta | Control |
|---:|---|---|
| 1 | ¿Quién recibe? | Buscador y lista de filas de 64 px, con los recientes primero |
| 2 | ¿Qué le entregas? | Producto en filas de 64 px, talla en botones de 56×56 px, cantidad con botones − y + de 64×64 px y cifra de 40 px |
| 3 | Toma la foto | Botón de cámara de 120 px y vista previa con alto reservado. La foto es obligatoria |
| 4 | Revisa y guarda | Resumen en texto de 18 px y botón **Guardar** |

La entrada usa los pasos: ¿Qué ingresa?, Cantidad, y Revisa y guarda.

Al guardar:

- Sin conexión: "Guardado en este celular. Se subirá solo cuando haya conexión."
- Con conexión y subida confirmada: "Guardado y subido."
- Botón **Registrar otro**, y enlace **Ir al inicio**.

Si falta espacio en el dispositivo (`SinEspacioError`), se dice con claridad y no se pierde lo escrito.

### 7.6 Pantalla Por subir

Filas de 72 px con producto, cantidad, trabajador, hora y estado:

| Estado interno | Texto |
|---|---|
| `pendiente` | Esperando conexión |
| `subiendo` | Subiendo |
| `sin_migracion` | Esperando actualización del sistema |
| `confirmado` | Subido |
| `rechazado` | No se pudo subir, con el motivo y el botón **Reintentar** de 56 px |

Vacío: "Todo subido. No hay nada pendiente en este celular."

### 7.7 Tokens

Sustituyen a la paleta "Slab" de `src/index.css`. Conservan los nombres en uso para no romper clases como `bg-ink` o `text-warn`.

```css
@theme {
  --font-sans: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-display: var(--font-sans);
  --color-ground: #f1f5f7;
  --color-surface: #ffffff;
  --color-ink: #0b1d26;
  --color-ink-2: #1b2b35;
  --color-muted: #3f4f59;
  --color-faint: #56646e;
  --color-line: #c9d3d9;
  --color-line-2: #dfe6ea;
  --color-action: #004257;
  --color-info: #0972a1;
  --color-red: #b3261e;
  --color-red-soft: #fdecea;
  --color-ok: #14663f;
  --color-ok-soft: #e4f4ec;
  --color-warn: #7a4a00;
  --color-warn-soft: #fff4d6;
  --color-band-offline: #ffc247;
  --color-on-band-offline: #2b1a00;
}
```

Los botones principales pasan de `bg-ink` a `bg-action`.

- Se usa fuente del sistema: 0 KB, sin dependencia de red y sin saltos de diseño. Se eliminan los enlaces a Google Fonts de `index.html`, que bloquean el pintado y fallan sin conexión, y también Fraunces y la clase `.display`.
- Texto: 18/26 en el cuerpo, 16 en secundarios, 24 en títulos. Mínimo de 14 px en toda la app. Hoy hay etiquetas de 10,5 y 11 px.
- Contraste: `#0b1d26` sobre blanco 17,24:1, `#3f4f59` sobre `#f1f5f7` 7,74:1, `#7a4a00` sobre `#fff4d6` 6,83:1.
- Objetivos táctiles: 56 px como mínimo, 64 px en acción principal, 12 px entre objetivos. `touch-action: manipulation`.
- Radios: 6 px en controles, 8 px en bloques. Sin sombras ni `backdrop-blur`.
- `theme-color` igual a `#004257`.

### 7.8 Movimiento

| Elemento | Receta |
|---|---|
| Cambio de paso | Opacidad y `translateY(8px)`, 160 ms, `cubic-bezier(0.16, 1, 0.3, 1)` |
| Botón al presionar | `scale(0.98)`, 100 ms |
| Confirmación | Icono con opacidad y `scale(0.8)` a 1, 200 ms |
| Punto "en vivo", `shimmer` de carga | Se retiran. Bloques fijos con altura reservada |
| Isla de reporte semanal | Sin resortes. Pasa a **Más** |
| Movimiento reducido | Todo inmediato |

Se retira `framer-motion` y se usa CSS. Solo `transform` y `opacity`.

### 7.9 Presupuesto

- JS inicial ≤ 150 KB comprimidos, con objetivo de 120 KB.
- Bajo demanda: `Asistente`, `Reportes` y `jspdf`, `MovChart` y `recharts`, `mammoth`, `read-excel-file`.
- KPI en verde según §1, con 5 corridas y `--no-seo`.
- Prueba manual: registrar en modo avión, volver a la red y confirmar el conteo.

---

## 8. Orden de implementación y aceptación

| Paso | Trabajo | Verificación |
|---:|---|---|
| 1 | Tokens de `globals.css`, puente `--lp-*`, fuente Plex y `motion.css` | KPI en las 4 rutas base |
| 2 | Libro de Reclamaciones | §5.6 |
| 3 | Inicio, con retirada de la deuda del héroe | LCP móvil ≤ 2,5 s |
| 4 | Catálogo, familia, ficha | KPI en esas rutas |
| 5 | Industria, formularios, legal y acceso | KPI en esas rutas |
| 6 | Asistente, carrito y resto de capas globales | JS inicial ≤ 150 KB |
| 7 | Admin | §6 y KPI |
| 8 | Stock-Web-Automate | §7 y KPI |

Se mide en cada paso, no solo al final, según §1.3.

Lista de aceptación por plantilla:

- [ ] Un elemento LCP sin animación y una sola imagen con prioridad.
- [ ] Una acción principal.
- [ ] Solo `transform` y `opacity`, según §4.7.
- [ ] Sin degradados decorativos, `backdrop-filter`, bucles ni `pointermove`.
- [ ] Movimiento reducido según §4.5.
- [ ] Sin datos comerciales nuevos.
- [ ] Imágenes con espacio reservado.
- [ ] Teclado, foco, objetivos de 44 px, contraste AA y tema oscuro.
- [ ] Sin desborde en 320, 390, 768, 1024, 1261, 1440 y 1920 px.
- [ ] Todos los KPI de §1.1 en verde, con tabla antes y después.

---

## 9. Puntos abiertos

| Punto | Estado | Quién decide |
|---|---|---|
| Medición de INP y de peso de JS | `kpi-gate.mjs` no los calcula. Hasta que exista un script, se usan los métodos de §1.1 | Equipo técnico |
| Umbral de `kpi-gate.mjs` | Aprueba desde 90. Los objetivos de Accessibility y SEO son 95 | Equipo técnico |
| Vistas de `Admin` con sesión | `kpi-gate.mjs` no inicia sesión | Equipo técnico |
| Ubicación y denominación del Libro de Reclamaciones | Requiere validación jurídica | Área legal |
| Texto justificado en móvil (`globals.css` línea 319) | Se conserva porque es una decisión previa. Dificulta la lectura en pantallas angostas | Responsable del proyecto |
| Botón naranja a petróleo | Decidido en este brief por la identidad corporativa y porque el blanco sobre naranja da 3,06:1 | Responsable del proyecto puede revisarlo |
| Vídeo de Agricultura en bucle | Pasa a una sola reproducción por la regla de cero bucles | Responsable del proyecto puede revisarlo |
| Dato de campo P75 | Solo tras un despliegue autorizado | Responsable del proyecto |
