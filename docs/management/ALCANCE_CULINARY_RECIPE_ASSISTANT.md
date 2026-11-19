---
id: DOC-ALCANCE-RECIPE-ASSISTANT-2026
titulo: Alcance de entrega de Culinary Recipe Assistant
tipo: gestion
version: 0.1.5
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

## Unidad C — Interfaz de preparación

La plantilla `tools/templates/recipe-assistant.html` y los módulos CSS y JavaScript de assets ofrecen ingredientes en orden y por grupo, checklist reversible, mise en place explícita, rendimiento y tiempos declarados, evidencia y sus declaraciones, navegación de pasos, progreso, temporizador manual y reinicio confirmado. El cuerpo original completo se muestra como texto con un acceso directo desde la cabecera; las advertencias no dependen del paso activo. Se conserva la formulación sin interpretar Markdown como HTML. La vista incluye enlaces internos a técnicas y ficha, avisos de incertidumbre, foco visible y adaptación móvil.

El acceso previsto es recipe-assistant.html?id=...&commit=...&index=..., con ID literal y procedencia del catálogo de Explorer. Se exige un único valor de cada parámetro; se contrasta el manifiesto con la procedencia recibida, se verifica pertenencia del ID, nombre de archivo SHA-256, huella de bytes de registro y coincidencia de esquema, identidad y fuente. El navegador requiere contexto seguro (HTTPS o localhost) para Web Crypto; no se descarga el catálogo completo de Explorer. No es una autenticación criptográfica del sitio, sino una comprobación de consistencia. Se comprueban rutas relativas, estructura y localizadores antes de habilitar la vista. La unidad D incorporará el enlace desde Explorer y la publicación del manifiesto/plantilla; por tanto, no se exponen enlaces nuevos en la aplicación publicada durante C.

El temporizador se actualiza desde el reloj de sesión, no del número de refrescos, y anuncia cambios de estado mediante una región de estado. No promete avisos en suspensión. La sesión se pierde al recargar, salir o cambiar de receta; no hay almacenamiento. La comprobación de sintaxis se integra en Knowledge audit. Los recorridos reales, la correspondencia de enlaces y la validación de accesibilidad dirigida quedan pendientes de D.

## Unidad D — Integración con el portal

La preparación ordinaria de site_docs genera Explorer y Recipe Assistant a partir de los mismos bytes del índice. Publica la plantilla recipe-assistant.html, el manifiesto y un JSON por receta bajo recipe_assistant/. Cada tarjeta del explorador mantiene el enlace al documento y ofrece «Preparar receta», con ID literal, commit y huella del índice. Se conserva el flujo de despliegue vigente; no se publica el índice completo.

El verificador check_recipe_assistant_site.py contrasta inventario, procedencia, huellas, campos compartidos, ingredientes y destinos HTML de recetas y técnicas. El workflow de sitio comprueba dos generaciones idénticas, conserva la regresión del explorador y agrega recorridos Chromium del asistente bajo el subdirectorio del portal. Se cubren el curry amarillo, pastel de manzana, talo y berenjenas Sichuán; checklist por teclado, navegación y foco, temporizador con pausa y reanudación, reinicio, recarga, ficha original, retorno, dos tamaños de pantalla, identificador desconocido, procedencia incorrecta y datos alterados. Los resultados quedan pendientes de CI; no se presume accesibilidad exhaustiva ni publicación remota.

### Uso

Abrir el explorador desde la portada, buscar una receta y seleccionar «Preparar receta». Consultar primero la ficha completa y el contexto original. Marcar ingredientes y pasos conforme se avanza, sin que el sistema deduzca disponibilidad ni cocción. Introducir manualmente minutos y segundos para iniciar un temporizador; el aviso no certifica que el alimento esté listo y puede retrasarse si el navegador suspende la página. Reiniciar con confirmación, o volver al explorador para elegir otra receta. No se guarda el progreso.

Para uso local: instalar requirements.txt, ejecutar python tools/build_site_docs.py, mkdocs build, python tools/check_explorer_site.py y python tools/check_recipe_assistant_site.py; servir con python -m http.server 8000 --directory site y abrir http://localhost:8000/. Se requiere HTTPS o localhost para Web Crypto.

La aceptación de AST-01–AST-15 se registrará con evidencia de ejecución y publicación. La release v1.6.0 y el kit permanecen sin cambios en este incremento.

## Cierre técnico — #281

Las unidades A–D están integradas mediante #278–#281. Merge: `e985d875bb1fe09bbca019edb837f9b165c6a08e`. Los tres workflows de la PR #281 finalizaron correctamente; el snapshot probado fue `683bed8fca9c511ad2f55e4ff5a4418981e4a1fc`, distinto del merge.

- [Knowledge audit](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44614197049/job/135878393878): 141 pruebas Python, nueve pruebas Node superadas, 62 contrastes del explorador, cero advertencias semánticas y huérfanos, doble generación de 590 recetas.
- [Culinary Explorer site](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44614197032/job/135878393545): dos generaciones idénticas, 590 recetas, 591 archivos del asistente, 51 destinos de técnicas, regresión del explorador y recorridos Chromium satisfactorios. Huella del índice del snapshot: `673b3f4ee1d90c9e4712d8b382b9e0bfce187d94f889e9b8d8600e1a5d57d4de`.
- Publicación: gh-pages `bf6bc322ec6aa0b297697337a66bda72f9bbfbb3` declara Deployed e985d87. Se comprobaron la plantilla, el manifiesto (590 recetas) y el enlace Preparar receta en esa rama. No se verificó la disponibilidad HTTP pública.

| Criterio | Evidencia y límites |
|---|---|
| AST-01 | Inventario, procedencia, huellas y doble generación del corpus |
| AST-02 | Verificadores y rechazo en Chromium de ID desconocido, commit incoherente y bytes alterados |
| AST-03 | Reconciliación de ingredientes con extractor e inventario compartido; no precisión culinaria independiente |
| AST-04 | Conservación de declaraciones y diagnósticos, sin cálculo |
| AST-05 | Contraste de pasos con extractor y cuerpo completo; navegación dirigida |
| AST-06 | Contexto íntegro, mise en place y aviso de 74 °C presente en muestra de curry; sin garantía de identificación exhaustiva de advertencias |
| AST-07 | Evidencia original contrastada con índice y Explorer; no certificación de fórmula |
| AST-08 | Pruebas puras y recorrido checklist, navegación, marcado y reinicio |
| AST-09 | Reloj controlado, pausa, reanudación y aviso visual en Chromium; no garantía en suspensión |
| AST-10 | Aislamiento en pruebas y reinicio por recarga en navegador |
| AST-11 | Acceso y retorno, ficha original, 51 destinos de técnicas comprobados en build |
| AST-12 | Teclado, foco y dos tamaños de ventana en recorridos; no auditoría exhaustiva |
| AST-13 | Validación de carga, estado de error y texto seguro; ausencia de pasos cubierta en núcleo, sin recorrido DOM específico |
| AST-14 | 141 pruebas Python, nueve Node, 62 contrastes y cuatro recetas de referencia en Chromium |
| AST-15 | Build reproducible, destinos comprobados y despliegue registrado en gh-pages; uso documentado, comprobación pública pendiente |

Estado: implementación completa y validación técnica dirigida superada; aceptación pública pendiente de comprobar el recorrido en el sitio servido. No se modifica v1.6.0 ni se acredita precisión culinaria, seguridad alimentaria o accesibilidad universal. La siguiente capacidad candidata es Culinary Pantry, sin inferir compatibilidad.
