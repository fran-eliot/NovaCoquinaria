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

## Línea base de conocimiento

El workflow [Knowledge audit](../.github/workflows/knowledge-audit.yml) conserva informes de inventario y auditoría como artefactos de GitHub Actions durante 30 días. No modifica los informes versionados. Se ejecuta sobre PR, cambios a main y activación manual. El commit real del checkout consta en commit.txt e inventory.json.

Reproducción local desde un checkout limpio:

```bash
python -m unittest discover -s tools -p 'test_audit_inventory.py'
python tools/audit_inventory.py --output site/knowledge-audit/inventory.json
python tools/audit_knowledge.py --output site/knowledge-audit/KNOWLEDGE_AUDIT.md --json-output site/knowledge-audit/knowledge_audit.json
```

El inventario consulta rutas del árbol Git de HEAD; la auditoría de dominios lee el checkout. Ejecutar ambos desde un checkout limpio para mantener correspondencia. El directorio site está excluido del cargador documental. La cobertura estructural de dominios no equivale al inventario por módulos ni a la validación culinaria.

## Proyección inicial de recetas

`extract_recipe_metadata.py` lee exclusivamente archivos del árbol Git de un commit, no cambios locales ni archivos sin seguimiento. Genera una proyección parcial (etapa `metadata_only`) con identidad literal, metadatos, ubicación y SHA-256 de la fuente, además del contraste entre rutas y documentos de tipo receta. Todavía no extrae ingredientes, procedimientos ni evidencia culinaria.

```bash
python -m unittest discover -s tools -p 'test_*.py'
python tools/extract_recipe_metadata.py --ref HEAD --output site/knowledge-audit/recipe_metadata.json
```

Las pruebas de aceptación de metadatos necesitan el commit fijado en `tools/fixtures/recipe_contract_cases.json` en el historial local. El workflow Knowledge audit realiza checkout con historial completo y publica la proyección dentro de su artefacto temporal. La salida no modifica el Markdown ni constituye un índice definitivo.

## Extracción de ingredientes (0.2.0)

La proyección incorpora listas bajo encabezados Ingredientes, grupos, cantidades exactas o intervalos, fracciones sin redondeo, opcionalidad y resolución únicamente mediante enlaces explícitos a fichas de ingrediente del mismo snapshot. Conserva texto y localizadores. Los formatos todavía no reconocidos generan diagnósticos; no se infieren cantidades ni se convierten medidas domésticas. La salida mantiene el nombre histórico recipe_metadata.json y declara la etapa metadata_and_ingredients. Los procedimientos y la evidencia culinaria siguen pendientes.

## Extracción de procedimientos y evidencia (0.3.0)

Se conservan secciones Markdown ordenadas con localizadores, pasos bajo Elaboración (listas numeradas y encabezados numerados) y declaraciones explícitas de experiencia con su texto fuente. Una declaración histórica no acredita la fórmula actual. El reconocimiento de evidencia es deliberadamente limitado: si no se reconoce una declaración suficiente o hay conflicto, se conserva unknown y se emite diagnóstico. Quedan pendientes rendimiento, duraciones, relaciones generales y evaluación de cobertura.

## Rendimiento, duraciones y referencias (0.4.0)

La proyección añade rendimiento y fases temporales de tablas Información general, conservando expresiones compuestas sin sumar duraciones ni inventar unidades. Los enlaces Markdown inline se resuelven contra el árbol del mismo snapshot; un destino sin ID conocido mantiene su ruta, sin crear identidad. Los enlaces no equivalen automáticamente a relaciones semánticas tipadas y no se verifica la existencia de anclas. Los formatos no reconocidos quedan en secciones y diagnósticos. La etapa recipe_projection_preview aún requiere evaluación de cobertura antes de crear el índice.

## Cobertura de la proyección de recetas

```bash
python tools/report_recipe_coverage.py --input site/knowledge-audit/recipe_metadata.json --output site/knowledge-audit/recipe_coverage.json
```

El informe presenta presencia de campos por receta, distribución de estados de cantidades y evidencia, resolución explícita de ingredientes y referencias, diagnósticos por módulo y fichas afectadas. Cada proporción declara numerador y denominador; sin observaciones el porcentaje es nulo. Se cuentan ocurrencias, no ingredientes únicos. Las referencias internas excluyen enlaces externos y anclas locales. Los resultados miden reconocimiento del extractor, no exhaustividad de las listas originales, precisión semántica o calidad culinaria. Knowledge audit incluye el informe derivado y un resumen en consola.
