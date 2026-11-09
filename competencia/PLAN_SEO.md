# Plan SEO de FUNDIGSAC para cobertura nacional en Perú

Fecha: 9 de noviembre de 2026.

Base del plan: `Report/competencia/INFORME_COMPETENCIA.md`. Las referencias V-01 a V-25 corresponden a la lista "requiere validación de FUNDIGSAC" de la sección 10 del informe.

## 1. Reglas del plan

1. **No se publica nada inventado.** Certificaciones, cifras, precios, stock, plazos, clientes u homologaciones requieren documento. Lo que no lo tenga queda en la lista de validación (sección 11 de este plan y sección 10 del informe).
2. **`modules/catalog/data.ts` no es fuente.** Es un dataset de maqueta. Las fuentes válidas son `valve-sheets.ts`, las fichas FT y la lista de precios de `lib/catalog-pdf.ts`, siempre tras revisión técnica.
3. **Toda corrección mide todos los KPI y queda en verde.** El comando y los umbrales están en la sección 9. Un KPI sin medir no cuenta como aprobado.
4. **El sitio sigue en `noindex` hasta completar el checklist de la sección 10.**
5. **Sin volumen de búsqueda.** Esta revisión no tiene datos de volumen ni de posiciones reales. La prioridad sale de las líneas de negocio y de las 20 búsquedas del informe, y debe corregirse con datos de Search Console.

Situación de partida: 28 URL en el sitemap, 10 fichas indexables (todas de válvulas), dominio `fundigsac.com` todavía en WordPress y KPI de móvil en rojo.

## 2. Arquitectura de URL

```text
/                                         portada nacional
/productos                                catálogo general
/productos/valvulas                       familia
/productos/valvulas/{ficha}               ficha
/productos/tuberias                       familia
/productos/tuberias/{ficha}               ficha (nueva)
/productos/marcos-y-tapas                 familia
/productos/marcos-y-tapas/{ficha}         ficha (nueva)
/productos/conexiones                     familia (nueva)
/productos/conexiones/{ficha}             ficha (nueva)
/productos/acoples-y-bridas               familia (nueva)
/productos/acoples-y-bridas/{ficha}       ficha (nueva)
/industrias/{sector}                      saneamiento, minería, agricultura
/productos/hdpe                           familia condicionada a decisión comercial
/productos/equipos-termofusion            familia condicionada a decisión comercial
/productos/medidores                      familia condicionada a decisión comercial
/guias/{tema}                             contenido técnico (nuevo)
/cobertura                                despachos a regiones (nuevo)
/cobertura/{region}                       solo con evidencia real
/contacto y /cotizar                      conversión
```

Notas de implementación:

- No usar `/recursos` para las guías: `next.config.ts` redirige esa ruta a `/contacto`.
- No crear URL por filtro DN o PN salvo que exista una consulta con demanda demostrada y contenido propio.
- `CategorySlug` admite hoy solo tres valores. Las familias nuevas requieren ampliar el registro y crear sus rutas.
- Un cambio de slug publicado exige redirección permanente.

## 3. Mapa de palabras clave y URL

Estado: **Existe** (la URL ya es indexable), **Nueva** (la URL debe crearse), **Bloqueada** (no publicar hasta validar). Evidencia: identificador de la búsqueda en el informe, ficha de competidor o referencia del catálogo propio. "Lista de precios" y "tarjeta de la familia" prueban que el producto figura en Frontend, no que haya demanda.

