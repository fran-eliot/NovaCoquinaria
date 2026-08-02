---
id: SPEC-CONVENCIONES
tipo: especificacion
titulo: Convenciones para las especificaciones de NovaCoquinaria
version: 1.0.0
estado: borrador
ultima_revision: 2026-08-02
tags:
  - specifications
  - conventions
  - governance
  - architecture
  - documentation
---

# Convenciones para las especificaciones de NovaCoquinaria

---

# Parte I — Convenciones generales de documentación

---

# Introducción

Las especificaciones constituyen la fuente principal de conocimiento técnico del proyecto NovaCoquinaria.

Para garantizar que toda la documentación evolucione de forma consistente resulta necesario definir un conjunto de convenciones comunes.

Estas convenciones establecen cómo deben redactarse, organizarse, identificarse y mantenerse los documentos que forman parte de la arquitectura documental.

No describen la arquitectura funcional del sistema.

Tampoco sustituyen al glosario ni al mapa de dependencias.

Su objetivo es normalizar la forma en la que la información se presenta.

---

# Objetivos

Este documento persigue los siguientes objetivos:

- unificar el estilo documental;
- facilitar la lectura;
- mejorar la mantenibilidad;
- favorecer la automatización;
- simplificar las revisiones;
- reducir ambigüedades;
- facilitar la incorporación de nuevos colaboradores;
- servir como referencia para futuras herramientas de validación.

---

# Alcance

Estas convenciones deberán aplicarse a todos los documentos incluidos en:

```text
docs/specifications/
```

Podrán extenderse posteriormente a:

- arquitectura;
- ADR;
- documentación técnica;
- documentación funcional;
- documentación de usuario.

---

# Relación con otros documentos

Cada documento transversal responde a una pregunta distinta.

| Documento | Pregunta que responde |
|------------|----------------------|
| README | ¿Qué documentos existen? |
| DEPENDENCIAS | ¿Cómo se relacionan? |
| GLOSARIO | ¿Qué significa cada término? |
| CONVENCIONES | ¿Cómo debe escribirse? |

---

# Principios generales

Toda especificación deberá cumplir los siguientes principios.

---

## Claridad

La redacción deberá ser precisa.

Se evitarán frases ambiguas o abiertas a múltiples interpretaciones.

---

## Consistencia

Un mismo concepto deberá escribirse siempre de la misma forma.

---

## Uniformidad

Las estructuras repetidas deberán seguir un mismo formato.

---

## Modularidad

Cada documento deberá centrarse en una responsabilidad claramente delimitada.

---

## Reutilización

Cuando un concepto ya exista en otra especificación deberá referenciarse.

No deberá duplicarse.

---

## Trazabilidad

Toda afirmación importante deberá poder relacionarse con:

- una especificación;
- un contrato;
- una decisión arquitectónica;
- un cambio documentado.

---

## Evolución controlada

Las especificaciones deberán poder evolucionar sin perder coherencia histórica.

---

## Automatización

Siempre que sea posible, las convenciones deberán poder comprobarse mediante herramientas automáticas.

---

# Organización documental

---

# Un documento por responsabilidad

Cada documento deberá poseer un único propósito principal.

Ejemplo:

```text
Knowledge Graph
```

describe el modelo del grafo.

No deberá describir el funcionamiento del Retrieval.

---

# Evitar documentos monolíticos

Cuando un documento crezca excesivamente deberá dividirse en varias especificaciones.

La división deberá seguir límites conceptuales.

---

# Referencias cruzadas

Los documentos deberán enlazarse entre sí cuando exista relación conceptual.

Las referencias deberán evitar duplicar contenido.

---

# Autoridad documental

Cada concepto deberá tener un documento propietario.

Las demás especificaciones podrán referenciar dicho concepto.

No deberán redefinirlo.

---

# Estructura mínima recomendada

Toda especificación debería seguir una organización similar.

```text
Front Matter

Introducción

Objetivos

Alcance

Modelo conceptual

Componentes

Contratos

Reglas

Validaciones

Casos de uso

Antipatrones

Checklist

Referencias
```

No todos los apartados serán obligatorios.

---

# Organización por partes

Los documentos extensos podrán dividirse en partes numeradas.

Formato recomendado:

```text
Parte I

Parte II

Parte III
```

Las partes deberán mantener continuidad lógica.

---

# Encabezados

Se utilizarán encabezados Markdown.

Nivel recomendado:

```text
#

##

###
```

No se recomienda superar el cuarto nivel salvo necesidad excepcional.

---

# Títulos

Los títulos deberán:

- describir claramente el contenido;
- evitar abreviaturas innecesarias;
- mantenerse estables.

---

# Numeración

Las partes utilizarán numeración romana.

Los apartados utilizarán encabezados Markdown.

No se recomienda numeración manual tipo:

```text
1.2.3
```

cuando Markdown ya represente la jerarquía.

---

# Idioma

---

# Idioma principal

Las especificaciones deberán redactarse en español.

---

# Terminología inglesa

