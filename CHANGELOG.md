# CHANGELOG

Todas las modificaciones relevantes de **NovaCoquinaria** se documentan en este archivo.

El formato está inspirado en **Keep a Changelog**, adaptado a las necesidades del proyecto y complementado por la documentación de gobernanza del SGCC.

---

# Propósito

El CHANGELOG registra los cambios funcionales introducidos en cada versión del proyecto.

Debe responder únicamente a la pregunta:

> **¿Qué cambió en esta versión?**

No explica el contexto histórico (BITÁCORA), el estado actual (PROJECT_STATUS) ni los objetivos de cada versión (RELEASES).

---

# Tipos de cambios

Las modificaciones se clasifican utilizando las siguientes categorías.

## Añadido

Nuevas funcionalidades, documentos, herramientas o módulos.

## Mejorado

Mejoras funcionales, ampliaciones del conocimiento o incremento de la reutilización.

## Modificado

Cambios de comportamiento, reorganizaciones o refactorizaciones relevantes.

## Corregido

Corrección de errores, inconsistencias o problemas detectados.

## Eliminado

Contenido obsoleto, duplicado o retirado del proyecto.

---

# Política de versionado

NovaCoquinaria utiliza **Semantic Versioning (SemVer)**.

```text
MAJOR.MINOR.PATCH
```

Donde:

- **MAJOR** → cambios incompatibles o evolución arquitectónica significativa.
- **MINOR** → nuevas funcionalidades compatibles.
- **PATCH** → correcciones, mejoras y mantenimiento.

---

# Historial

## [1.4.0] - 2026-07-11

### Añadido

- Documento `DEVELOPMENT_WORKFLOW.md`.
- `KNOWLEDGE_STRATEGY.md`.
- `KNOWLEDGE_DEBT.md`.
- `KNOWLEDGE_MATURITY.md`.
- Marco completo de gobernanza del conocimiento.

### Mejorado

- Consolidación de la documentación estratégica.
- Separación definitiva entre arquitectura, gobernanza y conocimiento.
- Definición del workflow oficial de desarrollo del SGCC.

### Modificado

- El proyecto entra en una nueva fase centrada en la expansión sistemática del conocimiento culinario.

---

## [1.3.0] - 2026-07-09

### Añadido

- Primer Knowledge Graph de NovaCoquinaria.
- Modelo `KnowledgeGraph`.
- Generación automática del grafo Mermaid.
- Estadísticas avanzadas del grafo.
- Detección de conocimiento reutilizable huérfano.
- Validación semántica básica.
- Reglas semánticas separadas en `semantic_rules.py`.

### Mejorado

- El modelo documental incorpora identidad lógica.
- Las herramientas trabajan sobre entidades documentales y no únicamente sobre archivos.
- Incremento de la trazabilidad entre documentos.

---

## [1.2.0] - 2026-07-09

### Añadido

- Framework documental.
- Validación de Front Matter.
- Validación de identificadores únicos.
- Validación de enlaces internos.
- Pipeline `validate_all.py`.
- Estadísticas básicas del repositorio.
- Documento base `Mise en place`.

### Mejorado

- Separación entre validación, generación y automatización.
- Introducción del primer Quality Gate documental.

---

## [1.1.0] - 2026-07-07

### Añadido

- Portal basado en MkDocs Material.
- Landing Page personalizada.
- Identidad visual.
- Logo.
- Favicon.
- Navegación principal.
- Generación automática de `site_docs`.

### Mejorado

- Experiencia de navegación.
- Organización de la documentación publicada.
- Preparación para GitHub Pages.

---

## [1.0.0] - 2026-07-05

### Añadido

- Arquitectura documental completa.
- Documentación estratégica.
- ADR fundacionales.
- Organización modular del SGCC.
- Bases culinarias iniciales.
- Despensa.
- Patrones reutilizables.
- Tablas.
- Primer conjunto de recetas normalizadas.

### Mejorado

- Referencias cruzadas.
- Identificadores estables.
- Front Matter YAML.
- Modelo documental reutilizable.

### Modificado

- Evolución desde un repositorio de recetas hacia un Sistema de Gestión del Conocimiento Culinario.

---

## [0.1.0] - 2026-06-30

### Añadido

- Estructura inicial del repositorio.
- Primer README.
- Primeras recetas.
- Primeras bases culinarias.
- Organización inicial del proyecto.

---

# Próximas versiones

## [2.0.0]

Objetivos previstos:

- Plataforma software.
- API REST.
- Motor de búsqueda semántica.
- Planificador semanal.
- Lista inteligente de la compra.
- Integración con IA.

---

# Criterios de registro

Registrar únicamente cambios con impacto funcional o arquitectónico.

No registrar:

- correcciones tipográficas;
- cambios de formato;
- reorganizaciones menores;
- modificaciones temporales;
- trabajo en progreso.

El objetivo es mantener un historial claro, estable y útil para comprender la evolución funcional del proyecto.

---

# Relación con otros documentos

Este documento complementa:

- [RELEASES](docs/management/RELEASES.md)
- [BITACORA](docs/management/BITACORA.md)
- [PROJECT_STATUS](docs/management/PROJECT_STATUS.md)

No sustituye a ninguno de ellos.

Su responsabilidad consiste exclusivamente en registrar **qué cambios relevantes incorpora cada versión publicada**.

