# EATHISA Perú

| Campo | Valor |
|---|---|
| Sitio indicado | https://web.eathisa.com.pe/ |
| Segmento | Importador y distribuidor |
| Fecha de la revisión | 9 de noviembre de 2026 |
| Estado del rastreo | ok |
| Páginas con datos | 22 de 22 solicitadas (23 solicitudes HTTP contando robots.txt) |
| robots.txt | Presente, sin demora de rastreo; declara `sitemap.xml`. Ninguna página omitida por robots |
| PageSpeed móvil | n/d (cuota de la API agotada) |
| Datos en bruto | `Report/competencia/datos/eathisa.json` |

## Resumen

EATHISA publica su catálogo como entradas de blog. La mayor parte del contenido visible es de 2018 y la entrada más reciente es de abril de 2022. Cubre tubería, compuerta, mariposa y marcos y tapas, y añade una línea de ingeniería que FUNDIGSAC no presenta: válvulas anulares, actuadores, medidores de caudal y biofiltros.

Su sitio no tiene datos estructurados JSON-LD, H1 en la portada, atributo de idioma ni enlaces `tel:`. Su punto más sólido es la lista de normas de la tubería y la mención de aprobación de SEDAPAL en válvulas compuerta, que es una declaración comercial sin verificar.

Inferencia: la plataforma es Blogger, por el patrón de rutas `/AAAA/MM/*.html`, `/p/*.html` y `/search/label/*`.

## Alcance y límites de la medición

Estos límites condicionan la lectura de las secciones siguientes.

- **Rastreo agotado, no truncado.** El rastreador terminó con `pendientes_sin_visitar: 0`. Llegó a 22 páginas siguiendo enlaces.
- **El catálogo real puede ser mayor.** El rastreador no visita rutas `/search`, de modo que no entró en las 13 etiquetas ni en la paginación de la portada. Tampoco lee el sitemap. Las 16 entradas analizadas son un mínimo.
- **Especificaciones sin medir.** El JSON registra 0 pares atributo-valor. Ese cero no significa que las páginas carezcan de datos técnicos: la extracción de tablas genéricas solo se activa en rutas de tipo `/producto/`, y estas no lo son.
- **Productos sin selector.** El campo `productos` está vacío porque los selectores son de WooCommerce. La lista de esta revisión sale de títulos y H1.
- **Texto no almacenado.** Solo se guardan título, meta descripción, H1, H2 y enlaces. La presencia de una dirección o de un botón en el cuerpo no se puede afirmar ni descartar.
- **Sin revisión visual.** El rastreo fue HTTP simple, sin navegador. No se evaluó el diseño ni el comportamiento en móvil.

## Rendimiento

La API pública de PageSpeed respondió HTTP 429 (`RESOURCE_EXHAUSTED`, `rateLimitExceeded`). Se hizo una sola llamada, que pedía rendimiento, SEO, accesibilidad y buenas prácticas. Se registra **n/d** en las cuatro categorías.

El único dato disponible es el tamaño del HTML: entre 133 082 y 173 781 bytes, con media de 143 092 bytes por página.

Inferencia: el HTML es pesado para páginas de poco contenido, probablemente por estilos y widgets incrustados en la plantilla. Sin PageSpeed no se puede concluir sobre LCP, INP ni CLS.

## Cobertura de catálogo y familias

| Familia | Entradas encontradas | Fecha en la URL |
|---|---|---|
| Tubería de hierro dúctil | Tubería de Hierro Ductil ISO 2531 | 2018/05 |
| Válvulas compuerta | Compuerta bridada con aprobación de SEDAPAL; compuerta de asiento elastomérico marca EATHISA | 2022/04; 2018/02 |
| Válvula mariposa | Mariposa excéntrica | 2018/02 |
| Válvulas de control | Control y regulación; anular F500 con actuador | 2018/04; 2018/04 |
| Marcos y tapas | Marco y tapa de alcantarillado EATHISA | 2019/11 |
| Uniones y accesorios | Adaptador universal brida-campana (Maxiquick); unión de desmontaje; acople flexible Dresser; brida plana para soldar ISO PN16 | 2018/02 (las cuatro) |
| Medidores de caudal | Electromagnético (BEIFEI); ultrasónico (Micronics) | 2018/02 (ambos) |
| Actuadores | Actuadores eléctricos AUMA | 2018/03 |
| Tratamiento | Biofiltro de olores | 2019/03 |
| Servicio y proyectos | Suministro y montaje de válvula anular DN700 | 2018/12 |

