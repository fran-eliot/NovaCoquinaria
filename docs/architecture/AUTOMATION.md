---
id: ARC-0015
tipo: arquitectura
titulo: Automatización del SGCC
version: 2.0
estado: estable
ultima_revision: 2026-07-20
---

# Automatización del SGCC

> **Proyecto:** NovaCoquinaria
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento define el papel de la automatización dentro de la arquitectura de NovaCoquinaria.

La automatización constituye una capacidad transversal cuya finalidad es preservar la calidad, coherencia y mantenibilidad del Sistema de Gestión del Conocimiento Culinario.

No genera conocimiento culinario.

No sustituye la revisión humana.

No modifica la fuente oficial de verdad.

---

# Papel de la automatización

Dentro del SGCC, la automatización actúa como mecanismo de apoyo a la arquitectura.

Su responsabilidad consiste en:

- validar;
- detectar inconsistencias;
- generar artefactos derivados;
- facilitar la publicación;
- reducir tareas repetitivas.

Nunca sustituye el criterio editorial.

---

# Principios

Toda automatización del proyecto deberá respetar los siguientes principios.

## La fuente de verdad permanece inalterada

Markdown constituye la única fuente oficial del conocimiento.

La automatización nunca modifica directamente dicho conocimiento.

---

## La automatización protege el conocimiento

Las herramientas existen para preservar la coherencia del sistema.

Nunca deben alterar su significado.

---

## Los artefactos son derivados

Todo contenido generado automáticamente constituye un artefacto derivado.

Ejemplos:

- site_docs;
- índices;
- estadísticas;
- documentación publicada.

---

## Automatizar únicamente aquello que aporta valor

La automatización deberá eliminar tareas repetitivas, pero nunca introducir complejidad innecesaria.

---

## Transparencia

Toda automatización deberá ser:

- comprensible;
- auditable;
- reproducible;
- mantenible.

---

# Alcance

Actualmente la automatización cubre las siguientes áreas.

## Calidad documental

- validación estructural;
- validación documental;
- control de referencias.

---

## Generación

- documentación publicada;
- estadísticas;
- índices.

---

## Infraestructura

- preparación de publicación;
- procesos auxiliares.

---

# Fuera del alcance

La automatización no incorpora conocimiento culinario.

Quedan expresamente fuera de su responsabilidad:

- creación de recetas;
- modificación automática de documentación;
- toma de decisiones editoriales;
- sustitución del criterio humano;
- generación automática de conocimiento.

---

# Evolución prevista

La automatización evolucionará acompañando al crecimiento del SGCC.

Su desarrollo seguirá esta progresión.

```text
Validación

↓

Generación

↓

Análisis

↓

Automatización semántica

↓

Asistencia inteligente
```

Cada nueva capacidad deberá respetar siempre los principios definidos en este documento.

---

# Relación con la arquitectura

La automatización constituye una capacidad transversal.

```text
Markdown

↓

Automatización

↓

Calidad

↓

Publicación
```

Su finalidad consiste en proteger la arquitectura documental y facilitar su evolución.

---

# Relaciones documentales

| Documento | Responsabilidad |
|-----------|-----------------|
| QUALITY_PIPELINE | Flujo de validación |
| TOOLS_FRAMEWORK | Arquitectura técnica |
| QUALITY | Modelo de calidad |
| ARQUITECTURA | Arquitectura del SGCC |

---

# Documentación relacionada

## Arquitectura

- ARQUITECTURA
- QUALITY
- QUALITY_PIPELINE
- TOOLS_FRAMEWORK

## ADR

- ADR-0003 · Markdown como fuente de verdad
- ADR-0012 · Preparación para publicación web MkDocs
- ADR-0014 · Gestión del conocimiento

---

# Conclusión

La automatización constituye una capacidad de infraestructura del SGCC.

Su misión no consiste en producir conocimiento, sino en preservar su calidad, facilitar su evolución y garantizar que el crecimiento del proyecto continúe siendo sostenible.

Toda automatización deberá estar siempre al servicio de la arquitectura y del conocimiento, nunca al contrario.