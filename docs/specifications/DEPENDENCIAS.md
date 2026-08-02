---
id: SPEC-DEPENDENCIAS
tipo: especificacion
titulo: Mapa de dependencias entre especificaciones
version: 1.0.0
estado: borrador
ultima_revision: 2026-08-02
tags:
  - specifications
  - dependencies
  - architecture
  - traceability
  - governance
---

# Mapa de dependencias entre especificaciones

---

# Parte I — Fundamentos y modelo de dependencias

---

# Introducción

La arquitectura de NovaCoquinaria está descrita mediante un conjunto de documentos de especificación especializados.

Cada documento aborda un dominio funcional concreto:

- conocimiento;
- ingesta;
- indexación;
- recuperación;
- razonamiento;
- generación;
- validación;
- orquestación;
- APIs;
- interfaces;
- ejecución.

Sin embargo, ninguno de estos documentos constituye un sistema aislado.

Cada especificación depende, en mayor o menor medida, de otras especificaciones para definir:

- conceptos;
- contratos;
- estructuras de datos;
- flujos de ejecución;
- eventos;
- estados;
- interfaces;
- restricciones.

El propósito de este documento es describir dichas dependencias de forma explícita.

No pretende duplicar contenido técnico ya definido en otros documentos.

Su función consiste en documentar:

- qué documento depende de cuál;
- qué tipo de dependencia existe;
- cuál es la dirección de dicha dependencia;
- qué impacto tendría una modificación;
- cómo debe mantenerse la coherencia arquitectónica.

---

# Objetivos

Este documento persigue los siguientes objetivos:

- identificar las dependencias entre especificaciones;
- evitar dependencias implícitas;
- reducir duplicidad documental;
- facilitar el mantenimiento;
- facilitar el análisis de impacto;
- definir niveles de acoplamiento;
- identificar documentos fundamentales;
- establecer reglas de trazabilidad;
- facilitar futuras reorganizaciones;
- apoyar la gobernanza documental.

---

# Alcance

Este documento cubre exclusivamente las relaciones entre los documentos de especificación.

No describe:

- dependencias de código;
- dependencias Maven;
- dependencias Python;
- dependencias entre módulos de implementación;
- dependencias entre repositorios.

Las dependencias descritas son exclusivamente arquitectónicas y documentales.

---

# Principios

La definición de dependencias deberá respetar los siguientes principios.

---

## Dependencias explícitas

Toda dependencia significativa deberá estar documentada.

No deberán existir dependencias críticas ocultas.

---

## Acoplamiento mínimo

Siempre que sea posible:

```text
A → B
```

será preferible a

```text
A ↔ B
```

Las dependencias bidireccionales deberán justificarse.

---

## Dirección única

Las dependencias deberán seguir una dirección clara.

Un documento consumidor no deberá redefinir conceptos pertenecientes al documento proveedor.

---

## Fuente única de verdad

Cada concepto arquitectónico deberá tener un documento propietario.

Ejemplos:

- Retrieval Plan;
- Candidate Set;
- Evidence Set;
- Prompt Template;
- RagExecution;
- Execution Context.

Cada uno deberá definirse únicamente en un documento principal.

Los demás documentos únicamente deberán referenciarlo.

---

## Reutilización

Cuando varios documentos necesiten el mismo concepto deberán reutilizar la definición existente.

No deberán aparecer definiciones incompatibles.

---

## Baja redundancia

La información repetida deberá limitarse a:

- resúmenes;
- referencias;
- contexto mínimo.

Nunca deberá mantenerse una copia completa del contenido técnico.

---

## Evolución controlada

Toda modificación importante deberá analizar previamente:

- documentos afectados;
- dependencias;
- compatibilidad;
- impacto.

---

# Conceptos básicos

---

## Documento proveedor

Es el documento que define un concepto.

Ejemplo:

```text
ESPECIFICACION_DEL_RETRIEVAL_ENGINE

define

Candidate Set
```

---

## Documento consumidor

Es el documento que utiliza dicho concepto.

Ejemplo:

```text
ESPECIFICACION_DEL_MOTOR_RAG

utiliza

Candidate Set
```

---

## Dependencia

Existe una dependencia cuando un documento necesita conceptos definidos por otro.

---

## Dependencia fuerte

Sin el documento proveedor el documento consumidor pierde coherencia.

---

## Dependencia débil

El documento consumidor puede comprenderse parcialmente sin el proveedor.

---

## Dependencia normativa

El documento proveedor establece reglas obligatorias.

Ejemplo:

```text
APIs

define

contratos
```

Los consumidores deberán respetarlos.

---

## Dependencia informativa

Solo proporciona contexto.

---

# Tipos de dependencia

Las relaciones entre especificaciones podrán clasificarse en varias categorías.

---

## Dependencia conceptual

Un documento reutiliza conceptos definidos por otro.

Ejemplo:

```text
Motor RAG

↓

Retrieval Engine
```

---

## Dependencia contractual

Un documento utiliza contratos definidos externamente.

Ejemplo:

```text
Orquestador

↓

APIs
```

---

## Dependencia funcional

Un proceso requiere otro proceso.

Ejemplo:

```text
RAG

↓

Retrieval
```

---

## Dependencia estructural

Se reutilizan estructuras de datos.

Ejemplo:

```text
Evidence Set
```

---

## Dependencia temporal

Una operación requiere otra previamente.

Ejemplo:

```text
Ingesta

↓

Indexación

↓

Retrieval
```

---

## Dependencia operacional

La ejecución depende del comportamiento de otro componente.

---

## Dependencia normativa

Una especificación define políticas obligatorias.

Ejemplo:

```text
Validación

↓

Quality Gates
```

---

## Dependencia documental

Un documento simplemente referencia otro.

---

# Intensidad de dependencia

Se utilizarán cuatro niveles.

---

## Nivel 0

Sin dependencia.

---

## Nivel 1

Referencia ocasional.

---

## Nivel 2

Dependencia funcional.

---

## Nivel 3

Dependencia crítica.

Una modificación puede invalidar el documento consumidor.

---

# Dirección de las dependencias

Todas las dependencias deberán representarse mediante:

```text
Proveedor

↓

Consumidor
```

Nunca al contrario.

---

# Dependencias permitidas

```text
Knowledge

↓

Ingesta

↓

Indexación

↓

Retrieval

↓

RAG

↓

APIs
```

---

# Dependencias no recomendadas

Ejemplo:

```text
APIs

↓

Knowledge
```

Las interfaces no deberían definir el conocimiento.

---

# Dependencias cíclicas

Siempre que sea posible deberán evitarse ciclos.

Ejemplo no deseable:

```text
A

↓

B

↓

C

↓

A
```

---

# Dependencias justificadas

Cuando un ciclo resulte inevitable deberá:

- documentarse;
- justificarse;
- mantenerse estable;
- revisarse periódicamente.

---

# Niveles arquitectónicos

Las especificaciones pueden agruparse en varios niveles.

```text
Nivel 1
Fundamentos

↓

Nivel 2
Conocimiento

↓

Nivel 3
Procesamiento

↓

Nivel 4
Ejecución

↓

Nivel 5
Interfaces

↓

Nivel 6
Gobierno
```

---

# Nivel 1 — Fundamentos

Incluye documentos base:

- Arquitectura;
- ADR;
- VISION;
- ROADMAP.

---

# Nivel 2 — Conocimiento

Describe:

- conocimiento;
- colecciones;
- ontologías;
- Knowledge Graph.

---

# Nivel 3 — Procesamiento

Describe:

- ingesta;
- indexación;
- enriquecimiento;
- embeddings.

---

# Nivel 4 — Ejecución

Describe:

- Retrieval;
- Razonador;
- Motor RAG;
- Validación;
- Orquestador.

---

# Nivel 5 — Interfaces

Describe:

- APIs;
- eventos;
- contratos.

---

# Nivel 6 — Gobierno

Describe:

- validaciones;
- Quality Gates;
- conformidad;
- trazabilidad.

---

# Tipos de consumidores

Un documento podrá actuar como:

- consumidor;
- proveedor;
- ambos.

---

# Documentos fundamentalmente proveedores

Ejemplos:

- Retrieval Engine;
- APIs;
- Knowledge Graph.

---

# Documentos principalmente consumidores

Ejemplos:

- Orquestador;
- Motor RAG.

---

# Documentos mixtos

Ejemplos:

- Validación;
- Indexing Engine.

---

# Representación gráfica

Las dependencias utilizarán la siguiente convención.

```text
A ─────► B
```

Significa:

```text
B depende de A
```

---

# Convenciones

Se utilizarán las siguientes abreviaturas.

| Abreviatura | Significado |
|-------------|-------------|
| C | Conceptual |
| F | Funcional |
| S | Estructural |
| T | Temporal |
| N | Normativa |
| D | Documental |

---

# Convención de intensidad

| Nivel | Significado |
|--------|-------------|
| 0 | Sin dependencia |
| 1 | Baja |
| 2 | Media |
| 3 | Crítica |

---

# Beneficios

La documentación explícita de dependencias permite:

- comprender la arquitectura;
- reducir inconsistencias;
- evitar duplicidades;
- facilitar cambios;
- mejorar revisiones;
- apoyar Quality Gates;
- facilitar automatización futura;
- simplificar auditorías.

---

# Lo que no pretende este documento

Este documento no pretende:

- sustituir diagramas UML;
- sustituir ADR;
- describir implementación;
- documentar clases;
- describir código fuente;
- documentar microservicios;
- describir despliegues.

Su propósito es exclusivamente representar las relaciones arquitectónicas entre las distintas especificaciones.

---

# Estado de esta parte

Con esta primera parte quedan definidos:

- el propósito del documento;
- el modelo conceptual de dependencias;
- los tipos de relación;
- los niveles de acoplamiento;
- la dirección de las dependencias;
- la organización por niveles arquitectónicos.

