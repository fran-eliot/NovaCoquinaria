# Changelog

Todos los cambios relevantes de **NovaCoquinaria** se documentan en este archivo.

Este documento sigue el estándar **Keep a Changelog**, adaptado a la arquitectura documental del proyecto.

NovaCoquinaria utiliza **Semantic Versioning (SemVer)**.

---

# Objetivo

Este documento registra los cambios funcionales incorporados en cada versión publicada.

Debe responder exclusivamente a la pregunta:

> **¿Qué cambió en esta versión?**

No explica:

- la historia del proyecto;
- la evolución arquitectónica;
- las decisiones metodológicas;
- el estado actual.

---

# Tipos de cambio

Se utilizan las siguientes categorías.

## Added

Nuevas capacidades.

## Changed

Cambios de comportamiento o arquitectura.

## Improved

Mejoras compatibles.

## Fixed

Correcciones.

## Removed

Contenido eliminado.

## Deprecated

Contenido que deja de recomendarse.

## Security

Cambios relacionados con seguridad.

---

# Versionado

NovaCoquinaria utiliza Semantic Versioning.

```
MAJOR.MINOR.PATCH
```

---

# Historial

## [Unreleased]

### Changed

- _(Reservado para cambios posteriores a v1.7.0.)_

---

## [1.7.0] - Pendiente de publicación

### Added

- Culinary Explorer 0.1.0: búsqueda pública por título, ingredientes mencionados y otros metadatos, con enlaces a las fuentes y distinción entre coincidencias textuales e identidades.
- Culinary Recipe Assistant 0.1.0: ingredientes, elaboración por pasos, temporizador manual, consulta del contexto y selección de ingredientes para compras.
- Culinary Pantry 0.1.0: inventario local declarado, gestión de lotes y consulta orientativa por menciones, sin inferir disponibilidad o cocinabilidad.
- Culinary Shopping 0.1.0: listas de compra locales, revisión de ingredientes enviados desde recetas, marcado de compras e incorporación explícita de lotes a Pantry.
- Culinary Planner 0.1.0: planificación manual de comidas por fecha, selección de recetas y referencias a su procedencia.
- Exportación y vista previa de importación JSON independientes para las aplicaciones de datos personales.

### Improved

- Navegación integrada entre Explorer, Assistant, Planner, Shopping y Pantry, sin altas implícitas de comidas, compras o inventario.
- Adaptación orientativa de cantidades para raciones declaradas y unidades admitidas, con advertencias y revisión humana antes de enviar a Shopping.
- Consolidación de recorridos, pruebas de persistencia y fallos de almacenamiento, recuperación conservadora y accesibilidad dirigida mediante Chromium.
- Comprobaciones públicas HTTP y Chromium, y aceptación funcional manual acotada PUB-01–PUB-07, registradas con sus límites.

### Changed

- Se mantiene Markdown como fuente canónica; las aplicaciones consumen proyecciones regenerables y los datos personales permanecen en almacenamiento local independiente.
- La siguiente prioridad propuesta es medir la calidad y utilidad del conocimiento culinario antes de ampliar la automatización.

### Limitations

- No se entrega backend, sincronización entre dispositivos, compras automáticas, recomendaciones de cocinabilidad, suficiencia de cantidades ni garantías de seguridad alimentaria.
- La aceptación manual no equivale a auditoría completa de accesibilidad, compatibilidad, seguridad o calidad del corpus.

---

## [1.6.0] - 2026-11-19

### Added

- Expansión sistemática del conocimiento culinario, incluidas 174 propuestas de cocina tradicional española en 29 tandas.
- Registro de elaboraciones, variantes y valoraciones con distinción entre evidencia doméstica y propuestas.
- Auditoría reproducible del conocimiento e inventario por commit.
- Contrato de datos de recetas 0.1.0, extractor 0.4.6 e índice derivado 0.2.0.
- Motor de consultas de solo lectura 0.2.0: metadatos, texto exacto, términos completos, identidades explícitas y candidatos.

### Improved

- Relaciones semánticas, navegación y trazabilidad de las fuentes.
- Reconstrucción determinista del índice y evaluación automatizada de consultas.
- Gobernanza de la evolución de recetas y tratamiento explícito de incertidumbre.

### Changed

- Prioridad estratégica: consolidación y explotación del conocimiento antes de implementar la plataforma software.
- Markdown permanece como fuente canónica; la representación consultable es derivada.

---

## [1.5.0] - 2026-08-02

### Added

- Framework completo de especificaciones.
- README de especificaciones.
- DEPENDENCIAS.
- GLOSARIO.
- CONVENCIONES.
- Especificaciones del Runtime.
- Especificación de APIs.

### Improved

- Gobernanza documental.
- Organización de especificaciones.
- Consistencia estructural.
- Referencias cruzadas.

### Changed

- El SGCC incorpora una arquitectura completa de especificaciones preparada para la futura implementación software.

---

## [1.4.0] - 2026-07-11

### Added

- DEVELOPMENT_WORKFLOW.
- KNOWLEDGE_STRATEGY.
- KNOWLEDGE_DEBT.
- KNOWLEDGE_MATURITY.

### Improved

- Gobernanza del conocimiento.
- Separación entre arquitectura, gobernanza y conocimiento.
- Modelo metodológico.

### Changed

- Inicio de la expansión sistemática del conocimiento.

---

## [1.3.0] - 2026-07-09

### Added

- Knowledge Graph.
- Mermaid Graph.
- Validación semántica.
- Estadísticas avanzadas.

### Improved

- Identidad lógica del modelo documental.
- Reutilización del conocimiento.

---

## [1.2.0] - 2026-07-09

### Added

- Framework documental.
- Pipeline.
- Validadores.
- Estadísticas.

### Improved

- Quality Gate.

---

## [1.1.0] - 2026-07-07

### Added

- Portal MkDocs.
- Landing Page.
- Logo.
- Favicon.
- Navegación.

### Improved

- Experiencia de consulta.

---

## [1.0.0] - 2026-07-05

### Added

- Arquitectura documental.
- ADR.
- Front Matter.
- Bases culinarias.
- Tablas.
- Patrones.

### Changed

- Evolución hacia SGCC.

---

## [0.1.0] - 2026-06-30

### Added

- Inicio del proyecto.

---

# Política

Registrar únicamente cambios relevantes para el usuario o para la evolución funcional del proyecto.

No registrar:

- correcciones tipográficas;
- cambios editoriales;
- reorganizaciones menores;
- trabajo intermedio;
- commits.

---

# Relaciones

| Documento | Responsabilidad |
|-----------|-----------------|
| PROJECT_STATUS | Estado actual |
| ROADMAP | Dirección futura |
| BITÁCORA | Historia |
| RELEASES | Significado de cada versión |

---

# Conclusión

El CHANGELOG constituye el registro cronológico de los cambios funcionales incorporados en NovaCoquinaria.

Debe mantenerse preciso, estable y objetivo.

