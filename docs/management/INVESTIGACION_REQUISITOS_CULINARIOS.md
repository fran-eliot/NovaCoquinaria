---
id: DOC-REQUISITOS-CULINARIOS-2026
titulo: Investigación del modelo de requisitos culinarios
tipo: gestion
version: 0.5.1
estado: borrador
ultima_revision: 2026-11-19
---

# Culinary Requirements Model

## CRM-D01 — Propósito y alcance de investigación

### Punto de partida

Tras la integración de #256, el corte de referencia es `d54e56e135020257ac58fd2f9564fa7e44d720eb`. Los tres workflows de main finalizaron correctamente. La [investigación de compatibilidad](./INVESTIGACION_COMPATIBILIDAD_CULINARIA.md) mostró viabilidad técnica acotada, pero utilidad operativa insuficiente para justificar una entrega productiva: 590 recetas indeterminadas sin confirmaciones manuales. Se adopta la alternativa B como dirección de investigación, sin aprobar una entrega de CCE.

### Problema

Una lista de ingredientes no siempre representa una conjunción de obligaciones. Puede contener alternativas, grupos de acompañamiento, elementos condicionales, cantidades netas o presentaciones específicas. La estructura editorial puede aportar contexto que no aparece en cada línea aislada. Una identidad conceptual tampoco acredita equivalencia entre formatos.

El ejemplo del curry verde de pollo (REC-0023) documentado en CCE-D05 muestra alternativas de arroz en líneas separadas y expresiones condicionales clasificadas como required. No se conoce la prevalencia de esos problemas en el corpus.

### Preguntas y fronteras

| ID | Pregunta de investigación |
|---|---|
| CRM-Q01 | ¿Qué estructuras de requisitos aparecen en las recetas y en qué contexto documental? |
| CRM-Q02 | ¿Qué deuda procede de la proyección y cuál requiere aclaración de la fuente canónica? |
| CRM-Q03 | ¿Cómo preservar alternativas dentro de una línea y entre líneas sin imponer simultaneidad? |
| CRM-Q04 | ¿Cómo distinguir requisitos, opcionales, condiciones, acompañamientos y ambigüedad? |
| CRM-Q05 | ¿Cómo conservar identidad, presentación, cantidad y procedencia sin promover equivalencias? |
| CRM-Q06 | ¿Qué representación derivada ofrece una mejora verificable con mínima complejidad? |

### Plan de investigación

| Incremento | Resultado esperado |
|---|---|
| CRM-D01 | Propósito, preguntas, límites y criterios de evaluación |
| CRM-D02 | Inventario reproducible del corpus: señales, localizadores, recuentos y límites |
| CRM-D03 | Contraste documental dirigido, incluyendo negativos y muestras ajenas al ajuste |
| CRM-D04 | Comparación de representaciones y experimento aislado, con casos fijados y regresión |
| CRM-D05 | Síntesis de evidencia, decisión sobre viabilidad y alternativas de entrega |

CRM-D02 distinguirá señales de defectos confirmados: una conjunción, un encabezado o un término como «opcional» no demuestran por sí solos su alcance semántico. Registrar denominadores por ocurrencia y receta, solapamientos y procedencia. El corpus histórico de RET-D01 permite comparar resultados; cualquier corpus adicional deberá fijarse explícitamente. CRM-D03 contrastará fuentes originales, no solo datos derivados.

### Criterios de evaluación

- Preservar Markdown como fuente canónica, ID literal, texto original y referencias por posición y localizador.
- Separar alternativas declaradas, conjunciones, condiciones no evaluadas y estructuras no interpretadas; evitar inferencias por mera aparición de palabras.
- No cambiar el significado de required, optional y unknown en los contratos publicados sin decisión posterior.
- Medir cobertura de representación, discrepancias, falsos positivos, abstenciones y regresiones, sin extrapolar precisión global a partir de muestras dirigidas.
- Comparar una extensión acotada del extractor, una proyección derivada independiente y la alternativa de no entregar; no seleccionar arquitectura de implementación anticipadamente.

### Límites

