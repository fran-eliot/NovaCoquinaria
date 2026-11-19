---
id: DOC-0016
titulo: Roadmap
tipo: gestion
version: 2.12
estado: estable
ultima_revision: 2026-11-19
---

# Roadmap

> **Proyecto:** NovaCoquinaria  
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento define la evolución estratégica prevista para NovaCoquinaria.

No constituye un calendario de trabajo ni un backlog de tareas.

Describe las capacidades que el SGCC deberá incorporar progresivamente para cumplir la visión del proyecto.

---

# Filosofía

NovaCoquinaria evoluciona mediante la incorporación gradual de capacidades.

Cada nueva capacidad se apoya sobre las anteriores.

La prioridad siempre será consolidar una capacidad antes de iniciar otra de mayor nivel.

---

# Mapa de evolución

```text
Identidad

↓

Arquitectura

↓

Conocimiento

↓

Calidad

↓

Automatización

↓

Knowledge Graph

↓

Gobernanza

↓

Publicación

↓

Consolidación y explotación del conocimiento

↓

Plataforma

↓

Inteligencia
```

Cada capacidad representa un incremento del valor global del sistema.

---

# Capacidades consolidadas

## Identidad

**Estado:** ✅ Consolidada

### Objetivo

Definir la identidad del proyecto.

### Capacidades incorporadas

- README
- NovaCoquinaria
- MANIFESTO
- VISION

---

## Arquitectura

**Estado:** ✅ Consolidada

### Objetivo

Diseñar el SGCC.

### Capacidades incorporadas

- Arquitectura documental
- ADR
- Modelo de conocimiento
- Referencias cruzadas
- Front Matter

---

## Conocimiento

**Estado:** 🟡 En consolidación e incorporación selectiva

### Objetivo

Construir conocimiento culinario reutilizable.

### Capacidades

- Ingredientes
- Técnicas
- Bases
- Patrones
- Tablas
- Recetas

Esta capacidad crecerá durante toda la vida del proyecto.

---

## Calidad

**Estado:** ✅ Operativa

### Capacidades

- Validación documental
- Validación estructural
- Estadísticas
- Quality Gate

---

## Automatización

**Estado:** ✅ Operativa

### Capacidades

- Scripts
- Validadores
- Generadores
- Automatizaciones

---

## Knowledge Graph

**Estado:** ✅ Operativo

### Capacidades

- Grafo documental
- Relaciones
- Validación semántica
- Estadísticas

Continuará evolucionando de forma permanente.

---

## Gobernanza

**Estado:** ✅ Consolidada

### Capacidades

- Workflow
- Estrategia
- Madurez
- Gestión de deuda

---

## Publicación

**Estado:** 🟡 En consolidación

### Capacidades previstas

- GitHub Pages
- Portal estable
- Índices automáticos
- Navegación avanzada

---

# Capacidad prioritaria: consolidación y explotación del conocimiento

**Estado:** 🟡 Recuperación textual acotada publicada en v1.6.0; compatibilidad culinaria investigada; modelo de requisitos contrastado de forma manual; reconocimiento determinista contrastado de forma acotada; integración diferida.

El inventario del recetario proporciona una base suficiente para explorar el consumo estructurado sin dar por terminada la evolución culinaria. La progresión de referencia es (los primeros cuatro puntos cuentan con prototipos o evidencia dirigida; el quinto incluye la investigación y entrega textual acotada, sin decidir la siguiente capacidad):

1. Línea base reproducible de calidad y relaciones.
2. Contrato de datos de recetas, con trazabilidad y tratamiento explícito de datos desconocidos.
3. Prototipo de ingesta e indexación derivada de Markdown.
4. Consultas reproducibles por ingredientes y metadatos.
5. Evaluación de alternativas de explotación: recuperación textual por términos integrada (motor 0.2.0); identidades adicionales permanecen experimentales.
6. Revisión estratégica global del siguiente bloque funcional: identidades, tiempo/rendimiento, despensa limitada o acceso de solo lectura; revisión documentada en #248.

