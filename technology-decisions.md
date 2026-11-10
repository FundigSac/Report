# Decisiones de tecnología (con fuente)

| Fecha | Tecnología | Decisión | Fuente consultada |
| --- | --- | --- | --- |
| 2026-11-10 | `postgres` (porsager) 3.4.9 → 4.1.0 | Usarlo por el pooler de transacciones de Supavisor con `prepare: false`, `max_pipeline: 1` e `infer: true` | Context7 `/porsager/postgres`: secciones «Connection poolers» y «Upgrading from v3» (consultado el 2026-11-10) |
| 2026-11-10 | Resend (HTTP API) | Correos transaccionales con bandeja de salida y reintentos | API REST pública `POST https://api.resend.com/emails`; el mensaje de error real se registra en `email_outbox.last_error` |
| 2026-11-10 | Next.js `after()` | Enviar correos después de responder, sin bloquear la petición | Next.js 16 instalado (`node_modules/next/dist/docs`, según AGENTS.md del Admin) |
| 2026-11-10 | `@electric-sql/pglite` 0.3 | Restaurar respaldos en un Postgres en memoria, sin Docker | npm |
| 2026-11-10 | `zod` 4.6.7 | Parche de seguridad (agotamiento de memoria) | `npm audit` |
