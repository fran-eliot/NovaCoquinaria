---
id: DOC-ALCANCE-RECUPERACION-2026
titulo: Alcance de entrega de recuperación textual
tipo: gestion
version: 0.1.0
estado: borrador
ultima_revision: 2026-11-19
---

# Alcance de entrega de recuperación textual

## Base y propósito

La síntesis de [evolución de recuperación culinaria](./EVOLUCION_RECUPERACION_CULINARIA.md) se integró mediante #241 en el commit `e127b5b840d6a422d5e8aee39c6c0b88b4d4c7c1`. Los workflows de dicha PR concluyeron correctamente. Se desarrolla la propuesta A para revisión de alcance, no una autorización de implementación. La evidencia procede de RET-D01–D04, con muestras dirigidas y sin estimación estadística de precisión.

## Entrega propuesta

Culinary Query Engine 0.2.0: añadir exclusivamente el modo de ingrediente `terms` a la función Python y CLI existentes. Mantener el extractor 0.4.6, contrato de datos 0.1.0 e índice 0.2.0. No modificar Markdown culinario, identidades ni candidatos. La versión de herramienta no implica release del proyecto.

Ejemplo de interfaz propuesta:

```bash
python tools/query_recipe_index.py --index site/knowledge-audit/recipe_index.json --ingredient terms "ajo" --ingredient terms "salsa de soja"
```

El modo text sigue comparando nombres completos; explicit y candidate conservan su semántica. terms compara secuencias contiguas de tokens alfanuméricos Unicode con NFC, casefold y separación por puntuación y guion bajo, preservando diacríticos. La consulta sin tokens se rechaza exclusivamente en el nuevo modo. No se expanden plurales, sinónimos, negaciones ni términos separados por otras palabras. Una mención no implica identidad, disponibilidad, equivalencia, necesidad de compra o seguridad alergénica.

## Diseño y compatibilidad

El consumidor utiliza las claves y postings de by_text del índice ya contrastado. No requiere extractor, Git ni PyYAML en tiempo de consulta. Un recorrido de claves es suficiente como punto de partida; no se promete latencia ni escalabilidad sin medición. Compartir la lógica pura de tokenización y contigüidad con el experimento, conservando su variante folded exclusivamente experimental. Ordenar las referencias por ID literal y posición; no duplicar ocurrencias. Mantener esquema de respuesta de modos existentes salvo query_version; para terms registrar modo y valor originales, texto íntegro, posición y localizador, y alcance de coincidencia textual. No introducir un campo obligatorio nuevo en las respuestas anteriores.

## Criterios de aceptación

| ID | Criterio |
|---|---|
| RET-01 | Los tres modos anteriores conservan resultados y evidencia, salvo versión de herramienta; 16 casos previos superados |
| RET-02 | terms es explícito en función y CLI, nunca ampliación implícita de text |
| RET-03 | Tokens completos contiguos, NFC/casefold, puntuación y guion bajo como separadores; diacríticos preservados |
| RET-04 | No coincidencia por subcadena, plural automático ni secuencia discontinua |
| RET-05 | Consulta terms sin tokens o modo desconocido es error; consulta válida sin coincidencias devuelve cero |
| RET-06 | Combinación AND con otras cláusulas y facetas, incluida opcionalidad |
| RET-07 | Recetas únicas ordenadas por ID literal, ocurrencias únicas por posición y orden estable |
| RET-08 | Procedencia, nombre, raw, posición, opcionalidad y resolución original disponibles; coincidencia identificada como textual |
| RET-09 | Alternativas y productos diferentes conservados sin inferir identidad; negación no interpretada |
| RET-10 | Índice no modificado, sin dependencia de extractor ni acceso Git en la consulta |
| RET-11 | Contraste de los 18 casos fijados en exact/text y terms; folded permanece experimental |
| RET-12 | Equivalencia de conjuntos de ocurrencias con RET-D02 para las 17 consultas del corte fijado |
| RET-13 | Evaluación sobre índice del CI vigente, con recuentos observados, procedencia y regresión; no imponer cifras históricas al corpus nuevo |
| RET-14 | Documentar modalidad, ejemplo CLI, limitaciones y cambios de versión; sin release del proyecto |

## Unidades propuestas

| Unidad | Entrega | Criterios principales |
|---|---|---|
| A | Funciones léxicas puras compartidas y recuperación por postings | RET-03, 04, 07, 10 |
| B | Integración del modo terms en función y CLI, evidencia y composición | RET-01, 02, 05–09 |
| C | Contraste en corpus fijado y vigente, integración CI e informe | RET-01, 11–13 |
| D | Documentación de contrato y cierre acotado | RET-14 y revisión conjunta de todos |

Los criterios pueden solaparse; la aceptación final exige evidencia conjunta. Las unidades se ejecutarán de forma incremental, sin declarar completitud por mera fusión. La lógica de experimentación no se elimina antes de contrastar equivalencia.

## Exclusiones y decisión pendiente

No se incorporan folded, las 72 propuestas de identidad, reglas adicionales, ranking, lenguaje natural, filtros temporales, persistencia, API, despensa, RAG ni recomendaciones. Se requiere aprobación de este alcance antes de comenzar la unidad A. No se fija release, calendario ni milestone.

## Referencias

- [Evolución de recuperación culinaria](./EVOLUCION_RECUPERACION_CULINARIA.md)
- [Contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md)
- [Consolidación del conocimiento](./CONSOLIDACION_CONOCIMIENTO.md)
