---
id: DOC-CONTINUIDAD-2026
titulo: Kit de continuidad de NovaCoquinaria
tipo: gestion
version: 1.3.0
estado: estable
ultima_revision: 2026-11-15
---

# Kit de continuidad de NovaCoquinaria

> **Repositorio:** [fran-eliot/NovaCoquinaria](https://github.com/fran-eliot/NovaCoquinaria)  
> **Arquitectura conceptual:** GASTRO — Sistema de Gestión del Conocimiento Culinario (SGCC)  
> **Corte de información:** 15 de noviembre de 2026, después de la fusión de la PR #158.  
> **Naturaleza:** documento de traspaso operativo; no reemplaza la documentación oficial ni el estado vigente de GitHub.

## 1. Identidad y propósito

NovaCoquinaria es un proyecto personal de ingeniería del conocimiento culinario. Su finalidad es capturar, estructurar, relacionar y reutilizar conocimiento de ingredientes, técnicas, bases, patrones, tablas, platos, variantes y recetas. No se limita a un recetario.

**GASTRO** designa la arquitectura conceptual; **NovaCoquinaria**, su aplicación práctica. El principio rector es **«Documentar una vez. Relacionar siempre. Reutilizar continuamente.»**

Referencias: [identidad](../../NovaCoquinaria.md), [visión](../VISION.md), [arquitectura](../architecture/ARQUITECTURA.md), [modelo de conocimiento](../architecture/MODELO_DE_CONOCIMIENTO.md).

## 2. Estado comprobado en este corte

| Elemento | Situación y alcance de la evidencia |
|---|---|
| Rama principal | `main`, consultada en GitHub el 2026-11-15 (commit de merge #158) |
| Última versión publicada | [`v1.5.0`](https://github.com/fran-eliot/NovaCoquinaria/releases/tag/v1.5.0), publicada el 2026-08-02 |
| Fase estratégica | Expansión del conocimiento culinario, sin pasar aún a una plataforma software |
| Última PR fusionada | [#158 — Seis guisos, ensaladas y untables de legumbres](https://github.com/fran-eliot/NovaCoquinaria/pull/158) |
| PRs inmediatamente anteriores | [#157](https://github.com/fran-eliot/NovaCoquinaria/pull/157), [#156](https://github.com/fran-eliot/NovaCoquinaria/pull/156), [#155](https://github.com/fran-eliot/NovaCoquinaria/pull/155), fusionadas |
| Último commit comprobado en `main` | [`5943448ebd8d34f3659af2d7b9299cdd44c39469`](https://github.com/fran-eliot/NovaCoquinaria/commit/5943448ebd8d34f3659af2d7b9299cdd44c39469), merge de #158 |
| PR abiertas | Ninguna en la consulta de este corte |
| Integridad de `main` | Workflow **Knowledge integrity**: **in_progress** para el merge #158 al realizar la consulta; el workflow de la cabeza de PR #158 (`061bbf356e9ea0641d0b682b4e42393a883d15f8`) terminó en **success** |
| Sitio web de documentación | Workflow **Deploy MkDocs site**: **in_progress** para el merge #158 en la última consulta; no atribuirle éxito sin verificar resultado posterior |
| Inventario Markdown en `main` | 730 archivos `.md` en el árbol remoto |
| Fichas de ingredientes | 125 archivos `.md` en `11_Despensa`, excluidos README y BACKLOG |
| Documentos de recetas | 398 archivos `.md` en los diez módulos de recetas, excluidos README |
| Documentos de técnicas | 52 archivos `.md` en `00_Bases/03_Tecnicas`, excluido README |
| Identificadores | Último identificador de receta incorporado en la serie reciente: `REC-0399`; `REC-0400` es solo un candidato para la siguiente receta, sujeto a verificar unicidad. No se ha efectuado auditoría global de IDs. |
| Working tree local | No comprobado: el estado remoto no acredita que el árbol de trabajo local esté limpio |

Los recuentos son un **inventario por rutas del árbol de `main` en este corte**, no una auditoría semántica ni prueba de que cada receta se haya elaborado y validado en cocina. La release más reciente se contrastó con el registro de GitHub (v1.5.0, 2026-08-02). Las funciones software especificadas no se consideran implementadas; la CI de `main` aún estaba ejecutándose para el merge #158 al cerrar este corte.

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

1. Consultar el `main` remoto: comparar su commit vigente con `5943448ebd8d34f3659af2d7b9299cdd44c39469` (**referencia de este corte**, no asumir que sigue siendo HEAD).
2. Comprobar la PR más reciente, las PR abiertas y las ejecuciones del workflow [Knowledge integrity](../../.github/workflows/knowledge-integrity.yml). Si el kit se ha actualizado mediante una PR posterior, tomar también su merge como nuevo punto de partida.
3. Leer este kit junto con [PROJECT_STATUS](./PROJECT_STATUS.md), [ROADMAP](./ROADMAP.md), [BITACORA](./BITACORA.md), [RELEASES](./RELEASES.md), [CONSOLIDACION_CONOCIMIENTO](./CONSOLIDACION_CONOCIMIENTO.md), [EVOLUCION_DE_RECETAS](./EVOLUCION_DE_RECETAS.md), [RECETAS_COCINADAS](./RECETAS_COCINADAS.md) y el índice del módulo que se vaya a ampliar.
4. Distinguir contenido ya publicado, fichas en borrador, decisiones acordadas, objetivos estratégicos y capacidades aún no implementadas; no convertir propuestas en experiencias confirmadas.
5. Comprobar los identificadores existentes **en el árbol vigente**. La serie reciente de recetas llega a `REC-0399`; `REC-0400` solo es candidato si sigue libre en el momento de crear la ficha. Para ingredientes y otras entidades, comprobar la numeración real sin arrastrar reservas históricas.
6. Alternar la expansión de Despensa con revisión de cobertura, calidad culinaria y conexión efectiva entre recetas, técnicas, patrones y tablas; evitar fichas nuevas por mera acumulación.
7. Preparar un incremento de alcance delimitado, actualizar índices y comprobar enlaces. Crear PR para revisión, sin fusionarla ni borrar su rama.

**Precedencia:** GitHub vigente (`main`, PR y CI) > contenido actual de la documentación > corte histórico del kit > supuestos. Las cifras de auditoría solo son válidas para el commit y alcance en que se obtuvieron.

## 8. Registro del corte y siguiente actualización

| Campo | Valor en el corte de 2026-11-15 |
|---|---|
| Última PR fusionada observada | [#158](https://github.com/fran-eliot/NovaCoquinaria/pull/158) |
| Commit de `main` | `5943448ebd8d34f3659af2d7b9299cdd44c39469` |
| Últimos aportes | Seis recetas de legumbres `REC-0394`–`REC-0399`; última tanda [PR #158](https://github.com/fran-eliot/NovaCoquinaria/pull/158) |
| PR abiertas al realizar la consulta | Ninguna |
| Workflow para el merge #158 | `Knowledge integrity`: **in_progress**; `Deploy MkDocs site`: **in_progress** en la consulta. Integridad de la cabeza de la PR #158: **success** |
| Última release publicada | `v1.5.0` (2026-08-02) |
| Próximo identificador | `REC-0400` es candidato, sujeto a confirmar unicidad y ausencia de nuevas PR o commits antes de usarlo |
| Siguiente prioridad | Incorporar nuevas recetas y técnicas sin duplicación; reforzar relaciones, seguridad y trazabilidad de recetas domésticas; verificar enlaces reales antes de crear nuevas fichas |
| Controles no realizados | Auditoría global de IDs/relaciones, comprobación manual completa de todos los enlaces, revisión culinaria práctica de las fichas, estado del árbol local |

**Inventario de este corte:** 730 archivos Markdown, 398 fichas de recetas en diez módulos, 125 fichas de Despensa (sin README/BACKLOG) y 52 técnicas (sin README). Son recuentos de rutas, no validación semántica ni ensayo culinario.

Este registro se actualizará con el **estado comprobado** después de nuevos merges relevantes. No reutilizar el SHA o los recuentos de este corte como si fueran datos dinámicos.

---

Este kit permite reanudar el trabajo sin trasladar a NovaCoquinaria decisiones, nomenclaturas o planificación de otros proyectos.
