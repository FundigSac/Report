# 08 · Contratos de la API `/api/v1` que usan Admin y Frontend

Fuente: código del Backend Java (`Backend/src/main/java/com/fundigsac/**`, abreviado `…/`), `application.yml`, migraciones Flyway y los BFF de `Admin/src` y `Frontend/src`. Objetivo: reimplementar en TypeScript (route handlers de Next.js + Postgres) **solo** lo que llaman los dos clientes, con el mismo comportamiento observable.

---

## 0. Convenciones comunes

### 0.1 Transporte
| Aspecto | Contrato |
|---|---|
| Base | `BACKEND_URL` + `/api/v1/...` (los BFF llaman siempre server-to-server, timeout 10 s, `redirect: manual`, `cache: no-store`). |
| Cabeceras que envían los BFF | `Accept: application/json`, `Accept-Language: es-PE`, `Content-Type: application/json` (si hay cuerpo), `Authorization: Bearer <access>` (si hay sesión), `X-Forwarded-For: <ip>` (solo si `VERCEL=1` o `TRUST_PROXY=1`; IP validada `^[0-9a-fA-F:.]{3,45}$`), `Idempotency-Key` (solo cotización y reclamo, Frontend), `If-Match` (Admin, `^"?\d{1,12}"?$`), `X-Receipt-Token` (constancia de cotización). |
| Método por defecto en BFF | `POST` si hay cuerpo, si no `GET` (Admin reenvía el método real: GET/POST/PUT/PATCH/DELETE). |
| JSON estricto | `spring.jackson.deserialization.fail-on-unknown-properties=true`: un campo no declarado ⇒ **400 `UNKNOWN_FIELD`** con `errors:[{field:<nombre>,code:"UNKNOWN_FIELD"}]`. Tipo erróneo (p. ej. UUID/enum/fecha inválidos) ⇒ **400 `INVALID_VALUE`** con `errors[0].field` = ruta (`items[0].quantity`). JSON roto ⇒ **400 `MALFORMED_REQUEST`**. |
| Tamaño | Cuerpo máx. 64 KB (`fundigsac.web.max-body-bytes=65536`) ⇒ **413 `PAYLOAD_TOO_LARGE`**. (BFF: Frontend forms 48 KB, account 8 KB; Admin proxy 64 KB, session 4 KB.) |
| Parámetros de consulta | Rechazo de U+0000 en cualquier query param ⇒ 400 `VALIDATION_ERROR` / `INVALID_CHARACTER`. |
| Fechas | Instantes ISO-8601 UTC (`2026-11-10T15:04:05.123Z`); fechas de negocio `YYYY-MM-DD` calculadas en `America/Lima` (`…/shared/domain/PeruTime.java`). |
| Respuestas | `Cache-Control: no-store` en altas públicas, constancias y fichas de personal. CORS no aplica (BFF server-side). |

### 0.2 Formato de error (RFC 9457) — `…/shared/web/ApiExceptionHandler.java`
`Content-Type: application/problem+json`
```json
{ "type":"about:blank", "title":"Bad Request", "status":400, "detail":"Revise los campos indicados.",
  "code":"VALIDATION_ERROR", "requestId":"…",
  "errors":[{"field":"contact.ruc","code":"INVALID_RUC","message":"El RUC no es válido (11 dígitos con dígito verificador)."}] }
```
`errors` solo aparece si hay errores de campo. Mapeo excepción → HTTP:

| Origen | HTTP | `code` |
|---|---|---|
| Bean Validation del DTO (todos los errores juntos) | 400 | `VALIDATION_ERROR`; `errors[].code`: NotBlank/NotNull/NotEmpty→`REQUIRED`, Size→`INVALID_LENGTH`, Email→`INVALID_EMAIL`, Pattern→`INVALID_FORMAT`, Min/Max/Positive/DecimalMin/DecimalMax/Digits→`OUT_OF_RANGE`, AssertTrue→`MUST_ACCEPT`, Past*/Future*→`INVALID_DATE`, otro→`INVALID_VALUE` |
| Validación de dominio `ValidationException` (solo **la primera** violación) | 400 | `VALIDATION_ERROR` + `errors[0]` con code de dominio (`REQUIRED`, `TOO_SHORT`, `TOO_LONG`, `TOO_MANY`, `INVALID_RUC`, `INVALID_EMAIL`, `INVALID_PHONE`, `INVALID_TOKEN`, …) |
| `NotFoundException` | 404 | p. ej. `QUOTE_NOT_FOUND` |
| `ConflictException` | 409 | p. ej. `INVALID_TRANSITION` |
| `RuleViolationException` | 422 | p. ej. `EMPTY_QUOTE` |
| `ForbiddenException` | 403 | p. ej. `EMAIL_NOT_VERIFIED` |
| `UnauthorizedException` | 401 | p. ej. `INVALID_CREDENTIALS` |
| `StaleVersionException` | 412 | `STALE_VERSION` |
| Falta `If-Match` | 428 | `IF_MATCH_REQUIRED` |
| `If-Match` no numérico | 400 | `VALIDATION_ERROR` / field `If-Match` / `INVALID_ETAG` |
| Rate limit | 429 | `RATE_LIMITED` + cabecera `Retry-After: <segundos>` |
| Sin token / token inválido-revocado (filtro de seguridad) | 401 | `AUTHENTICATION_REQUIRED` / `INVALID_TOKEN` (+ `WWW-Authenticate: Bearer …`) |
| Rol/permiso insuficiente | 403 | `FORBIDDEN` |
| Integridad SQL (clase 22 → 400 `INVALID_VALUE`; resto → 409 `CONFLICT`) / inesperado | 400/409/500 | `INTERNAL_ERROR` para 500 |
| Ruta no mapeada / UUID inválido en path | 404 / 400 | `NOT_FOUND` / `BAD_REQUEST` |

**Lo que ve el navegador (relay de ambos BFF):** `{ "error": <code>, "message": <detail>, "errors": [{field,code,message}] }` con el mismo status; sin Backend `503 {error:"NOT_CONFIGURED"}`, caído `503 {error:"UNREACHABLE"}`; un 204 se convierte en `200 {ok:true}` (o el `okBody` del BFF). Se reenvía `Retry-After` y (Admin) `ETag`.

### 0.3 Concurrencia, paginación
- `GET` de fichas del personal devuelve `ETag: "<version>"` (versión entera de la fila). Toda escritura de personal sobre registro versionado exige `If-Match` (acepta `"7"`, `7`, `W/"7"`): falta ⇒ 428, distinto ⇒ 412 `STALE_VERSION`. Cada `UPDATE` hace `version = version + 1` (en `user_accounts` también al iniciar sesión, porque se guarda `last_login_at`). La respuesta de la escritura trae el nuevo `ETag`.
- Listas: `page` (≥0, def. 0), `size` (1–100, def. 20; `@Max(100)` ⇒ 400 si >100). Respuesta `PageResult`: `{items:[…], page, size, totalItems, totalPages}` (`totalPages = ceil(total/size)`, 0 si vacío).

### 0.4 Límites de frecuencia (`…/shared/web/RateLimitInterceptor.java`, `application.yml`)
Token bucket en memoria por **(política, IP remota)**; en prod `server.forward-headers-strategy=native` ⇒ la IP sale de `X-Forwarded-For`. Recarga “greedy” completa en el periodo. Respuesta OK añade `RateLimit-Remaining`.

| Política | Capacidad / periodo | Endpoints |
|---|---|---|
| `public-form` | 5 / 10 min | POST quotes, inquiries, complaints, privacy/requests |
| `consent` | 30 / 1 min | POST privacy/consents |
| `receipt` | 30 / 1 min | GET quotes/{folio}/receipt (y complaints/{folio}/receipt) |
| `register` | 5 / 1 h | POST auth/register |
| `login` | 10 / 15 min | POST auth/login, auth/google (y account/password, DELETE account) |
| `token` | 10 / 15 min | POST auth/verify-email, auth/refresh, auth/password/reset, auth/staff/code/verify |
| `password-reset` | 3 / 1 h | POST auth/password/forgot, auth/verify-email/resend |
| `login-code` | 5 / 15 min | POST auth/staff/code |
| — | sin límite | auth/logout, todo `/staff/**`, `/account/me` |

> Ojo: `auth/refresh` comparte la política `token` (10/15 min por IP del visitante). Los BFF deduplican renovaciones simultáneas 15 s.

