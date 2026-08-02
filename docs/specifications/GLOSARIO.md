---
id: SPEC-GLOSARIO
tipo: especificacion
titulo: Glosario de las especificaciones de NovaCoquinaria
version: 1.0.0
estado: borrador
ultima_revision: 2026-08-02
tags:
  - specifications
  - glossary
  - terminology
  - architecture
  - governance
---

# Glosario de las especificaciones de NovaCoquinaria

---

# Parte I — Fundamentos, principios terminológicos y vocabulario del conocimiento

---

# Introducción

Las especificaciones de NovaCoquinaria utilizan un vocabulario técnico común que constituye la base de toda la arquitectura documental.

Este glosario tiene como finalidad establecer el significado preciso de los términos empleados a lo largo de las especificaciones para garantizar:

- consistencia terminológica;
- ausencia de ambigüedad;
- interoperabilidad documental;
- trazabilidad conceptual;
- comprensión compartida entre personas y herramientas.

Este documento no pretende sustituir las especificaciones individuales.

Cada especificación continúa siendo la autoridad sobre los conceptos de su dominio.

El glosario únicamente proporciona una referencia centralizada y uniforme.

---

# Objetivos

Este documento persigue los siguientes objetivos:

- definir el vocabulario oficial;
- evitar sinónimos ambiguos;
- unificar la terminología;
- facilitar la lectura de las especificaciones;
- servir como referencia para futuras implementaciones;
- apoyar la validación documental;
- facilitar la incorporación de nuevos colaboradores;
- servir como base para futuras ontologías y diccionarios semánticos.

---

# Alcance

El glosario cubre exclusivamente la terminología utilizada dentro del ecosistema documental de NovaCoquinaria.

No pretende definir:

- conceptos culinarios;
- técnicas de cocina;
- ingredientes;
- recetas;
- modelos de IA externos;
- tecnologías concretas;
- APIs de terceros.

---

# Organización

Los términos se agrupan por dominios arquitectónicos.

Cada entrada incluye, cuando corresponda:

- definición;
- contexto;
- documento propietario;
- sinónimos admitidos;
- términos relacionados;
- observaciones.

---

# Formato de una entrada

Las entradas seguirán el siguiente esquema conceptual.

```yaml
termino:
  nombre:
  categoria:
  definicion:
  propietario:
  sinonimos:
  relacionados:
  observaciones:
```

---

# Convenciones generales

---

## Definición única

Cada término tendrá una definición principal.

---

## Documento propietario

Cada concepto pertenecerá a una especificación concreta.

El glosario nunca sustituirá dicha autoridad.

---

## Terminología estable

Los nombres deberán permanecer estables siempre que sea posible.

Los cambios importantes requerirán actualización coordinada.

---

## Evitar ambigüedad

Cuando un término tenga varios significados deberán utilizarse nombres específicos.

Ejemplo:

```text
Execution Context
```

deberá especializarse según corresponda.

---

# Categorías terminológicas

Los términos se clasifican en las siguientes categorías.

| Categoría | Descripción |
|------------|-------------|
| Arquitectura | Conceptos generales del sistema |
| Conocimiento | Modelo semántico |
| Runtime | Motores de ejecución |
| Interfaces | Contratos públicos |
| Gobernanza | Calidad y validación |
| Infraestructura | Componentes técnicos |

---

# Dominio de conocimiento

Esta primera parte recoge la terminología relacionada con el modelo de conocimiento del SGCC.

---

# Ontología

## Definición

Modelo formal que define las entidades, conceptos, atributos y relaciones del dominio culinario.

## Documento propietario

```text
ESPECIFICACION_DE_ONTOLOGIA.md
```

## Sinónimos admitidos

Ninguno.

## Relacionados

- Knowledge Graph
- Relación
- Componente

## Observaciones

Toda la semántica del sistema se apoya en la Ontología.

---

# Documento

## Definición

Unidad documental básica gestionada por el SGCC.

Representa cualquier elemento persistente del conocimiento.

## Documento propietario

```text
ESPECIFICACION_DE_DOCUMENTOS.md
```

## Relacionados

- Front Matter
- Componente
- Colección

---

# Front Matter

## Definición

Bloque YAML inicial que identifica un documento y contiene sus metadatos.

## Documento propietario

```text
ESPECIFICACION_DE_DOCUMENTOS.md
```

## Campos habituales

- id
- tipo
- titulo
- version
- estado
- ultima_revision
- tags

---

# Identificador documental

## Definición

Valor único que identifica un documento dentro del SGCC.

## Documento propietario

Documentos.

## Observaciones

Nunca deberá duplicarse.

---

# Componente

## Definición

Unidad reutilizable de conocimiento utilizada para construir documentos más complejos.

## Documento propietario

```text
ESPECIFICACION_DE_COMPONENTES.md
```

## Ejemplos

- técnica;
- ingrediente;
- utensilio;
- plantilla.

---

# Relación

## Definición

Vínculo semántico existente entre dos entidades del modelo de conocimiento.

## Documento propietario

```text
ESPECIFICACION_DE_RELACIONES.md
```

## Ejemplos

```text
usa
contiene
deriva_de
requiere
sustituye
```

---

# Colección

## Definición

Agrupación lógica de documentos o componentes.

Puede ser:

- estática;
- dinámica;
- virtual.

## Documento propietario

```text
ESPECIFICACION_DE_COLECCIONES.md
```

---

# Knowledge Graph

## Definición

Representación en forma de grafo del conocimiento gestionado por el sistema.

## Documento propietario

```text
ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md
```

## Elementos

- nodos;
- aristas;
- propiedades;
- metadatos.

---

# Nodo

## Definición

Entidad individual del Knowledge Graph.

---

# Arista

## Definición

Relación existente entre dos nodos.

---

# Propiedad

## Definición

Atributo asociado a un nodo o a una arista.

---

# Entidad

## Definición

Elemento del dominio susceptible de ser representado dentro del grafo.

---

# Clase

## Definición

Categoría ontológica a la que pertenece una entidad.

---

# Instancia

## Definición

Representación concreta de una clase.

---

# Esquema

## Definición

Conjunto de reglas que definen la estructura del modelo de conocimiento.

---

# Modelo semántico

## Definición

Organización conceptual de los elementos del dominio.

---

# Vocabulario controlado

## Definición

Conjunto limitado y autorizado de términos empleados por el sistema.

---

# Taxonomía

## Definición

Clasificación jerárquica de conceptos.

---

# Ontología aplicada

## Definición

Uso operativo de la ontología dentro del SGCC.

---

# Semántica

## Definición

Significado formal asociado a los conceptos del sistema.

---

# Concepto

## Definición

Idea abstracta representada dentro del modelo de conocimiento.

---

# Atributo

## Definición

Característica asociada a un concepto o entidad.

---

# Valor

## Definición

Contenido concreto de un atributo.

---

# Dominio

## Definición

Conjunto de conceptos pertenecientes a un mismo ámbito funcional.

---

# Bounded Context

## Definición

Límite dentro del cual un modelo mantiene un significado consistente.

---

# Modelo canónico

## Definición

Representación oficial utilizada como referencia por todo el sistema.

---

# Fuente de verdad (Source of Truth)

## Definición

Documento considerado autoritativo para un concepto determinado.

---

# Authority Map

## Definición

Relación entre conceptos y sus documentos propietarios.

---

# Trazabilidad

## Definición

Capacidad para seguir el origen y evolución de un elemento del conocimiento.

---

# Provenance

## Definición

Información que describe el origen y las transformaciones sufridas por un dato.

---

# Evidencia

## Definición

Información utilizada para justificar una afirmación o resultado.

---

# Statement

## Definición

Afirmación estructurada sobre el conocimiento del dominio.

---

# Claim

## Definición

Proposición susceptible de ser verificada mediante evidencia.

---

# Inferencia

## Definición

Conclusión obtenida a partir de reglas y conocimiento existente.

---

# Regla

## Definición

Condición formal utilizada para validar o inferir conocimiento.

---

# Restricción

## Definición

Limitación impuesta por el modelo semántico o por una especificación.

---

# Invariante

## Definición

Condición que debe cumplirse siempre.

---

# Snapshot

## Definición

Representación consistente del estado de un conjunto de conocimiento en un instante determinado.

---

# Versionado

## Definición

Gestión de la evolución controlada de documentos y conceptos.

---

# Compatibilidad

## Definición

Capacidad de una versión para coexistir con otra sin producir incompatibilidades.

---

# Breaking Change

## Definición

Cambio que rompe la compatibilidad con versiones anteriores.

---

# Deprecation

## Definición

Proceso mediante el cual un elemento deja de recomendarse antes de su retirada.

---

# Retirement

## Definición

Retirada definitiva de un elemento previamente deprecado.

---

# Consumidor

## Definición

Documento o componente que utiliza un concepto definido por otro.

---

# Proveedor

## Definición

Documento responsable de definir un concepto utilizado por otros.

---

# Dependencia

## Definición

Relación mediante la cual un documento necesita conceptos definidos por otro.

---

# Dependencia crítica

## Definición

Dependencia cuya modificación puede afectar significativamente a documentos consumidores.

---

# Radio de impacto

## Definición

Nivel de propagación esperado tras una modificación.

---

# Gobernanza documental

## Definición

Conjunto de normas que regulan la evolución del conocimiento documentado.

---

# Estado de esta parte

Con esta primera parte quedan definidos:

- los principios terminológicos;
- el formato de las entradas;
- las categorías generales;
- el vocabulario del modelo de conocimiento;
- los conceptos de gobernanza documental;
- la terminología fundamental empleada por las especificaciones.

---

# Transición hacia la Parte II

La Parte II desarrollará el vocabulario correspondiente al Runtime de NovaCoquinaria, incluyendo:

- Engines;
- Engine Registry;
- Ingesta;
- Indexing;
- Retrieval;
- Razonador;
- Motor RAG;
- Workflows;
- Execution Context;
- Candidate Set;
- Evidence Set;
- Grounding;
- Citation;
- demás conceptos operacionales.

---

# Parte II — Vocabulario del Runtime, ejecución, recuperación, razonamiento y generación aumentada

---

# Introducción

La Parte I ha definido:

- los principios terminológicos;
- el formato de las entradas;
- el vocabulario del conocimiento;
- los conceptos de autoridad;
- la trazabilidad;
- el versionado;
- la gobernanza documental.

Esta Parte II desarrolla el vocabulario correspondiente al Runtime de NovaCoquinaria.

El Runtime comprende los componentes responsables de:

- incorporar conocimiento;
- validarlo;
- indexarlo;
- recuperarlo;
- razonarlo;
- generar respuestas;
- coordinar ejecuciones;
- registrar capacidades;
- controlar estados;
- aplicar políticas operativas.

---

# Runtime

## Definición

Conjunto de componentes responsables de ejecutar procesos operativos sobre el conocimiento gestionado por NovaCoquinaria.

## Documento propietario

