---
id: DOC-ALCANCE-PLANNER-2026
titulo: Alcance de entrega de Culinary Planner
tipo: gestion
version: 0.1.3
estado: borrador
ultima_revision: 2026-11-21
---

# Culinary Planner — alcance de entrega

## Propósito y estado inicial

Planificar comidas de manera explícita para fechas concretas, reutilizando recetas documentadas del SGCC y permitiendo platos escritos libremente. El plan es una declaración personal editable, **no** una evaluación de cocinabilidad, suficiencia, seguridad, disponibilidad, nutrientes ni conveniencia gastronómica.

Base de decisión: Kit de continuidad 2.6.0 y Roadmap 2.15 tras #298. Culinary Explorer, Recipe Assistant, Pantry y Shopping 0.1.0 están desplegados; su uso público de extremo a extremo, especialmente la transferencia Shopping → Pantry, no está acreditado mediante prueba manual del propietario. La evidencia técnica dirigida no sustituye ese contraste.

Esta propuesta define la siguiente capacidad candidata, no la da por aprobada o implementada. No compromete una nueva release ni backend.

## Unidad de planificación

- **Fecha civil** ISO `AAAA-MM-DD`, válida en calendario gregoriano. Evitar convertir una fecha civil a UTC para no desplazar días por zona horaria.
- **Momento de comida** declarado entre desayuno, comida, cena y otro. No deducir horarios, objetivos nutricionales ni restricciones dietéticas. No es un horario de avisos.
- **Entrada independiente** con ID opaco estable, fecha, momento, título declarado y tipo de origen:
  - `recipe`: referencia al ID y título de una receta reconocida en el catálogo actual al seleccionarla; conservar procedencia documental (commit de catálogo y ruta de ficha) como referencia histórica.
  - `free_text`: plato, idea o preparación libre, sin atribución al SGCC ni enlace inventado.
- **Notas** opcionales del usuario. No almacenar cantidades calculadas, promesas de rendimiento ni evaluaciones nutricionales.
- Permitir **varias entradas** en un mismo día y momento (por ejemplo, entrante y principal). Preservar orden declarado sin agrupar ni sustituir entradas automáticamente.

## Recorridos incluidos

1. Abrir un calendario semanal con navegación a semanas anteriores y posteriores, y vista por día. La semana visible comienza en lunes; los cambios de día y semana no alteran las entradas. Añadir entradas desde fechas concretas, editar fecha, momento, título y notas, mover mediante una modificación explícita y eliminar con confirmación.
2. Añadir una receta desde Explorer o Recipe Assistant mediante una selección expresa. La entrada muestra la receta y un enlace a la ficha o asistente existente, sin copiar su texto como fuente canónica. Si cambia o desaparece la receta, no sustituir silenciosamente la referencia ni adjudicar un ID diferente; comunicar el estado y conservar el plan declarado.
3. Añadir platos libres cuando no exista una receta apropiada. La aplicación no debe convertir nombres de platos en IDs de receta por parecido textual.
4. Buscar o filtrar entradas del plan por fecha, momento y título declarado; indicar visualmente planes vacíos y múltiples entradas. Las búsquedas dentro del plan no implican búsqueda semántica en el catálogo.
5. Guardar el plan en el navegador con una **clave local exclusiva** y un esquema versionado. Permitir exportación JSON e importación validada con recuento, previsualización y confirmación de sustitución. La cancelación o datos incompatibles no escriben. Detectar conflictos observados entre pestañas, bloqueo de almacenamiento y agotamiento de cuota; no corregir ni reemplazar silenciosamente datos inválidos.
6. Desde una entrada vinculada a receta, **abrir el asistente** para consultar ingredientes y procedimientos y, cuando exista soporte, utilizar la selección manual ya disponible en Assistant → Shopping. No se generará una lista de compra automáticamente desde el plan ni se transferirán cantidades, notas o preferencias a Shopping en 0.1.0.
7. Ofrecer enlaces contextuales a Explorer, Assistant, Shopping y Pantry, diferenciando las funcionalidades de cada aplicación.

## Contrato de datos propuesto

`schema_version: "0.1.0"`; `entries: []`.

Cada entrada contiene como mínimo: `id`, `date`, `meal`, `title`, `notes`, `source`. `source` es una unión discriminada:
- `{type:"free_text"}`
- `{type:"recipe",recipe_id,source_commit,source_path}` con valores extraídos de un registro validado del catálogo en el momento de incorporación.

La definición final de tamaños máximos, orden, serialización, identificadores y límites de listas o entradas se fijará en la Unidad A. No introducir campos opcionales sin contrato. No asumir que dos recetas con el mismo título son idénticas. Un ID almacenado es una referencia histórica y debe verificarse contra el catálogo antes de generar enlaces al asistente.

## Persistencia, seguridad y privacidad