| Prioridad | Tema | Palabra principal | Variantes | Intención | URL destino | Estado | Evidencia | Validar |
|---|---|---|---|---|---|---|---|---|
| P0 | Marca | fundigsac | fundigsac perú, fundigsac válvulas | Marca | `/` | Existe | Q20 | V-07 |
| P0 | General | válvulas de hierro dúctil perú | válvulas industriales perú | Comercial | `/productos/valvulas` | Existe | Q17 | V-11 |
| P0 | Compuerta | válvula compuerta hierro dúctil | válvula compuerta bridada | Comercial | `/productos/valvulas/valvula-compuerta-fundigsac` | Existe | Q1, Q2 | V-08 |
| P0 | Compuerta | válvula compuerta bridada pn16 lima | proveedor válvula compuerta lima | Comercial local | `/productos/valvulas/valvula-compuerta` | Existe | Q2 | V-08, V-16 |
| P0 | Compuerta | válvula compuerta garantía | válvula compuerta garantía extendida | Comercial | `/productos/valvulas/valvula-compuerta-fundigsac-garantia-extendida` | Existe | Línea propia | V-09, V-10 |
| P0 | Compuerta HDPE | válvula compuerta acerrojada | válvula compuerta para tubería hdpe | Comercial | `/productos/valvulas/valvula-compuerta-acerrojada` | Existe | Q12 | Revisión técnica |
| P0 | Compuerta PVC | válvula compuerta luflex | válvula embone, espiga campana | Comercial | `/productos/valvulas/valvula-embone-tipo-luflex` | Existe | Fichas de Collaval y Citaly | Revisión técnica |
| P0 | Check | válvula check hierro dúctil | válvula check swing, válvula de retención | Comercial | `/productos/valvulas/valvula-check-swing` | Existe | Q4 | Revisión técnica |
| P0 | Check | válvula check flex | check disco flexible, check silenciosa | Comercial | `/productos/valvulas/valvula-check-flex` | Existe | Q4 | Revisión técnica |
| P0 | Regulación | válvula reductora de presión | reguladora de presión hierro dúctil | Comercial | `/productos/valvulas/valvula-reductora-de-presion` | Existe | Q11 | Revisión técnica |
| P0 | Regulación | válvula de alivio bridada | válvula de alivio de presión | Comercial | `/productos/valvulas/valvula-de-alivio-bridada` | Existe | Lista de precios | Revisión técnica |
| P0 | Regulación | válvula flotadora bridada | válvula control de nivel, válvula flotador | Comercial | `/productos/valvulas/valvula-flotadora-bridada` | Existe | Q18 | Revisión técnica |
| P0 | Mariposa | válvula mariposa hierro dúctil | válvula mariposa wafer, con timón, con palanca | Comercial | `/productos/valvulas/valvula-mariposa-wafer` | Nueva | Q3 | V-17 |
| P0 | Aire | válvula de aire triple efecto | ventosa trifuncional, válvula de aire 3 funciones | Comercial | `/productos/valvulas/valvula-de-aire-triple-funcion` | Nueva | Q5 | V-17 |
| P0 | Tubería | tubería hierro dúctil k9 | tubería c40, k7, tubo hierro dúctil, tubería fundición dúctil | Comercial | `/productos/tuberias/tuberia-hierro-ductil-c40-k9-k7` | Nueva | Q6, Q7 | V-13 |
| P0 | Tubería | tubería hierro dúctil iso 2531 | ntp iso 2531 tubería | Comercial técnica | `/productos/tuberias/tuberia-hierro-ductil-c40-k9-k7` | Nueva | Q7 | V-13 |
| P0 | Tubería | tuberías de hierro dúctil perú | proveedor tubería hierro dúctil | Comercial | `/productos/tuberias` | Existe | Q6 | V-18 |
| P0 | Tapas | marco y tapa de buzón d400 | tapa de buzón hierro dúctil | Comercial | `/productos/marcos-y-tapas` | Existe | Q8, Q9 | V-14 |
| P0 | Tapas | marco y tapa d400 doble seguro | tapa buzón 2 seguros 600 mm | Comercial | `/productos/marcos-y-tapas/marco-y-tapa-d400-2-seguros` | Nueva | Q8, Q9 | V-14 |
| P0 | Tapas | marco y tapa d400 un seguro | tapa buzón liviana | Comercial | `/productos/marcos-y-tapas/marco-y-tapa-d400-1-seguro` | Nueva | Q8 | V-14 |
| P1 | Rejillas | rejilla pluvial hierro dúctil | rejilla de sumidero perú | Comercial | `/productos/marcos-y-tapas/rejilla-pluvial` | Nueva | Q10; fichas de FUMOSAC e ICOFESA | V-14 |
| P1 | Tapas | tapa circular hierro dúctil | tapa redonda de buzón | Comercial | `/productos/marcos-y-tapas` | Existe | Q9; tarjeta de la familia | V-14, V-24 |
| P1 | Tapas | tapa para válvula | tapa para caja de válvulas, marco y tapa caja de válvulas | Comercial | `/productos/marcos-y-tapas` | Existe | Ficha de FUMOSAC; tarjeta de la familia | V-24 |
| P1 | Tapas | marco rectangular hierro dúctil | marco cuadrado hierro dúctil | Comercial | `/productos/marcos-y-tapas` | Existe | Fichas de FUMOSAC y Negofer; tarjeta de la familia | V-24 |
| P1 | Tapas | tapa de registro hierro dúctil | tapa cámara de inspección | Comercial | `/productos/marcos-y-tapas` | Existe | Tarjeta de la familia | V-24 |
| P1 | Tubería | tubería hierro dúctil unión junta | tubo espiga campana, tubería push-on | Comercial | `/productos/tuberias` | Existe | Q6; ficha de Negofer; tarjeta de la familia | V-13, V-24 |
| P1 | Tubería | tubería hierro dúctil unión mecánica | unión mecánica tubería hierro dúctil | Comercial | `/productos/tuberias` | Existe | Tarjeta de la familia | V-24 |
| P1 | Tubería | tubería hierro dúctil con bridas | tubo bridado hierro dúctil | Comercial | `/productos/tuberias` | Existe | `COMPETIDORES.md` (Kallpa); tarjeta de la familia | V-24 |
| P1 | Tubería | tubería con revestimiento de mortero de cemento | tubería revestida hierro dúctil | Comercial técnica | `/productos/tuberias` | Existe | Ficha de EATHISA; tarjeta de la familia | V-24 |
| P1 | Conexiones | conexiones bridadas hierro dúctil | accesorios hierro dúctil | Comercial | `/productos/conexiones` | Nueva | Q13 | Revisión técnica |
| P1 | Conexiones | tee bridada hierro dúctil | tee con reducción bridada | Comercial | `/productos/conexiones/tee-bridada` | Nueva | Q13 | Revisión técnica |
| P1 | Conexiones | yee bridado hierro dúctil | yee bridada | Comercial | `/productos/conexiones/yee-bridado` | Nueva | Q13 | Revisión técnica |
| P1 | Conexiones | tee luflex con brida | tee embone con derivación bridada | Comercial | `/productos/conexiones/tee-luflex-brida` | Nueva | Ficha de Negofer (Luflex Embone); lista de precios (TLB) | Revisión técnica |
| P1 | Conexiones | tubería sch-40 | codo sch40 90 grados, codo sch40 45 grados | Comercial | `/productos/conexiones/tuberia-y-codos-sch40` | Nueva | Ficha de Negofer; lista de precios (TSCH40, CSCH90, CSCH45) | Revisión técnica |
| P1 | Acoples | adaptador brida hdpe | adaptador brida tubo hdpe, adaptador rápido | Comercial | `/productos/acoples-y-bridas/adaptador-brida-hdpe` | Nueva | Q12 | Revisión técnica |
| P1 | Acoples | unión de desmontaje autoportante | unión autoportante | Comercial | `/productos/acoples-y-bridas/union-de-desmontaje-autoportante` | Nueva | Fichas de Citaly y EATHISA | Revisión técnica |
| P1 | Acoples | acople gran rango | adaptador brida gran rango, unión dresser | Comercial | `/productos/acoples-y-bridas/acople-gran-rango` | Nueva | Fichas de FUMOSAC y Citaly | Revisión técnica |
| P1 | Acoples | acople acerrojado hdpe | anillo acerrojado, adaptador acerrojado hdpe | Comercial | `/productos/acoples-y-bridas/acople-acerrojado-hdpe` | Nueva | Fichas de Collaval y Citaly; lista de precios (AAPTH, AACER) | Revisión técnica |
| P1 | Acoples | acople 995 | acople 995 hdpe | Comercial | `/productos/acoples-y-bridas/acople-995` | Nueva | Fichas de Citaly e Hi Perú; lista de precios (A995PTH) | Revisión técnica |
| P1 | Acoples | junta flexible bridada | junta flexible din, junta flexible ansi, junta de expansión | Comercial | `/productos/acoples-y-bridas/junta-flexible` | Nueva | Fichas de Leoneblu e ICOFESA; lista de precios (JFDIN, JFANSI) | Revisión técnica |
| P1 | Bridas | bridas para redes de agua | brida plana pn16, brida ansi, brida roscada | Comercial | `/productos/acoples-y-bridas/bridas` | Nueva | Fichas de Negofer, Mecka y EATHISA; lista de precios (BISO, BANSI, BROSCA) | V-25 |
| P1 | Bridas | brida ciega | brida ciega pn16 | Comercial | `/productos/acoples-y-bridas/brida-ciega` | Nueva | Fichas de Negofer y Mecka; lista de precios (BCIEGA) | V-25 |
| P1 | Check | válvula dúo check wafer | dúo check hierro dúctil | Comercial | `/productos/valvulas/valvula-duo-check-wafer` | Nueva | Q4 | Revisión técnica |
| P1 | Check | válvula check vertical cierre silencioso | check vertical, check de cierre silencioso | Comercial | `/productos/valvulas/valvula-check-vertical-cierre-silencioso` | Nueva | Fichas de Mecka y Rivali; lista de precios (VCVER) | Revisión técnica |
| P1 | Mariposa | válvula mariposa paleta inox | mariposa inox con palanca, mariposa inox con timón | Comercial | `/productos/valvulas/valvula-mariposa-paleta-inox` | Nueva | Lista de precios (MINOXP, MINOXT) | V-17 |
| P1 | Aire | válvula de aire roscada | ventosa roscada | Comercial | `/productos/valvulas/valvula-de-aire-roscada` | Nueva | Lista de precios (VDAR) | V-17 |
| P1 | Regulación | piloto válvula reductora de presión | piloto válvula de alivio | Comercial | `/productos/valvulas/valvula-reductora-de-presion` | Existe | Lista de precios (pilotos) | Revisión técnica |
| P1 | Filtros | filtro tipo y bridado | filtro y hierro dúctil, strainer | Comercial | `/productos/valvulas/filtro-tipo-y-bridado` | Nueva | Fichas de FUMOSAC, Mecka y Collaval. CTPS-ET-034 trata del filtro tipo cesto, no del Y | Revisión técnica |
| P1 | Guillotina | válvula guillotina | válvula cuchilla | Comercial | `/productos/valvulas/valvula-guillotina` | Nueva | Q14 | V-17 |
| P1 | Saneamiento | hierro dúctil para saneamiento | válvulas para agua potable | Comercial | `/industrias/saneamiento` | Existe | Q16 | V-13, V-14, V-19 |
| P1 | Saneamiento | válvulas para alcantarillado | componentes para plantas de tratamiento, redes de agua potable | Comercial | `/industrias/saneamiento` | Existe | Contenido del sector; Q16 | V-13, V-14, V-19 |
| P1 | Minería | válvulas para minería perú | válvulas para agua de proceso | Comercial | `/industrias/mineria` | Existe | Q14 | V-20, V-23 |
| P1 | Minería | válvulas para agua de proceso minería | recirculación minera, planta concentradora | Comercial | `/industrias/mineria` | Existe | Contenido del sector; Q14 | V-20, V-23 |
| P1 | Agricultura | válvulas para riego agrícola | válvulas hierro dúctil riego | Comercial | `/industrias/agricultura` | Existe | Q15 | V-18, revisión técnica |
| P1 | Agricultura | ventosa para riego | válvula de aire para riego | Comercial | `/industrias/agricultura` | Existe | Contenido del sector; Q15 | V-17 |
| P1 | Agricultura | filtro y para riego | filtro y bridado riego | Comercial | `/industrias/agricultura` | Existe | Contenido del sector; Q15 | Revisión técnica |
| P1 | Agricultura | tubería hdpe para riego | válvula de retención para riego | Comercial | `/industrias/agricultura` | Existe | Contenido del sector; Q15 | V-18 |
| P1 | Local | cotización válvulas lima | proveedor válvulas cercado de lima | Local | `/contacto` | Existe | Q2, Q4 | V-02, V-03, V-04 |
| P1 | Nacional | envío válvulas a regiones | proveedor válvulas arequipa, trujillo, piura | Local | `/cobertura` | Nueva | Q19 | V-06 |
| P1 | Guía | diferencia entre k7 k9 y c40 | clases tubería hierro dúctil | Informativa | `/guias/clases-tuberia-hierro-ductil` | Nueva | Q6, Q7 | V-13 |
| P1 | Guía | clases en 124 d400 c250 | clase de carga tapa de buzón | Informativa | `/guias/clases-de-carga-en-124` | Nueva | Q8 | V-14 |
| P1 | Guía | cómo elegir válvula de aire | ventosa trifuncional para qué sirve | Informativa | `/guias/como-elegir-valvula-de-aire` | Nueva | Q5 | V-17 |
| P1 | Guía | compuerta para hdpe o pvc | conexión hierro dúctil a hdpe | Informativa | `/guias/valvula-compuerta-para-hdpe-y-pvc` | Nueva | Q12 | Revisión técnica |
| P2 | SEDAPAL | válvula compuerta ctps-et-013 | especificación sedapal válvula compuerta | Técnica | `/guias/especificaciones-sedapal-valvulas` | Bloqueada | Q16 | V-19 |
| P2 | Regional | válvulas hierro dúctil arequipa | proveedor sedapar | Local | `/cobertura/arequipa` | Bloqueada | Q19 | V-06, V-20 |
| P2 | Regional | válvulas hierro dúctil trujillo | proveedor sedalib | Local | `/cobertura/la-libertad` | Bloqueada | Q19 | V-06, V-20 |
| P2 | Regional | válvulas hierro dúctil piura | proveedor eps grau | Local | `/cobertura/piura` | Bloqueada | Q19 | V-06, V-20 |
| P2 | Minería | válvulas para relaves y pulpas | válvula para pulpas, válvula para lodos minería | Comercial | `/industrias/mineria` | Bloqueada | Q14 | V-23 |
| P2 | Mariposa | válvula mariposa actuador neumático | mariposa neumática inox | Comercial | `/productos/valvulas/valvula-mariposa-actuador-neumatico` | Bloqueada | Lista de precios (MCAN) | V-17 |
| P2 | Tubería HDPE | tubería hdpe perú | tubo hdpe para agua | Comercial | `/productos/tuberias` | Bloqueada | Ficha de Hi Perú; Q12 | V-18 |
| P2 | HDPE | accesorios hdpe termofusión | conexiones hdpe perú, codo, tee, yee, cruz, reducción y tapón hdpe, flange, brida backing ring | Comercial | `/productos/hdpe` | Bloqueada | Q12 | Decisión comercial |
| P2 | Equipos | máquina de termofusión | soldadora hdpe, máquina termofusión 4 mordazas | Comercial | `/productos/equipos-termofusion` | Bloqueada | Fichas de Hi Perú y Leoneblu; lista de equipos | Decisión comercial |
| P2 | Equipos | máquina de electrofusión | equipo electrofusión hdpe | Comercial | `/productos/equipos-termofusion` | Bloqueada | Fichas de Hi Perú y Leoneblu; lista de equipos | Decisión comercial |
| P2 | Medición | medidor woltman | medidor electromagnético | Comercial | `/productos/medidores` | Bloqueada | Competidores | Decisión comercial |

