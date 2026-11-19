---
id: DOC-0014
titulo: Bitácora del Proyecto
tipo: gestion
version: 2.6
estado: estable
ultima_revision: 2026-11-19
---

# Bitácora del Proyecto

> **Proyecto:** NovaCoquinaria
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

La Bitácora conserva la memoria histórica de NovaCoquinaria.

Su finalidad no consiste en registrar cambios técnicos, sino en explicar la evolución del proyecto a través de los acontecimientos que modifican su identidad, arquitectura, metodología o visión.

Cada entrada responde a la pregunta:

> **¿Qué aprendimos que cambió el proyecto?**

---

# Filosofía

Solo se registran acontecimientos que transforman el proyecto.

No se documentan:

- tareas;
- commits;
- correcciones menores;
- trabajo cotidiano;
- cambios editoriales.

La Bitácora registra únicamente hitos que modifican la trayectoria del SGCC.

---

# Historia

---

## 2026-06-29 · Nacimiento de NovaCoquinaria

### Qué ocurrió

Se crea el repositorio con la intención de organizar una colección personal de recetas.

### Por qué ocurrió

La información culinaria comenzaba a dispersarse y necesitaba una estructura mantenible.

### Qué cambió

Aparece la idea de tratar las recetas como documentación.

### Impacto

Se sientan las bases del proyecto.

---

## 2026-06-30 · Primera fundación

### Qué ocurrió

Se publica la primera versión funcional.

### Por qué ocurrió

Era necesario disponer de una estructura mínima sobre la que experimentar.

### Qué cambió

El proyecto deja de ser una idea y pasa a ser un sistema operativo.

### Impacto

Hace posible toda la evolución posterior.

---

## 2026-07-01 · Nace el SGCC

### Qué ocurrió

NovaCoquinaria deja de concebirse como un recetario.

### Por qué ocurrió

Se detecta que las recetas reutilizan mucho conocimiento común.

### Qué cambió

El conocimiento pasa a ser el elemento principal del sistema.

### Impacto

Esta decisión redefine completamente el proyecto.

---

## 2026-07-03 · Arquitectura documental

### Qué ocurrió

Se consolida la arquitectura.

### Por qué ocurrió

El crecimiento del repositorio hacía necesaria una organización estable.

### Qué cambió

La documentación pasa a funcionar como un sistema.

### Impacto

El proyecto adquiere una arquitectura preparada para evolucionar.

---

## 2026-07-05 · Primera versión estable

### Qué ocurrió

Se publica la Release v1.0.0.

### Por qué ocurrió

La arquitectura alcanza un nivel suficiente de estabilidad.

### Qué cambió

NovaCoquinaria puede comenzar a crecer sin replantear continuamente sus fundamentos.

### Impacto

Comienza la evolución sostenible.

---

## 2026-07-06 · Separación entre fuente y publicación

### Qué ocurrió

Se incorpora MkDocs.

### Por qué ocurrió

Era necesario facilitar la consulta del conocimiento.

### Qué cambió

Markdown permanece como fuente única de verdad mientras la publicación pasa a ser un artefacto generado.

### Impacto

Se desacoplan conocimiento y presentación.

---

## 2026-07-09 · El conocimiento comienza a comprenderse a sí mismo

### Qué ocurrió

Se incorpora el Knowledge Graph.

### Por qué ocurrió

La simple validación documental ya no era suficiente.

### Qué cambió

El SGCC pasa a analizar las relaciones entre sus propias entidades.

### Impacto

El proyecto deja de validar únicamente documentos y comienza a validar conocimiento.

---

## 2026-07-11 · La gobernanza se convierte en arquitectura

### Qué ocurrió

Se completa el marco metodológico.

### Por qué ocurrió

El crecimiento del conocimiento exigía reglas explícitas para su evolución.

### Qué cambió

La metodología deja de ser implícita y pasa a formar parte del propio sistema.

### Impacto

La evolución futura queda gobernada por principios estables.

---

## 2026-07-14 · Primer dominio completamente consolidado

### Qué ocurrió

Se completa Currys.

### Por qué ocurrió

Era necesario validar todo el modelo metodológico mediante un dominio real.

### Qué cambió

Por primera vez el ciclo completo del SGCC se demuestra funcional.

### Impacto

El proyecto dispone de un patrón de referencia para futuras expansiones.

---

## 2026-07-30 — Reestructuración documental y consolidación de la arquitectura

### Hitos

