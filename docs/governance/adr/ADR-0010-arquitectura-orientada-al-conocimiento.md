# ADR-0010 — Arquitectura Orientada al Conocimiento del Sistema de Gestión del Conocimiento Culinario

**Identificador:** ADR-0010

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Arquitectura

---

# Contexto

El propósito del SGCC no es desarrollar una aplicación concreta.

Su objetivo es construir un sistema de conocimiento culinario capaz de alimentar múltiples consumidores presentes y futuros.

Entre ellos:

- documentación;
- aplicaciones;
- automatizaciones;
- motores de búsqueda;
- asistentes inteligentes;
- sistemas RAG;
- agentes especializados;
- futuras plataformas aún no definidas.

Para lograrlo, la arquitectura debe priorizar el conocimiento sobre cualquier implementación tecnológica.

---

# Problema

Los sistemas tradicionales suelen diseñarse alrededor de una aplicación.

Como consecuencia:

- el conocimiento queda acoplado a una tecnología;
- la reutilización resulta limitada;
- la evolución depende del software existente.

El SGCC necesita una arquitectura donde el conocimiento permanezca estable mientras las aplicaciones evolucionan de forma independiente.

---

# Decisión

El SGCC adoptará una arquitectura orientada al conocimiento.

El conocimiento constituye el activo central del sistema.

Todas las herramientas, procesos y aplicaciones actuarán como consumidores del conocimiento sin convertirse en propietarios del mismo.

La arquitectura deberá favorecer simultáneamente:

- comprensión humana;
- procesamiento automático;
- reutilización;
- evolución independiente;
- interoperabilidad.

---

# Justificación

Situar el conocimiento en el centro de la arquitectura permite desacoplar completamente la información de las tecnologías que la consumen.

Las aplicaciones podrán aparecer, evolucionar o desaparecer sin comprometer la integridad del conocimiento.

Este enfoque maximiza la reutilización y garantiza la sostenibilidad a largo plazo del SGCC.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- El conocimiento es el activo principal del SGCC.
- Ninguna aplicación posee el conocimiento.
- Toda herramienta consume el mismo repositorio.
- La arquitectura debe priorizar la reutilización.
- La automatización surge del modelo del conocimiento.
- La IA interpreta el conocimiento; no lo sustituye.
- La representación documental debe servir tanto a personas como a máquinas.

---

# Modelo conceptual

```text
                Conocimiento

                      │

        ┌─────────────┼─────────────┐
        │             │             │

 Documentación   Automatización   Aplicaciones

                      │

               Inteligencia Artificial
```

Todo el ecosistema consume una única base de conocimiento.

---

# Capacidades arquitectónicas

La arquitectura deberá facilitar, entre otras:

- navegación contextual;
- automatización documental;
- búsqueda semántica;
- generación de índices;
- construcción del Knowledge Graph;
- sistemas RAG;
- agentes especializados;
- futuras plataformas tecnológicas.

Estas capacidades son consecuencia del modelo de conocimiento y no requisitos independientes.

---

# Alternativas consideradas

## Arquitectura centrada en una aplicación

Descartada por acoplar el conocimiento a una implementación concreta.

---

## Arquitectura centrada exclusivamente en documentación

Descartada por limitar la reutilización automática del conocimiento.

---

## Arquitectura centrada exclusivamente en IA

Descartada por convertir la IA en el elemento central del sistema en lugar del conocimiento.

---

# Consecuencias

## Ventajas

- Independencia tecnológica.
- Máxima reutilización.
- Escalabilidad.
- Evolución sostenible.
- Integración sencilla de nuevas herramientas.
- Preparación para IA.
- Automatización natural.

---

## Inconvenientes

- Mayor esfuerzo inicial de modelado.
- Necesidad de mantener una arquitectura documental rigurosa.
- Requiere disciplina en la gobernanza del conocimiento.

---

# Impacto arquitectónico

Esta decisión sitúa el conocimiento como núcleo permanente del SGCC.

Como consecuencia:

- las aplicaciones dejan de almacenar conocimiento;
- la automatización reutiliza el mismo modelo;
- los asistentes inteligentes trabajan sobre una base común;
- el Knowledge Graph emerge de la propia arquitectura;
- futuras tecnologías podrán incorporarse sin modificar el modelo conceptual.

---

# Relación con otros ADR

Este ADR integra y consolida:

- ADR-0001 — Filosofía del Proyecto.
- ADR-0003 — Markdown como Fuente Única de Verdad.
- ADR-0005 — Descomposición del Conocimiento.
- ADR-0006 — Modelo de Relaciones.
- ADR-0007 — Modelo Conceptual del Dominio.
- ADR-0008 — Identidad Persistente.
- ADR-0009 — Ciclo de Vida y Evolución.

Es desarrollado posteriormente por:

- ADR-0012 — Automatización del SGCC.
- ADR-0018 — Modelo del Conocimiento del SGCC.
- ADR-0019 — Modelo Lógico vs Estructura Física.

---

# Documentación relacionada

La aplicación práctica de esta decisión se desarrolla en:

- ARQUITECTURA.md
- GOVERNANCE_MODEL.md
- KNOWLEDGE_STRATEGY.md
- AI_PROTOCOL.md
- AUTOMATION.md
- QUALITY.md

---

# Estado actual

La decisión continúa plenamente vigente.

La arquitectura orientada al conocimiento constituye el principio organizador del SGCC.

Toda evolución futura deberá preservar el conocimiento como núcleo permanente del sistema y considerar la automatización, las aplicaciones y la inteligencia artificial como consumidores especializados de una misma base de conocimiento compartida.