Conjunto de especificaciones del dominio `runtime`.

## Relacionados

- Engine
- Execution
- Workflow
- Orquestador
- Engine Registry

---

# Engine

## Definición

Componente ejecutable que proporciona una o varias capacidades operativas dentro del Runtime.

## Documento propietario

```text
ESPECIFICACION_DEL_ENGINE_REGISTRY.md
```

## Ejemplos

- Validation Engine;
- Indexing Engine;
- Retrieval Engine;
- Reasoning Engine;
- RAG Engine.

## Observaciones

El término `Engine` deberá utilizarse para componentes con:

- responsabilidad ejecutable;
- contrato;
- operaciones;
- capacidades;
- lifecycle;
- disponibilidad.

---

# Engine Definition

## Definición

Descripción declarativa de un Engine, sus capacidades, contratos, versiones y requisitos.

## Documento propietario

Engine Registry.

---

# Engine Instance

## Definición

Instancia concreta y disponible de un Engine Definition.

## Documento propietario

Engine Registry.

## Relacionados

- Provider
- Health
- Availability
- Routing

---

# Engine Registry

## Definición

Catálogo y plano de control responsable de registrar, descubrir y seleccionar Engines.

## Documento propietario

```text
ESPECIFICACION_DEL_ENGINE_REGISTRY.md
```

## Responsabilidades

- registro;
- descubrimiento;
- resolución;
- matching;
- routing;
- health;
- disponibilidad;
- lifecycle.

---

# Capability

## Definición

Funcionalidad declarada que un Engine puede ofrecer.

## Documento propietario

Engine Registry.

## Ejemplos

```text
hybrid_retrieval
semantic_validation
grounded_generation
graph_reasoning
```

## Observaciones

Una Capability no equivale a un endpoint ni a una implementación concreta.

---

# Operation

## Definición

Acción ejecutable expuesta por un Engine o contrato operativo.

## Documento propietario

Engine Registry, salvo operaciones específicas definidas por cada Engine.

---

# Provider

## Definición

Entidad técnica o lógica que suministra una implementación concreta de un Engine o modelo.

## Documento propietario

Engine Registry.

## Observaciones

No deberá confundirse con `Proveedor` en el sentido documental.

---

# Engine Contract

## Definición

Contrato que define las entradas, salidas, errores, restricciones y capacidades de un Engine.

## Documento propietario

Engine Registry.

---

# Engine Matching

## Definición

Proceso mediante el cual se seleccionan Engines compatibles con una necesidad o Capability.

---

# Routing

## Definición

Proceso de selección de una Engine Instance concreta para ejecutar una operación.

---

# Routing Candidate

## Definición

Engine Instance potencialmente apta para una ejecución.

---

# Health

## Definición

Estado técnico de una instancia o dependencia.

## Valores habituales

```text
healthy
degraded
unhealthy
unknown
```

---

# Availability

## Definición

Capacidad actual de un Engine para aceptar y ejecutar trabajo.

---

# Runtime State

## Definición

Estado operativo de un componente o ejecución dentro del Runtime.

---

# Ingesta

## Definición

Proceso mediante el cual una fuente de información se incorpora al SGCC.

## Documento propietario

```text
ESPECIFICACION_DE_INGESTA.md
```

## Relacionados

- Source
- Connector
- Parsing
- Normalización
- Staging
- Reingesta

---

# Source

## Definición

Origen interno o externo del conocimiento que será incorporado.

---

# Connector

## Definición

Componente responsable de acceder a una Source y extraer información.

---

# Acquisition

## Definición

Proceso de obtención inicial del contenido desde una Source.

---

# Parsing

## Definición

Transformación de contenido de entrada en una representación estructurada.

---

# Extraction

## Definición

Identificación de datos, entidades, metadatos o relaciones dentro del contenido.

---

# Normalización

## Definición

Transformación de datos de entrada al modelo canónico del SGCC.

---

# Deduplicación

## Definición

Proceso de detección y tratamiento de contenidos equivalentes o repetidos.

---

# Staging

## Definición

Área o estado temporal donde el contenido permanece antes de su publicación definitiva.

---

# Quarantine

## Definición

Estado de aislamiento aplicado a contenido que no cumple requisitos o requiere revisión.

---

# Reingesta

## Definición

Nueva ejecución del pipeline de ingesta sobre una fuente previamente procesada.

---

# Idempotencia de ingesta

## Definición

Propiedad que garantiza que repetir una misma ingesta no genera resultados duplicados no deseados.

---

# Lineage

## Definición

Registro de las transformaciones y estados por los que ha pasado una unidad de conocimiento.

---

# Validation

## Definición

Proceso mediante el cual se comprueba que un artefacto cumple reglas estructurales, semánticas, contractuales u operativas.

## Documento propietario

```text
ESPECIFICACION_DE_VALIDACION.md
```

---

# Validation Engine

## Definición

Engine responsable de ejecutar reglas de validación.

---

# Validation Rule

## Definición

Regla verificable que determina si una condición se cumple.

---

# Validation Result

## Definición

Resultado producido tras ejecutar una o varias validaciones.

---

# Validation Context

## Definición

Información necesaria para ejecutar una validación concreta.

---

# Diagnostic

## Definición

Resultado estructurado que describe un problema, advertencia o condición detectada.

## Documento propietario

Validación.

---

# Diagnostic Code

## Definición

Código estable y legible por máquina que identifica un diagnóstico.

---

# Severity

## Definición

Nivel de importancia asociado a un diagnóstico.

## Valores recomendados

```text
info
warning
error
critical
```

---

# Retryable

## Definición

Propiedad que indica si una operación fallida puede reintentarse razonablemente.

---

# Quality Gate

## Definición

Conjunto de criterios que debe cumplirse para permitir una transición, publicación, despliegue o aceptación.

## Documento propietario

Validación.

---

# Gate Result

## Definición

Resultado de la evaluación de un Quality Gate.

---

# Indexing

## Definición

Proceso mediante el cual el conocimiento canónico se transforma en estructuras optimizadas para recuperación.

## Documento propietario

```text
ESPECIFICACION_DEL_INDEXING_ENGINE.md
```

---

# Indexing Engine

## Definición

Engine responsable de crear, actualizar y retirar índices.

---

# Index

## Definición

Estructura optimizada para localizar conocimiento.

---

# Search Index

## Definición

Índice orientado a búsquedas lexicales, semánticas, estructuradas o híbridas.

---

# Vector Index

## Definición

Índice que almacena representaciones vectoriales y permite búsquedas por similitud.

---

# Lexical Index

## Definición

Índice basado en términos, tokens o estructuras textuales.

---

# Hybrid Index

## Definición

Configuración que combina varios tipos de índice para recuperación híbrida.

---

# Chunk

## Definición

Unidad fragmentada de contenido preparada para indexación y recuperación.

## Documento propietario

Indexing Engine.

---

# Chunking

## Definición

Proceso de división de contenido en Chunks.

---

# Chunk Boundary

## Definición

Límite estructural o semántico utilizado para determinar dónde comienza y termina un Chunk.

---

# Embedding

## Definición

Representación vectorial de un contenido, entidad o consulta.

---

# Embedding Model

## Definición

Modelo utilizado para generar embeddings.

---

# Index Snapshot

## Definición

Representación consistente y versionada del estado de uno o varios índices.

## Documento propietario

Indexing Engine.

---

# Indexing Job

## Definición

Ejecución concreta de una operación de indexación.

---

# Reindexación

## Definición

Proceso de reconstrucción parcial o completa de índices existentes.

---

# Index Freshness

## Definición

Grado de actualización de un índice respecto al conocimiento canónico.

---

# Retrieval

## Definición

Proceso de recuperación de conocimiento relevante para una consulta o necesidad.

## Documento propietario

```text
ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md
```

---

# Retrieval Engine

## Definición

Engine responsable de interpretar consultas, ejecutar estrategias de recuperación, fusionar candidatos y seleccionar evidencia.

---

# Retrieval Query

## Definición

Representación normalizada de una necesidad de recuperación.

---

# Query Understanding

## Definición

Proceso de interpretación de una consulta antes de ejecutar Retrieval.

## Puede incluir

- normalización;
- detección de idioma;
- detección de intención;
- extracción de entidades;
- expansión;
- desambiguación.

---

# Query Expansion

## Definición

Proceso de ampliación de una consulta mediante términos relacionados, sinónimos o entidades.

---

# Query Decomposition

## Definición

División de una consulta compleja en subconsultas.

---

# Retrieval Strategy

## Definición

Método o combinación de métodos utilizados para recuperar conocimiento.

## Valores habituales

```text
lexical
semantic
hybrid
graph
structured
metadata
```

---

# Retrieval Plan

## Definición

Plan declarativo que describe cómo se ejecutará una operación de Retrieval.

## Documento propietario

Retrieval Engine.

## Puede incluir

- estrategias;
- filtros;
- Executors;
- prioridades;
- timeouts;
- fusión;
- ranking;
- fallbacks.

---

# Retrieval Executor

## Definición

Componente responsable de ejecutar una parte concreta de un Retrieval Plan.

---

# Retrieval Execution

## Definición

Ejecución concreta de un Retrieval Plan.

---

# Retrieval Execution Context

## Definición

Contexto operativo utilizado durante una Retrieval Execution.

## Observaciones

No deberá confundirse con Workflow Execution Context ni con RagContext.

---

# Retrieval Candidate

## Definición

Resultado potencial recuperado antes de la selección final.

---

# Candidate Record

## Definición

Representación estructurada de un Retrieval Candidate.

---

# Candidate Set

## Definición

Conjunto de candidatos producidos por uno o varios Retrieval Executors.

## Documento propietario

Retrieval Engine.

---

# Candidate Fusion

## Definición

Proceso de combinación de Candidate Sets procedentes de distintas estrategias.

---

# Score

## Definición

Valor asociado a un candidato que representa relevancia, similitud u otra medida.

---

# Score Normalization

## Definición

Transformación de scores heterogéneos a una escala comparable.

---

# Ranking

## Definición

Proceso de ordenación inicial de candidatos.

---

# Re-ranking

## Definición

Segunda fase de ordenación que utiliza señales adicionales para mejorar la relevancia.

---

# Reciprocal Rank Fusion

## Definición

Método de combinación de rankings procedentes de varias estrategias de recuperación.

---

# Diversity

## Definición

Propiedad que evita que los resultados seleccionados sean excesivamente similares.

---

# Deduplication

## Definición

Eliminación o consolidación de candidatos duplicados o equivalentes.

---

# Retrieval Filter

## Definición

Restricción aplicada para limitar los resultados recuperables.

---

# Metadata Filter

## Definición

Filtro basado en atributos estructurados.

---

# Graph Retrieval

## Definición

Recuperación basada en nodos, relaciones, rutas o subgrafos del Knowledge Graph.

---

# Semantic Retrieval

## Definición

Recuperación basada en similitud semántica.

---

