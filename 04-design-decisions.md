# 04 · Decisiones de diseño

Fecha: 2026-11-10. Parte de las ideas de `03-design-inspiration.md` y `Report/diseno/referencias.md`. Toda decisión queda sujeta a `Report/diseno/BRIEF_DISENO.md`, que manda en caso de conflicto. Nada se da por aprobado hasta medir los KPI del brief §1.1 en verde, en móvil y escritorio.

## Cómo se puntúa

Cada criterio va de 1 a 5. Un 5 es siempre lo mejor: en costo, 5 significa barato; en rendimiento, 5 significa que no afecta a los KPI.

- **Impacto**: comercial en Frontend y operativo en Admin y Stock.
- **Marca**: coherencia con la "lámina técnica" y con los colores reales del logotipo.
- **Costo**: horas de trabajo y archivos tocados.
- **Rend.**: efecto previsto sobre LCP, CLS, INP y JS inicial.
- **Mant.**: mantenibilidad, es decir, sin dependencias nuevas y con tokens existentes.

Corte: se selecciona con total ≥ 19 y ningún criterio por debajo de 3.

## Frontend (sitio público)

| Idea | Origen | Impacto | Marca | Costo | Rend. | Mant. | Total | Decisión |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Animación de entrada "Línea de presión" | magicui (Animated Beam), promptmotion (SVG) | 4 | 5 | 4 | 4 | 4 | 21 | **Seleccionada**. Ver la sección de entrada |
| Control de pausa visible en el video de Agricultura | promptmotion, smoothui | 3 | 4 | 5 | 5 | 5 | 22 | **Seleccionada**. Cumple WCAG 2.2.2 |
| Barra de catálogo: familia, búsqueda y orden en una fila de 44 px | promptmotion | 5 | 4 | 3 | 4 | 4 | 20 | **Seleccionada**. Sin `backdrop-filter` |
| Ficha en dos paneles con plano o foto fija (`sticky`) | dbdiagram, referencias (refero) | 5 | 5 | 3 | 4 | 4 | 21 | **Seleccionada**. Orden de lectura correcto en móvil |
| Plano de válvula por capas que se muestran u ocultan | promptmotion (despiece) | 4 | 5 | 2 | 4 | 3 | 18 | Descartada por ahora: costo alto. Se retoma con el SVG que entregue Ingeniería |
| Retícula de papel técnico solo con CSS | magicui (Grid Pattern) | 2 | 4 | 5 | 5 | 5 | 21 | **Seleccionada**, solo en el plano de la ficha. No en el héroe |
| Lista de documentos: icono, nombre, tipo y peso | promptmotion, getdesign.md | 4 | 4 | 4 | 5 | 5 | 22 | **Seleccionada** |
| Mapa de cobertura con puntos | magicui (Dotted Map) | 3 | 3 | 3 | 4 | 4 | 17 | Descartada: requiere zonas validadas por Comercial |
| Contador numérico, Marquee, Border Beam | magicui | 2 | 1 | 4 | 3 | 4 | 14 | Descartadas: bucles, brillos y cifras no validadas |
| Bloques Stats y Logo Clouds | smoothui | 3 | 2 | 4 | 4 | 4 | 17 | Descartados: no hay datos comerciales validados (brief §2) |

## Admin (panel del personal)

| Idea | Origen | Impacto | Marca | Costo | Rend. | Mant. | Total | Decisión |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Animación de entrada "Regla de tinta" | getdesign.md (regla), animate-ui (Progress) | 2 | 5 | 5 | 5 | 4 | 21 | **Seleccionada** |
| Guardar: "Guardando…" y luego "Guardado" con icono, 200 ms | animate-ui | 4 | 4 | 4 | 5 | 5 | 22 | **Seleccionada** |
| Botón Copiar junto a código, RUC y correo, anunciado por `aria-live` | promptmotion | 4 | 4 | 4 | 5 | 5 | 22 | **Seleccionada** |
| Pestañas de Solicitudes con contador real | getdesign.md | 4 | 4 | 4 | 5 | 4 | 21 | **Seleccionada**. Ya existe en parte (`sectionWaiting`) |
| Fila atendida que sale con opacidad en 140 ms | animate-ui | 3 | 4 | 4 | 5 | 4 | 20 | **Seleccionada**, sin animar la altura |
| Filtros guardados ("Mis reclamos que vencen") | dbdiagram (vistas) | 4 | 3 | 2 | 4 | 3 | 16 | Descartada por ahora: costo de backend |
| Comparación antes/después en Historial de cambios | dbdiagram (versiones) | 3 | 3 | 2 | 4 | 3 | 15 | Descartada por ahora |
| Cifras que cuentan (Number Ticker) | magicui | 1 | 3 | 4 | 4 | 4 | 16 | Descartada: el brief §6.7 lo retiró |

