---
id: DOC-RECONOCIMIENTO-REQUISITOS-2026
titulo: Investigación del reconocimiento de requisitos culinarios
tipo: gestion
version: 0.4.0
estado: borrador
ultima_revision: 2026-11-19
---

# Culinary Requirements Recognition

## CRR-D01 — Propósito y alcance

Tras #262 (merge `68ac1c195d9399f30b699a835e960acc67503616`), la [investigación CRM](./INVESTIGACION_REQUISITOS_CULINARIOS.md) acredita capacidad representacional acotada: 16 casos, 20 ocurrencias anotadas manualmente de 5.047; no reconocimiento automático. Se adopta la alternativa B de CRM-D05 como dirección de investigación, sin entrega productiva de CRM ni CCE.

### Preguntas de investigación

| ID | Pregunta |
|---|---|
| CRR-Q01 | ¿Qué patrones documentales permiten reconocer una estructura de requisitos sin inferencia culinaria no respaldada? |
| CRR-Q02 | ¿Qué incremento proporciona el reconocimiento respecto de la proyección y las señales actuales? |
| CRR-Q03 | ¿Qué situaciones deben permanecer opacas y cuáles necesitan revisión editorial? |
| CRR-Q04 | ¿Qué coste, trazabilidad y riesgo tiene mantener reglas deterministas? |
| CRR-Q05 | ¿Existe una capacidad acotada que justifique una entrega posterior? |

### Familias candidatas

| Familia | Hipótesis | Límite |
|---|---|---|
| P01 | Alternativas en líneas adyacentes con conector explícito | No unir grupos o líneas sin relación acreditada |
| P02 | Grupo de elección con encabezado y declaración explícita | No inferir cardinalidad ni obligatoriedad de guarnición |
| P03 | Opcionalidad inequívoca de toda una ocurrencia | No extender el marcador a componentes o grupos vecinos |
| P04 | Condición de preparación delimitada | No convertir la presencia del ingrediente en opcional |
| P05 | Condición de ajuste adicional delimitada | No alterar el requisito base ni asignar dosis extra |

Las familias son candidatas; pueden reducirse o descartarse tras contrastar fuentes. No se acomete división genérica por conectores, inferencia de alternativas anidadas, normalización de identidad, disponibilidad, suficiencia de cantidad ni equivalencia de productos. No usar las señales heurísticas como etiquetas de verdad. No se modifica Markdown canónico ni contratos existentes.

### Metodología y etapas

| Etapa | Evidencia |
|---|---|
| CRR-D01 | Alcance, límites y criterios |
| CRR-D02 | Selección de patrones y muestras documentales |
| CRR-D03 | Reglas candidatas, expectativas de ajuste y contraste fijadas |
| CRR-D04 | Prototipo experimental aislado y evaluación |
| CRR-D05 | Síntesis y decisión de viabilidad |

Corpus inicial: RET-D01, commit `c0dd020dea003d8a4f7a0278a43f30d81501a7f0`, huella `d72cb4cb48f8ab112d3f60003bb8a20acfe295925756e6456b12bf7b2648a89c`. Preservar las versiones publicadas; si se añade otro corpus, identificarlos separadamente. Seleccionar casos de ajuste y contraste disjuntos por receta; excluir del contraste las recetas de CRM y CCE ya utilizadas para ajustar las familias. Usar señales únicamente para localizar candidatos, incluyendo muestras negativas y no señaladas. Fijar expectativas documentales y localizadores antes de ejecutar y registrar las modificaciones posteriores como nueva iteración, no como éxito retrospectivo. La revisión humana realizada dentro del proyecto no equivale a validación externa independiente.

### Puertas de decisión

- CRR-G01: conservar todas las ocurrencias y sus datos de identidad, cantidad y opcionalidad original; no duplicar raíces ni perder posiciones.
- CRR-G02: cada reconocimiento debe enlazar evidencia exacta del corpus, regla versionada y alcance; sin evidencia suficiente, opaque.
- CRR-G03: cero reconocimientos incorrectos en los negativos y casos fijados del contraste para recomendar una entrega de esa familia; cualquier error obliga a restringir o diferir y reevaluar con casos nuevos. No es garantía de precisión global.
- CRR-G04: medir por familia oportunidades revisadas, aciertos, falsos positivos, omisiones y abstenciones, por ocurrencia y receta; declarar denominadores y solapamientos. Los resultados no revisados del corpus son propuestas, no aciertos.
- CRR-G05: resultados deterministas, referencias válidas, partición sin solapamientos y pruebas de regresión, incluidos casos inválidos.
- CRR-G06: documentar valor incremental y carga de revisión; si una familia no tiene contraste positivo suficiente o no reduce trabajo de revisión, no recomendar su entrega. No se fija objetivo arbitrario de cobertura.

