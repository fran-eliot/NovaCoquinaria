---
id: DOC-COMPATIBILIDAD-CULINARIA-2026
titulo: Investigación de compatibilidad culinaria
tipo: gestion
version: 0.2.0
estado: borrador
ultima_revision: 2026-11-19
---

# Investigación de compatibilidad culinaria

## CCE-D01 — Casos de uso y requisitos

### Punto de partida

Tras la publicación de v1.6.0 y el merge #250, el corte de investigación es `2c1e8d340bb9563fd7f0173043fe65a2f90724f8`. Los tres workflows del merge finalizaron correctamente. Se reutilizan el extractor 0.4.6, índice 0.2.0 y motor de consultas 0.2.0; no se altera su comportamiento. El inventario histórico de #246 (5.047 ocurrencias, 36 explícitas, 1.044 candidatas y 3.967 sin resolver) motiva la evaluación, no fija objetivos de cobertura.

### Casos de uso

| ID | Necesidad | Resultado esperado |
|---|---|---|
| UC-01 | Explorar recetas ante una lista de ingredientes | Compatibilidad de presencia documentada, no garantía de elaboración |
| UC-02 | Identificar carencias | Ausencia declarada o ausencia bajo inventario cerrado e identidad suficientemente acreditada |
| UC-03 | Distinguir opcionales | Carencias opcionales separadas; no bloquean por sí solas |
| UC-04 | Identidad incierta | Evidencia de coincidencia y abstención explícita, sin promoción automática |
| UC-05 | Lista parcial | Lo no declarado permanece desconocido |
| UC-06 | Entender resultados | Motivos por ocurrencia y resumen explicable |
| UC-07 | Distinguir presencia de cantidad suficiente | Cantidad no evaluada; no presentar presencia como suficiencia |
| UC-08 | Consultar la fuente | ID literal, ruta, commit, posición y localizador original |

### Entradas y fronteras

La entrada candidata es el índice derivado contrastado, una selección explícita de recetas o el corpus, y una declaración temporal de disponibilidad aportada por el usuario. Estudiar entradas con IDs literales y etiquetas textuales, sin deducir que un texto coincidente acredita identidad. La lista es abierta salvo declaración explícita de exhaustividad; incluso en una lista cerrada no se resuelven por ausencia los ingredientes ambiguos. No asumir agua, sal ni aceite como disponibles. Las declaraciones contradictorias o inválidas requieren un tratamiento explícito en CCE-D03. No persistir datos personales ni modificar fuentes.

Las salidas deberán distinguir identidad y estado de disponibilidad, conservar opcionalidad y no perder ocurrencias repetidas. El diseño de estados y agregación se decidirá en CCE-D03; no hay puntuación ni ranking aprobado. Una coincidencia de presencia no implica cantidad, conservación, seguridad alimentaria ni posibilidad práctica de cocinar.

### Requisitos de investigación

| ID | Requisito |
|---|---|
| CCE-R01 | Consumir una versión explícitamente compatible del índice sin releer ni modificar Markdown en el consumidor. |
| CCE-R02 | Mantener separados identidad explícita, candidato, coincidencia textual y falta de resolución. |
| CCE-R03 | Diferenciar lista abierta y cerrada; no convertir silencio en ausencia sin condiciones. |
| CCE-R04 | Preservar required, optional y unknown; no dar por opcional un caso indeterminado. |
| CCE-R05 | Conservar alternativas compuestas y calificadores; no inferir sustitución, equivalencia ni disponibilidad por subcadena. |
| CCE-R06 | No evaluar suficiencia cuantitativa; mantener la cantidad original accesible. |
| CCE-R07 | Explicar cada ocurrencia con evidencia y procedencia; conservar repeticiones. |
| CCE-R08 | Resultados reproducibles, errores explícitos y separación de resultados vacíos válidos. |
| CCE-R09 | No alterar contratos vigentes ni promoción de candidatos sin decisión y evidencia diferenciadas. |
| CCE-R10 | No declarar seguridad, elaboración confirmada ni compatibilidad total de una receta a partir de coincidencias parciales. |

### Muestras documentales iniciales

Leídas en el corte indicado; son escenarios de investigación, no resultados ejecutados ni conjunto independiente de validación.

| Fuente | Escenario | Expectativa parcial |
|---|---|---|
| [Curry amarillo de pollo](../../05_Carnes/curry_amarillo_de_pollo.md) (REC-0017) | Leche de coco enlazada; azúcar y arroz de acompañamiento opcionales | Explorar identidad explícita; distinguir opcionales. Pechuga o contramuslo no son dos obligaciones. |
| [Pipirrana jiennense](../../04_Verduras/pipirrana_jiennense_con_atun_y_huevo.md) (REC-485) | Atún en conserva escurrido, ajo pequeño, vinagre opcional | No equiparar atún fresco con conserva; guardar calificadores; separar vinagre. |
| [Talo vasco](../../10_Horno/talo_vasco_de_maiz_en_plancha.md) (REC-573) | Harina fina de maíz no precocida, agua y sal | No equiparar harina precocida; agua no implícita; cantidad e intervalo no verificados. |
| [Berenjenas estilo Sichuán](../../07_Cocina_Asiatica/berenjenas_chinas_estilo_sichuan.md) (REC-0190) | Aceite de cacahuete o girasol; soja clara y oscura; cebolla opcional | No dividir automáticamente alternativa ni equiparar las dos salsas; conservar evidencia histórica y cantidades. |