No se modifica en este incremento ningún motor, contrato publicado, ficha culinaria ni regla de identidad. No se aprueba un nuevo servicio, persistencia, API, ranking, sustituciones, escalado, IA o release. El experimento CCE se conserva como evidencia; su entrega productiva queda diferida. La denominación CRM identifica esta investigación, no un compromiso de componente software independiente.

## CRM-D02 — Inventario de señales

Corpus fijado RET-D01 `c0dd020dea003d8a4f7a0278a43f30d81501a7f0` y huella de proyección `d72cb4cb48f8ab112d3f60003bb8a20acfe295925756e6456b12bf7b2648a89c`. El inventario verifica los bytes de todas las fuentes y localizadores de ocurrencias, conserva las líneas originales y exige repetibilidad. S01 alternativa léxica en línea, S02 conector final y siguiente ocurrencia adyacente del mismo grupo, S03 conjunción, S04 marcador condicional, S05 opcionalidad léxica, S06 acompañamiento o guarnición, S07 selección finita de calificadores de presentación y preparación, S08 cantidad cualitativa según proyección. S02 cuenta ambos extremos; conectores finales sin pareja adyacente se registran aparte. Las categorías se solapan. Se registran denominadores, intersecciones, módulo, opcionalidad heredada, grupos y procedencia.

Las señales son heurísticas: no acreditan alternativas reales, condiciones ni errores; no detectan todas las estructuras, principalmente fuera de las ocurrencias proyectadas. Se ignoran destinos de enlaces para las señales. No se modifica el extractor ni se promueve identidad. Pruebas sintéticas y ejecución de CI generan `culinary_requirements_inventory.json`; los recuentos reales se documentarán después de verificar la ejecución. CRM-D03 deberá contrastar fuentes originales incluyendo negativos y casos no señalados.


## CRM-D03 — Contraste documental dirigido

### Evidencia de CRM-D02

PR #258 integrada en `17a575b60c3cae6edf97be5b380e7ab9147ad811`; los tres workflows del merge finalizaron correctamente. El [job de la PR](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44534298112/job/135595527680) ejecutó 114 pruebas sin error y verificó 590 fuentes. Se abrió el informe culinary_requirements_inventory.json del artefacto 14533739744 (snapshot dd3a043af6febcaaa13f387d8ea43837cfa7d65c, distinto del merge). Corpus y huella fijados en D02. Los recuentos siguientes son señales, no defectos confirmados.

| Señal | Ocurrencias | Recetas | Required | Optional | Unknown |
|---|---:|---:|---:|---:|---:|
| S01 | 390 | 293 | 343 | 47 | 0 |
| S02 | 2 | 1 | 2 | 0 | 0 |
| S03 | 484 | 370 | 446 | 24 | 14 |
| S04 | 129 | 108 | 82 | 47 | 0 |
| S05 | 487 | 349 | 1 | 472 | 14 |
| S06 | 24 | 14 | 18 | 6 | 0 |
| S07 | 873 | 430 | 757 | 115 | 1 |
| S08 | 105 | 95 | 81 | 23 | 1 |

De 5.047 ocurrencias, 2.030 tienen alguna señal (40,2 %), distribuidas en 573/590 recetas. Las señales se solapan; S01/S03 coincide en 27 ocurrencias, S03/S07 en 95 y S05/S07 en 112. S02 detecta un único enlace adyacente; cero conectores finales sin pareja en la heurística. No representa todos los grupos de alternativas.

### Contraste con fuentes

Se seleccionaron seis recetas adicionales a los casos de ajuste inicial CCE, de manera deliberada para contrastar clases, negativos y contexto omitido. Se cotejaron las líneas originales del commit fijado con las posiciones y opcionalidad del informe. No es una muestra estadística ni evaluación de una implementación CRM.

