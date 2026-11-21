---
id: DOC-ALCANCE-SHOPPING-2026
titulo: Alcance de entrega de Culinary Shopping
tipo: gestion
version: 0.1.7
estado: borrador
ultima_revision: 2026-11-21
---

# Culinary Shopping — alcance de entrega

## Propósito

Organizar compras domésticas mediante listas personales declaradas, reutilizando el catálogo y el inventario sin confundir menciones, necesidades de compra y existencias. Base: main 08d8c91bf2048f82ddfec96f72617216f02f5829, kit 2.5.0. Pantry está desplegado con pruebas dirigidas satisfactorias; su comprobación pública sigue pendiente. Este alcance no acredita dicha comprobación ni compromete una release.

## Recorridos

- Crear, renombrar y eliminar listas independientes; confirmar eliminación. Añadir, editar, eliminar y marcar o desmarcar artículos comprados. Mantener artículos comprados visibles o filtrables. No fusionar automáticamente entradas, ni interpretar una marca como existencia.
- Artículo: ID opaco único, nombre obligatorio, cantidad y unidad opcionales declaradas juntas, categoría y notas opcionales, estado comprado booleano, procedencia opcional de receta. Reutilizar reglas de cantidades literales de Pantry; no sumar ni convertir unidades. Lista: ID, nombre y artículos en orden de inserción. Fijar límites explícitos en el modelo.
- Desde Recipe Assistant, seleccionar ocurrencias concretas y abrir Shopping en la misma pestaña. Mostrar receta, texto original y cantidad declarada como referencia; el usuario elige lista y confirma los artículos a registrar, revisando nombre, cantidad y unidad. Los rangos, alternativas y cantidades no reconocidas no se transforman automáticamente en cantidades exactas. Conservar ID de receta, posición y localizador como procedencia histórica, junto con texto original y commit. No importar toda la receta sin selección ni identificar faltantes.
- Desde una lista, seleccionar artículos comprados aún no transferidos y preparar entradas de Pantry. Revisar nombre, cantidad, unidad, categoría y ubicación individualmente; permitir completar fechas y notas. Crear lotes nuevos únicamente mediante confirmación explícita. No alterar cantidades existentes ni deducir ubicaciones o caducidades. Registrar estado de transferencia y evitar reenvíos automáticos. La marca de compra y la transferencia son estados distintos.
- La persistencia de Shopping y Pantry utiliza claves separadas. No existe transacción atómica entre ellas: la unidad de integración deberá definir recuperación verificable ante éxito parcial y evitar duplicados al reintentar mediante IDs estables y comprobación de la intención de transferencia. Ante incertidumbre o conflicto, detener y pedir revisión; nunca confirmar transferencia sin escritura acreditada en Pantry. No modificar ni eliminar entradas de Pantry como compensación automática.

## Persistencia e integración

Aplicación estática del mismo portal. Almacenamiento local versionado, exportación JSON e importación validada con recuento y confirmación de sustitución. Mantener última copia válida, detectar cambios externos y errores, sin reparación destructiva automática. Reutilizar los principios de Pantry sin compartir su clave ni modificar su esquema. El intercambio temporal de selecciones entre aplicaciones será local, con validación y consumo explícito; datos personales fuera de URL, solicitudes y repositorio. No hay sincronización, cifrado, aislamiento frente a otros scripts del origen ni garantía de recuperación. La restauración de una copia antigua puede requerir reconciliación manual con Pantry; no repetir transferencias por defecto.

## Criterios de aceptación