### 3.1 Comprobación de cobertura

Cruce del mapa con `lib/catalog.ts`, `lib/catalog-pdf.ts`, `modules/catalog/registry.tsx` y las tarjetas de familia. Hidrantes no figura: solo lo menciona el asistente con datos de maqueta (V-12).

| Familia o sector en Frontend | Referencias | Temas del mapa |
|---|---|---|
| Válvulas de compuerta | 5 fichas, VBBH, VBBL | Compuerta, Compuerta HDPE, Compuerta PVC |
| Válvulas check | Swing, flex, VCVER, VDCW | Check |
| Válvulas mariposa | 6 modelos | Mariposa |
| Válvulas de aire | VDAP, VDAR | Aire |
| Regulación, guillotina y filtros | Reductora, alivio, flotadora, pilotos, guillotina, FYB | Regulación, Guillotina, Filtros |
| Tubería de hierro dúctil | THD y 5 tarjetas | Tubería |
| Tubería HDPE | Tarjeta sin código | Tubería HDPE |
| Marcos, tapas y rejillas | 2SEG, 1SEG y 6 tarjetas | Tapas, Rejillas |
| Conexiones | TBB, TLB, YBB, SCH-40 | Conexiones |
| Acoples y uniones | 11 referencias | Acoples |
| Bridas | BISO, BCIEGA, BANSI, BROSCA | Bridas |
| Accesorios HDPE | 11 referencias | HDPE |
| Equipos de termofusión | 8 referencias | Equipos |
| Medidores | MELEC, MWOL | Medición |
| Saneamiento, minería y agricultura | 3 sectores | Saneamiento (2 filas), Minería (3), Agricultura (4) |

Términos que deben aparecer de forma natural para cubrir sinónimos: "ventosa" y "válvula de aire"; "tapa de buzón" y "marco y tapa"; "tubo" y "tubería"; "hierro dúctil" y "fundición dúctil"; "brida" y "bridado"; "embone" y "espiga campana".

## 4. Cobertura nacional

Se trabaja en tres capas. Solo las dos primeras se pueden ejecutar ya.

1. **Intención nacional.** Portada, familias y fichas apuntan a "en Perú". Es la capa de mayor alcance y no requiere páginas nuevas por región.
2. **Lima.** `/contacto`, Business Profile y `LocalBusiness` atienden las consultas locales con la dirección validada.
3. **Regiones.** `/cobertura` publica cómo se despacha a regiones: ciudades o agencias, plazos reales y condiciones. Debe enlazar a las familias y a `/cotizar`.

