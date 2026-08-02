---
id: SPEC-VALIDACION
tipo: especificacion
titulo: Especificación de Validación
version: 1.0.0
estado: borrador
ultima_revision: 2026-08-02
tags:
  - validation
  - quality-gates
  - diagnostics
  - constraints
  - architecture
---

# Parte I — Fundamentos y arquitectura del Validation Engine

---

# Introducción

La calidad del conocimiento constituye uno de los pilares fundamentales del Sistema de Gestión del Conocimiento Culinario (SGCC). La capacidad de adquirir información desde múltiples fuentes resulta insuficiente si el sistema no dispone de mecanismos que permitan garantizar que dicho conocimiento es consistente, trazable, coherente y conforme al modelo conceptual definido por NovaCoquinaria.

El **Validation Engine** es el componente responsable de evaluar sistemáticamente todos los artefactos generados durante el ciclo de vida del conocimiento antes de que puedan incorporarse al ecosistema del SGCC.

A diferencia del Ingestion Engine, cuyo objetivo consiste en transformar información heterogénea en representaciones normalizadas, el Validation Engine determina si dichas representaciones cumplen las restricciones arquitectónicas, ontológicas y de gobernanza establecidas por el sistema.

La validación constituye, por tanto, la frontera entre el conocimiento candidato y el conocimiento aceptado.

---

# Objetivos

Esta especificación persigue los siguientes objetivos:

- definir la arquitectura del Validation Engine;
- establecer el modelo conceptual de validación;
- diferenciar validación, razonamiento e inferencia;
- definir el ciclo de vida de una validación;
- establecer los distintos niveles de validación;
- introducir el concepto de restricción (Constraint);
- definir la arquitectura de validadores;
- establecer la interacción con el resto del Knowledge Engine;
- preparar el modelo que se desarrollará en las siguientes partes.

---

# Alcance

Esta especificación describe el funcionamiento interno del Validation Engine como componente del Knowledge Engine.

Incluye:

- arquitectura;
- responsabilidades;
- principios;
- tipos de validación;
- flujo general;
- integración con otros motores.

No describe en detalle:

- las restricciones individuales;
- las reglas de negocio concretas;
- los perfiles SHACL;
- la implementación tecnológica.

Estos aspectos se desarrollarán en las siguientes partes.

---

# Papel del Validation Engine

Dentro del SGCC, el Validation Engine constituye el responsable de verificar que todo conocimiento cumple las reglas necesarias antes de poder utilizarse como conocimiento oficial.

Su función principal puede resumirse como:

```text
Conocimiento candidato
        ↓
Validation Engine
        ↓
Conocimiento validado
```

El motor no genera conocimiento.

Tampoco realiza inferencias complejas.

Su misión consiste en evaluar la conformidad del conocimiento respecto al modelo definido por el sistema.

---

# Posición dentro del Knowledge Engine

La arquitectura general puede representarse de la siguiente forma:

```text
Fuentes
      │
      ▼
Ingestion Engine
      │
      ▼
Knowledge Package
      │
      ▼
Validation Engine
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

El Validation Engine constituye el último control antes de que el conocimiento pase a formar parte del Knowledge Graph.

---

# Misión

La misión del Validation Engine consiste en garantizar que todo conocimiento publicado sea:

- estructuralmente correcto;
- semánticamente consistente;
- ontológicamente válido;
- trazable;
- gobernado;
- reproducible.

---

# Visión

El Validation Engine deberá convertirse en el sistema central de aseguramiento de calidad del conocimiento de NovaCoquinaria.

No se limitará a validar documentos.

Validará cualquier artefacto gestionado por el SGCC:

- documentos;
- componentes;
- entidades;
- relaciones;
- colecciones;
- grafos;
- ontologías;
- afirmaciones;
- Knowledge Packages.

---

# Principios

El Validation Engine deberá diseñarse siguiendo los siguientes principios.

---

## Determinismo

La misma entrada deberá producir siempre el mismo resultado cuando:

- el conjunto de restricciones;
- las ontologías;
- la configuración;
- el entorno;

permanezcan constantes.

---

## Reproducibilidad

Toda validación deberá poder ejecutarse nuevamente produciendo exactamente las mismas conclusiones.

---

## Explicabilidad

Toda decisión deberá poder justificarse.

No deberán existir errores cuya causa no pueda identificarse.

---

## Independencia tecnológica

El modelo conceptual no dependerá de una tecnología concreta.

La arquitectura deberá ser compatible con:

- RDF;
- Neo4j;
- PostgreSQL;
- GraphDB;
- otros motores.

---

## Modularidad

Las restricciones deberán ser independientes entre sí.

La incorporación de nuevas reglas no deberá requerir modificar el motor principal.

---

## Escalabilidad

El sistema deberá permitir miles de reglas y millones de elementos sin modificar el modelo conceptual.

---

## Incrementalidad

Siempre que sea posible, únicamente deberán reevaluarse los elementos afectados por un cambio.

---

## Idempotencia

Ejecutar varias veces una misma validación no deberá alterar el estado del conocimiento.

---

## No destructividad

La validación nunca modificará directamente el conocimiento.

Solo emitirá resultados.

Las modificaciones corresponderán a otros componentes.

---

## Gobernanza

Toda validación deberá ser auditable.

---

# ¿Qué es validar?

Validar consiste en comprobar si un artefacto satisface un conjunto de restricciones definidas por el sistema.

Formalmente:

```text
Artefacto

+

Restricciones

↓

Resultado
```

---

# ¿Qué no es validar?

El Validation Engine no:

- deduce conocimiento nuevo;
- modifica documentos;
- crea entidades;
- corrige automáticamente errores;
- publica conocimiento;
- toma decisiones editoriales.

---

# Diferencia entre validación y razonamiento

Frecuentemente ambos conceptos se confunden.

Sin embargo representan procesos diferentes.

---

## Validación

Pregunta:

```text
¿Cumple las reglas?
```

Ejemplo:

```text
Una receta tiene al menos un ingrediente.
```

Resultado:

```text
Sí

No
```

---

## Razonamiento

Pregunta:

```text
¿Qué nuevo conocimiento puede deducirse?
```

Ejemplo:

```text
La receta contiene soja.

↓

Puede contener alérgenos.
```

---

# Diferencia con GraphRAG

GraphRAG responde preguntas.

Validation verifica conocimiento.

---

# Diferencia con Ingestion

Ingestion transforma.

Validation evalúa.

---

# Diferencia con Ontología

La ontología define el modelo.

Validation comprueba que dicho modelo se respeta.

---

# Concepto de validación

Una validación puede definirse como:

```text
Validation =
Target
+
Rule Set
+
Execution Context
+
Result
```

---

# Objeto de validación

El objeto validado recibe el nombre de:

```text
Validation Target
```

Podrá ser:

- documento;
- componente;
- receta;
- entidad;
- relación;
- colección;
- ontología;
- Knowledge Package;
- subgrafo.

---

# Resultado

Toda validación generará un resultado estructurado.

Nunca únicamente un valor booleano.

---

# Arquitectura lógica

El Validation Engine podrá representarse como:

```text
Validation Request
        │
        ▼
Target Resolver
        │
        ▼
Constraint Manager
        │
        ▼
Execution Planner
        │
        ▼
Validators
        │
        ▼
Diagnostics
        │
        ▼
Quality Gates
        │
        ▼
Validation Report
```

---

# Componentes principales

La arquitectura estará formada por los siguientes componentes.

---

## Validation API

Recibe solicitudes de validación.

---

## Target Resolver

Localiza el objeto que debe validarse.

---

## Constraint Manager

Gestiona todas las restricciones registradas.

---

## Execution Planner

Decide qué validadores deben ejecutarse.

---

## Validation Runtime

Coordina la ejecución.

---

## Validator Registry

Mantiene el catálogo de validadores.

---

## Diagnostics Engine

Genera errores y advertencias.

---

## Quality Gate Manager

Evalúa criterios de aceptación.

---

## Validation Report Builder

Construye el informe final.

---

## Audit Manager

Registra toda la ejecución.

---

# Ciclo general

El proceso completo puede resumirse como:

```text
Solicitud

↓

Resolver objetivo

↓

Seleccionar restricciones

↓

Ejecutar validadores

↓

Generar diagnósticos

↓

Aplicar Quality Gates

↓

Emitir informe
```

---

# Validation Request

Toda validación comienza mediante una solicitud.

Formato conceptual:

```yaml
validation_request:

  target:

  profile:

  scope:

  execution_mode:
```

---

# Validation Target

Representa aquello que se desea validar.

Ejemplos:

```text
REC-0008

Knowledge Package

Colección

Ontología

Knowledge Graph
```

---

# Validation Scope

Determina el alcance.

Ejemplos:

```text
Single Document

Collection

Repository

Knowledge Package

Entire Graph
```

---

# Validation Profile

Permite seleccionar conjuntos de restricciones.

Ejemplos:

```text
Basic

Standard

Strict

Publication

Experimental
```

---

# Validation Context

Toda validación se ejecutará dentro de un contexto.

Podrá incluir:

- versión de ontología;
- versión del SGCC;
- idioma;
- perfil;
- usuario;
- entorno.

---

# Validation Session

Cada ejecución generará una sesión.

Formato recomendado:

```text
VAL-SESSION-XXXXXX
```

---

# Contrato conceptual

```yaml
session:

  id:

  started_at:

  profile:

  target:

  ontology_version:

  validator_version:
```

---

# Tipos de validación

El Validation Engine soportará múltiples tipos de validación.

---

## Validación estructural

Comprueba la estructura.

---

## Validación documental

Comprueba documentos.

---

## Validación sintáctica

Comprueba formatos.

---

## Validación semántica

Comprueba significado.

---

## Validación ontológica

Comprueba compatibilidad con la ontología.

---

## Validación de relaciones

Comprueba relaciones.

---

## Validación de componentes

Comprueba componentes reutilizables.

---

## Validación de colecciones

Comprueba la coherencia de las colecciones.

---

## Validación del Knowledge Graph

Comprueba el estado global del grafo.

---

## Validación incremental

Solo evalúa los cambios.

---

## Validación completa

Reevalúa todos los elementos.

---

# Perfiles de validación

Los perfiles permiten ejecutar diferentes niveles de exigencia.

---

## Basic

Validaciones mínimas.

---

## Standard

Perfil recomendado.

---

## Strict

Ejecuta todas las restricciones.

---

## Publication

Requerido antes de publicar.

---

## Migration

Utilizado durante migraciones.

---

## Experimental

Incluye reglas aún no oficiales.

---

# Niveles

Las validaciones podrán organizarse por niveles.

```text
Nivel 1

Sintaxis

↓

Nivel 2

Estructura

↓

Nivel 3

Semántica

↓

Nivel 4

Ontología

↓

Nivel 5

Gobernanza

↓

Nivel 6

Publicación
```

Cada nivel podrá depender de los anteriores.

---

# Dependencias

Una validación podrá requerir resultados previos.

Ejemplo:

```text
Semántica

↓

requiere

↓

Estructura válida
```

---

# Jerarquía de validadores

Los validadores podrán organizarse jerárquicamente.

Ejemplo:

```text
Structural

Semantic

Ontology

Collections

Knowledge Graph
```

---

# Alcance futuro

La arquitectura deberá permitir incorporar nuevos tipos de validación sin modificar el núcleo del motor.

---

# Transición hacia la Parte II

Esta primera parte ha definido:

- la misión del Validation Engine;
- su posición dentro del Knowledge Engine;
- sus principios fundamentales;
- la diferencia entre validación y razonamiento;
- el ciclo general;
- la arquitectura lógica;
- los componentes internos;
- los perfiles de validación;
- los niveles de validación.

La Parte II desarrollará el núcleo formal del sistema de validación mediante la definición de:

- restricciones (Constraints);
- reglas;
- validadores;
- diagnósticos;
- evidencias;
- severidades;
- excepciones;
- contratos YAML;
- ciclo de vida de las reglas.

---

# Conclusión

El Validation Engine constituye el garante de la calidad del conocimiento dentro de NovaCoquinaria.

Su función trasciende la mera comprobación de documentos: actúa como un sistema de aseguramiento de conformidad que verifica que cualquier artefacto del SGCC respeta la arquitectura, la ontología y las políticas de gobernanza establecidas.

Gracias a su diseño modular, determinista y explicable, el motor permitirá que el conocimiento publicado en el Knowledge Graph mantenga un elevado nivel de consistencia y fiabilidad, proporcionando una base sólida para el Reasoning Engine, GraphRAG y los futuros agentes inteligentes.

---

# Parte II — Modelo formal de restricciones, validadores y diagnósticos

---

# Introducción

La Parte I ha definido:

- la misión del Validation Engine;
- su arquitectura;
- sus principios;
- los distintos tipos de validación;
- el flujo general del proceso.

Esta segunda parte define el núcleo conceptual del sistema de validación: el modelo formal mediante el cual NovaCoquinaria expresa las reglas que deben cumplir los distintos artefactos del SGCC.

El objetivo no consiste únicamente en comprobar si un documento es correcto, sino en disponer de un lenguaje uniforme para expresar cualquier tipo de restricción sobre el conocimiento.

---

# Objetivos

Esta parte persigue:

- definir el concepto de restricción;
- definir el modelo de regla;
- definir los validadores;
- definir los diagnósticos;
- definir la evidencia;
- definir la severidad;
- definir las excepciones;
- definir la supresión temporal;
- establecer contratos formales;
- preparar la ejecución del pipeline de validación.

---

# Modelo conceptual

Todo el sistema gira alrededor del siguiente modelo:

```text
Target
      │
      ▼
Constraint
      │
      ▼
Validator
      │
      ▼
Validation Result
      │
      ▼
Diagnostics
```

---

# Restricción (Constraint)

Una **Constraint** representa una condición que debe cumplirse.

Formalmente:

```text
Constraint =
Condition
+
Target
+
Severity
+
Policy
```

Una restricción nunca ejecuta lógica.

Simplemente declara una condición.

---

# Ejemplos

```text
Toda receta debe tener un título.

Todo ingrediente debe tener un ID.

Una técnica no puede contener ingredientes.

Una relación contains debe unir Recipe → Ingredient.
```

---

# Propiedades

Toda Constraint deberá poseer:

- identidad;
- nombre;
- descripción;
- versión;
- estado;
- ámbito;
- severidad;
- política;
- documentación.

---

# Identificador

Formato recomendado:

```text
CONSTRAINT-XXXXXX
```

Ejemplo:

```text
CONSTRAINT-000421
```

---

# Contrato mínimo

```yaml
constraint:

  id: CONSTRAINT-000421

  name: Recipe must contain ingredients

  status: active
```

---

# Contrato ampliado

```yaml
constraint:

  id: CONSTRAINT-000421

  name:
    es: Toda receta debe contener ingredientes

  version: 1.0.0

  status: active

  category: semantic

  severity: error

  target:
    type: Recipe

  documentation:
    specification:
      - ESPECIFICACION_DE_ONTOLOGIAS.md

  owner: Knowledge Team
```

---

# Ciclo de vida

Toda restricción deberá poseer un estado.

Valores recomendados:

```text
draft

experimental

active

deprecated

retired
```

---

# Draft

La restricción existe pero aún no participa en validaciones oficiales.

---

# Experimental

Puede ejecutarse en perfiles experimentales.

---

# Active

Forma parte del conjunto oficial.

---

# Deprecated

Debe sustituirse progresivamente.

---

# Retired

Ya no debe utilizarse.

---

# Versionado

Toda modificación incompatible deberá incrementar la versión.

---

# Compatibilidad

Cambios menores podrán conservar compatibilidad.

---

# Categorías

Las restricciones podrán clasificarse.

Ejemplos:

```text
Structural

Syntax

Metadata

Identity

Semantic

Ontology

Collections

Governance

Security

Publication
```

---

# Scope

Toda restricción deberá indicar dónde puede aplicarse.

Ejemplos:

```text
Document

Component

Entity

Statement

Collection

Knowledge Package

Knowledge Graph
```

---

# Nivel

También podrá declararse el nivel.

```text
Local

Repository

Global
```

---

# Restricción local

Solo evalúa el elemento.

---

# Restricción global

Necesita observar múltiples elementos.

---

# Restricción incremental

Puede reevaluarse únicamente sobre cambios.

---

# Restricción completa

Siempre requiere una evaluación global.

---

# Rule

Una Rule representa la formulación lógica de una Constraint.

Mientras la Constraint define:

```text
Qué debe cumplirse
```

la Rule define:

```text
Cómo comprobarlo
```

---

# Ejemplo

Constraint:

```text
Una receta debe contener ingredientes.
```

Rule:

```text
count(Ingredient) > 0
```

---

# Modelo

```text
Constraint

↓

Rule

↓

Validator
```

---

# Identificador

Formato:

```text
RULE-XXXXXX
```

---

# Contrato

```yaml
rule:

  id: RULE-000021

  constraint: CONSTRAINT-000421

  language: sgcc-rule

  expression:

    ingredient_count > 0
```

---

# Lenguaje

Las reglas podrán expresarse mediante:

- lenguaje declarativo;
- DSL SGCC;
- SHACL;
- SPARQL;
- motor de reglas;
- implementación Java;
- implementación Python.

La arquitectura no dependerá de ninguno.

---

# Validator

El Validator ejecuta una Rule.

---

# Diferencia

Constraint:

declara.

Rule:

expresa.

Validator:

ejecuta.

---

# Modelo

```text
Constraint

↓

Rule

↓

Validator

↓

Diagnostics
```

---

# Identificador

Formato:

```text
VALIDATOR-XXXXXX
```

---

# Contrato

```yaml
validator:

  id: VALIDATOR-000081

  name:

    es: Recipe Ingredient Validator

  version: 2.0.0

  supports:

    - Recipe
```

---

# Responsabilidades

El Validator deberá:

- recibir un Target;
- evaluar reglas;
- generar diagnósticos;
- aportar evidencia;
- no modificar el conocimiento.

---

# No responsabilidades

No deberá:

- crear entidades;
- corregir errores;
- publicar cambios;
- ejecutar inferencias.

---

# Tipos

Ejemplos:

```text
Structural Validator

Metadata Validator

Semantic Validator

Ontology Validator

Collection Validator

Security Validator
```

---

# Reutilización

Un Validator podrá implementar varias reglas.

---

# Rule Set

Las reglas podrán agruparse.

Formato:

```text
RULESET-XXXXXX
```

---

# Ejemplo

```text
Recipe Rules

Ingredient Rules

Ontology Rules

Publication Rules
```

---

# Contrato

```yaml
ruleset:

  id: RULESET-000041

  constraints:

    - CONSTRAINT-000421
    - CONSTRAINT-000422
    - CONSTRAINT-000423
```

---

# Validation Target

Toda validación opera sobre un Target.

---

# Tipos

```text
Document

Entity

Statement

Collection

Ontology

Knowledge Package

Knowledge Graph
```

---

# Identificador

Todo Target deberá poseer identidad estable.

---

# Resultado

El resultado nunca será simplemente:

```text
true

false
```

Deberá contener información completa.

---

# Validation Result

Formato recomendado:

```text
VALIDATION-RESULT
```

---

# Contrato

```yaml
result:

  validator:

  target:

  status:

  diagnostics:

  execution_time:
```

---

# Estados

```text
Passed

PassedWithWarnings

Failed

Skipped

NotApplicable
```

---

# Passed

Todas las reglas se cumplen.

---

# PassedWithWarnings

La validación es correcta pero existen advertencias.

---

# Failed

Existen errores.

---

# Skipped

El Validator no se ejecutó.

---

# NotApplicable

No aplica al Target.

---

# Diagnostic

Todo problema detectado genera un Diagnostic.

---

# Identificador

Formato:

```text
DIAG-XXXXXX
```

---

# Contrato mínimo

```yaml
diagnostic:

  id: DIAG-000081

  severity: error

  code:

  message:
```

---

# Contrato ampliado

```yaml
diagnostic:

  id: DIAG-000081

  validator: VALIDATOR-000081

  constraint: CONSTRAINT-000421

  target:

    id: REC-0008

  severity: error

  code:

    RECIPE_WITHOUT_INGREDIENTS

  message:

    es: La receta no contiene ingredientes.

  evidence:

  remediation:
```

---

# Código

Todo diagnóstico deberá poseer un código estable.

---

# Ejemplo

```text
INVALID_FRONT_MATTER

UNKNOWN_RELATION

INVALID_CARDINALITY

MISSING_COMPONENT

INVALID_COLLECTION
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

# Info

Información adicional.

---

# Warning

No bloquea la publicación.

---

# Error

Bloquea según política.

---

# Critical

Siempre bloquea.

---

# Categorías

Los diagnósticos podrán clasificarse.

Ejemplos:

```text
Structure

Syntax

Identity

Semantics

Ontology

Governance

Security
```

---

# Evidence

Todo diagnóstico deberá aportar evidencia.

---

# Ejemplos

- línea;
- bloque;
- componente;
- entidad;
- relación;
- consulta;
- valor encontrado.

---

# Contrato

```yaml
evidence:

  source:

  location:

  actual:

  expected:
```

---

# Actual

Valor encontrado.

---

# Expected

Valor esperado.

---

# Remediation

Todo diagnóstico podrá incluir una propuesta de resolución.

---

# Ejemplo

```text
Añadir al menos un ingrediente.
```

---

# Auto Fix

Algunos diagnósticos podrán indicar:

```text
auto_fix_available
```

El Validation Engine nunca aplicará automáticamente la corrección.

---

# Confidence

Los diagnósticos generados mediante IA podrán indicar confianza.

---

# Suppression

En ocasiones será necesario ignorar temporalmente una regla.

---

# Suppression ID

Formato:

```text
SUPPRESSION-XXXXXX
```

---

# Contrato

```yaml
suppression:

  constraint:

  target:

  reason:

  expires:
```

---

# Requisitos

Toda supresión deberá:

- tener responsable;
- justificar motivo;
- tener fecha de expiración.

---

# Waiver

Un Waiver representa una excepción aprobada.

---

# Diferencia

Suppression:

temporal.

Waiver:

aceptado oficialmente.

---

# Contrato

```yaml
waiver:

  id:

  constraint:

  approved_by:

  justification:
```

---

# Excepciones

Las excepciones deberán ser explícitas.

Nunca implícitas.

---

# Diagnostics Set

Los diagnósticos podrán agruparse.

Formato:

```text
DIAGNOSTIC-SET
```

---

# Validation Report

El informe final reúne:

- resultados;
- diagnósticos;
- evidencias;
- métricas;
- tiempos.

---

# Contrato

```yaml
validation_report:

  session:

  target:

  validators:

  diagnostics:

  metrics:
```

---

# Métricas

Ejemplos:

- reglas ejecutadas;
- reglas superadas;
- advertencias;
- errores;
- duración.

---

# Auditoría

Toda ejecución deberá conservar:

- reglas;
- versión;
- validadores;
- configuración.

---

# Registro

Nada deberá depender únicamente del log.

---

# Dependencias

Las reglas podrán depender de otras.

---

# Ejemplo

```text
Ontology Validation

↓

requiere

↓

Identity Validation
```

---

# Priorización

Las reglas críticas deberán ejecutarse antes.

---

# Compatibilidad

Una nueva regla no deberá romper validaciones anteriores salvo cambio mayor de versión.

---

# Registry

Todos los elementos deberán registrarse.

Ejemplos:

```text
Constraint Registry

Validator Registry

Ruleset Registry
```

---

# Arquitectura

```text
Constraint
        │
        ▼
Rule
        │
        ▼
Validator
        │
        ▼
Validation Result
        │
        ▼
Diagnostics
        │
        ▼
Validation Report
```

---

# Transición hacia la Parte III

Esta segunda parte ha definido:

- el modelo de restricciones;
- el concepto de Rule;
- los Validators;
- los RuleSets;
- los Validation Targets;
- los Validation Results;
- los Diagnostics;
- las severidades;
- las evidencias;
- las supresiones;
- los Waivers;
- los contratos YAML.

La Parte III desarrollará cómo se ejecuta realmente el pipeline de validación:

- planificación;
- selección de reglas;
- ejecución incremental;
- paralelismo;
- dependencias;
- cachés;
- reintentos;
- resultados parciales;
- consolidación del Validation Report.

---

# Conclusión

El modelo formal de restricciones constituye el núcleo del Validation Engine.

La separación entre **Constraint**, **Rule**, **Validator** y **Diagnostic** permite construir un sistema altamente modular, extensible y gobernado, en el que las reglas pueden evolucionar independientemente del motor que las ejecuta y donde cada decisión de validación queda plenamente documentada, trazable y explicable.

Esta arquitectura proporciona una base sólida para soportar desde simples validaciones documentales hasta complejos procesos de verificación semántica y ontológica a escala del Knowledge Graph.

---

# Parte III — Pipeline de validación y modelo de ejecución

---

# Introducción

Las partes anteriores han definido:

- la misión del Validation Engine;
- su posición dentro del Knowledge Engine;
- los tipos de validación;
- los perfiles y niveles de exigencia;
- el modelo formal de restricciones;
- las reglas;
- los validadores;
- los diagnósticos;
- las evidencias;
- las supresiones;
- los waivers;
- los informes de validación.

Esta tercera parte define cómo se ejecutan realmente estos elementos dentro del motor.

El objetivo consiste en establecer un pipeline de validación que sea:

- determinista;
- reproducible;
- incremental;
- observable;
- escalable;
- explicable;
- seguro;
- independiente de la tecnología concreta.

La ejecución no deberá limitarse a recorrer una lista de validadores.

El motor deberá ser capaz de:

- resolver el objetivo;
- fijar una versión consistente;
- seleccionar restricciones;
- ordenar dependencias;
- planificar validadores;
- gestionar ejecución paralela;
- consolidar resultados;
- detectar fallos del propio proceso;
- aplicar políticas;
- producir un informe final auditable.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir el ciclo completo de una validación;
- formalizar la solicitud de validación;
- establecer el contexto de ejecución;
- fijar snapshots y versiones;
- resolver targets;
- seleccionar constraints, rulesets y validators;
- construir el plan de ejecución;
- gestionar dependencias;
- ejecutar validadores por fases;
- soportar validación local, global e incremental;
- definir paralelismo y concurrencia;
- establecer cachés y reutilización de resultados;
- gestionar timeouts, cancelaciones y reintentos;
- consolidar diagnósticos;
- resolver duplicados y dependencias entre resultados;
- construir el Validation Report;
- definir estados de ejecución;
- establecer observabilidad y métricas;
- preparar la integración con Quality Gates.

---

# Principios de ejecución

Toda ejecución deberá respetar los siguientes principios.

---

## Snapshot consistente

Una sesión de validación deberá trabajar sobre una visión coherente de:

- artefactos;
- documentos;
- Knowledge Packages;
- ontología;
- constraints;
- rulesets;
- validators;
- configuración.

No deberán mezclarse versiones incompatibles dentro de una misma sesión.

---

## Planificación explícita

Antes de ejecutar validadores deberá existir un plan identificable.

---

## Orden por dependencias

Los validadores deberán ejecutarse conforme a sus dependencias lógicas.

---

## Cortocircuito controlado

Un error crítico podrá impedir fases posteriores cuando estas no puedan producir resultados fiables.

---

## Ejecución parcial visible

Cuando una sesión no pueda completar todo el plan, el resultado deberá indicar:

- qué se ejecutó;
- qué se omitió;
- qué falló;
- qué quedó pendiente.

---

## Incrementalidad

Siempre que sea posible, solo deberán reevaluarse los elementos afectados por un cambio.

---

## No modificación

El pipeline de validación no deberá modificar directamente el target.

---

## Reproducibilidad

Las mismas entradas y versiones deberán producir el mismo resultado, salvo validadores explícitamente probabilísticos.

---

## Idempotencia

La repetición de una misma validación no deberá generar estados ni diagnósticos duplicados persistentes.

---

## Aislamiento

Las sesiones concurrentes no deberán interferir entre sí.

---

## Explicabilidad operacional

El motor deberá poder explicar:

- por qué seleccionó un validador;
- por qué omitió otro;
- qué dependencia bloqueó una fase;
- qué política determinó el resultado.

---

# Arquitectura de ejecución

La arquitectura operacional podrá representarse así:

```text
Validation Request
        │
        ▼
Request Validator
        │
        ▼
Execution Context Builder
        │
        ▼
Snapshot Resolver
        │
        ▼
Target Resolver
        │
        ▼
Constraint Selector
        │
        ▼
Validator Planner
        │
        ▼
Dependency Resolver
        │
        ▼
Validation Runtime
        │
        ├── Structural Validators
        ├── Semantic Validators
        ├── Ontology Validators
        ├── Governance Validators
        └── Security Validators
        │
        ▼
Diagnostic Consolidator
        │
        ▼
Result Aggregator
        │
        ▼
Quality Gate Evaluator
        │
        ▼
Validation Report Builder
```

---

# Ciclo general de ejecución

Toda validación seguirá, conceptualmente, las siguientes etapas:

```text
Solicitud
   ↓
Validación de solicitud
   ↓
Construcción de contexto
   ↓
Resolución de snapshot
   ↓
Resolución de target
   ↓
Selección de perfil
   ↓
Selección de constraints
   ↓
Selección de validators
   ↓
Planificación
   ↓
Ejecución
   ↓
Consolidación
   ↓
Evaluación de Quality Gates
   ↓
Construcción del informe
   ↓
Auditoría
```

---

# Validation Request

Toda ejecución deberá comenzar mediante una solicitud estructurada.

Formato recomendado:

```text
VAL-REQ-XXXXXX
```

---

# Contrato mínimo

```yaml
validation_request:
  id: VAL-REQ-000041

  target:
    type: document
    id: REC-0009

  profile: standard
```

---

# Contrato ampliado

```yaml
validation_request:
  id: VAL-REQ-000041

  target:
    type: document
    id: REC-0009
    version: 1.2.0

  scope:
    mode: local
    include_dependencies: true
    include_dependents: false

  profile:
    id: VAL-PROFILE-STANDARD
    version: 1.0.0

  rulesets:
    include:
      - RULESET-DOCUMENTS
      - RULESET-RECIPES

    exclude:
      - RULESET-EXPERIMENTAL

  execution:
    mode: synchronous
    strategy: incremental
    fail_fast: false

  output:
    include_evidence: true
    include_remediation: true
    include_passed_checks: false

  requested_by:
    type: user
    id: USER-0001
```

---

# Validación de la solicitud

Antes de construir el plan deberán comprobarse:

- identidad de la solicitud;
- existencia del target;
- compatibilidad del perfil;
- autorización;
- formato;
- reglas incluidas;
- reglas excluidas;
- límites;
- versión solicitada.

---

# Solicitud inválida

Una solicitud inválida deberá rechazarse antes de iniciar la sesión.

Ejemplos:

```text
UNKNOWN_TARGET
UNKNOWN_PROFILE
INCOMPATIBLE_RULESET
UNAUTHORIZED_SCOPE
INVALID_EXECUTION_MODE
```

---

# Execution Context

El `Execution Context` reúne toda la información necesaria para ejecutar la sesión.

---

# Contenido

Podrá incluir:

- target;
- scope;
- perfil;
- snapshot;
- versiones;
- entorno;
- usuario;
- permisos;
- idioma;
- configuración;
- límites;
- estrategia;
- fecha.

---

# Contrato

```yaml
execution_context:
  request: VAL-REQ-000041

  environment: development

  snapshot:
    repository: GIT-6fa8c42
    ontology: ONT-2.0.0
    constraints: CS-1.4.0
    validators: VR-1.3.0

  user:
    id: USER-0001
    permissions:
      - validation_execute
      - validation_read_diagnostics

  locale:
    language: es
    timezone: Europe/Madrid

  limits:
    timeout_ms: 30000
    max_diagnostics: 5000
    max_parallel_validators: 4
```

---

# Inmutabilidad del contexto

El contexto deberá permanecer inmutable durante la sesión.

Si cambia cualquiera de sus versiones, deberá iniciarse una sesión nueva.

---

# Snapshot Resolver

El `Snapshot Resolver` fija el estado sobre el que se ejecutará la validación.

---

# Elementos del snapshot

Podrá incluir:

```text
Document Snapshot

Knowledge Package Snapshot

Knowledge Graph Snapshot

Ontology Version

Constraint Registry Version

Validator Registry Version

Policy Version
```

---

# Snapshot explícito

La solicitud indica versiones concretas.

---

# Snapshot implícito

El motor resuelve la versión actual compatible.

La resolución deberá quedar registrada.

---

# Compatibilidad de snapshot

Antes de ejecutar deberá comprobarse que:

- la ontología es compatible con los constraints;
- los validators soportan las reglas seleccionadas;
- el esquema del target es compatible;
- el perfil puede ejecutarse sobre ese snapshot.

---

# Mezcla de versiones

Una sesión no deberá utilizar silenciosamente:

```text
Ontology 2.0
+
Constraints 1.0
+
Validators 3.0
```

si no existe una matriz de compatibilidad válida.

---

# Target Resolver

El `Target Resolver` localiza y prepara el objetivo.

---

# Tipos de target

Podrán validarse:

- archivo;
- documento;
- componente;
- entidad;
- relación;
- afirmación;
- colección;
- Knowledge Package;
- subgrafo;
- ontología;
- repositorio;
- Knowledge Graph completo.

---

# Target directo

La solicitud identifica exactamente un elemento.

---

# Target compuesto

La solicitud identifica un conjunto.

Ejemplo:

```text
Todos los documentos de tipo Recipe
```

---

# Target derivado

El target se obtiene mediante consulta.

Ejemplo:

```text
Documentos modificados desde el último commit
```

---

# Target dinámico

Depende del estado actual.

Ejemplo:

```text
Todas las entidades sin fuente primaria
```

Deberá materializarse al iniciar la sesión para garantizar reproducibilidad.

---

# Target Set

Formato recomendado:

```text
VAL-TARGET-SET-XXXXXX
```

---

# Contrato

```yaml
target_set:
  id: VAL-TARGET-SET-000041

  source:
    type: git_changeset
    id: CHANGESET-000081

  targets:
    - type: document
      id: REC-0009

    - type: ingredient
      id: ING-0008

  resolved_at: 2026-08-01T19:00:00+02:00
```

---

# Scope Resolver

El alcance determina cuánto conocimiento adicional deberá cargarse.

---

# Scope local

Evalúa únicamente el target.

Adecuado para:

- sintaxis;
- Front Matter;
- estructura;
- campos obligatorios.

---

# Scope vecinal

Incluye:

- relaciones directas;
- referencias;
- dependencias inmediatas.

---

# Scope transitive

Incluye dependencias transitivas hasta un límite.

---

# Scope collection

Incluye una colección completa.

---

# Scope repository

Incluye el repositorio documental.

---

# Scope global

Incluye el Knowledge Graph o ecosistema completo.

---

# Dependencias de validación

Algunas restricciones necesitan contexto adicional.

Ejemplo:

```text
Validar un enlace interno
```

requiere:

```text
índice de documentos y rutas
```

---

# Scope mínimo suficiente

El motor deberá recuperar únicamente el contexto necesario.

No deberá cargar todo el grafo para una validación local si no resulta necesario.

---

# Perfil de validación

El perfil determina:

- constraints activos;
- severidades;
- políticas;
- tolerancias;
- gates;
- estrategia.

---

# Perfiles iniciales

```text
basic
standard
strict
publication
migration
experimental
security
audit
```

---

# Perfil `basic`

Incluye:

- sintaxis;
- IDs;
- campos obligatorios;
- referencias básicas.

---

# Perfil `standard`

Añade:

- semántica;
- tipos;
- relaciones;
- consistencia documental;
- procedencia.

---

# Perfil `strict`

Añade:

- ontología;
- restricciones globales;
- seguridad;
- tolerancia cero en errores.

---

# Perfil `publication`

Incluye todas las validaciones necesarias para publicar.

---

# Perfil `migration`

Adapta restricciones a estados transitorios.

---

# Perfil `experimental`

Incluye reglas no estables.

Los diagnósticos experimentales deberán marcarse.

---

# Perfil `security`

Prioriza:

- permisos;
- secretos;
- sensibilidad;
- privacidad;
- exposición.

---

# Perfil `audit`

Ejecuta validación exhaustiva con evidencia completa.

---

# Constraint Selector

El `Constraint Selector` determina qué restricciones son aplicables.

---

# Criterios de selección

Podrán incluir:

- tipo de target;
- perfil;
- estado;
- versión;
- entorno;
- módulo;
- categoría;
- contexto;
- permisos;
- reglas excluidas.

---

# Constraint aplicable

Una constraint será aplicable cuando:

- soporte el tipo de target;
- esté activa;
- sea compatible con el perfil;
- sea compatible con el snapshot;
- no esté excluida;
- no exista una supresión válida;
- se cumplan sus precondiciones.

---

# Constraint no aplicable

No deberá ejecutarse.

El resultado podrá registrarse como:

```text
not_applicable
```

cuando resulte útil para auditoría.

---

# Constraint omitida

Una constraint aplicable puede no ejecutarse por:

- dependencia fallida;
- timeout;
- cancelación;
- configuración;
- presupuesto;
- falta de recursos.

Deberá marcarse como:

```text
skipped
```

no como:

```text
passed
```

---

# Validator Selector

Una constraint puede disponer de una o varias implementaciones.

El `Validator Selector` elegirá la adecuada.

---

# Criterios

- lenguaje;
- runtime;
- versión;
- capacidad;
- rendimiento;
- perfil;
- entorno;
- disponibilidad;
- seguridad.

---

# Implementación preferida

Una constraint podrá indicar:

```yaml
implementations:
  preferred: VALIDATOR-SHACL-0001
  fallback:
    - VALIDATOR-PYTHON-0004
```

---

# Fallback

Solo podrá utilizarse si:

- produce semántica equivalente;
- está autorizado;
- queda registrado.

---

# Validator no disponible

El motor deberá decidir entre:

- fallar;
- omitir;
- degradar;
- usar fallback;
- solicitar ejecución asíncrona.

---

# Validator Planner

El `Validator Planner` construye el plan de ejecución.

Formato recomendado:

```text
VAL-PLAN-XXXXXX
```

---

# Objetivos del plan

El plan deberá indicar:

- constraints seleccionadas;
- validators seleccionados;
- dependencias;
- fases;
- orden;
- paralelismo;
- límites;
- puntos de cortocircuito;
- condiciones de finalización.

---

# Contrato

```yaml
validation_plan:
  id: VAL-PLAN-000041

  request: VAL-REQ-000041
  target_set: VAL-TARGET-SET-000041

  phases:
    - id: PHASE-STRUCTURE
      validators:
        - VALIDATOR-FRONT-MATTER
        - VALIDATOR-IDS

    - id: PHASE-REFERENCES
      depends_on:
        - PHASE-STRUCTURE

      validators:
        - VALIDATOR-INTERNAL-LINKS

    - id: PHASE-SEMANTIC
      depends_on:
        - PHASE-STRUCTURE
        - PHASE-REFERENCES

      validators:
        - VALIDATOR-RELATIONS
        - VALIDATOR-ONTOLOGY

  strategy:
    fail_fast: false
    parallelism: 4

  plan_hash: sha256:...
```

---

# Plan determinista

La misma solicitud y snapshot deberán producir el mismo plan, salvo estrategias explícitamente adaptativas.

---

# Plan dinámico

Podrá ajustarse durante la ejecución cuando:

- una fase descubra nuevos targets;
- una dependencia resulte no aplicable;
- se active un fallback;
- un error impida continuar.

Toda modificación deberá registrarse.

---

# Dependency Resolver

El `Dependency Resolver` construye el grafo de dependencias entre validadores.

---

# Tipos de dependencia

---

## Dependencia de orden

Un validator debe ejecutarse después de otro.

---

## Dependencia de resultado

Necesita el resultado de otro validator.

---

## Dependencia de artefacto

Necesita un índice, grafo, esquema o recurso generado previamente.

---

## Dependencia opcional

Mejora la validación, pero no la bloquea.

---

## Dependencia fuerte

Sin ella el validator no puede ejecutarse.

---

# Grafo acíclico

Las dependencias de ejecución deberán formar un DAG.

```text
Validator A
    ↓
Validator B
    ↓
Validator C
```

---

# Ciclos

Un ciclo deberá bloquear la planificación.

Diagnóstico recomendado:

```text
VALIDATOR_DEPENDENCY_CYCLE
```

---

# Precondiciones

Un validator podrá declarar precondiciones.

Ejemplo:

```yaml
preconditions:
  - validator: VALIDATOR-FRONT-MATTER
    expected_status:
      - passed
      - passed_with_warnings
```

---

# Validator bloqueado

Cuando una precondición falle, deberá registrarse:

```text
blocked_by_dependency
```

---

# Fases de validación

El pipeline podrá organizarse en fases.

Orden recomendado:

```text
1. Request Validation

2. Syntax Validation

3. Structural Validation

4. Identity Validation

5. Reference Validation

6. Semantic Validation

7. Ontology Validation

8. Context and Temporal Validation

9. Governance Validation

10. Security Validation

11. Global Consistency Validation

12. Quality Gate Evaluation
```

---

# Fase sintáctica

Comprueba que el artefacto pueda interpretarse.

Ejemplos:

- YAML válido;
- JSON válido;
- Markdown parseable;
- esquema legible.

Si falla de forma crítica, las fases posteriores podrán bloquearse.

---

# Fase estructural

Comprueba:

- campos;
- tipos;
- bloques;
- Front Matter;
- estructura mínima.

---

# Fase de identidad

Comprueba:

- IDs;
- unicidad;
- formato;
- colisiones;
- referencias de identidad.

---

# Fase de referencias

Comprueba:

- enlaces internos;
- referencias cruzadas;
- recursos;
- targets.

---

# Fase semántica

Comprueba:

- tipos conceptuales;
- relaciones;
- coherencia de valores;
- reglas de dominio.

---

# Fase ontológica

Comprueba:

- clases;
- propiedades;
- dominio;
- rango;
- cardinalidades;
- disjunciones;
- consistencia.

---

# Fase contextual y temporal

Comprueba:

- ámbito;
- vigencia;
- intervalos;
- variantes;
- versiones.

---

# Fase de gobernanza

Comprueba:

- propietario;
- estado;
- versionado;
- procedencia;
- revisión;
- licencia.

---

# Fase de seguridad

Comprueba:

- secretos;
- sensibilidad;
- permisos;
- exposición;
- contenido prohibido;
- segregación.

---

# Fase global

Comprueba invariantes que afectan a varios elementos.

Ejemplos:

- IDs únicos;
- ausencia de ciclos;
- compatibilidad entre módulos;
- integridad del grafo.

---

# Validation Runtime

El `Validation Runtime` coordina la ejecución efectiva del plan.

---

# Responsabilidades

Deberá:

- preparar entradas;
- invocar validators;
- aplicar límites;
- registrar estados;
- gestionar dependencias;
- capturar errores;
- controlar paralelismo;
- producir resultados;
- mantener trazabilidad.

---

# Estado de sesión

Valores recomendados:

```text
created
planning
ready
running
paused
cancelling
cancelled
completed
completed_with_warnings
partial
failed
blocked
```

---

# Sesión creada

La solicitud ha sido aceptada.

---

# Sesión en planificación

Se está construyendo el plan.

---

# Sesión preparada

El plan está validado.

---

# Sesión en ejecución

Existen validators activos o pendientes.

---

# Sesión parcial

No se ejecutó el plan completo.

---

# Sesión bloqueada

Una dependencia o política impide continuar.

---

# Estado de validator execution

Cada ejecución individual podrá encontrarse en:

```text
pending
ready
running
passed
passed_with_warnings
failed
skipped
blocked
cancelled
timed_out
errored
not_applicable
```

---

# Diferencia entre `failed` y `errored`

```text
failed
```

significa que el target incumple la constraint.

```text
errored
```

significa que el validator no pudo completar su trabajo.

---

# Error del target

Produce diagnóstico de validación.

---

# Error del validator

Produce diagnóstico operacional.

No deberá interpretarse como incumplimiento del target.

---

# Resultado individual

Formato recomendado:

```yaml
validator_execution:
  id: VAL-EXEC-000145

  validator:
    id: VALIDATOR-IDS
    version: 1.2.0

  target:
    type: repository
    id: REPO-NOVACOQUINARIA

  status: failed

  diagnostics:
    - DIAG-000081

  timing:
    started_at: 2026-08-01T19:10:00+02:00
    duration_ms: 18
```

---

# Ejecución secuencial

Adecuada cuando:

- existen dependencias;
- el target es pequeño;
- se prioriza simplicidad;
- el validator no es thread-safe.

---

# Ejecución paralela

Adecuada para validators independientes.

---

# Paralelismo por validator

Varios validators sobre el mismo target.

---

# Paralelismo por target

Un validator sobre múltiples targets.

---

# Paralelismo por partición

Se divide un conjunto grande.

Ejemplo:

```text
10.000 documentos
↓
20 particiones
↓
20 workers
```

---

# Límites de paralelismo

Deberán configurarse por:

- sesión;
- validator;
- tipo de target;
- recurso;
- entorno.

---

# Thread safety

Todo validator deberá declarar si soporta ejecución concurrente.

---

# Orden de resultados

El orden de finalización no deberá alterar el informe final.

---

# Validación local

Evalúa un único target o subgrafo reducido.

Ventajas:

- baja latencia;
- feedback rápido;
- incrementalidad;
- menor coste.

---

# Validación global

Evalúa invariantes transversales.

Ventajas:

- detecta colisiones;
- ciclos;
- inconsistencias globales;
- deuda sistémica.

---

# Estrategia combinada

Recomendación:

```text
Validación local
ante cada cambio

+

Validación global
antes de merge o release
```

---

# Validación completa

Reevalúa todo el ámbito.

Adecuada para:

- releases;
- migraciones;
- cambios ontológicos;
- auditorías;
- reconstrucción.

---

# Validación incremental

Evalúa únicamente cambios y elementos afectados.

---

# Change Set

La validación incremental deberá partir de un Change Set.

```yaml
changeset:
  id: CHANGESET-000041

  created:
    - DOC-0141

  updated:
    - REC-0009

  deleted:
    - DOC-0081

  renamed:
    - from: docs/old.md
      to: docs/new.md
```

---

# Impact Analyzer

El `Impact Analyzer` determina qué targets deben reevaluarse.

---

# Impacto directo

El elemento modificado.

---

# Impacto vecinal

Elementos directamente relacionados.

---

# Impacto transitivo

Dependencias y consumidores.

---

# Impacto ontológico

Clases, propiedades o shapes afectados.

---

# Impacto documental

Enlaces, referencias y colecciones dependientes.

---

# Ejemplo

Cambio:

```text
ING-0008 modifica su ID
```

Targets afectados:

- documento del ingrediente;
- recetas que lo referencian;
- relaciones;
- colecciones;
- índices;
- validación global de unicidad.

---

# Grafo de dependencias de validación

El sistema podrá mantener:

```text
Target
    │
    ├── referenced_by
    ├── validated_by
    ├── depends_on
    └── affects
```

---

# Reutilización de resultados

Un resultado previo podrá reutilizarse cuando no hayan cambiado:

- target;
- constraint;
- validator;
- snapshot;
- configuración;
- dependencias.

---

# Validation Cache

La caché podrá almacenar resultados individuales.

---

# Clave de caché

```text
target_hash
+
constraint_version
+
validator_version
+
context_hash
+
dependency_hash
```

---

# Resultado cacheado

Deberá indicar:

```yaml
cache:
  hit: true
  original_execution: VAL-EXEC-000101
```

---

# Invalidación de caché

Deberá producirse cuando cambie:

- target;
- dependencia;
- constraint;
- validator;
- ontología;
- política;
- perfil.

---

# Caché negativa

Podrá reutilizar resultados fallidos cuando el target no haya cambiado.

---

# Caché y seguridad

La clave deberá incluir el contexto de permisos cuando el resultado pueda depender del acceso.

---

# Ejecución síncrona

Adecuada para:

- validaciones locales;
- IDE;
- pre-commit;
- solicitudes pequeñas.

