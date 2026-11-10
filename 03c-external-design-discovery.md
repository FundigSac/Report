# 03c · Descubrimiento externo de referencias de diseño

Fecha de revisión: 2026-11-10. Alcance: referencias externas nuevas, distintas de los marcadores del propietario (02-bookmarks-inventory.csv) y de los competidores peruanos ya evaluados en 05-competitor-benchmark.md. Se proponen patrones adaptados; no se copian logos, fotos, textos ni código de terceros.

## 1. Método

Las páginas se trataron como datos. No se inició sesión, no se enviaron formularios, no se agregó nada a carritos y no se descargó ningún archivo. En los banners de cookies se eligió la opción más restrictiva disponible (rechazar o solo esenciales); donde no había opción de rechazo, no se aceptó nada. La revisión se detuvo ante una verificación anti-bot (Saint-Gobain, móvil).

**Viewports.** La ventana de Chrome era compartida y estaba maximizada a 1707×842, así que no se pudo fijar en 1440. Por eso las capturas de escritorio de X1–X8 están a 1707×842. Para el móvil (390×844) y para el escritorio de X9–X14 (1440×900) se usó el panel de navegador integrado con emulación de viewport. A mitad de la sesión otro proceso cerró el grupo de pestañas de Chrome, y el resto del trabajo se hizo en el panel integrado. No quedaron pestañas propias abiertas.

## 2. Líneas de descubrimiento y consultas

| Línea | Objetivo | Consultas usadas (WebSearch) | Resultado |
|---|---|---|---|
| (a) Fabricantes B2B de válvulas y tubería | Catálogos y buscadores de producto | `waterworks valves product finder filters ductile iron gate valve catalog`; `válvulas hierro dúctil Perú catálogo fabricante`; `electrofusion fittings product finder HDPE catalog`; `gfps.com ELGEF Plus electrofusion fittings product page` | Semillas AVK, BERMAD ×2, Saint-Gobain PAM; nuevos: Pollardwater, GF Piping Systems |
| (b) Cotización sin precio + fichas técnicas | Carrito de solicitud y centro de descargas | `electromagnetic water meter product page datasheet download configurator`; `Endress+Hauser Promag W 400 water electromagnetic flowmeter product page` | Endress+Hauser Promag W 400; GF (carrito 'Request') |
| (c) Inventario / almacén / EPP | Stock por talla, entregas, offline | `offline-first mobile field app design pattern sync status pending uploads design system` (búsqueda por brecha) | Sortly; guía de Dynamics 365 Field Service (no navegable, ver brechas) |
| (d) Admin: usuarios/roles y casos/reclamos | RBAC, cola con SLA | `complaints case management dashboard UI SLA deadline ticket queue design system`; `design system pattern roles permissions matrix UI user management admin guidelines` (brecha) | Shopify Polaris (App Home), GitHub Docs (matriz de roles), Carbon (estados) |
| (e) Microinteracciones, grillas, tablas densas accesibles | Estados vacíos, tablas, guardado, formularios | `design system data table pattern accessible bulk actions filters empty state` | Cloudscape, Primer, GOV.UK |

La segunda búsqueda, guiada por brechas, se centró en dos áreas débiles tras la primera ronda: la **UI de permisos** (se encontró GitHub Docs) y el **stock móvil offline** (se encontró Sortly; la documentación de Microsoft quedó bloqueada en el navegador). La ficha de producto quedó bien cubierta por AVK, E+H y GF.

## 3. Shortlist priorizada (14 referencias)

| # | Referencia | URL | Tipo | Por qué | Páginas visitadas | Viewports | Limitaciones | Fecha |
|---|---|---|---|---|---|---|---|---|
| X1 | AVK Válvulas – Buscador de productos | https://www.avkvalvulas.com/es-es/buscador-de-productos | Fabricante válvulas waterworks (semilla) | Buscador facetado en español de válvulas de fundición dúctil con ficha técnica muy completa; mismo dominio que FUNDIGSAC. | Buscador (listado 561), menú Especificaciones técnicas desplegado, búsqueda sin resultados, ficha 01-70-035 (descargas, tabla de datos, componentes, relacionados) | Escritorio 1707×842 (Chrome); móvil 390×844 (panel con emulación) | Chrome compartido no permitió redimensionar a 1440; no se descargó ningún archivo; móvil solo listado. | 2026-11-10 |
| X2 | BERMAD – Válvulas de control | https://www.bermad.com/es/products/control-valves/ | Fabricante válvulas de control (semilla) | Listado con filtros en línea, chips, contador y estado en URL; ficha con pestaña Documentación. | Listado, filtro Segmentos aplicado (309→127), ficha /es/product/1020-2/ pestañas Características y Documentación | Escritorio 1707×842; móvil 390×844 (banner de cookies cubrió la vista) | Banner Cookiebot sin rechazo en primera capa; se eligieron solo cookies necesarias en escritorio y no se aceptó nada en móvil. | 2026-11-10 |
| X3 | BERMAD – Waterworks | https://www.bermad.com/waterworks/ | Landing por sector (semilla) | Página de sector con sub-segmentos, aplicaciones, localizador de oficinas y buscador rápido persistente. | Landing completa (texto), barra inferior de producto, localizador de expertos; móvil | Escritorio 1707×842; móvil 390×844 | No se abrió el demo 3D ni el brochure PDF (descarga). | 2026-11-10 |
| X4 | Saint-Gobain PAM Perú | https://www.saint-gobain.com.pe/es/pam | Competidor local hierro dúctil (semilla) | Referente local de hierro dúctil; útil sobre todo como contraejemplo. | Página PAM, 404 (/es/pam/valvulas-xyz), búsqueda 'valvula' | Escritorio 1707×842; móvil bloqueado | Móvil: verificación anti-bot de Cloudflare; se detuvo ahí sin resolverla. | 2026-11-10 |
| X5 | Pollardwater – AWWA Valves | https://www.pollardwater.com/category/valves/awwa-valves/_/N-zc3vww | Distribuidor B2B waterworks | Facetas con conteos por atributo técnico y norma; ficha con colección por tamaño y ayuda telefónica. | Categoría AWWA, ficha M200MD11 (Call for Pricing), búsqueda sin resultados, móvil del listado | Escritorio 1707×842; móvil 390×844 | Panel de filtro móvil no terminó de renderizar en la captura; no se agregó nada al carrito. | 2026-11-10 |
| X6 | Endress+Hauser – Promag W 400 | https://www.za.endress.com/en/field-instruments-overview/flow-measurement-product-overview/electromagnetic-flowmeter-promag-w400-5w4c | Fabricante caudalímetros electromagnéticos | Ficha de medidor electromagnético para agua: specs at a glance, centro de descargas filtrable, pestañas con URL. | Overview, Downloads (filtro por tipo), móvil Downloads | Escritorio 1707×842; móvil 390×844 | Configurador y precio requieren login; no se usaron. No se descargó nada. | 2026-11-10 |
| X7 | GF Piping Systems – Catálogo | https://www.gfps.com/en-us/products-solutions.catalog.html/fittings/couplers-sockets/~106921/753911817.html | Fabricante accesorios PE electrofusión | Referente directo para accesorios HDPE: búsqueda federada, ficha por variante y carrito de solicitud sin precio. | 404 de búsqueda, buscador typeahead 'electrofusion coupler', ficha Coupler d160 (variante 1/7), móvil ficha | Escritorio 1707×842; móvil 390×844 | No se agregó al carrito 'Request'; cookies rechazadas. | 2026-11-10 |
| X8 | Cloudscape Design System (AWS) | https://cloudscape.design/patterns/general/empty-states/ | Design system – tablas y estados | Guía explícita de empty state vs. zero results y demo de tabla densa con orden múltiple y preferencias. | Patrón Empty states, demo Table view (filtro sin coincidencias), móvil demo | Escritorio 1707×842; móvil 390×844 | El modal de preferencias no abrió en el clic probado. | 2026-11-10 |
| X9 | Shopify Polaris – App Home patterns | https://shopify.dev/docs/api/app-home/latest/patterns | Design system – admin | Plantillas Index/Details y composiciones (index table, setup guide, metrics card) para paneles de gestión. | Índice de patrones, plantilla Details, composición Index table, Setup guide | Escritorio 1440×900 (emulado) | La URL antigua polaris-react redirige a shopify.dev; móvil no revisado. | 2026-11-10 |
| X10 | GitHub Primer | https://primer.style/product/components/data-table/ | Design system – tablas, guardado, degradación | DataTable accesible y patrones de guardado explícito y experiencias degradadas, útiles para stock offline y admin. | DataTable, UI pattern Degraded experiences, UI pattern Saving, móvil DataTable | Escritorio 1440×900; móvil 390×844 | Componentes React marcados como experimentales. | 2026-11-10 |
| X11 | GOV.UK Design System | https://design-system.service.gov.uk/patterns/check-answers/ | Design system – formularios públicos | Referente de accesibilidad para formularios con efecto legal (Libro de Reclamaciones) y confirmaciones con número de referencia. | Check answers, Confirmation pages, Error summary; banner de cookies (rechazado) | Móvil 390×844; escritorio no capturado | Ejemplos completos abren en pestaña nueva y no se abrieron. | 2026-11-10 |
| X12 | Carbon Design System – Status indicators | https://www.carbondesignsystem.com/building-blocks/core/patterns/status-indicators | Design system – estados y severidad | Reglas de indicadores de estado (icono+forma+color+texto, consolidación por severidad) para plazos legales y stock bajo. | Patrón Status indicators (redirigido desde /patterns/status-indicator-pattern/) | Escritorio 1440×900 | Móvil no revisado. | 2026-11-10 |
| X13 | GitHub Docs – Repository roles | https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization | Documentación RBAC (búsqueda por brecha) | Matriz pública acciones × roles acumulativos: modelo claro para la pantalla de roles del admin. | Artículo completo; inspección de las 2 tablas de permisos | Escritorio 1440×900; móvil intentado | En móvil la emulación reportó innerWidth 764, no se pudo verificar el comportamiento a 390 px. | 2026-11-10 |
| X14 | Sortly – Inventory features | https://www.sortly.com/features/ | Software inventario (búsqueda por brecha) | Funciones de inventario de campo: check-in/out, alertas de stock bajo, reportes de flujo, offline y escaneo. | Página Features, 404 (/features/item-check-in-check-out/), móvil 404 | Escritorio 1440×900; móvil 390×844 | Es página de marketing; la app real requiere cuenta (no se inició sesión). | 2026-11-10 |

