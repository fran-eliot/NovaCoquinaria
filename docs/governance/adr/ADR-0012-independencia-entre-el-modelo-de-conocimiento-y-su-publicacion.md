# ADR-0012 — Independencia entre el Modelo de Conocimiento y su Publicación

**Identificador:** ADR-0012

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Arquitectura

---

# Contexto

El SGCC gestiona conocimiento culinario mediante documentos estructurados en Markdown.

Ese conocimiento podrá consumirse desde múltiples canales:

- documentación navegable;
- sitios web;
- aplicaciones móviles;
- APIs;
- sistemas RAG;
- asistentes inteligentes;
- futuras plataformas tecnológicas.

Cada plataforma posee requisitos propios de presentación, navegación e interacción.

Sin embargo, todas deben consumir la misma base de conocimiento.

---

# Problema

Si el conocimiento se diseña pensando en una plataforma concreta:

- aumenta el acoplamiento tecnológico;
- disminuye la reutilización;
- dificulta la evolución futura;
- obliga a modificar el contenido al cambiar de herramienta.

El SGCC necesita un modelo que permita publicar el conocimiento mediante diferentes tecnologías sin alterar su estructura.

---

# Decisión

El modelo de conocimiento será completamente independiente de cualquier plataforma de publicación.

La organización del conocimiento deberá permitir que distintas tecnologías generen representaciones equivalentes a partir de una única fuente de verdad.

Las herramientas de publicación actuarán exclusivamente como consumidores especializados del repositorio.

---

# Justificación

Separar conocimiento y presentación garantiza la sostenibilidad del sistema.

La evolución o sustitución de una tecnología de publicación no implicará cambios en el modelo de conocimiento ni en los documentos que lo representan.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- El conocimiento no pertenece a ninguna plataforma.
- La publicación es una capacidad, no una característica del conocimiento.
- Toda plataforma consume la misma fuente de verdad.
- La presentación puede evolucionar independientemente del contenido.
- El modelo documental debe permanecer estable frente a cambios tecnológicos.

---

# Modelo conceptual

```text
            Conocimiento (Markdown)

                    │

        ┌───────────┼────────────┐
        │           │            │

     Web        Aplicación      IA

        │           │            │

     Plataforma de Publicación
```

Las plataformas interpretan el conocimiento.

No lo modifican.

---

# Capacidades arquitectónicas

La arquitectura deberá facilitar:

- publicación web;
- generación automática de documentación;
- navegación contextual;
- búsqueda estructurada;
- consumo mediante APIs;
- integración con asistentes inteligentes;
- futuras plataformas tecnológicas.

Estas capacidades se derivan del modelo de conocimiento y no de una herramienta específica.

---

# Alternativas consideradas

## Diseñar el repositorio para una única plataforma

Descartada por generar dependencia tecnológica.

---

## Mantener contenido específico para cada plataforma

Descartada por introducir duplicidad y aumentar el coste de mantenimiento.

---

## Acoplar la estructura documental a un generador concreto

Descartada por limitar la evolución del sistema.

---

# Consecuencias

## Ventajas

- Independencia tecnológica.
- Reutilización máxima.
- Evolución sencilla.
- Compatibilidad con múltiples plataformas.
- Mayor vida útil del conocimiento.

---

## Inconvenientes

- Requiere una estructura documental rigurosa.
- Algunas plataformas podrán necesitar adaptadores específicos.

---

# Impacto arquitectónico

Esta decisión desacopla completamente el conocimiento de sus mecanismos de publicación.

Como consecuencia:

- podrán incorporarse nuevas plataformas sin modificar el SGCC;
- las herramientas de publicación compartirán una misma base de conocimiento;
- la evolución tecnológica quedará desacoplada del modelo conceptual;
- el repositorio conservará su papel como única fuente de verdad.

---

# Relación con otros ADR

Este ADR desarrolla:

- ADR-0003 — Markdown como Fuente Única de Verdad.
- ADR-0010 — Arquitectura Orientada al Conocimiento.
- ADR-0011 — Modelo de Capas Conceptuales del Proyecto.

Es complementado posteriormente por:

- ADR-0018 — Modelo del Conocimiento del SGCC.
- ADR-0019 — Modelo Lógico vs Estructura Física.

---

# Documentación relacionada

La aplicación práctica de esta decisión se desarrolla en:

- ARQUITECTURA.md
- TOOLS_FRAMEWORK.md
- AUTOMATION.md
- ESPECIFICACION_DE_DOCUMENTOS.md

La selección de herramientas concretas de publicación (MkDocs, Material for MkDocs, Docusaurus u otras) constituye una decisión de implementación y podrá modificarse sin afectar a este ADR.

---

# Estado actual

La decisión continúa plenamente vigente.

El SGCC mantiene una arquitectura independiente de la plataforma de publicación, permitiendo que el mismo modelo de conocimiento pueda representarse mediante diferentes tecnologías presentes y futuras sin alterar su estructura ni comprometer la sostenibilidad del sistema.