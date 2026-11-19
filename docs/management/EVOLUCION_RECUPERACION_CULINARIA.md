---
id: DOC-EVOLUCION-RECUPERACION-2026
titulo: Evolución de la recuperación del conocimiento culinario
tipo: gestion
version: 0.1.5
estado: borrador
ultima_revision: 2026-11-19
---

# Evolución de la recuperación del conocimiento culinario

## Situación y evidencia

Tras el merge de #236, main se encuentra en `50ad8cb55afad6772624af612010ce12f643ca37`. El [job de PR #236](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44514156962/job/135525701712), snapshot `d05805e30e4ecf7cadaa9b9f0ddbc71f425fec6c`, registra 81 pruebas, 16 casos de consulta, tres entradas inválidas rechazadas, 590 huellas verificadas, reconstrucción idéntica, cero avisos semánticos y cero huérfanos. El snapshot de CI no es el merge; no se inspeccionó íntegramente el ZIP.

Índice 0.2.0, extractor 0.4.6 y consultas 0.1.0: 590 recetas, 5.047 ocurrencias, 5.046 textuales en 2.588 claves; 36 explícitas, 1.044 candidatas únicas y 3.967 sin candidato ni identidad. Los modos actuales comparan nombres completos normalizados o IDs literales. El candidato procede de título exacto o alias revisado, no de una resolución confirmada. Los resultados abiertos de #235 son observaciones, no estimaciones de precisión.

## Problema

El usuario culinario necesita recuperar expresiones con calificadores y formatos distintos sin perder las diferencias relevantes entre productos. Ampliar la recuperación de texto no exige ampliar la identidad; identificar un ingrediente no demuestra disponibilidad, intercambiabilidad, necesidad de compra ni ausencia de alérgenos.

## Alternativas

| Alternativa | Aporte | Riesgo y dependencia |
|---|---|---|
| A. Recuperación textual flexible | Encontrar nombres compuestos y variantes gráficas | Falsos positivos; exige semántica explícita de coincidencia y contraste |
| B. Identidades de ingredientes | Mejorar candidatos y revisión de correspondencias | Confundir variantes, familias y equivalencias; exige evidencia documental |
| C. Tiempo y rendimiento | Filtrar declaraciones útiles | Solo 101/590 con total numérico único; calificadores e intervalos requieren contrato |
| D. Consumidor de despensa | Aplicación práctica del conocimiento | Depende de identidad, alternativas, cantidades, unidades y opcionalidad; riesgo de declarar disponibilidad indebida |

Se propone evaluar A y B conjuntamente, con experimentos independientes y conservando los modos actuales. C y D quedan como alternativas posteriores; no se descartan. No se seleccionan tecnologías ni se autoriza implementación o release por este documento.

## Hipótesis de recuperación

Comparar la línea base exacta con una modalidad explícita de búsqueda por secuencia de términos completos, insensible a mayúsculas y, como variante experimental separada, a diacríticos. No utilizar subcadenas arbitrarias, sinónimos automáticos, stemming ni expansión silenciosa. El resultado debe identificar la regla usada, la expresión íntegra y su localizador. Una mención en una alternativa se presenta como mención, no como ingrediente obligatorio. Los aciertos textuales no modifican el extractor, los IDs, las cantidades ni la opcionalidad.

## Hipótesis de identidad

Evaluar un repertorio acotado de calificadores de preparación y alias revisados contra fichas de Despensa y ocurrencias originales. Separar grafía, preparación, presentación, variedad, familia y producto distinto. Conservar candidatos múltiples, ausencia de candidato y resolución explícita original. Una posible correspondencia no sustituye un ID explícito. No generalizar una regla por frecuencia ni promover candidatos automáticamente; una decisión editorial futura requeriría evidencia y alcance por separado.

## Casos de contraste propuestos

| Expresión de consulta | Ocurrencia ilustrativa | Interpretación esperada |
|---|---|---|
| ajo | ajo picado | Mención textual; posible candidato sujeto a contraste |
| ajo | ajo negro | Mención textual; no equivalencia de producto |
| ajo | ajonjolí | No coincidencia por término completo |
| salsa de soja | salsa de soja oscura | Mención textual; preservar variedad |
| aceite | aceite de cacahuete o girasol | Mención; alternativa sin dividir automáticamente |
| leche | leche de coco | Mención textual, no identidad de leche animal |
| limón | ralladura de limón | Mención; preservar forma de uso |
| sal | salsa de soja | No coincidencia por término completo |