# Lexical Retrieval

## Definición

Recuperación basada en coincidencia de términos o estructuras textuales.

---

# Hybrid Retrieval

## Definición

Recuperación que combina estrategias lexicales, semánticas, estructuradas o de grafo.

---

# Evidence Record

## Definición

Representación estructurada de una evidencia seleccionada.

---

# Evidence Set

## Definición

Conjunto de evidencias seleccionadas y trazables que respaldan una operación posterior.

## Documento propietario

Retrieval Engine.

## Consumidores habituales

- Motor RAG;
- Razonador;
- Validación;
- APIs.

---

# Retrieval Result

## Definición

Resultado final producido por una Retrieval Execution.

---

# Retrieval Explanation

## Definición

Representación que explica cómo se obtuvo y ordenó un resultado.

---

# Explainability

## Definición

Capacidad de reconstruir y comunicar el proceso de Retrieval.

---

# Retrieval Provenance

## Definición

Información que permite rastrear cada resultado hasta su fuente, índice, snapshot y transformación.

---

# Razonador

## Definición

Componente responsable de aplicar reglas, restricciones e inferencias sobre conocimiento y evidencia.

## Documento propietario

```text
ESPECIFICACION_DEL_RAZONADOR.md
```

---

# Reasoning Engine

## Definición

Engine responsable de ejecutar procesos de razonamiento.

---

# Reasoning Request

## Definición

Solicitud estructurada que inicia una operación de razonamiento.

---

# Reasoning Context

## Definición

Conjunto de conocimiento, reglas, evidencias y restricciones disponibles para una ejecución de razonamiento.

---

# Reasoning Result

## Definición

Resultado producido por una operación de razonamiento.

---

# Rule Engine

## Definición

Componente especializado en aplicar reglas declarativas.

---

# Deduction

## Definición

Inferencia obtenida mediante aplicación lógica de reglas.

---

# Constraint Resolution

## Definición

Proceso de evaluación y resolución de restricciones compatibles o conflictivas.

---

# Derived Statement

## Definición

Statement generado mediante inferencia.

---

# Explanation Trace

## Definición

Secuencia trazable de reglas, evidencias y pasos que justifican una conclusión.

---

# Confidence de razonamiento

## Definición

Medida gobernada asociada a una conclusión inferida.

## Observaciones

No deberá confundirse con la autoconfianza expresada por un modelo.

---

# RAG

## Definición

Arquitectura de generación aumentada mediante recuperación.

Corresponde a:

```text
Retrieval-Augmented Generation
```

## Documento propietario

```text
ESPECIFICACION_DEL_MOTOR_RAG.md
```

---

# Motor RAG

## Definición

Engine responsable de transformar consultas y evidencia recuperada en respuestas fundamentadas.

---

# RagQuery

## Definición

Solicitud estructurada dirigida al Motor RAG.

## Documento propietario

Motor RAG.

---

# RagExecution

## Definición

Ejecución concreta del pipeline RAG.

---

# RagContext

## Definición

Contexto ensamblado para una RagExecution.

## Observaciones

No equivale a Evidence Set.

El Evidence Set contiene fuentes seleccionadas.

El RagContext contiene la representación efectiva preparada para generación.

---

# Context Assembly

## Definición

Proceso de selección, ordenación, compresión y ensamblado de evidencia para construir un RagContext.

---

# Context Budget

## Definición

Límite de tokens o capacidad disponible para contexto.

---

# Context Compression

## Definición

Proceso de reducción del contexto preservando hechos y provenance.

---

# Prompt Assembly

## Definición

Proceso de construcción de la entrada efectiva enviada al modelo de generación.

---

# Prompt Template

## Definición

Plantilla versionada utilizada durante Prompt Assembly.

---

# Prompt Fingerprint

## Definición

Hash o identificador de la representación efectiva de un prompt.

---

# Grounding

## Definición

Propiedad que exige que las afirmaciones relevantes de una respuesta estén respaldadas por evidencia.

## Documento propietario

Motor RAG.

---

# Grounding Mode

## Definición

Nivel de exigencia de respaldo aplicado a una RagExecution.

## Valores habituales

```text
none
preferred
required
strict
```

---

# Grounding Report

## Definición

Resultado estructurado de la evaluación de Grounding.

---

# Grounded Claim Ratio

## Definición

Proporción de Claims respaldados respecto al total evaluado.

---

# Citation

## Definición

Referencia que vincula una parte de la respuesta con una fuente o evidencia concreta.

## Documento propietario

Motor RAG.

---

# Citation Validation

## Definición

Proceso que comprueba existencia, permisos, ubicación y alineación semántica de una Citation.

---

# Citation Status

## Definición

Estado de validación de una Citation.

## Valores habituales

```text
verified
partially_verified
unverified
invalid
stale
restricted
```

---

# Citation Span

## Definición

Rango de texto de una respuesta respaldado por una Citation.

---

# RagResponse

## Definición

Resultado final producido por una RagExecution.

---

# No-Answer

## Definición

Resultado válido mediante el cual el Motor RAG se abstiene de responder por falta de evidencia, contradicción o política.

---

# Completeness

## Definición

Grado en que una RagResponse cubre los aspectos de la consulta.

---

# Structured Output

## Definición

Respuesta generada conforme a un schema estructurado.

---

# Response Validation

## Definición

Proceso de validación final de una RagResponse.

---

# Generation Profile

## Definición

Conjunto gobernado de parámetros y políticas de generación.

---

# Logical Model

## Definición

Referencia abstracta a una capacidad de modelo sin acoplarse directamente a un proveedor concreto.

---

# Model Selection

## Definición

Proceso mediante el cual se elige un Logical Model o una implementación compatible.

---

# Fallback Model

## Definición

Modelo alternativo utilizado cuando el preferente no está disponible.

---

# Generation Parameters

## Definición

Parámetros que controlan el comportamiento del modelo de generación.

## Ejemplos

- temperature;
- topP;
- maximumOutputTokens;
- stopSequences;
- seed.

---

# Tool

## Definición

Capacidad invocable por un Engine o agente durante una ejecución.

---

# Tool Call

## Definición

Solicitud estructurada para ejecutar una Tool.

---

# Side Effect

## Definición

Modificación observable producida por una operación.

---

# Guardrail

## Definición

Control aplicado a input, contexto, ejecución, Tools u output para preservar seguridad y conformidad.

---

# Prompt Injection

## Definición

Intento de introducir instrucciones maliciosas o no autorizadas dentro del flujo de generación.

---

# Hallucination

## Definición

Contenido generado que no está respaldado o es incompatible con el conocimiento disponible.

## Observaciones

El término deberá utilizarse con precisión.

No toda respuesta incompleta es una alucinación.

---

# Workflow

## Definición

Definición declarativa de una secuencia o grafo de actividades ejecutables.

## Documento propietario

```text
ESPECIFICACION_DEL_ORQUESTADOR_DE_EJECUCION.md
```

---

# Workflow Definition

## Definición

Representación versionada de un Workflow.

---

# Workflow Execution

## Definición

Ejecución concreta de un Workflow Definition.

---

# Orquestador de Ejecución

## Definición

Componente responsable de coordinar Workflows, Jobs, Activities, estados, retries, señales y compensaciones.

---

# Job

## Definición

Unidad de trabajo gestionada por el Orquestador.

---

# Activity

## Definición

Paso ejecutable de un Workflow.

## Documento propietario

Orquestador de Ejecución.

---

# Step

## Definición

Unidad lógica de un Workflow.

## Observaciones

Cuando `Step` y `Activity` tengan semánticas distintas deberán definirse expresamente.

No deberán utilizarse como sinónimos automáticamente.

---

# Task

## Definición

Unidad concreta de trabajo asignable o ejecutable dentro de un Job o Activity.

## Observaciones

Deberá especializarse si coexisten distintos tipos de Task.

---

# DAG

## Definición

Grafo dirigido acíclico utilizado para representar dependencias entre Steps o Activities.

---

# Scheduler

## Definición

Componente responsable de determinar cuándo una unidad de trabajo puede ejecutarse.

---

# Worker

## Definición

Proceso o instancia responsable de ejecutar trabajo asignado.

---

# Worker Pool

## Definición

Conjunto de Workers gestionados como una unidad.

---

# Workflow Execution Context

## Definición

Contexto operativo asociado a una Workflow Execution.

## Observaciones

No deberá confundirse con Retrieval Execution Context.

---

# Retry

## Definición

Nuevo intento de ejecución tras un fallo retryable.

---

# Backoff

## Definición

Espera progresiva aplicada entre retries.

---

# Jitter

## Definición

Variación aleatoria añadida al Backoff para evitar reintentos sincronizados.

---

# Timeout

## Definición

Tiempo máximo permitido para una operación.

---

# Deadline

## Definición

Instante límite absoluto antes del cual una operación debe completarse.

---

# Cancellation

## Definición

Solicitud para detener una ejecución en curso.

---

# Compensation

## Definición

Operación utilizada para contrarrestar efectos de una ejecución previa.

---

# Signal

## Definición

Mensaje dirigido a una ejecución activa para modificar su comportamiento.

---

# Event

## Definición

Hecho ocurrido y publicado para consumo posterior.

---

# Timer

## Definición

Mecanismo que activa una operación tras un intervalo o en un instante determinado.

---

# Recovery

## Definición

Proceso mediante el cual una ejecución interrumpida recupera un estado consistente.

---

# Checkpoint

## Definición

Estado persistido que permite reanudar una ejecución.

---

# Partial Result

## Definición

Resultado incompleto producido antes de finalizar una ejecución o tras una degradación.

---

# Degraded Mode

## Definición

Modo operativo en el que el sistema mantiene capacidad reducida y declarada.

---

# Circuit Breaker

## Definición

Patrón que detiene temporalmente llamadas a una dependencia inestable.

---

# Estado de esta parte

Con esta segunda parte quedan definidos:

- los conceptos fundamentales del Runtime;
- la terminología de Engines y Engine Registry;
- la Ingesta;
- la Validación;
- el Indexing Engine;
- el Retrieval Engine;
- el Razonador;
- el Motor RAG;
- el Orquestador;
- los principales contratos operativos;
- las diferencias entre Candidate Set, Evidence Set y RagContext;
- las distintas especializaciones de Execution Context;
- el vocabulario de retries, compensaciones y recuperación.

---

# Transición hacia la Parte III

La Parte III cerrará el glosario mediante el vocabulario de interfaces, conversación y gobernanza, incluyendo:

- API;
- Endpoint;
- Contract;
- Request;
- Response;
- Problem Details;
- Event Envelope;
- Webhook;
- Callback;
- Conversation;
- Session;
- Turn;
- Message;
- Memory;
- Streaming;
- términos ambiguos;
- términos desaconsejados;
- sinónimos admitidos;
- reglas para incorporar nuevos términos;
- Quality Gates;
- checklist;
- referencias y conformidad global.

---