| ID | Criterio |
|---|---|
| SHP-01 | Esquema versionado, límites, IDs y campos validados |
| SHP-02 | Varias listas independientes y operaciones explícitas |
| SHP-03 | Artículos, cantidades literales, unidades, categorías y notas |
| SHP-04 | Marcado reversible y filtros; sin modificación implícita de Pantry |
| SHP-05 | Persistencia local separada y recarga |
| SHP-06 | Exportación e importación validada, confirmación y cancelación |
| SHP-07 | Fallos de almacenamiento y cambios externos sin pérdida silenciosa |
| SHP-08 | Selección explícita de ocurrencias desde Assistant |
| SHP-09 | Revisión de artículos y procedencia, sin conversiones ni faltantes inferidos |
| SHP-10 | Selección de comprados y revisión explícita para Pantry |
| SHP-11 | Transferencia con IDs estables, recuperación de éxito parcial y rechazo de duplicados/conflictos |
| SHP-12 | Interfaz adaptable, teclado, estados vacíos y confirmaciones |
| SHP-13 | Datos personales locales y texto no confiable sin HTML activo |
| SHP-14 | Pruebas puras, almacenamiento simulado, fallos de transferencia y recorridos Chromium |
| SHP-15 | Build versionado, regresión, guía, despliegue y comprobación pública acotada |

## Unidades

| Unidad | Entrega |
|---|---|
| A — Shopping Model | Listas, artículos, estados, procedencia y filtros |
| B — Shopping Persistence | Almacenamiento, copias y conflictos |
| C — Shopping UI | Gestión de listas y artículos |
| D — Integration | Selección desde Assistant, revisión hacia Pantry, recuperación de transferencias, publicación y pruebas |

La unidad D debe resolver el protocolo de transferencia antes de activarlo; si no acredita recuperación ante fallo parcial, no se publica ese recorrido. La comprobación pública de Pantry se mantiene pendiente y debe registrarse antes de aceptar el recorrido integrado.

## Exclusiones

Compatibilidad automática, deducción de faltantes, agregación semántica, conversiones, escalado, precios, proveedores, pedidos, consumo automático, planificación, IA, backend, sincronización y nueva release. Markdown sigue siendo fuente canónica; el estado personal no forma parte del conocimiento documental.

## Referencias

- [Culinary Pantry](./ALCANCE_CULINARY_PANTRY.md)
- [Recipe Assistant](./ALCANCE_CULINARY_RECIPE_ASSISTANT.md)
- [Culinary Explorer](./ALCANCE_CULINARY_EXPLORER.md)
- [Roadmap](./ROADMAP.md)
- [Deuda de requisitos](./DEUDA_REQUISITOS_CULINARIOS.md)

## Unidad A — Modelo de listas

El módulo `assets/culinary-shopping-model.mjs` define el esquema 0.1.0: schema_version, lists; cada lista contiene id, name e items. Se admiten hasta 100 listas y 2000 artículos en total. Los IDs son únicos dentro del documento, incluidos los de listas, con un máximo de 80 caracteres para listas y 71 para artículos. El nombre de lista admite hasta 160 caracteres. Las operaciones devuelven copias y mantienen el orden de inserción. No fusionan productos.

Cada artículo contiene id, name, quantity, unit, category, notes, purchased, provenance y transfer. Se reutiliza validateEntry de Pantry para validar los campos compartidos sin modificar su contrato. Las cantidades se mantienen como decimales positivos literales o null; no se convierten ni suman. La procedencia es null o contiene recipe_id, position (desde cero), source_location (start_line/end_line), raw (hasta 8000 caracteres) y source_commit (SHA de 40 caracteres). Es una referencia histórica, no una certificación de correspondencia; su contraste con el catálogo corresponde a integración. Se conserva al editar el artículo.

La compra se marca y desmarca expresamente mientras no haya registro de transferencia. La transferencia es null o contiene state (pending/completed) y entry (copia completa del destino validado por Pantry). El ID de destino es shopping- seguido del ID del artículo. prepareTransfer registra exclusivamente la intención revisada; recordTransferCompleted exige una entrada coincidente campo a campo, pero no acredita por sí mismo una escritura. El coordinador de la unidad D deberá contrastar el almacenamiento y gestionar fallos parciales, colisiones e incertidumbres antes de invocarlo. No existe acceso a almacenamiento en esta unidad.

Para conservar evidencia e impedir reintentos accidentales, los artículos con transferencia pendiente o completada no se pueden editar, desmarcar ni eliminar; tampoco se elimina su lista. Esta restricción de la primera versión limita la limpieza de listas históricas; el archivado o reconciliación destructiva queda fuera del alcance inicial. No se pretende garantizar unicidad histórica después de restaurar copias independientes. La UI deberá comunicar estas restricciones.

