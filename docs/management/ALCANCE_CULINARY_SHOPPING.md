---
id: DOC-ALCANCE-SHOPPING-2026
titulo: Alcance de entrega de Culinary Shopping
tipo: gestion
version: 0.1.4
estado: borrador
ultima_revision: 2026-11-19
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
