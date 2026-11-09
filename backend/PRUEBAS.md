# Pruebas del backend de FUNDIGSAC

Fecha de ejecución: 9 de noviembre de 2026. Todo se ejecutó en local, con Docker Desktop y Java 21. No se hizo commit, push ni
despliegue, y no se usó ningún sistema de producción.

## Resultado final

Medición sobre el código definitivo, después de la segunda auditoría. Esa auditoría reprodujo en verde los indicadores de la
primera tanda, pero refutó la afirmación "backend completamente probado": 10 de 13 mutantes nuevos sobrevivían a la suite Maven
y una prueba dependía de la zona horaria de la JVM.

| Indicador | Antes de la segunda tanda | Resultado | Meta |
|---|---|---|---|
| `./mvnw verify` (Surefire) | 167 | 185 ejecutadas, 0 fallos, 0 errores, 0 omitidas | Verde |
| `./mvnw verify` (Failsafe, PostgreSQL real) | 362 | 432 ejecutadas, 0 fallos, 0 errores, 0 omitidas | Verde |
| `./mvnw verify -Duser.timezone=Pacific/Kiritimati` (JVM a UTC+14) | 1 fallo (`ComplaintIT:150`) | 185 + 432, 0 fallos | Verde |
| Medición completa después de cada corrección | No aplicaba | 14 mediciones (pasos 1 a 12). Las 11 de los pasos 2b, 3 a 8, 9b y 10 a 12 quedaron en verde; las 3 en rojo están explicadas en la tabla de la segunda tanda | Verde al cerrar cada paso |
| Cobertura de líneas (JaCoCo) | 97,0 % (5070 de 5228) | 97,6 % (5192 de 5317) | 95 % o más |
| Cobertura de métodos (JaCoCo) | 96,9 % (1492 de 1540) | 97,4 % (1519 de 1559) | 95 % o más |
| Cobertura de ramas (JaCoCo) | 84,4 % (1333 de 1580) | 85,5 % (1397 de 1634) | 80 % o más |
| Mutantes de la segunda auditoría detectados | 3 de 13 | 13 de 13 | Todos |
| Mutantes nuevos sobre las correcciones detectados | No aplicaba | 17 de 17 (uno sobrevivió en la primera ronda; se corrigió la prueba y ahora muere) | Todos |
| Respuestas de la suite comparadas con el contrato OpenAPI | 0 | Todas las de MockMvc en las pruebas de integración: código, tipo de contenido y esquema | Todas |
| Operaciones del contrato que documentan errores 4xx | 0 de 97 | 97 de 97, con esquema `Problem` (RFC 9457) | Todas |
| Operaciones cuyo código de éxito documentado es el real | 80 de 97 | 97 de 97 (10 con 201, 6 con 202 y 1 con 302) | Todas |
| Permisos de los 7 roles comprobados contra una tabla independiente | 0 (se derivaban de `Role`) | 7 de 7 roles, 67 de 67 operaciones | Todos |
| Casos de validación de JWT con token fabricado | 0 | 16 (firma, emisor, audiencia, vencimiento, tolerancia, `nbf`, `alg`, sello, sujeto y rol) | Todos |
| Prueba de humo (`sh scripts/smoke-test.sh`), dos corridas seguidas | 32 de 32 y luego 29 de 32 (429) | 34 de 34 en las dos corridas seguidas | Verde |
| Colección de Postman | 256 peticiones y 430 aserciones, 0 fallos | 257 peticiones y 431 aserciones, 0 fallos | Verde |
| Entorno Docker reconstruido con este código | Saludable | `backend`, `postgres` y `mailpit` saludables | Saludable |

Los totales de Postman cambian entre corridas, entre 254 y 259 peticiones y entre 428 y 433 aserciones, porque las esperas de
correo y de revocación de tokens repiten la misma petición hasta cumplirse. La colección define 235 peticiones. Lo estable es que
ninguna corrida tuvo fallos. El contrato en vivo tiene 87 rutas y 97 operaciones.

De las 97 operaciones, 96 responden 2xx en el tráfico de las pruebas. `GET /resources/{slug}/download` responde 302 (redirección al
archivo) o 409 (documento bajo solicitud): no tiene un éxito 2xx. La primera tanda decía "97 de 97 con respuesta 2xx", y era
inexacto.

El ingreso con correo inexistente, con personal sin contraseña y con cliente con contraseña tiene medianas de 28, 30 y 31 ms
(12 muestras cada uno, perfil de pruebas, medido en la primera tanda).

## Comandos

Desde `Backend/`, con Git Bash:

```bash
./mvnw verify          # incluye JaCoCo; informe en target/site/jacoco/index.html
./mvnw verify -Duser.timezone=Pacific/Kiritimati   # la suite no depende de la zona de la JVM
sh scripts/generate-secrets.sh
docker compose up -d --build
sh scripts/smoke-test.sh
sh postman/run.sh
```

## Medición después de cada corrección

| Momento | `mvnw verify` | Humo | Postman | Operaciones con prueba |
|---|---|---|---|---|
| Línea base, sin cambios | 37 + 55, correcto | 32/32 | No existía | 65 de 97 |
| Con las pruebas nuevas, antes de corregir | 37 + 117, 3 fallos | Sin repetir | No existía | 97 de 97 |
| Tras corregir el reintento del carrito | 37 + 118, correcto | 32/32 | 247 peticiones, 433 aserciones, 6 fallos | 97 de 97 |
| Tras corregir el sello de seguridad | 44 + 118, correcto | 32/32 | 258 peticiones, 432 aserciones, 0 fallos, dos corridas | 97 de 97 |

