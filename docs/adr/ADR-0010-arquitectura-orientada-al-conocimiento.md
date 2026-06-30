# ADR-0010 - Arquitectura Orientada al Conocimiento, la Automatización y la Inteligencia Artificial

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Fran Ramírez

---

# Contexto

El proyecto GASTRO nace como un repositorio Markdown de conocimiento culinario.

Sin embargo, su objetivo no es limitarse a servir como documentación estática, sino convertirse en la base de una plataforma capaz de alimentar múltiples herramientas presentes y futuras.

Entre ellas:

* documentación navegable;
* buscadores;
* aplicaciones móviles;
* asistentes culinarios;
* sistemas de recomendación;
* planificación de menús;
* automatización de tareas;
* inteligencia artificial.

Para conseguirlo, el conocimiento debe organizarse pensando tanto en las personas como en las máquinas.

---

# Problema

Los documentos escritos únicamente para lectura humana presentan limitaciones importantes:

* estructura inconsistente;
* información difícil de indexar;
* baja reutilización;
* escasa capacidad de automatización.

Es necesario definir una arquitectura que permita explotar el conocimiento mediante procesos automáticos sin perder legibilidad.

---

# Decisión

Todo el conocimiento del proyecto se diseñará siguiendo el principio de **doble legibilidad**.

Cada documento deberá ser:

* fácilmente comprensible por una persona;
* fácilmente interpretable por software.

La estructura documental, los metadatos y las relaciones entre documentos deberán favorecer la automatización desde el diseño inicial.

---

# Principios

## El conocimiento es el activo principal

Las aplicaciones son herramientas.

El conocimiento es permanente.

Toda decisión arquitectónica deberá proteger el conocimiento antes que cualquier implementación tecnológica.

---

## Independencia de la presentación

El contenido no dependerá de:

* una página web;
* una aplicación móvil;
* una base de datos;
* un asistente de IA.

Todas estas herramientas consumirán el mismo repositorio.

---

## Modularidad

Cada documento representa una unidad de conocimiento independiente.

La combinación de documentos permite construir recetas, menús, guías o recomendaciones.

---

## Estructura explícita

El contenido deberá estar organizado de forma consistente.

Esto permitirá:

* búsquedas estructuradas;
* navegación contextual;
* generación automática de documentación.

---

## Relaciones explícitas

Las conexiones entre documentos deberán declararse mediante referencias cruzadas.

Estas relaciones constituyen el grafo de conocimiento del proyecto.

---

## Automatización como objetivo

Siempre que sea posible, las tareas repetitivas deberán poder automatizarse.

Ejemplos:

* generación de índices;
* mapas de conocimiento;
* catálogos de ingredientes;
* menús automáticos;
* listas de compra;
* documentación navegable.

---

# Preparación para Inteligencia Artificial

El contenido deberá facilitar su utilización por sistemas basados en IA.

Esto implica:

* documentos pequeños y cohesionados;
* lenguaje claro;
* estructura consistente;
* metadatos normalizados;
* relaciones explícitas;
* ausencia de duplicidades.

Estas características favorecen técnicas como Retrieval-Augmented Generation (RAG), búsqueda semántica y razonamiento basado en conocimiento.

---

# Casos de uso futuros

La arquitectura permitirá desarrollar, entre otros:

## Aplicación móvil

Consulta y gestión de recetas.

---

## Sitio web

Documentación navegable.

---

## Motor de búsqueda

Búsquedas por:

* ingredientes;
* técnicas;
* categorías;
* etiquetas.

---

## Planificador de menús

Generación automática de menús según distintos criterios.

---

## Lista inteligente de la compra

Obtención automática de ingredientes a partir de uno o varios menús.

---

## Asistente culinario

Respuesta a preguntas utilizando exclusivamente el conocimiento del repositorio.

---

## Sistema RAG

Consulta inteligente del repositorio mediante modelos de lenguaje.

---

## Agentes especializados

Futuros agentes podrán:

* adaptar recetas;
* proponer sustituciones;
* planificar batch cooking;
* optimizar la despensa;
* generar variantes;
* responder preguntas culinarias fundamentadas en el conocimiento del proyecto.

---

# Justificación

Diseñar el conocimiento pensando desde el inicio en su reutilización reduce el esfuerzo necesario para desarrollar nuevas herramientas.

La calidad de las aplicaciones dependerá directamente de la calidad del conocimiento.

---

# Alternativas consideradas

## Diseñar únicamente para lectura humana

**Descartado**.

Limita considerablemente la reutilización y la automatización.

---

## Diseñar únicamente para software

**Descartado**.

Reduce la legibilidad y dificulta el mantenimiento manual.

---

# Consecuencias

## Ventajas

* Arquitectura preparada para el futuro.
* Mayor reutilización.
* Compatibilidad con IA.
* Automatización sencilla.
* Independencia tecnológica.
* Escalabilidad.

## Inconvenientes

* Mayor disciplina documental.
* Necesidad de mantener estructuras homogéneas.

---

# Impacto futuro

Esta decisión convierte el repositorio en una base de conocimiento preparada para evolucionar hacia un ecosistema completo de herramientas culinarias.

Las futuras aplicaciones no almacenarán el conocimiento; simplemente lo interpretarán y lo presentarán de diferentes maneras.

---

# Dependencias

* [ADR-0001 - Filosofía del Proyecto](./ADR-0001-filosofia-del-proyecto.md)
* [ADR-0003 - El Repositorio Markdown como Fuente Única de Verdad](./ADR-0003-markdown-como-fuente-de-verdad.md)
* [ADR-0004 - Front Matter YAML como Metadatos Canónicos](./ADR-0004-front-matter-yaml.md)
* [ADR-0005 - Separación del Conocimiento Culinario](./ADR-0005-separacion-del-conocimiento.md)
* [ADR-0006 - Referencias Cruzadas como Modelo de Navegación](./ADR-0006-referencias-cruzadas.md)
* [ADR-0007 - Modelo de Dominio del Sistema de Gestión del Conocimiento Culinario](./ADR-0007-modelo-de-dominio-del-sgcc.md)
* [ADR-0008 - Identificadores Únicos y Estables](./ADR-0008-identificadores-unicos.md)
* [ADR-0009 - Ciclo de Vida y Versionado del Conocimiento](./ADR-0009-ciclo-de-vida-y-versionado.md)

---

# Véase también

* [README](../../README.md)
* [GUIA_DE_ESTILO](../../GUIA_DE_ESTILO.md)
* [ESPECIFICACION_DE_DOCUMENTOS](../../ESPECIFICACION_DE_DOCUMENTOS.md)
* [CHANGELOG](../../CHANGELOG.md)

---

# Utilizado por

Este ADR establece los principios que deberán seguir todas las futuras herramientas construidas sobre el Sistema de Gestión del Conocimiento Culinario (SGCC).
