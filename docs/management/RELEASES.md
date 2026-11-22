---
id: DOC-0013
titulo: Releases
tipo: gestion
version: 2.3
estado: estable
ultima_revision: 2026-11-22
---

# Releases

> **Proyecto:** NovaCoquinaria
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento resume las Releases oficiales de NovaCoquinaria.

Cada Release representa una capacidad consolidada del SGCC y marca un incremento significativo en el valor del proyecto.

No documenta los cambios realizados (CHANGELOG), ni la evolución histórica (BITÁCORA).

Su finalidad consiste en explicar qué aporta cada versión al sistema.

---

# Evolución del producto

```text
Fundación

↓

Arquitectura

↓

Portal

↓

Calidad

↓

Knowledge Graph

↓

Gobernanza

↓

Conocimiento

↓

Plataforma

↓

Inteligencia
```

Cada Release consolida una nueva capacidad antes de incorporar la siguiente.

---

# Resumen ejecutivo

| Versión | Estado | Capacidad principal |
|---------|:------:|---------------------|
| v0.1.0 | ✅ | Fundación |
| v1.0.0 | ✅ | Arquitectura estable |
| v1.1.0 | ✅ | Portal documental |
| v1.2.0 | ✅ | Framework de calidad |
| v1.3.0 | ✅ | Knowledge Graph |
| v1.4.0 | ✅ | Gobernanza del conocimiento |
| v1.5.0 | ✅ | Marco de especificaciones |
| v1.6.0 | ✅ | Culinary Knowledge & Retrieval |
| v1.7.0 | ⏳ Candidata | Culinary Applications & Workflows |

---

# Releases

---

## v0.1.0 · Fundación

### Propósito

Crear la primera base funcional del proyecto.

### Capacidades incorporadas

- estructura inicial;
- primeras recetas;
- primeras bases culinarias;
- estilo documental.

### Impacto

Hace posible la evolución posterior del SGCC.

### Preparó la siguiente Release

Arquitectura estable.

---

## v1.0.0 · Arquitectura estable

### Propósito

Transformar el repositorio en un Sistema de Gestión del Conocimiento Culinario.

### Capacidades incorporadas

- arquitectura documental;
- entidades reutilizables;
- referencias cruzadas;
- ADR;
- Front Matter.

### Impacto

El conocimiento pasa a ser el activo principal del proyecto.

### Preparó la siguiente Release

Portal documental.

---

## v1.1.0 · Portal documental

### Propósito

Facilitar la consulta del conocimiento.

### Capacidades incorporadas

- MkDocs;
- Landing Page;
- navegación;
- identidad visual;
- publicación.

### Impacto

La documentación pasa a ser navegable y preparada para publicación.

### Preparó la siguiente Release

Framework de calidad.

---

## v1.2.0 · Framework de calidad

### Propósito

Automatizar el aseguramiento de calidad.

### Capacidades incorporadas

- validadores;
- pipeline;
- estadísticas;
- framework documental.

### Impacto

La calidad deja de depender exclusivamente de revisión manual.

### Preparó la siguiente Release

Knowledge Graph.

---

## v1.3.0 · Knowledge Graph

### Propósito

Comprender las relaciones del conocimiento.

### Capacidades incorporadas

- Knowledge Graph;
- grafo Mermaid;
- validación semántica;
- estadísticas avanzadas.

### Impacto

El SGCC puede analizar su propio conocimiento.

### Preparó la siguiente Release

Gobernanza.

---

## v1.4.0 · Gobernanza del conocimiento

### Propósito

Completar el marco metodológico del SGCC.

### Capacidades incorporadas

- estrategia;
- workflow;
- madurez;
- deuda documental;
- gobernanza.

### Impacto

El proyecto dispone de un modelo completo para evolucionar el conocimiento de forma sostenible.

### Preparó la siguiente etapa

Expansión sistemática del conocimiento culinario.

---

## v1.5.0 · Marco de especificaciones

### Propósito

Consolidar la arquitectura documental del SGCC mediante un conjunto completo de especificaciones técnicas y transversales.

### Capacidades incorporadas

- especificaciones del Runtime;
- especificaciones de Interfaces;
- especificaciones de Ingesta;
- especificaciones de Validación;
- Engine Registry;
- Orquestador de Ejecución;
- documentación transversal;
- gobernanza documental;
- glosario técnico;
- convenciones de especificación.

### Impacto

El SGCC dispone por primera vez de una arquitectura completamente especificada y preparada para evolucionar hacia una implementación software.

### Preparó la siguiente etapa

Expansión, consolidación y explotación del conocimiento.

---

## v1.6.0 · Culinary Knowledge & Retrieval

### Propósito

Consolidar la expansión del patrimonio culinario y la primera capacidad de consumo programático reproducible del SGCC.

### Capacidades incorporadas

- Conocimiento culinario ampliado, relaciones y criterios de evidencia doméstica.
- Auditoría reproducible por commit.
- Contrato de datos 0.1.0, extractor 0.4.6, índice 0.2.0 y motor de consultas 0.2.0.
- Recuperación de solo lectura por metadatos, texto exacto, términos completos, identidad explícita y candidatos, sin confundir menciones e identidades.

### Impacto y evidencia

