---
id: SPEC-README
tipo: especificacion
titulo: Catálogo y gobierno de las especificaciones de NovaCoquinaria
version: 1.0.0
estado: revision
ultima_revision: 2026-08-02
tags:
  - specifications
  - documentation
  - governance
  - architecture
---

# Especificaciones del SGCC (Sistema de Gestión del Conocimiento Culinario)

**Versión:** 1.0.0  
**Estado:** Enterprise Draft  
**Ubicación:** `/specifications`  
**Última actualización:** 2026-08-02

---

# Introducción

El directorio **`/specifications`** constituye el repositorio de referencia para las especificaciones funcionales y arquitectónicas del **Sistema de Gestión del Conocimiento Culinario (SGCC)** de NovaCoquinaria.

Su objetivo es definir, de forma rigurosa, los componentes que conforman la plataforma, sus responsabilidades, contratos, relaciones y comportamiento esperado, proporcionando una base sólida para el diseño, implementación, validación y evolución del sistema.

A diferencia de la documentación de gestión o de arquitectura de alto nivel, las especificaciones describen **qué es cada componente**, **qué responsabilidades tiene**, **cómo interactúa con el resto del sistema** y **qué requisitos debe cumplir** para considerarse conforme.

---

# Objetivos del directorio

Las especificaciones persiguen los siguientes objetivos:

- definir formalmente cada componente del SGCC;
- establecer responsabilidades claras entre módulos;
- describir contratos funcionales y técnicos;
- documentar modelos de datos y entidades;
- normalizar terminología y conceptos;
- facilitar la implementación independiente de cada componente;
- servir como referencia para revisiones arquitectónicas;
- apoyar la validación funcional y técnica;
- permitir la evolución controlada de la plataforma;
- reducir ambigüedades durante el desarrollo.

---

# Filosofía

Toda especificación del SGCC deberá responder, al menos, a las siguientes preguntas:

- ¿Qué problema resuelve este componente?
- ¿Cuál es su responsabilidad?
- ¿Qué entidades gestiona?
- ¿Qué información consume?
- ¿Qué información produce?
- ¿Qué contratos expone?
- ¿Qué dependencias posee?
- ¿Qué restricciones debe respetar?
- ¿Cómo interactúa con otros componentes?
- ¿Qué criterios determinan su conformidad?

Las especificaciones no constituyen documentación de implementación.

No describen código fuente, tecnologías concretas ni decisiones de bajo nivel, salvo cuando resulten necesarias para formalizar un contrato arquitectónico.

---

# Alcance

Las especificaciones cubren los principales dominios funcionales del SGCC:

- conocimiento;
- ingesta;
- ejecución;
- interfaces;
- integración entre componentes.

Otros aspectos transversales (arquitectura global, decisiones ADR, roadmap, gobierno del proyecto, etc.) se documentan en sus respectivos directorios.

---

# Organización

Actualmente las especificaciones se agrupan en los siguientes dominios:

```text
specifications/

├── knowledge/
├── ingestion/
├── runtime/
└── interfaces/
```

Cada dominio reúne documentos relacionados con una misma responsabilidad arquitectónica.

---

# Principios generales

Todas las especificaciones del SGCC comparten los siguientes principios.

---

## Responsabilidad única

Cada documento describe un único componente o dominio claramente identificado.

No deberán mezclarse responsabilidades independientes dentro de una misma especificación.

---

## Cohesión

Las entidades descritas dentro de un documento deberán pertenecer al mismo ámbito funcional.

---

## Bajo acoplamiento

Las dependencias con otros componentes deberán minimizarse y documentarse explícitamente.

---

## Contratos explícitos

Toda interacción entre componentes deberá realizarse mediante contratos claramente definidos.

---

## Versionado

Toda especificación deberá evolucionar mediante versiones identificables.

Los cambios incompatibles deberán quedar documentados.

---

## Trazabilidad

Toda decisión relevante deberá poder relacionarse con:

- arquitectura;
- ADR;
- requisitos;
- componentes afectados.

---

## Consistencia terminológica

Los conceptos utilizados deberán mantener el mismo significado en toda la documentación.

Cuando exista un término oficial, deberá utilizarse siempre la misma denominación.

---

## Independencia tecnológica

Siempre que sea posible, las especificaciones deberán describir el comportamiento esperado sin depender de una implementación concreta.

---

## Reutilización

Las definiciones comunes deberán compartirse entre documentos, evitando duplicidades innecesarias.

---

## Evolución incremental

Las especificaciones están diseñadas para evolucionar progresivamente sin comprometer la coherencia global del sistema.

---

# Tipología de documentos

Dentro del directorio existen diferentes tipos de especificaciones.

## Especificaciones de conocimiento

Definen la estructura del conocimiento culinario.

Ejemplos:

- Ontología
- Documentos
- Relaciones
- Colecciones
- Componentes
- Knowledge Graph

---

## Especificaciones de ingesta

Definen el proceso mediante el cual el conocimiento entra en el sistema.

Incluyen:

- adquisición;
- transformación;
- validación;
- incorporación al repositorio.

---

## Especificaciones de ejecución

Describen los motores responsables del funcionamiento operativo del SGCC.

Incluyen, entre otros:

- Engine Registry;
- Retrieval Engine;
- Indexing Engine;
- Motor RAG;
- Razonador;
- Orquestador de Ejecución;
- Motor de Validación.

---

## Especificaciones de interfaces

Definen los contratos de comunicación entre el SGCC y consumidores externos o internos.

Actualmente incluyen la especificación de APIs.

---

# Nivel de detalle esperado

Las especificaciones siguen un enfoque de ingeniería de software orientado a sistemas enterprise.

Cada documento desarrolla, cuando resulta aplicable:

- modelo conceptual;
- principios;
- arquitectura;
- entidades;
- contratos;
- ciclo de vida;
- reglas de negocio;
- validaciones;
- métricas;
- eventos;
- diagnósticos;
- calidad;
- conformidad;
- casos de uso;
- antipatrones.

No todos los documentos requieren necesariamente todos estos apartados, pero se recomienda mantener una estructura homogénea siempre que sea posible.

---

# Público objetivo

Estas especificaciones están dirigidas principalmente a:

- arquitectos software;
- desarrolladores;
- revisores técnicos;
- responsables funcionales;
- colaboradores del proyecto;
- asistentes de inteligencia artificial utilizados durante el desarrollo.

No constituyen documentación orientada al usuario final.

---

# Relación con el resto del proyecto

Las especificaciones forman parte del conjunto documental de NovaCoquinaria y deben interpretarse conjuntamente con:

- la arquitectura general del sistema;
- las decisiones ADR;
- la visión del proyecto;
- el roadmap;
- las guías de desarrollo;
- la documentación de gestión.

Cada uno de estos documentos cumple una función diferente y complementaria.

---

# Transición hacia la Parte II

La siguiente parte desarrollará:

- estructura completa del directorio;
- descripción detallada de cada dominio;
- mapa de especificaciones existentes;
- relaciones entre documentos;
- dependencias arquitectónicas;
- orden recomendado de lectura;
- criterios para incorporar nuevas especificaciones.

---

# Parte II — Estructura documental, dominios, catálogo de especificaciones, dependencias y orden recomendado de lectura

---

# Estructura general del directorio

La estructura actual del directorio de especificaciones es la siguiente:

```text
specifications/

├── README.md
│
├── ingestion/
│   └── ESPECIFICACION_DE_INGESTA.md
│
├── interfaces/
│   └── ESPECIFICACION_DE_APIS.md
│
├── knowledge/
│   ├── ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md
│   ├── ESPECIFICACION_DE_COLECCIONES.md
│   ├── ESPECIFICACION_DE_COMPONENTES.md
│   ├── ESPECIFICACION_DE_DOCUMENTOS.md
│   ├── ESPECIFICACION_DE_ONTOLOGIA.md
│   └── ESPECIFICACION_DE_RELACIONES.md
│
└── runtime/
    ├── ESPECIFICACION_DEL_ENGINE_REGISTRY.md
    ├── ESPECIFICACION_DEL_INDEXING_ENGINE.md
    ├── ESPECIFICACION_DEL_MOTOR_RAG.md
    ├── ESPECIFICACION_DEL_ORQUESTADOR_DE_EJECUCION.md
    ├── ESPECIFICACION_DEL_RAZONADOR.md
    ├── ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md
    └── ESPECIFICACION_DE_VALIDACION.md
```

La organización responde a cuatro dominios principales:

```text
knowledge
ingestion
runtime
interfaces
```

Cada dominio representa una responsabilidad arquitectónica diferenciada.

---

# Dominio `knowledge`

El dominio **`knowledge`** define el modelo estructural, semántico y relacional del conocimiento culinario gestionado por NovaCoquinaria.

Su responsabilidad principal es responder:

