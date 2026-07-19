# Estructura del Proyecto

> Resumen de la organización del repositorio NovaCoquinaria.

---

# Filosofía de la estructura

La estructura física del repositorio existe para soportar el modelo lógico del conocimiento.

Los directorios organizan los documentos, pero no definen el conocimiento.

El verdadero modelo del sistema está representado por las entidades, sus relaciones y las decisiones arquitectónicas documentadas mediante ADR.

---

# Organización lógica

```text
Conocimiento
        │
        ▼
Entidades
        │
        ▼
Relaciones
        │
        ▼
Knowledge Graph
        │
        ▼
Documentos Markdown
        │
        ▼
Repositorio
```

---

## Arquitectura documental

La documentación de NovaCoquinaria se organiza por responsabilidades:

| Documento | Responsabilidad |
|------------|-----------------|
| README | Presentación del proyecto |
| CONTEXT | Índice maestro de navegación |
| NovaCoquinaria | Identidad del proyecto |
| MANIFESTO | Principios permanentes |
| VISION | Dirección estratégica |
| ARQUITECTURA | Diseño del sistema |
| MODELO_DE_CONOCIMIENTO | Ontología del conocimiento |
| PROJECT_ONBOARDING | Incorporación de colaboradores |
| CONTRIBUTING | Proceso de contribución |
| PROJECT_STRUCTURE | Organización física |

---

## Directorios principales

### Conocimiento

| Directorio | Propósito |
|------------|-----------|
| `00_Bases/` | Fundamentos y técnicas culinarias reutilizables. |
| `01_Arroces/` | Dominio culinario especializado en arroces. |
| `04_Verduras/` | Dominio culinario especializado en verduras. |
| `05_Carnes/` | Dominio culinario especializado en carnes. |
| `06_Pescados_y_Mariscos/` | Dominio culinario especializado en pescados y mariscos. |
| `11_Despensa/` | Ingredientes, salsas, especias y productos. |
| `12_Plantillas/` | Patrones y estructuras reutilizables para representar conocimiento culinario. |
| `98_Tablas/` | Tablas de referencia culinarias. |

### Documentación

| Directorio | Propósito |
|------------|-----------|
| `docs/` | Documentación técnica y arquitectónica. |

### Infraestructura


| Directorio | Propósito |
|------------|-----------|
| `assets/` | Recursos gráficos del proyecto. |
| `tools/` | Scripts y herramientas auxiliares. |
| `site_docs/` | Documentación generada para MkDocs (no editar manualmente). |

---

## Documentación técnica

La documentación técnica complementa el modelo de conocimiento y describe la arquitectura, el gobierno y la evolución del proyecto.

```text
docs/
├── adr/
│   └── Decisiones arquitectónicas
├── architecture/
│   └── Arquitectura del sistema
├── diagrams/
│   └── Diagramas generados y manuales
├── images/ 
│   └── Recursos gráficos
├── management/
│   └── Gobierno del proyecto
├── templates/
│   └── Plantillas reutilizables
├── ARQUITECTURA.md
├── QUALITY.md
├── ROADMAP.md
└── VISION.md
```

---

## Herramientas

```text
tools/
├── common.py
├── models.py
├── graph.py
├── semantic_rules.py
├── validate_all.py
├── validate_frontmatter.py
├── validate_ids.py
├── validate_links.py
├── validate_semantics.py
├── generate_graph.py
├── generate_graph_stats.py
├── generate_stats.py
├── find_orphans.py
└── build_site_docs.py
```

Las herramientas se dividen en:

- validadores;
- generadores;
- modelos compartidos;
- procesos de construcción.

---

## Principios de organización

- Markdown es la única fuente de verdad.
- El modelo lógico es independiente del repositorio.
- La estructura física puede evolucionar sin alterar el conocimiento.
- Cada documento tiene una única responsabilidad.
- Las entidades se relacionan mediante referencias explícitas.
- `site_docs` es siempre un artefacto generado.
- El Knowledge Graph representa la organización semántica del sistema.

---

## Evolución de la estructura

La organización del repositorio no es estática.

Podrá modificarse cuando:

- mejore la reutilización;
- simplifique la navegación;
- reduzca duplicidades;
- refleje mejor la evolución del modelo de conocimiento.

Toda reorganización significativa deberá documentarse mediante un ADR.

---

## Referencias

- [README](../../README.md)
- [CONTEXT](../../CONTEXT.md)
- [NovaCoquinaria](../../NovaCoquinaria.md)
- [Arquitectura](../ARQUITECTURA.md)
- [Modelo de conocimiento](../MODELO_DE_CONOCIMIENTO.md)
- [PROJECT_ONBOARDING](../management/PROJECT_ONBOARDING.md)
- [CONTRIBUTING](../../CONTRIBUTING.md)
- [ADR-0002 Estructura del repositorio](../adr/ADR-0002-estructura-del-repositorio.md)
- [Visión](../VISION.md)