### Fronteras

Prototipo experimental separado; no nueva dependencia, servicio, API, persistencia, IA, ranking, sustituciones, release ni integración productiva. El nombre CRR identifica el ciclo de investigación, no un componente arquitectónico obligatorio. El cierre puede concluir con una entrega acotada propuesta, una nueva restricción o diferir. Toda entrega requiere decisión y alcance diferenciados.


## CRR-D02 — Selección documental de patrones y muestras

#263 integrada en `03b9b818d93dd5f2938204eeb5884d5f25848acf`. Los workflows Knowledge integrity y Knowledge audit de la PR finalizaron satisfactoriamente. Se inspeccionó el inventario de señales del artefacto 14556389543 del run 44578067339 (snapshot b7c6f1e28e12766f64f0e30f061072bd0d9a8e64). Se contrastaron las líneas originales de las recetas indicadas en el corpus fijado, no solo las señales. La selección es dirigida.

### Decisión provisional por familia

P01 solo tiene un enlace adyacente detectado por S02 en el corpus: REC-0023, ya empleado en CCE. Diferir su reconocimiento como familia entregable por falta de contraste positivo independiente. P02 dispone de un segundo ejemplo documental, REC-0008, además de REC-0009 utilizado en CRM; mantener como exploración, sin evidencia suficiente para recomendar entrega por sí solo. P03, P04 y P05 son candidatos prioritarios a reglas restringidas. No generalizar por palabras aisladas.

### Ajuste documental

Posiciones base cero y líneas del Markdown fijado. Los casos siguientes pueden orientar reglas; no se contabilizarán como contraste independiente.

| Caso | Familia | Fuente | Posición / línea | Observación |
|---|---|---|---|---|
| A01 | P01 | [Curry verde](../../05_Carnes/curry_verde_de_pollo.md) REC-0023 | 18–19 / 93–94 | Alternativa vinculada explícitamente; acompañamiento, presencia no determinada |
| A02 | P02 | [Caballa japonesa](../../06_Pescados_y_Mariscos/caballa_japonesa.md) REC-0009 | 3–7 / 69–77 | Guarnición a elegir; cardinalidad desconocida |
| A03 | P03 | [Arroz frito con gambas](../../01_Arroces/arroz_frito_gambas.md) REC-0021 | 9,12,13 / 66,72,73 | Marcador terminal entre paréntesis; alcance completo de cada ocurrencia |
| A04 | P04 | [Gambas al ajillo](../../06_Pescados_y_Mariscos/gambas_al_ajillo.md) REC-0059 | 0 / 32,43 | Descongeladas si procede; condición de preparación |
| A05 | P03 | REC-0059 | 3 / 35,44 | Guindilla pequeña opcional, marcador separado por coma |
| A06 | P05 | [Patatas a la importancia](../../04_Verduras/patatas_a_la_importancia_castellanas.md) REC-448 | 9 / 41,50–51 | Reponer aceite si hace falta, ajuste sobre cantidad base |
| A07 | P05 | [Trucha a la navarra](../../06_Pescados_y_Mariscos/trucha_a_la_navarra_rellena_de_jamon.md) REC-493 | 3 / 35,46 | Añadir aceite si hace falta, ajuste sobre cantidad base |

### Contraste documental reservado

Las recetas de esta tabla no pertenecen a la muestra de ajuste anterior ni a las muestras representacionales y de compatibilidad CRM/CCE. Son expectativas documentales preliminares anteriores al código. La revisión procede del mismo proyecto; no es un conjunto ciego externo. Los casos positivos fuera de una regla finalmente acotada se contabilizarán como omisiones de alcance, no como éxitos.

