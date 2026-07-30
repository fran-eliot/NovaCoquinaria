# ADR-0009 — Ciclo de Vida y Evolución de las Unidades de Conocimiento

**Identificador:** ADR-0009

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Gobernanza del Conocimiento

---

# Contexto

El conocimiento gestionado por el SGCC evoluciona de forma continua.

Nuevas técnicas, ingredientes, recetas y relaciones se incorporan progresivamente al sistema.

Sin embargo, la evolución del conocimiento debe realizarse de forma controlada para preservar la calidad, la coherencia y la estabilidad del repositorio.

Es necesario distinguir entre la evolución del contenido y el grado de consolidación de cada unidad de conocimiento.

---

# Problema

Cada unidad de conocimiento puede cambiar a lo largo del tiempo.

Sin un modelo común resulta difícil:

- conocer el grado de consolidación del documento;
- controlar su evolución;
- coordinar revisiones;
- automatizar procesos de calidad;
- ofrecer información fiable a consumidores del conocimiento.

---

# Decisión

Toda unidad de conocimiento del SGCC dispondrá de dos mecanismos independientes de evolución:

- un estado que represente su ciclo de vida documental;
- una versión que represente la evolución de su contenido.

Ambos mecanismos formarán parte de los metadatos oficiales del documento.

---

# Justificación

El estado y la versión responden a preguntas diferentes.

El estado indica el grado de consolidación del documento.

La versión describe la evolución del contenido.

Mantener ambos conceptos separados facilita la gobernanza del conocimiento y evita confundir estabilidad con evolución.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- Todo documento posee un ciclo de vida.
- Todo documento posee una versión.
- El estado y la versión evolucionan de forma independiente.
- La evolución del conocimiento debe ser trazable.
- La calidad documental debe mantenerse durante toda la vida del documento.

---

# Modelo conceptual

```text
          Unidad de Conocimiento

                    │
        ┌───────────┴───────────┐
        │                       │

  Ciclo de Vida            Versionado

        │                       │

 Consolidación          Evolución del
 del documento            contenido
```

El estado refleja madurez documental.

La versión refleja evolución del contenido.

---

# Ciclo de vida

Las unidades de conocimiento seguirán un ciclo documental común.

Los estados concretos y sus reglas forman parte del Modelo Documental y podrán evolucionar independientemente de este ADR.

El ciclo de vida permite conocer el grado de consolidación de cada documento y coordinar su revisión dentro del SGCC.

---

# Versionado

Toda unidad de conocimiento dispondrá de una versión propia.

El sistema de versionado permitirá reflejar la evolución controlada del contenido manteniendo su trazabilidad histórica.

La estrategia concreta de versionado pertenece al Modelo Documental y podrá evolucionar sin modificar esta decisión.

---

# Alternativas consideradas

## Sin estados documentales

Descartada por impedir conocer el nivel de consolidación del conocimiento.

---

## Versionado únicamente a nivel de proyecto

Descartado por no reflejar la evolución independiente de cada unidad de conocimiento.

---

## Sin versionado

Descartado por dificultar la trazabilidad y la evolución controlada del conocimiento.

---

# Consecuencias

## Ventajas

- Evolución controlada.
- Trazabilidad.
- Gobernanza del conocimiento.
- Mejor automatización.
- Integración con procesos de revisión.
- Mayor calidad documental.

---

## Inconvenientes

- Mayor disciplina de mantenimiento.
- Necesidad de actualizar metadatos.
- Validaciones adicionales.

---

# Impacto arquitectónico

Esta decisión proporciona un mecanismo uniforme para gestionar la evolución del conocimiento del SGCC.

Como consecuencia:

- podrán automatizarse revisiones;
- podrán detectarse documentos desactualizados;
- podrán generarse informes de calidad;
- las aplicaciones podrán adaptar su comportamiento según el estado documental;
- el historial de evolución permanecerá desacoplado de la estructura física del repositorio.

---

# Relación con otros ADR

Este ADR desarrolla:

- ADR-0004 — Front Matter YAML como Modelo Canónico de Metadatos.
- ADR-0008 — Identidad Persistente de las Unidades de Conocimiento.

Es complementado posteriormente por:

- ADR-0012 — Automatización del SGCC.
- ADR-0018 — Modelo del Conocimiento del SGCC.

---

# Documentación relacionada

La implementación de esta decisión se desarrolla en:

- ESPECIFICACION_DE_DOCUMENTOS.md
- QUALITY.md
- KNOWLEDGE_MATURITY.md
- KNOWLEDGE_DEBT.md
- QUALITY_PIPELINE.md

La definición concreta de estados, reglas de transición y estrategia de versionado forma parte del Modelo Documental y podrá evolucionar sin modificar este ADR.

---

# Estado actual

La decisión continúa plenamente vigente.

El ciclo de vida y el versionado constituyen dos mecanismos complementarios de gobernanza que permiten gestionar la evolución de las unidades de conocimiento del SGCC preservando su trazabilidad, calidad y estabilidad a largo plazo.