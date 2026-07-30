# ADR-0002 — Organización del Repositorio por Dominios de Conocimiento

**Identificador:** ADR-0002

**Estado:** Aceptado

**Vigencia:** Activa

**Última Revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Arquitectura

---

# Contexto

Tras adoptar el enfoque de Sistema de Gestión del Conocimiento Culinario (SGCC) (ADR-0001), surge la necesidad de definir una organización física del repositorio coherente con dicha filosofía.

Los recetarios tradicionales suelen estructurarse como una colección de recetas agrupadas por categorías culinarias.

Sin embargo, este enfoque mezcla distintos tipos de conocimiento, favorece la duplicación de información y dificulta su evolución.

El SGCC requiere una organización capaz de reflejar la naturaleza modular del conocimiento culinario.

---

# Problema

Es necesario definir una estructura de repositorio que permita:

- separar responsabilidades;
- organizar el conocimiento por dominios;
- favorecer la reutilización;
- facilitar el mantenimiento;
- permitir el crecimiento del proyecto sin perder coherencia.

---

# Decisión

El repositorio se organizará siguiendo una arquitectura basada en **dominios de conocimiento** y **responsabilidades funcionales**, en lugar de limitarse a clasificar recetas.

Cada área del repositorio tendrá un propósito claramente definido.

La organización física deberá reflejar la arquitectura conceptual del SGCC.

La estructura concreta de directorios podrá evolucionar con el tiempo siempre que respete estos principios.

---

# Justificación

La organización por dominios permite desacoplar el conocimiento culinario de su representación física.

Cada documento pertenece a un dominio concreto y posee una única responsabilidad.

Esta decisión facilita:

- reutilización;
- mantenibilidad;
- escalabilidad;
- evolución independiente de cada dominio;
- automatización.

La arquitectura deja de depender de un árbol concreto de carpetas.

---

# Alternativas consideradas

## Organización basada exclusivamente en recetas

Descartada por:

- duplicación de conocimiento;
- baja reutilización;
- mantenimiento complejo.

---

## Wiki sin organización definida

Descartada por:

- crecimiento desordenado;
- pérdida de coherencia;
- dificultades de automatización;
- escasa escalabilidad.

---

## Organización basada únicamente en tipos de fichero

Descartada por:

- mezclar dominios conceptuales diferentes;
- dificultar la navegación del conocimiento;
- limitar la evolución futura.

---

# Consecuencias

## Ventajas

- Arquitectura modular.
- Separación clara de responsabilidades.
- Mayor reutilización.
- Escalabilidad.
- Independencia entre dominios.
- Organización coherente con el modelo del SGCC.
- Adaptabilidad ante futuras reorganizaciones.

---

## Inconvenientes

- Requiere mayor planificación inicial.
- Obliga a mantener una arquitectura documental consistente.
- Exige comprender la separación entre dominio lógico y estructura física.

---

# Principios derivados

Esta decisión establece varios principios arquitectónicos.

- La estructura física refleja el modelo lógico del conocimiento.
- Cada dominio mantiene una responsabilidad claramente definida.
- La organización puede evolucionar sin alterar la filosofía del SGCC.
- El conocimiento tiene prioridad sobre la ubicación física de los documentos.

---

# Impacto futuro

Esta decisión permite que el repositorio pueda evolucionar sin depender de una estructura fija de directorios.

Como consecuencia, el SGCC podrá adaptarse a nuevas necesidades organizativas, nuevas colecciones o nuevas plataformas de publicación sin modificar los principios arquitectónicos fundamentales.

---

# Relación con otros ADR

Este ADR desarrolla la decisión fundacional establecida en:

- ADR-0001 — Filosofía del Proyecto.

Es ampliado posteriormente por:

- ADR-0005 — Separación del conocimiento.
- ADR-0010 — Arquitectura orientada al conocimiento.
- ADR-0018 — Modelo del conocimiento del SGCC.
- ADR-0019 — Modelo lógico vs estructura física.

---

# Documentación relacionada

La implementación de esta decisión se desarrolla en:

- ARQUITECTURA.md
- GOVERNANCE_MODEL.md
- ESPECIFICACION_DE_DOCUMENTOS.md
- ESPECIFICACION_DE_COLECCIONES.md

La estructura concreta del repositorio deberá mantenerse documentada en ARQUITECTURA.md y podrá evolucionar sin necesidad de modificar este ADR.

---

# Estado actual

La decisión continúa plenamente vigente.

Aunque la organización física del repositorio haya evolucionado desde la adopción de este ADR (por ejemplo, mediante la incorporación de nuevas áreas como **governance**, **specification** o **management**), dichos cambios representan una evolución de la implementación y no modifican la decisión arquitectónica adoptada.

El principio de organizar el SGCC por dominios de conocimiento y responsabilidades sigue constituyendo uno de los pilares fundamentales de la arquitectura del proyecto.