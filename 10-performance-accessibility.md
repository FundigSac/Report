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

## Pendiente

- Lighthouse de rendimiento y trazas del sitio público después de publicar la entrada (mediana de 3 corridas antes y después).
- Suite visual en los 7 tamaños pedidos y en Firefox/WebKit: no configurada todavía.
