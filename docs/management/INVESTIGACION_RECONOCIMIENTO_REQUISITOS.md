---
id: DOC-RECONOCIMIENTO-REQUISITOS-2026
titulo: Investigación del reconocimiento de requisitos culinarios
tipo: gestion
version: 0.1.0
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

## Referencias

- [Modelo de requisitos](./INVESTIGACION_REQUISITOS_CULINARIOS.md)
- [Compatibilidad culinaria](./INVESTIGACION_COMPATIBILIDAD_CULINARIA.md)
- [Revisión estratégica](./REVISION_ESTRATEGICA_CULINARIA.md)