| Caso | Familia | Fuente | Posición / línea | Expectativa semántica |
|---|---|---|---|---|
| H01 | P02 | [Medallones asiáticos](../../05_Carnes/medallones_solomillo_asiaticos.md) REC-0008 | 5–8 / 89–96 | Un grupo choice, cuatro miembros, accompaniment, presencia y cardinalidad desconocidas |
| H02 | P02 | [Hamburguesa asiática](../../05_Carnes/hamburguesa_asiatica.md) REC-0007 | 6–8 / 83–87 | Negativo: encabezado Guarnición sin declaración de elección; no agrupar |
| H03 | P03 | [Arroz frito con pollo](../../01_Arroces/arroz_frito_pollo.md) REC-0022 | 12–13 / 58–59 | Dos ocurrencias opcionales independientes |
| H04 | P03 | REC-0022 | 9 / 52 | Negativo no señalado: salsa de ostras sin marcador; no reconocer opcionalidad por analogía con otra receta |
| H05 | P03 | [Ternera con setas](../../05_Carnes/ternera_salteada_con_setas_y_mirin.md) REC-0183 | 9 / 43,71 | Negativo: opcionalidad parcial del cebollino; abstenerse de declarar todo opcional |
| H06 | P04 | [Calamares con kimchi](../../07_Cocina_Asiatica/calamares_salteados_con_kimchi.md) REC-0201 | 0 / 35,48 | Presencia requerida; descongelación condicional |
| H07 | P03 | REC-0201 | 5 / 40,53 | Salsa de soja clara opcional, marcador terminal separado por coma |
| H08 | P04/P05 | REC-0201 | 6 / 41 | Negativo: agua si fuera necesario, condición de presencia; no tratar como preparación ni incremento sobre dosis base |
| H09 | P04 | [Sepia a la plancha](../../06_Pescados_y_Mariscos/sepia_a_la_plancha_con_ajo_y_perejil.md) REC-302 | 0 / 31,42,52 | Preparación condicional; conjunción de calificadores; no dividir producto |
| H10 | P04 | [Puchero andaluz](../../05_Carnes/puchero_andaluz_con_pringa_y_hierbabuena.md) REC-491 | 5 / 37,49–50 | Desalado condicional, presencia del hueso requerida |
| H11 | P04/P03 | REC-491 | 4 / 36,49 | Costilla opcional con condición de preparación; no forzar presencia requerida |
| H12 | P05 | [Berenjenas de Almagro](../../04_Verduras/berenjenas_de_almagro_alinadas.md) REC-526 | 1 / 33,47 | Agua base y cantidad adicional condicional; no asignar cantidad extra |
| H13 | P05/P04 | [Judías verdes guisadas](../../04_Verduras/judias_verdes_guisadas_con_tomate_y_cebolla.md) REC-343 | 6 / 37,49 | Negativo: toda la dosis de agua es condicional; no deducir base requerida |
| H14 | P03 | REC-526 | 8 / 40,50 | Pimiento asado opcional; plural del marcador |
| H15 | P03 | REC-302 | 4 / 35,47 | Zumo de limón opcional, marcador terminal sin coma |

La muestra reservada incluye ocho recetas y quince casos; algunos abarcan varias ocurrencias o familias. Las posiciones se contrastaron con el inventario excepto H04, que se localizó por orden de la lista Markdown y se verificará contra la proyección fijada antes de ejecutar. Los negativos no equivalen a declarar ausencia de otros requisitos. P01 carece de contraste positivo reservado. P02 solo dispone de un positivo y un negativo dirigido.

### Condiciones para CRR-D03

Fijar fixtures de ajuste y contraste con texto exacto, ID, ruta, posición y línea. Especificar alcance, regla y resultado esperado por familia; validar corpus, disyunción por receta y preservar evidencia. No utilizar los casos H para modificar reglas después de ejecutar; si se modifica una regla, registrar iteración y reservar casos nuevos. Añadir negativos sintéticos, incluidos marcadores en enlaces, negaciones, alcance parcial, encabezados sin elección, condiciones de presencia y cantidades no acreditadas. No comprometer implementación productiva ni ampliar reglas de identidad. No se ha ejecutado todavía reconocimiento automático.


## CRR-D03 — Reglas candidatas y expectativas fijadas

#264 integrada en `86dfcbde06d7c7d24ca2a17c71ef9ba0b167effb`. Se fija la primera iteración de reconocimiento y el fixture experimental `tools/fixtures/requirements_recognition_cases.json`, con 22 casos documentales y ocho negativos sintéticos. Los localizadores de evaluación se resolverán por línea exacta y receta en el corpus fijado, no por posiciones estimadas; se rechazará toda referencia inexistente o discrepancia de fuente. El corpus y la huella son los de D01. Ajuste y contraste son disjuntos por receta. Las expectativas semánticas se conservan incluso cuando una regla acotada no pueda cubrirlas.

### Reglas de iteración 0.1.0

Normalización exclusivamente para reconocer marcadores: NFC, casefold, espacios y puntuación final editorial; retirar destinos de enlaces conservando etiquetas; conservar texto y cantidad originales. No eliminar acentos ni reconstruir nombres. Las reglas no usan ID de receta ni listas de casos como predicados. Una anotación afecta solo a la ocurrencia o grupo explícitamente identificado. No crear identidades ni afirmar atomicidad; los reconocimientos de alcance pueden conservar un nodo opaque con una anotación separada.