```text
¿Qué conocimiento existe?

¿Cómo se representa?

¿Cómo se relaciona?

¿Cómo se organiza?

¿Cómo se identifica?

¿Cómo puede consultarse y reutilizarse?
```

Este dominio constituye la base conceptual del SGCC.

---

# Especificaciones del dominio `knowledge`

---

## `ESPECIFICACION_DE_ONTOLOGIA.md`

Define la ontología general del conocimiento culinario.

Sus responsabilidades incluyen:

- categorías conceptuales;
- clases;
- entidades;
- propiedades;
- restricciones semánticas;
- vocabulario controlado;
- jerarquías;
- axiomas;
- dominios y rangos;
- reglas de interoperabilidad semántica.

La Ontología establece el significado compartido de los conceptos utilizados por el resto de especificaciones.

---

## `ESPECIFICACION_DE_DOCUMENTOS.md`

Define el modelo documental del SGCC.

Sus responsabilidades incluyen:

- tipos de documentos;
- estructura común;
- metadatos;
- Front Matter;
- identidad documental;
- lifecycle;
- versionado;
- estado;
- contenido;
- referencias;
- validación;
- trazabilidad.

Esta especificación determina cómo se representa una unidad documental dentro del repositorio de conocimiento.

---

## `ESPECIFICACION_DE_COMPONENTES.md`

Define los componentes reutilizables del conocimiento culinario.

Puede incluir entidades como:

- ingredientes;
- técnicas;
- bases;
- preparaciones;
- plantillas;
- tablas;
- equipamiento;
- unidades;
- procesos;
- estructuras reutilizables.

Su objetivo es evitar duplicidades y permitir la composición de conocimiento a partir de unidades normalizadas.

---

## `ESPECIFICACION_DE_RELACIONES.md`

Define las relaciones entre documentos, componentes y entidades.

Sus responsabilidades incluyen:

- tipos de relaciones;
- direccionalidad;
- cardinalidad;
- semántica;
- restricciones;
- relaciones inversas;
- integridad referencial;
- provenance;
- lifecycle de relaciones.

Ejemplos conceptuales:

```text
usa
depende_de
deriva_de
sustituye_a
incluye
pertenece_a
relacionado_con
requiere
```

Esta especificación constituye la base relacional del Knowledge Graph.

---

## `ESPECIFICACION_DE_COLECCIONES.md`

Define cómo se agrupan documentos y componentes en conjuntos funcionales.

Sus responsabilidades incluyen:

- identidad de colección;
- criterios de pertenencia;
- colecciones estáticas;
- colecciones dinámicas;
- filtros;
- orden;
- visibilidad;
- versionado;
- curatoría;
- publicación.

Las colecciones permiten organizar el conocimiento según objetivos de consulta, navegación o uso.

---

## `ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md`

Define la representación en grafo del conocimiento culinario.

Sus responsabilidades incluyen:

- nodos;
- relaciones;
- propiedades;
- Statements;
- provenance;
- snapshots;
- subgrafos;
- consultas;
- inferencia;
- validación;
- consistencia;
- traversal;
- lineage.

El Knowledge Graph integra:

```text
Ontología
+
Documentos
+
Componentes
+
Relaciones
+
Colecciones
```

y proporciona una estructura navegable y procesable para los motores del Runtime.

---

# Dependencias internas de `knowledge`

La relación conceptual principal es:

```text
Ontología
    ↓
Documentos
    ↓
Componentes
    ↓
Relaciones
    ↓
Colecciones
    ↓
Knowledge Graph
```

No representa necesariamente un orden de implementación estrictamente lineal, pero sí un orden de comprensión recomendado.

---

# Autoridad conceptual dentro de `knowledge`

Cada especificación deberá actuar como fuente principal para su propio ámbito.

| Concepto | Especificación autoritativa |
|---|---|
| Clases y conceptos | Ontología |
| Unidad documental | Documentos |
| Elementos reutilizables | Componentes |
| Vínculos semánticos | Relaciones |
| Agrupaciones | Colecciones |
| Representación en grafo | Knowledge Graph |

Cuando un concepto aparezca en varias especificaciones, deberá mantenerse una única fuente autoritativa y utilizarse referencias desde el resto.

---

# Dominio `ingestion`

El dominio **`ingestion`** define cómo entra el conocimiento en NovaCoquinaria.

Responde:

```text
¿De dónde procede la información?

¿Cómo se recibe?

¿Cómo se identifica?

¿Cómo se transforma?

¿Cómo se normaliza?

¿Cómo se valida?

¿Cómo se incorpora al SGCC?
```

---

# `ESPECIFICACION_DE_INGESTA.md`

Esta especificación define el pipeline de incorporación de conocimiento.

Sus responsabilidades pueden incluir:

- fuentes;
- conectores;
- adquisición;
- recepción;
- lotes;
- documentos de entrada;
- formatos;
- parsing;
- extracción;
- normalización;
- deduplicación;
- clasificación;
- staging;
- lineage;
- validación;
- errores;
- cuarentena;
- publicación;
- reingesta;
- idempotencia.

La ingesta actúa como frontera entre fuentes externas o internas y el modelo canónico del SGCC.

---

# Relación de Ingesta con `knowledge`

La ingesta deberá producir información compatible con:

- la Ontología;
- el modelo de Documentos;
- los Componentes;
- las Relaciones;
- el Knowledge Graph.

Flujo conceptual:

```text
Fuente
    ↓
Ingesta
    ↓
Normalización
    ↓
Validación
    ↓
Documento canónico
    ↓
Componentes y Relaciones
    ↓
Knowledge Graph
```

---

# Relación de Ingesta con `runtime`

La ingesta podrá utilizar componentes del Runtime para:

- validación;
- indexación;
- extracción;
- clasificación;
- razonamiento;
- orquestación;
- publicación de eventos.

No obstante, la responsabilidad funcional de incorporar información seguirá perteneciendo a `ingestion`.

---

# Dominio `runtime`

El dominio **`runtime`** contiene los componentes responsables del procesamiento operativo del conocimiento.

Responde:

```text
¿Cómo se valida el conocimiento?

¿Cómo se indexa?

¿Cómo se recupera?

¿Cómo se razona?

¿Cómo se genera una respuesta?

¿Cómo se coordinan los procesos?

¿Cómo se descubren y seleccionan los motores?
```

---

# Especificaciones del dominio `runtime`

---

## `ESPECIFICACION_DE_VALIDACION.md`

Define el motor o proceso de validación.

Sus responsabilidades incluyen:

- validación estructural;
- validación semántica;
- reglas;
- Quality Gates;
- diagnósticos;
- severidades;
- resultados;
- excepciones;
- validación incremental;
- validación de documentos;
- validación de relaciones;
- validación de snapshots.

Esta especificación es responsable de determinar si una unidad de conocimiento cumple los contratos del SGCC.

---

## `ESPECIFICACION_DEL_INDEXING_ENGINE.md`

Define el motor de indexación.

Sus responsabilidades incluyen:

- selección de unidades indexables;
- chunking;
- representaciones;
- embeddings;
- índices lexicales;
- índices vectoriales;
- índices híbridos;
- snapshots;
- publicación;
- actualización;
- eliminación;
- consistency;
- lineage;
- recuperación.

El Indexing Engine transforma el conocimiento canónico en estructuras optimizadas para recuperación.

---

## `ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md`

Define el motor de recuperación.

Sus responsabilidades incluyen:

- Query Understanding;
- planificación de consulta;
- recuperación lexical;
- recuperación vectorial;
- recuperación estructurada;
- recuperación mediante grafo;
- ranking;
- reranking;
- fusión;
- filtros;
- evidencia;
- provenance;
- context selection.

El Retrieval Engine recupera unidades de conocimiento relevantes para una necesidad concreta.

---

## `ESPECIFICACION_DEL_RAZONADOR.md`

Define el motor de razonamiento.

Sus responsabilidades incluyen:

- reglas;
- inferencia;
- deducción;
- resolución de restricciones;
- explicación;
- Statements;
- consistencia;
- razonamiento sobre relaciones;
- validación lógica;
- inferencia culinaria controlada.

El Razonador deberá operar sobre conocimiento trazable y declarar siempre la base de sus conclusiones.

---

## `ESPECIFICACION_DEL_MOTOR_RAG.md`

Define el motor de generación aumentada mediante recuperación.

Sus responsabilidades incluyen:

- recepción de consultas;
- recuperación de contexto;
- context assembly;
- grounding;
- prompt construction;
- generación;
- citas;
- validación;
- no-respuesta;
- control de alucinaciones;
- modelos;
- resultados;
- feedback.

El Motor RAG combina recuperación y generación sin sustituir al Retrieval Engine ni al Knowledge Graph.

---

## `ESPECIFICACION_DEL_ORQUESTADOR_DE_EJECUCION.md`

Define la coordinación de procesos ejecutables.

Sus responsabilidades incluyen:

