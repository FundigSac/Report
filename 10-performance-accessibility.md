# 10 · Rendimiento y accesibilidad (medido)

Mediciones de laboratorio del 10/11/2026. No hay datos de campo (CrUX): las tres páginas no tienen tráfico suficiente.

## Lighthouse (móvil), producción

| Página | Accesibilidad | Buenas prácticas | SEO | Nota | Evidencia |
| --- | --- | --- | --- | --- | --- |
| https://fundigsac-admin.vercel.app/login | 100 | 100 | 66 | SEO bajo a propósito: `noindex` en un panel interno | `qa/lighthouse/admin-login-mobile.html` |
| https://fundigsac-stock-dashboard.vercel.app/ | 100 | 100 | 50 | `noindex` a propósito y sin meta description (app interna) | `qa/lighthouse/stock-home-mobile.html` |

La herramienta de auditoría de este entorno no incluye la categoría Rendimiento. Por eso el rendimiento se midió con trazas de Chrome.

## Trazas de Chrome (celular 390×844, CPU 4× más lenta, red Slow 4G), producción

| Página | LCP | CLS | Observación | Evidencia |
| --- | --- | --- | --- | --- |
| Admin `/login` | 785 ms (TTFB 564 ms + render 221 ms) | 0,00 | 14,2 kB de JS heredado (polyfills) se pueden quitar | `qa/lighthouse/admin-login-trace.json.gz` |
| Stock `/` | 327 ms | 0,00 | Carga en caliente servida por el service worker (TTFB 3 ms); una primera visita sin caché será más lenta | `qa/lighthouse/stock-home-trace.json.gz` |

Objetivo §9F: LCP ≤ 2,5 s y CLS ≤ 0,1. Ambas páginas lo cumplen en laboratorio.

## Animaciones de entrada

| Sistema | Duración | Garantías verificadas con E2E |
| --- | --- | --- |
| Stock «Línea de flujo» | 0,9 s | Una vez por sesión, se retira sola, `pointer-events: none`, el primer toque funciona durante la animación, no aparece con movimiento reducido |
| Admin «Regla de tinta» | 0,9 s | Una vez por sesión, no se repite al recargar, oculta con movimiento reducido |
| Sitio «Línea de presión» | 1,5 s | Solo en `/`, una vez por sesión, sin texto ni imágenes (no compite por el LCP), `pointer-events: none`, no aparece con movimiento reducido |

## Lighthouse del sitio publicado (10/11, commit 513312c)

Lighthouse 12.8.2, mediana de 3 corridas por página y formato. En celular usa la limitación simulada por defecto (CPU 4× más lenta, red 4G lenta). Las corridas se hicieron mientras tres agentes ejecutaban pruebas en el mismo equipo, así que el rendimiento en celular puede salir algo peor de lo que verían los visitantes. Solo se abrieron páginas: no se envió ningún formulario.

| Página | Formato | Rendimiento | Accesibilidad | Buenas prácticas | SEO | LCP | CLS | TBT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Portada `/` | celular | 89 | 100 | 100 | 100 | 3,7 s | 0 | 51 ms |
| Portada `/` | escritorio | 99 | 100 | 100 | 100 | 0,9 s | 0,003 | 0 ms |
| Catálogo `/productos` | celular | 94 | 100 | 100 | 100 | 3,1 s | 0 | 25 ms |
| Catálogo `/productos` | escritorio | 99 | 100 | 100 | 100 | 0,8 s | 0 | 0 ms |
| Familia `/productos/valvulas` | celular | 95 | 100 | 100 | 100 | 2,9 s | 0 | 97 ms |
| Familia `/productos/valvulas` | escritorio | 99 | 94 | 100 | 100 | 0,8 s | 0 | 0 ms |
| Ficha `/productos/valvulas/valvula-compuerta` | celular | 89 | 100 | 100 | 100 | 3,4 s | 0 | 179 ms |
| Ficha | escritorio | 99 | 100 | 100 | 100 | 0,8 s | 0 | 0 ms |
| Cotizar `/cotizar` | celular | 95 | 100 | 100 | 100 | 2,7 s | 0 | 54 ms |
| Cotizar | escritorio | 100 | 100 | 100 | 100 | 0,6 s | 0 | 0 ms |
| Reclamaciones `/reclamaciones` | celular | 93 | 100 | 100 | 100 | 3,0 s | 0 | 125 ms |
| Reclamaciones | escritorio | 100 | 100 | 100 | 100 | 0,7 s | 0 | 0 ms |

En reclamaciones (celular) una de las tres corridas falló, así que su mediana sale de dos corridas. La primera corrida de cada página y formato está en `qa/lighthouse/sitio-2026-11-10/`.

Hallazgos y acción (en la rama `feat/ideas-tanda-2` del sitio):

1. **Puntos del carrusel de la familia** de 21,7 × 19,8 px, por debajo de los 24 × 24 px que pide WCAG 2.2 (2.5.8). Se agranda el área táctil sin cambiar el punto visible.
2. **Contraste de las tarjetas de familia** (1,4–1,7) en escritorio: el texto se midió a mitad del fundido de entrada. Se revisa que el texto quede legible aunque la animación no se dispare.
3. **Imágenes de la portada**: las fotos de sectores y de la válvula se sirven a 640 px para mostrarse a unos 330 px, y la foto de la planta (elemento LCP) admite más compresión. El ahorro estimado es de unos 370 KiB en celular. Se añaden variantes más pequeñas con `srcset`/`sizes`.
4. El LCP de la portada en celular empieza con un TTFB de 0,76 s (16 % del total). El resto es la descarga y el pintado de la foto de la planta.

## Pendiente

- Volver a medir después de publicar la tanda 2 (las mismas 6 páginas, mediana de 3).
- Suite visual en los 7 tamaños pedidos y en Firefox/WebKit: en curso en las ramas `feat/ideas-tanda-2`.