---

# Ejecución asíncrona

Adecuada para:

- repositorios;
- grafos completos;
- migraciones;
- auditorías;
- validaciones costosas.

---

# Contrato asíncrono

```yaml
validation_job:
  id: VAL-JOB-000041

  request: VAL-REQ-000041
  status: queued

  links:
    status: /validation/jobs/VAL-JOB-000041
    report: /validation/reports/VAL-REPORT-000041
```

---

# Cola de validación

Las sesiones asíncronas podrán utilizar una cola.

Prioridades recomendadas:

```text
critical
publication
interactive
standard
background
audit
```

---

# Backpressure

Cuando el sistema no pueda asumir más trabajo deberá:

- encolar;
- limitar;
- rechazar con información;
- degradar;
- reprogramar.

---

# Timeout

Podrán existir límites para:

- sesión;
- fase;
- validator;
- target;
- operación externa.

---

# Timeout de validator

No deberá marcar automáticamente el target como inválido.

Resultado:

```text
timed_out
```

---

# Reintentos

Solo deberán aplicarse a errores operacionales recuperables.

---

# Errores reintentables

Ejemplos:

- recurso temporalmente no disponible;
- timeout externo;
- servicio auxiliar caído;
- bloqueo transitorio.

---

# Errores no reintentables

Ejemplos:

- regla inválida;
- esquema incompatible;
- target corrupto;
- falta de permisos.

---

# Política de reintentos

```yaml
retry_policy:
  max_attempts: 3
  strategy: exponential_backoff
  retry_on:
    - TEMPORARY_DEPENDENCY_FAILURE
    - REMOTE_TIMEOUT
```

---

# Checkpoints

Las validaciones largas podrán crear checkpoints.

---

# Contenido de checkpoint

- fase completada;
- validators completados;
- diagnósticos;
- caché;
- targets pendientes;
- snapshot.

---

# Reanudación

Solo podrá realizarse si el snapshot sigue siendo válido.

---

# Cancelación

Una sesión deberá poder cancelarse.

---

# Cancelación cooperativa

Los validators deberán comprobar señales de cancelación.

---

# Resultado de cancelación

El informe deberá indicar:

- fase;
- validators completados;
- validators cancelados;
- diagnósticos obtenidos;
- ausencia de decisión final cuando proceda.

---

# Fail-fast

El modo `fail-fast` detiene la ejecución tras un error bloqueante.

---

# Cuándo utilizarlo

Adecuado para:

- validación sintáctica;
- feedback rápido;
- pre-commit;
- artefactos corruptos.

---

# Cuándo evitarlo

No resulta adecuado cuando se necesita un informe completo.

---

# Fail-safe

El motor continúa siempre que los resultados posteriores sigan siendo fiables.

---

# Matriz de continuación

Ejemplo:

| Resultado previo | Siguiente fase | Acción |
|---|---|---|
| Error sintáctico crítico | Semántica | Bloquear |
| Warning estructural | Semántica | Continuar |
| Error de enlace | Ontología | Continuar |
| Ontología no disponible | Ontología | Marcar `errored` |
| Conflicto de identidad | Publicación | Bloquear |

---

# Degradación controlada

Ante fallos no críticos, el motor podrá:

- omitir un validator opcional;
- utilizar fallback;
- producir informe parcial;
- marcar incertidumbre;
- solicitar ejecución posterior.

---

# Resultado parcial

Formato conceptual:

```yaml
validation_session:
  status: partial

  completed_validators: 18
  skipped_validators: 2
  errored_validators: 1

  completeness:
    value: 0.86
```

---

# Diagnostic Collector

Cada validator produce diagnósticos independientes.

El `Diagnostic Collector` los recopila.

---

# Diagnostic Consolidator

El `Diagnostic Consolidator` deberá:

- normalizar;
- deduplicar;
- agrupar;
- ordenar;
- enriquecer;
- vincular evidencias;
- aplicar supresiones y waivers.

---

# Deduplicación de diagnósticos

Dos diagnósticos podrán considerarse equivalentes cuando compartan:

- código;
- target;
- constraint;
- localización;
- evidencia relevante.

---

# Diagnósticos relacionados

Podrán agruparse bajo una causa común.

Ejemplo:

```text
Front Matter ausente
```

puede provocar:

- ID ausente;
- tipo ausente;
- versión ausente.

El informe podrá mostrar una causa raíz y diagnósticos derivados.

---

# Diagnóstico primario

Representa la causa principal.

---

# Diagnóstico secundario

Consecuencia de otro diagnóstico.

---

# Relación causal

```yaml
diagnostic:
  id: DIAG-000082
  caused_by:
    - DIAG-000081
```

---

# Aplicación de supresiones

Las supresiones deberán evaluarse después de generar el diagnóstico.

---

# Diagnóstico suprimido

No desaparecerá del sistema.

Se marcará:

```text
suppressed
```

---

# Waiver

Un waiver podrá convertir un diagnóstico bloqueante en aceptado para un ámbito concreto.

---

# Diagnóstico con waiver

Deberá conservar:

- constraint;
- target;
- aprobación;
- vigencia;
- justificación.

---

# Suppression Expiration

Una supresión expirada deberá dejar de aplicarse automáticamente.

---

# Result Aggregator

El `Result Aggregator` combina resultados individuales.

---

# Reglas de agregación

Ejemplo general:

```text
Critical
    ↓
Error
    ↓
Warning
    ↓
Info
```

El resultado global dependerá de:

- severidad;
- política;
- perfil;
- gates;
- estado de validators;
- completitud.

---

# Estados agregados

Valores recomendados:

```text
passed
passed_with_warnings
failed
blocked
partial
errored
cancelled
```

---

# `passed`

Todos los validators obligatorios han finalizado y no existen diagnósticos bloqueantes.

---

# `passed_with_warnings`

No existen errores bloqueantes, pero sí warnings.

---

# `failed`

El target incumple al menos una constraint bloqueante.

---

# `blocked`

No pudo completarse una fase necesaria.

---

# `partial`

La ejecución quedó incompleta, aunque existen resultados utilizables.

---

# `errored`

El motor o varios validators críticos fallaron operacionalmente.

---

# Precedencia de estados

Orden recomendado:

```text
errored
↓
blocked
↓
failed
↓
partial
↓
passed_with_warnings
↓
passed
```

La política podrá variar según el perfil.

---

# Quality Gate Evaluator

El `Quality Gate Evaluator` utiliza:

- diagnósticos;
- métricas;
- estado;
- completitud;
- perfil;
- política.

Su definición detallada se desarrollará en la Parte V.

---

# Validation Report Builder

El informe final deberá ser una representación completa y estable de la sesión.

Formato recomendado:

```text
VAL-REPORT-XXXXXX
```

---

# Contrato mínimo

```yaml
validation_report:
  id: VAL-REPORT-000041

  session: VAL-SESSION-000041
  target: REC-0009

  status: failed

  summary:
    errors: 2
    warnings: 1
```

---

# Contrato ampliado

```yaml
validation_report:
  id: VAL-REPORT-000041

  request: VAL-REQ-000041
  session: VAL-SESSION-000041
  plan: VAL-PLAN-000041

  target:
    type: document
    id: REC-0009
    version: 1.2.0

  snapshot:
    repository: GIT-6fa8c42
    ontology: ONT-2.0.0
    constraints: CS-1.4.0
    validators: VR-1.3.0

  profile: publication

  status: failed

  execution:
    started_at: 2026-08-01T19:10:00+02:00
    completed_at: 2026-08-01T19:10:00.084+02:00
    duration_ms: 84

  coverage:
    planned_validators: 12
    executed_validators: 12
    completed_ratio: 1.0

  summary:
    passed: 8
    passed_with_warnings: 1
    failed: 3
    skipped: 0
    errored: 0

  diagnostics:
    critical: 0
    errors: 2
    warnings: 1
    info: 3

  quality_gates:
    status: failed

  artifacts:
    diagnostics_set: DIAG-SET-000041

  audit:
    event: AUD-VAL-000041
```

---

# Informes resumidos y completos

Podrán existir varias representaciones.

---

## Informe resumido

Incluye:

- estado;
- contadores;
- principales errores;
- gate.

---

## Informe estándar

Añade:

- validators;
- constraints;
- evidencias;
- remediaciones.

---

## Informe técnico

Añade:

- plan;
- dependencias;
- tiempos;
- caché;
- versiones.

---

## Informe de auditoría

Añade:

- hashes;
- permisos;
- supresiones;
- waivers;
- logs;
- trazas;
- artefactos.

---

# Orden de diagnósticos

Orden recomendado:

1. criticidad;
2. fase;
3. documento;
4. posición;
5. código.

---

# Límite de diagnósticos

Una sesión podrá limitar el número de diagnósticos.

---

# Truncamiento

Cuando se alcance el límite deberá indicarse:

```yaml
diagnostics:
  returned: 5000
  total_estimated: 7314
  truncated: true
```

---

# Muestreo

No deberá utilizarse para validaciones críticas salvo que el perfil lo permita.

---

# Auditoría de ejecución

Toda sesión deberá registrar:

- solicitud;
- contexto;
- snapshot;
- plan;
- validators;
- versiones;
- estados;
- resultados;
- supresiones;
- waivers;
- informe.

---

# Identificador de auditoría

Formato recomendado:

```text
AUD-VAL-XXXXXX
```

---

# Contrato

```yaml
audit_event:
  id: AUD-VAL-000041
  type: validation_session_completed

  session: VAL-SESSION-000041
  report: VAL-REPORT-000041

  actor:
    type: user
    id: USER-0001

  timestamp: 2026-08-01T19:10:00.084+02:00

  result:
    status: failed
```

---

# Observabilidad

El pipeline deberá producir:

- logs;
- métricas;
- trazas;
- eventos;
- diagnósticos operacionales.

---

# Logs estructurados

Ejemplo:

```yaml
log:
  level: INFO
  event: validator_completed

  session: VAL-SESSION-000041
  validator: VALIDATOR-IDS
  target: REPO-NOVACOQUINARIA

  status: passed
  duration_ms: 12
```

---

# Trazas

Una traza podrá representar:

```text
Validation Request
↓
Snapshot Resolution
↓
Target Resolution
↓
Planning
↓
Validator Execution
↓
Diagnostic Consolidation
↓
Report Generation
```

---

# Métricas de sesión

Ejemplos:

- sesiones iniciadas;
- sesiones completadas;
- sesiones fallidas;
- duración media;
- p95;
- targets;
- validators;
- diagnósticos;
- cache hit rate;
- validaciones incrementales.

---

# Métricas de validator

Ejemplos:

- ejecuciones;
- duración;
- tasa de fallo;
- tasa de error operacional;
- diagnósticos generados;
- resultados cacheados;
- timeouts.

---

# Métricas de planificación

Ejemplos:

- validators seleccionados;
- validators omitidos;
- dependencias;
- ciclos detectados;
- tiempo de planificación;
- paralelismo real.

---

# Métricas de incrementalidad

Ejemplos:

- targets modificados;
- targets reevaluados;
- validaciones evitadas;
- porcentaje de reutilización;
- dependencias afectadas.

---

# Eventos

El motor podrá emitir:

```text
validation_requested
validation_planned
validation_started
validator_started
validator_completed
diagnostic_created
validation_completed
validation_failed
validation_cancelled
```

---

# Contrato de evento

```yaml
event:
  id: EVT-VAL-000041
  type: validation_completed
  version: 1.0

  timestamp: 2026-08-01T19:10:00.084+02:00

  payload:
    session: VAL-SESSION-000041
    report: VAL-REPORT-000041
    status: failed
```

---

# Seguridad de ejecución

El pipeline deberá comprobar:

- quién solicita;
- qué target puede leer;
- qué validators puede ejecutar;
- qué diagnósticos puede consultar;
- qué evidencias pueden mostrarse.

---

# Ejecución con privilegios

Un validator no deberá elevar permisos respecto a la sesión.

---

# Evidencias restringidas

El informe podrá redaccionar contenido sensible.

---

# Validadores externos

Los validators que invoquen servicios externos deberán declarar:

- endpoint;
- autenticación;
- datos enviados;
- retención;
- timeout;
- política de error.

---

# Aislamiento

Los validators no confiables o experimentales deberán ejecutarse en sandbox.

---

# Límites

Podrán aplicarse:

- CPU;
- memoria;
- disco;
- red;
- tiempo;
- tamaño de salida.

---

# Determinismo y validadores probabilísticos

Por defecto, los validators deberán ser deterministas.

---

# Validator probabilístico

Podrá utilizarse para:

- detección de anomalías;
- clasificación;
- sugerencias;
- calidad lingüística;
- duplicados.

---

# Requisitos reforzados

Deberá registrar:

- modelo;
- versión;
- parámetros;
- puntuación;
- umbral;
- semilla cuando exista;
- confianza.

---

# Diagnóstico probabilístico

No deberá bloquear publicación crítica salvo que una política explícita y validada lo autorice.

---

# Reproducibilidad probabilística

Cuando no sea totalmente reproducible deberá declararse.

---

# Validación distribuida

El pipeline podrá distribuir validators entre workers.

---

# Requisitos

- snapshot compartido;
- contratos versionados;
- idempotencia;
- trazabilidad;
- consolidación determinista;
- tolerancia a duplicados.

---

# Resultado duplicado

El consolidator deberá reconocer dos ejecuciones equivalentes del mismo validator.

---

# Consistencia eventual

Los resultados distribuidos podrán llegar en distinto orden.

La agregación final deberá ser independiente de dicho orden.

---

# Checkpoint distribuido

Deberá conservar:

- validators completados;
- resultados;
- particiones;
- workers;
- snapshot.

---

# Fallo de worker

Las tareas podrán reasignarse si son idempotentes.

---

# Validación en CI/CD

El pipeline podrá ejecutarse en:

- pre-commit;
- Pull Request;
- merge;
- release;
- despliegue;
- auditoría periódica.

---

# Pre-commit

Perfil rápido.

Ejemplos:

- Front Matter;
- IDs;
- enlaces locales;
- sintaxis.

---

# Pull Request

Perfil estándar o publication parcial.

---

# Merge

Perfil global.

---

# Release

Perfil publication estricto.

---

# Auditoría periódica

Perfil completo sobre snapshot.

---

# Validación interactiva

Podrá integrarse con:

- IDE;
- editor;
- CLI;
- panel web;
- API.

---

# Feedback progresivo

El sistema podrá mostrar resultados a medida que finalizan los validators.

El informe definitivo solo se cerrará al completar la sesión.

---

# CLI conceptual

```text
validate target
validate changed
validate repository
validate graph
validate --profile publication
```

---

# Resultado CLI

Deberá utilizar códigos de salida estables.

Ejemplo:

```text
0  passed
1  failed
2  errored
3  blocked
4  partial
```

---

# Pruebas del pipeline

---

# Pruebas unitarias

Para:

- selección;
- dependencias;
- agregación;
- supresiones;
- caché;
- estados.

---

# Pruebas de integración

Para:

- ejecución completa;
- plugins;
- servicios externos;
- informes;
- auditoría.

---

# Pruebas de concurrencia

Para:

- sesiones paralelas;
- caché;
- cancelación;
- reintentos;
- particiones.

---

# Pruebas de idempotencia

La repetición deberá producir:

- mismo estado;
- mismos diagnósticos;
- mismo informe semántico.

---

# Pruebas de recuperación

Deberán comprobar:

- checkpoint;
- reanudación;
- worker caído;
- dependencia temporalmente no disponible.

---

# Pruebas de planificación

Deberán detectar:

- ciclos;
- orden inválido;
- validators incompatibles;
- fallback incorrecto;
- target no soportado.

---

# Golden Validation Run

Un caso de referencia podrá definir:

```yaml
golden_validation_run:
  id: GOLDEN-VAL-0001

  request:
    target: TEST-REC-0001
    profile: standard

  expected:
    status: failed

    diagnostics:
      - code: RECIPE_WITHOUT_INGREDIENTS
        severity: error

    validators:
      executed: 8
      skipped: 0
```

---

# Perfil mínimo de ejecución

La primera implementación podrá incluir:

- ejecución síncrona;
- targets documentales;
- perfiles basic y standard;
- planificación secuencial;
- dependencias simples;
- validación incremental por archivos;
- consolidación de diagnósticos;
- informes;
- códigos de salida;
- caché básica.

---

# Perfil estructurado

Añadirá:

- ejecución asíncrona;
- paralelismo;
- scopes vecinales;
- Target Sets;
- checkpoints;
- reintentos;
- CI/CD;
- auditoría completa.

---

# Perfil semántico

Añadirá:

- validación de grafos;
- impacto ontológico;
- dependencias transitivas;
- SHACL;
- validación global;
- caching semántico.

---

# Perfil enterprise

Añadirá:

- ejecución distribuida;
- colas;
- autoscaling;
- validadores externos;
- trazas distribuidas;
- alta disponibilidad;
- políticas adaptativas;
- reporting avanzado.

---

# Implementación inicial recomendada

La primera implementación práctica debería evolucionar desde las herramientas ya existentes del repositorio:

```text
validate_all.py
        │
        ├── validate_front_matter
        ├── validate_ids
        └── validate_links
```

hacia un pipeline estructurado:

```text
Validation Request
        ↓
Resolve changed Markdown files
        ↓
Run Front Matter Validator
        ↓
Run Identifier Validator
        ↓
Run Internal Links Validator
        ↓
Consolidate Diagnostics
        ↓
Build Validation Report
        ↓
Return Stable Exit Code
```

La primera fase debería soportar:

- ejecución local;
- repositorio Markdown;
- perfiles `basic`, `standard` y `publication`;
- diagnósticos estructurados;
- resultados reproducibles;
- validación incremental por `git diff`;
- informes Markdown o JSON;
- integración con CI.

No será necesario implementar inicialmente:

- ejecución distribuida;
- colas;
- plugins remotos;
- validadores probabilísticos;
- grafos completos;
- autoscaling;
- validación continua;
- caché distribuida.

---

# Caso de uso 1 — Validación de documento modificado

Cambio:

```text
docs/recipes/REC-0009.md
```

Flujo:

```text
Detectar archivo modificado
↓
Resolver target REC-0009
↓
Seleccionar perfil standard
↓
Ejecutar sintaxis y Front Matter
↓
Validar ID
↓
Validar enlaces
↓
Validar tipo documental
↓
Generar informe
```

---

# Caso de uso 2 — ID duplicado

El validator global de identidad detecta:

```text
DOC-0010
```

en dos documentos.

Resultado:

```text
failed
```

Diagnóstico:

```text
DUPLICATE_IDENTIFIER
```

La validación semántica de esos documentos podrá continuar, pero el Quality Gate de publicación deberá bloquearse.

---

# Caso de uso 3 — Error sintáctico crítico

Un Front Matter YAML no puede parsearse.

Resultado:

```text
INVALID_FRONT_MATTER_SYNTAX
```

El pipeline:

- bloquea validadores dependientes de metadatos;
- continúa, si es posible, con validadores independientes;
- genera informe parcial.

---

# Caso de uso 4 — Validación incremental

Un commit modifica una única relación.

El Impact Analyzer selecciona:

- documento modificado;
- target de la relación;
- índice de referencias;
- validator semántico correspondiente.

No ejecuta validadores de todo el repositorio salvo aquellos globales imprescindibles.

---

# Caso de uso 5 — Validator operacionalmente fallido

El servicio ontológico no responde.

Resultado del validator:

```text
errored
```

No:

```text
failed
```

El informe deberá indicar que no pudo determinarse la conformidad ontológica.

El perfil `publication` podrá bloquear el gate.

---

# Caso de uso 6 — Supresión temporal

Existe una supresión válida para:

```text
MISSING_TRANSLATION
```

sobre:

```text
DOC-0042
```

El diagnóstico se genera y conserva, pero queda marcado como suprimido y no bloquea mientras la supresión esté vigente.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Ejecutar todos los validators siempre

Impide escalabilidad e incrementalidad.

---

## Plan implícito

Dificulta auditoría y reproducibilidad.

---

## Mezclar versiones durante la sesión

Produce resultados incoherentes.

---

## Tratar error operacional como incumplimiento

Confunde fallo del motor con fallo del conocimiento.

---

## Marcar validator omitido como superado

Oculta validación incompleta.

---

## Paralelizar validators dependientes

Puede producir resultados incorrectos.

---

## Consolidar por orden de llegada

El resultado deberá ser determinista.

---

## Caché sin dependencias

Puede reutilizar resultados obsoletos.

---

## Reintentar errores semánticos

No resolverá el incumplimiento.

---

## Fail-fast en auditorías completas

Impide obtener una visión global.

---

## Continuar tras sintaxis irrecuperable

Puede producir diagnósticos falsos.

---

## Eliminar diagnósticos suprimidos

Destruye trazabilidad.

---

## Reanudar con snapshot diferente

Rompe reproducibilidad.

---

## Ejecutar validadores experimentales en perfiles estrictos

Debe existir selección explícita.

---

## Bloquear por diagnósticos probabilísticos sin política

Puede producir falsos positivos críticos.

---

## Truncar diagnósticos sin indicarlo

Oculta el alcance real del problema.

---

## Planificar sobre targets dinámicos no materializados

Puede cambiar el ámbito durante la sesión.

---

## Compartir caché entre ámbitos de seguridad incompatibles

Puede filtrar información.

---

## Informes sin versiones

Impiden reproducir el resultado.

---

# Reglas mínimas de conformidad

---

## Solicitud identificada

Toda sesión deberá partir de una solicitud válida.

---

## Contexto inmutable

La sesión deberá fijar sus versiones.

---

## Target resuelto

El conjunto de targets deberá quedar materializado.

---

## Plan explícito

Toda ejecución deberá disponer de un plan.

---

## Dependencias acíclicas

El grafo de validators no deberá contener ciclos.

---

## Estados diferenciados

Deberán distinguirse:

- fallo del target;
- error operacional;
- omisión;
- bloqueo;
- no aplicabilidad.

---

## Diagnósticos persistentes

Los diagnósticos deberán conservar identidad y evidencia.

---

## Agregación determinista

El orden de ejecución no deberá alterar el resultado.

---

## Informe completo

Toda sesión finalizada deberá producir un Validation Report.

---

## Auditoría

La ejecución deberá quedar registrada.

---

## Validación parcial explícita

La incompletitud deberá declararse.

---

## Seguridad

Los validators y resultados deberán respetar el contexto de acceso.

---

# Conformidad de solicitud

Una solicitud será conforme cuando:

- tenga identidad;
- declare target;
- declare perfil;
- declare alcance;
- indique modo;
- respete permisos;
- utilice valores válidos.

---

# Conformidad de contexto

Será conforme cuando:

- fije versiones;
- declare entorno;
- incluya límites;
- identifique actor;
- sea inmutable;
- pueda serializarse.

---

# Conformidad de plan

Será conforme cuando:

- enumere validators;
- declare fases;
- resuelva dependencias;
- indique estrategia;
- permita auditoría;
- posea hash.

---

# Conformidad de ejecución individual

Será conforme cuando:

- identifique validator y versión;
- identifique target;
- tenga estado;
- conserve tiempos;
- produzca diagnósticos o razón de omisión;
- respete límites.

---

# Conformidad de resultado agregado

Será conforme cuando:

- derive de reglas documentadas;
- diferencie estados;
- conserve completitud;
- aplique supresiones;
- preserve diagnósticos;
- sea reproducible.

---

# Conformidad de informe

Será conforme cuando:

- identifique sesión;
- identifique plan;
- declare snapshot;
- incluya estado;
- incluya cobertura;
- incluya diagnósticos;
- incluya métricas;
- enlace auditoría.

---

# Lista de comprobación

Antes de cerrar una sesión deberá comprobarse:

```text
[ ] La solicitud fue validada.
[ ] El contexto quedó fijado.
[ ] El snapshot es coherente.
[ ] Los targets fueron materializados.
[ ] Las constraints aplicables fueron seleccionadas.
[ ] Los validators fueron resueltos.
[ ] El plan no contiene ciclos.
[ ] Las dependencias fueron respetadas.
[ ] Los errores operacionales están diferenciados.
[ ] Las supresiones fueron aplicadas con trazabilidad.
[ ] Los diagnósticos fueron consolidados.
[ ] La completitud fue calculada.
[ ] El estado agregado fue determinado.
[ ] Los Quality Gates fueron evaluados o marcados como pendientes.
[ ] El informe fue generado.
[ ] La auditoría fue registrada.
```