Prioridad sugerida para FUNDIGSAC: X7 GF, X1 AVK, X6 E+H y X5 Pollardwater para el frontend; X11 GOV.UK para el Libro de Reclamaciones; X8 Cloudscape, X9 Polaris, X13 GitHub Docs y X12 Carbon para el admin; X10 Primer y X14 Sortly para el stock. X4 Saint-Gobain PAM sirve sobre todo como contraejemplo.

## 4. Ideas por sitio (98 ideas)

Escala: impacto 0–5; esfuerzo S/M/L. Decisión: aprovechar (usar tal cual el patrón), adaptar (ajustar a FUNDIGSAC), descartar (no aplica o es contraejemplo a evitar).

### X1 · AVK Válvulas – Buscador de productos

Fuente: https://www.avkvalvulas.com/es-es/buscador-de-productos

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X1-1 | buscador-de-productos | Cuatro menús de filtro: Uso, Producto, Especificaciones técnicas (PN, Material, Tipo de tubería, Conexión, DN, Dirección de cierre) y Normas, más búsqueda por referencia/serie y contador 'Resultados 561'. | El catálogo por familia no permite acotar por DN, PN, conexión o norma. | Barra de filtros en /productos agrupada en Aplicación (agua potable, saneamiento, agricultura, minería), Familia, Especificación (DN, PN, material, conexión) y Norma, con contador de resultados. | frontend · Catálogo /productos – FilterBar | 5 | M | Filtros como &lt;fieldset&gt;/&lt;legend&gt;; contador en aria-live=polite. | adaptar |
| X1-2 | buscador-de-productos (tarjeta) | Cada tarjeta muestra nombre, subtítulo, serie y 4 atributos (Conexión, Material, Rango DN, PN) más enlace 'Consulta'. | Las tarjetas actuales no permiten comparar a simple vista. | ProductCard con 4 atributos clave en lista &lt;dl&gt; y botón 'Añadir a cotización'. | frontend · ProductCard | 5 | S | &lt;dl&gt; semántica; botón con nombre accesible que incluya el producto. | aprovechar |
| X1-3 | ficha 01-70-035 | Columna de accesos: Hoja técnica, Certificados, Dibujos 3D, Vídeo, Añadir a la consulta, Productos relacionados. | La ficha obliga a hacer scroll para encontrar el PDF. | Barra de anclas sticky en la ficha (Descargas, Certificados, Tabla de medidas, Cotizar). | frontend · ProductSheet – AnchorNav | 4 | S | Enlaces de ancla con foco visible; sticky solo en ≥1024 px. | adaptar |
| X1-4 | ficha 01-70-035 (Tabla de datos) | Tabla por referencia con DN, dimensiones y peso; aviso 'Desplazar para más información'. | Las medidas por DN están en PDF y no se pueden consultar en móvil. | Tabla de variantes por DN con &lt;caption&gt;, th scope y primera columna fija; scroll horizontal anunciado. | frontend · ProductSheet – VariantTable | 5 | M | Contenedor con tabindex=0 y role=region con etiqueta para teclado. | adaptar |
| X1-5 | ficha 01-70-035 (Descargas) | Descargas agrupadas: Hoja técnica, Apéndices, Certificados, Manual IOM, Vídeo; selección múltiple con 'Descargar zip · 0 archivos seleccionados'. | Los PDF aparecen sueltos sin tipo ni versión. | Agrupar descargas por tipo con tamaño y fecha; dejar el zip para una fase posterior. | frontend · ProductSheet – DownloadList | 4 | M | Mostrar peso del archivo antes del clic; enlaces con tipo de archivo en el texto. | adaptar |
| X1-6 | ficha 01-70-035 (Componentes) | Lista numerada de componentes con material (cuerpo GJS-500-7, eje 1.4104, etc.). | El cliente técnico no ve los materiales sin abrir el PDF. | Sección 'Materiales' en la ficha como lista numerada vinculada al despiece. | frontend · ProductSheet – MaterialsList | 3 | S | Texto plano indexable (SEO). | aprovechar |
| X1-7 | buscador (Comparar) | Casilla 'Comparar' en cada tarjeta y botón 'Comparar productos'; en móvil desaparece. | No existe forma de comparar dos válvulas. | Comparador de hasta 3 productos solo en escritorio. | frontend · CompareDrawer | 3 | M | Checkbox con etiqueta; anunciar cantidad seleccionada. | adaptar |
| X1-8 | búsqueda 'zzxqw' | La búsqueda sin coincidencias muestra solo 'Resultados 0', sin ayuda. | Contraejemplo: el visitante queda sin salida. | Estado vacío con sugerencias, botón 'Limpiar filtros', familias populares y WhatsApp. | frontend · SearchEmptyState | 4 | S | Mensaje en aria-live. | aprovechar |
| X1-9 | buscador (móvil 390) | En móvil los 4 filtros se apilan como bloques azules y empujan los resultados. | En móvil el catálogo se ve tarde. | En móvil, botón 'Filtrar (n)' que abre una hoja inferior con los filtros y 'Ver N resultados'. | frontend · FilterSheet (móvil) | 4 | M | Gestión de foco al abrir/cerrar; Escape cierra. | adaptar |