Son expectativas ilustrativas, no resultados observados ni un conjunto representativo. Deben complementarse con ocurrencias reales identificadas por receta y posición, casos negativos y expresiones no resueltas.

## Evaluación propuesta

| ID | Actividad | Evidencia esperada |
|---|---|---|
| RET-D01 | Línea base y muestras | Corpus fijado, consultas y expectativas parciales revisadas; denominadores separados |
| RET-D02 | Experimento textual | Comparación exacta frente a términos completos; nuevos resultados y falsos positivos revisados, sin cambiar modos existentes |
| RET-D03 | Experimento de candidatos | Reglas acotadas, muestras positivas y negativas, distinción de variantes y conflictos, sin promoción de identidad |
| RET-D04 | Síntesis | Resultados por regla, límites, riesgos, coste de mantenimiento y decisión explícita sobre alcance de entrega |

Medir ocurrencias y recetas únicas por separado. No presentar una muestra dirigida como estimación estadística de recall o precisión del corpus. Un resultado incremental no es necesariamente correcto; se revisará evidencia de falsos positivos y negativos. Conservar reproducibilidad, procedencia por commit y los 16 casos de consulta vigentes. Los experimentos deberían producir artefactos derivados, sin modificar fichas ni contratos de producción antes de decidir el alcance.

## RET-D01 — Línea base fijada y muestras

El corpus experimental queda fijado al merge #237, `c0dd020dea003d8a4f7a0278a43f30d81501a7f0`, con extractor 0.4.6 e índice 0.2.0. El fixture `tools/fixtures/retrieval_baseline_cases.json` contiene 18 expectativas parciales de seis recetas de cinco módulos, revisadas en sus fuentes. Cada caso identifica ID literal, ruta, posición de base cero, línea de origen, nombre proyectado esperado y consulta. Se contrastan la procedencia, el nombre y el resultado exacto con la reconstrucción del corte fijado; los resultados de las modalidades experimentales son expectativas, no observaciones.

Modalidades a contrastar en RET-D02:

- exact: comportamiento vigente (NFC, casefold, espacios; conserva puntuación y diacríticos).
- terms: secuencia contigua de palabras completas, NFC y casefold, sin eliminar diacríticos.
- folded: misma secuencia, con eliminación experimental de diacríticos; no se aplica a IDs.

No se expanden plurales, no se unen términos separados por otras palabras y no se transforma una mención textual en identidad. Los casos incluyen puntuación, calificadores, alternativas, formas de uso, productos distintos, diacríticos y falsos positivos por subcadena. Para cada modalidad, contar ocurrencias y recetas únicas, conservar el nombre original y reportar discrepancias con las expectativas. Las muestras deliberadas no permiten estimar precisión ni exhaustividad general.

La reconstrucción de este corte mediante las herramientas vigentes es una prueba de regresión de la línea base, no una obligación de mantener indefinidamente compatibilidad con todas las versiones futuras. Si cambia el extractor o el índice, versionar o adaptar explícitamente la evaluación sin reescribir las expectativas históricas. RET-D03 requiere un conjunto independiente de expectativas de identidad y fichas de Despensa contrastadas.

## RET-D02 — Experimento textual aislado

El script `tools/experiment_retrieval_text.py` reconstruye el corte fijado de RET-D01 y compara tres modalidades sobre 17 consultas, con informe JSON en `site/knowledge-audit/retrieval_text_experiment.json`. Se utilizan secuencias contiguas de tokens alfanuméricos Unicode: la puntuación y el guion bajo actúan como separadores. La versión folded elimina marcas combinantes después de descomposición NFD, incluyendo la tilde de ñ; esta pérdida de distinciones requiere especial cautela. No hay expansión de plurales, inferencia de identidad ni interpretación de negaciones.

