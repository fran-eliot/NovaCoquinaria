---
id: SPEC-ENGINE-REGISTRY
titulo: Especificación del Engine Registry
tipo: especificacion
version: 1.0.0
estado: borrador
propietarios:
  - NovaCoquinaria Architecture Team
creado: 2026-08-02
ultima_revision: 2026-08-02
tags:
  - engine-registry
  - engines
  - capabilities
  - discovery
  - service-registry
  - orchestration
  - architecture
---

# Parte I — Fundamentos, arquitectura, alcance, modelo de Engine, metadatos, capacidades y contratos básicos

---

# Introducción

NovaCoquinaria dispone de múltiples motores especializados responsables de ejecutar capacidades concretas dentro de la plataforma.

Entre ellos se encuentran:

- Ingestion Engine;
- Validation Engine;
- Indexing Engine;
- Retrieval Engine;
- Reasoning Engine;
- RAG Engine;
- Knowledge Graph Engine;
- Policy Engine;
- Citation Engine;
- futuros Agent Engines;
- proveedores externos de modelos;
- motores especializados de transformación;
- servicios operativos auxiliares.

El Orquestador de Ejecución puede coordinar estos motores mediante Activities y Engine Adapters.

Sin embargo, para poder invocar un motor de forma segura y desacoplada necesita responder previamente a preguntas como:

```text
¿Qué Engines existen?

¿Qué tipo de Engine es cada uno?

¿Qué capacidades ofrece?

¿Qué versiones soporta?

¿Qué contratos implementa?

¿En qué entorno se encuentra?

¿Está disponible?

¿Está sano?

¿Qué recursos necesita?

¿Qué restricciones posee?

¿Qué tenants puede atender?

¿Qué protocolos admite?

¿Qué costes y latencias presenta?

¿Qué nivel de confianza tiene?

¿Qué instancia concreta debe seleccionarse?

¿Qué fallback existe si no está disponible?
```

Sin un componente central responsable de conservar esta información, el Orquestador podría depender de:

- configuraciones estáticas;
- URLs codificadas;
- listas manuales;
- adaptadores acoplados;
- versiones implícitas;
- capacidades supuestas;
- políticas duplicadas;
- health checks dispersos;
- reglas de routing embebidas en código.

Esto produciría:

- fuerte acoplamiento;
- dificultad para incorporar nuevos Engines;
- selección incorrecta de proveedores;
- incompatibilidades de contratos;
- fallos en tiempo de ejecución;
- rutas obsoletas;
- falta de trazabilidad;
- ausencia de gobernanza;
- dificultad para aplicar failover;
- imposibilidad de conocer el estado real del ecosistema.

Para evitarlo, NovaCoquinaria define el:

```text
Engine Registry
```

El Engine Registry será el subsistema responsable de registrar, describir, descubrir y gobernar los motores disponibles en la plataforma.

Conceptualmente:

```text
Engine Providers
        ↓
Engine Registration
        ↓
Contract Validation
        ↓
Capability Publication
        ↓
Health and Availability
        ↓
Engine Catalog
        ↓
Discovery and Selection
        ↓
Execution Orchestrator
```

El Engine Registry no ejecutará las capacidades de los motores.

Tampoco sustituirá:

- al Scheduler;
- al Orquestador;
- al Policy Engine;
- al Service Mesh;
- al sistema de colas;
- a los Engine Adapters;
- a la plataforma de observabilidad.

Su responsabilidad será mantener una representación gobernada, versionada y consultable de los Engines y sus capacidades.

---

# Objetivos

Esta especificación persigue los siguientes objetivos generales:

- definir el Engine Registry;
- establecer su posición en NovaCoquinaria;
- formalizar el concepto de Engine;
- definir Engine Types;
- definir Engine Providers;
- definir Engine Instances;
- establecer Engine Identities;
- formalizar Engine Metadata;
- definir Engine Capabilities;
- establecer Capability Contracts;
- formalizar operaciones;
- definir protocolos;
- establecer Engine Endpoints;
- formalizar versiones;
- definir compatibilidad;
- establecer estados;
- formalizar lifecycle;
- definir registro;
- definir descubrimiento;
- establecer health y availability;
- definir selección;
- preparar routing;
- permitir múltiples proveedores;
- gobernar fallbacks;
- establecer seguridad;
- formalizar trust levels;
- definir observabilidad;
- establecer auditoría;
- formalizar deprecation;
- definir Quality Gates;
- establecer reglas de conformidad;
- preparar integración con el Orquestador;
- preparar integración con Scheduler y Workers;
- preparar integración con Policy Engine;
- preparar integración con agentes.

---

# Problema que resuelve

Sin un Engine Registry, el Orquestador podría conocer los Engines mediante configuraciones como:

```yaml
retrieval_engine_url: http://retrieval-engine:8080
rag_engine_url: http://rag-engine:8080
reasoner_url: http://reasoner:8080
```

Este enfoque es insuficiente cuando existen:

- varias instancias;
- varias versiones;
- distintos proveedores;
- múltiples regiones;
- Engines internos y externos;
- capacidades opcionales;
- contratos diferentes;
- restricciones por tenant;
- cuotas;
- costes;
- modelos distintos;
- versiones en migración;
- Engines degradados;
- proveedores temporalmente indisponibles.

El Engine Registry deberá sustituir las referencias estáticas por descripciones formales.

En lugar de preguntar:

```text
¿Cuál es la URL del Retrieval Engine?
```

el sistema deberá poder preguntar:

```text
¿Qué Engine activo puede ejecutar
hybrid_retrieval@2.x,
en producción,
para TENANT-0001,
con soporte de citations,
latencia máxima de 500 ms
y clasificación internal?
```

El Registry devolverá candidatos compatibles, no una única dirección asumida.

---

# Definición

Se define el **Engine Registry** como:

> El subsistema responsable de registrar, validar, catalogar, versionar, descubrir y exponer Engines y capacidades ejecutables, manteniendo su identidad, contratos, compatibilidad, disponibilidad, estado operativo, restricciones, seguridad y metadatos de selección.

---

# Principio central

El Engine Registry deberá poder responder en todo momento:

```text
¿Qué Engines están registrados?

¿Qué Engine Types existen?

¿Qué capacidades ofrece cada Engine?

¿Qué operaciones implementa?

¿Qué versiones de contrato soporta?

¿Qué instancias están activas?

¿En qué entorno y región están desplegadas?

¿Qué protocolos utilizan?

¿Qué endpoints poseen?

¿Qué Engines son compatibles con una Activity?

¿Qué restricciones de seguridad aplican?

¿Qué tenants pueden utilizarlos?

¿Qué estado operativo presentan?

¿Qué versiones están deprecated?

¿Qué proveedor debe utilizarse?

¿Qué alternativa existe si falla?

¿Qué metadatos justifican la selección?
```

---

# Posición dentro de NovaCoquinaria

```text
                         Consumers
                             │
       ┌─────────────────────┼─────────────────────┐
       │                     │                     │
Execution Orchestrator   Scheduler           Agent Framework
       │                     │                     │
       └─────────────────────┼─────────────────────┘
                             │
                             ▼
              ═════════════════════════════
                     ENGINE REGISTRY
              ═════════════════════════════
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
 Engine Catalog      Capability Catalog     Contract Catalog
        │                    │                    │
        ├────────────────────┼────────────────────┤
        │                    │                    │
        ▼                    ▼                    ▼
Instance Registry      Health Registry      Policy Metadata
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                             ▼
               Registered Engine Ecosystem
                             │
    ┌────────────┬────────────┬────────────┬────────────┐
    ▼            ▼            ▼            ▼            ▼
Ingestion   Validation    Retrieval      RAG       Reasoner
```

---

# Alcance

El Engine Registry será responsable de:

- registrar Engine Definitions;
- registrar Engine Providers;
- registrar Engine Instances;
- validar contratos;
- mantener versiones;
- describir capacidades;
- describir operaciones;
- mantener endpoints;
- conservar protocolos;
- registrar restricciones;
- mantener estados;
- exponer información de health;
- publicar availability;
- resolver compatibilidad;
- responder consultas de descubrimiento;
- proporcionar candidatos de selección;
- soportar deprecation;
- mantener auditoría;
- emitir eventos;
- aplicar Quality Gates;
- conservar fingerprints;
- integrar políticas de uso.

---

# Fuera de alcance

El Engine Registry no será responsable de:

- ejecutar Activities;
- invocar directamente Engines por defecto;
- planificar Workflows;
- gestionar Jobs;
- balancear tráfico de red en tiempo real;
- persistir resultados de negocio;
- implementar retries de Activities;
- almacenar secretos;
- autorizar por sí solo una ejecución;
- realizar inferencias;
- validar conocimiento culinario;
- generar respuestas;
- administrar contenedores;
- sustituir un Service Mesh;
- sustituir un API Gateway;
- sustituir al Scheduler;
- sustituir al Policy Engine.

---

# Separación de responsabilidades

| Componente | Responsabilidad |
|---|---|
| Engine Registry | Describir y descubrir Engines |
| Orquestador | Coordinar procesos |
| Scheduler | Programar Jobs |
| Engine Adapter | Traducir e invocar Engines |
| Engine | Ejecutar capacidad especializada |
| Policy Engine | Autorizar y limitar uso |
| Service Mesh | Gestionar tráfico de red |
| Observability Platform | Medir salud y rendimiento |
| Secrets Manager | Custodiar credenciales |
| API Gateway | Exponer APIs y aplicar controles de entrada |

---

# Registry frente a Service Discovery

El Engine Registry y un sistema de Service Discovery podrán colaborar, pero no serán equivalentes.

---

# Service Discovery

Responde principalmente:

```text
¿Qué instancias de red están disponibles?
```

---

# Engine Registry

Responde:

```text
¿Qué Engine representa esta instancia?

¿Qué capacidad ofrece?

¿Qué versión implementa?

¿Qué contrato utiliza?

¿Qué restricciones posee?

¿Qué nivel de confianza tiene?

¿Es compatible con esta Activity?
```

---

# Relación recomendada

```text
Engine Registry
        ↓
Engine Instance Metadata
        ↓
Service Discovery
        ↓
Network Endpoint Resolution
```

El Registry podrá almacenar endpoints directamente en implementaciones simples.

En arquitecturas avanzadas podrá conservar referencias lógicas hacia Service Discovery.

---

# Registry frente a Engine Adapter Registry

El **Engine Registry** registra motores y capacidades.

El **Engine Adapter Registry** registra adaptadores de integración.

Ejemplo:

```text
Engine:
RETRIEVAL-ENGINE-PRIMARY@2.1.0
```

```text
Adapter:
EXEC-ADAPTER-RETRIEVAL@1.4.0
```

Un mismo Adapter podrá ser compatible con varias versiones de Engine.

Un Engine podrá admitir varios protocolos y, por tanto, varios Adapters.

---

# Registry frente a Capability Registry

El Engine Registry contendrá o integrará un catálogo de capacidades.

Conceptualmente:

```text
Capability
        ↓
implemented_by
        ↓
Engine Definition
        ↓
deployed_as
        ↓
Engine Instance
```

La Capability no deberá confundirse con el Engine.

---

# Ejemplo

```text
Capability:
hybrid_retrieval
```

puede ser implementada por:

```text
RETRIEVAL-ENGINE-INTERNAL
RETRIEVAL-ENGINE-EXPERIMENTAL
EXTERNAL-SEARCH-PROVIDER
```

---

# Principios arquitectónicos

Toda implementación deberá respetar los siguientes principios.

---

## Identidad estable

Todo Engine deberá poseer una identidad independiente de:

- hostname;
- IP;
- pod;
- endpoint;
- deployment.

---

## Definición e instancia separadas

La definición describe el producto o motor.

La instancia representa un despliegue concreto.

---

## Capacidades explícitas

No deberán inferirse capacidades por el nombre del Engine.

---

## Contratos versionados

Toda operación deberá referenciar schemas o contratos concretos.

---

## Compatibilidad declarada

No deberá suponerse compatibilidad entre versiones.

---

## Registro validado

Ningún Engine deberá aparecer como utilizable sin superar validación.

---

## Estados explícitos

Un Engine deberá declarar lifecycle y estado operativo.

---

## Descubrimiento consultivo

El Registry devolverá candidatos compatibles.

La selección final podrá corresponder a:

- Orquestador;
- Scheduler;
- Router;
- Policy Engine.

---

## No endpoint hardcoded

Los consumidores deberán resolver Engines mediante identificadores o consultas.

---

## Seguridad por diseño

El Registry deberá conservar:

- clasificación;
- tenant scope;
- trust level;
- protocols;
- authentication requirements.

---

## Metadatos mínimos

No deberá convertirse en un repositorio arbitrario de configuración.

---

## Fuente canónica definida

Los datos de registro deberán tener un owner y origen conocido.

---

## Registro auditable

Altas, cambios, deprecaciones y retiradas deberán quedar registradas.

---

## Versiones inmutables

Una versión publicada de Engine Definition no deberá modificarse en lugar.

---

## Instancias efímeras permitidas

Las Engine Instances podrán aparecer y desaparecer sin alterar la identidad de la Definition.

---

## Health separado de lifecycle

Un Engine puede estar:

```text
active
```

pero una instancia concreta:

```text
unhealthy
```

---

## Availability contextual

La disponibilidad podrá depender de:

- tenant;
- región;
- clasificación;
- operación;
- cuota;
- policy.

---

## Compatibilidad con múltiples proveedores

Una Capability podrá tener varias implementaciones.

---

## No selección opaca

Toda selección deberá poder justificarse mediante metadatos.

---

## No confianza implícita

Todo Engine deberá declarar su trust level y provenance.

---

## Fingerprints

Las definiciones y contratos deberán poder verificarse.

---

## Evolución gobernada

El lifecycle deberá incluir:

- experimental;
- active;
- deprecated;
- retired.

---

# Arquitectura conceptual del Engine Registry

```text
┌───────────────────────────────────────────────┐
│              Registration Gateway             │
│                                               │
│ Auth · Validation · Policy · Ownership        │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                Engine Catalog                 │
│                                               │
│ Definitions · Providers · Instances           │
└──────────────────────┬────────────────────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
   Capabilities     Contracts     Versions
          │            │            │
          └────────────┼────────────┘
                       ▼
┌───────────────────────────────────────────────┐
│            Operational Registry               │
│                                               │
│ Health · Availability · Endpoints · Load      │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Discovery and Matching            │
│                                               │
│ Query · Filter · Compatibility · Candidates   │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│           Consumers and Integrations           │
│                                               │
│ Orchestrator · Scheduler · Agents · APIs       │
└───────────────────────────────────────────────┘
```

---

# Componentes principales

El Engine Registry podrá dividirse en:

```text
Registration Gateway
Engine Catalog
Provider Catalog
Instance Registry
Capability Catalog
Operation Catalog
Contract Catalog
Version Resolver
Compatibility Resolver
Endpoint Resolver
Health Registry
Availability Resolver
Discovery Engine
Selection Candidate Builder
Policy Metadata Resolver
Registry Event Publisher
Registry Audit Writer
Registry Validator
```

---

# Registration Gateway

Punto de entrada para altas y modificaciones.

Responsabilidades:

- autenticar registrante;
- autorizar operación;
- validar ownership;
- validar schema;
- comprobar duplicados;
- aplicar políticas;
- crear Registration Request;
- emitir auditoría.

---

# Engine Catalog

Almacena Engine Definitions versionadas.

---

# Provider Catalog

Almacena organizaciones o componentes responsables de proporcionar Engines.

---

# Instance Registry

Mantiene despliegues concretos.

---

# Capability Catalog

Mantiene capacidades normalizadas y versionadas.

---

# Operation Catalog

Mantiene operaciones invocables.

---

# Contract Catalog

Mantiene contratos de entrada, salida y error.

---

# Version Resolver

Resuelve versiones compatibles.

---

# Compatibility Resolver

Determina compatibilidad entre:

- Engine;
- Capability;
- Operation;
- Adapter;
- Activity;
- Contract;
- Environment.

---

# Endpoint Resolver

Resuelve endpoints o referencias lógicas.

---

# Health Registry

Mantiene observaciones de salud.

---

# Availability Resolver

Determina si una instancia puede utilizarse en un contexto específico.

---

# Discovery Engine

Responde consultas sobre Engines.

---

# Selection Candidate Builder

Devuelve una lista estructurada de candidatos.

No deberá ejecutar por sí mismo el routing final salvo perfil simplificado.

---

# Registry Event Publisher

Publica eventos de cambios.

---

# Registry Audit Writer

Conserva operaciones administrativas.

---

# Registry Validator

Ejecuta validaciones estructurales, semánticas, operativas y de seguridad.

---

# Modelo conceptual

```text
Engine Type
        ↓
Engine Definition
        ↓
Engine Provider
        ↓
Engine Version
        ↓
Engine Instance
        ↓
Capability Implementation
        ↓
Operation
        ↓
Contract
        ↓
Endpoint
```

---

# Engine

Se define un **Engine** como:

> Un componente especializado que implementa una o varias capacidades ejecutables mediante contratos, operaciones y protocolos formalmente declarados.

Un Engine podrá ser:

- un servicio independiente;
- un componente local;
- un modelo;
- un proveedor externo;
- una librería;
- un cluster;
- una plataforma especializada;
- un conjunto de Workers homogéneos.

---

# Engine ID

Formato recomendado:

```text
ENGINE-XXXXXX
```

Ejemplos:

```text
ENGINE-INGESTION-PRIMARY
ENGINE-VALIDATION-PRIMARY
ENGINE-INDEXING-PRIMARY
ENGINE-RETRIEVAL-HYBRID
ENGINE-RAG-PRIMARY
ENGINE-REASONER-SYMBOLIC
ENGINE-KNOWLEDGE-GRAPH
```

---

# Engine Type

Un **Engine Type** representa una categoría funcional.

Formato recomendado:

```text
ENGINE-TYPE-XXXXXX
```

---

# Tipos iniciales

```text
ingestion
validation
transformation
knowledge_graph
indexing
retrieval
ranking
reranking
citation
reasoning
rag
generation
embedding
classification
policy
agent
memory
notification
audit
storage
external_provider
utility
```

---

# Ingestion Engine

Responsable de:

- recibir;
- parsear;
- normalizar;
- transformar documentos.

---

# Validation Engine

Responsable de:

- validar estructura;
- validar semántica;
- ejecutar Quality Gates;
- generar diagnósticos.

---

# Knowledge Graph Engine

Responsable de:

- entidades;
- relaciones;
- Statements;
- paths;
- subgrafos;
- snapshots.

---

# Indexing Engine

Responsable de:

- unidades indexables;
- chunking;
- embeddings;
- índices;
- publicación de snapshots.

---

# Retrieval Engine

Responsable de:

- Query Understanding;
- planificación;
- recuperación;
- ranking;
- evidencia;
- context packing.

---

# Ranking Engine

Responsable de:

- score normalization;
- fusion;
- ranking;
- diversificación.

Podrá formar parte del Retrieval Engine o registrarse independientemente.

---

# Citation Engine

Responsable de:

- resolver citas;
- validar spans;
- reconstruir provenance.

---

# Reasoning Engine

Responsable de:

- inferencia;
- reglas;
- deducción;
- explicación;
- resolución de Statements.

---

# RAG Engine

Responsable de:

- consumo de contexto;
- generación grounded;
- citas;
- políticas de no respuesta.

---

# Generation Engine

Representa un proveedor o motor generativo.

---

# Embedding Engine

Genera representaciones vectoriales.

---

# Policy Engine

Evalúa políticas.

---

# Agent Engine

Ejecuta planes o agentes controlados.

---

# Utility Engine

Ofrece capacidades auxiliares.

Ejemplos:

- conversión;
- compresión;
- extracción;
- traducción;
- renderizado.

---

# External Provider

Representa una capacidad proporcionada por un tercero.

---

# Engine Type Contract

```yaml
engine_type:
  id: ENGINE-TYPE-RETRIEVAL

  version: 1.0.0

  name: Retrieval Engine

  category: knowledge_access

  expected_capabilities:
    - query_understanding
    - lexical_retrieval
    - vector_retrieval
    - hybrid_retrieval

  governance:
    owner: NovaCoquinaria Architecture Team
```

---

# Engine Definition

Una **Engine Definition** representa la descripción lógica, estable y versionada de un Engine.

Formato recomendado:

```text
ENGINE-DEF-XXXXXX
```

---

# Contrato

```yaml
engine_definition:
  id: ENGINE-DEF-RETRIEVAL-HYBRID
  version: 2.1.0
  status: active

  engine:
    id: ENGINE-RETRIEVAL-HYBRID

  type:
    id: ENGINE-TYPE-RETRIEVAL
    version: 1.0.0

  metadata:
    name: Hybrid Retrieval Engine
    description: >
      Motor de recuperación lexical, vectorial,
      estructurada y basada en grafo.

  provider:
    id: ENGINE-PROVIDER-NOVACOQUINARIA

  capabilities:
    - CAP-HYBRID-RETRIEVAL@2.0.0
    - CAP-STATEMENT-RETRIEVAL@1.0.0
    - CAP-GRAPH-RETRIEVAL@1.1.0

  operations:
    - ENGINE-OP-RETRIEVE@2.0.0
    - ENGINE-OP-EXPLAIN@1.0.0
    - ENGINE-OP-HEALTH@1.0.0

  lifecycle:
    status: active

  compatibility:
    minimum_registry_version: 1.0.0

  fingerprint:
    algorithm: sha256
    value: ...
```

---

# Engine Definition Immutability

Una versión publicada no deberá modificarse.

Todo cambio contractual deberá producir una nueva versión.

---

# Engine Definition Status

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

# Draft

En preparación.

---

# Validating

Pendiente de validación.

---

# Experimental

Disponible para:

- sandbox;
- pruebas;
- tenants autorizados;
- shadow traffic.

---

# Active

Disponible para selección normal.

---

# Deprecated

Sigue disponible, pero no se recomienda para nuevas integraciones.

---

# Retired

No deberá seleccionarse.

---

# Blocked

Temporalmente prohibido por:

- seguridad;
- incidente;
- incompatibilidad;
- policy.

---

# Invalid

La definición no cumple contratos.

---

# Engine Family

Una **Engine Family** agrupa variantes del mismo dominio funcional.

Formato recomendado:

```text
ENGINE-FAMILY-XXXXXX
```

---

# Ejemplo

```yaml
engine_family:
  id: ENGINE-FAMILY-RETRIEVAL

  members:
    - ENGINE-RETRIEVAL-LEXICAL
    - ENGINE-RETRIEVAL-HYBRID
    - ENGINE-RETRIEVAL-GRAPH
```

---

# Uso

Permite:

- routing;
- fallback;
- comparación;
- migración;
- deprecation.

---

# Engine Variant

Una variante podrá representar:

- precisión;
- coste;
- latencia;
- modalidad;
- proveedor;
- entorno.

Ejemplo:

```text
ENGINE-RAG-FAST
ENGINE-RAG-STANDARD
ENGINE-RAG-HIGH-QUALITY
```

---

# Engine Provider

Un **Engine Provider** representa el propietario técnico u organización responsable.

Formato recomendado:

```text
ENGINE-PROVIDER-XXXXXX
```

---

# Tipos

```text
internal_team
internal_platform
external_vendor
open_source
managed_service
local_component
community
```

---

# Contrato

```yaml
engine_provider:
  id: ENGINE-PROVIDER-NOVACOQUINARIA

  type: internal_platform

  name: NovaCoquinaria Platform

  ownership:
    technical_owner: NovaCoquinaria Architecture Team
    operational_owner: NovaCoquinaria Platform Operations

  trust:
    level: trusted_internal

  status: active
```

---

# Provider Responsibilities

- mantener Engine;
- publicar versiones;
- declarar compatibilidad;
- responder incidentes;
- mantener contratos;
- proporcionar soporte;
- cumplir seguridad;
- comunicar deprecation.

---

# Provider Status

```text
active
restricted
suspended
deprecated
retired
```

---

# External Provider

Deberá declarar adicionalmente:

- región;
- jurisdicción;
- tratamiento de datos;
- SLA;
- términos;
- límites;
- certificaciones;
- subprocesadores;
- retention;
- model training policy.

---

# Engine Instance

Una **Engine Instance** representa un despliegue concreto y utilizable de una Engine Definition.

Formato recomendado:

```text
ENGINE-INSTANCE-XXXXXX
```

---

# Ejemplo

```yaml
engine_instance:
  id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  environment:
    id: production

  region:
    id: eu-west

  deployment:
    id: DEPLOYMENT-RETRIEVAL-20260802-001

  endpoints:
    - ENGINE-ENDPOINT-RETRIEVAL-HTTP-001

  lifecycle:
    state: registered

  operational:
    health: healthy
    availability: available

  capacity:
    maximum_concurrency: 100
    current_load: 23

  registered_at: 2026-08-02T20:00:00Z
```

---

# Definition vs Instance

```text
Engine Definition
=
qué es y qué implementa
```

```text
Engine Instance
=
dónde y en qué estado está desplegado
```

---

# Instance Identity

No deberá basarse únicamente en:

- hostname;
- pod name;
- IP;
- process ID.

Podrá corresponder a:

- deployment lógico;
- réplica;
- cluster;
- endpoint group;
- provider account.

---

# Instance Granularity

La implementación deberá decidir si una Engine Instance representa:

```text
un proceso
```

```text
una réplica
```

```text
un deployment
```

```text
un cluster
```

La semántica deberá ser única y documentada.

---

# Recomendación inicial

Representar como Engine Instance una unidad de routing lógico.

Las réplicas internas podrán gestionarse mediante Service Discovery.

---

# Engine Instance Lifecycle

Estados iniciales:

```text
discovered
registering
registered
validating
starting
available
degraded
draining
unavailable
maintenance
quarantined
deregistering
deregistered
failed
```

---

# Discovered

La instancia ha sido detectada, pero no registrada.

---

# Registering

Se está validando.

---

# Registered

Existe en el Registry, pero no necesariamente está disponible.

---

# Validating

Se comprueban contratos, health y seguridad.

---

# Starting

Está iniciando.

---

# Available

Puede recibir trabajo.

---

# Degraded

Puede recibir solo ciertos tipos de trabajo o bajo restricciones.

---

# Draining

No acepta nuevas operaciones.

---

# Unavailable

No deberá seleccionarse.

---

# Maintenance

Excluida temporalmente.

---

# Quarantined

Aislada por riesgo de:

- seguridad;
- outputs inválidos;
- incompatibilidad;
- comportamiento anómalo.

---

# Deregistering

Está retirándose.

---

# Deregistered

Ya no participa.

---

# Failed

Se ha detectado fallo persistente.

---

# Lifecycle State vs Health State

Ejemplo:

```text
lifecycle = available
health = degraded
```

El Availability Resolver decidirá si continúa siendo seleccionable.

---

# Engine Instance Revision

Toda modificación deberá utilizar control de revisión.

```yaml
revision: 18
```

---

# Engine Metadata

Los metadatos describen propiedades de un Engine.

---

# Categorías

```text
identity
ownership
functional
operational
deployment
security
compliance
cost
performance
compatibility
governance
```

---

# Identity Metadata

- ID;
- name;
- type;
- family;
- version;
- provider.

---

# Ownership Metadata

- technical owner;
- operational owner;
- security owner;
- support contact.

---

# Functional Metadata

- capabilities;
- operations;
- limitations;
- modalities;
- languages;
- domains.

---

# Operational Metadata

- environment;
- region;
- endpoints;
- health;
- capacity;
- limits.

---

# Security Metadata

- trust level;
- classification;
- authentication;
- encryption;
- tenant isolation.

---

# Compliance Metadata

- data residency;
- retention;
- certifications;
- processing restrictions.

---

# Cost Metadata

- fixed cost;
- per request;
- per token;
- per second;
- resource units.

---

# Performance Metadata

- expected latency;
- throughput;
- concurrency;
- batch support;
- streaming support.

---

# Compatibility Metadata

- API versions;
- schemas;
- adapters;
- Activities;
- protocols.

---

# Governance Metadata

- lifecycle;
- deprecation;
- replacement;
- review date;
- owner.

---

# Metadata Contract

```yaml
engine_metadata:
  identity:
    engine_id: ENGINE-RETRIEVAL-HYBRID
    definition_version: 2.1.0

  ownership:
    technical_owner: TEAM-KNOWLEDGE-PLATFORM
    operational_owner: TEAM-PLATFORM-OPS

  functional:
    domains:
      - culinary_knowledge

    languages:
      - es
      - en
      - fr

  operational:
    environments:
      - production
      - staging

  security:
    trust_level: trusted_internal
    maximum_classification: internal

  governance:
    review_date: 2026-11-01
```

---

# Metadata Schema

Deberá estar versionado.

---

# Required Metadata

Todo Engine deberá declarar como mínimo:

- Engine ID;
- Definition ID;
- version;
- type;
- provider;
- owner;
- lifecycle;
- capabilities;
- operations;
- contracts;
- trust level;
- environments;
- compatibility.

---

# Optional Metadata

Podrá incluir:

- cost;
- benchmarks;
- affinities;
- labels;
- documentation;
- model card;
- service level;
- energy profile.

---

# Labels

Podrán utilizarse para descubrimiento auxiliar.

Ejemplos:

```yaml
labels:
  latency: low
  quality: high
  modality: text
  deployment: internal
```

---

# No lógica crítica basada solo en labels

Las propiedades importantes deberán ser campos tipados.

---

# Engine Descriptor

Un **Engine Descriptor** será la representación consolidada que podrán consumir los clientes del Registry.

Formato recomendado:

```text
ENGINE-DESCRIPTOR-XXXXXX
```

---

# Contrato

```yaml
engine_descriptor:
  id: ENGINE-DESCRIPTOR-RETRIEVAL-HYBRID-2.1.0

  definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  type:
    id: ENGINE-TYPE-RETRIEVAL

  provider:
    id: ENGINE-PROVIDER-NOVACOQUINARIA

  capabilities:
    - CAP-HYBRID-RETRIEVAL@2.0.0

  operations:
    - ENGINE-OP-RETRIEVE@2.0.0

  trust:
    level: trusted_internal

  lifecycle:
    status: active

  instances:
    available: 3
    degraded: 1
```

---

# Capability

Una **Capability** representa una función abstracta que uno o varios Engines pueden implementar.

Formato recomendado:

```text
CAP-XXXXXX
```

---

# Ejemplos

```text
CAP-DOCUMENT-INGESTION
CAP-SEMANTIC-VALIDATION
CAP-EMBEDDING-GENERATION
CAP-HYBRID-RETRIEVAL
CAP-GRAPH-RETRIEVAL
CAP-CLAIM-VERIFICATION
CAP-RAG-GENERATION
CAP-SYMBOLIC-REASONING
CAP-CITATION-RESOLUTION
```

---

# Capability Definition

```yaml
capability:
  id: CAP-HYBRID-RETRIEVAL

  version: 2.0.0

  name: Hybrid Retrieval

  description: >
    Recupera candidatos combinando búsqueda lexical,
    vectorial y estructurada.

  category: retrieval

  operations:
    - retrieve
    - explain

  contract:
    input: HYBRID-RETRIEVAL-REQUEST@2.0.0
    output: HYBRID-RETRIEVAL-RESULT@2.0.0

  characteristics:
    deterministic: partially
    side_effecting: false
    streaming_supported: true
```

---

# Capability vs Operation

```text
Capability
=
qué función general ofrece el Engine
```

```text
Operation
=
qué llamada concreta puede ejecutarse
```

---

# Ejemplo

Capability:

```text
CAP-KNOWLEDGE-VALIDATION
```

Operations:

```text
validate_document
validate_graph
validate_snapshot
explain_diagnostics
```

---

# Capability Categories

```text
ingestion
validation
transformation
indexing
retrieval
ranking
reasoning
generation
policy
storage
observability
administration
```

---

# Capability Characteristics

Toda Capability podrá declarar:

```text
read_only
side_effecting
idempotent
deterministic
streaming
batch
interactive
cancellable
checkpointable
reconcilable
```

---

# Capability Contract

```yaml
capability_characteristics:
  read_only: true
  side_effecting: false
  idempotent: true
  deterministic: false
  streaming: true
  cancellable: true
```

---

# Capability Requirements

Podrá requerir:

- GPU;
- Knowledge Graph;
- Vector Index;
- external provider;
- language;
- model;
- classification;
- region.

---

# Capability Constraint

```yaml
capability_constraint:
  type: required_resource

  resource:
    id: VECTOR-INDEX

  minimum_version: 2.0.0
```

---

# Capability Implementation

Una **Capability Implementation** relaciona una Capability con un Engine.

Formato recomendado:

```text
CAP-IMPL-XXXXXX
```

---

# Contrato

```yaml
capability_implementation:
  id: CAP-IMPL-HYBRID-RETRIEVAL-ENGINE-RETRIEVAL

  capability:
    id: CAP-HYBRID-RETRIEVAL
    version: 2.0.0

  engine_definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  operation:
    id: ENGINE-OP-RETRIEVE
    version: 2.0.0

  conformance:
    status: passed

  limitations:
    maximum_query_length: 8192
    maximum_results: 1000
```

---

# Implementation Conformance

Deberá comprobar:

- input contract;
- output contract;
- error contract;
- semantics;
- limits;
- security;
- cancellation;
- idempotency.

---

# Capability Profile

Una misma Capability podrá ofrecer perfiles.

Ejemplo:

```text
fast
standard
high_quality
low_cost
strict
experimental
```

---

# Capability Profile Contract

```yaml
capability_profile:
  id: CAP-PROFILE-HYBRID-RETRIEVAL-FAST

  capability:
    id: CAP-HYBRID-RETRIEVAL
    version: 2.0.0

  objectives:
    latency_p95_ms: 300

  tradeoffs:
    reduced_reranking: true
    maximum_candidates: 100
```

---

# Capability Versioning

Las Capabilities deberán versionarse de forma independiente de los Engines.

Un Engine podrá actualizarse sin cambiar Capability Contract cuando no altere la semántica pública.

---

# Capability Compatibility

Valores:

```text
backward
forward
full
none
```

---

# Capability Alias

Podrá existir un alias lógico.

Ejemplo:

```text
hybrid_retrieval.standard
```

El alias deberá resolver hacia una versión gobernada.

---

# No alias `latest` no controlado

---

# Engine Operation

Una **Engine Operation** representa una operación invocable.

Formato recomendado:

```text
ENGINE-OP-XXXXXX
```

---

# Contrato

```yaml
engine_operation:
  id: ENGINE-OP-RETRIEVE

  version: 2.0.0

  capability:
    id: CAP-HYBRID-RETRIEVAL
    version: 2.0.0

  name: retrieve

  contracts:
    request:
      id: HYBRID-RETRIEVAL-REQUEST
      version: 2.0.0

    response:
      id: HYBRID-RETRIEVAL-RESULT
      version: 2.0.0

    error:
      id: ENGINE-ERROR
      version: 1.0.0

  semantics:
    side_effecting: false
    idempotent: true
    cancellable: true
    streaming: true

  timeouts:
    recommended: PT2S
    maximum: PT30S
```

---

# Operation Types

```text
command
query
stream
job
callback
health
administrative
```

---

# Query Operation

No produce side effects funcionales.

---

# Command Operation

Produce efectos.

---

# Job Operation

Inicia una operación asíncrona.

---

# Stream Operation

Produce resultados parciales.

---

# Callback Operation

Recibe una notificación del Engine.

---

# Health Operation

Informa de estado.

---

# Administrative Operation

Solo para administración autorizada.

---

# Operation Semantics

Toda operación deberá declarar:

- sync o async;
- idempotencia;
- side effects;
- cancelabilidad;
- retryability;
- reconciliation;
- streaming;
- batch;
- timeout;
- security.

---

# Asynchronous Operation

Podrá implementar:

```text
start
status
cancel
result
```

---

# Asynchronous Operation Contract

```yaml
asynchronous_operation:
  start: ENGINE-OP-BUILD-INDEX-START@1.0.0
  status: ENGINE-OP-BUILD-INDEX-STATUS@1.0.0
  cancel: ENGINE-OP-BUILD-INDEX-CANCEL@1.0.0
  result: ENGINE-OP-BUILD-INDEX-RESULT@1.0.0
```

---

# Reconciliation Operation

Las operaciones con side effects deberán ofrecer, cuando sea posible:

```text
get_status_by_operation_id
```

o:

```text
get_result_by_idempotency_key
```

---

# Engine Contract

Un **Engine Contract** describe formalmente la interfaz de un Engine u Operation.

Formato recomendado:

```text
ENGINE-CONTRACT-XXXXXX
```

---

# Tipos de contrato

```text
request
response
error
event
callback
stream_item
health
metadata
```

---

# Contrato básico

```yaml
engine_contract:
  id: ENGINE-CONTRACT-HYBRID-RETRIEVAL-REQUEST

  version: 2.0.0

  type: request

  schema:
    format: json_schema
    reference: HYBRID-RETRIEVAL-REQUEST@2.0.0

  compatibility:
    policy: backward
```

---

# Contract Registry

Los contratos deberán almacenarse en un catálogo versionado.

---

# Request Contract

Deberá declarar:

- required fields;
- types;
- constraints;
- security context;
- idempotency;
- correlation;
- deadlines;
- options.

---

# Response Contract

Deberá declarar:

- status;
- outputs;
- diagnostics;
- references;
- timing;
- provenance;
- partial semantics.

---

# Error Contract

Deberá declarar:

- code;
- category;
- severity;
- retryability;
- message;
- details;
- correlation;
- diagnostics.

---

# Engine Error

```yaml
engine_error:
  code: RETRIEVAL_INDEX_UNAVAILABLE
  category: dependency
  severity: error
  retryable: true

  message: >
    El índice vectorial no se encuentra disponible.

  correlation_id: CORR-000041
```

---

# Error Categories

```text
validation
authorization
authentication
policy
capacity
timeout
dependency
compatibility
contract
internal
external
unknown
```

---

# No errores libres sin código

---

# Partial Result Contract

Las operaciones que permitan resultados parciales deberán declararlo.

```yaml
partial_result:
  supported: true

  minimum_guarantees:
    schema_valid: true
    diagnostics_present: true
```

---

# Contract Fingerprint

Todo contrato deberá disponer de fingerprint.

---

# Contract Compatibility

No deberá basarse solo en el número de versión.

Deberá evaluarse:

- fields;
- required status;
- types;
- enums;
- semantics;
- defaults;
- error behavior.

---

# Protocol

Un **Engine Protocol** representa el mecanismo de comunicación.

Valores iniciales:

```text
local
http
grpc
event
queue
websocket
stream
batch_file
provider_sdk
database
```

---

# Protocol Contract

```yaml
engine_protocol:
  type: http

  version: 1.1

  serialization: json

  security:
    tls: required
    authentication: oauth2_client_credentials

  tracing:
    propagation: w3c
```

---

# Local Protocol

Invocación dentro del mismo proceso.

---

# HTTP

Adecuado para APIs síncronas.

---

# gRPC

Adecuado para contratos tipados y streaming.

---

# Event

Adecuado para comunicación asíncrona.

---

# Queue

Adecuado para Jobs.

---

# Provider SDK

Adecuado para proveedores externos.

---

# Batch File

Adecuado para intercambios voluminosos no interactivos.

---

# Protocol Independence

Una Capability no deberá depender conceptualmente de un protocolo.

---

# Engine Endpoint

Un **Engine Endpoint** representa una ubicación o referencia invocable.

Formato recomendado:

```text
ENGINE-ENDPOINT-XXXXXX
```

---

# Contrato

```yaml
engine_endpoint:
  id: ENGINE-ENDPOINT-RETRIEVAL-HTTP-001

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  protocol:
    type: http
    version: 1.1

  address:
    service_ref: SERVICE-RETRIEVAL-PRODUCTION

  operations:
    - ENGINE-OP-RETRIEVE@2.0.0
    - ENGINE-OP-EXPLAIN@1.0.0

  security:
    authentication_profile: AUTH-PROFILE-INTERNAL-SERVICE
    tls_profile: TLS-PROFILE-INTERNAL

  status: active
```

---

# Endpoint Address

Deberá preferir referencias lógicas.

Ejemplo:

```text
service_ref
```

sobre direcciones físicas.

---

# Dirección física

Podrá almacenarse en entornos simples, pero no deberá convertirse en identidad del Engine.

---

# Endpoint Types

```text
primary
secondary
read
write
stream
callback
administrative
health
```

---

# Endpoint Scope

Podrá limitarse por:

- operación;
- tenant;
- región;
- clasificación;
- environment;
- protocol.

---

# Endpoint Status

```text
active
degraded
draining
inactive
blocked
```

---

# Endpoint Priority

Podrá utilizarse como hint, no como única regla.

---

# Endpoint Weight

```yaml
routing_weight: 80
```

---

# Engine Version

La versión del Engine representa la versión de implementación y contratos declarados.

---

# Version Dimensions

Podrán distinguirse:

```text
engine_version
capability_version
operation_version
contract_version
adapter_version
deployment_version
model_version
```

---

# No usar una única versión para todo

---

# Engine Version Record

```yaml
engine_version:
  engine:
    id: ENGINE-RETRIEVAL-HYBRID

  version: 2.1.0

  capabilities:
    CAP-HYBRID-RETRIEVAL: 2.0.0
    CAP-GRAPH-RETRIEVAL: 1.1.0

  contracts:
    HYBRID-RETRIEVAL-REQUEST: 2.0.0
    HYBRID-RETRIEVAL-RESULT: 2.0.0

  implementation:
    build: 2026.08.02.41
```

---

# Semantic Versioning

Se recomienda utilizar:

```text
MAJOR.MINOR.PATCH
```

---

# Major

Cambio incompatible.

---

# Minor

Nueva capacidad compatible.

---

# Patch

Corrección compatible.

---

# Model Version

Un Engine basado en modelos deberá declarar además:

- model ID;
- model version;
- weights version;
- tokenizer;
- provider;
- deployment revision.

---

# Version Pinning

Las ejecuciones reproducibles deberán poder fijar:

```text
Engine Definition
+
Capability Version
+
Operation Version
+
Contract Version
```

---

# Version Range

Una Activity podrá declarar:

```text
2.x
```

solo cuando la compatibilidad haya sido validada.

---

# Exact Version

Recomendada para:

- producción crítica;
- replay;
- auditoría;
- benchmarks.

---

# Engine Compatibility

La compatibilidad deberá evaluarse en distintas dimensiones.

---

# Dimensiones

```text
functional
contract
protocol
adapter
security
environment
data
model
operational
```

---

# Functional Compatibility

La Capability requerida está implementada.

---

# Contract Compatibility

Inputs y outputs son compatibles.

---

# Protocol Compatibility

El consumidor puede comunicarse.

---

# Adapter Compatibility

Existe un Adapter compatible.

---

# Security Compatibility

El Engine puede procesar el nivel de clasificación.

---

# Environment Compatibility

Está permitido en el entorno.

---

# Data Compatibility

Admite:

- schema;
- language;
- format;
- snapshot;
- modality.

---

# Model Compatibility

Admite el modelo o versión requerida.

---

# Operational Compatibility

Cumple:

- latencia;
- capacidad;
- streaming;
- timeout;
- region.

---

# Compatibility Record

```yaml
engine_compatibility:
  consumer:
    activity: ACT-RUN-RETRIEVAL@2.0.0

  candidate:
    engine_definition: ENGINE-DEF-RETRIEVAL-HYBRID@2.1.0

  dimensions:
    functional: compatible
    contract: compatible
    protocol: compatible
    adapter: compatible
    security: compatible
    environment: compatible
    operational: compatible

  result: compatible
```

---

# Compatibility States

```text
compatible
compatible_with_adapter
compatible_with_degradation
incompatible
unknown
```

---

# Unknown Compatibility

No deberá seleccionarse para producción crítica salvo policy explícita.

---

# Engine Lifecycle

El lifecycle completo de un Engine podrá representarse así:

```text
Proposed
    ↓
Draft
    ↓
Validating
    ↓
Experimental
    ↓
Active
    ↓
Deprecated
    ↓
Retired
```

Estados alternativos:

```text
Blocked
Suspended
Invalid
```

---

# Proposed

Existe una propuesta, pero todavía no una Definition utilizable.

---

# Draft

La definición está siendo preparada.

---

# Validating

Se evalúan contratos y conformance.

---

# Experimental

Uso limitado.

---

# Active

Uso general autorizado.

---

# Deprecated

Permanece disponible para migración.

---

# Retired

No se utiliza.

---

# Lifecycle Contract

```yaml
engine_lifecycle:
  engine_definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  state: active

  activated_at: 2026-08-02T20:00:00Z

  review:
    next_review_at: 2026-11-01T00:00:00Z
```

---

# Lifecycle Transition

Toda transición deberá:

- estar autorizada;
- estar auditada;
- cumplir Quality Gates;
- emitir evento;
- declarar razón.

---

# Deprecation

Una Definition deprecated deberá declarar:

- fecha;
- razón;
- replacement;
- migration guidance;
- end-of-support;
- retirement date.

---

# Deprecation Contract

```yaml
engine_deprecation:
  engine_definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 1.4.0

  deprecated_at: 2026-08-02T00:00:00Z

  replacement:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  support_until: 2026-11-01T00:00:00Z
  retirement_at: 2026-12-01T00:00:00Z
```

---

# No retirada inmediata

Salvo:

- incidente grave;
- vulnerabilidad crítica;
- violación contractual;
- policy block.

---

# Engine Trust Level

Todo Engine deberá declarar nivel de confianza.

Formato recomendado:

```text
ENGINE-TRUST-LEVEL-XXXXXX
```

---

# Niveles iniciales

```text
trusted_internal
approved_internal
approved_external
restricted_external
experimental
untrusted
blocked
```

---

# Trusted Internal

Control completo por NovaCoquinaria.

---

# Approved Internal

Motor interno aprobado, pero con alcance limitado.

---

# Approved External

Proveedor externo autorizado.

---

# Restricted External

Solo datos permitidos y tenants concretos.

---

# Experimental

No deberá utilizarse para operaciones críticas.

---

# Untrusted

No deberá recibir datos reales.

---

# Blocked

No utilizable.

---

# Trust Contract

```yaml
engine_trust:
  level: approved_external

  constraints:
    maximum_classification: public
    personal_data_allowed: false
    production_allowed: true
    human_approval_required: false
```

---

# Trust no sustituye autorización

El Policy Engine deberá evaluar el uso concreto.

---

# Engine Scope

Un Engine podrá restringirse por:

```text
tenant
environment
region
classification
domain
workflow
activity
operation
```

---

# Scope Contract

```yaml
engine_scope:
  environments:
    - staging
    - production

  tenants:
    allow:
      - TENANT-0001
      - TENANT-0002

  classifications:
    maximum: internal

  domains:
    - culinary_knowledge
```

---

# Engine Registration Manifest

Toda Definition podrá suministrarse mediante un manifest.

Formato recomendado:

```text
ENGINE-MANIFEST-XXXXXX
```

---

# Contrato

```yaml
engine_manifest:
  id: ENGINE-MANIFEST-RETRIEVAL-HYBRID-2.1.0

  engine_definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  provider:
    id: ENGINE-PROVIDER-NOVACOQUINARIA

  type:
    id: ENGINE-TYPE-RETRIEVAL

  capabilities:
    - CAP-HYBRID-RETRIEVAL@2.0.0
    - CAP-GRAPH-RETRIEVAL@1.1.0

  operations:
    - ENGINE-OP-RETRIEVE@2.0.0

  contracts:
    - HYBRID-RETRIEVAL-REQUEST@2.0.0
    - HYBRID-RETRIEVAL-RESULT@2.0.0

  trust:
    level: trusted_internal

  fingerprint:
    algorithm: sha256
    value: ...
```

---

# Manifest Validation

Deberá comprobar:

- schema;
- IDs;
- version;
- owner;
- provider;
- capabilities;
- operations;
- contracts;
- trust;
- fingerprint;
- compatibility;
- lifecycle.

---

# Engine Registry Record

La representación persistida podrá incluir:

```yaml
engine_registry_record:
  definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  manifest:
    id: ENGINE-MANIFEST-RETRIEVAL-HYBRID-2.1.0

  status: active

  validation:
    status: passed
    validated_at: 2026-08-02T20:00:00Z

  revision: 7
```

---

# Ownership

Todo Engine deberá tener owners explícitos.

---

# Roles de ownership

```text
technical_owner
operational_owner
security_owner
data_owner
product_owner
support_owner
```

---

# Ownership Contract

```yaml
engine_ownership:
  technical_owner:
    id: TEAM-KNOWLEDGE-PLATFORM

  operational_owner:
    id: TEAM-PLATFORM-OPERATIONS

  security_owner:
    id: TEAM-SECURITY

  escalation:
    contact: ONCALL-KNOWLEDGE-PLATFORM
```

---

# No Engine huérfano

Una Definition sin owner válido no deberá activarse.

---

# Documentation Reference

Todo Engine deberá enlazar a documentación.

```yaml
documentation:
  overview: DOC-ENGINE-RETRIEVAL
  operations: DOC-ENGINE-RETRIEVAL-OPERATIONS
  runbook: RUNBOOK-ENGINE-RETRIEVAL
  changelog: CHANGELOG-ENGINE-RETRIEVAL
```

---

# No almacenar documentación completa en Registry

Solo referencias estables.

---

# Engine Constraints

Un Engine podrá declarar limitaciones.

---

# Tipos

```text
input_size
output_size
concurrency
rate
language
modality
classification
region
tenant
cost
latency
availability_window
```

---

# Constraint Contract

```yaml
engine_constraint:
  id: ENGINE-CONSTRAINT-QUERY-LENGTH

  type: input_size

  field: query_text

  maximum: 8192

  unit: character
```

---

# Hard Constraint

No deberá violarse.

---

# Soft Constraint

Podrá utilizarse como preferencia.

---

# Engine Limit

Ejemplos:

```yaml
engine_limits:
  maximum_concurrency: 100
  requests_per_minute: 5000
  maximum_batch_size: 128
  maximum_input_tokens: 32768
```

---

# Limit Source

Deberá distinguir:

```text
provider
deployment
tenant
policy
contract
```

---

# Effective Limit

Será el mínimo aplicable entre las restricciones pertinentes.

---

# Engine Feature

Una **Engine Feature** representa una característica opcional.

Ejemplos:

```text
streaming
citations
structured_output
function_calling
multilingual
batch
explainability
checkpointing
```

---

# Feature Contract

```yaml
engine_feature:
  id: FEATURE-STRUCTURED-OUTPUT

  version: 1.0.0

  status: supported

  constraints:
    schema_formats:
      - json_schema
```

---

# Capability vs Feature

Capability:

```text
qué puede hacer
```

Feature:

```text
cómo o con qué propiedades puede hacerlo
```

---

# Engine Characteristics

Podrá declarar:

```text
stateless
stateful
read_only
side_effecting
deterministic
probabilistic
streaming
batch
interactive
long_running
```

---

# Engine Statefulness

Un Engine stateful deberá declarar:

- session model;
- persistence;
- affinity;
- recovery;
- cleanup;
- tenant isolation.

---

# Stateless Engine

Podrá recibir solicitudes en cualquier instancia compatible.

---

# Stateful Engine

Podrá requerir:

- sticky routing;
- session ID;
- affinity;
- checkpoint;
- state transfer.

---

# Model-Based Engine

Un Engine basado en IA deberá declarar:

- model;
- provider;
- version;
- context window;
- modalities;
- output modes;
- safety profile;
- data policy;
- deterministic parameters;
- evaluation record.

---

# Model Descriptor

```yaml
model_descriptor:
  id: MODEL-RAG-GENERATOR-0001

  provider: internal
  version: 1.0.0

  modalities:
    - text

  context_window:
    tokens: 32768

  structured_output: true

  data_usage:
    training_on_requests: false
```

---

# Engine Provenance

El Registry deberá conservar de dónde procede la información de registro.

---

# Provenance Sources

```text
provider_manifest
deployment_controller
service_discovery
health_monitor
operator
policy_engine
benchmark_platform
```

---

# Provenance Contract

```yaml
registry_provenance:
  field: operational.capacity.maximum_concurrency

  source:
    type: provider_manifest
    id: ENGINE-MANIFEST-RETRIEVAL-HYBRID-2.1.0

  observed_at: 2026-08-02T20:00:00Z
```

---

# Field Authority

Cuando varias fuentes aporten un mismo campo deberá existir una precedencia.

Ejemplo:

```text
Policy-enforced value
↓
Operator override
↓
Deployment observation
↓
Provider manifest
↓
Default
```

---

# No mezcla silenciosa

El valor efectivo deberá conservar provenance.

---

# Registry Snapshot

El Registry podrá producir snapshots versionados.

Formato recomendado:

```text
ENGINE-REGISTRY-SNAPSHOT-XXXXXX
```

---

# Objetivos

- reproducibilidad;
- auditoría;
- rollback;
- comparación;
- ejecución fijada.

---

# Contrato

```yaml
engine_registry_snapshot:
  id: ENGINE-REGISTRY-SNAPSHOT-20260802-0001

  created_at: 2026-08-02T20:00:00Z

  definitions:
    count: 18

  instances:
    count: 42

  capabilities:
    count: 57

  fingerprint: ...

  status: active
```

---

# Static Registry Snapshot

Contiene definiciones y contratos.

---

# Operational Snapshot

Podrá incluir estado operativo observado en un momento concreto.

---

# Recomendación

Separar:

```text
catalog snapshot
```

de:

```text
operational state
```

porque el health cambia con frecuencia.

---

# Registry Fingerprint

Deberá representar:

```text
Definitions
+
Capabilities
+
Operations
+
Contracts
+
Compatibility
+
Lifecycle
```

No necesariamente:

```text
current load
```

---

# Catálogo inicial recomendado

```text
ENGINE-TYPE-INGESTION
ENGINE-TYPE-VALIDATION
ENGINE-TYPE-KNOWLEDGE-GRAPH
ENGINE-TYPE-INDEXING
ENGINE-TYPE-RETRIEVAL
ENGINE-TYPE-RANKING
ENGINE-TYPE-CITATION
ENGINE-TYPE-REASONING
ENGINE-TYPE-RAG
ENGINE-TYPE-EMBEDDING
ENGINE-TYPE-POLICY
ENGINE-TYPE-AGENT
```

---

# Engines iniciales recomendados

```text
ENGINE-INGESTION-PRIMARY
ENGINE-VALIDATION-PRIMARY
ENGINE-KNOWLEDGE-GRAPH-PRIMARY
ENGINE-INDEXING-PRIMARY
ENGINE-RETRIEVAL-HYBRID
ENGINE-RAG-PRIMARY
ENGINE-REASONER-PRIMARY
ENGINE-POLICY-PRIMARY
```

---

# Capabilities iniciales recomendadas

```text
CAP-DOCUMENT-INGESTION
CAP-DOCUMENT-NORMALIZATION
CAP-STRUCTURAL-VALIDATION
CAP-SEMANTIC-VALIDATION
CAP-KNOWLEDGE-GRAPH-BUILD
CAP-STATEMENT-EXTRACTION
CAP-INDEX-BUILD
CAP-EMBEDDING-GENERATION
CAP-LEXICAL-RETRIEVAL
CAP-VECTOR-RETRIEVAL
CAP-HYBRID-RETRIEVAL
CAP-GRAPH-RETRIEVAL
CAP-EVIDENCE-SELECTION
CAP-CITATION-RESOLUTION
CAP-SYMBOLIC-REASONING
CAP-RAG-GENERATION
CAP-POLICY-EVALUATION
```

---

# Operaciones comunes

Todo Engine podrá implementar ciertas operaciones estándar cuando proceda.

```text
describe
health
readiness
capabilities
validate_contract
start
status
cancel
result
```

---

# Describe Operation

Devuelve su descriptor.

---

# Health Operation

Devuelve salud técnica.

---

# Readiness Operation

Indica si puede recibir trabajo.

---

# Capabilities Operation

Devuelve capacidades observadas.

---

# Validate Contract Operation

Permite comprobar compatibilidad.

---

# Start, Status, Cancel, Result

Adecuadas para operaciones asíncronas.

---

# Engine Descriptor Endpoint

Conceptualmente:

```text
GET /engine/descriptor
```

---

# Health Endpoint

Conceptualmente:

```text
GET /health
```

---

# Readiness Endpoint

Conceptualmente:

```text
GET /ready
```

---

# No dependencia obligatoria de HTTP

Son contratos lógicos.

---

# Engine Registration Policy

Formato recomendado:

```text
ENGINE-REGISTRATION-POLICY-XXXXXX
```

---

# Contrato preliminar

```yaml
engine_registration_policy:
  id: ENGINE-REGISTRATION-POLICY-STANDARD

  version: 1.0.0

  requirements:
    owner_required: true
    provider_required: true
    contracts_required: true
    health_operation_required: true
    trust_level_required: true
    documentation_required: true
    fingerprint_required: true

  production:
    experimental_engines_allowed: false
```

---

# Registration Modes

```text
manual
declarative
deployment_driven
self_registration
provider_sync
import
```

---

# Manual Registration

Realizada por operador.

---

# Declarative Registration

A partir de manifests versionados.

---

# Deployment-Driven Registration

A partir del sistema de despliegue.

---

# Self-Registration

El Engine anuncia su existencia.

Deberá validarse antes de activarse.

---

# Provider Sync

Sincroniza catálogo de proveedor externo.

---

# Import

Importa definiciones desde otro Registry.

---

# Recomendación

Utilizar registro declarativo para Definitions y registro dinámico para Instances.

---

# Registration Request

Formato recomendado:

```text
ENGINE-REGISTRATION-REQUEST-XXXXXX
```

---

# Contrato

```yaml
engine_registration_request:
  id: ENGINE-REGISTRATION-REQUEST-000041

  type: engine_definition

  manifest:
    id: ENGINE-MANIFEST-RETRIEVAL-HYBRID-2.1.0

  requested_by:
    id: TEAM-KNOWLEDGE-PLATFORM
    type: team

  target:
    environment: production

  requested_at: 2026-08-02T20:00:00Z
```

---

# Registration Result

```yaml
engine_registration_result:
  request:
    id: ENGINE-REGISTRATION-REQUEST-000041

  status: accepted

  registry_record:
    definition: ENGINE-DEF-RETRIEVAL-HYBRID@2.1.0

  validation:
    status: passed

  registered_at: 2026-08-02T20:01:00Z
```

---

# Registration States

```text
received
validating
pending_approval
accepted
rejected
blocked
completed
```

---

# Registration Validation

Categorías:

```text
schema
identity
ownership
capability
contract
compatibility
security
operational
governance
```

---

# Schema Validation

Comprueba estructura.

---

# Identity Validation

Comprueba:

- IDs;
- versiones;
- duplicados;
- namespaces.

---

# Ownership Validation

Comprueba owners y provider.

---

# Capability Validation

Comprueba que las capacidades existan y sean compatibles.

---

# Contract Validation

Comprueba schemas.

---

# Compatibility Validation

Comprueba adapters y consumidores.

---

# Security Validation

Comprueba:

- trust;
- authentication;
- classification;
- scopes.

---

# Operational Validation

Comprueba:

- health operation;
- endpoints;
- timeouts;
- capacity metadata.

---

# Governance Validation

Comprueba:

- lifecycle;
- documentation;
- review date;
- deprecation plan cuando proceda.

---

# Engine Definition Quality Gate

```yaml
quality_gate:
  id: QG-ENGINE-DEFINITION-0001

  criteria:
    all:
      - definition_schema_valid == true
      - engine_id_unique == true
      - definition_version_valid == true
      - engine_type_resolved == true
      - provider_resolved == true
      - ownership_complete == true
      - capabilities_resolved == true
      - operations_resolved == true
      - contracts_valid == true
      - trust_level_defined == true
      - lifecycle_defined == true
      - fingerprint_valid == true
```

---

# Capability Quality Gate

```yaml
quality_gate:
  id: QG-ENGINE-CAPABILITY-0001

  criteria:
    all:
      - capability_schema_valid == true
      - capability_version_valid == true
      - operations_defined == true
      - request_contract_valid == true
      - response_contract_valid == true
      - error_contract_valid == true
      - characteristics_declared == true
      - limitations_declared == true
```

---

# Operation Quality Gate

```yaml
quality_gate:
  id: QG-ENGINE-OPERATION-0001

  criteria:
    all:
      - operation_schema_valid == true
      - capability_reference_valid == true
      - contracts_resolved == true
      - idempotency_declared == true
      - side_effects_declared == true
      - timeout_declared == true
      - cancellation_semantics_declared == true
      - retry_semantics_declared == true
```

---

# Instance Quality Gate

```yaml
quality_gate:
  id: QG-ENGINE-INSTANCE-0001

  criteria:
    all:
      - definition_active == true
      - instance_identity_valid == true
      - environment_allowed == true
      - endpoints_valid == true
      - health_operation_reachable == true
      - security_profile_valid == true
      - capacity_declared == true
      - registration_revision_valid == true
```

---

# Registry Record Quality Gate

```yaml
quality_gate:
  id: QG-ENGINE-REGISTRY-RECORD-0001

  criteria:
    all:
      - manifest_valid == true
      - validation_passed == true
      - provenance_complete == true
      - owner_present == true
      - audit_record_created == true
      - registry_fingerprint_valid == true
```

---

# Eventos iniciales

Catálogo inicial:

```text
engine_definition_proposed
engine_definition_registered
engine_definition_validated
engine_definition_activated
engine_definition_deprecated
engine_definition_retired
engine_definition_blocked
engine_instance_discovered
engine_instance_registered
engine_instance_available
engine_instance_degraded
engine_instance_draining
engine_instance_unavailable
engine_instance_quarantined
engine_instance_deregistered
engine_capability_registered
engine_contract_registered
engine_compatibility_changed
engine_registry_snapshot_created
```

---

# Evento de registro

```yaml
event:
  type: engine_definition_registered

  subject:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    type: engine-definition

  data:
    version: 2.1.0
    provider: ENGINE-PROVIDER-NOVACOQUINARIA
    capabilities: 3

  correlation:
    correlation_id: CORR-000041
    causation_id: ENGINE-REGISTRATION-REQUEST-000041
```

---

# Evento de instancia disponible

```yaml
event:
  type: engine_instance_available

  subject:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001
    type: engine-instance

  data:
    definition: ENGINE-DEF-RETRIEVAL-HYBRID@2.1.0
    environment: production
    region: eu-west
```

---

# Auditoría

Deberán auditarse:

- registro;
- aprobación;
- activación;
- modificación;
- deprecation;
- retirement;
- block;
- quarantine;
- owner change;
- trust change;
- contract change;
- override.

---

# Audit Record

```yaml
engine_registry_audit:
  id: ENGINE-AUDIT-000041

  action: engine_definition.activate

  actor:
    id: USER-PLATFORM-ADMIN-0001
    type: user

  target:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  result: succeeded

  occurred_at: 2026-08-02T20:01:00Z
```

---

# Seguridad básica del Registry

El Registry será un componente de alta confianza.

---

# Riesgos

- registro de Engine falso;
- suplantación de Provider;
- modificación de endpoints;
- elevación de trust;
- publicación de contratos maliciosos;
- routing hacia proveedor no autorizado;
- cross-tenant exposure;
- eliminación no autorizada;
- downgrade de versión;
- dependencia comprometida.

---

# Controles iniciales

- autenticación;
- autorización;
- ownership validation;
- manifest signatures;
- fingerprints;
- immutable versions;
- audit;
- tenant isolation;
- trust policies;
- endpoint validation;
- allowlists;
- approval workflows.

---

# Manifest Signature

Los manifests podrán firmarse.

```yaml
manifest_signature:
  algorithm: ed25519
  signer: TEAM-KNOWLEDGE-PLATFORM
  value: ...
```

---

# No secretos en Registry

El Registry conservará únicamente referencias.

```yaml
authentication_profile:
  id: AUTH-PROFILE-INTERNAL-SERVICE
```

---

# Endpoint Poisoning

Los endpoints deberán proceder de fuentes autorizadas.

---

# Trust Elevation

Cambiar de:

```text
experimental
```

a:

```text
trusted_internal
```

deberá requerir aprobación y Quality Gates.

---

# Engine Quarantine

Una instancia podrá quedar aislada por:

- health inconsistente;
- outputs inválidos;
- anomalía de seguridad;
- incompatibilidad;
- checksum incorrecto;
- comportamiento no conforme.

---

# Quarantine Record

```yaml
engine_quarantine:
  id: ENGINE-QUARANTINE-000041

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  reason:
    code: INVALID_OUTPUT_CONTRACT

  status: active

  activated_at: 2026-08-02T20:10:00Z
```

---

# No selección de instancias quarantined

---

# Observabilidad básica

Desde la primera implementación deberán existir métricas sobre:

- Definitions;
- Instances;
- Capabilities;
- versiones;
- lifecycle;
- registros;
- validaciones;
- compatibilidad;
- health;
- availability.

---

# Métricas iniciales

```text
engine_definitions_total
engine_definitions_active
engine_definitions_deprecated
engine_instances_registered
engine_instances_available
engine_instances_degraded
engine_instances_quarantined
engine_capabilities_total
engine_registration_failures
engine_contract_validation_failures
engine_compatibility_failures
```

---

# Registry Log

```yaml
log:
  event: engine_definition_registered

  engine_definition: ENGINE-DEF-RETRIEVAL-HYBRID@2.1.0

  provider: ENGINE-PROVIDER-NOVACOQUINARIA

  capabilities: 3
  operations: 2

  validation_status: passed

  correlation_id: CORR-000041
```

---

# No incluir secretos ni endpoints sensibles completos

---

# Diagnósticos iniciales

```text
ENGINE_DEFINITION_SCHEMA_INVALID
ENGINE_ID_DUPLICATE
ENGINE_VERSION_INVALID
ENGINE_TYPE_NOT_FOUND
ENGINE_PROVIDER_NOT_FOUND
ENGINE_OWNER_MISSING
ENGINE_CAPABILITY_NOT_FOUND
ENGINE_CAPABILITY_VERSION_INCOMPATIBLE
ENGINE_OPERATION_NOT_FOUND
ENGINE_CONTRACT_NOT_FOUND
ENGINE_CONTRACT_INVALID
ENGINE_CONTRACT_INCOMPATIBLE
ENGINE_PROTOCOL_UNSUPPORTED
ENGINE_ENDPOINT_INVALID
ENGINE_ENDPOINT_NOT_AUTHORIZED
ENGINE_TRUST_LEVEL_MISSING
ENGINE_SCOPE_INVALID
ENGINE_FINGERPRINT_MISMATCH
ENGINE_MANIFEST_SIGNATURE_INVALID
ENGINE_DEFINITION_INACTIVE
ENGINE_INSTANCE_DEFINITION_NOT_ACTIVE
ENGINE_INSTANCE_ENVIRONMENT_NOT_ALLOWED
ENGINE_INSTANCE_QUARANTINED
ENGINE_COMPATIBILITY_UNKNOWN
ENGINE_REGISTRATION_REJECTED
ENGINE_LIFECYCLE_TRANSITION_INVALID
```

---

# Diagnostic Contract

```yaml
engine_registry_diagnostic:
  id: ENGINE-DIAGNOSTIC-000041

  code: ENGINE_CONTRACT_INCOMPATIBLE
  severity: error

  target:
    engine_definition: ENGINE-DEF-RETRIEVAL-HYBRID@2.1.0
    operation: ENGINE-OP-RETRIEVE@2.0.0

  details:
    expected_contract: HYBRID-RETRIEVAL-RESULT@2.0.0
    provided_contract: HYBRID-RETRIEVAL-RESULT@1.4.0

  retryable: false
```

---

# Casos de uso

---

# Caso de uso 1 — Registro de Retrieval Engine

El proveedor registra:

- Definition;
- Capability;
- Operation;
- Contracts;
- trust;
- ownership.

La Definition supera el Gate y pasa a `active`.

---

# Caso de uso 2 — Varias instancias

Una misma Definition dispone de:

- dos instancias en `eu-west`;
- una instancia en `eu-central`;
- una instancia de staging.

El Registry las diferencia sin duplicar la Definition.

---

# Caso de uso 3 — Nueva versión

Se registra:

```text
ENGINE-DEF-RETRIEVAL-HYBRID@2.2.0
```

La versión 2.1.0 continúa activa hasta completar migración.

---

# Caso de uso 4 — Capability compartida

Dos Engines implementan:

```text
CAP-EMBEDDING-GENERATION
```

uno interno y otro externo.

El Discovery Engine podrá devolver ambos bajo restricciones distintas.

---

# Caso de uso 5 — Operación asíncrona

El Indexing Engine registra:

- start;
- status;
- cancel;
- result.

El Orquestador sabe que debe tratarla como Job prolongado.

---

# Caso de uso 6 — Engine experimental

Un nuevo Reasoner se registra como:

```text
experimental
```

Solo podrá seleccionarse en sandbox y shadow mode.

---

# Caso de uso 7 — Proveedor externo restringido

Un RAG Provider externo admite únicamente:

```text
classification = public
```

No podrá recibir contenido interno.

---

# Caso de uso 8 — Contract mismatch

La Operation declara una respuesta incompatible con la Capability.

El Registration Quality Gate falla.

---

# Caso de uso 9 — Instance quarantined

Una instancia produce outputs que incumplen schema.

Se pone en quarantine sin retirar toda la Definition.

---

# Caso de uso 10 — Definition deprecated

La versión antigua declara:

- replacement;
- support deadline;
- retirement date.

Las nuevas Activities dejan de seleccionarla.

---

# Caso de uso 11 — Engine stateful

Un Engine requiere session affinity.

El Descriptor declara:

- stateful;
- sticky routing;
- session contract.

---

# Caso de uso 12 — Service Discovery externo

El Registry conserva:

```text
service_ref
```

y el runtime resuelve las réplicas mediante Service Discovery.

---

# Caso de uso 13 — Registry Snapshot

Una Execution crítica fija un Catalog Snapshot para conservar reproducibilidad.

---

# Caso de uso 14 — Trust elevation

Un proveedor pasa de `experimental` a `approved_external` tras:

- evaluación;
- seguridad;
- benchmark;
- aprobación.

---

# Caso de uso 15 — Owner inexistente

Un Engine pierde su equipo responsable.

La revisión de gobernanza lo bloquea para nuevas activaciones.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Engine identificado por URL

Una URL no representa identidad ni capacidad.

---

## Capacidad inferida por nombre

`retrieval-service` no demuestra qué Retrieval implementa.

---

## Definition e Instance mezcladas

Dificulta versionado y deployments.

---

## Una Definition por réplica

Duplica catálogo.

---

## Una Instance para todos los entornos

Mezcla producción, staging y desarrollo.

---

## Contratos no versionados

Impiden compatibilidad.

---

## Engine Version utilizada para versionar todos los contratos

Las dimensiones evolucionan independientemente.

---

## Operaciones sin semántica

Debe conocerse:

- idempotencia;
- side effects;
- cancelación;
- timeout.

---

## Errores como texto libre

Impiden decisiones de retry y fallback.

---

## Endpoints hardcoded en Workflows

Acoplan definición y despliegue.

---

## Utilizar labels para restricciones críticas

Las propiedades de seguridad deberán estar tipadas.

---

## Registrar una Capability sin contrato

No permite invocación segura.

---

## Registrar Engines sin owner

Genera componentes huérfanos.

---

## Registrar proveedor externo como trusted internal

Rompe el modelo de confianza.

---

## Elevar trust automáticamente

Deberá existir evaluación y aprobación.

---

## Modificar una versión publicada

Rompe reproducibilidad.

---

## Utilizar `latest` en ejecuciones críticas

Puede cambiar la implementación sin trazabilidad.

---

## Retirar una versión inmediatamente

Puede romper Executions y Adapters activos.

---

## Mezclar health y lifecycle

Un Engine activo puede estar temporalmente unhealthy.

---

## Engine disponible por existir en catálogo

La disponibilidad requiere instancia operativa.

---

## Registrar endpoints no verificados

Permite endpoint poisoning.

---

## Guardar credenciales en Metadata

El Registry deberá contener referencias.

---

## No conservar provenance de campos

Impide conocer qué fuente prevaleció.

---

## Registry como almacén de configuración arbitraria

Debe conservar contratos y metadatos gobernados.

---

## Service Discovery como sustituto de Registry

No conserva capacidades ni compatibilidad.

---

## Registry como Router obligatorio

El Registry descubre; el Router selecciona y ejecuta según arquitectura.

---

## No diferenciar Capability y Feature

Produce catálogos ambiguos.

---

## No declarar límites

Puede provocar requests no soportadas.

---

## Conformance solo documental

Los contratos deberán probarse.

---

## Quarantine a nivel Definition por fallo de una sola réplica

Deberá distinguirse el alcance.

---

## Borrar registros retirados

Son necesarios para auditoría y replay.

---

# Reglas mínimas de conformidad

---

## Engine ID estable

Todo Engine deberá disponer de identidad lógica.

---

## Definition versionada

Toda Definition deberá tener ID, versión y fingerprint.

---

## Instance separada

Los despliegues deberán registrarse independientemente.

---

## Engine Type

Toda Definition deberá declarar categoría.

---

## Provider

Todo Engine deberá declarar proveedor.

---

## Ownership

Todo Engine deberá poseer responsables.

---

## Capability explícita

Toda función deberá declararse.

---

## Capability versionada

Toda Capability deberá tener contrato.

---

## Operation explícita

Toda llamada invocable deberá estar registrada.

---

## Contract versionado

Requests, responses y errors deberán cumplir schemas.

---

## Protocol declarado

Toda comunicación deberá ser compatible.

---

## Endpoint gobernado

Los endpoints deberán ser autorizados y verificables.

---

## Lifecycle explícito

Toda Definition e Instance deberán declarar estado.

---

## Trust Level

Todo Engine deberá declarar confianza.

---

## Scope

Las restricciones de entorno, tenant y clasificación deberán ser explícitas.

---

## Compatibility Record

La compatibilidad no deberá asumirse.

---

## Manifest

Toda Definition deberá poder representarse mediante manifest.

---

## Registration Validation

Ningún Engine deberá activarse sin Quality Gate.

---

## Provenance

Los metadatos deberán conservar origen.

---

## Version Pinning

Las ejecuciones reproducibles deberán poder fijar versiones.

---

## Deprecation gobernada

Toda retirada deberá declarar sustitución o justificación.

---

## Quarantine

Las instancias no conformes deberán poder aislarse.

---

## Audit

Los cambios críticos deberán registrarse.

---

## No secrets

El Registry solo conservará referencias de autenticación.

---

# Conformidad de Engine Type

Será conforme cuando:

- tenga ID;
- tenga versión;
- declare categoría;
- declare capacidades esperadas;
- declare owner;
- sea único.

---

# Conformidad de Engine Definition

Será conforme cuando:

- tenga ID;
- tenga versión;
- tenga fingerprint;
- declare Engine;
- declare Type;
- declare Provider;
- declare ownership;
- declare Capabilities;
- declare Operations;
- declare Contracts;
- declare lifecycle;
- declare trust;
- declare compatibility.

---

# Conformidad de Engine Provider

Será conforme cuando:

- tenga ID;
- declare tipo;
- declare ownership;
- declare trust;
- declare status;
- declare condiciones cuando sea externo.

---

# Conformidad de Engine Instance

Será conforme cuando:

- tenga ID;
- referencie Definition y versión;
- declare environment;
- declare region;
- declare endpoints;
- declare lifecycle;
- declare health;
- declare availability;
- declare capacity;
- utilice revisión.

---

# Conformidad de Capability

Será conforme cuando:

- tenga ID;
- tenga versión;
- declare descripción;
- declare categoría;
- declare Operations;
- declare contratos;
- declare características;
- declare requirements;
- declare limitaciones.

---

# Conformidad de Capability Implementation

Será conforme cuando:

- tenga ID;
- referencie Capability;
- referencie Engine Definition;
- referencie Operation;
- declare conformance;
- declare limitaciones;
- supere Quality Gate.

---

# Conformidad de Engine Operation

Será conforme cuando:

- tenga ID;
- tenga versión;
- referencie Capability;
- declare Request Contract;
- declare Response Contract;
- declare Error Contract;
- declare side effects;
- declare idempotencia;
- declare cancelabilidad;
- declare timeout;
- declare modalidad.

---

# Conformidad de Engine Contract

Será conforme cuando:

- tenga ID;
- tenga versión;
- declare tipo;
- declare schema;
- declare compatibility;
- tenga fingerprint;
- pueda validarse.

---

# Conformidad de Engine Endpoint

Será conforme cuando:

- tenga ID;
- identifique Instance;
- declare protocol;
- declare address reference;
- declare Operations;
- declare security profile;
- declare status;
- no contenga secrets.

---

# Conformidad de Engine Manifest

Será conforme cuando:

- tenga ID;
- identifique Definition;
- identifique Provider;
- identifique Type;
- declare Capabilities;
- declare Operations;
- declare Contracts;
- declare Trust;
- tenga fingerprint;
- tenga firma cuando proceda.

---

# Lista de comprobación

Antes de activar una Engine Definition deberá comprobarse:

```text
[ ] El Engine posee ID estable.
[ ] La Engine Definition tiene ID.
[ ] La Engine Definition está versionada.
[ ] La Definition publicada es inmutable.
[ ] La Definition tiene fingerprint.
[ ] El Engine Type existe.
[ ] El Provider existe.
[ ] El Provider está activo.
[ ] El Technical Owner está declarado.
[ ] El Operational Owner está declarado.
[ ] El Security Owner está declarado cuando procede.
[ ] Las Capabilities están registradas.
[ ] Las Capabilities están versionadas.
[ ] Las Operations están registradas.
[ ] Cada Operation referencia una Capability.
[ ] Los Request Contracts existen.
[ ] Los Response Contracts existen.
[ ] Los Error Contracts existen.
[ ] Los Contracts cumplen schema.
[ ] La compatibilidad está declarada.
[ ] La idempotencia está declarada.
[ ] Los side effects están declarados.
[ ] La cancelabilidad está declarada.
[ ] Los timeouts están declarados.
[ ] Los protocolos están declarados.
[ ] Los Adapters compatibles pueden resolverse.
[ ] Los Endpoints utilizan referencias gobernadas.
[ ] Los Endpoints no contienen secrets.
[ ] El Trust Level está definido.
[ ] El Engine Scope está definido.
[ ] La clasificación máxima está definida.
[ ] Los environments permitidos están definidos.
[ ] Las regiones permitidas están definidas.
[ ] Los tenants permitidos están definidos cuando procede.
[ ] Los límites están declarados.
[ ] La capacidad está declarada.
[ ] Las Features están diferenciadas de Capabilities.
[ ] La statefulness está declarada.
[ ] Los Engines basados en modelos tienen Model Descriptor.
[ ] La provenance del registro está conservada.
[ ] La precedencia de fuentes está definida.
[ ] El Engine Manifest cumple schema.
[ ] La firma del Manifest es válida cuando procede.
[ ] La Registration Request está autorizada.
[ ] La Lifecycle Policy permite la activación.
[ ] La documentación está referenciada.
[ ] El runbook está referenciado cuando procede.
[ ] La deprecation policy está definida.
[ ] Existe capacidad de quarantine.
[ ] Los eventos del Registry están versionados.
[ ] Las operaciones administrativas se auditan.
[ ] El Quality Gate de Definition ha pasado.
[ ] El Quality Gate de Capability ha pasado.
[ ] El Quality Gate de Operation ha pasado.
[ ] El Quality Gate de Registry Record ha pasado.
```

---

# Arquitectura final de la Parte I

```text
Engine Proposal
        ↓
Engine Manifest
        ↓
Registration Gateway
        ↓
Identity and Ownership Validation
        ↓
Engine Type Resolution
        ↓
Provider Resolution
        ↓
Capability Registration
        ↓
Operation Registration
        ↓
Contract Validation
        ↓
Trust and Scope Validation
        ↓
Compatibility Validation
        ↓
Engine Definition
        ↓
Engine Instance Registration
        ↓
Registry Record
        ↓
Quality Gates
        ↓
Engine Catalog
```

---

# Transición hacia la Parte II

Esta primera parte ha definido:

- el propósito del Engine Registry;
- el problema que resuelve;
- su posición en NovaCoquinaria;
- su alcance;
- sus límites;
- la diferencia con Service Discovery;
- la diferencia con Engine Adapter Registry;
- la diferencia entre Engine y Capability;
- los principios arquitectónicos;
- los componentes principales;
- Engine Types;
- Engine Definitions;
- Engine Families;
- Engine Variants;
- Engine Providers;
- Engine Instances;
- Instance Lifecycle;
- Engine Metadata;
- Engine Descriptors;
- Capabilities;
- Capability Implementations;
- Capability Profiles;
- Operations;
- Engine Contracts;
- protocolos;
- endpoints;
- versionado;
- compatibilidad;
- lifecycle;
- deprecation;
- trust levels;
- Engine Scopes;
- Engine Manifests;
- ownership;
- documentación;
- constraints;
- limits;
- features;
- statefulness;
- Model Descriptors;
- provenance;
- Registry Snapshots;
- catálogo inicial;
- Registration Policies;
- Registration Requests;
- validaciones;
- Quality Gates;
- eventos;
- auditoría;
- seguridad básica;
- observabilidad;
- diagnósticos;
- casos de uso;
- antipatrones;
- reglas de conformidad.

La Parte II desarrollará:

- Registration Service;
- alta de Engine Definitions;
- registro dinámico de Instances;
- self-registration;
- declarative registration;
- deployment-driven registration;
- Provider synchronization;
- Instance Discovery;
- Heartbeats;
- Health Checks;
- Readiness;
- Liveness;
- Availability;
- Capacity Reports;
- Registration Leases;
- Instance Expiration;
- Deregistration;
- Draining;
- Quarantine;
- Registry Reconciliation;
- stale records;
- ownership renewal;
- discovery queries;
- Registry APIs;
- caching;
- consistency;
- Registry Events;
- Quality Gates de Registration y Discovery.

---

# Conclusión

El Engine Registry será la fuente gobernada mediante la que NovaCoquinaria conocerá qué motores existen y qué capacidades pueden utilizarse.

Su ciclo básico puede resumirse así:

```text
Definir Engine
        ↓
Declarar Provider
        ↓
Declarar Capabilities
        ↓
Declarar Operations
        ↓
Versionar Contracts
        ↓
Validar Compatibility
        ↓
Registrar Definition
        ↓
Registrar Instances
        ↓
Publicar Metadata
        ↓
Exponer Discovery
```

El Engine Type clasifica la función.

La Engine Definition describe el motor.

El Provider declara quién lo suministra.

La Instance representa un despliegue concreto.

La Capability define qué puede hacer.

La Operation define cómo se invoca.

Los Contracts definen inputs, outputs y errores.

El Protocol define cómo se comunica.

El Endpoint identifica dónde puede invocarse.

El Trust Level limita qué datos puede procesar.

El Lifecycle controla su evolución.

La Compatibility determina si puede utilizarse.

El Manifest formaliza su registro.

Los Quality Gates impiden activar Engines incompletos o inseguros.

Un Engine correctamente registrado deberá poder responder:

```text
¿Qué identidad posee?

¿Qué tipo de Engine es?

¿Qué versión implementa?

¿Quién lo proporciona?

¿Quién lo mantiene?

¿Qué capacidades ofrece?

¿Qué operaciones soporta?

¿Qué contratos implementa?

¿Qué protocolos utiliza?

¿Qué instancias están desplegadas?

¿Qué restricciones posee?

¿Qué nivel de confianza tiene?

¿Qué environments y tenants admite?

¿Qué límites de capacidad declara?

¿Qué Adapter puede utilizarse?

¿Qué versiones son compatibles?

¿Qué lifecycle posee?

¿Qué reemplazo existe si está deprecated?

¿Qué Quality Gates ha superado?
```

Con esta primera parte quedan establecidos los fundamentos, la arquitectura y el modelo contractual del **Engine Registry de NovaCoquinaria**.

La siguiente parte formalizará cómo las Definitions e Instances se registran, validan, mantienen vivas, reconcilian y descubren dinámicamente mediante heartbeats, health checks, leases, expiración y APIs de consulta.

---

# Parte II — Registration Service, Instance Discovery, Heartbeats, Health, Availability, Capacity, Leases, Reconciliation y APIs de consulta

---

# Introducción

La Parte I ha definido:

- el propósito del Engine Registry;
- el concepto de Engine;
- Engine Types;
- Engine Definitions;
- Engine Providers;
- Engine Instances;
- Capabilities;
- Operations;
- Contracts;
- Protocols;
- Endpoints;
- lifecycle;
- trust levels;
- scopes;
- manifests;
- ownership;
- versionado;
- compatibilidad;
- Quality Gates iniciales.

Esta segunda parte formaliza cómo esas Definitions e Instances entran, permanecen y salen del Registry.

El Engine Registry deberá soportar dos ritmos de cambio diferentes:

```text
Catálogo lógico
```

y:

```text
Estado operativo
```

El catálogo lógico cambia con relativa poca frecuencia e incluye:

- Definitions;
- Providers;
- Capabilities;
- Operations;
- Contracts;
- versiones;
- compatibilidad;
- deprecation;
- trust.

El estado operativo cambia continuamente e incluye:

- Instances disponibles;
- health;
- readiness;
- endpoints;
- capacidad;
- carga;
- heartbeats;
- leases;
- mantenimiento;
- draining;
- quarantine.

Conceptualmente:

```text
Engine Definition Manifest
        ↓
Definition Registration
        ↓
Contract and Governance Validation
        ↓
Definition Activation
        ↓
Engine Instance Registration
        ↓
Identity and Endpoint Validation
        ↓
Heartbeat and Health Monitoring
        ↓
Availability Calculation
        ↓
Discovery Index
        ↓
Consumer Queries
```

El Registration Service no deberá limitarse a guardar registros.

Deberá garantizar que cada Engine utilizable sea:

- identificable;
- auténtico;
- compatible;
- gobernado;
- saludable;
- localizable;
- observable;
- renovable;
- retirable;
- reconciliable.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir Registration Service;
- formalizar Definition Registration;
- formalizar Instance Registration;
- establecer registro declarativo;
- establecer Self-Registration;
- definir Deployment-Driven Registration;
- formalizar Provider Synchronization;
- definir Registration Requests;
- establecer Registration Approvals;
- formalizar Registration Leases;
- definir Instance Discovery;
- establecer Heartbeats;
- definir Liveness;
- definir Readiness;
- formalizar Health Checks;
- establecer Health Profiles;
- definir Availability;
- formalizar Availability Resolution;
- definir Capacity Reports;
- establecer Load Reports;
- formalizar Endpoint Discovery;
- definir Instance Expiration;
- establecer Deregistration;
- definir Draining;
- formalizar Maintenance;
- establecer Quarantine;
- definir Registry Reconciliation;
- detectar Stale Records;
- establecer Ownership Renewal;
- formalizar Registry Queries;
- definir filtros;
- establecer paginación;
- formalizar caching;
- definir consistency;
- establecer APIs;
- definir eventos;
- formalizar diagnósticos;
- establecer Quality Gates;
- definir casos de uso;
- establecer antipatrones;
- formalizar conformidad de Registration y Discovery.

---

# Principios de Registration y Discovery

Toda implementación deberá respetar los siguientes principios.

---

## Definition Registration estable

Las Engine Definitions deberán registrarse mediante procesos gobernados y versionados.

---

## Instance Registration dinámica

Las Engine Instances podrán aparecer y desaparecer con frecuencia.

---

## Definitions e Instances separadas

Una Instance no deberá introducir nuevas capacidades no declaradas por su Definition.

---

## Registro no equivale a disponibilidad

Una Instance registrada podrá seguir estando:

```text
validating
```

```text
starting
```

```text
unhealthy
```

```text
draining
```

---

## Identidad autenticada

Una instancia no deberá autoafirmar una identidad sin validación.

---

## Heartbeat no equivale a Health

Un proceso puede estar vivo y producir resultados inválidos.

---

## Health no equivale a Readiness

Un Engine sano puede no estar preparado para recibir nuevo trabajo.

---

## Availability contextual

La disponibilidad dependerá del contexto de consumo.

---

## Leases temporales

Los registros dinámicos deberán expirar si no se renuevan.

---

## No registros eternamente stale

Una Instance sin heartbeat ni lease válida no deberá seguir apareciendo como disponible.

---

## Endpoint validado

Todo Endpoint deberá corresponder a una Instance y protocolo autorizados.

---

## Capacidad observable

La selección deberá conocer límites y carga cuando sea relevante.

---

## Reconciliation periódica

El Registry deberá contrastar su estado con fuentes externas.

---

## Deregistration gobernada

La retirada deberá diferenciar:

- temporal;
- operativa;
- definitiva;
- forzada.

---

## Draining antes de retirada

Cuando sea posible, la Instance dejará de recibir nuevo trabajo antes de desaparecer.

---

## Quarantine inmediata

Una instancia peligrosa deberá poder excluirse sin retirar toda la Definition.

---

## Cache segura

Las caches no deberán prolongar artificialmente la disponibilidad de una Instance expirada.

---

## Consistencia diferenciada

Los datos de catálogo podrán tolerar una propagación moderada.

Los datos de:

- quarantine;
- block;
- trust;
- security;
- lease expiration;

deberán propagarse con mayor urgencia.

---

## Auditoría

Toda alta, renovación, retirada, quarantine y override deberá quedar registrada.

---

# Arquitectura conceptual

```text
┌───────────────────────────────────────────────┐
│             Registration Sources              │
│                                               │
│ Manifest · Deployment · Self · Provider       │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Registration Gateway              │
│                                               │
│ Auth · Ownership · Schema · Policy            │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Registration Service             │
│                                               │
│ Definitions · Instances · Leases · Revisions  │
└──────────────────────┬────────────────────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
    Health Monitor   Lease Manager   Reconciler
          │            │            │
          └────────────┼────────────┘
                       ▼
┌───────────────────────────────────────────────┐
│             Availability Resolver             │
│                                               │
│ Health · Readiness · Capacity · Policy        │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                Discovery API                  │
│                                               │
│ Queries · Filters · Candidates · Snapshots    │
└───────────────────────────────────────────────┘
```

---

# Registration Service

El **Registration Service** será el componente responsable de recibir, validar, persistir y mantener registros de Engine Definitions e Instances.

Formato recomendado:

```text
ENGINE-REGISTRATION-SERVICE-XXXXXX
```

---

# Responsabilidades

- recibir Registration Requests;
- autenticar registrantes;
- validar ownership;
- resolver Provider;
- validar manifests;
- registrar Definitions;
- registrar Instances;
- emitir revisiones;
- crear Registration Leases;
- gestionar renewals;
- aplicar lifecycle transitions;
- gestionar deregistration;
- emitir eventos;
- mantener auditoría;
- coordinar reconciliación.

---

# Contrato

```yaml
engine_registration_service:
  id: ENGINE-REGISTRATION-SERVICE-PRIMARY

  version: 1.0.0

  capabilities:
    - definition_registration
    - instance_registration
    - lease_management
    - deregistration
    - reconciliation

  policies:
    registration:
      id: ENGINE-REGISTRATION-POLICY-STANDARD

    ownership:
      id: ENGINE-OWNERSHIP-POLICY-STANDARD

  status: active
```

---

# Registration Domains

El servicio deberá diferenciar:

```text
catalog_registration
instance_registration
operational_update
governance_transition
```

---

# Catalog Registration

Incluye:

- Engine Type;
- Provider;
- Capability;
- Operation;
- Contract;
- Engine Definition.

---

# Instance Registration

Incluye:

- Instance identity;
- deployment;
- environment;
- region;
- endpoints;
- protocols;
- capacity;
- lease.

---

# Operational Update

Incluye:

- heartbeat;
- health;
- readiness;
- load;
- capacity;
- maintenance;
- draining.

---

# Governance Transition

Incluye:

- activate;
- deprecate;
- retire;
- block;
- quarantine;
- restore.

---

# Registration Modes

El Registry deberá soportar varios modos.

```text
declarative
manual
self_registration
deployment_driven
provider_sync
federated_import
recovery
```

---

# Declarative Registration

Una Definition se registra desde un manifest versionado.

---

# Flujo

```text
Manifest Created
        ↓
Signature Verification
        ↓
Schema Validation
        ↓
Ownership Validation
        ↓
Capability Resolution
        ↓
Contract Validation
        ↓
Security Validation
        ↓
Quality Gates
        ↓
Registration
```

---

# Ventajas

- reproducibilidad;
- revisión;
- GitOps;
- auditoría;
- comparación;
- rollback.

---

# Recomendación

Será el modo preferido para:

- Engine Definitions;
- Capabilities;
- Operations;
- Contracts;
- Providers.

---

# Manual Registration

Un operador crea o modifica un registro mediante una API administrativa.

---

# Restricciones

Deberá:

- exigir autorización;
- generar manifest equivalente;
- registrar actor;
- conservar justificación;
- pasar los mismos Quality Gates.

---

# No bypass de validación

El registro manual no deberá eludir:

- schemas;
- trust;
- compatibility;
- ownership;
- security.

---

# Self-Registration

Una Engine Instance podrá anunciarse al Registry.

---

# Flujo

```text
Instance Starts
        ↓
Authenticates
        ↓
Submits Instance Descriptor
        ↓
Definition Resolution
        ↓
Identity Validation
        ↓
Endpoint Validation
        ↓
Lease Creation
        ↓
Health Validation
        ↓
Instance Available
```

---

# Self-Registration Scope

Se recomienda limitarlo a:

- Instances;
- runtime metadata;
- endpoints;
- capacity;
- health hooks.

No deberá permitirse por defecto que una Instance cree una nueva Definition en producción.

---

# Self-Registration Identity

La instancia deberá autenticarse mediante:

- workload identity;
- mTLS certificate;
- signed token;
- deployment identity;
- service account.

---

# Self-Registration Contract

```yaml
engine_self_registration:
  request_id: ENGINE-INSTANCE-REGISTRATION-REQUEST-000041

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  deployment:
    id: DEPLOYMENT-RETRIEVAL-20260802-001

  environment:
    id: production

  region:
    id: eu-west

  endpoints:
    - ENGINE-ENDPOINT-RETRIEVAL-HTTP-001

  capacity:
    maximum_concurrency: 100

  identity:
    workload_identity: WORKLOAD-RETRIEVAL-001
```

---

# Self-Registration Validation

Deberá comprobar:

- identidad;
- Definition activa;
- deployment autorizado;
- environment permitido;
- region permitida;
- endpoint permitido;
- protocol permitido;
- version compatible;
- scope;
- trust;
- certificate;
- nonce;
- replay protection.

---

# Deployment-Driven Registration

El sistema de despliegue registra o actualiza Instances.

---

# Fuentes posibles

- Kubernetes Operator;
- Deployment Controller;
- Infrastructure-as-Code;
- Service Catalog;
- CI/CD Pipeline;
- Platform Controller.

---

# Ventajas

- fuente operativa autorizada;
- menor dependencia de autoafirmaciones;
- lifecycle sincronizado;
- integración con rollouts.

---

# Deployment Event

```yaml
deployment_registration_event:
  deployment:
    id: DEPLOYMENT-RETRIEVAL-20260802-001

  action: available

  engine_definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  replicas:
    desired: 3
    available: 3
```

---

# Provider Synchronization

El Registry podrá sincronizar catálogos de proveedores externos.

---

# Objetivos

- conocer modelos;
- versiones;
- regiones;
- límites;
- deprecations;
- precios;
- capacidades;
- cambios de contrato.

---

# Provider Sync Contract

Formato recomendado:

```text
ENGINE-PROVIDER-SYNC-XXXXXX
```

```yaml
engine_provider_sync:
  id: ENGINE-PROVIDER-SYNC-000041

  provider:
    id: ENGINE-PROVIDER-EXTERNAL-001

  mode: incremental

  cursor:
    value: provider-cursor-1842

  imported:
    definitions: 3
    versions: 7
    deprecated: 1

  status: completed
```

---

# Provider Sync Policies

```text
automatic_accept
review_required
metadata_only
disabled
```

---

# Recomendación

Para producción:

```text
review_required
```

para nuevas Definitions o cambios contractuales.

---

# External Metadata Trust

Los datos del proveedor deberán distinguirse de:

- observaciones internas;
- benchmarks;
- políticas;
- overrides.

---

# Federated Import

Podrá importarse información desde otro Engine Registry.

---

# Requisitos

- Registry identity;
- trust relationship;
- schema compatibility;
- namespace;
- signature;
- provenance;
- conflict policy.

---

# Registration Request

Toda operación de registro deberá representarse formalmente.

Formato recomendado:

```text
ENGINE-REGISTRATION-REQUEST-XXXXXX
```

---

# Contrato ampliado

```yaml
engine_registration_request:
  id: ENGINE-REGISTRATION-REQUEST-000041

  resource:
    type: engine_instance

  mode: self_registration

  subject:
    instance:
      id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  requester:
    id: WORKLOAD-RETRIEVAL-001
    type: workload

  context:
    environment: production
    region: eu-west
    tenant_scope: shared

  idempotency_key: >
    ENGINE-INSTANCE-RETRIEVAL-EU-001:
    DEPLOYMENT-RETRIEVAL-20260802-001

  requested_at: 2026-08-02T20:00:00Z
```

---

# Required Fields

- Request ID;
- resource type;
- registration mode;
- requester;
- subject;
- Definition;
- context;
- timestamp;
- idempotency key.

---

# Registration Idempotency

La misma solicitud repetida no deberá crear múltiples registros equivalentes.

---

# Scope

La idempotency key deberá considerar:

```text
provider
+
engine definition
+
instance
+
deployment
+
environment
```

---

# Duplicate Registration

Podrá producir:

```text
existing_record_returned
```

```text
renewal
```

```text
update
```

```text
conflict
```

según contexto.

---

# Registration Validation Pipeline

```text
Receive Request
        ↓
Authenticate
        ↓
Authorize
        ↓
Validate Schema
        ↓
Resolve Definition
        ↓
Validate Ownership
        ↓
Validate Identity
        ↓
Validate Environment
        ↓
Validate Endpoint
        ↓
Validate Contracts
        ↓
Validate Security
        ↓
Apply Quality Gates
        ↓
Persist Record
        ↓
Create Lease
        ↓
Publish Event
```

---

# Registration Approval

Algunos registros requerirán aprobación.

---

# Approval Triggers

- external provider;
- production environment;
- new trust level;
- sensitive classification;
- new side-effecting capability;
- new administrative operation;
- cross-region endpoint;
- unknown compatibility;
- contract exception.

---

# Approval Record

Formato recomendado:

```text
ENGINE-REGISTRATION-APPROVAL-XXXXXX
```

---

# Contrato

```yaml
engine_registration_approval:
  id: ENGINE-REGISTRATION-APPROVAL-000041

  request:
    id: ENGINE-REGISTRATION-REQUEST-000041

  required_roles:
    - platform_admin
    - security_reviewer

  decisions:
    - actor: USER-PLATFORM-ADMIN-0001
      decision: approve

    - actor: USER-SECURITY-0001
      decision: approve

  status: approved
```

---

# Approval States

```text
not_required
pending
approved
rejected
expired
cancelled
```

---

# Approval Expiration

Toda aprobación pendiente deberá tener una fecha límite.

---

# No aprobación implícita por timeout

---

# Definition Registration

El registro de una Definition deberá crear una versión inmutable.

---

# Definition Registration Record

```yaml
engine_definition_registration:
  id: ENGINE-DEF-REGISTRATION-000041

  definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  manifest:
    id: ENGINE-MANIFEST-RETRIEVAL-HYBRID-2.1.0

  validation:
    id: ENGINE-VALIDATION-RESULT-000041
    status: passed

  lifecycle:
    initial_state: experimental

  revision: 1
```

---

# Initial Lifecycle State

La política determinará si una nueva Definition entra como:

```text
draft
```

```text
experimental
```

```text
active
```

---

# Recomendación

Por defecto:

```text
experimental
```

tras validación técnica, y:

```text
active
```

tras aprobación operativa y de seguridad.

---

# Definition Duplicate

Una misma combinación:

```text
Definition ID + Version
```

no podrá registrarse dos veces con fingerprints diferentes.

---

# Error

```text
ENGINE_DEFINITION_VERSION_CONFLICT
```

---

# Same Fingerprint

Podrá considerarse idempotente.

---

# Instance Registration

El registro de Instance deberá vincular un despliegue operativo con una Definition.

---

# Instance Registration Record

```yaml
engine_instance_registration:
  id: ENGINE-INSTANCE-REGISTRATION-000041

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  deployment:
    id: DEPLOYMENT-RETRIEVAL-20260802-001

  lifecycle:
    state: validating

  registration:
    lease:
      id: ENGINE-REGISTRATION-LEASE-000041

  revision: 1
```

---

# Instance ID Uniqueness

Deberá ser único dentro del namespace del Registry.

---

# Reuse of Instance ID

No se recomienda reutilizar el mismo ID para deployments semánticamente diferentes.

---

# Instance Generation

El ID podrá derivarse de:

```text
Engine
+
Environment
+
Region
+
Deployment
+
Logical Unit
```

---

# Registration Lease

Una **Registration Lease** mantiene vivo un registro dinámico.

Formato recomendado:

```text
ENGINE-REGISTRATION-LEASE-XXXXXX
```

---

# Contrato

```yaml
engine_registration_lease:
  id: ENGINE-REGISTRATION-LEASE-000041

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  holder:
    id: WORKLOAD-RETRIEVAL-001

  issued_at: 2026-08-02T20:00:00Z
  expires_at: 2026-08-02T20:01:00Z

  renewal:
    interval: PT20S
    grace_period: PT30S

  fencing_token: 7

  status: active
```

---

# Lease Purpose

Evitar que una Instance desaparecida continúe figurando como disponible.

---

# Lease Duration

Deberá equilibrar:

- detección rápida de fallo;
- tolerancia a jitter;
- carga del Registry;
- latencia de red.

---

# Ejemplo

```text
lease duration = 60 s
renewal interval = 20 s
grace period = 30 s
```

---

# Lease Renewal

```text
Instance Sends Heartbeat
        ↓
Identity Validated
        ↓
Lease Token Validated
        ↓
Operational Data Updated
        ↓
Lease Extended
```

---

# Renewal Contract

```yaml
engine_lease_renewal:
  lease:
    id: ENGINE-REGISTRATION-LEASE-000041

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  expected_fencing_token: 7

  health:
    status: healthy

  readiness:
    status: ready

  capacity:
    available_concurrency: 74

  observed_at: 2026-08-02T20:00:20Z
```

---

# Lease Fencing Token

Toda nueva lease deberá recibir un token creciente.

Una Instance antigua no deberá renovar con un token obsoleto.

---

# Lease Renewal Failure

Puede deberse a:

- token obsoleto;
- Instance quarantined;
- Definition retired;
- identity mismatch;
- expired credentials;
- scope violation;
- Registry unavailable.

---

# Lease States

```text
issued
active
renewing
grace
expired
revoked
superseded
```

---

# Grace State

Durante un periodo breve podrá mantenerse la Instance como:

```text
suspected
```

o:

```text
degraded
```

pero no necesariamente como plenamente disponible.

---

# Expired Lease

La Instance deberá pasar a:

```text
unavailable
```

o:

```text
stale
```

según policy.

---

# Lease Revocation

El Registry podrá revocarla por:

- security incident;
- quarantine;
- deployment removal;
- contract violation;
- administrative action.

---

# Heartbeat

Un **Engine Heartbeat** informa de que una Instance sigue activa.

Formato recomendado:

```text
ENGINE-HEARTBEAT-XXXXXX
```

---

# Contrato

```yaml
engine_heartbeat:
  id: ENGINE-HEARTBEAT-000041

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  lease:
    id: ENGINE-REGISTRATION-LEASE-000041
    fencing_token: 7

  lifecycle:
    state: available

  health:
    state: healthy

  readiness:
    state: ready

  capacity:
    maximum_concurrency: 100
    active_requests: 23
    available_concurrency: 77

  emitted_at: 2026-08-02T20:00:20Z
```

---

# Heartbeat Content

Deberá ser pequeño.

Podrá incluir:

- lease;
- lifecycle;
- health summary;
- readiness;
- load;
- capacity;
- version;
- endpoint revision;
- timestamp.

---

# No payload funcional

No deberá contener resultados de negocio.

---

# Heartbeat Authentication

Deberá validarse:

- workload identity;
- signature;
- tenant;
- Instance ID;
- lease token;
- freshness;
- replay protection.

---

# Heartbeat Frequency

Deberá ser configurable por profile.

---

# Heartbeat Drift

El Registry podrá medir:

```text
received_at - emitted_at
```

---

# Heartbeat Out-of-Order

Un heartbeat antiguo no deberá sobrescribir un estado más reciente.

---

# Sequence

Podrá incluir:

```yaml
sequence: 1842
```

---

# Duplicate Heartbeat

Deberá tratarse como idempotente.

---

# Heartbeat Failure

La ausencia de heartbeat inicia detección de indisponibilidad, pero no prueba por sí sola que el Engine haya fallado.

---

# Liveness

La **Liveness** indica si el proceso o despliegue responde.

---

# Liveness States

```text
alive
suspected
dead
unknown
```

---

# Liveness Check

Puede consistir en:

- heartbeat;
- process probe;
- network probe;
- deployment observation.

---

# Liveness Contract

```yaml
engine_liveness:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  state: alive

  source:
    type: heartbeat

  observed_at: 2026-08-02T20:00:20Z
```

---

# Liveness no garantiza corrección

Una instancia puede estar viva y devolver outputs inválidos.

---

# Readiness

La **Readiness** indica si una Instance puede aceptar nuevas operaciones.

---

# Readiness States

```text
ready
not_ready
limited
draining
unknown
```

---

# Readiness Factors

- dependencias disponibles;
- warmup completado;
- contratos cargados;
- modelos cargados;
- índices disponibles;
- capacity;
- maintenance;
- draining;
- policy.

---

# Readiness Contract

```yaml
engine_readiness:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  state: ready

  checks:
    model_loaded: true
    lexical_index_available: true
    vector_index_available: true
    policy_connection: true

  observed_at: 2026-08-02T20:00:20Z
```

---

# Limited Readiness

Podrá aceptar solo determinadas operaciones.

---

# Ejemplo

```yaml
limited_operations:
  allowed:
    - ENGINE-OP-LEXICAL-RETRIEVE@1.0.0

  blocked:
    - ENGINE-OP-HYBRID-RETRIEVE@2.0.0
```

---

# Health

La **Engine Health** representa el estado técnico y funcional observado.

---

# Health States

```text
healthy
degraded
unhealthy
unknown
```

---

# Health Dimensions

```text
process
dependencies
contracts
data
performance
security
capacity
quality
```

---

# Health Contract

```yaml
engine_health:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  overall: degraded

  dimensions:
    process: healthy
    dependencies: degraded
    contracts: healthy
    data: healthy
    performance: degraded
    security: healthy
    capacity: healthy

  reasons:
    - code: VECTOR_INDEX_LATENCY_HIGH

  observed_at: 2026-08-02T20:00:20Z
```

---

# Health Profiles

Formato recomendado:

```text
ENGINE-HEALTH-PROFILE-XXXXXX
```

---

# Contrato

```yaml
engine_health_profile:
  id: ENGINE-HEALTH-PROFILE-STANDARD

  version: 1.0.0

  checks:
    liveness:
      required: true

    readiness:
      required: true

    contract_probe:
      required: true
      interval: PT5M

    dependency_probe:
      required: true
      interval: PT30S

  thresholds:
    degraded_after_failures: 2
    unhealthy_after_failures: 5
```

---

# Health Check Types

```text
passive
active
synthetic
contract
dependency
functional
security
performance
```

---

# Passive Health

Derivada de:

- requests;
- errors;
- latency;
- timeouts.

---

# Active Health

El monitor invoca una probe.

---

# Synthetic Health

Ejecuta una operación controlada.

---

# Contract Health

Valida que la Instance sigue cumpliendo su contrato.

---

# Dependency Health

Comprueba dependencias críticas.

---

# Functional Health

Ejecuta un caso mínimo funcional.

---

# Security Health

Comprueba:

- certificates;
- trust;
- authentication;
- policy;
- revocation.

---

# Performance Health

Comprueba:

- latency;
- throughput;
- saturation;
- error rate.

---

# Deep Health

Deberá ejecutarse con menor frecuencia.

---

# Health Check Record

```yaml
engine_health_check:
  id: ENGINE-HEALTH-CHECK-000041

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  type: contract

  operation:
    id: ENGINE-OP-RETRIEVE
    version: 2.0.0

  result: passed

  latency_ms: 84

  observed_at: 2026-08-02T20:00:00Z
```

---

# Health Source Authority

Podrán existir varias fuentes:

- instance self-report;
- external monitor;
- service mesh;
- scheduler observations;
- benchmark platform;
- operator.

---

# Precedencia recomendada

```text
Security block
↓
External monitor
↓
Scheduler observations
↓
Service mesh
↓
Instance self-report
```

---

# No confiar únicamente en self-report

---

# Health Aggregation

El estado general deberá calcularse mediante una policy.

---

# Ejemplo

```text
security = unhealthy
→ overall = unhealthy
```

```text
performance = degraded
+
resto healthy
→ overall = degraded
```

---

# Health Flapping

Una Instance puede alternar rápidamente entre estados.

---

# Flapping Protection

Podrá utilizar:

- hysteresis;
- consecutive failures;
- recovery threshold;
- minimum state duration;
- cooldown.

---

# Flapping Record

```yaml
engine_health_flapping:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  transitions_last_10m: 14

  action:
    quarantine_candidate: true
```

---

# Availability

La **Availability** indica si una Engine Instance puede ser considerada candidata para una solicitud concreta.

---

# Availability States

```text
available
available_with_restrictions
degraded
temporarily_unavailable
unavailable
blocked
unknown
```

---

# Availability Inputs

- Definition lifecycle;
- Instance lifecycle;
- lease;
- liveness;
- readiness;
- health;
- capacity;
- scope;
- trust;
- security;
- policy;
- maintenance;
- quarantine;
- operation;
- tenant;
- environment;
- region.

---

# Availability Contract

```yaml
engine_availability:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  context:
    operation: ENGINE-OP-RETRIEVE@2.0.0
    tenant: TENANT-0001
    environment: production
    classification: internal

  result: available

  reasons:
    - definition_active
    - lease_valid
    - readiness_ready
    - health_acceptable
    - capacity_available
    - scope_compatible
```

---

# Availability Resolver

Formato recomendado:

```text
ENGINE-AVAILABILITY-RESOLVER-XXXXXX
```

---

# Responsabilidades

- recopilar estado;
- evaluar lifecycle;
- validar lease;
- comprobar health;
- comprobar readiness;
- comprobar capacity;
- validar scope;
- validar trust;
- consultar policy;
- generar decisión.

---

# Availability Policy

Formato recomendado:

```text
ENGINE-AVAILABILITY-POLICY-XXXXXX
```

---

# Contrato

```yaml
engine_availability_policy:
  id: ENGINE-AVAILABILITY-POLICY-STANDARD

  version: 1.0.0

  requirements:
    definition_status:
      in:
        - active

    instance_state:
      in:
        - available
        - degraded

    lease_valid: true

    readiness:
      in:
        - ready
        - limited

    health:
      in:
        - healthy
        - degraded

    quarantine: false
```

---

# Contextual Availability

Una misma Instance podrá estar:

```text
available
```

para una operación y:

```text
unavailable
```

para otra.

---

# Ejemplo

Retrieval lexical disponible.

Retrieval vectorial no disponible.

---

# Availability Decision

```yaml
availability_decision:
  id: ENGINE-AVAILABILITY-DECISION-000041

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  operation:
    id: ENGINE-OP-HYBRID-RETRIEVE
    version: 2.0.0

  result: degraded

  restrictions:
    - vector_component_unavailable

  fallback_hint:
    operation: ENGINE-OP-LEXICAL-RETRIEVE@1.0.0
```

---

# Capacity Report

Una **Capacity Report** describe la capacidad declarada y disponible.

Formato recomendado:

```text
ENGINE-CAPACITY-REPORT-XXXXXX
```

---

# Contrato

```yaml
engine_capacity_report:
  id: ENGINE-CAPACITY-REPORT-000041

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  capacity:
    maximum_concurrency: 100
    active_operations: 23
    available_concurrency: 77

  resources:
    cpu_utilization: 0.58
    memory_utilization: 0.62

  queue:
    pending_operations: 4

  observed_at: 2026-08-02T20:00:20Z
```

---

# Capacity Dimensions

```text
concurrency
requests_per_second
tokens_per_minute
batch_size
gpu_slots
memory
queue_depth
throughput
storage
sessions
```

---

# Declared Capacity

Proviene de:

- manifest;
- deployment;
- provider;
- policy.

---

# Observed Capacity

Proviene de:

- metrics;
- Scheduler;
- Service Mesh;
- Worker Pool;
- runtime.

---

# Effective Capacity

Se calcula considerando:

```text
declared limit
-
current use
-
reserved capacity
-
policy reserve
```

---

# Capacity Confidence

Podrá declararse:

```yaml
confidence: 0.92
```

---

# Stale Capacity Report

No deberá utilizarse indefinidamente.

---

# Capacity Report TTL

```yaml
ttl: PT30S
```

---

# Load Report

El **Load Report** describe la utilización actual.

---

# Contrato

```yaml
engine_load_report:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  active_operations: 23
  queued_operations: 4

  latency:
    p50_ms: 74
    p95_ms: 182
    p99_ms: 410

  errors:
    rate: 0.004

  saturation:
    value: 0.61

  observed_at: 2026-08-02T20:00:20Z
```

---

# Capacity vs Load

```text
Capacity
=
cuánto puede atender
```

```text
Load
=
cuánto está atendiendo
```

---

# Reserved Capacity

Podrá reservarse para:

- critical workflows;
- tenants premium;
- recovery;
- administration;
- health checks.

---

# No exponer capacidad reservada a todos los consumidores

---

# Instance Discovery

El **Instance Discovery** permite localizar instancias de una Definition o Capability.

---

# Discovery Request

Formato recomendado:

```text
ENGINE-DISCOVERY-REQUEST-XXXXXX
```

---

# Contrato

```yaml
engine_discovery_request:
  id: ENGINE-DISCOVERY-REQUEST-000041

  target:
    capability:
      id: CAP-HYBRID-RETRIEVAL
      version_constraint: 2.x

  context:
    environment: production
    region:
      preferred:
        - eu-west
        - eu-central

    tenant: TENANT-0001
    classification: internal

  requirements:
    readiness: ready
    health:
      maximum_degradation: degraded

    streaming: true
    maximum_p95_latency_ms: 500

  include:
    - compatibility
    - capacity
    - endpoints
    - availability_explanation
```

---

# Discovery Targets

La consulta podrá dirigirse a:

```text
engine_id
engine_definition
engine_type
engine_family
capability
operation
provider
feature
```

---

# Discovery Filters

```text
version
environment
region
tenant
classification
trust
lifecycle
health
readiness
availability
protocol
feature
capacity
cost
latency
provider
```

---

# Required vs Preferred Filters

Deberán diferenciarse.

---

# Required

Si no se cumple, el candidato se excluye.

---

# Preferred

Influye en orden o score, pero no excluye.

---

# Ejemplo

```yaml
filters:
  required:
    environment: production
    trust_level:
      in:
        - trusted_internal
        - approved_internal

  preferred:
    region: eu-west
    latency_profile: low
```

---

# Discovery Result

Formato recomendado:

```text
ENGINE-DISCOVERY-RESULT-XXXXXX
```

---

# Contrato

```yaml
engine_discovery_result:
  id: ENGINE-DISCOVERY-RESULT-000041

  request:
    id: ENGINE-DISCOVERY-REQUEST-000041

  candidates:
    - instance:
        id: ENGINE-INSTANCE-RETRIEVAL-EU-001

      definition:
        id: ENGINE-DEF-RETRIEVAL-HYBRID
        version: 2.1.0

      availability: available
      compatibility: compatible

      capacity:
        available_concurrency: 77

      endpoint:
        id: ENGINE-ENDPOINT-RETRIEVAL-HTTP-001

  total_candidates: 3

  registry_snapshot:
    id: ENGINE-REGISTRY-SNAPSHOT-20260802-0001

  operational_observed_at: 2026-08-02T20:00:20Z
```

---

# Discovery Candidate

Cada candidato deberá incluir:

- Definition;
- Instance;
- Capability Implementation;
- Operation;
- compatibility;
- availability;
- endpoint;
- health;
- readiness;
- capacity;
- trust;
- scope;
- provenance.

---

# Discovery no Selection

El Discovery podrá ordenar candidatos preliminarmente, pero no deberá ocultar las razones.

---

# Discovery Explanation

```yaml
discovery_candidate_explanation:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  included_because:
    - capability_match
    - contract_compatible
    - region_preferred
    - health_healthy
    - capacity_available

  excluded_constraints:
    none: true
```

---

# Excluded Candidate Explanation

Podrá solicitarse para administración.

```yaml
excluded_candidate:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-US-001

  reasons:
    - region_not_allowed
    - classification_not_supported
```

---

# Discovery Pagination

Las consultas amplias deberán soportar paginación.

---

# Cursor Pagination

Recomendada para catálogos grandes.

```yaml
pagination:
  limit: 50
  cursor: ...
```

---

# Stable Snapshot

Para paginación consistente deberá fijarse:

```text
catalog snapshot
```

---

# Operational State Drift

El estado operativo podrá cambiar entre páginas.

Deberá declararse.

---

# Discovery Sorting

Opciones iniciales:

```text
compatibility
availability
health
capacity
latency
cost
region_affinity
provider_preference
version
```

---

# No sort crítico solo por metadata no verificada

---

# Endpoint Discovery

El Registry deberá resolver Endpoints compatibles.

---

# Endpoint Resolution Inputs

- Instance;
- Operation;
- protocol;
- environment;
- network zone;
- tenant;
- security profile;
- region.

---

# Endpoint Resolution Result

```yaml
endpoint_resolution:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  operation:
    id: ENGINE-OP-RETRIEVE
    version: 2.0.0

  endpoint:
    id: ENGINE-ENDPOINT-RETRIEVAL-HTTP-001

  protocol:
    type: http

  address:
    service_ref: SERVICE-RETRIEVAL-PRODUCTION

  security:
    authentication_profile: AUTH-PROFILE-INTERNAL-SERVICE
```

---

# Multiple Endpoints

Una Instance podrá ofrecer:

- HTTP;
- gRPC;
- streaming;
- admin;
- callback.

---

# Endpoint Compatibility

Deberá evaluarse:

- protocol;
- operation;
- version;
- security;
- network;
- region.

---

# Endpoint Revision

Los cambios deberán utilizar revisión.

---

# Endpoint TTL

Cuando proceda, una resolución podrá tener TTL.

---

# No utilizar Endpoint tras expirar su Instance Lease

---

# Instance Expiration

Una Instance deberá expirar cuando:

- la lease vence;
- no hay heartbeat;
- el deployment desaparece;
- el Provider la retira;
- el Registry la revoca.

---

# Expiration Process

```text
Lease Near Expiration
        ↓
Mark Suspected
        ↓
Grace Period
        ↓
Recheck Sources
        ↓
Expire Instance
        ↓
Availability = Unavailable
        ↓
Publish Event
        ↓
Optional Deregistration
```

---

# Instance Expiration Record

```yaml
engine_instance_expiration:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  reason:
    code: REGISTRATION_LEASE_EXPIRED

  last_heartbeat_at: 2026-08-02T20:00:20Z
  expired_at: 2026-08-02T20:01:30Z

  status: expired
```

---

# Expired vs Deregistered

```text
expired
```

indica pérdida operativa.

```text
deregistered
```

indica retirada formal del Registry activo.

---

# Expired Record Retention

El registro deberá conservarse durante una ventana para:

- auditoría;
- debugging;
- flap detection;
- recovery.

---

# Automatic Resurrection

Una Instance expirada no deberá recuperar automáticamente la lease anterior.

Deberá:

- registrarse de nuevo;
- obtener nuevo fencing token;
- validar identity;
- validar deployment.

---

# Deregistration

La **Deregistration** elimina una Instance de la selección activa.

---

# Deregistration Types

```text
graceful
forced
expired
administrative
deployment_removed
provider_removed
security
```

---

# Graceful Deregistration

Proceso recomendado:

```text
Request Deregistration
        ↓
Enter Draining
        ↓
Stop New Work
        ↓
Wait Active Operations
        ↓
Release Lease
        ↓
Deregister
```

---

# Deregistration Request

Formato recomendado:

```text
ENGINE-DEREGISTRATION-REQUEST-XXXXXX
```

---

# Contrato

```yaml
engine_deregistration_request:
  id: ENGINE-DEREGISTRATION-REQUEST-000041

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  mode: graceful

  requested_by:
    id: DEPLOYMENT-CONTROLLER
    type: service

  reason:
    code: ROLLING_UPGRADE

  grace_period: PT5M
```

---

# Deregistration Result

```yaml
engine_deregistration_result:
  request:
    id: ENGINE-DEREGISTRATION-REQUEST-000041

  active_operations:
    initial: 7
    completed: 7
    cancelled: 0

  final_state: deregistered
```

---

# Forced Deregistration

Podrá utilizarse por:

- seguridad;
- corrupción;
- endpoint compromise;
- invalid outputs;
- emergency.

---

# Active Operations

La política deberá decidir:

- continuar;
- cancelar;
- reasignar;
- reconciliar;
- permitir finalizar.

---

# Definition Deregistration

Las Definitions no deberán eliminarse igual que las Instances.

El lifecycle adecuado será:

```text
deprecate
→
retire
→
archive
```

---

# Draining

Una Instance en **Draining** no acepta nuevas operaciones.

---

# Draining Contract

```yaml
engine_draining:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  started_at: 2026-08-02T20:00:00Z

  deadline: 2026-08-02T20:05:00Z

  active_operations: 7

  policy:
    on_deadline: request_cancel
```

---

# Draining States

```text
requested
active
completed
timed_out
cancelled
```

---

# Draining Readiness

Deberá ser:

```text
not_ready
```

para nuevo trabajo.

---

# Existing Operations

Podrán continuar según policy.

---

# Draining Timeout Actions

```text
force_deregister
extend
cancel_operations
quarantine
manual_review
```

---

# Maintenance

Una Instance podrá entrar en **Maintenance**.

---

# Maintenance Types

```text
planned
emergency
provider
security
upgrade
data_migration
```

---

# Maintenance Window

```yaml
engine_maintenance:
  id: ENGINE-MAINTENANCE-000041

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  type: planned

  window:
    start: 2026-08-03T01:00:00Z
    end: 2026-08-03T02:00:00Z

  availability:
    new_operations: blocked
    active_operations: allowed_to_complete
```

---

# Scheduled Maintenance

El Discovery Engine deberá poder excluir o penalizar Instances próximas a mantenimiento.

---

# Maintenance Expiration

Al terminar deberá:

- ejecutar health;
- validar readiness;
- renovar lease;
- volver a available.

---

# Quarantine

La **Quarantine** aísla una Instance por riesgo o incumplimiento.

---

# Quarantine Triggers

- contract violation;
- security anomaly;
- invalid output;
- repeated health failures;
- version mismatch;
- endpoint poisoning;
- trust violation;
- unexpected side effects;
- data leakage risk.

---

# Quarantine Contract

```yaml
engine_quarantine:
  id: ENGINE-QUARANTINE-000041

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  reason:
    code: INVALID_OUTPUT_CONTRACT

  severity: critical

  effects:
    discovery_excluded: true
    lease_revoked: true
    new_operations_blocked: true

  status: active
```

---

# Quarantine Scope

Podrá afectar:

```text
instance
endpoint
operation
capability
definition
provider
```

---

# Instance Quarantine

Aísla un despliegue.

---

# Operation Quarantine

Bloquea solo una operación.

---

# Capability Quarantine

Bloquea una capacidad concreta.

---

# Definition Block

Bloquea todas sus Instances.

---

# Provider Suspension

Bloquea todos los Engines de un proveedor.

---

# Quarantine Release

Deberá requerir:

- resolución;
- revalidación;
- health checks;
- contract tests;
- aprobación;
- auditoría.

---

# No liberación automática solo por heartbeat sano

---

# Quarantine Review

```yaml
quarantine_review:
  quarantine:
    id: ENGINE-QUARANTINE-000041

  validation:
    contract_tests: passed
    security_review: passed
    health_checks: passed

  decision: release

  approved_by:
    - USER-PLATFORM-ADMIN-0001
    - USER-SECURITY-0001
```

---

# Stale Records

Un registro será **stale** cuando su información operativa haya superado la ventana aceptable.

---

# Stale Dimensions

```text
heartbeat
health
readiness
capacity
endpoint
ownership
contract_validation
benchmark
security_review
```

---

# Staleness Contract

```yaml
engine_record_staleness:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  fields:
    capacity:
      last_observed_at: 2026-08-02T19:55:00Z
      ttl: PT1M
      stale: true

    health:
      last_observed_at: 2026-08-02T20:00:20Z
      ttl: PT30S
      stale: false
```

---

# Stale Policy

Podrá:

- exclude;
- degrade;
- warn;
- refresh;
- use last known value.

---

# Recomendación por dimensión

```text
Security status stale
→ exclude

Lease stale
→ unavailable

Capacity stale
→ degrade or ignore capacity score

Benchmark stale
→ warning
```

---

# Registry Reconciliation

El **Registry Reconciler** compara el Registry con fuentes autorizadas.

Formato recomendado:

```text
ENGINE-REGISTRY-RECONCILER-XXXXXX
```

---

# Fuentes de reconciliación

- Deployment Controller;
- Service Discovery;
- Workload Identity Platform;
- Health Monitor;
- Provider Catalog;
- Service Mesh;
- Scheduler observations;
- Contract Test Platform;
- Security Platform.

---

# Reconciliation Goals

- detectar Instances desaparecidas;
- detectar Instances no registradas;
- detectar endpoints inconsistentes;
- corregir lifecycle;
- actualizar capacity;
- detectar version mismatch;
- detectar owner inexistente;
- detectar trust inconsistente;
- detectar registros stale;
- recuperar eventos perdidos.

---

# Reconciliation Request

```yaml
registry_reconciliation_request:
  id: ENGINE-RECONCILIATION-REQ-000041

  scope:
    engine_definition:
      id: ENGINE-DEF-RETRIEVAL-HYBRID
      version: 2.1.0

  sources:
    - deployment_controller
    - service_discovery
    - health_monitor

  mode: compare_and_repair
```

---

# Reconciliation Result

```yaml
registry_reconciliation_result:
  id: ENGINE-RECONCILIATION-RESULT-000041

  findings:
    missing_instances: 0
    stale_instances: 1
    endpoint_mismatches: 1
    version_mismatches: 0

  actions:
    - type: endpoint_update
      instance: ENGINE-INSTANCE-RETRIEVAL-EU-001

    - type: mark_unavailable
      instance: ENGINE-INSTANCE-RETRIEVAL-EU-002

  status: completed_with_changes
```

---

# Reconciliation Modes

```text
observe
compare
repair_safe
compare_and_repair
manual_review
```

---

# Safe Repairs

Podrán incluir:

- marcar stale;
- actualizar observed capacity;
- corregir health;
- expirar lease;
- retirar endpoint inexistente.

---

# Unsafe Repairs

Deberán requerir aprobación:

- cambiar trust;
- cambiar owner;
- cambiar Definition;
- elevar lifecycle;
- modificar Contracts;
- liberar quarantine;
- cambiar Provider.

---

# Reconciliation Frequency

Podrá depender de:

- entorno;
- Engine Type;
- criticidad;
- churn;
- provider.

---

# Reconciliation Storm

Tras una caída de infraestructura deberá limitarse:

- concurrencia;
- frecuencia;
- Provider calls;
- writes;
- events.

---

# Ownership Renewal

Los owners deberán confirmar periódicamente que una Definition sigue mantenida.

---

# Ownership Review

Formato recomendado:

```text
ENGINE-OWNERSHIP-REVIEW-XXXXXX
```

---

# Contrato

```yaml
engine_ownership_review:
  id: ENGINE-OWNERSHIP-REVIEW-000041

  engine_definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  current_owner:
    id: TEAM-KNOWLEDGE-PLATFORM

  review_due_at: 2026-11-01T00:00:00Z

  status: pending
```

---

# Ownership Review Outcomes

```text
confirmed
transferred
deprecated
blocked
expired
```

---

# Missing Owner

Una Definition sin owner válido podrá:

- generar warning;
- bloquear nuevas Instances;
- pasar a deprecated;
- quedar blocked.

---

# Recomendación

Para Engines críticos:

```text
owner missing
→ block new registrations
```

---

# Registry Consistency Model

El Registry deberá distinguir entre catálogo y operación.

---

# Catalog Consistency

Para:

- Definitions;
- Capabilities;
- Contracts;
- Trust;
- Lifecycle;
- Providers;

se recomienda consistencia fuerte o lectura versionada.

---

# Operational Consistency

Para:

- health;
- load;
- capacity;
- heartbeat;

podrá aceptarse consistencia eventual con TTL explícito.

---

# Critical Operational Fields

Deberán propagarse rápidamente:

- quarantine;
- lease revoked;
- security block;
- Definition retired;
- endpoint revoked;
- trust downgrade.

---

# Registry Revision

Los registros deberán utilizar:

```yaml
revision: 18
```

---

# Optimistic Concurrency

Toda actualización administrativa deberá incluir:

```text
expected_revision
```

---

# Conflict

```text
ENGINE_REGISTRY_REVISION_CONFLICT
```

---

# Registry Snapshot Consistency

Una consulta podrá fijar:

- Catalog Snapshot;
- Operational Observation Time.

---

# Ejemplo

```yaml
registry_read_context:
  catalog_snapshot:
    id: ENGINE-REGISTRY-SNAPSHOT-20260802-0001

  operational_consistency:
    maximum_staleness: PT15S
```

---

# Registry Cache

Los consumidores podrán cachear información.

---

# Cacheable Data

- Engine Types;
- Definitions;
- Capabilities;
- Operations;
- Contracts;
- static compatibility.

---

# Short-Lived Cache

- endpoints;
- availability;
- health;
- readiness;
- capacity.

---

# Non-Cacheable or Urgent Invalidation

- quarantine;
- trust downgrade;
- security block;
- Definition retirement;
- lease revocation.

---

# Cache Contract

```yaml
registry_cache_policy:
  catalog:
    ttl: PT10M

  operational:
    ttl: PT10S

  security:
    ttl: PT0S
    push_invalidation: true
```

---

# Push Invalidation

Los cambios críticos deberán emitir eventos para invalidar caches.

---

# Stale-While-Revalidate

Podrá utilizarse para metadata no crítica.

---

# No utilizar stale availability para side effects críticos

---

# Registry Read Model

Podrán existir proyecciones optimizadas para Discovery.

---

# Discovery Index

Podrá indexar:

- Capability;
- Operation;
- Version;
- Environment;
- Region;
- Trust;
- Health;
- Readiness;
- Availability;
- Capacity.

---

# Projection Lag

Deberá declararse.

---

# Fuente canónica

El registro principal y sus revisiones seguirán siendo la fuente autoritativa.

---

# APIs de Registration

---

# Registrar Definition

```text
POST /api/v1/engine-registry/definitions
```

---

# Consultar Definition

```text
GET /api/v1/engine-registry/definitions/{definitionId}/versions/{version}
```

---

# Validar Definition

```text
POST /api/v1/engine-registry/definitions:validate
```

---

# Activar Definition

```text
POST /api/v1/engine-registry/definitions/{definitionId}/versions/{version}:activate
```

---

# Deprecar Definition

```text
POST /api/v1/engine-registry/definitions/{definitionId}/versions/{version}:deprecate
```

---

# Retirar Definition

```text
POST /api/v1/engine-registry/definitions/{definitionId}/versions/{version}:retire
```

---

# Registrar Instance

```text
POST /api/v1/engine-registry/instances
```

---

# Renovar Lease

```text
POST /api/v1/engine-registry/instances/{instanceId}/lease:renew
```

---

# Enviar Heartbeat

```text
POST /api/v1/engine-registry/instances/{instanceId}/heartbeat
```

---

# Solicitar Draining

```text
POST /api/v1/engine-registry/instances/{instanceId}:drain
```

---

# Deregistrar Instance

```text
DELETE /api/v1/engine-registry/instances/{instanceId}
```

---

# Quarantine

```text
POST /api/v1/engine-registry/instances/{instanceId}:quarantine
```

---

# Liberar Quarantine

```text
POST /api/v1/engine-registry/instances/{instanceId}:release-quarantine
```

---

# Reconcile

```text
POST /api/v1/engine-registry/reconciliation
```

---

# APIs de Discovery

---

# Buscar Engines

```text
POST /api/v1/engine-registry/discovery
```

---

# Buscar por Capability

```text
GET /api/v1/engine-registry/capabilities/{capabilityId}/instances
```

---

# Buscar por Operation

```text
GET /api/v1/engine-registry/operations/{operationId}/instances
```

---

# Consultar Availability

```text
POST /api/v1/engine-registry/availability:resolve
```

---

# Resolver Endpoint

```text
POST /api/v1/engine-registry/endpoints:resolve
```

---

# Consultar Health

```text
GET /api/v1/engine-registry/instances/{instanceId}/health
```

---

# Consultar Capacity

```text
GET /api/v1/engine-registry/instances/{instanceId}/capacity
```

---

# Consultar Descriptor

```text
GET /api/v1/engine-registry/instances/{instanceId}/descriptor
```

---

# Registration API Request

```yaml
register_instance_request:
  definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  deployment:
    id: DEPLOYMENT-RETRIEVAL-20260802-001

  environment: production
  region: eu-west

  endpoints:
    - id: ENGINE-ENDPOINT-RETRIEVAL-HTTP-001

  capacity:
    maximum_concurrency: 100

  idempotency_key: >
    ENGINE-INSTANCE-RETRIEVAL-EU-001:
    DEPLOYMENT-RETRIEVAL-20260802-001
```

---

# Registration API Response

```yaml
register_instance_response:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  lifecycle:
    state: validating

  lease:
    id: ENGINE-REGISTRATION-LEASE-000041
    expires_at: 2026-08-02T20:01:00Z
    fencing_token: 7

  validation:
    status: pending_health_check
```

---

# Discovery API Request

```yaml
discover_engines_request:
  capability:
    id: CAP-HYBRID-RETRIEVAL
    version_constraint: 2.x

  requirements:
    environment: production
    classification: internal
    tenant: TENANT-0001
    streaming: true

  preferences:
    regions:
      - eu-west
      - eu-central

    latency_profile: low

  pagination:
    limit: 20
```

---

# Discovery API Response

```yaml
discover_engines_response:
  candidates:
    - instance_id: ENGINE-INSTANCE-RETRIEVAL-EU-001
      definition: ENGINE-DEF-RETRIEVAL-HYBRID@2.1.0
      availability: available
      compatibility: compatible
      health: healthy
      readiness: ready
      available_concurrency: 77
      region: eu-west

  total: 3

  catalog_snapshot:
    id: ENGINE-REGISTRY-SNAPSHOT-20260802-0001

  operational_observed_at: 2026-08-02T20:00:20Z
```

---

# API Idempotency

Las operaciones de alta, renovación, draining, quarantine y deregistration deberán soportar idempotencia cuando corresponda.

---

# API Errors

Toda API deberá utilizar códigos estructurados.

---

# Ejemplo

```yaml
engine_registry_error:
  code: ENGINE_INSTANCE_DEFINITION_NOT_ACTIVE
  category: lifecycle
  retryable: false

  message: >
    La Definition indicada no está activa
    para el entorno production.

  correlation_id: CORR-000041
```

---

# API Security

Deberá aplicar:

- authentication;
- authorization;
- tenant;
- environment;
- ownership;
- rate limits;
- idempotency;
- audit;
- input validation.

---

# Internal vs External APIs

Las APIs de:

- heartbeat;
- lease renewal;
- deployment sync;
- health reports;

deberán considerarse internas.

---

# Registry Events

Catálogo inicial de esta parte:

```text
engine_registration_requested
engine_registration_validating
engine_registration_approval_required
engine_registration_approved
engine_registration_rejected
engine_definition_registered
engine_instance_registration_requested
engine_instance_registered
engine_registration_lease_issued
engine_registration_lease_renewed
engine_registration_lease_grace_started
engine_registration_lease_expired
engine_registration_lease_revoked
engine_heartbeat_received
engine_liveness_changed
engine_readiness_changed
engine_health_changed
engine_availability_changed
engine_capacity_changed
engine_instance_draining_started
engine_instance_draining_completed
engine_instance_maintenance_started
engine_instance_maintenance_completed
engine_instance_expired
engine_instance_deregistered
engine_instance_quarantined
engine_instance_quarantine_released
engine_registry_reconciliation_started
engine_registry_reconciliation_completed
engine_registry_stale_record_detected
engine_ownership_review_due
engine_ownership_expired
```

---

# Evento de Lease Expirada

```yaml
event:
  type: engine_registration_lease_expired

  subject:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001
    type: engine-instance

  data:
    lease_id: ENGINE-REGISTRATION-LEASE-000041
    last_heartbeat_at: 2026-08-02T20:00:20Z
    expired_at: 2026-08-02T20:01:30Z

  correlation:
    correlation_id: CORR-000041
```

---

# Evento de Availability

```yaml
event:
  type: engine_availability_changed

  subject:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001
    type: engine-instance

  data:
    previous: available
    current: degraded
    reason: vector_index_unavailable
```

---

# Event Ordering

Los eventos de una misma Instance deberán conservar revisión o secuencia.

---

# Event Deduplication

Los consumidores deberán ser idempotentes.

---

# Observabilidad

---

# Métricas de Registration

- Registration Requests;
- accepted;
- rejected;
- pending approval;
- validation duration;
- duplicate registrations;
- signature failures;
- ownership failures.

---

# Métricas de Instances

- registered;
- available;
- degraded;
- unavailable;
- draining;
- maintenance;
- quarantined;
- expired.

---

# Métricas de Leases

- leases issued;
- renewals;
- renewal failures;
- grace entries;
- expirations;
- revocations;
- stale tokens.

---

# Métricas de Heartbeat

- heartbeat rate;
- heartbeat latency;
- missing heartbeats;
- duplicate heartbeats;
- out-of-order heartbeats;
- heartbeat drift.

---

# Métricas de Health

- health checks;
- failures;
- health transitions;
- flapping;
- contract check failures;
- dependency failures.

---

# Métricas de Availability

- available candidates per Capability;
- zero-candidate queries;
- degraded availability;
- policy exclusions;
- scope exclusions;
- capacity exclusions.

---

# Métricas de Discovery

- query count;
- query latency;
- candidate count;
- cache hit ratio;
- stale result rate;
- excluded candidates;
- pagination usage.

---

# Métricas de Reconciliation

- runs;
- findings;
- repairs;
- stale records;
- endpoint mismatches;
- missing Instances;
- version mismatches;
- reconciliation latency.

---

# Logs

```yaml
log:
  event: engine_instance_registered

  instance_id: ENGINE-INSTANCE-RETRIEVAL-EU-001
  definition: ENGINE-DEF-RETRIEVAL-HYBRID@2.1.0

  environment: production
  region: eu-west

  lease_id: ENGINE-REGISTRATION-LEASE-000041
  fencing_token: 7

  correlation_id: CORR-000041
```

---

# No incluir

- secrets;
- tokens;
- certificates completos;
- endpoint credentials;
- payloads funcionales;
- información sensible innecesaria.

---

# Tracing

```text
Registration Request
↓
Authentication
↓
Manifest Validation
↓
Definition Resolution
↓
Instance Validation
↓
Lease Creation
↓
Health Validation
↓
Availability Decision
↓
Discovery Publication
```

---

# Diagnósticos

Códigos iniciales:

```text
ENGINE_REGISTRATION_REQUEST_INVALID
ENGINE_REGISTRATION_MODE_NOT_ALLOWED
ENGINE_REGISTRATION_NOT_AUTHORIZED
ENGINE_REGISTRATION_IDEMPOTENCY_CONFLICT
ENGINE_REGISTRATION_APPROVAL_REQUIRED
ENGINE_REGISTRATION_APPROVAL_REJECTED
ENGINE_DEFINITION_VERSION_CONFLICT
ENGINE_INSTANCE_ID_DUPLICATE
ENGINE_INSTANCE_IDENTITY_INVALID
ENGINE_INSTANCE_DEFINITION_NOT_ACTIVE
ENGINE_INSTANCE_DEPLOYMENT_NOT_AUTHORIZED
ENGINE_INSTANCE_ENVIRONMENT_NOT_ALLOWED
ENGINE_INSTANCE_REGION_NOT_ALLOWED
ENGINE_INSTANCE_ENDPOINT_INVALID
ENGINE_INSTANCE_ENDPOINT_UNREACHABLE
ENGINE_INSTANCE_PROTOCOL_INCOMPATIBLE
ENGINE_REGISTRATION_LEASE_INVALID
ENGINE_REGISTRATION_LEASE_EXPIRED
ENGINE_REGISTRATION_LEASE_REVOKED
ENGINE_REGISTRATION_FENCING_TOKEN_STALE
ENGINE_HEARTBEAT_INVALID
ENGINE_HEARTBEAT_DUPLICATE
ENGINE_HEARTBEAT_OUT_OF_ORDER
ENGINE_HEARTBEAT_TIMEOUT
ENGINE_LIVENESS_UNKNOWN
ENGINE_READINESS_NOT_READY
ENGINE_HEALTH_CHECK_FAILED
ENGINE_HEALTH_FLAPPING
ENGINE_AVAILABILITY_UNRESOLVED
ENGINE_CAPACITY_REPORT_STALE
ENGINE_CAPACITY_EXHAUSTED
ENGINE_INSTANCE_DRAINING
ENGINE_INSTANCE_MAINTENANCE
ENGINE_INSTANCE_EXPIRED
ENGINE_INSTANCE_DEREGISTRATION_FAILED
ENGINE_INSTANCE_QUARANTINED
ENGINE_QUARANTINE_RELEASE_REJECTED
ENGINE_REGISTRY_RECORD_STALE
ENGINE_REGISTRY_RECONCILIATION_FAILED
ENGINE_REGISTRY_REVISION_CONFLICT
ENGINE_OWNERSHIP_REVIEW_EXPIRED
ENGINE_DISCOVERY_QUERY_INVALID
ENGINE_DISCOVERY_NO_CANDIDATES
ENGINE_ENDPOINT_RESOLUTION_FAILED
ENGINE_REGISTRY_CACHE_STALE
```

---

# Diagnostic Contract

```yaml
engine_registry_diagnostic:
  id: ENGINE-DIAGNOSTIC-000041

  code: ENGINE_REGISTRATION_FENCING_TOKEN_STALE
  severity: error

  target:
    instance: ENGINE-INSTANCE-RETRIEVAL-EU-001
    lease: ENGINE-REGISTRATION-LEASE-000041

  details:
    received_token: 6
    current_token: 7

  message: >
    La renovación procede de una lease obsoleta.

  retryable: false
```

---

# Quality Gate de Definition Registration

```yaml
quality_gate:
  id: QG-ENGINE-DEFINITION-REGISTRATION-0001

  criteria:
    all:
      - request_authenticated == true
      - requester_authorized == true
      - manifest_schema_valid == true
      - manifest_signature_valid == true
      - definition_id_unique == true
      - version_fingerprint_consistent == true
      - provider_active == true
      - ownership_complete == true
      - capabilities_resolved == true
      - contracts_valid == true
      - security_review_passed == true
      - lifecycle_transition_allowed == true
```

---

# Quality Gate de Instance Registration

```yaml
quality_gate:
  id: QG-ENGINE-INSTANCE-REGISTRATION-0001

  criteria:
    all:
      - instance_identity_authenticated == true
      - definition_active == true
      - deployment_authorized == true
      - environment_allowed == true
      - region_allowed == true
      - endpoints_valid == true
      - protocols_compatible == true
      - trust_scope_compatible == true
      - registration_lease_created == true
      - health_validation_passed == true
```

---

# Quality Gate de Heartbeat y Lease

```yaml
quality_gate:
  id: QG-ENGINE-LEASE-HEARTBEAT-0001

  criteria:
    all:
      - heartbeat_authenticated == true
      - heartbeat_schema_valid == true
      - lease_active == true
      - fencing_token_current == true
      - heartbeat_sequence_valid == true
      - heartbeat_timestamp_fresh == true
      - operational_metadata_valid == true
```

---

# Quality Gate de Health

```yaml
quality_gate:
  id: QG-ENGINE-HEALTH-0001

  criteria:
    all:
      - liveness_observed == true
      - readiness_observed == true
      - health_profile_defined == true
      - contract_check_current == true
      - dependency_health_current == true
      - security_health_current == true
      - flapping_policy_applied == true
```

---

# Quality Gate de Availability

```yaml
quality_gate:
  id: QG-ENGINE-AVAILABILITY-0001

  criteria:
    all:
      - definition_lifecycle_compatible == true
      - instance_lifecycle_compatible == true
      - lease_valid == true
      - readiness_acceptable == true
      - health_acceptable == true
      - scope_compatible == true
      - trust_compatible == true
      - policy_permitted == true
      - quarantine_absent == true
```

---

# Quality Gate de Discovery

```yaml
quality_gate:
  id: QG-ENGINE-DISCOVERY-0001

  criteria:
    all:
      - query_schema_valid == true
      - required_filters_applied == true
      - compatibility_evaluated == true
      - availability_evaluated == true
      - stale_critical_data_excluded == true
      - candidate_provenance_complete == true
      - registry_snapshot_declared == true
      - operational_observation_time_declared == true
```

---

# Quality Gate de Deregistration

```yaml
quality_gate:
  id: QG-ENGINE-DEREGISTRATION-0001

  criteria:
    all:
      - request_authorized == true
      - draining_policy_applied == true
      - active_operations_accounted == true
      - lease_revoked_or_released == true
      - availability_removed == true
      - audit_record_created == true
      - deregistration_event_published == true
```

---

# Quality Gate de Reconciliation

```yaml
quality_gate:
  id: QG-ENGINE-RECONCILIATION-0001

  criteria:
    all:
      - authoritative_sources_defined == true
      - source_precedence_defined == true
      - stale_records_detected == true
      - unsafe_repairs_require_approval == true
      - repairs_revision_controlled == true
      - actions_audited == true
      - reconciliation_budget_defined == true
```

---

# Casos de uso

---

# Caso de uso 1 — Definition declarativa

El equipo publica un manifest de Retrieval Engine.

El Registration Service:

- valida firma;
- comprueba owner;
- valida Contracts;
- registra Definition;
- deja lifecycle en `experimental`.

---

# Caso de uso 2 — Self-Registration de Instance

Una Instance arranca en producción.

Se autentica, registra endpoints, obtiene lease y queda `validating`.

Tras health y readiness pasa a `available`.

---

# Caso de uso 3 — Heartbeat perdido

La Instance deja de enviar heartbeats.

El Registry:

- entra en grace;
- la marca `suspected`;
- expira lease;
- cambia availability a `unavailable`.

---

# Caso de uso 4 — Heartbeat fuera de orden

Llega un heartbeat con secuencia anterior.

El Registry lo ignora y conserva el estado más reciente.

---

# Caso de uso 5 — Readiness limitada

El componente lexical está disponible, pero el vectorial no.

La Instance queda disponible solo para operaciones lexicales.

---

# Caso de uso 6 — Health degradado

La latencia p95 supera el umbral.

El Health Resolver marca `degraded`, pero mantiene selección bajo policies tolerantes.

---

# Caso de uso 7 — Capacidad agotada

La Instance está sana, pero sin slots disponibles.

Availability puede mantenerse, aunque Discovery la marca como no preferente o temporalmente saturada.

---

# Caso de uso 8 — Draining por rollout

El Deployment Controller solicita draining.

La Instance deja de aparecer para nuevas operaciones y finaliza las activas.

---

# Caso de uso 9 — Quarantine

Una Instance devuelve un output incompatible.

Se revoca la lease y queda excluida de Discovery.

---

# Caso de uso 10 — Reconciliation

El Deployment Controller informa de dos Instances, pero el Registry conserva tres.

La tercera se marca stale y se expira.

---

# Caso de uso 11 — Provider Sync

Un proveedor externo de modelos anuncia una deprecation.

El Registry importa el cambio como pendiente de revisión.

---

# Caso de uso 12 — Discovery contextual

Un tenant solicita una Capability para datos `internal`.

El Registry excluye proveedores externos que solo admiten `public`.

---

# Caso de uso 13 — Cache invalidada

Una Instance es quarantined.

El evento crítico invalida inmediatamente las caches de Discovery.

---

# Caso de uso 14 — Ownership vencido

El owner no confirma la revisión.

La Definition continúa operativa durante una ventana, pero bloquea nuevas versiones o Instances según policy.

---

# Caso de uso 15 — Resurrection segura

Una Instance expirada vuelve a arrancar.

Debe registrarse de nuevo y recibe un nuevo fencing token.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Self-Registration creando Definitions en producción

Permite que un workload se otorgue capacidades no aprobadas.

---

## Registro sin identidad de workload

Facilita suplantación.

---

## Lease sin expiración

Mantiene Instances fantasma.

---

## Heartbeat como única prueba de salud

Un proceso vivo puede ser funcionalmente inválido.

---

## Health autoafirmado como fuente única

Debe contrastarse externamente.

---

## Readiness igual a liveness

Una Instance viva puede no estar preparada.

---

## Availability global única

La disponibilidad depende de operación, tenant y clasificación.

---

## Mantener disponible durante grace sin restricciones

Puede enviar trabajo a una Instance perdida.

---

## Renovación con token antiguo

Permite resurrectar un despliegue obsoleto.

---

## Reutilizar Instance ID para deployments distintos

Rompe trazabilidad.

---

## Endpoint actualizado sin revisión

Puede producir carreras.

---

## Capacity Report sin TTL

Puede generar decisiones basadas en carga obsoleta.

---

## Discovery devolviendo solo una URL

Pierde compatibilidad, provenance y alternativas.

---

## Required y preferred mezclados

Puede excluir candidatos válidos o aceptar incompatibles.

---

## Cache larga para quarantine

Mantiene Engines peligrosos en uso.

---

## Proyección de Discovery como fuente canónica

Puede estar retrasada.

---

## Automatic acceptance de Provider Sync

Puede introducir cambios contractuales sin revisión.

---

## Deregistration inmediata en rollout normal

Interrumpe operaciones activas.

---

## Draining sin deadline

Puede no terminar nunca.

---

## Quarantine liberada por un único heartbeat

No demuestra corrección.

---

## Reconciliation cambiando trust automáticamente

Es una reparación insegura.

---

## Owner review puramente informativa

Un Engine crítico no debería permanecer huérfano indefinidamente.

---

## Expired y Deregistered tratados como iguales

Tienen causas y consecuencias distintas.

---

## Eliminar registros expirados inmediatamente

Se pierde evidencia operacional.

---

## Heartbeats con payloads grandes

Aumentan carga innecesaria.

---

## Discovery sin snapshot o observation time

Impide interpretar la frescura del resultado.

---

## Endpoint físico como identidad

Rompe estabilidad.

---

## No auditar revocación de lease

Dificulta investigar caídas.

---

# Reglas mínimas de conformidad

---

## Registration Service

Deberá existir un servicio responsable del ciclo completo.

---

## Registration Modes

Deberán estar definidos y gobernados.

---

## Declarative Definitions

Las Definitions deberán poder registrarse mediante manifests.

---

## Dynamic Instances

Las Instances deberán registrarse de forma independiente.

---

## Identity Validation

Toda Instance deberá autenticarse.

---

## Idempotency

Toda Registration Request deberá ser deduplicable.

---

## Registration Lease

Toda Instance dinámica deberá tener lease temporal.

---

## Fencing Token

Toda nueva lease deberá invalidar la anterior.

---

## Heartbeat

Las Instances deberán renovar su estado.

---

## Liveness

Deberá medirse independientemente.

---

## Readiness

Deberá determinar si acepta nuevo trabajo.

---

## Health

Deberá incluir dimensiones técnicas y funcionales.

---

## Availability

Deberá resolverse en contexto.

---

## Capacity

Deberá declararse y observarse.

---

## TTL

Los datos operativos deberán tener frescura definida.

---

## Discovery

Deberá devolver candidatos compatibles y explicables.

---

## Endpoint Resolution

Deberá utilizar referencias gobernadas.

---

## Instance Expiration

Las leases vencidas deberán retirar disponibilidad.

---

## Draining

La retirada normal deberá evitar nuevo trabajo.

---

## Deregistration

Deberá ser auditable y gobernada.

---

## Quarantine

Las Instances peligrosas deberán poder aislarse.

---

## Reconciliation

Deberá contrastar el Registry con fuentes autorizadas.

---

## Stale Detection

Los registros obsoletos deberán detectarse.

---

## Ownership Review

Los Engines deberán mantener responsables vigentes.

---

## Cache Invalidation

Los cambios críticos deberán propagarse rápidamente.

---

## Revision Control

Las actualizaciones deberán detectar conflictos.

---

## APIs versionadas

Registration y Discovery deberán exponerse mediante contratos estables.

---

## Events

Los cambios deberán emitir eventos versionados.

---

## Quality Gates

Ninguna Instance deberá quedar disponible sin superar validaciones.

---

# Conformidad de Registration Request

Será conforme cuando:

- tenga ID;
- declare recurso;
- declare modo;
- identifique requester;
- preserve contexto;
- declare idempotency key;
- cumpla schema;
- esté autorizada.

---

# Conformidad de Registration Lease

Será conforme cuando:

- tenga ID;
- identifique Instance;
- identifique holder;
- declare emisión;
- declare expiración;
- declare renewal interval;
- declare grace period;
- declare fencing token;
- tenga estado.

---

# Conformidad de Heartbeat

Será conforme cuando:

- tenga ID;
- identifique Instance;
- identifique lease;
- declare fencing token;
- declare sequence;
- declare health summary;
- declare readiness;
- declare capacity;
- declare timestamp;
- esté autenticado.

---

# Conformidad de Health Record

Será conforme cuando:

- identifique Instance;
- declare overall state;
- declare dimensiones;
- declare razones;
- declare fuente;
- declare observation time;
- respete Health Profile.

---

# Conformidad de Availability Decision

Será conforme cuando:

- identifique Instance;
- declare contexto;
- evalúe lifecycle;
- evalúe lease;
- evalúe readiness;
- evalúe health;
- evalúe capacity;
- evalúe scope;
- evalúe trust;
- evalúe policy;
- declare resultado;
- declare razones.

---

# Conformidad de Discovery Request

Será conforme cuando:

- tenga ID;
- declare target;
- declare contexto;
- diferencie requisitos y preferencias;
- declare versión;
- declare paginación;
- cumpla schema.

---

# Conformidad de Discovery Result

Será conforme cuando:

- identifique Request;
- declare candidatos;
- declare compatibilidad;
- declare availability;
- preserve endpoints;
- declare capacity;
- preserve provenance;
- declare Catalog Snapshot;
- declare observation time.

---

# Conformidad de Deregistration

Será conforme cuando:

- tenga Request;
- identifique Instance;
- declare modo;
- declare actor;
- declare reason;
- aplique draining cuando proceda;
- trate operaciones activas;
- libere o revoque lease;
- emita auditoría.

---

# Conformidad de Quarantine

Será conforme cuando:

- tenga ID;
- declare alcance;
- declare razón;
- declare severidad;
- excluya Discovery;
- bloquee nuevas operaciones;
- declare revisión;
- preserve auditoría.

---

# Conformidad de Reconciliation

Será conforme cuando:

- tenga Request;
- declare scope;
- declare fuentes;
- preserve source precedence;
- declare findings;
- declare actions;
- aplique revision control;
- audite cambios;
- limite reparaciones inseguras.

---

# Lista de comprobación

Antes de aprobar Registration y Discovery deberá comprobarse:

```text
[ ] Existe Registration Service.
[ ] Los Registration Modes están definidos.
[ ] Las Definitions se registran mediante manifest.
[ ] Los manifests se validan.
[ ] Las firmas se verifican cuando procede.
[ ] Las Instances se registran separadamente.
[ ] Self-Registration está limitada a Instances.
[ ] Las Workload Identities se validan.
[ ] Deployment-Driven Registration está soportada.
[ ] Provider Sync está gobernado.
[ ] Las Registration Requests tienen ID.
[ ] Las Registration Requests tienen idempotency key.
[ ] Las Registration Approvals están definidas.
[ ] Las Definitions publicadas son inmutables.
[ ] Los fingerprints de versión son consistentes.
[ ] Las Instances tienen IDs únicos.
[ ] Las Instances referencian Definition exacta.
[ ] Las Instances declaran deployment.
[ ] Las Instances declaran environment.
[ ] Las Instances declaran region.
[ ] Los endpoints se validan.
[ ] Los protocolos se validan.
[ ] Toda Instance dinámica tiene Registration Lease.
[ ] Las Leases tienen expiración.
[ ] Las Leases tienen renewal interval.
[ ] Las Leases tienen grace period.
[ ] Las Leases tienen fencing token.
[ ] Los tokens obsoletos se rechazan.
[ ] Los Heartbeats se autentican.
[ ] Los Heartbeats tienen sequence.
[ ] Los Heartbeats fuera de orden se rechazan.
[ ] Los Heartbeats duplicados son idempotentes.
[ ] Liveness está definida.
[ ] Readiness está definida.
[ ] Health está definida.
[ ] Los Health Profiles están versionados.
[ ] Existen Health Checks externos.
[ ] La Health Aggregation está definida.
[ ] Existe protección contra flapping.
[ ] Availability es contextual.
[ ] Availability considera lifecycle.
[ ] Availability considera lease.
[ ] Availability considera readiness.
[ ] Availability considera health.
[ ] Availability considera capacity.
[ ] Availability considera trust.
[ ] Availability considera scope.
[ ] Availability considera Policy.
[ ] Capacity Reports tienen TTL.
[ ] Load Reports tienen observation time.
[ ] Discovery admite Capability.
[ ] Discovery admite Operation.
[ ] Discovery admite Definition.
[ ] Discovery distingue required y preferred.
[ ] Discovery declara Catalog Snapshot.
[ ] Discovery declara observation time.
[ ] Discovery preserva provenance.
[ ] Endpoint Resolution está gobernada.
[ ] Endpoints no sobreviven a leases expiradas.
[ ] Instance Expiration está automatizada.
[ ] Expired y Deregistered están diferenciados.
[ ] La resurrection exige nueva lease.
[ ] Draining está definido.
[ ] Draining tiene deadline.
[ ] Deregistration está auditada.
[ ] Maintenance está modelada.
[ ] Quarantine está soportada.
[ ] Quarantine puede aplicarse por scope.
[ ] Quarantine revoca disponibilidad.
[ ] La liberación de Quarantine requiere revalidación.
[ ] Existen políticas de staleness.
[ ] Security staleness excluye candidatos.
[ ] Existe Registry Reconciler.
[ ] Las fuentes autoritativas están definidas.
[ ] Las reparaciones inseguras requieren aprobación.
[ ] Existe Ownership Review.
[ ] Los Engines críticos no pueden quedar huérfanos.
[ ] Catalog y Operational Consistency están diferenciadas.
[ ] Se utiliza revision control.
[ ] Las caches tienen TTL por categoría.
[ ] Los cambios críticos invalidan caches.
[ ] Las APIs están versionadas.
[ ] Las APIs internas están separadas.
[ ] Los Events están versionados.
[ ] Existen métricas de Registration.
[ ] Existen métricas de Leases.
[ ] Existen métricas de Heartbeats.
[ ] Existen métricas de Health.
[ ] Existen métricas de Discovery.
[ ] Existen métricas de Reconciliation.
[ ] Los diagnósticos están estructurados.
[ ] El Quality Gate de Definition Registration ha pasado.
[ ] El Quality Gate de Instance Registration ha pasado.
[ ] El Quality Gate de Heartbeat y Lease ha pasado.
[ ] El Quality Gate de Health ha pasado.
[ ] El Quality Gate de Availability ha pasado.
[ ] El Quality Gate de Discovery ha pasado.
[ ] El Quality Gate de Deregistration ha pasado.
[ ] El Quality Gate de Reconciliation ha pasado.
```

---

# Arquitectura final de la Parte II

```text
Definition Manifest
        ↓
Definition Registration
        ↓
Validation and Approval
        ↓
Definition Activation
        ↓
Instance Registration
        ↓
Identity and Endpoint Validation
        ↓
Registration Lease
        ↓
Heartbeat
        ↓
Liveness · Readiness · Health
        ↓
Capacity and Load Reports
        ↓
Availability Resolution
        ↓
Discovery Index
        ↓
Discovery Query
        ↓
Compatible Candidates
        ↓
Draining · Deregistration · Quarantine
        ↓
Registry Reconciliation
```

---

# Transición hacia la Parte III

Esta segunda parte ha definido:

- Registration Service;
- Registration Domains;
- Registration Modes;
- Declarative Registration;
- Manual Registration;
- Self-Registration;
- Deployment-Driven Registration;
- Provider Synchronization;
- Federated Import;
- Registration Requests;
- idempotencia;
- Registration Validation Pipeline;
- Registration Approvals;
- Definition Registration;
- Instance Registration;
- Registration Leases;
- Lease Renewal;
- Fencing Tokens;
- Heartbeats;
- Heartbeat Security;
- Liveness;
- Readiness;
- Health;
- Health Profiles;
- Health Checks;
- Health Aggregation;
- Flapping Protection;
- Availability;
- Availability Resolver;
- Capacity Reports;
- Load Reports;
- Instance Discovery;
- Discovery Requests;
- filtros;
- required y preferred constraints;
- Discovery Results;
- Candidate Explanations;
- paginación;
- Endpoint Discovery;
- Instance Expiration;
- Deregistration;
- Draining;
- Maintenance;
- Quarantine;
- Stale Records;
- Registry Reconciliation;
- Ownership Renewal;
- Consistency Model;
- revision control;
- Registry Cache;
- APIs;
- eventos;
- observabilidad;
- diagnósticos;
- Quality Gates;
- casos de uso;
- antipatrones;
- reglas de conformidad.

La Parte III desarrollará:

- Capability Model avanzado;
- Capability Taxonomy;
- Capability Dependencies;
- Capability Composition;
- Capability Requirements;
- Feature Model;
- Operation Semantics;
- Contract Matching;
- Capability Matching;
- Activity-to-Capability Resolution;
- Adapter Matching;
- Resource Requirements;
- Scheduling Hints;
- Affinity;
- Anti-Affinity;
- Capacity Classes;
- Cost Profiles;
- Latency Profiles;
- Quality Profiles;
- Context Windows;
- Token Limits;
- Batch and Streaming Support;
- Data Classification Constraints;
- Engine Candidate Scoring;
- Matching Diagnostics;
- Capability Quality Gates.

---

# Conclusión

El Registration Service y el Discovery Model convierten el catálogo estático del Engine Registry en un sistema operativo y dinámico.

Su ciclo puede resumirse así:

```text
Registrar Definition
        ↓
Registrar Instance
        ↓
Emitir Lease
        ↓
Recibir Heartbeats
        ↓
Evaluar Liveness
        ↓
Evaluar Readiness
        ↓
Evaluar Health
        ↓
Actualizar Capacity
        ↓
Resolver Availability
        ↓
Responder Discovery
        ↓
Reconciliar cambios
        ↓
Drenar, retirar o aislar
```

La Definition describe qué es el Engine.

La Instance representa dónde se encuentra desplegado.

La Registration Lease demuestra que el registro sigue vigente.

El Heartbeat informa de continuidad operativa.

Liveness indica que el proceso responde.

Readiness indica que puede aceptar nuevo trabajo.

Health evalúa su estado técnico y funcional.

Capacity describe cuánto puede atender.

Availability determina si puede utilizarse en un contexto concreto.

Discovery devuelve candidatos compatibles.

Draining permite retirarlo sin interrumpir trabajo.

Deregistration elimina su participación activa.

Quarantine protege la plataforma ante instancias no confiables.

Reconciliation corrige divergencias entre el Registry y la infraestructura real.

Un Engine Instance correctamente registrada deberá poder responder:

```text
¿Quién la registró?

¿Qué identidad autenticada posee?

¿Qué Definition y versión implementa?

¿Qué deployment representa?

¿Qué endpoints expone?

¿Qué lease mantiene vigente su registro?

¿Cuándo fue su último heartbeat?

¿Está viva?

¿Está preparada?

¿Está sana?

¿Qué operaciones tiene disponibles?

¿Qué capacidad libre posee?

¿Qué datos puede procesar?

¿Para qué tenants está autorizada?

¿Está en mantenimiento?

¿Está drenando?

¿Está quarantined?

¿Cuándo expira su registro?

¿Qué fuentes confirman su estado?

¿Puede aparecer en una consulta de Discovery?

¿Por qué fue incluida o excluida?
```

Con esta segunda parte queda formalizado el ciclo mediante el que NovaCoquinaria registra, valida, mantiene, descubre, drena, reconcilia y retira dinámicamente las instancias de sus Engines.

La siguiente parte definirá cómo el Registry traduce las necesidades de una Activity en requisitos de Capability y construye candidatos mediante compatibilidad contractual, recursos, afinidad, coste, latencia, calidad y restricciones de seguridad.

---

# Parte III — Capability Model avanzado: taxonomía, dependencias, composición, matching, requisitos, afinidad, recursos, coste, latencia, calidad y scoring de candidatos

---

# Introducción

La Parte II ha definido cómo:

- se registran Engine Definitions;
- se registran Engine Instances;
- se emiten Registration Leases;
- se reciben Heartbeats;
- se evalúan Liveness, Readiness y Health;
- se calcula Availability;
- se publican Capacity Reports;
- se resuelven Endpoints;
- se ejecutan consultas de Discovery;
- se drenan, retiran, aíslan y reconcilian Instances.

Sin embargo, descubrir una Instance disponible no es suficiente.

El Orquestador no debería preguntar únicamente:

```text
¿Qué Retrieval Engines están disponibles?
```

Deberá expresar con precisión qué necesita ejecutar.

Por ejemplo:

```text
Necesito una Capability de recuperación híbrida
compatible con el contrato 2.x,
que pueda procesar conocimiento interno,
con soporte de streaming,
citas verificables,
latencia p95 inferior a 500 ms,
contexto en español,
índice de snapshot concreto,
coste máximo determinado
y Adapter compatible.
```

Esta necesidad deberá transformarse en un proceso formal de:

```text
Activity Requirements
        ↓
Capability Resolution
        ↓
Contract Matching
        ↓
Feature Matching
        ↓
Constraint Evaluation
        ↓
Resource Matching
        ↓
Security Matching
        ↓
Operational Matching
        ↓
Candidate Scoring
        ↓
Ranked Engine Candidates
```

Esta parte formaliza el modelo avanzado de Capabilities y el mecanismo por el que NovaCoquinaria traducirá una Activity o intención de ejecución en una lista explicable de Engine Candidates.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- formalizar Capability Taxonomy;
- definir Capability Families;
- definir Capability Specializations;
- establecer Capability Dependencies;
- formalizar Capability Composition;
- definir Composite Capabilities;
- establecer Capability Requirements;
- formalizar Capability Constraints;
- definir Feature Model;
- diferenciar Capabilities, Features y Operations;
- establecer Operation Semantics;
- formalizar Activity Requirements;
- definir Activity-to-Capability Resolution;
- establecer Contract Matching;
- formalizar Schema Compatibility;
- definir Semantic Compatibility;
- establecer Adapter Matching;
- formalizar Protocol Matching;
- definir Resource Requirements;
- establecer Capacity Classes;
- formalizar Scheduling Hints;
- definir Affinity;
- establecer Anti-Affinity;
- formalizar Data Locality;
- definir Region Affinity;
- establecer Tenant Affinity;
- formalizar Model Affinity;
- definir Cost Profiles;
- establecer Latency Profiles;
- formalizar Quality Profiles;
- definir Reliability Profiles;
- establecer Sustainability Profiles;
- formalizar Context Windows;
- definir Token Limits;
- establecer Batch Support;
- formalizar Streaming Support;
- definir Data Classification Constraints;
- establecer Residency Constraints;
- formalizar Candidate Eligibility;
- definir Candidate Scoring;
- establecer Score Normalization;
- formalizar Hard Filters;
- definir Soft Preferences;
- establecer Tie-Breaking;
- formalizar Matching Explanations;
- definir Matching Diagnostics;
- establecer Capability Quality Gates;
- formalizar reglas de conformidad.

---

# Principios del Capability Matching

Toda implementación deberá respetar los siguientes principios.

---

## Necesidad antes que proveedor

La resolución deberá partir de:

```text
qué capacidad se necesita
```

y no de:

```text
qué Engine se desea invocar
```

salvo pinning explícito.

---

## Hard Constraints antes de scoring

Los candidatos incompatibles deberán excluirse antes de puntuar preferencias.

---

## Compatibilidad multidimensional

Un Engine no será compatible únicamente por compartir el mismo Capability ID.

---

## Capabilities normalizadas

Las capacidades deberán definirse mediante una taxonomía común.

---

## Specialization explícita

Una Capability especializada deberá declarar de cuál deriva.

---

## Dependencias explícitas

Toda Capability que requiera otra deberá declararlo.

---

## Features no equivalentes a Capabilities

Una Feature modifica cómo se presta una Capability, pero no la sustituye.

---

## Semántica de operación declarada

No deberán inferirse:

- side effects;
- idempotencia;
- streaming;
- cancelabilidad;
- retryability.

---

## Contracts como condición necesaria

La compatibilidad funcional sin compatibilidad contractual no será suficiente.

---

## Seguridad como filtro obligatorio

Ningún score alto podrá compensar una incompatibilidad de seguridad.

---

## Availability contextual

El matching deberá utilizar el contexto concreto de ejecución.

---

## Coste y latencia como perfiles

No deberán tratarse únicamente como labels.

---

## Calidad observable

Las decisiones podrán usar benchmarks y métricas, pero deberán conservar frescura y provenance.

---

## Scoring explicable

Todo candidato deberá poder justificar:

- inclusión;
- exclusión;
- puntuación;
- posición.

---

## No score único universal

La ponderación deberá depender del perfil de selección.

---

## No `best engine` absoluto

Un Engine puede ser mejor para:

- bajo coste;
- baja latencia;
- mayor calidad;
- entorno restringido;

y peor para otros objetivos.

---

## Preferencias no pueden violar límites

Una preferencia nunca deberá sobrepasar un hard constraint.

---

## Fallback explícito

La degradación de requisitos deberá ser gobernada.

---

## Matching reproducible

Las entradas, versiones, perfiles y scores deberán poder reconstruirse.

---

# Arquitectura conceptual

```text
┌───────────────────────────────────────────────┐
│              Activity Requirement             │
│                                               │
│ Capability · Contracts · Constraints          │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            Capability Resolver                │
│                                               │
│ Taxonomy · Specialization · Composition       │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Eligibility Filter               │
│                                               │
│ Security · Contract · Scope · Availability    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Matching Engine                 │
│                                               │
│ Features · Resources · Affinity · Profiles    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Candidate Scoring                │
│                                               │
│ Quality · Latency · Cost · Reliability        │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│          Ranked Candidate Set                 │
│                                               │
│ Scores · Explanations · Fallbacks             │
└───────────────────────────────────────────────┘
```

---

# Capability Taxonomy

La **Capability Taxonomy** organiza las capacidades de NovaCoquinaria.

Formato recomendado:

```text
CAP-TAXONOMY-XXXXXX
```

---

# Contrato

```yaml
capability_taxonomy:
  id: CAP-TAXONOMY-NOVACOQUINARIA

  version: 1.0.0

  roots:
    - CAP-DOMAIN-KNOWLEDGE-INGESTION
    - CAP-DOMAIN-KNOWLEDGE-VALIDATION
    - CAP-DOMAIN-KNOWLEDGE-ACCESS
    - CAP-DOMAIN-REASONING
    - CAP-DOMAIN-GENERATION
    - CAP-DOMAIN-GOVERNANCE

  status: active
```

---

# Capability Domains

Dominios iniciales:

```text
knowledge_ingestion
knowledge_validation
knowledge_transformation
knowledge_graph
indexing
knowledge_access
retrieval
ranking
reasoning
generation
policy
agentic_execution
observability
administration
```

---

# Capability Family

Una **Capability Family** agrupa capacidades relacionadas.

Formato recomendado:

```text
CAP-FAMILY-XXXXXX
```

---

# Ejemplo

```yaml
capability_family:
  id: CAP-FAMILY-RETRIEVAL

  domain: knowledge_access

  members:
    - CAP-LEXICAL-RETRIEVAL
    - CAP-VECTOR-RETRIEVAL
    - CAP-HYBRID-RETRIEVAL
    - CAP-GRAPH-RETRIEVAL
    - CAP-STATEMENT-RETRIEVAL
```

---

# Capability Hierarchy

Una Capability podrá declarar:

- parent;
- children;
- specialization;
- alternatives;
- composition.

---

# Ejemplo

```text
CAP-RETRIEVAL
    ├── CAP-LEXICAL-RETRIEVAL
    ├── CAP-VECTOR-RETRIEVAL
    ├── CAP-GRAPH-RETRIEVAL
    └── CAP-HYBRID-RETRIEVAL
```

---

# Generic Capability

Representa una necesidad amplia.

Ejemplo:

```text
CAP-RETRIEVAL
```

---

# Specialized Capability

Representa una semántica más concreta.

Ejemplo:

```text
CAP-HYBRID-RETRIEVAL
```

---

# Capability Specialization

Formato recomendado:

```text
CAP-SPECIALIZATION-XXXXXX
```

---

# Contrato

```yaml
capability_specialization:
  child:
    id: CAP-HYBRID-RETRIEVAL
    version: 2.0.0

  parent:
    id: CAP-RETRIEVAL
    version: 1.0.0

  compatibility:
    satisfies_parent: true

  additional_requirements:
    - lexical_index
    - vector_index
```

---

# Substitutability

Una Capability especializada podrá satisfacer una necesidad genérica si:

- conserva semántica;
- cumple contrato;
- no añade side effects incompatibles;
- respeta límites;
- la política lo permite.

---

# No substitución inversa automática

Una Capability genérica no satisface necesariamente una especializada.

---

# Capability Alias

Podrá existir un alias gobernado.

```text
retrieval.standard
```

podrá resolver a:

```text
CAP-HYBRID-RETRIEVAL@2.0.0
```

---

# Alias Resolution

Deberá quedar fijada para cada resolución.

---

# Capability Dependency

Una **Capability Dependency** representa otra Capability necesaria.

Formato recomendado:

```text
CAP-DEPENDENCY-XXXXXX
```

---

# Tipos

```text
required
optional
conditional
runtime
data
infrastructure
policy
model
```

---

# Contrato

```yaml
capability_dependency:
  id: CAP-DEPENDENCY-HYBRID-VECTOR

  capability:
    id: CAP-HYBRID-RETRIEVAL
    version: 2.0.0

  depends_on:
    capability:
      id: CAP-VECTOR-RETRIEVAL
      version_constraint: 2.x

  type: required
```

---

# Required Dependency

Debe estar disponible.

---

# Optional Dependency

Mejora la Capability, pero no es imprescindible.

---

# Conditional Dependency

Solo se necesita bajo una condición.

---

# Ejemplo

```yaml
condition:
  feature_required: citations
```

---

# Runtime Dependency

Se resuelve durante ejecución.

---

# Infrastructure Dependency

Ejemplos:

- Vector Index;
- Graph Store;
- GPU;
- Model Provider.

---

# Policy Dependency

Requiere un Policy Engine o una decisión previa.

---

# Model Dependency

Requiere un modelo concreto o rango compatible.

---

# Dependency Closure

El Capability Resolver deberá calcular todas las dependencias transitivas.

---

# Dependency Cycle

No deberán existir ciclos obligatorios irresolubles.

Error:

```text
ENGINE_CAPABILITY_DEPENDENCY_CYCLE
```

---

# Dependency Satisfaction

Estados:

```text
satisfied
satisfied_with_degradation
unsatisfied
unknown
not_applicable
```

---

# Capability Composition

Una **Composite Capability** combina varias capacidades.

Formato recomendado:

```text
CAP-COMPOSITE-XXXXXX
```

---

# Ejemplo

```text
CAP-RAG-ANSWERING
=
CAP-RETRIEVAL
+
CAP-CONTEXT-ASSEMBLY
+
CAP-GENERATION
+
CAP-CITATION-RESOLUTION
```

---

# Composite Capability Contract

```yaml
composite_capability:
  id: CAP-RAG-ANSWERING

  version: 1.0.0

  components:
    all:
      - CAP-HYBRID-RETRIEVAL@2.x
      - CAP-CONTEXT-ASSEMBLY@1.x
      - CAP-GROUNDED-GENERATION@2.x
      - CAP-CITATION-RESOLUTION@1.x

  execution:
    mode: orchestrated
```

---

# Composition Modes

```text
single_engine
multi_engine
orchestrated
pipeline
fallback
ensemble
```

---

# Single Engine

Un único Engine implementa la composición.

---

# Multi-Engine

Varias Engines colaboran.

---

# Orchestrated

El Orquestador materializa varias Activities.

---

# Pipeline

Las capacidades se ejecutan secuencialmente.

---

# Fallback

Una Capability sustituye a otra si falla.

---

# Ensemble

Varias implementaciones producen resultados combinados.

---

# Capability Bundle

Un Engine podrá anunciar un bundle optimizado.

Ejemplo:

```text
Retrieval + Reranking + Citation
```

---

# Bundle Benefit

Podrá reducir:

- latencia;
- transferencias;
- coste;
- complejidad.

---

# Bundle Risk

Podrá aumentar:

- acoplamiento;
- opacidad;
- dependencia de proveedor;
- dificultad de sustitución.

---

# Composition Policy

Deberá decidir cuándo preferir:

- Engine único;
- Engines independientes;
- bundle;
- pipeline.

---

# Capability Requirement

Un **Capability Requirement** expresa una necesidad concreta de ejecución.

Formato recomendado:

```text
CAP-REQUIREMENT-XXXXXX
```

---

# Contrato

```yaml
capability_requirement:
  id: CAP-REQUIREMENT-000041

  capability:
    id: CAP-HYBRID-RETRIEVAL
    version_constraint: 2.x

  operation:
    id: ENGINE-OP-RETRIEVE
    version_constraint: 2.x

  contracts:
    request: HYBRID-RETRIEVAL-REQUEST@2.0.0
    response: HYBRID-RETRIEVAL-RESULT@2.0.0

  required_features:
    - FEATURE-STREAMING
    - FEATURE-CITATIONS

  context:
    tenant: TENANT-0001
    environment: production
    classification: internal
    language: es

  objectives:
    latency_p95_ms:
      maximum: 500

    cost:
      maximum: 0.05
      currency: EUR
```

---

# Requirement Sources

Podrá proceder de:

- Activity Definition;
- Workflow Step;
- Execution Profile;
- Agent Plan;
- API Request;
- Policy;
- Tenant Profile;
- Environment Profile.

---

# Requirement Precedence

Orden recomendado:

```text
Security Policy
↓
Environment Policy
↓
Workflow Hard Requirements
↓
Activity Requirements
↓
Tenant Limits
↓
Execution Preferences
↓
Request Preferences
```

---

# No override de seguridad desde Request

---

# Hard Requirement

Debe cumplirse.

---

# Soft Requirement

Influye en ranking.

---

# Conditional Requirement

Se aplica si una condición es cierta.

---

# Derived Requirement

Se infiere de:

- input data;
- selected operation;
- Artifact;
- classification;
- workflow mode.

---

# Requirement Set

Formato recomendado:

```text
CAP-REQUIREMENT-SET-XXXXXX
```

---

# Contrato

```yaml
capability_requirement_set:
  id: CAP-REQUIREMENT-SET-000041

  hard:
    - CAP-REQ-SECURITY-0001
    - CAP-REQ-CONTRACT-0001
    - CAP-REQ-STREAMING-0001

  soft:
    - CAP-REQ-LOW-LATENCY-0001
    - CAP-REQ-LOW-COST-0001

  fallback:
    profile: CAP-FALLBACK-PROFILE-RETRIEVAL
```

---

# Activity Requirement

Una **Activity Requirement** relaciona una Activity del Orquestador con una Capability.

Formato recomendado:

```text
ACT-CAP-REQUIREMENT-XXXXXX
```

---

# Contrato

```yaml
activity_capability_requirement:
  id: ACT-CAP-REQUIREMENT-RUN-RETRIEVAL

  activity:
    id: ACT-RUN-RETRIEVAL
    version: 2.0.0

  capability:
    id: CAP-HYBRID-RETRIEVAL
    version_constraint: 2.x

  operation:
    name: retrieve

  characteristics:
    read_only: true
    idempotent: true
    cancellable: true

  required_contracts:
    input: HYBRID-RETRIEVAL-REQUEST@2.0.0
    output: HYBRID-RETRIEVAL-RESULT@2.0.0
```

---

# Activity-to-Capability Resolution

El **Activity Capability Resolver** transforma una Activity en requisitos.

Formato recomendado:

```text
ACT-CAP-RESOLVER-XXXXXX
```

---

# Flujo

```text
Activity Definition
        ↓
Resolve Capability Requirement
        ↓
Merge Workflow Constraints
        ↓
Merge Execution Context
        ↓
Apply Policy Constraints
        ↓
Produce Requirement Set
```

---

# Resolution Result

```yaml
activity_capability_resolution:
  id: ACT-CAP-RESOLUTION-000041

  activity:
    id: ACT-RUN-RETRIEVAL
    version: 2.0.0

  requirements:
    id: CAP-REQUIREMENT-SET-000041

  resolution:
    capability: CAP-HYBRID-RETRIEVAL@2.x
    operation: ENGINE-OP-RETRIEVE@2.x

  status: resolved
```

---

# Unresolved Activity

Error:

```text
ENGINE_ACTIVITY_CAPABILITY_UNRESOLVED
```

---

# Ambiguous Resolution

Si una Activity puede mapearse a varias Capabilities deberá existir:

- profile;
- selector;
- explicit alternative set;
- policy.

---

# Capability Feature Model

Una **Feature** describe una propiedad opcional o modo de prestación.

---

# Feature Categories

```text
interface
execution
quality
data
security
observability
model
operational
```

---

# Ejemplos

```text
streaming
batch
structured_output
citations
explainability
multilingual
checkpointing
cancellation
shadow_mode
deterministic_seed
tool_calling
```

---

# Feature Definition

```yaml
engine_feature:
  id: FEATURE-CITATIONS

  version: 1.0.0

  category: quality

  semantics:
    description: >
      El resultado incluye referencias verificables
      a evidencia de origen.

  contract_extensions:
    response_fields:
      - citations
```

---

# Feature Support

Estados:

```text
required
supported
partially_supported
unsupported
experimental
deprecated
```

---

# Feature Implementation

```yaml
feature_implementation:
  feature:
    id: FEATURE-CITATIONS
    version: 1.0.0

  engine_definition:
    id: ENGINE-DEF-RAG-PRIMARY
    version: 2.0.0

  status: supported

  limitations:
    maximum_citations: 50
```

---

# Feature Dependency

Una Feature podrá depender de otra.

Ejemplo:

```text
structured_citations
→
structured_output
```

---

# Feature Conflict

Ejemplo:

```text
deterministic_mode
```

podría ser incompatible con:

```text
high_creativity_profile
```

---

# Feature Constraint Solver

Deberá detectar:

- missing feature;
- incompatible features;
- required extension;
- unsupported combination.

---

# Operation Semantics

Cada Operation deberá declarar semántica suficiente para el matching.

---

# Semantics Contract

```yaml
operation_semantics:
  operation:
    id: ENGINE-OP-RETRIEVE
    version: 2.0.0

  execution:
    mode: synchronous

  effects:
    side_effecting: false

  reliability:
    idempotent: true
    retryable: true
    reconcilable: true

  control:
    cancellable: true
    timeout_supported: true

  delivery:
    streaming: true
    batch: true
```

---

# Semantic Compatibility

Un candidato deberá respetar la semántica requerida.

---

# Ejemplo incompatible

Activity requiere:

```text
read_only = true
```

Operation declara:

```text
side_effecting = true
```

Resultado:

```text
incompatible
```

---

# Contract Matching

El **Contract Matcher** compara los contratos requeridos y ofrecidos.

Formato recomendado:

```text
ENGINE-CONTRACT-MATCHER-XXXXXX
```

---

# Dimensiones

```text
schema
version
required_fields
types
nullability
enums
constraints
semantics
errors
streaming
partial_results
```

---

# Contract Match Result

```yaml
contract_match:
  required:
    id: HYBRID-RETRIEVAL-REQUEST
    version: 2.0.0

  offered:
    id: HYBRID-RETRIEVAL-REQUEST
    version: 2.1.0

  compatibility:
    schema: compatible
    semantics: compatible
    defaults: compatible
    errors: compatible

  result: compatible
```

---

# Match States

```text
exact
compatible
compatible_with_adapter
compatible_with_transformation
incompatible
unknown
```

---

# Exact

Mismo contrato y versión.

---

# Compatible

Diferente versión, pero compatible.

---

# Compatible with Adapter

Necesita Adapter.

---

# Compatible with Transformation

Necesita transformación de datos autorizada.

---

# Incompatible

No puede utilizarse.

---

# Unknown

No deberá aceptarse para producción crítica.

---

# Input Compatibility

El Engine deberá aceptar todos los inputs requeridos.

---

# Output Compatibility

El consumidor deberá entender todos los outputs obligatorios.

---

# Error Compatibility

El Orquestador deberá poder interpretar:

- códigos;
- retryability;
- categories;
- unknown outcomes.

---

# Schema Evolution

Cambios típicamente compatibles:

- campo opcional nuevo;
- enum ampliado si consumidor tolera desconocidos;
- metadata adicional.

---

# Cambios típicamente incompatibles

- campo requerido nuevo;
- tipo modificado;
- semántica alterada;
- campo eliminado;
- error retryable convertido en terminal sin versionado.

---

# Semantic Contract

Además del schema podrá existir una semántica formal.

---

# Ejemplo

```yaml
semantic_contract:
  score:
    range:
      minimum: 0
      maximum: 1

    direction: higher_is_better
```

---

# Adapter Matching

El **Adapter Matcher** determina si existe un Engine Adapter compatible.

---

# Inputs

- Activity;
- Operation;
- Protocol;
- Contracts;
- Engine Version;
- Authentication Profile;
- streaming mode.

---

# Adapter Match Contract

```yaml
adapter_match:
  activity:
    id: ACT-RUN-RETRIEVAL
    version: 2.0.0

  engine_operation:
    id: ENGINE-OP-RETRIEVE
    version: 2.1.0

  adapter:
    id: EXEC-ADAPTER-RETRIEVAL
    version: 1.4.0

  compatibility: compatible
```

---

# No Adapter

Si la invocación requiere Adapter y no existe:

```text
ENGINE_ADAPTER_NOT_FOUND
```

---

# Adapter Preference

Podrá preferirse:

- internal;
- latest compatible;
- lower overhead;
- streaming-native;
- security-approved.

---

# Protocol Matching

El consumidor deberá soportar al menos un protocolo ofrecido.

---

# Protocol Requirement

```yaml
protocol_requirement:
  allowed:
    - grpc
    - http

  preferred:
    - grpc

  streaming_required: true
```

---

# Protocol Incompatibility

Ejemplo:

- Activity requiere streaming bidireccional;
- Engine solo ofrece HTTP síncrono.

Resultado:

```text
incompatible
```

---

# Resource Requirement

Un **Resource Requirement** describe recursos necesarios.

Formato recomendado:

```text
ENGINE-RESOURCE-REQ-XXXXXX
```

---

# Resource Types

```text
cpu
memory
gpu
storage
network
token_budget
external_api
index
knowledge_graph
model
session
```

---

# Contrato

```yaml
resource_requirement:
  id: ENGINE-RESOURCE-REQ-000041

  resources:
    cpu:
      minimum_cores: 2

    memory:
      minimum_gb: 8

    vector_index:
      snapshot_id: IDX-SNAP-20260802-0001

    gpu:
      required: false
```

---

# Engine Resource Profile

```yaml
engine_resource_profile:
  id: ENGINE-RESOURCE-PROFILE-RAG-HIGH-QUALITY

  consumption:
    gpu_units: 1
    memory_gb: 24
    estimated_duration: PT10S

  concurrency_weight: 4
```

---

# Resource Availability

El matching deberá comprobar:

- recurso soportado;
- recurso presente;
- versión;
- snapshot;
- capacity;
- reservation;
- locality.

---

# Capacity Class

Una **Capacity Class** normaliza perfiles de capacidad.

Formato recomendado:

```text
ENGINE-CAPACITY-CLASS-XXXXXX
```

---

# Clases iniciales

```text
micro
small
medium
large
xlarge
gpu_small
gpu_large
high_memory
high_throughput
low_latency
```

---

# Contrato

```yaml
capacity_class:
  id: ENGINE-CAPACITY-CLASS-LARGE

  limits:
    maximum_concurrency:
      minimum: 100

    throughput_per_second:
      minimum: 500
```

---

# Capacity Requirement

```yaml
capacity_requirement:
  minimum_available_concurrency: 5
  maximum_queue_depth: 50
  saturation_below: 0.80
```

---

# Capacity Eligibility

Una Instance sin capacidad suficiente podrá:

- excluirse;
- mantenerse como fallback;
- recibir penalización;
- esperar reserva.

---

# Scheduling Hint

Un **Scheduling Hint** orienta al Scheduler o Selector.

Formato recomendado:

```text
ENGINE-SCHED-HINT-XXXXXX
```

---

# Tipos

```text
prefer_region
prefer_local_data
prefer_warm_instance
prefer_low_load
prefer_same_provider
avoid_provider
prefer_gpu
avoid_cold_start
critical_path
sticky_session
```

---

# Contrato

```yaml
scheduling_hint:
  id: ENGINE-SCHED-HINT-LOCAL-INDEX

  type: prefer_local_data

  resource:
    snapshot_id: IDX-SNAP-20260802-0001

  weight: 0.20
```

---

# Hint no equivale a Constraint

Un hint puede ignorarse si no viola semántica.

---

# Affinity

La **Affinity** expresa preferencia por una relación.

---

# Affinity Types

```text
engine
instance
provider
region
data
model
tenant
session
workflow
artifact
```

---

# Affinity Contract

```yaml
engine_affinity:
  id: ENGINE-AFFINITY-DATA-LOCALITY

  type: data

  target:
    snapshot_id: IDX-SNAP-20260802-0001

  strength: preferred
  weight: 0.25
```

---

# Affinity Strength

```text
required
preferred
weak
```

---

# Required Affinity

Funciona como hard constraint.

---

# Preferred Affinity

Aumenta score.

---

# Sticky Affinity

Útil para:

- sesiones;
- cachés;
- stateful Engines;
- warm models.

---

# Affinity Expiration

Podrá caducar.

---

# Anti-Affinity

La **Anti-Affinity** evita un candidato o relación.

---

# Casos

- evitar mismo Provider;
- evitar misma región;
- distribuir carga;
- aislamiento de tenant;
- evitar Instance con fallo previo;
- reducir correlated failure.

---

# Anti-Affinity Contract

```yaml
engine_anti_affinity:
  id: ENGINE-ANTI-AFFINITY-PROVIDER-DIVERSITY

  type: provider

  target:
    id: ENGINE-PROVIDER-EXTERNAL-001

  strength: preferred
  weight: 0.15
```

---

# Hard Anti-Affinity

Excluye.

---

# Soft Anti-Affinity

Penaliza.

---

# Data Locality

La **Data Locality** indica cercanía entre Engine y datos.

---

# Locality Levels

```text
same_process
same_host
same_zone
same_region
cross_region
external
unknown
```

---

# Data Locality Contract

```yaml
data_locality:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  resource:
    id: IDX-SNAP-20260802-0001

  locality: same_region

  confidence: 1.0
```

---

# Locality Benefits

- menor latencia;
- menor coste de red;
- menor exposición;
- mejor throughput.

---

# Locality as Hard Constraint

Podrá ser obligatoria por:

- residencia;
- clasificación;
- volumen;
- política.

---

# Region Affinity

Podrá considerar:

- user region;
- data region;
- execution region;
- failover region.

---

# Tenant Affinity

Un Engine podrá mantener:

- tenant-specific cache;
- tenant-specific model;
- isolated deployment.

---

# Model Affinity

Una Activity podrá requerir:

- model family;
- exact model;
- tokenizer;
- weights version;
- fine-tune;
- safety profile.

---

# Model Requirement

```yaml
model_requirement:
  family: MODEL-FAMILY-GENERATIVE-TEXT
  version_constraint: 3.x
  structured_output: true
  minimum_context_tokens: 32768
```

---

# Cost Profile

Un **Cost Profile** describe el coste estimado.

Formato recomendado:

```text
ENGINE-COST-PROFILE-XXXXXX
```

---

# Cost Dimensions

```text
per_request
per_token
per_second
per_batch
per_gpu_second
storage
network
fixed
minimum_charge
```

---

# Contrato

```yaml
engine_cost_profile:
  id: ENGINE-COST-PROFILE-RAG-STANDARD

  currency: EUR

  pricing:
    input_token: 0.000001
    output_token: 0.000003
    request_base: 0.001

  effective_from: 2026-08-01T00:00:00Z

  provenance:
    source: provider_contract
```

---

# Cost Estimate

```yaml
engine_cost_estimate:
  instance:
    id: ENGINE-INSTANCE-RAG-EU-001

  request:
    estimated_input_tokens: 12000
    estimated_output_tokens: 1200

  estimated_cost:
    value: 0.0166
    currency: EUR

  confidence: 0.83
```

---

# Cost Hard Limit

Si supera el budget:

```text
candidate excluded
```

---

# Cost Preference

Podrá penalizar candidatos caros.

---

# Cost Freshness

Los perfiles externos deberán tener fecha de vigencia.

---

# Latency Profile

Un **Latency Profile** describe comportamiento temporal.

Formato recomendado:

```text
ENGINE-LATENCY-PROFILE-XXXXXX
```

---

# Contrato

```yaml
engine_latency_profile:
  id: ENGINE-LATENCY-PROFILE-RETRIEVAL-EU

  operation:
    id: ENGINE-OP-RETRIEVE
    version: 2.0.0

  measurements:
    p50_ms: 80
    p95_ms: 220
    p99_ms: 480

  conditions:
    region: eu-west
    payload_class: medium

  observed_at: 2026-08-02T20:00:00Z
```

---

# Latency Sources

- benchmark;
- production metrics;
- synthetic tests;
- provider SLA;
- historical execution.

---

# Effective Latency

Podrá considerar:

```text
network
+
queue
+
cold start
+
execution
+
response transfer
```

---

# Cold Start Profile

Los Engines con warmup deberán declararlo.

```yaml
cold_start:
  expected_duration: PT30S
  warm_instance_available: true
```

---

# Latency Requirement

```yaml
latency_requirement:
  p95_ms:
    maximum: 500

  first_item_ms:
    maximum: 200
```

---

# Streaming Latency

Deberá distinguir:

- time to first item;
- total duration.

---

# Quality Profile

Un **Quality Profile** representa calidad observada o certificada.

Formato recomendado:

```text
ENGINE-QUALITY-PROFILE-XXXXXX
```

---

# Quality Dimensions

```text
accuracy
precision
recall
grounding
citation_validity
schema_compliance
hallucination_rate
coverage
consistency
relevance
```

---

# Contrato

```yaml
engine_quality_profile:
  id: ENGINE-QUALITY-PROFILE-RAG-HQ

  capability:
    id: CAP-RAG-GENERATION
    version: 2.0.0

  metrics:
    grounding_score: 0.94
    citation_validity: 0.98
    schema_compliance: 0.995

  benchmark:
    id: BENCH-RAG-CULINARY-2026-08

  observed_at: 2026-08-01T00:00:00Z
```

---

# Quality Profile Provenance

Deberá indicar:

- benchmark;
- dataset;
- evaluator;
- model version;
- environment;
- sample size.

---

# No comparar métricas de benchmarks incompatibles

---

# Quality Requirement

```yaml
quality_requirement:
  grounding_score:
    minimum: 0.90

  citation_validity:
    minimum: 0.95
```

---

# Reliability Profile

Un **Reliability Profile** describe estabilidad operativa.

---

# Dimensiones

```text
availability
success_rate
timeout_rate
retry_rate
unknown_outcome_rate
recovery_rate
contract_violation_rate
```

---

# Contrato

```yaml
engine_reliability_profile:
  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  window: PT24H

  metrics:
    success_rate: 0.998
    timeout_rate: 0.001
    contract_violation_rate: 0.0001
```

---

# Reliability Requirement

Podrá exigir:

```text
success_rate >= 0.995
```

---

# Sustainability Profile

Podrá describir consumo y eficiencia.

Formato recomendado:

```text
ENGINE-SUSTAINABILITY-PROFILE-XXXXXX
```

---

# Dimensiones

- energy per request;
- GPU time;
- carbon region factor;
- batch efficiency;
- idle efficiency.

---

# Uso

Será normalmente una preferencia, salvo políticas específicas.

---

# Context Window

Los Engines basados en modelos deberán declarar límites de contexto.

---

# Context Window Contract

```yaml
context_window:
  maximum_tokens: 32768

  reserved_output_tokens: 4096

  effective_input_tokens: 28672
```

---

# Token Limit Types

```text
input
output
total
per_minute
per_day
tenant
provider
```

---

# Token Requirement

```yaml
token_requirement:
  estimated_input_tokens: 24000
  requested_output_tokens: 2000
```

---

# Token Compatibility

El candidato deberá admitir:

```text
input + reserved output <= total context
```

---

# Token Safety Margin

Se recomienda reservar margen.

```yaml
safety_margin: 0.10
```

---

# Batch Support

Una Operation podrá admitir procesamiento por lotes.

---

# Batch Contract

```yaml
batch_support:
  supported: true
  maximum_items: 128
  maximum_total_tokens: 100000
  partial_failure: collect
```

---

# Batch Requirements

- batch size;
- ordering;
- partial failure;
- atomicity;
- result correlation.

---

# Streaming Support

Una Operation podrá producir stream.

---

# Streaming Modes

```text
server_stream
client_stream
bidirectional
event_stream
chunked_response
```

---

# Streaming Contract

```yaml
streaming_support:
  mode: server_stream

  item_contract:
    id: RAG-STREAM-ITEM
    version: 1.0.0

  ordering: guaranteed

  cancellation: supported
```

---

# Streaming Requirement

Si es obligatorio y el Engine no lo soporta:

```text
candidate excluded
```

---

# Data Classification Constraint

El matching deberá respetar clasificación.

---

# Classification Levels

Ejemplo inicial:

```text
public
internal
confidential
restricted
```

---

# Engine Classification Support

```yaml
data_classification_support:
  maximum: internal

  allowed:
    - public
    - internal

  personal_data:
    allowed: false
```

---

# Classification Rule

Un Engine no podrá procesar un nivel superior al permitido.

---

# Data Residency Constraint

Define dónde pueden procesarse o almacenarse datos.

---

# Contrato

```yaml
data_residency_constraint:
  allowed_regions:
    - eu-west
    - eu-central

  cross_region_transfer: false

  external_processing: false
```

---

# Processing vs Storage Residency

Deberán diferenciarse.

---

# Data Retention Constraint

Podrá exigir:

```text
no request retention
```

o:

```text
maximum retention = 0
```

---

# Training Usage Constraint

Para proveedores externos:

```yaml
training_usage:
  request_data_allowed: false
```

---

# Candidate Eligibility

Un candidato será elegible cuando supere todos los filtros obligatorios.

---

# Eligibility Pipeline

```text
Definition Active?
        ↓
Capability Match?
        ↓
Operation Match?
        ↓
Contract Compatible?
        ↓
Adapter Available?
        ↓
Security Compatible?
        ↓
Scope Compatible?
        ↓
Availability Acceptable?
        ↓
Capacity Acceptable?
        ↓
Resource Requirements Met?
        ↓
Candidate Eligible
```

---

# Eligibility Result

```yaml
candidate_eligibility:
  candidate:
    instance: ENGINE-INSTANCE-RETRIEVAL-EU-001

  checks:
    capability: passed
    operation: passed
    contract: passed
    adapter: passed
    security: passed
    availability: passed
    capacity: passed
    resources: passed

  result: eligible
```

---

# Exclusion Reason

Cada exclusión deberá tener código estructurado.

---

# Ejemplos

```text
capability_missing
contract_incompatible
classification_exceeded
region_not_allowed
instance_unavailable
capacity_insufficient
adapter_missing
cost_limit_exceeded
```

---

# Candidate Matching

El **Capability Matching Engine** evalúa candidatos elegibles.

Formato recomendado:

```text
ENGINE-CAPABILITY-MATCHER-XXXXXX
```

---

# Inputs

- Requirement Set;
- Engine Definitions;
- Capability Implementations;
- Instances;
- Operational State;
- Profiles;
- Policy;
- Registry Snapshot.

---

# Output

- eligible candidates;
- excluded candidates;
- scores;
- explanations;
- fallback candidates.

---

# Match Request

```yaml
engine_match_request:
  id: ENGINE-MATCH-REQUEST-000041

  requirements:
    id: CAP-REQUIREMENT-SET-000041

  context:
    execution_id: EXEC-000041
    activity_id: ACT-RUN-RETRIEVAL@2.0.0

  selection_profile:
    id: ENGINE-SELECTION-PROFILE-BALANCED

  include_excluded: true
```

---

# Match Result

```yaml
engine_match_result:
  id: ENGINE-MATCH-RESULT-000041

  request:
    id: ENGINE-MATCH-REQUEST-000041

  eligible:
    - ENGINE-CANDIDATE-000041
    - ENGINE-CANDIDATE-000042

  excluded:
    - ENGINE-CANDIDATE-000043

  registry_snapshot:
    id: ENGINE-REGISTRY-SNAPSHOT-20260802-0001

  operational_observed_at: 2026-08-02T20:00:20Z
```

---

# Candidate

Formato recomendado:

```text
ENGINE-CANDIDATE-XXXXXX
```

---

# Contrato

```yaml
engine_candidate:
  id: ENGINE-CANDIDATE-000041

  definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  instance:
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  capability:
    id: CAP-HYBRID-RETRIEVAL
    version: 2.0.0

  operation:
    id: ENGINE-OP-RETRIEVE
    version: 2.0.0

  adapter:
    id: EXEC-ADAPTER-RETRIEVAL
    version: 1.4.0

  eligibility: eligible

  score:
    total: 0.91

  rank: 1
```

---

# Candidate Scoring

El scoring deberá aplicarse únicamente a candidatos elegibles.

---

# Score Dimensions

```text
functional_fit
contract_fit
availability
capacity
latency
quality
cost
reliability
affinity
locality
sustainability
provider_preference
version_preference
```

---

# Score Range

Recomendado:

```text
0.0 – 1.0
```

---

# Score Contract

```yaml
candidate_score:
  candidate:
    id: ENGINE-CANDIDATE-000041

  dimensions:
    functional_fit: 1.00
    contract_fit: 1.00
    availability: 0.95
    capacity: 0.88
    latency: 0.93
    quality: 0.92
    cost: 0.80
    reliability: 0.98
    affinity: 0.90

  total: 0.91
```

---

# Selection Profile

Un **Selection Profile** define ponderaciones y prioridades.

Formato recomendado:

```text
ENGINE-SELECTION-PROFILE-XXXXXX
```

---

# Perfil balanced

```yaml
engine_selection_profile:
  id: ENGINE-SELECTION-PROFILE-BALANCED

  version: 1.0.0

  weights:
    quality: 0.25
    latency: 0.20
    reliability: 0.20
    cost: 0.15
    capacity: 0.10
    affinity: 0.10
```

---

# Perfil low_latency

```yaml
weights:
  latency: 0.45
  capacity: 0.20
  reliability: 0.15
  quality: 0.10
  cost: 0.10
```

---

# Perfil high_quality

```yaml
weights:
  quality: 0.50
  reliability: 0.20
  latency: 0.10
  cost: 0.05
  affinity: 0.15
```

---

# Perfil low_cost

```yaml
weights:
  cost: 0.50
  reliability: 0.20
  latency: 0.10
  quality: 0.10
  capacity: 0.10
```

---

# Perfil critical

Podrá priorizar:

- reliability;
- exact version;
- trusted internal;
- regional redundancy;
- no experimental.

---

# Weight Validation

La suma deberá normalizarse.

---

# No pesos negativos salvo penalización explícita

---

# Score Normalization

Las métricas heterogéneas deberán normalizarse.

---

# Latency Normalization

Ejemplo:

```text
menor latencia
→
mayor score
```

---

# Cost Normalization

```text
menor coste
→
mayor score
```

---

# Quality Normalization

```text
mayor calidad
→
mayor score
```

---

# Missing Metric

La política podrá:

```text
exclude
use_default
penalize
ignore_dimension
require_review
```

---

# Recomendación

Para métricas críticas:

```text
exclude or penalize strongly
```

---

# Confidence-Adjusted Score

Las métricas podrán ponderarse por confianza.

```text
effective_score
=
raw_score × confidence
```

---

# Freshness-Adjusted Score

Los datos stale podrán recibir penalización.

---

# Score Cap

Un health degradado podrá limitar la puntuación máxima.

---

# Example

```text
health = degraded
→ total score cannot exceed 0.75
```

---

# Hard Filters

Deberán aplicarse antes del scoring.

---

# Hard Filter Categories

```text
security
contract
capability
operation
scope
lifecycle
availability
resource
budget
residency
adapter
```

---

# Soft Preferences

Ejemplos:

- región preferida;
- menor coste;
- menor latencia;
- Engine warm;
- Provider preferido;
- data locality;
- version más reciente compatible.

---

# Candidate Ranking

Se ordenará por:

1. eligibility;
2. total score;
3. tie-break rules.

---

# Tie-Breaking

Orden recomendado:

```text
higher reliability
↓
better availability
↓
lower latency
↓
lower cost
↓
stable deterministic ID
```

---

# Stable Tie-Break

Deberá permitir reproducibilidad.

---

# Randomized Selection

Podrá utilizarse para:

- load distribution;
- canary;
- experimentation;

pero deberá:

- estar autorizado;
- utilizar seed persistida;
- registrar decisión.

---

# Candidate Diversity

Para listas de fallback podrá evitarse devolver candidatos demasiado correlacionados.

---

# Diversity Dimensions

- Provider;
- region;
- model family;
- infrastructure;
- deployment.

---

# Fallback Candidate Set

Podrá preferirse:

```text
primary candidate
+
different provider
+
different region
```

---

# Correlated Failure Penalty

Candidatos dependientes del mismo recurso podrán penalizarse.

---

# Candidate Explanation

Toda puntuación deberá ser explicable.

---

# Contrato

```yaml
candidate_explanation:
  candidate:
    id: ENGINE-CANDIDATE-000041

  included_because:
    - exact_capability_match
    - contract_compatible
    - trusted_internal
    - region_preferred
    - latency_within_target

  score_contributions:
    quality: 0.230
    latency: 0.186
    reliability: 0.196
    cost: 0.120
    capacity: 0.088
    affinity: 0.090

  penalties:
    - code: CAPACITY_REPORT_NEAR_STALE
      value: 0.009

  total: 0.901
```

---

# Exclusion Explanation

```yaml
candidate_exclusion:
  candidate:
    id: ENGINE-CANDIDATE-000043

  excluded_by:
    code: DATA_CLASSIFICATION_NOT_SUPPORTED

  required:
    classification: internal

  offered:
    maximum_classification: public
```

---

# Matching Decision Record

Formato recomendado:

```text
ENGINE-MATCH-DECISION-XXXXXX
```

---

# Contrato

```yaml
engine_match_decision:
  id: ENGINE-MATCH-DECISION-000041

  request:
    id: ENGINE-MATCH-REQUEST-000041

  selected_candidates:
    - ENGINE-CANDIDATE-000041
    - ENGINE-CANDIDATE-000042

  selection_profile:
    id: ENGINE-SELECTION-PROFILE-BALANCED
    version: 1.0.0

  registry_snapshot:
    id: ENGINE-REGISTRY-SNAPSHOT-20260802-0001

  decided_at: 2026-08-02T20:00:21Z
```

---

# Matching vs Routing

El Matching Engine produce candidatos ordenados.

El Routing Engine, definido en la Parte IV, decidirá:

- candidato final;
- balanceo;
- failover;
- hedging;
- canary;
- retries.

---

# Capability Degradation

Algunos requisitos podrán relajarse bajo un perfil de fallback.

---

# Degradation Profile

Formato recomendado:

```text
CAP-DEGRADATION-PROFILE-XXXXXX
```

---

# Contrato

```yaml
capability_degradation_profile:
  id: CAP-DEGRADATION-PROFILE-RETRIEVAL

  levels:
    - level: 0
      capability: CAP-HYBRID-RETRIEVAL
      required_features:
        - FEATURE-CITATIONS

    - level: 1
      capability: CAP-LEXICAL-RETRIEVAL
      required_features:
        - FEATURE-CITATIONS

    - level: 2
      capability: CAP-LEXICAL-RETRIEVAL
      required_features: []
```

---

# Degradation Rules

No podrán relajarse:

- security;
- tenant isolation;
- residency;
- mandatory validation;
- hard budget;
- non-exemptible Quality Gates.

---

# Degradation Decision

Deberá registrar:

- requirement original;
- nivel;
- garantías perdidas;
- actor o policy;
- resultado.

---

# Capability Ensemble

Varias Engines podrán combinarse.

---

# Ensemble Types

```text
parallel
vote
rank_fusion
fallback
cascade
consensus
specialist
```

---

# Ensemble Requirement

```yaml
capability_ensemble:
  id: CAP-ENSEMBLE-RETRIEVAL-FUSION

  members:
    - CAP-LEXICAL-RETRIEVAL
    - CAP-VECTOR-RETRIEVAL
    - CAP-GRAPH-RETRIEVAL

  aggregation:
    capability: CAP-RANK-FUSION
```

---

# Ensemble Matching

Deberá encontrar un conjunto compatible, no solo un candidato.

---

# Set Constraints

- máximo de miembros;
- diversidad;
- coste total;
- latencia;
- disponibilidad conjunta;
- dependencia común.

---

# Ensemble Score

Podrá considerar:

- calidad combinada;
- coste;
- critical path;
- correlated failure;
- aggregation overhead.

---

# Capability Matching Cache

Los resultados estáticos podrán cachearse parcialmente.

---

# Cacheable Components

- taxonomía;
- specialization;
- static contract compatibility;
- Adapter compatibility;
- Feature support.

---

# Dynamic Components

No deberán cachearse durante mucho tiempo:

- health;
- availability;
- capacity;
- load;
- latency reciente;
- cost dynamic.

---

# Cache Key

Deberá incluir:

```text
Requirement Set
+
Selection Profile
+
Catalog Snapshot
+
Policy Version
+
Operational Freshness Bucket
```

---

# Invalidation

Cambios en:

- quarantine;
- trust;
- Definition lifecycle;
- contract;
- availability;
- lease;

deberán invalidar resultados.

---

# Matching Consistency

La resolución deberá declarar:

- Catalog Snapshot;
- operational observation time;
- Policy version;
- profile version.

---

# Matching Determinism

Con los mismos datos y seed, el resultado deberá ser reproducible.

---

# Observabilidad del Matching

---

# Métricas

- match requests;
- eligible candidates;
- excluded candidates;
- zero-candidate results;
- contract mismatches;
- security exclusions;
- capacity exclusions;
- average scoring latency;
- cache hit rate;
- fallback usage;
- degradation level;
- ensemble size.

---

# Score Distribution

Permitirá detectar:

- falta de diversidad;
- perfiles mal calibrados;
- candidatos dominantes;
- métricas stale.

---

# Exclusion Distribution

Ejemplos:

```text
35 % classification mismatch
20 % capacity unavailable
15 % contract mismatch
```

---

# Profile Usage

- balanced;
- low_latency;
- high_quality;
- low_cost;
- critical.

---

# Candidate Churn

Mide cuánto cambia el ranking.

Un churn alto puede indicar:

- health flapping;
- load instability;
- scoring overly sensitive;
- stale data.

---

# Matching Latency

Deberá medirse por fase:

```text
requirement resolution
eligibility filtering
contract matching
profile lookup
scoring
explanation
```

---

# Logs

```yaml
log:
  event: engine_capability_matched

  execution_id: EXEC-000041
  activity: ACT-RUN-RETRIEVAL@2.0.0

  capability: CAP-HYBRID-RETRIEVAL@2.x

  candidates:
    eligible: 3
    excluded: 5

  selected_profile: ENGINE-SELECTION-PROFILE-BALANCED@1.0.0
  top_candidate: ENGINE-CANDIDATE-000041

  correlation_id: CORR-000041
```

---

# Eventos

Catálogo inicial:

```text
capability_taxonomy_registered
capability_specialization_registered
capability_dependency_registered
composite_capability_registered
activity_capability_resolved
capability_requirement_created
engine_contract_match_completed
engine_adapter_match_completed
engine_candidate_eligible
engine_candidate_excluded
engine_candidate_scored
engine_matching_completed
engine_matching_no_candidates
engine_degradation_applied
engine_ensemble_resolved
engine_selection_profile_updated
```

---

# Evento de candidato excluido

```yaml
event:
  type: engine_candidate_excluded

  subject:
    id: ENGINE-CANDIDATE-000043
    type: engine-candidate

  data:
    reason: DATA_CLASSIFICATION_NOT_SUPPORTED
    required: internal
    supported: public
```

---

# Diagnósticos

Códigos iniciales:

```text
ENGINE_CAPABILITY_TAXONOMY_INVALID
ENGINE_CAPABILITY_PARENT_NOT_FOUND
ENGINE_CAPABILITY_SPECIALIZATION_INVALID
ENGINE_CAPABILITY_DEPENDENCY_UNRESOLVED
ENGINE_CAPABILITY_DEPENDENCY_CYCLE
ENGINE_CAPABILITY_COMPOSITION_INVALID
ENGINE_CAPABILITY_REQUIREMENT_INVALID
ENGINE_ACTIVITY_CAPABILITY_UNRESOLVED
ENGINE_ACTIVITY_CAPABILITY_AMBIGUOUS
ENGINE_FEATURE_NOT_SUPPORTED
ENGINE_FEATURE_COMBINATION_INVALID
ENGINE_OPERATION_SEMANTICS_INCOMPATIBLE
ENGINE_CONTRACT_MATCH_FAILED
ENGINE_CONTRACT_SEMANTICS_INCOMPATIBLE
ENGINE_ADAPTER_NOT_FOUND
ENGINE_ADAPTER_INCOMPATIBLE
ENGINE_PROTOCOL_REQUIREMENT_UNSATISFIED
ENGINE_RESOURCE_REQUIREMENT_UNSATISFIED
ENGINE_CAPACITY_CLASS_UNSATISFIED
ENGINE_CAPACITY_INSUFFICIENT
ENGINE_AFFINITY_UNSATISFIED
ENGINE_ANTI_AFFINITY_VIOLATED
ENGINE_DATA_LOCALITY_UNSATISFIED
ENGINE_MODEL_REQUIREMENT_UNSATISFIED
ENGINE_CONTEXT_WINDOW_INSUFFICIENT
ENGINE_TOKEN_LIMIT_EXCEEDED
ENGINE_BATCH_NOT_SUPPORTED
ENGINE_STREAMING_NOT_SUPPORTED
ENGINE_DATA_CLASSIFICATION_NOT_SUPPORTED
ENGINE_DATA_RESIDENCY_NOT_SUPPORTED
ENGINE_COST_LIMIT_EXCEEDED
ENGINE_LATENCY_LIMIT_EXCEEDED
ENGINE_QUALITY_THRESHOLD_UNSATISFIED
ENGINE_RELIABILITY_THRESHOLD_UNSATISFIED
ENGINE_CANDIDATE_NOT_ELIGIBLE
ENGINE_CANDIDATE_SCORE_INVALID
ENGINE_SELECTION_PROFILE_INVALID
ENGINE_MATCHING_NO_CANDIDATES
ENGINE_DEGRADATION_NOT_ALLOWED
ENGINE_ENSEMBLE_CONSTRAINT_UNSATISFIED
ENGINE_MATCHING_DATA_STALE
```

---

# Diagnostic Contract

```yaml
engine_matching_diagnostic:
  id: ENGINE-MATCH-DIAGNOSTIC-000041

  code: ENGINE_CONTEXT_WINDOW_INSUFFICIENT
  severity: error

  candidate:
    instance: ENGINE-INSTANCE-RAG-EU-001

  required:
    effective_input_tokens: 24000
    requested_output_tokens: 4000

  offered:
    total_context_tokens: 24576

  retryable: false
```

---

# Quality Gate de Capability Taxonomy

```yaml
quality_gate:
  id: QG-CAPABILITY-TAXONOMY-0001

  criteria:
    all:
      - taxonomy_schema_valid == true
      - capability_ids_unique == true
      - parent_references_resolved == true
      - specializations_valid == true
      - dependency_cycles_detected == 0
      - aliases_governed == true
      - capability_versions_valid == true
```

---

# Quality Gate de Capability Requirement

```yaml
quality_gate:
  id: QG-CAPABILITY-REQUIREMENT-0001

  criteria:
    all:
      - requirement_schema_valid == true
      - capability_resolved == true
      - operation_resolved == true
      - hard_and_soft_constraints_separated == true
      - contracts_declared == true
      - security_context_present == true
      - budget_declared == true
      - fallback_profile_valid == true
```

---

# Quality Gate de Contract Matching

```yaml
quality_gate:
  id: QG-ENGINE-CONTRACT-MATCHING-0001

  criteria:
    all:
      - request_contract_compatible == true
      - response_contract_compatible == true
      - error_contract_compatible == true
      - semantic_contract_compatible == true
      - nullability_compatible == true
      - enum_compatibility_valid == true
      - adapter_resolved == true
```

---

# Quality Gate de Resource Matching

```yaml
quality_gate:
  id: QG-ENGINE-RESOURCE-MATCHING-0001

  criteria:
    all:
      - required_resources_resolved == true
      - capacity_sufficient == true
      - data_locality_policy_satisfied == true
      - model_requirements_satisfied == true
      - token_limits_satisfied == true
      - batch_streaming_requirements_satisfied == true
```

---

# Quality Gate de Security Matching

```yaml
quality_gate:
  id: QG-ENGINE-SECURITY-MATCHING-0001

  criteria:
    all:
      - classification_supported == true
      - residency_supported == true
      - tenant_scope_compatible == true
      - trust_level_acceptable == true
      - retention_policy_compatible == true
      - training_usage_policy_compatible == true
      - external_processing_policy_compatible == true
```

---

# Quality Gate de Candidate Scoring

```yaml
quality_gate:
  id: QG-ENGINE-CANDIDATE-SCORING-0001

  criteria:
    all:
      - only_eligible_candidates_scored == true
      - selection_profile_versioned == true
      - weights_normalized == true
      - metrics_freshness_evaluated == true
      - confidence_applied == true
      - hard_constraints_not_overridden == true
      - score_explanation_complete == true
      - tie_breaking_stable == true
```

---

# Quality Gate de Degradation

```yaml
quality_gate:
  id: QG-ENGINE-CAPABILITY-DEGRADATION-0001

  criteria:
    all:
      - degradation_profile_versioned == true
      - guarantees_lost_declared == true
      - non_degradable_constraints_preserved == true
      - policy_authorized == true
      - degradation_level_recorded == true
      - consumer_informed == true
```

---

# Quality Gate de Ensemble

```yaml
quality_gate:
  id: QG-ENGINE-CAPABILITY-ENSEMBLE-0001

  criteria:
    all:
      - ensemble_members_eligible == true
      - aggregation_capability_resolved == true
      - diversity_constraints_satisfied == true
      - total_cost_within_budget == true
      - latency_within_deadline == true
      - correlated_failure_evaluated == true
      - output_contract_valid == true
```

---

# Casos de uso

---

# Caso de uso 1 — Activity a Capability

`ACT-RUN-RETRIEVAL@2.0.0` se resuelve como:

```text
CAP-HYBRID-RETRIEVAL@2.x
```

con Operation:

```text
ENGINE-OP-RETRIEVE@2.x
```

---

# Caso de uso 2 — Specialization

La Activity requiere Retrieval genérico.

Un Hybrid Retrieval Engine satisface el requisito porque su Capability declara substitución válida.

---

# Caso de uso 3 — Dependencia transitiva

RAG Answering requiere:

- Retrieval;
- Context Assembly;
- Generation;
- Citation Resolution.

El Resolver calcula el cierre completo.

---

# Caso de uso 4 — Feature obligatoria

La respuesta debe ser streaming.

Los Engines que no implementan `FEATURE-STREAMING` quedan excluidos.

---

# Caso de uso 5 — Contract Adapter

El Engine implementa Response Contract 2.1.

La Activity espera 2.0.

Un Adapter aprobado convierte la respuesta y el candidato sigue siendo elegible.

---

# Caso de uso 6 — Clasificación incompatible

Un proveedor externo admite solo contenido público.

La Execution utiliza conocimiento interno.

El candidato se excluye antes del scoring.

---

# Caso de uso 7 — Context Window

La petición necesita 28 000 tokens efectivos.

Un modelo de 24 576 queda excluido.

---

# Caso de uso 8 — Bajo coste

El perfil `low_cost` selecciona un Engine menos preciso, pero que sigue superando el umbral mínimo de calidad.

---

# Caso de uso 9 — Alta calidad

El perfil `high_quality` prioriza un Engine con mejor grounding aunque tenga mayor latencia y coste.

---

# Caso de uso 10 — Data Locality

Dos Engines son equivalentes.

Se selecciona el que tiene el índice en la misma región.

---

# Caso de uso 11 — Capacidad baja

La Instance preferida está al 98 % de saturación.

Sigue siendo elegible, pero recibe una penalización fuerte.

---

# Caso de uso 12 — Métrica stale

El Cost Profile es actual, pero el Capacity Report está stale.

El candidato permanece, aunque con penalización y advertencia.

---

# Caso de uso 13 — Degradación controlada

No existe Hybrid Retrieval disponible.

La policy permite degradar a Lexical Retrieval con citas.

La decisión registra garantías reducidas.

---

# Caso de uso 14 — Ensemble

Se seleccionan:

- Lexical Retrieval;
- Vector Retrieval;
- Graph Retrieval;

y se combinan mediante Rank Fusion.

---

# Caso de uso 15 — Fallback diverso

El candidato primario y el secundario pertenecen a regiones y Providers distintos para reducir fallo correlacionado.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Capability como texto libre

Impide taxonomía, versión y compatibilidad.

---

## Seleccionar por Engine Type únicamente

Un mismo Type puede ofrecer capacidades distintas.

---

## Tratar especialización como igualdad

Una Capability especializada puede satisfacer una genérica, pero no siempre al contrario.

---

## Dependencias no declaradas

Generan fallos tardíos.

---

## Composite Capability como Engine monolítico obligatorio

Puede impedir composición flexible.

---

## Feature utilizada como Capability

`streaming` no sustituye a `retrieval`.

---

## Requisitos mezclando hard y soft constraints

Puede permitir violaciones o exclusiones incorrectas.

---

## Request sobrescribiendo políticas

Las preferencias del consumidor no pueden modificar seguridad.

---

## Matching solo por versión

La semántica puede ser incompatible.

---

## Schema compatible pero significado distinto

La compatibilidad semántica también debe evaluarse.

---

## Adapter implícito

Debe existir y estar versionado.

---

## Coste tratado como label

Debe tener unidad, moneda, vigencia y provenance.

---

## Latencia sin percentil ni contexto

Una media aislada es insuficiente.

---

## Quality Score sin benchmark

No permite comparación fiable.

---

## Comparar benchmarks diferentes directamente

Puede producir rankings engañosos.

---

## Reliability global sin ventana temporal

No expresa comportamiento reciente.

---

## Capacity sin TTL

Puede estar obsoleta.

---

## Affinity obligatoria modelada como preferencia

Puede violar statefulness o residencia.

---

## Anti-Affinity sin scope

Puede excluir demasiados candidatos.

---

## Context Window igual a input disponible

Debe reservarse espacio para output y margen.

---

## Batch Support asumido por aceptar listas

Debe existir semántica de fallos y correlación.

---

## Streaming simulado sin contrato

Puede no soportar cancelación ni orden.

---

## Scoring antes de filtrar seguridad

Un score alto nunca debe salvar un candidato inseguro.

---

## Un score universal para todos los casos

Los objetivos cambian por workflow.

---

## Pesos no versionados

Impiden reproducibilidad.

---

## Missing Metrics tratadas como valor óptimo

Favorece Engines sin observabilidad.

---

## Tie-Break aleatorio no registrado

Dificulta auditoría.

---

## Fallback idéntico al primario

No aporta resiliencia.

---

## Degradación silenciosa

El consumidor debe conocer garantías reducidas.

---

## Degradar controles de seguridad

No deberá permitirse.

---

## Ensemble sin presupuesto total

Puede multiplicar coste y latencia.

---

## Cache de matching ignorando Policy Version

Puede devolver candidatos ya no autorizados.

---

## Score sin explicación

Genera selección opaca.

---

# Reglas mínimas de conformidad

---

## Capability Taxonomy

Deberá existir una taxonomía versionada.

---

## Capability IDs

Toda Capability deberá disponer de identidad estable.

---

## Specialization

Las relaciones padre-hijo deberán declararse.

---

## Dependencies

Toda dependencia deberá ser explícita y acíclica.

---

## Composition

Las Composite Capabilities deberán declarar componentes y modo.

---

## Requirements

Toda necesidad deberá expresarse mediante Requirement Set.

---

## Hard y Soft Constraints

Deberán diferenciarse.

---

## Activity Mapping

Toda Activity ejecutable deberá resolver una Capability u Operation.

---

## Feature Model

Las Features deberán estar versionadas.

---

## Operation Semantics

Toda Operation deberá declarar efectos y control.

---

## Contract Matching

Los contratos deberán evaluarse antes de selección.

---

## Semantic Compatibility

No deberá limitarse a schema.

---

## Adapter Matching

Todo Adapter requerido deberá resolverse.

---

## Protocol Matching

El protocolo deberá ser compatible.

---

## Resource Requirements

Los recursos deberán declararse.

---

## Capacity

El candidato deberá tener capacidad suficiente o política explícita.

---

## Affinity

Las afinidades deberán tener fuerza y scope.

---

## Anti-Affinity

Las exclusiones deberán ser gobernadas.

---

## Locality

La cercanía a datos deberá ser evaluable.

---

## Cost Profile

Todo coste utilizado en scoring deberá estar versionado y vigente.

---

## Latency Profile

Toda latencia deberá declarar percentil y contexto.

---

## Quality Profile

Toda calidad deberá conservar benchmark y provenance.

---

## Reliability Profile

Deberá declarar ventana temporal.

---

## Context Limits

Los límites de tokens deberán evaluarse.

---

## Batch y Streaming

El soporte deberá declararse formalmente.

---

## Data Classification

Toda selección deberá respetarla.

---

## Residency

Las regiones y transferencias deberán validarse.

---

## Candidate Eligibility

Solo candidatos compatibles deberán pasar al scoring.

---

## Selection Profiles

Las ponderaciones deberán versionarse.

---

## Scoring

Deberá normalizar métricas y considerar confianza.

---

## Tie-Break

Deberá ser estable.

---

## Explainability

Toda inclusión, exclusión y puntuación deberá explicarse.

---

## Degradation

Deberá estar gobernada y registrada.

---

## Ensemble

Deberá evaluar coste, latencia y diversidad.

---

## Freshness

Los datos operativos stale deberán tratarse.

---

## Matching Context

Todo resultado deberá declarar Snapshot, Policy y observation time.

---

# Conformidad de Capability Taxonomy

Será conforme cuando:

- tenga ID;
- tenga versión;
- declare domains;
- declare families;
- preserve hierarchy;
- declare specializations;
- no contenga ciclos;
- preserve aliases gobernados.

---

# Conformidad de Capability Requirement

Será conforme cuando:

- tenga ID;
- declare Capability;
- declare version constraint;
- declare Operation;
- declare Contracts;
- declare Features;
- declare contexto;
- diferencie hard y soft;
- declare objetivos;
- preserve security constraints.

---

# Conformidad de Activity-to-Capability Resolution

Será conforme cuando:

- identifique Activity;
- identifique versión;
- resuelva Capability;
- resuelva Operation;
- incorpore Workflow constraints;
- incorpore Execution context;
- incorpore Policy;
- produzca Requirement Set.

---

# Conformidad de Contract Match

Será conforme cuando:

- identifique required Contract;
- identifique offered Contract;
- evalúe schema;
- evalúe semántica;
- evalúe error behavior;
- declare Adapter cuando proceda;
- declare resultado;
- preserve fingerprints.

---

# Conformidad de Resource Match

Será conforme cuando:

- declare recursos;
- declare versiones;
- declare locality;
- declare capacidad;
- declare reservas;
- evalúe disponibilidad;
- preserve observation time.

---

# Conformidad de Candidate

Será conforme cuando:

- tenga ID;
- identifique Definition;
- identifique Instance;
- identifique Capability;
- identifique Operation;
- identifique Adapter;
- declare eligibility;
- declare score;
- declare rank;
- preserve explanation.

---

# Conformidad de Candidate Score

Será conforme cuando:

- declare dimensiones;
- utilice profile versionado;
- normalice valores;
- considere confidence;
- considere freshness;
- preserve penalties;
- declare total;
- sea reproducible.

---

# Conformidad de Degradation Decision

Será conforme cuando:

- identifique Requirement original;
- declare perfil;
- declare nivel;
- declare garantías perdidas;
- preserve restricciones no degradables;
- esté autorizada;
- sea auditable.

---

# Conformidad de Ensemble

Será conforme cuando:

- declare miembros;
- declare aggregation;
- declare diversidad;
- declare coste total;
- declare latencia estimada;
- evalúe fallos correlacionados;
- cumpla output contract.

---

# Lista de comprobación

Antes de aprobar Capability Matching deberá comprobarse:

```text
[ ] Existe Capability Taxonomy.
[ ] La Taxonomy está versionada.
[ ] Las Capabilities tienen IDs estables.
[ ] Las Capability Families están definidas.
[ ] Las Specializations están declaradas.
[ ] La substitución está gobernada.
[ ] Los aliases están versionados.
[ ] Las Capability Dependencies están declaradas.
[ ] No existen dependency cycles.
[ ] Las Composite Capabilities están definidas.
[ ] Los modos de composición están declarados.
[ ] Los Requirement Sets están tipados.
[ ] Hard y Soft Constraints están separados.
[ ] La precedencia de requisitos está definida.
[ ] Las Requests no sobrescriben seguridad.
[ ] Toda Activity resuelve Capability.
[ ] Toda Activity resuelve Operation.
[ ] Las Features están diferenciadas.
[ ] Las Features están versionadas.
[ ] Las combinaciones incompatibles se detectan.
[ ] Las Operation Semantics están completas.
[ ] Los Request Contracts se comparan.
[ ] Los Response Contracts se comparan.
[ ] Los Error Contracts se comparan.
[ ] La compatibilidad semántica se evalúa.
[ ] Los Adapters se resuelven.
[ ] Los Protocols se comparan.
[ ] Los Resource Requirements están declarados.
[ ] Las Capacity Classes están definidas.
[ ] La capacidad disponible se evalúa.
[ ] Los Scheduling Hints están diferenciados de constraints.
[ ] Las Affinities tienen strength.
[ ] Las Anti-Affinities tienen scope.
[ ] La Data Locality se evalúa.
[ ] La Region Affinity se evalúa.
[ ] La Tenant Affinity se evalúa.
[ ] Los Model Requirements se evalúan.
[ ] Los Cost Profiles están versionados.
[ ] Los Cost Profiles tienen vigencia.
[ ] Los Latency Profiles declaran percentiles.
[ ] Los Latency Profiles declaran contexto.
[ ] Los Quality Profiles declaran benchmark.
[ ] Los Quality Profiles conservan provenance.
[ ] Los Reliability Profiles declaran ventana.
[ ] Los Sustainability Profiles están separados.
[ ] Los Context Windows se validan.
[ ] Se reserva margen para output.
[ ] Los Token Limits se comprueban.
[ ] Batch Support está formalizado.
[ ] Streaming Support está formalizado.
[ ] La Data Classification se valida.
[ ] La Data Residency se valida.
[ ] Las políticas de retention se validan.
[ ] Las políticas de training usage se validan.
[ ] Los Hard Filters se aplican antes del scoring.
[ ] Solo se puntúan candidatos elegibles.
[ ] Los Selection Profiles están versionados.
[ ] Los pesos se normalizan.
[ ] Los scores consideran freshness.
[ ] Los scores consideran confidence.
[ ] Los scores tienen explicación.
[ ] El Tie-Break es estable.
[ ] Los fallbacks son diversos cuando procede.
[ ] La Capability Degradation está gobernada.
[ ] Las garantías reducidas se declaran.
[ ] Los controles no degradables se preservan.
[ ] Los Ensembles tienen límites.
[ ] Los Ensembles evalúan coste total.
[ ] Los Ensembles evalúan correlated failures.
[ ] El Matching Result declara Catalog Snapshot.
[ ] El Matching Result declara Policy Version.
[ ] El Matching Result declara observation time.
[ ] Los caches incluyen contexto completo.
[ ] Los cambios críticos invalidan cache.
[ ] Existen métricas de matching.
[ ] Existen diagnósticos estructurados.
[ ] El Quality Gate de Taxonomy ha pasado.
[ ] El Quality Gate de Requirements ha pasado.
[ ] El Quality Gate de Contract Matching ha pasado.
[ ] El Quality Gate de Resource Matching ha pasado.
[ ] El Quality Gate de Security Matching ha pasado.
[ ] El Quality Gate de Candidate Scoring ha pasado.
[ ] El Quality Gate de Degradation ha pasado.
[ ] El Quality Gate de Ensemble ha pasado.
```

---

# Arquitectura final de la Parte III

```text
Activity Definition
        ↓
Activity-to-Capability Resolution
        ↓
Capability Requirement Set
        ↓
Capability Taxonomy Resolution
        ↓
Dependency Closure
        ↓
Feature and Operation Resolution
        ↓
Contract Matching
        ↓
Adapter and Protocol Matching
        ↓
Security and Scope Filtering
        ↓
Resource and Capacity Filtering
        ↓
Affinity and Locality Evaluation
        ↓
Cost · Latency · Quality · Reliability Profiles
        ↓
Candidate Eligibility
        ↓
Candidate Scoring
        ↓
Stable Ranking
        ↓
Explanations
        ↓
Fallback or Ensemble Candidate Set
```

---

# Transición hacia la Parte IV

Esta tercera parte ha definido:

- Capability Taxonomy;
- Capability Domains;
- Capability Families;
- Generic y Specialized Capabilities;
- Capability Specialization;
- substitutability;
- aliases;
- Capability Dependencies;
- dependency closure;
- Composite Capabilities;
- composition modes;
- Capability Requirements;
- Requirement Sets;
- hard y soft constraints;
- Activity Requirements;
- Activity-to-Capability Resolution;
- Feature Model;
- Feature Dependencies;
- Operation Semantics;
- Contract Matching;
- Semantic Compatibility;
- Adapter Matching;
- Protocol Matching;
- Resource Requirements;
- Capacity Classes;
- Scheduling Hints;
- Affinity;
- Anti-Affinity;
- Data Locality;
- Region Affinity;
- Tenant Affinity;
- Model Affinity;
- Cost Profiles;
- Cost Estimates;
- Latency Profiles;
- Quality Profiles;
- Reliability Profiles;
- Sustainability Profiles;
- Context Windows;
- Token Limits;
- Batch Support;
- Streaming Support;
- Data Classification;
- Data Residency;
- Candidate Eligibility;
- Candidate Matching;
- Candidate Scoring;
- Selection Profiles;
- Score Normalization;
- Confidence y Freshness;
- Tie-Breaking;
- Candidate Explanations;
- Matching Decisions;
- Capability Degradation;
- Ensembles;
- Matching Cache;
- observabilidad;
- eventos;
- diagnósticos;
- Quality Gates;
- casos de uso;
- antipatrones;
- reglas de conformidad.

La Parte IV desarrollará:

- Engine Routing;
- Route Definitions;
- Routing Policies;
- Candidate Selection;
- Load Balancing;
- Weighted Routing;
- Priority Routing;
- Sticky Routing;
- Affinity Routing;
- Locality Routing;
- Cost-Aware Routing;
- Latency-Aware Routing;
- Quality-Aware Routing;
- Multi-Provider Routing;
- Failover;
- Fallback;
- Retry Routing;
- Hedged Requests;
- Shadow Traffic;
- Mirroring;
- Canary Routing;
- A/B Testing;
- Traffic Splitting;
- Circuit Breakers;
- Bulkheads;
- Provider Limits;
- Route Health;
- Route Reconciliation;
- Routing Decisions;
- Routing Diagnostics;
- Routing Quality Gates.

---

# Conclusión

El Capability Model avanzado permite que NovaCoquinaria seleccione Engines a partir de necesidades funcionales y no de referencias estáticas.

Su ciclo puede resumirse así:

```text
Comprender la Activity
        ↓
Resolver Capability
        ↓
Resolver Operation
        ↓
Validar Contracts
        ↓
Validar Features
        ↓
Validar seguridad
        ↓
Validar recursos
        ↓
Evaluar perfiles
        ↓
Filtrar candidatos
        ↓
Puntuar candidatos
        ↓
Explicar ranking
        ↓
Preparar fallback o ensemble
```

La Capability Taxonomy organiza lo que los Engines pueden hacer.

Las Specializations permiten resolver necesidades genéricas y específicas.

Las Dependencies identifican recursos y capacidades auxiliares.

Las Composite Capabilities permiten construir funciones complejas.

Los Requirement Sets expresan límites obligatorios y preferencias.

El Activity Resolver traduce Activities en necesidades ejecutables.

El Feature Model describe propiedades opcionales.

Las Operation Semantics definen efectos, idempotencia y control.

El Contract Matcher asegura compatibilidad de datos y errores.

El Adapter Matcher garantiza que la invocación pueda realizarse.

Los Resource Requirements validan capacidad técnica.

Affinity y Locality optimizan colocación.

Los Cost, Latency, Quality y Reliability Profiles permiten comparar candidatos.

Los Context Windows y Token Limits evitan invocaciones imposibles.

Los filtros de clasificación y residencia preservan seguridad.

La Candidate Eligibility elimina opciones incompatibles.

El Candidate Scoring ordena las opciones restantes.

Las Explanations justifican cada decisión.

Los Degradation Profiles permiten fallback sin relajar controles esenciales.

Los Ensembles permiten combinar varias implementaciones cuando aporten valor.

Un matching correctamente resuelto deberá poder responder:

```text
¿Qué Capability necesita la Activity?

¿Qué Operation debe ejecutarse?

¿Qué Contracts son obligatorios?

¿Qué Features requiere?

¿Qué dependencias existen?

¿Qué recursos necesita?

¿Qué Engines implementan la Capability?

¿Qué Instances están disponibles?

¿Qué candidatos son contractualmente compatibles?

¿Qué candidatos están autorizados?

¿Qué candidatos tienen capacidad?

¿Qué candidato cumple latencia y coste?

¿Qué calidad observable presenta?

¿Qué afinidades existen?

¿Por qué un candidato fue excluido?

¿Cómo se calculó cada score?

¿Qué perfil de selección se utilizó?

¿Qué fallback está permitido?

¿Qué garantías se perderían al degradar?

¿Debe utilizarse un Engine, varios o un ensemble?
```

Con esta tercera parte queda formalizado el mecanismo mediante el que NovaCoquinaria transforma Activities en requisitos de Capability y construye candidatos compatibles, seguros, explicables y comparables.

La siguiente parte definirá cómo esos candidatos se convierten en una ruta concreta mediante políticas de routing, balanceo, failover, circuit breakers, canary, shadow traffic y selección multi-provider.

---

# Parte IV — Engine Routing Model: Route Definitions, Routing Policies, Load Balancing, Failover, Hedging, Shadow Traffic, Canary Releases y Circuit Breakers

---

# Introducción

La Parte III ha definido cómo el Capability Matching Engine transforma una necesidad funcional en un conjunto de candidatos elegibles, compatibles y puntuados.

Sin embargo, el candidato con mayor puntuación no tiene por qué ser el Engine que finalmente ejecute una Activity.

Todavía quedan decisiones operativas:

- ¿Debe distribuirse la carga?
- ¿Debe utilizarse un proveedor preferente?
- ¿Conviene mantener afinidad con la sesión?
- ¿Debe enviarse tráfico a un Canary?
- ¿Debe duplicarse la petición mediante Hedged Requests?
- ¿Está un proveedor parcialmente degradado?
- ¿Debe activarse un Circuit Breaker?
- ¿Existe una política de Failover?
- ¿Debe hacerse Mirroring?
- ¿Se requiere Routing Multi-Región?
- ¿Debe respetarse un presupuesto diario?

Todo ello corresponde al **Routing Engine**.

Mientras que el Matching responde:

```text
¿Qué Engines podrían ejecutar esta Activity?
```

el Routing responde:

```text
¿Cuál ejecutará realmente esta Activity?
```

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir Engine Routing;
- formalizar Route Definitions;
- establecer Route Tables;
- definir Routing Policies;
- formalizar Route Constraints;
- establecer Route Priorities;
- definir Candidate Selection;
- formalizar Load Balancing;
- establecer Weighted Routing;
- definir Least Load Routing;
- formalizar Least Latency Routing;
- establecer Cost-aware Routing;
- definir Quality-aware Routing;
- formalizar Affinity Routing;
- establecer Sticky Routing;
- definir Session Routing;
- formalizar Tenant Routing;
- establecer Locality Routing;
- definir Multi-Region Routing;
- formalizar Provider Routing;
- establecer Multi-Provider Routing;
- definir Traffic Splitting;
- formalizar Canary Routing;
- establecer Shadow Traffic;
- definir Mirroring;
- formalizar Hedged Requests;
- establecer Retry Routing;
- definir Failover;
- formalizar Circuit Breakers;
- establecer Bulkheads;
- definir Rate Limiting;
- formalizar Quotas;
- establecer Admission Control;
- definir Budget-aware Routing;
- formalizar Execution Preferences;
- establecer Routing Decisions;
- definir Route Explanations;
- formalizar Route Diagnostics;
- establecer Routing Metrics;
- definir Routing Quality Gates;
- formalizar reglas de conformidad.

---

# Principios

## Matching antes que Routing

Nunca se deberá enrutar un candidato no elegible.

---

## Routing separado del Matching

El Matching descubre candidatos.

El Routing selecciona uno o varios.

---

## Routing determinista

Con mismas entradas deberá obtenerse el mismo resultado salvo política explícita.

---

## Política gobernada

Toda decisión deberá responder a una Routing Policy.

---

## Balanceo explicable

Nunca deberá existir reparto "aleatorio" no registrado.

---

## Seguridad inmutable

El Routing nunca podrá saltarse restricciones de seguridad.

---

## Routing observable

Toda decisión deberá poder reconstruirse.

---

## Failover gobernado

Nunca deberá improvisarse un proveedor alternativo.

---

## Diversidad controlada

Cuando exista redundancia deberá minimizarse el riesgo de fallo correlacionado.

---

## Routing reproducible

Toda decisión deberá conservar:

- snapshot;
- policy;
- métricas;
- candidatos;
- razones.

---

# Arquitectura conceptual

```text
Capability Matching
        │
        ▼
Ranked Candidates
        │
        ▼
Routing Policies
        │
        ▼
Constraint Evaluation
        │
        ▼
Load Balancer
        │
        ▼
Affinity Resolver
        │
        ▼
Traffic Policies
        │
        ▼
Failover Policies
        │
        ▼
Execution Route
```

---

# Engine Route

Una Route representa una posible ruta de ejecución.

Formato recomendado:

```text
ENGINE-ROUTE-XXXXXX
```

---

# Contrato

```yaml
engine_route:
  id: ENGINE-ROUTE-RETRIEVAL-EU

  version: 1.0.0

  capability:
    id: CAP-HYBRID-RETRIEVAL

  candidates:
    - ENGINE-CANDIDATE-000041
    - ENGINE-CANDIDATE-000042

  routing_policy:
    id: ROUTING-POLICY-BALANCED

  status: active
```

---

# Route States

```text
draft
active
deprecated
disabled
retired
```

---

# Route Definition

Una Route Definition especifica cómo seleccionar candidatos.

Formato recomendado:

```text
ENGINE-ROUTE-DEFINITION-XXXXXX
```

---

# Componentes

- Capability
- Candidate Filter
- Routing Policy
- Constraints
- Failover
- Retry
- Traffic Policy

---

# Route Table

Una Route Table organiza múltiples rutas.

```yaml
route_table:
  id: ROUTE-TABLE-PRODUCTION

  routes:
    - ENGINE-ROUTE-RETRIEVAL-EU
    - ENGINE-ROUTE-RAG
    - ENGINE-ROUTE-GENERATION
```

---

# Route Matching

Una Activity resolverá exactamente una Route activa.

Si varias coinciden:

- prioridad;
- specificity;
- policy.

---

# Route Priority

Mayor prioridad domina.

Ejemplo:

```text
100
```

---

# Route Constraints

Una Route puede restringirse por:

- tenant;
- región;
- clasificación;
- entorno;
- workflow;
- horario;
- presupuesto.

---

# Routing Policy

Formato recomendado:

```text
ROUTING-POLICY-XXXXXX
```

---

# Contrato

```yaml
routing_policy:
  id: ROUTING-POLICY-BALANCED

  strategy: weighted

  retry_policy:
    id: RETRY-POLICY-STANDARD

  failover_policy:
    id: FAILOVER-POLICY-EU

  load_balancer:
    strategy: least_latency
```

---

# Routing Strategies

Inicialmente:

```text
single
weighted
round_robin
least_latency
least_load
lowest_cost
highest_quality
sticky
random_seeded
priority
adaptive
```

---

# Single

Siempre selecciona el primer candidato elegible.

---

# Weighted

Distribuye según pesos.

---

# Round Robin

Reparto circular.

---

# Least Latency

Prioriza menor latencia observada.

---

# Least Load

Prioriza menor carga.

---

# Lowest Cost

Prioriza menor coste.

---

# Highest Quality

Prioriza mayor calidad.

---

# Sticky

Mantiene afinidad.

---

# Adaptive

Ajusta pesos dinámicamente.

---

# Candidate Selector

El Candidate Selector aplica la Routing Policy.

Entradas:

- candidatos;
- métricas;
- políticas;
- contexto.

Salida:

```text
Execution Candidate
```

---

# Candidate Selection Result

```yaml
candidate_selection:
  selected:
    instance: ENGINE-INSTANCE-RETRIEVAL-EU-001

  policy:
    id: ROUTING-POLICY-BALANCED

  score: 0.92
```

---

# Weighted Routing

Cada candidato posee un peso.

Ejemplo:

```text
A → 60%

B → 30%

C → 10%
```

---

# Weight Sources

- configuración;
- calidad;
- capacidad;
- política;
- coste.

---

# Dynamic Weights

Podrán modificarse automáticamente.

---

# Weight Normalization

La suma deberá ser:

```text
100%
```

---

# Adaptive Routing

Podrá reajustar pesos utilizando:

- latencia;
- errores;
- capacidad;
- disponibilidad.

---

# Hysteresis

Los cambios deberán evitar flapping.

---

# Load Balancer

Responsable del reparto de carga.

---

# Estrategias

```text
round_robin
least_connections
least_load
least_latency
weighted
adaptive
random_seeded
```

---

# Least Connections

Selecciona el Engine con menos ejecuciones activas.

---

# Least Load

Considera:

- CPU;
- memoria;
- cola;
- concurrencia.

---

# Least Latency

Utiliza latencia reciente.

---

# Random Seeded

Permite reproducibilidad.

---

# Sticky Routing

Mantiene afinidad con:

- sesión;
- tenant;
- usuario;
- workflow.

---

# Sticky Keys

Ejemplos:

```text
session_id
tenant_id
workflow_id
conversation_id
```

---

# Sticky Expiration

Podrá caducar.

---

# Affinity Routing

Podrá favorecer:

- mismo índice;
- mismo modelo;
- mismo proveedor;
- misma región.

---

# Anti-Affinity Routing

Podrá evitar:

- mismo proveedor;
- misma región;
- misma AZ.

---

# Session Routing

Mantiene continuidad.

Especialmente útil para:

- LLM stateful;
- cachés;
- streaming.

---

# Tenant Routing

Permite Engines dedicados.

---

# Region Routing

Selecciona región adecuada.

Ejemplo:

```text
eu-west
```

---

# Locality Routing

Reduce tráfico entre regiones.

---

# Provider Routing

Permite políticas entre proveedores.

Ejemplo:

```text
Internal

Azure

OpenAI

Anthropic
```

---

# Multi-Provider Routing

Distribuye entre proveedores.

Beneficios:

- resiliencia;
- coste;
- calidad.

---

# Provider Preference

Puede existir prioridad.

Ejemplo:

```text
Internal
↓
Azure
↓
OpenAI
```

---

# Traffic Splitting

Divide tráfico.

Ejemplo:

```text
90%

10%
```

---

# Uso

- pruebas;
- migraciones;
- despliegues.

---

# Split Types

```text
percentage
tenant
region
user
workflow
feature_flag
```

---

# Canary Routing

Envía una parte del tráfico a una nueva versión.

Ejemplo:

```text
95%

5%
```

---

# Canary Promotion

Podrá aumentar:

```text
5
10
25
50
100
```

---

# Canary Rollback

Automático si fallan Quality Gates.

---

# Shadow Traffic

Duplica tráfico.

Solo una respuesta llega al consumidor.

---

# Objetivos

- benchmarking;
- validación;
- migraciones.

---

# Mirroring

Similar al Shadow.

Puede almacenar resultados.

---

# Mirroring Policy

```yaml
mirroring:
  enabled: true

  percentage: 10
```

---

# Hedged Requests

Envía la misma petición a varios candidatos.

La primera respuesta válida gana.

---

# Uso

- latencia;
- colas;
- degradación.

---

# Hedge Delay

Ejemplo:

```text
100 ms
```

---

# Hedge Cancellation

Las restantes ejecuciones deberán cancelarse.

---

# Retry Routing

Tras error retryable puede cambiar de candidato.

---

# Retry Policy

Componentes:

- máximo;
- backoff;
- jitter;
- candidatos.

---

# Retry Candidate

Preferentemente distinto del anterior.

---

# Failover

Selecciona candidato alternativo.

---

# Tipos

```text
same_region

cross_region

cross_provider
```

---

# Failover Policy

```yaml
failover_policy:
  maximum_failovers: 2

  order:
    - same_region
    - cross_region
    - cross_provider
```

---

# Bulkheads

Permiten aislar recursos.

Ejemplo:

```text
LLM

Retrieval

Graph
```

Cada uno mantiene su propia capacidad.

---

# Circuit Breaker

Protege frente a fallos repetidos.

Estados:

```text
closed

open

half_open
```

---

# Open

No envía tráfico.

---

# Half Open

Prueba recuperación.

---

# Close

Servicio normal.

---

# Circuit Metrics

- failures;
- latency;
- timeout;
- success.

---

# Rate Limiting

Puede limitar:

- tenant;
- usuario;
- workflow.

---

# Quotas

Ejemplos:

```text
requests/day

tokens/day

cost/day
```

---

# Admission Control

Puede rechazar ejecución.

Razones:

- sin presupuesto;
- saturación;
- política.

---

# Budget-aware Routing

Puede evitar Engines caros cuando el presupuesto restante es reducido.

---

# Execution Preference

El consumidor puede expresar preferencias.

Nunca podrán romper Hard Constraints.

---

# Routing Decision

Formato recomendado:

```text
ENGINE-ROUTING-DECISION-XXXXXX
```

---

# Contrato

```yaml
routing_decision:
  id: ENGINE-ROUTING-DECISION-000041

  selected_candidate:
    id: ENGINE-CANDIDATE-000041

  routing_policy:
    id: ROUTING-POLICY-BALANCED

  strategy:
    weighted

  failover_enabled: true
```

---

# Route Explanation

Debe indicar:

- por qué;
- política;
- pesos;
- penalizaciones.

---

# Routing Metrics

- routing latency;
- selected provider;
- failovers;
- retries;
- hedge wins;
- circuit opens;
- traffic split.

---

# Routing Events

Inicialmente:

```text
route_selected
route_failed
failover_started
failover_completed
retry_started
retry_completed
canary_selected
shadow_started
hedge_started
hedge_completed
circuit_opened
circuit_closed
bulkhead_saturated
```

---

# Diagnósticos

Ejemplos:

```text
ENGINE_ROUTE_NOT_FOUND
ENGINE_ROUTE_DISABLED
ENGINE_ROUTING_POLICY_INVALID
ENGINE_CIRCUIT_OPEN
ENGINE_FAILOVER_EXHAUSTED
ENGINE_HEDGE_TIMEOUT
ENGINE_ROUTE_CONSTRAINT_FAILED
ENGINE_RATE_LIMIT_EXCEEDED
ENGINE_BUDGET_EXCEEDED
```

---

# Parte V — Execution Routing avanzado: Routing Pipelines, Retry Policies, Adaptive Routing, Multi-Region, QoS, SLA, Resilience Patterns, Route Governance y Auditoría

---

# Introducción

La Parte IV ha definido:

- Route Definitions;
- Routing Policies;
- Candidate Selection;
- Load Balancing;
- Weighted Routing;
- Sticky Routing;
- Traffic Splitting;
- Canary;
- Shadow Traffic;
- Hedged Requests;
- Retry;
- Failover;
- Circuit Breakers;
- Bulkheads.

Sin embargo, el Routing real de NovaCoquinaria deberá soportar escenarios mucho más complejos.

Una decisión de Routing no consistirá únicamente en seleccionar un Engine.

En muchos casos será necesario construir un Pipeline completo de ejecución:

```text
Receive Request
        ↓
Admission Control
        ↓
Policy Evaluation
        ↓
Budget Validation
        ↓
Capability Matching
        ↓
Routing Decision
        ↓
Execution
        ↓
Retries
        ↓
Fallback
        ↓
Telemetry
        ↓
Audit
```

Además:

- existirán múltiples regiones;
- múltiples proveedores;
- múltiples niveles de QoS;
- múltiples SLAs;
- ventanas de mantenimiento;
- límites presupuestarios;
- prioridades;
- degradaciones controladas.

Esta parte formaliza ese Routing avanzado.

---

# Objetivos

Esta parte persigue:

- definir Execution Routing Pipeline;
- formalizar Routing Stages;
- establecer Routing Middleware;
- definir Routing Context;
- formalizar Execution Context;
- establecer Request Classification;
- definir Priority Classes;
- formalizar QoS Profiles;
- establecer SLA Profiles;
- definir Adaptive Routing;
- formalizar Runtime Routing;
- establecer Predictive Routing;
- definir Latency Prediction;
- formalizar Congestion Avoidance;
- establecer Queue-aware Routing;
- definir Cold Start Mitigation;
- formalizar Warm Pools;
- establecer Multi-Region Execution;
- definir Region Failover;
- formalizar Active-Active;
- establecer Active-Passive;
- definir Provider Federation;
- formalizar Execution Windows;
- establecer Maintenance Routing;
- definir Draining Policies;
- formalizar Graceful Shutdown Routing;
- establecer Budget Routing;
- definir Cost Governance;
- formalizar Priority Scheduling;
- establecer Deadline-aware Routing;
- definir Execution Deadlines;
- formalizar Routing Pipelines;
- establecer Auditability;
- definir Route Replay;
- formalizar Compliance.

---

# Principios

## Routing como Pipeline

El Routing deberá entenderse como una secuencia de decisiones.

---

## Contexto inmutable

Todo el Routing compartirá un Execution Context único.

---

## Seguridad primero

Las restricciones de seguridad nunca podrán modificarse durante el Pipeline.

---

## Determinismo

La misma entrada deberá producir la misma decisión salvo adaptación explícita.

---

## Observabilidad completa

Cada etapa deberá registrar:

- entrada;
- salida;
- duración;
- decisión.

---

## Degradación controlada

Toda degradación deberá quedar registrada.

---

## QoS explícita

La calidad de servicio deberá modelarse.

---

## SLA verificable

Los SLAs deberán medirse.

---

## Gobernanza

Toda política deberá estar versionada.

---

# Arquitectura

```text
Execution Request
        │
        ▼
Admission
        ▼
Classification
        ▼
Policy
        ▼
Budget
        ▼
Capability Matching
        ▼
Routing
        ▼
Execution
        ▼
Retry
        ▼
Fallback
        ▼
Audit
```

---

# Execution Routing Pipeline

Formato:

```text
ENGINE-ROUTING-PIPELINE-XXXXXX
```

---

# Contrato

```yaml
routing_pipeline:
  id: ENGINE-ROUTING-PIPELINE-STANDARD

  stages:
    - admission
    - classification
    - policy
    - matching
    - routing
    - execution
    - resilience
    - telemetry
    - audit
```

---

# Routing Stage

Formato:

```text
ENGINE-ROUTING-STAGE-XXXXXX
```

---

# Tipos

```text
admission
classification
policy
matching
routing
execution
retry
fallback
audit
telemetry
```

---

# Admission Stage

Valida:

- autenticación;
- autorización;
- cuota;
- presupuesto;
- clasificación.

---

# Classification Stage

Clasifica:

- prioridad;
- criticidad;
- SLA;
- QoS;
- tipo de workflow.

---

# Policy Stage

Aplica:

- políticas;
- restricciones;
- overrides autorizados.

---

# Matching Stage

Ejecuta Capability Matching.

---

# Routing Stage

Selecciona candidato.

---

# Execution Stage

Invoca Adapter.

---

# Retry Stage

Gestiona reintentos.

---

# Fallback Stage

Gestiona degradaciones.

---

# Telemetry Stage

Publica métricas.

---

# Audit Stage

Genera evidencias.

---

# Routing Context

Formato:

```text
ENGINE-ROUTING-CONTEXT-XXXXXX
```

---

# Contrato

```yaml
routing_context:
  execution:
    id: EXEC-000041

  activity:
    id: ACT-RUN-RETRIEVAL

  tenant:
    id: TENANT-0001

  region:
    eu-west

  qos:
    premium
```

---

# Context Attributes

- tenant;
- región;
- budget;
- workflow;
- SLA;
- prioridad;
- usuario;
- conversación.

---

# Request Classification

Permite categorizar peticiones.

---

# Clases

```text
interactive
background
batch
critical
administrative
```

---

# Interactive

Prioriza latencia.

---

# Background

Prioriza coste.

---

# Batch

Optimiza throughput.

---

# Critical

Prioriza resiliencia.

---

# Priority Classes

```text
P0
P1
P2
P3
```

---

# QoS Profile

Formato:

```text
QOS-PROFILE-XXXXXX
```

---

# Contrato

```yaml
qos_profile:
  id: PREMIUM

  objectives:
    latency:
      p95: 250

    availability:
      minimum: 0.999

    retries:
      enabled: true
```

---

# QoS Dimensions

- latencia;
- disponibilidad;
- throughput;
- prioridad.

---

# SLA Profile

Formato:

```text
SLA-PROFILE-XXXXXX
```

---

# Ejemplo

```yaml
sla_profile:
  id: SLA-GOLD

  guarantees:
    availability: 99.95
    latency_p95: 300
```

---

# SLA Violation

Generará:

- evento;
- métrica;
- auditoría.

---

# Adaptive Routing

Puede modificar decisiones utilizando:

- carga;
- latencia;
- errores;
- presupuesto.

---

# Predictive Routing

Podrá utilizar modelos predictivos.

---

# Prediction Sources

- histórico;
- tendencias;
- telemetría;
- estacionalidad.

---

# Congestion Avoidance

Evita rutas congestionadas.

---

# Queue-aware Routing

Considera:

- cola;
- backlog;
- tiempo estimado.

---

# Cold Start Mitigation

Evita instancias frías.

---

# Warm Pool

Mantiene Engines preparados.

---

# Warm Pool Policy

```yaml
warm_pool:
  minimum_instances: 2
```

---

# Multi-Region Routing

Puede seleccionar:

- misma región;
- región cercana;
- región secundaria.

---

# Active-Active

Todas las regiones sirven tráfico.

---

# Active-Passive

Solo una región activa.

---

# Region Failover

Cambio automático entre regiones.

---

# Provider Federation

Coordina múltiples proveedores.

---

# Federation Policies

- prioridad;
- coste;
- resiliencia.

---

# Maintenance Window

Una región puede entrar en mantenimiento.

---

# Maintenance Routing

Redirige tráfico.

---

# Draining

No acepta nuevas peticiones.

Permite finalizar las existentes.

---

# Graceful Shutdown

Evita cancelaciones innecesarias.

---

# Cost Governance

Permite limitar gasto.

---

# Budget Profile

```yaml
budget_profile:
  daily_limit:
    EUR: 250
```

---

# Budget Routing

Puede cambiar a Engines más económicos.

---

# Deadline-aware Routing

Prioriza cumplir un deadline.

---

# Deadline Contract

```yaml
deadline:
  maximum_duration: PT2S
```

---

# Deadline Miss

Genera diagnóstico.

---

# Execution Windows

Algunas Activities solo podrán ejecutarse en determinados horarios.

---

# Scheduling Window

```yaml
window:
  from: "08:00"
  to: "22:00"
```

---

# Runtime Adaptation

Puede modificar:

- pesos;
- candidatos;
- región.

Siempre dentro de Policy.

---

# Route Replay

Permite reconstruir decisiones históricas.

---

# Replay Inputs

- snapshot;
- policy;
- métricas.

---

# Replay Output

Debe coincidir con la decisión original.

---

# Auditoría

Toda decisión deberá registrar:

- candidatos;
- descartes;
- métricas;
- política;
- tiempos.

---

# Métricas

Inicialmente:

- pipeline duration;
- routing duration;
- retries;
- failovers;
- SLA violations;
- QoS compliance;
- replay success.

---

# Eventos

```text
routing_pipeline_started
routing_pipeline_completed
routing_stage_started
routing_stage_completed
qos_profile_applied
sla_profile_applied
maintenance_routing
budget_limit_reached
deadline_missed
region_failover
provider_switched
warm_pool_used
```

---

# Diagnósticos

```text
ENGINE_QOS_NOT_SATISFIED
ENGINE_SLA_VIOLATED
ENGINE_DEADLINE_MISSED
ENGINE_BUDGET_LIMIT_REACHED
ENGINE_MAINTENANCE_ACTIVE
ENGINE_REGION_UNAVAILABLE
ENGINE_PROVIDER_FEDERATION_ERROR
ENGINE_REPLAY_FAILED
```

---

# Quality Gate del Routing Pipeline

```yaml
quality_gate:
  id: QG-ENGINE-ROUTING-PIPELINE-0001

  criteria:
    all:
      - pipeline_complete == true
      - routing_context_present == true
      - qos_profile_applied == true
      - sla_profile_applied == true
      - audit_generated == true
      - telemetry_published == true
```

---

# Casos de uso

## Caso 1

Una petición interactiva Premium obtiene:

- región local;
- warm instance;
- menor latencia.

---

## Caso 2

Un Batch nocturno utiliza el proveedor más barato.

---

## Caso 3

Una región entra en mantenimiento.

El Routing drena tráfico y conmuta automáticamente.

---

## Caso 4

El presupuesto diario alcanza el 95 %.

El Routing cambia a Engines low-cost.

---

## Caso 5

Una petición crítica activa Hedged Requests y Failover regional.

---

# Antipatrones

No deberán permitirse:

- Routing sin contexto;
- QoS implícito;
- SLA no medible;
- Budget ignorado;
- Cold Starts innecesarios;
- Replay imposible;
- Auditoría incompleta;
- Políticas no versionadas;
- Adaptación sin límites.

---

# Reglas mínimas

Toda implementación deberá:

- soportar Routing Pipeline;
- versionar QoS;
- versionar SLA;
- registrar auditoría;
- soportar Replay;
- publicar telemetría;
- respetar presupuesto;
- soportar Multi-Region;
- soportar Maintenance Routing;
- preservar reproducibilidad.

---

# Transición hacia la Parte VI

La siguiente parte desarrollará el plano operativo del Engine Registry:

- sincronización distribuida;
- replicación;
- snapshots;
- consenso;
- cachés;
- índices;
- eventos;
- consistencia;
- escalabilidad horizontal;
- recuperación ante desastre;
- gobierno operacional.

---

# Parte VI — Arquitectura Distribuida del Engine Registry: Replicación, Consistencia, Snapshots, Sincronización, Cachés, Índices, Recuperación ante Desastres y Gobierno Operacional

---

# Introducción

Hasta este punto la especificación ha definido:

- el modelo de Engines;
- Registry;
- Discovery;
- Capability Matching;
- Routing;
- Execution Routing.

Sin embargo, aún no se ha descrito **cómo existe físicamente el Engine Registry**.

En producción, el Registry no será una única base de datos.

Será un sistema distribuido compuesto por múltiples nodos que deberán mantener una visión coherente del ecosistema completo de Engines.

Dicho sistema deberá soportar:

- alta disponibilidad;
- múltiples regiones;
- replicación;
- snapshots;
- sincronización;
- consistencia;
- recuperación;
- auditoría;
- escalabilidad horizontal.

Esta parte formaliza ese plano operacional.

---

# Objetivos

Esta parte persigue:

- definir Registry Cluster;
- formalizar Registry Nodes;
- establecer Topologías;
- definir Replication Model;
- formalizar Consistency Model;
- establecer Snapshot Model;
- definir Registry Cache;
- formalizar Distributed Cache;
- establecer Registry Indexes;
- definir Search Index;
- formalizar Registry Journal;
- establecer Event Log;
- definir Replication Events;
- formalizar Synchronization;
- establecer Leader Election;
- definir Read Models;
- formalizar Write Models;
- establecer Version Vectors;
- definir Conflict Resolution;
- formalizar Disaster Recovery;
- establecer Backup Policies;
- definir Restore Procedures;
- formalizar Registry Bootstrap;
- establecer Registry Migration;
- definir Operational Governance;
- formalizar Registry Metrics;
- establecer Registry Health;
- definir Operational Quality Gates.

---

# Principios

## Registry distribuido

El Registry deberá poder ejecutarse sobre múltiples nodos.

---

## Sin punto único de fallo

No deberá existir un único nodo imprescindible.

---

## Consistencia gobernada

Toda inconsistencia deberá ser observable.

---

## Replicación verificable

Cada cambio deberá poder seguirse.

---

## Snapshots reproducibles

Todo snapshot deberá reconstruir exactamente el estado.

---

## Journaling permanente

Toda modificación deberá quedar registrada.

---

## Separación lectura/escritura

El plano de lectura podrá diferir del plano de escritura.

---

## Observabilidad completa

Toda operación deberá generar evidencias.

---

# Arquitectura conceptual

```text
             Registry Cluster
                    │
 ┌──────────────────┼──────────────────┐
 │                  │                  │
 ▼                  ▼                  ▼
Node A           Node B            Node C
 │                  │                  │
 ├────Replication────┼────Replication──┤
 │                  │                  │
 ▼                  ▼                  ▼
 Distributed Journal / Snapshots / Indexes
```

---

# Registry Cluster

Formato recomendado:

```text
ENGINE-REGISTRY-CLUSTER-XXXXXX
```

---

# Contrato

```yaml
registry_cluster:
  id: ENGINE-REGISTRY-CLUSTER-PRODUCTION

  version: 1.0.0

  regions:
    - eu-west
    - eu-central

  replication:
    mode: active-active
```

---

# Registry Node

Formato:

```text
ENGINE-REGISTRY-NODE-XXXXXX
```

---

# Estados

```text
starting
joining
active
syncing
draining
maintenance
offline
retired
```

---

# Contrato

```yaml
registry_node:
  id: ENGINE-REGISTRY-NODE-EUWEST-01

  region: eu-west

  role:
    leader: false
    writable: true
    readable: true

  status: active
```

---

# Roles

Los nodos podrán actuar como:

- writer;
- reader;
- leader;
- follower;
- observer.

---

# Cluster Topologies

Inicialmente:

```text
single-region
multi-region
active-active
active-passive
hub-spoke
mesh
```

---

# Replication Model

Formato recomendado:

```text
ENGINE-REPLICATION-MODEL-XXXXXX
```

---

# Tipos

```text
synchronous
asynchronous
quorum
eventual
```

---

# Replicación síncrona

Mayor consistencia.

Mayor latencia.

---

# Replicación asíncrona

Mayor disponibilidad.

Consistencia eventual.

---

# Quorum

Permite confirmar cambios mediante mayoría.

---

# Eventual Consistency

Los nodos convergerán con el tiempo.

---

# Consistency Model

Formato:

```text
ENGINE-CONSISTENCY-MODEL-XXXXXX
```

---

# Niveles

```text
strong
bounded
session
eventual
```

---

# Strong

Toda lectura observa el último estado confirmado.

---

# Session Consistency

Una sesión observa sus propias escrituras.

---

# Bounded Staleness

Se admite retraso limitado.

---

# Eventual

No existe garantía inmediata.

---

# Registry Journal

Todo cambio deberá registrarse.

---

# Journal Entry

```yaml
journal_entry:
  sequence: 84321

  event:
    type: engine_registered

  timestamp:
    2026-08-03T12:31:22Z
```

---

# Journal Properties

- append-only;
- immutable;
- ordered;
- auditable.

---

# Event Log

Los eventos constituirán el origen de verdad histórico.

---

# Snapshot

Formato:

```text
ENGINE-REGISTRY-SNAPSHOT-XXXXXX
```

---

# Contrato

```yaml
snapshot:
  id: ENGINE-REGISTRY-SNAPSHOT-20260803-0001

  sequence: 84321

  timestamp:
    2026-08-03T12:35:00Z
```

---

# Snapshot Contents

Incluye:

- Definitions;
- Instances;
- Policies;
- Capabilities;
- Contracts;
- Health;
- Routing Tables.

---

# Snapshot Frequency

Podrá configurarse por:

- tiempo;
- eventos;
- tamaño.

---

# Incremental Snapshot

Solo almacena diferencias.

---

# Full Snapshot

Representa el estado completo.

---

# Snapshot Validation

Todo snapshot deberá poder validarse.

---

# Snapshot Hash

Cada snapshot deberá disponer de fingerprint.

---

# Registry Cache

Permite acelerar lecturas.

---

# Cache Levels

```text
local
distributed
persistent
```

---

# Local Cache

Cada nodo mantiene copia parcial.

---

# Distributed Cache

Compartida por el Cluster.

---

# Persistent Cache

Permite recuperación rápida.

---

# Cache Keys

Ejemplos:

```text
engine_definition
engine_instance
capability
route
policy
```

---

# Cache Invalidation

Se producirá cuando cambien:

- leases;
- heartbeats;
- policies;
- definitions.

---

# Cache Freshness

Toda entrada tendrá TTL.

---

# Search Index

Optimiza Discovery.

---

# Índices

```text
engine_id
capability
region
provider
status
health
tags
contracts
```

---

# Composite Indexes

Ejemplo:

```text
Capability
+
Region
+
Health
```

---

# Reverse Indexes

Permiten responder:

```text
¿Qué Engines implementan esta Capability?
```

---

# Synchronization

Mantiene convergencia.

---

# Sync Cycle

```text
Detect
↓

Compare
↓

Transfer
↓

Apply
↓

Verify
```

---

# Synchronization Policies

```text
continuous
periodic
manual
```

---

# Leader Election

Cuando exista liderazgo deberá definirse.

---

# Election Strategies

```text
raft
bully
external
manual
```

---

# Leader Responsibilities

- coordinación;
- snapshots;
- journal;
- governance.

---

# Follower Responsibilities

- replicación;
- consultas;
- recuperación.

---

# Observer Node

Solo lectura.

---

# Write Model

Las escrituras seguirán un flujo gobernado.

---

# Flujo

```text
Validate

↓

Journal

↓

Replicate

↓

Commit

↓

Publish
```

---

# Read Model

Las lecturas podrán utilizar:

- snapshot;
- cache;
- índice;
- journal.

---

# CQRS

Se recomienda separar:

- escritura;
- lectura.

---

# Version Vectors

Permiten detectar divergencias.

---

# Conflict Detection

Podrá detectar:

- escritura concurrente;
- pérdida de réplica;
- reorder.

---

# Conflict Resolution

Inicialmente:

```text
last_writer
manual
merge
vector_clock
policy
```

---

# Registry Bootstrap

Inicializa un nodo nuevo.

---

# Bootstrap Sources

- snapshot;
- backup;
- peer;
- empty.

---

# Disaster Recovery

Formato:

```text
ENGINE-DISASTER-RECOVERY-XXXXXX
```

---

# Recovery Objectives

```text
RPO

RTO
```

---

# Backup Policy

Incluye:

- frecuencia;
- retención;
- cifrado;
- validación.

---

# Restore

Todo backup deberá poder restaurarse.

---

# Restore Validation

Se comprobará:

- integridad;
- hashes;
- journal.

---

# Registry Migration

Permite evolucionar esquemas.

---

# Migration Steps

```text
Prepare

↓

Replicate

↓

Validate

↓

Switch

↓

Verify
```

---

# Governance

Toda modificación del Registry deberá estar gobernada.

---

# Governance Objects

- Definitions;
- Policies;
- Contracts;
- Routes;
- Capabilities.

---

# Governance Workflow

```text
Draft

↓

Review

↓

Approve

↓

Publish
```

---

# Metrics

Inicialmente:

- replication lag;
- cache hit;
- cache miss;
- snapshot duration;
- sync duration;
- journal growth;
- node count;
- conflicts;
- restores;
- bootstrap duration.

---

# Health

El Cluster deberá publicar:

- overall health;
- node health;
- replication health;
- snapshot health;
- cache health.

---

# Eventos

```text
registry_node_joined
registry_node_left
snapshot_created
snapshot_restored
replication_started
replication_completed
cache_invalidated
leader_elected
conflict_detected
conflict_resolved
bootstrap_completed
backup_created
restore_completed
```

---

# Diagnósticos

```text
ENGINE_CLUSTER_UNAVAILABLE
ENGINE_NODE_UNHEALTHY
ENGINE_REPLICATION_FAILED
ENGINE_REPLICATION_LAG
ENGINE_SNAPSHOT_INVALID
ENGINE_CACHE_CORRUPTED
ENGINE_CACHE_STALE
ENGINE_CONFLICT_DETECTED
ENGINE_CONFLICT_UNRESOLVED
ENGINE_BACKUP_FAILED
ENGINE_RESTORE_FAILED
ENGINE_BOOTSTRAP_FAILED
```

---

# Quality Gate del Cluster

```yaml
quality_gate:
  id: QG-ENGINE-REGISTRY-CLUSTER-0001

  criteria:
    all:
      - replication_healthy == true
      - snapshots_valid == true
      - journal_consistent == true
      - cache_consistent == true
      - indexes_valid == true
      - no_unresolved_conflicts == true
```

---

# Casos de uso

## Caso 1

Un nodo nuevo entra en producción.

Obtiene el último Snapshot y reproduce el Journal restante.

---

## Caso 2

Se pierde una región completa.

El Cluster conmuta automáticamente.

---

## Caso 3

Un Snapshot resulta corrupto.

Se restaura el anterior y se reproduce el Journal.

---

## Caso 4

Dos nodos escriben simultáneamente.

El Conflict Resolver aplica Version Vectors.

---

## Caso 5

Se reconstruye completamente el Registry utilizando únicamente Backups y Journal.

---

# Antipatrones

No deberán permitirse:

- Registry sin Journal;
- Snapshots no verificables;
- Cache sin TTL;
- Replicación silenciosa;
- Conflictos ocultos;
- Backups no restaurables;
- Leader permanente;
- Escrituras fuera del Journal.

---

# Reglas mínimas

Toda implementación deberá:

- soportar Cluster;
- soportar Replication;
- mantener Journal;
- generar Snapshots;
- validar Hashes;
- soportar Bootstrap;
- soportar Restore;
- detectar Conflicts;
- publicar métricas;
- conservar auditoría.

---

# Transición hacia la Parte VII

La siguiente parte desarrollará:

- seguridad del Engine Registry;
- identidad;
- autenticación;
- autorización;
- Zero Trust;
- RBAC/ABAC;
- Secrets;
- firmas;
- certificados;
- auditoría de seguridad;
- cumplimiento normativo;
- gobierno criptográfico.

---

# Parte VII — Seguridad, Identidad, Zero Trust, RBAC/ABAC, Secretos, Firmas, Certificados, Auditoría y Gobierno Criptográfico del Engine Registry

---

# Introducción

La Parte VI ha definido la arquitectura distribuida del Engine Registry mediante:

- Registry Cluster;
- Registry Nodes;
- replicación;
- consistencia;
- snapshots;
- Journal;
- sincronización;
- caches;
- índices;
- bootstrap;
- backups;
- restore;
- Disaster Recovery;
- gobernanza operacional.

Sin embargo, un Registry distribuido no puede considerarse confiable únicamente porque sus nodos repliquen correctamente la información.

El Engine Registry mantiene datos que determinan:

- qué Engines existen;
- qué capacidades pueden ejecutarse;
- qué endpoints se consideran válidos;
- qué proveedores están autorizados;
- qué contratos son compatibles;
- qué Engines pueden procesar datos internos;
- qué rutas puede utilizar el Orquestador;
- qué instancias deben bloquearse;
- qué niveles de confianza se aplican.

Una modificación maliciosa o no autorizada en el Registry podría provocar:

- ejecución en un Engine falso;
- exfiltración de datos;
- downgrade de seguridad;
- enrutamiento hacia un proveedor no aprobado;
- uso de versiones vulnerables;
- exposición cross-tenant;
- activación de endpoints comprometidos;
- omisión de Quality Gates;
- supresión de Quarantine;
- alteración de Contracts;
- desactivación de controles de residencia;
- elevación indebida de Trust Level.

Por ello, el Engine Registry deberá considerarse un componente de alta confianza dentro de NovaCoquinaria.

Conceptualmente:

```text
Identity
   ↓
Authentication
   ↓
Authorization
   ↓
Policy Enforcement
   ↓
Validated Registry Operation
   ↓
Integrity Protection
   ↓
Audit and Detection
   ↓
Cryptographic Evidence
```

La seguridad no deberá añadirse únicamente en las APIs externas.

Deberá aplicarse de extremo a extremo sobre:

- manifests;
- Definitions;
- Instances;
- Providers;
- Capabilities;
- Contracts;
- Routes;
- Policies;
- Registry Nodes;
- caches;
- snapshots;
- Journal;
- backups;
- eventos;
- operaciones administrativas.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir el modelo de seguridad del Engine Registry;
- formalizar Registry Principals;
- establecer Workload Identities;
- definir User Identities;
- formalizar Service Identities;
- establecer Provider Identities;
- definir Registry Node Identities;
- formalizar Zero Trust;
- establecer autenticación;
- definir autorización;
- formalizar RBAC;
- establecer ABAC;
- definir Policy Enforcement;
- formalizar Resource Scopes;
- establecer Tenant Isolation;
- definir Environment Isolation;
- formalizar Region Isolation;
- establecer Data Classification Enforcement;
- definir Trust Level Enforcement;
- formalizar Provider Trust;
- establecer Registration Authorization;
- definir Discovery Authorization;
- formalizar Routing Authorization;
- establecer Administrative Authorization;
- definir Break-Glass Access;
- formalizar Approval Workflows;
- establecer Separation of Duties;
- definir Least Privilege;
- formalizar Secret References;
- establecer Secret Rotation;
- definir Credential Profiles;
- formalizar mTLS;
- establecer certificados;
- definir Certificate Lifecycle;
- formalizar firmas de manifests;
- establecer firma de snapshots;
- definir firma de eventos;
- formalizar fingerprints;
- establecer Supply Chain Security;
- definir Artifact Attestations;
- formalizar Software Bill of Materials;
- establecer Vulnerability Policies;
- definir Key Management;
- formalizar Key Rotation;
- establecer Cryptographic Profiles;
- definir Audit Trails;
- formalizar Security Events;
- establecer Threat Detection;
- definir Security Quarantine;
- formalizar Incident Response;
- establecer compliance;
- definir retention de auditoría;
- formalizar Security Quality Gates;
- establecer reglas de conformidad.

---

# Principios de seguridad

Toda implementación deberá respetar los siguientes principios.

---

## Zero Trust

Ningún actor será confiable únicamente por:

- red;
- ubicación;
- namespace;
- región;
- proceso;
- pertenencia al cluster.

Toda operación deberá autenticarse y autorizarse.

---

## Identidad antes que red

La autorización deberá basarse en identidad verificada.

---

## Least Privilege

Cada principal deberá poseer únicamente los permisos necesarios.

---

## Deny by Default

Toda acción no autorizada explícitamente deberá rechazarse.

---

## Separation of Duties

Las operaciones críticas deberán separar:

- solicitud;
- revisión;
- aprobación;
- ejecución.

---

## No Auto-Elevation

Un Engine no deberá elevar por sí mismo:

- Trust Level;
- Scope;
- Classification;
- Lifecycle;
- Provider Status.

---

## Definitions inmutables

Una versión publicada no deberá modificarse.

---

## Integridad verificable

Manifests, Contracts, Snapshots y Events críticos deberán poder verificarse criptográficamente.

---

## Secretos fuera del Registry

El Registry conservará referencias, nunca secretos en claro.

---

## Tenant Isolation

Una operación de un tenant no deberá afectar a otro salvo permisos administrativos explícitos.

---

## Environment Isolation

Desarrollo, staging y producción deberán mantener controles separados.

---

## Trust contextual

Un Provider aprobado para datos públicos no deberá considerarse aprobado para datos internos.

---

## Registro autenticado

Toda Definition e Instance deberá proceder de una identidad validada.

---

## Security Metadata autoritativa

Los campos de seguridad no deberán confiar en self-report no verificado.

---

## Endpoints gobernados

Una Instance no deberá poder anunciar endpoints arbitrarios.

---

## No Downgrade Silencioso

Toda reducción de seguridad deberá bloquearse o requerir aprobación.

---

## Auditoría inmutable

Las acciones sensibles deberán conservarse de forma append-only.

---

## Break-Glass restringido

El acceso de emergencia deberá:

- ser temporal;
- justificarse;
- auditarse;
- revisarse.

---

## Rotación obligatoria

Credenciales y claves deberán rotarse.

---

## Supply Chain verificada

La Definition deberá poder vincularse con:

- build;
- Artifact;
- SBOM;
- firma;
- attestation;
- deployment.

---

## Fail Closed

Cuando no pueda comprobarse un control crítico, deberá rechazarse la operación.

---

## Caches no autoritativas para seguridad

Un estado de autorización stale no deberá permitir acciones críticas.

---

## Revocación rápida

Los cambios de:

- trust;
- quarantine;
- credential revocation;
- provider suspension;

deberán propagarse inmediatamente.

---

# Arquitectura conceptual

```text
┌───────────────────────────────────────────────┐
│                 Registry Client               │
│                                               │
│ User · Service · Engine · Provider · Node     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Identity Gateway                │
│                                               │
│ Authenticate · Attest · Verify Credentials    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Authorization Layer              │
│                                               │
│ RBAC · ABAC · Tenant · Scope · Environment    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Policy Enforcement               │
│                                               │
│ Trust · Classification · Residency · Risk     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            Registry Security Controls         │
│                                               │
│ Signatures · mTLS · Secrets · Fencing         │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Audit and Detection              │
│                                               │
│ Events · Alerts · Evidence · Incident         │
└───────────────────────────────────────────────┘
```

---

# Registry Principal

Un **Registry Principal** representa una identidad autenticada que interactúa con el Registry.

Formato recomendado:

```text
ENGINE-PRINCIPAL-XXXXXX
```

---

# Principal Types

```text
user
service
workload
engine_instance
engine_provider
registry_node
deployment_controller
scheduler
orchestrator
security_service
automation
external_registry
```

---

# Principal Contract

```yaml
registry_principal:
  id: ENGINE-PRINCIPAL-WORKLOAD-RETRIEVAL-001

  type: workload

  identity:
    provider: WORKLOAD-IDENTITY-PLATFORM
    subject: workload://production/retrieval/001

  tenant_scope:
    - TENANT-0001

  environment_scope:
    - production

  status: active
```

---

# Principal Status

```text
active
restricted
suspended
revoked
expired
unknown
```

---

# User Identity

Representa una persona autenticada.

---

# Requisitos

- identidad corporativa;
- MFA para operaciones críticas;
- roles;
- atributos;
- tenant;
- session;
- expiry.

---

# Service Identity

Representa un servicio interno.

---

# Workload Identity

Representa una carga concreta.

Ejemplos:

- pod;
- deployment;
- job;
- process;
- serverless function.

---

# Engine Instance Identity

Una Engine Instance deberá disponer de identidad propia.

No deberá compartir indiscriminadamente credenciales con todas las instancias de una Definition.

---

# Provider Identity

Un proveedor externo deberá autenticarse mediante:

- certificado;
- OAuth client;
- signed metadata;
- federation;
- provider-specific trust relationship.

---

# Registry Node Identity

Cada Registry Node deberá autenticarse frente al cluster.

---

# Node Identity Contract

```yaml
registry_node_identity:
  node:
    id: ENGINE-REGISTRY-NODE-EUWEST-01

  certificate:
    subject: registry-node-euwest-01
    issuer: NOVACOQUINARIA-INTERNAL-CA
    serial: ...

  cluster:
    id: ENGINE-REGISTRY-CLUSTER-PRODUCTION

  roles:
    - reader
    - writer
```

---

# Identity Proof

Podrá basarse en:

```text
certificate
signed_token
workload_attestation
federated_identity
hardware_attestation
provider_signature
```

---

# Identity Federation

El Registry podrá confiar en varios Identity Providers.

---

# Federation Contract

Formato recomendado:

```text
ENGINE-IDENTITY-FEDERATION-XXXXXX
```

---

# Contrato

```yaml
identity_federation:
  id: ENGINE-IDENTITY-FEDERATION-EXTERNAL-001

  issuer: https://identity.provider.example

  subject_types:
    - engine_provider

  audiences:
    - engine-registry

  trust:
    status: approved

  constraints:
    environment:
      - staging
      - production
```

---

# Authentication

Toda operación deberá autenticar al principal.

---

# Authentication Methods

```text
mTLS
OAuth2
OIDC
JWT
signed_request
API key
workload identity
federated identity
```

---

# Recomendación

Para comunicación interna:

```text
mTLS
+
workload identity
```

Para usuarios:

```text
OIDC
+
MFA
```

Para proveedores:

```text
OAuth2 client credentials
+
mTLS
```

cuando sea viable.

---

# Authentication Profile

Formato recomendado:

```text
ENGINE-AUTHN-PROFILE-XXXXXX
```

---

# Contrato

```yaml
authentication_profile:
  id: ENGINE-AUTHN-PROFILE-INTERNAL-WORKLOAD

  methods:
    all:
      - mtls
      - workload_identity

  token:
    maximum_age: PT10M

  certificate:
    required: true

  replay_protection: true
```

---

# Authentication Context

```yaml
authentication_context:
  principal:
    id: ENGINE-PRINCIPAL-WORKLOAD-RETRIEVAL-001

  method:
    - mtls
    - workload_identity

  assurance_level: high

  authenticated_at: 2026-08-02T20:00:00Z
  expires_at: 2026-08-02T20:10:00Z
```

---

# Authentication Assurance Levels

```text
low
medium
high
hardware_backed
```

---

# Reauthentication

Las operaciones críticas podrán requerir autenticación reciente.

---

# Replay Protection

Las solicitudes sensibles deberán incluir:

- nonce;
- timestamp;
- request ID;
- signature;
- idempotency key.

---

# Authentication Failure

Código:

```text
ENGINE_AUTHENTICATION_FAILED
```

---

# Authorization

La autorización decidirá si un principal puede realizar una acción sobre un recurso.

---

# Authorization Decision

Formato recomendado:

```text
ENGINE-AUTHZ-DECISION-XXXXXX
```

---

# Contrato

```yaml
authorization_decision:
  id: ENGINE-AUTHZ-DECISION-000041

  principal:
    id: ENGINE-PRINCIPAL-WORKLOAD-RETRIEVAL-001

  action: engine_instance.heartbeat

  resource:
    type: engine_instance
    id: ENGINE-INSTANCE-RETRIEVAL-EU-001

  context:
    environment: production
    region: eu-west

  decision: permit

  policy:
    id: ENGINE-AUTHZ-POLICY-INSTANCE-HEARTBEAT
    version: 1.0.0
```

---

# Authorization Outcomes

```text
permit
deny
conditional
not_applicable
indeterminate
```

---

# Indeterminate

Para operaciones críticas deberá tratarse como:

```text
deny
```

---

# RBAC

El **Role-Based Access Control** asigna permisos mediante roles.

---

# Roles iniciales

```text
registry_reader
registry_operator
engine_owner
engine_provider
workflow_designer
platform_admin
security_admin
auditor
deployment_controller
registry_node
emergency_operator
```

---

# Registry Reader

Puede:

- consultar Definitions;
- consultar Capabilities;
- consultar estado autorizado;
- ejecutar Discovery.

---

# Registry Operator

Puede:

- gestionar Instances;
- iniciar draining;
- ejecutar reconciliation segura;
- revisar health.

---

# Engine Owner

Puede:

- proponer versiones;
- modificar drafts;
- iniciar deprecation;
- gestionar documentación.

No deberá elevar trust por sí solo.

---

# Engine Provider

Puede:

- publicar manifests permitidos;
- sincronizar metadata;
- registrar Instances autorizadas.

---

# Platform Admin

Puede:

- gestionar lifecycle;
- aprobar producción;
- modificar Routes;
- ejecutar operaciones administrativas.

---

# Security Admin

Puede:

- cambiar trust;
- aplicar block;
- aplicar quarantine;
- revocar credenciales;
- aprobar external providers.

---

# Auditor

Solo lectura sobre:

- History;
- Audit;
- Decisions;
- Evidence.

---

# Emergency Operator

Dispone de acciones temporales de emergencia.

---

# RBAC Role Contract

```yaml
registry_role:
  id: ROLE-ENGINE-OWNER

  permissions:
    - engine_definition.create_draft
    - engine_definition.submit
    - engine_definition.deprecate_request
    - engine_metadata.update_non_security

  constraints:
    production_activation: false
    trust_change: false
```

---

# ABAC

El **Attribute-Based Access Control** permite decisiones contextuales.

---

# Attributes

```text
principal.role
principal.tenant
principal.environment
principal.provider
resource.owner
resource.tenant
resource.environment
resource.classification
resource.lifecycle
action
time
region
risk
authentication_assurance
```

---

# ABAC Policy Example

```yaml
authorization_policy:
  id: ENGINE-AUTHZ-POLICY-INSTANCE-HEARTBEAT

  effect: permit

  when:
    all:
      - principal.type == workload
      - principal.id == resource.registered_identity
      - principal.environment == resource.environment
      - action == engine_instance.heartbeat
      - resource.lifecycle != quarantined
```

---

# RBAC + ABAC

Modelo recomendado:

```text
RBAC grants broad permission
+
ABAC constrains context
```

---

# Resource Scope

Toda autorización deberá declarar alcance.

---

# Scopes

```text
global
provider
tenant
environment
region
engine_type
engine_definition
engine_instance
capability
operation
route
contract
```

---

# Scope Contract

```yaml
authorization_scope:
  tenants:
    - TENANT-0001

  environments:
    - staging

  engine_definitions:
    - ENGINE-DEF-RETRIEVAL-HYBRID

  actions:
    - read
    - register_instance
```

---

# No Wildcard Global Implícito

El acceso global deberá ser explícito.

---

# Tenant Isolation

El Registry deberá separar datos y operaciones por tenant cuando corresponda.

---

# Tenant-Aware Resources

- dedicated Instances;
- tenant Routes;
- quotas;
- provider permissions;
- usage profiles;
- security metadata;
- custom Engines.

---

# Tenant Context

Toda request tenant-aware deberá incluir:

```yaml
tenant_context:
  tenant_id: TENANT-0001
```

---

# Cross-Tenant Access

Deberá requerir:

- rol autorizado;
- motivo;
- scope;
- auditoría;
- minimización de datos.

---

# Tenant Isolation Modes

```text
logical
namespace
database
cluster
dedicated_instance
```

---

# Environment Isolation

Desarrollo, staging y producción deberán separarse.

---

# Reglas

- credenciales diferentes;
- certificados diferentes;
- policies diferentes;
- Trust Levels diferentes;
- approvals independientes;
- no promotion implícita;
- no endpoint crossover.

---

# Production Boundary

Un Engine de desarrollo no deberá registrarse en producción por reutilizar el mismo ID.

---

# Environment Promotion

Deberá crear un registro o aprobación específica para producción.

---

# Region Isolation

Las regiones podrán tener:

- CAs;
- keys;
- policies;
- Providers;
- endpoints;
- data scopes;

diferenciados.

---

# Trust Level Enforcement

El Trust Level deberá utilizarse como control obligatorio.

---

# Trust Decision

```yaml
engine_trust_decision:
  engine_definition:
    id: ENGINE-DEF-RAG-EXTERNAL
    version: 1.0.0

  level: restricted_external

  constraints:
    maximum_classification: public
    production_allowed: true
    personal_data_allowed: false
    training_usage_allowed: false
```

---

# Trust Changes

Cambios de trust deberán requerir:

- security review;
- evidence;
- approval;
- audit;
- versioned decision.

---

# Trust Downgrade

Deberá propagarse inmediatamente.

---

# Provider Trust

El Provider deberá tener su propio perfil.

---

# Provider Trust Profile

Formato recomendado:

```text
ENGINE-PROVIDER-TRUST-PROFILE-XXXXXX
```

---

# Contrato

```yaml
provider_trust_profile:
  id: ENGINE-PROVIDER-TRUST-EXTERNAL-001

  provider:
    id: ENGINE-PROVIDER-EXTERNAL-001

  status: approved_external

  allowed:
    classifications:
      - public

    regions:
      - eu-west

    operations:
      - generation

  restrictions:
    personal_data: false
    request_retention: false
    model_training: false
```

---

# Provider Suspension

Deberá bloquear:

- nuevas registrations;
- nuevas selections;
- Route usage;
- lease renewals cuando proceda.

---

# Data Classification Enforcement

La clasificación deberá comprobarse en:

- Registration;
- Discovery;
- Matching;
- Routing;
- Invocation;
- Logging;
- Audit;
- Backup;
- Replication.

---

# Classification Policy

```yaml
classification_policy:
  id: ENGINE-CLASSIFICATION-POLICY-STANDARD

  levels:
    - public
    - internal
    - confidential
    - restricted

  inheritance:
    higher_includes_lower: true
```

---

# Classification Downgrade

No deberá permitirse sin una transformación autorizada.

---

# Data Residency Enforcement

La seguridad deberá validar:

- processing region;
- storage region;
- logging region;
- backup region;
- Provider location;
- failover region.

---

# Registration Authorization

No todo principal podrá registrar cualquier recurso.

---

# Definition Registration Requirements

- Engine Owner;
- valid Provider;
- signed manifest;
- approved namespace;
- review;
- Quality Gates.

---

# Instance Registration Requirements

- workload identity;
- Definition activa;
- deployment authorized;
- endpoint authorized;
- region allowed;
- environment allowed.

---

# Discovery Authorization

Una consulta Discovery podrá estar limitada.

---

# Ejemplo

Un usuario podrá conocer:

- Engine logical name;
- Capability;
- availability;

pero no necesariamente:

- internal address;
- security profile;
- exact certificate;
- provider secret metadata.

---

# Discovery Response Filtering

El resultado deberá adaptarse al principal.

---

# Endpoint Disclosure

Los Endpoints completos solo deberán exponerse a consumidores autorizados.

---

# Routing Authorization

La ruta deberá evaluarse contra:

- principal;
- tenant;
- Engine;
- Provider;
- classification;
- environment;
- operation;
- cost;
- policy.

---

# Administrative Authorization

Operaciones críticas:

```text
activate_definition
retire_definition
change_trust
release_quarantine
force_deregister
override_route
revoke_provider
restore_snapshot
rotate_keys
break_glass
```

---

# Strong Authentication

Deberá requerirse para acciones críticas.

---

# Approval Workflow

Formato recomendado:

```text
ENGINE-SECURITY-APPROVAL-XXXXXX
```

---

# Contrato

```yaml
security_approval:
  id: ENGINE-SECURITY-APPROVAL-000041

  action: engine_definition.change_trust

  target:
    id: ENGINE-DEF-RAG-EXTERNAL
    version: 1.0.0

  required_approvers:
    - security_admin
    - platform_admin

  decisions:
    - approver: USER-SECURITY-0001
      decision: approve

    - approver: USER-PLATFORM-0001
      decision: approve

  status: approved
```

---

# Separation of Duties

Ejemplos:

```text
Engine Owner proposes
Security Admin reviews
Platform Admin activates
```

---

# No Auto-Approval by Requester

El solicitante no deberá aprobar su propia operación crítica.

---

# Four-Eyes Principle

Al menos dos actores para acciones de alto riesgo.

---

# Break-Glass Access

Permite actuar durante una emergencia.

Formato recomendado:

```text
ENGINE-BREAK-GLASS-XXXXXX
```

---

# Contrato

```yaml
break_glass_access:
  id: ENGINE-BREAK-GLASS-000041

  actor:
    id: USER-EMERGENCY-OPERATOR-0001

  reason:
    code: ACTIVE_SECURITY_INCIDENT

  permissions:
    - engine_provider.suspend
    - engine_route.disable

  expires_at: 2026-08-02T21:00:00Z

  status: active
```

---

# Requisitos

- duración corta;
- MFA;
- reason obligatorio;
- alert inmediata;
- audit completa;
- revisión posterior.

---

# No Break-Glass Permanente

---

# Session Security

Las sesiones administrativas deberán:

- expirar;
- revocarse;
- estar ligadas a MFA;
- limitarse por riesgo;
- registrar device y context cuando proceda.

---

# Secret Management

El Registry no deberá almacenar secretos.

---

# Secret Reference

```yaml
secret_reference:
  id: SECRET-REF-ENGINE-PROVIDER-001

  provider:
    id: SECRETS-MANAGER-PRIMARY

  path: engines/providers/external-001

  version: current
```

---

# Secrets Types

- client secrets;
- API keys;
- private keys;
- certificates;
- database credentials;
- signing keys;
- webhook secrets.

---

# Secret Access

Deberá realizarse just-in-time por el componente autorizado.

---

# Secret Rotation

Toda credencial deberá declarar:

- owner;
- rotation interval;
- last rotation;
- next rotation;
- revocation process.

---

# Secret Rotation Contract

```yaml
secret_rotation_policy:
  id: ENGINE-SECRET-ROTATION-STANDARD

  maximum_age: P90D

  overlap:
    duration: P7D

  automatic_rotation: true

  audit_required: true
```

---

# Dual Credential Rotation

Se recomienda:

```text
Introduce New Credential
↓
Allow Old + New
↓
Migrate Consumers
↓
Revoke Old
```

---

# Credential Profile

Formato recomendado:

```text
ENGINE-CREDENTIAL-PROFILE-XXXXXX
```

---

# Contrato

```yaml
credential_profile:
  id: ENGINE-CREDENTIAL-PROFILE-EXTERNAL-001

  authentication:
    method: oauth2_client_credentials

  secret_reference:
    id: SECRET-REF-ENGINE-PROVIDER-001

  rotation_policy:
    id: ENGINE-SECRET-ROTATION-STANDARD

  status: active
```

---

# mTLS

La comunicación interna crítica deberá utilizar autenticación mutua.

---

# mTLS Profile

```yaml
mtls_profile:
  id: ENGINE-MTLS-PROFILE-INTERNAL

  trust_domain: novacoquinaria.internal

  minimum_tls_version: "1.3"

  client_certificate_required: true
  server_certificate_required: true

  revocation_check: required
```

---

# Certificate Lifecycle

Estados:

```text
requested
issued
active
rotating
revoked
expired
compromised
```

---

# Certificate Contract

```yaml
certificate_record:
  id: ENGINE-CERTIFICATE-000041

  subject:
    principal: ENGINE-PRINCIPAL-WORKLOAD-RETRIEVAL-001

  issuer:
    id: NOVACOQUINARIA-INTERNAL-CA

  valid_from: 2026-08-02T00:00:00Z
  valid_until: 2026-08-03T00:00:00Z

  status: active
```

---

# Short-Lived Certificates

Se recomienda para workloads.

---

# Certificate Revocation

Deberá propagarse rápidamente a:

- Registry Nodes;
- Registration Gateway;
- Discovery;
- Routing;
- Service Mesh.

---

# Certificate Pinning

Podrá utilizarse para proveedores críticos, con gobernanza de rotación.

---

# Manifest Signing

Los Engine Manifests deberán poder firmarse.

---

# Signature Contract

```yaml
manifest_signature:
  algorithm: ed25519

  signer:
    id: ENGINE-PRINCIPAL-TEAM-KNOWLEDGE-PLATFORM

  key_id: SIGNING-KEY-0001

  signed_at: 2026-08-02T20:00:00Z

  value: ...
```

---

# Signature Verification

Deberá comprobar:

- signer autorizado;
- key válida;
- manifest fingerprint;
- timestamp;
- revocation;
- algorithm policy.

---

# Signature Failure

```text
ENGINE_MANIFEST_SIGNATURE_INVALID
```

---

# Multi-Signature

Definitions críticas podrán requerir varias firmas.

---

# Snapshot Signing

Los Registry Snapshots deberán poder firmarse.

---

# Snapshot Signature

```yaml
registry_snapshot_signature:
  snapshot:
    id: ENGINE-REGISTRY-SNAPSHOT-20260802-0001

  fingerprint: ...

  signer:
    id: ENGINE-REGISTRY-SIGNING-SERVICE

  algorithm: ed25519
```

---

# Restore Verification

No deberá restaurarse un Snapshot cuya firma no sea válida.

---

# Journal Integrity

El Journal podrá mantener una cadena de hashes.

---

# Journal Entry Integrity

```yaml
journal_integrity:
  sequence: 84321
  previous_hash: ...
  current_hash: ...
  signature: ...
```

---

# Event Signing

Los eventos críticos podrán firmarse.

---

# Eventos candidatos

- trust changed;
- provider suspended;
- quarantine applied;
- route disabled;
- snapshot restored;
- key rotated;
- Definition activated.

---

# Cryptographic Profile

Formato recomendado:

```text
ENGINE-CRYPTO-PROFILE-XXXXXX
```

---

# Contrato

```yaml
cryptographic_profile:
  id: ENGINE-CRYPTO-PROFILE-STANDARD

  signatures:
    allowed:
      - ed25519
      - ecdsa-p256

  hashes:
    allowed:
      - sha256
      - sha384

  transport:
    minimum_tls: "1.3"

  deprecated:
    - sha1
    - rsa-1024
```

---

# Algorithm Agility

Los algoritmos deberán poder cambiarse sin romper contratos.

---

# Key Management

Las claves deberán administrarse mediante un KMS o HSM cuando proceda.

---

# Key Types

```text
signing
encryption
mTLS CA
token signing
backup encryption
snapshot signing
provider federation
```

---

# Key Record

```yaml
key_record:
  id: ENGINE-KEY-SNAPSHOT-SIGNING-0001

  type: signing

  provider:
    id: KMS-PRIMARY

  algorithm: ed25519

  status: active

  rotation:
    next_at: 2026-11-01T00:00:00Z
```

---

# Key Rotation

Deberá preservar capacidad de verificar artefactos históricos.

---

# Verification Key Retention

Las claves públicas antiguas deberán conservarse durante la retención de:

- Manifests;
- Snapshots;
- Journal;
- Events;
- Audit.

---

# Key Compromise

Proceso:

```text
Detect Compromise
↓
Revoke Key
↓
Block New Signatures
↓
Identify Affected Records
↓
Re-sign or Quarantine
↓
Rotate Credentials
↓
Audit and Incident Review
```

---

# Supply Chain Security

El Registry deberá vincular un Engine con su procedencia software.

---

# Supply Chain Objects

```text
source repository
commit
build
artifact
container image
SBOM
signature
attestation
deployment
Engine Definition
Engine Instance
```

---

# Engine Build Provenance

```yaml
engine_build_provenance:
  engine_definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  source:
    repository: REPO-RETRIEVAL
    commit: abc123...

  build:
    id: BUILD-20260802-0041

  artifact:
    digest: sha256:...

  attestation:
    id: ATTESTATION-ENGINE-000041
```

---

# Artifact Attestation

Formato recomendado:

```text
ENGINE-ATTESTATION-XXXXXX
```

---

# Contrato

```yaml
engine_attestation:
  id: ENGINE-ATTESTATION-000041

  subject:
    artifact_digest: sha256:...

  predicate:
    build_system: BUILD-SYSTEM-PRIMARY
    source_commit: abc123...
    tests_passed: true
    vulnerability_scan_passed: true

  signer:
    id: BUILD-SIGNING-SERVICE

  status: verified
```

---

# SBOM

Todo Engine desplegable deberá disponer de Software Bill of Materials cuando proceda.

---

# SBOM Reference

```yaml
sbom_reference:
  id: SBOM-ENGINE-RETRIEVAL-2.1.0
  format: cyclonedx
  artifact_digest: sha256:...
```

---

# Vulnerability Policy

La activación deberá considerar vulnerabilidades.

---

# Vulnerability Levels

```text
low
medium
high
critical
```

---

# Policy Example

```yaml
vulnerability_policy:
  id: ENGINE-VULNERABILITY-POLICY-PRODUCTION

  block:
    - critical

  require_approval:
    - high

  allowed:
    - medium
    - low
```

---

# Exception

Toda excepción deberá declarar:

- vulnerability;
- justification;
- owner;
- expiration;
- compensating controls;
- approval.

---

# Image or Artifact Verification

Una Engine Instance deberá demostrar que ejecuta el Artifact aprobado.

---

# Runtime Attestation

Podrá verificar:

- image digest;
- deployment ID;
- workload identity;
- node;
- environment;
- secure boot;
- runtime policy.

---

# Definition-to-Deployment Binding

```yaml
definition_deployment_binding:
  definition:
    id: ENGINE-DEF-RETRIEVAL-HYBRID
    version: 2.1.0

  artifact:
    digest: sha256:...

  deployment:
    id: DEPLOYMENT-RETRIEVAL-20260802-001

  verification:
    status: passed
```

---

# Endpoint Security

Los Endpoints deberán validar:

- ownership;
- DNS or service reference;
- certificate;
- protocol;
- network zone;
- operation scope;
- environment;
- region.

---

# Endpoint Allowlist

Podrá limitar dominios o service namespaces.

---

# Endpoint Poisoning Protection

Una Instance no deberá poder modificar su endpoint hacia un destino no autorizado mediante heartbeat.

---

# Endpoint Change Approval

Cambios sensibles deberán requerir:

- revision;
- deployment source;
- signature;
- revalidation.

---

# SSRF Protection

El Registry y sus Health Monitors deberán impedir probes contra destinos arbitrarios.

---

# Callback Security

Callbacks deberán utilizar:

- signed payload;
- nonce;
- timestamp;
- mTLS o secret;
- idempotency;
- allowlisted destination.

---

# Event Security

Los eventos deberán:

- autenticar producer;
- validar schema;
- preservar tenant;
- minimizar payload;
- aplicar encryption cuando proceda;
- permitir deduplicación;
- conservar signature para eventos críticos.

---

# Cache Security

Las caches deberán:

- aplicar tenant isolation;
- no almacenar secrets;
- invalidar trust changes;
- proteger datos de endpoints;
- cifrar cuando proceda;
- evitar cache poisoning.

---

# Cache Poisoning Protection

Toda entrada deberá proceder de:

- State Store;
- Journal;
- verified event;
- trusted Registry Node.

---

# Snapshot Security

Los Snapshots deberán:

- cifrarse;
- firmarse;
- aplicar access control;
- preservar tenant boundaries;
- auditar restore;
- impedir downgrade.

---

# Snapshot Rollback Protection

No deberá restaurarse un Snapshot antiguo sin autorización explícita.

---

# Downgrade Detection

El Restore deberá comparar:

- sequence;
- epoch;
- schema version;
- trust changes;
- revocations.

---

# Backup Security

Los backups deberán:

- cifrarse;
- usar credenciales separadas;
- aplicar retention;
- soportar immutability;
- auditar restores;
- probar recovery.

---

# Registry Node Security

Los Nodes deberán:

- utilizar workload identity;
- aplicar mTLS;
- ejecutar software firmado;
- limitar permisos;
- aislar storage;
- aplicar patching;
- emitir health;
- usar fencing epoch.

---

# Node Joining

Un nuevo Node deberá:

1. autenticar identidad;
2. demostrar pertenencia al cluster;
3. validar versión;
4. verificar Artifact;
5. obtener aprobación o policy;
6. sincronizar Snapshot;
7. verificar Journal;
8. entrar en estado `active`.

---

# Unauthorized Node

Código:

```text
ENGINE_REGISTRY_NODE_NOT_AUTHORIZED
```

---

# Cluster Membership

Los cambios deberán auditarse y firmarse.

---

# Security Quarantine

Una **Security Quarantine** bloquea un recurso por riesgo.

---

# Scopes

```text
provider
definition
instance
endpoint
operation
route
registry_node
credential
artifact
```

---

# Security Quarantine Contract

```yaml
security_quarantine:
  id: ENGINE-SECURITY-QUARANTINE-000041

  target:
    type: engine_provider
    id: ENGINE-PROVIDER-EXTERNAL-001

  reason:
    code: CREDENTIAL_COMPROMISE

  effects:
    discovery: blocked
    routing: blocked
    lease_renewal: blocked
    registration: blocked

  status: active
```

---

# Quarantine Priority

Security Quarantine deberá prevalecer sobre:

- availability;
- routing weights;
- user preferences;
- fallback policies.

---

# Release Requirements

- incident resolved;
- credentials rotated;
- verification passed;
- approval;
- audit;
- cache invalidation.

---

# Threat Model

El Registry deberá mantener un Threat Model actualizado.

---

# Threat Categories

```text
spoofing
tampering
repudiation
information_disclosure
denial_of_service
elevation_of_privilege
supply_chain
insider_threat
cross_tenant_access
rollback_attack
cache_poisoning
endpoint_poisoning
```

---

# Threat Examples

---

## Spoofed Engine Instance

Una carga intenta registrarse como una Instance autorizada.

Control:

- workload identity;
- mTLS;
- deployment binding;
- fencing token.

---

## Tampered Manifest

Una Definition fue alterada.

Control:

- fingerprint;
- signature;
- immutable version;
- Journal.

---

## Malicious Endpoint

Una Instance anuncia una URL externa.

Control:

- allowlist;
- deployment-driven source;
- endpoint validation.

---

## Trust Escalation

Un owner intenta elevar un Provider.

Control:

- separation of duties;
- Security Approval;
- audit.

---

## Rollback Attack

Se restaura un Snapshot anterior a una revocación.

Control:

- restore epoch;
- monotonic sequence;
- revocation replay;
- signed Snapshot.

---

## Cache Poisoning

Un nodo introduce una entrada falsa.

Control:

- signed events;
- trusted source;
- version checks;
- cache invalidation.

---

## Cross-Tenant Discovery

Un tenant consulta Engines dedicados de otro.

Control:

- tenant-scoped authorization;
- filtered responses.

---

## Supply Chain Compromise

Un deployment ejecuta un Artifact distinto.

Control:

- digest binding;
- attestation;
- runtime verification.

---

# Security Event

Formato recomendado:

```text
ENGINE-SECURITY-EVENT-XXXXXX
```

---

# Contrato

```yaml
security_event:
  id: ENGINE-SECURITY-EVENT-000041

  type: engine_manifest_signature_failed

  severity: critical

  subject:
    type: engine_definition
    id: ENGINE-DEF-RETRIEVAL-HYBRID

  actor:
    id: ENGINE-PRINCIPAL-TEAM-KNOWLEDGE-PLATFORM

  occurred_at: 2026-08-02T20:00:00Z

  correlation_id: CORR-000041
```

---

# Security Event Categories

```text
authentication
authorization
trust
credential
signature
integrity
supply_chain
tenant
endpoint
quarantine
administrative
anomaly
incident
```

---

# Security Events iniciales

```text
engine_authentication_failed
engine_authorization_denied
engine_identity_revoked
engine_provider_suspended
engine_trust_changed
engine_trust_downgraded
engine_manifest_signature_failed
engine_snapshot_signature_failed
engine_certificate_expired
engine_certificate_revoked
engine_key_rotated
engine_key_compromised
engine_endpoint_rejected
engine_endpoint_poisoning_detected
engine_cross_tenant_access_denied
engine_security_quarantine_applied
engine_security_quarantine_released
engine_break_glass_activated
engine_break_glass_expired
engine_supply_chain_attestation_failed
engine_vulnerability_policy_violated
registry_node_join_rejected
registry_snapshot_rollback_blocked
```

---

# Security Logging

Todo log de seguridad deberá incluir:

- timestamp;
- principal;
- action;
- resource;
- tenant;
- environment;
- decision;
- policy;
- reason;
- correlation;
- authentication assurance.

---

# No incluir

- secrets;
- raw tokens;
- private keys;
- full certificates;
- personal data innecesaria;
- request payload completo.

---

# Audit Trail

El **Registry Security Audit Trail** deberá ser append-only.

---

# Audit Record

```yaml
security_audit_record:
  id: ENGINE-SECURITY-AUDIT-000041

  action: engine_definition.change_trust

  actor:
    id: USER-SECURITY-0001

  target:
    id: ENGINE-DEF-RAG-EXTERNAL
    version: 1.0.0

  previous:
    trust: experimental

  resulting:
    trust: approved_external

  approval:
    id: ENGINE-SECURITY-APPROVAL-000041

  occurred_at: 2026-08-02T20:00:00Z
```

---

# Audit Requirements

- append-only;
- integrity protected;
- searchable;
- retention;
- access controlled;
- exportable;
- legal hold;
- correlation;
- non-repudiation cuando proceda.

---

# Audit Categories

```text
identity
authentication
authorization
registration
lifecycle
trust
quarantine
provider
route
policy
credential
key
snapshot
restore
break_glass
incident
```

---

# Audit Retention

Deberá definirse por:

- environment;
- legal requirements;
- tenant;
- severity;
- action type.

---

# Security Monitoring

La plataforma deberá detectar:

- failed authentication bursts;
- authorization anomalies;
- unexpected endpoint changes;
- trust modifications;
- unusual Discovery patterns;
- repeated lease failures;
- signature failures;
- Registry Node changes;
- quarantine releases;
- break-glass use;
- snapshot restore attempts.

---

# Security Detection Rule

Formato recomendado:

```text
ENGINE-DETECTION-RULE-XXXXXX
```

---

# Contrato

```yaml
security_detection_rule:
  id: ENGINE-DETECTION-RULE-ENDPOINT-CHURN

  condition:
    endpoint_changes:
      greater_than: 5
      window: PT10M

  scope:
    engine_instance: any

  severity: high

  action:
    - alert
    - quarantine_candidate
```

---

# Threat Detection States

```text
observed
suspected
confirmed
false_positive
resolved
```

---

# Security Alert

```yaml
security_alert:
  id: ENGINE-SECURITY-ALERT-000041

  severity: critical

  rule:
    id: ENGINE-DETECTION-RULE-ENDPOINT-CHURN

  target:
    instance: ENGINE-INSTANCE-RETRIEVAL-EU-001

  recommended_actions:
    - quarantine
    - revoke_lease
    - investigate_deployment
```

---

# Incident Response

Formato recomendado:

```text
ENGINE-SECURITY-INCIDENT-XXXXXX
```

---

# Incident Lifecycle

```text
detected
triaged
contained
investigating
remediating
recovering
closed
```

---

# Incident Contract

```yaml
security_incident:
  id: ENGINE-SECURITY-INCIDENT-000041

  type: provider_credential_compromise

  severity: critical

  affected:
    provider:
      id: ENGINE-PROVIDER-EXTERNAL-001

  containment:
    provider_suspended: true
    credentials_revoked: true
    routes_disabled: true

  status: contained
```

---

# Containment Actions

- revoke credential;
- suspend Provider;
- quarantine Instance;
- disable Route;
- invalidate caches;
- stop lease renewal;
- rotate key;
- block registration;
- activate emergency mode.

---

# Security Recovery

Antes de restaurar servicio deberá:

- validar identity;
- rotate credentials;
- verify Artifacts;
- rerun Quality Gates;
- reconcile Instances;
- review routes;
- update threat model;
- document incident.

---

# Forensics

Deberán conservarse:

- Journal entries;
- Audit Records;
- security events;
- signatures;
- snapshots;
- endpoint history;
- authentication context;
- route decisions;
- lease history.

---

# Compliance

El Registry deberá poder aplicar requisitos de cumplimiento.

---

# Compliance Domains

```text
data_protection
access_control
auditability
retention
residency
third_party
cryptography
incident_response
change_management
business_continuity
```

---

# Compliance Profile

Formato recomendado:

```text
ENGINE-COMPLIANCE-PROFILE-XXXXXX
```

---

# Contrato

```yaml
compliance_profile:
  id: ENGINE-COMPLIANCE-PROFILE-PRODUCTION

  controls:
    access_reviews: required
    mfa_for_admin: required
    audit_retention: P2555D
    encryption_at_rest: required
    encryption_in_transit: required
    restore_testing: required
    provider_review: annual
```

---

# Control Evidence

Cada control deberá poder producir evidencia.

---

# Evidence Types

- policy version;
- Audit Record;
- certificate;
- attestation;
- scan result;
- approval;
- restore test;
- access review;
- key rotation record;
- incident report.

---

# Compliance Evidence Record

```yaml
compliance_evidence:
  id: ENGINE-COMPLIANCE-EVIDENCE-000041

  control:
    id: CONTROL-MANIFEST-SIGNATURE

  subject:
    definition: ENGINE-DEF-RETRIEVAL-HYBRID@2.1.0

  evidence:
    signature_valid: true
    signer_authorized: true

  collected_at: 2026-08-02T20:00:00Z
```

---

# Access Review

Los permisos deberán revisarse periódicamente.

---

# Access Review Contract

```yaml
access_review:
  id: ENGINE-ACCESS-REVIEW-2026-Q3

  scope:
    environment: production
    roles:
      - platform_admin
      - security_admin
      - emergency_operator

  status: completed
```

---

# Dormant Access

Los permisos no utilizados podrán revocarse.

---

# Provider Review

Los proveedores externos deberán revisarse periódicamente.

---

# Review Dimensions

- trust;
- contract;
- security;
- compliance;
- certifications;
- sub-processors;
- data policy;
- incident history;
- availability;
- SLA.

---

# Security Observability

---

# Metrics de Identity

- active principals;
- revoked principals;
- failed authentication;
- MFA challenges;
- certificate expirations;
- workload attestation failures.

---

# Metrics de Authorization

- permit;
- deny;
- indeterminate;
- policy evaluation latency;
- denied actions by type;
- cross-tenant denies.

---

# Metrics de Credentials

- credentials by age;
- overdue rotations;
- revocations;
- failed secret retrieval;
- expired certificates.

---

# Metrics de Integrity

- signature verification failures;
- fingerprint mismatches;
- Snapshot verification failures;
- Journal integrity errors;
- attestation failures.

---

# Metrics de Supply Chain

- Definitions without SBOM;
- unsigned Artifacts;
- vulnerable Builds;
- runtime digest mismatches;
- expired attestations.

---

# Metrics de Audit

- audit write failures;
- audit lag;
- evidence gaps;
- retention violations;
- unauthorized audit access.

---

# Metrics de Incidents

- incidents;
- time to detect;
- time to contain;
- time to recover;
- quarantine duration;
- break-glass usage.

---

# Security SLIs

```text
authentication_success_rate
authorization_decision_latency
revocation_propagation_time
signature_verification_success
audit_record_durability
quarantine_activation_time
credential_rotation_compliance
```

---

# Security SLO Examples

```text
Credential revocation propagation < 60 s

Critical quarantine activation < 30 s

Audit write availability ≥ 99.99 %

Manifest signature verification = 100 %
```

---

# Security Diagnostics

Códigos iniciales:

```text
ENGINE_AUTHENTICATION_FAILED
ENGINE_AUTHENTICATION_ASSURANCE_INSUFFICIENT
ENGINE_AUTHORIZATION_DENIED
ENGINE_AUTHORIZATION_INDETERMINATE
ENGINE_PRINCIPAL_NOT_FOUND
ENGINE_PRINCIPAL_SUSPENDED
ENGINE_PRINCIPAL_REVOKED
ENGINE_WORKLOAD_IDENTITY_INVALID
ENGINE_PROVIDER_IDENTITY_INVALID
ENGINE_REGISTRY_NODE_NOT_AUTHORIZED
ENGINE_TENANT_SCOPE_VIOLATION
ENGINE_ENVIRONMENT_SCOPE_VIOLATION
ENGINE_REGION_SCOPE_VIOLATION
ENGINE_CLASSIFICATION_POLICY_VIOLATION
ENGINE_RESIDENCY_POLICY_VIOLATION
ENGINE_TRUST_LEVEL_INSUFFICIENT
ENGINE_TRUST_CHANGE_NOT_AUTHORIZED
ENGINE_PROVIDER_SUSPENDED
ENGINE_BREAK_GLASS_REQUIRED
ENGINE_BREAK_GLASS_EXPIRED
ENGINE_SEPARATION_OF_DUTIES_VIOLATED
ENGINE_APPROVAL_REQUIRED
ENGINE_APPROVAL_INVALID
ENGINE_SECRET_REFERENCE_INVALID
ENGINE_SECRET_ROTATION_OVERDUE
ENGINE_SECRET_RETRIEVAL_FAILED
ENGINE_CERTIFICATE_INVALID
ENGINE_CERTIFICATE_EXPIRED
ENGINE_CERTIFICATE_REVOKED
ENGINE_MTLS_REQUIRED
ENGINE_MANIFEST_SIGNATURE_INVALID
ENGINE_SNAPSHOT_SIGNATURE_INVALID
ENGINE_EVENT_SIGNATURE_INVALID
ENGINE_FINGERPRINT_MISMATCH
ENGINE_JOURNAL_INTEGRITY_FAILED
ENGINE_KEY_NOT_FOUND
ENGINE_KEY_REVOKED
ENGINE_KEY_ROTATION_OVERDUE
ENGINE_CRYPTOGRAPHIC_ALGORITHM_NOT_ALLOWED
ENGINE_ARTIFACT_ATTESTATION_MISSING
ENGINE_ARTIFACT_ATTESTATION_INVALID
ENGINE_SBOM_MISSING
ENGINE_VULNERABILITY_POLICY_VIOLATED
ENGINE_RUNTIME_ARTIFACT_MISMATCH
ENGINE_ENDPOINT_SECURITY_INVALID
ENGINE_ENDPOINT_POISONING_DETECTED
ENGINE_CALLBACK_SIGNATURE_INVALID
ENGINE_CACHE_POISONING_DETECTED
ENGINE_SECURITY_QUARANTINED
ENGINE_SECURITY_QUARANTINE_RELEASE_DENIED
ENGINE_AUDIT_WRITE_FAILED
ENGINE_AUDIT_INTEGRITY_FAILED
ENGINE_COMPLIANCE_EVIDENCE_MISSING
ENGINE_ACCESS_REVIEW_OVERDUE
ENGINE_SECURITY_INCIDENT_ACTIVE
```

---

# Diagnostic Contract

```yaml
engine_security_diagnostic:
  id: ENGINE-SECURITY-DIAGNOSTIC-000041

  code: ENGINE_RUNTIME_ARTIFACT_MISMATCH
  severity: critical

  target:
    instance: ENGINE-INSTANCE-RETRIEVAL-EU-001

  expected:
    artifact_digest: sha256:expected

  observed:
    artifact_digest: sha256:unexpected

  actions:
    - quarantine_instance
    - revoke_lease
    - open_incident

  retryable: false
```

---

# Quality Gate de Identity

```yaml
quality_gate:
  id: QG-ENGINE-IDENTITY-0001

  criteria:
    all:
      - principal_identity_verified == true
      - identity_provider_trusted == true
      - subject_not_revoked == true
      - authentication_assurance_sufficient == true
      - tenant_scope_valid == true
      - environment_scope_valid == true
      - replay_protection_enabled == true
```

---

# Quality Gate de Authorization

```yaml
quality_gate:
  id: QG-ENGINE-AUTHORIZATION-0001

  criteria:
    all:
      - deny_by_default_enabled == true
      - rbac_role_resolved == true
      - abac_attributes_current == true
      - resource_scope_valid == true
      - tenant_isolation_preserved == true
      - environment_isolation_preserved == true
      - separation_of_duties_applied == true
      - authorization_decision_audited == true
```

---

# Quality Gate de Trust

```yaml
quality_gate:
  id: QG-ENGINE-TRUST-0001

  criteria:
    all:
      - trust_level_defined == true
      - provider_trust_profile_valid == true
      - classification_constraints_defined == true
      - residency_constraints_defined == true
      - production_permission_explicit == true
      - external_processing_policy_defined == true
      - trust_change_approved == true
```

---

# Quality Gate de Secrets

```yaml
quality_gate:
  id: QG-ENGINE-SECRETS-0001

  criteria:
    all:
      - no_plaintext_secrets_in_registry == true
      - secret_references_valid == true
      - credential_profiles_versioned == true
      - rotation_policy_defined == true
      - overdue_rotations == 0
      - secret_access_audited == true
      - revocation_process_defined == true
```

---

# Quality Gate de Certificates

```yaml
quality_gate:
  id: QG-ENGINE-CERTIFICATES-0001

  criteria:
    all:
      - mtls_enabled_for_internal_traffic == true
      - certificates_valid == true
      - certificate_subject_matches_identity == true
      - revocation_checks_enabled == true
      - short_lived_workload_certificates_enabled == true
      - certificate_rotation_current == true
```

---

# Quality Gate de Cryptographic Integrity

```yaml
quality_gate:
  id: QG-ENGINE-CRYPTO-INTEGRITY-0001

  criteria:
    all:
      - manifest_fingerprint_valid == true
      - manifest_signature_valid == true
      - snapshot_signature_valid == true
      - journal_integrity_valid == true
      - cryptographic_profile_current == true
      - deprecated_algorithms_absent == true
      - signing_keys_not_revoked == true
```

---

# Quality Gate de Supply Chain

```yaml
quality_gate:
  id: QG-ENGINE-SUPPLY-CHAIN-0001

  criteria:
    all:
      - source_commit_identified == true
      - build_identified == true
      - artifact_digest_verified == true
      - build_attestation_valid == true
      - sbom_available == true
      - vulnerability_policy_passed == true
      - runtime_artifact_matches_approved_artifact == true
```

---

# Quality Gate de Endpoint Security

```yaml
quality_gate:
  id: QG-ENGINE-ENDPOINT-SECURITY-0001

  criteria:
    all:
      - endpoint_source_authorized == true
      - endpoint_address_allowed == true
      - protocol_security_valid == true
      - certificate_valid == true
      - environment_matches == true
      - region_matches == true
      - operation_scope_valid == true
      - endpoint_revision_valid == true
```

---

# Quality Gate de Audit

```yaml
quality_gate:
  id: QG-ENGINE-SECURITY-AUDIT-0001

  criteria:
    all:
      - audit_store_append_only == true
      - audit_integrity_enabled == true
      - critical_actions_audited == true
      - actor_identity_present == true
      - correlation_present == true
      - retention_policy_defined == true
      - legal_hold_supported == true
      - audit_access_restricted == true
```

---

# Quality Gate de Incident Response

```yaml
quality_gate:
  id: QG-ENGINE-INCIDENT-RESPONSE-0001

  criteria:
    all:
      - detection_rules_defined == true
      - quarantine_supported == true
      - credential_revocation_supported == true
      - provider_suspension_supported == true
      - cache_invalidation_supported == true
      - incident_runbooks_available == true
      - evidence_preservation_defined == true
      - recovery_validation_defined == true
```

---

# Quality Gate de Compliance

```yaml
quality_gate:
  id: QG-ENGINE-COMPLIANCE-0001

  criteria:
    all:
      - compliance_profile_versioned == true
      - access_reviews_current == true
      - provider_reviews_current == true
      - encryption_in_transit_enabled == true
      - encryption_at_rest_enabled == true
      - retention_compliant == true
      - restore_tests_current == true
      - control_evidence_available == true
```

---

# Casos de uso

---

# Caso de uso 1 — Registro autenticado

Una Instance intenta registrarse.

El Registry valida:

- Workload Identity;
- certificado;
- deployment;
- Definition;
- environment;
- endpoint.

Solo entonces emite la Registration Lease.

---

# Caso de uso 2 — Manifest manipulado

El fingerprint del Manifest no coincide con su firma.

La Definition se rechaza y se genera un Security Event.

---

# Caso de uso 3 — Elevación de Trust

Un Engine Owner solicita pasar un Provider de `experimental` a `approved_external`.

Se requieren:

- revisión de seguridad;
- aprobación Platform;
- evidencia;
- Audit Record.

---

# Caso de uso 4 — Cross-Tenant Discovery

Un usuario de TENANT-0001 intenta descubrir una Instance dedicada a TENANT-0002.

La respuesta la excluye y registra autorización denegada.

---

# Caso de uso 5 — Certificado revocado

Una Instance continúa enviando Heartbeats con un certificado revocado.

La autenticación falla, la lease no se renueva y la Instance expira.

---

# Caso de uso 6 — Endpoint Poisoning

Una Instance intenta cambiar su Endpoint hacia un dominio no permitido.

El cambio se rechaza y la Instance entra en Security Quarantine.

---

# Caso de uso 7 — Runtime Artifact Mismatch

El deployment ejecuta un digest distinto del aprobado.

Se revoca la lease y se abre un incidente.

---

# Caso de uso 8 — Vulnerabilidad crítica

Una nueva vulnerabilidad crítica afecta a una versión activa.

La Vulnerability Policy bloquea nuevas selecciones y activa el proceso de sustitución.

---

# Caso de uso 9 — Break-Glass

Durante un incidente, un Emergency Operator suspende un Provider.

El acceso expira automáticamente y se revisa después del incidente.

---

# Caso de uso 10 — Restore Rollback Attack

Se intenta restaurar un Snapshot anterior a una revocación de credenciales.

El Restore Epoch y la secuencia monotónica bloquean la restauración no autorizada.

---

# Caso de uso 11 — Cache Stale tras Trust Downgrade

Un Provider pierde autorización.

El evento crítico invalida las caches y el Routing deja de seleccionarlo inmediatamente.

---

# Caso de uso 12 — Firma histórica

Una Definition antigua fue firmada con una clave ya rotada.

La clave pública se conserva para verificar el registro histórico.

---

# Caso de uso 13 — Quarantine de Operation

Una única Operation produce datos inválidos.

Se bloquea esa Operation sin retirar el resto de capacidades de la Instance.

---

# Caso de uso 14 — Provider externo

El proveedor solo está autorizado para:

- datos públicos;
- región europea;
- sin retención;
- sin entrenamiento.

El Routing aplica estas restricciones como hard constraints.

---

# Caso de uso 15 — Auditoría

Un auditor reconstruye:

- quién activó una Definition;
- qué firmas se validaron;
- qué Artifact se desplegó;
- qué Trust Level se aprobó;
- qué Routes la utilizaron.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Confiar en la red interna

La ubicación no sustituye autenticación.

---

## Compartir una credencial entre todas las Instances

Impide revocación y trazabilidad granular.

---

## API Key permanente

Debe preferirse identidad y credenciales temporales.

---

## Self-Reported Trust

Una Instance no decide su propio nivel de confianza.

---

## RBAC sin contexto

Un rol amplio puede ser insuficiente sin ABAC.

---

## ABAC sin fuente autoritativa

Los atributos deberán proceder de sistemas confiables.

---

## Permitir acceso global mediante wildcard por defecto

Debe ser explícito y revisado.

---

## Mezclar entornos

Una identidad de staging no deberá operar en producción.

---

## Registrar Secrets en Metadata

El Registry solo conserva referencias.

---

## No rotar credenciales

Aumenta riesgo de compromiso prolongado.

---

## Certificados de larga duración para workloads

Dificultan revocación.

---

## No comprobar revocación

Un certificado formalmente válido puede haber sido revocado.

---

## Firmar sin comprobar autorización del signer

La firma criptográfica no implica aprobación.

---

## Fingerprint sin firma

Detecta cambios, pero no autenticidad.

---

## Firma sin fingerprint canónico

Puede generar ambigüedad de serialización.

---

## Restaurar Snapshot sin verificar firma

Puede introducir estado manipulado.

---

## Restaurar un Snapshot antiguo sin epoch

Puede reactivar recursos revocados.

---

## Journal sin cadena de integridad

Dificulta detectar manipulación.

---

## No conservar claves públicas antiguas

Impide verificar histórico.

---

## Utilizar algoritmos obsoletos

Debe existir Crypto Profile.

---

## Deploy sin Attestation

No demuestra provenance.

---

## SBOM sin vinculación al Artifact

Puede corresponder a otro build.

---

## Vulnerability Exception sin expiración

Se convierte en bypass permanente.

---

## Endpoint aceptado desde Heartbeat

Debe validarse contra fuentes autorizadas.

---

## Health Probe arbitraria

Puede convertirse en SSRF.

---

## Cache con datos de seguridad stale

Puede seguir autorizando recursos bloqueados.

---

## Audit mutable

Compromete investigación y compliance.

---

## Audit accesible a todos los operadores

Debe aplicarse acceso mínimo.

---

## Break-Glass sin expiración

Genera privilegios permanentes.

---

## Requester aprobando su propio cambio crítico

Viola Separation of Duties.

---

## Quarantine liberada por el owner afectado

Debe existir revisión independiente.

---

## Security Event sin correlation

Dificulta investigación.

---

## Logging de tokens o certificados completos

Expone credenciales.

---

## Compliance solo documental

Deberá existir evidencia verificable.

---

## Access Review sin consecuencias

Los permisos no justificados deberán revocarse.

---

## Provider aprobado para todos los datos

El Trust debe ser contextual.

---

## Security Failure tratado como Degraded

Los controles críticos deberán fallar de forma cerrada.

---

# Reglas mínimas de conformidad

---

## Zero Trust

Toda operación deberá autenticarse y autorizarse.

---

## Registry Principals

Toda identidad deberá estar tipada y versionada.

---

## Workload Identity

Toda Instance deberá disponer de identidad autenticada.

---

## Node Identity

Todo Registry Node deberá validar pertenencia al cluster.

---

## Deny by Default

Las acciones no permitidas deberán rechazarse.

---

## RBAC y ABAC

La autorización deberá combinar roles y contexto cuando proceda.

---

## Tenant Isolation

Toda operación tenant-aware deberá aplicar scope.

---

## Environment Isolation

Las identidades y permisos deberán separarse por entorno.

---

## Trust Enforcement

El Trust Level deberá ser un hard constraint.

---

## Provider Trust

Todo Provider deberá disponer de perfil.

---

## Registration Authorization

Definitions e Instances deberán registrarse por actores autorizados.

---

## Administrative Approval

Las acciones críticas deberán requerir revisión.

---

## Separation of Duties

Solicitud y aprobación deberán separarse.

---

## Break-Glass

Deberá ser temporal y auditable.

---

## No Secrets

El Registry solo deberá almacenar referencias.

---

## Secret Rotation

Toda credencial deberá tener política.

---

## mTLS

La comunicación interna crítica deberá autenticarse mutuamente.

---

## Certificate Revocation

Deberá comprobarse y propagarse.

---

## Manifest Signature

Las Definitions críticas deberán firmarse.

---

## Snapshot Integrity

Los Snapshots deberán verificarse antes de restore.

---

## Journal Integrity

El historial deberá detectar alteraciones.

---

## Key Management

Las claves deberán administrarse de forma gobernada.

---

## Algorithm Agility

El Crypto Profile deberá estar versionado.

---

## Supply Chain

Toda versión desplegable deberá vincularse a Artifact y Build.

---

## Attestation

Los Artifacts críticos deberán tener provenance verificable.

---

## SBOM

Los Engines desplegables deberán declarar componentes.

---

## Vulnerability Policy

Las vulnerabilidades deberán evaluarse antes de activación y durante operación.

---

## Endpoint Validation

Los Endpoints deberán proceder de fuentes autorizadas.

---

## Runtime Verification

La Instance deberá ejecutar el Artifact aprobado.

---

## Security Quarantine

Los recursos comprometidos deberán poder bloquearse inmediatamente.

---

## Audit

Toda acción crítica deberá conservarse.

---

## Threat Detection

Deberán existir reglas y alertas.

---

## Incident Response

Deberán existir procesos de contención y recuperación.

---

## Compliance Evidence

Los controles deberán producir evidencia.

---

## Access Reviews

Los permisos deberán revisarse periódicamente.

---

## Quality Gates

Ningún Engine o Provider deberá activarse sin superar controles.

---

# Conformidad de Registry Principal

Será conforme cuando:

- tenga ID;
- declare tipo;
- declare identity provider;
- declare subject;
- declare scopes;
- declare status;
- pueda revocarse;
- sea auditable.

---

# Conformidad de Authentication Profile

Será conforme cuando:

- tenga ID;
- esté versionado;
- declare métodos;
- declare assurance;
- declare expiración;
- aplique replay protection;
- declare revocation.

---

# Conformidad de Authorization Decision

Será conforme cuando:

- tenga ID;
- identifique principal;
- identifique acción;
- identifique recurso;
- preserve contexto;
- declare policy;
- declare decisión;
- preserve reason;
- se audite cuando proceda.

---

# Conformidad de Registry Role

Será conforme cuando:

- tenga ID;
- declare permisos;
- declare restricciones;
- preserve scope;
- no otorgue privilegios implícitos;
- tenga owner;
- tenga review date.

---

# Conformidad de Trust Decision

Será conforme cuando:

- identifique Engine o Provider;
- declare nivel;
- declare restricciones;
- preserve evidence;
- preserve approvals;
- declare vigencia;
- sea auditable.

---

# Conformidad de Secret Reference

Será conforme cuando:

- tenga ID;
- identifique Secrets Manager;
- declare path lógico;
- no exponga secreto;
- declare version;
- declare owner;
- declare rotation policy.

---

# Conformidad de Certificate

Será conforme cuando:

- identifique principal;
- declare issuer;
- declare validity;
- declare status;
- preserve serial;
- soporte revocation;
- corresponda al environment.

---

# Conformidad de Manifest Signature

Será conforme cuando:

- declare algorithm;
- identifique signer;
- identifique key;
- preserve timestamp;
- firme representación canónica;
- valide fingerprint;
- use key no revocada.

---

# Conformidad de Cryptographic Profile

Será conforme cuando:

- tenga ID;
- tenga versión;
- declare algoritmos permitidos;
- declare algoritmos deprecated;
- declare TLS mínimo;
- permita rotación;
- preserve compatibilidad histórica.

---

# Conformidad de Attestation

Será conforme cuando:

- tenga ID;
- identifique Artifact;
- declare source;
- declare build;
- preserve tests;
- preserve scans;
- identifique signer;
- tenga firma válida.

---

# Conformidad de Security Quarantine

Será conforme cuando:

- tenga ID;
- declare target;
- declare scope;
- declare reason;
- declare effects;
- prevalezca sobre Routing;
- tenga status;
- preserve approvals de release;
- sea auditable.

---

# Conformidad de Audit Record

Será conforme cuando:

- tenga ID;
- declare actor;
- declare acción;
- declare target;
- declare previous state;
- declare resulting state;
- preserve approval;
- preserve timestamp;
- preserve correlation;
- sea inmutable.

---

# Conformidad de Security Incident

Será conforme cuando:

- tenga ID;
- declare tipo;
- declare severidad;
- declare afectados;
- declare lifecycle;
- declare containment;
- preserve evidencia;
- declare owner;
- preserve timeline;
- declare cierre.

---

# Lista de comprobación

Antes de aprobar la seguridad del Engine Registry deberá comprobarse:

```text
[ ] Existe modelo Zero Trust.
[ ] Toda operación requiere autenticación.
[ ] Toda operación requiere autorización.
[ ] Existe catálogo de Registry Principals.
[ ] Los Principals tienen IDs estables.
[ ] Las User Identities utilizan Identity Provider autorizado.
[ ] Las operaciones críticas exigen MFA.
[ ] Las Service Identities están separadas.
[ ] Las Workload Identities están soportadas.
[ ] Cada Engine Instance tiene identidad propia.
[ ] Cada Registry Node tiene identidad propia.
[ ] La federación de identidad está gobernada.
[ ] Los Authentication Profiles están versionados.
[ ] Las credenciales tienen expiración.
[ ] Existe Replay Protection.
[ ] Se aplica Deny by Default.
[ ] Existen roles RBAC.
[ ] Los roles tienen scopes.
[ ] Se aplica ABAC cuando procede.
[ ] Los atributos proceden de fuentes autoritativas.
[ ] Existe Tenant Isolation.
[ ] Existe Environment Isolation.
[ ] Existe Region Isolation cuando procede.
[ ] El Trust Level es obligatorio.
[ ] Los Providers tienen Trust Profile.
[ ] Los Trust Changes requieren aprobación.
[ ] Los Trust Downgrades invalidan caches.
[ ] La clasificación se valida en Registration.
[ ] La clasificación se valida en Discovery.
[ ] La clasificación se valida en Matching.
[ ] La clasificación se valida en Routing.
[ ] La residencia se valida.
[ ] La retención del Provider se valida.
[ ] La política de training usage se valida.
[ ] Definition Registration está autorizada.
[ ] Instance Registration está autorizada.
[ ] Discovery Response se filtra según Principal.
[ ] Los Endpoints solo se revelan a consumidores autorizados.
[ ] Routing Authorization está definida.
[ ] Las acciones administrativas requieren Strong Authentication.
[ ] Existe Separation of Duties.
[ ] El requester no aprueba su propia acción crítica.
[ ] Existe Four-Eyes Principle para alto riesgo.
[ ] Existe Break-Glass Access.
[ ] Break-Glass tiene expiración.
[ ] Break-Glass genera alerta.
[ ] Break-Glass se revisa posteriormente.
[ ] El Registry no almacena Secrets.
[ ] Los Secret References están gobernados.
[ ] Existe Secret Rotation.
[ ] Existe revocación de credenciales.
[ ] La comunicación interna utiliza mTLS.
[ ] El TLS mínimo está definido.
[ ] Los certificados de workload son short-lived.
[ ] Se comprueba revocación.
[ ] Existe rotación de certificados.
[ ] Los Manifests tienen fingerprint.
[ ] Los Manifests críticos están firmados.
[ ] Los signers están autorizados.
[ ] La serialización firmada es canónica.
[ ] Los Snapshots están firmados.
[ ] Los Snapshots están cifrados.
[ ] El Journal tiene integridad verificable.
[ ] Los eventos críticos pueden firmarse.
[ ] Existe Cryptographic Profile.
[ ] Los algoritmos deprecated están bloqueados.
[ ] Existe Algorithm Agility.
[ ] Las claves se gestionan mediante KMS o HSM cuando procede.
[ ] Las claves tienen rotación.
[ ] Las claves revocadas se propagan.
[ ] Las claves públicas históricas se conservan.
[ ] Existe proceso ante Key Compromise.
[ ] Las Definitions se vinculan con source commit.
[ ] Las Definitions se vinculan con build.
[ ] Las Definitions se vinculan con Artifact digest.
[ ] Los Artifacts críticos tienen Attestation.
[ ] Existe SBOM.
[ ] El SBOM corresponde al Artifact.
[ ] Existe Vulnerability Policy.
[ ] Las excepciones de vulnerabilidad expiran.
[ ] Runtime Artifact coincide con Artifact aprobado.
[ ] Los Endpoints proceden de fuente autorizada.
[ ] Existe Endpoint Allowlist.
[ ] Existe protección frente a Endpoint Poisoning.
[ ] Existe protección SSRF en Health Checks.
[ ] Los Callbacks se autentican.
[ ] Los Events se validan.
[ ] Las Caches preservan Tenant Isolation.
[ ] Los cambios de seguridad invalidan caches.
[ ] Los Snapshots aplican rollback protection.
[ ] Los Backups están cifrados.
[ ] Los Registry Nodes ejecutan software aprobado.
[ ] El Node Join está autenticado.
[ ] Existe Security Quarantine.
[ ] Security Quarantine prevalece sobre Routing.
[ ] La liberación requiere revisión.
[ ] Existe Threat Model.
[ ] Existen Security Events.
[ ] Existen Detection Rules.
[ ] Existen Security Alerts.
[ ] Existe Incident Response.
[ ] Existen Runbooks de seguridad.
[ ] Se preserva evidencia forense.
[ ] Existe Compliance Profile.
[ ] Existen Access Reviews.
[ ] Existen Provider Reviews.
[ ] Existe retention de auditoría.
[ ] El Audit Store es append-only.
[ ] Los accesos al Audit Store están restringidos.
[ ] Existen Security SLIs.
[ ] Existen Security SLOs.
[ ] Los diagnósticos están estructurados.
[ ] El Quality Gate de Identity ha pasado.
[ ] El Quality Gate de Authorization ha pasado.
[ ] El Quality Gate de Trust ha pasado.
[ ] El Quality Gate de Secrets ha pasado.
[ ] El Quality Gate de Certificates ha pasado.
[ ] El Quality Gate de Crypto Integrity ha pasado.
[ ] El Quality Gate de Supply Chain ha pasado.
[ ] El Quality Gate de Endpoint Security ha pasado.
[ ] El Quality Gate de Audit ha pasado.
[ ] El Quality Gate de Incident Response ha pasado.
[ ] El Quality Gate de Compliance ha pasado.
```

---

# Arquitectura final de la Parte VII

```text
Principal
        ↓
Identity Verification
        ↓
Authentication
        ↓
RBAC and ABAC
        ↓
Tenant · Environment · Region Scope
        ↓
Trust and Classification Enforcement
        ↓
Policy Decision
        ↓
Manifest · Artifact · Endpoint Verification
        ↓
Secret Reference and mTLS
        ↓
Authorized Registry Operation
        ↓
Signed Journal and Audit Record
        ↓
Threat Detection
        ↓
Quarantine or Incident Response
        ↓
Compliance Evidence
```

---

# Transición hacia la Parte VIII

Esta séptima parte ha definido:

- Registry Principals;
- User Identities;
- Service Identities;
- Workload Identities;
- Engine Instance Identities;
- Provider Identities;
- Registry Node Identities;
- Identity Federation;
- Authentication;
- Authentication Profiles;
- assurance levels;
- replay protection;
- Authorization Decisions;
- RBAC;
- ABAC;
- Resource Scopes;
- Tenant Isolation;
- Environment Isolation;
- Region Isolation;
- Trust Level Enforcement;
- Provider Trust;
- Data Classification;
- Data Residency;
- Registration Authorization;
- Discovery Authorization;
- Routing Authorization;
- Administrative Authorization;
- Approval Workflows;
- Separation of Duties;
- Four-Eyes Principle;
- Break-Glass Access;
- Secret References;
- Credential Profiles;
- Secret Rotation;
- mTLS;
- Certificate Lifecycle;
- Certificate Revocation;
- Manifest Signing;
- Snapshot Signing;
- Journal Integrity;
- Event Signing;
- Cryptographic Profiles;
- Key Management;
- Key Rotation;
- Key Compromise;
- Supply Chain Security;
- Build Provenance;
- Artifact Attestations;
- SBOM;
- Vulnerability Policies;
- Runtime Verification;
- Endpoint Security;
- Endpoint Poisoning Protection;
- Callback Security;
- Event Security;
- Cache Security;
- Snapshot Security;
- Backup Security;
- Registry Node Security;
- Security Quarantine;
- Threat Model;
- Security Events;
- Security Logging;
- Audit Trails;
- Security Monitoring;
- Detection Rules;
- Security Alerts;
- Incident Response;
- Forensics;
- Compliance Profiles;
- Compliance Evidence;
- Access Reviews;
- Provider Reviews;
- Security Metrics;
- Security SLIs y SLOs;
- diagnósticos;
- Quality Gates;
- casos de uso;
- antipatrones;
- reglas de conformidad.

La Parte VIII cerrará `ESPECIFICACION_DEL_ENGINE_REGISTRY.md` mediante:

- observabilidad integral;
- métricas y tracing;
- SLIs, SLOs y SLAs;
- testing unitario;
- Contract Testing;
- Integration Testing;
- Compatibility Testing;
- Registry Simulation;
- Routing Simulation;
- Failure Injection;
- Chaos Engineering;
- Performance Testing;
- Benchmarking;
- Capacity Testing;
- Security Testing;
- Compliance Testing;
- Migration Testing;
- Disaster Recovery Testing;
- modelo de madurez;
- roadmap de implementación;
- arquitectura global final;
- Quality Gates consolidados;
- conformidad completa;
- checklist global;
- cierre y estado final del documento.

---

# Conclusión

La seguridad del Engine Registry determina si el ecosistema de Engines puede considerarse confiable.

Su ciclo puede resumirse así:

```text
Identificar Principal
        ↓
Autenticar
        ↓
Autorizar
        ↓
Aplicar Trust y Scope
        ↓
Verificar integridad
        ↓
Validar Supply Chain
        ↓
Ejecutar operación
        ↓
Auditar
        ↓
Detectar amenazas
        ↓
Contener incidentes
```

La Identity demuestra quién realiza una operación.

La Authentication valida esa identidad.

RBAC concede capacidades generales.

ABAC limita su uso según contexto.

Tenant Isolation impide cruces indebidos.

Environment Isolation separa los ciclos de vida.

Trust Level limita qué datos puede procesar un Engine.

Provider Trust gobierna terceros.

Los Secret References mantienen credenciales fuera del Registry.

mTLS protege la comunicación interna.

Los certificados vinculan workloads e identidades.

Las firmas protegen Manifests y Snapshots.

Los fingerprints detectan alteraciones.

El Journal preserva integridad histórica.

El KMS protege claves.

Las Attestations vinculan software y despliegue.

El SBOM permite conocer componentes.

La Vulnerability Policy bloquea builds inseguros.

Runtime Verification confirma qué Artifact se ejecuta.

Endpoint Security evita redirecciones maliciosas.

Security Quarantine detiene recursos comprometidos.

Audit conserva evidencia.

Threat Detection identifica anomalías.

Incident Response contiene y recupera.

Compliance transforma controles en evidencia verificable.

Un Engine Registry seguro deberá poder responder:

```text
¿Quién realizó esta operación?

¿Cómo se autenticó?

¿Qué permisos poseía?

¿Qué Policy autorizó la acción?

¿A qué tenant, entorno y región estaba limitado?

¿Qué Trust Level tenía el Engine?

¿Qué clasificación podía procesar?

¿Quién aprobó el cambio?

¿Qué Manifest se verificó?

¿Qué firma lo protegía?

¿Qué Artifact se desplegó?

¿Qué build lo produjo?

¿Qué SBOM posee?

¿Qué vulnerabilidades se aceptaron?

¿Qué certificado utilizó la Instance?

¿Qué Endpoint se autorizó?

¿Qué Secret Reference se utilizó?

¿Qué clave firmó el Snapshot?

¿Se ha revocado alguna credencial?

¿Existe una Quarantine activa?

¿Qué evento de seguridad se produjo?

¿Qué evidencia conserva la auditoría?

¿Qué controles de compliance se han superado?
```

Con esta séptima parte queda formalizado el modelo de seguridad, identidad, confianza, integridad criptográfica, supply chain, auditoría, detección y respuesta ante incidentes del **Engine Registry de NovaCoquinaria**.

La octava y última parte cerrará la especificación mediante observabilidad, testing, simulación, Chaos Engineering, benchmarking, madurez, roadmap y conformidad final.

---

# Parte VIII — Observabilidad, Testing, Simulación, Chaos Engineering, Benchmarking, Madurez, Roadmap y Conformidad Final del Engine Registry

---

# Introducción

Las siete partes anteriores han definido el Engine Registry desde los planos:

- conceptual;
- funcional;
- operacional;
- distribuido;
- de routing;
- de resiliencia;
- de seguridad.

Sin embargo, un Registry correctamente diseñado no garantiza por sí mismo un funcionamiento correcto durante años.

Para ello resulta imprescindible definir:

- cómo observarlo;
- cómo medirlo;
- cómo probarlo;
- cómo validarlo;
- cómo simularlo;
- cómo hacerlo evolucionar;
- cómo certificar su conformidad.

Esta última parte formaliza dicho plano de gobierno continuo.

---

# Objetivos

Esta parte persigue:

- definir Observabilidad Integral;
- formalizar métricas;
- establecer SLIs;
- definir SLOs;
- formalizar SLAs;
- establecer Logging;
- definir Distributed Tracing;
- formalizar Correlation;
- establecer Dashboards;
- definir Alerting;
- formalizar Testing;
- establecer Contract Testing;
- definir Integration Testing;
- formalizar Compatibility Testing;
- establecer Registry Simulation;
- definir Routing Simulation;
- formalizar Failure Injection;
- establecer Chaos Engineering;
- definir Performance Testing;
- formalizar Capacity Planning;
- establecer Benchmarking;
- definir Security Testing;
- formalizar Disaster Recovery Testing;
- establecer Compliance Testing;
- definir Madurez;
- formalizar Evolución;
- establecer Roadmap;
- definir Checklist Final;
- formalizar Conformidad Global.

---

# Principios

## Todo debe poder observarse

No deberán existir decisiones invisibles.

---

## Todo debe poder medirse

Todo comportamiento importante deberá disponer de métricas.

---

## Todo debe poder reproducirse

Toda incidencia deberá reconstruirse.

---

## Todo debe poder probarse

Las políticas deberán validarse antes de producción.

---

## Todo cambio deberá medirse

No deberá desplegarse una modificación sin evidencias.

---

## Calidad continua

La conformidad no será un estado puntual sino permanente.

---

# Arquitectura conceptual

```text
Registry

↓

Metrics

↓

Logs

↓

Traces

↓

Dashboards

↓

Alerts

↓

Testing

↓

Simulation

↓

Chaos

↓

Benchmark

↓

Quality Gates

↓

Continuous Improvement
```

---

# Observabilidad

La observabilidad deberá abarcar:

- Registry;
- Discovery;
- Matching;
- Routing;
- Health;
- Security;
- Replication;
- Cache;
- Journal;
- Snapshots.

---

# Tres pilares

```text
Metrics

Logs

Traces
```

---

# Metrics

Toda métrica deberá ser:

- consistente;
- versionada;
- documentada;
- etiquetable.

---

# Métricas del Registry

Inicialmente:

- Definitions;
- Instances;
- Providers;
- Routes;
- Policies;
- Contracts;
- Leases;
- Heartbeats.

---

# Métricas operacionales

- Requests;
- Throughput;
- Latency;
- Availability;
- Errors.

---

# Métricas de Discovery

- búsquedas;
- tiempo medio;
- filtros;
- candidatos.

---

# Métricas de Matching

- candidatos;
- score;
- descartes.

---

# Métricas de Routing

- retries;
- failovers;
- hedges;
- circuit opens.

---

# Métricas de Replicación

- replication lag;
- sync duration;
- conflicts.

---

# Métricas de Caché

- hit ratio;
- misses;
- invalidations.

---

# Métricas de Seguridad

- autenticaciones;
- autorizaciones;
- firmas;
- cuarentenas.

---

# Logging

Todos los componentes deberán emitir logs estructurados.

---

# Log mínimo

```yaml
timestamp:
component:
operation:
correlation_id:
duration:
result:
```

---

# No incluir

- secretos;
- tokens;
- claves privadas.

---

# Distributed Tracing

Cada operación deberá disponer de Trace.

---

# Trace mínimo

```text
Trace

↓

Discovery

↓

Matching

↓

Routing

↓

Execution
```

---

# Correlation ID

Toda petición deberá poseer:

```text
CORR-XXXXXX
```

---

# Dashboards

Inicialmente:

- Registry;
- Health;
- Routing;
- Discovery;
- Replication;
- Security.

---

# Alerting

Alertas sobre:

- latencia;
- errores;
- disponibilidad;
- seguridad;
- replicación.

---

# SLIs

Ejemplos:

```text
Availability

Latency

Success Rate

Replication Lag
```

---

# SLOs

Ejemplos:

```text
Availability ≥ 99.95%

Discovery <150 ms

Routing <30 ms

Replication Lag <10 s
```

---

# SLAs

Podrán derivarse de SLOs.

---

# Testing

Todo componente deberá disponer de pruebas.

---

# Pirámide

```text
Unit

↓

Contract

↓

Integration

↓

System

↓

Simulation
```

---

# Unit Testing

Valida componentes aislados.

---

# Contract Testing

Valida contratos.

---

# Integration Testing

Valida colaboración.

---

# Compatibility Testing

Comprueba compatibilidad entre versiones.

---

# Regression Testing

Evita reintroducción de errores.

---

# Performance Testing

Evalúa:

- latencia;
- throughput;
- concurrencia.

---

# Capacity Testing

Evalúa:

- escalabilidad;
- límites;
- saturación.

---

# Load Testing

Carga sostenida.

---

# Stress Testing

Carga extrema.

---

# Spike Testing

Picos bruscos.

---

# Endurance Testing

Ejecuciones prolongadas.

---

# Security Testing

Incluye:

- autenticación;
- autorización;
- firmas;
- endpoints;
- supply chain.

---

# Chaos Engineering

Introduce fallos controlados.

---

# Escenarios

- caída nodo;
- pérdida región;
- cache corrupta;
- Journal inaccesible;
- Provider caído.

---

# Failure Injection

Permite simular:

- timeout;
- latencia;
- errores;
- corrupción.

---

# Registry Simulation

Simula:

- altas;
- bajas;
- heartbeats;
- failover.

---

# Routing Simulation

Simula:

- weighted;
- sticky;
- canary;
- shadow;
- hedging.

---

# Discovery Simulation

Evalúa búsquedas masivas.

---

# Security Simulation

Simula:

- credencial revocada;
- certificado expirado;
- Provider comprometido.

---

# Disaster Recovery Testing

Valida:

- restore;
- bootstrap;
- snapshots;
- backups.

---

# Compliance Testing

Comprueba:

- evidencias;
- auditoría;
- políticas.

---

# Benchmarking

Permite comparar versiones.

---

# Indicadores

- throughput;
- latencia;
- memoria;
- CPU.

---

# Benchmark Contract

```yaml
benchmark:
  version: 2.1.0

  throughput:
    requests_per_second: 4800

  latency:
    p95: 28
```

---

# Capacity Planning

Debe proyectar crecimiento.

---

# Horizonte

```text
6 meses

12 meses

24 meses
```

---

# Escalabilidad

Se medirá:

- vertical;
- horizontal.

---

# Madurez

Modelo recomendado:

```text
Level 0

Level 1

Level 2

Level 3

Level 4

Level 5
```

---

# Level 0

Registry manual.

---

# Level 1

Discovery básico.

---

# Level 2

Routing gobernado.

---

# Level 3

Distribuido.

---

# Level 4

Seguro y observable.

---

# Level 5

Autónomo y autooptimizante.

---

# Roadmap

## Fase 1

Definitions.

---

## Fase 2

Instances.

---

## Fase 3

Discovery.

---

## Fase 4

Matching.

---

## Fase 5

Routing.

---

## Fase 6

Security.

---

## Fase 7

Distributed Registry.

---

## Fase 8

AI Optimization.

---

# KPIs

Inicialmente:

- disponibilidad;
- tiempo de registro;
- tiempo Discovery;
- tiempo Routing;
- failovers;
- incidents;
- deployments.

---

# Arquitectura final

```text
Engine Definitions
        │
        ▼
Engine Registry
        │
        ▼
Discovery
        │
        ▼
Capability Matching
        │
        ▼
Routing
        │
        ▼
Execution
        │
        ▼
Observability
        │
        ▼
Quality
        │
        ▼
Governance
```

---

# Quality Gates finales

El Registry solo será conforme cuando:

- Definitions válidas;
- Contracts válidos;
- Capabilities verificadas;
- Discovery correcto;
- Matching correcto;
- Routing correcto;
- Health correcto;
- Replication correcta;
- Security validada;
- Auditoría completa.

---

# Checklist Final

```text
✓ Definitions

✓ Providers

✓ Instances

✓ Contracts

✓ Capabilities

✓ Discovery

✓ Matching

✓ Routing

✓ Policies

✓ Health

✓ Leases

✓ Heartbeats

✓ Replication

✓ Snapshots

✓ Journal

✓ Cache

✓ Security

✓ Identity

✓ Authorization

✓ Trust

✓ Supply Chain

✓ Observability

✓ Metrics

✓ Logs

✓ Traces

✓ Dashboards

✓ Alerts

✓ Testing

✓ Chaos

✓ Simulation

✓ Performance

✓ Compliance

✓ Governance
```

---

# Estado Final del Documento

La especificación **ESPECIFICACION_DEL_ENGINE_REGISTRY.md** queda compuesta por ocho grandes bloques:

1. Fundamentos del Engine Registry.
2. Modelo de Engines, Providers e Instances.
3. Capability Matching y Discovery.
4. Routing, Load Balancing y Resilience.
5. Execution Routing avanzado.
6. Arquitectura distribuida y operación.
7. Seguridad, identidad y gobierno criptográfico.
8. Observabilidad, validación, testing y conformidad.

En conjunto define un **Engine Registry Enterprise** preparado para soportar el ecosistema completo de NovaCoquinaria.

---

# Visión global

```text
Definitions
      │
      ▼
Registry
      │
      ▼
Discovery
      │
      ▼
Capability Matching
      │
      ▼
Routing
      │
      ▼
Execution
      │
      ▼
Monitoring
      │
      ▼
Continuous Validation
      │
      ▼
Governance
      │
      ▼
Evolution
```

---

# Conclusión

El **Engine Registry** constituye el plano de control del ecosistema de ejecución de NovaCoquinaria.

Centraliza la definición de capacidades, mantiene el inventario de Engines e Instances, gobierna el descubrimiento, dirige el enrutamiento, garantiza la seguridad, preserva la integridad criptográfica y proporciona la base para una operación observable, resiliente y auditada.

Con esta octava parte se cierra la especificación completa, estableciendo un marco arquitectónico coherente para la gestión del ciclo de vida de los Engines, su operación distribuida y su evolución futura dentro de la plataforma.
