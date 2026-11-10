# Respaldo y restauración de Stock

- `dump.mjs <archivo-env> <carpeta-destino> <archivo-clave>`: lee las tablas con la clave pública (igual que la app) y las 38 fotos públicas de `evidencias` (lista de nombres en `names.txt`, obtenida de `storage.objects`), y guarda todo en un archivo cifrado AES-256-GCM. La clave queda en un archivo aparte.
- `restore.mjs <archivo-cifrado> <archivo-clave>`: descifra en un Postgres en memoria (PGlite), sin red, y calcula conteos, saldos y una huella MD5 de los saldos por código para compararla con producción.
- Dependencias: `npm i @supabase/supabase-js@2 @electric-sql/pglite@0.3`.

El respaldo y su clave se guardan fuera de los repositorios. Nunca se suben a Git.
