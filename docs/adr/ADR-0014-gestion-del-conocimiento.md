# ADR-0014 - Gestión del Conocimiento y Evolución del SGCC

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Fran Ramírezg

---

# Contexto

NovaCoquinaria no se concibe como una colección de recetas independientes, sino como un Sistema de Gestión del Conocimiento Culinario (SGCC).

El objetivo principal del proyecto es capturar, organizar, relacionar, reutilizar y hacer evolucionar conocimiento culinario de forma estructurada.

Las recetas constituyen únicamente una de las formas de representar dicho conocimiento.

---

# Problema

Los recetarios tradicionales organizan la información como documentos aislados.

Esto provoca:

* duplicidad de técnicas;
* repetición de ingredientes;
* dificultad de mantenimiento;
* escasa reutilización;
* crecimiento desordenado.

Es necesario adoptar un modelo centrado en el conocimiento y no en los documentos.

---

# Decisión

El conocimiento será la unidad fundamental del sistema.

Los documentos actuarán únicamente como contenedores estructurados de dicho conocimiento.

La evolución del proyecto deberá orientarse siempre a mejorar la calidad del conocimiento existente antes que aumentar el número de documentos.

---

# Principios

## El conocimiento prevalece sobre los documentos

El objetivo no es crear más recetas.

El objetivo es mejorar la base de conocimiento.

---

## Reutilización sistemática

Siempre que un conocimiento pueda reutilizarse:

* deberá documentarse una única vez;
* será referenciado desde el resto de documentos.

---

## Mejora continua

Todos los documentos podrán evolucionar.

La incorporación de nueva información deberá priorizar:

* ampliar;
* corregir;
* reorganizar;

antes que duplicar contenido.

---

## Modularidad

Cada documento representará una unidad cohesionada de conocimiento.

La composición de varias unidades permitirá construir recetas, menús, guías o futuras funcionalidades.

---

## Escalabilidad

El sistema deberá permitir incorporar nuevos dominios sin modificar la arquitectura existente.

Ejemplos futuros:

* nutrición;
* enología;
* fermentaciones;
* cocina molecular;
* planificación semanal;
* costes;
* sostenibilidad.

---

# Modelo de evolución

```text
Experiencia

↓

Nuevo conocimiento

↓

Clasificación

↓

Integración

↓

Referencias

↓

Reutilización

↓

Mejora continua

↓

Nueva experiencia
```

Este ciclo constituye el mecanismo de aprendizaje permanente del SGCC.

---

# Justificación

El valor de NovaCoquinaria no dependerá del número de recetas almacenadas.

Su principal activo será la calidad, organización y reutilización del conocimiento culinario.

Este enfoque facilita:

* mantenimiento;
* aprendizaje;
* automatización;
* evolución tecnológica;
* desarrollo de nuevas aplicaciones.

---

# Alternativas consideradas

## Repositorio orientado a recetas

**Descartado**.

No favorece la reutilización del conocimiento.

---

## Base documental sin estructura

**Descartada**.

No proporciona relaciones explícitas entre conceptos.

---

# Consecuencias

## Ventajas

* Base de conocimiento coherente.
* Evolución sostenible.
* Mayor calidad documental.
* Preparación para automatización.
* Excelente base para sistemas de IA.

## Inconvenientes

* Requiere disciplina documental.
* Incrementa el esfuerzo de análisis inicial.

---

# Impacto futuro

Este ADR permitirá que NovaCoquinaria evolucione desde un repositorio Markdown hasta una auténtica plataforma de gestión del conocimiento culinario.

Las futuras aplicaciones, asistentes inteligentes y herramientas de planificación compartirán siempre la misma base de conocimiento, garantizando coherencia y reutilización.

---

# Dependencias

* [ADR-0001 - Filosofía del Proyecto](./ADR-0001-filosofia-del-proyecto.md)
* [ADR-0005 - Separación del Conocimiento Culinario](./ADR-0005-separacion-del-conocimiento.md)
* [ADR-0007 - Modelo de Dominio del Sistema de Gestión del Conocimiento Culinario](./ADR-0007-modelo-de-dominio-del-sgcc.md)
* [ADR-0010 - Arquitectura Orientada al Conocimiento, la Automatización y la Inteligencia Artificial](./ADR-0010-arquitectura-orientada-al-conocimiento.md)

---

# Véase también

* [ARQUITECTURA](../ARQUITECTURA.md)
* [VISION](../VISION.md) *(pendiente de creación)*
* [ROADMAP](../ROADMAP.md) *(pendiente de creación)*

---

# Utilizado por

Este ADR resume los principios fundamentales del Sistema de Gestión del Conocimiento Culinario y deberá servir como referencia para cualquier evolución futura del proyecto.
