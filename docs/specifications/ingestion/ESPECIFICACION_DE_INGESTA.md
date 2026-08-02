---
id: SPEC-INGESTA
tipo: especificacion
titulo: Especificación de Ingesta
version: 1.0.0
estado: borrador
ultima_revision: 2026-08-02
tags:
  - ingestion
  - sources
  - normalization
  - pipeline
  - architecture
---

# ESPECIFICACION_DE_INGESTA.md

**Versión:** 2.0.0  
**Estado:** Draft  
**Autor:** NovaCoquinaria Project  
**Última actualización:** 2026-08-01

---

# Parte I — Arquitectura del Ingestion Engine

---

# Introducción

El conocimiento constituye el principal activo del Sistema de Gestión del Conocimiento Culinario (SGCC) de NovaCoquinaria.

Toda capacidad avanzada del sistema —búsqueda semántica, razonamiento, GraphRAG, agentes inteligentes o recomendaciones personalizadas— depende de que dicho conocimiento haya sido incorporado de forma correcta, coherente y trazable.

El **Ingestion Engine** es el componente responsable de transformar información procedente de múltiples fuentes heterogéneas en conocimiento estructurado, validado y preparado para incorporarse al ecosistema semántico del SGCC.

Su misión no consiste únicamente en importar documentos.

Debe garantizar que toda la información:

- pueda identificarse;
- pueda versionarse;
- conserve su procedencia;
- respete la ontología;
- mantenga consistencia;
- pueda evolucionar sin perder trazabilidad.

El motor de ingesta constituye, por tanto, la puerta de entrada oficial al conocimiento del sistema.

---

# Objetivos

Esta especificación persigue los siguientes objetivos:

- definir la arquitectura conceptual del Ingestion Engine;
- establecer su posición dentro del Knowledge Engine;
- formalizar el ciclo de vida de una ingesta;
- definir los distintos tipos de fuentes de conocimiento;
- establecer los componentes internos del pipeline;
- definir los contratos conceptuales entre módulos;
- establecer principios de trazabilidad y procedencia;
- describir los estados de una ingesta;
- preparar la integración con los motores posteriores del SGCC.

---

# Alcance

Esta especificación describe el comportamiento conceptual del proceso de ingesta.

No define:

- implementaciones concretas;
- librerías;
- frameworks;
- motores OCR;
- parsers específicos;
- bases de datos.

Es un documento de arquitectura conceptual.

---

# Papel del Ingestion Engine dentro del SGCC

El Ingestion Engine constituye el primer gran componente operativo del ciclo de vida del conocimiento.

Mientras que el Knowledge Graph representa el conocimiento persistente, la ingesta representa el proceso mediante el cual dicho conocimiento llega al sistema.

Conceptualmente:

```text
Fuentes
    │
    ▼
Ingestion Engine
    │
    ▼
Knowledge Graph
    │
    ▼
Reasoning Engine
    │
    ▼
GraphRAG
    │
    ▼
Agentes
```

Todo conocimiento utilizado posteriormente por el sistema deberá haber pasado previamente por el proceso de ingesta.

---

# Definición

Se define el **Ingestion Engine** como:

> El conjunto de procesos responsables de adquirir, transformar, enriquecer, validar y publicar conocimiento procedente de fuentes internas o externas para incorporarlo al ecosistema semántico del SGCC preservando identidad, procedencia, contexto y calidad.

---

# Responsabilidades

El Ingestion Engine deberá ser responsable de:

- adquirir información;
- identificar el tipo de fuente;
- extraer contenido;
- normalizar formatos;
- generar representaciones internas;
- enriquecer metadatos;
- resolver identidades;
- validar consistencia;
- generar entidades;
- generar relaciones;
- preparar publicación;
- registrar procedencia;
- iniciar la construcción del Knowledge Graph.

No será responsable de:

- realizar inferencias complejas;
- responder consultas;
- generar recomendaciones;
- ejecutar agentes;
- resolver conflictos semánticos avanzados.

Estas capacidades pertenecen a otros motores especializados.

---

# Principios arquitectónicos

Toda implementación del Ingestion Engine deberá respetar los siguientes principios.

---

## Separación entre adquisición y conocimiento

Obtener información no equivale a incorporar conocimiento.

La adquisición es únicamente el primer paso del pipeline.

---

## Fuente inmutable

Toda fuente original deberá conservarse sin modificaciones.

Las transformaciones posteriores deberán operar sobre representaciones derivadas.

---

## Transformaciones reproducibles

Toda transformación deberá poder reconstruirse.

No deberán existir modificaciones ocultas.

---

## Procedencia obligatoria

Todo elemento generado deberá conservar su origen.

La pérdida de procedencia invalidará la incorporación del conocimiento.

---

## Versionado

Las fuentes y sus derivados deberán versionarse.

---

## Idempotencia

Procesar dos veces exactamente la misma fuente no deberá generar conocimiento duplicado.

---

## Modularidad

Cada transformación deberá pertenecer a un componente claramente identificado.

---

## Trazabilidad completa

Deberá ser posible reconstruir el recorrido completo desde cualquier entidad hasta la fuente original.

---

## Validación progresiva

La validación no deberá realizarse únicamente al final del proceso.

Cada fase deberá validar aquello que le corresponde.

---

## Publicación controlada

El conocimiento únicamente podrá incorporarse al Knowledge Graph cuando haya superado los controles definidos.

---

# Modelo conceptual

La ingesta puede entenderse como una tubería de transformación progresiva.

```text
Información

↓

Datos estructurados

↓

Representación documental

↓

Representación semántica

↓

Conocimiento validado

↓

Knowledge Graph
```

Cada etapa incrementa el valor semántico de la información.

---

# Modelo general del pipeline

Conceptualmente, el pipeline puede representarse como:

```text
Fuente

↓

Adquisición

↓

Extracción

↓

Normalización

↓

Representación interna

↓

Enriquecimiento

↓

Validación

↓

Construcción semántica

↓

Publicación
```

Cada fase constituye una responsabilidad independiente.

---

# Capas del proceso

El proceso de ingesta puede dividirse en varias capas.

```text
Captura

↓

Procesamiento documental

↓

Procesamiento semántico

↓

Validación

↓

Publicación
```

---

# Tipos de entrada

El motor deberá admitir múltiples tipos de conocimiento.

Conceptualmente podrán clasificarse como:

```text
Documentos

Datos estructurados

Contenido multimedia

Fuentes externas

Conocimiento generado

Eventos
```

Cada categoría requerirá un pipeline específico.

---

# Conocimiento explícito e implícito

La ingesta distinguirá entre:

## Conocimiento explícito

Información declarada directamente.

Ejemplo:

```text
El miso contiene soja.
```

---

## Conocimiento implícito

Información susceptible de derivarse posteriormente mediante razonamiento.

Ejemplo:

```text
La receta contiene soja.
```

La ingesta únicamente incorporará el hecho explícito.

Las inferencias corresponderán al Reasoner.

---

# Modelo de transformación

Cada fase recibe un artefacto y produce otro.

```text
Artefacto A

↓

Transformación

↓

Artefacto B
```

Las transformaciones deberán ser deterministas siempre que sea posible.

---

# Artefactos

Ejemplos de artefactos conceptuales:

```text
Documento original

Documento normalizado

AST

Representación documental

Entidades

Relaciones

Metadatos

Knowledge Package
```

Cada artefacto deberá poseer identidad propia.

---

# Flujo de alto nivel

```text
Documento

↓

Extracción

↓

Documento normalizado

↓

Análisis

↓

Modelo interno

↓

Enriquecimiento

↓

Modelo semántico

↓

Validación

↓

Publicación
```

---

# Knowledge Package

El resultado principal del proceso previo a la publicación será un **Knowledge Package**.

Este paquete contendrá todo el conocimiento extraído de una fuente.

Conceptualmente:

```text
Documento

+

Metadatos

+

Entidades

+

Relaciones

+

Contexto

+

Procedencia

+

Versiones

+

Diagnósticos
```

---

# Definición

Un Knowledge Package representa una unidad autocontenida de conocimiento preparada para ser validada y publicada.

---

# Características

Todo Knowledge Package deberá:

- ser identificable;
- ser versionable;
- ser trazable;
- ser reproducible;
- ser portable;
- ser validable.

---

# Identidad

Formato recomendado:

```text
KP-XXXXXX
```

Ejemplo:

```text
KP-000421
```

---

# Contrato conceptual

```yaml
id: KP-000421

source:
    id: DOC-00124

version: 1.0.0

status: normalized

entities: [...]

relations: [...]

metadata: [...]

provenance: [...]

diagnostics: [...]
```

---

# Fuente

La fuente representa el origen del conocimiento.

Una fuente podrá ser:

- local;
- remota;
- dinámica;
- generada.

---

# Identidad de fuente

Formato recomendado:

```text
SRC-XXXXXX
```

---

# Tipos de fuente

Ejemplos:

```text
Markdown

PDF

Imagen

HTML

API

CSV

JSON

Vídeo

Audio

Base de datos

RSS

Repositorio Git
```

La clasificación detallada se desarrollará en la Parte II.

---

# Procedencia

Todo elemento generado deberá conservar información sobre:

- origen;
- autor;
- fecha;
- versión;
- licencia;
- método de adquisición.

---

# Definición de procedencia

La procedencia describe el historial conocido de un elemento desde su origen hasta su estado actual.

---

# Cadena de procedencia

```text
Fuente

↓

Extracción

↓

Normalización

↓

Enriquecimiento

↓

Validación

↓

Publicación
```

---

# Lineage

El Ingestion Engine deberá construir el primer nivel del lineage utilizado posteriormente por el Knowledge Graph y el Reasoner.

---

# Contexto

La ingesta deberá preservar el contexto documental.

Ejemplos:

- colección;
- idioma;
- versión;
- autor;
- región;
- época;
- dominio.

---

# Snapshot

Toda ejecución operará sobre un snapshot identificable.

```text
Snapshot

↓

Pipeline

↓

Knowledge Package
```

---

# Identidad de ejecución

Cada ejecución deberá poseer un identificador único.

Formato recomendado:

```text
ING-EXEC-XXXXXX
```

---

# Contrato de ejecución

```yaml
id: ING-EXEC-000041

source:
    id: SRC-00112

pipeline: PIPELINE-MARKDOWN

started_at: ...

status: running
```

---

# Estados de ejecución

Valores recomendados:

```text
Queued

Running

Paused

Waiting

Completed

Failed

Cancelled

RolledBack
```

---

# Queued

Pendiente de ejecución.

---

# Running

Actualmente procesándose.

---

# Waiting

Esperando un recurso externo.

---

# Completed

Proceso finalizado correctamente.

---

# Failed

Proceso interrumpido por error.

---

# Cancelled

Proceso cancelado.

---

# RolledBack

Los cambios fueron revertidos.

---

# Pipeline

Un pipeline representa una secuencia ordenada de transformaciones.

Formato recomendado:

```text
PIPELINE-MARKDOWN

PIPELINE-PDF

PIPELINE-WEB

PIPELINE-API
```

---

# Paso

Cada pipeline se compone de pasos.

```text
Pipeline

↓

Step

↓

Step

↓

Step
```

---

# Identidad de paso

Formato:

```text
STEP-XXXX
```

---

# Tipos de paso

Ejemplos:

```text
Acquire

Extract

Normalize

Enrich

Validate

Publish
```

---

# Contrato de paso

```yaml
step:

    id: STEP-0005

    name: Normalize

    input:
        Document

    output:
        NormalizedDocument
```

---

# Dependencias

Cada paso podrá depender de pasos anteriores.

No deberán existir ciclos.

---

# Paralelismo

Dos pasos independientes podrán ejecutarse en paralelo.

El pipeline deberá declarar dichas dependencias explícitamente.

---

# Orquestación

La orquestación del pipeline deberá ser responsabilidad del Ingestion Engine.

Los pasos individuales no deberán decidir el flujo global.

---

# Eventos

Cada transición importante generará eventos internos.

Ejemplos:

```text
SourceDetected

ExtractionCompleted

NormalizationCompleted

ValidationStarted

KnowledgePackageReady

PublicationCompleted
```

---

# Observabilidad

Toda ejecución deberá producir:

- logs;
- métricas;
- trazas;
- diagnósticos.

Los detalles operativos se desarrollarán en la Parte VI.

---

# Errores

El pipeline distinguirá entre:

```text
Error

Advertencia

Información
```

---

# Error

Impide continuar.

---

# Advertencia

Permite continuar con restricciones.

---

# Información

No modifica el flujo.

---

# Reintentos

Los pasos podrán declararse:

```text
Retryable

Non Retryable
```

---

# Idempotencia del pipeline

La repetición del mismo pipeline sobre la misma versión de una fuente deberá producir el mismo Knowledge Package.

---

# Publicación

La publicación constituye el límite entre:

```text
Conocimiento procesado
```

y

```text
Conocimiento disponible
```

Hasta este momento el conocimiento permanecerá aislado del Knowledge Graph.

---

# Calidad

El Ingestion Engine constituye la primera línea de defensa de la calidad del conocimiento.

Todo conocimiento deberá superar los controles definidos antes de publicarse.

---

# Responsabilidad

El Ingestion Engine garantiza:

- adquisición;
- transformación;
- trazabilidad;
- consistencia documental;
- identidad;
- procedencia.

No garantiza la corrección lógica completa del conocimiento, responsabilidad que recaerá posteriormente sobre el Validation Engine y el Reasoning Engine.

---

# Arquitectura conceptual

La arquitectura general puede resumirse mediante el siguiente esquema.

```text
                    Fuentes
                       │
                       ▼
               Ingestion Engine
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
  Acquisition     Transformation   Validation
        │              │              │
        └──────────────┼──────────────┘
                       ▼
              Knowledge Package
                       │
                       ▼
               Publication Engine
                       │
                       ▼
               Knowledge Graph
```

---

# Relación con otros motores

El Ingestion Engine se integra con el resto del Knowledge Engine de la siguiente forma:

```text
Fuentes
    │
    ▼
Ingestion Engine
    │
    ▼
Knowledge Graph
    │
    ├────────► Constraint Engine
    ├────────► Reasoning Engine
    ├────────► Explanation Engine
    ├────────► Materialization Engine
    └────────► GraphRAG
```

---

# Transición hacia la Parte II

Esta primera parte ha definido:

- la misión del Ingestion Engine;
- sus responsabilidades;
- su arquitectura conceptual;
- el pipeline general;
- los principios arquitectónicos;
- el concepto de Knowledge Package;
- las fuentes;
- la procedencia;
- la identidad de las ejecuciones;
- los estados del pipeline;
- la estructura de publicación.

La **Parte II** desarrollará el proceso de adquisición del conocimiento describiendo:

- tipos de fuentes;
- conectores;
- importadores;
- extracción documental;
- adquisición incremental;
- conectores externos;
- formatos soportados;
- integración con APIs;
- OCR;
- multimedia;
- streaming;
- plugins de ingesta.

---

# Conclusión

El Ingestion Engine constituye la puerta de entrada oficial al conocimiento de NovaCoquinaria.

Su responsabilidad no consiste únicamente en importar información, sino en transformarla de manera controlada en conocimiento estructurado, trazable y preparado para integrarse con el ecosistema semántico del SGCC.

Todo el funcionamiento posterior del sistema —Knowledge Graph, Razonador, GraphRAG y Agentes— depende de la calidad, consistencia y gobernanza establecidas durante este proceso inicial de ingesta.

Por ello, el Ingestion Engine debe entenderse como el primer componente operativo del **Knowledge Engine**, encargado de garantizar que cada nuevo elemento incorporado al sistema conserve su identidad, procedencia, contexto y capacidad de evolución durante todo su ciclo de vida.

---

# Parte II — Fuentes, conectores y extracción

---

# Introducción

La Parte I ha definido:

- la misión del Ingestion Engine;
- su posición dentro del Knowledge Engine;
- el pipeline general;
- el concepto de fuente;
- el concepto de Knowledge Package;
- la identidad de las ejecuciones;
- los estados del proceso;
- los principios de trazabilidad, idempotencia y publicación controlada.

Esta segunda parte desarrolla la primera mitad operativa del proceso de ingesta:

```text
Fuente
   ↓
Conector
   ↓
Adquisición
   ↓
Extracción
   ↓
Artefacto extraído
```

El objetivo consiste en formalizar cómo el SGCC obtiene información procedente de fuentes heterogéneas sin perder:

- identidad;
- formato original;
- estructura;
- procedencia;
- contexto;
- licencia;
- integridad.

La adquisición y la extracción no deberán interpretarse como operaciones equivalentes.

La adquisición responde:

> ¿Cómo obtiene el sistema acceso a la fuente?

La extracción responde:

> ¿Cómo obtiene el sistema el contenido útil de dicha fuente?

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir el modelo formal de fuente;
- clasificar los tipos de fuente admitidos;
- definir conectores e importadores;
- formalizar la adquisición;
- definir mecanismos de extracción;
- distinguir contenido, estructura y metadatos;
- regular la ingesta de documentos y datos estructurados;
- definir la extracción desde contenido multimedia;
- establecer políticas para OCR y transcripción;
- regular las fuentes web y APIs;
- definir ingestas batch, incrementales y por streaming;
- establecer contratos para conectores;
- preservar procedencia, licencia e integridad;
- definir errores, reintentos y aislamiento;
- preparar la representación normalizada de la Parte III.

---

# Principios de adquisición y extracción

Toda adquisición deberá respetar los siguientes principios.

---

## Preservación del original

La fuente original deberá conservarse, referenciarse o poder recuperarse cuando:

- la licencia lo permita;
- la seguridad lo permita;
- el origen permanezca disponible.

Las transformaciones no deberán sobrescribirla.

---

## Identidad de fuente

Toda fuente deberá poseer una identidad estable dentro del SGCC.

---

## Integridad verificable

El sistema deberá poder comprobar que el contenido adquirido no ha cambiado durante el procesamiento.

---

## Procedencia obligatoria

Todo artefacto extraído deberá indicar:

- fuente;
- versión;
- conector;
- ejecución;
- fecha;
- método;
- transformaciones iniciales.

---

## Adquisición autorizada

El sistema no deberá adquirir contenido sin:

- permiso;
- licencia;
- base legítima;
- configuración autorizada.

---

## Separación entre contenido y estructura

La extracción deberá preservar, cuando resulte relevante:

- contenido textual;
- jerarquía;
- tablas;
- listas;
- enlaces;
- imágenes;
- notas;
- metadatos;
- posición.

---

## Idempotencia

Procesar la misma versión de una fuente con el mismo conector no deberá generar duplicados.

---

## Reproducibilidad

La extracción deberá poder repetirse utilizando:

- misma fuente;
- misma versión;
- mismo conector;
- misma configuración.

---

## Degradación visible

Cuando no pueda conservarse toda la información, la pérdida deberá declararse.

---

## Seguridad por defecto

Las fuentes no confiables deberán procesarse en entornos aislados.

---

# Modelo formal de fuente

Una fuente es cualquier origen identificable desde el que el SGCC puede adquirir información.

Formalmente:

```text
Source = (
  Identity,
  Type,
  Location,
  Version,
  Ownership,
  License,
  Integrity,
  AccessPolicy,
  Metadata
)
```

---

# Identificador de fuente

Formato recomendado:

```text
SRC-XXXXXX
```

Ejemplo:

```text
SRC-000142
```

---

# Contrato mínimo de fuente

```yaml
id: SRC-000142
type: markdown_document

location:
  uri: docs/recipes/REC-0009.md

status: active
```

---

# Contrato ampliado de fuente

```yaml
id: SRC-000142
type: markdown_document

name: Receta de sopa de miso

location:
  scheme: repository
  uri: docs/recipes/REC-0009.md

version:
  type: git_commit
  value: 6fa8c42

status: active
sensitivity: internal

ownership:
  owner: NovaCoquinaria
  maintainer: knowledge_team

license:
  id: internal-project-license
  reuse_allowed: true

integrity:
  algorithm: sha256
  hash: sha256:...

language:
  - es

metadata:
  domain: recipes
  expected_document_type: recipe
```

