# ADR-0011 - Separación entre Marca, Producto, Sistema y Repositorio

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Fran Ramírez
---

# Contexto

El proyecto ha evolucionado desde la idea inicial de un repositorio de recetas hasta convertirse en una plataforma orientada a la gestión del conocimiento culinario.

Durante esta evolución han aparecido distintos nombres para referirse al proyecto:

* NovaCoquinaria
* GASTRO
* SGCC

Cada uno representa un concepto diferente y conviene definir claramente su función para evitar ambigüedades en la documentación y en el desarrollo futuro.

---

# Problema

Utilizar indistintamente los nombres del proyecto puede generar confusión entre:

* la marca visible para el usuario;
* el producto desarrollado;
* la arquitectura conceptual;
* el repositorio técnico.

Es necesario establecer una terminología única y consistente.

---

# Decisión

Se diferenciarán claramente cuatro niveles:

## Marca

**NovaCoquinaria**

Es la identidad pública del proyecto.

Será el nombre utilizado en:

* la web;
* la aplicación móvil;
* la documentación pública;
* las presentaciones;
* el material gráfico;
* la comunicación del proyecto.

La marca podrá evolucionar sin afectar a la arquitectura interna.

---

## Producto

**NovaCoquinaria**

El producto es el ecosistema de herramientas construido sobre la base de conocimiento.

En el futuro podrá incluir:

* aplicación web;
* aplicación móvil;
* asistente culinario;
* buscador;
* planificador de menús;
* gestor de despensa;
* API pública.

---

## Sistema

**GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)**

Constituye el núcleo conceptual del proyecto.

Es el conjunto de principios, documentos, relaciones y modelos que organizan el conocimiento culinario.

El sistema es independiente de cualquier interfaz o tecnología concreta.

---

## Repositorio

**NovaCoquinaria (GitHub)**

El repositorio contiene la implementación documental del sistema.

Incluye:

* documentos Markdown;
* arquitectura;
* ADR;
* recetas;
* técnicas;
* ingredientes;
* plantillas;
* tablas;
* scripts futuros.

El repositorio es la implementación física del SGCC.

---

# Relación entre los conceptos

```text
                    NovaCoquinaria
                         (Marca)
                              │
                              ▼
                    NovaCoquinaria
                       (Producto)
                              │
                              ▼
              GASTRO - SGCC (Sistema)
                              │
                              ▼
         Repositorio Markdown + GitHub
                    (Implementación)
```

---

# Justificación

Separar estos conceptos aporta varias ventajas:

* evita ambigüedades;
* facilita la documentación;
* permite evolucionar cada nivel de forma independiente;
* desacopla la identidad comercial de la implementación técnica.

---

# Alternativas consideradas

## Utilizar un único nombre para todo

**Descartado**.

Aunque más sencillo inicialmente, dificulta la evolución del proyecto y mezcla responsabilidades.

---

## Mantener GASTRO como marca

**Descartado**.

GASTRO describe adecuadamente el sistema interno, pero NovaCoquinaria transmite mejor la identidad pública del proyecto y su inspiración histórica.

---

# Consecuencias

## Ventajas

* Terminología consistente.
* Mejor documentación.
* Mayor flexibilidad para evolucionar la marca.
* Independencia entre arquitectura y presentación.

## Inconvenientes

* Requiere mantener la nomenclatura de forma disciplinada.

---

# Impacto futuro

Esta separación permitirá:

* cambiar la identidad visual sin modificar la arquitectura;
* desarrollar varias aplicaciones sobre el mismo sistema;
* crear diferentes interfaces utilizando la misma base de conocimiento;
* mantener una documentación técnica independiente del marketing o la comunicación.

---

# Dependencias

* [ADR-0001 - Filosofía del Proyecto](./ADR-0001-filosofia-del-proyecto.md)
* [ADR-0002 - Estructura del Repositorio](./ADR-0002-estructura-del-repositorio.md)
* [ADR-0003 - El Repositorio Markdown como Fuente Única de Verdad](./ADR-0003-markdown-como-fuente-de-verdad.md)
* [ADR-0010 - Arquitectura Orientada al Conocimiento, la Automatización y la Inteligencia Artificial](./ADR-0010-arquitectura-orientada-al-conocimiento.md)

---

# Véase también

* [README](../../README.md)
* [ARQUITECTURA](../ARQUITECTURA.md)
* [VISION](../VISION.md) *(pendiente de creación)*

---

# Utilizado por

Este ADR establece la terminología oficial que deberá emplearse en toda la documentación y en las futuras aplicaciones del proyecto.
