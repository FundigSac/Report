# 07 · Preservación de datos y migraciones

Fecha: 10 de noviembre de 2026. Solo cifras agregadas; sin datos personales.

## Stock (Supabase `vdxhhuzivzbtbiahjork`, producción)

Fuente de verdad: Postgres de Supabase (tablas `productos`, `personal`, `entradas`, `salidas`, `pedidos`, `ajustes`, `editores`, `ia_uso`; vistas `stock_items`, `trabajadores`) y Storage `evidencias` (bucket público). La app además guarda una cola sin conexión en IndexedDB de cada dispositivo: no se tocó, ni se borró caché o almacenamiento.

### Respaldo verificable

| Elemento | Valor |
| --- | --- |
| Archivo | `C:\Users\Productora Zamar\Backups\fundigsac-stock\stock-2026-11-10.json.enc` (fuera de los repos) |
| Cifrado | AES-256-GCM; la clave está en un archivo separado, fuera de los repos |
| Tamaño | 6,37 MB cifrado |
| SHA-256 del contenido | `3167950adf91e62332b42d9a4f4ffe711c2f93a61dc9d66c34d394de23b5dff3` |
| Contenido | productos 187, personal 19, entradas 82, salidas 31, pedidos 0, ajustes 1, editores 0; fotos 38/38 (4 696 738 bytes) |
| No incluido | `ia_uso` (contador de uso del asistente; la clave pública no lo lee por RLS). Respaldo nativo de Supabase: el plan gratis no permite descargarlo. |
| Scripts | `Report/stock/respaldo/` |

### Prueba de restauración aislada (PGlite en memoria, sin red)

| Métrica | Restaurado | Producción (consulta en vivo) |
| --- | --- | --- |
| Saldo total | 511 | 511 (`sum(queda)` de `stock_items`) |
| Entradas vigentes (unidades) | 530 | 530 |
| Salidas vigentes (unidades) | 19 | 19 |
| Huella MD5 de saldos por código | c889a94a70e07e6d1607f200b38c79a2 | c889a94a70e07e6d1607f200b38c79a2 |
| Fotos con SHA-256 íntegro | 38/38 | 38 objetos |
| Saldos negativos | — | 0 |

Resultado: **respaldo restaurable y conciliado; cero diferencias**.

### Migraciones en Stock

Ninguna en esta sesión. Las cinco del 9/11/2026 siguen como estaban.

## Admin / API (Supabase `ufutozmnnifimgfasmbe`, nuevo)

Proyecto nuevo, sin datos previos: no había nada que migrar. Las migraciones son aditivas y están descritas en `Admin/supabase/README.md`. Los datos sintéticos de las pruebas se borraron y los correlativos se reiniciaron antes de publicar. Las únicas filas son dos cuentas de administrador.

## Plan de rollback

| Sistema | Aplicación | Datos |
| --- | --- | --- |
| Admin | Promover el despliegue anterior `fundigsac-admin-eo3dqwmj7-…` (demo) con `vercel promote` o desde el panel de Vercel. | La base nueva queda intacta; no hay datos que revertir. |
| Sitio | Promover `fundigsac-248vclsh2-…` o quitar `BACKEND_URL`. | Los formularios ya enviados se conservan en la base. |
| Stock | Sin cambios. | Restaurar desde el respaldo cifrado (script `restore.mjs` como base de una carga real). |