---

# Tipos de fuente

Las fuentes podrán clasificarse mediante varias dimensiones.

---

# Según su origen

---

## Fuente interna

Gestionada directamente por NovaCoquinaria.

Ejemplos:

- repositorio Markdown;
- configuración;
- vocabularios;
- tablas;
- ontología;
- documentos de gestión.

---

## Fuente externa

Pertenece a un sistema ajeno.

Ejemplos:

- API pública;
- web;
- publicación;
- dataset;
- catálogo externo.

---

## Fuente personal

Pertenece a un usuario.

Ejemplos:

- inventario;
- fotografía de despensa;
- ticket de compra;
- receta privada;
- preferencia.

Deberá mantenerse separada del conocimiento global.

---

## Fuente generada

Producida por un proceso automático.

Ejemplos:

- transcripción;
- resultado OCR;
- resumen;
- extracción de entidades;
- propuesta generada mediante IA.

No deberá confundirse con la fuente original.

---

# Según su estructura

---

## Fuente estructurada

Posee un esquema explícito.

Ejemplos:

- JSON;
- YAML;
- CSV;
- base de datos;
- RDF.

---

## Fuente semiestructurada

Posee estructura parcial.

Ejemplos:

- Markdown;
- HTML;
- XML;
- correo electrónico;
- documento con Front Matter.

---

## Fuente no estructurada

No ofrece una estructura semántica directamente utilizable.

Ejemplos:

- texto libre;
- PDF escaneado;
- imagen;
- audio;
- vídeo.

---

# Según su actualización

---

## Fuente estática

No cambia tras su publicación.

Ejemplo:

```text
libro digitalizado
```

---

## Fuente versionada

Conserva historial.

Ejemplos:

- Git;
- API con versión;
- dataset con releases.

---

## Fuente mutable

Puede cambiar sin conservar historial accesible.

Ejemplo:

```text
página web viva
```

---

## Fuente continua

Produce eventos de forma permanente.

Ejemplos:

- streaming;
- webhook;
- feed;
- cola de mensajes.

---

# Según su confianza

Valores recomendados:

```text
authoritative
validated
trusted
unverified
experimental
untrusted
```

La confianza de la fuente no deberá transferirse automáticamente a todas sus afirmaciones.

---

# Según su sensibilidad

Valores posibles:

```text
public
internal
restricted
confidential
personal
critical
```

---

# Registro de fuentes

Toda fuente deberá registrarse antes de incorporarse a un pipeline estable.

El registro deberá permitir:

- localizarla;
- identificarla;
- conocer su tipo;
- aplicar el conector correcto;
- controlar permisos;
- definir frecuencia;
- conservar historial.

---

# Catálogo de fuentes

El SGCC podrá mantener un catálogo central.

```yaml
source_catalog:
  sources:
    - SRC-000142
    - SRC-000143
    - SRC-000144
```

---

# Estado de fuente

Valores recomendados:

```text
proposed
registered
active
paused
unavailable
deprecated
blocked
archived
```

---

# Fuente propuesta

Todavía no se ha aprobado su uso.

---

# Fuente registrada

Existe en el catálogo, pero no necesariamente dispone de una ingesta activa.

---

# Fuente activa

Puede ser procesada.

---

# Fuente pausada

Se conserva, pero no se programan nuevas ejecuciones.

---

# Fuente no disponible

No puede accederse temporalmente.

---

# Fuente deprecada

No deberá utilizarse en nuevas ingestas salvo compatibilidad histórica.

---

# Fuente bloqueada

No puede procesarse debido a:

- licencia;
- seguridad;
- calidad;
- integridad;
- decisión de gobernanza.

---

# Fuente archivada

Solo se conserva para trazabilidad histórica.

---

# Fuente y documento

Una fuente no es necesariamente un documento SGCC.

Ejemplo:

```text
SRC-000142
```

representa el origen adquirido.

```text
DOC-0051
```

representa el documento normalizado y gobernado dentro del SGCC.

La relación podrá expresarse como:

```text
DOC-0051 derived_from SRC-000142
```

---

# Fuente compuesta

Una fuente podrá contener múltiples unidades.

Ejemplos:

- repositorio;
- archivo ZIP;
- base de datos;
- sitio web;
- feed;
- carpeta.

---

# Unidad de fuente

Formato recomendado:

```text
SRC-ITEM-XXXXXX
```

Ejemplo:

```text
SRC-ITEM-000421
```

---

## Contrato de unidad de fuente

```yaml
id: SRC-ITEM-000421

source: SRC-REPOSITORY-0001

path: docs/recipes/REC-0009.md

media_type: text/markdown

integrity:
  algorithm: sha256
  hash: sha256:...
```

---

# Descubrimiento de fuentes

El descubrimiento identifica nuevas unidades susceptibles de ingesta.

Podrá realizarse mediante:

- exploración de directorios;
- lectura de manifiestos;
- enumeración de API;
- crawling;
- consulta de base de datos;
- consumo de eventos;
- configuración manual.

---

# Descubrimiento completo

Enumera todos los elementos disponibles.

---

# Descubrimiento incremental

Obtiene solo:

- nuevos elementos;
- elementos modificados;
- elementos eliminados.

---

# Cursor de descubrimiento

Una fuente incremental podrá mantener:

```yaml
cursor:
  source: SRC-API-0004
  value: "2026-08-01T10:00:00Z"
```

---

# Watermark

Podrá utilizarse una marca temporal o secuencial para determinar hasta qué punto se ha procesado una fuente.

---

# Limitaciones del descubrimiento

El sistema deberá registrar cuando una fuente no permita detectar de forma fiable:

- eliminaciones;
- modificaciones;
- versiones;
- orden;
- duplicados.

---

# Conector

Un conector es el componente que permite comunicarse con un tipo de fuente.

Formato recomendado:

```text
CONNECTOR-<TIPO>-XXXX
```

Ejemplos:

```text
CONNECTOR-FILESYSTEM-0001
CONNECTOR-GIT-0001
CONNECTOR-HTTP-0001
CONNECTOR-API-0003
```

---

# Responsabilidades de un conector

Un conector podrá ser responsable de:

- autenticación;
- localización;
- descubrimiento;
- lectura;
- paginación;
- descarga;
- control de versiones;
- reintentos;
- rate limiting;
- comprobación de integridad.

No deberá realizar normalización semántica avanzada.

---

# Contrato mínimo de conector

```yaml
id: CONNECTOR-GIT-0001
type: git_connector

version: 1.0.0
status: stable

supported_sources:
  - git_repository
```

---

# Contrato ampliado de conector

```yaml
id: CONNECTOR-GIT-0001
type: git_connector

name: Conector de repositorios Git
version: 1.0.0
status: stable

capabilities:
  discovery: true
  incremental: true
  deletions: true
  versioning: true
  checksums: true
  streaming: false

input:
  source_types:
    - git_repository

output:
  artifact_type: acquired_binary

security:
  authentication:
    - ssh_key
    - access_token

  sandbox_required: false

limits:
  max_file_size_mb: 25

governance:
  owner: ingestion_platform_team
```

---

# Capacidades de un conector

Un conector deberá declarar si soporta:

- descubrimiento;
- adquisición completa;
- adquisición parcial;
- incrementalidad;
- detección de eliminaciones;
- reanudación;
- paginación;
- streaming;
- autenticación;
- hashes;
- versionado;
- webhooks.

---

# Conector de lectura

Solo obtiene información.

Será el tipo predeterminado.

---

# Conector bidireccional

Puede leer y escribir.

Su uso deberá estar restringido.

La ingesta no deberá modificar la fuente salvo flujo explícitamente gobernado.

---

# Adaptador

Un adaptador transforma la interfaz específica de un sistema externo en el contrato común del Ingestion Engine.

---

# Diferencia entre conector y extractor

El conector obtiene los bytes o registros.

El extractor interpreta su contenido.

```text
Conector
   ↓
Artefacto adquirido
   ↓
Extractor
   ↓
Contenido extraído
```

---

# Importador

Un importador combina configuración de:

- fuente;
- conector;
- extractor;
- mapeo;
- políticas.

Formato recomendado:

```text
IMPORTER-XXXX
```

---

# Contrato de importador

```yaml
id: IMPORTER-MARKDOWN-RECIPES
version: 1.0.0
status: stable

source_types:
  - markdown_document

connector: CONNECTOR-FILESYSTEM-0001
extractor: EXTRACTOR-MARKDOWN-0001
mapping: MAP-MARKDOWN-RECIPE-0001

pipeline: PIPELINE-MARKDOWN
```

---

# Plugin de ingesta

Un plugin podrá incorporar soporte para:

- nuevo formato;
- nuevo sistema externo;
- nueva extracción;
- nuevo mapeo.

Los plugins deberán:

- registrarse;
- versionarse;
- declarar permisos;
- aislarse;
- superar validaciones.

---

# Registro de conectores

El SGCC deberá mantener un catálogo de conectores.

```yaml
connector_registry:
  connectors:
    - CONNECTOR-FILESYSTEM-0001
    - CONNECTOR-GIT-0001
    - CONNECTOR-HTTP-0001
```

---

# Selección de conector

Podrá basarse en:

- tipo de fuente;
- URI;
- media type;
- configuración;
- política;
- prioridad.

---

# Detección automática

La detección automática podrá proponer un conector.

No deberá seleccionar silenciosamente uno ambiguo en fuentes críticas.

---

# Configuración del conector

La configuración deberá separarse del código.

Ejemplo:

```yaml
connector_config:
  connector: CONNECTOR-HTTP-0001

  timeout_seconds: 20
  max_retries: 3
  follow_redirects: true

  rate_limit:
    requests_per_minute: 60
```

---

# Secretos

Las credenciales no deberán almacenarse en:

- documentos;
- YAML versionado;
- Knowledge Graph;
- logs;
- Knowledge Package.

Deberán referenciarse mediante un gestor de secretos.

---

# Adquisición

La adquisición es el proceso mediante el cual se obtiene una representación fiel de la fuente.

---

# Artefacto adquirido

Formato recomendado:

```text
ACQ-ART-XXXXXX
```

---

## Contrato de artefacto adquirido

```yaml
id: ACQ-ART-000421
type: acquired_artifact

source: SRC-000142
source_item: SRC-ITEM-000421

execution: ING-EXEC-000041
connector: CONNECTOR-GIT-0001

media_type: text/markdown
size_bytes: 14231

integrity:
  algorithm: sha256
  hash: sha256:...

acquired_at: 2026-08-01T12:00:00+02:00
```

---

# Modos de adquisición

---

## Adquisición completa

Obtiene todo el contenido.

---

## Adquisición parcial

Obtiene:

- rango;
- página;
- sección;
- campos concretos;
- lote.

---

## Adquisición incremental

Obtiene únicamente cambios.

---

## Adquisición por eventos

Se activa cuando la fuente notifica un cambio.

---

## Adquisición programada

Se ejecuta según planificación.

---

## Adquisición manual

La inicia un usuario autorizado.

---

# Integridad de adquisición

La integridad podrá comprobarse mediante:

- hash;
- ETag;
- versión;
- firma;
- tamaño;
- checksum del proveedor.

---

# Huella de fuente

Podrá construirse una huella combinando:

```text
source_id
+
source_version
+
content_hash
+
connector_version
```

---

# Detección de duplicados en adquisición

Dos artefactos podrán considerarse idénticos cuando compartan:

- contenido;
- tamaño;
- media type;
- hash.

La identidad de fuente deberá mantenerse aunque el contenido coincida.

---

# Reanudación

Los conectores podrán soportar reanudación de:

- descarga;
- paginación;
- streaming;
- lote.

La reanudación deberá conservar:

- cursor;
- offset;
- hash parcial;
- ejecución.

---

# Paginación

Las APIs y bases de datos podrán devolver contenido paginado.

El conector deberá registrar:

- página;
- cursor;
- token;
- total conocido;
- orden.

---

# Orden estable

La ingesta incremental deberá utilizar un orden estable cuando la fuente lo permita.

---

# Rate limiting

Los conectores externos deberán respetar los límites del proveedor.

---

# Política de reintentos

Podrá definirse:

```yaml
retry_policy:
  max_attempts: 4
  strategy: exponential_backoff
  initial_delay_ms: 500
  retryable_status:
    - 429
    - 502
    - 503
    - 504
```

---

# Circuit breaker

Podrá utilizarse para evitar llamadas repetidas a una fuente fallida.

---

# Timeout

Deberán existir límites para:

- conexión;
- lectura;
- ejecución;
- descarga total.

---

# Adquisición atómica

Cuando sea posible, deberá adquirirse una versión consistente de la fuente.

---

# Fuente modificada durante la adquisición

Si una fuente cambia mientras se procesa, el sistema deberá:

- reiniciar;
- fijar una versión;
- marcar inconsistencia;
- rechazar el artefacto.

---

# Extracción

La extracción convierte el artefacto adquirido en contenido interpretable.

Formalmente:

```text
Acquired Artifact
        ↓
Extractor
        ↓
Extracted Artifact
```

---

# Extractor

Formato recomendado:

```text
EXTRACTOR-<FORMATO>-XXXX
```

Ejemplos:

```text
EXTRACTOR-MARKDOWN-0001
EXTRACTOR-PDF-0001
EXTRACTOR-HTML-0001
EXTRACTOR-CSV-0001
```

---

# Responsabilidades del extractor

El extractor deberá:

- reconocer formato;
- interpretar estructura;
- extraer contenido;
- conservar posiciones;
- generar diagnósticos;
- declarar pérdidas;
- preservar metadatos técnicos.

No deberá:

- resolver identidades semánticas definitivas;
- publicar conocimiento;
- ejecutar inferencias;
- modificar la fuente.

---

# Contrato mínimo de extractor

```yaml
id: EXTRACTOR-MARKDOWN-0001
type: markdown_extractor

version: 1.0.0
status: stable

input_media_types:
  - text/markdown

output_type: extracted_document
```

---

# Contrato ampliado de extractor

```yaml
id: EXTRACTOR-MARKDOWN-0001
type: markdown_extractor

name: Extractor Markdown SGCC
version: 1.0.0
status: stable

input_media_types:
  - text/markdown

capabilities:
  text: true
  headings: true
  lists: true
  tables: true
  links: true
  images: true
  front_matter: true
  source_positions: true

output:
  type: extracted_document
  schema_version: 1.0.0

loss_profile:
  expected_loss: none

governance:
  owner: ingestion_platform_team
```

---

# Artefacto extraído

Formato recomendado:

```text
EXT-ART-XXXXXX
```

---

## Contrato de artefacto extraído

```yaml
id: EXT-ART-000421
type: extracted_document

source_artifact: ACQ-ART-000421
extractor: EXTRACTOR-MARKDOWN-0001

content:
  title: Sopa de miso
  blocks: [...]

metadata:
  front_matter: {...}

diagnostics: []

integrity:
  source_hash: sha256:...
  extraction_hash: sha256:...
```

---

# Modelo de contenido extraído

El contenido extraído podrá incluir:

- texto;
- bloques;
- estructura;
- metadatos;
- referencias;
- recursos;
- posiciones;
- anotaciones;
- diagnósticos.

---

# Posición de origen

Todo fragmento relevante debería poder enlazarse con:

- página;
- línea;
- columna;
- rango de bytes;
- XPath;
- selector CSS;
- timestamp;
- frame;
- celda;
- registro.

---

# Selector de fuente

Ejemplo:

```yaml
source_selector:
  type: line_range
  start_line: 42
  end_line: 57
```

---

# Extracción sin pérdida

Conserva toda la información relevante del origen.

---

# Extracción con pérdida controlada

El extractor no puede conservar ciertos elementos.

Deberá declararlo.

```yaml
losses:
  - type: unsupported_layout
    description: La posición flotante de la imagen no se conserva.
```

---

# Perfil de extracción

Podrán existir perfiles:

```text
full
semantic
text_only
metadata_only
preview
```

---

# Perfil completo

Intenta conservar todo.

---

# Perfil semántico

Prioriza elementos útiles para conocimiento.

---

# Perfil de texto

Extrae únicamente contenido textual.

---

# Perfil de metadatos

No procesa el cuerpo.

---

# Perfil de previsualización

Obtiene una muestra de bajo coste.

---

# Extracción documental

Los documentos podrán descomponerse en:

```text
Documento
   │
   ├── Metadatos
   ├── Secciones
   ├── Párrafos
   ├── Listas
   ├── Tablas
   ├── Imágenes
   ├── Enlaces
   └── Notas
```

---

# Extracción de Markdown

El extractor Markdown deberá reconocer:

- Front Matter;
- títulos;
- encabezados;
- párrafos;
- listas;
- tablas;
- bloques de código;
- citas;
- enlaces;
- imágenes;
- notas;
- identificadores;
- etiquetas.

---

# Front Matter

El Front Matter deberá extraerse como estructura independiente.

Ejemplo:

```yaml
front_matter:
  id: REC-0009
  type: recipe
  status: active
```

---

# AST Markdown

La representación intermedia recomendada será un árbol sintáctico.

```text
Document
 ├── Heading
 ├── Paragraph
 ├── List
 ├── Table
 └── CodeBlock
```

---

# Bloques de código

Los bloques de código no deberán interpretarse automáticamente como conocimiento factual.

Podrán contener:

- ejemplos;
- contratos;
- pseudocódigo;
- datos.

Su semántica dependerá del tipo de documento.

---

# Enlaces Markdown

Deberán extraerse:

- texto;
- destino;
- tipo;
- posición;
- si son internos o externos.

---

# Tablas Markdown

Deberán conservar:

- cabeceras;
- filas;
- celdas;
- alineación;
- posición;
- contexto de sección.

---

# Extracción de PDF

Los PDF podrán ser:

- digitales;
- híbridos;
- escaneados.

---

# PDF digital

Permite extraer directamente:

- texto;
- metadatos;
- páginas;
- enlaces;
- marcadores;
- imágenes.

---

# PDF escaneado

Requiere OCR.

La salida OCR deberá marcarse como derivada y probabilística.

---

# PDF híbrido

Podrá combinar texto digital e imágenes escaneadas.

El sistema deberá evitar duplicar texto.

---

# Orden de lectura

Los PDF pueden contener columnas o diseños complejos.

El extractor deberá registrar la confianza del orden reconstruido.

---

# Páginas

Toda unidad extraída de un PDF deberá poder enlazarse con su página.

---

# Tablas PDF

La extracción de tablas deberá conservar:

- página;
- región;
- filas;
- columnas;
- celdas;
- confianza.

---

# Gráficos e imágenes PDF

Deberán tratarse como recursos enlazados.

No deberán convertirse automáticamente en hechos sin una fase específica de interpretación.

---

# Extracción de HTML

El extractor HTML deberá diferenciar:

- contenido principal;
- navegación;
- publicidad;
- cabecera;
- pie;
- scripts;
- elementos ocultos.

---

# DOM

La representación inicial podrá conservar el árbol DOM.

---

# Contenido principal

Podrá identificarse mediante:

- etiquetas semánticas;
- selectores;
- reglas del sitio;
- heurísticas;
- modelos.

La estrategia deberá declararse.

---

# HTML dinámico

Algunas páginas requieren renderizado.

El conector deberá declarar si utiliza:

- HTTP simple;
- navegador sin interfaz;
- API subyacente;
- snapshot proporcionado.

---

# Scripts

El código JavaScript no deberá ejecutarse salvo entorno controlado.

---

# Formularios

No deberán enviarse automáticamente salvo flujo autorizado.

---

# Extracción de XML

Deberá conservar:

- namespaces;
- atributos;
- jerarquía;
- orden;
- esquema;
- validación.

---

# Extracción de JSON

El extractor deberá conservar:

- claves;
- valores;
- arrays;
- tipos;
- rutas JSON Pointer;
- esquema cuando exista.

---

# JSON Pointer

Ejemplo:

```text
/recipes/0/ingredients/2
```

---

# Extracción de YAML

Deberá evitar ambigüedades de:

- tipos implícitos;
- duplicidad de claves;
- anchors;
- aliases;
- tags personalizados.

