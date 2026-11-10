# 12 · Despliegues

| Fecha | Sistema | Repo / rama | Commit | Tipo | URL | Estado | Rollback |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Admin + API | `FundigSac/Admin` · `feat/api-real-supabase` | 30040c5 | Preview (CLI) | https://fundigsac-admin-86o1hp2bh-diegos-projects-1a03253b.vercel.app | READY; API conectada a Supabase verificada | Preview: no afecta producción |
| 2026-11-10 | Supabase `fundigsac-admin` | — | migraciones 20261110140248 a 20261110140631 | Esquema nuevo (aditivo, proyecto nuevo) | — | Aplicado; base limpia salvo la cuenta administradora inicial | Proyecto aislado; Stock no se tocó |

Producción de los tres enlaces sin cambios en esta fecha. La promoción de Admin (`NEXT_PUBLIC_DATA_SOURCE=backend`, `BACKEND_URL=self`) y del sitio (`BACKEND_URL=https://fundigsac-admin.vercel.app`) espera la clave de Resend: sin correo nadie del personal podría entrar ni recibir constancias.

## Variables en Vercel `fundigsac-admin` (valores cifrados, no se listan)

Preview y Production: `DATABASE_URL`, `API_JWT_SECRET`, `ADMIN_AUTH_SECRET`, `RECEIPT_KEY`, `SITE_URL`, `ADMIN_URL`, `MAIL_FROM`, `SALES_INBOX`, `LEGAL_INBOX`, `PRIVACY_INBOX`. Solo Preview: `NEXT_PUBLIC_DATA_SOURCE=backend`, `BACKEND_URL=self`. Pendiente: `RESEND_API_KEY` (la carga el responsable).

## 2026-11-10 (tarde): publicación en producción

| Sistema | Commit en `main` | Despliegue | URL estable | Verificación en producción | Rollback |
| --- | --- | --- | --- | --- | --- |
| Admin + API | 99c1370 | `fundigsac-admin-3t8ncni2g-…` | https://fundigsac-admin.vercel.app | Sin demo; `/api/v1/staff/profile` y BFF responden 401 sin sesión; código de acceso enviado por Resend (`SENT`) | Promover `fundigsac-admin-eo3dqwmj7-…` |
| Sitio | 72030f3 | `dpl_474BbZK5rcTvtJyC15n2TcXUWWsx` | https://fundigsac-web.vercel.app | Reclamo inválido → 400 con errores por campo (sin crear registro); consentimiento 201; el límite cuenta por la IP real del visitante; `CUSTOMER_ACCOUNTS=off` | Promover `fundigsac-248vclsh2-…` o quitar `BACKEND_URL` |
| Stock | c574d21 (bbffd82 + intro) | `fundigsac-stock-dashboard-lk8h5h83p-…` | https://fundigsac-stock-dashboard.vercel.app | Tras el aviso «Actualizar» de la PWA: tabla de 19 trabajadores (igual que la base), sin errores de consola | Promover `fundigsac-stock-dashboard-7rg8an409-…` |
| Admin (diseño) | 3ae4319 | `fundigsac-admin-jdqeejrj6-…` | https://fundigsac-admin.vercel.app | Login sin demo, API 401 sin sesión, sin errores de consola | Promover `fundigsac-admin-3t8ncni2g-…` |

Previews de Stock: no tienen variables de Supabase a propósito, para no exponer datos reales de trabajadores en un Preview (regla 5). Sus pruebas corren con mocks.

## 2026-11-10 (noche): diseño restaurado + 22 mejoras de favoritos y referencias

| Sistema | Commit en `main` | URL | Verificación en producción |
| --- | --- | --- | --- |
| Admin | 5e72910 (diseño 20/10) → a76c367 (7 ideas) | https://fundigsac-admin.vercel.app | Sin demo, salud `ok`, 0 correos pendientes |
| Stock | 55b6762 (diseño 30/10 + espacio) → ed3696f (7 ideas) | https://fundigsac-stock-dashboard.vercel.app | Aviso PWA «Actualizar» → versión nueva, cifras tabulares, estados con ícono, sin errores |
| Sitio | 2221b5c (diseño 4/11, 7 familias, 85 fichas) → 513312c (9 ideas) | https://fundigsac-web.vercel.app | CTA #c94f0a, búsqueda vacía con «Pedir cotización», 0 imágenes rotas, reclamo inválido 400 |

Base `app`: 0 reclamos, 0 cotizaciones, 0 consultas tras las pruebas de humo (ningún dato ficticio).

## 2026-11-10 (noche) · tanda 2

| Sistema | Commit en `main` | Despliegue | URL | Verificación en producción | Rollback |
| --- | --- | --- | --- | --- | --- |
| Admin | e8f086a | Preview `fundigsac-admin-gd94v8buh-…` y luego producción `fundigsac-admin-lz8pax8ig-…` (CLI) | https://fundigsac-admin.vercel.app | health ok (base 62 ms), `stats` sin sesión 401 | promover a76c367 |
| Stock | d10c00e | producción `fundigsac-stock-dashboard-d5vq35yjr-…` (CLI) | https://fundigsac-stock-dashboard.vercel.app | aviso «Hay una versión nueva» → Actualizar → carga `index-yxdalcZ4.js`; barra de salud visible; «En línea · Todo subido»; sin cambios de datos | promover ed3696f |
| Sitio | 6ddbb32 | Preview `fundigsac-gjn3a1aao-…` (READY) y luego push a `main` | https://fundigsac-web.vercel.app | ficha con «Medidas disponibles», caption, chips y «Agregar a cotización»; /productos con conteos y Equipos de termofusión; puntos del carrusel 34×34; 0 imágenes rotas; sin desborde; reclamo inválido → 400; la base sigue con 0 cotizaciones, 0 reclamos y 0 consultas | promover 513312c |
