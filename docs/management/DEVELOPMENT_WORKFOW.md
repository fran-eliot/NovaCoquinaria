---
title: Workflow de Desarrollo
version: 1.0
status: stable
owner: NovaCoquinaria
updated: 2026-07-13
---

# Workflow de Desarrollo

## Objetivo

Definir el proceso oficial para desarrollar y ampliar NovaCoquinaria de forma coherente, incremental y sostenible.

El objetivo del workflow es garantizar que el conocimiento culinario crezca con la misma calidad y consistencia independientemente del dominio que se esté desarrollando.

---

# Principios

Todo el desarrollo del SGCC se rige por los siguientes principios:

1. El conocimiento precede a las recetas.
2. Cada documento debe aportar un valor claro al sistema.
3. Reutilizar siempre que sea posible antes de crear nuevo contenido.
4. La arquitectura solo evoluciona cuando una necesidad real del conocimiento lo justifica.
5. Cada dominio debe poder desarrollarse y consolidarse de forma independiente.

---

# Ciclo de desarrollo

Cada nuevo dominio seguirá el mismo ciclo de vida.

```text
Selección del dominio
        ↓
Inventario del conocimiento existente
        ↓
Identificación de carencias
        ↓
Desarrollo del conocimiento reutilizable
        ↓
Creación de la receta canónica
        ↓
Desarrollo de variantes
        ↓
Validación automática
        ↓
Consolidación del dominio
```

---

# Fase 1 · Selección del dominio

El desarrollo comienza escogiendo un dominio culinario.

Ejemplos:

- Currys
- Wok
- Arroces
- Cocina mediterránea
- Marinados
- Salsas

Cada dominio constituye una unidad independiente de conocimiento.

---

# Fase 2 · Inventario

Antes de crear nuevos documentos se revisa el conocimiento existente.

Se identifican:

- ingredientes;
- técnicas;
- bases;
- plantillas;
- tablas;
- recetas.

El objetivo es reutilizar al máximo el conocimiento ya documentado.

---

# Fase 3 · Identificación de carencias

Una vez realizado el inventario se identifican los activos de conocimiento que faltan.

La prioridad vendrá determinada por su capacidad de reutilización.

Se priorizarán los documentos con mayor impacto transversal.

---

# Fase 4 · Desarrollo del conocimiento reutilizable

Antes de crear nuevas recetas deberán consolidarse los elementos reutilizables del dominio.

Por ejemplo:

- ingredientes;
- técnicas;
- plantillas;
- tablas.

---

# Fase 5 · Receta canónica

Cada dominio dispondrá inicialmente de una receta de referencia.

La receta canónica debe:

- reutilizar el máximo conocimiento existente;
- evitar duplicidades;
- servir como modelo para futuras recetas del dominio.

---

# Fase 6 · Variantes

Una vez consolidada la receta canónica podrán desarrollarse variantes que reutilicen el conocimiento ya existente.

---

# Fase 7 · Validación

Todo cambio deberá superar el pipeline documental.

Validaciones mínimas:

- Front Matter.
- Identificadores únicos.
- Enlaces internos.
- Validación semántica.
- Knowledge Graph.
- Detección de documentos huérfanos.

---

# Fase 8 · Consolidación

Un dominio se considera consolidado cuando:

- dispone del conocimiento reutilizable necesario;
- cuenta con una receta canónica;
- reutiliza correctamente ingredientes, técnicas y plantillas;
- supera todas las validaciones automáticas;
- no presenta deuda significativa.

---

# Mejora continua

Cada dominio consolidado proporciona experiencia para mejorar el desarrollo de los siguientes.

La metodología podrá evolucionar cuando la experiencia práctica así lo justifique.

---

# Prioridades

El desarrollo seguirá siempre este orden de preferencia:

1. Corregir deuda de conocimiento.
2. Crear conocimiento reutilizable.
3. Consolidar dominios.
4. Crear nuevas recetas.
5. Evolucionar la arquitectura (solo si es necesario).

---

# Relación con otros documentos

Este documento complementa:

- [VISION](../VISION.md)
- [ROADMAP](../ROADMAP.md)
- [ARQUITECTURA](../ARQUITECTURA.md)
- [KNOWLEDGE_STRATEGY](./KNOWLEDGE_STRATEGY.md)
- [KNOWLEDGE_DEBT](./KNOWLEDGE_DEBT.md)
- [KNOWLEDGE_MATURITY](./KNOWLEDGE_MATURITY.md)

No sustituye a ninguno de ellos; describe únicamente el proceso de desarrollo del SGCC.