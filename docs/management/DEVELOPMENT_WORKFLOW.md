---
id: DOC-0009
titulo: Workflow de Desarrollo
tipo: gestion
version: 1.0
estado: estable
ultima_revision: 2026-07-19
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
5. Cada iniciativa de conocimiento debe poder evolucionar de forma independiente.

---

# Ciclo de desarrollo

Cada nueva iniciativa de conocimiento seguirá el mismo ciclo de vida.

```text
Idea u oportunidad
        ↓
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
        ↓
Actualización de PROJECT_STATUS
        ↓
Registro en BITÁCORA
        ↓
Preparación de Release (si procede)
        ↓
Nueva iteración
```

---

# Fase 1 · Selección de la iniciativa de conocimiento

El desarrollo comienza escogiendo una iniciativa de conocimiento.

- un dominio culinario;
- una técnica;
- una colección de ingredientes;
- una arquitectura documental;
- una mejora transversal.

---

# Fase 2 · Inventario

Antes de crear nuevos documentos se revisa el conocimiento existente.

Se identifican:

- ingredientes;
- técnicas;
- bases;
- patrones culinarios reutilizables;
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
- patrones culinarios reutilizables;
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

## Validación automática

- Front Matter.
- Identificadores únicos.
- Enlaces internos.
- Validación semántica.
- Knowledge Graph.
- Detección de documentos huérfanos.

## Validación arquitectónica

- ausencia de duplicidades;
- coherencia con el modelo de conocimiento;
- reutilización adecuada;
- cumplimiento de los ADR.

---

# Fase 8 · Consolidación

Un dominio se considera consolidado cuando:

- dispone del conocimiento reutilizable necesario;
- cuenta con una receta canónica;
- ingredientes, técnicas, patrones culinarios y demás entidades reutilizables;
- supera todas las validaciones automáticas;
- no presenta deuda significativa.

---

# Mejora continua

Cada dominio consolidado proporciona experiencia para mejorar el desarrollo de los siguientes.

La metodología podrá evolucionar cuando la experiencia práctica así lo justifique.

---

# Prioridades

El desarrollo seguirá siempre este orden de preferencia:

1. Corregir deuda de conocimiento
2. Mejorar conocimiento existente
3. Crear conocimiento reutilizable
4. Consolidar iniciativas
5. Incorporar nuevas recetas
6. Evolucionar la arquitectura

---

# Tipos de evolución

El workflow puede aplicarse a diferentes tipos de cambios:

- incorporación de nuevo conocimiento;
- ampliación de conocimiento existente;
- reorganización documental;
- evolución de herramientas;
- evolución de la arquitectura (mediante ADR).

---

# Relación con otros documentos


## Integración con el ciclo de vida del proyecto

```text
Idea
   │
   ▼
CONTRIBUTING
   │
   ▼
DEVELOPMENT_WORKFLOW
   │
   ▼
Validación
   │
   ▼
PROJECT_STATUS
   │
   ▼
BITÁCORA
   │
   ▼
RELEASES
   │
   ▼
ROADMAP
```

Este documento complementa:

- [VISION](../VISION.md)
- [ROADMAP](../ROADMAP.md)
- [ARQUITECTURA](../ARQUITECTURA.md)
- [KNOWLEDGE_STRATEGY](./KNOWLEDGE_STRATEGY.md)
- [KNOWLEDGE_DEBT](./KNOWLEDGE_DEBT.md)
- [KNOWLEDGE_MATURITY](./KNOWLEDGE_MATURITY.md)
- [PROJECT_ONBOARDING](./PROJECT_ONBOARDING.md)
- [CONTRIBUTING](../../CONTRIBUTING.md)
- [PROJECT_STRUCTURE](./PROJECT_STRUCTURE.md)
- [PROJECT_STATUS](./PROJECT_STATUS.md)
- [BITACORA](./BITACORA.md)
- [RELEASES](./RELEASES.md)

No sustituye a ninguno de ellos; describe únicamente el proceso de desarrollo del SGCC.