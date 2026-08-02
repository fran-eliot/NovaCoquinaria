---
id: DOC-0014
titulo: Bitácora del Proyecto
tipo: gestion
version: 2.0
estado: estable
ultima_revision: 2026-08-02
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