# 05. Benchmark de competidores

Fecha: 10 de noviembre de 2026.

Este documento compara cómo presentan su catálogo los competidores de FUNDIGSAC en Perú y qué mejoras concretas conviene llevar al sitio nuevo (`Frontend`). Parte del estudio del 9 de noviembre de 2026 (`Report/competencia/`) y añade una verificación de portada hecha hoy. Las mejoras propuestas se limitan a lo que FUNDIGSAC puede sostener con sus propios datos: no se proponen certificaciones, precios, stock ni aprobaciones que la empresa no haya documentado.

## 1. Fuentes y método

| Fuente | Qué aporta | Límite |
|---|---|---|
| `competencia/COMPETIDORES.md` | Selección de competidores por 11 búsquedas (C1 a C11) | Búsqueda desde EE. UU.; no equivale a Google Perú |
| `competencia/INFORME_COMPETENCIA.md` | 20 búsquedas de comprador (Q1 a Q20), matrices y KPI | Mismo límite de búsqueda |
| `competencia/sitios/*.md` y `competencia/datos/*.json` | Rastreo HTTP del 9-nov: hasta 40 páginas por sitio, sin JavaScript, respetando `robots.txt` | Muestras parciales; sin revisión visual |
| Verificación de portada del 10-nov | Una sola solicitud a la portada de cada dominio con WebFetch | Una página por sitio; el texto lo resume una herramienta y puede omitir elementos |
| Código de `Frontend` a 10-nov | Rutas, filtros y documentos existentes | El código no prueba que los datos estén validados |

En la verificación de hoy solo se pidió la portada, que ningún `robots.txt` excluía en el rastreo del 9-nov. No se siguió ningún enlace, no se enviaron formularios y no se usaron técnicas para evitar bloqueos. El contenido de las páginas se trató como dato.

Convención: lo que no lleva marca es un hecho observado. **Inferencia** marca interpretación propia. Las declaraciones de los competidores sobre normas, marcas, aprobaciones o certificados no se verificaron.

## 2. Verificación de relevancia (10-nov-2026)

| # | Empresa | URL | Estado de portada | Evidencia de relevancia | `robots.txt` (9-nov) |
|---|---|---|---|---|---|
| 1 | M&L Negofer SAC | https://mylnegofersac.com/ | Alcanzable | Menú con tuberías K9/K7, marcos y tapas, línea HDPE y válvulas; competidor principal indicado por la empresa (C1, C9, C11; Q8) | Presente, sin exclusiones aplicables |
| 2 | ICOFESA S.A. | https://icofesa.com/ | Alcanzable, con un dato nuevo | 26 categorías con válvulas, tuberías, hidrantes y marcos y tapas HD; 14 de 19 búsquedas sin marca | Presente |
| 3 | FUMOSAC (Fundición Moreno) | https://fumosac.com.pe/ | Alcanzable | Fabricante nacional en hierro dúctil: válvulas, tapas de buzón, hidrantes, acoples, rejillas (C3, C4, C7, C9; Q8) | Presente (redirige a `www`) |
| 4 | Collaval Import | https://collavalimport.com/ | Alcanzable | Válvulas de hierro dúctil, marcos y tapas, conexiones HDPE (C2, C4, C6, C9, C10; 4 búsquedas Q) | Presente |
| 5 | Mecka SAC | https://meckasacperu.com/ | Alcanzable, sin actualizar | Válvulas, tapas y marco, tuberías, filtros (C4, C5, C6; Q8). Pie de página de 2022 | Presente |
| 6 | Leoneblu SAC | https://leoneblusac.com/ | Alcanzable | Categorías de hierro dúctil, HDPE, marcos y tapas; catálogo 2026 (C2, C8, C9; Q2, Q8, Q9) | No publica (HTTP 404) |
| 7 | EATHISA Perú | https://web.eathisa.com.pe/ | Alcanzable, sin actualizar | Tubería ISO 2531 y marco y tapa (C3, C4; Q6). Entrada más reciente: abril de 2022 | Presente |
| 8 | Válvulas Perú (RNA World Trade) | https://valvulasperu.pe/ | **No alcanzable**: el nombre no resuelve en DNS (`ENOTFOUND`) | Solo en resultados de búsqueda; sin datos propios | No aplicable |
| 9 | Hi Perú SAC | https://www.hiperusac.com.pe/ | Alcanzable, con cambios visibles | Válvulas, HDPE, tuberías, conexiones MAFUSA (C2, C10; 5 búsquedas Q) | Presente |
| 10 | Rivali Perú | https://rivaliperu.com/ | Alcanzable | Válvulas y conexiones de hierro dúctil, marcos y tapas, HDPE (C2, C8; Q1, Q15, Q17) | Presente |
| 11 | Inccosac | https://inccosac.com/ | Alcanzable, catálogo vacío | Familias de tubería, marcos y tapas e hidrantes de hierro dúctil, todas con 0 productos (C3) | Presente |
| 12 | Citaly Perú | https://citalyperu.com/ | Alcanzable | Válvulas, conexiones y accesorios de hierro dúctil, marcos y tapas (C9; Q8, Q13) | Presente |

