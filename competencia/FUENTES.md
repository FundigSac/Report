# Fuentes y controles del estudio de competencia

Fecha: 9 de noviembre de 2026.

Este documento indica de dónde sale cada tipo de afirmación de `COMPETIDORES.md`, `INFORME_COMPETENCIA.md` y `PLAN_SEO.md`, y qué sigue sin respaldo.

## 1. Trazabilidad

| Tipo de afirmación | Archivo fuente | Alcance |
|---|---|---|
| Títulos, metadatos, H1, normas, JSON-LD y enlaces de competidores | `datos/*.json` | Hechos del HTML público, sin JavaScript, con tope de 40 páginas |
| Lectura por competidor, productos y fortalezas | `sitios/*.md` | Lo marcado como Inferencia es interpretación |
| Quién aparece en cada búsqueda | Sección 3 de este documento | Salida de la herramienta, no posiciones en Google.pe |
| Catálogo y rutas de FUNDIGSAC | `Frontend/src/lib/catalog.ts`, `Frontend/src/lib/catalog-pdf.ts`, `Frontend/src/modules/catalog/registry.tsx`, `Frontend/src/modules/catalog/valve-sheets.ts`, `Frontend/src/app/sitemap.ts` | El código no prueba que el dato sea correcto |
| Tarjetas de familia y sectores | `Frontend/src/screens/islands/w03-valvulas-copy.ts`, `w04-tuberias-copy.ts`, `w05-marcos-copy.ts`, `Frontend/src/app/industrias/*/copy.ts` | Textos actuales, varios pendientes de validar |
| KPI de FUNDIGSAC | `Report/kpi/fundigsac-indexable.jsonl` | 84 corridas locales con Lighthouse 13.5.0 |
| Recomendaciones, prioridades y valoraciones Alta, Media y Baja | Criterio del analista | No son hechos observados |
| Datos de empresa pendientes | Sección 10 del informe, V-01 a V-25 | Requieren documento de FUNDIGSAC |

## 2. Estado del rastreo por sitio

Bloqueos del sitio son respuestas 403 o 429, captcha o página de desafío. Omitidas son rutas excluidas por `robots.txt`.

| Sitio | Estado | Solicitudes HTTP | Páginas pedidas | Con datos | Sin visitar | Omitidas | Bloqueos | Limitación principal |
|---|---|---:|---:|---:|---:|---:|---:|---|
| M&L Negofer | ok | 41 | 40 | 40 | 226 | 0 | 0 | Solo 1 de las 11 páginas de Válvulas; ficha K-7 y K-9 sin visitar |
| ICOFESA | ok | 41 | 40 | 23 | 289 | 0 | 0 | 17 redirecciones 302; categorías de válvulas y tubería sin visitar; 1 sola ficha |
| FUMOSAC | ok | 38 | 35 | 34 | 0 | 0 | 0 | Rastreo completo por enlaces; sitemap sin leer |
| Collaval Import | ok | 41 | 40 | 36 | 147 | 0 | 0 | Ninguna ficha visitada; 3 respuestas 404 |
| Mecka | ok | 41 | 40 | 40 | 14 | 0 | 0 | 12 fichas sin visitar, entre ellas todas las bombas |
| Leoneblu | ok | 41 | 40 | 40 | 111 | 0 | 0 | Sin `robots.txt` (HTTP 404); 53 categorías sin visitar |
| EATHISA Perú | ok | 23 | 22 | 22 | 0 | 0 | 0 | Rutas `/search` excluidas por regla; el catálogo puede ser mayor |
| Válvulas Perú | error | 1 | 0 | 0 | 0 | 0 | 0 | Dominio inexistente (NXDOMAIN). Sin datos |
| Hi Perú | ok | 41 | 40 | 39 | 127 | 0 | 0 | 14 de 127 fichas visitadas |
| Rivali Perú | ok | 41 | 40 | 40 | 184 | 0 | 0 | Solo la primera página de cada listado; contacto sin visitar |
| Inccosac | ok | 27 | 26 | 18 | 0 | 0 | 0 | 5 respuestas 404 y 3 redirecciones; 3 de 4 familias vacías |
| Citaly Perú | ok | 41 | 40 | 40 | 30 | 0 | 0 | 26 de 53 fichas visitadas; contacto sin visitar |

**Sitios bloqueados: 0 de 12.** Válvulas Perú figura con estado `error` porque su dominio no existe, no porque rechazara el acceso.

PageSpeed es un caso distinto: la API pública respondió HTTP 429 sin clave en los 12 casos, por lo que no hay datos de rendimiento real de ningún competidor. Ese 429 lo emitió la API de Google, no los sitios.

## 3. Resultados de las búsquedas

Lista extraída de la salida original de la herramienta WebSearch en modo `extended`, con título y URL de cada resultado. Es la base de las columnas de búsquedas de `COMPETIDORES.md` y de la sección 4 del informe.

Tres búsquedas adicionales por nombre (Válvulas Perú, EATHISA e Inccosac) y las primeras pasadas de Q1 a Q5 usaron el modo `standard`. No se incluyen porque no cuentan para ningún recuento.

### Búsquedas de selección de competidores

### C1. Negofer Perú válvulas tuberías hierro dúctil sitio web oficial

- válvula compuerta tipo dado de hierro dúctil para tubería: https://www.sodimac.com.pe/sodimac-pe/articulo/150484799/valvula-compuerta-tipo-dado-de-hierro-ductil-para-tuberia/150484800
- MYL Negofer sac: https://mylnegofersac.com/
- Tubería Hierro Dúctil C-40: https://mylnegofersac.com/producto/tuberia-hierro-ductil-c-40/
- Tuberías: https://mylnegofersac.com/categoria-producto/tuberias/
- Tubería Hierro Dúctil K-7, K-9: https://mylnegofersac.com/producto/tuberia-hierro-ductil-k-7-k-9/
- PLIEGO DE ESPECIFICACIONES TÉCNICAS TUBERÍA EN HIERRO DÚCTIL K9: https://icofesa.com/sistema/fichastecnicas/Tuberia%20Ductil%20K9%205.5%20Mt%20Pam.pdf
- Tubería de Hierro Ductil Bridado: https://mylnegofersac.com/producto/tuberia-de-hierro-ductil-bridado/
- Fiorella Representaciones S.A.C.: https://www.fiorellarepre.com.pe/
- Tubería de fierro galvanizado: https://mylnegofersac.com/producto/tuberia-de-fierro-galvanizado/

### C2. válvulas compuerta hierro dúctil proveedor Lima Perú distribuidor saneamiento