La [revisión estratégica global](./REVISION_ESTRATEGICA_CULINARIA.md) propone investigar la compatibilidad culinaria acotada como caso de uso para orientar la resolución de identidades. La [investigación CCE-D01–D05](./INVESTIGACION_COMPATIBILIDAD_CULINARIA.md) concluyó con viabilidad técnica acotada y utilidad operativa insuficiente. Se difiere la entrega de CCE y se inicia la [investigación del modelo de requisitos culinarios](./INVESTIGACION_REQUISITOS_CULINARIOS.md), sin seleccionar una implementación. CRM ha acreditado viabilidad representacional acotada; el [reconocimiento de requisitos culinarios](./INVESTIGACION_RECONOCIMIENTO_REQUISITOS.md) concluyó con utilidad incremental limitada. Se registra [deuda semántica](./DEUDA_REQUISITOS_CULINARIOS.md) y se priorizó una nueva revisión de explotación práctica. La revisión #269 seleccionó Culinary Explorer como primera aplicación estática de consulta; sus cuatro unidades están integradas tras #274, con aceptación técnica acotada y publicación observada tras #275.

El [alcance de recuperación textual](./ALCANCE_RECUPERACION_TEXTUAL.md) registra RET-01–RET-14. Los criterios de aceptación se concretan en [Consolidación del conocimiento](./CONSOLIDACION_CONOCIMIENTO.md). La base de conocimiento Markdown permanece canónica; ninguna tecnología de persistencia o framework queda seleccionada. La incorporación de recetas se mantiene de forma selectiva.

## Explotación práctica

- Culinary Explorer 0.1.0: datos, búsqueda, interfaz e integración publicados; aceptación técnica acotada cerrada.
- [Culinary Recipe Assistant](./ALCANCE_CULINARY_RECIPE_ASSISTANT.md): 0.1.0 integrado y desplegado en gh-pages; aceptación técnica dirigida superada y funcionamiento público comunicado tras #284.
- [Culinary Pantry](./ALCANCE_CULINARY_PANTRY.md): alcance 0.1.0 de inventario declarado, persistencia local y búsqueda por menciones; implementación pendiente.
- Compras y planificación: capacidades posteriores, no comprometidas.

# Capacidades futuras

## Plataforma software

**Estado:** ⚪ Planificada

Objetivos:

- Backend
- API
- Gestión de despensa
- Planificador
- Compra inteligente

---

## Inteligencia

**Estado:** ⚪ Visión

Objetivos:

- IA
- RAG
- Agentes
- Recomendaciones
- Sustituciones inteligentes
- Cocina asistida

---

# Prioridades estratégicas

La evolución seguirá siempre el siguiente orden.

## Muy alta

- Establecer una línea base actualizada de calidad y relaciones.
- Consolidar conocimiento reutilizable y reducir deuda según evidencia.
- Evaluar la utilidad y los límites del consumo estructurado ya implementado.

---

## Alta

- Mejorar automatización.
- Evolucionar Knowledge Graph.
- Consolidar publicación.

---

## Estratégica

- Diseñar la plataforma software.
- Preparar integración IA.

---

# Principios de evolución

Toda nueva capacidad deberá:

- aportar valor al conocimiento;
- incrementar reutilización;
- reducir duplicidades;
- integrarse con el modelo existente;
- respetar la arquitectura;
- facilitar futuras capacidades.

---

# Criterios de incorporación

Antes de añadir una nueva línea al Roadmap deberán responderse afirmativamente las siguientes preguntas.

- ¿Aporta una capacidad nueva?
- ¿Incrementa el valor del SGCC?
- ¿Está alineada con la visión?
- ¿No introduce complejidad innecesaria?
- ¿Puede mantenerse a largo plazo?

---

# Relaciones entre documentos

| Documento | Responsabilidad |
|-----------|-----------------|
| PROJECT_STATUS | Situación actual |
| ROADMAP | Evolución futura |
| BITÁCORA | Evolución histórica |
| RELEASES | Capacidades incorporadas |
| CHANGELOG | Cambios realizados |

---

# Documentación relacionada

## Gestión

- PROJECT_STATUS
- BITÁCORA
- RELEASES
- CHANGELOG

## Arquitectura

- VISION
- ARQUITECTURA

---

# Conclusión

NovaCoquinaria evoluciona incorporando nuevas capacidades sobre una arquitectura estable.

El Roadmap no define fechas ni tareas.

Define la dirección estratégica del SGCC y las capacidades que permitirán convertir un sistema documental en una plataforma inteligente de conocimiento culinario.