### X2 · BERMAD – Válvulas de control

Fuente: https://www.bermad.com/es/products/control-valves/

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X2-1 | control-valves | Filtros en dropdown en una fila (Segmentos, Soluciones, Aplicaciones, Tipo, Serie), chips eliminables, 'Restablecer todo' y contador '309 → 127 productos encontrados · Mostrando 1-12 de 127'. | No se ve qué filtros están activos. | Chips de filtros activos con 'x' y 'Restablecer todo' bajo la barra de filtros. | frontend · Catálogo – ActiveFilterChips | 5 | S | Chip como botón 'Quitar filtro X'. | aprovechar |
| X2-2 | control-valves?segments[]=… | El estado del filtro va en la URL y hay un icono de compartir junto al contador. | Los vendedores no pueden enviar una búsqueda filtrada. | Serializar filtros en query string y botón 'Compartir búsqueda' (copia enlace o WhatsApp). | frontend · Catálogo – ShareFilters | 4 | S | Sin datos personales en la URL. | aprovechar |
| X2-3 | product/1020-2 (Documentación) | Pestaña Documentación: conmutador Métrico/Imperial y filas con icono descargar y compartir. | Los enlaces a PDF no se pueden compartir sin descargar. | Fila de documento con 'Descargar' y 'Copiar enlace'; sin conmutador de unidades (Perú usa métrico). | frontend · ProductSheet – DocRow | 3 | S | Iconos con aria-label. | adaptar |
| X2-4 | product/1020-2 | Chip de segmento, serie, bloque 'Cómo se usa en agua potable' y soluciones relacionadas. | La ficha no conecta el producto con su aplicación. | Bloque 'Aplicaciones' en la ficha enlazando a páginas de sector. | frontend · ProductSheet – ApplicationsBlock | 4 | M | Enlaces internos (SEO). | adaptar |
| X2-5 | product/1020-2 (cierre) | Cierre con '¿Aún tienes preguntas? Contáctenos'. | El final de la ficha no tiene un siguiente paso. | CTA final con 'Solicitar cotización' y WhatsApp prellenado con el código. | frontend · ProductSheet – EndCTA | 4 | S | El texto de WhatsApp no lleva datos personales. | aprovechar |
| X2-6 | control-valves (contraejemplos) | Las tarjetas abren en pestaña nueva; el texto SEO muestra HTML escapado (&lt;h2&gt;, &lt;a href&gt;); el banner de cookies no ofrece rechazar en la primera capa. | Riesgo de repetir esos errores. | No abrir fichas en pestaña nueva; probar el render de contenido rico; banner con 'Rechazar' al mismo nivel. | frontend · Lista de verificación QA | 3 | S | WCAG 3.2.5; consentimiento informado. | descartar |
| X2-7 | product/1020-2 (breadcrumb) | Breadcrumb completo: Productos &gt; Válvulas de control &gt; Reductoras de presión &gt; 1020. | La subfamilia no aparece en la miga. | Breadcrumb familia/subfamilia con JSON-LD BreadcrumbList. | frontend · Breadcrumb | 3 | S | &lt;nav aria-label='Ruta'&gt;. | aprovechar |

### X3 · BERMAD – Waterworks

Fuente: https://www.bermad.com/waterworks/

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X3-1 | waterworks | Landing del sector con tarjetas de sub-segmentos: Recursos hídricos, Saneamiento, Tratamiento/Desalinización, Minería/Industrial, Redes municipales. | FUNDIGSAC atiende 4 sectores pero no tiene páginas por sector. | Páginas /sectores/{agua-potable, saneamiento, agricultura, mineria} con sus familias y casos. | frontend · SectorLanding | 5 | M | Imágenes propias, lazy y con dimensiones (CLS). | adaptar |
| X3-2 | waterworks (barra inferior) | Barra sticky inferior '209 Products \| Waterworks \| Product Type \| Product Series \| GO'; en móvil colapsa a '209 Products ^'. | Desde contenido editorial no hay acceso rápido al catálogo filtrado. | Barra 'Encuentra tu producto' en páginas de sector con 2 selects y contador; en móvil un botón colapsado. | frontend · SectorFinderBar | 4 | M | No tapar el contenido ni el botón de WhatsApp; respetar safe-area. | adaptar |
| X3-3 | waterworks (aplicaciones) | Carrusel 'Applications in action' con Explore por aplicación (presión, golpe de ariete, bombeo, reservorios). | No se explica qué problema resuelve cada familia. | Grid de aplicaciones (no carrusel) con enlace a productos. | frontend · ApplicationsGrid | 3 | M | Evitar carrusel automático (WCAG 2.2.2). | adaptar |
| X3-4 | waterworks (expertos) | Localizador por segmento y país con tarjetas de oficina (dirección, teléfono, correo). | El contacto es genérico. | 'Contacto por zona' (Lima, norte, sur) con asesor y WhatsApp. | frontend · ContactByRegion | 3 | S | Teléfonos como tel: enlaces. | adaptar |
| X3-5 | waterworks (brochure) | Enlace 'Read Waterworks Solutions Brochure'. | No hay un catálogo por sector descargable. | PDF de catálogo por sector con tamaño indicado. | frontend · SectorLanding – BrochureLink | 3 | S | Indicar formato y peso. | aprovechar |
| X3-6 | waterworks (móvil) | En móvil, logo, buscar y menú van en una barra inferior, en la zona del pulgar. | En el almacén se usa el teléfono con una mano. | Barra de navegación inferior en la app stock (Stock, Entregas, Historial, Más). | stock · AppShell – BottomNav | 4 | M | Objetivos táctiles ≥44 px; aria-current. | adaptar |
| X3-7 | waterworks (DOM) | El carrusel clona tarjetas y el texto de cada segmento sale 3 veces en el DOM. | Contraejemplo: los lectores de pantalla repiten el contenido. | No clonar nodos para carruseles; usar aria-hidden en duplicados si son inevitables. | frontend · Lista de verificación QA | 2 | S | Lectores de pantalla. | descartar |

### X4 · Saint-Gobain PAM Perú

