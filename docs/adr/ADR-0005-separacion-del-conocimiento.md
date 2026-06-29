# ADR-0005 - Separación del Conocimiento Culinario

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Francisco Ramírez Martín

---

# Contexto

La mayoría de los recetarios organizan el contenido alrededor de recetas completas.

Como consecuencia, técnicas, ingredientes y procedimientos aparecen repetidos en numerosos documentos.

Esta duplicidad dificulta:

* la actualización del contenido;
* la reutilización del conocimiento;
* el aprendizaje progresivo;
* la automatización futura.

El proyecto GASTRO pretende organizar el conocimiento culinario como un conjunto de componentes reutilizables.

---

# Problema

Es necesario definir cómo se estructurará el conocimiento culinario para evitar redundancias y facilitar su evolución.

La cuestión principal es decidir si toda la información debe residir en las recetas o si debe dividirse en documentos especializados.

---

# Decisión

El conocimiento culinario se dividirá en documentos con una única responsabilidad.

Las recetas serán únicamente una forma de combinar conocimientos previamente documentados.

Los principales tipos de conocimiento serán:

* Técnicas.
* Ingredientes.
* Plantillas.
* Tablas.
* Recetas.
* Notas.

Cada uno evolucionará de manera independiente.

---

# Modelo conceptual

```text
                    Conocimiento Culinario

                              │

        ┌──────────────┬──────────────┬──────────────┐
        │              │              │              │
        ▼              ▼              ▼              ▼
    Técnicas     Ingredientes    Plantillas      Tablas
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                   Recetas
```

Las recetas reutilizan el conocimiento existente.

No lo duplican.

---

# Responsabilidades

## Técnicas

Explican procedimientos reutilizables.

Ejemplos:

* Sofrito.
* Salteado en wok.
* Emulsiones.

---

## Ingredientes

Describen productos de la despensa.

Ejemplos:

* Miso.
* Mirin.
* Salsa de soja.

---

## Plantillas

Definen patrones generales.

Ejemplos:

* Curry base.
* Guiso base.
* Salteado asiático.

---

## Tablas

Recogen información de consulta rápida.

Ejemplos:

* Tiempos de cocción.
* Temperaturas.
* Sustituciones.

---

## Recetas

Combinan todos los elementos anteriores para obtener una elaboración concreta.

---

# Justificación

Separar el conocimiento permite:

* eliminar duplicidades;
* simplificar el mantenimiento;
* mejorar la reutilización;
* facilitar el aprendizaje;
* favorecer la automatización.

Una mejora en un documento base beneficia automáticamente a todas las recetas que lo utilizan.

---

# Alternativas consideradas

## Documentos monolíticos

Toda la información incluida dentro de cada receta.

**Descartado** por:

* repetición constante;
* mantenimiento complejo;
* inconsistencias.

---

## Wiki sin clasificación

Conocimiento distribuido sin distinguir tipos de documento.

**Descartado** por:

* falta de cohesión;
* crecimiento desordenado;
* dificultad para automatizar.

---

# Consecuencias

## Ventajas

* Arquitectura modular.
* Reutilización máxima.
* Mantenimiento sencillo.
* Menor riesgo de inconsistencias.
* Mejor experiencia de aprendizaje.

## Inconvenientes

* Mayor número de documentos.
* Necesidad de mantener referencias cruzadas.

---

# Impacto futuro

Esta decisión permite representar el repositorio como un **grafo de conocimiento culinario**, donde cada documento constituye un nodo y las referencias entre ellos forman relaciones explícitas.

Este modelo facilitará:

* navegación contextual;
* búsqueda semántica;
* generación automática de documentación;
* asistentes basados en IA;
* motores de recomendación;
* planificación inteligente de menús.

---

# Dependencias

* [ADR-0001 - Filosofía del Proyecto](./ADR-0001-filosofia-del-proyecto.md)
* [ADR-0002 - Estructura del Repositorio](./ADR-0002-estructura-del-repositorio.md)
* [ADR-0003 - El Repositorio Markdown como Fuente Única de Verdad](./ADR-0003-markdown-como-fuente-de-verdad.md)

---

# Véase también

* [README](../../README.md)
* [GUIA_DE_ESTILO](../../GUIA_DE_ESTILO.md)
* [ESPECIFICACION_DE_DOCUMENTOS](../../ESPECIFICACION_DE_DOCUMENTOS.md)

---

# Utilizado por

Este ADR sirve como base conceptual para todos los documentos de técnicas, ingredientes, plantillas y recetas del proyecto.
