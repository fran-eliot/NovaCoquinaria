---
id: DOC-ALCANCE-RECIPE-ASSISTANT-2026
titulo: Alcance de entrega de Culinary Recipe Assistant
tipo: gestion
version: 0.1.2
estado: borrador
ultima_revision: 2026-11-19
---

# Culinary Recipe Assistant — alcance de entrega

## Base y propósito

Culinary Explorer 0.1.0 está publicado; #276 integra su cierre y el kit 2.3.0. Los tres workflows de la PR #276 finalizaron correctamente. Corte de main: `032709c4042b3c1f46f42879ea948955f88f4da6`. El asistente 0.1.0 transforma una receta seleccionada en una vista de consulta y seguimiento durante la preparación. Markdown sigue siendo fuente canónica; no se modifica la release v1.6.0.

## Recorridos

- Desde una tarjeta del explorador abrir el asistente para el ID literal seleccionado; mantener acceso separado a la ficha completa.
- Consultar ingredientes agrupados en orden original, cantidades y calificadores textuales; marcar o desmarcar cada ocurrencia como preparada, sin inferir inventario ni cocinabilidad.
- Consultar mise en place explícita cuando existe, pasos de elaboración reconocidos en su orden y puntos críticos o advertencias explícitos. Avanzar y retroceder sin saltos automáticos; marcar pasos completados y reiniciar con confirmación. El marcado no acredita cocción suficiente.
- Consultar rendimiento y tiempos declarados, sin sumar fases, convertir unidades ni derivar una duración operativa. Mostrar ausencia o ambigüedad como tal.
- Consultar enlaces a técnicas internas resueltas y a la ficha completa. Una referencia no implica que aplique a un paso particular.
- Iniciar voluntariamente un temporizador manual independiente del paso, en minutos/segundos, con pausa, reanudación y cancelación. Aviso visual y accesible al terminar; no iniciar desde cifras extraídas ni indicar que el alimento está listo. El temporizador funciona mientras la página permanece abierta; no se garantiza aviso con pestaña suspendida o dispositivo bloqueado.
- Mantener el progreso y temporizador solo en memoria de la página; recarga o cambio de receta los pierde. Sin cuentas ni almacenamiento persistente.

## Representación y límites

Generar desde los mismos bytes del índice 0.2.0 que consume Explorer una proyección adicional versionada, separada por receta para cargar solo la seleccionada. Un manifiesto de IDs y rutas de datos derivadas, construido en el mismo build, vincula commit y huella del índice; el consumidor verifica coincidencia de procedencia e ID y bloquea datos faltantes/incompatibles. Nombres de archivo seguros, rutas relativas y verificadas; no usar IDs recibidos en URL como rutas sin resolver contra el manifiesto. No versionar JSON generado ni publicar el índice completo. La unidad A definirá el esquema exacto, cobertura, validación de localizadores y contraste con fuente; reutilizar el índice sin cambios canónicos.

Usar raw, group, quantity, optionality y localizadores de las ocurrencias; preservar fracciones, rangos, unidades y alternativas. No duplicar cantidades desde distribución o pasos. Los pasos del extractor 0.4.6 son un reconocimiento parcial de procedimientos explícitos, no transcripción completa: no descartar avisos, párrafos o subfases que el extractor no reconoció. Conservar como contexto el bloque de procedimiento original y las secciones explícitas de preparación, seguridad/alérgenos, puntos críticos, conservación y notas pertinentes, según un criterio conservador documentado. Mostrar siempre aviso de consultar ficha completa y opción de abrirla; si no se puede garantizar la delimitación de un bloque, mostrar fuente completa en lugar de una guía supuestamente exhaustiva. No inferir seguridad ni ocultar texto crítico por avanzar un paso. Renderizar datos como texto, sin HTML no confiable; los enlaces se construyen solamente desde rutas internas validadas. Respetar evidence y alcance original.