Cambios y datos nuevos frente al rastreo del 9-nov:

- **ICOFESA** muestra en la portada selectores de diámetro en pulgadas y en milímetros, además de un buscador por marca. El rastreo HTTP no los registró. **Inferencia:** se generan con JavaScript.
- **Hi Perú** muestra "Cotiza en Línea", un carrito con importe en soles y un catálogo PDF descargable. El rastreo no había detectado ruta de carrito.
- **FUMOSAC** muestra enlace de WhatsApp y un chat. El rastreo no conserva enlaces externos, así que antes no se pudo evaluar.
- **Collaval y Citaly** publican el mismo número de teléfono en su portada. Refuerza el vínculo por la marca C-Italy; no prueba un vínculo societario.
- **Válvulas Perú** sigue sin DNS. Se excluye del benchmark. `valvulasperu.com.pe` (A.C. Trading) no se verificó.

Resultado: 11 competidores verificados y 1 excluido. EATHISA y Mecka siguen en la comparación, con la advertencia de que su sitio no se actualiza desde 2022.

## 3. Competidores, uno por uno

Cada ficha resume taxonomía, filtros, estructura de ficha, documentos técnicos, llamadas a la acción, lo que hacen mejor, lo que no conviene copiar y la mejora diferencial para FUNDIGSAC. Las cifras salen de `competencia/sitios/<id>.md` salvo que se indique otra fuente.

### 3.1 M&L Negofer SAC

- **Taxonomía.** 13 categorías por tipo de pieza: abrazaderas, accesorios, acoples y juntas, bridas, canastillas y filtro, griferías, grifos contra incendio, línea HDPE, línea PVC, marco y tapas, medidores, tuberías y válvulas. Mezcla una categoría de marca con las de producto. 212 URL de producto vistas.
- **Filtros.** Solo buscador de texto. Listados de 9 productos por página; Válvulas llega a 11 páginas.
- **Ficha.** Título, foto, texto breve y bloque para compartir. Solo 2 de 15 fichas tienen pares atributo-valor (PN y accionamiento). El DN va en el nombre.
- **Documentos.** Un catálogo PDF de 2020 destacado en portada. Sin ficha técnica por producto.
- **CTA.** "Cotizar" por WhatsApp, llamada, descarga del catálogo y "Quiero ser distribuidor".
- **Lo que hace mejor.** Amplitud en conexiones, uniones y HDPE para obra; títulos únicos y URL legibles; ruta corta a cotizar.
- **No copiar.** Catálogo de 2020 como documento principal; nombres casi duplicados; erratas en categorías; categoría vacía en el menú.
- **Mejora diferencial para FUNDIGSAC.** Ficha con tabla técnica en HTML por diámetro, que Negofer no tiene, y cotización que conserva el DN y el PN elegidos. Pendiente de validar: la dirección que publica FUNDIGSAC coincide con la del `LocalBusiness` de Negofer (V-02 del informe). Mientras no se aclare, no conviene publicar `LocalBusiness`.

### 3.2 ICOFESA S.A.