## Stock-Web-Automate (app de campo)

| Idea | Origen | Impacto | Marca | Costo | Rend. | Mant. | Total | Decisión |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Animación de entrada "Línea de flujo" | animate-ui (Progress), v0 (indicadores) | 3 | 4 | 5 | 5 | 5 | 22 | **Seleccionada** |
| Barra lineal de subida en "Por subir" con `scaleX` | magicui (progreso), animate-ui | 4 | 4 | 4 | 5 | 4 | 21 | **Seleccionada**. Un anillo se lee peor al sol |
| Confirmación "Guardado en este celular" con icono de 0,8 a 1, 200 ms | animate-ui | 5 | 4 | 5 | 5 | 5 | 24 | **Seleccionada**. Ya prevista en el brief §7.8 |
| Barra "Paso 2 de 4" con `scaleX` | v0 | 4 | 4 | 4 | 5 | 5 | 22 | **Seleccionada** |
| Cifra de la banda que cambia con opacidad en 120 ms | smoothui (Number Flow) | 2 | 3 | 4 | 5 | 4 | 18 | Descartada: aporta poco. La cifra cambia al instante |
| Rótulo visible en todos los campos | ui-skills | 4 | 4 | 4 | 5 | 5 | 22 | **Seleccionada** |

---

## Animación de entrada

### Restricciones comunes

Valen para los tres sistemas. Si una implementación no las cumple, se retira.

| Restricción | Cómo se cumple |
|---|---|
| Duración de 0,8 a 1,8 s | Frontend 1,5 s, Admin 0,9 s, Stock 0,9 s |
| Solo CSS/SVG o dependencias existentes | `@keyframes` CSS, SVG en línea y un script en línea de menos de 400 bytes. Sin `framer-motion` ni `motion` |
| Una vez por sesión | `sessionStorage` con clave propia por sistema. La clave se escribe al empezar, de modo que una recarga a mitad no repite la animación |
| No bloquea CTA, desplazamiento ni entrada | Capa con `pointer-events: none`, `aria-hidden="true"` y sin fondo. No hay espera ni `overflow: hidden` en `body`. El contenido es usable desde el primer fotograma |
| Respaldo estático | Sin JS, la capa tiene `display: none` porque el atributo `data-intro` nunca llega a ponerse. Con `prefers-reduced-motion: reduce`, el script no pone el atributo y además el CSS la oculta. Lo que queda es la página normal, con sus reglas estáticas |
| Sin penalización en LCP | La capa no contiene texto, `<img>` ni `<image>`, así que no puede ser candidata a LCP. No tapa el H1 ni la imagen del héroe, que se pintan con opacidad 1 y sin retraso. Su fondo es transparente |
| Sin penalización en CLS | Posición `absolute` o `fixed`, fuera del flujo, con alto fijo. Solo se anima `transform`, que no desplaza a otros elementos |
| Sin penalización en INP/TBT | No hay manejadores de puntero. Solo un `animationend` que retira el atributo. El script en línea no hace trabajo pesado |
| Propiedades | Solo `transform` (`scaleX`, `scaleY`, `translate`, `rotate`) y `opacity`. El brief §4.2 prohíbe `stroke-dashoffset`, así que el "trazo" se hace escalando tramos rectos con `transform-origin` en el extremo inicial |
| Logotipo | Nunca se anima, recolorea ni filtra (brief §2). La animación termina junto al logotipo real, que ya está pintado y quieto |

Script de arranque, igual en los tres sistemas salvo la clave y la condición de ruta. Va en `<head>`, antes de que se pinte `<body>`:

```js
try {
  if (/* condición de ruta */ !sessionStorage.getItem(KEY) &&
      !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    document.documentElement.setAttribute("data-intro", "");
    sessionStorage.setItem(KEY, "1");
  }
} catch (e) {}
```

