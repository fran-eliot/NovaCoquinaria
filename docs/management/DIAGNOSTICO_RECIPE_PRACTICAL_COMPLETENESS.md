---
id: DOC-RPC-A-DIAGNOSTICO-2026
titulo: Recipe Practical Completeness — RPC-A, contrato y diagnóstico
tipo: gestion
version: 0.1.0
estado: diagnostico-tecnico-acotado
ultima_revision: 2026-11-22
---

# Recipe Practical Completeness — RPC-A

## Objeto y límites

Este documento establece un **contrato de lectura editorial y diagnóstico**, no una nueva regla de validación, un campo canónico, un índice paralelo ni un algoritmo para declarar recetas «cocinables». Se inicia tras la [decisión estratégica de Unidad D](./DECISION_ESTRATEGICA_POST_CALIDAD_CULINARIA.md) y la fusión de [PR #347](https://github.com/fran-eliot/NovaCoquinaria/pull/347) en `c3386a24ab53dc298eee362b6bdb415e7a2df3c8`, con tres workflows de PR satisfactorios.

RPC-A **no modifica recetas, interfaz, esquema de Front Matter ni los scripts de extracción existentes**. Su utilidad consiste en saber qué puede afirmarse de los documentos con la evidencia disponible, qué exige lectura humana y qué debe permanecer desconocido.

## Evidencia reproducible

El corte más reciente consultado es el de [Knowledge audit #317](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/45051257428) (job `137296653983`, resultado `success`). La **proyección declara** `source_commit: 15f83df0a11897ad492f9de572599864d0297309`, SHA del checkout del job de la PR #347, **no el commit del merge**. El script `tools/audit_inventory.py` cuenta rutas; `tools/extract_recipe_metadata.py` produce la proyección; `tools/report_recipe_coverage.py` calcula cobertura descriptiva; `tools/evaluate_recipe_queries.py` distingue tiempos totales de tiempos parciales. La reproducción exige checkout del SHA de la proyección, las dependencias del workflow y los mismos comandos; no mezclar cortes ni metodologías.

| Métrica observada | Resultado | Denominador y significado |
|---|---:|---|
| Markdown versionados | 945 | Rutas Git `.md`, no solamente recetas |
| Recetas | 590 | Fichas canónicas, diez módulos |
| Ingredientes documentales | 126 | Fichas de despensa, no ocurrencias en recetas |
| Técnicas | 52 | Rutas de técnicas |
| Recetas con líneas de ingredientes reconocidas | 590 / 590 | Presencia extraída, no suficiencia |
| Recetas con pasos reconocidos | 590 / 590 | Presencia extraída, no posibilidad de reproducción |
| Rendimiento declarado | 587 / 590 | Incluye valores no interpretables |
| Rendimiento numérico reconocido | 492 / 590 | Puede usar unidades heterogéneas |
| Alguna duración declarada | 386 / 590 | Puede ser preparación, cocción o total |
| Alguna duración numérica reconocida | 284 / 590 | **No equivale** a tiempo total |
| Tiempo total numérico único reconocido | 101 / 590 | Según `temporal_coverage()`; no exactitud cronológica verificada |
| Tiempo total no declarado | 395 / 590 | Según el mismo evaluador |
| Tiempo total declarado no interpretable | 94 / 590 | Según el mismo evaluador |
| Cantidades numéricas, exactas o rangos | 4.283 / 5.047 | Ocurrencias de ingredientes, no fichas de receta |
| Identidades explícitas | 36 / 5.047 | Ocurrencias, no ingredientes distintos |
| Candidatos sobre identidades no resueltas | 1.044 / 5.011 | No equivale a identidad confirmada |
| Evidencia reconocida como preparada | 6 / 590 | Estado de proyección, no verificación independiente |
| Evidencia reconocida como pendiente | 373 / 590 | Estado de proyección |
| Evidencia desconocida | 211 / 590 | No equivale a no cocinada |

Las cifras coinciden en sus definiciones principales con el corte de Unidad A, pero no prueban que las correcciones del piloto hayan incrementado cobertura cuantitativa: **su valor era aclarar instrucciones existentes**. El incremento de archivos Markdown deriva también de documentación de gestión.

## Contrato de lectura RPC-A

Para cada eje, una revisión editorial futura utilizará una de estas cinco categorías **por observación**:

| Categoría | Uso permitido | Prohibición |
|---|---|---|
| `presente` | Dato expreso en fuente canónica, con ruta y localización; no necesariamente suficiente | No inferir resultado doméstico ni precisión |
| `interpretado` | Proyección o parser reconoce un dato bajo reglas documentadas | No atribuir certeza superior al extractor |
| `no_declarado` | Se comprobó en la fuente pertinente que el dato esperado no está expresado | No confundir con «no existe en la cocina real» |
| `desconocido` | Información no recuperada, fuente sin verificar, ambigüedad no resoluble o prueba no ejecutada | No rellenar con suposiciones ni atribuir incidencia por defecto |
| `no_aplica` | Se justifica por qué el eje no tiene sentido en ese caso | No utilizarlo para ocultar carencias |

Un mismo campo puede tener dos observaciones: por ejemplo, **rendimiento `presente` como texto** y **valor numérico `desconocido`**. Los estados no deben agregarse sin fijar unidad de análisis y denominador. Cada observación futura debe conservar `REC-ID`, ruta, SHA, sección o línea, eje, estado, justificación y si procede propuesta de mejora.

### Ejes de suficiencia práctica

| Eje | Condición documental observable | Herramienta disponible y límite |
|---|---|---|
| RPC-01 · Ingredientes | Lista, cantidades, unidades, agrupaciones, opcionales y menciones de preparaciones externas | `extract_recipe_ingredients.py`, `report_recipe_coverage.py`; reconoce ocurrencias, no asegura lista completa |
| RPC-02 · Preparaciones reutilizadas | La salsa, base o plantilla citada se puede localizar y se distingue cuánto se incorpora | `extract_recipe_details.py` y referencias; enlace resuelto no demuestra dosis utilizable |
| RPC-03 · Pasos y secuencia | Orden, técnica, punto de decisión, incorporaciones condicionales y dependencia de plantilla | `extract_recipe_content.py`; existencia de pasos no mide claridad |
| RPC-04 · Tiempos | Preparación, cocción, espera y total distinguidos; unidades y condiciones explícitas | `report_recipe_coverage.py` y `temporal_coverage()`; tiempo total único se evalúa por separado |
| RPC-05 · Rendimiento | Personas/raciones, unidades, formato de referencia y compatibilidad con cantidades | `report_recipe_coverage.py` y `temporal_coverage()`; número interpretable no demuestra escalabilidad |
| RPC-06 · Condiciones y alternativas | Descongelación, tipo/grosor de producto, ingredientes opcionales y variantes | Señales CRM y lectura documental; no resolver alternativas mediante heurísticas |
| RPC-07 · Experiencia de preparación | Preparada, pendiente, propuesta, valoración y procedencia de cantidades históricas | Estado proyectado y revisión humana; no equiparar `prepared` con prueba independiente |
| RPC-08 · Acceso útil | Explorer → Assistant → fuente; información contextual y advertencias recuperables | E07 de [Unidad C](./CIERRE_PILOTO_CALIDAD_CULINARIA.md); prueba local dirigida, no garantía de reproducción culinaria |
| RPC-09 · Límites prácticos | Condiciones críticas, alérgenos y conservación formuladas con prudencia | Revisión editorial; no certificación de inocuidad o nutrición |

El juicio de suficiencia **no** se reduce a contar ejes `presente` ni se traduce en un porcentaje global. Cada receta puede contener dependencias prácticas y decisiones legítimas que solo se resuelven consultando la fuente y, eventualmente, preparando el plato.

## Casos contrastables del piloto anterior

Se utilizan ejemplos documentales ya auditados, **no una muestra nueva ni una segunda evaluación de sus resultados**:

| Caso | Contrato implicado | Observación del piloto |
|---|---|---|
| `REC-0007` · Hamburguesa asiática | RPC-02, RPC-03, RPC-07 | La salsa china existe como plantilla, pero su cantidad de uso no puede recuperarse de la preparación doméstica anterior; #344 clarificó uso incremental |
| `REC-0009` · Caballa japonesa | RPC-02, RPC-04, RPC-07 | La experiencia muy satisfactoria no conserva la dosis de glaseado ni tiempos realmente ejecutados; #344 delimitó la referencia orientativa |
| `REC-0008` · Medallones asiáticos | RPC-03, RPC-06, RPC-07 | Ternera/cerdo requerían distinguir criterio de cocción; 265 g eran una adaptación propuesta, no ejecución confirmada |
| `REC-0021` · Arroz frito con gambas | RPC-03, RPC-09 | La indicación aislada de fuego fuerte para recalentar contradecía la cautela sobre conservación previa; #343 armonizó el texto |
| `REC-448` · Patatas a la importancia | RPC-09 | El apartado de conservación contenía texto ajeno al plato; #343 lo acotó |
| `REC-0201` · Calamares con kimchi | RPC-01, RPC-03, RPC-06 | Se declaraba agua «si fuera necesario» sin momento de incorporación; #343 explicitó el ajuste como propuesta pendiente |
| `REC-0057` y `REC-0059` | Control de no intervención | Sin mejora prioritaria identificada en la revisión documental de Unidad B |

Estos ejemplos enseñan la diferencia entre **existe un campo, enlace o paso** y **hay instrucciones reproducibles y comprobadas**. No inferir que los cambios de #343–#344 fueron comprobados en una elaboración posterior.

## Diagnóstico de viabilidad

**Viable ya, sin añadir software:** seleccionar y revisar fichas con la rúbrica anterior; identificar documentación clara, desconocidos y brechas prácticas verificables, utilizando rutas, secciones y SHA. Los informes automáticos existentes pueden orientar la selección, pero no emitir decisiones editoriales ni etiquetas «cocinable».

**No demostrado todavía:** precisión de un nuevo detector automático de suficiencia, correspondencia de nombres libres con identidades de despensa, total de trabajo culinario a partir de duraciones parciales, cantidad de salsa consumida por una receta, disponibilidad de ingredientes de Pantry, sustituciones y seguridad alimentaria.

**Riesgo prioritario:** presentar como completos campos que solo se han reconocido sintácticamente. El dato de 590/590 recetas con ingredientes y pasos, por ejemplo, convive con ambigüedades operativas localizadas en la muestra de ocho.

## Alternativas y decisión de salida RPC-A

| Alternativa | Valor y límite | Decisión propuesta |
|---|---|---|
| A · Continuar con **RPC-B, muestra ampliada** y revisión editorial orientada a suficiencia | Contrasta utilidad real en pastas, legumbres, postres, bebidas y horno, ausentes en la muestra anterior | **Recomendada, previa aprobación de protocolo y estratos** |
| B · Añadir inmediatamente un verificador automático global | Riesgo alto de convertir la presencia extraída en juicio culinario | Diferir; no hay referencia anotada suficiente para validarlo |
| C · Incorporar filtros por tiempo total y rendimiento | La cobertura confiable es limitada y heterogénea; falta validar consultas y abstenciones | Diferir hasta contraste de fuente, necesidad y semántica |
| D · Normalización masiva de ingredientes y recetas desde la proyección | Podría destruir variantes, procedencia y ambigüedades legítimas | No recomendada |
| E · Funcionalidad nueva en Planner, Pantry o backend | No responde al defecto editorial medido | Diferir |

**Recomendación de RPC-A:** aprobar solo el contrato de observación y un **protocolo acotado RPC-B**, con muestra estratificada acordada antes de revisar resultados. No autoriza cambios masivos, nuevos motores, filtros, sincronización, publicación de release ni fases RPC-C/D. La referencia global publicada sigue siendo `v1.7.0`.

## Reproducción

Checkout del commit indicado por el artefacto, Python y dependencias declaradas en el workflow `.github/workflows/knowledge-audit.yml`:

```bash
mkdir -p site/knowledge-audit
python tools/audit_inventory.py --output site/knowledge-audit/inventory.json
python tools/extract_recipe_metadata.py --output site/knowledge-audit/recipe_metadata.json
python tools/report_recipe_coverage.py --input site/knowledge-audit/recipe_metadata.json --output site/knowledge-audit/recipe_coverage.json
python tools/build_recipe_index.py --input site/knowledge-audit/recipe_metadata.json --output site/knowledge-audit/recipe_index.json
python tools/evaluate_recipe_queries.py --index site/knowledge-audit/recipe_index.json --output site/knowledge-audit/recipe_query_evaluation.json
```

Los JSON de `site/knowledge-audit/` son **salidas derivadas**, no la fuente de verdad. La auditoría de esta PR regenerará los datos con su propio SHA; el corte descriptivo arriba se mantiene ligado a la ejecución #317. Al comparar ejecuciones, conservar **los dos SHA** y el contrato del extractor, sin atribuir cambios de contenido a una variación de herramienta.