- Workflows;
- DAGs;
- Steps;
- Jobs;
- Scheduler;
- Worker Pools;
- estados;
- eventos;
- señales;
- timers;
- retries;
- cancelación;
- compensación;
- concurrencia;
- persistencia;
- recovery;
- resultados;
- operación distribuida.

El Orquestador determina:

```text
qué debe ejecutarse
```

```text
en qué orden
```

```text
con qué dependencias
```

```text
bajo qué políticas de recuperación
```

---

## `ESPECIFICACION_DEL_ENGINE_REGISTRY.md`

Define el catálogo y plano de control de Engines.

Sus responsabilidades incluyen:

- Engine Definitions;
- Engine Instances;
- Providers;
- Capabilities;
- Operations;
- Contracts;
- registro;
- discovery;
- health;
- availability;
- matching;
- routing;
- seguridad;
- gobernanza;
- lifecycle.

El Engine Registry responde:

```text
¿Qué Engines existen?

¿Qué capacidades ofrecen?

¿Qué instancias están disponibles?

¿Cuál puede ejecutar una Activity concreta?
```

---

# Dependencias internas de `runtime`

Flujo operativo simplificado:

```text
Orquestador de Ejecución
        ↓
Engine Registry
        ↓
Engine compatible
        ↓
Validación / Indexación / Retrieval / Razonamiento / RAG
```

Flujo de conocimiento:

```text
Conocimiento canónico
        ↓
Validation Engine
        ↓
Indexing Engine
        ↓
Retrieval Engine
        ↓
Razonador
        ↓
Motor RAG
```

Este flujo no implica que todos los componentes deban utilizarse siempre ni en ese orden exacto.

---

# Autoridad conceptual dentro de `runtime`

| Concepto | Especificación autoritativa |
|---|---|
| Reglas de validación | Validación |
| Estructuras de índice | Indexing Engine |
| Recuperación y ranking | Retrieval Engine |
| Inferencia | Razonador |
| Generación grounded | Motor RAG |
| Workflows y lifecycle de ejecución | Orquestador |
| Engines, Capabilities y Discovery | Engine Registry |

---

# Límites de responsabilidad en `runtime`

Para evitar solapamientos, deberán respetarse las siguientes fronteras.

---

## Orquestador frente a Engine Registry

El Orquestador:

- coordina;
- agenda;
- controla estados;
- recupera ejecuciones.

El Engine Registry:

- registra;
- describe;
- descubre;
- evalúa compatibilidad;
- proporciona candidatos.

---

## Retrieval Engine frente a Motor RAG

El Retrieval Engine:

- recupera evidencia;
- ordena candidatos;
- prepara contexto.

El Motor RAG:

- consume contexto;
- genera una respuesta;
- mantiene grounding;
- produce citas.

---

## Knowledge Graph frente a Razonador

El Knowledge Graph:

- representa hechos y relaciones.

El Razonador:

- deriva conclusiones;
- aplica reglas;
- explica inferencias.

---

## Validación frente a Razonamiento

La Validación comprueba conformidad.

El Razonamiento genera conclusiones derivadas.

Una conclusión puede posteriormente someterse a validación.

---

## Indexing frente a Retrieval

El Indexing Engine crea y mantiene índices.

El Retrieval Engine consulta dichos índices.

---

# Dominio `interfaces`

El dominio **`interfaces`** define cómo se exponen y consumen las capacidades del SGCC.

Responde:

```text
¿Cómo se comunica un consumidor con NovaCoquinaria?

¿Qué recursos se exponen?

¿Qué contratos se utilizan?

¿Cómo se versionan?

¿Cómo se representan errores?

¿Cómo se autentican las solicitudes?

¿Cómo se mantiene compatibilidad?
```

---

# `ESPECIFICACION_DE_APIS.md`

Define los contratos de interfaz del SGCC.

Sus responsabilidades incluyen:

- API families;
- recursos;
- endpoints;
- requests;
- responses;
- errores;
- paginación;
- filtros;
- versionado;
- idempotencia;
- autenticación;
- autorización;
- rate limits;
- eventos;
- callbacks;
- observabilidad;
- lifecycle de contratos.

Las APIs no deberán duplicar la lógica funcional de los componentes internos.

Deberán exponerla mediante contratos estables.

---

# Relación de `interfaces` con el resto de dominios

```text
Consumidor
    ↓
API
    ↓
Orquestador o componente funcional
    ↓
Knowledge / Runtime / Ingestion
```

La API actúa como frontera contractual.

No deberá convertirse en la fuente autoritativa del modelo interno.

---

# Catálogo actual de especificaciones

| Dominio | Documento | Responsabilidad principal |
|---|---|---|
| Knowledge | Ontología | Modelo conceptual |
| Knowledge | Documentos | Unidad documental |
| Knowledge | Componentes | Elementos reutilizables |
| Knowledge | Relaciones | Vínculos semánticos |
| Knowledge | Colecciones | Agrupación de conocimiento |
| Knowledge | Knowledge Graph | Representación en grafo |
| Ingestion | Ingesta | Entrada y normalización |
| Runtime | Validación | Conformidad y diagnósticos |
| Runtime | Indexing Engine | Creación de índices |
| Runtime | Retrieval Engine | Recuperación de conocimiento |
| Runtime | Razonador | Inferencia y reglas |
| Runtime | Motor RAG | Generación grounded |
| Runtime | Orquestador | Coordinación de ejecuciones |
| Runtime | Engine Registry | Registro y selección de Engines |
| Interfaces | APIs | Contratos de exposición |

---

# Mapa general de dependencias

```text
                         VISION
                           │
                           ▼
                     ARQUITECTURA
                           │
                           ▼
                        ADRs
                           │
                           ▼
                    SPECIFICATIONS
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      Knowledge        Ingestion        Interfaces
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                        Runtime
```

---

# Dependencias funcionales principales

```text
Ontología
    ↓
Documentos
    ↓
Componentes
    ↓
Relaciones
    ↓
Knowledge Graph
```

```text
Fuentes
    ↓
Ingesta
    ↓
Validación
    ↓
Knowledge Graph
```

```text
Knowledge Graph
    ↓
Indexing Engine
    ↓
Retrieval Engine
    ↓
Motor RAG
```

```text
Knowledge Graph
    ↓
Razonador
    ↓
Motor RAG
```

```text
Orquestador de Ejecución
    ↓
Engine Registry
    ↓
Engines especializados
```

```text
APIs
    ↓
Orquestador
    ↓
Runtime
    ↓
Knowledge
```

---

# Dependencias documentales

Las dependencias documentales no deberán confundirse con dependencias de ejecución.

Ejemplo:

```text
Motor RAG
```

puede depender documentalmente de:

- Retrieval Engine;
- APIs;
- Knowledge Graph;
- Ontología.

Pero una implementación concreta podría desacoplarse mediante contratos.

---

# Tipos de dependencia

Toda dependencia entre especificaciones debería clasificarse como:

```text
conceptual
contractual
runtime
data
security
governance
optional
```

---

# Dependencia conceptual

Una especificación utiliza conceptos definidos por otra.

Ejemplo:

```text
Knowledge Graph
→
Ontología
```

---

# Dependencia contractual

Un componente consume contratos definidos por otro.

Ejemplo:

```text
Motor RAG
→
Retrieval Result Contract
```

---

# Dependencia Runtime

Un componente necesita que otro esté disponible durante ejecución.

Ejemplo:

```text
Orquestador
→
Engine Registry
```

---

# Dependencia de datos

Un componente consume datos producidos por otro.

Ejemplo:

```text
Retrieval Engine
→
Index Snapshot
```

---

# Dependencia de seguridad

Un componente necesita una decisión o perfil de seguridad.

Ejemplo:

```text
Engine Registry
→
Trust Policy
```

---

# Dependencia de gobernanza

Una evolución requiere aprobación o ADR.

---

# Dependencia opcional

El componente puede operar sin ella, pero con capacidades reducidas.

---

# Orden recomendado de lectura

No existe un único orden obligatorio.

El orden dependerá del objetivo del lector.

---

# Ruta de lectura conceptual

Recomendada para comprender el modelo de conocimiento:

```text
1. README.md
2. ESPECIFICACION_DE_ONTOLOGIA.md
3. ESPECIFICACION_DE_DOCUMENTOS.md
4. ESPECIFICACION_DE_COMPONENTES.md
5. ESPECIFICACION_DE_RELACIONES.md
6. ESPECIFICACION_DE_COLECCIONES.md
7. ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md
```

---

# Ruta de lectura del ciclo de conocimiento

Recomendada para comprender cómo entra y se transforma la información:

```text
1. README.md
2. ESPECIFICACION_DE_INGESTA.md
3. ESPECIFICACION_DE_VALIDACION.md
4. ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md
5. ESPECIFICACION_DEL_INDEXING_ENGINE.md
6. ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md
```

---

# Ruta de lectura de consulta y generación

Recomendada para comprender la interacción de consulta:

```text
1. README.md
2. ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md
3. ESPECIFICACION_DEL_INDEXING_ENGINE.md
4. ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md
5. ESPECIFICACION_DEL_RAZONADOR.md
6. ESPECIFICACION_DEL_MOTOR_RAG.md
7. ESPECIFICACION_DE_APIS.md
```

---

# Ruta de lectura del Runtime

Recomendada para comprender la ejecución distribuida:

```text
1. README.md
2. ESPECIFICACION_DEL_ORQUESTADOR_DE_EJECUCION.md
3. ESPECIFICACION_DEL_ENGINE_REGISTRY.md
4. ESPECIFICACION_DE_VALIDACION.md
5. ESPECIFICACION_DEL_INDEXING_ENGINE.md
6. ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md
7. ESPECIFICACION_DEL_RAZONADOR.md
8. ESPECIFICACION_DEL_MOTOR_RAG.md
```

---

# Ruta de lectura de integración

Recomendada para implementar consumidores:

```text
1. README.md
2. ESPECIFICACION_DE_APIS.md
3. ESPECIFICACION_DEL_ORQUESTADOR_DE_EJECUCION.md
4. Especificación funcional del componente consumido
```

---

# Ruta de lectura para arquitectura

Recomendada para revisar el conjunto:

```text
1. VISION.md
2. ARQUITECTURA.md
3. ADR relevantes
4. specifications/README.md
5. Ontología
6. Knowledge Graph
7. Ingesta
8. Orquestador
9. Engine Registry
10. Retrieval Engine
11. Motor RAG
12. APIs
```

---

# Ruta de lectura para implementación incremental

Orden recomendado de construcción conceptual:

```text
1. Ontología
2. Documentos
3. Componentes
4. Relaciones
5. Validación
6. Ingesta
7. Knowledge Graph
8. Indexing Engine
9. Retrieval Engine
10. APIs básicas
11. Razonador
12. Motor RAG
13. Orquestador
14. Engine Registry
15. Capacidades avanzadas
```

Este orden es orientativo.

No implica que todos los componentes deban desarrollarse de forma completa antes de comenzar el siguiente.

---

# Niveles de madurez documental

Cada especificación podrá clasificarse según el siguiente modelo.

---

## Nivel 0 — Idea

Existe el concepto, pero no una definición formal.

---

## Nivel 1 — Borrador inicial

El propósito y alcance están definidos.

---

## Nivel 2 — Modelo conceptual

Existen entidades, relaciones y responsabilidades.

---

## Nivel 3 — Contratos definidos

Existen contratos, estados, reglas y errores.

---

## Nivel 4 — Especificación completa

Incluye:

- arquitectura;
- lifecycle;
- seguridad;
- observabilidad;
- Quality Gates;
- conformidad.

---

## Nivel 5 — Validada para implementación

La especificación:

- ha sido revisada;
- no contiene contradicciones conocidas;
- está alineada con ADR;
- dispone de ejemplos;
- dispone de criterios de aceptación;
- puede implementarse.

---

## Nivel 6 — Implementada

Existe una implementación conforme.

---

## Nivel 7 — Verificada en producción

La implementación ha sido:

- desplegada;
- observada;
- validada;
- contrastada con la especificación.

---

# Estado general esperado

La documentación actual representa principalmente:

```text
Nivel 3
a
Nivel 4
```

según el documento.

La existencia de una especificación extensa no implica automáticamente que esté validada para implementación.

---

# Estado documental recomendado

Cada especificación deberá declarar un estado.

Valores recomendados:

```text
draft
review
approved
implementation_ready
implemented
deprecated
retired
```

---

# Draft

Documento en construcción.

---

# Review

Contenido completo pendiente de revisión.

---

# Approved

Arquitectura aprobada.

---

# Implementation Ready

Posee detalle suficiente para comenzar implementación.

---

# Implemented

Existe una implementación conforme.

---

# Deprecated

No se recomienda para nuevas implementaciones.

---

# Retired

Solo se conserva para referencia histórica.

---

# Criterios para crear una nueva especificación

No deberá crearse un nuevo documento únicamente porque aparezca un nuevo término.

Una nueva especificación estará justificada cuando exista:

- responsabilidad propia;
- lifecycle propio;
- contratos propios;
- modelo de datos propio;
- ownership claro;
- independencia razonable;
- necesidad de evolución separada;
- volumen suficiente;
- impacto arquitectónico.

---

# Preguntas previas

Antes de crear una especificación deberá comprobarse:

```text
¿Existe ya un documento que cubre esta responsabilidad?

¿Es un componente o únicamente una función?

¿Tiene entidades propias?

¿Tiene contratos propios?

¿Tiene lifecycle propio?

¿Puede evolucionar independientemente?

¿Necesita un owner distinto?

¿Su separación reduce o aumenta duplicidad?
```

---

# Cuándo ampliar una especificación existente

Se ampliará un documento existente cuando:

- el concepto pertenece claramente al mismo dominio;
- comparte lifecycle;
- comparte contratos;
- comparte ownership;
- su separación no aporta independencia;
- el volumen añadido sigue siendo manejable.

---

# Cuándo dividir una especificación

Podrá dividirse cuando:

- se vuelva difícil de navegar;
- contenga varios bounded contexts;
- existan owners diferentes;
- los ciclos de vida sean independientes;
- haya contratos reutilizables;
- existan implementaciones separadas;
- la evolución produzca conflictos frecuentes.

---

# No dividir únicamente por tamaño

Un documento extenso puede seguir siendo correcto si mantiene:

- cohesión;
- índice;
- estructura;
- autoridad única;
- navegación adecuada.

---

# Criterios de ubicación por directorio

---

## Ubicar en `knowledge/`

Cuando el documento defina:

- conocimiento;
- semántica;
- entidades;
- documentos;
- relaciones;
- grafos;
- agrupaciones.

---

## Ubicar en `ingestion/`

Cuando defina:

- entrada;
- adquisición;
- normalización;
- staging;
- incorporación;
- reingesta.

---

## Ubicar en `runtime/`

Cuando defina:

- ejecución;
- procesamiento;
- motores;
- planificación;
- recuperación;
- generación;
- razonamiento;
- validación operativa.

---

## Ubicar en `interfaces/`

Cuando defina:

- APIs;
- eventos públicos;
- callbacks;
- Webhooks;
- SDKs;
- contratos de consumidores.

---

# Posibles dominios futuros

Solo deberán crearse cuando existan documentos reales que los justifiquen.

Ejemplos potenciales:

```text
governance/
security/
operations/
integration/
deployment/
evaluation/
agents/
```

No deberán crearse directorios vacíos únicamente como previsión.

---

# Convención de referencias

Las especificaciones deberán referenciar otros documentos mediante rutas relativas.

Ejemplo:

```markdown
[Especificación del Knowledge Graph](./knowledge/ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md)
```

---

# Referencias estables

Las referencias deberán utilizar:

- nombre canónico;
- ruta real;
- capitalización correcta;
- extensión exacta.

---

# No duplicar contenido autoritativo

Cuando otra especificación sea la fuente principal, se deberá:

1. resumir únicamente lo necesario;
2. enlazar la fuente;
3. evitar redefinir el contrato;
4. declarar cualquier extensión específica.

---

# Mapa de ownership documental

Se recomienda que cada documento declare:

```text
owner conceptual
owner técnico
revisores
estado
última revisión
próxima revisión
```

---

# Ejemplo

```yaml
document_ownership:
  conceptual_owner: TEAM-KNOWLEDGE
  technical_owner: TEAM-PLATFORM
  reviewers:
    - ARCHITECTURE-BOARD
  review_cycle: P90D
```

---

# Revisión cruzada

Las especificaciones con dependencias deberán revisarse conjuntamente cuando exista un cambio incompatible.

Ejemplos:

```text
Ontología
+
Knowledge Graph
```

```text
Indexing Engine
+
Retrieval Engine
```

```text
Orquestador
+
Engine Registry
```

```text
Motor RAG
+
Retrieval Engine
+
APIs
```

---

# Matriz de impacto

Todo cambio relevante deberá identificar:

- documento modificado;
- documentos consumidores;
- contratos afectados;
- migraciones;
- compatibilidad;
- ADR necesario;
- versión resultante.

---

# Ejemplo

```yaml
specification_change_impact:
  source:
    document: ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md

  change:
    contract: RETRIEVAL-RESULT
    from: 2.0.0
    to: 3.0.0

  affected:
    - ESPECIFICACION_DEL_MOTOR_RAG.md
    - ESPECIFICACION_DEL_ENGINE_REGISTRY.md
    - ESPECIFICACION_DE_APIS.md

  compatibility: breaking
```

---

# Dependencias circulares documentales

Deberán evitarse ciclos de autoridad.

Ejemplo problemático:

```text
A define X según B
B define X según A
```

Cada concepto deberá tener una única fuente principal.

