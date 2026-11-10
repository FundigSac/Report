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
