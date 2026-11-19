---
id: DOC-REVISION-ESTRATEGICA-CULINARIA-2026
titulo: Revisión estratégica global del conocimiento culinario
tipo: gestion
version: 0.1.0
estado: borrador
ultima_revision: 2026-11-19
---

# Revisión estratégica global

## Corte y evidencia

Main tras [PR #247](https://github.com/fran-eliot/NovaCoquinaria/pull/247): `fe53c5d93e1124b6579a2f32a1c4b1f7f5804528`. Sin PR abiertas en la consulta; release v1.5.0. Knowledge integrity, Knowledge audit y Deploy MkDocs del HEAD finalizaron correctamente ([integridad](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44525950968), [auditoría](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44525951341), [publicación](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44525950988)).

El corte documentado de #246 registra 590 recetas, 5.047 ocurrencias de ingredientes, 36 identidades explícitas, 1.044 ocurrencias con candidato y 3.967 sin resolver ni candidato; 102 pruebas, 18 casos textuales y cero advertencias semánticas y huérfanos según las reglas existentes. Son resultados históricos, no una auditoría individual de los artefactos ni evidencia de elaboración doméstica. El motor 0.2.0 admite text, terms, explicit y candidate; no interpreta disponibilidad, negaciones ni alternativas. Los 72 candidatos experimentales permanecen sin integrar.

## Diagnóstico

La recuperación de menciones es útil, pero no equivale a disponibilidad. La visión del SGCC exige reutilización práctica con Markdown canónico, separación de automatización y consumo, trazabilidad y simplicidad. El corpus permite estudiar una capacidad funcional sin seleccionar infraestructura de plataforma.

## Alternativas

| Alternativa | Valor | Dependencia o riesgo |
|---|---|---|
| Identidades como ciclo independiente | Alto | Cobertura no equivale a precisión; gobernanza de reglas |
| Compatibilidad acotada receta-despensa | Muy alto | Identidades, opcionalidad, incertidumbre |
| Filtros de tiempo y rendimiento | Alto | Solo 101 recetas con total numérico único en el corte #235; unidades y calificadores |
| Acceso práctico de solo lectura | Alto | Facilita consumo, no resuelve semántica |
| Escalado de cantidades | Alto | Unidades, rendimientos, proporciones y excepciones |
| Menús y compra inteligente | Alto | Requiere compatibilidad, cantidades y preferencias |
| RAG y agentes | Potencial alto | No sustituye contratos ni evaluación |

Valoración cualitativa, no resultado experimental. Se recomienda investigar compatibilidad acotada como caso de uso que oriente el refinamiento de identidades. El trabajo de identidad independiente y los filtros declarados se mantienen como alternativas si la viabilidad resulta insuficiente.

## Capacidad candidata: Culinary Compatibility Engine

Consumidor determinista de solo lectura del índice derivado y una lista declarada de ingredientes disponibles. Separar identidad explícita, candidato y coincidencia textual. No promover automáticamente candidatos, interpretar ausencia de datos como falta de ingrediente ni asumir que una lista parcial es exhaustiva. Distinguir requerido, opcional e indeterminado y conservar alternativas compuestas sin inferencia automática. Diferenciar presencia declarada, ausencia explícita bajo un inventario cerrado, incertidumbre y cantidad no comprobada. No declarar una receta cocinable por mera coincidencia textual, ni recomendar sustituciones o inferir seguridad alimentaria. Conservar fuente, commit, posición y motivos de cada resultado. Cualquier puntuación futura deberá explicitar denominador e incertidumbre y validarse antes de adoptarse.

## Investigación propuesta

- CCE-D01: casos de uso, entradas, fronteras y criterios de evaluación.
- CCE-D02: contraste de identidades, revisión individual de los 72 candidatos y gobernanza de reglas; analizar si cubren casos de uso relevantes.
- CCE-D03: alternativas de representación y compatibilidad, estados desconocidos, política de inventario abierto/cerrado y opcionalidad.
- CCE-D04: experimento aislado con corpus fijado, expectativas documentales independientes, negativos y casos ambiguos; comparar con recorrido de referencia, medir abstenciones y errores, sin extrapolar precisión global.
- CCE-D05: síntesis de evidencia y decisión de viabilidad, incluyendo alternativa de no entrega.

Una eventual entrega requerirá alcance, criterios de aceptación y decisión diferenciada. No se autoriza implementación productiva, cambio de arquitectura, persistencia, API, ranking, gestor de despensa, escalado, planificación, IA ni release. La evolución del conocimiento sigue abierta.

## Referencias

- [Visión](../VISION.md)
- [Manifiesto](../../MANIFESTO.md)
- [Arquitectura](../architecture/ARQUITECTURA.md)
- [Roadmap](./ROADMAP.md)
- [Kit de continuidad](./NOVACOQUINARIA_KIT_CONTINUITY.md)
- [Consolidación](./CONSOLIDACION_CONOCIMIENTO.md)
- [Evolución de recuperación](./EVOLUCION_RECUPERACION_CULINARIA.md)
- [Contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md)