- Válvula Compuerta Bridada de Hierro Dúctil - Hi Perú: https://www.hiperusac.com.pe/producto/valvula-compuerta-bridada-de-hierro-ductil-cierre-hermetico-y-alta-resistencia/
- Válvula Compuerta Hierro Ductil - Cosmoplas Perú: https://www.cosmoplas.pe/producto/valvula-compuerta-hierro-ductil/
- Collaval Import: https://collavalimport.com/
- Comercializadora LIMAFERR: https://limaferrperu.com/
- VÁLVULA COMPUERTA UF: https://limaferrperu.com/producto/valvula-compuerta-uf/
- Rivali Perú - Válvulas Industriales y Sistemas Contra incendios: https://rivaliperu.com/
- VALVULA COMPUERTA BRIDADA: http://www.leoneblusac.com/producto.php?id=13648
- ICOFESA S.A.: https://icofesa.com/
- Fiorella Representaciones S.A.C.: https://www.fiorellarepre.com.pe/

### C3. tubería hierro dúctil Perú venta importador accesorios ISO 2531 proveedor

- E d i C I Ó N 2 0 0 9 VENTAS INTERNACIONALES Tuberías y Accesorios: https://uspipe.com/wp-content/uploads/2020/12/20111041547130.Ductile-Iron-FPF-SPN-Metric-BRO-089sm.pdf
- Tubería de Hierro Ductil ISO 2531 - EATHISA PERU: https://web.eathisa.com.pe/2018/05/tuberia-de-hierro-ductil-iso-2531.html
- CONSIDERACIONES TÉCNICAS PARA TUBERÍAS Y ...: https://cdn.www.gob.pe/uploads/document/file/5976587/5295689-ctps-re-001-consideraciones-tecnicas-para-el-uso-de-tuberias-y-accesorios-agua-potable.pdf
- Accesorios para tuberías de agua y alcantarillado: https://fumosac.com.pe/accesorios/
- TUBOS BRIDADOS DE HIERRO DÚCTIL ISO 2531: http://www.kallpa-peru.com/cmrclytcnc/cmrclytcnc16/cmrclytcnc1607/fchstcncs/FCHSTCNCSKLLP/FCHSTCNCSKLLP16/FCHSTCNCSKLLP1607/CCSRSHDBRDDS/KALLPA%20-%20TUBOS%20BRIDADOS%20DE%20HIERRO%20DUCTIL.pdf
- ACCESORIOS EN HIERRO DUCTIL: https://termofusion-riego.com/categoria-producto/hierro-ductil/
- Tubería de Hierro Dúctil - Inccosac: https://inccosac.com/producto/tuberia-de-hierro-ductil/
- TUBERIAS DE HIEERO DUCTIL Y CONEXIONES: https://www.ecomexperu.com/CNBM%20Catalogo%20de%20Tuberias%20y%20Conexiones.pdf
- PLIEGO DE ESPECIFICACIONES TÉCNICAS TUBERÍA EN HIERRO DÚCTIL K9: https://icofesa.com/sistema/fichastecnicas/Tuberia%20Ductil%20K9%205.5%20Mt%20Pam.pdf

### C4. marcos y tapas hierro dúctil buzón EN 124 Perú fabricante proveedor

- MARCOS Y TAPAS HIERRO DUCTIL: https://www.ayc.com.pe/producto/marcos-y-tapas-hierro-ductil/
- TAPAS Y MARCO - Mecka Sac Peru: https://meckasacperu.com/tapas-y-marco/
- Marco y tapa estandar - FUMOSAC: https://fumosac.com.pe/marco-y-tapa-estandar-2/
- Marco y tapa de hierro dúctil para buzón| MeckaSAC: https://www.meckasacperu.com/marco-tapa-de-hierro-ductil-buzon.html
- MARCO-Y-TAPA-DE-BUZON.pdf: https://roalcomperu.com/wp-content/uploads/2024/03/MARCO-Y-TAPA-DE-BUZON.pdf
- Marco y Tapa de Alcantarillado EATHISA - EATHISA PERU: https://web.eathisa.com.pe/2019/11/marco-y-tapa-de-alcantarillado-eathisa.html?m=1
- Marco y Tapa de Buzón Hierro Dúctil D400 - Collaval Import: https://collavalimport.com/web/productos/marco-y-tapa-de-buzon-hierro-ductil-d400/
- MARCO Y TAPA HIERRO DUCTIL - Theatlantic s.a.: https://theatlantic.pe/producto.php?id=23722
- MARCO Y TAPA HIERRO DUCTIL: https://icofesa.com/producto.php?id=15942

### C5. válvula mariposa válvula check válvula de aire agua potable proveedor Perú empresa

- Valvula Ahorradora Agua- Bloqueadora de Aire - ASOCIE PERU - YouTube: https://www.youtube.com/watch?v=USO4RqYPevw
- Adquisicion De Valvulas Mariposa Y Check Para Manifold De A...-Petroleos Del Peru S.A.: https://www.todolicitaciones.pe/licitacion/ocds-dgv273-seacev3-907063/adquisicion-de-valvulas-mariposa-y-check-para-manifold-de-agua-ci-de-las-esferas-602-y-604
- Experiencia en Suministros: https://tecval.pe/experiencia-en-suministros/
- Venta de Válvulas en Perú: https://romicorp.com.pe/valvulas.html
- Válvula de aire para aguas residuales o desague| MeckaSAC: https://www.meckasacperu.com/valvula-de-aire-para-aguas-residuales.html
- Valvulas Check Wafer RUD: https://www.rudmex.com/valvulas-check-wafer
- PNEUMATIC VÁLVULAS DE CONTROLES Y EQUIPOS INDUSTRIALES: https://www.fullcontrolperu.com/catalogo.pdf
- Valvula ahorradora de Agua- Bloqueadora de Aire: https://asocieperu.com/producto/valvula-ahorradora-de-agua-bloqueadora-de-aire/
- Válvulas check Cyber Wow 🔥 ¡Últimas horas!: https://www.promart.pe/gasfiteria/valvulas-y-llaves-de-agua/valvulas-check
- APTEIN - Válvulas de aire: https://www.apteinperu.com/productos/v%C3%A1lvulas/v%C3%A1lvulas-de-aire

### C6. importador distribuidor waterworks Perú válvulas tuberías accesorios saneamiento minería agricultura empresa