---

# Dependencias circulares Runtime

Podrán existir colaboraciones bidireccionales, pero deberán formalizarse mediante contratos.

Ejemplo:

```text
Orquestador
↔
Engine Registry
```

El Orquestador consulta el Registry.

El Registry puede recibir métricas operativas del Orquestador.

Esto no implica que ambos definan el mismo concepto.

---

# Documentos transversales futuros

Para mejorar la cohesión del conjunto se prevé la posible creación de:

```text
GLOSARIO.md
CONVENCIONES.md
DEPENDENCIAS.md
```

---

# `GLOSARIO.md`

Servirá como fuente común de términos.

---

# `CONVENCIONES.md`

Definirá:

- nombres;
- IDs;
- versiones;
- estados;
- contratos;
- ejemplos;
- estilo documental.

---

# `DEPENDENCIAS.md`

Podrá mantener:

- matriz completa;
- diagramas;
- impacto;
- authority map;
- ciclos;
- orden de evolución.

---

# No sustituir las especificaciones

Estos documentos transversales deberán complementar, no reemplazar, las especificaciones de dominio.

---

# Transición hacia la Parte III

La tercera y última parte desarrollará:

- convenciones de nomenclatura;
- convenciones de archivos;
- estructura interna recomendada;
- versionado documental;
- estados;
- control de cambios;
- Quality Gates documentales;
- validación de enlaces;
- mantenimiento;
- gobernanza;
- checklist global;
- estado final del README.

---

# Parte III — Convenciones, versionado, estados, validación, mantenimiento, gobernanza y conformidad documental

---

# Convenciones generales

El directorio `specifications/` deberá mantener convenciones homogéneas para facilitar:

- navegación;
- búsqueda;
- mantenimiento;
- revisión;
- automatización;
- validación;
- trazabilidad.

Las convenciones descritas en esta parte se aplican a todas las especificaciones salvo excepción explícita y justificada.

---

# Convención de nombres de archivo

Los nombres de archivo deberán:

- utilizar mayúsculas;
- utilizar guion bajo;
- evitar espacios;
- utilizar caracteres ASCII siempre que sea posible;
- conservar extensión `.md`;
- describir con precisión el contenido;
- evitar abreviaturas ambiguas;
- mantener una única forma canónica.

Formato general:

```text
ESPECIFICACION_DE_<CONCEPTO>.md
```

o:

```text
ESPECIFICACION_DEL_<CONCEPTO>.md
```

Ejemplos:

```text
ESPECIFICACION_DE_INGESTA.md
ESPECIFICACION_DE_DOCUMENTOS.md
ESPECIFICACION_DE_RELACIONES.md
ESPECIFICACION_DEL_ENGINE_REGISTRY.md
ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md
ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md
```

---

# Nombres canónicos

Cada especificación deberá tener un único nombre oficial.

No deberán coexistir variantes como:

```text
Knowledge Graph
KnowledgeGraph
Knowledge-Graph
Grafo de Conocimiento
KNOLWEDGE GRAPH
```

salvo en contextos de traducción o explicación.

El nombre canónico deberá utilizarse en:

- títulos;
- enlaces;
- índices;
- referencias;
- diagramas;
- metadatos;
- dependencias.

---

# Corrección de nombres

Todo renombrado deberá incluir:

1. cambio del archivo;
2. actualización de enlaces;
3. actualización de índices;
4. actualización de referencias en ADR;
5. validación de enlaces;
6. registro del cambio.

Ejemplo:

```text
ESPECIFICACION_DEL_KNOLWEDGE_GRAPH.md
```

deberá renombrarse como:

```text
ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md
```

---

# Convención de títulos

El título principal deberá reflejar el nombre oficial.

Ejemplo:

```markdown
# Especificación del Engine Registry
```

o:

```markdown
# Especificación del Knowledge Graph
```

No deberán utilizarse títulos genéricos como:

```markdown
# Documento técnico
```

---

# Convención de idioma

La documentación del proyecto se redactará principalmente en español.

Los términos técnicos ampliamente aceptados podrán conservarse en inglés cuando:

- sean nombres canónicos;
- formen parte de un contrato;
- representen componentes;
- eviten traducciones ambiguas.

Ejemplos:

```text
Engine Registry
Knowledge Graph
Runtime
Workflow
Snapshot
Capability
Quality Gate
```

Cuando un término inglés sea central, deberá utilizarse de forma consistente.

---

# Convención de capitalización

Se recomienda utilizar mayúscula inicial para conceptos arquitectónicos formalizados.

Ejemplos:

```text
Engine
Capability
Document
Collection
Statement
Workflow
Execution
Snapshot
```

Los usos genéricos podrán escribirse en minúscula.

Ejemplo:

```text
El Engine Registry registra Engines.
```

---

# Convención de identificadores

Los identificadores documentados deberán ser:

- únicos;
- estables;
- descriptivos;
- tipados;
- versionables cuando proceda.

Formato recomendado:

```text
<TIPO>-<DOMINIO>-<IDENTIFICADOR>
```

Ejemplos:

```text
ENGINE-RETRIEVAL-HYBRID
CAP-HYBRID-RETRIEVAL
EXEC-000041
DOC-000123
COL-000010
REL-000081
```

---

# Prefijos

Los prefijos deberán documentarse en `CONVENCIONES.md` o `GLOSARIO.md`.

Ejemplos iniciales:

| Prefijo | Significado |
|---|---|
| `DOC` | Documento |
| `COMP` | Componente |
| `REL` | Relación |
| `COL` | Colección |
| `KG` | Knowledge Graph |
| `ENGINE` | Engine |
| `CAP` | Capability |
| `EXEC` | Execution |
| `ACT` | Activity |
| `WF` | Workflow |
| `QG` | Quality Gate |
| `DIAG` | Diagnóstico |

---

# IDs de ejemplo

Los ejemplos deberán distinguirse claramente de IDs reales.

Se recomienda utilizar:

```text
000001
000041
EXAMPLE
DEMO
```

No deberán reutilizarse IDs reales del repositorio sin necesidad.

---

# Convención de versiones

Las especificaciones deberán utilizar Semantic Versioning cuando sea aplicable:

```text
MAJOR.MINOR.PATCH
```

---

# Versión mayor

Se incrementará cuando exista:

- cambio incompatible;
- modificación de contratos;
- redefinición de entidades;
- eliminación de comportamiento;
- cambio de autoridad conceptual.

Ejemplo:

```text
1.4.0
→
2.0.0
```

---

# Versión menor

Se incrementará cuando se añada:

- nueva sección;
- nueva entidad compatible;
- nueva capacidad;
- nuevo caso de uso;
- regla compatible.

Ejemplo:

```text
1.4.0
→
1.5.0
```

---

# Versión patch

Se incrementará para:

- erratas;
- enlaces;
- aclaraciones;
- ejemplos;
- mejoras editoriales;
- correcciones no contractuales.

Ejemplo:

```text
1.4.0
→
1.4.1
```

---

# Versión documental frente a versión de contrato

No deberán confundirse:

```text
versión del documento
```

con:

```text
versión de una API, Contract, Engine o Schema
```

Ejemplo:

```yaml
document:
  version: 1.3.0

api_contract:
  version: 2.0.0
```

---

# Versionado por partes

Cuando una especificación se redacte por partes, la numeración deberá ser consecutiva y completa.

Ejemplo correcto:

```text
Parte I
Parte II
Parte III
Parte IV
Parte V
```

Ejemplo incorrecto:

```text
Parte I
Parte II
Parte III
Parte V
```

---

# Revisión de numeración

Antes de cerrar una especificación deberá comprobarse:

- que no falten partes;
- que no existan partes duplicadas;
- que la transición entre partes sea correcta;
- que el índice coincida con el contenido;
- que el cierre indique el número total real.

---

# Convención de estados documentales

Estados recomendados:

```text
draft
review
approved
implementation_ready
implemented
deprecated
retired
```

---

# Estado `draft`

El documento:

- está en construcción;
- puede cambiar;
- no debe tomarse como contrato definitivo.

---

# Estado `review`

El contenido está completo y pendiente de revisión.

---

# Estado `approved`

La arquitectura ha sido aprobada.

---

# Estado `implementation_ready`

El documento contiene detalle suficiente para implementación.

---

# Estado `implemented`

Existe implementación alineada con la especificación.

---

# Estado `deprecated`

El documento continúa disponible, pero no se recomienda para nuevas implementaciones.

---

# Estado `retired`

Se conserva únicamente por trazabilidad histórica.

---

# Transiciones de estado

Flujo recomendado:

```text
draft
    ↓
review
    ↓
approved
    ↓
implementation_ready
    ↓
implemented
```

Ramas alternativas:

```text
approved
    ↓
deprecated
    ↓
retired
```

---

# Estado y madurez

El estado documental y el nivel de madurez son conceptos diferentes.

Ejemplo:

```text
status = review
maturity = level 4
```

Una especificación puede ser extensa y madura, pero seguir pendiente de revisión formal.

---

# Cabecera recomendada

Cada especificación deberá comenzar con una cabecera homogénea.

Ejemplo:

```yaml
---
id: SPEC-ENGINE-REGISTRY
title: Especificación del Engine Registry
version: 1.0.0
status: review
domain: runtime
owners:
  conceptual: TEAM-ARCHITECTURE
  technical: TEAM-PLATFORM
created: 2026-08-02
updated: 2026-08-02
review_cycle: P90D
tags:
  - engine-registry
  - runtime
  - discovery
---
```

---

# Campos mínimos de cabecera

Se recomienda incluir:

```text
id
title
version
status
domain
owners
created
updated
tags
```

---

# Campos opcionales

```text
reviewers
review_cycle
dependencies
consumed_by
supersedes
superseded_by
adr
maturity
```

---

# Estructura interna recomendada

No todas las especificaciones deberán ser idénticas, pero se recomienda el siguiente patrón:

```text
1. Introducción
2. Objetivos
3. Problema que resuelve
4. Alcance
5. Fuera de alcance
6. Principios
7. Arquitectura conceptual
8. Modelo de dominio
9. Entidades
10. Contratos
11. Lifecycle
12. Reglas
13. Integraciones
14. Seguridad
15. Observabilidad
16. Eventos
17. Diagnósticos
18. Quality Gates
19. Casos de uso
20. Antipatrones
21. Reglas de conformidad
22. Checklist
23. Conclusión
```

---

# Índice

Los documentos extensos deberían disponer de índice.

El índice podrá generarse mediante herramientas o mantenerse manualmente.

Deberá reflejar:

- partes;
- capítulos;
- secciones principales;
- enlaces internos válidos.

---

# Partición de documentos extensos

Durante la redacción, una especificación podrá dividirse en varias entregas.

Sin embargo, el archivo final deberá leerse como un único documento continuo.

---

# Convención de partes

Formato recomendado:

```markdown
# Parte I — Fundamentos
# Parte II — Modelo de dominio
# Parte III — Operación
```

No se recomienda comenzar cada parte con una nueva cabecera YAML.

La cabecera corresponde al documento completo.

---

# Transiciones entre partes

Cada parte podrá terminar con:

```text
Transición hacia la Parte siguiente
```

La última parte deberá cerrar el documento y declarar su estado.

---

# Convención de ejemplos

Los ejemplos deberán ser:

- válidos;
- coherentes;
- mínimos;
- representativos;
- claramente diferenciados de contratos normativos.

---

# Ejemplo normativo

Cuando un bloque sea obligatorio deberá indicarse.

Ejemplo:

```text
Formato requerido:
```

---

# Ejemplo ilustrativo

Cuando no sea normativo deberá declararse.

Ejemplo:

```text
Ejemplo orientativo:
```

---

# YAML

Los bloques YAML deberán:

- respetar indentación;
- utilizar claves consistentes;
- evitar valores ambiguos;
- conservar versionado cuando proceda.

---

# JSON

Los ejemplos JSON deberán ser sintácticamente válidos.

---

# Pseudocódigo

El pseudocódigo deberá diferenciarse claramente de código implementable.

---

# Diagramas textuales

Los diagramas ASCII deberán:

- mantener alineación;
- evitar anchura excesiva;
- reflejar el flujo real;
- utilizar nombres canónicos.

---

# Tablas

Las tablas deberán utilizarse cuando mejoren la comparación.

No deberán sustituir explicaciones necesarias.

---

# Contratos

Todo Contract deberá definir, cuando corresponda:

- ID;
- versión;
- input;
- output;
- errores;
- compatibilidad;
- ownership;
- lifecycle.

---

# Estados

Las máquinas de estados deberán:

- enumerar estados;
- declarar transiciones;
- declarar condiciones;
- declarar estados terminales;
- declarar errores.

---

# Eventos

Todo evento deberá definir:

- tipo;
- subject;
- timestamp;
- versión;
- datos;
- correlation;
- provenance.

---

# Diagnósticos

Los diagnósticos deberán utilizar códigos estables.

Formato recomendado:

```text
<DOMINIO>_<CONCEPTO>_<PROBLEMA>
```

Ejemplos:

```text
ENGINE_CONTRACT_INCOMPATIBLE
DOCUMENT_FRONT_MATTER_MISSING
RELATION_TARGET_NOT_FOUND
```

---

# Severidades

Valores recomendados:

```text
info
warning
error
critical
```

---

# Retryability

Cuando proceda, un diagnóstico deberá declarar:

```text
retryable: true
```

o:

```text
retryable: false
```

---

# Quality Gates

Los Quality Gates deberán:

- tener ID;
- estar versionados;
- declarar criterios;
- producir resultado;
- conservar evidencia.

---

# Formato

```yaml
quality_gate:
  id: QG-DOCUMENT-0001

  criteria:
    all:
      - schema_valid == true
      - references_valid == true
      - metadata_complete == true
```

---

# Conformidad

Cada documento deberá definir qué significa ser conforme.

La conformidad deberá expresarse mediante:

- reglas;
- Quality Gates;
- checklist;
- invariantes;
- criterios verificables.

---

# Antipatrones

Los antipatrones deberán:

- describir errores reales;
- explicar por qué son problemáticos;
- estar relacionados con el ámbito del documento.

No deberán convertirse en listas genéricas desconectadas.

---

# Referencias

Cada especificación deberá incluir una sección final de referencias cuando proceda.

Ejemplo:

```markdown
## Referencias

- [ARQUITECTURA](../architecture/ARQUITECTURA.md)
- [VISION](../VISION.md)
- [ADR](../governance/adr/README.md)
```

---

# Rutas relativas

Los enlaces deberán calcularse desde la ubicación real del documento.

Ejemplo desde `specifications/runtime/`:

```markdown
[Knowledge Graph](./knowledge/ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md)
```

---

# Enlaces internos

Los enlaces a secciones deberán utilizar anchors estables.

Se evitarán títulos que cambien con frecuencia cuando sean muy referenciados.

---

# Referencias rotas

No deberá aceptarse una modificación que introduzca enlaces rotos.

---

# Validación documental

Las especificaciones deberán pasar validaciones automáticas cuando exista soporte.

---

# Validaciones mínimas

```text
Front Matter válido
IDs únicos
Enlaces internos válidos
Enlaces relativos válidos
Archivos referenciados existentes
Numeración de partes correcta
Encabezados coherentes
Bloques YAML válidos
Duplicados detectados
Nombres canónicos correctos
```

---

# Herramientas

El proyecto podrá utilizar:

```text
validate_all.py
validate_semantics.py
generate_graph.py
build_site_docs.py
```

según el alcance de cada documento.

---

# `validate_all.py`

Deberá comprobar, al menos:

- Front Matter;
- IDs;
- enlaces;
- estructura;
- referencias.

---

# `validate_semantics.py`

Podrá comprobar:

- tipos;
- dependencias;
- authority map;
- relaciones;
- campos obligatorios;
- conflictos terminológicos.

---

# `generate_graph.py`

Podrá generar:

- grafo documental;
- relaciones;
- estadísticas;
- huérfanos;
- dependencias.

---

# `build_site_docs.py`

Podrá generar documentación navegable.

---

# Validación manual

La automatización no sustituye revisión humana.

Deberán revisarse manualmente:

- coherencia conceptual;
- autoridad;
- duplicidad;
- contradicciones;
- claridad;
- utilidad para implementación.

---

# Quality Gate documental

Se recomienda un Gate común.

```yaml
quality_gate:
  id: QG-SPECIFICATION-DOCUMENT-0001

  criteria:
    all:
      - front_matter_valid == true
      - canonical_name_valid == true
      - document_id_unique == true
      - version_valid == true
      - status_valid == true
      - domain_valid == true
      - ownership_defined == true
      - headings_consistent == true
      - parts_consecutive == true
      - internal_links_valid == true
      - external_references_valid == true
      - yaml_examples_valid == true
      - terminology_consistent == true
      - authoritative_scope_defined == true
      - dependencies_declared == true
      - conformity_defined == true
```

---

# Quality Gate de referencias

```yaml
quality_gate:
  id: QG-SPECIFICATION-REFERENCES-0001

  criteria:
    all:
      - relative_paths_valid == true
      - referenced_files_exist == true
      - renamed_files_updated == true
      - no_circular_authority == true
      - references_use_canonical_names == true
```

---

# Quality Gate de numeración

```yaml
quality_gate:
  id: QG-SPECIFICATION-PARTS-0001

  criteria:
    all:
      - part_numbers_unique == true
      - part_numbers_consecutive == true
      - declared_total_matches == true
      - transitions_match_next_part == true
      - final_part_closes_document == true
```

---

# Control de cambios

Todo cambio relevante deberá quedar trazado.

---

