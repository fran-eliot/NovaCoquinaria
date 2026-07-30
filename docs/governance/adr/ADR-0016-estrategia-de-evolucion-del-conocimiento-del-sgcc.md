# ADR-0016 — Estrategia de Evolución del Conocimiento del Sistema de Gestión del Conocimiento Culinario

**Identificador:** ADR-0016

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Estrategia del Conocimiento

---

# Contexto

El SGCC está concebido como un sistema de conocimiento en evolución continua.

Su crecimiento potencial abarca múltiples dominios, miles de unidades de conocimiento y un elevado número de relaciones entre ellas.

En este contexto, no resulta sostenible incorporar conocimiento siguiendo únicamente criterios cronológicos, temáticos o de completitud.

Es necesario disponer de una estrategia que oriente la evolución del sistema hacia aquellas incorporaciones que aporten un mayor valor al conjunto.

---

# Problema

La capacidad para incorporar nuevo conocimiento siempre será inferior al conocimiento potencial existente.

Sin una estrategia explícita de priorización:

- el crecimiento puede resultar desordenado;
- aumenta la deuda de conocimiento;
- disminuye la reutilización;
- aparecen dominios inconexos;
- se reduce el valor global del sistema.

---

# Decisión

La evolución del SGCC se priorizará según el valor estructural que cada nueva unidad de conocimiento aporte al conjunto del sistema.

La incorporación de nuevo conocimiento deberá fortalecer progresivamente:

- la reutilización;
- la conectividad;
- la cobertura;
- la cohesión;
- la madurez;
- la capacidad de evolución futura.

La completitud de un dominio nunca tendrá prioridad sobre el fortalecimiento del sistema global.

---

# Justificación

El conocimiento no posee el mismo impacto arquitectónico.

Algunas unidades actúan como componentes fundamentales reutilizados por numerosos dominios, mientras que otras representan aplicaciones concretas de dicho conocimiento.

Priorizar los componentes con mayor capacidad estructural incrementa el valor del SGCC de forma acumulativa y sostenible.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- El valor estructural prevalece sobre el volumen de contenido.
- La reutilización tiene prioridad sobre la duplicación.
- Los componentes fundamentales se desarrollan antes que sus aplicaciones.
- La evolución fortalece primero la base del sistema.
- Cada nueva incorporación debe integrarse con el conocimiento existente.

---

# Modelo conceptual

```text
Necesidad

      │

      ▼

Evaluación del Valor

      │

      ▼

Priorización

      │

      ▼

Incorporación

      │

      ▼

Integración

      │

      ▼

Mayor Valor del Sistema
```

La evolución del conocimiento responde a una estrategia y no a un crecimiento lineal.

---

# Criterios de priorización

La incorporación de nuevas unidades de conocimiento podrá considerar, entre otros factores:

- capacidad de reutilización;
- impacto estructural;
- conectividad dentro del Knowledge Graph;
- reducción de deuda de conocimiento;
- incremento de la cobertura;
- mejora de la madurez;
- fortalecimiento de dominios estratégicos.

Los criterios concretos podrán evolucionar conforme lo haga el sistema.

---

# Alternativas consideradas

## Crecimiento cronológico

Descartado por no maximizar el valor estructural del conocimiento.

---

## Completar dominios uno a uno

Descartado por limitar la reutilización transversal.

---

## Priorización exclusivamente temática

Descartada por ignorar la importancia arquitectónica de determinados componentes.

---

# Consecuencias

## Ventajas

- Crecimiento sostenible.
- Mayor reutilización.
- Mejor cohesión.
- Reducción de deuda.
- Incremento de la madurez.
- Evolución más eficiente.
- Mayor valor acumulado del conocimiento.

---

## Inconvenientes

- Requiere una evaluación continua del conocimiento existente.
- Hace menos predecible el orden de incorporación de nuevos documentos.

---

# Impacto arquitectónico

Esta decisión establece una estrategia explícita para la evolución del SGCC.

Como consecuencia:

- el roadmap podrá reorganizarse según el valor arquitectónico del conocimiento;
- la evolución favorecerá primero los componentes fundamentales;
- el crecimiento reforzará progresivamente el Knowledge Graph;
- la incorporación de nuevos dominios seguirá una estrategia orientada al fortalecimiento del sistema completo.

---

# Relación con otros ADR

Este ADR desarrolla:

- ADR-0014 — Modelo de Gestión del Conocimiento.
- ADR-0015 — Arquitectura Basada en Componentes de Conocimiento.

Se complementa con:

- KNOWLEDGE_STRATEGY.md
- KNOWLEDGE_MATURITY.md
- KNOWLEDGE_DEBT.md
- QUALITY.md

---

# Documentación relacionada

La aplicación práctica de esta decisión se desarrolla en:

- KNOWLEDGE_STRATEGY.md
- ROADMAP.md
- BITACORA.md
- GOVERNANCE_MODEL.md

Los criterios operativos de planificación podrán evolucionar sin modificar este ADR.

---

# Estado actual

La decisión continúa plenamente vigente.

El SGCC mantiene una estrategia de evolución basada en el valor estructural del conocimiento, priorizando aquellas incorporaciones que fortalecen la reutilización, la conectividad y la capacidad de crecimiento del sistema antes que la mera ampliación del volumen documental.