---
id: DOC-CONTINUIDAD-2026
titulo: Kit de continuidad de NovaCoquinaria
tipo: gestion
version: 1.5.0
estado: estable
ultima_revision: 2026-11-17
---

# Kit de continuidad de NovaCoquinaria

> **Repositorio:** [fran-eliot/NovaCoquinaria](https://github.com/fran-eliot/NovaCoquinaria)  
> **Arquitectura conceptual:** GASTRO — Sistema de Gestión del Conocimiento Culinario (SGCC)  
> **Corte de información:** 17 de noviembre de 2026, después de la fusión de la PR #187.  
> **Naturaleza:** documento de traspaso operativo; no reemplaza la documentación oficial ni el estado vigente de GitHub.

## 1. Identidad y propósito

NovaCoquinaria es un proyecto personal de ingeniería del conocimiento culinario. Su finalidad es capturar, estructurar, relacionar y reutilizar conocimiento de ingredientes, técnicas, bases, patrones, tablas, platos, variantes y recetas. No se limita a un recetario.

**GASTRO** designa la arquitectura conceptual; **NovaCoquinaria**, su aplicación práctica. El principio rector es **«Documentar una vez. Relacionar siempre. Reutilizar continuamente.»**

Referencias: [identidad](../../NovaCoquinaria.md), [visión](../VISION.md), [arquitectura](../architecture/ARQUITECTURA.md), [modelo de conocimiento](../architecture/MODELO_DE_CONOCIMIENTO.md).

## 2. Estado comprobado en este corte

| Elemento | Situación y alcance de la evidencia |
|---|---|
| Rama principal | `main`, consultada en GitHub el 2026-11-17, después del merge de la PR #187 |
| Última versión publicada | [`v1.5.0`](https://github.com/fran-eliot/NovaCoquinaria/releases/tag/v1.5.0), publicada el 2026-08-02; las PR recientes no suponen una nueva release |
| Fase estratégica | Expansión y conexión del conocimiento culinario en Markdown, sin pasar aún a una plataforma software |
| Última PR fusionada | [#187 — Seis especialidades tradicionales españolas (XXIV)](https://github.com/fran-eliot/NovaCoquinaria/pull/187) |
| PRs inmediatamente anteriores | [#186](https://github.com/fran-eliot/NovaCoquinaria/pull/186), [#185](https://github.com/fran-eliot/NovaCoquinaria/pull/185), [#184](https://github.com/fran-eliot/NovaCoquinaria/pull/184), fusionadas |
| Último commit comprobado en `main` | [`e89963c4fb14cff2d92440dec768bdbdbec201c8`](https://github.com/fran-eliot/NovaCoquinaria/commit/e89963c4fb14cff2d92440dec768bdbdbec201c8), merge de #187 |
| PR abiertas | Ninguna en la consulta de este corte |
| Integridad de `main` | Workflow **Knowledge integrity**: **success** para el merge #187 (run 44132642451) |
| Sitio web de documentación | Workflow **Deploy MkDocs site**: **success** para el merge #187 (run 44132642433) |
| Inventario Markdown en `main` | **892** archivos `.md` en el árbol remoto |
| Fichas de recetas | **560** archivos `.md` en los diez módulos de recetas, excluidos README |
| Recetas por módulo | Arroces 39; Pastas 37; Legumbres 61; Verduras 81; Carnes 75; Pescados y Mariscos 64; Cocina Asiática 44; Postres 73; Bebidas 36; Horno 50 |
| Fichas de ingredientes | **125** archivos `.md` en `11_Despensa`, excluidos README y BACKLOG |
| Documentos de técnicas | **52** archivos `.md` en `00_Bases/03_Tecnicas`, excluido README |
| Identificadores | Último identificador de la secuencia reciente: `REC-0561` (representación numérica; `REC-561` en Front Matter). `REC-0562` es candidato sujeto a verificación de unicidad y del árbol actual. No se ha realizado auditoría global de IDs. |
| Working tree local | No comprobado; el estado remoto no demuestra que el repositorio local esté limpio |

Los recuentos son **inventario de rutas en el árbol remoto de `main` al cierre de la PR #187**, no una auditoría semántica ni una prueba culinaria. Los **560 archivos de recetas** no deben interpretarse como 560 elaboraciones realizadas: numerosas fichas siguen marcadas como propuestas pendientes de prueba. Los controles CI acreditan las comprobaciones automáticas que ejecutan, no pruebas prácticas en cocina.

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
- **Resultado comprobado:** #177–#187 fusionadas; integridad y despliegue del merge #187 exitosos. La próxima tanda candidata es XXV, sin comprometer de antemano recetas ni identificadores.
- **Alcance:** las 60 incorporaciones posteriores a #176 siguen siendo propuestas pendientes de prueba doméstica. No se modifica la fase estratégica, la identidad ni la última release del proyecto.

Las PR aportan crecimiento editorial; su fusión y sus validaciones técnicas no prueban que las recetas se hayan cocinado. Los detalles por ficha se consultan en el índice de cada módulo.

La [Bitácora](./BITACORA.md) mantiene los hitos que cambian la identidad o trayectoria del proyecto. No debe convertirse en un registro cotidiano de PRs, commits o correcciones.

## 4. Capacidades y alcance real

**Disponibles o documentadas:** organización por dominios y entidades Markdown con Front Matter, IDs, enlaces, tablas y plantillas; validadores estructurales; Knowledge Graph y herramientas de análisis semántico; MkDocs y documentación de arquitectura, gobernanza y especificaciones.

**En expansión:** el conocimiento culinario reutilizable en `00_Bases`, `01_Arroces`, `02_Pastas`, `03_Legumbres`, `04_Verduras`, `05_Carnes`, `06_Pescados_y_Mariscos`, `07_Cocina_Asiatica`, `08_Postres`, `09_Bebidas`, `10_Horno`, `11_Despensa`, `12_Plantillas` y `98_Tablas`. La expansión reciente ha dado especial profundidad a ingredientes y sus vínculos con recetas y técnicas.

**Futuras o solo especificadas:** backend, API, gestor de despensa, planificación, compra inteligente, Runtime operativo, RAG/GraphRAG y agentes. No confundir una especificación con una función implementada.

**Documentación de gestión desfasada respecto al contenido:** [PROJECT_STATUS](./PROJECT_STATUS.md) sigue revisado a 2026-08-02, y el [BACKLOG de Despensa](../../11_Despensa/BACKLOG.md) contiene casillas históricas sin sincronizar con numerosas fichas existentes. Utilizarlos como contexto, no como inventario actual hasta su revisión. No modificar sus declaraciones históricas mediante una actualización del kit.

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

Los resultados, alcances y limitaciones de las comprobaciones anteriores se registran en [CONSOLIDACION_CONOCIMIENTO](./CONSOLIDACION_CONOCIMIENTO.md).

## 7. Recuperación del estado antes de un nuevo incremento

1. Consultar el `main` remoto y contrastar su commit vigente con `e89963c4fb14cff2d92440dec768bdbdbec201c8` (**referencia histórica de este corte**, no asumir que continúa siendo HEAD).
2. Revisar si la última PR conocida ([#187](https://github.com/fran-eliot/NovaCoquinaria/pull/187)) ha sido seguida por nuevas PR, la lista de PR abiertas y los resultados de [Knowledge integrity](../../.github/workflows/knowledge-integrity.yml) y MkDocs para el commit relevante. Ante una PR abierta o CI fallida, resolver primero ese estado y no generar tandas paralelas sin necesidad.
3. Leer este kit junto con [PROJECT_STATUS](./PROJECT_STATUS.md), [ROADMAP](./ROADMAP.md), [BITACORA](./BITACORA.md), [RELEASES](./RELEASES.md), [CONSOLIDACION_CONOCIMIENTO](./CONSOLIDACION_CONOCIMIENTO.md), [EVOLUCION_DE_RECETAS](./EVOLUCION_DE_RECETAS.md), [RECETAS_COCINADAS](./RECETAS_COCINADAS.md) y los índices del módulo en cuestión.
4. Antes de redactar, revisar el árbol completo de `main` y detectar solapamientos por **nombre, ingrediente, técnica y tradición regional**, no solo por el nombre exacto del archivo. Distinguir las variantes de una misma familia de platos y explicar las diferencias cuando sea pertinente.
5. Comprobar todos los identificadores de receta vigentes. La serie reciente llega a `REC-0561` (Front Matter `REC-561`) en este corte; `REC-0562` es **solo candidato** si continúa libre, y nunca un ID reservado irrevocablemente. Recalcular también recuentos de ficheros antes de reutilizarlos.
6. Priorizar, mientras se mantenga el criterio actual, tandas de hasta seis recetas tradicionales españolas con ingredientes medidos, raciones, tiempos, elaboración numerada, alérgenos, seguridad alimentaria, diagnóstico, conservación y enlaces internos existentes. Las recetas no cocinadas se identifican como propuestas pendientes de prueba.
7. Cuando se introduzcan antecedentes de recetas que el propietario haya cocinado, preservar su versión principal y su valoración comprobada. No dar por mejor una versión posterior ni trasladar cantidades antiguas a otra sin evidencia.
8. Crear una rama temática desde el `main` actualizado, incorporar fichas e índices coherentes, comprobar enlaces y abrir una PR. Entregar el enlace directo de la PR y revisar el resultado de GitHub Actions. El propietario revisa, fusiona y elimina la rama remota; no hacerlo en su lugar.
9. Reservar las actualizaciones de gestión, continuidad o integridad para PR específicas cuando corresponda, sin completar artificialmente tandas con fichas que no aporten valor.

**Precedencia:** GitHub vigente (`main`, PR y CI) > contenido actual de los documentos > corte histórico del kit > suposiciones. Las cifras de auditoría solo son válidas para el commit y alcance en que se obtuvieron.

## 8. Registro del corte y siguiente actualización

| Campo | Valor en el corte de 2026-11-17 |
|---|---|
| Última PR fusionada observada | [#187](https://github.com/fran-eliot/NovaCoquinaria/pull/187) |
| Commit de `main` | `e89963c4fb14cff2d92440dec768bdbdbec201c8` |
| Últimos aportes | Seis fichas `REC-0556`–`REC-0561` (Castilla y León, Cataluña, Andalucía, Madrid y Galicia) |
| PR abiertas al realizar la consulta | Ninguna |
| Workflows del merge #187 | `Knowledge integrity`: **success**; `Deploy MkDocs site`: **success** |
| Última release publicada | `v1.5.0` (2026-08-02) |
| Próximo identificador | `REC-0562`, únicamente como candidato sujeto a verificar unicidad y estado del repositorio |
| Siguiente prioridad | Cocina tradicional española por tandas de hasta seis especialidades nuevas, con variedad regional y sin duplicación; mantener vínculos entre técnica, ingrediente y receta |
| Controles no realizados | Auditoría global de IDs y enlaces, revisión culinaria práctica de las propuestas, comprobación del working tree local |

**Inventario de este corte:** 892 archivos Markdown; 560 fichas de recetas distribuidas en diez módulos; 125 fichas de Despensa (excluidos README/BACKLOG); 52 técnicas (excluido README). Los recuentos son por rutas y no prueban validación culinaria.

Este corte debe actualizarse después de merges futuros; no reutilizar el SHA o los recuentos como si fueran dinámicos.

---

Este kit permite reanudar el trabajo sin trasladar a NovaCoquinaria decisiones, nomenclaturas o planificación de otros proyectos.