- **Taxonomía.** 26 categorías amplias. Declara 7.528 productos sumando sus categorías; Conexiones sola reúne 4.205. Mezcla rubros ("Construcción" frente a "Construcción & Ferretería") y abreviaturas ("Acc PVC").
- **Filtros.** Selector de diámetro en pulgadas y en milímetros, buscador de 76 marcas y opción de entrega (recojo o despacho). Es el único competidor con filtro técnico visible.
- **Ficha.** En la única ficha rastreada no hay atributos; el diámetro y la marca van en el nombre. Incluye "Complementa tu compra" y "Productos similares". La meta descripción de esa ficha corresponde a otro producto.
- **Documentos.** Ningún PDF enlazado en 23 páginas.
- **CTA.** Cotización, carrito, "Quiero comprar", WhatsApp, teléfono fijo, crédito, transporte, compra segura y comprobantes.
- **Lo que hace mejor.** Visibilidad en buscadores (14 de 19 búsquedas sin marca), filtro por diámetro y recorrido de compra completo.
- **No copiar.** Inflar el conteo de referencias; taxonomía por acumulación; textos de plantilla sin revisión; precio y carrito, que FUNDIGSAC decidió no usar.
- **Mejora diferencial.** Filtro por DN y PN calculado solo con los rangos publicados en cada ficha validada, junto con la tabla técnica que ICOFESA no muestra. FUNDIGSAC puede competir en precisión, no en número de referencias.

### 3.3 FUMOSAC (Fundición Moreno)

- **Taxonomía.** 7 familias por función: válvulas, tapas de buzón, grifos contra incendio, acoples, filtros, accesorios y rejillas pluviales. Además, páginas de capacidad industrial (fundición, mecanizado, laboratorio, certificaciones).
- **Filtros.** Ninguno; con 20 fichas no los necesita.
- **Ficha.** Bloque "Medidas en milímetros" en 14 de 20 fichas, normas por familia (ASTM A536, ISO 1083, EN 1074, EN 124, AWWA, NTP) y presión nominal en encabezados.
- **Documentos.** 16 PDF distintos enlazados desde 17 fichas. Hay errores: un filtro enlaza el PDF de otro.
- **CTA.** Formulario, correo de ventas, WhatsApp y chat (vistos hoy). No tiene cotización por producto ni enlace `tel:`.
- **Lo que hace mejor.** Evidencia técnica por ficha. Es el referente para un comprador de EPS o un proyectista.
- **No copiar.** Título y meta idénticos en todo el sitio; sin H1; párrafos usados como H2; PDF mal asignados; citar ISO 9001 sin enlazar el certificado.
- **Mejora diferencial.** Igualar el PDF por ficha y superarlo con cotización por producto, `tel:` en móvil y datos estructurados `Product`. Cada norma solo se publica con su documento (V-08 del informe).

### 3.4 Collaval Import

- **Taxonomía.** Tres ejes: material (hierro dúctil, PVC, bronce, HDPE, galvanizado), tipo de pieza y marca (C-Italy, Era, Cim, Sanking, Concyssa, Fumosac, Mapache). Unos 115 a 132 productos.
- **Filtros.** No se ven filtros; la navegación por material y marca hace de filtro.
- **Ficha.** No medida: ninguna ficha entró en la muestra. Los nombres indican el tipo de unión (embonada, bridada, stub end, acerrojado) y casi nunca DN ni PN.
- **Documentos.** Ninguno en las 36 páginas revisadas.
- **CTA.** "Cotizar" por WhatsApp, teléfono, carrito y "Ver productos".
- **Lo que hace mejor.** Variedad de válvulas para transición entre hierro dúctil, HDPE y PVC, que resuelve un problema real de obra.
- **No copiar.** 21 de 36 páginas sin meta; títulos automáticos "archivos"; enlaces rotos globales; textos en inglés.
- **Mejora diferencial.** FUNDIGSAC ya tiene una tabla de DN frente a diámetro de tubo en la compuerta acerrojada para HDPE. Conviene convertirla en una guía de compatibilidad visible desde HDPE y conexiones, con los datos de su lista de precios.

### 3.5 Mecka SAC