Regla para `/cobertura/{region}`: se publica solo con al menos una entrega u obra real y autorizada, datos propios de esa región y texto que no se reutilice en otra página. Sin eso, una página por ciudad es contenido duplicado y resta calidad al sitio. No se observaron páginas regionales en ningún competidor analizado, así que no hay urgencia competitiva. La muestra es parcial y no incluye a las empresas sin rastrear.

Orden sugerido cuando exista evidencia (**hipótesis comercial**, no indica relación con ninguna entidad):

| Macrorregión | Regiones | Motivo | EPS de referencia para la búsqueda |
|---|---|---|---|
| Sur | Arequipa, Moquegua, Cusco, Tacna | Minería y saneamiento | SEDAPAR, EPS Moquegua, SEDACUSCO, EPS Tacna |
| Norte | La Libertad, Piura, Lambayeque, Áncash, Cajamarca | Agroindustria, minería y saneamiento | SEDALIB, EPS Grau, EPSEL, SEDACHIMBOTE |
| Centro | Ica, Junín, Pasco | Agroindustria y minería | EMAPICA, SEDAM Huancayo |
| Oriente | Loreto, San Martín, Ucayali | Saneamiento | SEDALORETO, EMAPA San Martín |

Los nombres de EPS y la vocación productiva de cada región son conocimiento general. No salen del rastreo ni de las búsquedas, y deben confirmarse con el registro de SUNASS antes de usarse en un contenido.

## 5. Títulos y meta descripciones

Los títulos están escritos tal como se mostrarán, con marca. Longitud objetivo: título de hasta 60 caracteres y descripción de 120 a 158. Para los títulos con marca incluida se usa `title: { absolute: ... }`, porque la plantilla ya añade "| FUNDIGSAC".

Las columnas T y D indican caracteres. "Condición" es lo que debe validarse antes de publicar ese texto.

### 5.1 Rutas existentes

| Ruta | Título | T | Meta descripción | D | Condición |
|---|---|---:|---|---:|---|
| `/` | Válvulas y tuberías de hierro dúctil en Perú \| FUNDIGSAC | 56 | Válvulas, tubería de hierro dúctil, marcos y tapas para agua y saneamiento. Revisa cada ficha técnica y solicita tu cotización a FUNDIGSAC desde Lima. | 150 | V-07 |
| `/productos` | Catálogo de válvulas, tuberías y tapas \| FUNDIGSAC | 50 | Catálogo FUNDIGSAC de válvulas, tubería de hierro dúctil, marcos y tapas para redes de agua y alcantarillado. Consulta medidas y pide tu cotización. | 148 | Fichas nuevas |
| `/productos/valvulas` | Válvulas de hierro dúctil en Perú \| FUNDIGSAC | 45 | Válvulas de compuerta, check, reductoras, de alivio y flotadoras de hierro dúctil. Consulta DN, PN y materiales en cada ficha y solicita tu cotización. | 151 | V-11 |
| `/productos/tuberias` | Tubería de hierro dúctil C40, K9 y K7 \| FUNDIGSAC | 49 | Tubería de hierro dúctil clases C40, K9 y K7 para redes de agua potable y alcantarillado. Consulta diámetros disponibles y solicita tu cotización. | 146 | V-13, V-18 |
| `/productos/marcos-y-tapas` | Marcos y tapas de buzón D400 en Perú \| FUNDIGSAC | 48 | Marcos y tapas de buzón clase D400 de 600 mm con uno o dos seguros, para vías y redes de alcantarillado. Compara modelos y solicita tu cotización. | 146 | V-14 |
| `/productos/valvulas/valvula-compuerta` | Válvula de compuerta bridada DN40 a DN600 \| FUNDIGSAC | 53 | Válvula de compuerta de cierre elástico H-ITALY con extremos bridados, DN40 a DN600 y PN10/PN16. Revisa la ficha técnica y cotiza con FUNDIGSAC en Lima. | 152 | V-08, V-16 |
| `/productos/valvulas/valvula-compuerta-fundigsac` | Válvula de compuerta FUNDIGSAC DN50 a DN600 PN10/PN16 | 53 | Válvula de compuerta bridada FUNDIGSAC de asiento resiliente, DN50 a DN600 y PN10/PN16, en hierro dúctil GGG50 para redes de agua. Cotiza desde Lima. | 149 | V-08 |
| `/productos/valvulas/valvula-compuerta-fundigsac-garantia-extendida` | Válvula de compuerta FUNDIGSAC con garantía extendida | 53 | Válvula de compuerta FUNDIGSAC con garantía extendida: cierre elástico, extremos bridados, DN40 a DN600 y PN10/PN16 en hierro dúctil. Cotiza desde Lima. | 152 | V-08, V-10 |
| `/productos/valvulas/valvula-check-swing` | Válvula check swing hierro dúctil DN50-DN300 \| FUNDIGSAC | 56 | Válvula de retención check swing de hierro dúctil con bridas ISO PN16, DN50 a DN300, para bombeo, impulsión y redes de agua. Solicita tu cotización. | 148 | Revisión técnica |
| `/productos/valvulas/valvula-check-flex` | Válvula check flex hierro dúctil DN50-DN300 \| FUNDIGSAC | 55 | Válvula check flex de hierro dúctil con disco flexible de EPDM y bridas ISO PN16, DN50 a DN300. Cierre automático para bombeo y redes de agua. | 142 | Revisión técnica |
| `/productos/valvulas/valvula-reductora-de-presion` | Válvula reductora de presión DN50-DN350 \| FUNDIGSAC | 51 | Válvula reductora de presión DN50 a DN350 para mantener estable la presión aguas abajo en redes de agua potable, riego e industria. Cotiza desde Lima. | 150 | Revisión técnica |
| `/productos/valvulas/valvula-compuerta-acerrojada` | Válvula compuerta acerrojada para HDPE \| FUNDIGSAC | 50 | Válvula de compuerta acerrojada de hierro dúctil con cuña de EPDM y clase ISO PN16, para tubería HDPE de 63 a 315 mm (DN50 a DN300). Cotiza desde Lima. | 151 | Revisión técnica |
| `/productos/valvulas/valvula-embone-tipo-luflex` | Válvula compuerta embone Luflex DN50-DN300 \| FUNDIGSAC | 54 | Válvula de compuerta de embone tipo Luflex (espiga-campana) en hierro dúctil, cuña de EPDM y clase ISO PN16, DN50 a DN300, para redes de agua. | 142 | Revisión técnica |
| `/productos/valvulas/valvula-de-alivio-bridada` | Válvula de alivio bridada DN50 a DN300 \| FUNDIGSAC | 50 | Válvula de alivio bridada de hierro dúctil, DN50 a DN300 y hasta 16 bar: protege la red de sobrepresiones y golpes de ariete en bombeo y agua potable. | 150 | Revisión técnica |
| `/productos/valvulas/valvula-flotadora-bridada` | Válvula flotadora bridada DN50 a DN400 \| FUNDIGSAC | 50 | Válvula flotadora bridada de hierro dúctil, DN50 a DN400 y PN10/PN16: controla el nivel de tanques, cisternas y reservorios sin reboses. Cotiza en Lima. | 152 | Revisión técnica |
| `/industrias` | Válvulas y hierro dúctil por sector en Perú \| FUNDIGSAC | 55 | Componentes FUNDIGSAC para saneamiento, minería y agricultura en Perú: válvulas, tubería de hierro dúctil, acoples y soluciones para cada aplicación. | 149 | Ninguna |
| `/industrias/saneamiento` | Hierro dúctil para agua y saneamiento \| FUNDIGSAC | 49 | Válvulas de compuerta, marcos y tapas, tuberías y acoples de hierro dúctil para redes de agua potable, alcantarillado y plantas de tratamiento en Perú. | 151 | V-13, V-14 |
| `/industrias/mineria` | Válvulas y tuberías para minería en Perú \| FUNDIGSAC | 52 | Válvulas de compuerta, tuberías, acoples y bridas FUNDIGSAC de hierro dúctil para agua de proceso y control de fluidos en operaciones mineras del Perú. | 151 | V-20 |
| `/industrias/agricultura` | Válvulas y tuberías para riego en Perú \| FUNDIGSAC | 50 | Válvulas de compuerta, check, filtros Y y tuberías FUNDIGSAC para sistemas de riego agrícola en Perú. Consulta opciones y solicita tu cotización técnica. | 153 | V-18 |
| `/nosotros` | Empresa peruana de hierro dúctil \| FUNDIGSAC | 44 | Conoce a FUNDIGSAC, empresa peruana especializada en soluciones de hierro dúctil para redes de agua, alcantarillado e infraestructura urbana. | 141 | V-07 |
| `/contacto` | Contacto y cotizaciones en Lima \| FUNDIGSAC | 43 | Contacta al equipo técnico-comercial de FUNDIGSAC en el Cercado de Lima: teléfono y WhatsApp +51 908 849 664, correo y formulario de consulta. | 142 | V-02, V-03 |
| `/cotizar` | Solicitar cotización de válvulas y tuberías \| FUNDIGSAC | 55 | Solicita una cotización técnica de válvulas, tuberías, marcos y tapas de hierro dúctil FUNDIGSAC: indica familia, medidas, cantidad y destino del proyecto. | 155 | Ninguna |