La siguiente parte desarrollará la matriz completa de dependencias entre todas las especificaciones de NovaCoquinaria.

---

# Transición hacia la Parte II

La Parte II definirá:

- inventario completo de especificaciones;
- matriz de dependencias;
- relaciones proveedor–consumidor;
- dependencias fuertes y débiles;
- dependencias directas e indirectas;
- análisis de impacto entre documentos;
- grafo general de dependencias arquitectónicas.

---

# Parte II — Inventario, matriz detallada y grafo de dependencias entre especificaciones

---

# Introducción

La Parte I ha definido:

- el propósito del mapa de dependencias;
- los conceptos de proveedor y consumidor;
- los tipos de dependencia;
- los niveles de intensidad;
- la dirección de las relaciones;
- los niveles arquitectónicos;
- los principios de acoplamiento y autoridad documental.

Esta Parte II aplica ese modelo al catálogo actual de especificaciones de NovaCoquinaria.

Su objetivo es representar de forma explícita:

- qué especificaciones existen;
- qué responsabilidad posee cada una;
- cuáles actúan como proveedoras;
- cuáles actúan como consumidoras;
- qué dependencias directas mantienen;
- qué dependencias indirectas pueden derivarse;
- qué relaciones presentan mayor criticidad;
- qué documentos tienen mayor impacto transversal.

---

# Inventario actual de especificaciones

El catálogo actual está compuesto por quince especificaciones distribuidas en cuatro dominios.

---

# Dominio `knowledge`

```text
ESPECIFICACION_DE_ONTOLOGIA.md
ESPECIFICACION_DE_DOCUMENTOS.md
ESPECIFICACION_DE_COMPONENTES.md
ESPECIFICACION_DE_RELACIONES.md
ESPECIFICACION_DE_COLECCIONES.md
ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md
```

---

# Dominio `ingestion`

```text
ESPECIFICACION_DE_INGESTA.md
```

---

# Dominio `runtime`

```text
ESPECIFICACION_DE_VALIDACION.md
ESPECIFICACION_DEL_INDEXING_ENGINE.md
ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md
ESPECIFICACION_DEL_RAZONADOR.md
ESPECIFICACION_DEL_MOTOR_RAG.md
ESPECIFICACION_DEL_ORQUESTADOR_DE_EJECUCION.md
ESPECIFICACION_DEL_ENGINE_REGISTRY.md
```

---

# Dominio `interfaces`

```text
ESPECIFICACION_DE_APIS.md
```

---

# Abreviaturas canónicas

Para simplificar diagramas y matrices se utilizarán las siguientes abreviaturas.

| Abreviatura | Especificación |
|---|---|
| `ONT` | Ontología |
| `DOC` | Documentos |
| `COM` | Componentes |
| `REL` | Relaciones |
| `COL` | Colecciones |
| `KG` | Knowledge Graph |
| `ING` | Ingesta |
| `VAL` | Validación |
| `IDX` | Indexing Engine |
| `RET` | Retrieval Engine |
| `REA` | Razonador |
| `RAG` | Motor RAG |
| `ORQ` | Orquestador de Ejecución |
| `REG` | Engine Registry |
| `API` | APIs |

---

# Clasificación principal de cada especificación

| Código | Dominio | Responsabilidad principal | Rol predominante |
|---|---|---|---|
| `ONT` | Knowledge | Definir vocabulario, clases y semántica | Proveedor |
| `DOC` | Knowledge | Definir la unidad documental | Proveedor |
| `COM` | Knowledge | Definir componentes reutilizables | Proveedor |
| `REL` | Knowledge | Definir vínculos semánticos | Proveedor |
| `COL` | Knowledge | Definir agrupaciones de conocimiento | Mixto |
| `KG` | Knowledge | Representar el conocimiento en grafo | Mixto |
| `ING` | Ingestion | Incorporar y normalizar conocimiento | Consumidor/proveedor |
| `VAL` | Runtime | Validar estructura, semántica y contratos | Mixto |
| `IDX` | Runtime | Crear y mantener índices | Consumidor/proveedor |
| `RET` | Runtime | Recuperar y ordenar conocimiento | Consumidor/proveedor |
| `REA` | Runtime | Aplicar reglas e inferencia | Consumidor/proveedor |
| `RAG` | Runtime | Generar respuestas fundamentadas | Consumidor |
| `ORQ` | Runtime | Coordinar ejecuciones | Consumidor/proveedor |
| `REG` | Runtime | Registrar y seleccionar Engines | Proveedor |
| `API` | Interfaces | Exponer contratos de consumo | Consumidor/proveedor contractual |

---

# Autoridad principal por concepto

| Concepto | Especificación autoritativa |
|---|---|
| Clases ontológicas | `ONT` |
| Vocabulario controlado | `ONT` |
| Documento | `DOC` |
| Front Matter documental | `DOC` |
| Componente reutilizable | `COM` |
| Relación semántica | `REL` |
| Colección | `COL` |
| Nodo y arista del grafo | `KG` |
| Snapshot del Knowledge Graph | `KG` |
| Pipeline de ingesta | `ING` |
| Regla de validación | `VAL` |
| Diagnóstico | `VAL` |
| Quality Gate de validación | `VAL` |
| Index Snapshot | `IDX` |
| Chunk indexable | `IDX` |
| Retrieval Plan | `RET` |
| Candidate Set | `RET` |
| Evidence Set | `RET` |
| Regla de inferencia | `REA` |
| Statement inferido | `REA` |
| RagQuery | `RAG` |
| RagExecution | `RAG` |
| RagContext | `RAG` |
| RagResponse | `RAG` |
| Workflow | `ORQ` |
| Job | `ORQ` |
| Step o Activity | `ORQ` |
| Engine Definition | `REG` |
| Engine Instance | `REG` |
| Capability | `REG` |
| Contrato HTTP público | `API` |
| Problem Details público | `API` |
| Webhook público | `API` |

---

# Mapa general de dependencias

```text
                           ONT
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
             DOC           COM           REL
              │             │             │
              └─────────────┼─────────────┘
                            ▼
                           COL
                            │
                            ▼
                            KG
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
             ING           VAL           REA
              │             │             │
              └──────┬──────┘             │
                     ▼                    │
                    IDX                   │
                     │                    │
                     ▼                    │
                    RET ◄─────────────────┘
                     │
                     ▼
                    RAG
                     │
                     ▼
                    API

                    REG
                     │
                     ▼
                    ORQ
                     │
          ┌──────────┼──────────┬──────────┐
          ▼          ▼          ▼          ▼
         VAL        IDX        RET        RAG
```

Este diagrama representa dependencias principales.

No muestra todas las dependencias secundarias ni transversales.

---

# Dependencias del dominio `knowledge`

---

# Ontología

La Ontología actúa como fundamento semántico del modelo de conocimiento.

---

## Dependencias de Ontología

La Ontología no debería depender de otras especificaciones funcionales.

Podrá depender documentalmente de:

- `VISION.md`;
- `ARQUITECTURA.md`;
- ADR semánticos;
- convenciones transversales.

---

## Consumidores principales

```text
ONT ─────► DOC
ONT ─────► COM
ONT ─────► REL
ONT ─────► COL
ONT ─────► KG
ONT ─────► ING
ONT ─────► VAL
ONT ─────► IDX
ONT ─────► RET
ONT ─────► REA
ONT ─────► RAG
```

---

## Intensidad

| Consumidor | Tipo | Intensidad |
|---|---|---:|
| `DOC` | Conceptual, normativa | 3 |
| `COM` | Conceptual, estructural | 3 |
| `REL` | Conceptual, normativa | 3 |
| `COL` | Conceptual | 2 |
| `KG` | Conceptual, estructural | 3 |
| `ING` | Conceptual | 2 |
| `VAL` | Normativa | 3 |
| `IDX` | Conceptual | 2 |
| `RET` | Conceptual | 2 |
| `REA` | Conceptual, normativa | 3 |
| `RAG` | Informativa | 1 |

---

# Documentos

La especificación de Documentos define la unidad documental canónica del SGCC.

---

## Proveedores

```text
ONT ─────► DOC
```

---

## Consumidores

```text
DOC ─────► COM
DOC ─────► REL
DOC ─────► COL
DOC ─────► KG
DOC ─────► ING
DOC ─────► VAL
DOC ─────► IDX
DOC ─────► RET
DOC ─────► RAG
DOC ─────► API
```

---

## Intensidad

| Consumidor | Tipo | Intensidad |
|---|---|---:|
| `COM` | Estructural | 2 |
| `REL` | Estructural | 2 |
| `COL` | Estructural | 2 |
| `KG` | Estructural | 3 |
| `ING` | Estructural, temporal | 3 |
| `VAL` | Normativa | 3 |
| `IDX` | Estructural | 3 |
| `RET` | Estructural | 2 |
| `RAG` | Documental | 1 |
| `API` | Contractual | 2 |

---

# Componentes

La especificación de Componentes define unidades reutilizables del conocimiento culinario.

---

## Proveedores

```text
ONT ─────► COM
DOC ─────► COM
```

---

## Consumidores

```text
COM ─────► REL
COM ─────► COL
COM ─────► KG
COM ─────► ING
COM ─────► VAL
COM ─────► IDX
COM ─────► RET
COM ─────► REA
COM ─────► RAG
```

---

## Intensidad

| Consumidor | Tipo | Intensidad |
|---|---|---:|
| `REL` | Conceptual | 3 |
| `COL` | Conceptual | 2 |
| `KG` | Estructural | 3 |
| `ING` | Estructural | 2 |
| `VAL` | Normativa | 3 |
| `IDX` | Estructural | 2 |
| `RET` | Conceptual | 2 |
| `REA` | Conceptual | 2 |
| `RAG` | Informativa | 1 |

---

# Relaciones

La especificación de Relaciones define los vínculos semánticos entre entidades.

---

## Proveedores

```text
ONT ─────► REL
DOC ─────► REL
COM ─────► REL
```

---

## Consumidores

