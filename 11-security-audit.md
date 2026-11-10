# 11 · Auditoría de seguridad (API nueva)

Referencia: OWASP ASVS 5.0 (V2 autenticación, V3 sesiones, V4 control de acceso, V5 validación, V8 datos, V11 lógica de negocio). Revisión del código propio de esta sesión; no se hicieron pruebas intrusivas contra producción.

| ID | Hallazgo | Criticidad | Estado | Prueba |
| --- | --- | --- | --- | --- |
| S-01 | La reutilización de un refresh revocado no revocaba la familia: el `UPDATE` quedaba dentro de la transacción que se deshacía al lanzar el error. | Alta | Corregido antes de publicar | `staff-access` «refresh rota y la reutilización revoca la familia» |
| S-02 | La auditoría del ingreso usaba otro `resource_type` y no aparecía en la actividad del panel. | Baja | Corregido | `staff-accounts` actividad |
| S-03 | Admin sin backend real: cualquiera con el enlace veía un panel de demostración con datos inventados. | Media | Resuelto en rama; se publica al configurar el correo | — |
| S-04 | Libro de Reclamaciones sin registro: el sitio solo abría correo o WhatsApp, sin número correlativo ni constancia. | Alta (cumplimiento) | Resuelto en rama; se publica al configurar el correo | `forms` hoja REC |

## Controles implementados

- Acceso del personal sin contraseña: código de 6 dígitos, 10 minutos, 5 intentos, un solo uso, reenvío ≥60 s, respuesta idéntica exista o no la cuenta, hash HMAC ligado a la cuenta.
- Clientes: scrypt (N=2^15), bloqueo de 15 min tras 5 fallos, comparación con hash ficticio para igualar tiempos, política 12–128 sin contraseñas comunes ni el correo.
- Tokens: acceso HS256 de 15 min con sello de seguridad (cambiar roles, desactivar o restablecer contraseña invalida los tokens vigentes); refresh rotativo guardado como SHA-256, 12 h personal / 14 días clientes.
- Autorización en el servidor por permiso en cada endpoint, denegación por defecto; el BFF guarda tokens en cookies `HttpOnly`, `SameSite=Strict`, `Secure`.
- Validación estricta: campos desconocidos rechazados, límites de longitud, RUC con dígito verificador, documentos por tipo, cuerpos ≤64 KB, consultas parametrizadas (postgres.js).
- Límites de frecuencia en Postgres por IP y por correo; 429 con `Retry-After`.
- Concurrencia optimista con `If-Match`/`ETag`; idempotencia de 24 h en formularios públicos.
- Base: esquema no expuesto por la API REST de Supabase, RLS activo, rol sin `DELETE` en registros legales, historiales solo inserción, trigger que impide reescribir una hoja de reclamación o su respuesta.
- Secretos: solo en variables cifradas de Vercel y en archivos locales ignorados por Git; nunca impresos.

## Pendientes

- Verificar el dominio `fundigsac.com` en Resend (SPF/DKIM/DMARC) para que los correos al público no caigan en spam.
- Revisión legal humana del texto de los correos y del cómputo de plazos (feriados 2026–2027 cargados a mano).
- `npm audit --omit=dev` de Admin: 1 alta preexistente en `zod` <4.6.6 (agotamiento de memoria). Corregida con `zod` 4.6.7 (commit d74ac8d); ahora 0 vulnerabilidades.