Entre las dos últimas filas también cambió la espera de revocación de la colección, por lo que sus totales de Postman no son
directamente comparables.

### Tanda de correcciones de la auditoría

| Paso | `mvnw verify` | Ramas | Resultado del paso |
|---|---|---|---|
| Correcciones de código y primeras pruebas de regresión | 95 + 335, 1 error | 72,7 % | Error propio de la prueba (texto SQL mal escapado) |
| Pruebas de reglas de dominio y de filtros | 164 + 358, 1 error | 83,9 % | El ensayo del plazo vencido violaba un `CHECK`: ahora mueve también la fecha de registro |
| Documentación, CI y orden aleatorio | 164 + 358, 1 fallo | 83,9 % | Código de error esperado incorrecto en la prueba |
| Siguiente corrida | 164 + 358, 1 fallo | 83,9 % | El orden aleatorio destapó una dependencia entre dos pruebas de catálogo; corregida |
| Dos corridas siguientes | 164 + 358, verde | 84,3 % | Verde |
| Código definitivo, cuatro corridas | 167 + 362, verde | 84,4 % | Verde |

`verify` y JaCoCo se midieron en cada paso. Mutación, tráfico por operación, humo y Postman se midieron una vez, sobre el código
definitivo de `src/main`: las correcciones posteriores solo agregaron pruebas. En la segunda tanda se midieron todos los
indicadores después de cada corrección.

### Tanda de la segunda auditoría

Después de cada corrección se midieron todos los indicadores con el mismo guion, en este orden: `./mvnw clean verify` con la JVM
en `Pacific/Kiritimati` (UTC+14), `./mvnw clean verify` en la zona del equipo (America/Lima) con JaCoCo, `docker compose up -d
--build --force-recreate --wait`, dos corridas seguidas de la prueba de humo y la colección de Postman. `clean` evita que JaCoCo
sume la cobertura de corridas anteriores.

| Paso | Corrección | `verify` UTC+14 | `verify` Lima | Líneas / métodos / ramas | Humo, dos corridas | Postman |
|---|---|---|---|---|---|---|
| 1 | Matriz de permisos con oráculo propio | 167 + 363, 1 fallo (`ComplaintIT:150`, hallazgo de zona horaria) | 167 + 363, verde | 97,0 / 96,9 / 84,4 % | 32/32 y 29/32 (429) | 258 y 432, 0 fallos |
| 2a | Fechas de prueba en hora de Lima | 167 + 363, 1 error propio | 167 + 363, 1 error propio | Sin informe | No se midió en verde | 254 y 428, 0 fallos |
| 2b | La misma, corregida | 167 + 363, verde | 167 + 363, verde | 97,0 / 96,9 / 84,4 % | 32/32 y 29/32 (429) | 0 fallos (resumen no capturado) |
| 3 | Humo repetible y comprobación de actuator | 167 + 363, verde | 167 + 363, verde | 97,0 / 96,9 / 84,4 % | 34/34 y 34/34 | 259 y 433, 0 fallos |
| 4 | Validación de JWT con tokens fabricados | 167 + 379, verde | 167 + 379, verde | 97,0 / 96,9 / 84,4 % | 34/34 y 34/34 | 257 y 431, 0 fallos |
| 5 | Contrato OpenAPI y comprobación de cada respuesta | 175 + 384, verde | 175 + 384, verde | 97,1 / 96,9 / 84,7 % | 34/34 y 34/34 | 257 y 431, 0 fallos |
| 6 | Valores de configuración del README | 175 + 391, verde | 175 + 391, verde | 97,1 / 96,9 / 84,7 % | 34/34 y 34/34 | 258 y 432, 0 fallos |
| 7 | Enmascarado completo de la constancia | 175 + 392, verde | 175 + 392, verde | 97,1 / 96,9 / 84,7 % | 34/34 y 34/34 | 257 y 431, 0 fallos |
| 8 | U+0000 responde 400 | 175 + 403, verde | 175 + 403, verde | 97,0 / 96,9 / 84,2 % | 34/34 y 34/34 | 258 y 432, 0 fallos |
| 9a | Cuerpos inválidos del personal | 175 + 413, 1 fallo | 175 + 413, 1 fallo | Sin informe | 34/34 y 34/34 | 258 y 432, 0 fallos |
| 9b | La misma, con el defecto de `errors[].field` corregido | 175 + 413, verde | 175 + 413, verde | 97,0 / 96,9 / 84,2 % | 34/34 y 34/34 | 259 y 433, 0 fallos |
| 10 | Código que no se ejecutaba | 183 + 417, verde | 183 + 417, verde | 97,6 / 97,4 / 85,4 % | 34/34 y 34/34 | 258 y 432, 0 fallos |
| 11 | Garantías del README sin prueba | 185 + 432, verde | 185 + 432, verde | 97,6 / 97,4 / 85,5 % | 34/34 y 34/34 | 258 y 432, 0 fallos |
| 12 | Espera de 3 s en el caso negativo del reintento de eventos (un mutante sobrevivía) | 185 + 432, verde | 185 + 432, verde | 97,6 / 97,4 / 85,5 % | 34/34 y 34/34 | 257 y 431, 0 fallos |

Los rojos de la tabla:

- Paso 1: es el hallazgo de zona horaria, todavía sin corregir. El segundo humo falla por el límite de 5 formularios cada 10
  minutos, también sin corregir en ese paso.
