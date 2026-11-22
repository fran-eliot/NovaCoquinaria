---
id: DOC-0011
titulo: Estado del Proyecto
tipo: gestion
version: 3.6
estado: estable
ultima_revision: 2026-11-21
---

# Estado del Proyecto

> **Proyecto:** NovaCoquinaria  
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento proporciona una **visión ejecutiva del estado actual del proyecto**.

Su finalidad es ofrecer una fotografía precisa del SGCC en un momento determinado, facilitando la comprensión de su nivel de madurez, prioridades y situación operativa.

No documenta la evolución histórica del proyecto ni planifica su futuro.

---

# Resumen ejecutivo

| Campo | Valor |
|---------|-------|
| Proyecto | NovaCoquinaria |
| Sistema | GASTRO (SGCC) |
| Versión publicada | **v1.6.0 — Culinary Knowledge & Retrieval** |
| Estado | 🟢 Desarrollo activo |
| Fase | Consolidación y explotación del conocimiento |
| Madurez global | Pendiente de reevaluación con auditoría actualizada |
| Próximo objetivo | Evaluar una línea base actualizada de calidad y utilidad del conocimiento culinario, tras la aceptación funcional pública acotada |

---

# Estado general

## Situación actual

NovaCoquinaria dispone actualmente de una arquitectura documental consolidada, un modelo formal de conocimiento, un marco completo de gobernanza y un conjunto integral de especificaciones que describen la organización, los motores de ejecución, las interfaces y la evolución del SGCC.

Tras completar este marco de especificaciones (v1.5.0), el proyecto ha iniciado una nueva fase centrada en la expansión sistemática del conocimiento culinario. Durante esta etapa se ha consolidado el dominio **Currys** como primer dominio culinario completo del repositorio, validando el modelo mediante ingredientes, técnicas, plantillas, tablas comparativas y recetas reutilizables.

El sistema de auditoría del conocimiento permite medir automáticamente la cobertura estructural, la madurez y la reutilización del conocimiento por dominios culinarios, facilitando la planificación de futuras ampliaciones.

---

## Corte de transición — 2026-11-18

El inventario comprobado tras la PR #193 contiene 922 archivos Markdown, 590 fichas de recetas, 125 fichas de ingredientes y 52 técnicas. La serie española comprende 174 propuestas en 29 tandas. La PR #194 incorpora la propuesta de transición. Los recuentos son de rutas, no acreditan unicidad semántica ni pruebas culinarias. El informe de auditoría publicado sigue fechado el 2026-08-03; se requiere una nueva línea base antes de actualizar la madurez de los dominios.

## Corte de explotación — 2026-11-19

Tras #235, el primer ciclo de extracción, indexación y consultas está implementado y contrastado de forma dirigida. El [informe de CI](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44512835060/job/135521171559) registra 590 recetas y huellas verificadas, 81 pruebas, 16 casos de consulta superados, tres entradas inválidas rechazadas y reconstrucción idéntica. El snapshot auditado es distinto del merge en main. Cero advertencias semánticas y un huérfano documental cuya resolución se propone en este cierre. Véanse [consolidación](./CONSOLIDACION_CONOCIMIENTO.md) y [contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md).

## Corte de recuperación textual — 2026-11-19

Tras #246 (merge `d1aca80a3ff4e39fa1868d36137c22d491d6c893`), las cuatro unidades de recuperación por términos están integradas. El [job de #246](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44524998284/job/135563094114) confirma 927 Markdown, 590 recetas, 102 pruebas, 68 comparaciones directas de registros, 34 con experimento, 18 casos fijados y 16 de regresión por corpus, cero advertencias y huérfanos. Snapshot de CI distinto del merge. Véase [alcance y evidencia](./ALCANCE_RECUPERACION_TEXTUAL.md). Las 72 propuestas adicionales de identidad no se integraron. En aquel corte no se había publicado nueva release; no se acredita precisión culinaria exhaustiva.