---

# Duplicidad de claves YAML

Deberá considerarse error.

---

# Extracción de CSV

El extractor deberá declarar:

- delimitador;
- codificación;
- cabecera;
- escape;
- comillas;
- formato de fechas;
- tipos inferidos.

---

# Inferencia de tipos CSV

Los tipos inferidos deberán considerarse provisionales.

---

# Posición CSV

La procedencia deberá conservar:

- fila;
- columna;
- nombre de campo.

---

# Extracción de hojas de cálculo

Podrá conservar:

- libro;
- hoja;
- celda;
- fórmula;
- valor calculado;
- formato;
- rango;
- tablas.

---

# Fórmula y valor

Deberán distinguirse.

Ejemplo:

```yaml
cell:
  address: C8
  formula: "=A8*B8"
  calculated_value: 240
```

---

# Celdas combinadas

Deberán registrarse para evitar interpretaciones incorrectas.

---

# Filas ocultas

No deberán descartarse silenciosamente.

---

# Bases de datos

La adquisición desde bases de datos podrá realizarse mediante:

- snapshot;
- consulta;
- exportación;
- CDC;
- réplica de lectura.

---

# Conector de base de datos

Deberá definir:

- motor;
- esquema;
- tablas;
- consulta;
- aislamiento;
- cursor;
- credenciales;
- límites.

---

# Snapshot de base de datos

Será preferible para cargas reproducibles.

---

# Consulta de extracción

Toda consulta deberá:

- versionarse;
- auditarse;
- ser de solo lectura;
- registrar parámetros.

---

# Change Data Capture

CDC podrá utilizarse para ingesta incremental.

Deberá preservar:

- operación;
- clave;
- orden;
- timestamp;
- transacción.

---

# Operaciones CDC

```text
insert
update
delete
snapshot
```

---

# Eliminaciones

Una eliminación en la fuente no deberá provocar necesariamente una eliminación física en el SGCC.

Podrá generar:

```text
source_item_deleted
```

para evaluación posterior.

---

# APIs

Las APIs podrán utilizar:

- REST;
- GraphQL;
- SOAP;
- RPC;
- protocolos específicos.

---

# Contrato de API externa

El registro deberá incluir:

- endpoint;
- versión;
- autenticación;
- paginación;
- límites;
- esquema;
- términos de uso;
- disponibilidad.

---

# Versionado de API externa

Los cambios de versión deberán tratarse como posibles cambios incompatibles del conector.

---

# Respuestas parciales

Una API puede devolver datos incompletos.

El conector deberá distinguir:

- respuesta vacía;
- página final;
- error parcial;
- campo omitido;
- dato no autorizado.

---

# GraphQL externo

El importador deberá versionar:

- consulta;
- variables;
- fragmentos;
- esquema esperado.

---

# SOAP

Deberá conservar:

- WSDL;
- operación;
- namespaces;
- versión;
- fault.

---

# Web

La ingesta web deberá diferenciar:

- adquisición puntual;
- crawling;
- monitorización;
- importación autorizada.

---

# Crawling

Todo crawler deberá respetar:

- alcance;
- frecuencia;
- exclusiones;
- términos;
- robots;
- límites;
- identificación.

---

# Frontera del crawler

Deberá definirse mediante:

- dominios;
- rutas;
- profundidad;
- tipos;
- patrones.

---

# Canonical URL

Cuando esté disponible, deberá conservarse.

---

# Redirecciones

Deberán registrarse.

---

# Contenido duplicado

El sistema podrá detectar contenido idéntico publicado en varias URL.

No deberá fusionar automáticamente sus fuentes.

---

# RSS y Atom

Los feeds deberán conservar:

- identificador de entrada;
- título;
- fecha;
- actualización;
- autor;
- enlace;
- contenido;
- categorías.

---

# Actualización de entrada

Una entrada existente puede modificarse.

Deberá conservarse historial cuando sea posible.

---

# Repositorios Git

El conector Git podrá adquirir:

- archivos;
- árbol;
- commit;
- tag;
- rama;
- historial.

---

# Unidad de versión Git

La versión reproducible deberá fijarse mediante commit.

No mediante una rama mutable.

---

# Cambios Git

La ingesta incremental podrá utilizar:

- archivos añadidos;
- modificados;
- renombrados;
- eliminados.

---

# Renombrado

Un cambio de ruta no deberá crear automáticamente una nueva entidad documental si la identidad del documento se conserva.

---

# Issues y Pull Requests

Podrán ser fuentes separadas.

No deberán mezclarse automáticamente con documentación canónica.

---

# Correo electrónico

Un conector de correo podrá extraer:

- remitente;
- destinatarios;
- fecha;
- asunto;
- cuerpo;
- adjuntos;
- hilo.

Deberá aplicar políticas reforzadas de privacidad.

---

# Adjuntos

Cada adjunto deberá convertirse en una unidad de fuente independiente relacionada con el mensaje.

---

# Hilos

Deberá conservarse el orden conversacional.

---

# Documentos ofimáticos

Los formatos ofimáticos podrán incluir:

- DOCX;
- ODT;
- PPTX;
- ODP;
- XLSX;
- ODS.

---

# Extracción de documentos de texto

Deberá conservar:

- títulos;
- párrafos;
- tablas;
- notas;
- comentarios;
- imágenes;
- secciones;
- estilos semánticos.

---

# Extracción de presentaciones

Deberá conservar:

- diapositiva;
- orden;
- cuadros de texto;
- notas;
- imágenes;
- gráficos;
- relaciones espaciales.

---

# Extracción de hojas de cálculo

Deberá seguir las reglas definidas para celdas, fórmulas y rangos.

---

# OCR

El OCR convierte contenido visual en texto.

Su resultado deberá considerarse:

```text
transcripción automática
```

no:

```text
fuente original
```

---

# Artefacto OCR

Formato recomendado:

```text
OCR-ART-XXXXXX
```

---

# Contrato OCR

```yaml
id: OCR-ART-000041

source_artifact: ACQ-ART-000922

engine:
  id: OCR-ENGINE-0001
  version: 2.4.0

language:
  - es

text_blocks: [...]

confidence:
  average: 0.91

generated_at: 2026-08-01T14:00:00+02:00
```

---

# Posiciones OCR

Cada bloque deberá conservar:

- página;
- coordenadas;
- orientación;
- confianza;
- orden estimado.

---

# Confianza OCR

Podrá registrarse a nivel de:

- documento;
- página;
- línea;
- palabra;
- carácter.

---

# Umbral OCR

Contenido por debajo del umbral podrá:

- marcarse;
- excluirse;
- requerir revisión;
- conservarse como incierto.

---

# Corrección OCR

Las correcciones humanas deberán conservar:

- valor original;
- valor corregido;
- responsable;
- fecha;
- motivo.

---

# OCR multilingüe

Deberá declarar los idiomas esperados.

---

# Texto manuscrito

La extracción deberá utilizar un perfil específico y mayor revisión.

---

# Imágenes

Las imágenes podrán contener:

- texto;
- ingredientes;
- platos;
- etiquetas;
- tablas;
- diagramas;
- códigos.

---

# Metadatos de imagen

Podrán extraerse:

- formato;
- dimensiones;
- orientación;
- fecha;
- perfil de color;
- metadatos EXIF autorizados.

---

# Privacidad de metadatos

Los metadatos de ubicación deberán eliminarse o restringirse cuando no sean necesarios.

---

# Clasificación visual

Un modelo podrá proponer:

- tipo de plato;
- ingrediente;
- utensilio;
- documento;
- etiqueta.

Estas propuestas deberán marcarse como probabilísticas.

---

# Detección de objetos

Cada detección deberá incluir:

- clase;
- región;
- puntuación;
- modelo;
- versión.

---

# Etiquetas de producto

Podrán procesarse mediante:

```text
Imagen
↓
OCR
↓
Estructuración
↓
Normalización
```

---

# Códigos de barras y QR

Podrán extraerse como identificadores técnicos.

El contenido recuperado mediante el código deberá conservar su propia procedencia.

---

# Audio

La ingesta de audio podrá incluir:

- metadatos;
- transcripción;
- segmentación;
- hablantes;
- marcas temporales.

---

# Artefacto de transcripción

```yaml
id: TRANSCRIPT-000041

source: ACQ-ART-AUDIO-001

engine:
  id: ASR-ENGINE-0001
  version: 1.3.0

segments:
  - start: 00:00:12.400
    end: 00:00:18.900
    speaker: speaker_1
    text: Añadimos el miso fuera del hervor.
    confidence: 0.94
```

---

# Identificación de hablantes

Será opcional y deberá respetar privacidad.

---

# Música y ruido

Deberán registrarse cuando afecten a la calidad de la transcripción.

---

# Vídeo

La ingesta de vídeo podrá combinar:

- audio;
- transcripción;
- frames;
- subtítulos;
- capítulos;
- objetos;
- texto en pantalla.

---

# Timeline

Todo contenido extraído deberá conservar su posición temporal.

---

# Subtítulos

Deberá distinguirse entre:

- subtítulo original;
- subtítulo automático;
- transcripción generada.

---

# Frames

No deberán extraerse todos los frames por defecto.

Podrán seleccionarse mediante:

- intervalos;
- cambios de escena;
- detección de texto;
- eventos.

---

# Recetas audiovisuales

Podrán generar propuestas de:

- ingredientes;
- pasos;
- técnicas;
- tiempos;
- temperaturas.

Estas propuestas requerirán normalización y validación posteriores.

---

# Datos geográficos

Las fuentes geográficas podrán incluir:

- países;
- regiones;
- coordenadas;
- divisiones administrativas;
- nombres históricos.

---

# Precisión geográfica

Deberá declararse.

---

# Datos temporales

Las fechas podrán presentarse como:

- instante;
- día;
- intervalo;
- periodo;
- fecha aproximada.

La extracción no deberá inventar precisión inexistente.

---

# Archivos comprimidos

Un archivo comprimido deberá tratarse como fuente compuesta.

---

# Seguridad de archivos comprimidos

Deberán prevenirse:

- zip bombs;
- rutas relativas maliciosas;
- archivos excesivos;
- formatos inesperados;
- ejecutables.

---

# Archivos anidados

La profundidad deberá limitarse.

---

# Binarios no soportados

Deberán:

- conservarse;
- clasificarse;
- marcarse como no extraídos;
- generar diagnóstico.

---

# Streaming

Una fuente streaming produce eventos de forma continua.

---

# Evento de ingesta

Cada evento deberá incluir:

- identificador;
- clave;
- secuencia;
- timestamp;
- fuente;
- operación;
- payload;
- versión.

---

# Contrato de evento de fuente

```yaml
event:
  id: SRC-EVT-000041
  source: SRC-STREAM-0001

  key: REC-0009
  sequence: 88341
  timestamp: 2026-08-01T15:00:00Z

  operation: update

  payload:
    ...
```

---

# Garantías de entrega

Podrán existir:

```text
at_most_once
at_least_once
effectively_once
```

La ingesta deberá ser idempotente.

---

# Orden

Cuando el orden sea relevante, deberá conservarse por:

- clave;
- partición;
- secuencia;
- transacción.

---

# Eventos tardíos

Deberán gestionarse mediante:

- ventanas;
- watermark;
- corrección;
- reordenación;
- historial.

---

# Batch

La ingesta batch procesa conjuntos delimitados.

---

# Lote

Formato recomendado:

```text
ING-BATCH-XXXXXX
```

---

# Contrato de lote

```yaml
id: ING-BATCH-000041

source: SRC-DATASET-0007

items:
  total: 2500

status: running

execution:
  pipeline: PIPELINE-CSV
  started_at: 2026-08-01T08:00:00Z
```

---

# Chunking de lote

Los lotes podrán dividirse para:

- memoria;
- paralelismo;
- reintentos;
- control de errores.

---

# Atomicidad de lote

Podrá configurarse como:

```text
all_or_nothing
partial_commit
quarantine_failed
```

---

# Ingesta incremental

La ingesta incremental procesa únicamente diferencias.

---

# Tipos de cambio

```text
created
updated
renamed
deleted
restored
unchanged
```

---

# Change Set

Formato recomendado:

```text
CHANGESET-XXXXXX
```

---

## Contrato de Change Set

```yaml
id: CHANGESET-000041

source: SRC-REPOSITORY-0001

from_version: commit-a
to_version: commit-b

changes:
  created:
    - docs/ingredients/ING-0041.md

  updated:
    - docs/recipes/REC-0009.md

  deleted:
    - docs/archive/OLD-0001.md
```

---

# Detección de cambios

Podrá basarse en:

- versión;
- timestamp;
- hash;
- ETag;
- CDC;
- eventos;
- comparación.

---

# Cambio de metadatos

Deberá distinguirse de un cambio de contenido.

---

# Cambio semántico potencial

Una modificación textual podrá producir o no un cambio semántico.

La determinación definitiva corresponderá a fases posteriores.

---

# Borrado en origen

Un borrado deberá producir un evento de evaluación.

No deberá eliminar inmediatamente:

- documento;
- entidad;
- afirmaciones;
- historial.

---

# Fuente no disponible

Una fuente temporalmente inaccesible no deberá interpretarse como eliminada.

---

# Plugins

El sistema podrá ampliarse mediante plugins de conectores y extractores.

---

# Manifiesto de plugin

```yaml
plugin:
  id: PLUGIN-INGESTION-0001
  version: 1.0.0

  provides:
    connectors:
      - CONNECTOR-CUSTOM-0001

    extractors:
      - EXTRACTOR-CUSTOM-0001

  permissions:
    network: restricted
    filesystem: read_only
```

---

# Aislamiento de plugins

Los plugins deberán ejecutarse con:

- permisos mínimos;
- límites de memoria;
- timeout;
- acceso restringido;
- validación de salida.

---

# Firma de plugin

Podrá exigirse firma para plugins de producción.

---

# Compatibilidad de plugin

Deberá declarar versiones compatibles del:

- Ingestion Engine;
- esquema de artefactos;
- runtime;
- API de plugins.

---

# Marketplace o catálogo

Los plugins no deberán instalarse automáticamente desde fuentes no verificadas.

---

# Extracción asistida por IA

Los modelos de IA podrán ayudar en:

- clasificación de formato;
- segmentación;
- OCR;
- transcripción;
- identificación de campos;
- extracción de entidades;
- detección de tablas.

---

# Resultado de IA

Todo resultado deberá registrar:

- modelo;
- versión;
- prompt o configuración;
- entrada;
- puntuación;
- fecha;
- estado.

---

# IA como propuesta

Los resultados semánticos de IA deberán considerarse:

```text
proposed
```

hasta su validación.

---

# Prompt injection en fuentes

El contenido adquirido puede contener instrucciones maliciosas.

Dichas instrucciones deberán tratarse como datos.

No deberán modificar:

- pipeline;
- políticas;
- permisos;
- configuración;
- comportamiento de agentes.

---

# Adquisición manual

Los usuarios podrán subir fuentes manualmente.

---

# Metadatos requeridos

La carga manual deberá solicitar:

- tipo;
- origen;
- autor cuando se conozca;
- licencia;
- sensibilidad;
- finalidad.

---

# Fuentes desconocidas

Cuando no pueda determinarse el formato, el sistema deberá:

- conservar el artefacto;
- detectar media type;
- generar diagnóstico;
- impedir extracción no segura;
- permitir revisión.

---

# Detección de tipo

Podrá utilizar:

- extensión;
- MIME;
- firma binaria;
- contenido;
- configuración.

La extensión no deberá considerarse suficiente.

---

# Codificación de texto

El extractor deberá detectar o recibir:

- UTF-8;
- UTF-16;
- ISO-8859-1;
- otras codificaciones.

La conversión deberá registrarse.

---

# Caracteres inválidos

Podrán:

- rechazarse;
- reemplazarse;
- conservarse como bytes;
- producir advertencia.

---

# Idioma

El sistema podrá detectar idioma.

La detección deberá considerarse probabilística.

---

# Contenido multilingüe

Un mismo documento podrá contener varios idiomas.

La extracción deberá permitir anotación por fragmentos.

---

# Licencia y derechos

Toda fuente deberá declarar, cuando proceda:

- licencia;
- titular;
- atribución;
- restricciones;
- fecha;
- jurisdicción.

---

# Fuente sin licencia conocida

No deberá publicarse externamente hasta su revisión.

---

# Uso permitido

Podrá clasificarse:

```text
internal_only
redistributable
transformable
citation_only
unknown
prohibited
```

---

# Atribución

La cadena de procedencia deberá conservar la atribución requerida.

---

# Contenido protegido

La ingesta interna no implica autorización para redistribuir.

---

# Retención del original

La política deberá considerar:

- licencia;
- tamaño;
- privacidad;
- reproducibilidad;
- valor histórico.

---

# Seguridad de fuentes

Toda fuente deberá considerarse potencialmente no confiable.

---

# Riesgos

- malware;
- macros;
- scripts;
- archivos corruptos;
- contenido excesivo;
- rutas maliciosas;
- payloads de deserialización;
- prompt injection;
- datos personales;
- secretos.

---

# Escaneo de seguridad

Podrá incluir:

- antivirus;
- detección de macros;
- validación de formato;
- límites;
- sandbox;
- descompresión segura.

---

# Macros

No deberán ejecutarse durante la extracción.

---

# Enlaces externos

No deberán seguirse automáticamente salvo configuración del pipeline.

---

# Recursos remotos incrustados

El extractor deberá decidir si:

- los descarga;
- los referencia;
- los bloquea;
- los pone en cuarentena.

---

# Cuarentena

Las fuentes sospechosas deberán almacenarse en un ámbito aislado.

Estado recomendado:

```text
quarantined
```

---

# Política de tamaño

Deberán existir límites por:

- archivo;
- fuente;
- lote;
- ejecución;
- contenido descomprimido.

---

# Datos personales

Las fuentes personales deberán aplicar:

- minimización;
- finalidad;
- retención;
- acceso;
- eliminación;
- segregación.

---

# Secretos detectados

Si una fuente contiene credenciales o secretos, deberá:

- bloquearse;
- redaccionarse;
- notificarse;
- ponerse en cuarentena;
- impedir publicación.

---

# Diagnósticos de adquisición

Los diagnósticos podrán incluir:

```text
SOURCE_UNAVAILABLE
AUTHENTICATION_FAILED
RATE_LIMITED
CHECKSUM_MISMATCH
UNSUPPORTED_MEDIA_TYPE
SOURCE_CHANGED_DURING_READ
```

---

# Diagnósticos de extracción

Ejemplos:

```text
INVALID_FRONT_MATTER
UNREADABLE_PDF_PAGE
OCR_LOW_CONFIDENCE
TABLE_STRUCTURE_AMBIGUOUS
UNKNOWN_ENCODING
PARTIAL_EXTRACTION
```

---

# Contrato de diagnóstico

```yaml
diagnostic:
  id: DIA-000041
  code: OCR_LOW_CONFIDENCE
  severity: warning

  target: OCR-ART-000041

  message:
    es: La confianza media del OCR es inferior al umbral recomendado.

  evidence:
    confidence: 0.62
    threshold: 0.80
```

---

# Severidad

Valores:

```text
info
warning
error
critical
```

---

# Error recuperable

Permite reintento o degradación.

---

# Error no recuperable

Requiere:

- cancelar;
- poner en cuarentena;
- corregir configuración;
- revisión manual.

---

# Política por elemento

En un lote, un elemento fallido podrá:

- bloquear todo el lote;
- aislarse;
- omitirse con advertencia;
- reintentarse.

---

# Dead-letter queue

Las fuentes o eventos no procesables podrán enviarse a una cola de errores.

Deberá conservar:

- contenido;
- motivo;
- intentos;
- ejecución;
- fecha;
- próxima acción.

---

# Idempotencia de extracción

La clave podrá construirse a partir de:

```text
source_artifact_hash
+
extractor_id
+
extractor_version
+
configuration_hash
```

---

# Hash de extracción

Permitirá detectar si la salida ha cambiado.

---

# Determinismo

Los extractores deterministas deberán producir exactamente la misma salida.