### 0.5 Autenticación (resumen; detalle en §7)
- Público (`permitAll`): POST quotes, inquiries, complaints, privacy/consents, privacy/requests; GET quotes/*/receipt; POST `/auth/**`.
- `/api/v1/account/**` ⇒ `ROLE_CUSTOMER`. `/api/v1/staff/**` ⇒ `ROLE_STAFF` (cualquier rol interno) + permiso fino por endpoint (`@PreAuthorize`).
- Bearer opaco para los clientes: ningún BFF decodifica el JWT; solo usan `accessToken`, `expiresIn`, `refreshToken`, `refreshExpiresIn`.

---

## 1. Índice de endpoints usados

Rutas Java relativas a `Backend/src/main/java/com/fundigsac/`.

| # | Método y ruta | Quién llama | Auth | Java |
|---|---|---|---|---|
| 1 | POST `/quotes` | FE `/api/forms/quote` | ninguna (bearer cliente opcional) | `quotation/web/QuoteController.java` |
| 2 | GET `/quotes/{folio}/receipt` | FE `cotizar/confirmacion/page.tsx` | `X-Receipt-Token` | idem |
| 3 | POST `/inquiries` | FE `/api/forms/inquiry` | ninguna (bearer reenviado, ignorado) | `inquiry/web/InquiryController.java` |
| 4 | POST `/complaints` | FE `/api/forms/complaint` | ninguna | `complaint/web/ComplaintController.java` |
| 5 | POST `/privacy/requests` | FE `/api/forms/privacy-request` | ninguna | `privacy/web/PrivacyController.java` |
| 6 | POST `/privacy/consents` | FE `/api/forms/consent` | ninguna | idem |
| 7 | POST `/auth/register` | FE `/api/account/register` | ninguna | `identity/web/AuthController.java` |
| 8 | POST `/auth/verify-email` | FE `/api/account/verify-email` | ninguna | idem |
| 9 | POST `/auth/verify-email/resend` | FE `/api/account/resend-verification` | ninguna | idem |
| 10 | POST `/auth/login` | FE `/api/account/login` | ninguna | idem |
| 11 | POST `/auth/google` | FE `/api/auth/callback/google` | ninguna | idem |
| 12 | POST `/auth/refresh` | FE y Admin (`session.ts`) | refresh token en cuerpo | idem |
| 13 | POST `/auth/logout` | FE `/api/auth/logout`, Admin `/api/session/logout` | refresh token en cuerpo | idem |
| 14 | POST `/auth/password/forgot` | FE `/api/account/forgot-password` | ninguna | idem |
| 15 | POST `/auth/password/reset` | FE `/api/account/reset-password` | ninguna | idem |
| 16 | GET `/account/me` | FE `modules/backend/account.ts` | bearer CUSTOMER | `identity/web/AccountController.java` |
| 17 | POST `/auth/staff/code` | Admin `/api/session/code` | ninguna | `identity/web/StaffAccessController.java` |
| 18 | POST `/auth/staff/code/verify` | Admin `/api/session/verify` | ninguna | idem |
| 19 | GET `/staff/profile` | Admin `/api/session/verify` | bearer STAFF (sin permiso fino) | `identity/web/StaffUserController.java` |
| 20 | GET `/staff/users` | Admin `staffList()` (`?size=100`) | `users:manage` | idem |
| 21 | POST `/staff/users` | Admin `createUser` | `users:manage` | idem |
| 22 | PUT `/staff/users/{id}/roles` | Admin `updateUser` | `users:manage` + If-Match | idem |
| 23 | GET `/staff/accounts` | Admin `listUsers`, `exportCsv` | `users:manage` | `backoffice/web/AccountDirectoryController.java` |
| 24 | GET `/staff/accounts/stats` | Admin `stats` | `users:manage` | idem |
| 25 | GET `/staff/accounts/activity` | Admin `listActivity` | `users:manage` | idem |
| 26 | GET `/staff/accounts/{id}` | Admin (ficha y ETag) | `users:manage` | idem |
| 27 | PUT `/staff/accounts/{id}/notes` | Admin | `users:manage` (sin If-Match) | idem |
| 28 | PATCH `/staff/accounts/{id}` | Admin | `users:manage` + If-Match | `identity/web/StaffAccountController.java` |
| 29 | POST `/staff/accounts/{id}/disable` | Admin | `users:manage` + If-Match | idem |
| 30 | POST `/staff/accounts/{id}/enable` | Admin | `users:manage` + If-Match | idem |
| 31 | DELETE `/staff/accounts/{id}` | Admin `deleteUsers` | `users:manage` + If-Match | idem |
| 32 | POST `/staff/accounts/{id}/verification-email` | Admin | `users:manage` | idem |
| 33 | POST `/staff/accounts/{id}/password-reset` | Admin | `users:manage` | idem |
| 34 | GET `/staff/quotes` | Admin `fetchAll("quotes")` | `quote:read` | `quotation/web/StaffQuoteController.java` |
| 35 | GET `/staff/quotes/{id}` | Admin | `quote:read` | idem |
| 36 | POST `/staff/quotes/{id}/assign` | Admin | `quote:manage` + If-Match | idem |
| 37 | POST `/staff/quotes/{id}/status` | Admin `moveQuote` | `quote:manage` + If-Match | idem |
| 38 | GET `/staff/inquiries` | Admin | `inquiry:read` | `inquiry/web/InquiryController.java` |
| 39 | GET `/staff/inquiries/{id}` | Admin | `inquiry:read` | idem |
| 40 | POST `/staff/inquiries/{id}/assign` | Admin | `inquiry:manage` + If-Match | idem |
| 41 | POST `/staff/inquiries/{id}/status` | Admin | `inquiry:manage` + If-Match | idem |
| 42 | GET `/staff/complaints` | Admin | `complaint:read` | `complaint/web/ComplaintController.java` |
| 43 | GET `/staff/complaints/{id}` | Admin | `complaint:read` | idem |
| 44 | POST `/staff/complaints/{id}/assign` | Admin | `complaint:manage` + If-Match | idem |
| 45 | POST `/staff/complaints/{id}/notes` | Admin | `complaint:manage` + If-Match | idem |
| 46 | POST `/staff/complaints/{id}/answer` | Admin | `complaint:manage` + If-Match | idem |
| 47 | GET `/staff/privacy/requests` | Admin | `privacy:read` | `privacy/web/PrivacyController.java` |
| 48 | GET `/staff/privacy/requests/{id}` | Admin | `privacy:read` | idem |
| 49 | POST `/staff/privacy/requests/{id}/start` | Admin | `privacy:manage` + If-Match | idem |
| 50 | POST `/staff/privacy/requests/{id}/conclude` | Admin | `privacy:manage` + If-Match | idem |

Todos los `/staff/**` sin permiso devuelven 403 `FORBIDDEN`; sin sesión 401.

---

## 2. Formularios públicos (Frontend)

### 2.1 POST `/api/v1/quotes` — solicitar cotización
`quotation/web/QuoteController.java`, `quotation/application/QuoteSubmissionService.java`, `quotation/domain/*`
- Cabeceras: `Idempotency-Key` opcional (BFF lo reenvía si cumple `^[A-Za-z0-9_-]{8,128}$`), `Authorization` opcional (si el token tiene `ROLE_CUSTOMER`, `customer_id = sub`; si no, null). Rate `public-form`.
- Cuerpo (`SubmitQuoteRequest`):

| Campo | Tipo | Req. | Reglas DTO → dominio |
|---|---|---|---|
| `origin` | string | sí | `GENERAL_FORM\|PRODUCT_FORM\|PROCUREMENT` (Pattern; `CART` existe en el enum pero el DTO no lo acepta). Prefijo de folio: PROCUREMENT→`REQ`, resto→`COT` |
| `contact.companyName` | string | sí | 2–160 |
| `contact.ruc` | string | sí | `^\d{11}$` + dígito SUNAT (prefijo 10/15/16/17/20, mód. 11 pesos 5-4-3-2-7-6-5-4-3-2) ⇒ `INVALID_RUC` field `contact.ruc` |
| `contact.contactName` | string | sí | 2–120 |
| `contact.position` | string | no | ≤120 |
| `contact.email` | string | sí | @Email, ≤254; dominio: minúsculas, regex estricta, local ≤64 ⇒ `INVALID_EMAIL` |
| `contact.phone` | string | sí | ≤24; dominio `^\+?[0-9 ().-]{7,24}$`, normaliza a `^\+?[0-9]{7,15}$` ⇒ `INVALID_PHONE` |
| `project` | object | no | (si falta, todo null) |
| `project.projectType` | string | no | ≤120 (FE manda “Agua y saneamiento”, “Redes y matrices”, “Alcantarillado y drenaje”, “Otro”) |
| `project.deliveryDepartment` | string | no | ≤60 |
| `project.deliveryPlace` | string | no | ≤200 |
| `project.requestedDeliveryDate` | `YYYY-MM-DD` | no | entre hoy (Lima) y hoy+3 años ⇒ `INVALID_DATE` field `project.requestedDeliveryDate` |
| `project.message` | string | no | ≤4000, multilínea |
| `items` | array | no | ≤50 (`TOO_MANY`) |
| `items[].productSlug` | string | no | ≤120. Si viene: debe existir producto **publicado** con slug `^[a-z0-9]+(-[a-z0-9]+)*$` ⇒ si no 400 `errors[0]={field:"items.productSlug",code:"UNKNOWN_PRODUCT"}`; se copian nombre, sku, id |
| `items[].productName` | string | condicional | ≤200; obligatorio sin slug (`items.productName` `REQUIRED`); dominio 2–200 |
| `items[].variantLabel` | string | no | ≤120; con slug debe estar en las variantes del producto (si tiene) ⇒ `UNKNOWN_VARIANT` field `items.variantLabel` |
| `items[].quantity` | number | sí | >0, ≤1 000 000, ≤7 enteros y ≤3 decimales |
| `items[].unit` | string | sí | ≤10; `und\|juego\|lote\|m\|kg` o `UNIT\|SET\|LOT\|METER\|KILOGRAM` ⇒ `INVALID_UNIT` field `items.unit`. Se guarda el código (`und`) y la etiqueta (`Unidades`, `Juego completo`, `Lote`, `Metros lineales`, `Kilogramos`) |
| `items[].addons` | string[] | no | ≤10 elementos de 1–120, deduplicados |
| `items[].notes` | string | no | ≤1000 |
| `privacyNoticeVersion` | string | sí | 1–20 (FE: `"2026-10"`) |
| `acceptPrivacyNotice` | boolean | sí | debe ser `true` (`MUST_ACCEPT`) |
| `website` | string | no | honeypot: debe estar vacío (`INVALID_LENGTH`) |

- Reglas: sin ítems y `message` <10 caracteres ⇒ **422 `EMPTY_QUOTE`**. Texto normalizado (quita controles, colapsa espacios). Estado inicial `RECEIVED`, historial `{from:null,to:RECEIVED,actorId:customerId}`. Folio vía `folio_sequences` (§7.1) en la misma transacción.
- **201** + `Location: /api/v1/quotes/{folio}/receipt`:
```json
{"folio":"COT-2026-000042","status":"RECEIVED","receivedAt":"…Z","receiptToken":"<b64url>",
 "receiptUrl":"/api/v1/quotes/COT-2026-000042/receipt","message":"Solicitud registrada. Ventas la revisará y le responderá por correo. Guarde su folio."}
```
  El BFF devuelve al navegador solo `{folio}` y guarda `{folio, receiptToken}` firmado en la cookie httpOnly `fundigsac-receipt` (path `/cotizar`, 30 min).
- Idempotencia: scope `quote` (§7.2). Reintento igual ⇒ misma respuesta 201 con el mismo folio; misma clave con otro cuerpo ⇒ **409 `IDEMPOTENCY_KEY_REUSED`**; en curso ⇒ 409 `REQUEST_IN_PROGRESS`; clave mal formada ⇒ 400 `INVALID_IDEMPOTENCY_KEY`.
- Cliente: 400 con `errors[].code ∈ {UNKNOWN_PRODUCT, UNKNOWN_VARIANT}` ⇒ reintenta sin `productSlug` (texto libre) con clave `<key>-libre`. 400/409/422 ⇒ “invalid”; 429 ⇒ “limited” (`Retry-After`, def. 60); otro/503 ⇒ “offline” (envío por correo/WhatsApp).
- Correos: `QUOTE_RECEIPT` y `QUOTE_SALES` (§10). Auditoría `QUOTE_SUBMITTED`.

### 2.2 GET `/api/v1/quotes/{folio}/receipt` — constancia
- Path `folio` ≤16, formato `^[A-Z]{3}-\d{4}-\d{6}$` ⇒ si no 400 `VALIDATION_ERROR`/`INVALID_FOLIO` (field `folio`). Cabecera `X-Receipt-Token`. Rate `receipt`.
- Token válido = `base64url_nopad(HMAC_SHA256(receipt_key, "quote:" + folio))`, comparación en tiempo constante. Token ausente/erróneo o folio inexistente ⇒ **404 `QUOTE_NOT_FOUND`**.
- **200**: `{folio, status, receivedAt, companyName, contactName, email:"c***@dominio", items:[ItemView]}` (ItemView en §6.1). El cliente usa `folio` y `receivedAt`; error `http` ⇒ página sin lead; `unreachable/not_configured` ⇒ aviso de no disponible.

### 2.3 POST `/api/v1/inquiries` — consulta de contacto
`inquiry/web/InquiryController.java`, `inquiry/application/InquiryService.java`, `inquiry/domain/Inquiry.java`
- Rate `public-form`. `Idempotency-Key` aceptado (scope `inquiry`) pero el BFF **no** lo envía. Bearer reenviado e ignorado.

| Campo | Tipo | Req. | Reglas |
|---|---|---|---|
| `reason` | string | no | `GENERAL\|TECHNICAL\|COMMERCIAL\|DOCUMENTATION\|MEETING\|AFTER_SALES\|OTHER`; null ⇒ `GENERAL` (FE manda GENERAL, DOCUMENTATION o MEETING) |
| `fullName` | string | sí | 2–120 |
| `companyName` | string | sí | 2–160 |
| `ruc` | string | no | `""` o `^\d{11}$` + SUNAT (`INVALID_RUC` field `ruc`) |
| `position` | string | no | ≤120 |
| `email` | string | sí | @Email ≤254 + dominio |
| `phone` | string | sí | ≤24 + dominio |
| `message` | string | sí | 10–4000 |
| `requestedDocument` | string | no | ≤200 |
| `privacyNoticeVersion` | string | sí | ≤20 |
| `acceptPrivacyNotice` | boolean | sí | `true` |
| `website` | string | no | vacío |

- Folio prefijo `CON`. Estado `RECEIVED`; evento de historial `{from:null,to:RECEIVED}`.
- **201** + `Location: /api/v1/inquiries/{folio}`: `{"folio":"CON-2026-000001","status":"RECEIVED","receivedAt":"…","message":"Consulta registrada. Le responderemos por correo o teléfono."}`. Cliente usa `folio`.
- Correos `INQUIRY_RECEIPT`, `INQUIRY_SALES`. Auditoría `INQUIRY_RECEIVED`.

### 2.4 POST `/api/v1/complaints` — Libro de Reclamaciones
`complaint/web/ComplaintController.java`, `complaint/application/ComplaintService.java`, `complaint/domain/Complaint.java`, `complaint/domain/ResponseDeadlinePolicy.java`
- Rate `public-form`. `Idempotency-Key` (scope `complaint`; el FE lo manda y lo regenera tras invalid/limited).

| Campo | Tipo | Req. | Reglas |
|---|---|---|---|
| `kind` | string | sí | `CLAIM` (reclamo) \| `GRIEVANCE` (queja) |
| `consumerName` | string | sí | 2–160 |
| `documentType` | string | sí | `DNI\|CE\|PASSPORT\|RUC` |
| `documentNumber` | string | sí | ≤12; se quitan espacios/puntos/guiones y se pasa a mayúsculas; DNI `\d{8}`, CE `[A-Z0-9]{9,12}`, PASSPORT `[A-Z0-9]{6,12}`, RUC SUNAT ⇒ `INVALID_DOCUMENT` field `documentNumber` |
| `email` | string | sí | @Email ≤254 + dominio |
| `phone` | string | sí | ≤24 + dominio |
| `address` | string | sí | 5–300 |
| `minor` | boolean | no (def. false) | si `true` exige apoderado ⇒ si falta 400 field `guardian` `REQUIRED` |
| `guardianName` | string | cond. | ≤160 (2–160); el apoderado solo se crea si `minor && guardianName` no vacío |
| `guardianDocumentType` | string | cond. | `""\|DNI\|CE\|PASSPORT` (RUC ⇒ `INVALID_DOCUMENT` field `guardian.documentType`); vacío con nombre ⇒ `INVALID_VALUE` |
| `guardianDocumentNumber` | string | cond. | ≤12, mismas reglas por tipo |
| `goodType` | string | cond. | `""\|PRODUCT\|SERVICE`; obligatorio si `kind=CLAIM` (400 field `goodType` `REQUIRED`) |
| `goodDescription` | string | sí | 5–1000 |
| `claimedAmount` | number | no | 0–99 999 999.99, ≤2 decimales (`INVALID_AMOUNT` field `amount`) |
| `currency` | string | no | `""\|PEN\|USD`; con monto y sin moneda ⇒ PEN |
| `serviceLocation` | string | no | ≤200 |
| `incidentDate` | `YYYY-MM-DD` | sí | `@PastOrPresent`; dominio: ≤ hoy Lima y ≥ hoy−5 años ⇒ `INVALID_DATE` field `incidentDate` |
| `relatedReference` | string | no | ≤60 |
| `facts` | string | sí | 20–4000 |
| `consumerRequest` | string | sí | 5–2000 |
| `responseChannel` | string | sí | `EMAIL\|POSTAL_ADDRESS` |
| `privacyNoticeVersion` | string | sí | ≤20 |
| `acceptPrivacyNotice` | boolean | sí | `true` |
| `website` | string | no | vacío |

- Folio prefijo `REC` (`REC-AAAA-NNNNNN`). Estado `FILED`. `response_due_on` = §7.4. Evento `FILED`.
- **201** + `Location: /api/v1/complaints/{folio}/receipt`:
```json
{"folio":"REC-2026-000007","kind":"CLAIM","status":"FILED","filedAt":"…Z","responseDueOn":"2026-12-01","receiptToken":"…"}
```
  (`receiptToken` = HMAC con propósito `complaint`). Cliente usa `folio`, `kind`, `responseDueOn`.
- Correos `COMPLAINT_RECEIPT`, `COMPLAINT_LEGAL`. Auditoría `COMPLAINT_FILED`.

### 2.5 POST `/api/v1/privacy/requests` — derechos ARCO / supresión
`privacy/web/PrivacyController.java`, `privacy/application/PrivacyService.java`, `privacy/domain/DataSubjectRequest.java`
- Rate `public-form`. `Idempotency-Key` aceptado (scope `privacy-request`), el BFF no lo envía.

| Campo | Tipo | Req. | Reglas |
|---|---|---|---|
| `type` | string | sí | `ACCESS\|RECTIFICATION\|CANCELLATION\|OPPOSITION\|ACCOUNT_DELETION` (FE: OPPOSITION o ACCOUNT_DELETION) |
| `fullName` | string | sí | 2–160 |
| `email` | string | sí | @Email ≤254 + dominio |
| `documentType` | string | no | `""\|DNI\|CE\|PASSPORT\|RUC` |
| `documentNumber` | string | cond. | ≤12; validado por tipo si hay tipo |
| `details` | string | sí | 10–4000 |
| `acceptPrivacyNotice` | boolean | sí | `true` |
| `website` | string | no | vacío |

No existe `privacyNoticeVersion` en este DTO (enviarlo ⇒ 400 `UNKNOWN_FIELD`).
- Folio `ARC`. Estado `RECEIVED`. **201** + Location: `{"folio":"ARC-2026-000003","status":"RECEIVED","receivedAt":"…"}`.
- Correos `RIGHTS_RECEIPT`, `RIGHTS_PRIVACY`. Auditoría `DSR_RECEIVED`.

### 2.6 POST `/api/v1/privacy/consents` — evidencia de cookies
- Rate `consent`. Sin idempotencia. FE: fire-and-forget (ignora resultado).

| Campo | Tipo | Req. | Reglas |
|---|---|---|---|
| `consentId` | uuid | no | si falta se genera |
| `choices` | `{string:boolean}` | sí | claves **exactamente** `necessary` y `thirdParty` (`INVALID_CHOICES`); `necessary` = true (`MUST_BE_TRUE`, field `choices.necessary`). FE manda `{necessary:true, thirdParty:<bool>}` |
| `policyVersion` | string | sí | ≤20, `^[0-9A-Za-z._-]{1,20}$` (`INVALID_VERSION`); si existe alguna versión publicada de `cookie-policy` en `legal_notices`, debe ser una de ellas ⇒ 400 `UNKNOWN_POLICY_VERSION` |
| `source` | string | sí | `BANNER\|PREFERENCES\|POLICY\|EMBED` |

- **201** `{"consentId":"uuid","policyVersion":"…","recordedAt":"…"}`. Sin IP ni UA. Sin correo.

---

## 3. Cuentas de clientes (Frontend `/api/account/*`, `/api/auth/*`)

`identity/web/AuthController.java`, `identity/application/{Registration,Authentication,PasswordReset,GoogleSignIn,Account}Service.java`, `identity/domain/{UserAccount,PasswordPolicy,SignupProfile}.java`

**TokenResponse** (login, google, refresh, staff verify) — **200**:
```json
{"tokenType":"Bearer","accessToken":"<JWT>","expiresIn":900,"refreshToken":"<43 chars b64url>","refreshExpiresIn":1209600}
```
`refreshExpiresIn` = 1 209 600 (14 d) para CUSTOMER, 43 200 (12 h) para STAFF. Los BFF fijan con él la vida de sus cookies.

**Política de contraseña** (`PasswordPolicy`): 12–128 *code points*; rechaza lista común (`123456789012`, `password1234`, `fundigsac123`, `fundigsac2026`, `administrador`, `qwertyuiop12`, `contraseña123`, …) o <4 caracteres distintos ⇒ `PASSWORD_TOO_COMMON`; contiene la parte local del correo (si ≥4 chars) ⇒ `PASSWORD_CONTAINS_EMAIL`; `PASSWORD_TOO_SHORT`/`PASSWORD_TOO_LONG`. **Nota:** el DTO ya tiene `@Size(min=12,max=128)` ⇒ en la práctica una contraseña corta/larga responde `errors[0].code = "INVALID_LENGTH"` (no `PASSWORD_TOO_SHORT`).

| # | Endpoint | Cuerpo (todos estrictos) | Éxito | Errores y reglas |
|---|---|---|---|---|
| 7 | POST `/auth/register` (rate `register`) | `email` req @Email ≤254; `password` req 12–128; `fullName` req 2–120; `companyName` ≤160; `ruc` ≤11 (SUNAT si viene); `phone` ≤24 (dominio); `privacyNoticeVersion` req ≤20; `acceptPrivacyNotice` true; `source` ≤12 ∈ `registro\|carrito\|cotizar\|login` (otro ⇒ `INVALID_SOURCE`); `newsletter` bool opcional. BFF manda email, password, fullName, companyName?, phone?, `privacyNoticeVersion:"2026-10"`, acceptPrivacyNotice, newsletter, source? | **202** `{"message":"Si los datos son válidos, recibirá un correo con las instrucciones."}` (siempre igual) | 400 de campos (`INVALID_EMAIL`, `INVALID_PHONE`, `INVALID_LENGTH`, `PASSWORD_TOO_COMMON`, `PASSWORD_CONTAINS_EMAIL`, `MUST_ACCEPT`, `INVALID_SOURCE`). Correo ya existente ⇒ mismo 202, hash igual (tiempo), correo `REGISTRATION_ATTEMPT`. Nueva cuenta: `kind=CUSTOMER`, `status=PENDING_VERIFICATION`, rol CUSTOMER, `signup_method=EMAIL`, `signup_source`, `newsletter_opt_in_at=now` si newsletter, token de verificación 24 h ⇒ correo `VERIFY_EMAIL` |
| 8 | POST `/auth/verify-email` (rate `token`) | `token` req ≤128 | **204** (BFF ⇒ `{ok:true}`) | Token inexistente/vencido/usado/otro propósito ⇒ 400 `VALIDATION_ERROR` errors `[{field:"token",code:"INVALID_TOKEN"}]`; cuenta no pendiente o sin contraseña ⇒ 409 `ALREADY_VERIFIED` (rollback, token no se consume). Efecto: `ACTIVE`, `email_verified_at=now`; auditoría `EMAIL_VERIFIED` |
| 9 | POST `/auth/verify-email/resend` (rate `password-reset`) | `email` req @Email ≤254 | **202** mismo mensaje | Solo si existe CUSTOMER `PENDING_VERIFICATION`: invalida tokens pendientes del propósito y emite otro (24 h) ⇒ `VERIFY_EMAIL` |
| 10 | POST `/auth/login` (rate `login`) | `email` req ≤254; `password` req ≤128 | **200** TokenResponse | **401 `INVALID_CREDENTIALS`** si: correo inválido/inexistente, bloqueada (`locked_until>now`), DISABLED, DELETED, contraseña errónea (con hash simulado para igualar tiempos). **403 `EMAIL_NOT_VERIFIED`** solo tras contraseña correcta y estado PENDING. Fallo con contraseña real suma `failed_login_attempts`; al 5.º: `locked_until=now+15 min`, contador a 0, correo `ACCOUNT_LOCKED`. Éxito: contador 0, `locked_until=null`, `last_login_at=now`, auditoría `SIGNED_IN {method:PASSWORD}`. BFF luego llama `/account/me` (un STAFF con contraseña obtendría 403 ahí) |
| 11 | POST `/auth/google` (rate `login`) | `idToken` req ≤4096; `privacyNoticeVersion` ≤20; `source` ≤12; `newsletter` bool. BFF: `{idToken, privacyNoticeVersion:"2026-10", source:"registro"\|"login"}` | **200** TokenResponse | Sin `GOOGLE_CLIENT_ID` ⇒ 422 `GOOGLE_SIGN_IN_DISABLED`. Token inválido (firma JWKS Google, iss `accounts.google.com`/`https://accounts.google.com`, aud = client id, exp ±60 s, `email_verified` true, `sub`) ⇒ 401 `INVALID_GOOGLE_TOKEN`. Busca por `google_subject`, si no por email. Existente: STAFF ⇒ 403 `STAFF_USE_PANEL`; DISABLED o subject distinto ya vinculado ⇒ 401 `INVALID_CREDENTIALS`; DELETED ⇒ 409 `ACCOUNT_DELETED` (inalcanzable en la práctica: la anonimización cambia el correo y borra el subject); vincula subject; PENDING ⇒ ACTIVE + verificado. Nuevo: exige `privacyNoticeVersion` (400 `REQUIRED`), crea CUSTOMER ACTIVE sin contraseña, `signup_method=GOOGLE`, nombre de Google ajustado a 2–120 (fallback parte local del correo / “Cliente FUNDIGSAC”). Auditoría `SIGNED_IN {method:GOOGLE}` (+`EMAIL_VERIFIED` si aplica). Sin correo. BFF: si falla, mantiene sesión solo-Google |
| 12 | POST `/auth/refresh` (rate `token`) | `refreshToken` req ≤128 | **200** TokenResponse (refresh nuevo) | 401 `INVALID_SESSION` (§7.6). BFF: error `http` ⇒ borra cookies (Admin responde `401 {error:"SESSION_EXPIRED"}`) |
| 13 | POST `/auth/logout` (sin rate) | `refreshToken` req ≤128 | **204** siempre | Revoca toda la familia si existe; los BFF ignoran el resultado |
| 14 | POST `/auth/password/forgot` (rate `password-reset`) | `email` req @Email ≤254 | **202** mismo mensaje | Solo si cuenta `ACTIVE` o (`PENDING_VERIFICATION` con contraseña): token 30 min ⇒ `PASSWORD_RESET` |
| 15 | POST `/auth/password/reset` (rate `token`) | `token` req ≤128; `password` req 12–128 | **204** (BFF ⇒ `{ok:true}`) | `INVALID_TOKEN` (400, field `token`); política de contraseña (field `password`); DISABLED ⇒ 422 `ACCOUNT_DISABLED`; DELETED ⇒ 409 `ACCOUNT_DELETED`. Efecto: nuevo hash Argon2, desbloquea, PENDING⇒ACTIVE+verificado, `security_stamp++`, revoca **todos** los refresh del usuario, correo `PASSWORD_CHANGED`, auditoría `PASSWORD_RESET` |
| 16 | GET `/account/me` (CUSTOMER) | — | **200** AccountView (§5.0) | 401/403; 404 `ACCOUNT_NOT_FOUND`. BFF usa `fullName`, `email` |

Códigos que el Frontend traduce (`modules/access/access-copy.ts`): `INVALID_CREDENTIALS`, `EMAIL_NOT_VERIFIED` (además muestra “reenviar enlace”), `PASSWORD_TOO_SHORT`, `PASSWORD_TOO_LONG`, `PASSWORD_TOO_COMMON`, `PASSWORD_CONTAINS_EMAIL`, `INVALID_TOKEN`, `INVALID_EMAIL`, `INVALID_PHONE`; 429 ⇒ “limited” (`Retry-After`, def. 900 s); 503 ⇒ “offline”. Toma `errors[0].code` antes que `error`.

---

## 4. Acceso del personal (Admin `/api/session/*`)

`identity/web/StaffAccessController.java`, `identity/application/StaffCodeLoginService.java`, `identity/domain/StaffLoginCode.java`, tabla `staff_login_codes`.

| # | Endpoint | Cuerpo | Éxito | Reglas / errores |
|---|---|---|---|---|
| 17 | POST `/auth/staff/code` (rate `login-code`) | `email` req ≤254 | **202** `{"message":"Si el correo pertenece al personal, recibirá un código de acceso.","expiresInSeconds":600,"resendAfterSeconds":60}` — **idéntico exista o no** | Elegible: `kind=STAFF` y status `ACTIVE` o `PENDING_VERIFICATION` (el bloqueo por contraseña **no** aplica). Si el último código sigue usable y se creó hace <60 s ⇒ no se emite otro (silencioso). Si no: marca usados (`used_at=now`) los pendientes, genera `%06d` aleatorio, guarda `code_hash = sha256(userId + ":" + code)` (hex), `expires_at=now+10 min`, `attempts_left=5` ⇒ correo `STAFF_LOGIN_CODE`. Admin: 429 ⇒ “limited”, otro error ⇒ “offline”; usa `expiresInSeconds` |
| 18 | POST `/auth/staff/code/verify` (rate `token`) | `email` req ≤254; `code` req ≤12 | **200** TokenResponse (`refreshExpiresIn=43200`) | Cualquier fallo ⇒ **401 `INVALID_CODE`** (cuenta no elegible, sin código usable = no usado, `attempts_left>0`, no vencido, código ≠ `^\d{6}$` o hash distinto). Un fallo con código vigente descuenta 1 intento y **se confirma** aunque la respuesta sea error. Éxito: `used_at=now`; PENDING⇒ACTIVE + `email_verified_at`; `last_login_at`; auditoría `SIGNED_IN {method:STAFF_CODE}` (+`EMAIL_VERIFIED`). Admin lleva su propio contador de 5 intentos y 10 min |
| 19 | GET `/staff/profile` (STAFF, sin permiso fino) | — | **200** AccountView | 404 `USER_NOT_FOUND` si no es STAFF o está DELETED. Admin exige `kind === "STAFF"` (si no, 403 `NOT_STAFF` del BFF) y guarda `id, fullName, email, roles (minúsculas), permissions` en cookie firmada |

---

## 5. Panel: cuentas y personal

### 5.0 Vistas
**AccountView** (`identity/application/AccountView.java`) — `/account/me`, `/staff/profile`, `/staff/users*`, PATCH/disable/enable de cuentas:
```json
{"id":"uuid","kind":"CUSTOMER|STAFF","email":"…","fullName":"…","companyName":null,"ruc":null,"phone":"+51987654321",
 "status":"ACTIVE|PENDING_VERIFICATION|DISABLED","roles":["SALES"],"permissions":["catalog:read","inquiry:manage",…],
 "emailVerified":true,"lastLoginAt":"…|null","createdAt":"…","version":3}
```
`roles` y `permissions` ordenados alfabéticamente (permisos = unión de los roles, §8).

**AccountRow** (`backoffice/application/AccountViews.java`, SQL en `backoffice/infrastructure/JdbcAccountReadModel.java`):
`{id, kind, fullName, email, companyName, ruc, phone, signupMethod: EMAIL|GOOGLE|FACEBOOK, status, roles: string[] (orden alfabético), emailVerified (email_verified_at≠null), newsletter (newsletter_opt_in_at≠null), privacyNoticeVersion, signupSource (registro|carrito|cotizar|login|null), createdAt, lastLoginAt, quotes (count quote_requests.customer_id), cartItems (count quote_cart_items.owner_id), activeSessions (refresh_tokens no revocados y no vencidos), signIns (count audit_events action=SIGNED_IN resource USER), notes (account_notes.notes), version}`. Nunca lista `DELETED`.

### 5.1 GET `/staff/accounts` (users:manage)
Query (todas opcionales; valor fuera de lista ⇒ 400 field `<param>` `INVALID_FILTER`; `all`/vacío = sin filtro):

| Param | Valores |
|---|---|
| `q` (≤100) | hasta 6 palabras; cada una debe aparecer (ILIKE, `unaccent`) en `concat_ws(' ', full_name, email, company_name, ruc, phone)` |
| `status` | `ACTIVE`, `PENDING_VERIFICATION`, `DISABLED` |
| `kind` | `CUSTOMER`, `STAFF` |
| `method` | `EMAIL`, `GOOGLE`, `FACEBOOK` |
| `role` | `CUSTOMER`, `ADMINISTRATOR`, `SALES`, `CATALOG_EDITOR`, `CATALOG_REVIEWER`, `LEGAL_SUPPORT`, `READ_ONLY` |
| `range` | `7d`, `30d`, `90d`, `all` ⇒ `created_at >= now − N días` (otro ⇒ `INVALID_FILTER` field `range`) |
| `sort` | `name` (lower(full_name)), `registeredAt` (def., created_at), `lastActiveAt` (last_login_at NULLS LAST), `quotes`, `status` (ACTIVE<PENDING<DISABLED); desempate `id` |
| `desc` | bool, def. `true` |
| `page`, `size` | §0.3 |

**200**: `{items: AccountRow[], page, size, totalItems, totalPages, statusCounts: {all, ACTIVE, PENDING_VERIFICATION, DISABLED}}` — `statusCounts` con los mismos filtros **excepto** `status`. Admin pagina de 100 en 100 hasta 100 páginas para CSV.

### 5.2 GET `/staff/accounts/{id}` → **200** AccountRow + `ETag`. 404 `USER_NOT_FOUND` (incluye DELETED); UUID inválido ⇒ 400 (Admin lo trata como null).

### 5.3 PUT `/staff/accounts/{id}/notes` — sin If-Match
Cuerpo `{notes: string}` (`@NotNull`, ≤2000 tras `strip`; U+0000 ⇒ `INVALID_CHARACTER`; >2000 ⇒ `TOO_LONG`). Vacía ⇒ borra la fila. Upsert en `account_notes(user_id, notes, updated_by, updated_at)`. **200** AccountRow + ETag (la versión de la cuenta no cambia). 404 `USER_NOT_FOUND`.

### 5.4 PATCH `/staff/accounts/{id}` — If-Match
Cuerpo `{fullName req 2–120, companyName ≤160, ruc ≤11 (SUNAT), phone ≤24 (dominio)}` (Admin manda null en vacíos). No cambia el correo. **200** AccountView + ETag. Errores 404 `USER_NOT_FOUND`, 412, 428, 409 `ACCOUNT_DELETED`. Auditoría `USER_UPDATED` (actor = personal).

### 5.5 POST `/staff/accounts/{id}/disable` | `/enable` — If-Match, sin cuerpo (Admin manda `{}`, se ignora)
- disable: 422 `CANNOT_DISABLE_SELF`; si es ADMINISTRATOR activo y es el último ⇒ 422 `LAST_ADMINISTRATOR`; ya DISABLED ⇒ 409 `ALREADY_DISABLED`. Efecto: `DISABLED`, `security_stamp++`, revoca todos sus refresh. Auditoría `USER_STATUS_CHANGED {status:"DISABLED"}`.
- enable: no DISABLED ⇒ 409 `NOT_DISABLED`. Nuevo estado `ACTIVE` si tiene contraseña o (STAFF con correo verificado); si no `PENDING_VERIFICATION`. Limpia intentos/bloqueo. Auditoría `USER_STATUS_CHANGED {status:<nuevo>}`.
- **200** AccountView + ETag.

### 5.6 DELETE `/staff/accounts/{id}` — If-Match → **204**
422 `CANNOT_DELETE_SELF`, `LAST_ADMINISTRATOR`. Anonimiza: email `eliminada-<uuid sin guiones>@cuentas-eliminadas.invalid`, fullName `Cuenta eliminada`, borra company/ruc/phone/password, newsletter y google subject; `status=DELETED`, `deleted_at`, `security_stamp++`; revoca refresh; borra `account_notes`. Auditoría `ACCOUNT_DELETED` (actor = personal). Cotizaciones/reclamos conservan su copia.

### 5.7 POST `/staff/accounts/{id}/verification-email` → **202** `{"message":"Enviamos el correo a la cuenta."}`
Solo CUSTOMER `PENDING_VERIFICATION`, si no 422 `NOT_PENDING`. Emite token 24 h ⇒ `VERIFY_EMAIL`. 404 `USER_NOT_FOUND`.

### 5.8 POST `/staff/accounts/{id}/password-reset` → **202** mismo cuerpo
STAFF ⇒ 422 `STAFF_PASSWORDLESS`; DISABLED ⇒ 422 `ACCOUNT_DISABLED`. Token 30 min ⇒ `PASSWORD_RESET`.

### 5.9 GET `/staff/accounts/activity` (users:manage)
Query: `q` (≤100; ILIKE sin unaccent sobre nombre/correo del usuario, nombre del actor y `detail`), `type` ∈ `SIGNUP, LOGIN, VERIFY, QUOTE, PASSWORD, DISABLE, ENABLE, ROLES, UPDATE, DELETE, INVITE` (otro ⇒ `INVALID_FILTER`), `userId` (uuid), `page`, `size`.
Fuente (UNION ALL), orden `at DESC, id`:
| Origen | `id` | `type` | `detail` |
|---|---|---|---|
| `audit_events` (resource_type `USER`): SIGNED_IN→LOGIN, EMAIL_VERIFIED→VERIFY, PASSWORD_RESET/PASSWORD_CHANGED→PASSWORD, USER_ROLES_CHANGED→ROLES, STAFF_INVITED→INVITE, ACCOUNT_DELETED→DELETE, USER_UPDATED→UPDATE, USER_STATUS_CHANGED→DISABLE si `details.status='DISABLED'` si no ENABLE | `aud_<uuid>` | … | `details.method` o `details.roles` |
| `user_accounts` CUSTOMER (created_at) | `usr_<uuid>` | SIGNUP | `signup_method` |
| `quote_requests` con customer_id (submitted_at) | `cot_<uuid>` | QUOTE | folio |
`actorId` solo si `actor_id ≠ resource_id`. **200** `PageResult<{id, at, type, userId, userName, actorName|null, detail|null}>`. Admin pasa `type` a minúsculas y `detail` a minúsculas.

### 5.10 GET `/staff/accounts/stats` → §9.

### 5.11 GET `/staff/users` (users:manage)
Query `q` (≤100; ILIKE en email o full_name), `page`, `size`. Solo `kind=STAFF` y no DELETED, orden `full_name, id`. **200** `PageResult<AccountView>`. Admin usa `id, fullName, email, roles` (caché 60 s) para mapear responsables. Si el usuario no tiene `users:manage`, el panel no puede resolver nombres ni asignar (`UNKNOWN_ASSIGNEE` local).

### 5.12 POST `/staff/users` — invitar (users:manage)
Cuerpo `{email req @Email ≤254, fullName req 2–120, roles req no vacío: Role[]}`; rol desconocido ⇒ 400 `INVALID_VALUE` (field `roles…`); incluye `CUSTOMER` ⇒ 400 field `roles` `INVALID_ROLE`. Correo existente (cualquier estado) ⇒ **409 `EMAIL_IN_USE`** (Admin ⇒ `email_taken`). Crea STAFF `PENDING_VERIFICATION` sin contraseña; token `STAFF_INVITATION` (3 d, no se envía). **201** + `Location: /api/v1/staff/users/{id}` + ETag, AccountView. Correo `STAFF_INVITATION`; auditoría `STAFF_INVITED` (actor = quien invita).

### 5.13 PUT `/staff/users/{id}/roles` — If-Match (Admin usa el ETag de `/staff/accounts/{id}`: misma columna `version`)
Cuerpo `{roles: Role[] no vacío}`. 404 `USER_NOT_FOUND` (no STAFF o DELETED). Quitar ADMINISTRATOR a sí mismo ⇒ 422 `CANNOT_DEMOTE_SELF`; dejar sin administradores activos ⇒ 422 `LAST_ADMINISTRATOR`; `CUSTOMER` ⇒ 400 `INVALID_ROLE`. Efecto: reemplaza `user_roles`, `security_stamp++` (sus JWT vigentes dejan de valer en ≤10 s). **200** AccountView + ETag. Auditoría `USER_ROLES_CHANGED {roles:"A,B"}`.

---

## 6. Panel: colas de atención

Admin lee **todas** las páginas (`?page=N&size=100`, máx. 10 páginas) y filtra, ordena y cuenta en el navegador; luego pide la ficha de cada fila visible (y de cada cotización `CLOSED` para distinguir ganada/perdida). Los filtros del Backend existen pero el panel no los usa.

Asignación (todas las colas): `{assigneeId: uuid}` (`@NotNull`); la persona debe ser STAFF `ACTIVE` con el permiso *manage* del módulo ⇒ si no 400 field `assigneeId` `INVALID_ASSIGNEE`. Cola cerrada/final ⇒ 409 `INVALID_TRANSITION` / `ALREADY_ANSWERED`.

### 6.1 Cotizaciones — `quotation/web/StaffQuoteController.java`, `quotation/application/{QuoteQueryService,StaffQuoteService}.java`, `quotation/domain/{QuoteRequest,QuoteStatus}.java`
- **GET `/staff/quotes`** (quote:read). Query: `status` ∈ `RECEIVED, ASSIGNED, IN_REVIEW, RESPONDED, CLOSED, CANCELLED` (otro ⇒ `INVALID_FILTER`), `assigneeId` uuid, `unassigned` bool (def. false), `q` ≤100 (ILIKE folio, company_name, contact_name, email), `page`, `size`. Orden `submitted_at DESC, id DESC`. Item `QuoteSummaryView`: `{id, folio, origin, status, companyName, contactName, email, lineCount, assigneeId|null, submittedAt, updatedAt}`.
- **GET `/staff/quotes/{id}`** → `QuoteDetailView` + ETag; 404 `QUOTE_NOT_FOUND`:
```json
{"id":"…","folio":"COT-2026-000042","origin":"GENERAL_FORM","status":"RECEIVED",
 "contact":{"companyName":"…","ruc":"20…","contactName":"…","position":null,"email":"…","phone":"+51…"},
 "project":{"projectType":null,"deliveryDepartment":"Lima","deliveryPlace":null,"requestedDeliveryDate":"2026-12-01","message":"…"},
 "items":[{"lineNo":1,"productSlug":null,"productName":"…","sku":null,"variantLabel":"DN 100","quantity":3,"unit":"und","unitLabel":"Unidades","addons":[],"notes":null}],
 "privacyNoticeVersion":"2026-10","customerId":null,"assigneeId":null,"statusReason":null,
 "history":[{"from":null,"to":"RECEIVED","note":null,"actorId":null,"occurredAt":"…"}],
 "submittedAt":"…","updatedAt":"…","version":0}
```
  (`quantity` sin ceros finales.)
- **POST `/staff/quotes/{id}/assign`** (quote:manage, If-Match): no permitido si RESPONDED, CLOSED o CANCELLED (409 `INVALID_TRANSITION`). Fija `assignee_id`; RECEIVED⇒ASSIGNED (otro estado se mantiene); siempre añade historial `{from, to, note:"Asignada", actorId}`. **200** QuoteDetailView + ETag.
- **POST `/staff/quotes/{id}/status`** (quote:manage, If-Match): `{status req ≤12, note ≤1000}`; estado desconocido ⇒ 400 field `status` `INVALID_STATUS`. Transiciones (si no 409 `INVALID_TRANSITION`):

| Desde | Hacia |
|---|---|
| RECEIVED | ASSIGNED, IN_REVIEW, CANCELLED |
| ASSIGNED | IN_REVIEW, CANCELLED |
| IN_REVIEW | RESPONDED, CANCELLED |
| RESPONDED | CLOSED, IN_REVIEW |
| CLOSED, CANCELLED | — (finales) |

  CANCELLED exige nota ≥5 caracteres ⇒ si no 422 `REASON_REQUIRED`; guarda `status_reason` (≤500). Nota multilínea ≤1000. Historial + auditoría `QUOTE_<TO>`. **Sin correo** por cambio de estado.
- Convenciones del panel (`http-adapter.ts`): “ganada” = cierre con nota `"Ganada"` (IN_REVIEW→RESPONDED→CLOSED); “perdida” = desde RESPONDED cierre con nota `"Perdida"`, en otro estado CANCELLED con nota `"Marcada como perdida desde el panel"`.

### 6.2 Consultas — `inquiry/web/InquiryController.java`, `inquiry/application/InquiryService.java`, `inquiry/domain/Inquiry.java`
- **GET `/staff/inquiries`** (inquiry:read): `status` ∈ `RECEIVED, IN_PROGRESS, ANSWERED, CLOSED` (otro ⇒ 400 `INVALID_VALUE`), `q` (ILIKE folio, full_name, company_name, email), `page`, `size`. Orden `received_at DESC, id DESC`. Item `{id, folio, reason, status, fullName, companyName, email, assigneeId, receivedAt}`.
- **GET `/staff/inquiries/{id}`** + ETag; 404 `INQUIRY_NOT_FOUND`: `{id, folio, reason, status, fullName, companyName, ruc, position, email, phone, message, requestedDocument, privacyNoticeVersion, assigneeId, history:[{from,to,note,actorId,occurredAt}], receivedAt, updatedAt, version}` (historial `ORDER BY occurred_at, id`).
- **POST `…/{id}/assign`** (inquiry:manage, If-Match): CLOSED ⇒ 409 `INVALID_TRANSITION`; RECEIVED⇒IN_PROGRESS; historial nota `"Asignada"`.
- **POST `…/{id}/status`** (inquiry:manage, If-Match): `{status ≤12, note ≤1000}`; inválido ⇒ 400 `INVALID_VALUE`. Transiciones: RECEIVED→{IN_PROGRESS, ANSWERED, CLOSED}; IN_PROGRESS→{ANSWERED, CLOSED}; ANSWERED→{CLOSED, IN_PROGRESS}; CLOSED→∅. Pasar a **ANSWERED con nota** ⇒ la nota es la respuesta ⇒ correo `INQUIRY_ANSWER` al remitente. Auditoría `INQUIRY_<TO>`. Admin usa la última nota de un evento `to=ANSWERED` como “respuesta”.

### 6.3 Reclamaciones — `complaint/web/ComplaintController.java`, `complaint/application/{ComplaintService,ComplaintViews}.java`
- **GET `/staff/complaints`** (complaint:read): `status` ∈ `FILED, IN_REVIEW, ANSWERED, CLOSED` (otro ⇒ `INVALID_VALUE`), `overdue` bool (⇒ `status IN (FILED,IN_REVIEW) AND response_due_on < hoy Lima`), `q` (ILIKE folio, consumer_name, email), `page`, `size`. Orden `response_due_on, filed_at, id`. Item `{id, folio, kind, status, consumerName, filedAt, responseDueOn, overdue, assigneeId}`.
- **GET `/staff/complaints/{id}`** + ETag + no-store; 404 `COMPLAINT_NOT_FOUND`. `ComplaintSheet` (vista personal, sin enmascarar):
```json
{"id","folio","kind","status","consumerName","document":"DNI 12345678","email","phone","address","minor",
 "guardianName","guardianDocument":"DNI 87654321","goodType":"PRODUCT|SERVICE|null","goodDescription",
 "claimedAmount":{"amount":120.50,"currency":"PEN"}|null,"serviceLocation","incidentDate":"YYYY-MM-DD","relatedReference",
 "facts","consumerRequest","responseChannel":"EMAIL|POSTAL_ADDRESS","filedAt","responseDueOn":"YYYY-MM-DD","overdue",
 "responseText","respondedAt","closedAt","assigneeId","history":[{"type":"FILED|ASSIGNED|IN_REVIEW|ANSWERED|CLOSED|NOTE","note","actorId","occurredAt"}],"version"}
```
  `overdue` = status FILED/IN_REVIEW y hoy (Lima) > `responseDueOn`.
- **POST `…/{id}/assign`** (complaint:manage, If-Match): ANSWERED/CLOSED ⇒ 409 `ALREADY_ANSWERED`; FILED⇒IN_REVIEW; evento `ASSIGNED` (sin nota).
- **POST `…/{id}/notes`** (complaint:manage, If-Match): `{note req 3–1000}`; evento `NOTE` (no cambia estado, permitido en cualquier estado).
- **POST `…/{id}/answer`** (complaint:manage, If-Match): `{response req 20–8000}`; ANSWERED/CLOSED ⇒ 409 `ALREADY_ANSWERED`. Guarda `response_text`, `responded_at`, `responded_by`; status ANSWERED; evento `ANSWERED`; `late` = hoy Lima > due. Correo: canal EMAIL ⇒ `COMPLAINT_ANSWER` al consumidor; POSTAL_ADDRESS ⇒ `COMPLAINT_ANSWER_POST` a Legal. Auditoría `COMPLAINT_ANSWERED {…}` + `COMPLAINT_<EVENT>` para el resto de eventos.
- Todas responden **200** ComplaintSheet + ETag.

### 6.4 Privacidad — `privacy/web/PrivacyController.java`, `privacy/application/PrivacyService.java`, `privacy/domain/DataSubjectRequest.java`
- **GET `/staff/privacy/requests`** (privacy:read): `status` ∈ `RECEIVED, IN_PROGRESS, RESOLVED, REJECTED`, `page`, `size` (sin `q`). Orden `received_at ASC, id`. Item = RequestView.
- **GET `…/{id}`** + ETag; 404 `REQUEST_NOT_FOUND`. `RequestView`: `{id, folio, type, status, fullName, email, document:"DNI 12345678"|null, details, resolutionNote, receivedAt, resolvedAt, resolvedBy, version}`.
- **POST `…/{id}/start`** (privacy:manage, If-Match, sin cuerpo): solo desde RECEIVED (si no 409 `INVALID_TRANSITION`) ⇒ IN_PROGRESS. Sin correo. Auditoría `DSR_IN_PROGRESS`.
- **POST `…/{id}/conclude`** (privacy:manage, If-Match): `{accepted: boolean, resolutionNote req 10–4000}`; desde RECEIVED o IN_PROGRESS (ya RESOLVED/REJECTED ⇒ 409 `INVALID_TRANSITION`) ⇒ RESOLVED si accepted, REJECTED si no; `resolved_at`, `resolved_by`. Correo `RIGHTS_RESOLUTION`. Auditoría `DSR_<STATUS>`. Admin siempre manda `accepted:true` con nota fija (Ley 29733).
- No hay plazo ni historial en la API: Admin calcula “vence” = recepción + 10 días hábiles en el cliente.

---

## 7. Reglas de negocio transversales

### 7.1 Folios — `shared/domain/Folio.java`, `shared/infrastructure/JdbcFolioGenerator.java`, tabla `folio_sequences(prefix char(3), year int, last_value int 1..999999, PK(prefix,year))`
- Formato `PPP-AAAA-NNNNNN` (`%s-%04d-%06d`). Año = año de la fecha **en Lima** del instante actual. Prefijos: `COT` (cotización GENERAL_FORM/PRODUCT_FORM/CART), `REQ` (PROCUREMENT), `CON` (consulta), `REC` (reclamación), `ARC` (derechos ARCO).
- Asignación atómica en la misma transacción del alta:
```sql
INSERT INTO folio_sequences (prefix, year, last_value) VALUES ($1, $2, 1)
ON CONFLICT (prefix, year) DO UPDATE SET last_value = folio_sequences.last_value + 1
RETURNING last_value;
```
  Rollback ⇒ sin huecos. Correlativo independiente por prefijo y año (reinicia en 1 cada año). Parseo estricto `^([A-Z]{3})-(\d{4})-(\d{6})$` (strip).

### 7.2 Idempotencia — `shared/application/Idempotency.java`, `shared/infrastructure/JdbcIdempotencyStore.java`, tabla `idempotency_records(scope, idem_key, fingerprint char(64), resource_ref, created_at, expires_at, PK(scope,idem_key))`
- Sin clave ⇒ se ejecuta normal. Clave `^[A-Za-z0-9_-]{8,128}$` (si no 400 field `Idempotency-Key` `INVALID_IDEMPOTENCY_KEY`). TTL 24 h. Scopes: `quote`, `inquiry`, `complaint`, `privacy-request`.
- `fingerprint = sha256(<clase del comando> + ":" + JSON del comando)` (comando de aplicación, **después** de mapear el DTO; incluye `customerId` en cotizaciones).
- Reserva: `INSERT … ON CONFLICT (scope, idem_key) DO UPDATE SET fingerprint=…, resource_ref=NULL, created_at=…, expires_at=… WHERE idempotency_records.expires_at < EXCLUDED.created_at` (reusa claves vencidas). Si no reservó: fingerprint distinto ⇒ 409 `IDEMPOTENCY_KEY_REUSED`; `resource_ref` null ⇒ 409 `REQUEST_IN_PROGRESS`; si no ⇒ responde la constancia del folio guardado (`resource_ref = folio`). Todo dentro de la transacción del alta.

### 7.3 Token de constancia
`receiptToken = base64url_sin_relleno(HMAC-SHA256(receipt_key, "<propósito>:<folio>"))`, propósito `quote` o `complaint`; `receipt_key` ≥32 bytes en Base64 (`RECEIPT_KEY`). Es determinista: un reintento idempotente devuelve el mismo token.

### 7.4 Plazo de respuesta de reclamaciones — `complaint/domain/ResponseDeadlinePolicy.java`
- `filedOn = fecha Lima de filedAt`; se avanza día a día desde `filedOn + 1`, contando solo días hábiles (lunes–viernes y no feriado) hasta sumar **15** (`fundigsac.complaints.response-business-days`, 1..60); `responseDueOn` = el día en que se completa el conteo. El día del registro nunca cuenta.
- Feriados: `fundigsac.complaints.holidays` (lista de fechas) — **vacía** en `application.yml` (Legal debe mantenerla; sin feriados el plazo calculado es más corto, nunca más largo).
- Se fija al registrar y no se recalcula. Vencida = estado FILED/IN_REVIEW y hoy Lima > due. Respuesta tardía se registra (`late` en el evento).

### 7.5 JWT de acceso — `identity/infrastructure/{JwtAccessTokenIssuer,JwtConfig,SecurityStampValidator}.java`
- RS256 (clave RSA ≥2048 bits, `JWT_PRIVATE_KEY`), header `{alg:RS256, kid, typ:"JWT"}`.
- Claims: `iss` (`JWT_ISSUER`, def. `https://api.fundigsac.com`), `aud: ["fundigsac-api"]`, `sub` = id de cuenta, `iat`, `nbf`, `exp = iat + 15 min`, `jti` uuid, `kind` (`CUSTOMER|STAFF`), `roles` (nombres ordenados), `sv` (security stamp entero). Sin correo ni datos personales.
- Validación: firma, iss, aud, exp/nbf con 60 s de tolerancia; `sv` debe igualar el `security_stamp` actual y la cuenta debe estar `ACTIVE` (caché 10 s; si el sello del token ≥ el cacheado se reconsulta). Autoridades derivadas en el servidor: `ROLE_<rol>` + permisos del rol + `ROLE_STAFF` si algún rol es interno.
- `security_stamp++` en: cambio/reset de contraseña, cambio de roles, desactivación, eliminación, aceptación de invitación.
- Para la reimplementación: los clientes tratan el token como opaco; basta mantener `expiresIn`=900 y la revocación por sello/estado.

### 7.6 Refresh con rotación — `identity/application/{AuthenticationService,SessionIssuer}.java`, tabla `refresh_tokens(id, user_id, family_id, token_hash char(64) unique, issued_at, expires_at, revoked_at, replaced_by)`
- Valor: 32 bytes aleatorios en base64url sin relleno (43 chars); se guarda `sha256` hex. TTL: CUSTOMER 14 d, STAFF 12 h. Cada login abre una familia nueva.
- `refresh`: entrada vacía o >128 ⇒ no encontrado. No existe ⇒ 401 `INVALID_SESSION`. **Ya revocado ⇒ reutilización: revoca toda la familia y 401**. Vencido ⇒ 401. Cuenta no ACTIVE ⇒ 401. Rotación `UPDATE refresh_tokens SET revoked_at=now, replaced_by=$new WHERE id=$id AND revoked_at IS NULL`; 0 filas (carrera) ⇒ revoca familia y 401. Emite nuevo refresh **en la misma familia** con TTL completo (sesión deslizante) + nuevo access.
- `logout`: revoca toda la familia (204 siempre). Reset/cambio de contraseña, desactivación y eliminación revocan **todos** los refresh del usuario.
- Los BFF comparten una renovación por refresh token durante 15 s y renuevan cuando faltan <30 s para `expiresIn`.

### 7.7 Tokens de un solo uso — `identity/application/OneTimeTokens.java`
Propósitos `EMAIL_VERIFICATION` (24 h), `PASSWORD_RESET` (30 min), `STAFF_INVITATION` (3 d). Emitir invalida los pendientes del mismo propósito y usuario. Canje: sha256 del valor, propósito y vigencia correctos, `markUsed` atómico; cualquier fallo ⇒ 400 field `token` `INVALID_TOKEN`. Enlaces: `{SITE_URL}/verificar-correo#token=…`, `{SITE_URL}/restablecer#token=…` (el FE lee `#token=[A-Za-z0-9_-]{20,128}`).

### 7.8 Código de acceso del personal — ver §4 (6 dígitos, 10 min, 5 intentos, reenvío ≥60 s, respuesta uniforme, `INVALID_CODE` genérico, hash con id de cuenta).

### 7.9 Reglas de administración
Nadie se desactiva, elimina ni quita su rol ADMINISTRATOR a sí mismo; siempre debe quedar ≥1 ADMINISTRATOR `ACTIVE` (`count` de `user_roles.role='ADMINISTRATOR'` con status ACTIVE >1 antes de quitarlo, desactivarlo o eliminarlo).

---

## 8. Roles → permisos (`identity/domain/Role.java`, `shared/security/Permission.java`)

| Rol | Interno | Permisos |
|---|---|---|
| CUSTOMER | no | — |
| ADMINISTRATOR | sí | **todos**: `catalog:read`, `catalog:write`, `catalog:publish`, `quote:read`, `quote:manage`, `inquiry:read`, `inquiry:manage`, `complaint:read`, `complaint:manage`, `privacy:read`, `privacy:manage`, `legal:publish`, `users:manage`, `audit:read`, `notifications:manage` |
| SALES | sí | `quote:read`, `quote:manage`, `inquiry:read`, `inquiry:manage`, `catalog:read` |
| CATALOG_EDITOR | sí | `catalog:read`, `catalog:write` |
| CATALOG_REVIEWER | sí | `catalog:read`, `catalog:publish` |
| LEGAL_SUPPORT | sí | `complaint:read`, `complaint:manage`, `privacy:read`, `privacy:manage`, `legal:publish`, `inquiry:read` |
| READ_ONLY | sí | `catalog:read`, `quote:read`, `inquiry:read`, `complaint:read` |

Permisos efectivos = unión de los roles. Admin muestra roles en minúsculas y guarda `permissions` en su cookie.

---

## 9. Indicadores del panel

### 9.1 GET `/staff/accounts/stats?range=7d|30d|90d|all` (users:manage) — `backoffice/application/AccountDirectoryService.java#stats`, `JdbcAccountReadModel#stats`
Universo: `user_accounts` con `kind='CUSTOMER' AND status<>'DELETED'`. `N` = 7/30/90; `all`/vacío ⇒ `from = prev = epoch`, serie de 120 días.
- `from` = medianoche Lima de (hoy Lima − (N−1)); `prev` = `from − N días`; `now` = instante actual.

| Campo | Cálculo |
|---|---|
| `total` | count(*) |
| `newInRange` | `created_at >= from` |
| `newPrevRange` | `prev <= created_at < from` (0 con `all`) |
| `pending` | status `PENDING_VERIFICATION` |
| `activeWeek` | `last_login_at >= now − 7 d` |
| `disabled` | status `DISABLED` |
| `verifiedRate` | (count `email_verified_at` no nulo) / total, fracción 0..1 (0 si total=0) |
| `newsletterRate` | (count `newsletter_opt_in_at` no nulo) / total |
| `series` | `[{day:"YYYY-MM-DD", count}]` un elemento por día Lima de los últimos N (o 120) días, con ceros (`generate_series` + agrupación por `(created_at AT TIME ZONE 'America/Lima')::date`) |
| `byMethod` | `{EMAIL, GOOGLE, FACEBOOK}` con `created_at >= from` (ceros incluidos) |
| `byStatus` | `{ACTIVE, PENDING_VERIFICATION, DISABLED}` sin filtro de fecha |
| `bySource` | `[{source, count}]`, `COALESCE(signup_source,'registro')`, `created_at >= from`, orden count desc, source |
| `latest` | 6 AccountRow más recientes (created_at desc, id) |
| `funnel` | `{registered, verified, quoted}` entre `created_at >= from`: total, con correo verificado, con ≥1 `quote_requests.customer_id` |
| `pendingOldest` | 4 AccountRow PENDING más antiguas |
| `pendingOver48h` | PENDING con `created_at < now − 48 h` |
| `generatedAt` | `now` |

Rango inválido ⇒ 400 field `range` `INVALID_FILTER`. Admin rellena `byCity: []`.

### 9.2 Lo que **no** calcula la API
Contadores de colas (`queueCounts`: cotizaciones “nuevas” = RECEIVED; consultas RECEIVED/IN_PROGRESS; reclamos FILED/IN_REVIEW; privacidad RECEIVED/IN_PROGRESS), lista de vencimientos (reclamos con `responseDueOn` y privacidad con recepción + 10 días hábiles, ≤5 días hábiles restantes), conteos por estado y búsqueda en colas: todo lo hace Admin en el navegador sobre las listas completas (`Admin/src/lib/api/http-adapter.ts`, `lib/business-days.ts`). Mapeos del panel: cotización RECEIVED→new, ASSIGNED/IN_REVIEW→reviewing, RESPONDED→sent, CLOSED→won/lost (por nota), CANCELLED→lost; consulta RECEIVED/IN_PROGRESS→new, ANSWERED→answered, CLOSED→closed; reclamo FILED→received, IN_REVIEW→in_progress, ANSWERED/CLOSED→answered; privacidad RECEIVED→received, IN_PROGRESS→processing, RESOLVED/REJECTED→done.

---

## 10. Correos encolados en `email_outbox` (`notification/application/{NotificationListeners,EmailTemplates,NotificationProperties}.java`)

Fila: `{id uuid, dedupe_key ≤200 UNIQUE (ON CONFLICT DO NOTHING), template ≤40, recipient ≤254 (Email normalizado), subject ≤200, body text (texto plano, limpiado multilínea, 1–20 000), status 'PENDING', attempts 0, next_attempt_at = now, reference ≤40 (folio o userId), created_at}`. `dedupe_key = "<TEMPLATE>:<reference>:<occurredAt epoch ms>:<recipient>"` (truncado a 200). Destinatario vacío o inválido ⇒ se omite. En Java se encola tras el commit (evento asíncrono con reintento); despacho: hasta 8 intentos, backoff 30 s×2ⁿ, lotes de 20; al enviar se borra `body`. Remitente `MAIL_FROM` (def. `FUNDIGSAC <no-responder@fundigsac.local>`). Fechas en `d 'de' MMMM 'de' yyyy, HH:mm 'h'` es-PE hora Lima; firma común “Atentamente, FUNDIGSAC - Fundición y Desarrollo de Ingeniería y Gestión S.A.C. Este es un mensaje automático; no responda a este correo.” (solo correos al público). Cuerpos exactos en `EmailTemplates.java`.

| Acción (endpoint) | Template | Destinatario | Asunto |
|---|---|---|---|
| POST quotes | `QUOTE_RECEIPT` | `contact.email` | `FUNDIGSAC: recibimos su solicitud de cotización {folio}` (nombre, folio, fecha, nº de productos) |
| POST quotes | `QUOTE_SALES` | `SALES_INBOX` (def. `ventas@fundigsac.local`) | `Nueva solicitud de cotización {folio} - {empresa}` (empresa, contacto, origen, productos) |
| POST inquiries | `INQUIRY_RECEIPT` | `email` | `FUNDIGSAC: recibimos su consulta {folio}` |
| POST inquiries | `INQUIRY_SALES` | `SALES_INBOX` | `Nueva consulta {folio} - {empresa}` (empresa, contacto, motivo) |
| staff inquiries status→ANSWERED con nota | `INQUIRY_ANSWER` | email del remitente | `FUNDIGSAC: respuesta a su consulta {folio}` (incluye la nota) |
| POST complaints | `COMPLAINT_RECEIPT` | `email` | `FUNDIGSAC: constancia de su {reclamo\|queja} {folio}` (hoja N.°, fecha, “a más tardar el {responseDueOn}”) |
| POST complaints | `COMPLAINT_LEGAL` | `LEGAL_INBOX` (def. `legal@fundigsac.local`) | `Libro de Reclamaciones: nueva hoja {folio}` (kind, fecha límite) |
| staff complaints answer, canal EMAIL | `COMPLAINT_ANSWER` | email del consumidor | `FUNDIGSAC: respuesta a su hoja de reclamación {folio}` (texto de la respuesta) |
| staff complaints answer, canal POSTAL_ADDRESS | `COMPLAINT_ANSWER_POST` | `LEGAL_INBOX` | `Libro de Reclamaciones: enviar respuesta por correo postal {folio}` |
| POST privacy/requests | `RIGHTS_RECEIPT` | `email` | `FUNDIGSAC: recibimos su solicitud de datos personales {folio}` (tipo) |
| POST privacy/requests | `RIGHTS_PRIVACY` | `PRIVACY_INBOX` (def. `privacidad@fundigsac.local`) | `Nueva solicitud de derechos del titular {folio}` |
| staff privacy conclude | `RIGHTS_RESOLUTION` | email del titular | `FUNDIGSAC: resultado de su solicitud {folio}` (“fue atendida” si RESOLVED / “no pudo ser atendida”, + nota) |
| register (nuevo), resend, staff verification-email | `VERIFY_EMAIL` | cuenta | `FUNDIGSAC: confirme su correo` (enlace `/verificar-correo#token=`, vence) — reference = userId |
| register con correo existente | `REGISTRATION_ATTEMPT` | dueño | `FUNDIGSAC: intento de registro con su correo` |
| forgot, staff password-reset | `PASSWORD_RESET` | cuenta | `FUNDIGSAC: restablezca su contraseña` (enlace `/restablecer#token=`, vence) |
| password/reset (y cambio de contraseña) | `PASSWORD_CHANGED` | cuenta | `FUNDIGSAC: su contraseña cambió` |
| 5.º login fallido | `ACCOUNT_LOCKED` | cuenta | `FUNDIGSAC: bloqueamos temporalmente su cuenta` (hasta {lockedUntil}) |
| POST staff/users | `STAFF_INVITATION` | invitado | `FUNDIGSAC: invitación al panel interno` (enlace `{ADMIN_URL}/login`, sin token) |
| POST auth/staff/code (si emite) | `STAFF_LOGIN_CODE` | personal | `FUNDIGSAC: su código de acceso al panel interno` (código en claro, vence) |

Sin correo: consentimientos, login correcto, Google, verify-email, refresh/logout, asignaciones, notas, cambios de estado de cotización, inicio de trámite de privacidad, cambios de rol, desactivar/activar/eliminar/editar cuenta, notas de cuenta.

---

## 11. Auditoría necesaria (`audit_events`) — `audit/application/AuditTrail.java`
Tabla `audit_events(id, occurred_at, recorded_at, actor_id, action ≤60, resource_type ≤40, resource_id ≤80, details jsonb objeto, UNIQUE(action, resource_type, resource_id, occurred_at))`. La usan `/staff/accounts/activity` y `signIns`. Acciones (resource_type `USER`, resource_id = userId):
`SIGNED_IN {method: PASSWORD|GOOGLE|STAFF_CODE}` (actor = usuario), `EMAIL_VERIFIED` (actor = usuario), `PASSWORD_RESET` / `PASSWORD_CHANGED` (actor = usuario), `ACCOUNT_LOCKED {lockedUntil}`, `USER_UPDATED` (actor = personal), `USER_ROLES_CHANGED {roles:"A,B"}`, `USER_STATUS_CHANGED {status}`, `STAFF_INVITED` (actor = quien invita), `ACCOUNT_DELETED` (actor = personal o el propio usuario).
Otros módulos (no leídos por los clientes, pero escritos): `QUOTE_SUBMITTED`, `QUOTE_<estado>` (QUOTE), `INQUIRY_RECEIVED`, `INQUIRY_<estado>` (INQUIRY), `COMPLAINT_FILED`, `COMPLAINT_ANSWERED`, `COMPLAINT_<ASSIGNED|NOTE|CLOSED>` (COMPLAINT), `DSR_RECEIVED`, `DSR_<estado>` (DATA_SUBJECT_REQUEST).

---

## 12. Endpoints opcionales / con respaldo (`not_configured`)

Sin `BACKEND_URL` los BFF devuelven `503 {error:"NOT_CONFIGURED"}` y:
1. **Frontend `/api/forms/*` → POST quotes, inquiries, complaints, privacy/requests**: el formulario pasa a “offline” y prepara el envío por correo/WhatsApp (sin folio real). Opcional.
2. **POST privacy/consents**: fire-and-forget; la cookie `fundigsac-consent` sigue siendo la constancia. Opcional.
3. **GET quotes/{folio}/receipt**: sin Backend la confirmación solo reconoce el marcador “pendiente de conexión”; con Backend caído muestra “no disponible”. Opcional.
4. **POST auth/google**: si falla o no hay Backend, se abre sesión solo con Google (cookie firmada del sitio). Opcional.
5. **POST auth/refresh / auth/logout**: solo cuando hay sesión API; logout ignora el resultado. Opcional en modo sin cuentas.
6. **Cuentas con correo (register, login, verify-email, resend, forgot, reset, account/me)**: `/api/auth/session` publica `accounts:false` y la UI muestra “La zona de clientes llega muy pronto”; con 503 el formulario muestra “offline”. Requeridos solo para la función de cuentas.
7. **Admin**: todo `/staff/**` y `/auth/staff/*` solo se usa con `NEXT_PUBLIC_DATA_SOURCE=backend`; sin esa variable el panel usa el adaptador simulado. En modo backend son obligatorios; `GET /staff/users` puede fallar sin romper la lectura (nombres de responsables en blanco) pero bloquea asignar.

No usados por ningún cliente (no reimplementar): `PATCH /account/me`, `DELETE /account`, `POST /account/password`, `/cart/**`, `/catalog/**`, `/resources/**`, `/legal/**`, `/staff/catalog/**`, `/staff/legal/**`, `GET /staff/users/{id}`, `/staff/users/{id}/disable|enable`, `/staff/complaints/{id}/close`, `GET /complaints/{folio}/receipt`, `/auth/invitation/accept` (obsoleto), `/staff/audit`, `/staff/notifications`, `/account/quotes`.
