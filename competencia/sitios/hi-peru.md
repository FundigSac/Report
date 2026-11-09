# Hi Perú SAC

Ficha de análisis competitivo para FUNDIGSAC. Fecha de la medición: 9 de noviembre de 2026.

| Dato | Valor |
|---|---|
| Sitio | https://www.hiperusac.com.pe/ |
| Segmento | Importador y distribuidor |
| Datos crudos | `Report/competencia/datos/hi-peru.json` |
| Estado del rastreo | ok |
| PageSpeed móvil, rendimiento | n/d |
| PageSpeed móvil, SEO | n/d |

Convención de lectura: lo que no lleva marca es un hecho observado en los datos del rastreo. Lo que empieza con "Inferencia:" es una interpretación y debe confirmarse antes de usarse en una decisión.

## 1. Resumen

Hi Perú concentra su oferta en dos ejes: la línea HDPE, con máquinas de fusión, y las válvulas, en buena parte de la marca Mafusa, de la que se declara distribuidor exclusivo en Perú. De los 126 nombres de producto observados, 64 son HDPE o máquinas y 49 son válvulas.

El hierro dúctil tiene poco peso visible y no apareció ningún marco ni tapa de buzón. Esa es la mayor diferencia con FUNDIGSAC.

Su debilidad más aprovechable está en la ejecución SEO: ninguna de las 24 páginas de categoría tiene H1, 18 conservan el título automático con la palabra "archivos" y ninguna ficha publica datos estructurados Product.

## 2. Alcance del rastreo

| Indicador | Resultado |
|---|---|
| robots.txt | HTTP 200, sin `Crawl-delay`, declara `sitemap_index.xml` |
| Rutas omitidas por robots.txt | 0 |
| Solicitudes HTTP | 41 (robots.txt y 40 páginas) |
| Páginas con datos | 39: portada, 24 categorías y 14 fichas de producto |
| Redirecciones | 1 (301) |
| URL pendientes sin visitar | 127 |
| Bloqueos | Ninguno |

El cupo de 40 páginas se agotó en el catálogo. Por eso no se visitaron `/nosotros/`, `/servicios/`, `/blogs/`, `/contacto/` ni `/tienda/`, y solo se abrieron 14 de las 127 URL de producto enlazadas.

## 3. Rendimiento móvil

La API pública de PageSpeed respondió HTTP 429 con estado `RESOURCE_EXHAUSTED`, por agotamiento de la cuota diaria. El valor se registra como n/d y no se estimó con otra fuente.

Dato disponible del rastreo, que no reemplaza a PageSpeed: el HTML pesa 209 KB en la portada, 173 KB de media en categorías y 160 KB de media en fichas.

Inferencia: ese peso de HTML apunta a un constructor visual sobre WordPress y WooCommerce, por las rutas `/producto/`, `/categoria-producto/` y `/wp-content/`.

## 4. Catálogo y familias

Se observaron 126 nombres de producto y 127 URL de producto, una de ellas redirigida. Es un piso, porque quedaron sin visitar `/categoria-producto/mafusa/page/4/`, las páginas 2 y 3 de accesorios de hierro dúctil, `/categoria-producto/accesorios/` y `/categoria-producto/mafusa/tuberia-de-fundicion-ductil/`.

Inferencia: la agrupación siguiente se hizo por palabras clave del nombre y puede tener errores puntuales.

| Familia | Productos | Ejemplos |
|---|---|---|
| Accesorios HDPE | 42 | Termofusión, electrofusión, compresión, FM Approved |
| Tubería HDPE y mangueras | 7 | Contra incendio FM, corrugada SN2/SN4/SN8, gas, azul SEDAPAL |
| Máquinas y equipos de fusión o soldadura | 15 | Electrofusión, cuña caliente, extrusión |
| Válvulas de compuerta y cuchilla | 13 | Cierre elástico, bridada, guillotina, bronce |
| Válvulas de control | 11 | Serie VH, reductoras, anticipadora de onda |
| Válvulas de retención y check | 7 | Bola, sándwich, axial, swing, dúo check |
| Válvulas de mariposa | 5 | Wafer, lug, bi-excéntrica |
| Ventosas y válvulas de aire | 4 | Trifuncional, doble efecto |
| Otras válvulas y filtros | 9 | Globo, esférica, pinch, filtros Y y canasta |
| Contadores y medidores | 5 | Chorro único, chorro múltiple, Woltman |
| Accesorios de hierro dúctil y contra incendio | 5 | Acoples 995 y 997, yee y niple bridados |
| Tubería de hierro dúctil o acero | 2 | Fundición dúctil, acero al carbón |
| Otros | 1 | Tapones inflables |