Los extractores probabilísticos deberán registrar:

- semilla cuando exista;
- modelo;
- versión;
- parámetros.

---

# Reextracción

Será necesaria cuando cambie:

- extractor;
- configuración;
- esquema;
- modelo;
- política;
- fuente.

---

# Compatibilidad de artefactos

Un extractor deberá declarar la versión del esquema de salida.

---

# Migración de artefactos

Los artefactos antiguos podrán:

- migrarse;
- reextraerse;
- mantenerse para auditoría.

---

# Calidad de extracción

La calidad podrá evaluarse mediante:

- cobertura;
- precisión;
- pérdida;
- confianza;
- estructura;
- consistencia;
- posición de origen;
- completitud.

---

# Cobertura

Porcentaje de contenido procesado.

---

# Precisión

Corrección del contenido extraído.

---

# Fidelidad estructural

Grado en que se conserva la organización del origen.

---

# Calidad posicional

Capacidad de localizar el contenido en la fuente.

---

# Métricas de extracción

Ejemplos:

- fuentes adquiridas;
- bytes procesados;
- documentos extraídos;
- páginas;
- tablas;
- imágenes;
- errores;
- advertencias;
- confianza OCR;
- duración;
- tasa de reintentos.

---

# Pruebas de conectores

Todo conector estable deberá probar:

- autenticación;
- descubrimiento;
- lectura;
- paginación;
- timeout;
- reintento;
- cambio de versión;
- error;
- idempotencia.

---

# Pruebas de extractores

Todo extractor estable deberá incluir:

- documento mínimo;
- documento completo;
- formato inválido;
- codificación distinta;
- contenido vacío;
- estructura compleja;
- archivo grande;
- caso con pérdida;
- golden artifact.

---

# Golden Artifact

Un Golden Artifact define la salida esperada para una fuente conocida.

```yaml
golden_extraction:
  id: GOLDEN-EXT-MARKDOWN-0001

  source_artifact: TEST-ACQ-0001
  extractor: EXTRACTOR-MARKDOWN-0001

  expected:
    headings: 8
    tables: 2
    links: 14
    front_matter_id: REC-0009
```

---

# Pruebas de regresión

Deberán detectar cambios inesperados en:

- texto;
- estructura;
- metadatos;
- posiciones;
- diagnósticos;
- hashes;
- cobertura.

---

# Benchmarks

Podrán medir:

- documentos por segundo;
- MB por segundo;
- latencia;
- memoria;
- escalabilidad;
- OCR por página;
- tamaño de lote.

---

# Perfil mínimo de fuentes y extracción

La primera implementación de NovaCoquinaria debería soportar:

- archivos Markdown;
- JSON;
- YAML;
- CSV;
- repositorio Git;
- descubrimiento incremental;
- extracción de Front Matter;
- extracción de estructura Markdown;
- hashes;
- procedencia;
- diagnósticos;
- reintentos básicos.

---

# Perfil estructurado

Añadirá:

- HTML;
- XML;
- bases de datos;
- APIs;
- documentos ofimáticos;
- PDF digital;
- hojas de cálculo;
- lotes;
- plugins.

---

# Perfil multimedia

Añadirá:

- OCR;
- imágenes;
- audio;
- vídeo;
- transcripciones;
- códigos;
- texto en pantalla.

---

# Perfil avanzado

Añadirá:

- streaming;
- CDC;
- crawling controlado;
- clasificación mediante IA;
- extracción multimodal;
- conectores externos complejos;
- sandbox avanzado.

---

# Implementación inicial recomendada

La primera implementación práctica del Ingestion Engine debería centrarse en el repositorio documental existente:

```text
Repositorio Git
      ↓
Descubrimiento de archivos Markdown
      ↓
Adquisición por commit
      ↓
Hash de contenido
      ↓
Extracción de Front Matter
      ↓
Construcción de AST
      ↓
Extracción de secciones, enlaces y tablas
      ↓
Artefacto extraído
```

Este alcance permitirá consolidar el pipeline utilizando fuentes:

- controladas;
- versionadas;
- reproducibles;
- ya gobernadas por el proyecto.

No será necesario implementar inicialmente:

- crawling web;
- OCR;
- audio;
- vídeo;
- streaming;
- APIs externas;
- CDC;
- plugins de terceros;
- clasificación visual;
- transcripción automática.

---

# Ejemplo integrado — Fuente Markdown

```yaml
source:
  id: SRC-000142
  type: markdown_document

  location:
    scheme: repository
    uri: docs/recipes/REC-0009.md

  version:
    type: git_commit
    value: 6fa8c42

  status: active
```

---

# Ejemplo integrado — Adquisición

```yaml
acquired_artifact:
  id: ACQ-ART-000421

  source: SRC-000142
  execution: ING-EXEC-000041
  connector: CONNECTOR-GIT-0001

  media_type: text/markdown
  size_bytes: 14231

  integrity:
    algorithm: sha256
    hash: sha256:...

  acquired_at: 2026-08-01T12:00:00+02:00
```

---

# Ejemplo integrado — Extracción

```yaml
extracted_artifact:
  id: EXT-ART-000421

  source_artifact: ACQ-ART-000421
  extractor: EXTRACTOR-MARKDOWN-0001

  document:
    front_matter:
      id: REC-0009
      type: recipe
      status: active

    structure:
      headings: 8
      paragraphs: 31
      lists: 6
      tables: 2
      links: 14

  diagnostics: []

  extraction:
    schema_version: 1.0.0
    completed_at: 2026-08-01T12:00:01+02:00
```

---

# Ejemplo integrado — PDF escaneado

```yaml
source:
  id: SRC-000901
  type: scanned_pdf

acquired_artifact:
  id: ACQ-ART-000901
  source: SRC-000901
  media_type: application/pdf

extraction:
  primary_extractor: EXTRACTOR-PDF-0001
  fallback:
    - OCR-ENGINE-0001

output:
  text_origin: ocr
  pages: 12

confidence:
  average: 0.87

diagnostics:
  - code: OCR_LOW_CONFIDENCE
    severity: warning
    pages:
      - 7
```

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Utilizar la ruta como única identidad

La ruta puede cambiar.

---

## Sobrescribir la fuente original

Destruye reproducibilidad.

---

## Mezclar conector y extractor

Acopla adquisición e interpretación.

---

## Inferir formato únicamente por extensión

Puede provocar procesamiento inseguro o incorrecto.

---

## Descargar sin comprobar integridad

Impide detectar cambios o corrupción.

---

## Seguir enlaces web sin frontera

Puede producir crawling ilimitado.

---

## Ejecutar scripts de las fuentes

Introduce riesgos de seguridad.

---

## Ejecutar macros ofimáticas

No deberán formar parte de la extracción.

---

## Conservar secretos en configuración versionada

Compromete seguridad.

---

## Tratar OCR como texto confirmado

El OCR es una transcripción probabilística.

---

## Eliminar contenido de baja confianza

Deberá conservarse y marcarse cuando sea posible.

---

## Fusionar fuentes por contenido idéntico

Pueden tener distinta procedencia, licencia o autoridad.

---

## Interpretar una fuente no disponible como eliminada

Puede invalidar conocimiento incorrectamente.

---

## Procesar archivos comprimidos sin límites

Expone el sistema a ataques.

---

## Ignorar licencias

La adquisición técnica no autoriza la reutilización.

---

## Importar datos personales al grafo global

Deben permanecer segregados.

---

## Usar IA sin registrar modelo y versión

Impide reproducibilidad.

---

## Permitir que el contenido controle el pipeline

Las fuentes son datos, no instrucciones.

---

## No conservar posiciones de origen

Dificulta trazabilidad y revisión.

---

## Reintentar indefinidamente

Puede saturar el sistema o el proveedor.

---

## No versionar consultas externas

Impide reproducir ingestas.

---

## Interpretar borrado como eliminación física inmediata

Debe evaluarse dentro del ciclo de vida del conocimiento.

---

## Procesar todo mediante OCR

El texto digital deberá extraerse directamente cuando exista.

---

## Extraer únicamente texto de documentos estructurados

Puede perder tablas, jerarquías y relaciones.

---

# Reglas mínimas de conformidad

---

## Fuente identificada

Toda adquisición deberá referenciar una fuente registrada o provisional.

---

## Conector registrado

Todo conector utilizado deberá tener identidad y versión.

---

## Extractor registrado

Todo extractor deberá tener identidad y versión.

---

## Integridad calculada

Todo artefacto adquirido deberá poseer una huella cuando sea técnicamente posible.

---

## Media type conocido

Deberá declararse el tipo real o marcarse como desconocido.

---

## Procedencia conservada

Todo artefacto extraído deberá enlazar con el artefacto adquirido.

---

## Diagnósticos preservados

Los errores y advertencias no deberán descartarse.

---

## Pérdidas declaradas

Toda pérdida conocida deberá registrarse.

---

## Licencia registrada

Las fuentes externas deberán declarar licencia o estado desconocido.

---

## Sensibilidad registrada

Las fuentes personales o restringidas deberán clasificarse.

---

## Ejecución segura

Los formatos no confiables deberán procesarse de forma aislada.

---

## Salida versionada

Todo artefacto extraído deberá indicar la versión de su esquema.

---

# Conformidad de fuente

Una fuente será conforme cuando:

- posea identidad;
- declare tipo;
- tenga localización o referencia;
- tenga estado;
- conserve versión cuando exista;
- declare sensibilidad;
- declare licencia cuando proceda;
- pueda auditarse.

---

# Conformidad de conector

Un conector será conforme cuando:

- tenga identidad;
- esté versionado;
- declare capacidades;
- aplique límites;
- gestione errores;
- preserve integridad;
- respete seguridad;
- disponga de pruebas.

---

# Conformidad de extractor

Un extractor será conforme cuando:

- declare formatos de entrada;
- produzca un esquema versionado;
- preserve procedencia;
- genere diagnósticos;
- declare pérdidas;
- sea reproducible;
- disponga de pruebas y Golden Artifacts.

---

# Conformidad de adquisición

Una adquisición será conforme cuando:

- identifique la fuente;
- identifique el conector;
- registre ejecución;
- calcule integridad;
- conserve fecha;
- respete permisos;
- no modifique el original.

---

# Conformidad de extracción

Una extracción será conforme cuando:

- enlace con el artefacto adquirido;
- identifique el extractor;
- conserve estructura relevante;
- conserve posiciones cuando sea posible;
- declare confianza;
- declare pérdidas;
- produzca diagnósticos.

---

# Lista de comprobación

Antes de entregar un artefacto a la fase de normalización deberá comprobarse:

```text
[ ] La fuente está identificada.
[ ] El acceso está autorizado.
[ ] La licencia está registrada o marcada como desconocida.
[ ] El conector está registrado y versionado.
[ ] El artefacto original se conserva o puede recuperarse.
[ ] La integridad ha sido calculada.
[ ] El media type ha sido validado.
[ ] El extractor es compatible.
[ ] La extracción conserva la estructura relevante.
[ ] Las posiciones de origen están disponibles cuando procede.
[ ] Los diagnósticos se han registrado.
[ ] Las pérdidas conocidas están declaradas.
[ ] La sensibilidad está clasificada.
[ ] No se han ejecutado contenidos activos no autorizados.
[ ] La salida utiliza un esquema versionado.
```

---

# Arquitectura de fuentes y extracción

```text
┌───────────────────────────────────────────────┐
│                  Fuentes                     │
│                                               │
│ Git · Archivos · APIs · Web · BBDD · Media   │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Source Registry                │
│                                               │
│ Identidad · Tipo · Licencia · Sensibilidad   │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                  Connectors                   │
│                                               │
│ Descubrimiento · Acceso · Lectura · Cambios  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Acquired Artifacts               │
│                                               │
│ Bytes · Registros · Hash · Versión · Origen  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                  Extractors                   │
│                                               │
│ Parsing inicial · Estructura · Posiciones     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Extracted Artifacts              │
│                                               │
│ Contenido · Metadatos · Recursos · Diagnóstico│
└───────────────────────────────────────────────┘
```

---

# Transición hacia la Parte III

Esta segunda parte ha definido:

- el modelo formal de fuente;
- el catálogo y ciclo de vida de fuentes;
- las unidades de fuente;
- el descubrimiento;
- los conectores;
- los importadores;
- la adquisición;
- los artefactos adquiridos;
- los extractores;
- los artefactos extraídos;
- la extracción de Markdown, PDF, HTML, XML, JSON, YAML y CSV;
- la ingesta desde hojas de cálculo, bases de datos y APIs;
- la ingesta web, Git, correo y documentos ofimáticos;
- OCR;
- imágenes;
- audio;
- vídeo;
- streaming;
- batch;
- incrementalidad;
- plugins;
- IA asistida;
- seguridad;
- licencias;
- diagnósticos;
- pruebas;
- perfiles de capacidad.

La Parte III desarrollará la transformación de los artefactos extraídos en una representación interna homogénea mediante:

- parsing;
- AST;
- limpieza;
- canonicalización;
- normalización de texto;
- normalización de fechas y unidades;
- Front Matter;
- metadatos;
- segmentación;
- identificación de documentos;
- generación de IDs;
- extracción de componentes;
- extracción de entidades;
- extracción de relaciones;
- resolución de identidad;
- deduplicación;
- enriquecimiento;
- alineación con la ontología;
- construcción del Knowledge Package.

---

# Conclusión

Las fuentes, los conectores y los extractores constituyen la frontera entre el entorno exterior y el sistema de conocimiento de NovaCoquinaria.

Esta frontera deberá impedir que la heterogeneidad, la ambigüedad o la inseguridad de las fuentes se propaguen directamente hacia el Knowledge Graph.

El ciclo definido puede resumirse así:

```text
Fuente registrada
      ↓
Conector autorizado
      ↓
Artefacto adquirido
      ↓
Integridad verificada
      ↓
Extractor compatible
      ↓
Artefacto extraído
      ↓
Diagnósticos y procedencia
```

El conector obtiene.

El extractor interpreta.

La fuente conserva su identidad.

El artefacto adquirido conserva el original.

El artefacto extraído conserva contenido y estructura.

Ninguno de estos elementos constituye todavía conocimiento canónico.

Su función consiste en proporcionar una base fiel, trazable y segura para que la siguiente fase pueda normalizar, enriquecer y estructurar la información conforme al modelo de conocimiento del SGCC.

Con esta segunda parte queda definida la entrada física y documental del Ingestion Engine.

La siguiente parte establecerá cómo estos artefactos heterogéneos se convierten en representaciones normalizadas, entidades candidatas, relaciones candidatas y paquetes de conocimiento preparados para su validación.

---

# Parte III — Normalización, representación interna y enriquecimiento semántico

---

# Introducción

Las partes anteriores han definido cómo el Ingestion Engine:

- descubre fuentes;
- adquiere contenido;
- preserva procedencia;
- extrae información documental.

Sin embargo, el resultado de la extracción continúa siendo heterogéneo.

Cada extractor produce representaciones diferentes.

Un documento Markdown, un PDF, una API REST o un CSV poseen estructuras completamente distintas.

El objetivo de esta tercera parte consiste en transformar todas esas representaciones en un modelo interno uniforme sobre el que el resto del Knowledge Engine pueda trabajar.

Conceptualmente:

```text
Extracted Artifact
        │
        ▼
Normalization Engine
        │
        ▼
Internal Representation
        │
        ▼
Semantic Enrichment
        │
        ▼
Knowledge Package
```

A partir de este punto comienza la transición desde el mundo documental hacia el mundo semántico.

---

# Objetivos

Esta parte persigue:

- definir la representación interna común;
- establecer el proceso de normalización;
- unificar estructuras heterogéneas;
- resolver formatos;
- normalizar metadatos;
- generar identidades estables;
- preparar entidades y relaciones candidatas;
- enriquecer semánticamente el contenido;
- construir el Knowledge Package.

---

# Principios

Toda normalización deberá respetar:

- reproducibilidad;
- trazabilidad;
- determinismo;
- conservación del significado;
- mínima pérdida de información;
- independencia del formato original;
- independencia tecnológica.

---

# Concepto de normalización

Normalizar significa transformar múltiples representaciones distintas en una representación interna única.

No implica todavía:

- razonar;
- inferir;
- validar semánticamente.

Únicamente prepara el conocimiento.

---

# Pipeline conceptual

```text
Extracted Artifact

↓

Normalization

↓

Canonical Representation

↓

Metadata Enrichment

↓

Identity Resolution

↓

Entity Extraction

↓

Relationship Extraction

↓

Knowledge Package
```

---

# Normalization Engine

El **Normalization Engine** es responsable de:

- unificar formatos;
- limpiar inconsistencias;
- generar modelos internos;
- preparar el conocimiento para validación.

---

# Responsabilidades

Deberá encargarse de:

- normalizar texto;
- normalizar estructuras;
- normalizar metadatos;
- normalizar referencias;
- normalizar unidades;
- normalizar fechas;
- normalizar idiomas;
- normalizar identificadores.

---

# No responsabilidades

No deberá:

- ejecutar inferencias;
- modificar la ontología;
- validar restricciones;
- resolver conflictos lógicos.

---

# Representación interna

Toda fuente terminará representándose mediante un modelo común.

Conceptualmente:

```text
Document

Metadata

Sections

Blocks

Resources

References

Diagnostics
```

---

# Documento canónico

La representación documental interna constituye el formato oficial del pipeline.

Formato recomendado:

```text
Canonical Document
```

---

# Contrato conceptual

```yaml
document:

    id: DOC-00421

    metadata:

    content:

    sections:

    resources:

    diagnostics:
```

---

# Canonical Document

El Canonical Document deberá ser:

- independiente del origen;
- independiente del extractor;
- independiente del formato.

---

# Canonical Metadata

Los metadatos deberán almacenarse de forma uniforme.

Ejemplo:

```yaml
metadata:

    title:

    author:

    language:

    version:

    tags:

    collections:

    source:

    provenance:
```

---

# Normalización textual

Todo texto podrá pasar por varias transformaciones.

Ejemplos:

- codificación;
- espacios;
- saltos;
- caracteres invisibles;
- Unicode;
- puntuación.

---

# Unicode

Toda representación textual deberá utilizar Unicode normalizado.

---

# Espacios

Los espacios redundantes podrán eliminarse.

No deberán alterarse cuando modifiquen significado.

---

# Saltos de línea

Los distintos formatos deberán convertirse a un formato interno común.

---

# Codificación

Toda codificación original deberá registrarse.

La representación interna utilizará una codificación estándar.

---

# Caracteres especiales

Los caracteres especiales deberán preservarse.

No deberán sustituirse por aproximaciones.

---

# Emojis

Los emojis podrán conservarse.

La política dependerá del tipo documental.

---

# HTML embebido

El HTML embebido deberá:

- conservarse;
- eliminarse;
- transformarse;

según el perfil del pipeline.

---

# Limpieza

La limpieza podrá eliminar:

- elementos temporales;
- artefactos OCR;
- duplicados de formato;
- caracteres corruptos.

Toda limpieza deberá ser reproducible.

---

# Canonicalización

La canonicalización transforma múltiples variantes equivalentes en una representación estable.

Ejemplos:

```text
Kg

KG

kg
```

↓

```text
kg
```

---

# Unidades

Las unidades deberán representarse mediante un formato común.

Ejemplo:

```text
gramos

g

Gr.
```

↓

```text
g
```

---

# Fechas

Las fechas deberán almacenarse mediante un formato canónico.

---

# Horas

Las horas deberán conservar zona horaria cuando exista.

---

# Cantidades

Las cantidades deberán almacenarse separadas de sus unidades.

Ejemplo:

```yaml
amount: 250

unit: ml
```

---

# Idiomas

Los idiomas deberán utilizar identificadores normalizados.

---

# Etiquetas

Las etiquetas podrán:

- limpiarse;
- ordenar;
- deduplicarse.

---

# Referencias

Las referencias internas deberán convertirse a un formato uniforme.

---

# Recursos

Los recursos deberán conservar identidad propia.

Ejemplos:

```text
Imagen

Vídeo

Tabla

Código

Audio
```

