---
id: SPEC-ORQUESTADOR-EJECUCION
titulo: Especificación del Orquestador de Ejecución
tipo: especificacion
version: 1.0.0
estado: borrador
propietarios:
  - NovaCoquinaria Architecture Team
creado: 2026-08-02
ultima_revision: 2026-08-02
tags:
  - orchestration
  - execution
  - workflows
  - pipelines
  - jobs
  - sagas
  - architecture
---

# Parte I — Fundamentos, arquitectura, alcance y responsabilidades del Orquestador de Ejecución

# Introducción

NovaCoquinaria dispone de múltiples motores especializados capaces de realizar operaciones concretas sobre el conocimiento culinario.

Entre ellos se encuentran:

- Ingestion Engine;
- Validation Engine;
- Knowledge Graph;
- Reasoning Engine;
- Indexing Engine;
- Retrieval Engine;
- Motor RAG;
- API Layer;
- Event Bus;
- Policy Engine;
- futuros Agent Engine y Workflow Engine.

Cada uno de estos subsistemas posee responsabilidades bien delimitadas.

Sin embargo, muchos procesos reales de NovaCoquinaria no pueden resolverse mediante la ejecución aislada de un único motor.

Por ejemplo, la incorporación de una nueva receta puede requerir:

```text
Recibir documento
        ↓
Validar formato
        ↓
Extraer componentes
        ↓
Resolver relaciones
        ↓
Actualizar Knowledge Graph
        ↓
Generar unidades indexables
        ↓
Construir índices
        ↓
Validar snapshot
        ↓
Publicar
```

La respuesta a una consulta compleja puede requerir:

```text
Recibir solicitud
        ↓
Aplicar políticas
        ↓
Ejecutar Retrieval
        ↓
Comprobar cobertura
        ↓
Invocar Reasoner
        ↓
Recuperar evidencia adicional
        ↓
Construir contexto
        ↓
Ejecutar RAG
        ↓
Validar respuesta
        ↓
Entregar resultado
```

Una operación de mantenimiento puede requerir:

```text
Detectar cambio de ontología
        ↓
Calcular impacto
        ↓
Invalidar inferencias
        ↓
Reprocesar relaciones
        ↓
Reconstruir índices afectados
        ↓
Ejecutar benchmarks
        ↓
Promover snapshot
```

Estos procesos necesitan un componente capaz de:

- conocer el flujo completo;
- decidir qué motores intervienen;
- controlar el orden;
- gestionar dependencias;
- ejecutar pasos en paralelo;
- mantener el estado;
- reaccionar ante fallos;
- aplicar reintentos;
- ejecutar compensaciones;
- emitir eventos;
- auditar decisiones;
- garantizar que el proceso finaliza de manera coherente.

Esta responsabilidad corresponde al:

```text
Orquestador de Ejecución
```

También podrá denominarse:

```text
Execution Orchestrator
```

o:

```text
Execution Engine
```

En esta especificación se utilizará preferentemente:

```text
Orquestador de Ejecución
```

porque describe con mayor precisión su función principal:

> Coordinar la ejecución de capacidades distribuidas sin sustituir las responsabilidades internas de cada motor.

El Orquestador no será un nuevo motor de conocimiento.

No deberá:

- validar documentos;
- construir índices;
- recuperar evidencia;
- generar respuestas;
- realizar inferencias;
- modificar directamente el Knowledge Graph.

Su función será dirigir, supervisar y gobernar cómo colaboran los motores especializados.

---

# Objetivos

Esta especificación persigue los siguientes objetivos generales:

- definir el Orquestador de Ejecución;
- establecer su papel dentro de NovaCoquinaria;
- separar orquestación y lógica de dominio;
- formalizar ejecuciones;
- definir workflows;
- definir pipelines;
- formalizar pasos y dependencias;
- establecer estados;
- coordinar motores;
- gestionar eventos;
- formalizar triggers;
- establecer scheduling;
- gestionar jobs;
- controlar concurrencia;
- permitir paralelismo;
- soportar ejecución distribuida;
- definir reintentos;
- establecer compensaciones;
- formalizar Sagas;
- gestionar timeouts;
- permitir cancelaciones;
- establecer prioridades;
- definir presupuestos;
- garantizar idempotencia;
- permitir reanudación;
- establecer checkpoints;
- definir observabilidad;
- formalizar auditoría;
- aplicar seguridad;
- integrar políticas;
- establecer Quality Gates;
- definir APIs administrativas;
- preparar integración con agentes;
- establecer reglas de conformidad;
- definir evolución y madurez.

---

# Problema que resuelve

Sin un Orquestador de Ejecución, los motores de NovaCoquinaria podrían quedar conectados mediante:

- llamadas directas;
- scripts;
- lógica duplicada;
- dependencias implícitas;
- procesos manuales;
- cron jobs aislados;
- eventos sin correlación;
- secuencias difíciles de reanudar.

Esto generaría problemas como:

- acoplamiento;
- falta de trazabilidad;
- reintentos inconsistentes;
- duplicación de operaciones;
- estados parciales;
- imposibilidad de compensar;
- dificultad para conocer qué ocurrió;
- workflows imposibles de versionar;
- fallos difíciles de reproducir;
- procesos no auditables.

El Orquestador deberá resolver estos problemas proporcionando una capa explícita de ejecución.

---

# Definición

Se define el **Orquestador de Ejecución** como:

> El subsistema responsable de planificar, iniciar, coordinar, supervisar, reanudar, cancelar y finalizar procesos compuestos por múltiples pasos y motores, preservando dependencias, estado, políticas, seguridad, observabilidad e idempotencia.

---

# Principio central

El Orquestador deberá responder siempre a las siguientes preguntas:

```text
¿Qué proceso se está ejecutando?

¿Por qué se inició?

¿Qué versión del workflow utiliza?

¿Qué pasos contiene?

¿Qué motores intervienen?

¿Qué paso se encuentra activo?

¿Qué dependencias existen?

¿Qué estado posee cada paso?

¿Qué datos recibe cada paso?

¿Qué resultados produce?

¿Qué políticas se aplican?

¿Qué presupuesto consume?

¿Qué ocurre si falla?

¿Qué puede reintentarse?

¿Qué debe compensarse?

¿Cómo puede reanudarse?

¿Cómo puede cancelarse?

¿Qué evidencia de ejecución queda registrada?
```

---

# Posición dentro de NovaCoquinaria

```text
                        Consumers
                             │
              ┌──────────────┼──────────────┐
              │              │              │
             API           Agents        Scheduler
              │              │              │
              └──────────────┼──────────────┘
                             │
                             ▼
              ═════════════════════════════
                 ORQUESTADOR DE EJECUCIÓN
              ═════════════════════════════
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
 Ingestion Engine     Validation Engine     Policy Engine
        │                    │                    │
        ├────────────────────┼────────────────────┤
        │                    │                    │
        ▼                    ▼                    ▼
 Knowledge Graph      Reasoning Engine      Indexing Engine
        │                    │                    │
        ├────────────────────┼────────────────────┤
        │                    │                    │
        ▼                    ▼                    ▼
 Retrieval Engine        RAG Engine          Event Bus
```

El Orquestador no deberá convertirse en intermediario obligatorio para todas las llamadas simples.

Una consulta directa a una API podrá utilizar un motor sin workflow complejo cuando:

- no exista coordinación multi-step;
- no se necesite estado persistente;
- no se requieran compensaciones;
- no se necesite reanudación.

---

# Alcance

El Orquestador será responsable de:

- iniciar ejecuciones;
- resolver definiciones de workflow;
- validar inputs;
- aplicar políticas;
- crear contexto;
- programar pasos;
- resolver dependencias;
- ejecutar tareas;
- coordinar motores;
- controlar concurrencia;
- gestionar estados;
- almacenar checkpoints;
- aplicar reintentos;
- gestionar timeouts;
- ejecutar compensaciones;
- emitir eventos;
- recopilar métricas;
- cerrar ejecuciones;
- producir resultados;
- conservar auditoría.

---

# Fuera de alcance

El Orquestador no será responsable de:

- lógica culinaria;
- validación semántica interna;
- parsing de documentos;
- generación de embeddings;
- construcción física de índices;
- ranking de candidatos;
- generación de respuestas;
- inferencia de conocimiento;
- autorización de dominio;
- almacenamiento canónico;
- implementación interna de los motores.

---

# Separación entre orquestación y coreografía

NovaCoquinaria podrá utilizar dos modelos de coordinación.

---

# Orquestación

Existe un componente central que conoce el workflow y dirige sus pasos.

```text
Orchestrator
    ├── Step A
    ├── Step B
    └── Step C
```

---

# Coreografía

Los componentes reaccionan a eventos sin un coordinador central que dirija toda la secuencia.

```text
Event A
    ↓
Service B
    ↓
Event B
    ↓
Service C
```

---

# Uso recomendado

La orquestación será preferible cuando:

- el flujo sea crítico;
- exista orden definido;
- existan compensaciones;
- se necesite estado;
- se requiera observabilidad completa;
- exista una salida final común.

---

# Coreografía recomendada

Será adecuada para:

- notificaciones;
- proyecciones;
- métricas;
- auditoría;
- side effects no críticos;
- actualizaciones desacopladas.

---

# Modelo híbrido

NovaCoquinaria podrá utilizar:

```text
Orquestación para el flujo principal
+
Coreografía para efectos secundarios
```

Ejemplo:

```text
Workflow de ingesta
        ↓
Publicación completada
        ↓
Evento
        ├── Actualizar métricas
        ├── Notificar
        └── Generar auditoría
```

---

# Principios arquitectónicos

Toda implementación del Orquestador deberá respetar los siguientes principios.

---

## Separación de responsabilidades

El Orquestador coordina.

Los motores ejecutan lógica especializada.

---

## Workflows declarativos

Los procesos deberán definirse mediante contratos versionados.

---

## Estado explícito

Toda ejecución deberá disponer de un estado observable.

---

## Pasos identificables

Cada paso deberá poseer:

- ID;
- tipo;
- inputs;
- outputs;
- políticas;
- estado.

---

## Dependencias explícitas

El orden no deberá depender de convenciones implícitas.

---

## Idempotencia

Toda operación reintentable deberá ser idempotente o disponer de protección equivalente.

---

## Reanudación

Las ejecuciones persistentes deberán poder continuar desde un checkpoint válido.

---

## Compensación

Las operaciones distribuidas deberán definir cómo revertir o neutralizar efectos cuando proceda.

---

## Inmutabilidad de definición

Una ejecución deberá conservar la versión exacta del workflow con la que se inició.

---

## Seguridad por diseño

Cada paso deberá ejecutarse con la identidad y los permisos mínimos necesarios.

---

## Política antes de ejecución

Las políticas deberán evaluarse antes de ejecutar operaciones sensibles.

---

## Presupuesto explícito

Toda ejecución deberá disponer de límites de:

- tiempo;
- coste;
- pasos;
- reintentos;
- concurrencia.

---

## Observabilidad completa

Toda ejecución deberá producir:

- logs;
- métricas;
- eventos;
- trazas;
- auditoría.

---

## Fallos como parte del diseño

Los errores no deberán tratarse como excepciones imprevisibles, sino como estados definidos.

---

## No estado oculto

El progreso no deberá depender únicamente de memoria local.

---

## Ejecución distribuida segura

El fallo de un worker no deberá corromper el workflow.

---

## Consistencia consciente

No deberá asumirse una transacción ACID entre motores distribuidos.

---

## Determinismo controlado

Las decisiones del Orquestador deberán ser reproducibles cuando los inputs y políticas no cambien.

---

## Evolución versionada

Los workflows, steps y políticas deberán evolucionar mediante versiones.

---

## Cancelación cooperativa

Los pasos deberán respetar señales de cancelación cuando sea posible.

---

## Backpressure

El Orquestador deberá limitar la presión sobre los motores dependientes.

---

## Fail Closed en seguridad

Si no puede verificarse identidad, tenant o policy, la ejecución deberá bloquearse.

---

# Arquitectura conceptual

```text
┌───────────────────────────────────────────────┐
│                 Trigger Layer                 │
│                                               │
│ API · Event · Schedule · Manual · Agent       │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Execution Gateway                │
│                                               │
│ Validation · Auth · Policy · Idempotency       │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Workflow Resolver                │
│                                               │
│ Definition · Version · Inputs · Compatibility │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Execution Coordinator             │
│                                               │
│ State · Dependencies · Scheduling · Budgets   │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                 Step Runtime                  │
│                                               │
│ Workers · Adapters · Engines · Activities     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│          State and Persistence Layer          │
│                                               │
│ Executions · Steps · Checkpoints · Results    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│          Observability and Governance         │
│                                               │
│ Events · Metrics · Audit · Quality Gates      │
└───────────────────────────────────────────────┘
```

---

# Componentes principales

El Orquestador podrá dividirse en los siguientes componentes.

```text
Execution Gateway
Workflow Registry
Workflow Resolver
Execution Coordinator
State Machine
Dependency Resolver
Step Scheduler
Worker Dispatcher
Activity Registry
Engine Adapter Registry
Policy Evaluator
Budget Controller
Retry Manager
Timeout Manager
Compensation Manager
Checkpoint Manager
Event Publisher
Result Aggregator
Audit Writer
Execution Monitor
```

---

# Execution Gateway

Punto de entrada de solicitudes.

Será responsable de:

- autenticar;
- autorizar;
- validar;
- resolver tenant;
- aplicar idempotency key;
- identificar trigger;
- crear Execution Request.

---

# Workflow Registry

Almacenará definiciones versionadas de workflows.

Deberá permitir:

- registrar;
- consultar;
- deprecar;
- validar;
- resolver compatibilidad.

---

# Workflow Resolver

Seleccionará:

- workflow;
- versión;
- profile;
- políticas;
- variables;
- capacidades requeridas.

---

# Execution Coordinator

Será el núcleo del Orquestador.

Coordinará:

- estado;
- pasos;
- dependencias;
- scheduling;
- resultados;
- fallos.

---

# State Machine

Gestionará las transiciones válidas de ejecución y steps.

---

# Dependency Resolver

Determinará qué pasos:

- están bloqueados;
- pueden ejecutarse;
- pueden paralelizarse;
- deben omitirse.

---

# Step Scheduler

Asignará trabajo en función de:

- prioridad;
- dependencias;
- capacidad;
- deadline;
- quotas.

---

# Worker Dispatcher

Enviará actividades a:

- workers;
- motores;
- colas;
- adaptadores.

---

# Activity Registry

Definirá actividades ejecutables por el Orquestador.

---

# Engine Adapter Registry

Contendrá adaptadores para invocar:

- Ingestion;
- Validation;
- Knowledge Graph;
- Reasoner;
- Indexing;
- Retrieval;
- RAG.

---

# Policy Evaluator

Aplicará políticas antes y durante la ejecución.

---

# Budget Controller

Controlará límites.

---

# Retry Manager

Aplicará políticas de reintento.

---

# Timeout Manager

Gestionará deadlines y timeouts.

---

# Compensation Manager

Ejecutará acciones compensatorias.

---

# Checkpoint Manager

Permitirá persistir progreso recuperable.

---

# Event Publisher

Emitirá eventos de dominio y operación.

---

# Result Aggregator

Construirá el resultado final a partir de outputs parciales.

---

# Audit Writer

Persistirá decisiones y acciones relevantes.

---

# Execution Monitor

Supervisará:

- estado;
- lag;
- bloqueos;
- fallos;
- consumo;
- salud.

---

# Dominios de ejecución

El Orquestador deberá soportar múltiples tipos de procesos.

---

# Knowledge Lifecycle

Procesos relacionados con conocimiento:

- ingesta;
- validación;
- publicación;
- actualización;
- eliminación;
- migración.

---

# Retrieval Lifecycle

Procesos relacionados con consultas:

- Retrieval;
- RAG;
- Reasoning;
- GraphRAG;
- agentes.

---

# Index Lifecycle

Procesos relacionados con índices:

- build;
- reindex;
- migration;
- activation;
- rollback;
- reconciliation.

---

# Maintenance Lifecycle

Procesos operativos:

- compactación;
- Garbage Collection;
- backups;
- health checks;
- reparaciones.

---

# Governance Lifecycle

Procesos de:

- aprobación;
- Quality Gates;
- auditoría;
- revisión;
- incidentes;
- excepciones.

---

# Agentic Lifecycle

Procesos futuros:

- tool selection;
- multi-agent coordination;
- plan execution;
- human approval;
- bounded autonomy.

---

# Tipos de ejecución

Valores iniciales:

```text
synchronous
asynchronous
scheduled
event_driven
manual
interactive
batch
streaming
long_running
compensating
recovery
```

---

# Synchronous Execution

El consumidor espera el resultado en la misma interacción.

Adecuada para:

- validaciones rápidas;
- retrieval simple;
- operaciones de baja latencia.

---

# Asynchronous Execution

Devuelve un Execution ID.

Adecuada para:

- ingesta;
- indexación;
- migraciones;
- workflows prolongados.

---

# Scheduled Execution

Se inicia mediante una programación.

---

# Event-Driven Execution

Se inicia al recibir un evento.

---

# Manual Execution

Se inicia mediante una acción administrativa.

---

# Interactive Execution

Puede requerir:

- aclaraciones;
- aprobación;
- input humano;
- decisiones intermedias.

---

# Batch Execution

Procesa colecciones o lotes.

---

# Streaming Execution

Produce resultados parciales.

---

# Long-Running Execution

Puede durar:

- minutos;
- horas;
- días.

Deberá persistir estado.

---

# Compensating Execution

Ejecuta acciones compensatorias.

---

# Recovery Execution

Recupera una ejecución fallida o interrumpida.

---

# Trigger

Un **Trigger** inicia una ejecución.

Formato recomendado:

```text
EXEC-TRIGGER-XXXXXX
```

---

# Tipos de trigger

```text
api
event
schedule
manual
system
agent
dependency
recovery
```

---

# Trigger Contract

```yaml
execution_trigger:
  id: EXEC-TRIGGER-000041

  type: event

  source:
    id: EVENT-DOCUMENT-PUBLISHED-000041

  requested_workflow:
    id: WF-KNOWLEDGE-INGESTION

  occurred_at: 2026-08-02T20:00:00Z
```

---

# API Trigger

Procede de una llamada autenticada.

---

# Event Trigger

Procede del Event Bus.

---

# Schedule Trigger

Procede del Scheduler.

---

# Manual Trigger

Procede de un operador.

---

# System Trigger

Lo inicia el propio sistema.

---

# Agent Trigger

Procede de un Agent Engine autorizado.

---

# Dependency Trigger

Una ejecución finalizada inicia otra.

---

# Recovery Trigger

Reanuda o reconstruye una ejecución.

---

# Trigger Validation

Deberá comprobar:

- identidad;
- origen;
- autorización;
- schema;
- idempotency;
- tenant;
- workflow permitido;
- timestamp;
- replay window.

---

# Execution Request

Toda ejecución deberá comenzar mediante una solicitud formal.

Formato recomendado:

```text
EXEC-REQUEST-XXXXXX
```

---

# Contrato

```yaml
execution_request:
  id: EXEC-REQUEST-000041

  workflow:
    id: WF-KNOWLEDGE-INGESTION
    version: 1.0.0

  trigger:
    id: EXEC-TRIGGER-000041

  requester:
    id: SERVICE-INGESTION-API
    type: service

  context:
    tenant: TENANT-0001
    environment: production

  inputs:
    document_id: DOC-0051

  options:
    priority: normal
    mode: asynchronous
    explain: true

  idempotency_key: ingest-DOC-0051-rev-17
```

---

# Campos mínimos

- request ID;
- workflow ID;
- trigger;
- requester;
- tenant;
- environment;
- inputs;
- mode.

---

# Campos opcionales

```text
workflow version
priority
deadline
budget
correlation ID
causation ID
idempotency key
labels
metadata
callback
```

---

# Idempotency Key

Deberá impedir ejecuciones duplicadas cuando una misma solicitud se repita.

---

# Scope

La clave deberá estar limitada por:

```text
tenant
+
workflow
+
operation
+
resource
```

---

# Duplicate Request

Podrá devolver:

- ejecución existente;
- resultado existente;
- conflicto;
- nueva ejecución;

según política.

---

# Execution

Una **Execution** representa una instancia concreta de un workflow.

Formato recomendado:

```text
EXEC-XXXXXX
```

---

# Contrato inicial

```yaml
execution:
  id: EXEC-000041

  request:
    id: EXEC-REQUEST-000041

  workflow:
    id: WF-KNOWLEDGE-INGESTION
    version: 1.0.0

  trigger:
    id: EXEC-TRIGGER-000041

  context:
    tenant: TENANT-0001
    environment: production

  state:
    status: created

  timing:
    created_at: 2026-08-02T20:00:01Z

  correlation:
    correlation_id: CORR-000041
    causation_id: EVENT-DOCUMENT-PUBLISHED-000041
```

---

# Execution ID

Deberá ser único y estable.

---

# Execution Context

La ejecución tendrá un contexto compartido.

Formato recomendado:

```text
EXEC-CONTEXT-XXXXXX
```

---

# Contenido

- tenant;
- environment;
- requester;
- workflow;
- trigger;
- policies;
- budget;
- deadlines;
- capabilities;
- correlation;
- variables;
- secrets references;
- observability context.

---

# Execution Context Contract

```yaml
execution_context:
  id: EXEC-CONTEXT-000041

  execution:
    id: EXEC-000041

  security:
    tenant: TENANT-0001
    principal: SERVICE-INGESTION-API
    policy_set: POLICY-SET-EXECUTION-0001

  environment:
    id: production

  budget:
    id: EXEC-BUDGET-000041

  correlation:
    trace_id: TRACE-000041
    correlation_id: CORR-000041

  variables:
    document_id: DOC-0051
    document_revision: 17
```

---

# Inmutabilidad

Los siguientes campos no deberán modificarse una vez iniciada la ejecución:

- tenant;
- requester;
- workflow version;
- trigger;
- idempotency key;
- base policies.

---

# Variables mutables

Podrán existir variables de ejecución controladas.

Ejemplos:

- step outputs;
- counters;
- checkpoints;
- flags;
- intermediate references.

---

# No usar contexto como almacenamiento arbitrario

Deberá limitarse mediante schema.

---

# Execution Result

Toda ejecución deberá producir un resultado formal.

Formato recomendado:

```text
EXEC-RESULT-XXXXXX
```

---

# Contrato preliminar

```yaml
execution_result:
  id: EXEC-RESULT-000041

  execution:
    id: EXEC-000041

  status: succeeded

  outputs:
    knowledge_snapshot_id: KG-SNAP-20260802-0001
    index_snapshot_id: IDX-SNAP-20260802-0001

  diagnostics:
    warnings: 1
    errors: 0

  completed_at: 2026-08-02T20:08:00Z
```

---

# Result Status

Valores iniciales:

```text
succeeded
succeeded_with_warnings
partial
failed
cancelled
timed_out
compensated
blocked
```

---

# Workflow

Un **Workflow** representa una definición versionada de proceso.

Formato recomendado:

```text
WF-XXXXXX
```

---

# Definición preliminar

```yaml
workflow:
  id: WF-KNOWLEDGE-INGESTION

  version: 1.0.0
  status: active

  name: Knowledge Ingestion Workflow

  trigger_types:
    - api
    - event
    - manual

  execution_mode: asynchronous

  inputs_schema:
    id: WF-KNOWLEDGE-INGESTION-INPUT
    version: 1.0.0

  outputs_schema:
    id: WF-KNOWLEDGE-INGESTION-OUTPUT
    version: 1.0.0
```

---

# Workflow Responsibilities

Una definición deberá declarar:

- inputs;
- outputs;
- steps;
- dependencias;
- condiciones;
- timeouts;
- reintentos;
- compensaciones;
- Quality Gates;
- permisos;
- budgets.

---

# Workflow Instance

La Execution será la instancia de un Workflow.

```text
Workflow Definition
        ↓
Execution
```

---

# Workflow Version

Toda ejecución deberá quedar fijada a una versión.

---

# No actualización in-place

Una ejecución iniciada con:

```text
WF-X@1.0.0
```

no deberá continuar con:

```text
WF-X@1.1.0
```

salvo migración explícita.

---

# Workflow Status

```text
draft
experimental
active
deprecated
retired
blocked
```

---

# Pipeline

Un **Pipeline** representa una secuencia orientada al procesamiento de datos.

---

# Diferencia conceptual

```text
Workflow
```

describe un proceso de negocio o sistema más amplio.

```text
Pipeline
```

describe una cadena de transformación.

---

# Ejemplo

Workflow:

```text
Publicar conocimiento
```

Pipeline interno:

```text
Parse
↓
Normalize
↓
Validate
↓
Transform
```

---

# Pipeline ID

Formato recomendado:

```text
PIPE-XXXXXX
```

---

# Activity

Una **Activity** representa una unidad ejecutable invocable por el Orquestador.

Formato recomendado:

```text
ACT-XXXXXX
```

---

# Ejemplos

```text
ACT-VALIDATE-DOCUMENT
ACT-BUILD-KNOWLEDGE-GRAPH
ACT-GENERATE-EMBEDDINGS
ACT-BUILD-INDEX
ACT-RUN-RETRIEVAL
ACT-GENERATE-RAG-RESPONSE
```

---

# Activity Contract

```yaml
activity:
  id: ACT-VALIDATE-DOCUMENT

  version: 1.0.0

  executor:
    type: engine_adapter
    target: VALIDATION-ENGINE

  input_schema:
    id: VALIDATION-REQUEST
    version: 1.0.0

  output_schema:
    id: VALIDATION-RESULT
    version: 1.0.0

  characteristics:
    idempotent: true
    cancellable: true
    retryable: true
```

---

# Step

Un **Step** será una instancia declarativa de una Activity dentro de un Workflow.

---

# Diferencia

```text
Activity
=
capacidad reutilizable
```

```text
Step
=
uso concreto de esa capacidad dentro de un workflow
```

---

# Step ID

Formato recomendado:

```text
STEP-XXXXXX
```

---

# Ejemplo

```yaml
workflow_step:
  id: STEP-VALIDATE-DOCUMENT

  activity:
    id: ACT-VALIDATE-DOCUMENT
    version: 1.0.0

  input_mapping:
    document_id: ${workflow.inputs.document_id}

  depends_on:
    - STEP-PARSE-DOCUMENT

  required: true
```

---

# Step Run

Cada ejecución de un Step deberá tener una instancia propia.

Formato recomendado:

```text
STEP-RUN-XXXXXX
```

---

# Contrato preliminar

```yaml
step_run:
  id: STEP-RUN-000041

  execution:
    id: EXEC-000041

  step:
    id: STEP-VALIDATE-DOCUMENT

  activity:
    id: ACT-VALIDATE-DOCUMENT
    version: 1.0.0

  state:
    status: pending

  attempt: 0
```

---

# Engine Adapter

Un **Engine Adapter** permitirá invocar un motor sin acoplar el workflow a su implementación física.

Formato recomendado:

```text
EXEC-ADAPTER-XXXXXX
```

---

# Responsabilidades

- traducir inputs;
- invocar motor;
- manejar protocolo;
- normalizar outputs;
- mapear errores;
- propagar tracing;
- aplicar timeouts;
- respetar cancelación.

---

# Adapter Contract

```yaml
engine_adapter:
  id: EXEC-ADAPTER-VALIDATION

  version: 1.0.0

  target_engine:
    id: VALIDATION-ENGINE

  protocol: internal_api

  capabilities:
    synchronous: true
    asynchronous: true
    cancellation: true
    idempotency: true
```

---

# No lógica de negocio en adaptadores

Los adaptadores no deberán:

- reinterpretar resultados;
- corregir datos;
- cambiar políticas;
- decidir compensaciones.

---

# Catálogo inicial de motores integrables

```text
INGESTION-ENGINE
VALIDATION-ENGINE
KNOWLEDGE-GRAPH
REASONING-ENGINE
INDEXING-ENGINE
RETRIEVAL-ENGINE
RAG-ENGINE
POLICY-ENGINE
NOTIFICATION-SERVICE
AUDIT-SERVICE
```

---

# Modos de integración

```text
synchronous_api
asynchronous_api
event
queue
job
local_component
human_task
```

---

# Synchronous API

Adecuada para tareas breves.

---

# Asynchronous API

Adecuada para tareas prolongadas con Job ID.

---

# Event

Adecuada para desacoplamiento.

---

# Queue

Adecuada para workers.

---

# Job

Adecuada para ejecución programada.

---

# Local Component

Adecuada para componentes dentro del mismo servicio.

---

# Human Task

Adecuada para:

- aprobación;
- revisión;
- resolución de conflicto;
- Quality Gate manual.

---

# Categorías de workflows iniciales

---

# Ingestion Workflow

```text
Receive
↓
Parse
↓
Normalize
↓
Validate
↓
Persist
↓
Publish
```

---

# Knowledge Graph Build Workflow

```text
Resolve Resources
↓
Extract Entities
↓
Build Statements
↓
Build Relations
↓
Validate Graph
↓
Create Snapshot
```

---

# Index Build Workflow

```text
Resolve Snapshot
↓
Generate Units
↓
Chunk
↓
Embed
↓
Build Indexes
↓
Validate
↓
Publish Candidate
```

---

# Query Response Workflow

```text
Policy
↓
Retrieval
↓
Coverage
↓
Reasoning Optional
↓
RAG
↓
Validation
↓
Response
```

---

# Reindex Workflow

```text
Detect Changes
↓
Impact Analysis
↓
Invalidate
↓
Rebuild
↓
Reconcile
↓
Activate
```

---

# Publication Workflow

```text
Release Candidate
↓
Benchmark
↓
Security Gate
↓
Approval
↓
Canary
↓
Stabilization
↓
Complete
```

---

# Recovery Workflow

```text
Detect Failure
↓
Resolve Checkpoint
↓
Restore State
↓
Re-execute
↓
Reconcile
↓
Complete
```

---

# Human-in-the-Loop Workflow

```text
Automated Processing
↓
Manual Review
↓
Approve / Reject
↓
Continue / Compensate
```

---

# Ejecución simple frente a workflow

No toda operación deberá convertirse en un workflow.

---

# Operación simple

Adecuada cuando:

- es atómica;
- es breve;
- no requiere estado persistente;
- no posee dependencias;
- no necesita compensación.

---

# Workflow

Adecuado cuando:

- existen múltiples pasos;
- existen dependencias;
- puede fallar parcialmente;
- requiere reanudación;
- necesita auditoría;
- puede durar mucho tiempo.

---

# Heurística inicial

```text
Una activity simple
→ llamada directa posible

Dos o más pasos dependientes
→ considerar workflow

Operación distribuida con side effects
→ workflow obligatorio
```

---

# Límites de responsabilidad

El Orquestador deberá evitar convertirse en:

- Business Logic Engine;
- Data Transformation Engine;
- Rule Engine genérico;
- almacenamiento de conocimiento;
- API Gateway universal;
- Event Bus;
- sistema de colas;
- motor de búsqueda;
- motor de agentes.

---

# Orquestación gruesa

El Orquestador deberá trabajar preferentemente con actividades de granularidad suficiente.

Ejemplo adecuado:

```text
Validate Document
```

Ejemplo demasiado fino:

```text
Read Character
Normalize Space
Check Comma
```

---

# Granularidad recomendada

Una Activity deberá representar:

- una operación coherente;
- reintentable;
- observable;
- con input y output definido.

---

# Ejemplo de workflow de alto nivel

```yaml
workflow:
  id: WF-KNOWLEDGE-PUBLICATION
  version: 1.0.0

  steps:
    - id: STEP-VALIDATE
      activity: ACT-VALIDATE-KNOWLEDGE

    - id: STEP-BUILD-GRAPH
      activity: ACT-BUILD-KNOWLEDGE-GRAPH
      depends_on:
        - STEP-VALIDATE

    - id: STEP-BUILD-INDEX
      activity: ACT-BUILD-INDEX
      depends_on:
        - STEP-BUILD-GRAPH

    - id: STEP-RUN-GATES
      activity: ACT-RUN-PUBLICATION-GATES
      depends_on:
        - STEP-BUILD-INDEX

    - id: STEP-PUBLISH
      activity: ACT-PUBLISH-SNAPSHOT
      depends_on:
        - STEP-RUN-GATES
```

---

# Responsabilidades por capa

| Capa | Responsabilidad |
|---|---|
| Orquestador | Coordinar |
| Workflow | Describir proceso |
| Step | Declarar operación concreta |
| Activity | Definir capacidad ejecutable |
| Adapter | Invocar motor |
| Motor | Ejecutar lógica especializada |
| State Store | Persistir estado |
| Event Bus | Distribuir eventos |
| Policy Engine | Decidir permisos y políticas |
| Observability | Medir y trazar |

---

# Interacción con Policy Engine

El Orquestador deberá consultar políticas en distintos momentos.

---

# Pre-Execution Policy

Antes de iniciar:

- autorización;
- tenant;
- workflow permitido;
- presupuesto;
- entorno.

---

# Step Policy

Antes de un paso:

- motor permitido;
- datos permitidos;
- acción permitida;
- límites.

---

# Post-Step Policy

Después de un paso:

- output permitido;
- redaction;
- publicación;
- retención.

---

# Compensation Policy

Antes de compensar:

- alcance;
- permisos;
- impacto.

---

# Policy Decision Record

```yaml
policy_decision:
  id: POLICY-DECISION-000041

  execution:
    id: EXEC-000041

  action: workflow.start

  decision: permit

  policy_set:
    id: POLICY-SET-EXECUTION-0001
```

---

# Interacción con Event Bus

El Orquestador publicará eventos y podrá consumir triggers.

---

# Eventos de dominio

Ejemplos:

```text
knowledge_published
index_snapshot_activated
retrieval_completed
workflow_failed
```

---

# Eventos operativos

Ejemplos:

```text
execution_started
step_started
step_completed
retry_scheduled
compensation_started
```

---

# No usar eventos como estado exclusivo

El estado canónico de la ejecución deberá persistirse.

---

# Correlation ID

Todas las operaciones relacionadas deberán compartir un identificador de correlación.

---

# Causation ID

Cada evento deberá indicar qué acción lo causó.

---

# Ejemplo

```yaml
event_metadata:
  correlation_id: CORR-000041
  causation_id: STEP-RUN-000041
```

---

# Interacción con APIs

La API podrá:

- iniciar;
- consultar;
- cancelar;
- pausar;
- reanudar;
- aprobar;
- inspeccionar;
- descargar resultados.

---

# No ejecución opaca

Toda operación larga deberá devolver:

- Execution ID;
- estado;
- timestamps;
- enlaces de seguimiento.

---

# Interacción con agentes

Un Agent Engine futuro podrá solicitar workflows.

Sin embargo:

- no seleccionará versiones arbitrarias;
- no desactivará políticas;
- no excederá budgets;
- no accederá a motores no autorizados.

---

# Agent Execution Profile

Deberá limitar:

- workflows permitidos;
- pasos máximos;
- duración;
- coste;
- aprobación humana;
- side effects.

---

# Interacción con humanos

El Orquestador deberá soportar tareas humanas.

---

# Human Task

Formato recomendado:

```text
HUMAN-TASK-XXXXXX
```

---

# Ejemplo

```yaml
human_task:
  id: HUMAN-TASK-000041

  execution:
    id: EXEC-000041

  type: approval

  assigned_to:
    role: knowledge_reviewer

  decision_options:
    - approve
    - reject
    - request_changes

  deadline: 2026-08-05T18:00:00Z
```

---

# Human Task States

```text
created
assigned
in_progress
completed
expired
cancelled
```

---

# No bloqueo de worker

Una espera humana deberá persistir estado y liberar recursos.

---

# Seguridad

El Orquestador deberá ser un componente de alta confianza.

---

# Riesgos

- ejecución no autorizada;
- escalation;
- workflow injection;
- replay;
- duplicación;
- modificación de inputs;
- abuso de recursos;
- acceso entre tenants;
- compensación maliciosa.

---

# Controles

- autenticación;
- autorización;
- workflow allowlist;
- schemas;
- idempotency;
- signatures;
- secrets management;
- tenant isolation;
- rate limiting;
- audit.

---

# Workflow Injection

Los usuarios no deberán definir workflows arbitrarios en producción salvo capacidad administrativa autorizada.

---

# Dynamic Workflow

Podrá permitirse únicamente en:

- sandbox;
- previews;
- Agent Engine limitado;
- casos aprobados.

---

# Secrets

Los workflows deberán referenciar secretos mediante IDs.

No deberán contener valores.

---

# Ejemplo

```yaml
secret_reference:
  id: SECRET-REF-INDEXING-API
```

---

# Tenant Isolation

Cada Execution deberá pertenecer a un tenant o scope explícito.

---

# Cross-Tenant Workflow

Deberá estar prohibido salvo proceso administrativo especial.

---

# Least Privilege

Cada Activity deberá ejecutarse con permisos mínimos.

---

# Execution Identity

Podrá utilizar:

- requester identity;
- service identity;
- delegated identity;
- workflow identity.

---

# No delegación implícita

---

# Auditoría

Deberán auditarse:

- inicio;
- cancelación;
- reanudación;
- aprobación;
- override;
- compensación;
- cambio de prioridad;
- migración;
- resultado.

---

# Audit Record

```yaml
execution_audit_event:
  id: EXEC-AUDIT-000041

  execution:
    id: EXEC-000041

  action: execution.started

  actor:
    id: SERVICE-INGESTION-API
    type: service

  result: succeeded

  occurred_at: 2026-08-02T20:00:01Z
```

---

# Presupuesto de ejecución

Toda ejecución deberá disponer de un budget.

Formato recomendado:

```text
EXEC-BUDGET-XXXXXX
```

---

# Dimensiones

```text
maximum_duration
maximum_steps
maximum_attempts
maximum_parallel_steps
maximum_external_calls
maximum_cost
maximum_tokens
maximum_storage
```

---

# Contrato preliminar

```yaml
execution_budget:
  id: EXEC-BUDGET-000041

  limits:
    maximum_duration: PT30M
    maximum_steps: 20
    maximum_attempts_per_step: 3
    maximum_parallel_steps: 4
    maximum_external_calls: 50
    maximum_cost: 5.00
    currency: EUR
```

---

# Budget Sources

- workflow;
- tenant;
- requester;
- environment;
- policy;
- operation.

---

# Hard Limits

No deberán superarse.

---

# Soft Limits

Podrán generar:

- warning;
- approval;
- degradation.

---

# Ejecución durable

Los workflows prolongados deberán ser durables.

---

# Durable Execution

Significa que la ejecución puede sobrevivir a:

- reinicios;
- fallos de worker;
- despliegues;
- pérdida de conexión;
- pausas.

---

# Persistencia mínima

Deberán persistirse:

- Execution;
- Step Runs;
- state transitions;
- inputs references;
- outputs references;
- checkpoints;
- attempts;
- events;
- diagnostics.

---

# No persistir datos masivos en estado

Los outputs grandes deberán almacenarse externamente y referenciarse.

---

# Artifact Reference

```yaml
artifact_reference:
  id: ARTIFACT-REF-000041
  type: validation_result
  location: internal-object-store
  checksum: ...
```

---

# Durabilidad frente a consistencia

El State Store deberá garantizar que una transición confirmada no se pierda.

---

# Estados preliminares de Execution

```text
created
validating
queued
running
waiting
paused
cancelling
compensating
succeeded
succeeded_with_warnings
partial
failed
cancelled
timed_out
blocked
```

---

# Estados preliminares de Step Run

```text
pending
ready
queued
running
waiting
retrying
succeeded
succeeded_with_warnings
failed
skipped
cancelled
timed_out
compensating
compensated
```

La Parte V desarrollará formalmente el modelo de estados.

---

# Observabilidad básica

Desde la primera implementación deberán existir:

- Execution ID;
- Step Run IDs;
- logs estructurados;
- timestamps;
- estados;
- métricas;
- traces;
- diagnostics.

---

# Métricas iniciales

- executions started;
- executions completed;
- executions failed;
- execution duration;
- steps executed;
- retries;
- compensations;
- cancellations;
- queue time.

---

# Logs

```yaml
log:
  event: execution_started

  execution_id: EXEC-000041
  workflow: WF-KNOWLEDGE-INGESTION@1.0.0

  trigger: event
  tenant: TENANT-0001
  environment: production
```

---

# No payloads sensibles en logs

---

# Eventos iniciales

```text
execution_requested
execution_created
execution_started
execution_completed
execution_failed
execution_cancelled
step_ready
step_started
step_completed
step_failed
```

---

# Evento de inicio

```yaml
event:
  type: execution_started

  subject:
    id: EXEC-000041
    type: execution

  data:
    workflow: WF-KNOWLEDGE-INGESTION@1.0.0
    trigger_type: event
```

---

# Perfiles iniciales del Orquestador

---

# Perfil mínimo

Incluye:

- workflows declarativos;
- ejecución secuencial;
- persistencia de estado;
- reintentos básicos;
- logs;
- API de estado.

---

# Perfil estándar

Añade:

- DAGs;
- paralelismo;
- eventos;
- cancelación;
- checkpoints;
- políticas;
- Quality Gates.

---

# Perfil avanzado

Añade:

- Sagas;
- compensaciones;
- scheduling;
- dynamic branching;
- human tasks;
- budgets;
- distributed workers.

---

# Perfil agentic

Añade:

- planificación dinámica controlada;
- tools;
- human approval;
- bounded autonomy;
- memory references;
- policy-driven branching.

---

# Perfil enterprise

Añade:

- multi-region;
- HA;
- DR;
- quotas;
- governance;
- federated execution;
- compliance.

---

# Implementación inicial recomendada

La primera implementación práctica debería soportar:

```text
Execution Request
        ↓
Workflow Resolution
        ↓
Sequential Steps
        ↓
Persistent State
        ↓
Retries
        ↓
Execution Result
```

---

# Workflows iniciales recomendados

```text
WF-DOCUMENT-VALIDATION
WF-KNOWLEDGE-INGESTION
WF-INDEX-BUILD
WF-RETRIEVAL-RAG
```

---

# Segunda iteración

Añadirá:

```text
DAGs
+
Parallel Steps
+
Checkpoints
+
Cancellation
+
Events
```

---

# Tercera iteración

Añadirá:

```text
Sagas
+
Compensations
+
Human Tasks
+
Scheduling
+
Distributed Workers
```

---

# No será necesario inicialmente

- workflow DSL completa;
- auto-scaling predictivo;
- multi-region active-active;
- autonomous workflow generation;
- arbitrary user-defined workflows;
- nested distributed transactions;
- visual workflow designer;
- self-modifying workflows;
- unlimited dynamic branching.

---

# Casos de uso

---

# Caso de uso 1 — Validación de documento

```text
Receive Request
↓
Validate Input
↓
Invoke Validation Engine
↓
Store Result
↓
Complete
```

---

# Caso de uso 2 — Publicación de conocimiento

```text
Validate
↓
Build Graph
↓
Build Index
↓
Run Quality Gates
↓
Publish
```

---

# Caso de uso 3 — Consulta RAG

```text
Policy Check
↓
Retrieve Evidence
↓
Generate Context
↓
Invoke RAG
↓
Validate Response
```

---

# Caso de uso 4 — Ejecución parcial

La indexación termina, pero la publicación falla.

El Orquestador deberá:

- conservar snapshot candidato;
- marcar ejecución parcial o fallida;
- permitir retry;
- no repetir pasos exitosos sin necesidad.

---

# Caso de uso 5 — Evento duplicado

El mismo evento llega dos veces.

La idempotency key evita crear dos ejecuciones equivalentes.

---

# Caso de uso 6 — Espera humana

Un snapshot requiere aprobación.

La ejecución queda:

```text
waiting
```

sin mantener un worker ocupado.

---

# Caso de uso 7 — Cancelación

Un operador cancela un reindexado.

El Orquestador:

- deja de programar nuevos steps;
- solicita cancelación de steps activos;
- ejecuta cleanup si procede;
- registra estado.

---

# Caso de uso 8 — Recuperación tras reinicio

El servicio se reinicia.

La ejecución se reanuda desde el último estado persistido.

---

# Caso de uso 9 — Tenant isolation

Un workflow del Tenant A no puede leer artifacts del Tenant B.

---

# Caso de uso 10 — Agent trigger

Un agente solicita un workflow permitido.

El Orquestador aplica:

- profile;
- budget;
- policy;
- approval si existe side effect.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Lógica de dominio en el Orquestador

El Orquestador no deberá validar recetas ni razonar.

---

## Workflows codificados únicamente en controladores

Impide versionado y reanudación.

---

## Estado solo en memoria

Se pierde ante reinicios.

---

## Llamadas encadenadas sin Execution ID

Impiden trazabilidad.

---

## Dependencias implícitas

Dificultan entender el proceso.

---

## Reintentos sin idempotencia

Duplican efectos.

---

## Compensación equivalente a rollback técnico

En sistemas distribuidos, la compensación puede ser una nueva acción.

---

## Un workflow para cada método

Produce granularidad excesiva.

---

## Una activity gigantesca

Impide reintentos selectivos.

---

## Workers esperando tareas humanas

Desperdicia recursos.

---

## Eventos como única fuente de estado

Puede perderse contexto.

---

## Permitir workflows arbitrarios en producción

Compromete seguridad.

---

## Secrets incluidos en definiciones

Expone credenciales.

---

## Tenant proporcionado por input textual

Debe proceder del contexto autenticado.

---

## No fijar versión de workflow

Impide reproducibilidad.

---

## Modificar definición durante ejecución

Genera estados incoherentes.

---

## Ignorar outputs parciales

Impide reanudar.

---

## Almacenar blobs grandes en State Store

Deteriora rendimiento.

---

## Ejecutar todo sin budget

Permite consumo ilimitado.

---

## Confundir Event Bus y Orquestador

Cumplen funciones distintas.

---

## Orquestador como punto de lógica universal

Produce un monolito de coordinación.

---

## No distinguir workflow y pipeline

Dificulta modelar procesos.

---

## No auditar overrides

Impide gobernanza.

---

## Cancelar eliminando el registro

La ejecución debe conservar historial.

---

## Ejecutar compensaciones sin política

Puede empeorar el estado.

---

# Reglas mínimas de conformidad

---

## Execution Request identificada

Toda ejecución deberá comenzar con una solicitud formal.

---

## Trigger identificado

Deberá conocerse el origen.

---

## Workflow versionado

Toda ejecución deberá fijar una versión.

---

## Execution ID estable

Toda instancia deberá ser trazable.

---

## Tenant resuelto

Deberá proceder del contexto autorizado.

---

## Idempotency

Las solicitudes repetibles deberán disponer de protección.

---

## Steps explícitos

Toda operación compuesta deberá declarar sus pasos.

---

## Activities registradas

Toda capacidad deberá estar definida.

---

## Adapters versionados

Toda integración deberá ser trazable.

---

## Estado persistente

Las ejecuciones prolongadas deberán ser durables.

---

## Inputs y outputs tipados

Todo contrato deberá ajustarse a schema.

---

## Policies aplicadas

Toda ejecución deberá evaluar autorización.

---

## Budget identificado

Toda ejecución deberá tener límites.

---

## Correlation ID

Toda operación distribuida deberá poder correlacionarse.

---

## Auditoría

Las operaciones relevantes deberán registrarse.

---

## No lógica especializada

El Orquestador no deberá sustituir motores.

---

# Conformidad de Execution Request

Será conforme cuando:

- tenga ID;
- identifique workflow;
- identifique trigger;
- identifique requester;
- declare tenant;
- declare environment;
- cumpla schema;
- declare idempotency cuando proceda.

---

# Conformidad de Workflow

Será conforme cuando:

- tenga ID;
- tenga versión;
- declare status;
- declare inputs;
- declare outputs;
- declare steps;
- declare policies;
- declare budgets;
- declare compatibilidad.

---

# Conformidad de Activity

Será conforme cuando:

- tenga ID;
- tenga versión;
- declare executor;
- declare input schema;
- declare output schema;
- declare idempotencia;
- declare retryability;
- declare cancellability.

---

# Conformidad de Step

Será conforme cuando:

- tenga ID;
- referencie Activity;
- declare input mapping;
- declare dependencias;
- declare obligatoriedad;
- declare políticas;
- declare límites.

---

# Conformidad de Engine Adapter

Será conforme cuando:

- tenga ID;
- tenga versión;
- identifique motor;
- declare protocolo;
- normalice errores;
- propague tracing;
- respete timeout;
- preserve seguridad.

---

# Conformidad de Execution

Será conforme cuando:

- tenga ID;
- identifique request;
- identifique workflow y versión;
- preserve trigger;
- declare contexto;
- declare estado;
- preserve correlation;
- genere resultado.

---

# Lista de comprobación

Antes de aprobar los fundamentos del Orquestador deberá comprobarse:

```text
[ ] El Orquestador posee una responsabilidad delimitada.
[ ] No contiene lógica culinaria.
[ ] No sustituye a los motores especializados.
[ ] Existe un Execution Gateway.
[ ] Existe un Workflow Registry.
[ ] Existe un Execution Coordinator.
[ ] Existe un State Store durable.
[ ] Los triggers están tipados.
[ ] Las Execution Requests tienen ID.
[ ] Las idempotency keys están definidas.
[ ] Los workflows están versionados.
[ ] Las ejecuciones fijan versión.
[ ] Las Activities están registradas.
[ ] Los Steps referencian Activities.
[ ] Los Engine Adapters están versionados.
[ ] Los inputs y outputs tienen schema.
[ ] El tenant procede del contexto autenticado.
[ ] Los permisos se evalúan.
[ ] Los secrets se referencian.
[ ] Las ejecuciones tienen budget.
[ ] Los procesos largos son asíncronos.
[ ] Los estados se persisten.
[ ] Los outputs grandes se almacenan como artifacts.
[ ] Los eventos tienen correlation y causation.
[ ] Las tareas humanas liberan workers.
[ ] Las cancelaciones preservan historial.
[ ] Las operaciones son auditables.
[ ] Las definiciones no cambian durante ejecución.
[ ] Los workflows dinámicos están limitados.
[ ] Los perfiles iniciales están definidos.
```

---

# Arquitectura final de la Parte I

```text
Trigger
        ↓
Execution Gateway
        ↓
Execution Request
        ↓
Policy and Idempotency Validation
        ↓
Workflow Resolution
        ↓
Execution Creation
        ↓
Execution Context
        ↓
Execution Coordinator
        ↓
Steps
        ↓
Activities
        ↓
Engine Adapters
        ↓
Specialized Engines
        ↓
Step Results
        ↓
Execution Result
        ↓
Events · Metrics · Audit
```

---

# Transición hacia la Parte II

Esta primera parte ha definido:

- la misión del Orquestador;
- el problema que resuelve;
- el alcance;
- la diferencia entre orquestación y coreografía;
- los principios arquitectónicos;
- los componentes internos;
- los dominios de ejecución;
- los tipos de ejecución;
- los triggers;
- las Execution Requests;
- las Executions;
- el Execution Context;
- los resultados;
- los Workflows;
- los Pipelines;
- las Activities;
- los Steps;
- los Step Runs;
- los Engine Adapters;
- los modos de integración;
- las categorías iniciales de workflows;
- la relación con Policy Engine;
- la relación con Event Bus;
- la relación con APIs;
- la relación con agentes;
- las tareas humanas;
- la seguridad;
- la auditoría;
- los budgets;
- la ejecución durable;
- los perfiles;
- los casos de uso;
- los antipatrones;
- las reglas de conformidad.

La Parte II desarrollará el **Execution Model**, incluyendo:

- modelo formal de Execution;
- Execution Definition;
- Execution Instance;
- Execution Context;
- Execution Variables;
- Input Bindings;
- Output Bindings;
- Artifacts;
- Step Definitions;
- Step Runs;
- Activities;
- Activity Results;
- Commands;
- Decisions;
- Conditions;
- Branches;
- Loops controlados;
- Child Executions;
- Parent Executions;
- Correlation;
- Causation;
- Idempotency;
- Checkpoints;
- Execution History;
- determinismo;
- replay;
- versionado;
- compatibilidad;
- schemas;
- contratos completos.

---

# Conclusión

El Orquestador de Ejecución será la capa encargada de convertir capacidades independientes en procesos completos, durables y gobernados.

Su función puede resumirse así:

```text
Recibir una intención de ejecución
        ↓
Resolver el workflow
        ↓
Crear una ejecución
        ↓
Aplicar políticas
        ↓
Coordinar pasos
        ↓
Invocar motores
        ↓
Mantener estado
        ↓
Gestionar fallos
        ↓
Producir resultado
        ↓
Auditar
```

Los triggers explican por qué se inicia un proceso.

Las Execution Requests formalizan la solicitud.

Los Workflows describen el proceso.

Las Activities representan capacidades reutilizables.

Los Steps utilizan esas capacidades dentro de un flujo.

Los Engine Adapters conectan con los motores.

El Execution Coordinator mantiene orden y estado.

El State Store aporta durabilidad.

El Policy Engine limita acciones.

El Event Bus desacopla efectos secundarios.

Los budgets evitan consumo ilimitado.

La auditoría permite reconstruir decisiones.

Un Orquestador conforme deberá poder responder:

```text
¿Qué workflow se ejecuta?

¿Qué versión utiliza?

¿Qué solicitud lo inició?

¿Qué actor lo solicitó?

¿Qué tenant afecta?

¿Qué steps contiene?

¿Qué activities ejecuta?

¿Qué motores intervienen?

¿Qué estado posee?

¿Qué presupuesto tiene?

¿Qué eventos ha emitido?

¿Qué resultados ha producido?

¿Qué decisiones se han auditado?
```

Con esta primera parte quedan establecidos los fundamentos, la arquitectura y los límites de responsabilidad del **Orquestador de Ejecución de NovaCoquinaria**.

La siguiente parte formalizará el modelo interno mediante el que cada workflow, ejecución, step, activity, artifact, variable, decisión y checkpoint será representado de forma versionada, durable y reproducible.

---

# Parte II — Execution Model: definiciones, instancias, variables, bindings, artefactos, decisiones, subejecuciones, checkpoints y replay

---

# Introducción

La Parte I ha definido:

- la misión del Orquestador de Ejecución;
- su posición dentro de NovaCoquinaria;
- sus límites de responsabilidad;
- los tipos de ejecución;
- los triggers;
- las Execution Requests;
- los Workflows;
- las Activities;
- los Steps;
- los Engine Adapters;
- la persistencia durable;
- los budgets;
- la seguridad;
- la auditoría;
- los perfiles iniciales.

Esta segunda parte formaliza el modelo interno mediante el que el Orquestador representará una ejecución.

El **Execution Model** deberá permitir describir de forma precisa:

- qué definición se está ejecutando;
- qué instancia concreta existe;
- qué inputs recibió;
- cómo se enlazan esos inputs;
- qué variables mantiene;
- qué Steps se crean;
- qué Activities se invocan;
- qué outputs producen;
- qué artefactos generan;
- qué decisiones se toman;
- qué ramas se activan;
- qué ejecuciones hijas se crean;
- qué checkpoints se conservan;
- qué historial permite reconstruir;
- cómo se reanuda;
- cómo se reproduce;
- cómo evoluciona entre versiones.

Conceptualmente:

```text
Execution Definition
        ↓
Execution Request
        ↓
Execution Instance
        ↓
Execution Context
        ↓
Input Bindings
        ↓
Execution Variables
        ↓
Step Instances
        ↓
Activity Invocations
        ↓
Outputs and Artifacts
        ↓
Decisions and State Transitions
        ↓
Checkpoints
        ↓
Execution History
        ↓
Execution Result
```

El modelo deberá diferenciar con claridad entre:

```text
Definición
```

e:

```text
Instancia
```

Una definición describe qué podría ejecutarse.

Una instancia representa lo que realmente se ejecutó.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- formalizar Execution Definitions;
- distinguir definición e instancia;
- definir Execution Instances;
- formalizar Execution Contexts;
- establecer Execution Inputs;
- definir Input Bindings;
- formalizar Execution Variables;
- diferenciar variables inmutables y mutables;
- establecer Output Bindings;
- definir Artifacts;
- formalizar Artifact References;
- definir Activity Definitions;
- definir Activity Invocations;
- formalizar Activity Results;
- definir Step Definitions;
- formalizar Step Instances;
- definir Step Runs;
- establecer Commands;
- formalizar Decisions;
- definir Conditions;
- establecer Branches;
- regular Loops controlados;
- definir Map y Fan-Out;
- definir Join y Fan-In;
- formalizar Child Executions;
- definir Parent Executions;
- establecer Subworkflows;
- formalizar Correlation;
- definir Causation;
- establecer Idempotency;
- formalizar Checkpoints;
- definir Execution History;
- establecer Replay;
- definir determinismo;
- formalizar versionado;
- establecer compatibilidad;
- definir schemas;
- formalizar diagnósticos;
- establecer Quality Gates;
- definir conformidad del Execution Model.

---

# Principios del Execution Model

Toda implementación deberá respetar los siguientes principios.

---

## Definición e instancia separadas

Una Execution Definition no deberá contener estado de una ejecución concreta.

---

## Instancias inmutables en identidad

Una Execution Instance conservará siempre:

- Execution ID;
- Workflow ID;
- Workflow Version;
- tenant;
- trigger;
- requester;
- creation time.

---

## Contratos tipados

Inputs, outputs, variables, Commands, Decisions y Artifacts deberán ajustarse a schemas.

---

## Estado explícito

Toda mutación relevante deberá representarse mediante una transición o evento.

---

## No datos implícitos

Los Steps no deberán depender de variables ocultas del proceso.

---

## Bindings declarativos

La conexión entre outputs e inputs deberá ser visible.

---

## Artefactos referenciados

Los datos voluminosos deberán almacenarse fuera del Execution State y utilizar referencias.

---

## Historial append-only

El historial de decisiones y transiciones no deberá reescribirse.

---

## Replay seguro

La reproducción no deberá repetir side effects sin control.

---

## Determinismo del coordinador

Dado el mismo historial y la misma definición, el Orquestador deberá reconstruir el mismo estado lógico.

---

## No determinismo encapsulado

Fechas, UUID, respuestas externas o aleatoriedad deberán capturarse como datos del historial.

---

## Subejecuciones explícitas

Toda ejecución hija deberá conservar parent, correlation y policy.

---

## Versionado fijado

Toda instancia deberá ejecutar definiciones concretas e inmutables.

---

## Compatibilidad declarada

No deberá asumirse que dos versiones son compatibles.

---

## Idempotencia por operación

La idempotencia deberá definirse en el nivel apropiado:

- Request;
- Execution;
- Step;
- Activity;
- Command.

---

## Checkpoints verificables

Todo checkpoint deberá corresponder a un estado consistente.

---

## Outputs finales diferenciados de intermedios

No todo output de Step deberá convertirse en output del Workflow.

---

## Variables mínimas

El Execution Context no deberá convertirse en una base de datos general.

---

## Seguridad heredada y restringible

Una subejecución podrá recibir menos permisos, nunca más, salvo elevación explícita y autorizada.

---

# Arquitectura del Execution Model

```text
┌───────────────────────────────────────────────┐
│           Execution Definition Layer          │
│                                               │
│ Workflow · Steps · Activities · Schemas       │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            Execution Instance Layer           │
│                                               │
│ Request · Context · Variables · State         │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Step Runtime Layer              │
│                                               │
│ Step Instances · Runs · Attempts · Commands   │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            Data and Artifact Layer            │
│                                               │
│ Inputs · Outputs · Bindings · References      │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            History and Recovery Layer         │
│                                               │
│ Events · Decisions · Checkpoints · Replay     │
└───────────────────────────────────────────────┘
```

---

# Execution Definition

Una **Execution Definition** representa la definición completa y versionada de un proceso ejecutable.

Podrá corresponder a:

- Workflow;
- Pipeline;
- Subworkflow;
- Recovery Flow;
- Compensation Flow.

Formato recomendado:

```text
EXEC-DEF-XXXXXX
```

---

# Contrato

```yaml
execution_definition:
  id: EXEC-DEF-KNOWLEDGE-PUBLICATION
  version: 1.0.0
  status: active

  kind: workflow

  metadata:
    name: Knowledge Publication
    description: >
      Valida, transforma, indexa y publica conocimiento.

  inputs_schema:
    id: EXEC-INPUT-KNOWLEDGE-PUBLICATION
    version: 1.0.0

  outputs_schema:
    id: EXEC-OUTPUT-KNOWLEDGE-PUBLICATION
    version: 1.0.0

  variables_schema:
    id: EXEC-VARS-KNOWLEDGE-PUBLICATION
    version: 1.0.0

  steps:
    - STEP-VALIDATE
    - STEP-BUILD-GRAPH
    - STEP-BUILD-INDEX
    - STEP-RUN-GATES
    - STEP-PUBLISH

  policies:
    id: EXEC-POLICY-KNOWLEDGE-PUBLICATION

  budget:
    id: EXEC-BUDGET-PROFILE-PUBLICATION

  compatibility:
    minimum_orchestrator_version: 1.0.0
```

---

# Definition Kinds

```text
workflow
pipeline
subworkflow
compensation
recovery
maintenance
interactive
agentic
```

---

# Definition Status

```text
draft
validating
experimental
active
deprecated
retired
blocked
invalid
```

---

# Definition Immutability

Una versión publicada no deberá modificarse.

Cualquier cambio deberá producir:

```text
new version
```

---

# Definition Fingerprint

Deberá calcularse sobre:

- metadata relevante;
- schemas;
- Steps;
- Activities;
- bindings;
- condiciones;
- políticas;
- budgets;
- compensaciones.

---

# Uso

Permitirá detectar:

- modificaciones;
- inconsistencias;
- definiciones corruptas;
- diferencias entre ambientes.

---

# Definition Manifest

```yaml
execution_definition_manifest:
  definition: EXEC-DEF-KNOWLEDGE-PUBLICATION@1.0.0

  fingerprint:
    algorithm: sha256
    value: ...

  dependencies:
    activities:
      - ACT-VALIDATE-KNOWLEDGE@1.0.0
      - ACT-BUILD-GRAPH@1.2.0
      - ACT-BUILD-INDEX@2.0.0

    adapters:
      - EXEC-ADAPTER-VALIDATION@1.0.0
      - EXEC-ADAPTER-INDEXING@1.1.0

    policies:
      - EXEC-POLICY-KNOWLEDGE-PUBLICATION@1.0.0
```

---

# Execution Instance

Una **Execution Instance** representa la ejecución concreta de una definición.

Formato recomendado:

```text
EXEC-XXXXXX
```

---

# Contrato ampliado

```yaml
execution:
  id: EXEC-000041

  definition:
    id: EXEC-DEF-KNOWLEDGE-PUBLICATION
    version: 1.0.0
    fingerprint: ...

  request:
    id: EXEC-REQUEST-000041

  trigger:
    id: EXEC-TRIGGER-000041
    type: event

  requester:
    id: SERVICE-KNOWLEDGE-API
    type: service

  context:
    id: EXEC-CONTEXT-000041

  state:
    status: running
    revision: 18

  timing:
    created_at: 2026-08-02T20:00:01Z
    started_at: 2026-08-02T20:00:02Z
    deadline: 2026-08-02T20:30:02Z

  correlation:
    correlation_id: CORR-000041
    causation_id: EVENT-KNOWLEDGE-READY-000041

  hierarchy:
    parent_execution_id: null
    root_execution_id: EXEC-000041

  state_store:
    revision: 18
```

---

# Execution Revision

Toda modificación del estado deberá aumentar una revisión lógica.

---

# Optimistic Concurrency

Las actualizaciones deberán poder utilizar:

```text
expected_revision
```

---

# Error

```text
EXECUTION_REVISION_CONFLICT
```

---

# Root Execution

Representa la ejecución superior de una jerarquía.

---

# Parent Execution

Ejecución que crea una subejecución.

---

# Child Execution

Ejecución creada por otra.

---

# Execution Labels

Podrán utilizarse para:

- búsqueda;
- operación;
- agrupación;
- coste;
- observabilidad.

---

# Ejemplo

```yaml
labels:
  domain: knowledge
  operation: publication
  resource_id: REC-0009
  release: v1.4.0
```

---

# No lógica basada exclusivamente en labels

Las labels no sustituyen campos tipados.

---

# Execution Context

El **Execution Context** contiene el contexto estable y compartido de una ejecución.

---

# Secciones

```text
identity
security
environment
correlation
budget
deadline
policies
capabilities
variables
observability
```

---

# Contrato ampliado

```yaml
execution_context:
  id: EXEC-CONTEXT-000041

  execution:
    id: EXEC-000041

  identity:
    requester:
      id: SERVICE-KNOWLEDGE-API
      type: service

    execution_principal:
      id: SERVICE-EXECUTION-ORCHESTRATOR
      type: service

  security:
    tenant: TENANT-0001
    clearance: internal
    policy_set: POLICY-SET-EXECUTION-0001

  environment:
    id: production
    region: eu-west

  correlation:
    trace_id: TRACE-000041
    correlation_id: CORR-000041
    causation_id: EVENT-KNOWLEDGE-READY-000041

  budget:
    id: EXEC-BUDGET-000041

  deadline:
    absolute: 2026-08-02T20:30:02Z

  capabilities:
    knowledge_graph: available
    indexing: available
    validation: available

  variables:
    id: EXEC-VARIABLE-SET-000041

  observability:
    logging_profile: EXEC-LOGGING-STANDARD
    tracing_profile: EXEC-TRACING-STANDARD
```

---

# Context Inheritance

Las subejecuciones podrán heredar:

- correlation;
- tenant;
- environment;
- policy constraints;
- observability context.

---

# No inheritance automática de:

- secrets;
- elevated roles;
- budget completo;
- mutable variables;
- deadlines sin ajuste.

---

# Context Narrowing

Una subejecución podrá recibir un scope más limitado.

---

# Ejemplo

```yaml
context_narrowing:
  parent_clearance: internal
  child_clearance: public

  parent_budget: EXEC-BUDGET-000041
  child_budget: EXEC-BUDGET-CHILD-000041
```

---

# Execution Inputs

Los **Execution Inputs** representan los datos proporcionados al iniciar el proceso.

Formato recomendado:

```text
EXEC-INPUT-SET-XXXXXX
```

---

# Contrato

```yaml
execution_inputs:
  id: EXEC-INPUT-SET-000041

  execution:
    id: EXEC-000041

  schema:
    id: EXEC-INPUT-KNOWLEDGE-PUBLICATION
    version: 1.0.0

  values:
    knowledge_snapshot_id: KG-SNAP-20260802-0001
    publication_mode: standard
    requested_environment: production

  validation:
    status: valid
```

---

# Input Sources

```text
request
trigger
parent_execution
artifact
policy
system
human_task
```

---

# Input Precedence

No deberá mezclarse input de varias fuentes sin política.

Orden recomendado:

```text
System-enforced values
↓
Policy-enforced values
↓
Authenticated context
↓
Parent bindings
↓
Request inputs
↓
Defaults
```

---

# No override de valores de seguridad

Un Request Input no deberá sobrescribir:

- tenant;
- principal;
- environment restringido;
- policy set.

---

# Input Validation

Deberá comprobar:

- schema;
- required fields;
- types;
- ranges;
- references;
- authorization;
- artifact existence;
- snapshot compatibility.

---

# Input Normalization

Podrá normalizar:

- fechas;
- IDs;
- enums;
- referencias.

No deberá alterar semántica.

---

# Input Binding

Un **Input Binding** define cómo obtiene un Step sus inputs.

Formato recomendado:

```text
EXEC-BINDING-XXXXXX
```

---

# Binding Sources

```text
workflow_input
execution_variable
step_output
artifact
constant
secret_reference
policy_value
system_value
parent_output
```

---

# Contrato

```yaml
input_binding:
  id: EXEC-BINDING-000041

  target:
    step: STEP-BUILD-INDEX
    field: knowledge_graph_snapshot_id

  source:
    type: step_output
    step: STEP-BUILD-GRAPH
    field: snapshot_id

  required: true

  transformation:
    type: identity
```

---

# Binding Path Syntax

Podrá utilizar una sintaxis controlada.

Ejemplo:

```text
${steps.STEP-BUILD-GRAPH.outputs.snapshot_id}
```

---

# No evaluación arbitraria de código

Los bindings no deberán permitir:

- scripts sin sandbox;
- ejecución de comandos;
- acceso libre a objetos.

---

# Binding Transformations

Valores iniciales:

```text
identity
select
rename
cast
default
format
join
list
object
reference
```

---

# Transformaciones complejas

Deberán implementarse mediante Activities específicas, no mediante expresiones opacas.

---

# Binding Validation

Deberá comprobar:

- source existente;
- type compatibility;
- nullability;
- execution order;
- security compatibility.

---

# Binding Dependency

Un binding desde `step_output` crea una dependencia lógica.

---

# Missing Required Binding

Error:

```text
EXECUTION_REQUIRED_BINDING_UNRESOLVED
```

---

# Optional Binding

Podrá quedar ausente.

---

# Default Value

Deberá declararse en schema o binding.

---

# Execution Variables

Las **Execution Variables** representan datos internos de coordinación.

Formato recomendado:

```text
EXEC-VARIABLE-SET-XXXXXX
```

---

# Tipos

```text
immutable
mutable
derived
system
secret_reference
counter
flag
collection
```

---

# Immutable Variables

Se fijan al inicio.

Ejemplos:

- resource ID;
- source snapshot;
- requested environment;
- workflow version.

---

# Mutable Variables

Pueden cambiar mediante operaciones controladas.

Ejemplos:

- retry count;
- selected branch;
- active snapshot candidate;
- approval state.

---

# Derived Variables

Se calculan a partir de otras.

---

# System Variables

Ejemplos:

```text
execution_id
current_time_reference
current_step
attempt
deadline
```

---

# Secret Reference Variables

Contienen únicamente referencias.

---

# Variable Contract

```yaml
execution_variable:
  name: candidate_snapshot_id

  type: string

  mutability: mutable

  value: IDX-SNAP-CANDIDATE-000041

  source:
    step_run: STEP-RUN-BUILD-INDEX-000041

  revision: 2
```

---

# Variable Update

Toda actualización deberá registrar:

- variable;
- old value hash;
- new value hash;
- actor;
- Step Run;
- timestamp;
- revision.

---

# Variable Update Command

```yaml
variable_update:
  variable: candidate_snapshot_id
  expected_revision: 1
  new_value: IDX-SNAP-CANDIDATE-000041
```

---

# Variable Conflict

```text
EXECUTION_VARIABLE_REVISION_CONFLICT
```

---

# Atomic Variable Updates

Podrán agruparse cuando deban mantenerse consistentes.

---

# No mutable global state

Las variables deberán estar limitadas a la Execution.

---

# Step Definition

Un **Step Definition** describe el uso de una Activity dentro de una definición.

---

# Contrato ampliado

```yaml
workflow_step:
  id: STEP-BUILD-INDEX

  activity:
    id: ACT-BUILD-INDEX
    version: 2.0.0

  input_bindings:
    - EXEC-BINDING-000041
    - EXEC-BINDING-000042

  output_bindings:
    - EXEC-OUTPUT-BINDING-000041

  depends_on:
    all:
      - STEP-BUILD-GRAPH

  condition:
    id: EXEC-CONDITION-000041

  execution:
    required: true
    cancellable: true
    idempotent: true

  retry_policy:
    id: EXEC-RETRY-POLICY-INDEXING

  timeout_policy:
    id: EXEC-TIMEOUT-POLICY-INDEXING

  compensation:
    activity: ACT-DISCARD-INDEX-CANDIDATE

  quality_gate:
    id: QG-STEP-BUILD-INDEX
```

---

# Step Definition Types

```text
activity
decision
parallel
join
map
loop
wait
human_task
subworkflow
signal
quality_gate
compensation
```

---

# Activity Step

Invoca una Activity.

---

# Decision Step

Evalúa una Decision.

---

# Parallel Step

Inicia varias ramas.

---

# Join Step

Espera varias ramas.

---

# Map Step

Aplica una Activity a una colección.

---

# Loop Step

Repite de forma controlada.

---

# Wait Step

Espera:

- tiempo;
- evento;
- señal;
- condición.

---

# Human Task Step

Espera una acción humana.

---

# Subworkflow Step

Inicia una Child Execution.

---

# Signal Step

Emite o espera una señal.

---

# Quality Gate Step

Evalúa criterios.

---

# Compensation Step

Ejecuta compensación.

---

# Step Instance

Una **Step Instance** representa un Step materializado dentro de una Execution.

Formato recomendado:

```text
STEP-INSTANCE-XXXXXX
```

---

# Contrato

```yaml
step_instance:
  id: STEP-INSTANCE-000041

  execution:
    id: EXEC-000041

  definition:
    workflow_step: STEP-BUILD-INDEX

  state:
    status: ready
    revision: 3

  dependencies:
    resolved: true

  activation:
    activated_at: 2026-08-02T20:02:00Z

  current_run:
    id: STEP-RUN-000045
```

---

# Step Instance vs Step Run

```text
Step Instance
```

representa el Step dentro de la Execution.

```text
Step Run
```

representa un intento de ejecución.

---

# Ejemplo

```text
STEP-BUILD-INDEX
    ├── Run 1 → failed
    ├── Run 2 → timed_out
    └── Run 3 → succeeded
```

---

# Step Run

Formato recomendado:

```text
STEP-RUN-XXXXXX
```

---

# Contrato ampliado

```yaml
step_run:
  id: STEP-RUN-000045

  step_instance:
    id: STEP-INSTANCE-000041

  attempt: 3

  activity:
    id: ACT-BUILD-INDEX
    version: 2.0.0

  adapter:
    id: EXEC-ADAPTER-INDEXING
    version: 1.1.0

  state:
    status: running

  timing:
    queued_at: 2026-08-02T20:02:01Z
    started_at: 2026-08-02T20:02:03Z
    deadline: 2026-08-02T20:12:03Z

  worker:
    id: WORKER-INDEXING-0004

  command:
    id: EXEC-COMMAND-000045
```

---

# Attempt Number

Deberá comenzar por:

```text
1
```

o utilizar una convención única y documentada.

---

# Step Run Identity

Cada retry deberá crear un nuevo Step Run.

No deberá sobrescribirse el intento anterior.

---

# Activity Definition

Una **Activity Definition** representa una capacidad invocable.

---

# Contrato ampliado

```yaml
activity_definition:
  id: ACT-BUILD-INDEX
  version: 2.0.0
  status: active

  executor:
    type: engine_adapter
    target: INDEXING-ENGINE
    operation: build_index_snapshot

  schemas:
    input: INDEX-BUILD-REQUEST@2.0.0
    output: INDEX-BUILD-RESULT@2.0.0
    error: INDEX-BUILD-ERROR@1.0.0

  characteristics:
    idempotent: true
    deterministic: false
    cancellable: true
    retryable: true
    compensatable: true
    long_running: true

  limits:
    maximum_duration: PT20M

  compatibility:
    adapter: EXEC-ADAPTER-INDEXING@1.x
```

---

# Activity Characteristics

```text
idempotent
deterministic
retryable
cancellable
compensatable
side_effecting
long_running
streaming
checkpointable
```

---

# Side-Effecting Activity

Produce cambios externos.

Ejemplos:

- publicar snapshot;
- eliminar recurso;
- enviar notificación;
- actualizar grafo.

---

# Read-Only Activity

No produce efectos permanentes.

---

# Activity Invocation

Una **Activity Invocation** representa la llamada concreta enviada al executor.

Formato recomendado:

```text
ACT-INVOKE-XXXXXX
```

---

# Contrato

```yaml
activity_invocation:
  id: ACT-INVOKE-000041

  step_run:
    id: STEP-RUN-000045

  activity:
    id: ACT-BUILD-INDEX
    version: 2.0.0

  input:
    schema: INDEX-BUILD-REQUEST@2.0.0

    values:
      knowledge_graph_snapshot_id: KG-SNAP-20260802-0001
      profile: IDX-PROFILE-RAG-STANDARD

  execution:
    idempotency_key: EXEC-000041:STEP-BUILD-INDEX
    deadline: 2026-08-02T20:12:03Z

  security:
    principal: SERVICE-INDEX-BUILDER
    tenant: TENANT-0001
```

---

# Activity Result

Formato recomendado:

```text
ACT-RESULT-XXXXXX
```

---

# Contrato

```yaml
activity_result:
  id: ACT-RESULT-000041

  invocation:
    id: ACT-INVOKE-000041

  status: succeeded

  output:
    schema: INDEX-BUILD-RESULT@2.0.0

    values:
      candidate_snapshot_id: IDX-SNAP-CANDIDATE-000041
      manifest_id: IDX-MANIFEST-000041

  artifacts:
    - ARTIFACT-REF-INDEX-BUILD-000041

  diagnostics:
    warnings: 1
    errors: 0

  timing:
    completed_at: 2026-08-02T20:08:00Z
```

---

# Activity Result States

```text
succeeded
succeeded_with_warnings
partial
failed
cancelled
timed_out
unknown
```

---

# Unknown Result

Puede ocurrir cuando:

- la llamada se envió;
- la conexión se perdió;
- no se sabe si el side effect ocurrió.

---

# Importancia

Este estado deberá tratarse de forma explícita.

No deberá reintentarse ciegamente una operación no idempotente.

---

# Unknown Outcome Resolution

Podrá requerir:

- consultar estado externo;
- reconciliar;
- usar idempotency key;
- intervención humana;
- compensación.

---

# Output Binding

Un **Output Binding** define cómo se propaga un output.

Formato recomendado:

```text
EXEC-OUTPUT-BINDING-XXXXXX
```

---

# Destinos

```text
execution_variable
workflow_output
step_input
artifact_reference
event_payload
child_execution_input
```

---

# Contrato

```yaml
output_binding:
  id: EXEC-OUTPUT-BINDING-000041

  source:
    step: STEP-BUILD-INDEX
    field: candidate_snapshot_id

  target:
    type: execution_variable
    name: candidate_snapshot_id

  required: true
```

---

# Workflow Output

Los outputs finales deberán declararse explícitamente.

---

# Contrato

```yaml
workflow_output_binding:
  target_field: published_snapshot_id

  source:
    step: STEP-PUBLISH
    field: active_snapshot_id
```

---

# No exposición automática de todos los outputs

Solo los outputs declarados deberán formar parte del Execution Result.

---

# Artifact

Un **Artifact** representa un resultado persistente, potencialmente voluminoso o reutilizable.

Formato recomendado:

```text
EXEC-ARTIFACT-XXXXXX
```

---

# Tipos

```text
document
report
manifest
snapshot
dataset
log_bundle
validation_result
index_build
graph_export
context_package
model_output
archive
```

---

# Artifact Metadata

```yaml
execution_artifact:
  id: EXEC-ARTIFACT-000041

  type: index_build

  produced_by:
    execution: EXEC-000041
    step_run: STEP-RUN-000045

  storage:
    provider: internal_object_store
    location_ref: OBJECT-000041

  integrity:
    checksum:
      algorithm: sha256
      value: ...

  schema:
    id: INDEX-BUILD-ARTIFACT
    version: 1.0.0

  security:
    tenant: TENANT-0001
    classification: internal

  retention:
    policy: EXEC-ARTIFACT-RETENTION-STANDARD
```

---

# Artifact Reference

Los workflows utilizarán referencias.

```yaml
artifact_reference:
  id: ARTIFACT-REF-INDEX-BUILD-000041

  artifact:
    id: EXEC-ARTIFACT-000041

  access:
    mode: read

  expected_checksum: ...
```

---

# Artifact Immutability

Los artefactos finalizados deberán ser inmutables o versionados.

---

# Mutable Workspace

Podrá existir durante un Step Run.

Deberá diferenciarse de un Artifact final.

---

# Artifact Lineage

Deberá registrar:

- inputs;
- producing Step;
- Activity;
- version;
- transformations.

---

# Artifact Retention

Deberá definirse por:

- tipo;
- entorno;
- auditoría;
- rollback;
- privacidad;
- coste.

---

# Commands

Un **Execution Command** representa una instrucción dirigida al Orquestador o a un Step Runtime.

Formato recomendado:

```text
EXEC-COMMAND-XXXXXX
```

---

# Command Types

```text
start_execution
start_step
cancel_execution
cancel_step
pause_execution
resume_execution
retry_step
skip_step
approve_task
reject_task
send_signal
create_checkpoint
run_compensation
```

---

# Command Contract

```yaml
execution_command:
  id: EXEC-COMMAND-000041

  type: start_step

  target:
    execution: EXEC-000041
    step_instance: STEP-INSTANCE-000041

  expected_state:
    execution: running
    step: ready

  requested_by:
    id: EXECUTION-COORDINATOR
    type: service

  issued_at: 2026-08-02T20:02:01Z
```

---

# Command Validation

Deberá comprobar:

- autorización;
- target;
- state;
- revision;
- policy;
- idempotency;
- deadline.

---

# Command Idempotency

Repetir el mismo Command ID no deberá ejecutar dos veces la operación.

---

# Command Result

```yaml
command_result:
  command: EXEC-COMMAND-000041
  status: accepted
  resulting_state: queued
```

---

# Command States

```text
created
validated
accepted
rejected
executed
failed
expired
duplicate
```

---

# Decisions

Una **Execution Decision** representa una decisión persistida que afecta al flujo.

Formato recomendado:

```text
EXEC-DECISION-XXXXXX
```

---

# Decision Types

```text
branch
continue
stop
retry
skip
compensate
wait
approve
reject
degrade
escalate
select_version
select_capability
```

---

# Contrato

```yaml
execution_decision:
  id: EXEC-DECISION-000041

  execution:
    id: EXEC-000041

  decision_type: branch

  source:
    step: STEP-EVALUATE-GATES

  outcome:
    selected_branch: publish

  inputs:
    quality_gate_status: passed

  policy:
    id: EXEC-DECISION-POLICY-PUBLICATION

  decided_at: 2026-08-02T20:09:00Z
```

---

# Decision Source

Podrá ser:

```text
rule
policy_engine
quality_gate
human
activity_result
system
agent
```

---

# Decision Determinism

Una decisión basada en inputs persistidos deberá poder reproducirse.

---

# Human Decision

Deberá registrar:

- actor;
- opciones;
- justificación;
- timestamp;
- scope.

---

# Model-Assisted Decision

Deberá registrar:

- model;
- version;
- prompt;
- output schema;
- confidence;
- policy;
- human approval cuando proceda.

---

# No decisión crítica exclusivamente opaca

---

# Condition

Una **Condition** es una expresión booleana controlada.

Formato recomendado:

```text
EXEC-CONDITION-XXXXXX
```

---

# Contrato

```yaml
execution_condition:
  id: EXEC-CONDITION-000041

  expression:
    operator: equals

    left:
      source: step_output
      step: STEP-RUN-GATES
      field: status

    right:
      constant: passed

  on_true: activate_step
  on_false: skip_step
```

---

# Condition Operators

```text
equals
not_equals
greater_than
greater_than_or_equal
less_than
less_than_or_equal
contains
not_contains
exists
not_exists
all
any
not
matches
in
```

---

# No lenguaje de scripting arbitrario

---

# Condition Evaluation

Deberá producir:

- result;
- inputs;
- evaluator version;
- timestamp.

---

# Condition Result

```yaml
condition_result:
  condition: EXEC-CONDITION-000041
  result: true
  evaluated_at: 2026-08-02T20:09:00Z
```

---

# Missing Input Policy

Valores:

```text
false
true
error
wait
use_default
```

---

# Branch

Una **Branch** representa una ruta alternativa.

---

# Branch Types

```text
exclusive
inclusive
parallel
conditional
fallback
```

---

# Exclusive Branch

Solo una ruta.

---

# Inclusive Branch

Una o varias.

---

# Parallel Branch

Varias rutas simultáneas.

---

# Fallback Branch

Se activa por fallo o degradación.

---

# Branch Contract

```yaml
execution_branch:
  id: BRANCH-PUBLICATION-DECISION

  type: exclusive

  options:
    - id: publish
      condition: EXEC-CONDITION-PUBLISH

    - id: reject
      condition: EXEC-CONDITION-REJECT

  default:
    action: fail
```

---

# Default Branch

Deberá declararse.

---

# No caída implícita

Si ninguna condición coincide, el comportamiento deberá ser explícito.

---

# Controlled Loops

Los loops deberán estar estrictamente limitados.

---

# Casos permitidos

- polling;
- paginación;
- procesamiento por lotes;
- retries de negocio;
- iteración sobre colecciones;
- refinamiento limitado.

---

# Loop Definition

```yaml
execution_loop:
  id: LOOP-PROCESS-BATCHES

  type: while

  condition:
    source: execution_variable
    name: remaining_batches
    operator: greater_than
    value: 0

  body:
    subworkflow: WF-PROCESS-BATCH@1.0.0

  limits:
    maximum_iterations: 100
    maximum_duration: PT2H
```

---

# Loop Types

```text
while
until
for_each
repeat
poll
```

---

# Maximum Iterations

Obligatorio.

---

# Loop Budget

Deberá limitar:

- iteraciones;
- tiempo;
- coste;
- elementos;
- concurrencia.

---

# Infinite Loop Protection

Error:

```text
EXECUTION_LOOP_LIMIT_EXCEEDED
```

---

# Loop State

Deberá persistir:

- iteration;
- cursor;
- processed items;
- checkpoint;
- failures.

---

# Map / Fan-Out

Un **Map Step** aplica una Activity o Subworkflow a una colección.

---

# Ejemplo

```yaml
map_step:
  id: STEP-VALIDATE-DOCUMENTS

  items:
    source: workflow_input
    field: document_ids

  activity:
    id: ACT-VALIDATE-DOCUMENT
    version: 1.0.0

  concurrency:
    maximum: 5

  failure_policy: collect_failures
```

---

# Map Instance

Cada item deberá tener identidad.

---

# Item ID

Formato recomendado:

```text
MAP-ITEM-XXXXXX
```

---

# Map Failure Policies

```text
fail_fast
collect_failures
continue
retry_failed
partial_success
```

---

# Map Ordering

Podrá ser:

```text
ordered
unordered
preserve_input_order
```

---

# Fan-Out Limit

Obligatorio.

---

# Join / Fan-In

Un **Join Step** espera y combina ramas o Map Items.

---

# Join Policies

```text
all
all_successful
minimum_count
minimum_percentage
first_success
first_completed
quorum
```

---

# Join Contract

```yaml
join_step:
  id: STEP-JOIN-VALIDATIONS

  waits_for:
    map_step: STEP-VALIDATE-DOCUMENTS

  policy:
    type: minimum_percentage
    value: 0.95

  timeout: PT30M

  aggregation:
    activity: ACT-AGGREGATE-VALIDATION-RESULTS
```

---

# Join Result

Deberá declarar:

- completed;
- successful;
- failed;
- timed out;
- omitted.

---

# Quorum

Adecuado solo cuando la semántica lo permita.

---

# Child Execution

Una **Child Execution** representa una ejecución iniciada por otra.

---

# Contrato

```yaml
child_execution:
  id: EXEC-000052

  definition:
    id: EXEC-DEF-PROCESS-DOCUMENT
    version: 1.0.0

  hierarchy:
    parent_execution_id: EXEC-000041
    root_execution_id: EXEC-000041
    parent_step_instance_id: STEP-INSTANCE-000052

  correlation:
    correlation_id: CORR-000041
    causation_id: STEP-RUN-000052
```

---

# Child Execution Modes

```text
wait_for_completion
fire_and_track
fire_and_forget
detached
```

---

# Wait for Completion

El parent espera.

---

# Fire and Track

El parent continúa, pero mantiene seguimiento.

---

# Fire and Forget

Solo permitido para efectos secundarios no críticos.

---

# Detached

La ejecución hija adquiere ciclo de vida independiente.

Requerirá política explícita.

---

# Parent Cancellation

La política deberá indicar si cancelar parent cancela children.

---

# Valores

```text
cascade
request_cancel
do_not_cancel
detach
```

---

# Parent Compensation

Podrá requerir compensar children completados.

---

# Subworkflow

Un **Subworkflow Step** encapsula una definición reutilizable.

---

# Contrato

```yaml
subworkflow_step:
  id: STEP-PROCESS-DOCUMENT

  definition:
    id: EXEC-DEF-DOCUMENT-PROCESSING
    version: 1.2.0

  input_bindings:
    document_id: ${workflow.inputs.document_id}

  execution_mode: wait_for_completion

  output_bindings:
    validation_result: ${child.outputs.validation_result}
```

---

# Subworkflow Version

Deberá fijarse.

No se recomienda:

```text
latest
```

en producción.

---

# Subworkflow Compatibility

Deberá validarse:

- input schema;
- output schema;
- security;
- environment;
- budget.

---

# Correlation

La **Correlation** permite agrupar operaciones relacionadas.

---

# Correlation Fields

```text
correlation_id
causation_id
root_execution_id
parent_execution_id
request_id
trace_id
business_key
```

---

# Business Key

Podrá identificar una operación funcional.

Ejemplo:

```text
publication:REC-0009:revision-17
```

---

# No usar Business Key como único ID técnico

---

# Causation Chain

```text
Trigger Event
    ↓
Execution
    ↓
Step Run
    ↓
Activity Invocation
    ↓
Child Execution
```

---

# Correlation Record

```yaml
execution_correlation:
  execution_id: EXEC-000041
  root_execution_id: EXEC-000041
  parent_execution_id: null
  correlation_id: CORR-000041
  causation_id: EVENT-KNOWLEDGE-READY-000041
  trace_id: TRACE-000041
```

---

# Idempotency

La idempotencia deberá formalizarse en distintos niveles.

---

# Request Idempotency

Evita crear múltiples Executions.

---

# Step Idempotency

Evita duplicar la misma operación lógica.

---

# Activity Idempotency

Permite repetir una invocación sin efecto adicional.

---

# Command Idempotency

Evita ejecutar dos veces un Command.

---

# Event Idempotency

Evita procesar dos veces el mismo evento.

---

# Idempotency Record

```yaml
idempotency_record:
  key: publication:REC-0009:revision-17

  scope:
    tenant: TENANT-0001
    definition: EXEC-DEF-KNOWLEDGE-PUBLICATION@1.0.0

  result:
    execution_id: EXEC-000041

  status: completed

  expires_at: 2026-11-01T00:00:00Z
```

---

# Idempotency States

```text
reserved
in_progress
completed
failed_retryable
failed_terminal
expired
```

---

# Key Reservation

Deberá realizarse atómicamente.

---

# Duplicate While In Progress

Podrá devolver:

- Execution ID existente;
- conflict;
- wait;
- subscription.

---

# Idempotency Retention

Deberá superar la ventana de:

- event replay;
- retries;
- delayed delivery;
- client timeout.

---

# Non-Idempotent Activities

Deberán utilizar mecanismos como:

- external idempotency key;
- precondition;
- deduplication;
- reconciliation;
- compensation;
- human review.

---

# Checkpoint

Un **Execution Checkpoint** representa un estado recuperable.

Formato recomendado:

```text
EXEC-CHECKPOINT-XXXXXX
```

---

# Contrato

```yaml
execution_checkpoint:
  id: EXEC-CHECKPOINT-000041

  execution:
    id: EXEC-000041

  state_revision: 18

  completed_steps:
    - STEP-VALIDATE
    - STEP-BUILD-GRAPH

  active_steps:
    - STEP-BUILD-INDEX

  variables:
    reference: EXEC-VARIABLE-SNAPSHOT-000041

  artifacts:
    - ARTIFACT-REF-GRAPH-SNAPSHOT-000041

  history_position:
    sequence: 142

  consistency:
    status: valid

  created_at: 2026-08-02T20:02:00Z
```

---

# Checkpoint Types

```text
automatic
manual
step_boundary
batch_boundary
pre_side_effect
post_side_effect
recovery
migration
```

---

# Step Boundary Checkpoint

Se crea después de un Step exitoso.

---

# Pre-Side-Effect Checkpoint

Permite saber qué estado existía antes de una operación crítica.

---

# Post-Side-Effect Checkpoint

Confirma el resultado.

---

# Checkpoint Content

Deberá incluir únicamente lo necesario para recuperar:

- state revision;
- Step states;
- variables;
- artifact refs;
- history offset;
- pending timers;
- pending signals;
- child executions.

---

# Checkpoint Integrity

Deberá protegerse mediante:

- checksum;
- version;
- schema;
- State Store transaction.

---

# Checkpoint Validation

Antes de reanudar deberá comprobarse:

- definition disponible;
- version compatible;
- artifacts disponibles;
- history intacto;
- no side effect incierto;
- security context vigente.

---

# Invalid Checkpoint

```text
EXECUTION_CHECKPOINT_INVALID
```

---

# Execution History

El **Execution History** representa la secuencia ordenada de hechos de una Execution.

---

# Características

- append-only;
- ordenado;
- durable;
- auditable;
- reproducible.

---

# History Entry

Formato recomendado:

```text
EXEC-HISTORY-XXXXXX
```

---

# Contrato

```yaml
execution_history_entry:
  id: EXEC-HISTORY-000142

  execution:
    id: EXEC-000041

  sequence: 142

  type: step_completed

  subject:
    step_run: STEP-RUN-000041

  data:
    status: succeeded
    output_reference: ACT-RESULT-000041

  occurred_at: 2026-08-02T20:02:00Z

  correlation:
    correlation_id: CORR-000041
    causation_id: ACT-RESULT-000041
```

---

# History Entry Types

```text
execution_created
execution_started
state_changed
step_materialized
step_ready
step_started
activity_invoked
activity_completed
activity_failed
decision_recorded
variable_updated
artifact_created
signal_received
timer_scheduled
timer_fired
checkpoint_created
child_started
child_completed
compensation_started
execution_completed
```

---

# Sequence Number

Deberá ser estrictamente creciente dentro de una Execution.

---

# History Payload

Deberá ser:

- tipado;
- mínimo;
- referencial cuando sea voluminoso.

---

# No modificación retrospectiva

Las correcciones deberán añadirse como nuevos eventos.

---

# History Compaction

Podrá existir para almacenamiento, preservando:

- semántica;
- auditabilidad;
- replay.

---

# Snapshot de estado

Podrá complementar al historial para acelerar carga.

---

# No reemplazar historial crítico

---

# Determinismo

El Orquestador deberá mantener comportamiento determinista en su lógica de coordinación.

---

# Fuentes de no determinismo

```text
current time
random values
UUID generation
external service responses
unordered collections
parallel completion order
model outputs
human decisions
environment state
```

---

# Estrategia

Toda fuente no determinista deberá convertirse en un valor persistido.

---

# Current Time

El workflow no deberá consultar libremente el reloj durante replay.

Deberá utilizar un evento o valor registrado.

---

# Random Value

Deberá persistirse.

---

# UUID

Deberá generarse como Command Result o history data.

---

# External Response

Deberá registrarse mediante Activity Result.

---

# Parallel Completion

La lógica deberá depender de eventos ordenados en el historial.

---

# Human Decision

Deberá registrarse como Decision.

---

# Deterministic Workflow Code

Si la implementación utiliza código, deberá evitar:

- I/O directo;
- red;
- reloj;
- aleatoriedad;
- threads no gobernados;
- estado global.

---

# Replay

El **Replay** reconstruye el estado aplicando el historial.

---

# Objetivos

- recuperación;
- debugging;
- auditoría;
- migración;
- verificación;
- simulación.

---

# Replay Modes

```text
state_reconstruction
dry_run
simulation
debug
migration
audit
```

---

# State Reconstruction

Reconstruye estado sin repetir Activities.

---

# Dry-Run Replay

Evalúa decisiones sin side effects.

---

# Simulation

Puede probar una definición nueva sobre datos históricos.

---

# Debug Replay

Permite inspección.

---

# Migration Replay

Transforma historial o estado hacia una nueva representación.

---

# Audit Replay

Verifica consistencia.

---

# Replay Request

```yaml
execution_replay_request:
  id: EXEC-REPLAY-REQ-000041

  execution:
    id: EXEC-000041

  mode: state_reconstruction

  until:
    history_sequence: 142

  side_effects:
    allowed: false
```

---

# Replay Result

```yaml
execution_replay_result:
  id: EXEC-REPLAY-RESULT-000041

  execution:
    id: EXEC-000041

  reconstructed_state:
    status: running
    revision: 18

  history_entries_processed: 142

  determinism:
    status: passed
```

---

# Replay Safety

El replay no deberá:

- invocar motores;
- emitir eventos externos;
- crear artifacts;
- repetir side effects;

salvo modo explícito y aislado.

---

# Non-Determinism Detected

```text
EXECUTION_REPLAY_NON_DETERMINISTIC
```

---

# Replay Compatibility

La versión de definición utilizada deberá estar disponible.

---

# Definition Archival

Las definiciones retiradas deberán conservarse mientras existan Executions o historial que dependan de ellas.

---

# Workflow Versioning

Las definiciones deberán utilizar versionado semántico o política equivalente.

---

# Cambios compatibles

Ejemplos posibles:

- metadata;
- descripción;
- nuevos campos opcionales;
- nuevos outputs opcionales;
- timeout aumentado.

---

# Cambios incompatibles

- eliminar Step;
- cambiar semántica;
- cambiar tipo de input requerido;
- cambiar Activity;
- alterar branch;
- cambiar compensación;
- cambiar binding obligatorio.

---

# Major Version

Para cambios incompatibles.

---

# Minor Version

Para cambios compatibles.

---

# Patch Version

Para correcciones sin cambio contractual.

---

# Definition Compatibility Record

```yaml
definition_compatibility:
  source: EXEC-DEF-KNOWLEDGE-PUBLICATION@1.0.0
  target: EXEC-DEF-KNOWLEDGE-PUBLICATION@1.1.0

  compatibility:
    input: backward_compatible
    output: backward_compatible
    history_replay: compatible
    in_flight_migration: not_required
```

---

# In-Flight Executions

Por defecto continuarán con su versión original.

---

# Definition Migration

Solo deberá realizarse mediante proceso explícito.

---

# Execution Migration

Formato recomendado:

```text
EXEC-MIGRATION-XXXXXX
```

---

# Contrato

```yaml
execution_migration:
  id: EXEC-MIGRATION-000041

  execution:
    id: EXEC-000041

  from_definition:
    id: EXEC-DEF-KNOWLEDGE-PUBLICATION
    version: 1.0.0

  to_definition:
    id: EXEC-DEF-KNOWLEDGE-PUBLICATION
    version: 1.1.0

  mapping:
    step_ids:
      STEP-OLD-GATE: STEP-RUN-GATES

  status: proposed
```

---

# Migration Preconditions

- estado compatible;
- Step mapping;
- variable mapping;
- output mapping;
- compensation compatibility;
- history replay;
- aprobación.

---

# No migración automática por despliegue

---

# Schema Registry

Todos los contratos deberán registrarse.

---

# Schemas

```text
execution_definition
execution_request
execution_context
execution_inputs
execution_variables
workflow_step
activity_invocation
activity_result
artifact
command
decision
condition
checkpoint
history_entry
execution_result
```

---

# Schema Versioning

Deberá ser independiente cuando proceda.

---

# Schema Compatibility

Valores:

```text
backward
forward
full
none
```

---

# Input Schema Compatibility

Importante para Requests y Parent Bindings.

---

# Output Schema Compatibility

Importante para downstream Steps y consumidores.

---

# Schema Validation Timing

Deberá realizarse:

- al registrar definición;
- al crear Execution;
- antes de Activity;
- después de Activity;
- antes de completar.

---

# Invalid Output

No deberá propagarse.

Error:

```text
EXECUTION_ACTIVITY_OUTPUT_SCHEMA_INVALID
```

---

# Nullability

Deberá declararse.

---

# Unknown Fields

La política podrá ser:

```text
reject
ignore
preserve
warn
```

---

# Recommended Production Policy

```text
reject
```

para campos críticos.

---

# Data Conversion

Las conversiones deberán ser explícitas.

---

# Execution Result

El **Execution Result** constituye la salida final canónica.

---

# Contrato ampliado

```yaml
execution_result:
  id: EXEC-RESULT-000041

  execution:
    id: EXEC-000041

  definition:
    id: EXEC-DEF-KNOWLEDGE-PUBLICATION
    version: 1.0.0

  status: succeeded

  outputs:
    schema:
      id: EXEC-OUTPUT-KNOWLEDGE-PUBLICATION
      version: 1.0.0

    values:
      published_snapshot_id: IDX-SNAP-20260802-0001
      publication_id: IDX-PUBLICATION-000041

  artifacts:
    - EXEC-ARTIFACT-000041
    - EXEC-ARTIFACT-000042

  steps:
    total: 5
    succeeded: 5
    failed: 0
    skipped: 0

  diagnostics:
    warnings: 1
    errors: 0

  timing:
    started_at: 2026-08-02T20:00:02Z
    completed_at: 2026-08-02T20:10:00Z
    duration: PT9M58S

  history:
    last_sequence: 284

  final_checkpoint:
    id: EXEC-CHECKPOINT-000052
```

---

# Partial Result

Deberá declarar:

- outputs disponibles;
- outputs ausentes;
- Steps fallidos;
- garantías reducidas.

---

# Failed Result

Podrá incluir:

- failure code;
- failed Step;
- retryability;
- compensation status;
- recovery options.

---

# Result Immutability

Una vez finalizada la Execution, el Result deberá ser inmutable.

---

# Result Correction

Deberá producir:

- nueva Execution;
- recovery execution;
- result amendment registrado.

---

# Execution Diagnostic

Formato recomendado:

```text
EXEC-DIAGNOSTIC-XXXXXX
```

---

# Códigos iniciales

```text
EXECUTION_DEFINITION_NOT_FOUND
EXECUTION_DEFINITION_INACTIVE
EXECUTION_DEFINITION_FINGERPRINT_MISMATCH
EXECUTION_INPUT_SCHEMA_INVALID
EXECUTION_OUTPUT_SCHEMA_INVALID
EXECUTION_VARIABLE_SCHEMA_INVALID
EXECUTION_REQUIRED_BINDING_UNRESOLVED
EXECUTION_BINDING_TYPE_MISMATCH
EXECUTION_ACTIVITY_NOT_FOUND
EXECUTION_ACTIVITY_OUTPUT_SCHEMA_INVALID
EXECUTION_ADAPTER_INCOMPATIBLE
EXECUTION_COMMAND_INVALID
EXECUTION_COMMAND_DUPLICATE
EXECUTION_DECISION_INVALID
EXECUTION_CONDITION_INPUT_MISSING
EXECUTION_BRANCH_UNRESOLVED
EXECUTION_LOOP_LIMIT_EXCEEDED
EXECUTION_MAP_FANOUT_LIMIT_EXCEEDED
EXECUTION_JOIN_POLICY_UNSATISFIED
EXECUTION_CHILD_FAILED
EXECUTION_IDEMPOTENCY_CONFLICT
EXECUTION_CHECKPOINT_INVALID
EXECUTION_HISTORY_GAP
EXECUTION_HISTORY_CORRUPTED
EXECUTION_REPLAY_NON_DETERMINISTIC
EXECUTION_VERSION_INCOMPATIBLE
EXECUTION_MIGRATION_REQUIRED
EXECUTION_ARTIFACT_MISSING
EXECUTION_ARTIFACT_CHECKSUM_MISMATCH
EXECUTION_REVISION_CONFLICT
EXECUTION_VARIABLE_REVISION_CONFLICT
EXECUTION_UNKNOWN_ACTIVITY_OUTCOME
```

---

# Diagnostic Contract

```yaml
execution_diagnostic:
  id: EXEC-DIAGNOSTIC-000041

  code: EXECUTION_REQUIRED_BINDING_UNRESOLVED
  severity: error

  execution:
    id: EXEC-000041

  target:
    step: STEP-BUILD-INDEX
    binding: EXEC-BINDING-000041

  message: >
    No se ha podido resolver el output snapshot_id
    de STEP-BUILD-GRAPH.

  retryable: false
```

---

# Severidades

```text
info
warning
error
critical
```

---

# Model Validation

La definición completa deberá validarse antes de activarse.

---

# Validaciones estructurales

- IDs únicos;
- schemas;
- referencias;
- Activity versions;
- adapter compatibility;
- binding paths;
- output mappings.

---

# Validaciones lógicas

- dependencias válidas;
- branches completas;
- loops limitados;
- join policies;
- children;
- compensaciones;
- no ciclos ilegales.

---

# Validaciones operativas

- budgets;
- timeouts;
- retry policies;
- artifact policies;
- retention;
- observability.

---

# Validaciones de seguridad

- Activities permitidas;
- principals;
- tenant propagation;
- secrets;
- human roles;
- environment restrictions.

---

# Execution Definition Quality Gate

```yaml
quality_gate:
  id: QG-EXECUTION-DEFINITION-0001

  criteria:
    all:
      - definition_schema_valid == true
      - definition_fingerprint_valid == true
      - step_ids_unique == true
      - activity_references_resolved == true
      - bindings_resolved == true
      - schemas_compatible == true
      - loops_bounded == true
      - branches_complete == true
      - security_policies_defined == true
      - budget_defined == true
```

---

# Execution Instance Quality Gate

```yaml
quality_gate:
  id: QG-EXECUTION-INSTANCE-0001

  criteria:
    all:
      - request_valid == true
      - definition_active == true
      - definition_version_fixed == true
      - context_valid == true
      - tenant_resolved == true
      - inputs_valid == true
      - idempotency_valid == true
      - initial_state_persisted == true
```

---

# Checkpoint Quality Gate

```yaml
quality_gate:
  id: QG-EXECUTION-CHECKPOINT-0001

  criteria:
    all:
      - state_revision_consistent == true
      - history_position_valid == true
      - variables_snapshot_valid == true
      - artifact_references_valid == true
      - pending_operations_recorded == true
      - checksum_valid == true
```

---

# Replay Quality Gate

```yaml
quality_gate:
  id: QG-EXECUTION-REPLAY-0001

  criteria:
    all:
      - history_complete == true
      - definition_available == true
      - schema_versions_available == true
      - side_effects_disabled == true
      - reconstructed_state_matches == true
      - nondeterminism_detected == false
```

---

# Casos de uso

---

# Caso de uso 1 — Binding entre Steps

`STEP-BUILD-GRAPH` produce:

```text
snapshot_id
```

`STEP-BUILD-INDEX` lo recibe mediante Output Binding e Input Binding.

---

# Caso de uso 2 — Retry de Activity

El primer Step Run falla.

Se crea un segundo Step Run con:

- nuevo Run ID;
- mismo Step Instance;
- mismo idempotency scope;
- nuevo attempt number.

---

# Caso de uso 3 — Output grande

La indexación genera un manifest grande.

Se almacena como Artifact y el Step Result conserva una referencia.

---

# Caso de uso 4 — Unknown Outcome

La publicación recibe timeout tras enviar la operación.

Antes de reintentar se consulta el estado mediante la idempotency key.

---

# Caso de uso 5 — Rama por Quality Gate

Si el Gate pasa:

```text
publish
```

Si falla:

```text
reject candidate
```

La Decision queda persistida.

---

# Caso de uso 6 — Map de documentos

Se validan cien documentos con concurrencia máxima de cinco.

---

# Caso de uso 7 — Join parcial

Se exige que al menos el 95 % de documentos sean válidos.

---

# Caso de uso 8 — Child Execution

Cada documento se procesa mediante un subworkflow independiente.

---

# Caso de uso 9 — Parent cancelado

La política indica `request_cancel` para children activos.

---

# Caso de uso 10 — Checkpoint

Tras construir el Knowledge Graph se crea un checkpoint.

Un reinicio permite continuar desde la indexación.

---

# Caso de uso 11 — Replay

Se reconstruye el estado sin volver a invocar motores.

---

# Caso de uso 12 — Non-Determinism

El workflow consultaba el reloj directamente.

El replay produce una decisión diferente y el Gate falla.

---

# Caso de uso 13 — Versión nueva

Las ejecuciones activas continúan con `1.0.0`.

Las nuevas utilizan `1.1.0`.

---

# Caso de uso 14 — Migration

Una ejecución pausada se migra mediante un mapping aprobado.

---

# Caso de uso 15 — Artifact corrupto

El checksum no coincide.

La ejecución no se reanuda hasta reparar o reconstruir.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Mezclar definición e instancia

La definición no deberá contener estados de ejecución.

---

## Reutilizar el mismo Step Run para retries

Destruye historial.

---

## Variables sin schema

Generan estado opaco.

---

## Variables como almacén de blobs

Deterioran el State Store.

---

## Bindings mediante código arbitrario

Comprometen seguridad y determinismo.

---

## Inferir dependencias solo por orden visual

Deberán declararse.

---

## Exponer todos los outputs automáticamente

Rompe encapsulación.

---

## Ignorar resultados `unknown`

Puede duplicar side effects.

---

## Tratar `null`, `missing` y `false` como equivalentes

Tienen semánticas distintas.

---

## Loops sin límites

Pueden ejecutar indefinidamente.

---

## Fan-Out sin concurrencia máxima

Puede saturar infraestructura.

---

## Join sin política

No define cuándo continuar.

---

## Child Execution sin parent linkage

Rompe trazabilidad.

---

## Fire-and-forget para procesos críticos

Impide conocer resultado.

---

## Cancelación en cascada implícita

Debe ser política explícita.

---

## Idempotency key global sin scope

Puede producir colisiones.

---

## Retención corta de idempotency

Permite duplicados tardíos.

---

## Checkpoint sin checksum

Puede recuperar estado corrupto.

---

## Checkpoint en mitad de estado inconsistente

No es recuperable.

---

## Historial mutable

Impide auditoría y replay.

---

## Replay que ejecuta Activities

Duplica efectos.

---

## Consultar reloj durante replay

Produce no determinismo.

---

## Generar UUID diferentes durante replay

Altera estado.

---

## Utilizar `latest` para Activities

Rompe reproducibilidad.

---

## Migrar ejecuciones automáticamente

Puede alterar semántica.

---

## Eliminar definiciones retiradas

Impide replay histórico.

---

## Schemas sin versión

Impiden compatibilidad.

---

## Conversiones implícitas de tipos

Pueden alterar datos.

---

## Corregir outputs inválidos en el Orquestador

La Activity deberá producir contratos válidos.

---

## Result mutable

Destruye trazabilidad.

---

# Reglas mínimas de conformidad

---

## Execution Definition versionada

Toda definición deberá tener ID, versión y fingerprint.

---

## Execution Instance identificada

Toda instancia deberá fijar definición y versión.

---

## Input Schema

Toda Execution deberá validar inputs.

---

## Bindings explícitos

Toda transferencia de datos deberá declararse.

---

## Variables tipadas

Toda variable deberá poseer schema y mutabilidad.

---

## Step Instance separada de Step Run

Los retries deberán preservar historial.

---

## Activity Invocation identificada

Toda llamada deberá tener ID e idempotency scope.

---

## Activity Result tipado

Todo output deberá validarse.

---

## Artifacts referenciados

Los outputs voluminosos deberán almacenarse externamente.

---

## Commands persistidos

Las operaciones de control deberán ser trazables.

---

## Decisions registradas

Las ramas deberán conservar la decisión.

---

## Conditions controladas

No deberán utilizar código arbitrario.

---

## Loops limitados

Todo loop deberá tener límites.

---

## Fan-Out limitado

Todo Map deberá declarar concurrencia.

---

## Join gobernado

Toda convergencia deberá declarar política.

---

## Child Execution correlacionada

Toda subejecución deberá conservar parent y root.

---

## Idempotency

Toda operación repetible deberá protegerse.

---

## Checkpoints consistentes

Toda recuperación deberá usar checkpoints validados.

---

## History append-only

Toda transición deberá quedar registrada.

---

## Replay sin side effects

La reconstrucción no deberá repetir Activities.

---

## Determinismo

Toda entrada no determinista deberá persistirse.

---

## Versiones archivadas

Las definiciones necesarias para replay deberán conservarse.

---

## Migración explícita

Las ejecuciones activas no deberán cambiar de definición automáticamente.

---

## Result inmutable

Toda finalización deberá producir un resultado estable.

---

# Conformidad de Execution Definition

Será conforme cuando:

- tenga ID;
- tenga versión;
- tenga fingerprint;
- declare schemas;
- declare Steps;
- declare Activities;
- declare bindings;
- declare políticas;
- declare budgets;
- declare compatibilidad.

---

# Conformidad de Execution Instance

Será conforme cuando:

- tenga ID;
- preserve Request;
- preserve Trigger;
- fije Definition;
- preserve Context;
- declare revisión;
- preserve correlation;
- preserve hierarchy;
- produzca Result.

---

# Conformidad de Input Binding

Será conforme cuando:

- tenga ID;
- declare source;
- declare target;
- declare tipo;
- declare obligatoriedad;
- declare transformación;
- preserve seguridad;
- sea compatible.

---

# Conformidad de Execution Variable

Será conforme cuando:

- tenga nombre;
- tenga tipo;
- declare mutabilidad;
- declare valor;
- declare origen;
- tenga revisión;
- cumpla schema.

---

# Conformidad de Step Instance

Será conforme cuando:

- identifique Execution;
- referencie Step Definition;
- declare estado;
- declare dependencias;
- preserve Runs;
- preserve revisión.

---

# Conformidad de Step Run

Será conforme cuando:

- tenga ID;
- identifique Step Instance;
- declare attempt;
- identifique Activity;
- identifique Adapter;
- declare estado;
- declare timing;
- preserve Command;
- preserve Result.

---

# Conformidad de Activity Invocation

Será conforme cuando:

- tenga ID;
- identifique Step Run;
- identifique Activity y versión;
- valide input;
- declare idempotency;
- declare deadline;
- preserve identidad;
- preserve tenant.

---

# Conformidad de Activity Result

Será conforme cuando:

- tenga ID;
- identifique Invocation;
- declare status;
- cumpla output schema;
- declare artifacts;
- declare diagnostics;
- declare timing.

---

# Conformidad de Artifact

Será conforme cuando:

- tenga ID;
- tenga tipo;
- declare producer;
- declare storage reference;
- declare checksum;
- declare schema;
- preserve seguridad;
- declare retención.

---

# Conformidad de Decision

Será conforme cuando:

- tenga ID;
- identifique Execution;
- declare tipo;
- declare inputs;
- declare outcome;
- declare source;
- declare policy;
- declare timestamp.

---

# Conformidad de Checkpoint

Será conforme cuando:

- tenga ID;
- identifique Execution;
- declare state revision;
- declare Step states;
- declare variables;
- declare Artifacts;
- declare history position;
- tenga checksum;
- sea consistente.

---

# Conformidad de Execution History

Será conforme cuando:

- sea append-only;
- tenga secuencias;
- no tenga gaps;
- utilice schemas;
- preserve correlation;
- preserve causation;
- permita replay.

---

# Conformidad de Replay

Será conforme cuando:

- declare Execution;
- declare modo;
- declare límite;
- deshabilite side effects;
- utilice definición original;
- procese historial completo;
- verifique determinismo.

---

# Lista de comprobación

Antes de aprobar el Execution Model deberá comprobarse:

```text
[ ] Las Execution Definitions tienen ID.
[ ] Las Execution Definitions están versionadas.
[ ] Las definiciones tienen fingerprint.
[ ] Las definiciones publicadas son inmutables.
[ ] Las Executions fijan definición y versión.
[ ] Las Executions utilizan revisión de estado.
[ ] El Execution Context está tipado.
[ ] El tenant es inmutable.
[ ] Los inputs cumplen schema.
[ ] Los valores de seguridad no pueden sobrescribirse.
[ ] Los Input Bindings son explícitos.
[ ] Los Output Bindings son explícitos.
[ ] Los bindings no ejecutan código arbitrario.
[ ] Las Execution Variables están tipadas.
[ ] La mutabilidad está declarada.
[ ] Las actualizaciones usan revisión.
[ ] Los Step Definitions referencian Activities.
[ ] Los Step Instances están separados de Runs.
[ ] Cada retry crea un nuevo Step Run.
[ ] Las Activities están versionadas.
[ ] Las invocaciones tienen idempotency key.
[ ] Los Activity Results cumplen schema.
[ ] Los estados unknown están tratados.
[ ] Los outputs grandes utilizan Artifacts.
[ ] Los Artifacts tienen checksum.
[ ] Los Artifacts tienen lineage.
[ ] Los Commands están identificados.
[ ] Los Commands son idempotentes.
[ ] Las Decisions están persistidas.
[ ] Las Conditions utilizan operadores permitidos.
[ ] Las Branches tienen default explícito.
[ ] Los Loops tienen máximo de iteraciones.
[ ] Los Loops tienen budget.
[ ] Los Map Steps limitan concurrencia.
[ ] Los Join Steps declaran política.
[ ] Las Child Executions conservan parent y root.
[ ] Las políticas de cancelación de children están definidas.
[ ] Las subejecuciones fijan versión.
[ ] La correlación está presente.
[ ] La causación está presente.
[ ] Las idempotency keys tienen scope.
[ ] La retención de idempotencia está definida.
[ ] Los Checkpoints tienen checksum.
[ ] Los Checkpoints corresponden a estados consistentes.
[ ] El historial es append-only.
[ ] El historial no contiene gaps.
[ ] Las fuentes no deterministas se persisten.
[ ] El Replay no repite side effects.
[ ] Las definiciones históricas se conservan.
[ ] La compatibilidad entre versiones está declarada.
[ ] Las migraciones son explícitas.
[ ] Todos los schemas están versionados.
[ ] El Execution Result es inmutable.
[ ] Los Quality Gates del modelo han pasado.
```

---

# Arquitectura final de la Parte II

```text
Execution Definition
        ↓
Definition Validation
        ↓
Execution Request
        ↓
Execution Instance
        ↓
Execution Context
        ↓
Execution Inputs
        ↓
Input Bindings
        ↓
Execution Variables
        ↓
Step Instances
        ↓
Step Runs
        ↓
Activity Invocations
        ↓
Activity Results
        ↓
Output Bindings
        ↓
Artifacts
        ↓
Commands and Decisions
        ↓
Branches · Loops · Map · Join
        ↓
Child Executions
        ↓
Checkpoints
        ↓
Execution History
        ↓
Replay
        ↓
Execution Result
```

---

# Transición hacia la Parte III

Esta segunda parte ha definido:

- Execution Definitions;
- Definition Manifests;
- Execution Instances;
- revisiones;
- Execution Contexts;
- Context Inheritance;
- Execution Inputs;
- Input Precedence;
- Input Bindings;
- Output Bindings;
- Execution Variables;
- Step Definitions;
- Step Instances;
- Step Runs;
- Activity Definitions;
- Activity Invocations;
- Activity Results;
- estados unknown;
- Artifacts;
- Artifact References;
- Commands;
- Decisions;
- Conditions;
- Branches;
- Controlled Loops;
- Map y Fan-Out;
- Join y Fan-In;
- Child Executions;
- Subworkflows;
- Correlation;
- Causation;
- Idempotency;
- Checkpoints;
- Execution History;
- determinismo;
- Replay;
- versionado;
- compatibilidad;
- migrations;
- schemas;
- diagnósticos;
- Quality Gates;
- casos de uso;
- antipatrones;
- reglas de conformidad.

La Parte III desarrollará:

- Workflow Graph;
- Directed Acyclic Graphs;
- Step Dependencies;
- Dependency Types;
- Dependency Resolution;
- Activation Rules;
- Parallel Branches;
- Join Semantics;
- Conditional Paths;
- Dynamic Steps;
- Subworkflow Composition;
- Pipeline Stages;
- Quality Gates dentro del DAG;
- Graph Validation;
- Cycle Detection;
- Topological Ordering;
- Critical Path;
- Execution Planning;
- DAG Materialization;
- Runtime Expansion;
- Workflow Templates;
- Workflow Composition;
- reutilización;
- librerías de workflows;
- contratos completos de Workflows, Pipelines y DAGs.

---

# Conclusión

El Execution Model establece la representación formal y durable de todo proceso coordinado por NovaCoquinaria.

Su ciclo puede resumirse así:

```text
Resolver definición
        ↓
Crear instancia
        ↓
Validar inputs
        ↓
Aplicar bindings
        ↓
Materializar Steps
        ↓
Invocar Activities
        ↓
Persistir resultados
        ↓
Crear Artifacts
        ↓
Registrar decisiones
        ↓
Actualizar variables
        ↓
Crear checkpoints
        ↓
Conservar historial
        ↓
Producir resultado
```

Las Execution Definitions describen procesos.

Las Execution Instances representan ejecuciones concretas.

El Execution Context fija identidad, seguridad y políticas.

Los Inputs aportan datos iniciales.

Los Bindings conectan pasos.

Las Variables conservan estado mínimo de coordinación.

Los Step Instances representan operaciones dentro de una ejecución.

Los Step Runs preservan intentos y reintentos.

Las Activities encapsulan capacidades.

Las Invocations representan llamadas concretas.

Los Results preservan outputs y diagnósticos.

Los Artifacts externalizan datos persistentes.

Los Commands controlan la ejecución.

Las Decisions formalizan ramas y cambios de flujo.

Los Loops permiten iteración limitada.

Map y Join permiten procesamiento paralelo gobernado.

Las Child Executions permiten composición.

La Idempotency evita duplicaciones.

Los Checkpoints permiten recuperación.

El History permite auditoría y replay.

El determinismo permite reconstruir estado.

El versionado preserva reproducibilidad.

Una Execution correctamente modelada deberá poder responder:

```text
¿Qué definición utiliza?

¿Qué versión y fingerprint tiene?

¿Qué inputs recibió?

¿De dónde procede cada input?

¿Qué variables mantiene?

¿Qué Steps se materializaron?

¿Qué Runs tuvo cada Step?

¿Qué Activity se invocó?

¿Qué outputs produjo?

¿Qué Artifacts creó?

¿Qué decisiones se tomaron?

¿Qué ramas se activaron?

¿Qué subejecuciones se iniciaron?

¿Qué checkpoint permite reanudar?

¿Qué historial permite reconstruirla?

¿Puede reproducirse de forma determinista?

¿Qué resultado final produjo?
```

Con esta segunda parte queda formalizado el modelo interno mediante el que NovaCoquinaria representará ejecuciones, Steps, Activities, variables, artefactos, decisiones, subejecuciones, checkpoints e historial de forma versionada, durable, trazable y reproducible.

La siguiente parte definirá cómo estos elementos se organizan en **Workflows, Pipelines y DAGs ejecutables**, estableciendo dependencias, paralelismo, ramas, uniones, composición, validación y planificación del grafo completo.

---

# Parte III — Workflows, Pipelines y DAGs: dependencias, composición, paralelismo, ramas, validación y planificación del grafo

---

# Introducción

La Parte II ha formalizado el modelo interno del Orquestador de Ejecución mediante:

- Execution Definitions;
- Execution Instances;
- Execution Contexts;
- Inputs;
- Bindings;
- Variables;
- Step Definitions;
- Step Instances;
- Step Runs;
- Activities;
- Activity Invocations;
- Activity Results;
- Artifacts;
- Commands;
- Decisions;
- Conditions;
- Branches;
- Loops;
- Map;
- Join;
- Child Executions;
- Checkpoints;
- Execution History;
- Replay;
- versionado;
- compatibilidad.

Esta tercera parte desarrolla cómo estos elementos se organizan en estructuras ejecutables completas.

El Orquestador deberá poder transformar una definición declarativa como:

```text
Validar conocimiento
        ↓
Construir Knowledge Graph
        ↓
Construir índices
        ↓
Ejecutar Quality Gates
        ↓
Publicar
```

en un grafo formal capaz de expresar:

- secuencias;
- dependencias;
- ramas;
- paralelismo;
- convergencia;
- condiciones;
- subworkflows;
- fallbacks;
- Quality Gates;
- compensaciones;
- esperas;
- tareas humanas;
- expansión dinámica controlada.

Esta estructura se denominará:

```text
Workflow Graph
```

y, cuando no admita ciclos directos de ejecución, podrá representarse como:

```text
Directed Acyclic Graph
```

o:

```text
DAG
```

Conceptualmente:

```text
Workflow Definition
        ↓
Workflow Validation
        ↓
Graph Construction
        ↓
Dependency Analysis
        ↓
Cycle Detection
        ↓
Topological Planning
        ↓
DAG Materialization
        ↓
Runtime Activation
        ↓
Step Execution
        ↓
Graph Completion
```

El DAG no representará únicamente un diagrama visual.

Será el contrato ejecutable que determinará:

- cuándo puede activarse un Step;
- qué resultados necesita;
- qué ramas deben completarse;
- cuándo puede continuar el flujo;
- qué pasos pueden ejecutarse simultáneamente;
- qué pasos deben omitirse;
- qué condiciones pueden bloquearlo;
- cuándo una ejecución puede considerarse finalizada.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- formalizar Workflow Graphs;
- definir Directed Acyclic Graphs;
- establecer Workflow Nodes;
- establecer Workflow Edges;
- definir Dependency Types;
- formalizar Dependency Expressions;
- establecer Activation Rules;
- definir Completion Rules;
- formalizar Step Readiness;
- definir dependencias obligatorias y opcionales;
- establecer dependencias de datos;
- establecer dependencias de control;
- establecer dependencias temporales;
- definir ramas paralelas;
- formalizar Join Semantics;
- definir Conditional Paths;
- establecer fallback paths;
- formalizar Quality Gates dentro del grafo;
- definir Wait Nodes;
- definir Human Task Nodes;
- establecer Subworkflow Composition;
- formalizar Pipeline Stages;
- definir Stage Gates;
- establecer Workflow Templates;
- formalizar Workflow Composition;
- definir Workflow Libraries;
- establecer reutilización;
- definir Dynamic Steps;
- regular Runtime Expansion;
- establecer límites de expansión;
- formalizar DAG Materialization;
- definir Execution Planning;
- establecer Topological Ordering;
- calcular Critical Path;
- detectar ciclos;
- detectar nodos inaccesibles;
- detectar dependencias imposibles;
- validar terminación;
- definir diagnósticos;
- establecer Quality Gates;
- formalizar conformidad de Workflows, Pipelines y DAGs.

---

# Principios de diseño de Workflows y DAGs

Toda definición deberá respetar los siguientes principios.

---

## Grafo explícito

Las dependencias no deberán inferirse únicamente por:

- posición;
- orden del archivo;
- nombre;
- convención visual.

---

## Nodos identificables

Todo nodo deberá disponer de:

- ID;
- tipo;
- definición;
- estado;
- reglas de activación;
- reglas de finalización.

---

## Aristas tipadas

Toda relación entre nodos deberá declarar su semántica.

---

## Datos y control diferenciados

Una dependencia de control no equivale necesariamente a una dependencia de datos.

---

## Acyclicidad del grafo materializado

El DAG ejecutable no deberá contener ciclos directos.

Los loops deberán representarse mediante primitivas controladas.

---

## Paralelismo explícito

Los Steps independientes podrán ejecutarse en paralelo únicamente cuando el grafo lo permita.

---

## Convergencia gobernada

Todo Join deberá declarar qué resultados necesita para continuar.

---

## Ramas completas

Toda decisión deberá declarar:

- opciones;
- condiciones;
- prioridad;
- comportamiento por defecto.

---

## No rutas implícitas

Una rama no seleccionada deberá quedar formalmente:

```text
skipped
```

o:

```text
not_activated
```

---

## Terminación verificable

Toda definición deberá disponer de uno o varios nodos finales alcanzables.

---

## Calidad como parte del flujo

Los Quality Gates deberán representarse como nodos o reglas explícitas.

---

## Fallos diferenciados de decisiones

Una rama funcional no deberá modelarse mediante una excepción técnica.

---

## Composición antes que duplicación

Los procesos reutilizables deberán encapsularse como:

- Activities;
- Subworkflows;
- Templates;
- Pipelines.

---

## Expansión dinámica limitada

Los nodos creados en runtime deberán respetar:

- schemas;
- allowlists;
- budgets;
- límites;
- políticas.

---

## Planificación reproducible

La materialización inicial del DAG deberá poder reconstruirse.

---

## Seguridad propagada

Toda rama y subworkflow deberá mantener:

- tenant;
- identity;
- policies;
- classification;
- budget.

---

## Estado durable

El progreso del grafo no deberá depender de un scheduler en memoria.

---

## Compensación separada

El grafo principal y el grafo de compensación deberán poder relacionarse sin confundirse.

---

# Arquitectura conceptual

```text
┌───────────────────────────────────────────────┐
│             Workflow Definition               │
│                                               │
│ Nodes · Edges · Conditions · Policies         │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Workflow Validator                │
│                                               │
│ References · Cycles · Reachability · Schemas  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Workflow Compiler                │
│                                               │
│ Normalize · Expand · Resolve · Materialize    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                  Workflow DAG                 │
│                                               │
│ Nodes · Typed Edges · Activation Rules        │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Execution Planner                │
│                                               │
│ Topology · Parallel Groups · Critical Path    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                 DAG Runtime                   │
│                                               │
│ Readiness · Scheduling · Joins · Completion   │
└───────────────────────────────────────────────┘
```

---

# Workflow Graph

Un **Workflow Graph** representa la estructura lógica completa de una definición.

Formato recomendado:

```text
WF-GRAPH-XXXXXX
```

---

# Contrato

```yaml
workflow_graph:
  id: WF-GRAPH-KNOWLEDGE-PUBLICATION

  version: 1.0.0

  definition:
    id: EXEC-DEF-KNOWLEDGE-PUBLICATION
    version: 1.0.0

  nodes:
    - WF-NODE-VALIDATE
    - WF-NODE-BUILD-GRAPH
    - WF-NODE-BUILD-INDEX
    - WF-NODE-RUN-GATES
    - WF-NODE-PUBLISH

  edges:
    - WF-EDGE-0001
    - WF-EDGE-0002
    - WF-EDGE-0003
    - WF-EDGE-0004

  entry_nodes:
    - WF-NODE-VALIDATE

  terminal_nodes:
    - WF-NODE-PUBLISH

  status: valid
```

---

# Workflow Graph Types

```text
linear
dag
branching
parallel
staged
hierarchical
event_waiting
interactive
compensating
dynamic_bounded
```

---

# Linear Workflow

Representa una secuencia simple.

```text
A → B → C
```

---

# DAG Workflow

Permite:

- múltiples dependencias;
- paralelismo;
- convergencia;
- ramas.

---

# Branching Workflow

Incluye decisiones.

---

# Parallel Workflow

Incluye ramas concurrentes.

---

# Staged Workflow

Agrupa Steps por fases.

---

# Hierarchical Workflow

Incluye Subworkflows.

---

# Event-Waiting Workflow

Incluye esperas por eventos o señales.

---

# Interactive Workflow

Incluye Human Tasks.

---

# Compensating Workflow

Coordina acciones compensatorias.

---

# Dynamic Bounded Workflow

Permite expansión runtime limitada.

---

# Workflow Node

Un **Workflow Node** representa una unidad lógica dentro del grafo.

Formato recomendado:

```text
WF-NODE-XXXXXX
```

---

# Node Contract

```yaml
workflow_node:
  id: WF-NODE-BUILD-INDEX

  type: activity

  definition:
    step_id: STEP-BUILD-INDEX

  activation:
    rule: all_required_dependencies_satisfied

  completion:
    success_states:
      - succeeded
      - succeeded_with_warnings

  required: true
```

---

# Node Types

```text
start
activity
decision
parallel_split
join
quality_gate
wait
timer
signal
human_task
map
loop
subworkflow
compensation
end
```

---

# Start Node

Representa la entrada explícita.

Podrá omitirse en definiciones simples si existen `entry_nodes`.

---

# Activity Node

Invoca una Activity.

---

# Decision Node

Evalúa una o varias condiciones.

---

# Parallel Split Node

Activa varias ramas.

---

# Join Node

Espera resultados de varias ramas.

---

# Quality Gate Node

Evalúa criterios antes de continuar.

---

# Wait Node

Espera un evento, señal o condición.

---

# Timer Node

Espera hasta una fecha o duración.

---

# Signal Node

Emite o consume una señal.

---

# Human Task Node

Crea una tarea humana.

---

# Map Node

Materializa operaciones sobre una colección.

---

# Loop Node

Coordina una repetición limitada.

---

# Subworkflow Node

Inicia una Child Execution.

---

# Compensation Node

Ejecuta una acción compensatoria.

---

# End Node

Representa una terminación.

---

# Node Metadata

Podrá incluir:

- nombre;
- descripción;
- dominio;
- owner;
- tags;
- criticidad;
- observabilidad;
- documentación.

---

# Node Required

Un nodo requerido deberá alcanzar un estado final compatible para que la ejecución global tenga éxito.

---

# Optional Node

Puede:

- fallar;
- omitirse;
- expirar;

sin bloquear necesariamente el workflow.

---

# Conditional Node

Solo es requerido si se activa.

---

# Workflow Edge

Una **Workflow Edge** representa una dependencia o transición entre nodos.

Formato recomendado:

```text
WF-EDGE-XXXXXX
```

---

# Contrato

```yaml
workflow_edge:
  id: WF-EDGE-000041

  from:
    node: WF-NODE-BUILD-GRAPH

  to:
    node: WF-NODE-BUILD-INDEX

  type: success_dependency

  required: true
```

---

# Edge Types

```text
control
success_dependency
completion_dependency
failure_dependency
data
condition
signal
temporal
compensation
fallback
cancellation
```

---

# Control Edge

Indica orden lógico.

---

# Success Dependency

El nodo origen debe finalizar correctamente.

---

# Completion Dependency

El nodo origen debe alcanzar cualquier estado terminal permitido.

---

# Failure Dependency

La ruta se activa cuando el origen falla.

---

# Data Dependency

El destino necesita un output del origen.

---

# Condition Edge

La transición depende de una condición.

---

# Signal Edge

La transición depende de una señal.

---

# Temporal Edge

La activación depende de tiempo o deadline.

---

# Compensation Edge

Relaciona un Step con su compensación.

---

# Fallback Edge

Activa una alternativa.

---

# Cancellation Edge

Propaga o reacciona a cancelación.

---

# Edge Direction

Toda arista deberá ser dirigida.

```text
source → target
```

---

# Edge Guard

Una arista podrá incluir una condición.

```yaml
guard:
  condition:
    id: EXEC-CONDITION-000041
```

---

# Edge Priority

Cuando varias aristas sean candidatas podrá establecerse:

```yaml
priority: 100
```

---

# No prioridad implícita por orden

---

# Default Edge

Una Decision podrá definir una arista por defecto.

---

# Edge Data Mapping

Una dependencia de datos podrá incluir bindings.

```yaml
data_mapping:
  source_field: snapshot_id
  target_field: knowledge_graph_snapshot_id
```

---

# Dependency Types

Las dependencias deberán modelarse con precisión.

---

# Required Dependency

Debe satisfacerse.

---

# Optional Dependency

Puede aportar información, pero no bloquea indefinidamente.

---

# Hard Dependency

Sin ella el nodo no puede activarse.

---

# Soft Dependency

Puede esperarse durante una ventana y continuar sin ella.

---

# Success Dependency

Requiere éxito.

---

# Completion Dependency

Requiere terminación, independientemente del resultado.

---

# Data Dependency

Requiere un dato.

---

# Policy Dependency

Requiere una decisión de política.

---

# Human Dependency

Requiere input humano.

---

# Temporal Dependency

Requiere que se cumpla una condición temporal.

---

# Capability Dependency

Requiere una capacidad operativa.

---

# Artifact Dependency

Requiere un Artifact válido.

---

# Dependency Contract

```yaml
step_dependency:
  id: DEP-BUILD-INDEX-GRAPH

  source:
    node: WF-NODE-BUILD-GRAPH

  target:
    node: WF-NODE-BUILD-INDEX

  type: data

  required: true

  satisfaction:
    source_state:
      in:
        - succeeded
        - succeeded_with_warnings

    output:
      field: snapshot_id
      required: true
```

---

# Dependency Expression

Un nodo podrá combinar dependencias.

---

# ALL

Todas deben satisfacerse.

```yaml
depends_on:
  all:
    - WF-NODE-A
    - WF-NODE-B
```

---

# ANY

Al menos una.

```yaml
depends_on:
  any:
    - WF-NODE-A
    - WF-NODE-B
```

---

# NONE

Ninguna deberá haber alcanzado una condición.

---

# QUORUM

Se requiere un número mínimo.

```yaml
depends_on:
  quorum:
    nodes:
      - WF-NODE-A
      - WF-NODE-B
      - WF-NODE-C
    minimum: 2
```

---

# PERCENTAGE

Se requiere un porcentaje.

---

# EXPRESSION

Combinación lógica.

```yaml
depends_on:
  expression:
    all:
      - node: WF-NODE-A
        state: succeeded

      - any:
          - node: WF-NODE-B
            state: succeeded
          - node: WF-NODE-C
            state: succeeded
```

---

# Dependency Satisfaction

Una dependencia deberá quedar en uno de estos estados:

```text
pending
satisfied
unsatisfied
impossible
waived
expired
```

---

# Impossible Dependency

Ocurre cuando ya no puede satisfacerse.

Ejemplo:

- requiere éxito de A;
- A terminó en failed;
- no existe retry ni fallback.

---

# Dependency Waiver

Solo podrá aplicarse mediante:

- política;
- override autorizado;
- Quality Gate;
- operación administrativa.

---

# No waiver de seguridad implícito

---

# Dependency Resolution

El **Dependency Resolver** calculará continuamente qué nodos pueden activarse.

---

# Inputs

- estados de nodos;
- resultados;
- condiciones;
- señales;
- timers;
- políticas;
- capabilities;
- artifacts.

---

# Output

Para cada nodo:

```text
blocked
pending
ready
skipped
impossible
```

---

# Readiness Evaluation

```yaml
step_readiness:
  node: WF-NODE-BUILD-INDEX

  dependencies:
    total: 2
    satisfied: 2
    pending: 0
    impossible: 0

  activation_rule:
    result: true

  status: ready
```

---

# Step Readiness

Un Step estará `ready` cuando:

- todas sus dependencias obligatorias estén satisfechas;
- su condición de activación sea verdadera;
- no esté cancelado;
- no esté bloqueado por policy;
- exista budget;
- exista capability;
- sus bindings puedan resolverse.

---

# Ready no equivale a Running

El Scheduler decidirá cuándo encolarlo.

---

# Step Activation Rule

Formato recomendado:

```text
WF-ACTIVATION-RULE-XXXXXX
```

---

# Contrato

```yaml
activation_rule:
  id: WF-ACTIVATION-RULE-BUILD-INDEX

  criteria:
    all:
      - dependencies_satisfied
      - condition_true
      - required_inputs_resolved
      - budget_available
      - capability_available
      - execution_not_cancelling
```

---

# Activation States

```text
not_evaluated
pending
eligible
activated
rejected
expired
```

---

# Activation Decision

Toda activación deberá quedar registrada.

```yaml
activation_decision:
  node: WF-NODE-BUILD-INDEX
  decision: activate
  reason: all_requirements_satisfied
  decided_at: 2026-08-02T20:02:00Z
```

---

# No activación repetida

Un nodo no deberá materializarse varias veces salvo:

- Map;
- Loop;
- retry;
- runtime expansion autorizada.

---

# Completion Rule

Define cuándo un nodo se considera completado.

---

# Contrato

```yaml
completion_rule:
  node: WF-NODE-BUILD-INDEX

  successful_states:
    - succeeded
    - succeeded_with_warnings

  terminal_states:
    - succeeded
    - succeeded_with_warnings
    - failed
    - cancelled
    - timed_out
    - skipped
```

---

# Node Outcome

Podrá distinguir:

```text
success
warning
failure
skip
cancel
timeout
partial
```

---

# Workflow Completion

Una ejecución podrá completarse cuando:

- todos los terminal nodes requeridos hayan alcanzado estado terminal;
- no queden nodos activos;
- no existan dependencias pendientes alcanzables;
- se haya evaluado la política final.

---

# Workflow Success

Requiere que todos los nodos requeridos activados hayan finalizado en estados aceptados.

---

# Workflow Partial

Podrá declararse cuando:

- algunos nodos opcionales fallan;
- un Map alcanza umbral parcial;
- existen outputs parciales válidos;
- el Result Schema lo permite.

---

# Workflow Failure

Se produce cuando:

- falla un nodo requerido sin fallback;
- una dependencia obligatoria se vuelve imposible;
- un Quality Gate bloqueante falla;
- se supera budget;
- se pierde consistencia.

---

# Workflow Skip Semantics

Un nodo podrá quedar `skipped` por:

- rama no seleccionada;
- condición falsa;
- dependencia no aplicable;
- policy;
- optimización;
- resultado previo.

---

# Skip Reason

Deberá registrarse.

```yaml
skip_reason:
  code: BRANCH_NOT_SELECTED
  decision: EXEC-DECISION-000041
```

---

# DAG

Un **Directed Acyclic Graph** será la representación ejecutable normalizada de un Workflow.

Formato recomendado:

```text
WF-DAG-XXXXXX
```

---

# Contrato

```yaml
workflow_dag:
  id: WF-DAG-KNOWLEDGE-PUBLICATION-0001

  workflow:
    id: EXEC-DEF-KNOWLEDGE-PUBLICATION
    version: 1.0.0

  nodes:
    count: 7

  edges:
    count: 8

  entry_nodes:
    - WF-NODE-START

  terminal_nodes:
    - WF-NODE-END-SUCCESS
    - WF-NODE-END-REJECTED

  validation:
    acyclic: true
    reachable: true
    terminable: true

  fingerprint: ...
```

---

# DAG Normalization

El Workflow Compiler podrá transformar construcciones de alto nivel en nodos y aristas básicos.

---

# Ejemplo: Parallel Block

Definición:

```yaml
parallel:
  - STEP-A
  - STEP-B
```

Normalización:

```text
Parallel Split
    ├── STEP-A
    └── STEP-B
           ↓
         Join
```

---

# Ejemplo: Decision

Definición:

```yaml
decision:
  if: gate_passed
  then: publish
  else: reject
```

Normalización:

```text
Decision
    ├── condition=true  → Publish
    └── default         → Reject
```

---

# Ejemplo: Map

Definición abstracta:

```text
Map documents
```

Materialización runtime:

```text
Map Controller
    ├── Item 1
    ├── Item 2
    ├── Item 3
    └── Join
```

---

# DAG Fingerprint

Deberá incluir:

- nodes;
- edges;
- node versions;
- conditions;
- bindings;
- policies;
- joins;
- terminal rules.

---

# Cycle Detection

El grafo materializado deberá ser acíclico.

---

# Algoritmos posibles

```text
depth-first search
Kahn topological algorithm
strongly connected components
```

---

# Cycle Diagnostic

```text
WORKFLOW_GRAPH_CYCLE_DETECTED
```

---

# Ejemplo

```text
A → B → C → A
```

---

# Ciclos permitidos conceptualmente

Los loops controlados no deberán representarse como ciclos directos en el DAG.

Podrán modelarse mediante:

- Loop Controller;
- Child Executions por iteración;
- Map Controller;
- estado de cursor;
- nueva materialización limitada.

---

# Self-Dependency

Un nodo no deberá depender de sí mismo.

Error:

```text
WORKFLOW_NODE_SELF_DEPENDENCY
```

---

# Indirect Cycle

También deberá detectarse.

---

# Reachability Analysis

Todo nodo debería ser alcanzable desde un entry node, salvo nodos especiales documentados.

---

# Unreachable Node

```text
WORKFLOW_NODE_UNREACHABLE
```

---

# Dead-End Node

Un nodo no terminal que no conduce a ninguna salida.

```text
WORKFLOW_NODE_DEAD_END
```

---

# Terminal Reachability

Desde todo nodo activable deberá existir al menos una ruta potencial hacia:

- terminación;
- compensación;
- fallo explícito.

---

# Non-Terminating Path

```text
WORKFLOW_PATH_NON_TERMINATING
```

---

# Topological Ordering

El DAG deberá permitir un orden topológico.

---

# Uso

- validar dependencias;
- planificar;
- estimar etapas;
- calcular critical path;
- crear parallel groups.

---

# Topological Order

Ejemplo:

```text
1. START
2. VALIDATE
3. BUILD_GRAPH
4. BUILD_INDEX
5. RUN_GATES
6. PUBLISH
7. END
```

---

# Múltiples órdenes válidos

Un DAG paralelo puede admitir varios.

El Orquestador podrá utilizar un orden estable para:

- reproducibilidad;
- planificación;
- explicación.

---

# Stable Topological Ordering

Podrá usar como desempate:

- explicit priority;
- node ID;
- definition order estable.

---

# No implicar ejecución secuencial

El orden topológico no elimina paralelismo.

---

# Execution Level

Podrá calcularse por niveles.

```text
Level 0 → START
Level 1 → A, B
Level 2 → C
Level 3 → END
```

---

# Parallel Group

Formato recomendado:

```text
WF-PARALLEL-GROUP-XXXXXX
```

---

# Contrato

```yaml
parallel_group:
  id: WF-PARALLEL-GROUP-000041

  nodes:
    - WF-NODE-VALIDATE-GRAPH
    - WF-NODE-VALIDATE-INDEX

  maximum_concurrency: 2

  join:
    node: WF-NODE-JOIN-VALIDATIONS
```

---

# Parallel Split

Activa múltiples ramas.

---

# Parallel Split Contract

```yaml
parallel_split:
  id: WF-NODE-SPLIT-BUILD

  branches:
    - id: graph_branch
      entry_node: WF-NODE-BUILD-GRAPH

    - id: metadata_branch
      entry_node: WF-NODE-BUILD-METADATA

  activation: all
```

---

# Parallel Branch Identity

Cada rama deberá tener ID.

---

# Branch Status

```text
not_started
running
succeeded
failed
partial
cancelled
skipped
```

---

# Branch Isolation

Los outputs no deberán colisionar sin bindings o reglas explícitas.

---

# Shared Variable Writes

Deberán:

- evitarse;
- serializarse;
- usar atomic updates;
- aplicar merge policy.

---

# Race Condition

El Workflow Validator deberá detectar escrituras potencialmente conflictivas cuando sea posible.

---

# Variable Merge Policies

```text
reject_conflict
last_writer_forbidden
append
union
merge_object
aggregate
custom_activity
```

---

# No `last writer wins` implícito

---

# Join Semantics

Un **Join Node** controla la convergencia de varias ramas.

---

# Join Types

```text
all
all_successful
any
first_success
first_completed
quorum
minimum_percentage
collect
race
```

---

# Join `all`

Espera a todas las ramas activadas.

---

# Join `all_successful`

Exige éxito de todas.

---

# Join `any`

Continúa cuando una termina en estado aceptado.

---

# Join `first_success`

Continúa con el primer éxito.

---

# Join `first_completed`

Continúa con la primera terminación.

---

# Join `quorum`

Exige un número mínimo.

---

# Join `minimum_percentage`

Exige porcentaje.

---

# Join `collect`

Espera y agrega resultados.

---

# Join `race`

La primera rama válida gana y las demás podrán cancelarse.

---

# Join Contract

```yaml
join_node:
  id: WF-NODE-JOIN-VALIDATIONS

  type: join

  sources:
    - WF-NODE-VALIDATE-GRAPH
    - WF-NODE-VALIDATE-INDEX
    - WF-NODE-VALIDATE-SECURITY

  policy:
    type: all_successful

  timeout:
    duration: PT10M

  on_timeout:
    action: fail

  aggregation:
    activity:
      id: ACT-AGGREGATE-VALIDATION-RESULTS
      version: 1.0.0
```

---

# Activated Branches Only

Un Join deberá distinguir entre:

- ramas definidas;
- ramas activadas;
- ramas omitidas.

Por defecto esperará únicamente las activadas.

---

# Join Timeout

Deberá existir cuando una rama pueda quedar bloqueada.

---

# Join Timeout Actions

```text
fail
continue_partial
cancel_remaining
escalate
wait_for_approval
```

---

# Join Cancellation

En `first_success` o `race`, las ramas restantes podrán:

- continuar;
- recibir cancel request;
- quedar detached;
- compensarse.

---

# Join Result

```yaml
join_result:
  join_node: WF-NODE-JOIN-VALIDATIONS

  activated_branches: 3
  completed_branches: 3
  successful_branches: 3
  failed_branches: 0

  policy_satisfied: true
  status: succeeded
```

---

# Conditional Paths

Una **Conditional Path** se activa según una Decision.

---

# Conditional Path Contract

```yaml
conditional_path:
  id: WF-PATH-PUBLISH

  decision_node:
    id: WF-NODE-DECIDE-PUBLICATION

  condition:
    id: EXEC-CONDITION-PUBLICATION-PASSED

  target:
    node: WF-NODE-PUBLISH

  priority: 100
```

---

# Exclusive Decision

Solo una salida.

---

# Inclusive Decision

Varias salidas.

---

# Decision Evaluation Order

Deberá ser:

- explícito;
- estable;
- registrado.

---

# Overlapping Conditions

En una rama exclusiva deberán detectarse o resolverse.

Diagnostic:

```text
WORKFLOW_EXCLUSIVE_BRANCH_MULTIPLE_MATCH
```

---

# No Matching Branch

```text
WORKFLOW_BRANCH_NO_MATCH
```

salvo default.

---

# Decision Result

Deberá persistir:

- condiciones evaluadas;
- valores usados;
- ramas candidatas;
- rama seleccionada;
- default usado.

---

# Conditional Skip

Las rutas no seleccionadas deberán marcarse.

---

# Fallback Path

Una **Fallback Path** proporciona una alternativa controlada.

---

# Fallback Triggers

```text
step_failure
timeout
capability_unavailable
quality_gate_failure
budget_pressure
policy_decision
```

---

# Fallback Contract

```yaml
fallback_path:
  id: WF-FALLBACK-VECTOR-TO-LEXICAL

  source:
    node: WF-NODE-VECTOR-RETRIEVAL

  trigger:
    states:
      - failed
      - timed_out

    error_codes:
      - VECTOR_CAPABILITY_UNAVAILABLE

  target:
    node: WF-NODE-LEXICAL-FALLBACK

  degradation:
    status: degraded
```

---

# Fallback Scope

Deberá declarar qué garantía cambia.

---

# No fallback de seguridad

No deberán relajarse:

- tenant;
- ACL;
- clasificación;
- required validation;
- critical Quality Gates.

---

# Fallback Chain

Deberá ser acíclica y limitada.

---

# Quality Gates dentro del DAG

Los Quality Gates podrán representarse como nodos.

---

# Quality Gate Node Contract

```yaml
quality_gate_node:
  id: WF-NODE-PUBLICATION-GATE

  gate:
    id: QG-KNOWLEDGE-PUBLICATION
    version: 1.0.0

  inputs:
    validation_result: ${steps.STEP-VALIDATE.outputs.result}
    index_result: ${steps.STEP-BUILD-INDEX.outputs.result}

  outcomes:
    passed:
      target: WF-NODE-PUBLISH

    failed:
      target: WF-NODE-REJECT-CANDIDATE

    review_required:
      target: WF-NODE-HUMAN-APPROVAL
```

---

# Gate Outcomes

```text
passed
passed_with_warnings
failed
blocked
review_required
waived
```

---

# Gate as Dependency

Un downstream Step podrá requerir:

```text
gate == passed
```

---

# Gate Waiver

Deberá:

- estar autorizado;
- tener ID;
- declarar scope;
- declarar expiración;
- registrar riesgo;
- no aplicarse a controles no eximibles.

---

# Stage

Un **Pipeline Stage** agrupa nodos relacionados.

Formato recomendado:

```text
PIPE-STAGE-XXXXXX
```

---

# Ejemplo

```text
Stage 1 — Validate
Stage 2 — Transform
Stage 3 — Build
Stage 4 — Evaluate
Stage 5 — Publish
```

---

# Stage Contract

```yaml
pipeline_stage:
  id: PIPE-STAGE-BUILD

  name: Build Artifacts

  nodes:
    - WF-NODE-BUILD-GRAPH
    - WF-NODE-BUILD-INDEX
    - WF-NODE-BUILD-CITATIONS

  entry_conditions:
    - validation_stage_passed

  completion:
    policy: all_successful

  stage_gate:
    id: QG-PIPELINE-BUILD
```

---

# Stage States

```text
not_started
running
waiting
passed
passed_with_warnings
failed
skipped
cancelled
```

---

# Stage Gate

Puede controlar el paso a la siguiente fase.

---

# Stage Isolation

Un Stage podrá:

- compartir artifacts internos;
- exponer outputs declarados;
- ocultar detalles al siguiente.

---

# Stage Output Contract

```yaml
stage_output:
  stage: PIPE-STAGE-BUILD

  values:
    graph_snapshot_id: KG-SNAP-000041
    index_snapshot_id: IDX-SNAP-000041
```

---

# Pipeline

Un **Pipeline** modelará una cadena de procesamiento de datos o artefactos.

Formato recomendado:

```text
PIPE-XXXXXX
```

---

# Pipeline Contract

```yaml
pipeline:
  id: PIPE-KNOWLEDGE-PUBLICATION

  version: 1.0.0

  stages:
    - PIPE-STAGE-VALIDATE
    - PIPE-STAGE-TRANSFORM
    - PIPE-STAGE-BUILD
    - PIPE-STAGE-EVALUATE
    - PIPE-STAGE-PUBLISH

  mode: batch

  artifact_flow:
    input: KNOWLEDGE-PACKAGE@1.0.0
    output: PUBLISHED-KNOWLEDGE@1.0.0
```

---

# Pipeline Modes

```text
batch
streaming
incremental
event_driven
scheduled
interactive
```

---

# Pipeline vs Workflow

Un Pipeline deberá enfocarse en:

- transformación;
- artefactos;
- etapas;
- calidad de datos.

Un Workflow podrá incluir:

- humanos;
- políticas;
- decisiones;
- compensaciones;
- procesos de negocio.

---

# Pipeline Node

Podrá ser una Activity o un Subpipeline.

---

# Pipeline Artifact Flow

Deberá declarar:

- input artifacts;
- output artifacts;
- intermediate artifacts;
- schemas;
- checksums;
- lineage.

---

# Pipeline Stage Boundary

Podrá crear checkpoint automático.

---

# Stage Retry

Podrá reejecutarse una etapa sin repetir las anteriores cuando:

- outputs previos siguen válidos;
- artifacts están disponibles;
- definition es compatible.

---

# Pipeline Promotion

Una etapa podrá producir un artefacto candidato que se promociona en una etapa posterior.

---

# Subworkflow Composition

Los workflows complejos deberán poder componerse.

---

# Composition Types

```text
embedded
child_execution
referenced
template_instantiation
pipeline_inclusion
```

---

# Embedded

La definición se expande dentro del mismo DAG.

---

# Child Execution

Se crea una ejecución hija durable.

---

# Referenced

El nodo conserva referencia a definición externa.

---

# Template Instantiation

Se parametriza una plantilla.

---

# Pipeline Inclusion

Se incluye un Pipeline como bloque.

---

# Embedded Composition

Ventajas:

- un único historial;
- menor overhead;
- planificación global.

Riesgos:

- DAG grande;
- acoplamiento;
- upgrades complejos.

---

# Child Execution Composition

Ventajas:

- aislamiento;
- reutilización;
- lifecycle independiente;
- retry separado.

Riesgos:

- mayor coordinación;
- latencia;
- múltiples historiales.

---

# Composition Policy

Deberá indicar cuándo usar cada una.

---

# Subworkflow Contract

```yaml
workflow_composition:
  parent:
    id: EXEC-DEF-KNOWLEDGE-PUBLICATION
    version: 1.0.0

  node:
    id: WF-NODE-BUILD-INDEX-SUBWORKFLOW

  child:
    id: EXEC-DEF-INDEX-BUILD
    version: 2.0.0

  mode: child_execution

  completion:
    wait_for: result

  cancellation:
    policy: request_cancel

  compensation:
    policy: propagate
```

---

# Input Mapping

Deberá ser explícito.

---

# Output Mapping

Deberá ser explícito.

---

# Child Result Status Mapping

El parent deberá saber cómo interpretar:

- succeeded;
- partial;
- failed;
- compensated;
- cancelled.

---

# Workflow Template

Un **Workflow Template** representa una estructura reutilizable parametrizable.

Formato recomendado:

```text
WF-TEMPLATE-XXXXXX
```

---

# Contrato

```yaml
workflow_template:
  id: WF-TEMPLATE-VALIDATE-BUILD-PUBLISH

  version: 1.0.0

  parameters:
    - name: validation_activity
      type: activity_reference
      required: true

    - name: build_activity
      type: activity_reference
      required: true

    - name: publication_activity
      type: activity_reference
      required: true

  structure:
    - validate
    - build
    - quality_gate
    - publish
```

---

# Template Parameters

Podrán incluir:

- Activity references;
- policies;
- timeouts;
- schemas;
- profiles;
- branch options;
- budgets.

---

# No parámetros de código arbitrario

---

# Template Instantiation

Deberá producir una definición concreta con:

- ID;
- versión;
- fingerprint;
- parámetros resueltos.

---

# Template Instance Record

```yaml
workflow_template_instance:
  template: WF-TEMPLATE-VALIDATE-BUILD-PUBLISH@1.0.0

  generated_definition:
    id: EXEC-DEF-KNOWLEDGE-PUBLICATION
    version: 1.0.0

  parameters:
    validation_activity: ACT-VALIDATE-KNOWLEDGE@1.0.0
    build_activity: ACT-BUILD-INDEX@2.0.0
    publication_activity: ACT-PUBLISH-INDEX@1.0.0
```

---

# Workflow Library

Una **Workflow Library** agrupa definiciones, plantillas y componentes reutilizables.

Formato recomendado:

```text
WF-LIB-XXXXXX
```

---

# Contenido

- workflows;
- pipelines;
- templates;
- common Activities;
- conditions;
- policies;
- compensation patterns.

---

# Library Contract

```yaml
workflow_library:
  id: WF-LIB-KNOWLEDGE-LIFECYCLE

  version: 1.0.0

  exports:
    workflows:
      - EXEC-DEF-KNOWLEDGE-INGESTION@1.0.0
      - EXEC-DEF-KNOWLEDGE-PUBLICATION@1.0.0

    templates:
      - WF-TEMPLATE-VALIDATE-BUILD-PUBLISH@1.0.0
```

---

# Library Dependency

Una definición deberá fijar versión de librería.

---

# No dependencia implícita a latest

---

# Workflow Imports

Deberán validar:

- compatibilidad;
- collisions;
- security;
- schemas;
- aliases.

---

# Namespace

Las librerías podrán utilizar namespaces.

Ejemplo:

```text
knowledge.publication
index.build
retrieval.rag
```

---

# Dynamic Steps

Un **Dynamic Step** se materializa durante la ejecución.

---

# Casos válidos

- Map sobre una colección;
- batch partitioning;
- graph traversal limitado;
- child workflows por elemento;
- ejecución adaptativa autorizada;
- agentic plan limitado.

---

# Dynamic Step Definition

```yaml
dynamic_step_policy:
  id: WF-DYNAMIC-POLICY-DOCUMENT-MAP

  generator:
    type: map
    source:
      step: STEP-DISCOVER-DOCUMENTS
      field: document_ids

  template:
    id: WF-STEP-TEMPLATE-VALIDATE-DOCUMENT

  limits:
    maximum_generated_steps: 500
    maximum_depth: 1
    maximum_parallelism: 10
```

---

# Runtime Expansion

La expansión deberá producir un registro formal.

Formato recomendado:

```text
WF-EXPANSION-XXXXXX
```

---

# Contrato

```yaml
workflow_runtime_expansion:
  id: WF-EXPANSION-000041

  execution:
    id: EXEC-000041

  source_node:
    id: WF-NODE-DISCOVER-DOCUMENTS

  policy:
    id: WF-DYNAMIC-POLICY-DOCUMENT-MAP

  generated_nodes:
    count: 125

  generated_edges:
    count: 250

  fingerprint: ...

  status: applied
```

---

# Expansion Determinism

La lista de elementos deberá persistirse.

El replay no deberá volver a consultar la fuente externa.

---

# Generated Node ID

Deberá derivarse de manera estable cuando sea posible.

Ejemplo:

```text
WF-NODE-VALIDATE-DOC-DOC-0051
```

---

# Expansion Limits

Obligatorios:

```text
maximum_nodes
maximum_edges
maximum_depth
maximum_fanout
maximum_parallelism
maximum_cost
maximum_duration
```

---

# Expansion Policy

Podrá:

- reject;
- truncate;
- paginate;
- batch;
- require approval.

---

# No truncamiento silencioso

---

# Dynamic Branching

Podrá permitir seleccionar rutas en runtime.

Deberá estar basado en:

- Decision;
- policy;
- Activity Result;
- human approval;
- Agent Plan validado.

---

# Agent-Generated Steps

Solo deberán permitirse cuando:

- las Activities estén en allowlist;
- los schemas sean válidos;
- exista límite de pasos;
- exista budget;
- no haya ciclos;
- se aplique policy;
- exista aprobación para side effects.

---

# Agentic Workflow Plan

```yaml
agentic_workflow_plan:
  id: WF-AGENT-PLAN-000041

  allowed_activities:
    - ACT-RUN-RETRIEVAL
    - ACT-RUN-REASONER
    - ACT-GENERATE-RAG-RESPONSE

  maximum_steps: 8
  maximum_depth: 2
  side_effects_allowed: false

  validation:
    status: passed
```

---

# No auto-modificación de ejecución activa sin registro

---

# DAG Materialization

La **DAG Materialization** convierte la definición en nodos ejecutables de una Execution.

---

# Materialization Phases

```text
Resolve Definition
↓
Resolve Imports
↓
Instantiate Templates
↓
Expand Embedded Subworkflows
↓
Normalize High-Level Constructs
↓
Resolve Static Conditions
↓
Build Nodes
↓
Build Edges
↓
Validate Graph
↓
Persist Materialized DAG
```

---

# Materialized DAG

Formato recomendado:

```text
WF-MATERIALIZED-DAG-XXXXXX
```

---

# Contrato

```yaml
materialized_workflow_dag:
  id: WF-MATERIALIZED-DAG-000041

  execution:
    id: EXEC-000041

  source:
    definition: EXEC-DEF-KNOWLEDGE-PUBLICATION@1.0.0
    graph: WF-GRAPH-KNOWLEDGE-PUBLICATION@1.0.0

  nodes:
    count: 9

  edges:
    count: 11

  entry_nodes:
    - WF-NODE-START-000041

  terminal_nodes:
    - WF-NODE-END-SUCCESS-000041
    - WF-NODE-END-REJECTED-000041

  fingerprint: ...

  status: ready
```

---

# Static Materialization

Se realiza al crear la Execution.

---

# Incremental Materialization

Añade nodos durante runtime bajo una política.

---

# Materialization Record

Deberá conservar:

- inputs relevantes;
- resolved versions;
- template parameters;
- static decisions;
- generated IDs;
- fingerprint.

---

# No materialización parcial no registrada

---

# Execution Planning

El **Execution Planner** analiza el DAG materializado y prepara su ejecución.

---

# Responsabilidades

- identificar entry nodes;
- calcular topología;
- calcular niveles;
- detectar paralelismo;
- estimar critical path;
- asignar prioridades;
- calcular budgets;
- determinar checkpoints;
- identificar capabilities;
- preparar scheduling hints.

---

# Execution Plan

Formato recomendado:

```text
EXEC-PLAN-XXXXXX
```

---

# Contrato

```yaml
execution_plan:
  id: EXEC-PLAN-000041

  execution:
    id: EXEC-000041

  dag:
    id: WF-MATERIALIZED-DAG-000041

  topology:
    levels: 6

  parallel_groups:
    - WF-PARALLEL-GROUP-000041

  critical_path:
    id: WF-CRITICAL-PATH-000041

  estimated:
    duration: PT12M
    cost: 2.40

  checkpoints:
    - after: WF-NODE-BUILD-GRAPH
    - after: WF-NODE-BUILD-INDEX

  status: ready
```

---

# Execution Plan vs Workflow Definition

La definición describe el proceso.

El Execution Plan describe cómo se prevé ejecutar una instancia concreta.

---

# Plan Inputs

- materialized DAG;
- capabilities;
- capacity;
- budgets;
- priorities;
- deadlines;
- historical metrics.

---

# Planning Hints

Podrán incluir:

- preferred worker pool;
- locality;
- expected duration;
- resource class;
- priority;
- queue.

---

# No garantía absoluta

El runtime podrá adaptarse, preservando semántica.

---

# Critical Path

El **Critical Path** representa la secuencia que determina la duración mínima estimada.

Formato recomendado:

```text
WF-CRITICAL-PATH-XXXXXX
```

---

# Ejemplo

```text
VALIDATE
↓
BUILD_GRAPH
↓
BUILD_INDEX
↓
RUN_GATES
↓
PUBLISH
```

---

# Critical Path Calculation

Podrá utilizar:

- duración estimada;
- dependencias;
- joins;
- branches probables;
- historical metrics.

---

# Conditional Critical Path

En workflows con ramas podrá existir:

- expected critical path;
- worst-case critical path;
- active critical path.

---

# Critical Path Contract

```yaml
workflow_critical_path:
  id: WF-CRITICAL-PATH-000041

  nodes:
    - WF-NODE-VALIDATE
    - WF-NODE-BUILD-GRAPH
    - WF-NODE-BUILD-INDEX
    - WF-NODE-RUN-GATES
    - WF-NODE-PUBLISH

  estimated_duration: PT11M30S

  confidence: 0.78
```

---

# Uso

- priorización;
- alertas;
- deadline risk;
- capacity planning;
- optimización.

---

# Critical Path Drift

Podrá compararse estimación y realidad.

---

# Workflow Deadline Feasibility

Antes de iniciar podrá estimarse si el deadline es viable.

---

# Deadline Risk

```yaml
deadline_feasibility:
  deadline_remaining: PT10M
  estimated_critical_path: PT12M
  status: at_risk
```

---

# Acciones

- rechazar;
- degradar;
- pedir extensión;
- aumentar prioridad;
- ajustar recursos;
- continuar con warning.

---

# Workflow Priority

Podrá definirse a nivel:

- Execution;
- Stage;
- Node;
- Branch.

---

# Priority Values

```text
critical
high
normal
low
background
```

---

# Priority Inheritance

Un Step heredará la prioridad de Execution salvo override autorizado.

---

# No prioridad para saltar seguridad

---

# Scheduling Priority Score

Podrá considerar:

```text
base priority
+
deadline urgency
+
critical path
+
age
+
tenant quota
-
resource pressure
```

---

# Workflow Graph Validation

Toda definición deberá validarse antes de activarse.

---

# Validation Categories

```text
structural
referential
topological
semantic
dataflow
termination
security
operational
version
```

---

# Structural Validation

Comprueba:

- nodos;
- edges;
- IDs;
- tipos;
- entry nodes;
- terminal nodes.

---

# Referential Validation

Comprueba:

- Step Definitions;
- Activities;
- conditions;
- policies;
- schemas;
- Subworkflows.

---

# Topological Validation

Comprueba:

- cycles;
- self-dependencies;
- unreachable nodes;
- dead ends.

---

# Semantic Validation

Comprueba:

- join policies;
- branch semantics;
- fallback;
- quality gates;
- cancellation.

---

# Dataflow Validation

Comprueba:

- bindings;
- producer-before-consumer;
- types;
- optional outputs;
- multiple writers.

---

# Termination Validation

Comprueba:

- rutas finales;
- loops limitados;
- waits con timeout;
- branches con default;
- joins alcanzables.

---

# Security Validation

Comprueba:

- Activities autorizadas;
- policy nodes;
- tenant propagation;
- secrets;
- side effects;
- human roles.

---

# Operational Validation

Comprueba:

- budgets;
- timeouts;
- retries;
- queues;
- worker pools;
- checkpoints;
- observability.

---

# Version Validation

Comprueba:

- versions pinned;
- imports;
- Subworkflows;
- adapters;
- schema compatibility.

---

# Workflow Diagnostics

Códigos iniciales:

```text
WORKFLOW_GRAPH_SCHEMA_INVALID
WORKFLOW_GRAPH_NO_ENTRY_NODE
WORKFLOW_GRAPH_NO_TERMINAL_NODE
WORKFLOW_NODE_DUPLICATE
WORKFLOW_EDGE_DUPLICATE
WORKFLOW_NODE_REFERENCE_MISSING
WORKFLOW_ACTIVITY_REFERENCE_MISSING
WORKFLOW_GRAPH_CYCLE_DETECTED
WORKFLOW_NODE_SELF_DEPENDENCY
WORKFLOW_NODE_UNREACHABLE
WORKFLOW_NODE_DEAD_END
WORKFLOW_PATH_NON_TERMINATING
WORKFLOW_DEPENDENCY_IMPOSSIBLE
WORKFLOW_REQUIRED_OUTPUT_MISSING
WORKFLOW_BINDING_TYPE_MISMATCH
WORKFLOW_MULTIPLE_WRITERS_CONFLICT
WORKFLOW_EXCLUSIVE_BRANCH_MULTIPLE_MATCH
WORKFLOW_BRANCH_NO_DEFAULT
WORKFLOW_JOIN_POLICY_INVALID
WORKFLOW_JOIN_UNREACHABLE
WORKFLOW_LOOP_UNBOUNDED
WORKFLOW_MAP_FANOUT_UNBOUNDED
WORKFLOW_DYNAMIC_EXPANSION_UNBOUNDED
WORKFLOW_SUBWORKFLOW_VERSION_UNRESOLVED
WORKFLOW_TEMPLATE_PARAMETER_INVALID
WORKFLOW_LIBRARY_VERSION_INCOMPATIBLE
WORKFLOW_QUALITY_GATE_MISSING
WORKFLOW_SECURITY_POLICY_MISSING
WORKFLOW_TERMINATION_UNPROVABLE
WORKFLOW_DEADLINE_INFEASIBLE
```

---

# Diagnostic Contract

```yaml
workflow_diagnostic:
  id: WF-DIAGNOSTIC-000041

  code: WORKFLOW_GRAPH_CYCLE_DETECTED
  severity: error

  graph:
    id: WF-GRAPH-KNOWLEDGE-PUBLICATION

  path:
    - WF-NODE-A
    - WF-NODE-B
    - WF-NODE-C
    - WF-NODE-A

  message: >
    El grafo contiene una dependencia cíclica.
```

---

# Graph Validation Result

```yaml
workflow_graph_validation:
  graph:
    id: WF-GRAPH-KNOWLEDGE-PUBLICATION

  status: valid

  checks:
    schema: passed
    references: passed
    topology: passed
    dataflow: passed
    termination: passed
    security: passed
    operation: passed

  diagnostics:
    errors: 0
    warnings: 2
```

---

# Workflow Quality Gate

```yaml
quality_gate:
  id: QG-WORKFLOW-GRAPH-0001

  criteria:
    all:
      - graph_schema_valid == true
      - entry_nodes_present == true
      - terminal_nodes_present == true
      - cycles_detected == 0
      - unreachable_required_nodes == 0
      - non_terminating_paths == 0
      - required_bindings_resolved == true
      - branch_defaults_defined == true
      - joins_valid == true
      - loops_bounded == true
      - dynamic_expansion_bounded == true
      - security_policies_defined == true
      - workflow_versions_pinned == true
```

---

# Pipeline Quality Gate

```yaml
quality_gate:
  id: QG-PIPELINE-DEFINITION-0001

  criteria:
    all:
      - stages_ordered == true
      - stage_inputs_valid == true
      - stage_outputs_valid == true
      - artifact_lineage_complete == true
      - stage_gates_defined == true
      - retry_boundaries_defined == true
      - checkpoint_boundaries_defined == true
```

---

# DAG Materialization Quality Gate

```yaml
quality_gate:
  id: QG-DAG-MATERIALIZATION-0001

  criteria:
    all:
      - definition_fingerprint_valid == true
      - all_versions_resolved == true
      - templates_instantiated == true
      - embedded_workflows_expanded == true
      - generated_node_ids_unique == true
      - materialized_graph_acyclic == true
      - graph_fingerprint_valid == true
```

---

# Execution Planning Quality Gate

```yaml
quality_gate:
  id: QG-EXECUTION-PLANNING-0001

  criteria:
    all:
      - materialized_dag_valid == true
      - critical_path_calculated == true
      - parallel_groups_valid == true
      - budgets_allocated == true
      - checkpoints_planned == true
      - deadline_feasibility_evaluated == true
      - required_capabilities_available == true
```

---

# Workflow Explainability

El Orquestador deberá poder explicar el grafo.

---

# Workflow Explanation

```yaml
workflow_explanation:
  workflow:
    id: EXEC-DEF-KNOWLEDGE-PUBLICATION
    version: 1.0.0

  summary: >
    El proceso valida el conocimiento, construye el grafo y los
    índices, evalúa Quality Gates y publica el snapshot aprobado.

  entry_nodes:
    - WF-NODE-VALIDATE

  parallelism:
    groups:
      - WF-PARALLEL-GROUP-BUILD

  decisions:
    - WF-NODE-PUBLICATION-DECISION

  quality_gates:
    - WF-NODE-PUBLICATION-GATE

  terminal_outcomes:
    - published
    - rejected
    - failed
```

---

# Node Explanation

Deberá indicar:

- por qué está bloqueado;
- qué dependencias faltan;
- qué condición se evaluó;
- por qué se omitió;
- qué rama lo activó.

---

# Ejemplo

```yaml
node_explanation:
  node: WF-NODE-PUBLISH

  status: blocked

  waiting_for:
    - dependency: WF-NODE-PUBLICATION-GATE
      expected_state: passed
      current_state: running
```

---

# Workflow Visualization

Podrá generarse una representación visual desde el contrato.

---

# Requisitos

La visualización no deberá ser la fuente canónica.

---

# Vistas

```text
definition
materialized
runtime
critical_path
failure
compensation
```

---

# Runtime View

Podrá mostrar:

```text
succeeded
running
ready
blocked
failed
skipped
```

---

# Workflow Diff

Deberá poder compararse entre versiones.

---

# Diff Types

```text
node_added
node_removed
edge_added
edge_removed
activity_changed
condition_changed
binding_changed
policy_changed
gate_changed
compensation_changed
```

---

# Workflow Compatibility Analysis

Un cambio podrá afectar:

- nuevas Executions;
- replay;
- migration;
- Subworkflow consumers;
- bindings;
- artifacts.

---

# Workflow Diff Record

```yaml
workflow_diff:
  source: EXEC-DEF-KNOWLEDGE-PUBLICATION@1.0.0
  target: EXEC-DEF-KNOWLEDGE-PUBLICATION@1.1.0

  changes:
    - type: node_added
      node: WF-NODE-SECURITY-VALIDATION

    - type: edge_added
      from: WF-NODE-BUILD-INDEX
      to: WF-NODE-SECURITY-VALIDATION

  compatibility:
    new_executions: compatible
    in_flight: migration_required
    replay: compatible
```

---

# Workflow Testing

Las definiciones deberán probarse antes de activarse.

---

# Test Types

```text
schema
graph
binding
condition
branch
join
loop
subworkflow
failure
fallback
compensation
replay
security
performance
```

---

# Graph Test

Comprueba topología.

---

# Branch Test

Ejecuta cada ruta posible.

---

# Join Test

Comprueba semántica con combinaciones de estados.

---

# Failure Test

Simula fallos.

---

# Fallback Test

Comprueba alternativa.

---

# Replay Test

Comprueba determinismo.

---

# Property-Based Testing

Podrá utilizarse para:

- combinaciones de estados;
- ramas;
- joins;
- loops;
- límites.

---

# Workflow Test Case

```yaml
workflow_test_case:
  id: WF-TEST-PUBLICATION-GATE-FAIL

  workflow:
    id: EXEC-DEF-KNOWLEDGE-PUBLICATION
    version: 1.0.0

  inputs:
    knowledge_snapshot_id: KG-SNAP-TEST-0001

  mocks:
    STEP-RUN-GATES:
      result:
        status: failed

  expected:
    activated_nodes:
      - WF-NODE-REJECT-CANDIDATE

    skipped_nodes:
      - WF-NODE-PUBLISH

    final_status: failed
```

---

# Workflow Simulation

Podrá estimar:

- rutas;
- costes;
- duración;
- fan-out;
- critical path;
- failures.

---

# Simulation Result

```yaml
workflow_simulation:
  workflow: EXEC-DEF-KNOWLEDGE-PUBLICATION@1.0.0

  scenarios: 1000

  estimated:
    success_rate: 0.96
    average_duration: PT9M
    p95_duration: PT14M
    average_cost: 2.10

  risks:
    - node: WF-NODE-BUILD-INDEX
      type: critical_path_bottleneck
```

---

# Observabilidad de Workflows y DAGs

---

# Métricas de definición

- workflows registrados;
- versiones activas;
- definitions deprecated;
- validation failures;
- template usage.

---

# Métricas de grafo

- nodes por workflow;
- edges;
- depth;
- width;
- parallel groups;
- branches;
- joins;
- Subworkflows.

---

# Métricas de runtime

- ready nodes;
- blocked nodes;
- active nodes;
- skipped nodes;
- branch frequency;
- join wait time;
- critical path duration.

---

# Métricas de expansión

- generated nodes;
- generated edges;
- fan-out;
- expansion failures;
- limit breaches.

---

# Métricas de Stage

- stage duration;
- stage success;
- gate failure;
- retries por Stage;
- checkpoint recovery.

---

# Métricas de planificación

- materialization latency;
- planning latency;
- critical path error;
- deadline risk;
- parallelism utilization.

---

# Branch Distribution

Permitirá detectar:

- ramas nunca usadas;
- condiciones incorrectas;
- fallbacks frecuentes.

---

# Join Wait Time

Puede identificar cuellos de botella.

---

# DAG Width

Número máximo de nodos paralelos potenciales.

---

# DAG Depth

Longitud máxima de dependencia.

---

# Runtime Critical Path

Podrá compararse con el estimado.

---

# Logs

```yaml
log:
  event: workflow_dag_materialized

  execution_id: EXEC-000041
  workflow: EXEC-DEF-KNOWLEDGE-PUBLICATION@1.0.0

  nodes: 9
  edges: 11
  parallel_groups: 1

  critical_path_estimated_ms: 690000
  duration_ms: 18
```

---

# Eventos

Catálogo inicial:

```text
workflow_definition_registered
workflow_definition_validated
workflow_definition_activated
workflow_definition_deprecated
workflow_graph_compiled
workflow_graph_validation_failed
workflow_dag_materialized
workflow_runtime_expanded
workflow_node_ready
workflow_node_activated
workflow_node_skipped
workflow_branch_selected
workflow_join_satisfied
workflow_join_timed_out
workflow_stage_started
workflow_stage_completed
workflow_quality_gate_passed
workflow_quality_gate_failed
workflow_execution_plan_created
```

---

# Evento de rama

```yaml
event:
  type: workflow_branch_selected

  subject:
    id: EXEC-000041
    type: execution

  data:
    decision_node: WF-NODE-PUBLICATION-DECISION
    selected_branch: publish
    decision_id: EXEC-DECISION-000041
```

---

# Evento de Join

```yaml
event:
  type: workflow_join_satisfied

  subject:
    id: WF-NODE-JOIN-VALIDATIONS
    type: workflow-node

  data:
    policy: all_successful
    activated_branches: 3
    successful_branches: 3
```

---

# Casos de uso

---

# Caso de uso 1 — Workflow lineal

```text
Validate
↓
Build
↓
Publish
```

Cada Step depende del éxito anterior.

---

# Caso de uso 2 — Construcción paralela

Tras validar se ejecutan en paralelo:

- Knowledge Graph;
- Metadata;
- Citation Index.

Un Join espera a todas.

---

# Caso de uso 3 — Rama por Quality Gate

```text
Gate passed
    → Publish

Gate failed
    → Reject

Review required
    → Human Task
```

---

# Caso de uso 4 — Fallback

Si Vector Index falla por indisponibilidad:

```text
Lexical-only build
```

La ejecución se marca como degradada.

---

# Caso de uso 5 — Map de documentos

Se descubren 125 documentos.

El DAG se expande de forma limitada y se procesan con concurrencia máxima de diez.

---

# Caso de uso 6 — Join porcentual

El flujo continúa si al menos el 95 % de documentos han sido validados.

---

# Caso de uso 7 — First Success

Se consultan dos proveedores equivalentes.

El primer resultado válido permite continuar y el segundo recibe cancelación cooperativa.

---

# Caso de uso 8 — Wait por evento

La publicación espera una aprobación externa.

El nodo queda `waiting` sin ocupar worker.

---

# Caso de uso 9 — Timer

Un rollout espera treinta minutos antes del siguiente porcentaje.

---

# Caso de uso 10 — Subworkflow

El workflow de publicación utiliza:

```text
WF-INDEX-BUILD@2.0.0
```

como Child Execution.

---

# Caso de uso 11 — Rama imposible

Una rama requiere el éxito de un Step que ya falló terminalmente.

La dependencia queda `impossible`.

---

# Caso de uso 12 — Nodo inaccesible

Un Step existe en la definición, pero ninguna rama puede alcanzarlo.

La validación bloquea la activación del workflow.

---

# Caso de uso 13 — Loop controlado

Un polling comprueba el estado de una indexación cada treinta segundos, con máximo de veinte iteraciones.

---

# Caso de uso 14 — Critical Path

La construcción del Vector Index determina la duración total.

El Scheduler prioriza su ejecución.

---

# Caso de uso 15 — Dynamic Agent Plan

Un agente propone:

```text
Retrieval
↓
Reasoning
↓
Additional Retrieval
↓
RAG
```

El plan se valida contra:

- allowlist;
- máximo de Steps;
- no side effects;
- budget;
- acyclicidad.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Dependencias basadas en orden del archivo

No constituyen un contrato fiable.

---

## DAG usado solo como dibujo

Debe representar semántica ejecutable.

---

## Edges sin tipo

No explican qué relación existe.

---

## Confundir control y datos

Un Step puede terminar sin producir el output requerido.

---

## Activar Steps antes de resolver bindings

Puede producir inputs incompletos.

---

## Marcar ready sin comprobar budget

El Step podría no ser ejecutable.

---

## Tratar optional como required

Genera bloqueos innecesarios.

---

## Tratar required como optional

Produce ejecuciones incoherentes.

---

## Ramas sin default

Pueden dejar el workflow bloqueado.

---

## Condiciones solapadas sin política

Generan selecciones ambiguas.

---

## Rama funcional modelada como error

Mezcla decisiones y fallos.

---

## Join esperando ramas no activadas

Produce deadlocks.

---

## Join sin timeout

Puede esperar indefinidamente.

---

## `all` cuando se necesita `all_successful`

Permite continuar con fallos no deseados.

---

## `first_completed` cuando se necesita `first_success`

Puede seleccionar un fallo.

---

## Cancelar ramas restantes sin política

Puede dejar side effects parciales.

---

## Variables compartidas entre ramas sin merge policy

Produce race conditions.

---

## Last-writer-wins implícito

Oculta conflictos.

---

## Loops como ciclos directos

Rompen acyclicidad y replay.

---

## Expansión dinámica ilimitada

Puede agotar recursos.

---

## Generar nodos con IDs no estables

Dificulta replay.

---

## Reconsultar elementos durante replay

Produce otro DAG.

---

## Subworkflow `latest`

Rompe reproducibilidad.

---

## Embedded Subworkflow gigantesco

Puede generar DAGs inmanejables.

---

## Child Executions para cada operación trivial

Aumenta overhead.

---

## Templates con código arbitrario

Comprometen seguridad.

---

## Workflow Libraries sin versión

Rompen dependencias.

---

## Quality Gate fuera del grafo

Oculta por qué avanzó una ejecución.

---

## Saltar Gate mediante fallback genérico

Puede comprometer calidad.

---

## Stage sin outputs declarados

Aumenta acoplamiento.

---

## Reejecutar Pipeline completo por un fallo tardío

Desperdicia trabajo cuando existen checkpoints válidos.

---

## No analizar alcanzabilidad

Deja nodos muertos.

---

## No verificar terminación

Puede crear workflows que nunca finalizan.

---

## Confundir Topological Order con ejecución secuencial

El DAG puede permitir paralelismo.

---

## No calcular Critical Path

Dificulta deadlines y optimización.

---

## Prioridad sin quotas

Puede provocar starvation.

---

## Workflow dinámico generado directamente por LLM

Debe pasar validación y límites.

---

## Visual editor como fuente canónica

La definición contractual debe ser la fuente.

---

## Cambiar el DAG materializado durante ejecución sin registro

Rompe auditoría.

---

# Reglas mínimas de conformidad

---

## Workflow Graph identificado

Toda definición compuesta deberá disponer de grafo.

---

## Nodes tipados

Todo nodo deberá declarar tipo.

---

## Edges tipados

Toda arista deberá declarar semántica.

---

## Entry Nodes

Deberá existir al menos uno.

---

## Terminal Nodes

Deberá existir al menos uno.

---

## Dependencias explícitas

Todo orden deberá declararse.

---

## Acyclicidad

El DAG materializado no deberá contener ciclos.

---

## Reachability

Todo nodo requerido deberá ser alcanzable.

---

## Terminación

Toda ruta activable deberá poder finalizar.

---

## Activation Rules

Todo nodo deberá declarar cuándo puede activarse.

---

## Completion Rules

Todo nodo deberá declarar qué estados acepta.

---

## Branches completas

Toda Decision deberá tener condiciones y default o error explícito.

---

## Join gobernado

Toda convergencia deberá declarar política.

---

## Parallelism limitado

Toda rama paralela deberá respetar concurrencia.

---

## Shared State protegido

Toda escritura concurrente deberá tener merge policy.

---

## Loops controlados

Toda repetición deberá usar primitivas limitadas.

---

## Runtime Expansion limitada

Todo nodo dinámico deberá proceder de una policy.

---

## Quality Gates explícitos

Los controles críticos deberán formar parte del grafo.

---

## Stages definidos

Los Pipelines deberán agrupar operaciones coherentes.

---

## Subworkflows versionados

Toda composición deberá fijar versión.

---

## Templates versionadas

Toda instanciación deberá ser reproducible.

---

## Libraries versionadas

Toda importación deberá fijarse.

---

## DAG materializado persistido

Cada Execution deberá conservar su estructura ejecutable.

---

## Topología validada

El grafo deberá superar Cycle Detection y Reachability.

---

## Critical Path calculado

Las ejecuciones relevantes deberán conocer su ruta crítica estimada.

---

## Execution Plan

Toda Execution no trivial deberá disponer de plan.

---

## Quality Gate

Ningún grafo inválido deberá activarse.

---

# Conformidad de Workflow Graph

Será conforme cuando:

- tenga ID;
- tenga versión;
- identifique definición;
- declare nodes;
- declare edges;
- declare entry nodes;
- declare terminal nodes;
- tenga fingerprint;
- supere validación.

---

# Conformidad de Workflow Node

Será conforme cuando:

- tenga ID;
- declare tipo;
- referencie definición;
- declare activation rule;
- declare completion rule;
- declare obligatoriedad;
- preserve políticas;
- preserve budget.

---

# Conformidad de Workflow Edge

Será conforme cuando:

- tenga ID;
- declare source;
- declare target;
- declare tipo;
- declare obligatoriedad;
- declare guard cuando proceda;
- declare data mapping cuando proceda.

---

# Conformidad de Dependency

Será conforme cuando:

- identifique source;
- identifique target;
- declare tipo;
- declare condición de satisfacción;
- declare obligatoriedad;
- pueda alcanzar un estado terminal.

---

# Conformidad de Decision Branch

Será conforme cuando:

- identifique Decision;
- declare condición;
- declare target;
- declare prioridad;
- preserve default;
- sea determinista o registre ambigüedad.

---

# Conformidad de Join

Será conforme cuando:

- identifique ramas;
- declare policy;
- considere solo ramas activadas;
- declare timeout;
- declare comportamiento ante timeout;
- declare agregación;
- preserve resultados.

---

# Conformidad de Pipeline Stage

Será conforme cuando:

- tenga ID;
- agrupe nodes;
- declare entry criteria;
- declare completion policy;
- declare outputs;
- declare Stage Gate;
- declare checkpoint cuando proceda.

---

# Conformidad de Workflow Template

Será conforme cuando:

- tenga ID;
- tenga versión;
- declare parámetros;
- declare tipos;
- declare estructura;
- limite extensiones;
- produzca definición validable.

---

# Conformidad de Runtime Expansion

Será conforme cuando:

- tenga ID;
- identifique Execution;
- identifique source node;
- declare policy;
- preserve elementos;
- limite nodes y edges;
- genere fingerprint;
- sea reproducible.

---

# Conformidad del DAG Materializado

Será conforme cuando:

- tenga ID;
- identifique Execution;
- identifique Definition;
- preserve versiones;
- declare nodes;
- declare edges;
- declare entry nodes;
- declare terminal nodes;
- sea acíclico;
- sea alcanzable;
- tenga fingerprint.

---

# Conformidad del Execution Plan

Será conforme cuando:

- tenga ID;
- identifique Execution;
- identifique DAG;
- declare topología;
- declare parallel groups;
- declare Critical Path;
- declare estimaciones;
- declare checkpoints;
- declare budgets;
- supere Gate.

---

# Lista de comprobación

Antes de activar un Workflow deberá comprobarse:

```text
[ ] El Workflow Graph tiene ID.
[ ] El Workflow Graph está versionado.
[ ] La definición posee fingerprint.
[ ] Los Node IDs son únicos.
[ ] Los Edge IDs son únicos.
[ ] Todos los Nodes tienen tipo.
[ ] Todos los Edges tienen tipo.
[ ] Existen Entry Nodes.
[ ] Existen Terminal Nodes.
[ ] Todos los Nodes requeridos son alcanzables.
[ ] No existen Self Dependencies.
[ ] No existen ciclos directos.
[ ] Los Loops utilizan primitivas controladas.
[ ] Toda ruta activable puede terminar.
[ ] No existen Dead-End Nodes no terminales.
[ ] Las dependencias obligatorias están definidas.
[ ] Las dependencias de datos tienen bindings.
[ ] Los bindings son compatibles.
[ ] Las Activation Rules están definidas.
[ ] Las Completion Rules están definidas.
[ ] Las Branches exclusivas no son ambiguas.
[ ] Toda Decision tiene default o fallo explícito.
[ ] Las rutas no seleccionadas se marcan como skipped.
[ ] Los Parallel Splits están definidos.
[ ] Las ramas paralelas tienen identidad.
[ ] La concurrencia está limitada.
[ ] Las escrituras compartidas tienen merge policy.
[ ] Los Join Nodes declaran policy.
[ ] Los Join Nodes consideran ramas activadas.
[ ] Los Join Nodes tienen timeout cuando procede.
[ ] Los fallbacks están limitados.
[ ] Los fallbacks no relajan seguridad.
[ ] Los Quality Gates forman parte del DAG.
[ ] Los waivers están gobernados.
[ ] Los Pipeline Stages tienen límites claros.
[ ] Los Stage Outputs están declarados.
[ ] Los Stage Gates están definidos.
[ ] Los Subworkflows fijan versión.
[ ] Los mappings de Subworkflows son válidos.
[ ] Las Workflow Templates están versionadas.
[ ] Las Template Instances son reproducibles.
[ ] Las Workflow Libraries están versionadas.
[ ] Las importaciones son compatibles.
[ ] Los Dynamic Steps proceden de policy.
[ ] La Runtime Expansion tiene límites.
[ ] Los IDs dinámicos son estables.
[ ] Los elementos dinámicos quedan persistidos.
[ ] El DAG materializado se persiste.
[ ] El DAG materializado tiene fingerprint.
[ ] El orden topológico es válido.
[ ] Los Parallel Groups están identificados.
[ ] El Critical Path está calculado.
[ ] El deadline ha sido evaluado.
[ ] Los checkpoints están planificados.
[ ] El Execution Plan está identificado.
[ ] La seguridad está propagada.
[ ] La observabilidad está configurada.
[ ] El Workflow Graph Quality Gate ha pasado.
[ ] El DAG Materialization Quality Gate ha pasado.
[ ] El Execution Planning Quality Gate ha pasado.
```

---

# Arquitectura final de la Parte III

```text
Workflow Definition
        ↓
Resolve Imports and Templates
        ↓
Build Workflow Graph
        ↓
Validate Nodes and Edges
        ↓
Resolve Dependencies
        ↓
Detect Cycles
        ↓
Analyze Reachability
        ↓
Validate Termination
        ↓
Normalize Branches and Joins
        ↓
Expand Embedded Subworkflows
        ↓
Materialize DAG
        ↓
Calculate Topology
        ↓
Identify Parallel Groups
        ↓
Calculate Critical Path
        ↓
Allocate Budgets and Checkpoints
        ↓
Create Execution Plan
        ↓
Persist Materialized Graph
        ↓
Activate Entry Nodes
```

---

# Transición hacia la Parte IV

Esta tercera parte ha definido:

- Workflow Graphs;
- Workflow Nodes;
- Workflow Edges;
- Edge Types;
- Dependency Types;
- Dependency Expressions;
- Dependency Resolution;
- Step Readiness;
- Activation Rules;
- Completion Rules;
- Workflow Completion;
- Directed Acyclic Graphs;
- DAG Normalization;
- Cycle Detection;
- Reachability;
- Dead Ends;
- Topological Ordering;
- Execution Levels;
- Parallel Groups;
- Parallel Splits;
- Branch Isolation;
- Variable Merge Policies;
- Join Semantics;
- Conditional Paths;
- Fallback Paths;
- Quality Gates dentro del DAG;
- Pipeline Stages;
- Pipelines;
- Artifact Flow;
- Subworkflow Composition;
- Workflow Templates;
- Workflow Libraries;
- Dynamic Steps;
- Runtime Expansion;
- Agent-Generated Steps;
- DAG Materialization;
- Execution Planning;
- Critical Path;
- Deadline Feasibility;
- Workflow Priority;
- Graph Validation;
- Workflow Diagnostics;
- Quality Gates;
- Workflow Explainability;
- Workflow Visualization;
- Workflow Diff;
- Workflow Testing;
- Workflow Simulation;
- observabilidad;
- casos de uso;
- antipatrones;
- reglas de conformidad.

La Parte IV desarrollará:

- Scheduler Architecture;
- Job Model;
- Job Definitions;
- Job Instances;
- Trigger Engine;
- Schedule Definitions;
- cron schedules;
- interval schedules;
- calendar schedules;
- event triggers;
- dependency triggers;
- manual triggers;
- delayed execution;
- timers;
- waiting;
- signals;
- queues;
- worker pools;
- routing;
- priority queues;
- quotas;
- rate limits;
- fairness;
- backpressure;
- admission control;
- dispatching;
- leases;
- heartbeats;
- worker availability;
- job claiming;
- orphan recovery;
- scheduling policies;
- capacity-aware scheduling;
- deadline-aware scheduling;
- Quality Gates del Scheduler.

---

# Conclusión

Los Workflows, Pipelines y DAGs constituyen la estructura mediante la que el Orquestador convierte Activities independientes en procesos completos.

El ciclo puede resumirse así:

```text
Definir Nodes
        ↓
Definir Edges
        ↓
Resolver dependencias
        ↓
Validar ramas
        ↓
Validar joins
        ↓
Controlar loops
        ↓
Componer Subworkflows
        ↓
Materializar DAG
        ↓
Calcular topología
        ↓
Identificar paralelismo
        ↓
Calcular Critical Path
        ↓
Crear Execution Plan
        ↓
Activar Steps
```

Los Nodes representan operaciones o controles.

Los Edges representan dependencias y transiciones.

Las Activation Rules determinan cuándo un Step puede comenzar.

Las Completion Rules determinan qué resultado acepta el flujo.

Las Branches permiten decisiones.

Los Parallel Splits permiten concurrencia.

Los Joins coordinan la convergencia.

Los Quality Gates gobiernan el avance.

Los Stages organizan Pipelines.

Los Subworkflows permiten composición.

Las Templates reducen duplicación.

Las Libraries permiten reutilización versionada.

La Runtime Expansion permite fan-out controlado.

La DAG Materialization convierte la definición en una estructura concreta.

El Topological Ordering valida el orden.

El Critical Path identifica la duración dominante.

El Execution Plan prepara la ejecución real.

Un Workflow correctamente definido deberá poder responder:

```text
¿Qué nodos contiene?

¿Qué tipo posee cada nodo?

¿Qué dependencias existen?

¿Qué datos fluyen entre Steps?

¿Qué nodos pueden ejecutarse en paralelo?

¿Qué condiciones activan cada rama?

¿Qué ocurre si ninguna condición coincide?

¿Qué ramas debe esperar cada Join?

¿Qué Quality Gates controlan el avance?

¿Qué Subworkflows intervienen?

¿Qué nodos pueden crearse dinámicamente?

¿Qué límites existen?

¿Existe algún ciclo?

¿Todos los nodos requeridos son alcanzables?

¿Toda ruta puede terminar?

¿Cuál es el Critical Path?

¿Qué DAG concreto se materializó para la Execution?
```

Con esta tercera parte queda formalizado el mecanismo mediante el que NovaCoquinaria representará, validará, compondrá, materializará y planificará Workflows, Pipelines y DAGs ejecutables.

La siguiente parte definirá cómo el **Scheduler, el Trigger Engine, las colas y los workers** convierten ese Execution Plan en trabajo programado, distribuido, priorizado y controlado.

---

# Parte IV — Scheduler Runtime: Worker Pools, Colas, Dispatching, Leases, Heartbeats, Backpressure y Control de Capacidad

---

# Introducción

Una vez que el **Workflow Compiler** ha generado un **Materialized DAG** y el **Execution Planner** ha calculado:

- topología,
- dependencias,
- grupos paralelos,
- Critical Path,
- checkpoints,
- prioridades,
- budgets,

el siguiente problema consiste en ejecutar realmente dicho plan.

El Scheduler constituye el componente responsable de transformar un conjunto de nodos "ready" en trabajo distribuido ejecutado por múltiples workers.

No es simplemente un planificador temporal.

Es un sistema distribuido responsable de:

- decidir qué ejecutar;
- cuándo ejecutarlo;
- dónde ejecutarlo;
- bajo qué restricciones;
- con qué prioridad;
- respetando límites de capacidad;
- preservando la semántica del Workflow.

Conceptualmente:

```text
Workflow DAG
        ↓
Dependency Resolver
        ↓
Ready Queue
        ↓
Scheduler
        ↓
Dispatch
        ↓
Worker Pool
        ↓
Execution
        ↓
Heartbeat
        ↓
Completion
        ↓
Next Ready Steps
```

Esta parte formaliza el Scheduler distribuido.

---

# Objetivos

Esta parte persigue:

- definir Scheduler Runtime;
- formalizar Worker Pools;
- definir Worker Capabilities;
- establecer Worker Lifecycle;
- definir Queue Architecture;
- formalizar Queue Types;
- definir Priority Queues;
- establecer Multi-tenant Scheduling;
- definir Dispatch Policies;
- formalizar Worker Selection;
- definir Capacity-aware Scheduling;
- establecer Deadline-aware Scheduling;
- definir Fair Scheduling;
- formalizar Admission Control;
- establecer Rate Limiting;
- definir Resource Reservations;
- formalizar Job Leasing;
- definir Lease Renewal;
- establecer Lease Expiration;
- formalizar Heartbeats;
- definir Failure Detection;
- establecer Worker Recovery;
- formalizar Job Reassignment;
- definir Graceful Shutdown;
- establecer Scheduler Metrics;
- formalizar Scheduler Diagnostics;
- definir Scheduler Quality Gates;
- garantizar ejecución reproducible.

---

# Principios del Scheduler

Todo Scheduler deberá cumplir los siguientes principios.

---

## Stateless en memoria

Las decisiones no deberán depender únicamente de memoria RAM.

---

## Estado durable

La información crítica deberá persistirse.

---

## Idempotencia

La reasignación de un Job no deberá producir efectos duplicados.

---

## Determinismo

La política de scheduling deberá ser reproducible.

---

## Fairness

Un tenant no deberá monopolizar el sistema.

---

## Prioridad gobernada

La prioridad no deberá romper aislamiento.

---

## Capacidad conocida

Todo Worker deberá anunciar capacidades.

---

## Heartbeats obligatorios

Todo trabajo largo deberá emitir heartbeats.

---

## Recuperación automática

Los trabajos huérfanos deberán recuperarse.

---

## Escalabilidad horizontal

El Scheduler deberá admitir múltiples instancias.

---

## Backpressure

El sistema deberá protegerse frente a sobrecarga.

---

## Observabilidad

Toda decisión relevante deberá quedar registrada.

---

# Arquitectura conceptual

```text
                  Materialized DAG
                         │
                         ▼
              Dependency Resolver
                         │
                         ▼
                  Ready Job Queue
                         │
                         ▼
                  Scheduler Core
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
 Priority Engine   Capacity Engine   Policy Engine
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                Dispatch Decision
                         │
                         ▼
                 Worker Registry
                         │
                         ▼
                  Worker Pools
                         │
                         ▼
                    Job Lease
                         │
                         ▼
                    Worker Runtime
                         │
                         ▼
 Heartbeats ──► Completion ──► Next Ready Jobs
```

---

# Scheduler Runtime

El **Scheduler Runtime** coordina toda la ejecución distribuida.

Formato recomendado:

```text
SCHEDULER-RUNTIME-XXXXXX
```

---

# Responsabilidades

- monitorizar Ready Queue;
- seleccionar Jobs;
- elegir Workers;
- emitir leases;
- controlar prioridades;
- controlar cuotas;
- aplicar políticas;
- gestionar heartbeats;
- detectar fallos;
- reasignar trabajos;
- producir métricas.

---

# Scheduler Contract

```yaml
scheduler_runtime:
  id: SCHEDULER-RUNTIME-PRIMARY

  version: 1.0.0

  mode: distributed

  scheduling_policy:
    id: POLICY-DEFAULT

  worker_registry:
    id: WR-PRIMARY

  queues:
    - READY
    - DELAYED
    - WAITING
    - RETRY

  status: running
```

---

# Scheduler Modes

```text
single_node
active_passive
distributed
geo_distributed
```

---

# Distributed Scheduler

El modelo recomendado para NovaCoquinaria.

Varios Scheduler Nodes colaboran utilizando almacenamiento durable.

---

# Scheduler Tick

El Scheduler podrá reevaluar periódicamente:

- nuevos Jobs;
- expiración de leases;
- heartbeats;
- timers;
- señales;
- prioridades.

---

# Tick Interval

Configuración típica:

```yaml
tick:
  every: PT1S
```

Aunque podrá emplearse arquitectura dirigida por eventos.

---

# Scheduler Event Loop

```text
Receive Events
        ↓
Update State
        ↓
Find Ready Jobs
        ↓
Evaluate Policies
        ↓
Dispatch
        ↓
Issue Leases
        ↓
Wait
```

---

# Ready Queue

La Ready Queue contiene Jobs preparados para ejecutarse.

---

# Requisitos

- orden estable;
- persistencia;
- prioridad;
- soporte multi-tenant;
- deduplicación.

---

# Ready Queue Contract

```yaml
ready_queue:
  id: READY

  ordering:
    - priority
    - deadline
    - enqueue_time

  durable: true
```

---

# Queue Types

```text
ready
delayed
retry
waiting_signal
waiting_timer
waiting_human
dead_letter
maintenance
```

---

# Delayed Queue

Jobs pendientes de una fecha futura.

---

# Retry Queue

Jobs esperando próximo retry.

---

# Waiting Signal Queue

Jobs bloqueados por señal.

---

# Waiting Human Queue

Esperando intervención humana.

---

# Dead Letter Queue

Jobs que ya no pueden reintentarse.

---

# Queue Metadata

Toda cola podrá definir:

- prioridad;
- TTL;
- retention;
- tenant;
- quotas.

---

# Queue Item

```yaml
queue_item:
  job: JOB-000041

  execution: EXEC-000041

  priority: high

  deadline: 2026-08-05T09:30:00Z

  tenant: knowledge

  enqueue_time: ...
```

---

# Queue Ordering

Por defecto:

```text
priority
↓
deadline
↓
critical path
↓
enqueue time
```

---

# Stable Ordering

Empates deberán resolverse de forma estable.

---

# Queue Sharding

Las colas podrán particionarse.

Ejemplo:

```text
tenant
workflow
priority
region
```

---

# Worker Registry

El Scheduler deberá conocer los Workers disponibles.

Formato recomendado:

```text
WORKER-REGISTRY-XXXXXX
```

---

# Responsabilidades

- registrar Workers;
- capacidades;
- estado;
- heartbeats;
- versiones;
- cargas.

---

# Worker Registry Contract

```yaml
worker_registry:
  id: WR-PRIMARY

  workers:
    - WORKER-001
    - WORKER-002

  status: active
```

---

# Worker

Un Worker ejecuta Jobs.

Formato recomendado:

```text
WORKER-XXXXXX
```

---

# Worker Contract

```yaml
worker:
  id: WORKER-KNOWLEDGE-001

  pool:
    id: POOL-KNOWLEDGE

  capabilities:
    - retrieval
    - indexing
    - embeddings

  status: idle

  max_concurrency: 8
```

---

# Worker States

```text
starting
idle
busy
draining
maintenance
offline
failed
```

---

# Idle

Disponible.

---

# Busy

Ejecutando Jobs.

---

# Draining

No acepta nuevos Jobs.

---

# Maintenance

Temporalmente excluido.

---

# Failed

No responde.

---

# Worker Pool

Agrupa Workers equivalentes.

Formato recomendado:

```text
WORKER-POOL-XXXXXX
```

---

# Pool Contract

```yaml
worker_pool:
  id: POOL-RAG

  workers:
    - WORKER-001
    - WORKER-002

  capabilities:
    - rag_generation

  scheduling_policy:
    least_loaded
```

---

# Pool Types

```text
general
cpu
gpu
rag
retrieval
indexing
validation
human
external
```

---

# Capability

Una capacidad representa una función ejecutable.

Formato recomendado:

```text
CAPABILITY-XXXXXX
```

---

# Ejemplos

```text
retrieval
reranking
embedding_generation
knowledge_validation
citation_generation
knowledge_publication
```

---

# Capability Contract

```yaml
capability:
  id: retrieval

  versions:
    - 1.x
    - 2.x

  resource_class:
    cpu
```

---

# Capability Matching

El Scheduler solo asignará Jobs a Workers compatibles.

---

# Worker Registration

Proceso:

```text
Worker Boot
        ↓
Authenticate
        ↓
Register
        ↓
Advertise Capabilities
        ↓
Heartbeat
        ↓
Accept Jobs
```

---

# Registration Contract

```yaml
worker_registration:
  worker: WORKER-001

  version: 1.2.0

  capabilities:
    - retrieval
    - reranking

  max_concurrency: 12
```

---

# Dynamic Registration

Los Workers podrán añadirse en caliente.

---

# Worker Lifecycle

```text
Created
↓
Registered
↓
Healthy
↓
Busy
↓
Idle
↓
Draining
↓
Offline
```

---

# Worker Health

El Scheduler deberá conocer:

- heartbeat;
- carga;
- errores;
- memoria;
- CPU;
- capacidad disponible.

---

# Health States

```text
healthy
degraded
unhealthy
unknown
```

---

# Worker Capacity

Representa la carga admisible.

---

# Contract

```yaml
capacity:
  maximum_slots: 16
  occupied_slots: 9
  available_slots: 7
```

---

# Slot

Unidad lógica de concurrencia.

No equivale necesariamente a un hilo.

---

# Weighted Slots

Algunos Jobs podrán consumir más de un slot.

```yaml
required_slots: 4
```

---

# Resource Classes

```text
small
medium
large
gpu
high_memory
```

---

# Worker Selection

El Scheduler elegirá Worker considerando:

- capacidades;
- slots;
- prioridad;
- locality;
- tenant;
- afinidad;
- historial.

---

# Selection Policies

```text
first_available
least_loaded
round_robin
weighted
random
sticky
locality
capability_score
```

---

# Least Loaded

Recomendado por defecto.

---

# Sticky Scheduling

Favorece reutilizar el mismo Worker.

Útil para cachés locales.

---

# Locality Scheduling

Prioriza Workers cercanos al dato.

---

# Capability Score

Cada Worker podrá recibir una puntuación.

```yaml
worker_score:
  worker: WORKER-001

  score: 0.94
```

---

# Dispatch

El Dispatch asigna un Job a un Worker.

Formato recomendado:

```text
DISPATCH-XXXXXX
```

---

# Dispatch Contract

```yaml
dispatch:
  id: DISPATCH-000041

  job: JOB-000041

  worker: WORKER-001

  lease: LEASE-000041

  status: assigned
```

---

# Dispatch Steps

```text
Job Ready
↓
Worker Selected
↓
Lease Created
↓
Dispatch
↓
Worker ACK
↓
Execution Starts
```

---

# Dispatch ACK

El Worker deberá confirmar recepción.

---

# No ACK

El Job volverá a Ready Queue.

---

# Dispatch Timeout

Configuración:

```yaml
dispatch_timeout:
  PT10S
```

---

# Scheduler Decisions

Toda asignación deberá quedar registrada.

```yaml
scheduler_decision:
  decision: dispatch

  reason:
    least_loaded_worker
```

---

# Scheduling Policies

Formato recomendado:

```text
SCHED-POLICY-XXXXXX
```

---

# Policies

```text
FIFO
Priority
Weighted
Fair
Deadline
CriticalPath
TenantAware
Hybrid
```

---

# FIFO

Simple.

---

# Priority

Respeta prioridad.

---

# Deadline

Prioriza deadlines próximos.

---

# Critical Path

Favorece Jobs pertenecientes al Critical Path.

---

# Tenant Aware

Evita monopolios.

---

# Hybrid

Combina múltiples criterios.

---

# Policy Contract

```yaml
scheduler_policy:
  id: POLICY-HYBRID

  weights:
    priority: 0.40
    deadline: 0.25
    critical_path: 0.20
    fairness: 0.15
```

---

# Capacity-aware Scheduling

El Scheduler deberá evitar sobrecargar Workers.

---

# Inputs

- slots;
- memoria;
- CPU;
- GPU;
- IO;
- carga histórica.

---

# Decision

Solo asignar si existe capacidad.

---

# Deadline-aware Scheduling

Trabajos con deadline cercano aumentan prioridad efectiva.

---

# Deadline Risk

```yaml
deadline_score: 0.91
```

---

# Fair Scheduling

Garantiza reparto entre tenants.

---

# Fairness Window

Ejemplo:

```text
últimos 10 minutos
```

---

# Tenant Share

```yaml
tenant_share:
  knowledge: 35%
  ingestion: 20%
  retrieval: 45%
```

---

# Starvation Prevention

Todo Job deberá terminar siendo atendido.

---

# Aging

La prioridad podrá incrementarse con el tiempo.

```yaml
aging:
  increase_every: PT5M
```

---

# Parte V — Gestión de estados, eventos, señales, timers y ciclo de vida de ejecuciones, Jobs y Steps

---

# Introducción

La Parte IV ha definido cómo el Scheduler transforma nodos preparados del DAG en trabajo distribuido mediante:

- Ready Queues;
- Worker Pools;
- Worker Capabilities;
- Dispatching;
- prioridades;
- fairness;
- Capacity-aware Scheduling;
- Deadline-aware Scheduling;
- leases;
- heartbeats;
- control de carga;
- recuperación de Jobs huérfanos.

Para que esta ejecución distribuida sea durable y coherente, NovaCoquinaria deberá formalizar con precisión:

- qué estados puede tener una Execution;
- qué estados puede tener un Step;
- qué estados puede tener un Job;
- qué transiciones son válidas;
- qué eventos provocan cada transición;
- cómo se persiste el progreso;
- cómo se manejan señales externas;
- cómo se representan esperas;
- cómo se crean y disparan timers;
- cómo se pausa o reanuda un proceso;
- cómo se cancela;
- cómo se detecta una ejecución bloqueada;
- cómo se construye su resultado final.

La gestión de estados no deberá reducirse a un único campo textual como:

```text
status = running
```

Cada estado deberá formar parte de una máquina de estados explícita, versionada y gobernada.

Conceptualmente:

```text
Command
   │
   ▼
State Validation
   │
   ▼
Transition Decision
   │
   ▼
Persist Transition
   │
   ▼
Publish Event
   │
   ▼
Schedule Consequences
   │
   ▼
New Durable State
```

Esta parte desarrolla el modelo formal de ciclo de vida del Orquestador de Ejecución.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- formalizar Execution State Machines;
- definir Step State Machines;
- definir Job State Machines;
- establecer estados terminales y no terminales;
- definir transiciones válidas;
- establecer Transition Guards;
- formalizar State Transition Records;
- definir Commands y Events;
- diferenciar comandos, eventos y señales;
- formalizar Event Envelopes;
- establecer Event Ordering;
- definir Event Deduplication;
- establecer Event Delivery Semantics;
- definir Correlation y Causation;
- formalizar Signals;
- definir Signal Routing;
- establecer Signal Buffering;
- definir Timers;
- formalizar Delayed Actions;
- definir Wait States;
- establecer Pause y Resume;
- formalizar Cancellation;
- definir Cooperative Cancellation;
- establecer Forced Termination;
- formalizar Suspension;
- definir Execution Blocking;
- detectar Stalled Executions;
- establecer State Reconciliation;
- formalizar terminalización;
- construir Execution Results;
- definir eventos de lifecycle;
- establecer observabilidad;
- definir diagnósticos;
- establecer Quality Gates;
- formalizar reglas de conformidad.

---

# Principios de gestión de estado

Toda implementación deberá respetar los siguientes principios.

---

## Estado durable

Toda transición significativa deberá persistirse antes de considerarse efectiva.

---

## Máquina de estados explícita

Las transiciones permitidas deberán estar definidas.

No deberán depender de condiciones dispersas por el código.

---

## Transiciones atómicas

El cambio de estado y el registro de la transición deberán confirmarse de forma indivisible.

---

## Eventos derivados del estado

Un evento no deberá publicarse como completado antes de persistir el estado correspondiente.

---

## No transición silenciosa

Toda modificación del estado deberá dejar evidencia.

---

## Versionado optimista

Las actualizaciones concurrentes deberán utilizar revisión esperada.

---

## Estados terminales inmutables

Una Execution finalizada no deberá volver directamente a `running`.

Deberá crearse:

- una Recovery Execution;
- una Retry Execution;
- una nueva Execution relacionada.

---

## Diferenciación de niveles

Execution, Step Instance, Step Run y Job deberán poseer ciclos de vida distintos.

---

## Comando no equivale a resultado

Solicitar una cancelación no significa que la ejecución ya esté cancelada.

---

## Espera sin consumo activo

Los estados de espera no deberán mantener Workers ocupados.

---

## Timers durables

Los timers deberán sobrevivir a reinicios.

---

## Señales idempotentes

La recepción repetida de una misma señal no deberá duplicar transiciones.

---

## Orden parcial consciente

En sistemas distribuidos no deberá asumirse un orden global total.

---

## Causalidad preservada

Toda transición deberá poder relacionarse con:

- comando;
- evento;
- Step Run;
- Activity Result;
- actor.

---

## Reconciliación

El estado interno y el externo deberán poder compararse y reparar divergencias.

---

## Cancelación cooperativa

La cancelación deberá propagarse mediante una solicitud antes de recurrir a terminación forzada.

---

## Resultado separado del estado

El estado indica dónde está la ejecución.

El resultado indica qué produjo.

---

## Seguridad en transiciones

No todo actor podrá ejecutar cualquier transición.

---

# Arquitectura conceptual

```text
┌───────────────────────────────────────────────┐
│                 Command Layer                 │
│                                               │
│ Start · Pause · Resume · Cancel · Signal      │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│          State Transition Validator           │
│                                               │
│ Current State · Guard · Policy · Revision     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              State Transition                 │
│                                               │
│ Previous · Next · Reason · Actor · Timestamp  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                 State Store                   │
│                                               │
│ Execution · Step · Job · Timers · Signals     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Event Publisher                 │
│                                               │
│ Lifecycle · Domain · Audit · Scheduler        │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│           Consequence and Scheduling          │
│                                               │
│ Activate · Queue · Retry · Complete · Wait    │
└───────────────────────────────────────────────┘
```

---

# State Machine Definition

Toda entidad con ciclo de vida deberá disponer de una definición formal.

Formato recomendado:

```text
STATE-MACHINE-XXXXXX
```

---

# Contrato

```yaml
state_machine:
  id: STATE-MACHINE-EXECUTION

  version: 1.0.0

  entity_type: execution

  initial_state: created

  terminal_states:
    - succeeded
    - succeeded_with_warnings
    - partial
    - failed
    - cancelled
    - timed_out
    - compensated

  transitions:
    - EXEC-TRANSITION-CREATE-VALIDATE
    - EXEC-TRANSITION-VALIDATE-QUEUE
    - EXEC-TRANSITION-QUEUE-RUN
```

---

# State Machine Versioning

Las máquinas de estados deberán versionarse.

Una Execution deberá conservar la versión con la que fue creada.

---

# No cambio de semántica in-place

Modificar una transición existente requerirá una nueva versión.

---

# Estado de Execution

Una **Execution State** representa la situación global de una instancia de Workflow.

---

# Estados principales

```text
created
validating
queued
running
waiting
paused
suspending
suspended
cancelling
compensating
recovering
succeeded
succeeded_with_warnings
partial
failed
cancelled
timed_out
compensated
blocked
```

---

# Created

La instancia existe, pero todavía no ha sido validada completamente.

---

# Validating

Se están comprobando:

- inputs;
- definición;
- políticas;
- capacidades;
- presupuesto;
- idempotencia.

---

# Queued

La Execution está admitida, pero aún no ha comenzado trabajo activo.

---

# Running

Existe al menos una actividad ejecutable, activa o pendiente de scheduling.

---

# Waiting

La Execution espera un elemento externo o temporal.

Ejemplos:

- señal;
- timer;
- aprobación;
- Child Execution;
- capacidad;
- ventana temporal.

---

# Paused

La ejecución se ha pausado de forma controlada y no se programarán nuevos Steps.

---

# Suspending

Se está intentando alcanzar un punto seguro de suspensión.

---

# Suspended

La Execution está detenida de forma durable en un checkpoint seguro.

---

# Cancelling

Se ha solicitado cancelación, pero todavía existen:

- Jobs activos;
- compensaciones;
- cleanup;
- confirmaciones pendientes.

---

# Compensating

Se están ejecutando acciones compensatorias.

---

# Recovering

La Execution se está restaurando desde:

- checkpoint;
- fallo del Orquestador;
- inconsistencia;
- worker loss;
- reconciliación.

---

# Blocked

La Execution no puede progresar sin una intervención o condición especial.

Ejemplos:

- política denegada;
- Artifact ausente;
- conflicto de versión;
- dependencia imposible;
- side effect con resultado desconocido.

---

# Succeeded

Todos los requisitos obligatorios han finalizado correctamente.

---

# Succeeded with Warnings

La ejecución cumple su objetivo, pero existen advertencias no bloqueantes.

---

# Partial

Solo se ha producido una parte válida del resultado.

---

# Failed

La Execution ha terminado sin cumplir su objetivo y sin compensación completa que cambie su estado final.

---

# Cancelled

La cancelación se ha completado.

---

# Timed Out

Se ha alcanzado el deadline global.

---

# Compensated

La ejecución original no se completó, pero sus efectos compensables han sido neutralizados según política.

---

# Estados terminales

```text
succeeded
succeeded_with_warnings
partial
failed
cancelled
timed_out
compensated
```

---

# Estados no terminales

Todos los demás.

---

# Execution State Contract

```yaml
execution_state:
  execution:
    id: EXEC-000041

  state: running

  revision: 18

  state_machine:
    id: STATE-MACHINE-EXECUTION
    version: 1.0.0

  entered_at: 2026-08-02T20:00:02Z

  reason:
    code: FIRST_STEP_STARTED
```

---

# Estado de Step Instance

El **Step Instance State** representa el progreso lógico de un Step dentro de una Execution.

---

# Estados

```text
created
blocked
pending
ready
queued
running
waiting
retry_scheduled
suspending
suspended
cancelling
compensating
succeeded
succeeded_with_warnings
partial
failed
skipped
cancelled
timed_out
compensated
```

---

# Created

La instancia ha sido materializada.

---

# Blocked

Sus dependencias o condiciones no permiten todavía evaluación completa.

---

# Pending

Está esperando dependencias potencialmente alcanzables.

---

# Ready

Puede ser programada.

---

# Queued

Se ha creado un Job y está esperando dispatch.

---

# Running

Existe un Step Run activo.

---

# Waiting

El Step espera:

- señal;
- Child Execution;
- timer;
- Human Task;
- resultado externo.

---

# Retry Scheduled

Existe un retry futuro planificado.

---

# Skipped

El Step no se ejecutará.

Deberá declarar motivo.

---

# Step State Contract

```yaml
step_instance_state:
  step_instance:
    id: STEP-INSTANCE-000041

  state: ready

  revision: 7

  reason:
    code: DEPENDENCIES_SATISFIED

  entered_at: 2026-08-02T20:02:00Z
```

---

# Estado de Step Run

El **Step Run State** representa un intento concreto.

---

# Estados

```text
created
dispatching
dispatched
accepted
running
heartbeat_lost
completion_pending
succeeded
succeeded_with_warnings
partial
failed
cancel_requested
cancelled
timed_out
unknown
abandoned
```

---

# Dispatching

El Scheduler está intentando asignarlo.

---

# Dispatched

La asignación fue enviada.

---

# Accepted

El Worker confirmó la recepción.

---

# Heartbeat Lost

Se ha superado el umbral de heartbeat, pero todavía no se ha determinado el resultado final.

---

# Completion Pending

El Worker afirma haber terminado, pero el resultado aún está siendo validado o persistido.

---

# Unknown

No puede determinarse si el side effect ocurrió.

---

# Abandoned

El Run ya no será considerado activo, pero se conserva para auditoría.

---

# Estado de Job

El **Job State** representa la unidad de scheduling.

---

# Estados

```text
created
admitted
rejected
ready
delayed
queued
leased
dispatched
running
retry_wait
waiting_signal
waiting_timer
waiting_human
completed
failed
cancelled
timed_out
dead_lettered
orphaned
```

---

# Admitted

Ha superado Admission Control.

---

# Rejected

No fue admitido.

---

# Delayed

No deberá estar disponible hasta una fecha concreta.

---

# Leased

Está reservado para un Worker.

---

# Retry Wait

Espera al siguiente intento.

---

# Dead-Lettered

No puede progresar automáticamente y se ha enviado a una Dead Letter Queue.

---

# Orphaned

Su lease expiró o el Worker desapareció.

---

# Job State Contract

```yaml
job_state:
  job:
    id: JOB-000041

  state: leased

  revision: 6

  lease:
    id: LEASE-000041

  worker:
    id: WORKER-001

  entered_at: 2026-08-02T20:02:01Z
```

---

# State Transition

Una **State Transition** representa un cambio válido entre dos estados.

Formato recomendado:

```text
STATE-TRANSITION-XXXXXX
```

---

# Contrato

```yaml
state_transition:
  id: STATE-TRANSITION-000041

  entity:
    type: execution
    id: EXEC-000041

  state_machine:
    id: STATE-MACHINE-EXECUTION
    version: 1.0.0

  from: queued
  to: running

  trigger:
    type: event
    id: EVENT-STEP-STARTED-000041

  actor:
    id: EXECUTION-COORDINATOR
    type: service

  expected_revision: 17
  resulting_revision: 18

  reason:
    code: FIRST_REQUIRED_STEP_STARTED

  occurred_at: 2026-08-02T20:00:02Z
```

---

# Transition Definition

Cada transición permitida deberá declararse.

```yaml
transition_definition:
  id: EXEC-TRANSITION-QUEUE-RUN

  entity_type: execution

  from:
    - queued

  to: running

  triggers:
    - step_started
    - child_execution_started

  guard:
    execution_not_cancelled: true
```

---

# Transition Guard

Una **Transition Guard** determina si la transición puede producirse.

---

# Guard Inputs

- estado actual;
- revisión;
- política;
- actor;
- contexto;
- deadline;
- Step states;
- permisos;
- resultados.

---

# Guard Contract

```yaml
transition_guard:
  id: GUARD-EXECUTION-START

  criteria:
    all:
      - definition_valid == true
      - policy_permitted == true
      - execution_not_cancelled == true
      - budget_available == true
      - at_least_one_step_ready == true
```

---

# Invalid Transition

Error:

```text
EXECUTION_STATE_TRANSITION_INVALID
```

---

# Stale Revision

```text
EXECUTION_STATE_REVISION_CONFLICT
```

---

# Transition Atomicity

La operación deberá persistir de manera atómica:

- nuevo estado;
- nueva revisión;
- History Entry;
- Outbox Event;
- timestamps.

---

# Transactional Outbox

Se recomienda utilizar un patrón de Outbox para evitar que:

- el estado cambie;
- el evento no se publique.

---

# Outbox Record

```yaml
outbox_record:
  id: OUTBOX-000041

  aggregate:
    type: execution
    id: EXEC-000041

  event:
    id: EVENT-EXECUTION-STATE-CHANGED-000041

  status: pending
```

---

# Command

Un **Command** expresa una intención de cambio.

Ejemplos:

```text
StartExecution
PauseExecution
ResumeExecution
CancelExecution
RetryStep
SkipStep
SendSignal
CompleteHumanTask
```

---

# Command vs Event

```text
Command
=
solicitud de que algo ocurra
```

```text
Event
=
hecho que ya ocurrió
```

---

# Ejemplo

```text
CancelExecution
```

no implica:

```text
ExecutionCancelled
```

Entre ambos pueden existir:

- rechazo;
- cancelación parcial;
- espera;
- timeout;
- compensación.

---

# Command Contract

```yaml
execution_command:
  id: EXEC-COMMAND-000041

  type: cancel_execution

  target:
    execution_id: EXEC-000041

  requested_by:
    id: USER-ADMIN-0001
    type: user

  expected_revision: 18

  options:
    reason: manual_operator_request
    run_compensation: true

  issued_at: 2026-08-02T20:05:00Z
```

---

# Command Handling

```text
Receive Command
        ↓
Authenticate
        ↓
Authorize
        ↓
Validate State
        ↓
Validate Revision
        ↓
Evaluate Policy
        ↓
Accept or Reject
        ↓
Persist Decision
        ↓
Produce Consequences
```

---

# Command Result

```yaml
command_result:
  command:
    id: EXEC-COMMAND-000041

  status: accepted

  transition:
    id: STATE-TRANSITION-000052

  resulting_state: cancelling
```

---

# Command Rejection

Deberá declarar:

- código;
- estado actual;
- política;
- retryability.

---

# Event

Un **Execution Event** representa un hecho durable relacionado con el lifecycle.

Formato recomendado:

```text
EXEC-EVENT-XXXXXX
```

---

# Event Categories

```text
lifecycle
step
job
worker
timer
signal
policy
quality
compensation
recovery
audit
domain
```

---

# Event Envelope

```yaml
event:
  id: EXEC-EVENT-000041

  type: execution_started
  version: 1.0.0

  occurred_at: 2026-08-02T20:00:02Z
  recorded_at: 2026-08-02T20:00:02.120Z

  subject:
    type: execution
    id: EXEC-000041

  source:
    id: EXECUTION-COORDINATOR

  correlation:
    correlation_id: CORR-000041
    causation_id: EXEC-COMMAND-START-000041
    trace_id: TRACE-000041

  tenant:
    id: TENANT-0001

  data:
    workflow: EXEC-DEF-KNOWLEDGE-PUBLICATION@1.0.0
```

---

# Event ID

Deberá ser globalmente único dentro del ámbito definido.

---

# Event Type Version

Deberá versionarse de forma independiente.

---

# Occurred At vs Recorded At

```text
occurred_at
```

indica cuándo sucedió el hecho.

```text
recorded_at
```

indica cuándo se persistió.

---

# Event Ordering

No deberá asumirse orden global entre todas las Executions.

---

# Per-Execution Sequence

Cada Execution deberá tener una secuencia monotónica.

```yaml
sequence:
  execution: 142
```

---

# Aggregate Ordering

Los eventos de una misma entidad deberán aplicarse en orden de revisión o secuencia.

---

# Out-of-Order Event

Podrá:

- almacenarse temporalmente;
- rechazarse;
- reconciliarse;
- solicitar eventos faltantes.

---

# Event Gap

```text
EXECUTION_EVENT_SEQUENCE_GAP
```

---

# Duplicate Event

Los consumidores deberán deduplicar por Event ID.

---

# Event Delivery Semantics

Se recomienda asumir:

```text
at-least-once
```

y exigir consumidores idempotentes.

---

# No asumir exactly-once end-to-end

Puede implementarse equivalencia funcional mediante:

- deduplicación;
- idempotency keys;
- transactional state;
- Outbox/Inbox.

---

# Inbox Pattern

Los consumidores podrán persistir IDs procesados.

```yaml
inbox_record:
  consumer: SCHEDULER-CORE
  event_id: EXEC-EVENT-000041
  status: processed
```

---

# Lifecycle Events

Catálogo inicial:

```text
execution_created
execution_validation_started
execution_validated
execution_queued
execution_started
execution_waiting
execution_paused
execution_resumed
execution_suspending
execution_suspended
execution_cancellation_requested
execution_cancelling
execution_compensation_started
execution_recovery_started
execution_blocked
execution_succeeded
execution_succeeded_with_warnings
execution_partial
execution_failed
execution_cancelled
execution_timed_out
execution_compensated
```

---

# Step Events

```text
step_created
step_blocked
step_ready
step_queued
step_started
step_waiting
step_retry_scheduled
step_succeeded
step_succeeded_with_warnings
step_partial
step_failed
step_skipped
step_cancelled
step_timed_out
step_compensation_started
step_compensated
```

---

# Job Events

```text
job_created
job_admitted
job_rejected
job_ready
job_delayed
job_queued
job_leased
job_dispatched
job_accepted
job_started
job_heartbeat_received
job_completed
job_failed
job_retry_scheduled
job_cancel_requested
job_cancelled
job_timed_out
job_orphaned
job_dead_lettered
```

---

# Event Data Minimization

Los eventos no deberán incluir grandes payloads.

Deberán usar:

- IDs;
- referencias;
- hashes;
- metadata mínima.

---

# Domain Event vs Operational Event

---

# Domain Event

Representa un cambio relevante para NovaCoquinaria.

Ejemplo:

```text
knowledge_snapshot_published
```

---

# Operational Event

Describe el funcionamiento del Orquestador.

Ejemplo:

```text
step_retry_scheduled
```

---

# No publicar todos los detalles internos como eventos de dominio

---

# Signal

Una **Signal** es un mensaje dirigido a una Execution o Step activo que puede modificar su progreso.

Formato recomendado:

```text
EXEC-SIGNAL-XXXXXX
```

---

# Signal Types

```text
resume
cancel
approval
rejection
external_result
manual_input
capacity_available
child_completed
custom
```

---

# Signal Contract

```yaml
execution_signal:
  id: EXEC-SIGNAL-000041

  type: approval

  target:
    execution_id: EXEC-000041
    step_instance_id: STEP-INSTANCE-APPROVAL-000041

  payload:
    decision: approve
    comment: Snapshot revisado.

  sender:
    id: USER-REVIEWER-0001
    type: user

  correlation:
    correlation_id: CORR-000041

  sent_at: 2026-08-02T20:15:00Z
```

---

# Signal Schema

Cada tipo deberá declarar schema.

---

# Signal Authentication

Toda señal deberá:

- autenticar sender;
- autorizar acción;
- validar tenant;
- validar target;
- validar estado.

---

# Signal Routing

La señal deberá poder dirigirse mediante:

- Execution ID;
- Step Instance ID;
- Human Task ID;
- Business Key autorizado;
- Correlation ID con selector.

---

# Preferencia

Utilizar identificadores concretos cuando sea posible.

---

# Signal Buffering

Una señal puede llegar antes de que el Step esté esperando.

La política podrá ser:

```text
buffer
reject
expire
route_to_execution
```

---

# Buffered Signal

```yaml
buffered_signal:
  signal: EXEC-SIGNAL-000041

  target:
    execution: EXEC-000041

  expires_at: 2026-08-03T20:15:00Z

  status: pending
```

---

# Signal Matching

Un Wait Node deberá declarar qué señales acepta.

```yaml
signal_wait:
  accepted_types:
    - approval
    - rejection

  correlation_field:
    human_task_id: HUMAN-TASK-000041
```

---

# Signal Deduplication

El Signal ID deberá impedir doble aplicación.

---

# Late Signal

Una señal recibida después de la terminación podrá:

- rechazarse;
- auditarse;
- iniciar una nueva Execution;
- almacenarse como no aplicada.

---

# Signal Timeout

Los Wait Nodes deberán tener timeout o política explícita de espera indefinida autorizada.

---

# Timer

Un **Execution Timer** representa una acción temporal durable.

Formato recomendado:

```text
EXEC-TIMER-XXXXXX
```

---

# Timer Types

```text
delay
deadline
retry
heartbeat_timeout
signal_timeout
human_task_timeout
schedule
poll
grace_period
```

---

# Timer Contract

```yaml
execution_timer:
  id: EXEC-TIMER-000041

  type: retry

  target:
    execution_id: EXEC-000041
    step_instance_id: STEP-INSTANCE-000041

  fire_at: 2026-08-02T20:10:00Z

  created_from:
    retry_policy: EXEC-RETRY-POLICY-INDEXING

  status: scheduled
```

---

# Timer States

```text
scheduled
armed
fired
cancelled
expired
failed
```

---

# Durable Timer Store

Los timers deberán persistirse en almacenamiento durable.

---

# Timer Wheel o Polling

La implementación podrá utilizar:

- timer wheel;
- priority queue;
- database polling;
- broker delayed messages;
- scheduler service.

El contrato no deberá depender de una tecnología concreta.

---

# Timer Precision

Deberá declararse.

Ejemplo:

```yaml
precision: PT1S
```

---

# Missed Timer

Si el Orquestador estuvo detenido y el tiempo ya pasó, el timer deberá dispararse al recuperarse según política.

---

# Missed Timer Policies

```text
fire_immediately
skip
reschedule
fail
coalesce
```

---

# Coalescing

Varios timers repetitivos vencidos podrán combinarse cuando la semántica lo permita.

---

# Timer Idempotency

Disparar dos veces el mismo timer no deberá duplicar la transición.

---

# Timer Event

```yaml
event:
  type: execution_timer_fired

  subject:
    id: EXEC-TIMER-000041
    type: timer

  data:
    scheduled_at: 2026-08-02T20:05:00Z
    fired_at: 2026-08-02T20:10:00.420Z
```

---

# Wait State

Una Execution o Step puede entrar en estado `waiting` sin consumir un Worker.

---

# Wait Reasons

```text
timer
signal
human_task
child_execution
external_job
capacity
policy
artifact
manual_intervention
```

---

# Wait Record

Formato recomendado:

```text
EXEC-WAIT-XXXXXX
```

---

# Contrato

```yaml
execution_wait:
  id: EXEC-WAIT-000041

  execution:
    id: EXEC-000041

  step_instance:
    id: STEP-INSTANCE-APPROVAL-000041

  type: signal

  condition:
    accepted_signal_types:
      - approval
      - rejection

  timeout:
    timer_id: EXEC-TIMER-APPROVAL-000041

  status: active
```

---

# Wait States

```text
created
active
satisfied
timed_out
cancelled
failed
```

---

# Wait Satisfaction

Deberá registrar:

- evento o señal;
- condición satisfecha;
- timestamp;
- transición resultante.

---

# No polling activo innecesario

Una espera por señal deberá ser event-driven cuando sea posible.

---

# External Job Wait

Si una Activity externa devuelve un Job ID, el Step podrá quedar esperando:

- callback;
- event;
- polling controlado.

---

# Pause

Una **Pause** evita programar nuevo trabajo sin necesariamente cancelar trabajo activo.

---

# Pause Types

```text
soft
safe_point
immediate
administrative
policy
```

---

# Soft Pause

No programa nuevos Steps, pero deja terminar los activos.

---

# Safe-Point Pause

Espera a un checkpoint o frontera segura.

---

# Immediate Pause

Solicita detener también tareas activas que sean pausables.

---

# Pause Command

```yaml
execution_command:
  type: pause_execution

  options:
    mode: safe_point
    reason: maintenance_window
```

---

# Pause Preconditions

- estado no terminal;
- actor autorizado;
- workflow pausible;
- no compensación crítica en curso, salvo política.

---

# Paused Execution

Deberá conservar:

- Steps activos;
- timers;
- señales;
- checkpoint;
- reason;
- actor.

---

# Timer Behaviour While Paused

La política deberá declarar si los timers:

```text
continue
freeze
reschedule
expire
```

---

# Default Recommendation

Los deadlines absolutos continúan.

Los timers internos de retry podrán congelarse o reprogramarse según profile.

---

# Resume

La reanudación deberá:

- validar estado;
- validar definición;
- validar policies;
- validar capabilities;
- comprobar Artifacts;
- recalcular deadlines;
- reactivar scheduling.

---

# Resume Command

```yaml
execution_command:
  type: resume_execution

  target:
    execution_id: EXEC-000041

  expected_state: paused
```

---

# No resume desde estado terminal

---

# Suspension

La **Suspension** representa una detención durable más fuerte que Pause.

---

# Diferencia conceptual

```text
Pause
```

es una decisión operativa reversible.

```text
Suspension
```

implica alcanzar y persistir un punto seguro para una interrupción prolongada o migración.

---

# Suspension Process

```text
Request Suspension
        ↓
Stop New Scheduling
        ↓
Wait or Cancel Active Work
        ↓
Create Checkpoint
        ↓
Validate Checkpoint
        ↓
Enter Suspended
```

---

# Suspension Reasons

- mantenimiento;
- migración;
- falta de capacidad prolongada;
- policy hold;
- revisión;
- incidente.

---

# Cancelación

La cancelación deberá modelarse como proceso, no como cambio instantáneo.

---

# Cancellation Lifecycle

```text
Cancel Requested
        ↓
Validate Request
        ↓
Execution → Cancelling
        ↓
Stop New Scheduling
        ↓
Propagate Cancel Requests
        ↓
Wait for Active Work
        ↓
Cleanup / Compensation Optional
        ↓
Execution → Cancelled
```

---

# Cancellation Request

Formato recomendado:

```text
EXEC-CANCEL-REQUEST-XXXXXX
```

---

# Contrato

```yaml
cancellation_request:
  id: EXEC-CANCEL-REQUEST-000041

  execution:
    id: EXEC-000041

  requested_by:
    id: USER-ADMIN-0001
    type: user

  mode: cooperative

  reason:
    code: OPERATOR_REQUEST

  compensation:
    requested: true

  requested_at: 2026-08-02T20:05:00Z
```

---

# Cancellation Modes

```text
cooperative
graceful
force_after_grace
immediate_force
compensating
```

---

# Cooperative

Solicita a Jobs activos que finalicen cuanto antes.

---

# Graceful

Permite finalizar unidades seguras actuales.

---

# Force After Grace

Espera un periodo y después fuerza terminación.

---

# Immediate Force

Solo para situaciones críticas y Activities compatibles.

---

# Compensating

Tras cancelar, ejecuta compensaciones.

---

# Cancellation Scope

Podrá afectar:

```text
execution
step
branch
stage
child_execution
map_item
```

---

# Cancellation Propagation

Valores:

```text
cascade
request_cancel
do_not_cancel
detach
policy_based
```

---

# Active Activity Cancellation

El Adapter deberá declarar si soporta:

- cancel;
- pause;
- abort;
- none.

---

# Cancellation Acknowledgement

El Worker deberá confirmar:

- accepted;
- already_completed;
- not_cancellable;
- unknown.

---

# Cancel Race

Puede ocurrir que la Activity termine al mismo tiempo que llega la cancelación.

La política deberá resolver mediante:

- revisión;
- timestamp causal;
- estado persistido;
- idempotency.

---

# Completed Before Cancel

Si el resultado se persistió primero, el Step podrá quedar `succeeded`.

La Execution podrá seguir cancelándose para los Steps restantes.

---

# Forced Termination

Deberá utilizarse únicamente cuando:

- el Worker puede aislarse;
- se conoce el impacto;
- existe reconciliación;
- la política lo permite.

---

# No asumir rollback de side effects

---

# Cancellation Result

```yaml
cancellation_result:
  request:
    id: EXEC-CANCEL-REQUEST-000041

  execution:
    id: EXEC-000041

  active_jobs:
    requested: 3
    cancelled: 2
    already_completed: 1

  compensation:
    status: succeeded

  final_state: cancelled
```

---

# Deadline

Toda Execution podrá disponer de un deadline global.

---

# Deadline Types

```text
absolute
relative
stage
step
activity
soft
hard
```

---

# Soft Deadline

Genera:

- warning;
- prioridad;
- escalación;
- degradación.

---

# Hard Deadline

Obliga a iniciar timeout o cancelación.

---

# Deadline Record

```yaml
execution_deadline:
  type: hard
  value: 2026-08-02T20:30:02Z
```

---

# Deadline Timer

Deberá materializarse como timer durable.

---

# Timeout

Un timeout afecta a una operación concreta.

---

# Timeout Scopes

```text
execution
stage
step
step_run
activity
dispatch
heartbeat
signal
human_task
join
```

---

# Timeout Policy

Formato recomendado:

```text
EXEC-TIMEOUT-POLICY-XXXXXX
```

---

# Contrato

```yaml
timeout_policy:
  id: EXEC-TIMEOUT-POLICY-INDEXING

  scope: activity

  duration: PT10M

  on_timeout:
    action: retry

  maximum_timeout_retries: 1

  cancellation:
    request_worker_cancel: true
```

---

# Timeout Actions

```text
fail
retry
cancel
compensate
fallback
continue_partial
escalate
wait_for_review
```

---

# Heartbeat Timeout

No equivale automáticamente a Activity Timeout.

Puede producir:

```text
unknown
```

hasta reconciliar.

---

# Grace Period

Podrá existir antes de declarar timeout final.

---

# Blocking

Una Execution queda `blocked` cuando no puede progresar automáticamente.

---

# Blocking Reasons

```text
policy_denied
artifact_missing
capability_missing
unknown_side_effect
version_conflict
manual_intervention
dependency_impossible
security_hold
quota_hold
external_inconsistency
```

---

# Block Record

```yaml
execution_block:
  id: EXEC-BLOCK-000041

  execution:
    id: EXEC-000041

  reason:
    code: UNKNOWN_SIDE_EFFECT

  source:
    step_run: STEP-RUN-000045

  resolution_options:
    - reconcile
    - compensate
    - mark_succeeded
    - mark_failed

  status: active
```

---

# Block Resolution

Deberá realizarse mediante un Command o proceso de reconciliación autorizado.

---

# No desbloqueo silencioso

---

# Stalled Execution

Una Execution podrá estar técnicamente `running`, pero sin progreso.

---

# Stall Conditions

- no cambia la secuencia;
- no existen heartbeats;
- no hay Jobs activos;
- existen Steps ready sin dispatch;
- Join espera ramas imposibles;
- timer no dispara;
- señal no enruta;
- worker lease inconsistente.

---

# Stall Detection

Formato recomendado:

```text
EXEC-STALL-DETECTOR-XXXXXX
```

---

# Stall Policy

```yaml
stall_policy:
  id: EXEC-STALL-POLICY-STANDARD

  thresholds:
    no_state_change: PT15M
    ready_without_dispatch: PT2M
    waiting_without_timer: PT1M

  actions:
    - emit_warning
    - reconcile
    - escalate
```

---

# Stalled vs Waiting

Una Execution correctamente `waiting` no está stalled si:

- existe Wait Record;
- existe condición;
- existe timeout o policy;
- su estado es coherente.

---

# Reconciliation

La **State Reconciliation** compara estado interno y externo.

---

# Casos

- Worker indica completed, Orchestrator indica running;
- lease expirado, Activity externa sigue activa;
- Child Execution finalizó, parent sigue waiting;
- timer fired, Wait sigue activo;
- Artifact existe, Step figura failed.

---

# Reconciliation Request

```yaml
reconciliation_request:
  id: EXEC-RECONCILE-REQ-000041

  execution:
    id: EXEC-000041

  scope:
    step_run: STEP-RUN-000045

  reason: heartbeat_timeout
```

---

# Reconciliation Sources

- State Store;
- Worker Registry;
- external engine;
- idempotency record;
- Artifact Store;
- Event History;
- Child Execution state.

---

# Reconciliation Result

```yaml
reconciliation_result:
  id: EXEC-RECONCILE-RESULT-000041

  internal_state: running
  external_state: succeeded

  decision:
    action: apply_external_result

  evidence:
    activity_result_id: ACT-RESULT-000041
    idempotency_key: EXEC-000041:STEP-BUILD-INDEX

  status: resolved
```

---

# Reconciliation Actions

```text
no_change
apply_external_result
retry
mark_unknown
mark_failed
request_cancel
compensate
manual_review
```

---

# No confiar en una única fuente no autenticada

---

# State Projection

Para consultas rápidas podrán existir proyecciones derivadas.

---

# Ejemplos

```text
Execution Summary
Active Jobs
Waiting Executions
Failed Steps
Tenant Queue State
```

---

# Source of Truth

La fuente canónica deberá seguir siendo:

- State Store;
- History;
- Transition Records.

---

# Eventual Consistency

Las proyecciones podrán tener retraso.

Deberán declarar:

- last sequence;
- last update;
- lag.

---

# Execution Summary

```yaml
execution_summary:
  execution_id: EXEC-000041
  state: running

  steps:
    total: 9
    succeeded: 4
    running: 2
    ready: 1
    blocked: 2

  progress:
    percentage: 44

  projection:
    last_sequence: 142
```

---

# Progress Calculation

No deberá basarse únicamente en:

```text
completed_steps / total_steps
```

Podrá considerar:

- pesos;
- duración estimada;
- dynamic nodes;
- critical path;
- stages.

---

# Progress Profile

```yaml
progress_profile:
  strategy: weighted_steps

  weights:
    STEP-VALIDATE: 0.10
    STEP-BUILD-GRAPH: 0.25
    STEP-BUILD-INDEX: 0.40
    STEP-RUN-GATES: 0.15
    STEP-PUBLISH: 0.10
```

---

# No mostrar 100 % antes de terminalización

---

# Terminalización de Step

Un Step Instance podrá terminalizarse cuando:

- su último Run sea terminal;
- se haya validado el output;
- se hayan aplicado bindings;
- se haya persistido resultado;
- se hayan creado Artifacts;
- se haya evaluado retry/fallback.

---

# Step Completion Decision

```yaml
step_completion_decision:
  step_instance: STEP-INSTANCE-000041

  run:
    id: STEP-RUN-000045
    status: succeeded

  output_validation: passed
  quality_gate: passed
  retry_required: false

  final_step_state: succeeded
```

---

# Terminalización de Execution

Una Execution podrá terminalizarse cuando:

- no queden Steps activos;
- no existan retries pendientes;
- no existan timers pendientes relevantes;
- no existan waits activos;
- no existan compensaciones pendientes;
- se hayan evaluado terminal nodes;
- se haya construido el Result.

---

# Finalization Process

```text
Detect Terminal Condition
        ↓
Freeze New Scheduling
        ↓
Validate Step States
        ↓
Aggregate Outputs
        ↓
Validate Result Schema
        ↓
Run Final Quality Gate
        ↓
Persist Execution Result
        ↓
Transition to Terminal State
        ↓
Publish Terminal Event
```

---

# Finalization Lock

Deberá evitar dos terminalizaciones simultáneas.

---

# Final Result Builder

Formato recomendado:

```text
EXEC-RESULT-BUILDER-XXXXXX
```

---

# Result Aggregation

Podrá incluir:

- Workflow Outputs;
- Artifact References;
- Step Summary;
- diagnostics;
- costs;
- timings;
- warnings;
- compensation status.

---

# Result Status Mapping

```text
All required Steps succeeded
→ succeeded

Required Steps succeeded + warnings
→ succeeded_with_warnings

Partial contract satisfied
→ partial

Required Step terminal failure
→ failed

Cancellation completed
→ cancelled

Deadline terminal
→ timed_out

Failure + successful compensations
→ compensated
```

---

# Execution Result Contract

```yaml
execution_result:
  id: EXEC-RESULT-000041

  execution:
    id: EXEC-000041

  state: succeeded_with_warnings

  outputs:
    published_snapshot_id: IDX-SNAP-20260802-0001

  artifacts:
    - EXEC-ARTIFACT-000041

  step_summary:
    total: 9
    succeeded: 8
    succeeded_with_warnings: 1
    failed: 0
    skipped: 0

  warnings:
    - code: OPTIONAL_METADATA_INCOMPLETE

  timing:
    started_at: 2026-08-02T20:00:02Z
    completed_at: 2026-08-02T20:10:00Z
    duration: PT9M58S

  final_history_sequence: 284
```

---

# Result Validation

Deberá comprobar:

- output schema;
- required outputs;
- Artifact checksums;
- terminal state compatibility;
- no active work;
- security;
- diagnostics;
- lineage.

---

# Result Amendment

No deberá modificarse un Result terminal.

Una corrección deberá crear:

- Amendment Record;
- Recovery Execution;
- nueva Execution Result relacionada.

---

# Execution Lifecycle Policy

Formato recomendado:

```text
EXEC-LIFECYCLE-POLICY-XXXXXX
```

---

# Contrato

```yaml
execution_lifecycle_policy:
  id: EXEC-LIFECYCLE-POLICY-STANDARD

  version: 1.0.0

  pause:
    allowed_states:
      - queued
      - running
      - waiting

  cancel:
    allowed_states:
      - created
      - validating
      - queued
      - running
      - waiting
      - paused
      - suspended
      - blocked

  terminal_state_mutation: forbidden

  timers_while_paused: continue_deadlines

  child_cancellation: request_cancel
```

---

# Lifecycle Policy por Workflow

Un Workflow podrá restringir:

- pausabilidad;
- cancelabilidad;
- suspension;
- reanudación;
- compensación.

---

# Seguridad de transiciones

---

# Transition Authorization

Toda operación deberá comprobar:

- actor;
- role;
- tenant;
- target;
- current state;
- command type;
- workflow policy.

---

# Ejemplo

Solo un rol administrativo podrá ejecutar:

```text
force_complete
```

o:

```text
mark_unknown_as_succeeded
```

---

# Dangerous Administrative Commands

```text
force_fail
force_complete
skip_required_step
waive_quality_gate
override_unknown_outcome
terminate_worker_job
```

---

# Requisitos

- autorización reforzada;
- motivo obligatorio;
- auditoría;
- scope;
- doble aprobación cuando proceda;
- no aplicable a controles no eximibles.

---

# Audit Record

```yaml
execution_audit_event:
  action: execution.force_fail

  actor:
    id: USER-ADMIN-0001

  execution:
    id: EXEC-000041

  previous_state: blocked
  resulting_state: failed

  justification: Resultado externo no recuperable.

  approval:
    required: true
    approved_by: USER-ADMIN-0002
```

---

# Event Security

Los eventos deberán:

- evitar secretos;
- aplicar clasificación;
- aislar tenants;
- firmarse cuando proceda;
- validar producers.

---

# Signal Security

Una señal no deberá modificar:

- tenant;
- principal;
- policy set;
- definición;
- budget duro.

---

# Timer Security

La creación o cancelación manual de timers deberá estar autorizada.

---

# Observabilidad del ciclo de vida

---

# Métricas de estados

- Executions por estado;
- Steps por estado;
- Jobs por estado;
- tiempo en cada estado;
- terminalización por resultado.

---

# Transition Metrics

- transiciones por tipo;
- invalid transition attempts;
- revision conflicts;
- transition latency;
- event publication lag.

---

# Waiting Metrics

- waiting duration;
- waits por tipo;
- signal latency;
- human task wait;
- child execution wait;
- timer drift.

---

# Cancellation Metrics

- cancellation requests;
- cancellation latency;
- cooperative success rate;
- forced termination rate;
- compensation after cancellation.

---

# Pause Metrics

- pauses;
- pause duration;
- resume failures;
- suspended executions.

---

# Stall Metrics

- stalled executions;
- stall reasons;
- reconciliation attempts;
- automatic recovery rate.

---

# Event Metrics

- events produced;
- duplicate events;
- sequence gaps;
- outbox lag;
- consumer lag;
- dead-lettered events.

---

# Signal Metrics

- signals received;
- signals buffered;
- duplicate signals;
- rejected signals;
- expired signals.

---

# Timer Metrics

- timers scheduled;
- timers fired;
- timer drift;
- missed timers;
- cancelled timers;
- duplicate firing prevented.

---

# State Duration

Deberá medirse por:

```text
created_duration
queued_duration
running_duration
waiting_duration
paused_duration
cancelling_duration
compensating_duration
```

---

# State Transition Log

```yaml
log:
  event: execution_state_changed

  execution_id: EXEC-000041

  from: running
  to: waiting

  reason: human_approval_required

  revision: 24

  correlation_id: CORR-000041
```

---

# No payloads sensibles

---

# Tracing

```text
Command Received
↓
Authorization
↓
Guard Evaluation
↓
Transition Persisted
↓
Outbox Event Created
↓
Event Published
↓
Consequences Scheduled
```

---

# Diagnósticos

Códigos iniciales:

```text
EXECUTION_STATE_TRANSITION_INVALID
EXECUTION_STATE_REVISION_CONFLICT
EXECUTION_STATE_MACHINE_VERSION_MISSING
EXECUTION_STATE_TERMINAL_MUTATION_FORBIDDEN
EXECUTION_COMMAND_NOT_AUTHORIZED
EXECUTION_COMMAND_STATE_INCOMPATIBLE
EXECUTION_EVENT_DUPLICATE
EXECUTION_EVENT_SEQUENCE_GAP
EXECUTION_EVENT_OUT_OF_ORDER
EXECUTION_EVENT_SCHEMA_INVALID
EXECUTION_SIGNAL_SCHEMA_INVALID
EXECUTION_SIGNAL_NOT_AUTHORIZED
EXECUTION_SIGNAL_TARGET_NOT_FOUND
EXECUTION_SIGNAL_DUPLICATE
EXECUTION_SIGNAL_EXPIRED
EXECUTION_SIGNAL_NOT_EXPECTED
EXECUTION_TIMER_INVALID
EXECUTION_TIMER_DUPLICATE_FIRE
EXECUTION_TIMER_MISSED
EXECUTION_TIMER_DRIFT_EXCEEDED
EXECUTION_WAIT_WITHOUT_RESOLUTION
EXECUTION_PAUSE_NOT_SUPPORTED
EXECUTION_RESUME_VALIDATION_FAILED
EXECUTION_SUSPENSION_CHECKPOINT_INVALID
EXECUTION_CANCELLATION_NOT_SUPPORTED
EXECUTION_CANCELLATION_TIMEOUT
EXECUTION_FORCED_TERMINATION_REQUIRED
EXECUTION_BLOCKED
EXECUTION_STALLED
EXECUTION_RECONCILIATION_REQUIRED
EXECUTION_RECONCILIATION_FAILED
EXECUTION_TERMINALIZATION_CONFLICT
EXECUTION_RESULT_SCHEMA_INVALID
EXECUTION_RESULT_REQUIRED_OUTPUT_MISSING
EXECUTION_RESULT_ARTIFACT_INVALID
```

---

# Diagnostic Contract

```yaml
execution_diagnostic:
  id: EXEC-DIAGNOSTIC-000041

  code: EXECUTION_STATE_TRANSITION_INVALID
  severity: error

  execution:
    id: EXEC-000041

  details:
    current_state: succeeded
    requested_state: running

  message: >
    Una ejecución terminal no puede volver directamente
    al estado running.

  retryable: false
```

---

# Quality Gate de State Machine

```yaml
quality_gate:
  id: QG-EXECUTION-STATE-MACHINE-0001

  criteria:
    all:
      - initial_state_defined == true
      - terminal_states_defined == true
      - transitions_versioned == true
      - invalid_transitions_blocked == true
      - terminal_mutations_forbidden == true
      - transition_guards_defined == true
      - revision_control_enabled == true
```

---

# Quality Gate de eventos

```yaml
quality_gate:
  id: QG-EXECUTION-EVENTS-0001

  criteria:
    all:
      - event_ids_unique == true
      - event_schemas_valid == true
      - execution_sequences_contiguous == true
      - correlation_present == true
      - causation_present == true
      - outbox_delivery_enabled == true
      - duplicate_consumption_safe == true
```

---

# Quality Gate de señales

```yaml
quality_gate:
  id: QG-EXECUTION-SIGNALS-0001

  criteria:
    all:
      - signal_schema_valid == true
      - sender_authenticated == true
      - sender_authorized == true
      - target_valid == true
      - deduplication_enabled == true
      - buffering_policy_defined == true
      - expiration_defined == true
```

---

# Quality Gate de timers

```yaml
quality_gate:
  id: QG-EXECUTION-TIMERS-0001

  criteria:
    all:
      - timer_store_durable == true
      - timer_ids_unique == true
      - duplicate_fire_safe == true
      - missed_timer_policy_defined == true
      - precision_declared == true
      - timer_drift_observable == true
```

---

# Quality Gate de cancelación

```yaml
quality_gate:
  id: QG-EXECUTION-CANCELLATION-0001

  criteria:
    all:
      - cancellation_states_defined == true
      - propagation_policy_defined == true
      - active_job_handling_defined == true
      - grace_period_defined == true
      - compensation_policy_defined == true
      - forced_termination_audited == true
```

---

# Quality Gate de terminalización

```yaml
quality_gate:
  id: QG-EXECUTION-FINALIZATION-0001

  criteria:
    all:
      - no_active_required_steps == true
      - no_pending_required_retries == true
      - no_unresolved_required_waits == true
      - required_outputs_present == true
      - result_schema_valid == true
      - artifacts_valid == true
      - final_state_compatible == true
      - final_event_published == true
```

---

# Casos de uso

---

# Caso de uso 1 — Ejecución normal

```text
created
↓
validating
↓
queued
↓
running
↓
succeeded
```

Cada transición queda persistida y emite su evento correspondiente.

---

# Caso de uso 2 — Espera humana

Un Step crea una Human Task.

```text
running
↓
waiting
↓
approval signal
↓
running
```

No se mantiene ningún Worker ocupado durante la espera.

---

# Caso de uso 3 — Retry temporal

Un Step falla con error retryable.

```text
running
↓
retry_scheduled
↓
timer fired
↓
ready
↓
queued
↓
running
```

---

# Caso de uso 4 — Evento duplicado

El consumidor recibe dos veces `step_completed`.

El Inbox Record impide aplicar la transición dos veces.

---

# Caso de uso 5 — Señal temprana

La aprobación llega antes de que el Step entre en `waiting`.

La señal se almacena y se consume al activar el Wait Node.

---

# Caso de uso 6 — Timer perdido por reinicio

El servicio se recupera después de `fire_at`.

La política `fire_immediately` activa el retry.

---

# Caso de uso 7 — Pause segura

Un operador solicita `safe_point`.

El Orquestador:

- deja de programar nuevos Steps;
- espera a que terminen los activos;
- crea checkpoint;
- entra en `paused`.

---

# Caso de uso 8 — Resume fallido

Durante la pausa se retiró una versión de Activity necesaria.

La validación de reanudación falla y la Execution queda `blocked`.

---

# Caso de uso 9 — Cancelación cooperativa

La Execution tiene tres Jobs activos.

Dos aceptan cancelación y uno ya había terminado.

Después del cleanup la Execution queda `cancelled`.

---

# Caso de uso 10 — Cancelación con compensación

La publicación ya activó un snapshot candidato.

La cancelación ejecuta una Activity que retira el candidato.

El estado final es `cancelled` o `compensated` según política.

---

# Caso de uso 11 — Resultado desconocido

Se pierde conexión tras invocar una operación no idempotente.

El Step Run queda `unknown` y la Execution pasa a `blocked` hasta reconciliar.

---

# Caso de uso 12 — Stall

Existen Steps `ready`, pero no se han despachado durante el umbral permitido.

El Stall Detector inicia reconciliación del Scheduler.

---

# Caso de uso 13 — Child completado

La Child Execution termina, pero el parent sigue esperando por pérdida de evento.

La reconciliación detecta el estado y satisface el Wait Record.

---

# Caso de uso 14 — Deadline global

El deadline dispara mientras hay Jobs activos.

La Execution pasa a `cancelling`, solicita cancelación y termina como `timed_out`.

---

# Caso de uso 15 — Carrera de terminalización

Dos nodos finales intentan completar la Execution.

El Finalization Lock y la revisión impiden crear dos Results.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Campo status sin máquina de estados

Permite transiciones incoherentes.

---

## Modificar estado directamente desde cualquier componente

Toda transición deberá pasar por el coordinador o servicio autorizado.

---

## Publicar evento antes de persistir estado

Puede anunciar hechos que no quedaron confirmados.

---

## Actualizar estado y evento en transacciones separadas sin Outbox

Puede perder eventos.

---

## Estados terminales reversibles

Rompen historial y semántica.

---

## Reutilizar una Execution fallida para un nuevo intento global

Deberá crearse una Recovery o nueva Execution.

---

## Considerar `cancel_requested` equivalente a `cancelled`

La cancelación puede tardar o fallar.

---

## Eliminar una Execution cancelada

Debe conservarse auditoría.

---

## Wait manteniendo thread o Worker

Desperdicia recursos.

---

## Timer solo en memoria

Se pierde al reiniciar.

---

## Disparar timers sin deduplicación

Puede repetir acciones.

---

## Señales sin schema

Generan inputs opacos.

---

## Señales sin autenticación

Permiten alterar workflows.

---

## Buscar señales solo por Business Key no único

Puede dirigirlas a la Execution incorrecta.

---

## Ignorar señales tempranas

Puede bloquear procesos que ya recibieron respuesta.

---

## Bufferizar señales indefinidamente

Debe existir expiración.

---

## Exactly-once asumido mágicamente

Los consumidores deberán ser idempotentes.

---

## Orden global de eventos

No es necesario ni escalable para todos los aggregates.

---

## No conservar causation

Dificulta reconstruir por qué cambió el estado.

---

## Pausa que detiene deadlines sin política

Puede incumplir contratos.

---

## Resume sin revalidar contexto

Puede usar capacidades o políticas obsoletas.

---

## Forzar terminación como primera opción

Puede dejar side effects desconocidos.

---

## Marcar Job failed al perder heartbeat inmediatamente

El resultado puede ser desconocido.

---

## Resolver `unknown` mediante retry ciego

Puede duplicar efectos.

---

## Bloqueo sin opciones de resolución

Una Execution bloqueada deberá ser operable.

---

## Stall Detector confundiendo waiting con bloqueo

Las esperas válidas tienen registros y condiciones.

---

## Reconciliación no auditada

Puede alterar estados importantes.

---

## Progreso calculado solo por número de Steps

No refleja pesos ni rutas dinámicas.

---

## Finalizar antes de validar outputs

Puede producir un Result inválido.

---

## Crear Result después del evento terminal

El evento podría apuntar a un resultado inexistente.

---

## Modificar Result terminal

Debe conservarse inmutabilidad.

---

## Comandos administrativos peligrosos sin doble control

Comprometen gobernanza.

---

# Reglas mínimas de conformidad

---

## Máquinas de estados versionadas

Execution, Step y Job deberán disponer de modelos formales.

---

## Estados terminales definidos

Deberán diferenciarse claramente.

---

## Transiciones declaradas

Toda transición deberá estar permitida por contrato.

---

## Transition Guards

Toda transición sensible deberá validar condiciones.

---

## Control de revisión

Las actualizaciones concurrentes deberán detectar conflictos.

---

## Registro atómico

Estado, History y Outbox deberán mantenerse coherentes.

---

## Commands identificados

Toda solicitud de cambio deberá ser trazable.

---

## Events identificados

Todo hecho deberá tener ID, tipo y versión.

---

## Correlation y Causation

Todos los eventos de ejecución deberán conservar ambas.

---

## Event Deduplication

Los consumidores deberán ser seguros ante reentrega.

---

## Signals tipadas

Toda señal deberá cumplir schema.

---

## Signal Security

El sender deberá estar autenticado y autorizado.

---

## Signal Buffering gobernado

Las señales tempranas deberán seguir una política.

---

## Timers durables

Los timers no deberán depender de memoria local.

---

## Timer Idempotency

El disparo repetido no deberá duplicar efectos.

---

## Wait Records

Toda espera deberá tener una condición explícita.

---

## Pause gobernada

Deberá declarar comportamiento de Jobs y timers.

---

## Resume validado

No deberá continuar sin comprobar compatibilidad.

---

## Cancelación como proceso

Deberá distinguir solicitud y finalización.

---

## Propagación explícita

Children, Jobs y branches deberán tener política de cancelación.

---

## Unknown Outcomes

Deberán bloquear retry ciego.

---

## Stall Detection

Las ejecuciones sin progreso deberán poder detectarse.

---

## Reconciliation

Deberá existir un mecanismo formal de reparación.

---

## Finalization Lock

Solo podrá producirse un Result terminal.

---

## Result validado

Toda salida deberá cumplir schema y Artifacts.

---

## Auditabilidad

Overrides y comandos peligrosos deberán registrarse.

---

# Conformidad de State Machine

Será conforme cuando:

- tenga ID;
- tenga versión;
- declare estado inicial;
- declare estados terminales;
- declare transiciones;
- declare guards;
- prohíba mutación terminal;
- permita validación.

---

# Conformidad de State Transition

Será conforme cuando:

- tenga ID;
- identifique entidad;
- declare `from`;
- declare `to`;
- preserve trigger;
- preserve actor;
- valide revisión;
- declare razón;
- quede persistida.

---

# Conformidad de Event

Será conforme cuando:

- tenga ID;
- tenga tipo;
- tenga versión;
- identifique subject;
- declare source;
- preserve tenant;
- preserve correlation;
- preserve causation;
- cumpla schema.

---

# Conformidad de Signal

Será conforme cuando:

- tenga ID;
- declare tipo;
- declare target;
- cumpla schema;
- identifique sender;
- preserve tenant;
- declare expiración cuando proceda;
- sea deduplicable.

---

# Conformidad de Timer

Será conforme cuando:

- tenga ID;
- tenga tipo;
- declare target;
- declare `fire_at`;
- declare policy;
- sea durable;
- sea idempotente;
- preserve estado.

---

# Conformidad de Wait

Será conforme cuando:

- tenga ID;
- identifique Execution o Step;
- declare tipo;
- declare condición;
- declare resolución;
- declare timeout o excepción autorizada;
- no consuma Worker.

---

# Conformidad de Cancellation Request

Será conforme cuando:

- tenga ID;
- identifique Execution;
- identifique actor;
- declare modo;
- declare razón;
- declare compensation policy;
- preserve timestamp;
- sea auditable.

---

# Conformidad de Reconciliation

Será conforme cuando:

- tenga Request;
- declare scope;
- consulte fuentes autorizadas;
- preserve evidencia;
- declare decisión;
- registre transición;
- no oculte incertidumbre.

---

# Conformidad de Execution Result

Será conforme cuando:

- tenga ID;
- identifique Execution;
- declare estado terminal;
- cumpla output schema;
- preserve Artifacts;
- preserve Step Summary;
- preserve diagnostics;
- declare timing;
- declare History Sequence;
- sea inmutable.

---

# Lista de comprobación

Antes de aprobar la gestión de estados deberá comprobarse:

```text
[ ] Existe State Machine para Execution.
[ ] Existe State Machine para Step Instance.
[ ] Existe State Machine para Step Run.
[ ] Existe State Machine para Job.
[ ] Las máquinas de estados están versionadas.
[ ] Los estados iniciales están definidos.
[ ] Los estados terminales están definidos.
[ ] Las transiciones permitidas están declaradas.
[ ] Las transiciones inválidas se bloquean.
[ ] Las transiciones utilizan revisión esperada.
[ ] El estado y el History se persisten atómicamente.
[ ] Existe Transactional Outbox.
[ ] Los Commands tienen ID.
[ ] Los Commands se autentican.
[ ] Los Commands se autorizan.
[ ] Command y Event están diferenciados.
[ ] Los Events tienen ID único.
[ ] Los Events tienen schema versionado.
[ ] Los Events conservan Correlation ID.
[ ] Los Events conservan Causation ID.
[ ] Existe secuencia por Execution.
[ ] Los consumidores deduplican Events.
[ ] Se asume entrega at-least-once.
[ ] Las Signals están tipadas.
[ ] Las Signals se autentican.
[ ] Las Signals se autorizan.
[ ] Las Signals tempranas tienen política.
[ ] Las Signals tienen expiración cuando procede.
[ ] Los Timers son durables.
[ ] Los Timers son idempotentes.
[ ] Existe política para Timers perdidos.
[ ] La precisión temporal está declarada.
[ ] Toda espera tiene Wait Record.
[ ] Toda espera declara condición.
[ ] Toda espera declara timeout o excepción autorizada.
[ ] Las esperas no mantienen Workers.
[ ] Pause tiene semántica definida.
[ ] El comportamiento de timers durante Pause está definido.
[ ] Resume revalida contexto.
[ ] Suspension crea checkpoint seguro.
[ ] Cancel Request y Cancelled están diferenciados.
[ ] La propagación de cancelación está definida.
[ ] Existe periodo de gracia.
[ ] Forced Termination está gobernada.
[ ] Los resultados unknown se reconcilian.
[ ] Existe Stall Detector.
[ ] Waiting y Stalled están diferenciados.
[ ] Existe Reconciliation formal.
[ ] El progreso utiliza un profile.
[ ] La terminalización bloquea nuevo scheduling.
[ ] Existe Finalization Lock.
[ ] El Result se crea antes del evento terminal.
[ ] El Result cumple schema.
[ ] Los Artifacts finales se validan.
[ ] Los Results terminales son inmutables.
[ ] Los comandos administrativos peligrosos se auditan.
[ ] Los Quality Gates de lifecycle han pasado.
```

---

# Arquitectura final de la Parte V

```text
Command or External Event
        ↓
Authentication and Authorization
        ↓
State and Revision Validation
        ↓
Transition Guard Evaluation
        ↓
Transition Decision
        ↓
Atomic State Persistence
        ↓
History Append
        ↓
Outbox Event
        ↓
Consequences
        ├── Schedule Job
        ├── Create Timer
        ├── Enter Wait
        ├── Request Cancellation
        ├── Reconcile
        └── Finalize
        ↓
Durable New State
```

---

# Transición hacia la Parte VI

Esta quinta parte ha definido:

- State Machines;
- Execution States;
- Step Instance States;
- Step Run States;
- Job States;
- terminal y non-terminal states;
- State Transitions;
- Transition Definitions;
- Transition Guards;
- revision control;
- Transactional Outbox;
- Commands;
- Command Handling;
- Events;
- Event Envelopes;
- Event Ordering;
- secuencias;
- Event Deduplication;
- delivery semantics;
- Inbox Pattern;
- Lifecycle Events;
- Signals;
- Signal Routing;
- Signal Buffering;
- Signal Security;
- Timers;
- durable timers;
- missed timer policies;
- Wait Records;
- Pause;
- Resume;
- Suspension;
- Cancellation;
- Cooperative Cancellation;
- Forced Termination;
- deadlines;
- timeouts;
- Blocking;
- Stall Detection;
- Reconciliation;
- State Projections;
- Progress Calculation;
- Step Terminalization;
- Execution Finalization;
- Execution Results;
- Lifecycle Policies;
- seguridad;
- observabilidad;
- diagnósticos;
- Quality Gates;
- casos de uso;
- antipatrones;
- reglas de conformidad.

La Parte VI desarrollará:

- Concurrency Model;
- Parallel Execution;
- Distributed Coordination;
- Worker Concurrency;
- Resource Isolation;
- Mutual Exclusion;
- Execution Locks;
- Resource Locks;
- Semaphores;
- Quotas;
- Rate Limits;
- Critical Sections;
- Optimistic Concurrency;
- Pessimistic Concurrency;
- Leader Election;
- Scheduler Coordination;
- Distributed Leases;
- Fencing Tokens;
- Split-Brain Prevention;
- Exactly-Once Effects by Idempotency;
- Partition Handling;
- Multi-region Execution;
- Data Locality;
- Backpressure avanzado;
- Load Shedding;
- Autoscaling Signals;
- Distributed Execution Quality Gates.

---

# Conclusión

La gestión de estados constituye la memoria operativa del Orquestador de Ejecución.

Su ciclo puede resumirse así:

```text
Recibir intención
        ↓
Validar transición
        ↓
Persistir estado
        ↓
Registrar historial
        ↓
Publicar evento
        ↓
Ejecutar consecuencias
        ↓
Esperar, continuar o finalizar
```

Las State Machines definen qué estados son válidos.

Las Transition Guards impiden cambios incoherentes.

Las revisiones protegen frente a concurrencia.

Los Commands expresan intenciones.

Los Events registran hechos.

Las Signals aportan inputs asíncronos.

Los Timers representan decisiones temporales durables.

Los Wait Records permiten esperar sin consumir Workers.

Pause y Suspension detienen de forma gobernada.

Resume revalida el contexto antes de continuar.

Cancellation coordina la detención y posible compensación.

Los estados `unknown` evitan reintentos peligrosos.

Stall Detection identifica procesos sin progreso.

Reconciliation repara divergencias.

La terminalización construye un Result inmutable.

Una Execution correctamente gobernada deberá poder responder:

```text
¿En qué estado se encuentra?

¿Cómo llegó a ese estado?

¿Qué transición lo produjo?

¿Qué comando o evento la causó?

¿Qué revisión posee?

¿Qué Signals ha recibido?

¿Qué Timers están pendientes?

¿Por qué está esperando?

¿Puede pausarse?

¿Puede reanudarse?

¿Existe una cancelación activa?

¿Qué Jobs siguen ejecutándose?

¿Está bloqueada o simplemente esperando?

¿Necesita reconciliación?

¿Qué estado terminal alcanzó?

¿Qué resultado produjo?
```

Con esta quinta parte queda formalizado el ciclo de vida durable, auditable y distribuido de Executions, Steps, Runs y Jobs en NovaCoquinaria.

La siguiente parte definirá cómo múltiples Scheduler Nodes, Workers y Executions concurrentes colaboran de forma segura mediante locks, leases, fencing tokens, quotas, aislamiento y coordinación distribuida.

---

# Parte VI — Modelo de Concurrencia, Coordinación Distribuida, Locks, Leases, Quotas, Resource Isolation y Consistencia

---

# Introducción

Hasta este punto se ha definido:

- Workflow Engine
- Execution Engine
- Scheduler
- State Machines
- Event System
- Worker Pools
- Dispatch
- Retry
- Signals
- Timers
- Cancellation

Sin embargo, todavía queda un problema fundamental:

> ¿Cómo garantizar que cientos o miles de Workers, múltiples Scheduler Nodes y miles de Executions concurrentes trabajen simultáneamente sin corromper el estado del sistema?

El Scheduler debe soportar escenarios como:

- dos Scheduler intentando despachar el mismo Job;
- varios Workers intentando reservar el mismo recurso;
- múltiples Executions actualizando un mismo índice;
- Activities que consumen recursos exclusivos;
- reintentos concurrentes;
- caída de un Scheduler durante una asignación;
- split-brain;
- pérdida de conectividad entre nodos.

Para ello NovaCoquinaria define un **Concurrency Model** explícito basado en:

- aislamiento;
- leases;
- fencing tokens;
- locks;
- optimistic concurrency;
- quotas;
- semáforos;
- coordinación distribuida;
- backpressure.

---

# Objetivos

Esta parte persigue:

- definir el modelo de concurrencia;
- establecer aislamiento entre Executions;
- formalizar Resource Locks;
- definir Execution Locks;
- establecer Distributed Leases;
- formalizar Fencing Tokens;
- definir Distributed Coordination;
- establecer Scheduler Coordination;
- definir Worker Coordination;
- formalizar Optimistic Concurrency;
- definir Pessimistic Concurrency;
- establecer Resource Isolation;
- definir Critical Sections;
- formalizar Semaphores;
- establecer Resource Quotas;
- definir Global Quotas;
- definir Tenant Quotas;
- establecer Rate Limits;
- formalizar Admission Limits;
- definir Load Shedding;
- establecer Leader Election;
- prevenir Split-Brain;
- definir Partition Handling;
- formalizar Consistency Model;
- establecer Idempotent Effects;
- definir Multi-region Coordination;
- establecer Data Locality;
- formalizar Concurrency Diagnostics;
- definir métricas;
- establecer Quality Gates.

---

# Principios

Todo mecanismo concurrente deberá cumplir:

- determinismo;
- aislamiento;
- reproducibilidad;
- recuperación automática;
- no duplicación de side effects;
- idempotencia;
- tolerancia a fallos;
- observabilidad;
- escalabilidad horizontal.

---

# Arquitectura conceptual

```text
                 Scheduler Cluster
        ┌──────────────┬──────────────┐
        ▼              ▼              ▼
 Scheduler A     Scheduler B     Scheduler C
        │              │              │
        └──────────────┼──────────────┘
                       ▼
            Distributed Coordination
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
 Resource Locks   Execution Locks   Leases
      │                │                │
      └────────────────┼────────────────┘
                       ▼
             Worker Pools Cluster
                       │
                       ▼
             Parallel Job Execution
```

---

# Modelo de concurrencia

NovaCoquinaria utiliza una combinación de:

```text
Optimistic Concurrency
+
Distributed Leases
+
Fine-Grained Locks
+
Idempotent Execution
+
Fencing Tokens
```

No dependerá exclusivamente de locks globales.

---

# Niveles de aislamiento

La concurrencia se gestiona en varios niveles:

```text
Workflow
Execution
Stage
Step
Step Run
Job
Worker
Artifact
External Resource
```

Cada nivel puede utilizar mecanismos distintos.

---

# Optimistic Concurrency

Será el mecanismo preferido para:

- State Store;
- Execution State;
- Step State;
- Job State;
- Metadata.

---

# Revision Control

Cada Aggregate deberá poseer:

```yaml
revision: 42
```

Toda actualización deberá comprobar:

```text
expected_revision == current_revision
```

---

# Conflict Detection

Si la revisión no coincide:

```text
EXECUTION_STATE_REVISION_CONFLICT
```

---

# Retry Strategy

El Scheduler podrá:

- recargar estado;
- volver a evaluar;
- reintentar;
- abortar.

---

# Ventajas

- alta escalabilidad;
- mínimo bloqueo;
- menor contención;
- mayor throughput.

---

# Pessimistic Concurrency

Solo deberá utilizarse cuando:

- exista un recurso exclusivo;
- no pueda tolerarse doble acceso;
- el coste del conflicto sea elevado.

---

# Casos

- escritura exclusiva;
- publicación final;
- promoción de snapshots;
- cambio de alias global;
- operaciones destructivas.

---

# Execution Lock

Protege una Execution concreta.

Formato recomendado:

```text
EXECUTION-LOCK-XXXXXX
```

---

# Contrato

```yaml
execution_lock:
  id: EXECUTION-LOCK-000041

  execution:
    id: EXEC-000041

  owner:
    id: SCHEDULER-A

  acquired_at: ...

  expires_at: ...
```

---

# Objetivo

Evitar que dos Scheduler modifiquen simultáneamente la misma Execution.

---

# Lock Scope

Puede proteger:

- Execution;
- Stage;
- Step;
- Resource.

---

# Lock Duration

Siempre deberá ser limitada.

Nunca indefinida.

---

# Lock Renewal

Si continúa siendo necesario:

```text
Acquire
↓
Renew
↓
Renew
↓
Release
```

---

# Resource Lock

Protege un recurso compartido.

Ejemplos:

```text
Knowledge Index
Snapshot
Graph Store
Repository
Artifact
LLM GPU
```

---

# Resource Lock Contract

```yaml
resource_lock:
  id: RESOURCE-LOCK-INDEX

  resource:
    id: KNOWLEDGE-INDEX

  owner:
    execution: EXEC-000041

  expires_at: ...
```

---

# Granularidad

Se recomienda:

- locks pequeños;
- corta duración;
- alta especificidad.

Evitar:

```text
GLOBAL LOCK
```

---

# Critical Section

Representa un bloque donde solo un actor puede modificar un recurso.

---

# Ejemplo

```text
Promote Snapshot
```

Solo una Execution podrá realizarlo.

---

# Critical Section Contract

```yaml
critical_section:
  id: SNAPSHOT-PROMOTION

  locking:
    resource_lock
```

---

# Distributed Lease

Una Lease concede derecho temporal a ejecutar una acción.

Formato recomendado:

```text
LEASE-XXXXXX
```

---

# Lease Contract

```yaml
lease:
  id: LEASE-000041

  holder:
    worker: WORKER-001

  resource:
    job: JOB-000041

  expires_at: ...

  renewable: true
```

---

# Lease vs Lock

```text
Lock
=
exclusividad
```

```text
Lease
=
permiso temporal
```

---

# Lease Expiration

Cuando expira:

- puede renovarse;
- puede reasignarse;
- puede reconciliarse.

---

# Lease Renewal

```text
Acquire
↓
Heartbeat
↓
Renew
↓
Renew
↓
Release
```

---

# Lease Failure

Si expira:

```text
JOB_ORPHANED
```

---

# Fencing Token

Cada Lease deberá poseer un número creciente.

---

# Objetivo

Evitar que un Worker antiguo siga modificando recursos.

---

# Ejemplo

```text
Lease 15

↓

Lease expira

↓

Lease 16

↓

Worker antiguo intenta escribir

↓

Token 15 rechazado
```

---

# Contract

```yaml
fencing_token:
  value: 16
```

---

# Regla

Todo recurso protegido deberá validar:

```text
incoming_token >= current_token
```

---

# Worker Ownership

Solo el propietario de una Lease válida podrá ejecutar.

---

# Ownership Transfer

Cuando una Lease cambia:

```text
Worker A

↓

Lease Expired

↓

Worker B

↓

Nuevo Fencing Token
```

---

# Leader Election

Algunas tareas requieren un líder.

Ejemplos:

- limpieza global;
- mantenimiento;
- reconciliación.

---

# Leader Contract

```yaml
leader:
  scheduler: SCHEDULER-A

  lease:
    LEADER-LEASE-001
```

---

# Leader Failure

Otro Scheduler asumirá liderazgo.

---

# Leader Election Properties

- automática;
- segura;
- observable;
- con Lease.

---

# Split-Brain

Puede ocurrir cuando dos líderes creen ser válidos.

---

# Prevención

Mediante:

- leases;
- fencing tokens;
- quorum;
- majority.

---

# No confiar en relojes locales

---

# Scheduler Coordination

Todos los Scheduler compartirán:

- Ready Queue;
- State Store;
- Worker Registry;
- Coordination Store.

---

# Scheduler Independence

No deberán compartir memoria RAM.

---

# Coordination Store

Podrá implementarse mediante:

- etcd;
- ZooKeeper;
- Consul;
- PostgreSQL;
- FoundationDB;
- otros sistemas equivalentes.

El contrato no dependerá de una tecnología concreta.

---

# Scheduler Responsibilities

Cada Scheduler podrá:

- adquirir Jobs;
- renovar leases;
- reconciliar;
- emitir eventos.

---

# Scheduler Collision

Dos Scheduler podrán intentar:

```text
Dispatch JOB-41
```

Solo uno obtendrá la Lease.

---

# Worker Coordination

Los Workers no deberán comunicarse directamente entre sí salvo necesidad explícita.

Toda coordinación deberá pasar por:

- Scheduler;
- State Store;
- Event Bus.

---

# Parallel Execution

NovaCoquinaria deberá permitir miles de Steps ejecutándose simultáneamente.

---

# Parallel Constraints

La concurrencia estará limitada por:

- DAG;
- capacidades;
- cuotas;
- recursos;
- políticas.

---

# Parallel Groups

El Planner ya habrá calculado:

```text
Level 1

Level 2

Level 3
```

El Scheduler utilizará dichos grupos.

---

# Maximum Parallelism

Podrá configurarse:

```yaml
max_parallelism: 128
```

---

# Dynamic Parallelism

Algunas ramas podrán generarse dinámicamente.

Ejemplo:

```text
Map Step
```

---

# Concurrency Limit

Cada Activity podrá declarar:

```yaml
maximum_parallel_runs: 5
```

---

# Semaphore

Un Semaphore limita concurrencia.

Formato recomendado:

```text
SEMAPHORE-XXXXXX
```

---

# Semaphore Contract

```yaml
semaphore:
  id: EMBEDDING-GPU

  capacity: 4

  acquired: 3
```

---

# Acquire

Si existe capacidad:

```text
Acquire

↓

Execute

↓

Release
```

---

# Capacity Exhausted

El Step permanecerá:

```text
waiting_capacity
```

---

# Weighted Semaphore

Cada Activity podrá consumir más de una unidad.

```yaml
required_units: 2
```

---

# Resource Classes

```text
cpu

gpu

memory

network

storage

external_api
```

---

# Resource Reservation

Antes del Dispatch podrán reservarse recursos.

---

# Reservation Contract

```yaml
reservation:
  resource: GPU

  units: 2

  expires_at: ...
```

---

# Reservation Timeout

Si no comienza ejecución:

```text
Reservation Expired
```

---

# Resource Isolation

Cada Tenant deberá disponer de aislamiento configurable.

---

# Isolation Levels

```text
shared

soft

hard

exclusive
```

---

# Hard Isolation

Un Tenant nunca utilizará recursos reservados a otro.

---

# Exclusive Isolation

Solo una Execution podrá utilizar el recurso.

---

# Tenant Quotas

Cada Tenant podrá tener límites propios.

```yaml
tenant_quota:

  executions: 500

  workers: 40

  gpu_hours: 200
```

---

# Global Quotas

También existirán límites globales.

---

# Quota Evaluation

Antes de admitir un Workflow:

```text
Admission Control

↓

Quota Check

↓

Accept / Reject
```

---

# Quota Exceeded

```text
TENANT_QUOTA_EXCEEDED
```

---

# Dynamic Quotas

Podrán modificarse sin reiniciar el sistema.

---

# Rate Limiting

Protege recursos frente a abuso.

---

# Scope

Puede aplicarse sobre:

- Tenant;
- Workflow;
- Activity;
- API;
- Scheduler;
- Resource.

---

# Algorithms

Ejemplos:

- Token Bucket;
- Leaky Bucket;
- Sliding Window.

El contrato no obliga a uno concreto.

---

# Rate Limit Contract

```yaml
rate_limit:
  requests: 200

  every: PT1M
```

---

# Load Shedding

Si el sistema alcanza saturación:

- rechazar trabajo;
- degradar prioridad;
- retrasar Jobs.

---

# Admission Backoff

Podrá responder:

```text
Retry Later
```

---

# Queue Backpressure

Cuando una cola crece:

- disminuir Admission;
- reducir paralelismo;
- activar autoscaling.

---

# Execution Backpressure

Una Execution podrá ralentizar ramas secundarias.

---

# Adaptive Scheduling

El Scheduler podrá modificar prioridades según:

- carga;
- latencia;
- deadlines;
- critical path.

---

# Deadlock

Los Locks deberán diseñarse para evitar interbloqueos.

---

# Reglas

- orden fijo;
- timeout;
- locks pequeños;
- no anidamiento innecesario.

---

# Deadlock Detection

El Scheduler podrá detectar ciclos.

---

# Deadlock Recovery

Opciones:

- liberar Lease;
- cancelar;
- retry;
- intervención manual.

---

# Livelock

También deberá evitarse.

---

# Starvation

Toda Execution deberá progresar.

---

# Fairness

Los recursos deberán repartirse justamente.

---

# Locality

Siempre que sea posible:

```text
Mover el cálculo al dato
```

en lugar de mover grandes volúmenes de datos.

---

# Data Affinity

Los Workers podrán anunciar:

```yaml
local_data:
- embeddings
- graph
```

---

# Affinity Scheduling

El Scheduler podrá favorecer Workers con datos locales.

---

# Multi-region

NovaCoquinaria podrá ejecutarse en varias regiones.

---

# Objetivos

- resiliencia;
- latencia;
- soberanía del dato.

---

# Cross-region Coordination

Se minimizarán las operaciones síncronas.

---

# Consistency Model

Se adopta:

```text
Strong Consistency
```

para:

- estado;
- leases;
- locks.

```text
Eventual Consistency
```

para:

- proyecciones;
- métricas;
- dashboards.

---

# Side Effects

Los side effects deberán ser:

- idempotentes;
- identificables;
- reconciliables.

---

# Idempotency Key

```yaml
idempotency_key:
EXEC-41:STEP-BUILD-INDEX
```

---

# Exactly Once Effects

No se garantiza exactly-once de transporte.

Sí se persigue:

```text
Exactly Once Observable Effects
```

mediante:

- idempotencia;
- deduplicación;
- reconciliación.

---

# Network Partition

Si existe partición:

- preservar consistencia;
- evitar doble liderazgo;
- evitar doble ejecución.

---

# Partition Policies

```text
stop

degraded

read_only

quorum
```

---

# Recomendación

Utilizar:

```text
quorum
```

para componentes críticos.

---

# Autoscaling Signals

El Scheduler podrá emitir:

- queue length;
- waiting jobs;
- lease pressure;
- CPU;
- GPU;
- latency.

---

# Autoscaling Decisions

Ejemplo:

```text
Queue > Threshold

↓

Crear Workers
```

---

# Observabilidad

Se registrarán:

- locks;
- leases;
- conflictos;
- revisiones;
- starvation;
- deadlocks;
- fairness;
- throughput.

---

# Métricas

- Lock Wait Time
- Lease Renewals
- Lease Expiration
- Scheduler Conflicts
- Parallel Jobs
- Queue Length
- Resource Utilization
- Semaphore Usage
- Quota Consumption
- Fencing Rejects
- Leader Changes
- Partition Events

---

# Diagnósticos

Ejemplos:

```text
LEASE_EXPIRED

LEASE_RENEW_FAILED

LOCK_TIMEOUT

LOCK_CONFLICT

RESOURCE_BUSY

FENCING_TOKEN_REJECTED

QUOTA_EXCEEDED

RATE_LIMIT_EXCEEDED

DEADLOCK_DETECTED

STARVATION_DETECTED

SPLIT_BRAIN_PREVENTED

LEADER_LOST

PARTITION_DETECTED
```

---

# Quality Gate

```yaml
quality_gate:
  id: QG-CONCURRENCY-0001

  criteria:

    all:

      - optimistic_concurrency_enabled == true

      - revision_control_enabled == true

      - leases_have_expiration == true

      - fencing_tokens_enabled == true

      - locks_have_timeout == true

      - quotas_defined == true

      - semaphores_declared == true

      - rate_limits_defined == true

      - leader_election_defined == true

      - split_brain_protection == true

      - idempotency_keys_defined == true

      - deadlock_prevention_defined == true
```

---

# Casos de uso

## Caso 1

Dos Scheduler intentan despachar el mismo Job.

La Lease solo permite uno.

---

## Caso 2

Un Worker pierde conectividad.

La Lease expira.

Otro Worker continúa.

---

## Caso 3

Un Worker antiguo intenta escribir.

El Fencing Token lo rechaza.

---

## Caso 4

Una GPU admite cuatro trabajos.

El Semaphore limita concurrencia.

---

## Caso 5

Un Tenant supera cuota.

Admission Control rechaza nuevas Executions.

---

## Caso 6

Un índice solo admite una promoción.

Resource Lock garantiza exclusividad.

---

## Caso 7

Caída del líder.

Otro Scheduler adquiere la Leader Lease.

---

## Caso 8

Existe partición de red.

El nodo sin quorum deja de despachar Jobs.

---

# Antipatrones

No deberán utilizarse:

- locks globales permanentes;
- leases sin expiración;
- workers escribiendo sin fencing;
- revisiones ignoradas;
- semáforos infinitos;
- recursos exclusivos sin lock;
- Scheduler coordinándose mediante memoria;
- exactly-once asumido sin idempotencia;
- leader fijo;
- relojes locales como fuente de verdad.

---

# Reglas de conformidad

Será conforme cuando:

- toda actualización utilice control de revisión;
- las Leases sean temporales;
- existan Fencing Tokens;
- los Locks tengan timeout;
- exista Leader Election;
- exista protección frente a Split-Brain;
- los recursos críticos utilicen aislamiento;
- existan Quotas;
- existan Rate Limits;
- exista Backpressure;
- exista prevención de Deadlocks;
- los Side Effects sean idempotentes;
- exista Coordinación Distribuida.

---

# Arquitectura final

```text
Executions
      │
      ▼
Scheduler Cluster
      │
      ▼
Distributed Coordination
      │
 ┌────┼────┐
 ▼    ▼    ▼
Locks Leases Fencing
 │     │      │
 ▼     ▼      ▼
Worker Pools
      │
      ▼
Parallel Execution
      │
      ▼
Idempotent Effects
      │
      ▼
Consistent State
```

---

# Transición hacia la Parte VII

La siguiente parte desarrollará la **Arquitectura Operacional del Scheduler**, incluyendo:

- Persistence Layer.
- State Store.
- Event Store.
- History Store.
- Queue Store.
- Outbox e Inbox.
- Snapshots.
- Checkpoints.
- Recovery Engine.
- Disaster Recovery.
- Backup y Restore.
- Garbage Collection.
- Archivado.
- Retención.
- Compaction.
- Rebuild del estado.
- Auditoría avanzada.
- Observabilidad completa.
- Alta disponibilidad.
- Operación en producción.

---

# Parte VII — Arquitectura Operacional: Persistencia, Recovery Engine, Alta Disponibilidad, Disaster Recovery, Retención, Compaction y Operación en Producción

---

# Introducción

Las partes anteriores han definido:

- el modelo formal de Execution;
- Workflows, Pipelines y DAGs;
- el Scheduler Runtime;
- Worker Pools y colas;
- máquinas de estados;
- eventos, señales y timers;
- cancelación y reconciliación;
- concurrencia distribuida;
- Locks;
- Leases;
- Fencing Tokens;
- Quotas;
- Rate Limits;
- aislamiento de recursos.

Sin embargo, una plataforma de orquestación no puede considerarse durable únicamente porque sus componentes conozcan qué deben ejecutar.

Debe ser capaz de conservar y recuperar de forma segura:

- definiciones;
- ejecuciones;
- estados;
- historiales;
- Jobs;
- leases;
- timers;
- señales;
- decisiones;
- checkpoints;
- artefactos;
- eventos;
- índices operativos;
- registros de auditoría.

También deberá sobrevivir a:

- reinicios;
- fallos de procesos;
- caída de Workers;
- caída de Scheduler Nodes;
- pérdida parcial de infraestructura;
- despliegues;
- corrupción lógica;
- errores operativos;
- indisponibilidad regional;
- restauraciones desde backup.

Esta responsabilidad corresponde a la **Arquitectura Operacional del Orquestador de Ejecución**.

Conceptualmente:

```text
Execution Activity
        ↓
Durable State Persistence
        ↓
History and Event Recording
        ↓
Checkpointing
        ↓
Snapshots and Backups
        ↓
Recovery and Reconciliation
        ↓
Archival and Retention
        ↓
Operational Observability
        ↓
Production Governance
```

La persistencia no deberá entenderse como una única base de datos en la que se almacena todo indiscriminadamente.

NovaCoquinaria deberá separar responsabilidades entre:

- State Store;
- History Store;
- Event Store;
- Queue Store;
- Timer Store;
- Artifact Store;
- Audit Store;
- Projection Store;
- Backup Store.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir la arquitectura operacional;
- formalizar el Persistence Layer;
- definir State Store;
- definir History Store;
- establecer Event Store;
- formalizar Queue Store;
- definir Timer Store;
- establecer Signal Store;
- definir Checkpoint Store;
- formalizar Artifact Store;
- definir Audit Store;
- establecer Projection Stores;
- formalizar Outbox e Inbox;
- definir transacciones;
- establecer snapshots operativos;
- definir compaction;
- formalizar archivado;
- establecer retención;
- definir Garbage Collection;
- formalizar Recovery Engine;
- establecer State Reconstruction;
- definir Job Recovery;
- formalizar Worker Recovery;
- establecer Scheduler Recovery;
- definir Execution Recovery;
- formalizar reconciliación;
- definir Backup;
- establecer Restore;
- formalizar Disaster Recovery;
- definir RPO y RTO;
- establecer alta disponibilidad;
- definir failover;
- formalizar rolling upgrades;
- establecer schema migrations;
- definir capacity planning;
- formalizar observabilidad operacional;
- establecer alertas;
- definir runbooks;
- establecer Quality Gates operacionales;
- preparar la operación en producción.

---

# Principios operacionales

Toda implementación deberá respetar los siguientes principios.

---

## Durabilidad

Todo estado confirmado deberá sobrevivir a reinicios y fallos de proceso.

---

## Separación de almacenes

No todos los datos deberán utilizar el mismo patrón de persistencia.

---

## Fuente canónica explícita

Cada tipo de dato deberá disponer de una fuente de verdad definida.

---

## Persistencia antes de exposición

Un cambio no deberá considerarse confirmado hasta que se haya persistido.

---

## Historial inmutable

Los hechos históricos no deberán reescribirse.

---

## Reconstrucción posible

El estado deberá poder reconstruirse a partir de:

- historial;
- snapshots;
- checkpoints;
- eventos;
- artefactos.

---

## Transacciones limitadas

Las transacciones deberán mantenerse pequeñas y localizadas.

---

## No transacciones distribuidas globales

La coherencia entre componentes deberá obtenerse mediante:

- Outbox;
- Inbox;
- idempotencia;
- reconciliación;
- Sagas.

---

## Recuperación automatizada

Los fallos previsibles deberán disponer de mecanismos automáticos de recuperación.

---

## Restauración verificable

Un backup no será válido si no puede restaurarse y comprobarse.

---

## Retención gobernada

Los datos no deberán conservarse indefinidamente sin política.

---

## Eliminación segura

La limpieza deberá respetar:

- lineage;
- auditoría;
- referencias;
- retención;
- seguridad.

---

## Alta disponibilidad sin doble ejecución

El failover no deberá generar:

- dos líderes válidos;
- dos despachos;
- dos efectos observables.

---

## Operación observable

Toda degradación deberá ser detectable.

---

## Cambios reversibles

Los despliegues y migraciones deberán disponer de rollback o roll-forward gobernado.

---

## No dependencia de memoria local

El estado operativo crítico deberá persistirse externamente.

---

## Backups cifrados

Los backups deberán conservar las mismas garantías de seguridad que los datos activos.

---

## Recovery probado

Los procesos de recuperación deberán ejercitarse regularmente.

---

# Arquitectura conceptual

```text
┌───────────────────────────────────────────────┐
│              Orchestrator Runtime             │
│                                               │
│ Coordinator · Scheduler · Workers · APIs      │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Persistence Layer               │
│                                               │
│ State · History · Queue · Timers · Signals    │
└──────────────────────┬────────────────────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Outbox        Artifacts      Audit
          │            │            │
          └────────────┼────────────┘
                       ▼
┌───────────────────────────────────────────────┐
│               Recovery Engine                 │
│                                               │
│ Replay · Reconcile · Resume · Reassign        │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│      Backup, Archive and Disaster Recovery    │
│                                               │
│ Snapshots · Restore · Failover · Retention    │
└───────────────────────────────────────────────┘
```

---

# Persistence Layer

El **Persistence Layer** representa el conjunto de almacenes y contratos responsables de mantener el estado durable del Orquestador.

Formato recomendado:

```text
EXEC-PERSISTENCE-LAYER-XXXXXX
```

---

# Responsabilidades

- persistir Aggregates;
- mantener revisiones;
- conservar historial;
- almacenar Jobs;
- mantener timers;
- persistir señales;
- almacenar checkpoints;
- preservar referencias a Artifacts;
- mantener Outbox e Inbox;
- soportar consultas operativas;
- permitir recuperación;
- aplicar retención.

---

# Contrato

```yaml
execution_persistence_layer:
  id: EXEC-PERSISTENCE-LAYER-PRIMARY

  version: 1.0.0

  stores:
    state: EXEC-STATE-STORE-PRIMARY
    history: EXEC-HISTORY-STORE-PRIMARY
    queue: EXEC-QUEUE-STORE-PRIMARY
    timer: EXEC-TIMER-STORE-PRIMARY
    signal: EXEC-SIGNAL-STORE-PRIMARY
    checkpoint: EXEC-CHECKPOINT-STORE-PRIMARY
    artifact: EXEC-ARTIFACT-STORE-PRIMARY
    audit: EXEC-AUDIT-STORE-PRIMARY

  transaction_profile:
    id: EXEC-TRANSACTION-PROFILE-STANDARD

  status: active
```

---

# Store Responsibilities Matrix

| Store | Responsabilidad principal |
|---|---|
| State Store | Estado actual de Aggregates |
| History Store | Secuencia histórica append-only |
| Event Store | Eventos durables y publicables |
| Queue Store | Jobs preparados, retrasados y reintentos |
| Timer Store | Timers durables |
| Signal Store | Señales pendientes y consumidas |
| Checkpoint Store | Puntos de recuperación |
| Artifact Store | Resultados voluminosos |
| Audit Store | Evidencia de acciones y overrides |
| Projection Store | Vistas derivadas para consulta |

---

# State Store

El **State Store** mantiene la representación actual de:

- Executions;
- Step Instances;
- Step Runs;
- Jobs;
- Wait Records;
- Leases;
- Locks;
- Human Tasks;
- Child Execution Links.

Formato recomendado:

```text
EXEC-STATE-STORE-XXXXXX
```

---

# Contrato

```yaml
state_store:
  id: EXEC-STATE-STORE-PRIMARY

  consistency: strong

  capabilities:
    transactions: true
    optimistic_concurrency: true
    compare_and_swap: true
    secondary_indexes: true

  durability:
    mode: synchronous_commit

  status: active
```

---

# Requisitos

- escritura durable;
- control de revisión;
- lectura consistente;
- índices operativos;
- transacciones cortas;
- recuperación puntual;
- aislamiento multi-tenant.

---

# Aggregate Record

```yaml
aggregate_record:
  aggregate:
    type: execution
    id: EXEC-000041

  state:
    status: running
    revision: 18

  state_machine:
    id: STATE-MACHINE-EXECUTION
    version: 1.0.0

  updated_at: 2026-08-02T20:02:00Z
```

---

# Aggregate Boundary

Cada Aggregate deberá definir qué cambios necesitan consistencia transaccional.

Ejemplos:

```text
Execution State
+
History Append
+
Outbox Record
```

Podrán persistirse en una única transacción local.

---

# No Aggregate excesivamente grande

Una Execution no deberá almacenarse como un único documento gigantesco con:

- todo el historial;
- todos los Jobs;
- todos los Artifacts;
- todos los eventos.

---

# Current State vs History

El State Store mantiene:

```text
qué estado existe ahora
```

El History Store conserva:

```text
cómo se llegó a ese estado
```

---

# State Store Indexes

Índices iniciales recomendados:

```text
execution_id
tenant_id
workflow_id
state
created_at
updated_at
correlation_id
business_key
deadline
```

---

# Step Indexes

```text
execution_id
step_definition_id
state
current_run_id
updated_at
```

---

# Job Indexes

```text
state
queue
priority
tenant
available_at
deadline
lease_expiration
worker_id
```

---

# State Store Consistency

Para cambios críticos deberá utilizarse:

```text
strong consistency
```

No deberá utilizarse una réplica retrasada para decidir:

- dispatch;
- terminalización;
- lock ownership;
- lease validity;
- idempotency.

---

# History Store

El **History Store** conserva una secuencia append-only de hechos de cada Execution.

Formato recomendado:

```text
EXEC-HISTORY-STORE-XXXXXX
```

---

# Contrato

```yaml
history_store:
  id: EXEC-HISTORY-STORE-PRIMARY

  mode: append_only

  sequence_scope: execution

  integrity:
    checksums: true
    gap_detection: true

  retention:
    policy: EXEC-HISTORY-RETENTION-STANDARD

  status: active
```

---

# Requisitos

- append-only;
- secuencia monotónica;
- detección de gaps;
- checksum;
- acceso por rango;
- replay;
- archivado;
- compaction controlada.

---

# History Partitioning

Podrá particionarse por:

- tenant;
- fecha;
- Execution ID;
- workflow;
- entorno.

---

# Orden recomendado

El orden canónico deberá conservarse por:

```text
execution_id + sequence
```

---

# History Integrity Chain

Podrá utilizarse una cadena de hashes.

```yaml
history_integrity:
  sequence: 142
  previous_hash: ...
  current_hash: ...
```

---

# Objetivo

Detectar:

- alteración;
- pérdida;
- reordenación;
- corrupción.

---

# History Gap

Si faltan secuencias:

```text
EXECUTION_HISTORY_GAP
```

La Execution no deberá reanudarse automáticamente hasta resolver la inconsistencia.

---

# History Snapshot

Podrá almacenarse un snapshot de estado para acelerar replay.

---

# Snapshot Rule

Un snapshot no sustituye al historial.

Representa:

```text
estado reconstruido hasta la secuencia N
```

---

# History Snapshot Contract

```yaml
execution_history_snapshot:
  id: EXEC-HISTORY-SNAPSHOT-000041

  execution:
    id: EXEC-000041

  through_sequence: 1000

  state_reference:
    id: EXEC-STATE-SNAPSHOT-000041

  checksum: ...

  created_at: 2026-08-02T21:00:00Z
```

---

# Event Store

El **Event Store** conservará eventos publicables o de integración cuando se necesite una persistencia específica.

Formato recomendado:

```text
EXEC-EVENT-STORE-XXXXXX
```

---

# Diferencia con History Store

El History Store representa el historial interno del Aggregate.

El Event Store podrá representar:

- eventos de integración;
- eventos de dominio;
- lifecycle events;
- streams consumibles.

---

# No duplicación no gobernada

Un mismo hecho podrá tener:

- History Entry interna;
- Integration Event externa;

pero la relación deberá ser explícita.

---

# Event Record

```yaml
event_store_record:
  event:
    id: EXEC-EVENT-000041

  aggregate:
    type: execution
    id: EXEC-000041

  stream:
    id: EXECUTION-LIFECYCLE

  sequence:
    aggregate: 142
    stream: 840001

  publication:
    status: published
```

---

# Queue Store

El **Queue Store** mantiene Jobs pendientes de scheduling.

Formato recomendado:

```text
EXEC-QUEUE-STORE-XXXXXX
```

---

# Requisitos

- durabilidad;
- leasing atómico;
- prioridades;
- delayed availability;
- retries;
- multi-tenant;
- deduplicación;
- Dead Letter Queue;
- búsqueda por lease expirado.

---

# Queue Record

```yaml
queue_record:
  job:
    id: JOB-000041

  queue:
    id: QUEUE-INDEXING-HIGH

  state: ready

  priority: high
  available_at: 2026-08-02T20:02:00Z
  deadline: 2026-08-02T20:12:00Z

  tenant: TENANT-0001

  revision: 5
```

---

# Atomic Job Claim

El paso:

```text
ready
→
leased
```

deberá ser atómico.

---

# Claim Preconditions

- Job en estado compatible;
- `available_at <= now`;
- lease inexistente o expirada;
- quota disponible;
- Worker compatible;
- revisión esperada.

---

# Claim Conflict

Solo un Scheduler deberá obtener éxito.

---

# Delayed Queue

Los Jobs retrasados podrán permanecer en el mismo almacén con:

```text
available_at > current_time
```

o utilizar una estructura separada.

---

# Dead Letter Queue

Deberá conservar:

- Job;
- error final;
- intentos;
- historial;
- acciones permitidas;
- retención.

---

# Dead Letter Record

```yaml
dead_letter_record:
  id: DLQ-000041

  job:
    id: JOB-000041

  reason:
    code: MAXIMUM_ATTEMPTS_EXCEEDED

  attempts: 5

  resolution_options:
    - retry_manually
    - inspect
    - discard
    - create_recovery_execution
```

---

# Timer Store

El **Timer Store** mantiene timers durables y ordenados por vencimiento.

Formato recomendado:

```text
EXEC-TIMER-STORE-XXXXXX
```

---

# Requisitos

- durabilidad;
- búsqueda por `fire_at`;
- claim atómico;
- deduplicación de disparo;
- recuperación tras reinicio;
- precisión declarada;
- sharding temporal.

---

# Timer Record

```yaml
timer_record:
  timer:
    id: EXEC-TIMER-000041

  fire_at: 2026-08-02T20:10:00Z
  state: scheduled

  target:
    execution_id: EXEC-000041
    step_instance_id: STEP-INSTANCE-000041

  partition:
    bucket: 2026-08-02T20:10
```

---

# Timer Claim

Un Scheduler o Timer Worker deberá reclamar el timer antes de dispararlo.

---

# Duplicate Fire Prevention

El estado deberá evolucionar mediante:

```text
scheduled
→
claimed
→
fired
```

con control de revisión.

---

# Signal Store

El **Signal Store** conserva señales:

- pendientes;
- bufferizadas;
- aplicadas;
- expiradas;
- rechazadas.

Formato recomendado:

```text
EXEC-SIGNAL-STORE-XXXXXX
```

---

# Signal Record

```yaml
signal_store_record:
  signal:
    id: EXEC-SIGNAL-000041

  target:
    execution_id: EXEC-000041

  type: approval
  state: buffered

  expires_at: 2026-08-03T20:15:00Z

  deduplication_key: EXEC-SIGNAL-000041
```

---

# Signal Consumption

La aplicación de una señal deberá ser transaccional respecto a:

- Wait satisfaction;
- State Transition;
- Signal state;
- History;
- Outbox.

---

# Checkpoint Store

El **Checkpoint Store** conserva puntos de recuperación validados.

Formato recomendado:

```text
EXEC-CHECKPOINT-STORE-XXXXXX
```

---

# Requisitos

- inmutabilidad;
- checksum;
- versionado;
- compatibilidad;
- referencias a Artifacts;
- búsqueda por Execution;
- marcado de último checkpoint válido.

---

# Checkpoint Record

```yaml
checkpoint_store_record:
  checkpoint:
    id: EXEC-CHECKPOINT-000041

  execution:
    id: EXEC-000041

  state_revision: 18
  history_sequence: 142

  status: valid

  checksum: ...

  retention:
    policy: EXEC-CHECKPOINT-RETENTION-STANDARD
```

---

# Checkpoint Chain

Podrá conservarse:

- full checkpoint;
- incremental checkpoints.

---

# Full Checkpoint

Contiene todo el estado necesario.

---

# Incremental Checkpoint

Contiene cambios desde otro checkpoint.

---

# Recomendación inicial

Utilizar full checkpoints en límites relevantes hasta que el volumen justifique incrementalidad.

---

# Artifact Store

El **Artifact Store** mantiene outputs persistentes y voluminosos.

Formato recomendado:

```text
EXEC-ARTIFACT-STORE-XXXXXX
```

---

# Propiedades

- almacenamiento de objetos;
- inmutabilidad;
- checksum;
- versionado;
- cifrado;
- retención;
- lineage;
- tenant isolation.

---

# Artifact Classes

```text
ephemeral
intermediate
candidate
published
audit
recovery
archive
```

---

# Ephemeral Artifact

Puede eliminarse tras la ejecución o una ventana breve.

---

# Intermediate Artifact

Necesario para pasos posteriores o recuperación.

---

# Candidate Artifact

Puede promocionarse.

---

# Published Artifact

Forma parte de un resultado activo y tiene retención ampliada.

---

# Recovery Artifact

Se conserva para rollback o reconciliación.

---

# Artifact Promotion

No deberá copiarse necesariamente el contenido.

Podrá cambiar:

- status;
- retention;
- visibility;
- alias;
- metadata.

---

# Artifact Reference Integrity

Antes de reanudar o finalizar deberá comprobarse:

- existencia;
- checksum;
- tenant;
- clasificación;
- schema;
- lifecycle state.

---

# Audit Store

El **Audit Store** conserva acciones relevantes para:

- seguridad;
- compliance;
- operación;
- gobernanza.

Formato recomendado:

```text
EXEC-AUDIT-STORE-XXXXXX
```

---

# Audit Requirements

- append-only;
- actor;
- acción;
- target;
- resultado;
- justificación;
- timestamp;
- tenant;
- correlation;
- integrity protection.

---

# Audit Categories

```text
execution_control
security
policy
human_decision
override
compensation
recovery
migration
retention
data_access
administrative
```

---

# Audit Record

```yaml
audit_record:
  id: EXEC-AUDIT-000041

  category: administrative
  action: execution.force_fail

  actor:
    id: USER-ADMIN-0001
    type: user

  target:
    execution_id: EXEC-000041

  result: succeeded

  justification: Resultado externo no recuperable.

  occurred_at: 2026-08-02T20:30:00Z
```

---

# Projection Store

Las **Projections** permiten consultas rápidas sin cargar el historial completo.

---

# Ejemplos

- Executions activas;
- Jobs por estado;
- Workflows fallidos;
- queue depth;
- Human Tasks pendientes;
- costes por tenant;
- SLA dashboards.

---

# Projection Record

```yaml
execution_projection:
  execution_id: EXEC-000041
  state: running
  progress: 44
  active_steps: 2
  blocked_steps: 1
  last_sequence: 142
  updated_at: 2026-08-02T20:02:00Z
```

---

# Projection Lag

Toda proyección deberá declarar hasta qué secuencia está actualizada.

---

# No usar proyección retrasada para decisiones críticas

---

# Transaction Model

El Orquestador deberá definir límites transaccionales claros.

---

# Transacción de cambio de estado

Deberá incluir normalmente:

```text
Read Current Aggregate
↓
Validate Revision
↓
Persist New State
↓
Append History
↓
Create Outbox Record
↓
Commit
```

---

# No incluir llamadas externas dentro de transacciones

No deberán mantenerse bloqueos de base de datos mientras:

- se invoca un motor;
- se llama a un API;
- se espera un Worker;
- se genera un Artifact.

---

# Transaction Profile

Formato recomendado:

```text
EXEC-TRANSACTION-PROFILE-XXXXXX
```

---

# Contrato

```yaml
transaction_profile:
  id: EXEC-TRANSACTION-PROFILE-STANDARD

  isolation:
    state_transition: serializable_or_compare_and_swap
    read_projection: read_committed

  timeout:
    state_transition: PT5S

  external_calls_inside_transaction: forbidden
```

---

# Transaction Retry

Los conflictos transaccionales podrán reintentarse cuando:

- no exista side effect externo;
- se vuelva a leer el estado;
- se reevalúen Guards;
- el Command siga siendo válido.

---

# Outbox Pattern

El **Transactional Outbox** garantiza que los eventos derivados de una transición no se pierdan.

---

# Flujo

```text
Persist State
+
Persist Outbox
        ↓
Commit
        ↓
Outbox Publisher
        ↓
Event Bus
        ↓
Mark Published
```

---

# Outbox Record

```yaml
outbox_record:
  id: OUTBOX-000041

  aggregate:
    type: execution
    id: EXEC-000041

  event:
    id: EXEC-EVENT-000041
    type: execution_started

  state: pending

  attempts: 0
  available_at: 2026-08-02T20:00:02Z
```

---

# Outbox States

```text
pending
publishing
published
retry_wait
failed
dead_lettered
```

---

# Outbox Ordering

Cuando el orden por Execution sea relevante, deberá preservarse mediante:

- aggregate sequence;
- partition key;
- publicación ordenada;
- consumidores con buffer.

---

# Outbox Retry

Deberá ser idempotente.

---

# Inbox Pattern

El **Inbox** evita procesar dos veces el mismo mensaje.

---

# Flujo

```text
Receive Event
↓
Check Inbox
↓
Persist Inbox Record
+
Apply State Change
↓
Commit
↓
Acknowledge Message
```

---

# Inbox Record

```yaml
inbox_record:
  id: INBOX-SCHEDULER-EXEC-EVENT-000041

  consumer:
    id: SCHEDULER-CORE

  message:
    id: EXEC-EVENT-000041

  state: processed

  processed_at: 2026-08-02T20:00:02Z
```

---

# Inbox Retention

Deberá cubrir la ventana máxima de:

- reentrega;
- replay;
- retrasos;
- recuperación.

---

# Persistence Failure

Los fallos de persistencia deberán impedir confirmar transiciones.

---

# No “best effort” para estado crítico

---

# Write Failure Policy

Podrá:

- reintentar;
- degradar a read-only;
- bloquear nuevas ejecuciones;
- activar failover;
- entrar en modo de emergencia.

---

# Read-Only Operational Mode

El Orquestador podrá disponer de un modo:

```text
read_only
```

para permitir:

- inspección;
- diagnóstico;
- exportación;
- no nuevos dispatches;
- no nuevas transiciones.

---

# Recovery Engine

El **Recovery Engine** coordina la recuperación de estado y trabajo tras fallos.

Formato recomendado:

```text
EXEC-RECOVERY-ENGINE-XXXXXX
```

---

# Responsabilidades

- detectar ejecuciones incompletas;
- recuperar Scheduler state;
- identificar Jobs huérfanos;
- reconstruir Aggregates;
- rearmar timers;
- reactivar waits;
- reconciliar Workers;
- validar checkpoints;
- reanudar Executions;
- crear Recovery Executions;
- registrar diagnósticos.

---

# Contrato

```yaml
recovery_engine:
  id: EXEC-RECOVERY-ENGINE-PRIMARY

  version: 1.0.0

  capabilities:
    - state_reconstruction
    - orphan_recovery
    - timer_recovery
    - checkpoint_resume
    - external_reconciliation

  status: active
```

---

# Recovery Types

```text
process_restart
worker_failure
scheduler_failure
state_rebuild
checkpoint_resume
artifact_recovery
external_reconciliation
disaster_recovery
manual_recovery
```

---

# Process Restart Recovery

Al reiniciarse un nodo del Orquestador deberá:

1. registrarse;
2. validar su versión;
3. adquirir sus roles;
4. leer configuración;
5. recuperar timers reclamables;
6. detectar leases expiradas;
7. reconstruir caches;
8. reanudar polling o event consumers;
9. iniciar reconciliación.

---

# Scheduler Failure Recovery

Si un Scheduler desaparece:

- sus locks expiran;
- sus leases de coordinación expiran;
- otros Scheduler continúan;
- Jobs leased a Workers no se reasignan automáticamente si la Worker Lease sigue válida;
- se reconcilian operaciones incompletas.

---

# Worker Failure Recovery

Si un Worker deja de emitir heartbeats:

```text
healthy
↓
suspected
↓
unreachable
↓
lease_expired
↓
job_orphaned
↓
reconcile
↓
reassign / block / fail
```

---

# Worker Failure States

```text
suspected
unreachable
confirmed_failed
recovered
```

---

# Heartbeat Grace

Deberá existir una ventana antes de declarar fallo confirmado.

---

# Job Orphan Recovery

Un Job huérfano deberá analizarse antes de reasignarse.

---

# Orphan Recovery Decision

```yaml
orphan_recovery_decision:
  job:
    id: JOB-000041

  step_run:
    id: STEP-RUN-000045

  activity:
    idempotent: true

  external_status:
    result: not_started

  decision:
    action: requeue

  new_attempt_required: true
```

---

# Posibles decisiones

```text
requeue
wait
reconcile
mark_succeeded
mark_failed
mark_unknown
manual_review
compensate
```

---

# Idempotent Job

Puede reencolarse con menor riesgo.

---

# Non-Idempotent Job

Deberá consultar:

- external idempotency record;
- estado del motor;
- Artifact Store;
- callback;
- audit trail.

---

# State Reconstruction

El estado podrá reconstruirse mediante:

```text
Latest Valid Snapshot
        ↓
History Entries after Snapshot
        ↓
Apply Transitions
        ↓
Validate Revision
        ↓
Compare Current State
```

---

# Reconstruction Request

```yaml
state_reconstruction_request:
  id: EXEC-RECONSTRUCTION-REQ-000041

  execution:
    id: EXEC-000041

  source:
    snapshot: EXEC-HISTORY-SNAPSHOT-000041
    from_sequence: 1001

  mode: validate_and_compare
```

---

# Reconstruction Result

```yaml
state_reconstruction_result:
  execution:
    id: EXEC-000041

  reconstructed_revision: 118
  persisted_revision: 118

  status: consistent
```

---

# Divergence

Si el estado reconstruido no coincide:

```text
EXECUTION_STATE_DIVERGENCE
```

La Execution deberá:

- bloquearse;
- auditarse;
- reconciliarse;
- no continuar ciegamente.

---

# Checkpoint Resume

La reanudación desde checkpoint deberá verificar:

- checksum;
- History Sequence;
- Definition Version;
- State Machine Version;
- Activities disponibles;
- Artifacts;
- security context;
- policies;
- deadlines;
- child states;
- pending timers.

---

# Resume Plan

Formato recomendado:

```text
EXEC-RESUME-PLAN-XXXXXX
```

---

# Contrato

```yaml
execution_resume_plan:
  id: EXEC-RESUME-PLAN-000041

  execution:
    id: EXEC-000041

  checkpoint:
    id: EXEC-CHECKPOINT-000041

  completed_steps:
    - STEP-VALIDATE
    - STEP-BUILD-GRAPH

  resume_from:
    - STEP-BUILD-INDEX

  recovered_timers:
    - EXEC-TIMER-000041

  validation:
    status: passed
```

---

# No repetir Steps completados

Salvo que:

- su Artifact sea inválido;
- el output haya expirado;
- la política requiera revalidación;
- se cree una Recovery Execution.

---

# Recovery Execution

Cuando no pueda continuarse la misma Execution deberá crearse una ejecución específica.

Formato recomendado:

```text
EXEC-RECOVERY-XXXXXX
```

---

# Contrato

```yaml
recovery_execution:
  id: EXEC-000052

  type: recovery

  recovers:
    execution_id: EXEC-000041

  definition:
    id: EXEC-DEF-KNOWLEDGE-PUBLICATION-RECOVERY
    version: 1.0.0

  strategy:
    resume_from_checkpoint: EXEC-CHECKPOINT-000041

  correlation:
    root_execution_id: EXEC-000041
    correlation_id: CORR-000041
```

---

# Recovery Result

Deberá declarar:

- qué se recuperó;
- qué se repitió;
- qué se descartó;
- qué se compensó;
- qué resultado sustituye o complementa al anterior.

---

# Timer Recovery

Al iniciar el Timer Service deberá:

- identificar timers vencidos;
- reclamar lotes;
- aplicar missed timer policy;
- impedir doble disparo;
- registrar drift;
- rearmar próximos timers.

---

# Signal Recovery

Deberá:

- reactivar señales bufferizadas;
- eliminar expiradas;
- relacionarlas con Wait Records;
- detectar señales aplicadas sin transición;
- reconciliar inconsistencias.

---

# Child Execution Recovery

El parent deberá revisar:

- children terminales;
- children activos;
- children perdidos;
- resultados no aplicados;
- cancelaciones pendientes.

---

# External Reconciliation

Algunos motores externos mantendrán su propio estado.

---

# Reconciliation Adapter

Cada Engine Adapter crítico podrá ofrecer:

```text
get_operation_status
get_result_by_idempotency_key
cancel_operation
verify_artifact
```

---

# External Status Contract

```yaml
external_operation_status:
  operation_id: INDEX-BUILD-000041
  idempotency_key: EXEC-000041:STEP-BUILD-INDEX

  status: succeeded

  result_reference:
    id: IDX-SNAP-CANDIDATE-000041

  fencing_token: 16
```

---

# Recovery Priorities

Orden recomendado:

```text
Security and Consistency
↓
Prevent Duplicate Effects
↓
Restore State
↓
Recover Critical Path
↓
Recover Optional Work
↓
Rebuild Projections
```

---

# Recovery Budget

Toda recuperación deberá tener límites.

```yaml
recovery_budget:
  maximum_duration: PT30M
  maximum_reconciliation_calls: 100
  maximum_retries: 3
  maximum_parallel_recoveries: 20
```

---

# Recovery Storm

Después de una caída global podrían existir miles de Executions recuperables.

El sistema deberá evitar una tormenta de recuperación.

---

# Recovery Admission Control

Podrá:

- procesar por prioridad;
- limitar concurrencia;
- escalonar tenants;
- priorizar Critical Path;
- retrasar trabajo no esencial;
- aplicar jitter.

---

# Backup

Un **Backup** conserva una copia recuperable de datos operativos.

---

# Backup Scope

Podrá incluir:

- State Store;
- History Store;
- Event Store;
- definitions;
- schemas;
- policy references;
- Audit Store;
- Checkpoint Store;
- Artifact metadata;
- objetos críticos.

---

# No todos los Artifacts requieren copia completa

La política deberá distinguir:

- reconstruibles;
- irremplazables;
- publicados;
- temporales.

---

# Backup Types

```text
full
incremental
differential
continuous
snapshot
logical
physical
```

---

# Backup Contract

Formato recomendado:

```text
EXEC-BACKUP-XXXXXX
```

```yaml
execution_backup:
  id: EXEC-BACKUP-20260802-0001

  type: incremental

  scope:
    environment: production
    tenants:
      - TENANT-0001

  base_backup:
    id: EXEC-BACKUP-20260801-0001

  range:
    from: 2026-08-02T00:00:00Z
    to: 2026-08-02T23:59:59Z

  integrity:
    checksum: ...
    encrypted: true

  status: completed
```

---

# Backup Frequency

Deberá derivarse del RPO.

---

# Backup Validation

Deberá comprobar:

- integridad;
- descifrado;
- completitud;
- schemas;
- referencias;
- restaurabilidad.

---

# Restore Test

Todo plan deberá incluir restauraciones periódicas en un entorno aislado.

---

# Backup Retention

Podrá establecerse por niveles:

```text
daily
weekly
monthly
release
incident
legal_hold
```

---

# Backup Security

Deberá incluir:

- cifrado en tránsito;
- cifrado en reposo;
- acceso mínimo;
- separación de credenciales;
- auditoría;
- protección frente a borrado;
- copia fuera de la región cuando proceda.

---

# Restore

El **Restore** recupera datos desde backup.

---

# Restore Types

```text
full_environment
tenant
execution
store
point_in_time
artifact
metadata
```

---

# Point-in-Time Recovery

Cuando la tecnología lo permita deberá poder restaurarse a un instante previo.

---

# Restore Plan

Formato recomendado:

```text
EXEC-RESTORE-PLAN-XXXXXX
```

---

# Contrato

```yaml
restore_plan:
  id: EXEC-RESTORE-PLAN-000041

  source_backup:
    id: EXEC-BACKUP-20260802-0001

  target:
    environment: recovery
    point_in_time: 2026-08-02T20:00:00Z

  scope:
    stores:
      - state
      - history
      - queue
      - timer

  validation:
    dry_run_required: true
```

---

# Restore Phases

```text
Prepare Target
↓
Validate Backup
↓
Restore Base Data
↓
Apply Incrementals
↓
Verify Integrity
↓
Rebuild Projections
↓
Reconcile External Systems
↓
Run Quality Gates
↓
Open Traffic
```

---

# Restore Isolation

No deberá restaurarse directamente sobre producción sin:

- plan;
- aprobación;
- backup del estado actual;
- validación;
- rollback.

---

# Restoration of Active Executions

Las Executions restauradas pueden contener:

- leases antiguas;
- timers vencidos;
- Jobs activos;
- Workers inexistentes;
- callbacks ya ocurridos.

---

# Post-Restore Sanitization

Deberá:

- invalidar leases;
- incrementar fencing epochs;
- marcar Jobs activos como recovery_pending;
- rearmar timers;
- reconciliar external operations;
- bloquear side effects hasta validar.

---

# Restore Epoch

Podrá existir un identificador global.

```yaml
restore_epoch:
  value: 2026080201
```

Todo Worker o Scheduler con epoch anterior deberá quedar invalidado.

---

# Disaster Recovery

El **Disaster Recovery** define cómo recuperar el sistema tras una pérdida grave.

---

# Escenarios

- pérdida completa de Scheduler Cluster;
- pérdida de State Store;
- pérdida regional;
- corrupción extensa;
- credenciales comprometidas;
- pérdida de Artifact Store;
- publicación errónea masiva.

---

# DR Plan

Formato recomendado:

```text
EXEC-DR-PLAN-XXXXXX
```

---

# Contrato

```yaml
disaster_recovery_plan:
  id: EXEC-DR-PLAN-PRODUCTION

  version: 1.0.0

  target:
    rpo: PT5M
    rto: PT30M

  failover_region:
    id: eu-central

  stores:
    state:
      strategy: replicated
    history:
      strategy: continuous_backup
    artifacts:
      strategy: cross_region_replication

  activation:
    approval_required: true
```

---

# Recovery Point Objective

El **RPO** define la pérdida máxima de datos aceptable.

Ejemplo:

```text
RPO = 5 minutos
```

---

# Recovery Time Objective

El **RTO** define el tiempo máximo objetivo para restaurar el servicio.

Ejemplo:

```text
RTO = 30 minutos
```

---

# RPO/RTO por componente

| Componente | RPO | RTO |
|---|---:|---:|
| State Store | muy bajo | corto |
| History Store | muy bajo | corto |
| Queue Store | bajo | corto |
| Projection Store | más alto | reconstruible |
| Metrics | moderado | no crítico |
| Ephemeral Artifacts | variable | reconstruible |

---

# DR Modes

```text
backup_restore
warm_standby
hot_standby
active_passive
active_active
```

---

# Recomendación inicial

Para una primera implementación:

```text
active_passive
+
backup restore
```

con evolución posterior según necesidades.

---

# Failover

El failover deberá:

1. declarar incidente;
2. congelar el origen cuando sea posible;
3. validar quorum;
4. activar destino;
5. incrementar epoch;
6. restaurar o promocionar datos;
7. invalidar leases antiguas;
8. reconstruir queues;
9. rearmar timers;
10. reconciliar external systems;
11. validar Quality Gates;
12. abrir tráfico.

---

# Failback

Volver a la región original deberá tratarse como un nuevo proceso controlado.

---

# No failback automático no validado

---

# Split-Brain durante DR

Deberá evitarse mediante:

- fencing epoch;
- quorum;
- DNS o routing controlado;
- revocación de credenciales;
- leader lease;
- write authority única.

---

# Disaster Recovery Exercise

Deberán realizarse simulacros.

---

# DR Exercise Record

```yaml
dr_exercise:
  id: EXEC-DR-EXERCISE-2026-08

  plan:
    id: EXEC-DR-PLAN-PRODUCTION

  scenario: primary_region_loss

  measured:
    rpo: PT2M
    rto: PT24M

  status: passed
```

---

# Alta disponibilidad

El Orquestador deberá operar sin depender de una única instancia.

---

# Componentes HA

- Execution Gateway;
- Scheduler Nodes;
- Timer Workers;
- Outbox Publishers;
- Recovery Engine;
- State Store;
- Queue Store;
- Event Bus;
- Artifact metadata.

---

# Stateless Services

Siempre que sea posible, los nodos de aplicación deberán ser stateless.

---

# Stateful Services

Los almacenes deberán disponer de:

- replicación;
- failover;
- backups;
- monitorización;
- quorum;
- consistency guarantees.

---

# Scheduler High Availability

Múltiples Scheduler Nodes podrán operar concurrentemente mediante:

- atomic claims;
- leases;
- revision control;
- leader election para tareas singleton.

---

# No sticky ownership permanente

Una Execution no deberá depender indefinidamente del mismo Scheduler.

---

# Worker High Availability

Los Worker Pools podrán contener múltiples Workers equivalentes.

---

# Degraded Pool

Si un Worker Pool pierde capacidad:

- se reduce admission;
- se incrementa queue time;
- se activa autoscaling;
- se utilizan fallbacks;
- se bloquean workloads no compatibles.

---

# Health Checks

Tipos:

```text
liveness
readiness
startup
dependency
deep_health
```

---

# Liveness

Indica si el proceso está vivo.

---

# Readiness

Indica si puede recibir trabajo.

---

# Dependency Health

Comprueba:

- State Store;
- Queue Store;
- Event Bus;
- Artifact Store;
- Policy Engine.

---

# Deep Health

No deberá ejecutarse con una frecuencia excesiva.

---

# Health Status

```text
healthy
degraded
unhealthy
unknown
```

---

# Traffic Management

Un nodo no ready deberá retirarse del balanceo.

---

# Graceful Shutdown

Durante shutdown:

1. dejar de aceptar nuevo trabajo;
2. entrar en draining;
3. dejar de reclamar Jobs;
4. finalizar operaciones seguras;
5. renovar leases necesarias;
6. transferir ownership o abandonar;
7. persistir estado;
8. cerrar conexiones;
9. finalizar.

---

# Shutdown Timeout

Si se excede:

- liberar leases;
- marcar Runs para reconciliación;
- terminar proceso.

---

# Rolling Upgrade

Las actualizaciones deberán poder realizarse sin detener todas las Executions.

---

# Rolling Upgrade Preconditions

- compatibilidad de schemas;
- State Machine Versions disponibles;
- Definition Versions archivadas;
- workers mixtos compatibles;
- feature flags;
- rollback plan.

---

# Version Skew

Podrá permitirse un rango limitado de versiones coexistentes.

---

# Compatibility Matrix

```yaml
compatibility_matrix:
  orchestrator:
    1.4.x:
      workers:
        - 1.3.x
        - 1.4.x

      state_schema:
        - 3.x

      event_schema:
        - 2.x
        - 3.x
```

---

# No despliegue que retire contratos activos

---

# Database Migration

Las migraciones deberán:

- versionarse;
- ser idempotentes cuando sea posible;
- soportar rollback o roll-forward;
- evitar bloqueos prolongados;
- preservar datos;
- probarse con volúmenes reales.

---

# Expand and Contract

Patrón recomendado:

```text
Add New Schema
↓
Write Old + New
↓
Backfill
↓
Read New
↓
Stop Writing Old
↓
Remove Old Later
```

---

# Migration State

Formato recomendado:

```text
EXEC-MIGRATION-STATE-XXXXXX
```

---

# Contrato

```yaml
schema_migration:
  id: EXEC-SCHEMA-MIGRATION-000041

  store: EXEC-STATE-STORE-PRIMARY

  from_version: 3.0.0
  to_version: 3.1.0

  strategy: expand_contract

  status: backfilling
```

---

# Backfill

Los backfills deberán:

- ser reanudables;
- utilizar checkpoints;
- limitar carga;
- emitir métricas;
- preservar revisiones;
- no impedir operación normal.

---

# Feature Flags

Podrán utilizarse para activar capacidades gradualmente.

---

# No feature flags permanentes sin owner

Cada flag deberá tener:

- owner;
- propósito;
- fecha de revisión;
- estrategia de retirada.

---

# Operational Modes

El Orquestador podrá tener modos explícitos.

```text
normal
degraded
read_only
maintenance
draining
recovery
disaster_recovery
emergency_stop
```

---

# Normal

Operación completa.

---

# Degraded

Capacidades reducidas.

---

# Read Only

Consulta permitida, cambios bloqueados.

---

# Maintenance

Operaciones administrativas controladas.

---

# Recovery

Se prioriza recuperación.

---

# Emergency Stop

Se detienen nuevos side effects.

---

# Operational Mode Record

```yaml
operational_mode:
  environment: production

  mode: degraded

  reason:
    code: ARTIFACT_STORE_PARTIAL_OUTAGE

  restrictions:
    - no_new_index_publications

  activated_at: 2026-08-02T20:30:00Z
```

---

# Admission by Mode

Cada modo deberá declarar qué operaciones permite.

---

# Emergency Stop

Deberá poder:

- detener nuevos dispatches;
- impedir publicaciones;
- conservar lecturas;
- permitir cancelaciones;
- permitir recuperación;
- registrar auditoría.

---

# Retention

La **Retention Policy** define cuánto tiempo se conservan datos.

Formato recomendado:

```text
EXEC-RETENTION-POLICY-XXXXXX
```

---

# Dimensiones

```text
data_type
state
environment
tenant
classification
legal_hold
recovery_need
audit_need
```

---

# Contrato

```yaml
retention_policy:
  id: EXEC-RETENTION-POLICY-STANDARD

  version: 1.0.0

  rules:
    execution_state:
      terminal: P180D

    execution_history:
      succeeded: P365D
      failed: P730D

    audit:
      duration: P2555D

    ephemeral_artifacts:
      duration: P7D

    checkpoints:
      after_terminal: P30D
```

---

# Retention by Result

Podrá conservarse más tiempo:

- failed;
- compensated;
- security incidents;
- manual overrides;
- legal holds.

---

# Legal Hold

Deberá bloquear eliminación.

---

# Legal Hold Record

```yaml
legal_hold:
  id: EXEC-LEGAL-HOLD-000041

  scope:
    execution_id: EXEC-000041

  reason: security_investigation

  status: active
```

---

# Retention Evaluation

Antes de eliminar deberá comprobarse:

- referencias activas;
- legal hold;
- child relationships;
- Artifact lineage;
- audit requirements;
- recovery window;
- policy version.

---

# Archive

El **Archive** mueve datos fuera del almacenamiento operativo manteniendo acceso gobernado.

---

# Archivable Data

- Executions terminales;
- History antiguo;
- Events;
- Audit Records;
- Checkpoints;
- Artifacts no activos.

---

# Archive Record

```yaml
archive_record:
  id: EXEC-ARCHIVE-000041

  scope:
    execution_id: EXEC-000041

  contents:
    - state
    - history
    - audit
    - artifact_metadata

  storage:
    class: cold

  checksum: ...
  status: completed
```

---

# Archive Read

Podrá requerir:

- restauración temporal;
- acceso administrativo;
- auditoría;
- latencia superior.

---

# Archive Immutability

Los archivos de auditoría y compliance deberán protegerse contra modificación.

---

# Compaction

La **Compaction** reduce volumen sin perder semántica esencial.

---

# Compaction Targets

- History;
- Event Streams;
- Queue tombstones;
- Inbox Records;
- Outbox Records;
- Projections;
- Logs.

---

# History Compaction

Podrá:

- crear snapshots;
- agrupar eventos técnicos repetitivos;
- externalizar payloads;
- archivar segmentos.

---

# No eliminar hechos necesarios para replay

---

# Compaction Policy

Formato recomendado:

```text
EXEC-COMPACTION-POLICY-XXXXXX
```

---

# Contrato

```yaml
compaction_policy:
  id: EXEC-COMPACTION-POLICY-HISTORY

  version: 1.0.0

  trigger:
    history_entries_greater_than: 10000

  action:
    create_snapshot: true
    archive_before_sequence: 9000

  preserve:
    - decisions
    - state_transitions
    - commands
    - audit_events
    - side_effect_results
```

---

# Event Compaction

Solo podrá aplicarse cuando:

- exista una proyección o snapshot equivalente;
- los consumidores no necesiten cada evento;
- la política lo permita.

---

# Inbox Compaction

Los IDs procesados podrán eliminarse cuando supere la ventana máxima de redelivery.

---

# Outbox Compaction

Los records publicados podrán archivarse o eliminarse tras:

- confirmación;
- retención;
- auditoría.

---

# Garbage Collection

La **Garbage Collection** elimina datos no necesarios según políticas.

---

# GC Targets

- Artifacts huérfanos;
- leases expiradas;
- locks expirados;
- timers terminales;
- signals expiradas;
- temporary workspaces;
- stale projections;
- obsolete definitions no referenciadas;
- superseded snapshots.

---

# GC Candidate

Formato recomendado:

```text
EXEC-GC-CANDIDATE-XXXXXX
```

---

# Contrato

```yaml
garbage_collection_candidate:
  id: EXEC-GC-CANDIDATE-000041

  resource:
    type: artifact
    id: EXEC-ARTIFACT-000041

  reason:
    code: RETENTION_EXPIRED

  checks:
    active_references: 0
    legal_hold: false
    recovery_required: false

  status: eligible
```

---

# Mark and Sweep

Proceso recomendado:

```text
Discover Candidate
↓
Mark
↓
Wait Grace Period
↓
Revalidate References
↓
Delete
↓
Audit
```

---

# GC Grace Period

Evita eliminar datos por una referencia retrasada.

---

# No eliminación inmediata

Especialmente para:

- Artifacts;
- checkpoints;
- definitions;
- execution histories.

---

# Orphan Artifact Detection

Un Artifact será huérfano cuando:

- no lo referencie ninguna Execution;
- no pertenezca a un resultado;
- no tenga legal hold;
- haya superado grace period.

---

# Definition Garbage Collection

Una Definition solo podrá eliminarse si:

- no existen Executions activas;
- no se necesita para replay;
- no se necesita para auditoría;
- no la importa otra Definition;
- ha expirado su retención.

---

# Operational Observability

La arquitectura operacional deberá ser observable en profundidad.

---

# Golden Signals

```text
latency
traffic
errors
saturation
```

---

# Métricas de persistencia

- State Store latency;
- write failures;
- transaction conflicts;
- History append latency;
- History gaps;
- Queue claim latency;
- timer scan latency;
- Outbox backlog;
- Inbox deduplication rate.

---

# Métricas de almacenamiento

- rows;
- partitions;
- bytes;
- growth rate;
- index size;
- fragmentation;
- archive volume;
- backup size.

---

# Métricas de recuperación

- recovery attempts;
- recovery success rate;
- executions recovered;
- orphan Jobs;
- reconciliation duration;
- checkpoint validation failures;
- state divergence.

---

# Métricas de backup

- backup duration;
- backup age;
- backup failures;
- checksum failures;
- restore test age;
- RPO achieved.

---

# Métricas de DR

- replication lag;
- standby readiness;
- last DR exercise;
- measured RTO;
- measured RPO;
- failover errors.

---

# Métricas de GC

- candidates;
- deleted resources;
- bytes reclaimed;
- protected by hold;
- deletion failures;
- orphan Artifacts.

---

# Métricas de retención

- records by policy;
- records expired;
- archive backlog;
- policy violations.

---

# Outbox Lag

```text
current_time
-
oldest_pending_outbox_record
```

---

# Queue Recovery Lag

Tiempo entre:

- lease expiration;
- orphan detection;
- recovery decision;
- requeue.

---

# Timer Drift

```text
actual_fire_time
-
scheduled_fire_time
```

---

# Storage SLOs

Podrán establecerse SLOs para:

- state write availability;
- History durability;
- queue claim latency;
- timer firing delay;
- Outbox publication latency;
- recovery time.

---

# SLO Contract

```yaml
operational_slo:
  id: SLO-EXECUTION-STATE-WRITE

  objective:
    availability: 0.9999
    p95_latency_ms: 100

  window: P30D
```

---

# Alertas

Las alertas deberán ser accionables.

---

# Alert Categories

```text
availability
durability
consistency
capacity
latency
recovery
security
retention
backup
disaster_recovery
```

---

# Alert Examples

```text
State Store unavailable
Outbox backlog above threshold
History gap detected
Timer drift exceeded
Queue claim failures
Recovery storm
Backup overdue
Restore test expired
Artifact corruption
Split-brain risk
```

---

# Alert Contract

```yaml
operational_alert:
  id: ALERT-OUTBOX-BACKLOG

  severity: critical

  condition:
    oldest_pending_age:
      greater_than: PT5M

  impact:
    description: Lifecycle events may be delayed.

  runbook:
    id: RUNBOOK-OUTBOX-BACKLOG
```

---

# Severidades

```text
info
warning
major
critical
```

---

# No alertar por cada fallo individual esperado

Los retries normales deberán observarse mediante métricas, no necesariamente alertas.

---

# Runbooks

Todo incidente relevante deberá disponer de un runbook.

Formato recomendado:

```text
EXEC-RUNBOOK-XXXXXX
```

---

# Runbook Contents

- síntoma;
- impacto;
- comprobaciones;
- métricas;
- logs;
- acciones seguras;
- acciones peligrosas;
- rollback;
- escalación;
- criterios de cierre.

---

# Runbook Example

```yaml
runbook:
  id: RUNBOOK-HISTORY-GAP

  trigger:
    diagnostic: EXECUTION_HISTORY_GAP

  steps:
    - freeze_execution
    - verify_replica
    - inspect_backup
    - reconstruct_missing_entries
    - validate_state
    - resume_or_create_recovery_execution
```

---

# Operational Dashboard

Vistas recomendadas:

- Executions activas;
- Queue Depth;
- Workers;
- Timers;
- Outbox;
- Recoveries;
- Backups;
- State Store;
- Artifact Health;
- DR readiness.

---

# Logging operacional

Los logs deberán incluir:

- Execution ID;
- Step Run ID;
- Job ID;
- tenant;
- correlation;
- component;
- version;
- operational mode.

---

# No incluir

- secrets;
- payloads completos;
- datos personales innecesarios;
- contenido de Artifacts;
- tokens de acceso.

---

# Tracing operacional

Deberá cubrir:

```text
API Request
↓
Execution Creation
↓
State Transaction
↓
Outbox Publication
↓
Job Claim
↓
Worker Invocation
↓
Activity Result
↓
Finalization
```

---

# Trace Sampling

Las Executions fallidas o lentas podrán conservar tracing completo.

---

# Auditability

Deberá poder reconstruirse:

- quién inició;
- qué versión;
- qué estado;
- qué decisiones;
- qué overrides;
- qué backup;
- qué restore;
- qué recovery;
- qué eliminación.

---

# Capacity Planning

La operación en producción deberá dimensionarse.

---

# Capacity Dimensions

```text
executions_per_second
active_executions
steps_per_execution
jobs_per_second
history_events_per_second
timers
signals
artifact_volume
worker_slots
storage_growth
```

---

# Capacity Model

```yaml
capacity_model:
  expected:
    executions_per_day: 100000
    average_steps_per_execution: 12
    peak_jobs_per_second: 500
    active_timers: 1000000

  growth:
    monthly: 0.10
```

---

# Headroom

Deberá conservarse margen operativo.

Ejemplo:

```text
30 %
```

---

# Saturation Signals

- Queue Depth;
- transaction latency;
- lock contention;
- worker utilization;
- timer lag;
- storage IO;
- Outbox lag.

---

# Autoscaling Inputs

- Ready Jobs;
- queue age;
- Worker saturation;
- estimated work;
- critical deadlines;
- tenant quotas.

---

# No escalar únicamente por CPU

Un Worker puede estar limitado por:

- API externa;
- GPU;
- memoria;
- IO;
- rate limit.

---

# Cost Management

La arquitectura podrá registrar:

- compute;
- storage;
- network;
- external API;
- LLM;
- GPU;
- backups.

---

# Cost Allocation

Podrá atribuirse por:

- tenant;
- workflow;
- Activity;
- environment;
- Execution.

---

# Cost Record

```yaml
execution_cost_record:
  execution_id: EXEC-000041

  dimensions:
    compute: 0.42
    storage: 0.03
    external_api: 0.12

  currency: EUR
```

---

# Security operacional

---

# Store Credentials

Deberán:

- rotarse;
- limitarse;
- separarse por componente;
- evitar acceso global.

---

# Backup Credentials

Deberán ser independientes de las credenciales operativas cuando sea posible.

---

# Encryption

Obligatoria para:

- State Store sensible;
- History;
- Audit;
- Artifacts;
- Backups.

---

# Key Rotation

Deberá existir una estrategia de rotación.

---

# Audit Access

El acceso a Audit Store deberá estar especialmente restringido.

---

# Restore Authorization

Las restauraciones deberán requerir:

- actor autorizado;
- motivo;
- scope;
- aprobación;
- auditoría.

---

# Deletion Authorization

Las eliminaciones irreversibles deberán:

- pasar retention checks;
- respetar holds;
- generar audit;
- permitir dry-run.

---

# Operational Diagnostics

Códigos iniciales:

```text
EXECUTION_STATE_STORE_UNAVAILABLE
EXECUTION_STATE_WRITE_FAILED
EXECUTION_STATE_DIVERGENCE
EXECUTION_HISTORY_APPEND_FAILED
EXECUTION_HISTORY_GAP
EXECUTION_HISTORY_CORRUPTED
EXECUTION_QUEUE_STORE_UNAVAILABLE
EXECUTION_JOB_CLAIM_CONFLICT
EXECUTION_TIMER_STORE_UNAVAILABLE
EXECUTION_TIMER_RECOVERY_FAILED
EXECUTION_SIGNAL_STORE_INCONSISTENT
EXECUTION_CHECKPOINT_STORE_UNAVAILABLE
EXECUTION_CHECKPOINT_CORRUPTED
EXECUTION_ARTIFACT_STORE_UNAVAILABLE
EXECUTION_ARTIFACT_MISSING
EXECUTION_ARTIFACT_CORRUPTED
EXECUTION_OUTBOX_BACKLOG
EXECUTION_OUTBOX_PUBLICATION_FAILED
EXECUTION_INBOX_DUPLICATE
EXECUTION_PROJECTION_LAG_EXCEEDED
EXECUTION_RECOVERY_FAILED
EXECUTION_RECOVERY_STORM
EXECUTION_RESTORE_FAILED
EXECUTION_BACKUP_FAILED
EXECUTION_BACKUP_OVERDUE
EXECUTION_BACKUP_INTEGRITY_FAILED
EXECUTION_DR_REPLICATION_LAG
EXECUTION_DR_FAILOVER_FAILED
EXECUTION_RETENTION_POLICY_VIOLATION
EXECUTION_ARCHIVE_FAILED
EXECUTION_COMPACTION_FAILED
EXECUTION_GARBAGE_COLLECTION_FAILED
EXECUTION_LEGAL_HOLD_VIOLATION
EXECUTION_STORAGE_CAPACITY_RISK
EXECUTION_OPERATIONAL_MODE_DEGRADED
```

---

# Diagnostic Contract

```yaml
operational_diagnostic:
  id: EXEC-OP-DIAGNOSTIC-000041

  code: EXECUTION_OUTBOX_BACKLOG
  severity: critical

  component:
    id: OUTBOX-PUBLISHER-PRIMARY

  details:
    pending_records: 12500
    oldest_age: PT12M

  impact:
    lifecycle_events_delayed: true

  runbook:
    id: RUNBOOK-OUTBOX-BACKLOG
```

---

# Quality Gate de persistencia

```yaml
quality_gate:
  id: QG-EXECUTION-PERSISTENCE-0001

  criteria:
    all:
      - state_store_durable == true
      - optimistic_concurrency_enabled == true
      - history_append_only == true
      - history_gap_detection_enabled == true
      - queue_claim_atomic == true
      - timers_durable == true
      - signals_deduplicated == true
      - checkpoints_checksummed == true
      - artifacts_checksummed == true
      - audit_append_only == true
```

---

# Quality Gate de Outbox e Inbox

```yaml
quality_gate:
  id: QG-EXECUTION-MESSAGING-0001

  criteria:
    all:
      - outbox_transactional == true
      - outbox_retry_idempotent == true
      - event_ordering_preserved == true
      - inbox_deduplication_enabled == true
      - inbox_retention_defined == true
      - dead_letter_handling_defined == true
```

---

# Quality Gate de Recovery

```yaml
quality_gate:
  id: QG-EXECUTION-RECOVERY-0001

  criteria:
    all:
      - orphan_detection_enabled == true
      - checkpoint_resume_supported == true
      - state_reconstruction_supported == true
      - unknown_outcome_reconciliation_defined == true
      - recovery_budget_defined == true
      - recovery_storm_protection_enabled == true
      - recovery_actions_audited == true
```

---

# Quality Gate de Backup y Restore

```yaml
quality_gate:
  id: QG-EXECUTION-BACKUP-RESTORE-0001

  criteria:
    all:
      - backup_schedule_defined == true
      - backups_encrypted == true
      - backup_integrity_verified == true
      - restore_procedure_defined == true
      - restore_tests_current == true
      - retention_defined == true
      - restore_epoch_supported == true
```

---

# Quality Gate de Disaster Recovery

```yaml
quality_gate:
  id: QG-EXECUTION-DR-0001

  criteria:
    all:
      - rpo_defined == true
      - rto_defined == true
      - failover_plan_defined == true
      - split_brain_protection_enabled == true
      - standby_health_verified == true
      - last_dr_exercise_passed == true
      - failback_plan_defined == true
```

---

# Quality Gate de retención

```yaml
quality_gate:
  id: QG-EXECUTION-RETENTION-0001

  criteria:
    all:
      - retention_policies_versioned == true
      - legal_hold_supported == true
      - archive_integrity_verified == true
      - garbage_collection_has_grace_period == true
      - active_references_checked == true
      - destructive_actions_audited == true
```

---

# Quality Gate operacional

```yaml
quality_gate:
  id: QG-EXECUTION-OPERATIONS-0001

  criteria:
    all:
      - health_checks_defined == true
      - operational_modes_defined == true
      - graceful_shutdown_supported == true
      - rolling_upgrade_supported == true
      - compatibility_matrix_defined == true
      - runbooks_available == true
      - alerts_actionable == true
      - capacity_headroom_defined == true
      - security_controls_enabled == true
```

---

# Casos de uso

---

# Caso de uso 1 — Reinicio del Orquestador

El proceso se reinicia durante una ejecución.

El nuevo nodo:

- recupera configuración;
- lee State Store;
- detecta Jobs y timers;
- reanuda Outbox;
- no repite Activities confirmadas.

---

# Caso de uso 2 — Worker perdido

El heartbeat desaparece.

Tras el periodo de gracia:

- expira la lease;
- el Job queda orphaned;
- se consulta el estado externo;
- se reencola si es seguro.

---

# Caso de uso 3 — History extensa

Una Execution posee 100 000 History Entries.

Se crea un snapshot hasta la secuencia 95 000 y se archivan segmentos antiguos sin perder replay.

---

# Caso de uso 4 — Outbox retrasada

El Event Bus falla.

Las transiciones continúan persistiendo Outbox Records.

Cuando el bus se recupera, los eventos se publican de forma ordenada.

---

# Caso de uso 5 — Señal antes del Wait

La señal se almacena en Signal Store.

Al materializarse el Wait, la señal se consume transaccionalmente.

---

# Caso de uso 6 — Timer vencido durante caída

El Timer Service se recupera.

Aplica `fire_immediately`, evita doble disparo y registra el drift.

---

# Caso de uso 7 — Artifact corrupto

El checksum no coincide.

La Execution queda bloqueada y se inicia una Recovery Execution para reconstruir el Artifact.

---

# Caso de uso 8 — Restauración puntual

Se restaura el entorno a un instante anterior a una corrupción.

Después:

- se invalidan leases;
- se incrementa epoch;
- se rearman timers;
- se reconcilian operaciones externas.

---

# Caso de uso 9 — Pérdida regional

Se activa el DR Plan.

La región secundaria asume autoridad de escritura tras validar quorum y fencing epoch.

---

# Caso de uso 10 — Rolling Upgrade

Conviven Scheduler 1.3 y 1.4 durante el despliegue.

La Compatibility Matrix garantiza que ambos comprenden los contratos activos.

---

# Caso de uso 11 — Backfill de schema

Se añade un nuevo campo.

El backfill procesa lotes con checkpoints sin bloquear Executions nuevas.

---

# Caso de uso 12 — Retención expirada

Una Execution finalizada supera su política.

Se archiva el History y se eliminan Artifacts efímeros tras verificar referencias.

---

# Caso de uso 13 — Legal Hold

Una investigación bloquea el archivado destructivo y Garbage Collection de una Execution.

---

# Caso de uso 14 — Recovery Storm

Tras una caída, diez mil Jobs aparecen como orphaned.

Admission Control limita recuperaciones y prioriza workflows críticos.

---

# Caso de uso 15 — Divergencia de estado

El replay produce revisión 118, pero State Store contiene 119 con contenido incompatible.

La Execution queda `blocked` y requiere reconciliación.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Una única tabla para todo

Dificulta escalado, retención y semántica.

---

## State Store como History Store

Sobrescribir estado no conserva cómo se llegó a él.

---

## History mutable

Impide auditoría y replay fiable.

---

## Eventos externos como única fuente de verdad

Pueden perderse o llegar desordenados.

---

## Queue únicamente en memoria

Pierde Jobs al reiniciar.

---

## Timers únicamente en memoria

Pierde deadlines y retries.

---

## Outbox no transaccional

Puede separar estado y eventos.

---

## Inbox sin retención suficiente

Permite reprocesar mensajes tardíos.

---

## Payloads grandes en History

Aumentan coste y dificultan replay.

---

## Blobs en State Store

Deterioran transacciones.

---

## Checkpoints sin checksum

Permiten recuperar estados corruptos.

---

## Reanudar sin validar Artifacts

Puede propagar corrupción.

---

## Reencolar automáticamente todo Job orphaned

Puede duplicar side effects.

---

## Recovery sin presupuesto

Puede saturar el sistema tras una caída.

---

## Backup sin prueba de restore

No demuestra recuperabilidad.

---

## Backup con las mismas credenciales que producción

Aumenta riesgo de pérdida simultánea.

---

## Restaurar conservando leases antiguas

Puede provocar doble ejecución.

---

## Failover sin fencing epoch

Permite split-brain.

---

## Failback automático inmediato

Puede introducir nueva inconsistencia.

---

## Schema migration destructiva directa

Dificulta rollback.

---

## Backfill sin checkpoints

No puede reanudarse.

---

## Desplegar retirando versiones activas

Rompe Executions en curso.

---

## Proyección como fuente canónica

Puede estar retrasada.

---

## Retención igual para todos los datos

Ignora necesidades distintas.

---

## Eliminar antes de comprobar referencias

Puede romper lineage y recuperación.

---

## Garbage Collection sin grace period

Puede eliminar recursos todavía necesarios.

---

## Compactar eventos necesarios para replay

Impide reconstrucción.

---

## Legal Hold no integrado con GC

Puede producir eliminación indebida.

---

## Alertas sin runbook

Generan ruido sin acción.

---

## Alertar cada retry

Produce fatiga.

---

## No medir Outbox Lag

Puede ocultar eventos retrasados.

---

## No medir Timer Drift

Puede ocultar fallos temporales.

---

## Operación normal durante corrupción detectada

Debe degradarse o bloquearse.

---

## Emergency Stop que impide cancelaciones

Debe detener nuevos side effects, no toda capacidad operativa.

---

# Reglas mínimas de conformidad

---

## State Store durable

El estado confirmado deberá persistirse.

---

## History append-only

Toda transición deberá conservarse.

---

## Queue durable

Los Jobs deberán sobrevivir a reinicios.

---

## Timers durables

Los timers no dependerán de memoria local.

---

## Signals persistidas

Las señales bufferizadas deberán sobrevivir.

---

## Checkpoints verificables

Todo checkpoint deberá tener checksum.

---

## Artifacts protegidos

Deberán conservar integrity y lineage.

---

## Audit separado

Las acciones sensibles deberán ser auditables.

---

## Outbox transaccional

Los eventos deberán derivarse de estado confirmado.

---

## Inbox idempotente

La reentrega no deberá duplicar efectos.

---

## Recovery Engine

Deberá existir recuperación formal.

---

## Orphan Recovery

Los Jobs huérfanos deberán reconciliarse.

---

## State Reconstruction

El estado deberá poder reconstruirse.

---

## Recovery Budget

La recuperación deberá limitar carga.

---

## Backups verificables

Todo backup deberá comprobarse.

---

## Restore probado

La restauración deberá ensayarse.

---

## RPO y RTO definidos

Los objetivos deberán ser explícitos.

---

## Failover gobernado

Deberá impedir split-brain.

---

## Restore Epoch

Los actores anteriores a una restauración deberán invalidarse.

---

## Rolling Upgrade

Las versiones coexistentes deberán ser compatibles.

---

## Migrations versionadas

Los cambios de schema deberán ser trazables.

---

## Retention Policy

Toda clase de datos deberá tener política.

---

## Legal Hold

Deberá impedir eliminación.

---

## Garbage Collection segura

Deberá comprobar referencias y aplicar grace period.

---

## Observabilidad

Deberán existir métricas, logs, traces y alertas.

---

## Runbooks

Los incidentes críticos deberán tener procedimiento.

---

## Quality Gates

Ningún entorno productivo deberá operar sin superar controles operacionales.

---

# Conformidad del State Store

Será conforme cuando:

- sea durable;
- soporte revisión;
- permita transacciones;
- mantenga índices operativos;
- preserve tenant isolation;
- no dependa de memoria local;
- participe en backups.

---

# Conformidad del History Store

Será conforme cuando:

- sea append-only;
- mantenga secuencia;
- detecte gaps;
- preserve checksums;
- soporte replay;
- disponga de retención;
- permita archivado.

---

# Conformidad del Queue Store

Será conforme cuando:

- mantenga Jobs durables;
- soporte claims atómicos;
- preserve prioridad;
- soporte delayed Jobs;
- soporte retries;
- detecte leases expiradas;
- disponga de Dead Letter Queue.

---

# Conformidad del Timer Store

Será conforme cuando:

- persista timers;
- permita buscar vencidos;
- soporte claim;
- evite doble fire;
- aplique missed timer policy;
- mida drift.

---

# Conformidad del Artifact Store

Será conforme cuando:

- mantenga referencias estables;
- aplique checksum;
- preserve tenant;
- preserve clasificación;
- declare lifecycle;
- declare retención;
- soporte recovery.

---

# Conformidad de Outbox

Será conforme cuando:

- se escriba en la misma transacción que el estado;
- tenga ID;
- preserve ordering metadata;
- soporte retries;
- sea idempotente;
- tenga Dead Letter handling;
- sea observable.

---

# Conformidad de Recovery Engine

Será conforme cuando:

- detecte estados recuperables;
- preserve idempotencia;
- reconcilie unknown outcomes;
- valide checkpoints;
- reanime timers;
- procese Signals;
- controle recovery storms;
- audite decisiones.

---

# Conformidad de Backup

Será conforme cuando:

- tenga ID;
- declare scope;
- declare tipo;
- esté cifrado;
- tenga checksum;
- declare base cuando sea incremental;
- declare retención;
- haya sido validado.

---

# Conformidad de Restore

Será conforme cuando:

- tenga plan;
- declare source;
- declare target;
- preserve integridad;
- invalide leases;
- incremente epoch;
- reconstruya proyecciones;
- reconcilie externos;
- supere Gate.

---

# Conformidad de Disaster Recovery

Será conforme cuando:

- declare RPO;
- declare RTO;
- declare estrategia;
- declare región o entorno alternativo;
- preserve authority única;
- evite split-brain;
- tenga ejercicio reciente;
- tenga failback plan.

---

# Conformidad de Retention Policy

Será conforme cuando:

- tenga ID;
- tenga versión;
- declare data types;
- declare duraciones;
- considere estados;
- considere legal hold;
- sea auditable;
- sea ejecutable.

---

# Lista de comprobación

Antes de considerar operable el Orquestador deberá comprobarse:

```text
[ ] Existe Persistence Layer definido.
[ ] Existe State Store durable.
[ ] El State Store soporta optimistic concurrency.
[ ] El State Store soporta transacciones cortas.
[ ] Existe History Store append-only.
[ ] El History conserva secuencias.
[ ] El History detecta gaps.
[ ] El History utiliza checksums.
[ ] Existe Event Store o contrato equivalente.
[ ] Existe Queue Store durable.
[ ] Los Job Claims son atómicos.
[ ] Existe Delayed Queue.
[ ] Existe Retry Queue.
[ ] Existe Dead Letter Queue.
[ ] Existe Timer Store durable.
[ ] Los Timers evitan duplicate fire.
[ ] Existe Signal Store.
[ ] Las Signals están deduplicadas.
[ ] Existe Checkpoint Store.
[ ] Los Checkpoints tienen checksum.
[ ] Existe Artifact Store.
[ ] Los Artifacts tienen integrity metadata.
[ ] Los Artifacts tienen lineage.
[ ] Existe Audit Store.
[ ] El Audit Store es append-only.
[ ] Las Projections declaran lag.
[ ] Las Projections no se usan para decisiones críticas.
[ ] Las transacciones no incluyen llamadas externas.
[ ] Existe Transactional Outbox.
[ ] Existe Inbox para consumidores críticos.
[ ] La retención de Inbox está definida.
[ ] Existe Recovery Engine.
[ ] Se detectan Jobs orphaned.
[ ] Los Jobs no idempotentes se reconcilian antes de retry.
[ ] El estado puede reconstruirse desde History.
[ ] Existe validación de divergencia.
[ ] Los Checkpoints pueden reanudarse.
[ ] Existen Recovery Executions.
[ ] Los Timers se recuperan tras reinicio.
[ ] Las Signals se recuperan.
[ ] Los Children se reconcilian.
[ ] Existe Recovery Budget.
[ ] Existe protección frente a Recovery Storm.
[ ] Existe política de backups.
[ ] Los Backups están cifrados.
[ ] Los Backups tienen checksum.
[ ] Se realizan Restore Tests.
[ ] Existe Point-in-Time Recovery cuando procede.
[ ] El Restore invalida leases anteriores.
[ ] El Restore incrementa epoch.
[ ] Existe DR Plan.
[ ] El RPO está definido.
[ ] El RTO está definido.
[ ] Existe failover controlado.
[ ] Existe protección frente a split-brain.
[ ] Existe failback plan.
[ ] Se realizan DR Exercises.
[ ] Los componentes críticos tienen HA.
[ ] Existe Graceful Shutdown.
[ ] Existe Rolling Upgrade.
[ ] Existe Compatibility Matrix.
[ ] Las migraciones utilizan estrategia segura.
[ ] Los backfills tienen checkpoints.
[ ] Los Operational Modes están definidos.
[ ] Existe Emergency Stop.
[ ] Las Retention Policies están versionadas.
[ ] Existe Legal Hold.
[ ] Existe Archive.
[ ] Existe Compaction gobernada.
[ ] Existe Garbage Collection con grace period.
[ ] El GC comprueba referencias.
[ ] Existen métricas operativas.
[ ] Existen SLOs.
[ ] Las alertas tienen runbook.
[ ] Existe Capacity Planning.
[ ] Existe headroom.
[ ] Los accesos a stores están limitados.
[ ] Los restores se auditan.
[ ] Las eliminaciones se auditan.
[ ] Los Quality Gates operacionales han pasado.
```

---

# Arquitectura final de la Parte VII

```text
Executions and Jobs
        ↓
Transactional State Persistence
        ├── State Store
        ├── History Store
        ├── Queue Store
        ├── Timer Store
        ├── Signal Store
        └── Checkpoint Store
        ↓
Outbox and Inbox
        ↓
Event Publication and Consumption
        ↓
Artifact and Audit Persistence
        ↓
Operational Projections
        ↓
Failure Detection
        ↓
Recovery Engine
        ├── Reconstruct
        ├── Reconcile
        ├── Resume
        └── Reassign
        ↓
Backup and Restore
        ↓
Disaster Recovery
        ↓
Retention · Archive · Compaction · GC
        ↓
Observability · Alerts · Runbooks
        ↓
Production Operation
```

---

# Transición hacia la Parte VIII

Esta séptima parte ha definido:

- Persistence Layer;
- State Store;
- Aggregate Records;
- History Store;
- History Integrity;
- History Snapshots;
- Event Store;
- Queue Store;
- Atomic Job Claims;
- Dead Letter Queue;
- Timer Store;
- Signal Store;
- Checkpoint Store;
- Artifact Store;
- Artifact Lifecycle;
- Audit Store;
- Projection Stores;
- Transaction Model;
- Transactional Outbox;
- Inbox Pattern;
- Recovery Engine;
- Process Restart Recovery;
- Scheduler Recovery;
- Worker Recovery;
- Orphan Job Recovery;
- State Reconstruction;
- Checkpoint Resume;
- Recovery Executions;
- Timer Recovery;
- Signal Recovery;
- External Reconciliation;
- Recovery Budgets;
- Recovery Storm Protection;
- Backups;
- Restore;
- Point-in-Time Recovery;
- Restore Epoch;
- Disaster Recovery;
- RPO;
- RTO;
- Failover;
- Failback;
- DR Exercises;
- alta disponibilidad;
- Health Checks;
- Graceful Shutdown;
- Rolling Upgrades;
- Compatibility Matrix;
- Schema Migrations;
- Backfills;
- Feature Flags;
- Operational Modes;
- Retention;
- Legal Hold;
- Archive;
- Compaction;
- Garbage Collection;
- Operational Observability;
- métricas;
- SLOs;
- alertas;
- runbooks;
- Capacity Planning;
- Cost Management;
- seguridad operacional;
- diagnósticos;
- Quality Gates;
- casos de uso;
- antipatrones;
- reglas de conformidad.

La Parte VIII cerrará la especificación mediante:

- APIs del Orquestador;
- contratos externos;
- integración formal con motores;
- integración con agentes;
- Policy Enforcement;
- seguridad completa;
- auditoría avanzada;
- observabilidad end-to-end;
- SLIs, SLOs y SLAs;
- testing;
- simulación;
- chaos engineering;
- benchmarking;
- modelo de madurez;
- roadmap de implementación;
- arquitectura completa;
- conformidad final;
- checklist global;
- cierre de `ESPECIFICACION_DEL_ORQUESTADOR_DE_EJECUCION.md`.

---

# Conclusión

La arquitectura operacional convierte el modelo lógico del Orquestador en una plataforma durable, recuperable y operable en producción.

Su ciclo puede resumirse así:

```text
Persistir estado
        ↓
Conservar historial
        ↓
Publicar eventos
        ↓
Mantener Jobs y timers
        ↓
Crear checkpoints
        ↓
Detectar fallos
        ↓
Reconstruir
        ↓
Reconciliar
        ↓
Reanudar
        ↓
Respaldar
        ↓
Restaurar
        ↓
Archivar y depurar
        ↓
Observar y operar
```

El State Store mantiene el estado actual.

El History Store conserva cómo se alcanzó.

El Queue Store mantiene el trabajo pendiente.

El Timer Store preserva decisiones temporales.

El Signal Store conserva inputs asíncronos.

El Checkpoint Store permite reanudación.

El Artifact Store mantiene resultados durables.

El Audit Store preserva la gobernanza.

Outbox e Inbox garantizan mensajería confiable.

El Recovery Engine repara ejecuciones interrumpidas.

Los backups permiten restaurar.

El Disaster Recovery protege frente a pérdidas graves.

La alta disponibilidad evita puntos únicos de fallo.

Las migraciones permiten evolucionar sin romper procesos activos.

La retención controla el ciclo de vida de los datos.

El archivado reduce presión operativa.

La compaction reduce volumen sin perder semántica.

La Garbage Collection elimina recursos no necesarios de forma segura.

La observabilidad permite detectar y resolver degradaciones.

Un Orquestador operacionalmente conforme deberá poder responder:

```text
¿Dónde se conserva el estado actual?

¿Dónde se conserva el historial?

¿Cómo se evita perder eventos?

¿Cómo se deduplican mensajes?

¿Cómo se recupera un Job huérfano?

¿Cómo se reconstruye una Execution?

¿Qué checkpoint permite reanudarla?

¿Qué ocurre tras reiniciar el Scheduler?

¿Qué ocurre tras perder un Worker?

¿Qué backups existen?

¿Cuándo se probó el último restore?

¿Cuál es el RPO?

¿Cuál es el RTO?

¿Cómo se realiza un failover?

¿Cómo se evita split-brain?

¿Qué datos pueden archivarse?

¿Qué datos pueden eliminarse?

¿Qué Legal Holds existen?

¿Qué señales indican saturación?

¿Qué runbook debe ejecutarse ante una incidencia?
```

Con esta séptima parte queda formalizada la arquitectura operacional mediante la que NovaCoquinaria preservará, recuperará, restaurará, archivará y operará sus Workflows y Executions de forma durable, segura, observable y preparada para producción.

La octava y última parte cerrará la especificación definiendo los contratos externos, la integración completa, la seguridad end-to-end, la evaluación, el roadmap y la conformidad final del **Orquestador de Ejecución de NovaCoquinaria**.

---

# Parte VIII — APIs, Integración, Seguridad, Gobernanza, Observabilidad End-to-End, Testing, Chaos Engineering, Madurez y Conformidad Final del Orquestador de Ejecución

---

# Introducción

Con esta parte concluye la especificación completa del **Orquestador de Ejecución** de NovaCoquinaria.

Las partes anteriores han definido:

- modelo de ejecución;
- Workflows;
- DAG;
- Scheduler;
- Workers;
- colas;
- estados;
- eventos;
- señales;
- timers;
- retries;
- cancelación;
- concurrencia;
- persistencia;
- recuperación;
- Disaster Recovery;
- operación en producción.

La última responsabilidad consiste en definir cómo el Orquestador se relaciona con el resto del ecosistema.

Esto incluye:

- APIs;
- contratos;
- SDKs;
- integración con motores;
- integración con agentes IA;
- seguridad;
- autorización;
- auditoría;
- observabilidad extremo a extremo;
- testing;
- simulación;
- chaos engineering;
- benchmarking;
- roadmap;
- criterios de conformidad.

---

# Objetivos

Esta parte persigue:

- definir APIs públicas;
- definir APIs internas;
- formalizar contratos;
- definir SDKs;
- establecer Webhooks;
- definir Callbacks;
- formalizar Event APIs;
- establecer integración con Engine Registry;
- definir integración con Agent Framework;
- establecer integración con Knowledge Graph;
- formalizar integración con RAG Engine;
- definir integración con Policy Engine;
- establecer integración con Observability Platform;
- definir autenticación;
- establecer autorización;
- formalizar auditoría;
- definir SLIs;
- establecer SLOs;
- definir SLAs;
- formalizar testing;
- definir simulación;
- establecer Chaos Engineering;
- formalizar Benchmarking;
- definir niveles de madurez;
- establecer roadmap;
- definir conformidad global.

---

# Arquitectura global

```text
                 Client APIs
                      │
                      ▼
             Execution Gateway
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
Workflow API    Control API    Monitoring API
      │               │               │
      └───────────────┼───────────────┘
                      ▼
             Execution Orchestrator
                      │
 ┌──────────────┬─────────────┬─────────────┐
 ▼              ▼             ▼             ▼
Workers     Engine Registry   Policy     Observability
                      │
                      ▼
             Knowledge Platform
```

---

# API Philosophy

Toda API deberá ser:

- consistente;
- versionada;
- documentada;
- observable;
- segura;
- idempotente cuando corresponda;
- extensible.

---

# API Families

NovaCoquinaria define varias familias.

```text
Workflow API

Execution API

Control API

Administration API

Monitoring API

Internal API

Worker API

Engine API

Policy API
```

---

# Versionado

Toda API deberá poseer:

```text
major.minor.patch
```

---

# Compatibilidad

Cambios incompatibles únicamente podrán introducirse en:

```text
major
```

---

# Workflow API

Responsable de:

- registrar Workflows;
- consultar versiones;
- publicar nuevas versiones;
- validar definiciones.

---

# Execution API

Responsable de:

- crear Executions;
- consultar estado;
- cancelar;
- pausar;
- reanudar;
- enviar señales;
- obtener resultados.

---

# Execution Resource

```yaml
execution:
  id: EXEC-000041

  workflow:
    id: KNOWLEDGE-PUBLICATION

  status: running
```

---

# Control API

Permite:

- retry;
- compensation;
- recovery;
- override;
- terminate;
- emergency stop.

---

# Monitoring API

Permite consultar:

- métricas;
- estado;
- colas;
- Workers;
- Timers;
- eventos;
- diagnósticos.

---

# Administration API

Permite:

- registrar Engines;
- configurar Policies;
- administrar Tenants;
- gestionar cuotas.

---

# Internal APIs

Reservadas para:

- Scheduler;
- Workers;
- Recovery Engine;
- Timer Service;
- Outbox Publisher.

Nunca deberán exponerse públicamente.

---

# Worker API

Contrato mínimo:

```yaml
worker:
  capabilities:
    - embedding
    - graph
    - llm

  heartbeat: true

  leases: true
```

---

# Heartbeat API

Todo Worker deberá emitir:

```text
Heartbeat
```

de forma periódica.

---

# Engine API

Todos los motores registrados deberán implementar contratos homogéneos.

Ejemplo:

```text
Start

Status

Cancel

Resume

Validate

Health
```

---

# Policy API

Permite consultar:

- reglas;
- políticas;
- límites;
- autorizaciones.

---

# Event API

Todo evento publicado deberá poseer:

- ID;
- tipo;
- timestamp;
- Aggregate;
- correlación;
- versión.

---

# Webhooks

Podrán utilizarse para:

- Execution Completed;
- Execution Failed;
- Human Task Created;
- Artifact Published.

---

# Callback Contract

```yaml
callback:

  target:
    url: ...

  retries: 5

  timeout: PT30S
```

---

# SDKs

Podrán existir SDK oficiales para:

- Java;
- Python;
- TypeScript;
- Go.

---

# SDK Responsibilities

- autenticación;
- retries;
- serialización;
- observabilidad;
- tracing.

---

# Engine Registry Integration

El Scheduler nunca invocará motores desconocidos.

Siempre utilizará:

```text
Engine Registry
```

---

# Knowledge Graph Integration

Las Activities podrán consultar:

- nodos;
- relaciones;
- metadata;
- lineage.

---

# Retrieval Engine Integration

Permitirá:

- búsquedas;
- recuperación híbrida;
- ranking.

---

# RAG Engine Integration

Permitirá:

- generación aumentada;
- contexto;
- grounding.

---

# Agent Framework Integration

El Orquestador podrá lanzar:

- agentes;
- equipos;
- pipelines multiagente.

---

# Seguridad

Todo acceso deberá autenticarse.

---

# Authentication

Podrá soportar:

- OAuth2;
- OIDC;
- JWT;
- API Keys;
- certificados.

---

# Authorization

Modelo recomendado:

```text
RBAC

+

ABAC
```

---

# Roles

Ejemplos:

```text
Administrator

Operator

Workflow Designer

Auditor

Tenant Admin

Worker
```

---

# Least Privilege

Todo componente utilizará únicamente los permisos necesarios.

---

# Secrets

Nunca deberán almacenarse:

- en código;
- en logs;
- en History.

---

# Secret Providers

Podrán utilizarse:

- Vault;
- Secrets Manager;
- Kubernetes Secrets.

---

# Encryption

Obligatoria:

- en tránsito;
- en reposo.

---

# Auditoría

Toda acción administrativa deberá registrarse.

---

# Audit Categories

- configuración;
- despliegue;
- override;
- recovery;
- seguridad;
- publicación.

---

# Correlation IDs

Toda petición deberá generar:

```text
Correlation ID
```

---

# Trace IDs

Toda Execution deberá poseer:

```text
Trace ID
```

---

# Observabilidad End-to-End

Deberá cubrir:

```text
API

↓

Gateway

↓

Scheduler

↓

Worker

↓

Engine

↓

Artifact

↓

Result
```

---

# Logging

Todo log deberá incluir:

- Execution ID;
- Trace ID;
- Correlation ID;
- Tenant.

---

# Metrics

Mínimas:

- latency;
- throughput;
- errors;
- queue depth;
- retries;
- timers;
- workers;
- CPU;
- memoria.

---

# Distributed Tracing

Toda Activity deberá poder trazarse.

---

# Dashboards

Ejemplos:

- Scheduler;
- Workers;
- Recovery;
- Timers;
- Queues;
- Policies.

---

# SLIs

Indicadores:

- disponibilidad;
- latencia;
- throughput;
- éxito;
- recuperación.

---

# SLOs

Ejemplos:

```text
99.9 %

P95 < 500 ms
```

---

# SLAs

Definirán:

- compromisos;
- disponibilidad;
- tiempos máximos.

---

# Testing

La plataforma deberá disponer de:

- Unit Tests;
- Integration Tests;
- Contract Tests;
- Workflow Tests;
- Simulation Tests;
- Load Tests;
- Recovery Tests.

---

# Workflow Simulation

Toda Definition podrá simularse.

---

# Dry Run

Permitirá:

- validar;
- estimar;
- detectar errores.

---

# Replay Testing

Permitirá reproducir Executions históricas.

---

# Chaos Engineering

El sistema deberá probar:

- caída de Workers;
- caída de Scheduler;
- pérdida de red;
- corrupción;
- timers perdidos;
- recuperación.

---

# Chaos Scenarios

Ejemplos:

```text
Kill Scheduler

Lose Worker

Drop Events

Delay Timers

Expire Lease

Split Network
```

---

# Benchmarking

Se medirán:

- Executions/s;
- Jobs/s;
- Throughput;
- Latencia;
- Recuperación.

---

# Performance Profiles

Ejemplos:

```text
Small

Medium

Large

XL
```

---

# Escalabilidad

La arquitectura deberá soportar:

- escalado horizontal;
- multi-tenant;
- millones de Jobs.

---

# Modelo de Madurez

Nivel 1

```text
Single Node
```

---

Nivel 2

```text
HA Scheduler
```

---

Nivel 3

```text
Distributed Execution
```

---

Nivel 4

```text
Cross Region
```

---

Nivel 5

```text
Autonomous Orchestrator
```

---

# Roadmap

Fase 1

- Execution Engine
- Scheduler
- Workers

---

Fase 2

- Recovery
- Timers
- Signals

---

Fase 3

- Policies
- Quotas
- Agent Framework

---

Fase 4

- Multi Region
- Chaos
- Benchmark

---

# Compatibilidad

Toda nueva versión deberá mantener:

- APIs;
- Contracts;
- Definitions;
- History.

---

# Governance

Toda evolución deberá pasar por:

- ADR;
- revisión;
- validación;
- Quality Gates.

---

# Documentación

Toda API deberá disponer de:

- especificación;
- ejemplos;
- errores;
- contratos.

---

# Casos de uso

## Caso 1

Un cliente crea una Execution mediante la Execution API.

---

## Caso 2

Un Worker consulta el Job asignado.

---

## Caso 3

Un Scheduler recupera el estado mediante State Store.

---

## Caso 4

Un operador ejecuta Recovery desde Control API.

---

## Caso 5

Un motor LLM registra un nuevo resultado.

---

## Caso 6

Un Agent Framework lanza una subejecución.

---

## Caso 7

Una política bloquea una publicación.

---

## Caso 8

Chaos Engineering elimina un Scheduler y la plataforma continúa funcionando.

---

# Antipatrones

No deberán utilizarse:

- APIs sin versión;
- autenticación opcional;
- secretos en logs;
- Workers sin Heartbeat;
- motores no registrados;
- overrides sin auditoría;
- APIs internas públicas;
- tracing parcial;
- Chaos únicamente en producción;
- cambios sin ADR.

---

# Reglas de conformidad

Será conforme cuando:

- todas las APIs estén versionadas;
- exista autenticación;
- exista autorización;
- exista auditoría;
- exista tracing;
- existan métricas;
- existan SLOs;
- exista testing;
- exista Recovery;
- exista documentación;
- exista gobernanza.

---

# Checklist global

```text
✓ Workflow Engine

✓ Execution Engine

✓ Scheduler

✓ Worker Pools

✓ Queues

✓ Timers

✓ Signals

✓ Retry

✓ Compensation

✓ Persistence

✓ Recovery

✓ Backups

✓ Disaster Recovery

✓ Policies

✓ Security

✓ APIs

✓ SDKs

✓ Observability

✓ Testing

✓ Chaos Engineering

✓ Governance
```

---

# Arquitectura final del Orquestador

```text
Clients
    │
    ▼
Execution Gateway
    │
    ▼
Workflow APIs
Execution APIs
Control APIs
Monitoring APIs
    │
    ▼
Execution Orchestrator
    │
    ├──────── Scheduler
    ├──────── Workers
    ├──────── Recovery
    ├──────── Timers
    ├──────── Signals
    ├──────── Policies
    ├──────── Persistence
    └──────── Observability
             │
             ▼
Engine Registry
Knowledge Graph
Retrieval Engine
RAG Engine
LLM Providers
Artifact Store
Audit Store
```

---

# Conclusión

Con esta octava parte queda finalizada la especificación del **Orquestador de Ejecución de NovaCoquinaria**.

El documento define una arquitectura de nivel enterprise para la orquestación de procesos inteligentes basada en:

- ejecución determinista;
- persistencia durable;
- coordinación distribuida;
- recuperación automática;
- observabilidad completa;
- seguridad por diseño;
- integración desacoplada;
- escalabilidad horizontal;
- gobernanza y evolución controlada.

Este Orquestador constituye el núcleo operativo sobre el que podrán ejecutarse de forma fiable los procesos de ingestión, validación, recuperación de conocimiento, generación aumentada (RAG), publicación y automatización inteligente del ecosistema NovaCoquinaria.

---

# Estado del documento

```text
Documento:
ESPECIFICACION_DEL_ORQUESTADOR_DE_EJECUCION.md

Estado:
COMPLETO

Versión:
1.0.0

Estado de madurez:
Arquitectura de referencia (Enterprise)

Partes:
8 / 8

Especificación:
FINALIZADA
```