- CUPERSA - Distribuidores de Válvulas y Tuberías: https://grupocunado.com/en/grupo-cunado-companies/cupersa
- Importadores de Productos Industriales - PATMO PERÚ: https://patmoperu.com/
- Válvulas Perú: https://valvulasperu.pe/
- Distribuidor de Tuberías PVC y Conexiones en Lima: https://www.wgcorporaciongoicha.com/
- TUBERÍAS - Mecka Sac Peru: https://meckasacperu.com/tuberias/
- Collaval Import: https://collavalimport.com/
- CIGSAC: http://www.cigsac.com/
- A.C. TRADING COMPANY: https://www.valvulasperu.com.pe/
- Válvulas y sistemas de control de fluidos: https://redmin.pe/solucion/valvulas-y-sistemas-de-control-de-fluidos/

### C7. fundición hierro dúctil Perú fabricante válvulas tapas buzón Fumosac Inccosac

- FUNDICION MORENO S.A.C.: https://www.perumarketplace.com/es/tienda/inicio/FUMOSAC
- Proveedores de Accesorios de fundición dúctil - Distribuidores, Productores y Fabricantes - QuimiNet: https://www.quiminet.com/proveedores/accesorios-de-fundicion-ductil-114361840705.htm
- FICHA TÉCNICA NTP 350.106 MARCO Y TAPA DE HIERRO DÚCTIL: https://fumosac.com.pe/fichas/caja-de-valvula.pdf
- Fundición Moreno-FUMOSAC-Accesorios para Agua y Alcantarillado: https://www.guiaperu.pe/manufactura-y-metalurgia/281-fundicion-moreno-fumosac-accesorios-para-agua-y-alcantarillado
- Marco y tapa estandar - FUMOSAC: https://fumosac.com.pe/marco-y-tapa-estandar-2/
- Fumosac: https://fumosac.com.pe/marco-y-tapa/
- MARCO Y TAPA HIERRO DUCTIL - Theatlantic s.a.: https://theatlantic.pe/producto.php?id=23722
- Fumosac - Aguamarket: https://www.aguamarket.com/sql/empresas/emp.asp?Empresa=14941
- Marco y tapa D400 - FUMOSAC: https://fumosac.com.pe/marco-y-tapa-d400/
- ICOFESA S.A.: https://icofesa.com/

### C8. válvula de aire triple efecto hierro dúctil Lima precio SEDAPAL proveedor

- valvula de aire hierro ductil - LEONEBLU SAC: https://leoneblusac.com/producto.php?id=12730&p=VALVULA+DE+AIRE+HIERRO+DUCTIL
- Válvula de Aire Triple Efecto: https://rivaliperu.com/producto/valvula-de-aire-triple-efecto/
- VALVULA DE AIRE HIERRO DUCTIL: https://leoneblusac.com/producto.php?id=13277
- VALVULA DE AIRE HIERRO DUCTIL: https://icofesa.com/producto.php?id=18625
- Válvula De Aire Triple Efecto Citaly - Valvoline Perú: https://www.valvoline-peru.com/producto/valvula-de-aire-triple-efecto-citaly/
- VALVULA DE AIRE HIERRO DUCTIL: https://icofesa.com/producto.php?id=21162
- VALVULA DE AIRE HIERRO DUCTIL: https://icofesa.com/producto.php?id=21703
- VALVULA DE AIRE HIERRO DUCTIL: http://www.icofesa.com/producto.php?id=15825
- VALVULA DE AIRE VENTOSA TRIFUNCIONAL: https://icofesa.com/producto.php?id=22218

### C9. tapa de buzón hierro dúctil D400 Lima venta empresa saneamiento conexiones bridadas

- Marco y tapa de buzón hierro dúctil D400: https://valvulasperu.pe/producto/marco-y-tapa-de-buzon-hierro-ductil-d400/
- Marco y tapa D400 - FUMOSAC: https://fumosac.com.pe/marco-y-tapa-d400/
- Marco y Tapa de Buzón Hierro Dúctil D400 - Collaval Import: https://collavalimport.com/web/productos/marco-y-tapa-de-buzon-hierro-ductil-d400/
- Marcos Y Tapas: https://citalyperu.com/product-category/marcos-y-tapas/
- MARCOS Y TAPAS HIERRO DUCTIL: https://www.ayc.com.pe/producto/marcos-y-tapas-hierro-ductil/
- Marco Cuadrado y tapa de hierro dúctil con 1 seguro D400: https://mylnegofersac.com/producto/marco-cuadrado-y-tapa-de-hierro-ductil-con-1-seguro-d400/
- MARCO Y TAPA BUZON D400: https://leoneblusac.com/producto.php?id=13566
- Marco y Tapa De Buzón D400 Con Doble Seguro: https://citalyperu.com/product/marco-y-tapa-de-buzon-d400-con-doble-seguro/
- Marco cuadrado y tapa circular - FUMOSAC: https://fumosac.com.pe/marco-cuadrado-y-tapa-circular-2/

### C10. válvulas para riego agrícola y minería hierro dúctil Perú importador directo HDPE stub end

- Collaval Import: https://collavalimport.com/
- Tubería HDPE, Accesorios y Conexiones en Perú: https://www.acorsaperu.com/linea-hidraulica/16588-2/
- Tubería HDPE en Perú para Minería y Agua: https://www.acorsaperu.com/linea-hidraulica/tuberia-hdpe-en-peru/
- Hi Perú SAC - Especialistas en Válvulas Industriales y Línea HDPE: https://www.hiperusac.com.pe/
- A.C. TRADING COMPANY: https://www.valvulasperu.com.pe/
- Válvula HD Bridada DN-160MM: https://soluplastic.com.pe/productos/valvula-de-hierro-ductil-bridado/
- ICOFESA S.A.: https://icofesa.com/
- ACCESORIOS EN HIERRO DUCTIL: https://termofusion-riego.com/categoria-producto/hierro-ductil/
- Válvulas Industriales: https://corsaflex.com/tienda/valvulas-industriales/

### C11. Negofer SAC Lima RUC "Negofer" tuberías válvulas M&L Negofer contacto

- Válvula esférica con doble unión universal: https://mylnegofersac.com/producto/valvula-esferica-con-doble-union-universal/
- Tienda: https://mylnegofersac.com/myl-negofer-sac/shop/
- MYL Negofer sac: https://mylnegofersac.com/
- Válvula Compuerta Luflex M&L: https://mylnegofersac.com/producto/valvula-compuerta-luflex-ml/
- Válvula Check Flex M&L: https://mylnegofersac.com/producto/valvula-check-flex-ml/
- M&L Negofer SAC: https://mylnegofersac.com/categoria-producto/ml-negofer-sac/
- Válvula De Toma Termo plástica con Salida a Tuberías de PE: https://mylnegofersac.com/producto/valvula-de-toma-termo-plastica-con-salida-a-tuberias-de-pe/
- Válvula Luflex ISO 2531: https://mylnegofersac.com/producto/valvula-luflex-iso-2531/
- Válvula Flotador M&L: https://mylnegofersac.com/producto/valvula-flotador-ml/
- Válvula Ventosa trifuncional: https://mylnegofersac.com/producto/valvula-ventosa-trifuncional/