Los nombres técnicos ampliamente aceptados podrán mantenerse en inglés.

Ejemplos:

```text
Knowledge Graph
Engine
Workflow
Grounding
Snapshot
Embedding
```

---

# Traducciones

Cuando un término inglés sea importante podrá acompañarse de una explicación en español.

Ejemplo:

```text
Grounding (fundamentación)
```

---

# Contratos

Los nombres utilizados en:

- APIs;
- Schemas;
- IDs;
- YAML;
- JSON;
- Events;

deberán mantenerse en su forma canónica.

---

# Estilo de redacción

---

# Tiempo verbal

Se utilizará preferentemente el futuro normativo.

Ejemplo:

```text
El documento deberá...
```

en lugar de:

```text
El documento debe...
```

---

# Voz

Se recomienda voz activa.

---

# Persona

Las especificaciones deberán redactarse en tercera persona.

---

# Estilo

Se evitarán:

- opiniones;
- lenguaje coloquial;
- comentarios personales;
- humor;
- expresiones ambiguas.

---

# Terminología

Se utilizarán exclusivamente los términos definidos en:

```text
GLOSARIO.md
```

---

# Coherencia terminológica

Un término no deberá cambiar de significado entre documentos.

---

# Longitud de frases

Se recomienda:

- frases relativamente cortas;
- un concepto por párrafo;
- listas para enumeraciones.

---

# Listas

Las listas deberán utilizar Markdown estándar.

Ejemplo:

```markdown
- elemento
- elemento
- elemento
```

---

# Enumeraciones

Cuando el orden sea relevante se utilizarán listas numeradas.

---

# Negritas

Las negritas deberán reservarse para:

- conceptos importantes;
- advertencias;
- nombres relevantes.

No deberán utilizarse para decoración.

---

# Cursivas

Las cursivas podrán utilizarse para:

- términos extranjeros;
- énfasis puntual.

---

# Código

Todo identificador técnico deberá escribirse en formato de código.

Ejemplo:

```text
RagExecution
```

---

# Bloques de código

Se utilizarán para:

- YAML;
- JSON;
- pseudocódigo;
- ejemplos;
- contratos.

---

# Markdown

---

# Sintaxis

Se utilizará Markdown estándar compatible con MkDocs.

---

# Tablas

Las tablas deberán utilizar el formato estándar Markdown.

---

# Separadores

Se utilizarán líneas horizontales para separar bloques principales.

```markdown
---
```

---

# Enlaces

Los enlaces internos deberán ser relativos.

Ejemplo:

```markdown
[README](README.md)
```

---

# Imágenes

Las imágenes deberán utilizarse únicamente cuando aporten información relevante.

---

# Diagramas

Siempre que sea posible se preferirán diagramas declarativos.

---

# Front Matter

---

# Obligatoriedad

Toda especificación deberá incluir Front Matter.

---

# Posición

El Front Matter deberá aparecer al inicio del documento.

---

# Formato

Se utilizará YAML.

---

# Campos mínimos

```yaml
id:
tipo:
titulo:
version:
estado:
ultima_revision:
tags:
```

---

# Campo `id`

Deberá ser único.

---

# Campo `tipo`

Ejemplo:

```text
especificacion
```

---

# Campo `titulo`

Deberá coincidir con el título principal del documento.

---

# Campo `version`

Seguirá el versionado semántico.

---

# Campo `estado`

Valores iniciales recomendados:

```text
borrador
revision
estable
deprecated
retirado
```

---

# Campo `ultima_revision`

Formato recomendado:

```text
YYYY-MM-DD
```

---

# Campo `tags`

Lista YAML.

---

# Orden recomendado

```yaml
id
tipo
titulo
version
estado
ultima_revision
tags
```

---

# Identificadores documentales

---

# Formato

Formato recomendado:

```text
SPEC-NOMBRE
```

Ejemplos:

```text
SPEC-GLOSARIO

SPEC-DEPENDENCIAS

SPEC-APIS
```

---

# Unicidad

No podrán existir dos documentos con el mismo identificador.

---

# Estabilidad

Un ID no deberá modificarse salvo causa justificada.

---

# Nombres de archivos

---

# Idioma

Los nombres de archivo utilizarán mayúsculas para las especificaciones principales.

Ejemplo:

```text
ESPECIFICACION_DEL_RETRIEVAL_ENGINE.md
```

---

# Separadores

Se utilizará guion bajo.

---

# Extensión

Todos los documentos utilizarán:

```text
.md
```

---

# Evitar

No utilizar:

- espacios;
- caracteres especiales;
- tildes;
- nombres ambiguos.

---

# Directorios

Las carpetas deberán agrupar documentos por dominio.

Ejemplo:

```text
knowledge/

runtime/

interfaces/

ingestion/
```

---

# Responsabilidad de directorios

Cada directorio representará un dominio arquitectónico.

No deberá utilizarse como simple agrupación arbitraria.

---

# Estados documentales

Los documentos podrán encontrarse en distintos estados.

---

# Borrador

Documento en elaboración.

---

# Revisión

