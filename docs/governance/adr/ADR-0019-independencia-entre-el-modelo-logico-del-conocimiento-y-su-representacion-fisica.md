# ADR-0019 — Independencia entre el Modelo Lógico del Conocimiento y su Representación Física

**Identificador:** ADR-0019

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Arquitectura del Conocimiento

---

# Contexto

El SGCC representa conocimiento culinario mediante entidades, relaciones y metadatos organizados dentro de un modelo conceptual común.

Actualmente dicho conocimiento se almacena mediante documentos Markdown organizados en un repositorio de directorios y archivos.

Sin embargo, el almacenamiento constituye únicamente una representación física del conocimiento y no su definición conceptual.

La evolución futura del sistema podrá incorporar nuevos mecanismos de almacenamiento, indexación o publicación sin modificar el modelo lógico.

---

# Problema

Confundir la organización física con el modelo lógico del conocimiento provoca:

- dependencia entre almacenamiento y significado;
- reorganizaciones costosas;
- pérdida de flexibilidad;
- dificultad para evolucionar hacia modelos basados en grafos;
- acoplamiento innecesario entre arquitectura e implementación.

Es necesario establecer una separación explícita entre ambos niveles.

---

# Decisión

El SGCC distinguirá dos representaciones complementarias del conocimiento:

- un modelo lógico, responsable de definir las entidades, sus propiedades y sus relaciones;
- una representación física, responsable de almacenar, organizar y presentar dichas entidades.

La representación física podrá evolucionar libremente siempre que preserve el modelo lógico del conocimiento.

---

# Justificación

El conocimiento constituye el activo permanente del sistema.

Su representación física podrá modificarse para adaptarse a nuevas tecnologías, herramientas o necesidades organizativas sin alterar el significado de las entidades ni las relaciones existentes entre ellas.

Esta separación incrementa la estabilidad arquitectónica y facilita la evolución tecnológica del SGCC.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- El significado nunca depende de la ubicación física.
- La representación física es intercambiable.
- El modelo lógico constituye la referencia arquitectónica.
- Las relaciones prevalecen sobre la jerarquía documental.
- La arquitectura permanece estable frente a cambios tecnológicos.

---

# Modelo conceptual

```text
        Modelo Lógico del Conocimiento

         Entidades · Relaciones · Tipos

                    │

                    ▼

        Representación Física

   Markdown · Carpetas · Archivos

                    │

                    ▼

        Plataformas de Publicación
```

La representación implementa el modelo lógico, pero no lo define.

---

# Representaciones físicas

El modelo lógico podrá representarse mediante distintas implementaciones, entre ellas:

- documentos Markdown;
- repositorios Git;
- bases de datos;
- Knowledge Graphs;
- APIs;
- aplicaciones;
- plataformas web.

Todas ellas deberán preservar la misma semántica del conocimiento.

---

# Alternativas consideradas

## Identificar el modelo lógico con la estructura de carpetas

Descartada por introducir dependencia entre organización física y significado.

---

## Mantener una representación física única

Descartada por limitar la evolución tecnológica del sistema.

---

## Permitir que cada herramienta defina su propio modelo

Descartada por romper la coherencia del conocimiento.

---

# Consecuencias

## Ventajas

- Independencia tecnológica.
- Reorganización sencilla.
- Mayor flexibilidad.
- Compatibilidad con múltiples representaciones.
- Excelente preparación para Knowledge Graphs, RAG y sistemas inteligentes.

---

## Inconvenientes

- Requiere mantener explícitamente el modelo lógico.
- Exige disciplina en la gestión de metadatos y relaciones.

---

# Impacto arquitectónico

Esta decisión desacopla completamente el conocimiento de su representación física.

Como consecuencia:

- la reorganización del repositorio no alterará el modelo conceptual;
- nuevas tecnologías de almacenamiento podrán incorporarse sin modificar el conocimiento;
- la navegación podrá generarse a partir del modelo lógico y no únicamente de la estructura documental;
- el SGCC conservará una arquitectura estable frente a cambios de implementación.

---

# Relación con otros ADR

Este ADR desarrolla:

- ADR-0003 — Markdown como Fuente Única de Verdad.
- ADR-0008 — Identidad Persistente de las Unidades de Conocimiento.
- ADR-0012 — Independencia entre el Modelo de Conocimiento y su Publicación.
- ADR-0018 — Ontología del Conocimiento del SGCC.

Se complementa con:

- KNOWLEDGE_MODEL.md
- KNOWLEDGE_GRAPH.md
- ESPECIFICACION_DE_DOCUMENTOS.md

---

# Documentación relacionada

La aplicación práctica de esta decisión se desarrolla en:

- ARQUITECTURA.md
- KNOWLEDGE_MODEL.md
- KNOWLEDGE_GRAPH.md
- ESPECIFICACION_DE_DOCUMENTOS.md

Las implementaciones concretas de almacenamiento podrán evolucionar sin modificar el modelo lógico definido por este ADR.

---

# Estado actual

La decisión continúa plenamente vigente.

El SGCC mantiene una arquitectura en la que el modelo lógico del conocimiento permanece independiente de cualquier representación física, garantizando que la evolución del almacenamiento, la organización documental o las plataformas tecnológicas no altere el significado ni las relaciones del conocimiento gestionado.