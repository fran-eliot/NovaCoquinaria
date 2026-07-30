---
id: DOC-0020
titulo: Incorporación al Proyecto
tipo: gestion
version: 2.0
estado: estable
ultima_revision: 2026-07-30
---

# PROJECT_ONBOARDING

> **Proyecto:** NovaCoquinaria  
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento define el **proceso oficial de incorporación** al proyecto NovaCoquinaria.

Su finalidad es proporcionar el contexto mínimo necesario para que cualquier colaborador —humano o asistente basado en IA— pueda comenzar a trabajar manteniendo la coherencia del SGCC.

No explica el proyecto en profundidad.

Su función consiste en indicar **qué debe comprenderse antes de realizar cualquier contribución**.

---

# Perfil del colaborador

Toda persona o sistema que participe en el proyecto deberá comprender:

- qué es NovaCoquinaria;
- qué es GASTRO;
- cómo se organiza el conocimiento;
- cómo evoluciona el proyecto;
- cuáles son las normas de gobernanza.

---

# Itinerario recomendado

La incorporación sigue el siguiente recorrido.

```text
README
      │
      ▼
NovaCoquinaria
      │
      ▼
VISION
      │
      ▼
MANIFESTO
      │
      ▼
ARQUITECTURA
      │
      ▼
MODELO_DE_CONOCIMIENTO
      │
      ▼
CONTEXT
      │
      ▼
PROJECT_STATUS
      │
      ▼
PROJECT_ONBOARDING
```

Una vez completado este recorrido, el colaborador dispone del contexto necesario para comenzar a participar en el proyecto.

---

# Conocimientos mínimos

Antes de realizar cualquier cambio deberá comprenderse:

## Identidad

- propósito del proyecto;
- alcance del SGCC;
- papel de GASTRO.

---

## Arquitectura

- diseño general del sistema;
- modelo de conocimiento;
- separación entre modelo lógico y estructura física.

---

## Gobernanza

- workflow de desarrollo;
- proceso de contribución;
- documentación mediante ADR;
- responsabilidades documentales.

---

## Estado del proyecto

Consultar siempre:

- PROJECT_STATUS;
- BITÁCORA;
- ROADMAP.

---

# Antes de contribuir

Todo colaborador deberá revisar:

1. CONTRIBUTING
2. DEVELOPMENT_WORKFLOW

Estos documentos describen cómo debe evolucionar el conocimiento y cómo integrar nuevas contribuciones.

---

# Antes de modificar la arquitectura

Las modificaciones que afecten a:

- arquitectura;
- modelo de conocimiento;
- organización documental;
- estructura del repositorio;

deberán evaluarse previamente mediante una **Architecture Decision Record (ADR)**.

---

# Validaciones

Antes de integrar cambios relevantes deberán ejecutarse las validaciones oficiales del proyecto.

Como mínimo:

- validación documental;
- validación semántica;
- generación del Knowledge Graph;
- comprobación de documentos huérfanos.

Las herramientas concretas se documentan en la documentación operativa correspondiente.

---

# Rol esperado del colaborador

Todo colaborador deberá actuar siguiendo los principios definidos en el MANIFESTO.

En particular deberá priorizar:

- coherencia;
- reutilización;
- simplicidad;
- mantenibilidad;
- evolución sostenible.

La calidad del sistema prevalece sobre la cantidad de documentación incorporada.

---

# Rol esperado del asistente IA

Cuando la colaboración se realice mediante asistentes basados en IA, estos deberán actuar como apoyo arquitectónico del proyecto.

Su responsabilidad consiste en:

- preservar la coherencia del sistema;
- detectar duplicidades;
- proponer mejoras;
- cuestionar incoherencias;
- respetar la arquitectura y el modelo de conocimiento.

El asistente no debe limitarse a ejecutar instrucciones, sino contribuir activamente a mantener la calidad del SGCC.

---

# Checklist de incorporación

Antes de comenzar asegúrate de poder responder afirmativamente a todas estas preguntas.

## Identidad

- ☐ Comprendo qué es NovaCoquinaria.
- ☐ Comprendo qué es GASTRO.

## Arquitectura

- ☐ Comprendo cómo está diseñado el SGCC.
- ☐ Comprendo el modelo de conocimiento.

## Gobernanza

- ☐ Sé cómo contribuir.
- ☐ Conozco el workflow oficial.
- ☐ Sé cuándo es necesaria una ADR.

## Estado

- ☐ Conozco el estado actual del proyecto.
- ☐ Sé dónde consultar la hoja de ruta.

---

# Documentación relacionada

## Identidad

- README
- NovaCoquinaria
- VISION
- MANIFESTO

## Arquitectura

- ARQUITECTURA
- MODELO_DE_CONOCIMIENTO

## Gobernanza

- CONTEXT
- CONTRIBUTING
- DEVELOPMENT_WORKFLOW

## Gestión

- PROJECT_STATUS
- BITÁCORA
- ROADMAP

---

# Conclusión

La incorporación a NovaCoquinaria no consiste únicamente en conocer la estructura del repositorio.

Consiste en comprender la identidad del proyecto, su arquitectura, su modelo de conocimiento y las normas que gobiernan su evolución.

Solo después de adquirir ese contexto un colaborador está preparado para contribuir de forma coherente al crecimiento del SGCC.