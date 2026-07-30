---
id: ARC-0019
tipo: arquitectura
titulo: Modelo de Calidad del SGCC
version: 2.0
estado: estable
ultima_revision: 2026-07-20
---

# Modelo de Calidad del SGCC

> Proyecto: NovaCoquinaria
> Sistema: GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento define el modelo de calidad utilizado por el Sistema de Gestión del Conocimiento Culinario (SGCC).

Su finalidad consiste en establecer los principios y criterios que permiten evaluar la calidad del conocimiento almacenado en NovaCoquinaria.

La calidad constituye un principio transversal que afecta a toda la arquitectura del sistema.

---

# Alcance

Este documento define:

- qué significa calidad dentro del SGCC;
- las distintas dimensiones de la calidad;
- los criterios generales de aceptación;
- la relación entre calidad, automatización y evolución.

No describe los mecanismos concretos de validación.

Estos pertenecen al Pipeline de Calidad.

---

# Filosofía

La calidad no consiste en cumplir una lista de comprobación.

La calidad consiste en facilitar que el conocimiento sea:

- correcto;
- reutilizable;
- coherente;
- mantenible;
- comprensible;
- evolutivo.

Cada documento debe fortalecer el ecosistema de conocimiento del SGCC.

---

# Dimensiones de la calidad

La calidad del SGCC se evalúa desde distintas perspectivas complementarias.

## Calidad estructural

Evalúa la conformidad con el modelo documental.

Ejemplos:

- estructura correcta;
- Front Matter válido;
- identificadores únicos;
- relaciones coherentes.

---

## Calidad editorial

Evalúa la forma en que el conocimiento se expresa.

Incluye aspectos como:

- claridad;
- precisión;
- terminología uniforme;
- ausencia de ambigüedades.

---

## Calidad arquitectónica

Evalúa la integración del conocimiento dentro del sistema.

Ejemplos:

- responsabilidad única;
- ausencia de duplicidades;
- reutilización;
- coherencia con la arquitectura.

---

## Calidad del conocimiento

Evalúa el propio contenido.

Aspectos principales:

- utilidad;
- exactitud;
- profundidad adecuada;
- explicaciones suficientes;
- actualidad.

---

## Calidad de integración

Evalúa cómo se relaciona un documento con el resto del SGCC.

Ejemplos:

- referencias cruzadas;
- conectividad;
- reutilización efectiva;
- ausencia de documentos huérfanos.

---

# Principios de calidad

Todo conocimiento incorporado al SGCC deberá respetar los siguientes principios.

- Responsabilidad única.
- Una única fuente para cada conocimiento.
- Reutilización antes que repetición.
- Evolución incremental.
- Coherencia terminológica.
- Trazabilidad.
- Comprensión antes que complejidad.

---

# Evaluación de calidad

La evaluación combina distintos mecanismos.

## Validación automática

Comprueba aspectos objetivos.

Ejemplos:

- enlaces;
- metadatos;
- identificadores;
- estructura;
- consistencia documental.

---

## Revisión arquitectónica

Comprueba:

- duplicidades;
- organización;
- relaciones;
- integración.

---

## Revisión editorial

Comprueba:

- claridad;
- precisión;
- legibilidad;
- coherencia narrativa.

---

## Revisión funcional

Comprueba que el conocimiento resulte realmente útil.

---

# Criterios de aceptación

Un activo de conocimiento puede considerarse integrado cuando:

- cumple el modelo documental;
- respeta la guía editorial;
- se integra en la arquitectura;
- aporta valor al SGCC;
- puede reutilizarse desde otros documentos.

---

# Calidad y automatización

La automatización facilita la calidad.

No la sustituye.

Las herramientas permiten detectar errores.

La calidad sigue siendo una responsabilidad compartida entre la arquitectura, la documentación y las revisiones humanas.

---

# Evolución

La calidad del SGCC evoluciona junto con el conocimiento.

Los criterios podrán ampliarse conforme aparezcan nuevas necesidades metodológicas, manteniendo siempre la estabilidad del modelo.

---

# Relación con otros documentos

| Documento | Responsabilidad |
|-----------|-----------------|
| ESPECIFICACION_DE_DOCUMENTOS | Modelo documental |
| GUIA_DE_ESTILO | Calidad editorial |
| AUTOMATION | Estrategia de automatización |
| QUALITY_PIPELINE | Validación y publicación |
| TOOLS_FRAMEWORK | Implementación técnica |

---

# Conclusión

La calidad constituye una propiedad emergente del SGCC.

No depende únicamente de la corrección de un documento individual, sino de la coherencia del conjunto del conocimiento, de su capacidad de reutilización y de su integración dentro de la arquitectura general del sistema.

El objetivo final no consiste en producir documentos perfectos, sino en construir un sistema de conocimiento cada vez más sólido, coherente y útil.
