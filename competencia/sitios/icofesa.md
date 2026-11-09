# ICOFESA S.A.

| Campo | Valor |
|---|---|
| Sitio | https://icofesa.com/ |
| Segmento | Distribuidor nacional |
| Fecha de la revisión | 9 de noviembre de 2026 |
| Estado del rastreo | ok, con cobertura parcial |
| Páginas solicitadas | 40 de 40 permitidas (41 solicitudes HTTP con robots.txt) |
| Páginas con datos | 23 (17 respuestas fueron redirecciones 302) |
| PageSpeed móvil | n/d (cuota de la API agotada) |
| Datos en bruto | `Report/competencia/datos/icofesa.json` |

## Resumen

ICOFESA es un distribuidor generalista con tienda propia: 25 categorías y al menos 7.528 productos declarados en 18 de ellas. Su fuerza está en la amplitud del catálogo y en las facilidades de compra, como cotización en línea, carrito, crédito y transporte. En los datos obtenidos su debilidad es el contenido técnico: no se detectó ninguna norma ni especificación estructurada, y los títulos de categoría son una sola palabra. Las conclusiones sobre fichas se apoyan en una sola ficha rastreada, por lo que son provisionales.

## Límites de esta revisión

Estos límites condicionan todo el informe:

- **Categorías clave sin visitar.** El tope de 40 páginas se agotó antes de llegar a `valvulas-166`, `tuberias-167`, `tuberia-pvc-179`, `saneamiento-187`, `rejilla-186` y `pernos-tuercas-176`. Las dos primeras son las más cercanas a FUNDIGSAC. No se hizo un segundo rastreo porque superaría el máximo de 40 páginas por sitio.
- **Solo una ficha de producto.** Se rastreó `valvula-reductora-de-presion-hierro-ductil-100mm-bermad-15136`. Una ficha no representa todo el catálogo.
- **17 solicitudes sin datos.** Fueron URL del tipo `/producto/categoria/...`, que respondieron 302.
- **Páginas institucionales sin visitar.** Quedaron fuera `/nosotros.php`, `/servicios.php`, `/catalogos.php` y `/contacto.php`. Si las normas o certificaciones figuran allí o en catálogos descargables, este informe no las refleja.
- **Solo HTML inicial.** El rastreo no ejecuta JavaScript. Lo que se cargue después en el navegador no aparece en los datos.
- **Enlaces de portada truncados.** Se guardaron 80 de los 252 enlaces internos de la portada.
- **Búsquedas no ejecutadas.** Los enlaces `vertodos.php?q=...` se registraron, pero no se solicitaron, conforme a las reglas del estudio.

El robots.txt respondió 200, sin demora de rastreo y con `sitemap.xml` declarado. Ninguna ruta se omitió por robots.txt. No hubo bloqueo, captcha ni desafío.

## PageSpeed móvil

La API pública respondió HTTP 429 (`RESOURCE_EXHAUSTED`, cuota diaria con límite 0). Se hizo una sola llamada y se registra **n/d** tanto en rendimiento como en SEO. Queda como dato indirecto el peso del HTML: 428.825 bytes en la portada, unos 108.000 en categorías y 139.194 en la ficha.

## Cobertura de catálogo y familias

Se identificaron 25 categorías enlazadas desde la portada. La tabla recoge las cifras que el propio sitio publica en la meta descripción de cada categoría visitada.

| Categoría | Productos declarados |
|---|---:|
| Conexiones | 4.205 |
| Industrial | 1.257 |
| Abrazaderas | 356 |
| Construcción y ferretería | 320 |
| Gasfitería | 281 |
| Juntas | 231 |
| Mangueras | 214 |
| Marcos y tapas | 186 |
| Medidores | 120 |
| Manómetro | 104 |
| Bomberil | 103 |
| Hidráulico | 58 |
| Accesorios de PVC | 41 |
| Limpieza y mantenimiento | 19 |
| Accesorios de bronce | 16 |
| Equipos | 7 |
| Hidrantes | 7 |
| Construcción | 3 |
| EPP y ropa industrial | sin cifra publicada |
| Válvulas, tuberías, tubería PVC, saneamiento, rejilla, pernos y tuercas | no visitadas |