Marcas visibles en categorías y nombres: Mafusa, Integrity, TecPipe, Asson, Fumansa, HAMLEM, Pengwang, Weldy, ROTHENBERGER, Hurner y ROTHENZEHN.

Cruce con las líneas de FUNDIGSAC:

| Línea | Presencia en Hi Perú |
|---|---|
| Válvulas compuerta, mariposa, check y aire | Alta. Es su competencia directa |
| Tubería de hierro dúctil | Una sola ficha, de DN80 a DN2000, clases K y C |
| Conexiones de hierro dúctil | Baja en la muestra; dos páginas de la categoría sin visitar |
| Marcos y tapas | No aparece. La única coincidencia es un repuesto de válvula |

## 5. Profundidad de especificaciones

De las 14 fichas visitadas:

| Indicador | Fichas |
|---|---|
| Con pares atributo-valor extraíbles | 2 |
| Con alguna norma citada | 6 |
| Con pestaña de descripción (H2 Descripción) | 8 |
| Con sección de valoraciones | 5 |

Las dos fichas más completas:

- Válvula de mariposa wafer con reductor, 9 atributos: presión de trabajo y de prueba, bridas PN10, PN16 y ANSI B16.5, temperatura de -20 a 100 ºC, normas de diseño y prueba, y materiales de cuerpo, eje SS416 y disco con nylon.
- Tubería HDPE contra incendio FM Approved, 5 atributos: PE100, ISO 4427 y ASTM F714, SDR 11, 9 y 7.4 con su PN, y diámetros de 90 a 630 mm.

Varias meta descripciones ofrecen la descarga de una ficha técnica, pero el rastreo no detectó ningún enlace a PDF de ficha. Los dos únicos PDF enlazados son un catálogo de proyectos y la política del sistema integrado de gestión.

Inferencia: parte de los datos técnicos podría estar en imágenes, porque las fichas enlazan archivos como `CURVA.png` o `CANASTILLA.png` junto a la foto del producto. Esos datos no son indexables como texto. El botón de descarga podría depender de JavaScript o de un destino externo que el rastreo no registra.

## 6. Normas y certificaciones citadas

| Norma o sello | Dónde aparece |
|---|---|
| ISO 9001 | Portada |
| EN 545, EN 598, ISO 2531, ISO 7186 | Tubería de fundición dúctil |
| EN 1074, EN 1074-1, EN 558, EN 1092-2, ISO 7005-2, DIN 30677 | Válvula de compuerta de cierre elástico con bridas |
| EN 593, EN 558:2008, EN 12266-1, EN 1092-2 | Válvula de mariposa bi-excéntrica |
| API 609, API 598, EN 10204, ANSI B16.5 | Válvulas de mariposa wafer |
| ISO 4427, ASTM F714 | Tubería HDPE contra incendio |
| FM Approved | Nombres de tubería y accesorios HDPE |
| Certificación SEDAPAL | Nombre de la tubería HDPE azul SN2/SN4 |

La captura "EN 12" aparece en la ficha de compuerta con bridas. Inferencia: es un fragmento de una norma escrita con espacios, como EN 12266, y no una norma independiente.

En las 39 páginas no aparecieron AWWA, NTP, EN 124 ni NSF/ANSI 61. Todas estas referencias son declaraciones comerciales que no se verificaron con certificados ni con SEDAPAL.

## 7. Palabras clave objetivo

Inferencia: la lista sale de títulos, H1, H2 y meta descripciones, y no de datos de posicionamiento real.

| Grupo | Términos probables |
|---|---|
| Marca y posicionamiento | Hi Perú, válvulas industriales, línea HDPE, especialistas en HDPE |
| HDPE | accesorios HDPE termofusión, electrofusión y compresión, tubería HDPE contra incendio FM Approved, tubería HDPE corrugada, tubería HDPE gas |
| Válvulas | válvula compuerta cierre elástico, válvula compuerta bridada hierro dúctil, válvula mariposa wafer, válvula bi-excéntrica, válvula guillotina, ventosa trifuncional, válvula reductora de presión |
| Hierro dúctil | tubería de fundición dúctil, acople contra incendio 995 y 997 |
| Máquinas | máquina de termofusión, máquina de electrofusión, soldadora de geomembrana |
| Marcas de terceros | Mafusa, Integrity, TecPipe, Asson, Fumansa, HAMLEM, ROTHENBERGER |
| Medición | contador Woltman, medidor de chorro único |