---

# AST interno

La representación documental utilizará un árbol sintáctico común.

```text
Document

↓

Section

↓

Block

↓

Inline
```

---

# Tipos de bloque

Ejemplos:

```text
Paragraph

Heading

List

Table

Quote

Image

Code

Note
```

---

# Identidad de bloques

Formato recomendado:

```text
BLOCK-XXXXXX
```

---

# Contrato de bloque

```yaml
block:

    id: BLOCK-00041

    type: paragraph

    position:

    content:
```

---

# Posición

Todo bloque deberá mantener:

- documento;
- sección;
- orden;
- referencia al origen.

---

# Jerarquía

La jerarquía documental deberá conservarse.

---

# Segmentación

La segmentación divide el contenido en unidades independientes.

Ejemplo:

```text
Documento

↓

Secciones

↓

Bloques

↓

Fragmentos
```

---

# Fragmentos

Los fragmentos podrán convertirse posteriormente en unidades semánticas.

---

# Normalización estructural

Las distintas estructuras deberán converger.

Ejemplo:

```text
Markdown

↓

Heading

HTML

↓

H1

DOCX

↓

Título
```

↓

```text
Section
```

---

# Tablas

Las tablas deberán convertirse en un modelo común.

---

# Filas

Las filas conservarán identidad.

---

# Columnas

Las columnas conservarán nombre y posición.

---

# Celdas

Cada celda deberá ser identificable.

---

# Recursos embebidos

Las imágenes, vídeos y otros recursos deberán desacoplarse del documento.

---

# Referencias cruzadas

Las referencias internas deberán preservarse.

Ejemplo:

```text
REC-0008

↓

DocumentReference
```

---

# Enlaces externos

Los enlaces externos deberán registrarse.

No deberán resolverse automáticamente.

---

# Normalización de Front Matter

El Front Matter constituye el principal origen de metadatos estructurados.

---

# Validación inicial

Antes del enriquecimiento deberá comprobarse:

- sintaxis;
- claves duplicadas;
- tipos.

---

# Claves conocidas

Las claves estándar deberán mapearse directamente.

---

# Claves desconocidas

Podrán:

- conservarse;
- advertirse;
- rechazarse;

según política.

---

# Metadata Enrichment

Una vez normalizado el documento podrá enriquecerse.

---

# Objetivos

Añadir información no explícita pero derivable sin razonamiento complejo.

Ejemplos:

- idioma;
- longitud;
- categorías;
- resumen;
- palabras clave.

---

# Metadatos derivados

Ejemplos:

```yaml
statistics:

    words:

    paragraphs:

    headings:

    tables:
```

---

# Estadísticas

Podrán calcularse:

- número de palabras;
- longitud;
- enlaces;
- tablas;
- imágenes.

---

# Clasificación documental

El documento podrá clasificarse automáticamente.

Ejemplos:

```text
Recipe

Ingredient

Technique

Architecture

ADR

Specification
```

La clasificación deberá registrarse como propuesta hasta su validación.

---

# Palabras clave

Podrán extraerse automáticamente.

---

# Resumen

Podrá generarse un resumen preliminar.

Siempre deberá marcarse como generado automáticamente.

---

# Detección de idioma

La detección automática complementará el idioma declarado.

---

# Consistencia

Si el idioma declarado y el detectado difieren significativamente se generará una advertencia.

---

# Normalización de identificadores

Todos los identificadores deberán adoptar un formato estable.

---

# IDs SGCC

Ejemplos:

```text
REC-0004

ING-0012

TEC-0002

COL-0008
```

---

# Identidades temporales

Cuando un elemento carezca de ID podrá recibir un identificador provisional.

Ejemplo:

```text
TMP-ENTITY-00421
```

Posteriormente podrá resolverse.

---

# Resolución de identidad

La resolución intenta determinar si dos elementos representan la misma entidad.

No realiza todavía validación ontológica completa.

---

# Estrategias

Ejemplos:

- ID explícito;
- hash;
- nombre;
- URI;
- combinación de atributos.

---

# Coincidencia exacta

La estrategia preferida.

---

# Coincidencia aproximada

Podrá utilizar:

- distancia léxica;
- similitud;
- reglas.

Nunca deberá sustituir una identidad confirmada sin revisión.

---

# Deduplicación

La deduplicación elimina duplicados internos del Knowledge Package.

No modifica todavía el Knowledge Graph.

---

# Tipos de duplicados

Ejemplos:

```text
Documento

Bloque

Entidad

Relación

Referencia
```

---

# Política

Los duplicados podrán:

- fusionarse;
- conservarse;
- marcarse;
- rechazarse.

---

# Canonical Entity Candidate

Las entidades detectadas pasarán a representarse mediante candidatos.

Formato:

```text
ENTITY-CANDIDATE
```

---

# Contrato

```yaml
entity:

    id:

    label:

    confidence:

    source:
```

---

# Confidence

Toda extracción automática podrá registrar una confianza.

---

# Confidence no implica verdad

Representa únicamente la seguridad del proceso de extracción.

---

# Entity Extraction

La extracción de entidades identifica conceptos relevantes.

Ejemplos:

- ingredientes;
- recetas;
- técnicas;
- utensilios;
- documentos;
- personas.

---

# Entity Candidate

Las entidades detectadas aún no pertenecen al Knowledge Graph.

---

# Alias

Podrán detectarse alias.

Ejemplo:

```text
cebolla morada

↓

cebolla roja
```

La decisión final corresponderá posteriormente a la ontología.

---

# Normalización léxica

Podrán aplicarse:

- singular;
- plural;
- mayúsculas;
- tildes.

Siempre preservando el valor original.

---

# Relationship Candidate

Las relaciones también se extraerán como candidatos.

---

# Tipos

Ejemplos:

```text
contains

references

uses

derived_from

belongs_to
```

---

# Contrato

```yaml
relation:

    source:

    target:

    predicate:

    confidence:
```

---

# Relaciones explícitas

Provienen directamente del documento.

---

# Relaciones implícitas

No deberán generarse todavía.

Corresponden al Reasoner.

---

# Alineación preliminar con la ontología

La ontología podrá utilizarse para:

- reconocer clases;
- validar tipos básicos;
- identificar vocabulario.

No deberá realizar inferencias.

---

# Diccionarios

El pipeline podrá utilizar diccionarios terminológicos.

---

# Sinónimos

Los sinónimos podrán proponerse.

No deberán sustituirse automáticamente.

---

# Vocabularios controlados

Cuando existan deberán priorizarse.

---

# Recursos externos

El enriquecimiento podrá consultar recursos externos.

Toda consulta deberá registrarse.

---

# IA opcional

Los modelos de IA podrán ayudar en:

- clasificación;
- resumen;
- extracción;
- categorización.

Los resultados deberán marcarse como propuestas.

---

# Prompt Registry

Todo prompt utilizado deberá identificarse.

---

# Modelo

Toda ejecución IA registrará:

- modelo;
- versión;
- parámetros.

---

# Explicabilidad

Toda propuesta automática deberá poder justificarse.

---

# Knowledge Package Builder

El Builder reúne todos los artefactos generados.

---

# Componentes

```text
Documento

Metadatos

Entidades

Relaciones

Diagnósticos

Procedencia
```

---

# Contrato

```yaml
knowledge_package:

    id:

    document:

    metadata:

    entities:

    relations:

    provenance:

    diagnostics:
```

---

# Estado

Al finalizar esta fase el Knowledge Package estará preparado para la validación formal que se desarrollará en la Parte IV.

---

# Transición hacia la Parte IV

La siguiente parte abordará:

- validación estructural;
- validación semántica;
- restricciones;
- políticas;
- Quality Gates;
- publicación;
- rollback;
- snapshots;
- versionado.

---

# Conclusión

La normalización constituye el puente entre el contenido documental y el conocimiento estructurado.

Tras esta fase, todas las fuentes, independientemente de su formato original, convergen hacia una representación canónica común. Sobre ella pueden construirse entidades, relaciones y metadatos coherentes, preservando la procedencia y evitando introducir inferencias prematuras.

El resultado es un **Knowledge Package** consistente, enriquecido y preparado para afrontar las etapas de validación y publicación que permitirán su incorporación segura al Knowledge Graph del SGCC.

---

# Parte IV — Validación, publicación y control de calidad

---

# Introducción

Las partes anteriores han definido:

- la adquisición de fuentes;
- la extracción documental;
- la normalización;
- el enriquecimiento;
- la construcción del Knowledge Package.

A partir de este punto el conocimiento deja de ser simplemente información estructurada y comienza el proceso mediante el cual podrá convertirse en conocimiento oficial del SGCC.

No todo conocimiento extraído deberá incorporarse automáticamente al Knowledge Graph.

Antes deberá superar un conjunto de validaciones destinadas a garantizar:

- integridad;
- consistencia;
- coherencia semántica;
- calidad;
- gobernanza;
- trazabilidad.

Esta fase constituye el **Quality Gate** del Ingestion Engine.

---

# Objetivos

Esta parte define:

- el proceso de validación;
- los distintos niveles de validación;
- los motores participantes;
- las políticas de aceptación;
- los diagnósticos;
- los estados de validación;
- los Quality Gates;
- la publicación;
- el rollback;
- el versionado;
- la auditoría.

---

# Principios

Toda validación deberá respetar:

- reproducibilidad;
- determinismo;
- independencia del formato;
- explicabilidad;
- trazabilidad;
- auditabilidad;
- mínima intervención manual.

---

# Pipeline de validación

```text
Knowledge Package

↓

Structural Validation

↓

Semantic Validation

↓

Policy Validation

↓

Quality Gates

↓

Publication Decision

↓

Knowledge Graph
```

---

# Validation Engine

El **Validation Engine** es el componente encargado de decidir si un Knowledge Package puede incorporarse al ecosistema de conocimiento.

---

# Responsabilidades

Será responsable de:

- validar estructura;
- validar metadatos;
- validar referencias;
- validar componentes;
- validar relaciones;
- validar ontologías;
- validar restricciones;
- aplicar políticas;
- calcular calidad;
- emitir diagnósticos;
- decidir publicación.

---

# No responsabilidades

No deberá:

- modificar el contenido original;
- ejecutar inferencias complejas;
- resolver conflictos ontológicos;
- generar recomendaciones.

---

# Modelo de validación

Toda validación podrá producir uno de los siguientes resultados:

```text
Accepted

AcceptedWithWarnings

Rejected

Quarantined
```

---

# Accepted

El Knowledge Package puede publicarse.

---

# AcceptedWithWarnings

Puede publicarse pero conserva advertencias.

---

# Rejected

No podrá incorporarse.

---

# Quarantined

Quedará aislado para revisión posterior.

---

# Estados internos

Durante el proceso el paquete podrá encontrarse en:

```text
Pending

Running

Waiting

Completed

Failed

Published

RolledBack
```

---

# Validación estructural

La validación estructural comprueba la integridad formal del Knowledge Package.

Ejemplos:

- estructura YAML;
- Front Matter;
- identificadores;
- bloques;
- enlaces;
- recursos.

---

# Validaciones típicas

Ejemplos:

```text
Documento válido

ID válido

Tipo conocido

Bloques consistentes

Sin ciclos documentales

Referencias existentes
```

---

# Identificadores

Todos los IDs deberán:

- respetar el formato;
- ser únicos;
- pertenecer al tipo correcto.

---

# Referencias

Toda referencia deberá poder resolverse.

Ejemplo:

```text
REC-0007

↓

Documento existente
```

---

# Recursos

Las imágenes, vídeos y demás recursos deberán existir cuando sean obligatorios.

---

# Front Matter

Se validará:

- sintaxis;
- claves obligatorias;
- tipos;
- versiones.

---

# Metadata

Los metadatos deberán respetar los esquemas definidos.

---

# Validación documental

El documento deberá pertenecer a una categoría reconocida.

Ejemplo:

```text
Recipe

Ingredient

Technique

Specification

ADR
```

---

# Validación semántica

Una vez superada la estructura comienza la validación del significado.

---

# Objetivos

Comprobar que:

- entidades;
- relaciones;
- componentes;
- vocabulario;

sean compatibles con el modelo de conocimiento.

---

# Validación de entidades

Cada entidad deberá:

- poseer tipo;
- identidad;
- procedencia;
- metadatos mínimos.

---

# Validación de relaciones

Toda relación deberá verificar:

- origen;
- destino;
- predicado;
- cardinalidad;
- tipo.

---

# Relaciones inválidas

Ejemplo:

```text
Recipe

contains

Architecture
```

podrá resultar incompatible con la ontología.

---

# Ontology Validation

La ontología constituye la referencia principal.

Se comprobará:

- clases;
- propiedades;
- dominios;
- rangos.

---

# Tipos compatibles

Toda entidad deberá pertenecer a una clase conocida.

---

# Propiedades

Las propiedades deberán existir.

---

# Dominio

Ejemplo:

```text
contains
```

solo podrá utilizar determinados tipos de origen.

---

# Rango

Igualmente deberá respetarse el tipo del destino.

---

# Restricciones

Las restricciones podrán provenir de:

- ontología;
- políticas;
- reglas;
- colecciones;
- esquemas.

---

# Constraint Sets

Las restricciones se organizarán mediante conjuntos independientes.

Formato:

```text
CONSTRAINT-SET
```

---

# Tipos de restricción

Ejemplos:

```text
Obligatoria

Opcional

Experimental

Temporal
```

---

# SHACL

Cuando el Knowledge Graph utilice RDF o tecnologías equivalentes podrán aplicarse perfiles SHACL.

La arquitectura no dependerá obligatoriamente de SHACL.

---

# Reglas de negocio

También podrán existir restricciones específicas del dominio culinario.

Ejemplos:

- una receta debe contener al menos un ingrediente;
- una técnica no puede contener ingredientes;
- un ingrediente no pertenece simultáneamente a dos categorías excluyentes.

---

# Consistencia

La validación comprobará contradicciones conocidas.

---

# Consistencia documental

Ejemplo:

```text
status: archived

published: true
```

podrá generar advertencia.

---

# Consistencia temporal

Se validarán:

- versiones;
- fechas;
- vigencias.

---

# Consistencia de colecciones

Un documento deberá pertenecer únicamente a las colecciones compatibles.

---

# Consistencia de componentes

Los componentes deberán respetar las especificaciones correspondientes.

---

# Consistencia de relaciones

No deberán existir relaciones incompatibles.

---

# Consistencia de identidad

Dos entidades con el mismo ID no podrán representar conceptos distintos.

---

# Validación de calidad

Además de validar corrección se evaluará calidad.

---

# Indicadores

Ejemplos:

- completitud;
- coherencia;
- reutilización;
- documentación;
- cobertura;
- trazabilidad.

---

# Completitud

Se comprobará:

- metadatos;
- componentes;
- referencias;
- relaciones.

---

# Cobertura

Porcentaje de elementos correctamente descritos.

---

# Trazabilidad

Todo elemento deberá mantener:

- origen;
- ejecución;
- versión;
- procedencia.

---

# Explicabilidad

Todo rechazo deberá explicar:

- regla;
- restricción;
- evidencia.

---

# Diagnósticos

Todo resultado generará diagnósticos.

---

# Contrato

```yaml
diagnostic:

    id: DIA-00081

    severity: error

    code: INVALID_REFERENCE

    target:

    evidence:

    explanation:
```

---

# Severidad

Valores recomendados:

```text
Info

Warning

Error

Critical
```

---

# Evidence

Toda validación deberá aportar evidencia.

---

# Explicación

La explicación deberá ser comprensible para usuarios y desarrolladores.

---

# Agrupación

Los diagnósticos podrán agruparse por:

- documento;
- entidad;
- relación;
- regla;
- componente.

---

# Quality Score

El sistema podrá calcular una puntuación de calidad.

Ejemplo:

```text
0

↓

100
```

---

# Factores

Ejemplos:

- documentación;
- consistencia;
- completitud;
- referencias;
- diagnósticos.

---

# No sustituye las reglas

Una puntuación elevada nunca sustituirá una restricción obligatoria.

---

# Quality Gates

La publicación estará gobernada mediante puertas de calidad.

---

# Modelo

```text
Gate 1

↓

Gate 2

↓

Gate 3

↓

Publish
```

---

# Gate 1

Integridad documental.

---

# Gate 2

Consistencia semántica.

---

# Gate 3

Políticas del proyecto.

---

# Gate 4 (opcional)

Revisión humana.

---

# Políticas

Las políticas podrán exigir:

- revisión manual;
- aprobación;
- doble validación;
- firma.

---

# Publicación

La publicación incorpora oficialmente el conocimiento.

---

# Publication Engine

Será responsable de:

- insertar;
- actualizar;
- invalidar;
- versionar;
- registrar auditoría.

---

# Inserción

Un Knowledge Package nuevo generará nuevos elementos.

---

# Actualización

Una versión posterior actualizará los elementos existentes.

---

# Invalidación

Los elementos obsoletos podrán invalidarse.

No necesariamente eliminarse.

---

# Eliminación

La eliminación física será excepcional.

---

# Versionado

Toda publicación generará una nueva versión.

---

# Snapshot

Cada publicación podrá asociarse a un Snapshot.

Formato:

```text
SNAPSHOT-XXXX
```

---

# Auditoría

Toda publicación registrará:

- usuario;
- fecha;
- ejecución;
- versión;
- cambios.

---

# Contrato

```yaml
publication:

    package:

    snapshot:

    version:

    published_at:

    published_by:
```

---

# Rollback

Toda publicación deberá poder revertirse.

---

# Rollback parcial

Podrá afectar únicamente a determinados elementos.

---

# Rollback completo

Restaurará el Snapshot anterior.

---

# Versiones

El historial deberá conservarse.

Nunca deberá sobrescribirse.

---

# Historial

Toda modificación deberá ser auditable.

---

# Firma

Las publicaciones críticas podrán firmarse digitalmente.

---

# Publicación incremental

Solo modificará los cambios.

---

# Publicación completa

Reconstruirá completamente el Knowledge Graph correspondiente.

---

# Publicación diferida

Podrá programarse para un momento posterior.

---

# Publicación manual

Requerirá intervención explícita.

---

# Publicación automática

Será posible cuando todos los Gates hayan sido superados.

---

# Estados finales

```text
Published

Rejected

Archived

RolledBack
```

---

# Métricas

Ejemplos:

- paquetes publicados;
- rechazados;
- advertencias;
- tiempo medio;
- calidad media.

---

# KPIs

Ejemplos:

- tasa de aceptación;
- errores por documento;
- referencias inválidas;
- calidad media;
- tiempo de publicación.

---

# Checklist

Antes de publicar deberá comprobarse:

```text
[ ] Estructura válida
[ ] Ontología válida
[ ] Relaciones válidas
[ ] Restricciones superadas
[ ] Diagnósticos revisados
[ ] Procedencia completa
[ ] Versionado preparado
[ ] Snapshot generado
```

---

# Arquitectura

```text
Knowledge Package
        │
        ▼
Validation Engine
        │
 ┌──────┼──────────┐
 ▼      ▼          ▼
Structure Ontology Policy
        │
        ▼
 Quality Gates
        │
        ▼
Publication Engine
        │
        ▼
Knowledge Graph
```

---

# Transición hacia la Parte V

La siguiente parte desarrollará la integración con el Knowledge Graph:

- inserción de nodos;
- creación de relaciones;
- actualización incremental;
- invalidación;
- materialización inicial;
- índices;
- embeddings;
- integración con colecciones;
- sincronización con el Reasoning Engine.

---

# Conclusión

La validación constituye la frontera entre el conocimiento potencial y el conocimiento oficial del SGCC.

Su misión no consiste únicamente en detectar errores, sino en garantizar que toda la información publicada respete el modelo conceptual de NovaCoquinaria, conserve su trazabilidad y pueda evolucionar de forma segura.

Gracias a los distintos niveles de validación, los Quality Gates y el proceso controlado de publicación, el Ingestion Engine asegura que únicamente el conocimiento consistente, gobernado y auditable alcance el Knowledge Graph, proporcionando una base sólida para el Razonador, GraphRAG y los futuros agentes inteligentes.

