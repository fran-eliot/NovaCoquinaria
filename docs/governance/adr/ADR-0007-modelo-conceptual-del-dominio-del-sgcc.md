# ADR-0007 — Modelo Conceptual del Dominio del Sistema de Gestión del Conocimiento Culinario

**Identificador:** ADR-0007

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Modelo del Dominio

---

# Contexto

El SGCC no almacena únicamente documentos.

Gestiona un dominio de conocimiento culinario compuesto por conceptos especializados y las relaciones existentes entre ellos.

Tras establecer la filosofía del proyecto (ADR-0001), la fuente oficial del conocimiento (ADR-0003), la descomposición en componentes reutilizables (ADR-0005) y el modelo de relaciones (ADR-0006), resulta necesario definir el modelo conceptual que representa el dominio del conocimiento culinario.

Este modelo constituye la base sobre la que se construye toda la arquitectura del SGCC.

---

# Problema

Es necesario definir un modelo conceptual estable que represente el dominio culinario con independencia de:

- la organización física del repositorio;
- la estructura documental;
- las aplicaciones que consuman el conocimiento;
- las tecnologías utilizadas.

Este modelo deberá servir como referencia para toda evolución futura del SGCC.

---

# Decisión

El Sistema de Gestión del Conocimiento Culinario representará el dominio mediante un conjunto de entidades conceptuales claramente diferenciadas.

Cada entidad representa un concepto del dominio y mantiene una única responsabilidad.

Las entidades podrán relacionarse mediante referencias semánticas explícitas formando una red de conocimiento.

La representación documental de dichas entidades podrá evolucionar sin modificar este modelo conceptual.

---

# Justificación

Separar el dominio conceptual de su representación documental permite construir una arquitectura estable y evolutiva.

El conocimiento deja de depender de documentos concretos y pasa a representarse mediante conceptos relacionados entre sí.

Este enfoque facilita:

- reutilización;
- mantenibilidad;
- evolución;
- automatización;
- interoperabilidad.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- El dominio es independiente de la implementación.
- Cada entidad representa un único concepto.
- Las entidades mantienen relaciones explícitas.
- El modelo conceptual constituye la referencia del SGCC.
- La estructura documental implementa el modelo, pero no lo define.

---

# Modelo conceptual

```text
                 Sistema de Gestión del
              Conocimiento Culinario (SGCC)

                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼

   Ingredientes      Técnicas      Plantillas

        │                │                │
        └────────────┬───┴────────────┬───┘
                     ▼                ▼

                 Recetas          Tablas

                     │
                     ▼

            Otros conceptos futuros
```

Las entidades representan conceptos.

Las relaciones representan conocimiento.

El conjunto constituye el modelo conceptual del SGCC.

---

# Componentes del dominio

El dominio podrá incorporar diferentes tipos de entidades especializadas.

Entre ellas:

- ingredientes;
- técnicas;
- plantillas;
- recetas;
- tablas;
- notas;
- futuros conceptos que amplíen el dominio.

La definición concreta de cada entidad pertenece al Modelo Documental del proyecto y podrá evolucionar sin modificar este ADR.

---

# Alternativas consideradas

## Modelo centrado exclusivamente en recetas

Descartado por:

- duplicación del conocimiento;
- escasa reutilización;
- baja escalabilidad.

---

## Organización basada únicamente en carpetas

Descartada por confundir la representación física con el dominio conceptual.

---

## Dominio implícito

Descartado por dificultar:

- la evolución;
- la automatización;
- la interoperabilidad.

---

# Consecuencias

## Ventajas

- Modelo conceptual estable.
- Independencia tecnológica.
- Escalabilidad.
- Reutilización.
- Coherencia arquitectónica.
- Base para automatización.
- Integración con IA.

---

## Inconvenientes

- Mayor esfuerzo inicial de modelado.
- Necesidad de mantener coherencia conceptual.
- Evolución controlada del dominio.

---

# Impacto arquitectónico

Esta decisión convierte el SGCC en un sistema basado en un modelo conceptual explícito.

Como consecuencia:

- los documentos representan entidades del dominio;
- las referencias representan relaciones del dominio;
- el Knowledge Graph refleja directamente el modelo conceptual;
- futuras aplicaciones podrán reutilizar el mismo modelo independientemente de la tecnología empleada.

---

# Relación con otros ADR

Este ADR desarrolla:

- ADR-0001 — Filosofía del Proyecto.
- ADR-0005 — Descomposición del Conocimiento en Componentes Reutilizables.
- ADR-0006 — Referencias Cruzadas como Modelo de Relaciones del Conocimiento.

Es ampliado posteriormente por:

- ADR-0010 — Arquitectura Orientada al Conocimiento.
- ADR-0018 — Modelo del Conocimiento del SGCC.
- ADR-0019 — Modelo Lógico vs Estructura Física.

---

# Documentación relacionada

La implementación de esta decisión se desarrolla en:

- ARQUITECTURA.md
- ESPECIFICACION_DE_DOCUMENTOS.md
- ESPECIFICACION_DE_COLECCIONES.md
- GOVERNANCE_MODEL.md
- KNOWLEDGE_STRATEGY.md

La definición concreta de las entidades y su representación documental podrá evolucionar sin modificar este ADR.

---

# Estado actual

La decisión continúa plenamente vigente.

El Modelo Conceptual del Dominio constituye uno de los pilares arquitectónicos del SGCC y sirve como referencia para toda evolución del sistema, independientemente de la organización física del repositorio o de las tecnologías utilizadas.