### 5.2 Rutas nuevas

| Ruta | Título | T | Meta descripción | D | Condición |
|---|---|---:|---|---:|---|
| `/productos/tuberias/tuberia-hierro-ductil-c40-k9-k7` | Tubería hierro dúctil C40, K9 y K7 DN80-DN600 \| FUNDIGSAC | 57 | Tubería de hierro dúctil C40, K9 y K7 de DN80 a DN600 para redes de agua potable y conducción matriz en Perú. Revisa clases y medidas, y cotiza desde Lima. | 155 | V-13 |
| `/productos/marcos-y-tapas/marco-y-tapa-d400-2-seguros` | Marco y tapa D400 600 mm con 2 seguros \| FUNDIGSAC | 50 | Marco y tapa de buzón D400 de 600 mm con dos seguros y 60 kg, para calzadas y redes de alcantarillado en Perú. Revisa la ficha y solicita tu cotización. | 152 | V-14 |
| `/productos/marcos-y-tapas/marco-y-tapa-d400-1-seguro` | Marco y tapa D400 600 mm con 1 seguro \| FUNDIGSAC | 49 | Marco y tapa de buzón D400 de 600 mm, versión liviana con un seguro y 38 kg, para redes de alcantarillado en Perú. Revisa la ficha y solicita tu cotización. | 156 | V-14 |
| `/productos/marcos-y-tapas/rejilla-pluvial` | Rejilla pluvial de hierro dúctil en Perú \| FUNDIGSAC | 52 | Rejilla pluvial de hierro dúctil para captación y drenaje de aguas de lluvia en calzadas y veredas. Consulta medidas disponibles y solicita tu cotización. | 154 | V-14 |
| `/productos/valvulas/valvula-mariposa-wafer` | Válvula mariposa wafer de hierro dúctil \| FUNDIGSAC | 51 | Válvula mariposa wafer con palanca, timón o versión bridada para redes de agua e industria. Consulta medidas disponibles y solicita tu cotización en Lima. | 154 | V-17 |
| `/productos/valvulas/valvula-de-aire-triple-funcion` | Válvula de aire de 3 funciones en Perú \| FUNDIGSAC | 50 | Válvula de aire de tres funciones, también llamada ventosa trifuncional, para admitir, expulsar y purgar aire en redes de agua. Solicita ficha y cotización. | 156 | V-17 |
| `/productos/valvulas/valvula-duo-check-wafer` | Válvula duo check wafer hierro dúctil \| FUNDIGSAC | 49 | Válvula duo check tipo wafer para evitar el retorno de flujo en líneas de bombeo y redes de agua. Consulta medidas disponibles y solicita tu cotización. | 152 | Revisión técnica |
| `/productos/valvulas/valvula-guillotina` | Válvula guillotina para lodos y minería \| FUNDIGSAC | 51 | Válvula guillotina para fluidos con sólidos, lodos y aguas residuales en operaciones industriales y mineras. Consulta medidas y solicita tu cotización. | 151 | V-17 |
| `/productos/valvulas/filtro-tipo-y-bridado` | Filtro tipo Y bridado para redes de agua \| FUNDIGSAC | 52 | Filtro tipo Y bridado para retener sólidos y proteger válvulas y equipos en redes de agua y bombeo. Consulta medidas disponibles y solicita tu cotización. | 154 | Revisión técnica |
| `/productos/conexiones` | Conexiones bridadas de hierro dúctil \| FUNDIGSAC | 48 | Conexiones bridadas de hierro dúctil para redes de agua: tee, yee y piezas especiales con medidas por DN. Revisa cada ficha y solicita tu cotización. | 149 | Revisión técnica |
| `/productos/conexiones/tee-bridada` | Tee bridada de hierro dúctil ISO PN16 \| FUNDIGSAC | 49 | Tee de hierro dúctil con tres bridas ISO PN16, de igual diámetro o con derivación reducida, de DN50 a DN600. Consulta medidas y solicita tu cotización. | 151 | Revisión técnica |
| `/productos/conexiones/yee-bridado` | Yee bridado de hierro dúctil DN50-DN300 \| FUNDIGSAC | 51 | Yee de hierro dúctil con tres bridas clase ISO PN16, de DN50 a DN300, para derivaciones en redes de agua. Consulta medidas y solicita tu cotización. | 148 | Revisión técnica |
| `/productos/acoples-y-bridas` | Acoples, adaptadores y bridas \| FUNDIGSAC | 41 | Acoples de gran rango, adaptadores brida para HDPE, uniones de desmontaje, juntas flexibles y bridas para redes de agua. Solicita tu cotización. | 144 | Revisión técnica |
| `/productos/acoples-y-bridas/adaptador-brida-hdpe` | Adaptador brida para tubo HDPE \| FUNDIGSAC | 42 | Adaptador brida para unir tubería HDPE con válvulas y piezas bridadas en redes de agua, riego y saneamiento. Consulta medidas y solicita tu cotización. | 151 | Revisión técnica |
| `/productos/acoples-y-bridas/union-de-desmontaje-autoportante` | Unión de desmontaje autoportante \| FUNDIGSAC | 44 | Unión de desmontaje autoportante para instalar y retirar válvulas y equipos bridados en líneas de agua. Consulta medidas y solicita tu cotización. | 146 | Revisión técnica |
| `/productos/acoples-y-bridas/acople-gran-rango` | Acople de gran rango DN50 a DN600 \| FUNDIGSAC | 45 | Acople de gran rango de DN50 a DN600: cada medida cubre un intervalo de diámetro exterior de tubería. Consulta tu medida y solicita tu cotización. | 146 | Revisión técnica |
| `/productos/valvulas/valvula-check-vertical-cierre-silencioso` | Válvula check vertical cierre silencioso \| FUNDIGSAC | 52 | Válvula check vertical de cierre silencioso, DN50 a DN300, para evitar el retorno de flujo en líneas de bombeo y redes de agua. Solicita tu cotización. | 151 | Revisión técnica |
| `/productos/valvulas/valvula-mariposa-paleta-inox` | Válvula mariposa con paleta inox \| FUNDIGSAC | 44 | Válvula mariposa con paleta inox, con palanca o timón y clase ISO PN16. Consulta las medidas disponibles y solicita tu cotización a FUNDIGSAC en Lima. | 150 | V-17 |
| `/productos/valvulas/valvula-de-aire-roscada` | Válvula de aire roscada DN25 y DN50 \| FUNDIGSAC | 47 | Válvula de aire o ventosa con conexión roscada, DN25 y DN50, clase ISO PN16, para redes de agua. Solicita la ficha técnica y tu cotización en Lima. | 147 | V-17 |
| `/productos/conexiones/tee-luflex-brida` | Tee Luflex con derivación bridada \| FUNDIGSAC | 45 | Tee con extremos de embone Luflex y derivación bridada, para tubo de 63 a 200 mm y salida DN50 a DN100. Consulta medidas y solicita tu cotización. | 146 | Revisión técnica |
| `/productos/conexiones/tuberia-y-codos-sch40` | Tubería y codos SCH-40 para redes \| FUNDIGSAC | 45 | Tubería SCH-40 de DN50 a DN300 y codos SCH-40 de 45° y 90° de DN50 a DN600 para líneas de agua e industria. Consulta medidas y solicita tu cotización. | 150 | Revisión técnica |
| `/productos/acoples-y-bridas/acople-acerrojado-hdpe` | Acople acerrojado para tubo HDPE \| FUNDIGSAC | 44 | Acople acerrojado para unir tubería HDPE de 63 a 315 mm (DN50 a DN300) en redes de agua, riego y saneamiento. Consulta medidas y solicita tu cotización. | 152 | Revisión técnica |
| `/productos/acoples-y-bridas/acople-995` | Acople 995 para tubería HDPE \| FUNDIGSAC | 40 | Acople tipo 995 para tubería HDPE de 63 a 315 mm (DN50 a DN300), para uniones en redes de agua y riego. Consulta medidas y solicita tu cotización. | 146 | Revisión técnica |
| `/productos/acoples-y-bridas/junta-flexible` | Junta flexible bridada DIN y ANSI \| FUNDIGSAC | 45 | Junta flexible de caucho con bridas DIN, ISO o ANSI, de DN50 a DN300, para absorber movimiento y vibración en tuberías. Solicita tu cotización en Lima. | 151 | Revisión técnica |
| `/productos/acoples-y-bridas/bridas` | Bridas planas, ANSI y roscadas \| FUNDIGSAC | 42 | Bridas planas PN16, ANSI y roscadas DIN/ISO para conexiones de redes de agua, con medidas de DN50 a DN700 según modelo. Solicita tu cotización en Lima. | 151 | V-25 |
| `/productos/acoples-y-bridas/brida-ciega` | Brida ciega PN16 DN50 a DN600 \| FUNDIGSAC | 41 | Brida ciega clase PN16 de DN50 a DN600 para cerrar el extremo de una línea bridada en redes de agua. Consulta medidas y solicita tu cotización en Lima. | 151 | V-25 |
| `/cobertura` | Despachos de válvulas y tuberías a regiones \| FUNDIGSAC | 55 | Cómo despacha FUNDIGSAC válvulas, tuberías y piezas de hierro dúctil desde Lima a las regiones del Perú: condiciones, plazos y datos para cotizar. | 146 | V-06 |
| `/guias/clases-tuberia-hierro-ductil` | Tubería de hierro dúctil: clases K7, K9 y C40 \| FUNDIGSAC | 57 | Qué significan las clases K7, K9 y C40 en la tubería de hierro dúctil, en qué se diferencian y qué datos pedir antes de cotizar una red de agua. | 144 | V-13 |
| `/guias/clases-de-carga-en-124` | Clases de carga EN 124 para tapas de buzón \| FUNDIGSAC | 54 | Guía de las clases de carga EN 124 para marcos y tapas: qué significa D400, dónde se usa cada clase y qué documento pedir al comprar. | 133 | V-14 |
| `/guias/como-elegir-valvula-de-aire` | Cómo elegir una válvula de aire o ventosa \| FUNDIGSAC | 53 | Cómo elegir una válvula de aire para redes de agua: funciones, ubicación en la línea, datos del proyecto y documentación que conviene pedir al proveedor. | 153 | V-17 |
| `/guias/valvula-compuerta-para-hdpe-y-pvc` | Válvula compuerta para tubería HDPE y PVC \| FUNDIGSAC | 53 | Opciones de válvula de compuerta para tubería HDPE y PVC: unión acerrojada, embone y adaptadores. Compara el montaje y elige según tu proyecto. | 143 | Revisión técnica |

