# ADR-0017 — Modelo de Abstracción del Conocimiento Culinario

**Identificador:** ADR-0017

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Modelo de Dominio

---

# Contexto

El SGCC organiza el conocimiento culinario mediante distintos tipos de componentes especializados.

Durante la evolución del dominio se observó que determinadas unidades de conocimiento no podían clasificarse adecuadamente utilizando únicamente las categorías existentes.

Algunas representaban procesos reutilizables, mientras que otras constituían recetas de referencia que servían como origen de numerosas variantes posteriores.

Esta situación evidenció la necesidad de incorporar distintos niveles de abstracción dentro del modelo del conocimiento culinario.

---

# Problema

No todo el conocimiento culinario posee el mismo nivel de abstracción.

Agrupar bajo una misma categoría elementos conceptualmente diferentes provoca:

- ambigüedad en el modelo;
- responsabilidades mezcladas;
- menor reutilización;
- dificultad para representar familias gastronómicas;
- pérdida de expresividad del dominio.

Es necesario distinguir explícitamente los diferentes niveles de abstracción presentes en el conocimiento culinario.

---

# Decisión

El SGCC adoptará un modelo de abstracción jerárquico para representar el conocimiento culinario.

Cada nivel tendrá una responsabilidad específica y podrá servir de base para los niveles inmediatamente inferiores.

Las variantes culinarias se construirán a partir de platos canónicos, mientras que éstos podrán apoyarse en patrones culinarios reutilizables.

---

# Justificación

La diferenciación entre niveles de abstracción incrementa la expresividad del modelo de dominio.

Cada componente representa un tipo concreto de conocimiento y mantiene una única responsabilidad conceptual.

Este enfoque facilita la reutilización, mejora la organización del sistema y permite representar de forma natural la evolución de las familias culinarias.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- Cada nivel representa un tipo distinto de conocimiento.
- Los niveles superiores describen conocimiento más general.
- Los niveles inferiores especializan el conocimiento anterior.
- La reutilización se produce entre niveles consecutivos.
- Las familias culinarias evolucionan mediante especialización progresiva.

---

# Modelo conceptual

```text
Principios

      │

      ▼

Técnicas

      │

      ▼

Patrones Culinarios

      │

      ▼

Platos Canónicos

      │

      ▼

Variantes

      │

      ▼

Instancias
```

Cada nivel incrementa la especialización del conocimiento.

---

# Niveles del modelo

El modelo podrá incorporar, entre otros:

- principios culinarios;
- técnicas;
- patrones culinarios;
- platos canónicos;
- variantes;
- futuras especializaciones.

Cada nivel constituye una abstracción distinta del conocimiento gastronómico.

---

# Alternativas consideradas

## Mantener únicamente técnicas y recetas

Descartada por no representar adecuadamente las familias culinarias.

---

## Considerar los platos canónicos como simples plantillas

Descartada por mezclar procesos reutilizables con recetas de referencia.

---

## Tratar todas las recetas como equivalentes

Descartada por perder información estructural del dominio.

---

# Consecuencias

## Ventajas

- Modelo conceptual más expresivo.
- Mejor representación del dominio.
- Mayor reutilización.
- Separación clara de responsabilidades.
- Facilita la evolución del conocimiento.
- Mejor preparación para sistemas inteligentes.

---

## Inconvenientes

- Incrementa ligeramente la complejidad conceptual.
- Puede requerir migraciones progresivas del conocimiento existente.

---

# Impacto arquitectónico

Esta decisión amplía el modelo conceptual del SGCC incorporando distintos niveles de abstracción del conocimiento culinario.

Como consecuencia:

- las familias gastronómicas podrán representarse de forma explícita;
- la reutilización se realizará respetando la jerarquía conceptual;
- el modelo ganará capacidad para evolucionar sin introducir ambigüedades;
- futuras herramientas podrán interpretar mejor la estructura del conocimiento.

---

# Relación con otros ADR

Este ADR desarrolla:

- ADR-0007 — Modelo Conceptual del Dominio del SGCC.
- ADR-0014 — Modelo de Gestión del Conocimiento.
- ADR-0015 — Arquitectura Basada en Componentes de Conocimiento.
- ADR-0016 — Estrategia de Evolución del Conocimiento.

Se complementa con:

- KNOWLEDGE_MODEL.md
- KNOWLEDGE_GRAPH.md
- KNOWLEDGE_STRATEGY.md

---

# Documentación relacionada

La aplicación práctica de esta decisión se desarrolla en:

- KNOWLEDGE_MODEL.md
- ESPECIFICACION_DE_DOCUMENTOS.md
- ARQUITECTURA.md

Las reglas específicas de representación documental de cada nivel podrán evolucionar sin modificar este ADR.

---

# Estado actual

La decisión continúa plenamente vigente.

El SGCC representa el conocimiento culinario mediante un modelo jerárquico de abstracciones que diferencia principios, técnicas, patrones, platos canónicos y variantes, permitiendo describir las familias gastronómicas de forma coherente, reutilizable y evolutiva.