La suma de las 18 cifras es 7.528. Inferencia: el total real de referencias únicas puede ser distinto, porque un producto podría estar en más de una categoría y faltan seis categorías por contar.

Marcas leídas en los slugs de producto: BERMAD, CLAVAL, VALVE ITALY, ATLANTIC USA, FUMOSAC, PLUSCHLOR, PANTERA, AYRON e IQSACHLOR. La portada afirma suministrar directamente productos de las mejores marcas.

Otras líneas visibles en la portada: productos para limpieza de alcantarillado, equipos para pruebas hidráulicas y de estanqueidad, sistemas de cloración y línea contra incendio. Los enlaces de portada mencionan además compuertas bridadas y acerrojadas, geomembrana, water stop, juntas espirometálicas y mangueras HDPE.

Según `COMPETIDORES.md`, ICOFESA vende válvulas compuerta PN16, válvulas de aire y tubería K9, con precios en soles. Este rastreo no volvió a comprobar esos productos concretos.

Inferencia: ICOFESA compite por amplitud y por la compra conjunta de una obra. No se presenta como especialista en hierro dúctil, aunque su portada use ese término como reclamo principal.

## Profundidad de especificaciones

- Ficha rastreada: 0 pares atributo-valor detectados en tablas o listas.
- El diámetro y la marca aparecen en el nombre del producto y en el slug (100 mm, BERMAD).
- La ficha incluye los bloques `Complementa tu compra` y `Productos similares`.
- La meta descripción de esa ficha no corresponde al producto: describe una válvula de control de nivel en la página de una válvula reductora de presión.
- No se encontraron enlaces a documentos PDF, DOC, XLS o DWG en las 23 páginas.

Inferencia, con una sola ficha como base: la información técnica publicada es escasa o no está en el HTML inicial. Conviene confirmarlo con más fichas antes de usarlo como argumento comercial.

## Normas y certificaciones citadas

No se detectó ninguna norma (ISO, NTP, EN, AWWA, ASTM, NSF, BS, DIN, API) en las 23 páginas con datos, y tampoco certificaciones. La limitación es relevante, porque solo se vio una ficha y no se visitaron las páginas institucionales.

## Palabras clave inferidas

Todo este apartado es inferencia a partir de títulos, encabezados y slugs.

| Nivel | Términos objetivo probables |
|---|---|
| Portada | tuberías de hierro dúctil Lima, válvulas de hierro dúctil Lima, accesorios de hierro dúctil Perú, marcos y tapas de hierro dúctil, distribuidores en Lima, envíos a todo el Perú |
| Sectores (H2 de portada) | saneamiento, construcción, minería, línea contra incendio |
| Categorías | Un solo término genérico en el título: abrazaderas, conexiones, juntas, medidores, marcos y tapas |
| Fichas | Cola larga por producto, diámetro y marca: válvula reductora de presión hierro dúctil 100 mm Bermad |

Títulos observados: portada `ICOFESA S.A. | Tuberías y válvulas de hierro dúctil en Lima`; categorías con el patrón `NOMBRE | ICOFESA S.A.`; ficha con el patrón `NOMBRE DEL PRODUCTO | ICOFESA S.A.`.

La portada concentra la intención geográfica. Los títulos de categoría no incluyen material, uso ni ubicación. Las meta descripciones de categoría siguen una plantilla automática que produce formas como `Acc Pvc` o `Epp & Ropa Industrial`. Los nombres van en mayúsculas y sin tildes.

`COMPETIDORES.md` registra que ICOFESA aparece en 7 de las 11 búsquedas realizadas (C1, C2, C3, C4, C7, C8 y C10). No se anotaron posiciones. Inferencia: su visibilidad se apoya más en el volumen de fichas indexables que en la optimización de sus categorías.

## Marcado de esquema (JSON-LD)

