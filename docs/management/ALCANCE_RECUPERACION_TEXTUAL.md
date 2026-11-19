---
id: DOC-ALCANCE-RECUPERACION-2026
titulo: Alcance de entrega de recuperación textual
tipo: gestion
version: 0.1.1
estado: borrador
ultima_revision: 2026-11-19
---

# Alcance de entrega de recuperación textual

## Base y propósito

La síntesis de [evolución de recuperación culinaria](./EVOLUCION_RECUPERACION_CULINARIA.md) se integró mediante #241 en el commit `e127b5b840d6a422d5e8aee39c6c0b88b4d4c7c1`. Los workflows de dicha PR concluyeron correctamente. Se desarrolla la propuesta A para revisión de alcance, no una autorización de implementación. La evidencia procede de RET-D01–D04, con muestras dirigidas y sin estimación estadística de precisión.

## Entrega propuesta

Culinary Query Engine 0.2.0: añadir exclusivamente el modo de ingrediente `terms` a la función Python y CLI existentes. Mantener el extractor 0.4.6, contrato de datos 0.1.0 e índice 0.2.0. No modificar Markdown culinario, identidades ni candidatos. La versión de herramienta no implica release del proyecto.

Ejemplo de interfaz propuesta:

```bash
python tools/query_recipe_index.py --index site/knowledge-audit/recipe_index.json --ingredient terms "ajo" --ingredient terms "salsa de soja"
```

El modo text sigue comparando nombres completos; explicit y candidate conservan su semántica. terms compara secuencias contiguas de tokens alfanuméricos Unicode con NFC, casefold y separación por puntuación y guion bajo, preservando diacríticos. La consulta sin tokens se rechaza exclusivamente en el nuevo modo. No se expanden plurales, sinónimos, negaciones ni términos separados por otras palabras. Una mención no implica identidad, disponibilidad, equivalencia, necesidad de compra o seguridad alergénica.

## Diseño y compatibilidad

El consumidor utiliza las claves y postings de by_text del índice ya contrastado. No requiere extractor, Git ni PyYAML en tiempo de consulta. Un recorrido de claves es suficiente como punto de partida; no se promete latencia ni escalabilidad sin medición. Compartir la lógica pura de tokenización y contigüidad con el experimento, conservando su variante folded exclusivamente experimental. Ordenar las referencias por ID literal y posición; no duplicar ocurrencias. Mantener esquema de respuesta de modos existentes salvo query_version; para terms registrar modo y valor originales, texto íntegro, posición y localizador, y alcance de coincidencia textual. No introducir un campo obligatorio nuevo en las respuestas anteriores.

## Criterios de aceptación

| ID | Criterio |
|---|---|
| RET-01 | Los tres modos anteriores conservan resultados y evidencia, salvo versión de herramienta; 16 casos previos superados |
| RET-02 | terms es explícito en función y CLI, nunca ampliación implícita de text |
| RET-03 | Tokens completos contiguos, NFC/casefold, puntuación y guion bajo como separadores; diacríticos preservados |
| RET-04 | No coincidencia por subcadena, plural automático ni secuencia discontinua |
| RET-05 | Consulta terms sin tokens o modo desconocido es error; consulta válida sin coincidencias devuelve cero |
| RET-06 | Combinación AND con otras cláusulas y facetas, incluida opcionalidad |
| RET-07 | Recetas únicas ordenadas por ID literal, ocurrencias únicas por posición y orden estable |
| RET-08 | Procedencia, nombre, raw, posición, opcionalidad y resolución original disponibles; coincidencia identificada como textual |
| RET-09 | Alternativas y productos diferentes conservados sin inferir identidad; negación no interpretada |
| RET-10 | Índice no modificado, sin dependencia de extractor ni acceso Git en la consulta |
| RET-11 | Contraste de los 18 casos fijados en exact/text y terms; folded permanece experimental |
| RET-12 | Equivalencia de conjuntos de ocurrencias con RET-D02 para las 17 consultas del corte fijado |
| RET-13 | Evaluación sobre índice del CI vigente, con recuentos observados, procedencia y regresión; no imponer cifras históricas al corpus nuevo |
| RET-14 | Documentar modalidad, ejemplo CLI, limitaciones y cambios de versión; sin release del proyecto |

## Unidades propuestas