### Criterios para evaluar viabilidad

CCE-D02 contrastará individualmente las 72 propuestas experimentales y examinará su relevancia para los casos de uso. CCE-D03 comparará alternativas de representación, estados y política de disponibilidad. CCE-D04 fijará un corpus y expectativas documentales adicionales no utilizadas para ajustar reglas; incluirá casos sintéticos negativos, listas abiertas y cerradas, identidades ambiguas, opcionalidad, duplicados, errores y ausencia de cantidades. Medirá resultados por ocurrencia y receta, denominadores, discrepancias, falsos positivos y abstenciones, repetibilidad y trazabilidad mediante recorrido independiente. Las muestras deliberadas no estimarán precisión global. Una afirmación positiva no respaldada es un defecto, aunque aumente cobertura. CCE-D05 sintetizará valor y limitaciones, incluida la opción de no entregar.

### Exclusiones

Sin implementación productiva, catálogo automático de equivalencias, inventario persistente, compras, escalado, planificación, ranking, API, RAG, agentes ni release. CCE-D01 no compromete el diseño final ni autoriza promover las 72 propuestas.


## CCE-D02 — Contraste de candidatos de identidad

### Evidencia y método

CCE-D01 está integrado en #251; los tres workflows del merge `11478bcdf2867cad523b8b647bc59675bd875cdf` finalizaron correctamente. Se recuperó y abrió el ZIP original del [experimento RET-D03](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44517868515) (artefacto 14526277399). Se inspeccionaron las 72 entradas de `additions` de `retrieval_identity_experiment.json`, incluido raw, name, resolución, opcionalidad, regla y localizador. Corpus fijado `c0dd020dea003d8a4f7a0278a43f30d81501a7f0`, huella de proyección `d72cb4cb48f8ab112d3f60003bb8a20acfe295925756e6456b12bf7b2648a89c`. Se leyeron las cuatro fichas de destino en ese commit. Es revisión individual de texto proyectado, no relectura independiente de las 71 recetas Markdown completas ni certificación de extracción.

| Regla | Ficha | Ocurrencias | Juicio y condición |
|---|---|---:|---|
| G01 | [Ajo](../../11_Despensa/06_Verduras/ajo.md) ING-0014 | 56 | Coherencia conceptual; dientes frescos, conservar preparación |
| G02 | ING-0014 | 6 | Coherencia conceptual; tamaño no equivale a cantidad estándar |
| G03 | [Atún en conserva](../../11_Despensa/12_Conservas/atun_en_conserva.md) ING-0080 | 7 | Coherencia conceptual; conserva y peso escurrido, no atún fresco |
| G04 | [Manzana](../../11_Despensa/17_Frutas/manzana.md) ING-0084 | 2 | Coherencia conceptual; conservar pelado, descorazonado y peso neto |
| G05 | [Harina de maíz no precocida](../../11_Despensa/01_Cereales/harina_de_maiz_no_precocida.md) ING-0126 | 1 | Coherencia conceptual; conservar molienda fina y no precocción |

Las 72 propuestas son coherentes con el concepto de destino según raw y ficha, sin contradicción observada en esta revisión. Todas están clasificadas required por la proyección, sin validación independiente de esa clasificación. No se declaran identidades explícitas ni disponibilidad. La ficha de ajo incluye formatos deshidratados: disponer de un ID genérico no acredita disponer de dientes frescos. De manera análoga, las fichas de atún y harina no justifican equivalencia con cualquier presentación, ni las de manzana suficiencia neta.

### Registro individual

Cada fila identifica ID literal, posición de base cero, línea del corpus fijado y regla revisada. Juicio común: coherente como candidato, no confirmado como disponibilidad; aplican las condiciones específicas de la tabla anterior. El raw completo y la ruta se conservan en el artefacto.

