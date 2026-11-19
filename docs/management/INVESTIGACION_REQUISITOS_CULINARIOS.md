---
id: DOC-REQUISITOS-CULINARIOS-2026
titulo: Investigación del modelo de requisitos culinarios
tipo: gestion
version: 0.3.0
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

## Referencias

- [Compatibilidad culinaria](./INVESTIGACION_COMPATIBILIDAD_CULINARIA.md)
- [Revisión estratégica](./REVISION_ESTRATEGICA_CULINARIA.md)
- [Contrato de datos](../specifications/knowledge/CONTRATO_DE_DATOS_DE_RECETAS.md)
- [Contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md)
