---
id: SPEC-INDEXING-ENGINE
tipo: especificacion
titulo: Especificación del Indexing Engine
version: 1.0.0
estado: borrador
ultima_revision: 2026-08-02
tags:
  - indexing
  - chunks
  - embeddings
  - indexes
  - snapshots
  - architecture
---

# ESPECIFICACION_DEL_INDEXING_ENGINE.md

**Versión:** 2.0.0  
**Estado:** Draft  
**Autor:** NovaCoquinaria Project  
**Última actualización:** 2026-08-01

---

# Parte I — Fundamentos, arquitectura general y modelo conceptual del Indexing Engine

---

# Introducción

NovaCoquinaria dispone de una arquitectura formal para:

- representar documentos;
- modelar componentes;
- declarar relaciones;
- gobernar ontologías;
- organizar colecciones;
- construir el Knowledge Graph;
- ejecutar ingestas;
- validar conocimiento;
- aplicar razonamiento;
- generar respuestas mediante RAG;
- exponer capacidades mediante APIs.

Sin embargo, el conocimiento canónico no podrá consultarse de forma eficiente únicamente recorriendo:

- documentos Markdown;
- estructuras parseadas;
- tablas;
- relaciones completas;
- snapshots del Knowledge Graph.

Para proporcionar:

- búsquedas rápidas;
- recuperación semántica;
- filtros;
- ranking;
- navegación estructurada;
- GraphRAG;
- consultas híbridas;
- recuperación incremental;
- respuestas fundamentadas;

será necesario transformar el conocimiento validado en estructuras optimizadas para lectura.

Esta responsabilidad corresponderá al **Indexing Engine**.

Conceptualmente:

```text
Canonical Knowledge
        │
        ├── Documents
        ├── Components
        ├── Statements
        ├── Relations
        ├── Ontologies
        ├── Collections
        └── Knowledge Graph
        │
        ▼
Indexing Engine
        │
        ├── Select
        ├── Normalize
        ├── Segment
        ├── Enrich
        ├── Embed
        ├── Index
        ├── Validate
        └── Publish
        │
        ▼
Index Snapshots
        │
        ├── Lexical Index
        ├── Vector Index
        ├── Structured Index
        ├── Graph Index
        └── Metadata Index
```

El Indexing Engine no deberá convertirse en una segunda fuente de verdad.

Los índices serán representaciones derivadas, reconstruibles y subordinadas al conocimiento canónico.

---

# Misión

La misión del Indexing Engine será:

> Transformar conocimiento validado y versionado en representaciones recuperables, eficientes, trazables, reproducibles y compatibles con los motores de búsqueda, Retrieval y RAG de NovaCoquinaria.

---

# Visión

El Indexing Engine deberá permitir que una misma base de conocimiento pueda consultarse mediante distintas perspectivas:

```text
Texto
```

```text
Semántica
```

```text
Metadatos
```

```text
Relaciones
```

```text
Estructura
```

```text
Grafo
```

```text
Temporalidad
```

Estas perspectivas no deberán mantenerse como silos independientes.

Deberán conservar una referencia común hacia:

- recurso canónico;
- documento;
- fragmento;
- statement;
- relación;
- snapshot;
- versión;
- procedencia.

---

# Objetivos

Esta especificación persigue los siguientes objetivos:

- definir la misión y límites del Indexing Engine;
- establecer sus principios arquitectónicos;
- formalizar el concepto de índice derivado;
- definir los tipos de índice;
- establecer el modelo de unidad indexable;
- formalizar los snapshots de índice;
- diferenciar índices activos, candidatos e históricos;
- establecer el pipeline conceptual;
- definir responsabilidades y exclusiones;
- formalizar perfiles de indexación;
- definir ámbitos de indexación;
- establecer la relación con Ingestion, Validation, Knowledge Graph, Retrieval y RAG;
- introducir el modelo de consistencia;
- definir publicación atómica;
- formalizar la trazabilidad;
- establecer seguridad;
- definir gobernanza inicial;
- preparar el pipeline detallado de la Parte II.

---

# Alcance

Esta especificación define la arquitectura conceptual y técnica del Indexing Engine.

Incluye:

- selección de conocimiento indexable;
- transformación de documentos;
- extracción de unidades;
- chunking;
- enriquecimiento;
- embeddings;
- índices léxicos;
- índices vectoriales;
- índices estructurados;
- índices de metadatos;
- índices de grafo;
- snapshots;
- incremental indexing;
- invalidación;
- reconstrucción;
- publicación;
- activación;
- rollback;
- Quality Gates;
- seguridad;
- observabilidad;
- APIs internas;
- eventos.

No constituye por sí misma:

- la implementación concreta de un motor de búsqueda;
- la selección definitiva de una base vectorial;
- la elección de un proveedor de embeddings;
- la configuración exacta de infraestructura;
- una especificación completa del Retrieval Engine;
- una especificación completa de Chunking;
- una especificación completa de Embeddings.

Estos aspectos podrán desarrollarse en documentos derivados.

---

# Definición

Se define el **Indexing Engine** como:

> El subsistema responsable de construir, validar, versionar, publicar, mantener e invalidar representaciones derivadas del conocimiento canónico para permitir su recuperación eficiente y trazable.

---

# Index

Un **Index** será una estructura derivada que permite localizar o recuperar conocimiento mediante una estrategia concreta.

Ejemplos:

```text
Lexical Index
Vector Index
Structured Index
Graph Index
Metadata Index
Temporal Index
```

---

# Indexable Unit

Una **Indexable Unit** será la unidad mínima que el Indexing Engine podrá transformar e incorporar a uno o varios índices.

Ejemplos:

- documento;
- sección;
- bloque;
- párrafo;
- claim;
- statement;
- entidad;
- relación;
- tabla;
- fila;
- procedimiento;
- camino;
- subgrafo;
- resumen.

---

# Index Snapshot

Un **Index Snapshot** será una versión inmutable y coherente de uno o varios índices construidos a partir de un conjunto concreto de snapshots canónicos.

---

# Active Index

Un índice activo será aquel que el Retrieval Engine puede utilizar en producción para resolver consultas.

---

# Candidate Index

Un índice candidato será aquel que:

- ha sido construido;
- aún no está activado;
- debe superar validaciones y Quality Gates.

---

# Historical Index

Un índice histórico será una versión no activa conservada para:

- auditoría;
- rollback;
- reproducibilidad;
- evaluación;
- comparación.

---

# Principios arquitectónicos

Toda implementación del Indexing Engine deberá respetar los siguientes principios.

---

## Derivación, no canonicidad

Los índices no serán la fuente de verdad.

El conocimiento canónico residirá en:

- documentos aprobados;
- componentes;
- statements;
- relaciones;
- Knowledge Graph;
- snapshots oficiales.

---

## Reconstruibilidad

Todo índice deberá poder reconstruirse desde sus fuentes canónicas.

---

## Inmutabilidad de snapshots

Una vez publicado, un snapshot de índice no deberá modificarse.

---

## Publicación explícita

La construcción de un índice no implicará su activación.

---

## Activación atómica

Los consumidores deberán observar:

```text
Snapshot anterior
```

o:

```text
Snapshot nuevo
```

pero no una mezcla parcial de ambos.

---

## Trazabilidad completa

Toda unidad indexada deberá poder resolverse hacia su origen.

---

## Reproducibilidad

La misma entrada, configuración y versión de componentes deberá permitir reconstruir un índice equivalente.

---

## Separación entre construcción y consulta

El proceso de indexación no deberá bloquear ni contaminar las consultas activas.

---

## Versionado explícito

Deberán versionarse:

- pipeline;
- schemas;
- chunking;
- embeddings;
- normalización;
- índices;
- perfiles;
- modelos.

---

## Consistencia entre índices

Los índices que formen un snapshot compuesto deberán representar el mismo estado lógico del conocimiento.

---

## Fail Closed

Un índice incompleto o inválido no deberá activarse.

---

## Seguridad heredada

Las unidades indexadas deberán conservar:

- clasificación;
- tenant;
- ACL;
- restricciones;
- visibilidad.

---

## Filtrado antes de recuperación

La seguridad deberá incorporarse al índice o a sus filtros de acceso, no aplicarse únicamente después de recuperar.

---

## No pérdida semántica silenciosa

Toda transformación deberá preservar:

- negaciones;
- condiciones;
- unidades;
- temporalidad;
- procedencia;
- capa epistemológica.

---

## Incremental por defecto

Cuando sea seguro, deberán procesarse únicamente los cambios.

---

## Full Rebuild disponible

El sistema deberá conservar la capacidad de reconstruir índices completos.

---

## Independencia tecnológica

Los contratos del Indexing Engine no deberán depender de un proveedor concreto.

---

## Observabilidad

Toda indexación deberá ser medible y auditable.

---

## Idempotencia

Reprocesar la misma unidad con la misma configuración no deberá producir duplicados lógicos.

---

## Determinismo controlado

Las fases deterministas deberán producir el mismo resultado.

Las fases probabilísticas deberán registrar:

- modelo;
- versión;
- parámetros;
- seed cuando exista.

---

# Posición dentro de la arquitectura

```text
┌───────────────────────────────────────────────┐
│              Canonical Sources                │
│                                               │
│ Documents · Components · Ontologies · KG      │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Indexing Engine                 │
│                                               │
│ Plan · Extract · Transform · Embed · Build    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Index Snapshots                 │
│                                               │
│ Lexical · Vector · Structured · Graph         │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Retrieval Engine                 │
│                                               │
│ Search · Filter · Rank · Fuse · Retrieve      │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             RAG and Agent Layer               │
│                                               │
│ Context · Generation · Grounding · Tools      │
└───────────────────────────────────────────────┘
```

---

# Relación con el Ingestion Engine

El Ingestion Engine transforma fuentes en Knowledge Packages.

El Indexing Engine transforma conocimiento publicado o autorizado en índices.

---

# Flujo

```text
Source
↓
Ingestion
↓
Knowledge Package
↓
Validation
↓
Publication
↓
Canonical Snapshot
↓
Indexing
```

---

# Regla

Un Knowledge Package no deberá indexarse como conocimiento activo antes de superar:

- validación;
- Quality Gate;
- publicación;
- política de seguridad.

---

# Indexación preliminar

Podrá existir una indexación de preview o staging.

Deberá:

- permanecer aislada;
- declararse experimental;
- no mezclarse con producción;
- conservar clasificación;
- no alimentar respuestas finales sin autorización.

---

# Relación con el Validation Engine

El Validation Engine comprobará:

- conocimiento canónico;
- artefactos de indexación;
- integridad;
- cobertura;
- schemas;
- seguridad;
- consistencia.

---

# Dos niveles de validación

```text
Knowledge Validation
```

comprueba el contenido.

```text
Index Validation
```

comprueba la representación derivada.

---

# Ejemplos de Index Validation

- unidades sin origen;
- embeddings ausentes;
- documentos duplicados;
- metadatos incompletos;
- ACL no propagadas;
- índices inconsistentes;
- conteos divergentes;
- chunking corrupto.

---

# Relación con el Knowledge Graph

El Knowledge Graph proporcionará:

- entidades;
- statements;
- relaciones;
- caminos;
- subgrafos;
- inferencias autorizadas;
- snapshots.

El Indexing Engine podrá construir representaciones optimizadas de estos elementos.

---

# No sustitución del grafo

El índice de grafo no deberá reemplazar al Knowledge Graph canónico.

---

# Relación con el Reasoning Engine

El Reasoning Engine podrá producir inferencias.

Solo las inferencias autorizadas podrán indexarse.

---

# Capa epistemológica

El índice deberá diferenciar:

```text
explicit
validated
derived
inferred
predicted
hypothetical
recommendation
```

---

# No mezcla

Una inferencia no deberá indexarse como hecho explícito.

---

# Relación con el Retrieval Engine

El Retrieval Engine consumirá índices publicados.

---

# Responsabilidad del Indexing Engine

Preparar representaciones recuperables.

---

# Responsabilidad del Retrieval Engine

Seleccionar y combinar resultados para una consulta.

---

# Separación

El Indexing Engine no deberá decidir la respuesta final a una consulta.

---

# Relación con el Motor RAG

El Motor RAG utilizará los índices mediante el Retrieval Engine.

---

# Flujo

```text
RAG Query
↓
Retrieval Plan
↓
Index Selection
↓
Candidate Retrieval
↓
Evidence Selection
↓
Context Assembly
```

---

# Índices como evidencia

Un resultado recuperado desde un índice no constituye por sí mismo evidencia final.

Deberá resolverse hacia:

- fuente;
- fragmento;
- statement;
- relación;
- inferencia;
- documento.

---

# Relación con la API Layer

La API Layer podrá exponer:

- creación de indexaciones;
- jobs;
- snapshots;
- estados;
- activación;
- rollback;
- diagnósticos;
- métricas.

La interacción principal será interna o administrativa.

---

# Responsabilidades del Indexing Engine

Deberá:

- identificar fuentes canónicas indexables;
- construir planes;
- resolver snapshots;
- extraer unidades;
- normalizar contenido;
- segmentar documentos;
- generar metadatos;
- crear embeddings;
- construir índices;
- validar integridad;
- calcular cobertura;
- crear snapshots;
- publicar candidatos;
- activar versiones;
- invalidar unidades;
- reconstruir índices;
- emitir eventos;
- conservar auditoría.

---

# Responsabilidades excluidas

No deberá:

- aprobar conocimiento;
- modificar documentos canónicos;
- resolver conflictos semánticos;
- crear facts sin autorización;
- responder preguntas;
- decidir el ranking final multi-retriever;
- modificar ontologías;
- alterar permisos;
- convertir inferencias en hechos;
- ocultar pérdida de cobertura.

---

# Arquitectura interna

```text
┌───────────────────────────────────────────────┐
│               Indexing Request                │
│                                               │
│ Scope · Profile · Sources · Target            │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                Index Planner                  │
│                                               │
│ Dependencies · Changes · Strategies · Budget  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│           Indexable Unit Extractor            │
│                                               │
│ Documents · Blocks · Statements · Graph       │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│          Transformation Pipeline              │
│                                               │
│ Normalize · Chunk · Enrich · Embed            │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                Index Builders                 │
│                                               │
│ Lexical · Vector · Structured · Graph         │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│           Index Validation Layer              │
│                                               │
│ Coverage · Integrity · Security · Quality     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│           Snapshot and Publication            │
│                                               │
│ Candidate · Activate · Rollback · Retain      │
└───────────────────────────────────────────────┘
```

---

# Componentes principales

---

## Indexing Coordinator

Orquesta la ejecución completa.

---

## Index Planner

Determina:

- alcance;
- estrategia;
- dependencias;
- cambios;
- recursos;
- builders;
- validadores.

---

## Source Resolver

Resuelve los snapshots canónicos de entrada.

---

## Indexable Unit Extractor

Convierte recursos canónicos en unidades indexables.

---

## Normalization Processor

Normaliza texto y metadatos.

---

## Chunking Processor

Segmenta contenido cuando procede.

---

## Enrichment Processor

Añade metadatos y contexto derivados.

---

## Embedding Generator

Produce representaciones vectoriales.

---

## Index Builder

Construye un tipo concreto de índice.

---

## Index Validator

Comprueba calidad e integridad.

---

## Snapshot Manager

Agrupa índices en snapshots coherentes.

---

## Publication Manager

Activa o revierte snapshots.

---

## Invalidation Manager

Determina qué unidades o índices han quedado obsoletos.

---

## Index Registry

Conserva:

- índices;
- versiones;
- estados;
- perfiles;
- compatibilidad;
- propietarios.

---

# Tipos de índice

NovaCoquinaria podrá construir varios tipos complementarios.

---

# Lexical Index

Optimizado para:

- términos exactos;
- frases;
- prefijos;
- tokens;
- stemming;
- campos;
- ranking léxico.

---

# Vector Index

Optimizado para:

- similitud semántica;
- embeddings;
- recuperación aproximada;
- consultas multilingües;
- conceptos relacionados.

---

# Structured Index

Optimizado para:

- filtros;
- atributos;
- rangos;
- enums;
- fechas;
- estados;
- identificadores.

---

# Metadata Index

Optimizado para:

- procedencia;
- seguridad;
- colección;
- idioma;
- versión;
- calidad;
- temporalidad.

---

# Graph Index

Optimizado para:

- vecindarios;
- caminos;
- relaciones;
- comunidades;
- subgrafos;
- GraphRAG.

---

# Statement Index

Optimizado para recuperar afirmaciones estructuradas.

---

# Entity Index

Optimizado para:

- búsqueda de entidades;
- aliases;
- resolución de identidad;
- autocompletado.

---

# Citation Index

Optimizado para resolver:

- fuente;
- bloque;
- línea;
- posición;
- Evidence ID.

---

# Temporal Index

Optimizado para consultas por:

- fecha;
- vigencia;
- snapshot;
- versión;
- estado histórico.

---

# Index Suite

Un **Index Suite** será un conjunto coherente de índices complementarios.

---

# Ejemplo

```text
Recipe Search Suite
    ├── Lexical Index
    ├── Vector Index
    ├── Structured Index
    ├── Metadata Index
    └── Citation Index
```

---

# Index Suite ID

Formato recomendado:

```text
IDX-SUITE-XXXXXX
```

---

# Contrato conceptual

```yaml
index_suite:
  id: IDX-SUITE-RAG-0001

  version: 1.0.0

  indexes:
    - IDX-LEXICAL-0001
    - IDX-VECTOR-0001
    - IDX-STRUCTURED-0001
    - IDX-GRAPH-0001

  status: active
```

---

# Composite Index Snapshot

Un snapshot compuesto podrá agrupar varios índices.

---

# Ejemplo

```yaml
index_snapshot:
  id: IDX-SNAP-20260801-0001

  components:
    lexical: IDX-LEX-SNAP-0001
    vector: IDX-VEC-SNAP-0001
    structured: IDX-STR-SNAP-0001
    graph: IDX-GRAPH-SNAP-0001

  source_snapshots:
    documents: DOC-SNAP-20260801-0001
    knowledge_graph: KG-SNAP-20260801-0004
    ontology: ONT-2.0.0
```

---

# Coherencia de suite

Todos los componentes deberán corresponder a:

- mismo ámbito;
- mismas políticas;
- snapshots compatibles;
- versiones compatibles.

---

# Índices obligatorios y opcionales

Un perfil podrá declarar:

```text
required
optional
disabled
```

para cada tipo de índice.

---

# Ejemplo

```yaml
index_profile:
  lexical: required
  vector: required
  structured: required
  graph: optional
```

---

# Indexing Request

Toda ejecución deberá partir de una solicitud identificada.

Formato recomendado:

```text
IDX-REQ-XXXXXX
```

---

# Contrato mínimo

```yaml
indexing_request:
  id: IDX-REQ-000041

  scope:
    type: repository

  profile:
    id: IDX-PROFILE-STANDARD
```

---

# Contrato ampliado

```yaml
indexing_request:
  id: IDX-REQ-000041

  source_snapshots:
    documents:
      id: DOC-SNAP-20260801-0001

    knowledge_graph:
      id: KG-SNAP-20260801-0004

    ontology:
      id: ONT-2.0.0

  scope:
    type: collection
    ids:
      - COL-RECIPES
      - COL-INGREDIENTS

  profile:
    id: IDX-PROFILE-RAG-STANDARD
    version: 1.0.0

  mode: incremental

  target:
    environment: staging

  options:
    build_lexical: true
    build_vector: true
    build_structured: true
    build_graph: true
    validate: true
    activate: false
```

---

# Indexing Execution

Cada ejecución deberá poseer identidad.

Formato recomendado:

```text
IDX-EXEC-XXXXXX
```

---

# Estados de ejecución

Valores recomendados:

```text
created
planning
resolving_sources
extracting_units
normalizing
chunking
enriching
embedding
building_indexes
validating
creating_snapshot
ready_for_activation
activating
completed
completed_with_warnings
partial
paused
retrying
failed
cancelled
blocked
```

---

# Indexing Job

La ejecución podrá estar asociada a un Job común.

---

# Indexing Execution DTO conceptual

```yaml
indexing_execution:
  id: IDX-EXEC-000041

  request: IDX-REQ-000041

  status: building_indexes
  phase: vector_index

  progress:
    completed: 780
    total: 1000
    percentage: 78

  started_at: 2026-08-01T20:00:00+02:00

  target_snapshot:
    id: IDX-SNAP-20260801-0001
```

---

# Modos de indexación

---

## Full

Reconstruye todo el ámbito.

---

## Incremental

Procesa únicamente cambios.

---

## Selective

Procesa recursos seleccionados.

---

## Repair

Corrige unidades o particiones defectuosas.

---

## Rebuild

Reconstruye un índice concreto.

---

## Preview

Genera un índice aislado para pruebas.

---

## Migration

Transforma índices entre versiones incompatibles.

---

## Replay

Reconstruye a partir de eventos o snapshots históricos.

---

# Full Indexing

Adecuado cuando:

- cambia el schema;
- cambia el chunking;
- cambia el embedding model;
- cambia la normalización;
- existe corrupción;
- se introduce un nuevo tipo de índice.

---

# Incremental Indexing

Adecuado cuando:

- cambian pocos recursos;
- el schema sigue siendo compatible;
- las dependencias pueden calcularse;
- la invalidación es precisa.

---

# Selective Indexing

Podrá utilizarse para:

- colección;
- documento;
- entidad;
- tenant;
- idioma;
- recurso.

---

# Preview Index

No deberá recibir tráfico productivo.

---

# Repair Indexing

Deberá conservar evidencia de:

- causa;
- unidades afectadas;
- correcciones;
- resultado.

---

# Ámbitos de indexación

Valores iniciales:

```text
document
collection
repository
knowledge_package
knowledge_graph
subgraph
tenant
environment
snapshot
resource_set
```

---

# Document Scope

Procesa uno o varios documentos.

---

# Collection Scope

Procesa una colección.

---

# Repository Scope

Procesa todo el repositorio documental.

---

# Knowledge Package Scope

Procesa un paquete publicado.

---

# Knowledge Graph Scope

Procesa el snapshot completo del grafo.

---

# Subgraph Scope

Procesa una sección del grafo.

---

# Tenant Scope

Procesa el conocimiento de un tenant.

---

# Snapshot Scope

Reconstruye un estado histórico.

---

# Resource Set

Procesa una lista explícita.

---

# Indexing Profile

Un **Indexing Profile** definirá la configuración gobernada del pipeline.

Formato recomendado:

```text
IDX-PROFILE-XXXXXX
```

---

# Contenido

- fuentes;
- unidades;
- normalización;
- chunking;
- embeddings;
- índices;
- validación;
- seguridad;
- publicación;
- límites.

---

# Perfiles iniciales

```text
basic
standard
strict
rag
graphrag
search
preview
migration
audit
```

---

# Perfil `basic`

- documentos;
- campos básicos;
- índice léxico;
- metadatos mínimos.

---

# Perfil `standard`

- índice léxico;
- estructurado;
- metadatos;
- incremental;
- validación.

---

# Perfil `strict`

- procedencia completa;
- seguridad;
- Quality Gates;
- fail-closed;
- cobertura completa.

---

# Perfil `rag`

- chunks;
- embeddings;
- citas;
- metadata;
- lexical + vector.

---

# Perfil `graphrag`

- entidades;
- statements;
- caminos;
- subgrafos;
- summaries;
- índices de grafo.

---

# Perfil `search`

- documentos completos;
- facetas;
- autocompletado;
- filtros;
- ranking lexical.

---

# Perfil `preview`

- entorno aislado;
- retención corta;
- no activable en producción.

---

# Perfil `migration`

- compatibilidad;
- transformaciones;
- validación dual;
- rollback.

---

# Perfil `audit`

- artefactos completos;
- decisiones;
- hashes;
- mappings;
- métricas.

---

# Contrato de perfil

```yaml
indexing_profile:
  id: IDX-PROFILE-RAG-STANDARD

  version: 1.0.0
  status: active

  units:
    - document_section
    - paragraph
    - statement
    - entity

  processors:
    normalization: NORM-PROFILE-0001
    chunking: CHUNK-PROFILE-0001
    embeddings: EMB-PROFILE-0001

  indexes:
    lexical: required
    vector: required
    structured: required
    graph: optional

  quality_gate:
    id: QG-INDEX-RAG-0001
```

---

# Perfil inmutable por ejecución

Una ejecución deberá conservar la versión exacta del perfil.

---

# No configuración libre sin gobernanza

Los consumidores no deberán enviar directamente parámetros arbitrarios de:

- chunk size;
- embedding model;
- analyzer;
- index schema;
- graph depth;

salvo APIs administrativas autorizadas.

---

# Indexing Plan

Antes de ejecutar deberá existir un plan.

Formato recomendado:

```text
IDX-PLAN-XXXXXX
```

---

# Objetivos

El plan deberá definir:

- fuentes;
- snapshots;
- ámbito;
- cambios;
- unidades;
- dependencias;
- procesadores;
- índices;
- presupuesto;
- validadores;
- estrategia de publicación.

---

# Contrato

```yaml
indexing_plan:
  id: IDX-PLAN-000041

  request: IDX-REQ-000041

  mode: incremental

  source_snapshots:
    documents: DOC-SNAP-20260801-0001
    knowledge_graph: KG-SNAP-20260801-0004

  changes:
    created: 12
    updated: 7
    deleted: 2
    impacted: 31

  processors:
    - normalize
    - chunk
    - enrich
    - embed

  builders:
    - lexical
    - vector
    - structured
    - graph

  estimated:
    units: 320
    embeddings: 280
    duration_ms: 42000

  activation:
    automatic: false
```

---

# Plan determinista

La misma entrada y configuración deberá producir el mismo plan cuando no cambien:

- snapshots;
- políticas;
- dependencias;
- schemas;
- perfiles.

---

# Plan stale

Un plan quedará obsoleto si cambia:

- snapshot fuente;
- perfil;
- schema;
- modelo;
- permisos;
- scope;
- índice activo.

---

# Error conceptual

```text
INDEXING_PLAN_STALE
```

---

# Plan Approval

Los planes de alto impacto podrán requerir aprobación.

Ejemplos:

- full rebuild;
- production activation;
- cambio de embedding model;
- migración;
- eliminación masiva.

---

# Indexable Source

Una fuente indexable deberá declarar:

- tipo;
- snapshot;
- estado;
- clasificación;
- tenant;
- version;
- procedencia.

---

# Tipos de fuente indexable

```text
document
component
entity
statement
relation
inference
collection
table
procedure
graph_path
subgraph
summary
```

---

# Indexable Resource Contract

```yaml
indexable_resource:
  id: REC-0009
  type: recipe

  snapshot:
    id: DOC-SNAP-20260801-0001

  status: published

  classification:
    level: internal

  tenant:
    id: TENANT-0001
```

---

# Elegibilidad de indexación

Un recurso deberá cumplir:

- estado permitido;
- snapshot válido;
- permisos;
- schema;
- Quality Gate;
- no estar invalidado;
- no estar en cuarentena.

---

# Recursos no indexables

Ejemplos:

```text
draft
rejected
quarantined
invalidated
deleted
restricted_without_policy
```

---

# Excepciones

Un perfil de preview podrá indexar borradores en un índice aislado.

---

# Canonical Pointer

Toda unidad deberá conservar un puntero canónico.

---

# Contrato conceptual

```yaml
canonical_pointer:
  resource:
    id: REC-0009
    type: recipe

  document:
    id: DOC-0051

  location:
    block: BLOCK-00041

  snapshot:
    id: DOC-SNAP-20260801-0001
```

---

# Indexable Unit ID

Formato recomendado:

```text
IDX-UNIT-XXXXXX
```

---

# Identidad lógica y física

Deberá distinguirse:

```text
logical_unit_id
```

de:

```text
physical_record_id
```

---

# Logical Unit ID

Permanece estable mientras la unidad represente el mismo elemento lógico.

---

# Physical Record ID

Puede cambiar entre snapshots o proveedores.

---

# Ejemplo

```yaml
indexable_unit:
  id: IDX-UNIT-000041

  logical_key: DOC-0051#BLOCK-00041

  physical_record:
    id: vector-record-84721
```

---

# Content Hash

Toda unidad deberá disponer de hash de contenido cuando proceda.

---

# Objetivos

- detectar cambios;
- deduplicar;
- verificar integridad;
- reutilizar embeddings;
- identificar drift.

---

# Ejemplo

```yaml
content_hash:
  algorithm: sha256
  value: ...
```

---

# Transformation Hash

Además del contenido, podrá calcularse un hash que incluya:

- normalización;
- chunking;
- schema;
- embedding profile.

---

# Indexing Fingerprint

```text
content
+
profile
+
processor versions
+
model version
```

---

# Uso

Permite saber si una unidad debe reprocesarse.

---

# Index Entry

Un **Index Entry** será la representación incorporada a un índice concreto.

---

# Tipos

```text
lexical_entry
vector_entry
structured_entry
graph_entry
metadata_entry
citation_entry
```

---

# Contrato conceptual

```yaml
index_entry:
  id: IDX-ENTRY-000041

  unit: IDX-UNIT-000041
  index_type: vector

  index_snapshot:
    id: IDX-VEC-SNAP-0001

  status: active
```

---

# Relación cardinal

Una unidad podrá producir:

- cero entradas;
- una entrada;
- varias entradas;

según el índice.

---

# Ejemplo

Una sección podrá producir:

```text
1 lexical entry
3 vector chunks
1 metadata entry
2 graph entries
```

---

# No equivalencia entre chunk e index entry

Un chunk es una unidad semántica.

Una entrada es su representación en un índice concreto.

---

# Index Schema

Cada índice deberá utilizar un schema versionado.

Formato recomendado:

```text
IDX-SCHEMA-XXXXXX
```

---

# Contrato

```yaml
index_schema:
  id: IDX-SCHEMA-VECTOR-RAG

  version: 1.0.0
  status: active

  fields:
    - id
    - text
    - embedding
    - resource_id
    - document_id
    - block_id
    - classification
    - tenant_id
    - snapshot_id
```

---

# Schema Compatibility

Los cambios deberán clasificarse.

---

# Cambio compatible

- nuevo campo opcional;
- nuevo metadata;
- nuevo analyzer secundario;
- nueva vista.

---

# Cambio incompatible

- cambio de dimensión vectorial;
- eliminación de campo;
- cambio de tipo;
- cambio de tokenizer;
- cambio de semántica;
- cambio de partition key.

---

# Nueva versión de índice

Un cambio incompatible deberá producir:

- nuevo schema;
- nuevo índice;
- nuevo snapshot;
- validación;
- activación explícita.

---

# Index Registry

El Index Registry conservará información de todos los índices.

---

# Contenido

- ID;
- tipo;
- schema;
- versión;
- estado;
- owner;
- perfil;
- snapshots;
- compatibilidad;
- retención;
- consumidor.

---

# Index Record

```yaml
index:
  id: IDX-VECTOR-RAG-0001

  type: vector
  schema: IDX-SCHEMA-VECTOR-RAG@1.0.0

  status: active

  owner:
    team: ai-platform

  current_snapshot:
    id: IDX-VEC-SNAP-0001
```

---

# Estados de índice

```text
draft
building
candidate
validating
ready
active
degraded
stale
deprecated
retired
failed
```

---

# Draft

Definido, todavía no construido.

---

# Building

En construcción.

---

# Candidate

Construido, pendiente de validación.

---

# Ready

Validado y preparado para activación.

---

# Active

Disponible para retrieval.

---

# Degraded

Disponible con limitaciones.

---

# Stale

No representa el último estado canónico.

---

# Deprecated

Debe migrarse.

---

# Retired

No debe recibir consultas.

---

# Index Snapshot

Todo snapshot deberá ser inmutable.

---

# Identidad

Formato recomendado:

```text
IDX-SNAP-YYYYMMDD-NNNN
```

o:

```text
IDX-SNAP-XXXXXX
```

---

# Contrato ampliado

```yaml
index_snapshot:
  id: IDX-SNAP-20260801-0001

  suite:
    id: IDX-SUITE-RAG-0001

  status: candidate

  created_from:
    documents: DOC-SNAP-20260801-0001
    knowledge_graph: KG-SNAP-20260801-0004
    ontology: ONT-2.0.0

  pipeline:
    id: IDX-PIPELINE-RAG-0001
    version: 1.0.0

  profile:
    id: IDX-PROFILE-RAG-STANDARD
    version: 1.0.0

  components:
    lexical: IDX-LEX-SNAP-0001
    vector: IDX-VEC-SNAP-0001
    structured: IDX-STR-SNAP-0001
    graph: IDX-GRAPH-SNAP-0001

  metrics:
    units: 12450
    entries: 31280
```

---

# Snapshot Status

```text
building
candidate
validating
ready
active
superseded
rolled_back
stale
invalidated
retired
failed
```

---

# Snapshot Lineage

Todo snapshot deberá conservar su linaje.

---

# Ejemplo

```yaml
lineage:
  parent_snapshot: IDX-SNAP-20260725-0003
  change_set: CHANGESET-000041
  execution: IDX-EXEC-000041
```

---

# Snapshot completo e incremental

Un snapshot incremental deberá representar un estado lógico completo, aunque físicamente reutilice estructuras anteriores.

---

# No delta como vista activa incompleta

El Retrieval Engine deberá consultar una vista coherente.

---

# Snapshot Activation

La activación deberá ser una operación explícita.

---

# Precondiciones

- Quality Gate aprobado;
- índices completos;
- schema compatible;
- seguridad validada;
- cobertura suficiente;
- aliases o pointers preparados;
- rollback disponible.

---

# Activation Record

Formato recomendado:

```text
IDX-ACTIVATION-XXXXXX
```

---

# Contrato

```yaml
index_activation:
  id: IDX-ACTIVATION-000041

  snapshot:
    id: IDX-SNAP-20260801-0001

  previous_snapshot:
    id: IDX-SNAP-20260725-0003

  environment: production

  status: completed

  activated_at: 2026-08-01T22:00:00+02:00
```

---

# Alias o Logical Pointer

Los consumidores deberán utilizar un identificador lógico.

Ejemplo:

```text
rag-active
```

en lugar de un nombre físico concreto.

---

# Beneficios

- activación atómica;
- rollback;
- desacoplamiento;
- blue-green indexing.

---

# Blue-Green Indexing

Podrán coexistir:

```text
Blue Index
```

activo y:

```text
Green Index
```

candidato.

---

# Flujo

```text
Build Green
↓
Validate Green
↓
Switch Alias
↓
Monitor
↓
Retain Blue for Rollback
```

---

# Rollback

Deberá poder reactivarse un snapshot anterior compatible.

---

# Rollback Conditions

- snapshot anterior disponible;
- schema compatible;
- políticas válidas;
- datos no eliminados;
- seguridad preservada.

---

# Rollback Record

Deberá registrar:

- motivo;
- actor;
- snapshot origen;
- snapshot destino;
- fecha;
- impacto.

---

# No rollback silencioso

Toda reversión deberá emitir:

- evento;
- auditoría;
- alerta;
- actualización de estado.

---

# Consistencia

El Indexing Engine deberá declarar el modelo de consistencia.

---

# Canonical Consistency

Un índice puede retrasarse respecto al conocimiento canónico.

---

# Estados de frescura

```text
current
updating
stale
unknown
unavailable
```

---

# Freshness Metadata

```yaml
freshness:
  status: current
  source_snapshot: DOC-SNAP-20260801-0001
  indexed_at: 2026-08-01T20:30:00+02:00
  lag_seconds: 0
```

---

# Eventual Consistency

Será aceptable para:

- búsquedas;
- índices vectoriales;
- facetas;
- proyecciones.

---

# Strong Consistency

Podrá requerirse para:

- permisos;
- eliminación;
- publicación crítica;
- datos restringidos;
- tenant isolation.

---

# Security-Critical Invalidation

Cuando cambie un permiso o clasificación, la invalidación deberá priorizarse.

---

# No serving stale restricted data

Un índice stale no deberá seguir exponiendo contenido que ha perdido autorización.

---

# Tombstone

La eliminación podrá representarse mediante una marca de invalidación.

---

# Uso

- evitar resurrección;
- sincronizar réplicas;
- mantener historial;
- invalidar cachés.

---

# Tombstone Contract

```yaml
tombstone:
  resource:
    id: DOC-0051
    type: document

  invalidated_at: 2026-08-01T20:00:00Z

  reason: resource_deleted
```

---

# Retención de tombstones

Deberá ser suficiente para que todos los consumidores procesen la eliminación.

---

# Seguridad

La seguridad deberá integrarse desde la construcción.

---

# Metadata mínima de seguridad

Toda entrada deberá incluir:

- tenant;
- clasificación;
- visibilidad;
- ACL o política;
- resource owner cuando proceda.

---

# Security Trimming

El Retrieval Engine deberá poder limitar resultados según permisos.

---

# Estrategias

```text
pre-filtering
post-filtering
document-level ACL
field-level ACL
partition isolation
tenant isolation
```

---

# Recomendación

Priorizar:

```text
pre-filtering
```

o particiones seguras.

---

# Riesgo del post-filtering

Puede:

- recuperar contenido no autorizado;
- enviarlo al modelo;
- exponerlo en logs;
- alterar ranking;
- permitir inferencias.

---

# Security Hash

Los cambios de seguridad deberán alterar el fingerprint de indexación.

---

# Security Reindex

Un cambio de ACL podrá requerir:

- actualización de metadata;
- movimiento entre particiones;
- eliminación;
- rebuild.

---

# Encryption

Los índices deberán cifrarse:

- en tránsito;
- en reposo;
- en backups.

---

# Embeddings sensibles

Los vectores deberán heredar la clasificación de su contenido.

---

# No índice compartido inseguro

Los contenidos de tenants o clasificaciones incompatibles no deberán mezclarse sin filtros garantizados.

---

# Data Minimization

Los índices deberán contener únicamente los campos necesarios para retrieval.

---

# No secrets

No deberán indexarse:

- credenciales;
- tokens;
- claves;
- secretos;
- prompts internos;
- configuraciones sensibles.

---

# Secret Detection

La fase de indexación deberá poder bloquear contenido sospechoso aunque haya superado otras fases por error.

---

# Redaction

Podrá generarse una versión indexable redaccionada distinta del contenido canónico.

---

# Trazabilidad de redacción

Deberá conservar:

- política;
- campos eliminados;
- versión;
- actor o sistema;
- hash.

---

# Gobernanza

Todo índice deberá disponer de owner.

---

# Roles posibles

- Knowledge Platform;
- Search Platform;
- AI Platform;
- Security;
- Data Governance.

---

# Index Owner

Será responsable de:

- schema;
- disponibilidad;
- calidad;
- costes;
- deprecación;
- seguridad;
- consumidores.

---

# Pipeline Owner

Podrá diferir del owner del índice.

---

# Model Owner

Los modelos de embeddings deberán disponer de owner específico.

---

# Consumer Registry

Deberán registrarse consumidores conocidos.

Ejemplos:

- Retrieval Engine;
- RAG Engine;
- Search UI;
- Agent Tools;
- Analytics.

---

# Impact Analysis

Antes de modificar un índice deberá analizarse:

- consumidores;
- queries;
- schemas;
- SDKs;
- costes;
- latencia;
- compatibilidad.

---

# Quality Gate conceptual

Ningún snapshot deberá activarse sin superar un Gate.

---

# Criterios iniciales

```yaml
quality_gate:
  id: QG-INDEX-CANDIDATE-0001

  criteria:
    all:
      - source_snapshots_resolved == true
      - orphan_units == 0
      - missing_security_metadata == 0
      - duplicate_logical_units == 0
      - schema_validation_passed == true
      - required_indexes_completed == true
      - critical_diagnostics == 0
```

---

# Métricas iniciales

- recursos fuente;
- unidades extraídas;
- chunks;
- embeddings;
- entradas;
- errores;
- duplicados;
- huérfanos;
- cobertura;
- duración;
- tamaño.

---

# Index Coverage

La cobertura mide qué proporción del conocimiento elegible está representado.

---

# Fórmula conceptual

```text
indexed_eligible_units
/
total_eligible_units
```

---

# Cobertura por tipo

Podrá calcularse para:

- documentos;
- entidades;
- statements;
- relaciones;
- colecciones;
- idiomas;
- tenants.

---

# Coverage Gap

Todo gap deberá explicar:

- recurso;
- motivo;
- severidad;
- reintentabilidad.

---

# Index Integrity

La integridad deberá comprobar:

- IDs;
- hashes;
- referencias;
- schemas;
- counts;
- security metadata;
- snapshots;
- mappings.

---

# Index Drift

Existe drift cuando la representación activa diverge de:

- conocimiento canónico;
- configuración;
- schema;
- modelo esperado.

---

# Drift Detection

Podrá utilizar:

- hashes;
- muestreo;
- conteos;
- queries de control;
- comparación de snapshots.

---

# Indexing Events

El motor deberá emitir eventos.

---

# Catálogo inicial

```text
indexing_requested
indexing_started
indexing_plan_created
indexable_units_extracted
embedding_generation_started
index_build_completed
index_validation_completed
index_snapshot_ready
index_snapshot_activated
index_snapshot_rolled_back
indexing_failed
index_unit_invalidated
```

---

# Evento de activación

```yaml
event:
  type: index_snapshot_activated

  subject:
    id: IDX-SNAP-20260801-0001
    type: index-snapshot

  data:
    previous_snapshot: IDX-SNAP-20260725-0003
    environment: production
```

---

# Idempotencia

La indexación deberá utilizar claves lógicas.

---

# Idempotency Key conceptual

Podrá derivarse de:

```text
source snapshot
+
profile version
+
scope
+
mode
+
target
```

---

# Ejecución duplicada

La misma solicitud podrá:

- devolver ejecución existente;
- reutilizar snapshot;
- crear nueva ejecución sin duplicar entradas;

según política.

---

# Concurrencia

No deberán activarse simultáneamente snapshots incompatibles para el mismo alias.

---

# Lock lógico

La activación podrá utilizar un bloqueo o compare-and-swap.

---

# Concurrent Builds

Sí podrán existir múltiples builds aislados.

---

# Prioridad

Podrán priorizarse:

- cambios de seguridad;
- eliminaciones;
- contenido crítico;
- hotfixes;
- indexaciones regulares.

---

# Presupuesto

Toda ejecución deberá declarar límites.

---

# Tipos

```text
maximum_units
maximum_embeddings
maximum_duration
maximum_cost
maximum_memory
maximum_storage
maximum_parallelism
```

---

# Ejemplo

```yaml
budget:
  maximum_units: 50000
  maximum_embeddings: 40000
  maximum_duration: PT30M
  maximum_parallelism: 8
```

---

# Budget Exceeded

La ejecución deberá:

- pausar;
- fallar;
- producir parcial;
- solicitar aprobación;

según perfil.

---

# No activación parcial silenciosa

Un resultado parcial no deberá activarse como completo.

---

# Resiliencia

El Indexing Engine deberá tolerar:

- fallos de worker;
- timeouts;
- proveedor de embeddings no disponible;
- errores de almacenamiento;
- eventos duplicados;
- reinicios.

---

# Checkpoints

Las fases largas deberán poder crear checkpoints.

---

# Reanudación

Solo deberá realizarse si:

- configuración compatible;
- snapshot fuente vigente;
- artefactos íntegros;
- seguridad sin cambios incompatibles.

---

# Indexing Checkpoint

Formato recomendado:

```text
IDX-CHK-XXXXXX
```

---

# Contrato

```yaml
indexing_checkpoint:
  id: IDX-CHK-000041

  execution: IDX-EXEC-000041

  stage: embedding

  last_processed_unit: IDX-UNIT-000780

  status: valid
```

---

# Reintentos

Deberán distinguir:

- error de unidad;
- error de lote;
- error de dependencia;
- error estructural.

---

# Poison Unit

Una unidad que falla repetidamente podrá aislarse.

---

# Quarantine

Las unidades problemáticas deberán:

- quedar registradas;
- no desaparecer;
- generar diagnóstico;
- bloquear si son obligatorias.

---

# Partial Index

Podrá generarse para análisis, pero deberá declararse:

```text
partial
```

---

# No producción con Partial Index

Salvo un perfil de degradación explícitamente aprobado.

---

# Observabilidad inicial

Toda ejecución deberá generar:

- logs;
- métricas;
- traces;
- eventos;
- auditoría.

---

# Log estructurado

```yaml
log:
  event: indexing_execution_started
  execution: IDX-EXEC-000041
  profile: IDX-PROFILE-RAG-STANDARD
  mode: incremental
  scope: collection
```

---

# Métricas RED

- rate;
- errors;
- duration.

---

# Métricas específicas

- units per second;
- embeddings per second;
- index size;
- build duration;
- activation duration;
- lag;
- duplicate ratio;
- failure ratio.

---

# Tracing

Flujo:

```text
Indexing Request
↓
Plan
↓
Source Resolution
↓
Extraction
↓
Transformation
↓
Embedding
↓
Build
↓
Validation
↓
Activation
```

---

# Auditoría

Deberán auditarse:

- full rebuild;
- activation;
- rollback;
- schema change;
- model change;
- security reindex;
- deletion;
- migration.

---

# Perfil mínimo de implementación

La primera versión podrá incluir:

- documentos Markdown;
- secciones;
- índice léxico;
- metadata básica;
- index snapshot;
- full rebuild;
- activación por alias;
- validación básica;
- eventos;
- logs.

---

# Perfil RAG inicial

Añadirá:

- chunks;
- embeddings;
- vector index;
- Citation Index;
- incremental updates;
- security metadata.

---

# Perfil GraphRAG

Añadirá:

- entidades;
- statements;
- relaciones;
- paths;
- subgraphs;
- graph summaries.

---

# Perfil avanzado

Añadirá:

- multi-tenant;
- dual indexing;
- semantic cache;
- migrations;
- blue-green;
- continuous evaluation.

---

# Perfil enterprise

Añadirá:

- alta disponibilidad;
- multi-region;
- SLOs;
- DR;
- governance;
- cost controls;
- policy engine.

---

# Implementación inicial recomendada

La primera implementación práctica podrá seguir:

```text
Published Markdown
        ↓
Parse Sections
        ↓
Create Indexable Units
        ↓
Normalize Text
        ↓
Build Lexical Index
        ↓
Create Snapshot
        ↓
Validate
        ↓
Switch Active Alias
```

---

# Segunda iteración

```text
Indexable Units
        ↓
Chunk
        ↓
Generate Embeddings
        ↓
Build Vector Index
        ↓
Attach Provenance
        ↓
Validate
        ↓
Activate Composite Snapshot
```

---

# No será necesario inicialmente

- múltiples proveedores vectoriales;
- multi-region;
- adaptive chunking basado en LLM;
- graph communities;
- online indexing continuo;
- learned sparse retrieval;
- multimodal embeddings;
- automatic model routing;
- distributed compaction;
- index federation.

---

# Caso de uso 1 — Full rebuild

Se modifica el schema de chunks.

El sistema deberá:

- crear plan;
- reconstruir;
- validar;
- generar snapshot candidato;
- activar atómicamente;
- conservar rollback.

---

# Caso de uso 2 — Documento actualizado

Cambia una receta.

El sistema deberá:

- detectar hash;
- invalidar unidades afectadas;
- generar nuevos chunks;
- recalcular embeddings;
- actualizar índices;
- publicar nuevo snapshot.

---

# Caso de uso 3 — Documento eliminado

El recurso se elimina.

El sistema deberá:

- crear tombstone;
- eliminar o invalidar entradas;
- actualizar Citation Index;
- impedir recuperación;
- propagar evento.

---

# Caso de uso 4 — Cambio de ACL

Un documento pasa de `internal` a `restricted`.

El sistema deberá:

- priorizar invalidación;
- actualizar metadata;
- asegurar que no puede recuperarse con permisos antiguos;
- invalidar cachés;
- auditar.

---

# Caso de uso 5 — Modelo de embeddings nuevo

Cambia la dimensión vectorial.

El sistema deberá:

- crear nuevo schema;
- construir nuevo índice;
- evaluar calidad;
- activar por alias;
- conservar índice anterior.

---

# Caso de uso 6 — Build parcial fallido

Falla la generación de embeddings para varias unidades.

El snapshot deberá quedar:

```text
partial
```

y no activarse bajo perfil estricto.

---

# Caso de uso 7 — Preview

Un editor quiere probar búsqueda sobre un borrador.

El sistema construye un índice aislado con:

- scope limitado;
- retención corta;
- sin publicación productiva.

---

# Caso de uso 8 — Rollback

Tras activar un nuevo índice disminuye la calidad de retrieval.

La plataforma reactiva el snapshot anterior.

---

# Caso de uso 9 — GraphRAG

Se publica un nuevo snapshot del Knowledge Graph.

El Indexing Engine construye:

- Entity Index;
- Statement Index;
- Path Index;
- Graph Summary Index.

---

# Caso de uso 10 — Reproducibilidad

Una auditoría solicita reconstruir el índice usado por una respuesta histórica.

El sistema utiliza:

- source snapshots;
- pipeline version;
- profile;
- embedding model;
- index schema.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Tratar el índice como fuente canónica

Los índices son derivados.

---

## Modificar un snapshot activo

Destruye reproducibilidad.

---

## Mezclar registros de distintos snapshots sin control

Produce respuestas inconsistentes.

---

## Activar durante la construcción

Los consumidores pueden observar datos parciales.

---

## Reindexar todo ante cualquier cambio

Aumenta coste y latencia.

---

## Indexación incremental sin dependencias

Puede dejar contenido stale.

---

## Eliminar entradas sin tombstone

Puede provocar resurrección.

---

## No registrar versión de modelo

Impide reproducibilidad.

---

## Reutilizar embeddings con otra normalización

Puede producir inconsistencias.

---

## Mezclar hechos e inferencias

Destruye la capa epistemológica.

---

## Perder procedencia durante chunking

Impide citas.

---

## Recuperar primero y filtrar permisos después

Puede exponer contenido.

---

## Compartir índice entre tenants sin aislamiento

Compromete seguridad.

---

## Indexar secretos

Amplía su exposición.

---

## Truncar contenido sin registrar pérdida

Oculta degradación.

---

## Considerar un build completado como válido

Debe superar Quality Gate.

---

## Activar un snapshot parcial

Puede generar respuestas incompletas.

---

## Cambiar schema en el mismo índice físico

Rompe compatibilidad.

---

## Sobrescribir índices históricos

Impide rollback.

---

## Crear IDs físicos como IDs canónicos

Acopla al proveedor.

---

## No versionar perfiles

Impide reconstruir resultados.

---

## No medir cobertura

Oculta recursos ausentes.

---

## Ignorar drift

El índice puede divergir silenciosamente.

---

## No priorizar cambios de seguridad

Puede mantener exposición indebida.

---

## Full rebuild sin rollback

Aumenta riesgo operativo.

---

## Reanudar con snapshot fuente distinto

Rompe coherencia.

---

## Mantener previews indefinidamente

Aumenta coste y exposición.

---

## Permitir configuración arbitraria desde consumidores

Reduce gobernanza.

---

# Reglas mínimas de conformidad

---

## Índice derivado

Todo índice deberá enlazar con fuentes canónicas.

---

## Snapshot inmutable

Toda versión publicada deberá ser inmutable.

---

## Schema versionado

Todo índice deberá declarar schema y versión.

---

## Perfil identificado

Toda ejecución deberá utilizar un perfil versionado.

---

## Plan explícito

Toda ejecución compleja deberá disponer de plan.

---

## Trazabilidad de unidad

Toda entrada deberá resolver hacia su recurso original.

---

## Seguridad propagada

Tenant, clasificación y permisos deberán conservarse.

---

## Cobertura medida

Toda ejecución deberá calcular cobertura.

---

## Quality Gate

Ningún snapshot deberá activarse sin validación.

---

## Activación atómica

Los consumidores no deberán observar mezclas parciales.

---

## Rollback disponible

Las activaciones críticas deberán conservar una versión anterior.

---

## Idempotencia

Reprocesar la misma entrada no deberá duplicar resultados lógicos.

---

## Invalidación

Los cambios y eliminaciones deberán propagarse.

---

## Observabilidad

Toda ejecución deberá producir logs, métricas y trazas.

---

## Reproducibilidad

Deberán conservarse versiones de pipeline, perfiles y modelos.

---

# Conformidad de Indexing Request

Será conforme cuando:

- tenga ID;
- declare scope;
- declare perfil;
- resuelva snapshots;
- declare modo;
- declare target;
- defina opciones;
- respete permisos.

---

# Conformidad de Indexing Plan

Será conforme cuando:

- identifique request;
- declare fuentes;
- declare cambios;
- declare procesadores;
- declare builders;
- declare presupuesto;
- declare validación;
- tenga hash.

---

# Conformidad de Indexable Unit

Será conforme cuando:

- tenga identidad;
- declare tipo;
- conserve puntero canónico;
- tenga hash;
- conserve seguridad;
- declare snapshot;
- pueda invalidarse.

---

# Conformidad de Index Entry

Será conforme cuando:

- identifique unidad;
- identifique índice;
- declare schema;
- conserve metadata;
- conserve procedencia;
- pertenezca a un snapshot.

---

# Conformidad de Index Snapshot

Será conforme cuando:

- tenga identidad;
- sea inmutable;
- declare fuentes;
- declare pipeline;
- declare perfil;
- declare componentes;
- declare métricas;
- supere Gate;
- conserve lineage.

---

# Conformidad de activación

Será conforme cuando:

- identifique snapshot;
- identifique entorno;
- declare versión anterior;
- sea atómica;
- preserve rollback;
- genere auditoría;
- emita evento.

---

# Lista de comprobación

Antes de aprobar una arquitectura o ejecución de indexación deberá comprobarse:

```text
[ ] Las fuentes canónicas están identificadas.
[ ] Los snapshots fuente están fijados.
[ ] El scope está definido.
[ ] El modo de indexación está declarado.
[ ] El perfil está versionado.
[ ] El plan está identificado.
[ ] Las unidades indexables están tipadas.
[ ] Cada unidad conserva puntero canónico.
[ ] Los hashes están calculados.
[ ] Los procesadores están versionados.
[ ] Los índices requeridos están declarados.
[ ] Los schemas están versionados.
[ ] La seguridad se ha propagado.
[ ] El tenant está presente cuando proceda.
[ ] La capa epistemológica está preservada.
[ ] La cobertura está calculada.
[ ] Los duplicados están controlados.
[ ] Los huérfanos están detectados.
[ ] La invalidación está definida.
[ ] Los tombstones están considerados.
[ ] El snapshot es inmutable.
[ ] El Quality Gate se ha ejecutado.
[ ] La activación será atómica.
[ ] Existe rollback.
[ ] Los eventos están definidos.
[ ] La observabilidad está disponible.
[ ] La auditoría está configurada.
[ ] La reproducibilidad está garantizada.
```

---

# Arquitectura final de la Parte I

```text
Canonical Knowledge
        ↓
Indexing Request
        ↓
Indexing Plan
        ↓
Indexable Unit Extraction
        ↓
Transformation Pipeline
        ↓
Index Builders
        ↓
Index Validation
        ↓
Candidate Snapshot
        ↓
Quality Gate
        ↓
Atomic Activation
        ↓
Retrieval Consumption
```

---

# Transición hacia la Parte II

Esta primera parte ha definido:

- la misión del Indexing Engine;
- el concepto de índice derivado;
- las unidades indexables;
- los snapshots;
- los índices activos, candidatos e históricos;
- los principios arquitectónicos;
- la posición dentro del SGCC;
- la relación con Ingesta, Validación, Knowledge Graph, Reasoning, Retrieval y RAG;
- las responsabilidades;
- la arquitectura interna;
- los componentes;
- los tipos de índice;
- las Index Suites;
- las solicitudes;
- las ejecuciones;
- los modos;
- los ámbitos;
- los perfiles;
- los planes;
- las fuentes indexables;
- la elegibilidad;
- los punteros canónicos;
- los hashes;
- las entradas;
- los schemas;
- el Registry;
- los snapshots;
- la activación;
- el rollback;
- la consistencia;
- los tombstones;
- la seguridad;
- la gobernanza;
- los Quality Gates iniciales;
- la idempotencia;
- la resiliencia;
- los checkpoints;
- los eventos;
- la observabilidad;
- la implementación inicial;
- los antipatrones;
- las reglas de conformidad.

La Parte II desarrollará el pipeline de indexación y las unidades indexables en detalle, incluyendo:

- resolución de fuentes;
- selección de recursos;
- análisis de cambios;
- extracción;
- normalización;
- parsing;
- tipado;
- segmentación lógica;
- unidades documentales;
- unidades semánticas;
- unidades estructuradas;
- unidades de grafo;
- deduplicación;
- lineage;
- fingerprints;
- dependencias;
- artefactos intermedios;
- checkpoints;
- manejo de errores;
- contratos de cada etapa.

---

# Conclusión

El Indexing Engine constituye el puente operativo entre el conocimiento canónico y los mecanismos de recuperación.

Su función no consiste únicamente en insertar documentos en una base de búsqueda.

Deberá transformar conocimiento validado en representaciones:

- eficientes;
- coherentes;
- versionadas;
- seguras;
- reconstruibles;
- trazables.

El ciclo fundamental puede resumirse así:

```text
Seleccionar conocimiento
        ↓
Planificar
        ↓
Extraer unidades
        ↓
Transformar
        ↓
Construir índices
        ↓
Validar
        ↓
Crear snapshot
        ↓
Activar
        ↓
Monitorizar
        ↓
Invalidar o reconstruir
```

La selección determina qué conocimiento puede indexarse.

El plan define cómo se procesará.

Las unidades establecen la granularidad.

Las transformaciones preparan el contenido.

Los builders construyen representaciones especializadas.

La validación comprueba integridad y cobertura.

El snapshot preserva coherencia.

La activación evita estados parciales.

El rollback reduce riesgo.

La invalidación mantiene actualidad.

La trazabilidad permite volver siempre al conocimiento original.

Un índice correcto deberá poder responder:

```text
¿Qué conocimiento representa?

¿De qué snapshot procede?

¿Qué pipeline lo construyó?

¿Qué perfil utilizó?

¿Qué modelo produjo sus embeddings?

¿Qué unidades contiene?

¿Qué seguridad hereda?

¿Qué Quality Gate superó?

¿Cuándo fue activado?

¿A qué versión puede revertirse?
```

Con esta primera parte queda establecida la arquitectura general del Indexing Engine de NovaCoquinaria.

La siguiente parte formalizará el pipeline mediante el que documentos, statements, entidades, relaciones y subgrafos se convierten en unidades indexables gobernadas.

---

# Parte II — Pipeline de indexación y modelo detallado de unidades indexables

---

# Introducción

La Parte I ha definido:

- la misión del Indexing Engine;
- los índices como representaciones derivadas;
- las unidades indexables;
- los Index Snapshots;
- los perfiles;
- los planes;
- los tipos de índice;
- la activación;
- el rollback;
- la seguridad;
- la gobernanza;
- la relación con el resto del SGCC.

Esta segunda parte desarrolla el flujo mediante el que los recursos canónicos se transforman en unidades indexables gobernadas.

El objetivo no consiste únicamente en extraer texto.

El pipeline deberá identificar y preservar:

- estructura;
- semántica;
- identidad;
- procedencia;
- dependencias;
- clasificación;
- temporalidad;
- capa epistemológica;
- contexto suficiente para recuperación.

Conceptualmente:

```text
Canonical Snapshots
        ↓
Source Resolution
        ↓
Eligibility Evaluation
        ↓
Change Analysis
        ↓
Resource Extraction
        ↓
Parsing
        ↓
Normalization
        ↓
Logical Segmentation
        ↓
Indexable Unit Construction
        ↓
Enrichment
        ↓
Deduplication
        ↓
Dependency Resolution
        ↓
Unit Validation
        ↓
Transformation Artifacts
```

Las unidades producidas por esta fase constituirán la entrada de:

- chunking;
- generación de embeddings;
- builders léxicos;
- builders estructurados;
- builders de grafo;
- Citation Index;
- Metadata Index.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- formalizar el pipeline de indexación;
- definir sus etapas;
- establecer contratos de entrada y salida;
- resolver snapshots canónicos;
- determinar elegibilidad;
- analizar cambios;
- definir unidades documentales;
- definir unidades semánticas;
- definir unidades estructuradas;
- definir unidades de grafo;
- preservar procedencia;
- formalizar parsing;
- establecer normalización;
- definir segmentación lógica;
- conservar contexto;
- establecer deduplicación;
- formalizar fingerprints;
- resolver dependencias;
- generar artefactos intermedios;
- establecer checkpoints;
- manejar errores;
- definir Quality Gates por etapa;
- establecer reglas de conformidad.

---

# Principios del pipeline

---

## Etapas explícitas

Cada transformación deberá pertenecer a una etapa identificable.

---

## Contratos entre etapas

La salida de una etapa deberá cumplir un contrato antes de utilizarse como entrada de la siguiente.

---

## No mutación silenciosa

Toda transformación relevante deberá registrarse.

---

## Preservación del original

El pipeline deberá conservar referencias suficientes para reconstruir el contenido original.

---

## Reejecución selectiva

Las etapas deberán poder repetirse sin reiniciar todo el proceso cuando sus dependencias permanezcan válidas.

---

## Idempotencia

La misma entrada y configuración deberán producir las mismas unidades lógicas.

---

## Lineage completo

Cada artefacto deberá declarar:

- origen;
- etapa;
- procesador;
- versión;
- ejecución;
- snapshot.

---

## Seguridad desde la fuente

La clasificación y el tenant deberán propagarse desde la resolución inicial.

---

## Separación entre segmentación y chunking

La segmentación lógica identifica unidades del dominio.

El chunking posterior podrá dividirlas para retrieval o embeddings.

---

## No pérdida de estructura

La normalización textual no deberá destruir:

- títulos;
- listas;
- tablas;
- pasos;
- bloques;
- relaciones;
- referencias.

---

## Fallos localizables

Un error en una unidad deberá poder aislarse sin ocultar su impacto sobre el conjunto.

---

## Dependencias explícitas

Toda unidad derivada deberá declarar de qué recursos depende.

---

## Procesamiento gobernado

Los procesadores deberán estar registrados y versionados.

---

# Pipeline general

```text
┌───────────────────────────────────────────────┐
│              Canonical Snapshots              │
│                                               │
│ Documents · KG · Ontology · Collections       │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Source Resolution               │
│                                               │
│ Snapshot · Scope · Security · Availability    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Eligibility Evaluation            │
│                                               │
│ Status · Gates · Policy · Classification      │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Change Analysis                 │
│                                               │
│ Create · Update · Delete · Impact · Reuse     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Resource Extraction               │
│                                               │
│ Documents · Statements · Entities · Relations │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Parsing and Normalization         │
│                                               │
│ Structure · Text · Fields · References        │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Logical Segmentation              │
│                                               │
│ Sections · Procedures · Tables · Graph Units  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│         Indexable Unit Construction           │
│                                               │
│ Identity · Content · Metadata · Lineage       │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│        Enrichment and Dependency Model        │
│                                               │
│ Context · Aliases · Relations · Impact        │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│         Deduplication and Validation          │
│                                               │
│ Fingerprints · Conflicts · Quality Gates      │
└───────────────────────────────────────────────┘
```

---

# Indexing Pipeline

Todo pipeline deberá poseer identidad y versión.

Formato recomendado:

```text
IDX-PIPELINE-XXXXXX
```

---

# Contrato

```yaml
indexing_pipeline:
  id: IDX-PIPELINE-RAG-0001

  version: 1.0.0
  status: active

  stages:
    - source_resolution
    - eligibility
    - change_analysis
    - extraction
    - parsing
    - normalization
    - logical_segmentation
    - unit_construction
    - enrichment
    - deduplication
    - dependency_resolution
    - validation

  profile_compatibility:
    - IDX-PROFILE-RAG-STANDARD
    - IDX-PROFILE-GRAPHRAG
```

---

# Estados de pipeline

```text
draft
experimental
active
deprecated
retired
```

---

# Pipeline Definition Hash

Toda versión deberá disponer de un hash que represente:

- etapas;
- orden;
- procesadores;
- versiones;
- configuración.

---

# Processor Registry

Cada procesador deberá registrarse.

---

# Processor ID

Formato recomendado:

```text
IDX-PROC-XXXXXX
```

---

# Contrato

```yaml
processor:
  id: IDX-PROC-MARKDOWN-PARSER

  version: 1.0.0
  stage: parsing
  status: active

  input_types:
    - markdown_document

  output_types:
    - parsed_document
```

---

# Propiedades del procesador

Deberá declarar:

- determinismo;
- idempotencia;
- consumo;
- dependencias;
- límites;
- errores;
- propietario.

---

# Processor Execution

Cada invocación podrá poseer identidad.

Formato recomendado:

```text
IDX-PROC-EXEC-XXXXXX
```

---

# Contrato

```yaml
processor_execution:
  id: IDX-PROC-EXEC-000041

  processor:
    id: IDX-PROC-MARKDOWN-PARSER
    version: 1.0.0

  indexing_execution:
    id: IDX-EXEC-000041

  input_artifact:
    id: IDX-ART-000041

  output_artifact:
    id: IDX-ART-000042

  status: completed
```

---

# Stage Result

Toda etapa deberá producir un resultado.

---

# Contrato

```yaml
stage_result:
  stage: parsing
  status: completed

  input_count: 120
  output_count: 120

  diagnostics:
    errors: 0
    warnings: 2

  duration_ms: 420
```

---

# Estados de etapa

```text
pending
running
completed
completed_with_warnings
partial
failed
skipped
cancelled
blocked
```

---

# Etapa omitida

Solo podrá marcarse `skipped` cuando:

- el perfil la deshabilite;
- no aplique;
- pueda reutilizarse un artefacto válido.

---

# Reutilización de resultados

Una etapa podrá reutilizar resultados anteriores cuando coincidan:

- input hash;
- processor version;
- configuration hash;
- security hash;
- schema version.

---

# Reuse Decision

```yaml
reuse_decision:
  status: reused

  source_artifact:
    id: IDX-ART-000021

  reasons:
    - input_hash_unchanged
    - processor_version_unchanged
    - security_metadata_unchanged
```

---

# Artefacto intermedio

Un **Indexing Artifact** representa una salida persistida entre etapas.

Formato recomendado:

```text
IDX-ART-XXXXXX
```

---

# Tipos de artefacto

```text
resolved_source
change_set
parsed_document
normalized_document
logical_segment
indexable_unit_set
enriched_unit_set
dependency_graph
deduplication_report
validation_report
```

---

# Contrato

```yaml
indexing_artifact:
  id: IDX-ART-000041

  type: parsed_document
  schema: IDX-ART-SCHEMA-PARSED-DOC@1.0.0

  execution:
    id: IDX-EXEC-000041

  created_by:
    processor: IDX-PROC-MARKDOWN-PARSER@1.0.0

  input_artifacts:
    - IDX-ART-000040

  checksum:
    algorithm: sha256
    value: ...

  status: valid
```

---

# Estados de artefacto

```text
building
valid
invalid
stale
quarantined
expired
deleted
```

---

# Retención de artefactos

La retención dependerá de:

- perfil;
- entorno;
- criticidad;
- reproducibilidad;
- coste;
- auditoría.

---

# Artefactos de auditoría

El perfil `audit` podrá conservar todas las salidas intermedias.

---

# Artefactos de producción

Podrán conservarse únicamente:

- los necesarios para rollback;
- los necesarios para invalidación;
- los exigidos por trazabilidad.

---

# Primera etapa — Resolución de fuentes

La etapa `source_resolution` determina qué conocimiento canónico se utilizará.

---

# Source Resolution Request

```yaml
source_resolution_request:
  execution: IDX-EXEC-000041

  source_snapshots:
    documents: DOC-SNAP-20260801-0001
    knowledge_graph: KG-SNAP-20260801-0004
    ontology: ONT-2.0.0

  scope:
    type: collection
    ids:
      - COL-RECIPES
```

---

# Responsabilidades

- verificar existencia;
- verificar estado;
- verificar compatibilidad;
- fijar versiones;
- resolver referencias;
- aplicar tenant;
- aplicar clasificación;
- obtener manifests;
- bloquear fuentes inválidas.

---

# Source Manifest

Cada snapshot deberá proporcionar un manifest.

---

# Contrato

```yaml
source_manifest:
  snapshot:
    id: DOC-SNAP-20260801-0001

  resources:
    total: 129

  by_type:
    recipe: 42
    ingredient: 18
    technique: 11

  checksum:
    algorithm: sha256
    value: ...

  classification:
    maximum_level: internal
```

---

# Verificaciones

- snapshot inmutable;
- checksum;
- schema;
- publicación;
- Quality Gate;
- tenant;
- compatibilidad temporal.

---

# Snapshot incompatible

Ejemplo:

```text
Ontology snapshot older than document schema.
```

Error:

```text
INDEX_SOURCE_SNAPSHOT_INCOMPATIBLE
```

---

# Snapshot no autorizado

Error:

```text
INDEX_SOURCE_ACCESS_DENIED
```

---

# Source Resolution Result

```yaml
source_resolution_result:
  status: resolved

  resolved:
    documents: DOC-SNAP-20260801-0001
    knowledge_graph: KG-SNAP-20260801-0004
    ontology: ONT-2.0.0

  manifest:
    resources: 129

  security_context:
    tenant: TENANT-0001
    maximum_classification: internal
```

---

# Segunda etapa — Evaluación de elegibilidad

La etapa `eligibility` determina qué recursos pueden indexarse.

---

# Eligibility Rule

Toda regla deberá poseer identidad.

Formato recomendado:

```text
IDX-ELIG-RULE-XXXXXX
```

---

# Ejemplo

```yaml
eligibility_rule:
  id: IDX-ELIG-RULE-PUBLISHED

  condition:
    resource.status:
      in:
        - published
        - validated

  decision: eligible
```

---

# Señales de elegibilidad

- estado;
- Quality Gate;
- clasificación;
- tenant;
- tipo;
- idioma;
- vigencia;
- licencia;
- cuarentena;
- policy;
- scope.

---

# Decisiones

```text
eligible
ineligible
conditionally_eligible
preview_only
quarantined
unknown
```

---

# Conditionally Eligible

Podrá indexarse únicamente en:

- staging;
- preview;
- sandbox;
- tenant restringido.

---

# Eligibility Result

```yaml
eligibility_result:
  resource:
    id: REC-0009
    type: recipe

  decision: eligible

  rules:
    - IDX-ELIG-RULE-PUBLISHED
    - IDX-ELIG-RULE-SECURITY-ALLOWED
```

---

# Recurso ineligible

Deberá conservar:

- motivo;
- regla;
- severidad;
- posibilidad de reintento.

---

# Ejemplo

```yaml
eligibility_result:
  resource:
    id: REC-0042
    type: recipe

  decision: ineligible

  reason:
    code: RESOURCE_NOT_PUBLISHED
```

---

# Eligibility Coverage

Deberá calcularse:

```text
eligible
ineligible
quarantined
unknown
```

---

# Unknown

Bajo perfil estricto deberá bloquear.

---

# Tercera etapa — Análisis de cambios

La etapa `change_analysis` determina qué debe procesarse.

---

# Entradas

- snapshot actual;
- snapshot anterior;
- Change Set;
- manifests;
- hashes;
- dependency graph;
- active index snapshot.

---

# Tipos de cambio

```text
created
updated
deleted
renamed
moved
security_changed
classification_changed
dependency_changed
unchanged
```

---

# Cambio directo

Afecta al recurso modificado.

---

# Cambio indirecto

Afecta a recursos dependientes.

Ejemplo:

```text
Ingredient updated
↓
Recipes using ingredient impacted
```

---

# Change Analysis Result

```yaml
change_analysis:
  baseline:
    index_snapshot: IDX-SNAP-20260725-0003

  source_snapshot:
    id: DOC-SNAP-20260801-0001

  direct:
    created: 12
    updated: 7
    deleted: 2

  indirect:
    impacted: 31

  unchanged:
    reusable: 845
```

---

# Change Detection Strategies

```text
manifest_diff
content_hash
semantic_hash
revision
event_log
dependency_diff
security_hash
```

---

# Content Hash

Detecta cambios textuales o estructurales representados.

---

# Semantic Hash

Puede ignorar diferencias sin impacto semántico.

Ejemplo:

- espacios;
- formato;
- comentarios no indexables.

---

# Security Hash

Detecta cambios en:

- ACL;
- clasificación;
- tenant;
- visibilidad.

---

# Processor Hash

Detecta cambios de configuración que obligan a reprocesar aunque la fuente no cambie.

---

# Impact Analysis

Deberá calcular dependencias afectadas.

---

# Impact Types

```text
content
citation
entity_resolution
relation
embedding
security
ranking
graph
```

---

# Ejemplo

Cambiar el nombre preferido de un ingrediente puede afectar:

- Entity Index;
- lexical aliases;
- recipe summaries;
- embeddings contextuales;
- Citation Index.

---

# Change Graph

Podrá construirse un grafo temporal de impacto.

---

# Change Decision

Por unidad:

```text
create
rebuild
reuse
invalidate
delete
move
security_update
```

---

# Reuse

Solo cuando todas las dependencias sean compatibles.

---

# Change Analysis Error

Si no puede determinarse el impacto:

```text
INDEX_CHANGE_IMPACT_INDETERMINATE
```

Bajo perfil estricto deberá ampliar el scope o ejecutar full rebuild.

---

# Cuarta etapa — Extracción de recursos

La etapa `extraction` recupera representaciones canónicas.

---

# Resource Extractor

Podrá existir un extractor por tipo.

---

# Tipos

```text
DocumentExtractor
ComponentExtractor
StatementExtractor
EntityExtractor
RelationExtractor
TableExtractor
GraphExtractor
CollectionExtractor
```

---

# Extractor Contract

```yaml
extractor:
  id: IDX-EXTRACTOR-DOCUMENT

  version: 1.0.0

  source_type: document
  output_type: document_source_record
```

---

# Source Record

Representa el recurso todavía sin transformar.

---

# Contrato

```yaml
source_record:
  id: IDX-SOURCE-REC-000041

  canonical_resource:
    id: REC-0009
    type: recipe

  snapshot:
    id: DOC-SNAP-20260801-0001

  content:
    format: markdown

  security:
    tenant: TENANT-0001
    classification: internal

  checksum:
    algorithm: sha256
    value: ...
```

---

# Extracción documental

Deberá recuperar:

- Front Matter;
- cuerpo;
- headings;
- bloques;
- enlaces;
- tablas;
- listas;
- code blocks;
- posiciones;
- encoding.

---

# Extracción de componentes

Deberá recuperar:

- identidad;
- tipo;
- propiedades;
- referencias;
- relaciones;
- constraints.

---

# Extracción de Statements

Deberá recuperar:

- subject;
- predicate;
- object;
- qualifiers;
- negation;
- temporalidad;
- epistemic layer;
- provenance.

---

# Extracción de relaciones

Deberá recuperar:

- tipo;
- origen;
- destino;
- dirección;
- cardinalidad;
- propiedades;
- vigencia.

---

# Extracción de tablas

Deberá preservar:

- encabezados;
- filas;
- columnas;
- unidades;
- notas;
- merges;
- posición.

---

# Extracción de procedimientos

Deberá preservar:

- orden;
- pasos;
- precondiciones;
- tiempos;
- advertencias;
- dependencias.

---

# Extracción de grafo

Podrá producir:

- nodos;
- aristas;
- paths;
- neighborhoods;
- communities;
- summaries autorizados.

---

# Extracción parcial

No deberá presentarse como completa.

---

# Extraction Result

```yaml
extraction_result:
  status: completed

  resources:
    requested: 129
    extracted: 128
    failed: 1

  diagnostics:
    - code: RESOURCE_CONTENT_UNAVAILABLE
      target: DOC-0042
```

---

# Quinta etapa — Parsing

El parsing transforma contenido crudo en una estructura formal.

---

# Parser Types

```text
markdown
yaml
json
csv
html
plain_text
graph
table
```

---

# Parsed Document

```yaml
parsed_document:
  id: IDX-PARSED-DOC-000041

  source_record:
    id: IDX-SOURCE-REC-000041

  front_matter:
    id: REC-0009
    type: recipe
    status: published

  structure:
    headings:
      - id: H-001
        level: 1
        text: Sopa de miso

    blocks:
      - id: BLOCK-00041
        type: paragraph

  references:
    - target: ING-0008
      type: ingredient
```

---

# Parsing Preservation

Deberá conservar:

- offset original;
- línea;
- columna;
- bloque;
- jerarquía;
- fuente.

---

# Parser Diagnostics

Ejemplos:

```text
MALFORMED_FRONT_MATTER
UNBALANCED_MARKDOWN_STRUCTURE
INVALID_TABLE
UNRESOLVED_REFERENCE_SYNTAX
INVALID_ENCODING
```

---

# Error recuperable

Podrá producir una unidad parcial solo si el perfil lo permite.

---

# Parser Version

Toda unidad deberá registrar qué parser se utilizó.

---

# Sexta etapa — Normalización

La normalización prepara el contenido sin alterar su significado.

---

# Objetivos

- estabilizar representación;
- facilitar deduplicación;
- unificar campos;
- preparar búsqueda;
- mantener significado.

---

# Normalization Profile

Formato recomendado:

```text
NORM-PROFILE-XXXXXX
```

---

# Contrato

```yaml
normalization_profile:
  id: NORM-PROFILE-SPANISH-0001

  version: 1.0.0

  operations:
    - unicode_normalization
    - whitespace_normalization
    - line_ending_normalization
    - canonical_field_mapping
```

---

# Operaciones posibles

```text
unicode_normalization
whitespace_normalization
line_ending_normalization
case_normalization
punctuation_normalization
unit_normalization
date_normalization
identifier_normalization
language_detection
canonical_field_mapping
```

---

# Operaciones prohibidas sin trazabilidad

- eliminar negaciones;
- eliminar unidades;
- reescribir contenido;
- resumir;
- traducir;
- corregir hechos;
- expandir abreviaturas ambiguas.

---

# Texto original y normalizado

Deberán conservarse por separado.

---

# Contrato

```yaml
normalized_content:
  original: "Añadir 1 cda. de miso."
  normalized: "Añadir 1 cucharada de miso."

  transformations:
    - type: abbreviation_expansion
      rule: ABBR-CULINARY-0001
      confidence: 1.0
```

---

# Expansión ambigua

No deberá aplicarse automáticamente sin regla o confianza suficiente.

---

# Normalización de IDs

Deberá preservar la forma canónica.

---

# Normalización de unidades

Podrá producir:

```yaml
quantity:
  original:
    value: 1
    unit: cucharada

  canonical:
    value: 15
    unit: ml

  conversion:
    approximate: true
```

---

# Regla

El contenido indexable podrá incorporar ambas formas:

- original;
- canónica.

---

# Normalización lingüística

Podrá incluir:

- idioma;
- locale;
- script;
- token hints.

---

# No stemming en la fuente normalizada

El stemming deberá pertenecer al builder léxico, no destruir la representación base.

---

# Séptima etapa — Segmentación lógica

La segmentación lógica identifica unidades coherentes del dominio.

---

# Diferencia con chunking

```text
Logical Segmentation
```

preserva unidades estructurales y semánticas.

```text
Chunking
```

puede dividirlas o agruparlas para retrieval y embeddings.

---

# Logical Segment

Formato recomendado:

```text
IDX-SEG-XXXXXX
```

---

# Contrato

```yaml
logical_segment:
  id: IDX-SEG-000041

  type: procedure_step

  canonical_pointer:
    resource: REC-0009
    document: DOC-0051
    block: BLOCK-00041

  hierarchy:
    parent: IDX-SEG-000040
    order: 3

  content:
    original: Añadir el miso al final.
    normalized: Añadir el miso al final.
```

---

# Tipos de segmento

```text
document
front_matter
title
section
subsection
paragraph
list
list_item
procedure
procedure_step
table
table_row
table_cell
definition
warning
note
example
statement
entity
relation
graph_path
subgraph
summary
```

---

# Segmentación por estructura

Utiliza:

- headings;
- listas;
- bloques;
- tablas;
- delimitadores;
- componentes.

---

# Segmentación por dominio

Ejemplos:

- ingrediente;
- paso;
- tiempo;
- temperatura;
- sustitución;
- alérgeno;
- advertencia.

---

# Segmentación de recetas

Podrá producir:

```text
Recipe Metadata
Recipe Description
Ingredients List
Ingredient Item
Preparation Procedure
Procedure Step
Serving Notes
Safety Notes
Sources
```

---

# Segmentación de ingredientes

Podrá producir:

```text
Definition
Aliases
Properties
Uses
Compatibility
Allergens
Storage
Sources
```

---

# Segmentación de tablas

Podrá generar:

- tabla completa;
- fila;
- grupo de filas;
- celda contextualizada.

---

# Segmentación de procedimientos

Deberá conservar orden.

---

# Segment Order

```yaml
order:
  sequence: 4
  total: 12
```

---

# Segment Context

Podrá incluir contexto mínimo heredado.

---

# Ejemplo

```yaml
context:
  document_title: Sopa de miso
  section_title: Preparación
  entity_id: REC-0009
```

---

# No duplicación contextual excesiva

El contexto deberá permitir comprensión sin inflar innecesariamente el índice.

---

# Segment Boundary

Deberá registrar por qué se creó el límite.

```yaml
boundary:
  strategy: structural
  reason: heading_change
```

---

# Octava etapa — Construcción de unidades indexables

Las unidades indexables constituyen el principal resultado del pipeline.

---

# Indexable Unit Contract

```yaml
indexable_unit:
  id: IDX-UNIT-000041

  logical_key: REC-0009#PREPARATION#STEP-03

  type: procedure_step

  canonical_pointer:
    resource:
      id: REC-0009
      type: recipe

    document:
      id: DOC-0051

    segment:
      id: IDX-SEG-000041

    snapshot:
      id: DOC-SNAP-20260801-0001

  content:
    original: Añadir el miso al final.
    normalized: Añadir el miso al final.
    language: es

  hierarchy:
    parent_unit: IDX-UNIT-000040
    order: 3

  epistemic_layer: explicit

  security:
    tenant: TENANT-0001
    classification: internal

  hashes:
    content: ...
    transformation: ...

  status: ready
```

---

# Campos mínimos

Toda unidad deberá incluir:

- ID;
- logical key;
- tipo;
- puntero canónico;
- contenido o estructura;
- snapshot;
- seguridad;
- hash;
- estado.

---

# Tipos principales de unidad

---

## Document Unit

Representa un documento completo.

---

## Section Unit

Representa una sección jerárquica.

---

## Paragraph Unit

Representa un párrafo.

---

## Procedure Unit

Representa un procedimiento completo.

---

## Procedure Step Unit

Representa un paso.

---

## Table Unit

Representa una tabla.

---

## Table Row Unit

Representa una fila contextualizada.

---

## Statement Unit

Representa una afirmación estructurada.

---

## Entity Unit

Representa una entidad.

---

## Relation Unit

Representa una relación.

---

## Graph Path Unit

Representa un camino.

---

## Subgraph Unit

Representa un subgrafo.

---

## Summary Unit

Representa un resumen derivado y autorizado.

---

## Citation Unit

Representa una localización citable.

---

# Unidad documental

```yaml
indexable_unit:
  id: IDX-UNIT-DOC-000041
  type: document

  content:
    title: Sopa de miso
    text: ...

  metadata:
    document_type: recipe
    status: published
```

---

# Unidad de sección

```yaml
indexable_unit:
  id: IDX-UNIT-SEC-000041
  type: section

  content:
    heading: Preparación
    text: ...

  hierarchy:
    level: 2
```

---

# Unidad de Statement

```yaml
indexable_unit:
  id: IDX-UNIT-STM-000041
  type: statement

  statement:
    subject: REC-0009
    predicate: usesIngredient
    object: ING-0008

  epistemic_layer: validated
```

---

# Unidad de entidad

```yaml
indexable_unit:
  id: IDX-UNIT-ENT-000041
  type: entity

  entity:
    id: ING-0008
    entity_type: ingredient
    preferred_label: Miso
    aliases:
      - pasta de miso
```

---

# Unidad de relación

```yaml
indexable_unit:
  id: IDX-UNIT-REL-000041
  type: relation

  relation:
    source: REC-0009
    type: usesIngredient
    target: ING-0008
```

---

# Unidad de path

```yaml
indexable_unit:
  id: IDX-UNIT-PATH-000041
  type: graph_path

  path:
    nodes:
      - REC-0009
      - ING-0008
      - ALG-SOY

    relations:
      - usesIngredient
      - containsAllergen
```

---

# Unidad de tabla

Deberá conservar:

- tabla;
- encabezados;
- contexto;
- posición.

---

# Unidad de fila

```yaml
indexable_unit:
  id: IDX-UNIT-ROW-000041
  type: table_row

  context:
    table_title: Tiempos de cocción

  row:
    ingredient: Garbanzo
    time: PT45M
```

---

# Unidad de procedimiento

Deberá conservar todos los pasos y sus dependencias.

---

# Unidad de paso

Deberá conservar:

- paso;
- orden;
- procedimiento;
- precondiciones;
- resultados;
- advertencias.

---

# Unidades compuestas

Una unidad podrá agrupar otras cuando:

- el contexto sea necesario;
- la consulta requiera visión global;
- el perfil lo permita.

---

# Composite Unit

```yaml
composite_unit:
  id: IDX-UNIT-COMP-000041

  type: recipe_overview

  members:
    - IDX-UNIT-META-000041
    - IDX-UNIT-ING-000041
    - IDX-UNIT-PROC-000041
```

---

# Unidad atómica

Una unidad atómica no deberá dividirse lógicamente sin perder significado.

Ejemplos:

- statement;
- relación;
- celda con encabezados;
- constraint;
- claim.

---

# Unidad contextual

Incluye información heredada necesaria para comprenderla.

---

# Context Inheritance

Los segmentos podrán heredar:

- título;
- tipo;
- entidad;
- colección;
- sección;
- idioma;
- clasificación.

---

# Regla

El contexto heredado deberá distinguirse del contenido original.

---

# Context Block

```yaml
context:
  inherited:
    recipe_title: Sopa de miso
    section_title: Preparación

  original:
    text: Añadir el miso al final.
```

---

# Unidad derivada

Deberá declarar cómo fue generada.

---

# Derived Unit

```yaml
derived_from:
  units:
    - IDX-UNIT-000041
    - IDX-UNIT-000042

  processor:
    id: IDX-PROC-SUMMARIZER
    version: 1.0.0
```

---

# Capa epistemológica

Toda unidad deberá declarar una capa cuando contenga conocimiento.

Valores:

```text
explicit
validated
derived
inferred
predicted
hypothetical
recommendation
```

---

# Unidad predicted

No deberá mezclarse con facts.

---

# Indexability Status

Valores recomendados:

```text
candidate
ready
excluded
quarantined
invalid
stale
deleted
```

---

# Excluded

La unidad existe, pero el perfil no la indexará.

---

# Invalid

No cumple el contrato.

---

# Stale

Su fuente o dependencia cambió.

---

# Novena etapa — Enriquecimiento

El enriquecimiento añade contexto derivado sin sustituir al conocimiento original.

---

# Enrichment Processor

Podrá añadir:

- aliases;
- labels;
- categorías;
- relaciones;
- keywords;
- contexto jerárquico;
- resoluciones de identidad;
- propiedades calculadas;
- citas;
- idioma;
- quality metadata.

---

# Enrichment Types

```text
structural
semantic
graph
linguistic
security
citation
quality
temporal
```

---

# Enriquecimiento estructural

Añade:

- parent;
- siblings;
- section path;
- document type;
- order.

---

# Enriquecimiento semántico

Añade:

- entity IDs;
- ontology classes;
- concepts;
- normalized predicates.

---

# Enriquecimiento de grafo

Añade:

- neighbors;
- path summaries;
- relation counts;
- community IDs.

---

# Enriquecimiento lingüístico

Añade:

- idioma;
- tokens auxiliares;
- aliases multilingües;
- transliteraciones.

---

# Enriquecimiento de seguridad

Añade:

- tenant;
- ACL;
- classification;
- visibility;
- policy reference.

---

# Enriquecimiento de citas

Añade:

- document;
- block;
- line;
- section;
- source URI;
- Evidence ID.

---

# Enrichment Record

```yaml
enrichment:
  unit: IDX-UNIT-000041

  additions:
    entity_ids:
      - ING-0008

    section_path:
      - Sopa de miso
      - Preparación

    citation:
      document: DOC-0051
      block: BLOCK-00041

  processor:
    id: IDX-PROC-SEMANTIC-ENRICHER
    version: 1.0.0
```

---

# Enriquecimiento no autorizado

No deberá crear facts nuevos sin pasar por el flujo de conocimiento.

---

# Regla

El enriquecimiento indexable podrá mejorar recuperación, pero no deberá modificar el contenido canónico.

---

# Enrichment Confidence

Los enriquecimientos probabilísticos deberán declarar confianza.

---

# Threshold

El perfil deberá definir si:

- se acepta;
- se revisa;
- se excluye.

---

# Décima etapa — Deduplicación

La deduplicación evita múltiples representaciones lógicamente equivalentes no justificadas.

---

# Tipos de duplicado

```text
exact
normalized
semantic
structural
cross_source
version
```

---

# Exact Duplicate

Mismo contenido y metadata relevante.

---

# Normalized Duplicate

Distinto formato, mismo contenido normalizado.

---

# Semantic Duplicate

Contenido diferente con significado equivalente.

---

# Structural Duplicate

La misma unidad aparece varias veces por parsing o extracción.

---

# Cross-Source Duplicate

La misma información procede de fuentes diferentes.

---

# Version Duplicate

Versiones equivalentes sin cambios indexables.

---

# Deduplication Key

Podrá considerar:

- logical key;
- content hash;
- canonical pointer;
- type;
- snapshot;
- tenant;
- security hash.

---

# Deduplication Result

```yaml
deduplication_result:
  unit: IDX-UNIT-000041

  status: canonical

  duplicates:
    - IDX-UNIT-000042

  strategy: same_logical_key_same_hash
```

---

# Decisiones

```text
keep
merge
link
exclude
conflict
```

---

# Keep

Las unidades son similares, pero deben conservarse.

---

# Merge

Puede producirse una unidad compuesta gobernada.

---

# Link

Se conservan ambas y se relacionan.

---

# Exclude

Se elimina de la salida indexable, manteniendo trazabilidad.

---

# Conflict

Las unidades parecen duplicadas, pero difieren de forma incompatible.

---

# Duplicados con distinta seguridad

No deberán fusionarse de forma que amplíe acceso.

---

# Duplicados con distinta procedencia

La procedencia múltiple deberá preservarse.

---

# Evidencias independientes

No deberán perderse por deduplicación.

---

# Semantic Deduplication

Deberá utilizar umbrales gobernados.

No deberá eliminar automáticamente conocimiento por similitud vectorial.

---

# Deduplication Report

```yaml
deduplication_report:
  total_units: 12450
  exact_duplicates: 82
  linked_duplicates: 17
  conflicts: 2
```

---

# Undécima etapa — Fingerprints

Los fingerprints determinan identidad de procesamiento y reutilización.

---

# Tipos

```text
content_fingerprint
structure_fingerprint
security_fingerprint
dependency_fingerprint
transformation_fingerprint
embedding_fingerprint
```

---

# Content Fingerprint

Incluye contenido normalizado relevante.

---

# Structure Fingerprint

Incluye:

- jerarquía;
- orden;
- tipo;
- contexto.

---

# Security Fingerprint

Incluye:

- tenant;
- clasificación;
- ACL;
- visibility.

---

# Dependency Fingerprint

Incluye hashes de dependencias.

---

# Transformation Fingerprint

Incluye:

- processor versions;
- profile;
- configuration;
- schemas.

---

# Embedding Fingerprint

Se detallará en la Parte III.

---

# Composite Fingerprint

```text
content
+
structure
+
security
+
dependencies
+
transformations
```

---

# Fingerprint Contract

```yaml
fingerprints:
  content: ...
  structure: ...
  security: ...
  dependencies: ...
  transformation: ...
  composite: ...
```

---

# Reutilización segura

Solo podrá reutilizarse una salida cuando el fingerprint relevante coincida.

---

# Duodécima etapa — Resolución de dependencias

Las unidades indexables pueden depender de otros recursos.

---

# Dependency Types

```text
contains
references
uses
derived_from
requires
inherits_context
depends_on_schema
depends_on_ontology
depends_on_security
```

---

# Dependency Record

```yaml
dependency:
  source:
    id: IDX-UNIT-000041

  type: references

  target:
    id: ING-0008
    type: ingredient

  impact:
    lexical: true
    vector: true
    graph: true
```

---

# Unit Dependency Graph

El pipeline deberá construir un grafo de dependencias.

---

# Usos

- incremental indexing;
- invalidación;
- impacto;
- orden de procesamiento;
- reutilización;
- rollback.

---

# Dependencias directas

Ejemplo:

```text
Recipe Unit
↓
Ingredient Unit
```

---

# Dependencias transitivas

Ejemplo:

```text
Recipe
↓
Ingredient
↓
Allergen
```

---

# Dependency Depth

El perfil podrá limitar la expansión.

---

# Dependency Cycle

Los ciclos deberán detectarse.

---

# Cycles válidos

Algunas relaciones de grafo podrán ser cíclicas.

No deberán confundirse con ciclos de procesamiento imposibles.

---

# Processing Dependency

Define orden de ejecución.

---

# Semantic Dependency

Define impacto semántico.

---

# Security Dependency

Define propagación de permisos o clasificación.

---

# Missing Dependency

Deberá producir diagnóstico.

```text
INDEX_UNIT_DEPENDENCY_NOT_FOUND
```

---

# Dependencia opcional

Podrá registrarse como no bloqueante.

---

# Dependencia obligatoria

Su ausencia deberá invalidar la unidad.

---

# Dependency Snapshot

Toda dependencia deberá resolverse contra un snapshot.

---

# No mezclar snapshots

Una unidad no deberá enlazar silenciosamente con dependencias de otra versión lógica.

---

# Decimotercera etapa — Construcción de lineage

El lineage permite reconstruir cada transformación.

---

# Unit Lineage

```yaml
lineage:
  unit: IDX-UNIT-000041

  canonical_resource:
    id: REC-0009
    type: recipe

  source_snapshot:
    id: DOC-SNAP-20260801-0001

  artifacts:
    - IDX-ART-000041
    - IDX-ART-000042

  processors:
    - IDX-PROC-MARKDOWN-PARSER@1.0.0
    - IDX-PROC-NORMALIZER@1.0.0
    - IDX-PROC-SEGMENTER@1.0.0

  execution:
    id: IDX-EXEC-000041
```

---

# Lineage completo

Deberá permitir navegar:

```text
Index Entry
↓
Indexable Unit
↓
Logical Segment
↓
Parsed Document
↓
Source Record
↓
Canonical Resource
↓
Source Snapshot
```

---

# Reverse Lineage

También deberá permitir responder:

```text
¿Qué entradas de índice dependen de este recurso?
```

---

# Usos

- invalidación;
- auditoría;
- citas;
- debugging;
- derechos de eliminación;
- reindexado;
- explicabilidad.

---

# Lineage Integrity

Deberán detectarse:

- unidades huérfanas;
- punteros rotos;
- snapshots desconocidos;
- procesadores no registrados.

---

# Decimocuarta etapa — Validación de unidades

Antes de pasar a chunking o builders, las unidades deberán validarse.

---

# Unit Validator

Podrá comprobar:

- schema;
- identidad;
- contenido;
- puntero canónico;
- hashes;
- seguridad;
- lineage;
- dependencias;
- idioma;
- capa epistemológica.

---

# Diagnostic Codes iniciales

```text
INDEX_UNIT_SCHEMA_INVALID
INDEX_UNIT_ID_MISSING
INDEX_UNIT_CANONICAL_POINTER_MISSING
INDEX_UNIT_CONTENT_EMPTY
INDEX_UNIT_SECURITY_METADATA_MISSING
INDEX_UNIT_DEPENDENCY_NOT_FOUND
INDEX_UNIT_LINEAGE_BROKEN
INDEX_UNIT_DUPLICATE_LOGICAL_KEY
INDEX_UNIT_SNAPSHOT_MISMATCH
INDEX_UNIT_EPISTEMIC_LAYER_MISSING
```

---

# Unit Validation Result

```yaml
unit_validation:
  unit: IDX-UNIT-000041

  status: valid

  diagnostics:
    errors: 0
    warnings: 0
```

---

# Estados

```text
valid
valid_with_warnings
invalid
quarantined
unknown
```

---

# Unidad vacía

Podrá ser válida únicamente para tipos estructurales expresamente permitidos.

---

# Empty Content Policy

El perfil deberá definirlo.

---

# Unidad con advertencias

Podrá pasar si el Gate lo permite.

---

# Unidad inválida

No deberá llegar a builders.

---

# Quarantine Unit

Una unidad podrá ponerse en cuarentena por:

- secreto;
- contenido malicioso;
- parsing corrupto;
- clasificación desconocida;
- conflicto grave.

---

# Unit Quarantine Record

```yaml
quarantine:
  id: IDX-QUAR-000041

  unit: IDX-UNIT-000041

  reason:
    code: POTENTIAL_SECRET_DETECTED

  status: under_review
```

---

# Quality Gate de unidades

```yaml
quality_gate:
  id: QG-INDEX-UNITS-0001

  criteria:
    all:
      - invalid_required_units == 0
      - missing_canonical_pointers == 0
      - missing_security_metadata == 0
      - duplicate_logical_keys == 0
      - broken_lineage == 0
```

---

# Checkpoints del pipeline

Las etapas deberán crear checkpoints cuando el volumen o coste lo justifique.

---

# Checkpoint Types

```text
after_source_resolution
after_change_analysis
after_extraction
after_parsing
after_normalization
after_segmentation
after_unit_construction
after_enrichment
after_deduplication
after_validation
```

---

# Checkpoint Contract

```yaml
indexing_checkpoint:
  id: IDX-CHK-000041

  execution:
    id: IDX-EXEC-000041

  stage: logical_segmentation

  artifact:
    id: IDX-ART-000047

  source_fingerprint: ...
  configuration_fingerprint: ...

  status: valid
```

---

# Reanudación

Deberá comprobar:

- snapshot fuente;
- processor versions;
- profile;
- security context;
- artifact integrity.

---

# Checkpoint Stale

Error:

```text
INDEXING_CHECKPOINT_STALE
```

---

# Partial Checkpoint

No deberá reutilizarse como completo.

---

# Procesamiento por lotes

Las unidades podrán procesarse en batches.

---

# Batch Contract

```yaml
unit_batch:
  id: IDX-BATCH-000041

  stage: normalization

  units:
    first: IDX-UNIT-000001
    last: IDX-UNIT-000100

  status: completed
```

---

# Batch Size

Deberá ajustarse según:

- tipo;
- tamaño;
- coste;
- memoria;
- proveedor;
- límites.

---

# Orden

El pipeline deberá declarar cuándo el orden importa.

---

# Procesamiento paralelo

Podrá aplicarse a unidades independientes.

---

# Barrier

Algunas etapas requerirán esperar a todos los batches.

Ejemplos:

- deduplicación global;
- coverage;
- dependency graph;
- Quality Gate.

---

# Backpressure

El pipeline deberá limitar producción cuando una etapa posterior esté saturada.

---

# Retry por unidad

Será adecuado para errores locales.

---

# Retry por batch

Será adecuado para fallos transitorios de dependencia.

---

# Fallo global

Será adecuado cuando:

- schema incompatible;
- snapshot corrupto;
- configuración inválida;
- seguridad no resoluble.

---

# Error Handling

Los errores deberán clasificarse.

---

# Categorías

```text
source
eligibility
change_analysis
extraction
parsing
normalization
segmentation
unit_construction
enrichment
deduplication
dependency
validation
security
infrastructure
```

---

# Error reintentable

Ejemplos:

- timeout;
- dependencia temporalmente no disponible;
- worker failure;
- rate limit.

---

# Error no reintentable

Ejemplos:

- schema inválido;
- snapshot incompatible;
- contenido corrupto persistente;
- configuración desconocida.

---

# Error por unidad

Podrá aislarse.

---

# Error estructural

Podrá bloquear la ejecución.

---

# Partial Execution

Podrá declararse cuando:

- algunas unidades válidas;
- otras fallan;
- el perfil lo permite.

---

# No activar partial bajo perfil estricto

La ejecución podrá continuar para diagnóstico, pero no publicar.

---

# Error Record

```yaml
indexing_error:
  id: IDX-ERROR-000041

  stage: parsing

  target:
    id: DOC-0042
    type: document

  code: MALFORMED_FRONT_MATTER
  retryable: false

  severity: error
```

---

# Error Budget por ejecución

El perfil podrá definir:

```yaml
failure_policy:
  maximum_unit_errors: 0
  maximum_warnings: 20
  allow_partial: false
```

---

# Observabilidad del pipeline

---

# Métricas por etapa

- input count;
- output count;
- drop count;
- error count;
- duration;
- throughput;
- reuse ratio;
- retry count.

---

# Métricas de unidades

- units by type;
- average size;
- empty units;
- duplicates;
- lineage errors;
- dependency count;
- security metadata gaps.

---

# Reuse Ratio

```text
reused_units
/
eligible_units
```

---

# Expansion Ratio

```text
indexable_units
/
canonical_resources
```

---

# Drop Ratio

```text
excluded_or_invalid_units
/
candidate_units
```

---

# Dependency Fan-Out

Mide cuántas unidades dependen de un recurso.

---

# Segment Size Distribution

Será importante para preparar chunking.

---

# Logs estructurados

```yaml
log:
  event: indexing_stage_completed

  execution: IDX-EXEC-000041
  stage: unit_construction

  input_count: 129
  output_count: 846
  warnings: 3
  duration_ms: 980
```

---

# Tracing

Cada unidad podrá enlazar con la traza de transformación.

---

# Sampling

No será necesario trazar individualmente todas las unidades en producción.

Deberán conservarse muestras y trazas completas para errores.

---

# Auditoría

Deberán auditarse:

- cambio de pipeline;
- cambio de parser;
- cambio de normalización;
- cambio de eligibility rules;
- exclusión masiva;
- cuarentena;
- override;
- reanudación desde checkpoint.

---

# Seguridad del pipeline

---

# Principio

La seguridad no deberá añadirse después de construir las unidades.

---

# Propagación

Cada etapa deberá preservar:

- tenant;
- classification;
- visibility;
- ACL;
- purpose restrictions.

---

# Procesadores autorizados

Un procesador deberá estar autorizado para tratar la clasificación correspondiente.

---

# External Processor

Si una etapa utiliza un proveedor externo deberá comprobarse:

- clasificación;
- transferencia;
- contrato;
- región;
- retención;
- logging.

---

# No enviar contenido restringido sin política

---

# Artifact Security

Los artefactos intermedios deberán heredar clasificación.

---

# Artifact Encryption

Deberán cifrarse en reposo.

---

# Artifact Access

Deberá limitarse a:

- ejecución;
- operadores autorizados;
- auditoría;
- debugging controlado.

---

# Redaction antes de externalización

Cuando proceda, deberá aplicarse antes de cualquier procesador externo.

---

# Malicious Content

El contenido deberá tratarse como datos.

---

# Prompt Injection

Las etapas basadas en modelos no deberán seguir instrucciones contenidas en los documentos.

---

# Output Validation

La salida de un modelo deberá validarse contra schema.

---

# Unit-Level ACL

Las unidades podrán heredar ACL de:

- documento;
- sección;
- entidad;
- relación.

---

# Restricción más alta

Cuando una unidad combine fuentes deberá heredar la clasificación más restrictiva.

---

# Tenant Mixing

No deberán construirse unidades combinando tenants distintos salvo operación administrativa explícita.

---

# Casos de uso

---

# Caso de uso 1 — Receta Markdown

```text
Recipe Document
↓
Parse Front Matter
↓
Identify Sections
↓
Create Ingredient Units
↓
Create Procedure Step Units
↓
Attach Canonical Pointers
↓
Validate Units
```

---

# Caso de uso 2 — Tabla de equivalencias

```text
Markdown Table
↓
Parse Headers
↓
Create Table Unit
↓
Create Row Units
↓
Attach Header Context
↓
Normalize Quantities
```

---

# Caso de uso 3 — Statement del Knowledge Graph

```text
Statement
↓
Extract Subject, Predicate and Object
↓
Preserve Qualifiers
↓
Create Statement Unit
↓
Attach Provenance
```

---

# Caso de uso 4 — Cambio en ingrediente

Se modifica `ING-0008`.

El análisis de impacto identifica:

- Entity Unit;
- recipes que lo referencian;
- paths de alérgenos;
- summaries dependientes.

---

# Caso de uso 5 — Cambio meramente editorial

Se corrigen espacios sin alterar contenido normalizado.

El fingerprint semántico no cambia.

Las unidades pueden reutilizarse.

---

# Caso de uso 6 — Cambio de clasificación

Una sección pasa a `restricted`.

El Security Fingerprint cambia.

Todas sus unidades deberán actualizarse aunque el texto permanezca igual.

---

# Caso de uso 7 — Referencia rota

Una receta enlaza con un ingrediente inexistente.

La unidad se construye como inválida o bloqueada según perfil.

Se genera:

```text
INDEX_UNIT_DEPENDENCY_NOT_FOUND
```

---

# Caso de uso 8 — Duplicado multifuente

Dos documentos incluyen la misma definición.

Se conservan ambas procedencias y se enlazan como duplicados.

---

# Caso de uso 9 — Resumen derivado

Un procesador autorizado genera un resumen.

La unidad declara:

- fuentes;
- procesador;
- versión;
- capa `derived`;
- confianza.

---

# Caso de uso 10 — Checkpoint

Falla el pipeline después de segmentación.

La reanudación reutiliza los artefactos si:

- snapshots;
- perfiles;
- procesadores;
- seguridad;

siguen siendo compatibles.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Extraer únicamente texto plano

Destruye estructura y procedencia.

---

## Confundir segmentación con chunking

Dificulta diseño y trazabilidad.

---

## Normalizar sobrescribiendo el original

Impide reconstrucción.

---

## Corregir contenido durante indexación

El Indexing Engine no debe modificar conocimiento canónico.

---

## Crear unidades sin puntero canónico

Impide citas e invalidación.

---

## Utilizar offsets como identidad estable

Pueden cambiar ante ediciones.

---

## Generar IDs aleatorios sin logical key

Dificulta incremental indexing.

---

## Perder el orden de procedimientos

Puede alterar significado.

---

## Convertir tablas en texto sin headers

Descontextualiza valores.

---

## Dividir Statements

Puede destruir sujeto, predicado u objeto.

---

## Mezclar contexto heredado y contenido original

Dificulta grounding.

---

## Duplicar contexto excesivo

Aumenta coste y sesgo en retrieval.

---

## Deduplicar únicamente mediante embeddings

Puede eliminar información distinta.

---

## Fusionar duplicados con ACL diferentes

Puede ampliar acceso.

---

## Reutilizar artefactos sin Security Fingerprint

Puede mantener permisos obsoletos.

---

## Tratar cualquier cambio como semántico

Reduce eficiencia.

---

## Ignorar cambios indirectos

Deja unidades stale.

---

## No distinguir dependencias de procesamiento y semánticas

Produce ciclos o invalidaciones incorrectas.

---

## Omitir lineage de unidades derivadas

Impide explicar su origen.

---

## Permitir que un modelo cree facts

Debe limitarse a enriquecimiento derivado.

---

## Aceptar salida de modelo sin schema

Puede introducir contenido corrupto.

---

## Ignorar unidades fallidas

Oculta pérdida de cobertura.

---

## Continuar tras snapshot incompatible

Rompe coherencia.

---

## Reanudar con configuración diferente

Produce resultados no reproducibles.

---

## Conservar artefactos indefinidamente

Aumenta coste y exposición.

---

## Procesar tenants distintos en el mismo contexto

Compromete aislamiento.

---

## Registrar contenido completo en logs

Compromete seguridad.

---

# Reglas mínimas de conformidad

---

## Pipeline versionado

Toda ejecución deberá indicar pipeline y versión.

---

## Procesadores registrados

Toda etapa deberá utilizar procesadores identificados.

---

## Contratos entre etapas

Toda salida deberá cumplir schema.

---

## Resolución de snapshots

Las fuentes deberán fijarse antes de procesar.

---

## Elegibilidad evaluada

Todo recurso deberá tener una decisión.

---

## Cambios analizados

La indexación incremental deberá justificar reutilización e invalidación.

---

## Parsing trazable

La estructura original deberá preservarse.

---

## Normalización reversible

El original y las transformaciones deberán conservarse.

---

## Segmentación lógica

Las unidades deberán respetar estructura y dominio.

---

## Identidad estable

Toda unidad deberá poseer logical key.

---

## Puntero canónico

Toda unidad deberá resolverse hacia su fuente.

---

## Seguridad propagada

Toda unidad deberá conservar tenant y clasificación.

---

## Fingerprints

La reutilización deberá basarse en fingerprints compatibles.

---

## Dependencias explícitas

Toda dependencia relevante deberá registrarse.

---

## Lineage completo

Toda unidad deberá declarar cómo fue creada.

---

## Deduplicación gobernada

Las decisiones deberán conservar procedencia y seguridad.

---

## Validación de unidades

Las unidades inválidas no deberán llegar a builders.

---

## Checkpoints compatibles

La reanudación deberá verificar hashes y versiones.

---

## Errores estructurados

Los fallos deberán ser localizables y auditables.

---

# Conformidad de Source Resolution

Será conforme cuando:

- fije snapshots;
- valide checksums;
- valide estados;
- aplique tenant;
- aplique clasificación;
- produzca manifest.

---

# Conformidad de Eligibility Result

Será conforme cuando:

- identifique recurso;
- declare decisión;
- declare reglas;
- declare motivo;
- preserve política.

---

# Conformidad de Change Analysis

Será conforme cuando:

- declare baseline;
- declare snapshot nuevo;
- clasifique cambios;
- calcule impacto;
- identifique reutilización;
- detecte cambios de seguridad.

---

# Conformidad de Parsed Document

Será conforme cuando:

- conserve estructura;
- conserve posiciones;
- conserve Front Matter;
- conserve referencias;
- identifique parser y versión.

---

# Conformidad de Normalized Content

Será conforme cuando:

- preserve original;
- declare transformaciones;
- no altere significado;
- identifique perfil;
- conserve unidades y negaciones.

---

# Conformidad de Logical Segment

Será conforme cuando:

- tenga identidad;
- tenga tipo;
- preserve jerarquía;
- preserve orden;
- conserve puntero;
- declare límites.

---

# Conformidad de Indexable Unit

Será conforme cuando:

- tenga ID;
- tenga logical key;
- declare tipo;
- conserve puntero canónico;
- conserve snapshot;
- declare seguridad;
- declare hashes;
- declare capa epistemológica;
- tenga lineage.

---

# Conformidad de Dependency Graph

Será conforme cuando:

- identifique origen y destino;
- declare tipo;
- declare impacto;
- preserve snapshot;
- detecte ciclos;
- distinga dependencias obligatorias.

---

# Conformidad de Deduplication Result

Será conforme cuando:

- identifique unidades;
- declare estrategia;
- preserve procedencia;
- preserve seguridad;
- declare conflictos.

---

# Lista de comprobación

Antes de aprobar la salida del pipeline deberá comprobarse:

```text
[ ] El pipeline está versionado.
[ ] Los procesadores están registrados.
[ ] Los snapshots fuente están resueltos.
[ ] Los manifests son válidos.
[ ] La elegibilidad se ha evaluado.
[ ] El análisis de cambios está completo.
[ ] Los cambios de seguridad se han detectado.
[ ] Los recursos se han extraído con procedencia.
[ ] El parsing conserva estructura y posiciones.
[ ] El contenido original se conserva.
[ ] La normalización está registrada.
[ ] La segmentación respeta jerarquía.
[ ] Las tablas conservan encabezados.
[ ] Los procedimientos conservan orden.
[ ] Los Statements conservan sus componentes.
[ ] Toda unidad tiene logical key.
[ ] Toda unidad tiene puntero canónico.
[ ] Toda unidad tiene snapshot.
[ ] Toda unidad tiene clasificación.
[ ] Los fingerprints están calculados.
[ ] Las dependencias están resueltas.
[ ] El lineage está completo.
[ ] La deduplicación ha sido evaluada.
[ ] No se han fusionado ACL incompatibles.
[ ] Las unidades inválidas están aisladas.
[ ] El Quality Gate de unidades ha finalizado.
[ ] Los artefactos cumplen retención y seguridad.
[ ] Los checkpoints son compatibles.
[ ] Las métricas de cobertura están disponibles.
```

---

# Arquitectura final de la Parte II

```text
Canonical Snapshots
        ↓
Source Resolution
        ↓
Eligibility
        ↓
Change Analysis
        ↓
Resource Extraction
        ↓
Parsing
        ↓
Normalization
        ↓
Logical Segmentation
        ↓
Indexable Unit Construction
        ↓
Enrichment
        ↓
Deduplication
        ↓
Dependency Resolution
        ↓
Lineage
        ↓
Unit Validation
        ↓
Validated Indexable Units
```

---

# Transición hacia la Parte III

Esta segunda parte ha definido:

- el pipeline de indexación;
- los procesadores;
- los contratos entre etapas;
- los artefactos intermedios;
- la resolución de fuentes;
- los manifests;
- la elegibilidad;
- el análisis de cambios;
- la extracción;
- el parsing;
- la normalización;
- la segmentación lógica;
- las unidades documentales;
- las unidades semánticas;
- las unidades estructuradas;
- las unidades de grafo;
- las unidades compuestas;
- el contexto heredado;
- la capa epistemológica;
- el enriquecimiento;
- la deduplicación;
- los fingerprints;
- las dependencias;
- el lineage;
- la validación de unidades;
- los checkpoints;
- el procesamiento por lotes;
- los errores;
- la seguridad;
- la observabilidad;
- los casos de uso;
- los antipatrones;
- las reglas de conformidad.

La Parte III desarrollará:

- estrategias de chunking;
- Chunk Profiles;
- chunks estructurales;
- chunks semánticos;
- chunks de tablas;
- chunks de procedimientos;
- ventanas de contexto;
- solapamiento;
- parent-child retrieval;
- contextualización;
- modelos de embeddings;
- selección de modelos;
- dimensiones;
- pooling;
- normalización vectorial;
- batch embedding;
- caché de embeddings;
- fingerprints;
- privacidad;
- evaluación;
- Quality Gates de chunks y embeddings.

---

# Conclusión

El pipeline de indexación convierte conocimiento canónico en unidades gobernadas que pueden ser transformadas en representaciones recuperables.

Su función no consiste únicamente en leer archivos.

Deberá determinar:

- qué recursos son elegibles;
- qué cambió;
- qué puede reutilizarse;
- cómo preservar estructura;
- cómo construir unidades;
- cómo conservar procedencia;
- cómo propagar seguridad;
- cómo resolver dependencias;
- cómo detectar duplicados;
- cómo validar resultados.

El ciclo puede resumirse así:

```text
Resolver
    ↓
Seleccionar
    ↓
Comparar
    ↓
Extraer
    ↓
Parsear
    ↓
Normalizar
    ↓
Segmentar
    ↓
Construir
    ↓
Enriquecer
    ↓
Relacionar
    ↓
Validar
```

La resolución fija el conocimiento de entrada.

La elegibilidad aplica políticas.

El análisis de cambios permite incremental indexing.

La extracción recupera recursos canónicos.

El parsing preserva estructura.

La normalización estabiliza representación.

La segmentación identifica unidades lógicas.

La construcción crea unidades indexables.

El enriquecimiento añade contexto.

La deduplicación reduce redundancia.

Las dependencias permiten invalidación precisa.

El lineage conserva trazabilidad.

La validación garantiza que únicamente unidades conformes lleguen a los builders.

Una unidad indexable correcta deberá poder responder:

```text
¿Qué representa?

¿De qué recurso procede?

¿En qué snapshot existe?

¿Qué parte exacta del documento contiene?

¿Qué transformaciones recibió?

¿Qué procesadores intervinieron?

¿Qué dependencias posee?

¿Qué clasificación hereda?

¿Qué fingerprint determina su reutilización?

¿En qué entradas de índice terminará?
```

Con esta segunda parte queda formalizado el pipeline mediante el que NovaCoquinaria transforma documentos, componentes, entidades, Statements, relaciones, tablas, procedimientos y subgrafos en unidades indexables seguras, reproducibles y trazables.

La siguiente parte definirá cómo estas unidades se convierten en chunks y representaciones vectoriales preparadas para recuperación semántica.

---

# Parte III — Chunking, contextualización y generación de embeddings

---

# Introducción

La Parte II ha definido el pipeline mediante el que NovaCoquinaria transforma conocimiento canónico en unidades indexables:

```text
Canonical Resource
        ↓
Parsing
        ↓
Normalization
        ↓
Logical Segmentation
        ↓
Indexable Unit
```

Sin embargo, una unidad indexable no siempre constituye la representación óptima para recuperación semántica.

Una unidad puede ser:

- demasiado grande;
- demasiado pequeña;
- dependiente de su contexto;
- estructuralmente compleja;
- compuesta por varias secciones;
- incompatible con los límites del modelo de embeddings;
- poco adecuada para una consulta concreta.

Por ello será necesaria una fase adicional encargada de transformar unidades indexables en representaciones adaptadas a:

- búsqueda semántica;
- recuperación vectorial;
- recuperación híbrida;
- parent-child retrieval;
- contextual retrieval;
- GraphRAG;
- grounding;
- citación.

Esta fase estará compuesta principalmente por:

```text
Chunking
```

y:

```text
Embedding Generation
```

Conceptualmente:

```text
Validated Indexable Units
        ↓
Chunk Planning
        ↓
Chunk Construction
        ↓
Context Enrichment
        ↓
Chunk Validation
        ↓
Embedding Preparation
        ↓
Embedding Generation
        ↓
Vector Validation
        ↓
Embedding Artifacts
```

El chunking no deberá consistir simplemente en dividir texto cada cierto número de caracteres.

La generación de embeddings tampoco deberá considerarse una operación opaca sobre texto arbitrario.

Ambas fases deberán preservar:

- significado;
- estructura;
- procedencia;
- identidad;
- relaciones;
- seguridad;
- temporalidad;
- capa epistemológica;
- capacidad de citación.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir el modelo de chunk;
- diferenciar unidad indexable y chunk;
- formalizar estrategias de chunking;
- establecer Chunk Profiles;
- definir chunking estructural;
- definir chunking semántico;
- regular chunks de procedimientos;
- regular chunks de tablas;
- definir parent-child retrieval;
- formalizar ventanas de contexto;
- regular overlap;
- definir contextualización;
- preservar citas;
- formalizar Chunk Fingerprints;
- definir modelos de embeddings;
- establecer Embedding Profiles;
- formalizar la preparación de entradas;
- definir selección de modelos;
- regular dimensión, pooling y normalización;
- definir batching;
- formalizar caché de embeddings;
- establecer versionado;
- regular privacidad y seguridad;
- definir evaluación;
- formalizar Quality Gates;
- establecer observabilidad;
- preparar los builders vectoriales de la Parte IV.

---

# Principios de chunking

Toda estrategia de chunking deberá respetar los siguientes principios.

---

## Preservación semántica

Un chunk no deberá dividir una idea de forma que altere su significado.

---

## Preservación estructural

Los límites naturales del contenido deberán tener prioridad sobre límites arbitrarios.

---

## Atomicidad contextual

Un chunk deberá contener suficiente información para ser comprendido dentro de su caso de uso.

---

## Trazabilidad

Todo chunk deberá resolverse hacia una o varias unidades indexables.

---

## Identidad estable

La identidad lógica de un chunk deberá mantenerse cuando su contenido lógico no cambie.

---

## Contexto explícito

El contexto añadido deberá diferenciarse del contenido original.

---

## No contaminación

El contexto de un chunk no deberá incorporar información de otro tenant, clasificación o scope incompatible.

---

## Seguridad heredada

Todo chunk deberá conservar la clasificación más restrictiva de sus fuentes.

---

## Reproducibilidad

La misma unidad, perfil y versión deberán producir el mismo conjunto lógico de chunks en las fases deterministas.

---

## No truncamiento silencioso

Toda pérdida de contenido deberá:

- declararse;
- diagnosticarse;
- bloquear cuando proceda.

---

## Tamaño gobernado

Los límites deberán definirse mediante perfiles versionados.

---

## Overlap justificado

El solapamiento no deberá aplicarse indiscriminadamente.

---

## Separación de contenido y metadata

El texto indexado y los metadatos deberán poder evolucionar de forma controlada.

---

## Compatibilidad con citas

Todo fragmento recuperable deberá poder citarse.

---

## Adecuación al retriever

El chunking deberá responder a las necesidades del Retrieval Engine sin acoplarse a una única implementación.

---

## Evaluación empírica

La calidad de una estrategia deberá medirse mediante datasets y consultas representativas.

---

# Unidad indexable y chunk

Una **Indexable Unit** representa una unidad lógica del conocimiento.

Un **Chunk** representa una unidad adaptada para recuperación o embeddings.

---

# Ejemplo

Una unidad indexable puede representar:

```text
Procedimiento completo de una receta
```

El chunking puede producir:

```text
Chunk 1 → pasos 1–3
Chunk 2 → pasos 3–5
Chunk 3 → pasos 5–7
```

---

# Relación cardinal

Una unidad indexable podrá producir:

```text
0 chunks
1 chunk
N chunks
```

---

# Cero chunks

Será posible cuando:

- la unidad esté excluida;
- solo se utilice en índice estructurado;
- no contenga contenido semántico recuperable;
- esté invalidada;
- pertenezca a un perfil sin vectorización.

---

# Un chunk

Será habitual para:

- Statement;
- definición;
- relación;
- párrafo breve;
- advertencia;
- Entity Unit.

---

# Varios chunks

Será habitual para:

- documento;
- sección extensa;
- tabla;
- procedimiento;
- subgrafo;
- resumen extenso.

---

# Chunk

Se define un **Chunk** como:

> Una representación derivada, contextualizada y trazable de una o varias unidades indexables, construida para facilitar recuperación, ranking, embeddings, grounding o citación.

---

# Chunk ID

Formato recomendado:

```text
IDX-CHUNK-XXXXXX
```

---

# Chunk Logical Key

Deberá existir una clave lógica estable.

Ejemplo:

```text
REC-0009#PREPARATION#WINDOW-01
```

---

# Chunk Contract

```yaml
chunk:
  id: IDX-CHUNK-000041

  logical_key: REC-0009#PREPARATION#WINDOW-01

  type: procedure_window

  source_units:
    - IDX-UNIT-STEP-000001
    - IDX-UNIT-STEP-000002
    - IDX-UNIT-STEP-000003

  canonical_pointer:
    resource:
      id: REC-0009
      type: recipe

    document:
      id: DOC-0051

    snapshot:
      id: DOC-SNAP-20260801-0001

  content:
    original: |
      1. Calentar el caldo.
      2. Añadir las verduras.
      3. Incorporar el tofu.

    contextualized: |
      Receta: Sopa de miso.
      Sección: Preparación.
      Pasos 1 a 3.
      1. Calentar el caldo.
      2. Añadir las verduras.
      3. Incorporar el tofu.

    language: es

  hierarchy:
    parent_chunk: IDX-CHUNK-PARENT-000041
    sequence: 1
    total: 3

  security:
    tenant: TENANT-0001
    classification: internal

  epistemic_layer: explicit

  hashes:
    content: ...
    context: ...
    chunking: ...
    composite: ...

  status: ready
```

---

# Estados de chunk

```text
candidate
ready
excluded
invalid
quarantined
stale
embedded
indexed
deleted
```

---

# Tipos de chunk

Valores iniciales:

```text
document
section
paragraph
semantic
procedure
procedure_window
procedure_step
table
table_row_group
definition
statement
entity
relation
graph_path
subgraph
summary
citation
contextual
parent
child
```

---

# Chunk Profile

Un **Chunk Profile** define cómo se construyen chunks para un caso de uso.

Formato recomendado:

```text
CHUNK-PROFILE-XXXXXX
```

---

# Contenido

- tipos de unidad admitidos;
- estrategia;
- tamaño objetivo;
- tamaño mínimo;
- tamaño máximo;
- unidad de medida;
- overlap;
- contexto;
- jerarquía;
- exclusiones;
- validadores;
- fallback.

---

# Contrato

```yaml
chunk_profile:
  id: CHUNK-PROFILE-RAG-STANDARD

  version: 1.0.0
  status: active

  strategy:
    primary: structural_semantic
    fallback: token_window

  size:
    target_tokens: 350
    minimum_tokens: 80
    maximum_tokens: 600

  overlap:
    strategy: semantic_boundary
    maximum_tokens: 80

  context:
    include_document_title: true
    include_section_path: true
    include_entity_labels: true

  hierarchy:
    create_parent_chunks: true
    create_child_chunks: true

  validators:
    - CHUNK-VALIDATOR-SIZE
    - CHUNK-VALIDATOR-LINEAGE
    - CHUNK-VALIDATOR-SECURITY
```

---

# Perfiles iniciales

```text
document_search
rag_standard
rag_precise
rag_broad
graphrag
procedure
table
entity
statement
preview
multilingual
```

---

# Perfil `document_search`

Adecuado para:

- búsqueda documental;
- resultados amplios;
- snippets;
- facetas.

Características:

- chunks de sección;
- tamaño medio;
- poco overlap;
- contexto documental.

---

# Perfil `rag_standard`

Adecuado para:

- preguntas generales;
- respuestas con citas;
- recuperación híbrida.

Características:

- chunks estructurales y semánticos;
- parent-child;
- contexto moderado;
- overlap controlado.

---

# Perfil `rag_precise`

Adecuado para:

- hechos concretos;
- cantidades;
- tiempos;
- alérgenos;
- statements.

Características:

- chunks pequeños;
- alta precisión;
- citas exactas;
- poca agregación.

---

# Perfil `rag_broad`

Adecuado para:

- síntesis;
- comparación;
- visión global.

Características:

- chunks mayores;
- summaries;
- contexto amplio;
- parent retrieval.

---

# Perfil `graphrag`

Adecuado para:

- relaciones;
- caminos;
- comunidades;
- explicaciones estructuradas.

Características:

- Entity Chunks;
- Statement Chunks;
- Path Chunks;
- Subgraph Summaries.

---

# Perfil `procedure`

Adecuado para:

- recetas;
- técnicas;
- workflows;
- secuencias.

Características:

- preservación de orden;
- ventanas de pasos;
- contexto de precondiciones;
- overlap por dependencia.

---

# Perfil `table`

Adecuado para:

- tablas;
- equivalencias;
- tiempos;
- cantidades.

Características:

- repetición de headers;
- agrupación de filas;
- contexto de tabla;
- preservación de unidades.

---

# Perfil `entity`

Adecuado para:

- búsqueda de entidades;
- aliases;
- desambiguación;
- autocompletado.

---

# Perfil `statement`

Adecuado para recuperar hechos atómicos.

---

# Perfil `preview`

Adecuado para contenido no publicado en un ámbito aislado.

---

# Perfil `multilingual`

Podrá:

- mantener idioma original;
- añadir labels multilingües;
- generar embeddings multilingües;
- preservar locale.

---

# Estrategias de chunking

NovaCoquinaria podrá utilizar varias estrategias.

---

# Structural Chunking

Utiliza límites estructurales.

Ejemplos:

- heading;
- sección;
- lista;
- tabla;
- bloque;
- paso.

---

# Semantic Chunking

Utiliza cambios de tema o cohesión semántica.

---

# Fixed Token Window

Divide según número de tokens.

---

# Fixed Character Window

Divide según caracteres.

Solo deberá utilizarse como fallback o para formatos muy controlados.

---

# Sentence Window

Agrupa frases consecutivas.

---

# Paragraph Chunking

Utiliza párrafos como unidades.

---

# Recursive Chunking

Aplica una jerarquía de separadores.

Ejemplo:

```text
Section
↓
Paragraph
↓
Sentence
↓
Token Window
```

---

# Entity-Aware Chunking

Evita separar menciones y contexto relevante de entidades.

---

# Relation-Aware Chunking

Preserva relaciones completas.

---

# Procedure-Aware Chunking

Respeta:

- orden;
- dependencias;
- precondiciones;
- resultados.

---

# Table-Aware Chunking

Preserva:

- encabezados;
- columnas;
- unidades;
- contexto.

---

# Graph-Aware Chunking

Construye representaciones a partir de:

- nodos;
- aristas;
- paths;
- neighborhoods;
- communities.

---

# Hierarchical Chunking

Produce:

- parent chunks;
- child chunks;
- mappings jerárquicos.

---

# Adaptive Chunking

Ajusta estrategia según:

- tipo de documento;
- densidad;
- estructura;
- complejidad;
- idioma.

---

# Model-Assisted Chunking

Podrá utilizar modelos para detectar fronteras semánticas.

Deberá:

- estar versionado;
- producir salida estructurada;
- registrar confianza;
- disponer de fallback;
- no seguir instrucciones del contenido.

---

# Estrategia híbrida recomendada

```text
Structural Boundaries
        ↓
Semantic Cohesion
        ↓
Token Limits
        ↓
Fallback Split
```

---

# Chunk Planning

Antes de construir chunks podrá generarse un plan.

Formato recomendado:

```text
CHUNK-PLAN-XXXXXX
```

---

# Contrato

```yaml
chunk_plan:
  id: CHUNK-PLAN-000041

  unit:
    id: IDX-UNIT-PROC-000041

  profile:
    id: CHUNK-PROFILE-PROCEDURE
    version: 1.0.0

  strategy:
    primary: procedure_window
    fallback: token_window

  expected:
    chunks: 3

  boundaries:
    - after_step: 3
    - after_step: 5
```

---

# Chunk Planner

Deberá considerar:

- tipo de unidad;
- tamaño;
- jerarquía;
- límites naturales;
- contexto;
- dependencias;
- presupuesto;
- modelo de embedding.

---

# Chunk Boundary

Todo límite deberá declarar su causa.

---

# Boundary Types

```text
structural
semantic
size
procedure
table
graph
security
manual
fallback
```

---

# Boundary Contract

```yaml
chunk_boundary:
  after_segment: IDX-SEG-000041

  type: structural

  reason: section_end

  confidence: 1.0
```

---

# Tamaño de chunk

El tamaño podrá medirse en:

```text
tokens
characters
sentences
segments
rows
steps
nodes
edges
```

---

# Unidad primaria recomendada

Para modelos de embeddings se utilizarán tokens o una estimación compatible.

---

# Target Size

Representa el tamaño preferido.

---

# Minimum Size

Evita chunks demasiado pequeños y poco informativos.

---

# Maximum Size

Evita exceder:

- límites del modelo;
- presupuesto;
- calidad de retrieval.

---

# Hard Limit

No deberá superarse.

---

# Soft Limit

Podrá superarse para preservar atomicidad semántica dentro de un margen gobernado.

---

# Oversized Atomic Unit

Una unidad atómica que exceda el máximo deberá:

- usar estrategia especial;
- generar diagnóstico;
- conservar versión completa;
- producir representaciones auxiliares.

---

# Ejemplo

Un Statement muy largo no deberá dividirse arbitrariamente.

---

# Undersized Chunk

Un chunk demasiado pequeño podrá:

- fusionarse con un vecino;
- heredar contexto;
- permanecer separado si es atómico;
- excluirse.

---

# Merge Policy

La fusión deberá respetar:

- estructura;
- seguridad;
- tenant;
- capa epistemológica;
- orden.

---

# Overlap

El overlap replica contexto entre chunks adyacentes.

---

# Objetivos

- preservar continuidad;
- evitar pérdida en fronteras;
- mantener referencias;
- mejorar recall.

---

# Riesgos

- duplicación;
- coste;
- sesgo de ranking;
- redundancia en contexto;
- repetición de citas.

---

# Estrategias de overlap

```text
fixed_tokens
fixed_sentences
semantic_boundary
procedure_dependency
table_header
none
```

---

# Fixed Token Overlap

Ejemplo:

```text
50 tokens
```

---

# Semantic Boundary Overlap

Replica únicamente la unidad semántica necesaria.

---

# Procedure Dependency Overlap

Replica:

- paso previo;
- ingrediente usado;
- precondición;
- estado resultante.

---

# Table Header Overlap

Repite encabezados en cada grupo de filas.

---

# Overlap Metadata

```yaml
overlap:
  strategy: procedure_dependency

  previous_chunk:
    id: IDX-CHUNK-000040

  shared_units:
    - IDX-UNIT-STEP-000003
```

---

# No overlap por defecto universal

La estrategia deberá depender del perfil.

---

# Chunk de documento

Representa una vista amplia del documento.

---

# Uso

- recuperación inicial;
- búsqueda documental;
- parent retrieval;
- summaries.

---

# Contenido

Podrá incluir:

- título;
- descripción;
- metadata;
- resumen;
- secciones principales.

---

# No incluir todo el documento si excede límites

Podrá utilizar:

- summary;
- outline;
- hierarchy.

---

# Chunk de sección

Representa una sección completa o subdividida.

---

# Section Path

Deberá conservar:

```text
Documento
>
Sección
>
Subsección
```

---

# Chunk de párrafo

Adecuado cuando el párrafo sea autocontenido.

---

# Contexto mínimo

Podrá añadir:

- título;
- heading;
- resource ID;
- type.

---

# Chunk semántico

Agrupa contenido por cohesión temática.

---

# Semantic Boundary Detection

Podrá utilizar:

- similarity entre frases;
- topic shifts;
- discourse markers;
- estructura;
- entidades.

---

# Threshold

Deberá estar gobernado.

---

# Semantic Chunk Record

```yaml
chunk:
  id: IDX-CHUNK-SEM-000041

  type: semantic

  source_units:
    - IDX-UNIT-PAR-000041
    - IDX-UNIT-PAR-000042

  boundary:
    start_reason: section_start
    end_reason: semantic_shift

  confidence: 0.91
```

---

# Semantic Chunking Probabilístico

Deberá registrar:

- modelo;
- versión;
- configuración;
- score;
- seed cuando proceda.

---

# Chunk de procedimiento

Un procedimiento deberá conservar:

- identidad;
- orden;
- pasos;
- dependencias;
- inputs;
- outputs;
- advertencias.

---

# Estrategias

```text
full_procedure
step
step_window
phase
dependency_group
```

---

# Full Procedure

Adecuado para procedimientos breves.

---

# Step Chunk

Representa un paso individual con contexto.

---

# Step Window

Agrupa varios pasos consecutivos.

---

# Phase Chunk

Agrupa una fase lógica.

Ejemplos:

- preparación;
- cocción;
- reposo;
- montaje.

---

# Dependency Group

Agrupa pasos unidos por una dependencia fuerte.

---

# Procedure Context

```yaml
procedure_context:
  recipe: REC-0009
  procedure: preparation
  previous_state: broth_heated
  next_state: miso_added
```

---

# Orden obligatorio

Los chunks deberán conservar:

- sequence;
- previous;
- next;
- total.

---

# Chunk de tabla

Las tablas requieren tratamiento específico.

---

# Riesgos de conversión plana

- pérdida de headers;
- asociación incorrecta;
- pérdida de unidades;
- mezcla de filas.

---

# Estrategias

```text
full_table
row
row_group
column_group
cell_with_context
```

---

# Full Table

Adecuado para tablas pequeñas.

---

# Row Chunk

Cada fila se convierte en una representación contextualizada.

---

# Row Group

Agrupa varias filas bajo los mismos headers.

---

# Column Group

Adecuado cuando las columnas representan dimensiones temáticas.

---

# Cell with Context

Adecuado para valores concretos.

---

# Table Chunk Contract

```yaml
chunk:
  id: IDX-CHUNK-TABLE-000041

  type: table_row_group

  context:
    table_title: Tiempos de cocción
    headers:
      - Ingrediente
      - Tiempo
      - Método

  rows:
    - ingredient: Garbanzo
      time: PT45M
      method: olla convencional

    - ingredient: Garbanzo
      time: PT20M
      method: olla a presión
```

---

# Headers repetidos

Todo chunk de filas deberá incluir sus headers.

---

# Merged Cells

Deberán expandirse o representarse explícitamente.

---

# Chunk de Statement

Un Statement deberá permanecer atómico.

---

# Statement Text Projection

Podrá producirse una representación textual.

Ejemplo:

```text
La receta REC-0009 utiliza el ingrediente ING-0008.
```

---

# Representación estructurada

Deberá preservarse por separado.

---

# Statement Chunk Contract

```yaml
chunk:
  id: IDX-CHUNK-STMT-000041

  type: statement

  structured:
    subject: REC-0009
    predicate: usesIngredient
    object: ING-0008

  textualized:
    es: La receta Sopa de miso utiliza miso.
```

---

# Textualization Profile

Las reglas de textualización deberán versionarse.

---

# Negación

Deberá preservarse explícitamente.

---

# Qualifiers

No deberán omitirse si cambian el significado.

---

# Chunk de entidad

Podrá incluir:

- preferred label;
- aliases;
- definición;
- clases;
- propiedades principales;
- relaciones resumidas.

---

# Entity Chunk

```yaml
chunk:
  id: IDX-CHUNK-ENTITY-000041

  type: entity

  entity:
    id: ING-0008
    type: ingredient

  content:
    preferred_label: Miso
    aliases:
      - pasta de miso

    description: Pasta fermentada de soja.
```

---

# Alias Injection

Los aliases podrán añadirse para mejorar retrieval.

Deberán permanecer identificados como metadata o contexto.

---

# Chunk de relación

Podrá representar:

```text
source
relation
target
qualifiers
provenance
```

---

# Chunk de path

Representa un camino de grafo.

---

# Path Textualization

Ejemplo:

```text
La receta Sopa de miso utiliza miso, que contiene soja.
```

---

# No omitir saltos

Deberán conservarse todos los nodos y relaciones.

---

# Chunk de subgrafo

Podrá representar:

- root;
- nodes;
- edges;
- summary;
- scope;
- depth.

---

# Tamaño

Deberá limitarse por:

- nodos;
- aristas;
- tokens;
- coste.

---

# Graph Summary Chunk

Podrá generar un resumen derivado.

Deberá indicar:

- algoritmo;
- modelo;
- fuentes;
- capa `derived`.

---

# Parent-Child Chunking

El modelo jerárquico produce chunks de diferentes granularidades.

---

# Parent Chunk

Representa contexto amplio.

Ejemplo:

```text
Sección completa de preparación.
```

---

# Child Chunk

Representa contenido preciso.

Ejemplo:

```text
Paso 3 de preparación.
```

---

# Flujo de retrieval

```text
Retrieve Child
        ↓
Resolve Parent
        ↓
Expand Context
```

---

# Beneficios

- precisión;
- contexto;
- citas;
- menor ruido.

---

# Parent-Child Contract

```yaml
chunk_hierarchy:
  parent:
    id: IDX-CHUNK-PARENT-000041

  children:
    - IDX-CHUNK-CHILD-000041
    - IDX-CHUNK-CHILD-000042
    - IDX-CHUNK-CHILD-000043
```

---

# Multi-Level Hierarchy

Podrá existir:

```text
Document
↓
Section
↓
Paragraph
↓
Sentence
```

---

# Límite de niveles

Deberá gobernarse para evitar complejidad excesiva.

---

# Retrieval Level

El perfil deberá indicar:

- nivel indexado;
- nivel recuperado;
- nivel expandido.

---

# Contextual Retrieval

El chunk podrá enriquecerse con contexto antes de generar embeddings.

---

# Context Types

```text
document_title
section_path
resource_type
entity_labels
collection
procedure_state
table_headers
graph_context
temporal_context
```

---

# Contextualized Text

Deberá diferenciarse del texto original.

---

# Ejemplo

```yaml
content:
  original: Añadir el miso al final.

  contextualized: |
    Receta: Sopa de miso.
    Sección: Preparación.
    Instrucción: Añadir el miso al final.
```

---

# Context Template

Las plantillas deberán versionarse.

Formato recomendado:

```text
CTX-TEMPLATE-XXXXXX
```

---

# Contrato

```yaml
context_template:
  id: CTX-TEMPLATE-PROCEDURE-0001

  version: 1.0.0

  fields:
    - recipe_title
    - section_title
    - step_number
    - content
```

---

# Context Budget

El contexto añadido deberá tener límites.

---

# Riesgo de sobrecontextualización

Puede:

- diluir el contenido;
- aumentar similitud artificial;
- duplicar términos;
- perjudicar ranking.

---

# Regla

Solo deberá añadirse contexto necesario para comprender o recuperar correctamente el chunk.

---

# Context Inheritance

El contexto podrá heredarse desde:

- documento;
- sección;
- entidad;
- colección;
- grafo.

---

# Context Conflict

Si dos fuentes proporcionan contexto incompatible deberá:

- bloquear;
- elegir según política;
- conservar ambas con qualifiers;
- generar diagnóstico.

---

# Citation Mapping

Todo chunk deberá conservar un mapa de citas.

---

# Citation Span

```yaml
citation_span:
  chunk_start: 0
  chunk_end: 62

  source:
    document: DOC-0051
    block: BLOCK-00041
    line_start: 84
    line_end: 86
```

---

# Chunks compuestos

Cuando un chunk combine fuentes deberá conservar varios spans.

---

# Citation Completeness

Todo fragmento no generado deberá poder mapearse a una fuente.

---

# Contenido contextual derivado

Deberá marcarse como:

```text
generated_context
```

y no citarse como texto original.

---

# Chunk Hashes

Todo chunk deberá tener varios hashes.

---

# Content Hash

Representa contenido original incluido.

---

# Context Hash

Representa contexto añadido.

---

# Structure Hash

Representa orden y jerarquía.

---

# Security Hash

Representa clasificación y permisos.

---

# Chunking Hash

Representa:

- perfil;
- estrategia;
- límites;
- overlap;
- template;
- processor version.

---

# Composite Chunk Fingerprint

```text
content_hash
+
context_hash
+
structure_hash
+
security_hash
+
chunking_hash
```

---

# Chunk Fingerprint Contract

```yaml
chunk_fingerprint:
  content: ...
  context: ...
  structure: ...
  security: ...
  chunking: ...
  composite: ...
```

---

# Reutilización de chunks

Un chunk podrá reutilizarse cuando coincidan los fingerprints relevantes.

---

# Chunk Lineage

```yaml
lineage:
  chunk: IDX-CHUNK-000041

  source_units:
    - IDX-UNIT-000041
    - IDX-UNIT-000042

  chunk_profile:
    id: CHUNK-PROFILE-RAG-STANDARD
    version: 1.0.0

  processor:
    id: IDX-PROC-CHUNKER-STRUCTURAL
    version: 1.0.0

  execution:
    id: IDX-EXEC-000041
```

---

# Chunk Validation

Todo chunk deberá validarse antes de generar embeddings.

---

# Validaciones

- schema;
- tamaño;
- contenido;
- lineage;
- citas;
- jerarquía;
- seguridad;
- idioma;
- capa epistemológica;
- duplicación;
- truncamiento.

---

# Diagnostic Codes

```text
CHUNK_SCHEMA_INVALID
CHUNK_CONTENT_EMPTY
CHUNK_TOO_SMALL
CHUNK_TOO_LARGE
CHUNK_SOURCE_UNIT_MISSING
CHUNK_LINEAGE_BROKEN
CHUNK_CITATION_MAPPING_INCOMPLETE
CHUNK_SECURITY_METADATA_MISSING
CHUNK_TENANT_MISMATCH
CHUNK_EPISTEMIC_LAYER_MISSING
CHUNK_TRUNCATED
CHUNK_DUPLICATE_LOGICAL_KEY
CHUNK_CONTEXT_TOO_LARGE
```

---

# Chunk Validation Result

```yaml
chunk_validation:
  chunk: IDX-CHUNK-000041

  status: valid

  metrics:
    tokens: 342
    source_units: 3
    citation_coverage: 1.0

  diagnostics:
    errors: 0
    warnings: 0
```

---

# Quality Gate de chunks

```yaml
quality_gate:
  id: QG-CHUNKS-RAG-0001

  criteria:
    all:
      - invalid_chunks == 0
      - missing_lineage == 0
      - missing_security_metadata == 0
      - citation_coverage == 1.0
      - truncated_required_chunks == 0
      - duplicate_logical_keys == 0
```

---

# Métricas de chunking

- chunks totales;
- chunks por tipo;
- tamaño medio;
- mediana;
- percentiles;
- overlap ratio;
- parent-child ratio;
- citation coverage;
- excluded chunks;
- invalid chunks;
- expansion ratio.

---

# Chunk Expansion Ratio

```text
chunks
/
indexable_units
```

---

# Context Ratio

```text
context_tokens
/
total_chunk_tokens
```

---

# Overlap Ratio

```text
duplicated_overlap_tokens
/
total_tokens
```

---

# Embeddings

Un **Embedding** será una representación vectorial derivada de un contenido preparado.

---

# Definición

> Representación numérica obtenida mediante un modelo versionado, destinada a aproximar similitud o relación semántica dentro de un espacio vectorial determinado.

---

# Importante

Un embedding:

- no será conocimiento canónico;
- no será interpretable como hecho;
- no será equivalente al texto original;
- heredará su clasificación;
- dependerá del modelo y configuración utilizados.

---

# Embeddable Input

No todo chunk deberá vectorizarse.

---

# Elegibilidad para embedding

Un chunk deberá cumplir:

- estado `ready`;
- perfil compatible;
- contenido no vacío;
- tamaño permitido;
- seguridad compatible;
- idioma soportado;
- no estar excluido;
- no estar en cuarentena.

---

# Embedding Profile

Un **Embedding Profile** define la configuración gobernada de generación.

Formato recomendado:

```text
EMB-PROFILE-XXXXXX
```

---

# Contrato

```yaml
embedding_profile:
  id: EMB-PROFILE-MULTILINGUAL-0001

  version: 1.0.0
  status: active

  model:
    id: EMB-MODEL-0001
    version: 2.0.0

  input:
    source: contextualized
    maximum_tokens: 800
    truncation: forbidden

  output:
    dimensions: 1024
    normalization: l2

  batching:
    maximum_items: 64
    maximum_tokens: 16000

  cache:
    enabled: true

  security:
    maximum_classification: internal
    external_processing: false
```

---

# Contenido del perfil

- modelo;
- versión;
- tokenizer;
- idioma;
- input projection;
- prefijos;
- dimensiones;
- pooling;
- normalización;
- batching;
- caché;
- seguridad;
- proveedor;
- límites;
- fallback.

---

# Perfiles iniciales

```text
semantic_search
multilingual
short_fact
document
graph
entity
query
preview
local_restricted
```

---

# Perfil `semantic_search`

Adecuado para chunks generales de RAG.

---

# Perfil `multilingual`

Adecuado para consultas y contenido en varios idiomas.

---

# Perfil `short_fact`

Adecuado para:

- statements;
- facts;
- relaciones breves.

---

# Perfil `document`

Adecuado para:

- summaries;
- chunks grandes;
- búsqueda amplia.

---

# Perfil `graph`

Adecuado para:

- paths;
- subgraphs;
- relation textualizations.

---

# Perfil `entity`

Adecuado para:

- labels;
- aliases;
- definiciones;
- entity resolution.

---

# Perfil `query`

Podrá utilizarse para embeddings de consulta si el modelo distingue entre:

```text
query
```

y:

```text
document
```

---

# Perfil `preview`

Aislado y de retención corta.

---

# Perfil `local_restricted`

Obliga a procesamiento local para contenido restringido.

---

# Embedding Model

Todo modelo deberá registrarse.

Formato recomendado:

```text
EMB-MODEL-XXXXXX
```

---

# Model Record

```yaml
embedding_model:
  id: EMB-MODEL-0001

  version: 2.0.0
  status: active

  capabilities:
    languages:
      - es
      - en
      - fr

    maximum_tokens: 8192
    asymmetric_retrieval: true

  output:
    dimensions: 1024

  provider:
    type: internal

  owner:
    team: ai-platform
```

---

# Estados del modelo

```text
experimental
candidate
active
deprecated
retired
blocked
```

---

# Model Provenance

Deberá registrar:

- origen;
- versión;
- checksum;
- licencia;
- fecha;
- evaluación;
- owner.

---

# Selección de modelo

La selección deberá considerar:

- idioma;
- dominio;
- longitud;
- latencia;
- privacidad;
- coste;
- calidad;
- dimensiones;
- infraestructura.

---

# No selección arbitraria por consumidor

Los clientes deberán elegir un perfil, no un modelo libre, salvo APIs administrativas.

---

# Model Routing

Podrá existir en el futuro.

Deberá ser:

- determinista por política;
- trazable;
- versionado;
- evaluable.

---

# Input Projection

Antes de generar embeddings deberá definirse qué contenido se utiliza.

---

# Opciones

```text
original
normalized
contextualized
summary
structured_textualization
```

---

# Recomendación

Para RAG general:

```text
contextualized
```

Para citas exactas:

```text
normalized
```

Para statements:

```text
structured_textualization
```

---

# Input Template

Podrá utilizarse una plantilla.

Formato recomendado:

```text
EMB-INPUT-TEMPLATE-XXXXXX
```

---

# Ejemplo

```yaml
embedding_input_template:
  id: EMB-INPUT-TEMPLATE-RECIPE-0001

  version: 1.0.0

  template: |
    Tipo: receta
    Título: {{document_title}}
    Sección: {{section_path}}
    Contenido: {{content}}
```

---

# Template Hash

Deberá formar parte del Embedding Fingerprint.

---

# Query Prefix y Document Prefix

Algunos modelos podrán utilizar prefijos distintos.

Ejemplo conceptual:

```text
query:
```

```text
document:
```

Deberán definirse en el perfil.

---

# No prompt libre

La entrada de embeddings no deberá aceptar instrucciones arbitrarias del consumidor.

---

# Tokenization

El tokenizer deberá corresponder al modelo.

---

# Token Count

Deberá calcularse antes de invocar el modelo.

---

# Token Count Metadata

```yaml
embedding_input:
  chunk: IDX-CHUNK-000041
  token_count: 342
  tokenizer: EMB-TOKENIZER-0001@1.0.0
```

---

# Maximum Tokens

No deberá superarse.

---

# Truncation Policy

Valores:

```text
forbidden
head
tail
balanced
semantic
summarize
split
```

---

# Recomendación general

```text
forbidden
```

para evitar pérdida silenciosa.

---

# Split

Deberá regresar a chunking y producir nuevos chunks.

---

# Summarize

Solo podrá utilizarse si:

- el perfil lo permite;
- el resumen es derivado;
- conserva lineage;
- se valida;
- no sustituye al original.

---

# Embedding Request

Formato recomendado:

```text
EMB-REQ-XXXXXX
```

---

# Contrato

```yaml
embedding_request:
  id: EMB-REQ-000041

  chunks:
    - IDX-CHUNK-000041
    - IDX-CHUNK-000042

  profile:
    id: EMB-PROFILE-MULTILINGUAL-0001
    version: 1.0.0

  target:
    index: IDX-VECTOR-RAG-0001
```

---

# Embedding Execution

Formato recomendado:

```text
EMB-EXEC-XXXXXX
```

---

# Estados

```text
created
planning
preparing_inputs
checking_cache
batching
generating
validating
completed
completed_with_warnings
partial
failed
cancelled
blocked
```

---

# Embedding Record

Formato recomendado:

```text
EMB-XXXXXX
```

---

# Contrato

```yaml
embedding:
  id: EMB-000041

  chunk:
    id: IDX-CHUNK-000041

  profile:
    id: EMB-PROFILE-MULTILINGUAL-0001
    version: 1.0.0

  model:
    id: EMB-MODEL-0001
    version: 2.0.0

  input:
    fingerprint: ...
    token_count: 342
    projection: contextualized

  vector:
    dimensions: 1024
    normalization: l2

  security:
    tenant: TENANT-0001
    classification: internal

  status: valid
```

---

# Almacenamiento del vector

El contrato conceptual no deberá incluir necesariamente todos los valores numéricos.

Podrá incluir:

- referencia;
- hash;
- dimensiones;
- metadata.

---

# Vector Reference

```yaml
vector_reference:
  provider_record_id: vec-84721
  index_partition: tenant-0001
```

---

# Dimensión

La dimensión deberá coincidir con:

- modelo;
- schema;
- índice.

---

# Error

```text
EMBEDDING_DIMENSION_MISMATCH
```

---

# Pooling

Cuando el modelo lo requiera deberá registrarse.

Valores posibles:

```text
cls
mean
max
weighted_mean
model_default
```

---

# Normalización vectorial

Podrá aplicarse:

```text
none
l2
unit_length
model_default
```

---

# Compatibilidad con métrica

La normalización deberá ser compatible con:

- cosine;
- dot product;
- Euclidean distance.

---

# No cambiar normalización sin nueva versión

Puede alterar ranking.

---

# Quantization

Podrá utilizarse para reducir almacenamiento.

Tipos:

```text
float32
float16
int8
binary
provider_default
```

---

# Riesgo

La cuantización puede degradar calidad.

Deberá evaluarse.

---

# Original Vector

Podrá conservarse para evaluación o reconstrucción según política.

---

# Batch Embedding

La generación deberá agruparse cuando resulte eficiente.

---

# Batch Constraints

- número de items;
- tokens totales;
- tamaño;
- clasificación;
- tenant;
- modelo;
- idioma;
- proveedor.

---

# No mezclar seguridad incompatible

Un batch no deberá mezclar contenido con requisitos de procesamiento incompatibles.

---

# Batch Contract

```yaml
embedding_batch:
  id: EMB-BATCH-000041

  profile: EMB-PROFILE-MULTILINGUAL-0001

  chunks:
    count: 48

  tokens:
    total: 15320

  security:
    tenant: TENANT-0001
    maximum_classification: internal

  status: completed
```

---

# Dynamic Batching

Podrá ajustar el tamaño según:

- tokens;
- latencia;
- límites;
- memoria.

---

# Batch Ordering

La respuesta deberá mapearse de forma segura a cada chunk.

---

# Missing Batch Result

Deberá detectarse.

Error:

```text
EMBEDDING_BATCH_RESULT_MISSING
```

---

# Retry de batch

Los errores transitorios podrán reintentarse.

---

# Retry por item

Cuando sea posible deberá aislarse la unidad fallida.

---

# Embedding Cache

La caché permitirá reutilizar embeddings compatibles.

---

# Cache Key

Deberá incluir:

```text
input fingerprint
+
model ID
+
model version
+
profile version
+
template hash
+
normalization
```

---

# No reutilizar solo por content hash

Dos entradas iguales con contexto o perfil distinto pueden requerir embeddings distintos.

---

# Cache Record

```yaml
embedding_cache_entry:
  key: ...

  embedding:
    id: EMB-000041

  created_at: 2026-08-01T20:00:00Z

  model:
    id: EMB-MODEL-0001
    version: 2.0.0

  security:
    tenant: TENANT-0001
    classification: internal
```

---

# Seguridad de caché

La caché deberá:

- aislar tenants;
- respetar clasificación;
- cifrarse;
- invalidarse;
- aplicar retención.

---

# Cross-Tenant Reuse

Deberá prohibirse por defecto.

---

# Reuse con contenido público

Podrá considerarse únicamente bajo política explícita.

---

# Embedding Fingerprint

Deberá incluir:

- chunk composite fingerprint;
- input projection;
- context template;
- tokenizer;
- model;
- model version;
- pooling;
- normalization;
- dimensions.

---

# Contrato

```yaml
embedding_fingerprint:
  chunk: ...
  input_projection: contextualized
  template: ...
  tokenizer: ...
  model: EMB-MODEL-0001@2.0.0
  pooling: model_default
  normalization: l2
  composite: ...
```

---

# Embedding Lineage

```yaml
lineage:
  embedding: EMB-000041

  chunk:
    id: IDX-CHUNK-000041

  source_units:
    - IDX-UNIT-000041

  model:
    id: EMB-MODEL-0001
    version: 2.0.0

  profile:
    id: EMB-PROFILE-MULTILINGUAL-0001
    version: 1.0.0

  execution:
    id: EMB-EXEC-000041
```

---

# Embedding Validation

Todo embedding deberá validarse antes de indexarse.

---

# Validaciones estructurales

- vector presente;
- dimensiones;
- valores numéricos;
- no NaN;
- no infinitos;
- norma;
- mapping;
- metadata;
- seguridad.

---

# Validaciones estadísticas

- distribución;
- norma;
- duplicados;
- colapso;
- outliers;
- densidad.

---

# Zero Vector

Un vector nulo deberá considerarse inválido salvo justificación específica.

---

# Near-Duplicate Vectors

Podrán indicar:

- contenido duplicado;
- colapso del modelo;
- plantilla dominante;
- error de procesamiento.

---

# Embedding Validation Result

```yaml
embedding_validation:
  embedding: EMB-000041

  status: valid

  metrics:
    dimensions: 1024
    norm: 1.0
    contains_nan: false
    contains_infinity: false
```

---

# Diagnostic Codes

```text
EMBEDDING_INPUT_TOO_LARGE
EMBEDDING_INPUT_EMPTY
EMBEDDING_MODEL_NOT_AVAILABLE
EMBEDDING_MODEL_NOT_ALLOWED
EMBEDDING_DIMENSION_MISMATCH
EMBEDDING_VECTOR_MISSING
EMBEDDING_VECTOR_INVALID
EMBEDDING_ZERO_VECTOR
EMBEDDING_CONTAINS_NAN
EMBEDDING_CONTAINS_INFINITY
EMBEDDING_MAPPING_MISSING
EMBEDDING_SECURITY_METADATA_MISSING
EMBEDDING_CACHE_SCOPE_MISMATCH
EMBEDDING_BATCH_RESULT_MISSING
EMBEDDING_OUTPUT_SCHEMA_INVALID
```

---

# Semantic Validation

Podrán utilizarse pruebas de vecinos conocidos.

---

# Canary Queries

Ejemplos:

- “miso” debe recuperar ingredientes fermentados;
- “olla rápida” debe relacionarse con olla a presión;
- una receta no debe confundirse con una técnica.

---

# Retrieval Evaluation

La calidad de embeddings deberá evaluarse mediante:

- recall;
- precision;
- MRR;
- nDCG;
- hit rate;
- semantic similarity;
- human judgment.

---

# No evaluar únicamente distancia

La utilidad real deberá medirse en retrieval.

---

# Embedding Quality Gate

```yaml
quality_gate:
  id: QG-EMBEDDINGS-RAG-0001

  criteria:
    all:
      - missing_embeddings == 0
      - invalid_vectors == 0
      - dimension_mismatches == 0
      - security_metadata_missing == 0
      - retrieval_recall_at_10 >= 0.85
      - retrieval_ndcg_at_10 >= 0.80
```

---

# Dataset de evaluación

Deberá incluir:

- consultas frecuentes;
- consultas difíciles;
- sinónimos;
- multilingüismo;
- negaciones;
- cantidades;
- relaciones;
- consultas sin respuesta.

---

# Ground Truth

Podrá construirse mediante:

- anotación humana;
- relaciones canónicas;
- logs revisados;
- reglas;
- datasets sintéticos validados.

---

# Hard Negatives

Deberán incluirse resultados semánticamente próximos, pero incorrectos.

---

# Ejemplo

Consulta:

```text
miso blanco
```

Hard negative:

```text
salsa de soja
```

---

# Evaluación por tipo

Deberá separarse para:

- recetas;
- ingredientes;
- técnicas;
- statements;
- relaciones;
- procedimientos.

---

# Evaluación multilingüe

Deberá comprobar:

- consulta y documento en mismo idioma;
- consulta y documento en idiomas distintos;
- aliases;
- transliteraciones.

---

# Model Comparison

Los modelos candidatos deberán compararse bajo el mismo:

- dataset;
- chunk profile;
- index;
- retrieval configuration.

---

# A/B Testing

Podrá utilizarse tras superar validación offline.

---

# Shadow Evaluation

El nuevo modelo podrá recibir consultas sin afectar respuestas.

---

# No activación por coste únicamente

El modelo deberá cumplir mínimos de calidad y seguridad.

---

# Embedding Drift

Puede producirse cuando cambian:

- contenido;
- modelo;
- proveedor;
- tokenizer;
- template;
- distribución del corpus.

---

# Drift Detection

Podrá medir:

- distribución de normas;
- vecinos;
- centroides;
- recall;
- query performance;
- error rates.

---

# Model Upgrade

Un cambio de modelo deberá producir:

- nuevo Embedding Profile;
- nuevos fingerprints;
- nuevo vector index;
- evaluación;
- snapshot candidato;
- activación explícita.

---

# Dual Embedding

Podrán coexistir dos modelos durante una migración.

---

# No mezclar espacios vectoriales

Vectores de modelos o dimensiones incompatibles no deberán consultarse juntos como si pertenecieran al mismo espacio.

---

# Vector Space ID

Formato recomendado:

```text
VSPACE-XXXXXX
```

---

# Contrato

```yaml
vector_space:
  id: VSPACE-MULTILINGUAL-0001

  model: EMB-MODEL-0001@2.0.0
  dimensions: 1024
  normalization: l2
  metric: cosine
```

---

# Vector Space Compatibility

Dos embeddings serán comparables únicamente si pertenecen a espacios compatibles.

---

# Query Embeddings

Las consultas deberán utilizar un perfil compatible con los documentos.

---

# Asymmetric Models

Podrán requerir:

- query profile;
- document profile.

---

# Query Embedding Contract

```yaml
query_embedding:
  id: QEMB-000041

  query_execution: RET-EXEC-000041

  profile:
    id: EMB-PROFILE-QUERY-0001

  vector_space:
    id: VSPACE-MULTILINGUAL-0001
```

---

# Privacidad de embeddings

Los embeddings deberán tratarse como datos derivados potencialmente sensibles.

---

# Riesgos

- memorización parcial;
- membership inference;
- correlación;
- reconstrucción aproximada;
- fuga entre tenants.

---

# Reglas

- heredar clasificación;
- aislar tenants;
- cifrar;
- limitar exportación;
- aplicar retención;
- auditar acceso;
- eliminar al borrar fuente.

---

# External Embedding Providers

Solo podrán utilizarse cuando:

- la clasificación lo permita;
- exista contrato;
- la región sea válida;
- la retención esté controlada;
- el proveedor no use datos indebidamente;
- la transferencia esté autorizada.

---

# Request Minimization

Solo deberá enviarse el texto necesario.

---

# Redaction

Podrá aplicarse antes de externalización.

---

# Local Processing

Será obligatorio para perfiles restringidos cuando la política lo exija.

---

# Provider Logs

Deberán evaluarse:

- contenido;
- retención;
- identifiers;
- prompts;
- metadata.

---

# No enviar IDs sensibles innecesarios

Los proveedores externos no necesitarán conocer:

- tenant ID real;
- user ID;
- resource ID canónico;

salvo necesidad justificada.

---

# Data Residency

Deberá respetarse por tenant y clasificación.

---

# Embedding Deletion

La eliminación de un recurso deberá propagarse a:

- embedding record;
- vector index;
- caches;
- replicas;
- backups según política.

---

# Embedding Export

Deberá restringirse.

---

# Reidentification Risk

La exportación masiva de embeddings deberá considerarse de alto riesgo.

---

# Seguridad de chunks

Los chunks también deberán tratarse como datos derivados sensibles.

---

# Context Leakage

El contexto añadido no deberá revelar información fuera del scope.

---

# Cross-Classification Context

No deberá añadirse contexto de clasificación superior a un chunk menos restringido sin elevar su clasificación.

---

# Cross-Tenant Context

Deberá prohibirse.

---

# Prompt Injection en chunking asistido

Los modelos utilizados para segmentar o contextualizar deberán recibir instrucciones de sistema controladas.

El documento deberá tratarse como datos.

---

# Output Schema

La salida deberá validarse.

---

# No ejecución de contenido

Un chunk no deberá provocar herramientas o comandos.

---

# Chunk Quarantine

Los chunks sospechosos deberán aislarse.

---

# Coste

La generación de embeddings deberá medir:

- requests;
- tokens;
- batches;
- latency;
- provider cost;
- cache hits;
- retries;
- failures.

---

# Cost Budget

```yaml
embedding_budget:
  maximum_tokens: 1000000
  maximum_cost: 25.00
  currency: EUR
  maximum_duration: PT30M
```

---

# Budget Exceeded

La ejecución podrá:

- pausar;
- fallar;
- producir partial;
- solicitar aprobación.

---

# No activar índice incompleto

---

# Observabilidad de chunking

---

# Métricas

- chunks generados;
- chunks excluidos;
- size distribution;
- overlap ratio;
- context ratio;
- citation coverage;
- invalid chunks;
- parent-child mappings.

---

# Observabilidad de embeddings

---

# Métricas

- embeddings generados;
- cache hit rate;
- token count;
- batch size;
- latency;
- error rate;
- cost;
- vector validation failures;
- model usage.

---

# Métricas por modelo

- throughput;
- p50;
- p95;
- p99;
- cost per 1000 units;
- recall;
- nDCG.

---

# Logs

Deberán incluir:

- execution ID;
- profile;
- model;
- batch;
- counts;
- duration;
- error.

---

# No contenido en logs

No deberá registrarse el texto completo.

---

# Tracing

```text
Chunk Plan
↓
Chunk Build
↓
Context Enrichment
↓
Chunk Validation
↓
Embedding Input
↓
Cache Lookup
↓
Model Invocation
↓
Vector Validation
↓
Artifact Storage
```

---

# Auditoría

Deberán auditarse:

- cambio de Chunk Profile;
- cambio de Context Template;
- cambio de modelo;
- cambio de proveedor;
- cambio de dimensión;
- cambio de normalización;
- exportación de embeddings;
- activación de un nuevo vector space.

---

# Eventos

Catálogo inicial:

```text
chunking_started
chunk_created
chunk_excluded
chunk_validation_completed
embedding_generation_started
embedding_cache_hit
embedding_batch_completed
embedding_generated
embedding_validation_completed
embedding_generation_failed
embedding_profile_activated
embedding_model_deprecated
```

---

# Evento de embedding generado

```yaml
event:
  type: embedding_generated

  subject:
    id: EMB-000041
    type: embedding

  data:
    chunk: IDX-CHUNK-000041
    model: EMB-MODEL-0001@2.0.0
    vector_space: VSPACE-MULTILINGUAL-0001
```

---

# Resiliencia

El sistema deberá tolerar:

- timeout del modelo;
- rate limiting;
- batch parcial;
- worker failure;
- caché no disponible;
- almacenamiento temporal caído.

---

# Checkpoints

Podrán crearse:

```text
after_chunk_planning
after_chunking
after_chunk_validation
after_input_preparation
after_cache_resolution
after_embedding_generation
after_embedding_validation
```

---

# Reanudación

Deberá comprobar:

- Chunk Profile;
- Embedding Profile;
- modelo;
- vector space;
- fingerprints;
- seguridad;
- fuente.

---

# Model Unavailable

Podrá:

- reintentar;
- usar fallback autorizado;
- pausar;
- fallar.

---

# Fallback Model

Solo podrá utilizarse si:

- está declarado en el perfil;
- es compatible;
- produce un espacio separado;
- se registra;
- supera Gate.

---

# No fallback silencioso

---

# Partial Embedding Set

Podrá conservarse para diagnóstico.

No deberá activar un vector index completo bajo perfil estricto.

---

# Poison Chunk

Un chunk que falla repetidamente deberá:

- aislarse;
- generar diagnóstico;
- conservar lineage;
- bloquear si es obligatorio.

---

# Casos de uso

---

# Caso de uso 1 — Sección extensa

Una sección de 1800 tokens se divide mediante:

```text
Paragraph Boundaries
↓
Semantic Cohesion
↓
Maximum Token Limit
```

Se producen cuatro chunks con parent común.

---

# Caso de uso 2 — Paso dependiente

El paso:

```text
Añadirlo a la mezcla.
```

no es comprensible solo.

El chunk añade:

- receta;
- sección;
- referente resuelto.

---

# Caso de uso 3 — Tabla

Una tabla de equivalencias se divide por grupos de filas.

Cada chunk repite:

- título;
- headers;
- unidades.

---

# Caso de uso 4 — Statement

El Statement se conserva atómico y se textualiza en español para embeddings.

---

# Caso de uso 5 — Modelo nuevo

Se introduce un modelo de 1536 dimensiones.

El sistema crea:

- nuevo Embedding Profile;
- nuevo Vector Space;
- nuevos embeddings;
- nuevo índice;
- evaluación independiente.

---

# Caso de uso 6 — Cache hit

El chunk y su fingerprint no cambiaron.

Se reutiliza el embedding existente.

---

# Caso de uso 7 — Cambio de contexto

El texto permanece igual, pero cambia el título de sección.

El Context Hash cambia.

El embedding contextual deberá regenerarse.

---

# Caso de uso 8 — Cambio de ACL

El texto permanece igual.

El Security Hash cambia.

El embedding puede reutilizarse solo si la política y el almacenamiento permiten actualizar metadata sin riesgo.

---

# Caso de uso 9 — Contenido restringido

El perfil obliga a modelo local.

No se permite proveedor externo.

---

# Caso de uso 10 — Oversized input

Un chunk supera el máximo.

La ejecución regresa a chunking.

No se trunca silenciosamente.

---

# Caso de uso 11 — Query-document asymmetry

Las consultas usan un prefijo diferente al contenido documental, pero comparten Vector Space compatible.

---

# Caso de uso 12 — Chunk duplicado

Dos chunks comparten contenido, pero poseen distinta procedencia.

Pueden compartir embedding si la política lo permite, pero deberán mantener registros y citas independientes.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Dividir únicamente por caracteres

Ignora estructura y semántica.

---

## Usar un tamaño universal

Los tipos de contenido requieren estrategias distintas.

---

## Crear chunks sin citas

Impide grounding verificable.

---

## Sobrescribir contenido original con contexto

Confunde fuente y enriquecimiento.

---

## Añadir todo el documento como contexto

Diluirá el significado y aumentará coste.

---

## Overlap fijo en todos los tipos

Produce duplicación innecesaria.

---

## Cortar procedimientos sin conservar orden

Puede alterar instrucciones.

---

## Separar una tabla de sus headers

Descontextualiza valores.

---

## Dividir Statements

Puede destruir su significado.

---

## Fusionar chunks con seguridad incompatible

Puede ampliar acceso.

---

## Usar IDs aleatorios sin logical key

Dificulta incremental indexing.

---

## Truncar inputs para embeddings

Puede perder información crítica.

---

## Reutilizar embeddings solo por texto

Ignora contexto, modelo y seguridad.

---

## Mezclar vectores de modelos distintos

Las distancias dejan de ser comparables.

---

## Cambiar dimensión en el mismo índice

Rompe schema y consultas.

---

## No registrar tokenizer

Impide reproducibilidad.

---

## Ocultar el pooling utilizado

Puede alterar resultados.

---

## Utilizar un modelo externo para contenido restringido

Compromete privacidad.

---

## Compartir caché entre tenants

Puede filtrar información.

---

## Exportar embeddings sin control

Amplía riesgo de reidentificación.

---

## Evaluar calidad solo mediante similitud

No mide retrieval real.

---

## Activar modelo sin dataset de evaluación

Impide conocer regresiones.

---

## Usar queries reales sin controles de privacidad

Puede exponer datos personales.

---

## Permitir fallback silencioso

Rompe reproducibilidad.

---

## Tratar embeddings como conocimiento

Son representaciones derivadas.

---

## Considerar alta similitud como verdad

No implica corrección factual.

---

## Generar summaries sin lineage

Impide justificar su contenido.

---

## Aceptar salida de chunking asistido sin schema

Puede producir límites corruptos.

---

## No recalcular tras cambiar template

El espacio semántico puede variar.

---

## No medir context ratio

Puede ocultar sobrecontextualización.

---

## No detectar zero vectors

Puede degradar el índice.

---

## Activar embeddings parciales

Produce pérdida de cobertura.

---

# Reglas mínimas de conformidad

---

## Chunk Profile versionado

Toda estrategia deberá utilizar un perfil identificado.

---

## Chunk Identity

Todo chunk deberá tener ID y logical key.

---

## Source Mapping

Todo chunk deberá enlazar con unidades indexables.

---

## Citation Mapping

Todo contenido original deberá ser citable.

---

## Context Separation

El contexto añadido deberá diferenciarse.

---

## Security Propagation

Todo chunk deberá conservar tenant y clasificación.

---

## Size Validation

Todo chunk deberá respetar límites.

---

## No Silent Truncation

Toda truncación deberá bloquear o diagnosticarse.

---

## Hierarchy Preserved

Los chunks parent-child deberán conservar mappings.

---

## Fingerprints

Todo chunk deberá disponer de fingerprints.

---

## Embedding Profile versionado

Toda generación deberá declarar perfil.

---

## Model Registered

Todo modelo deberá estar registrado y aprobado.

---

## Vector Space Identified

Todo embedding deberá pertenecer a un espacio conocido.

---

## Dimension Validation

La dimensión deberá coincidir con el schema.

---

## Cache Safety

La reutilización deberá considerar contenido, contexto, modelo y seguridad.

---

## Embedding Lineage

Todo vector deberá enlazar con su chunk.

---

## Vector Validation

No deberán indexarse vectores inválidos.

---

## Evaluation Required

Todo modelo candidato deberá evaluarse.

---

## Privacy Preserved

Los embeddings deberán heredar clasificación y retención.

---

## Quality Gate

Los conjuntos de chunks y embeddings deberán superar Gate.

---

# Conformidad de Chunk Profile

Será conforme cuando:

- tenga ID;
- tenga versión;
- declare estrategia;
- declare tamaños;
- declare overlap;
- declare contexto;
- declare jerarquía;
- declare validadores.

---

# Conformidad de Chunk

Será conforme cuando:

- tenga identidad;
- declare tipo;
- conserve source units;
- preserve canonical pointer;
- preserve citations;
- declare seguridad;
- declare capa epistemológica;
- tenga hashes;
- respete tamaño.

---

# Conformidad de Parent-Child Mapping

Será conforme cuando:

- identifique parent;
- identifique children;
- preserve orden;
- evite ciclos;
- permita expansión.

---

# Conformidad de Table Chunk

Será conforme cuando:

- conserve headers;
- conserve unidades;
- preserve filas;
- preserve contexto;
- conserve posición.

---

# Conformidad de Procedure Chunk

Será conforme cuando:

- preserve orden;
- preserve dependencias;
- declare secuencia;
- declare contexto;
- no altere instrucciones.

---

# Conformidad de Embedding Profile

Será conforme cuando:

- declare modelo;
- declare versión;
- declare input projection;
- declare tokenizer;
- declare dimensiones;
- declare normalización;
- declare seguridad;
- declare batching;
- declare caché.

---

# Conformidad de Embedding

Será conforme cuando:

- identifique chunk;
- identifique perfil;
- identifique modelo;
- identifique vector space;
- tenga dimensiones correctas;
- no contenga valores inválidos;
- preserve seguridad;
- preserve lineage.

---

# Conformidad de Embedding Cache

Será conforme cuando:

- utilice fingerprint completo;
- preserve tenant;
- preserve clasificación;
- cifre datos;
- soporte invalidación;
- tenga retención.

---

# Lista de comprobación

Antes de aprobar chunks y embeddings deberá comprobarse:

```text
[ ] El Chunk Profile está versionado.
[ ] La estrategia primaria está definida.
[ ] El fallback está definido.
[ ] Los tamaños mínimo, objetivo y máximo están definidos.
[ ] La unidad de medida está declarada.
[ ] El overlap está justificado.
[ ] El contexto añadido está limitado.
[ ] El contenido original se conserva.
[ ] Los chunks tienen logical key.
[ ] Los chunks conservan source units.
[ ] Los chunks conservan canonical pointers.
[ ] Los chunks conservan citation mappings.
[ ] Los chunks conservan tenant y clasificación.
[ ] Los procedimientos conservan orden.
[ ] Las tablas conservan headers.
[ ] Los Statements permanecen atómicos.
[ ] Los parent-child mappings son válidos.
[ ] Los Chunk Fingerprints están calculados.
[ ] No existe truncamiento silencioso.
[ ] El Quality Gate de chunks ha finalizado.
[ ] El Embedding Profile está versionado.
[ ] El modelo está registrado.
[ ] El tokenizer es compatible.
[ ] La dimensión está definida.
[ ] El Vector Space está identificado.
[ ] La normalización está definida.
[ ] El input projection está definido.
[ ] El template está versionado.
[ ] El token count está validado.
[ ] La caché utiliza fingerprint completo.
[ ] La caché respeta tenant y clasificación.
[ ] Los batches respetan límites.
[ ] Los vectores no contienen NaN ni infinitos.
[ ] Los vectores nulos están detectados.
[ ] El mapping chunk-embedding está completo.
[ ] El lineage está completo.
[ ] La evaluación offline ha superado los mínimos.
[ ] La privacidad del proveedor ha sido revisada.
[ ] El Quality Gate de embeddings ha finalizado.
```

---

# Arquitectura final de la Parte III

```text
Validated Indexable Units
        ↓
Chunk Profile Resolution
        ↓
Chunk Planning
        ↓
Structural and Semantic Chunking
        ↓
Context Enrichment
        ↓
Citation Mapping
        ↓
Chunk Validation
        ↓
Embedding Profile Resolution
        ↓
Input Projection
        ↓
Cache Lookup
        ↓
Batch Embedding
        ↓
Vector Validation
        ↓
Validated Embeddings
        ↓
Vector Index Builder
```

---

# Transición hacia la Parte IV

Esta tercera parte ha definido:

- el concepto de chunk;
- la diferencia entre unidad y chunk;
- los Chunk Profiles;
- las estrategias de chunking;
- el Chunk Plan;
- los límites;
- el overlap;
- los chunks documentales;
- los chunks semánticos;
- los chunks de procedimientos;
- los chunks de tablas;
- los chunks de Statements;
- los chunks de entidades;
- los chunks de relaciones;
- los chunks de grafo;
- parent-child retrieval;
- contextual retrieval;
- las plantillas de contexto;
- los Citation Mappings;
- los Chunk Fingerprints;
- la validación de chunks;
- los Embedding Profiles;
- los modelos;
- los Input Templates;
- tokenización;
- truncation policies;
- batching;
- caché;
- fingerprints;
- lineage;
- Vector Spaces;
- validación vectorial;
- evaluación;
- privacidad;
- seguridad;
- coste;
- observabilidad;
- eventos;
- resiliencia;
- antipatrones;
- reglas de conformidad.

La Parte IV desarrollará en detalle los builders y estructuras de índice, incluyendo:

- Lexical Index;
- analyzers;
- tokenización léxica;
- campos;
- boosting;
- facetas;
- Vector Index;
- métricas de distancia;
- Approximate Nearest Neighbor;
- particiones;
- Structured Index;
- Metadata Index;
- Entity Index;
- Statement Index;
- Citation Index;
- Graph Index;
- Path Index;
- índices híbridos;
- schemas;
- mappings;
- consistencia entre índices;
- validación de builders;
- contratos de publicación.

---

# Conclusión

El chunking y la generación de embeddings constituyen la transformación mediante la que las unidades indexables se convierten en representaciones adecuadas para recuperación semántica.

El ciclo puede resumirse así:

```text
Analizar unidad
        ↓
Elegir estrategia
        ↓
Determinar límites
        ↓
Construir chunks
        ↓
Añadir contexto
        ↓
Preservar citas
        ↓
Validar
        ↓
Preparar input
        ↓
Generar embedding
        ↓
Validar vector
        ↓
Registrar lineage
```

El Chunk Profile define la estrategia.

Los límites estructurales preservan organización.

Los límites semánticos preservan significado.

El overlap mantiene continuidad cuando resulta necesario.

Los parent chunks aportan contexto.

Los child chunks aportan precisión.

Las citas conectan cada fragmento con su origen.

Los fingerprints permiten reutilización segura.

El Embedding Profile gobierna modelo y configuración.

El Vector Space garantiza comparabilidad.

La caché reduce coste sin sacrificar trazabilidad.

La validación evita vectores corruptos.

La evaluación comprueba utilidad real.

La seguridad protege contenido derivado.

Un chunk correcto deberá poder responder:

```text
¿Qué contenido representa?

¿Qué unidades lo originaron?

¿Por qué se eligieron esos límites?

¿Qué contexto se añadió?

¿Qué parte es original?

¿Cómo se cita?

¿Qué seguridad hereda?

¿Qué Chunk Profile lo construyó?
```

Un embedding correcto deberá poder responder:

```text
¿Qué chunk representa?

¿Qué input exacto recibió el modelo?

¿Qué modelo y versión se utilizaron?

¿Qué tokenizer y template se aplicaron?

¿A qué Vector Space pertenece?

¿Qué dimensión posee?

¿Qué fingerprint permite reutilizarlo?

¿Qué evaluación y Quality Gate superó?
```

Con esta tercera parte queda formalizada la transformación de unidades indexables en chunks y embeddings seguros, versionados, reproducibles y preparados para recuperación semántica.

La siguiente parte definirá las estructuras concretas donde estas representaciones serán almacenadas y consultadas: los índices léxicos, vectoriales, estructurados, semánticos y de grafo.

---

# Parte IV — Builders y estructuras de índice: lexical, vectorial, estructurado, semántico y de grafo

---

# Introducción

La Parte III ha definido cómo NovaCoquinaria transforma unidades indexables en:

- chunks;
- parent chunks;
- child chunks;
- representaciones contextualizadas;
- Citation Mappings;
- embeddings;
- Vector Spaces;
- artefactos validados.

Esta cuarta parte desarrolla las estructuras concretas en las que esas representaciones deberán almacenarse para permitir:

- búsqueda léxica;
- búsqueda semántica;
- filtrado;
- facetas;
- navegación por entidades;
- recuperación de Statements;
- citación;
- consultas de grafo;
- recuperación híbrida;
- GraphRAG.

Conceptualmente:

```text
Validated Units
    ├── Textual Content
    ├── Structured Metadata
    ├── Embeddings
    ├── Entities
    ├── Statements
    ├── Relations
    └── Citation Mappings
            ↓
        Index Builders
            ├── Lexical Builder
            ├── Vector Builder
            ├── Structured Builder
            ├── Metadata Builder
            ├── Entity Builder
            ├── Statement Builder
            ├── Citation Builder
            └── Graph Builder
                    ↓
             Index Components
                    ↓
           Composite Index Snapshot
```

Los builders no deberán limitarse a insertar registros en un proveedor concreto.

Deberán transformar artefactos validados en estructuras:

- coherentes;
- versionadas;
- seguras;
- optimizadas;
- reproducibles;
- compatibles con Retrieval.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- formalizar el concepto de Index Builder;
- definir contratos comunes de construcción;
- establecer schemas y mappings;
- definir el Lexical Index;
- formalizar analyzers y tokenización;
- definir campos, boosting y facetas;
- establecer el Vector Index;
- formalizar métricas de distancia;
- definir Approximate Nearest Neighbor;
- establecer particiones vectoriales;
- definir el Structured Index;
- formalizar el Metadata Index;
- definir Entity Index;
- definir Statement Index;
- definir Relation Index;
- formalizar Citation Index;
- establecer Graph Index;
- definir Path Index;
- definir Subgraph Index;
- formalizar índices híbridos;
- regular consistencia entre índices;
- definir publicación de componentes;
- establecer validaciones;
- definir Quality Gates;
- regular seguridad;
- establecer observabilidad;
- preparar la indexación incremental de la Parte V.

---

# Principios de los builders

Todo builder deberá respetar los siguientes principios.

---

## Entrada validada

Un builder solo deberá consumir artefactos conformes con los schemas de entrada.

---

## Salida tipada

La salida deberá ajustarse a un Index Schema versionado.

---

## Determinismo controlado

La misma entrada y configuración deberán producir resultados equivalentes.

---

## No pérdida de lineage

Toda entrada física deberá conservar referencia hacia:

- chunk;
- unidad;
- recurso;
- snapshot;
- ejecución.

---

## Independencia tecnológica

El contrato no deberá depender de:

- Elasticsearch;
- OpenSearch;
- Solr;
- PostgreSQL;
- Neo4j;
- Qdrant;
- Milvus;
- Pinecone;
- Weaviate;
- un proveedor concreto.

---

## Mappings explícitos

La transformación entre artefacto lógico y registro físico deberá documentarse.

---

## Seguridad incorporada

Tenant, clasificación, visibilidad y permisos deberán formar parte del registro indexado o de su partición segura.

---

## Consistencia de snapshot

Un builder deberá trabajar sobre una versión fija del conjunto de entrada.

---

## Idempotencia

La repetición de un build no deberá duplicar entradas lógicas.

---

## Validación posterior

Construir físicamente un índice no implica que sea válido.

---

## Métricas reproducibles

Todo builder deberá producir métricas estructuradas.

---

## Separación entre build y activation

Un componente construido permanecerá candidato hasta su activación.

---

## Compatibilidad explícita

Cada builder deberá declarar:

- schemas soportados;
- perfiles;
- consumidores;
- versión de salida.

---

# Index Builder

Un **Index Builder** será el componente encargado de convertir artefactos validados en entradas de un tipo concreto de índice.

Formato recomendado:

```text
IDX-BUILDER-XXXXXX
```

---

# Contrato

```yaml
index_builder:
  id: IDX-BUILDER-VECTOR-RAG

  version: 1.0.0
  status: active

  index_type: vector

  input_schemas:
    - EMBEDDING-RECORD@1.0.0
    - CHUNK-METADATA@1.0.0

  output_schema:
    id: IDX-SCHEMA-VECTOR-RAG
    version: 1.0.0

  capabilities:
    incremental: true
    deletion: true
    partitioning: true
    snapshot_build: true
```

---

# Estados

```text
draft
experimental
active
deprecated
retired
blocked
```

---

# Builder Execution

Cada ejecución deberá poseer identidad.

Formato recomendado:

```text
IDX-BUILD-EXEC-XXXXXX
```

---

# Contrato

```yaml
builder_execution:
  id: IDX-BUILD-EXEC-000041

  builder:
    id: IDX-BUILDER-VECTOR-RAG
    version: 1.0.0

  indexing_execution:
    id: IDX-EXEC-000041

  target:
    index: IDX-VECTOR-RAG-0001

  status: completed

  metrics:
    input_records: 12450
    output_entries: 12450
    failed_entries: 0
```

---

# Estados de ejecución

```text
created
preparing
mapping
building
flushing
validating
completed
completed_with_warnings
partial
failed
cancelled
blocked
```

---

# Build Manifest

Cada builder deberá producir un manifest.

---

# Contrato

```yaml
build_manifest:
  id: IDX-BUILD-MANIFEST-000041

  builder_execution:
    id: IDX-BUILD-EXEC-000041

  index:
    id: IDX-VECTOR-RAG-0001

  index_snapshot:
    id: IDX-VEC-SNAP-000041

  source:
    chunks: 12450
    embeddings: 12450

  output:
    entries: 12450
    partitions: 4
    storage_bytes: 348000000

  checksum:
    algorithm: sha256
    value: ...
```

---

# Index Mapping

Un **Index Mapping** definirá cómo se transforma un artefacto lógico en un registro indexado.

Formato recomendado:

```text
IDX-MAPPING-XXXXXX
```

---

# Ejemplo

```yaml
index_mapping:
  id: IDX-MAPPING-CHUNK-TO-VECTOR

  version: 1.0.0

  source_schema:
    id: CHUNK-WITH-EMBEDDING
    version: 1.0.0

  target_schema:
    id: IDX-SCHEMA-VECTOR-RAG
    version: 1.0.0

  fields:
    chunk.id: record_id
    chunk.logical_key: logical_key
    embedding.vector: vector
    chunk.content.contextualized: searchable_text
    chunk.security.tenant: tenant_id
    chunk.security.classification: classification
    chunk.canonical_pointer.resource.id: resource_id
```

---

# Mapping Version

Todo cambio de semántica deberá generar una nueva versión.

---

# Transformación de campo

Podrá incluir:

```text
copy
rename
normalize
flatten
expand
derive
hash
omit
encrypt
```

---

# Campo derivado

Deberá registrar:

- fórmula;
- procesador;
- versión;
- origen.

---

# No mapping implícito

Las asociaciones críticas no deberán depender de convenciones no documentadas.

---

# Index Entry común

Todos los tipos de índice deberán compartir campos transversales.

---

# Campos mínimos

```yaml
index_entry:
  id:
  logical_key:
  index_id:
  index_snapshot_id:
  source_unit_ids:
  chunk_id:
  resource_id:
  resource_type:
  source_snapshot_id:
  tenant_id:
  classification:
  status:
  created_at:
  fingerprint:
```

---

# Campos opcionales

```text
document_id
block_id
entity_ids
statement_ids
relation_ids
language
collection_ids
quality
epistemic_layer
valid_from
valid_until
```

---

# Entry Status

```text
candidate
active
stale
invalidated
deleted
quarantined
```

---

# Entry Fingerprint

Deberá incluir:

- contenido relevante;
- mapping;
- schema;
- builder;
- seguridad;
- configuración.

---

# Physical Entry ID

Podrá ser específico del proveedor.

No deberá sustituir a `logical_key`.

---

# Lexical Index

El **Lexical Index** optimiza recuperación basada en términos y campos textuales.

---

# Casos de uso

- búsqueda exacta;
- búsqueda por palabras;
- frases;
- prefijos;
- aliases;
- búsqueda de títulos;
- búsqueda documental;
- autocompletado;
- filtros textuales;
- ranking BM25 o equivalente.

---

# Lexical Index ID

Formato recomendado:

```text
IDX-LEX-XXXXXX
```

---

# Lexical Entry

```yaml
lexical_entry:
  id: IDX-LEX-ENTRY-000041

  logical_key: REC-0009#PREPARATION#WINDOW-01

  title: Sopa de miso

  body: |
    Calentar el caldo.
    Añadir las verduras.
    Incorporar el tofu.

  contextual_text: |
    Receta: Sopa de miso.
    Sección: Preparación.
    Pasos 1 a 3.

  aliases:
    - sopa japonesa de miso

  resource_id: REC-0009
  resource_type: recipe
  chunk_id: IDX-CHUNK-000041
  language: es

  tenant_id: TENANT-0001
  classification: internal
```

---

# Lexical Schema

Deberá distinguir campos según función.

---

# Campos posibles

```text
id
logical_key
title
body
contextual_text
aliases
keywords
entity_labels
section_path
resource_type
language
status
collection_ids
tenant_id
classification
```

---

# Campo `title`

Podrá recibir mayor peso.

---

# Campo `body`

Contendrá contenido principal.

---

# Campo `contextual_text`

Podrá utilizarse para mejorar recall.

No deberá sustituir a `body`.

---

# Campo `aliases`

Adecuado para:

- sinónimos;
- transliteraciones;
- nombres alternativos;
- abreviaturas.

---

# Campo `keywords`

Deberá contener términos gobernados o derivados.

---

# Field Types

Un mismo valor podrá indexarse mediante varias representaciones.

Ejemplo:

```text
analyzed text
keyword
normalized keyword
suggestion
```

---

# Multi-Fields

Un campo como `title` podrá disponer de:

```text
title.text
title.keyword
title.normalized
title.suggest
```

---

# Analyzer

Un **Analyzer** define cómo se transforma texto en términos indexables.

Formato recomendado:

```text
IDX-ANALYZER-XXXXXX
```

---

# Contrato

```yaml
lexical_analyzer:
  id: IDX-ANALYZER-SPANISH-0001

  version: 1.0.0
  language: es

  char_filters:
    - unicode_normalizer

  tokenizer:
    id: TOKENIZER-STANDARD

  token_filters:
    - lowercase
    - accent_normalization
    - spanish_stopwords
    - spanish_stemmer
```

---

# Componentes de analyzer

```text
char_filter
tokenizer
token_filter
normalizer
```

---

# Char Filter

Podrá:

- normalizar Unicode;
- limpiar caracteres;
- mapear variantes;
- preservar posiciones.

---

# Tokenizer

Divide texto en tokens.

---

# Token Filters

Podrán:

- convertir a minúsculas;
- normalizar acentos;
- aplicar stemming;
- eliminar stopwords;
- expandir sinónimos;
- producir n-grams.

---

# Analyzer por idioma

Deberá existir una estrategia por idioma soportado.

---

# Language Unknown

Podrá utilizarse un analyzer neutro.

No deberá aplicarse un stemmer incorrecto.

---

# Analyzer de nombres culinarios

Podrá conservar:

- guiones;
- unidades;
- términos compuestos;
- identificadores.

---

# Exact Analyzer

Para IDs y valores canónicos.

```text
REC-0009
```

no deberá dividirse de forma destructiva.

---

# Search Analyzer

El analyzer de consulta podrá diferir del analyzer de indexación.

---

# Compatibilidad

Ambos deberán ser compatibles.

---

# Stopwords

Deberán configurarse con cuidado.

Palabras aparentemente vacías pueden ser importantes en:

- negaciones;
- expresiones culinarias;
- nombres propios.

---

# Negación

No deberán eliminarse términos como:

```text
sin
no
nunca
```

cuando alteren significado.

---

# Stemming

Deberá evaluarse.

Puede aumentar recall, pero generar falsos positivos.

---

# Lemmatization

Podrá considerarse si existe soporte fiable.

---

# Synonym Set

Los sinónimos deberán estar gobernados.

Formato recomendado:

```text
IDX-SYNSET-XXXXXX
```

---

# Ejemplo

```yaml
synonym_set:
  id: IDX-SYNSET-COOKING-ES-0001

  version: 1.0.0

  mappings:
    - terms:
        - olla rápida
        - olla a presión

      relation: equivalent
```

---

# Tipos de equivalencia

```text
equivalent
broader
narrower
related
contextual
```

---

# No todos los términos relacionados son sinónimos

Ejemplo:

```text
miso
```

y:

```text
salsa de soja
```

no deberán declararse equivalentes.

---

# Synonym Direction

Podrá ser:

```text
bidirectional
unidirectional
```

---

# Cambios en synonyms

Podrán requerir:

- actualización en consulta;
- reindexado;
- nueva versión de analyzer;

según implementación.

---

# Edge N-Grams

Podrán utilizarse para:

- autocompletado;
- prefijos;
- búsqueda incremental.

---

# Riesgo

Pueden aumentar:

- tamaño;
- ruido;
- coste.

---

# Shingles

Podrán preservar frases.

Ejemplos:

```text
leche de coco
olla a presión
miso blanco
```

---

# Phrase Search

El índice deberá preservar posiciones cuando se requiera.

---

# Fuzzy Search

Podrá tolerar errores tipográficos.

Deberá limitarse para evitar matches excesivos.

---

# Accent Insensitivity

Podrá permitir:

```text
pure
```

y:

```text
puré
```

pero deberá evaluarse por idioma y contexto.

---

# Lexical Boosting

Los campos podrán tener pesos diferentes.

---

# Ejemplo conceptual

```yaml
boosting:
  title: 4.0
  aliases: 3.0
  entity_labels: 2.5
  body: 1.0
  contextual_text: 0.7
```

---

# Regla

El boosting deberá:

- versionarse;
- evaluarse;
- formar parte del fingerprint;
- no aplicarse arbitrariamente por consumidor.

---

# Static Boost

Basado en campo.

---

# Dynamic Boost

Basado en:

- estado;
- calidad;
- actualidad;
- tipo;
- colección.

---

# Riesgo

No deberá ocultar contenido relevante por exceso de popularidad o prioridad.

---

# Lexical Ranking

Podrá utilizar modelos como:

```text
BM25
TF-IDF
provider-specific lexical ranking
```

---

# Ranking Profile

Formato recomendado:

```text
RANK-PROFILE-XXXXXX
```

---

# Contrato

```yaml
ranking_profile:
  id: RANK-PROFILE-LEXICAL-RAG-0001

  version: 1.0.0

  algorithm: bm25

  parameters:
    k1: 1.2
    b: 0.75

  field_boosts:
    title: 4.0
    aliases: 3.0
    body: 1.0
```

---

# Cambios de ranking

Deberán evaluarse con consultas canónicas.

---

# Facets

El Lexical o Structured Index podrá soportar facetas.

---

# Campos facetables

Ejemplos:

```text
resource_type
collection
language
status
difficulty
cuisine
ingredient_category
technique
```

---

# Facet Cardinality

No deberán exponerse campos de cardinalidad excesiva sin necesidad.

---

# Facet Security

Los conteos deberán respetar:

- tenant;
- permisos;
- clasificación.

---

# Aggregation Leakage

Una faceta no deberá revelar existencia de recursos restringidos.

---

# Highlighting

Podrá producir snippets coincidentes.

---

# Requisitos

- preservar posiciones;
- escapar contenido;
- aplicar seguridad;
- no presentar texto contextual como original sin marcarlo.

---

# Lexical Entry Validation

Deberá comprobar:

- campos requeridos;
- analyzer;
- idioma;
- logical key;
- lineage;
- seguridad;
- ausencia de contenido vacío;
- mapping.

---

# Diagnósticos

```text
LEXICAL_ENTRY_SCHEMA_INVALID
LEXICAL_ENTRY_BODY_EMPTY
LEXICAL_ANALYZER_NOT_FOUND
LEXICAL_LANGUAGE_ANALYZER_MISMATCH
LEXICAL_SECURITY_METADATA_MISSING
LEXICAL_DUPLICATE_LOGICAL_KEY
LEXICAL_MAPPING_FAILED
LEXICAL_TERM_EXPANSION_EXCESSIVE
```

---

# Vector Index

El **Vector Index** almacena embeddings y permite búsqueda por proximidad.

---

# Casos de uso

- similitud semántica;
- búsqueda multilingüe;
- recuperación por intención;
- vecinos semánticos;
- matching de entidades;
- recuperación RAG.

---

# Vector Index ID

Formato recomendado:

```text
IDX-VEC-XXXXXX
```

---

# Vector Entry

```yaml
vector_entry:
  id: IDX-VEC-ENTRY-000041

  logical_key: REC-0009#PREPARATION#WINDOW-01

  embedding:
    id: EMB-000041

  vector_space:
    id: VSPACE-MULTILINGUAL-0001

  dimensions: 1024

  chunk_id: IDX-CHUNK-000041
  resource_id: REC-0009
  resource_type: recipe
  language: es

  tenant_id: TENANT-0001
  classification: internal

  metadata:
    section: preparation
    epistemic_layer: explicit
```

---

# Vector Index Schema

Deberá incluir:

- vector;
- Vector Space;
- logical key;
- chunk ID;
- resource ID;
- tenant;
- clasificación;
- filtros;
- snapshot;
- lineage.

---

# Vector Metric

Las métricas iniciales podrán incluir:

```text
cosine
dot_product
euclidean
```

---

# Cosine Similarity

Compara orientación.

Adecuada para vectores normalizados.

---

# Dot Product

Puede ser eficiente y compatible con modelos entrenados específicamente.

---

# Euclidean Distance

Mide distancia geométrica.

---

# Regla

La métrica deberá definirse en el Vector Space.

---

# No cambiar métrica sin evaluación

Puede alterar ranking.

---

# Exact Search

Compara contra todos los vectores.

Adecuado para:

- corpus pequeños;
- evaluación;
- referencia.

---

# Approximate Nearest Neighbor

Adecuado para corpus grandes.

---

# ANN

El **Approximate Nearest Neighbor** permite acelerar búsquedas sacrificando una parte controlada de exactitud.

---

# Estrategias posibles

```text
graph-based
inverted-file
tree-based
quantized
provider-specific
```

---

# HNSW conceptual

Una implementación graph-based podrá configurar:

```text
construction_quality
search_quality
maximum_connections
```

---

# No acoplamiento

El contrato no deberá depender de nombres concretos de parámetros del proveedor.

---

# ANN Profile

Formato recomendado:

```text
ANN-PROFILE-XXXXXX
```

---

# Contrato

```yaml
ann_profile:
  id: ANN-PROFILE-RAG-STANDARD

  version: 1.0.0

  strategy: graph_based

  build:
    quality: high
    memory_profile: balanced

  search:
    recall_target: 0.95
    latency_target_ms: 100
```

---

# ANN Evaluation

Deberá compararse con búsqueda exacta.

---

# Métricas

- recall@k;
- latency;
- memory;
- index build time;
- storage;
- throughput.

---

# No optimizar solo latencia

La pérdida de recall deberá permanecer dentro del Gate.

---

# Vector Filtering

La búsqueda vectorial deberá soportar prefiltrado por:

- tenant;
- clasificación;
- resource type;
- estado;
- colección;
- idioma;
- snapshot;
- temporalidad.

---

# Pre-filtering

Aplica filtros antes o durante la búsqueda vectorial.

---

# Post-filtering

Aplica filtros después.

---

# Recomendación

Utilizar pre-filtering para seguridad y filtros obligatorios.

---

# Riesgo del post-filtering

Puede:

- reducir el número útil de resultados;
- recuperar contenido no autorizado;
- afectar ranking;
- exponer contenido internamente.

---

# Partitioned Vector Index

Podrá dividirse por:

- tenant;
- clasificación;
- idioma;
- dominio;
- Vector Space;
- entorno.

---

# Partition Key

Deberá definirse formalmente.

---

# Ejemplo

```yaml
vector_partition:
  key:
    tenant: TENANT-0001
    vector_space: VSPACE-MULTILINGUAL-0001
    environment: production
```

---

# Partición por clasificación

Podrá separar:

```text
public
internal
restricted
```

---

# Beneficios

- seguridad;
- escalabilidad;
- retención;
- aislamiento.

---

# Riesgo de demasiadas particiones

Puede:

- reducir calidad;
- aumentar coste;
- complicar consultas.

---

# Vector Metadata

Deberá mantenerse mínima, pero suficiente para filtros y resolución.

---

# No duplicar el documento completo

El Vector Index no deberá convertirse en un almacén documental paralelo salvo justificación.

---

# Payload asociado

Podrá incluir:

- snippet breve;
- título;
- section path;
- citation pointer.

---

# Vector Quantization

Podrá reducir:

- memoria;
- almacenamiento;
- latencia.

---

# Tipos conceptuales

```text
scalar
product
binary
provider_default
```

---

# Evaluación obligatoria

La cuantización deberá compararse contra vectores originales.

---

# Re-ranking posterior

El Retrieval Engine podrá refinar candidatos.

No pertenece al Vector Builder, pero el índice deberá producir suficientes candidatos.

---

# Candidate Depth

El builder y el perfil deberán permitir configurar la profundidad de candidatos esperada.

---

# Vector Entry Validation

Deberá comprobar:

- dimensiones;
- Vector Space;
- valores;
- metadata;
- seguridad;
- mapping;
- partición;
- duplicados.

---

# Diagnósticos

```text
VECTOR_ENTRY_SCHEMA_INVALID
VECTOR_SPACE_UNKNOWN
VECTOR_DIMENSION_MISMATCH
VECTOR_METRIC_INCOMPATIBLE
VECTOR_PARTITION_MISSING
VECTOR_SECURITY_METADATA_MISSING
VECTOR_DUPLICATE_LOGICAL_KEY
VECTOR_PAYLOAD_TOO_LARGE
VECTOR_MAPPING_FAILED
```

---

# Structured Index

El **Structured Index** optimiza consultas basadas en atributos tipados.

---

# Casos de uso

- filtros;
- rangos;
- fechas;
- estados;
- cantidades;
- enums;
- identificadores;
- joins controlados;
- facetas.

---

# Structured Index ID

```text
IDX-STR-XXXXXX
```

---

# Structured Entry

```yaml
structured_entry:
  id: IDX-STR-ENTRY-000041

  resource_id: REC-0009
  resource_type: recipe

  fields:
    status: published
    difficulty: easy
    servings: 4
    preparation_time_minutes: 15
    cooking_time_minutes: 10
    language: es

  tenant_id: TENANT-0001
  classification: internal
```

---

# Tipos de campo

```text
string
keyword
integer
decimal
boolean
date
date_time
duration
quantity
enum
identifier
geo
nested
```

---

# Quantity Mapping

Una cantidad deberá conservar:

- valor;
- unidad;
- valor canónico;
- aproximación.

---

# Ejemplo

```yaml
quantity_field:
  original_value: 1
  original_unit: tablespoon
  canonical_value: 15
  canonical_unit: ml
  approximate: true
```

---

# Duration Mapping

Podrá conservar:

```text
ISO 8601 duration
```

y campos numéricos derivados para rango.

---

# Enum Mapping

Deberá utilizar valores canónicos.

---

# Nested Fields

Deberán controlarse para evitar complejidad excesiva.

---

# Structured Schema

Cada campo deberá declarar:

- nombre;
- tipo;
- nullable;
- filtrable;
- ordenable;
- facettable;
- sensible;
- fuente.

---

# Contrato

```yaml
structured_field:
  name: preparation_time_minutes
  type: integer
  filterable: true
  sortable: true
  facetable: false
  source: recipe.preparation_time
```

---

# Field Registry

Podrá existir un registro de campos estructurados.

---

# Dynamic Fields

Deberán evitarse en índices estables.

---

# Riesgo

Los campos dinámicos pueden:

- introducir mappings incorrectos;
- producir conflictos;
- aumentar cardinalidad;
- romper consultas.

---

# Range Queries

Deberán soportarse para:

- tiempos;
- cantidades;
- fechas;
- puntuaciones;
- temperaturas.

---

# Null Semantics

Deberá distinguirse:

```text
missing
null
unknown
not_applicable
```

cuando el dominio lo requiera.

---

# Sort Fields

Solo deberán permitirse campos autorizados.

---

# Structured Entry Validation

Deberá comprobar:

- tipos;
- rangos;
- unidades;
- enums;
- mappings;
- campos obligatorios;
- seguridad.

---

# Diagnósticos

```text
STRUCTURED_ENTRY_SCHEMA_INVALID
STRUCTURED_FIELD_TYPE_MISMATCH
STRUCTURED_FIELD_RANGE_INVALID
STRUCTURED_ENUM_UNKNOWN
STRUCTURED_UNIT_UNKNOWN
STRUCTURED_DYNAMIC_FIELD_NOT_ALLOWED
STRUCTURED_SECURITY_METADATA_MISSING
```

---

# Metadata Index

El **Metadata Index** optimiza consultas sobre procedencia, seguridad, calidad y organización.

---

# Casos de uso

- filtrar por colección;
- resolver snapshot;
- comprobar clasificación;
- buscar por owner;
- recuperar lineage;
- seleccionar calidad;
- aplicar temporalidad.

---

# Metadata Fields

```text
resource_id
resource_type
document_id
chunk_id
source_snapshot_id
index_snapshot_id
collection_ids
tenant_id
classification
visibility
owner
language
status
quality_status
epistemic_layer
created_at
updated_at
valid_from
valid_until
```

---

# Metadata Entry

```yaml
metadata_entry:
  id: IDX-META-ENTRY-000041

  logical_key: REC-0009#PREPARATION#WINDOW-01

  resource:
    id: REC-0009
    type: recipe

  source:
    document_id: DOC-0051
    chunk_id: IDX-CHUNK-000041
    source_snapshot_id: DOC-SNAP-20260801-0001

  organization:
    collections:
      - COL-RECIPES

  security:
    tenant_id: TENANT-0001
    classification: internal
    visibility: tenant

  quality:
    status: validated

  epistemic_layer: explicit
```

---

# Metadata Denormalization

Podrá duplicarse metadata crítica entre índices para:

- filtrado;
- seguridad;
- resolución.

---

# Regla

La duplicación deberá:

- estar gobernada;
- derivarse de fuente común;
- validar consistencia;
- actualizarse conjuntamente.

---

# Metadata Conflict

Si distintos índices contienen metadata incompatible, el snapshot deberá fallar o quedar degradado.

---

# Entity Index

El **Entity Index** optimiza recuperación y resolución de entidades.

---

# Casos de uso

- búsqueda de ingredientes;
- aliases;
- desambiguación;
- autocompletado;
- entity linking;
- navegación inicial.

---

# Entity Entry

```yaml
entity_entry:
  id: IDX-ENTITY-ENTRY-000041

  entity_id: ING-0008
  entity_type: ingredient

  preferred_label:
    language: es
    value: Miso

  aliases:
    - language: es
      value: pasta de miso

    - language: en
      value: miso paste

  description: Pasta fermentada de soja.

  ontology_classes:
    - fermented_ingredient

  collections:
    - COL-INGREDIENTS

  tenant_id: TENANT-0001
  classification: internal
```

---

# Entity Fields

- entity ID;
- type;
- preferred label;
- aliases;
- descriptions;
- ontology classes;
- external IDs;
- collections;
- status;
- language;
- popularity controlada;
- quality.

---

# Entity Resolution Keys

Podrán incluir:

- normalized labels;
- aliases;
- external IDs;
- ontology class;
- contextual terms.

---

# Ambiguous Entity

Deberá conservar candidatos.

---

# No fusión automática

Dos entidades similares no deberán fusionarse únicamente por score.

---

# Entity Suggestion Index

Podrá existir para autocompletado.

---

# Security

Las entidades restringidas no deberán aparecer en sugerencias no autorizadas.

---

# Entity Index Validation

Deberá detectar:

- IDs duplicados;
- labels ausentes;
- aliases conflictivos;
- external ID collisions;
- security gaps.

---

# Statement Index

El **Statement Index** optimiza recuperación de afirmaciones atómicas.

---

# Casos de uso

- preguntas factuales;
- grounding;
- razonamiento;
- GraphRAG;
- recuperación por sujeto, predicado u objeto.

---

# Statement Entry

```yaml
statement_entry:
  id: IDX-STMT-ENTRY-000041

  statement_id: STMT-000041

  subject:
    id: REC-0009
    type: recipe

  predicate: usesIngredient

  object:
    id: ING-0008
    type: ingredient

  qualifiers:
    optional: false

  negated: false

  epistemic_layer: validated

  textualizations:
    es: La receta Sopa de miso utiliza miso.

  provenance:
    document_id: DOC-0051
    block_id: BLOCK-00041

  tenant_id: TENANT-0001
  classification: internal
```

---

# Statement Search Fields

- subject;
- predicate;
- object;
- qualifiers;
- negation;
- temporalidad;
- epistemic layer;
- textualization;
- provenance.

---

# Predicate Normalization

Deberá utilizar términos canónicos.

---

# Object Types

El objeto podrá ser:

```text
resource
literal
quantity
date
enum
text
```

---

# Literal Object

Deberá conservar tipo y unidad.

---

# Negation

Deberá indexarse explícitamente.

---

# No flattening destructivo

Un Statement no deberá reducirse únicamente a texto.

---

# Statement Index Validation

Deberá comprobar:

- subject;
- predicate;
- object;
- qualifiers;
- negation;
- provenance;
- snapshot;
- epistemic layer.

---

# Diagnósticos

```text
STATEMENT_ENTRY_SCHEMA_INVALID
STATEMENT_SUBJECT_MISSING
STATEMENT_PREDICATE_UNKNOWN
STATEMENT_OBJECT_INVALID
STATEMENT_PROVENANCE_MISSING
STATEMENT_EPISTEMIC_LAYER_MISSING
STATEMENT_NEGATION_LOST
```

---

# Relation Index

El **Relation Index** optimiza consultas sobre relaciones directas.

---

# Relation Entry

```yaml
relation_entry:
  id: IDX-REL-ENTRY-000041

  relation_id: REL-000041

  source:
    id: REC-0009
    type: recipe

  relation_type: usesIngredient

  target:
    id: ING-0008
    type: ingredient

  direction: outgoing

  properties:
    optional: false

  snapshot_id: KG-SNAP-20260801-0004
```

---

# Diferencia con Statement

Una Relation puede representar la arista estructural.

Un Statement puede incluir:

- qualifiers;
- temporalidad;
- evidencia;
- epistemic layer.

---

# Uso

El diseño podrá materializar ambos cuando aporten valor.

---

# Citation Index

El **Citation Index** conecta resultados recuperados con fuentes verificables.

---

# Casos de uso

- generar citas;
- resolver bloques;
- localizar líneas;
- mostrar evidencia;
- verificar respuestas;
- auditoría.

---

# Citation Entry

```yaml
citation_entry:
  id: IDX-CITE-ENTRY-000041

  chunk_id: IDX-CHUNK-000041

  resource:
    id: REC-0009
    type: recipe

  document:
    id: DOC-0051

  source_snapshot:
    id: DOC-SNAP-20260801-0001

  spans:
    - block_id: BLOCK-00041
      line_start: 84
      line_end: 86
      source_hash: ...

  generated_context:
    present: true
    citable: false

  tenant_id: TENANT-0001
  classification: internal
```

---

# Citation Granularity

Podrá ser:

```text
document
section
block
line
character_span
statement
table_row
```

---

# Granularidad recomendada

Deberá ser lo bastante precisa para verificar el contenido sin fragmentar excesivamente.

---

# Citation Integrity

El contenido citado deberá corresponder al hash registrado.

---

# Snapshot-Specific Citation

Una cita deberá resolver dentro del snapshot utilizado.

---

# Documento actualizado

Una cita histórica no deberá apuntar silenciosamente a la versión actual.

---

# Citation Rendering

Podrá producir:

- título;
- sección;
- URL;
- rango;
- snippet.

---

# Seguridad

La cita no deberá revelar la ubicación de una fuente no autorizada.

---

# Citation Index Validation

Deberá comprobar:

- chunk mapping;
- documento;
- snapshot;
- span;
- hash;
- permisos;
- generated context.

---

# Diagnósticos

```text
CITATION_ENTRY_SCHEMA_INVALID
CITATION_CHUNK_NOT_FOUND
CITATION_SOURCE_NOT_FOUND
CITATION_SPAN_INVALID
CITATION_HASH_MISMATCH
CITATION_SNAPSHOT_MISMATCH
CITATION_SECURITY_METADATA_MISSING
CITATION_GENERATED_CONTEXT_MARKING_MISSING
```

---

# Graph Index

El **Graph Index** optimiza navegación y recuperación sobre estructuras de grafo.

---

# Casos de uso

- neighbors;
- paths;
- subgraphs;
- GraphRAG;
- comunidades;
- expansión de entidades;
- impacto;
- dependencias.

---

# No sustitución del Knowledge Graph

El Graph Index será una proyección derivada.

---

# Graph Components

```text
Node Index
Edge Index
Neighborhood Index
Path Index
Subgraph Index
Community Index
Graph Summary Index
```

---

# Node Entry

```yaml
graph_node_entry:
  id: IDX-GNODE-ENTRY-000041

  node_id: ING-0008
  node_type: ingredient

  labels:
    - Miso

  properties:
    category: fermented

  snapshot_id: KG-SNAP-20260801-0004

  tenant_id: TENANT-0001
  classification: internal
```

---

# Edge Entry

```yaml
graph_edge_entry:
  id: IDX-GEDGE-ENTRY-000041

  edge_id: REL-000041

  source_id: REC-0009
  relation_type: usesIngredient
  target_id: ING-0008

  directed: true

  snapshot_id: KG-SNAP-20260801-0004
```

---

# Graph Partitioning

Podrá realizarse por:

- tenant;
- dominio;
- colección;
- connected component;
- community;
- snapshot.

---

# Riesgo

Las particiones no deberán romper caminos necesarios sin estrategia de federación.

---

# Neighborhood Index

Materializa vecindarios frecuentes.

---

# Neighborhood Entry

```yaml
neighborhood_entry:
  id: IDX-NEIGH-ENTRY-000041

  root:
    id: ING-0008
    type: ingredient

  depth: 2

  nodes:
    count: 24

  edges:
    count: 41

  relation_types:
    - usedByRecipe
    - containsAllergen

  snapshot_id: KG-SNAP-20260801-0004
```

---

# Materialización selectiva

No deberán materializarse todos los vecindarios indiscriminadamente.

---

# Criterios

- frecuencia;
- coste;
- centralidad;
- casos de uso;
- tamaño.

---

# Path Index

El **Path Index** materializa caminos o patrones relevantes.

---

# Path Entry

```yaml
path_entry:
  id: IDX-PATH-ENTRY-000041

  path_type: allergen_trace

  source:
    id: REC-0009
    type: recipe

  target:
    id: ALG-SOY
    type: allergen

  nodes:
    - REC-0009
    - ING-0008
    - ALG-SOY

  relations:
    - usesIngredient
    - containsAllergen

  length: 2

  snapshot_id: KG-SNAP-20260801-0004
```

---

# Tipos de path

```text
dependency
composition
substitution
allergen_trace
technique_chain
provenance
ontology
custom
```

---

# Path Explosion

No deberán materializarse todos los caminos posibles.

---

# Límites

- longitud máxima;
- tipos permitidos;
- frecuencia;
- utilidad;
- coste.

---

# Path Canonicalization

Caminos equivalentes deberán representarse de forma estable.

---

# Cyclic Paths

Deberán manejarse explícitamente.

---

# Subgraph Index

El **Subgraph Index** materializa subgrafos útiles.

---

# Casos

- una receta y sus ingredientes;
- un ingrediente y alérgenos;
- una técnica y variantes;
- una colección temática;
- una comunidad.

---

# Subgraph Entry

```yaml
subgraph_entry:
  id: IDX-SUBGRAPH-ENTRY-000041

  root:
    id: REC-0009
    type: recipe

  scope:
    relation_types:
      - usesIngredient
      - requiresTechnique

    maximum_depth: 2

  nodes:
    count: 18

  edges:
    count: 27

  snapshot_id: KG-SNAP-20260801-0004
```

---

# Subgraph Serialization

Podrá almacenarse como:

- referencias;
- adjacency list;
- compressed structure;
- summary;
- provider-specific graph payload.

---

# Graph Summary Index

Contiene resúmenes derivados de grafos o comunidades.

---

# Summary Entry

```yaml
graph_summary_entry:
  id: IDX-GSUMMARY-ENTRY-000041

  scope:
    type: community
    id: COMMUNITY-0007

  summary:
    language: es
    text: Grupo de recetas japonesas que utilizan ingredientes fermentados.

  derived_from:
    nodes: 84
    edges: 163

  epistemic_layer: derived

  model:
    id: SUMMARY-MODEL-0001
    version: 1.0.0
```

---

# No hechos nuevos

El summary deberá conservar:

- fuentes;
- modelo;
- versión;
- validación.

---

# Community Index

Podrá materializar comunidades detectadas.

---

# Community Detection

Deberá registrar:

- algoritmo;
- versión;
- parámetros;
- snapshot.

---

# No comunidad canónica automática

Una comunidad es una agrupación derivada.

---

# Graph Index Validation

Deberá comprobar:

- nodos;
- aristas;
- direcciones;
- snapshots;
- permisos;
- paths;
- cycles;
- lineage.

---

# Diagnósticos

```text
GRAPH_NODE_MISSING
GRAPH_EDGE_ENDPOINT_MISSING
GRAPH_RELATION_TYPE_UNKNOWN
GRAPH_SNAPSHOT_MISMATCH
GRAPH_PATH_BROKEN
GRAPH_SUBGRAPH_TOO_LARGE
GRAPH_SECURITY_METADATA_MISSING
GRAPH_COMMUNITY_LINEAGE_MISSING
```

---

# Temporal Index

El **Temporal Index** podrá optimizar consultas históricas y de vigencia.

---

# Campos

```text
valid_from
valid_until
published_at
indexed_at
snapshot_id
revision
```

---

# Casos de uso

- estado en una fecha;
- versiones;
- recursos vigentes;
- citas históricas;
- rollback;
- análisis de cambios.

---

# Temporal Entry

```yaml
temporal_entry:
  id: IDX-TEMP-ENTRY-000041

  resource_id: REC-0009

  valid_from: 2026-07-01T00:00:00Z
  valid_until: null

  source_snapshot_id: DOC-SNAP-20260801-0001
  index_snapshot_id: IDX-SNAP-20260801-0001
```

---

# Bitemporalidad

Podrá distinguirse:

```text
valid time
transaction time
```

---

# Valid Time

Cuándo el hecho es válido en el dominio.

---

# Transaction Time

Cuándo fue registrado por el sistema.

---

# No necesidad inicial universal

Solo deberá implementarse cuando el caso de uso lo requiera.

---

# Hybrid Index

Un **Hybrid Index** combina señales lexicales, vectoriales, estructuradas o de grafo.

---

# Importante

No siempre será un índice físico separado.

Podrá ser:

- una suite;
- una vista;
- un contrato de Retrieval;
- una colección coordinada de componentes.

---

# Hybrid Index Suite

```yaml
hybrid_index_suite:
  id: IDX-SUITE-HYBRID-RAG-0001

  components:
    lexical: IDX-LEX-RAG-0001
    vector: IDX-VEC-RAG-0001
    structured: IDX-STR-RAG-0001
    metadata: IDX-META-RAG-0001
    citation: IDX-CITE-RAG-0001
```

---

# Hybrid Retrieval

El Retrieval Engine podrá combinar:

- lexical score;
- vector score;
- graph score;
- quality score;
- recency;
- authority.

---

# Builder Responsibility

Los builders deberán producir señales comparables y metadata suficiente.

---

# Score Normalization

No deberá pertenecer necesariamente al builder.

Sin embargo, cada índice deberá documentar:

- rango;
- dirección;
- interpretación;
- estabilidad.

---

# Lexical Score

No deberá compararse directamente con un cosine score sin normalización.

---

# Fusion Strategies futuras

```text
weighted_sum
reciprocal_rank_fusion
rank_based
learned_fusion
rule_based
```

---

# Index Suite Manifest

Un snapshot compuesto deberá conservar un manifest.

---

# Contrato

```yaml
index_suite_manifest:
  suite:
    id: IDX-SUITE-HYBRID-RAG-0001

  snapshot:
    id: IDX-SNAP-20260801-0001

  components:
    lexical:
      snapshot: IDX-LEX-SNAP-000041
      entries: 12450

    vector:
      snapshot: IDX-VEC-SNAP-000041
      entries: 12450

    structured:
      snapshot: IDX-STR-SNAP-000041
      entries: 3200

    citation:
      snapshot: IDX-CITE-SNAP-000041
      entries: 12450
```

---

# Consistencia entre índices

Todos los componentes deberán representar el mismo estado lógico.

---

# Consistency Dimensions

```text
resource coverage
snapshot compatibility
security metadata
tenant
logical keys
deletions
epistemic layer
citation mappings
```

---

# Cross-Index Mapping

Deberá permitir resolver:

```text
Lexical Entry
↔
Vector Entry
↔
Metadata Entry
↔
Citation Entry
```

mediante `logical_key` o un identificador común.

---

# Common Entry Key

Formato conceptual:

```text
INDEX-LOGICAL-KEY
```

---

# Missing Component

Una unidad podrá no aparecer en todos los índices si el perfil lo declara.

---

# Required Component

Si es obligatorio y falta, deberá generarse diagnóstico.

---

# Cross-Index Validation

Deberá comprobar:

- entries esperadas;
- orphan entries;
- duplicate keys;
- mismatched security;
- mismatched snapshots;
- missing citations;
- stale components.

---

# Diagnósticos

```text
INDEX_COMPONENT_ENTRY_MISSING
INDEX_COMPONENT_ORPHAN_ENTRY
INDEX_COMPONENT_SNAPSHOT_MISMATCH
INDEX_COMPONENT_SECURITY_MISMATCH
INDEX_COMPONENT_TENANT_MISMATCH
INDEX_COMPONENT_LOGICAL_KEY_MISMATCH
INDEX_COMPONENT_CITATION_MISSING
```

---

# Index Build Order

Algunos componentes podrán construirse en paralelo.

---

# Ejemplo

```text
Chunks
    ├── Lexical Builder
    ├── Vector Builder
    ├── Metadata Builder
    └── Citation Builder
```

---

# Dependencias de build

Ejemplos:

```text
Embedding Generation
↓
Vector Builder
```

```text
Entity Index
↓
Path Builder
```

---

# Build Dependency Graph

Deberá registrarse.

---

# Barrier de snapshot

La creación del Composite Snapshot deberá esperar a los componentes requeridos.

---

# Build Atomicity

Cada componente podrá construirse por separado.

La activación compuesta deberá ser atómica desde la perspectiva del consumidor.

---

# Candidate Component

Un componente podrá quedar `ready` sin activarse.

---

# Component Promotion

Podrá promoverse a candidate suite solo cuando todos los requeridos estén listos.

---

# Index Schema Registry

Todos los schemas deberán registrarse.

---

# Tipos

```text
lexical
vector
structured
metadata
entity
statement
relation
citation
graph
temporal
```

---

# Schema Record

```yaml
index_schema:
  id: IDX-SCHEMA-LEXICAL-RAG

  version: 1.0.0
  index_type: lexical
  status: active

  required_fields:
    - id
    - logical_key
    - body
    - resource_id
    - tenant_id
    - classification

  compatible_builders:
    - IDX-BUILDER-LEXICAL-RAG@1.0.0
```

---

# Schema Evolution

Los cambios deberán clasificarse.

---

# Compatible

- nuevo campo opcional;
- nueva metadata;
- nueva faceta opcional.

---

# Potencialmente incompatible

- nuevo analyzer;
- cambio de boosting;
- cambio de default;
- nuevo valor enum.

---

# Incompatible

- cambio de dimensión;
- cambio de tipo;
- campo requerido nuevo;
- eliminación;
- cambio de partition key;
- cambio de métrica.

---

# Index Migration

Un cambio incompatible requerirá:

- nuevo schema;
- nuevo índice físico o lógico;
- rebuild;
- validación;
- activación;
- rollback.

---

# Index Alias

Los consumidores deberán utilizar aliases lógicos.

---

# Ejemplos

```text
recipes-lexical-active
rag-vector-active
knowledge-graph-active
```

---

# Alias Metadata

```yaml
index_alias:
  id: rag-vector-active

  target:
    index: IDX-VEC-RAG-0001
    snapshot: IDX-VEC-SNAP-000041

  environment: production
```

---

# Alias Switch

Deberá ser:

- atómico;
- auditable;
- reversible.

---

# Multi-Alias Activation

Un Composite Snapshot podrá requerir cambiar varios aliases.

---

# Estrategia

Podrá utilizar:

- manifest versionado;
- routing layer;
- transactional metadata;
- indirection pointer.

---

# No cambios secuenciales visibles

El consumidor no deberá observar:

```text
lexical nuevo
+
vector antiguo
```

salvo modo degradado explícito.

---

# Index Validation

La validación deberá operar en varios niveles.

---

# Entry-Level Validation

Comprueba cada registro.

---

# Component-Level Validation

Comprueba un índice completo.

---

# Suite-Level Validation

Comprueba consistencia entre índices.

---

# Query-Level Validation

Ejecuta consultas canónicas.

---

# Security Validation

Comprueba aislamiento y filtros.

---

# Snapshot Validation

Comprueba coherencia de la versión final.

---

# Component Metrics

Cada builder deberá producir:

- entries;
- failures;
- storage;
- build time;
- duplicate ratio;
- orphan ratio;
- coverage;
- partitions;
- schema errors.

---

# Lexical Metrics

- term count;
- unique terms;
- average document length;
- analyzer failures;
- index size;
- search latency;
- lexical recall.

---

# Vector Metrics

- vectors;
- dimensions;
- ANN recall;
- build time;
- memory;
- cache ratio;
- search latency;
- invalid vectors.

---

# Structured Metrics

- entries;
- fields;
- null ratio;
- type errors;
- facet cardinality;
- range coverage.

---

# Graph Metrics

- nodes;
- edges;
- paths;
- communities;
- orphan nodes;
- broken edges;
- density;
- path count.

---

# Citation Metrics

- citation coverage;
- invalid spans;
- hash mismatches;
- orphan citations.

---

# Quality Gate de componente

```yaml
quality_gate:
  id: QG-INDEX-COMPONENT-0001

  criteria:
    all:
      - schema_errors == 0
      - orphan_entries == 0
      - missing_security_metadata == 0
      - duplicate_logical_keys == 0
      - required_coverage >= 0.99
```

---

# Quality Gate lexical

```yaml
quality_gate:
  id: QG-LEXICAL-INDEX-0001

  criteria:
    all:
      - lexical_entries_missing == 0
      - analyzer_failures == 0
      - lexical_recall_at_10 >= 0.85
      - forbidden_terms_indexed == 0
```

---

# Quality Gate vectorial

```yaml
quality_gate:
  id: QG-VECTOR-INDEX-0001

  criteria:
    all:
      - invalid_vectors == 0
      - dimension_mismatches == 0
      - ann_recall_at_10 >= 0.95
      - vector_security_failures == 0
      - vector_coverage >= 0.99
```

---

# Quality Gate de suite

```yaml
quality_gate:
  id: QG-INDEX-SUITE-0001

  criteria:
    all:
      - required_components_ready == true
      - cross_index_orphans == 0
      - snapshot_mismatches == 0
      - security_mismatches == 0
      - tenant_mismatches == 0
      - citation_coverage == 1.0
```

---

# Query Validation Set

Cada índice deberá probarse con consultas de referencia.

---

# Tipos

```text
exact
semantic
filter
facet
entity
statement
graph
citation
security
```

---

# Golden Queries

Deberán conservar:

- consulta;
- filtros;
- resultados esperados;
- tolerancias;
- perfil.

---

# Ejemplo

```yaml
golden_query:
  id: QUERY-GOLDEN-0001

  query: recetas con miso

  expected:
    must_include:
      - REC-0009

    must_not_include:
      - REC-0042
```

---

# Security Queries

Deberán comprobar:

- tenant isolation;
- clasificación;
- ACL;
- deleted resources;
- stale permissions.

---

# No usar únicamente métricas agregadas

Una buena media puede ocultar fallos críticos.

---

# Seguridad de los builders

Los builders deberán ejecutarse con identidades de servicio limitadas.

---

# Permisos mínimos

Ejemplos:

```text
index.read_source_artifacts
index.write_candidate
index.validate
```

---

# Activación separada

El builder no deberá poseer necesariamente permiso para activar.

---

# Separation of Duties

```text
Build
↓
Validate
↓
Approve
↓
Activate
```

podrán pertenecer a actores distintos.

---

# Tenant Isolation

Podrá implementarse mediante:

- índice separado;
- partición;
- campo obligatorio;
- namespace;
- instancia.

---

# Estrategia

Deberá documentarse por índice.

---

# Security Filter Field

Los campos de seguridad no deberán ser opcionales.

---

# ACL Encoding

Podrá utilizar:

- principals;
- roles;
- policy IDs;
- visibility groups;
- classification.

---

# Riesgo de ACL grande

No deberán insertarse listas ilimitadas de usuarios si existe un modelo de grupo o policy más estable.

---

# Policy Reference

Ejemplo:

```yaml
security:
  policy_id: POLICY-DOC-READ-0001
```

---

# Field-Level Security

Algunos índices podrán separar campos sensibles.

---

# Redacted Index Entry

Podrá contener una proyección reducida.

---

# Example

```yaml
content_projection:
  type: redacted
  policy: REDACTION-POLICY-0001
```

---

# No Security by Obscurity

Ocultar IDs no sustituye filtros.

---

# Encryption

Los índices deberán cifrarse en:

- disco;
- backups;
- tránsito;
- réplicas.

---

# Provider Access

Deberá restringirse mediante:

- service identity;
- network policy;
- credentials;
- audit.

---

# Index Export

Deberá considerarse una operación sensible.

---

# No dump indiscriminado

Una exportación deberá:

- autorizarse;
- cifrarse;
- expirar;
- auditarse;
- conservar clasificación.

---

# Observabilidad de builders

---

# Métricas comunes

- build executions;
- success rate;
- entries per second;
- build duration;
- storage;
- failures;
- retries;
- validation failures.

---

# Métricas por builder

Deberán etiquetarse por:

- builder ID;
- versión;
- index type;
- environment;
- profile.

---

# No labels de alta cardinalidad

No deberán utilizarse:

- resource ID;
- chunk ID;
- user ID;

como labels generales.

---

# Logs

```yaml
log:
  event: index_builder_completed

  builder: IDX-BUILDER-VECTOR-RAG@1.0.0
  execution: IDX-BUILD-EXEC-000041
  index: IDX-VECTOR-RAG-0001
  entries: 12450
  duration_ms: 84000
```

---

# Trazas

```text
Builder Execution
↓
Mapping
↓
Partition Resolution
↓
Write
↓
Flush
↓
Validation
↓
Manifest
```

---

# Slow Build Detection

Deberán existir alertas para:

- throughput bajo;
- partición saturada;
- flush lento;
- retries;
- storage growth.

---

# Index Health

Estados posibles:

```text
healthy
degraded
stale
unavailable
rebuilding
```

---

# No confundir salud con calidad

Un índice puede estar disponible y tener baja calidad de retrieval.

---

# Costes

Deberán medirse:

- almacenamiento;
- memoria;
- CPU;
- embeddings;
- build time;
- consultas;
- réplicas.

---

# Cost per Entry

Podrá utilizarse para optimización.

---

# No optimización que rompa calidad

Cualquier reducción deberá pasar evaluación.

---

# Eventos de builders

Catálogo inicial:

```text
index_builder_started
index_builder_completed
index_builder_failed
index_component_ready
index_component_validation_failed
index_suite_ready
index_schema_registered
index_mapping_updated
index_alias_switched
```

---

# Evento de componente listo

```yaml
event:
  type: index_component_ready

  subject:
    id: IDX-VEC-SNAP-000041
    type: vector-index-snapshot

  data:
    builder: IDX-BUILDER-VECTOR-RAG@1.0.0
    entries: 12450
    vector_space: VSPACE-MULTILINGUAL-0001
```

---

# Resiliencia de builders

---

# Retry

Será adecuado para:

- timeouts;
- errores transitorios;
- rate limit;
- fallo de red.

---

# No retry

Para:

- schema inválido;
- mapping incompatible;
- dimensión incorrecta;
- partición desconocida.

---

# Partial Build

Podrá conservarse para diagnóstico.

No deberá promocionarse bajo perfil estricto.

---

# Resume

Podrá reanudarse mediante checkpoints o lotes completados.

---

# Write Idempotency

Cada entrada deberá poder escribirse mediante:

```text
upsert by logical key
```

o mecanismo equivalente.

---

# Duplicate Physical Writes

No deberán generar duplicados lógicos.

---

# Delete Support

El builder deberá soportar:

- delete;
- tombstone;
- invalidation;
- replacement.

---

# Bulk Write

Podrá optimizarse por lotes.

---

# Backpressure

La fase de escritura deberá limitar productores.

---

# Failure Isolation

Un registro defectuoso podrá aislarse cuando no comprometa la coherencia global.

---

# Poison Entry

Deberá producir:

- diagnóstico;
- quarantine;
- lineage;
- bloqueo si es obligatorio.

---

# Implementación inicial recomendada

La primera implementación práctica podrá incluir:

```text
Lexical Index
+
Structured Metadata
+
Citation Index
```

---

# Segunda iteración

Añadirá:

```text
Vector Index
+
Hybrid Suite
```

---

# Tercera iteración

Añadirá:

```text
Entity Index
+
Statement Index
+
Graph Index
```

---

# Primera suite recomendada

```yaml
index_suite:
  id: IDX-SUITE-RAG-MVP

  required:
    - lexical
    - vector
    - metadata
    - citation

  optional:
    - structured
```

---

# Primera suite GraphRAG

```yaml
index_suite:
  id: IDX-SUITE-GRAPHRAG-MVP

  required:
    - entity
    - statement
    - relation
    - graph
    - metadata
    - citation

  optional:
    - vector
    - graph_summary
```

---

# No será necesario inicialmente

- learned sparse index;
- neural re-ranking dentro del índice;
- múltiples ANN simultáneos;
- path materialization exhaustiva;
- graph federation;
- distributed graph partitioning;
- multimodal index;
- geo index;
- online schema migration;
- automatic index tuning.

---

# Casos de uso

---

# Caso de uso 1 — Búsqueda exacta

Consulta:

```text
sopa de miso
```

El Lexical Index recupera la receta mediante:

- título;
- aliases;
- body.

---

# Caso de uso 2 — Búsqueda semántica

Consulta:

```text
plato japonés con pasta fermentada
```

El Vector Index recupera una receta con miso aunque no comparta exactamente los mismos términos.

---

# Caso de uso 3 — Filtro estructurado

Consulta:

```text
recetas de menos de 30 minutos
```

El Structured Index filtra por duración.

---

# Caso de uso 4 — Recuperación híbrida

La consulta combina:

- lexical match;
- vector candidates;
- filtros;
- Citation Index.

---

# Caso de uso 5 — Entity Resolution

La búsqueda:

```text
pasta de miso
```

resuelve la entidad:

```text
ING-0008
```

mediante aliases.

---

# Caso de uso 6 — Statement factual

La consulta:

```text
¿Qué alérgeno contiene el miso?
```

recupera Statements y caminos relacionados con soja.

---

# Caso de uso 7 — Citation Resolution

Un chunk recuperado se resuelve hacia:

- documento;
- bloque;
- líneas;
- snapshot.

---

# Caso de uso 8 — GraphRAG

A partir de una receta se recupera un subgrafo con:

- ingredientes;
- técnicas;
- alérgenos;
- relaciones.

---

# Caso de uso 9 — Cambio de dimensión

Un nuevo modelo vectorial obliga a:

- nuevo Vector Space;
- nuevo schema;
- nuevo índice;
- build completo.

---

# Caso de uso 10 — Inconsistencia entre componentes

Existe un Vector Entry sin Citation Entry obligatoria.

El Suite Gate falla.

---

# Caso de uso 11 — Tenant isolation

La consulta de `TENANT-0001` no puede recuperar entradas de `TENANT-0002`, aunque sean semánticamente similares.

---

# Caso de uso 12 — Rollback de suite

Tras una regresión en lexical ranking, se reactiva el Composite Snapshot anterior.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Un único índice para todo

Mezcla necesidades, schemas y riesgos distintos.

---

## Diseñar schemas según el proveedor

Acopla la arquitectura.

---

## Campos dinámicos sin control

Generan drift.

---

## Indexar todo como texto

Pierde tipos y filtros.

---

## Indexar todo como vector

Pierde exactitud y explicabilidad.

---

## Utilizar vector search para IDs

Los identificadores requieren búsqueda exacta.

---

## Utilizar lexical search para toda semántica

Reduce recall conceptual.

---

## Mezclar espacios vectoriales

Hace inválidas las distancias.

---

## Cambiar analyzer sin reindexar

Produce términos incompatibles.

---

## Stemming agresivo sin evaluación

Genera falsos positivos.

---

## Eliminar negaciones como stopwords

Altera significado.

---

## Sinónimos no gobernados

Pueden introducir equivalencias falsas.

---

## Boosts arbitrarios

Sesgan resultados.

---

## Facetas sin seguridad

Filtran existencia de recursos restringidos.

---

## Vector metadata insuficiente

Impide filtros y resolución.

---

## Post-filtering para seguridad

Puede exponer contenido.

---

## Particionar por cada pequeño atributo

Aumenta fragmentación.

---

## Dynamic fields en Structured Index

Rompen mappings.

---

## Statements convertidos solo a texto

Pierden semántica estructurada.

---

## Citations sin snapshot

Apuntan a versiones incorrectas.

---

## Citar contexto generado como fuente

Produce atribución falsa.

---

## Materializar todos los paths

Provoca explosión combinatoria.

---

## Confundir Graph Index con Knowledge Graph

El índice es derivado.

---

## Construir componentes sobre snapshots distintos

Rompe consistencia.

---

## Activar aliases uno por uno

Puede exponer una suite mixta.

---

## No validar logical keys entre índices

Genera huérfanos.

---

## Permitir que builders activen producción

Rompe separación de funciones.

---

## Exportar índices sin autorización

Expone datos derivados.

---

## No medir ANN recall

Puede ocultar pérdida de candidatos.

---

## Optimizar únicamente tamaño

Puede degradar retrieval.

---

## Utilizar score lexical y vectorial directamente juntos

Las escalas no son equivalentes.

---

## Considerar disponibilidad igual a calidad

Un índice puede responder correctamente y recuperar mal.

---

# Reglas mínimas de conformidad

---

## Builder identificado

Todo builder deberá tener ID y versión.

---

## Mapping explícito

Toda transformación deberá estar documentada.

---

## Schema versionado

Todo componente deberá declarar schema.

---

## Logical Key común

Las entradas relacionadas deberán poder resolverse entre índices.

---

## Lineage preservado

Toda entrada deberá enlazar con su origen.

---

## Seguridad obligatoria

Toda entrada deberá conservar tenant y clasificación.

---

## Lexical Analyzer versionado

Todo analyzer deberá estar registrado.

---

## Vector Space identificado

Todo vector deberá pertenecer a un espacio compatible.

---

## Structured Fields tipados

Los campos estructurados deberán declarar tipo.

---

## Citation Mapping completo

Todo chunk recuperable deberá disponer de cita cuando el perfil lo exija.

---

## Graph Snapshot preservado

Los elementos de grafo deberán pertenecer a un snapshot concreto.

---

## Cross-Index Validation

La suite deberá comprobar consistencia.

---

## Quality Gates

Cada componente y suite deberán superar Gate.

---

## Activation separada

Construcción y activación deberán ser operaciones distintas.

---

## Alias atómico

La activación deberá evitar suites mixtas.

---

## Rollback

Deberá conservarse un snapshot anterior cuando proceda.

---

# Conformidad de Index Builder

Será conforme cuando:

- tenga identidad;
- declare versión;
- declare input schemas;
- declare output schema;
- declare capacidades;
- produzca manifest;
- preserve lineage;
- emita métricas.

---

# Conformidad de Lexical Index

Será conforme cuando:

- declare analyzer;
- preserve idioma;
- preserve negaciones;
- declare campos;
- declare boosts;
- soporte seguridad;
- valide términos y mappings.

---

# Conformidad de Vector Index

Será conforme cuando:

- declare Vector Space;
- declare dimensión;
- declare métrica;
- preserve mapping;
- soporte filtros seguros;
- valide ANN recall;
- preserve tenant isolation.

---

# Conformidad de Structured Index

Será conforme cuando:

- tipifique campos;
- valide rangos;
- preserve unidades;
- limite dynamic fields;
- declare campos filtrables y ordenables.

---

# Conformidad de Metadata Index

Será conforme cuando:

- preserve snapshots;
- preserve tenant;
- preserve clasificación;
- preserve quality;
- preserve epistemic layer;
- mantenga consistencia.

---

# Conformidad de Entity Index

Será conforme cuando:

- identifique entidad;
- preserve preferred label;
- preserve aliases;
- preserve ontology classes;
- detecte ambigüedades;
- aplique seguridad.

---

# Conformidad de Statement Index

Será conforme cuando:

- preserve subject;
- preserve predicate;
- preserve object;
- preserve qualifiers;
- preserve negation;
- preserve provenance;
- preserve epistemic layer.

---

# Conformidad de Citation Index

Será conforme cuando:

- identifique chunk;
- identifique documento;
- identifique snapshot;
- preserve spans;
- preserve hashes;
- diferencie contexto generado.

---

# Conformidad de Graph Index

Será conforme cuando:

- preserve nodos;
- preserve aristas;
- preserve dirección;
- preserve snapshot;
- preserve seguridad;
- limite paths y subgrafos;
- mantenga lineage.

---

# Conformidad de Index Suite

Será conforme cuando:

- declare componentes;
- declare requeridos y opcionales;
- preserve snapshot común;
- preserve logical keys;
- preserve seguridad;
- supere validación cruzada;
- permita activación atómica.

---

# Lista de comprobación

Antes de aprobar los builders y componentes deberá comprobarse:

```text
[ ] Cada builder tiene ID y versión.
[ ] Los input schemas están definidos.
[ ] Los output schemas están versionados.
[ ] Los mappings están registrados.
[ ] Los campos comunes están presentes.
[ ] Los logical keys son estables.
[ ] Los fingerprints están calculados.
[ ] El lineage está completo.
[ ] Tenant y clasificación están presentes.
[ ] El Lexical Analyzer está versionado.
[ ] La configuración de stopwords está revisada.
[ ] Las negaciones se preservan.
[ ] Los sinónimos están gobernados.
[ ] Los boosts están versionados.
[ ] Las facetas respetan seguridad.
[ ] El Vector Space está identificado.
[ ] La dimensión coincide.
[ ] La métrica es compatible.
[ ] El ANN Profile está evaluado.
[ ] Los filtros vectoriales son seguros.
[ ] Las particiones están definidas.
[ ] Los campos estructurados están tipados.
[ ] Las unidades y rangos están normalizados.
[ ] El Metadata Index es consistente.
[ ] El Entity Index preserva aliases.
[ ] El Statement Index preserva qualifiers y negación.
[ ] El Citation Index preserva snapshot y spans.
[ ] El Graph Index preserva nodos, aristas y dirección.
[ ] Los paths están limitados.
[ ] Los summaries derivados conservan lineage.
[ ] Los componentes requeridos están completos.
[ ] No existen orphan entries.
[ ] No existen security mismatches.
[ ] No existen tenant mismatches.
[ ] La validación de consultas canónicas ha finalizado.
[ ] Los Quality Gates de componentes han pasado.
[ ] El Quality Gate de suite ha pasado.
[ ] La activación será atómica.
[ ] El rollback está disponible.
[ ] Los manifests están generados.
[ ] Las métricas y eventos están disponibles.
```

---

# Arquitectura final de la Parte IV

```text
Validated Chunks and Embeddings
        ↓
Builder Resolution
        ↓
Schema and Mapping Resolution
        ↓
Parallel Component Builds
        ├── Lexical Index
        ├── Vector Index
        ├── Structured Index
        ├── Metadata Index
        ├── Entity Index
        ├── Statement Index
        ├── Citation Index
        └── Graph Index
        ↓
Component Validation
        ↓
Cross-Index Validation
        ↓
Index Suite Manifest
        ↓
Candidate Composite Snapshot
```

---

# Transición hacia la Parte V

Esta cuarta parte ha definido:

- el concepto de Index Builder;
- las Builder Executions;
- los Build Manifests;
- los Index Mappings;
- el modelo común de entrada;
- el Lexical Index;
- analyzers;
- tokenización;
- stemming;
- synonyms;
- boosting;
- ranking;
- facetas;
- highlighting;
- el Vector Index;
- Vector Spaces;
- métricas;
- ANN;
- particiones;
- filtros;
- cuantización;
- el Structured Index;
- tipos de campo;
- rangos;
- cantidades;
- el Metadata Index;
- el Entity Index;
- el Statement Index;
- el Relation Index;
- el Citation Index;
- el Graph Index;
- Node Index;
- Edge Index;
- Neighborhood Index;
- Path Index;
- Subgraph Index;
- Graph Summary Index;
- Temporal Index;
- Hybrid Index Suites;
- consistencia cruzada;
- schemas;
- aliases;
- activación;
- validación;
- Quality Gates;
- seguridad;
- observabilidad;
- resiliencia;
- casos de uso;
- antipatrones;
- reglas de conformidad.

La Parte V desarrollará:

- incremental indexing;
- Change Sets;
- detección de cambios;
- invalidación;
- dependencias;
- propagación de impacto;
- upserts;
- deletes;
- tombstones;
- reindexado selectivo;
- full rebuild;
- index migrations;
- dual write;
- backfill;
- shadow indexing;
- snapshots;
- activación blue-green;
- rollback;
- compactación;
- retención;
- garbage collection;
- reconciliación;
- drift detection;
- recuperación tras fallos;
- contratos operativos.

---

# Conclusión

Los builders transforman chunks, embeddings, metadata y estructuras de conocimiento en componentes especializados para recuperación.

El ciclo puede resumirse así:

```text
Recibir artefactos validados
        ↓
Resolver builder
        ↓
Aplicar mapping
        ↓
Construir componente
        ↓
Validar entradas
        ↓
Validar índice
        ↓
Relacionar componentes
        ↓
Construir suite
        ↓
Crear snapshot candidato
```

El Lexical Index aporta coincidencia textual.

El Vector Index aporta proximidad semántica.

El Structured Index permite filtros y rangos.

El Metadata Index preserva organización, seguridad y procedencia.

El Entity Index resuelve conceptos.

El Statement Index recupera afirmaciones atómicas.

El Citation Index permite verificar evidencia.

El Graph Index permite navegar relaciones, paths y subgrafos.

La suite híbrida coordina esas perspectivas sin confundirlas.

Un componente correcto deberá poder responder:

```text
¿Qué tipo de recuperación soporta?

¿Qué schema utiliza?

¿Qué builder lo creó?

¿Qué mapping aplicó?

¿Qué entradas contiene?

¿Qué snapshot representa?

¿Qué seguridad preserva?

¿Qué métricas produjo?

¿Qué Quality Gate superó?
```

Una Index Suite correcta deberá poder responder:

```text
¿Qué componentes incluye?

¿Qué componentes son obligatorios?

¿Representan el mismo estado lógico?

¿Cómo se relacionan sus entradas?

¿Comparten tenant y clasificación?

¿Existe cobertura completa?

¿Puede activarse atómicamente?

¿A qué snapshot anterior puede revertirse?
```

Con esta cuarta parte quedan formalizadas las estructuras concretas de búsqueda y recuperación de NovaCoquinaria.

La siguiente parte definirá cómo estos índices se mantienen actualizados mediante incremental indexing, invalidación, reconstrucción, migración, activación y rollback.

---

# Parte V — Indexación incremental, invalidación, reconstrucción, migraciones, snapshots y ciclo de vida operativo

---

# Introducción

La Parte IV ha definido cómo NovaCoquinaria construye los diferentes componentes de índice:

- Lexical Index;
- Vector Index;
- Structured Index;
- Metadata Index;
- Entity Index;
- Statement Index;
- Relation Index;
- Citation Index;
- Graph Index;
- Hybrid Index Suites.

Sin embargo, la creación inicial de estos índices representa únicamente el comienzo de su ciclo de vida.

El conocimiento canónico evoluciona continuamente.

Pueden producirse:

- nuevos documentos;
- modificaciones;
- eliminaciones;
- cambios de relaciones;
- cambios de ontología;
- cambios de seguridad;
- nuevas inferencias;
- correcciones de errores;
- cambios en el chunking;
- cambios de embeddings;
- cambios de schema;
- cambios de mappings;
- cambios de configuración.

El Indexing Engine deberá mantener sincronizadas sus representaciones derivadas sin:

- reconstruir siempre todo el corpus;
- perder coherencia;
- servir datos eliminados;
- mezclar versiones;
- duplicar entradas;
- interrumpir consultas;
- comprometer seguridad.

Esta responsabilidad corresponderá al conjunto de capacidades operativas formado por:

```text
Incremental Indexing
Invalidation
Selective Reindexing
Full Rebuild
Migration
Snapshot Management
Activation
Rollback
Reconciliation
Retention
Garbage Collection
```

Conceptualmente:

```text
Canonical Change
        ↓
Change Detection
        ↓
Impact Analysis
        ↓
Invalidation Plan
        ↓
Incremental Build
        ↓
Candidate Snapshot
        ↓
Validation
        ↓
Atomic Activation
        ↓
Monitoring
        ↓
Retention or Rollback
```

El sistema deberá asumir que los índices pueden quedar temporalmente retrasados respecto al conocimiento canónico.

No obstante, ese retraso deberá ser:

- conocido;
- medido;
- limitado;
- gobernado;
- seguro.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir la indexación incremental;
- formalizar los Change Sets;
- establecer la detección de cambios;
- distinguir cambios directos e indirectos;
- definir la propagación de impacto;
- formalizar invalidaciones;
- definir tombstones;
- establecer upserts;
- regular eliminaciones;
- definir reindexado selectivo;
- formalizar full rebuild;
- establecer backfills;
- definir migraciones de índices;
- regular dual write;
- formalizar shadow indexing;
- definir blue-green indexing;
- establecer snapshots operativos;
- formalizar activación;
- definir rollback;
- regular compactación;
- establecer retención;
- definir Garbage Collection;
- formalizar reconciliación;
- detectar drift;
- definir recuperación tras fallos;
- establecer consistencia;
- regular concurrencia;
- definir APIs y eventos operativos;
- establecer Quality Gates;
- formalizar observabilidad;
- definir reglas de conformidad.

---

# Principios operativos

Toda operación de mantenimiento de índices deberá respetar los siguientes principios.

---

## Cambio explícito

Todo cambio deberá representarse mediante un recurso o evento identificable.

---

## Impacto calculado

No deberá asumirse que únicamente cambia el recurso directamente modificado.

---

## Seguridad prioritaria

Los cambios de:

- clasificación;
- tenant;
- ACL;
- visibilidad;
- eliminación;

deberán propagarse con prioridad.

---

## Incremental cuando sea seguro

La indexación incremental deberá preferirse cuando pueda garantizarse coherencia.

---

## Full rebuild cuando sea necesario

No deberá forzarse la incrementalidad si:

- cambia el schema;
- cambia el modelo;
- cambia el chunking;
- cambia la ontología de forma incompatible;
- no puede calcularse el impacto.

---

## Idempotencia

Reaplicar el mismo Change Set no deberá duplicar efectos lógicos.

---

## Inmutabilidad de snapshots

Los cambios deberán producir un nuevo snapshot lógico.

---

## Activación atómica

Los consumidores deberán observar una versión coherente.

---

## No resurrección

Los recursos eliminados no deberán reaparecer por:

- replay;
- caché;
- backfill;
- reconstrucción incompleta;
- eventos fuera de orden.

---

## Lineage preservado

Toda entrada nueva, modificada o eliminada deberá conservar trazabilidad.

---

## Rollback preparado

Las activaciones críticas deberán preservar una versión recuperable.

---

## Reconciliación periódica

La confianza no deberá depender únicamente de eventos incrementales.

---

## Drift detectable

La divergencia entre conocimiento e índice deberá medirse.

---

## Retención gobernada

Los snapshots y artefactos no deberán conservarse indefinidamente sin política.

---

## Eliminación segura

La eliminación deberá propagarse a:

- índices;
- cachés;
- réplicas;
- previews;
- snapshots expirables;
- artefactos derivados.

---

## Separación entre dato lógico y estructura física

Una operación lógica podrá modificar varios componentes físicos.

---

## Observabilidad de estado

Todo índice deberá declarar:

- frescura;
- cobertura;
- lag;
- snapshot activo;
- ejecución en curso.

---

# Arquitectura operativa

```text
┌───────────────────────────────────────────────┐
│              Canonical Changes                │
│                                               │
│ Documents · KG · Ontology · Security          │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Change Detection                 │
│                                               │
│ Events · Hashes · Revisions · Reconciliation  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Impact Analysis                 │
│                                               │
│ Dependencies · Lineage · Security · Graph     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Invalidation Planning             │
│                                               │
│ Reuse · Rebuild · Delete · Tombstone          │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Incremental Build                │
│                                               │
│ Upsert · Delete · Backfill · Repair            │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Candidate Snapshot                │
│                                               │
│ Validate · Reconcile · Compare · Gate         │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│        Activation and Lifecycle Control       │
│                                               │
│ Blue-Green · Rollback · Retention · GC        │
└───────────────────────────────────────────────┘
```

---

# Change Set

Un **Index Change Set** representa el conjunto gobernado de cambios que deberán reflejarse en los índices.

Formato recomendado:

```text
IDX-CHANGESET-XXXXXX
```

---

# Contrato

```yaml
index_change_set:
  id: IDX-CHANGESET-000041

  source:
    type: canonical_change_set
    id: CHANGESET-000041

  baseline:
    source_snapshot: DOC-SNAP-20260725-0003
    index_snapshot: IDX-SNAP-20260725-0003

  target:
    source_snapshot: DOC-SNAP-20260801-0001

  changes:
    created:
      - REC-0043

    updated:
      - REC-0009

    deleted:
      - REC-0017

    security_changed:
      - DOC-0051

  status: analyzed
```

---

# Estados

```text
created
analyzing
analyzed
planned
processing
applied
applied_with_warnings
partial
failed
cancelled
superseded
```

---

# Fuentes de Change Set

Podrán incluir:

```text
document change set
knowledge graph delta
ontology change
security change
manual selection
event range
snapshot diff
reconciliation result
```

---

# Change Item

Cada cambio deberá representarse individualmente.

---

# Contrato

```yaml
change_item:
  id: IDX-CHANGE-000041

  resource:
    id: REC-0009
    type: recipe

  change_type: updated

  changed_fields:
    - preparation
    - ingredients

  previous_revision: 16
  current_revision: 17

  fingerprints:
    previous: ...
    current: ...
```

---

# Tipos de cambio

```text
created
updated
deleted
renamed
moved
merged
split
restored
security_changed
classification_changed
tenant_changed
schema_changed
ontology_changed
dependency_changed
epistemic_layer_changed
```

---

# Created

Requiere nuevas unidades y entradas.

---

# Updated

Puede requerir:

- reutilización;
- regeneración parcial;
- rebuild completo del recurso.

---

# Deleted

Requiere invalidación y tombstone.

---

# Renamed

Puede afectar:

- Lexical Index;
- Entity Index;
- aliases;
- embeddings contextualizados;
- citations.

---

# Moved

Puede afectar:

- section paths;
- contexto;
- canonical pointers;
- logical keys si están mal diseñadas.

---

# Merged

Dos recursos se consolidan.

Deberá preservar:

- redirecciones;
- lineage;
- IDs históricos;
- referencias.

---

# Split

Un recurso se divide.

Deberá preservar mappings entre:

- recurso anterior;
- recursos resultantes;
- entradas históricas.

---

# Restored

Un recurso eliminado vuelve a estar disponible.

Deberá respetar:

- revisión;
- seguridad actual;
- tombstone previo;
- reconstrucción completa.

---

# Security Changed

Deberá tener prioridad sobre cambios de contenido normales.

---

# Schema Changed

Podrá requerir migración o full rebuild.

---

# Ontology Changed

Puede afectar:

- clasificaciones;
- Entity Index;
- Statement Index;
- Graph Index;
- embeddings contextualizados;
- summaries.

---

# Change Detection

La detección de cambios podrá utilizar varias fuentes.

---

# Estrategias

```text
revision comparison
content hash
structure hash
semantic hash
security hash
manifest diff
event stream
snapshot diff
dependency fingerprint
reconciliation scan
```

---

# Revision Comparison

Adecuada cuando cada recurso dispone de revisión fiable.

---

# Content Hash

Detecta modificaciones del contenido indexable.

---

# Structure Hash

Detecta cambios de:

- orden;
- headings;
- relaciones;
- jerarquía.

---

# Semantic Hash

Puede ignorar cambios no significativos para retrieval.

---

# Security Hash

Detecta cambios que afectan acceso.

---

# Manifest Diff

Compara conjuntos completos de recursos.

---

# Event Stream

Permite reaccionar a cambios en tiempo casi real.

---

# Snapshot Diff

Compara estados completos.

---

# Reconciliation Scan

Detecta divergencias no reflejadas en eventos.

---

# Detección combinada

Se recomienda utilizar:

```text
Events
+
Hashes
+
Periodic Reconciliation
```

---

# Evento como señal, no como única verdad

Un evento puede:

- perderse;
- duplicarse;
- llegar tarde;
- estar fuera de orden.

El estado canónico deberá seguir siendo verificable.

---

# Change Detection Result

```yaml
change_detection:
  baseline_snapshot: DOC-SNAP-20260725-0003
  target_snapshot: DOC-SNAP-20260801-0001

  detected:
    created: 12
    updated: 7
    deleted: 2
    unchanged: 845

  method:
    - event_stream
    - manifest_diff
    - content_hash
```

---

# Cambio editorial

Un cambio podrá clasificarse como no indexable cuando:

- no cambia texto normalizado;
- no cambia estructura;
- no cambia contexto;
- no cambia seguridad;
- no cambia procedencia relevante.

---

# No confiar únicamente en timestamp

Las fechas pueden cambiar sin modificación semántica o permanecer iguales tras una copia defectuosa.

---

# Impact Analysis

El análisis de impacto determina qué artefactos derivados quedan afectados.

---

# Entradas

- Change Set;
- dependency graph;
- lineage graph;
- active snapshot;
- profiles;
- schemas;
- security metadata;
- ontology.

---

# Impacted Artifact Types

```text
indexable_unit
chunk
embedding
lexical_entry
vector_entry
structured_entry
metadata_entry
entity_entry
statement_entry
relation_entry
citation_entry
graph_entry
path_entry
summary
cache_entry
```

---

# Impact Record

```yaml
impact_record:
  change:
    id: IDX-CHANGE-000041

  affected:
    units:
      - IDX-UNIT-000041

    chunks:
      - IDX-CHUNK-000041
      - IDX-CHUNK-000042

    embeddings:
      - EMB-000041
      - EMB-000042

    index_entries:
      - IDX-LEX-ENTRY-000041
      - IDX-VEC-ENTRY-000041

  impact_types:
    - content
    - citation
    - embedding
```

---

# Impact Dimensions

```text
content
structure
context
security
citation
embedding
lexical
structured
graph
ranking
temporal
```

---

# Direct Impact

El artefacto procede directamente del recurso modificado.

---

# Indirect Impact

El artefacto depende de un recurso modificado.

---

# Ejemplo

```text
Ingredient renamed
        ↓
Entity Entry impacted
        ↓
Recipes referencing ingredient impacted
        ↓
Contextualized chunks impacted
        ↓
Embeddings impacted
```

---

# Transitive Impact

Podrá propagarse a varias capas.

---

# Límite de propagación

Deberá controlarse mediante:

- tipos de dependencia;
- profundidad;
- perfil;
- coste;
- criticidad.

---

# Impact indeterminado

Cuando no pueda calcularse con confianza, el sistema deberá:

- ampliar scope;
- seleccionar full rebuild;
- bloquear;
- requerir aprobación.

---

# Error

```text
INDEX_IMPACT_ANALYSIS_INDETERMINATE
```

---

# Security Impact

Deberá propagarse incluso si:

- el contenido no cambió;
- el embedding puede reutilizarse;
- el índice físico permanece igual.

---

# Prioridad de invalidación

Orden recomendado:

```text
Deletion
Security
Tenant
Classification
Content
Context
Ranking
Optimization
```

---

# Invalidation

La **Invalidation** declara que un artefacto derivado ya no debe considerarse válido.

Formato recomendado:

```text
IDX-INVALIDATION-XXXXXX
```

---

# Contrato

```yaml
index_invalidation:
  id: IDX-INVALIDATION-000041

  target:
    id: IDX-CHUNK-000041
    type: chunk

  reason:
    code: SOURCE_RESOURCE_UPDATED

  source_change:
    id: IDX-CHANGE-000041

  effective_at: 2026-08-01T20:00:00Z

  priority: normal
  status: pending
```

---

# Estados

```text
pending
scheduled
processing
applied
failed
cancelled
superseded
```

---

# Tipos de invalidación

```text
logical
physical
security
temporal
dependency
schema
model
manual
```

---

# Logical Invalidation

La entrada deja de ser válida lógicamente.

---

# Physical Invalidation

La entrada deberá eliminarse o marcarse físicamente.

---

# Security Invalidation

Debe impedir acceso de forma prioritaria.

---

# Temporal Invalidation

El recurso deja de estar vigente.

---

# Dependency Invalidation

Una dependencia cambió.

---

# Schema Invalidation

La entrada ya no cumple el schema activo.

---

# Model Invalidation

El embedding o resumen fue generado por un modelo retirado o bloqueado.

---

# Invalidation Scope

Podrá afectar:

```text
entry
chunk
unit
resource
collection
partition
component
suite
tenant
snapshot
```

---

# Invalidation Plan

Antes de aplicar cambios complejos deberá existir un plan.

Formato recomendado:

```text
IDX-INV-PLAN-XXXXXX
```

---

# Contrato

```yaml
invalidation_plan:
  id: IDX-INV-PLAN-000041

  change_set:
    id: IDX-CHANGESET-000041

  actions:
    invalidate:
      - IDX-LEX-ENTRY-000041
      - IDX-VEC-ENTRY-000041

    rebuild:
      - IDX-CHUNK-000041

    reuse:
      - IDX-STR-ENTRY-000041

    delete:
      - IDX-CITE-ENTRY-000017

  priority: normal
```

---

# Invalidation Strategy

Valores:

```text
immediate
batched
scheduled
lazy
on_read
```

---

# Immediate

Obligatoria para:

- eliminación;
- seguridad;
- tenant;
- información restringida.

---

# Batched

Adecuada para cambios no críticos.

---

# Scheduled

Adecuada para reconstrucciones costosas.

---

# Lazy

Solo deberá utilizarse cuando el contenido stale no implique riesgo.

---

# On Read

Podrá comprobarse la vigencia al consultar.

No deberá sustituir invalidación real para seguridad.

---

# Cascading Invalidation

Una invalidación podrá generar otras mediante el dependency graph.

---

# Límite

El sistema deberá evitar bucles de invalidación.

---

# Invalidation Marker

Una entrada invalidada deberá registrar:

```yaml
invalidation:
  status: invalidated
  invalidated_at: 2026-08-01T20:00:00Z
  reason: SOURCE_RESOURCE_UPDATED
  replacement: IDX-LEX-ENTRY-000052
```

---

# Tombstone

Un **Tombstone** representa explícitamente una eliminación lógica.

Formato recomendado:

```text
IDX-TOMBSTONE-XXXXXX
```

---

# Objetivos

- evitar resurrección;
- sincronizar consumidores;
- preservar historial;
- permitir replay;
- propagar eliminación.

---

# Contrato

```yaml
index_tombstone:
  id: IDX-TOMBSTONE-000041

  logical_key: REC-0017#DOCUMENT

  resource:
    id: REC-0017
    type: recipe

  deleted_at: 2026-08-01T20:00:00Z

  source_snapshot:
    id: DOC-SNAP-20260801-0001

  reason: resource_deleted

  revision: 18
```

---

# Tombstone Revision

Deberá permitir comparar eventos fuera de orden.

---

# Regla

Una actualización con revisión anterior al tombstone no deberá restaurar el recurso.

---

# Tombstone Scope

Podrá aplicarse a:

- recurso;
- chunk;
- logical key;
- partition;
- tenant.

---

# Retención de tombstones

Deberá superar:

- retención de eventos;
- retraso máximo de consumidores;
- ventana de replay;
- duración de backfills.

---

# Tombstone Compaction

Podrá compactarse sin perder su función lógica.

---

# Hard Delete

La eliminación física definitiva deberá ocurrir cuando:

- todos los consumidores procesaron el tombstone;
- finalizó la retención;
- no existe Legal Hold;
- se cumplieron requisitos de auditoría.

---

# Upsert

Un **Upsert** crea o sustituye una entrada mediante su clave lógica.

---

# Regla

El upsert deberá utilizar:

```text
logical_key
+
target_snapshot
+
expected_revision
```

o mecanismo equivalente.

---

# Upsert Contract

```yaml
index_upsert:
  logical_key: REC-0009#PREPARATION#WINDOW-01

  expected_revision: 16
  target_revision: 17

  entry:
    id: IDX-LEX-ENTRY-000052
```

---

# Compare-and-Swap

Podrá utilizarse para impedir sobrescrituras fuera de orden.

---

# Idempotent Upsert

Repetir el mismo upsert deberá devolver el mismo estado lógico.

---

# Upsert Conflict

```text
INDEX_ENTRY_REVISION_CONFLICT
```

---

# Partial Upsert

No deberá utilizarse para cambiar campos que afectan:

- fingerprint;
- seguridad;
- lineage;
- snapshot;

sin recalcular la entrada completa.

---

# Metadata-Only Update

Podrá admitirse cuando:

- el schema lo permita;
- no cambie contenido;
- no cambie embedding;
- la consistencia esté garantizada.

---

# Security Metadata Update

Deberá aplicarse atómicamente o invalidar primero.

---

# Delete Operation

La eliminación podrá implementarse mediante:

```text
soft delete
tombstone
hard delete
partition drop
snapshot retirement
```

---

# Soft Delete

Marca la entrada como no recuperable.

---

# Tombstone

Preserva la eliminación para sincronización.

---

# Hard Delete

Elimina físicamente.

---

# Partition Drop

Adecuado para:

- tenant eliminado;
- snapshot retirado;
- partición temporal expirada.

---

# Snapshot Retirement

Hace inaccesible un snapshot completo.

---

# Delete Manifest

Toda eliminación masiva deberá producir un manifest.

---

# Contrato

```yaml
delete_manifest:
  id: IDX-DELETE-MANIFEST-000041

  scope:
    resource: REC-0017

  deleted:
    lexical_entries: 4
    vector_entries: 4
    citation_entries: 4
    graph_entries: 2

  tombstones_created: 1

  status: completed
```

---

# Referential Cleanup

La eliminación deberá revisar:

- parent-child mappings;
- citations;
- paths;
- summaries;
- graph edges;
- cache entries.

---

# Dangling References

No deberán permanecer referencias activas hacia entradas eliminadas.

---

# Incremental Indexing

La **Indexación Incremental** procesa únicamente cambios y dependencias afectadas.

---

# Condiciones de elegibilidad

Podrá utilizarse cuando:

- los schemas son compatibles;
- el pipeline es compatible;
- el baseline es válido;
- el dependency graph está disponible;
- el impacto es determinable;
- el snapshot activo es conocido.

---

# Incremental Plan

```yaml
incremental_indexing_plan:
  id: IDX-PLAN-INC-000041

  baseline:
    index_snapshot: IDX-SNAP-20260725-0003

  target:
    source_snapshot: DOC-SNAP-20260801-0001

  changes:
    created: 12
    updated: 7
    deleted: 2
    impacted: 31

  actions:
    create: 84
    rebuild: 56
    reuse: 812
    delete: 14
```

---

# Reuse Ratio

La ejecución deberá medir:

```text
reused_entries
/
eligible_entries
```

---

# Incremental Execution

Formato recomendado:

```text
IDX-INC-EXEC-XXXXXX
```

---

# Flujo

```text
Resolve Baseline
↓
Validate Baseline
↓
Apply Tombstones
↓
Rebuild Changed Units
↓
Rebuild Impacted Units
↓
Reuse Compatible Entries
↓
Validate Candidate Snapshot
↓
Activate
```

---

# Deletions First

Las eliminaciones y cambios de seguridad deberán aplicarse antes de exponer nuevas entradas cuando exista riesgo.

---

# Incremental Snapshot

Aunque se construya mediante deltas, deberá representar un estado lógico completo.

---

# Copy-on-Write

Podrá reutilizar estructuras del snapshot anterior y escribir únicamente cambios.

---

# Overlay Index

Podrá existir:

```text
Base Snapshot
+
Delta Overlay
```

---

# Riesgo

El número de overlays deberá limitarse.

---

# Overlay Compaction

Tras cierto número de deltas deberá consolidarse.

---

# Incremental Gate

```yaml
quality_gate:
  id: QG-INCREMENTAL-INDEX-0001

  criteria:
    all:
      - baseline_valid == true
      - unresolved_changes == 0
      - security_changes_applied == true
      - tombstones_applied == true
      - impacted_dependencies_processed == true
      - orphan_entries == 0
```

---

# Reindexado selectivo

El **Selective Reindexing** reconstruye un scope concreto.

---

# Scopes

```text
resource
document
collection
tenant
partition
index_type
language
subgraph
date_range
```

---

# Casos

- corregir una receta;
- reconstruir una colección;
- regenerar embeddings de un idioma;
- reparar una partición;
- actualizar un índice concreto.

---

# Selective Reindex Request

```yaml
selective_reindex_request:
  id: IDX-REINDEX-REQ-000041

  scope:
    type: collection
    ids:
      - COL-RECIPES

  components:
    - lexical
    - vector
    - citation

  reason: parser_bug_fixed
```

---

# Reindex Expansion

El scope inicial podrá ampliarse por dependencias.

---

# Declaración obligatoria

La respuesta deberá informar del scope efectivo.

---

# Ejemplo

```yaml
effective_scope:
  requested_resources: 42
  impacted_resources: 19
  total_resources: 61
```

---

# Selective Reindex Isolation

Podrá ejecutarse en una suite candidata separada.

---

# No modificación directa del activo

La estrategia preferida será construir y activar un nuevo snapshot.

---

# Repair Reindex

Podrá reparar únicamente entradas defectuosas.

---

# Repair Preconditions

- causa identificada;
- mapping compatible;
- snapshot fuente disponible;
- lineage íntegro.

---

# Full Rebuild

El **Full Rebuild** reconstruye completamente uno o varios índices.

---

# Casos obligatorios o recomendados

- cambio de schema incompatible;
- cambio de dimensión vectorial;
- cambio de analyzer incompatible;
- cambio de chunking global;
- cambio de modelo de embeddings;
- corrupción;
- dependency graph no fiable;
- drift significativo;
- migración de proveedor.

---

# Full Rebuild Request

```yaml
full_rebuild_request:
  id: IDX-FULL-REQ-000041

  scope:
    type: repository

  profile:
    id: IDX-PROFILE-RAG-STANDARD
    version: 2.0.0

  target:
    environment: staging

  activation:
    automatic: false
```

---

# Full Rebuild Phases

```text
Plan
↓
Provision Candidate Target
↓
Extract Full Corpus
↓
Build Components
↓
Validate
↓
Compare with Active
↓
Approve
↓
Activate
↓
Monitor
↓
Retire Previous
```

---

# Parallel Build

Los componentes podrán construirse en paralelo cuando sus dependencias lo permitan.

---

# Consistency Barrier

La suite no podrá declararse lista hasta completar los componentes requeridos.

---

# Full Rebuild Cost

Deberá estimarse:

- duración;
- almacenamiento;
- embeddings;
- tráfico;
- coste;
- capacidad.

---

# Build Freeze

Podrá fijarse un snapshot canónico para evitar cambios durante la reconstrucción.

---

# Catch-Up Phase

Si el conocimiento cambió durante el rebuild:

```text
Full Build Snapshot
↓
Apply Incremental Catch-Up
↓
Validate Final Candidate
```

---

# No activar un rebuild desactualizado

---

# Full Rebuild Comparison

Deberá compararse con el índice activo.

---

# Métricas comparativas

- cobertura;
- entradas;
- tamaño;
- calidad;
- latencia;
- resultados canónicos;
- seguridad;
- costes.

---

# Full Rebuild Gate

```yaml
quality_gate:
  id: QG-FULL-REBUILD-0001

  criteria:
    all:
      - required_components_complete == true
      - source_coverage >= 0.99
      - critical_diagnostics == 0
      - security_tests_passed == true
      - retrieval_regression == false
      - rollback_ready == true
```

---

# Backfill

Un **Backfill** incorpora datos históricos o campos ausentes a índices existentes o candidatos.

---

# Casos

- añadir nuevo metadata;
- generar embeddings históricos;
- completar Citation Index;
- incorporar una colección antigua;
- rellenar fingerprints.

---

# Backfill Request

```yaml
backfill_request:
  id: IDX-BACKFILL-000041

  target:
    index: IDX-META-RAG-0001

  field:
    name: epistemic_layer

  scope:
    type: repository

  mode: candidate_snapshot
```

---

# Online Backfill

Actualiza estructuras mientras siguen sirviendo consultas.

---

# Offline Backfill

Se ejecuta sobre un índice candidato.

---

# Recomendación

Preferir backfill offline para cambios que afectan consistencia global.

---

# Backfill Cursor

Deberá permitir reanudación.

---

# Backfill Idempotency

Reprocesar el mismo lote no deberá duplicar ni alterar incorrectamente datos.

---

# Backfill Coverage

Deberá medir:

- elegibles;
- procesados;
- pendientes;
- fallidos.

---

# No campo parcialmente poblado sin metadata

El índice deberá poder distinguir si un backfill está:

```text
not_started
in_progress
complete
partial
failed
```

---

# Index Migration

Una **Index Migration** transforma un índice o suite entre versiones incompatibles.

Formato recomendado:

```text
IDX-MIGRATION-XXXXXX
```

---

# Casos

- nuevo schema;
- cambio de proveedor;
- cambio de partición;
- nueva dimensión;
- nuevo analyzer;
- cambio de logical key;
- nueva política de seguridad.

---

# Migration Record

```yaml
index_migration:
  id: IDX-MIGRATION-000041

  source:
    index: IDX-VECTOR-RAG-0001
    schema: IDX-SCHEMA-VECTOR-RAG@1.0.0

  target:
    index: IDX-VECTOR-RAG-0002
    schema: IDX-SCHEMA-VECTOR-RAG@2.0.0

  strategy: rebuild

  status: planning
```

---

# Estrategias

```text
in_place
copy_transform
rebuild
dual_write
read_adapter
export_import
```

---

# In-Place Migration

Solo deberá utilizarse para cambios compatibles y de bajo riesgo.

---

# Copy-Transform

Copia entradas hacia una nueva estructura aplicando transformación.

---

# Rebuild

Reconstruye desde fuentes canónicas.

Será la opción preferida cuando la transformación derivada no sea fiable.

---

# Dual Write

Escribe simultáneamente en índice antiguo y nuevo durante una transición.

---

# Read Adapter

Permite que un consumidor lea versiones distintas mediante adaptación.

---

# Export-Import

Adecuado para migraciones de proveedor, con controles de seguridad.

---

# Migration Plan

Deberá declarar:

- source;
- target;
- strategy;
- mappings;
- compatibility;
- validation;
- cutover;
- rollback;
- cleanup.

---

# Schema Migration Mapping

```yaml
migration_mapping:
  source_field: preparation_time
  target_field: preparation_time_minutes

  transformation:
    type: duration_to_minutes
```

---

# No transformación irreversible sin fuente canónica

---

# Dual Write

El **Dual Write** mantiene dos índices actualizados durante una migración.

---

# Flujo

```text
Canonical Change
    ├── Write Old Index
    └── Write New Index
```

---

# Riesgos

- divergencia;
- orden;
- fallos parciales;
- costes;
- duplicación;
- complejidad.

---

# Dual Write State

```text
disabled
shadow
active
degraded
stopping
completed
```

---

# Write Result

Deberá registrar resultado por destino.

---

# Contrato

```yaml
dual_write_result:
  change: IDX-CHANGE-000041

  destinations:
    old_index:
      status: succeeded

    new_index:
      status: failed
      retryable: true

  overall_status: partial
```

---

# Atomicidad

No deberá asumirse atomicidad distribuida.

---

# Divergence Queue

Los fallos parciales deberán registrarse para reconciliación.

---

# Dual Write Reconciliation

Deberá comparar ambos destinos.

---

# Duración limitada

El dual write deberá tener:

- owner;
- fecha de inicio;
- fecha objetivo de retirada;
- métricas;
- criterio de salida.

---

# No dual write permanente

---

# Shadow Indexing

El **Shadow Indexing** construye y consulta un índice candidato sin afectar respuestas productivas.

---

# Objetivos

- comparar calidad;
- medir latencia;
- detectar errores;
- validar migraciones;
- probar modelos.

---

# Flujo

```text
Production Query
    ├── Active Index → User Response
    └── Shadow Index → Evaluation Only
```

---

# Shadow Query Result

No deberá influir en la respuesta visible.

---

# Shadow Metrics

- overlap de resultados;
- recall;
- ranking difference;
- latency;
- failures;
- security mismatches.

---

# Query Sampling

No será necesario duplicar todo el tráfico.

---

# Privacidad

El shadow index deberá respetar las mismas restricciones de:

- tenant;
- clasificación;
- logging;
- retención.

---

# Shadow Comparison

```yaml
shadow_comparison:
  query_id: RET-QUERY-000041

  active:
    snapshot: IDX-SNAP-OLD
    result_ids:
      - REC-0009
      - REC-0012

  shadow:
    snapshot: IDX-SNAP-NEW
    result_ids:
      - REC-0009
      - REC-0018

  overlap_at_10: 0.8
```

---

# Shadow Gate

La promoción podrá requerir umbrales mínimos.

---

# Blue-Green Indexing

La estrategia Blue-Green mantiene dos entornos completos.

---

# Blue

Snapshot actualmente activo.

---

# Green

Snapshot candidato.

---

# Flujo

```text
Build Green
↓
Validate Green
↓
Shadow Test Green
↓
Approve
↓
Switch Logical Pointer
↓
Monitor
↓
Retain Blue
↓
Retire Blue
```

---

# Ventajas

- activación atómica;
- rollback rápido;
- aislamiento;
- comparación.

---

# Coste

Requiere capacidad duplicada durante la transición.

---

# Green Catch-Up

Antes de activar deberá incorporar cambios ocurridos durante el build.

---

# Cutover

El cambio deberá realizarse mediante:

- alias;
- manifest activo;
- routing pointer;
- configuration version.

---

# Cutover Record

```yaml
cutover:
  id: IDX-CUTOVER-000041

  from: IDX-SNAP-BLUE
  to: IDX-SNAP-GREEN

  environment: production

  status: completed
  switched_at: 2026-08-01T22:00:00Z
```

---

# Cutover Freeze

Podrá utilizarse una ventana breve para asegurar consistencia.

---

# No necesidad de downtime

La arquitectura deberá intentar evitar interrupciones.

---

# Snapshot Management

Un **Index Snapshot** representa una vista lógica completa.

---

# Tipos de snapshot

```text
full
incremental
composite
historical
preview
migration
repair
```

---

# Snapshot Manifest

Deberá incluir:

- fuentes;
- componentes;
- schemas;
- perfiles;
- modelos;
- métricas;
- checksums;
- lineage;
- seguridad;
- estado.

---

# Contrato

```yaml
index_snapshot:
  id: IDX-SNAP-20260801-0001

  type: incremental
  status: candidate

  parent:
    id: IDX-SNAP-20260725-0003

  source_snapshots:
    documents: DOC-SNAP-20260801-0001
    knowledge_graph: KG-SNAP-20260801-0004

  change_set:
    id: IDX-CHANGESET-000041

  components:
    lexical: IDX-LEX-SNAP-000052
    vector: IDX-VEC-SNAP-000052
    metadata: IDX-META-SNAP-000052
    citation: IDX-CITE-SNAP-000052

  quality_gate:
    id: QG-RESULT-INDEX-000041

  created_at: 2026-08-01T21:30:00Z
```

---

# Snapshot Parent

Un snapshot incremental deberá declarar su predecesor.

---

# Snapshot Lineage Graph

Podrá existir una cadena:

```text
S1
↓
S2
↓
S3
```

y ramas para:

- previews;
- migraciones;
- experimentos.

---

# No ciclos

El lineage de snapshots deberá ser acíclico.

---

# Snapshot Immutability

Una vez `ready` o `active`, no deberá modificarse.

---

# Snapshot Reproducibility

Deberá poder reconstruirse con:

- source snapshots;
- profile;
- pipeline;
- models;
- mappings;
- schemas.

---

# Snapshot Checksum

Podrá calcularse sobre:

- manifest;
- component checksums;
- metadata.

---

# Snapshot Size

Deberá registrarse por componente.

---

# Snapshot Freshness

```yaml
freshness:
  source_snapshot: DOC-SNAP-20260801-0001
  latest_canonical_snapshot: DOC-SNAP-20260801-0001
  lag_seconds: 0
  status: current
```

---

# Snapshot Lag

Podrá medirse como:

```text
latest canonical revision
-
indexed canonical revision
```

o por tiempo.

---

# Activation

La activación convierte un snapshot candidato en el snapshot utilizado por consumidores.

---

# Activation Request

```yaml
activation_request:
  id: IDX-ACT-REQ-000041

  snapshot:
    id: IDX-SNAP-20260801-0001

  environment: production

  expected_active_snapshot:
    id: IDX-SNAP-20260725-0003

  reason: validated_incremental_update
```

---

# Precondiciones

- snapshot `ready`;
- Gate aprobado;
- catch-up completo;
- seguridad validada;
- consumers compatibles;
- rollback disponible;
- no activación concurrente;
- recursos suficientes.

---

# Optimistic Activation

Deberá comprobar:

```text
expected active snapshot
```

---

# Error

```text
INDEX_ACTIVE_SNAPSHOT_CONFLICT
```

---

# Activation Modes

```text
manual
automatic
scheduled
canary
progressive
emergency
```

---

# Manual

Requiere aprobación.

---

# Automatic

Permitido para cambios de bajo riesgo bajo política.

---

# Scheduled

Se ejecuta en una ventana.

---

# Canary

Expone el nuevo snapshot a una fracción controlada.

---

# Progressive

Aumenta gradualmente tráfico.

---

# Emergency

Se utiliza para correcciones críticas.

---

# Progressive Activation

Podrá aplicarse por:

- tenant;
- porcentaje;
- consumer;
- región;
- query type.

---

# Snapshot Routing

El routing deberá ser explícito.

---

# Activation Event

```text
index_snapshot_activated
```

---

# Post-Activation Monitoring

Deberá observar:

- errores;
- latencia;
- calidad;
- zero results;
- seguridad;
- carga;
- costes.

---

# Stabilization Window

Durante un periodo el snapshot anterior deberá conservarse.

---

# Activation Complete

No deberá declararse finalizada hasta superar la ventana de estabilización cuando la política lo exija.

---

# Rollback

El **Rollback** reactiva un snapshot anterior.

---

# Motivos

- regresión de calidad;
- errores;
- latencia;
- incompatibilidad;
- corrupción;
- fuga de seguridad;
- costes inesperados.

---

# Rollback Request

```yaml
rollback_request:
  id: IDX-ROLLBACK-REQ-000041

  current_snapshot:
    id: IDX-SNAP-20260801-0001

  target_snapshot:
    id: IDX-SNAP-20260725-0003

  reason:
    code: RETRIEVAL_QUALITY_REGRESSION

  emergency: false
```

---

# Preconditions

- target disponible;
- compatible con consumidores;
- seguridad aún válida;
- fuentes eliminadas tratadas;
- no viola obligaciones actuales.

---

# Seguridad y rollback

No deberá reactivarse un snapshot que contenga:

- datos eliminados;
- permisos obsoletos;
- clasificación antigua;
- tenant incorrecto.

---

# Secure Rollback

Podrá requerir aplicar primero:

- tombstones recientes;
- security deltas;
- eliminaciones críticas.

---

# Rollback Types

```text
full
component
routing
configuration
model
```

---

# Component Rollback

Solo será seguro si se conserva consistencia de suite.

---

# No suite mixta sin validación

---

# Rollback Event

```text
index_snapshot_rolled_back
```

---

# Rollback Audit

Deberá registrar:

- actor;
- motivo;
- impacto;
- snapshots;
- hora;
- resultado.

---

# Re-forward

Tras corregir el problema podrá activarse un nuevo snapshot, no modificar el fallido.

---

# Compaction

La **Compactación** consolida deltas, overlays o segmentos.

---

# Objetivos

- reducir profundidad;
- liberar espacio;
- mejorar latencia;
- simplificar recuperación;
- eliminar entradas obsoletas.

---

# Casos

- overlays incrementales;
- tombstones;
- segmentos pequeños;
- versiones físicas;
- cachés.

---

# Compaction Types

```text
logical
physical
overlay
tombstone
segment
metadata
```

---

# Logical Compaction

Consolida el estado visible.

---

# Physical Compaction

Reorganiza almacenamiento sin cambiar semántica.

---

# Overlay Compaction

Fusiona:

```text
Base
+
Delta 1
+
Delta 2
```

en un nuevo snapshot completo.

---

# Tombstone Compaction

Reduce tombstones preservando su efecto.

---

# Compaction Request

```yaml
compaction_request:
  id: IDX-COMPACT-REQ-000041

  target:
    index: IDX-LEX-RAG-0001

  strategy: overlay

  source_snapshots:
    - IDX-SNAP-000038
    - IDX-SNAP-000039
    - IDX-SNAP-000040
```

---

# Compaction Preconditions

- snapshots inmutables;
- lineage completo;
- tombstones procesados;
- no Legal Hold;
- validación posterior.

---

# No cambio lógico

La compactación deberá producir resultados equivalentes.

---

# Equivalence Validation

Deberá comparar:

- logical keys;
- counts;
- hashes;
- golden queries;
- seguridad.

---

# Retention

La retención define cuánto tiempo se conservan:

- snapshots;
- artefactos;
- índices;
- tombstones;
- manifests;
- logs;
- previews.

---

# Retention Policy

Formato recomendado:

```text
IDX-RETENTION-POLICY-XXXXXX
```

---

# Contrato

```yaml
index_retention_policy:
  id: IDX-RETENTION-POLICY-PRODUCTION

  active_snapshot:
    retention: indefinite_while_active

  superseded_snapshots:
    minimum_count: 3
    maximum_age: P90D

  preview_snapshots:
    maximum_age: P7D

  tombstones:
    minimum_age: P30D

  artifacts:
    maximum_age: P14D
```

---

# Factores

- rollback;
- auditoría;
- privacidad;
- coste;
- replay;
- regulación;
- debugging.

---

# Snapshot Retention

Deberá conservar al menos:

- activo;
- rollback inmediato;
- versiones requeridas por auditoría.

---

# Preview Retention

Deberá ser corta.

---

# Migration Snapshot Retention

Deberá mantenerse hasta completar:

- cutover;
- estabilización;
- rollback window;
- auditoría.

---

# Legal Hold

Deberá impedir eliminación.

---

# Retention Override

Requerirá:

- permiso;
- justificación;
- expiración;
- auditoría.

---

# Garbage Collection

La **Garbage Collection** elimina artefactos que ya no son necesarios.

---

# Candidatos

- snapshots expirados;
- índices no referenciados;
- artefactos temporales;
- chunks obsoletos;
- embeddings sin referencias;
- previews vencidos;
- cachés expiradas;
- logs temporales.

---

# GC Mark-and-Sweep conceptual

```text
Mark Referenced
↓
Identify Unreferenced
↓
Apply Retention
↓
Check Legal Hold
↓
Delete
↓
Audit
```

---

# GC Candidate

```yaml
gc_candidate:
  id: IDX-GC-CANDIDATE-000041

  resource:
    id: IDX-VEC-SNAP-000020
    type: vector-index-snapshot

  reason: retention_expired

  referenced: false
  legal_hold: false
```

---

# Dry-Run

La GC deberá soportar dry-run.

---

# GC Request

```yaml
garbage_collection_request:
  id: IDX-GC-REQ-000041

  scope:
    environment: production

  mode: dry_run
```

---

# GC Report

```yaml
garbage_collection_report:
  candidates: 48
  protected: 12
  deletable: 36
  estimated_storage_bytes: 920000000
```

---

# No eliminación inmediata sin manifest

---

# GC Safety

Deberá comprobar:

- aliases;
- snapshot lineage;
- rollback references;
- Legal Hold;
- migrations;
- active jobs;
- exports.

---

# GC Tombstones

Los tombstones podrán eliminarse únicamente cuando ya no exista riesgo de resurrección.

---

# Reconciliation

La **Reconciliación** compara conocimiento canónico e índices.

---

# Objetivos

- detectar eventos perdidos;
- detectar entradas huérfanas;
- detectar recursos ausentes;
- detectar security drift;
- comprobar counts;
- verificar hashes.

---

# Reconciliation Modes

```text
sample
partition
component
suite
full
security
```

---

# Sample Reconciliation

Comprueba una muestra.

---

# Full Reconciliation

Compara el corpus completo.

---

# Security Reconciliation

Prioriza:

- tenant;
- clasificación;
- ACL;
- eliminaciones.

---

# Reconciliation Request

```yaml
reconciliation_request:
  id: IDX-RECON-REQ-000041

  source_snapshot:
    id: DOC-SNAP-20260801-0001

  index_snapshot:
    id: IDX-SNAP-20260801-0001

  mode: full
```

---

# Reconciliation Checks

```text
resource presence
logical key presence
fingerprints
security metadata
citation integrity
snapshot compatibility
deletion propagation
coverage
```

---

# Reconciliation Result

```yaml
reconciliation_result:
  id: IDX-RECON-RESULT-000041

  status: drift_detected

  expected_resources: 129
  indexed_resources: 128

  differences:
    missing: 1
    orphan: 0
    mismatched: 2
    security_mismatches: 0
```

---

# Repair Plan

La reconciliación podrá generar:

```text
IDX-REPAIR-PLAN-XXXXXX
```

---

# Contrato

```yaml
repair_plan:
  id: IDX-REPAIR-PLAN-000041

  actions:
    rebuild:
      - REC-0042

    update_metadata:
      - DOC-0051

    delete_orphans:
      - IDX-LEX-ENTRY-009999
```

---

# Auto-Repair

Solo deberá permitirse para:

- cambios seguros;
- reglas conocidas;
- operaciones idempotentes.

---

# Manual Review

Será necesaria para:

- conflictos;
- datos sensibles;
- divergencias semánticas;
- pérdidas masivas.

---

# Drift

El **Index Drift** representa una divergencia entre el estado esperado y el real.

---

# Tipos

```text
content_drift
structure_drift
security_drift
schema_drift
model_drift
coverage_drift
citation_drift
configuration_drift
```

---

# Content Drift

El índice contiene contenido distinto de la fuente.

---

# Security Drift

Los permisos no coinciden.

Deberá considerarse crítico.

---

# Schema Drift

Las entradas no cumplen el schema esperado.

---

# Model Drift

El espacio vectorial o rendimiento ha cambiado.

---

# Coverage Drift

Disminuye la proporción de recursos representados.

---

# Citation Drift

Las citas ya no resuelven correctamente.

---

# Drift Record

```yaml
drift_record:
  id: IDX-DRIFT-000041

  type: security_drift
  severity: critical

  target:
    id: IDX-META-ENTRY-000041

  expected:
    classification: restricted

  actual:
    classification: internal
```

---

# Drift Response

Valores:

```text
ignore
monitor
repair
invalidate
rebuild
rollback
block
```

---

# Drift Thresholds

Deberán definirse por tipo.

---

# Security Drift

Umbral recomendado:

```text
0
```

---

# Coverage Drift

Podrá tolerar pequeños gaps según perfil.

---

# Recovery After Failure

El Indexing Engine deberá recuperarse de fallos sin corromper el estado activo.

---

# Tipos de fallo

```text
worker failure
batch failure
storage failure
provider failure
activation failure
partial write
event loss
checkpoint corruption
snapshot corruption
```

---

# Worker Failure

El job podrá reasignarse desde checkpoint.

---

# Batch Failure

Podrá reintentarse o aislarse.

---

# Storage Failure

Deberá impedir promoción del snapshot.

---

# Partial Write

La entrada deberá verificarse mediante manifest y fingerprint.

---

# Activation Failure

El snapshot anterior deberá permanecer activo.

---

# Event Loss

La reconciliación deberá detectarlo.

---

# Checkpoint Corruption

Deberá retrocederse al checkpoint anterior válido.

---

# Snapshot Corruption

Deberá:

- invalidarse;
- impedir activación;
- restaurarse;
- reconstruirse.

---

# Recovery Plan

Formato recomendado:

```text
IDX-RECOVERY-PLAN-XXXXXX
```

---

# Contrato

```yaml
recovery_plan:
  id: IDX-RECOVERY-PLAN-000041

  failure:
    code: PARTIAL_VECTOR_WRITE

  strategy:
    type: resume_from_checkpoint

  checkpoint:
    id: IDX-CHK-000040

  cleanup:
    delete_partial_records: true
```

---

# Write-Ahead Manifest

Podrá registrar intención antes de escribir.

---

# Completed Batch Manifest

Permitirá identificar qué lotes son válidos.

---

# Orphan Physical Records

Deberán detectarse y limpiarse.

---

# Recovery Idempotency

Repetir una recuperación no deberá duplicar entradas.

---

# Concurrency

Varias ejecuciones pueden afectar al mismo ámbito.

---

# Tipos de conflicto

```text
concurrent_incremental
incremental_vs_full
activation_vs_activation
migration_vs_rebuild
gc_vs_activation
rollback_vs_build
```

---

# Scope Lock

Podrá utilizarse un bloqueo lógico por:

- suite;
- tenant;
- alias;
- partition;
- environment.

---

# Read-Write Separation

Los builds candidatos no deberán bloquear lectura del snapshot activo.

---

# Concurrent Incrementals

Podrán:

- serializarse;
- fusionarse;
- rebasarse;
- cancelarse;

según política.

---

# Rebase

Una ejecución construida sobre un baseline antiguo podrá aplicar los cambios posteriores.

---

# Rebase Preconditions

- Change Sets compatibles;
- sin conflicto;
- lineage íntegro;
- seguridad actualizada.

---

# Stale Build

Un build deberá marcarse stale si su baseline ya no puede promoverse.

---

# Error

```text
INDEX_BUILD_BASELINE_STALE
```

---

# Activation Lock

Solo una activación deberá modificar el pointer activo a la vez.

---

# Garbage Collection Lock

La GC no deberá eliminar recursos utilizados por:

- builds;
- rollback;
- migrations;
- activations.

---

# Consistency Model

El Indexing Engine deberá declarar varios niveles.

---

# Build Consistency

Los builders consumen snapshots fijos.

---

# Snapshot Consistency

La suite representa un estado lógico completo.

---

# Activation Consistency

El pointer cambia atómicamente.

---

# Query Consistency

Una consulta deberá ejecutarse contra una versión coherente.

---

# Session Consistency

Una sesión de retrieval prolongada podrá fijar el snapshot utilizado.

---

# Read-Your-Writes

Podrá ser necesario en:

- previews;
- editores;
- validaciones.

---

# Production Search

Podrá aceptar eventual consistency bajo límites.

---

# Security Consistency

Deberá ser fuerte o fail-closed.

---

# Freshness SLO

Podrá definirse:

```yaml
freshness_slo:
  normal_changes:
    maximum_lag: PT5M

  security_changes:
    maximum_lag: PT30S

  deletions:
    maximum_lag: PT30S
```

---

# Index Lag

Métricas:

```text
revision lag
time lag
event lag
resource lag
```

---

# API interna de operaciones

Podrán exponerse los siguientes recursos.

---

# Change Sets

```text
POST /api/v1/index-change-sets
GET  /api/v1/index-change-sets/{changeSetId}
```

---

# Incremental Executions

```text
POST /api/v1/indexing-executions
GET  /api/v1/indexing-executions/{executionId}
```

---

# Reindex

```text
POST /api/v1/index-reindex-requests
GET  /api/v1/index-reindex-requests/{requestId}
```

---

# Migrations

```text
POST /api/v1/index-migrations
GET  /api/v1/index-migrations/{migrationId}
```

---

# Activations

```text
POST /api/v1/index-activations
GET  /api/v1/index-activations/{activationId}
```

---

# Rollbacks

```text
POST /api/v1/index-rollbacks
GET  /api/v1/index-rollbacks/{rollbackId}
```

---

# Reconciliation

```text
POST /api/v1/index-reconciliations
GET  /api/v1/index-reconciliations/{reconciliationId}
```

---

# Garbage Collection

```text
POST /api/v1/admin/index-garbage-collections
GET  /api/v1/admin/index-garbage-collections/{gcId}
```

---

# Dry-Run

Deberá soportarse para:

- invalidación;
- reindexado;
- migración;
- activación;
- rollback;
- GC;
- reconciliación.

---

# Ejemplo

```http
POST /api/v1/index-reindex-requests?dryRun=true
```

---

# Dry-Run Result

```yaml
dry_run_result:
  affected_resources: 61
  rebuilt_chunks: 214
  regenerated_embeddings: 180
  estimated_duration: PT8M
  estimated_cost: 2.40
  blockers: []
```

---

# Permisos operativos

Ejemplos:

```text
index.changes.read
index.incremental.execute
index.reindex.execute
index.full_rebuild.execute
index.migration.execute
index.activate
index.rollback
index.reconcile
index.gc.execute
```

---

# Separación de funciones

El actor que construye no deberá activar automáticamente en entornos críticos salvo política aprobada.

---

# Operaciones de alto riesgo

- full rebuild;
- migración;
- activación;
- rollback;
- eliminación masiva;
- GC de producción.

Podrán requerir:

- MFA;
- aprobación;
- ventana;
- justificación.

---

# Eventos operativos

Catálogo inicial:

```text
index_change_set_created
index_change_detected
index_impact_analysis_completed
index_invalidation_planned
index_entry_invalidated
index_tombstone_created
incremental_indexing_started
incremental_indexing_completed
selective_reindex_started
full_rebuild_started
full_rebuild_completed
index_backfill_started
index_backfill_completed
index_migration_started
index_migration_completed
index_dual_write_degraded
shadow_index_evaluation_completed
index_snapshot_ready
index_snapshot_activated
index_snapshot_rolled_back
index_compaction_completed
index_reconciliation_completed
index_drift_detected
index_garbage_collection_completed
```

---

# Evento de drift

```yaml
event:
  type: index_drift_detected

  subject:
    id: IDX-SNAP-20260801-0001
    type: index-snapshot

  data:
    drift_type: security_drift
    severity: critical
    affected_entries: 1
```

---

# Evento de tombstone

```yaml
event:
  type: index_tombstone_created

  subject:
    id: IDX-TOMBSTONE-000041
    type: index-tombstone

  data:
    resource_id: REC-0017
    revision: 18
```

---

# Observabilidad

---

# Métricas de cambios

- Change Sets;
- items;
- changes by type;
- security changes;
- unresolved changes;
- impact size.

---

# Métricas incrementales

- reused entries;
- rebuilt entries;
- deleted entries;
- tombstones;
- reuse ratio;
- duration;
- lag.

---

# Métricas de rebuild

- corpus size;
- processing rate;
- embeddings generated;
- component duration;
- catch-up duration;
- total cost.

---

# Métricas de migración

- source entries;
- migrated entries;
- failures;
- divergence;
- dual-write lag;
- consumer adoption.

---

# Métricas de activación

- activation duration;
- errors;
- rollback rate;
- stabilization alerts;
- traffic distribution.

---

# Métricas de reconciliación

- missing;
- orphan;
- mismatched;
- security drift;
- repair count.

---

# Métricas de GC

- candidates;
- protected;
- deleted;
- reclaimed storage;
- failures.

---

# Métricas de frescura

- p50 lag;
- p95 lag;
- maximum lag;
- stale resources;
- stale partitions.

---

# Alertas

- lag superior al SLO;
- security invalidation retrasada;
- tombstone no aplicado;
- build stale;
- dual write divergente;
- drift crítico;
- snapshot corrupto;
- GC sobre recurso referenciado;
- rollback fallido;
- activación parcial.

---

# Logs

```yaml
log:
  event: incremental_indexing_completed

  execution: IDX-INC-EXEC-000041
  baseline: IDX-SNAP-20260725-0003
  target: IDX-SNAP-20260801-0001

  changes:
    created: 12
    updated: 7
    deleted: 2

  entries:
    reused: 812
    rebuilt: 140
    deleted: 14
```

---

# Trazas

```text
Change Event
↓
Change Set
↓
Impact Analysis
↓
Invalidation
↓
Rebuild
↓
Snapshot
↓
Gate
↓
Activation
```

---

# Auditoría

Deberán auditarse:

- invalidación manual;
- eliminación;
- full rebuild;
- migración;
- dual write;
- activación;
- rollback;
- retention override;
- Garbage Collection;
- reparación automática;
- security drift.

---

# Quality Gates operativos

---

# Gate de Change Set

```yaml
quality_gate:
  id: QG-INDEX-CHANGESET-0001

  criteria:
    all:
      - source_snapshot_resolved == true
      - baseline_snapshot_resolved == true
      - unresolved_change_types == 0
      - security_changes_classified == true
```

---

# Gate de invalidación

```yaml
quality_gate:
  id: QG-INDEX-INVALIDATION-0001

  criteria:
    all:
      - required_invalidations_planned == true
      - deletion_tombstones_created == true
      - security_invalidations_priority == immediate
      - dependency_impact_complete == true
```

---

# Gate de migración

```yaml
quality_gate:
  id: QG-INDEX-MIGRATION-0001

  criteria:
    all:
      - source_target_mapping_valid == true
      - migration_coverage >= 0.99
      - critical_diagnostics == 0
      - shadow_evaluation_passed == true
      - rollback_ready == true
```

---

# Gate de activación

```yaml
quality_gate:
  id: QG-INDEX-ACTIVATION-0001

  criteria:
    all:
      - candidate_snapshot_ready == true
      - candidate_snapshot_current == true
      - suite_validation_passed == true
      - security_validation_passed == true
      - rollback_snapshot_available == true
      - active_snapshot_unchanged == true
```

---

# Gate de reconciliación

```yaml
quality_gate:
  id: QG-INDEX-RECONCILIATION-0001

  criteria:
    all:
      - missing_required_resources == 0
      - orphan_entries == 0
      - security_mismatches == 0
      - deletion_mismatches == 0
      - broken_citations == 0
```

---

# Casos de uso

---

# Caso de uso 1 — Nueva receta

Se publica `REC-0043`.

El sistema:

- crea Change Item;
- analiza dependencias;
- genera unidades;
- crea chunks;
- genera embeddings;
- construye entradas;
- produce snapshot incremental;
- valida;
- activa.

---

# Caso de uso 2 — Cambio editorial sin impacto

Se corrige formato.

Los fingerprints indexables no cambian.

Las entradas se reutilizan.

---

# Caso de uso 3 — Cambio de ingrediente

Se modifica una entidad.

El impacto se propaga a:

- Entity Index;
- recetas relacionadas;
- chunks contextualizados;
- embeddings;
- graph paths.

---

# Caso de uso 4 — Eliminación

Se elimina una receta.

El sistema:

- crea tombstone;
- invalida entradas;
- elimina citas;
- elimina relaciones;
- invalida cachés;
- evita resurrección.

---

# Caso de uso 5 — Cambio de ACL

Un documento pasa de `internal` a `restricted`.

La invalidación de seguridad se aplica inmediatamente.

El índice no deberá servir la versión anterior durante el rebuild.

---

# Caso de uso 6 — Rebuild por modelo nuevo

Se cambia el modelo de embeddings.

Se crea:

- nuevo Vector Space;
- nuevo Vector Index;
- shadow evaluation;
- Composite Snapshot candidato;
- activación blue-green.

---

# Caso de uso 7 — Migración de proveedor

Se construye un índice nuevo mediante exportación controlada o rebuild.

Se ejecuta dual write temporal.

Se comparan resultados.

Se cambia el alias.

---

# Caso de uso 8 — Evento perdido

Un documento actualizado no se reindexa.

La reconciliación detecta fingerprint distinto y crea Repair Plan.

---

# Caso de uso 9 — Drift de seguridad

El índice conserva clasificación antigua.

La reconciliación genera alerta crítica, invalida la entrada y bloquea la suite si procede.

---

# Caso de uso 10 — Rollback seguro

El nuevo índice degrada el retrieval.

Antes de volver al anterior se reaplican:

- tombstones;
- cambios de seguridad;
- eliminaciones recientes.

---

# Caso de uso 11 — Backfill de metadata

Se añade `epistemic_layer`.

El backfill construye un snapshot candidato sin detener consultas.

---

# Caso de uso 12 — Garbage Collection

Expira un preview.

La GC verifica:

- ausencia de referencias;
- no Legal Hold;
- no job activo;

y elimina sus artefactos.

---

# Caso de uso 13 — Concurrent Incremental

Dos Change Sets llegan consecutivamente.

La segunda ejecución se rebasa sobre el snapshot candidato o se serializa.

---

# Caso de uso 14 — Compaction

Después de diez overlays incrementales se crea un snapshot consolidado equivalente.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Reindexar únicamente el recurso directo

Ignora dependencias.

---

## Confiar solo en eventos

Puede perder cambios.

---

## Confiar solo en timestamps

No refleja semántica.

---

## Incremental sin baseline válido

Produce inconsistencias.

---

## Reutilizar entradas sin fingerprints

Puede conservar contenido stale.

---

## Aplicar seguridad después del rebuild

Puede mantener exposición durante la transición.

---

## Eliminar sin tombstone

Permite resurrección.

---

## Hard delete inmediato

Puede romper replay y consumidores retrasados.

---

## Upsert sin revisión

Puede sobrescribir cambios recientes.

---

## Modificar el snapshot activo

Destruye inmutabilidad.

---

## Usar overlays indefinidamente

Aumenta complejidad y latencia.

---

## Full rebuild sin catch-up

Activa un índice ya obsoleto.

---

## Backfill directo en producción sin estado

Puede dejar campos parcialmente poblados.

---

## Migración in-place incompatible

Impide rollback.

---

## Dual write permanente

Genera deuda y divergencia.

---

## Ignorar fallos parciales de dual write

Produce índices distintos.

---

## Shadow index con datos o permisos diferentes

Invalida la comparación.

---

## Cambiar aliases por componente

Puede crear una suite mixta.

---

## Rollback a permisos antiguos

Puede reexponer datos.

---

## Rollback sin tombstones recientes

Resucita eliminaciones.

---

## Compactar sin validar equivalencia

Puede perder entradas.

---

## Retener todo indefinidamente

Aumenta coste y riesgo.

---

## Garbage Collection sin dry-run

Puede eliminar rollback o artefactos activos.

---

## GC sin revisar Legal Hold

Puede incumplir obligaciones.

---

## Reconciliación solo por conteos

Dos conjuntos pueden tener igual tamaño y contenido distinto.

---

## Auto-repair de conflictos semánticos

Puede ocultar errores.

---

## Ignorar drift pequeño de seguridad

No existe tolerancia segura.

---

## Builds concurrentes sin control

Pueden sobrescribirse.

---

## Activar sobre baseline stale

Pierde cambios.

---

## Asumir atomicidad distribuida

Oculta fallos parciales.

---

## No medir lag

Impide conocer frescura.

---

## Considerar snapshot ready igual a current

Puede estar validado, pero desactualizado.

---

## Eliminar previews sin invalidar enlaces

Deja referencias rotas.

---

# Reglas mínimas de conformidad

---

## Change Set identificado

Todo cambio incremental deberá pertenecer a un Change Set.

---

## Baseline fijado

Toda ejecución incremental deberá declarar snapshot base.

---

## Target fijado

Deberá declarar el snapshot canónico objetivo.

---

## Impacto calculado

Todo cambio deberá evaluar dependencias.

---

## Seguridad prioritaria

Los cambios de acceso deberán procesarse inmediatamente.

---

## Invalidación explícita

Los artefactos stale deberán identificarse.

---

## Tombstones

Toda eliminación deberá generar una marca persistente cuando proceda.

---

## Idempotencia

Los upserts y deletes deberán tolerar reintentos.

---

## Snapshot lógico completo

Un resultado incremental deberá representar un estado coherente.

---

## Reindexado gobernado

Toda reconstrucción selectiva deberá declarar scope efectivo.

---

## Full rebuild disponible

El sistema deberá poder reconstruir desde fuentes canónicas.

---

## Migración versionada

Todo cambio incompatible deberá utilizar un proceso explícito.

---

## Dual write limitado

Deberá disponer de fecha y criterio de finalización.

---

## Activación atómica

El cambio de snapshot deberá evitar versiones mixtas.

---

## Rollback seguro

No deberá restaurar datos o permisos obsoletos.

---

## Reconciliación periódica

Los índices deberán compararse con la fuente canónica.

---

## Drift medido

Las divergencias deberán clasificarse.

---

## Retención definida

Cada artefacto deberá disponer de política.

---

## Garbage Collection segura

Toda eliminación física deberá comprobar referencias.

---

## Recuperación

Los fallos parciales deberán poder reanudarse o limpiarse.

---

## Observabilidad

Deberán medirse lag, cobertura, drift y estado.

---

# Conformidad de Change Set

Será conforme cuando:

- tenga ID;
- declare baseline;
- declare target;
- clasifique cambios;
- preserve revisiones;
- conserve fingerprints;
- identifique seguridad.

---

# Conformidad de Impact Analysis

Será conforme cuando:

- identifique artefactos directos;
- identifique dependencias;
- declare tipos de impacto;
- declare scope efectivo;
- detecte incertidumbre.

---

# Conformidad de Invalidation Plan

Será conforme cuando:

- identifique Change Set;
- declare invalidaciones;
- declare rebuilds;
- declare reutilización;
- priorice seguridad;
- preserve lineage.

---

# Conformidad de Tombstone

Será conforme cuando:

- tenga logical key;
- identifique recurso;
- declare revisión;
- declare fecha;
- declare motivo;
- tenga retención;
- evite resurrección.

---

# Conformidad de Incremental Execution

Será conforme cuando:

- valide baseline;
- procese Change Set;
- aplique tombstones;
- reconstruya impactos;
- reutilice mediante fingerprints;
- produzca snapshot;
- supere Gate.

---

# Conformidad de Full Rebuild

Será conforme cuando:

- fije fuentes;
- estime coste;
- construya en aislamiento;
- aplique catch-up;
- compare calidad;
- prepare rollback;
- active atómicamente.

---

# Conformidad de Migration

Será conforme cuando:

- declare source y target;
- declare schemas;
- declare estrategia;
- preserve seguridad;
- permita validación;
- permita rollback;
- tenga owner y plazo.

---

# Conformidad de Activation

Será conforme cuando:

- identifique snapshot;
- valide expected active;
- supere Gate;
- sea atómica;
- preserve rollback;
- genere evento y auditoría.

---

# Conformidad de Rollback

Será conforme cuando:

- declare motivo;
- valide target;
- reaplique cambios críticos;
- preserve seguridad;
- sea auditable;
- monitorice resultado.

---

# Conformidad de Reconciliation

Será conforme cuando:

- compare fuentes e índices;
- verifique logical keys;
- verifique fingerprints;
- verifique seguridad;
- detecte huérfanos;
- produzca Repair Plan.

---

# Conformidad de Garbage Collection

Será conforme cuando:

- soporte dry-run;
- identifique referencias;
- respete retención;
- respete Legal Hold;
- genere manifest;
- sea auditable.

---

# Lista de comprobación

Antes de aprobar una operación incremental, migración o activación deberá comprobarse:

```text
[ ] El Change Set está identificado.
[ ] El baseline está fijado.
[ ] El target snapshot está fijado.
[ ] Los tipos de cambio están clasificados.
[ ] Los cambios de seguridad se han priorizado.
[ ] El análisis de impacto está completo.
[ ] El scope efectivo está declarado.
[ ] Las invalidaciones están planificadas.
[ ] Los recursos eliminados tienen tombstones.
[ ] Las revisiones se comparan correctamente.
[ ] Los upserts son idempotentes.
[ ] Las entradas reutilizadas tienen fingerprints compatibles.
[ ] Las dependencias indirectas se han procesado.
[ ] El snapshot incremental representa un estado completo.
[ ] El catch-up se ha aplicado cuando procede.
[ ] El reindexado se ejecuta en aislamiento.
[ ] El full rebuild dispone de estimación.
[ ] La migración tiene source y target explícitos.
[ ] El dual write tiene fecha de finalización.
[ ] El shadow index respeta seguridad.
[ ] La suite candidata ha sido validada.
[ ] Los aliases se cambiarán atómicamente.
[ ] El snapshot activo esperado coincide.
[ ] Existe rollback.
[ ] El rollback preserva tombstones y ACL actuales.
[ ] La ventana de estabilización está definida.
[ ] La retención está configurada.
[ ] La GC dispone de dry-run.
[ ] No existen Legal Holds incompatibles.
[ ] La reconciliación está programada.
[ ] El drift de seguridad es cero.
[ ] El lag está dentro del SLO.
[ ] Los Quality Gates han pasado.
[ ] Los eventos están definidos.
[ ] La auditoría está configurada.
```

---

# Arquitectura final de la Parte V

```text
Canonical Change
        ↓
Change Set
        ↓
Change Detection
        ↓
Impact Analysis
        ↓
Invalidation Plan
        ├── Reuse
        ├── Rebuild
        ├── Delete
        └── Tombstone
        ↓
Incremental or Full Build
        ↓
Candidate Snapshot
        ↓
Reconciliation
        ↓
Quality Gate
        ↓
Blue-Green Activation
        ↓
Stabilization
        ├── Continue
        └── Rollback
        ↓
Retention
        ↓
Compaction and Garbage Collection
```

---

# Transición hacia la Parte VI

Esta quinta parte ha definido:

- los Index Change Sets;
- los Change Items;
- las estrategias de detección;
- el análisis de impacto;
- los cambios directos, indirectos y transitivos;
- las invalidaciones;
- los Invalidation Plans;
- los tombstones;
- los upserts;
- las eliminaciones;
- la indexación incremental;
- los snapshots incrementales;
- los overlays;
- el reindexado selectivo;
- los repair builds;
- el full rebuild;
- el catch-up;
- los backfills;
- las migraciones;
- el dual write;
- el shadow indexing;
- blue-green indexing;
- los snapshots;
- la activación;
- los modos de activación;
- el rollback;
- la compactación;
- la retención;
- Garbage Collection;
- la reconciliación;
- el drift;
- la recuperación tras fallos;
- la concurrencia;
- el modelo de consistencia;
- las APIs internas;
- los permisos;
- los eventos;
- la observabilidad;
- los Quality Gates;
- los casos de uso;
- los antipatrones;
- las reglas de conformidad.

La Parte VI desarrollará:

- publicación de índices;
- Promotion Pipeline;
- ambientes;
- aprobación;
- Release Candidate;
- validación preproducción;
- Canary Activation;
- tráfico progresivo;
- políticas de rollout;
- Quality Gates globales;
- consultas canónicas;
- evaluación offline y online;
- observabilidad avanzada;
- SLI y SLO;
- alertas;
- dashboards;
- auditoría;
- APIs administrativas;
- seguridad operativa;
- gestión de incidentes;
- contratos de publicación;
- estado de capacidad del Indexing Engine.

---

# Conclusión

La indexación incremental y el ciclo de vida operativo permiten que los índices evolucionen junto al conocimiento canónico sin perder coherencia, seguridad ni trazabilidad.

El ciclo puede resumirse así:

```text
Detectar cambio
        ↓
Clasificar
        ↓
Calcular impacto
        ↓
Invalidar
        ↓
Reutilizar o reconstruir
        ↓
Crear snapshot
        ↓
Reconciliar
        ↓
Validar
        ↓
Activar
        ↓
Monitorizar
        ↓
Revertir o consolidar
```

Los Change Sets explican qué cambió.

El análisis de impacto determina qué artefactos quedan afectados.

Las invalidaciones impiden utilizar representaciones obsoletas.

Los tombstones evitan resurrecciones.

Los upserts mantienen identidad lógica.

La indexación incremental reduce coste.

El full rebuild garantiza reconstruibilidad.

Los backfills completan información histórica.

Las migraciones permiten evolucionar schemas y proveedores.

El dual write facilita transiciones controladas.

El shadow indexing permite evaluar sin afectar usuarios.

Blue-Green permite activar de forma atómica.

El rollback reduce riesgo.

La compactación evita acumulación de deltas.

La retención limita coste y exposición.

La reconciliación detecta cambios perdidos.

El drift mide divergencias.

La Garbage Collection elimina artefactos sin uso de forma segura.

Una ejecución incremental correcta deberá poder responder:

```text
¿Qué cambió?

¿Desde qué baseline?

¿Qué dependencias fueron afectadas?

¿Qué entradas se reutilizaron?

¿Qué entradas se reconstruyeron?

¿Qué recursos se eliminaron?

¿Qué tombstones se crearon?

¿Qué snapshot resultó?
```

Una activación correcta deberá poder responder:

```text
¿Qué snapshot se activó?

¿Qué snapshot estaba activo?

¿Qué Quality Gates superó?

¿Estaba actualizado respecto al conocimiento canónico?

¿Cómo se realizó el cambio?

¿Qué rollback está disponible?

¿Qué métricas se vigilan durante la estabilización?
```

Una migración correcta deberá poder responder:

```text
¿Qué índice se sustituye?

¿Qué schema se abandona?

¿Qué schema se adopta?

¿Qué estrategia se utilizó?

¿Cómo se verificó la equivalencia?

¿Existe dual write?

¿Existe shadow evaluation?

¿Cómo se revierte?
```

Con esta quinta parte queda formalizado el mantenimiento operativo de los índices de NovaCoquinaria.

La siguiente parte definirá cómo los snapshots candidatos se promocionan, publican, observan y gobiernan hasta convertirse en capacidades de recuperación activas y confiables.

---

# Parte VI — Publicación, promoción, evaluación, observabilidad y operación productiva del Indexing Engine

---

# Introducción

La Parte V ha definido el ciclo de vida técnico mediante el que los índices de NovaCoquinaria pueden:

- detectar cambios;
- calcular impacto;
- invalidar artefactos;
- reconstruir entradas;
- ejecutar indexación incremental;
- realizar full rebuilds;
- migrar schemas;
- mantener dual write;
- construir snapshots candidatos;
- activar;
- revertir;
- reconciliar;
- compactar;
- aplicar retención;
- ejecutar Garbage Collection.

Sin embargo, un snapshot correctamente construido no deberá convertirse automáticamente en una capacidad productiva.

Antes de que un índice pueda ser utilizado por:

- Retrieval Engine;
- Motor RAG;
- Search API;
- GraphRAG;
- agentes;
- interfaces humanas;
- sistemas externos;

deberá superar un proceso formal de:

```text
Evaluación
↓
Promoción
↓
Publicación
↓
Rollout
↓
Observación
↓
Estabilización
↓
Operación
```

Esta sexta parte define cómo los artefactos producidos por el Indexing Engine se convierten en capacidades activas, confiables y operables.

Conceptualmente:

```text
Candidate Index Snapshot
        ↓
Release Candidate
        ↓
Pre-Publication Validation
        ↓
Offline Evaluation
        ↓
Security Validation
        ↓
Promotion Gate
        ↓
Staging Publication
        ↓
Shadow / Canary Evaluation
        ↓
Production Rollout
        ↓
Stabilization Window
        ↓
Active Capability
        ↓
Continuous Monitoring
```

La publicación no deberá entenderse únicamente como el cambio de un alias físico.

Deberá representar una decisión gobernada mediante la que NovaCoquinaria declara que un snapshot:

- es coherente;
- es seguro;
- posee calidad suficiente;
- es compatible;
- está actualizado;
- puede ser operado;
- dispone de rollback;
- puede ser consumido dentro de unas garantías conocidas.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir el Publication Pipeline;
- formalizar el Promotion Pipeline;
- establecer ambientes;
- definir Release Candidates;
- formalizar Promotion Requests;
- establecer aprobaciones;
- definir Quality Gates globales;
- regular publicación en staging;
- formalizar shadow evaluation;
- definir canary activation;
- establecer progressive rollout;
- regular A/B retrieval;
- definir políticas de rollout;
- establecer validación offline;
- establecer validación online;
- formalizar Golden Queries;
- definir Benchmark Suites;
- establecer regression detection;
- formalizar aceptación productiva;
- definir observabilidad avanzada;
- establecer métricas operativas;
- definir dashboards;
- formalizar SLI y SLO;
- establecer alertas;
- definir capacidad y escalabilidad;
- formalizar APIs administrativas;
- regular seguridad operacional;
- establecer auditoría;
- definir gestión de incidentes;
- formalizar recuperación y continuidad;
- establecer criterios finales de conformidad del Indexing Engine.

---

# Principios de publicación

Toda publicación de índices deberá respetar los siguientes principios.

---

## Construir no implica publicar

Un snapshot podrá estar técnicamente completo y no ser apto para producción.

---

## Evaluación previa

Todo candidato deberá evaluarse antes de recibir tráfico real.

---

## Promoción gobernada

El paso entre ambientes deberá ser explícito.

---

## Misma identidad lógica

El artefacto promovido deberá conservar:

- snapshot;
- manifest;
- schemas;
- perfiles;
- modelos;
- checksums.

---

## No reconstrucción silenciosa entre ambientes

El mismo Release Candidate no deberá producir artefactos diferentes sin nueva identidad.

---

## Seguridad antes que calidad

Un índice con buena recuperación, pero con fallos de aislamiento o clasificación, deberá bloquearse.

---

## Compatibilidad verificada

Los consumidores deberán ser compatibles con:

- schemas;
- campos;
- Vector Spaces;
- aliases;
- capabilities.

---

## Rollout gradual cuando exista riesgo

Los cambios relevantes deberán introducirse progresivamente.

---

## Rollback preparado

No deberá iniciarse una publicación crítica sin una estrategia de reversión.

---

## Observabilidad antes de tráfico

Las métricas y alertas deberán estar disponibles antes de activar.

---

## Estabilización explícita

Una activación no deberá considerarse completada inmediatamente después del cambio de alias.

---

## No degradación silenciosa

Toda pérdida de capacidad o calidad deberá declararse.

---

## Evidencia de promoción

Cada decisión deberá conservar:

- resultados;
- Gates;
- aprobadores;
- motivos;
- fecha;
- excepciones.

---

## Separación de funciones

La construcción, validación, aprobación y activación podrán requerir actores diferentes.

---

## Reproducibilidad

Deberá ser posible reconstruir qué índice respondió a una consulta histórica.

---

# Arquitectura de publicación

```text
┌───────────────────────────────────────────────┐
│             Candidate Snapshot                │
│                                               │
│ Components · Manifest · Metrics · Lineage     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Release Candidate                 │
│                                               │
│ Freeze · Evidence · Compatibility · Owner     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│          Pre-Publication Validation           │
│                                               │
│ Quality · Security · Performance · Drift      │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Promotion Pipeline               │
│                                               │
│ Development → Staging → Production            │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                Rollout Control                │
│                                               │
│ Shadow · Canary · Progressive · Full           │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Production Operation              │
│                                               │
│ SLO · Alerts · Capacity · Incident Response   │
└───────────────────────────────────────────────┘
```

---

# Ambientes

El Indexing Engine deberá distinguir ambientes lógicos y operativos.

Valores iniciales:

```text
development
test
staging
production
preview
sandbox
disaster_recovery
```

---

# Development

Adecuado para:

- desarrollo;
- pruebas locales;
- cambios de pipeline;
- schemas experimentales;
- debugging.

---

# Test

Adecuado para:

- contract tests;
- integration tests;
- datasets controlados;
- pruebas automatizadas.

---

# Staging

Deberá reproducir, cuando sea viable:

- schemas productivos;
- modelos;
- configuración;
- seguridad;
- perfiles;
- volumen representativo.

---

# Production

Contendrá únicamente snapshots aprobados para consumidores reales.

---

# Preview

Aislado y orientado a:

- borradores;
- pruebas editoriales;
- consultas temporales;
- validación previa.

---

# Sandbox

Permitirá experimentación con:

- datos ficticios;
- límites;
- reset;
- sin garantías productivas.

---

# Disaster Recovery

Mantendrá capacidades necesarias para recuperar el servicio.

---

# Environment Record

```yaml
index_environment:
  id: IDX-ENV-STAGING

  name: staging

  status: available

  capabilities:
    lexical: true
    vector: true
    graph: true

  policies:
    production_data_allowed: limited
    automatic_activation: false
```

---

# Separación de ambientes

Deberán separarse:

- credenciales;
- aliases;
- almacenamiento;
- eventos;
- permisos;
- métricas;
- cachés.

---

# No mezcla de datos

Los datos de producción no deberán utilizarse fuera de producción sin:

- autorización;
- minimización;
- anonimización o pseudonimización;
- necesidad demostrada.

---

# Environment Promotion

La promoción no deberá significar copiar configuración manualmente.

Deberá utilizar artefactos versionados.

---

# Release Candidate

Un **Index Release Candidate** representa un snapshot congelado propuesto para publicación.

Formato recomendado:

```text
IDX-RC-XXXXXX
```

---

# Contrato

```yaml
index_release_candidate:
  id: IDX-RC-000041

  version: 1.4.0-rc.1

  snapshot:
    id: IDX-SNAP-20260801-0001

  suite:
    id: IDX-SUITE-RAG-MVP

  source_snapshots:
    documents: DOC-SNAP-20260801-0001
    knowledge_graph: KG-SNAP-20260801-0004

  pipeline:
    id: IDX-PIPELINE-RAG-0001
    version: 1.2.0

  profiles:
    indexing: IDX-PROFILE-RAG-STANDARD@1.1.0
    chunking: CHUNK-PROFILE-RAG-STANDARD@1.2.0
    embeddings: EMB-PROFILE-MULTILINGUAL-0001@2.0.0

  status: proposed

  owner:
    team: ai-platform
```

---

# Estados de Release Candidate

```text
draft
proposed
validating
rejected
approved_for_staging
staging
approved_for_production
publishing
active
superseded
withdrawn
failed
```

---

# Candidate Freeze

Una vez propuesta, la definición del candidato deberá quedar congelada.

---

# Cambio posterior

Cualquier modificación de:

- snapshot;
- profile;
- schema;
- model;
- mapping;
- Quality Gate;

deberá producir una nueva revisión del Release Candidate.

---

# Release Candidate Manifest

Deberá contener:

- componentes;
- checksums;
- schemas;
- dependencias;
- consumidores compatibles;
- métricas;
- resultados;
- riesgos;
- rollback.

---

# Ejemplo

```yaml
release_candidate_manifest:
  release_candidate: IDX-RC-000041

  components:
    lexical: IDX-LEX-SNAP-000052
    vector: IDX-VEC-SNAP-000052
    metadata: IDX-META-SNAP-000052
    citation: IDX-CITE-SNAP-000052

  checksums:
    lexical: ...
    vector: ...
    metadata: ...
    citation: ...

  evaluation:
    benchmark_result: IDX-BENCH-RESULT-000041
    security_result: IDX-SEC-RESULT-000041

  rollback:
    snapshot: IDX-SNAP-20260725-0003
```

---

# Promotion Request

Una **Promotion Request** solicita promover un Release Candidate a un ambiente.

Formato recomendado:

```text
IDX-PROMOTION-REQ-XXXXXX
```

---

# Contrato

```yaml
promotion_request:
  id: IDX-PROMOTION-REQ-000041

  release_candidate:
    id: IDX-RC-000041

  from_environment: staging
  to_environment: production

  requested_by:
    id: USER-0001
    type: user

  reason: retrieval_quality_improvement

  rollout_policy:
    id: IDX-ROLLOUT-CANARY-0001
```

---

# Estados

```text
requested
reviewing
approved
rejected
scheduled
executing
stabilizing
completed
rolled_back
failed
cancelled
```

---

# Promotion Evidence

La solicitud deberá enlazar con:

- Quality Gates;
- benchmark;
- security tests;
- compatibility report;
- operational readiness;
- rollback plan.

---

# Promotion Approval

Podrá requerir aprobación de:

- owner del índice;
- plataforma;
- seguridad;
- producto;
- operaciones.

---

# Approval Record

```yaml
promotion_approval:
  id: IDX-PROMOTION-APPROVAL-000041

  promotion_request:
    id: IDX-PROMOTION-REQ-000041

  approver:
    id: USER-SECURITY-0001
    type: user

  decision: approved

  scope:
    - security
    - privacy

  decided_at: 2026-08-01T20:00:00Z
```

---

# Separation of Duties

En producción podrá requerirse que:

```text
Builder
≠
Approver
≠
Activator
```

---

# Emergency Promotion

Podrá utilizarse para:

- vulnerabilidad;
- fuga de seguridad;
- eliminación urgente;
- corrupción crítica.

---

# Requisitos reforzados

- justificación;
- MFA;
- auditoría;
- owner;
- rollback;
- revisión posterior.

---

# Promotion Pipeline

El **Promotion Pipeline** coordina el paso del Release Candidate entre ambientes.

---

# Etapas recomendadas

```text
Candidate Freeze
↓
Artifact Verification
↓
Schema Validation
↓
Offline Evaluation
↓
Security Validation
↓
Compatibility Validation
↓
Staging Publication
↓
Staging Acceptance
↓
Production Approval
↓
Rollout
↓
Stabilization
↓
Completion
```

---

# Promotion Pipeline ID

Formato recomendado:

```text
IDX-PROMOTION-PIPELINE-XXXXXX
```

---

# Contrato

```yaml
promotion_pipeline:
  id: IDX-PROMOTION-PIPELINE-STANDARD

  version: 1.0.0

  stages:
    - artifact_verification
    - contract_validation
    - offline_evaluation
    - security_validation
    - staging_publication
    - staging_acceptance
    - production_approval
    - controlled_rollout
    - stabilization
```

---

# Stage Result

```yaml
promotion_stage_result:
  stage: offline_evaluation
  status: passed

  evidence:
    benchmark_result: IDX-BENCH-RESULT-000041

  diagnostics:
    errors: 0
    warnings: 2
```

---

# Estados de etapa

```text
pending
running
passed
passed_with_warnings
failed
skipped
blocked
cancelled
```

---

# Skip

Una etapa solo podrá omitirse por:

- perfil;
- emergencia;
- no aplicabilidad;
- waiver aprobado.

---

# Promotion Waiver

Una excepción deberá poseer:

- ID;
- criterio omitido;
- riesgo;
- aprobador;
- expiración;
- compensación.

---

# Contrato

```yaml
promotion_waiver:
  id: IDX-WAIVER-000041

  criterion: retrieval_ndcg_at_10

  current_value: 0.79
  required_value: 0.80

  justification: critical_security_fix

  expires_at: 2026-08-08T00:00:00Z
```

---

# No waiver para seguridad crítica

No deberán aceptarse excepciones para:

- tenant isolation;
- datos eliminados;
- permisos incorrectos;
- exposición de secretos;
- integridad comprometida.

---

# Publication Package

La publicación deberá utilizar un paquete inmutable.

Formato recomendado:

```text
IDX-PUBLICATION-PACKAGE-XXXXXX
```

---

# Contenido

```yaml
index_publication_package:
  id: IDX-PUBLICATION-PACKAGE-000041

  release_candidate: IDX-RC-000041

  snapshot: IDX-SNAP-20260801-0001

  manifests:
    - IDX-BUILD-MANIFEST-000041
    - IDX-SUITE-MANIFEST-000041

  contracts:
    - IDX-SCHEMA-LEXICAL-RAG@1.0.0
    - IDX-SCHEMA-VECTOR-RAG@2.0.0

  evidence:
    - IDX-BENCH-RESULT-000041
    - IDX-SEC-RESULT-000041
    - IDX-COMPAT-RESULT-000041

  checksum:
    algorithm: sha256
    value: ...
```

---

# Artifact Verification

Antes de publicar deberá comprobarse:

- checksum;
- firma;
- identidad;
- manifest;
- inmutabilidad;
- correspondencia entre componentes.

---

# Publication Record

Formato recomendado:

```text
IDX-PUBLICATION-XXXXXX
```

---

# Contrato

```yaml
index_publication:
  id: IDX-PUBLICATION-000041

  package:
    id: IDX-PUBLICATION-PACKAGE-000041

  environment: production

  status: stabilizing

  previous_snapshot:
    id: IDX-SNAP-20260725-0003

  current_snapshot:
    id: IDX-SNAP-20260801-0001

  started_at: 2026-08-01T22:00:00Z
```

---

# Publication States

```text
created
verifying
publishing
routing
stabilizing
completed
completed_with_warnings
failed
rolled_back
cancelled
```

---

# Publicación física y lógica

Deberá distinguirse:

```text
Physical Publication
```

de:

```text
Logical Activation
```

---

# Physical Publication

Hace que los componentes estén disponibles en el ambiente.

---

# Logical Activation

Hace que consumidores autorizados los utilicen.

---

# Pre-Publication Validation

Antes de promoción deberán verificarse varios niveles.

---

# Validaciones obligatorias

```text
artifact_integrity
schema
component_consistency
suite_consistency
security
privacy
compatibility
retrieval_quality
performance
operational_readiness
rollback_readiness
```

---

# Operational Readiness

Deberá comprobar:

- dashboards;
- alertas;
- capacidad;
- runbooks;
- permisos;
- soporte;
- rollback;
- owners.

---

# Operational Readiness Result

```yaml
operational_readiness:
  status: ready

  checks:
    dashboards_available: true
    alerts_configured: true
    rollback_tested: true
    on_call_owner_defined: true
    capacity_sufficient: true
```

---

# Evaluation Framework

La evaluación deberá medir la calidad del índice de forma sistemática.

---

# Capas de evaluación

```text
Structural Evaluation
Retrieval Evaluation
Security Evaluation
Performance Evaluation
Online Evaluation
Human Evaluation
```

---

# Structural Evaluation

Comprueba:

- cobertura;
- consistencia;
- lineage;
- mappings;
- citas;
- schemas.

---

# Retrieval Evaluation

Comprueba:

- recall;
- precision;
- ranking;
- relevancia;
- diversidad;
- grounding.

---

# Security Evaluation

Comprueba:

- aislamiento;
- filtros;
- ACL;
- eliminaciones;
- tenant;
- clasificación.

---

# Performance Evaluation

Comprueba:

- latencia;
- throughput;
- memoria;
- almacenamiento;
- coste.

---

# Online Evaluation

Mide comportamiento con tráfico real o representativo.

---

# Human Evaluation

Permite valorar:

- relevancia;
- utilidad;
- coherencia;
- errores difíciles de automatizar.

---

# Benchmark Suite

Una **Index Benchmark Suite** agrupa datasets y evaluaciones.

Formato recomendado:

```text
IDX-BENCH-SUITE-XXXXXX
```

---

# Contrato

```yaml
benchmark_suite:
  id: IDX-BENCH-SUITE-RAG-0001

  version: 1.0.0

  datasets:
    - IDX-DATASET-RECIPE-SEARCH
    - IDX-DATASET-FACTUAL-QUESTIONS
    - IDX-DATASET-SECURITY

  metrics:
    - recall_at_10
    - precision_at_5
    - ndcg_at_10
    - mrr
    - citation_accuracy
    - zero_result_rate
```

---

# Benchmark Dataset

Deberá incluir:

- queries;
- filtros;
- resultados relevantes;
- resultados prohibidos;
- dificultad;
- idioma;
- tipo.

---

# Dataset Record

```yaml
benchmark_dataset:
  id: IDX-DATASET-RECIPE-SEARCH

  version: 1.0.0

  domain: recipes

  queries: 250

  languages:
    - es

  reviewed_by:
    - culinary_domain_expert
    - retrieval_engineer
```

---

# Dataset Versioning

Todo cambio deberá producir una nueva versión.

---

# Dataset Leakage

El dataset de evaluación no deberá utilizarse de forma que sobreajuste continuamente el ranking sin validación externa.

---

# Golden Query

Una **Golden Query** representa un caso de referencia estable.

Formato recomendado:

```text
IDX-GOLDEN-QUERY-XXXXXX
```

---

# Contrato

```yaml
golden_query:
  id: IDX-GOLDEN-QUERY-000041

  query: recetas rápidas con garbanzos

  filters:
    maximum_total_time_minutes: 30

  expected:
    must_include:
      - REC-0012

    must_not_include:
      - REC-0088

  tolerances:
    must_include_within_rank: 5

  tags:
    - lexical
    - vector
    - structured_filter
```

---

# Tipos de Golden Query

```text
exact_match
semantic
hybrid
structured
entity
statement
graph
citation
security
negative
no_answer
```

---

# Query negativa

Verifica que un recurso no aparezca.

---

# No-Answer Query

Verifica que el sistema no devuelva resultados irrelevantes cuando no existe respuesta.

---

# Security Golden Query

Deberá comprobar:

- recursos prohibidos;
- tenant incorrecto;
- contenido eliminado;
- clasificación superior.

---

# Query Set Coverage

El conjunto deberá cubrir:

- recetas;
- ingredientes;
- técnicas;
- tablas;
- statements;
- relaciones;
- graph paths;
- multilingüismo;
- sinónimos;
- errores tipográficos;
- negaciones;
- restricciones.

---

# Offline Evaluation

Se ejecutará sin tráfico productivo.

---

# Ventajas

- reproducibilidad;
- comparación;
- seguridad;
- control.

---

# Métricas iniciales

```text
Recall@K
Precision@K
MRR
nDCG@K
Hit Rate
Zero Result Rate
Citation Accuracy
Security Violation Rate
```

---

# Recall@K

Mide la proporción de resultados relevantes recuperados dentro de K.

---

# Precision@K

Mide la proporción de resultados recuperados que son relevantes.

---

# MRR

Mide la posición del primer resultado relevante.

---

# nDCG

Evalúa ranking con relevancia graduada.

---

# Hit Rate

Indica si aparece al menos un resultado relevante.

---

# Zero Result Rate

Mide consultas sin resultados.

---

# Citation Accuracy

Mide si el resultado recuperado puede resolverse hacia la evidencia correcta.

---

# Security Violation Rate

Deberá ser:

```text
0
```

---

# Offline Evaluation Result

```yaml
benchmark_result:
  id: IDX-BENCH-RESULT-000041

  release_candidate: IDX-RC-000041

  suite: IDX-BENCH-SUITE-RAG-0001@1.0.0

  metrics:
    recall_at_10: 0.91
    precision_at_5: 0.87
    ndcg_at_10: 0.88
    mrr: 0.90
    citation_accuracy: 1.0
    security_violation_rate: 0.0

  status: passed
```

---

# Baseline Comparison

Todo candidato deberá compararse con:

- snapshot activo;
- última versión estable;
- objetivo mínimo.

---

# Regression

Una regresión podrá producirse aunque el valor absoluto supere el mínimo.

---

# Ejemplo

```text
Candidato nDCG = 0.84
Mínimo = 0.80
Activo = 0.91
```

Aunque supere el mínimo, existe regresión significativa.

---

# Regression Policy

Deberá definir tolerancias por métrica.

---

# Contrato

```yaml
regression_policy:
  id: IDX-REGRESSION-POLICY-0001

  thresholds:
    recall_at_10:
      maximum_relative_drop: 0.03

    ndcg_at_10:
      maximum_absolute_drop: 0.02

    security_violation_rate:
      maximum_value: 0
```

---

# Regression Result

```yaml
regression_result:
  candidate: IDX-RC-000041
  baseline: IDX-SNAP-20260725-0003

  regressions:
    - metric: ndcg_at_10
      baseline: 0.90
      candidate: 0.86
      allowed_drop: 0.02
      status: failed
```

---

# Segment Evaluation

Las métricas deberán desglosarse por:

- tipo de recurso;
- idioma;
- tenant;
- query type;
- dificultad;
- índice;
- perfil.

---

# No media única

Una media global puede ocultar una regresión en:

- tablas;
- alérgenos;
- consultas de seguridad;
- un idioma.

---

# Hard Queries

Deberán existir consultas difíciles:

- ambiguas;
- multihop;
- con negación;
- con sinónimos;
- con filtros combinados;
- con cantidades.

---

# Retrieval Evaluation por componente

Podrá aislarse:

- lexical;
- vector;
- graph;
- hybrid.

---

# Ablation Testing

Podrá medir el efecto de eliminar:

- contextualización;
- aliases;
- graph expansion;
- boosts;
- vector component.

---

# Online Evaluation

La evaluación online utiliza tráfico real o controlado.

---

# Estrategias

```text
shadow
canary
A/B test
interleaving
progressive exposure
```

---

# Shadow Evaluation

El candidato recibe consultas, pero no afecta la respuesta.

---

# Canary Evaluation

Una fracción limitada recibe resultados del candidato.

---

# A/B Test

Dos grupos utilizan versiones distintas.

---

# Interleaving

Combina resultados para evaluar preferencias de forma eficiente.

---

# Requisitos de privacidad

Las consultas reales deberán:

- minimizar datos;
- aplicar retención;
- evitar logging completo;
- respetar consentimiento y política.

---

# Online Metrics

- click-through;
- reformulation rate;
- abandonment;
- zero-result rate;
- answer grounding;
- citation usage;
- latency;
- errors;
- rollback signals.

---

# Advertencia

Las métricas de interacción no equivalen automáticamente a calidad.

---

# Search Satisfaction Proxy

Podrá combinar:

- clicks;
- dwell time;
- reformulaciones;
- feedback;
- éxito de tarea.

---

# Human Evaluation

Podrá utilizar revisores para comparar resultados.

---

# Evaluation Record

```yaml
human_evaluation:
  id: IDX-HUMAN-EVAL-000041

  candidate: IDX-RC-000041
  baseline: IDX-SNAP-20260725-0003

  evaluators: 3
  queries: 50

  result:
    candidate_preferred: 31
    baseline_preferred: 12
    tie: 7
```

---

# Blind Evaluation

Los evaluadores no deberían conocer qué versión produjo cada resultado cuando sea viable.

---

# Reviewer Guidelines

Deberán definir:

- relevancia;
- exactitud;
- diversidad;
- claridad;
- citabilidad;
- seguridad.

---

# Pre-Production Quality Gate

```yaml
quality_gate:
  id: QG-INDEX-PREPRODUCTION-0001

  criteria:
    all:
      - artifact_integrity == passed
      - schema_validation == passed
      - suite_consistency == passed
      - security_validation == passed
      - compatibility_validation == passed
      - offline_benchmark == passed
      - regression_check == passed
      - rollback_readiness == passed
      - observability_readiness == passed
```

---

# Production Promotion Gate

```yaml
quality_gate:
  id: QG-INDEX-PRODUCTION-PROMOTION-0001

  criteria:
    all:
      - staging_acceptance == passed
      - canary_plan_defined == true
      - capacity_check == passed
      - on_call_owner_defined == true
      - rollback_snapshot_available == true
      - critical_diagnostics == 0
      - security_violation_rate == 0
```

---

# Staging Publication

El Release Candidate deberá publicarse primero en staging cuando proceda.

---

# Staging Acceptance

Deberá comprobar:

- consultas reales simuladas;
- integración con Retrieval;
- integración con RAG;
- integración con APIs;
- permisos;
- observabilidad;
- rendimiento.

---

# Acceptance Suite

```yaml
staging_acceptance_suite:
  id: IDX-ACCEPTANCE-STAGING-0001

  tests:
    - retrieval_contract_tests
    - rag_grounding_tests
    - security_queries
    - latency_tests
    - failure_recovery_tests
```

---

# Consumer Compatibility

Los consumidores conocidos deberán validar compatibilidad.

---

# Consumer Types

- Retrieval Engine;
- RAG Engine;
- Search API;
- GraphRAG;
- Agent Tools;
- Analytics;
- administrative UI.

---

# Compatibility Record

```yaml
consumer_compatibility:
  consumer: RAG-ENGINE
  version: 1.3.0

  release_candidate: IDX-RC-000041

  status: compatible

  validated_capabilities:
    - vector_search
    - citation_resolution
    - metadata_filtering
```

---

# Capability Contract

El candidato deberá declarar capacidades disponibles.

---

# Ejemplo

```yaml
index_capabilities:
  lexical_search:
    status: available

  vector_search:
    status: available

  graph_paths:
    status: unavailable

  citation_resolution:
    status: available
```

---

# No asumir capacidades

El consumidor deberá descubrirlas o usar contratos versionados.

---

# Rollout Policy

Una **Rollout Policy** define cómo se activa un snapshot.

Formato recomendado:

```text
IDX-ROLLOUT-XXXXXX
```

---

# Contrato

```yaml
rollout_policy:
  id: IDX-ROLLOUT-CANARY-0001

  version: 1.0.0

  stages:
    - traffic_percentage: 1
      minimum_duration: PT15M

    - traffic_percentage: 10
      minimum_duration: PT30M

    - traffic_percentage: 50
      minimum_duration: PT1H

    - traffic_percentage: 100

  automatic_rollback:
    enabled: true
```

---

# Modos de rollout

```text
immediate
scheduled
shadow
canary
progressive
tenant_based
consumer_based
region_based
manual
```

---

# Immediate

Solo recomendable para:

- bajo riesgo;
- entorno no crítico;
- emergencia controlada.

---

# Scheduled

Se ejecuta en una ventana operativa.

---

# Shadow

No afecta respuestas visibles.

---

# Canary

Expone a una fracción pequeña.

---

# Progressive

Incrementa tráfico gradualmente.

---

# Tenant-Based

Activa para tenants seleccionados.

---

# Consumer-Based

Activa para consumidores concretos.

---

# Region-Based

Activa por región cuando exista despliegue distribuido.

---

# Canary Allocation

Podrá seleccionarse por:

- porcentaje aleatorio;
- tenant;
- user cohort;
- query type;
- consumer;
- capability.

---

# Sticky Assignment

Una sesión o usuario deberá mantener una versión coherente durante la evaluación cuando proceda.

---

# Canary Snapshot Routing

```yaml
routing_rule:
  active_snapshot: IDX-SNAP-OLD
  canary_snapshot: IDX-SNAP-NEW

  allocation:
    type: percentage
    value: 10
```

---

# Canary Metrics

Deberán compararse:

- error rate;
- p95 latency;
- zero results;
- relevance;
- security;
- RAG grounding;
- cost.

---

# Canary Gate

```yaml
quality_gate:
  id: QG-INDEX-CANARY-0001

  criteria:
    all:
      - canary_error_rate <= baseline_error_rate + 0.001
      - canary_p95_latency <= baseline_p95_latency * 1.10
      - relevance_regression == false
      - security_incidents == 0
      - citation_failures == 0
```

---

# Automatic Promotion

Podrá avanzar a la siguiente etapa si se cumplen los criterios.

---

# Manual Hold

Podrá requerirse revisión entre etapas.

---

# Automatic Rollback

Deberá activarse ante:

- fuga de seguridad;
- errores críticos;
- latencia extrema;
- corrupción;
- caída de disponibilidad;
- regresión severa.

---

# Rollback Trigger

```yaml
rollback_trigger:
  metric: security_violation_count
  operator: greater_than
  threshold: 0
  action: immediate_rollback
```

---

# Progressive Rollout State

```text
planned
shadowing
canary
expanding
full_traffic
stabilizing
completed
paused
rolled_back
failed
```

---

# Pause

El rollout podrá pausarse sin revertir inmediatamente.

---

# Resume

Solo si:

- el candidato sigue vigente;
- no cambió la fuente;
- las métricas son aceptables;
- la seguridad permanece válida.

---

# A/B Retrieval

Permite comparar dos configuraciones activas.

---

# Usos

- ranking;
- embeddings;
- analyzers;
- chunking;
- hybrid fusion;
- graph expansion.

---

# A/B Experiment

Formato recomendado:

```text
IDX-EXPERIMENT-XXXXXX
```

---

# Contrato

```yaml
index_experiment:
  id: IDX-EXPERIMENT-000041

  type: ab_retrieval

  variants:
    A:
      snapshot: IDX-SNAP-OLD

    B:
      snapshot: IDX-SNAP-NEW

  allocation:
    A: 0.5
    B: 0.5

  metrics:
    - successful_search_rate
    - reformulation_rate
    - citation_accuracy

  status: running
```

---

# Experiment Guardrails

Deberán establecer límites de:

- seguridad;
- latencia;
- errores;
- coste;
- calidad mínima.

---

# Experiment Duration

Deberá definirse por:

- volumen;
- significancia;
- estacionalidad;
- riesgo.

---

# No experimentar con seguridad

No deberán realizarse variantes que relajen controles de acceso.

---

# Experiment Result

```yaml
experiment_result:
  experiment: IDX-EXPERIMENT-000041

  winner: B

  confidence: 0.96

  metrics:
    successful_search_rate:
      A: 0.82
      B: 0.87
```

---

# Feature Flags

Podrán controlar capacidades relacionadas con índices.

---

# Ejemplos

```text
use_new_vector_index
enable_graph_expansion
enable_new_synonym_set
enable_parent_child_retrieval
```

---

# Requisitos

Toda flag deberá tener:

- owner;
- estado;
- ambiente;
- fecha de expiración;
- rollback;
- auditoría.

---

# No flags permanentes

Las flags de migración deberán retirarse.

---

# Index Capability Status

El Indexing Engine deberá exponer el estado de sus capacidades.

---

# Endpoint conceptual

```text
GET /api/v1/index-capabilities
```

---

# Response

```json
{
  "snapshot": "IDX-SNAP-20260801-0001",
  "capabilities": {
    "lexicalSearch": {
      "status": "available"
    },
    "vectorSearch": {
      "status": "degraded",
      "reason": "high_latency"
    },
    "graphPaths": {
      "status": "unavailable"
    }
  }
}
```

---

# Estados de capacidad

```text
available
degraded
unavailable
updating
disabled
unknown
```

---

# Degradación explícita

El Retrieval Engine deberá conocer si una capacidad está:

- deshabilitada;
- degradada;
- incompleta.

---

# Observabilidad avanzada

La operación productiva deberá disponer de observabilidad continua.

---

# Dimensiones

```text
availability
latency
throughput
quality
freshness
coverage
security
cost
capacity
drift
```

---

# Métricas de disponibilidad

- successful queries;
- failed queries;
- timeout rate;
- index availability;
- partition availability.

---

# Métricas de latencia

- p50;
- p95;
- p99;
- por índice;
- por query type;
- por tenant;
- por filtro.

---

# Métricas de throughput

- queries per second;
- entries indexed per second;
- concurrent queries;
- batch throughput.

---

# Métricas de calidad

- zero-result rate;
- click-through;
- recall de canaries;
- citation success;
- relevance feedback;
- RAG grounding rate.

---

# Métricas de frescura

- index lag;
- stale entries;
- delayed invalidations;
- latest source snapshot;
- active snapshot age.

---

# Métricas de cobertura

- eligible resources;
- indexed resources;
- chunks;
- embeddings;
- citations;
- graph nodes.

---

# Métricas de seguridad

- denied retrievals;
- tenant mismatch attempts;
- ACL failures;
- security drift;
- forbidden result count;
- deleted resource hits.

---

# Métricas de coste

- storage;
- memory;
- CPU;
- query cost;
- vector cost;
- embedding cost;
- cost per 1,000 queries.

---

# Métricas de capacidad

- partition saturation;
- storage utilization;
- memory utilization;
- queue depth;
- concurrency;
- replica load.

---

# Dashboard

Deberán existir dashboards por:

- operación;
- calidad;
- seguridad;
- publicación;
- capacidad;
- coste.

---

# Indexing Operations Dashboard

Deberá mostrar:

- snapshot activo;
- Release Candidate;
- builds;
- lag;
- failures;
- activaciones;
- rollbacks.

---

# Retrieval Quality Dashboard

Deberá mostrar:

- Golden Queries;
- zero results;
- relevance;
- citation accuracy;
- regresiones;
- segmentos afectados.

---

# Security Dashboard

Deberá mostrar:

- violations;
- ACL mismatches;
- tenant isolation;
- deletions pendientes;
- security drift.

---

# Publication Dashboard

Deberá mostrar:

- rollout stage;
- tráfico por versión;
- baseline;
- canary;
- rollback status;
- estabilización.

---

# Capacity Dashboard

Deberá mostrar:

- almacenamiento;
- CPU;
- memoria;
- latencia;
- particiones;
- réplicas;
- forecast.

---

# SLI

Los **Service Level Indicators** deberán medir la operación real.

---

# SLI iniciales

```text
query_success_rate
query_latency
index_freshness
citation_resolution_rate
security_correctness
snapshot_activation_success
```

---

# Query Success Rate

```text
successful_valid_queries
/
total_valid_queries
```

---

# Index Freshness

```text
queries_served_by_current_snapshot
/
total_queries
```

o mediante lag temporal.

---

# Citation Resolution Rate

```text
successfully_resolved_citations
/
requested_citations
```

---

# Security Correctness

Deberá medirse mediante tests y eventos.

Objetivo:

```text
100%
```

---

# SLO

Un **Service Level Objective** establece el objetivo esperado.

---

# Ejemplo

```yaml
indexing_slos:
  lexical_query_availability:
    target: 99.9%

  vector_query_p95_latency:
    target: PT0.2S

  normal_change_freshness:
    target: PT5M

  security_change_freshness:
    target: PT30S

  citation_resolution:
    target: 99.99%

  forbidden_result_rate:
    target: 0
```

---

# SLO por capacidad

No todas las capacidades deberán tener el mismo objetivo.

---

# Ejemplo

```text
Lexical Search
99.9%

Graph Path Search
99.0%

Preview Search
95.0%
```

---

# Error Budget

El Error Budget permitirá gobernar la velocidad de cambios.

---

# Uso

Si se consume el presupuesto:

- pausar promociones;
- reducir experimentos;
- priorizar estabilidad;
- ejecutar revisión.

---

# Quality Budget

Además del Error Budget podrá existir un presupuesto de regresión de calidad.

---

# Ejemplo

```text
No más de 1% de caída relativa en nDCG semanal.
```

---

# Alertas

Las alertas deberán ser accionables.

---

# Alertas críticas

- forbidden result detected;
- tenant isolation failure;
- deleted resource returned;
- active snapshot corrupted;
- activation inconsistent;
- rollback unavailable.

---

# Alertas altas

- p95 latency fuera de SLO;
- index lag crítico;
- citation failures;
- vector partition unavailable;
- canary regression.

---

# Alertas medias

- storage forecast;
- increased zero-result rate;
- stale preview;
- rising cost;
- low cache hit.

---

# Alert Fatigue

Deberán evitarse alertas:

- redundantes;
- no accionables;
- sin owner;
- sin runbook.

---

# Alert Record

```yaml
index_alert:
  id: IDX-ALERT-000041

  severity: critical
  code: FORBIDDEN_RESULT_DETECTED

  snapshot:
    id: IDX-SNAP-20260801-0001

  status: open

  owner:
    team: security
```

---

# Runbook

Toda alerta relevante deberá enlazar con un procedimiento.

---

# Runbook ID

Formato recomendado:

```text
IDX-RUNBOOK-XXXXXX
```

---

# Contenido

- síntoma;
- impacto;
- diagnóstico;
- mitigación;
- rollback;
- escalado;
- verificación.

---

# Capacity Planning

El Indexing Engine deberá anticipar necesidades de recursos.

---

# Factores

- crecimiento documental;
- número de chunks;
- dimensión vectorial;
- réplicas;
- consultas;
- tenants;
- retención;
- snapshots.

---

# Capacity Model

```yaml
capacity_model:
  current:
    documents: 129
    chunks: 12450
    vectors: 12450
    storage_gb: 2.8

  forecast:
    period: P180D
    documents: 1000
    chunks: 95000
    storage_gb: 24
```

---

# Forecasting

Podrá utilizar:

- crecimiento histórico;
- roadmap;
- carga esperada;
- escenarios.

---

# Headroom

Deberá mantenerse capacidad adicional.

---

# Scaling Strategies

```text
vertical
horizontal
partitioning
replication
sharding
caching
tiering
```

---

# Vertical Scaling

Aumenta recursos de una instancia.

---

# Horizontal Scaling

Añade nodos o réplicas.

---

# Partitioning

Distribuye datos.

---

# Replication

Aumenta disponibilidad y lectura.

---

# Caching

Reduce carga repetida.

---

# Storage Tiering

Mueve snapshots históricos a almacenamiento más económico.

---

# Hot, Warm and Cold

Podrán existir niveles:

```text
hot
warm
cold
archive
```

---

# Hot

Snapshot activo y consultas frecuentes.

---

# Warm

Rollback y snapshots recientes.

---

# Cold

Históricos poco consultados.

---

# Archive

Retención de auditoría.

---

# Capacity Gate

Antes de publicar deberá comprobarse capacidad suficiente.

---

# Contrato

```yaml
capacity_check:
  release_candidate: IDX-RC-000041

  estimated:
    storage_growth_gb: 3.2
    memory_growth_gb: 1.1
    query_load_growth: 0.08

  available:
    storage_headroom_gb: 20
    memory_headroom_gb: 8

  status: passed
```

---

# Performance Testing

Deberá realizarse con carga representativa.

---

# Tipos

```text
load
stress
soak
spike
scalability
failover
```

---

# Load Test

Verifica carga esperada.

---

# Stress Test

Determina límites.

---

# Soak Test

Detecta degradación prolongada.

---

# Spike Test

Evalúa picos.

---

# Failover Test

Evalúa pérdida de nodo o partición.

---

# Performance Test Result

```yaml
performance_test_result:
  id: IDX-PERF-RESULT-000041

  release_candidate: IDX-RC-000041

  load:
    queries_per_second: 100

  latency:
    p50_ms: 42
    p95_ms: 110
    p99_ms: 180

  error_rate: 0.0002

  status: passed
```

---

# APIs administrativas

La operación productiva podrá exponerse mediante APIs restringidas.

---

# Release Candidates

```text
POST /api/v1/index-release-candidates
GET  /api/v1/index-release-candidates
GET  /api/v1/index-release-candidates/{releaseCandidateId}
```

---

# Promotion Requests

```text
POST /api/v1/index-promotion-requests
GET  /api/v1/index-promotion-requests/{promotionRequestId}
POST /api/v1/index-promotion-requests/{promotionRequestId}/approve
POST /api/v1/index-promotion-requests/{promotionRequestId}/reject
```

---

# Publications

```text
POST /api/v1/index-publications
GET  /api/v1/index-publications/{publicationId}
POST /api/v1/index-publications/{publicationId}/pause
POST /api/v1/index-publications/{publicationId}/resume
POST /api/v1/index-publications/{publicationId}/rollback
```

---

# Evaluations

```text
POST /api/v1/index-evaluations
GET  /api/v1/index-evaluations/{evaluationId}
```

---

# Benchmarks

```text
GET /api/v1/index-benchmark-suites
GET /api/v1/index-benchmark-results/{resultId}
```

---

# Experiments

```text
POST /api/v1/index-experiments
GET  /api/v1/index-experiments/{experimentId}
POST /api/v1/index-experiments/{experimentId}/stop
```

---

# Capability Status

```text
GET /api/v1/index-capabilities
GET /api/v1/index-capabilities/{capabilityId}
```

---

# Operational Status

```text
GET /api/v1/index-status
GET /api/v1/index-snapshots/active
```

---

# Dry-Run

La promoción deberá soportar dry-run.

---

# Ejemplo

```http
POST /api/v1/index-promotion-requests?dryRun=true
```

---

# Dry-Run Result

```yaml
promotion_dry_run:
  release_candidate: IDX-RC-000041

  compatible_consumers:
    - RAG-ENGINE
    - SEARCH-API

  blockers: []

  estimated_rollout:
    duration: PT2H

  rollback:
    available: true
```

---

# Permisos administrativos

```text
index.release_candidate.create
index.release_candidate.read
index.evaluate.execute
index.promotion.request
index.promotion.approve
index.publish
index.rollout.pause
index.rollout.resume
index.rollback
index.experiment.manage
index.capability.read
index.incident.manage
```

---

# Seguridad operacional

La publicación deberá utilizar identidades limitadas.

---

# Service Principals

Podrán existir:

```text
index-builder
index-validator
index-promoter
index-router
index-monitor
```

---

# Permisos separados

El `index-builder` no deberá poder modificar el alias productivo.

---

# Activación privilegiada

Podrá requerir:

- MFA;
- step-up authentication;
- approval;
- change ticket;
- maintenance window.

---

# Secrets

Las credenciales de:

- motores;
- brokers;
- providers;
- storage;
- KMS;

deberán gestionarse mediante Secret Manager.

---

# No secreto en manifests

---

# Network Security

Los índices internos deberán limitar acceso por:

- red;
- identidad;
- mTLS;
- policy.

---

# Administrative API Protection

Deberá incluir:

- autenticación fuerte;
- autorización por recurso;
- rate limits;
- auditoría;
- protección CSRF cuando proceda;
- allowlist opcional.

---

# Audit

Toda operación relevante deberá auditarse.

---

# Eventos auditables

- creación de Release Candidate;
- aprobación;
- waiver;
- publicación;
- pause;
- resume;
- rollout expansion;
- rollback;
- experimento;
- cambio de flag;
- cambio de SLO;
- cambio de alerta.

---

# Audit Record

```yaml
index_audit_event:
  id: IDX-AUDIT-000041

  action: index_snapshot_publish

  actor:
    id: USER-0001
    type: user

  target:
    id: IDX-SNAP-20260801-0001
    type: index-snapshot

  result: succeeded

  environment: production

  occurred_at: 2026-08-01T22:00:00Z
```

---

# Evidencia de decisión

La auditoría deberá enlazar con:

- Promotion Request;
- approvals;
- Gates;
- Release Candidate;
- rollback.

---

# Incident Management

Un incidente del Indexing Engine representa una degradación de:

- disponibilidad;
- seguridad;
- calidad;
- frescura;
- integridad;
- coste.

---

# Incident Categories

```text
availability
latency
quality
security
freshness
corruption
capacity
cost
publication
```

---

# Incident Record

```yaml
index_incident:
  id: IDX-INCIDENT-000041

  severity: SEV-2
  category: retrieval_quality

  status: mitigating

  affected_snapshot:
    id: IDX-SNAP-20260801-0001

  started_at: 2026-08-01T22:30:00Z
```

---

# Estados

```text
detected
triaging
mitigating
monitoring
resolved
closed
```

---

# Severidades

```text
SEV-1
SEV-2
SEV-3
SEV-4
```

---

# SEV-1

Ejemplos:

- exposición entre tenants;
- datos eliminados recuperables;
- indisponibilidad total;
- corrupción irreversible.

---

# SEV-2

Ejemplos:

- regresión grave de calidad;
- alta latencia general;
- pérdida de componente obligatorio.

---

# SEV-3

Ejemplos:

- degradación parcial;
- un tenant afectado;
- retraso de indexación.

---

# SEV-4

Ejemplos:

- problema menor;
- warning operacional;
- desviación sin impacto inmediato.

---

# Incident Response

```text
Detect
↓
Classify
↓
Contain
↓
Mitigate
↓
Recover
↓
Validate
↓
Review
```

---

# Containment

Podrá incluir:

- desactivar capability;
- revertir;
- bloquear tenant;
- detener rollout;
- invalidar snapshot.

---

# Quality Incident

Podrá mitigarse mediante:

- rollback;
- desactivar vector search;
- usar lexical fallback;
- cambiar ranking profile.

---

# Security Incident

Deberá priorizar:

- bloqueo;
- invalidación;
- revocación;
- auditoría;
- preservación de evidencia.

---

# Incident Timeline

Deberá conservar todos los eventos relevantes.

---

# Postmortem

Los incidentes relevantes deberán generar:

- causa;
- impacto;
- detección;
- respuesta;
- mejoras;
- acciones.

---

# No culpa individual

El análisis deberá centrarse en el sistema.

---

# Operational Runbooks

Deberán existir para:

- activación;
- rollback;
- componente degradado;
- lag alto;
- snapshot corrupto;
- drift;
- tenant isolation;
- vector index unavailable;
- citation failure;
- storage saturation.

---

# Disaster Recovery

El Indexing Engine deberá poder recuperarse ante pérdida de infraestructura.

---

# Elementos recuperables

- manifests;
- schemas;
- profiles;
- snapshots;
- aliases;
- Vector Spaces;
- registries;
- audit records.

---

# Reconstrucción desde fuentes canónicas

Los índices deberán poder reconstruirse sin depender exclusivamente de backups físicos.

---

# Backup

Aun siendo reconstruibles, podrán mantenerse backups para reducir RTO.

---

# RTO y RPO

```yaml
index_disaster_recovery:
  production_search:
    rto: PT4H
    rpo: PT15M

  security_metadata:
    rto: PT30M
    rpo: PT1M
```

---

# Diferenciación

Los metadatos de seguridad podrán requerir objetivos más estrictos que el contenido derivado.

---

# Recovery Strategies

```text
restore_snapshot
rebuild_from_canonical
activate_replica
promote_dr_environment
hybrid_recovery
```

---

# Restore Snapshot

Restaura un snapshot físico.

---

# Rebuild from Canonical

Reconstruye desde fuentes.

---

# Activate Replica

Promueve una réplica.

---

# DR Environment Promotion

Activa el ambiente de recuperación.

---

# Hybrid Recovery

Restaura una base y aplica catch-up.

---

# Recovery Validation

Antes de reabrir tráfico deberá comprobarse:

- seguridad;
- cobertura;
- coherencia;
- citas;
- frescura;
- aliases.

---

# Recovery Drill

Deberán realizarse simulacros periódicos.

---

# Recovery Drill Result

```yaml
recovery_drill:
  id: IDX-DRILL-000041

  scenario: total_vector_index_loss

  recovery_strategy: rebuild_from_canonical

  measured_rto: PT2H20M
  measured_rpo: PT5M

  status: passed
```

---

# Business Continuity

Cuando un componente no esté disponible, el sistema podrá degradarse.

---

# Degradation Matrix

```yaml
degradation_policy:
  vector_unavailable:
    fallback:
      - lexical
      - structured

    response_status: degraded

  graph_unavailable:
    fallback:
      - entity
      - statement
```

---

# No fallback engañoso

El consumidor deberá conocer que el resultado utiliza una capacidad reducida.

---

# Capability Degradation Event

```text
index_capability_degraded
```

---

# Readiness

El Indexing Engine deberá exponer health checks.

---

# Endpoints internos

```text
/health/live
/health/ready
/health/startup
```

---

# Readiness Conditions

Podrán incluir:

- active snapshot resolved;
- required components reachable;
- security filters available;
- routing valid.

---

# No información sensible pública

---

# Component Readiness

Podrá declararse por componente.

---

# Ejemplo

```json
{
  "status": "degraded",
  "components": {
    "lexical": "ready",
    "vector": "unavailable",
    "citation": "ready"
  }
}
```

---

# Publication Events

Catálogo inicial:

```text
index_release_candidate_created
index_release_candidate_rejected
index_release_candidate_approved
index_promotion_requested
index_promotion_approved
index_promotion_rejected
index_publication_started
index_staging_published
index_canary_started
index_rollout_expanded
index_rollout_paused
index_rollout_resumed
index_publication_completed
index_publication_failed
index_publication_rolled_back
index_capability_degraded
index_capability_restored
index_slo_breached
index_incident_created
```

---

# Evento de canary

```yaml
event:
  type: index_canary_started

  subject:
    id: IDX-PUBLICATION-000041
    type: index-publication

  data:
    candidate_snapshot: IDX-SNAP-20260801-0001
    baseline_snapshot: IDX-SNAP-20260725-0003
    traffic_percentage: 1
```

---

# Evento de rollout expandido

```yaml
event:
  type: index_rollout_expanded

  subject:
    id: IDX-PUBLICATION-000041
    type: index-publication

  data:
    previous_percentage: 10
    current_percentage: 50
```

---

# Evento de SLO breached

```yaml
event:
  type: index_slo_breached

  subject:
    id: IDX-CAP-VECTOR-SEARCH
    type: index-capability

  data:
    slo: vector_query_p95_latency
    target_ms: 200
    actual_ms: 420
```

---

# Quality Gates globales

---

# Gate de Release Candidate

```yaml
quality_gate:
  id: QG-INDEX-RELEASE-CANDIDATE-0001

  criteria:
    all:
      - candidate_snapshot_ready == true
      - manifests_complete == true
      - checksums_valid == true
      - schemas_registered == true
      - lineage_complete == true
      - rollback_defined == true
```

---

# Gate de calidad

```yaml
quality_gate:
  id: QG-INDEX-QUALITY-0001

  criteria:
    all:
      - recall_at_10 >= 0.85
      - ndcg_at_10 >= 0.80
      - citation_accuracy == 1.0
      - critical_segment_regressions == 0
      - zero_result_regression == false
```

---

# Gate de seguridad

```yaml
quality_gate:
  id: QG-INDEX-SECURITY-0001

  criteria:
    all:
      - tenant_isolation_failures == 0
      - forbidden_results == 0
      - deleted_resource_hits == 0
      - security_metadata_mismatches == 0
      - secret_exposure_findings == 0
```

---

# Gate de rendimiento

```yaml
quality_gate:
  id: QG-INDEX-PERFORMANCE-0001

  criteria:
    all:
      - p95_latency_ms <= 200
      - error_rate <= 0.001
      - capacity_headroom >= 0.25
      - build_duration_within_budget == true
```

---

# Gate de operación

```yaml
quality_gate:
  id: QG-INDEX-OPERATIONAL-0001

  criteria:
    all:
      - dashboards_available == true
      - alerts_configured == true
      - runbooks_available == true
      - on_call_owner_defined == true
      - rollback_tested == true
      - disaster_recovery_validated == true
```

---

# Gate de publicación

```yaml
quality_gate:
  id: QG-INDEX-PUBLICATION-0001

  criteria:
    all:
      - release_candidate_gate == passed
      - quality_gate == passed
      - security_gate == passed
      - performance_gate == passed
      - operational_gate == passed
      - approvals_complete == true
```

---

# Gate de estabilización

```yaml
quality_gate:
  id: QG-INDEX-STABILIZATION-0001

  criteria:
    all:
      - error_rate_within_slo == true
      - latency_within_slo == true
      - security_incidents == 0
      - quality_regression == false
      - rollback_signals == 0
```

---

# Publication Completion

La publicación se considerará completada cuando:

- el rollout alcance el objetivo;
- termine la estabilización;
- los Gates permanezcan aprobados;
- no existan incidentes bloqueantes;
- el snapshot anterior entre en retención.

---

# Post-Publication Review

Podrá analizar:

- métricas;
- desviaciones;
- costes;
- duración;
- incidentes;
- mejoras.

---

# Publication Report

```yaml
publication_report:
  id: IDX-PUBLICATION-REPORT-000041

  publication: IDX-PUBLICATION-000041

  rollout:
    started_at: 2026-08-01T22:00:00Z
    completed_at: 2026-08-02T01:00:00Z

  outcome: succeeded

  metrics:
    error_rate: 0.0003
    p95_latency_ms: 145
    quality_regression: false

  rollback_used: false
```

---

# Estado de capacidad productiva

Cada capacidad deberá declarar:

- snapshot;
- versión;
- estado;
- SLO;
- owner;
- dependencias.

---

# Capability Record

```yaml
index_capability:
  id: IDX-CAP-VECTOR-SEARCH

  version: 2.0.0

  status: available

  active_snapshot:
    id: IDX-SNAP-20260801-0001

  owner:
    team: ai-platform

  slo:
    availability: 99.9
    p95_latency_ms: 200
```

---

# Perfiles operativos

---

# Perfil mínimo

Incluye:

- publicación manual;
- staging;
- Quality Gate;
- alias atómico;
- rollback;
- logs;
- métricas.

---

# Perfil estructurado

Añade:

- Release Candidates;
- Promotion Pipeline;
- benchmarks;
- dashboards;
- alertas;
- canary;
- SLOs.

---

# Perfil RAG

Añade:

- citation metrics;
- grounding metrics;
- query benchmarks;
- vector quality;
- hybrid evaluation.

---

# Perfil GraphRAG

Añade:

- graph path evaluation;
- subgraph coverage;
- multihop benchmarks;
- graph capability status.

---

# Perfil agentic

Añade:

- tool capability discovery;
- agent-specific evaluation;
- policy-aware retrieval;
- action tracing.

---

# Perfil enterprise

Añade:

- multi-region;
- DR;
- progressive routing;
- SLOs avanzados;
- governance;
- compliance;
- federated approval.

---

# Implementación inicial recomendada

La primera implementación podrá seguir:

```text
Candidate Snapshot
        ↓
Manual Validation
        ↓
Golden Query Suite
        ↓
Security Checks
        ↓
Staging Publication
        ↓
Manual Approval
        ↓
Atomic Alias Switch
        ↓
Monitoring
        ↓
Manual Rollback
```

---

# Segunda iteración

Añadirá:

```text
Release Candidate
+
Promotion Pipeline
+
Automated Quality Gates
+
Canary
+
Stabilization Window
```

---

# Tercera iteración

Añadirá:

```text
A/B Retrieval
+
Progressive Rollout
+
SLOs
+
Automatic Rollback
+
Capacity Forecasting
```

---

# No será necesario inicialmente

- multi-region active-active;
- learned online ranking;
- fully autonomous promotion;
- complex interleaving experiments;
- continuous automatic model routing;
- global federated indexes;
- self-healing production changes;
- zero-human approval for high-risk releases.

---

# Casos de uso

---

# Caso de uso 1 — Release Candidate estándar

Un nuevo snapshot supera:

- consistencia;
- benchmark;
- seguridad;
- staging.

Se aprueba y publica con rollout progresivo.

---

# Caso de uso 2 — Regresión offline

El candidato mejora recall general, pero empeora consultas de alérgenos.

El Quality Gate falla.

No se publica.

---

# Caso de uso 3 — Canary con latencia alta

El 1% del tráfico utiliza el nuevo índice.

La latencia p95 supera el límite.

El rollout se pausa y se revierte.

---

# Caso de uso 4 — Security failure

Una Golden Query recupera un recurso de otro tenant.

El candidato queda bloqueado inmediatamente.

No se admite waiver.

---

# Caso de uso 5 — A/B de embeddings

Dos Vector Spaces se comparan con tráfico controlado.

La variante B mejora calidad sin superar coste ni latencia.

Se promueve.

---

# Caso de uso 6 — Publicación de emergencia

Se necesita retirar un recurso sensible.

Se crea un candidato mínimo con:

- tombstone;
- security validation;
- rollback seguro.

Se utiliza promoción de emergencia.

---

# Caso de uso 7 — Capability degradada

El Vector Index queda indisponible.

El sistema activa búsqueda lexical y structured.

La respuesta se marca como degradada.

---

# Caso de uso 8 — Rollback durante estabilización

El índice nuevo produce aumento de zero results.

Se reactiva el anterior, preservando eliminaciones y ACL recientes.

---

# Caso de uso 9 — SLO breach

El índice permanece disponible, pero supera la latencia objetivo.

Se genera alerta, se abre incidente y se limita el rollout.

---

# Caso de uso 10 — Capacity shortage

El análisis previo detecta que el nuevo Vector Space agotaría memoria.

El Promotion Gate bloquea la publicación.

---

# Caso de uso 11 — Disaster Recovery

Se pierde el índice productivo.

Se restaura un snapshot reciente y se aplica catch-up desde Change Sets.

---

# Caso de uso 12 — Consumer incompatible

El nuevo schema elimina un campo utilizado por una versión antigua de Retrieval Engine.

La promoción se bloquea hasta migrar el consumidor.

---

# Caso de uso 13 — Shadow success

El candidato recibe tráfico en shadow durante una semana.

Los resultados muestran mejora de nDCG y latencia estable.

Se autoriza canary.

---

# Caso de uso 14 — Publication waiver

Una corrección urgente de seguridad reduce levemente una métrica de relevancia.

Se aprueba un waiver temporal para calidad, nunca para seguridad.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Activar al terminar el build

Construcción y publicación son etapas distintas.

---

## Promover artefactos diferentes entre ambientes

Rompe reproducibilidad.

---

## Reconstruir silenciosamente en producción

Impide verificar qué se publicó.

---

## Aprobar sin baseline

No permite detectar regresiones.

---

## Utilizar solo una métrica media

Oculta fallos por segmento.

---

## Evaluar únicamente Golden Queries sencillas

No representa casos reales.

---

## No incluir consultas negativas

Puede ocultar falsos positivos.

---

## No probar seguridad como retrieval

Los permisos deben probarse sobre resultados reales.

---

## Considerar recall suficiente como calidad total

También importan precisión, ranking y citas.

---

## Canary sin sticky routing

Puede producir experiencias incoherentes.

---

## Canary sin criterios de rollback

Convierte el rollout en una activación manual prolongada.

---

## A/B sin guardrails

Puede exponer variantes defectuosas.

---

## Experimentos con ACL diferentes

Compromete seguridad.

---

## Feature Flags permanentes

Generan deuda.

---

## Cambiar aliases sin Promotion Record

Impide trazabilidad.

---

## Activación completa inmediata para cambios de alto riesgo

Aumenta impacto.

---

## Monitorizar solo errores HTTP

Puede existir degradación semántica sin errores técnicos.

---

## Confundir disponibilidad con calidad

El índice puede responder, pero recuperar mal.

---

## Alertas sin runbook

No facilitan respuesta.

---

## SLOs sin medición

No son operativos.

---

## Dashboards sin owner

Quedan abandonados.

---

## Capacity Planning únicamente tras fallos

Debe anticiparse.

---

## No probar rollback

Un plan no probado puede fallar.

---

## Rollback a un snapshot inseguro

Puede reexponer contenido.

---

## DR basado solo en backups

Los índices deberán poder reconstruirse.

---

## Logs con consultas completas

Puede comprometer privacidad.

---

## Promociones con cuenta compartida

Impiden atribución.

---

## Waivers indefinidos

Convierten excepciones en reglas.

---

## Automatic Promotion sin límites

Puede publicar regresiones.

---

## No fijar ventana de estabilización

Declara éxito demasiado pronto.

---

## Cerrar publicación sin informe

Pierde evidencia operativa.

---

# Reglas mínimas de conformidad

---

## Release Candidate identificado

Todo snapshot propuesto deberá convertirse en un Release Candidate inmutable.

---

## Promotion Request explícita

Toda promoción productiva deberá registrarse.

---

## Artefactos verificables

Los manifests y checksums deberán validarse.

---

## Evaluación offline

Todo candidato deberá superar una Benchmark Suite.

---

## Baseline obligatorio

Deberá compararse con el snapshot activo.

---

## Seguridad sin tolerancia

Los fallos de seguridad deberán bloquear.

---

## Compatibilidad comprobada

Los consumidores conocidos deberán ser compatibles.

---

## Staging

Los cambios relevantes deberán validarse en staging.

---

## Rollout definido

Toda publicación deberá declarar una política.

---

## Rollback preparado

Deberá existir una versión segura y accesible.

---

## Observabilidad previa

Las métricas y alertas deberán existir antes del tráfico.

---

## Estabilización

La publicación deberá incluir una ventana de observación.

---

## Auditoría

Toda decisión deberá atribuirse.

---

## SLO

Las capacidades productivas deberán disponer de objetivos.

---

## Incident Readiness

Deberán existir runbooks y owners.

---

## DR

Los índices críticos deberán poder recuperarse.

---

# Conformidad de Release Candidate

Será conforme cuando:

- tenga ID;
- tenga versión;
- identifique snapshot;
- preserve manifests;
- declare profiles;
- declare schemas;
- declare owner;
- declare rollback;
- sea inmutable.

---

# Conformidad de Promotion Request

Será conforme cuando:

- identifique candidato;
- declare ambiente origen;
- declare destino;
- declare motivo;
- declare rollout;
- incluya evidencia;
- tenga aprobaciones.

---

# Conformidad de Benchmark Suite

Será conforme cuando:

- tenga versión;
- declare datasets;
- declare métricas;
- incluya consultas negativas;
- incluya seguridad;
- preserve resultados;
- permita comparación.

---

# Conformidad de Golden Query

Será conforme cuando:

- tenga identidad;
- declare consulta;
- declare filtros;
- declare expectativas;
- declare tolerancias;
- declare versión.

---

# Conformidad de Rollout Policy

Será conforme cuando:

- declare etapas;
- declare tráfico;
- declare duración;
- declare métricas;
- declare pausas;
- declare rollback.

---

# Conformidad de Publication

Será conforme cuando:

- utilice paquete inmutable;
- verifique checksums;
- preserve snapshot anterior;
- aplique routing controlado;
- genere métricas;
- complete estabilización;
- produzca informe.

---

# Conformidad de Capability

Será conforme cuando:

- tenga ID;
- declare versión;
- declare estado;
- identifique snapshot;
- declare owner;
- declare SLO;
- declare dependencias.

---

# Conformidad de Observabilidad

Será conforme cuando:

- mida disponibilidad;
- mida latencia;
- mida calidad;
- mida frescura;
- mida seguridad;
- mida coste;
- disponga de dashboards;
- disponga de alertas.

---

# Conformidad de Incident Management

Será conforme cuando:

- clasifique severidad;
- identifique owner;
- preserve timeline;
- permita mitigación;
- permita rollback;
- produzca revisión.

---

# Conformidad de Disaster Recovery

Será conforme cuando:

- declare RTO;
- declare RPO;
- preserve artefactos;
- permita reconstrucción;
- pruebe restauración;
- valide seguridad tras recuperación.

---

# Lista de comprobación

Antes de publicar un Index Snapshot deberá comprobarse:

```text
[ ] El Release Candidate está identificado.
[ ] El Release Candidate está congelado.
[ ] Los manifests están completos.
[ ] Los checksums son válidos.
[ ] Los schemas están registrados.
[ ] Los profiles están versionados.
[ ] El snapshot fuente está actualizado.
[ ] El baseline está identificado.
[ ] La Benchmark Suite se ha ejecutado.
[ ] Las Golden Queries han pasado.
[ ] Las consultas negativas han pasado.
[ ] Las Security Queries han pasado.
[ ] No existen forbidden results.
[ ] No existen deleted resource hits.
[ ] La Citation Accuracy cumple el objetivo.
[ ] La regresión por segmentos se ha evaluado.
[ ] El rendimiento cumple los límites.
[ ] La capacidad disponible es suficiente.
[ ] Los consumidores son compatibles.
[ ] El candidato se ha publicado en staging.
[ ] La aceptación de staging ha pasado.
[ ] Los dashboards están disponibles.
[ ] Las alertas están configuradas.
[ ] Los runbooks están disponibles.
[ ] El owner operativo está definido.
[ ] El rollback está preparado.
[ ] El rollback ha sido validado.
[ ] La Rollout Policy está identificada.
[ ] Los criterios de canary están definidos.
[ ] Los triggers de rollback están definidos.
[ ] Las aprobaciones están completas.
[ ] La auditoría está configurada.
[ ] La ventana de estabilización está definida.
[ ] Los SLOs están declarados.
[ ] El plan de incidentes está disponible.
[ ] La recuperación ante desastre está documentada.
[ ] El Quality Gate de publicación ha pasado.
```

---

# Arquitectura final de la Parte VI

```text
Candidate Snapshot
        ↓
Release Candidate
        ↓
Artifact Verification
        ↓
Offline Evaluation
        ├── Golden Queries
        ├── Benchmarks
        ├── Regression Checks
        └── Security Queries
        ↓
Staging Publication
        ↓
Consumer Acceptance
        ↓
Promotion Approval
        ↓
Controlled Rollout
        ├── Shadow
        ├── Canary
        ├── Progressive
        └── Full Traffic
        ↓
Stabilization
        ├── Complete
        ├── Pause
        └── Rollback
        ↓
Active Capability
        ↓
Continuous Observability
        ├── SLI / SLO
        ├── Quality
        ├── Security
        ├── Capacity
        └── Cost
        ↓
Incident Response and Recovery
```

---

# Integración final con el SGCC

El Indexing Engine deberá integrarse con los demás subsistemas mediante contratos explícitos.

---

# Ingestion Engine

Proporcionará:

- Knowledge Packages;
- fuentes;
- snapshots;
- Change Sets.

---

# Validation Engine

Proporcionará:

- diagnósticos;
- Quality Gates;
- validación de contenido;
- validación de artefactos.

---

# Knowledge Graph

Proporcionará:

- entidades;
- Statements;
- relaciones;
- snapshots;
- subgrafos.

---

# Reasoning Engine

Proporcionará inferencias autorizadas y versionadas.

---

# Retrieval Engine

Consumirá:

- Index Suites;
- snapshots;
- capabilities;
- filtros;
- scoring metadata.

---

# Motor RAG

Consumirá resultados recuperables con:

- evidencia;
- Citation Mappings;
- seguridad;
- snapshot;
- lineage.

---

# API Layer

Expondrá:

- estado;
- jobs;
- snapshots;
- promoción;
- publicación;
- capacidad;
- auditoría.

---

# Event Bus

Distribuirá:

- cambios;
- activaciones;
- degradaciones;
- incidentes;
- SLO breaches.

---

# Security Layer

Aplicará:

- identidad;
- autorización;
- tenant;
- clasificación;
- auditoría;
- secretos.

---

# Arquitectura completa del Indexing Engine

```text
Canonical Knowledge
        ↓
Source Resolution
        ↓
Eligibility
        ↓
Change Analysis
        ↓
Indexable Units
        ↓
Chunking
        ↓
Embeddings
        ↓
Index Builders
        ├── Lexical
        ├── Vector
        ├── Structured
        ├── Metadata
        ├── Entity
        ├── Statement
        ├── Citation
        └── Graph
        ↓
Candidate Snapshot
        ↓
Reconciliation
        ↓
Release Candidate
        ↓
Benchmark and Security Evaluation
        ↓
Promotion Pipeline
        ↓
Controlled Rollout
        ↓
Active Index Capability
        ↓
Retrieval Engine
        ↓
RAG · Search · GraphRAG · Agents
```

---

# Modelo de madurez del Indexing Engine

---

# Nivel 0 — Manual

Características:

- build manual;
- índice único;
- sin snapshots;
- activación directa;
- sin métricas de calidad.

---

# Nivel 1 — Reproducible

Características:

- pipeline versionado;
- manifests;
- schemas;
- full rebuild;
- alias lógico.

---

# Nivel 2 — Incremental

Características:

- Change Sets;
- fingerprints;
- invalidación;
- tombstones;
- snapshots incrementales.

---

# Nivel 3 — Gobernado

Características:

- Release Candidates;
- Quality Gates;
- Promotion Pipeline;
- auditoría;
- rollback.

---

# Nivel 4 — Observable

Características:

- dashboards;
- alertas;
- SLI;
- SLO;
- drift;
- reconciliación.

---

# Nivel 5 — Progressive

Características:

- shadow;
- canary;
- progressive rollout;
- A/B retrieval;
- automatic rollback.

---

# Nivel 6 — Resilient Enterprise

Características:

- multi-tenant;
- multi-region;
- DR;
- capacity planning;
- governance;
- policy engine;
- compliance.

---

# Objetivo inicial

Para una primera implementación práctica se recomienda alcanzar:

```text
Nivel 2
```

con elementos de:

```text
Nivel 3
```

---

# Roadmap recomendado

---

# Fase 1 — Índice reproducible

- documentos publicados;
- parsing;
- Lexical Index;
- Metadata Index;
- Citation Index;
- snapshots;
- alias activo.

---

# Fase 2 — RAG inicial

- chunking;
- embeddings;
- Vector Index;
- Hybrid Suite;
- Golden Queries;
- Quality Gate.

---

# Fase 3 — Incrementalidad

- Change Sets;
- fingerprints;
- invalidación;
- tombstones;
- reconciliación.

---

# Fase 4 — Publicación gobernada

- Release Candidates;
- Promotion Requests;
- staging;
- approvals;
- rollback.

---

# Fase 5 — Operación avanzada

- canary;
- progressive rollout;
- SLOs;
- dashboards;
- incident management.

---

# Fase 6 — GraphRAG

- Entity Index;
- Statement Index;
- Graph Index;
- Path Index;
- graph benchmarks.

---

# Fase 7 — Enterprise

- multi-tenancy;
- DR;
- capacity forecasting;
- multi-region;
- compliance.

---

# Estado de madurez de la especificación

| Área | Estado |
|---|---|
| Fundamentos | Completo |
| Arquitectura | Completa |
| Pipeline | Completo |
| Unidades indexables | Completas |
| Chunking | Completo |
| Embeddings | Completo |
| Lexical Index | Completo |
| Vector Index | Completo |
| Structured Index | Completo |
| Metadata Index | Completo |
| Entity Index | Completo |
| Statement Index | Completo |
| Citation Index | Completo |
| Graph Index | Completo |
| Incremental Indexing | Completo |
| Invalidación | Completa |
| Tombstones | Completos |
| Full Rebuild | Completo |
| Migraciones | Completas |
| Snapshots | Completos |
| Activación | Completa |
| Rollback | Completo |
| Reconciliación | Completa |
| Retención y GC | Completas |
| Release Candidates | Completos |
| Promotion Pipeline | Completo |
| Evaluación | Completa |
| Rollout | Completo |
| Observabilidad | Completa |
| SLI y SLO | Completos |
| Seguridad operacional | Completa |
| Incidentes | Completos |
| Disaster Recovery | Completo |
| Roadmap | Completo |

---

# Especificaciones derivadas recomendadas

A partir de este documento podrán desarrollarse:

```text
ESPECIFICACION_DE_CHUNKING.md
ESPECIFICACION_DE_EMBEDDINGS.md
ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md
ESPECIFICACION_DE_INDICES_VECTORIALES.md
ESPECIFICACION_DE_INDICES_DE_GRAFO.md
ESPECIFICACION_DE_EVALUACION_RAG.md
ESPECIFICACION_DE_PUBLICACION_DE_INDICES.md
ESPECIFICACION_DE_OBSERVABILIDAD_DE_INDICES.md
```

---

# Antipatrones finales

El Indexing Engine no deberá convertirse en:

```text
Un script que vuelca documentos en una base vectorial.
```

Tampoco deberá operar como:

```text
Una segunda fuente canónica de conocimiento.
```

No deberá publicar índices únicamente porque:

```text
El proceso terminó sin errores técnicos.
```

No deberá confundir:

```text
Disponibilidad
```

con:

```text
Calidad.
```

No deberá considerar que una alta similitud vectorial implica:

```text
Verdad factual.
```

No deberá permitir que una activación sea una operación opaca sin:

- manifest;
- Gate;
- baseline;
- rollout;
- rollback;
- auditoría.

No deberá mantener snapshots activos sin poder responder:

```text
¿Qué conocimiento representan?

¿Qué modelos utilizaron?

¿Qué Quality Gates superaron?

¿Qué consumidores los utilizan?

¿Qué SLO ofrecen?

¿Cómo se revierten?
```

---

# Reglas finales de conformidad del Indexing Engine

El Indexing Engine completo será conforme cuando:

- todos los índices sean derivados;
- todas las fuentes canónicas estén identificadas;
- todos los pipelines estén versionados;
- todas las unidades conserven puntero canónico;
- todos los chunks preserven citas;
- todos los embeddings identifiquen modelo y Vector Space;
- todos los builders estén versionados;
- todos los schemas estén registrados;
- todos los snapshots sean inmutables;
- toda indexación incremental declare baseline y target;
- toda eliminación genere invalidación o tombstone;
- todo cambio de seguridad se propague con prioridad;
- toda suite preserve consistencia entre componentes;
- todo Release Candidate sea inmutable;
- toda promoción pase Quality Gates;
- toda publicación utilice rollout gobernado;
- toda activación preserve rollback;
- toda capacidad productiva tenga owner;
- toda capacidad crítica tenga SLO;
- toda operación relevante sea auditable;
- toda divergencia pueda detectarse mediante reconciliación;
- todo incidente disponga de respuesta;
- todo índice pueda reconstruirse desde fuentes canónicas;
- toda recuperación valide seguridad y consistencia.

---

# Transición hacia la siguiente especificación

Con esta sexta parte queda completada:

```text
ESPECIFICACION_DEL_INDEXING_ENGINE.md
```

NovaCoquinaria dispone ahora de una definición formal para:

- seleccionar conocimiento;
- generar unidades indexables;
- construir chunks;
- generar embeddings;
- construir índices;
- mantenerlos actualizados;
- invalidarlos;
- reconstruirlos;
- migrarlos;
- versionarlos;
- evaluarlos;
- publicarlos;
- observarlos;
- operarlos;
- recuperarlos.

La siguiente especificación recomendada será:

```text
ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md
```

El Retrieval Engine deberá desarrollar:

- Query Understanding;
- Query Normalization;
- Query Classification;
- Retrieval Plans;
- Lexical Retrieval;
- Vector Retrieval;
- Structured Retrieval;
- Graph Retrieval;
- Hybrid Retrieval;
- Candidate Generation;
- Filtering;
- Security Trimming;
- Score Normalization;
- Fusion;
- Re-ranking;
- Diversification;
- Evidence Selection;
- Citation Resolution;
- Context Expansion;
- Retrieval Evaluation;
- APIs;
- eventos;
- observabilidad;
- Quality Gates.

El Indexing Engine prepara las estructuras recuperables.

El Retrieval Engine decidirá cómo consultarlas y combinar sus resultados.

---

# Conclusión

El Indexing Engine constituye la infraestructura que transforma conocimiento canónico en capacidades de recuperación operables.

Su ciclo completo puede resumirse así:

```text
Resolver fuentes
        ↓
Extraer unidades
        ↓
Segmentar
        ↓
Generar chunks
        ↓
Generar embeddings
        ↓
Construir índices
        ↓
Crear snapshot
        ↓
Detectar cambios
        ↓
Invalidar
        ↓
Reconstruir
        ↓
Evaluar
        ↓
Promover
        ↓
Publicar
        ↓
Observar
        ↓
Revertir o consolidar
```

Las fuentes determinan qué conocimiento se representa.

Las unidades preservan estructura y procedencia.

Los chunks adaptan el contenido a retrieval.

Los embeddings aportan representación semántica.

Los builders generan índices especializados.

Los snapshots preservan coherencia.

La indexación incremental mantiene actualidad.

Las invalidaciones impiden servir conocimiento obsoleto.

Los tombstones evitan resurrecciones.

La reconciliación detecta drift.

Los Release Candidates congelan artefactos publicables.

Los benchmarks miden calidad.

Los Quality Gates bloquean regresiones.

El rollout progresivo reduce impacto.

La estabilización confirma el comportamiento.

Los SLOs convierten la capacidad en un servicio operable.

Los incidentes y el rollback permiten responder ante fallos.

La recuperación garantiza continuidad.

Un Indexing Engine completo deberá poder responder:

```text
¿Qué conocimiento está indexado?

¿De qué snapshots procede?

¿Qué pipeline lo procesó?

¿Qué chunks se generaron?

¿Qué modelo creó los embeddings?

¿Qué índices forman la suite?

¿Qué cambios se aplicaron?

¿Qué Release Candidate se publicó?

¿Qué evaluación superó?

¿Qué snapshot está activo?

¿Qué SLO ofrece?

¿Cómo se revierte?

¿Cómo se reconstruye?
```

Con esta sexta parte queda completada la **Especificación del Indexing Engine de NovaCoquinaria**, estableciendo el sistema mediante el que el conocimiento validado se transforma en índices seguros, trazables, versionados, evaluados, publicables y operables para búsqueda, Retrieval, RAG, GraphRAG y agentes inteligentes.
