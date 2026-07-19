---
id: DOC-0013
titulo: Releases
tipo: gestion
version: 1.1
estado: estable
ultima_revision: 2026-07-19
---

# Releases

> Resumen ejecutivo de las versiones publicadas de NovaCoquinaria y de los objetivos alcanzados en cada una de ellas.

---

# Propósito

Este documento resume las Releases oficiales del proyecto.

Su objetivo es responder a la pregunta:

> **¿Qué representa cada versión publicada?**

No sustituye al **CHANGELOG**, que detalla los cambios realizados, ni a la **BITÁCORA**, que explica la evolución histórica del proyecto.

Cada Release representa un hito funcional o arquitectónico significativo en la evolución del Sistema de Gestión del Conocimiento Culinario (SGCC).

---

# Versiones publicadas

| Versión | Fecha | Estado | Hito principal |
|----------|------------|:------:|---------------------------------------------|
| **v0.1.0** | 2026-06-30 | ✅ | Fundación del proyecto |
| **v1.0.0** | 2026-07-05 | ✅ | Primera arquitectura estable del SGCC |
| **v1.1.0** | 2026-07-07 | ✅ | Portal documental MkDocs |
| **v1.2.0** | 2026-07-09 | ✅ | Framework de calidad |
| **v1.3.0** | 2026-07-09 | ✅ | Knowledge Graph |
| **v1.4.0** | 2026-07-11 | ✅ | Gobernanza del conocimiento |

---

# Resumen de Releases

## v0.1.0 · Fundación del proyecto

Primera versión funcional de NovaCoquinaria.

### Objetivos alcanzados

- Creación del repositorio.
- Primera estructura documental.
- Primeras recetas.
- Primeras bases culinarias.
- Definición del estilo documental.

Esta versión establece los cimientos sobre los que evolucionará posteriormente el SGCC.

---

## v1.0.0 · Arquitectura estable

Primera versión estable del proyecto.

### Objetivos alcanzados

- Arquitectura documental.
- Organización modular del conocimiento.
- ADR fundacionales.
- Referencias cruzadas.
- Front Matter YAML.
- Base inicial de conocimiento.

Esta versión transforma NovaCoquinaria en un auténtico Sistema de Gestión del Conocimiento Culinario.

---

## v1.1.0 · Portal documental

Primera publicación preparada para navegación web.

### Objetivos alcanzados

- Integración con MkDocs Material.
- Landing Page.
- Navegación principal.
- Identidad visual.
- Generación automática de `site_docs`.

Esta versión separa definitivamente la documentación fuente de la documentación publicada.

---

## v1.2.0 · Framework de calidad

Incorporación de la primera infraestructura de validación.

### Objetivos alcanzados

- Validadores automáticos.
- Pipeline documental.
- Validación estructural.
- Estadísticas del repositorio.
- Herramientas reutilizables.

Esta Release establece la primera infraestructura de aseguramiento de calidad del SGCC.

---

## v1.3.0 · Knowledge Graph

El SGCC adquiere conocimiento sobre sus propias relaciones internas.

### Objetivos alcanzados

- Knowledge Graph.
- Grafo Mermaid.
- Validación semántica.
- Estadísticas avanzadas.
- Detección de conocimiento huérfano.

Esta versión marca el paso desde un repositorio validado hacia un sistema capaz de analizar su propio conocimiento.

---

## v1.4.0 · Gobernanza del conocimiento

Se completa el marco metodológico del proyecto.

### Objetivos alcanzados

- Modelo de gobernanza.
- Estrategia del conocimiento.
- Gestión de deuda documental.
- Modelo de madurez.
- Workflow oficial de desarrollo.
- Consolidación de la documentación estratégica.

Con esta versión finaliza la construcción de la infraestructura metodológica del SGCC y comienza la etapa de expansión sistemática del conocimiento culinario.

---

# Próximas Releases

## v2.0.0 · Plataforma software

Objetivos previstos:

- Plataforma web.
- API REST.
- Motor de búsqueda semántica.
- Gestión inteligente de recetas.
- Planificador semanal.
- Lista de la compra.
- Integración con IA.

La versión 2.0 supondrá la evolución desde un SGCC documental hacia una plataforma software basada en dicho conocimiento.

---

# Política de Releases

Las Releases oficiales representan hitos relevantes del proyecto.

Una nueva Release se publica cuando se cumple al menos una de las siguientes condiciones:

- finalización de una fase importante;
- incorporación de una capacidad significativa;
- consolidación de una arquitectura;
- evolución del modelo de conocimiento;
- publicación de un nuevo marco metodológico.

No todas las iteraciones de desarrollo generan una Release.

---

# Versionado

NovaCoquinaria utiliza **Semantic Versioning (SemVer)**.

- **Major** → evolución arquitectónica o funcional significativa.
- **Minor** → incorporación de nuevas capacidades compatibles.
- **Patch** → mantenimiento, correcciones y mejoras.

---

# Relación con otros documentos

Este documento complementa:

- [CHANGELOG](../../CHANGELOG.md)
- [BITACORA](BITACORA.md)
- [PROJECT_STATUS](PROJECT_STATUS.md)
- [ROADMAP](../ROADMAP.md)

No sustituye a ninguno de ellos.

Su responsabilidad consiste exclusivamente en resumir el significado y alcance de cada Release publicada.