| Receta | Posición | Línea | Regla |
|---|---:|---:|---|
| REC-0007 | 1 | 77 | G01 |
| REC-0028 | 3 | 38 | G01 |
| REC-0032 | 4 | 38 | G01 |
| REC-0033 | 3 | 37 | G01 |
| REC-0036 | 2 | 38 | G01 |
| REC-0060 | 1 | 33 | G01 |
| REC-0079 | 0 | 36 | G04 |
| REC-0086 | 0 | 31 | G04 |
| REC-0102 | 5 | 35 | G01 |
| REC-0103 | 5 | 39 | G02 |
| REC-0104 | 3 | 37 | G01 |
| REC-0106 | 4 | 38 | G01 |
| REC-0107 | 5 | 39 | G01 |
| REC-0108 | 3 | 37 | G01 |
| REC-0110 | 4 | 38 | G01 |
| REC-0111 | 4 | 38 | G01 |
| REC-0115 | 4 | 38 | G01 |
| REC-0117 | 2 | 36 | G01 |
| REC-0118 | 5 | 39 | G01 |
| REC-0125 | 3 | 37 | G01 |
| REC-0127 | 3 | 37 | G01 |
| REC-0128 | 4 | 38 | G01 |
| REC-0129 | 4 | 38 | G01 |
| REC-0130 | 3 | 37 | G01 |
| REC-0131 | 2 | 36 | G01 |
| REC-0132 | 3 | 37 | G01 |
| REC-0134 | 2 | 36 | G01 |
| REC-0135 | 4 | 38 | G01 |
| REC-0136 | 3 | 37 | G01 |
| REC-0140 | 7 | 41 | G01 |
| REC-0141 | 4 | 38 | G01 |
| REC-0162 | 1 | 35 | G03 |
| REC-0167 | 4 | 38 | G01 |
| REC-0171 | 4 | 38 | G01 |
| REC-0177 | 3 | 36 | G01 |
| REC-0178 | 5 | 39 | G01 |
| REC-0179 | 5 | 39 | G01 |
| REC-0181 | 2 | 36 | G01 |
| REC-0183 | 3 | 37 | G01 |
| REC-0190 | 2 | 49 | G01 |
| REC-0191 | 3 | 50 | G01 |
| REC-0193 | 4 | 50 | G01 |
| REC-0199 | 6 | 41 | G01 |
| REC-0200 | 8 | 43 | G01 |
| REC-0201 | 3 | 38 | G01 |
| REC-0204 | 3 | 38 | G01 |
| REC-0205 | 3 | 38 | G01 |
| REC-0206 | 2 | 37 | G01 |
| REC-0221 | 3 | 35 | G02 |
| REC-0247 | 1 | 32 | G03 |
| REC-0262 | 4 | 35 | G01 |
| REC-0265 | 3 | 34 | G01 |
| REC-0266 | 2 | 33 | G01 |
| REC-0281 | 5 | 36 | G01 |
| REC-271 | 2 | 33 | G03 |
| REC-274 | 2 | 33 | G01 |
| REC-279 | 10 | 41 | G01 |
| REC-307 | 4 | 35 | G02 |
| REC-347 | 4 | 35 | G01 |
| REC-351 | 2 | 33 | G01 |
| REC-367 | 1 | 32 | G03 |
| REC-368 | 3 | 34 | G02 |
| REC-381 | 3 | 34 | G01 |
| REC-406 | 2 | 33 | G01 |
| REC-409 | 6 | 37 | G01 |
| REC-444 | 3 | 35 | G01 |
| REC-480 | 3 | 35 | G02 |
| REC-485 | 3 | 35 | G03 |
| REC-485 | 4 | 36 | G02 |
| REC-546 | 3 | 35 | G03 |
| REC-573 | 0 | 32 | G05 |
| REC-574 | 3 | 35 | G03 |

### Gobernanza y relevancia

- No incorporar las cinco reglas al extractor ni modificar los candidatos existentes. Mantener el conjunto experimental separado; versionar reglas, corpus, fuente autorizada, negativos y evidencia si se propone una entrega.
- Las coincidencias G01/G02 describen preparación o tamaño, G03/G04 describen preparación y G05 presentación específica. No eliminar calificadores ni convertir identidad de concepto en equivalencia de producto.
- Exigir contraste de fuentes independiente y casos no utilizados en el ajuste antes de integrar reglas; reconsiderar cambios de ficha, conflictos y regresiones. El juicio favorable sobre las 72 entradas seleccionadas no estima precisión global.
- De 5.047 ocurrencias históricas, 36 explícitas y 1.044 candidatas permanecen sin cambios. Las 72 adicionales elevarían la cobertura potencial a 1.152 de 5.047 (22,83 %), sin alterar las explícitas; 3.895 quedarían sin identidad ni candidato. No es cobertura entregada ni disponibilidad.
- Para UC-01/02/04/05/06, estudiar por separado evidencia de identidad, presentación y declaración de disponibilidad. Un candidato único no autoriza resultado positivo; un ID genérico tampoco acredita una presentación específica. Los casos no resueltos requieren abstención. Para UC-03/07/08, preservar opcionalidad, cantidad original y trazabilidad.
- En CCE-D03 comparar un núcleo estrictamente explícito con una modalidad de evidencia candidata separada y con una alternativa de coincidencia textual informativa. No elegir aún promoción, ranking o resolución automática.

## Referencias

- [Revisión estratégica](./REVISION_ESTRATEGICA_CULINARIA.md)
- [Contrato de datos](../specifications/knowledge/CONTRATO_DE_DATOS_DE_RECETAS.md)
- [Contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md)
- [Investigación de recuperación](./EVOLUCION_RECUPERACION_CULINARIA.md)