| Caso | Fuente, posición base cero y línea | Observación documental | Expectativa parcial |
|---|---|---|---|
| CRM-C01 | [Arroz chaufa](../../01_Arroces/arroz_chaufa.md) REC-0001, 0, L49 | Arroz jazmín o basmati, cocido y completamente frío; required | Alternativa entre variedades; la conjunción de calificadores no crea dos ingredientes; conservar 300 g y preparación compartida |
| CRM-C02 | REC-0001, 5, L54 | Un trozo pequeño de jengibre; required | Cantidad cualitativa, no cero; no deducir gramos |
| CRM-C03 | REC-0001, 9, L61 | Mirin (opcional); optional | Conservar opción explícita |
| CRM-C04 | [Merluza al horno](../../06_Pescados_y_Mariscos/merluza_al_horno_con_limon.md) REC-0057, 0, L32 y L43 | 600 g de lomos, descongelados si procede; optional | Condición de preparación, no de presencia del pescado; discrepancia confirmada de opcionalidad |
| CRM-C05 | REC-0057, 5, L37 y L46 | Sal y pimienta; required | Conjunción de dos ingredientes, sin repartir cantidades |
| CRM-C06 | [Mapo tofu](../../07_Cocina_Asiatica/mapo_tofu_de_inspiracion_sichuan.md) REC-274, 1, L32 y L48 | Carne de cerdo o ternera, opcional | Alternativa dentro de requisito opcional |
| CRM-C07 | REC-274, 4, L35 y L56 | Doubanjiang o chile y miso como adaptación | Alternativa con rama compuesta y carácter de adaptación; no equivalencia ni transferencia automática de dosis |
| CRM-C08 | [Trucha a la navarra](../../06_Pescados_y_Mariscos/trucha_a_la_navarra_rellena_de_jamon.md) REC-493, 3, L35 y L46 | 3 cucharadas de aceite, añadir si hace falta; optional | El aceite base no es opcional; el ajuste adicional es condicional; discrepancia confirmada de opcionalidad |
| CRM-C09 | REC-493, 4, L36 y L48 | Limón para acompañar; required; elaboración declara opcional | Acompañamiento opcional explícito en otra sección; discrepancia contextual |
| CRM-C10 | REC-493, 5, L37 | Sal moderada, pimienta y perejil opcional; unknown | Preservar ámbito mixto; no extender opcionalidad del perejil a toda la línea |
| CRM-C11 | [Caballa japonesa](../../06_Pescados_y_Mariscos/caballa_japonesa.md) REC-0009, 3–7, L69–77 | Guarnición, «A elegir:», cinco líneas required; S06 sin S02 | Grupo de elección explícito entre líneas sin conectores finales; no cinco obligaciones simultáneas; cardinalidad exacta y necesidad de servir guarnición quedan sin afirmar |
| CRM-C12 | [Fusilli con crema de pimientos](../../02_Pastas/fusilli_con_crema_de_pimientos_asados_y_nueces.md) REC-368, 1, L32 y L45 | Pimiento asado y pelado, bien escurrido; required | Negativo para división por conjunción: un producto con tres calificadores |

### Implicaciones

Dos discrepancias de opcionalidad se explican por confundir el ámbito de una condición de manejo/ajuste con el del ingrediente base; otra depende de evidencia de elaboración fuera de la lista. Un grupo explícito de elección no está cubierto por S02. La conjunción puede describir cualificadores, requisitos distintos o una rama compuesta; por ello no se admite una regla general de división por conectores. El corpus proyectado conserva texto útil, pero los encabezados y frases no extraídas también son evidencia relevante.

Para CRM-D04 comparar una representación plana con anotaciones de alcance frente a una representación lógica acotada de grupos y miembros, conservando ocurrencias y localizadores. No interpretar expresiones arbitrarias; abstenerse cuando ámbito o cardinalidad no estén acreditados. Los doce casos constituyen expectativas parciales derivadas de revisión, no resultados de ejecución. D04 debe fijar expectativas comprobables antes del código y añadir negativos sintéticos y muestras de contraste no utilizadas en el ajuste. No se cambia el contrato, extractor, identidad ni fichas.


## CRM-D04A — Modelo lógico candidato

### Corte y opciones