```text
REL ─────► COL
REL ─────► KG
REL ─────► ING
REL ─────► VAL
REL ─────► IDX
REL ─────► RET
REL ─────► REA
REL ─────► RAG
```

---

## Intensidad

| Consumidor | Tipo | Intensidad |
|---|---|---:|
| `COL` | Conceptual | 2 |
| `KG` | Estructural, normativa | 3 |
| `ING` | Estructural | 2 |
| `VAL` | Normativa | 3 |
| `IDX` | Estructural | 2 |
| `RET` | Funcional | 3 |
| `REA` | Funcional, normativa | 3 |
| `RAG` | Informativa | 1 |

---

# Colecciones

La especificación de Colecciones define agrupaciones estáticas o dinámicas.

---

## Proveedores

```text
ONT ─────► COL
DOC ─────► COL
COM ─────► COL
REL ─────► COL
```

---

## Consumidores

```text
COL ─────► KG
COL ─────► ING
COL ─────► VAL
COL ─────► IDX
COL ─────► RET
COL ─────► RAG
COL ─────► API
```

---

## Intensidad

| Consumidor | Tipo | Intensidad |
|---|---|---:|
| `KG` | Estructural | 2 |
| `ING` | Funcional | 1 |
| `VAL` | Normativa | 2 |
| `IDX` | Funcional | 2 |
| `RET` | Funcional | 3 |
| `RAG` | Funcional | 2 |
| `API` | Contractual | 2 |

---

# Knowledge Graph

El Knowledge Graph integra Ontología, Documentos, Componentes, Relaciones y Colecciones.

---

## Proveedores

```text
ONT ─────► KG
DOC ─────► KG
COM ─────► KG
REL ─────► KG
COL ─────► KG
```

---

## Consumidores

```text
KG ─────► ING
KG ─────► VAL
KG ─────► IDX
KG ─────► RET
KG ─────► REA
KG ─────► RAG
KG ─────► API
```

---

## Intensidad

| Consumidor | Tipo | Intensidad |
|---|---|---:|
| `ING` | Funcional | 2 |
| `VAL` | Normativa | 3 |
| `IDX` | Estructural | 3 |
| `RET` | Funcional | 3 |
| `REA` | Funcional | 3 |
| `RAG` | Funcional | 2 |
| `API` | Contractual | 2 |

---

# Dependencias del dominio `ingestion`

---

# Ingesta

La Ingesta recibe conocimiento, lo normaliza y lo prepara para su incorporación al SGCC.

---

## Proveedores principales

```text
ONT ─────► ING
DOC ─────► ING
COM ─────► ING
REL ─────► ING
COL ─────► ING
KG ─────► ING
VAL ─────► ING
ORQ ─────► ING
REG ─────► ING
```

---

## Consumidores principales

```text
ING ─────► VAL
ING ─────► KG
ING ─────► IDX
ING ─────► ORQ
ING ─────► API
```

---

## Observación sobre bidireccionalidad aparente

Podrán aparecer relaciones como:

```text
KG ─────► ING
```

y:

```text
ING ─────► KG
```

Esto no deberá interpretarse como autoridad circular.

La dirección conceptual será:

- `KG` define el modelo de destino;
- `ING` produce operaciones que actualizan el grafo.

Por tanto:

```text
KG
=
proveedor de contrato
```

```text
ING
=
proveedor de datos y eventos
```

---

## Intensidad

| Proveedor | Tipo | Intensidad |
|---|---|---:|
| `ONT` | Conceptual | 2 |
| `DOC` | Estructural | 3 |
| `COM` | Estructural | 2 |
| `REL` | Estructural | 2 |
| `COL` | Funcional | 1 |
| `KG` | Contractual | 2 |
| `VAL` | Normativa | 3 |
| `ORQ` | Operacional | 2 |
| `REG` | Operacional | 1 |

---

# Dependencias del dominio `runtime`

---

# Validación

La Validación comprueba conformidad estructural, semántica y contractual.

---

## Proveedores

```text
ONT ─────► VAL
DOC ─────► VAL
COM ─────► VAL
REL ─────► VAL
COL ─────► VAL
KG ─────► VAL
ING ─────► VAL
IDX ─────► VAL
RET ─────► VAL
REA ─────► VAL
RAG ─────► VAL
ORQ ─────► VAL
REG ─────► VAL
API ─────► VAL
```

---

## Consumidores

```text
VAL ─────► ING
VAL ─────► IDX
VAL ─────► RET
VAL ─────► REA
VAL ─────► RAG
VAL ─────► ORQ
VAL ─────► REG
VAL ─────► API
```

---

## Naturaleza transversal

La Validación presenta dependencias en ambos sentidos con numerosos documentos.

Esto no implica autoridad circular si se distingue entre:

```text
contrato validado
```

y:

```text
mecanismo de validación
```

Ejemplo:

```text
RET
define
Candidate Set
```

```text
VAL
define
cómo se valida Candidate Set
```

---

## Intensidad principal

| Consumidor | Tipo | Intensidad |
|---|---|---:|
| `ING` | Normativa | 3 |
| `IDX` | Normativa | 3 |
| `RET` | Normativa | 2 |
| `REA` | Normativa | 2 |
| `RAG` | Normativa | 3 |
| `ORQ` | Normativa | 2 |
| `REG` | Normativa | 2 |
| `API` | Contractual | 2 |

---

# Indexing Engine

El Indexing Engine transforma conocimiento canónico en estructuras optimizadas para recuperación.

---

## Proveedores

```text
ONT ─────► IDX
DOC ─────► IDX
COM ─────► IDX
REL ─────► IDX
COL ─────► IDX
KG ─────► IDX
ING ─────► IDX
VAL ─────► IDX
ORQ ─────► IDX
REG ─────► IDX
```

---

## Consumidores

```text
IDX ─────► RET
IDX ─────► RAG
IDX ─────► ORQ
IDX ─────► API
IDX ─────► VAL
```

---

## Intensidad

| Consumidor | Tipo | Intensidad |
|---|---|---:|
| `RET` | Funcional, estructural | 3 |
| `RAG` | Funcional indirecta | 2 |
| `ORQ` | Operacional | 2 |
| `API` | Contractual | 1 |
| `VAL` | Normativa | 2 |

---

# Retrieval Engine

El Retrieval Engine recupera, fusiona, ordena y selecciona evidencia.

---

## Proveedores

```text
ONT ─────► RET
DOC ─────► RET
COM ─────► RET
REL ─────► RET
COL ─────► RET
KG ─────► RET
VAL ─────► RET
IDX ─────► RET
REG ─────► RET
ORQ ─────► RET
```

---

## Consumidores

```text
RET ─────► REA
RET ─────► RAG
RET ─────► ORQ
RET ─────► API
RET ─────► VAL
```

---

## Contratos principales provistos

```text
Retrieval Query
Retrieval Plan
Retrieval Execution
Candidate Record
Candidate Set
Evidence Record
Evidence Set
Retrieval Result
Retrieval Explanation
```

---

## Intensidad

| Consumidor | Tipo | Intensidad |
|---|---|---:|
| `REA` | Funcional | 2 |
| `RAG` | Funcional, estructural | 3 |
| `ORQ` | Operacional | 2 |
| `API` | Contractual | 3 |
| `VAL` | Normativa | 2 |

---

# Razonador

El Razonador aplica reglas, restricciones e inferencia sobre conocimiento trazable.

---

## Proveedores

```text
ONT ─────► REA
COM ─────► REA
REL ─────► REA
KG ─────► REA
VAL ─────► REA
RET ─────► REA
REG ─────► REA
ORQ ─────► REA
```

---

## Consumidores

```text
REA ─────► RAG
REA ─────► ORQ
REA ─────► API
REA ─────► VAL
```

---

## Intensidad

| Consumidor | Tipo | Intensidad |
|---|---|---:|
| `RAG` | Funcional | 2 |
| `ORQ` | Operacional | 2 |
| `API` | Contractual | 2 |
| `VAL` | Normativa | 2 |

---

# Motor RAG

El Motor RAG transforma evidencia y contexto en respuestas fundamentadas.

---

## Proveedores

```text
DOC ─────► RAG
COM ─────► RAG
REL ─────► RAG
COL ─────► RAG
KG ─────► RAG
VAL ─────► RAG
IDX ─────► RAG
RET ─────► RAG
REA ─────► RAG
REG ─────► RAG
ORQ ─────► RAG
```

---

## Consumidores

```text
RAG ─────► API
RAG ─────► ORQ
RAG ─────► VAL
```

---

## Contratos principales provistos

```text
RagQuery
RagExecution
Evidence Set Reference
RagContext
Prompt Assembly
Claim
Citation
Grounding Report
RagResponse
Conversation
Session
Turn
Memory Item
```

---

## Intensidad

| Consumidor | Tipo | Intensidad |
|---|---|---:|
| `API` | Contractual | 3 |
| `ORQ` | Operacional | 2 |
| `VAL` | Normativa | 3 |

---

# Engine Registry

El Engine Registry registra Engines, Capabilities, Contracts e instancias disponibles.

---

## Proveedores conceptuales

```text
VAL ─────► REG
API ─────► REG
```

La especificación de APIs podrá definir contratos de exposición.

La especificación de Validación podrá definir reglas de conformidad.

---

## Consumidores

```text
REG ─────► ING
REG ─────► IDX
REG ─────► RET
REG ─────► REA
REG ─────► RAG
REG ─────► ORQ
REG ─────► API
```

---

## Contratos principales provistos

```text
Engine Definition
Engine Instance
Provider
Capability
Operation
Engine Contract
Health
Availability
Matching
Routing Candidate
```

---

## Intensidad

| Consumidor | Tipo | Intensidad |
|---|---|---:|
| `ING` | Operacional | 1 |
| `IDX` | Operacional | 2 |
| `RET` | Operacional | 2 |
| `REA` | Operacional | 2 |
| `RAG` | Operacional | 3 |
| `ORQ` | Operacional, contractual | 3 |
| `API` | Contractual | 2 |

