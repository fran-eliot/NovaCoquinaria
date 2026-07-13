# Bitácora del Proyecto

> Registro cronológico de los principales hitos de NovaCoquinaria.

---

## Propósito

La Bitácora documenta la evolución del proyecto a lo largo del tiempo.

No pretende sustituir al **CHANGELOG** ni al historial de Git, sino explicar los hitos que han marcado la evolución de NovaCoquinaria y las decisiones más relevantes adoptadas durante su desarrollo.

---

## Criterios de registro

La Bitácora solo recoge:

- Releases.
- Cambios arquitectónicos.
- Nuevos módulos.
- Cambios de filosofía.
- Grandes refactorizaciones.
- Incorporación de nuevas tecnologías.

No registra cambios menores ni tareas cotidianas.

---

# 2026

## 2026-06-29 · Inicio del proyecto

Se crea el repositorio **NovaCoquinaria** con el objetivo inicial de organizar una colección personal de recetas utilizando Markdown como formato principal de documentación.

---

## 2026-06-30 · Release v0.1.0

Primera versión funcional del proyecto.

### Hitos

- Creación de la estructura inicial del repositorio.
- Primeros documentos base.
- Primeras recetas.
- Primeras bases culinarias.
- Definición del estilo documental.

---

## 2026-07-01 · Nacimiento del SGCC

El proyecto evoluciona desde un simple recetario hacia un **Sistema de Gestión del Conocimiento Culinario (SGCC)**.

### Decisiones

- Separación entre recetas y conocimiento reutilizable.
- Introducción de Bases, Despensa, Plantillas y Tablas.
- Organización modular del conocimiento.

---

## 2026-07-03 · Arquitectura documental

Se consolida la arquitectura documental del proyecto.

### Hitos

- Incorporación de ADR.
- Front Matter YAML.
- Sistema de referencias cruzadas.
- Estructura definitiva del repositorio.

---

## 2026-07-05 · Release v1.0.0

Primera versión estable.

### Hitos

- Arquitectura consolidada.
- Documentación técnica completa.
- Base de conocimiento inicial.
- Publicación de la primera Release.

---

## 2026-07-06 · Portal web

Comienza la integración de **MkDocs Material**.

### Decisiones

- Markdown continúa siendo la fuente de verdad.
- `site_docs` pasa a generarse automáticamente.
- MkDocs se utiliza únicamente como herramienta de publicación.

---

## 2026-07-06 · Identidad visual

Se incorpora la identidad gráfica del proyecto.

### Hitos

- Landing page.
- Tarjetas de navegación.
- Logo.
- Favicon.
- Tema claro/oscuro.
- Mejora de la experiencia de usuario.

---

### 2026-07-07

Release v1.1.0 publicada.

Se consolida:

- Portal MkDocs
- Identidad visual
- Documentación de gestión
- Continuidad del proyecto

Con esta versión concluye la primera etapa de NovaCoquinaria, centrada en la definición de su arquitectura, la organización del conocimiento culinario y la construcción de una infraestructura documental preparada para evolucionar en futuras versiones.

---

## 2026-07-09 · Release v1.2.0

Se incorpora el primer framework de calidad y automatización del SGCC.

### Hitos

- Validación automática de Front Matter.
- Validación de identificadores únicos.
- Validación de enlaces internos.
- Pipeline local `validate_all.py`.
- Estadísticas básicas del repositorio.
- Documento base `Mise en place`.

---

## 2026-07-09 · Release v1.3.0

NovaCoquinaria incorpora su primer **Knowledge Graph**.

### Hitos

- Modelo interno `KnowledgeGraph`.
- Generación de grafo Mermaid.
- Estadísticas avanzadas del grafo.
- Detección de conocimiento reutilizable huérfano.
- Validación semántica básica.
- Separación de reglas semánticas en `semantic_rules.py`.

Esta versión marca el paso desde un repositorio validado hacia un sistema capaz de analizar relaciones entre documentos.

---

## 2026-07-11 · Release v1.4.0  Gobernanza del conocimiento

### Gobernanza del conocimiento

- Definido el modelo de gobernanza del SGCC.
- Incorporados los documentos:
  - KNOWLEDGE_STRATEGY
  - KNOWLEDGE_DEBT
  - KNOWLEDGE_MATURITY
- Actualizada la documentación de onboarding y estructura.
- Consolidada la separación entre arquitectura, gestión y conocimiento.
- Esta versión marca la transición desde la construcción de la infraestructura documental hacia el desarrollo sistemático del conocimiento culinario.

---

## 2026-07-13 · Marco de gobernanza completado

Se completa el conjunto de documentación estratégica y metodológica del SGCC.

### Hitos

- Incorporación de `DEVELOPMENT_WORKFLOW.md`.
- Revisión y consolidación de `README.md`.
- Revisión y consolidación de `VISION.md`.
- Definición oficial del workflow de desarrollo.
- Estabilización de la documentación de gobernanza.
- Inicio de la transición hacia el desarrollo sistemático de dominios culinarios.

Con este hito finaliza la etapa de construcción del marco metodológico del proyecto. A partir de este momento el foco principal de NovaCoquinaria pasa a ser la expansión del conocimiento culinario mediante el desarrollo de dominios reutilizables.

---

## Próximos hitos

- Publicación mediante GitHub Pages.
- Automatización del portal.
- Nuevas colecciones de recetas.
- Plataforma software.

---

## Referencias

- [PROJECT_STATUS](PROJECT_STATUS.md)
- [RELEASES](RELEASES.md)
- [ROADMAP](../ROADMAP.md)