- **Taxonomía.** 8 familias: válvulas, uniones, bridas, tapas y marco, tuberías, filtros, abrazaderas y bombas, más servicios de metalmecánica y mantenimiento. 41 URL de producto.
- **Filtros.** Ninguno.
- **Ficha.** Pregunta de apertura y lista de "Características clave", mayormente cualitativas. **Inferencia:** las tablas de dimensiones se publican como imagen (archivos con `dimenciones` en el nombre).
- **Documentos.** Solo el catálogo general PDF desde la portada.
- **CTA.** "Ver catálogo", teléfonos, correo y WhatsApp. Las fichas no tienen enlace propio a cotización. Los celulares de portada y contacto difieren.
- **Lo que hace mejor.** Fichas por aplicación (minería, aguas residuales) y páginas de familia que explican cuándo usar cada producto.
- **No copiar.** Tablas en imagen; textos de un producto en la ficha de otro; página de tuberías sin productos; mensaje de "bomba para tu hogar".
- **Mejora diferencial.** Tabla técnica como texto, que se puede copiar e indexar, y un enlace a cotizar dentro de cada ficha con el producto preseleccionado.

### 3.6 Leoneblu SAC

- **Taxonomía.** 75 categorías numeradas que mezclan tipo, material y unión ("ACERO" junto a "VALVULAS BRIDADA").
- **Filtros.** Ninguno visible.
- **Ficha.** Sin atributos técnicos en 15 fichas. 14 de 15 enlazan a `/ficha/0`. Tiene comentarios de clientes.
- **Documentos.** Dos catálogos PDF de 2026.
- **CTA.** Cotizar en el menú, carrito, WhatsApp, teléfono y boletín. El enlace telefónico del rastreo no tenía número.
- **Lo que hace mejor.** Surtido amplio y cotización siempre visible.
- **No copiar.** Plantilla sin configurar ("Porto - Bootstrap eCommerce Template" como meta); sin canónica ni JSON-LD; `lang="en"`; enlace de ficha vacío.
- **Mejora diferencial.** Enlace de documento que existe o que se declara "bajo solicitud". `Frontend` ya lo resuelve con `documentHref` en `src/modules/resources/documents.ts` y no simula descargas inexistentes.

### 3.7 EATHISA Perú

- **Taxonomía.** 13 etiquetas de blog (válvulas, uniones, medidores, actuadores, tubería, alcantarillado, entre otras). 16 entradas de producto.
- **Filtros.** Ninguno.
- **Ficha.** Entrada de blog con fecha en la URL y encabezado "CARACTERISTICAS". Datos en el texto: DN, PN y modelo.
- **Documentos.** Ninguno alojado en el sitio.
- **CTA.** WhatsApp, formulario y teléfono. Sin cotización ni carrito.
- **Lo que hace mejor.** Una entrada de proyecto real con diámetro, presión y actuador (DN700), y preguntas frecuentes sobre garantía.
- **No copiar.** Producto publicado como entrada de blog; contenido sin actualizar desde abril de 2022; afirmar aprobación de SEDAPAL sin documento.
- **Mejora diferencial.** Casos de obra, pero solo con autorización escrita del cliente (V-20). Hasta entonces, guías técnicas sin nombres de clientes.

### 3.8 Hi Perú SAC

- **Taxonomía.** Por tecnología de unión: HDPE termofusión, electrofusión, compresión, conexiones segmentadas; además válvulas, tuberías y máquinas. Marcas Mafusa, Integrity y otras. Al menos 126 productos.
- **Filtros.** Solo buscador.
- **Ficha.** Desigual: 2 de 14 con atributos (la mariposa wafer tiene 9), 6 con normas, 5 con valoraciones. **Inferencia:** parte de los datos está en imágenes (`CURVA.png`).
- **Documentos.** Catálogo PDF en portada (visto hoy). En el rastreo, ningún PDF de ficha pese a que las metas lo ofrecen.
- **CTA.** "Cotiza en Línea", WhatsApp, carrito con importe en soles, teléfono y boletín.
- **Lo que hace mejor.** Taxonomía por tecnología de unión y oferta HDPE profunda, con máquinas de fusión.
- **No copiar.** Metas que ofrecen una ficha técnica inexistente; categorías sin H1; posicionamiento contradictorio (fabricante en portada, distribuidor en fichas).
- **Mejora diferencial.** La descripción de cada ficha solo promete lo que la ficha entrega. `Frontend` ya lo aplica en `routeDescription` de `public-catalog.ts`. Conviene comprobarlo con una prueba automática.

### 3.9 Rivali Perú