Documento sometido a revisión.

---

# Estable

Documento aceptado como referencia.

---

# Deprecated

Documento sustituido pero todavía disponible.

---

# Retirado

Documento fuera de uso.

---

# Transiciones

La transición entre estados deberá quedar registrada.

---

# Versionado documental

---

# Esquema

Se utilizará Semantic Versioning.

```text
MAJOR.MINOR.PATCH
```

---

# Cambio mayor

Cuando cambie la compatibilidad documental.

---

# Cambio menor

Cuando se añada contenido compatible.

---

# Cambio PATCH

Cuando únicamente existan:

- correcciones;
- aclaraciones;
- erratas.

---

# Compatibilidad

Siempre que sea posible deberá preservarse la compatibilidad documental.

---

# Referencias internas

---

# Referencias relativas

Siempre deberán utilizarse rutas relativas.

---

# Referencias explícitas

Las referencias deberán apuntar al documento concreto.

No a un directorio.

---

# Referencias circulares

Podrán existir cuando aporten contexto.

No deberán generar dependencia conceptual circular.

---

# Estado de esta parte

Con esta primera parte quedan definidas:

- las convenciones generales;
- la estructura documental;
- el estilo de redacción;
- el uso de Markdown;
- el Front Matter;
- los identificadores;
- la organización de directorios;
- el versionado documental;
- las referencias internas.

---

# Transición hacia la Parte II

La Parte II desarrollará las convenciones relativas a modelos, contratos y elementos técnicos, incluyendo:

- YAML;
- JSON;
- Schemas;
- DTO;
- APIs;
- Events;
- Engines;
- Runtime;
- estados;
- enums;
- contratos;
- compatibilidad;
- nombres canónicos;
- modelos de datos;
- estructuras reutilizables.

---

# Parte II — Convenciones para modelos, contratos, APIs y componentes técnicos

---

# Introducción

Esta segunda parte establece las convenciones aplicables a todos los artefactos técnicos definidos por las especificaciones.

Su objetivo es asegurar que:

- los contratos sean consistentes;
- los modelos sean homogéneos;
- las APIs compartan una misma filosofía de diseño;
- los Engines utilicen una terminología uniforme;
- las estructuras puedan validarse automáticamente.

Las reglas aquí descritas deberán aplicarse siempre que una especificación defina contratos consumibles por otros componentes.

---

# Principios generales

Los contratos deberán ser:

- explícitos;
- deterministas;
- versionables;
- compatibles;
- autocontenidos;
- trazables.

Siempre que sea posible deberán expresarse mediante un esquema formal.

---

# Convenciones para YAML

---

# Objetivo

YAML será el formato principal para representar:

- Front Matter;
- ejemplos de configuración;
- contratos declarativos;
- Quality Gates;
- diagnósticos;
- workflows;
- políticas.

---

# Estilo

Se utilizará:

- indentación de dos espacios;
- espacios en lugar de tabuladores;
- claves en minúsculas cuando representen atributos;
- listas mediante guiones.

Ejemplo:

```yaml
workflow:
  id: WF-001
  version: 1.0.0

  activities:
    - validate
    - retrieve
    - generate
```

---

# Orden de campos

Siempre que sea posible se mantendrá un orden estable.

Ejemplo recomendado:

```yaml
id:
type:
version:
status:
metadata:
configuration:
```

---

# Valores booleanos

Se utilizarán:

```yaml
true
false
```

No deberán emplearse variantes como:

```yaml
yes
no
on
off
```

---

# Valores nulos

Se utilizará:

```yaml
null
```

o la ausencia del campo cuando el contrato lo permita.

---

# Comentarios

Los comentarios deberán utilizarse únicamente cuando aporten información relevante.

---

# Convenciones para JSON

---

# Objetivo

JSON se utilizará para representar:

- Requests;
- Responses;
- eventos;
- ejemplos de APIs;
- contratos externos.

---

# Estilo

Los nombres de propiedades utilizarán:

```text
camelCase
```

Ejemplo:

```json
{
  "requestId": "...",
  "conversationId": "...",
  "ragExecutionId": "..."
}
```

---

# Nombres de propiedades

Deberán ser:

- claros;
- estables;
- coherentes;
- suficientemente descriptivos.

---

# Campos opcionales

Los contratos deberán indicar explícitamente cuándo un campo es opcional.

---

# Nullability

Siempre deberá quedar definida.

No deberá deducirse.

---

# Convenciones para Schemas

---

# Autoridad

Todo Schema deberá tener una especificación propietaria.

---

# Versionado

Cada Schema deberá disponer de:

- versión;
- compatibilidad;
- historial de cambios.

---

# Reutilización

Los Schemas reutilizables deberán referenciarse.

No copiarse.

---

# Compatibilidad

Las modificaciones incompatibles requerirán incremento de versión mayor.

---

# Validación

Todo Schema deberá poder validarse automáticamente.

---

# Convenciones para modelos

---

# Modelo lógico

Describe el dominio.

No depende de tecnologías concretas.

---

# Modelo físico