- Paso 2a: error propio al editar la prueba. El bloque `DO $$` quedó como `DO $` y PostgreSQL lo rechazó. Se corrigió y se
  repitió la medición completa (2b).
- Paso 5, antes de la medición: la comprobación del contrato hizo fallar 16 pruebas por dos esquemas fundidos (ver defecto 9) y
  luego 1 prueba por un error propio del cambio de nombre (la cabecera `X-Receipt-Token` se renombró por error). Ambos se
  corrigieron antes de la medición del paso 5.
- Paso 9a: la prueba nueva destapó el defecto 10 (`errors[].field` con el nombre del parámetro Java).
- Paso 11, antes de la medición: la prueba de logs encontró el nombre de la empresa en el log (defecto 11).

## Defectos encontrados y corregidos

### 1. El reintento de `POST /api/v1/cart/submit` devolvía 422

El contrato indica que la operación acepta `Idempotency-Key`. Al reintentar con la misma clave, el carrito ya estaba vacío, de modo
que la API respondía `CART_EMPTY` en vez de devolver el mismo folio. Un cliente que perdiera la respuesta por un corte de red no podía
recuperar su folio.

Causa: la clave solo protegía la cotización generada, cuyo contenido depende de las líneas del carrito, y la comprobación de carrito
vacío ocurría antes. Corrección: `CartService` aplica la idempotencia al envío del carrito, con un ámbito de claves por cliente. Se
agregó `QuoteSubmission.receipt(folio)` para responder al reintento con la constancia existente. Lo cubre `CartManagementIT`: reintento
con el mismo folio, clave reutilizada con otro contenido, aislamiento entre clientes y clave no consumida cuando el envío falla.

### 2. Un JWT recién emitido se rechazaba hasta 10 segundos después de cambiar la contraseña

La colección de Postman lo detectó en el entorno real. Tras restablecer la contraseña e ingresar de nuevo, la primera llamada con el
token nuevo respondía 401. Las pruebas de integración no lo detectaban porque usan una caché de revocación de 0 segundos, mientras
que el entorno real usa 10 segundos.

Causa: `SecurityStampValidator` comparaba el sello del token con el valor en caché, anterior al cambio. Corrección: cuando la caché
rechaza un token cuyo sello es igual o mayor que el recordado, vuelve a consultar la base de datos. Un token con sello menor sigue siendo
una revocación real y no genera consultas adicionales. Lo cubre `SecurityStampValidatorTests`, con la caché real de 10 segundos.

### 3. El inicio de sesión revelaba por tiempo que un correo existía

Una cuenta sin contraseña (todo el personal y las cuentas creadas con Google) respondía en 5 ms, porque `Argon2PasswordHasher.matches`
terminaba antes de calcular el hash. Corrección: sin hash se ejecuta el mismo cálculo contra un hash de referencia. Lo cubren
`Argon2PasswordHasherTests` y `AuthenticationServiceTests`.

### 4. Un anónimo podía bloquear el acceso del personal durante 15 minutos

Cinco contraseñas erróneas contra un correo del personal fijaban `locked_until`, y `canRequestLoginCode` negaba después el código.
Corrección: una cuenta sin contraseña ya no acumula fallos, y el bloqueo solo afecta al ingreso con contraseña. El código conserva sus
propios límites. Lo cubren `LoginProtectionIT` y `UserAccountRulesTests`.

### 5. Una cuenta creada con Google no podía eliminarse ni definir contraseña

`DELETE /account` y `POST /account/password` exigían una contraseña que esa cuenta no tiene, y respondían `WRONG_PASSWORD`. Corrección: se
aceptan con `googleIdToken`, un ID token vigente del mismo sujeto vinculado a la cuenta. Una cuenta con contraseña sigue obligada a
enviarla: el token de Google no la sustituye. Lo cubre `LoginProtectionIT`.

### 6. Contratos que no coincidían con la conducta

| Tema | Corrección | Prueba |
|---|---|---|
| `If-Match` | El README lista las 8 modificaciones del personal que no lo usan y el motivo. No se exigió en las notas ni en los reenvíos porque el panel `Admin` los llama sin versión. | `OptimisticLockingContractIT` |
| Invitación del personal | La descripción OpenAPI ya no promete un enlace de 72 horas. `POST /auth/invitation/accept` queda marcado como obsoleto. | `AccessDocumentationTests`, `StaffUserManagementIT`, `LoginProtectionIT` |
| `GET /staff/users` | `page` y `size` se validan igual que en las demás bandejas: 400 fuera de rango. | `StaffUserManagementIT` |
| `GET /staff/quotes?status=` | Un estado desconocido responde 400. | `QuotationIT` |
| `family` y `sector` desconocidos | Se mantiene 200 con lista vacía y queda documentado: son datos del catálogo, no una lista cerrada. | `CatalogIT` |
| `scripts/generate-secrets.sh` | Ya no imprime la contraseña del administrador. | Revisión del script |
| README | Rutas omitidas y carpeta `../Admin` corregidas. | Revisión |

### 7. La matriz de permisos no podía detectar una escalada de privilegios

`AuthorizationMatrixIT` calculaba lo esperado con `Role.permissions()`, el mismo enum que usa la aplicación. Si `READ_ONLY` recibía
`USERS_MANAGE` y `AUDIT_READ`, la prueba esperaba también que lo tuviera, y pasaba. Corrección: la prueba tiene su propia tabla de
permisos por rol, escrita a mano según la arquitectura §12.2, y una prueba nueva compara esa tabla con `Role` rol por rol. Además,
una operación permitida ya no acepta un 500 como éxito: antes solo se exigía que no fuera 401 ni 403.