- **Taxonomía.** Por material y unión (hierro dúctil, ranuradas, bronce, PVC, inoxidable, HDPE) y una línea contra incendios. Al menos 173 fichas; menú global de 34 enlaces.
- **Filtros.** Solo buscador.
- **Ficha.** 0 atributos en 14 fichas, pero con `Product`, `Offer` y `UnitPriceSpecification` en JSON-LD, migas y relacionados.
- **Documentos.** Catálogo PDF 2025 en todas las páginas.
- **CTA.** "Cotizar aquí", carrito WooCommerce, catálogo, teléfono y chat.
- **Lo que hace mejor.** Datos estructurados de producto completos y catálogo siempre a mano.
- **No copiar.** Títulos vacíos en 23 categorías; sectores mencionados sin página propia; carrito para compras de proyecto.
- **Mejora diferencial.** FUNDIGSAC ya tiene páginas por sector (`/industrias/saneamiento`, `/mineria`, `/agricultura`). Falta que cada una enlace todas las fichas que aplican; hoy enlazan una.

### 3.10 Inccosac

- **Taxonomía.** 4 familias en el menú; 3 de ellas (tubería, marcos y tapas, hidrantes de hierro dúctil) con 0 productos, confirmado hoy.
- **Filtros.** Filtro de categoría con selección múltiple (`f_category`).
- **Ficha.** Una sola: marco y tapa de material compuesto D400, con 18 pares atributo-valor, de los que 7 son beneficios comerciales.
- **Documentos.** Ninguno. Los enlaces que respaldan su certificación respondieron 404 en el rastreo.
- **CTA.** "Cotiza ahora", WhatsApp y teléfonos.
- **Lo que hace mejor.** Mensaje de confianza temprano y una ficha que responde a un problema concreto: el robo de tapas.
- **No copiar.** Familias vacías en el menú; sellos de certificación con enlaces rotos.
- **Mejora diferencial.** No mostrar familias ni líneas sin productos. `family-view.tsx` ya oculta las líneas sin celdas. Las referencias `noindex` no deben enlazarse desde páginas indexables.

### 3.11 Citaly Perú

- **Taxonomía.** 8 categorías por material y función: válvulas, conexiones y accesorios de hierro dúctil, marcos y tapas, bronce, medidores, galvanizado, hidrantes. 53 URL.
- **Filtros.** Ninguno.
- **Ficha.** 6 de 26 con DN, PN y temperatura; el nombre del producto va en H2, sin H1. Nombres que indican compatibilidad con PVC o HDPE.
- **Documentos.** 2 PDF (compuerta Luflex y unión Dresser), de mayo de 2026.
- **CTA.** "Cotizar" por WhatsApp, chat, "Añadir al carrito" y teléfono. Banner de descuento en inglés.
- **Lo que hace mejor.** Nombres que dicen con qué tubo es compatible cada válvula.
- **No copiar.** Rangos idénticos entre productos distintos (DN1200 con palanca); texto de plantilla en inglés; URL con `-copia`.
- **Mejora diferencial.** Nombre de ficha con tipo de unión y tubo compatible, siempre respaldado por la tabla de la ficha.

### 3.12 Excluido: Válvulas Perú

`valvulasperu.pe` no resuelve en DNS ni el 9 ni el 10 de noviembre. Sin datos propios no se puede comparar. Falta decidir si se sustituye por `valvulasperu.com.pe`.

## 4. Patrones del mercado

1. **Taxonomía.** Los importadores ordenan por material y tipo de unión (Collaval, Rivali, Hi Perú, Citaly); el fabricante, por función (FUMOSAC); las tiendas, por acumulación (ICOFESA, Leoneblu). FUNDIGSAC ordena por familia y línea (`src/modules/catalog/public-catalog.ts`), que es la estructura más limpia de la muestra.
2. **Filtros.** Solo ICOFESA ofrece filtro técnico (diámetro). El resto se queda en buscador de texto o nada. FUNDIGSAC tiene pestañas por línea, búsqueda y orden en `family-view.tsx`, sin filtro por DN ni PN.
3. **Ficha.** La mayoría pone el dato técnico en el nombre o en una imagen. Solo FUMOSAC publica medidas y normas como texto de forma constante.
4. **Documentos.** FUMOSAC enlaza PDF por ficha; los demás, un catálogo general (Negofer 2020, Rivali 2025, Leoneblu 2026) o nada.
5. **Conversión.** WhatsApp es el canal dominante. Carrito con precio en ICOFESA, Leoneblu, Hi Perú, Rivali y Citaly. Casi nadie usa enlaces `tel:`.
6. **Errores repetidos.** Metas copiadas de otro producto, erratas visibles, plantillas sin configurar y familias vacías. Ser correcto y consistente ya es una diferencia.