Se incorporan diez pruebas Node para operaciones, límites, cantidades, procedencia, filtros, compra reversible y estados de transferencia. Knowledge audit ejecutará estas pruebas. Persistencia, UI, contraste con recetas y coordinación efectiva con Pantry permanecen pendientes. No se modifica la release.

## Unidad B — Persistencia de listas y copias

El adaptador `assets/culinary-shopping-persistence.mjs` conserva la interfaz de persistencia de Pantry con validación del esquema de Shopping 0.1.0 y clave independiente novacoquinaria.culinary-shopping. El acceso a Storage es inyectable; no hay DOM ni red. Una clave ausente permite iniciar un documento vacío sin escritura automática. Se distinguen acceso bloqueado, lectura inválida, versión incompatible, cuota, escritura y conflicto. Se conserva la última copia válida y se impide escribir tras una carga fallida. El límite de JSON de entrada y salida es de 12 millones de unidades UTF-16, sin garantizar capacidad equivalente del navegador.

La escritura contrasta la cadena original con la lectura actual y bloquea ante eventos externos pertinentes; los cambios de la clave de Pantry no invalidan por sí mismos Shopping. No hay atomicidad entre pestañas ni entre aplicaciones. La exportación conserva listas, artículos, procedencia y registros de transferencia. La previsualización de importación presenta recuentos de listas y artículos; cancelar no escribe. La sustitución confirmada vuelve a validar el documento y rechaza copias que omitan o alteren cualquier registro de transferencia vigente en la última copia válida. Esta protección conservadora no equivale a verificar la presencia actual del destino en Pantry. Las copias con transferencias históricas o pendientes requieren revisión antes de cualquier reintento; no se inicia ninguna transferencia al importar. Tras pérdida o borrado independiente de ambos almacenamientos no existe garantía de reconciliación.

Se añaden once pruebas Node con Storage simulado y ejecución en Knowledge audit: separación de claves, recarga, datos inválidos, acceso y escritura fallidos, cuota, conflictos, importación y cancelación, conservación de transferencias, exportación y límite de JSON. Las pruebas en navegador y el coordinador de transferencia siguen pendientes de las unidades C y D. No se modifica Pantry ni la release.

## Unidad C — Interfaz de listas

La plantilla culinary-shopping.html y los recursos culinary-shopping.css y culinary-shopping-ui.mjs conectan el modelo y la persistencia con controles nativos. Se ofrecen creación, selección, renombrado y eliminación confirmada de listas; alta, edición, eliminación confirmada y marcado reversible de artículos; progreso por lista y filtros acumulables por nombre, categoría, compra y transferencia. Las cantidades opcionales conservan su representación literal, con adaptación de coma decimal a punto en el formulario. Los identificadores nuevos se generan mediante Web Crypto. Se mantiene la procedencia de receta como texto histórico consultable, incluso al editar.

Los registros de transferencia pendientes o completados se muestran como protegidos, sin edición, borrado ni desmarcado; sus listas no se pueden eliminar. Una transferencia registrada no acredita existencias actuales. La UI no inicia transferencias ni escribe en Pantry. Los recorridos desde Recipe Assistant y hacia Pantry se incorporarán en la unidad D, sujetos a las condiciones de recuperación y revisión del alcance.

La aplicación emplea localStorage a través del adaptador, muestra errores y bloquea cambios ante conflicto observado. La exportación crea un archivo local JSON con la última copia válida; la importación muestra recuentos de listas y artículos y exige confirmación de sustitución. Los rechazos por historial protegido no modifican el documento. Los textos personales se insertan mediante textContent; los datos no se envían a un servidor. La interfaz comparte el estilo base de Explorer y añade adaptación móvil. La plantilla todavía no se incorpora al build público. Knowledge audit verifica sintaxis y pruebas de núcleo y persistencia; quedan pendientes los recorridos reales de navegador, el protocolo de transferencia y el despliegue.