---

# Parte V — Integración con el Knowledge Graph

---

# Introducción

Las partes anteriores han definido:

- la arquitectura general del Ingestion Engine;
- las fuentes, conectores y extractores;
- la normalización y representación interna;
- el enriquecimiento semántico;
- la construcción del Knowledge Package;
- la validación estructural y semántica;
- los Quality Gates;
- la decisión de publicación.

Esta quinta parte define cómo un Knowledge Package validado se transforma en conocimiento persistente dentro del Knowledge Graph del SGCC.

La integración con el grafo no deberá entenderse como una simple operación de inserción.

Publicar conocimiento implica:

- resolver identidades;
- comparar el estado entrante con el estado existente;
- crear o actualizar entidades;
- publicar afirmaciones;
- conservar procedencia;
- gestionar eliminaciones lógicas;
- mantener dependencias;
- actualizar índices;
- invalidar artefactos derivados;
- activar procesos posteriores;
- garantizar atomicidad y reversibilidad.

El proceso deberá preservar en todo momento la distinción entre:

```text
Fuente adquirida
Documento normalizado
Entidad candidata
Entidad canónica
Afirmación explícita
Inferencia
Índice derivado
```

La ingesta publicará principalmente conocimiento explícito y validado.

Las inferencias seguirán correspondiendo al Reasoning Engine.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir el contrato entre el Ingestion Engine y el Knowledge Graph;
- formalizar el proceso de construcción del grafo;
- establecer políticas de identidad y resolución de entidades;
- definir la creación y actualización de nodos;
- regular la publicación de relaciones y afirmaciones;
- preservar procedencia y contexto;
- definir sincronización incremental;
- gestionar renombrados, fusiones, divisiones y eliminaciones;
- establecer invalidación de artefactos derivados;
- actualizar índices y colecciones;
- integrar la ingesta con el Razonador;
- garantizar atomicidad, idempotencia y rollback;
- definir eventos, métricas y pruebas de integración.

---

# Principios de integración

Toda integración con el Knowledge Graph deberá respetar los siguientes principios.

---

## Identidad antes que persistencia

Antes de crear una entidad deberá determinarse si:

- ya existe;
- representa una nueva versión;
- constituye una variante;
- es un duplicado;
- requiere revisión.

---

## Publicación explícita

La ingesta no deberá publicar inferencias como si fueran hechos declarados.

---

## Procedencia inseparable

No deberá publicarse una afirmación sin conservar:

- fuente;
- documento;
- fragmento;
- ejecución;
- transformación;
- versión.

---

## Atomicidad

Una publicación no deberá dejar estados parciales.

---

## Idempotencia

Procesar dos veces el mismo Knowledge Package no deberá duplicar:

- entidades;
- relaciones;
- afirmaciones;
- índices;
- membresías.

---

## Incrementalidad

Deberán modificarse únicamente los elementos afectados.

---

## Historial preservado

Las versiones anteriores no deberán sobrescribirse de forma destructiva.

---

## Separación por capas

El conocimiento deberá publicarse en la capa epistemológica correspondiente.

---

## Invalidación propagada

Los cambios deberán invalidar de forma controlada:

- inferencias;
- colecciones;
- índices;
- embeddings;
- cachés;
- vistas derivadas.

---

## Reversibilidad

Toda publicación deberá poder revertirse cuando su naturaleza lo permita.

---

## Consistencia transaccional

El grafo y sus metadatos de procedencia deberán quedar sincronizados.

---

## Independencia del motor

El contrato conceptual no dependerá exclusivamente de:

- RDF;
- Neo4j;
- SQL;
- un grafo de propiedades;
- una tecnología concreta.

---

# Posición del Graph Integration Layer

La integración podrá representarse así:

```text
Knowledge Package validado
          │
          ▼
Graph Integration Layer
          │
          ├── Identity Resolver
          ├── Change Planner
          ├── Graph Mapper
          ├── Statement Publisher
          ├── Provenance Writer
          ├── Dependency Updater
          ├── Index Coordinator
          └── Event Publisher
          │
          ▼
Knowledge Graph
```

---

# Graph Integration Layer

La **Graph Integration Layer** será la capa responsable de traducir el Knowledge Package validado al modelo persistente del Knowledge Graph.

No deberá limitarse a enviar operaciones técnicas al almacén.

Deberá aplicar:

- políticas de identidad;
- contratos ontológicos;
- control de versiones;
- procedencia;
- atomicidad;
- gobernanza.

---

# Responsabilidades

Será responsable de:

- resolver entidades;
- identificar cambios;
- crear un plan de publicación;
- mapear artefactos al grafo;
- escribir nodos y relaciones;
- conservar afirmaciones;
- actualizar estados;
- registrar dependencias;
- emitir eventos;
- coordinar índices;
- verificar el resultado.

---

# Responsabilidades excluidas

No será responsable de:

- inferir nuevo conocimiento complejo;
- aprobar fusiones ambiguas;
- modificar la ontología;
- resolver controversias;
- generar recomendaciones;
- promover predicciones a conocimiento canónico.

---

# Contrato de entrada

La entrada deberá ser un Knowledge Package que haya superado los Quality Gates requeridos.

Ejemplo:

```yaml
graph_integration_request:
  package:
    id: KP-000421
    version: 1.0.0

  validation:
    run: VAL-ING-000041
    result: accepted

  publication_profile: standard

  target:
    graph: knowledge
    environment: production
```

---

# Contrato de salida

La integración deberá producir un resultado estructurado.

```yaml
graph_integration_result:
  id: GRAPH-PUB-000041
  package: KP-000421

  status: completed

  changes:
    entities_created: 1
    entities_updated: 2
    statements_created: 8
    statements_invalidated: 1
    relations_created: 5

  snapshot:
    id: KG-SNAP-20260801-004

  audit:
    event: AUD-KG-000451
```

---

# Estados de integración

Valores recomendados:

```text
planned
prepared
executing
verifying
committed
failed
rolled_back
partially_recovered
```

---

# Plan de publicación

Antes de modificar el grafo deberá generarse un plan.

Formato recomendado:

```text
GRAPH-PLAN-XXXXXX
```

---

## Objetivos del plan

El plan deberá indicar:

- qué se creará;
- qué se actualizará;
- qué se invalidará;
- qué se mantendrá;
- qué conflictos existen;
- qué artefactos derivados se verán afectados.

---

## Contrato de plan

```yaml
id: GRAPH-PLAN-000041
package: KP-000421

target_snapshot: KG-SNAP-20260801-003

operations:
  create_entities:
    - ENTITY-CANDIDATE-0001

  update_entities:
    - ING-0008

  create_statements:
    - STM-CANDIDATE-0041

  invalidate_statements:
    - STM-000871

impact:
  inferences:
    - INF-000041

  collections:
    - COL-0003

  indexes:
    - IDX-TEXT-0001
    - IDX-VECTOR-0001
```

---

# Modo dry-run

Todo plan relevante deberá poder ejecutarse en modo simulación.

El `dry-run` deberá mostrar:

- operaciones;
- impacto;
- conflictos;
- errores;
- coste estimado;
- elementos derivados afectados.

No deberá modificar el grafo.

---

# Comparación con el estado existente

El Change Planner deberá comparar:

```text
Knowledge Package entrante
```

con:

```text
Knowledge Graph actual
```

---

# Tipos de resultado de comparación

```text
new
unchanged
modified
renamed
merged_candidate
split_candidate
deprecated
removed_from_source
conflicted
```

---

# Elemento nuevo

No existe una identidad equivalente en el grafo.

---

# Elemento sin cambios

La representación semántica y su procedencia relevante permanecen iguales.

---

# Elemento modificado

Conserva identidad, pero cambia alguna propiedad o afirmación.

---

# Elemento renombrado

Cambia:

- ruta;
- etiqueta;
- nombre visible;

pero conserva identidad.

---

# Candidato a fusión

Podría representar una entidad ya existente.

No deberá fusionarse automáticamente salvo política autorizada.

---

# Candidato a división

La entidad existente parece mezclar conceptos distintos.

Requerirá revisión.

---

# Elemento retirado de la fuente

Ya no aparece en la versión actual de la fuente.

No implica eliminación física automática.

---

# Elemento en conflicto

El contenido entrante contradice o resulta incompatible con el grafo existente.

---

# Identity Resolver

El Identity Resolver determinará la correspondencia entre candidatos y entidades canónicas.

---

# Estrategias de identidad

La resolución deberá aplicar las estrategias en un orden controlado.

---

## Identificador canónico explícito

Estrategia preferente.

Ejemplo:

```text
ING-0008
```

---

## URI canónica

Podrá utilizarse cuando exista.

---

## Identificador externo estable

Ejemplo:

```text
Wikidata Q...
```

No deberá sustituir al identificador SGCC.

---

## Historial de origen

Puede permitir reconocer:

- renombrados;
- cambios de ruta;
- movimientos;
- versiones.

---

## Hash semántico

Podrá ayudar a detectar equivalencia de contenido.

No deberá ser la única prueba de identidad.

---

## Claves naturales

Ejemplos:

- nombre + tipo + región;
- código de producto;
- combinación de atributos.

Deberán utilizarse con cautela.

---

## Similitud

Podrá generar candidatos.

No deberá confirmar automáticamente identidad en casos ambiguos.

---

# Orden recomendado de resolución

```text
ID SGCC explícito
        ↓
URI canónica
        ↓
Mapeo externo validado
        ↓
Historial de procedencia
        ↓
Clave natural
        ↓
Similitud
        ↓
Revisión
```

---

# Resultado de resolución

Valores recomendados:

```text
resolved
new_entity
ambiguous
conflicted
manual_review_required
```

---

# Contrato de resolución

```yaml
identity_resolution:
  candidate: ENTITY-CANDIDATE-0001

  result: resolved
  canonical_entity: ING-0008

  strategy: explicit_sgcc_id
  confidence: 1.0

  evidence:
    source_document: DOC-0051
    declared_id: ING-0008
```

---

# Identidad provisional

Cuando no pueda resolverse una identidad, podrá mantenerse:

```text
TMP-ENTITY-XXXXXX
```

El identificador provisional no deberá publicarse como identidad canónica estable salvo política explícita.

---

# Colisión de identificadores

Existe colisión cuando un mismo identificador pretende representar conceptos incompatibles.

La publicación deberá bloquearse.

---

# Resolución ambigua

Cuando existan varios candidatos plausibles, el sistema deberá:

- detener la creación canónica;
- registrar candidatos;
- poner el elemento en revisión;
- evitar la fusión silenciosa.

---

# Entity Mapping

El Graph Mapper transformará entidades candidatas en representaciones compatibles con el grafo.

---

# Tipos de elemento publicados

El Knowledge Package podrá generar:

- documentos;
- entidades;
- componentes;
- afirmaciones;
- relaciones;
- contextos;
- fuentes;
- actividades de procedencia;
- diagnósticos publicables.

---

# Documento como nodo

Un documento SGCC podrá representarse como entidad del grafo.

Ejemplo:

```text
DOC-0051
    │
    ├── describes → REC-0009
    ├── mentions → ING-0008
    └── derived_from → SRC-000142
```

---

# Fuente como nodo

Las fuentes relevantes podrán representarse en la capa de procedencia.

---

# Componente como nodo

Los componentes reutilizables podrán poseer identidad propia.

---

# Entidad de dominio

Ejemplos:

- receta;
- ingrediente;
- técnica;
- utensilio;
- región;
- colección.

---

# Afirmación

La unidad principal de publicación factual deberá ser la afirmación.

---

# Relación directa y afirmación enriquecida

Una relación simple podrá representarse como:

```text
REC-0009 uses_ingredient ING-0008
```

Cuando requiera metadatos deberá modelarse como afirmación enriquecida.

---

# Statement Publisher

El Statement Publisher será responsable de crear y mantener afirmaciones explícitas.

---

# Identidad de afirmación

Formato recomendado:

```text
STM-XXXXXX
```

---

# Contrato de afirmación explícita

```yaml
id: STM-000123
type: explicit_statement

subject: REC-0009
predicate: uses_ingredient
object: ING-0008

status: validated
layer: explicit

context:
  recipe_version: 1.2.0

provenance:
  document: DOC-0051
  source: SRC-000142
  fragment: BLOCK-00041
  ingestion_execution: ING-EXEC-000041
```

---

# Afirmación literal

Ejemplo:

```yaml
subject: REC-0009
predicate: servings
value: 4
datatype: integer
```

---

# Afirmación relacional

Conecta entidades.

---

# Afirmación contextual

Incluye ámbito de validez.

---

# Afirmación temporal

Incluye:

- `valid_from`;
- `valid_until`;
- tiempo de registro.

---

# Afirmación negativa explícita

Solo deberá publicarse cuando el origen declare una negación real.

---

# Afirmación propuesta

Los resultados automáticos no confirmados deberán publicarse, si se permite, en una capa separada:

```text
proposed
```

---

# Estado de afirmación

Valores recomendados:

```text
proposed
extracted
validated
confirmed
disputed
deprecated
invalidated
archived
```

---

# Publicación por capas

El grafo deberá distinguir, como mínimo:

```text
explicit
validated
proposed
inferred
predicted
hypothetical
```

La ingesta operará principalmente sobre:

```text
explicit
validated
proposed
```

---

# Prohibición de promoción silenciosa

Un candidato extraído automáticamente no deberá publicarse directamente como:

```text
confirmed
```

sin la validación requerida.

---

# Granularidad de procedencia

La procedencia podrá registrarse a nivel de:

- documento;
- sección;
- bloque;
- tabla;
- fila;
- celda;
- página;
- coordenada;
- timestamp;
- registro.

---

# Provenance Writer

El Provenance Writer deberá publicar la cadena de procedencia.

---

# Modelo conceptual de procedencia

```text
Fuente
   ↓
Artefacto adquirido
   ↓
Artefacto extraído
   ↓
Documento canónico
   ↓
Knowledge Package
   ↓
Afirmación publicada
```

---

# Actividad de ingesta

La ejecución podrá representarse como actividad.

```text
ING-EXEC-000041
    │
    ├── used → SRC-000142
    ├── generated → KP-000421
    └── generated → STM-000123
```

---

# Agente de publicación

Podrá identificarse:

- sistema;
- usuario;
- pipeline;
- conector;
- extractor;
- modelo IA.

---

# Procedencia directa

Conecta la afirmación con su fuente inmediata.

---

# Procedencia transitiva

Permite llegar hasta el origen último conocido.

---

# Fuente primaria y fuente secundaria

El modelo deberá permitir diferenciarlas.

---

# Evidencia textual

Una afirmación podrá enlazar con el fragmento exacto que la respalda.

---

# Múltiples evidencias

Una afirmación podrá estar respaldada por varias fuentes.

La incorporación de una nueva evidencia no deberá crear necesariamente una nueva afirmación lógica.

---

# Una conclusión factual con varias evidencias

Modelo recomendado:

```text
Statement
   │
   ├── supported_by → Evidence A
   ├── supported_by → Evidence B
   └── supported_by → Evidence C
```

---

# Separación entre afirmación y evidencia

La misma afirmación podrá sobrevivir aunque una evidencia concreta quede invalidada, siempre que mantenga respaldo suficiente.

---

# Creación de entidades

Una entidad nueva podrá publicarse cuando:

- no exista identidad equivalente;
- su tipo sea válido;
- disponga de procedencia;
- supere los Quality Gates;
- no exista ambigüedad crítica.

---

# Contrato de entidad canónica

```yaml
id: ING-0042
type: Ingredient

preferred_label:
  es: Miso blanco

status: active

provenance:
  created_from:
    package: KP-000421
    source: SRC-000142
```

---

# Actualización de entidades

Una actualización podrá afectar:

- etiqueta;
- descripción;
- alias;
- clasificación;
- estado;
- relaciones;
- procedencia.

---

# Actualización no destructiva

Los valores anteriores deberán:

- conservarse en historial;
- deprecarse;
- contextualizarse;
- versionarse.

---

# Propiedad funcional

Cuando una propiedad admita un único valor, la actualización deberá:

- cerrar el valor anterior;
- crear el nuevo;
- conservar vigencia;
- registrar cambio.

---

# Propiedad multivaluada

Podrá añadirse una nueva afirmación sin invalidar las anteriores.

---

# Cambio editorial

Ejemplo:

- corrección de etiqueta;
- descripción;
- traducción.

No deberá confundirse con un cambio semántico.

---

# Cambio semántico

Ejemplo:

- nuevo tipo;
- reclasificación;
- relación incompatible;
- cambio de identidad.

Requerirá mayor control.

---

# Versionado de entidad

La identidad podrá mantenerse mientras evolucionan sus revisiones.

```text
ING-0008
  ├── revision 1
  ├── revision 2
  └── revision 3
```

---

# Renombrados

Un renombrado de archivo o etiqueta no deberá generar una nueva entidad cuando la identidad permanezca.

---

# Detección de renombrado

Podrá utilizar:

- ID canónico;
- historial Git;
- hash;
- procedencia;
- metadatos.

---

# Alias de ruta

Las rutas anteriores podrán conservarse para:

- redirección;
- compatibilidad;
- auditoría.

---

# Fusiones

La fusión combina identidades duplicadas.

No deberá ejecutarse automáticamente salvo casos inequívocos y de bajo riesgo.

---

# Plan de fusión

Deberá indicar:

- entidad canónica;
- entidades absorbidas;
- relaciones afectadas;
- afirmaciones;
- alias;
- conflictos;
- consumidores.

---

# Ejemplo

```text
ING-0042
ING-0108
        │
        ▼
ING-0008
```

---

# Estado de entidades fusionadas

Deberán quedar:

```text
deprecated
```

o:

```text
merged
```

y enlazadas mediante:

```text
merged_into
```

---

# Redirección de relaciones

Las relaciones deberán apuntar a la entidad canónica.

El historial de los sujetos originales deberá conservarse.

---

# Divisiones

Una entidad deberá dividirse cuando agrupe conceptos diferentes.

---

# Proceso de división

```text
Entidad ambigua
      ↓
Nuevas entidades
      ↓
Clasificación de afirmaciones
      ↓
Redistribución
      ↓
Deprecación de la entidad original
```

---

# División asistida

La ingesta podrá detectar candidatos, pero la aprobación deberá pertenecer a la gobernanza del conocimiento.

---

# Eliminaciones

La ausencia en una fuente no implica borrado inmediato.

---

# Tipos de eliminación

---

## Eliminación de fuente

La unidad deja de existir en el origen.

---

## Retirada editorial

El contenido deja de estar activo.

---

## Deprecación semántica

El concepto se sustituye.

---

## Eliminación física

Se borra del almacenamiento.

Será excepcional.

---

# Política recomendada

```text
Eliminar de fuente
       ↓
Marcar source_missing
       ↓
Evaluar otras evidencias
       ↓
Invalidar afirmaciones sin respaldo
       ↓
Deprecar entidad si procede
```

---

# Afirmación sin otras evidencias

Podrá invalidarse.

---

# Afirmación con otras evidencias

Podrá mantenerse activa.

---

# Entidad sin fuente activa

Podrá permanecer por:

- historial;
- otras procedencias;
- valor canónico;
- uso externo.

---

# Tombstone

Un elemento eliminado lógicamente podrá dejar un marcador.

Formato conceptual:

```yaml
tombstone:
  target: STM-000123
  reason: source_removed
  removed_at: 2026-08-01
  source_event: SRC-EVT-000081
```

---

# Restauración

Si la fuente reaparece, el elemento podrá restaurarse tras validación.

---

# Sincronización incremental

La publicación incremental deberá utilizar el Change Set generado durante la ingesta.

---

# Flujo incremental

```text
Change Set
    │
    ▼
Impact Analysis
    │
    ▼
Graph Plan
    │
    ▼
Transactional Update
    │
    ▼
Verification
    │
    ▼
Derived Artifact Invalidation
```

---

# Creación incremental

Añade elementos nuevos.

---

# Actualización incremental

Modifica únicamente los elementos afectados.

---

# Invalidación incremental