Fuente: https://www.saint-gobain.com.pe/es/pam

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X4-1 | es/pam | Página de marca con 3 párrafos, sin catálogo ni enlaces a producto. | Oportunidad: el competidor local no posiciona producto. | Fichas indexables y páginas de familia optimizadas para 'válvulas de hierro dúctil Perú'. | frontend · SEO – Familia/Ficha | 4 | S | Metadatos y JSON-LD Product sin precio. | aprovechar |
| X4-2 | es/pam/valvulas-xyz (404) | 404 en inglés ('Page not found') en el sitio en español, con solo 'Go to Homepage'. | Un 404 sin salida pierde visitas. | 404 en español con buscador, familias principales y WhatsApp. | frontend · NotFoundPage | 3 | S | Título &lt;h1&gt; claro; status 404 real. | aprovechar |
| X4-3 | es/search?…=valvula | La búsqueda devuelve una página vacía con solo 'Página 1'. | Contraejemplo de búsqueda muda. | Siempre mostrar el término, el número de resultados y un estado vacío explícito. | frontend · SearchResults | 3 | S | aria-live para el conteo. | aprovechar |
| X4-4 | es/pam (banner) | Banner de cookies con consentimiento implícito ('al continuar navegando acepta'). | Riesgo legal (Ley 29733). | Si solo hay cookies esenciales, no mostrar banner; si hay analítica, aceptar/rechazar con el mismo peso. | frontend · CookieBanner | 3 | S | Botones del mismo tamaño y contraste. | aprovechar |
| X4-5 | es/pam (copy) | Errata visible 'produtos'. | Los errores de copy restan credibilidad técnica. | Revisión ortográfica y humanizer del copy antes de publicar. | frontend · Proceso de contenido | 2 | S | — | aprovechar |
| X4-6 | es/pam (móvil) | El acceso móvil activó una verificación anti-bot (Cloudflare 403). | Un challenge en catálogo público ahuyenta clientes y buscadores. | No activar challenge en rutas públicas de catálogo; limitar por tasa solo en formularios. | frontend · Config. Vercel/firewall | 2 | S | Los challenges suelen fallar con tecnologías de asistencia. | aprovechar |

### X5 · Pollardwater – AWWA Valves

Fuente: https://www.pollardwater.com/category/valves/awwa-valves/_/N-zc3vww

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X5-1 | awwa-valves | Facetas con conteo por valor ('8 in (5)', 'Ductile Iron (9)'), bloque 'Your Selections' y 'Clear Filters'. | Se elige un filtro sin saber si devolverá resultados. | Mostrar conteo por valor de filtro y ocultar o deshabilitar valores en 0. | frontend · FilterBar – FacetCounts | 5 | M | Conteos calculados en cliente sobre catálogo estático (rápido). | aprovechar |
| X5-2 | awwa-valves (normas) | Facetas por norma: AWWA C-509, C-515, ASTM A-536, ANSI B16.1. | Los compradores de licitación buscan por norma. | Filtro 'Norma' (ISO 2531, ISO 4427, NTP, AWWA) y norma visible en la tarjeta. | frontend · FilterBar – Norma | 4 | S | — | aprovechar |
| X5-3 | awwa-valves (precios) | En la misma grilla conviven precios y 'Call for Pricing'. | Mezclar precio y 'consultar' confunde. | Sin precios públicos y un CTA único 'Solicitar cotización'. | frontend · ProductCard – CTA | 4 | S | — | aprovechar |
| X5-4 | ficha M200MD11 | 'Entire Collection 1-4 of 4' con los demás tamaños de la serie. | Para cambiar de DN hay que volver al listado. | Selector o lista de DN hermanos de la misma serie en la ficha. | frontend · ProductSheet – SiblingSizes | 5 | M | Lista de enlaces con DN en el texto. | adaptar |
| X5-5 | ficha M200MD11 | 'Need Help? 1-800-… 7:30 am to 7:30 pm EST' junto a cantidad y CTA. | El cliente no sabe cuándo lo atenderán. | Bloque de ayuda con horario de atención, WhatsApp y teléfono junto al CTA de cotización. | frontend · ProductSheet – HelpBox | 4 | S | tel: y wa.me como enlaces. | aprovechar |
| X5-6 | ficha M200MD11 | Especificaciones clave más 'View All Specifications'. | Las fichas largas abruman en móvil. | Specs clave visibles y el resto en acordeón 'Ver todas'. | frontend · ProductSheet – SpecsAccordion | 3 | S | &lt;details&gt;/&lt;summary&gt; nativo. | aprovechar |
| X5-7 | no-result?Ntt=zzxqw valve | 'We couldn't find any results for …' con consejos y categorías destacadas con imagen. | Ya cubierto en X1-8; aquí está el contenido modelo. | Estado vacío con el término, 3 consejos y familias destacadas. | frontend · SearchEmptyState | 5 | S | Repetir el término dentro del &lt;h1&gt;. | aprovechar |
| X5-8 | awwa-valves (móvil) | Botones 'Filter' y 'Sort' en una fila a ancho completo; lista con imagen a la izquierda. | En móvil la grilla de 2 columnas es apretada. | En móvil, lista de 1 columna (imagen 96 px a la izquierda) y botones Filtrar/Ordenar arriba. | frontend · Catálogo – MobileList | 4 | S | Imágenes con width/height. | aprovechar |
| X5-9 | awwa-valves (datos) | Facetas duplicadas por mayúsculas: 'Non-rising (12)' y 'Non-Rising (1)'. | Contraejemplo: atributos en texto libre ensucian los filtros. | En admin, atributos técnicos como listas cerradas (enum) y normalización al guardar. | admin · Productos – AttributeEditor | 4 | S | — | aprovechar |

### X6 · Endress+Hauser – Promag W 400

