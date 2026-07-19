# CONTEXT

> Mapa de navegación de la documentación de NovaCoquinaria.

Este documento proporciona una visión global de la documentación del proyecto y ayuda a localizar rápidamente la información adecuada según el objetivo de cada consulta.

No sustituye al README ni a la documentación especializada; actúa como punto de entrada y guía de navegación para colaboradores humanos y asistentes de IA.

---

# Mapa conceptual

```text
NovaCoquinaria
│
├── Documentación fundacional
│
├── Arquitectura
│
├── Gobierno del proyecto
│
├── Gestión del conocimiento
│
├── Desarrollo e infraestructura
│
└── Publicación
```

---

# Primera lectura recomendada

Si es la primera vez que trabajas con NovaCoquinaria, el orden recomendado es:

1. [README](README.md)
2. [NovaCoquinaria](./NovaCoquinaria.md)
3. [VISION](./docs/VISION.md)
4. [ARQUITECTURA](./docs/ARQUITECTURA.md)
5. [Modelo de Conocimiento](./docs/MODELO_DE_CONOCIMIENTO.md)
6. [Roadmap](./docs/ROADMAP.md)

---

# Navegación por objetivos

## Quiero entender el proyecto

- [README](./README.md)
- [NovaCoquinaria](./NovaCoquinaria.md)
- [Manifiesto](./MANIFESTO.md)
- [VISION](./docs/VISION.md)
- [ARQUITECTURA](./docs/ARQUITECTURA.md)

---

## Quiero entender el conocimiento

- [Modelo de Conocimiento](./docs/MODELO_DE_CONOCIMIENTO.md)
- [Especificación de colecciones](./docs/ESPECIFICACION_DE_COLECCIONES.md)
- [Estrategia del conocimiento](./docs/management/KNOWLEDGE_STRATEGY.md)
- [Madurez del conocimiento](./docs/management/KNOWLEDGE_MATURITY.md)

---

## Quiero conocer decisiones arquitectónicas

- [ADR](./docs/adr/)
- [Sumario de decisiones](./docs/management/DECISIONS_SUMMARY.md)


---

## Quiero empezar a colaborar

- [CONTRIBUTING](CONTRIBUTING.md)
- [PROJECT_ONBOARDING](./docs/management/PROJECT_ONBOARDING.md)
- [AI ONBOARDING](./docs/management/AI_ONBOARDING.md)
- [Guía de estilo](GUIA_DE_ESTILO.md)

---

## Quiero saber el estado actual

- [Estado del proyecto](./docs/management/PROJECT_STATUS.md)
- [Bitácora](./docs/management/BITACORA.md)
- [Roadmap](./docs/ROADMAP.md)
- [Releases](./docs/management/RELEASES.md)

---

## Quiero saber cómo evoluciona el proyecto

- [Roadmap](./docs/ROADMAP.md)
- [Bitácora](./docs/management/BITACORA.md)
- [Changelog](./CHANGELOG.md)
- [Releases](./docs/management/RELEASES.md)

---

## Quiero trabajar en el código

### Desarrollo

- [Flujo de desarrollo](./docs/management/DEVELOPMENT_WORKFLOW.md)
- [Tools Framework](./tools/README.md)
- [Quality](./docs/QUALITY.md)

### Mantenimiento

- [Limitaciones conocidas](docs/management/KNOWN_ISSUES.md)
- [Ideas futuras](docs/management/FUTURE_IDEAS.md)

---

## Publicación

La documentación publicada mediante MkDocs se genera automáticamente.

No editar:

```text
site_docs/
```

Fuente de verdad:

- Markdown del repositorio.
- Ningún archivo de `site_docs/` debe editarse manualmente.

---

## Principios

La documentación del proyecto sigue varios principios:

- un documento, una responsabilidad;
- referencias cruzadas antes que duplicación;
- evolución mediante ADR;
- documentación versionada;
- conocimiento reutilizable;
- el conocimiento se organiza mediante entidades y relaciones, no mediante jerarquías de carpetas.

---

## ¿No sabes dónde buscar?

- Si quieres entender NovaCoquinaria, comienza por el README.
- Si buscas un documento concreto, utiliza las categorías anteriores.
- Si tienes dudas sobre la estructura del proyecto, consulta este documento antes que cualquier otro.

---

# Convenciones

Este documento actúa como índice maestro de la documentación.

Siempre que se incorpore un nuevo documento relevante al proyecto deberá evaluarse si debe incluirse en este índice para mantener actualizada la navegación de NovaCoquinaria.