#259 integrada en `0934cb12b2b36e862727231d8f70814ad9248e36`; los tres workflows de main finalizaron correctamente. Se conservan el corpus y la huella de D02. Evaluar tres representaciones, sin decidir entrega:

| Alternativa | Representación | Límite |
|---|---|---|
| A | Anotaciones planas por ocurrencia | No expresa agrupación arbitraria ni ramas compuestas sin convenciones adicionales |
| B | Árbol lógico como representación principal | Mayor coste de migración y riesgo de perder datos originales |
| C | Ocurrencias originales intactas más árboles derivados parciales | Requiere trazabilidad y cobertura explícita, permite abstención |

C es la hipótesis recomendada para el experimento. Comparar además extensión integrada del extractor frente a proyección experimental separada; para investigar se usa esta última, sin seleccionar arquitectura productiva. La opción de no entregar sigue abierta.

### Semántica candidata

Unidad de salida: requisito anotado asociado a una o varias ocurrencias originales de la misma receta y a evidencia documental adicional cuando sea necesaria. El árbol no reemplaza las ocurrencias ni altera su opcionalidad de origen. Cada nodo tiene tipo, hijos ordenados si procede, evidencia, y alcance de presencia (required, optional, conditional, unknown). conditional conserva una condición literal no evaluada. role distingue base, accompaniment, unknown; accompaniment no implica optional.

| Tipo | Semántica |
|---|---|
| atom | Concepto textual único; no genera un ID de ingrediente |
| all | Conjunción documentada; cada miembro conserva su propio alcance |
| any | Alternativa documentada; no presupone exclusividad ni exactitud de dosis |
| choice | Selección declarada con cardinalidad no determinada |
| opaque | Expresión conservada cuya estructura o alcance no se ha interpretado |

Las cantidades originales se conservan en la ocurrencia. Una cantidad compartida se vincula al grupo cuando consta su alcance; nunca se copia a cada miembro de una conjunción o adaptación. Los calificadores se adjuntan al ámbito acreditado, como texto; una condición de preparación o ajuste se distingue de la condición de presencia (preparation, adjustment, presence, unknown). No se interpretan cantidades, condiciones, sustituciones ni disponibilidad en este ciclo. La marca adaptation conserva una alternativa culinaria declarada, no una equivalencia.

### Integridad y abstención

- Identidad de origen: commit, huella de proyección, receta, ruta, huella de fuente, posición y línea; toda evidencia adicional conserva sus líneas y texto original. Los nodos derivados no son nuevas ocurrencias del índice.
- Mantener todas las ocurrencias, incluidas duplicadas; las raíces forman una partición de posiciones sin pérdidas ni duplicación. Dentro de una raíz pueden reutilizarse referencias a la misma línea para describir partes de una expresión. No duplicar recuentos por esa reutilización.
- Sin evidencia revisada, producir una raíz opaque por ocurrencia, con alcance unknown, conservando separadamente la opcionalidad heredada. No asumir atomicidad por ausencia de señales. Un grupo parcial no puede presentarse como exhaustivo.
- Identidades explícitas y candidatos se conservan en la ocurrencia original. Ninguna división textual distribuye automáticamente IDs entre hijos ni promueve candidatos. No crear IDs nuevos ni unir grupos por nombre.
- Para el experimento, interpretaciones documentales acotadas mediante declaraciones revisadas ligadas al corpus; validar referencias, tipos, aridad, ausencia de solapamiento de raíces, procedencia y estructura. No confundir representación de una interpretación manual con extracción automática de semántica.

### Expectativas fijadas para el contraste