---

# Orquestador de Ejecución

El Orquestador coordina Workflows, Jobs, Activities, retries, señales y compensaciones.

---

## Proveedores

```text
VAL ─────► ORQ
REG ─────► ORQ
API ─────► ORQ
```

Además, el Orquestador consume contratos de los Engines que coordina:

```text
ING ─────► ORQ
IDX ─────► ORQ
RET ─────► ORQ
REA ─────► ORQ
RAG ─────► ORQ
```

---

## Consumidores

```text
ORQ ─────► ING
ORQ ─────► VAL
ORQ ─────► IDX
ORQ ─────► RET
ORQ ─────► REA
ORQ ─────► RAG
ORQ ─────► API
```

---

## Explicación de la colaboración bidireccional

El Orquestador:

- consume contratos de Engines;
- inicia ejecuciones;
- controla estados;
- recibe resultados.

Los Engines:

- reciben Execution Context;
- ejecutan Activities;
- devuelven resultados;
- publican eventos.

Esta colaboración deberá modelarse mediante contratos, no mediante redefinición mutua.

---

## Intensidad

| Relación | Tipo | Intensidad |
|---|---|---:|
| `REG ─► ORQ` | Operacional | 3 |
| `ING ─► ORQ` | Contractual | 2 |
| `IDX ─► ORQ` | Contractual | 2 |
| `RET ─► ORQ` | Contractual | 2 |
| `REA ─► ORQ` | Contractual | 2 |
| `RAG ─► ORQ` | Contractual | 2 |
| `ORQ ─► API` | Contractual | 3 |

---

# Dependencias del dominio `interfaces`

---

# APIs

La especificación de APIs expone capacidades mediante contratos estables.

---

## Proveedores funcionales

```text
DOC ─────► API
COL ─────► API
KG ─────► API
ING ─────► API
VAL ─────► API
IDX ─────► API
RET ─────► API
REA ─────► API
RAG ─────► API
ORQ ─────► API
REG ─────► API
```

---

## Consumidores

Los consumidores de la especificación de APIs son principalmente externos al catálogo:

- aplicaciones web;
- aplicaciones móviles;
- agentes;
- herramientas administrativas;
- integraciones;
- SDK;
- conectores.

Dentro del catálogo, las APIs pueden actuar como proveedor contractual para:

```text
API ─────► ORQ
API ─────► REG
API ─────► VAL
```

cuando estos documentos necesiten describir:

- callbacks;
- Webhooks;
- operaciones públicas;
- Problem Details;
- versionado;
- eventos expuestos.

---

## Intensidad de dependencias principales

| Proveedor | Tipo | Intensidad |
|---|---|---:|
| `RET` | Contractual | 3 |
| `RAG` | Contractual | 3 |
| `ORQ` | Contractual | 3 |
| `REG` | Contractual | 2 |
| `VAL` | Contractual | 2 |
| `ING` | Contractual | 2 |
| `KG` | Contractual | 2 |

---

# Matriz resumida de dependencias directas

En la siguiente matriz:

```text
3
=
dependencia crítica
```

```text
2
=
dependencia media
```

```text
1
=
dependencia baja
```

```text
—
=
sin dependencia directa relevante
```

La fila representa el proveedor.

La columna representa el consumidor.

| Proveedor ↓ / Consumidor → | ONT | DOC | COM | REL | COL | KG | ING | VAL | IDX | RET | REA | RAG | ORQ | REG | API |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ONT` | — | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 1 | — | — | — |
| `DOC` | — | — | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | — | — | 2 |
| `COM` | — | — | — | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 1 | — | — | 1 |
| `REL` | — | — | — | — | 2 | 3 | 2 | 3 | 2 | 3 | 3 | 1 | — | — | 1 |
| `COL` | — | — | — | — | — | 2 | 1 | 2 | 2 | 3 | 1 | 2 | — | — | 2 |
| `KG` | — | — | — | — | — | — | 2 | 3 | 3 | 3 | 3 | 2 | — | — | 2 |
| `ING` | — | — | — | — | — | 2 | — | 2 | 3 | — | — | — | 2 | — | 2 |
| `VAL` | — | — | — | — | — | — | 3 | — | 3 | 2 | 2 | 3 | 2 | 2 | 2 |
| `IDX` | — | — | — | — | — | — | — | 2 | — | 3 | — | 2 | 2 | — | 1 |
| `RET` | — | — | — | — | — | — | — | 2 | — | — | 2 | 3 | 2 | — | 3 |
| `REA` | — | — | — | — | — | — | — | 2 | — | — | — | 2 | 2 | — | 2 |
| `RAG` | — | — | — | — | — | — | — | 3 | — | — | — | — | 2 | — | 3 |
| `ORQ` | — | — | — | — | — | — | 2 | 2 | 2 | 2 | 2 | 2 | — | — | 3 |
| `REG` | — | — | — | — | — | — | 1 | 2 | 2 | 2 | 2 | 3 | 3 | — | 2 |
| `API` | — | — | — | — | — | — | — | 2 | — | — | — | — | 2 | 2 | — |

---

# Dependencias directas e indirectas

---

# Dependencia directa

Existe cuando el consumidor utiliza directamente un concepto del proveedor.

Ejemplo:

```text
RET ─────► RAG
```

El Motor RAG utiliza `Evidence Set` definido por Retrieval.

---

# Dependencia indirecta

Existe cuando la relación se produce a través de otro documento.

Ejemplo:

```text
ONT ─────► KG ─────► RET ─────► RAG
```

El Motor RAG depende indirectamente de la Ontología.

---

# Importancia de las dependencias indirectas

Una modificación en un documento fundacional puede propagarse a varios niveles.

Ejemplo:

```text
Cambio en Ontología
        ↓
Cambio en Knowledge Graph
        ↓
Cambio en Indexing
        ↓
Cambio en Retrieval
        ↓
Cambio en RAG
        ↓
Cambio en APIs
```

---

# Caminos de dependencia críticos

---

## Camino de conocimiento

```text
ONT
 ↓
DOC
 ↓
COM
 ↓
REL
 ↓
KG
```

---

## Camino de incorporación

```text
DOC
 ↓
ING
 ↓
VAL
 ↓
KG
```

---

## Camino de recuperación

```text
KG
 ↓
IDX
 ↓
RET
```

---

## Camino de generación

```text
RET
 ↓
RAG
 ↓
API
```

---

## Camino de inferencia

```text
KG
 ↓
REA
 ↓
RAG
```

---

## Camino de ejecución

```text
REG
 ↓
ORQ
 ↓
RET / REA / RAG / IDX / ING
```

---

## Camino de exposición

```text
Componentes funcionales
        ↓
API
        ↓
