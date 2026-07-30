# ADR-0001 — Filosofía del Proyecto GASTRO

**Identificador:** ADR-0001

**Estado:** Aceptado

**Vigencia:** Activa

**Última Revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Arquitectura / Gobernanza

---

# Contexto

Existen multitud de aplicaciones y recetarios para almacenar recetas.

Sin embargo, la mayoría presentan una limitación importante: el conocimiento culinario aparece repetido en numerosas recetas.

Las mismas técnicas, ingredientes, procesos o procedimientos se documentan una y otra vez, dificultando su mantenimiento, evolución y reutilización.

Además, los recetarios tradicionales suelen centrarse en el resultado final, dedicando poca atención a los fundamentos culinarios que permiten comprender y adaptar una receta.

El proyecto nace con la intención de resolver este problema desde una perspectiva arquitectónica.

---

# Problema

Se necesita un sistema capaz de:

- organizar conocimiento culinario de forma estructurada;
- reutilizar información entre múltiples recetas;
- minimizar duplicidades;
- facilitar el mantenimiento y la evolución del conocimiento;
- servir como base para futuras formas de consumo del conocimiento culinario.

---

# Decisión

Se adopta un enfoque basado en un **Sistema de Gestión del Conocimiento Culinario (SGCC)** en lugar de un recetario tradicional.

El conocimiento se organizará mediante documentos especializados, cada uno con una única responsabilidad.

Entre ellos:

- arquitectura;
- técnicas;
- ingredientes;
- procesos;
- plantillas;
- tablas;
- recetas;
- notas.

Las recetas no contendrán explicaciones duplicadas, sino que reutilizarán el conocimiento existente mediante referencias a los documentos correspondientes.

---

# Consecuencias

## Ventajas

- Mayor reutilización del conocimiento.
- Eliminación de duplicidades.
- Mantenimiento más sencillo.
- Mejor escalabilidad.
- Mayor coherencia documental.
- Compatibilidad con automatizaciones.
- Preparación para futuras aplicaciones y herramientas.
- Mejor experiencia de aprendizaje.

---

## Inconvenientes

- Mayor complejidad inicial.
- Requiere planificación arquitectónica.
- Exige mantener referencias cruzadas.
- Obliga a diseñar un modelo documental consistente.

---

# Alternativas consideradas

## Recetario tradicional

Descartado por:

- duplicidad de información;
- difícil mantenimiento;
- escasa reutilización;
- limitada capacidad de evolución.

---

## Wiki sin estructura definida

Descartada por:

- crecimiento desordenado;
- falta de consistencia;
- baja reutilización;
- dificultades para automatizar.

---

# Justificación

El conocimiento culinario presenta una naturaleza modular comparable a la del conocimiento técnico.

Técnicas, ingredientes, procesos y conceptos pueden reutilizarse en múltiples recetas.

Separar estos elementos en documentos especializados permite construir un sistema mantenible, escalable y preparado para evolucionar durante muchos años.

---

# Principios derivados

Esta decisión establece varios principios fundamentales del proyecto:

- El conocimiento tiene prioridad sobre las recetas.
- Cada concepto debe documentarse una única vez.
- La reutilización prevalece sobre la duplicación.
- La organización del conocimiento constituye un objetivo arquitectónico.
- Las recetas representan una aplicación del conocimiento, no su contenedor principal.

Estos principios servirán de base para decisiones arquitectónicas posteriores.

---

# Impacto futuro

Esta decisión desacopla el conocimiento culinario de sus posibles formas de consumo.

Como consecuencia, el SGCC podrá reutilizarse desde diferentes plataformas presentes y futuras, tales como:

- aplicaciones web;
- aplicaciones móviles;
- asistentes inteligentes;
- motores de búsqueda;
- sistemas RAG;
- herramientas de planificación culinaria;
- sistemas de análisis nutricional;
- futuras aplicaciones aún no definidas.

---

# Relación con otros ADR

Este ADR constituye la decisión fundacional del proyecto.

Es ampliado por decisiones posteriores, entre ellas:

- ADR-0003 — Markdown como fuente de verdad.
- ADR-0005 — Separación del conocimiento.
- ADR-0010 — Arquitectura orientada al conocimiento.
- ADR-0015 — Arquitectura basada en reutilización.
- ADR-0018 — Modelo del conocimiento del SGCC.

---

# Documentación relacionada

Esta decisión se desarrolla posteriormente en los siguientes documentos del proyecto:

- VISION.md
- GOVERNANCE_MODEL.md
- ARQUITECTURA.md
- ESPECIFICACION_DE_DOCUMENTOS.md
- ESPECIFICACION_DE_COLECCIONES.md
- KNOWLEDGE_STRATEGY.md

---

# Estado actual

La decisión continúa plenamente vigente y constituye el fundamento arquitectónico sobre el que se construye el Sistema de Gestión del Conocimiento Culinario (SGCC).

Toda evolución futura deberá respetar los principios establecidos en este ADR.