# Válvulas Perú (RNA World Trade)

| Campo | Valor |
|---|---|
| Sitio indicado | https://valvulasperu.pe/ |
| Segmento | Importador |
| Fecha de la revisión | 9 de noviembre de 2026 |
| Estado del rastreo | error (el dominio no existe en DNS) |
| Páginas con datos | 0 |
| PageSpeed móvil | n/d (cuota de la API agotada) |
| Datos en bruto | `Report/competencia/datos/valvulas-peru.json` |

## Resultado

No se pudo analizar este sitio. El dominio `valvulasperu.pe` no resuelve, por lo que no se obtuvo ninguna página ni el archivo robots.txt. Este informe no contiene datos del sitio. Las secciones de análisis quedan sin datos para no presentar suposiciones como hechos.

## Evidencia

| Comprobación | Resultado |
|---|---|
| Rastreador en Docker (Scrapling, Fetcher HTTP) | `estado: error`, `No se pudo leer robots.txt: DNSError` |
| DNS del equipo local | Dominio inexistente |
| DNS dentro del contenedor | No resuelve; `google.com` sí resuelve, así que la red del contenedor funciona |
| Google Public DNS, `valvulasperu.pe` y `www.valvulasperu.pe`, tipos A, AAAA y NS | Status 3 (NXDOMAIN) en todos los casos |
| Cloudflare DNS, `valvulasperu.pe` tipo A | Status 3 (NXDOMAIN), con autoridad de la zona `.pe` (serie 2026110911) |
| Búsqueda web de la empresa y del dominio | Sin resultados de la empresa ni del dominio |

La búsqueda específica por nombre no devolvió la empresa, pero `valvulasperu.pe` sí salió en las búsquedas temáticas C6, C9, Q8, Q12 y Q17. Eso indica que el índice de la herramienta conserva el dominio.

La respuesta NXDOMAIN procede de la propia zona `.pe` y coincide en tres resolutores distintos. Por eso se descarta un fallo local de la red.

Esto no es un bloqueo del sitio: no hubo respuesta 403 ni 429, captcha ni página de desafío. El contador `solicitudes_http: 1` del JSON registra un intento que no llegó a conectarse con ningún servidor.

Inferencia: el dominio pudo vencer o darse de baja después de que el buscador lo indexara, o bien la dirección registrada en `COMPETIDORES.md` es incorrecta. DNS no permite distinguir entre ambos casos. Haría falta consultar el WHOIS de punto.pe.

## PageSpeed móvil

La API pública respondió HTTP 429 (`RESOURCE_EXHAUSTED`, `rateLimitExceeded`). Se hizo una sola llamada y se registra **n/d**. No se midió ningún KPI de rendimiento ni de SEO de este sitio.

## Análisis solicitado

| Apartado | Estado |
|---|---|
| Cobertura de catálogo y familias | Sin datos |
| Profundidad de especificaciones | Sin datos |
| Normas y certificaciones citadas | Sin datos |
| Palabras clave inferidas de títulos y encabezados | Sin datos |
| Marcado de esquema (JSON-LD) | Sin datos |
| Enlazado interno | Sin datos |
| Llamadas a la acción | Sin datos |
| Señales de SEO local | Sin datos |
| Fortalezas y debilidades de experiencia de usuario | Sin datos |

## Información previa no verificada

`COMPETIDORES.md` describe a la empresa como importador con válvulas de hierro dúctil, marcos y tapas D400 y línea HDPE, para minería, agricultura y construcción. La empresa apareció en las búsquedas C6 y C9. Ese documento cita además una ficha en `valvulasperu.pe/producto/marco-y-tapa-de-buzon-hierro-ductil-d400/`, que hoy no es accesible porque el dominio no resuelve.

El mismo documento menciona `valvulasperu.com.pe` (A.C. Trading Company), con textos casi idénticos, y señala que podría ser la misma empresa. Ese sitio no se rastreó: no era el objetivo indicado y su vínculo con RNA World Trade no está confirmado.

## Oportunidades para FUNDIGSAC

Todas son inferencias, porque no hay datos del sitio que las respalden.

1. Si se confirma que el dominio está caído, este competidor deja de captar demanda orgánica en las consultas donde apareció: importador y distribuidor de válvulas para saneamiento, minería y agricultura (C6) y tapa de buzón D400 en Lima (C9). FUNDIGSAC puede reforzar páginas dedicadas a esas dos intenciones de búsqueda.
2. Conviene comparar FUNDIGSAC con `valvulasperu.com.pe` solo después de confirmar qué empresa opera ese sitio.

## Acciones pendientes

1. Consultar en el WHOIS de punto.pe si `valvulasperu.pe` estuvo registrado y cuándo venció.
2. Decidir si se sustituye el objetivo por `valvulasperu.com.pe` o si esta empresa se retira del listado de competidores.
3. Repetir la medición de PageSpeed cuando se recupere la cuota, solo si existe un dominio activo que medir.

## Notas de método

- El rastreo se ejecutó una sola vez, dentro de la imagen `fundig-scrapling`.
- Durante el diagnóstico se ejecutó también un `curl` a `/robots.txt` desde el equipo, con el User-Agent del estudio. Falló en la resolución de DNS y no llegó a ningún servidor. Se apartó de la regla de usar solo el Fetcher de Scrapling.
- Esta revisión no incluyó correcciones en los sitios de FUNDIGSAC, por lo que no hubo KPI propios que medir.