### Búsquedas de compradores

### Q1. válvula compuerta hierro dúctil Perú precio

- válvula compuerta tipo dado de hierro dúctil para tubería: https://www.sodimac.com.pe/sodimac-pe/articulo/150484799/valvula-compuerta-tipo-dado-de-hierro-ductil-para-tuberia/150484800
- Valvula de Compuerta: https://www.sodimac.com.pe/sodimac-pe/b/valvula-de-compuerta
- válvula compuerta tipo dado de hierro dúctil para tubería GENERICO: https://www.falabella.com.pe/falabella-pe/product/150484799/valvula-compuerta-tipo-dado-de-hierro-ductil-para-tuberia/150484800
- Válvula Compuerta Bridada Hierro Dúctil - Valvoline Perú: https://www.valvoline-peru.com/producto/valvula-compuerta-bridada-hierro-ductil/
- VÁLVULA TIPO COMPUERTA: https://www.agromax.pe/product/valvula-tipo-compuerta/
- Válvula Compuerta Bridada hierro dúctil: https://rivaliperu.com/producto/valvula-compuerta-bridada-hierro-ductil/
- Inicio old - Valvoline Perú: https://www.valvoline-peru.com/
- Hierro Dúctil: https://fitflowretail.com/collections/hierro-ductil
- ICOFESA S.A.: https://icofesa.com/

### Q2. válvula compuerta bridada PN16 Lima proveedor

- VÁLVULA COMPUERTA BRIDADA CIM 72F: https://www.fiorellarepre.com.pe/VALVULA-COMPUERTA-BRIDADA-CIM-72F/851036
- Válvula Compuerta Bridada de Hierro Dúctil - Hi Perú: https://www.hiperusac.com.pe/producto/valvula-compuerta-bridada-de-hierro-ductil-cierre-hermetico-y-alta-resistencia/
- VALVULA COMPUERTA BRIDADA: http://www.leoneblusac.com/producto.php?id=13648
- Válvula de Compuerta 6" con Brida: https://www.tecnototalperu.com/producto/valvula-de-compuerta-6-con-brida/
- VALVULA COMPUERTA BRIDADA: http://www.leoneblusac.com/producto.php?id=12440&p=VALVULA+COMPUERTA+BRIDA
- VALVULA COMPUERTA BRIDADA: http://www.leoneblusac.com/producto.php?id=12447
- VÁLVULA COMPUERTA BRIDA: https://icofesa.com/producto.php?id=23525
- ICOFESA S.A.: https://icofesa.com/
- VÁLVULA COMPUERTA BRIDA: https://icofesa.com/producto.php?id=16539
- VÁLVULA COMPUERTA BRIDA: https://www.icofesa.com/producto.php?id=14541

### Q3. válvula mariposa hierro dúctil Perú

- VÁLVULA MARIPOSA RANURADA FIERRO DÚCTIL ASTM A536 300 PSI UL/FM: https://www.fiorellarepre.com.pe/VALVULA-MARIPOSA-RANURADA-FIERRO-DUCTIL-ASTM-A536-300-PSI-UL-FM/842000
- Válvulas Mariposa - Adolphus Tecnología y experiencia: https://adolphus.pe/productos/valvulas-mariposa
- Válvula mariposa con timón hierro dúctil: https://orbe.com.pe/producto/valvula-mariposa-con-timon-hierro-ductil/
- Válvulas Mariposa: https://www.fiorellarepre.com.pe/valvulas/mariposa
- VALVULA MARIPOSA BRIDA HIERRO DUCTIL: https://icofesa.com/producto.php?id=22726
- VALVULA MARIPOSA TIPO LUG HIERRO DUCTIL: https://icofesa.com/producto.php?id=22772
- VALVULA MARIPOSA WAFER HIERRO DUCTIL: https://icofesa.com/producto.php?id=22590
- VALVULA MARIPOSA WAFER HIERRO DUCTIL SUBTERRANEA VASTAGO EXTENDIDO: https://icofesa.com/producto.php?id=20166
- ICOFESA S.A.: https://icofesa.com/

### Q4. válvula check hierro dúctil Lima venta

- Válvula dúo check hierro dúctil - Redline Perú: https://redlineperu.pe/producto/valvula-duo-check-hierro-ductil/
- Válvulas Check: https://www.fiorellarepre.com.pe/valvulas/check
- VALVULA CHECK HIERRO DUCTIL: https://icofesa.com/producto.php?id=19734
- VALVULA CHECK HIERRO DUCTIL: http://www.icofesa.com/producto.php?id=22319
- VALVULA CHECK HIERRO DUCTIL: https://icofesa.com/producto.php?id=15598
- VALVULA CHECK HIERRO DUCTIL: https://icofesa.com/producto.php?id=16768
- VALVULA CHECK HIERRO DUCTIL: https://www.icofesa.com/producto.php?id=22164
- VALVULA CHECK HIERRO DUCTIL: http://www.icofesa.com/producto.php?id=21350
- ICOFESA S.A.: https://icofesa.com/

### Q5. válvula de aire triple efecto agua potable Perú

- valvulas de aire segun sedapal para el peru: https://www.slideshare.net/slideshow/valvulas-de-aire-segun-sedapal-para-el-peru/272478547
- ESPECIFICACIÓN TÉCNICA Código Revisión Aprobado Fecha Página : : : : :: https://cdn.www.gob.pe/uploads/document/file/5976797/5295689-ctps-et-017-rev-02.pdf?v=1712669896
- Válvula de aire de triple función de Hierro Dúctil - Marca Kallpa: http://kallpa-peru.com/cmrclytcnc/cmrclytcnc16/cmrclytcnc1607/fchstcncs/FCHSTCNCSKLLP/FCHSTCNCSKLLP16/FCHSTCNCSKLLP1607/VLVLS/KALLPA%20-%20VALVULA%20DE%20AIRE%20DE%20TRIPLE%20FUNCION%20DE%20HD.pdf
- Válvulas de aire - Redes de agua potable - Infraestructura > HIDROPLAST: https://www.hidroplast.net/subrubro/valvulas-de-aire.html
- Válvula de Aire Triple Efecto Flowram: Especificaciones y Aplicaciones - Studocu: https://www.studocu.com/pe/document/universidad-privada-de-tacna/abastecimiento-de-agua-y-alcantarillado/valvula-de-aire-triple-efecto-flowram/75627153
- Valvula de aire triple efecto: https://asocieperu.com/producto/valvula-de-aire-triple-efecto/
- Valvula de aire bridado triple efecto: https://asocieperu.com/producto/valvula-de-aire-bridado-triple-efecto/
- ESPECIFICACIÓN TÉCNICA Código Revisión Aprobado Fecha Página : : : : :: https://cdn.www.gob.pe/uploads/document/file/5976798/5295689-ctps-et-018-rev-02.pdf?v=1712781111
- VALVULA DE AIRE PVC: https://icofesa.com/producto.php?id=19867
- Valvula de aire triple funcion: https://asocieperu.com/producto/valvula-de-aire-triple-funcion/