# Tipos de cambio

```text
editorial
compatible
breaking
structural
rename
deprecation
retirement
```

---

# Cambio editorial

No modifica contratos ni semántica.

Ejemplos:

- erratas;
- formato;
- enlaces;
- aclaraciones.

---

# Cambio compatible

Añade contenido sin romper consumidores.

---

# Cambio incompatible

Modifica:

- contratos;
- semántica;
- IDs;
- estados;
- invariantes;
- authority.

---

# Cambio estructural

Incluye:

- división de documento;
- movimiento de directorio;
- reorganización de dominios;
- nuevo mapa de autoridad.

---

# Registro de cambios

Podrá incluirse una sección:

```markdown
# Historial de cambios
```

---

# Formato recomendado

```markdown
| Versión | Fecha | Tipo | Descripción |
|---|---|---|---|
| 1.0.0 | 2026-08-02 | initial | Primera versión |
| 1.0.1 | 2026-08-03 | editorial | Corrección de enlaces |
| 1.1.0 | 2026-08-10 | compatible | Añadido lifecycle |
```

---

# Relación con Git

Los cambios documentales deberán utilizar commits descriptivos.

Ejemplos:

```text
docs(specifications): add specifications README
docs(knowledge): fix Knowledge Graph filename
docs(apis): correct part numbering
docs(retrieval): normalize part numbering
```

---

# Pull Requests

Los cambios relevantes deberían incluir:

- propósito;
- documentos afectados;
- impacto;
- compatibilidad;
- validaciones ejecutadas;
- enlaces modificados;
- ADR relacionado.

---

# Revisión documental

Cada especificación deberá revisarse según criticidad.

---

# Ciclos recomendados

```text
critical runtime: P90D
security: P90D
interfaces: P120D
knowledge: P180D
stable foundational: P365D
```

---

# Eventos que obligan a revisión

- nueva versión mayor;
- cambio de arquitectura;
- incidente;
- vulnerabilidad;
- implementación divergente;
- nuevo consumidor;
- deprecation;
- migración;
- nuevo ADR.

---

# Ownership

Cada especificación deberá tener owner.

---

# Responsabilidades del owner

- mantener contenido;
- resolver contradicciones;
- revisar cambios;
- aprobar versiones;
- actualizar dependencias;
- coordinar migraciones;
- iniciar deprecation.

---

# Documento huérfano

Una especificación sin owner deberá:

- generar warning;
- bloquear promoción de estado;
- asignarse temporalmente al equipo de arquitectura;
- revisarse.

---

# Gobernanza

La evolución de las especificaciones deberá integrarse con:

- Architecture Board;
- ADR;
- Roadmap;
- Release Process;
- Quality Pipeline.

---

# ADR obligatorio

Deberá considerarse ADR cuando un cambio:

- altera límites de dominio;
- cambia fuente autoritativa;
- introduce nuevo componente crítico;
- modifica contratos transversales;
- cambia estrategia de seguridad;
- cambia persistencia o consistencia;
- divide o fusiona especificaciones.

---

# No todo cambio requiere ADR

No será necesario para:

- erratas;
- enlaces;
- ejemplos;
- aclaraciones;
- cambios editoriales.

---

# Deprecation documental

Una especificación deprecated deberá declarar:

- razón;
- fecha;
- sustitución;
- periodo de transición;
- consumidores afectados;
- versión final soportada.

---

# Retirada

Una especificación retirada no deberá eliminarse inmediatamente.

Deberá:

- mantenerse en archivo;
- conservar historial;
- enlazar sustitución;
- excluirse de nuevas implementaciones;
- preservar referencias históricas.

---

# Movimiento de archivos

Mover una especificación entre directorios deberá tratarse como cambio estructural.

---

# Requisitos

- justificar nuevo dominio;
- actualizar enlaces;
- actualizar README;
- actualizar mapa de dependencias;
- mantener redirect documental cuando sea posible;
- validar site build.

---

# Directorios futuros

No deberán crearse directorios vacíos.

Un nuevo dominio se justificará cuando exista:

- responsabilidad diferenciada;
- al menos una especificación real;
- ownership;
- dependencias claras;
- evolución independiente.

---

# Mantenimiento del README

Este README deberá actualizarse cuando:

- se cree una especificación;
- se retire una especificación;
- se mueva un archivo;
- cambie un dominio;
- cambie el orden de lectura;
- cambie la matriz de autoridad;
- cambie el modelo de madurez.

---

# Mantenimiento del catálogo

La tabla de especificaciones deberá reflejar siempre el estado real del repositorio.

---

# No usar el README como duplicado

El README debe:

- orientar;
- resumir;
- enlazar;
- definir convenciones.

No debe reproducir el contenido completo de cada especificación.

---

# Checklist para una nueva especificación

```text
[ ] El nuevo componente no está ya cubierto.
[ ] Existe responsabilidad propia.
[ ] Existe owner.
[ ] Existe dominio adecuado.
[ ] El nombre de archivo es canónico.
[ ] El ID documental es único.
[ ] La cabecera está completa.
[ ] El propósito está definido.
[ ] El alcance está definido.
[ ] El fuera de alcance está definido.
[ ] La autoridad conceptual está definida.
[ ] Las dependencias están declaradas.
[ ] Los contratos están identificados.
[ ] El lifecycle está definido.
[ ] Los diagnósticos están definidos cuando proceda.
[ ] Los Quality Gates están definidos.
[ ] La conformidad está definida.
[ ] Las referencias son válidas.
[ ] El README se ha actualizado.
[ ] El mapa de dependencias se ha actualizado.
[ ] Se ha determinado si requiere ADR.
[ ] Las validaciones automáticas han pasado.
```

---

# Checklist para modificar una especificación

```text
[ ] Se ha clasificado el tipo de cambio.
[ ] Se ha actualizado la versión.
[ ] Se ha actualizado la fecha.
[ ] Se han identificado consumidores.
[ ] Se han revisado contratos.
[ ] Se ha evaluado compatibilidad.
[ ] Se han actualizado referencias.
[ ] Se ha actualizado el historial.
[ ] Se ha ejecutado validate_all.py.
[ ] Se ha ejecutado validación semántica cuando procede.
[ ] Se ha revisado el impacto en ADR.
[ ] Se ha actualizado el README si procede.
[ ] Se ha actualizado el mapa de dependencias.
```

---

# Checklist para renombrar una especificación

```text
[ ] Se ha definido el nuevo nombre canónico.
[ ] Se ha renombrado el archivo.
[ ] Se han actualizado todos los enlaces.
[ ] Se han actualizado referencias en ADR.
[ ] Se ha actualizado README.
[ ] Se ha actualizado navegación.
[ ] Se ha actualizado site_docs.
[ ] Se ha validado el repositorio.
[ ] No quedan referencias al nombre anterior.
[ ] Se ha registrado el cambio.
```

---

# Checklist para cerrar una especificación

```text
[ ] Todas las partes están presentes.
[ ] La numeración es consecutiva.
[ ] El total de partes coincide.
[ ] La conclusión está completa.
[ ] El estado documental es correcto.
[ ] La versión es correcta.
[ ] Los owners están definidos.
[ ] Las dependencias están actualizadas.
[ ] Los casos de uso están cubiertos.
[ ] Los antipatrones están cubiertos.
[ ] Las reglas de conformidad están completas.
[ ] El checklist interno está completo.
[ ] Las referencias son válidas.
[ ] Los Quality Gates están definidos.
[ ] La validación automática ha pasado.
[ ] La revisión manual ha pasado.
```

---

# Diagnósticos documentales

Catálogo inicial recomendado:

```text
SPEC_FRONT_MATTER_MISSING
SPEC_DOCUMENT_ID_DUPLICATE
SPEC_VERSION_INVALID
SPEC_STATUS_INVALID
SPEC_DOMAIN_INVALID
SPEC_OWNER_MISSING
SPEC_CANONICAL_NAME_INVALID
SPEC_FILENAME_TYPO
SPEC_PART_NUMBER_DUPLICATE
SPEC_PART_NUMBER_GAP
SPEC_DECLARED_PART_COUNT_MISMATCH
SPEC_INTERNAL_LINK_BROKEN
SPEC_REFERENCE_TARGET_MISSING
SPEC_REFERENCE_USES_NON_CANONICAL_NAME
SPEC_YAML_EXAMPLE_INVALID
SPEC_TERMINOLOGY_INCONSISTENT
SPEC_AUTHORITY_AMBIGUOUS
SPEC_DEPENDENCY_UNDECLARED
SPEC_DEPENDENCY_CYCLE
SPEC_CONTRACT_DUPLICATED
SPEC_CHANGELOG_MISSING
SPEC_REVIEW_OVERDUE
SPEC_DEPRECATED_WITHOUT_REPLACEMENT
SPEC_RETIRED_STILL_REFERENCED
```

---

# Diagnostic Contract

