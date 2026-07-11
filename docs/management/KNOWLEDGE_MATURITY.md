---
id: MGT-0014
tipo: gestion
titulo: Madurez del Conocimiento
version: 1.0
estado: estable
ultima_revision: 2026-07-10
---

# Madurez del Conocimiento

> Modelo para evaluar la evolución y calidad del conocimiento del Sistema de Gestión del Conocimiento Culinario (SGCC).

---

# Objetivo

Este documento establece un modelo común para evaluar la madurez del conocimiento contenido en NovaCoquinaria.

Su finalidad no es medir la cantidad de documentos, sino valorar la calidad, reutilización, conectividad y evolución del conocimiento.

La evaluación de la madurez facilita:

* priorizar el trabajo;
* detectar desequilibrios;
* orientar el crecimiento del proyecto;
* medir la evolución entre versiones.

---

# Modelo de madurez

NovaCoquinaria adopta un modelo de seis niveles.

| Nivel | Nombre       | Significado                                                 |
| ----- | ------------ | ----------------------------------------------------------- |
| 0     | No iniciado  | El dominio no dispone de conocimiento documentado.          |
| 1     | Inicial      | Existen documentos básicos, todavía incompletos.            |
| 2     | Estructurado | El conocimiento presenta una estructura coherente.          |
| 3     | Reutilizable | Los documentos son reutilizados de forma habitual.          |
| 4     | Consolidado  | El dominio presenta alta calidad y buena conectividad.      |
| 5     | Referencia   | El dominio constituye un modelo de referencia para el SGCC. |

---

# Dimensiones de evaluación

La madurez se evaluará considerando varias dimensiones complementarias.

## Cobertura

Grado en que el dominio dispone del conocimiento reutilizable necesario.

Ejemplos:

* bases;
* técnicas;
* ingredientes;
* plantillas;
* tablas.

---

## Reutilización

Nivel de reutilización del conocimiento existente.

Indicadores posibles:

* referencias recibidas;
* uso desde recetas;
* uso desde plantillas.

---

## Conectividad

Calidad de las relaciones existentes dentro del Knowledge Graph.

Ejemplos:

* ausencia de documentos huérfanos;
* enlaces cruzados adecuados;
* integración entre dominios.

---

## Calidad documental

Valoración editorial del conocimiento.

Aspectos considerados:

* estructura;
* claridad;
* referencias;
* coherencia;
* mantenimiento.

---

# Estado actual

| Área         | Cobertura | Reutilización | Conectividad | Calidad | Nivel |
| ------------ | :-------: | :-----------: | :----------: | :-----: | :---: |
| Bases        |     🟡    |       🟢      |      🟢      |    🟢   |   3   |
| Técnicas     |     🟡    |       🟢      |      🟢      |    🟢   |   3   |
| Ingredientes |     🟢    |       🟡      |      🟢      |    🟢   |   3   |
| Plantillas   |     🟡    |       🟡      |      🟡      |    🟡   |   2   |
| Tablas       |     🟢    |       🟢      |      🟢      |    🟢   |   4   |
| Recetas      |     🟡    |       🟢      |      🟢      |    🟢   |   2   |

> Los valores anteriores representan una valoración global del proyecto y se revisarán en cada versión.

---

# Evolución histórica

| Versión | Bases | Técnicas | Ingredientes | Plantillas | Tablas | Recetas |
| ------- | :---: | :------: | :----------: | :--------: | :----: | :-----: |
| v1.0.0  |   2   |     2    |       2      |      1     |    3   |    2    |
| v1.1.0  |   2   |     2    |       2      |      1     |    3   |    2    |
| v1.2.0  |   2   |     2    |       2      |      1     |    3   |    2    |
| v1.3.0  |   3   |     3    |       3      |      2     |    4   |    2    |

Esta tabla permitirá visualizar la evolución del conocimiento a lo largo del proyecto.

---

# Integración con las herramientas

La evaluación podrá apoyarse parcialmente en:

* `generate_graph_stats.py`
* `find_orphans.py`
* `validate_semantics.py`
* `validate_links.py`
* futuras métricas del Knowledge Graph.

La valoración final seguirá siendo una decisión editorial.

---

# Relación con otros documentos

Este documento complementa:

* `KNOWLEDGE_STRATEGY.md`, que define cómo evoluciona el conocimiento.
* `KNOWLEDGE_DEBT.md`, que identifica las principales carencias.
* `PROJECT_STATUS.md`, que resume el estado global del proyecto.
* `ROADMAP.md`, que establece las fases de evolución.

---

# Revisión

La madurez deberá revisarse al preparar cada nueva versión del proyecto.

No es necesario modificar este documento durante el desarrollo diario.

---

# Principios

* La calidad prevalece sobre la cantidad.
* La reutilización prevalece sobre la duplicación.
* La conectividad favorece el aprendizaje y el mantenimiento.
* La evolución debe ser gradual y medible.

---

# Referencias

* [KNOWLEDGE_STRATEGY](KNOWLEDGE_STRATEGY.md)
* [KNOWLEDGE_DEBT](KNOWLEDGE_DEBT.md)
* [PROJECT_STATUS](PROJECT_STATUS.md)
* [ROADMAP](../ROADMAP.md)
* [ARQUITECTURA](../ARQUITECTURA.md)
* [ADR-0014 · Gestión del conocimiento](../adr/ADR-0014-gestion-del-conocimiento.md)
