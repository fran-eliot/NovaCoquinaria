# ADR-0003 - El Repositorio Markdown como Fuente Única de Verdad

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Francisco Ramírez Martín

---

# Contexto

La mayoría de las aplicaciones de recetas almacenan el conocimiento en una base de datos.

El contenido se edita mediante formularios y la aplicación constituye el centro del sistema.

Este enfoque presenta varios inconvenientes:

* dependencia de una tecnología concreta;
* dificultad para versionar el conocimiento;
* escasa portabilidad;
* complejidad para reutilizar la información en otros sistemas.

El proyecto GASTRO pretende construir un sistema de gestión del conocimiento culinario independiente de cualquier tecnología concreta.

---

# Problema

Es necesario definir cuál será la fuente oficial del conocimiento.

Las posibles alternativas son:

* Base de datos relacional.
* Base de datos documental.
* Aplicación web.
* Sistema wiki.
* Repositorio Markdown.

La decisión condicionará toda la arquitectura futura.

---

# Decisión

El repositorio de archivos Markdown será la **única fuente de verdad** del conocimiento culinario.

Toda la información relevante del proyecto deberá residir en documentos Markdown versionados.

Ninguna aplicación futura será propietaria de los datos.

Las aplicaciones actuarán únicamente como consumidoras o editoras del repositorio.

---

# Principios derivados

Esta decisión implica que:

* el conocimiento pertenece al repositorio;
* las aplicaciones son intercambiables;
* la información nunca dependerá de una base de datos específica;
* cualquier herramienta podrá reconstruirse a partir del contenido Markdown.

---

# Arquitectura

```text
                   Repositorio Markdown
                   (Fuente de Verdad)
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   Sitio Web          Aplicación        Asistente IA
                        móvil
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                 Otros servicios futuros
```

Todos los sistemas obtienen la información del mismo origen.

---

# Justificación

Markdown presenta numerosas ventajas:

## Independencia tecnológica

Los documentos pueden abrirse con cualquier editor.

No dependen de una aplicación concreta.

---

## Longevidad

Markdown es un formato ampliamente adoptado y con altas probabilidades de mantenerse durante décadas.

---

## Versionado

Git permite conocer:

* quién modificó un documento;
* cuándo;
* qué cambió;
* por qué cambió.

---

## Portabilidad

Todo el repositorio puede copiarse, sincronizarse o respaldarse sin necesidad de exportaciones complejas.

---

## Legibilidad

Los documentos son fácilmente comprensibles tanto para personas como para herramientas informáticas.

---

## Automatización

A partir del repositorio podrán generarse automáticamente:

* páginas web;
* aplicaciones móviles;
* documentación navegable;
* motores de búsqueda;
* listas de compra;
* planes de menú;
* asistentes basados en inteligencia artificial.

---

# Alternativas consideradas

## Base de datos relacional

**Descartada**

Ventajas:

* consultas rápidas;
* integridad referencial.

Inconvenientes:

* difícil versionado;
* dependencia tecnológica;
* menor portabilidad.

---

## CMS o Wiki

**Descartado**

Ventajas:

* edición sencilla.

Inconvenientes:

* escasa reutilización;
* dependencia de la plataforma;
* dificultades para automatización avanzada.

---

## Archivos propietarios

**Descartados**

El conocimiento no debe depender de formatos cerrados.

---

# Consecuencias

## Ventajas

* Independencia tecnológica.
* Versionado mediante Git.
* Mayor durabilidad del conocimiento.
* Compatibilidad con múltiples herramientas.
* Facilidad para automatización.
* Sencillez para realizar copias de seguridad.
* Posibilidad de trabajar sin conexión.

---

## Inconvenientes

* Requiere mayor disciplina documental.
* Necesidad de mantener una estructura consistente.
* Algunas consultas complejas requerirán procesos de indexación.

---

# Impacto futuro

Esta decisión permite que el repositorio evolucione hacia una plataforma completa sin modificar el contenido existente.

El mismo repositorio podrá alimentar:

* un sitio web estático;
* una aplicación móvil;
* un buscador semántico;
* un sistema RAG para inteligencia artificial;
* un planificador de menús;
* un generador automático de listas de la compra;
* un sistema de análisis nutricional;
* futuras herramientas que todavía no existen.

El conocimiento permanecerá independiente de cualquier implementación tecnológica.

---

# Relación con GitOps

La filosofía adoptada es similar a la utilizada en arquitecturas GitOps.

En ambos casos:

* Git almacena el estado deseado del sistema.
* Los consumidores interpretan dicho estado.
* El repositorio constituye la referencia oficial.

En GASTRO, el estado deseado no es una infraestructura, sino el conocimiento culinario.

---

# Referencias

- [ADR-0001 - Filosofía del Proyecto](./ADR-0001-filosofia-del-proyecto.md)
- [ADR-0002 - Estructura del Repositorio](./ADR-0002-estructura-del-repositorio.md)
- [README](../../README.md)
- [ESPECIFICACION_DE_DOCUMENTOS](../../ESPECIFICACION_DE_DOCUMENTOS.md)
