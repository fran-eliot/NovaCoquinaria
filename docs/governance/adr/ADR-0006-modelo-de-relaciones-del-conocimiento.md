# ADR-0006 — Referencias Cruzadas como Modelo de Relaciones del Conocimiento

**Identificador:** ADR-0006

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Modelo del Conocimiento

---

# Contexto

El SGCC organiza el conocimiento como un conjunto de componentes reutilizables (ADR-0005).

Sin embargo, un conjunto de documentos independientes no constituye por sí mismo un sistema de conocimiento.

Es necesario representar explícitamente las relaciones existentes entre dichos componentes para preservar el contexto, facilitar la reutilización y permitir una navegación coherente.

Las relaciones forman parte del propio conocimiento y no únicamente de su presentación.

---

# Problema

Es necesario definir un mecanismo uniforme para expresar relaciones entre documentos.

Dicho mecanismo debe:

- evitar duplicidades;
- facilitar la navegación;
- permitir el análisis automático de dependencias;
- servir de base para la construcción del Knowledge Graph del SGCC;
- ser comprensible tanto para personas como para herramientas.

---

# Decisión

Los documentos del SGCC establecerán relaciones explícitas mediante referencias cruzadas.

Las referencias representan relaciones semánticas entre componentes de conocimiento.

Estas relaciones deberán utilizar una estructura homogénea y mantenerse sincronizadas con la evolución del repositorio.

Las referencias forman parte del modelo del conocimiento y no constituyen simples enlaces de navegación.

---

# Justificación

El conocimiento adquiere significado no solo por el contenido de cada documento, sino también por las relaciones que mantiene con otros.

Representar dichas relaciones explícitamente permite:

- contextualizar el conocimiento;
- favorecer la reutilización;
- analizar impactos;
- construir grafos de conocimiento;
- automatizar procesos de navegación e indexación.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- Todo componente puede relacionarse con otros componentes.
- Las relaciones representan significado, no únicamente navegación.
- El conocimiento debe ser navegable en cualquier dirección.
- Las referencias deberán mantenerse coherentes con la evolución del repositorio.
- El modelo de relaciones constituye parte del SGCC.

---

# Modelo conceptual

```text
                Knowledge Graph

        Ingrediente ───────┐
                            │
        Técnica ────────────┤
                            ▼
                       Receta
                            ▲
        Plantilla ──────────┤
                            │
        Tabla ──────────────┘
```

Los documentos representan nodos.

Las referencias representan relaciones.

El conjunto constituye el Knowledge Graph del SGCC.

---

# Tipos de relaciones

El SGCC podrá establecer distintos tipos de relaciones semánticas.

Entre ellas:

- dependencias;
- ampliaciones;
- reutilización;
- composición;
- referencias relacionadas.

La definición concreta de cada tipo pertenece al Modelo Documental y podrá evolucionar independientemente de este ADR.

---

# Alternativas consideradas

## Documentos independientes

Descartados por:

- aislar el conocimiento;
- dificultar la reutilización;
- impedir el análisis de dependencias.

---

## Enlaces arbitrarios

Descartados por:

- falta de consistencia;
- dificultad para automatización;
- ausencia de significado semántico.

---

## Relaciones implícitas

Descartadas por:

- depender exclusivamente de interpretación humana;
- impedir el procesamiento automático.

---

# Consecuencias

## Ventajas

- Knowledge Graph explícito.
- Navegación contextual.
- Reutilización del conocimiento.
- Mejor comprensión del dominio.
- Automatización.
- Análisis de impacto.
- Integración con IA.

---

## Inconvenientes

- Mayor disciplina documental.
- Necesidad de mantener relaciones consistentes.
- Validación automática de referencias.

---

# Impacto arquitectónico

Esta decisión transforma el repositorio en una red de conocimiento explícitamente conectada.

Como consecuencia:

- podrán generarse mapas de conocimiento;
- será posible navegar por relaciones semánticas;
- podrán realizarse análisis de impacto;
- los sistemas RAG dispondrán de contexto estructurado;
- los asistentes inteligentes comprenderán mejor la relación entre conceptos.

---

# Relación con otros ADR

Este ADR desarrolla:

- ADR-0003 — Markdown como Fuente Única de Verdad.
- ADR-0004 — Front Matter YAML como Modelo Canónico de Metadatos.
- ADR-0005 — Descomposición del Conocimiento en Componentes Reutilizables.

Es ampliado posteriormente por:

- ADR-0010 — Arquitectura Orientada al Conocimiento.
- ADR-0018 — Modelo del Conocimiento del SGCC.
- ADR-0019 — Modelo Lógico vs Estructura Física.

---

# Documentación relacionada

La implementación de esta decisión se desarrolla en:

- ESPECIFICACION_DE_DOCUMENTOS.md
- ESPECIFICACION_DE_COLECCIONES.md
- ARQUITECTURA.md
- KNOWLEDGE_STRATEGY.md
- TOOLS_FRAMEWORK.md

La representación concreta de las referencias podrá evolucionar sin modificar esta decisión arquitectónica.

---

# Estado actual

La decisión continúa plenamente vigente.

Las referencias cruzadas constituyen uno de los mecanismos fundamentales mediante los que el SGCC representa el conocimiento como una red de componentes interconectados.

Toda evolución futura deberá preservar el carácter explícito, coherente y semántico de dichas relaciones.
