---
id: SPEC-RAZONADOR
tipo: especificacion
titulo: Especificación del Razonador
version: 1.0.0
estado: borrador
ultima_revision: 2026-08-02
tags:
  - reasoning
  - inference
  - rules
  - statements
  - architecture
---

# ESPECIFICACIÓN DEL RAZONADOR

> Proyecto: NovaCoquinaria
>
> Sistema: GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)
>
> Release objetivo: v1.5.0 — Knowledge Engine

---

# Parte I — Fundamentos y arquitectura del razonador

---

# Introducción

Las especificaciones anteriores han definido la arquitectura formal del conocimiento de NovaCoquinaria:

```text
Documentos
      ↓
Componentes
      ↓
Relaciones
      ↓
Ontología
      ↓
Knowledge Graph
      ↓
Colecciones de Conocimiento
```

Estas capas permiten:

- representar conocimiento;
- identificar entidades;
- describir relaciones;
- definir significado;
- conservar procedencia;
- contextualizar afirmaciones;
- organizar dominios;
- consultar conocimiento conectado.

Sin embargo, representar conocimiento no equivale a utilizarlo de forma activa.

El SGCC necesita una capacidad capaz de interpretar hechos, aplicar reglas, validar restricciones, derivar conclusiones y explicar por qué una determinada respuesta puede considerarse válida.

Esa capacidad es el **Razonador**.

El Razonador constituye el núcleo lógico del **Knowledge Engine** de NovaCoquinaria.

Su responsabilidad consiste en transformar conocimiento estructurado en conclusiones:

- reproducibles;
- trazables;
- contextualizadas;
- explicables;
- gobernadas.

---

# Propósito de la especificación

La presente especificación define la arquitectura oficial del Razonador del SGCC.

Su propósito es establecer:

- qué es el Razonador;
- qué responsabilidades posee;
- qué límites deberá respetar;
- cómo se relaciona con el resto del sistema;
- qué tipos de razonamiento podrá ejecutar;
- cómo deberá estructurarse internamente;
- qué principios regirán su comportamiento;
- cómo evolucionará desde una implementación mínima hasta un motor avanzado.

Esta primera parte se centra en los fundamentos y en la arquitectura conceptual.

Las partes siguientes formalizarán:

- hechos;
- reglas;
- premisas;
- conclusiones;
- inferencias;
- ejecución;
- conflictos;
- validación;
- explicabilidad;
- gobernanza.

---

# Objetivos

El Razonador deberá permitir al SGCC:

- aplicar reglas sobre hechos conocidos;
- derivar nuevo conocimiento;
- validar restricciones;
- detectar contradicciones;
- clasificar entidades;
- resolver consultas inferenciales;
- evaluar condiciones;
- calcular consecuencias;
- justificar conclusiones;
- invalidar inferencias obsoletas;
- distinguir hechos, inferencias, hipótesis y recomendaciones;
- proporcionar servicios lógicos a aplicaciones, sistemas RAG y agentes.

---

# Alcance

Esta especificación regula:

- la arquitectura lógica del Razonador;
- sus componentes;
- los tipos de razonamiento;
- el modelo general de ejecución;
- la separación entre validación e inferencia;
- la relación con la ontología;
- la relación con el Knowledge Graph;
- la relación con Colecciones;
- la integración con GraphRAG y agentes;
- los perfiles de capacidad;
- los principios de seguridad y explicabilidad.

Esta primera parte no regula todavía en detalle:

- la sintaxis de reglas;
- los algoritmos de matching;
- la agenda de activación;
- el encadenamiento;
- la resolución de conflictos;
- el modelo formal de inferencias;
- las APIs concretas;
- la persistencia;
- la implementación tecnológica.

Estos aspectos se desarrollarán en las partes posteriores.

---

# Definición normativa

El Razonador del SGCC es el componente lógico encargado de evaluar conocimiento estructurado conforme a reglas, axiomas, restricciones y contextos definidos, con el propósito de producir validaciones, inferencias, explicaciones y decisiones derivadas.

El Razonador opera sobre conocimiento existente.

No constituye por sí mismo una fuente primaria de conocimiento.

Sus conclusiones dependerán de:

- los hechos disponibles;
- la ontología aplicada;
- las reglas activas;
- el contexto;
- la versión del Knowledge Graph;
- las políticas de ejecución.

---

# Naturaleza del Razonador

El Razonador representa simultáneamente:

- un motor lógico;
- un motor de reglas;
- un sistema de validación;
- un generador de inferencias;
- un mecanismo de explicación;
- una capa de ejecución semántica.

No deberá concebirse como un único algoritmo.

Será una arquitectura modular capaz de coordinar distintos mecanismos de razonamiento.

---

# Papel dentro del Knowledge Engine

El Knowledge Engine podrá representarse conceptualmente así:

```text
Knowledge Graph
      │
      ├── Hechos
      ├── Entidades
      ├── Relaciones
      ├── Contextos
      ├── Procedencia
      └── Temporalidad
      │
      ▼
Ontología y reglas
      │
      ▼
Razonador
      │
      ├── Validación
      ├── Clasificación
      ├── Inferencia
      ├── Cálculo
      ├── Detección de conflictos
      └── Explicación
      │
      ▼
Servicios inteligentes
      │
      ├── Consultas
      ├── Colecciones dinámicas
      ├── GraphRAG
      ├── Agentes
      ├── Recomendaciones
      └── Aplicaciones
```

---

# Función principal

La función principal del Razonador consiste en aplicar conocimiento formal sobre conocimiento factual.

Conceptualmente:

```text
Hechos
+
Ontología
+
Reglas
+
Contexto
        ↓
Razonador
        ↓
Conclusiones
+
Validaciones
+
Explicaciones
```

---

# Una visión resumida

Ejemplo:

```text
REC-0009 utiliza ING-0008
```

```text
ING-0008 contiene ALG-SOY
```

```text
Regla:
Si una receta utiliza un ingrediente que contiene un alérgeno,
la receta contiene ese alérgeno.
```

Conclusión:

```text
REC-0009 contiene ALG-SOY
```

El Razonador deberá conservar:

- las premisas;
- la regla;
- la conclusión;
- el contexto;
- la procedencia;
- la versión;
- la explicación.

---

# Qué es razonamiento

Razonar consiste en obtener una conclusión a partir de conocimiento previo conforme a un mecanismo definido.

El razonamiento del SGCC podrá adoptar formas como:

```text
Clasificación
```

```text
Deducción
```

```text
Validación
```

```text
Cálculo
```

```text
Resolución de restricciones
```

```text
Evaluación contextual
```

```text
Predicción
```

No todos estos mecanismos producen el mismo tipo de resultado.

---

# Qué no es el Razonador

Para evitar ambigüedades, el Razonador deberá distinguirse de otros componentes.

---

## No es el Knowledge Graph

El Knowledge Graph almacena y conecta hechos.

El Razonador interpreta dichos hechos y produce conclusiones.

---

## No es la ontología

La ontología define:

- clases;
- propiedades;
- axiomas;
- restricciones;
- significado.

El Razonador ejecuta parte de ese significado.

---

## No es una base de datos

Una base de datos persiste información.

El Razonador evalúa conocimiento.

---

## No es un buscador

Un buscador recupera elementos existentes.

El Razonador puede derivar elementos no declarados explícitamente.

---

## No es un sistema RAG

RAG recupera contexto y genera respuestas.

El Razonador puede aportar:

- validaciones;
- restricciones;
- inferencias;
- explicaciones

al contexto utilizado por RAG.

---

## No es un modelo de lenguaje

Un modelo de lenguaje genera texto probabilísticamente.

El Razonador deberá aplicar mecanismos:

- explícitos;
- controlados;
- versionados;
- reproducibles.

---

## No es un agente

Un agente persigue objetivos y utiliza herramientas.

El Razonador constituye una de las herramientas que un agente podrá utilizar.

---

## No es únicamente un validador

La validación es una de sus capacidades.

También podrá:

- clasificar;
- inferir;
- calcular;
- explicar;
- detectar conflictos.

---

## No es únicamente un motor de reglas

Podrá integrar:

- razonamiento ontológico;
- reglas;
- restricciones;
- cálculos;
- temporalidad;
- modelos probabilísticos gobernados.

---

# Diferencia entre hecho e inferencia

Un hecho es una afirmación disponible para el sistema.

Ejemplo:

```text
Miso contiene soja.
```

Una inferencia es una conclusión derivada a partir de uno o varios hechos.

Ejemplo:

```text
Una receta que utiliza miso contiene soja.
```

El sistema deberá conservar esta diferencia en todo momento.

---

# Diferencia entre inferencia y predicción

Una inferencia determinista se obtiene mediante una regla lógica o cálculo exacto.

Una predicción se obtiene mediante un modelo probabilístico.

Ejemplo determinista:

```text
200 g + 300 g = 500 g
```

Ejemplo probabilístico:

```text
Esta receta probablemente pertenece a la cocina japonesa.
```

Ambos resultados deberán representarse de forma distinta.

---

# Diferencia entre inferencia y recomendación

Una inferencia expresa una conclusión derivada.

Una recomendación expresa una propuesta adecuada dentro de un contexto.

Ejemplo:

```text
La receta contiene soja.
```

es una inferencia.

```text
Puede sustituirse el mirin por vinagre de arroz y azúcar.
```

es una recomendación contextual.

La recomendación no deberá convertirse automáticamente en un hecho universal.

---

# Diferencia entre validación e inferencia

La validación responde:

> ¿Cumple este conocimiento las restricciones definidas?

La inferencia responde:

> ¿Qué nuevo conocimiento puede derivarse?

Ejemplo de validación:

```text
¿La receta tiene al menos un ingrediente?
```

Ejemplo de inferencia:

```text
¿La receta contiene un alérgeno derivado de sus ingredientes?
```

---

# Diferencia entre clasificación y validación

La clasificación asigna una entidad a una clase.

Ejemplo:

```text
Miso es un ingrediente fermentado.
```

La validación comprueba si la entidad cumple una condición.

Ejemplo:

```text
Todo ingrediente fermentado debe indicar su proceso de fermentación.
```

---

# Diferencia entre cálculo y razonamiento semántico

Un cálculo opera sobre valores.

Ejemplo:

```text
Cantidad total = cantidad × número de raciones
```

El razonamiento semántico opera sobre significado y relaciones.

Ejemplo:

```text
Una receta es vegana si utiliza únicamente ingredientes compatibles.
```

El Knowledge Engine podrá combinar ambos mecanismos.

---

# Responsabilidades del Razonador

El Razonador será responsable de:

- cargar hechos y reglas;
- identificar premisas aplicables;
- ejecutar reglas;
- producir conclusiones;
- validar restricciones;
- gestionar prioridades;
- detectar contradicciones;
- registrar dependencias;
- conservar explicaciones;
- materializar inferencias cuando proceda;
- invalidar conclusiones afectadas por cambios;
- exponer resultados a otros servicios.

---

# Responsabilidades excluidas

El Razonador no será responsable directamente de:

- redactar documentos;
- crear contenido canónico;
- definir la ontología;
- resolver identidad de entidades durante la ingesta;
- administrar usuarios;
- almacenar archivos;
- tomar decisiones editoriales finales;
- aprobar propuestas generadas por IA;
- modificar conocimiento estable sin gobernanza.

---

# Principios fundamentales

Todo Razonador del SGCC deberá respetar los siguientes principios.

---

## Determinismo cuando sea posible

Una misma ejecución con:

- los mismos hechos;
- las mismas reglas;
- la misma ontología;
- el mismo contexto;
- la misma versión

deberá producir el mismo resultado.

---

## Reproducibilidad

Toda conclusión deberá poder reconstruirse.

---

## Explicabilidad

Toda inferencia relevante deberá poder justificar:

- premisas;
- reglas;
- contexto;
- conclusión.

---

## Trazabilidad

Toda ejecución deberá registrar:

- entrada;
- reglas;
- motor;
- versión;
- fecha;
- salida.

---

## Separación epistemológica

El sistema deberá distinguir:

```text
Hecho explícito
```

```text
Hecho validado
```

```text
Inferencia
```

```text
Hipótesis
```

```text
Predicción
```

```text
Recomendación
```

```text
Propuesta
```

---

## Contextualidad

Una regla podrá ser válida únicamente en un contexto determinado.

El Razonador no deberá generalizarla fuera de dicho contexto.

---

## Incrementalidad

Los cambios deberán provocar el recálculo mínimo necesario.

---

## Invalidación controlada

Una conclusión deberá invalidarse cuando cambien sus premisas o reglas.

---

## Modularidad

Los diferentes tipos de razonamiento deberán poder evolucionar de forma independiente.

---

## Seguridad

El Razonador deberá respetar permisos sobre:

- hechos;
- reglas;
- contextos;
- resultados;
- explicaciones.

---

## Abstención

Cuando no existan premisas suficientes, deberá poder concluir:

```text
Indeterminado
```

---

## No invención

El Razonador no deberá crear:

- entidades inexistentes;
- predicados no definidos;
- fuentes;
- premisas;
- reglas.

---

## Conservación de procedencia

Las conclusiones deberán mantener acceso a la procedencia de sus premisas.

---

## Versionado

Toda regla, modelo y ejecución deberá estar asociada a una versión.

---

# Arquitectura lógica

El Razonador podrá estructurarse mediante los siguientes componentes:

```text
Reasoner
    │
    ├── Fact Provider
    ├── Ontology Adapter
    ├── Rule Registry
    ├── Rule Compiler
    ├── Matcher
    ├── Execution Planner
    ├── Agenda
    ├── Inference Engine
    ├── Constraint Engine
    ├── Conflict Resolver
    ├── Explanation Engine
    ├── Materialization Manager
    ├── Invalidation Manager
    ├── Audit Service
    └── Metrics Service
```

---

# Fact Provider

El `Fact Provider` suministra los hechos que serán evaluados.

Podrá obtenerlos desde:

- Knowledge Graph;
- snapshot;
- colección;
- subgrafo;
- consulta;
- contexto de usuario;
- estado operativo.

Deberá preservar:

- identidad;
- procedencia;
- estado;
- temporalidad;
- permisos.

---

# Ontology Adapter

El `Ontology Adapter` expone al Razonador:

- clases;
- propiedades;
- jerarquías;
- dominio;
- rango;
- equivalencias;
- restricciones;
- axiomas.

Su función consiste en evitar que el motor dependa de una representación ontológica concreta.

---

# Rule Registry

El `Rule Registry` constituye el catálogo oficial de reglas.

Deberá permitir:

- localizar reglas;
- resolver versiones;
- filtrar por módulo;
- consultar estado;
- identificar dependencias;
- conocer prioridad;
- localizar pruebas;
- consultar responsable.

---

# Rule Compiler

El `Rule Compiler` transforma reglas declarativas en una representación ejecutable.

Podrá realizar:

- validación sintáctica;
- validación semántica;
- resolución de variables;
- optimización;
- compilación de patrones;
- análisis de dependencias;
- detección de ciclos.

---

# Matcher

El `Matcher` identifica hechos que satisfacen las premisas de una regla.

Deberá gestionar:

- tipos;
- valores;
- relaciones;
- variables;
- contexto;
- temporalidad;
- confianza;
- estado.

---

# Execution Planner

El `Execution Planner` determina:

- qué reglas evaluar;
- en qué orden;
- sobre qué hechos;
- con qué estrategia;
- bajo qué límites.

---

# Agenda

La `Agenda` contiene activaciones pendientes.

Una activación representa una regla cuyas premisas han sido satisfechas.

---

# Inference Engine

El `Inference Engine` ejecuta reglas y produce conclusiones.

Podrá soportar:

- encadenamiento hacia delante;
- encadenamiento hacia atrás;
- ejecución híbrida;
- inferencia ontológica;
- reglas contextuales.

---

# Constraint Engine

El `Constraint Engine` comprueba restricciones.

Podrá integrar:

- reglas de integridad;
- SHACL;
- cardinalidades;
- dominios;
- rangos;
- valores permitidos;
- invariantes.

---

# Conflict Resolver

El `Conflict Resolver` gestiona:

- reglas incompatibles;
- conclusiones contradictorias;
- prioridades;
- excepciones;
- conocimiento disputado.

---

# Explanation Engine

El `Explanation Engine` construye:

- explicaciones resumidas;
- árboles de justificación;
- caminos;
- trazas técnicas;
- explicaciones contrastivas;
- causas de fallo.

---

# Materialization Manager

El `Materialization Manager` decide qué inferencias deben persistirse.

Gestionará:

- almacenamiento;
- versión;
- estado;
- actualización;
- expiración;
- separación por capas.

---

# Invalidation Manager

El `Invalidation Manager` identifica conclusiones afectadas cuando cambia:

- un hecho;
- una regla;
- la ontología;
- el contexto;
- un modelo;
- una versión.

---

# Audit Service

El `Audit Service` registra:

- ejecuciones;
- reglas activadas;
- conclusiones;
- errores;
- invalidaciones;
- decisiones de conflicto.

---

# Metrics Service

El `Metrics Service` calcula:

- reglas ejecutadas;
- activaciones;
- inferencias;
- tiempo de ejecución;
- conflictos;
- invalidaciones;
- cache hits;
- profundidad de razonamiento.

---

# Arquitectura por capas

El Razonador podrá dividirse en capas.

```text
Capa de acceso
      ↓
Capa de normalización
      ↓
Capa de planificación
      ↓
Capa de ejecución
      ↓
Capa de consistencia
      ↓
Capa de explicación
      ↓
Capa de publicación
```

---

# Capa de acceso

Obtiene:

- hechos;
- reglas;
- ontología;
- contexto;
- permisos.

---

# Capa de normalización

Transforma las entradas en una representación común.

---

# Capa de planificación

Selecciona estrategia y reglas.

---

# Capa de ejecución

Aplica las reglas.

---

# Capa de consistencia

Comprueba conflictos y restricciones.

---

# Capa de explicación

Construye justificaciones.

---

# Capa de publicación

Entrega resultados a:

- Knowledge Graph;
- API;
- GraphRAG;
- agentes;
- aplicaciones.

---

# Entradas del Razonador

El Razonador podrá recibir:

- hechos;
- afirmaciones;
- entidades;
- relaciones;
- reglas;
- axiomas;
- restricciones;
- consultas;
- contexto;
- parámetros;
- versión;
- perfil;
- permisos.

---

## Entrada mínima

```yaml
reasoning_request:
  facts:
    - STM-000123
    - STM-000431

  rules:
    - RULE-ALLERGEN-0001
```

---

## Entrada contextual

```yaml
reasoning_request:
  graph_version: 1.5.0
  ontology_version: 2.0.0

  scope:
    collection: COL-0001

  context:
    diet: vegetarian
    region: Japan

  include_layers:
    - validated
    - inferred

  execution:
    mode: deterministic
```

---

# Salidas del Razonador

El resultado podrá contener:

- inferencias;
- validaciones;
- conflictos;
- clasificaciones;
- cálculos;
- recomendaciones;
- advertencias;
- explicaciones;
- métricas.

---

## Salida conceptual

```yaml
reasoning_result:
  request_id: RSN-000145
  status: completed

  conclusions:
    - INF-000041

  violations: []
  conflicts: []
  warnings: []

  explanation:
    available: true

  execution:
    duration_ms: 18
    rules_evaluated: 4
    rules_fired: 1
```

---

# Tipos de resultado

---

## Hecho inferido

Conclusión derivada de hechos y reglas.

---

## Clasificación

Asignación de una entidad a una clase.

---

## Violación

Incumplimiento de una restricción.

---

## Conflicto

Existencia de conclusiones o hechos incompatibles.

---

## Advertencia

Situación no crítica que requiere atención.

---

## Cálculo

Valor derivado.

---

## Recomendación

Propuesta contextual.

---

## Indeterminación

Ausencia de conocimiento suficiente.

---

# Tipos de razonamiento soportados

El SGCC podrá soportar varios tipos de razonamiento.

---

# Razonamiento ontológico

Utilizará:

- subclases;
- equivalencias;
- dominio;
- rango;
- inversas;
- transitividad;
- restricciones;
- disjunciones.

---

## Ejemplo

```text
Miso es IngredienteFermentado
```

```text
IngredienteFermentado es subclase de Ingrediente
```

Conclusión:

```text
Miso es Ingrediente
```

---

# Razonamiento basado en reglas

Utilizará reglas explícitas.

```text
SI receta usa ingrediente
Y ingrediente contiene alérgeno
ENTONCES receta contiene alérgeno
```

---

# Razonamiento por encadenamiento

Podrá utilizar:

- encadenamiento hacia delante;
- encadenamiento hacia atrás;
- estrategia híbrida.

---

# Razonamiento hacia delante

Parte de hechos conocidos.

```text
Hechos
↓
Reglas aplicables
↓
Nuevos hechos
↓
Nuevas reglas aplicables
```

Será adecuado para:

- materialización;
- alertas;
- validaciones;
- actualización incremental.

---

# Razonamiento hacia atrás

Parte de una pregunta o conclusión objetivo.

```text
Objetivo
↓
Reglas que podrían demostrarlo
↓
Premisas necesarias
↓
Hechos disponibles
```

Será adecuado para:

- consultas;
- explicaciones;
- verificación bajo demanda.

---

# Razonamiento híbrido

Combinará ambas estrategias.

Ejemplo:

- materializar inferencias frecuentes;
- resolver consultas específicas hacia atrás.

---

# Razonamiento temporal

Permitirá interpretar:

- intervalos;
- secuencias;
- vigencia;
- precedencia;
- duración;
- solapamientos.

---

# Razonamiento contextual

Aplicará reglas únicamente cuando el contexto sea compatible.

Ejemplos:

- cocina japonesa;
- entorno doméstico;
- dieta vegana;
- conservación en frío;
- temporada concreta.

---

# Razonamiento cuantitativo

Permitirá:

- conversiones;
- escalado;
- agregación;
- proporciones;
- costes;
- tiempos;
- cantidades;
- nutrientes.

---

# Razonamiento de restricciones

Permitirá comprobar:

- obligatoriedad;
- cardinalidades;
- tipos;
- valores;
- compatibilidad;
- límites;
- invariantes.

---

# Razonamiento de clasificación

Permitirá clasificar:

- ingredientes;
- recetas;
- técnicas;
- documentos;
- colecciones;
- riesgos.

---

# Razonamiento por similitud

Podrá sugerir:

- equivalencias;
- duplicados;
- sustituciones;
- afinidades;
- clasificaciones.

Sus resultados serán probabilísticos o heurísticos.

No deberán convertirse automáticamente en hechos canónicos.

---

# Razonamiento probabilístico

Podrá integrar modelos que produzcan:

- probabilidad;
- puntuación;
- ranking;
- clasificación;
- predicción.

Deberá mantenerse separado del razonamiento determinista.

---

# Razonamiento no monotónico

El SGCC podrá utilizar razonamiento no monotónico en contextos controlados.

Este tipo de razonamiento permite revisar conclusiones cuando aparece nueva información.

Ejemplo:

```text
Se considera una receta vegetariana
salvo evidencia de ingredientes animales.
```

Su utilización deberá ser explícita.

---

# Razonamiento monotónico

Por defecto, las reglas lógicas simples serán monotónicas.

Añadir hechos no invalidará conclusiones anteriores, salvo que:

- cambie una premisa;
- exista una contradicción;
- se aplique lógica no monotónica;
- cambie el contexto.

---

# Mundo abierto

El Razonador operará por defecto bajo el supuesto de mundo abierto.

Esto significa:

```text
No conocido
≠
Falso
```

Ejemplo:

La ausencia de gluten en una lista incompleta no permite concluir:

```text
La receta es sin gluten.
```

---

# Mundo cerrado contextual

Algunos dominios podrán declararse cerrados.

Ejemplo:

```text
Inventario validado de despensa
```

Dentro de ese contexto:

```text
Ingrediente no listado
```

podrá interpretarse como:

```text
Ingrediente no disponible
```

El cierre deberá declararse explícitamente.

---

# Negación

El Razonador deberá distinguir:

- negación explícita;
- ausencia de conocimiento;
- negación por fallo;
- incompatibilidad;
- no aplicabilidad.

---

# Negación explícita

Ejemplo:

```text
REC-0009 no contiene alcohol.
```

---

# Negación por ausencia

No será válida por defecto.

---

# Indeterminación

Cuando no pueda demostrarse ni afirmarse ni negarse una conclusión, el resultado será:

```text
indeterminado
```

---

# Perfiles de ejecución

El Razonador podrá operar bajo distintos perfiles.

---

## Perfil estricto

Características:

- solo hechos validados;
- reglas estables;
- inferencia determinista;
- errores bloqueantes;
- explicación obligatoria.

Adecuado para:

- seguridad;
- validación;
- publicación.

---

## Perfil estándar

Características:

- hechos validados;
- reglas activas;
- inferencias deterministas;
- advertencias no bloqueantes.

---

## Perfil exploratorio

Podrá incluir:

- hipótesis;
- reglas experimentales;
- predicciones;
- baja confianza;
- análisis de escenarios.

Los resultados deberán marcarse claramente.

---

## Perfil RAG

Optimizado para:

- consultas;
- recuperación;
- generación de contexto;
- explicaciones breves.

---

## Perfil agente

Optimizado para:

- herramientas;
- planificación;
- consultas iterativas;
- decisiones controladas.

---

## Perfil auditoría

Prioriza:

- trazabilidad completa;
- versiones;
- premisas;
- reglas;
- tiempos;
- logs;
- diferencias.

---

# Modos de ejecución

---

## Bajo demanda

Se ejecuta ante una consulta.

---

## Por eventos

Se ejecuta cuando cambia un hecho o regla.

---

## Programado

Se ejecuta periódicamente.

---

## Por lotes

Procesa un conjunto amplio.

---

## Incremental

Evalúa únicamente cambios.

---

## Simulación

Ejecuta reglas sin publicar conclusiones.

---

## Dry-run

Muestra qué ocurriría sin modificar ningún estado.

---

# Ámbito de ejecución

Una ejecución podrá aplicarse sobre:

- todo el Knowledge Graph;
- un módulo;
- una colección;
- un subgrafo;
- una entidad;
- una consulta;
- un snapshot;
- un conjunto de hechos.

---

# Presupuesto de ejecución

Toda ejecución podrá limitar:

- número de reglas;
- profundidad;
- tiempo;
- memoria;
- número de inferencias;
- número de iteraciones;
- coste.

---

## Ejemplo

```yaml
execution_limits:
  max_rules: 1000
  max_iterations: 20
  max_inferences: 10000
  timeout_ms: 5000
```

---

# Terminación

El Razonador deberá impedir ciclos infinitos.

Podrá utilizar:

- deduplicación de inferencias;
- límites de iteración;
- detección de ciclos;
- agenda controlada;
- reglas de terminación;
- presupuestos.

---

# Idempotencia

La ejecución repetida sobre las mismas entradas no deberá crear inferencias duplicadas.

---

# Concurrencia

El Razonador deberá gestionar:

- varias consultas;
- actualizaciones simultáneas;
- snapshots;
- cambios de reglas;
- materializaciones.

---

# Consistencia de ejecución

Una ejecución deberá operar sobre una versión consistente de:

- hechos;
- ontología;
- reglas;
- contexto.

No deberá mezclar silenciosamente versiones incompatibles.

---

# Snapshot de razonamiento

Una ejecución crítica podrá fijar:

```text
Knowledge Graph snapshot
+
Ontology version
+
Ruleset version
```

---

# Ruleset

Un `Ruleset` representa un conjunto coherente de reglas.

Ejemplos:

```text
RS-ALLERGENS
RS-DIETS
RS-TEMPORAL
RS-COLLECTIONS
RS-QUALITY
```

---

# Activación de rulesets

Una ejecución podrá seleccionar:

- todos los rulesets activos;
- un conjunto concreto;
- rulesets asociados a una colección;
- rulesets asociados a un perfil.

---

# Dependencias entre rulesets

Un ruleset podrá depender de:

- otro ruleset;
- módulo ontológico;
- subgrafo;
- vocabulario;
- función de cálculo.

---

# Arquitectura modular del razonamiento

El Razonador podrá dividirse por dominios.