Consumidores externos
```

---

# Dependencias críticas de nivel 3

Las dependencias de nivel 3 requieren revisión conjunta ante cambios incompatibles.

---

# Núcleo semántico

```text
ONT ─────► DOC
ONT ─────► COM
ONT ─────► REL
ONT ─────► KG
```

---

# Núcleo del grafo

```text
DOC ─────► KG
COM ─────► KG
REL ─────► KG
```

---

# Núcleo de procesamiento

```text
DOC ─────► ING
VAL ─────► ING
KG  ─────► IDX
ING ─────► IDX
VAL ─────► IDX
IDX ─────► RET
KG  ─────► RET
REL ─────► RET
```

---

# Núcleo RAG

```text
RET ─────► RAG
VAL ─────► RAG
RAG ─────► API
RET ─────► API
```

---

# Núcleo de ejecución

```text
REG ─────► ORQ
REG ─────► RAG
ORQ ─────► API
```

---

# Núcleo de validación

```text
ONT ─────► VAL
DOC ─────► VAL
COM ─────► VAL
REL ─────► VAL
KG  ─────► VAL
```

---

# Especificaciones con mayor impacto transversal

---

## Ontología

Impacto:

```text
muy alto
```

Razón:

- define significado;
- afecta al modelo completo;
- condiciona validación e inferencia.

---

## Documentos

Impacto:

```text
muy alto
```

Razón:

- define la unidad persistida;
- afecta a ingesta, validación, indexación y APIs.

---

## Knowledge Graph

Impacto:

```text
muy alto
```

Razón:

- integra el conocimiento;
- abastece Indexing, Retrieval y Reasoning.

---

## Validación

Impacto:

```text
muy alto
```

Razón:

- aplica reglas transversales;
- puede bloquear publicación y ejecución.

---

## Retrieval Engine

Impacto:

```text
alto
```

Razón:

- abastece RAG;
- define Candidate Set y Evidence Set;
- afecta a APIs.

---

## Motor RAG

Impacto:

```text
alto
```

Razón:

- concentra generación, Grounding, Citations y conversación;
- expone contratos complejos mediante APIs.

---

## Orquestador

Impacto:

```text
alto
```

Razón:

- coordina múltiples Engines;
- afecta a estados, retries y operación distribuida.

---

## Engine Registry

Impacto:

```text
alto
```

Razón:

- determina descubrimiento, matching y routing;
- condiciona Orquestador y Runtime.

---

## APIs

Impacto:

```text
alto
```

Razón:

- materializa contratos públicos;
- cualquier breaking change afecta a consumidores externos.

---

# Especificaciones con menor impacto transversal

Las especificaciones más acotadas no son menos importantes.

Simplemente poseen menor número de consumidores directos.

Ejemplos:

- Colecciones;
- Ingesta;
- Razonador.

Su impacto puede seguir siendo crítico dentro de su bounded context.

---

# Riesgo de propagación

Se recomienda clasificar los cambios según su radio de impacto.

---

## Radio 0

Cambio interno editorial.

No afecta a consumidores.

---

## Radio 1

Afecta a un único consumidor directo.

---

## Radio 2

Afecta a varios consumidores directos.

---

## Radio 3

Se propaga por varios niveles arquitectónicos.

---

## Radio 4

Afecta contratos externos o arquitectura fundacional.

---

# Ejemplos

---

## Cambio de título

```text
Radio 0
```

---

## Nuevo filtro opcional en Retrieval

```text
Radio 1 o 2
```

---

## Cambio del contrato `Evidence Set`

```text
Radio 3
```

Puede afectar:

- Motor RAG;
- Validación;
- APIs;
- Orquestador.

---

## Cambio de IDs documentales

```text
Radio 3 o 4
```

Puede afectar:

- Knowledge Graph;
- Indexing;
- Retrieval;
- enlaces;
- APIs.

---

## Cambio de ontología

```text
Radio 4
```

Puede afectar a casi todo el sistema.

---

# Relaciones potencialmente bidireccionales

Algunas colaboraciones pueden parecer bidireccionales.

Deberán dividirse por tipo de contrato.

---

# Ingesta y Knowledge Graph

```text
KG ─────► ING
```

El grafo define el modelo de destino.

```text
ING ─────► KG
```

La ingesta produce mutaciones y eventos.

---

# Validación y Runtime

```text
RET ─────► VAL
```

Retrieval define contratos validables.

```text
VAL ─────► RET
```

Validación define reglas aplicables.

---

# Orquestador y Engines

```text
Engine ─────► ORQ
```

El Engine define operaciones ejecutables.

```text
ORQ ─────► Engine
```

El Orquestador inicia y controla ejecuciones.

---

# APIs y Runtime

```text
Runtime ─────► API
```

El Runtime proporciona capacidades.

```text
API ─────► Runtime
```

La API define el contrato de invocación pública.

---

# Regla para dependencias bidireccionales

Toda relación bidireccional deberá separar:

- autoridad conceptual;
- autoridad contractual;
- flujo de datos;
- flujo de ejecución;
- feedback operativo.

---

# Dependencias documentales recomendadas

Cada especificación deberá incluir una sección final de referencias.

---

# Ontología

Debería referenciar:

- Arquitectura;
- ADR semánticos;
- Documentos;
- Componentes;
- Relaciones;
- Knowledge Graph.

---

# Documentos

Debería referenciar:

- Ontología;
- Componentes;
- Relaciones;
- Validación;
- Ingesta.

---

# Componentes

Debería referenciar:

- Ontología;
- Documentos;
- Relaciones;
- Knowledge Graph.

---

# Relaciones

Debería referenciar:

- Ontología;
- Componentes;
- Knowledge Graph;
- Razonador.

---

# Colecciones

Debería referenciar:

- Documentos;
- Componentes;
- Relaciones;
- Knowledge Graph;
- Retrieval Engine.

---

# Knowledge Graph

Debería referenciar:

- Ontología;
- Documentos;
- Componentes;
- Relaciones;
- Colecciones;
- Indexing Engine;
- Retrieval Engine;
- Razonador.

---

# Ingesta

Debería referenciar:

- Documentos;
- Componentes;
- Relaciones;
- Knowledge Graph;
- Validación;
- Indexing Engine;
- Orquestador.

---

# Validación

Debería referenciar:

- Ontología;
- Documentos;
- Relaciones;
- Knowledge Graph;
- Runtime Engines;
- APIs.

---

# Indexing Engine

Debería referenciar:

- Documentos;
- Knowledge Graph;
- Ingesta;
- Validación;
- Retrieval Engine;
- Engine Registry;
- Orquestador.

---

# Retrieval Engine

Debería referenciar:

- Knowledge Graph;
- Colecciones;
- Indexing Engine;
- Validación;
- Razonador;
- Motor RAG;
- Engine Registry;
- Orquestador;
- APIs.

---

# Razonador

Debería referenciar:

- Ontología;
- Relaciones;
- Knowledge Graph;
- Retrieval Engine;
- Motor RAG;
- Validación;
- Engine Registry;
- Orquestador.

---

# Motor RAG

Debería referenciar:

- Retrieval Engine;
- Razonador;
- Validación;
- Engine Registry;
- Orquestador;
- APIs.

---

# Orquestador

Debería referenciar:

- Engine Registry;
- Validación;
- Runtime Engines;
- APIs.

---

# Engine Registry

Debería referenciar:

- Orquestador;
- Runtime Engines;
- Validación;
- APIs.

---

# APIs

Debería referenciar:

- Ingesta;
- Knowledge Graph;
- Validación;
- Indexing Engine;
- Retrieval Engine;
- Razonador;
- Motor RAG;
- Orquestador;
- Engine Registry.

---

# Orden recomendado de revisión conjunta

Cuando se modifique una especificación se recomienda revisar grupos coherentes.

---

## Grupo semántico

```text
ONT
DOC
COM
REL
KG
```

---

## Grupo de ingesta

```text
ING
VAL
KG
IDX
```

---

## Grupo de recuperación

```text
IDX
RET
KG
COL
VAL
```

---

## Grupo de razonamiento

```text
ONT
REL
KG
REA
VAL
```

---

## Grupo RAG

```text
RET
REA
RAG
VAL
API
```

---

## Grupo de ejecución

```text
REG
ORQ
VAL
Runtime Engines
```

---

## Grupo de interfaces

```text
API
ORQ
REG
RET
RAG
VAL
```

---

# Dependencias que requieren especial vigilancia

---

## `Evidence Set`

Propietario:

```text
RET
```

Consumidores:

```text
RAG
VAL
API
ORQ
```

---

## `Execution Context`

Deberá diferenciarse según ámbito:

```text
Retrieval Execution Context
```

propiedad de `RET`.

```text
Workflow Execution Context
```

propiedad de `ORQ`.

No deberán utilizarse como sinónimos.

---

## `Snapshot`

Puede aparecer en:

- Knowledge Graph;
- Indexing;
- Retrieval;
- RAG.

Cada tipo deberá utilizar un nombre canónico:

```text
Knowledge Graph Snapshot
Index Snapshot
Retrieval Snapshot Reference
RAG Reproducibility Snapshot Set
```

---

## `Engine`

Propietario:

```text
REG
```

Los demás documentos deberán consumir su definición.

---

## `Capability`

Propietario:

```text
REG
```

No deberá redefinirse en Orquestador o APIs.

---

## `Quality Gate`

Propietario transversal:

```text
VAL
```

Cada especificación podrá declarar Gates específicos, pero el contrato común deberá pertenecer a Validación.

---

## `Problem Details`

Propietario:

```text
API
```

Los Runtime Engines podrán producir diagnósticos internos, pero la transformación HTTP pertenecerá a APIs.

---

## `Conversation`

Propietario:

```text
RAG
```

La API expone el recurso, pero no deberá redefinir su semántica interna.

---

# Resumen de la matriz

Las dependencias pueden resumirse en seis ejes principales:

```text
Semántica
ONT → DOC / COM / REL / KG
```

```text
Conocimiento
DOC / COM / REL / COL → KG
```

```text
Procesamiento
ING → VAL → IDX
```

```text
Recuperación
KG / IDX → RET
```

```text
Inteligencia
RET / REA → RAG
```

```text
Operación y exposición
REG → ORQ → API
```

---

# Estado de esta parte

Con esta segunda parte quedan definidos:

- el inventario actual de especificaciones;
- las abreviaturas;
- los roles proveedor–consumidor;
- la autoridad principal por concepto;
- el mapa general;
- las dependencias por documento;
- la matriz resumida;
- los caminos críticos;
- los radios de impacto;
- las dependencias bidireccionales;
- los grupos de revisión conjunta;
- los conceptos transversales que requieren vigilancia.

---

# Transición hacia la Parte III

La Parte III cerrará el documento mediante:

- reglas de análisis de impacto;
- gestión de cambios;
- prevención de ciclos;
- authority map;
- gobernanza;
- versionado de dependencias;
- automatización;
- validación;
- diagnósticos;
- Quality Gates;
- métricas;
- checklist;
- conformidad global;
- mantenimiento del mapa de dependencias.

---

# Parte III — Impacto, gobernanza, validación, Quality Gates y conformidad global

---

# Introducción

Las Partes I y II han definido:

- el propósito del mapa de dependencias;
- los tipos de dependencia;
- los niveles de intensidad;
- la dirección proveedor–consumidor;
- el inventario de especificaciones;
- la autoridad principal por concepto;
- la matriz de dependencias;
- los caminos críticos;
- los radios de impacto;
- las relaciones bidireccionales;
- los grupos de revisión conjunta.

Esta Parte III establece cómo deberán mantenerse y gobernarse dichas dependencias.

Su objetivo es asegurar que cualquier cambio documental o arquitectónico pueda responder de forma trazable a las siguientes preguntas:

```text
¿Qué especificación cambia?

¿Qué conceptos modifica?

¿Qué documentos dependen de ella?

¿Qué contratos se ven afectados?

¿Qué nivel de impacto tiene el cambio?

¿Qué documentos deben revisarse?

¿Es compatible?

¿Requiere ADR?

¿Qué validaciones deben ejecutarse?

