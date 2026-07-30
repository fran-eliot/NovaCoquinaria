# Architecture Decision Records (ADR)

> Decisiones arquitectónicas que definen la evolución, gobernanza y modelo de conocimiento del Sistema de Gestión del Conocimiento Culinario (SGCC).

---

## Propósito

Los Architecture Decision Records (ADR) constituyen la memoria arquitectónica de NovaCoquinaria.

Cada ADR documenta una decisión estable que afecta a la arquitectura del proyecto, preservando:

- el contexto en el que se tomó;
- el problema que resuelve;
- la decisión adoptada;
- su justificación;
- sus consecuencias;
- su relación con otras decisiones.

Los ADR representan conocimiento arquitectónico y, por tanto, evolucionan únicamente cuando cambia la arquitectura del SGCC.

---

# Organización

Los ADR se agrupan conceptualmente en tres grandes bloques.

## I. Fundamentos

Establecen los principios básicos del proyecto.

- ADR-0001 — Filosofía del Proyecto
- ADR-0002 — Documentación como Código
- ADR-0003 — Markdown como Fuente Única de Verdad
- ADR-0004 — Front Matter YAML como Metadatos Canónicos

---

## II. Arquitectura del Conocimiento

Definen cómo se estructura y organiza el conocimiento.

- ADR-0005 — Descomposición del Conocimiento en Componentes Reutilizables
- ADR-0006 — Modelo de Relaciones del Conocimiento
- ADR-0007 — Modelo Conceptual del Dominio del SGCC
- ADR-0008 — Identidad Persistente de las Unidades de Conocimiento
- ADR-0009 — Ciclo de Vida y Evolución de las Unidades de Conocimiento
- ADR-0010 — Arquitectura Orientada al Conocimiento
- ADR-0011 — Modelo de Capas Conceptuales del Proyecto

---

## III. Gobernanza y Evolución

Definen cómo evoluciona y se gobierna el conocimiento.

- ADR-0012 — Independencia entre el Modelo de Conocimiento y su Publicación
- ADR-0013 — Gobernanza de la Publicación y Apertura del Conocimiento
- ADR-0014 — Modelo de Gestión del Conocimiento del SGCC
- ADR-0015 — Arquitectura Basada en Componentes de Conocimiento
- ADR-0016 — Estrategia de Evolución del Conocimiento del SGCC
- ADR-0017 — Modelo de Abstracción del Conocimiento Culinario
- ADR-0018 — Ontología del Conocimiento del SGCC
- ADR-0019 — Independencia entre el Modelo Lógico del Conocimiento y su Representación Física

---

# Relación con la documentación

Los ADR establecen decisiones arquitectónicas permanentes.

No contienen especificaciones de implementación.

Las implementaciones concretas se desarrollan en documentos como:

- ARQUITECTURA.md
- KNOWLEDGE_MODEL.md
- KNOWLEDGE_GRAPH.md
- GOVERNANCE_MODEL.md
- ESPECIFICACION_DE_DOCUMENTOS.md
- KNOWLEDGE_STRATEGY.md

---

# Ciclo de vida

Los ADR son documentos estables.

Una vez aceptados:

- no describen implementaciones temporales;
- no sustituyen a la documentación funcional;
- solo se modifican cuando cambia una decisión arquitectónica.

La evolución normal del proyecto se refleja mediante nuevos ADR o mediante la actualización explícita de los existentes.

---

# Estado actual

Actualmente el SGCC dispone de un conjunto de ADR que definen de forma coherente:

- los principios fundamentales del proyecto;
- la arquitectura del conocimiento;
- la gobernanza del sistema;
- el modelo conceptual del dominio;
- la estrategia de evolución del conocimiento;
- la ontología del SGCC;
- la independencia entre el modelo lógico y sus representaciones físicas.

En conjunto constituyen la referencia arquitectónica oficial de NovaCoquinaria.

---

# Evolución de la arquitectura

Los ADR siguen una secuencia lógica de construcción:

```text
Fundamentos
      ↓
Arquitectura del conocimiento
      ↓
Gobernanza
      ↓
Modelo conceptual
      ↓
Ontología
      ↓
Representación del conocimiento

Cada ADR amplía decisiones anteriores sin reemplazarlas, formando un cuerpo arquitectónico coherente y evolutivo.
```