```yaml
specification_diagnostic:
  id: SPEC-DIAGNOSTIC-000041

  code: SPEC_PART_NUMBER_GAP
  severity: error

  document:
    path: specifications/interfaces/ESPECIFICACION_DE_APIS.md

  details:
    detected_parts:
      - I
      - II
      - III
      - IV
      - VI

    missing:
      - V

  retryable: false
```

---

# Métricas documentales

El proyecto podrá medir:

- número de especificaciones;
- documentos por dominio;
- nivel de madurez;
- enlaces válidos;
- enlaces rotos;
- documentos sin owner;
- revisiones vencidas;
- diagnósticos;
- dependencias;
- Quality Gates superados;
- documentos implementados;
- divergencias implementación-especificación.

---

# Indicadores recomendados

```text
specifications_total
specifications_by_domain
specifications_by_status
specifications_by_maturity
broken_links_total
documents_without_owner
overdue_reviews
validation_failures
dependency_cycles
implementation_alignment
```

---

# Dashboard documental

Podrá mostrar:

- catálogo;
- estado;
- madurez;
- owner;
- revisión;
- dependencias;
- errores;
- últimas modificaciones.

---

# Deuda documental

Se considerará deuda documental:

- especificación incompleta;
- contrato duplicado;
- autoridad ambigua;
- enlace roto;
- owner inexistente;
- revisión vencida;
- implementación divergente;
- nombres inconsistentes;
- falta de Quality Gates;
- falta de deprecation plan.

---

# Registro de deuda

Podrá integrarse con:

```text
KNOWN_ISSUES
KNOWLEDGE_DEBT
ROADMAP
BITACORA
```

---

# Priorización de deuda

Orden recomendado:

```text
1. Contradicciones
2. Seguridad
3. Contratos rotos
4. Authority ambiguity
5. Enlaces rotos
6. Owners ausentes
7. Revisiones vencidas
8. Mejoras editoriales
```

---

# Conformidad del directorio `specifications/`

El directorio será conforme cuando:

- todas las especificaciones estén catalogadas;
- los dominios sean coherentes;
- los nombres sean canónicos;
- los archivos existan;
- los enlaces sean válidos;
- los owners estén definidos;
- las versiones sean válidas;
- los estados sean válidos;
- las partes sean consecutivas;
- las dependencias estén documentadas;
- no existan ciclos de autoridad;
- las referencias utilicen rutas reales;
- los Quality Gates documentales hayan pasado;
- el README represente el estado real.

---

# Quality Gate global

```yaml
quality_gate:
  id: QG-SPECIFICATIONS-REPOSITORY-0001

  criteria:
    all:
      - readme_exists == true
      - catalog_complete == true
      - domains_valid == true
      - canonical_filenames_valid == true
      - front_matter_complete == true
      - document_ids_unique == true
      - versions_valid == true
      - statuses_valid == true
      - owners_present == true
      - parts_consecutive == true
      - internal_links_valid == true
      - external_references_valid == true
      - no_authority_cycles == true
      - dependencies_declared == true
      - no_orphan_specifications == true
      - review_dates_current == true
      - validation_pipeline_passed == true
```

---

# Orden inmediato de saneamiento

Tras crear este README se recomienda ejecutar:

```text
1. Renombrar el archivo del Knowledge Graph.
2. Actualizar todas sus referencias.
3. Corregir la numeración de ESPECIFICACION_DE_APIS.md.
4. Corregir la numeración de ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md.
5. Ejecutar validate_all.py.
6. Corregir enlaces rotos.
7. Normalizar cabeceras.
8. Crear GLOSARIO.md.
9. Crear CONVENCIONES.md.
10. Crear DEPENDENCIAS.md.
```

---

# Estructura objetivo inmediata

```text
specifications/

├── README.md
├── GLOSARIO.md
├── CONVENCIONES.md
├── DEPENDENCIAS.md
│
├── ingestion/
├── interfaces/
├── knowledge/
└── runtime/
```

Los tres documentos transversales solo deberán añadirse cuando estén realmente redactados.

---

# Estado inicial del catálogo

```text
Especificaciones totales:
15

Dominios:
4

Knowledge:
6

Ingestion:
1

Runtime:
7

Interfaces:
1
```

---

# Arquitectura documental final

```text
VISION
    ↓
ARQUITECTURA
    ↓
ADR
    ↓
SPECIFICATIONS README
    ↓
┌───────────────┬───────────────┬───────────────┬───────────────┐
│               │               │               │               │
Knowledge    Ingestion       Runtime        Interfaces      Transversal
│               │               │               │               │
Ontology      Sources       Orchestrator       APIs          Glossary
Documents     Pipeline      Registry                         Conventions
Components    Staging       Engines                          Dependencies
Relations                   Execution
Collections                 Retrieval
Graph                       RAG
```

---

# Checklist global del README

```text
[ ] El objetivo del directorio está definido.
[ ] La filosofía está definida.
[ ] El alcance está definido.
[ ] Los dominios están definidos.
[ ] Las especificaciones están catalogadas.
[ ] Las responsabilidades están descritas.
[ ] Las fuentes autoritativas están declaradas.
[ ] Las dependencias están descritas.
[ ] Los límites entre componentes están definidos.
[ ] Las rutas de lectura están incluidas.
[ ] El modelo de madurez está definido.
[ ] Los estados documentales están definidos.
[ ] Los criterios para nuevas especificaciones están definidos.
[ ] Las convenciones de archivos están definidas.
[ ] Las convenciones de IDs están definidas.
[ ] El versionado está definido.
[ ] La estructura interna está recomendada.
[ ] Los contratos están normalizados.
[ ] Los eventos están normalizados.
[ ] Los diagnósticos están normalizados.
[ ] Los Quality Gates están definidos.
[ ] La validación automática está descrita.
[ ] La revisión manual está descrita.
[ ] El control de cambios está definido.
[ ] La relación con Git está definida.
[ ] La gobernanza está definida.
[ ] La deprecation está definida.
[ ] Los movimientos de archivo están gobernados.
[ ] Los checklists están incluidos.
[ ] Las métricas documentales están definidas.
[ ] La deuda documental está definida.
[ ] La conformidad global está definida.
[ ] Las incidencias conocidas están registradas.
[ ] El orden de saneamiento está definido.
```

---

# Referencias

- [ARQUITECTURA](../architecture/ARQUITECTURA.md)
- [VISION](../VISION.md)
- [ROADMAP](../management/ROADMAP.md)
- [ADR](../governance/adr/README.md)
- [PROJECT_STATUS](../management/PROJECT_STATUS.md)
- [KNOWN_ISSUES](../management/KNOWN_ISSUES.md)
- [BITACORA](../management/BITACORA.md)

---

# Estado final del documento

```text
Documento:
specifications/README.md

Versión:
1.0.0

Estado:
review

Dominio:
Documentación transversal

Partes:
3 / 3

Estado de madurez:
Nivel 4 — Especificación completa

Especificación:
FINALIZADA
```

---

# Conclusión

El directorio `specifications/` constituye el catálogo formal de contratos, dominios y componentes del SGCC.

Este README define:

- qué contiene;
- cómo se organiza;
- cómo debe leerse;
- cómo deben nombrarse los documentos;
- cómo deben versionarse;
- cómo deben validarse;
- cómo deben evolucionar;
- cómo se gobiernan;
- qué significa que sean conformes.

Su función principal puede resumirse así:

```text
Orientar
    ↓
Catalogar
    ↓
Relacionar
    ↓
Normalizar
    ↓
Validar
    ↓
Gobernar
    ↓
Evolucionar
```

El dominio `knowledge` define qué conocimiento existe.

El dominio `ingestion` define cómo entra.

El dominio `runtime` define cómo se procesa.

El dominio `interfaces` define cómo se expone.

Las convenciones garantizan consistencia.

El versionado permite evolución.

Los estados declaran madurez.

Las dependencias permiten analizar impacto.

Los Quality Gates aseguran calidad.

La validación evita errores estructurales.

La gobernanza mantiene coherencia a largo plazo.

Un repositorio de especificaciones correctamente mantenido deberá poder responder:

```text
¿Qué documentos existen?

¿Qué responsabilidad tiene cada uno?

¿Cuál es la fuente autoritativa de un concepto?

¿Qué documentos dependen de otro?

¿Qué orden de lectura se recomienda?

¿Qué versión está vigente?

¿Qué estado posee cada especificación?

¿Quién es su owner?

¿Qué contratos define?

¿Qué Quality Gates debe superar?

¿Qué cambios son compatibles?

¿Qué cambios requieren ADR?

¿Qué enlaces se verán afectados por un renombrado?

¿Qué deuda documental existe?

¿Qué debe corregirse antes de implementar?
```

Con esta tercera parte queda completado `specifications/README.md` como puerta de entrada, catálogo maestro y marco de gobierno documental de las especificaciones de NovaCoquinaria.