El plan es personal y permanece en el origen y perfil del navegador. No se sincroniza entre dispositivos, no se envía al servidor, no se inserta en URLs y no se añade al repositorio. Las exportaciones contienen información personal y requieren custodia del usuario. Mantener copia válida tras errores. Utilizar `textContent` o mecanismos seguros para mostrar texto libre. El estado no se integra en la base Markdown ni modifica esquemas de Pantry o Shopping.

El planificador no convierte datos de recetas en decisiones de alimentación segura. Si una receta contiene tiempos, cantidades o raciones incompletas, el planificador no rellenará los huecos con suposiciones.

## Criterios de aceptación 0.1.0

| ID | Evidencia requerida |
|---|---|
| PLN-01 | Esquema 0.1.0 y límites validados, IDs únicos, fechas civiles correctas |
| PLN-02 | Varias entradas por fecha/momento, orden preservado y operaciones inmutables |
| PLN-03 | Semanas con lunes inicial, navegación y transición de año sin desfase horario |
| PLN-04 | Alta, edición, cambio de fecha y eliminación expresos, con confirmación |
| PLN-05 | Platos libres diferenciados de recetas documentadas |
| PLN-06 | Incorporación explícita de receta desde catálogo y procedencia verificable al seleccionar |
| PLN-07 | Manejo conservador de referencias obsoletas o ausentes, sin sustitución automática |
| PLN-08 | Filtros de fecha, momento y título, estados vacíos y entradas múltiples |
| PLN-09 | Persistencia local separada, recarga y manejo de conflictos, cuota y datos ilegibles |
| PLN-10 | Copias JSON, previsualización, importación confirmada y cancelación sin escritura |
| PLN-11 | Acceso seguro al asistente y navegación entre aplicaciones; sin inventar rutas |
| PLN-12 | No modificar Shopping/Pantry ni generar listas o faltantes automáticamente |
| PLN-13 | Texto libre no ejecutable, datos personales fuera de URLs/red y manejo de errores |
| PLN-14 | Pruebas Node del modelo y persistencia y recorridos Chromium dirigidos |
| PLN-15 | Build reproducible, recursos versionados, regresión de las cuatro aplicaciones y verificación de publicación |

La comprobación pública del usuario se registrará como evidencia separada, sin confundirla con el CI o con el commit desplegado.

## Plan de implementación

| Unidad | Alcance | Dependencias y puerta de salida |
|---|---|---|
| A — Planner Model | Contrato, operaciones, filtro y cálculo civil de semanas | Pruebas puras; ninguna escritura |
| B — Planner Persistence | Almacenamiento exclusivo, copias, errores y conflictos | Pruebas con almacenamiento simulado |
| C — Planner UI | Semana/día, formularios, edición y estados vacíos | Sin publicación ni sincronización implícita |
| D — Planner Integration | Selección explícita desde aplicaciones, enlaces seguros, build y Chromium | Sin modificar contratos de Shopping/Pantry; verificación de despliegue |

Las ramas y PR serán temáticas, partiendo cada una del último `main` aprobado; el propietario fusiona y elimina las ramas remotas. Mantener criterios de aceptación y limitaciones ligados a evidencia concreta.

## Exclusiones y decisiones diferidas

- Recomendación o generación automática de menús; nutrición, calorías, macros, alergias y dietas; optimización de recetas; restricciones de presupuesto y comparación de precios.
- Deducción de inventario disponible o faltante; suficiencia por cantidades; sustituciones de ingredientes; escalado de recetas y cálculo de raciones.
- Generación automática o modificación de Shopping/Pantry desde el plan; consumos, reservas y decrementos del inventario.
- Recurrencias, notificaciones, sincronización, compartir calendarios, backend, autenticación, RAG/LLM/agentes y nueva release.
- Importación automática de calendarios externos y asignación implícita de una receta por similitud textual.

## Referencias

- [Kit de continuidad 2.6.0](./NOVACOQUINARIA_KIT_CONTINUITY.md)
- [Roadmap](./ROADMAP.md)
- [Culinary Explorer](./ALCANCE_CULINARY_EXPLORER.md)
- [Recipe Assistant](./ALCANCE_CULINARY_RECIPE_ASSISTANT.md)
- [Culinary Pantry](./ALCANCE_CULINARY_PANTRY.md)
- [Culinary Shopping](./ALCANCE_CULINARY_SHOPPING.md)
- [Deuda semántica de requisitos culinarios](./DEUDA_REQUISITOS_CULINARIOS.md)

## Unidad A — Contrato y modelo de planificación

`assets/culinary-planner-model.mjs` implementa un modelo puro, sin almacenamiento, DOM o red. La estructura `{schema_version:"0.1.0",entries:[]}` admite hasta 2.000 entradas, cada una con ID ASCII opaco y único de hasta 80 caracteres, fecha civil ISO de año 0001–9999, comida declarada (`breakfast`, `lunch`, `dinner`, `other`), título de hasta 160 caracteres, notas opcionales de hasta 1.000 caracteres y origen estricto. Las operaciones de alta, edición y eliminación conservan el orden de inserción y devuelven copias validadas.