### Q6. tubería hierro dúctil K9 Perú proveedor

- Especificaciones de Tuberías K9: https://es.scribd.com/document/419413121/06-PET-K9
- Tubería de Hierro Ductil ISO 2531 - EATHISA PERU: https://web.eathisa.com.pe/2018/05/tuberia-de-hierro-ductil-iso-2531.html
- Tuberías de Hierro Dúctil - PATMO PERÚ: https://patmoperu.com/tuberias/hierro-ductil/
- TUBERIA HD P. EPOXICA K9 / C-40 U/F - Grupo Hidraulica: https://grupohidraulica.com/producto/tuberia-hd-p-epoxica-k9-c-40-u-f/
- Tuberías de Hierro Dúctil K9 y K7 para Redes de Agua y ...: https://www.hiperusac.com.pe/producto/tuberias-hierro-ductil/
- Venta de tubería y accesorio en hierro dúctil en Perú: https://romicorp.com.pe/hierro-ductil-accesorio.html
- PLIEGO DE ESPECIFICACIONES TÉCNICAS TUBERÍA EN HIERRO DÚCTIL K9: https://icofesa.com/sistema/fichastecnicas/Tuberia%20Ductil%20K9%205.5%20Mt%20Pam.pdf
- TUBO HIERRO DUCTIL: https://icofesa.com/producto.php?id=14659
- TUBO HIERRO DUCTIL: https://www.icofesa.com/producto.php?id=20001

### Q7. tubería hierro dúctil ISO 2531 Lima precio

- Precio de Tubería Hierro Dúctil, obtenga la última lista de precios de Tubería Hierro Dúctil 2026 - Made-in-China.com: https://es.made-in-china.com/tag_search_product/Pipe-Ductile-Iron_Price_oesyuyn_1.html
- Tubos, accesorios (fittings), aditamentos y sus juntas de hierro dúctil para conducción de agua.: https://inteco.org/tienda/catalogo/INTEISO25312020
- Precios de TUBOS DE HIERRO DUCTIL - QuimiNet: https://www.quiminet.com/productos/tubos-de-hierro-ductil-77081752610/precios.htm
- Precios de Tubería hierro dúctil - QuimiNet: https://www.quiminet.com/productos/tuberia-hierro-ductil-116305550329/precios.htm
- NTP-ISO 2531-2015: Normativa sobre Tuberías y Accesorios de Hierro Dúctil - Studocu: https://www.studocu.com/pe/document/universidad-andina-del-cusco/saneamiento/ntp-iso-2531-2015-tuberias-y-accesorios-de-hd/107481401
- TUBO HIERRO DUCTIL: https://icofesa.com/producto.php?id=21436
- ICOFESA S.A.: https://icofesa.com/index.php
- TUBO HIERRO DUCTIL: https://icofesa.com/producto.php?id=24309
- Durable, Galvanized & Perforated 200mm Ductile Iron Pipes - Alibaba.com: https://www.alibaba.com/showroom/200mm-ductile-iron-pipes.html

### Q8. marco y tapa de buzón D400 hierro dúctil Lima

- Marco y tapa de buzón hierro dúctil D400: https://valvulasperu.pe/producto/marco-y-tapa-de-buzon-hierro-ductil-d400/
- Marco y tapa D400 - FUMOSAC: https://fumosac.com.pe/marco-y-tapa-d400/
- MARCO Y TAPA DE BUZON HD D400 NF EN124 - Grupo Hidraulica: https://grupohidraulica.com/producto/marco-y-tapa-de-buzon-hd-d400-nf-en124/
- Marco Cuadrado y tapa de hierro dúctil con 1 seguro D400: https://mylnegofersac.com/producto/marco-cuadrado-y-tapa-de-hierro-ductil-con-1-seguro-d400/
- MARCO-Y-TAPA-DE-BUZON.pdf: https://roalcomperu.com/wp-content/uploads/2024/03/MARCO-Y-TAPA-DE-BUZON.pdf
- Marco y Tapa de Buzón Hierro Dúctil D400 - Collaval Import: https://collavalimport.com/web/productos/marco-y-tapa-de-buzon-hierro-ductil-d400/
- MARCO Y TAPA BUZON D400: https://leoneblusac.com/producto.php?id=13566
- Marco y tapa de hierro dúctil para buzón| MeckaSAC: https://www.meckasacperu.com/marco-tapa-de-hierro-ductil-buzon.html
- Marco y Tapa De Buzón D400 Con Doble Seguro: https://citalyperu.com/product/marco-y-tapa-de-buzon-d400-con-doble-seguro/

### Q9. tapa de buzón hierro dúctil precio Perú

- MARCO Y TAPA HIERRO DUCTIL: https://theatlantic.pe/producto.php?id=21117
- Marco y tapa de buzón de hierro dúctil - Roalcom: https://roalcomperu.com/producto/marco-y-tapa-de-buzon-de-hierro-ductil/
- MARCO Y TAPA HIERRO DUCTIL: https://theatlantic.pe/producto.php?id=23147
- MARCO Y TAPA HIERRO DUCTIL - Theatlantic s.a.: https://theatlantic.pe/producto.php?id=23722
- MARCO Y TAPA HIERRO DUCTIL: https://theatlantic.pe/producto.php?id=15348
- MARCO Y TAPA HIERRO DUCTIL: https://leoneblusac.com/producto.php?id=13783
- Puerta de Hierro, Zapopan: https://en.wikipedia.org/wiki/Puerta_de_Hierro,_Zapopan
- MARCO Y TAPA HIERRO DUCTIL: https://icofesa.com/producto.php?id=15942
- marco y tapa hierro ductil - LEONEBLU SAC: http://www.leoneblusac.com/producto.php?id=13991

### Q10. rejilla pluvial sumidero hierro dúctil Perú