| Página | Tipos detectados |
|---|---|
| Portada | Organization, Store, PostalAddress, Country |
| Ficha de producto | Product, Brand, Offer, Organization |
| Categorías, listados | Ninguno |

No se detectó BreadcrumbList, ItemList, CollectionPage, FAQPage ni WebSite. La presencia de Offer es coherente con la publicación de precios. Las etiquetas canónicas existen en portada, categorías y ficha, pero faltan en `categorias.php?cat=0` y `vertodos.php`. Esta última tampoco tiene H1.

## Enlazado interno

- Portada: 252 enlaces internos. Se accede a las 25 categorías y a selecciones por uso, como cloración o pruebas hidráulicas.
- Categorías: 52 enlaces internos, casi todos de navegación global. **Ninguna categoría visitada contiene enlaces a fichas en el HTML inicial**, pese a declarar hasta 4.205 productos.
- Ficha: 61 enlaces, con enlaces a productos relacionados.
- Enlaces utilitarios en todas las páginas: cotizar, carrito, sesión, registro, envíos, compra segura, crédito, boletines, catálogos, servicios, transporte gratuito, empleo, términos, política de ingreso, contacto, reclamaciones, misión y visión.

Inferencia: los listados de categoría se cargan con JavaScript. Si es así, el descubrimiento de fichas depende del sitemap y de los pocos enlaces de la portada y de los bloques de productos similares.

Anomalías observadas:

- Los enlaces se resuelven como relativos a la ruta actual, lo que genera rutas como `/categoria/categoria/abrazaderas-174` y `/producto/producto/...`. Las 17 URL del tipo `/producto/categoria/...` solicitadas respondieron 302. No se pudo comprobar si el HTML incluye una etiqueta `<base>` que corrija esto en el navegador, porque el rastreador no la conserva.
- Hay un enlace a `resgistro.php`, con error de escritura, junto a `registro.php`, y otro a una ruta `/2`.
- Los correos usan la protección de Cloudflare (`/cdn-cgi/l/email-protection`). Inferencia: el sitio está detrás de Cloudflare.

## Llamadas a la acción

- `Cotiza en línea y recibe envíos a todo el Perú` se repite en las meta descripciones.
- Rutas de compra: `/cotizar.php`, `/carrito.php`, `/sesion.php` y `/registro.php`.
- Refuerzos comerciales: `/solicita-tu-credito.php`, `/transporte-gratuito.php`, `/envios.php`, `/compra-segura.php` y `/comprobantes.php`.
- Venta cruzada en ficha: `Complementa tu compra` y `Productos similares`.

No fue posible determinar si existe botón de WhatsApp, porque los enlaces externos no se conservan en los datos. Sí hay un número móvil publicado.

## Señales de SEO local

- JSON-LD de tipo Store con dirección completa: Av. Urbano Cueto Mz. B Lote 18, Pueblo Libre (antes de llegar al Cementerio Los Sauces), San Juan de Lurigancho, Lima, PE.
- Teléfonos de empresa: +5117824123 y [celular omitido].
- `Lima` y `Perú` aparecen en el título, el H1 y la meta descripción de la portada.
- Enlace a libro de reclamaciones, requisito habitual en el comercio peruano.
- Idioma declarado: `es`.
- No se observaron páginas por ciudad o región entre los enlaces disponibles. La promesa de envío nacional no se desarrolla por zonas en los datos obtenidos.

## Experiencia de usuario

Se trata de inferencias, porque el análisis se basa en HTML y no hubo revisión visual.

**Fortalezas**

- El recorrido comercial es completo: cotización, carrito, crédito, envíos y comprobantes en todas las páginas.
- Las categorías muestran cifras de productos, lo que transmite disponibilidad.
- La portada agrupa productos por problema: desatoro, pruebas hidráulicas, cloración.
- La ficha promueve la compra de complementos.

**Debilidades**