# Parte III — Interfaces, conversación, términos ambiguos, gobernanza terminológica y conformidad global

---

# Introducción

Las Partes I y II han definido:

- los principios terminológicos;
- el vocabulario del conocimiento;
- la autoridad documental;
- la trazabilidad;
- la terminología de Engines;
- la Ingesta;
- la Validación;
- la Indexación;
- el Retrieval;
- el Razonador;
- el Motor RAG;
- el Orquestador;
- los conceptos de ejecución y recuperación.

Esta Parte III completa el glosario mediante los términos relacionados con:

- interfaces;
- APIs;
- contratos;
- asincronía;
- eventos;
- conversación;
- memoria;
- streaming;
- seguridad;
- observabilidad;
- gobernanza terminológica;
- conformidad documental.

También establece:

- diferencias entre términos próximos;
- sinónimos admitidos;
- términos desaconsejados;
- reglas para incorporar nuevos conceptos;
- Quality Gates terminológicos;
- checklist de mantenimiento.

---

# Dominio de interfaces

---

# API

## Definición

Interfaz programática mediante la cual un consumidor accede a capacidades del SGCC.

## Documento propietario

```text
ESPECIFICACION_DE_APIS.md
```

## Observaciones

Una API expone capacidades.

No deberá convertirse en propietaria del modelo de dominio que representa.

---

# API Family

## Definición

Conjunto coherente de operaciones y recursos pertenecientes a un mismo ámbito funcional.

## Ejemplos

```text
Retrieval API
RAG API
Conversation API
Validation API
Ingestion API
```

---

# Endpoint

## Definición

Punto concreto de acceso a una operación de API.

## Ejemplo

```text
POST /api/v1/rag-queries
```

---

# Resource

## Definición

Entidad identificable expuesta mediante una API.

## Ejemplos

- Conversation;
- RagExecution;
- Evidence Set;
- Citation;
- Memory Item.

---

# Resource Identifier

## Definición

Identificador estable de un Resource.

---

# Resource Reference

## Definición

Referencia compacta a un Resource.

## Estructura habitual

```yaml
resource_reference:
  id:
  type:
  href:
  version:
```

---

# URI

## Definición

Identificador utilizado para localizar o referenciar un recurso.

---

# Route

## Definición

Patrón de URL asociado a una operación.

## Observaciones

No deberá utilizarse como sinónimo exacto de Endpoint.

Una Route puede admitir varios métodos HTTP.

---

# Operation ID

## Definición

Identificador estable del tipo de operación expuesta por una API.

## Ejemplos

```text
createRagQuery
retrieveSearch
cancelRagExecution
```

---

# Request

## Definición

Solicitud enviada por un consumidor a una API.

---

# Request Body

## Definición

Contenido estructurado enviado en el cuerpo de una Request.

---

# Request Envelope

## Definición

Conjunto de metadatos comunes asociados a una Request.

## Puede incluir

- Request ID;
- Correlation ID;
- actor;
- tenant;
- tracing;
- preferencias;
- idempotencia.

---

# Request ID

## Definición

Identificador único de una invocación concreta.

---

# Correlation ID

## Definición

Identificador común utilizado para agrupar varias Requests dentro del mismo flujo lógico.

---

# Trace ID

## Definición

Identificador utilizado por Distributed Tracing para correlacionar Spans.

---

# Client Request ID

## Definición

Identificador proporcionado por el consumidor para correlación propia.

## Observaciones

No sustituye al Request ID generado o validado por el servidor.

---

# Response

## Definición

Resultado devuelto por una API tras procesar una Request.

---

# Response Envelope

## Definición

Estructura común que contiene:

- datos;
- metadatos;
- enlaces;
- warnings;
- diagnósticos.

---

# Response Metadata

## Definición

Metadatos asociados a una Response.

## Ejemplos

- API Version;
- Request ID;
- Correlation ID;
- timestamp;
- snapshot;
- duración;
- warnings.

---

# Status Code

## Definición

Código HTTP que representa el resultado general de una operación.

---

# Success Response

## Definición

Response que indica que una operación ha sido procesada conforme a su contrato.

## Observaciones

Una operación puede ser técnicamente correcta y devolver:

```text
no_answer
```

sin considerarse un error.

---

# Error Response

## Definición

Response que representa un fallo técnico, contractual, de seguridad o de dominio.

---

# Problem Details

## Definición

Contrato estructurado utilizado para representar errores HTTP.

## Documento propietario

APIs.

## Campos habituales

- type;
- title;
- status;
- code;
- detail;
- instance;
- requestId;
- retryable.

---

# Error Code

## Definición

Código estable y legible por máquina que identifica un tipo de error.

## Observaciones

No deberá depender del idioma del mensaje.

---

# Warning

## Definición

Condición anómala o degradada que no impide necesariamente utilizar el resultado.

---

# Violation

## Definición

Incumplimiento concreto de una regla de validación.

---

# Retry-After

## Definición

Valor que indica cuándo una operación retryable puede volver a intentarse.

---

# Idempotency Key

## Definición

Clave proporcionada por el consumidor para evitar efectos duplicados al repetir una operación.

---

# Idempotency Record

## Definición

Registro que relaciona:

- Idempotency Key;
- operación;
- actor;
- tenant;
- fingerprint;
- resultado;
- expiración.

---

# Payload Fingerprint

## Definición

Hash canónico utilizado para verificar que una Idempotency Key se reutiliza con el mismo contenido lógico.

---

# ETag

## Definición

Identificador de versión de una representación de Resource.

---

# Precondition

## Definición

Condición que debe cumplirse antes de ejecutar una operación.

## Ejemplos

```text
If-Match
If-None-Match
```

---

# Optimistic Concurrency

## Definición

Estrategia que evita sobrescrituras mediante comparación de versiones o ETags.

---

# Pagination

## Definición

Mecanismo para dividir una colección de resultados en páginas.

---

# Cursor Pagination

## Definición

Paginación basada en un cursor opaco que representa una posición estable dentro de un conjunto ordenado.

---

# Offset Pagination

## Definición

Paginación basada en desplazamiento numérico.

---

# Cursor

## Definición

Token opaco utilizado para continuar una consulta paginada.

---

# Stable Ordering

## Definición

Orden determinista que garantiza consistencia entre páginas.

---

# Sorting

## Definición

Criterio utilizado para ordenar resultados.

---

# Filtering

## Definición

Restricción aplicada para seleccionar únicamente Resources que cumplan determinadas condiciones.

---

# Projection

## Definición

Representación predefinida de un Resource con un subconjunto o nivel específico de detalle.

## Ejemplos

```text
summary
standard
detailed
audit
```

---

# Sparse Fieldset

## Definición

Selección explícita de campos que el consumidor desea recibir.

---

# Expansion

## Definición

Inclusión de Resources relacionados dentro de una Response.

---

# Content Negotiation

## Definición

Proceso mediante el cual cliente y servidor acuerdan:

- formato;
- idioma;
- encoding;
- versión de representación.

---

# Media Type

## Definición

Tipo de contenido utilizado para representar una Request o Response.

## Ejemplos

```text
application/json
application/problem+json
text/event-stream
application/x-ndjson
```

---

# API Version

## Definición

Versión mayor de una familia de API.

## Documento propietario

APIs.

---

# Contract Version

## Definición

Versión de un contrato, schema o Resource concreto.

---

# Backward Compatibility

## Definición

Capacidad de una nueva versión para seguir siendo utilizable por consumidores anteriores.

---

# Forward Compatibility

## Definición

Capacidad de un consumidor para tolerar evoluciones compatibles del proveedor.

---

# Deprecation Header

## Definición

Cabecera que comunica que una API o contrato está deprecated.

---

# Sunset

## Definición

Fecha a partir de la cual una API o contrato dejará de estar disponible.

---

# Migration Guide

## Definición

Documento que describe cómo migrar entre versiones incompatibles.

---

# Contract

## Definición

Acuerdo formal que define:

- entradas;
- salidas;
- estados;
- errores;
- invariantes;
- compatibilidad;
- lifecycle.

---

# Public Contract

## Definición

Contrato consumible fuera del componente que lo define.

---

# Internal Contract

## Definición

Contrato utilizado entre componentes internos.

---

# Schema

## Definición

Definición formal de la estructura válida de un payload o Resource.

---

# JSON Schema

## Definición

Schema expresado mediante el estándar JSON Schema.

---

# OpenAPI

## Definición

Descripción formal de APIs HTTP síncronas.

---

# AsyncAPI

## Definición

Descripción formal de eventos, mensajería y APIs asíncronas.

---

# Consumer

## Definición

Aplicación, servicio, agente o persona que utiliza una API o Contract.

## Observaciones

No deberá confundirse con consumidor documental, aunque ambos comparten la idea de dependencia.

---

# Provider de API

## Definición

Componente responsable de implementar y publicar una API.

## Observaciones

No deberá confundirse con Provider de Engine.

---

# SDK

## Definición

Biblioteca cliente que facilita el consumo de una API.

---

# Callback

## Definición

Invocación realizada por el sistema hacia una URL previamente proporcionada por un consumidor.

---

# Webhook

## Definición

Mecanismo mediante el cual el sistema envía eventos HTTP a un receptor registrado.

## Documento propietario

APIs.

---

# Webhook Subscription

## Definición

Registro que relaciona:

- consumidor;
- endpoint;
- eventos;
- secreto;
- filtros;
- estado.

---

# Delivery Attempt

## Definición

Intento individual de entregar un evento o Webhook.

---

# Delivery Guarantee

## Definición

Semántica de entrega ofrecida por un canal.

## Valores habituales

```text
at_most_once
at_least_once
effectively_once
```

---

# Event

## Definición

Representación inmutable de un hecho ocurrido.

## Observaciones

Un Event describe algo que ya ha sucedido.

No es una orden.

---

# Command

## Definición

Solicitud explícita para que un componente realice una acción.

## Observaciones

No deberá utilizarse como sinónimo de Event.

---

# Event Envelope

## Definición

Estructura común que envuelve un Event.

## Campos habituales

- id;
- type;
- subject;
- source;
- timestamp;
- version;
- correlation;
- data.

---

# Event Type

## Definición

Identificador estable de la clase de hecho representado.

---

# Event Version

## Definición

Versión del contrato de un Event.

---

# Event Subject

## Definición

Resource principal al que se refiere el Event.

---

# Event Source

## Definición

Componente que publica el Event.

---

# Event Consumer

## Definición

Componente que procesa un Event.

---

# Event Producer

## Definición

Componente que crea y publica un Event.

---

# Event Stream

## Definición

Secuencia ordenada de Events relacionados.

---

# Event Ordering

## Definición

Garantía sobre el orden en que se producen o reciben Events.

---

# Sequence Number

## Definición

Número monotónico utilizado para ordenar eventos dentro de un scope determinado.

---

# Replay

## Definición

Reprocesamiento de Events previamente publicados.

---

# Replay Window

## Definición

