---
id: DOC-REQUISITOS-CULINARIOS-2026
titulo: Investigación del modelo de requisitos culinarios
tipo: gestion
version: 0.2.0
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

## Referencias

- [Compatibilidad culinaria](./INVESTIGACION_COMPATIBILIDAD_CULINARIA.md)
- [Revisión estratégica](./REVISION_ESTRATEGICA_CULINARIA.md)
- [Contrato de datos](../specifications/knowledge/CONTRATO_DE_DATOS_DE_RECETAS.md)
- [Contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md)