---

# Arquitectura del pipeline

```text
┌───────────────────────────────────────────────┐
│             Validation Request               │
│                                               │
│ Target · Scope · Profile · Rulesets · Limits  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            Execution Context                 │
│                                               │
│ Snapshot · Versions · User · Environment      │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Planning Layer                   │
│                                               │
│ Targets · Constraints · Validators · DAG      │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Validation Runtime               │
│                                               │
│ Phases · Parallelism · Retry · Cache          │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│           Diagnostic Consolidation           │
│                                               │
│ Deduplication · Suppression · Evidence        │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│         Result and Report Generation         │
│                                               │
│ Status · Coverage · Gates · Audit             │
└───────────────────────────────────────────────┘
```

---

# Transición hacia la Parte IV

Esta tercera parte ha definido:

- la solicitud de validación;
- el contexto de ejecución;
- los snapshots;
- la resolución de targets;
- los scopes;
- los perfiles;
- la selección de constraints;
- la selección de validators;
- el plan de validación;
- las dependencias;
- las fases;
- el Validation Runtime;
- la ejecución secuencial y paralela;
- la validación local, global e incremental;
- el análisis de impacto;
- la caché;
- la ejecución síncrona y asíncrona;
- los reintentos;
- los checkpoints;
- la cancelación;
- el fail-fast;
- la degradación;
- la consolidación de diagnósticos;
- la agregación de resultados;
- los informes;
- la auditoría;
- la observabilidad;
- la seguridad;
- las pruebas;
- los perfiles de capacidad.

La Parte IV desarrollará las familias concretas de validación que el motor deberá soportar:

- validación sintáctica;
- validación estructural;
- Front Matter;
- identificadores;
- enlaces;
- esquemas;
- componentes;
- entidades;
- relaciones;
- cardinalidades;
- dominio y rango;
- SHACL;
- consistencia ontológica;
- contexto;
- temporalidad;
- procedencia;
- gobernanza;
- seguridad;
- integridad global del Knowledge Graph.

---

# Conclusión

El pipeline de validación constituye el mecanismo operativo que transforma un conjunto de constraints y validators en una decisión de conformidad reproducible.

Su valor no reside únicamente en ejecutar comprobaciones.

Debe garantizar que cada validación se realiza:

- sobre un snapshot coherente;
- con un perfil conocido;
- mediante un plan explícito;
- respetando dependencias;
- diferenciando incumplimientos de fallos operacionales;
- conservando evidencias;
- midiendo completitud;
- generando informes auditables.

El ciclo puede resumirse así:

```text
Resolver
   ↓
Seleccionar
   ↓
Planificar
   ↓
Ejecutar
   ↓
Consolidar
   ↓
Evaluar
   ↓
Informar
```

La resolución fija el objeto.

La selección determina las reglas.

La planificación ordena el trabajo.

La ejecución aplica los validators.

La consolidación organiza los diagnósticos.

La evaluación determina la conformidad.

El informe conserva el resultado.

Con esta tercera parte queda definido el comportamiento operacional del Validation Engine.

La siguiente parte formalizará las validaciones estructurales, semánticas y ontológicas que permitirán evaluar de forma concreta los distintos artefactos del SGCC.

---

# Parte IV — Validación estructural, semántica y ontológica

---

# Introducción

Las partes anteriores han definido:

- la arquitectura del Validation Engine;
- el modelo formal de restricciones;
- el pipeline de ejecución.

Esta cuarta parte desarrolla el **contenido** de las validaciones que ejecutará el motor.

Hasta ahora se ha definido **cómo** validar.

A partir de este punto se define **qué debe validarse**.

El objetivo es establecer una jerarquía de validaciones suficientemente rigurosa para garantizar la calidad del conocimiento del SGCC desde los niveles más básicos (estructura documental) hasta los niveles más complejos (coherencia ontológica del Knowledge Graph).

---

# Objetivos

Esta parte persigue:

- definir las distintas familias de validación;
- establecer su orden lógico;
- definir las restricciones estructurales;
- definir las restricciones semánticas;
- definir las restricciones ontológicas;
- establecer la validación documental;
- formalizar la validación del grafo;
- definir la integridad del conocimiento;
- establecer los principios de consistencia global.

---

# Jerarquía de validaciones

Las validaciones deberán ejecutarse progresivamente.

```text
Sintaxis

↓

Estructura

↓

Identidad

↓

Referencias

↓

Semántica

↓

Ontología

↓

Gobernanza

↓

Knowledge Graph
```

Cada nivel presupone que los anteriores son suficientemente correctos.

---

# Familias de validación

El Validation Engine organizará las restricciones en familias.

```text
Structural

Documental

Metadata

Identity

Reference

Semantic

Ontology

Collection

Knowledge Graph

Governance

Security
```

Cada familia podrá evolucionar independientemente.

---

# Validación sintáctica

La validación sintáctica constituye el primer nivel.

Su objetivo consiste únicamente en comprobar que el artefacto puede interpretarse.

No evalúa significado.

---

# Ejemplos

- YAML válido.
- JSON válido.
- Markdown parseable.
- UTF-8 correcto.
- caracteres válidos.
- formato permitido.

---

# No responsabilidades

La sintaxis no valida:

- relaciones;
- semántica;
- ontología;
- calidad documental.

---

# Validación estructural

La validación estructural comprueba que el documento respeta la estructura definida por el SGCC.

Pregunta:

```text
¿Está construido correctamente?
```

---

# Ejemplos

- bloques existentes;
- Front Matter;
- encabezados;
- secciones obligatorias;
- tablas;
- listas;
- componentes requeridos.

---

# Restricciones estructurales

Ejemplos:

```text
Toda receta debe contener Front Matter.

Toda plantilla posee un identificador.

Un ingrediente contiene una sección de descripción.

Una técnica dispone de pasos.
```

---

# Front Matter

El Front Matter constituye el contrato estructural principal del SGCC.

Será obligatorio en todos los documentos oficiales.

---

# Restricciones

Ejemplos:

- id obligatorio;
- tipo válido;
- versión;
- título;
- estado;
- fechas;
- colecciones.

---

# Esquemas

Cada tipo documental dispondrá de un esquema.

Ejemplos:

```text
Recipe Schema

Ingredient Schema

Technique Schema

Collection Schema
```

---

# Validación de esquema

Comprueba:

- campos;
- tipos;
- obligatoriedad;
- cardinalidad;
- formato.

---

# Ejemplo

```yaml
id: REC-0008
type: recipe
version: 1.0.0
```

---

# Campos obligatorios

Cada esquema definirá:

```text
Required

Optional

Deprecated

Experimental
```

---

# Campos desconocidos

Podrán:

- aceptarse;
- advertirse;
- rechazarse.

Dependerá del perfil.

---

# Tipos

Ejemplos:

```text
String

Integer

Boolean

Enum

Date

URI

Reference

List
```

---

# Formatos

Ejemplos:

```text
UUID

ISO8601

Semantic Version

Slug

Markdown

URI
```

---

# Validación documental

La validación documental evalúa la organización del contenido.

---

# Ejemplos

- títulos;
- jerarquía;
- secciones;
- orden lógico;
- consistencia interna.

---

# Organización

Ejemplo:

```text
Introducción

Ingredientes

Preparación

Variantes
```

---

# Encabezados

No deberán existir:

- saltos jerárquicos;
- niveles imposibles;
- duplicados.

---

# Tablas

Las tablas deberán cumplir:

- columnas válidas;
- cabeceras;
- alineación.

---

# Código

Los bloques de código deberán indicar lenguaje cuando sea posible.

---

# Validación de componentes

Todo componente reutilizable será validado individualmente.

---

# Ejemplos

```text
Plantillas

Bases

Ingredientes

Técnicas

Utensilios
```

---

# Componentes obligatorios

El sistema comprobará:

- existencia;
- formato;
- referencias;
- dependencias.

---

# Componentes huérfanos

Podrán detectarse componentes sin referencias.

---

# Componentes inaccesibles

También podrán detectarse componentes referenciados inexistentes.

---

# Validación de metadatos

Comprueba:

- autor;
- licencia;
- estado;
- revisión;
- fechas;
- idioma;
- versión.

---

# Procedencia

Todo conocimiento deberá indicar su origen.

---

# Restricciones

Ejemplos:

```text
Toda receta posee fuente.

Toda técnica indica procedencia.

Toda colección posee responsable.
```

---

# Fechas

Las fechas deberán cumplir:

- formato;
- coherencia;
- orden temporal.

---

# Ejemplo

Incorrecto:

```text
updated < created
```

---

# Estado documental

Ejemplos:

```text
draft

review

published

deprecated

archived
```

---

# Compatibilidad

Los estados deberán ser compatibles con el resto de metadatos.

---

# Validación de identidad

Todo artefacto deberá poseer identidad única.

---

# Restricciones

Ejemplos:

- unicidad;
- formato;
- prefijo;
- persistencia.

---

# Identificadores

Ejemplos:

```text
REC

ING

TEC

COL

DOC
```

---

# Colisiones

No podrán existir IDs duplicados.

---

# Persistencia

Un ID no deberá reutilizarse tras eliminar un documento.

---

# Validación de referencias

Comprueba todas las referencias internas.

---

# Ejemplos

- enlaces;
- relaciones;
- componentes;
- colecciones;
- documentos.

---

# Referencias rotas

Generarán diagnóstico.

---

# Referencias circulares

No siempre serán errores.

Dependerá del tipo de relación.

---

# Referencias externas

Podrán validarse:

- formato;
- disponibilidad;
- dominio permitido.

---

# Referencias obsoletas

El sistema podrá detectar:

- documentos retirados;
- versiones antiguas;
- recursos desaparecidos.

---

# Validación semántica

La validación semántica analiza el significado del conocimiento.

Pregunta:

```text
¿Tiene sentido?
```

---

# Diferencia

Estructura:

```text
Está bien construido.
```

Semántica:

```text
Representa correctamente el conocimiento.
```

---

# Ejemplo

Correcto estructuralmente:

```text
ingredient:
   potato
```

Pero semánticamente incorrecto:

```text
Potato

type: Technique
```

---

# Dominio

Cada entidad pertenece a un dominio.

---

# Restricciones

Ejemplos:

```text
Recipe contiene Ingredient.

Technique contiene Steps.

Ingredient no contiene Recipes.
```

---

# Valores válidos

Los valores deberán pertenecer al dominio permitido.

---

# Enumeraciones

Los Enum deberán utilizar únicamente valores autorizados.

---

# Cardinalidades

Las cardinalidades forman parte de la semántica.

Ejemplos:

```text
Recipe

1..*

Ingredient
```

---

# Cardinalidad mínima

Ejemplo:

```text
Toda receta contiene al menos un ingrediente.
```

---

# Cardinalidad máxima

Ejemplo:

```text
Una receta posee un único identificador.
```

---

# Cardinalidades múltiples

Ejemplo:

```text
Technique

0..*

Tips
```

---

# Relaciones

Las relaciones deberán ser semánticamente válidas.

---

# Ejemplos

Correcto:

```text
Recipe

contains

Ingredient
```

Incorrecto:

```text
Ingredient

contains

Recipe
```

---

# Simetría

Algunas relaciones podrán ser simétricas.

---

# Transitividad

Algunas relaciones podrán heredarse.

---

# Relaciones prohibidas

La ontología podrá declarar relaciones imposibles.

---

# Coherencia

El conjunto de relaciones deberá ser coherente.

---

# Validación ontológica

La validación ontológica constituye el nivel conceptual superior.

Pregunta:

```text
¿Respeta el modelo de conocimiento?
```

---

# Ontología

La ontología define:

- clases;
- propiedades;
- relaciones;
- restricciones.

---

# Clases

Toda entidad deberá pertenecer a una clase válida.

---

# Jerarquía

Las jerarquías deberán respetarse.

---

# Herencia

La herencia deberá ser consistente.

---

# Propiedades

Toda propiedad deberá pertenecer a su clase.

---

# Dominio

El dominio deberá respetarse.

---

# Ejemplo

```text
contains

Domain

Recipe
```

---

# Rango

También deberá respetarse.

```text
Range

Ingredient
```

---

# Restricción

Incorrecto:

```text
Recipe

contains

Technique
```

(si la ontología no lo permite)

---

# SHACL

El sistema podrá expresar restricciones mediante SHACL Shapes.

---

# Shapes

Cada Shape representará una restricción ontológica.

---

# Violaciones

Toda violación SHACL generará diagnóstico.

---

# Consistencia ontológica

El motor comprobará:

- contradicciones;
- incompatibilidades;
- dominios;
- rangos;
- cardinalidades.

---

# Disjunciones

Las clases incompatibles no podrán coexistir.

---

# Equivalencias

Las clases equivalentes deberán respetarse.

---

# Inferencias

Las inferencias del Reasoning Engine nunca sustituirán la validación.

Podrán utilizarse como apoyo.

---

# Validación contextual

Algunas restricciones dependerán del contexto.

---

# Ejemplos

- idioma;
- cultura;
- país;
- variante gastronómica.

---

# Contexto temporal

También podrá influir:

- época;
- temporada;
- versión.

---

# Procedencia

La procedencia forma parte del significado.

---

# Restricción

Todo conocimiento deberá indicar origen cuando la política lo exija.

---

# Calidad semántica

Además de la corrección podrá evaluarse la calidad.

Ejemplos:

- ambigüedad;
- duplicidad;
- precisión;
- completitud.

---

# Calidad documental

Ejemplos:

- descripción insuficiente;
- enlaces excesivos;
- referencias ausentes.

---

# Validación de colecciones

Las colecciones deberán cumplir:

- homogeneidad;
- coherencia;
- integridad.

---

# Ejemplo

Una colección de ingredientes no deberá contener recetas.

---

# Cobertura

También podrá comprobarse la cobertura de una colección.

---

# Validación del Knowledge Package

Todo Knowledge Package será validado como unidad.

---

# Restricciones

Ejemplos:

- consistencia;
- referencias;
- dependencias;
- componentes.

---

# Integridad

No deberán existir dependencias incompletas.

---

# Validación del Knowledge Graph

El Knowledge Graph constituye el nivel global.

---

# Restricciones globales

Ejemplos:

- IDs únicos;
- relaciones válidas;
- ausencia de ciclos prohibidos;
- conectividad.

---

# Componentes aislados

El sistema podrá detectar:

```text
Orphan Nodes
```

---

# Relaciones redundantes

También podrán detectarse.

---

# Ciclos

No todos los ciclos serán errores.

Dependerá del modelo.

---

# Densidad

Podrán calcularse métricas.

---

# Conectividad

El sistema podrá identificar regiones aisladas.

---

# Integridad global

La integridad representa la ausencia de contradicciones.

---

# Consistencia global

El conjunto del Knowledge Graph deberá permanecer consistente.

---

# Validación multinivel

Una misma entidad podrá atravesar:

```text
Sintaxis

↓

Estructura

↓

Semántica

↓

Ontología

↓

Knowledge Graph
```

---

# Estrategia

Cada nivel reducirá progresivamente el número de errores posibles.

---

# Independencia

Cada familia de validación podrá evolucionar independientemente.

---

# Extensibilidad

Nuevas familias podrán añadirse sin modificar el núcleo del motor.

---

# Arquitectura conceptual

```text
Artefacto

↓

Sintaxis

↓

Estructura

↓

Metadatos

↓

Identidad

↓

Referencias

↓

Semántica

↓

Ontología

↓

Knowledge Graph

↓

Resultado
```

---

# Perfil mínimo recomendado

La primera implementación debería incluir:

- Front Matter;
- esquemas;
- IDs;
- enlaces internos;
- metadatos;
- componentes.

---

# Perfil intermedio

Añadirá:

- semántica;
- relaciones;
- cardinalidades;
- colecciones.

---

# Perfil avanzado

Añadirá:

- SHACL;
- ontología;
- validación global;
- métricas del grafo.

---

# Perfil enterprise

Incorporará:

- validación distribuida;
- razonamiento asistido;
- validación continua;
- restricciones dinámicas;
- perfiles adaptativos;
- monitorización permanente del Knowledge Graph.

---

# Transición hacia la Parte V

Con esta parte quedan definidas las familias de validación que el Validation Engine deberá soportar.

La Parte V desarrollará los mecanismos que convierten los resultados técnicos en decisiones operativas mediante:

- **Quality Gates**;
- políticas de aceptación;
- scoring de calidad;
- informes ejecutivos y técnicos;
- integración con CI/CD;
- integración con el Ingestion Engine;
- integración con el Reasoning Engine;
- integración con el Knowledge Graph;
- APIs de validación;
- eventos y observabilidad.

---

# Conclusión

El Validation Engine no valida únicamente documentos, sino la conformidad integral del conocimiento en todos sus niveles de abstracción.

La validación se organiza como una pirámide de confianza, donde cada nivel se apoya en el anterior: desde la correcta interpretación sintáctica del artefacto hasta la consistencia ontológica y la integridad global del Knowledge Graph.

Esta organización modular permitirá que NovaCoquinaria incorpore nuevas familias de validación en el futuro sin alterar la arquitectura del motor, garantizando que la calidad del conocimiento evolucione al mismo ritmo que el propio SGCC.

---

# Parte V — Quality Gates, reporting e integración

---

# Introducción

Las partes anteriores han definido:

- la arquitectura del Validation Engine;
- el modelo formal de constraints, rules, validators y diagnostics;
- el pipeline de ejecución;
- la validación incremental, local y global;
- las familias de validación sintáctica, estructural, semántica y ontológica;
- la validación de documentos, componentes, colecciones, Knowledge Packages y Knowledge Graph.

Esta quinta parte establece cómo los resultados técnicos de validación se convierten en decisiones operativas dentro de NovaCoquinaria.

Una validación no finaliza cuando se detectan errores o advertencias.

El sistema deberá determinar:

- si el conocimiento puede continuar hacia la siguiente fase;
- si puede publicarse;
- si requiere revisión;
- si debe bloquearse;
- si puede aceptarse con deuda conocida;
- si necesita cuarentena;
- si el resultado es suficientemente completo y fiable.

Los **Quality Gates** constituyen el mecanismo mediante el cual el SGCC transforma un conjunto de diagnósticos en una decisión gobernada.

Conceptualmente:

```text
Validation Results
        ↓
Diagnostic Consolidation
        ↓
Quality Metrics
        ↓
Quality Gates
        ↓
Operational Decision
```

Esta parte también define:

- los informes del Validation Engine;
- el scoring de calidad;
- la integración con CI/CD;
- la integración con el Ingestion Engine;
- la integración con el Knowledge Graph;
- la integración con el Reasoning Engine;
- las APIs;
- los eventos;
- la observabilidad;
- la seguridad de los resultados.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir el concepto de Quality Gate;
- formalizar criterios de aceptación y bloqueo;
- distinguir validación técnica de decisión operativa;
- definir perfiles de gates;
- establecer modelos de scoring;
- definir informes técnicos, ejecutivos y de auditoría;
- regular evidencias y remediaciones;
- integrar el Validation Engine con CI/CD;
- integrar la validación con el Ingestion Engine;
- integrar la validación con el Knowledge Graph;
- integrar la validación con el Reasoning Engine;
- definir APIs de validación;
- definir eventos y notificaciones;
- establecer observabilidad y métricas;
- regular permisos, sensibilidad y acceso a resultados;
- definir mecanismos de revisión y aprobación.

---

# Principios de decisión

Toda decisión derivada de una validación deberá respetar los siguientes principios.

---

## La decisión no es un booleano simple

El resultado no deberá reducirse únicamente a:

```text
válido
```

o:

```text
inválido
```

El sistema deberá distinguir, al menos:

```text
accepted
accepted_with_warnings
conditionally_accepted
rejected
blocked
quarantined
indeterminate
```

---

## El Quality Gate no sustituye la validación

La validación produce evidencia.

El gate aplica una política sobre esa evidencia.

---

## Políticas explícitas

Toda decisión deberá derivar de:

- una política;
- un perfil;
- una versión;
- un conjunto de thresholds;
- un contexto.

---

## Reproducibilidad

Con los mismos resultados y la misma política, el gate deberá producir la misma decisión.

---

## Explicabilidad

Toda decisión deberá poder explicar:

- qué reglas se aplicaron;
- qué diagnósticos influyeron;
- qué métricas se utilizaron;
- por qué se aceptó o bloqueó;
- qué condiciones quedan pendientes.

---

## Separación entre severidad y bloqueo

Un diagnóstico de severidad `warning` podrá bloquear en determinados perfiles.

Un diagnóstico `error` podrá quedar cubierto por un waiver autorizado.

La severidad describe impacto.

La política determina el efecto operativo.

---

## Fallo seguro

En perfiles críticos, la ausencia de resultados suficientes deberá bloquear.

---

## No aceptación por puntuación únicamente

Una buena puntuación global nunca deberá compensar una violación crítica.

---

## Revisión gobernada

Las excepciones deberán ser explícitas, temporales cuando proceda y auditables.

---

# Quality Gate

Un **Quality Gate** es una política evaluable que determina si un conjunto de resultados de validación permite continuar hacia una fase concreta.

Formalmente:

```text
Quality Gate =
Input Results
+
Policy
+
Thresholds
+
Context
+
Decision
```

---

# Identidad de Quality Gate

Formato recomendado:

```text
QG-<DOMINIO>-XXXX
```

Ejemplos:

```text
QG-DOCUMENT-0001
QG-INGESTION-0002
QG-PUBLICATION-0001
QG-RELEASE-0001
QG-SECURITY-0001
```

---

# Contrato mínimo

```yaml
quality_gate:
  id: QG-PUBLICATION-0001

  name: Publication Quality Gate

  status: active
  version: 1.0.0
```

---

# Contrato ampliado

```yaml
quality_gate:
  id: QG-PUBLICATION-0001

  name:
    es: Puerta de calidad para publicación

  description: >
    Determina si un Knowledge Package puede publicarse
    en el Knowledge Graph de producción.

  version: 1.0.0
  status: active

  target:
    types:
      - KnowledgePackage

  profile:
    required: publication

  criteria:
    all:
      - completed_validation_ratio >= 1.0
      - critical_diagnostics == 0
      - unsuppressed_errors == 0
      - ontology_validation == passed
      - provenance_validation == passed
      - security_validation == passed

  warnings:
    maximum: 25

  decision:
    on_pass: accepted
    on_warning_threshold: conditionally_accepted
    on_fail: rejected
    on_incomplete: blocked

  governance:
    owner: knowledge_quality_team
    review_required: true
```

---

# Tipos de Quality Gate

---

## Gate documental

Evalúa documentos individuales.

---

## Gate de Knowledge Package

Determina si un paquete puede pasar a publicación.

---

## Gate de ingesta

Evalúa si una ejecución de ingesta puede continuar.

---

## Gate semántico

Comprueba conformidad con:

- vocabulario;
- relaciones;
- ontología;
- restricciones.

---

## Gate de Knowledge Graph

Evalúa integridad global o parcial del grafo.

---

## Gate de migración

Determina si una migración puede continuar.

---

## Gate de Pull Request

Evalúa cambios antes de merge.

---

## Gate de release

Evalúa la preparación de una versión.

---

## Gate de seguridad

Comprueba:

- secretos;
- permisos;
- sensibilidad;
- privacidad;
- políticas críticas.

---

## Gate de auditoría

Exige trazabilidad y evidencia completas.

---

# Niveles de Quality Gate

Los gates podrán encadenarse.

```text
Gate 1 — Sintaxis
        ↓
Gate 2 — Estructura
        ↓
Gate 3 — Semántica
        ↓
Gate 4 — Gobernanza
        ↓
Gate 5 — Seguridad
        ↓
Gate 6 — Publicación
```

---

# Dependencias entre gates

Un gate podrá depender de otros.

Ejemplo:

