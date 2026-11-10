# 12 · Despliegues

| Fecha | Sistema | Repo / rama | Commit | Tipo | URL | Estado | Rollback |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Admin + API | `FundigSac/Admin` · `feat/api-real-supabase` | 30040c5 | Preview (CLI) | https://fundigsac-admin-86o1hp2bh-diegos-projects-1a03253b.vercel.app | READY; API conectada a Supabase verificada | Preview: no afecta producción |
| 2026-11-10 | Supabase `fundigsac-admin` | — | migraciones 20261110140248 a 20261110140631 | Esquema nuevo (aditivo, proyecto nuevo) | — | Aplicado; base limpia salvo la cuenta administradora inicial | Proyecto aislado; Stock no se tocó |

Producción de los tres enlaces sin cambios en esta fecha. La promoción de Admin (`NEXT_PUBLIC_DATA_SOURCE=backend`, `BACKEND_URL=self`) y del sitio (`BACKEND_URL=https://fundigsac-admin.vercel.app`) espera la clave de Resend: sin correo nadie del personal podría entrar ni recibir constancias.

## Variables en Vercel `fundigsac-admin` (valores cifrados, no se listan)

Preview y Production: `DATABASE_URL`, `API_JWT_SECRET`, `ADMIN_AUTH_SECRET`, `RECEIPT_KEY`, `SITE_URL`, `ADMIN_URL`, `MAIL_FROM`, `SALES_INBOX`, `LEGAL_INBOX`, `PRIVACY_INBOX`. Solo Preview: `NEXT_PUBLIC_DATA_SOURCE=backend`, `BACKEND_URL=self`. Pendiente: `RESEND_API_KEY` (la carga el responsable).