Periodo durante el cual un Event puede volver a entregarse.

---

# Dead Letter Queue

## Definición

Destino utilizado para almacenar mensajes o Events que no pudieron procesarse correctamente.

---

# Consumer Offset

## Definición

Posición hasta la que un consumidor ha procesado un Event Stream.

---

# Acknowledgement

## Definición

Confirmación de que un mensaje o Event ha sido recibido o procesado.

---

# Streaming

## Definición

Entrega progresiva de datos durante una operación todavía activa.

---

# Server-Sent Events

## Definición

Protocolo HTTP unidireccional utilizado para enviar eventos desde servidor a cliente.

---

# WebSocket

## Definición

Canal bidireccional persistente entre cliente y servidor.

---

# Stream Event

## Definición

Unidad individual emitida dentro de un stream.

---

# Delta

## Definición

Fragmento incremental de una respuesta en construcción.

---

# Heartbeat

## Definición

Evento periódico utilizado para mantener o verificar una conexión activa.

---

# Backpressure

## Definición

Mecanismo utilizado cuando un consumidor procesa datos más lentamente de lo que el productor los genera.

---

# Stream Resume

## Definición

Reanudación de un stream desde el último evento recibido correctamente.

---

# Final Event

## Definición

Evento que declara la finalización de un stream.

---

# Dominio conversacional

---

# Conversation

## Definición

Interacción lógica continuada entre uno o varios participantes y NovaCoquinaria.

## Documento propietario

Motor RAG.

## Observaciones

Puede abarcar varias Sessions y múltiples Turns.

---

# Conversation ID

## Definición

Identificador estable de una Conversation.

---

# Conversation Status

## Definición

Estado del lifecycle de una Conversation.

## Valores habituales

```text
active
paused
archived
expired
deleted
blocked
under_review
```

---

# Participant

## Definición

Actor que interviene en una Conversation.

---

# Participant Role

## Definición

Rol que determina la relación del Participant con una Conversation.

## Ejemplos

```text
owner
member
observer
reviewer
system
```

---

# Conversation Session

## Definición

Ventana temporal y operativa dentro de una Conversation.

## Observaciones

No deberá utilizarse como sinónimo de Conversation.

---

# Session

## Definición

Forma abreviada permitida para `Conversation Session` cuando el contexto sea inequívoco.

---

# Session State

## Definición

Estado operativo de una Conversation Session.

## Valores habituales

```text
starting
active
idle
closing
closed
expired
revoked
blocked
```

---

# Session Expiration

## Definición

Finalización de una Session por:

- inactividad;
- tiempo absoluto;
- expiración de credenciales;
- política;
- revocación.

---

# Session Renewal

## Definición

Extensión autorizada de la vigencia de una Session.

---

# Reauthentication

## Definición

Proceso mediante el cual se exige confirmar de nuevo la identidad o el nivel de autenticación.

---

# Turn

## Definición

Unidad secuencial de interacción dentro de una Conversation.

## Documento propietario

Motor RAG.

---

# Turn Sequence

## Definición

Posición estable de un Turn dentro de una rama conversacional.

---

# Turn State

## Definición

Estado operativo de un Turn.

---

# Message

## Definición

Contenido aportado por un Participant dentro de un Turn.

---

# Message Role

## Definición

Rol semántico asociado a un Message.

## Valores habituales

```text
user
assistant
system
tool
agent
reviewer
```

---

# Conversation History

## Definición

Conjunto de Turns y Messages producidos en una Conversation.

---

# Effective Conversation Context

## Definición

Subconjunto del historial, memoria y estado realmente utilizado para ejecutar un Turn.

---

# Context Carryover

## Definición

Proceso mediante el cual se selecciona información de Turns anteriores para un nuevo Turn.

---

# Conversation Summary

## Definición

Representación derivada y compactada de una parte del historial conversacional.

## Observaciones

No es una fuente primaria.

Debe mantener provenance hacia los Turns originales.

---

# Conversation State

## Definición

Información operativa que describe la situación actual de una Conversation.

## Puede incluir

- tema activo;
- entidades seleccionadas;
- restricciones;
- pregunta pendiente;
- rama;
- locale;
- perfil.

---

# Anaphora Resolution

## Definición

Proceso de resolver referencias como:

```text
esa receta
la segunda opción
hazla sin limón
```

---

# Reference Resolution

## Definición

Proceso general de vincular una expresión con una entidad, Turn, Message o Resource previo.

---

# Ambiguous Reference

## Definición

Referencia que admite varias interpretaciones razonables.

---

# Conversation Branch

## Definición

Línea alternativa de Turns derivada de un punto anterior de una Conversation.

---

# Fork

## Definición

Creación de una nueva Conversation o rama a partir de un Turn existente.

---

# Regeneration

## Definición

Creación de una nueva RagResponse para un Turn existente.

---

# Response Alternative

## Definición

Respuesta adicional asociada al mismo Turn sin sobrescribir respuestas anteriores.

---

# Superseded Response

## Definición

Respuesta que ha sido sustituida como preferida, pero se conserva para trazabilidad.

---

# Memory

## Definición

Información seleccionada para reutilización futura dentro de un scope definido.

## Documento propietario

Motor RAG.

## Observaciones

No deberá confundirse con historial, Conversation Summary ni perfil.

---

# Memory Item

## Definición

Unidad individual de Memory.

---

# Memory Scope

## Definición

Ámbito durante el cual un Memory Item puede aplicarse.

## Valores habituales

```text
turn
session
conversation
persistent
```

---

# Memory Mode

## Definición

Política que determina si la Memory está habilitada y bajo qué condiciones.

## Valores habituales

```text
disabled
turn
session
conversation
persistent
explicit_only
```

---

# Candidate Memory

## Definición

Información inferida que podría convertirse en Memory, pero todavía no ha sido confirmada.

---

# Confirmed Memory

## Definición

Memory Item validado o confirmado conforme a la policy.

---

# Explicit Memory

## Definición

Memory creada a petición expresa del usuario.

---

# Inferred Memory

## Definición

Memory propuesta a partir del comportamiento o contenido observado.

## Observaciones

No deberá persistirse automáticamente como verdad confirmada cuando requiera consentimiento.

---

# Memory Provenance

## Definición

Información que identifica:

- Turn de origen;
- Message;
- actor;
- fecha;
- método de creación;
- confirmación.

---

# Memory Expiration

## Definición

Momento o condición tras la cual un Memory Item deja de aplicarse.

---

# Memory Invalidation

## Definición

Proceso que marca un Memory Item como no válido sin borrar necesariamente su historial.

---

# Memory Conflict

## Definición

Situación en la que dos Memory Items activos contienen información incompatible.

---

# False Memory

## Definición

Información almacenada como Memory que no fue afirmada, confirmada o inferida correctamente.

---

# Profile

## Definición

Conjunto persistente y gobernado de atributos o preferencias asociados a un actor o caso de uso.

## Observaciones

No deberá utilizarse como sinónimo de Memory.

---

# Preference

## Definición

Elección o inclinación declarada o confirmada.

---

# Constraint

## Definición

Restricción aplicable a una operación, Turn, Session o Conversation.

---

# Feedback

## Definición

Valoración o señal proporcionada sobre una Response, Turn, Citation, Engine o resultado.

---

# Rating

## Definición

Valor cuantitativo asociado a Feedback.

---

# Correction Feedback

## Definición

Feedback que propone una corrección concreta.

## Observaciones

No deberá convertirse automáticamente en conocimiento canónico.

---

# Report

## Definición

Feedback que señala:

- riesgo;
- falsedad;
- cita incorrecta;
- fuga de información;
- contenido inseguro;
- comportamiento anómalo.

---

# Seguridad y control de acceso

---

# Authentication

## Definición

Proceso de verificar la identidad de un actor o servicio.

---

# Principal

## Definición

Identidad autenticada que realiza una operación.

---

# Authorization

## Definición

Proceso de decidir si un Principal puede realizar una acción sobre un Resource.

---

# Scope

## Definición

Permiso declarado asociado a un token o identidad.

---

# Resource-Level Authorization

## Definición

Autorización evaluada sobre un Resource concreto.

---

# Field-Level Authorization

## Definición

Autorización que determina qué campos de un Resource puede ver o modificar un Principal.

---

# Tenant

## Definición

Ámbito lógico de aislamiento de datos, configuración, cuotas y seguridad.

---

# Tenant Context

## Definición

Información confiable que identifica el Tenant efectivo de una operación.

---

# Tenant Isolation

## Definición

Garantía de que datos y operaciones de un Tenant no se mezclan con los de otro.

---

# Cross-Tenant Operation

## Definición

Operación autorizada que afecta o consulta más de un Tenant.

---

# Least Privilege

## Definición

Principio que exige conceder únicamente los permisos mínimos necesarios.

---

# Data Classification

## Definición

Nivel de sensibilidad asignado a datos o Resources.

## Valores iniciales

```text
public
internal
confidential
restricted
```

---

# Effective Classification

## Definición

Clasificación resultante tras combinar varias fuentes.

## Observaciones

Deberá adoptar al menos el nivel más restrictivo aplicable.

---

# Data Residency

## Definición

Requisitos sobre las regiones donde los datos pueden:

- procesarse;
- almacenarse;
- replicarse;
- respaldarse.

---

# Personal Data

## Definición

Información relacionada con una persona identificada o identificable.

---

# Sensitive Data

## Definición

Datos que requieren controles adicionales por su naturaleza, clasificación o regulación.

---

# Redaction

## Definición

Ocultación parcial o total de contenido sensible.

---

# Sanitization

## Definición

Transformación destinada a eliminar o neutralizar contenido no permitido o peligroso.

---

# Retention

## Definición

Periodo durante el cual un Resource o registro debe conservarse.

---

# Retention Policy

## Definición

Regla que determina duración, almacenamiento y eliminación de datos.

---

# Legal Hold

## Definición

Bloqueo de eliminación debido a una obligación legal o investigadora.

---

# Soft Delete

## Definición

Eliminación lógica que oculta un Resource sin borrarlo físicamente de inmediato.

---

# Hard Delete

## Definición

Eliminación física cuando es técnica y legalmente aplicable.

---

# Anonymization

## Definición

Transformación que elimina o desvincula la identidad personal de los datos.

---

# Security Event

## Definición

Event que representa una condición relevante de seguridad.

---

# Security Decision

## Definición

Resultado estructurado de una evaluación de seguridad.

---

# Policy

## Definición

Conjunto de reglas que gobierna una decisión o comportamiento.

---

# Policy Decision

## Definición

Resultado de evaluar una Policy sobre un contexto.

---

# Guardrail Decision

## Definición

Resultado producido por un Guardrail.

## Valores habituales

```text
allow
allow_with_constraints
sanitize
redact
request_confirmation
block
escalate
```

---

# Rate Limit

## Definición

Límite de consumo aplicado durante una ventana temporal.

---

# Quota

## Definición