El origen `free_text` contiene únicamente su discriminante. Un origen `recipe` conserva `recipe_id`, `source_commit` (SHA de 40 caracteres) y `source_path` (ruta relativa Markdown acotada). Estos campos son referencias históricas, no enlaces autorizados: el consumidor deberá comprobar el registro contra el catálogo actual antes de habilitar navegación. El título es siempre una declaración del usuario; no se normaliza contra otras recetas. La edición conserva el tipo y la procedencia, y requiere crear otra entrada para cambiar la identidad documental.

El cálculo de semanas emplea días ordinales gregorianos enteros, sin conversiones a UTC ni objeto `Date`; comienza en lunes y rechaza desplazamientos fuera del intervalo representable. El último día del año 9999 es válido como fecha, pero una vista semanal que sobrepase el límite del calendario no se genera. Los filtros por fecha, momento y título son acumulables; el texto se compara con normalización Unicode NFC y sin distinguir mayúsculas, sin interpretación semántica. La composición de referencias visibles, el catálogo y las búsquedas de recetas quedan fuera de esta unidad.

Se incorporan ocho pruebas Node sobre validación, años bisiestos, transiciones anuales, orden, inmovilidad de origen, duplicados, filtros, referencias no comprobadas y ausencia de URLs personales. La cobertura se conecta con Knowledge audit. Persistencia, interfaz e integración continúan pendientes; no se modifica la release v1.6.0.

## Unidad B — Persistencia local del Planner

El módulo `assets/culinary-planner-persistence.mjs` proporciona un adaptador sin DOM ni red, con `Storage` inyectable y clave `novacoquinaria.culinary-planner`, independiente de Shopping y Pantry. Conserva el esquema de `culinary-planner-model.mjs` 0.1.0 y un máximo de 12 millones de unidades UTF-16 para el JSON; el espacio real depende del navegador. La primera carga sin clave devuelve un plan vacío sin escribir. Una carga inválida o de versión no admitida bloquea las modificaciones sin reemplazar el documento existente.

Las escrituras comparan el contenido actual con la línea base cargada y rechazan los cambios externos observados. Se distinguen falta de almacenamiento, errores de lectura, conflictos, falta de cuota y errores de escritura, sin suponer transacciones atómicas entre pestañas. El último documento válido se conserva en memoria incluso cuando una carga posterior falla; no constituye una segunda copia durable.

La exportación produce JSON validado y conserva notas y referencias históricas. La previsualización de importación muestra el recuento de entradas y vincula la confirmación a esa previsualización concreta del adaptador. Cancelar no escribe. La sustitución, solo tras confirmación explícita y contraste con el almacenamiento vigente, permite reemplazar el plan completo; no modifica Pantry ni Shopping, ni agrega entradas automáticamente. No se añade sincronización, recuperación de borrados ni almacenamiento remoto.

Once pruebas Node cubren aislamiento de claves, recarga, versiones, fallos de acceso, lectura y escritura, cuota, conflictos entre pestañas, previsualización, cancelación, importación y copias de referencias documentales. Knowledge audit ejecuta las pruebas. Quedan pendientes la interfaz, recorridos Chromium y publicación; no se modifica la release v1.6.0.

## Unidad C — Interfaz semanal y edición manual

La plantilla `tools/templates/culinary-planner.html` y los recursos `assets/culinary-planner-ui.mjs` y `assets/culinary-planner.css` introducen una aplicación estática adaptable al móvil con vista semanal desde lunes, selección de día, navegación de semanas y días, y tarjetas por momento de comida. Cada fecha admite varias entradas y conserva su orden declarado. La selección de fecha y los desplazamientos usan el modelo civil sin conversión de día a UTC. La fecha del sistema se lee exclusivamente para determinar el día actual en el navegador, no para interpretar las entradas almacenadas.

Los formularios permiten añadir platos libres, modificar fecha, momento, título y notas, o eliminar entradas mediante confirmación. Si existe una referencia a receta en una copia importada, su procedencia permanece inalterada durante la edición y se etiqueta como pendiente de comprobación; no se construyen enlaces a recetas desde IDs sin contrastar con el catálogo. La selección desde Explorer o Recipe Assistant se reserva para la unidad D. Los filtros por momento y título actúan sobre el día seleccionado y no cambian el plan.

La UI emplea el adaptador de persistencia de la unidad B: guardado y recarga locales, exportación JSON, importación con recuento y confirmación, manejo visible de conflictos y de errores, bloqueo de cambios tras modificaciones externas observadas. Los textos personales se insertan mediante `textContent`; no se escriben datos en Shopping ni Pantry. Los controles utilizan etiquetas nativas, regiones de estado y foco visible. Aún no se acredita una revisión integral de accesibilidad.

La plantilla y los recursos se incorporan como fuentes, pero **no al build público** en esta unidad. Knowledge audit comprobará la sintaxis del módulo; las pruebas de recorrido Chromium y publicación corresponden a la unidad D. El estado de Planner 0.1.0 permanece en implementación y la release v1.6.0 no cambia.