| Regla | Predicado acotado | Propuesta |
|---|---|---|
| CRR-R01 | Deshabilitada en esta iteración | Sin propuesta; registrar omisión de A01 |
| CRR-R02 | Subgrupo exacto Guarnición, declaración independiente A elegir:, seguido únicamente de al menos dos viñetas del mismo grupo, sin otra prosa hasta el fin de la sección; correspondencia exacta con ocurrencias proyectadas | choice con miembros opacos, role accompaniment, presencia y cardinalidad unknown; exploratoria |
| CRR-R03 | Marcador terminal literal (opcional), coma opcional o marcador separado por espacio, admitiendo plural; prefijo no vacío; rechazar conectores y/e/o/u, negación, otros marcadores condicionales, coma anterior al separador y ámbito mixto | Anotación optional sobre toda la ocurrencia; no afirmar número de ingredientes |
| CRR-R04 | Sufijo delimitado descongelado/a/os/as si procede, sin otra condición, alternativa ni opcionalidad; conservar el prefijo y el calificador | Anotación preparation, presencia base required como interpretación candidata; no interpretar condiciones |
| CRR-R05 | Cantidad base proyectada exacta o rango positivo, sufijo separado por coma reponer si hace falta o añadir si hace falta; sin alternativa ni otro marcador de condición | Anotación adjustment; base required; cantidad adicional no determinada |

R04 y R05 se restringen a las formas observadas en ajuste. No ampliar a desalado, adverbios intermedios, ni otras variantes por conocimiento del conjunto H en esta iteración. R03 incluye las variantes terminales propuestas como hipótesis general morfológica, no como garantía de alcance. Ante múltiples reglas aplicables o conflicto de grupo y anotación, abstenerse de todas en los miembros afectados y registrar motivo. No reconocer por contenido de URLs, texto fuera de la sección ni analogía entre recetas.

### Evaluación

El fixture registra expectativa semántica, no resultado esperado por implementación restringida. A01, H09, H10, H11 y H12 pueden quedar fuera del alcance de estas reglas; contabilizar omisiones, no convertir expectativas positivas en negativas. H11 exige conservar simultáneamente opcionalidad y preparación; los marcadores mixtos quedan fuera del alcance inicial. Los negativos sintéticos son entradas aisladas, sin contexto documental o cantidad base acreditada. No se exige afirmar presencia en ellos. En H02 se evalúa la ausencia de agrupación, no otros marcadores de la receta.

El informe de D04 distinguirá ajuste y contraste, casos y ocurrencias (los grupos se contabilizan también como una unidad), expectativas positivas, negativos, aciertos exactos de alcance, falsos positivos, omisiones y propuestas no revisadas. Comparará contra la opcionalidad heredada donde sea pertinente; ninguna propuesta corregirá el extractor. Los casos multirregla deben contrastarse por tipo y alcance. Las líneas de encabezado y declaración son evidencia contextual, no ocurrencias adicionales. Mantener determinismo, partición de raíces y preservación de datos, pruebas de referencias inexistentes y solapamiento. Cualquier cambio de reglas posterior al contraste requiere nueva iteración y nuevos casos reservados. No se declara ejecución ni recomendación de entrega.

## CRR-D04 — Prototipo y evaluación

Se incorpora `experiment_requirements_recognition.py` con R02–R05, R01 deshabilitada. Las propuestas conservan los datos originales y las raíces opacas; R02 genera choice con cardinalidad desconocida. La anotación de alcance no acredita atomicidad ni disponibilidad. Se verifican huellas, referencias del fixture, disyunción por receta, partición, repetibilidad y ausencia de mutación. Los conflictos producen abstención. El informe separa ajuste, contraste, negativos sintéticos, propuestas por tipo, opcionalidad heredada y resultados por caso. La clasificación de casos compuestos es conservadora: un resultado parcial no es un acierto completo; se conserva el detalle observado para análisis posterior. Los falsos positivos y omisiones son datos de evaluación, no fallos del job; los errores de integridad sí detienen la ejecución. No se modifica ninguna expectativa ni motor publicado. La evaluación por familia y carga de revisión se completará a partir del artefacto; resultados pendientes de CI.

## Referencias

- [Modelo de requisitos](./INVESTIGACION_REQUISITOS_CULINARIOS.md)
- [Compatibilidad culinaria](./INVESTIGACION_COMPATIBILIDAD_CULINARIA.md)
- [Revisión estratégica](./REVISION_ESTRATEGICA_CULINARIA.md)
