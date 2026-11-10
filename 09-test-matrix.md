# 09 · Matriz de pruebas

Solo resultados ejecutados en esta sesión. Datos siempre sintéticos (`@example.test`), borrados después.

| Prueba | Entorno | Commit (Admin) | Resultado | Evidencia |
| --- | --- | --- | --- | --- |
| `tests/api/staff-access` (4): código uniforme, intento descontado, código de un solo uso, rotación y reutilización de refresh, token alterado | local → Supabase `fundigsac-admin` | 19bbc89 | 4/4 | `npm run test:api` |
| `tests/api/forms` (7): cotización con constancia, idempotencia y `IDEMPOTENCY_KEY_REUSED`, validaciones (RUC, correo, teléfono, campo desconocido, honeypot), `EMPTY_QUOTE`, 429 con `Retry-After`, hoja de reclamación con plazo y trigger que impide reescribirla, privacidad y consentimiento | idem | 19bbc89 | 7/7 | idem |
| `tests/api/staff-cases` (5): 401/403 por permiso, `If-Match` 428/412, transiciones 409, `REASON_REQUIRED`, `INVALID_ASSIGNEE`, respuesta única del reclamo, correo de respuesta encolado | idem | 19bbc89 | 5/5 | idem |
| `tests/api/staff-accounts` (4): directorio y búsqueda sin tildes, estadísticas, actividad, invitar, roles, notas, desactivar, reactivar, eliminar (anonimiza), reglas de autoprotección, invalidación de token por cambio de roles | idem | 19bbc89 | 4/4 | idem |
| `tests/api/customers` (3): registro, `EMAIL_NOT_VERIFIED`, verificación, login, bloqueo tras 5 fallos, recuperación, política de contraseña, token de un solo uso, Google deshabilitado | idem | 19bbc89 | 3/3 | idem |
| **Total integración API** | | | **23/23** | |
| E2E manual: código por correo (forzado en prueba) → panel «Para hoy» con datos de la API | local, navegador integrado | 19bbc89 | correcto | 10 pendientes reales de prueba listados |
| E2E transversal: formulario `/reclamaciones` del sitio → API → cola del panel | Frontend local + Admin local | 19bbc89 | correcto | hoja REC-2026-000003 visible con 15 días hábiles |
| BFF en el mismo proceso (`BACKEND_URL=self`), permisos de READ_ONLY | local | 30040c5 | correcto | 3×200 y 2×403 en 0,4 s |
| Preview en Vercel: API con base de datos | `fundigsac-admin-86o1hp2bh-…vercel.app` | 30040c5 | correcto | `GET /api/v1/quotes/…/receipt` → 404 `QUOTE_NOT_FOUND` (escribe el límite en la base) |
| `tsc --noEmit`, `eslint src tests/api`, `next build` | local | 39ebc0a | sin errores | |
| Stock en producción: datos visibles | https://fundigsac-stock-dashboard.vercel.app | sin cambios | correcto | 187 productos, «En línea · Todo subido» |

## No ejecutado todavía (pendiente explícito)

- Inicio de sesión real del personal en Preview/producción: falta la clave de Resend.
- Suite visual multi-navegador, Lighthouse y axe de esta versión.
- Pruebas del Backend Java con Testcontainers: Docker Desktop está detenido en este equipo.
- Una base de pruebas separada para CI: hoy las pruebas de integración corren contra el proyecto real y se limpian a mano; antes de abrir CI hay que crear un proyecto o rama de Supabase de pruebas.

## 2026-11-10 (noche)

| Suite | Entorno | Commit | Resultado |
| --- | --- | --- | --- |
| Sitio: Playwright completo (escritorio + celular) | local, BACKEND_URL=off | 513312c | 612 aprobadas, 18 omitidas (ya existentes), 0 fallidas |
| Sitio: vitest | local | 513312c | 138/138 |
| Admin: tests/panel.spec.ts (demo) | local | a76c367 | 60 aprobadas, 4 omitidas (solo escritorio), 0 fallidas |
| Admin: auditoría responsive | local | a76c367 | 19 pantallas × 13 anchos sin problemas |
| Stock: Playwright | local con backend simulado | ed3696f | 61/61 |
| Stock: vitest | local | ed3696f | 227/227 |
| Scrapling: parser | local | Report de9873c | 44/44 |
| Producción: humo en las 3 URL | producción | ver 12-deployments | correcto, sin crear datos |

## 2026-11-10 (tanda 2, ramas `feat/ideas-tanda-2`, sin publicar)

Primera corrida en Firefox y WebKit (motor de Safari). Todo local, con datos sintéticos o de demostración; ninguna prueba apunta a producción.

| Suite | Proyecto | Aprobadas | Fallidas | Omitidas |
| --- | --- | --- | --- | --- |
| Sitio (6ddbb32) | Chromium escritorio | 321 | 0 | 9 |
| Sitio | Chromium celular | 321 | 0 | 9 |
| Sitio | Firefox escritorio | 318 | 1 | 11 |
| Sitio | WebKit escritorio | 320 | 1 | 9 |
| Sitio | WebKit iPhone 15 | 319 | 2 | 9 |
| Sitio: vitest | | 153 | 0 | |
| Admin (e8f086a), modo demo | Chromium escritorio | 39 | 0 | 0 |
| Admin | Pixel 7 | 34 | 0 | 5 |
| Admin | Firefox | 39 | 0 | 0 |
| Admin | WebKit | 39 | 0 | 0 |
| Admin | iPhone 13 | 34 | 0 | 5 |
| Stock (d10c00e), backend simulado | Chromium | 72 | 0 | 0 |
| Stock | Firefox | 68 | 0 | 4 |
| Stock | WebKit | 65 | 0 | 7 |
| Stock | iPhone 13 | 64 | 0 | 8 |
| Stock: vitest | | 242 | 0 | |

Las 4 fallas del sitio son intermitentes: al repetirlas 3 veces, pasan la mayoría de las veces. Son el asistente y el envío del Libro de Reclamaciones en WebKit escritorio, el foco del título de la constancia de reclamo en iPhone y el foco del buscador en Firefox. Las omisiones tienen su motivo escrito en el código: Google OAuth o el backend en Docker, que no hay en local; el service worker, que Playwright no puede interceptar en WebKit; y Firefox en modo «trabajar sin conexión».

Errores reales que salieron con los otros navegadores y ya se corrigieron:

- Stock en Safari privado no guardaba fotos (IndexedDB), así que una entrega con foto quedaba esperando sin terminar.
- Stock decía «Conectado» unos 7 s estando sin red.
- La isla del reporte semanal de Stock se salía 244 px de la pantalla en tabletas con Safari.
- En el sitio con Firefox, el correo del pie ensanchaba la página 7 px a 390 px de ancho.
- En el sitio con WebKit, lo escrito en el buscador antes de terminar la carga no filtraba.
- En el Admin, «Limpiar filtros» cambiaba la ruta sin necesidad e interrumpía la siguiente navegación (Firefox, iPhone).

La consulta nueva de `GET /staff/accounts/stats` (filtros por KPI) se probó en la base real dentro de una transacción de solo lectura y respondió sin errores.