¿Qué evidencia debe conservarse?
```

---

# Principios de mantenimiento

El mapa de dependencias deberá mantenerse bajo los siguientes principios.

---

## Actualización simultánea

Cuando se cree, elimine, divida, fusione o renombre una especificación, este documento deberá actualizarse en el mismo cambio.

---

## Coherencia con el repositorio

El mapa deberá reflejar siempre:

- los archivos reales;
- los nombres canónicos;
- las rutas existentes;
- las versiones vigentes;
- los estados documentales;
- los conceptos autoritativos.

---

## No inferencia silenciosa

No deberá asumirse una dependencia únicamente porque dos documentos compartan terminología.

La relación deberá justificarse mediante:

- contrato;
- flujo;
- concepto;
- estructura;
- norma;
- referencia explícita.

---

## Dependencia mínima necesaria

Solo deberán documentarse como directas las dependencias realmente necesarias.

Las dependencias transitivas no deberán duplicarse como directas salvo que exista consumo explícito.

---

## Authority before reference

Antes de añadir una referencia deberá identificarse el documento propietario del concepto.

---

## Cambio trazable

Toda modificación relevante deberá preservar:

- origen;
- motivo;
- alcance;
- impacto;
- compatibilidad;
- revisión;
- aprobación.

---

# Authority Map

El **Authority Map** identifica qué documento es propietario de cada concepto transversal.

---

# Reglas de autoridad

Un concepto será autoritativo en una única especificación.

Los demás documentos podrán:

- referenciarlo;
- resumirlo;
- especializarlo;
- restringirlo;
- mapearlo a otro contrato.

No podrán redefinirlo de forma incompatible.

---

# Authority Record

Formato recomendado:

```yaml
authority_record:
  concept: Evidence Set
  owner: ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md
  consumers:
    - ESPECIFICACION_DEL_MOTOR_RAG.md
    - ESPECIFICACION_DE_VALIDACION.md
    - ESPECIFICACION_DE_APIS.md
    - ESPECIFICACION_DEL_ORQUESTADOR_DE_EJECUCION.md
  status: active
```

---

# Conceptos con autoridad única

| Concepto | Documento propietario |
|---|---|
| Ontología | Ontología |
| Documento | Documentos |
| Componente | Componentes |
| Relación | Relaciones |
| Colección | Colecciones |
| Knowledge Graph | Knowledge Graph |
| Pipeline de Ingesta | Ingesta |
| Quality Gate | Validación |
| Diagnóstico | Validación |
| Chunk indexable | Indexing Engine |
| Index Snapshot | Indexing Engine |
| Retrieval Plan | Retrieval Engine |
| Candidate Set | Retrieval Engine |
| Evidence Set | Retrieval Engine |
| Regla de inferencia | Razonador |
| Statement inferido | Razonador |
| RagQuery | Motor RAG |
| RagExecution | Motor RAG |
| RagContext | Motor RAG |
| RagResponse | Motor RAG |
| Workflow | Orquestador |
| Job | Orquestador |
| Activity | Orquestador |
| Engine | Engine Registry |
| Capability | Engine Registry |
| Engine Instance | Engine Registry |
| HTTP Problem Details | APIs |
| Webhook público | APIs |
| API Version | APIs |

---

# Conceptos con posibles colisiones

Algunos términos pueden aparecer en varios documentos con significados distintos.

Deberán especializarse.

---

## `Execution Context`

Formas permitidas:

```text
Retrieval Execution Context
Workflow Execution Context
RAG Execution Context
Validation Execution Context
```

No deberá utilizarse únicamente:

```text
Execution Context
```

cuando exista riesgo de ambigüedad.

---

## `Snapshot`

Formas permitidas:

```text
Knowledge Graph Snapshot
Index Snapshot
Retrieval Snapshot Reference
RAG Reproducibility Snapshot Set
```

---

## `Execution`

Formas permitidas:

```text
Retrieval Execution
RagExecution
Workflow Execution
Validation Execution
Indexing Execution
```

---

## `Result`

Formas permitidas:

```text
Retrieval Result
Validation Result
Reasoning Result
RagResponse
Workflow Result
```

---

## `Context`

Formas permitidas:

```text
RagContext
Conversation Context
Execution Context
Security Context
Tenant Context
```

---

# Reglas de especialización

Cuando un documento amplíe un concepto de otro deberá declarar:

```text
base concept
owner
specialization
compatibility
```

---

# Ejemplo

```yaml
concept_specialization:
  base:
    concept: Execution Context
    owner: ESPECIFICACION_DEL_ORQUESTADOR_DE_EJECUCION.md

  specialization:
    concept: Retrieval Execution Context
    owner: ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md

  compatibility:
    mode: extension
```

---

# Análisis de impacto

Todo cambio relevante deberá someterse a análisis de impacto.

---

# Entrada mínima

```yaml
change_impact:
  source_document:
  changed_concepts:
  change_type:
  compatibility:
  direct_consumers:
  indirect_consumers:
  required_reviews:
  required_validations:
```

---

# Tipos de cambio

```text
editorial
clarification
compatible
breaking
structural
rename
deprecation
retirement
authority_transfer
```

---

# Cambio editorial

Afecta:

- ortografía;
- formato;
- enlaces;
- estilo.

Impacto habitual:

```text
Radio 0
```

---

# Aclaración

Mejora comprensión sin cambiar semántica.

Impacto habitual:

```text
Radio 0 o 1
```

---

# Cambio compatible

Añade capacidad sin romper consumidores existentes.

Ejemplos:

- campo opcional;
- estado adicional tolerable;
- nuevo endpoint;
- nueva relación compatible.

Impacto habitual:

```text
Radio 1 o 2
```

---

# Cambio incompatible

Modifica:

- significado;
- tipo;
- obligatoriedad;
- ID;
- lifecycle;
- invariantes;
- autoridad.

Impacto habitual:

```text
Radio 2 a 4
```

---

# Cambio estructural

Incluye:

- mover archivo;
- dividir especificación;
- fusionar documentos;
- reorganizar dominios;
- cambiar ownership.

Impacto habitual:

```text
Radio 2 a 4
```

---

# Renombrado

Deberá afectar:

- archivo;
- título;
- Front Matter;
- README;
- referencias;
- matriz;
- navegación;
- site build.

---

# Deprecation

Deberá declarar:

- sustitución;
- consumidores;
- fecha;
- transición;
- versión final.

---

# Retirement

Deberá conservar:

- trazabilidad;
- historial;
- redirección;
- referencias históricas.

---

# Transferencia de autoridad

Es uno de los cambios más sensibles.

Ejemplo:

```text
Evidence Set

deja de pertenecer a Retrieval

y pasa a pertenecer a RAG
```

Requiere:

- ADR;
- actualización del Authority Map;
- revisión de consumidores;
- migración;
- versionado mayor;
- validación cruzada.

---

# Procedimiento de análisis

---

## Paso 1 — Identificar el concepto

Ejemplo:

```text
Candidate Set
```

---

## Paso 2 — Identificar propietario

```text
Retrieval Engine
```

---

## Paso 3 — Identificar consumidores directos

```text
Motor RAG
Validación
APIs
Orquestador
```

---

## Paso 4 — Identificar consumidores indirectos

Ejemplo:

```text
Aplicaciones externas
```

a través de APIs.

---

## Paso 5 — Clasificar compatibilidad

```text
compatible
breaking
unknown
```

---

## Paso 6 — Determinar radio

```text
0
1
2
3
4
```

---

## Paso 7 — Seleccionar revisión conjunta

Ejemplo:

```text
Grupo RAG
```

---

## Paso 8 — Determinar validaciones

- enlaces;
- schemas;
- semántica;
- contratos;
- ejemplos;
- Quality Gates.

---

## Paso 9 — Registrar resultado

En:

- PR;
- changelog;
- ADR;
- BITACORA cuando sea hito;
- este mapa si cambia la relación.

---

# Matriz de impacto por documento

| Documento modificado | Revisión mínima recomendada |
|---|---|
| Ontología | Documentos, Componentes, Relaciones, KG, Validación, Razonador |
| Documentos | Componentes, Relaciones, KG, Ingesta, Validación, Indexing |
| Componentes | Relaciones, Colecciones, KG, Validación |
| Relaciones | Colecciones, KG, Retrieval, Razonador |
| Colecciones | KG, Indexing, Retrieval, APIs |
| Knowledge Graph | Ingesta, Validación, Indexing, Retrieval, Razonador |
| Ingesta | Validación, KG, Indexing, Orquestador, APIs |
| Validación | Todos los Engines consumidores |
| Indexing Engine | Retrieval, Validación, Orquestador |
| Retrieval Engine | RAG, Razonador, Validación, Orquestador, APIs |
| Razonador | RAG, Validación, Orquestador, APIs |
| Motor RAG | Validación, Orquestador, APIs |
| Orquestador | Registry, Runtime Engines, APIs |
| Engine Registry | Orquestador, Runtime Engines, APIs |
| APIs | Consumidores externos, Orquestador, Registry, Validación |

---

# Cambios que requieren ADR

Deberá considerarse ADR cuando el cambio:

- altera un bounded context;
- mueve autoridad conceptual;
- introduce un nuevo dominio;
- crea dependencia bidireccional;
- elimina una dependencia crítica;
- cambia estrategia de integración;
- redefine el papel de un Engine;
- fusiona especificaciones;
- divide una especificación fundacional;
- introduce contratos transversales nuevos;
- cambia semántica de snapshots;
- cambia modelo de ejecución;
- modifica estrategia de consistencia.

---

# Cambios que normalmente no requieren ADR

- corrección de erratas;
- actualización de enlaces;
- Front Matter;
- ejemplos;
- aclaraciones;
- reorganización interna sin cambio semántico;
- etiquetas;
- índice.

---

# Prevención de ciclos

Las dependencias cíclicas deberán detectarse y clasificarse.

---

# Ciclo de autoridad

Ejemplo no permitido:

```text
A define X según B
B define X según A
```

Resultado:

```text
authority_cycle
```

---

# Ciclo contractual

Puede existir si se separan contratos.

Ejemplo:

```text
ORQ consume Engine Contract
Engine consume Workflow Context
```

No existe ciclo de autoridad si cada contrato tiene propietario claro.

---

# Ciclo operacional

Puede existir durante ejecución.

Ejemplo:

```text
Orquestador inicia Engine
Engine publica evento
Orquestador procesa evento
```

Es válido si está modelado.

---

# Ciclo documental

Ejemplo:

```text
A referencia B
B referencia A
```

Puede ser válido si no existe definición circular.

---

# Clasificación de ciclos

```text
authority
contractual
operational
documental
data
```

---

# Política

| Tipo | Política |
|---|---|
| Authority | Prohibido |
| Contractual | Permitido con ownership |
| Operational | Permitido si está modelado |
| Documental | Permitido con moderación |
| Data | Permitido si se controla consistencia |

---

# Detección automática

La validación podrá construir un grafo:

```text
document_id
relationship_type
target_document_id
```

y detectar:

- ciclos;
- huérfanos;
- dependencias inexistentes;
- authority conflicts;
- rutas excesivas.

---

# Dependencias huérfanas

Una dependencia es huérfana cuando:

- referencia un archivo inexistente;
- referencia un concepto sin owner;
- utiliza un ID retirado;
- depende de una especificación deprecated sin sustitución.

---

# Diagnósticos recomendados

```text
SPEC_DEPENDENCY_TARGET_MISSING
SPEC_DEPENDENCY_TYPE_INVALID
SPEC_DEPENDENCY_INTENSITY_INVALID
SPEC_DEPENDENCY_DIRECTION_INVALID
SPEC_DEPENDENCY_UNDECLARED
SPEC_DEPENDENCY_STALE
SPEC_DEPENDENCY_CYCLE
SPEC_AUTHORITY_CONFLICT
SPEC_AUTHORITY_MISSING
SPEC_AUTHORITY_CYCLE
SPEC_CONCEPT_DUPLICATED
SPEC_CONSUMER_UNDECLARED
SPEC_PROVIDER_UNDECLARED
SPEC_DEPRECATED_PROVIDER_IN_USE
SPEC_DEPENDENCY_MATRIX_INCONSISTENT
SPEC_DEPENDENCY_README_MISMATCH
```

---

# Diagnostic Contract

```yaml
specification_dependency_diagnostic:
  id: SPEC-DEP-DIAG-000041
  code: SPEC_AUTHORITY_CONFLICT
  severity: error

  concept:
    name: Evidence Set

  owners:
    - ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md
    - ESPECIFICACION_DEL_MOTOR_RAG.md

  message:
    El concepto posee más de un documento autoritativo.

  retryable: false