Límite acumulado de uso asociado a un actor, Tenant, operación o periodo.

---

# Budget

## Definición

Límite de coste o recursos aplicable a una operación o periodo.

---

# Admission Control

## Definición

Proceso que determina si una operación puede aceptarse, encolarse, diferirse o rechazarse.

---

# Observabilidad y operación

---

# Observability

## Definición

Capacidad de comprender el estado interno del sistema a partir de señales externas.

---

# Metric

## Definición

Medida cuantitativa obtenida de una operación o sistema.

---

# Log

## Definición

Registro estructurado o textual de un hecho operativo.

---

# Structured Log

## Definición

Log expresado mediante campos tipados y consultables.

---

# Trace

## Definición

Representación distribuida del recorrido de una operación.

---

# Span

## Definición

Unidad individual de trabajo dentro de una Trace.

---

# Distributed Tracing

## Definición

Técnica que correlaciona Spans producidos por múltiples componentes.

---

# Audit

## Definición

Registro formal y trazable de acciones relevantes.

---

# Audit Record

## Definición

Entrada individual del Audit Trail.

---

# Audit Trail

## Definición

Secuencia protegida de Audit Records.

---

# SLI

## Definición

Indicador cuantitativo del nivel de servicio.

Corresponde a:

```text
Service Level Indicator
```

---

# SLO

## Definición

Objetivo cuantitativo asociado a uno o varios SLIs.

Corresponde a:

```text
Service Level Objective
```

---

# SLA

## Definición

Compromiso contractual de nivel de servicio.

Corresponde a:

```text
Service Level Agreement
```

## Observaciones

No deberá utilizarse como sinónimo de SLO.

---

# Error Budget

## Definición

Margen de incumplimiento permitido por un SLO durante una ventana.

---

# Burn Rate

## Definición

Velocidad a la que se consume un Error Budget.

---

# Alert

## Definición

Notificación generada cuando una condición operativa requiere atención.

---

# Dashboard

## Definición

Representación visual agregada de métricas, estados o tendencias.

---

# Health Check

## Definición

Comprobación del estado operativo de un componente.

---

# Liveness

## Definición

Indicador de que un proceso está vivo y puede continuar ejecutándose.

---

# Readiness

## Definición

Indicador de que un componente puede aceptar tráfico y cumplir sus contratos esenciales.

---

# Startup Check

## Definición

Comprobación de que la inicialización de un proceso ha finalizado.

---

# Degraded State

## Definición

Estado en el que un componente funciona con capacidades reducidas y declaradas.

---

# Incident

## Definición

Evento operativo que degrada o interrumpe un servicio.

---

# Runbook

## Definición

Procedimiento operativo documentado para responder a situaciones concretas.

---

# Rollback

## Definición

Retorno controlado a una versión o estado anterior.

---

# Recovery Time Objective

## Definición

Tiempo máximo objetivo para recuperar un servicio.

Abreviatura:

```text
RTO
```

---

# Recovery Point Objective

## Definición

Máxima pérdida temporal de datos aceptable.

Abreviatura:

```text
RPO
```

---

# Testing y evaluación

---

# Unit Test

## Definición

Prueba de una unidad lógica aislada.

---

# Integration Test

## Definición

Prueba de interacción entre varios componentes.

---

# End-to-End Test

## Definición

Prueba de un flujo completo desde el consumidor hasta el resultado final.

---

# Contract Test

## Definición

Prueba que verifica el cumplimiento de un Contract.

---

# Provider Contract Test

## Definición

Prueba que verifica que el proveedor implementa correctamente el contrato publicado.

---

# Consumer-Driven Contract Test

## Definición

Prueba basada en expectativas de consumidores concretos.

---

# Schema Test

## Definición

Prueba de validez y compatibilidad de un Schema.

---

# Regression Test

## Definición

Prueba destinada a detectar pérdida de comportamiento previamente correcto.

---

# Golden Dataset

## Definición

Dataset versionado utilizado como referencia estable de evaluación.

---

# Evaluation Run

## Definición

Ejecución concreta de una evaluación sobre:

- dataset;
- snapshot;
- modelo;
- perfil;
- versión.

---

# Ground Truth

## Definición

Resultado de referencia considerado correcto para una evaluación.

---

# Human Evaluation

## Definición

Evaluación realizada por revisores humanos mediante criterios definidos.

---

# LLM-as-Judge

## Definición

Uso de un modelo de lenguaje para evaluar outputs de otro sistema.

## Observaciones

Deberá utilizarse como señal auxiliar y gobernada.

---

# Benchmark

## Definición

Prueba reproducible destinada a medir rendimiento o calidad bajo condiciones definidas.

---

# Load Test

## Definición

Prueba bajo una carga prevista y sostenida.

---

# Stress Test

## Definición

Prueba que supera la capacidad esperada para observar degradación.

---

# Spike Test

## Definición

Prueba con incrementos abruptos de carga.

---

# Endurance Test

## Definición

Prueba prolongada destinada a detectar degradación acumulativa.

---

# Capacity Test

## Definición

Prueba destinada a determinar límites máximos de capacidad.

---

# Resilience Test

## Definición

Prueba de comportamiento ante fallos de dependencias o infraestructura.

---

# Chaos Experiment

## Definición

Experimento controlado que introduce fallos para validar hipótesis de resiliencia.

---

# Security Test

## Definición

Prueba destinada a validar controles de seguridad.

---

# Privacy Test

## Definición

Prueba destinada a validar minimización, retención, eliminación y protección de datos.

---

# Compatibility Test

## Definición

Prueba que verifica coexistencia entre versiones de contratos o componentes.

---

# Migration Test

## Definición

Prueba que valida la transición de una versión o modelo a otro.

---

# Canary

## Definición

Despliegue limitado utilizado para validar una nueva versión con una parte del tráfico.

---

# Shadow Testing

## Definición

Ejecución paralela de una versión nueva sin utilizar su resultado como respuesta principal.

---

# Términos que no deberán usarse como equivalentes

---

# Documento y Componente

```text
Documento
≠
Componente
```

Un Documento es una unidad documental.

Un Componente es una unidad reutilizable de conocimiento.

---

# Relación y Arista

```text
Relación
≠
Arista
```

La Relación es el concepto semántico.

La Arista es su representación dentro del Knowledge Graph.

---

# Entidad y Nodo

```text
Entidad
≠
Nodo
```

La Entidad pertenece al dominio.

El Nodo es una representación de dicha entidad en el grafo.

---

# Snapshot e Índice

```text
Snapshot
≠
Index
```

Un Snapshot representa un estado consistente.

Un Index es una estructura de búsqueda.

---

# Candidate Set y Evidence Set

```text
Candidate Set
≠
Evidence Set
```

El Candidate Set contiene resultados potenciales.

El Evidence Set contiene evidencias seleccionadas.

---

# Evidence Set y RagContext

```text
Evidence Set
≠
RagContext
```

El Evidence Set conserva fuentes.

El RagContext representa el contexto efectivo de generación.

---

# Retrieval Result y RagResponse

```text
Retrieval Result
≠
RagResponse
```

Retrieval devuelve conocimiento recuperado.

RAG devuelve una respuesta generada.

---

# Claim y Statement

```text
Claim
≠
Statement
```

Un Claim es una afirmación evaluable dentro de una respuesta.

Un Statement es una afirmación estructurada del modelo de conocimiento o razonamiento.

---

# Citation y Evidence

```text
Citation
≠
Evidence
```

La Evidence es la fuente.

La Citation es el vínculo efectivo entre la respuesta y esa fuente.

---

# Diagnostic y Problem Details

```text
Diagnostic
≠
Problem Details
```

Diagnostic es un contrato interno de validación.

Problem Details es su posible representación pública HTTP.

---

# Engine y Engine Instance

```text
Engine
≠
Engine Instance
```

Engine representa la capacidad o definición.

Engine Instance representa una implementación concreta disponible.

---

# Capability y Operation

```text
Capability
≠
Operation
```

Capability describe qué puede hacer un Engine.

Operation describe una acción invocable.

---

# Workflow y Workflow Execution

```text
Workflow
≠
Workflow Execution
```

Workflow es la definición.

Workflow Execution es una ejecución concreta.

---

# Job, Activity, Step y Task

No deberán tratarse automáticamente como equivalentes.

```text
Job
```

representa una unidad de trabajo gestionada.

```text
Activity
```

representa una acción ejecutable de un Workflow.

```text
Step
```

representa una unidad lógica del flujo.

```text
Task
```

representa trabajo concreto asignable o ejecutable.

---

# Conversation y Session

```text
Conversation
≠
Session
```

La Conversation es lógica y persistente.

La Session es temporal y operativa.

---

# History y Memory

```text
Conversation History
≠
Memory
```

History registra lo ocurrido.

Memory selecciona información reutilizable.

---

# Memory y Profile

```text
Memory
≠
Profile
```

Memory procede de interacciones o información retenida.

Profile es una configuración o conjunto de atributos gobernados.

---

# Regeneration y Retry

```text
Regeneration
≠
Retry
```

Regeneration busca una nueva respuesta.

Retry repite una operación fallida.

---

# Event y Command

```text
Event
≠
Command
```

Event describe un hecho pasado.

Command solicita una acción futura.

---

# Callback y Webhook

```text
Callback
≠
Webhook
```

Un Callback suele formar parte de una operación concreta.

Un Webhook corresponde normalmente a una suscripción persistente a Events.

---

# Warning y Error

```text
Warning
≠
Error
```

Un Warning permite continuar.

Un Error impide cumplir una operación según su contrato.

---

# Authentication y Authorization

```text
Authentication
≠
Authorization
```

Authentication verifica identidad.

Authorization verifica permisos.

---

# Scope y Role

```text
Scope
≠
Role
```

Scope representa un permiso declarado.

Role agrupa responsabilidades o permisos.

---

# Rate Limit, Quota y Budget

```text
Rate Limit
≠
Quota
≠
Budget
```

Rate Limit limita frecuencia.

Quota limita uso acumulado.

Budget limita coste o recursos.

---

# SLI, SLO y SLA

```text
SLI
≠
SLO
≠
SLA
```

SLI mide.

SLO fija un objetivo.

SLA establece un compromiso contractual.

---

# Liveness y Readiness

```text
Liveness
≠
Readiness
```

Liveness indica que el proceso está vivo.

Readiness indica que puede aceptar tráfico.

---

# Deprecation y Retirement

```text
Deprecation
≠
Retirement
```

Deprecation inicia la retirada.

Retirement la completa.

---

# Términos desaconsejados

---

# `IA`

Podrá utilizarse en lenguaje general.

En contratos deberá preferirse el componente concreto:

- Motor RAG;
- modelo;
- Razonador;
- Agent;
- Engine.

---

# `Motor inteligente`

Es demasiado ambiguo.

Deberá sustituirse por:

- Retrieval Engine;
- Reasoning Engine;
- RAG Engine;
- Validation Engine.

