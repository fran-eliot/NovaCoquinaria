---
id: DOC-ACEPTACION-PUBLICA-CULINARIA-2026
titulo: Protocolo de aceptación pública de las aplicaciones culinarias
tipo: gestion
version: 0.1.2
estado: pendiente-de-ejecucion-manual
ultima_revision: 2026-11-21
---

# Protocolo de aceptación pública — Culinary Workflows Consolidation

## Objetivo y criterios de evidencia

Este protocolo concreta la Unidad D y el criterio CWC-12 de la [revisión estratégica](./REVISION_ESTRATEGICA_APLICACIONES_CULINARIAS.md): comprobar la experiencia real de las cinco aplicaciones en GitHub Pages, separar los resultados del CI y registrar observaciones reproducibles. **El documento es un plan de ejecución, no un acta de resultados.** Ningún caso manual figura como superado por el hecho de existir el protocolo.

La ruta pública conocida es `https://fran-eliot.github.io/NovaCoquinaria/`. Para cada comprobación, anotar URL, fecha, navegador y versión, acción, resultado observado y evidencia. No confundir una plantilla presente en `gh-pages` con carga HTTP real o éxito funcional en la web pública.

### Condiciones previas

1. Verificar que `main` contiene el merge #308 (commit `49cd7925f8de2c280512b1854b0dbd2f4120f0a7`) y que Knowledge integrity, Knowledge audit y Culinary Explorer site han terminado correctamente.
2. Verificar un nuevo mensaje de despliegue de `gh-pages` que corresponda a ese commit **o a otro posterior que lo contenga** y comprobar que los cinco HTML incluyen el enlace `Saltar al contenido principal`. Inicialmente se observó `Deployed 6402600`, anterior a #308; posteriormente `gh-pages` se actualizó a `63ea9fc73467b1503d62beeeca65508340fd0980` (`Deployed 49cd792`). Los cinco HTML incorporan el enlace de salto en la rama publicada; comprobar el funcionamiento real en la URL pública sigue siendo un control separado.
3. Usar **perfil temporal o ventana de prueba aislada** sin datos habituales de Pantry, Shopping y Planner. Las tres aplicaciones comparten el origen y guardan datos en `localStorage`; borrar los datos del sitio en un perfil normal podría destruir información real.
4. No importar las copias personales en esta prueba; emplear exclusivamente nombres y cantidades de ejemplo. Si la prueba se interrumpe, conservar el perfil de prueba mientras se investiga y eliminarlo solo cuando el usuario haya revisado sus resultados.
5. No ejecutar compras reales, no asumir que una receta es segura para el consumo ni interpretar productos declarados como físicamente disponibles.

## Inventario de páginas y comprobaciones