- Rejilla Pluvial D-400: Especificaciones y Usos: https://www.scribd.com/document/514730016/rejilla-ffd-d400-1000x475-1
- FICHAS TÉCNICAS DE SUMIDEROS, TAPAS Y REJILLAS DE HIERRO Página 1 de 8 1: https://portal.compraspublicas.gob.ec/sercop/wp-content/uploads/2022/06/Fichas-T%C3%A9cnicas_Sumideros-Tapas-y-Rejillas-de-Hierro.pdf
- 1 NORMA TÉCNICA O.S. 060 DRENAJE PLUVIAL URBANO Artículo 1. OBJETIVO: https://www.saludarequipa.gob.pe/desa/archivos/Normas_Legales/saneamiento/OS.060.pdf
- Reja para sumidero horizontal de hierro dúctil: https://www.minfraestructura.com.ar/productos/pluvial/sumideros/reja-sumidero-horizontal-hierro-ductil/
- Rejilla Sumidero en Hierro Dúctil EN124: https://equihersas.com/producto/rejilla-sumidero-hierro-ductil-en124/
- Rejillas Para Sumideros: https://fundiec.com/rejillas_para_sumideros.htm
- Rejilla de fundición dúctil de 500 mm de largo empotrar Clase E-600: https://www.tapasyregistros.com/rejillas-e-imbornales/262-rejilla-de-fundicion-ductil-de-largo-500-mm-de-empotrar-clase-e-600.html
- Rejilla de metal 0.40m - Prefabricados CIFA: https://prefabricadoscifa.com/linea-de-productos/urbanizacion/regillas/rejilla-de-hierro-ductil/rejilla-de-metal-0-40m/
- CE.040 DRENAJE PLUVIAL_RM 126-2021-VIVIENDA.pdf: https://cdn.www.gob.pe/uploads/document/file/2366728/CE.040%20DRENAJE%20PLUVIAL_RM%20126-2021-VIVIENDA.pdf
- Acueducto: REJILLA CON MARCO PARA SUMIDERO: https://www.colfergroup.com/productos/acueducto/rejilla-con-marco-para-sumidero-detail

### Q11. válvula reductora de presión hierro dúctil Perú proveedor

- Válvula Reguladora de Presión - Hi Perú: https://www.hiperusac.com.pe/producto/valvula-reguladora-de-presion/
- Válvula Reductora de Presión de Hierro Dúctil - Roalcom: https://roalcomperu.com/producto/valvula-reductora-de-presion-de-hierro-ductil/
- Válvula reductora de presión bridado hierro dúctil: https://orbe.com.pe/producto/valvula-reductora-de-presion-bridado-hierro-ductil/
- Repuestos Industriales Peru, Valvulas Reductora de Presion: https://www.fullcontrolperu.com/valvula-reductora-presion.html
- Inicio old - Valvoline Perú: https://www.valvoline-peru.com/
- ICOFESA S.A.: https://icofesa.com/
- Valvula reductora de presion: https://asocieperu.com/producto/valvula-reductora-de-presion-2/
- VALVULA DE CONTROL DE NIVEL HIERRO DUCTIL: https://icofesa.com/producto.php?id=23315
- Valvula reductora de presion: https://asocieperu.com/producto/valvula-reductora-de-presion/

### Q12. válvula compuerta para tubería HDPE acerrojada Perú

- Válvula compuerta acerrojada para tubería HDPE: https://www.valvulasperu.com.pe/producto/valvula-compuerta-acerrojada-para-tuberia-hdpe/
- Válvula compuerta acerrojada para tubería HDPE: https://valvulasperu.pe/producto/valvula-compuerta-acerrojada-para-tuberia-hdpe/
- Válvula compuerta bridada con adaptador rápido para tubería HDPE: https://valvulasperu.pe/producto/valvula-compuerta-bridada-con-adaptador-rapido-para-tuberia-hdpe/
- Accesorios Hierro Dúctil archivos - Hi Perú: https://www.hiperusac.com.pe/categoria-producto/accesorios-hierro-ductil/
- Collaval Import: https://collavalimport.com/
- Válvula Compuerta Bridada Con Adaptador Brida Acerrojado Para Tubería HDPE - Collaval Import: https://collavalimport.com/productos/valvula-compuerta-bridada-con-adaptador-brida-acerrojado-para-tuberia-hdpe/
- Tuberías y accesorios para agua potable — página 3 — Concretmarco: https://tuberiaspvc.pe/catalogo/saneamiento/saneamiento-agua-potable/pagina/3
- Válvula de Compuerta Vástago fijo PN16, extremos Autoblocantes para Polietileno HDPE/PEAD: https://fimaca.com/product/valvula-compuerta-pn16-pead/
- Valvula compuerta acerrojada para tuberia HDPE: https://asocieperu.com/producto/valvula-compuerta-acerrojada-para-tuberia-hdpe/

### Q13. conexiones bridadas hierro dúctil tee codo Perú

- Tee Bridado de Hierro Dúctil - Redline Perú: https://redlineperu.pe/producto/tee-bridado-de-hierro-ductil/
- Conexiones de Hierro Dúctil archivos - Redline Perú: https://redlineperu.pe/categoria-producto/conexiones/conexiones-de-hierro-ductil/
- Tee bridado hierro dúctil: https://orbe.com.pe/producto/tee-bridado-hierro-ductil/
- Conexiones Bridadas Hierro Dúctil archivos - Valvoline Perú: https://www.valvoline-peru.com/categoria-producto/conexiones-bridadas-hierro-ductil/
- Codo 90° Hierro Dúctil Bridado - Valvoline Perú: https://www.valvoline-peru.com/producto/codo-90-hierro-ductil-bridado/
- Tee Bridado de Hierro Dúctil NEGRO: https://confundsac.com/producto/tee-bridado-de-hierro-ductil-negro/
- Tee Con Reducción Bridado Hierro Dúctil: https://citalyperu.com/product/tee-con-reduccion-bridado-hierro-ductil/
- TEE HIERRO DUCTIL: https://icofesa.com/producto.php?id=16672
- CODO BRIDADO: https://icofesa.com/producto.php?id=19277

### Q14. válvulas para minería relaves Perú proveedor hierro dúctil

- Válvulas y Accesorios en Hierro Dúctil: https://www.facebook.com/GyRNegociosComerciales/
- División Suministros: https://tecval.pe/division-suministros/
- Collaval Import: https://collavalimport.com/
- Inicio old - Valvoline Perú: https://www.valvoline-peru.com/
- Válvulas para minería cuchillas pinch check - Válvulas ...: https://valvulasmineras.com/
- Experiencia en Suministros: https://tecval.pe/experiencia-en-suministros/
- Válvulas Industriales: https://corsaflex.com/tienda/valvulas-industriales/
- ICOFESA S.A.: https://icofesa.com/
- Válvulas: https://www.fiorellarepre.com.pe/valvulas