```text
QG-PUBLICATION-0001
```

requiere:

```text
QG-STRUCTURE-0001
QG-SEMANTIC-0001
QG-SECURITY-0001
```

---

# Gate compuesto

Un gate compuesto combina varias decisiones.

---

# Gate secuencial

Los gates se evalúan en orden.

---

# Gate paralelo

Varios gates independientes pueden evaluarse al mismo tiempo.

---

# Gate bloqueante

Impide continuar si falla.

---

# Gate informativo

Genera resultado, pero no bloquea.

---

# Gate condicional

Permite continuar bajo condiciones.

---

# Gate manual

Requiere aprobación humana.

---

# Gate automatizado

Produce una decisión sin intervención humana.

---

# Entrada del Quality Gate

El gate podrá utilizar:

- Validation Report;
- diagnósticos;
- métricas;
- cobertura;
- estado de validators;
- waivers;
- supresiones;
- contexto;
- historial;
- perfil;
- datos de riesgo.

---

# Resultado del Quality Gate

Formato recomendado:

```text
QG-RESULT-XXXXXX
```

---

# Contrato de resultado

```yaml
quality_gate_result:
  id: QG-RESULT-000041

  gate:
    id: QG-PUBLICATION-0001
    version: 1.0.0

  validation_report: VAL-REPORT-000041

  decision: rejected

  reasons:
    - code: UNSUPPRESSED_ERRORS
      observed: 2
      expected: 0

  evaluated_at: 2026-08-01T20:00:00+02:00
```

---

# Decisiones

Valores recomendados:

```text
accepted
accepted_with_warnings
conditionally_accepted
rejected
blocked
quarantined
indeterminate
manual_review_required
```

---

# Accepted

El target puede continuar sin restricciones.

---

# AcceptedWithWarnings

Puede continuar, pero conserva advertencias.

---

# ConditionallyAccepted

Puede continuar si se cumplen condiciones explícitas.

Ejemplo:

```text
Publicar únicamente en entorno experimental.
```

---

# Rejected

No puede continuar.

---

# Blocked

No existe evidencia suficiente para decidir o una dependencia crítica ha fallado.

---

# Quarantined

El target queda aislado hasta revisión.

---

# Indeterminate

Los resultados son insuficientes o contradictorios.

---

# ManualReviewRequired

Se requiere una decisión humana.

---

# Criterio

Un criterio representa una condición evaluable dentro de un gate.

---

# Identidad de criterio

Formato recomendado:

```text
QGC-XXXXXX
```

---

# Tipos de criterio

- conteo;
- severidad;
- estado;
- cobertura;
- score;
- presencia;
- ausencia;
- compatibilidad;
- tendencia;
- revisión;
- seguridad.

---

# Criterio de conteo

Ejemplo:

```text
critical_diagnostics == 0
```

---

# Criterio de severidad

Ejemplo:

```text
maximum_unsuppressed_severity <= warning
```

---

# Criterio de estado

Ejemplo:

```text
ontology_validation == passed
```

---

# Criterio de cobertura

Ejemplo:

```text
completed_validation_ratio >= 0.95
```

---

# Criterio de scoring

Ejemplo:

```text
quality_score >= 85
```

---

# Criterio de revisión

Ejemplo:

```text
semantic_reviewer_approval == true
```

---

# Criterio de seguridad

Ejemplo:

```text
secret_detection_result == passed
```

---

# Expresiones de gate

Las expresiones deberán utilizar un lenguaje limitado y seguro.

Ejemplo:

```yaml
criteria:
  all:
    - metric: critical_diagnostics
      operator: equals
      value: 0

    - metric: validation_coverage
      operator: greater_than_or_equal
      value: 1.0
```

---

# Operadores

Podrán soportarse:

```text
equals
not_equals
greater_than
greater_than_or_equal
less_than
less_than_or_equal
contains
not_contains
in
not_in
exists
not_exists
```

---

# Combinación de criterios

---

## All

Todos deben cumplirse.

---

## Any

Al menos uno.

---

## None

Ninguno.

---

## At least N

Debe cumplirse un número mínimo.

---

## Weighted

Cada criterio aporta un peso.

No deberá utilizarse para neutralizar bloqueos críticos.

---

# Precedencia de criterios

Orden recomendado:

1. seguridad;
2. integridad;
3. errores críticos;
4. completitud;
5. ontología;
6. gobernanza;
7. calidad;
8. advertencias;
9. métricas informativas.

---

# Política de bloqueo

Toda política deberá declarar qué situaciones bloquean.

Ejemplos:

```text
critical_diagnostic
validator_errored
coverage_below_threshold
missing_provenance
ontology_incompatible
secret_detected
```

---

# Bloqueo por incompletitud

Un gate podrá bloquear si la validación no se completó.

Ejemplo:

```yaml
incomplete_validation:
  policy: block
```

---

# Bloqueo por validator fallido

Deberá distinguirse:

```text
validator failed
```

de:

```text
validator errored
```

Ambos podrán bloquear, pero por motivos diferentes.

---

# Política fail-open

Permite continuar cuando un validator no está disponible.

Solo deberá utilizarse en contextos de bajo riesgo.

---

# Política fail-closed

Bloquea ante ausencia de evidencia.

Será obligatoria en:

- seguridad;
- privacidad;
- publicación canónica;
- migraciones críticas;
- alérgenos;
- toxicidad.

---

# Excepciones al Quality Gate

Un gate podrá aceptar:

- waiver;
- aprobación manual;
- excepción temporal;
- entorno experimental.

---

# Waiver de gate

Formato recomendado:

```text
QG-WAIVER-XXXXXX
```

---

# Contrato

```yaml
quality_gate_waiver:
  id: QG-WAIVER-000041

  gate: QG-PUBLICATION-0001
  target: KP-000421

  waived_criteria:
    - QGC-MISSING-TRANSLATION

  justification: >
    La traducción se incorporará antes de la publicación pública.

  scope:
    environment: staging

  approved_by: USER-0008
  approved_at: 2026-08-01

  expires_at: 2026-08-15
```

---

# Restricciones del waiver

No deberá permitir excepciones sobre:

- secretos;
- corrupción estructural;
- colisiones de identidad;
- pérdida de procedencia crítica;
- violaciones legales;
- riesgos críticos de seguridad.

---

# Revisión manual

Algunos gates podrán requerir aprobación humana.

---

# Tipos de revisión

- semántica;
- culinaria;
- editorial;
- ontológica;
- seguridad;
- legal;
- publicación.

---

# Contrato de revisión

```yaml
review:
  id: REVIEW-VAL-000041

  target: KP-000421
  gate: QG-PUBLICATION-0001

  reviewer:
    id: USER-0008
    role: semantic_reviewer

  decision: approved_with_conditions

  conditions:
    - resolve_warning_before_public_release

  reviewed_at: 2026-08-01
```

---

# Separación de funciones

Cuando proceda, quien genera el contenido no debería ser la única persona que lo aprueba.

---

# Doble aprobación

Podrá exigirse en:

- cambios ontológicos;
- seguridad alimentaria;
- publicación pública;
- fusiones de identidad;
- migraciones incompatibles.

---

# Quality Score

El Validation Engine podrá calcular una puntuación global de calidad.

---

# Propósito

El score puede servir para:

- comparar;
- priorizar;
- monitorizar;
- detectar tendencias;
- identificar deuda.

No deberá sustituir los criterios bloqueantes.

---

# Escala

Formato recomendado:

```text
0–100
```

---

# Dimensiones de calidad

Podrán incluir:

```text
structural_quality
metadata_quality
semantic_quality
ontology_quality
provenance_quality
documentation_quality
security_quality
governance_quality
```

---

# Contrato de score

```yaml
quality_score:
  total: 88.5

  dimensions:
    structural: 100
    metadata: 85
    semantic: 92
    ontology: 90
    provenance: 80
    governance: 84

  model:
    id: QUALITY-MODEL-0001
    version: 1.0.0
```

---

# Modelo de scoring

Toda fórmula deberá estar:

- documentada;
- versionada;
- probada;
- calibrada;
- auditable.

---

# Ponderación

Ejemplo:

```text
Structural       15 %
Metadata         10 %
Semantic         25 %
Ontology         20 %
Provenance       15 %
Governance       15 %
```

---

# Penalizaciones

Podrán aplicarse por:

- warnings;
- deuda;
- información ausente;
- duplicados;
- baja cobertura;
- procedencia incompleta.

---

# Bloqueos no compensables

Un diagnóstico crítico deberá producir:

```text
gate = failed
```

aunque el score sea alto.

---

# Score de confianza

No deberá confundirse con la calidad.

```text
quality_score
```

mide conformidad y completitud.

```text
confidence_score
```

mide seguridad de una extracción o predicción.

---

# Tendencia de calidad

El sistema podrá comparar scores a lo largo del tiempo.

---

# Quality Regression

Una disminución relevante podrá bloquear.

Ejemplo:

```yaml
quality_regression:
  maximum_allowed_drop: 5
```

---

# Baseline

Una validación podrá compararse con una línea base.

---

# Baseline de Pull Request

Representa el estado de la rama objetivo.

---

# Delta de calidad

```text
score_after - score_before
```

---

# Diagnósticos nuevos

El sistema deberá distinguir:

- existentes;
- corregidos;
- nuevos;
- agravados;
- reducidos.

---

# New Issues Policy

Un gate podrá permitir deuda histórica, pero impedir nueva deuda.

Ejemplo:

```yaml
new_issues:
  errors_allowed: 0
  warnings_allowed: 3
```

---

# Debt Baseline

La deuda aceptada deberá estar identificada.

No deberá ocultarse como éxito completo.

---

# Reporting

El Validation Engine deberá producir informes adaptados a distintos consumidores.

---

# Tipos de informe

```text
summary
developer
quality
publication
executive
audit
machine_readable
```

---

# Informe resumido

Incluye:

- estado;
- gate;
- contadores;
- principales diagnósticos;
- siguiente acción.

---

# Informe para desarrolladores

Incluye:

- archivo;
- línea;
- constraint;
- evidencia;
- remediation;
- validator;
- versión.

---

# Informe de calidad

Incluye:

- score;
- dimensiones;
- tendencias;
- deuda;
- cobertura;
- regresiones.

---

# Informe de publicación

Incluye:

- gates;
- revisiones;
- waivers;
- bloqueos;
- snapshot;
- decisión.

---

# Informe ejecutivo

Incluye:

- estado general;
- riesgos;
- evolución;
- áreas de atención;
- decisión recomendada.

No deberá ocultar limitaciones relevantes.

---

# Informe de auditoría

Incluye:

- solicitud;
- contexto;
- snapshot;
- plan;
- validators;
- resultados;
- evidencias;
- waivers;
- revisiones;
- hashes;
- trazas;
- decisión.

---

# Informe legible por máquinas

Formatos posibles:

- JSON;
- YAML;
- SARIF;
- RDF;
- CSV;
- XML.

---

# SARIF

Podrá utilizarse para integración con herramientas de desarrollo.

---

# Markdown

Será adecuado para:

- repositorio;
- CI;
- documentación;
- Pull Requests.

---

# HTML

Será adecuado para:

- dashboards;
- informes navegables;
- auditorías.

---

# Contrato de report package

```yaml
report_package:
  id: VAL-REPORT-PKG-000041

  validation_report: VAL-REPORT-000041

  quality_gate_results:
    - QG-RESULT-000041

  quality_score:
    total: 88.5

  formats:
    - type: json
      location: reports/validation/VAL-REPORT-000041.json

    - type: markdown
      location: reports/validation/VAL-REPORT-000041.md
```

---

# Resumen de diagnósticos

El informe deberá separar:

- activos;
- suprimidos;
- cubiertos por waiver;
- resueltos;
- nuevos;
- históricos.

---

# Causa raíz

Cuando varios diagnósticos deriven del mismo problema, el informe debería destacar la causa principal.

---

# Remediation Plan

El sistema podrá generar un plan de remediación.

---

# Contrato

```yaml
remediation_plan:
  id: REM-PLAN-000041

  target: REC-0009

  actions:
    - priority: critical
      diagnostic: DIAG-000081
      action: add_front_matter

    - priority: high
      diagnostic: DIAG-000082
      action: assign_unique_identifier
```

---

# Orden de remediación

Recomendación:

1. sintaxis;
2. estructura;
3. identidad;
4. referencias;
5. semántica;
6. ontología;
7. gobernanza;
8. calidad.

---

# Auto-fix

Algunos diagnósticos podrán ofrecer corrección automática.

---

# Separación de responsabilidades

El Validation Engine podrá proponer un fix.

No deberá aplicarlo directamente salvo flujo explícito y gobernado.

---

# Fix Proposal

Formato recomendado:

```text
FIX-PROPOSAL-XXXXXX
```

---

# Contrato

```yaml
fix_proposal:
  id: FIX-PROPOSAL-000041

  diagnostic: DIAG-000081

  operation:
    type: add_front_matter

  confidence: 1.0

  requires_review: true
```

---

# Aplicación de fix

Deberá realizarse mediante:

- herramienta especializada;
- transacción;
- revisión;
- auditoría.

---

# Verificación posterior

Tras aplicar un fix deberá ejecutarse nuevamente la validación afectada.

---

# Integración con el Ingestion Engine

El Validation Engine constituye un servicio central del pipeline de ingesta.

---

# Flujo

```text
Knowledge Package
        ↓
Validation Request
        ↓
Validation Engine
        ↓
Quality Gate
        ↓
Publication Decision
```

---

# Validación previa a publicación

Todo Knowledge Package deberá superar el perfil requerido.

---

# Resultado para Ingestion Engine

```yaml
ingestion_validation_result:
  package: KP-000421

  validation_report: VAL-REPORT-000041
  publication_gate: QG-RESULT-000041

  decision: rejected
```

---

# Comportamiento del Ingestion Engine

Según la decisión:

---

## Accepted

Continuar a publicación.

---

## AcceptedWithWarnings

Continuar y conservar warnings.

---

## ConditionallyAccepted

Continuar únicamente bajo las condiciones declaradas.

---

## Rejected

Detener publicación.

---

## Blocked

Esperar resolución de dependencia.

---

## Quarantined

Mover a cuarentena.

---

# Feedback al pipeline

Los diagnósticos deberán regresar al paso responsable.

Ejemplo:

```text
INVALID_FRONT_MATTER
```

se vincula con:

```text
normalization
```

o:

```text
source_document
```

---

# Reprocesamiento

El Ingestion Engine podrá reanudar desde el checkpoint apropiado tras corregir el problema.

---

# Validación progresiva

Podrá ejecutarse en varias fases:

```text
Extracción
↓
Validación sintáctica

Normalización
↓
Validación estructural

Enriquecimiento
↓
Validación semántica

Publicación
↓
Validación global
```

---

# Cuarentena de ingesta

Los paquetes con problemas de:

- seguridad;
- licencia;
- identidad;
- corrupción;
- datos personales;

deberán aislarse.

---

# Integración con el Knowledge Graph

El Validation Engine podrá validar:

- planes de publicación;
- nodos;
- afirmaciones;
- relaciones;
- snapshots;
- subgrafos;
- grafo completo.

---

# Validación previa al commit

El Graph Integration Layer podrá solicitar:

```text
validate_graph_plan
```

---

# Validación post-publicación

Después del commit podrá ejecutarse:

```text
validate_graph_snapshot
```

---

# Flujo recomendado

```text
Graph Plan
    ↓
Pre-publication Validation
    ↓
Commit
    ↓
Read-after-write Validation
    ↓
Post-publication Gate
```

---

# Inconsistencia post-publicación

Podrá producir:

- rollback;
- compensación;
- bloqueo del snapshot;
- incidente;
- cuarentena.

---

# Validación de snapshot

Deberá indicar:

- versión;
- ontología;
- cobertura;
- diagnósticos;
- integridad;
- score.

---

# Estado de snapshot

Valores posibles:

```text
valid
valid_with_warnings
invalid
blocked
under_review
```

---

# Integración con el Reasoning Engine

El Reasoning Engine podrá consumir resultados de validación.

---

# Premisas validadas

Los perfiles estrictos deberán utilizar únicamente:

```text
validated
```

o:

```text
confirmed
```

---

# Validación de reglas

El Validation Engine deberá validar:

- sintaxis;
- variables;
- predicados;
- tipos;
- dependencias;
- terminación;
- explicación;
- seguridad.

---

# Validación de inferencias

Podrá comprobar:

- premisas;
- regla;
- contexto;
- versión;
- consistencia;
- procedencia.

---

# Inferencia inválida

Deberá bloquearse o invalidarse.

---

# Inferencia obsoleta

Podrá detectarse cuando cambie una dependencia.

---

# Quality Gate inferencial

Ejemplo:

```yaml
quality_gate:
  id: QG-INFERENCE-0001

  criteria:
    all:
      - premises_valid == true
      - rule_status == stable
      - explanation_available == true
      - conflicts == 0
```

---

# Validación antes de materialización

Toda inferencia materializada deberá superar el gate correspondiente.

---

# Integración con Colecciones

Las colecciones podrán validarse respecto a:

- definición;
- criterios;
- membresía;
- coherencia;
- completitud;
- snapshot;
- reglas de resolución.

---

# Pertenencia inválida

Una entidad incompatible con el tipo de colección deberá generar diagnóstico.

---

# Colección dinámica

Deberá validar:

- consulta;
- ruleset;
- dependencias;
- materialización;
- explicación de pertenencia.

---

# Integración con GraphRAG

GraphRAG podrá utilizar el Validation Engine para:

- validar chunks;
- comprobar metadatos;
- verificar fuentes;
- validar claims;
- comprobar grounding;
- detectar contradicciones.

---

# Validación del contexto RAG

El paquete de contexto deberá comprobar:

- accesibilidad;
- relevancia mínima;
- procedencia;
- estado;
- sensibilidad;
- vigencia.

---

# Validación de respuesta

Cada claim podrá clasificarse:

```text
supported
inferred
partially_supported
unsupported
contradicted
indeterminate
```

---

# Gate de respuesta

Podrá bloquear respuestas:

- no fundamentadas;
- contradictorias;
- sensibles;
- inseguras.

---

# Integración con agentes

Los agentes podrán invocar:

```text
validate_entity
validate_action
validate_plan
validate_output
validate_claims
```

---

# Validación de acción

Antes de ejecutar una acción, el agente podrá comprobar:

- precondiciones;
- permisos;
- restricciones;
- riesgo;
- coherencia.

---

# Validación de plan

Podrá comprobar:

- dependencias;
- orden;
- recursos;
- incompatibilidades;
- políticas.

---

# Validación de salida

Podrá comprobar:

- formato;
- contenido;
- procedencia;
- seguridad;
- grounding.

---

# Agente bloqueado por gate

Un agente deberá respetar una decisión `rejected` o `blocked`.

No deberá eludirla modificando el prompt.

---

# APIs del Validation Engine

El Validation Engine deberá exponer contratos versionados.

---

# Endpoints conceptuales

```text
POST /validation/execute
POST /validation/plan
POST /validation/gates/evaluate
POST /validation/fixes/propose
GET  /validation/sessions/{id}
GET  /validation/reports/{id}
GET  /validation/diagnostics/{id}
GET  /validation/constraints
GET  /validation/validators
GET  /validation/gates
```

---

# Ejecutar validación

```http
POST /api/v1/validation/execute
```

---

# Solicitud conceptual

```json
{
  "target": {
    "type": "document",
    "id": "REC-0009"
  },
  "profile": "publication",
  "scope": {
    "mode": "local",
    "includeDependencies": true
  }
}
```

---

# Respuesta conceptual

```json
{
  "sessionId": "VAL-SESSION-000041",
  "status": "failed",
  "reportId": "VAL-REPORT-000041",
  "qualityGate": {
    "id": "QG-RESULT-000041",
    "decision": "rejected"
  },
  "summary": {
    "errors": 2,
    "warnings": 1
  }
}
```

---

# Planificar validación

```http
POST /api/v1/validation/plan
```

Devuelve:

- targets;
- constraints;
- validators;
- fases;
- dependencias;
- coste estimado.

---

# Evaluar gate

```http
POST /api/v1/validation/gates/evaluate
```

---

# Recuperar informe

```http
GET /api/v1/validation/reports/VAL-REPORT-000041
```

---

# Recuperar diagnóstico

```http
GET /api/v1/validation/diagnostics/DIAG-000081
```

---

# Listar constraints

```http
GET /api/v1/validation/constraints
```

Filtros:

- categoría;
- estado;
- versión;
- target;
- severidad;
- owner.

---

# Validación síncrona

Adecuada para:

- documentos;
- acciones;
- claims;
- pre-commit.

---

# Validación asíncrona

Adecuada para:

- repositorio;
- Knowledge Graph;
- migraciones;
- auditorías;
- release.

---

# Idempotencia API

Las solicitudes deberán admitir:

```http
Idempotency-Key
```

---

# Errores de API

Ejemplos:

```text
UNKNOWN_TARGET
UNKNOWN_PROFILE
INCOMPATIBLE_VALIDATOR_VERSION
VALIDATION_TIMEOUT
GATE_NOT_FOUND
UNAUTHORIZED_EVIDENCE
SNAPSHOT_NOT_AVAILABLE
```

---

# Contrato de error

```json
{
  "error": {
    "code": "UNKNOWN_PROFILE",
    "message": "El perfil solicitado no existe.",
    "traceId": "TRACE-VAL-000041"
  }
}
```

---

# Integración mediante eventos

El Validation Engine podrá consumir y publicar eventos.

---

# Eventos de entrada

```text
document_changed
knowledge_package_ready
graph_plan_created
graph_snapshot_created
rule_changed
ontology_changed
release_candidate_created
```

---

# Eventos de salida

```text
validation_requested
validation_started
diagnostic_created
validation_completed
quality_gate_passed
quality_gate_failed
manual_review_required
target_quarantined
```

---

# Contrato de evento

```yaml
event:
  id: EVT-VAL-000081
  type: quality_gate_failed
  version: 1.0

  timestamp: 2026-08-01T20:15:00+02:00
  trace_id: TRACE-VAL-000041

  payload:
    gate_result: QG-RESULT-000041
    target: KP-000421
    decision: rejected
```

---

# Eventos idempotentes

Los consumidores deberán soportar duplicados.

---

# Orden de eventos

No deberá asumirse orden global.

---

# Eventos sensibles

Deberán proteger:

- evidencias;
- datos personales;
- secretos;
- contenido restringido.

---

# Integración con CI/CD

El Validation Engine deberá formar parte de los pipelines de calidad.

---

# Pre-commit

Validaciones rápidas:

- sintaxis;
- Front Matter;
- ID local;
- referencias modificadas.

---

# Pull Request

Validaciones:

- estructura;
- IDs globales;
- enlaces;
- semántica;
- deuda nueva;
- quality regression.

---

# Merge

Validación global del repositorio.

---

# Release

Perfil estricto:

- validación completa;
- gate de publicación;
- baseline;
- compatibilidad;
- snapshot;
- auditoría.

---

# Despliegue

Podrá validar:

- configuración;
- esquema;
- compatibilidad;
- migración;
- reglas;
- endpoints.

---

# Quality Gate de CI

Un job deberá utilizar códigos de salida estables.

Ejemplo:

```text
0 accepted
1 rejected
2 blocked
3 errored
4 manual_review_required
```

---

# Pull Request Decoration

El sistema podrá publicar:

- resumen;
- diagnósticos nuevos;
- archivos afectados;
- score;
- gate;
- enlaces a informes.

---

# Comentarios inline

Podrán generarse cuando exista:

- archivo;
- línea;
- columna;
- diagnóstico.

---

# Baseline de CI

El pipeline deberá comparar contra:

- rama principal;
- último release;
- snapshot aprobado.

---

# Política de nueva deuda

Ejemplo:

```yaml
pull_request_gate:
  new_errors: 0
  new_critical: 0
  maximum_new_warnings: 5
  minimum_score: 85
```

---

# Quality Gate de release

Podrá exigir:

- cero críticos;
- cero errores;
- score mínimo;
- cobertura completa;
- validación global;
- compatibilidad;
- aprobación humana;
- documentación actualizada.

---