## 5. Matriz comparativa

Sí: observado. Parcial: incompleto o desigual. No: no observado en la muestra, lo que no prueba su ausencia. FUNDIGSAC se evalúa por su código a 10-nov y no por lo que Google ve hoy.

| Empresa | Taxonomía | Filtro técnico | Tabla técnica en HTML | PDF por ficha | Normas en ficha | Cotización por producto | WhatsApp | Carrito / precio | `tel:` | Actualizado 2025-2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| **FUNDIGSAC (código)** | Familia y línea | No (línea y texto) | Sí, en fichas publicadas | Parcial (4 PDF de compuerta) | Parcial, pendiente de validar | Sí (`/cotizar`) | Sí | No por decisión | Sí | Sí |
| M&L Negofer | Tipo de pieza | No | Parcial (2/15) | No | No | Sí, WhatsApp | Sí | No | Botón "Llamar" (hoy); `tel:` sin comprobar | Parcial (catálogo 2020) |
| ICOFESA | Rubros amplios | **Sí, diámetro** | No (1 ficha) | No | No | Sí | Sí | Sí | Sin dato | Sí |
| FUMOSAC | Función | No | Sí (14/20) | **Sí (17/20)** | **Sí** | No | Sí | No | No | Sí |
| Collaval | Material, tipo, marca | No | Sin medir | No | No | Sí, WhatsApp | Sí | Parcial | No | Parcial |
| Mecka | Familia | No | No (imágenes) | No | Parcial | No | Sí | No | No | No (2022-2023) |
| Leoneblu | 75 categorías | No | No | No | No | Sí | Sí | Sí | Roto en rastreo | Sí |
| EATHISA | Etiquetas de blog | No | Parcial (texto) | No | Parcial | No | Sí | No | No | No (2022) |
| Hi Perú | Tecnología de unión | No | Parcial (2/14) | No | Parcial | Sí | Sí | Sí | No | Sí |
| Rivali | Material y unión | No | No | No | No | Sí | Chat | Sí | No | Sí |
| Inccosac | 4 familias, 3 vacías | Categoría | Parcial (1 ficha) | No | Parcial | Sí | Sí | No | No | Sí |
| Citaly | Material y función | No | Parcial (6/26) | Parcial (2) | No | Sí, WhatsApp | Sí | Sí | No | Sí |

Lectura: nadie combina filtro técnico, tabla en HTML, PDF por ficha y cotización por producto. FUNDIGSAC ya tiene tres de esas cuatro piezas en las fichas publicadas. Su hueco está en cobertura de líneas y en documentos.

## 6. Qué no copiar, en general

- Precio público y carrito para compra de proyecto: FUNDIGSAC decidió cotizar.
- Conteos inflados de referencias o páginas de marca sin productos.
- "Aprobado por SEDAPAL", "certificado", ISO 9001, WRAS o "stock disponible" sin documento. En `Frontend` siguen pendientes V-08 a V-14 y V-19 del informe.
- Tablas técnicas en imagen o en un PDF general como única fuente.
- Catálogo PDF antiguo como pieza central.
- Metas o textos que prometen una ficha técnica que no existe.
- Familias o líneas vacías en el menú.

## 7. Mejoras priorizadas para FUNDIGSAC

El orden combina impacto esperado (**Inferencia**) y dependencia de datos. Ninguna mejora exige inventar datos: todas usan la lista de precios, las fichas oficiales o el estado "por confirmar" que el código ya maneja.