- Reorganización completa de `/docs`.
- Separación en architecture, governance, management y specifications.
- Traslado de los ADR a `docs/governance/adr`.
- Actualización de referencias internas.
- Refuerzo de las herramientas de validación documental.
- Validación satisfactoria:
  - 125 documentos
  - 90 identificadores únicos
  - 822 enlaces internos

---

## 2026-08-01 — Finalización del núcleo de especificaciones del modelo de conocimiento

### Hito

Se completa la primera gran fase de diseño del Sistema de Gestión del Conocimiento Culinario (SGCC), finalizando el núcleo de especificaciones que define la arquitectura formal del conocimiento de NovaCoquinaria.

Durante esta fase se ha consolidado un modelo coherente y gobernado para representar, organizar y evolucionar el conocimiento culinario, estableciendo una base sólida para el desarrollo futuro de la plataforma y de sus capacidades de inteligencia artificial.

### Principales logros

- Finalización de la especificación del modelo documental.
- Definición formal del modelo de componentes reutilizables.
- Especificación completa del sistema de relaciones semánticas.
- Formalización de la ontología del dominio culinario.
- Rediseño y ampliación del modelo de Colecciones de Conocimiento.
- Especificación integral del Knowledge Graph, incluyendo:
  - metamodelo;
  - construcción e ingestión;
  - consultas y navegación;
  - gobernanza;
  - versionado;
  - calidad;
  - evolución;
  - integración con GraphRAG;
  - integración con agentes inteligentes;
  - razonamiento e inferencias.

### Impacto arquitectónico

Con este hito, NovaCoquinaria dispone de una arquitectura de conocimiento completa y coherente, donde los distintos niveles del sistema quedan claramente definidos:

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

Esta arquitectura constituye la base semántica sobre la que se construirán todas las capacidades inteligentes del proyecto.

### Validación

La reorganización documental ha permitido:

- unificar criterios de diseño;
- homogeneizar la estructura documental;
- reforzar la gobernanza del conocimiento;
- validar la integridad de identificadores, Front Matter y enlaces internos mediante las herramientas automáticas del proyecto.

### Próxima etapa

Concluida la definición del modelo de conocimiento, el proyecto inicia una nueva fase centrada en el **Knowledge Engine**, responsable de convertir dicho conocimiento en un sistema operativo capaz de:

- razonar;
- aplicar reglas;
- ejecutar inferencias;
- recuperar conocimiento mediante GraphRAG;
- asistir mediante agentes inteligentes;
- proporcionar explicaciones y recomendaciones fundamentadas.

Esta transición marca el paso desde una **arquitectura del conocimiento** hacia una **arquitectura de ejecución del conocimiento**, que constituirá el objetivo principal de la versión **v1.5.0 – Knowledge Engine**.

---

## 2026-08-02 · Consolidación del marco de especificaciones del SGCC

### Qué ocurrió

Se completa el primer marco integral de especificaciones arquitectónicas de NovaCoquinaria.

Por primera vez el proyecto dispone de un conjunto coherente de documentos que describen no solo la arquitectura del conocimiento, sino también las reglas que gobiernan su organización, terminología, contratos, interfaces y evolución.

### Por qué ocurrió

La creciente complejidad del SGCC hacía insuficiente una colección de especificaciones independientes.

Era necesario establecer un marco común que definiera cómo se documenta, cómo se relaciona y cómo evoluciona todo el sistema.

### Qué cambió

El proyecto incorpora una nueva capa de gobernanza documental formada por especificaciones transversales que unifican el resto de la documentación.

Durante esta fase se completan, entre otras, las especificaciones de:

- Engine Registry;
- Orquestador de Ejecución;
- Retrieval Engine;
- Motor RAG;
- APIs;
- Ingesta;
- Validación;
- Indexing Engine;
- Razonador;

y se incorpora un conjunto de documentos transversales compuesto por:

- README de especificaciones;
- DEPENDENCIAS;
- GLOSARIO;
- CONVENCIONES.

Con ello, las especificaciones dejan de ser documentos aislados y pasan a constituir un marco arquitectónico cohesionado.

### Impacto

NovaCoquinaria dispone ahora de una base documental preparada para soportar el desarrollo de la futura plataforma software y de sus capacidades de ejecución del conocimiento.

La arquitectura queda organizada en tres niveles claramente diferenciados:

```text
Modelo de conocimiento
        ↓
Motores de ejecución (Runtime)
        ↓
Contratos e interfaces
```
sobre los que se apoyan las especificaciones transversales de organización, gobernanza y terminología.