Fuente: https://www.za.endress.com/en/field-instruments-overview/flow-measurement-product-overview/electromagnetic-flowmeter-promag-w400-5w4c

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X6-1 | promag-w400 | Pestañas Overview, Specifications, Downloads, Spare parts, Related, Configure; la pestaña queda en la URL (?t.tabId=product-downloads). | No se puede enlazar directo a las descargas de una ficha. | Pestañas de ficha con deep-link (#descargas) que se restauran al recargar. | frontend · ProductSheet – Tabs | 4 | M | Patrón tabs ARIA con flechas; contenido presente en el HTML (SEO). | adaptar |
| X6-2 | promag-w400 (Specs at a glance) | Bloque de 5 datos: error máx., rango de medición, temperatura, presión, materiales. | Las fichas de medidores no tienen resumen técnico. | Bloque 'Datos clave' en medidores electromagnéticos (DN, rango, precisión, IP, alimentación). | frontend · ProductSheet – KeySpecs | 5 | S | &lt;dl&gt;; unidades con abreviatura accesible. | aprovechar |
| X6-3 | promag-w400 (Downloads) | Filtro lateral por tipo de documento con conteo (Manuals and Datasheets 84, Approval 37…) y tarjetas con tipo, idioma, fecha de versión y 'otros idiomas/versiones'. | Los PDF no indican versión ni fecha. | Centro de descargas por ficha con tipo, versión, fecha e idioma; filtro por tipo cuando haya más de 6 documentos. | frontend · ProductSheet – DownloadCenter | 5 | M | Fecha en &lt;time&gt;. | adaptar |
| X6-4 | promag-w400 (acciones) | Acciones de página: Download as PDF, Share, Save to list, Compare. | No se puede guardar un producto para después. | 'Guardar en cotización' (carrito existente) y 'Compartir enlace' en la cabecera de la ficha. | frontend · ProductSheet – HeaderActions | 4 | S | Botones con texto, no solo icono. | adaptar |
| X6-5 | promag-w400 (alternativas) | 'Show alternatives' y 'Predecessor: Promag 50W…'. | Clientes con modelos antiguos no encuentran el reemplazo. | Campo 'Reemplaza a / Reemplazado por' en la ficha y en admin. | frontend · ProductSheet – Supersedes | 3 | S | — | adaptar |
| X6-6 | promag-w400 (precio) | 'Price after login' y carrito con login. | El modelo B2B de FUNDIGSAC no usa login público ni precio. | No aplicar. | frontend · — | 1 | S | — | descartar |
| X6-7 | promag-w400 Downloads (móvil) | En móvil: pestañas desplazables con flechas, botón 'Filter downloads' y breadcrumb compacto '&lt; Flow measurement'. | Las pestañas no caben en 390 px. | Pestañas con scroll horizontal y flechas; breadcrumb móvil reducido al nivel padre. | frontend · ProductSheet – MobileTabs | 4 | S | Las flechas no deben ser el único medio; se debe poder hacer swipe y usar teclado. | aprovechar |
| X6-8 | promag-w400 (cookies) | Banner con 'Accept only essential' al mismo nivel que 'Accept all'. | — | Igual que X4-4. | frontend · CookieBanner | 3 | S | Mismo peso visual. | aprovechar |

### X7 · GF Piping Systems – Catálogo

Fuente: https://www.gfps.com/en-us/products-solutions.catalog.html/fittings/couplers-sockets/~106921/753911817.html

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X7-1 | buscador typeahead | Panel de búsqueda federada: Sugerencias, Sistemas (3), Familias (2), Productos (1030) con miniatura y rango d/SDR, Descargas (266), Páginas (65), y 'See All Search Results'. | El buscador actual no separa productos, documentos y páginas. | Buscador del header con resultados agrupados (Productos con DN/SDR, Fichas PDF, Páginas) sobre un índice JSON estático. | frontend · Header – SearchCombobox | 5 | L | Debounce de 150 ms; combobox ARIA; índice cargado bajo demanda. | adaptar |
| X7-2 | ficha Coupler 753911817 | Selector de variante 'código – d 160, DN 150, PN 10' con paginación 1/7 y URL propia por variante. | Los accesorios de electrofusión tienen muchas medidas y hoy son una sola ficha. | Selector de variante (d/DN/SDR/PN) con URL por variante y código FUNDIGSAC visible. | frontend · ProductSheet – VariantSelect | 5 | M | &lt;select&gt; nativo o listbox ARIA; actualizar &lt;title&gt;. | adaptar |
| X7-3 | ficha Coupler | Stepper −/1/+ y 'Add to cart' hacia un carrito 'Request' con contador en el header, sin precio. | Valida el modelo del carrito de cotización. | Revisar el carrito: stepper accesible, contador en header con aria-live y variante elegida en la línea. | frontend · QuoteCart – AddButton | 5 | S | Botones −/+ con aria-label; input type=number con min=1. | aprovechar |
| X7-4 | ficha Coupler | 'Download datasheet' junto al título. | El PDF queda abajo. | Botón 'Ficha técnica PDF' en la cabecera de la ficha (tamaño del archivo visible). | frontend · ProductSheet – HeaderActions | 4 | S | — | aprovechar |
| X7-5 | ficha Coupler (Additional information) | Pestañas Measurements, Images, CAD, BIM, Documents; medidas d1, Lmax; 'Suitable for SDR pipe 9-26'. | No se indica con qué SDR es compatible un accesorio. | Línea 'Compatible con tubería SDR 9-26' y medidas d1/L en accesorios HDPE. | frontend · ProductSheet – Compatibility | 5 | S | — | aprovechar |
| X7-6 | ficha Coupler (móvil) | En móvil la tabla Code/d/DN/PN pasa a lista clave-valor. | Las tablas anchas se rompen en móvil. | Patrón responsive: tabla en escritorio y &lt;dl&gt; clave-valor en móvil para una sola variante. | frontend · ProductSheet – ResponsiveSpec | 4 | S | Mismo DOM semántico; sin duplicar contenido. | aprovechar |
| X7-7 | search.html (404) | 404 con 'Back to Homepage', 'Get in Touch' y 'Selection of our product portfolio' por categorías. | Ver X4-2. | 404 con familias y contacto. | frontend · NotFoundPage | 3 | S | — | aprovechar |
| X7-8 | cookies | 'Reject All' con el mismo peso que 'Accept All'. | — | Igual que X4-4. | frontend · CookieBanner | 2 | S | — | aprovechar |

### X8 · Cloudscape Design System (AWS)

Fuente: https://cloudscape.design/patterns/general/empty-states/

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X8-1 | patterns/general/empty-states | Distingue empty state (sin recursos: 'No distributions' + acción de crear) y zero results (filtro sin coincidencias: 'No matches' + 'Clear filter'). | Las tablas del admin y del historial de stock muestran el mismo mensaje en ambos casos. | Dos estados: 'Aún no hay reclamos' / 'Ningún resultado con estos filtros' + 'Limpiar filtros'. | admin · DataTable – EmptyState | 5 | S | El estado vacío ocupa toda la tabla (colspan) y se anuncia. | aprovechar |
| X8-2 | examples/react/table | Contador en el título 'Distributions (40)' y '0 matches' junto al filtro. | No se ve cuántos casos hay en cola. | Contador en el título de cada tabla y conteo de coincidencias junto al buscador. | admin · DataTable – Header | 4 | S | aria-live en el conteo filtrado. | aprovechar |
| X8-3 | examples/react/table | Orden por varias columnas con índices 1▲ 2▲ y 'Clear sort'. | La cola de reclamos requiere ordenar por vencimiento y luego por fecha. | Orden secundario en la cola de reclamos (plazo, luego fecha de ingreso) con 'Quitar orden'. | admin · Complaints – Queue | 3 | M | aria-sort en &lt;th&gt;. | adaptar |
| X8-4 | examples/react/table | Preferencias (engranaje): columnas visibles, tamaño de página, densidad. | Cada rol necesita columnas distintas. | Preferencias por usuario (columnas y densidad) guardadas en localStorage. | admin · DataTable – Preferences | 3 | M | — | adaptar |
| X8-5 | examples/react/table | Flashbar verde descartable 'Resource created successfully' sobre la tabla. | Tras guardar, el usuario no sabe si funcionó. | Mensaje de éxito persistente y descartable tras crear o editar (no toast efímero para acciones legales). | admin · Flash/Toast | 4 | S | role=status; no desaparecer antes de 5 s. | aprovechar |
| X8-6 | examples/react/table (móvil) | En 390 px: scroll horizontal con primera columna y columna Acciones fijas. | El admin en móvil oculta las acciones. | Columna ID y columna Acciones sticky en tablas del admin y del stock. | admin · DataTable – StickyColumns | 4 | M | Sombra indicadora de scroll; región enfocable. | aprovechar |
| X8-7 | empty-states (guía) | Valor vacío = guion '-'; no usar empty states para errores (usar flashbar). | Hoy se mezclan errores de red con 'sin datos'. | Convención: '-' para vacío y error con reintento separado del estado vacío. | admin · Guía de UI | 3 | S | — | aprovechar |

### X9 · Shopify Polaris – App Home patterns

Fuente: https://shopify.dev/docs/api/app-home/latest/patterns

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X9-1 | templates/details | Plantilla Details de dos columnas: principal editable, lateral con estado/metadatos/resumen; breadcrumb; acciones secundarias (Duplicar, Eliminar crítico). | El detalle de cotización/reclamo mezcla datos y estado. | Detalle a dos columnas: izquierda datos del cliente y del pedido; derecha estado, plazo legal, responsable y auditoría. | admin · Quote/Complaint – DetailPage | 5 | M | Orden DOM: contenido principal primero. | adaptar |
| X9-2 | templates/details | Secciones con heading, accessory (conteo), supplemental (estado) y acciones en el header de la sección. | Las acciones están lejos de lo que modifican. | Encabezado de sección con conteo y acciones locales (p. ej. 'Ítems (4) · Editar'). | admin · SectionHeader | 4 | S | Botones icono con nombre accesible. | aprovechar |
| X9-3 | compositions/index-table | Index table: búsqueda, popover de orden, acciones masivas con checkbox, clic de fila delegado al checkbox, paginación. | No hay acciones masivas (asignar, cerrar). | Selección múltiple con barra 'N seleccionados · Asignar · Exportar' en cotizaciones y consultas. | admin · DataTable – BulkActions | 4 | M | Checkbox con etiqueta por fila; confirmar acciones destructivas. | adaptar |
| X9-4 | templates/details (uso) | Caso de uso 'pages that require a save/discard workflow'. | Se pierden cambios al salir de la edición de usuario. | Barra 'Cambios sin guardar · Descartar · Guardar' en edición de usuario/rol. | admin · Users – EditForm SaveBar | 4 | M | Aviso beforeunload; foco al primer error. | adaptar |
| X9-5 | compositions/setup-guide | Checklist con progreso y pasos expandibles, descartable. | Usuarios nuevos del admin o del stock no saben por dónde empezar. | Guía de inicio para nuevos usuarios (cambiar clave, revisar rol, primera entrega). | admin · Onboarding – SetupGuide | 3 | M | Progreso con &lt;progress&gt; y texto. | adaptar |
| X9-6 | compositions (metrics card) | Metrics card para indicadores clave. | Falta un resumen al entrar. | Tarjetas: reclamos por vencer, cotizaciones nuevas, stock bajo. | admin · Dashboard – MetricCards | 3 | S | Número + etiqueta + tendencia en texto. | aprovechar |
| X9-7 | templates/details (a11y) | Botón de editar solo icono con accessibilityLabel. | Iconos sin nombre accesible. | Regla: todo botón de icono lleva aria-label descriptivo. | admin · Guía de UI | 4 | S | WCAG 4.1.2. | aprovechar |

### X10 · GitHub Primer

Fuente: https://primer.style/product/components/data-table/

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X10-1 | components/data-table | DataTable con rowHeader, título enlazado por aria-labelledby y fechas relativas ('5 minutes ago', 'yesterday'). | Las fechas absolutas largas cuestan de leer en el historial. | Fecha relativa con la absoluta en tooltip/&lt;time datetime&gt; en auditoría e historial de stock. | admin · AuditLog – Table | 4 | S | &lt;time&gt; con datetime ISO; zona America/Lima. | aprovechar |
| X10-2 | components/data-table | Anchos de columna grow, growCollapse y min/max por columna. | Las columnas de texto largo rompen la tabla. | Definir anchos mínimo/máximo por columna y truncado con title. | admin · DataTable – ColumnSizing | 3 | S | Texto truncado accesible completo. | aprovechar |
| X10-3 | components/data-table (móvil) | En 390 px la tabla queda en un contenedor con scroll horizontal y el resto de la página no se desborda. | — | Contenedor de tabla con overflow propio en todas las apps. | stock · Historial – Table | 3 | S | role=region + tabindex. | aprovechar |
| X10-4 | ui-patterns/degraded-experiences | Banner global 'warning' cuando falla un servicio; no mostrar un empty state si los datos existen pero no cargan, para que el usuario no crea que se perdieron. | Sin conexión o con Supabase caído, la app stock puede mostrar 'sin stock'. | En stock: banner 'Sin conexión — mostrando datos guardados a las HH:MM' y nunca 'sin datos' si la carga falló. | stock · AppShell – OfflineBanner | 5 | S | role=status; contraste AA. | aprovechar |
| X10-5 | ui-patterns/saving | Guardado explícito; no mezclar autosave y guardado manual en un formulario; preservar datos ante error; aviso de cambios sin guardar. | Las entregas de EPP con foto pueden perderse si falla el envío. | En entregas: botón explícito 'Registrar entrega', borrador local si falla y reintento sin perder la foto. | stock · Entregas – Form | 5 | M | Mensaje de error ligado al campo. | aprovechar |
| X10-6 | ui-patterns/saving (CTA) | Los CTA usan verbos activos: Create, Save, Delete, Update. | Hay botones 'Aceptar' u 'OK' ambiguos. | Verbos específicos: 'Registrar entrega', 'Guardar rol', 'Cerrar reclamo'. | admin · Guía de UX copy | 3 | S | — | aprovechar |

### X11 · GOV.UK Design System

Fuente: https://design-system.service.gov.uk/patterns/check-answers/

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X11-1 | patterns/check-answers | Página de revisión antes de enviar con 'Cambiar' por sección; los enlaces llevan texto oculto para lectores de pantalla. | El Libro de Reclamaciones se envía sin paso de revisión; error costoso legalmente. | Paso 'Revisa tu reclamo' con secciones y 'Cambiar', antes de 'Enviar reclamo'. | frontend · LibroReclamaciones – Review | 5 | M | 'Cambiar &lt;span class=sr-only&gt;datos del consumidor&lt;/span&gt;'. | aprovechar |
| X11-2 | patterns/confirmation-pages | Confirmación con número de referencia, qué pasa después y cuándo, contacto, enlace de feedback y forma de guardar (PDF). | Tras enviar un reclamo o una cotización no queda constancia clara. | Confirmación con código de hoja, plazo legal de respuesta, correo de constancia y botón 'Descargar constancia PDF'. | frontend · LibroReclamaciones – Confirmation | 5 | S | El panel verde no contiene enlaces (contraste). | aprovechar |
| X11-3 | components/error-summary | Resumen de errores al inicio del formulario con enlaces a cada campo. | Los formularios largos muestran errores dispersos. | Error summary en cotización, reclamo, login admin y entrega de stock. | frontend · Forms – ErrorSummary | 5 | S | Foco al resumen al enviar; role=alert. | aprovechar |
| X11-4 | patterns/check-answers (layout) | Layout de dos tercios para respuestas cortas (longitud de línea, lupa). | Formularios a ancho completo en escritorio. | Formularios públicos con ancho máximo ~66 ch. | frontend · Forms – Layout | 3 | S | Ayuda a usuarios con magnificador. | aprovechar |
| X11-5 | banner de cookies | 'Accept analytics cookies' y 'Reject analytics cookies' con el mismo estilo, más 'View cookies'. | Ver X4-4. | Banner con dos botones iguales. | frontend · CookieBanner | 3 | S | — | aprovechar |
| X11-6 | patterns/confirmation-pages (bookmark) | Los usuarios guardan la confirmación como recibo; la URL debe seguir funcionando. | El consumidor no puede consultar el estado de su reclamo. | URL de seguimiento con token no adivinable que muestra el estado (sin datos personales en la URL). | frontend · LibroReclamaciones – Tracking | 4 | M | Sin datos personales en query string. | adaptar |

### X12 · Carbon Design System – Status indicators

Fuente: https://www.carbondesignsystem.com/building-blocks/core/patterns/status-indicators

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X12-1 | patterns/status-indicators | Indicador de estado = icono + forma + color + etiqueta de texto. | Los plazos legales se marcan solo con color. | Estados de reclamo 'En plazo / Por vencer (≤3 días) / Vencido' con icono, forma y texto; stock 'Bajo / Agotado' igual. | admin · StatusBadge | 5 | S | WCAG 1.4.1 (no solo color). | aprovechar |
| X12-2 | status-indicators (consolidación) | Un estado consolidado toma el de mayor severidad. | Un producto con tallas tiene estados mixtos. | Estado del producto = peor talla (si una talla está agotada, el producto muestra 'Agotado parcial'). | stock · Stock – ProductRow | 4 | S | Texto explica cuál talla. | adaptar |
| X12-3 | status-indicators (badge) | Badge con número en la cabecera para novedades. | Las nuevas consultas no se notan. | Badge numérico en el menú del admin (Reclamos 3, Cotizaciones 5). | admin · Sidebar – CountBadge | 4 | S | El número va en el nombre accesible del enlace. | aprovechar |
| X12-4 | status-indicators (differential) | El indicador diferencial exige signo +/- o flecha, no solo color. | Entradas y salidas de stock solo diferenciadas por color. | Movimientos '+20 entrada' / '−3 entrega' con signo y flecha. | stock · Historial – MovementCell | 4 | S | Signo legible por lector de pantalla. | aprovechar |
| X12-5 | status-indicators (carga cognitiva) | No usar indicadores sin acción requerida; más de 5-6 abruma. | El dashboard puede saturarse de badges. | Máximo 5 tipos de estado por vista; texto plano para estados informativos. | admin · Guía de UI | 3 | S | — | aprovechar |

### X13 · GitHub Docs – Repository roles

Fuente: https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X13-1 | repository-roles … (Permissions for each role) | Tabla acciones × roles (Read, Triage, Write, Maintain, Admin) con ✓/✗; roles acumulativos. | La pantalla de roles no muestra qué permite cada rol. | Matriz de permisos solo lectura en Admin &gt; Roles: filas = acciones, columnas = roles, agrupada por módulo. | admin · Roles – PermissionMatrix | 5 | M | &lt;th scope&gt; en filas y columnas; caption. | adaptar |
| X13-2 | repository-roles (estructura) | Los roles se presentan del menor al mayor acceso y cada uno incluye al anterior. | Los roles actuales no tienen jerarquía visible. | Ordenar roles de menor a mayor privilegio y mostrar 'incluye todo lo de X'. | admin · Roles – RoleList | 4 | S | — | aprovechar |
| X13-3 | repository-roles (a11y) | Los permisos se marcan con caracteres ✓/✗ sin texto alternativo visible. | Los lectores pueden anunciar 'check mark' sin contexto. | Celdas con icono + texto sr-only 'Permitido'/'No permitido'. | admin · Roles – PermissionMatrix | 4 | S | WCAG 1.1.1. | adaptar |
| X13-4 | repository-roles (agrupación) | Las acciones se agrupan por área funcional en tablas separadas. | Una matriz grande cansa. | Grupos plegables: Cotizaciones, Consultas, Reclamos, Usuarios, Auditoría, Stock. | admin · Roles – PermissionMatrix | 4 | S | &lt;details&gt; por grupo. | aprovechar |
| X13-5 | repository-roles (ayuda) | La documentación explica cada rol en lenguaje claro. | Los administradores asignan roles sin entender el alcance. | Panel lateral 'Qué puede hacer este rol' al elegir un rol en la creación de usuario. | admin · Users – RoleHelp | 3 | S | Asociado con aria-describedby. | adaptar |
| X13-6 | banner de idioma | Banner 'This article is also available in Spanish'. | Sitio solo en español. | No aplica. | frontend · — | 1 | S | — | descartar |

### X14 · Sortly – Inventory features

Fuente: https://www.sortly.com/features/

| ID | Página | Observación | Problema FUNDIGSAC | Propuesta adaptada | App · componente | Imp. | Esf. | Perf/a11y | Decisión |
|---|---|---|---|---|---|---|---|---|---|
| X14-1 | features (Check-in/Check-out) | Check-in/check-out: quién tenía qué, cuándo y dónde. | El EPP retornable (arneses, cascos) no tiene devolución registrada. | Flujo 'Devolución' que cierra una entrega previa con estado del equipo. | stock · Entregas – Return | 4 | M | — | adaptar |
| X14-2 | features (Low Stock Alerts) | Alertas de stock bajo por umbral mínimo, in-app y por correo. | Las tallas se agotan sin aviso. | Mínimo por producto/talla y alerta en el dashboard y por correo semanal. | stock · Stock – MinThreshold | 5 | M | El estado bajo usa StatusBadge (X12-1). | aprovechar |
| X14-3 | features (Reports) | Reportes Item Flow (cambios de cantidad por periodo), Move Summary y Activity History por usuario. | El historial no responde '¿cuánto salió este mes?'. | Reporte de flujo por periodo y por trabajador con exportación CSV. | stock · Historial – FlowReport | 4 | M | Tabla accesible + resumen en texto. | adaptar |
| X14-4 | features (Offline Mobile Access) | Acceso móvil offline con sincronización automática. | El almacén tiene mala señal. | Cola local de operaciones con estado por registro (pendiente/sincronizado/conflicto) e icono global en el header. | stock · AppShell – SyncStatus | 5 | L | Idempotencia por id de operación; no perder fotos. | adaptar |
| X14-5 | features (Barcode & QR) | Escaneo de códigos de barras/QR desde el smartphone y etiquetas imprimibles. | Buscar un producto por nombre en el almacén es lento. | QR por producto/talla en el estante que abre la ficha de stock. | stock · Stock – QRLookup | 3 | L | Alternativa manual siempre disponible. | adaptar |
| X14-6 | features (Pick Lists) | Pick lists para reunir ítems. | Entregas a cuadrillas se registran una por una. | Lista de entrega por cuadrilla (varios trabajadores y productos) en un solo registro. | stock · Entregas – BatchDelivery | 3 | M | — | adaptar |
| X14-7 | features/item-check-in-check-out (404) | 404 simple con 'Back to Homepage'; footer en acordeón en móvil. | — | Footer en acordeón en móvil para el frontend. | frontend · Footer – MobileAccordion | 2 | S | Botones de acordeón con aria-expanded. | adaptar |

## 5. Top 10 por aplicación

### frontend

| # | ID | Propuesta | Componente | Imp. | Esf. |
|---|---|---|---|---|---|
| 1 | X1-2 | ProductCard con 4 atributos clave en lista &lt;dl&gt; y botón 'Añadir a cotización'. | ProductCard | 5 | S |
| 2 | X2-1 | Chips de filtros activos con 'x' y 'Restablecer todo' bajo la barra de filtros. | Catálogo – ActiveFilterChips | 5 | S |
| 3 | X5-7 | Estado vacío con el término, 3 consejos y familias destacadas. | SearchEmptyState | 5 | S |
| 4 | X6-2 | Bloque 'Datos clave' en medidores electromagnéticos (DN, rango, precisión, IP, alimentación). | ProductSheet – KeySpecs | 5 | S |
| 5 | X7-3 | Revisar el carrito: stepper accesible, contador en header con aria-live y variante elegida en la línea. | QuoteCart – AddButton | 5 | S |
| 6 | X7-5 | Línea 'Compatible con tubería SDR 9-26' y medidas d1/L en accesorios HDPE. | ProductSheet – Compatibility | 5 | S |
| 7 | X11-2 | Confirmación con código de hoja, plazo legal de respuesta, correo de constancia y botón 'Descargar constancia PDF'. | LibroReclamaciones – Confirmation | 5 | S |
| 8 | X11-3 | Error summary en cotización, reclamo, login admin y entrega de stock. | Forms – ErrorSummary | 5 | S |
| 9 | X1-1 | Barra de filtros en /productos agrupada en Aplicación (agua potable, saneamiento, agricultura, minería), Familia, Especificación (DN, PN, material, conexión) y Norma, con contador de resultados. | Catálogo /productos – FilterBar | 5 | M |
| 10 | X1-4 | Tabla de variantes por DN con &lt;caption&gt;, th scope y primera columna fija; scroll horizontal anunciado. | ProductSheet – VariantTable | 5 | M |

### admin

| # | ID | Propuesta | Componente | Imp. | Esf. |
|---|---|---|---|---|---|
| 1 | X8-1 | Dos estados: 'Aún no hay reclamos' / 'Ningún resultado con estos filtros' + 'Limpiar filtros'. | DataTable – EmptyState | 5 | S |
| 2 | X12-1 | Estados de reclamo 'En plazo / Por vencer (≤3 días) / Vencido' con icono, forma y texto; stock 'Bajo / Agotado' igual. | StatusBadge | 5 | S |
| 3 | X9-1 | Detalle a dos columnas: izquierda datos del cliente y del pedido; derecha estado, plazo legal, responsable y auditoría. | Quote/Complaint – DetailPage | 5 | M |
| 4 | X13-1 | Matriz de permisos solo lectura en Admin &gt; Roles: filas = acciones, columnas = roles, agrupada por módulo. | Roles – PermissionMatrix | 5 | M |
| 5 | X5-9 | En admin, atributos técnicos como listas cerradas (enum) y normalización al guardar. | Productos – AttributeEditor | 4 | S |
| 6 | X8-2 | Contador en el título de cada tabla y conteo de coincidencias junto al buscador. | DataTable – Header | 4 | S |
| 7 | X8-5 | Mensaje de éxito persistente y descartable tras crear o editar (no toast efímero para acciones legales). | Flash/Toast | 4 | S |
| 8 | X9-2 | Encabezado de sección con conteo y acciones locales (p. ej. 'Ítems (4) · Editar'). | SectionHeader | 4 | S |
| 9 | X9-7 | Regla: todo botón de icono lleva aria-label descriptivo. | Guía de UI | 4 | S |
| 10 | X10-1 | Fecha relativa con la absoluta en tooltip/&lt;time datetime&gt; en auditoría e historial de stock. | AuditLog – Table | 4 | S |

### stock

| # | ID | Propuesta | Componente | Imp. | Esf. |
|---|---|---|---|---|---|
| 1 | X10-4 | En stock: banner 'Sin conexión — mostrando datos guardados a las HH:MM' y nunca 'sin datos' si la carga falló. | AppShell – OfflineBanner | 5 | S |
| 2 | X10-5 | En entregas: botón explícito 'Registrar entrega', borrador local si falla y reintento sin perder la foto. | Entregas – Form | 5 | M |
| 3 | X14-2 | Mínimo por producto/talla y alerta en el dashboard y por correo semanal. | Stock – MinThreshold | 5 | M |
| 4 | X14-4 | Cola local de operaciones con estado por registro (pendiente/sincronizado/conflicto) e icono global en el header. | AppShell – SyncStatus | 5 | L |
| 5 | X12-2 | Estado del producto = peor talla (si una talla está agotada, el producto muestra 'Agotado parcial'). | Stock – ProductRow | 4 | S |
| 6 | X12-4 | Movimientos '+20 entrada' / '−3 entrega' con signo y flecha. | Historial – MovementCell | 4 | S |
| 7 | X3-6 | Barra de navegación inferior en la app stock (Stock, Entregas, Historial, Más). | AppShell – BottomNav | 4 | M |
| 8 | X14-1 | Flujo 'Devolución' que cierra una entrega previa con estado del equipo. | Entregas – Return | 4 | M |
| 9 | X14-3 | Reporte de flujo por periodo y por trabajador con exportación CSV. | Historial – FlowReport | 4 | M |
| 10 | X10-3 | Contenedor de tabla con overflow propio en todas las apps. | Historial – Table | 3 | S |

## 6. Análisis de brechas

**Bien cubierto.** Catálogo y ficha técnica (filtros con conteo, chips, variantes por DN/SDR, centro de descargas, carrito de solicitud sin precio). Formularios públicos con efecto legal (revisión, resumen de errores, confirmación con código). Tablas densas del admin (estados vacíos, contadores, columnas fijas, acciones masivas).

**Cobertura parcial.**

- *Stock móvil offline.* Sortly confirma las funciones (check-in/out, alertas de stock bajo, offline, escaneo), pero solo desde una página de marketing; la app real requiere cuenta. La guía de Microsoft Dynamics 365 Field Service sobre el icono de sincronización en el header (sincronizando, cambios pendientes, sin conexión) se conoce solo por el resultado de búsqueda: el navegador bloqueó learn.microsoft.com. Antes de implementar X14-4, conviene validarla con un prototipo propio o con una demo pública navegable.
- *UI de permisos.* GitHub Docs muestra la matriz como documentación, no como pantalla editable. Falta una referencia pública de editor de roles (asignar y quitar permisos con confirmación y auditoría). Se propone diseñarlo combinando X13-1 (matriz), X9-4 (barra guardar/descartar) y X10-5 (guardado explícito).
- *Cola de reclamos con plazo legal.* Carbon y Cloudscape cubren estados y orden, pero ningún sitio visitado muestra un contador de SLA en la fila. Las búsquedas apuntan a ServiceNow y Zoho Desk, que tienen documentación pública pero no demos navegables. Se propone StatusBadge (X12-1) con días hábiles restantes calculados en el servidor.

**No verificado.** Móvil de Saint-Gobain PAM (verificación anti-bot), Shopify Polaris y Carbon (solo escritorio), GitHub Docs a 390 px (la emulación reportó un innerWidth de 764 px). Ningún sitio se midió con Lighthouse; las notas de rendimiento son recomendaciones, no mediciones.

**Riesgos al adaptar.** Los carruseles (BERMAD) y los clones en el DOM perjudican la accesibilidad. Un buscador federado (X7-1) puede aumentar el JS inicial: conviene cargar el índice bajo demanda. Un zip de descargas (X1-5) requiere backend y queda para una fase posterior.

Archivo de ideas en formato tabular: `03-inspiration-parts/external-ideas.csv`.