### 8. Una prueba dependía de la zona horaria de la JVM

`ComplaintIT.staffInboxHighlightsOverdueSheets` fijaba el plazo con `CURRENT_DATE - 1`, que usa la zona de la sesión de
PostgreSQL, heredada de la JVM. La aplicación calcula los vencimientos con la fecha de Lima. Con la JVM en UTC+14 la prueba
fallaba, y en un runner de CI en UTC habría fallado de 19:00 a 24:00 hora de Lima. Corrección: la prueba usa
`LocalDate.now(PeruTime.ZONE)`, y también lo hacen las fechas de incidente de las demás pruebas. La hoja vigente vence ahora el
mismo día, para comprobar el límite exacto: vence hoy, todavía no está vencida. `ci.yml` agrega un trabajo que ejecuta la suite
con la JVM en `Pacific/Kiritimati`.

### 9. El contrato OpenAPI no describía la conducta real

`/v3/api-docs` no documentaba ningún error 4xx en sus 97 operaciones, y 17 documentaban un código de éxito distinto del real.
Además, dos clases con el mismo nombre simple (`HistoryView` de reclamaciones y de cotizaciones, y `Receipt` de reclamaciones y
de cotizaciones) se fundían en un solo esquema. Así, el contrato describía mal el historial de una hoja y la constancia de
`POST /cart/submit`.

Correcciones:

- `@ResponseStatus` en las 17 operaciones: 10 con 201, 6 con 202 y la descarga con 302.
- `ProblemResponses` documenta los errores RFC 9457 de cada operación a partir de su firma: 400 por parámetros, 413 y 415 por
  cuerpo, 404 por identificador en la ruta, 412 y 428 por `If-Match`, 409 por `Idempotency-Key`, 429 por límite de frecuencia,
  403 en áreas protegidas, 409 y 422 en modificaciones del personal, y 401 y 500 en todas. `@ApiProblems` agrega los propios de
  una operación: 403 al iniciar sesión, 403 y 422 con Google, 409 al confirmar un correo o aceptar una invitación, 409 en la
  descarga bajo solicitud, y 422 al agregar al carrito y al enviarlo.
- `ComplaintViews.HistoryView` y `ComplaintViews.Receipt` pasan a llamarse `ComplaintHistoryView` y `ComplaintReceipt`.

Lo cubren `OpenApiContractIT` y, sobre todo, `OpenApiContractConfiguration`: en todas las pruebas de integración cada respuesta de
MockMvc se compara con el contrato. Se comprueba que el código esté documentado para esa operación, que el tipo de contenido sea el
documentado y que el cuerpo cumpla el esquema, sin campos no documentados. `OpenApiContractTests` demuestra con un contrato mínimo
que el comprobador detecta cada tipo de error. Una prueba nueva impide que dos cargas distintas compartan nombre de esquema.

### 10. `errors[].field` informaba el nombre del parámetro Java

En las operaciones que validan a la vez la ruta y el cuerpo (`POST /staff/legal/{type}/versions`), Spring usa la validación del
método. El manejador ponía en cada error el nombre del parámetro Java (`r`) en lugar del campo JSON (`title`). La prueba de cuerpos
inválidos lo destapó. Corrección: si el error es de un campo, `ApiExceptionHandler` informa ese campo.

### 11. El log revelaba el nombre de la empresa de una consulta

Con `MAIL_DELIVERY=log`, que es el valor por defecto de `application.yml`, `ConfiguredMailGateway` escribía el asunto de cada
correo, y el aviso de una consulta nueva lleva el nombre de la empresa. Además, `OutboxDispatcher` escribía el texto del error de
SMTP, que puede incluir la dirección del destinatario. Corrección: el modo de registro ya no escribe el asunto y el error de envío
se registra solo con el tipo de excepción. El texto completo sigue en `last_error`, visible para el personal. Lo cubren
`LogPrivacyIT`, `ConfiguredMailGatewayTests` y `OutboxDispatcherTests`.

### 12. U+0000 en filtros y notas del personal respondía 409 CONFLICT

PostgreSQL rechaza ese carácter y `ApiExceptionHandler.integrity` traducía el error como conflicto, también en lecturas. Correcciones:

- `RequestParameterGuard` rechaza con 400 `INVALID_CHARACTER` cualquier parámetro de consulta con U+0000 en `/api/**`, después
  de la autenticación. Un anónimo sigue recibiendo 401. `GET /catalog/products?q=` con U+0000 respondía 200 con una lista vacía y
  ahora responde 400.
- `PUT /staff/accounts/{id}/notes` aplica la misma regla a la nota, con `Guard.noNullCharacter`.
- Como defensa adicional, un error de PostgreSQL de clase 22 (dato no válido) responde 400 `INVALID_VALUE` en lugar de 409.

Lo cubren `NullCharacterIT`, con los 8 filtros del personal, el catálogo público, el anónimo y la nota, y `ApiExceptionHandlerTests`.

### 13. La prueba de humo no se podía repetir en 10 minutos

Todas las peticiones salían de la misma IP y la segunda corrida seguida agotaba el límite de 5 formularios cada 10 minutos.
Corrección: cada corrida envía una IP propia en `X-Forwarded-For`, igual que la colección de Postman. La API solo la acepta desde
redes internas. La prueba agrega dos comprobaciones: `GET /actuator/health` por el puerto público responde 401 y el puerto 8081 no
está publicado. Son 34 comprobaciones.

## Cambios en pruebas existentes

