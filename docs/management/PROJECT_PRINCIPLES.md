---
id: DOC-0012
titulo: Principios Vigentes
tipo: arquitectura
version: 2.0
estado: estable
ultima_revision: 2026-07-20
---

# Principios Vigentes

> **Proyecto:** NovaCoquinaria
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento reúne los principios actualmente vigentes que gobiernan NovaCoquinaria.

No sustituye a los Architecture Decision Records (ADR).

Los ADR documentan el contexto, las alternativas y la justificación de cada decisión.

Este documento recoge únicamente el resultado consolidado de dichas decisiones.

Debe responder a una única pregunta.

> **¿Qué principios gobiernan hoy el SGCC?**

---

# Naturaleza del documento

Los principios aquí descritos se consideran vigentes hasta que una nueva Architecture Decision Record los modifique expresamente.

Cuando exista conflicto entre este documento y un ADR aprobado posteriormente, prevalecerá siempre el ADR.

---

# Principios fundamentales

## El conocimiento es el activo principal

NovaCoquinaria es un Sistema de Gestión del Conocimiento Culinario.

Las recetas constituyen aplicaciones del conocimiento, no el conocimiento en sí mismo.

---

## El conocimiento se documenta una única vez

Todo conocimiento reutilizable debe poseer una representación única.

La reutilización tiene prioridad sobre la duplicación.

---

## Las relaciones son conocimiento

Las relaciones entre entidades forman parte del conocimiento del sistema.

El Knowledge Graph constituye una representación lógica de dichas relaciones.

---

## La arquitectura sirve al conocimiento

La arquitectura existe para facilitar la evolución del conocimiento.

Nunca debe convertirse en un fin en sí misma.

---

# Principios arquitectónicos

## Organización lógica

La organización conceptual prevalece sobre la estructura física del repositorio.

---

## Responsabilidad única

Cada documento posee una única responsabilidad claramente definida.

---

## Modularidad

El conocimiento evoluciona mediante entidades independientes y reutilizables.

---

## Evolución incremental

La arquitectura únicamente evoluciona cuando una necesidad real lo justifica.

---

# Principios documentales

Se mantiene como fuente oficial de verdad:

- Markdown.

Se consideran derivados:

- site_docs;
- MkDocs;
- documentación publicada.

Toda publicación es un artefacto generado.

---

# Principios de calidad

El proyecto mantiene como criterios permanentes:

- validación automática;
- validación arquitectónica;
- detección de deuda;
- detección de duplicidades;
- control semántico.

---

# Principios de desarrollo

Toda evolución del SGCC deberá priorizar:

1. Coherencia.
2. Reutilización.
3. Simplicidad.
4. Mantenibilidad.
5. Automatización.
6. Nuevas capacidades.

---

# Principios de gobernanza

Toda evolución deberá:

- preservar la arquitectura;
- mantener la coherencia;
- respetar el modelo de conocimiento;
- documentar decisiones relevantes mediante ADR.

---

# Principios permanentes

Las siguientes afirmaciones resumen la filosofía completa del proyecto.

> El conocimiento precede a las recetas.

> Documentar una vez. Reutilizar siempre.

> La arquitectura sirve al conocimiento.

> La calidad precede a la cantidad.

> Cada entidad posee una única responsabilidad.

---

# Evolución

Este documento evoluciona únicamente cuando cambia alguno de los principios anteriores.

Las modificaciones deberán estar respaldadas por una Architecture Decision Record.

---

# Relaciones

| Documento | Responsabilidad |
|-----------|-----------------|
| ADR | Registro de decisiones |
| DECISIONS_SUMMARY | Principios vigentes |
| ARQUITECTURA | Diseño del SGCC |
| MODELO_DE_CONOCIMIENTO | Modelo conceptual |
| CONTRIBUTING | Normas de contribución |

---

# Conclusión

Los Architecture Decision Records explican cómo y por qué se tomaron las decisiones.

Este documento conserva únicamente aquellas que continúan definiendo la identidad arquitectónica y metodológica de NovaCoquinaria.

Constituye la referencia ejecutiva de los principios que gobiernan actualmente el SGCC.