El informe registra por modalidad recuentos de ocurrencias y recetas distintas, diferencias respecto de la modalidad anterior, referencias completas de las ocurrencias añadidas o retiradas y contraste de los 18 casos fijados. Las diferencias no se interpretan automáticamente como aciertos culinarios. Las pruebas sintéticas cubren límites léxicos, contigüidad, diacríticos, ocurrencias repetidas e inputs inválidos. Knowledge audit ejecuta el experimento sin alterar los modos del motor vigente. La revisión de resultados y falsos positivos queda pendiente de la evidencia de ejecución y de la síntesis.

## RET-D03 — Experimento conservador de candidatos

El [job de RET-D02](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44517050880/job/135535659644) registra 18/18 casos y 87 pruebas. Recetas recuperadas exacta/terms: aceite 0/448, ajo 103/298, sal 53/423, limón 4/165, salsa de soja 10/45. La consulta limon recupera 165 en folded frente a cero en las otras modalidades. Son menciones, no identidades ni medidas de precisión.

RET-D03 prueba cinco reglas de etiquetas completas revisadas en cuatro fichas de Despensa: preparación y tamaño de ajo, escurrido de atún en conserva, pelado y descorazonado de manzana y molienda fina de harina de maíz no precocida. La preparación y presentación se conservan en el texto de origen. No se amplían candidatos existentes ni se alteran identidades explícitas o ambiguas. Se reutiliza la normalización del candidato vigente y se admite una coma tras ajo únicamente cuando el resultado es una etiqueta revisada. No se eliminan calificadores arbitrarios ni se dividen alternativas. Las etiquetas se contrastan con la ficha y el ID del corte fijado.

El fixture `tools/fixtures/retrieval_identity_cases.json` contiene 12 casos documentales y 10 negativos sintéticos. El informe `retrieval_identity_experiment.json` conserva procedencia, propuestas por ocurrencia, recuentos por regla e ingrediente y casos sin ampliación. Los negativos son ausencia de nuevas propuestas, no negación de relaciones existentes. Los casos documentales fueron seleccionados deliberadamente para contraste de reglas, no para validación independiente ni estimación estadística. Las nuevas correspondencias siguen siendo propuestas experimentales y no se incorporan al índice ni al extractor. El contraste de conflictos preserva todos los candidatos sin escoger uno.

## RET-D04 — Síntesis y propuesta de alcance

### Evidencia del corte

La PR #240 está fusionada en `f3f1a121a21d28358bb3f9b99464041aec18c58f`. Los dos workflows de la PR finalizaron correctamente. El [job de contraste](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44517868515/job/135538482522) registra 90 pruebas, cero advertencias semánticas, cero huérfanos, 18/18 casos textuales, 12/12 casos documentales de identidad y 10/10 negativos sintéticos. Ambos experimentos reconstruyeron el mismo corpus fijado en RET-D01, con huella de proyección `d72cb4cb48f8ab112d3f60003bb8a20acfe295925756e6456b12bf7b2648a89c`. La evidencia procede de los registros de CI; no se ha inspeccionado exhaustivamente el contenido de los artefactos ZIP.

| Consulta | Recetas exact | Recetas terms | Recetas folded |
|---|---:|---:|---:|
| aceite | 0 | 448 | 448 |
| sal | 53 | 423 | 423 |
| ajo | 103 | 298 | 298 |
| limón | 4 | 165 | 165 |
| azúcar | 36 | 140 | 140 |
| leche | 5 | 66 | 66 |
| salsa de soja | 10 | 45 | 45 |
| limon | 0 | 0 | 165 |
| cafe | 0 | 0 | 8 |

Son consultas seleccionadas, no estimaciones de precisión o exhaustividad culinaria. No sumar recetas de diferentes consultas. La recuperación por términos permite encontrar variantes de preparación y menciones, pero puede incluir productos distintos, alternativas o expresiones como «sin sal». No se interpretan negaciones ni se deduce disponibilidad. La normalización folded elimina también la distinción entre n y ñ; no se recomienda trasladarla sin una política ortográfica explícita y nuevos casos de contraste.

| Regla | Nuevas ocurrencias propuestas |
|---|---:|
| G01: preparación de ajo | 56 |
| G02: tamaño de ajo | 6 |
| G03: atún en conserva escurrido | 7 |
| G04: manzana pelada y descorazonada | 2 |
| G05: harina fina de maíz no precocida | 1 |
| Total | 72 |

