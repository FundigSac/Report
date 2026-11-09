# Fundición Moreno (FUMOSAC)

| Campo | Valor |
|---|---|
| Sitio analizado | https://fumosac.com.pe/ (redirige con 301 a https://www.fumosac.com.pe/) |
| Segmento | Fabricante nacional |
| Fecha del rastreo | 9 de noviembre de 2026, 17:31 UTC |
| Estado del rastreo | ok |
| Páginas con datos | 34 de 35 solicitudes de página; la restante fue la redirección inicial |
| Solicitudes HTTP totales | 38, con intervalo mínimo de 3 segundos |
| robots.txt | Presente (HTTP 200), sin crawl-delay; ninguna ruta omitida |
| PageSpeed móvil | n/d: la API respondió HTTP 429 por cuota agotada |
| Datos de origen | `Report/competencia/datos/fumosac.json` |

## Alcance y límites del dato

En este documento, lo que no lleva la marca **Inferencia** procede directamente del rastreo. Lo marcado como **Inferencia** es interpretación.

- El rastreo terminó sin URL pendientes, por lo que cubre todas las páginas alcanzables por enlaces desde la portada. No se leyó `wp-sitemap.xml`, de modo que podrían existir páginas sin enlazar.
- El rastreador usa HTTP simple y no ejecuta JavaScript. El contenido que se cargue por script no aparece aquí.
- No se guardó el texto de las páginas. Solo hay título, meta descripción, H1, H2, enlaces internos, normas detectadas y tipos JSON-LD.
- Los campos `productos`, `categorias` y `especificaciones` del JSON están vacíos porque el extractor espera estructura de WooCommerce o rutas `/producto/`. Ese vacío no prueba ausencia de datos: los productos de este informe se tomaron de los H1, y el detalle de las tablas de medidas no se capturó.
- Los PDF enlazados no se descargaron ni se leyeron.
- Las normas son citas del sitio. No se verificó ningún certificado.
- El rastreador solo registra enlaces internos y formatos `tel:` y `mailto:`. No permite afirmar nada sobre botones de WhatsApp, redes sociales ni apariencia visual.

## Indicadores medidos

| Indicador | Resultado | Lectura |
|---|---|---|
| PageSpeed móvil, rendimiento | n/d | Sin medición por cuota de la API |
| PageSpeed móvil, SEO | n/d | Sin medición por cuota de la API |
| Títulos únicos | 1 de 34 páginas | Deficiente |
| Meta descripciones únicas | 1 de 34 páginas | Deficiente |
| Longitud de la meta descripción | 500 caracteres o más (el rastreador corta en 500) | Excesiva |
| Caracteres corruptos en la meta descripción | 12 caracteres de reemplazo en los primeros 500 | Defecto |
| Páginas con H1 | 20 de 34 | Parcial; faltan portada y categorías |
| Páginas con más de un H1 | 0 | Correcto |
| Canónica autorreferente | 34 de 34 | Correcto |
| Atributo de idioma | `es` en 34 de 34 | Correcto |
| Páginas con JSON-LD | 0 de 34 | Ausente |
| Fichas con PDF enlazado | 17 de 20 | Bueno |
| Peso del HTML | 45,3 KB a 65,7 KB; mediana 49,2 KB | Moderado |
| Enlaces internos por página | 14 a 20; mediana 16 | Solo navegación y descenso a fichas |

La medición de PageSpeed queda pendiente de una cuota disponible. La API informó un límite diario de 0 consultas para solicitudes sin clave, así que no se reintentó ni se sustituyó por otra herramienta.

## Cobertura de catálogo y familias

El sitio presenta 20 fichas de producto y dos páginas de familia sin fichas hijas.

| Familia | Página | Fichas | Productos |
|---|---|---|---|
| Válvulas | `/categoria-valvulas/` | 6 | Compuerta garra de cóndor (HDPE), compuerta serie 15 Luflex (PVC), compuerta brida serie 3, compuerta brida serie 14, check flex, válvula de aire doble efecto triple función |
| Tapas de buzón | `/categoria-tapas-de-buzon/` | 4 | Marco y tapa D-400, marco cuadrado y tapa circular, marco y tapa estándar, marco y tapa para caja de válvulas |
| Grifos contra incendio | `/categoria-grifos-contra-incendio/` | 4 | Hidrante cuerpo seco brida HDPE/PVC, hidrante cuerpo seco de 3 bocas, hidrante cuerpo húmedo brida/embone PVC, grifo subterráneo |
| Acoples | `/categoria-acoples/` | 4 | Acople flexible gran rango escalonado, unión rígida de desmontaje autoportante, adaptador universal HDPE, adaptador de bridas |
| Filtros | `/categoria-filtros/` | 2 | Filtro tipo Y (strainer), filtro tipo H (canasta) |
| Accesorios | `/categoria-accesorios/` | 0 | Una sola página agrupada: tee, transiciones, cruces y reducciones, codos |
| Rejillas pluviales | `/rejillas-pluviales/` | 0 | Página única |