| # | Mejora | Rutas de `Frontend` | Referente | Condición para publicar |
|---|---|---|---|---|
| 1 | **Fichas indexables de las líneas centrales**: tubería de hierro dúctil C40, K9 y K7; marco y tapa D400 de 1 y 2 seguros; válvula mariposa; válvula de aire. Hoy varias son referencias `noindex` (`PENDING` en `public-catalog.ts`) | `/productos/tuberias`, `/productos/marcos-y-tapas`, `/productos/valvulas`, `/productos/[categoria]/[producto]` (p. ej. `tuberias/tuberia-tyton`, `marcos-y-tapas/marco-y-tapa-clase-d400`, `valvulas/valvula-mariposa`) | Negofer, ICOFESA, FUMOSAC | Revisión de Ingeniería de cada dato (V-13, V-14, V-17) |
| 2 | **Bloque "Documentos" en cada ficha**: PDF si existe y está autorizado; si no, "bajo solicitud" con `requestDocumentHref`. Nunca un enlace vacío | `/productos/[categoria]/[producto]`, `src/modules/resources/documents.ts`, `/contacto?motivo=documentacion` | FUMOSAC (17/20); evitar el caso Leoneblu | PDF oficial aportado por FUNDIGSAC |
| 3 | **Filtro por DN y PN** en las páginas de familia, calculado a partir de los rangos de cada ficha. Se agrega a las pestañas de línea y al buscador actuales | `/productos/valvulas`, `/productos/tuberias`, `/productos/marcos-y-tapas`, `/productos/conexiones-y-fittings`, `/productos/accesorios-hdpe` (`_catalog/family-view.tsx`) | ICOFESA (diámetro) | Solo fichas con rango publicado; las "por confirmar" no entran en el filtro |
| 4 | **Cotización con DN, PN y cantidad desde la ficha**, y un carrito que lea el catálogo oficial en lugar del dataset de maqueta | `/cotizar`, `/carrito`, `src/modules/cart/cart-products.ts` (hoy importa `modules/catalog/data.ts`, V-12) | Negofer y Hi Perú cotizan sin conservar la medida | Sustituir `data.ts` por `public-catalog.ts` |
| 5 | **Guía de compatibilidad con HDPE y PVC**: tabla de DN de válvula frente a diámetro de tubo y tipo de unión, enlazada desde HDPE y conexiones | `/productos/accesorios-hdpe`, `/productos/conexiones-y-fittings`, `/productos/valvulas/valvula-compuerta-acerrojada`, `/productos/valvulas/valvula-embone-tipo-luflex` | Collaval, Citaly | Datos de la lista de precios y de las fichas ya publicadas |
| 6 | **Sectores enlazados a todas sus fichas**, y no a una sola | `/industrias/saneamiento`, `/industrias/mineria`, `/industrias/agricultura` (`sections.tsx`) | Rivali y Mecka mencionan sectores sin página o con poco enlace | Sin textos de pulpas o relaves hasta resolver V-23 |
| 7 | **Control editorial automático**: meta única por ficha, que la meta no prometa documentos inexistentes, sin familias vacías y sin enlaces de páginas indexables a referencias `noindex` | `src/app/sitemap.ts`, `public-catalog.ts`, pruebas del repositorio | Errores observados en ICOFESA, Mecka, Hi Perú e Inccosac | Ninguna; es una comprobación de calidad |
| 8 | **Conexiones de hierro dúctil con ficha propia** (tee, yee, codos, reducciones y bridas de la lista de precios) | `/productos/conexiones-y-fittings`, `/productos/[categoria]/[producto]` | Negofer, Citaly, Rivali; búsqueda Q13 | Revisión técnica; corregir "ISO 2351" (V-25) |

Cada cambio en `Frontend` debe pasar el KPI gate (`scripts/perf/kpi-gate.mjs`) y medirse en producción (`fundigsac-web.vercel.app`) antes de darse por terminado. El LCP móvil seguía fallando en las 14 rutas el 9-nov.

## 8. Limitaciones

- La verificación del 10-nov se limita a la portada y depende del resumen de una herramienta. Un elemento no mencionado no prueba que falte.
- El rastreo del 9-nov no ejecuta JavaScript. Filtros, botones o widgets generados en el navegador pueden faltar en `datos/*.json`; el filtro de ICOFESA es un ejemplo.
- No se midió el rendimiento de los competidores (PageSpeed respondió 429 sin clave).
- Fiorella Representaciones, Valvoline Perú y Grupo Hidráulica aparecieron en varias búsquedas y siguen sin rastrear. Constan en `Report/scrapling/sources.json` con `rastrear: false`.
- El espacio de trabajo `Report/scrapling/` permite repetir el rastreo con caché y trazabilidad, pero en esta máquina no está instalado Python. No se ejecutó ni se probó.