Los títulos siguen el patrón `Nombre del producto - Hi Perú`, sin DN, PN ni localidad. La palabra Lima no figura en ningún dato del rastreo. Usa "fundición dúctil" en la tubería, mientras que FUNDIGSAC y otros competidores usan "hierro dúctil".

## 8. Datos estructurados

| Tipo JSON-LD | Páginas de 39 |
|---|---|
| Organization, WebSite, SearchAction | 39 |
| BreadcrumbList, ImageObject | 39 |
| CollectionPage | 24 |
| WebPage, ReadAction | 15 |
| Product, Offer, AggregateRating, Review | 0 |
| LocalBusiness, FAQPage | 0 |

Organization expone el nombre, pero el rastreo no halló teléfono, correo ni dirección en ese nodo. Cinco fichas muestran valoraciones sin marcado AggregateRating.

Inferencia: el conjunto de tipos corresponde a la configuración por defecto de un complemento SEO de WordPress, sin integración de producto.

## 9. Enlazado interno

- Menú global en las 39 páginas: `/`, `/nosotros/`, `/tienda/`, `/servicios/`, `/blogs/` y `/contacto/`. La política del sistema de gestión también se enlaza desde las 39.
- Se detectaron 187 destinos internos únicos: 127 de producto, 34 de categoría, 20 archivos en `/wp-content/` y 6 páginas institucionales.
- Las categorías tienen 31 enlaces internos de media y las fichas, 15.
- Las 15 categorías principales aparecen en al menos 24 páginas.
- `/producto/tuberia-de-fundicion-ductil/` es la ficha más enlazada, con 26 enlaces. La siguiente tiene 6.
- El catálogo de proyectos en PDF solo se enlaza desde la portada.
- La portada enlaza a `/producto/tuberia-hdpe-fm-aproved/`, que redirige con 301 a la URL corregida.
- Las paginaciones enlazan versiones `/page/1/`, que duplican la primera página de la categoría.
- Cada ficha analizada enlaza a su categoría y a hasta cuatro productos relacionados.

Inferencia: la tubería de fundición dúctil figura como enlace fijo en la plantilla de categoría, lo que indica interés comercial en ese producto. Los productos relacionados parecen automáticos, porque mezclan familias distintas.

## 10. Llamadas a la acción

El rastreo no guarda el texto de los botones, así que esta sección se basa en metadatos y estructura de enlaces.

- Las meta descripciones de válvulas invitan a comprar o adquirir, y la de tubería contra incendio invita a cotizar stock.
- Las meta descripciones de accesorios prometen asesoría, capacitación, entrega nacional, stock permanente y ficha técnica.
- El menú global ofrece `/contacto/` y `/tienda/`.
- No se detectaron enlaces `tel:` ni correos genéricos `mailto:` en las 39 páginas, ni URL de carrito en los enlaces internos.

Inferencia: la conversión se apoya en contacto o cotización y posiblemente en WhatsApp, cuyo enlace externo el rastreo no registra. Queda por confirmar, igual que la publicación de precios.

## 11. Señales de SEO local

| Señal | Resultado |
|---|---|
| Dominio `.com.pe` y `lang="es"` | Sí |
| Mención de Perú en metadatos | Sí, sobre todo como distribuidor exclusivo en Perú |
| Entrega a nivel nacional | Sí, en meta descripciones |
| Referencia a SEDAPAL | Sí, en una línea de tubería HDPE |
| Lima u otras ciudades o regiones | No, en los 39 registros |
| LocalBusiness | No |
| Dirección o teléfono en datos estructurados | No |

La página `/contacto/` no se visitó, por lo que la existencia de dirección física o mapa queda sin determinar.

## 12. Experiencia de usuario

No se evaluó la interfaz en un navegador. Todo este apartado es inferencia a partir de HTML y metadatos.

Fortalezas:

- Taxonomía amplia que combina tecnología de unión, marca y tipo de válvula.
- URL legibles, canónicas coherentes en las 39 páginas y migas de pan en todas.
- Portada con accesos directos a categorías y productos destacados.
- Valoraciones visibles en algunas fichas y sello FM Approved como argumento de confianza.

Debilidades:

- Portada con un H1 dedicado a un solo producto, en lugar de la propuesta de la empresa.
- Categorías sin H1 y, en 18 de 24 casos, sin meta descripción.
- Clasificación confusa: Accesorios Hierro Dúctil contiene válvulas, y Válvulas Industriales contiene tubería de acero.
- Posicionamiento inconsistente: la portada dice fabricantes e importadores, y las fichas dicen distribuidor exclusivo.
- Errores de redacción como "FM APROVED", "SRD21" y "SDRll".
- Meta descripciones repetidas: tres fichas HDPE comparten texto, y la mariposa con reductor usa la descripción de la mariposa de eje centrado.
- Fichas desiguales: seis no tienen pestaña de descripción.
- Categorías de nueve productos por página, que alargan la navegación.

## 13. Oportunidades para FUNDIGSAC

**Advertencia:** las normas de FUNDIGSAC citadas en esta sección proceden de `Frontend/src/modules/catalog/data.ts`, cuya cabecera lo declara dataset de maqueta. No son datos verificados y no deben publicarse sin documento (informe, sección 10, V-12).

La prioridad es una inferencia basada en la brecha observada. Las referencias a FUNDIGSAC proceden de `Frontend/src/modules/catalog/data.ts` y de la página de producto del repositorio. Cada norma debe publicarse solo con respaldo documental.

| Prioridad | Oportunidad | Acción concreta |
|---|---|---|
| Alta | Marcos y tapas sin presencia en Hi Perú | Reforzar la categoría con D400, EN 124 y NTP 350.085 en título, H1 y texto |
| Alta | Normas peruanas y AWWA sin citar | Crear contenido indexable por norma, usando NTP 350.085, AWWA C530 y EN 1074 ya presentes en el catálogo |
| Alta | Tubería de hierro dúctil con ficha única | Publicar páginas por clase y rango de DN, y cubrir también el término "fundición dúctil" |
| Alta | Categorías sin H1 ni descripción | Dar a cada categoría H1, título con material y norma, y una introducción técnica propia |
| Media | Fichas sin datos estructurados | Mantener Product y añadir DN, PN y norma como propiedades, sin marcar precio ni valoraciones inexistentes |
| Media | Ficha técnica prometida y no detectada | Dar a cada producto datos en HTML y PDF enlazado de forma directa |
| Media | SEO local ausente | Publicar LocalBusiness con dirección y teléfono verificados, y páginas para Lima y regiones con obra pública |
| Media | Evidencia ante SEDAPAL | Publicar homologaciones o aprobaciones reales con documento consultable |
| Media | Sinónimos de válvula de aire | Unificar en una página los términos ventosa, válvula de aire, trifuncional y triple efecto |
| Baja | Proyectos solo en PDF | Publicar casos de obra en HTML, con cliente autorizado, diámetro y norma |

No se recomienda competir de frente en HDPE ni en máquinas de fusión, salvo decisión comercial expresa. Esas líneas suman la mitad del catálogo observado y no están entre las líneas del estudio de FUNDIGSAC.

## 14. Control de indicadores

| Indicador | Meta | Resultado | Estado |
|---|---|---|---|
| Cumplimiento de robots.txt | Sin rutas prohibidas | Leído antes de las páginas | Verde |
| Límite de páginas | Máximo 40 | 40 | Verde |
| Intervalo entre solicitudes | Mínimo 3 s | Configurado en 3 s; media de 3,97 s | Verde |
| Bloqueos o desafíos | Detener si ocurren | No ocurrieron | Verde |
| Datos personales en el JSON | Ninguno | 0 correos, 0 teléfonos, 0 nodos Person | Verde |
| PageSpeed móvil, rendimiento | Medido | n/d por cuota agotada | Sin medir |
| PageSpeed móvil, SEO | Medido | n/d por cuota agotada | Sin medir |

Los dos indicadores de PageSpeed no están en verde porque no se pudieron medir. Debe repetirse la consulta cuando la cuota se renueve o con una clave autorizada del proyecto.

## 15. Limitaciones

- La muestra cubre 39 páginas. Los resultados "no aparece" valen para esa muestra y no para todo el sitio.
- El rastreo usa HTTP simple, así que no ve contenido cargado por JavaScript.
- Los recuentos de H1 se refieren al HTML servido. Un H1 insertado por JavaScript no se contabiliza.
- Las normas y certificaciones son declaraciones del sitio y no se verificaron.
- No se pudo revisar el mapa del sitio, porque el cupo de 40 páginas ya estaba consumido.