Muestras documentales del corte: curry amarillo de pollo REC-0017 (grupos, mise en place, nueve pasos, 74 °C declarados fuera de elaboración); pastel de manzana REC-0079 (840 g y distribución 640/200, horneado orientativo, lemon curd histórico frente a mermelada propuesta); talo REC-573 (6 unidades, rango de agua, 3–5 min por cara, pendiente); berenjenas Sichuán REC-0190 (fracciones, alternativas, pasos por encabezados, formulación no confirmada). Son expectativas de contraste, no resultados aún ejecutados.

## Criterios de aceptación

| ID | Criterio |
|---|---|
| AST-01 | Una representación por receta del índice del mismo commit, ID literal y huella verificables; manifiesto y datos reproducibles |
| AST-02 | Rechazo de ID desconocido, procedencia inconsistente, esquema inválido y rutas inseguras; sin carga parcial engañosa |
| AST-03 | Ingredientes, grupos, cantidades originales, alternativas, opcionalidad y localizadores preservados sin inferencia |
| AST-04 | Rendimiento y tiempos declarados conservados; desconocidos/ambiguos explícitos; sin cálculo ni escalado |
| AST-05 | Pasos reconocidos en orden con texto y localizador; contexto de procedimiento no omitido; fallback a ficha cuando delimitación insuficiente |
| AST-06 | Mise en place, advertencias y puntos críticos explícitos visibles con procedencia; no inferir seguridad ni certificación |
| AST-07 | Evidencia y alcance originales; propuesta, elaboración histórica y fórmula actual no confundidas |
| AST-08 | Checklist reversible por ocurrencia; progreso de pasos explícito, navegación y reinicio; sin mutar datos fuente |
| AST-09 | Temporizador manual validado con inicio, pausa, reanudación, cancelación y aviso al completar; independiente de cocción |
| AST-10 | Estado efímero de sesión explicado y reinicio al cambiar de receta/recargar; sin persistencia |
| AST-11 | Acceso desde Explorer, retorno y enlace a ficha; técnicas internas verificadas cuando se exponen |
| AST-12 | Interfaz adaptable, teclado, foco, etiquetas y avisos accesibles; recorrido móvil y escritorio |
| AST-13 | Carga/error/ausencia de pasos o datos diferenciados; texto seguro y sin dependencias externas en ejecución |
| AST-14 | Regresión de Explorer, contraste de muestras y corpus, temporizador con reloj controlado y recorridos Chromium |
| AST-15 | Build reproducible, comprobación de destinos y publicación por flujo vigente; guía y evidencia de uso con límites |

## Unidades de implementación

| Unidad | Entrega | Criterios principales |
|---|---|---|
| A — Recipe Assistant Data | Proyección, manifiesto, procedencia y contexto conservador | AST-01–07 |
| B — Cooking Session | Estado de checklist, pasos y temporizador con pruebas puras | AST-08–10, 14 |
| C — Recipe Assistant UI | Vista de cocina, integración de interacción y enlaces | AST-03–13 |
| D — Integration | Build, contrastes, pruebas de navegador, guía y cierre | AST-11–15 |

No se establece un ciclo de discovery independiente. La aceptación conjunta depende de evidencia ejecutada, no de la mera implementación.

## Exclusiones

Escalado, conversión de unidades, sustituciones, inferencia de seguridad, nutrición, alérgenos inferidos, compatibilidad, despensa, compra, planificación, IA, edición de fichas, persistencia, backend, API y nueva release. La deuda semántica conserva su alcance. La selección de tecnología se limita al consumidor estático existente; las decisiones de capacidades posteriores quedan abiertas.

## Referencias

- [Culinary Explorer](./ALCANCE_CULINARY_EXPLORER.md)
- [Contrato de recetas](../specifications/knowledge/CONTRATO_DE_DATOS_DE_RECETAS.md)
- [Contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md)
- [Roadmap](./ROADMAP.md)
- [Deuda de requisitos](./DEUDA_REQUISITOS_CULINARIOS.md)

## Unidad A — Contrato de publicación derivada