Para las rutas sin indexar (`/login`, `/registro`, `/recuperar`, `/restablecer`, `/carrito`, `/cotizar/confirmacion`) no se propone título: deben seguir en `noindex`. Las rutas legales conservan los textos actuales.

## 6. Datos estructurados por plantilla

Solo se marcan datos visibles en la página y validados.

| Plantilla | Organization | WebSite | LocalBusiness | Product | BreadcrumbList | FAQPage |
|---|---|---|---|---|---|---|
| Global (`layout.tsx`) | Sí, ya existe | Sí, ya existe | No | No | No | No |
| `/` | Hereda | Hereda | No | No | No | Solo con preguntas visibles |
| `/contacto` | Hereda | Hereda | **Sí, tras V-02, V-04 y V-05** | No | Añadir | No |
| `/productos` | Hereda | Hereda | No | No | Añadir | No |
| Familias | Hereda | Hereda | No | No | Sí, ya existe | Solo con preguntas visibles |
| Ficha de producto | Hereda | Hereda | No | Sí, ya existe; ampliar | Sí, ya existe | Solo con preguntas visibles |
| `/industrias/*` | Hereda | Hereda | No | No | Añadir | Solo con preguntas visibles |
| `/guias/*` | Hereda | Hereda | No | No | Añadir | Solo con preguntas visibles |
| `/cobertura` y regiones | Hereda | Hereda | No por región | No | Añadir | Solo con preguntas visibles |

