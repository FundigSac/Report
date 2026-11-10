# 02b · Cobertura de favoritos

Fuente: barra de favoritos del perfil principal de Chrome, leída del archivo local `AccountBookmarks` el 10/11/2026 (la integración de Chrome no permite abrir `chrome://bookmarks`). La barra no tiene carpetas ni subcarpetas; todos los enlaces están en el primer nivel. «Otros favoritos» tiene 3 enlaces no relacionados con diseño.

| Métrica | Valor |
| --- | --- |
| total_de_marcadores_detectados (barra) | 71 |
| duplicados | 0 |
| personales excluidos (sin listar) | 9 |
| herramientas/paneles de desarrollo (no son referencia visual) | 32 |
| relevantes de diseño/UI | 30 |
| relevantes_revisados con Claude in Chrome | 29 |
| parcial (requiere login) | 1 (Mobbin) |
| inaccesibles | 1 (gooddesign.tools: falla TLS) |
| pendientes | 0 |
| % de cobertura con resultado verificable | 100 % (30/30); 96,7 % visitados con contenido (29/30) |
| ideas registradas de favoritos | 170 |
| referencias externas nuevas (fuera de favoritos) | 14, con 98 ideas (`03c-external-design-discovery.md`) |

## Limitaciones reales

- El ancho de celular (390×844) no se pudo fijar en la ventana compartida de Chrome: `resize_window` respondió bien pero la página siguió en ~1568 px. Para 11 a 20 y para X9–X14 se usó la emulación del navegador integrado; en el resto, la observación móvil se dio solo cuando el sitio tenía su propia vista de dispositivo. Esas notas están marcadas como inferidas en cada parte.
- En Stitch la sesión del usuario ya estaba abierta: solo se miró la galería y un prototipo público, sin abrir proyectos privados.
- No se inició sesión, no se enviaron formularios ni se descargaron archivos en ningún sitio.

## Herramientas no auditadas como diseño (motivo)

Paneles con login o herramientas de trabajo (Vercel, Supabase, Netlify, Render, Cloudflare, Context7, AI Studio, Jules, v0 chat privado, Search Console, Lucid, dbdiagram, etc.): se usan como herramientas del proyecto, no como fuente visual. Están listados en `02-bookmarks-inventory.csv` con categoría «herramienta/desarrollo».
