# ADR-0003 — Markdown como Fuente Única de Verdad

**Identificador:** ADR-0003

**Estado:** Aceptado

**Vigencia:** Activa

**Última Revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Arquitectura

---

# Contexto

Una de las decisiones fundamentales del SGCC consiste en determinar dónde reside el conocimiento oficial del sistema.

Las aplicaciones tradicionales sitúan el conocimiento en una base de datos y consideran la aplicación como el centro del sistema.

Este enfoque genera dependencias tecnológicas, dificulta el versionado y limita la reutilización del conocimiento entre diferentes plataformas.

El SGCC persigue una filosofía distinta: desacoplar completamente el conocimiento de cualquier implementación tecnológica.

---

# Problema

Es necesario establecer cuál será la fuente oficial de verdad del conocimiento culinario.

Las alternativas consideradas incluyen:

- bases de datos relacionales;
- bases de datos documentales;
- aplicaciones web;
- sistemas wiki;
- repositorios Markdown.

La decisión condicionará toda la arquitectura del sistema.

---

# Decisión

Se adopta el repositorio de documentos Markdown versionados mediante Git como **única fuente oficial de verdad** del Sistema de Gestión del Conocimiento Culinario (SGCC).

Todo conocimiento estructural del proyecto deberá residir en documentos Markdown.

Ninguna aplicación, servicio o herramienta será propietaria del conocimiento.

Las aplicaciones actuarán únicamente como consumidoras, editoras o transformadoras del contenido almacenado en el repositorio.

---

# Justificación

Markdown constituye un formato abierto, legible y ampliamente adoptado.

Su utilización proporciona:

- independencia tecnológica;
- versionado completo mediante Git;
- portabilidad;
- longevidad;
- facilidad de automatización;
- interoperabilidad entre herramientas.

La combinación Markdown + Git convierte el conocimiento en un activo independiente de cualquier implementación software.

---

# Principios derivados

Esta decisión establece varios principios fundamentales.

- El conocimiento pertenece al repositorio.
- Markdown constituye la única fuente oficial de verdad.
- Los artefactos generados nunca sustituyen al contenido original.
- Las aplicaciones son intercambiables.
- La arquitectura tiene prioridad sobre la tecnología.
- El conocimiento puede publicarse en múltiples plataformas sin modificarse.

---

# Modelo arquitectónico

```text
                 Markdown Repository
                 (Source of Truth)
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
    Sitio Web      Aplicaciones     Inteligencia Artificial
        │               │                │
        └───────────────┼────────────────┘
                        ▼
               Otros consumidores futuros
```

Toda plataforma consume el mismo conocimiento.

Ninguna plataforma es propietaria de él.

---

# Alternativas consideradas

## Base de datos relacional

Descartada por:

- dependencia tecnológica;
- dificultades de versionado;
- menor portabilidad.

---

## Base de datos documental

Descartada por:

- mantener la dependencia respecto a una tecnología concreta;
- dificultar la evolución independiente del conocimiento.

---

## CMS o Wiki

Descartado por:

- dependencia de la plataforma;
- escasa reutilización;
- dificultades para automatización avanzada.

---

## Formatos propietarios

Descartados por comprometer la independencia y longevidad del conocimiento.

---

# Consecuencias

## Ventajas

- Independencia tecnológica.
- Versionado completo.
- Máxima trazabilidad.
- Portabilidad.
- Reutilización.
- Automatización.
- Preparación para múltiples plataformas.
- Conservación a largo plazo.

---

## Inconvenientes

- Mayor disciplina documental.
- Necesidad de mantener una arquitectura consistente.
- Algunas operaciones requieren procesos adicionales de indexación.

---

# Impacto arquitectónico

Esta decisión desacopla completamente el conocimiento culinario de sus formas de consumo.

Como consecuencia:

- nuevas aplicaciones podrán desarrollarse sin modificar el conocimiento;
- podrán coexistir múltiples consumidores;
- el conocimiento sobrevivirá a la evolución tecnológica;
- cualquier implementación futura deberá respetar el repositorio Markdown como origen oficial.

---

# Principios de implementación

Toda implementación derivada deberá cumplir las siguientes reglas:

- Nunca editar artefactos generados.
- Toda modificación deberá realizarse sobre los documentos Markdown originales.
- La generación de sitios web, índices o bases de datos constituye un proceso derivado.
- La sincronización siempre será unidireccional desde el repositorio hacia los consumidores.

---

# Relación con GitOps

La filosofía adoptada presenta similitudes con GitOps.

En ambos casos:

- Git almacena el estado oficial.
- Los consumidores interpretan dicho estado.
- El repositorio constituye la referencia única.

La diferencia es que, en el SGCC, el estado representa conocimiento y no infraestructura.

---

# Relación con otros ADR

Este ADR desarrolla los principios establecidos en:

- ADR-0001 — Filosofía del Proyecto.
- ADR-0002 — Organización del Repositorio.

Es ampliado posteriormente por:

- ADR-0004 — Front Matter YAML.
- ADR-0006 — Referencias Cruzadas.
- ADR-0012 — Publicación con MkDocs.
- ADR-0018 — Modelo del Conocimiento del SGCC.
- ADR-0019 — Modelo Lógico vs Estructura Física.

---

# Documentación relacionada

Esta decisión se desarrolla en:

- ARQUITECTURA.md
- GOVERNANCE_MODEL.md
- AI_PROTOCOL.md
- TOOLS_FRAMEWORK.md
- AUTOMATION.md
- QUALITY_PIPELINE.md

---

# Estado actual

La decisión continúa plenamente vigente y constituye uno de los pilares tecnológicos del SGCC.

Toda automatización, publicación, integración con Inteligencia Artificial o desarrollo de nuevas plataformas deberá respetar el principio de que el repositorio Markdown constituye la única fuente oficial de verdad del conocimiento.