Invalida dependencias de los elementos modificados.

---

# Renombrado incremental

Actualiza localización y referencias sin cambiar identidad.

---

# Eliminación incremental

Aplica la política de baja lógica.

---

# Change Set semántico

El cambio técnico de un archivo deberá traducirse a un cambio semántico.

Ejemplo:

```text
Archivo modificado
```

puede producir:

```text
sin cambio semántico
```

o:

```text
dos afirmaciones nuevas
una afirmación invalidada
```

---

# Semantic Diff

El sistema deberá poder generar una diferencia semántica.

Formato recomendado:

```text
SEM-DIFF-XXXXXX
```

---

## Contrato de diferencia semántica

```yaml
id: SEM-DIFF-000041

package_from: KP-000420
package_to: KP-000421

changes:
  entities:
    updated:
      - REC-0009

  statements:
    added:
      - STM-CANDIDATE-0081

    removed:
      - STM-000871

    unchanged:
      - STM-000123
```

---

# Igualdad semántica

Dos documentos pueden diferir textualmente, pero producir el mismo conocimiento.

En ese caso no deberá modificarse el grafo innecesariamente.

---

# Hash semántico

Podrá calcularse sobre:

- entidades;
- afirmaciones;
- contexto;
- valores;
- relaciones.

---

# Dependency Updater

El Dependency Updater deberá mantener las relaciones de dependencia entre:

- documentos;
- entidades;
- afirmaciones;
- inferencias;
- colecciones;
- índices;
- embeddings;
- vistas.

---

# Grafo de dependencias

Ejemplo:

```text
DOC-0051
   ↓
STM-000123
   ↓
INF-000041
   ↓
COL-0003
   ↓
IDX-VECTOR-0001
```

---

# Impacto de cambio

Antes de publicar deberá determinarse qué elementos derivados quedarán afectados.

---

# Tipos de impacto

- directo;
- transitivo;
- semántico;
- temporal;
- de seguridad;
- de índice;
- de consulta.

---

# Inferencias

Cuando cambie una premisa, las inferencias dependientes deberán marcarse como:

```text
stale
```

antes de su recálculo.

---

# Colecciones

Las membresías dinámicas podrán quedar pendientes de resolución.

---

# Índices

Los documentos, entidades o chunks afectados deberán reindexarse.

---

# Embeddings

Deberán regenerarse cuando cambie el contenido relevante.

---

# Cachés

Deberán invalidarse utilizando las dependencias afectadas.

---

# Vistas materializadas

Deberán actualizarse o marcarse como obsoletas.

---

# Índices

La integración podrá coordinar varios índices derivados.

---

# Tipos de índice

```text
identity
text
graph
ontology
vector
temporal
provenance
collection
```

---

# Índice de identidad

Facilita resolución de:

- IDs;
- URI;
- alias;
- claves externas.

---

# Índice textual

Indexa:

- etiquetas;
- descripciones;
- contenido;
- alias;
- fragmentos.

---

# Índice de grafo

Optimiza:

- vecinos;
- caminos;
- tipos;
- predicados.

---

# Índice ontológico

Facilita:

- jerarquías;
- clases;
- propiedades;
- equivalencias.

---

# Índice vectorial

Almacena embeddings.

Será un artefacto derivado.

---

# Índice temporal

Facilita consultas de:

- vigencia;
- historia;
- versiones;
- eventos.

---

# Índice de procedencia

Permite recorrer fuentes y derivaciones.

---

# Índice de colección

Optimiza pertenencia y resolución de colecciones.

---

# Index Coordinator

El Index Coordinator deberá decidir qué índices actualizar.

---

# Escritura síncrona y asíncrona

Algunos índices podrán actualizarse:

- dentro de la transacción;
- inmediatamente después;
- mediante eventos;
- por lotes.

---

# Índices críticos

Los índices necesarios para identidad e integridad deberán actualizarse de forma síncrona o transaccionalmente coordinada.

---

# Índices eventualmente consistentes

Los índices de búsqueda o embeddings podrán actualizarse de forma asíncrona.

Deberán declarar su estado.

---

# Estado de índice

Valores recomendados:

```text
current
updating
stale
failed
rebuilding
```

---

# Embeddings

Los embeddings podrán generarse para:

- documentos;
- bloques;
- entidades;
- relaciones;
- colecciones;
- subgrafos.

---

# Embedding como artefacto derivado

No formará parte del conocimiento canónico.

---

# Contrato de embedding

```yaml
id: EMB-000145
target: BLOCK-00041

model:
  id: EMBEDDING-MODEL-0001
  version: 1.0.0

dimensions: 1536

source_hash: sha256:...
generated_at: 2026-08-01

status: current
```

---

# Cuándo regenerar

Cuando cambien:

- texto;
- estructura relevante;
- modelo;
- chunking;
- normalización;
- idioma;
- permisos.

---

# No regeneración innecesaria

Un cambio editorial no relevante para el embedding podrá conservar el vector existente si el hash semántico permanece igual.

---

# Permisos de embeddings

Los vectores deberán heredar:

- sensibilidad;
- permisos;
- ámbito;
- retención.

---

# Colecciones

La publicación podrá afectar Colecciones de Conocimiento.

---

# Pertenencia explícita

Procede de una declaración directa.

Ejemplo:

```text
REC-0009 member_of COL-0001
```

---

# Pertenencia derivada

Deberá resolverse posteriormente mediante:

- reglas;
- consultas;
- criterios de colección.

No deberá publicarse como explícita.

---

# Collection Resolver

La integración podrá notificar al Collection Resolver que existen cambios relevantes.

---

# Tipos de actualización

- añadir miembro explícito;
- retirar miembro;
- recalcular membresía dinámica;
- invalidar snapshot;
- actualizar métricas.

---

# Snapshot de colección

Una colección materializada podrá requerir un nuevo snapshot.

---

# Dependencia con afirmaciones

La membresía deberá conservar qué afirmaciones o reglas la justifican.

---

# Integración con el Reasoning Engine

La publicación de nuevos hechos podrá activar razonamiento.

---

# Secuencia recomendada

```text
Publicar hechos explícitos
        ↓
Confirmar transacción
        ↓
Emitir evento
        ↓
Invalidar inferencias afectadas
        ↓
Ejecutar razonamiento incremental
        ↓
Materializar inferencias autorizadas
```

---

# Separación transaccional

La publicación de hechos y el razonamiento podrán ejecutarse en transacciones separadas.

Esto evita que un fallo del Reasoner invalide la publicación factual.

---

# Estado intermedio

Mientras se recalculan inferencias, el sistema deberá marcar:

```text
reasoning_pending
```

cuando resulte relevante.

---

# Evento para el Reasoner

Ejemplo:

```yaml
event:
  type: graph_statements_changed

  payload:
    created:
      - STM-000991

    invalidated:
      - STM-000871

    affected_entities:
      - REC-0009
      - ING-0008

    graph_snapshot: KG-SNAP-20260801-004
```

---

# Rulesets afectados

El impacto podrá utilizarse para seleccionar:

- reglas;
- rulesets;
- módulos;
- colecciones.

---

# Razonamiento incremental

Solo deberán recalcularse las inferencias dependientes.

---

# Inferencias no materializadas

Las consultas bajo demanda utilizarán el nuevo snapshot sin requerir materialización completa.

---

# Integración con el Validation Engine

La validación deberá continuar después de escribir el grafo.

---

# Validación posterior a publicación

Podrá comprobar:

- nodos creados;
- referencias;
- tipos;
- dominio;
- rango;
- procedencia;
- índices;
- consistencia transaccional.

---

# Read-after-write verification

El sistema deberá verificar que el estado persistido corresponde al plan.

---

# Post-publication Gate

La publicación no deberá considerarse finalizada hasta superar la verificación requerida.

---

# Inconsistencia detectada después de escribir

Deberá producir:

- rollback;
- compensación;
- bloqueo;
- incidente;

según la política.

---

# Transacciones

Toda publicación deberá definir su frontera transaccional.

---

# Transacción única

Adecuada cuando:

- el volumen es pequeño;
- un único almacén soporta todas las operaciones;
- se requiere consistencia fuerte.

---

# Transacción por paquete

Publica un Knowledge Package completo.

---

# Transacción por unidad

Publica entidades o documentos independientes.

---

# Saga

Podrá utilizarse cuando intervengan varios servicios.

Cada paso deberá disponer de compensación.

---

# Atomicidad lógica

Aunque existan varios sistemas, el resultado deberá comportarse como una unidad coherente para los consumidores.

---

# Commit

Solo deberá realizarse tras:

- aplicar operaciones;
- verificar integridad;
- registrar procedencia;
- registrar auditoría.

---

# Rollback

Deberá restaurar el estado anterior cuando sea posible.

---

# Compensación

Cuando no sea posible rollback técnico, deberá ejecutarse una operación semánticamente inversa.

---

# Publicación parcial

Solo se permitirá cuando el perfil lo autorice.

Deberá declarar:

- elementos publicados;
- elementos fallidos;
- consistencia;
- acciones pendientes.

---

# Publicación all-or-nothing

Será recomendable para:

- cambios de identidad;
- fusiones;
- migraciones;
- paquetes críticos.

---

# Idempotencia

Toda operación deberá disponer de una clave idempotente.

---

# Clave de publicación

Podrá construirse con:

```text
package_id
+
package_version
+
target_graph
+
publication_profile
```

---

# Operación repetida

Si ya existe una publicación equivalente, deberá devolver el resultado previo o indicar:

```text
already_applied
```

---

# Identidad de operaciones

Formato recomendado:

```text
GRAPH-OP-XXXXXX
```

---

# Registro de operaciones

```yaml
operation:
  id: GRAPH-OP-000041
  type: create_statement

  target: STM-000991
  status: committed

  idempotency_key: sha256:...
```

---

# Concurrencia

Varias ingestas pueden afectar los mismos elementos.

---

# Control optimista

Cada actualización podrá comprobar una versión esperada.

---

# Conflicto de versión

Si el elemento cambió después de planificar:

- abortar;
- regenerar plan;
- fusionar;
- solicitar revisión.

---

# Bloqueo pesimista

Podrá utilizarse en operaciones críticas como:

- fusión;
- división;
- migración de identidad.

---

# Orden causal

Los eventos incrementales deberán respetar el orden causal cuando afecten la misma entidad.

---

# Escritura concurrente

No deberá sobrescribir silenciosamente cambios de otra ejecución.

---

# Rebase semántico

Un plan obsoleto podrá recalcularse contra el snapshot actual.

---

# Snapshots

Toda publicación estable debería asociarse con un snapshot o una revisión identificable.

---

# Snapshot lógico

Representa un estado coherente del grafo.

---

# Snapshot completo

Incluye todo el Knowledge Graph.

---

# Snapshot parcial

Incluye:

- módulo;
- colección;
- paquete;
- subgrafo.

---

# Inmutabilidad

Un snapshot publicado no deberá modificarse.

---

# Manifest de snapshot

```yaml
snapshot:
  id: KG-SNAP-20260801-004
  version: 1.5.0

  created_at: 2026-08-01T20:00:00+02:00

  source_publications:
    - GRAPH-PUB-000041

  ontology_version: 2.0.0

  hashes:
    graph: sha256:...
    provenance: sha256:...
```

---

# Snapshot y reproducibilidad

Una consulta o inferencia crítica deberá poder indicar el snapshot utilizado.

---

# Auditoría

Toda integración deberá ser auditable.

---

# Eventos auditables

- plan generado;
- identidad resuelta;
- entidad creada;
- entidad actualizada;
- afirmación creada;
- afirmación invalidada;
- fusión;
- división;
- rollback;
- snapshot;
- índice actualizado;
- evento emitido.

---

# Contrato de auditoría

```yaml
audit_event:
  id: AUD-KG-000451
  type: knowledge_package_published

  actor:
    type: system
    id: INGESTION-ENGINE

  package: KP-000421
  publication: GRAPH-PUB-000041

  before_snapshot: KG-SNAP-20260801-003
  after_snapshot: KG-SNAP-20260801-004

  timestamp: 2026-08-01T20:00:00+02:00
```

---

# Eventos de integración

El Graph Integration Layer deberá emitir eventos para desacoplar consumidores.

---

# Eventos principales

```text
graph_publication_started
entity_created
entity_updated
statement_created
statement_invalidated
source_removed
graph_publication_completed
graph_publication_failed
snapshot_created
```

---

# Evento de publicación completada

```yaml
event:
  id: EVT-KG-000041
  type: graph_publication_completed
  version: 1.0

  timestamp: 2026-08-01T20:00:00+02:00

  payload:
    publication: GRAPH-PUB-000041
    package: KP-000421
    snapshot: KG-SNAP-20260801-004

    changed_entities:
      - REC-0009
      - ING-0008
```

---

# Consumidores

Podrán consumir eventos:

- Reasoning Engine;
- Collection Resolver;
- Search Engine;
- Embedding Engine;
- GraphRAG;
- cachés;
- observabilidad.

---

# Entrega de eventos

La semántica de entrega deberá estar declarada.

La idempotencia de consumidores será obligatoria.

---

# Outbox pattern

Cuando la publicación y los eventos utilicen sistemas distintos, podrá utilizarse un patrón de outbox para evitar:

- publicación sin evento;
- evento sin publicación.

---

# Seguridad

La integración deberá respetar:

- autenticación;
- autorización;
- sensibilidad;
- segregación;
- minimización;
- licencias.

---

# Permisos de publicación

Ejemplos:

```text
graph_publish
graph_update
graph_invalidate
graph_merge
graph_migrate
graph_admin
```

---

# Mínimo privilegio

El Ingestion Engine no deberá poseer permisos globales innecesarios.

---

# Grafo global y grafos personales

Las fuentes personales deberán publicarse en ámbitos segregados.

---

# Propagación de sensibilidad

La sensibilidad de una entidad o afirmación deberá considerar:

- fuente;
- contenido;
- contexto;
- política.

---

# Información restringida

No deberá incorporarse a índices públicos.

---

# Licencias

Las afirmaciones publicadas deberán conservar las restricciones de reutilización cuando proceda.

---

# Secreto detectado

No deberá publicarse.

---

# Datos personales

Deberán aplicar:

- minimización;
- retención;
- derecho de eliminación;
- aislamiento;
- acceso controlado.

---

# Cifrado

Las operaciones críticas podrán requerir cifrado:

- en tránsito;
- en reposo;
- en copias;
- en eventos.

---

# Integridad

Podrán utilizarse:

- hashes;
- firmas;
- controles de versión;
- verificaciones post-publicación.

---

# Rendimiento

La integración deberá escalar sin sacrificar consistencia.

---

# Estrategias

- procesamiento por lotes;
- operaciones bulk;
- índices;
- paralelismo por particiones;
- caché de identidad;
- diffs semánticos;
- escritura incremental.

---

# Publicación bulk

Podrá utilizarse para grandes volúmenes.

Deberá conservar:

- trazabilidad por elemento;
- capacidad de error;
- idempotencia;
- rollback o compensación.

---

# Paralelismo

Solo deberán ejecutarse en paralelo operaciones independientes.

---

# Particionamiento

Podrá realizarse por:

- módulo;
- tipo;
- colección;
- fuente;
- entidad.

---

# Contención

Las entidades de alta conectividad podrán requerir serialización.

---

# Caché de identidad

Podrá acelerar resolución de:

- IDs;
- URI;
- alias.

Deberá invalidarse ante fusiones o cambios de identidad.

---

# Métricas de integración

Ejemplos:

- paquetes publicados;
- entidades creadas;
- entidades actualizadas;
- afirmaciones creadas;
- afirmaciones invalidadas;
- conflictos de identidad;
- rollbacks;
- duración;
- operaciones por segundo;
- índices pendientes;
- inferencias invalidadas.

---

# Métricas de calidad

- publicaciones idempotentes;
- afirmaciones sin procedencia;
- entidades provisionales;
- operaciones parciales;
- divergencias entre plan y resultado;
- índices obsoletos;
- fallos post-publicación.

---

# Métricas de identidad

- resoluciones exactas;
- resoluciones aproximadas;
- ambigüedades;
- fusiones propuestas;
- colisiones;
- revisiones pendientes.

---

# Métricas incrementales

- elementos sin cambio;
- cambios textuales;
- cambios semánticos;
- tamaño medio del diff;
- recálculos evitados.

---

# Observabilidad

La integración deberá producir:

- logs;
- métricas;
- trazas;
- auditoría;
- diagnósticos;
- informes de impacto.

---

# Logs estructurados

```yaml
log:
  level: INFO
  event: statement_created

  publication: GRAPH-PUB-000041
  operation: GRAPH-OP-000041

  statement: STM-000991
  package: KP-000421

  duration_ms: 4
```

---

# Trazas

Una traza podrá incluir:

```text
Validation
↓
Graph Planning
↓
Identity Resolution
↓
Graph Write
↓
Verification
↓
Index Update
↓
Event Publication
```

---

# Alertas

Ejemplos:

- aumento de colisiones;
- publicación bloqueada;
- rollback fallido;
- índice desactualizado;
- divergencia entre grafo y procedencia;
- backlog de razonamiento;
- eventos no entregados.

---

# Pruebas

La integración deberá probarse en múltiples niveles.

---

# Pruebas unitarias

Para:

- mapeos;
- resolución;
- generación de operaciones;
- idempotencia;
- hashes;
- políticas.

---

# Pruebas de contrato

Entre:

- Knowledge Package;
- Graph Integration Layer;
- Knowledge Graph;
- índices;
- eventos.

---

# Pruebas de integración

Deberán verificar:

- creación;
- actualización;
- renombrado;
- invalidación;
- rollback;
- eventos;
- índices;
- procedencia.

---

# Pruebas de idempotencia

La misma publicación ejecutada varias veces deberá producir el mismo estado final.

---

# Pruebas de concurrencia

Deberán cubrir:

- dos actualizaciones sobre la misma entidad;
- rebase;
- conflicto de versión;
- bloqueo;
- eventos fuera de orden.

---

# Pruebas de rollback

Deberán comprobar:

- restauración;
- auditoría;
- índices;
- eventos;
- dependencias.

---

# Pruebas de procedencia

Toda afirmación deberá poder rastrearse hasta el origen.

---

# Pruebas de seguridad

Deberán verificar:

- separación de grafos;
- permisos;
- índices;
- eventos;
- datos personales;
- sensibilidad.

---

# Golden Graph

Un Golden Graph representa el estado esperado tras publicar un paquete conocido.

```yaml
golden_graph_case:
  id: GOLDEN-KG-0001

  input:
    package: TEST-KP-0001

  expected:
    entities:
      created:
        - REC-TEST-0001

    statements:
      created:
        - subject: REC-TEST-0001
          predicate: uses_ingredient
          object: ING-TEST-0001

    conflicts: []
```

---

# Pruebas de diferencias semánticas

Deberán comprobar que:

- cambios editoriales no generan operaciones innecesarias;
- cambios semánticos sí generan actualizaciones;
- eliminaciones invalidan únicamente lo necesario.

---

# Perfil mínimo de integración

La primera implementación podrá soportar:

- documentos Markdown;
- IDs canónicos explícitos;
- creación y actualización de nodos;
- afirmaciones explícitas;
- procedencia documental;
- publicación incremental;
- invalidación lógica;
- snapshot;
- eventos básicos;
- integración con validadores.

---

# Perfil estructurado

Añadirá:

- resolución de identidad avanzada;
- semantic diff;
- fusiones gobernadas;
- divisiones;
- índices;
- colecciones;
- transacciones distribuidas;
- rebase.

---

# Perfil semántico

Añadirá:

- RDF-star o representación equivalente;
- grafos nombrados;
- temporalidad;
- múltiples evidencias;
- alineaciones externas;
- validación ontológica post-publicación.

---

# Perfil inteligente

Añadirá:

- embeddings;
- reindexación automática;
- GraphRAG;
- detección de duplicados mediante IA;
- impacto inferencial;
- propuestas automáticas de fusión;
- optimización adaptativa.

---

# Implementación inicial recomendada

