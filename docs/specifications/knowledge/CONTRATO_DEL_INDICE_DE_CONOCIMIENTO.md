---
id: SPEC-INDICE-RECETAS
tipo: especificacion
titulo: Contrato del índice de conocimiento culinario
version: 0.1.3
estado: borrador
ultima_revision: 2026-11-19
tags:
  - conocimiento
  - recetas
  - indexacion
  - procedencia
---

# Contrato del índice de conocimiento culinario

## Propósito

Definir una primera capacidad de indexación reproducible de recetas del SGCC, sobre la proyección estructurada existente. El índice pertenece a la capa de automatización y sirve a consumidores posteriores; no modifica el modelo conceptual, ni sustituye el Knowledge Graph ni convierte la representación derivada en fuente canónica.

El punto de partida es el cierre del extractor 0.4.6 en el commit `1f62c6bfd6bbfab9ebe52069236a1c90d73d27cc` (PR #229). Los resultados de cobertura documentados corresponden a #228: 590 recetas, 5.047 ocurrencias de ingredientes, 36 identidades explícitas y 1.044 ocurrencias con candidato único. Son una línea base histórica, no constantes del índice ni objetivos de cobertura.

## Entrada y frontera

La entrada es un único objeto de etapa `recipe_projection_preview`, contrato 0.1.0 y versión de extractor 0.4.6 inicialmente soportados. Contiene `source_commit`, `inventory` y `recipes`. No se releen los Markdown en el constructor del índice ni se ejecuta extracción adicional. La compatibilidad con otras versiones es explícita, no implícita.

El constructor valida los campos que consume, unicidad exacta de ID y ruta, coherencia del commit por registro, formato de huella SHA-256 y recuento de recetas del inventario. No certifica así los bytes originales: la verificación contra Git es una comprobación independiente. Una entrada inconsistente no produce un índice válido. Las ausencias admitidas y los diagnósticos de extracción permanecen visibles.

## Representación lógica propuesta

| Componente | Contenido |
|---|---|
| Cabecera | index_version, contract_version, extractor_version, source_commit, stage y huella SHA-256 de la proyección serializada de entrada |
| Registros | Un registro por ID exacto, con la proyección de receta conservada |
| Índice de rutas | Ruta relativa exacta → ID |
| Metadatos | Índices invertidos por módulo físico, categoría explícita, estado documental y evidencia de elaboración |
| Títulos | Clave textual normalizada → IDs de recetas |
| Ingredientes textuales | Clave textual normalizada → ocurrencias |
| Identidades explícitas | ID de ingrediente → ocurrencias con resolution=explicit |
| Candidatos | ID candidato → ocurrencias con sus métodos y evidencia léxica |
| Inventario | Recuentos derivados de registros, ocurrencias y claves, sin confundir sus denominadores |

Los registros conservan metadatos originales, rendimientos, duraciones, evidencia con alcance, pasos, referencias y diagnósticos. Las listas invertidas referencian el registro, sin copiar íntegramente la receta. Una ocurrencia se identifica mediante ID exacto de receta e índice de posición de base cero en la lista ingredients; su localizador de origen permanece accesible en el registro. No se deduplican ocurrencias de una misma receta, aunque una consulta posterior pueda devolver recetas únicas. Los campos nulos se conservan; no se inventa una categoría ni un valor desconocido para rellenar índices. El esquema concreto de serialización deberá documentarse con el prototipo.

## Normalización y límites semánticos

La identidad de receta y los IDs de ingrediente son cadenas literales: REC-0017 y REC-17 son distintos. No se fusionan por equivalencia numérica. Para claves de texto se propone normalización Unicode NFC, casefold y colapso de espacios, conservando diacríticos y puntuación; no se aplicarán sinónimos, stemming ni singularización. Las claves vacías se excluyen, sin eliminar sus registros originales. La normalización de búsqueda no redefine la utilizada por el extractor al producir candidatos.

El texto indexado del ingrediente será el campo name cuando exista; raw permanece accesible como evidencia y no se mezcla con name en el mismo índice. Las alternativas compuestas se conservan como una única ocurrencia. La presencia textual no equivale a identidad confirmada ni a necesidad de compra. Una identidad explícita debe provenir del campo ingredient_id de una ocurrencia marcada explicit. Los candidatos permanecen separados incluso si hay uno solo; se preservan múltiples métodos de un mismo candidato sin duplicar la referencia a la ocurrencia. No se generan nuevas identidades, relaciones ni equivalencias.

## Reconstrucción y determinismo

El mismo contenido de entrada y la misma versión del constructor deben producir bytes idénticos. Ordenar claves de mapas y referencias por ID literal y posición; conservar el orden de listas de origen. La serialización JSON UTF-8 propuesta para la vista de intercambio no compromete una tecnología de persistencia. No incluir marcas de tiempo, rutas absolutas ni datos de ejecución no deterministas. Los artefactos generados se mantienen fuera del corpus canónico, bajo site/ en el prototipo, sin versionar sus resultados como nuevas fichas. El índice se reconstruye completo; no hay actualizaciones parciales en este alcance.

## Vista de intercambio 0.2.0

La cabecera incorpora `index_version`, `contract_version`, `extractor_version`, `stage=recipe_index_ingredients_preview`, `source_commit` y `projection_sha256` (huella de los bytes exactos del JSON de entrada). `records` y `by_path` son mapas; `by_title` y `facets` contienen listas de IDs. `ingredients` contiene tres mapas independientes: `by_text`, `by_explicit_id` y `by_candidate_id`. Cada referencia contiene `recipe_id` y `position` (base cero); las referencias de candidatos añaden `methods`, lista ordenada de métodos distintos. La evidencia completa se recupera del registro original. `inventory` diferencia claves, recetas, ocurrencias y referencias a candidatos.

La generación se integra en Knowledge audit. El archivo derivado `recipe_index.json` se construye dos veces desde la misma proyección; `recipe_index_audit.json` registra la igualdad de bytes, huellas de los documentos de receta recuperados del commit Git, reconciliación de registros, facetas y referencias de ingredientes y muestras deterministas por modalidad. Los resultados están sujetos al commit de cada ejecución; el contraste no certifica la extracción culinaria ni comprueba independientemente la identidad semántica de los candidatos. Los artefactos se conservan conforme a la retención del workflow.

## Consultas previstas

El motor posterior consumirá el índice sin depender del extractor. La primera interfaz será reproducible y de solo lectura:

- Recuperación por ID literal y ruta exacta.
- Filtros por módulo físico, categoría, estado documental y estado de evidencia; prepared no implica validación de la fórmula actual.
- Coincidencia textual por nombre de ingrediente, diferenciada de coincidencia por identidad explícita y de candidato. No ampliar silenciosamente un modo al otro.
- Combinación de filtros por intersección y resultados ordenados por ID literal. Resultados vacíos válidos, no equivalentes a un error.
- Cada resultado identifica la receta, fuente y motivo de coincidencia; los filtros de ingredientes conservan la opcionalidad y las ocurrencias correspondientes.
- Una extensión posterior podrá filtrar rendimientos y duración total declarada utilizando unidades y límites compatibles. No sumar fases, no interpretar ausencia como cero, no presentar un tiempo orientativo como medición exacta.

No se incorpora búsqueda difusa, ranking, lenguaje natural, recomendación, inferencia de alérgenos ni comprobación de disponibilidad de despensa.

## Interfaz de consultas 0.1.0

El consumidor de solo lectura `tools/query_recipe_index.py` acepta exclusivamente la vista de índice 0.2.0. La interfaz inicial es una función Python y una CLI que emite JSON a stdout; no depende del extractor ni modifica archivos. Las facetas y los IDs se comparan literalmente; títulos y nombres textuales usan la normalización del índice. La coincidencia textual es de nombre completo, no de subcadena. Todas las condiciones se intersectan a nivel de receta, no exigen que diferentes condiciones coincidan en la misma ocurrencia. Sin filtros devuelve el inventario; no hay paginación ni ranking.

Ejemplos:

```bash
python tools/query_recipe_index.py --index site/knowledge-audit/recipe_index.json --id REC-0017
python tools/query_recipe_index.py --index site/knowledge-audit/recipe_index.json --physical-module 07_Cocina_Asiatica --ingredient text "salsa de soja"
python tools/query_recipe_index.py --index site/knowledge-audit/recipe_index.json --ingredient-with-optionality text "leche de coco" optional
```

Los modos son `text`, `explicit` y `candidate`; estos dos últimos reciben IDs literales de ingrediente. Se pueden repetir las opciones de ingrediente. Se devuelve cada receta una vez, ordenada por ID, junto con procedencia, evidencia y motivos por condición, incluyendo ocurrencias y evidencia de candidatos. El resultado vacío es válido; las entradas inválidas producen un error. Se presupone un índice previamente contrastado por la auditoría. Los filtros de rendimiento y tiempo, búsqueda flexible y recomendaciones no forman parte de esta interfaz.

## Evaluación dirigida del motor

La evaluación de QRY-02 se integra en Knowledge audit mediante `tools/evaluate_recipe_queries.py`. Contrasta 16 expectativas parciales basadas en fichas reales revisadas en el corte #234, comprueba recuperación completa, repetibilidad y rechazo de tres consultas inválidas. El informe `recipe_query_evaluation.json` conserva el commit, la huella del índice, resultados y muestras de consultas abiertas. Los recuentos abiertos son observaciones, no expectativas fijadas de antemano.

Se mantienen los filtros temporales y de rendimiento fuera de la interfaz 0.1.0. La evaluación mide cuántas recetas tienen una única declaración total numérica, cuántas carecen de ella o presentan ambigüedad y qué unidades de rendimiento existen. Una cifra numérica interpretada no garantiza duración completa: las expresiones orientativas y calificadores requieren revisión adicional. No sumar fases ni equiparar unidades de rendimiento diferentes. La incorporación futura de estos filtros requiere un contrato específico sobre intervalos, unidades, calificadores y tratamiento de casos desconocidos.

## Incrementos y aceptación

| ID | Incremento | Evidencia exigida |
|---|---|---|
| IDX-01 | Contrato y alcance | Revisión del contrato, correspondencia con la proyección existente y separación de responsabilidades |
| IDX-02 | Constructor e índices básicos | Casos sintéticos de identidad literal, metadatos, ruta, procedencia y errores bloqueantes |
| IDX-03 | Índices de ingredientes | Ocurrencias repetidas, opcionales, alternativas, identidades explícitas y candidatos múltiples separados |
| IDX-04 | Integración y contraste | Reconstrucción sobre un commit, igualdad de bytes, recuentos reconciliados, referencias válidas y muestras contrastables |
| QRY-01 | Motor de consultas básico | Recuperación y filtros reproducibles con explicación de coincidencias, resultados vacíos y errores de entrada diferenciados |
| QRY-02 | Evaluación dirigida | Casos reales y negativos, documentación de límites y decisión sobre filtros temporales y de rendimiento |

La integración no sustituye las validaciones estructurales ni la auditoría semántica. Los recuentos deberán compararse contra la proyección del mismo commit, no contra valores históricos. Las pruebas de recuperación no miden precisión culinaria exhaustiva. No se compromete una release, una API, persistencia definitiva ni una ampliación a todas las entidades del SGCC.

## Referencias

- [Contrato de datos de recetas](./CONTRATO_DE_DATOS_DE_RECETAS.md)
- [Arquitectura](../../architecture/ARQUITECTURA.md)
- [Modelo de conocimiento](../../architecture/MODELO_DE_CONOCIMIENTO.md)
- [Especificación de ingesta](../ingestion/ESPECIFICACION_DE_INGESTA.md)
- [Consolidación del conocimiento](../../management/CONSOLIDACION_CONOCIMIENTO.md)
