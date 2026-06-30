# ROADMAP

> **Proyecto:** NovaCoquinaria
> **Sistema:** GASTRO - Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento define la hoja de ruta de NovaCoquinaria.

Su finalidad es ordenar la evolución del proyecto por fases de madurez, evitando depender de fechas rígidas.

El roadmap no pretende ser un calendario cerrado, sino una guía estratégica para decidir qué construir primero y qué dejar para fases posteriores.

---

# Principio General

NovaCoquinaria evolucionará de forma incremental.

Cada fase deberá consolidar una capa del sistema antes de avanzar a la siguiente.

```text
Visión
  ↓
Arquitectura
  ↓
Base de conocimiento
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
* ADR fundacionales

## Criterio de finalización

La fase se considera completada cuando existe una arquitectura documental estable y una visión clara del sistema.

---

# Nivel II - Base de Conocimiento

**Estado:** En desarrollo

## Objetivo

Construir el núcleo culinario reutilizable del SGCC.

## Áreas principales

* `00_Bases`
* `98_Tablas`
* `11_Despensa`
* `12_Plantillas`

## Entregables esperados

* técnicas fundamentales;
* proporciones;
* tiempos de cocción;
* tiempos de horno;
* conservación;
* congelación;
* seguridad alimentaria;
* ingredientes principales de despensa;
* plantillas reutilizables de elaboración.

## Criterio de finalización

La fase estará madura cuando la mayoría de recetas puedan apoyarse en documentos base, tablas, despensa y plantillas sin duplicar explicaciones.

---

# Nivel III - Recetas Estructuradas

**Estado:** Pendiente

## Objetivo

Revisar, normalizar y ampliar las recetas existentes siguiendo la especificación del proyecto.

## Entregables esperados

* recetas con Front Matter YAML;
* estructura homogénea;
* referencias cruzadas;
* dependencias claras;
* criterios de conservación, congelación y recalentado;
* variantes documentadas.

## Criterio de finalización

La fase estará madura cuando las recetas de uso habitual estén normalizadas y conectadas con el resto de la base de conocimiento.

---

# Nivel IV - Automatización

**Estado:** Pendiente

## Objetivo

Automatizar tareas repetitivas de mantenimiento y validación.

## Posibles automatizaciones

* validación de Front Matter YAML;
* detección de enlaces rotos;
* generación automática de índices;
* listado de documentos por tipo;
* control de identificadores duplicados;
* generación de mapas de dependencias;
* revisión básica de estructura documental.

## Criterio de finalización

La fase estará madura cuando el repositorio pueda validarse automáticamente antes de integrar cambios importantes.

---

# Nivel V - Publicación Web

**Estado:** Pendiente

## Objetivo

Convertir el repositorio en una documentación navegable.

## Posibles herramientas

* MkDocs;
* Material for MkDocs;
* GitHub Pages.

## Entregables esperados

* sitio web navegable;
* buscador;
* navegación por categorías;
* navegación por tipos de documento;
* índice de recetas;
* índice de ingredientes;
* índice de técnicas.

## Criterio de finalización

La fase estará madura cuando NovaCoquinaria pueda consultarse cómodamente como manual web.

---

# Nivel VI - Plataforma

**Estado:** Visión futura

## Objetivo

Construir herramientas software sobre la base de conocimiento.

## Posibles componentes

* API;
* backend;
* base de datos derivada;
* panel de administración;
* gestor de recetas;
* gestor de despensa;
* planificador de menús;
* generador de lista de la compra.

## Criterio de finalización

La fase estará madura cuando exista una aplicación funcional que consuma el repositorio como fuente de verdad.

---

# Nivel VII - Inteligencia

**Estado:** Visión futura

## Objetivo

Incorporar inteligencia artificial y búsqueda semántica sobre el conocimiento culinario.

## Posibles funcionalidades

* asistente culinario basado en el repositorio;
* sistema RAG;
* recomendaciones según despensa;
* adaptación de recetas;
* planificación semanal inteligente;
* sugerencias de sustituciones;
* generación de variantes;
* ayuda en batch cooking.

## Criterio de finalización

La fase estará madura cuando el sistema pueda responder preguntas y generar propuestas utilizando el conocimiento estructurado de NovaCoquinaria.

---

# Prioridad Actual

La prioridad inmediata del proyecto es completar el **Nivel II - Base de Conocimiento**.

Orden recomendado:

1. `98_Tablas`
2. `00_Bases`
3. `11_Despensa`
4. `12_Plantillas`
5. normalización progresiva de recetas

---

# Criterios de Priorización

Antes de añadir una tarea al roadmap, evaluar:

* ¿Mejora la reutilización del conocimiento?
* ¿Reduce duplicidades?
* ¿Facilita cocinar mejor?
* ¿Ayuda a estructurar futuras recetas?
* ¿Prepara el sistema para automatización?
* ¿Mantiene la coherencia con la visión del proyecto?

---

# Documentación Relacionada

* [VISION](./VISION.md)
* [ARQUITECTURA](./ARQUITECTURA.md)
* [README](../README.md)
* [ADR](./adr/)

---

# Conclusión

El roadmap de NovaCoquinaria no se basa en fechas, sino en madurez.

Cada fase debe fortalecer el sistema antes de pasar a la siguiente.

El objetivo no es avanzar rápido, sino construir una base de conocimiento culinario sólida, coherente y preparada para evolucionar durante años.
