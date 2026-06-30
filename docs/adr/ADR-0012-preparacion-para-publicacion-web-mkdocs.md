# ADR-0012 - Preparación para Publicación Web con MkDocs

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Fran Ramírez 

---

# Contexto

NovaCoquinaria nace como un repositorio Markdown privado, pero está diseñado para poder evolucionar hacia una documentación navegable, una web pública o una aplicación.

Los documentos actuales ya utilizan Markdown, referencias relativas, Front Matter YAML y una estructura modular.

---

# Problema

Si el repositorio no se diseña pensando en una futura publicación web, podrían aparecer problemas como:

* rutas inconsistentes;
* documentos difíciles de indexar;
* navegación poco clara;
* estructura poco compatible con generadores estáticos;
* necesidad de reorganizar el contenido más adelante.

---

# Decisión

El repositorio se mantendrá compatible con una futura publicación mediante **MkDocs**, preferentemente con el tema **Material for MkDocs**.

No se implementará obligatoriamente desde el inicio, pero todos los documentos deberán escribirse de forma compatible con una futura generación automática de sitio web.

---

# Principios

## Markdown estándar

Los documentos deberán usar Markdown claro y portable.

---

## Enlaces relativos

Las referencias internas deberán utilizar enlaces relativos navegables.

---

## Estructura estable

La organización de carpetas deberá mantenerse coherente para facilitar la navegación.

---

## Separación entre contenido y presentación

El contenido no dependerá de MkDocs.

MkDocs será únicamente una capa de presentación.

---

# Justificación

MkDocs permite convertir un repositorio Markdown en una web navegable con poco esfuerzo.

Es adecuado para:

* documentación técnica;
* bases de conocimiento;
* manuales;
* proyectos personales;
* documentación versionada.

---

# Alternativas consideradas

## GitHub Wiki

**Descartada** por separar la documentación del repositorio principal.

---

## Docusaurus

**Posible alternativa futura**, pero más orientada a proyectos con React y documentación web avanzada.

---

## Jekyll

**Posible alternativa**, aunque menos flexible para este caso concreto.

---

# Consecuencias

## Ventajas

* Publicación sencilla en GitHub Pages.
* Documentación navegable.
* Buena experiencia de lectura.
* Compatibilidad con búsqueda.
* Preparación para exposición pública del proyecto.

## Inconvenientes

* Puede requerir configuración adicional.
* Algunas funciones avanzadas dependerán de plugins.

---

# Impacto futuro

Esta decisión permitirá publicar NovaCoquinaria como:

* web privada;
* documentación pública;
* manual culinario navegable;
* base para una futura aplicación;
* portfolio técnico.

---

# Dependencias

* [ADR-0003 - El Repositorio Markdown como Fuente Única de Verdad](./ADR-0003-markdown-como-fuente-de-verdad.md)
* [ADR-0004 - Front Matter YAML como Metadatos Canónicos](./ADR-0004-front-matter-yaml.md)
* [ADR-0006 - Referencias Cruzadas como Modelo de Navegación](./ADR-0006-referencias-cruzadas.md)
* [ADR-0010 - Arquitectura Orientada al Conocimiento, la Automatización y la Inteligencia Artificial](./ADR-0010-arquitectura-orientada-al-conocimiento.md)

---

# Véase también

* [README](../../README.md)
* [ARQUITECTURA](../ARQUITECTURA.md)
* [GUIA_DE_ESTILO](../../GUIA_DE_ESTILO.md)

---

# Utilizado por

Este ADR orientará la redacción y organización de todos los documentos para garantizar compatibilidad futura con publicación web.