| Unidad | Entrega | Criterios principales |
|---|---|---|
| A | Funciones léxicas puras compartidas y recuperación por postings | RET-03, 04, 07, 10 |
| B | Integración del modo terms en función y CLI, evidencia y composición | RET-01, 02, 05–09 |
| C | Contraste en corpus fijado y vigente, integración CI e informe | RET-01, 11–13 |
| D | Documentación de contrato y cierre acotado | RET-14 y revisión conjunta de todos |

Los criterios pueden solaparse; la aceptación final exige evidencia conjunta. Las unidades se ejecutarán de forma incremental, sin declarar completitud por mera fusión. La lógica de experimentación no se elimina antes de contrastar equivalencia.

## Unidad D — Evidencia de cierre técnico

Las unidades A, B y C se integraron mediante #243, #244 y #245. El merge de #245 es `5ecc94155d354bd33d4e866523c9c0e86a4607f4`. El [job de #245](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44520878705/job/135548859640) registra 102 pruebas, cero advertencias semánticas y cero huérfanos, 590 huellas de fuentes verificadas y reconstrucción idéntica. El corte vigente de esa ejecución fue el merge sintético `53f8d35a8ab7bf340d36416a4d35627142353e49`, distinto del merge definitivo; ambos corpus tenían 590 recetas. No se certifica aquí la ejecución posterior al merge. La huella de proyección del corte fijado es `d72cb4cb48f8ab112d3f60003bb8a20acfe295925756e6456b12bf7b2648a89c`; la del corte vigente de CI es `ac2e66a2451c0948d4152a4dcc1d0738a932fa333a8331e07d2f7bbbb2d08a24`.

| Criterio | Evidencia técnica |
|---|---|
| RET-01 | 16 casos de regresión por corpus y pruebas de modos separados; revisión del cambio localizado en query_recipe_index.py. No comparación exhaustiva byte a byte con binario anterior. |
| RET-02 | test_new_mode_is_explicit_and_ordered y test_cli_terms_and_optionality |
| RET-03 | test_unicode_and_separators y test_boundaries_and_diacritics |
| RET-04 | test_complete_contiguous_terms y casos dirigidos negativos |
| RET-05 | test_invalid_query, test_invalid_even_after_empty_filter_and_read_only y consultas válidas vacías |
| RET-06 | test_composition_and_provenance y test_cli_terms_and_optionality |
| RET-07 | test_literal_order_deduplication_and_read_only y comprobaciones de orden y unicidad en observed_refs |
| RET-08 | test_composition_and_provenance y contraste de campos de procedencia en observed_refs |
| RET-09 | Casos de ajo negro, leche o nata y sin sal; no inferencia de identidad, evidencia preservada |
| RET-10 | Núcleo puro de biblioteca estándar; query no importa extractor ni ejecuta Git; índice sin cambios en las unidades A–C |
| RET-11 | 18/18 casos documentales en text y terms; folded solo experimental |
| RET-12 | 34/34 comparaciones con RET-D02 en las 17 consultas del corte fijado; el experimento comparte el núcleo, no es un oráculo independiente |
| RET-13 | 68/68 comparaciones con recorrido independiente sobre registros, 34 por corpus; 16 casos de regresión por corpus |
| RET-14 | Contrato del índice 0.1.4, interfaz 0.2.0 y ejemplos documentados en esta unidad; sin nueva release |

El recorrido independiente evita los postings y el núcleo compartido, pero utiliza la misma proyección; no valida exhaustivamente la extracción ni la pertinencia culinaria. No se ha inspeccionado íntegramente el ZIP de artefactos. Los resultados son consistentes dentro del alcance definido. La unidad D completa la documentación y propone el cierre técnico sujeto a revisión y CI de esta entrega.

## Exclusiones y decisión pendiente

No se incorporan folded, las 72 propuestas de identidad, reglas adicionales, ranking, lenguaje natural, filtros temporales, persistencia, API, despensa, RAG ni recomendaciones. Las unidades A–C se han integrado siguiendo el alcance acotado; el cierre de D queda sujeto a revisión. No se fija release, calendario ni milestone.

## Referencias

- [Evolución de recuperación culinaria](./EVOLUCION_RECUPERACION_CULINARIA.md)
- [Contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md)
- [Consolidación del conocimiento](./CONSOLIDACION_CONOCIMIENTO.md)