La primera implementación práctica debería centrarse en el repositorio Markdown de NovaCoquinaria.

Flujo recomendado:

```text
Knowledge Package validado
        ↓
Resolver ID declarado
        ↓
Comparar con snapshot actual
        ↓
Generar Semantic Diff
        ↓
Crear Graph Plan
        ↓
Publicar documento, entidades y afirmaciones
        ↓
Registrar procedencia
        ↓
Verificar
        ↓
Crear snapshot
        ↓
Emitir evento
        ↓
Ejecutar validación e invalidación incremental
```

Inicialmente deberían soportarse:

- creación de documentos;
- actualización por ID;
- relaciones explícitas;
- referencias internas;
- procedencia por bloque;
- invalidación lógica;
- idempotencia;
- rollback por paquete;
- métricas básicas.

No será necesario implementar inicialmente:

- sincronización bidireccional;
- fusión automática;
- división automática;
- razonamiento distribuido;
- embeddings multimodales;
- transacciones multi-región;
- escritura desde agentes;
- alineaciones externas automáticas;
- publicación pública Linked Data.

---

# Caso de uso 1 — Nueva receta

Entrada:

```text
Nuevo documento REC-0042
```

Proceso:

```text
Validar ID
↓
Resolver como nueva entidad
↓
Crear nodo Recipe
↓
Crear nodo Document
↓
Crear afirmaciones de ingredientes y técnicas
↓
Registrar procedencia
↓
Publicar snapshot
↓
Notificar al Reasoner y a las Colecciones
```

---

# Caso de uso 2 — Cambio editorial sin impacto semántico

Cambio:

```text
Corrección ortográfica en la introducción.
```

Resultado:

- nueva revisión documental;
- procedencia actualizada;
- sin nuevas entidades;
- sin cambios en afirmaciones;
- sin recálculo inferencial innecesario.

---

# Caso de uso 3 — Eliminación de un ingrediente

Cambio:

```text
La receta deja de utilizar ING-0008.
```

Proceso:

```text
Detectar afirmación retirada
↓
Invalidar STM correspondiente
↓
Actualizar revisión de receta
↓
Marcar inferencias dependientes como stale
↓
Recalcular alérgenos
↓
Actualizar colecciones
↓
Invalidar índices afectados
```

---

# Caso de uso 4 — Renombrado de archivo

Cambio:

```text
docs/recipes/sopa-miso.md
↓
docs/recipes/REC-0009_SOPA_DE_MISO.md
```

Resultado:

- misma entidad;
- mismo documento lógico;
- nueva localización;
- alias de ruta anterior;
- sin duplicación;
- sin cambio semántico.

---

# Caso de uso 5 — Fuente retirada

Cambio:

```text
El documento de origen se elimina.
```

Proceso:

```text
Registrar source_item_deleted
↓
Evaluar otras fuentes
↓
Mantener afirmaciones con respaldo alternativo
↓
Invalidar afirmaciones sin evidencia
↓
Deprecar documento si procede
↓
Conservar historial
```

---

# Caso de uso 6 — Posible duplicado

Entrada:

```text
Nuevo candidato "pasta de miso blanco"
```

Resultado:

```text
Candidato probable a ING-0042
```

El sistema deberá:

- registrar similitud;
- mostrar evidencias;
- impedir fusión automática si existe ambigüedad;
- enviar a revisión.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Crear entidades antes de resolver identidad

Genera duplicados.

---

## Utilizar la ruta como identidad canónica

Las rutas cambian.

---

## Sobrescribir afirmaciones

Destruye historial y procedencia.

---

## Eliminar físicamente al desaparecer una fuente

Puede destruir conocimiento respaldado por otras evidencias.

---

## Publicar predicciones como hechos

Rompe la separación epistemológica.

---

## Crear relaciones sin afirmación ni procedencia

Impide trazabilidad.

---

## Fusionar por similitud

La similitud no demuestra identidad.

---

## Regenerar todo el grafo ante cada cambio

Impide escalabilidad e incrementa riesgo.

---

## Recalcular todos los embeddings

Deben regenerarse únicamente los afectados.

---

## Emitir eventos antes del commit

Puede provocar consumidores trabajando sobre cambios inexistentes.

---

## Publicar sin verificación posterior

Puede dejar divergencias entre plan y estado.

---

## Permitir publicaciones parciales silenciosas

Toda parcialidad deberá ser explícita.

---

## Mezclar hechos e inferencias

Las capas deberán mantenerse separadas.

---

## Ignorar otras evidencias al retirar una fuente

Puede invalidar conocimiento todavía respaldado.

---

## Modificar el grafo desde conectores

Los conectores solo adquieren información.

---

## Dejar índices críticos eventualmente inconsistentes

La identidad y la integridad requieren garantías superiores.

---

## Caché de identidad no invalidada

Puede producir mapeos incorrectos tras una fusión.

---

## Actualización sin control de versión

Puede sobrescribir cambios concurrentes.

---

## Rollback sin revertir procedencia

Deja un estado incoherente.

---

## Publicar datos personales en el grafo global

Deben mantenerse segregados.

---

## Perder la licencia durante la transformación

Puede permitir reutilizaciones no autorizadas.

---

# Reglas mínimas de conformidad

---

## Paquete validado

No podrá publicarse un Knowledge Package rechazado o bloqueado.

---

## Plan obligatorio

Toda publicación deberá disponer de un plan reproducible.

---

## Identidad resuelta

Toda entidad canónica deberá poseer una identidad válida.

---

## Procedencia completa

Toda afirmación publicada deberá enlazar con su origen.

---

## Capas separadas

El conocimiento explícito, propuesto e inferido no deberá mezclarse.

---

## Escritura atómica

No deberán existir afirmaciones sin entidades o procedencia.

---

## Idempotencia

La repetición de una publicación no deberá producir duplicados.

---

## Historial preservado

Las modificaciones deberán conservar el estado anterior.

---

## Eliminación lógica

La eliminación física será excepcional y gobernada.

---

## Verificación posterior

El estado persistido deberá compararse con el plan.

---

## Impacto registrado

Toda modificación deberá identificar consumidores derivados.

---

## Snapshot o revisión

Toda publicación estable deberá asociarse con un estado identificable.

---

## Auditoría

Toda operación relevante deberá quedar registrada.

---

# Conformidad de plan

Un Graph Plan será conforme cuando:

- identifique paquete y snapshot;
- declare operaciones;
- indique impacto;
- detecte conflictos;
- pueda ejecutarse en dry-run;
- sea versionado o firmado mediante hash.

---

# Conformidad de resolución de identidad

Será conforme cuando:

- declare estrategia;
- conserve evidencia;
- indique confianza;
- gestione ambigüedad;
- no fusione silenciosamente;
- sea auditable.

---

# Conformidad de afirmación

Será conforme cuando:

- posea identidad;
- tenga sujeto y predicado;
- tenga objeto o valor;
- declare capa;
- tenga estado;
- conserve contexto;
- conserve procedencia;
- pueda invalidarse.

---

# Conformidad de publicación

Será conforme cuando:

- supere validación;
- aplique el plan;
- sea idempotente;
- sea atómica;
- registre auditoría;
- verifique el resultado;
- genere snapshot o revisión;
- emita eventos después del commit.

---

# Conformidad de invalidación

Será conforme cuando:

- declare motivo;
- conserve historial;
- identifique dependencias;
- no elimine otras evidencias válidas;
- produzca eventos;
- pueda reconstruirse.

---

# Conformidad de índice

Será conforme cuando:

- identifique su fuente;
- declare versión;
- preserve permisos;
- pueda regenerarse;
- tenga estado;
- se invalide ante cambios relevantes.

---

# Lista de comprobación

Antes de confirmar una publicación deberá verificarse:

```text
[ ] El Knowledge Package ha sido aceptado.
[ ] El snapshot de referencia sigue vigente.
[ ] Las identidades han sido resueltas.
[ ] No existen colisiones críticas.
[ ] El Semantic Diff ha sido generado.
[ ] El Graph Plan ha sido validado.
[ ] Las operaciones son idempotentes.
[ ] Las afirmaciones conservan procedencia.
[ ] Las capas epistemológicas están separadas.
[ ] Las eliminaciones son lógicas salvo autorización.
[ ] Las dependencias afectadas están identificadas.
[ ] Los permisos y la sensibilidad se han aplicado.
[ ] La transacción puede revertirse o compensarse.
[ ] La verificación posterior está configurada.
[ ] Los eventos se publicarán tras el commit.
[ ] El snapshot o revisión será generado.
```

---

# Arquitectura de integración con el grafo

```text
┌───────────────────────────────────────────────┐
│          Knowledge Package validado           │
│                                               │
│ Documentos · Entidades · Relaciones · Fuentes │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            Identity Resolution               │
│                                               │
│ IDs · URI · Historial · Alias · Similitud     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Change Planning                 │
│                                               │
│ Semantic Diff · Impacto · Graph Plan          │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Graph Publication                │
│                                               │
│ Entidades · Afirmaciones · Procedencia        │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│          Verificación y dependencias          │
│                                               │
│ Validación · Índices · Inferencias · Colecciones│
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            Snapshot y eventos                 │
│                                               │
│ Auditoría · Event Bus · Consumidores          │
└───────────────────────────────────────────────┘
```

---

# Transición hacia la Parte VI

Esta quinta parte ha definido:

- el contrato de integración con el Knowledge Graph;
- la Graph Integration Layer;
- el plan de publicación;
- el dry-run;
- la comparación con el estado existente;
- la resolución de identidad;
- el mapeo de entidades;
- la publicación de afirmaciones;
- la procedencia;
- la creación y actualización de entidades;
- los renombrados;
- las fusiones y divisiones;
- las eliminaciones lógicas;
- la sincronización incremental;
- el Semantic Diff;
- las dependencias;
- la invalidación de inferencias;
- la actualización de colecciones;
- los índices;
- los embeddings;
- la integración con el Reasoning Engine;
- las transacciones;
- la idempotencia;
- la concurrencia;
- los snapshots;
- la auditoría;
- los eventos;
- la seguridad;
- el rendimiento;
- las pruebas;
- los perfiles de capacidad.

La Parte VI desarrollará la operación y automatización del Ingestion Engine, incluyendo:

- ejecución por eventos;
- colas;
- scheduling;
- paralelismo;
- backpressure;
- reintentos;
- cachés;
- observabilidad;
- logs;
- métricas;
- trazas;
- alertas;
- rendimiento;
- escalabilidad;
- CI/CD;
- seguridad operacional;
- continuidad;
- recuperación ante fallos.

---

# Conclusión

La integración con el Knowledge Graph constituye el momento en que la información procesada por el Ingestion Engine pasa a formar parte del conocimiento operativo de NovaCoquinaria.

Este proceso no puede reducirse a crear nodos y relaciones.

Debe garantizar:

- identidad;
- coherencia;
- procedencia;
- versionado;
- atomicidad;
- idempotencia;
- reversibilidad;
- separación epistemológica;
- actualización incremental;
- propagación controlada del impacto.

El ciclo definido puede resumirse así:

```text
Knowledge Package validado
        ↓
Resolución de identidad
        ↓
Diferencia semántica
        ↓
Plan de publicación
        ↓
Escritura transaccional
        ↓
Verificación
        ↓
Actualización de dependencias
        ↓
Snapshot
        ↓
Eventos
```

El Ingestion Engine publica hechos explícitos.

El Knowledge Graph los conserva y conecta.

El Reasoning Engine deriva conclusiones.

Las Colecciones organizan ámbitos.

Los índices permiten recuperar conocimiento.

GraphRAG y los agentes lo utilizan bajo contratos gobernados.

Con esta quinta parte queda definido el puente persistente entre las fuentes documentales y el núcleo semántico del SGCC.

La siguiente parte establecerá cómo automatizar, observar, escalar y proteger este proceso en condiciones reales de operación.

---

# Parte VI — Operación, automatización y observabilidad del Ingestion Engine

---

# Introducción

Las partes anteriores han definido:

- la arquitectura del Ingestion Engine;
- las fuentes;
- la adquisición;
- la extracción;
- la normalización;
- la validación;
- la publicación;
- la integración con el Knowledge Graph.

Sin embargo, un motor de ingesta no es únicamente un pipeline de transformación.

También constituye un sistema distribuido que debe operar durante años, soportar múltiples fuentes, recuperarse de fallos, escalar horizontalmente y ofrecer garantías de observabilidad y gobernanza.

Esta parte define el funcionamiento operativo del Ingestion Engine.

---

# Objetivos

Esta parte persigue:

- definir la ejecución del motor;
- establecer el modelo de planificación;
- definir colas y eventos;
- gestionar paralelismo;
- regular la escalabilidad;
- controlar el consumo de recursos;
- definir observabilidad;
- definir logging;
- definir métricas;
- definir trazabilidad operacional;
- definir alertas;
- definir recuperación ante fallos;
- definir resiliencia;
- definir seguridad operacional;
- definir integración con CI/CD;
- establecer la operación continua.

---

# Principios

Toda operación deberá respetar:

- disponibilidad;
- resiliencia;
- observabilidad;
- reproducibilidad;
- automatización;
- desacoplamiento;
- escalabilidad;
- recuperación automática;
- mínima intervención manual.

---

# Arquitectura operacional

```text
              Scheduler
                    │
                    ▼
          Execution Queue
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
 Worker A                 Worker B
        ▼                       ▼
 Pipelines             Pipelines
        ▼                       ▼
 Monitoring ───────► Event Bus
```

---

# Execution Engine

El Execution Engine coordina todas las ejecuciones.

Será responsable de:

- iniciar pipelines;
- asignar workers;
- controlar concurrencia;
- registrar estados;
- gestionar cancelaciones;
- coordinar reintentos.

---

# Scheduler

El Scheduler determina cuándo debe ejecutarse una ingesta.

Podrá iniciar ejecuciones mediante:

- planificación temporal;
- eventos;
- ejecución manual;
- dependencias;
- webhooks;
- cambios Git;
- APIs.

---

# Modos de ejecución

Se definen los siguientes modos:

```text
Scheduled

Manual

Event Driven

Continuous

Incremental

Recovery
```

---

# Scheduler basado en tiempo

Ejemplo:

```text
Cada noche

Cada hora

Cada domingo

Primer día del mes
```

---

# Scheduler basado en eventos

Ejemplos:

- nuevo commit;
- nuevo documento;
- cambio en colección;
- webhook;
- subida manual.

---

# Scheduler dependiente

Permite:

```text
Pipeline B

↓

solo cuando

↓

Pipeline A finalice correctamente
```

---

# Execution Queue

Las ejecuciones deberán almacenarse en una cola.

Cada ejecución será independiente.

Formato:

```text
EXECUTION-JOB
```

---

# Contrato

```yaml
job:

    id:

    pipeline:

    priority:

    state:

    retries:
```

---

# Prioridades

```text
Critical

High

Normal

Low

Background
```

---

# Workers

Los Workers ejecutan los pipelines.

Podrán ser:

- locales;
- distribuidos;
- efímeros;
- permanentes.

---

# Escalado horizontal

El sistema deberá permitir aumentar workers sin modificar el pipeline.

---

# Afinidad

Algunos pipelines podrán requerir:

- GPU;
- OCR;
- IA;
- memoria elevada.

---

# Balanceo

El Scheduler distribuirá trabajos.

---

# Concurrencia

La concurrencia podrá configurarse por:

- fuente;
- pipeline;
- colección;
- organización.

---

# Exclusión

Algunos pipelines no deberán ejecutarse simultáneamente.

---

# Paralelismo

El paralelismo será posible cuando no existan dependencias.

---

# Particionamiento

Ejemplo:

```text
Repositorio

↓

100 documentos

↓

10 workers
```

---

# Backpressure

Cuando la capacidad sea insuficiente:

- ralentizar;
- reprogramar;
- pausar;
- rechazar.

Nunca saturar el sistema.

---

# Reintentos

Toda ejecución podrá reintentarse.

---

# Estrategias

Ejemplos:

- exponencial;
- lineal;
- inmediata.

---

# Dead Letter Queue

Las ejecuciones fallidas repetidamente podrán enviarse a una DLQ.

---

# Cancelación

Una ejecución podrá cancelarse.

---

# Reanudación

Los pipelines compatibles podrán continuar desde checkpoints.

---

# Checkpoints

Formato:

```text
CHECKPOINT
```

Permitirá continuar una ejecución larga.

---

# Estado de ejecución

```text
Queued

Running

Paused

Retrying

Completed

Cancelled

Failed
```

---

# Observabilidad

Toda operación deberá ser observable.

---

# Logs

Los logs deberán ser:

- estructurados;
- correlacionables;
- consultables.

---

# Correlation ID

Toda ejecución compartirá un identificador.

---

# Trace ID

Las operaciones distribuidas compartirán trazas.

---

# Métricas

Ejemplos:

- pipelines ejecutados;
- duración;
- throughput;
- errores;
- tiempo medio.

---

# KPIs

Ejemplos:

- éxito de ingesta;
- tiempo hasta publicación;
- tiempo medio de recuperación;
- porcentaje incremental.

---

# Trazas distribuidas

Las trazas deberán recorrer:

```text
Scheduler

↓

Worker

↓

Extractor

↓

Normalizer

↓

Validation

↓

Publication
```

---

# Dashboards

El sistema deberá proporcionar paneles operativos.

---

# Alertas

Ejemplos:

- cola saturada;
- worker caído;
- errores repetidos;
- publicación bloqueada;
- incremento anómalo de tiempos.

---

# Health Checks

Cada componente deberá exponer:

```text
Liveness

Readiness

Startup
```

---

# Recuperación

El sistema deberá recuperarse automáticamente siempre que sea posible.

---

# Estrategias

- restart;
- retry;
- failover;
- replanificación.

---

# Alta disponibilidad

No deberá existir un único punto de fallo.

---

# Seguridad operacional

La operación deberá respetar:

- autenticación;
- autorización;
- auditoría;
- cifrado;
- gestión de secretos.

---

# Secret Management

Las credenciales nunca residirán en pipelines.

---

# Observabilidad de seguridad

Los accesos deberán auditarse.

---

# CI/CD

El Ingestion Engine deberá integrarse con el pipeline DevOps.

---

# Automatización

Cada cambio podrá ejecutar:

- tests;
- validadores;
- golden tests;
- benchmarks.

---

# Canary

Las nuevas versiones podrán desplegarse parcialmente.

---

# Rollback operacional

Toda versión deberá poder revertirse.

---

# Versionado del motor

Formato recomendado:

```text
Ingestion Engine 1.0.0
```

---

# Compatibilidad

El motor deberá declarar:

- versión de esquema;
- versión de ontología;
- versión de APIs.

---

# Benchmark

Se medirán:

- documentos/segundo;
- MB/segundo;
- tiempo de publicación;
- memoria.

---

# Pruebas de carga

El motor deberá soportar:

- miles de documentos;
- múltiples pipelines;
- ejecuciones simultáneas.

---

# Operación continua

El Ingestion Engine deberá diseñarse para funcionar de manera permanente.

---

# Mantenimiento

El mantenimiento deberá realizarse con mínima interrupción.

---

# Perfil mínimo

La primera implementación debería soportar:

- Scheduler simple;
- ejecución manual;
- ejecución incremental Git;
- logging;
- métricas básicas;
- checkpoints sencillos.

---

# Perfil enterprise

Añadirá:

- Event Bus;
- Scheduler distribuido;
- escalado automático;
- observabilidad completa;
- tracing distribuido;
- alta disponibilidad;
- recuperación automática;
- múltiples pipelines concurrentes.

---

# Conclusión

El Ingestion Engine no es únicamente un conjunto de transformaciones documentales.

Constituye un sistema distribuido responsable de incorporar conocimiento al SGCC de forma continua, segura y gobernada.

Su operación deberá ser:

- observable;
- escalable;
- resiliente;
- automatizada;
- reproducible.

Con esta sexta parte queda completamente especificada la arquitectura del **Ingestion Engine**, desde la adquisición de fuentes hasta la operación continua en producción, estableciendo una base sólida para su futura implementación dentro de NovaCoquinaria.

