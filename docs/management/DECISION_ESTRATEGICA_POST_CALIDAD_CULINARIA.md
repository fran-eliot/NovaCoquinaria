---
id: DOC-DECISION-CAPACIDAD-POST-CALIDAD-2026
titulo: Decisión estratégica tras el piloto de calidad culinaria — Unidad D
tipo: gestion
version: 0.1.0
estado: propuesta-de-decision
ultima_revision: 2026-11-22
---

# Decisión estratégica — Culinary Knowledge Quality Baseline, Unidad D

## Corte de decisión

Se analiza el proyecto en `main` tras la fusión de la [PR #346](https://github.com/fran-eliot/NovaCoquinaria/pull/346), commit `3c9b8d024ec2c7502987620b448f9ade35bdc7b0`, con los tres workflows de PR finalizados en `success` y ninguna PR abierta al tomar este corte. Última release publicada: **v1.7.0 — Culinary Applications & Workflows**. Las cinco aplicaciones estáticas siguen integradas, con datos personales locales sin sincronización ni backend.

Esta decisión utiliza tres tipos de evidencia separados:

1. [Unidad A](./LINEA_BASE_CALIDAD_CULINARIA.md): auditoría reproducible de un **corte anterior** (`7bc20e9a019d95445a13f59b109d52185c450a18`), que no se confunde con métricas vivas de este commit.
2. [Unidad B](./EVALUACION_MUESTRA_CALIDAD_CULINARIA.md): revisión documental de una muestra fija de **ocho recetas**, dirigida y no estadísticamente representativa.
3. [Unidad C](./CIERRE_PILOTO_CALIDAD_CULINARIA.md): **seis correcciones editoriales** integradas, dos controles sin cambio y ocho recorridos locales de Chromium correctamente ejecutados, sin prueba culinaria doméstica posterior ni aceptación manual individual del sitio público.

## Qué hemos aprendido

**El acceso informático funciona en los recorridos dirigidos, pero la utilidad práctica de la receta sigue siendo el límite que más conviene abordar.** El piloto detectó deficiencias concretas en cantidades de salsas referenciadas, procedimiento según proteína, condiciones de agua y conservación, aun cuando las fichas contenían ingredientes y pasos reconocidos por el extractor. Las correcciones mejoraron la claridad documental observada; su eficacia gastronómica real **no está validada**.

El corte de Unidad A registra 590 recetas; todas con ingredientes y pasos extraídos. Pero únicamente 284/590 incluyen alguna duración numérica reconocida, y solo **101/590** presentan un **total temporal numérico único** según la evaluación de consultas del mismo job. El rendimiento numérico se reconoce en 492/590. Estos campos tienen denominadores diferentes y un extractor limitado: no se deben convertir en porcentajes de recetas listas para cocinar.

La identidad explícita de ingredientes se documenta en **36 de 5.047 ocurrencias**, con 1.044 candidatos no confirmados. Esto limita automatismos como «puedes cocinarla con tu despensa» o sustituciones seguras; no justifica alterar masivamente las fichas ni activar recomendaciones inferidas.

La proyección reconoce **6 `prepared`, 373 `pending` y 211 `unknown`**, pero su reconocimiento documental no es la verdad histórica sobre preparaciones del propietario. Mantener esa separación es más valioso que aumentar artificialmente la cifra de recetas «probadas».

## Alternativas comparadas

| Alternativa | Beneficio cercano | Viabilidad y riesgos | Decisión propuesta |
|---|---|---|---|
| **A · Recipe Practical Completeness**: suficiencia práctica, tiempos, cantidades, pasos y evidencia, con revisión trazable | Alto: mejora la utilidad de Explorer y Assistant sobre el contenido ya disponible | Exige lectura humana dirigida; se puede empezar sin modificar esquema | **Priorizar evaluación y piloto acotado** |
| B · Normalización de identidad y requisitos culinarios | Alto potencial técnico futuro | Baja evidencia actual de semántica segura; candidatos no validados | Mantener como deuda e investigar solo casos con valor demostrado |
| C · Nuevos filtros automáticos por tiempo/raciones | Beneficio visible en consulta | «Alguna duración» no garantiza total; riesgo de precisión engañosa | No implementar hasta fijar datos fiables y una necesidad comprobada |
| D · Más recetas tradicionales o nuevos dominios | Amplía repertorio | El volumen adicional sin revisión podría multiplicar errores y redundancias | Incorporación selectiva, sin objetivo de cantidad |
| E · Backend, sincronización, RAG o recomendaciones desde Pantry | Posible valor futuro | Mayor arquitectura, coste, privacidad y suposiciones culinarias | Diferir; no es la siguiente gran capacidad |

La comparación es cualitativa y basada en los artefactos del proyecto. **No** se dispone aquí de entrevistas independientes, analítica real de uso ni prueba A/B con usuarios.

## Recomendación: Recipe Practical Completeness — fase de descubrimiento acotada

Proponer una capacidad de **suficiencia práctica verificable de las recetas**, entendida como un proceso editorial y de medición de condiciones concretas, no como una etiqueta automática «cocinable» ni un nuevo motor de inferencia. Antes de construir filtros o cambiar el esquema, se debe determinar qué falta para que el lector prepare una receta con garantías documentales razonables y qué datos son verificables.

### Unidad RPC-A — Contrato de suficiencia y diagnóstico

- Definir criterios observables para ingredientes (incluidas bases referenciadas), pasos, tiempos totales y parciales, rendimiento, decisiones condicionales y procedencia de experiencia; separar `presente`, `interpretado`, `no_declarado`, `desconocido` y `no_aplica`.
- Reutilizar **los informes y proyecciones existentes**. No crear un segundo catálogo de métricas ni reetiquetar automáticamente las 590 fichas.
- Registrar con ejemplos los casos de salsa por plantilla, tiempo parcial frente a total, tipo de proteína y receta probada frente a formulación propuesta.
- Elaborar un **diagnóstico de viabilidad**, denominadores y límites antes de modificar el modelo canónico o la interfaz.
- Entregar alternativas para revisión, sin autorizar ni comprometer una versión nueva.

### Unidad RPC-B — Muestra ampliada y casos de uso (condicionada)

Tras revisar RPC-A, seleccionar una muestra nueva que incluya también los **cinco módulos ausentes** en B01–B08 (pastas, legumbres, postres, bebidas y horno), con reglas fijadas antes del examen. La selección debe buscar variedad, no atribuir representatividad estadística. Contrastarla desde receta fuente, Explorer y Assistant y decidir si la mejora es editorial o funcional.

### Unidad RPC-C — Piloto selectivo (condicionada)

Solo si existe evidencia suficiente, corregir fichas con defectos concretos en PR pequeñas, conservar formulaciones mejores y variantes y diferenciar claramente propuestas de elaboraciones realizadas. Medir antes y después sobre los mismos casos; detener la intervención cuando el beneficio no sea demostrable. No añadir puntuación global ni emitir garantías de seguridad alimentaria.

### Unidad RPC-D — Decisión de producto posterior (condicionada)

Decidir con resultados si merece la pena incorporar visualización de campos fiables, filtros estrictamente basados en datos explícitos o un nuevo componente. Un `go` a una PR documental de Unidad D **no** autoriza automáticamente las unidades RPC-B/C/D, un backend ni una release.

## Puertas y condiciones de parada

- **DG-01:** cifras ligadas a SHA, fecha, denominador y script; una medición nueva no reescribe silenciosamente la anterior.
- **DG-02:** jamás declarar «probada» por heurística ni convertir candidatos semánticos en identidades explícitas.
- **DG-03:** distinguir utilidad editorial observable de ejecución culinaria doméstica; no prometer seguridad, exactitud de tiempos ni disponibilidad automática.
- **DG-04:** conservar mejores recetas, variantes y procedencia; no imponer un formato homogéneo a cambio de perder riqueza culinaria.
- **DG-05:** no desarrollar filtros avanzados sobre campos insuficientes o parcialmente interpretados; una tasa elevada de incertidumbre conduce a abstención.
- **DG-06:** nuevas capacidades, esquema o release requieren revisión y autorización diferenciadas.

## Decisión solicitada

**Aprobar únicamente la prioridad estratégica de Recipe Practical Completeness y el alcance de diagnóstico RPC-A**, sin publicar una versión, crear un nuevo milestone ni aprobar las unidades posteriores. El cierre del ciclo Culinary Knowledge Quality Baseline A–D sería entonces **Complete — Bounded Evidence & Strategic Recommendation**, sujeto a la revisión de esta propuesta. Hasta esa aprobación, esta es una recomendación documentada, no un compromiso de producto.

Referencias: [Kit de continuidad](./NOVACOQUINARIA_KIT_CONTINUITY.md), [Estado del proyecto](./PROJECT_STATUS.md), [Revisión estratégica anterior](./REVISION_ESTRATEGICA_POST_ACEPTACION_PUBLICA.md), [Deuda de requisitos](./DEUDA_REQUISITOS_CULINARIOS.md).
