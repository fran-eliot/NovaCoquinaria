# ADR-0005 — Descomposición del Conocimiento en Componentes Reutilizables

**Identificador:** ADR-0005

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Modelo del Conocimiento

---

# Contexto

Tras establecer que el SGCC gestiona conocimiento culinario (ADR-0001) y que dicho conocimiento reside en un repositorio Markdown (ADR-0003), resulta necesario definir cómo debe modelarse internamente.

Los recetarios tradicionales concentran toda la información dentro de cada receta.

Como consecuencia, técnicas, ingredientes, procedimientos y conceptos aparecen repetidos una y otra vez, dificultando el mantenimiento y favoreciendo las inconsistencias.

El SGCC persigue un modelo basado en reutilización del conocimiento.

---

# Problema

Es necesario decidir si el conocimiento culinario debe almacenarse como documentos monolíticos o descomponerse en componentes independientes.

La decisión condicionará:

- la reutilización;
- la mantenibilidad;
- la evolución del conocimiento;
- la construcción del grafo de conocimiento del SGCC.

---

# Decisión

El conocimiento culinario se descompondrá en **componentes especializados**, cada uno responsable de un único concepto.

Las recetas dejarán de ser el lugar donde reside el conocimiento y pasarán a convertirse en composiciones de componentes previamente documentados.

Cada componente evolucionará de manera independiente y podrá reutilizarse desde múltiples recetas.

---

# Justificación

La descomposición del conocimiento permite eliminar redundancias y favorecer la reutilización sistemática.

Cada modificación realizada sobre un componente beneficia automáticamente a todas las recetas que dependen de él.

Este modelo aproxima el conocimiento culinario a principios ampliamente utilizados en arquitectura del software, como la modularidad, la separación de responsabilidades y la reutilización.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- Cada componente representa un único concepto.
- Cada concepto debe documentarse una sola vez.
- Las recetas ensamblan conocimiento existente.
- La reutilización tiene prioridad sobre la duplicación.
- La evolución de un componente no debe requerir modificar todas las recetas que lo utilizan.

---

# Modelo conceptual

```text
                 Conocimiento Culinario

                         │

        ┌──────────────┬──────────────┬──────────────┐
        │              │              │              │
        ▼              ▼              ▼              ▼
    Técnicas     Ingredientes    Plantillas      Tablas
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                   Recetas
```

Las recetas representan una composición de componentes de conocimiento.

No constituyen el origen del conocimiento.

---

# Alternativas consideradas

## Documentos monolíticos

Descartados por:

- duplicación constante;
- mantenimiento complejo;
- inconsistencias;
- baja reutilización.

---

## Wiki sin clasificación

Descartada por:

- ausencia de responsabilidades claras;
- crecimiento desordenado;
- dificultad para automatización.

---

## Componentes parcialmente reutilizables

Descartados por mantener duplicidades innecesarias y dificultar la evolución del conocimiento.

---

# Consecuencias

## Ventajas

- Arquitectura modular.
- Máxima reutilización.
- Evolución independiente de cada componente.
- Menor deuda de conocimiento.
- Mayor coherencia documental.
- Mejor experiencia de aprendizaje.

---

## Inconvenientes

- Incremento del número de documentos.
- Necesidad de mantener referencias consistentes.
- Mayor disciplina en el diseño del conocimiento.

---

# Impacto arquitectónico

Esta decisión transforma el SGCC en un sistema basado en componentes de conocimiento.

Como consecuencia:

- las recetas pasan a ser composiciones;
- el conocimiento puede representarse como un grafo;
- se favorece la navegación contextual;
- se facilita la búsqueda semántica;
- se habilitan futuros sistemas RAG, asistentes inteligentes y motores de recomendación.

---

# Relación con otros ADR

Este ADR desarrolla:

- ADR-0001 — Filosofía del Proyecto.
- ADR-0003 — Markdown como Fuente Única de Verdad.
- ADR-0004 — Front Matter YAML como Modelo Canónico de Metadatos.

Es ampliado posteriormente por:

- ADR-0006 — Referencias Cruzadas.
- ADR-0010 — Arquitectura Orientada al Conocimiento.
- ADR-0018 — Modelo del Conocimiento del SGCC.
- ADR-0019 — Modelo Lógico vs Estructura Física.

---

# Documentación relacionada

Esta decisión se desarrolla en:

- ARQUITECTURA.md
- ESPECIFICACION_DE_DOCUMENTOS.md
- ESPECIFICACION_DE_COLECCIONES.md
- KNOWLEDGE_STRATEGY.md
- KNOWLEDGE_MATURITY.md
- KNOWLEDGE_DEBT.md

---

# Estado actual

La decisión continúa plenamente vigente y constituye uno de los principios fundamentales del modelo de conocimiento del SGCC.

Toda evolución futura deberá preservar la descomposición del conocimiento en componentes reutilizables, evitando la duplicación sistemática y favoreciendo la construcción progresiva del grafo de conocimiento del proyecto.