# Integración con herramientas actuales

La implementación inicial podrá envolver las validaciones existentes:

```text
validate_front_matter.py
validate_ids.py
validate_links.py
validate_all.py
```

---

# Evolución de `validate_all.py`

Podrá pasar de:

```text
orquestador procedural
```

a:

```text
cliente CLI del Validation Engine
```

---

# Salida estructurada

Además del texto actual deberá poder producir:

```text
JSON
Markdown
SARIF
```

---

# Compatibilidad hacia atrás

La salida legible existente podrá mantenerse mientras se introduce el nuevo contrato.

---

# Observabilidad

El Validation Engine deberá ser observable a nivel técnico y de calidad.

---

# Logs

Los logs deberán incluir:

- sesión;
- target;
- validator;
- constraint;
- gate;
- decisión;
- trace ID;
- duración.

---

# Métricas operacionales

Ejemplos:

- sesiones;
- duración;
- errores operacionales;
- timeouts;
- retries;
- cache hit;
- colas;
- workers.

---

# Métricas de calidad

Ejemplos:

- diagnósticos;
- score;
- gates fallidos;
- deuda;
- regresiones;
- waivers;
- supresiones;
- cobertura.

---

# Métricas por familia

```text
structural_errors
identity_errors
reference_errors
semantic_errors
ontology_errors
security_errors
```

---

# Métricas de gates

- evaluaciones;
- aceptaciones;
- rechazos;
- bloqueos;
- revisiones manuales;
- tiempo hasta resolución.

---

# Métricas de remediación

- tiempo medio de corrección;
- diagnósticos reabiertos;
- auto-fixes propuestos;
- fixes aceptados;
- deuda vencida.

---

# Dashboards

Podrán mostrar:

- estado actual;
- evolución;
- score;
- áreas de riesgo;
- validadores más fallidos;
- deuda por módulo;
- gates;
- waivers;
- cobertura.

---

# Alertas

Ejemplos:

- gate crítico fallido;
- incremento de errores;
- regresión de score;
- validator caído;
- validación global incompleta;
- waiver próximo a expirar;
- supresión vencida;
- secretos detectados.

---

# SLOs

Podrán definirse objetivos como:

```text
95 % de validaciones locales < 2 s

99 % de gates de PR < 5 min

100 % de releases con validación completa
```

---

# SLA interno

Podrá existir para:

- revisión manual;
- resolución de diagnósticos críticos;
- reparación de validators;
- atención a incidentes.

---

# Seguridad

Los resultados de validación pueden contener información sensible.

---

# Permisos

Ejemplos:

```text
validation_execute
validation_read
validation_read_evidence
validation_manage_constraints
validation_manage_gates
validation_approve_waiver
validation_admin
```

---

# Separación entre informe y evidencia

Un usuario podrá ver el diagnóstico, pero no necesariamente la evidencia completa.

---

# Redacción

La evidencia sensible podrá ocultarse.

Ejemplo:

```yaml
evidence:
  redacted: true
  reason: restricted_source
```

---

# Datos personales

Los informes deberán minimizar:

- nombres;
- correos;
- direcciones;
- preferencias privadas;
- contenido personal.

---

# Secretos

Un diagnóstico de secreto no deberá incluir el secreto completo.

Deberá mostrar únicamente:

- tipo;
- localización;
- huella parcial;
- remediación.

---

# Seguridad de waivers

La aprobación de waivers deberá requerir permisos específicos.

---

# Auditoría de decisiones

Deberán auditarse:

- gate;
- waiver;
- revisión;
- aprobación;
- rechazo;
- cuarentena;
- cambio de política.

---

# Retención

Los informes deberán disponer de políticas de retención según:

- entorno;
- sensibilidad;
- tipo;
- auditoría;
- regulación.

---

# Firma y hash

Los informes críticos podrán:

- firmarse;
- hashearse;
- almacenarse de forma inmutable.

---

# Resiliencia

La evaluación de gates deberá poder continuar aunque fallen integraciones no críticas.

---

# Gate Engine no disponible

El Validation Report deberá conservarse.

La decisión quedará:

```text
blocked
```

hasta poder evaluar el gate.

---

# Reporting no disponible

La sesión podrá completarse y regenerar el informe posteriormente.

---

# Event Bus no disponible

Deberá utilizarse:

- outbox;
- reintento;
- persistencia.

---

# Fail-safe de decisiones

No deberá asumirse `accepted` por ausencia de respuesta.

---

# Pruebas de Quality Gates

Todo gate deberá disponer de pruebas.

---

# Caso de aceptación

Todos los criterios se cumplen.

---

# Caso de warning

Se permite continuar con advertencias.

---

# Caso de rechazo

Existe un criterio bloqueante.

---

# Caso de incompletitud

Falta un validator requerido.

---

# Caso de waiver

Un criterio queda cubierto legalmente.

---

# Caso de waiver expirado

El gate vuelve a fallar.

---

# Caso de revisión manual

La decisión depende de aprobación.

---

# Golden Gate Case

```yaml
golden_gate_case:
  id: GOLDEN-QG-0001

  gate: QG-PUBLICATION-0001

  input:
    critical_diagnostics: 0
    errors: 0
    warnings: 3
    validation_coverage: 1.0
    ontology_validation: passed

  expected:
    decision: accepted_with_warnings
```

---

# Pruebas de scoring

Deberán comprobar:

- pesos;
- redondeo;
- límites;
- dimensiones;
- penalizaciones;
- bloqueos no compensables.

---

# Pruebas de reporting

Deberán verificar:

- consistencia entre formatos;
- diagnósticos;
- evidencias;
- redacción;
- métricas;
- enlaces.

---

# Pruebas de CI/CD

Deberán comprobar:

- exit codes;
- baseline;
- diff;
- comentarios;
- bloqueo;
- reintentos;
- informes.

---

# Pruebas de integración

Deberán cubrir:

- Ingestion Engine;
- Knowledge Graph;
- Reasoner;
- GraphRAG;
- agentes;
- eventos;
- API.

---

# Pruebas de seguridad

Deberán verificar:

- permisos;
- redacción;
- aislamiento;
- waivers;
- secretos;
- datos personales.

---

# Perfil mínimo de Quality Gates e integración

La primera implementación podrá incluir:

- gate de repositorio;
- gate de Pull Request;
- gate de publicación;
- cero errores como criterio;
- warnings permitidos;
- salida CLI;
- informe Markdown;
- informe JSON;
- códigos de salida;
- integración CI;
- baseline sencillo.

---

# Perfil estructurado

Añadirá:

- score;
- quality regression;
- new issues policy;
- waivers;
- revisión manual;
- SARIF;
- API;
- eventos;
- dashboards.

---

# Perfil semántico

Añadirá:

- gates ontológicos;
- validación de Knowledge Graph;
- validación de inferencias;
- integración con colecciones;
- claims de GraphRAG.

---

# Perfil enterprise

Añadirá:

- políticas dinámicas;
- firma de informes;
- auditoría inmutable;
- múltiples aprobaciones;
- SLOs;
- dashboards completos;
- reporting ejecutivo;
- gates distribuidos;
- integración multiagente.

---

# Implementación inicial recomendada

La implementación inicial debería aprovechar el estado actual de NovaCoquinaria.

Flujo recomendado:

```text
python tools/validate_all.py
        ↓
Front Matter Validator
        ↓
Identifier Validator
        ↓
Internal Links Validator
        ↓
Validation Report
        ↓
Repository Quality Gate
        ↓
Stable Exit Code
```

---

# Gate inicial del repositorio

Criterios recomendados:

```yaml
quality_gate:
  id: QG-REPOSITORY-0001

  criteria:
    all:
      - front_matter_errors == 0
      - duplicate_ids == 0
      - broken_internal_links == 0
      - validator_operational_errors == 0

  decision:
    on_pass: accepted
    on_fail: rejected
    on_incomplete: blocked
```

---

# Salida esperada

```text
NovaCoquinaria - Validación
---------------------------

Front Matter: OK
Identificadores: OK
Enlaces internos: OK

Quality Gate: PASSED
Estado: OK
```

---

# Siguiente evolución

Posteriormente podrán añadirse:

- validación semántica;
- schemas por tipo documental;
- relaciones;
- ontología;
- colecciones;
- Quality Score;
- baseline de deuda;
- reportes estructurados.

---

# Caso de uso 1 — Pull Request válido

Resultados:

```text
0 errores
3 warnings
100 % de cobertura
```

Gate:

```text
accepted_with_warnings
```

El PR puede mergearse.

---

# Caso de uso 2 — Enlace interno roto

Resultado:

```text
1 error
```

Gate:

```text
rejected
```

El pipeline falla.

---

# Caso de uso 3 — Validator no ejecutado

El Ontology Validator no está disponible.

Perfil:

```text
publication
```

Resultado:

```text
blocked
```

No deberá asumirse aceptación.

---

# Caso de uso 4 — Deuda histórica

La rama principal contiene diez warnings conocidos.

El PR no añade nuevos warnings.

Política:

```text
new_issues_only
```

Resultado:

```text
accepted
```

La deuda existente continúa registrada.

---

# Caso de uso 5 — Waiver temporal

Una traducción pendiente posee waiver hasta una fecha.

El gate:

```text
conditionally_accepted
```

Cuando expire, volverá a bloquear.

---

# Caso de uso 6 — Publicación de Knowledge Package

El paquete supera:

- estructura;
- identidad;
- semántica;
- procedencia;
- seguridad.

Gate:

```text
accepted
```

El Ingestion Engine puede publicarlo.

---

# Caso de uso 7 — Inferencia sin explicación

La inferencia cumple sus premisas, pero no dispone de explicación.

El gate de materialización requiere explicabilidad.

Resultado:

```text
rejected
```

No se materializa.

---

# Caso de uso 8 — Respuesta GraphRAG no fundamentada

La respuesta contiene un claim sin soporte.

Gate de respuesta:

```text
rejected
```

El sistema deberá:

- regenerar;
- eliminar el claim;
- abstenerse.

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Reducir el gate a `errors == 0`

Puede ignorar:

- incompletitud;
- validators caídos;
- seguridad;
- cobertura;
- contexto.

---

## Confundir score alto con conformidad

Un crítico no puede compensarse.

---

## Permitir que warnings crezcan sin baseline

Genera deuda invisible.

---

## Waivers sin expiración

Convierten excepciones temporales en permanentes.

---

## Waivers globales

Deberán limitarse por target y criterio.

---

## Revisiones manuales sin auditoría

Impiden explicar la decisión.

---

## Gates distintos sin versionado

Producen resultados irreproducibles.

---

## Informes solo en logs

Los logs no sustituyen un artefacto estable.

---

## Exit codes inestables

Dificultan CI/CD.

---

## Publicar informes con secretos

Los diagnósticos deben redaccionarse.

---

## Aceptar ante fallo del Gate Engine

Debe utilizarse fail-closed cuando proceda.

---

## Aplicar fixes automáticamente durante la validación

Rompe la no destructividad.

---

## No revalidar después del fix

Puede dejar errores secundarios.

---

## Baseline sin identidad

La comparación debe referirse a un snapshot concreto.

---

## Ignorar cambios de score

Puede ocultar regresiones de calidad.

---

## Decorar PR con todos los diagnósticos históricos

Debe priorizar cambios nuevos.

---

## Permitir que agentes ignoren gates

Los gates constituyen contratos operativos.

---

## Exponer evidencia restringida en eventos

Debe aplicarse control de acceso.

---

## Tratar `blocked` como `failed`

Son decisiones distintas.

---

## Tratar `partial` como `passed`

La cobertura incompleta debe ser visible.

---

## Gates dependientes del orden de diagnósticos

La evaluación debe ser determinista.

---

# Reglas mínimas de conformidad

---

## Gate identificado

Todo gate deberá poseer identidad y versión.

---

## Política explícita

Deberá declarar criterios, thresholds y decisiones.

---

## Input trazable

Todo gate deberá enlazar con un Validation Report.

---

## Decisión tipada

No deberá devolver únicamente un booleano.

---

## Explicación

Toda decisión deberá incluir razones.

---

## Bloqueos no compensables

Los criterios críticos deberán declararse.

---

## Waivers gobernados

Deberán tener alcance, responsable y vigencia.

---

## Score versionado

Toda fórmula deberá identificar su versión.

---

## Informes persistentes

Los resultados deberán conservarse fuera de logs.

---

## Integración idempotente

Las llamadas y eventos deberán tolerar reintentos.

---

## Seguridad

Los informes deberán respetar sensibilidad y permisos.

---

## Auditoría

Toda decisión operativa deberá quedar registrada.

---

# Conformidad de Quality Gate

Un gate será conforme cuando:

- tenga identidad;
- esté versionado;
- declare target;
- defina criterios;
- defina política de incompletitud;
- defina decisiones;
- preserve trazabilidad;
- disponga de pruebas;
- tenga owner.

---

# Conformidad de resultado de gate

Será conforme cuando:

- identifique gate y versión;
- identifique informe;
- declare decisión;
- incluya razones;
- indique waivers;
- registre fecha;
- sea auditable.

---

# Conformidad de score

Será conforme cuando:

- utilice modelo versionado;
- declare dimensiones;
- declare pesos;
- no compense críticos;
- pueda reproducirse;
- disponga de tests.

---

# Conformidad de informe

Será conforme cuando:

- identifique sesión;
- incluya snapshot;
- declare cobertura;
- incluya diagnósticos;
- incluya gate;
- incluya métricas;
- preserve seguridad;
- pueda serializarse.

---

# Conformidad de integración CI/CD

Será conforme cuando:

- utilice exit codes estables;
- conserve informe;
- aplique baseline;
- diferencie errores nuevos;
- bloquee según política;
- sea reproducible.

---

# Conformidad de integración con Ingestion

Será conforme cuando:

- valide antes de publicar;
- devuelva decisión tipada;
- permita cuarentena;
- preserve diagnósticos;
- soporte reintento;
- no publique si el gate bloquea.

---

# Conformidad de integración con Reasoner

Será conforme cuando:

- valide reglas;
- valide premisas;
- valide inferencias;
- bloquee materialización insegura;
- conserve explicabilidad;
- preserve capas epistemológicas.

---

# Lista de comprobación

Antes de utilizar un resultado de validación para tomar una decisión deberá comprobarse:

```text
[ ] El Validation Report está completo.
[ ] El snapshot está identificado.
[ ] El Quality Gate está versionado.
[ ] Todos los criterios requeridos fueron evaluados.
[ ] Los validators obligatorios finalizaron.
[ ] Los errores operacionales están diferenciados.
[ ] Los diagnósticos suprimidos siguen auditados.
[ ] Los waivers son válidos y no han expirado.
[ ] Los criterios críticos no fueron compensados por score.
[ ] La decisión incluye una explicación.
[ ] Los permisos permiten acceder a la evidencia.
[ ] El resultado está registrado.
[ ] La integración consumidora respeta la decisión.
```

---

# Arquitectura de Quality Gates e integración

```text
┌───────────────────────────────────────────────┐
│              Validation Report               │
│                                               │
│ Results · Diagnostics · Coverage · Metrics    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Quality Model                   │
│                                               │
│ Score · Baseline · Regression · New Issues    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Quality Gates                   │
│                                               │
│ Criteria · Policies · Thresholds · Waivers    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            Operational Decision              │
│                                               │
│ Accept · Reject · Block · Quarantine · Review │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                 Integrations                  │
│                                               │
│ Ingestion · KG · Reasoner · CI/CD · GraphRAG  │
└───────────────────────────────────────────────┘
```

---

# Flujo completo

```text
Target
  ↓
Validation Request
  ↓
Validation Plan
  ↓
Validators
  ↓
Diagnostics
  ↓
Validation Report
  ↓
Quality Score
  ↓
Quality Gate
  ↓
Decision
  ↓
Publication / Rejection / Review
```

---

# Transición hacia la Parte VI

Esta quinta parte ha definido:

- el concepto de Quality Gate;
- los tipos y niveles de gates;
- los criterios;
- las políticas de bloqueo;
- las decisiones;
- los waivers;
- la revisión manual;
- el Quality Score;
- las dimensiones de calidad;
- las baselines;
- la detección de regresiones;
- la deuda nueva;
- los informes;
- los planes de remediación;
- las propuestas de fix;
- la integración con Ingestion Engine;
- la integración con Knowledge Graph;
- la integración con Reasoning Engine;
- la integración con Colecciones;
- la integración con GraphRAG y agentes;
- las APIs;
- los eventos;
- la integración con CI/CD;
- la observabilidad;
- la seguridad;
- las pruebas;
- los perfiles de capacidad;
- la implementación inicial recomendada.

La Parte VI completará la especificación del Validation Engine mediante:

- gobernanza de constraints;
- gobernanza de validators;
- gobernanza de profiles y gates;
- roles y responsabilidades;
- ciclo de vida;
- versionado;
- compatibilidad;
- deprecación;
- migraciones;
- pruebas y golden cases;
- deuda de validación;
- incidentes;
- métricas de madurez;
- niveles de conformidad;
- roadmap de implementación;
- arquitectura final.

---

# Conclusión

Los Quality Gates constituyen el punto en el que la validación deja de ser una actividad exclusivamente técnica y se convierte en una decisión operativa gobernada.

El Validation Engine detecta.

El Validation Report documenta.

El Quality Model mide.

El Quality Gate decide.

La integración ejecuta la decisión.

El ciclo puede resumirse así:

```text
Validar
   ↓
Medir
   ↓
Evaluar
   ↓
Decidir
   ↓
Actuar
```

La validación sin gate produce información, pero no controla el flujo.

El gate sin evidencia produce decisiones arbitrarias.

El scoring sin restricciones críticas puede ocultar riesgos.

Los waivers sin gobernanza generan deuda permanente.

Los informes sin trazabilidad impiden auditoría.

Las integraciones que ignoran el resultado destruyen el valor del sistema.

Por ello, NovaCoquinaria deberá garantizar que toda transición relevante —ingesta, publicación, merge, release, materialización inferencial o respuesta inteligente— utilice decisiones tipadas, explicables y versionadas.

Con esta quinta parte queda definido el puente entre la conformidad técnica y la operación real del SGCC.

La siguiente y última parte establecerá cómo gobernar, probar, mantener y evolucionar el Validation Engine de forma sostenible durante todo el ciclo de vida de NovaCoquinaria.

---

# Parte VI — Gobernanza, pruebas, deuda y evolución del Validation Engine

---

# Introducción

Las partes anteriores han definido:

- la misión y arquitectura del Validation Engine;
- el modelo formal de constraints, rules, validators y diagnostics;
- el pipeline de ejecución;
- la validación sintáctica, estructural, semántica y ontológica;
- los Quality Gates;
- el reporting;
- la integración con Ingestion Engine, Knowledge Graph, Reasoning Engine, GraphRAG, agentes y CI/CD.

Esta sexta y última parte establece cómo deberá gobernarse, mantenerse y evolucionar el Validation Engine durante todo el ciclo de vida de NovaCoquinaria.

Un sistema de validación no puede considerarse estable únicamente porque sus validadores funcionen correctamente en un momento determinado.

Las siguientes dimensiones también deberán gestionarse:

- propiedad;
- responsabilidad;
- versionado;
- compatibilidad;
- pruebas;
- cobertura;
- deuda;
- rendimiento;
- incidentes;
- seguridad;
- evolución;
- retirada;
- madurez.

Las reglas del SGCC evolucionarán.

La ontología cambiará.

Aparecerán nuevos tipos documentales.

Se incorporarán nuevos motores.

Las restricciones actuales podrán quedar obsoletas.

Por ello, cada componente del Validation Engine deberá tratarse como un artefacto gobernado y no como una comprobación técnica aislada.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir la gobernanza del Validation Engine;
- establecer roles y responsabilidades;
- formalizar el ciclo de vida de constraints;
- formalizar el ciclo de vida de validators;
- gobernar rulesets, perfiles y Quality Gates;
- definir versionado y compatibilidad;
- establecer políticas de deprecación y retirada;
- regular migraciones;
- definir la estrategia de pruebas;
- formalizar Golden Cases y regresión;
- establecer métricas de cobertura y calidad;
- definir la deuda de validación;
- regular incidentes y postmortems;
- establecer perfiles de conformidad;
- definir niveles de madurez;
- proponer el roadmap de implementación;
- consolidar la arquitectura final del Validation Engine.

---

# Principios de gobernanza

Toda evolución del Validation Engine deberá respetar los siguientes principios.

---

## Propiedad explícita

Todo artefacto estable deberá disponer de:

- owner;
- mantenedor;
- revisores;
- ámbito de responsabilidad.

---

## Responsabilidad separada

Quien implementa una validación no debería ser, necesariamente, quien aprueba su significado normativo.

---

## Trazabilidad de cambios

Toda modificación deberá indicar:

- qué cambió;
- por qué;
- quién lo propuso;
- quién lo aprobó;
- qué impacto produce;
- desde qué versión resulta efectiva.

---

## Compatibilidad evaluada

Ningún cambio deberá clasificarse como compatible de forma implícita.

---

## Pruebas obligatorias

Toda constraint, validator o gate estable deberá disponer de pruebas.

---

## Evolución gradual

Las reglas no deberán eliminarse sin:

- periodo de deprecación;
- alternativa;
- análisis de impacto;
- estrategia de migración.

---

## Independencia del runtime

La gobernanza deberá aplicarse al significado de la validación, no únicamente a su implementación concreta.

---

## Reproducibilidad histórica

Deberá ser posible reconstruir una validación antigua utilizando sus versiones originales o una representación archivada suficiente.

---

## Deuda visible

Los problemas conocidos no deberán ocultarse bajo supresiones indefinidas.

---

## Seguridad reforzada

Los cambios en validadores críticos deberán requerir controles superiores.

---

## Mejora continua

Las métricas deberán utilizarse para mejorar:

- precisión;
- cobertura;
- rendimiento;
- mantenibilidad;
- utilidad de los diagnósticos.

---

# Objetos gobernados

La gobernanza deberá abarcar, al menos:

```text
Constraints
Rules
Validators
Rulesets
Validation Profiles
Quality Gates
Quality Models
Diagnostic Codes
Remediation Rules
Waivers
Suppressions
Schemas
SHACL Shapes
Validation APIs
Validation Reports
Validator Plugins
```

---

# Gobernanza de Constraints

Una Constraint representa una obligación del modelo de conocimiento.

Por tanto, su significado deberá gobernarse como parte del conocimiento normativo del SGCC.

---

# Requisitos de una Constraint estable

Toda Constraint estable deberá disponer de:

- identificador;
- nombre;
- descripción;
- versión;
- categoría;
- target;
- alcance;
- severidad;
- owner;
- fundamento;
- documentación;
- implementación;
- pruebas;
- política de compatibilidad.

---

# Fundamentación

Toda Constraint deberá indicar su origen.

Ejemplos:

- especificación;
- ADR;
- ontología;
- política;
- norma;
- decisión editorial;
- requisito de seguridad;
- requisito legal.

---

# Constraint sin fundamento

Una Constraint sin fundamento explícito no deberá alcanzar el estado `active`.

---

# Owner de Constraint

El owner será responsable de:

- significado;
- evolución;
- revisión;
- deprecación;
- resolución de dudas.

---

# Implementación separada

Una Constraint podrá tener múltiples validators.

La sustitución de un validator no deberá cambiar automáticamente el significado de la Constraint.

---

# Ciclo de vida de una Constraint

Estados recomendados:

```text
proposed
draft
in_review
experimental
active
deprecated
retired
archived
rejected
```

---

# Proposed

La Constraint ha sido propuesta, pero aún no está formalizada.

---

# Draft

Su definición está en elaboración.

---

# InReview

Está siendo revisada por los roles correspondientes.

---

# Experimental

Puede ejecutarse en perfiles experimentales.

No deberá bloquear producción salvo política explícita.

---

# Active

Forma parte del modelo oficial de validación.

---

# Deprecated

Sigue disponible temporalmente, pero existe una alternativa o dejará de ser válida.

---

# Retired

Ya no debe utilizarse en nuevas validaciones.

---

# Archived

Se conserva únicamente por trazabilidad histórica.

---

