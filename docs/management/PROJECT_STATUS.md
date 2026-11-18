---
id: DOC-0011
titulo: Estado del Proyecto
tipo: gestion
version: 2.1
estado: estable
ultima_revision: 2026-11-18
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
| Versión actual | **v1.5.0 (tras la release)** |
| Estado | 🟢 Desarrollo activo |
| Fase | Consolidación y explotación del conocimiento |
| Madurez global | Pendiente de reevaluación con auditoría actualizada |
| Próximo objetivo | Línea base reproducible de calidad y preparación para consumo |

---

# Estado general

## Situación actual

NovaCoquinaria dispone actualmente de una arquitectura documental consolidada, un modelo formal de conocimiento, un marco completo de gobernanza y un conjunto integral de especificaciones que describen la organización, los motores de ejecución, las interfaces y la evolución del SGCC.

Tras completar este marco de especificaciones (v1.5.0), el proyecto ha iniciado una nueva fase centrada en la expansión sistemática del conocimiento culinario. Durante esta etapa se ha consolidado el dominio **Currys** como primer dominio culinario completo del repositorio, validando el modelo mediante ingredientes, técnicas, plantillas, tablas comparativas y recetas reutilizables.

El sistema de auditoría del conocimiento permite medir automáticamente la cobertura estructural, la madurez y la reutilización del conocimiento por dominios culinarios, facilitando la planificación de futuras ampliaciones.

---

## Corte de transición — 2026-11-18

El inventario comprobado tras la PR #193 contiene 922 archivos Markdown, 590 fichas de recetas, 125 fichas de ingredientes y 52 técnicas. La serie española comprende 174 propuestas en 29 tandas. La PR #194 incorpora la propuesta de transición. Los recuentos son de rutas, no acreditan unicidad semántica ni pruebas culinarias. El informe de auditoría publicado sigue fechado el 2026-08-03; se requiere una nueva línea base antes de actualizar la madurez de los dominios.

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
| Plataforma software | ⚪ En fase de diseño |

---

# Capacidades disponibles

Actualmente el SGCC permite:

- gestionar conocimiento culinario reutilizable;
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

Establecer una línea base reproducible de calidad documental y relaciones para orientar la estructuración e indexación del conocimiento. La [consolidación del conocimiento](./CONSOLIDACION_CONOCIMIENTO.md) define los incrementos y sus condiciones de aceptación. Las recetas nuevas se incorporarán de forma selectiva según experiencia, carencias y reutilización.

---

# Prioridades actuales

## Prioridad alta

- Actualizar la auditoría del conocimiento y distinguir métricas de inventario, madurez y validación culinaria.
- Revisar relaciones, duplicidades y formatos para consumo.
- Definir un contrato de datos de recetas a partir de muestras representativas.
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

La siguiente transición se evaluará tras demostrar la utilidad de una representación derivada consultable del conocimiento. La plataforma software y el Runtime completo siguen planificados; no se ha elegido tecnología.

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