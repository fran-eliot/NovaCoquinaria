# ARQUITECTURA

> **Proyecto:** NovaCoquinaria
> **Sistema:** GASTRO - Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento ofrece una visión global de la arquitectura del proyecto.

Su finalidad es explicar cómo se organiza el conocimiento culinario, cuáles son sus componentes principales y cómo interactúan entre sí.

No sustituye a los ADR ni a la documentación técnica, sino que proporciona una visión de conjunto del sistema.

---

# Visión General

NovaCoquinaria se concibe como un **Sistema de Gestión del Conocimiento Culinario (SGCC)**.

El conocimiento culinario constituye el núcleo del sistema.

Todas las aplicaciones presentes o futuras consumirán dicho conocimiento, pero ninguna será propietaria de él.

El repositorio Markdown constituye la única fuente de verdad.

---

# Principios Arquitectónicos

La arquitectura del sistema se basa en los siguientes principios:

* El conocimiento es el activo principal.
* Markdown es la fuente única de verdad.
* Cada documento tiene una única responsabilidad.
* El conocimiento debe ser modular.
* Evitar duplicidades.
* Favorecer la reutilización.
* Diseñar pensando tanto en personas como en software.
* Preparar el sistema para automatización e inteligencia artificial.

---

# Arquitectura General

```text
                         NovaCoquinaria

                               │

                 Sistema de Gestión del Conocimiento

                               │

                   Repositorio Markdown (Git)

                               │

      ┌───────────────┬───────────────┬───────────────┐
      │               │               │
      ▼               ▼               ▼
Documentación      Conocimiento    Automatización

      │               │               │
      ▼               ▼               ▼

 README          Técnicas         Scripts
 ADR             Ingredientes     IA
 Guías           Plantillas       Web
                 Recetas          App móvil
                 Tablas           APIs futuras
```

---

# Organización del Repositorio

La organización responde a criterios de conocimiento y no únicamente de clasificación culinaria.

```text
00_Bases/
01_Arroces/
02_Pastas/
03_Legumbres/
04_Verduras/
05_Carnes/
06_Pescados_y_Mariscos/
07_Cocina_Asiatica/
08_Postres/
09_Bebidas/
10_Horno/
11_Despensa/
12_Plantillas/
98_Tablas/
99_Notas/
```

Cada directorio representa un dominio concreto dentro del sistema.

---

# Modelo del Conocimiento

El conocimiento se organiza mediante entidades especializadas.

```text
                 Conocimiento

                      │

      ┌───────────────┼───────────────┐
      │               │               │
      ▼               ▼               ▼

 Ingredientes     Técnicas      Plantillas

      │               │               │
      └───────────────┼───────────────┘

                      ▼

                  Recetas

                      ▼

                    Menús
                 (Evolución futura)
```

Las relaciones entre entidades forman un grafo de conocimiento.

---

# Capas del Sistema

## Capa de Arquitectura

Define las normas del proyecto.

Ejemplos:

* README
* ADR
* Guía de estilo
* Especificación de documentos

---

## Capa de Conocimiento

Contiene la información culinaria reutilizable.

Incluye:

* técnicas;
* ingredientes;
* tablas;
* plantillas.

---

## Capa de Implementación

Representa la aplicación práctica del conocimiento.

Actualmente:

* recetas.

En el futuro:

* menús;
* planificación;
* batch cooking.

---

## Capa de Consumo

Incluye todas las herramientas que utilizan el conocimiento.

Ejemplos:

* sitio web;
* aplicación móvil;
* buscador;
* inteligencia artificial;
* sistemas RAG;
* agentes especializados.

---

# Flujo del Conocimiento

Todo nuevo conocimiento sigue el siguiente recorrido.

```text
Idea

↓

Investigación

↓

Clasificación

↓

Documento Base

↓

Referencias

↓

Recetas

↓

Reutilización

↓

Mejora continua
```

---

# Referencias Cruzadas

Las referencias entre documentos constituyen una parte esencial del sistema.

Permiten:

* navegación;
* reutilización;
* análisis de dependencias;
* construcción del grafo de conocimiento.

---

# Metadatos

Todos los documentos incluyen un bloque Front Matter YAML.

Los metadatos permiten:

* clasificación;
* búsqueda;
* automatización;
* integración con futuras aplicaciones.

---

# Evolución del Sistema

La arquitectura está diseñada para crecer de forma incremental.

La incorporación de nuevos documentos no requiere modificar la estructura existente.

Las futuras aplicaciones deberán adaptarse al conocimiento y no al contrario.

---

# Arquitectura Objetivo

A largo plazo, NovaCoquinaria podrá representarse como un ecosistema de servicios construidos sobre una única base de conocimiento.

```text
                Base de Conocimiento

                        │

      ┌────────┬────────┼────────┬────────┐
      │        │        │        │        │

     Web     Móvil     IA     Buscador   API

      │        │        │        │        │

      └────────┴────────┴────────┴────────┘

             Repositorio Markdown
```

---

# Documentación Relacionada

## Documentos fundamentales

* README.md
* GUIA_DE_ESTILO.md
* ESPECIFICACION_DE_DOCUMENTOS.md
* CONTRIBUTING.md
* CHANGELOG.md

## Decisiones de arquitectura

Consultar la carpeta `docs/adr/` para conocer las decisiones arquitectónicas adoptadas durante el diseño del sistema.

---

# Conclusión

NovaCoquinaria no es un recetario tradicional.

Es una plataforma de conocimiento culinario diseñada para evolucionar durante años, reutilizar información de forma eficiente y servir como base para futuras aplicaciones, automatizaciones e inteligencia artificial.

La arquitectura prioriza el conocimiento sobre la tecnología, garantizando que el contenido permanezca independiente de las herramientas que lo consuman.