Representa una implementación concreta.

No deberá confundirse con el modelo lógico.

---

# Modelo canónico

Representación oficial utilizada para intercambiar información entre componentes.

---

# DTO

Los DTO deberán representar exclusivamente intercambio de datos.

No contendrán lógica de negocio.

---

# Request DTO

Representa información enviada por un consumidor.

---

# Response DTO

Representa información devuelta por un proveedor.

---

# Internal DTO

Representa intercambio interno entre componentes.

---

# View Model

Representación adaptada para una interfaz concreta.

---

# Projection

Representación parcial de un modelo.

---

# Naming de DTO

Formato recomendado:

```text
RetrieveRequest

RetrieveResponse

ConversationSummary

EvidenceRecord
```

---

# Convenciones para APIs

---

# Diseño

Las APIs deberán ser:

- coherentes;
- predecibles;
- consistentes;
- versionables.

---

# Recursos

Las APIs deberán diseñarse alrededor de Resources.

No alrededor de acciones.

---

# Endpoints

Se utilizarán nombres en plural cuando representen colecciones.

Ejemplo:

```text
/api/v1/conversations
```

---

# Verbos HTTP

Se respetará su semántica.

| Método | Uso recomendado |
|----------|----------------|
| GET | Consulta |
| POST | Creación o ejecución |
| PUT | Sustitución completa |
| PATCH | Actualización parcial |
| DELETE | Eliminación |

---

# Versionado

Las APIs deberán versionarse explícitamente.

Ejemplo:

```text
/api/v1/
```

---

# Operaciones

Los nombres deberán expresar intención.

Ejemplo:

```text
retrieveEvidence

createConversation

cancelExecution
```

---

# Errores

Los errores deberán utilizar un contrato uniforme.

---

# Problem Details

Siempre que sea posible se utilizará un formato homogéneo.

---

# Diagnósticos

Los códigos deberán permanecer estables.

---

# Warnings

Los warnings no deberán impedir el procesamiento correcto.

---

# Convenciones para Events

---

# Naming

Formato recomendado:

```text
ConversationCreated

RetrievalCompleted

WorkflowFinished
```

---

# Tiempo verbal

Los Events describen hechos ocurridos.

Por tanto utilizarán participio o pasado.

---

# Event Types

Serán estables.

---

# Versionado

Cada Event dispondrá de versión propia.

---

# Payload

El Payload contendrá únicamente información necesaria.

---

# Metadata

Todo Event podrá incluir:

- timestamp;
- correlationId;
- eventVersion;
- producer.

---

# Convenciones para Engines

---

# Naming

Todos los Engines utilizarán el sufijo:

```text
Engine
```

Ejemplos:

```text
Retrieval Engine

Validation Engine

Reasoning Engine

RAG Engine
```

---

# Responsabilidad

Cada Engine deberá tener una responsabilidad claramente definida.

---

# Capacidades

Las Capabilities deberán describirse mediante nombres funcionales.

Ejemplo:

```text
semanticRetrieval

graphTraversal

hybridSearch
```

---

# Operaciones

Cada operación deberá tener:

- entrada;
- salida;
- errores;
- restricciones.

---

# Estados

Los estados deberán definirse explícitamente.

---

# Compatibilidad

Las modificaciones incompatibles requerirán nueva versión.

---

# Convenciones para Runtime

---

# Contextos

Todo Context deberá especializarse.

Ejemplos:

```text
RagContext

TenantContext

ExecutionContext

WorkflowExecutionContext
```

---

# Ejecuciones

Las ejecuciones deberán diferenciar:

- definición;
- instancia;
- resultado.

---

# Resultados

No deberá utilizarse únicamente:

```text
Result
```

Deberá especializarse.

---

# Identificadores

Toda ejecución deberá disponer de:

```text
Execution ID
```

---

# Estados

Los estados deberán definirse mediante enumeraciones.

---

# Convenciones para enumeraciones

---

# Formato

Los valores utilizarán:

```text
snake_case
```

cuando representen contratos.

Ejemplo:

```text
pending

running

completed

failed

cancelled
```

---

# Estabilidad

Los valores no deberán cambiar salvo cambio mayor.

---

# Valores reservados

Cuando sea posible se reservarán estados para futuras ampliaciones.

---

# Convenciones para identificadores

---

# IDs

Todo recurso persistente deberá disponer de un identificador estable.

---

# Prefijos

Se recomienda utilizar prefijos cuando existan varios tipos.

Ejemplo:

```text
CONV-

RAG-

WF-

ENG-
```

---

# Legibilidad

Los IDs destinados a personas deberán ser legibles.

---

# UUID

Podrá utilizarse cuando la unicidad global sea prioritaria.

---

# Convenciones para nombres

---

# Componentes

Se utilizará PascalCase.

Ejemplo:

```text
ReasoningEngine

EvidenceSet

ConversationSummary
```

---

# Variables YAML

Preferentemente:

```text
snake_case
```

---

# Variables JSON

Preferentemente:

```text
camelCase
```

---

# Archivos