Otras secciones: `/mineria/`, `/ingenieria-y-manufactura/`, `/tecnologia/`, `/certificaciones/`, `/nuestra-empresa/` y `/contacto/`. La portada anuncia también fundición para piezas mineras, agricultura y automotriz.

Ninguna URL, H1 ni H2 menciona válvula mariposa ni tubería de hierro dúctil, dos líneas que sí vende FUNDIGSAC.

**Inferencia:** FUMOSAC vende lo que funde y mecaniza. No aparece como proveedor de línea completa, porque no publica tubería ni válvula mariposa.

**Inferencia:** el sitio se reestructuró hace poco. Los PDF están en carpetas de junio y julio de 2026, y las URL anotadas en `COMPETIDORES.md` (`/accesorios/`, `/marco-y-tapa-d400/`) ya no figuran en su enlazado. No se comprobó si redirigen.

## Profundidad de especificaciones

| Elemento | Dato observado |
|---|---|
| Bloque de dimensiones | H2 "MEDIDAS EN MILIMETROS" en 14 de las 20 fichas |
| Ficha técnica PDF | 16 archivos distintos, enlazados desde 17 fichas |
| Fichas sin PDF | Adaptador universal HDPE, adaptador de bridas, unión rígida de desmontaje |
| Presión nominal en encabezados | PN 10, 16 y 25 en válvulas brida serie 3 y serie 14; PN16 en grifo subterráneo |
| Material en encabezados | Hierro dúctil ASTM A536 grado 65-45-12 en filtro tipo H |
| Recubrimiento en encabezados | Epóxico azul de 250 micras según BS 6920 en unión de desmontaje |
| Clase de carga | D-400, con mención de resistencias de hasta 60 y 90 toneladas |
| Compatibilidad | Embone directo a HDPE (garra de cóndor) y a PVC sin pegamento (serie 15) |

**Inferencia:** la profundidad técnica es buena para un comprador que ya conoce el producto, porque combina tabla de medidas, PDF y normas por ficha. Los rangos de diámetro no aparecen en títulos ni encabezados, así que no sirven para captar búsquedas por DN.

Errores de contenido detectados:

- `/filtro-tipo-y-strainer/` enlaza a `filtro-tipo-h.pdf`, el mismo archivo del filtro H.
- El H2 de `/marco-y-tapa-para-caja-de-valvulas/` describe anillos de la válvula Luflex y tubería PVC, ajenos a un marco y tapa.
- El archivo de la tapa D-400 se llama `marco-y-tsps-D-400-600mm-850.pdf`.
- Conviven "grifo" e "hidrante" para la misma familia, y "ISO1083" con "ISO 1083" para la misma norma.

## Normas y certificaciones citadas

Conteo por páginas, unificando variantes de escritura.

| Ámbito | Norma | Páginas |
|---|---|---|
| Material | ASTM A536 | 27 |
| Material | ISO 1083 | 26 |
| Contacto con agua y revestimiento | BS 6920 | 14 |
| Elastómeros | ISO 4633 y NTP-ISO 4633 | 9 y 9 |
| Elastómeros | ASTM D2000 | 3 |
| Bridas | ISO 7005-2 y NTP ISO 7005-2 | 10 y 2 |
| Bridas | ISO 7005 e ISO 7005-1 | 2 y 1 |
| Válvulas | EN 1074 | 7 |
| Válvulas | EN 558 e ISO 5752 | 3 y 2 |
| Válvulas | ISO 7259 y NTP 350.064 | 2 y 2 |
| Válvulas check y de aire | AWWA C508 y AWWA C512 | 2 y 3 |
| Marcos y tapas | EN 124 y UNE EN 124 | 3 y 3 |
| Marcos y tapas | NTP 350.106 | 2 |
| Grifos e hidrantes | AWWA C502 y AWWA C503 | 3 y 1 |
| Grifos e hidrantes | NTP 350.102 y BS 750 | 2 y 2 |
| Acoples | UNE EN 14525 y NTP 350.108 | 4 y 3 |
| Accesorios | ISO 2531 y NTP ISO 2531 | 1 y 1 |
| Tornillería y otros materiales | ASTM A307, ASTM A666, ASTM B62 | 5, 1 y 1 |
| Sistema de gestión | ISO 9001 | 2 (`/certificaciones/`, `/ingenieria-y-manufactura/`) |