Retirada: un `animationend` en el último elemento quita `data-intro`, con un `setTimeout` de respaldo de 2.000 ms. El atributo `data-intro` vuelve a dejar la capa en `display: none`.

Antes de implementar hay que revisar la CSP de cada app. Un script en línea puede necesitar `nonce` o `hash`. El brief §4.6 fija 0 KB de JS nuevo para movimiento: este script es una excepción de menos de 400 bytes, que debe aprobar el responsable del proyecto.

---

### Frontend: conceptos

| Concepto | Descripción | Peso | Riesgo | Decisión |
|---|---|---|---|---|
| A. Circuito hidráulico | Tres tuberías se trazan desde los bordes, se unen en una válvula estilizada, el agua recorre el circuito y todo converge en el logotipo | ~12 animaciones, SVG grande | Supera el tope de 8 animaciones vivas por ruta (brief §4.6). Ocupa la zona del héroe | Descartado |
| B. Línea de presión | Una tubería se traza bajo la cabecera, aparece una válvula estilizada, su timón gira un cuarto de vuelta y un pulso de agua viaja hasta el logotipo real | 6 animaciones, < 2 KB | Bajo | **Elegido** |
| C. Solo pulso en la regla | Un pulso recorre el borde inferior de la cabecera | 2 animaciones | Mínimo, pero pierde la válvula y el agua, que piden el concepto | Descartado: no cuenta la historia de producto |

B es el más ligero que conserva los tres elementos pedidos: tubería, válvula y agua que termina en la marca.

### Frontend: especificación de "Línea de presión"

**Dónde.** Solo en `/`, en la primera visita de la sesión. Clave `fx-intro-web`. Condición de ruta: `location.pathname === "/"`.

**Capa.** `<div class="fx-intro" aria-hidden="true">` en el HTML del servidor, como hijo directo de `<body>` justo después de la cabecera.

```css
.fx-intro { display: none; }
html[data-intro] .fx-intro {
  display: block;
  position: absolute;          /* se va con el desplazamiento: no persigue al usuario */
  top: var(--header-h);        /* 84 px, o 72 px por debajo de 860 px */
  left: 0; right: 0;
  height: 40px;
  z-index: 55;                 /* sobre la cabecera (50) y bajo los botones flotantes (60) */
  pointer-events: none;
  contain: layout paint;
  color: var(--c-sky);         /* #9bcee7 sobre #002b3a del héroe: 8,80:1 */
  animation: fx-out 320ms var(--mo-ease-in) 1180ms forwards;
}
@media (prefers-reduced-motion: reduce) { .fx-intro { display: none !important; } }
```

La banda ocupa los primeros 40 px del héroe, que tiene fondo `--c-primary-deep` `#002b3a`. Hay que confirmar con `motion-audit.mjs`, en 320, 390, 768, 1024, 1261, 1440 y 1920 px, que la banda no toca el H1. Si lo toca, se baja a 24 px de alto. Como la banda es transparente, aunque se superponga no oculta texto.

**Piezas.** `X` es el centro horizontal del logotipo de la cabecera: `calc(var(--lp-gutter) + 24px)`. Hay que ajustarlo al ancho real del icono en `landing-chrome`. `V` es la posición de la válvula: `62%` del ancho.

| Pieza | Forma | Posición | Color |
|---|---|---|---|
| `.fx-pipe` | Caja de 6 px de alto con `border-block: 2px solid currentColor`, que dibuja las dos paredes de la tubería | `top: 17px; left: X; right: 0` | `--c-sky` `#9bcee7` |
| `.fx-valve` | SVG de 40×40 en línea, `viewBox="0 0 40 40"`. Cuerpo: `<circle cx="20" cy="20" r="9">` con relleno `#002b3a` (`--c-primary-deep`) y trazo de 2 px. Bridas: dos `<rect>` de 2×14, en x=9 y x=29, y=13. Vástago: `<line x1="20" y1="11" x2="20" y2="4">`. Timón, grupo `.fx-wheel`: `<line x1="13" y1="4" x2="27" y2="4">` más `<circle cx="20" cy="4" r="2">`, con `transform-box: fill-box; transform-origin: center` | `left: calc(V - 20px); top: 0` | Trazo `currentColor`, 2 px, `stroke-linecap="square"` |
| `.fx-track` / `.fx-flow` | Pista con `overflow: hidden`, estática, entre X y V. Dentro, `.fx-flow` con `width: 100%`. Su `::before` es el pulso: 32×2 px pegado a su borde izquierdo | Pista: `top: 19px; left: X; right: calc(100% - V); height: 2px` | Pulso `--c-sky-soft` `#e3f0f9` |
| `.fx-riser` | Caja de 6×17 px con `border-inline: 2px solid currentColor`: el tramo vertical que sube hasta la cabecera, bajo el logotipo | `top: 0; left: calc(X - 3px)` | `--c-sky` |