---

# `Resultado`

Deberá especializarse:

- Retrieval Result;
- Validation Result;
- Reasoning Result;
- RagResponse;
- Workflow Result.

---

# `Contexto`

Deberá especializarse cuando exista ambigüedad:

- RagContext;
- Conversation Context;
- Tenant Context;
- Security Context;
- Retrieval Execution Context;
- Workflow Execution Context.

---

# `Ejecución`

Deberá especializarse:

- RagExecution;
- Retrieval Execution;
- Workflow Execution;
- Validation Execution;
- Indexing Execution.

---

# `Registro`

Puede significar:

- Record;
- Registry;
- Log;
- Audit Record;
- Database Row.

Deberá utilizarse el término concreto.

---

# `Servicio`

Podrá utilizarse de forma general.

En contratos arquitectónicos deberá especificarse:

- API Service;
- Runtime Component;
- Engine;
- Provider;
- Worker.

---

# `Proceso`

Deberá especializarse cuando sea relevante:

- Workflow;
- Job;
- Activity;
- Pipeline;
- Execution.

---

# `Dato`

Deberá sustituirse, cuando sea posible, por:

- Document;
- Component;
- Statement;
- Evidence;
- Attribute;
- Property;
- Payload.

---

# `Fuente`

Deberá diferenciarse entre:

- Source de Ingesta;
- Evidence Source;
- Event Source;
- Source of Truth.

---

# `Modelo`

Deberá especializarse:

- Ontological Model;
- Data Model;
- Embedding Model;
- Generation Model;
- Logical Model;
- Evaluation Model.

---

# `Estado`

Deberá asociarse al recurso:

- Conversation Status;
- Engine Health;
- Execution Status;
- Validation Status;
- Memory Status.

---

# Sinónimos admitidos

Los siguientes términos podrán utilizarse como equivalentes cuando el contexto sea claro.

| Término canónico | Sinónimo admitido |
|---|---|
| Knowledge Graph | Grafo de conocimiento |
| Retrieval | Recuperación |
| Indexing | Indexación |
| Reasoning | Razonamiento |
| Grounding | Fundamentación |
| Citation | Cita |
| Workflow | Flujo de trabajo |
| Runtime | Entorno de ejecución |
| Front Matter | Cabecera YAML |
| Breaking Change | Cambio incompatible |
| Deprecation | Marcado como obsoleto |
| Retirement | Retirada |
| Tenant | Espacio aislado |
| Trace | Traza |
| Audit | Auditoría |

---

# Restricción sobre traducciones

En contratos, IDs, schemas y nombres de componentes deberá mantenerse el término canónico.

Ejemplo:

```text
Evidence Set
```

podrá explicarse como:

```text
conjunto de evidencias
```

pero no deberá cambiarse el identificador contractual.

---

# Reglas para incorporar un nuevo término

Antes de incorporar un término deberá comprobarse:

```text
¿Existe ya un término equivalente?

¿El nuevo término representa un concepto distinto?

¿Tiene un documento propietario?

¿Puede definirse con precisión?

¿Necesita un nombre en inglés?

¿Necesita traducción al español?

¿Puede confundirse con otro término?

¿Aparece en contratos?

¿Requiere versionado?

¿Requiere actualización del Authority Map?
```

---

# Propuesta de término

Formato recomendado:

```yaml
term_proposal:
  name:
  category:
  definition:
  owner:
  synonyms:
  related_terms:
  conflicts:
  contract_usage:
  rationale:
```

---

# Revisión del nuevo término

Deberá evaluarse:

- necesidad;
- claridad;
- consistencia;
- autoridad;
- impacto;
- compatibilidad;
- adopción.

---

# Aprobación

Un término transversal deberá aprobarse cuando afecte a:

- varios dominios;
- contratos;
- APIs;
- schemas;
- eventos;
- estados;
- IDs.

---

# Renombrado terminológico

Un cambio de nombre deberá tratarse como:

```text
editorial
```

si no cambia significado.

Podrá ser:

```text
breaking
```

si afecta contratos, IDs o consumidores.

---

# Alias

Un término renombrado podrá conservar un alias temporal.

---

# Alias Record

```yaml
term_alias:
  old: Response Context
  canonical: RagContext
  status: deprecated
  sunset: 2027-02-01
```

---

# Deprecation terminológica

Deberá declarar:

- término antiguo;
- término nuevo;
- motivo;
- fecha;
- alcance;
- migración.

---

# Término prohibido

Un término podrá marcarse como prohibido cuando:

- cause ambigüedad grave;
- represente un concepto incorrecto;
- duplique otro término;
- induzca a errores contractuales.

---

# Catálogo de términos prohibidos inicial

```text
resultado
contexto
ejecución
registro
motor inteligente
```

No están prohibidos en lenguaje natural.

Están desaconsejados sin especialización en contratos y especificaciones técnicas.

---

# Gobernanza del glosario

---

# Owner

El glosario deberá tener:

- owner conceptual;
- owner documental;
- revisores.

---

# Responsabilidades

El owner deberá:

- revisar nuevos términos;
- resolver conflictos;
- mantener sinónimos;
- actualizar deprecations;
- verificar autoridad;
- coordinar con `DEPENDENCIAS.md`;
- mantener coherencia con especificaciones.

---

# Ciclo de revisión

Se recomienda:

```text
P180D
```

o revisión cuando:

- se cree una especificación;
- aparezca un nuevo Engine;
- cambie un contrato transversal;
- se detecte una colisión;
- se introduzca un nuevo dominio.

---

# Fuentes del glosario

El glosario deberá derivarse de:

- especificaciones vigentes;
- ADR;
- contratos;
- schemas;
- APIs;
- eventos.

No deberá introducir conceptos sin fuente.

---

# Glosario y Ontología

El glosario define terminología arquitectónica.

La Ontología define conceptos del dominio culinario.

No deberán fusionarse.

---

# Glosario y Convenciones

El glosario responde:

```text
¿Qué significa este término?
```

`CONVENCIONES.md` responderá:

```text
¿Cómo debe escribirse, nombrarse e identificarse?
```

---

# Glosario y Dependencias

`DEPENDENCIAS.md` define:

```text
¿Quién posee el concepto y quién lo consume?
```

El glosario define:

```text
¿Qué significa el concepto?
```

---

# Automatización terminológica

La validación podrá comprobar:

- términos canónicos;
- términos deprecated;
- términos prohibidos;
- autoridad;
- alias;
- colisiones;
- uso inconsistente.

---

# Modelo de datos sugerido

```yaml
glossary_term:
  id:
  canonical_name:
  category:
  definition:
  owner:
  synonyms:
  related_terms:
  deprecated_aliases:
  status:
```

---

# Estados terminológicos

```text
proposed
active
deprecated
retired
forbidden
```

---

# Diagnósticos recomendados

```text
GLOSSARY_TERM_MISSING
GLOSSARY_TERM_DUPLICATED
GLOSSARY_TERM_AMBIGUOUS
GLOSSARY_TERM_OWNER_MISSING
GLOSSARY_TERM_OWNER_CONFLICT
GLOSSARY_NON_CANONICAL_TERM_USED
GLOSSARY_DEPRECATED_TERM_USED
GLOSSARY_FORBIDDEN_TERM_USED
GLOSSARY_ALIAS_CONFLICT
GLOSSARY_DEFINITION_CONFLICT
GLOSSARY_TRANSLATION_INCONSISTENT
GLOSSARY_CONTRACT_TERM_RENAMED
```

---

# Diagnostic Contract

```yaml
glossary_diagnostic:
  id: GLOSSARY-DIAG-000041
  code: GLOSSARY_NON_CANONICAL_TERM_USED
  severity: warning

  document:
    path: specifications/runtime/ESPECIFICACION_DEL_MOTOR_RAG.md

  term:
    found: Contexto de respuesta
    canonical: RagContext

  retryable: false
```

---

# Quality Gate de términos

```yaml
quality_gate:
  id: QG-GLOSSARY-TERMS-0001

  criteria:
    all:
      - canonical_terms_unique == true
      - definitions_present == true
      - categories_valid == true
      - owners_present == true
      - duplicate_terms_absent == true
      - ambiguous_terms_specialized == true
```

---

# Quality Gate de autoridad

```yaml
quality_gate:
  id: QG-GLOSSARY-AUTHORITY-0001

  criteria:
    all:
      - every_term_has_single_owner == true
      - glossary_matches_authority_map == true
      - deprecated_owners_absent == true
      - ownership_conflicts_absent == true
```

---

# Quality Gate de uso terminológico

```yaml
quality_gate:
  id: QG-GLOSSARY-USAGE-0001

  criteria:
    all:
      - canonical_terms_used_in_contracts == true
      - forbidden_terms_absent_from_contracts == true
      - deprecated_terms_have_migration == true
      - translations_consistent == true
      - execution_contexts_specialized == true
      - result_terms_specialized == true
```

---

# Quality Gate de interfaces

```yaml
quality_gate:
  id: QG-GLOSSARY-INTERFACES-0001

  criteria:
    all:
      - request_and_response_differentiated == true
      - event_and_command_differentiated == true
      - callback_and_webhook_differentiated == true
      - api_and_contract_differentiated == true
      - error_and_warning_differentiated == true
      - api_and_contract_versions_differentiated == true
```

---

# Quality Gate conversacional

```yaml
quality_gate:
  id: QG-GLOSSARY-CONVERSATION-0001

  criteria:
    all:
      - conversation_and_session_differentiated == true
      - history_and_memory_differentiated == true
      - memory_and_profile_differentiated == true
      - retry_and_regeneration_differentiated == true
      - turns_ordered == true
      - summaries_declared_as_derived == true
```

---

# Quality Gate de seguridad

```yaml
quality_gate:
  id: QG-GLOSSARY-SECURITY-0001

  criteria:
    all:
      - authentication_and_authorization_differentiated == true
      - scope_and_role_differentiated == true
      - tenant_context_defined == true
      - classification_terms_defined == true
      - retention_and_deletion_terms_defined == true
```

---

# Quality Gate de observabilidad

```yaml
quality_gate:
  id: QG-GLOSSARY-OBSERVABILITY-0001

  criteria:
    all:
      - metrics_logs_and_traces_differentiated == true
      - audit_and_logs_differentiated == true
      - sli_slo_and_sla_differentiated == true
      - liveness_and_readiness_differentiated == true
      - rpo_and_rto_defined == true
```

---

# Quality Gate global

```yaml
quality_gate:
  id: QG-GLOSSARY-GLOBAL-0001

  criteria:
    all:
      - terms_gate_passed == true
      - authority_gate_passed == true
      - usage_gate_passed == true
      - interfaces_gate_passed == true
      - conversation_gate_passed == true
      - security_gate_passed == true
      - observability_gate_passed == true
```

---

# Métricas terminológicas

El proyecto podrá medir:

```text
glossary_terms_total
glossary_terms_by_category
glossary_terms_without_owner
glossary_ambiguous_terms_total
glossary_deprecated_terms_total
glossary_forbidden_term_uses
glossary_aliases_total
glossary_definition_conflicts
glossary_non_canonical_uses
```

---

# Casos de uso

---

# Caso de uso 1 — Nuevo concepto Runtime

Se introduce `Evaluation Engine`.

Acciones:

1. definir concepto;
2. asignar owner;
3. añadir al Engine Registry;
4. actualizar Glosario;
5. actualizar Dependencias;
6. validar términos relacionados.

---

# Caso de uso 2 — Término ambiguo

Una especificación utiliza:

```text
Execution Context
```

sin especialización.

Resultado:

```text
GLOSSARY_TERM_AMBIGUOUS
```

Resolución:

```text
Retrieval Execution Context
```

o:

```text
Workflow Execution Context
```

---

# Caso de uso 3 — Duplicidad conceptual

RAG define de nuevo `Evidence Set`.

Resultado:

```text
GLOSSARY_TERM_OWNER_CONFLICT
```

Resolución:

- mantener autoridad en Retrieval;
- referenciar el término;
- definir una especialización si es necesaria.

---

# Caso de uso 4 — Renombrado contractual

Se desea cambiar:

```text
RagExecution
```

por:

```text
Generation Execution
```

Se deberá evaluar:

- contratos;
- APIs;
- schemas;
- eventos;
- compatibilidad;
- deprecation.

---

# Caso de uso 5 — Traducción

La documentación usa:

```text
Grounding
```

y:

```text
Fundamentación
```

Ambos podrán coexistir si:

- `Grounding` permanece como término canónico;
- la traducción se usa con finalidad explicativa;
- los contratos mantienen el término canónico.

---

# Caso de uso 6 — Término retirado

Se depreca:

```text
Response Context
```

a favor de:

```text
RagContext
```

El glosario conserva el alias temporal y la fecha de Sunset.

---

# Caso de uso 7 — Nueva API

Una API introduce `Batch Query`.

Antes de publicarla deberá definirse:

- significado;
- owner;
- diferencia con `RagQuery`;
- lifecycle;
- contrato;
- relación con Job.

---

# Caso de uso 8 — Término genérico

Una sección utiliza:

```text
resultado
```

La revisión deberá sustituirlo por el tipo correcto.

---

# Antipatrones

---

## Utilizar sinónimos libremente en contratos

Dificulta interoperabilidad.

---

## Definir términos dentro de cada documento

Genera divergencias.

---

## Traducir IDs contractuales

Rompe consumidores.

---

## Utilizar inglés y español sin criterio

Produce inconsistencias.

---

## Asignar varios owners

Genera conflicto de autoridad.

---

## Añadir términos sin necesidad

Aumenta complejidad conceptual.

---

## Definir tecnología en lugar de concepto

Ejemplo problemático:

```text
Pinecone Search
```

El concepto debería ser:

```text
Vector Index
```

La implementación podrá utilizar Pinecone u otra tecnología.

---

## Confundir producto y capacidad

Un Provider no equivale a una Capability.

---

## Utilizar `Engine` para cualquier clase o servicio

El término exige contrato, capacidad y lifecycle.

---

## Utilizar `Memory` para cualquier persistencia

Una base de datos no es Memory conversacional.

---

## Utilizar `Event` para una petición

Una petición es Command o Request.

---

## Utilizar `Session` para Conversation

Reduce claridad temporal.

---

## Utilizar `Context` sin especialización

Puede referirse a varios conceptos.

---

## Considerar todos los errores retryable

La retryability debe definirse.

---

## Utilizar `SLA` para objetivos internos

Normalmente corresponde a SLO.

---

## Considerar `no_answer` como error

Es un resultado funcional válido.

---

## Confundir Feedback con conocimiento

Debe validarse antes de incorporarse.

---

## Mantener aliases indefinidamente

Toda deprecation deberá tener retirada.

---

# Reglas mínimas de conformidad

---

## Término canónico

Todo concepto transversal deberá tener nombre canónico.

---

## Definición

Todo término deberá disponer de una definición precisa.

---

## Owner

Todo término deberá asociarse a un documento propietario.

---

## Sinónimos

Los sinónimos deberán estar controlados.

---

## Ambigüedad

Los términos genéricos deberán especializarse.

---

## Contratos

Los contratos deberán utilizar nombres canónicos.

---

## Traducciones

Las traducciones no deberán modificar IDs ni schemas.

---

## Deprecation

Los términos retirados deberán conservar una migración temporal.

---

## Coherencia

El glosario deberá coincidir con:

- README;
- Dependencias;
- especificaciones;
- schemas;
- APIs.

---

## Automatización

El uso terminológico deberá poder validarse progresivamente.

---

# Checklist de incorporación de término

```text
[ ] El concepto no está ya definido.
[ ] El nombre es preciso.
[ ] La categoría está identificada.
[ ] La definición es inequívoca.
[ ] El owner está definido.
[ ] Los consumidores están identificados.
[ ] Los términos relacionados están enlazados.
[ ] Los sinónimos están controlados.
[ ] Las traducciones están definidas.
[ ] Los conflictos están revisados.
[ ] El uso contractual está definido.
[ ] El Authority Map está actualizado.
[ ] DEPENDENCIAS.md está actualizado.
[ ] Las validaciones han pasado.
```

---

# Checklist de renombrado

```text
[ ] El nuevo nombre canónico está definido.
[ ] El significado no cambia o se ha versionado.
[ ] Los aliases temporales están registrados.
[ ] Los contratos están actualizados.
[ ] Los schemas están actualizados.
[ ] Las APIs están actualizadas.
[ ] Los eventos están actualizados.
[ ] Las referencias están actualizadas.
[ ] La deprecation está definida.
[ ] El Sunset está definido.
[ ] Los consumidores han sido informados.
```

---

# Checklist de revisión del glosario

```text
[ ] Todos los términos tienen definición.
[ ] Todos los términos tienen owner.
[ ] No existen owners duplicados.
[ ] Los conceptos ambiguos están especializados.
[ ] Los sinónimos son coherentes.
[ ] Las traducciones son consistentes.
[ ] Los términos deprecated tienen sustitución.
[ ] Los términos prohibidos no aparecen en contratos.
[ ] Los términos de APIs coinciden con sus schemas.
[ ] Los términos de Runtime coinciden con Engine Registry.
[ ] Candidate Set, Evidence Set y RagContext están diferenciados.
[ ] Conversation, Session y Turn están diferenciados.
[ ] History, Summary y Memory están diferenciados.
[ ] Diagnostic y Problem Details están diferenciados.
[ ] Event y Command están diferenciados.
[ ] Scope y Role están diferenciados.
[ ] Rate Limit, Quota y Budget están diferenciados.
[ ] SLI, SLO y SLA están diferenciados.
[ ] Liveness y Readiness están diferenciados.
[ ] README y DEPENDENCIAS están alineados.
[ ] Los Quality Gates han pasado.
```

---

# Conformidad global

`GLOSARIO.md` será conforme cuando:

- defina el vocabulario transversal vigente;
- mantenga un nombre canónico por concepto;
- identifique un owner por término;
- diferencie conceptos próximos;
- controle sinónimos y traducciones;
- gobierne ambigüedades;
- permita deprecations;
- permanezca alineado con especificaciones;
- pueda utilizarse como referencia para validación;
- no sustituya a los documentos autoritativos.

---

# Estado final del documento

```text
Documento:
docs/specifications/GLOSARIO.md

Versión:
1.0.0

Estado:
borrador

Dominio:
Documentación transversal

Partes:
3 / 3

Madurez:
Nivel 4 — Especificación completa

Estado de redacción:
FINALIZADA
```

---

# Referencias

- [README de especificaciones](README.md)
- [Mapa de dependencias](DEPENDENCIAS.md)
- [ARQUITECTURA](../architecture/ARQUITECTURA.md)
- [VISION](../VISION.md)
- [ROADMAP](../management/ROADMAP.md)
- [ADR](../governance/adr/README.md)
- [Especificación de Ontología](knowledge/ESPECIFICACION_DE_ONTOLOGIA.md)
- [Especificación de Documentos](knowledge/ESPECIFICACION_DE_DOCUMENTOS.md)
- [Especificación de Componentes](knowledge/ESPECIFICACION_DE_COMPONENTES.md)
- [Especificación de Relaciones](knowledge/ESPECIFICACION_DE_RELACIONES.md)
- [Especificación de Colecciones](knowledge/ESPECIFICACION_DE_COLECCIONES.md)
- [Especificación del Knowledge Graph](knowledge/ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md)
- [Especificación de Ingesta](ingestion/ESPECIFICACION_DE_INGESTA.md)
- [Especificación de Validación](runtime/ESPECIFICACION_DE_VALIDACION.md)
- [Especificación del Indexing Engine](runtime/ESPECIFICACION_DEL_INDEXING_ENGINE.md)
- [Especificación del Retrieval Engine](runtime/ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md)
- [Especificación del Razonador](runtime/ESPECIFICACION_DEL_RAZONADOR.md)
- [Especificación del Motor RAG](runtime/ESPECIFICACION_DEL_MOTOR_RAG.md)
- [Especificación del Orquestador de Ejecución](runtime/ESPECIFICACION_DEL_ORQUESTADOR_DE_EJECUCION.md)
- [Especificación del Engine Registry](runtime/ESPECIFICACION_DEL_ENGINE_REGISTRY.md)
- [Especificación de APIs](interfaces/ESPECIFICACION_DE_APIS.md)

---

# Conclusión

El glosario proporciona un vocabulario común para las especificaciones de NovaCoquinaria.

Su función puede resumirse así:

```text
Identificar
    ↓
Definir
    ↓
Asignar autoridad
    ↓
Diferenciar
    ↓
Normalizar
    ↓
Validar
    ↓
Evolucionar
```

La Ontología define el dominio culinario.

El glosario define la terminología arquitectónica.

`DEPENDENCIAS.md` identifica propietarios y consumidores.

`CONVENCIONES.md` definirá cómo deben escribirse e identificarse los conceptos.

Los documentos de conocimiento definen la estructura semántica.

Los documentos Runtime definen los procesos ejecutables.

Las APIs exponen los contratos.

La gobernanza mantiene consistencia.

Los Quality Gates permiten detectar divergencias.

Una arquitectura terminológicamente coherente deberá poder responder:

```text
¿Qué significa este término?

¿Cuál es su nombre canónico?

¿Qué documento lo define?

¿Qué sinónimos están permitidos?

¿Qué términos no son equivalentes?

¿Puede utilizarse en un contrato?

¿Está deprecated?

¿Qué término lo sustituye?

¿Su traducción modifica el contrato?

¿Qué documentos deben actualizarse si cambia?
```

Con esta tercera parte queda completado `GLOSARIO.md` como referencia terminológica transversal para las especificaciones de NovaCoquinaria.