Distribución de las 22 páginas por sección: 13 de 2018, 2 de 2019, 1 de 2022, 5 institucionales (`/p/`) y la portada.

**Etiquetas del sitio (13):** valvulas, Uniones, medidores, actuadores, tuberia, alcantarillado, bridas, marco y tapas, montaje, Servicio, Tratamiento, valvulas de compuerta, valvulas de control.

No existe etiqueta para válvula check ni para válvula de aire o ventosa. Alguna entrada de esos tipos podría estar bajo la etiqueta general `valvulas`, que no se rastreó.

**Marcas mencionadas:** EATHISA (marca propia en compuerta, mariposa y marcos y tapas), AUMA, BEIFEI y Micronics, de la que se declara importador autorizado. También aparecen los nombres Maxiquick y Maxifit. Una serie de compuertas se describe como de procedencia italiana.

**Vigencia.** Han pasado 4 años y 7 meses desde la entrada más reciente. Inferencia: el sitio tiene poco mantenimiento. Esto no prueba que la empresa haya reducido su actividad comercial.

## Profundidad de especificaciones

Los datos siguientes proceden de títulos y meta descripciones.

| Producto | Dato visible |
|---|---|
| Mariposa excéntrica | Marca EATHISA, modelo 201, DN200-2000, PN10, PN16 y PN25, doble excentricidad |
| Anular F500 | PN10, PN16 y PN25, con actuador |
| Compuerta bridada | Bridas BB, Serie 14, procedencia italiana |
| Brida plana | Para soldar, ISO PN16 |
| Montaje anular | DN700, PN16, con actuador eléctrico AUMA |
| Ultrasónico | Modelo PF LV550 portátil |
| Marco y tapa | Circular, con seguro, hierro dúctil, EN124 |

`COMPETIDORES.md` indica tubería de DN50 a DN2000. Este rastreo no volvió a comprobar ese rango.

Ninguna de las 22 páginas enlaza un PDF u otro documento alojado en el propio sitio (`documentos_enlazados` vacío). Un documento alojado en un servicio externo no quedaría registrado.

Inferencia: cada ficha es una entrada descriptiva con encabezado "CARACTERISTICAS", sin matriz de cotas por diámetro descargable. Hay que abrir las páginas para confirmarlo.

## Normas y certificaciones citadas

| Norma, tal como aparece | Página | Observación |
|---|---|---|
| ISO 2531:2009 | Tubería | Norma de producto |
| ISO 4179:2005 | Tubería | Revestimiento interior de mortero |
| ISO 4633:2002 | Tubería | Juntas de elastómero |
| ISO 8179-2:1995 | Tubería | Revestimiento exterior |
| ISO 81791:2004 | Tubería | Inferencia: errata de ISO 8179-1:2004 |
| ISO 9001 | Tubería | Sin año ni organismo en los datos capturados |
| ISO 14001:2004 | Tubería | Edición sustituida por la de 2015 |
| ISO 28001:2001 | Tubería | Inferencia: posible errata; esa combinación de número y año no corresponde a una edición conocida |
| EN1074-1 | Compuerta bridada | Con mención de aprobación de SEDAPAL |
| ISO 7259 | Compuerta de asiento elastomérico | Norma de válvulas compuerta |
| EN124 | Marco y tapa | Norma de tapas de registro |

"ISO 2531" también aparece en las 22 páginas. Inferencia: se debe a que el enlace lateral a la tubería lleva la norma en el título, y no a que cada página la cite.

No se detectó ninguna cita de AWWA, ASTM, NSF ni NTP. Las aprobaciones y certificados son declaraciones del sitio y no se verificaron con SEDAPAL ni con organismos certificadores.

## Palabras clave inferidas

Toda esta sección es inferencia a partir de títulos y H1.

