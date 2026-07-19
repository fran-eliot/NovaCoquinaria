---
id: ADR-0017
titulo: Diferenciación entre Patrones Culinarios y Platos Canónicos
estado: Propuesto
fecha: 2026-07-17
autor: NovaCoquinaria
relacionadas:
  - ADR-0015
  - ADR-0016
---

# ADR-0017 · Diferenciación entre Patrones Culinarios y Platos Canónicos

## Contexto

Durante el desarrollo del dominio **Arroces** se introdujo la plantilla **Arroz frito base** con el objetivo de reutilizar el procedimiento común entre distintas recetas.

Sin embargo, el análisis de su contenido muestra que no representa únicamente un patrón culinario, sino un plato prácticamente completo que incluye:

- ingredientes estructurales;
- proporciones;
- procedimiento completo;
- criterios de resultado;
- variantes;
- equipamiento;
- conservación;
- consejos.

Esto difumina la frontera entre una **plantilla** y una **receta**.

---

# Problema

El SGCC distingue actualmente:

- Ingredientes
- Técnicas
- Plantillas
- Recetas

Sin embargo, existe un nivel conceptual intermedio que no estaba identificado:

**los platos canónicos**.

Un plato canónico no es una simple técnica reutilizable, sino una receta de referencia desde la que se derivan variantes.

---

# Decisión

Se distinguen dos conceptos diferentes.

## Patrón culinario

Describe una forma de cocinar.

No constituye un plato.

Puede reutilizarse en múltiples familias culinarias.

Ejemplos:

- Salteado asiático
- Curry base
- Marinada asiática
- Salsa china base
- Sofrito mediterráneo

Su finalidad es describir procesos reutilizables.

---

## Plato canónico

Representa la receta de referencia de una familia gastronómica.

Describe:

- ingredientes;
- flujo completo;
- resultado esperado;
- equilibrio del plato.

Puede servir de base para variantes posteriores.

Ejemplos:

- Arroz frito base
- Tortilla francesa
- Risotto blanco
- Pasta al pomodoro
- Curry amarillo básico

Las variantes implementan el plato canónico, no directamente el patrón culinario.

---

# Nuevo modelo conceptual

```text
Ingrediente
      │
      ▼
Técnica
      │
      ▼
Patrón culinario
      │
      ▼
Plato canónico
      │
      ▼
Variantes
```

---

# Consecuencias

## Plantillas

Las plantillas contendrán únicamente conocimiento transversal reutilizable.

No describirán platos completos.

---

## Recetas

Las recetas podrán clasificarse en dos categorías.

### Receta canónica

Actúa como referencia de una familia gastronómica.

### Receta derivada

Implementa una receta canónica añadiendo o modificando ingredientes, técnicas o contexto cultural.

---

# Ejemplo

```
Salteado asiático
        │
        ▼
Arroz frito base
        │
        ├── Arroz frito con huevo
        ├── Arroz frito con pollo
        ├── Arroz frito con gambas
        └── Arroz chaufa
```

---

# Beneficios

- Mayor claridad conceptual.
- Separación más limpia entre técnicas y recetas.
- Mejor reutilización del conocimiento.
- Facilita el crecimiento del SGCC.
- Reduce la complejidad de las plantillas.
- Permite representar familias culinarias de forma natural.

---

# Impacto

Esta ADR no implica cambios inmediatos.

Los documentos existentes podrán migrarse progresivamente cuando resulte conveniente.

La decisión afecta únicamente al modelo conceptual del SGCC.