# Changelog

## 2026-11-10 (noche) · tanda 2

### Sitio (6ddbb32)
- Tabla «Medidas disponibles» en las fichas, con enlace por medida (X1-4, X5-4).
- Chips DN/PN, cantidad y botón «Agregar a cotización» en la ficha (B10-2).
- Conteo en los filtros de /productos y tarjetas de Termofusión y Medidores (X5-1).
- Accesibilidad: puntos del carrusel de 24 px o más; el texto de las tarjetas ya no queda transparente por la animación.
- Fotos de la portada más livianas en celular (unos 53 KB menos).
- Correcciones para Firefox y Safari: desborde del pie y búsqueda escrita antes de terminar la carga.

### Admin (e8f086a)
- KPI como filtros (B4-1), cotizaciones por etapa (B2-2), matriz de permisos agrupada y línea de tiempo de estados (B12-4).
- «Limpiar filtros» ya no interrumpe la navegación siguiente.

### Stock (d10c00e)
- Barra de salud del inventario (B25-1), aviso sin conexión con la hora de la copia (X10-4), total y título de la tabla (B6-2), reintento sin perder la foto (X10-5) y flechas del teclado en Movimientos (B23-3).
- Fotos en Safari con navegación privada; «Conectado» falso sin red; isla del reporte en tabletas.

### Pruebas
- Primera corrida en Firefox y WebKit en las tres apps (ver 09-test-matrix).

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

### Diseño restaurado y mejoras de favoritos (noche)
- El responsable rechazó el rediseño del 9/11. Se restauró el diseño del 4/11 (sitio), 20/10 (Admin) y 30/10 (Stock), conservando API real, modo sin conexión y SEO; el sitio recupera además 7 familias y 85 fichas con ese diseño.
- Fase 2 V3: 71 favoritos inventariados, 30 de diseño revisados en Claude in Chrome (29 con contenido), 14 referencias externas nuevas, 268 ideas; Scrapling real sobre 15 fuentes (12 rastreadas, 3 bloqueadas por robots/403, respetadas).
- 22 ideas implementadas y publicadas (ver `03b-ideas-to-code.csv`): contraste AA del naranja, filtros con chips y conteo, búsqueda vacía útil, línea de especificaciones verificadas, botón de envío con estados, resumen de errores, constancia imprimible del Libro, carrito accesible; Admin: estados vacíos, plazo legal con ícono, conteos, fechas con hora exacta, cifras tabulares, mensaje de éxito persistente; Stock: estado con ícono y texto, movimientos con signo, esqueletos de carga, controles de 48 px, pestaña activa, error/vacío distintos.