| Intención | Términos |
|---|---|
| Tubería | tubería de hierro dúctil ISO 2531 |
| Compuerta | válvulas compuerta bridada aprobación SEDAPAL; válvula compuerta asiento elastomérico |
| Mariposa y control | válvula mariposa excéntrica; válvulas de control regulación; válvula anular PN10 PN16 PN25 |
| Alcantarillado | marco y tapa de alcantarillado |
| Accesorios | unión de desmontaje autoportante; acople flexible Dresser; adaptador universal brida campana; brida plana para soldar PN16 |
| Instrumentación | medidores de caudal electromagnético; medidores de caudal ultrasónicos; actuadores eléctricos AUMA |
| Tratamiento | biofiltro de olores |
| Marca | EATHISA PERU |

El término más diferenciador es "aprobación de SEDAPAL". Los títulos no incluyen ciudades ni términos como "precio", "proveedor" o "Lima". Hay faltas que reducen la coincidencia con búsquedas bien escritas o provocan mala imagen: "Ductil", "Valvulas", "Dressser" y `valvla` en una URL.

**Metadatos medidos:**

| Elemento | Resultado |
|---|---|
| Títulos | 12 a 71 caracteres. La portada dice solo "EATHISA PERU", 12 caracteres |
| Meta descripción | Presente en 20 de 22. Falta en Ingeniería y Proyectos y en Área Comercial |
| Meta descripción cortada con "..." | 19 de 20 |
| H1 | Presente en 21 de 22. Falta en la portada |
| H2 en páginas internas | 0 de contenido. Las 21 repiten los 5 H2 de la barra lateral |
| Canónica | Autorreferente en 22 de 22 |
| Atributo `lang` | Ausente en 22 de 22 |

## Marcado de esquema

No hay ningún bloque JSON-LD en las 22 páginas: ni Organization, Product, BreadcrumbList ni LocalBusiness. El rastreador solo mide JSON-LD, de modo que no descarta microdatos en la plantilla.

## Enlazado interno

Cada página tiene entre 24 y 29 enlaces internos únicos, con media de 25,7. La estructura base suma 24 enlaces: 11 de menú, 5 entradas fijas en la barra lateral y 8 etiquetas.

| Grupo | Enlaces entrantes (de 22 páginas) |
|---|---|
| Tubería ISO 2531, compuerta de asiento, adaptador universal, unión de desmontaje, acople Dresser | 21 cada una |
| Compuerta SEDAPAL, marco y tapa, biofiltro, montaje DN700 | 3 cada una |
| Mariposa, anular F500, válvulas de control, brida plana, actuadores, medidor electromagnético | 2 cada una |
| Medidor ultrasónico | 1 |

Inferencia: la autoridad interna se concentra en cinco entradas fijas, entre ellas tres de accesorios. La válvula compuerta con aprobación de SEDAPAL, su producto más comercial y reciente, recibe solo 3 enlaces.

Inferencia: las familias se agrupan en `/search/label/`, rutas que habitualmente quedan fuera del índice en Blogger. Si es así, el sitio carece de páginas de categoría posicionables. No se hizo esa comprobación, y el cuerpo del robots.txt no se conserva en el JSON.

## Llamadas a la acción

- El menú incluye CONTACTAR, ÁREA COMERCIAL y SERVICIO AL CLIENTE. Esta última contiene preguntas frecuentes sobre garantía.
- La meta descripción de contacto publica un WhatsApp comercial: [celular omitido].
- Hay un widget de búsqueda ("¿Qué estas Buscando?") y otro de Facebook.
- No hay ruta de cotización ni carrito entre los enlaces internos.
- No hay enlaces `tel:` en ninguna página.
- No se registró ningún correo. El rastreador solo conserva buzones genéricos, de modo que un buzón con otro formato no aparecería.

Inferencia: la conversión depende de que el visitante vaya a Contactar y escriba por WhatsApp. No se comprobó si existe un botón `wa.me`, porque los enlaces externos no se almacenan.

## Señales de SEO local

| Señal | Resultado |
|---|---|
| LocalBusiness u Organization en JSON-LD | No |
| Dirección, teléfono o correo estructurados | No |
| Enlaces `tel:` | No |
| Atributo de idioma o región | No |
| Ciudades en títulos o H1 | No; solo "PERU" como parte de la marca |
| Alcance declarado | "A todo el Perú y resto del mundo" (meta de portada) |
| Identidad | "EATHISA PERU SA", empresa peruana del Grupo EATHISA |
| Dominio | `.com.pe`, servido desde el subdominio `web.` |

El perfil de empresa en Google no se midió.

## Experiencia de usuario

**Fortalezas**