# Rejected

La propuesta ha sido descartada.

---

# Transiciones de estado

```text
proposed
    ↓
draft
    ↓
in_review
    ├── rejected
    ├── experimental
    └── active
             ↓
        deprecated
             ↓
          retired
             ↓
          archived
```

---

# Aprobación de Constraint

La aprobación deberá verificar:

- necesidad;
- claridad;
- aplicabilidad;
- ausencia de duplicidad;
- severidad adecuada;
- implementación disponible;
- cobertura de pruebas;
- impacto;
- remediación.

---

# Constraint experimental

Deberá declarar:

- finalidad;
- duración;
- targets;
- métricas;
- criterio de promoción;
- criterio de retirada.

---

# Promoción a activa

Requerirá:

- pruebas suficientes;
- falsos positivos aceptables;
- documentación;
- owner;
- compatibilidad;
- aprobación.

---

# Gobernanza de Rules

La Rule describe cómo se comprueba una Constraint.

---

# Requisitos

Toda Rule estable deberá:

- enlazar con una Constraint;
- declarar lenguaje;
- ser validable;
- estar versionada;
- disponer de pruebas;
- ser independiente de entradas no declaradas.

---

# Cambio de Rule

Un cambio puede ser:

```text
implementation_only
behavior_preserving
behavior_extending
behavior_restricting
behavior_breaking
```

---

# Cambio de implementación

No altera el conjunto de targets aceptados o rechazados.

Ejemplo:

- optimización;
- refactor;
- sustitución de consulta;
- mejora de caché.

---

# Cambio de comportamiento

Altera los resultados.

Deberá analizarse como cambio semántico.

---

# Equivalencia de reglas

Cuando una Rule se traduzca entre:

- Python;
- SHACL;
- SPARQL;
- Java;
- DSL;

deberá demostrarse equivalencia mediante Golden Cases.

---

# Gobernanza de Validators

Un Validator es un componente ejecutable y deberá gobernarse como software operativo.

---

# Requisitos de un Validator estable

Deberá disponer de:

- identificador;
- versión;
- owner técnico;
- constraints soportadas;
- targets soportados;
- runtime;
- dependencias;
- límites;
- política de errores;
- pruebas;
- benchmarks;
- documentación;
- observabilidad.

---

# Estados de Validator

```text
draft
experimental
active
degraded
deprecated
disabled
retired
archived
```

---

# Validator degradado

Sigue disponible, pero:

- presenta limitaciones;
- utiliza un fallback;
- no cumple objetivos de rendimiento;
- tiene dependencias parcialmente disponibles.

---

# Validator deshabilitado

No puede ejecutarse.

Deberá indicarse:

- motivo;
- fecha;
- impacto;
- alternativa.

---

# Sustitución de Validator

Una nueva implementación deberá demostrar:

- equivalencia funcional;
- compatibilidad de diagnósticos;
- rendimiento aceptable;
- ausencia de regresiones;
- soporte de versiones.

---

# Validator crítico

Se considerarán críticos aquellos relacionados con:

- identidad;
- seguridad;
- privacidad;
- procedencia;
- publicación;
- integridad ontológica;
- alérgenos;
- toxicidad.

---

# Requisitos reforzados

Los Validators críticos deberán exigir:

- revisión adicional;
- pruebas exhaustivas;
- Golden Cases;
- mutación;
- auditoría;
- fail-closed;
- rollback;
- monitorización.

---

# Gobernanza de Rulesets

Un Ruleset agrupa Constraints y Rules coherentes.

---

# Requisitos

Todo Ruleset deberá declarar:

- identidad;
- versión;
- dominio;
- dependencias;
- constraints;
- compatibilidad;
- perfil de uso;
- owner;
- estado.

---

# Estados

```text
draft
experimental
active
deprecated
retired
archived
```

---

# Dependencias

Un Ruleset podrá depender de:

- otro Ruleset;
- versión de ontología;
- esquema;
- vocabulario;
- validator runtime;
- política.

---

# Matriz de compatibilidad

Ejemplo:

| Ruleset | Versión | Ontología compatible | Validator Runtime |
|---|---:|---|---|
| `RULESET-DOCUMENTS` | `1.4.0` | `>=2.0 <3.0` | `>=1.3` |
| `RULESET-ONTOLOGY` | `2.0.0` | `2.x` | `>=2.0` |

---

# Ruleset incompatible

No deberá activarse cuando no se cumplan sus dependencias.

---

# Ruleset parcial

No deberá presentarse como completamente ejecutado si falta alguna Constraint obligatoria.

---

# Gobernanza de perfiles

Los Validation Profiles determinan:

- Rulesets activos;
- severidades;
- cobertura;
- gates;
- política de fallo;
- reporting.

---

# Perfiles oficiales iniciales

```text
basic
standard
strict
publication
migration
experimental
security
audit
```

---

# Requisitos de un perfil

Todo perfil deberá declarar:

- objetivo;
- entorno;
- Rulesets;
- Constraints obligatorias;
- tolerancias;
- fail policy;
- Quality Gates;
- nivel de evidencia;
- límites.

---

# Perfil versionado

Los perfiles deberán versionarse.

Cambiar la lista de Validators obligatorios podrá ser incompatible.

---

# Herencia de perfiles

Un perfil podrá extender otro.

Ejemplo:

```text
publication
extends
strict
```

---

# Restricción de herencia

La extensión no deberá relajar silenciosamente controles críticos.

---

# Perfil personalizado

Podrá permitirse en desarrollo.

No deberá utilizarse en publicación canónica salvo registro y aprobación.

---

# Gobernanza de Quality Gates

Los Quality Gates representan decisiones operativas.

Por tanto, deberán gobernarse con especial rigor.

---

# Requisitos de un Gate estable

Deberá disponer de:

- identidad;
- versión;
- target;
- criterios;
- thresholds;
- decisiones;
- owner;
- pruebas;
- política de incompletitud;
- política de waiver;
- auditoría.

---

# Cambio de Gate

Un cambio será incompatible cuando:

- aumente o reduzca bloqueos;
- cambie thresholds;
- modifique precedencias;
- acepte nuevos waivers;
- cambie fail-open/fail-closed;
- altere la decisión para los mismos resultados.

---

# Gate crítico

Ejemplos:

- publicación;
- release;
- seguridad;
- identidad;
- migración;
- materialización de inferencias.

---

# Doble revisión

Los Gates críticos deberán requerir revisión:

- técnica;
- de gobernanza;
- de dominio cuando proceda.

---

# Gobernanza del Quality Model

Los modelos de scoring deberán:

- estar versionados;
- declarar fórmula;
- declarar pesos;
- declarar dimensiones;
- documentar penalizaciones;
- incluir pruebas;
- evitar compensación de críticos.

---

# Cambio de score

Una modificación de pesos podrá alterar tendencias históricas.

El informe deberá indicar el modelo utilizado.

---

# Recalcular histórico

Podrá recalcularse un score histórico con un modelo nuevo, pero deberá distinguirse entre:

```text
score_original
```

y:

```text
score_recalculated
```

---

# Gobernanza de códigos de diagnóstico

Los códigos de diagnóstico forman parte de los contratos externos.

---

# Requisitos

Todo código deberá:

- ser único;
- ser estable;
- tener descripción;
- asociarse a una Constraint;
- declarar severidad predeterminada;
- incluir remediación;
- estar versionado cuando cambie su significado.

---

# Formato recomendado

```text
<DOMINIO>_<PROBLEMA>
```

Ejemplos:

```text
DOCUMENT_MISSING_FRONT_MATTER
IDENTITY_DUPLICATE_ID
REFERENCE_BROKEN_INTERNAL_LINK
ONTOLOGY_INVALID_RANGE
SECURITY_SECRET_DETECTED
```

---

# Renombrado de código

Deberá conservar alias o mapeo de compatibilidad.

---

# Reutilización prohibida

Un código retirado no deberá reutilizarse para un significado distinto.

---

# Gobernanza de remediaciones

Las remediaciones deberán:

- ser seguras;
- ser claras;
- no ocultar el problema;
- distinguirse de auto-fixes;
- estar vinculadas con el diagnóstico.

---

# Remediación automática

Solo podrá proponerse cuando:

- la transformación sea determinista;
- no exista ambigüedad;
- pueda revertirse;
- esté probada;
- requiera confirmación cuando proceda.

---

# Gobernanza de supresiones

Las supresiones deberán ser excepcionales.

---

# Requisitos obligatorios

Toda supresión deberá incluir:

- identidad;
- target;
- Constraint;
- motivo;
- owner;
- fecha;
- expiración;
- ámbito;
- aprobación.

---

# Supresión sin expiración

No deberá permitirse salvo casos históricos expresamente aprobados.

---

# Supresión vencida

Deberá generar un diagnóstico específico.

Ejemplo:

```text
SUPPRESSION_EXPIRED
```

---

# Supresiones masivas

Deberán evitarse.

Cuando sean necesarias, deberán:

- limitarse;
- documentarse;
- auditarse;
- acompañarse de un plan de corrección.

---

# Gobernanza de Waivers

Un Waiver representa una excepción formalmente aceptada.

---

# Requisitos

Deberá incluir:

- Constraint;
- target;
- justificación;
- riesgo;
- aprobador;
- fecha;
- vigencia;
- controles compensatorios.

---

# Riesgo residual

Todo Waiver deberá declarar el riesgo que permanece.

---

# Controles compensatorios

Ejemplo:

```text
La traducción está ausente,
pero el documento no se publicará externamente.
```

---

# Waivers prohibidos

No deberán admitirse para:

- secretos;
- corrupción de identidad;
- pérdida de procedencia crítica;
- violaciones legales;
- permisos indebidos;
- integridad transaccional.

---

# Roles y responsabilidades

El Validation Engine deberá distinguir roles funcionales y técnicos.

---

# Validation Architect

Responsable de:

- arquitectura;
- metamodelo;
- principios;
- interoperabilidad;
- evolución global.

---

# Constraint Owner

Responsable del significado de una Constraint.

---

# Validator Maintainer

Responsable de:

- implementación;
- rendimiento;
- errores;
- mantenimiento;
- observabilidad.

---

# Ontology Maintainer

Responsable de:

- clases;
- propiedades;
- restricciones ontológicas;
- compatibilidad.

---

# Domain Expert

Valida el significado de dominio.

En NovaCoquinaria podrá incluir revisión:

- culinaria;
- alimentaria;
- documental;
- semántica.

---

# Quality Reviewer

Revisa:

- diagnósticos;
- severidades;
- gates;
- cobertura;
- deuda.

---

# Security Reviewer

Responsable de:

- validadores de seguridad;
- datos sensibles;
- secretos;
- permisos;
- privacidad.

---

# Platform Maintainer

Responsable de:

- runtime;
- ejecución;
- escalabilidad;
- disponibilidad;
- integración.

---

# Release Manager

Responsable de aplicar:

- gates de release;
- compatibilidad;
- informes;
- aprobación.

---

# Auditor

Puede revisar:

- sesiones;
- evidencias;
- decisiones;
- waivers;
- cambios;
- trazabilidad.

---

# Matriz RACI conceptual

| Actividad | Architect | Constraint Owner | Validator Maintainer | Reviewer | Release Manager |
|---|---|---|---|---|---|
| Crear Constraint | C | R | C | A | I |
| Implementar Validator | C | C | R/A | C | I |
| Cambiar severidad | C | R | C | A | I |
| Modificar Gate | R | C | C | A | C |
| Aprobar Waiver | C | C | I | R/A | I |
| Publicar Ruleset | C | R | R | A | C |
| Aprobar release | I | I | I | C | R/A |

Leyenda:

```text
R — Responsible
A — Accountable
C — Consulted
I — Informed
```

---

# Versionado

Todos los artefactos gobernados deberán versionarse.

---

# Semantic Versioning

Formato recomendado:

```text
MAJOR.MINOR.PATCH
```

---

# PATCH

Cambios sin impacto esperado en resultados.

Ejemplos:

- documentación;
- mensajes;
- rendimiento;
- observabilidad;
- correcciones internas equivalentes.

---

# MINOR

Cambios compatibles que amplían capacidad.

Ejemplos:

- nueva Constraint opcional;
- nuevo formato de informe;
- nueva remediación;
- nuevo target compatible;
- nuevo Validator alternativo.

---

# MAJOR

Cambios incompatibles.

Ejemplos:

- nuevos bloqueos obligatorios;
- cambio de semántica;
- eliminación de códigos;
- cambio de output;
- modificación de thresholds;
- cambio de fail policy.

---

# Versión de Constraint

Deberá cambiar cuando se modifique:

- condición;
- target;
- severidad normativa;
- ámbito;
- excepciones.

---

# Versión de Validator

Deberá cambiar cuando se modifique:

- implementación;
- dependencias;
- runtime;
- algoritmo;
- output;
- rendimiento contractual.

---

# Versión de Ruleset

Deberá cambiar cuando cambie:

- composición;
- dependencia;
- orden;
- obligatoriedad.

---

# Versión de perfil

Deberá cambiar cuando cambien:

- Rulesets;
- thresholds;
- política;
- gates;
- nivel de evidencia.

---

# Versión de Gate

Deberá cambiar cuando cambie cualquier criterio de decisión.

---

# Versión de diagnóstico

El código podrá mantenerse si el significado permanece estable.

Un cambio semántico deberá crear:

- nueva versión contractual;
- o nuevo código.

---

# Compatibilidad

Toda release deberá declarar compatibilidad entre:

- Validation Engine;
- Constraint Registry;
- Validator Registry;
- Ontología;
- schemas;
- APIs;
- report formats;
- Quality Gates.

---

# Tipos de compatibilidad

```text
fully_compatible
backward_compatible
forward_compatible
partially_compatible
incompatible
unknown
```

---

# Compatibilidad hacia atrás

Una versión nueva puede validar targets antiguos.

---

# Compatibilidad hacia delante

Una versión anterior puede procesar artefactos nuevos dentro de límites.

---

# Compatibilidad parcial

Algunas capacidades quedan disponibles y otras no.

Deberán declararse explícitamente.

---

# Matriz de compatibilidad

```yaml
compatibility:
  validation_engine: 1.5.0

  constraint_registry:
    supported: ">=1.4.0 <2.0.0"

  ontology:
    supported: ">=2.0.0 <3.0.0"

  report_schema:
    supported:
      - 1.0
      - 1.1
```

---

# Negociación de versión

Las APIs y runtimes podrán seleccionar una versión compatible.

No deberán elegir silenciosamente una implementación con semántica distinta.

---

# Cambio incompatible

Deberá requerir:

- release mayor;
- documentación;
- migración;
- análisis de impacto;
- regresión;
- rollback.

---

# Deprecación

La deprecación deberá ser gradual.

---

# Requisitos de deprecación

Todo artefacto deprecado deberá indicar:

- motivo;
- fecha;
- alternativa;
- versión final soportada;
- fecha prevista de retirada;
- impacto.

---

# Periodo de deprecación

Deberá existir un intervalo suficiente para:

- migrar consumidores;
- actualizar perfiles;
- corregir dependencias;
- recalcular baselines.

---

# Diagnóstico de deprecación

Podrá emitirse:

```text
VALIDATOR_DEPRECATED
CONSTRAINT_DEPRECATED
RULESET_DEPRECATED
```

---

# Retirada

Un artefacto retirado no deberá ejecutarse en nuevas sesiones.

Podrá conservarse para:

- reproducción histórica;
- auditoría;
- migraciones.

---

# Archivado

Los artefactos archivados deberán permanecer inmutables.

---

# Migraciones

Las migraciones deberán gestionar cambios en:

- schemas;
- Constraints;
- Validators;
- códigos;
- perfiles;
- Gates;
- reports;
- ontología.

---

# Plan de migración

Formato recomendado:

```text
VAL-MIGRATION-XXXXXX
```

---

# Contrato

```yaml
validation_migration:
  id: VAL-MIGRATION-000041

  from:
    constraint_registry: 1.4.0
    validator_registry: 1.3.0

  to:
    constraint_registry: 2.0.0
    validator_registry: 2.0.0

  impact:
    affected_constraints: 18
    affected_profiles: 3
    affected_gates: 2

  strategy:
    mode: staged

  rollback:
    supported: true
```

---

# Tipos de migración

---

## Migración de Constraint

Cambia el significado o contrato de validación.

---

## Migración de Validator

Cambia la implementación.

---

## Migración de diagnóstico

Transforma códigos o formatos.

---

## Migración de Ruleset

Reorganiza conjuntos de reglas.

---

## Migración de perfil

Modifica qué controles se ejecutan.

---

## Migración de Gate

Cambia decisiones operativas.

---

## Migración de baseline

Actualiza deuda o líneas de referencia.

---

# Estrategias de migración

```text
big_bang
staged
parallel_run
shadow
canary
dual_validation
```

---

# Parallel Run

Las versiones antigua y nueva se ejecutan simultáneamente.

Se comparan resultados antes de sustituir.

---

# Shadow Validation

La nueva versión se ejecuta sin afectar Gates.

Permite medir:

- divergencias;
- falsos positivos;
- rendimiento.

---

# Canary

Se aplica a un subconjunto limitado.

---

# Dual Validation

Ambas versiones producen decisiones visibles.

Adecuado para cambios críticos.

---

# Comparación de migración

Deberá analizarse:

- diagnósticos añadidos;
- diagnósticos eliminados;
- cambios de severidad;
- cambios de gate;
- cambios de score;
- rendimiento;
- cobertura.

---

# Rollback de migración

Deberá estar definido antes de activar la nueva versión.

---

# Pruebas

Las pruebas constituyen un requisito de conformidad.

---

# Pirámide de pruebas

```text
Unit Tests
      ↓
Contract Tests
      ↓
Integration Tests
      ↓
Golden Cases
      ↓
Regression Tests
      ↓
Mutation Tests
      ↓
Performance Tests
      ↓
Security Tests
      ↓
Acceptance Tests
```

---

# Pruebas unitarias

Validan:

- expresiones;
- operadores;
- mapeos;
- severidades;
- consolidación;
- scoring;
- gates.

---

# Pruebas de contrato

Comprueban compatibilidad entre:

- Constraint y Rule;
- Rule y Validator;
- Validator y Runtime;
- Report y consumidor;
- Gate y Validation Report;
- API y cliente.

---

# Pruebas de integración

Comprueban flujos completos.

Ejemplos:

```text
Documento
↓
Validation Engine
↓
Diagnostics
↓
Quality Gate
↓
CI
```

---

# Pruebas de sistema

Validan el motor completo en un entorno representativo.

---

# Pruebas de aceptación

Comprueban requisitos de negocio y gobernanza.

---

# Pruebas positivas

El target válido supera la Constraint.

---

# Pruebas negativas

El target inválido genera el diagnóstico esperado.

---

# Pruebas límite

Cubren valores extremos y fronteras.

---

# Pruebas de no aplicabilidad

Comprueban que una Constraint no se ejecute sobre targets incompatibles.

---

# Pruebas de error operacional

Comprueban que el motor distingue:

```text
failed
```

de:

```text
errored
```

---

# Pruebas de supresión

Comprueban:

- aplicación;
- alcance;
- expiración;
- auditoría.

---

# Pruebas de Waiver

Comprueban:

- aprobación;
- alcance;
- riesgo;
- expiración;
- Gate.

---

# Golden Cases

Los Golden Cases constituyen ejemplos de referencia estables.

---

# Identidad

Formato recomendado:

```text
GOLDEN-VAL-XXXXXX
```

---

# Contrato

```yaml
golden_case:
  id: GOLDEN-VAL-000041

  target:
    type: document
    fixture: fixtures/recipes/recipe-without-id.md

  profile: standard

  expected:
    status: failed

    diagnostics:
      - code: IDENTITY_MISSING_ID
        severity: error

    quality_gate:
      decision: rejected
```

---

# Requisitos de Golden Case

Deberá incluir:

- fixture;
- snapshot;
- perfil;
- resultado;
- diagnósticos;
- Gate;
- versión.

---

# Golden Cases por dominio

Deberán existir para:

- documentos;
- Front Matter;
- IDs;
- enlaces;
- componentes;
- relaciones;
- ontología;
- colecciones;
- seguridad;
- publicación.

---

# Golden Case positivo

Representa un target completamente conforme.

---

# Golden Case negativo

Representa un incumplimiento conocido.

---

# Golden Case múltiple

Incluye varios diagnósticos relacionados.

---

# Golden Case de regresión

Captura un fallo histórico para impedir su reaparición.

---

# Golden Case crítico

Deberá ser obligatorio para:

- seguridad;
- identidad;
- procedencia;
- ontología;
- Gate de publicación.

---

# Pruebas de regresión

Toda modificación deberá comparar resultados con una baseline.

---

# Tipos de regresión

- diagnóstico nuevo;
- diagnóstico ausente;
- cambio de severidad;
- cambio de localización;
- cambio de remediación;
- cambio de Gate;
- cambio de score;
- cambio de cobertura;
- cambio de rendimiento.

---

# Regresión esperada

Algunos cambios serán intencionales.

Deberán aprobarse y documentarse.

---

# Snapshot de regresión

```yaml
regression_snapshot:
  id: REG-VAL-000041

  validator_registry: 1.3.0
  constraint_registry: 1.4.0

  cases:
    total: 214
    passed: 214
```

---

# Pruebas de mutación

Las pruebas de mutación permiten comprobar si la suite detecta cambios defectuosos.

---

# Mutaciones posibles

- invertir operador;
- cambiar cardinalidad;
- eliminar condición;
- cambiar severidad;
- omitir dependencia;
- alterar threshold;
- desactivar fail-closed.

---

# Objetivo

Una suite madura deberá detectar la mayoría de mutaciones relevantes.

---

# Pruebas basadas en propiedades

Permiten comprobar invariantes.

Ejemplos:

```text
Toda Constraint activa tiene owner.
```

```text
Todo diagnóstico referencia una Constraint.
```

```text
Ningún Gate crítico acepta una violación critical.
```

```text
Una supresión expirada no altera el Gate.
```

```text
El orden de ejecución no cambia el resultado agregado.
```

---

# Fuzzing

Podrá utilizarse para:

- parsers;
- schemas;
- expresiones;
- APIs;
- plugins;
- formatos.

---

# Pruebas de rendimiento

Deberán medir:

- latencia;
- throughput;
- memoria;
- CPU;
- tamaño de report;
- escalabilidad;
- caché.

---

# Benchmarks

Formato recomendado:

```text
BENCH-VAL-XXXXXX
```

---

# Dimensiones

- documentos por segundo;
- relaciones por segundo;
- validators por sesión;
- diagnósticos por segundo;
- latencia p50;
- latencia p95;
- latencia p99;
- consumo de memoria;
- hit rate de caché.

---

# Baseline de rendimiento

Toda versión estable deberá compararse con una baseline.

---

# Regresión de rendimiento

Podrá bloquear cuando supere el umbral permitido.

Ejemplo:

```yaml
performance_gate:
  maximum_p95_regression: 10%
```

---

# Pruebas de carga

Deberán incluir:

- miles de documentos;
- múltiples sesiones;
- validación global;
- validación incremental;
- alta cardinalidad de diagnósticos.

---

# Pruebas de estrés

Evaluarán:

- saturación;
- backpressure;
- degradación;
- recuperación;
- límites.

---

# Pruebas de resiliencia

Deberán simular:

- caída de validator;
- caída de registro;
- timeout;
- caché no disponible;
- cola saturada;
- pérdida temporal de ontología;
- fallo de reporting.

---

# Pruebas de seguridad

Deberán cubrir:

- permisos;
- aislamiento;
- secrets;
- redacción;
- inyección;
- traversal;
- deserialización;
- plugins;
- acceso a evidencia.

---

# Cobertura

La cobertura deberá medirse en varias dimensiones.

---

# Cobertura de Constraints

Porcentaje de Constraints con implementación ejecutable.

---

# Cobertura de pruebas

Porcentaje de:

- Constraints;
- Rules;
- Validators;
- Gates;
- códigos;
- remediaciones

cubiertos por pruebas.

---

# Cobertura de targets

Tipos de artefacto soportados.

---

# Cobertura semántica