- `IdentityIT.administratorManagesStaffAndDisablingRevokesAccess` pide el listado del personal con `size=100`, porque otras pruebas
  también invitan personal sobre la misma base de datos.
- `ComplaintIT.staffInboxHighlightsOverdueSheets` crea una hoja vencida, una vigente y una respondida, y exige solo la vencida. Antes
  solo comprobaba que la lista estaba vacía. En la segunda tanda usa la fecha de Lima en lugar de `CURRENT_DATE`, y la hoja vigente
  vence el mismo día.
- `AuthorizationMatrixIT` deja de derivar lo esperado de `Role.permissions()` (segunda tanda).
- `IntegrationTest` importa `OpenApiContractConfiguration`, y el perfil de pruebas publica `/v3/api-docs` para compararlo con cada
  respuesta (segunda tanda).
- `CatalogAdminIT` separa la prueba de datos sin verificar de la de cuatro ojos, que ahora obtiene `403 FOUR_EYES` por HTTP.
- `PrivacyIT.recordsConsentEvidenceWithoutTrackingData` comprueba que la fila guardada no conserva IP, agente de usuario ni cookies.
- `ModularityTests.writesModuleDocumentation` comprueba que los archivos se generan.
- Las 11 pruebas que solo verificaban el código HTTP comprueban además el `code` del error.
- `customerToken`, `staffToken` y `etagOf` fallan en el paso de preparación que corresponda, en vez de producir un error engañoso después.
- Las aserciones negativas sobre eventos asíncronos esperan a que el registro de publicaciones quede vacío (`awaitEventsProcessed`), en
  lugar de ventanas fijas de 1 o 2 segundos.

Ninguna prueba se desactivó ni se omitió. Clases y métodos se ejecutan en orden aleatorio (`junit-platform.properties`).

## Pruebas agregadas

### Tanda de la segunda auditoría

| Clase | Pruebas | Alcance |
|---|---|---|
| `JwtValidationIT` | 16 | Token correcto aceptado como control; otro emisor, sin emisor, otra audiencia, sin audiencia, vencido, tolerancia de 60 s, `nbf` futuro, otra clave, `alg: none`, HS256, carga alterada, sello revocado o ausente, sujeto inexistente y rol desconocido |
| `NullCharacterIT` | 11 | U+0000 en 8 filtros del personal, en el catálogo público, como anónimo y en la nota interna |
| `OpenApiContractTests` | 8 | El comprobador detecta código, tipo de contenido, campo obligatorio, campo de más, tipo, formato y enum |
| `DocumentedConfigurationIT` | 7 | Políticas de frecuencia, sesiones, bloqueo, cuerpo máximo, plazo del Libro y outbox, leídos de la configuración real y observados: bloqueo de 15 minutos, sesiones de 14 días y 12 horas, cuerpo de 65 536 bytes aceptado y de 65 537 rechazado, plazo de 15 días hábiles en hora de Lima |
| `ManagementPortIT` | 7 | Actuator responde 401 por el puerto público, puerto de gestión 8081 y `compose.yaml` solo publica el 8080 del backend |
| `AuditActionsIT` | 5 | Las 13 acciones de auditoría sin prueba, cada una con un solo registro, recurso y actor correctos |
| `OpenApiContractIT` | 5 | Inventario de 97 operaciones, código de éxito real, errores documentados, esquema `Problem` y nombres de esquema sin colisión |
| `ApiExceptionHandlerTests` | 4 | Error inesperado (500 sin trazas ni datos), duplicado (409), dato no válido (400) y violación sin SQLSTATE |
| `HmacReceiptTokensTests` | 4 | Arranque con clave corta, sin clave, con clave temporal y con clave configurada |
| `EventResubmissionIT` | 2 | Un oyente que falla deja el evento incompleto; el reintento lo entrega sin perder el correo y respeta los 2 minutos de espera |
| `MaintenanceJobsIT` | 1 | Solo se borran las claves de idempotencia vencidas |
| `IdentityMaintenanceIT` | 1 | Solo se borran las sesiones vencidas hace más de 30 días y los códigos vencidos hace más de un día |
| `LogPrivacyIT` | 1 | Consulta, reclamo, derechos, validación fallida, ingreso fallido, recuperación y envío de correos sin datos personales en el log |

También se agregaron casos a:

- `AuthorizationMatrixIT`: la tabla propia de permisos y la exigencia de que no haya errores 5xx.
- `InvalidInputCoverageIT`: 9 operaciones del personal con cuerpo inválido y el 404 de `POST /staff/quotes/{id}/assign`.
- `RateLimitPoliciesIT`: el `Retry-After` de cada política, que comprueba el periodo y no solo la capacidad.
- `ComplaintIT`: el teléfono y la dirección enmascarados, la respuesta por vía postal y el plazo que vence hoy.
- `QuotationIT`: la línea con un producto fuera del catálogo.
- `OutboxDispatcherTests` y `ConfiguredMailGatewayTests`: logs sin destinatario ni asunto.

### Tanda de la primera auditoría

