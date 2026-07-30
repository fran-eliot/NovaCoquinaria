# ADR-0018 — Ontología del Conocimiento del Sistema de Gestión del Conocimiento Culinario

**Identificador:** ADR-0018

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Modelo del Conocimiento

---

# Contexto

El SGCC se concibe como un sistema capaz de representar conocimiento culinario mediante entidades especializadas y relaciones explícitas.

Durante la evolución del proyecto se constató que los distintos componentes del conocimiento poseen naturalezas, responsabilidades y niveles de abstracción diferentes.

Para garantizar la coherencia del sistema resulta necesario definir un modelo ontológico común que permita clasificar, relacionar y evolucionar dichas entidades de forma consistente.

---

# Problema

Sin un modelo explícito de representación del conocimiento:

- aparecen categorías ambiguas;
- disminuye la coherencia del dominio;
- se dificulta la reutilización;
- las relaciones pierden significado;
- el crecimiento del sistema resulta difícil de gobernar.

Es necesario establecer una ontología que defina qué tipos de entidades existen y cómo pueden relacionarse.

---

# Decisión

El SGCC representará el conocimiento mediante un conjunto de tipos de entidades con identidad propia, responsabilidades diferenciadas y relaciones semánticas explícitas.

Cada unidad de conocimiento pertenecerá a un tipo determinado y participará en un grafo de conocimiento compartido.

El significado de una entidad vendrá determinado tanto por su naturaleza como por las relaciones que mantiene con el resto del sistema.

---

# Justificación

Una ontología común proporciona un lenguaje compartido para todo el SGCC.

Permite representar el conocimiento de forma coherente, facilita su evolución y constituye la base para futuras capacidades de búsqueda, razonamiento, automatización e inteligencia artificial.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- Toda unidad de conocimiento posee un tipo definido.
- Cada tipo representa una responsabilidad conceptual distinta.
- Las relaciones forman parte del propio conocimiento.
- El valor del sistema reside tanto en las entidades como en sus conexiones.
- El crecimiento del modelo preservará la coherencia ontológica.

---

# Modelo conceptual

```text
              Unidad de Conocimiento

                      │

      ┌───────────────┼────────────────┐

      │               │                │

     Tipo       Propiedades      Relaciones

      │               │                │

      └───────────────┼────────────────┘

                      ▼

           Grafo de Conocimiento
```

Las entidades adquieren significado mediante su clasificación y sus relaciones.

---

# Tipos de entidades

La ontología del SGCC incorpora inicialmente, entre otros, los siguientes tipos:

- ingredientes;
- técnicas;
- patrones culinarios;
- platos canónicos;
- variantes;
- tablas de conocimiento.

La incorporación de nuevos tipos requerirá justificar su identidad conceptual y su aportación al modelo.

---

# Relaciones semánticas

Las entidades podrán establecer relaciones como:

- utiliza;
- requiere;
- implementa;
- deriva de;
- sustituye;
- pertenece a;
- referencia;
- acompaña.

El catálogo de relaciones podrá ampliarse siempre que preserve la coherencia del modelo ontológico.

---

# Alternativas consideradas

## Representar únicamente documentos

Descartada por no reflejar adecuadamente la naturaleza del conocimiento.

---

## Clasificar todas las entidades mediante una única categoría

Descartada por perder expresividad conceptual.

---

## Modelar únicamente relaciones documentales

Descartada por limitar la capacidad de razonamiento y reutilización.

---

# Consecuencias

## Ventajas

- Modelo conceptual explícito.
- Mayor coherencia del dominio.
- Navegación semántica.
- Reutilización estructurada.
- Evolución controlada.
- Excelente preparación para Knowledge Graph, RAG y agentes inteligentes.

---

## Inconvenientes

- Requiere disciplina en la clasificación del conocimiento.
- Incrementa la complejidad conceptual inicial.

---

# Impacto arquitectónico

Esta decisión convierte la ontología en el núcleo estructural del SGCC.

Como consecuencia:

- todas las unidades de conocimiento compartirán un mismo modelo conceptual;
- las relaciones adquirirán valor arquitectónico propio;
- el sistema podrá evolucionar sin introducir inconsistencias conceptuales;
- futuras herramientas podrán interpretar el conocimiento de forma semántica.

---

# Relación con otros ADR

Este ADR consolida:

- ADR-0007 — Modelo Conceptual del Dominio del SGCC.
- ADR-0015 — Arquitectura Basada en Componentes de Conocimiento.
- ADR-0016 — Estrategia de Evolución del Conocimiento.
- ADR-0017 — Modelo de Abstracción del Conocimiento Culinario.

Se complementa con:

- KNOWLEDGE_MODEL.md
- KNOWLEDGE_GRAPH.md
- AI_PROTOCOL.md
- KNOWLEDGE_STRATEGY.md

---

# Documentación relacionada

La aplicación práctica de esta decisión se desarrolla en:

- KNOWLEDGE_MODEL.md
- KNOWLEDGE_GRAPH.md
- ARQUITECTURA.md
- ESPECIFICACION_DE_DOCUMENTOS.md

Las implementaciones concretas del modelo documental podrán evolucionar sin modificar esta ontología.

---

# Estado actual

La decisión continúa plenamente vigente.

El SGCC representa el conocimiento mediante una ontología compuesta por entidades tipificadas y relaciones semánticas explícitas que conforman un Knowledge Graph coherente, reutilizable y preparado para soportar futuras capacidades de automatización, búsqueda semántica e inteligencia artificial.