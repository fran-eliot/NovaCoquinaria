# Estructura del Proyecto

> Resumen de la organización del repositorio NovaCoquinaria.

---

## Directorios principales

| Directorio | Propósito |
|------------|-----------|
| `00_Bases/` | Fundamentos y técnicas culinarias reutilizables. |
| `01_Arroces/` | Recetas de arroces. |
| `04_Verduras/` | Recetas de verduras. |
| `05_Carnes/` | Recetas de carnes. |
| `06_Pescados_y_Mariscos/` | Recetas de pescados y mariscos. |
| `11_Despensa/` | Ingredientes, salsas, especias y productos. |
| `12_Plantillas/` | Patrones reutilizables para elaborar recetas. |
| `98_Tablas/` | Tablas de referencia culinarias. |
| `assets/` | Recursos gráficos del proyecto. |
| `docs/` | Documentación técnica y arquitectónica. |
| `tools/` | Scripts y herramientas auxiliares. |
| `site_docs/` | Documentación generada para MkDocs (no editar manualmente). |

---

## Documentación técnica

## Documentación técnica

```text
docs/
├── adr/
│   └── Decisiones arquitectónicas
├── architecture/
│   └── Automatización, pipeline de calidad y framework de herramientas
├── diagrams/
│   └── Grafo de conocimiento e informes generados
├── images/
├── management/
│   ├── Estado, releases y bitácora
│   ├── Onboarding y continuidad
│   └── Gobernanza del conocimiento
├── templates/
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

- Markdown es la fuente de verdad del conocimiento.
- `site_docs/` es un artefacto generado automáticamente.
- El conocimiento se organiza de forma modular para favorecer la reutilización.
- Las recetas orquestan información existente y evitan duplicidades.

---

## Referencias

- [Arquitectura](../ARQUITECTURA.md)
- [Visión](../VISION.md)