Mayúsculas para documentos principales.

---

# Directorios

Minúsculas.

---

# Convenciones para compatibilidad

---

# Breaking Change

Toda modificación incompatible deberá declararse.

---

# Deprecation

Los cambios compatibles deberán pasar primero por deprecation cuando sea posible.

---

# Sunset

Las retiradas deberán anunciarse.

---

# Migración

Toda ruptura deberá acompañarse de instrucciones de migración.

---

# Estado de esta parte

Con esta segunda parte quedan establecidas las convenciones relativas a:

- YAML;
- JSON;
- Schemas;
- modelos;
- DTO;
- APIs;
- Events;
- Engines;
- Runtime;
- enumeraciones;
- identificadores;
- compatibilidad y versionado técnico.

---

# Transición hacia la Parte III

La Parte III desarrollará las convenciones específicas para la documentación, incluyendo:

- tablas;
- diagramas;
- pseudocódigo;
- ejemplos;
- referencias;
- ADR;
- notas;
- advertencias;
- diagnósticos;
- métricas;
- Quality Gates;
- checklists;
- formatos reutilizables.

---

# Parte III — Convenciones para documentación, ejemplos, referencias y elementos reutilizables

---

# Introducción

Las convenciones descritas en esta parte regulan la forma en que debe presentarse la información dentro de las especificaciones.

Su objetivo es conseguir que todos los documentos del proyecto mantengan una estructura visual y semántica homogénea, facilitando:

- la lectura;
- la revisión;
- la navegación;
- la generación automática de documentación;
- la validación documental.

---

# Organización de capítulos

---

# Introducción

Toda especificación debería comenzar con una breve introducción que explique:

- qué describe;
- qué no describe;
- por qué existe.

---

# Objetivos

Siempre que resulte útil deberán enumerarse explícitamente.

Ejemplo:

```text
Objetivos

• definir el contrato
• establecer restricciones
• facilitar la implementación
• permitir validación automática
```

---

# Alcance

Deberá indicar claramente:

- qué cubre;
- qué queda fuera;
- relaciones con otros documentos.

---

# Modelo conceptual

Cuando el documento describa un dominio complejo deberá incorporar un modelo conceptual antes de entrar en detalles técnicos.

---

# Componentes

Cada componente importante deberá describirse de forma independiente.

---

# Reglas

Las reglas deberán agruparse por responsabilidad.

No deberán aparecer dispersas a lo largo del documento.

---

# Casos de uso

Siempre que un documento describa procesos complejos deberán incluirse ejemplos prácticos.

---

# Antipatrones

Los errores frecuentes deberán documentarse explícitamente.

---

# Checklist

Siempre que una especificación describa procesos verificables deberá finalizar con un checklist.

---

# Referencias

Las referencias deberán aparecer al final del documento.

---

# Convenciones para ejemplos

---

# Objetivo

Los ejemplos deberán facilitar la comprensión.

No sustituirán la especificación formal.

---

# Coherencia

Todos los ejemplos deberán respetar las reglas definidas por el documento.

---

# Realismo

Los ejemplos deberán representar situaciones plausibles.

---

# Independencia

Cada ejemplo deberá poder comprenderse sin depender de otro ejemplo anterior.

---

# Ejemplos de YAML

Siempre deberán ser válidos sintácticamente.

---

# Ejemplos JSON

Deberán representar contratos completos cuando sea posible.

---

# Ejemplos de APIs

Se recomienda mostrar:

- Request;
- Response;
- Error;
- Problem Details.

---

# Ejemplos de estados

Siempre deberán mostrar estados válidos.

---

# Ejemplos negativos

Cuando resulte útil se incluirán ejemplos incorrectos acompañados de la explicación correspondiente.

---

# Convenciones para pseudocódigo

---

# Objetivo

El pseudocódigo describe comportamiento.

No implementación.

---

# Nivel de detalle

Debe ser suficiente para comprender el algoritmo.

No deberá depender de un lenguaje concreto.

---

# Estilo

Se recomienda utilizar bloques de código.

Ejemplo:

```text
Validar entrada

Recuperar candidatos

Seleccionar evidencia

Generar respuesta

Validar grounding

Construir respuesta final
```

---

# Convenciones para diagramas

---

# Diagramas permitidos

Se recomienda utilizar:

- Mermaid;
- PlantUML;
- diagramas declarativos;
- tablas cuando resulten suficientes.

---

# Diagramas de flujo

Deberán representar únicamente el flujo principal.

---

# Diagramas de componentes

Cada componente deberá mantener el mismo nombre utilizado en el Glosario.

---

# Diagramas de dependencias

Deberán coincidir con:

```text
DEPENDENCIAS.md
```

---

# Diagramas temporales

Los eventos deberán respetar el orden real de ejecución.

---

# Convenciones para tablas

---

# Objetivo

Las tablas deberán utilizarse cuando faciliten la comparación.

---

# Encabezados

Los encabezados deberán ser breves y claros.

---

# Orden

Las filas deberán seguir un criterio estable.

Ejemplos:

- alfabético;
- cronológico;
- jerárquico.

---

# Columnas

Se evitarán tablas excesivamente anchas.

---

# Contenido

Las tablas no deberán contener párrafos largos.

---

# Convenciones para notas

---

# Nota

Las notas aportan información complementaria.

No modifican el significado del documento.

---

# Advertencia

Las advertencias indican riesgos o aspectos importantes.

---

# Recomendación

Las recomendaciones describen buenas prácticas.

No constituyen requisitos obligatorios.

---

# Observación

Las observaciones aclaran un concepto.

---

# Restricción

Las restricciones representan requisitos obligatorios.

---

# Convenciones para referencias

---

# Referencias internas

Siempre deberán utilizar rutas relativas.

---

# Referencias externas

Cuando existan deberán citar:

- estándar;
- RFC;
- especificación;
- documentación oficial.

---

# Referencias a ADR

Formato recomendado:

```text
ADR-0007
```

acompañado de su enlace correspondiente.

---

# Referencias cruzadas

Cuando un concepto pertenezca a otra especificación deberá enlazarse.

---

# Evitar

No copiar contenido procedente de otra especificación.

---

# Convenciones para diagnósticos

---

# Objetivo

Los diagnósticos deberán ser:

- únicos;
- legibles;
- estables.

---

# Formato recomendado

```text
PREFIX_CATEGORIA_ERROR
```

Ejemplo:

```text
RUNTIME_ENGINE_NOT_FOUND

GLOSSARY_DUPLICATED_TERM

VALIDATION_SCHEMA_INVALID
```

---

# Severidad

Se utilizarán los niveles definidos por el Glosario.

---

# Descripción

Cada diagnóstico deberá incluir una explicación comprensible.

---

# Acción recomendada

Siempre que sea posible deberá indicar cómo resolver el problema.

---

# Convenciones para métricas

---

# Objetivo

Las métricas deberán ser:

- objetivas;
- repetibles;
- automatizables.

---

# Naming

Formato recomendado:

```text
snake_case
```

Ejemplo:

```text
documents_total

engines_registered

retrieval_latency

grounded_claim_ratio
```

---

# Unidad

Toda métrica deberá indicar su unidad.

---

# Convenciones para Quality Gates

---

# Objetivo

Los Quality Gates deberán representar criterios verificables.

---

# Estructura

Se recomienda el siguiente formato:

```yaml
quality_gate:
  id:
  criteria:
```

---

# Requisitos

Los criterios deberán ser:

- medibles;
- objetivos;
- verificables.

---

# Independencia

Cada criterio deberá poder evaluarse sin interpretación humana.

Siempre que sea posible.

---

# Convenciones para Checklists

---

# Objetivo

Los checklists deberán facilitar revisiones.

---

# Formato

Markdown estándar.

Ejemplo:

```text
[ ] criterio

[ ] criterio

[x] criterio
```

---

# Organización

Los criterios deberán agruparse por responsabilidad.

---

# Completitud

El checklist deberá cubrir los aspectos importantes del documento.

---

# Convenciones para ejemplos reutilizables

---

# Fragmentos reutilizables

Cuando un ejemplo aparezca en varios documentos deberá mantenerse una única versión de referencia.

---

# Evitar duplicación

Los ejemplos repetidos deberán sustituirse por referencias.

---

# Versionado

Los ejemplos relevantes deberán evolucionar junto con los contratos que representan.

---

# Convenciones para bloques de código

---

# Lenguaje

Siempre que sea posible deberá indicarse el lenguaje.

Ejemplos:

```text
```yaml
```

```json
```

```text
```

---

# Longitud

Los bloques deberán contener únicamente la información necesaria.

---

# Formato

La indentación deberá mantenerse consistente.

---

# Convenciones para nomenclatura visual

---

# Separadores

Las secciones principales utilizarán:

```text
---
```

---

# Espaciado

Se dejará una línea en blanco entre bloques principales.

---

# Encabezados repetidos

No deberán existir dos encabezados idénticos dentro del mismo nivel jerárquico.

---

# Consistencia visual

Los documentos deberán mantener un aspecto uniforme.

---

# Convenciones para enlaces

---

# Texto del enlace

Deberá describir claramente el destino.

---

# Evitar

No utilizar:

```text
pincha aquí
```

---

# Destinos

Los enlaces deberán permanecer válidos tras reorganizaciones razonables del proyecto.

---

# Convenciones para listas

---

# Listas simples

Utilizarán guiones.

---

# Listas numeradas

Se utilizarán únicamente cuando el orden sea importante.

---

# Profundidad

No se recomienda superar tres niveles de anidamiento.

---

# Estado de esta parte

Con esta tercera parte quedan definidas las convenciones relativas a:

- organización documental;
- ejemplos;
- pseudocódigo;
- diagramas;
- tablas;
- referencias;
- notas;
- advertencias;
- diagnósticos;
- métricas;
- Quality Gates;
- checklists;
- bloques reutilizables;
- estilo visual.

---

# Transición hacia la Parte IV

La Parte IV cerrará el documento describiendo las convenciones relativas a:

- gobernanza documental;
- automatización;
- validaciones;
- herramientas;
- integración con el pipeline documental;
- antipatrones;
- control de calidad;
- conformidad global;
- mantenimiento evolutivo de las especificaciones.

---

# Parte IV — Gobernanza documental, automatización, validación y conformidad global

---

# Introducción

Las tres partes anteriores han establecido:

- la estructura general de las especificaciones;
- las convenciones para modelos y contratos;
- las normas de presentación documental.

Esta cuarta parte define cómo deberán mantenerse, evolucionar y validarse las especificaciones a lo largo del tiempo.

Su objetivo es garantizar que la documentación pueda crecer sin perder coherencia, consistencia ni capacidad de automatización.

---

# Gobernanza documental

---

# Objetivo

La gobernanza documental garantiza que todas las especificaciones evolucionen de forma coordinada.

---

# Principios

La gobernanza deberá asegurar:

- coherencia;
- trazabilidad;
- consistencia;
- mantenibilidad;
- automatización;
- evolución controlada.

---

# Documento propietario

Cada concepto deberá tener un único documento considerado autoridad.

Las modificaciones deberán realizarse siempre en dicho documento.

---

# Responsabilidades

Cada especificación deberá tener:

- propietario documental;
- revisores;
- consumidores identificados cuando proceda.

---

# Cambios

Toda modificación significativa deberá quedar reflejada en:

- historial documental;
- versión;
- Bitácora del proyecto cuando corresponda.

---

# Ciclo de vida documental

---

# Estados

Las especificaciones evolucionarán mediante estados bien definidos.

```text
Borrador
        ↓

Revisión
        ↓

Estable
        ↓

Deprecated
        ↓

Retirado
```

---

# Cambios compatibles

Podrán incorporarse mediante incremento MINOR.

---

# Cambios incompatibles

Requerirán incremento MAJOR y documentación de migración.

---

# Erratas

Las correcciones editoriales utilizarán incrementos PATCH.

---

# Automatización

---

# Objetivo

Siempre que sea posible las convenciones deberán comprobarse automáticamente.

La revisión manual deberá reservarse para aspectos semánticos o arquitectónicos.

---

# Herramientas actuales

Las especificaciones deberán ser compatibles con las herramientas del proyecto.

Ejemplos:

```text
validate_all.py

validate_semantics.py

generate_graph.py

build_site_docs.py
```

---

# Futuras herramientas

Las convenciones deberán permitir incorporar nuevas herramientas sin modificar la estructura documental.

---

# Validaciones automáticas

---

# Front Matter

Se comprobará:

- existencia;
- formato;
- campos obligatorios;
- unicidad del identificador.

---

# Identificadores

Se validará:

- unicidad;
- formato;
- estabilidad.

---

# Enlaces

Toda referencia interna deberá ser resoluble.

---

# Referencias rotas

No deberán existir enlaces a documentos inexistentes.

---

# Grafo documental

Las relaciones documentales deberán poder representarse mediante un Knowledge Graph.

---

# Dependencias

Las dependencias deberán ser compatibles con:

```text
DEPENDENCIAS.md
```

---

# Terminología

Los términos deberán coincidir con:

```text
GLOSARIO.md
```

---

# Convenciones

Las especificaciones deberán respetar este documento.

---

# Integración con el pipeline documental

---

# Pipeline

Toda modificación importante debería validarse antes de integrarse en la rama principal.

---

# Validaciones mínimas

Se recomienda ejecutar:

```text
validate_all.py
```

---

Posteriormente:

```text
validate_semantics.py
```

---

Finalmente:

```text
build_site_docs.py
```

---

Cuando proceda también:

```text
generate_graph.py
```

---

# Resultado esperado

El pipeline documental deberá finalizar sin:

- errores;
- referencias rotas;
- conflictos de identificadores.

---

# Quality Gates documentales

---

# Objetivo

Los Quality Gates representan criterios objetivos de aceptación.

---

# Front Matter

```yaml
quality_gate:
  id: QG-DOC-FRONTMATTER

  criteria:
    all:
      - frontmatter_exists == true
      - mandatory_fields_present == true
      - unique_identifier == true
```

---

# Referencias

```yaml
quality_gate:
  id: QG-DOC-REFERENCES

  criteria:
    all:
      - internal_links_valid == true
      - external_links_valid == true
      - authority_references_present == true
```

---

# Terminología

```yaml
quality_gate:
  id: QG-DOC-GLOSSARY

  criteria:
    all:
      - canonical_terms_used == true
      - forbidden_terms_absent == true
      - deprecated_terms_reported == true
```

---

# Dependencias

```yaml
quality_gate:
  id: QG-DOC-DEPENDENCIES

  criteria:
    all:
      - authority_defined == true
      - consumers_identified == true
      - dependency_cycles_controlled == true
```

---

# Calidad documental

```yaml
quality_gate:
  id: QG-DOC-QUALITY

  criteria:
    all:
      - duplicated_sections_absent == true
      - broken_examples_absent == true
      - orphan_documents_absent == true
      - markdown_valid == true