```

---

# Versionado de dependencias

Las relaciones podrán versionarse cuando sean contractuales.

---

# Dependency Record

```yaml
dependency:
  id: SPEC-DEP-RET-RAG-0001

  provider:
    document: SPEC-RETRIEVAL-ENGINE
    version: 1.0.0

  consumer:
    document: SPEC-MOTOR-RAG
    version: 1.0.0

  concepts:
    - Evidence Set
    - Retrieval Result

  type:
    - functional
    - structural

  intensity: 3
  status: active
```

---

# Estados de dependencia

```text
proposed
active
deprecated
superseded
retired
```

---

# Compatibilidad de versiones

Una dependencia podrá declarar:

```text
exact
compatible_major
compatible_minor
range
```

---

# Ejemplo

```yaml
compatibility:
  provider_versions: ">=1.2.0 <2.0.0"
```

---

# No versionar en exceso

No todas las referencias documentales necesitan un contrato versionado.

Se reservará para:

- contratos estructurales;
- schemas;
- APIs;
- eventos;
- conceptos compartidos críticos.

---

# Gobernanza de cambios

---

# Owner del documento

El owner del documento proveedor deberá:

- evaluar cambios;
- identificar consumidores;
- actualizar autoridad;
- coordinar revisiones;
- comunicar breaking changes.

---

# Owner consumidor

Deberá:

- validar compatibilidad;
- adaptar referencias;
- actualizar ejemplos;
- confirmar migración.

---

# Architecture Review

Será necesaria cuando:

- radio ≥ 3;
- dependencia crítica cambia;
- aparece ciclo;
- cambia autoridad;
- se introduce nuevo dominio;
- se modifica un contrato transversal.

---

# Pull Request

Toda PR relevante debería incluir:

```text
Documentos modificados
Conceptos modificados
Dependencias afectadas
Radio de impacto
Compatibilidad
Validaciones ejecutadas
ADR relacionado
Migración necesaria
```

---

# Plantilla de impacto

```markdown
## Impacto en especificaciones

- Documento origen:
- Conceptos afectados:
- Dependencias directas:
- Dependencias indirectas:
- Compatibilidad:
- Radio:
- Revisión conjunta:
- ADR:
- Migración:
- Validaciones:
```

---

# Automatización

El mapa podrá integrarse con herramientas del proyecto.

---

# `validate_all.py`

Podrá comprobar:

- existencia del documento;
- Front Matter;
- ID;
- enlaces;
- referencias.

---

# `validate_semantics.py`

Podrá comprobar:

- tipos de dependencia;
- autoridad;
- duplicidad;
- ciclos;
- owner;
- estados.

---

# `generate_graph.py`

Podrá producir:

- grafo de especificaciones;
- matriz;
- nodos centrales;
- ciclos;
- huérfanos;
- caminos críticos.

---

# `build_site_docs.py`

Podrá incluir:

- navegación;
- mapas;
- tablas;
- enlaces;
- authority map.

---

# Modelo de datos sugerido

```yaml
specification_dependency:
  id:
  provider:
  consumer:
  concepts:
  types:
  intensity:
  compatibility:
  status:
  rationale:
```

---

# Ejemplo

```yaml
specification_dependency:
  id: SPEC-DEP-IDX-RET-0001

  provider:
    id: SPEC-INDEXING-ENGINE

  consumer:
    id: SPEC-RETRIEVAL-ENGINE

  concepts:
    - Index Snapshot
    - Search Index
    - Chunk Representation

  types:
    - functional
    - structural

  intensity: 3
  compatibility: compatible_major
  status: active
```

---

# Validación estructural

Deberá comprobar:

- ID único;
- provider existente;
- consumer existente;
- tipos válidos;
- intensidad válida;
- estado válido;
- concepto no vacío.

---

# Validación semántica

Deberá comprobar:

- dirección correcta;
- owner coherente;
- dependencia justificada;
- ausencia de duplicados;
- compatibilidad;
- ciclo permitido.

---

# Validación de matriz

La matriz deberá coincidir con los registros individuales.

---

# Validación de README

El catálogo de `README.md` deberá coincidir con:

- inventario;
- dominios;
- número de especificaciones;
- rutas.

---

# Quality Gate de catálogo

```yaml
quality_gate:
  id: QG-SPEC-DEPENDENCY-CATALOG-0001

  criteria:
    all:
      - all_specifications_registered == true
      - document_ids_unique == true
      - document_paths_valid == true
      - domains_valid == true
      - authority_map_complete == true
```

---

# Quality Gate de dependencias

```yaml
quality_gate:
  id: QG-SPEC-DEPENDENCIES-0001

  criteria:
    all:
      - providers_exist == true
      - consumers_exist == true
      - dependency_types_valid == true
      - dependency_intensities_valid == true
      - critical_dependencies_documented == true
      - duplicate_dependencies_absent == true
      - stale_dependencies_absent == true
```

---

# Quality Gate de autoridad

```yaml
quality_gate:
  id: QG-SPEC-AUTHORITY-0001

  criteria:
    all:
      - concepts_have_single_owner == true
      - authority_cycles_absent == true
      - authority_conflicts_absent == true
      - specializations_declared == true
      - deprecated_owners_replaced == true
```

---

# Quality Gate de ciclos

```yaml
quality_gate:
  id: QG-SPEC-DEPENDENCY-CYCLES-0001

  criteria:
    all:
      - authority_cycles_absent == true
      - operational_cycles_classified == true
      - contractual_cycles_owned == true
      - documentary_cycles_non_blocking == true
      - unknown_cycles_absent == true
```

---

# Quality Gate de impacto

```yaml
quality_gate:
  id: QG-SPEC-CHANGE-IMPACT-0001

  criteria:
    all:
      - changed_concepts_identified == true
      - direct_consumers_identified == true
      - indirect_consumers_evaluated == true
      - compatibility_classified == true
      - impact_radius_assigned == true
      - required_reviews_completed == true
      - migrations_declared == true
```

---

# Quality Gate de compatibilidad

```yaml
quality_gate:
  id: QG-SPEC-DEPENDENCY-COMPATIBILITY-0001

  criteria:
    all:
      - provider_version_valid == true
      - consumer_version_valid == true
      - version_range_valid == true
      - breaking_changes_declared == true
      - migration_path_available == true
      - deprecated_contracts_not_used_without_plan == true
```

---

# Quality Gate de automatización

```yaml
quality_gate:
  id: QG-SPEC-DEPENDENCY-AUTOMATION-0001

  criteria:
    all:
      - dependency_graph_generated == true
      - dependency_matrix_generated == true
      - cycles_checked == true
      - orphans_checked == true
      - authority_conflicts_checked == true
      - validation_report_stored == true
```

---

# Quality Gate global

```yaml
quality_gate:
  id: QG-SPEC-DEPENDENCIES-GLOBAL-0001

  criteria:
    all:
      - catalog_gate_passed == true
      - dependencies_gate_passed == true
      - authority_gate_passed == true
      - cycles_gate_passed == true
      - impact_gate_passed == true
      - compatibility_gate_passed == true
      - automation_gate_passed == true
