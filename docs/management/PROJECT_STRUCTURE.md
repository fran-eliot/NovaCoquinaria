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

```text
docs/
├── adr/
├── management/
├── diagrams/
├── images/
├── templates/
├── ARQUITECTURA.md
├── QUALITY.md
├── ROADMAP.md
└── VISION.md
```

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