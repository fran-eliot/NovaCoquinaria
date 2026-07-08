# Herramientas de NovaCoquinaria

Este directorio contiene scripts auxiliares para validar, generar y mantener la documentación de NovaCoquinaria.

Las herramientas no son la fuente de verdad del proyecto.

La fuente de verdad sigue siendo el contenido Markdown del repositorio.

---

## Principios

Las herramientas deben:

- proteger la coherencia arquitectónica;
- detectar errores documentales;
- reducir tareas repetitivas;
- ser simples y auditables;
- no introducir conocimiento culinario nuevo.

---

## Scripts disponibles

| Script | Función |
|---|---|
| `build_site_docs.py` | Genera `site_docs/` a partir del Markdown fuente |
| `validate_frontmatter.py` | Comprueba la existencia y campos mínimos del Front Matter |
| `validate_ids.py` | Verifica que los identificadores sean únicos |
| `validate_links.py` | Detecta enlaces internos rotos |
| `validate_all.py` | Ejecuta todas las validaciones principales |
| `generate_stats.py` | Muestra estadísticas básicas del repositorio |

---

## Uso recomendado

Antes de generar la documentación publicada:

```bash
python tools/validate_all.py
```

Si la validación es correcta:

```bash
python tools/build_site_docs.py
```

Para consultar estadísticas:

```bash
python tools/generate_stats.py
```

---

## Directorios excluidos

Las herramientas ignoran:

```text
.git/
.venv/
venv/
site/
site_docs/
__pycache__/
```

---

## Criterio arquitectónico

Las herramientas forman parte de la infraestructura del SGCC.

Su objetivo es mantener la calidad del conocimiento, no reemplazar la revisión humana.

Toda nueva herramienta deberá justificar qué aspecto de la coherencia documental protege.