## Corte de publicación — 2026-11-19

[v1.6.0](https://github.com/fran-eliot/NovaCoquinaria/releases/tag/v1.6.0) publicada sobre `836f02e848299c0a7a7897b22bb83cd13e0c373a` (merge #249). Los tres workflows de main finalizaron correctamente. La compatibilidad culinaria permanece en investigación; no forma parte de la entrega publicada.

## Corte de investigación de compatibilidad — 2026-11-19

#256 integrada. La [investigación CCE](./INVESTIGACION_COMPATIBILIDAD_CULINARIA.md) acredita 110 pruebas y cinco escenarios dirigidos; las 590 recetas resultaron indeterminadas en el escenario sin confirmaciones. Viabilidad técnica acotada y utilidad operativa insuficiente para una entrega. Se inicia [CRM](./INVESTIGACION_REQUISITOS_CULINARIOS.md); no se modifica v1.6.0.

## Corte de investigación de requisitos — 2026-11-19

#262 integrada. [CRM](./INVESTIGACION_REQUISITOS_CULINARIOS.md) acredita 121 pruebas, 16 casos representados y 20 ocurrencias anotadas manualmente de 5.047. Viabilidad representacional acotada; automatización no demostrada. Se inicia [CRR](./INVESTIGACION_RECONOCIMIENTO_REQUISITOS.md), sin alterar v1.6.0.

## Corte de reconocimiento — 2026-11-19

#267 integrada en `c31bf9d6372737c182df79a5961c75a3d5ebca72`; los tres workflows de main finalizaron correctamente. [CRR](./INVESTIGACION_RECONOCIMIENTO_REQUISITOS.md) acredita 128 pruebas en #266, 358 ocurrencias con propuestas y seis aciertos de diez casos positivos reservados. Utilidad incremental limitada; [deuda registrada](./DEUDA_REQUISITOS_CULINARIOS.md), integración diferida. v1.6.0 sin cambios.

## Corte de explotación práctica — 2026-11-19

Las cuatro unidades de [Culinary Explorer 0.1.0](./ALCANCE_CULINARY_EXPLORER.md) están integradas tras #274. El CI acredita 134 pruebas, 62 contrastes de búsqueda, 590 destinos HTML y recorridos en Chromium. #275 completa teclado y catálogo vacío en Chromium; carga pública confirmada por el propietario. Aceptación técnica acotada cerrada. v1.6.0 sin cambios.

## Corte de preparación guiada — 2026-11-19

#281 integra las cuatro unidades de [Culinary Recipe Assistant](./ALCANCE_CULINARY_RECIPE_ASSISTANT.md). CI de la PR: 141 pruebas Python, nueve Node, 62 contrastes, 590 recetas, 591 archivos y 51 destinos de técnicas; recorridos Chromium correctos. gh-pages registró el despliegue del merge; funcionamiento público comunicado posteriormente tras #284. v1.6.0 permanece vigente.

## Corte de inventario personal — 2026-11-19

#289 integra las cuatro unidades de [Culinary Pantry](./ALCANCE_CULINARY_PANTRY.md). Las pruebas dirigidas de inventario, persistencia, copias, cambios externos y transferencia a Explorer finalizaron correctamente en Chromium. CI: 141 Python y 30 Node; 590 recetas. gh-pages registra el despliegue del merge; comprobación pública pendiente. No se modifica v1.6.0.

## Corte de listas de compra — 2026-11-21

Las PR #291–#297 incorporan [Culinary Shopping 0.1.0](./ALCANCE_CULINARY_SHOPPING.md): listas declaradas, revisión de ingredientes desde Recipe Assistant, marcado de compras y alta confirmada de lotes en Pantry. La intención se registra previamente y una recuperación no recrea un lote de resultado incierto. Web Locks solo coordina operaciones cooperantes; no existe transacción atómica entre almacenamientos. CI #297: 141 pruebas Python, 63 Node y recorridos Chromium satisfactorios de Explorer, Assistant, Pantry y Shopping. gh-pages registra Deployed 765d507; se comprobaron los recursos publicados en la rama, no la experiencia de un usuario real en la URL pública. La release vigente sigue siendo v1.6.0.

## Corte de planificación culinaria — 2026-11-21

La PR #303 integra Culinary Planner 0.1.0 en el commit `fd3ddc760788dc0a61749c514f964d51a126a527`. El planificador permite registrar varias comidas por fecha, conservar referencias históricas, seleccionar expresamente recetas desde Explorer/Assistant y mantener copias locales independientes de Shopping/Pantry. CI de #303: los tres workflows finalizaron en success y Chromium confirmó la navegación y el aislamiento. El despliegue en gh-pages está comprobado (fd3ddc7 y página del planificador), pero esta evidencia no acredita el uso manual público. No hay prueba manual pública acreditada. La release publicada permanece v1.6.0.

# Estado por capacidades

| Capacidad | Estado |
|-----------|:------:|
| Identidad del proyecto | ✅ Consolidada |
| Arquitectura | ✅ Consolidada |
| Modelo de conocimiento | ✅ Consolidado |
| Gobernanza | ✅ Consolidada |
| Marco de especificaciones | ✅ Consolidado |
| Framework documental | ✅ Operativo |
| Pipeline documental | ✅ Operativo |
| Knowledge Graph | ✅ Operativo |
| Portal MkDocs | 🟢 Operativo |
| Base de conocimiento | 🟡 En consolidación; incorporación selectiva |
| Extractor de recetas 0.4.6 | 🟢 Prototipo contrastado |
| Índice de recetas 0.2.0 | 🟢 Prototipo contrastado |
| Motor de consultas 0.2.0 | 🟢 CLI de recuperación textual acotada, contrastada |
| Compatibilidad culinaria | 🟡 Investigación concluida; entrega diferida |
| Requisitos culinarios | 🟡 Viabilidad representacional acotada; entrega diferida |
| Reconocimiento de requisitos | 🟡 Viabilidad técnica acotada; entrega diferida |
| Culinary Explorer 0.1.0 | 🟢 Publicado; aceptación técnica acotada |
| Culinary Recipe Assistant 0.1.0 | 🟢 Publicado; funcionamiento comunicado tras #284 |
| Culinary Pantry 0.1.0 | 🟢 Integrado y desplegado; prueba pública pendiente |
| Culinary Shopping 0.1.0 | 🟢 Integrado y desplegado; aceptación técnica dirigida, prueba pública pendiente |
| Culinary Planner 0.1.0 | 🟢 Implementado y desplegado, con CI dirigido satisfactorio; prueba manual pública pendiente |
| Plataforma software | ⚪ Backend y Runtime planificados |

---

# Capacidades disponibles

Actualmente el SGCC permite:

- gestionar conocimiento culinario reutilizable;
- consultar recetas por metadatos, texto exacto, términos completos, identidad explícita y candidatos;
- mantener referencias cruzadas;
- validar automáticamente la documentación;
- analizar relaciones mediante Knowledge Graph;
- detectar deuda documental;
- gobernar la evolución del conocimiento;
- publicar documentación mediante MkDocs;
- definir contratos formales;
- describir Engines;
- especificar APIs;
- modelar Runtime;
- gobernar dependencias;
- mantener terminología unificada;
- validar coherencia documental;
- generar documentación automáticamente;
- auditar automáticamente la madurez de los dominios culinarios.

---

## Estado de los dominios culinarios

| Dominio | Estado |
|----------|---------|
| Currys | 🌳 Consolidado |
| Salteados asiáticos | 🌿 Estructurado |
| Arroces | 🌿 Estructurado |
| Verduras | 🌿 Estructurado |
| Carnes | 🌿 Estructurado |
| Pescados y mariscos | 🌿 Estructurado |
| Huevos y lácteos | 🌿 Estructurado |
| Pastas | 🌱 Exploración |
| Legumbres | 🌱 Exploración |
| Postres | 🌱 Exploración |

> Estado histórico obtenido de la auditoría publicada el 2026-08-03 (`audit_knowledge.py`); no representa una reevaluación actual.

---

## Próximo objetivo

Ejecutar el protocolo manual de aceptación de las cinco aplicaciones y evaluar la siguiente prioridad, conservando la evidencia experimental y la deuda registrada. No se compromete nueva release. La [consolidación del conocimiento](./CONSOLIDACION_CONOCIMIENTO.md) define los incrementos y sus condiciones de aceptación. Las recetas nuevas se incorporarán de forma selectiva según experiencia, carencias y reutilización.

---

## Consolidación de recorridos — 21 de noviembre de 2026

Las PR #306–#308 consolidan pruebas de extremo a extremo, recuperación conservadora de transferencias y accesibilidad dirigida en las cinco aplicaciones. Cada PR superó Knowledge integrity, Knowledge audit y Culinary Explorer site. El despliegue de la PR #308 se observó en gh-pages `63ea9fc73467b1503d62beeeca65508340fd0980` (`Deployed 49cd792`) y se comprobaron los enlaces de salto al contenido en los cinco HTML de la rama. La aceptación funcional manual del portal público no se ha documentado y no debe considerarse superada.

La Unidad D dispone de un [protocolo de aceptación pública](./PROTOCOLO_ACEPTACION_PUBLICA_CULINARIA.md) con evidencia pendiente de cumplimentar. Ninguna de las nuevas unidades compromete una release; la última versión autorizada es v1.6.0.

## Aceptación manual pública comunicada — 22 de noviembre de 2026

El propietario comunicó resultado satisfactorio tras ejecutar de forma guiada los controles de las cinco aplicaciones y el recorrido integrado de selección de receta, planificación, revisión y registro de compras, incorporación confirmada de un lote a Pantry, persistencia y exportación/previa de copias JSON. También confirmó navegación por teclado, ausencia de desbordamiento apreciable en ventana estrecha, protección frente a repetición de transferencia e independencia de estados entre Planner, Shopping y Pantry. No se han comunicado incidencias.

El [protocolo de aceptación pública](./PROTOCOLO_ACEPTACION_PUBLICA_CULINARIA.md) recoge PUB-01–PUB-07 como **satisfactorios dentro del alcance manual declarado**, sin capturas ni metadatos completos del navegador. Las pruebas destructivas solo conservan la evidencia de CI; no se consideran ejecutadas manualmente. Tras la fusión de [PR #335](https://github.com/fran-eliot/NovaCoquinaria/pull/335), el registro de aceptación manual queda incorporado a `main`. **CWC-12 y Unidad D: Complete — Bounded Public Acceptance**, exclusivamente dentro de los controles comunicados y documentados en el protocolo, sujeto a la aprobación de la presente PR de cierre. Las sondas públicas HTTP y Chromium ya disponen de ejecuciones satisfactorias independientes. No se autoriza nueva release, ni se modifica `v1.6.0`.

## Cierre de consolidación de recorridos culinarios — 22 de noviembre de 2026

Las unidades A, B y C mantienen la evidencia técnica de PR #306–#308; la Unidad D dispone de prueba HTTP pública, sonda Chromium pública y resultados manuales de PUB-01–PUB-07 incorporados mediante PR #335 (merge `b4386d057bfb434d04133949f85d0317123ba99e`). Se registra **CWC-12 como cerrado en alcance funcional acotado** con las restricciones del [protocolo](./PROTOCOLO_ACEPTACION_PUBLICA_CULINARIA.md). El cierre no comprende escenarios destructivos manuales, conformidad WCAG global, garantía de sincronización ni integridad culinaria exhaustiva.

La consolidación de las cinco aplicaciones no crea una nueva fase por sí sola. La siguiente decisión es revisar la utilidad práctica, las carencias del conocimiento y la deuda de identidad/requisitos antes de autorizar nuevas capacidades. Continúa `v1.6.0` como última release publicada; no se autoriza otra.

## Revisión estratégica posterior a CWC-12 — 22 de noviembre de 2026

Tras la integración de #336 y el cierre acotado de la aceptación funcional pública de las cinco aplicaciones, se propone desplazar el énfasis de las interfaces hacia la **calidad, trazabilidad y utilidad del conocimiento culinario**. La [revisión estratégica tras la aceptación pública](./REVISION_ESTRATEGICA_POST_ACEPTACION_PUBLICA.md) compara las alternativas y recomienda primero una línea base reproducible de cobertura y calidad editorial, reutilizando herramientas y separando mediciones automáticas de revisión humana.

Esta propuesta no equivale a una nueva fase implementada, no aprueba automáticamente el piloto editorial ni altera `v1.6.0`. El siguiente desarrollo requiere una decisión diferenciada y PR temática.

# Prioridades actuales

## Prioridad alta

- Actualizar la auditoría del conocimiento y distinguir métricas de inventario, madurez y validación culinaria.
- Revisar relaciones, duplicidades y formatos para consumo.
- Evaluar el valor práctico y los límites de identidad, tiempos y acceso antes de ampliar el motor.
- Mantener la incorporación selectiva de conocimiento culinario.

---

## Prioridad media

- Incrementar automatizaciones.
- Mejorar el Knowledge Graph.
- Publicar el portal documental.

---

## Prioridad estratégica

- Desarrollo de la plataforma software.
- Runtime del SGCC.
- GraphRAG.
- Integración con LLM.
- Agentes especializados.

---

# Indicadores de madurez

| Área | Nivel |
|------|:-----:|
| Arquitectura | 🟢 Alto |
| Gobernanza | 🟢 Alto |
| Especificaciones | 🟢 Alto |
| Automatización | 🟢 Alto |
| Knowledge Graph | 🟢 Alto |
| Conocimiento culinario | 🟡 Medio |
| Plataforma | ⚪ Inicial |

---

# Riesgos actuales

La fase requiere controlar la deuda semántica, la heterogeneidad del contenido, la trazabilidad y el riesgo de confundir metadatos incompletos con datos verificados.

Los principales retos del proyecto son:

- mantener sincronizadas especificaciones e implementación;
- evitar divergencias entre documentación y código;
- crecimiento equilibrado entre infraestructura y conocimiento;
- controlar la complejidad del Runtime.

---

# Próxima transición prevista

La representación derivada consultable dispone de evidencia técnica inicial; la siguiente transición requiere evaluar su utilidad práctica y decidir el alcance de la próxima capacidad. La plataforma software y el Runtime completo siguen planificados; no se ha elegido tecnología.

---

# Actualización del documento

PROJECT_STATUS deberá revisarse cuando ocurra alguno de los siguientes eventos:

- publicación de una nueva Release;
- cambio de fase del proyecto;
- modificación significativa de las prioridades;
- incorporación de nuevas capacidades.

---

# Relaciones con otros documentos

| Documento | Responsabilidad |
|-----------|-----------------|
| ROADMAP | Dirección estratégica |
| BITÁCORA | Evolución histórica |
| RELEASES | Versiones publicadas |
| CHANGELOG | Cambios por versión |
| DEVELOPMENT_WORKFLOW | Evolución del conocimiento |

---

# Documentación relacionada

## Gestión

- ROADMAP
- BITÁCORA
- RELEASES
- CHANGELOG

## Gobernanza

- DEVELOPMENT_WORKFLOW

---

# Conclusión

NovaCoquinaria ha completado la definición de su arquitectura documental y del marco de especificaciones que gobierna el Sistema de Gestión del Conocimiento Culinario (SGCC).

El proyecto dispone ahora de una base sólida y coherente sobre la que desarrollar la futura plataforma software, manteniendo la evolución paralela del conocimiento culinario y de la infraestructura tecnológica que lo soportará.