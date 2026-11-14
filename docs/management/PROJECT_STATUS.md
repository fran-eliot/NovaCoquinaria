---
id: DOC-0011
titulo: Estado del Proyecto
tipo: gestion
version: 2.0
estado: estable
ultima_revision: 2026-08-02
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
| Fase | Expansión del conocimiento culinario |
| Madurez global | Alta |
| Próximo objetivo | Expansión sistemática de la base de conocimiento culinario |

---

# Estado general

## Situación actual

NovaCoquinaria dispone actualmente de una arquitectura documental consolidada, un modelo formal de conocimiento, un marco completo de gobernanza y un conjunto integral de especificaciones que describen la organización, los motores de ejecución, las interfaces y la evolución del SGCC.

Tras completar este marco de especificaciones (v1.5.0), el proyecto ha iniciado una nueva fase centrada en la expansión sistemática del conocimiento culinario. Durante esta etapa se ha consolidado el dominio **Currys** como primer dominio culinario completo del repositorio, validando el modelo mediante ingredientes, técnicas, plantillas, tablas comparativas y recetas reutilizables.

El sistema de auditoría del conocimiento permite medir automáticamente la cobertura estructural, la madurez y la reutilización del conocimiento por dominios culinarios, facilitando la planificación de futuras ampliaciones.

---

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
| Base de conocimiento | 🟡 En expansión |
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

> Estado obtenido mediante la auditoría automática del conocimiento (`audit_knowledge.py`).

---

## Próximo objetivo

Continuar la expansión del conocimiento culinario aplicando el modelo consolidado en Currys a nuevos dominios, comenzando por Pastas o Legumbres, e incorporando progresivamente nuevos ingredientes, técnicas, tablas y recetas de autoridad.

---

# Prioridades actuales

## Prioridad alta

- Ampliar la base de conocimiento culinario.
- Consolidar dominios culinarios.
- Completar recetas de referencia.
- Mejorar las herramientas de auditoría del conocimiento.

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

Actualmente no existen riesgos arquitectónicos relevantes.

Los principales retos del proyecto son:

- mantener sincronizadas especificaciones e implementación;
- evitar divergencias entre documentación y código;
- crecimiento equilibrado entre infraestructura y conocimiento;
- controlar la complejidad del Runtime.

---

# Próxima transición prevista

La siguiente transición significativa se producirá cuando el SGCC deje de ser únicamente una arquitectura documental y pase a disponer de una primera implementación software de sus componentes principales, iniciando la materialización del Runtime descrito en las especificaciones.

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