```text
Reasoner Core
    │
    ├── Ontology Module
    ├── Recipe Module
    ├── Ingredient Module
    ├── Allergen Module
    ├── Diet Module
    ├── Temporal Module
    ├── Collection Module
    └── Quality Module
```

---

# Núcleo del Razonador

El núcleo deberá proporcionar:

- modelo común;
- ejecución;
- agenda;
- variables;
- contextos;
- versionado;
- explicaciones;
- auditoría.

---

# Módulos especializados

Los módulos podrán añadir:

- reglas;
- funciones;
- restricciones;
- estrategias;
- vocabulario;
- pruebas.

---

# Integración con la ontología

El Razonador deberá utilizar la ontología para:

- validar tipos;
- recorrer jerarquías;
- aplicar restricciones;
- resolver equivalencias;
- interpretar predicados;
- detectar incompatibilidades.

---

# Integración con el Knowledge Graph

El Knowledge Graph proporcionará:

- hechos;
- afirmaciones;
- contextos;
- fuentes;
- capas;
- versiones.

El Razonador devolverá:

- inferencias;
- conflictos;
- violaciones;
- explicaciones;
- dependencias.

---

# Integración con Colecciones

Las Colecciones podrán:

- limitar el ámbito;
- seleccionar hechos;
- activar reglas;
- definir contexto;
- materializar resultados;
- utilizar inferencias para resolver miembros.

Ejemplo:

```text
Colección vegetariana
      ↓
Razonador dietético
      ↓
Clasificación de recetas
      ↓
Miembros inferidos
```

---

# Integración con GraphRAG

El Razonador podrá aportar a GraphRAG:

- hechos derivados;
- restricciones;
- explicaciones;
- advertencias;
- clasificaciones;
- validaciones.

---

# Integración con agentes

Los agentes podrán utilizar herramientas como:

```text
reason
```

```text
validate
```

```text
classify
```

```text
explain
```

```text
simulate
```

El agente no deberá interpretar por sí mismo una conclusión como canónica sin respetar el contrato del Razonador.

---

# Integración con APIs

El Razonador podrá exponerse mediante operaciones conceptuales como:

```text
POST /reason
POST /validate
POST /classify
POST /explain
POST /simulate
GET /rules
GET /inferences/{id}
```

La definición detallada se desarrollará posteriormente.

---

# Integración con MCP

Podrán exponerse herramientas como:

```text
reason_over_graph
```

```text
validate_entity
```

```text
explain_conclusion
```

```text
simulate_rules
```

```text
get_rule_dependencies
```

---

# Seguridad

El Razonador deberá aplicar permisos sobre:

- hechos;
- reglas;
- contextos;
- resultados;
- explicaciones;
- materializaciones.

---

# Seguridad de inferencias

Una inferencia puede revelar información no visible directamente.

El motor deberá comprobar que el usuario puede acceder a todas las premisas necesarias o a una representación autorizada de la conclusión.

---

# Seguridad de explicaciones

Las explicaciones deberán filtrarse para no revelar:

- fuentes restringidas;
- entidades ocultas;
- reglas internas sensibles;
- información personal.

---

# Seguridad alimentaria

Los razonamientos relacionados con:

- alérgenos;
- toxicidad;
- conservación;
- contaminación;
- temperaturas seguras;
- salud;

deberán utilizar perfiles reforzados.

---

## Requisitos reforzados

- hechos validados;
- fuentes autorizadas;
- reglas estables;
- explicación obligatoria;
- sin inferencias puramente probabilísticas;
- revisión humana cuando proceda;
- abstención ante insuficiencia.

---

# Explicabilidad como requisito central

El Razonador no deberá actuar como una caja negra.

Toda conclusión deberá poder asociarse con:

```text
Premisas
+
Regla
+
Contexto
+
Versión
+
Resultado
```

---

# Niveles de explicación

Podrán existir:

- explicación breve;
- explicación estándar;
- explicación detallada;
- explicación técnica;
- explicación de auditoría.

---

# Ejemplo breve

```text
La receta contiene soja porque utiliza miso,
que contiene soja.
```

---

# Ejemplo técnico

```text
STM-000123:
REC-0009 uses_ingredient ING-0008

STM-000431:
ING-0008 contains_allergen ALG-SOY

RULE-ALLERGEN-0001

INF-000041:
REC-0009 contains_allergen ALG-SOY
```

---

# Observabilidad

El Razonador deberá producir:

- logs;
- métricas;
- trazas;
- eventos;
- informes.

---

# Métricas iniciales

Ejemplos:

- ejecuciones;
- reglas evaluadas;
- reglas activadas;
- inferencias generadas;
- inferencias invalidadas;
- conflictos;
- violaciones;
- tiempo medio;
- profundidad media;
- tasa de caché.

---

# Registro de ejecución

Ejemplo conceptual:

```yaml
reasoning_execution:
  id: RSN-EXEC-000145
  request: RSN-000145

  graph_version: 1.5.0
  ontology_version: 2.0.0
  ruleset_version: 1.0.0

  started_at: 2026-08-01T12:00:00+02:00
  finished_at: 2026-08-01T12:00:00.018+02:00

  rules_evaluated: 4
  rules_fired: 1
  inferences_created: 1

  status: completed
```

---

# Calidad del razonamiento

La calidad deberá evaluarse mediante:

- corrección;
- completitud;
- consistencia;
- reproducibilidad;
- explicabilidad;
- rendimiento;
- estabilidad;
- cobertura de reglas;
- tasa de falsos positivos;
- tasa de falsos negativos.

---

# Corrección

Las conclusiones deberán derivarse correctamente de sus premisas.

---

# Completitud

El motor deberá generar todas las conclusiones esperadas dentro del perfil seleccionado.

---

# Consistencia

No deberá producir conclusiones incompatibles sin detectarlas.

---

# Reproducibilidad

Las mismas entradas deberán producir el mismo resultado.

---

# Explicabilidad

Toda conclusión relevante deberá ser justificable.

---

# Rendimiento

El motor deberá responder dentro de los límites definidos.

---

# Cobertura de reglas

Mide qué parte del dominio está respaldada por reglas ejecutables.

---

# Perfiles de capacidad

La implementación podrá evolucionar mediante niveles.

---

## Nivel 1 — Validación básica

Incluye:

- tipos;
- dominio;
- rango;
- campos obligatorios;
- restricciones simples.

---

## Nivel 2 — Reglas deterministas

Añade:

- reglas SI/ENTONCES;
- encadenamiento básico;
- inferencias;
- explicación mínima.

---

## Nivel 3 — Ejecución incremental

Añade:

- agenda;
- dependencias;
- materialización;
- invalidación;
- reglas por módulos.

---

## Nivel 4 — Razonamiento contextual

Añade:

- temporalidad;
- contextos;
- excepciones;
- prioridades;
- conflictos;
- cierres contextuales.

---

## Nivel 5 — Razonamiento híbrido gobernado

Añade:

- modelos probabilísticos;
- GraphRAG;
- agentes;
- simulación;
- razonamiento avanzado;
- evaluación continua;
- gobernanza completa.

---

# Implementación inicial recomendada

La primera implementación práctica del Razonador de NovaCoquinaria debería limitarse a:

```text
Hechos procedentes del Knowledge Graph

+

Reglas deterministas simples

+

Validaciones estructurales y semánticas

+

Encadenamiento hacia delante limitado

+

Consultas inferenciales simples

+

Separación de hechos e inferencias

+

Explicación mediante premisas

+

Invalidación básica

+

Auditoría completa
```

---

# Capacidades inicialmente excluidas

No será necesario implementar en la primera fase:

- lógica no monotónica completa;
- razonamiento probabilístico canónico;
- multiagente;
- planificación compleja;
- aprendizaje automático de reglas;
- razonamiento distribuido;
- escritura autónoma;
- resolución automática de todos los conflictos;
- razonamiento médico o nutricional clínico.

---

# Caso de uso inicial 1 — Propagación de alérgenos

Entrada:

```text
Receta utiliza Ingrediente
Ingrediente contiene Alérgeno
```

Resultado:

```text
Receta contiene Alérgeno
```

---

# Caso de uso inicial 2 — Clasificación dietética

Entrada:

```text
Receta utiliza únicamente ingredientes vegetarianos
```

Resultado:

```text
Receta compatible con dieta vegetariana
```

Solo podrá aplicarse cuando la lista de ingredientes se considere completa.

---

# Caso de uso inicial 3 — Validación de receta

Restricciones:

```text
Toda receta debe tener:
- título;
- al menos un ingrediente;
- al menos un paso.
```

Resultado:

```text
válida
```

o:

```text
violaciones detectadas
```

---

# Caso de uso inicial 4 — Colección dinámica

Entrada:

```text
Colección de recetas japonesas vegetarianas
```

El Razonador podrá combinar:

- pertenencia cultural;
- clasificación dietética;
- estado de la receta;
- contexto.

---

# Caso de uso inicial 5 — Explicación

Pregunta:

```text
¿Por qué esta receta contiene soja?
```

Respuesta:

```text
Porque utiliza miso y el miso contiene soja.
```

---

# Antipatrones arquitectónicos

Deberán evitarse los siguientes antipatrones.

---

## Utilizar un modelo de lenguaje como único razonador

La generación probabilística no sustituye reglas ni validación.

---

## Mezclar hechos e inferencias

Toda conclusión deberá marcarse como derivada.

---

## Reglas sin identidad

Impiden trazabilidad y versionado.

---

## Inferencias sin premisas registradas

Impiden explicación e invalidación.

---

## Reglas ocultas en código

Las reglas de dominio relevantes deberían ser declarativas y gobernables cuando sea viable.

---

## Reglas no versionadas

Impiden reproducir resultados históricos.

---

## Ejecutar sobre versiones inconsistentes

Puede producir conclusiones irreproducibles.

---

## Interpretar ausencia como falsedad

Contradice el mundo abierto.

---

## Generalizar reglas contextuales

Puede producir conclusiones incorrectas.

---

## Materializar todas las inferencias

Puede aumentar complejidad y coste sin necesidad.

---

## No invalidar inferencias

Produce conocimiento obsoleto.

---

## Resolver conflictos silenciosamente

Las divergencias deberán conservarse y explicarse.

---

## Utilizar confianza como verdad lógica

Una puntuación no equivale a certeza.

---

## Exponer explicaciones sin permisos

Puede revelar información restringida.

---

## Permitir publicación autónoma de conclusiones probabilísticas

Deberán pasar por revisión.

---

## Diseñar el Razonador para una única tecnología

La arquitectura deberá ser independiente del motor concreto.

---

# Arquitectura de referencia

```text
┌───────────────────────────────────────────────┐
│             Fuentes de conocimiento           │
│                                               │
│ Knowledge Graph · Ontología · Colecciones     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Entrada del Razonador             │
│                                               │
│ Hechos · Reglas · Contexto · Perfil · Versión │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                Núcleo lógico                  │
│                                               │
│ Matcher · Planner · Agenda · Engines          │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│           Consistencia y explicación          │
│                                               │
│ Validación · Conflictos · Justificaciones     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                   Salidas                     │
│                                               │
│ Inferencias · Violaciones · Alertas · Cálculos│
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                Consumidores                   │
│                                               │
│ KG · APIs · GraphRAG · Agentes · Aplicaciones │
└───────────────────────────────────────────────┘
```

---

# Conformidad arquitectónica

Una implementación del Razonador será arquitectónicamente conforme cuando:

- opere sobre hechos identificables;
- utilice reglas versionadas;
- distinga hechos e inferencias;
- conserve premisas;
- respete contexto;
- respete permisos;
- produzca explicaciones;
- permita invalidación;
- registre ejecuciones;
- no modifique conocimiento canónico sin gobierno.

---

# Conformidad de ejecución

Una ejecución será conforme cuando:

- identifique versiones;
- declare ámbito;
- utilice reglas activas;
- respete límites;
- produzca resultados tipados;
- conserve trazabilidad;
- sea reproducible cuando proceda;
- registre errores y advertencias.

---

# Conformidad de resultado

Un resultado será conforme cuando:

- indique su tipo;
- conserve premisas;
- identifique regla o método;
- declare contexto;
- registre confianza cuando proceda;
- permita explicación;
- pueda invalidarse;
- no se presente como hecho explícito.

---

# Relación con otras especificaciones

| Documento | Relación con el Razonador |
|---|---|
| `ESPECIFICACION_DE_DOCUMENTOS.md` | Proporciona fuentes documentales |
| `ESPECIFICACION_DE_COMPONENTES.md` | Proporciona unidades estructuradas |
| `ESPECIFICACION_DE_RELACIONES.md` | Define los predicados evaluados |
| `ESPECIFICACION_DE_ONTOLOGIA.md` | Define clases, axiomas y restricciones |
| `ESPECIFICACION_DE_COLECCIONES.md` | Delimita ámbitos de razonamiento |
| `ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md` | Proporciona hechos y recibe inferencias |
| `ESPECIFICACION_DEL_MOTOR_RAG.md` | Consumirá conclusiones y explicaciones |
| `ESPECIFICACION_DE_AGENTES.md` | Utilizará el Razonador como herramienta |
| `ESPECIFICACION_DE_VALIDACION.md` | Formalizará validaciones transversales |
| `ESPECIFICACION_DE_APIS.md` | Expondrá servicios de razonamiento |

---

# Transición hacia el modelo formal

Esta primera parte ha establecido:

- la definición del Razonador;
- su propósito;
- sus responsabilidades;
- sus límites;
- sus principios;
- su arquitectura;
- sus componentes;
- los tipos de razonamiento;
- los perfiles de ejecución;
- su integración con el SGCC;
- la implementación inicial recomendada.

La Parte II desarrollará el modelo formal de:

- hechos;
- premisas;
- conclusiones;
- reglas;
- variables;
- condiciones;
- excepciones;
- prioridades;
- contextos;
- inferencias;
- justificaciones;
- dependencias;
- estados;
- versionado;
- contratos YAML.

---

# Conclusión

El Razonador constituye el núcleo lógico del Knowledge Engine de NovaCoquinaria.

Su función consiste en convertir conocimiento representado en conocimiento operativo mediante procesos:

- deterministas cuando sea posible;
- contextuales;
- reproducibles;
- trazables;
- explicables;
- gobernados.

El Razonador no deberá sustituir:

- la ontología;
- el Knowledge Graph;
- la documentación;
- la gobernanza;
- la revisión humana.

Deberá actuar como la capa que conecta dichos elementos y permite ejecutar su significado.

La arquitectura del SGCC puede resumirse así:

```text
Documentos describen

Componentes estructuran

Relaciones conectan

Ontología define

Knowledge Graph materializa

Colecciones delimitan

Razonador interpreta

GraphRAG recupera

Agentes actúan
```

Con esta primera parte queda establecida la base conceptual y arquitectónica necesaria para formalizar, en la siguiente sección, el lenguaje y el metamodelo de reglas e inferencias del SGCC.

---

# Parte II — Modelo formal de reglas, hechos e inferencias

---

# Introducción

La Parte I ha definido:

- el propósito del Razonador;
- su posición dentro del Knowledge Engine;
- sus responsabilidades;
- sus componentes;
- los tipos de razonamiento;
- los perfiles y modos de ejecución;
- su integración con Ontología, Knowledge Graph, Colecciones, GraphRAG y agentes.

Esta segunda parte formaliza las unidades conceptuales que utilizará el motor.

El objetivo consiste en establecer un modelo preciso para representar:

- hechos;
- afirmaciones;
- premisas;
- patrones;
- variables;
- reglas;
- condiciones;
- excepciones;
- conclusiones;
- inferencias;
- justificaciones;
- conflictos;
- dependencias;
- conjuntos de reglas.

Sin este metamodelo, las reglas podrían quedar dispersas entre:

- código;
- documentación;
- consultas;
- prompts;
- scripts;
- decisiones implícitas.

El SGCC deberá evitar esa fragmentación.

Las reglas relevantes del dominio deberán ser:

- identificables;
- declarativas cuando sea viable;
- versionadas;
- comprobables;
- explicables;
- auditables;
- gobernadas.

---

# Objetivos del modelo formal

El modelo formal deberá permitir:

- representar hechos de entrada;
- distinguir hechos explícitos e inferidos;
- expresar reglas de forma estructurada;
- declarar variables y patrones;
- definir condiciones y excepciones;
- asignar prioridad a las reglas;
- limitar reglas mediante contexto;
- producir conclusiones tipadas;
- representar inferencias como entidades auditables;
- conservar la dependencia entre premisas y conclusiones;
- explicar por qué una regla se activó o no;
- invalidar inferencias cuando cambien sus dependencias;
- versionar reglas y conjuntos de reglas;
- traducir reglas a diferentes motores de ejecución.

---

# Principios del metamodelo

Todo elemento formal del Razonador deberá respetar los siguientes principios.

---

## Identidad

Las reglas, inferencias, ejecuciones y artefactos relevantes deberán disponer de identificadores estables.

---

## Tipado

Cada elemento deberá declarar claramente su tipo.

---

## Separación de responsabilidades

Deberán distinguirse:

```text
Hecho
Premisa
Regla
Conclusión
Inferencia
Explicación
```

---

## Declaratividad

Las reglas de dominio deberían expresar:

> qué condición conduce a qué conclusión

sin depender innecesariamente de detalles del motor.

---

## Independencia tecnológica

El metamodelo no deberá quedar acoplado a:

- Drools;
- Prolog;
- SPARQL;
- SHACL;
- Cypher;
- Python;
- Java;
- un motor propietario.

---

## Contexto explícito

Toda regla contextual deberá declarar el ámbito en el que resulta aplicable.

---

## Trazabilidad

Toda inferencia deberá enlazar con:

- premisas;
- regla;
- versión;
- ejecución;
- contexto;
- procedencia.

---

## Reproducibilidad

Las mismas premisas y versiones deberán producir la misma conclusión en reglas deterministas.

---

## Explicabilidad

Las reglas deberán poder transformarse en explicaciones legibles.

---

## Invalidación

Toda conclusión materializada deberá conocer sus dependencias.

---

# Niveles del modelo

El modelo del Razonador podrá comprenderse mediante tres niveles.

```text
M2 — Metamodelo del razonamiento
        ↓
M1 — Reglas y rulesets concretos
        ↓
M0 — Hechos, activaciones e inferencias
```

---

# Nivel M2 — Metamodelo

Define conceptos como:

- hecho;
- patrón;
- variable;
- regla;
- condición;
- excepción;
- conclusión;
- inferencia;
- justificación.

---

# Nivel M1 — Modelo ejecutable

Incluye reglas concretas.

Ejemplo:

```text
RULE-ALLERGEN-0001
Propagación de alérgenos desde ingredientes
```

---

# Nivel M0 — Ejecución

Incluye:

- hechos concretos;
- bindings;
- activaciones;
- inferencias;
- violaciones;
- explicaciones.

Ejemplo:

```text
REC-0009 utiliza ING-0008
ING-0008 contiene ALG-SOY
```

Conclusión:

```text
REC-0009 contiene ALG-SOY
```

---

# Modelo abstracto

Una regla podrá representarse formalmente como:

```text
R = (I, P, C, X, A, O, E, K, V)
```

donde:

- `I` representa su identidad;
- `P` representa sus premisas;
- `C` representa condiciones adicionales;
- `X` representa excepciones;
- `A` representa acciones o conclusiones;
- `O` representa orden o prioridad;
- `E` representa contexto y alcance;
- `K` representa metadatos de conocimiento;
- `V` representa versión y estado.

---

# Unidad de conocimiento factual

El Razonador operará sobre unidades de conocimiento factual.

Estas podrán adoptar distintas formas:

- afirmación del Knowledge Graph;
- valor literal;
- resultado calculado;
- hecho contextual;
- hecho temporal;
- evento;
- estado operativo;
- inferencia previa.

---

# Hecho

Un hecho es una unidad de conocimiento disponible para una ejecución.

Ejemplo:

```text
REC-0009 usa_ingrediente ING-0008
```

El hecho podrá proceder de:

- una afirmación explícita;
- una inferencia activa;
- un cálculo;
- un contexto cerrado;
- una entrada temporal de la ejecución.

---

# Hecho canónico

Procede del conocimiento validado del SGCC.

Ejemplo:

```text
ING-0008 contiene_alergeno ALG-SOY
```

---

# Hecho inferido

Procede de otra inferencia.

Ejemplo:

```text
REC-0009 contiene_alergeno ALG-SOY
```

---

# Hecho temporal

Solo resulta válido durante un intervalo.

Ejemplo:

```text
ING-0041 disponible_en DESPENSA-USER
```

con:

```text
válido hasta 2026-08-03
```

---

# Hecho contextual

Solo resulta interpretable dentro de un contexto.

Ejemplo:

```text
Yogur sustituye Nata
```

en:

```text
salsa fría
```

---

# Hecho negativo

Representa negación explícita.

Ejemplo:

```text
REC-0009 no_contiene_alcohol true
```

No deberá confundirse con la ausencia de una afirmación positiva.

---

# Hecho calculado

Se obtiene mediante una función determinista.

Ejemplo:

```text
REC-0009 tiempo_total 35 minutos
```

---

# Hecho operacional

Representa un estado temporal del entorno de ejecución.

Ejemplo:

```text
HORNO-01 disponible true
```

No deberá convertirse automáticamente en conocimiento permanente.

---

# Contrato mínimo de hecho

```yaml
fact:
  id: STM-000123
  type: explicit_statement

  subject: REC-0009
  predicate: uses_ingredient
  object: ING-0008

  status: validated
```

---

# Contrato ampliado de hecho

```yaml
fact:
  id: STM-000123
  type: explicit_statement

  subject: REC-0009
  predicate: uses_ingredient
  object: ING-0008

  layer: validated
  status: active
  confidence: 1.0

  context:
    recipe_version: 1.2.0
    component: broth

  validity:
    valid_from: 2026-07-31

  provenance:
    source: DOC-0051
    fragment: ingredients
```

---

# Hecho admisible

Un hecho será admisible para una ejecución cuando:

- exista;
- esté activo;
- pertenezca a una capa autorizada;
- sea visible para el solicitante;
- sea compatible con el contexto;
- esté vigente;
- cumpla el nivel mínimo de confianza;
- no haya sido invalidado.

---

# Premisa

Una premisa es una condición factual que debe satisfacerse para activar una regla.

Ejemplo:

```text
?recipe usa_ingrediente ?ingredient
```

Una premisa no es necesariamente un hecho concreto.

Puede ser un patrón que deberá coincidir con uno o varios hechos.

---

# Premisa positiva

Requiere la existencia de un hecho.

```text
?ingredient contiene_alergeno ?allergen
```

---

# Premisa negativa explícita

Requiere un hecho negativo.

```text
?recipe no_contiene_alcohol true
```

---

# Premisa de ausencia

Comprueba que no existe determinado hecho dentro de un ámbito cerrado.

Su utilización deberá ser explícita.

Ejemplo:

```text
no existe ingrediente no vegetariano
```

solo cuando:

```text
la lista de ingredientes está completa
```

---

# Premisa comparativa

Compara valores.

Ejemplo:

```text
?temperature >= 75
```

---

# Premisa tipológica

Exige que una entidad pertenezca a una clase.

```text
?ingredient instance_of AnimalIngredient
```

---

# Premisa relacional

Exige una relación entre entidades.

```text
?recipe uses_ingredient ?ingredient
```

---

# Premisa temporal

Exige una condición sobre tiempo.

```text
?ingredient available_during ?date
```

---

# Premisa contextual

Exige compatibilidad con un contexto.

```text
context.cooking_method = cold_preparation
```

---

# Premisa inferida

Puede utilizar una conclusión de otra regla.

```text
?recipe contains_allergen ?allergen
```

---

# Grupo de premisas

Las premisas podrán agruparse mediante operadores lógicos.

---

## Conjunción

Todas deben satisfacerse.

```text
A AND B AND C
```

---

## Disyunción

Debe satisfacerse al menos una.

```text
A OR B
```

---

## Negación

Una condición debe resultar falsa o ausente dentro de un cierre definido.

```text
NOT A
```

---

## Exclusión lógica

Solo una rama debe cumplirse.

```text
XOR
```

Su uso deberá ser excepcional.

---

## Grupos anidados

```text
A
AND
(
  B
  OR
  C
)
AND
NOT D
```

---

# Patrón

Un patrón describe la forma de un hecho buscado.

Ejemplo:

```yaml
pattern:
  subject: "?recipe"
  predicate: uses_ingredient
  object: "?ingredient"
```

---

# Patrón de triple

Representa:

```text
sujeto — predicado — objeto
```

---

# Patrón tipológico

```yaml
pattern:
  entity: "?ingredient"
  instance_of: FermentedIngredient
```

---

# Patrón literal

```yaml
pattern:
  subject: "?recipe"
  predicate: servings
  value: "?servings"
  datatype: integer
```

---

# Patrón de relación enriquecida

```yaml
pattern:
  type: IngredientUsage

  fields:
    recipe: "?recipe"
    ingredient: "?ingredient"
    quantity: "?quantity"
    unit: gram
```

---

# Patrón de camino

Permitirá recorrer una secuencia de relaciones.

```yaml
path:
  from: "?recipe"

  steps:
    - predicate: uses_ingredient
      bind: "?ingredient"

    - predicate: contains_allergen
      bind: "?allergen"
```

---

# Patrón jerárquico

Podrá incluir subclases.

```yaml
class_match:
  entity: "?ingredient"
  class: AnimalIngredient
  include_subclasses: true
```

---

# Patrón contextual

```yaml
context_match:
  field: preparation_type
  operator: equals
  value: cold_sauce
```

---

# Variable

Una variable representa un valor desconocido que será enlazado durante el matching.

Formato recomendado:

```text
?recipe
?ingredient
?allergen
```

---

# Identidad de variable

El nombre de la variable deberá ser:

- legible;
- local a la regla;
- semánticamente descriptivo;
- estable dentro de la versión de la regla.

---

# Tipado de variable

Una variable podrá declarar un tipo.

```yaml
variables:
  recipe:
    type: Recipe

  ingredient:
    type: Ingredient

  allergen:
    type: Allergen
```

---

# Variable de entidad

Representa una entidad del grafo.

---

# Variable literal

Representa:

- número;
- texto;
- fecha;
- booleano;
- cantidad;
- unidad.

---

# Variable de relación

Podrá enlazar una afirmación o relación enriquecida.

```text
?ingredient_usage
```

---

# Variable contextual

Representa un valor del contexto.

```text
?region
?date
?diet_profile
```

---

# Variable calculada

Obtiene su valor mediante una función.

```text
?total_time = sum(?preparation_time, ?cooking_time)
```

---

# Binding

Un binding asigna un valor concreto a una variable.

Ejemplo:

```yaml
bindings:
  recipe: REC-0009
  ingredient: ING-0008
  allergen: ALG-SOY
```

---

# Binding válido

Será válido cuando:

- respete el tipo declarado;
- satisfaga todas las premisas;
- sea compatible con el contexto;
- no viole restricciones de la regla;
- pertenezca al ámbito de ejecución.

---

# Binding parcial

Puede existir durante la evaluación antes de completar todas las premisas.

---

# Binding completo

Contiene valores para todas las variables necesarias para producir la conclusión.

---

# Unificación

La unificación comprueba si diferentes patrones pueden compartir bindings compatibles.

Ejemplo:

```text
?ingredient = ING-0008
```

debe mantenerse igual en todas las premisas de la activación.

---

# Regla

Una regla representa una unidad declarativa de razonamiento.

Estructura conceptual:

```text
SI
  Premisas
Y
  Condiciones
Y NO
  Excepciones
ENTONCES
  Conclusión
```

---

# Identidad de regla

Formato recomendado:

```text
RULE-<DOMINIO>-XXXX
```

Ejemplos:

```text
RULE-ALLERGEN-0001
RULE-DIET-0014
RULE-COLLECTION-0003
RULE-QUALITY-0022
```

---

# Nombre de regla

Toda regla deberá tener un nombre legible.

Ejemplo:

```text
Propagación de alérgenos desde ingredientes
```

---

# Propósito

Deberá explicar qué problema resuelve.

---

# Tipo de regla

Tipos iniciales recomendados:

```text
inference
validation
classification
calculation
transformation
recommendation
alert
conflict_detection
```

