---
id: ARC-0018
tipo: arquitectura
titulo: Modelo de Colecciones de Conocimiento
version: 2.0
estado: estable
ultima_revision: 2026-07-20
---

# Modelo de Colecciones de Conocimiento

> Proyecto: NovaCoquinaria
> Sistema: GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento define el modelo oficial de las Colecciones de Conocimiento del SGCC.

Las colecciones permiten gestionar el desarrollo de dominios culinarios de forma transversal, sin alterar la organización física del repositorio ni duplicar conocimiento existente.

Constituyen un mecanismo de planificación y consolidación del conocimiento.

---

# Alcance

Esta especificación define:

- qué es una colección;
- cuál es su responsabilidad;
- cómo se estructura;
- qué relaciones mantiene con el resto del SGCC;
- cómo evoluciona durante el ciclo de vida del conocimiento.

No define contenido culinario.

No sustituye documentos especializados.

---

# Definición

Una colección representa un dominio de conocimiento gestionado.

Agrupa virtualmente activos relacionados para facilitar:

- planificación;
- consolidación;
- reutilización;
- evaluación de madurez.

Una colección no constituye una categoría documental adicional.

Tampoco modifica la organización física del repositorio.

---

# Papel dentro del SGCC

Las colecciones ocupan un nivel superior al de los documentos individuales.

```text
Repositorio

↓

Documentos

↓

Knowledge Graph

↓

Colecciones

↓

Dominios culinarios
```

Su finalidad consiste en coordinar el desarrollo del conocimiento.

No almacenarlo.

---

# Principios

Toda colección deberá respetar los siguientes principios.

## No duplicación

Nunca contendrá conocimiento desarrollado en otros documentos.

---

## Planificación

Organiza el crecimiento del conocimiento.

---

## Reutilización

Favorece la reutilización entre dominios.

---

## Trazabilidad

Permite conocer el estado de desarrollo de un dominio.

---

## Evolución

Puede evolucionar independientemente del repositorio físico.

---

# Modelo de una colección

Toda colección representa cuatro dimensiones.

## Alcance

Qué dominio cubre.

---

## Cobertura

Qué conocimiento existe.

---

## Deuda

Qué conocimiento falta.

---

## Evolución

Qué prioridades existen.

---

# Estructura

Toda colección incluirá, como mínimo:

- Objetivo;
- Alcance;
- Estado;
- Conocimiento existente;
- Conocimiento pendiente;
- Deuda de conocimiento;
- Próximos hitos;
- Referencias.

La estructura podrá ampliarse cuando resulte necesario.

---

# Estados

Las colecciones evolucionan junto con el dominio.

Estados recomendados:

- propuesta;
- en desarrollo;
- en consolidación;
- referencia;
- archivada.

Los estados reflejan la madurez del dominio.

No la calidad individual de sus documentos.

---

# Relaciones

Las colecciones mantienen relaciones con distintos elementos del SGCC.

## Documentos

Agrupan activos existentes.

---

## Knowledge Graph

Complementan las relaciones reales mediante planificación.

---

## Roadmap

Permiten establecer prioridades.

---

## Knowledge Debt

Identifican carencias específicas del dominio.

---

## Knowledge Maturity

Facilitan evaluar la evolución del conocimiento.

---

# Evaluación

Una colección aporta valor cuando:

- posee un alcance claramente definido;
- organiza un dominio reconocible;
- reutiliza documentos existentes;
- identifica deuda de conocimiento;
- facilita decisiones de priorización;
- puede mantenerse de forma sostenible.

---

# Ciclo de vida

Las colecciones evolucionan conforme madura el conocimiento.

```text
Propuesta

↓

Desarrollo

↓

Consolidación

↓

Referencia
```

La evolución nunca implica reorganizar físicamente el repositorio.

---

# Compatibilidad

Las colecciones constituyen una capa lógica.

Podrán utilizarse como fuente para:

- paneles de seguimiento;
- métricas;
- planificación;
- herramientas de análisis;
- asistentes inteligentes;
- visualización de dominios.

---

# Relación con otros documentos

| Documento | Responsabilidad |
|-----------|-----------------|
| ESPECIFICACION_DE_DOCUMENTOS | Modelo documental |
| QUALITY | Modelo de calidad |
| KNOWLEDGE_GRAPH | Relaciones reales |
| KNOWLEDGE_DEBT | Carencias |
| KNOWLEDGE_MATURITY | Evolución |
| ROADMAP | Planificación temporal |

---

# Conclusión

Las Colecciones de Conocimiento constituyen una capa lógica de planificación dentro del SGCC.

Permiten gestionar dominios culinarios completos sin alterar la arquitectura documental ni duplicar conocimiento, facilitando una evolución coherente, reutilizable y sostenible del ecosistema de conocimiento.