| Caso | Estructura esperada | Alcance y límites |
|---|---|---|
| CRM-C01 | any(arroz jazmín, arroz basmati) | required; 300 g compartidos; cocido y completamente frío |
| CRM-C02 | atom(jengibre) | required; cantidad cualitativa original |
| CRM-C03 | atom(mirin) | optional |
| CRM-C04 | atom(lomos de merluza) | required; descongelación condicional de preparación |
| CRM-C05 | all(sal, pimienta) | required; sin asignar cantidades |
| CRM-C06 | any(carne picada de cerdo, carne picada de ternera) | optional; 180 g compartidos |
| CRM-C07 | any(doubanjiang, all(chile, miso)) | required; segunda rama adaptation; no trasladar dosis |
| CRM-C08 | atom(aceite de oliva) | required; 3 cucharadas base, ajuste condicional |
| CRM-C09 | atom(limón) | optional, accompaniment; evidencia L36 y L48 |
| CRM-C10 | all(sal moderada, pimienta, perejil) | primeros dos required; perejil optional; no extender opcionalidad |
| CRM-C11 | choice(cinco guarniciones) | accompaniment; presencia y cardinalidad unknown; evidencia L69–77 |
| CRM-C12 | atom(pimiento rojo) | required; asado, pelado y escurrido; no dividir calificadores |

Contraste adicional fijado fuera de los doce casos CRM-C01–C12, no utilizado para ajustar las futuras reglas: [ensalada de alubias](../../03_Legumbres/ensalada_alubias_blancas_con_atun.md) REC-0109, L34 (un producto con cocción y escurrido; no dividir), L42 (perejil optional), L43 y L63 (sal y pimienta negra, all); [fusilli con atún](../../02_Pastas/fusilli_atun_limon_alcaparras.md) REC-0117 L43 y L55–63 (sal y agua de cocción, all; no afirmar que agua de cocción sea agua disponible de despensa). REC-0117 ya fue utilizado en CCE; estas líneas no pertenecen a los doce casos CRM. Los cuatro casos adicionales son expectativas documentales, no evidencia independiente de revisión humana externa.

### Plan de ejecución

D04B fijará datos revisados y expectativas en archivos separados, ejecutará un prototipo aislado y comparará A (anotación plana) y C (árbol parcial) sobre el mismo conjunto. B se compara conceptualmente por coste de sustitución; no se exige una segunda implementación completa. Distinguir capacidad representacional de cobertura automática: medir ocurrencias anotadas, opacas, raíces, evidencia preservada, casos representables y discrepancias, no precisión clínica ni culinaria global. Añadir negativos sintéticos: conjunción de calificadores, grupo solapado, referencias inexistentes, aridad inválida, adaptación con dosis no justificada, elección sin cardinalidad y condición sin evaluar. Validar repetibilidad y ausencia de mutación del índice. Si se explora reconocimiento automático, separar sus resultados y casos no ajustados; una anotación manual no demuestra automatización. D05 decidirá si el valor justifica una entrega acotada o diferirla.

No se aprueba modificación del extractor, contrato, índice, fichas, motor CCE, infraestructura ni release.

## CRM-D04B — Prototipo representacional

Se fijan 16 anotaciones revisadas y expectativas de forma y alcance en archivos JSON separados. El prototipo verifica corpus, huella, líneas, posiciones, aridad, tipos y partición; preserva ocurrencias y genera raíces opacas para las posiciones no anotadas. Se compara un modelo plano restringido a anotaciones atómicas por ocurrencia con el híbrido; no se implementa un modelo plano con convenciones de agrupación adicionales. El contraste no constituye reconocimiento semántico automático, ni validación independiente de cada calificador o dosis: las expectativas comprueban forma y alcance raíz. El informe CI registra cobertura manual, abstención y reproducibilidad. No se cambia ningún contrato ni motor publicado. Resultados pendientes de ejecución.


## CRM-D05 — Síntesis y decisión propuesta

### Evidencia y límites

#261 integrada en `aa436c303143d3679223ef0ee53b982776e9502b`; los tres workflows de main finalizaron correctamente. El [job de la PR](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44553000211/job/135661435212) ejecutó 121 pruebas sin error. Se abrió localmente el informe requirements_model_experiment.json del artefacto 14543454216 (snapshot 0c7f87f7aee6c35816b774eca31473f6d3a1c4e1, distinto del merge). Corpus y huella de proyección idénticos a D02. Huellas de anotaciones b9a7cfdd4eda377ccb7cacbf79bfe3f48ef1da7dcff03de6aa5e2783886f744b y expectativas 2337755055ede2416d36622cdf75c355c3767447fcdf0e2fe426cc8c2ecbaa5f.

