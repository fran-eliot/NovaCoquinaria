---
id: DOC-0011
titulo: Estado del Proyecto
tipo: gestion
version: 3.0
estado: estable
ultima_revision: 2026-11-19
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
| Próximo objetivo | Definir alcance de Culinary Recipe Assistant |

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

Definir el alcance de Culinary Recipe Assistant para la preparación cotidiana, conservando la evidencia experimental y la deuda registrada. No se compromete nueva release. La [consolidación del conocimiento](./CONSOLIDACION_CONOCIMIENTO.md) define los incrementos y sus condiciones de aceptación. Las recetas nuevas se incorporarán de forma selectiva según experiencia, carencias y reutilización.

---

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