| Clase | Pruebas | Alcance |
|---|---|---|
| `AuthorizationMatrixIT` | 135 | 67 operaciones protegidas: 401 anónimo y permiso exacto con cada uno de los 7 roles; inventario contra los controladores |
| `OptimisticLockingContractIT` | 27 | 26 operaciones con 428, 412 y registro intacto; inventario de las excepciones documentadas |
| `RateLimitPoliciesIT` | 23 | 21 operaciones limitadas con 429 en el umbral exacto, inventario y contadores por IP |
| `ValueInvariantsTests` | 35 | Límites exactos de los valores de dominio |
| `AccountDirectoryFiltersIT` | 15 | Filtros, periodos y órdenes del directorio |
| `AuthenticationServiceTests` | 14 | Decisiones del ingreso y de la rotación de sesiones, incluida la carrera de rotación |
| `UserAccountRulesTests` | 14 | Transiciones de la cuenta |
| `NimbusGoogleIdTokenVerifierTests` | 12 | Firma, emisor, audiencia, vigencia y `email_verified` con una clave local |
| `LastAdministratorRulesTests` | 9 | Último administrador activo y administrador inicial |
| `ProblemDetailsIT` | 8 | Errores del marco web en RFC 9457 |
| `LoginProtectionIT` | 7 | Enumeración, bloqueo, refresh vencido y cuentas solo Google |
| `WebSupportTests` | 7 | Identificador de petición, límites e `If-Match` |
| `JwtKeysTests` | 6 | Carga de la clave PEM y arranque sin clave |
| `OutboxDispatcherTests` | 6 | Fallo de SMTP, espera creciente y paso a `FAILED` |
| `PayloadLimitFilterTests` | 5 | Cuerpo chunked leído por bloques y byte a byte |
| `ProductionProfileIT` | 5 | Arranque con `application-prod.yml`, clave PEM, sin datos de demostración y sin documentación |
| `Argon2PasswordHasherTests` | 4 | Cálculo igual con y sin contraseña |
| `ConfiguredMailGatewayTests` | 4 | SMTP y modo de registro |
| `DatabaseRolesIT` | 4 | Script real de roles y migraciones, conectando como `fundigsac_app` |
| `InvalidInputCoverageIT` | 4 | Entradas inválidas en operaciones que solo se probaban con datos correctos |
| `SecurityCurrentActorTests` | 4 | Actor derivado del JWT |
| `ConcurrencyIT` | 3 | 30 folios simultáneos sin duplicados ni huecos, 10 reintentos con la misma clave y 1×200 + 9×412 con `If-Match` |
| `AccessDocumentationTests` | 3 | Descripción OpenAPI de invitación y confirmación con Google |
| `RevocationCacheIT` | 1 | Caché de revocación real de 10 segundos, de punta a punta |

También se agregaron casos a `PlatformSecurityIT` (HSTS, COOP, honeypot en los cuatro formularios y cuerpo chunked), `CatalogIT` (filtros
`family` y `sector`), `ComplaintIT` (menor con apoderado), `QuotationIT` (cotizar con sesión), `StaffUserManagementIT` y `CatalogAdminIT`.

### Mutantes

Cada mutante se aplicó en una copia temporal del Backend, nunca en el repositorio, y se ejecutó la suite Maven completa (`verify`,
sin JaCoCo, dos copias en paralelo). Un mutante muere si al menos una prueba falla. Los mutantes no se midieron contra la prueba de
humo ni contra Postman.

Segunda tanda, 30 mutantes sobre el código definitivo:

| Origen | Mutantes | Resultado |
|---|---|---|
| Los 13 de la segunda auditoría | `READ_ONLY` con `USERS_MANAGE` y `AUDIT_READ`; JWT sin audiencia, sin emisor y sin vencimiento; trigger del Libro sin efecto; periodo del formulario público de 5 s; bloqueo de 5 s; cuerpo máximo de 69 000 bytes; plazo de 30 días hábiles; sesión del personal de 30 días; constancia con teléfono y dirección completos; anonimización que conserva datos; auditoría sin actor | 13 de 13 mueren. En la auditoría sobrevivían 10 |
| 17 nuevos sobre las correcciones | Sin filtro de U+0000 en parámetros y en la nota; error de clase 22 como 409; `errors[].field` con el nombre del parámetro; contrato sin 428, sin 429, con 200 en `POST /quotes` y con esquemas fundidos; asunto en el log; texto del error de SMTP en el log; reintento de eventos sin efecto y sin espera; limpieza que borra claves vigentes; sesiones borradas al día; respuesta postal al consumidor; clave de constancia de 16 bytes; línea de texto libre sin nombre | 17 de 17 mueren |

En la primera ronda sobrevivió "reintento de eventos sin espera": la prueba comprobaba que no había correos justo después del
reintento, pero la entrega es asíncrona. Ahora exige que durante 3 segundos no llegue ningún correo. Con esa prueba, el mutante y
el de "reintento sin efecto" se ejecutaron de nuevo y mueren.

Primera tanda: los 26 mutantes de esa tanda mueren (11 que sobrevivían en la primera auditoría, 2 que ya se detectaban y 13 nuevos).
No se volvieron a ejecutar en la segunda tanda. Las pruebas que los detectaban siguen en la suite y ninguna se quitó.

### Primera tanda

Son 63 pruebas de integración y 7 unitarias al cerrar esa tanda. La tabla da los totales actuales: `StaffUserManagementIT` tiene 6
pruebas porque la primera auditoría le agregó 2.