| Medida | Resultado |
|---|---:|
| Recetas conservadas | 590 |
| Ocurrencias originales conservadas | 5047 |
| Recetas con anotaciones | 8 |
| Ocurrencias revisadas | 20 |
| Ocurrencias opacas | 5027 |
| Raíces anotadas | 16 |
| Raíces atom/all/any/choice | 8/4/3/1 |
| Casos representables en plano atómico restringido | 8/16 |
| Casos representados en híbrido | 16/16 |

Las formas y presencia raíz de los 16 casos coinciden con las expectativas fijadas; se verificaron procedencia, partición, repetibilidad y ausencia de mutación. No se ha medido exactitud de interpretación automática: el 0,40 % anotado es esfuerzo de muestra manual, no estimación de cobertura alcanzable. El cálculo del plano es una comparación con un criterio restringido, no un prototipo general de anotaciones planas con agrupación. Las expectativas no verifican independientemente cada miembro, calificador, alcance de dosis ni condición. Las siete pruebas nuevas incluyen aridad, adaptación, elección, condición y ausencia de promoción; faltan pruebas unitarias específicas de solapamiento y referencias inexistentes aunque el prototipo valida ambos. Las declaraciones revisadas se mantienen como evidencia experimental, no datos de autoridad de producción.

### Alternativas

| Alternativa | Evaluación |
|---|---|
| A — Entregar representación híbrida con anotaciones manuales | Viable como representación acotada; no demuestra coste sostenible ni mejora de disponibilidad |
| B — Investigar reconocimiento determinista acotado de estructuras sobre fuentes | Recomendada: medir si se obtiene evidencia útil sin edición masiva ni división indiscriminada |
| C — Integrar directamente el modelo en extractor/índice | Prematura, implicaría cambio de contrato sin evidencias de automatización |
| D — Diferir CRM y priorizar otro consumo de conocimiento | Válida si B no muestra valor incremental |

Resultado propuesto: viabilidad representacional acotada del híbrido; reconocimiento automático no demostrado; entrega productiva diferida. No seleccionar todavía un contrato ni arquitectura de integración. Mantener CCE diferido.

### Siguiente investigación propuesta

Evaluar un reconocimiento acotado dentro de una proyección experimental separada, con señales como localizadores y no como verdad. Priorizar patrones documentales de ámbito inequívoco: grupos de elección con encabezado y declaración explícita, alternativas entre líneas con conectores, opcionalidad explícita y condiciones de preparación o ajuste claramente delimitadas. No comprometer todos estos patrones antes de revisar muestras. No dividir por conjunción de forma general, transferir cantidades o inferir cardinalidad ni identidades. Definir corpus fijado, conjunto de ajuste y conjunto de contraste disjunto por receta, expectativas documentales previas, negativos y abstención. Comparar contra la línea base heredada, registrar denominadores, falsos positivos, omisiones, coste de revisión y trazabilidad. Incluir pruebas de referencias y solapamiento antes de una eventual entrega. Si la evidencia es insuficiente, conservar el modelo como investigación y evaluar alternativas de consumo del conocimiento.

La decisión queda pendiente de revisión; no se aprueba Delivery Scope, cambios productivos, release ni nueva infraestructura.

### Disposición de la investigación

Tras la integración de #262 y la continuación de la línea de investigación, se adopta la alternativa B de CRM-D05. CRM queda cerrado como ciclo representacional acotado, sin prueba de reconocimiento automático ni aprobación de entrega. Se inicia [CRR](./INVESTIGACION_RECONOCIMIENTO_REQUISITOS.md). CCE permanece diferido; no se aprueba un cambio de contrato ni una release.

## Referencias

- [Compatibilidad culinaria](./INVESTIGACION_COMPATIBILIDAD_CULINARIA.md)
- [Revisión estratégica](./REVISION_ESTRATEGICA_CULINARIA.md)
- [Contrato de datos](../specifications/knowledge/CONTRATO_DE_DATOS_DE_RECETAS.md)
- [Contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md)
