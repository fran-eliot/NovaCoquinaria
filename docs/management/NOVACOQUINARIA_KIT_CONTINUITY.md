---
id: DOC-CONTINUIDAD-2026
titulo: Kit de continuidad de NovaCoquinaria
tipo: gestion
version: 1.2.0
estado: estable
ultima_revision: 2026-11-15
---

# Kit de continuidad de NovaCoquinaria

> **Repositorio:** [fran-eliot/NovaCoquinaria](https://github.com/fran-eliot/NovaCoquinaria)  
> **Arquitectura conceptual:** GASTRO — Sistema de Gestión del Conocimiento Culinario (SGCC)  
> **Corte de información:** 15 de noviembre de 2026, después de la fusión de la PR #116.  
> **Naturaleza:** documento de traspaso operativo; no reemplaza la documentación oficial ni el estado vigente de GitHub.

## 1. Identidad y propósito

NovaCoquinaria es un proyecto personal de ingeniería del conocimiento culinario. Su finalidad es capturar, estructurar, relacionar y reutilizar conocimiento de ingredientes, técnicas, bases, patrones, tablas, platos, variantes y recetas. No se limita a un recetario.

**GASTRO** designa la arquitectura conceptual; **NovaCoquinaria**, su aplicación práctica. El principio rector es **«Documentar una vez. Relacionar siempre. Reutilizar continuamente.»**

Referencias: [identidad](../../NovaCoquinaria.md), [visión](../VISION.md), [arquitectura](../architecture/ARQUITECTURA.md), [modelo de conocimiento](../architecture/MODELO_DE_CONOCIMIENTO.md).

## 2. Estado comprobado en este corte

| Elemento | Situación y alcance de la evidencia |
|---|---|
| Rama principal | `main`, consultada en GitHub el 2026-11-15 |
| Última versión publicada | [`v1.5.0`](https://github.com/fran-eliot/NovaCoquinaria/releases/tag/v1.5.0), publicada el 2026-08-02 |
| Fase estratégica | Expansión del conocimiento culinario, sin pasar aún a una plataforma software |
| Última PR fusionada | [#116 — Cangrejo al ajillo y experiencias de cocina](https://github.com/fran-eliot/NovaCoquinaria/pull/116) |
| PRs inmediatamente anteriores | [#115](https://github.com/fran-eliot/NovaCoquinaria/pull/115), [#114](https://github.com/fran-eliot/NovaCoquinaria/pull/114), [#113](https://github.com/fran-eliot/NovaCoquinaria/pull/113), fusionadas |
| Último commit comprobado en `main` | [`d745ff105932f482ba7988a6794afbf4145d9937`](https://github.com/fran-eliot/NovaCoquinaria/commit/d745ff105932f482ba7988a6794afbf4145d9937), merge de #116 |
| PR abiertas | Ninguna en la consulta de este corte |
| Integridad de `main` | Workflow **Knowledge integrity**: **success** para el commit de merge #116 |
| Sitio web de documentación | Workflow **Deploy MkDocs site**: **success** para el mismo commit |
| Inventario Markdown en `main` | 509 archivos `.md` en el árbol remoto |
| Fichas de ingredientes | 125 archivos `.md` en `11_Despensa`, excluidos README y BACKLOG |
| Documentos de recetas | 197 archivos `.md` en los diez módulos de recetas, excluidos README |
| Documentos de técnicas | 52 archivos `.md` en `00_Bases/03_Tecnicas`, excluido README |
| Identificadores | No se ha efectuado en este corte una auditoría global de IDs; verificar antes de crear fichas |
| Working tree local | No comprobado: el estado remoto no acredita que el árbol de trabajo local esté limpio |

Los recuentos son un **inventario por rutas del árbol de `main` en este corte**, no una auditoría semántica ni prueba de que cada receta se haya elaborado y validado en cocina. El último release publicado se ha contrastado mediante el registro de GitHub; las funciones software especificadas no se consideran implementadas.

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

1. Consultar el `main` remoto: comparar su commit vigente con `d745ff1059` (**referencia de este corte**, no asumir que sigue siendo HEAD).
2. Comprobar la PR más reciente, las PR abiertas y las ejecuciones del workflow [Knowledge integrity](../../.github/workflows/knowledge-integrity.yml). Si el kit se ha actualizado mediante una PR posterior, tomar también su merge como nuevo punto de partida.
3. Leer este kit junto con [PROJECT_STATUS](./PROJECT_STATUS.md), [ROADMAP](./ROADMAP.md), [BITACORA](./BITACORA.md), [RELEASES](./RELEASES.md), [CONSOLIDACION_CONOCIMIENTO](./CONSOLIDACION_CONOCIMIENTO.md), [EVOLUCION_DE_RECETAS](./EVOLUCION_DE_RECETAS.md), [RECETAS_COCINADAS](./RECETAS_COCINADAS.md) y el índice del módulo que se vaya a ampliar.
4. Distinguir contenido ya publicado, fichas en borrador, decisiones acordadas, objetivos estratégicos y capacidades aún no implementadas; no convertir propuestas en experiencias confirmadas.
5. Comprobar los identificadores existentes **en el árbol vigente**, sin reutilizar el candidato `ING-0126` del corte anterior como si continuase reservado.
6. Alternar la expansión de Despensa con revisión de cobertura, calidad culinaria y conexión efectiva entre recetas, técnicas, patrones y tablas; evitar fichas nuevas por mera acumulación.
7. Preparar un incremento de alcance delimitado, actualizar índices y comprobar enlaces. Crear PR para revisión, sin fusionarla ni borrar su rama.

**Precedencia:** GitHub vigente (`main`, PR y CI) > contenido actual de la documentación > corte histórico del kit > supuestos. Las cifras de auditoría solo son válidas para el commit y alcance en que se obtuvieron.

## 8. Registro del corte y siguiente actualización

| Campo | Valor en el corte de 2026-11-15 |
|---|---|
| Última PR fusionada observada | [#116](https://github.com/fran-eliot/NovaCoquinaria/pull/116) |
| Commit de `main` | `d745ff105932f482ba7988a6794afbf4145d9937` |
| Últimos aportes | Propuesta de cangrejo rojo cocido al ajillo y antecedentes de ternera con bambú y tarta de natillas |
| PR abiertas al realizar la consulta | Ninguna |
| Workflow para el merge #116 | `Knowledge integrity`: **success**; `Deploy MkDocs site`: **success** |
| Última release publicada | `v1.5.0` (2026-08-02) |
| Próximo identificador | Pendiente de comprobar unicidad y secuencia antes de asignarlo |
| Siguiente prioridad | Incorporar conocimiento culinario nuevo y preservar la trazabilidad de las experiencias sin degradar recetas preferidas |
| Controles no realizados | Auditoría global de IDs/relaciones, revisión culinaria práctica de todas las fichas, estado del árbol local |

Este registro se actualizará con el **estado comprobado** después de nuevos merges relevantes. No reutilizar el SHA o los recuentos de este corte como si fueran datos dinámicos.

---

Este kit permite reanudar el trabajo sin trasladar a NovaCoquinaria decisiones, nomenclaturas o planificación de otros proyectos.