### Validación

La consolidación del marco de especificaciones se completa satisfactoriamente mediante las herramientas automáticas del proyecto:

- 142 documentos validados.
- 107 identificadores únicos.
- 886 enlaces internos verificados.
- Grafo documental regenerado (107 nodos y 535 relaciones).
- Construcción satisfactoria de la documentación publicada.

### Próxima etapa

Consolidado el marco de especificaciones, el siguiente gran objetivo consistirá en iniciar la definición de la infraestructura software del SGCC, transformando la arquitectura documental en una plataforma ejecutable capaz de materializar los motores, contratos y flujos descritos en estas especificaciones.

---

## 2026-08-02 · El conocimiento pasa a ser la prioridad del proyecto

### Qué ocurrió

Tras completar el marco de especificaciones del SGCC se replanteó la planificación de las siguientes versiones.

### Por qué ocurrió

Se concluyó que desarrollar la plataforma software sobre una base culinaria todavía reducida introduciría una complejidad innecesaria y dificultaría validar el modelo de conocimiento.

### Qué cambió

La evolución del proyecto pasa a priorizar la expansión sistemática del conocimiento culinario antes de iniciar la implementación de la plataforma software.

Se incorporan herramientas automáticas de auditoría del conocimiento para medir cobertura, reutilización, madurez y dominios culinarios.

### Impacto

La futura plataforma podrá desarrollarse sobre un dominio culinario mucho más rico, validado y representativo, reduciendo cambios arquitectónicos posteriores.

---

## 2026-08-03 · Consolidación del primer dominio culinario

### Qué ocurrió

Se completó la consolidación del dominio culinario **Currys**, convirtiéndose en el primer dominio del SGCC que dispone de una estructura completa de conocimiento.

### Qué cambió

- incorporación de la técnica de autoridad «Cocinar un curry»;
- creación de la tabla comparativa «Familias de curry»;
- incorporación del ingrediente «Curry verde»;
- incorporación de la receta «Curry verde de pollo»;
- creación de la categoría `07_Comparativas` dentro de `98_Tablas`;
- ampliación de la auditoría del conocimiento para reconocer tablas y técnicas como documentos de autoridad.

### Resultado

El dominio Currys alcanza:

- cobertura estructural del 100 %;
- estado «🌳 Consolidado»;
- dos familias implementadas (amarillo y verde).

### Impacto

El dominio Currys pasa a ser el modelo de referencia para la futura expansión de los demás dominios culinarios del SGCC.

La arquitectura documental y el sistema de auditoría quedan validados mediante un caso de uso completo y reutilizable.

### Por qué ocurrió

Era necesario comprobar que el modelo documental del SGCC podía aplicarse de forma consistente a un dominio culinario real, reutilizando conocimiento entre ingredientes, técnicas, plantillas, tablas y recetas sin duplicaciones innecesarias.

---

## 2026-11-18 · Del crecimiento del recetario a la explotación del conocimiento

### Qué ocurrió

La expansión sistemática alcanzó un inventario de 590 fichas de recetas, 125 ingredientes y 52 técnicas; las 29 tandas españolas aportaron 174 propuestas. Se plantea y adopta como dirección de trabajo la consolidación y explotación del conocimiento.

### Por qué ocurrió

El volumen disponible permite evaluar consultas e ingesta sobre contenido representativo. Seguir creciendo por cantidad no garantiza reutilización ni calidad. La auditoría publicada anterior a la expansión requiere actualización.

### Qué cambió

La incorporación culinaria continúa según experiencia, cobertura y valor de reutilización. El esfuerzo principal se orienta a calidad, relaciones, contrato de datos y prototipos consultables derivados de Markdown.

### Impacto

El SGCC prepara su primera capacidad de consumo estructurado sin sustituir la fuente documental ni comprometer una tecnología o una implementación completa del Runtime. La madurez culinaria y la calidad semántica permanecen pendientes de evaluación.

---

## 2026-11-19 · El conocimiento comienza a ser consultable programáticamente

### Qué ocurrió

Se completó el primer ciclo dirigido de extracción, indexación y consultas de recetas. El índice reconstruible y el motor de solo lectura permiten recuperar recetas con criterios explícitos, preservando procedencia y evidencia.

### Qué cambió

El consumo del conocimiento deja de depender exclusivamente de la navegación documental. Las consultas separan texto, identidad explícita y candidatos sin convertir incertidumbre en hechos.

