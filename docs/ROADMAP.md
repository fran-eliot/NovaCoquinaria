# ROADMAP

> **Proyecto:** NovaCoquinaria
> **Sistema:** GASTRO - Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento define la hoja de ruta de NovaCoquinaria.

No funciona como un calendario cerrado, sino como una guía de evolución por niveles de madurez.

---

# Principio general

NovaCoquinaria evolucionará de forma incremental.

Cada fase debe consolidar una capa del sistema antes de avanzar a la siguiente.

```text
Visión
  ↓
Arquitectura
  ↓
Base de conocimiento
  ↓
Recetas normalizadas
  ↓
Automatización
  ↓
Publicación
  ↓
Plataforma
  ↓
Inteligencia
```

---

# Nivel I - Fundación

**Estado:** Completado

## Objetivo

Definir la identidad, arquitectura y reglas del proyecto.

## Entregables

* `README.md`
* `GUIA_DE_ESTILO.md`
* `ESPECIFICACION_DE_DOCUMENTOS.md`
* `CONTRIBUTING.md`
* `CHANGELOG.md`
* `docs/ARQUITECTURA.md`
* `docs/VISION.md`
* `docs/ROADMAP.md`
* ADR fundacionales

## Resultado

El proyecto dispone de una arquitectura documental estable y una visión clara como Sistema de Gestión del Conocimiento Culinario.

---

# Nivel II - Base de Conocimiento

**Estado:** Completado en versión inicial

## Objetivo

Construir el núcleo culinario reutilizable del SGCC.

## Módulos incluidos

* `98_Tablas`
* `00_Bases`
* `11_Despensa`
* `12_Plantillas`

## Resultado

El repositorio ya dispone de:

* tablas maestras;
* técnicas fundamentales;
* ingredientes clave;
* plantillas reutilizables;
* referencias cruzadas.

Este nivel seguirá ampliándose de forma incremental según aparezcan nuevas necesidades.

---

# Nivel III - Recetas Estructuradas

**Estado:** Completado en versión inicial

## Objetivo

Normalizar la colección inicial de recetas siguiendo la especificación del proyecto.

## Resultado

Las recetas originales han sido integradas en el modelo de conocimiento reutilizable.

Cada receta actúa como una aplicación concreta de:

* técnicas;
* ingredientes;
* plantillas;
* tablas.

---

# Nivel IV - Revisión y Calidad

**Estado:** En curso

## Objetivo

Revisar la coherencia general del repositorio antes de consolidar la versión `v1.0.0`.

## Tareas principales

* Revisar enlaces relativos.
* Validar IDs únicos.
* Revisar Front Matter.
* Revisar estructura de carpetas.
* Comprobar coherencia entre README, ROADMAP y CHANGELOG.
* Detectar documentos huérfanos.
* Revisar consistencia editorial.

## Criterio de finalización

La fase estará completa cuando el repositorio pueda considerarse estable como primera versión funcional.

---

# Nivel V - Automatización

**Estado:** Pendiente

## Objetivo

Automatizar tareas repetitivas de mantenimiento y validación.

## Posibles automatizaciones

* Validación de Front Matter YAML.
* Detección de enlaces rotos.
* Generación automática de índices.
* Listado de documentos por tipo.
* Control de identificadores duplicados.
* Generación de mapas de dependencias.
* Revisión básica de estructura documental.

---

# Nivel VI - Publicación Web

**Estado:** Pendiente

## Objetivo

Convertir el repositorio en documentación navegable.

## Posibles herramientas

* MkDocs.
* Material for MkDocs.
* GitHub Pages.

## Entregables esperados

* Sitio web navegable.
* Buscador.
* Índice de recetas.
* Índice de ingredientes.
* Índice de técnicas.
* Navegación por categorías y tipos de documento.

---

# Nivel VII - Plataforma

**Estado:** Visión futura

## Objetivo

Construir herramientas software sobre la base de conocimiento.

## Posibles componentes

* API.
* Backend.
* Base de datos derivada.
* Gestor de recetas.
* Gestor de despensa.
* Planificador de menús.
* Generador de lista de la compra.

---

# Nivel VIII - Inteligencia

**Estado:** Visión futura

## Objetivo

Incorporar inteligencia artificial y búsqueda semántica sobre el conocimiento culinario.

## Posibles funcionalidades

* Asistente culinario basado en el repositorio.
* Sistema RAG.
* Recomendaciones según despensa.
* Adaptación de recetas.
* Planificación semanal inteligente.
* Sugerencias de sustituciones.
* Generación de variantes.
* Ayuda en batch cooking.

---

# Prioridad actual

La prioridad inmediata es completar la fase de **Revisión y Calidad**.

Orden recomendado:

1. Revisar `README.md`.
2. Revisar `CHANGELOG.md`.
3. Revisar `ROADMAP.md`.
4. Revisar enlaces internos.
5. Revisar Front Matter e IDs.
6. Preparar release `v1.0.0`.

---

# Criterios de priorización

Antes de añadir una tarea al roadmap, evaluar:

* ¿Mejora la reutilización del conocimiento?
* ¿Reduce duplicidades?
* ¿Facilita cocinar mejor?
* ¿Ayuda a estructurar futuras recetas?
* ¿Prepara el sistema para automatización?
* ¿Mantiene la coherencia con la visión del proyecto?

---

# Documentación relacionada

* [VISION](./VISION.md)
* [ARQUITECTURA](./ARQUITECTURA.md)
* [README](../README.md)
* [ADR](./adr/)

---

# Conclusión

El roadmap de NovaCoquinaria no se basa en fechas, sino en madurez.

El objetivo no es avanzar rápido, sino construir una base de conocimiento culinario sólida, coherente y preparada para evolucionar durante años.