## Unidad D1 — Integración desde recetas y publicación parcial

El asistente incorpora una selección explícita de ocurrencias independiente del checklist de preparación. Tras confirmar la salida (se pierde el progreso efímero), se transfieren mediante sessionStorage los nombres sugeridos y la procedencia del registro de receta cargado, incluida la línea original, posición y commit. No se transfieren cantidades calculadas. Shopping consume la selección una sola vez y ofrece una revisión editable del nombre y de la cantidad y unidad de compra, inicialmente ausentes. Se puede excluir cualquier ocurrencia y elegir una lista existente o crear una nueva antes de confirmar. El guardado de los artículos seleccionados se realiza como una sola escritura del documento. No se incorpora nada al cancelar. La procedencia se conserva como declaración histórica; el consumidor valida la estructura, no verifica de nuevo el catálogo ni autentica datos de sessionStorage.

El build incorpora Shopping, acceso desde portada y versionado conjunto de módulos y estilos. La publicación parcial habilita listas y el recorrido desde Assistant, pero no la escritura en Pantry. Se añaden pruebas del transporte y recorridos Chromium de listas, copias, selección, revisión y aislamiento de almacenamiento. Resultados pendientes de CI; no se afirma aceptación pública. La unidad D2 resolverá el protocolo de transferencia a Pantry y sus fallos parciales antes de habilitarlo. El alcance sigue abierto, sin nueva release.

## Unidad D2 — Protocolo de transferencia (núcleo)

El coordinador `assets/culinary-shopping-pantry-coordinator.mjs` recibe adaptadores independientes y una fotografía revisada de Shopping. Para una única transferencia confirmada, contrasta el documento vigente, valida el destino con el esquema Pantry, rechaza cualquier ID de destino previamente existente y prepara el nuevo inventario sin escribir. Persiste primero la intención pending en Shopping; comprueba que se conserva y guarda después el lote en Pantry. Lee nuevamente Pantry y exige coincidencia de todos los campos del destino antes de registrar completed en Shopping. No hay compensación destructiva.

La recuperación de una intención pendiente es deliberadamente conservadora: solo permite completar el registro si existe una entrada exactamente igual a la intención. Nunca crea otra entrada en recuperación, aunque el destino esté ausente. La ausencia no permite distinguir un fallo de escritura de un lote posteriormente consumido, eliminado o perdido tras restauración. Una entrada diferente también bloquea la recuperación. Estos casos requieren revisión manual y mantienen el registro protegido; no se habilita aún resolución destructiva ni reintento de alta. Un estado completed acredita el contraste realizado entonces, no existencias actuales.

Los adaptadores conservan la detección de conflictos por lectura previa. No existe transacción atómica entre claves ni garantía frente a escrituras concurrentes, restauraciones independientes o modificaciones entre comprobaciones. El coordinador no adquiere bloqueo global y su uso exige confirmación individual. Las ocho pruebas Node cubren orden de escrituras, cancelación, fallo de intención, fallo de Pantry, fallo de finalización recuperable, colisión, destino modificado/ausente y datos desactualizados o inválidos. La interfaz y la publicación de este recorrido permanecen deshabilitadas hasta completar su revisión, controles de concurrencia y pruebas de navegador. No se modifica la release.

## Unidad D3 — Revisión y transferencia desde la interfaz

Shopping ofrece la incorporación individual de artículos comprados sin transferencia. Un diálogo revisa nombre, cantidad, unidad, categoría, notas, ubicación obligatoria y fecha opcional con su tipo. No se sugiere una ubicación ni una caducidad; el usuario confirma la creación de un lote independiente. El coordinador registra la intención antes de escribir en Pantry. Los artículos pendientes muestran los datos de destino y permiten exclusivamente verificar el lote existente, sin volver a darlo de alta. Tras un error la interfaz relee Shopping y comunica el estado sin confirmar éxito ni repetir la escritura. Los registros protegidos siguen sin admitir edición, desmarcado ni eliminación.