---

# Regla de inferencia

Produce nuevo conocimiento derivado.

---

# Regla de validación

Produce:

- conformidad;
- violación;
- advertencia.

---

# Regla de clasificación

Asigna una entidad a una clase o perfil.

---

# Regla de cálculo

Produce un valor.

---

# Regla de transformación

Genera una representación derivada.

No deberá modificar conocimiento canónico sin gobernanza.

---

# Regla de recomendación

Produce una propuesta contextual.

---

# Regla de alerta

Genera una advertencia operativa o de calidad.

---

# Regla de detección de conflicto

Identifica conocimiento incompatible.

---

# Contrato mínimo de regla

```yaml
id: RULE-ALLERGEN-0001
type: inference_rule
name: Propagación de alérgenos desde ingredientes

premises:
  - subject: "?recipe"
    predicate: uses_ingredient
    object: "?ingredient"

  - subject: "?ingredient"
    predicate: contains_allergen
    object: "?allergen"

conclusion:
  subject: "?recipe"
  predicate: contains_allergen
  object: "?allergen"
```

---

# Contrato normativo ampliado de regla

```yaml
id: RULE-ALLERGEN-0001
type: inference_rule

name: Propagación de alérgenos desde ingredientes

description: >
  Infiere que una receta contiene un alérgeno cuando utiliza
  un ingrediente activo que contiene dicho alérgeno.

purpose: >
  Propagar información validada de alérgenos desde los ingredientes
  hacia las recetas que los utilizan.

module: RS-ALLERGENS
version: 1.0.0
status: stable

authority: normative
priority: 100
salience: 100

variables:
  recipe:
    type: Recipe

  ingredient:
    type: Ingredient

  allergen:
    type: Allergen

premises:
  all:
    - id: P1
      pattern:
        subject: "?recipe"
        predicate: uses_ingredient
        object: "?ingredient"

    - id: P2
      pattern:
        subject: "?ingredient"
        predicate: contains_allergen
        object: "?allergen"

conditions:
  all:
    - expression: ingredient_usage_is_active("?recipe", "?ingredient")

    - expression: fact_status(P2) in ["validated", "confirmed"]

exceptions:
  any:
    - expression: ingredient_removed_by_context("?recipe", "?ingredient")

conclusion:
  type: inferred_statement

  statement:
    subject: "?recipe"
    predicate: contains_allergen
    object: "?allergen"

  confidence:
    strategy: minimum_premise_confidence

context:
  scope: global
  world_assumption: open

execution:
  mode:
    - forward
    - backward

  materialization: selective
  idempotent: true

explanation:
  template:
    es: >
      La receta {recipe} contiene {allergen} porque utiliza
      {ingredient}, que contiene ese alérgeno.

provenance:
  specification: ESPECIFICACION_DEL_RAZONADOR.md
  ontology_module: ONT-MOD-ALLERGENS
  approved_by: semantic_reviewer

governance:
  owner: allergen_rules_maintainer
  review_required: true
```

---

# Estado de una regla

Valores recomendados:

```text
proposed
draft
in_review
experimental
stable
deprecated
disabled
rejected
archived
```

---

# Regla propuesta

Todavía no puede ejecutarse en producción.

---

# Regla en borrador

Está siendo definida.

---

# Regla en revisión

Pendiente de revisión:

- semántica;
- técnica;
- culinaria;
- de seguridad.

---

# Regla experimental

Puede ejecutarse únicamente en perfiles exploratorios o simulaciones.

---

# Regla estable

Puede formar parte de rulesets de producción.

---

# Regla deprecada

No deberá utilizarse en nuevas ejecuciones salvo compatibilidad histórica.

---

# Regla deshabilitada

Permanece registrada, pero no puede activarse.

---

# Autoridad de regla

La autoridad describe su nivel normativo.

Valores posibles:

```text
normative
expert
editorial
documentary
heuristic
probabilistic
experimental
```

---

# Regla normativa

Deriva de:

- una especificación;
- una norma;
- una decisión aprobada;
- un criterio de seguridad.

---

# Regla experta

Ha sido validada por un experto del dominio.

---

# Regla editorial

Regula calidad, estructura o publicación.

---

# Regla documental

Se deriva de una fuente concreta.

---

# Regla heurística

Representa una estrategia práctica no universal.

---

# Regla probabilística

Utiliza un modelo o una puntuación.

---

# Condición

Una condición es una expresión adicional que debe cumplirse después del matching de las premisas.

Ejemplo:

```text
cantidad > 0
```

---

# Tipos de condición

- comparación;
- pertenencia;
- función;
- agregación;
- temporal;
- contextual;
- seguridad;
- calidad;
- permisos.

---

# Condición comparativa

```yaml
condition:
  left: "?temperature"
  operator: greater_than_or_equal
  right: 75
```

---

# Condición de pertenencia

```yaml
condition:
  value: "?status"
  operator: in
  set:
    - validated
    - confirmed
```

---

# Condición funcional

```yaml
condition:
  function: is_complete_ingredient_list
  arguments:
    - "?recipe"
```

---

# Condición temporal

```yaml
condition:
  function: overlaps
  arguments:
    - "?validity"
    - "?query_period"
```

---

# Condición contextual

```yaml
condition:
  context_field: preparation_type
  operator: equals
  value: cold_sauce
```

---

# Función

Una función realiza una operación reutilizable.

Ejemplos:

```text
sum
convert_unit
is_complete
has_permission
normalize_temperature
calculate_total_time
```

---

# Función pura

Con las mismas entradas produce siempre la misma salida y no modifica estado.

Será el tipo recomendado.

---

# Función externa

Consulta un servicio o fuente externa.

Deberá declarar:

- dependencia;
- versión;
- disponibilidad;
- comportamiento ante error;
- impacto sobre reproducibilidad.

---

# Función segura

No produce efectos secundarios.

---

# Función con efectos

Su uso dentro de reglas deberá estar restringido.

El Razonador debería separar:

```text
conclusión lógica
```

de:

```text
acción operacional
```

---

# Excepción

Una excepción impide o modifica la aplicación de una regla general.

Ejemplo:

```text
Yogur puede sustituir nata,
excepto cuando se requiere montado estable.
```

---

# Identidad de excepción

Las excepciones relevantes podrán tener identificador propio.

Formato recomendado:

```text
EXC-<DOMINIO>-XXXX
```

---

# Excepción local

Solo pertenece a una regla.

---

# Excepción reutilizable

Puede utilizarse en varias reglas.

Ejemplo:

```text
EXC-DIET-CROSSCONTAMINATION
```

---

# Excepción contextual

Se activa bajo determinado contexto.

---

# Excepción por entidad

Aplica a una entidad concreta.

---

# Excepción por subclase

Aplica a un conjunto de entidades.

---

# Excepción temporal

Solo resulta válida durante un intervalo.

---

# Excepción normativa

Tiene prioridad sobre reglas de menor autoridad.

---

# Contrato de excepción

```yaml
exceptions:
  - id: EXC-SUBSTITUTION-0003

    description: >
      No aplicar la sustitución cuando la preparación necesite
      nata montada estructuralmente estable.

    when:
      all:
        - context:
            preparation_function: whipped_structure
```

---

# Efecto de una excepción

Una excepción podrá:

- bloquear la regla;
- reducir confianza;
- cambiar la conclusión;
- generar advertencia;
- redirigir a otra regla;
- solicitar revisión.

---

# Prioridad

La prioridad determina qué regla deberá considerarse primero cuando varias reglas compiten.

Formato recomendado:

```text
0–1000
```

Una escala posible:

```text
900–1000  seguridad crítica
700–899   normativa
500–699   específica de dominio
300–499   editorial
100–299   heurística
1–99      auxiliar
```

---

# Salience

La salience representa prioridad de ejecución técnica.

No deberá confundirse con:

- autoridad;
- prioridad semántica;
- confianza.

---

# Prioridad semántica

Determina qué regla prevalece conceptualmente.

---

# Prioridad de ejecución

Determina qué regla se procesa antes.

---

# Especificidad

Cuando dos reglas sean compatibles pero una sea más específica, podrá prevalecer esta última.

Ejemplo:

```text
Regla general:
aceite apto para alta temperatura
```

```text
Regla específica:
aceite de lino no apto para alta temperatura
```

---

# Criterios de especificidad

Podrán considerarse:

- mayor número de premisas;
- clase más específica;
- contexto más restringido;
- entidad concreta;
- intervalo temporal más preciso.

---

# Estrategia de precedencia

Orden recomendado:

1. seguridad;
2. excepción explícita;
3. regla más específica;
4. mayor autoridad;
5. mayor prioridad;
6. mayor confianza;
7. versión más reciente compatible;
8. revisión manual.

---

# Contexto de regla

Toda regla podrá declarar su ámbito contextual.

---

# Contexto global

La regla pretende ser general dentro del SGCC.

---

# Contexto de dominio

Ejemplo:

```text
solo recetas
```

---

# Contexto geográfico

Ejemplo:

```text
Japón
```

---

# Contexto cultural

Ejemplo:

```text
tradición doméstica contemporánea
```

---

# Contexto tecnológico

Ejemplo:

```text
horno de convección
```

---

# Contexto dietético

Ejemplo:

```text
perfil vegetariano
```

---

# Contexto temporal

Ejemplo:

```text
periodo Edo
```

---

# Contexto de colección

Ejemplo:

```text
COL-0001 Cocina japonesa
```

---

# Contexto de usuario

Una regla personal deberá mantenerse separada de las reglas globales.

Ejemplo:

```text
El usuario evita cilantro.
```

No deberá modificar el conocimiento culinario general.

---

# Compatibilidad contextual

Una regla solo podrá activarse cuando:

- su contexto sea compatible;
- el ámbito de ejecución lo permita;
- no exista una exclusión contextual;
- las premisas pertenezcan al mismo contexto o a contextos compatibles.

---

# Cierre contextual

Una regla podrá declarar que opera bajo mundo cerrado para un conjunto concreto.

Ejemplo:

```yaml
world_assumption:
  mode: closed
  scope:
    entity: "?recipe"
    property: uses_ingredient
  completeness_required: true
```

---

# Conclusión

La conclusión describe el resultado producido por una activación.

---

# Tipos de conclusión

- afirmación inferida;
- clasificación;
- violación;
- advertencia;
- cálculo;
- conflicto;
- recomendación;
- propuesta;
- acción derivada.

---

# Conclusión factual

```yaml
conclusion:
  statement:
    subject: "?recipe"
    predicate: contains_allergen
    object: "?allergen"
```

---

# Conclusión de clasificación

```yaml
conclusion:
  classify:
    entity: "?recipe"
    class: VegetarianRecipe
```

---

# Conclusión de violación

```yaml
conclusion:
  violation:
    code: RECIPE_MISSING_STEPS
    target: "?recipe"
    severity: error
```

---

# Conclusión de advertencia

```yaml
conclusion:
  warning:
    code: LOW_CONFIDENCE_SOURCE
    target: "?statement"
```

---

# Conclusión calculada

```yaml
conclusion:
  calculated_fact:
    subject: "?recipe"
    predicate: total_time
    value:
      function: sum
      arguments:
        - "?preparation_time"
        - "?cooking_time"
```

---

# Conclusión de conflicto

```yaml
conclusion:
  conflict:
    type: incompatible_classification
    statements:
      - "?statement_a"
      - "?statement_b"
```

---

# Conclusión de recomendación

```yaml
conclusion:
  recommendation:
    type: ingredient_substitution
    original: "?original"
    substitute: "?substitute"
    confidence: 0.82
```

---

# Conclusión de acción

Una conclusión no debería ejecutar directamente una acción externa.

Se recomienda producir:

```text
ActionRequest
```

o:

```text
ProposedAction
```

para que otro componente decida su ejecución.

---

# Inferencia

Una inferencia es la materialización lógica de una conclusión obtenida mediante una activación.

---

# Identidad de inferencia

Formato recomendado:

```text
INF-XXXXXX
```

Ejemplo:

```text
INF-000041
```

---

# Tipos de inferencia

```text
deterministic
contextual
temporal
calculated
probabilistic
heuristic
```

---

# Inferencia determinista

Se obtiene mediante reglas exactas.

---

# Inferencia contextual

Solo resulta válida bajo contexto.

---

# Inferencia temporal

Tiene un intervalo de validez.

---

# Inferencia calculada

Produce un valor derivado.

---

# Inferencia probabilística

Incluye probabilidad o confianza de modelo.

---

# Inferencia heurística

Procede de una regla práctica no universal.

---

# Contrato mínimo de inferencia

```yaml
id: INF-000041
type: deterministic_inference

conclusion:
  subject: REC-0009
  predicate: contains_allergen
  object: ALG-SOY

premises:
  - STM-000123
  - STM-000431

rule: RULE-ALLERGEN-0001
```

---

# Contrato ampliado de inferencia

```yaml
id: INF-000041
type: deterministic_inference

status: active
layer: inferred

conclusion:
  subject: REC-0009
  predicate: contains_allergen
  object: ALG-SOY

premises:
  - id: STM-000123
    role: recipe_ingredient_usage

  - id: STM-000431
    role: ingredient_allergen

rule:
  id: RULE-ALLERGEN-0001
  version: 1.0.0

ruleset:
  id: RS-ALLERGENS
  version: 1.0.0

execution:
  id: RSN-EXEC-000145
  engine: SGCC-REASONER
  engine_version: 1.0.0

context:
  recipe_version: 1.2.0
  graph_snapshot: KG-SNAP-20260801-001

confidence:
  value: 1.0
  strategy: minimum_premise_confidence

generated_at: 2026-08-01T13:00:00+02:00

validity:
  valid_from: 2026-08-01T13:00:00+02:00

explanation:
  template: RULE-ALLERGEN-0001
  available_levels:
    - brief
    - standard
    - technical
    - audit

provenance:
  derived_from:
    - STM-000123
    - STM-000431

invalidation:
  dependencies:
    - STM-000123
    - STM-000431
    - RULE-ALLERGEN-0001@1.0.0
    - ONT-MOD-ALLERGENS@2.0.0
```

---

# Estado de inferencia

Valores recomendados:

```text
generated
validated
active
materialized
disputed
stale
invalidated
superseded
archived
```

---

# Inferencia generada

Acaba de producirse.

---

# Inferencia validada

Ha superado comprobaciones posteriores.

---

# Inferencia activa

Puede ser utilizada por consultas y otras reglas.

---

# Inferencia materializada

Se ha persistido.

---

# Inferencia disputada

Existe conflicto o revisión pendiente.

---

# Inferencia obsoleta

Sus dependencias han cambiado, pero todavía no ha sido recalculada.

---

# Inferencia invalidada

Ya no debe utilizarse.

---

# Inferencia sustituida

Ha sido reemplazada por otra conclusión.

---

# Confianza de inferencia

La confianza deberá representar la seguridad de la conclusión.

No deberá utilizarse cuando el resultado sea puramente lógico y binario, salvo para conservar la calidad de las premisas.

---

# Estrategias de confianza

---

## Mínimo de premisas

```text
confidence = min(premise_confidences)
```

---

## Producto

```text
confidence = product(premise_confidences)
```

Puede reducir rápidamente la puntuación.

---

## Media ponderada

Utiliza pesos por premisa.

---

## Confianza de regla

Combina la fiabilidad de la regla con las premisas.

---

## Modelo probabilístico

Utiliza la probabilidad devuelta por un modelo.

---

## Confianza manual

Asignada por revisión experta.

---

# Política de confianza

Toda estrategia deberá estar:

- documentada;
- versionada;
- calibrada;
- probada;
- vinculada a un tipo de inferencia.

---

# Dependencia inferencial

Toda inferencia deberá registrar los elementos de los que depende.

---

# Tipos de dependencia

- premisa;
- regla;
- ruleset;
- ontología;
- contexto;
- función;
- modelo;
- snapshot;
- permiso;
- fuente externa.

---

# Grafo de dependencias

```text
INF-000041
    │
    ├── depends_on → STM-000123
    ├── depends_on → STM-000431
    ├── generated_by → RULE-ALLERGEN-0001
    ├── uses_ontology → ONT-MOD-ALLERGENS
    └── generated_in → RSN-EXEC-000145
```

---

# Dependencia directa

La inferencia utiliza directamente el elemento.

---

# Dependencia transitiva

La inferencia depende de otra inferencia que, a su vez, depende de hechos anteriores.

---

# Profundidad inferencial

Indica cuántos niveles existen entre la conclusión y los hechos explícitos.

---

# Cadena inferencial

Ejemplo:

```text
Hecho A
+
Hecho B
        ↓
Inferencia 1
+
Hecho C
        ↓
Inferencia 2
```

---

# Límite de profundidad

Podrá limitarse para controlar:

- rendimiento;
- complejidad;
- explicabilidad;
- riesgo de error acumulado.

---

# Justificación

Una justificación explica formalmente por qué una inferencia es válida.

---

# Árbol de justificación

```text
Conclusión
    │
    ▼
Regla
    │
    ├── Premisa 1
    ├── Premisa 2
    └── Condición
```

---

# Grafo de justificación

Se utilizará cuando varias inferencias compartan premisas o existan múltiples caminos.

---

# Justificación mínima

Incluye:

- conclusión;
- regla;
- premisas.

---

# Justificación estándar

Añade:

- contexto;
- fuentes;
- confianza;
- versión.

---

# Justificación técnica

Añade:

- bindings;
- condiciones;
- activación;
- motor;
- tiempos;
- dependencias.

---

# Justificación de auditoría

Añade:

- hashes;
- snapshot;
- permisos;
- logs;
- decisiones de conflicto;
- historial.

---

# Activación

Una activación representa una coincidencia concreta entre una regla y un conjunto de hechos.

---

# Identidad de activación

Formato recomendado:

```text
ACT-XXXXXX
```

---

# Contrato de activación

```yaml
activation:
  id: ACT-000081

  rule:
    id: RULE-ALLERGEN-0001
    version: 1.0.0

  bindings:
    recipe: REC-0009
    ingredient: ING-0008
    allergen: ALG-SOY

  matched_facts:
    - STM-000123
    - STM-000431

  status: ready
  priority: 100
```

---

# Estado de activación

```text
candidate
ready
scheduled
executing
fired
suppressed
cancelled
failed
```

---

# Activación candidata

Las premisas parecen coincidir, pero aún faltan condiciones.

---

# Activación preparada

Cumple todos los requisitos.

---

# Activación programada

Se encuentra en la agenda.

---

# Activación ejecutada

Ha producido una conclusión.

---

# Activación suprimida

Otra regla o política ha evitado su ejecución.

---

# Activación cancelada

Sus hechos cambiaron antes de ejecutarse.

---

# Agenda

La agenda contiene activaciones pendientes.

Aunque su ejecución detallada se desarrollará en la Parte III, el metamodelo deberá representar:

- identificador;
- regla;
- bindings;
- prioridad;
- antigüedad;
- contexto;
- estado;
- dependencias.

---

# Ruleset

Un ruleset es un conjunto coherente y versionado de reglas.

Formato recomendado:

```text
RS-<DOMINIO>
```

Ejemplos:

```text
RS-ALLERGENS
RS-DIETS
RS-RECIPES
RS-COLLECTIONS
RS-QUALITY
```

---

# Objetivos de un ruleset

- modularizar reglas;
- gestionar versiones;
- declarar dependencias;
- activar perfiles;
- facilitar pruebas;
- asignar responsables;
- publicar releases coherentes.

---

# Contrato mínimo de ruleset

```yaml
id: RS-ALLERGENS
type: ruleset
name: Reglas de alérgenos

version: 1.0.0
status: stable

rules:
  - RULE-ALLERGEN-0001
```

---

# Contrato ampliado de ruleset

```yaml
id: RS-ALLERGENS
type: ruleset

name: Reglas de alérgenos
description: >
  Conjunto de reglas para propagación, validación y explicación
  de alérgenos en ingredientes, preparaciones y recetas.

version: 1.0.0
status: stable
authority: normative

scope:
  modules:
    - ingredients
    - recipes
    - allergens

ontology_dependencies:
  - id: ONT-MOD-ALLERGENS
    version: ">=2.0.0 <3.0.0"

rules:
  - id: RULE-ALLERGEN-0001
    required: true

  - id: RULE-ALLERGEN-0002
    required: true

execution:
  default_profile: strict
  max_iterations: 10
  materialization: selective

governance:
  owner: allergen_rules_maintainer

  reviewers:
    - semantic_reviewer
    - food_safety_reviewer
```

---

# Dependencias entre rulesets

Un ruleset podrá requerir otro.

Ejemplo:

```text
RS-DIETS
depende de
RS-ALLERGENS
```

---

# Dependencia fuerte

Sin el ruleset requerido no puede ejecutarse.

---

# Dependencia opcional

Amplía resultados, pero no impide la ejecución básica.

---

# Conflicto entre rulesets

Dos rulesets podrán:

- producir conclusiones incompatibles;
- utilizar diferentes contextos;
- aplicar políticas distintas.

Estos conflictos deberán declararse y resolverse.

---

# Orden de rulesets

Podrá definirse:

```text
RS-CORE
↓
RS-INGREDIENTS
↓
RS-ALLERGENS
↓
RS-DIETS
↓
RS-COLLECTIONS
```

---

# Perfil de reglas

Un perfil selecciona un subconjunto de rulesets o reglas.

Ejemplos:

```text
strict
standard
exploratory
rag
agent
audit
```

---

# Perfil estricto

Solo incluye:

- reglas estables;
- hechos validados;
- funciones deterministas;
- fuentes autorizadas.

---

# Perfil exploratorio

Puede incluir:

- reglas experimentales;
- hipótesis;
- predicciones;
- simulaciones.

---

# Función de conclusión

Algunas conclusiones requerirán cálculo.

Ejemplo:

```yaml
conclusion:
  calculated_fact:
    subject: "?recipe"
    predicate: total_weight

    value:
      function: sum
      over: "?ingredient_usages.quantity"
      target_unit: gram
```

---

# Agregación

Las reglas podrán utilizar agregaciones como:

- count;
- sum;
- average;
- minimum;
- maximum;
- all;
- any;
- none;
- distinct.

---

# Condición `all`

Ejemplo:

```text
todos los ingredientes son vegetarianos
```

Solo será válida cuando el conjunto se considere completo.

---

# Condición `any`

Ejemplo:

```text
al menos un ingrediente contiene soja
```

---

# Condición `none`

Ejemplo:

```text
ningún ingrediente contiene alcohol
```

Requiere cierre o negación explícita.

---

# Conteo

Ejemplo:

```text
la receta tiene al menos un paso
```

---

# Ventanas temporales

Las reglas podrán operar sobre hechos dentro de una ventana.

Ejemplo:

```text
Cambios producidos durante los últimos siete días
```

---

# Evento

Un evento representa algo ocurrido en un momento.

Ejemplos:

- documento actualizado;
- regla publicada;
- ingrediente añadido;
- inferencia invalidada;
- snapshot generado.

---

# Regla reactiva

Se activa ante un evento.

Ejemplo:

```text
Cuando cambia un ingrediente,
recalcular inferencias de recetas dependientes.
```

---

# Regla derivativa

Produce conocimiento.

---

# Regla operacional

Produce una solicitud de acción.

Deberá diferenciarse claramente de las reglas de conocimiento.

---

# Efectos secundarios

Las reglas de conocimiento no deberían producir efectos secundarios directos.

Se recomienda:

```text
Regla
↓
Conclusión o evento
↓
Orquestador
↓
Acción
```

---

# Severidad

Las reglas de validación podrán producir diferentes niveles.

```text
info
warning
error
critical
```

---

# Violación

Una violación deberá incluir:

- código;
- objetivo;
- regla;
- severidad;
- mensaje;
- evidencia;
- propuesta de corrección.

---

# Contrato de violación

```yaml
violation:
  id: VIO-000041
  code: RECIPE_REQUIRES_INGREDIENT
  severity: error

  target: REC-0042
  rule: RULE-RECIPE-VALIDATION-0001

  message:
    es: La receta debe contener al menos un ingrediente.

  evidence:
    ingredient_count: 0
```

---

# Advertencia

Una advertencia no invalida necesariamente el conocimiento.

Ejemplo:

```text
La receta solo dispone de una fuente.
```

---

# Conflicto

Un conflicto representa incompatibilidad entre:

- hechos;
- inferencias;
- reglas;
- clasificaciones;
- contextos;
- valores.

---

# Contrato de conflicto

```yaml
conflict:
  id: CNF-000021
  type: incompatible_classification

  target: REC-0009

  statements:
    - INF-000041
    - STM-000881

  detected_by: RULE-CONFLICT-0003
  status: open
  severity: high
```

---

# Resultado indeterminado

Una consulta podrá devolver:

```yaml
result:
  status: indeterminate

  reason:
    code: INSUFFICIENT_COMPLETE_DATA

  missing:
    - complete_ingredient_list
```

---

# Resultado no aplicable

Ejemplo:

```text
Una regla de horno no resulta aplicable a una preparación fría.
```

---

# Resultado bloqueado

Puede producirse por:

- permisos;
- dependencia ausente;
- ruleset incompatible;
- datos críticos no validados;
- política de seguridad.

---

# Proveniencia de regla

Toda regla deberá indicar de dónde procede.

Fuentes posibles:

- ontología;
- ADR;
- especificación;
- documento;
- norma;
- experto;
- análisis;
- modelo;
- consenso.

---

# Evidencia de regla

Una regla puede estar respaldada por:

- norma oficial;
- referencia científica;
- documentación interna;
- criterio experto;
- pruebas;
- historial de validación.

---

# Regla derivada de fuente

No deberá confundirse con una afirmación extraída.

Una fuente puede:

- describir un hecho;
- justificar una regla general.

Ambos casos deberán modelarse por separado.

---

# Versionado de reglas

Las reglas utilizarán:

```text
MAJOR.MINOR.PATCH
```

---

## PATCH

Cambios sin impacto semántico.

Ejemplos:

- descripción;
- traducción;
- plantilla de explicación;
- metadatos.

---

## MINOR

Ampliaciones compatibles.

Ejemplos:

- nueva condición opcional;
- nuevo modo de ejecución;
- nueva explicación;
- nuevo contexto compatible.

---

## MAJOR

Cambios incompatibles.

Ejemplos:

- modificar premisas;
- cambiar conclusión;
- alterar prioridad semántica;
- cambiar excepción;
- ampliar o reducir el ámbito de forma incompatible.

---

# Compatibilidad de regla

Una nueva versión deberá declarar:

```text
compatible
partially_compatible
incompatible
```

---

# Sustitución de regla

Una regla deprecada podrá indicar:

```yaml
replaced_by:
  - RULE-ALLERGEN-0010
```

---

# Historial de regla

Deberá conservar:

- versión;
- fecha;
- cambio;
- autor;
- motivo;
- revisión;
- migración.

---

# Versión de inferencia

Una inferencia deberá registrar la versión exacta de:

- regla;
- ruleset;
- ontología;
- Knowledge Graph;
- motor;
- funciones;
- modelos.

---

# Hash semántico de regla

Podrá calcularse sobre:

- premisas;
- condiciones;
- excepciones;
- conclusión;
- contexto;
- prioridad.

Esto permitirá detectar cambios relevantes.

---

# Serialización canónica

Las reglas podrán documentarse en Markdown y estructurarse inicialmente en YAML.

La representación canónica deberá permitir:

- lectura humana;
- validación automática;
- generación de artefactos;
- control de versiones.

---

# YAML como representación inicial

Ventajas:

- legibilidad;
- integración con Git;
- edición manual;
- validación;
- generación;
- independencia del motor.

---

# Riesgos de YAML

Deberán controlarse:

- duplicidad de claves;
- tipos implícitos;
- indentación;
- expresiones no seguras;
- ambigüedad;
- referencias rotas.

---

# Expresiones

Las expresiones deberán utilizar un lenguaje limitado y seguro.

No deberán ejecutar código arbitrario.

---

# Lenguaje de expresiones

Podrá soportar:

- comparaciones;
- operadores lógicos;
- funciones registradas;
- acceso controlado a variables;
- agregaciones;
- operaciones temporales.

---

# Ejemplo seguro