`tools/build_recipe_assistant.py` consume los bytes del índice 0.2.0 y las fuentes Git de su commit. Genera un directorio nuevo con manifest.json y un JSON por ID literal, cuyo nombre es el SHA-256 hexadecimal de los bytes UTF-8 del ID seguido de .json. El manifiesto (esquema 0.1.0) conserva index_version, source_commit, index_sha256, recipe_count y recipes (mapa de ID a file, sha256 del JSON, source_sha256 y href). Los registros repiten esquema, versión de índice, commit y huella de índice; contienen id, title, source_path, source_sha256, href, ingredients, steps, yield, durations, evidence, mise_en_place, context, techniques y diagnostics seleccionados. El consumidor posterior deberá contrastar manifiesto, registro y procedencia con Explorer.

Ingredientes: posición desde cero y campos raw, name, group, quantity, optionality y source_location originales; no se publican candidatos ni se reinterpretan cantidades. Pasos: order desde uno, source_number, text y source_location originales. Rendimiento nulo no distingue por sí solo ausencia de ambigüedad; los diagnósticos y cuerpo de origen permiten consultar la declaración. Duraciones conservan fases y texto sin cálculos. Mise en place recoge encabezados explícitos y descendientes; vacío no implica que no haga falta preparar ingredientes.

Se adopta el modo conservador context.mode=full_source para todas las fichas: cuerpo completo desde el final del front matter, con saltos de línea normalizados, y localizador. No se afirma que los pasos reconocidos sean el procedimiento completo; la interfaz deberá mostrar contexto y acceso a la ficha, con advertencias disponibles durante toda la sesión. No se copia el front matter completo ni el índice completo. Técnicas: referencias resueltas bajo 00_Bases/03_Tecnicas con destino Markdown preparado, etiqueta, ruta y localizador; no se asignan a pasos automáticamente. La existencia del HTML final se comprueba en D.

El generador contrasta huellas de bytes de origen, inventario, rutas, secciones, ingredientes seleccionados, pasos, rendimiento, duraciones y evidencia mediante el extractor existente; valida límites de localizadores. Esta reconciliación no constituye evaluación independiente de precisión del extractor. Se añaden seis pruebas sintéticas y doble generación con comparación de archivos en Knowledge audit. Los datos quedan como artefacto de auditoría hasta D; no se modifica Explorer ni se publican nuevas fichas. Los resultados de CI quedan pendientes de ejecución.

## Unidad B — Sesión de cocina

El módulo `assets/recipe-assistant-session.mjs` ofrece dos componentes puros, sin DOM, red ni persistencia. createCookingSession(recipe) valida ID y orden de ingredientes y pasos; mantiene posiciones preparadas y órdenes completados como conjuntos independientes. snapshot devuelve copias ordenadas, move acepta +1 o -1 y limita el cursor al intervalo válido (null sin pasos); marcar un paso no avanza ni acredita cocción. reset restaura el estado inicial. Un nuevo objeto de sesión no hereda progreso.

createManualTimer(now) admite un reloj monótono inyectable (por defecto performance.now). La duración manual se expresa en minutos enteros no negativos y segundos enteros 0–59, entre un segundo y 23 h 59 min 59 s. Los estados son idle, running, paused y finished. El plazo se calcula a partir del reloj, no contando intervalos de refresco. pause conserva el tiempo restante, resume fija un nuevo plazo, cancel restaura idle y snapshot detecta vencimiento y redondea hacia arriba para la presentación en segundos. No se sustituye un temporizador activo sin cancelarlo. El temporizador no modifica pasos ni ingredientes. La interfaz deberá confirmar reinicio, cancelar temporizador al reiniciar sesión, anunciar el vencimiento y explicar límites de suspensión, recarga y cambio de receta.

Se incorporan nueve pruebas Node con reloj controlado: ocurrencias duplicadas y reversibilidad, navegación y finalización independientes, aislamiento y reinicio, ausencia de pasos e inputs inválidos, plazo y redondeo, pausa/reanudación/cancelación, vencimiento previo a pausa, validación de duración/reloj e independencia respecto de la sesión culinaria. Knowledge audit las ejecuta con el Node 22 existente. La UI, el aviso real y la integración en navegador permanecen pendientes; no se cambia la versión de aplicación ni se publica una release.
