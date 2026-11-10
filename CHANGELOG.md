# Changelog

## 2026-11-10

### Admin (`feat/api-real-supabase`)
- **feat(api)** API `/api/v1` con el contrato del Backend Java sobre Supabase `fundigsac-admin`: acceso del personal con código, formularios públicos (cotización, consulta, Libro de Reclamaciones, derechos ARCO, consentimiento), colas del personal, cuentas, roles, indicadores, actividad y cuentas de clientes. 19bbc89
- **feat(bff)** El panel atiende su API en el mismo proceso (`BACKEND_URL=self`). 30040c5
- **fix(mail)** Reintentos de correo también tras lecturas y durante ~1 día. 39ebc0a
- **fix(deps)** `zod` 4.6.7 (vulnerabilidad alta). d74ac8d
- Pruebas: 23 de integración (`npm run test:api`).

### Datos
- Supabase nuevo `fundigsac-admin` (USD 0/mes) con esquema `app` y rol de mínimo privilegio. Stock: sin cambios, datos verificados (187 productos, 82 entradas, 31 salidas, 19 trabajadores, 38 fotos).