### Impacto

La evaluación inicial sobre 590 recetas abre una vía para contrastar capacidades de explotación antes de diseñar una plataforma. Markdown sigue siendo canónico; no se declara un Runtime completo ni una nueva release. Los límites y la evidencia se registran en [Consolidación del conocimiento](./CONSOLIDACION_CONOCIMIENTO.md).

---

## 2026-11-19 · De la coincidencia exacta a la recuperación flexible

### Qué ocurrió

El motor de consultas incorporó una modalidad de términos completos tras contrastar el comportamiento de búsqueda sobre un corpus fijado de 590 recetas.

### Qué cambió

Se separó explícitamente la recuperación de menciones de la resolución de identidades. El conocimiento se vuelve más accesible sin convertir coincidencias textuales, alternativas o variantes de producto en equivalencias. Las propuestas experimentales de identidad permanecen fuera de la entrega.

### Impacto

La evolución demuestra el valor de experimentar antes de ampliar las capacidades del SGCC. La siguiente transición puede centrarse en utilidad práctica con límites verificables, sin comprometer una plataforma completa. Véase [alcance de recuperación](./ALCANCE_RECUPERACION_TEXTUAL.md).

---

## 2026-11-19 · Primera aplicación pública de explotación culinaria

### Qué ocurrió

Culinary Explorer 0.1.0 se publicó en GitHub Pages, con carga pública observada de las 590 recetas del catálogo. Las cuatro unidades de datos, búsqueda, interfaz e integración se completaron y la validación técnica dirigida quedó registrada en el [alcance de entrega](./ALCANCE_CULINARY_EXPLORER.md).

### Qué cambió

NovaCoquinaria permite consultar el conocimiento desde una aplicación interactiva sin servidor de aplicación: búsqueda por título y menciones de ingredientes, filtros, evidencia y acceso a las fichas fuente.

### Impacto

El SGCC pasa del consumo programático a la explotación cotidiana desde el navegador, sin sustituir Markdown como fuente de verdad ni equiparar menciones con disponibilidad. La evidencia no acredita precisión culinaria exhaustiva. Se mantiene la release v1.6.0 y se prepara el alcance del asistente de recetas.

---

## 2026-11-19 · Del descubrimiento de recetas a la preparación guiada

Culinary Recipe Assistant 0.1.0 integra el conocimiento existente en una vista interactiva de preparación, con ingredientes, pasos, temporizador y contexto original. Las pruebas dirigidas sobre el portal construido y el despliegue en gh-pages quedaron registrados en el [alcance de entrega](./ALCANCE_CULINARY_RECIPE_ASSISTANT.md). El funcionamiento público se comunicó posteriormente tras #284.

El SGCC incorpora así seguimiento efímero de cocina sin alterar las fuentes canónicas ni deducir cocción o seguridad. No se publica una nueva release.

---

## 2026-11-19 · Del conocimiento al inventario personal

Culinary Pantry 0.1.0 incorpora por primera vez estado personal persistente al SGCC. El inventario vive en el navegador, separado del conocimiento canónico, con copias manuales y consultas de menciones seleccionadas. El [alcance de entrega](./ALCANCE_CULINARY_PANTRY.md) registra las pruebas dirigidas y el despliegue de #289; la comprobación pública permanece pendiente. Esta separación permite avanzar hacia listas de compra sin equiparar el inventario a una interpretación de requisitos. No se publica una nueva release.

---

# Próximos capítulos

La Bitácora continuará registrando únicamente acontecimientos que transformen la evolución del proyecto.

No todas las Releases generarán una nueva entrada.

No todos los cambios serán históricos.

Solo aquellos que modifiquen la trayectoria del SGCC.

---

# Relaciones

| Documento | Responsabilidad |
|-----------|-----------------|
| PROJECT_STATUS | Presente |
| ROADMAP | Futuro |
| BITÁCORA | Pasado |
| RELEASES | Hitos del producto |
| CHANGELOG | Cambios realizados |

---

# Conclusión

La Bitácora constituye la memoria institucional de NovaCoquinaria.

Mientras el CHANGELOG registra qué cambió y el ROADMAP describe hacia dónde evoluciona el proyecto, la Bitácora explica cómo el SGCC llegó a convertirse en el sistema que es hoy.

Cada entrada conserva no solo los hechos, sino también las decisiones, aprendizajes y cambios de perspectiva que definieron su evolución.