# 00 · Inventario de entornos, repositorios y datos

Fecha de corte: 10 de noviembre de 2026 (America/Lima). Cada dato lleva su estado: **verificado** (comprobado en esta sesión con un comando o consulta), **inferido** (deducido del código o la documentación) o **no accesible**.

## Mapa repositorio → proyecto → datos → URL

| Sistema | Repositorio (carpeta local) | Proyecto Vercel | Origen de datos | URL estable | Estado |
| --- | --- | --- | --- | --- | --- |
| Stock | `FundigSac/Stock-Web-Automate` (`Stock-Web-Automate/`) | `fundigsac-stock-dashboard` | Supabase `vdxhhuzivzbtbiahjork` (fundigsac-stock, sa-east-1) | https://fundigsac-stock-dashboard.vercel.app/ | verificado |
| Admin | `FundigSac/Admin` (`Admin/`) | `fundigsac-admin` | Hasta hoy: datos de demostración en `localStorage`. Desde hoy: Supabase `ufutozmnnifimgfasmbe` (fundigsac-admin), esquema `app` | https://fundigsac-admin.vercel.app/login | verificado |
| Frontend | `FundigSac/Frontend` (`Frontend/`) | `fundigsac-web` | Contenido estático del repositorio; formularios por correo o WhatsApp mientras no haya `BACKEND_URL` | https://fundigsac-web.vercel.app/ | verificado |
| Backend | `FundigSac/Backend` (`Backend/`) | ninguno | PostgreSQL local en Docker | no publicado | verificado |
| Report | `FundigSac/Report` (`Report/`) | ninguno | — | — | verificado |
| Scrapling | clon de `D4Vinci/Scrapling` (`Scrapling/`) | ninguno | — | — | verificado |

Equipo Vercel: `diegos-projects-1a03253b`. Según la memoria del 9 de noviembre, solo `fundigsac-web` despliega con cada push a `main`; Admin y Stock se publican con `vercel deploy --prod` (inferido; se vuelve a comprobar en cada despliegue).

## Herramientas (verificado)

| Herramienta | Versión |
| --- | --- |
| Node.js | 24.21.0 |
| npm | 11.19.0 |
| Git | 2.55.0 |
| Vercel CLI | 65.1.0 |
| Docker | 29.8.2 instalado, motor detenido (Docker Desktop no está corriendo) |
| Python | no instalado (el alias de Microsoft Store responde en su lugar) |
| Supabase CLI | sin sesión iniciada; se usa el conector MCP de Supabase |
| Context7 | disponible por MCP y consultado antes de introducir `postgres` (porsager) |
| Navegador | panel de navegador integrado de Claude; Claude in Chrome disponible como herramienta diferida |

## Datos de Stock (P0) — verificado el 10/11/2026 con conteos exactos

| Tabla | Filas |
| --- | --- |
| `productos` | 187 |
| `personal` | 19 |
| `entradas` | 82 |
| `salidas` | 31 |
| `ajustes` | 1 |
| `ia_uso` | 82 |
| `editores` | 0 |
| `pedidos` | 0 |
| Storage `evidencias` | 38 objetos |

Los registros reales siguen en Supabase y la app los muestra: la vista Stock lista 187 productos (45 con stock, 31 por agotarse, 111 sin stock) y la barra lateral indica «Último movimiento: 9 nov 2026». El texto «Conectando…» que se ve en la portada es el estado previo a la primera lectura; a los pocos segundos pasa a «En línea · Todo subido». No hay pérdida de datos.

## Admin (P0)

El panel publicado funciona solo con datos de demostración porque el Backend Java nunca se publicó. El 10/11/2026 el responsable eligió la opción «Supabase nuevo + API en Vercel». Se creó el proyecto Supabase `fundigsac-admin` (costo cotizado y aceptado: USD 0 al mes) y se aplicó el esquema del Backend (migraciones V1, V2, V4 a V15; se omiten V3 catálogo y la tabla `event_publication`, que solo usa Spring Modulith) dentro del esquema `app`, que la API pública de Supabase no expone.

El acceso es con el rol `fundigsac_api`: solo DML, sin `DELETE` sobre registros con valor legal, solo inserción en historiales y auditoría, RLS activo en todas las tablas. Su contraseña se generó en el equipo y a Postgres solo se envió el verificador SCRAM.

## Riesgos y bloqueos abiertos

| Riesgo | Detalle | Estado |
| --- | --- | --- |
| Correo transaccional | El ingreso del personal necesita enviar un código por correo. Falta una cuenta de Resend (u otro SMTP) creada por el responsable. | bloqueado por acceso |
| Docker detenido | Impide correr las pruebas de integración del Backend Java con Testcontainers en este equipo. | no bloqueante |
| Python ausente | Scrapling no se puede volver a ejecutar en local; el estudio de competencia del 9/11 ya está en `competencia/`. | no bloqueante |
| Favoritos de Chrome | Los marcadores del navegador no son legibles por la integración; el inventario del 9/11 está en `diseno/referencias.md`. | no accesible |