### Q15. válvulas hierro dúctil riego agrícola Perú

- VALVULA COMPUERTA DE HIERRO DUCTIL - Termofusion y Riego Peru SAC: https://termofusion-riego.com/producto/valvula-compuerta-de-hierro-ductil/
- VALVULA MARIPOSA TIPO PALANCA DE HIERRO DUCTIL: https://termofusion-riego.com/producto/valvula-mariposa-tipo-palanca-de-hierro-ductil
- Válvulas y Accesorios para Riego Agrícola: https://valmevm.com/aplicaciones/riego-agricola/
- Rivali Perú - Válvulas Industriales y Sistemas Contra incendios: https://rivaliperu.com/
- Válvulas Hidráulicas riego agrícola - Fuente Jardín: https://www.fuentejardin.com/465-valvulas-hidraulicas-riego-agricola
- ACCESORIOS EN HIERRO DUCTIL: https://termofusion-riego.com/categoria-producto/hierro-ductil/
- Válvula Compuerta Bridada hierro dúctil: https://rivaliperu.com/producto/valvula-compuerta-bridada-hierro-ductil/
- Valvulas de hierro dúctil sidertecnica - Sidertecnica: https://sidertecnica.com.ec/valvulas-de-hierro-ductil-sidertecnica/
- ICOFESA S.A.: https://icofesa.com/

### Q16. proveedor válvulas agua potable SEDAPAL especificación técnica hierro dúctil

- ESPECIFICACIÓN TÉCNICA Código Revisión Aprobado Fecha Página : : : : :: https://www.sedapal.com.pe/storage/objects/ctps-et-019-valvula-reductora-presion-hidraulica.pdf
- ESPECIFICACIÓN TÉCNICA Código Revisión Aprobado Fecha Página : : : : :: https://www.sedapal.com.pe/storage/objects/ctps-et-017-valvula-de-hierro-ductil-3-funciones-ap.pdf
- ESPECIFICACIÓN TÉCNICA Código Revisión Aprobado Fecha Página : : : : :: https://www.sedapal.com.pe/storage/objects/ctps-et-041-valvula-de-control-de-bomba-para-agua-potable.pdf
- Especificaciones Técnicas de Sedapal: https://es.scribd.com/document/379951273/13-Especificaciones-Tecnicas-Sedapal
- ESPECIFICACIÓN TÉCNICA Código Revisión Aprobado Fecha Página : : : : :: https://www.sedapal.com.pe/storage/objects/ctps-et-034-filtro-tipo-cesto.pdf
- ESPECIFICACIÓN TÉCNICA Código Revisión Aprobado Fecha Página : : : : :: https://cdn.www.gob.pe/uploads/document/file/5976781/5295689-ctps-et-008-instalacion-reahibiltacion-y-reposicion-de-lineas-de-agua-potable.pdf?v=1735564307
- Especificaciones tecnicas generales sedapal: https://www.slideshare.net/slideshow/especificaciones-tecnicas-generales-sedapal/62578392
- ESPECIFICACIÓN TÉCNICA Código Revisión Aprobado Fecha Página : : : : :: https://cdn.www.gob.pe/uploads/document/file/5976787/5295689-ctps-et-013-valvula-de-compuerta-de-fierro-fundido-ductil-para-agua-potable.pdf?v=1709664884
- ESPECIFICACIÓN TÉCNICA Código Revisión Aprobado Fecha Página : : : : :: https://cdn.www.gob.pe/uploads/document/file/5976798/5295689-ctps-et-018-rev-02.pdf?v=1712781111
- Especificaciones Técnicas y Reglamentos Técnicos - Contenido institucional - Servicio de Agua Potable y Alcantarillado de Lima - Plataforma del Estado Peruano: https://www.gob.pe/37508-servicio-de-agua-potable-y-alcantarillado-de-lima-especificaciones-tecnicas-y-reglamentos-tecnicos

### Q17. importador válvulas hierro dúctil Perú distribuidor

- Hi Perú SAC - Especialistas en Válvulas Industriales y Línea HDPE: https://www.hiperusac.com.pe/
- Válvulas Perú: https://valvulasperu.pe/
- Collaval Import: https://collavalimport.com/
- Rivali Perú - Válvulas Industriales y Sistemas Contra incendios: https://rivaliperu.com/
- A.C. TRADING COMPANY: https://www.valvulasperu.com.pe/
- Fiorella Representaciones S.A.C.: https://www.fiorellarepre.com.pe/
- Inicio old - Valvoline Perú: https://www.valvoline-peru.com/
- ICOFESA S.A.: https://icofesa.com/index.php
- Válvulas: https://www.fiorellarepre.com.pe/valvulas

### Q18. válvula flotadora bridada control de nivel Perú

- Válvula Flotador 1 PuLG 10bar - Automático Control De Nivel: https://articulo.mercadolibre.com.pe/MPE-680293140-valvula-flotador-1-pulg-10bar-automatico-control-de-nivel-_JM
- Válvula Flotador 1 1/2 PuLG 10bar - Autom Control De Nivel: https://articulo.mercadolibre.com.pe/MPE-692474444-valvula-flotador-1-12-pulg-10bar-autom-control-de-nivel-_JM
- VALVULA Y FLOTADOR 2" - rotoplas: https://www.rotoplas.com.pe/valvula-y-flotador-de-2-plg-310222/p
- Válvula de Flotador - Control Preciso de Nivel I VTS Suppliers: https://www.vts.com.pe/valvula-y-flotador/
- VALVULA FLOTADORA CONTROL DE NIVEL HIERRO DUCTIL: https://icofesa.com/producto.php?id=18921
- VALVULA DE CONTROL DE NIVEL HIERRO DUCTIL: https://icofesa.com/producto/valvula-de-control-de-nivel-hierro-ductil-150mm-22556
- ICOFESA S.A.: https://icofesa.com/
- Válvula de control de nivel de flotador eléctrico FLEL serie 500: https://backup.dudesign.pe/alhisac/producto/valvula-de-control-de-nivel-de-flotador-electrico-flel-serie-500/
- VALVULA DE CONTROL DE NIVEL HIERRO DUCTIL: https://icofesa.com/producto.php?id=21992

### Q19. válvulas y tuberías hierro dúctil Arequipa Trujillo Piura proveedor