Las 72 ocurrencias corresponden a 71 recetas distintas. Todas son propuestas adicionales sin identidad explícita ni candidato previo. Sobre 5.047 ocurrencias, la cobertura potencial de identidad o candidato pasa de 1.080 a 1.152 (21,40 % a 22,83 %); las 36 identidades explícitas no cambian. Quedarían 3.895 ocurrencias sin candidato ni identidad. El aumento de cobertura no mide exactitud. No se ha revisado individualmente la totalidad de las 72 propuestas. Los ejemplos positivos se eligieron para contrastar las reglas y no son un conjunto de validación independiente.

### Comparación de alternativas de entrega

| Alternativa | Alcance | Valor y limitaciones |
|---|---|---|
| A. Recuperación textual acotada | Nuevo modo explícito terms sobre el índice existente | Alto incremento de menciones recuperadas; bajo coste de mantenimiento; conserva la separación de identidades |
| B. Recuperación y candidatos simultáneos | A más incorporación de las cinco reglas | Mayor cobertura potencial, pero evidencia dirigida insuficiente para promoción; requiere revisión individual y gobernanza de reglas |
| C. Normalización flexible completa | A más folded y expansión léxica | Facilita escritura sin acentos; riesgo de colisiones y semántica no contrastada, especialmente ñ |
| D. Mantener prototipo | Sin nuevos modos | Mínimo riesgo, pero no materializa el valor observado |

Se recomienda A como primera entrega acotada. B se mantiene como línea de evaluación de candidatos, condicionada a la revisión de las 72 propuestas y a una decisión explícita sobre mantenimiento; C requiere contraste ortográfico adicional. D sigue siendo una alternativa válida si no se prioriza la recuperación.

### Condiciones propuestas para una futura entrega A

- Conservar exactamente los modos text, explicit y candidate de la interfaz vigente; añadir un modo explícito de términos completos, sin activarlo por defecto.
- Mantener el índice 0.2.0 y el extractor 0.4.6, salvo incompatibilidad demostrada; no alterar fuentes ni identidades.
- Recuperar ocurrencias mediante secuencias contiguas de términos completos, con la normalización contrastada en terms. No incorporar folded, plurales automáticos, sinónimos, ranking ni interpretación de negaciones.
- Mantener intersección de filtros, opcionalidad, deduplicación por receta, orden literal de ID, procedencia y explicación por ocurrencia.
- Contrastar los 18 casos de RET-D01 en las modalidades aplicables, preservar los 16 casos del motor vigente y añadir pruebas de integración de filtros, resultados vacíos, errores y preservación de candidatos.
- Distinguir claramente menciones textuales de identidades confirmadas; advertir sobre términos negados, alternativas y productos distintos.
- Verificar resultados sobre el corte fijado y sobre el corpus disponible al entregar, sin asumir que ambos tienen las mismas cifras.

La propuesta requiere aceptación del alcance antes de la implementación. No constituye autorización de una release, persistencia, API, planificación, despensa automática ni recomendación culinaria.

## Propuesta de entrega acotada

La síntesis RET-D04 se integró mediante #241 con ambos workflows satisfactorios. La alternativa A se desarrolla en el [alcance de entrega de recuperación textual](./ALCANCE_RECUPERACION_TEXTUAL.md), con criterios RET-01–RET-14 y cuatro unidades propuestas. Su implementación queda condicionada a la aceptación del alcance; las propuestas de identidad y folded permanecen experimentales.

## Límites y decisión pendiente

La prioridad propuesta es recuperación flexible y candidatos conservadores. El diseño de experimentos, su ejecución y una eventual entrega son etapas distintas. El resultado de esta revisión no constituye autorización de un nuevo modo de producción, resolución masiva, persistencia, API, RAG, runtime o release. Se mantienen los principios de Markdown canónico y separación entre automatización y consumo.

## Referencias

- [Consolidación del conocimiento](./CONSOLIDACION_CONOCIMIENTO.md)
- [Contrato de datos de recetas](../specifications/knowledge/CONTRATO_DE_DATOS_DE_RECETAS.md)
- [Contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md)
- [Modelo de conocimiento](../architecture/MODELO_DE_CONOCIMIENTO.md)
