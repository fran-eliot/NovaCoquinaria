---
id: MGT-0012
tipo: gestion
titulo: Deuda de Conocimiento
version: 1.0
estado: estable
ultima_revision: 2026-07-10
---

# Deuda de Conocimiento

> Registro de las carencias estructurales que afectan a la calidad, reutilización y evolución del conocimiento de NovaCoquinaria.

---

# Objetivo

La deuda de conocimiento identifica aquellos elementos cuya ausencia, incompletitud o escasa integración reducen el valor del Sistema de Gestión del Conocimiento Culinario (SGCC).

No sustituye al backlog del proyecto ni al roadmap.

Su finalidad es facilitar la priorización de mejoras sobre el propio conocimiento.

---

# Concepto

Se considera deuda de conocimiento cualquier situación que:

* limite la reutilización;
* provoque duplicidad de información;
* reduzca la coherencia documental;
* dificulte la evolución del SGCC;
* genere relaciones incompletas dentro del Knowledge Graph.

La deuda puede detectarse mediante revisión editorial o automáticamente mediante las herramientas del proyecto.

---

# Clasificación

## Conocimiento inexistente

Conocimiento reutilizable que debería existir y todavía no ha sido documentado.

Ejemplos:

* Técnica de deglasado.
* Técnica de reducción.
* Gestión del calor.

---

## Conocimiento incompleto

Documentos existentes que todavía no desarrollan suficientemente su contenido.

| Documento | Observación | Prioridad |
|-----------|-------------|:---------:|
| Vinagreta base | Documento esqueleto sin reutilización | Alta |

---

## Conocimiento poco reutilizado

Documentos correctamente documentados, pero apenas utilizados desde otros elementos del SGCC.

| Documento      | Observación                     |
| -------------- | ------------------------------- |


---

## Conocimiento aislado

Documentos correctamente desarrollados que presentan escasas relaciones dentro del Knowledge Graph.

La detección podrá apoyarse en:

* `find_orphans.py`
* `generate_graph_stats.py`
* futuras métricas de conectividad.

---

## Cobertura insuficiente

Dominios culinarios cuyo conocimiento reutilizable resulta insuficiente para soportar nuevas recetas de forma coherente.

Ejemplos actuales:

* Cocina mediterránea.

---

## Revisión editorial pendiente

Documentos cuyo contenido requiere una revisión completa de:

* estilo;
* estructura;
* referencias cruzadas;
* calidad técnica.

---

# Estado actual

## Prioridad alta

* Completar Vinagreta base.
* Documentar la técnica de deglasado.
* Documentar la técnica de reducción.

---

## Prioridad media

* Consolidar variantes del dominio Currys.
* Revisar cobertura del dominio mediterráneo.

---

## Prioridad baja

* Revisiones editoriales generales.
* Ampliación progresiva de ingredientes secundarios.

---

# Deuda resuelta

## Dominio Currys

Durante la versión actual se han resuelto los siguientes elementos de deuda:

- Compleción de la plantilla **Curry base**.
- Documentación del ingrediente **Leche de coco**.
- Integración de **Curry amarillo** dentro del dominio.
- Creación de **REC-0017 · Curry amarillo de pollo** como receta de referencia.
- Eliminación de advertencias semánticas del dominio.
- Integración completa en el Knowledge Graph.

El dominio Currys dispone ahora de una base sólida para desarrollar nuevas variantes reutilizando el conocimiento existente.

---

# Integración con el Knowledge Graph

Parte de la deuda puede detectarse automáticamente.

Ejemplos:

* documentos reutilizables huérfanos;
* documentos con escasas referencias;
* relaciones semánticas incompletas;
* dominios poco conectados.

Otras formas de deuda requieren revisión humana.

---

# Resolución

La deuda deberá revisarse en cada nueva versión.

Cada elemento podrá:

* resolverse;
* reclasificarse;
* reducir su prioridad;
* eliminarse cuando deje de ser relevante.

No existe el objetivo de mantener este documento vacío.

La aparición de nueva deuda no implica un deterioro del proyecto.

Por el contrario, refleja la evolución natural del conocimiento y permite priorizar de forma objetiva las futuras mejoras del SGCC.

Su función es reflejar de forma transparente las áreas donde el conocimiento puede seguir mejorando.

---

# Principios

* Priorizar conocimiento reutilizable frente a recetas aisladas.
* Resolver primero la deuda estructural.
* Evitar crear deuda nueva.
* Favorecer la reutilización antes que la duplicación.
* Mantener un equilibrio entre crecimiento y calidad.

---

# Referencias

* [PROJECT_STATUS](PROJECT_STATUS.md)
* [ROADMAP](../ROADMAP.md)
* [KNOWLEDGE_STRATEGY](KNOWLEDGE_STRATEGY.md)
* [KNOWLEDGE_MATURITY](KNOWLEDGE_MATURITY.md)
* [BITACORA](BITACORA.md)
* [ADR-0014 · Gestión del conocimiento](../adr/ADR-0014-gestion-del-conocimiento.md)