```yaml
expression:
  function: greater_than_or_equal
  arguments:
    - "?temperature"
    - 75
```

---

# Ejemplo no recomendado

```yaml
expression: "eval(user_supplied_code)"
```

---

# Registro de funciones

Toda función disponible deberá pertenecer a un catálogo.

Ejemplo:

```yaml
function:
  id: FN-CONVERT-UNIT
  name: convert_unit
  version: 1.0.0
  deterministic: true
  pure: true
```

---

# Contrato de función

Deberá declarar:

- entrada;
- salida;
- tipos;
- errores;
- determinismo;
- efectos;
- versión;
- pruebas.

---

# Tipos de función

- lógica;
- matemática;
- temporal;
- conversión;
- agregación;
- ontológica;
- consulta;
- validación.

---

# Error de función

La regla deberá declarar cómo actuar cuando una función falle.

Políticas:

```text
fail_rule
skip_activation
produce_warning
mark_indeterminate
retry
```

---

# Validación estructural de regla

Comprobará:

- identificador;
- tipo;
- versión;
- estado;
- variables;
- premisas;
- conclusión;
- referencias;
- expresiones;
- funciones.

---

# Validación semántica de regla

Comprobará:

- tipos de variables;
- dominio;
- rango;
- conclusión compatible;
- contexto;
- contradicciones;
- reglas redundantes;
- ciclos.

---

# Validación de seguridad

Comprobará:

- operaciones permitidas;
- funciones autorizadas;
- acceso a datos;
- ausencia de código arbitrario;
- efectos secundarios;
- ámbitos críticos.

---

# Validación de explicabilidad

Comprobará que la regla pueda generar:

- explicación mínima;
- identificación de premisas;
- identificación de conclusión;
- contexto.

---

# Validación de terminación

Deberá detectar reglas que puedan producir ciclos ilimitados.

---

# Reglas recursivas

Podrán permitirse cuando:

- estén justificadas;
- posean límites;
- tengan estrategia de terminación;
- se prueben explícitamente.

---

# Recursividad directa

Una regla produce hechos que vuelven a activarla.

---

# Recursividad indirecta

Dos o más reglas forman un ciclo.

---

# Prevención de duplicados

El motor deberá reconocer conclusiones ya existentes.

---

# Clave de inferencia

Podrá derivarse de:

- conclusión;
- contexto;
- regla;
- bindings;
- versión.

---

# Inferencias equivalentes

Dos inferencias podrán producir la misma conclusión desde caminos diferentes.

El sistema deberá decidir si:

- conserva ambas justificaciones;
- fusiona la conclusión;
- materializa una sola afirmación con múltiples evidencias.

La opción recomendada será:

```text
una conclusión lógica
+
múltiples justificaciones
```

---

# Multi-justificación

Ejemplo:

```text
REC-0009 pertenece a CocinaJaponesa
```

podrá justificarse por:

- fuente documental;
- ingredientes;
- técnica;
- clasificación experta.

---

# Justificación preferida

Podrá seleccionarse por:

- autoridad;
- simplicidad;
- menor profundidad;
- mayor confianza;
- mayor claridad.

---

# Regla redundante

Dos reglas son redundantes cuando producen la misma conclusión bajo condiciones equivalentes.

La redundancia deberá detectarse.

No siempre será un error si:

- proceden de módulos distintos;
- aportan justificaciones distintas;
- una actúa como respaldo.

---

# Regla subsumida

Una regla más general puede subsumir a otra.

Deberá evaluarse si:

- la específica aporta excepción;
- la específica mejora explicación;
- existe duplicación innecesaria.

---

# Regla contradictoria

Dos reglas son contradictorias cuando, en el mismo contexto, producen conclusiones incompatibles.

---

# Regla no alcanzable

Nunca puede activarse debido a:

- premisas imposibles;
- clases disjuntas;
- condiciones contradictorias;
- dependencia ausente.

---

# Regla huérfana

No pertenece a ningún ruleset activo o no tiene responsable.

---

# Métricas del metamodelo

Podrán calcularse:

- número de reglas;
- reglas por tipo;
- reglas por módulo;
- reglas estables;
- reglas experimentales;
- reglas sin pruebas;
- reglas sin explicación;
- reglas huérfanas;
- reglas redundantes;
- profundidad media;
- número de dependencias;
- inferencias por regla.

---

# Perfil mínimo del metamodelo

La primera implementación podrá soportar:

- hechos simples;
- patrones de triple;
- variables tipadas;
- conjunción de premisas;
- condiciones comparativas;
- conclusión factual;
- reglas versionadas;
- rulesets;
- inferencias con premisas;
- explicación básica.

---

# Perfil estructurado

Añadirá:

- disyunción;
- excepciones;
- prioridades;
- funciones;
- agregaciones;
- contexto;
- validaciones;
- activaciones;
- dependencias.

---

# Perfil semántico

Añadirá:

- jerarquías ontológicas;
- reglas recursivas controladas;
- negación;
- cierres contextuales;
- inferencias temporales;
- SHACL;
- reglas de conflicto.

---

# Perfil avanzado

Añadirá:

- incertidumbre;
- reglas probabilísticas;
- razonamiento no monotónico;
- explicación contrastiva;
- reglas aprendidas;
- multi-justificación avanzada;
- simulación de escenarios.

---

# Ejemplo integrado — Validación de receta

```yaml
id: RULE-RECIPE-VALIDATION-0001
type: validation_rule

name: Una receta debe tener al menos un ingrediente

version: 1.0.0
status: stable
authority: normative
priority: 800

variables:
  recipe:
    type: Recipe

premises:
  all:
    - pattern:
        entity: "?recipe"
        instance_of: Recipe

conditions:
  all:
    - function: count_relations
      arguments:
        entity: "?recipe"
        predicate: uses_ingredient
      operator: less_than
      value: 1

conclusion:
  violation:
    code: RECIPE_REQUIRES_INGREDIENT
    target: "?recipe"
    severity: error

explanation:
  template:
    es: >
      La receta {recipe} no contiene ningún ingrediente declarado.

governance:
  owner: recipe_rules_maintainer
```

---

# Ejemplo integrado — Clasificación vegetariana

```yaml
id: RULE-DIET-0014
type: classification_rule

name: Clasificación de receta vegetariana

version: 1.0.0
status: stable
authority: expert
priority: 700

variables:
  recipe:
    type: Recipe

premises:
  all:
    - pattern:
        entity: "?recipe"
        instance_of: Recipe

    - condition:
        function: is_complete_relation_set
        arguments:
          entity: "?recipe"
          predicate: uses_ingredient

    - condition:
        function: all_related_entities_match_class
        arguments:
          entity: "?recipe"
          predicate: uses_ingredient
          class: VegetarianCompatibleIngredient

exceptions:
  any:
    - pattern:
        subject: "?recipe"
        predicate: contains_cross_contamination_risk
        object: true

conclusion:
  classify:
    entity: "?recipe"
    class: VegetarianRecipe

context:
  world_assumption:
    mode: closed
    scope:
      entity: "?recipe"
      predicate: uses_ingredient

explanation:
  template:
    es: >
      La receta {recipe} se clasifica como vegetariana porque su lista
      de ingredientes está completa y todos los ingredientes declarados
      son compatibles con una dieta vegetariana.
```

---

# Ejemplo integrado — Sustitución contextual

```yaml
id: RULE-SUBSTITUTION-0008
type: recommendation_rule

name: Sustitución contextual de nata por yogur

version: 1.0.0
status: experimental
authority: heuristic
priority: 200

variables:
  preparation:
    type: Preparation

premises:
  all:
    - pattern:
        subject: "?preparation"
        predicate: requires_ingredient
        object: ING-CREAM

conditions:
  all:
    - context:
        preparation_type: cold_sauce

exceptions:
  any:
    - context:
        preparation_function: whipped_structure

conclusion:
  recommendation:
    type: ingredient_substitution
    original: ING-CREAM
    substitute: ING-YOGURT
    ratio: 1.0

  confidence:
    value: 0.78
    type: heuristic

explanation:
  template:
    es: >
      En salsas frías puede proponerse yogur como sustituto de la nata,
      salvo cuando la nata deba aportar una estructura montada estable.
```

---

# Ejemplo integrado — Inferencia con varias justificaciones

```yaml
inferred_statement:
  id: INF-000144

  conclusion:
    subject: REC-0042
    predicate: belongs_to_cuisine
    object: CUISINE-JAPANESE

  justifications:
    - id: JUS-0001
      type: documentary
      premises:
        - STM-0021
      rule: RULE-CUISINE-0001

    - id: JUS-0002
      type: relational
      premises:
        - STM-0031
        - STM-0032
        - STM-0033
      rule: RULE-CUISINE-0004

  preferred_justification: JUS-0001
  confidence: 0.96
  status: active
```

---

# Antipatrones del metamodelo

Deberán evitarse los siguientes antipatrones.

---

## Reglas sin identificador

Impiden versionado, auditoría e invalidación.

---

## Reglas expresadas únicamente en lenguaje natural

Dificultan ejecución y pruebas.

---

## Reglas expresadas únicamente en código

Ocultan conocimiento de dominio y reducen gobernanza.

---

## Variables sin tipo

Aumentan ambigüedad y errores de matching.

---

## Contexto incluido implícitamente en nombres

Ejemplo:

```text
substitutes_in_cold_japanese_sauce
```

El contexto deberá declararse estructuralmente.

---

## Excepciones ocultas en condiciones técnicas

Las excepciones de dominio deberán ser visibles.

---

## Prioridad utilizada para ocultar conflictos

Los conflictos deberán detectarse y explicarse.

---

## Confundir salience con autoridad

El orden técnico no define validez semántica.

---

## Conclusiones con efectos secundarios directos

El razonamiento y la ejecución operacional deberán separarse.

---

## Inferencias sin dependencias

No pueden invalidarse correctamente.

---

## Confianza sin estrategia

Una puntuación aislada no resulta interpretable.

---

## Negación por ausencia no declarada

Puede producir conclusiones falsas.

---

## Reglas probabilísticas tratadas como deterministas

Las predicciones deberán mantenerse separadas.

---

## Regla global para conocimiento contextual

Produce generalizaciones incorrectas.

---

## Funciones no versionadas

Impiden reproducibilidad.

---

## Código arbitrario dentro de expresiones

Introduce riesgos de seguridad y portabilidad.

---

## Materializar activaciones

Las activaciones son artefactos de ejecución, no conocimiento permanente salvo auditoría.

---

## Duplicar una conclusión por cada justificación

Será preferible una conclusión con múltiples justificaciones.

---

## Reutilizar una regla para significados diferentes

Un cambio de significado requiere nueva versión mayor o nueva identidad.

---

# Reglas mínimas de consistencia

---

## Identidad única

No podrán existir dos reglas activas con el mismo identificador y versión.

---

## Variables declaradas

Toda variable utilizada deberá estar declarada o ser inferible de forma inequívoca.

---

## Variables enlazadas

Toda variable empleada en la conclusión deberá estar enlazada por premisas o funciones deterministas.

---

## Tipos compatibles

Los bindings deberán respetar los tipos.

---

## Predicados válidos

Todo predicado deberá existir en el vocabulario u ontología autorizados.

---

## Conclusión válida

La conclusión deberá respetar dominio, rango y restricciones.

---

## Funciones registradas

Toda función deberá existir en el registro.

---

## Contexto coherente

No deberán existir condiciones contextuales incompatibles dentro de una misma regla.

---

## Prioridad válida

La prioridad deberá encontrarse en el rango definido.

---

## Versión obligatoria

Toda regla ejecutable deberá tener versión.

---

## Explicación mínima

Toda regla estable deberá poder producir una explicación básica.

---

## Responsable

Toda regla estable deberá tener propietario o mantenedor.

---

## Pruebas

Toda regla estable deberá disponer de al menos:

- caso positivo;
- caso negativo;
- caso límite.

---

# Validación del contrato YAML

El esquema deberá comprobar:

- campos obligatorios;
- enumeraciones;
- tipos;
- referencias;
- estructura de premisas;
- estructura de conclusiones;
- estados;
- versiones;
- confianza;
- prioridad.

---

# Representación alternativa

El metamodelo podrá transformarse en:

- RDF;
- SHACL Rules;
- SPARQL CONSTRUCT;
- SWRL;
- Datalog;
- Prolog;
- Drools;
- código Java o Python;
- consultas Cypher.

La transformación deberá preservar:

- identidad;
- premisas;
- condiciones;
- conclusión;
- contexto;
- prioridad;
- procedencia.

---

# Pérdida de expresividad

Toda traducción deberá declarar si no puede preservar:

- negación;
- excepción;
- prioridad;
- incertidumbre;
- temporalidad;
- explicación;
- no monotonicidad.

---

# Regla canónica y regla compilada

Deberán distinguirse:

```text
Regla declarativa canónica
```

de:

```text
Representación compilada para un motor
```

La representación compilada deberá regenerarse.

No deberá editarse manualmente.

---

# Artefacto compilado

Deberá registrar:

- regla fuente;
- versión;
- motor;
- versión del compilador;
- fecha;
- hash;
- perfil.

---

# Transición hacia la ejecución

Esta segunda parte ha definido formalmente:

- hechos;
- premisas;
- patrones;
- variables;
- bindings;
- reglas;
- condiciones;
- funciones;
- excepciones;
- prioridades;
- contexto;
- conclusiones;
- inferencias;
- dependencias;
- justificaciones;
- activaciones;
- rulesets;
- estados;
- versionado;
- contratos YAML;
- reglas de consistencia.

La Parte III desarrollará cómo estos elementos se ejecutan realmente dentro del motor, incluyendo:

- carga de hechos;
- compilación de reglas;
- matching;
- unificación;
- creación de activaciones;
- agenda;
- planificación;
- encadenamiento hacia delante;
- encadenamiento hacia atrás;
- resolución híbrida;
- orden de ejecución;
- control de ciclos;
- terminación;
- ejecución incremental;
- materialización;
- invalidación;
- recálculo;
- concurrencia;
- rendimiento.

---

# Conclusión

El metamodelo definido en esta parte convierte el razonamiento del SGCC en un sistema formal, gobernable y ejecutable.

Una regla deja de ser una frase informal o una condición oculta en código.

Pasa a constituir un artefacto de conocimiento con:

- identidad;
- versión;
- propósito;
- premisas;
- variables;
- contexto;
- condiciones;
- excepciones;
- prioridad;
- conclusión;
- explicación;
- procedencia;
- responsable.

Una inferencia deja de ser únicamente un resultado.

Pasa a constituir una entidad derivada con:

- conclusión;
- premisas;
- regla;
- ejecución;
- versión;
- confianza;
- contexto;
- dependencias;
- justificación;
- ciclo de vida.

Esta formalización permite que el Razonador pueda:

- ejecutar reglas de forma reproducible;
- explicar sus conclusiones;
- detectar cambios;
- invalidar resultados;
- comparar versiones;
- integrarse con distintos motores;
- conservar la separación entre hechos, inferencias, predicciones y recomendaciones.

La arquitectura lógica puede resumirse así:

```text
Hechos
      ↓
Patrones
      ↓
Bindings
      ↓
Activaciones
      ↓
Reglas
      ↓
Conclusiones
      ↓
Inferencias
      ↓
Justificaciones
      ↓
Dependencias
```

Con esta base formal, la siguiente parte podrá definir el comportamiento operativo del motor y el ciclo exacto mediante el cual una regla pasa de ser una definición declarativa a producir una conclusión activa dentro del Knowledge Engine.

---

# Parte III — Ejecución del razonador

---

# Introducción

Las partes anteriores han definido:

- la arquitectura conceptual del Razonador;
- el metamodelo de hechos, reglas e inferencias.

Esta tercera parte especifica el comportamiento operativo del motor.

Su objetivo consiste en describir cómo el Razonador transforma un conjunto de hechos en un conjunto coherente de inferencias mediante un proceso controlado, reproducible y explicable.

No se define una implementación concreta.

Se define el comportamiento normativo que cualquier implementación deberá respetar.

---

# Objetivos de la ejecución

Toda ejecución deberá:

- utilizar una visión consistente del conocimiento;
- aplicar únicamente reglas compatibles;
- respetar el contexto;
- generar inferencias reproducibles;
- conservar la trazabilidad;
- evitar ejecuciones infinitas;
- minimizar cálculos innecesarios;
- producir explicaciones;
- registrar métricas;
- permitir la invalidación posterior.

---

# Ciclo general de ejecución

Conceptualmente toda ejecución seguirá el siguiente flujo.

```text
Solicitud
      │
      ▼
Carga del contexto
      │
      ▼
Carga de hechos
      │
      ▼
Carga de reglas
      │
      ▼
Compilación
      │
      ▼
Matching
      │
      ▼
Creación de activaciones
      │
      ▼
Agenda
      │
      ▼
Planificador
      │
      ▼
Ejecución
      │
      ▼
Inferencias
      │
      ▼
Validación
      │
      ▼
Materialización
      │
      ▼
Publicación
```

---

# Pipeline normativo

Toda ejecución deberá poder representarse mediante el siguiente pipeline.

```text
Request

↓

Execution Context

↓

Snapshot

↓

Fact Provider

↓

Rule Registry

↓

Rule Compiler

↓

Matcher

↓

Agenda Builder

↓

Execution Planner

↓

Inference Engine

↓

Constraint Engine

↓

Conflict Resolver

↓

Explanation Engine

↓

Materialization Manager

↓

Publication
```

Cada etapa constituye un contrato independiente.

---

# Solicitud de razonamiento

Toda ejecución comienza mediante una solicitud.

La solicitud deberá definir:

- ámbito;
- contexto;
- perfil;
- versión;
- reglas;
- límites;
- permisos.

---

## Ejemplo

```yaml
reasoning_request:
  profile: strict

  scope:
    collection: COL-0003

  graph_version: 1.5.0

  ontology_version: 2.0.0

  rulesets:
    - RS-ALLERGENS
    - RS-DIETS
```

---

# Contexto de ejecución

Antes de comenzar la evaluación deberá fijarse un contexto.

El contexto podrá incluir:

- usuario;
- permisos;
- colección;
- idioma;
- cocina;
- dieta;
- región;
- temporalidad;
- snapshot.

Ninguna regla podrá modificar este contexto durante la ejecución.

---

# Snapshot de conocimiento

Una ejecución deberá trabajar sobre un snapshot consistente.

El snapshot representa una fotografía lógica del conocimiento.

Incluye:

- Knowledge Graph;
- Ontología;
- Rulesets;
- Configuración.

---

## Objetivos

El snapshot garantiza que:

- todas las reglas utilizan los mismos hechos;
- no aparecen cambios parciales;
- las inferencias son reproducibles.

---

# Carga de hechos

El Fact Provider recuperará únicamente los hechos necesarios.

No deberá cargar automáticamente todo el grafo.

---

## Estrategias

Podrá utilizar:

- carga completa;
- carga por colección;
- carga por entidad;
- carga por subgrafo;
- carga bajo demanda;
- carga incremental.

---

# Normalización

Los hechos deberán normalizarse.

Ejemplos:

- unidades;
- identificadores;
- tipos;
- fechas;
- estados.

---

# Validación inicial

Antes del matching deberán comprobarse:

- existencia;
- vigencia;
- permisos;
- consistencia;
- compatibilidad de tipos.

Los hechos inválidos no deberán entrar en la ejecución.

---

# Carga de reglas

El Rule Registry seleccionará únicamente las reglas compatibles.

Se filtrarán por:

- versión;
- estado;
- perfil;
- autoridad;
- contexto;
- módulo.

---

# Compilación

Las reglas declarativas deberán transformarse en una representación ejecutable.

La compilación podrá incluir:

- resolución de variables;
- validación;
- optimización;
- indexación;
- análisis de dependencias.

---

# Indexación

Las reglas deberán indexarse para reducir el espacio de búsqueda.

Ejemplo:

```text
predicate
↓

uses_ingredient

↓

RULE-0001
RULE-0008
RULE-0012
```

---

# Construcción del espacio de búsqueda

No todas las reglas deberán compararse con todos los hechos.

El motor deberá construir subconjuntos relevantes.

---

# Matching

El Matching identifica qué hechos satisfacen las premisas.

No produce todavía inferencias.

Produce candidatos.

---

## Ejemplo

Regla:

```text
?recipe uses ?ingredient
```

Hechos:

```text
REC-1 uses ING-2

REC-2 uses ING-8
```

Resultado:

```text
dos candidatos
```

---

# Matching estructural

Comprueba:

- sujeto;
- predicado;
- objeto.

---

# Matching tipológico

Comprueba:

- clases;
- subclases;
- restricciones.

---

# Matching contextual

Comprueba:

- región;
- dieta;
- cocina;
- colección.

---

# Matching temporal

Comprueba:

- vigencia;
- fechas;
- intervalos.

---

# Matching por propiedades

Comprueba atributos.

Ejemplo:

```text
temperatura >= 75
```

---

# Matching por camino

Puede recorrer relaciones.

Ejemplo:

```text
Receta

↓

Ingrediente

↓

Alérgeno
```

---

# Matching incremental

Solo analiza hechos modificados desde la última ejecución.

---

# Unificación

Tras el matching se realiza la unificación.

La unificación garantiza que una misma variable representa el mismo valor.

Ejemplo:

```text
?ingredient

↓

ING-0008
```

en todas las premisas.

---

# Binding

La unificación produce bindings.

Ejemplo:

```yaml
bindings:

recipe: REC-0009

ingredient: ING-0008

allergen: ALG-SOY
```

---

# Verificación de condiciones

Una vez creados los bindings deberán evaluarse las condiciones.

Ejemplo:

```text
cantidad > 0

estado = activo

contexto compatible
```

---

# Evaluación de excepciones

Después se comprobarán las excepciones.

Si alguna excepción resulta verdadera:

```text
la activación no deberá producirse
```

salvo que otra política indique lo contrario.

---

# Creación de activaciones

Cada combinación válida produce una activación.

```text
Regla

+

Bindings

+

Condiciones

↓

Activación
```

---

# Agenda

Las activaciones se almacenan en la Agenda.

La Agenda representa el conjunto de trabajo pendiente.

---

## Información mínima

Cada activación deberá registrar:

- regla;
- bindings;
- prioridad;
- profundidad;
- contexto;
- estado.

---

# Planificador

El Execution Planner determina el orden de ejecución.

No modifica reglas.

Solo decide:

```text
qué

cuándo

en qué orden
```

---

# Criterios de planificación

Podrán utilizarse:

- prioridad;
- autoridad;
- especificidad;
- antigüedad;
- profundidad;
- coste;
- estrategia.

---

# Estrategias

El planificador podrá utilizar:

- FIFO;
- prioridad;
- profundidad;
- coste;
- híbrida.

---

# FIFO

Ejecuta por orden de llegada.

Adecuado para cargas pequeñas.

---

# Prioridad

Ejecuta primero reglas críticas.

---

# Especificidad

Prioriza reglas más específicas.

---

# Coste

Intenta minimizar tiempo de ejecución.

---

# Estrategia híbrida

Combina varios criterios.

Será la recomendada.

---

# Forward Chaining

El encadenamiento hacia delante parte de hechos conocidos.

```text
Hechos

↓

Reglas

↓

Nuevos hechos

↓

Más reglas
```

---

## Ventajas

Adecuado para:

- materialización;
- validaciones;
- propagación.

---

## Ejemplo

```text
Miso contiene soja

↓

Receta usa miso

↓

Receta contiene soja
```

---

# Backward Chaining

Parte de una pregunta.

```text
¿La receta contiene soja?

↓

¿Qué reglas podrían demostrarlo?

↓

¿Qué hechos necesito?
```

---

## Ventajas

Adecuado para:

- consultas;
- GraphRAG;
- explicaciones.

---

# Estrategia híbrida

El SGCC recomienda una estrategia híbrida.

Ejemplo:

```text
Inferencias frecuentes

↓

Materializadas
```

```text
Consultas complejas

↓

Backward
```

---

# Activación de reglas

Una regla podrá:

- dispararse;
- esperar;
- cancelarse;
- suprimirse.

---

# Ejecución

Cuando una activación alcanza el estado:

```text
ready
```

el motor ejecutará:

- funciones;
- cálculos;
- conclusión.

---

# Producción de inferencias

Una ejecución puede producir:

- una inferencia;
- varias;
- ninguna.

No todas las reglas generan resultados.

---

# Detección de duplicados

Antes de crear una inferencia deberá comprobarse:

```text
¿Existe ya?
```

Si existe:

```text
no crear duplicado
```

---

# Actualización de inferencias

Cuando cambie una justificación:

- actualizar dependencias;
- conservar historial.

---

# Encadenamiento

Las nuevas inferencias podrán activar nuevas reglas.

```text
Inferencia

↓

Nuevo hecho

↓

Matching

↓

Nueva activación
```

---

# Profundidad

Toda ejecución registrará:

```text
depth = 0
```

para hechos explícitos.

Cada inferencia incrementará:

```text
depth +1
```

---

# Límite de profundidad

Podrá configurarse.

Ejemplo:

```yaml
limits:

max_depth: 8
```

---

# Control de ciclos

El motor deberá impedir:

```text
A

↓

B

↓

A
```

---

## Estrategias

- hashes;
- memoria;
- grafo de dependencias;
- profundidad;
- presupuesto.

---

# Terminación

La ejecución finalizará cuando:

- no existan activaciones;
- se alcance un límite;
- ocurra un error crítico;
- el usuario cancele.

---

# Presupuesto

Toda ejecución podrá limitar:

```yaml
limits:

max_rules: 1000

max_inferences: 5000

timeout_ms: 3000
```

---

# Materialización

El Materialization Manager decidirá:

```text
¿Persistir?

o

¿Mantener solo en memoria?
```

---

## Inferencias candidatas

No todas las inferencias deberán persistirse.

---

## Inferencias permanentes

Adecuadas para:

- alérgenos;
- clasificaciones;
- índices.

---

## Inferencias efímeras

Adecuadas para:

- consultas;
- GraphRAG;
- simulaciones.

---

# Invalidación

Cuando cambie:

- un hecho;
- una regla;
- la ontología;

las inferencias afectadas deberán invalidarse.

---

# Recalculo

El motor deberá recalcular únicamente las inferencias afectadas.

No todo el grafo.

---

# Ejecución incremental

La ejecución incremental constituye el modo recomendado.

Conceptualmente:

```text
Cambio

↓

Dependencias

↓

Inferencias afectadas

↓

Recalcular
```

---

# Caché

Podrá utilizarse caché para:

- consultas;
- reglas compiladas;
- funciones;
- patrones.

---

# Invalidación de caché

Toda modificación relevante deberá invalidar la caché correspondiente.

---

# Paralelismo

Las reglas independientes podrán ejecutarse en paralelo.

---

# Restricciones

Nunca deberán romper:

- consistencia;
- reproducibilidad;
- aislamiento.

---

# Concurrencia

El Reasoner deberá soportar:

- múltiples consultas;
- múltiples usuarios;
- múltiples agentes.

---

# Aislamiento

Cada ejecución deberá mantener su propio contexto.

---

# Recuperación ante errores

Errores posibles:

- timeout;
- regla inválida;
- función fallida;
- dependencia ausente.

---

# Estrategias

- abortar;
- continuar;
- degradar;
- reintentar.

---

# Observabilidad

Cada ejecución generará:

- logs;
- eventos;
- métricas;
- trazas.

---

# Métricas

Ejemplos:

- tiempo;
- reglas evaluadas;
- reglas activadas;
- inferencias;
- conflictos;
- profundidad.

---

# Registro de ejecución

```yaml
execution:

id: RSN-EXEC-00145

rules_evaluated: 145

rules_fired: 24

inferences: 37

duration_ms: 84

depth: 4

status: completed
```

---

# Estados de ejecución

```text
created

loading

matching

planning

executing

validating

materializing

completed

failed

cancelled
```

---

# Optimización

El motor podrá optimizar mediante:

- índices;
- compilación;
- caché;
- paralelismo;
- ejecución incremental.

---

# Calidad de ejecución

Toda ejecución deberá ser:

- determinista;
- reproducible;
- explicable;
- trazable;
- eficiente.

---

# Antipatrones

Deberán evitarse:

- cargar todo el grafo siempre;
- recompilar reglas continuamente;
- materializar todas las inferencias;
- ignorar dependencias;
- recalcular el sistema completo;
- ejecutar sin snapshot;
- mezclar versiones;
- permitir ciclos infinitos.

---

# Transición hacia la Parte IV

La Parte III ha definido:

- el pipeline operativo;
- matching;
- unificación;
- agenda;
- planificación;
- forward chaining;
- backward chaining;
- materialización;
- invalidación;
- ejecución incremental;
- control de ciclos;
- concurrencia;
- observabilidad.

La **Parte IV** abordará la gestión de:

- consistencia;
- conflictos;
- restricciones;
- excepciones;
- SHACL;
- validación semántica;
- resolución de contradicciones;
- políticas de calidad;
- degradación segura del razonamiento.

---

# Conclusión

La ejecución del Razonador constituye el puente entre el conocimiento declarado y el conocimiento operativo.

A partir de un conjunto coherente de hechos, reglas y contexto, el motor debe producir inferencias reproducibles, explicables y trazables, garantizando al mismo tiempo la consistencia del sistema y la eficiencia de su ejecución.

Con esta parte queda definido el ciclo operativo del **Knowledge Engine**, proporcionando la base necesaria para abordar en la siguiente sección la gestión formal de la consistencia y la resolución de conflictos del conocimiento.

---

# Parte IV — Consistencia, conflictos, excepciones y validación

---

# Introducción

Las partes anteriores han definido:

- la arquitectura conceptual del Razonador;
- el modelo formal de hechos, reglas e inferencias;
- el pipeline operativo de ejecución;
- el matching;
- la unificación;
- la agenda;
- la planificación;
- el encadenamiento;
- la materialización;
- la invalidación;
- la ejecución incremental.

Esta cuarta parte establece cómo el Razonador deberá preservar la coherencia del conocimiento durante y después de cada ejecución.

Aplicar reglas no consiste únicamente en producir conclusiones.

El motor deberá comprobar también que dichas conclusiones:

- respetan la ontología;
- no violan restricciones;
- no contradicen conocimiento de mayor autoridad;
- son válidas dentro de su contexto;
- mantienen su vigencia temporal;
- conservan procedencia;
- pueden explicarse;
- no producen estados inseguros.

El SGCC deberá distinguir claramente entre:

```text
Validación
≠
Inferencia
≠
Detección de conflictos
≠
Resolución de conflictos
```

Cada una de estas capacidades posee:

- objetivos diferentes;
- contratos diferentes;
- resultados diferentes;
- políticas de ejecución diferentes.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir el modelo de consistencia del Razonador;
- distinguir validación, inferencia y resolución de conflictos;
- formalizar las restricciones;
- regular la aplicación de excepciones;
- representar contradicciones;
- definir políticas de precedencia;
- gestionar negación e indeterminación;
- establecer cierres contextuales;
- integrar SHACL y validación ontológica;
- gestionar incertidumbre;
- prevenir inferencias inseguras;
- definir mecanismos de degradación controlada;
- establecer contratos de violación y conflicto;
- garantizar una salida coherente y explicable.

---

# Principios de consistencia

Toda ejecución deberá respetar los siguientes principios.

---

## Consistencia antes que completitud

Cuando una conclusión adicional produzca una contradicción no resoluble, el sistema deberá priorizar la coherencia frente a la generación indiscriminada de inferencias.

---

## Conservación del conflicto

Las contradicciones no deberán sobrescribirse ni ocultarse.

Deberán:

- registrarse;
- contextualizarse;
- clasificarse;
- conservar sus fuentes;
- someterse a resolución.

---

## Contextualidad

Dos afirmaciones aparentemente incompatibles podrán coexistir si pertenecen a:

- regiones distintas;
- periodos distintos;
- variantes distintas;
- perfiles distintos;
- versiones distintas.

---

## Autoridad explícita

El Razonador no deberá decidir qué conocimiento prevalece sin una política declarada.

---

## Ausencia no equivalente a falsedad

El modelo general utilizará mundo abierto.

```text
No conocido
≠
Falso
```

---

## Explicación de decisiones

Toda supresión, invalidación o resolución deberá poder explicar:

- qué elementos competían;
- qué política se aplicó;
- por qué prevaleció una conclusión;
- qué alternativas fueron descartadas.

---

## Seguridad conservadora

Ante incertidumbre en ámbitos críticos, el motor deberá optar por:

- abstención;
- advertencia;
- bloqueo;
- revisión humana.

---

## Separación entre dato inválido y dato contradictorio

Un hecho inválido viola el modelo o una restricción.

Un hecho contradictorio puede estar correctamente formado, pero ser incompatible con otro conocimiento.

---

# Modelo de consistencia

La consistencia podrá evaluarse en varios niveles.

```text
Consistencia
    │
    ├── estructural
    ├── tipológica
    ├── ontológica
    ├── lógica
    ├── contextual
    ├── temporal
    ├── inferencial
    ├── operacional
    └── de seguridad
```

---

# Consistencia estructural

Comprueba que los elementos poseen una forma válida.

Ejemplos:

- identificadores;
- tipos de datos;
- campos obligatorios;
- referencias;
- versiones;
- formatos.

---

# Consistencia tipológica

Comprueba que:

- los sujetos;
- los objetos;
- las variables;
- los bindings;
- los valores

poseen tipos compatibles.

---

# Consistencia ontológica

Comprueba:

- dominio;
- rango;
- cardinalidades;
- disjunciones;
- jerarquías;
- equivalencias;
- clases insatisfacibles.

---

# Consistencia lógica

Comprueba que el conjunto de hechos e inferencias no contiene contradicciones no gestionadas.

---

# Consistencia contextual

Comprueba que una afirmación o regla se interpreta dentro del contexto adecuado.

---

# Consistencia temporal

Comprueba:

- vigencia;
- intervalos;
- secuencia;
- solapamientos;
- estados históricos;
- versiones.

---

# Consistencia inferencial

Comprueba que las conclusiones derivadas:

- se apoyan en premisas válidas;
- utilizan reglas activas;
- no dependen de inferencias invalidadas;
- conservan sus dependencias;
- no producen ciclos prohibidos.

---

# Consistencia operacional

Comprueba que una ejecución:

- utiliza un snapshot coherente;
- no mezcla versiones incompatibles;
- respeta límites;
- no deja estados parciales.

---

# Consistencia de seguridad

Comprueba que una conclusión no revela información obtenida de:

- premisas restringidas;
- subgrafos no autorizados;
- datos personales;
- reglas internas sensibles.

---

# Validación e inferencia

La validación responde:

> ¿Cumple un elemento las restricciones definidas?

La inferencia responde:

> ¿Qué conclusión puede derivarse?

---

## Ejemplo de validación

```text
Toda receta debe poseer al menos un ingrediente.
```

Resultado:

```text
Válida
```

o:

```text
Violación
```

---

## Ejemplo de inferencia

```text
Una receta utiliza miso.
El miso contiene soja.
```

Resultado:

```text
La receta contiene soja.
```

---

# Validación y conflicto

La validación detecta incumplimientos respecto a una regla o forma esperada.

Un conflicto detecta conocimiento incompatible entre sí.

Ejemplo de validación:

```text
La receta no tiene título.
```

Ejemplo de conflicto:

```text
La receta está clasificada simultáneamente como vegana
y contiene huevo.
```

---

# Detección y resolución de conflictos

La detección responde:

> ¿Existe una incompatibilidad?

La resolución responde:

> ¿Cómo debe gestionarse esa incompatibilidad?

El Razonador deberá poder detectar conflictos sin resolverlos automáticamente.

---

# Restricción

Una restricción define una condición que el conocimiento deberá cumplir.

Podrá utilizarse para:

- validación;
- clasificación;
- seguridad;
- integridad;
- calidad;
- consistencia.

---

# Tipos de restricción

---

## Restricción estructural

Ejemplo:

```text
Toda regla debe tener identificador y versión.
```

---

## Restricción de cardinalidad

Ejemplo:

```text
Una receta debe tener al menos un paso.
```

---

## Restricción de tipo

Ejemplo:

```text
usa_ingrediente debe conectar Recipe con Ingredient.
```

---

## Restricción de valor

Ejemplo:

```text
La confianza debe encontrarse entre 0 y 1.
```

---

## Restricción de patrón

Ejemplo:

```text
Los identificadores de regla deben cumplir RULE-<DOMINIO>-XXXX.
```

---

## Restricción relacional

Ejemplo:

```text
Una colección no puede ser subcolección de sí misma.
```

---

## Restricción jerárquica

Ejemplo:

```text
La relación subclase_de no puede formar ciclos.
```

---

## Restricción contextual

Ejemplo:

```text
Una sustitución debe declarar el tipo de preparación.
```

---

## Restricción temporal

Ejemplo:

```text
valid_until no puede ser anterior a valid_from.
```

---

## Restricción de procedencia

Ejemplo:

```text
Toda afirmación estable debe disponer de fuente.
```

---

## Restricción de seguridad

Ejemplo:

```text
Una inferencia de seguridad alimentaria debe proceder
de reglas estables y hechos validados.
```

---

## Restricción de completitud

Ejemplo:

```text
La clasificación vegetariana requiere
una lista de ingredientes declarada como completa.
```

---

# Identidad de restricción

Formato recomendado:

```text
CONSTRAINT-<DOMINIO>-XXXX
```

Ejemplos:

```text
CONSTRAINT-RECIPE-0001
CONSTRAINT-RULE-0004
CONSTRAINT-SAFETY-0012
```

---

# Contrato mínimo de restricción

```yaml
id: CONSTRAINT-RECIPE-0001
type: cardinality_constraint

target_class: Recipe

property: uses_ingredient

minimum_count: 1

severity: error
```

---

# Contrato ampliado de restricción

```yaml
id: CONSTRAINT-RECIPE-0001
type: cardinality_constraint

name: Una receta debe tener al menos un ingrediente

description: >
  Toda entidad activa de tipo Recipe deberá declarar
  al menos una relación uses_ingredient.

version: 1.0.0
status: stable
authority: normative

target:
  class: Recipe
  include_subclasses: true

constraint:
  property: uses_ingredient
  minimum_count: 1

severity: error

message:
  es: La receta debe declarar al menos un ingrediente.

context:
  layers:
    - validated

governance:
  owner: recipe_rules_maintainer
```

---

# Severidad de restricción

Valores recomendados:

```text
info
warning
error
critical
```

---

## Info

Aporta información sin exigir acción.

---

## Warning

Indica una situación mejorable.

No bloquea necesariamente la ejecución.

---

## Error

Invalida el elemento o resultado dentro del perfil aplicable.

---

## Critical

Impide publicación o uso seguro.

---

# Violación

Una violación representa el incumplimiento concreto de una restricción.

Formato recomendado:

```text
VIO-XXXXXX
```

---

# Contrato ampliado de violación

```yaml
id: VIO-000041
type: constraint_violation

constraint:
  id: CONSTRAINT-RECIPE-0001
  version: 1.0.0

target:
  id: REC-0042
  type: Recipe

severity: error

status: open

message:
  es: La receta no declara ningún ingrediente.

evidence:
  observed_count: 0
  required_minimum: 1

execution:
  id: RSN-EXEC-000211

detected_at: 2026-08-01T17:00:00+02:00
```

---

# Estado de violación

Valores recomendados:

```text
open
acknowledged
accepted
resolved
suppressed
false_positive
archived
```

---

# Violación aceptada

Puede mantenerse cuando:

- existe una excepción aprobada;
- el elemento está incompleto deliberadamente;
- pertenece a un entorno experimental;
- forma parte de una migración.

---

# Supresión de violación

Una violación podrá suprimirse temporalmente.

Toda supresión deberá indicar:

- motivo;
- responsable;
- fecha;
- periodo;
- alcance;
- revisión.

---

# Excepción de validación

Una excepción podrá permitir que un elemento no cumpla una restricción general.

Ejemplo:

```text
Los documentos archivados no necesitan mantenedor activo.
```

---

# SHACL

Cuando el Knowledge Graph utilice RDF, SHACL podrá formar parte de la capa de validación.

SHACL será adecuado para:

- estructura de nodos;
- cardinalidades;
- tipos;
- valores;
- patrones;
- relaciones;
- formas cerradas.

---

# Shape

Una `Shape` define la forma esperada de un nodo.

Ejemplo conceptual:

```text
RecipeShape
    │
    ├── title minCount 1
    ├── usesIngredient minCount 1
    ├── containsStep minCount 1
    └── status in allowed values
```

---

# Node Shape

Valida una entidad concreta o una clase de entidades.

---

# Property Shape

Valida una propiedad.

---

# Severidad SHACL

Podrá mapearse a:

```text
sh:Info
sh:Warning
sh:Violation
```

El SGCC podrá añadir el nivel:

```text
critical
```

mediante una extensión propia.

---

# SHACL y reglas del Razonador

SHACL no deberá sustituir todas las reglas.

Se utilizará principalmente para:

- validación estructural;
- integridad;
- cardinalidad;
- patrones.

Las reglas del Razonador se utilizarán además para:

- inferencias;
- contexto;
- temporalidad;
- excepciones complejas;
- conflictos;
- recomendaciones;
- cálculo.

---

# Validación ontológica

El Ontology Adapter deberá proporcionar al Constraint Engine información sobre:

- clases;
- propiedades;
- disjunciones;
- dominio;
- rango;
- cardinalidades;
- equivalencias;
- restricciones de valor.

---

# Dominio y rango

Ejemplo:

```text
uses_ingredient

domain: Recipe
range: Ingredient
```

Una relación como:

```text
Japan uses_ingredient Miso
```

será incompatible, salvo que exista una modelización específica que la justifique.

---

# Disjunción

Dos clases podrán declararse incompatibles.

Ejemplo:

```text
AnimalIngredient
disjoint_with
VeganIngredient
```

Un individuo no deberá clasificarse simultáneamente en ambas clases dentro del mismo contexto.

---

# Clases insatisfacibles

Una clase será insatisfacible cuando sus restricciones no puedan cumplirse simultáneamente.

El Razonador deberá detectarlas antes de clasificar individuos.

---

# Cardinalidades ontológicas

Ejemplo:

```text
Un identificador canónico debe tener exactamente un valor.
```

---

# Validación local y global

---

## Validación local

Evalúa una entidad, relación o subgrafo limitado.

Ventajas:

- rapidez;
- incrementalidad;
- explicación sencilla.

---

## Validación global

Evalúa el conjunto completo o un módulo amplio.

Permite detectar:

- ciclos;
- contradicciones;
- inconsistencias transversales;
- dependencias rotas.

---

# Estrategia recomendada

```text
Validación local
ante cada cambio
```

más:

```text
Validación global
antes de publicación
```

---

# Validación previa a la ejecución

Antes de activar una regla deberán comprobarse:

- regla válida;
- hechos admisibles;
- tipos compatibles;
- contexto compatible;
- permisos;
- vigencia;
- dependencias.

---

# Validación posterior a la ejecución

Después de generar una conclusión deberán comprobarse:

- forma;
- tipos;
- dominio;
- rango;
- contradicciones;
- seguridad;
- duplicidad;
- procedencia;
- explicabilidad.

---

# Pipeline de validación

```text
Entrada
   │
   ▼
Validación estructural
   │
   ▼
Validación tipológica
   │
   ▼
Validación ontológica
   │
   ▼
Validación contextual
   │
   ▼
Validación temporal
   │
   ▼
Validación inferencial
   │
   ▼
Validación de seguridad
   │
   ▼
Resultado
```

---

# Conflicto

Un conflicto representa una incompatibilidad relevante entre elementos del razonamiento.

Formato recomendado:

```text
CNF-XXXXXX
```

---

# Tipos de conflicto

---

## Conflicto factual

Dos afirmaciones explícitas son incompatibles.

Ejemplo:

```text
La receta contiene alcohol.
La receta no contiene alcohol.
```

---

## Conflicto inferencial

Dos reglas producen conclusiones incompatibles.

---

## Conflicto entre hecho e inferencia

Una conclusión contradice un hecho validado.

---

## Conflicto tipológico

Una entidad pertenece a clases incompatibles.

---

## Conflicto de valor

Una propiedad funcional posee varios valores distintos.

---

## Conflicto temporal

Dos estados incompatibles se solapan temporalmente.

---

## Conflicto contextual

Dos conclusiones incompatibles se aplican al mismo contexto.

---

## Conflicto de identidad

Dos entidades podrían representar el mismo concepto o una entidad podría mezclar varios conceptos.

---

## Conflicto de reglas

Dos reglas contienen políticas incompatibles.

---

## Conflicto de prioridad

Las políticas disponibles no permiten decidir qué regla debe prevalecer.

---

## Conflicto de procedencia

Dos fuentes de autoridad comparable sostienen afirmaciones divergentes.

---

## Conflicto de seguridad

Una conclusión potencialmente válida viola una política de seguridad.

---

# Contrato de conflicto

```yaml
id: CNF-000021
type: fact_inference_conflict

target: REC-0009

elements:
  - id: STM-000881
    role: explicit_statement

  - id: INF-000041
    role: inferred_statement

description: >
  Una afirmación explícita indica que la receta no contiene soja,
  mientras que una inferencia concluye que sí contiene soja.

severity: critical
status: open

context:
  recipe_version: 1.2.0

detected_by:
  rule: RULE-CONFLICT-0003
  execution: RSN-EXEC-000211
```

---

# Estado de conflicto

Valores recomendados:

```text
detected
under_review
resolved
accepted_divergence
suppressed
invalidated
archived
```

---

# Divergencia aceptada

Un conflicto podrá aceptarse cuando represente:

- perspectivas distintas;
- contextos distintos;
- fuentes históricas divergentes;
- incertidumbre real;
- clasificación controvertida.

---

# Detección de conflictos

La detección podrá realizarse:

- antes de la ejecución;
- durante el encadenamiento;
- después de materializar;
- durante validaciones globales;
- ante cambios incrementales.

---

# Reglas de conflicto

Los conflictos podrán detectarse mediante reglas explícitas.

Ejemplo:

```yaml
id: RULE-CONFLICT-0003
type: conflict_detection_rule

premises:
  all:
    - pattern:
        subject: "?entity"
        predicate: "?predicate"
        object: "?value"

    - pattern:
        subject: "?entity"
        predicate: "?negative_predicate"
        object: true

conditions:
  all:
    - function: predicates_are_logical_negations
      arguments:
        - "?predicate"
        - "?negative_predicate"

conclusion:
  conflict:
    type: positive_negative_contradiction
```

---

# Política de resolución

Toda resolución deberá utilizar una política identificable.

Formato recomendado:

```text
POLICY-CONFLICT-XXXX
```

---

# Estrategias de resolución

---

## Preservar todas

```text
preserve_all
```

Mantiene todas las afirmaciones y registra el conflicto.

Adecuado para:

- conocimiento histórico;
- controversias;
- fuentes divergentes.

---

## Separar por contexto

```text
context_separation
```

Asigna las afirmaciones a contextos distintos.

---

## Mayor autoridad

```text
authority_wins
```

Prevalece la fuente o regla de mayor autoridad.

---

## Mayor especificidad

```text
specificity_wins
```

Prevalece la regla más específica.

---

## Mayor prioridad

```text
priority_wins
```

Prevalece el elemento con prioridad superior.

---

## Mayor confianza

```text
confidence_wins
```

Solo deberá utilizarse cuando las puntuaciones sean comparables y estén calibradas.

---

## Más reciente

```text
latest_valid_wins
```

Adecuada únicamente cuando el dominio considere que el dato más reciente reemplaza al anterior.

---

## Hecho validado sobre inferencia

```text
validated_fact_wins
```

Una afirmación explícita validada podrá prevalecer sobre una inferencia.

El conflicto deberá conservarse para revisar la regla o las premisas.

---

## Revisión manual

```text
manual_review
```

Adecuada cuando no pueda resolverse automáticamente.

---

## Bloqueo

```text
block_result
```

Impide utilizar la conclusión hasta resolver el conflicto.

---

# Precedencia recomendada

El SGCC podrá utilizar el siguiente orden general:

1. política de seguridad;
2. contexto;
3. excepción explícita;
4. conocimiento normativo;
5. mayor especificidad;
6. hecho validado;
7. autoridad;
8. prioridad;
9. confianza calibrada;
10. revisión manual.

Este orden no deberá aplicarse ciegamente.

Cada dominio podrá definir su propia política.

---

# Resolución automática

Solo debería permitirse cuando:

- la política sea inequívoca;
- los elementos sean comparables;
- el riesgo sea bajo;
- la resolución sea reproducible;
- exista explicación.

---

# Resolución semiautomática

El sistema podrá:

- proponer una resolución;
- calcular impacto;
- mostrar evidencias;
- solicitar aprobación.

---

# Resolución manual

Será obligatoria para conflictos relacionados con:

- seguridad alimentaria;
- alergias;
- identidad canónica;
- cambios ontológicos;
- fuentes normativas divergentes;
- datos personales;
- publicación pública.

---

# Resultado de resolución

Toda resolución deberá registrar:

```yaml
resolution:
  id: CNF-RES-000021
  conflict: CNF-000021

  policy:
    id: POLICY-CONFLICT-0004
    strategy: validated_fact_wins

  selected:
    - STM-000881

  invalidated:
    - INF-000041

  rationale: >
    La afirmación explícita ha sido validada manualmente y posee
    mayor autoridad que la inferencia derivada.

  decided_by: semantic_reviewer
  decided_at: 2026-08-01T17:30:00+02:00
```

---

# Excepciones

Las excepciones permiten adaptar reglas generales a casos específicos.

El sistema deberá evitar dos extremos:

```text
Reglas excesivamente generales
```

y:

```text
Reglas llenas de excepciones ocultas
```

---

# Jerarquía de excepciones

Una excepción podrá aplicarse a:

- una regla;
- un ruleset;
- una clase;
- una entidad;
- una colección;
- un contexto;
- un periodo.

---

# Excepción de bloqueo

Impide la aplicación de la regla.

---

# Excepción modificadora

Cambia:

- conclusión;
- confianza;
- severidad;
- materialización;
- explicación.

---

# Excepción de redirección

Activa una regla alternativa.

---

# Excepción de revisión

Impide automatización y exige decisión humana.

---

# Excepción temporal

Tiene una vigencia limitada.

---

# Excepción experimental

Solo se aplica en perfiles exploratorios.

---

# Prioridad de excepción

Una excepción explícita y compatible deberá prevalecer sobre la regla general.

---

# Conflictos entre excepciones

Dos excepciones podrán competir.

Se resolverán conforme a:

1. seguridad;
2. especificidad;
3. autoridad;
4. prioridad;
5. fecha de vigencia;
6. revisión manual.

---

# Negación

El Razonador deberá distinguir varias formas de negación.

---

# Negación explícita

Representa una afirmación negativa declarada.

Ejemplo:

```text
REC-0009 not_contains_alcohol true
```

---

# Negación ontológica

Puede derivarse de:

- clases disjuntas;
- incompatibilidades;
- restricciones.

---

# Negación por fallo

Asume que algo es falso porque no puede demostrarse.

No deberá utilizarse en mundo abierto salvo cierre contextual.

---

# Negación débil

Representa:

```text
no se ha podido demostrar
```

No equivale a falsedad.

---

# Negación fuerte

Representa:

```text
se ha demostrado que es falso
```

---

# Cierres contextuales

Un cierre contextual declara que un conjunto de conocimiento se considera completo para una propiedad y ámbito concretos.

Ejemplo:

```yaml
closure:
  entity: REC-0009
  property: uses_ingredient
  status: complete
  valid_for:
    recipe_version: 1.2.0
```

---

# Uso del cierre

Solo con ese cierre podrá inferirse:

```text
Ningún ingrediente de la receta pertenece a AnimalIngredient.
```

a partir de una lista exhaustiva.

---

# Tipos de cierre

---

## Cierre por entidad

Declara completa una propiedad de una entidad.

---

## Cierre por colección

Declara completo un conjunto dentro de una colección.

---

## Cierre por snapshot

Declara que un inventario o catálogo está completo en una versión.

---

## Cierre temporal

Solo resulta válido en un periodo.

---

# Invalidación de cierre

Un cierre deberá invalidarse cuando:

- se añada un miembro;
- cambie la versión;
- se detecte información incompleta;
- cambie la fuente;
- expire su vigencia.

---

# Indeterminación

El sistema deberá admitir resultados no binarios.

Estados recomendados:

```text
true
false
indeterminate
not_applicable
conflicted
blocked
```

---

# Verdadero

La conclusión ha sido demostrada.

---

# Falso

Existe negación explícita o demostración válida de falsedad.

---

# Indeterminado

No existe evidencia suficiente.

---

# No aplicable

La regla no pertenece al contexto.

---

# En conflicto

Existen conclusiones incompatibles no resueltas.

---

# Bloqueado

Una política impide producir o divulgar el resultado.

---

# Modelo de resultado lógico

```yaml
logical_result:
  target: REC-0009
  proposition: suitable_for_vegan_diet

  value: indeterminate

  reason:
    code: INGREDIENT_SET_NOT_CLOSED

  missing_requirements:
    - complete_ingredient_list
```

---

# Incertidumbre

El Razonador deberá distinguir:

- incertidumbre lógica;
- incertidumbre factual;
- incertidumbre de fuente;
- incertidumbre de modelo;
- incertidumbre contextual.

---

# Incertidumbre lógica

No puede demostrarse una conclusión.

---

# Incertidumbre factual

Las premisas poseen confianza limitada.

---

# Incertidumbre de fuente

La fuente puede ser incompleta o discutible.

---

# Incertidumbre de modelo

Procede de una predicción probabilística.

---

# Incertidumbre contextual

No está claro en qué ámbito resulta válida la afirmación.

---

# Confianza y consistencia

Una alta confianza no elimina una contradicción.

Dos afirmaciones de alta confianza pueden seguir siendo incompatibles.

---

# Agregación de confianza

La confianza deberá calcularse mediante una estrategia definida.

No deberá utilizarse para resolver automáticamente conflictos críticos.

---

# Umbrales

Podrán definirse umbrales por perfil.

Ejemplo:

```yaml
confidence_policy:
  strict:
    minimum_fact_confidence: 0.95
    minimum_inference_confidence: 0.95

  exploratory:
    minimum_fact_confidence: 0.50
    minimum_inference_confidence: 0.60
```

---

# Confianza insuficiente

Una conclusión podrá:

- no generarse;
- marcarse como provisional;
- producir advertencia;
- requerir revisión.

---

# Validación de reglas

Antes de activarse, una regla deberá superar varias validaciones.

---

## Validación estructural

Comprueba:

- identidad;
- versión;
- premisas;
- conclusión;
- referencias;
- funciones.

---

## Validación semántica

Comprueba:

- tipos;
- dominio;
- rango;
- variables;
- contexto;
- conclusión.

---

## Validación lógica

Comprueba:

- premisas contradictorias;
- conclusión imposible;
- recursividad;
- terminación;
- redundancia.

---

## Validación de excepciones

Comprueba:

- referencias;
- prioridad;
- contexto;
- contradicciones.

---

## Validación de seguridad

Comprueba:

- funciones autorizadas;
- efectos;
- fuentes;
- permisos;
- ámbito crítico.

---

## Validación de explicabilidad

Comprueba que la regla pueda producir una explicación mínima.

---

# Reglas incompatibles

El sistema deberá detectar rulesets con reglas incompatibles antes de ejecutarlos conjuntamente.

---

# Matriz de compatibilidad de rulesets

Ejemplo:

| Ruleset | Compatible | Requiere | Incompatible |
|---|---|---|---|
| `RS-DIETS` | `RS-INGREDIENTS` | `RS-CORE` | — |
| `RS-EXPERIMENTAL` | `RS-CORE` | — | `RS-STRICT-SAFETY` |

---

# Validación de ruleset

Deberá comprobar:

- dependencias;
- versiones;
- ciclos;
- reglas deshabilitadas;
- reglas deprecadas;
- políticas de conflicto;
- compatibilidad ontológica.

---

# Redundancia

La redundancia no siempre constituye un error.

Podrá clasificarse como:

```text
exacta
parcial
intencional
de respaldo
innecesaria
```

---

# Regla duplicada

Dos reglas son duplicadas cuando:

- tienen premisas equivalentes;
- contexto equivalente;
- conclusión equivalente;
- prioridad equivalente.

---

# Regla solapada

Coincide parcialmente con otra.

---

# Regla subsumida

Una regla específica está completamente cubierta por otra más general.

---

# Análisis de impacto

Antes de cambiar una regla deberá calcularse:

- inferencias dependientes;
- reglas downstream;
- colecciones;
- consultas;
- índices RAG;
- agentes;
- pruebas;
- materializaciones.

---

# Validación incremental

Ante un cambio, el sistema deberá validar primero:

- el elemento modificado;
- sus vecinos;
- sus dependencias;
- sus inferencias;
- sus consumidores.

---

# Validación global

Será necesaria:

- antes de release;
- tras cambios ontológicos;
- tras migraciones;
- al modificar políticas de conflicto;
- al incorporar rulesets críticos.

---

# Degradación segura

Cuando una capacidad falle, el sistema deberá evitar resultados silenciosamente incorrectos.

---

# Estrategias de degradación

---

## Abstenerse

No producir conclusión.

---

## Utilizar último resultado válido

Solo cuando:

- esté identificado como desactualizado;
- siga siendo seguro;
- la política lo permita.

---

## Ejecutar sin inferencias opcionales

Mantener únicamente hechos explícitos.

---

## Deshabilitar ruleset afectado

Permitir que otros módulos continúen.

---

## Reducir perfil

Ejemplo:

```text
strict
↓
validated_facts_only
```

---

## Solicitar revisión

Generar un caso manual.

---

# Fallo abierto y fallo cerrado

---

## Fail-open

Permite continuar pese al error.

Solo deberá utilizarse en ámbitos de bajo riesgo.

---

## Fail-closed

Bloquea la conclusión ante cualquier incertidumbre crítica.

Será el comportamiento recomendado para:

- alérgenos;
- seguridad alimentaria;
- privacidad;
- publicación canónica.

---

# Política por severidad

Ejemplo:

```yaml
failure_policy:
  info: continue
  warning: continue_with_warning
  error: block_result
  critical: abort_execution
```

---

# Seguridad alimentaria

Las reglas de seguridad deberán utilizar un perfil reforzado.

---

# Requisitos

- hechos validados;
- fuentes autorizadas;
- cierre explícito cuando proceda;
- reglas estables;
- fail-closed;
- explicación obligatoria;
- auditoría completa;
- revisión humana para conflictos críticos.

---

# Regla de alérgenos

La ausencia de un alérgeno no deberá inferirse únicamente porque no aparezca en una lista parcial.

---

# Contaminación cruzada

La compatibilidad dietética podrá diferenciar:

```text
no contiene ingrediente
```

de:

```text
sin riesgo de contaminación cruzada
```

---

# Toxicidad

Una clasificación de seguridad no deberá depender de:

- similitud vectorial;
- modelo generativo;
- fuente no validada;
- recomendación heurística.

---

# Validación de recomendaciones

Las recomendaciones deberán comprobar:

- contexto;
- restricciones;
- evidencia;
- conflictos;
- impacto;
- seguridad.

---

# Recomendación incompatible

Una recomendación deberá rechazarse cuando viole:

- alergias;
- dieta;
- disponibilidad;
- técnica;
- seguridad;
- preferencia obligatoria.

---

# Resultado seguro

Podrá incluir:

```yaml
recommendation_result:
  status: blocked

  reason:
    code: ALLERGEN_CONFLICT

  conflicting_constraint:
    allergen: ALG-SOY

  explanation: >
    La sustitución propuesta contiene soja y no es compatible
    con el perfil indicado.
```

---

# Consistencia temporal

Una conclusión deberá evaluarse en relación con:

- tiempo de validez de premisas;
- vigencia de la regla;
- snapshot;
- momento de consulta.

---

# Intersección temporal

Una inferencia solo será válida durante la intersección de vigencia de sus premisas.

Ejemplo:

```text
Premisa A válida: enero–junio
Premisa B válida: marzo–agosto
```

Inferencia válida:

```text
marzo–junio
```

---

# Inferencia sin solapamiento

Si las premisas no son simultáneamente válidas, la regla no deberá activarse.

---

# Corrección retroactiva

Una fuente puede corregir un hecho histórico.

El sistema deberá distinguir:

- cuándo ocurrió el hecho;
- cuándo se registró la corrección.

---

# Consistencia contextual

Una conclusión deberá conservar el contexto más específico necesario.

---

# Generalización contextual

No deberá promoverse una conclusión contextual a una afirmación global sin una regla explícita.

---

# Compatibilidad de contextos

Los contextos podrán ser:

```text
compatibles
incompatibles
parcialmente_compatibles
indeterminados
```

---

# Herencia de contexto

El contexto podrá heredarse desde:

- ejecución;
- colección;
- documento;
- afirmación;
- regla.

La fuente más específica deberá prevalecer.

---

# Orden de precedencia contextual

```text
Contexto de afirmación
↓
Contexto de regla
↓
Contexto de colección
↓
Contexto de ejecución
↓
Contexto global
```

---

# Conflicto contextual

Cuando dos contextos sean incompatibles, la activación deberá:

- descartarse;
- separarse;
- marcarse como indeterminada;
- solicitar revisión.

---

# Consistencia entre capas

El sistema deberá distinguir:

```text
explicit
validated
inferred
hypothetical
predicted
recommended
```

---

# Reglas por capa

Una regla deberá indicar qué capas puede consumir.

Ejemplo:

```yaml
input_layers:
  - validated
  - inferred
```

---

# Restricción de capas

Un perfil crítico podrá impedir utilizar:

- hipótesis;
- predicciones;
- recomendaciones

como premisas.

---

# Promoción entre capas

La promoción deberá estar gobernada.

Ejemplo:

```text
Predicción
↓
Revisión
↓
Afirmación validada
```

No deberá ocurrir automáticamente.

---

# Consistencia de procedencia

Toda inferencia deberá poder rastrear sus fuentes finales.

---

# Fuente perdida

Si una fuente deja de ser resoluble, las inferencias dependientes podrán quedar:

```text
stale
```

o:

```text
invalidated
```

según la política.

---

# Fuente deprecada

Una fuente deprecada no invalida necesariamente el hecho.

Deberá evaluarse:

- sustituto;
- autoridad;
- vigencia;
- corroboración.

---

# Múltiples fuentes

Una conclusión podrá disponer de varias justificaciones.

Si una fuente desaparece, la conclusión podrá seguir activa si conserva otra justificación válida.

---

# Consistencia de permisos

El Constraint Engine deberá validar también el ámbito de autorización.

---

# Inferencia no autorizada

Una inferencia podrá ser válida globalmente, pero no visible para un usuario concreto.

---

# Explicación filtrada

La explicación podrá mostrar una versión autorizada sin revelar premisas restringidas.

Ejemplo:

```text
La conclusión se deriva de fuentes internas validadas.
```

cuando no sea posible mostrar el detalle.

---

# Conflicto de permisos

Si una conclusión no puede explicarse sin revelar información restringida, el sistema podrá:

- ocultarla;
- mostrarla sin detalle;
- denegar acceso;
- solicitar autorización adicional.

---

# Registro de validación

Toda validación relevante deberá quedar registrada.

```yaml
validation_run:
  id: VAL-RSN-000041
  execution: RSN-EXEC-000211

  profile: strict

  results:
    structural:
      status: passed

    ontological:
      status: passed

    consistency:
      status: failed
      conflicts: 1

    security:
      status: passed

  completed_at: 2026-08-01T18:00:00+02:00
```

---

# Estados de validación

```text
not_started
running
passed
passed_with_warnings
failed
blocked
cancelled
```

---

# Quality Gate del Razonador

Una ejecución podrá bloquearse si existe:

- regla inválida;
- incompatibilidad ontológica;
- conflicto crítico;
- inferencia sin premisas;
- pérdida de procedencia;
- fallo de seguridad;
- cierre incompleto usado como completo;
- resultado crítico indeterminado.

---

# Advertencias no bloqueantes

Ejemplos:

- fuente única;
- confianza media;
- regla experimental;
- explicación parcial;
- nodo huérfano;
- dependencia opcional ausente.

---

# Pruebas de consistencia

Toda regla estable deberá incluir pruebas.

---

# Caso positivo

La regla produce la conclusión esperada.

---

# Caso negativo

La regla no se activa.

---

# Caso de excepción

La regla general queda bloqueada o modificada.

---

# Caso de conflicto

Se produce una contradicción controlada.

---

# Caso indeterminado

Faltan datos suficientes.

---

# Caso temporal

La regla solo se activa durante el intervalo válido.

---

# Caso contextual

La regla se activa en un contexto y no en otro.

---

# Caso de seguridad

La ejecución debe bloquearse.

---

# Golden cases

Podrán mantenerse conjuntos de casos esperados.

```yaml
golden_case:
  id: GC-ALLERGEN-0001

  facts:
    - STM-000123
    - STM-000431

  expected:
    inferences:
      - subject: REC-0009
        predicate: contains_allergen
        object: ALG-SOY

    conflicts: []
    violations: []
```

---

# Pruebas de regresión

Deberán detectar cambios inesperados en:

- conclusiones;
- conflictos;
- prioridades;
- explicaciones;
- severidades;
- materializaciones.

---

# Pruebas de mutación

Podrán modificar intencionadamente:

- operadores;
- prioridades;
- condiciones;
- excepciones

para comprobar que las pruebas detectan errores.

---

# Pruebas de propiedades

Podrán comprobar invariantes como:

```text
Ninguna inferencia activa depende de una premisa invalidada.
```

```text
Toda violación crítica bloquea la publicación.
```

```text
Una conclusión no puede ser simultáneamente activa e invalidada.
```

---

# Métricas de consistencia

Ejemplos:

- conflictos abiertos;
- conflictos críticos;
- violaciones;
- reglas incompatibles;
- clases insatisfacibles;
- inferencias invalidadas;
- cierres desactualizados;
- resultados indeterminados;
- excepciones activadas;
- resoluciones automáticas;
- revisiones manuales pendientes.

---

# Métricas de validación

Ejemplos:

- duración;
- entidades validadas;
- reglas validadas;
- porcentaje conforme;
- violaciones por módulo;
- advertencias por severidad;
- falsos positivos;
- regresiones.

---

# Métricas de conflicto

Ejemplos:

- tiempo medio de resolución;
- conflictos por ruleset;
- política más utilizada;
- divergencias aceptadas;
- conflictos reabiertos;
- conflictos provocados por cambios ontológicos.

---

# Observabilidad

La capa de consistencia deberá producir:

- logs;
- eventos;
- métricas;
- trazas;
- informes.

---

# Eventos

Ejemplos:

```text
constraint_violated
conflict_detected
conflict_resolved
exception_applied
inference_blocked
closure_invalidated
validation_failed
```

---

# Trazabilidad de decisión

Toda decisión automática deberá registrar:

- política;
- entradas;
- prioridad;
- autoridad;
- resultado;
- alternativas;
- explicación.

---

# Informe de consistencia

Una ejecución podrá producir:

```yaml
consistency_report:
  execution: RSN-EXEC-000211

  status: failed

  summary:
    conflicts: 1
    violations: 2
    warnings: 3

  blocking_issues:
    - CNF-000021

  recommendations:
    - review_explicit_statement
    - verify_rule_allergen_0001
```

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Confundir ausencia con negación

Produce conclusiones falsas en mundo abierto.

---

## Resolver conflictos sobrescribiendo datos

Destruye trazabilidad.

---

## Aplicar prioridades sin explicación

Oculta decisiones semánticas.

---

## Utilizar confianza como único criterio

No considera autoridad, contexto ni seguridad.

---

## Generalizar conclusiones contextuales

Produce conocimiento incorrecto.

---

## Excepciones ocultas en código

Impiden gobierno y revisión.

---

## Excepciones sin vigencia

Pueden permanecer activas indefinidamente.

---

## Silenciar violaciones críticas

Compromete calidad y seguridad.

---

## Tratar SHACL como motor universal

SHACL resulta útil para validación, pero no sustituye todo el razonamiento.

---

## Validar únicamente al final

Los errores deben detectarse durante todo el pipeline.

---

## Mezclar conflicto con violación

Requieren tratamientos diferentes.

---

## Considerar toda contradicción un error

Algunas divergencias son legítimas o contextuales.

---

## Resolver automáticamente conflictos de alto impacto

Deben someterse a revisión.

---

## Aplicar mundo cerrado global

Provocaría inferencias negativas incorrectas.

---

## Cierres sin versión

Impiden determinar su vigencia.

---

## Utilizar predicciones como premisas críticas

No ofrecen garantías suficientes.

---

## Permitir inferencias sin validación posterior

Puede introducir inconsistencias en cadena.

---

## Ignorar permisos durante la explicación

Puede provocar fugas de información.

---

## Fallar en modo abierto en ámbitos críticos

Debe utilizarse fail-closed.

---

# Perfil mínimo de consistencia

La primera implementación podrá incluir:

- validación estructural;
- tipos;
- dominio;
- rango;
- cardinalidades;
- violaciones;
- conflictos positivos-negativos;
- prioridad básica;
- excepciones simples;
- resultados indeterminados;
- bloqueo de inferencias inválidas.

---

# Perfil estructurado

Añadirá:

- SHACL;
- conflictos entre reglas;
- políticas de resolución;
- cierres contextuales;
- validación incremental;
- pruebas de regresión;
- métricas.

---

# Perfil semántico

Añadirá:

- clases insatisfacibles;
- disjunciones;
- temporalidad;
- contexto compuesto;
- explicación de conflictos;
- múltiples justificaciones;
- validación global.

---

# Perfil avanzado

Añadirá:

- lógica no monotónica;
- incertidumbre calibrada;
- resolución semiautomática;
- simulación;
- políticas por dominio;
- pruebas de mutación;
- seguridad inferencial avanzada.

---

# Implementación inicial recomendada

La primera implementación práctica debería incorporar:

```text
Validación de reglas
+
Validación de hechos
+
Dominio y rango
+
Cardinalidades
+
Detección de contradicciones simples
+
Excepciones explícitas
+
Política de precedencia básica
+
Resultados indeterminados
+
Fail-closed para reglas críticas
+
Registro de violaciones y conflictos
+
Pruebas automáticas
```

No será necesario inicialmente implementar:

- lógica paraconsistente completa;
- argumentación formal;
- sistemas probabilísticos complejos;
- resolución automática de controversias;
- lógica difusa;
- negociación multiagente;
- cierres globales;
- validación distribuida.

---

# Arquitectura de consistencia

```text
┌───────────────────────────────────────────────┐
│                 Entradas                     │
│                                               │
│ Hechos · Reglas · Ontología · Contexto        │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│               Validación previa               │
│                                               │
│ Estructura · Tipos · Dominio · Rango          │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Ejecución inferencial             │
│                                               │
│ Matching · Activación · Conclusión             │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Validación posterior              │
│                                               │
│ Consistencia · Contexto · Tiempo · Seguridad  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Gestión de conflictos            │
│                                               │
│ Detección · Política · Resolución · Revisión  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                 Resultados                    │
│                                               │
│ Inferencias · Violaciones · Conflictos        │
└───────────────────────────────────────────────┘
```

---

# Conformidad de restricción

Una restricción será conforme cuando:

- tenga identidad;
- esté versionada;
- declare objetivo;
- defina severidad;
- pueda evaluarse;
- produzca un resultado explicable;
- tenga responsable;
- disponga de pruebas.

---

# Conformidad de violación

Una violación será conforme cuando:

- identifique la restricción;
- identifique el objetivo;
- conserve evidencia;
- declare severidad;
- tenga estado;
- pueda resolverse o suprimirse;
- sea auditable.

---

# Conformidad de conflicto

Un conflicto será conforme cuando:

- identifique los elementos incompatibles;
- declare tipo;
- conserve contextos y fuentes;
- indique severidad;
- no sobrescriba información;
- permita revisión;
- conserve resolución.

---

# Conformidad de excepción

Una excepción será conforme cuando:

- tenga alcance claro;
- se vincule con una regla o política;
- sea específica;
- tenga prioridad;
- conserve procedencia;
- esté versionada;
- posea vigencia cuando proceda.

---

# Conformidad de resolución

Una resolución será conforme cuando:

- utilice una política registrada;
- identifique los elementos seleccionados y descartados;
- conserve una justificación;
- respete contexto y autoridad;
- sea reproducible;
- quede auditada.

---

# Conformidad de validación

Una validación será conforme cuando:

- declare perfil;
- identifique versiones;
- registre restricciones aplicadas;
- produzca resultados tipados;
- diferencie errores y advertencias;
- preserve evidencias;
- sea reproducible.

---

# Lista de comprobación

Antes de aceptar una inferencia deberá comprobarse:

```text
[ ] Las premisas son válidas.
[ ] Las premisas están vigentes.
[ ] La regla está activa.
[ ] El contexto es compatible.
[ ] Las variables están correctamente enlazadas.
[ ] No se activa ninguna excepción bloqueante.
[ ] La conclusión respeta dominio y rango.
[ ] No existe una contradicción crítica.
[ ] La seguridad permite utilizar el resultado.
[ ] La procedencia está disponible.
[ ] La explicación puede generarse.
[ ] Las dependencias están registradas.
```

---

# Transición hacia la Parte V

Esta cuarta parte ha establecido:

- el modelo de consistencia;
- la validación estructural y ontológica;
- las restricciones;
- las violaciones;
- la detección de conflictos;
- las políticas de resolución;
- las excepciones;
- la negación;
- los cierres contextuales;
- la indeterminación;
- la incertidumbre;
- la degradación segura;
- los perfiles críticos;
- la validación temporal y contextual;
- las pruebas;
- las métricas;
- la observabilidad.

La Parte V desarrollará la forma en que el Razonador deberá hacer visibles y utilizables sus resultados mediante:

- explicaciones;
- árboles de justificación;
- trazabilidad;
- auditoría;
- APIs;
- eventos;
- integración con Knowledge Graph;
- integración con GraphRAG;
- integración con agentes;
- observabilidad;
- seguridad de acceso;
- rendimiento.

---

# Conclusión

La consistencia constituye una responsabilidad central del Razonador.

Un motor que produce muchas inferencias, pero no puede:

- validar sus premisas;
- detectar contradicciones;
- respetar el contexto;
- gestionar excepciones;
- explicar sus decisiones;
- abstenerse cuando faltan datos

no constituye un sistema fiable de razonamiento.

El SGCC deberá mantener siempre una distinción explícita entre:

```text
Conocimiento válido
```

```text
Conocimiento inválido
```

```text
Conocimiento contradictorio
```

```text
Conocimiento indeterminado
```

```text
Conocimiento contextual
```

```text
Conocimiento bloqueado
```

Las restricciones permitirán comprobar la integridad.

Las excepciones permitirán adaptar reglas generales.

Los cierres contextuales permitirán realizar inferencias negativas de forma controlada.

Las políticas de resolución permitirán gestionar contradicciones sin destruir información.

La degradación segura permitirá que el sistema falle de forma visible y conservadora.

Con esta cuarta parte queda definido el marco lógico de consistencia sobre el que podrán construirse explicaciones, servicios inferenciales, integraciones GraphRAG y herramientas para agentes sin comprometer la trazabilidad ni la calidad del conocimiento.

---

# Parte V — Explicabilidad, trazabilidad e integración

---

# Introducción

Las partes anteriores han definido:

- la arquitectura conceptual del Razonador;
- el modelo formal de hechos, reglas e inferencias;
- el pipeline operativo de ejecución;
- el matching y la unificación;
- la agenda y la planificación;
- el encadenamiento hacia delante y hacia atrás;
- la materialización y la invalidación;
- la consistencia;
- las restricciones;
- las excepciones;
- los conflictos;
- la validación.

Esta quinta parte establece cómo los resultados del Razonador deberán convertirse en capacidades utilizables por el resto del SGCC.

Una inferencia no será suficiente por el mero hecho de haber sido calculada.

Para que resulte operativamente útil deberá poder:

- identificarse;
- explicarse;
- consultarse;
- auditarse;
- publicarse;
- integrarse con el Knowledge Graph;
- incorporarse a procesos GraphRAG;
- utilizarse por agentes;
- exponerse mediante APIs;
- supervisarse mediante métricas;
- protegerse mediante permisos;
- invalidarse cuando cambien sus dependencias.

El Razonador no deberá funcionar como una caja negra.

Cada conclusión relevante deberá poder responder, al menos, a las siguientes preguntas:

```text
¿Qué se ha concluido?

¿Por qué?

¿A partir de qué premisas?

¿Mediante qué regla?

¿En qué contexto?

¿Con qué versión del conocimiento?

¿Con qué nivel de confianza?

¿Durante cuánto tiempo resulta válida?

¿Quién puede verla?

¿Qué ocurriría si cambiara una premisa?
```

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir el modelo de explicabilidad del Razonador;
- formalizar justificaciones y árboles inferenciales;
- establecer niveles de explicación;
- conservar trazabilidad completa;
- definir auditoría de reglas y ejecuciones;
- integrar inferencias con el Knowledge Graph;
- regular su materialización;
- integrar el Razonador con Colecciones;
- integrar el Razonador con GraphRAG;
- integrar el Razonador con agentes inteligentes;
- establecer contratos de APIs y herramientas;
- definir eventos y mecanismos de suscripción;
- regular observabilidad, rendimiento y seguridad;
- garantizar que toda conclusión pueda consumirse sin perder su naturaleza epistemológica.

---

# Principios de explicabilidad e integración

Toda integración deberá respetar los siguientes principios.

---

## Explicación obligatoria

Toda inferencia estable, crítica o materializada deberá disponer de una explicación mínima.

---

## Trazabilidad extremo a extremo

Deberá ser posible navegar desde una conclusión hasta:

- la ejecución;
- la regla;
- las premisas;
- las fuentes originales;
- el contexto;
- las versiones.

---

## Separación epistemológica

Las integraciones deberán distinguir entre:

```text
hecho explícito
hecho validado
inferencia
predicción
recomendación
hipótesis
violación
conflicto
```

---

## Contratos tipados

Las APIs, eventos y herramientas deberán devolver resultados estructurados.

No deberán reducir una inferencia a una frase sin metadatos.

---

## Explicación proporcional

El nivel de detalle deberá adaptarse al consumidor.

Un usuario final no necesita necesariamente la misma traza que un auditor.

---

## Seguridad de la explicación

Una explicación no deberá revelar premisas o fuentes no autorizadas.

---

## Reproducibilidad

Toda explicación técnica deberá identificar las versiones utilizadas.

---

## Integración no destructiva

Los consumidores no deberán transformar automáticamente una inferencia en conocimiento canónico.

---

## Independencia tecnológica

Los contratos conceptuales no dependerán de un framework o protocolo concreto.

---

## Observabilidad

Toda ejecución relevante deberá producir:

- logs;
- métricas;
- trazas;
- eventos;
- diagnósticos.

---

# Explicabilidad

La explicabilidad es la capacidad del Razonador para describir de forma comprensible y verificable cómo se ha obtenido un resultado.

No equivale únicamente a mostrar la regla aplicada.

Una explicación completa podrá incluir:

- objetivo;
- conclusión;
- premisas;
- bindings;
- condiciones;
- excepciones evaluadas;
- regla;
- ruleset;
- contexto;
- fuente;
- confianza;
- versión;
- alternativas descartadas;
- conflictos;
- limitaciones.

---

# Tipos de explicación

El SGCC podrá ofrecer diferentes tipos de explicación.

---

## Explicación causal-operativa

Describe qué elementos produjeron directamente la conclusión dentro del motor.

Ejemplo:

```text
La inferencia se generó porque se activó RULE-ALLERGEN-0001
con REC-0009, ING-0008 y ALG-SOY.
```

---

## Explicación lógica

Muestra la relación formal entre premisas y conclusión.

```text
Si una receta usa un ingrediente
y ese ingrediente contiene un alérgeno,
entonces la receta contiene ese alérgeno.
```

---

## Explicación documental

Indica qué documentos o fragmentos respaldan las premisas.

---

## Explicación ontológica

Muestra jerarquías, equivalencias o axiomas utilizados.

Ejemplo:

```text
El miso se considera ingrediente porque está clasificado como
IngredienteFermentado, que es subclase de Ingrediente.
```

---

## Explicación contextual

Aclara el ámbito de validez.

Ejemplo:

```text
La sustitución se considera adecuada únicamente para salsas frías.
```

---

## Explicación temporal

Describe:

- vigencia;
- intervalos;
- versiones;
- solapamientos;
- momento de cálculo.

---

## Explicación cuantitativa

Muestra:

- valores;
- unidades;
- fórmula;
- conversiones;
- redondeos;
- resultado.

---

## Explicación probabilística

Muestra:

- modelo;
- versión;
- probabilidad;
- umbral;
- señales;
- incertidumbre;
- calibración.

---

## Explicación contrastiva

Responde:

```text
¿Por qué A y no B?
```

Ejemplo:

```text
La receta se clasifica como vegetariana, pero no como vegana,
porque contiene huevo.
```

---

## Explicación contrafactual

Responde:

```text
¿Qué tendría que cambiar para que la conclusión fuera distinta?
```

Ejemplo:

```text
La receta podría clasificarse como vegana si el huevo
se sustituyera por un ingrediente compatible y se validara
la ausencia de otros productos animales.
```

---

## Explicación de ausencia

Responde:

```text
¿Por qué no puede demostrarse la conclusión?
```

Ejemplo:

```text
No puede determinarse si la receta es sin gluten
porque la lista de ingredientes no está declarada como completa.
```

---

## Explicación de conflicto

Describe:

- afirmaciones incompatibles;
- fuentes;
- contexto;
- política;
- estado de resolución.

---

## Explicación de bloqueo

Indica por qué una conclusión no puede producirse o mostrarse.

Ejemplos:

- falta de permisos;
- regla deshabilitada;
- conflicto crítico;
- datos insuficientes;
- política de seguridad.

---

# Niveles de explicación

El Razonador deberá poder ofrecer varios niveles de detalle.

```text
brief
standard
detailed
technical
audit
```

---

# Nivel breve

Adecuado para usuarios finales.

Ejemplo:

```text
La receta contiene soja porque utiliza miso.
```

---

# Nivel estándar

Incluye:

- conclusión;
- regla resumida;
- premisas principales;
- advertencias.

Ejemplo:

```text
La receta contiene soja porque utiliza miso y el miso
está clasificado como producto de soja.
```

---

# Nivel detallado

Añade:

- identificadores;
- fuentes;
- contexto;
- confianza;
- excepciones relevantes.

---

# Nivel técnico

Añade:

- bindings;
- activación;
- reglas;
- versiones;
- ejecución;
- dependencias;
- tiempos.

---

# Nivel auditoría

Añade:

- snapshot;
- hashes;
- permisos;
- logs;
- decisiones de conflicto;
- historial;
- artefactos compilados;
- identificadores de correlación.

---

# Perfil de explicación

Una solicitud podrá indicar:

```yaml
explanation:
  level: detailed
  include:
    - premises
    - sources
    - context
    - confidence
  language: es
```

---

# Explicación mínima normativa

Toda inferencia estable deberá incluir al menos:

- conclusión;
- regla;
- premisas;
- contexto relevante;
- versión;
- estado.

---

# Plantillas de explicación

Las reglas podrán declarar plantillas legibles.

Ejemplo:

```yaml
explanation:
  templates:
    brief:
      es: >
        La receta {recipe} contiene {allergen}
        porque utiliza {ingredient}.

    standard:
      es: >
        La receta {recipe} contiene {allergen} porque utiliza
        el ingrediente {ingredient}, que está registrado como
        contenedor de dicho alérgeno.
```

---

# Generación de explicaciones

La explicación podrá construirse mediante:

1. selección de inferencia;
2. recuperación de regla;
3. recuperación de bindings;
4. resolución de etiquetas;
5. recuperación de premisas;
6. aplicación de plantilla;
7. incorporación de contexto;
8. filtrado de seguridad;
9. validación del resultado.

---

# Explicación generada mediante IA