**Tiempos.** Duración total: 1.500 ms. Todas las animaciones usan `backwards`, salvo `fx-out`, que usa `forwards`.

| Inicio | Duración | Pieza | De → a | Curva |
|---:|---:|---|---|---|
| 0 ms | 520 ms | `.fx-pipe` | `scaleX(0)` → `scaleX(1)`, `transform-origin: right`. El trazo avanza de derecha a izquierda, hacia la marca | `--mo-ease-out` `cubic-bezier(0.16, 1, 0.3, 1)` |
| 160 ms | 480 ms | `.fx-valve` | `opacity: 0; translate: 0 8px` → `opacity: 1; translate: 0 0` | `--mo-ease-out` |
| 520 ms | 480 ms | `.fx-wheel` | `rotate(0)` → `rotate(90deg)`. El timón abre la compuerta (tesis "Compuerta", brief §4.1) | `--mo-ease-in-out` `cubic-bezier(0.65, 0, 0.35, 1)` |
| 760 ms | 480 ms | `.fx-flow` | `translateX(100%)` → `translateX(0)`. El pulso viaja de la válvula al logotipo | `--mo-ease-in-out` |
| 1.040 ms | 200 ms | `.fx-riser` | `scaleY(0)` → `scaleY(1)`, `transform-origin: bottom`. El agua sube hasta la marca | `--mo-ease-out` |
| 1.180 ms | 320 ms | `.fx-intro` | `opacity: 1` → `0`. Queda la página normal | `--mo-ease-in` `cubic-bezier(0.4, 0, 1, 1)` |

**Tema oscuro.** No requiere cambios: el héroe sigue siendo oscuro y los colores salen de `--c-sky`, `--c-sky-soft` y `--c-primary-deep`.

**Presupuesto.** CSS de ~1,2 KB sin comprimir, SVG de < 600 B y script de < 400 B. Son 6 animaciones. Hoy la portada suma además `data-enter` en botones y cartela. Hay que comprobar con `motion-audit.mjs` que las animaciones vivas a los 250 ms no pasen de 8. Si pasan, `.fx-valve` y `.fx-wheel` se unen en una sola animación.

**Aceptación.** LCP, CLS y TBT iguales o mejores que sin la capa, con la mediana de 3 corridas. 0 errores de consola. Teclado: Tab llega al primer enlace sin esperar. La animación no se repite al volver a `/` dentro de la sesión.

---

### Admin: conceptos

| Concepto | Descripción | Decisión |
|---|---|---|
| A. Regla de tinta | La regla bajo la barra superior se traza de izquierda a derecha y una marca corta en azul de datos se asienta en su origen, como el cajetín de un plano | **Elegido**: 2 animaciones y ninguna toca el contenido |
| B. Marco de hoja | Los cuatro bordes de la hoja blanca (radio 10 px) se dibujan en secuencia | Descartado: 4 o 5 piezas, y las esquinas redondeadas no se trazan bien escalando tramos rectos |
| C. Contenido que sube | La hoja y su contenido entran con 8 px | Descartado: el brief §6.7 retiró `.route` y `.stagger`, porque las pantallas llegan quietas |

### Admin: especificación de "Regla de tinta"

**Dónde.** Primera pantalla del panel tras iniciar sesión, una vez por sesión. Clave `fx-intro-admin`. No se muestra en `/login`. Condición: el `<html>` de la ruta del panel. El script va en el layout de `(panel)`.

