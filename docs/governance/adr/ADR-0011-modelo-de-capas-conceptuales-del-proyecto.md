# ADR-0011 — Modelo de Capas Conceptuales del Proyecto NovaCoquinaria

**Identificador:** ADR-0011

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Arquitectura

---

# Contexto

A medida que el proyecto ha evolucionado han aparecido distintos conceptos utilizados para describir realidades diferentes:

- NovaCoquinaria;
- SGCC;
- repositorio;
- aplicaciones;
- documentación.

La utilización indistinta de estos términos dificulta la comprensión de la arquitectura y puede generar ambigüedades tanto en la documentación como en el desarrollo futuro.

Es necesario definir un modelo conceptual que distinga claramente cada nivel del proyecto.

---

# Problema

El proyecto está formado por diferentes capas conceptuales con responsabilidades distintas.

Sin una terminología uniforme resulta difícil diferenciar:

- la identidad pública;
- el producto;
- el sistema de conocimiento;
- la gobernanza;
- la implementación técnica.

---

# Decisión

El proyecto se organizará mediante un conjunto de capas conceptuales claramente diferenciadas.

Cada capa representa una responsabilidad específica y podrá evolucionar de forma relativamente independiente.

Las capas forman una jerarquía donde cada nivel se apoya sobre el anterior.

---

# Justificación

Separar explícitamente estos niveles permite desacoplar:

- identidad;
- arquitectura;
- gobernanza;
- conocimiento;
- implementación.

Este modelo facilita la evolución del proyecto sin comprometer la coherencia conceptual.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- La marca no define la arquitectura.
- El producto no define el conocimiento.
- El conocimiento no depende del repositorio.
- El repositorio implementa el sistema, pero no lo define.
- Cada capa mantiene una única responsabilidad.

---

# Modelo conceptual

```text
            NovaCoquinaria
                (Marca)

                   │

                   ▼

            NovaCoquinaria
               (Producto)

                   │

                   ▼

                SGCC
      (Sistema de Conocimiento)

                   │

                   ▼

             Gobernanza
   (Principios, Calidad, Estrategia)

                   │

                   ▼

         Repositorio Markdown
         (Implementación Física)
```

Cada capa representa una visión diferente del mismo proyecto.

---

# Capas conceptuales

## Marca

Representa la identidad pública del proyecto.

Es independiente de la arquitectura interna.

---

## Producto

Representa el conjunto de soluciones ofrecidas al usuario.

Podrá incorporar nuevas aplicaciones sin modificar el sistema de conocimiento.

---

## Sistema

Representa el modelo conceptual del SGCC.

Constituye el núcleo permanente del proyecto.

---

## Gobernanza

Define las reglas mediante las que evoluciona el sistema.

Incluye:

- arquitectura;
- calidad;
- estrategia;
- deuda;
- madurez;
- automatización;
- protocolo de IA.

---

## Implementación

Representa la materialización física del sistema mediante el repositorio y sus herramientas.

Podrá evolucionar sin modificar el modelo conceptual.

---

# Alternativas consideradas

## Utilizar un único término para todo el proyecto

Descartada por mezclar responsabilidades diferentes.

---

## Asociar la arquitectura directamente al repositorio

Descartada por acoplar el modelo conceptual a una implementación concreta.

---

## Considerar la marca como sistema

Descartada por confundir identidad pública con arquitectura.

---

# Consecuencias

## Ventajas

- Terminología uniforme.
- Arquitectura más comprensible.
- Evolución independiente de cada capa.
- Independencia entre negocio y tecnología.
- Mayor claridad documental.

---

## Inconvenientes

- Necesidad de mantener una nomenclatura consistente.
- Curva inicial de aprendizaje ligeramente superior.

---

# Impacto arquitectónico

Esta decisión establece una separación clara entre los distintos niveles del proyecto.

Como consecuencia:

- la marca podrá evolucionar sin afectar al SGCC;
- el producto podrá incorporar nuevas capacidades;
- la gobernanza permanecerá estable;
- el repositorio podrá reorganizarse;
- futuras aplicaciones compartirán el mismo sistema de conocimiento.

---

# Relación con otros ADR

Este ADR desarrolla:

- ADR-0001 — Filosofía del Proyecto.
- ADR-0003 — Markdown como Fuente Única de Verdad.
- ADR-0010 — Arquitectura Orientada al Conocimiento.

Es complementado posteriormente por:

- ADR-0018 — Modelo del Conocimiento del SGCC.
- ADR-0019 — Modelo Lógico vs Estructura Física.

---

# Documentación relacionada

La aplicación práctica de esta decisión se desarrolla en:

- ARQUITECTURA.md
- GOVERNANCE_MODEL.md
- VISION.md
- AI_PROTOCOL.md
- KNOWLEDGE_STRATEGY.md
- README.md

---

# Estado actual

La decisión continúa plenamente vigente.

El proyecto NovaCoquinaria se entiende como un conjunto de capas conceptuales complementarias donde la marca, el producto, el sistema, la gobernanza y la implementación representan responsabilidades distintas pero coordinadas.

Toda evolución futura deberá preservar esta separación para mantener la claridad arquitectónica y facilitar la evolución independiente de cada nivel.