| Clase | Pruebas | Alcance |
|---|---|---|
| `PublicCatalogDetailIT` | 5 | Detalle público de familias y documentos |
| `StaffCatalogProductsIT` | 5 | Listado, detalle, archivo y reapertura de fichas |
| `StaffCatalogDocumentsIT` | 8 | Registro, edición, publicación y retiro de documentos |
| `StaffComplaintDeskIT` | 5 | Hoja completa, asignación y notas internas |
| `StaffInquiryDeskIT` | 4 | Bandeja y asignación de consultas |
| `StaffPrivacyDeskIT` | 4 | Historial legal, bandeja de derechos y paso a trámite |
| `StaffUserManagementIT` | 6 | Ficha del personal, roles, reactivación y, desde la primera auditoría, paginación y descripción de la invitación |
| `SessionAndCredentialsIT` | 8 | Cierre de sesión, cambio de contraseña, reenvío e invitación |
| `CartManagementIT` | 9 | Líneas, vaciado, aislamiento entre clientes y reintentos |
| `NotificationRetryIT` | 4 | Reintento manual de correos |
| `AuditTrailIT` | 3 | Filtros, validación y permiso de auditoría |
| `PublicFormsIdempotencyIT` | 4 | `Idempotency-Key` en reclamaciones, consultas y derechos |
| `SecurityStampValidatorTests` | 7 | Revocación de JWT con caché real |

### Las 32 operaciones que no tenían prueba

En la columna de autorización, 401 es sin sesión y 403 es sin permiso. N/A indica que el caso no aplica a la operación.

| Operación | Caso feliz | Validación | Autorización | 404 | `If-Match` |
|---|---|---|---|---|---|
| `GET /catalog/categories/{slug}` | Sí | Longitud | Pública | Sí | N/A |
| `GET /resources/{slug}` | Sí | Longitud | Pública | Sí | N/A |
| `GET /legal/{type}/versions` | Sí | Longitud | Pública | Sí | N/A |
| `POST /auth/verify-email/resend` | Sí | Sí | Pública, sin revelar cuentas | N/A | N/A |
| `POST /auth/logout` | Sí | Sí | Pública | N/A | N/A |
| `POST /auth/invitation/accept` | Sí | Sí | Por token | N/A | N/A |
| `POST /account/password` | Sí | Sí | 401 y 403 | N/A | N/A |
| `PATCH /cart/items/{itemId}` | Sí | Sí | 401 y 403 | Sí, línea de otro cliente | N/A |
| `DELETE /cart` | Sí | N/A | 401 y 403 | Solo afecta al carrito propio | N/A |
| `GET /staff/catalog/products` | Sí | Sí | 401 y 403 | N/A | N/A |
| `GET /staff/catalog/products/{id}` | Sí | UUID | 401 y 403 | Sí | N/A |
| `POST /staff/catalog/products/{id}/archive` | Sí | ETag inválido | 401 y 403 | Sí | 428 y 412 |
| `POST /staff/catalog/products/{id}/reopen` | Sí | Transición, 409 | 401 y 403 | Sí | 428 y 412 |
| `GET /staff/catalog/documents` | Sí | Sí | 401 y 403 | N/A | N/A |
| `POST /staff/catalog/documents` | Sí | Sí | 401 y 403 | N/A | N/A |
| `GET /staff/catalog/documents/{id}` | Sí | UUID | 403 | Sí | N/A |
| `PUT /staff/catalog/documents/{id}` | Sí | Sí | 401 y 403 | Sí | 428 y 412 |
| `POST /staff/catalog/documents/{id}/publish` | Sí | Transición, 409 | 401 y 403 | Sí | 428 y 412 |
| `POST /staff/catalog/documents/{id}/withdraw` | Sí | Transición, 409 | 401 y 403 | Sí | 428 y 412 |
| `GET /staff/complaints/{id}` | Sí | UUID | 401 y 403 | Sí | N/A |
| `POST /staff/complaints/{id}/assign` | Sí | Sí | 401 y 403 | Sí | 428 y 412 |
| `POST /staff/complaints/{id}/notes` | Sí | Sí | 401 y 403 | Sí | 428 y 412 |
| `GET /staff/inquiries` | Sí | Sí | 401 y 403 | N/A | N/A |
| `POST /staff/inquiries/{id}/assign` | Sí | Sí | 401 y 403 | Sí | 428 y 412 |
| `GET /staff/privacy/requests` | Sí | Sí | 401 y 403 | N/A | N/A |
| `GET /staff/privacy/requests/{id}` | Sí | N/A | 401 y 403 | Sí | N/A |
| `POST /staff/privacy/requests/{id}/start` | Sí | Transición, 409 | 401 y 403 | Sí | 428 y 412 |
| `GET /staff/users/{id}` | Sí | UUID | 401 y 403 | Sí, también con cuenta de cliente | N/A |
| `PUT /staff/users/{id}/roles` | Sí | Sí | 401 y 403 | Sí | 428 y 412 |
| `POST /staff/users/{id}/enable` | Sí | Transición, 409 | 401 y 403 | Sí | 428 y 412 |
| `POST /staff/notifications/{id}/retry` | Sí | UUID | 401 y 403 | Sí | N/A |
| `GET /staff/audit` | Sí | Sí | 401 y 403 | N/A | N/A |

`Idempotency-Key` queda probada en las cinco operaciones que la documentan: `POST /quotes`, `/complaints`, `/inquiries`,
`/privacy/requests` y `/cart/submit`. En cada una se comprueba el mismo folio al reintentar, el 409 si la clave se reutiliza con otro
contenido y el 400 si la clave no es válida, salvo en `POST /quotes`, donde la clave inválida no se comprueba.

## Colección de Postman

Archivos en `Backend/postman`:

- `fundigsac-backend.postman_collection.json`: 235 peticiones en 10 carpetas, con flujos públicos, de acceso, de cuenta y del personal.
- `local.postman_environment.json`: URL locales. La contraseña del administrador queda vacía en el archivo.
- `run.sh`: toma la contraseña de `secrets/bootstrap_admin_password` y ejecuta la colección.