El [corte de #246](./CONSOLIDACION_CONOCIMIENTO.md) registra 590 recetas, 126 fichas de ingredientes según el inventario documentado en el [kit](./NOVACOQUINARIA_KIT_CONTINUITY.md), 52 técnicas, 927 Markdown, 102 pruebas, 18 casos textuales fijados y cero advertencias semánticas y huérfanos. El snapshot auditado es distinto del merge. Los flujos del merge #248 finalizaron correctamente. Estos resultados no certifican elaboración doméstica, precisión semántica exhaustiva ni disponibilidad de ingredientes.

### Límites y siguiente etapa

Markdown sigue siendo canónico. No se entrega plataforma, Runtime completo, persistencia, API, RAG, gestor de despensa ni compatibilidad culinaria. La [revisión estratégica](./REVISION_ESTRATEGICA_CULINARIA.md) propone investigar esta última capacidad.

### Estado

Publicada el 2026-11-19: [v1.6.0](https://github.com/fran-eliot/NovaCoquinaria/releases/tag/v1.6.0). Tag verificado sobre `836f02e848299c0a7a7897b22bb83cd13e0c373a` (merge #249); Knowledge integrity, Knowledge audit y Deploy MkDocs satisfactorios. La sincronización documental posterior no modifica el tag.

---

## v1.7.0 · Culinary Applications & Workflows — candidata

### Propósito

Consolidar las primeras **cinco aplicaciones culinarias públicas**, sus recorridos integrados y la aceptación funcional acotada tras v1.6.0. El tag y la GitHub Release **no están autorizados ni publicados** por esta propuesta documental.

### Capacidades incorporadas

- Culinary Explorer: búsqueda y consulta de recetas con procedencia rastreable.
- Recipe Assistant: preparación guiada, temporizador, contexto completo y adaptación conservadora de cantidades declaradas.
- Culinary Pantry: inventario local de lotes declarados y enlaces con las consultas.
- Culinary Shopping: listas personales, revisión de ingredientes de recetas y transferencias explícitas a Pantry.
- Culinary Planner: calendario manual de comidas, recetas vinculadas y conservación de referencias.
- Exportaciones y vistas previas de importación JSON individuales, sin restauración conjunta ni sincronización.
- Navegación pública entre aplicaciones y consolidación funcional con aceptación manual dirigida PUB-01–PUB-07, documentada en [CWC-12](./PROTOCOLO_ACEPTACION_PUBLICA_CULINARIA.md).

### Impacto y límites

NovaCoquinaria pasa de facilitar recuperación programática de conocimiento a ofrecer un conjunto usable de aplicaciones culinarias estáticas. Las cantidades adaptadas son orientativas; una lista parcial no prueba disponibilidad, ni una coincidencia demuestra cocinabilidad. No se entrega backend, transacción atómica entre almacenamientos, recomendaciones inteligentes ni garantía de seguridad alimentaria. La aceptación es funcional y acotada, no auditoría completa de accesibilidad o seguridad.

### Estado y publicación

**Candidata — pendiente de CI final, aprobación del propietario, creación de tag y publicación de GitHub Release.** La última versión realmente publicada permanece en [v1.6.0](https://github.com/fran-eliot/NovaCoquinaria/releases/tag/v1.6.0). El commit de publicación de v1.7.0 se fijará después del merge y de comprobar los workflows de `main`, evitando atribuir el tag a un commit provisional.

### Preparó la siguiente etapa

[Culinary Knowledge Quality Baseline](./REVISION_ESTRATEGICA_POST_ACEPTACION_PUBLICA.md): medir y contrastar calidad, trazabilidad y utilidad editorial antes de seleccionar otra gran capacidad.

---

# Próximas Releases

## v2.0.0 · Plataforma software

### Objetivo

Construir aplicaciones apoyadas sobre el conocimiento del SGCC.

Capacidades previstas:

- API;
- Backend;
- Gestor de despensa;
- Planificador;
- Compra inteligente;
- Plataforma web.

---

## v3.0.0 · Inteligencia

### Objetivo

Incorporar capacidades inteligentes sobre la plataforma.

Posibles capacidades:

- RAG;
- agentes;
- IA culinaria;
- búsqueda semántica;
- planificación inteligente.

---

# Política de Releases

Una nueva Release se publica únicamente cuando el proyecto incorpora una nueva capacidad consolidada.

No todas las iteraciones generan una Release.

Las mejoras menores se documentan mediante el CHANGELOG.

---

# Semantic Versioning

NovaCoquinaria utiliza Semantic Versioning.

| Tipo | Significado |
|-------|-------------|
| Major | Nueva etapa del producto |
| Minor | Nueva capacidad consolidada |
| Patch | Correcciones y mantenimiento |

---

# Relaciones entre documentos

| Documento | Responsabilidad |
|-----------|-----------------|
| PROJECT_STATUS | Estado actual |
| ROADMAP | Evolución futura |
| BITÁCORA | Historia del proyecto |
| CHANGELOG | Cambios incorporados |

---

# Documentación relacionada

## Gestión

- PROJECT_STATUS
- ROADMAP
- BITÁCORA
- CHANGELOG

---

# Conclusión

Las Releases representan los principales hitos de evolución del SGCC.

Cada una consolida una capacidad del sistema y prepara la siguiente etapa de crecimiento.

El conjunto de Releases constituye la historia funcional de NovaCoquinaria como producto.