**Capa.** `<div class="shell-intro" aria-hidden="true">` dentro de la barra superior, con `position: absolute; left: 0; right: 0; bottom: -1px; height: 3px; pointer-events: none; z-index: 1`. Termina exactamente sobre la línea inferior estática de la barra superior. Hay que verificar en `shell.css` qué borde dibuja hoy esa línea (alto de barra 60 px, `--topbar-h`).

| Pieza | Forma | Color |
|---|---|---|
| `.shell-intro__rule` | 1 px de alto, todo el ancho, abajo | `--rule-strong` `#1b262e` en claro y `#c9ced2` en oscuro |
| `.shell-intro__tick` | 40×3 px, en el borde izquierdo de la hoja | `--accent` `#0972a1` en claro y `#4fb3e3` en oscuro |

| Inicio | Duración | Pieza | De → a | Curva |
|---:|---:|---|---|---|
| 0 ms | 560 ms | `__rule` | `scaleX(0)` → `scaleX(1)`, `transform-origin: left` | `--ease-out` `cubic-bezier(0.16, 1, 0.3, 1)` |
| 440 ms | 200 ms | `__tick` | `opacity: 0; scaleX(0.4)` → `opacity: 1; scaleX(1)`, origen a la izquierda | `--ease-out` |
| 680 ms | 220 ms | `.shell-intro` | `opacity: 1` → `0` | `--ease-in` `cubic-bezier(0.4, 0, 1, 1)` |

Duración total: 900 ms. La búsqueda, el menú y el botón principal funcionan desde el primer fotograma. Con `prefers-reduced-motion` no se muestra. `base.css` ya reduce todo a 1 ms.

---

### Stock: conceptos

| Concepto | Descripción | Decisión |
|---|---|---|
| A. Línea de flujo | Bajo la banda de estado de 56 px, una línea de 3 px en petróleo cruza la pantalla de izquierda a derecha y se desvanece | **Elegido**: 1 pieza, CSS local y funciona sin red |
| B. Banda "Conectando…" con progreso indeterminado | Barra que va y viene mientras se resuelve el estado | Descartado: es un bucle y depende de la red |
| C. Botones de Registrar que suben 8 px | Los dos botones de 120 px se asientan | Descartado: mueve el objetivo del pulgar en el primer toque |

### Stock: especificación de "Línea de flujo"

**Dónde.** Al abrir la app, una vez por sesión. En la PWA instalada, la sesión dura lo que dura la ventana abierta. Clave `fx-intro-stock`. Sin condición de ruta: la app abre en Registrar.

**Offline.** La capa va en `index.html`, junto al primer pintado que ya existe (banda "Conectando…" y "¿Qué vas a registrar?"). Los keyframes van en `src/index.css`, que ya está en el bundle cacheado. No hay fuente, imagen ni petición nueva.

```css
.fx-flow-line { display: none; }
html[data-intro] .fx-flow-line {
  display: block;
  position: fixed;
  top: 56px;                    /* bajo la banda h-14 */
  left: 0; right: 0;
  height: 3px;
  z-index: 56;                  /* sobre la banda (55) y bajo z-[60] */
  pointer-events: none;
  background: var(--color-action); /* #004257 sobre #f1f5f7 */
  transform-origin: left;
  animation:
    fx-flow 600ms cubic-bezier(0.16, 1, 0.3, 1) backwards,
    fx-out 200ms cubic-bezier(0.4, 0, 1, 1) 700ms forwards;
}
@keyframes fx-flow { from { transform: scaleX(0); } }
@keyframes fx-out { to { opacity: 0; } }
@media (prefers-reduced-motion: reduce) { .fx-flow-line { display: none !important; } }
```

| Inicio | Duración | De → a | Curva |
|---:|---:|---|---|
| 0 ms | 600 ms | `scaleX(0)` → `scaleX(1)` | `cubic-bezier(0.16, 1, 0.3, 1)`, la misma curva del cambio de paso (brief §7.8) |
| 700 ms | 200 ms | `opacity: 1` → `0` | `cubic-bezier(0.4, 0, 1, 1)` |

Duración total: 900 ms. Si al terminar no se dispara `animationend`, por ejemplo con la pestaña en segundo plano, el respaldo de 2.000 ms retira `data-intro`. Prueba manual: modo avión, abrir la app, ver la línea y registrar de inmediato sin esperar.