| ID | Aplicación | Ruta pública | Contrato a comprobar |
|---|---|---|---|
| PUB-01 | Culinary Explorer | [culinary-explorer.html](https://fran-eliot.github.io/NovaCoquinaria/culinary-explorer.html) | Carga del catálogo, búsqueda, resultados, paginación, receta seleccionada |
| PUB-02 | Recipe Assistant | [recipe-assistant.html?id=REC-0017](https://fran-eliot.github.io/NovaCoquinaria/recipe-assistant.html?id=REC-0017) | Título, ingredientes, pasos y selección manual para compras |
| PUB-03 | Culinary Pantry | [culinary-pantry.html](https://fran-eliot.github.io/NovaCoquinaria/culinary-pantry.html) | Alta y consulta local de lote declarado; copia JSON |
| PUB-04 | Culinary Shopping | [culinary-shopping.html](https://fran-eliot.github.io/NovaCoquinaria/culinary-shopping.html) | Listas, revisión, compra declarada, transferencia confirmada |
| PUB-05 | Culinary Planner | [culinary-planner.html](https://fran-eliot.github.io/NovaCoquinaria/culinary-planner.html) | Semana, entrada manual, receta seleccionada, copias JSON |

Los enlaces son destinos previstos, no pruebas de que el navegador haya cargado cada uno.

## Recorrido manual integrado recomendado — PUB-06

Realizar las operaciones dentro del **mismo perfil de prueba**, sin abrir nuevas ventanas privadas independientes que pierdan el `sessionStorage`.

1. **Explorer:** cargar el catálogo, localizar una receta identificable y seleccionar `Planificar receta`. Comprobar que se abre Planner con nombre y referencia, sin que se haya creado aún una entrada.
2. **Planner:** elegir una fecha y momento, confirmar la incorporación y verificar que aparece la comida del día. Abrir su enlace `Abrir asistente`. Comprobar que no se crean listas ni lotes por esta acción.
3. **Recipe Assistant:** abrir `Seleccionar ingredientes para comprar`, marcar solo una ocurrencia y pulsar `Revisar en mis compras`. Comprobar que se muestra la revisión y que ninguna cantidad de compra ha sido calculada o aceptada automáticamente.
4. **Shopping:** crear una lista de prueba si no existe, revisar nombre y, si procede, introducir manualmente cantidad/unidad; confirmar el artículo. Marcarlo como comprado y comprobar que Pantry **sigue sin recibir un lote**. Iniciar `Incorporar a despensa`, cancelar y comprobar ausencia de nueva entrada. Repetir el flujo, indicar ubicación (obligatoria), revisar el resto de campos y confirmar expresamente.
5. **Pantry:** abrir la despensa y comprobar el lote individual declarado. Volver a Shopping y verificar que el historial de transferencia queda protegido. Recargar las páginas y observar que persisten los documentos locales y que Planner no se ha modificado por la compra.
6. **Copia de seguridad:** exportar una copia JSON desde cada aplicación que disponga de datos personales de prueba. Comprobar que la descarga existe y que la previsualización de importación muestra el recuento correcto. **Cancelar la importación**; la restauración efectiva de una copia de datos propios no es necesaria para la aceptación básica.
7. **Teclado y móvil:** sin usar ratón para la primera acción de cada página, pulsar Tab hasta `Saltar al contenido principal`, activarlo con Enter y comprobar que el foco llega a la región principal. Revisar en móvil estrecho si aparece desplazamiento horizontal involuntario. Registrar navegador, dispositivo o ancho comprobado, y cualquier barrera de interacción.

### Comprobaciones negativas (PUB-07)

- Eliminar o editar una entrada histórica vinculada a una receta no debe crear enlaces a referencias no verificadas.
- Una transferencia con destino ausente o divergente debe detenerse para revisión; **nunca** debe repetir automáticamente el alta. No forzar este escenario en el perfil habitual: está cubierto por pruebas automatizadas de Unidad B y solo se reproducirá manualmente en un perfil descartable si hay razón y pasos controlados.
- No probar pérdida de datos, fallos físicos, almacenamiento lleno ni restauraciones cruzadas en el perfil personal. Los escenarios destructivos pertenecen a pruebas aisladas.

## Registro de evidencia a completar por el propietario

| Caso | Estado inicial | Resultado manual | Evidencia o incidencia |
|---|---|---|---|
| PUB-01 Explorer | No ejecutado | Pendiente | — |
| PUB-02 Recipe Assistant | No ejecutado | Pendiente | — |
| PUB-03 Pantry | No ejecutado | Pendiente | — |
| PUB-04 Shopping | No ejecutado | Pendiente | — |
| PUB-05 Planner | No ejecutado | Pendiente | — |
| PUB-06 Recorrido conectado | No ejecutado | Pendiente | — |
| PUB-07 Límites negativos | No ejecutado; casos destructivos cubiertos solo por CI | Pendiente de decisión manual | — |
| CWC-12 Aceptación pública | **No acreditada** | Pendiente | — |

Para cada caso ejecutado, registrar como mínimo: `fecha`, `URL`, `commit main`, `commit de despliegue`, `navegador y sistema`, `acción y datos de prueba`, `resultado esperado`, `resultado observado`, `captura o referencia de incidencia` y `decisión de aceptación` (`aceptado` / `bloqueado` / `no ejecutado`). Evitar incluir datos personales en capturas compartidas.

## Matriz de estado del cierre técnico

| Evidencia | Estado comprobado en este corte | Límite |
|---|---|---|
| Unidad A — recorrido integrado | Integrada en #306; CI success | Chromium local, escenario controlado |
| Unidad B — matriz de fallos | Integrada en #307; CI success | Storage simulado, sin sincronización ni atomicidad |
| Unidad C — accesibilidad dirigida | Integrada en #308; CI success (15 casos) | No es auditoría WCAG ni prueba manual |
| GitHub Pages | `Deployed 49cd792` observado y cinco HTML con enlace de salto comprobados en la rama | Verificar uso público real |
| Pruebas públicas del propietario | No acreditadas | No marcar como superadas sin ejecución |
| Nueva release | No autorizada | Sigue v1.6.0 |

## Regla de cierre de la Unidad D

Esta unidad entrega **el protocolo, la matriz de evidencias vacía y la reconciliación documental**. No se declarará completada la aceptación pública hasta disponer de la comprobación manual del propietario, resolver incidencias bloqueantes y registrar su decisión. El cierre **documental** puede validarse en PR separada del cierre **operativo**.

No se añade backend, sincronización, inferencia de faltantes, automatización de compras, nuevas recetas, sprint, milestone ni release. Se mantienen los principios y el reparto de responsabilidades entre el repositorio y el propietario.

## Comprobación HTTP pública complementaria — sonda de solo lectura

Se incorpora `tools/check_culinary_public_http.py` y el workflow manual `Culinary Public HTTP Smoke`. Puede ejecutarse desde **GitHub → Actions → Culinary Public HTTP Smoke → Run workflow**, una vez fusionada la PR que lo incluya. El workflow no está programado, no modifica ningún documento ni accede al almacenamiento de los navegadores. Genera el artefacto `culinary-public-http-evidence` con la URL base, fecha UTC, resultados por página, recursos obtenidos y concordancia entre catálogo y manifiesto.

El contraste utiliza solicitudes GET de red a las cinco páginas, a sus scripts y CSS de entrada, al JSON del catálogo y al manifiesto de Recipe Assistant. Exige respuesta HTTP 200, enlace de salto visible en HTML, destino de navegación, módulos de entrada versionados, recursos presentes, catálogo no vacío y concordancia de recuento, `source_commit` e `index_sha256` con el manifiesto. Se rechazan recursos que cambien de origen o utilicen rutas relativas inseguras. Las pruebas de contrato del propio comprobador se ejecutan **sin acceso a red** durante Knowledge audit.

Esta comprobación es evidencia pública HTTP, **no** aceptación de los casos PUB-01–PUB-07: no ejecuta JavaScript, no comprueba interacciones, no usa el `localStorage` del usuario, no prueba un dispositivo real y no sustituye las decisiones del propietario. Hasta observar una ejecución real del workflow y su artefacto no se debe marcar como satisfecha la nueva comprobación. Un resultado HTTP positivo, si se obtiene, será un escalón intermedio entre publicación observada en `gh-pages` y aceptación manual del portal.

## Evidencia HTTP observada — 2026-11-21

El workflow `Culinary Public HTTP Smoke` se ejecutó correctamente en la PR #311, run `44946142425`, job `136973764535`, sobre la publicación `https://fran-eliot.github.io/NovaCoquinaria/`. El registro de ejecución indica `passed: true` y `checked_at_utc: 2026-11-21T20:25:04+00:00`.

| Control de red | Resultado real |
|---|---|
| Explorer, Assistant, Pantry, Shopping, Planner | 5/5 con HTTP 200 |
| Recursos de entrada JavaScript/CSS | 10 comprobados con HTTP 200 |
| Enlaces de salto y módulos de entrada versionados | Presentes en las cinco páginas |
| Catálogo público | 590 recetas |
| Concordancia catálogo/manifiesto de Recipe Assistant | Correcta |
| Commit documental del catálogo | `20214dd19a732c91d52ab469380d2b97146a6707` |

La verificación empleó GET de solo lectura. No ejecutó JavaScript, no manipuló datos personales, no comprobó `localStorage` y **no convierte PUB-01–PUB-07 o CWC-12 en aceptados**. El informe está disponible como artefacto de la ejecución de GitHub Actions y el resultado también consta en sus logs. Para afirmar aceptación operativa sigue siendo necesaria la comprobación del propietario con un perfil temporal aislado.

## Ampliación de la sonda pública: integridad de ficha individual

La comprobación HTTP de solo lectura contrasta también una ficha concreta de Recipe Assistant (`REC-0017`) con el manifiesto y el catálogo públicos. Descarga el JSON de la ficha, verifica el nombre de archivo derivado del identificador, compara la huella SHA-256 con la del manifiesto y comprueba identificador, título, procedencia, referencia e índice, así como la existencia de ingredientes y pasos. El resultado queda identificado en el informe mediante `sample_recipe_id` y `sample_recipe_integrity`.

Se trata de una muestra dirigida, no de la verificación íntegra de las 590 recetas ni de una prueba de navegador. La comprobación depende de ejecutar el workflow `Culinary Public HTTP Smoke` contra la publicación actual. Los casos PUB-01–PUB-07 permanecen pendientes de aceptación manual.

## Comprobación del portal público en Chromium aislado

El workflow manual `Culinary Public Browser Smoke` utiliza Chromium en un runner de GitHub Actions y carga las cinco aplicaciones desde `https://fran-eliot.github.io/NovaCoquinaria/`. Cada página se abre en un contexto desechable independiente, sin acceso al perfil personal del usuario. Comprueba respuesta HTTP de la página, inicialización de la interfaz JavaScript, una búsqueda no persistente en Explorer, contenido y pasos reconocidos en Recipe Assistant, disponibilidad de los controles iniciales de Pantry, Shopping y Planner, ausencia de errores JavaScript de página y desplazamiento horizontal no previsto a 390 px.

El workflow se activa manualmente desde Actions o al modificar los archivos de esta comprobación en una PR; produce el artefacto `culinary-public-browser-evidence`. No envía formularios de creación, edición, compra, transferencia o importación; tampoco recupera ni inspecciona el almacenamiento del navegador personal. Las comprobaciones automatizadas tienen un alcance dirigido y **no acreditan la aceptación manual PUB-01–PUB-07 ni CWC-12**. La ejecución y el resultado real del workflow deben verificarse antes de registrar evidencia positiva.

## Navegación pública Explorer → Recipe Assistant

La sonda Chromium pública también verifica la transición entre las dos aplicaciones: realiza una búsqueda por el título de `REC-0017` obtenido del catálogo público, selecciona `Preparar receta`, comprueba que la URL corresponde al identificador esperado y verifica título, ingredientes y pasos de la receta abierta. El informe registra `explorer_to_assistant` y `linked_recipe_id` para distinguir este recorrido del arranque aislado de cada página. Se conservan los controles sobre errores JavaScript, origen público oficial y contexto de navegador desechable.

La prueba es una muestra dirigida de navegación, no una aceptación manual de los recorridos PUB-01–PUB-07 ni una verificación general de todos los enlaces o recetas. No crea ni modifica registros personales.