- Menú corto por familias: válvulas, uniones, medidores, actuadores y tubería.
- Títulos uniformes con el formato "Producto - EATHISA PERU".
- Canónicas correctas en todas las páginas.
- Página de preguntas frecuentes sobre garantía.
- Una entrada de proyecto real con diámetro, presión y actuador (DN700).

**Debilidades**

- Fichas con fecha en la URL y aspecto de blog, sin plantilla de producto. Esta última parte es inferencia.
- Contenido antiguo, sin señales de actualización tras 2022.
- Portada sin H1 y H2 internos sin valor para el contenido.
- Errores ortográficos en títulos y encabezados.
- Sin documentos técnicos propios enlazados.
- Sin flujo de cotización.
- Meta descripciones generadas automáticamente y cortadas.

## Oportunidades para FUNDIGSAC

Todas son inferencias. Las referencias a FUNDIGSAC proceden del código del repositorio y no se verificaron en producción.

1. **Disputar "tubería de hierro dúctil ISO 2531".** Es la entrada más reforzada de EATHISA y cita ediciones antiguas y erratas. Una página de FUNDIGSAC con ediciones vigentes, revestimientos y juntas, y una matriz por DN, superaría en precisión. Cada edición debe confirmarse antes de publicarse.
2. **Responder a "aprobación de SEDAPAL".** Conviene crear una sección de homologaciones por producto solo si existe documento que lo respalde. No debe afirmarse sin evidencia, con el mismo criterio de QA-043 para el marcado de producto.
3. **Ocupar check y ventosas.** FUNDIGSAC tiene ambas familias en su catálogo y EATHISA no tiene etiqueta para ellas. Conviene dar a cada una su página de categoría indexable.
4. **Marcos y tapas por clase.** EATHISA tiene una entrada con 3 enlaces entrantes. Una página con clases EN 124, D400, seguro y carga de ensayo cubriría mejor esa intención. FUNDIGSAC tiene `marco-tapa-d400`, pero hoy es una referencia con `noindex`.
5. **Mantener datos estructurados.** El código de FUNDIGSAC declara Organization, WebSite, Product, Brand y BreadcrumbList. EATHISA no tiene JSON-LD, y esto es una ventaja directa si se mantiene válido en producción.
6. **Destacar la cotización.** FUNDIGSAC tiene `/cotizar` y carrito. Cada ficha debería mostrar esa acción junto con WhatsApp y teléfono con enlace `tel:`.
7. **Publicar fichas técnicas en PDF indexables.** EATHISA no enlaza documentos propios. El repositorio de FUNDIGSAC incluye `src/lib/catalog-pdf.ts`, base posible para este trabajo.
8. **Evaluar accesorios de instalación.** La unión de desmontaje, el acople Dresser y el adaptador universal reciben la mayor parte del enlazado de EATHISA. Conviene confirmar si FUNDIGSAC los vende y darles página propia.
9. **Publicar casos de obra.** La entrada DN700 muestra el formato: suministro, diámetro, presión y actuador. FUNDIGSAC puede hacer lo mismo con autorización del cliente.
10. **Reforzar el SEO local.** FUNDIGSAC ya declara `lang="es-PE"` y dirección en Organization. El siguiente paso es añadir contenido para Lima y regiones, con base en clientes reales.
11. **No priorizar anulares, medidores, actuadores ni biofiltros** salvo que se decida entrar en esa línea. Ahí EATHISA ofrece ingeniería con marcas reconocidas, y competir exigiría un catálogo que FUNDIGSAC no presenta.

## Acciones pendientes

1. Repetir la medición de PageSpeed cuando se recupere la cuota.
2. Confirmar la actividad comercial actual de EATHISA por una vía distinta del sitio web.
3. Si se necesita el total del catálogo, consultar el sitemap declarado en robots.txt.
4. Revisar manualmente dos fichas (tubería y compuerta) para confirmar la profundidad real de sus especificaciones.

## Notas de método

- El rastreo se ejecutó una sola vez, dentro de la imagen `fundig-scrapling`, con el User-Agent `FundigsacMarketResearch/1.0` e intervalo de 3 segundos.
- No hubo respuestas 403 ni 429, captcha ni páginas de desafío en el sitio.
- La revisión no incluyó correcciones en los sitios de FUNDIGSAC, por lo que no hubo KPI propios que medir.
