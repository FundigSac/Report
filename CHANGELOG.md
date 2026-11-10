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

### Producción (tarde)
- **Admin**: panel real en producción (sin demo). Tema e idioma en la barra superior, densidad compacta y números del mes abiertos en escritorio; entrada «Regla de tinta». 99c1370, 3ae4319
- **Sitio**: formularios conectados a la API real; cuentas de clientes apagadas hasta verificar el dominio de correo (`CUSTOMER_ACCOUNTS=off`); IP del visitante firmada para los límites. 3cf9e4d, 72030f3
- **Stock**: Resumen accesible en el celular, gráfico de 30 días a pedido, tabla de trabajadores en escritorio; entrada «Línea de flujo». bbffd82, c574d21
- **Datos**: respaldo cifrado de Stock con restauración aislada y conciliación exacta (huella de saldos idéntica).
