# CONTRIBUTING

> **Versión:** 2.0
> **Proyecto:** NovaCoquinaria
> **Sistema:** GASTRO - Sistema de Gestión del Conocimiento Culinario (SGCC)
---

# Objetivo

Este documento describe el procedimiento recomendado para incorporar nuevo conocimiento al proyecto NovaCoquinaria mediante la arquitectura GASTRO.

Aunque actualmente el proyecto tiene un único autor, estas normas garantizan la coherencia, la reutilización del conocimiento y la calidad de la documentación.

---

# Filosofía

En NovaCoquinaria no se incorporan simplemente documentos.

Se incorpora conocimiento.

Cada contribución debe aumentar, mejorar o relacionar el conocimiento existente antes que incrementar el número de archivos del repositorio.

---

# Flujo de contribución

```text
Nueva idea
      │
      ▼
¿Existe ya?
      │
 ┌────┴────┐
 │         │
Sí         No
 │         │
Ampliar    Crear entidad
 │         │
 └────┬────┘
      ▼
Relacionar
      ▼
Validar
      ▼
Integrar
```

---

# Flujo de trabajo

Antes de crear un documento nuevo, seguir siempre el siguiente proceso.

## 1. Identificar el conocimiento

Preguntarse:

* ¿Qué estoy documentando?
* ¿Es un ingrediente?
* ¿Es una técnica?
* ¿Es un patrón culinario?
* ¿Es un plato canónico?
* ¿Es una variante?
* ¿Es una tabla?
* ¿Es un documento de arquitectura?

No crear una receta cuando el conocimiento pertenece a otra categoría.

---

## 2. Buscar información existente

Antes de crear un documento nuevo:

* Buscar documentos relacionados.
* Comprobar si ya existe esa información.
* Revisar posibles duplicidades.

Siempre debe priorizarse ampliar un documento existente frente a crear uno nuevo.

---

## 3. Clasificar el conocimiento

Determinar si la información:

- amplía una entidad existente;
- crea una nueva entidad;
- establece una nueva relación;
- corrige conocimiento existente.

Solo después decidir el tipo de documento adecuado.

---

## 4. Elegir el tipo de documento

Seleccionar el tipo adecuado según la especificación del proyecto.

Tipos disponibles:

* Documentación fundacional
* Arquitectura
* Gestión
* Entidades del conocimiento (ingredientes, técnicas, patrones, platos canónicos, variantes…)
* Tabla de referencia
* Receta
* Nota

---

## 5. Redactar

Escribir el documento respetando:

* la guía de estilo
* la estructura correspondiente
* las convenciones del repositorio

---

## 6. Añadir referencias

Todo documento deberá enlazar aquellos contenidos relacionados que ya existan.

Ejemplos:

- ingredientes
- técnicas
- patrones culinarios
- platos canónicos
- variantes
- tablas

---

## 7. Revisar

Antes de considerar terminado un documento comprobar:

* ortografía
* claridad
* estructura
* coherencia con la documentación existente
* ausencia de duplicidades
* referencias internas

---

## 8. Validar reutilización

Comprobar que el documento:

- reutiliza conocimiento existente;
- no introduce duplicidades;
- enlaza las entidades relacionadas;
- mantiene la coherencia del modelo de conocimiento.

---

## 9. Integrar

Si el documento modifica conocimiento ya existente deberá actualizarse:

* referencias cruzadas
* índices
* documentos relacionados
* historial de cambios
* Knowledge Graph

---

# Cuándo crear un documento nuevo

Crear un documento únicamente cuando:

* represente conocimiento nuevo;
* tenga una única responsabilidad;
* vaya a reutilizarse en otros documentos;
* no exista ya un documento equivalente.

---

# Cuándo ampliar un documento existente

Preferir ampliar un documento cuando:

* la información pertenezca claramente al mismo tema;
* el contenido complemente una explicación ya existente;
* la ampliación mejore la calidad del documento.

---

# Cuándo crear una receta

Una receta sólo debe crearse cuando describa una elaboración concreta.

No utilizar recetas para documentar:

* ingredientes;
* técnicas;
* utensilios;
* mezclas de especias;
* salsas base;
* conceptos generales.

---

# Revisión de calidad

Antes de incorporar un documento responder afirmativamente a todas estas preguntas.

* ¿Tiene una única responsabilidad?
* ¿Es reutilizable?
* ¿Está correctamente estructurado?
* ¿Está escrito con claridad?
* ¿Evita duplicidades?
* ¿Incluye referencias?
* ¿Aporta conocimiento útil?
* ¿Respeta el modelo de conocimiento del proyecto?

Si alguna respuesta es negativa, revisar el documento.

---

# Mejora continua

Ningún documento debe considerarse definitivo.

Siempre podrá:

* corregirse;
* ampliarse;
* reorganizarse;
* enriquecerse con nuevas técnicas o conocimientos.

La mejora continua forma parte de la filosofía del proyecto.

---

# Regla de oro

Antes de guardar cualquier documento formular siempre esta pregunta:

> **¿Estoy aumentando el conocimiento del sistema? ¿O simplemente estoy añadiendo información?**

Si únicamente se está añadiendo información, debe replantearse el diseño del documento.

---

## Documentos relacionados

- [CONTEXT](./CONTEXT.md)
- [MANIFESTO](./MANIFESTO.md)
- [GUIA_DE_ESTILO](./GUIA_DE_ESTILO.md)
- [ESPECIFICACION_DE_DOCUMENTOS](./ESPECIFICACION_DE_DOCUMENTOS.md)
- [MODELO_DE_CONOCIMIENTO](./docs/MODELO_DE_CONOCIMIENTO.md)