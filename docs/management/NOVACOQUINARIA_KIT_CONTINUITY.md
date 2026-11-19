---
id: DOC-CONTINUIDAD-2026
titulo: Kit de continuidad de NovaCoquinaria
tipo: gestion
version: 1.8.0
estado: estable
ultima_revision: 2026-11-19
---

# Kit de continuidad de NovaCoquinaria

> **Repositorio:** [fran-eliot/NovaCoquinaria](https://github.com/fran-eliot/NovaCoquinaria)  
> **Arquitectura conceptual:** GASTRO — Sistema de Gestión del Conocimiento Culinario (SGCC)  
> **Corte de información:** 19 de noviembre de 2026, después de la fusión de la PR #228.  
> **Naturaleza:** documento de traspaso operativo; no reemplaza la documentación oficial ni el estado vigente de GitHub.

## 1. Identidad y propósito

NovaCoquinaria es un proyecto personal de ingeniería del conocimiento culinario. Su finalidad es capturar, estructurar, relacionar y reutilizar conocimiento de ingredientes, técnicas, bases, patrones, tablas, platos, variantes y recetas. No se limita a un recetario.

**GASTRO** designa la arquitectura conceptual; **NovaCoquinaria**, su aplicación práctica. El principio rector es **«Documentar una vez. Relacionar siempre. Reutilizar continuamente.»**

Referencias: [identidad](../../NovaCoquinaria.md), [visión](../VISION.md), [arquitectura](../architecture/ARQUITECTURA.md), [modelo de conocimiento](../architecture/MODELO_DE_CONOCIMIENTO.md).

## 2. Estado comprobado en este corte

| Elemento | Situación y alcance de la evidencia |
|---|---|
| Rama principal | `main`, consultada el 2026-11-19 después de #228 |
| Última versión publicada | [`v1.5.0`](https://github.com/fran-eliot/NovaCoquinaria/releases/tag/v1.5.0), 2026-08-02; sin nueva release |
| Fase estratégica | Consolidación y explotación; revisión dirigida del extractor completada, indexación pendiente |
| Última PR fusionada | [#228](https://github.com/fran-eliot/NovaCoquinaria/pull/228) |
| Commit comprobado | [`60d4a7a508f19ae382d9b66a355a3ee4e2bc9629`](https://github.com/fran-eliot/NovaCoquinaria/commit/60d4a7a508f19ae382d9b66a355a3ee4e2bc9629) |
| PR abiertas | Ninguna en la consulta del corte |
| Integridad | [Knowledge integrity](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44504038511): success |
| Auditoría | [Knowledge audit](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44504038182): success; 52 pruebas, 0 advertencias semánticas, 0 huérfanos globales |
| Despliegue | [Deploy MkDocs site](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44504038351): success |
| Inventario Markdown | 924 archivos |
| Recetas | 590 rutas y 590 documentos extraídos; Arroces 39; Pastas 37; Legumbres 61; Verduras 86; Carnes 82; Pescados y Mariscos 69; Cocina Asiática 44; Postres 82; Bebidas 36; Horno 54 |
| Despensa y técnicas | 126 fichas de ingrediente y 52 técnicas por ruta, excluidos índices y BACKLOG |
| Identificadores | Última secuencia editorial REC-0591 (Front Matter REC-591); REC-0592 candidato sujeto a verificar |
| Working tree local | No comprobado |

El inventario procede del árbol remoto y la ejecución del corte; no significa que 590 recetas hayan sido cocinadas. Las versiones de herramientas no son releases del proyecto. El contrato de datos está en [CONTRATO_DE_DATOS_DE_RECETAS](../specifications/knowledge/CONTRATO_DE_DATOS_DE_RECETAS.md).

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

Las PR aportan crecimiento editorial; su fusión y sus validaciones técnicas no prueban que las recetas se hayan cocinado. Los detalles por ficha se consultan en el índice de cada módulo.

La [Bitácora](./BITACORA.md) mantiene los hitos que cambian la identidad o trayectoria del proyecto. No debe convertirse en un registro cotidiano de PRs, commits o correcciones.

## 4. Capacidades y alcance real

**Disponibles o documentadas:** contrato de datos 0.1.0, extractor 0.4.6 en etapa recipe_projection_preview, informes reproducibles de cobertura y candidatos de identidad; auditoría automatizada con informes por commit; organización por dominios y entidades Markdown con Front Matter, IDs, enlaces, tablas y plantillas; validadores estructurales; Knowledge Graph y herramientas de análisis semántico; MkDocs y documentación de arquitectura, gobernanza y especificaciones.

**En consolidación e incorporación selectiva:** el conocimiento culinario reutilizable en `00_Bases`, `01_Arroces`, `02_Pastas`, `03_Legumbres`, `04_Verduras`, `05_Carnes`, `06_Pescados_y_Mariscos`, `07_Cocina_Asiatica`, `08_Postres`, `09_Bebidas`, `10_Horno`, `11_Despensa`, `12_Plantillas` y `98_Tablas`. La expansión reciente ha dado especial profundidad a ingredientes y sus vínculos con recetas y técnicas.

**Futuras o solo especificadas:** índice reconstruible de recetas y motor de consultas (siguiente etapa), backend, API, gestor de despensa, planificación, compra inteligente, Runtime operativo, RAG/GraphRAG y agentes. No confundir una especificación con una función implementada.

**Documentación de gestión desfasada respecto al contenido:** [PROJECT_STATUS](./PROJECT_STATUS.md) se actualizó en #195, antes de la primera línea base observada; el [BACKLOG de Despensa](../../11_Despensa/BACKLOG.md) contiene casillas históricas sin sincronizar con numerosas fichas existentes. Utilizarlos como contexto, no como inventario actual hasta su revisión. No modificar sus declaraciones históricas mediante una actualización del kit.

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

### Línea base vigente de extracción y prioridades

Corte #228: 590/590 recetas con ingredientes y pasos reconocidos; 5.047 ocurrencias de ingredientes, 4.283 cantidades numéricas, 658 sin cantidad reconocida, 105 cualitativas, 1 ambigua. Hay 36 identidades explícitas y 1.044 candidatos únicos entre las 5.011 entradas sin resolver (20,83 %); 3.967 entradas sin resolver ni candidato. Opcionalidad: 4.493 requeridas, 540 opcionales y 14 indeterminadas. Rendimiento declarado 587/590, numérico 492/590; duraciones declaradas 386/590, alguna numérica 284/590; 437/600 declaraciones temporales numéricas. Evidencia: 6 prepared, 373 pending, 211 unknown. Referencias: 2.543 ocurrencias, 2.497 internas resueltas por ruta, 2.100 con ID y 46 externas. No equivale a precisión, exhaustividad ni validación práctica.

1. Definir alcance y contrato del índice derivado de recetas: identidad exacta, metadatos, módulos físicos, ingredientes textuales, identidad explícita y candidatos separados, procedencia y evidencia.
2. Construir un índice reconstruible y determinista sobre la proyección de un commit, con comprobaciones de consistencia y pruebas; Markdown continúa siendo fuente canónica.
3. Evaluar consultas reproducibles por ID, ingredientes y metadatos. Distinguir tiempos totales declarados de fases, no inferir duración completa, y conservar incertidumbre.
4. Registrar limitaciones y contrastar muestras. La revisión EXT-01–EXT-05 fue dirigida; no se exige cobertura artificial del 100 %. No se selecciona persistencia, API, RAG o agentes ni se autoriza una release.

## 7. Recuperación del estado antes de un nuevo incremento

1. Consultar el `main` remoto y contrastar su commit vigente con `60d4a7a508f19ae382d9b66a355a3ee4e2bc9629` (**referencia histórica de este corte**, no asumir que continúa siendo HEAD).
2. Revisar si la última PR conocida ([#228](https://github.com/fran-eliot/NovaCoquinaria/pull/228)) ha sido seguida por nuevas PR, la lista de PR abiertas y los resultados de [Knowledge integrity](../../.github/workflows/knowledge-integrity.yml), [Knowledge audit](../../.github/workflows/knowledge-audit.yml) y MkDocs para el commit relevante. Ante una PR abierta o CI fallida, resolver primero ese estado y no generar tandas paralelas sin necesidad.
3. Leer este kit junto con [PROJECT_STATUS](./PROJECT_STATUS.md), [ROADMAP](./ROADMAP.md), [BITACORA](./BITACORA.md), [RELEASES](./RELEASES.md), [CONSOLIDACION_CONOCIMIENTO](./CONSOLIDACION_CONOCIMIENTO.md), [EVOLUCION_DE_RECETAS](./EVOLUCION_DE_RECETAS.md), [RECETAS_COCINADAS](./RECETAS_COCINADAS.md) y los índices del módulo en cuestión.
4. Antes de redactar, revisar el árbol completo de `main` y detectar solapamientos por **nombre, ingrediente, técnica y tradición regional**, no solo por el nombre exacto del archivo. Distinguir las variantes de una misma familia de platos y explicar las diferencias cuando sea pertinente.
5. Comprobar todos los identificadores de receta vigentes. La serie reciente llega a `REC-0591` (Front Matter `REC-591`) en este corte; `REC-0592` es **solo candidato** si continúa libre, y nunca un ID reservado irrevocablemente. Recalcular también recuentos de ficheros antes de reutilizarlos.
6. Priorizar el índice reconstruible y las consultas según el contrato de datos y CONSOLIDACION_CONOCIMIENTO; ROADMAP y PROJECT_STATUS conservan un corte anterior. Incorporar nuevas recetas selectivamente y mantener su estructura y evidencia de elaboración.
7. Cuando se introduzcan antecedentes de recetas que el propietario haya cocinado, preservar su versión principal y su valoración comprobada. No dar por mejor una versión posterior ni trasladar cantidades antiguas a otra sin evidencia.
8. Crear una rama temática desde el `main` actualizado, incorporar fichas e índices coherentes, comprobar enlaces y abrir una PR. Entregar el enlace directo de la PR y revisar el resultado de GitHub Actions. El propietario revisa, fusiona y elimina la rama remota; no hacerlo en su lugar.
9. Reservar las actualizaciones de gestión, continuidad o integridad para PR específicas cuando corresponda, sin completar artificialmente tandas con fichas que no aporten valor.

**Precedencia:** GitHub vigente (`main`, PR y CI) > contenido actual de los documentos > corte histórico del kit > suposiciones. Las cifras de auditoría solo son válidas para el commit y alcance en que se obtuvieron.

## 8. Registro del corte y siguiente actualización

| Campo | Valor en el corte de 2026-11-19 |
|---|---|
| Última PR fusionada observada | [#228](https://github.com/fran-eliot/NovaCoquinaria/pull/228) |
| Commit de main | `60d4a7a508f19ae382d9b66a355a3ee4e2bc9629` |
| Últimos aportes | Contrato, extracción 0.4.6, cobertura y revisión dirigida EXT-01–EXT-05 |
| PR abiertas al realizar la consulta | Ninguna |
| Workflows del merge #228 | Knowledge integrity, Knowledge audit y Deploy MkDocs site: success |
| Última release | v1.5.0 (2026-08-02) |
| Próximo identificador | REC-0592, candidato sujeto a verificar |
| Siguiente prioridad | Contrato y prototipo de índice derivado; consultas reproducibles |
| Controles pendientes | Contraste individual de los JSON, precisión/exhaustividad de extracción, revisión práctica, duplicidades conceptuales y working tree local |

Este corte debe actualizarse después de merges futuros; no reutilizar el SHA o recuentos como si fueran dinámicos.

---

Este kit permite reanudar el trabajo sin trasladar a NovaCoquinaria decisiones, nomenclaturas o planificación de otros proyectos.