Un modelo de lenguaje podrá reformular una explicación estructurada.

Sin embargo:

- no deberá inventar premisas;
- no deberá alterar la conclusión;
- no deberá ocultar incertidumbre;
- deberá utilizar únicamente el paquete estructurado autorizado;
- deberá conservar referencias;
- la explicación formal seguirá siendo la fuente canónica.

---

# Representación formal de explicación

Formato recomendado:

```text
EXP-XXXXXX
```

---

## Contrato de explicación

```yaml
id: EXP-000041
type: inference_explanation

inference: INF-000041
level: detailed
language: es

conclusion:
  subject: REC-0009
  predicate: contains_allergen
  object: ALG-SOY

rule:
  id: RULE-ALLERGEN-0001
  version: 1.0.0

premises:
  - STM-000123
  - STM-000431

bindings:
  recipe: REC-0009
  ingredient: ING-0008
  allergen: ALG-SOY

context:
  recipe_version: 1.2.0

sources:
  - DOC-0051
  - DOC-0062

text: >
  La receta contiene soja porque utiliza miso,
  un ingrediente que contiene soja.

generated_at: 2026-08-01T18:30:00+02:00
```

---

# Árbol de justificación

Una inferencia simple podrá representarse mediante un árbol.

```text
INF-000041
│
├── RULE-ALLERGEN-0001
│
├── STM-000123
│   └── REC-0009 uses_ingredient ING-0008
│
└── STM-000431
    └── ING-0008 contains_allergen ALG-SOY
```

---

# Grafo de justificación

Cuando existan:

- múltiples reglas;
- inferencias intermedias;
- varias fuentes;
- justificaciones alternativas;

deberá utilizarse un grafo.

```text
STM-A ─┐
       ├── RULE-1 ── INF-X ─┐
STM-B ─┘                    │
                            ├── RULE-2 ── INF-Z
STM-C ──────────────────────┘
```

---

# Justificación directa

Utiliza únicamente hechos explícitos.

---

# Justificación indirecta

Utiliza una o más inferencias previas.

---

# Justificación alternativa

Varias rutas producen la misma conclusión.

---

# Justificación mínima

El motor podrá seleccionar la ruta más corta.

---

# Justificación preferida

Podrá seleccionarse por:

- autoridad;
- confianza;
- claridad;
- menor profundidad;
- menor coste;
- mayor actualidad;
- fuente primaria.

---

# Justificación completa

Incluye todos los caminos válidos.

Su uso será más apropiado para auditoría que para interfaces de usuario.

---

# Profundidad explicativa

Podrá limitarse:

```yaml
explanation:
  max_depth: 4
```

Cuando se alcance el límite deberá indicarse que existen dependencias adicionales.

---

# Explicación de condiciones

La explicación deberá poder indicar qué condiciones se evaluaron.

Ejemplo:

```text
La regla se activó porque la temperatura era 78 °C,
superior al mínimo de 75 °C.
```

---

# Explicación de excepciones

También deberá indicar si se evaluaron excepciones.

Ejemplo:

```text
La sustitución se propuso porque la preparación era una salsa fría
y no requería una estructura montada.
```

---

# Explicación de regla no activada

El sistema deberá poder explicar por qué una regla no produjo resultado.

Motivos posibles:

- premisa ausente;
- binding incompatible;
- condición falsa;
- excepción activa;
- contexto incompatible;
- regla deshabilitada;
- confianza insuficiente;
- permiso denegado;
- conflicto;
- límite alcanzado.

---

## Ejemplo

```yaml
rule_evaluation:
  rule: RULE-DIET-0014
  result: not_fired

  reasons:
    - code: INCOMPLETE_RELATION_SET
      property: uses_ingredient
```

---

# Explicación contrastiva formal

```yaml
contrastive_explanation:
  target: REC-0009

  accepted_classification:
    class: VegetarianRecipe
    inference: INF-000211

  rejected_classification:
    class: VeganRecipe

  reason:
    conflicting_fact:
      subject: REC-0009
      predicate: uses_ingredient
      object: ING-EGG
```

---

# Explicación contrafactual formal

```yaml
counterfactual:
  target_conclusion:
    subject: REC-0009
    predicate: suitable_for
    object: VeganDiet

  required_changes:
    - remove_relation:
        subject: REC-0009
        predicate: uses_ingredient
        object: ING-EGG

    - add_validated_substitution:
        original: ING-EGG
        substitute: ING-VEGAN-BINDER
```

Los contrafactuales deberán considerarse simulaciones, no modificaciones reales.

---

# Trazabilidad

La trazabilidad permite reconstruir el recorrido completo de un resultado.

Conceptualmente:

```text
Fuente
   ↓
Documento
   ↓
Afirmación
   ↓
Premisa
   ↓
Activación
   ↓
Regla
   ↓
Inferencia
   ↓
Materialización
   ↓
Consulta o respuesta
```

---

# Niveles de trazabilidad

---

## Trazabilidad documental

Conecta hechos con documentos y fragmentos.

---

## Trazabilidad semántica

Conecta hechos con clases, propiedades y axiomas.

---

## Trazabilidad inferencial

Conecta conclusiones con premisas y reglas.

---

## Trazabilidad operacional

Conecta resultados con ejecuciones, procesos y servicios.

---

## Trazabilidad temporal

Conecta cada elemento con:

- versión;
- vigencia;
- fecha de creación;
- fecha de modificación;
- snapshot.

---

## Trazabilidad de consumo

Permite conocer qué:

- consulta;
- respuesta;
- colección;
- índice;
- agente

utilizó una inferencia.

---

# Identificadores de correlación

Toda solicitud deberá poder utilizar un identificador de correlación.

```yaml
correlation:
  request_id: REQ-000145
  trace_id: TRACE-000921
```

Este identificador deberá propagarse a:

- Razonador;
- Knowledge Graph;
- APIs;
- GraphRAG;
- agentes;
- logs;
- eventos.

---

# Lineage

El `lineage` representa la cadena de derivación de un resultado.

---

## Contrato de lineage

```yaml
lineage:
  target: INF-000041

  chain:
    - type: source
      id: DOC-0051

    - type: statement
      id: STM-000123

    - type: activation
      id: ACT-000081

    - type: rule
      id: RULE-ALLERGEN-0001
      version: 1.0.0

    - type: execution
      id: RSN-EXEC-000145

    - type: inference
      id: INF-000041
```

---

# Trazabilidad de transformaciones

Cuando una representación sea transformada deberá registrarse:

- origen;
- destino;
- herramienta;
- versión;
- parámetros;
- hash;
- pérdidas conocidas.

---

# Trazabilidad de reglas compiladas

La regla compilada deberá enlazar con:

- regla canónica;
- versión;
- compilador;
- motor;
- fecha;
- hash.

---

# Trazabilidad de respuestas

Una respuesta GraphRAG o de agente deberá enlazar con las inferencias utilizadas.

Ejemplo:

```yaml
response_grounding:
  response: RSP-000091

  used_inferences:
    - INF-000041

  used_statements:
    - STM-000123
    - STM-000431

  used_documents:
    - DOC-0051
```

---

# Auditoría

La auditoría conserva evidencia inmutable sobre el comportamiento del Razonador.

---

# Eventos auditables

Deberán auditarse, como mínimo:

- creación de regla;
- modificación de regla;
- activación;
- inferencia;
- materialización;
- invalidación;
- resolución de conflicto;
- supresión de violación;
- cambio de perfil;
- ejecución crítica;
- consulta sensible;
- exportación;
- acción de agente.

---

# Registro de auditoría

Formato recomendado:

```text
AUD-RSN-XXXXXX
```

---

## Contrato de evento de auditoría

```yaml
id: AUD-RSN-000145
type: inference_materialized

timestamp: 2026-08-01T18:45:00+02:00

actor:
  type: system
  id: SGCC-REASONER

target:
  type: inference
  id: INF-000041

execution: RSN-EXEC-000145
trace_id: TRACE-000921

rule:
  id: RULE-ALLERGEN-0001
  version: 1.0.0

graph_snapshot: KG-SNAP-20260801-001

result:
  status: success

hash: sha256:...
```

---

# Auditoría inmutable

Los eventos de auditoría no deberán editarse.

Una corrección deberá registrarse como un nuevo evento.

---

# Auditoría de decisiones

Toda decisión de:

- suprimir;
- bloquear;
- resolver;
- invalidar;
- aceptar;

deberá conservar:

- política;
- actor;
- motivo;
- evidencia;
- fecha.

---

# Auditoría de reglas probabilísticas

Deberá registrar además:

- modelo;
- versión;
- parámetros;
- umbral;
- puntuación;
- calibración;
- entrada.

---

# Auditoría de explicaciones generadas

Cuando una explicación sea reformulada por IA deberán registrarse:

- explicación formal de origen;
- modelo;
- versión;
- prompt o plantilla;
- resultado;
- validación posterior.

---

# Integración con el Knowledge Graph

El Knowledge Graph proporciona hechos al Razonador y puede recibir inferencias materializadas.

La relación deberá ser bidireccional, pero gobernada.

```text
Knowledge Graph
      │
      ├── hechos explícitos
      ├── hechos validados
      ├── contexto
      └── procedencia
      │
      ▼
Razonador
      │
      ├── inferencias
      ├── violaciones
      ├── conflictos
      └── explicaciones
      │
      ▼
Knowledge Graph derivado
```

---

# Capas del grafo

Las inferencias no deberán mezclarse con hechos explícitos.

Capas recomendadas:

```text
graph:explicit
graph:validated
graph:inferred
graph:predicted
graph:hypothetical
graph:violations
graph:conflicts
```

---

# Materialización como afirmación

Una inferencia materializada podrá representarse como afirmación enriquecida.

Ejemplo:

```text
REC-0009 contains_allergen ALG-SOY
```

con propiedades:

- `inferred = true`;
- `rule = RULE-ALLERGEN-0001`;
- `execution = RSN-EXEC-000145`;
- `confidence = 1.0`;
- `status = active`.

---

# Materialización mediante nodo de inferencia

Cuando se necesite mayor detalle podrá utilizarse:

```text
INF-000041
    │
    ├── concludes → Statement
    ├── uses_premise → STM-000123
    ├── uses_premise → STM-000431
    ├── generated_by → RULE-ALLERGEN-0001
    └── generated_in → RSN-EXEC-000145
```

---

# Materialización mediante RDF-star

Ejemplo conceptual:

```turtle
<< :REC-0009 :containsAllergen :ALG-SOY >>
    :inferredBy :RULE-ALLERGEN-0001 ;
    :generatedIn :RSN-EXEC-000145 ;
    :confidence 1.0 ;
    :status :active .
```

---

# Materialización en grafos de propiedades

Podrá representarse mediante una arista enriquecida o un nodo de inferencia.

---

# Política de materialización

Cada ruleset podrá declarar:

```text
none
ephemeral
selective
full
```

---

## Sin materialización

Las inferencias se calculan bajo demanda.

---

## Materialización efímera

Se conserva temporalmente.

---

## Materialización selectiva

Solo se persisten inferencias relevantes.

---

## Materialización completa

Se persisten todas las conclusiones dentro del ámbito.

Su uso deberá justificarse por coste y necesidad.

---

# Identidad de inferencia materializada

La identidad deberá ser estable mientras no cambien:

- conclusión;
- contexto;
- regla;
- bindings;
- versión.

---

# Actualización de materializaciones

Una nueva ejecución podrá:

- reutilizar;
- confirmar;
- actualizar;
- invalidar;
- sustituir

una inferencia existente.

---

# Estado en el Knowledge Graph

Valores posibles:

```text
active
stale
invalidated
superseded
archived
```

---

# Escritura transaccional

La materialización deberá realizarse de forma atómica.

No deberá quedar:

- la inferencia sin dependencias;
- la conclusión sin procedencia;
- la explicación sin inferencia;
- la auditoría sin resultado.

---

# Rollback

Si falla la materialización deberá revertirse toda la operación.

---

# Integración con Colecciones de Conocimiento

Las Colecciones podrán utilizar el Razonador para:

- calcular miembros;
- validar criterios;
- aplicar exclusiones;
- clasificar entidades;
- generar métricas;
- detectar deuda;
- explicar pertenencias.

---

# Pertenencia inferida

Ejemplo:

```text
REC-0009 pertenece a COL-VEGETARIAN
```

porque:

- su lista de ingredientes está completa;
- todos los ingredientes son compatibles;
- no se activa ninguna excepción.

---

# Explicación de pertenencia

La colección deberá poder mostrar:

```text
La receta pertenece a esta colección porque cumple
RULE-DIET-0014 y RULE-COLLECTION-0003.
```

---

# Colección como ámbito

Una ejecución podrá limitarse a:

```yaml
scope:
  collection: COL-0001
```

El Fact Provider solo recuperará hechos necesarios para ese dominio.

---

# Colección como activador de rulesets

Ejemplo:

```yaml
collection_reasoning:
  collection: COL-0001

  rulesets:
    - RS-JAPANESE-CUISINE
    - RS-RECIPES
```

---

# Colección dinámica

Una colección podrá resolverse mediante inferencias.

La resolución deberá registrar:

- versión de colección;
- snapshot del grafo;
- rulesets;
- inferencias;
- fecha;
- hash.

---

# Invalidación de colecciones

Cuando cambie una inferencia de pertenencia deberán actualizarse:

- miembros;
- snapshots;
- métricas;
- índices;
- vistas;
- agentes dependientes.

---

# Integración con GraphRAG

El Razonador podrá enriquecer GraphRAG mediante:

- clasificación de intención;
- resolución de restricciones;
- inferencias;
- selección de caminos;
- validación de respuestas;
- explicación;
- detección de incompatibilidades.

---

# Flujo Reasoner + GraphRAG

```text
Pregunta
    │
    ▼
Resolución de entidades
    │
    ▼
Consulta de hechos
    │
    ▼
Razonamiento bajo demanda
    │
    ▼
Subgrafo inferencial
    │
    ▼
Recuperación documental
    │
    ▼
Construcción de contexto
    │
    ▼
Generación
    │
    ▼
Validación de respuesta
```

---

# Inferencias como contexto

El paquete GraphRAG deberá distinguir:

```yaml
context:
  explicit_facts:
    - STM-000123

  inferred_facts:
    - INF-000041

  conflicts: []

  constraints:
    - CONSTRAINT-SAFETY-0012
```

---

# Razonamiento previo a recuperación

El Razonador podrá:

- expandir una consulta;
- detectar entidades implícitas;
- determinar restricciones;
- seleccionar una colección;
- activar reglas de ámbito.

---

# Razonamiento durante recuperación

Podrá:

- validar caminos;
- filtrar relaciones incompatibles;
- priorizar fuentes;
- detectar contradicciones;
- obtener inferencias intermedias.

---

# Razonamiento posterior a recuperación

Podrá:

- comprobar si los chunks respaldan la respuesta;
- detectar conclusiones no fundamentadas;
- validar restricciones;
- comprobar seguridad;
- generar explicación.

---

# Grounding inferencial

Una respuesta podrá apoyarse en una inferencia si:

- la inferencia está activa;
- posee premisas accesibles;
- la regla es compatible con el perfil;
- la explicación está disponible;
- la versión está registrada.

---

# Citas de inferencias

Una respuesta deberá citar preferentemente:

- las fuentes de las premisas;
- la regla;
- la inferencia cuando proceda.

No bastará con citar únicamente el texto generado.

---

# Abstención GraphRAG

El Razonador podrá indicar:

```yaml
answerability:
  status: insufficient_evidence
```

GraphRAG deberá respetar esta indicación y abstenerse o pedir más información.

---

# Validación de respuesta generada

La respuesta podrá descomponerse en afirmaciones candidatas.

Cada una podrá clasificarse como:

- respaldada explícitamente;
- respaldada inferencialmente;
- recomendación;
- hipótesis;
- no respaldada;
- contradictoria.

---

# Contrato de verificación

```yaml
response_validation:
  response: RSP-000091

  claims:
    - id: CLAIM-0001
      status: supported_by_inference
      support:
        - INF-000041

    - id: CLAIM-0002
      status: unsupported

  overall_status: failed
```

---

# Integración con agentes inteligentes

Los agentes utilizarán el Razonador como servicio especializado.

El agente no deberá reimplementar reglas críticas dentro de prompts.

---

# Herramientas conceptuales

```text
reason
validate
classify
explain
simulate
check_constraints
detect_conflicts
compare_scenarios
```

---

# Herramienta `reason`

Entrada:

- objetivo;
- hechos;
- ámbito;
- rulesets;
- contexto;
- perfil.

Salida:

- conclusiones;
- conflictos;
- explicaciones;
- advertencias.

---

# Herramienta `validate`

Comprueba un elemento o conjunto de elementos.

---

# Herramienta `classify`

Devuelve clasificaciones inferidas.

---

# Herramienta `explain`

Recupera una explicación existente.

---

# Herramienta `simulate`

Ejecuta cambios hipotéticos sin materializar.

---

# Herramienta `compare_scenarios`

Compara dos conjuntos de hechos o contextos.

---

# Contrato de herramienta

```yaml
tool:
  id: TOOL-RSN-REASON
  name: reason
  version: 1.0.0

  input:
    scope:
      type: object

    goals:
      type: array

    profile:
      enum:
        - strict
        - standard
        - exploratory

  output:
    conclusions:
      type: array

    conflicts:
      type: array

    explanations:
      type: array

  permissions:
    - reasoner_execute
```

---

# Herramientas de solo lectura

Las herramientas de razonamiento deberán ser de solo lectura por defecto.

---

# Herramientas con materialización

La materialización requerirá permiso adicional.

```text
reasoner_materialize
```

---

# Herramientas de simulación

Deberán operar sobre:

- snapshot;
- espacio aislado;
- contexto hipotético.

---

# Agentes y resultados tipados

El agente deberá conservar el tipo de resultado.

Ejemplo:

```yaml
agent_observation:
  type: inference
  id: INF-000041
```

No deberá convertirlo internamente en:

```text
hecho explícito
```

---

# Agentes y explicación

Antes de ejecutar una acción basada en una inferencia crítica, el agente deberá poder solicitar su explicación.

---

# Agentes y conflictos

Cuando el Razonador devuelva:

```text
conflicted
```

el agente no deberá escoger silenciosamente una conclusión.

Deberá:

- informar;
- pedir decisión;
- aplicar una política autorizada;
- abstenerse.

---

# Agentes y restricciones

El Razonador podrá actuar como guardrail semántico.

Ejemplo:

```text
El agente propone una sustitución.
```

El Razonador valida:

- alérgenos;
- dieta;
- técnica;
- disponibilidad;
- contexto.

---

# Planificación asistida

El Razonador podrá comprobar:

- precondiciones;
- dependencias;
- efectos;
- incompatibilidades.

Ejemplo:

```text
No iniciar horneado antes de finalizar precalentamiento.
```

---

# Acciones propuestas

El Razonador no ejecutará directamente acciones externas.

Producirá:

```text
ProposedAction
```

o:

```text
ActionConstraint
```

---

# Integración mediante APIs

El Razonador podrá exponerse mediante una API especializada.

---

# Recursos principales

```text
/reasoning/execute
/reasoning/validate
/reasoning/classify
/reasoning/simulate
/reasoning/explain/{id}
/reasoning/inferences/{id}
/reasoning/executions/{id}
/reasoning/conflicts/{id}
/reasoning/rules
/reasoning/rulesets
```

---

# Ejecutar razonamiento

```http
POST /api/v1/reasoning/execute
```

---

## Solicitud conceptual

```json
{
  "scope": {
    "collection": "COL-0001"
  },
  "rulesets": [
    "RS-ALLERGENS"
  ],
  "goals": [
    {
      "subject": "REC-0009",
      "predicate": "contains_allergen"
    }
  ],
  "profile": "strict",
  "explanation": {
    "level": "standard"
  }
}
```

---

## Respuesta conceptual

```json
{
  "executionId": "RSN-EXEC-000145",
  "status": "completed",
  "conclusions": [
    {
      "id": "INF-000041",
      "type": "deterministic_inference",
      "subject": "REC-0009",
      "predicate": "contains_allergen",
      "object": "ALG-SOY",
      "confidence": 1.0
    }
  ],
  "conflicts": [],
  "violations": [],
  "links": {
    "execution": "/api/v1/reasoning/executions/RSN-EXEC-000145",
    "explanation": "/api/v1/reasoning/explain/INF-000041"
  }
}
```

---

# Validar conocimiento

```http
POST /api/v1/reasoning/validate
```

Podrá recibir:

- entidad;
- documento;
- regla;
- subgrafo;
- colección;
- inferencia.

---

# Clasificar entidad

```http
POST /api/v1/reasoning/classify
```

---

# Simular cambios

```http
POST /api/v1/reasoning/simulate
```

La simulación deberá indicar claramente:

```text
not_materialized
```

---

# Recuperar explicación

```http
GET /api/v1/reasoning/explain/INF-000041?level=detailed
```

---

# Recuperar ejecución

```http
GET /api/v1/reasoning/executions/RSN-EXEC-000145
```

---

# Listar reglas

```http
GET /api/v1/reasoning/rules
```

Filtros posibles:

- ruleset;
- status;
- authority;
- version;
- domain;
- owner.

---

# API síncrona

Adecuada para:

- consultas pequeñas;
- validaciones locales;
- explicaciones;
- clasificación simple.

---

# API asíncrona

Adecuada para:

- ejecución masiva;
- validación global;
- materialización;
- simulaciones complejas;
- reconstrucción.

---

## Respuesta asíncrona

```http
202 Accepted
```

```json
{
  "jobId": "RSN-JOB-00041",
  "status": "queued"
}
```

---

# Idempotencia API

Las solicitudes de materialización deberán admitir una clave de idempotencia.

```http
Idempotency-Key: ...
```

---

# Paginación

Será necesaria para:

- inferencias;
- conflictos;
- violaciones;
- activaciones;
- auditoría.

---

# Versionado de API

Las APIs deberán versionarse.

```text
/api/v1/
```

Los cambios semánticos incompatibles requerirán nueva versión mayor.

---

# Errores de API

Ejemplos:

```text
RULESET_NOT_FOUND
INCOMPATIBLE_VERSION
INVALID_CONTEXT
EXECUTION_LIMIT_EXCEEDED
UNAUTHORIZED_PREMISE
CONFLICT_BLOCKED
INSUFFICIENT_EVIDENCE
```

---

# Contrato de error

```json
{
  "error": {
    "code": "INSUFFICIENT_EVIDENCE",
    "message": "No puede demostrarse la conclusión.",
    "details": {
      "missingRequirement": "complete_ingredient_list"
    },
    "traceId": "TRACE-000921"
  }
}
```

---

# Integración con MCP

El Razonador podrá exponerse mediante herramientas y recursos MCP.

---

# Recursos conceptuales

```text
reasoning://rules/RULE-ALLERGEN-0001
reasoning://rulesets/RS-ALLERGENS
reasoning://inferences/INF-000041
reasoning://executions/RSN-EXEC-000145
reasoning://conflicts/CNF-000021
```

---

# Herramientas MCP conceptuales

```text
reason_over_graph
validate_entity
classify_entity
explain_inference
simulate_changes
detect_conflicts
```

---

# Contrato de MCP

Las herramientas deberán:

- validar entradas;
- aplicar permisos;
- limitar coste;
- devolver estructuras tipadas;
- conservar identificadores;
- incluir advertencias;
- registrar auditoría.

---

# Integración mediante eventos

El Razonador podrá publicar y consumir eventos.

---

# Eventos de entrada

Ejemplos:

```text
statement_created
statement_updated
statement_invalidated
rule_published
rule_deprecated
ontology_updated
collection_resolved
snapshot_created
```

---

# Eventos de salida

Ejemplos:

```text
reasoning_started
reasoning_completed
inference_created
inference_materialized
inference_invalidated
violation_detected
conflict_detected
explanation_generated
```

---

# Contrato de evento

```yaml
event:
  id: EVT-000145
  type: inference_created
  version: 1.0

  timestamp: 2026-08-01T19:00:00+02:00
  trace_id: TRACE-000921

  payload:
    inference: INF-000041
    execution: RSN-EXEC-000145
    rule: RULE-ALLERGEN-0001
```

---

# Entrega de eventos

Podrá ser:

- al menos una vez;
- como máximo una vez;
- exactamente una vez lógica mediante idempotencia.

La política deberá declararse.

---

# Orden de eventos

No deberá asumirse orden global.

Cuando sea necesario deberán utilizarse:

- secuencia;
- versión;
- timestamp;
- causalidad.

---

# Eventos duplicados

Los consumidores deberán ser idempotentes.

---

# Eventos fallidos

Deberán utilizar:

- reintentos;
- dead-letter queue;
- alertas;
- auditoría.

---

# Integración con procesos batch

El Razonador podrá ejecutar trabajos periódicos para:

- recalcular inferencias;
- validar módulos;
- detectar conflictos;
- actualizar colecciones;
- generar informes.

---

# Programación

Los trabajos deberán declarar:

- frecuencia;
- ámbito;
- snapshot;
- rulesets;
- límites;
- propietario.

---

# Integración con CI/CD

El pipeline documental o semántico podrá ejecutar:

```text
Validación de reglas
↓
Compilación
↓
Pruebas
↓
Validación sobre snapshot
↓
Comparación de inferencias
↓
Quality Gate
```

---

# Quality Gate inferencial

Un cambio deberá bloquearse cuando:

- aparezcan conflictos críticos;
- cambien golden cases sin aprobación;
- se pierdan explicaciones;
- aumenten inferencias inválidas;
- se rompa compatibilidad;
- falle seguridad.

---

# Informe de impacto

Antes de publicar una regla deberá generarse:

```yaml
impact_report:
  rule: RULE-DIET-0014
  from_version: 1.0.0
  to_version: 2.0.0

  affected_inferences: 214
  affected_collections: 3
  affected_queries: 5
  affected_rag_indexes: 2

  compatibility: incompatible
```

---

# Observabilidad

La observabilidad deberá cubrir:

- ejecución;
- reglas;
- inferencias;
- conflictos;
- APIs;
- eventos;
- materialización;
- integraciones.

---

# Logs

Cada log deberá incluir, cuando proceda:

- timestamp;
- nivel;
- ejecución;
- regla;
- inferencia;
- trace_id;
- usuario o agente;
- duración;
- resultado.

---

# Log estructurado

```yaml
log:
  level: INFO
  event: rule_fired
  execution: RSN-EXEC-000145
  rule: RULE-ALLERGEN-0001
  activation: ACT-000081
  inference: INF-000041
  duration_ms: 2
```

---

# Niveles de log

```text
TRACE
DEBUG
INFO
WARN
ERROR
CRITICAL
```

---

# Datos sensibles en logs

No deberán registrarse:

- secretos;
- datos personales innecesarios;
- contenido restringido completo;
- tokens;
- credenciales.

---

# Métricas de ejecución

Ejemplos:

- ejecuciones totales;
- duración media;
- p50;
- p95;
- p99;
- reglas evaluadas;
- reglas activadas;
- inferencias generadas;
- inferencias materializadas;
- profundidad;
- timeouts.

---

# Métricas de explicación

Ejemplos:

- explicaciones generadas;
- tiempo de generación;
- inferencias sin explicación;
- profundidad media;
- explicaciones filtradas por permisos;
- explicaciones fallidas.

---

# Métricas de integración

Ejemplos:

- llamadas API;
- errores;
- eventos publicados;
- eventos fallidos;
- consultas GraphRAG asistidas;
- acciones de agentes validadas;
- materializaciones.

---

# Métricas de caché

- hit rate;
- miss rate;
- invalidaciones;
- tamaño;
- antigüedad;
- entradas por ruleset.

---

# Métricas de calidad

- inferencias activas;
- inferencias obsoletas;
- conflictos abiertos;
- violaciones críticas;
- reglas sin cobertura;
- explicaciones incompletas;
- resultados indeterminados.

---

# Trazas distribuidas

Una traza podrá incluir:

```text
API Gateway
↓
Reasoning Service
↓
Knowledge Graph
↓
Rule Registry
↓
Explanation Service
↓
Materialization Service
```

---

# Spans

Cada componente deberá crear spans para:

- carga de hechos;
- compilación;
- matching;
- planificación;
- ejecución;
- validación;
- explicación;
- persistencia.

---

# Alertas

Ejemplos:

- aumento de latencia;
- crecimiento anómalo de inferencias;
- reglas que nunca se activan;
- conflictos críticos;
- inferencias obsoletas;
- fallos de materialización;
- cola de eventos bloqueada;
- degradación de caché.

---

# Dashboards

Podrán mostrar:

- estado del Razonador;
- ejecuciones recientes;
- rulesets activos;
- inferencias por dominio;
- conflictos;
- violaciones;
- rendimiento;
- calidad;
- uso por GraphRAG;
- uso por agentes.

---

# Rendimiento

El Razonador deberá equilibrar:

- corrección;
- explicabilidad;
- latencia;
- coste;
- memoria.

La optimización nunca deberá eliminar trazabilidad esencial.

---

# Factores de coste

El coste dependerá de:

- número de hechos;
- número de reglas;
- cardinalidad de patrones;
- profundidad;
- contexto;
- funciones;
- agregaciones;
- materialización;
- explicación.

---

# Presupuesto de explicación

Las explicaciones completas pueden ser costosas.

Podrán generarse:

- bajo demanda;
- de forma diferida;
- parcialmente;
- desde artefactos precomputados.

---

# Caché de explicaciones

Podrá utilizarse cuando no hayan cambiado:

- inferencia;
- regla;
- premisas;
- etiquetas;
- permisos;
- idioma;
- nivel.

---

# Clave de caché

```text
inference
+
version
+
language
+
level
+
permissions
```

---

# Caché de inferencias

La clave deberá incluir:

- snapshot;
- ruleset;
- contexto;
- perfil;
- objetivo;
- permisos.

---

# Invalidación de caché

Deberá producirse cuando cambie cualquier dependencia relevante.

---

# Ejecución asíncrona

Las operaciones costosas deberán ejecutarse mediante trabajos.

---

# Colas

Podrán utilizarse para:

- materialización;
- invalidación masiva;
- explicación de auditoría;
- reconstrucción;
- validación global.

---

# Prioridades de cola

Ejemplo:

```text
critical
high
normal
low
batch
```

---

# Cancelación

Una ejecución deberá poder cancelarse.

La cancelación deberá:

- detener nuevas activaciones;
- conservar auditoría;
- revertir materializaciones parciales;
- marcar el estado.

---

# Timeouts

Los límites podrán aplicarse a:

- solicitud;
- regla;
- función;
- explicación;
- consulta externa.

---

# Degradación por rendimiento

Cuando se alcance un límite, el sistema podrá:

- devolver resultado parcial;
- marcar incompletitud;
- reducir nivel de explicación;
- omitir rulesets opcionales;
- ejecutar asíncronamente;
- abstenerse.

---

# Resultado parcial

Deberá declararse explícitamente.

```yaml
execution:
  status: partial

  reason:
    code: EXECUTION_BUDGET_EXCEEDED

  completeness:
    rules_evaluated_ratio: 0.82
```

---

# Seguridad

La integración del Razonador deberá aplicar seguridad en todas las capas.

---

# Autenticación

Toda ejecución no pública deberá identificar al actor.

---

# Autorización

Podrán existir permisos como:

```text
reasoner_read
reasoner_execute
reasoner_explain
reasoner_audit
reasoner_simulate
reasoner_materialize
reasoner_admin
```

---

# Seguridad por ruleset

Algunos rulesets podrán ser:

- públicos;
- internos;
- restringidos;
- críticos.

---

# Seguridad por inferencia

Una inferencia podrá heredar la sensibilidad máxima de sus premisas.

---

# Etiqueta de sensibilidad

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

# Propagación de sensibilidad

Ejemplo:

```text
Premisa A: interna
Premisa B: restringida
```

Resultado:

```text
Inferencia: restringida
```

---

# Explicación segura

Una explicación podrá redaccionarse.

Ejemplo:

```yaml
explanation:
  level: standard
  redacted: true

  text: >
    La conclusión se deriva de conocimiento interno validado.

  hidden_elements:
    - STM-PRIVATE-001
```

---

# Seguridad de reglas

Algunas reglas podrán contener lógica interna sensible.

El usuario podrá recibir la explicación funcional sin acceder al artefacto completo.

---

# Seguridad de simulaciones

Las simulaciones deberán ejecutarse en un entorno aislado y no afectar a:

- grafo canónico;
- materializaciones;
- caché compartida;
- eventos de producción.

---

# Seguridad de APIs

Deberán aplicarse:

- validación de entrada;
- límites;
- autorización;
- protección frente a inyección;
- rate limiting;
- auditoría.

---

# Inyección en expresiones

Las entradas no deberán convertirse en código ejecutable.

---

# Seguridad de agentes

Los agentes deberán utilizar herramientas registradas.

No deberán poder:

- modificar reglas;
- elevar permisos;
- materializar inferencias;
- ocultar conflictos

sin autorización.

---

# Ámbitos críticos

En:

- alérgenos;
- seguridad alimentaria;
- toxicidad;
- privacidad;
- publicación canónica;

se requerirá:

- perfil estricto;
- fail-closed;
- fuentes validadas;
- explicación;
- auditoría;
- permisos reforzados.

---

# Privacidad

El Razonador podrá operar sobre preferencias personales.

Estas deberán mantenerse en ámbitos separados.

---

# Inferencias personales

Ejemplo:

```text
Esta receta no se recomienda al usuario porque evita cilantro.
```

No deberá incorporarse al conocimiento global.

---

# Retención

Las ejecuciones personales deberán disponer de política de retención.

---

# Minimización

Solo deberán recuperarse los datos personales necesarios para la inferencia.

---

# Conformidad de explicación

Una explicación será conforme cuando:

- identifique la conclusión;
- identifique la regla;
- identifique premisas;
- conserve contexto;
- declare versión;
- respete permisos;
- no invente información;
- pueda vincularse con la ejecución.

---

# Conformidad de trazabilidad

La trazabilidad será conforme cuando permita recorrer:

```text
Conclusión
→ ejecución
→ regla
→ premisas
→ afirmaciones
→ fuentes
```

---

# Conformidad de materialización

Una materialización será conforme cuando:

- separe inferencias de hechos explícitos;
- conserve identidad;
- registre dependencias;
- sea transaccional;
- pueda invalidarse;
- mantenga auditoría;
- respete permisos.

---

# Conformidad de API

Una API será conforme cuando:

- utilice contratos versionados;
- devuelva resultados tipados;
- incluya identificadores;
- preserve trazabilidad;
- gestione errores;
- aplique límites;
- respete autorización.

---

# Conformidad de evento

Un evento será conforme cuando:

- tenga identificador;
- declare versión;
- incluya timestamp;
- conserve causalidad;
- sea idempotente;
- permita reintento;
- respete sensibilidad.

---

# Conformidad GraphRAG

La integración será conforme cuando:

- diferencie hechos e inferencias;
- conserve fuentes;
- use versiones;
- permita abstención;
- valide respuestas;
- respete permisos;
- registre las inferencias utilizadas.

---

# Conformidad de agente

La integración será conforme cuando:

- el agente utilice herramientas registradas;
- preserve tipos de resultado;
- no transforme inferencias en hechos;
- respete conflictos;
- solicite explicación cuando proceda;
- no materialice sin permiso;
- audite acciones.

---

# Lista de comprobación

Antes de exponer una inferencia deberá verificarse:

```text
[ ] La inferencia está activa.
[ ] La regla está identificada y versionada.
[ ] Las premisas siguen siendo válidas.
[ ] La explicación mínima está disponible.
[ ] El contexto está declarado.
[ ] La sensibilidad está calculada.
[ ] El consumidor dispone de permisos.
[ ] La versión del grafo está identificada.
[ ] La conclusión está tipada.
[ ] No existe un conflicto bloqueante.
[ ] La trazabilidad alcanza las fuentes.
[ ] La salida diferencia hecho e inferencia.
```

---

# Antipatrones de explicabilidad e integración

Deberán evitarse los siguientes antipatrones.

---

## Explicación generada sin estructura formal

Puede inventar razones inexistentes.

---

## Mostrar solo la regla

No demuestra que las premisas concretas se hayan satisfecho.

---

## Ocultar el contexto

Puede convertir una conclusión limitada en una afirmación universal.

---

## Perder bindings

Impide reproducir la activación concreta.

---

## Explicaciones técnicas para todos los usuarios

Reduce comprensión y utilidad.

---

## Explicaciones simplificadas que alteran el significado

La simplificación no deberá eliminar condiciones esenciales.

---

## Exponer premisas restringidas

Puede provocar fugas de información.

---

## Materializar inferencias en la capa explícita

Destruye la separación epistemológica.

---

## Guardar solo la conclusión

Impide invalidación y auditoría.

---

## Integrar reglas críticas únicamente en prompts

Reduce gobernanza y reproducibilidad.

---

## Permitir que GraphRAG ignore conflictos

Puede generar respuestas incorrectas.

---

## Permitir que agentes resuelvan conflictos sin política

Introduce decisiones no gobernadas.

---

## APIs que devuelven solo texto

Pierden metadatos, estado y procedencia.

---

## Eventos sin versión

Dificultan evolución de consumidores.

---

## Caché sin permisos

Puede provocar exposición indebida.

---

## Logs con datos sensibles

Comprometen privacidad.

---

## Métricas sin contexto

Pueden interpretarse de forma incorrecta.

---

## Optimizar eliminando trazabilidad

La mejora de rendimiento no deberá impedir explicación.

---

## Materializaciones parciales no transaccionales

Pueden dejar estados inconsistentes.

---

## Simulaciones que contaminan producción

Deben operar en ámbitos aislados.

---

## Explicaciones sin señalar indeterminación

Pueden aparentar certeza inexistente.

---

# Perfil mínimo de integración

La primera implementación podrá incluir:

- explicación breve y técnica;
- identificación de regla y premisas;
- lineage básico;
- auditoría de ejecución;
- materialización separada;
- API síncrona de lectura;
- integración con Knowledge Graph;
- integración GraphRAG de solo lectura;
- herramientas de agente de consulta;
- métricas básicas.

---

# Perfil estructurado

Añadirá:

- grafos de justificación;
- explicaciones contrastivas;
- API asíncrona;
- eventos;
- materialización selectiva;
- trazas distribuidas;
- caché;
- seguridad por capa.

---

# Perfil semántico

Añadirá:

- explicación ontológica;
- contexto compuesto;
- lineage completo;
- validación de respuestas;
- múltiples justificaciones;
- integración dinámica con colecciones.

---

# Perfil avanzado

Añadirá:

- explicaciones contrafactuales;
- reformulación mediante IA;
- simulación compleja;
- razonamiento interactivo;
- integración multiagente;
- seguridad inferencial avanzada;
- auditoría criptográfica.

---

# Implementación inicial recomendada

La primera implementación práctica debería incorporar:

```text
Explicación basada en regla y premisas
+
Árbol de justificación
+
Lineage hasta documentos
+
Auditoría de ejecuciones
+
Materialización en capa inferida
+
API /reason
+
API /validate
+
API /explain
+
Herramientas de solo lectura para agentes
+
Integración GraphRAG controlada
+
Métricas y logs estructurados
```

No será necesario implementar inicialmente:

- explicación contrafactual automática;
- reformulación mediante modelos generativos;
- event streaming distribuido;
- auditoría criptográfica;
- ejecución multiagente;
- materialización completa;
- explicaciones visuales avanzadas;
- razonamiento interactivo continuo.

---

# Arquitectura de integración

```text
┌───────────────────────────────────────────────┐
│             Fuentes del razonamiento          │
│                                               │
│ Knowledge Graph · Ontología · Rulesets        │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                 Razonador                     │
│                                               │
│ Ejecución · Validación · Conflictos           │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│       Explicabilidad y trazabilidad            │
│                                               │
│ Justificaciones · Lineage · Auditoría          │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Capa de integración               │
│                                               │
│ APIs · Eventos · MCP · Materialización         │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                 Consumidores                  │
│                                               │
│ Colecciones · GraphRAG · Agentes · Aplicaciones│
└───────────────────────────────────────────────┘
```

---

# Flujo completo de una inferencia consumible

```text
Hechos
  │
  ▼
Activación
  │
  ▼
Regla
  │
  ▼
Inferencia
  │
  ▼
Validación
  │
  ▼
Explicación
  │
  ▼
Auditoría
  │
  ▼
Materialización
  │
  ▼
API / GraphRAG / Agente
```

---

# Caso de uso 1 — Explicar un alérgeno

Pregunta:

```text
¿Por qué esta receta contiene soja?
```

Flujo:

```text
Resolver receta
↓
Localizar inferencia activa
↓
Recuperar regla
↓
Recuperar premisas
↓
Recuperar documentos
↓
Aplicar plantilla
↓
Filtrar permisos
↓
Devolver explicación
```

---

# Caso de uso 2 — Validar una respuesta GraphRAG

Respuesta generada:

```text
La receta es vegana.
```

El Razonador comprueba:

- lista completa de ingredientes;
- clasificación de ingredientes;
- excepciones;
- contaminación cruzada;
- conflictos.

Resultado:

```text
indeterminado
```

La respuesta deberá corregirse o abstenerse.

---

# Caso de uso 3 — Agente de sustituciones

El agente propone:

```text
Sustituir nata por yogur.
```

El Razonador valida:

- tipo de preparación;
- función de la nata;
- dieta;
- alérgenos;
- contexto;
- regla de sustitución.

Resultado:

```text
válida para salsa fría
```

pero:

```text
no aplicable para nata montada
```

---

# Caso de uso 4 — Simulación

Pregunta:

```text
¿Qué ocurriría si sustituyo el huevo?
```

El sistema:

1. crea contexto hipotético;
2. elimina temporalmente la relación con huevo;
3. añade sustitución propuesta;
4. ejecuta rulesets dietéticos;
5. compara resultados;
6. devuelve diferencias;
7. no materializa cambios.

---

# Caso de uso 5 — Invalidación propagada

Cambio:

```text
ING-0008 ya no está presente en la versión actual de la receta.
```

Flujo:

```text
Invalidar premisa
↓
Localizar inferencias dependientes
↓
Marcar stale
↓
Recalcular
↓
Invalidar conclusión de alérgeno si no existe otra justificación
↓
Actualizar colección
↓
Invalidar caché RAG
↓
Publicar evento
```

---

# Transición hacia la Parte VI

Esta quinta parte ha establecido:

- el modelo de explicabilidad;
- los tipos y niveles de explicación;
- árboles y grafos de justificación;
- explicación de reglas no activadas;
- explicaciones contrastivas y contrafactuales;
- trazabilidad extremo a extremo;
- lineage;
- auditoría;
- materialización en el Knowledge Graph;
- integración con Colecciones;
- integración con GraphRAG;
- integración con agentes;
- APIs;
- MCP;
- eventos;
- observabilidad;
- rendimiento;
- seguridad;
- perfiles de integración.

La Parte VI completará la especificación del Razonador mediante:

- gobernanza de reglas;
- ciclo de vida;
- roles y responsabilidades;
- versionado;
- compatibilidad;
- calidad;
- pruebas;
- golden cases;
- deuda del Razonador;
- migraciones;
- incidentes;
- niveles de madurez;
- perfiles de conformidad;
- roadmap de implementación;
- arquitectura final.

---

# Conclusión

La explicabilidad y la trazabilidad convierten al Razonador en una capacidad confiable del Knowledge Engine.

Una conclusión no deberá considerarse plenamente utilizable mientras no pueda responder:

```text
Qué se ha concluido

Por qué

Con qué regla

A partir de qué conocimiento

En qué contexto

Con qué versión

Con qué limitaciones

Con qué permisos
```

La integración operativa deberá conservar siempre la separación entre:

```text
Hecho explícito
        ↓
Inferencia
        ↓
Explicación
        ↓
Consumo
```

La materialización no deberá eliminar el origen derivado de una conclusión.

GraphRAG no deberá presentar inferencias sin respaldo.

Los agentes no deberán tratar recomendaciones como hechos.

Las APIs no deberán reducir resultados complejos a texto sin metadatos.

Las explicaciones no deberán revelar conocimiento restringido.

La arquitectura completa puede resumirse así:

```text
Razonar
   ↓
Validar
   ↓
Explicar
   ↓
Trazar
   ↓
Publicar
   ↓
Consumir
```

Con esta quinta parte queda definido el puente entre el núcleo lógico del Razonador y el resto de NovaCoquinaria.

La siguiente y última parte establecerá el marco de gobernanza, calidad y evolución necesario para que reglas, inferencias, explicaciones e integraciones puedan mantenerse de forma sostenible durante todo el ciclo de vida del SGCC.

---

# Parte VI — Gobernanza, ciclo de vida y roadmap del Razonador

---

# Introducción

Las partes anteriores han definido completamente el funcionamiento interno del Razonador:

- arquitectura;
- modelo lógico;
- ejecución;
- consistencia;
- explicabilidad;
- integración.

Esta última parte define cómo deberá evolucionar el Razonador durante toda la vida del proyecto.

Una regla correctamente implementada hoy puede dejar de ser válida dentro de varios años.

Una ontología puede evolucionar.

Una colección puede cambiar.

Nuevos tipos de conocimiento pueden aparecer.

Nuevos motores de inferencia pueden incorporarse.

Por ello el SGCC necesita un modelo formal de gobernanza.

---

# Objetivos

Esta parte establece:

- gobierno del Razonador;
- gobierno de reglas;
- gobierno de Rulesets;
- gobierno de perfiles;
- versionado;
- ciclo de vida;
- compatibilidad;
- migraciones;
- pruebas;
- calidad;
- deuda técnica;
- métricas;
- madurez;
- roadmap.

---

# Principios de gobernanza

Toda evolución del Razonador deberá respetar:

- estabilidad;
- reproducibilidad;
- trazabilidad;
- explicabilidad;
- compatibilidad;
- auditabilidad;
- mínima sorpresa;
- independencia tecnológica.

---

# Ciclo de vida de una regla

Toda regla seguirá un ciclo de vida.

```text
Draft

↓

Review

↓

Validated

↓

Stable

↓

Deprecated

↓

Archived
```

---

## Draft

Regla en construcción.

No deberá utilizarse en producción.

---

## Review

Pendiente de revisión.

---

## Validated

Ha superado pruebas funcionales.

---

## Stable

Puede utilizarse por cualquier Ruleset.

---

## Deprecated

Existe una alternativa recomendada.

---

## Archived

No participa en nuevas ejecuciones.

---

# Ciclo de vida de un Ruleset

```text
Draft

↓

Experimental

↓

Validated

↓

Stable

↓

Deprecated

↓

Archived
```

Los Rulesets podrán evolucionar independientemente.

---

# Versionado

Todos los componentes deberán versionarse.

Ejemplos:

```text
Reasoner

Ontology

Knowledge Graph

Rulesets

Rules

Constraint Sets

Profiles

APIs
```

---

# Semantic Versioning

Se recomienda:

```text
MAJOR.MINOR.PATCH
```

Ejemplo:

```text
2.3.1
```

---

# Compatibilidad

Toda modificación deberá clasificarse.

```text
Compatible

Compatible con advertencias

Incompatible
```

---

# Cambios compatibles

Ejemplos:

- nuevas reglas opcionales;
- nuevas explicaciones;
- nuevas métricas;
- optimizaciones internas.

---

# Cambios incompatibles

Ejemplos:

- modificación del significado de una regla;
- cambio de ontología incompatible;
- eliminación de clases;
- modificación de contratos públicos.

---

# Gestión de migraciones

Cuando un cambio sea incompatible deberá existir:

- estrategia;
- documentación;
- pruebas;
- rollback.

---

# Migración de reglas

Ejemplo:

```text
RULE-0007

↓

RULE-0018
```

La regla antigua podrá mantenerse deprecada hasta completar la transición.

---

# Migración de inferencias

Las inferencias existentes podrán:

- recalcularse;
- invalidarse;
- archivarse.

Nunca deberán reinterpretarse silenciosamente.

---

# Migración de la ontología

Toda modificación importante requerirá:

- validación completa;
- análisis de impacto;
- regeneración del grafo;
- recalculo de inferencias.

---

# Gobierno de perfiles

Los perfiles deberán estar documentados.

Ejemplos:

```text
strict

standard

exploratory

experimental
```

Cada perfil definirá:

- reglas permitidas;
- niveles de explicación;
- límites;
- seguridad.

---

# Roles

El SGCC distinguirá distintos roles.

---

## Knowledge Architect

Responsable de la arquitectura semántica.

---

## Ontology Maintainer

Responsable de la ontología.

---

## Rule Maintainer

Responsable de reglas.

---

## Quality Reviewer

Responsable de validaciones.

---

## Domain Expert

Responsable del conocimiento culinario.

---

## Platform Maintainer

Responsable del motor de ejecución.

---

# Responsabilidades

Toda regla deberá indicar:

```yaml
owner:
    team: knowledge
    maintainer: semantic-team
```

---

# Calidad

Toda regla estable deberá disponer de:

- documentación;
- explicación;
- pruebas;
- ejemplos;
- propietario.

---

# Cobertura

El proyecto medirá:

- cobertura de reglas;
- cobertura de inferencias;
- cobertura de restricciones;
- cobertura de explicaciones.

---

# Golden Cases

Toda funcionalidad importante deberá poseer Golden Cases.

Ejemplo:

```text
Allergen

Diet

Substitution

Classification

Collections
```

---

# Regresión

Toda Release ejecutará:

```text
Regression Suite
```

---

# Benchmarks

El motor mantendrá benchmarks para:

- rendimiento;
- memoria;
- escalabilidad;
- latencia.

---

# Métricas del Reasoner

Ejemplos:

```text
Rules

Rulesets

Inferencias

Explicaciones

Conflictos

Violaciones

Tiempo medio

Profundidad

Cache Hit

Materializaciones
```

---

# KPIs

Ejemplos:

- tiempo medio de razonamiento;
- inferencias por segundo;
- conflictos abiertos;
- reglas sin pruebas;
- reglas deprecadas;
- reglas duplicadas.

---

# Deuda del Razonador

El proyecto mantendrá un registro de deuda.

Ejemplos:

- reglas duplicadas;
- reglas obsoletas;
- excepciones excesivas;
- inferencias redundantes;
- explicaciones incompletas.

---

# Incidentes

Los incidentes deberán clasificarse.

Ejemplos:

```text
Performance

Consistency

Ontology

Rules

Execution

Security

Integration
```

---

# Postmortem

Todo incidente crítico deberá generar:

- causa;
- impacto;
- solución;
- acciones preventivas.

---

# Roadmap evolutivo

## Nivel 1

Motor básico.

Incluye:

- Forward Chaining;
- reglas deterministas;
- explicación básica.

---

## Nivel 2

Knowledge Graph completo.

Incluye:

- materialización;
- invalidación;
- colecciones.

---

## Nivel 3

GraphRAG.

Incluye:

- grounding;
- recuperación semántica;
- validación.

---

## Nivel 4

Agentes.

Incluye:

- herramientas;
- planificación;
- simulación.

---

## Nivel 5

Reasoning avanzado.

Incluye:

- contrafactuales;
- argumentación;
- múltiples estrategias.

---

# Madurez

Modelo recomendado.

```text
M0

Conceptual

↓

M1

Experimental

↓

M2

Operativo

↓

M3

Estable

↓

M4

Escalable

↓

M5

Enterprise
```

---

# Conformidad

Un Reasoner será conforme cuando:

- implemente contratos;
- preserve trazabilidad;
- mantenga explicabilidad;
- respete restricciones;
- gestione conflictos;
- soporte auditoría.

---

# Lista de comprobación

Antes de publicar una nueva versión:

```text
[ ] Todas las reglas poseen versión.
[ ] Todas las reglas poseen pruebas.
[ ] No existen conflictos críticos.
[ ] Las explicaciones funcionan.
[ ] Las APIs son compatibles.
[ ] Las métricas son correctas.
[ ] Se ejecutó la regresión.
[ ] Existe documentación.
```

---

# Relación con el resto del SGCC

El Razonador constituye uno de los motores fundamentales del Sistema de Gestión del Conocimiento.

Su posición conceptual puede resumirse como:

```text
                 Ontología
                     │
                     ▼
            Knowledge Graph
                     │
                     ▼
                RAZONADOR
                     │
     ┌───────────────┼────────────────┐
     ▼               ▼                ▼
 Inferencias    Validaciones    Explicaciones
     │               │                │
     └───────────────┼────────────────┘
                     ▼
          Knowledge Engine
                     │
     ┌───────────────┼────────────────────┐
     ▼               ▼                    ▼
 GraphRAG      Agentes IA          Aplicaciones
```

---

# Arquitectura final del Knowledge Engine

El Razonador no constituye un componente aislado.

Forma parte del **Knowledge Engine**, compuesto por varios motores especializados:

```text
                    Knowledge Engine
──────────────────────────────────────────────────

                Knowledge Graph
                       │
                       ▼
               Ontology Engine
                       │
                       ▼
                Reasoning Engine
                       │
       ┌───────────────┼────────────────┐
       ▼               ▼                ▼
 Constraint       Explanation      Validation
   Engine            Engine          Engine
       │               │                │
       └───────────────┼────────────────┘
                       ▼
            Materialization Engine
                       │
                       ▼
             GraphRAG / Agents / APIs
```

Cada motor posee una responsabilidad bien definida y desacoplada, facilitando su evolución independiente.

---

# Relación con otros documentos de especificación

Esta especificación se complementa con:

- `ESPECIFICACION_DE_DOCUMENTOS.md`
- `ESPECIFICACION_DE_COMPONENTES.md`
- `ESPECIFICACION_DE_RELACIONES.md`
- `ESPECIFICACION_DE_ONTOLOGIAS.md`
- `ESPECIFICACION_DE_COLECCIONES.md`
- `ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md`

En conjunto, estos documentos definen el núcleo conceptual del SGCC.

---

# Futuras especificaciones derivadas

A partir de este documento podrán desarrollarse especificaciones técnicas independientes, entre ellas:

- `ESPECIFICACION_DEL_RULE_ENGINE.md`
- `ESPECIFICACION_DE_RULESETS.md`
- `ESPECIFICACION_DE_REGLAS.md`
- `ESPECIFICACION_DEL_CONSTRAINT_ENGINE.md`
- `ESPECIFICACION_DEL_EXPLANATION_ENGINE.md`
- `ESPECIFICACION_DEL_MATERIALIZATION_ENGINE.md`
- `ESPECIFICACION_DEL_GRAPHRAG.md`
- `ESPECIFICACION_DE_AGENTES.md`
- `ESPECIFICACION_DE_PROMPTS.md`
- `ESPECIFICACION_DE_APIS_DEL_REASONER.md`

Estas especificaciones heredarán los principios arquitectónicos establecidos en este documento.

---

# Estado de madurez del documento

| Aspecto | Estado |
|----------|--------|
| Arquitectura conceptual | ✅ Completa |
| Modelo lógico | ✅ Completo |
| Pipeline de ejecución | ✅ Completo |
| Consistencia y validación | ✅ Completo |
| Explicabilidad | ✅ Completa |
| Integración | ✅ Completa |
| Gobernanza | ✅ Completa |
| Roadmap | ✅ Completo |

---

# Conclusión

Con esta sexta parte queda finalizada la especificación del **Reasoning Engine** de NovaCoquinaria.

El documento establece una definición formal, independiente de tecnologías concretas, sobre cómo un motor de razonamiento debe representar, procesar, validar, explicar y gobernar el conocimiento culinario.

Junto con las especificaciones de documentos, componentes, relaciones, ontologías, colecciones y Knowledge Graph, este documento completa el **núcleo arquitectónico del modelo de conocimiento del SGCC**.

Sobre esta base será posible desarrollar, de forma incremental y manteniendo la coherencia conceptual, implementaciones concretas del motor de razonamiento, GraphRAG, agentes inteligentes, motores de validación y demás capacidades avanzadas de NovaCoquinaria.

Con ello concluye la **Especificación del Razonador (Reasoning Engine)**, uno de los pilares fundamentales del ecosistema de gestión del conocimiento de NovaCoquinaria.