La interfaz emplea Web Locks con nombre novacoquinaria.shopping-pantry-transfer y adquisición exclusiva no bloqueante para serializar transferencias entre pestañas que ejecutan este protocolo. Si no existe la API, se deshabilita el recorrido; si el bloqueo está ocupado, se rechaza la operación. Durante la operación se impiden nuevos cambios en la misma interfaz y se contrasta la fotografía revisada. Las escrituras ordinarias de Pantry y Shopping no adquieren este bloqueo; los adaptadores conservan su contraste optimista. No se acredita atomicidad ni eliminación de toda carrera entre escrituras ordinarias, otras versiones de la aplicación o restauraciones independientes.

Se incorporan enlaces recíprocos entre Shopping y Pantry y se incluye el coordinador en el versionado de recursos. Se amplía el recorrido Chromium con cancelación, revisión de ubicación y fecha, alta y visualización en Pantry, protección del historial, fallo inducido al finalizar y recuperación tras recarga sin duplicar el lote, y fallo inducido al escribir Pantry con destino ausente y rechazo de recreación. Es evidencia dirigida, no una prueba exhaustiva de concurrencia ni accesibilidad. La comprobación real en el portal público de Pantry sigue pendiente, así como la aceptación final de Shopping y los resultados de este incremento. No se modifica la release v1.6.0.

## Cierre técnico — #297

Las unidades A–D se integraron a través de #292–#297, tras el alcance aprobado en #291. El merge final es `765d50784bcceb87303a72ce621090e40893d587`. La comprobación dirigida de CI de la PR #297 se ejecutó sobre el merge sintético `39ae81050fb9930c55b5ac78f55e559b68a9e720`, que no debe confundirse con el merge de main.

- [Knowledge integrity](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44697344018): success.
- [Knowledge audit](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44697343958): success; 141 Python y 63 pruebas Node, sin advertencias semánticas ni documentos huérfanos.
- [Culinary Explorer site](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44697343969): success; reconstrucción reproducible, 590 recetas y 591 archivos del asistente; los cuatro recorridos Chromium finalizaron con passed=true.
- gh-pages `a6f541d03364dade49d0b0f61dd90a2480926496`: mensaje de despliegue Deployed 765d507; se comprobó en la rama el HTML de Shopping, Pantry y Assistant con recursos versionados. La visita independiente de un usuario real al portal público no está acreditada.

| Criterio | Evidencia y límite |
|---|---|
| SHP-01 | Modelo 0.1.0 y límites, diez pruebas Node |
| SHP-02 | Operaciones puras y recorrido Chromium de listas |
| SHP-03 | Validación compartida con Pantry y revisión de cantidades literales |
| SHP-04 | Marcado reversible, filtros, progreso; no modifica Pantry al marcar |
| SHP-05 | Almacenamiento separado y recarga en navegador |
| SHP-06 | Copia JSON, importación validada y cancelación en pruebas |
| SHP-07 | Errores/conflictos simulados, sin garantía de concurrencia transaccional |
| SHP-08 | Selección de ocurrencias desde Assistant y transferencia efímera en Chromium |
| SHP-09 | Revisión de artículos y procedencia; no inferencia de cantidades o faltantes |
| SHP-10 | Incorporación individual de comprados con formulario de revisión; no transferencia masiva |
| SHP-11 | Intención anterior al lote, recuperación sin recreación y fallos parciales inducidos; sin atomicidad |
| SHP-12 | Controles nativos y pruebas Chromium móvil/escritorio; accesibilidad exhaustiva no auditada |
| SHP-13 | Texto no activo y datos personales locales; sin aislamiento de otros scripts del origen |
| SHP-14 | 141 Python, 63 Node y los cuatro recorridos Chromium en CI |
| SHP-15 | Build y despliegue versionados comprobados en rama; prueba manual pública pendiente |

**Estado:** implementación completa, validación técnica dirigida superada y despliegue registrado. La comprobación pública de Shopping y Pantry permanece pendiente. No se aprueba una nueva release; v1.6.0 sigue siendo la última versión publicada. La siguiente capacidad candidata es Culinary Planner, sin anticipar inferencias de suficiencia, disponibilidad o compatibilidad.
