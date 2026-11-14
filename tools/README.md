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
| `validate_semantics.py` | Comprueba advertencias semánticas básicas del SGCC |
| `semantic_rules.py` | Define reglas semánticas reutilizables para el grafo de conocimiento |
| `generate_stats.py` | Muestra estadísticas básicas del repositorio |
| `generate_graph.py` | Genera el grafo de conocimiento en formato Mermaid |
| `generate_graph_stats.py` | Genera estadísticas avanzadas del grafo de conocimiento |
| `find_orphans.py` | Detecta conocimiento reutilizable no referenciado |
| `graph.py` | Define el modelo interno del grafo de conocimiento |
| `models.py` | Define el modelo documental reutilizado por las herramientas |
| `common.py` | Centraliza utilidades compartidas |

---

## Uso recomendado

Antes de generar la documentación publicada:

```bash
python tools/validate_all.py
```

La validación principal también se ejecuta automáticamente mediante [Knowledge integrity](../.github/workflows/knowledge-integrity.yml) en pull requests y cambios a `main`, y admite ejecución manual desde GitHub Actions. El estado del job refleja el resultado real de los validadores; la existencia del workflow no implica que la base de conocimiento esté libre de errores.

Si la validación es correcta:

```bash
python tools/build_site_docs.py
```

Para consultar estadísticas:

```bash
python tools/generate_stats.py
```

Para generar el grafo de conocimiento:

```bash
python tools/generate_graph.py
```

Para generar estadísticas avanzadas del grafo:

```bash
python tools/generate_graph_stats.py
```

Para detectar conocimiento reutilizable huérfano:

```bash
python tools/find_orphans.py
```

Para ejecutar validaciones semánticas:

```bash
python tools/validate_semantics.py
```

Para detectar documentos reutilizables sin referencias:

```bash
python tools/find_orphans.py
```

Ambos diagnósticos también se ejecutan en el workflow `Knowledge integrity` después de los controles estructurales. Actualmente generan información para revisión: las advertencias semánticas y los documentos huérfanos **no bloquean** la integración por sí solos.

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