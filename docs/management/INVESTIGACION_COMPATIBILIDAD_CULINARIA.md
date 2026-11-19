---
id: DOC-COMPATIBILIDAD-CULINARIA-2026
titulo: Investigación de compatibilidad culinaria
tipo: gestion
version: 0.1.0
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

## Referencias

- [Revisión estratégica](./REVISION_ESTRATEGICA_CULINARIA.md)
- [Contrato de datos](../specifications/knowledge/CONTRATO_DE_DATOS_DE_RECETAS.md)
- [Contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md)
- [Investigación de recuperación](./EVOLUCION_RECUPERACION_CULINARIA.md)
