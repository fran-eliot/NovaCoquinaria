# ADR-0007 - Modelo de Dominio del Sistema de Gestión del Conocimiento Culinario

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Fran Ramírez

---

# Contexto

El proyecto GASTRO no pretende almacenar únicamente recetas, sino representar el conocimiento culinario de forma estructurada.

Para conseguirlo es necesario definir un modelo conceptual estable que permita organizar todos los elementos del sistema y las relaciones existentes entre ellos.

Este modelo deberá ser independiente de cualquier implementación tecnológica.

---

# Problema

Es necesario identificar las entidades principales del sistema y establecer las relaciones entre ellas.

Este modelo servirá como referencia para:

* la organización documental;
* futuras automatizaciones;
* desarrollo de aplicaciones;
* asistentes basados en IA;
* búsquedas y navegación.

---

# Decisión

El conocimiento culinario se organizará mediante entidades claramente diferenciadas.

Cada entidad tendrá una única responsabilidad y podrá relacionarse con otras mediante referencias explícitas.

---

# Modelo conceptual

```text
                     SGCC
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
 Ingrediente      Técnica      Plantilla
        │             │             │
        └──────┬──────┴──────┬──────┘
               ▼             ▼
             Receta       Tabla
               │
               ▼
             Menú (futuro)
```

Las relaciones representan dependencia y reutilización de conocimiento.

---

# Entidades del dominio

## Arquitectura

Documenta el funcionamiento del propio proyecto.

Ejemplos:

* README
* ADR
* Guía de estilo
* Especificación de documentos

---

## Técnica

Describe un procedimiento reutilizable.

Ejemplos:

* Sofrito
* Salteado en wok
* Emulsión
* Blanqueado

---

## Ingrediente

Describe un producto utilizado en cocina.

Ejemplos:

* Miso
* Salsa de soja
* Arroz basmati
* Leche de coco

---

## Plantilla

Representa un patrón general de elaboración.

Ejemplos:

* Curry base
* Guiso base
* Crema base
* Salteado asiático

---

## Tabla

Resume información de consulta rápida.

Ejemplos:

* Tiempos de cocción
* Conversión de unidades
* Conservación

---

## Receta

Combina técnicas, ingredientes, plantillas y tablas para elaborar un plato concreto.

Las recetas no deben contener conocimiento reutilizable que pertenezca a otra entidad.

---

## Nota

Almacena conocimiento temporal, ideas o experimentos.

No forma parte del conocimiento consolidado.

---

## Menú (evolución futura)

Agrupa recetas según un objetivo.

Ejemplos:

* Batch cooking semanal
* Menú vegetariano
* Menú de invierno

---

# Relaciones

Las entidades podrán relacionarse mediante referencias cruzadas.

Relaciones principales:

* depende de;
* utiliza;
* relacionado con;
* sustituye a;
* pertenece a.

Estas relaciones constituyen el grafo de conocimiento del proyecto.

---

# Justificación

Separar el dominio en entidades independientes permite:

* reducir duplicidades;
* facilitar el mantenimiento;
* mejorar la navegación;
* permitir reutilización máxima;
* simplificar futuras aplicaciones.

Cada documento tiene un propósito claro y puede evolucionar de manera independiente.

---

# Alternativas consideradas

## Modelo basado exclusivamente en recetas

**Descartado** por su escasa reutilización y elevada duplicación de información.

---

## Organización por carpetas sin modelo conceptual

**Descartado** porque dificulta la evolución y la automatización del sistema.

---

# Consecuencias

## Ventajas

* Arquitectura modular.
* Modelo estable.
* Escalabilidad.
* Independencia tecnológica.
* Base sólida para futuras aplicaciones.
* Compatibilidad con IA y búsquedas semánticas.

## Inconvenientes

* Mayor esfuerzo de diseño inicial.
* Necesidad de mantener la coherencia entre entidades.

---

# Impacto futuro

Este modelo podrá traducirse directamente a:

* entidades de una base de datos;
* clases de un backend;
* índices de búsqueda;
* grafos de conocimiento;
* APIs REST o GraphQL;
* sistemas RAG para inteligencia artificial.

La documentación se convierte así en el modelo de dominio del sistema.

---

# Dependencias

* [ADR-0001 - Filosofía del Proyecto](./ADR-0001-filosofia-del-proyecto.md)
* [ADR-0002 - Estructura del Repositorio](./ADR-0002-estructura-del-repositorio.md)
* [ADR-0003 - El Repositorio Markdown como Fuente Única de Verdad](./ADR-0003-markdown-como-fuente-de-verdad.md)
* [ADR-0005 - Separación del Conocimiento Culinario](./ADR-0005-separacion-del-conocimiento.md)
* [ADR-0006 - Referencias Cruzadas como Modelo de Navegación](./ADR-0006-referencias-cruzadas.md)

---

# Véase también

* [README](../../README.md)
* [ESPECIFICACION_DE_DOCUMENTOS](../../ESPECIFICACION_DE_DOCUMENTOS.md)
* [GUIA_DE_ESTILO](../../GUIA_DE_ESTILO.md)

---

# Utilizado por

Este ADR constituye el modelo conceptual sobre el que se construye todo el Sistema de Gestión del Conocimiento Culinario (SGCC).
