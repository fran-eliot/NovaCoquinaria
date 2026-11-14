---
id: DOC-CONTINUIDAD-2026
titulo: Kit de continuidad de NovaCoquinaria
tipo: gestion
version: 1.0.0
estado: estable
ultima_revision: 2026-11-14
---

# Kit de continuidad de NovaCoquinaria

> **Repositorio:** [fran-eliot/NovaCoquinaria](https://github.com/fran-eliot/NovaCoquinaria)  
> **Arquitectura conceptual:** GASTRO — Sistema de Gestión del Conocimiento Culinario (SGCC)  
> **Corte de información:** 14 de noviembre de 2026, después de la PR #67.  
> **Naturaleza:** documento de traspaso operativo; no reemplaza la documentación oficial ni el estado vigente de GitHub.

## 1. Identidad y propósito

NovaCoquinaria es un proyecto personal de ingeniería del conocimiento culinario. Su finalidad es capturar, estructurar, relacionar y reutilizar conocimiento de ingredientes, técnicas, bases, patrones, tablas, platos, variantes y recetas. No se limita a un recetario.

**GASTRO** designa la arquitectura conceptual; **NovaCoquinaria**, su aplicación práctica. El principio rector es **«Documentar una vez. Relacionar siempre. Reutilizar continuamente.»**

Referencias: [identidad](../../NovaCoquinaria.md), [visión](../VISION.md), [arquitectura](../architecture/ARQUITECTURA.md), [modelo de conocimiento](../architecture/MODELO_DE_CONOCIMIENTO.md).

## 2. Estado documentado en este corte

| Elemento | Situación y alcance de la evidencia |
|---|---|
| Rama principal | `main`, confirmada en GitHub |
| Última versión recogida en la documentación de gestión | `v1.5.0` — Marco de especificaciones del SGCC |
| Fase descrita en PROJECT_STATUS | Expansión del conocimiento culinario |
| Última PR consultada | [#67 — Cocción y conservación de postres con huevo y lácteos](https://github.com/fran-eliot/NovaCoquinaria/pull/67), fusionada el 2026-11-14 |
| PR anterior | [#66 — Seguridad y coherencia culinaria del arroz frito](https://github.com/fran-eliot/NovaCoquinaria/pull/66), fusionada el 2026-11-14 |
| PR precedente | [#65 — Navegación transversal del modelo de gobernanza](https://github.com/fran-eliot/NovaCoquinaria/pull/65), fusionada el 2026-11-14 |
| Commit de referencia tras #67 | [`3d3f9cb`](https://github.com/fran-eliot/NovaCoquinaria/commit/3d3f9cb01b82f80e90e3a0b8cb3abfa135307bc3) |
| Issues abiertas | Ninguna encontrada en la consulta efectuada para este corte |
| Ramas observadas | `main` y `gh-pages` |
| Releases/tags y milestones en GitHub | No contrastados directamente en este corte; consultar antes de afirmar su estado |
| Working tree local | No comprobado; no inferir limpieza a partir del repositorio remoto |

La versión `v1.5.0` está registrada en [PROJECT_STATUS](./PROJECT_STATUS.md) y [RELEASES](./RELEASES.md). No debe confundirse «última versión documentada» con «última release verificada en GitHub».

## 3. Decisiones y evolución relevantes

- **2026-06-29:** nacimiento del proyecto como colección estructurada de conocimiento culinario.
- **2026-07-01:** evolución conceptual desde recetario hacia SGCC.
- **2026-07-05:** primera versión estable `v1.0.0`.
- **2026-07-06:** incorporación de MkDocs; Markdown permanece como fuente de verdad.
- **2026-07-09:** incorporación del Knowledge Graph.
- **2026-08-02:** consolidación del marco de especificaciones `v1.5.0`.
- **2026-08-02:** decisión estratégica de **priorizar la expansión sistemática del conocimiento culinario** antes de desarrollar la plataforma software.
- **2026-08-03:** consolidación del dominio Currys como referencia estructural.
- **2026-11-14:** mejoras incrementales de integridad, relaciones, navegación y seguridad/coherencia de preparaciones culinarias, culminando en la PR #67 para el presente corte.

Las fechas y su interpretación histórica se desarrollan en la [Bitácora](./BITACORA.md). No convertir cada PR de mantenimiento en un nuevo hito de la Bitácora.

## 4. Capacidades consolidadas, en expansión y previstas

**Existentes/documentadas:** organización del conocimiento mediante Markdown y Front Matter, identificadores y referencias cruzadas; validadores estructurales; Knowledge Graph y análisis semántico; MkDocs; modelo de gobernanza y especificaciones del SGCC.

**En expansión:** contenido culinario y consolidación de dominios; revisión de enlaces, navegación, relaciones y calidad de fichas. El [PROJECT_STATUS](./PROJECT_STATUS.md) sitúa Currys como dominio consolidado y recomienda extender el patrón a Pastas o Legumbres; esa clasificación es un estado documental de su fecha de revisión, no una auditoría actualizada a noviembre.

**Futuras / no dar por implementadas:** backend, API, gestor de despensa, planificación, compra inteligente, plataforma web, Runtime operativo, RAG/GraphRAG y agentes. Son capacidades previstas en el [Roadmap](./ROADMAP.md) y las [Releases](./RELEASES.md); su presencia en especificaciones no equivale a una implementación funcional.

## 5. Forma de trabajo acordada

- Conversación y coordinación del proyecto en español.
- Cambios delimitados en una rama temática creada desde la versión vigente de `main`, con PR dirigida a `main`.
- La revisión, la fusión de PR y la eliminación de la rama remota corresponden al propietario del proyecto; no ejecutar esas acciones sin autorización expresa.
- Para nuevas incorporaciones culinarias, se pueden agrupar **hasta seis fichas relacionadas** (recetas, técnicas, ingredientes, tablas u otras) por incremento si mantienen coherencia temática y un diff revisable.
- Conservar Front Matter, IDs, referencias internas, estructura y principios de reutilización. Comprobar antes de crear una ficha que no exista ya una autoridad reutilizable.
- Priorizar exactitud de ingredientes y cantidades, procedimiento reproducible, seguridad alimentaria, conservación y relaciones semánticas pertinentes.
- Ejecutar las comprobaciones disponibles cuando proceda y distinguir entre *validación realizada*, *diagnóstico informativo* y *validación pendiente*. No afirmar CI satisfactorio sin consultar la ejecución correspondiente.
- Redactar documentación del proyecto, commits y PR de forma natural y profesional; reservar comprobaciones y notas de coordinación para el ámbito operativo, sin incorporarlas a fichas culinarias.

## 6. Integridad y calidad del conocimiento

El procedimiento vigente de [consolidación del conocimiento](./CONSOLIDACION_CONOCIMIENTO.md) distingue controles estructurales bloqueantes de diagnósticos semánticos informativos:

- `python tools/validate_all.py`: Front Matter, IDs y enlaces internos.
- `tools/validate_semantics.py` y `tools/find_orphans.py`: diagnósticos de relaciones y documentos huérfanos; no son por sí solos controles bloqueantes.
- Los recuentos de advertencias y huérfanos dependen de la ejecución y del commit; no reutilizar cifras históricas como resultados actuales.
- La revisión documental de una receta no acredita por sí sola su ensayo práctico en cocina.

Los resultados, alcances y limitaciones de las comprobaciones anteriores se registran en [CONSOLIDACION_CONOCIMIENTO](./CONSOLIDACION_CONOCIMIENTO.md).

## 7. Recuperación del estado antes de un nuevo incremento

1. Consultar `main` y contrastar el último commit con el indicado en este documento.
2. Revisar PR abiertas y recientes, issues, milestones, tags/releases y trabajos en curso; marcar como no verificado lo que no se pueda consultar.
3. Leer [PROJECT_STATUS](./PROJECT_STATUS.md), [ROADMAP](./ROADMAP.md), [BITACORA](./BITACORA.md), [RELEASES](./RELEASES.md) y los documentos específicos del área afectada.
4. Distinguir hechos publicados, propuestas, decisiones aprobadas y trabajo pendiente.
5. Seleccionar **un incremento de valor culinario** alineado con la prioridad de expansión y consolidación, evitando tareas documentales redundantes.
6. No modificar el repositorio sin alcance de ejecución autorizado.

**Precedencia:** estado vivo comprobado de GitHub y contenido vigente de `main` > documentación histórica del repositorio > este corte de continuidad > hipótesis. Ante discrepancias, documentarlas antes de reconciliar.

## 8. Registro para el siguiente corte

Al actualizar este kit, conservar la historia estable y anotar solo el nuevo contexto necesario:

| Campo | Último valor o criterio |
|---|---|
| Fecha del nuevo corte | Pendiente |
| Última versión publicada y verificada | Pendiente de contraste |
| Última PR fusionada | #67 en el corte inicial |
| Último commit en `main` | `3d3f9cb` en el corte inicial |
| Issues y milestones activos | Volver a consultar |
| Lote culinario finalizado | Pendiente de registrar |
| Nuevas decisiones relevantes | Registrar solo decisiones efectivas |
| Bloqueos y validaciones pendientes | Registrar con evidencia |
| Siguiente incremento acordado | Definir tras revisar el estado vigente |

---

Este kit permite reanudar el trabajo sin trasladar a NovaCoquinaria decisiones, nomenclaturas o planificación de otros proyectos.