- Proveedores de Tubería de hierro ductil - Teléfonos, Distribuidores, Productores y Fabricantes - QuimiNet: https://www.quiminet.com/proveedores/tuberia-de-hierro-ductil-5142032560.htm
- Tubería hierro dúctil bridado: https://www.valvulasperu.com.pe/producto/tuberia-hierro-ductil-bridado/
- Tubos de Hierro Dúctil - Koplast Industrial - Alta resistencia: https://www.koplastindustrial.com/producto/tubos-de-hierro-ductil/
- Venta de tubería y accesorio en hierro dúctil en Perú: https://romicorp.com.pe/hierro-ductil-accesorio.html
- Vaneco: https://www.vaneco.com.pe/
- Fiorella Representaciones S.A.C.: https://www.fiorellarepre.com.pe/
- Válvulas Industriales, La Mejor Calidad, Acorsa Peru.: https://www.acorsaperu.com/linea-hidraulica/valvulas-industriales/
- Eurotubo: https://eurotubo.com.pe/
- Válvulas: https://www.fiorellarepre.com.pe/valvulas

### Q20. FUNDIGSAC válvulas hierro dúctil

- VÁ VÁ VÁ VÁLVULAS LVULAS LVULAS LVULAS FUNDICIÓN NOD FUNDICIÓN NOD: https://www.tubacero.com.uy/pdf/Valvulas_Hierro_Fundido.pdf
- Diferencia entre válvulas de fundición dúctil y válvulas de acero fundido: https://www.bundorvalve.es/noticia/342.html
- Válvula Mariposa Excéntrica: https://fundigsac.com/product/valvula-mariposa-excentrica/
- Válvula Check Swing: https://fundigsac.com/product/valvula-check-swing/
- Válvula Compuerta Bridada: https://fundigsac.com/product/valvula-compuerta-bridada/
- FUNDIGSAC: https://fundigsac.com/
- Válvula Check Flex: https://fundigsac.com/product/valvula-check-flex/
- Válvula Guillotina: https://fundigsac.com/product/valvula-guillotina/
- Válvula Embone Tipo Luflex: https://fundigsac.com/product/valvula-embone-tipo-luflex/
- Válvula Compuerta Bridada de Hierro Dúctil: https://confundsac.com/producto/valvula-compuerta-bridada-de-hierro-ductil/

## 4. Controles de esta revisión

| Control | Método | Resultado |
|---|---|---|
| Empresas con ficha y datos | 12 del listado frente a `sitios/` y `datos/` | 12 de 12 |
| Empresas vistas en búsquedas sin clasificar | Dominios de C1 a C11 y Q1 a Q19 frente a `COMPETIDORES.md` | Todas clasificadas tras la corrección. Antes faltaban, entre otras, Valvoline Perú, Grupo Hidráulica, The Atlantic, Orbe, Asocie Perú y Redline Perú |
| Columna de búsquedas C1 a C11 | Salida original frente a `COMPETIDORES.md` | 12 de 12 empresas coinciden |
| Tabla Q1 a Q20 y conteo de presencia | Salida original frente al informe | 20 de 20 filas coinciden |
| Indicadores 6.3 de competidores | Recalculados desde `datos/*.json` | 11 de 11 filas coinciden. Válvulas Perú no tiene datos |
| Peso de HTML en 6.2 | Media por página desde `datos/*.json` | 11 de 11 coinciden en KiB |
| Tabla de KPI, sección 9 del informe | Medianas de las 84 corridas | 28 de 28 combinaciones de ruta y factor coinciden |
| Rastreo propio de FUNDIGSAC, 31 páginas | Repetido sobre la compilación local `.next-kpi` de las 12:23, sin cambiar el código | Título, meta, un H1 y canónica en 31 de 31; `Organization` y `WebSite` en 31; `BreadcrumbList` en 16; `Product` en 10, sin `Offer`; `LocalBusiness` en 0; `tel:` en 31; WhatsApp en 29; 4 títulos de más de 60 caracteres, máximo 62 |
| Catálogo de FUNDIGSAC | Conteo en `catalog.ts` y `catalog-pdf.ts` | 69 referencias: 14 base y 55 añadidas. 28 URL en el sitemap, 10 fichas |
| RUC | Dígito verificador | V-01 confirmado: el último dígito debería ser 9. El RUC de Negofer sí lo cumple |
| Longitud de títulos y descripciones del plan | Conteo de caracteres de cada fila | 53 filas: 0 con recuento erróneo, 0 fuera de los límites de 60 y de 120 a 158 caracteres, 0 duplicadas |

Correcciones hechas a raíz de estos controles:

- Se registró que Válvulas Perú no tiene datos en el propio listado de competidores.
- Se corrigieron en `COMPETIDORES.md` datos superados por el rastreo sobre Mecka, EATHISA, Inccosac, FUMOSAC y Collaval.
- El mapa de palabras clave cubre ahora equipos, bridas, juntas, acoples, SCH-40, mariposa inox, aire roscada, check vertical, las tarjetas de tubería y tapas, y más consultas por sector.
- Se documentó la coincidencia de dirección entre FUNDIGSAC y M&L Negofer (V-02), y se añadieron V-23, V-24 y V-25.
- Se advirtió en las fichas que las normas de `data.ts` no son datos verificados.

### KPI del sitio

**No están en verde.** La última medición completa da 14 de 14 rutas en verde en escritorio y 0 de 14 en móvil, con LCP de 3.535 a 5.256 ms frente a un máximo de 2.500 ms. La revisión de estos documentos no modificó el código del sitio, por lo que no cambia ese resultado.

## 5. Lo que sigue sin respaldo o sin medir

| Asunto | Situación | Qué hace falta |
|---|---|---|
| Rendimiento real de competidores | n/d en 12 de 12 | Clave de API de PageSpeed |
| Volumen, posiciones reales, clics y enlaces entrantes | Sin datos | Search Console y una herramienta de palabras clave |
| Declaraciones de competidores sobre normas, certificados, marcas y SEDAPAL | Sin verificar | Fuentes externas si se van a usar en un argumento comercial |
| Empresas no rastreadas | Fiorella, Valvoline Perú, Grupo Hidráulica y las demás de `COMPETIDORES.md` | Ampliar el rastreo con las mismas reglas |
| Válvulas Perú | Sin datos | WHOIS de punto.pe y decisión sobre `valvulasperu.com.pe` |
| Muestras parciales | Ver sección 2 | Nueva ronda con cupo autorizado |
| Comprobación de la ficha 404 de Inccosac | Solo consta en `sitios/inccosac.md`; el archivo temporal no se conservó | Repetirla si se usa como argumento |
| Nombres de EPS y vocación regional del plan | Conocimiento general | Registro de SUNASS |
| Datos propios de FUNDIGSAC | V-01 a V-25 abiertos | Documentos de la empresa |
| `scrape.py` | Defectos conocidos en la clasificación de fichas y el filtro de rutas | Corregir el script antes de otra ronda |