```

---

# Conformidad global

```yaml
quality_gate:
  id: QG-DOC-GLOBAL

  criteria:
    all:
      - documentation_pipeline_passed == true
      - glossary_consistent == true
      - dependencies_consistent == true
      - frontmatter_valid == true
      - references_valid == true
```

---

# Antipatrones

---

## Duplicar conceptos

Un concepto no deberá definirse en varios documentos.

---

## Copiar documentación

Cuando un contenido pertenezca a otra especificación deberá enlazarse.

---

## Cambiar nombres arbitrariamente

Los nombres canónicos deberán mantenerse estables.

---

## Mantener documentación obsoleta

Todo documento deprecated deberá indicar claramente su sustitución.

---

## Crear documentos sin propietario

Toda especificación deberá tener una autoridad documental.

---

## Referencias circulares innecesarias

Las referencias deberán aportar contexto.

No crear ciclos por simple organización.

---

## Introducir terminología nueva sin actualizar el glosario

Todo concepto transversal deberá incorporarse previamente al Glosario.

---

## Añadir dependencias ocultas

Las dependencias relevantes deberán reflejarse en:

```text
DEPENDENCIAS.md
```

---

## Saltarse el pipeline documental

Toda modificación importante deberá validarse antes de integrarse.

---

## Corregir únicamente la documentación generada

Los cambios deberán realizarse siempre sobre los documentos fuente.

Nunca sobre la documentación generada.

---

# Checklist para nuevas especificaciones

```text
[ ] Existe Front Matter.
[ ] Existe identificador único.
[ ] El documento tiene propietario.
[ ] Se han definido objetivos.
[ ] Se ha definido el alcance.
[ ] La terminología coincide con el Glosario.
[ ] Las dependencias están documentadas.
[ ] Existen referencias cruzadas.
[ ] Los ejemplos son válidos.
[ ] Los enlaces funcionan.
[ ] El documento supera validate_all.py.
```

---

# Checklist para modificaciones

```text
[ ] La versión se ha actualizado cuando corresponde.
[ ] No se rompe compatibilidad sin documentarlo.
[ ] Se actualizan referencias.
[ ] Se actualiza DEPENDENCIAS.md si procede.
[ ] Se actualiza GLOSARIO.md si aparecen nuevos términos.
[ ] Se revisan los documentos consumidores.
[ ] Se ejecuta el pipeline documental.
```

---

# Checklist previo a una Release

```text
[ ] Todos los documentos validan correctamente.
[ ] No existen enlaces rotos.
[ ] No existen Front Matter inválidos.
[ ] No existen identificadores duplicados.
[ ] No existen documentos huérfanos sin justificación.
[ ] El Knowledge Graph se genera correctamente.
[ ] La documentación del sitio se construye correctamente.
[ ] Las referencias entre especificaciones son consistentes.
```

---

# Integración con el resto del proyecto

Este documento complementa:

| Documento | Responsabilidad |
|-----------|-----------------|
| README.md | Organización general de las especificaciones |
| DEPENDENCIAS.md | Relaciones entre documentos |
| GLOSARIO.md | Terminología oficial |
| CONVENCIONES.md | Reglas de redacción y mantenimiento |

---

# Evolución futura

Las convenciones deberán evolucionar cuando aparezcan:

- nuevos dominios;
- nuevas herramientas;
- nuevos tipos documentales;
- nuevas necesidades de automatización.

Los cambios deberán priorizar siempre la compatibilidad con la documentación existente.

---

# Estado final del documento

```text
Documento:
docs/specifications/CONVENCIONES.md

Versión:
1.0.0

Estado:
borrador

Dominio:
Documentación transversal

Partes:
4 / 4

Madurez:
Nivel 4 — Especificación completa

Estado de redacción:
FINALIZADA
```

---

# Referencias

- [README](README.md)
- [DEPENDENCIAS](DEPENDENCIAS.md)
- [GLOSARIO](GLOSARIO.md)
- [ARQUITECTURA](../architecture/ARQUITECTURA.md)
- [VISION](../VISION.md)
- [ROADMAP](../management/ROADMAP.md)
- [ADR](../governance/adr/README.md)

---

# Conclusión

Las convenciones constituyen la base normativa de las especificaciones de NovaCoquinaria.

Mientras que:

- **README** organiza los documentos;
- **DEPENDENCIAS** describe sus relaciones;
- **GLOSARIO** define el significado de los conceptos;

**CONVENCIONES** establece cómo deben redactarse, identificarse, versionarse, validarse y mantenerse.

Su cumplimiento permite que la documentación:

- sea homogénea;
- pueda evolucionar de forma controlada;
- sea verificable mediante herramientas automáticas;
- sirva como fuente fiable para desarrolladores, agentes de IA y futuras implementaciones.

Con esta cuarta parte queda completado `CONVENCIONES.md`, cerrando el conjunto de documentos transversales fundamentales de la carpeta `docs/specifications`.
