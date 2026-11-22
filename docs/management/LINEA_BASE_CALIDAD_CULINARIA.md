---
id: DOC-CULINARY-KNOWLEDGE-QUALITY-BASELINE-2026
titulo: Culinary Knowledge Quality Baseline — Unidad A
tipo: gestion
version: 0.1.0
estado: linea-base-tecnica-dirigida
ultima_revision: 2026-11-22
---

# Culinary Knowledge Quality Baseline — Unidad A

## Alcance, fuente y reproducibilidad

Este informe consolida **medidas observadas** de las herramientas ya existentes, no una nueva puntuación editorial de calidad. La fuente es [Knowledge audit #300](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/45046377378), job `137281785850`, ejecutado el 2026-11-22 con resultado `success`. La proyección declara el commit `7bc20e9a019d95445a13f59b109d52185c450a18`, desde el que se extrajeron los datos; el job se disparó sobre la rama de la PR #339. Este corte **no representa automáticamente** el contenido de todos los commits de `main` posteriores a ese SHA. El artefacto del run es `knowledge-baseline-7bc20e9a019d95445a13f59b109d52185c450a18` (retención temporal de GitHub Actions).

El inventario de rutas procede de `tools/audit_inventory.py`, la cobertura de extracción de `tools/report_recipe_coverage.py`, y los dominios de `tools/audit_knowledge.py`. El workflow `.github/workflows/knowledge-audit.yml` genera los informes en `site/knowledge-audit/`, incluida la proyección `recipe_metadata.json`, `recipe_coverage.json`, `inventory.json` y `knowledge_audit.json`. Los informes generados son evidencia de CI, **no documentos fuente editados manualmente**. La regeneración posterior debe repetir los comandos del workflow, conservar el SHA y comparar únicamente indicadores con iguales definiciones y denominadores.

La auditoría automática de dominios usa reglas PRIMARY/SECONDARY/MENTION y tipos documentales esperados: su «madurez» es un indicador estructural orientativo, **no calidad culinaria verificada**. La ausencia de advertencias de validación no acredita que una receta esté probada, sea segura o tenga instrucciones óptimas.

## Inventario estructural observado

| Indicador | Resultado | Denominador o definición |
|---|---:|---|
| Archivos Markdown versionados | 940 | Rutas `.md` rastreadas por Git |
| Fichas de receta | 590 | Rutas en los 10 módulos culinarios, excluidos README |
| Fichas de ingredientes | 126 | Rutas de `11_Despensa` sin README/BACKLOG |
| Fichas de técnicas | 52 | Rutas de `00_Bases/03_Tecnicas` sin README |
| Ocurrencias extraídas de ingredientes | 5.047 | Líneas/ocurrencias en 590 recetas, no ingredientes distintos |
| Referencias internas resueltas | 2.497 / 2.497 | Referencias proyectadas internas; no revisión manual de utilidad |

### Distribución física de recetas

| Módulo | Recetas |
|---|---:|
| Arroces | 39 |
| Pastas | 37 |
| Legumbres | 61 |
| Verduras | 86 |
| Carnes | 82 |
| Pescados y mariscos | 69 |
| Cocina asiática | 44 |
| Postres | 82 |
| Bebidas | 36 |
| Horno | 54 |
| **Total** | **590** |

Las rutas no garantizan diversidad temática ni unicidad conceptual. En particular, una versión alternativa de una elaboración no constituye necesariamente un duplicado a eliminar.

## Cobertura descriptiva de la proyección

| Campo reconocido | Resultado | Alcance exacto |
|---|---:|---|
| Recetas con ingredientes extraídos | 590 / 590 (100 %) | Existencia, no suficiencia |
| Recetas con pasos extraídos | 590 / 590 (100 %) | Existencia, no claridad o exhaustividad |
| Recetas con categoría | 588 / 590 (99,66 %) | Metadato proyectado |
| Recetas con rendimiento declarado | 587 / 590 (99,49 %) | Puede ser texto no interpretable |
| Recetas con rendimiento numérico | 492 / 590 (83,39 %) | Interpretación dirigida del extractor |
| Recetas con alguna duración declarada | 386 / 590 (65,42 %) | No necesariamente duración total |
| Recetas con alguna duración numérica | 284 / 590 (48,14 %) | No necesariamente total único utilizable |
| Ocurrencias con cantidad exacta o rango numérico | 4.283 / 5.047 (84,86 %) | No acredita suficiencia para cocinar |
| Ocurrencias de identidad explícita | 36 / 5.047 (0,71 %) | Identificación documental, no normalización implícita |
| Ocurrencias no resueltas con candidato | 1.044 / 5.011 (20,83 %) | Candidatos no confirmados; no son identidades verificadas |

De las 5.047 ocurrencias de ingredientes, 5.011 no tienen identidad explícita resuelta. Sus 1.044 candidatos están sujetos a revisión; 3.967 ocurrencias no resueltas carecen además de candidato. La búsqueda textual conserva utilidad pero **no permite inferir automáticamente disponibilidad o compatibilidad culinaria**.

La evaluación de consultas del mismo job distinguió **101/590 recetas con un total temporal numérico único**, frente a 395 sin total declarado y 94 con total declarado no analizable; es una métrica más estricta que «alguna duración numérica» (284/590). No intercambiar ambos indicadores.

## Evidencia de preparación — estado reconocido, no validación de verdad

| Etiqueta de proyección | Recetas | Denominador |
|---|---:|---:|
| `prepared` | 6 | 590 |
| `pending` | 373 | 590 |
| `unknown` | 211 | 590 |

Los tres estados son **clasificaciones reconocidas por la proyección**, no un censo de las recetas realmente cocinadas por el propietario. En particular, `unknown` no significa «no probada» y `prepared` no prueba independientemente cuándo o cómo se realizó. Antes de corregir etiquetas habrá que cotejar el Markdown canónico y su procedencia.

## Observaciones y prioridades que se desprenden del corte

1. **No hace falta crear otro sistema de métricas para iniciar la revisión editorial.** Inventario, cobertura por receta/módulo, referencias y estados extraídos ya existen en los artefactos.
2. **El mayor hueco computable está en la identificación de ingredientes**, pero una mayor cobertura no es por sí sola argumento para desplegar compatibilidad automática. CCE, CRM y CRR ya documentan límites.
3. **Tiempos totales, rendimiento interpretable y evidencia de preparación** son buenos estratos para la muestra editorial porque muestran diferencias entre presencia documental y utilidad práctica.
4. **Duplicidades, versiones superiores, ingredientes suficientes, pasos correctos, seguridad y calidad real** no se pueden resolver mediante estos recuentos; requieren revisión individual de fuentes y decisiones del propietario.
5. **No se propone cambiar recetas en la Unidad A.** La línea base es descriptiva y con límites declarados, no una calificación global de madurez culinaria.

## Próximo paso sujeto a revisión: Unidad B

Proponer una muestra documental pequeña y estratificada, fijada **antes** de evaluarla, con recetas de distintos módulos y estados de evidencia, y casos de variantes o versiones repetidas. Cada observación tendrá identificador, ruta, líneas y criterio de suficiencia. No asignar automáticamente «probada», no borrar variantes ni reescribir una elaboración solo para mejorar el porcentaje de extracción.

La selección de la muestra y los cambios editoriales posteriores se plantearán en PR separadas después de revisar esta línea base. La release publicada es `v1.7.0`; no se autoriza otra versión ni una capacidad de inferencia.

## Procedimiento de reproducción y fuentes

La ejecución de [Knowledge audit #300](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/45046377378) aporta el informe, el log con los JSON de resumen y el artefacto `knowledge-baseline-7bc20e9a019d95445a13f59b109d52185c450a18`.

Comandos equivalentes, ejecutados **en un checkout del commit que se desee medir**:

```bash
mkdir -p site/knowledge-audit
python tools/audit_inventory.py --output site/knowledge-audit/inventory.json
python tools/audit_knowledge.py --output site/knowledge-audit/KNOWLEDGE_AUDIT.md --json-output site/knowledge-audit/knowledge_audit.json
python tools/extract_recipe_metadata.py --output site/knowledge-audit/recipe_metadata.json
python tools/report_recipe_coverage.py --input site/knowledge-audit/recipe_metadata.json --output site/knowledge-audit/recipe_coverage.json
```

Precondiciones: entorno Python y dependencias del workflow, archivos Markdown versionados presentes y checkout consistente. Conservar el SHA y el resultado de CI al comunicar cifras; no actualizar este corte sustituyéndolo en silencio con otro commit.
