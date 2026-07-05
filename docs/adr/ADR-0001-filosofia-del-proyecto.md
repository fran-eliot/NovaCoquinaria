# ADR-0001 - Filosofía del Proyecto GASTRO

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Fran Ramírez

---

# Contexto

Existen multitud de aplicaciones y recetarios para almacenar recetas.

Sin embargo, la mayoría presentan una limitación importante: el conocimiento se encuentra duplicado.

Las mismas técnicas, ingredientes o procedimientos aparecen repetidos en numerosas recetas, dificultando su mantenimiento y evolución.

Además, los recetarios tradicionales suelen centrarse en el resultado final, sin explicar suficientemente los fundamentos culinarios.

---

# Problema

Se necesita un sistema que permita:

* organizar el conocimiento culinario;
* reutilizar información;
* evitar duplicidades;
* evolucionar con el tiempo;
* servir como base para futuras herramientas software.

---

# Decisión

El proyecto GASTRO se diseñará como un **Sistema de Gestión del Conocimiento Culinario (SGCC)** y no como un simple recetario.

El conocimiento se organizará mediante documentos especializados:

* arquitectura;
* técnicas;
* ingredientes;
* plantillas;
* tablas;
* recetas;
* notas.

Cada documento tendrá una única responsabilidad.

Las recetas reutilizarán el conocimiento existente mediante referencias, evitando copiar explicaciones.

---

# Consecuencias

## Ventajas

* Mayor reutilización.
* Menor duplicidad.
* Mantenimiento más sencillo.
* Escalabilidad.
* Compatibilidad con automatizaciones.
* Integración sencilla con aplicaciones futuras.
* Mejor experiencia de aprendizaje.

## Inconvenientes

* Mayor complejidad inicial.
* Requiere planificación.
* Exige mantener referencias cruzadas.

---

# Alternativas consideradas

## Recetario tradicional

Descartado por:

* duplicidad de información;
* difícil mantenimiento;
* escasa reutilización.

---

## Wiki sin estructura

Descartada por:

* falta de consistencia;
* crecimiento desordenado;
* dificultades para automatizar.

---

# Justificación

El conocimiento culinario posee una estructura modular similar a la del conocimiento técnico.

Las técnicas, ingredientes y procedimientos pueden reutilizarse en múltiples recetas.

Separar estos conceptos mejora la mantenibilidad del repositorio y facilita su evolución.

---

# Impacto futuro

Esta decisión permitirá utilizar el repositorio como fuente de datos para:

* aplicaciones móviles;
* sitios web;
* motores de búsqueda;
* asistentes culinarios basados en IA;
* planificadores de menús;
* generadores de listas de la compra;
* herramientas de análisis nutricional.

---

# Estado

Esta decisión se considera estructural y servirá como base para el resto de ADR del proyecto.