Porcentaje de conceptos relevantes protegidos por restricciones.

---

# Cobertura de riesgos

Riesgos críticos cubiertos por validadores y Gates.

---

# Cobertura de diagnósticos

Códigos que disponen de:

- prueba;
- mensaje;
- evidencia;
- remediación.

---

# Cobertura de perfiles

Qué porcentaje de Constraints activas se ejecuta en cada perfil.

---

# Contrato de cobertura

```yaml
validation_coverage:
  constraints:
    total: 180
    implemented: 162
    tested: 154

  validators:
    total: 42
    tested: 42

  gates:
    total: 8
    tested: 8

  critical_constraints:
    total: 24
    tested: 24
```

---

# Umbrales

Los umbrales podrán variar por criticidad.

Ejemplo:

```text
Constraints críticas: 100 %
Constraints estándar: ≥ 90 %
Constraints experimentales: ≥ 70 %
```

---

# Falsos positivos

Un falso positivo ocurre cuando el sistema genera un diagnóstico incorrecto.

---

# Falsos negativos

Un falso negativo ocurre cuando no detecta un incumplimiento real.

---

# Medición

Deberán registrarse:

- tasa;
- categoría;
- validator;
- Constraint;
- severidad;
- impacto.

---

# Prioridad

Los falsos negativos críticos deberán considerarse de máxima prioridad.

---

# Precisión de diagnósticos

Podrá evaluarse mediante:

```text
precision
recall
false_positive_rate
false_negative_rate
```

especialmente para validadores probabilísticos.

---

# Calidad de remediación

También deberá evaluarse:

- claridad;
- aplicabilidad;
- corrección;
- utilidad;
- tasa de resolución.

---

# Deuda de validación

La deuda de validación representa insuficiencias conocidas del sistema.

---

# Tipos de deuda

---

## Deuda de cobertura

Existen áreas sin restricciones suficientes.

---

## Deuda de implementación

La Constraint está definida, pero no tiene Validator.

---

## Deuda de pruebas

El Validator carece de cobertura adecuada.

---

## Deuda de rendimiento

El Validator es demasiado costoso.

---

## Deuda de compatibilidad

Depende de versiones obsoletas.

---

## Deuda de diagnóstico

Los mensajes son ambiguos o poco útiles.

---

## Deuda de supresión

Existen demasiadas supresiones.

---

## Deuda de waiver

Existen excepciones prolongadas o repetidas.

---

## Deuda ontológica

La validación no cubre correctamente el modelo semántico.

---

## Deuda operacional

Existen fallos de observabilidad, resiliencia o despliegue.

---

# Registro de deuda

Formato recomendado:

```text
VAL-DEBT-XXXXXX
```

---

# Contrato

```yaml
validation_debt:
  id: VAL-DEBT-000041

  type: missing_validator

  target:
    constraint: CONSTRAINT-ONTOLOGY-0041

  severity: high

  description: >
    La Constraint de ciclos ontológicos todavía no dispone
    de implementación incremental.

  owner: validation_team

  planned_resolution:
    release: 1.6.0
```

---

# Estados de deuda

```text
identified
accepted
planned
in_progress
mitigated
resolved
cancelled
```

---

# Deuda aceptada

Deberá incluir:

- justificación;
- riesgo;
- controles compensatorios;
- fecha de revisión.

---

# Priorización de deuda

Podrá calcularse mediante:

```text
Impacto
×
Probabilidad
×
Exposición
×
Coste de demora
```

---

# Indicadores de deuda

Ejemplos:

- Constraints sin Validator;
- Validators sin pruebas;
- supresiones activas;
- waivers vencidos;
- códigos sin remediación;
- Validators deprecados;
- Gates sin owner;
- perfiles incompatibles;
- deuda crítica abierta.

---

# Presupuesto de deuda

Podrán fijarse límites.

Ejemplo:

```yaml
validation_debt_budget:
  critical: 0
  high: 5
  medium: 20
```

---

# Gate de deuda

Una release podrá bloquearse si supera el presupuesto.

---

# Backlog de validación

La deuda deberá integrarse en:

- roadmap;
- BITÁCORA;
- KNOWN_ISSUES;
- planificación;
- releases.

---

# Incidentes

Un incidente de validación ocurre cuando el sistema:

- acepta conocimiento inválido;
- rechaza conocimiento válido de forma significativa;
- no ejecuta controles críticos;
- produce decisiones incorrectas;
- pierde trazabilidad;
- expone evidencia sensible;
- bloquea el pipeline indebidamente.

---

# Identidad de incidente

Formato recomendado:

```text
INC-VAL-XXXXXX
```

---

# Categorías

```text
false_negative
false_positive
validator_failure
gate_failure
security
compatibility
performance
data_loss
reporting
availability
governance
```

---

# Severidad de incidente

```text
SEV-1
SEV-2
SEV-3
SEV-4
```

---

# SEV-1

Impacto crítico.

Ejemplos:

- publicación insegura;
- secreto expuesto;
- corrupción de identidad;
- Gate crítico eludido.

---

# SEV-2

Impacto alto.

Ejemplos:

- validación global no disponible;
- alta tasa de falsos negativos;
- release incorrectamente aceptada.

---

# SEV-3

Impacto moderado.

---

# SEV-4

Impacto menor.

---

# Ciclo de incidente

```text
detected
↓
triaged
↓
contained
↓
mitigated
↓
resolved
↓
reviewed
↓
closed
```

---

# Contención

Podrá incluir:

- deshabilitar Validator;
- activar fallback;
- bloquear Gate;
- revertir versión;
- poner targets en cuarentena;
- invalidar reports.

---

# Informe de incidente

```yaml
validation_incident:
  id: INC-VAL-000041

  severity: SEV-2
  category: false_negative

  affected:
    validator: VALIDATOR-INTERNAL-LINKS
    version: 2.1.0

  impact:
    affected_documents: 18
    affected_releases:
      - 1.5.0

  status: resolved
```

---

# Postmortem

Los incidentes relevantes deberán producir un postmortem.

---

# Contenido mínimo

- resumen;
- impacto;
- cronología;
- causa raíz;
- factores contribuyentes;
- detección;
- resolución;
- acciones correctivas;
- acciones preventivas;
- owner;
- seguimiento.

---

# Blameless Postmortem

El análisis deberá centrarse en:

- sistema;
- proceso;
- controles;
- diseño;

y no en culpabilizar personas.

---

# Acciones preventivas

Podrán incluir:

- Golden Case;
- nueva Constraint;
- nueva alerta;
- cambio de Gate;
- mejora de observabilidad;
- cambio de proceso;
- actualización de documentación.

---

# Métricas de gobernanza

Ejemplos:

- Constraints activas;
- Constraints deprecadas;
- Validators activos;
- Validators sin owner;
- Rulesets incompatibles;
- perfiles;
- Gates;
- waivers;
- supresiones;
- deuda;
- incidentes.

---

# Métricas de calidad

- cobertura;
- precisión;
- recall;
- falsos positivos;
- falsos negativos;
- diagnósticos por target;
- tiempo de resolución;
- calidad de remediación.

---

# Métricas operacionales

- latencia;
- disponibilidad;
- throughput;
- error rate;
- timeout;
- cache hit;
- reintentos;
- sesiones parciales.

---

# Métricas de evolución

- cambios por release;
- migraciones;
- deprecaciones;
- adopción de versiones;
- tiempo de transición;
- divergencias entre runtimes.

---

# KPIs recomendados

Ejemplos:

```text
100 % de Constraints críticas con pruebas

100 % de Gates críticos versionados

0 Validators activos sin owner

0 waivers críticos vencidos

0 falsos negativos críticos conocidos

≥ 95 % de sesiones locales bajo el SLO

≥ 90 % de cobertura de Constraints activas
```

---

# Observabilidad de gobernanza

Los dashboards deberán permitir identificar:

- deuda creciente;
- Validators inestables;
- Gates demasiado permisivos;
- exceso de supresiones;
- pérdida de cobertura;
- regresión de rendimiento;
- Rulesets obsoletos.

---

# Revisiones periódicas

Se recomienda:

```text
Revisión continua
```

para incidentes y métricas.

```text
Revisión mensual
```

para deuda y supresiones.

```text
Revisión por release
```

para compatibilidad y Gates.

```text
Revisión anual
```

para arquitectura y madurez.

---

# Conformidad

La conformidad del Validation Engine podrá evaluarse mediante perfiles.

---

# Perfil de conformidad mínimo

Una implementación mínima será conforme cuando:

- ejecute validadores deterministas;
- produzca diagnósticos estructurados;
- preserve evidencia;
- genere informes;
- distinga fallo y error operacional;
- disponga de Quality Gate;
- mantenga versionado básico;
- disponga de pruebas.

---

# Perfil de conformidad estructurado

Añadirá:

- registries;
- perfiles;
- incrementalidad;
- baseline;
- CI/CD;
- waivers;
- auditoría;
- Golden Cases.

---

# Perfil de conformidad semántico

Añadirá:

- validación ontológica;
- SHACL;
- Knowledge Graph;
- reglas;
- inferencias;
- colecciones;
- análisis de impacto.

---

# Perfil de conformidad enterprise

Añadirá:

- ejecución distribuida;
- alta disponibilidad;
- seguridad avanzada;
- auditoría inmutable;
- múltiples aprobaciones;
- SLOs;
- reporting ejecutivo;
- gestión formal de incidentes;
- migraciones complejas.

---

# Conformidad de una Constraint

Una Constraint será conforme cuando:

- tenga identidad;
- esté versionada;
- tenga owner;
- declare target;
- declare fundamento;
- disponga de Rule;
- disponga de Validator o estado de deuda;
- tenga pruebas;
- tenga diagnóstico;
- tenga remediación.

---

# Conformidad de un Validator

Será conforme cuando:

- esté registrado;
- esté versionado;
- declare capacidades;
- tenga owner;
- implemente Constraints identificadas;
- disponga de pruebas;
- tenga política de error;
- sea observable;
- respete seguridad.

---

# Conformidad de Ruleset

Será conforme cuando:

- tenga identidad;
- esté versionado;
- declare composición;
- declare dependencias;
- sea compatible;
- disponga de pruebas;
- tenga owner.

---

# Conformidad de perfil

Será conforme cuando:

- tenga objetivo;
- declare Rulesets;
- declare Gates;
- declare tolerancias;
- declare fail policy;
- esté versionado;
- disponga de pruebas.

---

# Conformidad de Gate

Será conforme cuando:

- tenga identidad;
- versión;
- criterios;
- decisiones;
- owner;
- política de waiver;
- pruebas;
- auditoría.

---

# Conformidad del sistema

El Validation Engine será conforme cuando:

- mantenga separación de responsabilidades;
- preserve reproducibilidad;
- produzca decisiones explicables;
- gestione compatibilidad;
- disponga de pruebas;
- gestione deuda;
- registre incidentes;
- aplique seguridad;
- permita evolución controlada.

---

# Modelo de madurez

Se propone el siguiente modelo.

```text
VAL-M0 — Ad hoc

VAL-M1 — Básico

VAL-M2 — Estructurado

VAL-M3 — Semántico

VAL-M4 — Operacional

VAL-M5 — Adaptativo
```

---

# VAL-M0 — Ad hoc

Características:

- scripts aislados;
- resultados en consola;
- reglas implícitas;
- poca trazabilidad;
- ejecución manual.

---

# VAL-M1 — Básico

Características:

- validadores identificados;
- diagnósticos;
- exit codes;
- informes básicos;
- CI inicial.

Estado aproximado del repositorio actual:

```text
validate_front_matter
validate_ids
validate_links
validate_all
```

---

# VAL-M2 — Estructurado

Características:

- Constraint Registry;
- Validator Registry;
- perfiles;
- Validation Report;
- Quality Gates;
- incrementalidad;
- pruebas formales.

---

# VAL-M3 — Semántico

Características:

- ontología;
- relaciones;
- SHACL;
- colecciones;
- Knowledge Packages;
- Knowledge Graph;
- procedencia.

---

# VAL-M4 — Operacional

Características:

- servicio independiente;
- APIs;
- eventos;
- ejecución asíncrona;
- observabilidad;
- SLOs;
- HA;
- seguridad avanzada.

---

# VAL-M5 — Adaptativo

Características:

- optimización automática;
- selección adaptativa;
- análisis predictivo;
- detección de anomalías;
- validación continua;
- asistencia inteligente;
- actualización gobernada de reglas.

Los modelos adaptativos no deberán modificar Constraints normativas sin aprobación.

---

# Roadmap de implementación

El roadmap deberá evolucionar desde las herramientas actuales sin introducir complejidad innecesaria.

---

# Fase 0 — Consolidación de validadores actuales

Objetivo:

```text
Estabilizar validate_all.py
```

Acciones:

- normalizar resultados;
- definir códigos;
- diferenciar warning y error;
- corregir excepciones no controladas;
- mantener salida legible;
- añadir tests.

---

# Fase 1 — Diagnósticos estructurados

Objetivo:

```text
Convertir errores de consola en objetos Diagnostic
```

Acciones:

- identificadores;
- códigos;
- severidades;
- target;
- evidencia;
- remediación;
- salida JSON.

---

# Fase 2 — Validation Report

Objetivo:

```text
Generar un informe consolidado
```

Acciones:

- sesiones;
- tiempos;
- cobertura;
- métricas;
- Markdown;
- JSON;
- exit codes estables.

---

# Fase 3 — Constraint y Validator Registry

Objetivo:

```text
Separar la definición normativa de la implementación
```

Acciones:

- catálogo de Constraints;
- catálogo de Validators;
- versiones;
- owners;
- perfiles;
- compatibilidad.

---

# Fase 4 — Validación incremental

Objetivo:

```text
Validar cambios y dependencias
```

Acciones:

- `git diff`;
- Change Set;
- Impact Analyzer;
- caché;
- dependencias;
- selección de targets.

---

# Fase 5 — Quality Gates

Objetivo:

```text
Convertir informes en decisiones operativas
```

Acciones:

- Gate de repositorio;
- Gate de PR;
- Gate de release;
- baseline;
- new issues policy;
- waivers.

---

# Fase 6 — Validación semántica

Objetivo:

```text
Validar el modelo documental y relacional
```

Acciones:

- schemas;
- tipos documentales;
- relaciones;
- componentes;
- cardinalidades;
- colecciones.

---

# Fase 7 — Validación ontológica

Objetivo:

```text
Alinear validación y ontología
```

Acciones:

- clases;
- dominio;
- rango;
- disjunciones;
- SHACL;
- consistencia global.

---

# Fase 8 — Integración con Knowledge Graph

Objetivo:

```text
Validar planes, snapshots y subgrafos
```

Acciones:

- Graph Plan;
- post-publication validation;
- procedencia;
- identidad;
- dependencias;
- snapshots.

---

# Fase 9 — Servicio de validación

Objetivo:

```text
Exponer el Validation Engine como servicio
```

Acciones:

- API;
- jobs;
- eventos;
- auditoría;
- seguridad;
- observabilidad.

---

# Fase 10 — Validación inteligente

Objetivo:

```text
Incorporar capacidades asistidas
```

Acciones:

- anomalías;
- clasificación;
- calidad lingüística;
- sugerencias;
- remediación asistida;
- detección de duplicados.

Los resultados probabilísticos deberán mantenerse separados de las Constraints deterministas.

---

# Priorización recomendada

Para la release `v1.5.0 — Knowledge Engine`, la implementación documental podrá considerar como objetivo:

```text
Fase 0
+
Fase 1
+
Fase 2
+
Diseño de Fase 3
```

No será necesario implementar inmediatamente:

- servicio distribuido;
- SHACL completo;
- validación continua;
- IA;
- ejecución multiagente;
- autoscaling.

---

# Arquitectura final del Validation Engine

```text
┌───────────────────────────────────────────────┐
│                Knowledge Targets              │
│                                               │
│ Documents · Packages · KG · Rules · Agents    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Validation Request               │
│                                               │
│ Scope · Profile · Snapshot · Permissions      │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Governance Layer                │
│                                               │
│ Constraints · Rulesets · Profiles · Versions  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                Planning Layer                 │
│                                               │
│ Targets · Dependencies · Validators · Impact  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Validation Runtime              │
│                                               │
│ Execute · Cache · Retry · Parallelism          │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            Diagnostic and Evidence Layer      │
│                                               │
│ Diagnostics · Evidence · Suppressions · Fixes │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            Quality Decision Layer             │
│                                               │
│ Score · Baseline · Gates · Reviews · Waivers  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Integration Layer               │
│                                               │
│ Ingestion · KG · Reasoner · CI/CD · GraphRAG  │
└───────────────────────────────────────────────┘
```

---

# Relación con el Knowledge Engine

El Validation Engine actúa de forma transversal.

```text
                   Validation Engine
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
 Ingestion Engine   Knowledge Graph   Reasoning Engine
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                    Quality Gates
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
      CI/CD            GraphRAG           Agents
```

---

# Relación con las especificaciones existentes

| Documento | Relación |
|---|---|
| `ESPECIFICACION_DE_DOCUMENTOS.md` | Define contratos documentales |
| `ESPECIFICACION_DE_COMPONENTES.md` | Define componentes validables |
| `ESPECIFICACION_DE_RELACIONES.md` | Define relaciones y restricciones |
| `ESPECIFICACION_DE_ONTOLOGIAS.md` | Define clases, propiedades y axiomas |
| `ESPECIFICACION_DE_COLECCIONES.md` | Define coherencia y membresía |
| `ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md` | Define integridad global y snapshots |
| `ESPECIFICACION_DEL_RAZONADOR.md` | Define reglas e inferencias validables |
| `ESPECIFICACION_DE_INGESTA.md` | Produce Knowledge Packages candidatos |
| `ESPECIFICACION_DEL_MOTOR_RAG.md` | Consumirá validación de contexto y claims |
| `ESPECIFICACION_DE_APIS.md` | Expondrá servicios de validación |

---

# Futuras especificaciones derivadas

A partir de este documento podrán desarrollarse:

- `ESPECIFICACION_DE_CONSTRAINTS.md`
- `ESPECIFICACION_DE_VALIDATORS.md`
- `ESPECIFICACION_DE_QUALITY_GATES.md`
- `ESPECIFICACION_DE_DIAGNOSTICOS.md`
- `ESPECIFICACION_DE_SHACL.md`
- `ESPECIFICACION_DE_VALIDACION_CONTINUA.md`
- `ESPECIFICACION_DE_REPORTING_DE_CALIDAD.md`
- `ESPECIFICACION_DE_DEUDA_DE_CONOCIMIENTO.md`

Estas especificaciones deberán heredar los principios definidos aquí.

---

# Estado de madurez del documento

| Área | Estado |
|---|---|
| Fundamentos | Completo |
| Arquitectura | Completa |
| Modelo de Constraints | Completo |
| Modelo de Validators | Completo |
| Diagnósticos y evidencias | Completo |
| Pipeline de ejecución | Completo |
| Familias de validación | Completo |
| Quality Gates | Completo |
| Reporting | Completo |
| Integración | Completa |
| Gobernanza | Completa |
| Pruebas | Completa |
| Deuda e incidentes | Completo |
| Roadmap | Completo |

---

# Lista de comprobación final

Antes de considerar conforme una implementación del Validation Engine deberá verificarse:

```text
[ ] Las Constraints poseen identidad, versión y owner.
[ ] Las Rules enlazan con Constraints.
[ ] Los Validators están registrados y probados.
[ ] Los Rulesets declaran dependencias.
[ ] Los perfiles están versionados.
[ ] Los diagnósticos poseen códigos estables.
[ ] Las evidencias conservan trazabilidad.
[ ] Las supresiones tienen expiración.
[ ] Los Waivers están aprobados y auditados.
[ ] Los Quality Gates poseen pruebas.
[ ] Los informes son reproducibles.
[ ] La compatibilidad está declarada.
[ ] Las deprecaciones indican alternativa.
[ ] Las migraciones poseen rollback.
[ ] Los Golden Cases cubren controles críticos.
[ ] Las regresiones son detectables.
[ ] La deuda está registrada.
[ ] Los incidentes generan acciones preventivas.
[ ] Las métricas permiten evaluar calidad y rendimiento.
[ ] La integración con CI/CD respeta las decisiones.
[ ] La seguridad protege diagnósticos y evidencias.
```

---

# Antipatrones de gobernanza

Deberán evitarse los siguientes antipatrones.

---

## Constraints sin owner

Terminan sin mantenimiento ni criterio de evolución.

---

## Validator confundido con Constraint

Acopla significado e implementación.

---

## Cambios de severidad sin versión

Alteran Gates de forma silenciosa.

---

## Gates modificados directamente en CI

Las políticas deberán residir en artefactos gobernados.

---

## Supresiones permanentes

Ocultan deuda.

---

## Waivers sin riesgo residual

Impiden evaluar el impacto aceptado.

---

## Diagnósticos sin códigos estables

Dificultan integración y seguimiento.

---

## Tests únicamente positivos

No comprueban la capacidad de detectar errores.

---

## Golden Cases actualizados automáticamente

Pueden aceptar regresiones sin revisión.

---

## Baselines regeneradas sin análisis

Ocultan nueva deuda.

---

## Migraciones sin ejecución paralela en cambios críticos

Incrementan el riesgo.

---

## Deuda no registrada

Convierte limitaciones conocidas en sorpresas.

---

## Incidentes sin postmortem

Favorecen la repetición.

---

## Métricas sin decisiones asociadas

Generan observabilidad sin mejora.

---

## Plugins sin gobernanza

Introducen comportamiento no controlado.

---

## Rulesets globales monolíticos

Dificultan evolución e incrementalidad.

---

## Versionar únicamente el motor

Los Constraints y Gates también alteran resultados.

---

## Retirar Validators sin conservar reproducibilidad

Impide auditar validaciones históricas.

---

## Utilizar IA para modificar reglas normativas

Toda modificación normativa deberá revisarse y aprobarse.

---

# Transición hacia la siguiente especificación

Con esta sexta parte queda finalizada la especificación del Validation Engine.

El sistema dispone ahora de una definición formal para:

- declarar Constraints;
- implementar Validators;
- ejecutar validaciones;
- consolidar diagnósticos;
- aplicar Quality Gates;
- producir informes;
- gobernar versiones;
- gestionar deuda;
- medir calidad;
- evolucionar de forma segura.

La siguiente especificación natural dentro de la release `v1.5.0 — Knowledge Engine` será:

```text
ESPECIFICACION_DEL_MOTOR_RAG.md
```

Este documento deberá definir cómo el sistema recupera y construye contexto utilizando:

- documentos;
- componentes;
- colecciones;
- Knowledge Graph;
- inferencias;
- embeddings;
- índices;
- validaciones;
- procedencia;
- restricciones.

---

# Conclusión

El Validation Engine constituye el sistema central de aseguramiento de calidad del conocimiento de NovaCoquinaria.

Su misión no consiste únicamente en detectar errores.

Debe garantizar que cada decisión de conformidad sea:

- explícita;
- reproducible;
- trazable;
- explicable;
- versionada;
- gobernada.

La arquitectura completa puede resumirse así:

```text
Definir Constraint
        ↓
Implementar Validator
        ↓
Seleccionar Profile
        ↓
Planificar Validation
        ↓
Ejecutar
        ↓
Generar Diagnostics
        ↓
Construir Report
        ↓
Evaluar Quality Gate
        ↓
Tomar Decision
        ↓
Auditar y evolucionar
```

Las Constraints expresan lo que debe cumplirse.

Las Rules formalizan cómo comprobarlo.

Los Validators ejecutan las comprobaciones.

Los Diagnostics explican los incumplimientos.

Los Reports conservan los resultados.

Los Quality Gates transforman evidencia en decisiones.

La gobernanza garantiza que todo este sistema pueda evolucionar sin perder coherencia.

Con esta sexta parte queda completada la **Especificación del Validation Engine**, uno de los componentes transversales fundamentales del Knowledge Engine de NovaCoquinaria y la base sobre la que podrán apoyarse de forma segura la ingesta, el Knowledge Graph, el Razonador, GraphRAG, los agentes y los futuros servicios inteligentes del SGCC.