- La taxonomía es poco clara: `Construcción` (3 productos) convive con `Construcción & Ferretería` (320), y `Conexiones` reúne 4.205 referencias.
- Se usan abreviaturas como `Acc PVC` y `Acc Bronce`.
- La portada es pesada: 428.825 bytes de HTML y 252 enlaces internos.
- Las fichas tienen poca información técnica verificable en la muestra, y una descripción no coincide con su producto.
- El contenido parece generado por plantillas y datos de catálogo sin revisión editorial.

## Oportunidades para FUNDIGSAC

Las comparaciones con FUNDIGSAC se basan en el código de `Frontend`. Los efectos esperados son inferencias.

1. **Competir por profundidad técnica.** Las fichas de FUNDIGSAC ya contienen medidas por DN y PN, como bridas y pernos. Hay que mantener esas tablas como texto en el HTML inicial y citar las normas que correspondan a cada producto, como ISO 2531 en tubería y EN 124 en tapas, siempre con respaldo documental. Es el punto donde ICOFESA se muestra más débil en la muestra disponible.
2. **Títulos de categoría con intención de compra.** Frente a títulos de una palabra, usar la fórmula producto, material y lugar: por ejemplo, válvulas de compuerta de hierro dúctil PN16 en Lima y tapas de buzón D400 de hierro dúctil en Perú.
3. **Listados rastreables.** Asegurar que las páginas de `/productos/valvulas`, `/productos/tuberias` y `/productos/marcos-y-tapas` tengan enlaces a todas las fichas en el HTML inicial. ICOFESA no los ofrece en las categorías visitadas.
4. **Ampliar el marcado de datos.** FUNDIGSAC ya usa BreadcrumbList en categorías y fichas, que ICOFESA no presenta. Se puede añadir ItemList o CollectionPage en categorías para ampliar esa ventaja.
5. **Completar la dirección estructurada.** El JSON-LD de FUNDIGSAC en `layout.tsx` solo incluye `addressLocality`, mientras ICOFESA publica dirección completa y tipo Store. Conviene añadir `streetAddress` y, si hay punto de atención al público, un tipo LocalBusiness adecuado.
6. **Mantener las páginas de sector.** FUNDIGSAC tiene `/industrias/saneamiento`, `/industrias/mineria` y `/industrias/agricultura`. En ICOFESA los sectores aparecen como titulares de portada y agricultura no figura entre ellos. Son páginas que pueden captar búsquedas por aplicación.
7. **Diferenciarse de la reventa multimarca.** ICOFESA revende marcas de terceros, incluida FUMOSAC. FUNDIGSAC puede destacar su marca propia, garantía y soporte técnico directo, en lugar de competir en número de referencias. Con 7.528 productos declarados, la amplitud no es un frente rentable.
8. **Revisar facilidades comerciales.** Crédito, transporte gratuito y comprobantes en línea son reclamos visibles de ICOFESA. Conviene decidir cuáles puede ofrecer FUNDIGSAC y publicar con claridad las condiciones de envío a regiones.
9. **Evaluar términos de cola larga.** La portada de ICOFESA empuja válvula reductora de presión, anticipadora de onda, de alivio, de control de nivel y compuerta acerrojada. Solo tiene sentido crear contenido sobre los que FUNDIGSAC venda de verdad.

## Acciones pendientes

1. Repetir PageSpeed móvil cuando se recupere la cuota de la API.
2. Revisar `valvulas-166`, `tuberias-167` y una muestra de fichas, con autorización para un nuevo cupo de páginas. Antes conviene ajustar el orden de rastreo, para no gastar cupo en URL `/producto/categoria/...`.
3. Comprobar si existen `<base>` y WhatsApp en una revisión manual.

## Notas de método

- El rastreo se ejecutó una sola vez dentro de la imagen `fundig-scrapling`, con el Fetcher HTTP simple y el User-Agent `FundigsacMarketResearch/1.0`.
- El script de la imagen coincide por SHA-256 con `Report/competencia/scripts/scrape.py`.
- Esta revisión no incluyó correcciones en los sitios de FUNDIGSAC, por lo que no hubo KPI propios que medir. Tampoco se pudo medir ningún KPI de PageSpeed de ICOFESA.