La cita de ISO 9001 no confirma una certificación vigente: no se revisó ni el texto ni el certificado.

**Inferencia:** el uso combinado de normas peruanas, europeas y AWWA por familia busca cubrir especificaciones de expedientes públicos y de EPS.

## Palabras clave objetivo

Todo este apartado es **inferencia**, a partir de títulos, encabezados y URL. No hay datos de posiciones ni volumen de búsqueda.

| Intención | Términos probables | Fuerza de la señal |
|---|---|---|
| Marca | Fumosac, Fundición Moreno | Alta: la marca abre el título global |
| Genérica del rubro | suministros de agua, alcantarillado y saneamiento | Media: título global, igual en todo el sitio |
| Producto, válvulas | válvula compuerta brida, válvula compuerta HDPE, válvula check, válvula de aire | Media: solo en H1 y URL |
| Producto, tapas | marco y tapa D-400, marco y tapa para caja de válvulas, tapas de buzón | Media: solo en H1 y URL |
| Producto, incendio | hidrante cuerpo seco, hidrante cuerpo húmedo, grifo contra incendio subterráneo | Media: solo en H1 y URL |
| Producto, uniones | acople flexible gran rango, unión de desmontaje autoportante, adaptador de bridas, filtro Y | Media: solo en H1 y URL |
| Sectores | minería, agricultura, automotriz, fundición de hierro dúctil | Baja: H2 de portada y `/tecnologia/` |

El título no aporta palabras de producto en ninguna ficha, de modo que el sitio depende del H1 y la URL para posicionar cada producto.

## Marcado de datos estructurados

Ninguna de las 34 páginas tiene JSON-LD: no hay Organization, LocalBusiness, Product, BreadcrumbList, WebSite ni FAQPage.

**Inferencia:** el sitio no obtiene resultados enriquecidos ni entrega señales estructuradas a buscadores y asistentes de IA.

Tampoco se detectaron migas de pan, ni en marcado ni con las clases CSS habituales.

## Enlazado interno

| Aspecto | Dato observado |
|---|---|
| Plataforma | WordPress (`wp-content`, `wp-sitemap.xml`) |
| Navegación global | 14 enlaces idénticos en las 34 páginas |
| Profundidad | Portada, categoría, ficha: dos clics |
| Enlaces entrantes a cada ficha | Uno desde su categoría, más el autoenlace de la propia página |
| Enlaces laterales entre fichas | Ninguno |
| Enlaces desde `/mineria/` a productos | Ninguno; solo la navegación global |
| URL | Planas en la raíz, sin carpeta de familia |
| Redirección de dominio | Sin www a www, con 301 |

**Inferencia:** toda la autoridad interna se concentra en las 14 páginas de la navegación. Las fichas reciben muy poca y no se refuerzan entre sí.

## Llamadas a la acción

Lo observable se limita a lo siguiente:

- Formulario en `/contacto/`, con el H2 "Envíanos un mensaje". No se envió.
- Correo `ventas@fumosac.com.pe` con enlace `mailto:`.
- Descarga de ficha PDF en 17 fichas.

No se encontró ningún enlace `tel:` en las 34 páginas ni URL de cotización o carrito. El rastreador no recoge precios ni enlaces externos, por lo que precios, WhatsApp y redes sociales quedan sin evaluar.

**Inferencia:** el recorrido comercial es consultivo y se cierra por correo o formulario, sin un paso de cotización por producto.

## Señales de SEO local

- Ningún título, H1 ni H2 contiene Lima, Perú ni otra localidad.
- Sin dirección ni teléfono en datos estructurados, y sin enlaces `tel:`.
- Sin páginas por ciudad o región.
- La meta descripción tampoco menciona ubicación en los primeros 500 caracteres.
- No se evaluó el perfil de empresa en Google.

**Inferencia:** en los campos capturados, el dominio `.com.pe` es casi la única señal geográfica. La dirección podría figurar en el texto de `/contacto/` o del pie de página, que no se guardó.