Las plantillas comerciales de la tabla no tienen hoy preguntas y respuestas visibles, por lo que no corresponde ningún `FAQPage` en ellas. Las únicas preguntas frecuentes del sitio están en páginas legales, como `/eliminar-cuenta`, y no conviene marcarlas. Google [limitó esos resultados enriquecidos en 2023](https://developers.google.com/search/blog/2023/08/howto-faq-changes), de modo que no hay motivo para crear preguntas artificiales.

### Organization

Mantener el bloque actual. Añadir `taxID` y `streetAddress` solo cuando se validen V-01 y V-02.

### LocalBusiness en `/contacto`

Se publica cuando estén validados los campos marcados. Los valores entre corchetes no son datos y no deben publicarse tal cual.

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://fundigsac.com/#local",
  "name": "FUNDIGSAC",
  "url": "https://fundigsac.com/contacto",
  "parentOrganization": { "@id": "https://fundigsac.com/#organizacion" },
  "telephone": "[teléfono validado]",
  "email": "[correo validado, V-03]",
  "image": "[foto real del local, V-21]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[calle validada, V-02]",
    "addressLocality": "Cercado de Lima",
    "addressRegion": "Lima",
    "addressCountry": "PE"
  },
  "openingHoursSpecification": "[horario validado, V-04]",
  "areaServed": "[solo si V-06 lo confirma]"
}
```

### Product en fichas

Campos actuales: `name`, `description`, `url`, `category`, `image`, `sku` y `brand`. Se propone añadir `additionalProperty` con las filas de la tabla técnica visible.

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Válvula check swing",
  "sku": "VCSW",
  "category": "Válvulas",
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "Material del cuerpo", "value": "Hierro dúctil GGG40 / GGG50" },
    { "@type": "PropertyValue", "name": "Clase de brida", "value": "ISO PN16 (DN200 también PN10)" }
  ]
}
```

Reglas para `Product`:

- **Sin `offers`, `review` ni `aggregateRating`** mientras no haya precios ni reseñas reales. Sin alguno de esos tres campos la ficha no opta a [fragmentos enriquecidos de producto](https://developers.google.com/search/docs/appearance/structured-data/product-snippet), y Search Console puede avisarlo. Ese aviso se acepta: no debe resolverse inventando precios.
- `brand` solo cuando la marca esté confirmada.
- Las normas se añaden a `additionalProperty` solo tras validarse.
- Las pantallas de referencia siguen como `WebPage` con `noindex`.

### BreadcrumbList

Usar `breadcrumbList()` en sectores, guías, `/productos`, `/contacto` y `/cobertura`, con los mismos niveles que se ven en pantalla.

## 7. Enlazado interno

Situación medida: la portada enlaza 0 fichas, cada sector enlaza 1, `/productos/tuberias` enlaza 0 y `/productos`, `/productos/valvulas` y `/productos/marcos-y-tapas` enlazan a referencias `noindex`.

| Origen | Destino | Regla | Anclas de ejemplo |
|---|---|---|---|
| `/` | 3 familias y al menos 6 fichas | Enlaces HTML en el contenido inicial | válvula de compuerta bridada, tubería de hierro dúctil K9 |
| `/productos` | Todas las familias y fichas destacadas | Sin enlaces a páginas `noindex` | marcos y tapas D400 |
| Familia | Todas sus fichas indexables | Enlaces presentes en el HTML inicial | válvula check swing |
| Tarjetas sin ficha | `/contacto?motivo=documentacion` | Solo mientras no exista ficha. Sustituir al publicarla | solicitar ficha de válvula de aire |
| Ficha | Familia, 3 relacionadas, 1 o 2 sectores, `/cotizar` | Relación técnica real. Ampliar a las 3 compuertas, que hoy no enlazan ninguna ficha indexable | válvula de compuerta acerrojada para HDPE |
| Ficha de compuerta | Unión de desmontaje, adaptador brida, tee | Armado real de una instalación | unión de desmontaje autoportante |
| Tubería | Conexiones, compuerta, guía de clases | Compatibilidad validada | clases K7, K9 y C40 |
| Marco y tapa | Guía EN 124, rejilla, `/industrias/saneamiento` | Por aplicación | clases de carga EN 124 |
| Sector | Al menos 4 fichas pertinentes | Solo productos respaldados para ese sector | válvula flotadora para reservorios |
| Guía | 2 a 5 fichas y 1 familia | Texto contextual | válvula de aire de tres funciones |
| `/cobertura` | Familias, `/cotizar`, `/contacto` | Sin listas de ciudades como relleno | solicita tu cotización para obra en regiones |
| Pie de página | Familias, sectores, `/cobertura`, contacto, legales | Sin enlazar todas las fichas | |

Reglas generales:

- Una misma URL debe usar anclas variadas y descriptivas. Evitar "ver más" cuando el contexto lo permita.
- La redirección `/product/:slug` hacia `/productos/valvulas` debe sustituirse por redirecciones 1:1 en cuanto existan las fichas de mariposa y guillotina.
- Corregir cualquier enlace que pase por una redirección.

## 8. Páginas nuevas y orden de publicación

| Orden | Página | Fuente disponible | Bloqueo |
|---:|---|---|---|
| 1 | Tubería C40, K9 y K7 | Lista de precios, página 11 | V-13 |
| 2 | Marco y tapa D400 de 2 seguros | Lista de precios, página 11 | V-14 |
| 3 | Marco y tapa D400 de 1 seguro | Lista de precios, página 11 | V-14 |
| 4 | Válvula mariposa wafer | `catalog-pdf.ts` (VMTWP, VMTWT, VMBB) | V-17 |
| 5 | Válvula de aire de 3 funciones | `catalog-pdf.ts` (VDAP) | V-17 |
| 6 | Rejilla pluvial | Tarjeta actual, sin datos técnicos | Falta ficha |
| 7 | Válvula duo check, check vertical, filtro tipo Y, guillotina, mariposa paleta inox, aire roscada | `catalog-pdf.ts` y WordPress anterior | Revisión técnica, V-17 |
| 8 | Familia de conexiones, tee, yee, tee Luflex y SCH-40 | `catalog-pdf.ts` (TBB, YBB, TLB, TSCH40, CSCH90, CSCH45) | Revisión técnica |
| 9 | Familia de acoples y bridas, y sus 8 fichas | `catalog-pdf.ts` | Revisión técnica, V-25 |
| 10 | `/cobertura` | Ninguna todavía | V-06 |
| 11 | Cuatro guías técnicas | Autor técnico de FUNDIGSAC | V-13, V-14, V-17 |
| 12 | Especificaciones SEDAPAL por válvula | Documentos públicos CTPS-ET | V-19 |
| 13 | Páginas regionales, tubería y accesorios HDPE, equipos, medidores, hidrantes | Pendiente | V-06, V-18, V-20, decisión comercial |

Contenido mínimo de una ficha: H1 con el nombre comercial, tabla HTML con DN, PN, material, recubrimiento y unión, aplicaciones, documento descargable, relacionados, cotización con producto preseleccionado y fecha de la ficha técnica. No se publica una ficha con atributos vacíos o genéricos.

Cada ficha nueva debe entrar por `registry.tsx`, con lo que la ruta, el sitemap y el marcado se generan solos. Las referencias `noindex` se retiran al publicarse la ficha real, con redirección permanente.

## 9. KPI obligatorios

**Estado al 9 de noviembre de 2026: no está en verde.** Móvil falla en 14 de 14 rutas por LCP y escritorio cumple en 14 de 14. Detalle en la sección 9 del informe.

Cada corrección o página nueva debe cumplir todo esto antes de darse por terminada, en móvil y en escritorio, con mediana de 3 corridas:

| KPI | Umbral |
|---|---|
| Rendimiento, accesibilidad, buenas prácticas y SEO | 90 o más |
| LCP | 2.500 ms o menos |
| CLS | 0,1 o menos |
| TBT | 200 ms o menos |
| FCP | 1.800 ms o menos |
| Speed Index | 3.400 ms o menos |

Procedimiento local, sin tocar `.next` ni producción:

```bash
# Desde Frontend/. Guardar tsconfig.json y next-env.d.ts antes de compilar y restaurarlos después:
# la compilación con NEXT_DIST_DIR los modifica.
NEXT_DIST_DIR=.next-kpi SITE_INDEXABLE=true NEXT_PUBLIC_SITE_URL=http://127.0.0.1 pnpm exec next build
NEXT_DIST_DIR=.next-kpi SITE_INDEXABLE=true NEXT_PUBLIC_SITE_URL=http://127.0.0.1 pnpm exec next start --hostname 127.0.0.1 -p 3199

# En Git Bash anteponer MSYS_NO_PATHCONV=1 para que no se alteren las rutas.
node scripts/perf/kpi-gate.mjs --app fundigsac-indexable --base http://127.0.0.1:3199 --routes "/,/productos,/productos/valvulas" --runs 3
```

`NEXT_PUBLIC_SITE_URL` no debe llevar puerto: la regla de host de `next.config.ts` compara sin él, y con puerto se añade `X-Robots-Tag: noindex`.

Las rutas nuevas se añaden a la lista. Además, antes del lanzamiento y tras cada publicación:

- `pnpm typecheck`, `pnpm lint` y `pnpm test:unit` sin errores.
- Prueba de resultados enriquecidos para cada plantilla.
- Cero enlaces internos rotos y ninguno hacia páginas `noindex` en la navegación principal.
- Títulos y descripciones únicos en todo el sitemap.
- Medición con PageSpeed sobre producción, con clave de API.

## 10. Checklist de lanzamiento

### Antes de activar la indexación

- [ ] V-01 a V-05 y V-07 resueltos.
- [ ] Textos sin respaldo retirados o sustentados (V-08 a V-11, V-23, V-24 y V-25).
- [ ] Asistente, carrito y buscador sin datos de `data.ts` no validados (V-12).
- [ ] Fichas P0 publicadas con datos revisados.
- [ ] KPI en verde en todas las rutas del sitemap, móvil y escritorio.
- [ ] Matriz de redirecciones: URL del WordPress, URL nueva, estado HTTP y responsable.
- [ ] Redirecciones 1:1 comprobadas, sin cadenas ni bucles. `/product/:slug` revisada.
- [ ] Decidir `www` frente a dominio raíz y redirigir el otro.
- [ ] Decidir si los PDF de `/docs` se indexan. Su nombre debe ser descriptivo y su contenido, vigente.
- [ ] Crear el documento `SEO-GOOGLE-LAUNCH.md` que cita `env.ts` o corregir esa referencia.

### Corte y Google Search Console

- [ ] Copia de seguridad del WordPress y exportación de URL, medios y metadatos.
- [ ] Acceso confirmado a DNS y a Vercel.
- [ ] `NEXT_PUBLIC_SITE_URL=https://fundigsac.com` y `SITE_INDEXABLE=true` solo en Production. La variable se lee al compilar: un rollback a una compilación anterior vuelve a `noindex`.
- [ ] Apuntar el dominio y comprobar HTTPS, redirección de host y certificado.
- [ ] Comprobar `/robots.txt`, `/sitemap.xml`, la meta de robots y la ausencia de `X-Robots-Tag: noindex` en el dominio canónico.
- [ ] Crear la propiedad de dominio por DNS. El sitio ya incluye la meta de verificación para la propiedad de prefijo de URL.
- [ ] Enviar `https://fundigsac.com/sitemap.xml`.
- [ ] Solicitar la inspección de la portada, las 3 familias y las fichas P0.
- [ ] Revisar el informe de indexación y el de datos estructurados a las 48 horas y cada semana durante 8 semanas.
- [ ] Revisar 404, cobertura y consultas. Comparar con la línea de base y ajustar la sección 3 con datos reales.
- [ ] Mantener activas las redirecciones al menos 12 meses.
- [ ] Vincular Search Console con GA4, respetando el consentimiento de cookies existente.

### Google Business Profile

`location.ts` ya apunta a un lugar de Google Maps llamado FUNDIGSAC. Hay que reclamar esa ficha y no crear una nueva.

- [ ] Confirmar quién administra la ficha y obtener acceso (V-22).
- [ ] Confirmar si el local atiende público. Si solo reparte, configurar área de servicio y ocultar la dirección (V-05).
- [ ] Nombre comercial real, sin palabras clave añadidas.
- [ ] Nombre, dirección y teléfono idénticos en la web, en la ficha, en Facebook y en directorios (V-02, V-03).
- [ ] Categoría principal elegida de la lista oficial de Google. Buscar términos como válvulas, suministros de fontanería o equipos industriales, y confirmar la opción disponible.
- [ ] Horario validado (V-04). Zona de servicio solo donde se despache (V-06).
- [ ] Enlace al sitio con parámetros UTM, y enlace directo a `/cotizar`.
- [ ] Fotos reales del local, de los productos y del equipo (V-21).
- [ ] Productos publicados en la ficha enlazando a su URL, sin precios no aprobados.
- [ ] Descripción sin certificaciones ni cifras sin respaldo.
- [ ] Verificación completada. Eliminar o fusionar duplicados.
- [ ] Solicitar reseñas solo a clientes reales y sin incentivos. Responder todas.
- [ ] Revisar mensualmente llamadas, clics, indicaciones y consultas.
- [ ] Unificar el perfil de Facebook e Instagram declarado en `sameAs`.

### Después del lanzamiento

- [ ] Medir clics e impresiones por grupo de la sección 3.
- [ ] Revisar KPI reales de Core Web Vitals en Search Console al acumularse datos.
- [ ] Comparar conversiones: cotizaciones, teléfono, WhatsApp y descargas.
- [ ] Solicitar enlaces reales: gremios, proveedores, obras autorizadas y directorios sectoriales.
- [ ] Revisar cada trimestre las búsquedas Q1 a Q19 y actualizar `COMPETIDORES.md`.

## 11. Requiere validación de FUNDIGSAC

La lista completa, con dato, ubicación y documento necesario, está en la sección 10 de `INFORME_COMPETENCIA.md`. Resumen para este plan:

| Bloque | Id | Efecto sobre el plan |
|---|---|---|
| Identidad y local | V-01 a V-05, V-07, V-22 | Bloquea `LocalBusiness`, Business Profile y `taxID` |
| Cobertura | V-06 | Bloquea `/cobertura` y las regiones |
| Normas y garantías | V-08, V-09, V-10, V-15 | Condiciona títulos y `additionalProperty` |
| Frases comerciales | V-11 | Deben retirarse o sustentarse antes de indexar |
| Dataset de maqueta | V-12 | No puede alimentar páginas públicas |
| Tubería y tapas | V-13, V-14 | Bloquea las fichas P0 de esas líneas |
| Mariposa, aire y guillotina | V-17 | Bloquea esas fichas |
| Marca H-ITALY | V-16 | Condiciona su ficha |
| HDPE | V-18 | Condiciona la categoría de tuberías |
| SEDAPAL y EPS | V-19 | Bloquea el contenido de conformidad |
| Clientes y fotos | V-20, V-21 | Bloquea casos de obra e imágenes |
| Minería | V-23 | Bloquea el contenido de pulpas y relaves |
| Tarjetas sin código | V-24 | Condiciona las variantes de tubería y tapas |
| Bridas | V-25 | Condiciona las fichas de bridas |

Los competidores citan aprobaciones y certificados que no se verificaron. Ninguna de esas afirmaciones debe usarse como modelo de lo que FUNDIGSAC puede decir.
