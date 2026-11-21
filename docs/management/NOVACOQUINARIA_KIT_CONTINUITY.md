---
id: DOC-CONTINUIDAD-2026
titulo: Kit de continuidad de NovaCoquinaria
tipo: gestion
version: 2.7.0
estado: estable
ultima_revision: 2026-11-21
---

# Kit de continuidad de NovaCoquinaria

> **Repositorio:** [fran-eliot/NovaCoquinaria](https://github.com/fran-eliot/NovaCoquinaria)  
> **Arquitectura conceptual:** GASTRO — Sistema de Gestión del Conocimiento Culinario (SGCC)  
> **Corte de información:** 21 de noviembre de 2026, tras la integración técnica de Culinary Planner (merge #303), con publicación confirmada en gh-pages y uso manual aún pendiente.  
> **Naturaleza:** documento de traspaso operativo; no reemplaza la documentación oficial ni el estado vigente de GitHub.

## 1. Identidad y propósito

NovaCoquinaria es un proyecto personal de ingeniería del conocimiento culinario. Su finalidad es capturar, estructurar, relacionar y reutilizar conocimiento de ingredientes, técnicas, bases, patrones, tablas, platos, variantes y recetas. No se limita a un recetario.

**GASTRO** designa la arquitectura conceptual; **NovaCoquinaria**, su aplicación práctica. El principio rector es **«Documentar una vez. Relacionar siempre. Reutilizar continuamente.»**

Referencias: [identidad](../../NovaCoquinaria.md), [visión](../VISION.md), [arquitectura](../architecture/ARQUITECTURA.md), [modelo de conocimiento](../architecture/MODELO_DE_CONOCIMIENTO.md).

## 2. Estado comprobado en este corte

| Elemento | Situación y alcance de la evidencia |
|---|---|
| Rama principal | `main`, consultada el 2026-11-21 después de #297 |
| Última versión publicada | [`v1.6.0`](https://github.com/fran-eliot/NovaCoquinaria/releases/tag/v1.6.0), 2026-11-19 |
| Fase estratégica | Explotación práctica; Explorer, Recipe Assistant, Pantry y Shopping desplegados; Planner integrado y desplegado; prueba manual pública pendiente |
| Última PR fusionada | [#303](https://github.com/fran-eliot/NovaCoquinaria/pull/303) |
| Commit histórico del tag | [`836f02e848299c0a7a7897b22bb83cd13e0c373a`](https://github.com/fran-eliot/NovaCoquinaria/commit/836f02e848299c0a7a7897b22bb83cd13e0c373a) |
| Commit de main comprobado | `fd3ddc760788dc0a61749c514f964d51a126a527` |
| PR abiertas | Ninguna en la consulta del corte |
| Integridad | [Knowledge integrity de PR #297](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44697344018): success |
| Auditoría | [Knowledge audit de PR #297](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44697343958): success; 141 pruebas Python y 63 Node |
| Despliegue | gh-pages `936e5b4f3ae822c5d7bb9d656618ddce4210abf7` (Deployed fd3ddc7); ruta Planner comprobada en la rama; prueba manual de uso pendiente |
| Inventario Markdown | 927 archivos según inventario del job #246 |
| Recetas | 590 rutas y 590 documentos extraídos; Arroces 39; Pastas 37; Legumbres 61; Verduras 86; Carnes 82; Pescados y Mariscos 69; Cocina Asiática 44; Postres 82; Bebidas 36; Horno 54 |
| Despensa y técnicas | 126 fichas de ingrediente y 52 técnicas por ruta, excluidos índices y BACKLOG |
| Identificadores | Última secuencia editorial REC-0591 (Front Matter REC-591); REC-0592 candidato sujeto a verificar |
| Working tree local | No comprobado |

El inventario procede de los registros del job #246 (snapshot 7249024567f5f74d0dd6c6c7d9d78babf62ab67a, distinto del merge); no significa que 590 recetas hayan sido cocinadas. Las versiones de herramientas no son releases del proyecto. El contrato de datos está en [CONTRATO_DE_DATOS_DE_RECETAS](../specifications/knowledge/CONTRATO_DE_DATOS_DE_RECETAS.md).

## 3. Evolución y decisiones relevantes

- **2026-06-29:** creación del proyecto y primeras recetas estructuradas.
- **2026-07-01:** evolución conceptual desde recetario hacia SGCC.
- **2026-07-05:** primera versión estable `v1.0.0`, según la documentación histórica.
- **2026-07-06 a 2026-07-09:** incorporación de MkDocs y Knowledge Graph, manteniendo Markdown como fuente de verdad.
- **2026-08-02:** marco de especificaciones `v1.5.0` y decisión estratégica de priorizar el conocimiento culinario sobre la implementación de la plataforma software.
- **2026-11-14:** sucesión de mejoras de estructura, integridad, navegación, seguridad alimentaria y contenido; después de la PR #67 se intensifican las incorporaciones temáticas de recetas, técnicas e ingredientes.
- **PRs #84–#86:** bloques de técnicas; **#87–#100:** ampliaciones progresivas del catálogo de Despensa, incluido el lote de seis ingredientes por PR. Se registran como progreso editorial, sin convertir cada PR en hito histórico de Bitácora.
- **PR #100:** incorporación de `ING-0120` a `ING-0125` (guanciale, panceta curada, apio, laurel, vino tinto para cocinar y concentrado de tomate).
- **PRs #102–#105:** 24 recetas nuevas distribuidas entre verduras, legumbres, pastas, mariscos, arroces, carnes, postres y bebidas.
- **PRs #106–#114:** recuperación de experiencias de cocina, ajustes, valoraciones y separación entre recetas consultadas y elaboraciones confirmadas. Incluye la corrección del acabado con lemon curd en el pastel de manzana.
- **PR #115:** consolidación del criterio de evolución de recetas: preservar versiones preferidas, separar antecedentes e impedir sustituciones retrospectivas sin evidencia comparativa.
- **PR #116:** cangrejo rojo cocido al ajillo como **propuesta no probada** y antecedentes diferenciados de ternera con bambú y tarta de galletas y natillas.

### Expansión posterior al corte de la PR #116

- **PR #117:** creación de este kit de continuidad como punto estable de recuperación del proyecto.
- **PRs #118–#122:** recuperación de recetas asiáticas, legumbres, horno y experiencias domésticas, manteniendo separadas las preparaciones probadas de las propuestas.
- **PR #123:** registro de tandas y criterio de comparación entre elaboraciones; las fórmulas posteriores no se consideran automáticamente mejores.
- **PRs #124–#138:** ampliación por módulos con seis recetas por tanda y documentación de preparaciones personales, entre ellas magret de pato y versiones habituales de cocina.
- **PRs #139–#141:** plantillas reutilizables de salsas, marinadas y cocciones; no confundir patrones culinarios con recetas probadas.
- **PRs #142–#158:** diecisiete tandas consecutivas de seis recetas por PR, distribuidas entre pescados, pastas, arroces, bebidas, carnes, horno, legumbres, verduras, cocina asiática y postres. El identificador más reciente de esta secuencia es `REC-0399` en el módulo de Legumbres.
- **PR #158:** seis fichas de ful medames, rajma masala, gigantes plaki, ensalada de lentejas con granada, tajín de garbanzos y crema untable de guisantes. Sus elaboraciones y valoraciones siguen **pendientes de prueba doméstica**.

### Actualización de continuidad: PRs #159–#176

- **PR #159:** actualización anterior del kit de continuidad a la versión `1.3.0`, con corte situado en la PR #158.
- **PRs #160–#162:** 18 propuestas nuevas de verduras, cocina asiática y postres, con identificadores `REC-0400`–`REC-0417`.
- **PRs #163–#176:** catorce tandas consecutivas de **seis recetas tradicionales españolas**: **84 fichas**, numeradas desde `REC-0418` hasta `REC-0501`. Las propuestas abarcan múltiples cocinas regionales y técnicas de guiso, legumbres, pescados, arroces, horno, verduras y repostería.
- **PR #176:** última tanda de aquel corte de seis platos: [habas a la catalana](../../04_Verduras/habas_a_la_catalana_con_menta_y_morcilla.md), [escaldums mallorquins](../../05_Carnes/escaldums_mallorquins_de_pollo_y_almendras.md), [rabas cántabras](../../06_Pescados_y_Mariscos/rabas_cantabras_de_calamar_rebozado.md), [papas con choco](../../06_Pescados_y_Mariscos/papas_con_choco_gaditanas.md), [pantxineta](../../08_Postres/pantxineta_vasca_de_hojaldre_crema_y_almendras.md) y [nevaditos](../../08_Postres/nevaditos_castellanos_de_manteca_y_vino_blanco.md).
- **Estado editorial:** las tandas de recetas regionales nuevas se registran como `receta-propuesta` y `pendiente-de-prueba`; su fusión y CI correctas no acreditan haberlas elaborado.
- **Prioridad vigente en este corte:** continuar la expansión de cocina tradicional española, con variedad geográfica, métodos diferenciados y sin repetir recetas del repositorio. No forzar la continuidad temática si una futura decisión cambia las prioridades.
- **Resultado comprobado de #176:** fusionada en `main` con integridad y despliegue MkDocs exitosos, sin PR abiertas en la consulta.

### Actualización de continuidad: PRs #177–#187

- **PR #177:** actualización del kit a la versión documental `1.4.0`, con corte tras #176.
- **PRs #178–#181:** tandas XV–XVIII, 24 recetas (`REC-0502`–`REC-0525`).
- **PRs #182–#187:** tandas XIX–XXIV, 36 recetas (`REC-0526`–`REC-0561`).
- **Balance de la serie #163–#187:** 24 tandas de seis fichas (144 propuestas), con #177 dedicada exclusivamente al kit. La numeración editorial se representa con cuatro dígitos; el Front Matter de las fichas recientes utiliza IDs de tres dígitos. No renumerar retrospectivamente sin una revisión específica.
- **PR #187:** [arroz a la zamorana](../../01_Arroces/arroz_a_la_zamorana_con_productos_del_cerdo.md), [calçots al horno](../../04_Verduras/calcots_asados_al_horno_con_salsa_romesco.md), [sopa de picadillo](../../05_Carnes/sopa_de_picadillo_andaluza_de_pollo_y_jamon.md), [besugo a la madrileña](../../06_Pescados_y_Mariscos/besugo_a_la_madrilena_al_horno.md), [mantecados de Estepa](../../08_Postres/mantecados_de_estepa_de_almendra.md) y [broa gallega](../../10_Horno/broa_gallega_de_maiz_y_centeno.md).
- **Resultado comprobado:** #177–#187 fusionadas; integridad y despliegue del merge #187 exitosos. La próxima tanda candidata en aquel corte era XXV.
- **Alcance:** las 60 incorporaciones posteriores a #176 siguen siendo propuestas pendientes de prueba doméstica. No se modifica la fase estratégica, la identidad ni la última release del proyecto.

### Actualización de continuidad: PRs #188–#194

- **#188:** actualización del kit v1.5.0.
- **#189–#193:** tandas XXV–XXIX; 30 propuestas (REC-0562–REC-0591). Balance de la serie: 174 fichas en 29 tandas.
- **#194:** propuesta de transición a consolidación y explotación del conocimiento; el presente incremento alinea la documentación de gestión con dicha dirección. Próximo objetivo: línea base reproducible de auditoría, antes del contrato de datos y de cualquier prototipo de ingesta.

### Actualización de continuidad: PRs #195–#202

- **#195:** adopción de la fase de consolidación y explotación; actualización de PROJECT_STATUS, ROADMAP, BITACORA, kit v1.6.0 y CONSOLIDACION_CONOCIMIENTO.
- **#196:** workflow Knowledge audit, inventario reproducible de los diez módulos, prueba unitaria y generación de informes por commit.
- **#197:** registro de la línea base de #196 (37 avisos: 13 técnicas y 24 recetas).
- **#198:** relaciones reutilizables de 13 técnicas; auditoría posterior: 24 avisos.
- **#199:** cinco bebidas; 19 avisos.
- **#200:** seis postres y una masa; 12 avisos.
- **#201:** cinco recetas de Verduras; 7 avisos.
- **#202:** siete recetas de Arroces, Pastas, Legumbres, Carnes y Cocina Asiática; 0 avisos confirmados en main. Se preservaron formulaciones, estados de prueba y reglas del auditor.

### Actualización de continuidad: PRs #203–#228

- #203: kit v1.7.0 y cierre del primer ciclo de relaciones.
- #204–#210: revisión dirigida AUD-01–AUD-06, rutas canónicas, denominadores, coincidencias léxicas y precedencia de asociaciones; cierre con deuda residual.
- #211–#212: deuda editorial selectiva; ficha ING-0126 de harina de maíz no precocida.
- #213–#214: contrato de datos 0.1.0 y casos de aceptación.
- #215–#219: prototipo de extracción de metadatos, ingredientes, cantidades, procedimientos, evidencia, rendimientos, tiempos y referencias; informe de cobertura.
- #220–#222: línea base y revisión de 18 fichas con carencias de reconocimiento EXT-01.
- #223–#225: candidatos léxicos, muestras trazables y ampliación dirigida de alias EXT-02.
- #226–#228: evidencia doméstica con alcance (EXT-03), formatos declarados de rendimiento y tiempo (EXT-04), cantidades y opcionalidad (EXT-05).

### Actualización de continuidad: PRs #229–#235

- #229: cierre del extractor y kit 1.8.0.
- #230–#233: contrato, constructor básico, índices de ingredientes y contraste reproducible (IDX-01–IDX-04).
- #234–#235: motor de consultas Python/CLI y evaluación dirigida (QRY-01–QRY-02).

### Actualización de continuidad: PRs #236–#246

- #236: kit 1.9.0; cierre de la primera etapa de indexación y consultas y resolución del huérfano documental confirmada en CI.
- #237–#241: RET-D01–D04, investigación de recuperación textual y candidatos conservadores de identidad, síntesis y propuesta A.
- #242: [alcance de entrega](./ALCANCE_RECUPERACION_TEXTUAL.md), RET-01–RET-14 y cuatro unidades.
- #243–#246: núcleo léxico, integración del modo terms, contraste sobre dos corpus y cierre documental de consultas 0.2.0. Ambas validaciones de #246 satisfactorias. Sin nueva release.

### Actualización de continuidad: PRs #247–#249 y publicación

- #247: kit 2.0.0.
- #248: [revisión estratégica global](./REVISION_ESTRATEGICA_CULINARIA.md), propuesta de investigación de Culinary Compatibility Engine.
- #249: preparación documental de v1.6.0; merge `836f02e848299c0a7a7897b22bb83cd13e0c373a` con [integridad](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44528643404), [auditoría](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44528643088) y despliegue satisfactorios.
- 2026-11-19: publicación oficial de [v1.6.0 — Culinary Knowledge & Retrieval](https://github.com/fran-eliot/NovaCoquinaria/releases/tag/v1.6.0), tag verificado en el merge #249. El siguiente incremento en aquel corte era CCE-D01 (casos de uso y requisitos), no implementación.

### Actualización de continuidad: PRs #250–#267

- #250: sincronización posterior a publicación y kit 2.1.0.
- #251–#256: CCE-D01–D05; cinco escenarios documentales, 590 recetas indeterminadas sin confirmación. Entrega diferida.
- #257–#262: CRM-D01–D05; inventario de señales (2.030 de 5.047 ocurrencias, 573 recetas), contraste documental y modelo híbrido: 16/16 casos frente a 8/16 del plano atómico restringido; 20 ocurrencias anotadas manualmente.
- #263–#267: CRR-D01–D05; cuatro reglas acotadas, 351 propuestas sobre 358 ocurrencias, seis aciertos de diez positivos reservados, cinco negativos correctos, cuatro omisiones y ocho negativos sintéticos sin propuesta. La evidencia no acredita precisión global ni coste de revisión.
- Cierre: [deuda de requisitos](./DEUDA_REQUISITOS_CULINARIOS.md), siete propuestas sobre 14 ocurrencias; integración productiva diferida. Próximo paso: revisión estratégica de explotación práctica.

### Actualización de continuidad: PRs #268–#275

- #268: kit 2.2.0.
- #269–#270: revisión estratégica y alcance de Culinary Explorer 0.1.0.
- #271–#274: datos, búsqueda, interfaz e integración MkDocs. Esquema de catálogo 0.1.1; 590 destinos HTML, 134 pruebas y 62 contrastes acreditados en #274.
- #275: evidencia técnica y pruebas adicionales de teclado y catálogo vacío; los tres workflows de la PR superados.
- Publicación: la rama gh-pages contiene el despliegue de #275. Tras guardar la configuración Pages (gh-pages, raíz), el propietario confirmó la carga del [explorador](https://fran-eliot.github.io/NovaCoquinaria/culinary-explorer.html) con 590 recetas, 24 tarjetas y 25 páginas. No se acredita una prueba HTTP independiente ni todas las consultas remotas.
- Cierre acotado de [Culinary Explorer](./ALCANCE_CULINARY_EXPLORER.md); siguiente capacidad candidata: Culinary Recipe Assistant, con alcance breve antes de implementación. No hay nueva release.

### Actualización de continuidad: PRs #276–#281

- #276: cierre de Explorer y kit 2.3.0.
- #277: alcance del asistente 0.1.0, AST-01–AST-15.
- #278–#281: proyección por receta, sesión efímera, interfaz e integración. Cuerpo completo de fuente como contexto, temporizador manual, sin persistencia.
- #281: CI de PR satisfactorio, 141 pruebas Python, nueve Node, 62 contrastes, 590 recetas, 591 archivos y 51 destinos de técnicas; Chromium PASS para cuatro recetas y rechazo de datos inválidos.
- gh-pages registra el despliegue de #281; plantilla, manifiesto y enlace Preparar receta comprobados en la rama. Uso público del asistente pendiente.
- Próxima capacidad candidata: Culinary Pantry; no confundir inventario declarado con cocinabilidad ni afirmar compatibilidad.

Las PR aportan crecimiento editorial; su fusión y sus validaciones técnicas no prueban que las recetas se hayan cocinado. Los detalles por ficha se consultan en el índice de cada módulo.

La [Bitácora](./BITACORA.md) mantiene los hitos que cambian la identidad o trayectoria del proyecto. No debe convertirse en un registro cotidiano de PRs, commits o correcciones.

## 4. Capacidades y alcance real

**Disponibles o documentadas:** contrato de datos 0.1.0, extractor 0.4.6 en etapa recipe_projection_preview, informes reproducibles de cobertura y candidatos de identidad; índice 0.2.0 y motor de consultas 0.2.0 de solo lectura (text, terms, explicit, candidate), con evaluación automatizada; auditoría automatizada con informes por commit; organización por dominios y entidades Markdown con Front Matter, IDs, enlaces, tablas y plantillas; validadores estructurales; Knowledge Graph y herramientas de análisis semántico; MkDocs y documentación de arquitectura, gobernanza y especificaciones.

**En consolidación e incorporación selectiva:** el conocimiento culinario reutilizable en `00_Bases`, `01_Arroces`, `02_Pastas`, `03_Legumbres`, `04_Verduras`, `05_Carnes`, `06_Pescados_y_Mariscos`, `07_Cocina_Asiatica`, `08_Postres`, `09_Bebidas`, `10_Horno`, `11_Despensa`, `12_Plantillas` y `98_Tablas`. La expansión reciente ha dado especial profundidad a ingredientes y sus vínculos con recetas y técnicas.

### Actualización de continuidad: PRs #282–#289

- #282: cierre técnico del asistente y kit 2.4.0.
- #283–#284: formato Markdown seguro, URL por ID y recursos versionados por contenido; funcionamiento público comunicado por el propietario.
- #285: alcance de Pantry, PAN-01–PAN-15.
- #286–#289: modelo, persistencia, interfaz e integración. Almacenamiento local con clave novacoquinaria.culinary-pantry, esquema 0.1.0; transferencia efímera de nombres a Explorer mediante sessionStorage.
- #289: tres workflows satisfactorios; 141 Python, 30 Node y recorridos Chromium de las tres aplicaciones. 590 recetas; 591 archivos de asistente y 51 destinos de técnicas. Snapshot CI 2ba17bded8f2de3c365c51745f3377b9f0fd3a33.
- gh-pages contiene el despliegue del merge #289 y la plantilla de Pantry con recursos versionados. Verificación de uso público pendiente.
- Culinary Shopping se desarrolló en #291–#297 y Culinary Planner en #299–#303; siguiente capacidad por decidir. Sin nueva release.

### Actualización de continuidad: PRs #290–#297

- #290: cierre técnico de Pantry y kit 2.5.0.
- #291: alcance de Shopping 0.1.0, criterios SHP-01–SHP-15 y separación entre listas, inventario y recetas.
- #292–#294: modelo de listas, almacenamiento local versionado e interfaz.
- #295: selección de ocurrencias desde Recipe Assistant hacia Shopping, con cantidades de compra revisadas y procedencia literal, sin inferir faltantes.
- #296: intención de transferencia persistida antes de escribir Pantry y recuperación sin recreación automática.
- #297: revisión individual, Web Locks para transferencias cooperantes, contraste de destino y recorridos Chromium, incluidos fallos parciales.
- CI #297: 141 pruebas Python, 63 Node; cuatro recorridos Chromium correctos. Auditoría semántica sin advertencias ni documentos huérfanos. Las 590 recetas se mantienen; la proyección contiene 591 archivos y 51 destinos de técnicas.
- gh-pages `a6f541d03364dade49d0b0f61dd90a2480926496` publicó `765d507` y contiene `culinary-shopping.html` y `culinary-pantry.html` con referencias versionadas. No hay prueba manual pública documentada para Shopping ni Pantry.
- Próximo candidato: Culinary Planner, mediante decisiones explícitas y sin suponer compatibilidad, existencias suficientes, nutrientes o tiempos completos. No se aprueba una nueva release.

**Aplicación publicada:** Culinary Explorer 0.1.0, consumidor estático de solo lectura del índice, con título, menciones AND, módulo, evidencia y acceso a fichas; sin interpretación de disponibilidad.

**Asistente publicado:** Culinary Recipe Assistant 0.1.0, preparación guiada, checklist y temporizador manual sin persistencia; funcionamiento comunicado tras #284. Véase [alcance](./ALCANCE_CULINARY_RECIPE_ASSISTANT.md).

**Despensa personal desplegada:** [Culinary Pantry 0.1.0](./ALCANCE_CULINARY_PANTRY.md), inventario local versionado, copias JSON, filtros, lotes y transferencia de nombres mediante sessionStorage; prueba pública pendiente. No infiere compatibilidad ni suficiencia.

**Listas personales desplegadas:** [Culinary Shopping 0.1.0](./ALCANCE_CULINARY_SHOPPING.md), listas y artículos, selección explícita desde Assistant, registro de compras y transferencia revisada a Pantry mediante intención persistida y verificación; sin atomicidad entre almacenamientos, prueba pública pendiente.

**Planificador integrado:** [Culinary Planner 0.1.0](./ALCANCE_CULINARY_PLANNER.md), calendario civil semanal, comidas declaradas, referencias verificadas a recetas y copias locales. PR #303 fusionada; publicación en gh-pages verificada, uso público manual pendiente.

**Futuras o solo especificadas:** búsqueda sin diacríticos o semántica, ampliación de candidatos de identidad, filtros de tiempos y rendimientos, backend, API, sincronización de despensa, planificación, comparativas de precios y compras automatizadas, Runtime operativo, RAG/GraphRAG y agentes. No confundir una especificación con una función implementada.

**Documentación de gestión desfasada respecto al contenido:** [PROJECT_STATUS](./PROJECT_STATUS.md) se actualiza con este cierre; conserva sus cortes históricos; el [BACKLOG de Despensa](../../11_Despensa/BACKLOG.md) contiene casillas históricas sin sincronizar con numerosas fichas existentes. El backlog de Despensa no debe utilizarse como inventario actual.

## 5. Forma de trabajo acordada

- Coordinación y documentación culinaria en español; redacción natural, precisa y profesional.
- Para cada incremento, comprobar primero si la última PR está fusionada y si existen otras PR abiertas.
- Consultar el árbol vigente de `main`, la ficha o índice afectado y los IDs existentes antes de seleccionar contenidos. Preferir incorporar conocimiento nuevo y evitar duplicados.
- Crear una **rama temática** desde `main`, introducir cambios directamente en GitHub y abrir una PR dirigida a `main`.
- Agrupar, cuando el alcance lo permita, **seis fichas relacionadas** (ingredientes, recetas, técnicas u otras) con desarrollo sustantivo e índices o relaciones correspondientes. Los ajustes de gestión, integridad o mantenimiento pueden constituir una PR propia sin completar artificialmente un lote de seis.
- El propietario del proyecto **revisa, fusiona y elimina la rama remota**. No realizar esas acciones en su nombre.
- Entregar siempre el **enlace directo a la PR** en la conversación y verificar la ejecución de GitHub Actions. Si aparece un fallo, analizarlo y corregir en la misma rama y PR.
- Mantener frontmatter, identificadores únicos, rutas existentes, enlaces internos y relaciones semánticas útiles. Priorizar cantidades y procedimientos reproducibles, seguridad alimentaria y conservación.
- Diferenciar **receta propuesta**, **elaboración realizada**, **valoración confirmada** y **variante histórica**; consultar [Recetas cocinadas](./RECETAS_COCINADAS.md) y [Evolución de recetas](./EVOLUCION_DE_RECETAS.md).
- No sustituir una versión principal posterior por una formulación anterior sin comparación o preferencia explícita. Conservar cantidades recuperadas como antecedentes cuando no puedan atribuirse a la versión preferida.
- Evitar repetir pequeñas modificaciones de las mismas fichas cuando sea posible aportar conocimiento nuevo.
- No incorporar a recetas, fichas o descripciones de PR instrucciones internas de coordinación, comprobaciones de desarrollo ni referencias al asistente. Los detalles de validación se comunican en la conversación y los registros de CI.

## 6. Integridad y calidad del conocimiento

El procedimiento vigente de [consolidación del conocimiento](./CONSOLIDACION_CONOCIMIENTO.md) distingue controles estructurales bloqueantes de diagnósticos semánticos informativos:

- `python tools/validate_all.py`: Front Matter, IDs y enlaces internos.
- `tools/validate_semantics.py` y `tools/find_orphans.py`: diagnósticos de relaciones y documentos huérfanos; no son por sí solos controles bloqueantes.
- Los recuentos de advertencias y huérfanos dependen de la ejecución y del commit; no reutilizar cifras históricas como resultados actuales.
- La revisión documental de una receta no acredita por sí sola su ensayo práctico en cocina.

Los resultados, alcances y limitaciones se registran en [CONSOLIDACION_CONOCIMIENTO](./CONSOLIDACION_CONOCIMIENTO.md).

### Línea base y cierre del primer ciclo de relaciones

| Merge | Advertencias semánticas |
|---|---:|
| #196 | 37 |
| #198 | 24 |
| #199 | 19 |
| #200 | 12 |
| #201 | 7 |
| #202 | 0 |

El workflow [Knowledge audit](../../.github/workflows/knowledge-audit.yml) genera inventario de rutas Git, informes de dominios Markdown/JSON y registros estructurales y semánticos; conserva artefactos durante 30 días. El [job de #202](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44402431807/job/135148731325) confirma cero errores estructurales, cero advertencias semánticas y cero huérfanos globales según las reglas actuales. No acredita calidad semántica exhaustiva, ausencia de duplicidades conceptuales ni pruebas en cocina.

### Cobertura de dominios según auditoría de #202

| Dominio | Cobertura de tipos esperados | Madurez automática |
|---|---:|---|
| Currys | 100 % | Consolidado |
| Salteados asiáticos | 60 % | Estructurado |
| Arroces | 80 % | Consolidado |
| Pastas | 60 % | Estructurado |
| Legumbres | 80 % | Consolidado |
| Verduras | 100 % | Estructurado |
| Carnes | 100 % | Estructurado |
| Pescados y mariscos | 100 % | Estructurado |
| Huevos y lácteos | 100 % | Estructurado |
| Postres | 40 % | Exploración |

Todas las tasas de enlaces de dominio son 100 % según el auditor; Currys conserva un documento sin referencias salientes dentro de su diagnóstico, distinto del indicador global de huérfanos. El informe generado versionado de agosto sigue siendo histórico. Los resultados recientes provienen del registro del job, no de la inspección íntegra del ZIP.

### Líneas base históricas y prioridades vigentes

Corte #228: 590/590 recetas con ingredientes y pasos reconocidos; 5.047 ocurrencias de ingredientes, 4.283 cantidades numéricas, 658 sin cantidad reconocida, 105 cualitativas, 1 ambigua. Hay 36 identidades explícitas y 1.044 candidatos únicos entre las 5.011 entradas sin resolver (20,83 %); 3.967 entradas sin resolver ni candidato. Opcionalidad: 4.493 requeridas, 540 opcionales y 14 indeterminadas. Rendimiento declarado 587/590, numérico 492/590; duraciones declaradas 386/590, alguna numérica 284/590; 437/600 declaraciones temporales numéricas. Evidencia: 6 prepared, 373 pending, 211 unknown. Referencias: 2.543 ocurrencias, 2.497 internas resueltas por ruta, 2.100 con ID y 46 externas. No equivale a precisión, exhaustividad ni validación práctica.

Corte #235: 590 recetas, 588 títulos normalizados, 5.047 ocurrencias de ingredientes, 5.046 textuales (2.588 claves), 36 explícitas (20 claves), 1.044 candidatas (61 claves). 590/590 huellas verificadas, reconstrucción idéntica, 81 pruebas, 16/16 casos y tres consultas inválidas rechazadas. Consultas abiertas: ajo 103, salsa de soja en módulo asiático 4, leche de coco explícita 2 y candidata 5, prepared 6. Total numérico único 101/590, no interpretado 94, no declarado 395; rendimiento numérico 492/590. Cero advertencias semánticas y un huérfano documental (contrato del índice, enlazado en este cierre; pendiente nueva comprobación). Referencia: [contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md).

Corte #246: 102 pruebas, 590/590 fuentes verificadas, igualdad de bytes, 68 comparaciones directas de registros, 34 con el experimento compartido, 18 casos fijados y 16 de regresión por corpus. Cero advertencias y cero huérfanos; 927 Markdown. El [job](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44524998284/job/135563094114) corresponde al snapshot sintético 7249024567f5f74d0dd6c6c7d9d78babf62ab67a. La proyección fijada de RET-D01 (c0dd020dea003d8a4f7a0278a43f30d81501a7f0) conserva huella d72cb4cb48f8ab112d3f60003bb8a20acfe295925756e6456b12bf7b2648a89c. El corpus de CI contiene 590 recetas, 5.047 ocurrencias, 36 explícitas y 1.044 candidatas; las 72 adicionales del experimento (71 recetas) no se integraron. Comparaciones de consistencia, no precisión culinaria ni validación exhaustiva del ZIP. Modo terms explícito, no interpreta negaciones, alternativas, equivalencias o disponibilidad. Referencias: [investigación](./EVOLUCION_RECUPERACION_CULINARIA.md) y [alcance](./ALCANCE_RECUPERACION_TEXTUAL.md).

1. Comprobar el uso público de Pantry, Shopping y Planner, y revisar la siguiente capacidad; conservar los experimentos y la [deuda de requisitos](./DEUDA_REQUISITOS_CULINARIOS.md). No promover identidades ni integrar requisitos automáticamente.
2. Preservar separación de coincidencia textual, identidad y candidatos, así como alcance de evidencia culinaria.
3. Revisar los informes y muestras por commit; no convertir cobertura en exactitud.
4. No seleccionar persistencia, API, RAG o agentes ni autorizar una release sin decisión específica.

## 7. Recuperación del estado antes de un nuevo incremento

1. Consultar el `main` remoto y contrastar su commit vigente con `fd3ddc760788dc0a61749c514f964d51a126a527` (**referencia histórica de este corte**, no asumir que continúa siendo HEAD).
2. Revisar si la última PR conocida ([#303](https://github.com/fran-eliot/NovaCoquinaria/pull/303)) ha sido seguida por nuevas PR, la lista de PR abiertas y los resultados de [Knowledge integrity](../../.github/workflows/knowledge-integrity.yml), [Knowledge audit](../../.github/workflows/knowledge-audit.yml) y MkDocs para el commit relevante. Ante una PR abierta o CI fallida, resolver primero ese estado y no generar tandas paralelas sin necesidad.
3. Leer este kit junto con [PROJECT_STATUS](./PROJECT_STATUS.md), [ROADMAP](./ROADMAP.md), [BITACORA](./BITACORA.md), [RELEASES](./RELEASES.md), [CONSOLIDACION_CONOCIMIENTO](./CONSOLIDACION_CONOCIMIENTO.md), [EVOLUCION_DE_RECETAS](./EVOLUCION_DE_RECETAS.md), [RECETAS_COCINADAS](./RECETAS_COCINADAS.md) y los índices del módulo en cuestión.
4. Antes de redactar, revisar el árbol completo de `main` y detectar solapamientos por **nombre, ingrediente, técnica y tradición regional**, no solo por el nombre exacto del archivo. Distinguir las variantes de una misma familia de platos y explicar las diferencias cuando sea pertinente.
5. Comprobar todos los identificadores de receta vigentes. La serie reciente llega a `REC-0591` (Front Matter `REC-591`) en este corte; `REC-0592` es **solo candidato** si continúa libre, y nunca un ID reservado irrevocablemente. Recalcular también recuentos de ficheros antes de reutilizarlos.
6. Completar la comprobación pública de Planner y decidir el siguiente alcance sin deducir faltantes, suficiencia ni preferencias. Incorporar nuevas recetas selectivamente y mantener su estructura y evidencia de elaboración.
7. Cuando se introduzcan antecedentes de recetas que el propietario haya cocinado, preservar su versión principal y su valoración comprobada. No dar por mejor una versión posterior ni trasladar cantidades antiguas a otra sin evidencia.
8. Crear una rama temática desde el `main` actualizado, incorporar fichas e índices coherentes, comprobar enlaces y abrir una PR. Entregar el enlace directo de la PR y revisar el resultado de GitHub Actions. El propietario revisa, fusiona y elimina la rama remota; no hacerlo en su lugar.
9. Reservar las actualizaciones de gestión, continuidad o integridad para PR específicas cuando corresponda, sin completar artificialmente tandas con fichas que no aporten valor.

**Precedencia:** GitHub vigente (`main`, PR y CI) > contenido actual de los documentos > corte histórico del kit > suposiciones. Las cifras de auditoría solo son válidas para el commit y alcance en que se obtuvieron.

## Actualización técnica del 21 de noviembre de 2026 — Planner

Las PR #299–#303 entregaron el alcance, modelo, persistencia local, interfaz semanal e integración del planificador con Explorer y Recipe Assistant. La PR #303 se fusionó en `fd3ddc760788dc0a61749c514f964d51a126a527`. Los tres workflows de PR terminaron en success: Knowledge integrity, Knowledge audit y Culinary Explorer site. El recorrido Chromium del planificador registró `passed: true`, incluidos calendario, operaciones CRUD, copia JSON, importación explícita de recetas, referencias obsoletas bloqueadas y aislamiento de Shopping/Pantry. El resultado es aceptación técnica dirigida, no validación manual del portal público.

**Despliegue observado:** `gh-pages` en `936e5b4f3ae822c5d7bb9d656618ddce4210abf7` indica `Deployed fd3ddc7`; se comprobó la existencia de `culinary-planner.html` en la rama publicada. No hay prueba de uso manual independiente en la URL pública. La última release continúa siendo v1.6.0. No se ha aprobado nueva release, plataforma ni capacidad inteligente.

## 8. Registro del corte y siguiente actualización

| Campo | Valor en el corte de 2026-11-21 |
|---|---|
| Última PR fusionada observada | [#303](https://github.com/fran-eliot/NovaCoquinaria/pull/303) |
| Commit de main | `fd3ddc760788dc0a61749c514f964d51a126a527` |
| Últimos aportes | Culinary Planner 0.1.0 integrado en main, CI superado; gh-pages desplegado desde el merge #303 |
| PR abiertas al realizar la consulta | Ninguna |
| Workflows de PR #303 | Knowledge integrity, Knowledge audit y Culinary Explorer site: success |
| Última release | v1.6.0 (2026-11-19) |
| Próximo identificador | REC-0592, candidato sujeto a verificar |
| Siguiente prioridad | Comprobar recorrido público de Planner y revisar la siguiente decisión estratégica |
| Controles pendientes | Pruebas públicas de consultas y accesibilidad exhaustiva; Contraste individual de los JSON, precisión/exhaustividad de extracción, revisión práctica, duplicidades conceptuales y working tree local |

Este corte debe actualizarse después de merges futuros; no reutilizar el SHA o recuentos como si fueran dinámicos.

---

Este kit permite reanudar el trabajo sin trasladar a NovaCoquinaria decisiones, nomenclaturas o planificación de otros proyectos.