## Fortalezas y debilidades de experiencia

Sin revisión visual; se basa en estructura y encabezados.

Fortalezas:

- Arquitectura simple, con cada producto a dos clics de la portada.
- Normas, medidas y PDF disponibles por producto.
- Páginas propias de capacidad industrial, con fundición, mecanizado, ingeniería, laboratorios y acabados.
- Fichas de hidrantes con normas AWWA y NTP, familia ausente del catálogo de FUNDIGSAC.
- ICOFESA y Leoneblu revenden la marca, según `COMPETIDORES.md`.

Debilidades:

- Título y meta descripción idénticos en todo el sitio, lo que dificulta distinguir los resultados de búsqueda.
- Meta descripción con caracteres corruptos. En el mismo documento el título y los H2 se leen bien, por lo que el defecto parece estar en la fuente (**inferencia**).
- Sin H1 en portada, categorías y páginas institucionales.
- H2 genéricos en categorías, como "SOLUCIONES", y párrafos completos usados como H2 en fichas.
- Accesorios en una sola página, sin URL por pieza.
- `/tecnologia/` mezcla español e inglés en una página con `lang="es"`.
- Mayúsculas y grafías irregulares en H1, como "FILTRO TIPO H" o "Marco y tapa estandar".

## Oportunidades para FUNDIGSAC

Las referencias a FUNDIGSAC provienen del código del repositorio `Frontend`. No se comprobó el sitio en producción.

1. **Ganar búsquedas por producto.** FUMOSAC repite un único título. FUNDIGSAC ya genera metadatos por ficha, y debería usarlos con producto, norma, PN y "Perú" (por ejemplo, "Marco y tapa D400 EN 124 en Perú").
2. **Dominar válvula mariposa y tubería de hierro dúctil.** FUMOSAC no las publica y FUNDIGSAC sí las tiene en catálogo. Conviene priorizar guías y fichas de ISO 2531, EN 545, clases K y válvulas mariposa.
3. **Convertir el marcado en ventaja.** FUMOSAC tiene 0 páginas con JSON-LD. FUNDIGSAC ya emite Organization, WebSite, Product y BreadcrumbList; puede añadir DN, PN y normas como `additionalProperty` en cada Product.
4. **Superar su ficha técnica.** FUMOSAC ofrece medidas y PDF. FUNDIGSAC debería publicar la misma información en HTML indexable, con DN, PN, material, recubrimiento y norma, además del PDF descargable. FUNDIGSAC tiene hoy 3 fichas PDF y 2 folletos, todos de válvula de compuerta (informe, sección 6.2).
5. **Crear páginas por pieza en conexiones.** FUMOSAC agrupa tees, codos, cruces y reducciones en una página. Una URL por pieza captura búsquedas que esa página no puede cubrir.
6. **Definir postura en hidrantes.** FUMOSAC tiene 4 fichas con AWWA C502, C503, NTP 350.102 y BS 750. En FUNDIGSAC solo aparecen en el asistente, como cotización a pedido. Hay que decidir entre crear fichas o aceptar esa brecha.
7. **Ganar en SEO local y contacto directo.** FUMOSAC no expone `tel:` ni dirección estructurada. FUNDIGSAC debe mantener su Organization con PostalAddress, un teléfono clicable y WhatsApp en cada ficha, y añadir contenido por zona o EPS donde haya venta real.
8. **Mantener la ruta de cotización como diferencial.** FUMOSAC no muestra un paso de cotización por producto; FUNDIGSAC tiene `/cotizar` y puede enlazarla desde cada ficha con el producto preseleccionado.
9. **Reforzar el enlazado lateral.** FUMOSAC no enlaza fichas entre sí ni conecta `/mineria/` con productos. FUNDIGSAC puede enlazar válvula, unión, marco y tapa como conjunto, y cada industria con sus productos.
10. **Responder al argumento de fabricante nacional.** FUMOSAC presenta fundición, mecanizado y laboratorios como capacidades integradas. FUNDIGSAC debería responder con evidencia verificable: certificados descargables, ensayos por lote, stock y plazos de entrega.
11. **Revisar referencias normativas propias.** FUMOSAC asocia NTP 350.106 a tapas y NTP 350.064 a válvulas, mientras `Frontend/src/modules/catalog/data.ts` usa NTP 350.085 en ambas familias. El área técnica debe validar cuál corresponde; aquí no se verificó el contenido de ninguna norma.