Los códigos de verificación y acceso se leen de Mailpit. Cada petición envía una IP distinta en `X-Forwarded-For` para no agotar los
límites por IP, y cada corrida genera correos propios, por lo que puede repetirse sin limpiar la base de datos.

El CLI v1.75.0 ejecutó la colección local sin iniciar sesión ni pedir un plan. No se publicó nada en ningún espacio de trabajo. Al
terminar muestra este aviso informativo, que no afecta al resultado:

> Publishing run details to postman cloud is currently supported only for collections specified via postman collection id or collections belonging to git linked APIs

## Entorno Docker

El volumen `fundigsac_pgdata` ya existía desde el 16 de octubre de 2026, con datos locales y con contraseñas de una carpeta `secrets`
que ya no estaba disponible. Con los secretos nuevos el backend no podía conectarse (`password authentication failed for user
"fundigsac_migrator"`).

Ese volumen no se borró ni se modificó. Se agregó `Backend/compose.override.yaml`, que Compose carga de forma automática y que hace que
el entorno use el volumen nuevo `fundigsac_pgdata_pruebas`. El archivo es nuevo en el repositorio y Git no lo ignora, así que hay que
decidir si se conserva. Para volver al volumen antiguo basta con eliminarlo, pero se necesitarían las contraseñas originales.

El entorno queda en marcha en `http://localhost:8080` (API), `http://localhost:8025` (Mailpit) y Swagger UI en
`http://localhost:8080/swagger-ui.html`. Las corridas de humo y de Postman dejaron datos de prueba en el volumen nuevo.

## Brechas y observaciones

| Tema | Situación |
|---|---|
| `POST /auth/invitation/accept` | El correo de invitación solo enlaza al acceso con código y no incluye el token, así que en la operación real no se usa. Queda marcado como obsoleto. La prueba ya usa el token real emitido al invitar, sin sembrarlo por SQL. Falta decidir si se retira o si la invitación debe enviar el enlace. |
| Confirmación con Google | Solo existe en la API. `Frontend` hoy no llama a `DELETE /account` ni a `POST /account/password`, así que esta corrección no tiene pantalla todavía. |
| `POST /auth/google` | Toda la validación se prueba con claves locales, sin contactar a Google. La descarga real de las claves públicas de Google no se ejecuta en ninguna prueba. En el entorno local no hay `GOOGLE_CLIENT_ID`. |
| `POST /staff/notifications/{id}/retry` | En Postman solo se comprueban 409 y 404, porque provocar un fallo real de SMTP exige detener Mailpit. El fallo y el reintento se prueban en `OutboxDispatcherTests` y `NotificationRetryIT`. |
| Revocación de JWT | Un token revocado sigue siendo válido hasta 10 segundos, según el diseño documentado. El perfil de pruebas mantiene la caché apagada para no esperar en cada prueba; `RevocationCacheIT` usa los 10 segundos reales. |
| `restrict_app_role` | Sigue sin efecto si el rol no existe, necesario para el perfil de pruebas. `DatabaseRolesIT` prueba el caso con rol. Un `DB_APP_ROLE` mal escrito en un despliegue no daría error. |
| Corte de cuerpo chunked | Se prueba con MockMvc y a nivel de filtro. Tomcat embebido no arranca en este equipo (`Unable to establish loopback connection`); en la auditoría se comprobó el 413 contra Docker. |
| CI | `ci.yml` agrega JaCoCo, el umbral y un trabajo con humo y Postman, pero solo se ejecutará en GitHub: no se hizo push. |
| Mutación | Los mutantes son conjuntos elegidos a mano sobre los controles críticos y se midieron solo contra la suite Maven, no contra humo ni Postman. No es un análisis exhaustivo. |
| Cobertura de ramas | El 14,5 % restante son en su mayoría comprobaciones defensivas de nulos y variantes de formato. |
| Documentación de la API | `/v3/api-docs` responde porque el entorno usa el perfil `local`. Con `application-prod.yml` responde 404, comprobado en `ProductionProfileIT`. |
| 409 y 422 en el contrato | Se documentan por regla en todas las modificaciones del personal y, con `@ApiProblems`, en las operaciones de acceso y del carrito que los usan. Es posible que alguna modificación del personal documente un 409 o un 422 que nunca devuelve. El comprobador garantiza lo contrario: ningún código observado queda sin documentar. |
| Comprobación del contrato | Valida códigos, tipos de contenido y esquemas de las respuestas en MockMvc. No valida los cuerpos de las peticiones contra el esquema ni el tráfico de humo y Postman. Un campo opcional se acepta ausente o con `null`. |
| Actuator en el puerto 8081 | MockMvc no levanta puertos. Se comprueba con MockMvc (401 por el puerto público), con la configuración (`management.server.port=8081`), con `compose.yaml` (solo publica el 8080) y en la prueba de humo contra Docker (401 en el 8080 y el 8081 sin publicar). |
| Reintento de eventos tras un reinicio | `EventResubmissionIT` simula la caída con un oyente que falla y prueba la tarea programada de reintento. El reintento automático al arrancar (`republish-outstanding-events-on-restart`) solo se comprueba como configuración: ninguna prueba reinicia la aplicación. |
| Zona horaria | La suite se comprueba con la JVM en UTC+14 y en Lima. No se ejecutó en el horario real de 19:00 a 24:00 de Lima con la JVM en UTC; UTC+14 reproduce el mismo desfase de fecha. |
| Filtros con U+0000 | Ahora responden 400 también en las rutas públicas. Antes, `GET /catalog/products?q=` con ese carácter respondía 200 con una lista vacía. |