```

---

# Métricas

El proyecto podrá medir:

```text
specification_dependencies_total
specification_dependencies_by_type
specification_dependencies_by_intensity
critical_dependencies_total
authority_conflicts_total
dependency_cycles_total
orphan_dependencies_total
deprecated_dependencies_total
average_consumers_per_specification
maximum_dependency_depth
```

---

# Centralidad

Podrá calcularse qué documentos son más centrales.

Indicadores posibles:

- in-degree;
- out-degree;
- betweenness;
- dependency depth;
- impact radius.

---

# Interpretación

Una centralidad alta no implica mala arquitectura.

Puede indicar:

- documento fundacional;
- contrato transversal;
- punto crítico;
- riesgo de propagación.

---

# Riesgo documental

Podrá calcularse de forma orientativa:

```text
risk
=
critical dependencies
+
consumer count
+
change frequency
+
authority weight
```

---

# Dashboard

Podrá mostrar:

- grafo;
- matriz;
- conceptos;
- owners;
- ciclos;
- huérfanos;
- cambios recientes;
- deprecations;
- radios de impacto.

---

# Casos de uso

---

# Caso de uso 1 — Cambio compatible en Retrieval

Se añade un campo opcional a `Evidence Set`.

Acciones:

1. actualizar Retrieval;
2. revisar RAG, Validación y APIs;
3. mantener versión mayor;
4. ejecutar Contract Tests;
5. actualizar este mapa si cambia la relación.

---

# Caso de uso 2 — Breaking Change en `Candidate Set`

Se cambia el tipo de score.

Acciones:

1. incrementar versión mayor;
2. revisar RAG, Razonador, Validación y APIs;
3. crear migración;
4. considerar ADR;
5. ejecutar Quality Gates.

---

# Caso de uso 3 — Nuevo Engine

Se añade un Evaluation Engine.

Acciones:

1. crear especificación si tiene responsabilidad propia;
2. registrar en Engine Registry;
3. definir relación con Orquestador;
4. actualizar README;
5. actualizar inventario;
6. actualizar matriz;
7. validar ciclos.

---

# Caso de uso 4 — División del Motor RAG

Se separa Conversation Engine.

Acciones:

1. justificar bounded context;
2. crear ADR;
3. transferir autoridad de Conversation;
4. actualizar APIs;
5. actualizar Orquestador;
6. migrar dependencias;
7. actualizar este documento.

---

# Caso de uso 5 — Deprecation de un contrato

Se depreca `Retrieval Result v1`.

Acciones:

1. registrar sustitución;
2. identificar consumidores;
3. mantener coexistencia;
4. fijar Sunset;
5. probar migración;
6. retirar dependencia antigua.

---

# Caso de uso 6 — Ciclo de autoridad

RAG redefine `Evidence Set`.

Resultado:

```text
SPEC_AUTHORITY_CONFLICT
```

Resolución:

- mantener autoridad en Retrieval;
- usar especialización o referencia;
- eliminar duplicidad.

---

# Caso de uso 7 — Archivo renombrado

Se renombra una especificación.

Acciones:

- actualizar rutas;
- actualizar README;
- actualizar matriz;
- actualizar referencias;
- ejecutar validación.

---

# Caso de uso 8 — Documento eliminado

No deberá eliminarse si existen consumidores activos.

Primero deberá:

- deprecarse;
- migrarse;
- retirarse;
- actualizar dependencias.

---

# Antipatrones

---

## Mantener dependencias solo en la memoria del equipo

Produce conocimiento tribal.

---

## Duplicar definiciones

Genera authority conflicts.

---

## Declarar todo como dependencia crítica

Reduce utilidad de la clasificación.

---

## Omitir dependencias indirectas en cambios fundacionales

Subestima impacto.

---

## Crear ciclos por comodidad

Aumenta acoplamiento.

---

## Confundir flujo de datos con autoridad

Un productor de datos no siempre define el contrato.

---

## Confundir API con modelo de dominio

La API expone, no necesariamente posee la semántica.

---

## Permitir que Validación sea propietaria de todos los contratos

Validación define reglas, no todos los modelos.

---

## Permitir que Orquestador redefina Engines

El Engine Registry conserva autoridad.

---

## Cambiar owner sin ADR

Puede romper el mapa conceptual.

---

## Mantener matriz manual y registros divergentes

Debe existir una fuente principal.

---

## Versionar cada enlace

Introduce complejidad innecesaria.

---

## No versionar contratos críticos

Impide gestionar compatibilidad.

---

## Eliminar dependencias deprecated sin migración

Rompe consumidores.

---

## Actualizar README y olvidar DEPENDENCIAS

Genera inconsistencias.

---

## Actualizar DEPENDENCIAS y olvidar documentos

El mapa debe reflejar la realidad.

---

# Reglas mínimas de conformidad

---

## Catálogo completo

Todas las especificaciones deberán estar registradas.

---

## Autoridad única

Cada concepto transversal deberá tener owner.

---

## Dependencias explícitas

Las relaciones críticas deberán estar declaradas.

---

## Dirección correcta

Proveedor y consumidor deberán distinguirse.

---

## Intensidad válida

Toda dependencia deberá clasificarse.

---

## Ciclos clasificados

No deberán existir ciclos desconocidos.

---

## Impacto evaluado

Todo breaking change deberá declarar radio.

---

## Versionado

Los contratos críticos deberán versionarse.

---

## Deprecation

Toda retirada deberá tener transición.

---

## Automatización

El grafo deberá poder validarse.

---

## Coherencia

README, archivos y matriz deberán coincidir.

---

## Gobernanza

Los cambios de alto impacto deberán revisarse.

---

# Checklist de nueva especificación

```text
[ ] El documento tiene responsabilidad propia.
[ ] El dominio está identificado.
[ ] El ID es único.
[ ] El owner está definido.
[ ] Los conceptos propietarios están declarados.
[ ] Los proveedores están identificados.
[ ] Los consumidores están identificados.
[ ] Las dependencias están clasificadas.
[ ] La intensidad está definida.
[ ] Los ciclos se han revisado.
[ ] El README está actualizado.
[ ] La matriz está actualizada.
[ ] El Authority Map está actualizado.
[ ] Se ha evaluado si requiere ADR.
[ ] Las validaciones han pasado.
```

---

# Checklist de modificación

```text
[ ] Los conceptos modificados están identificados.
[ ] El owner permanece correcto.
[ ] Los consumidores directos están identificados.
[ ] Los consumidores indirectos están evaluados.
[ ] La compatibilidad está clasificada.
[ ] El radio de impacto está asignado.
[ ] Las revisiones conjuntas están realizadas.
[ ] Los contratos se han versionado.
[ ] Las migraciones están declaradas.
[ ] El changelog está actualizado.
[ ] El mapa de dependencias está actualizado.
[ ] Los Quality Gates han pasado.
```

---

# Checklist de renombrado

```text
[ ] El archivo se ha renombrado.
[ ] El ID se mantiene o migra.
[ ] El título se ha actualizado.
[ ] Las rutas se han actualizado.
[ ] El README se ha actualizado.
[ ] La matriz se ha actualizado.
[ ] El grafo se ha actualizado.
[ ] Las referencias están válidas.
[ ] No quedan nombres antiguos.
[ ] La validación ha pasado.
```

---

# Checklist de deprecation

```text
[ ] La razón está documentada.
[ ] La sustitución está identificada.
[ ] Los consumidores están identificados.
[ ] La fecha de deprecation está definida.
[ ] El Sunset está definido.
[ ] La migración está disponible.
[ ] La dependencia antigua está marcada.
[ ] La nueva dependencia está activa.
[ ] La retirada está planificada.
```

---

# Checklist de cierre del documento

```text
[ ] El inventario contiene las 15 especificaciones.
[ ] Los dominios son correctos.
[ ] Las abreviaturas son únicas.
[ ] El Authority Map está completo.
[ ] La matriz representa las dependencias.
[ ] Las dependencias críticas están identificadas.
[ ] Los caminos de propagación están descritos.
[ ] Los ciclos están gobernados.
[ ] El análisis de impacto está definido.
[ ] El versionado está definido.
[ ] La gobernanza está definida.
[ ] La automatización está descrita.
[ ] Los diagnósticos están definidos.
[ ] Los Quality Gates están definidos.
[ ] Las métricas están definidas.
[ ] Los casos de uso están cubiertos.
[ ] Los antipatrones están cubiertos.
[ ] Los checklists están completos.
[ ] La conformidad global está definida.
```

---

# Conformidad global

`DEPENDENCIAS.md` será conforme cuando:

- represente todas las especificaciones vigentes;
- identifique propietarios conceptuales;
- distinga proveedor y consumidor;
- clasifique tipos e intensidad;
- declare dependencias críticas;
- documente caminos de propagación;
- evite ciclos de autoridad;
- gobierne ciclos operacionales;
- permita analizar impacto;
- preserve compatibilidad;
- soporte deprecation;
- pueda validarse automáticamente;
- permanezca alineado con README y repositorio.

---

# Estado final del documento

```text
Documento:
docs/specifications/DEPENDENCIAS.md

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

El mapa de dependencias proporciona una visión transversal de la arquitectura documental de NovaCoquinaria.

Su función puede resumirse así:

```text
Inventariar
    ↓
Relacionar
    ↓
Asignar autoridad
    ↓
Clasificar dependencias
    ↓
Analizar impacto
    ↓
Detectar ciclos
    ↓
Validar compatibilidad
    ↓
Gobernar cambios
```

Las especificaciones fundacionales definen el significado.

Las especificaciones de conocimiento estructuran el dominio.

La Ingesta incorpora información.

La Validación asegura conformidad.

El Indexing Engine prepara estructuras de búsqueda.

El Retrieval Engine recupera evidencia.

El Razonador deriva conclusiones.

El Motor RAG genera respuestas fundamentadas.

El Engine Registry descubre capacidades.

El Orquestador coordina la ejecución.

Las APIs exponen contratos estables.

El Authority Map evita redefiniciones.

La matriz permite evaluar propagación.

Los radios de impacto ayudan a priorizar revisión.

Los Quality Gates convierten las dependencias en reglas verificables.

Una arquitectura documental coherente deberá poder responder:

```text
¿Quién define cada concepto?

¿Quién lo consume?

¿Qué documentos dependen de otro?

¿Qué intensidad tiene la relación?

¿Qué ocurre si cambia un contrato?

¿Qué dependencias son críticas?

¿Qué ciclos existen?

¿Qué cambios requieren ADR?

¿Qué documentos deben revisarse juntos?

¿Qué migración es necesaria?

¿Qué validaciones deben ejecutarse?

¿El mapa coincide con el repositorio?
```

Con esta tercera parte queda completado `DEPENDENCIAS.md` como catálogo transversal de relaciones, authority map, mecanismo de análisis de impacto y marco de gobernanza de las especificaciones de NovaCoquinaria.
