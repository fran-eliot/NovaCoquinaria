---
id: DOC-ALCANCE-PANTRY-2026
titulo: Alcance de entrega de Culinary Pantry
tipo: gestion
version: 0.1.1
estado: borrador
ultima_revision: 2026-11-19
---

# Culinary Pantry — alcance de entrega

## Propósito

Gestionar un inventario personal declarado de alimentos, separado de las fichas canónicas del SGCC. Base: main 94150d80718b5e2aa09f360d991675311a6af998; Explorer y Recipe Assistant publicados. El propietario comunica que el asistente vuelve a funcionar tras #284. No se compromete una nueva release.

## Recorridos

- Crear, consultar, editar y eliminar entradas individuales, con confirmación al eliminar. Permitir varias entradas del mismo alimento para lotes o ubicaciones distintas; no fusionar automáticamente.
- Registrar nombre obligatorio, cantidad opcional (decimal positivo como texto), unidad explícita cuando exista cantidad (opciones domésticas y texto libre acotado), categoría opcional, ubicación (despensa, frigorífico, congelador, otra), tipo de fecha opcional (caducidad o consumo preferente), fecha civil ISO AAAA-MM-DD opcional y notas opcionales. Fecha y tipo se declaran juntos. No convertir unidades ni interpretar cantidades ausentes como cero.
- Buscar y filtrar inventario por nombre, categoría, ubicación y relación temporal con fecha declarada. Mostrar tipo y fecha sin deducir seguridad ni recomendar consumo de producto caducado. La comparación se hace con la fecha civil local, no con horas transcurridas.
- Seleccionar explícitamente entradas y abrir Explorer con menciones textuales AND, siguiendo su semántica de términos. El nombre puede contener calificadores que impidan encontrar coincidencias; permitir ajustar términos en Explorer. No utilizar automáticamente todo el inventario, inferir identidad o requisitos, calcular faltantes ni afirmar que una receta pueda cocinarse. Las cantidades no intervienen en las consultas.
- Exportar una copia JSON versionada y recuperar mediante importación validada con previsualización del recuento y confirmación de sustitución completa; no combinar lotes automáticamente. Cancelación y error no alteran el inventario previo.

## Decisión de persistencia

Se selecciona almacenamiento local del navegador (localStorage), con una clave exclusiva de NovaCoquinaria y un documento de esquema 0.1.0. No se publican datos personales, ni se transmiten a un servidor; el inventario reside en el origen y perfil del navegador. No es almacenamiento cifrado ni aislado de otros scripts del mismo origen; se recomienda evitar información sensible en notas. No hay sincronización, cuentas ni garantía frente a borrado, modo privado o pérdida de dispositivo. La exportación manual constituye el mecanismo de copia de seguridad. Las menciones seleccionadas se transfieren a la aplicación del mismo portal sin incluirlas en la URL ni enviar el inventario a la red; el transporte efímero y la gestión de errores se concretan en integración.

La primera unidad fijará esquema, límites y validación estricta: ID opaco único, versión, campos, tipos, longitudes, fechas reales, decimales sin aproximaciones ni valores no finitos, coherencia de cantidad/unidad y fecha/tipo. Separar datos canónicos de inventario. El núcleo no depende del DOM. El adaptador de persistencia distingue clave ausente, lectura inválida, versión no admitida, almacenamiento bloqueado y escritura fallida. No sustituir ni borrar automáticamente un inventario ilegible. Evitar sobrescribir cambios de otras pestañas de forma silenciosa; documentar que no se ofrece concurrencia transaccional y avisar ante cambios observados. No afirmar guardado si falla; conservar posibilidad de exportar la última copia válida disponible.

## Criterios de aceptación

| ID | Criterio |
|---|---|
| PAN-01 | Esquema versionado, identidad única, campos y límites validados |
| PAN-02 | Alta, edición y eliminación explícitas; lotes separados |
| PAN-03 | Cantidad/unidad y ausencia preservadas; sin equivalencias inventadas |
| PAN-04 | Categoría, ubicación y fechas civiles declaradas; sin inferencia de seguridad |
| PAN-05 | Filtrado y búsqueda reversibles, estados vacíos diferenciados |
| PAN-06 | Persistencia al recargar en el mismo origen/perfil |
| PAN-07 | Errores de lectura, cuota, versión y escritura visibles, sin pérdida silenciosa |
| PAN-08 | Exportación e importación con validación, confirmación y conservación ante error |
| PAN-09 | Aviso de cambios externos observados; límites de concurrencia documentados |
| PAN-10 | Selección explícita de menciones y transferencia local a Explorer; editable y sin inventario en URL |
| PAN-11 | Semántica AND existente; no compatibilidad, suficiencia ni ranking |
| PAN-12 | Interfaz móvil/escritorio, teclado, etiquetas y confirmaciones |
| PAN-13 | Texto no confiable renderizado sin HTML activo; datos personales fuera del repositorio y red |
| PAN-14 | Pruebas puras y de almacenamiento simulado, regresión de aplicaciones y recorridos Chromium |
| PAN-15 | Build y recursos versionados, publicación, guía y evidencia de uso con límites |

## Unidades

| Unidad | Entrega |
|---|---|
| A — Pantry Model | Modelo, validación, operaciones de inventario y filtros |
| B — Pantry Persistence | Adaptador local, copia/importación, fallos y cambios externos |
| C — Pantry UI | Interfaz, edición y selección de menciones |
| D — Integration | Transferencia a Explorer, portal, recursos versionados, pruebas y guía |

No se abre un ciclo de investigación independiente. Exclusiones: compatibilidad, reconciliación automática con IDs canónicos, consumo automático, alertas programadas, conversiones, compra, planificación, IA, backend, sincronización y release. La deuda semántica existente se mantiene.

## Referencias

- [Roadmap](./ROADMAP.md)
- [Revisión estratégica](./REVISION_ESTRATEGICA_CULINARIA.md)
- [Culinary Explorer](./ALCANCE_CULINARY_EXPLORER.md)
- [Recipe Assistant](./ALCANCE_CULINARY_RECIPE_ASSISTANT.md)
- [Deuda de requisitos](./DEUDA_REQUISITOS_CULINARIOS.md)

## Unidad A — Modelo de inventario declarado

El módulo `assets/culinary-pantry-model.mjs` define el documento de esquema 0.1.0 con schema_version y entries, un máximo de 2000 entradas y campos exactos id, name, quantity, unit, category, location, date_type, date y notes. ID opaco de 1–80 caracteres ASCII alfanuméricos, guion o guion bajo, único en el inventario; su generación corresponde al consumidor. Nombre obligatorio hasta 160 caracteres, categoría opcional hasta 80, unidad hasta 40 y notas hasta 1000 (admite salto de línea). Se rechazan textos vacíos, espacios exteriores y controles no admitidos. Los campos opcionales ausentes son null.

La cantidad es un decimal positivo literal con punto, hasta nueve cifras enteras y seis decimales, sin exponentes ni conversión a número; se conservan ceros decimales finales. Cantidad y unidad se declaran juntas. El consumidor podrá adaptar la coma decimal de entrada al punto del formato, sin modificar la magnitud. Las ubicaciones son pantry, fridge, freezer y other. Los tipos de fecha son expiry y best_before, siempre asociados a una fecha civil válida de año 0001–9999. La relación temporal past, today, future o undated no representa seguridad ni estado sanitario.

Las operaciones emptyPantry, validatePantry, addEntry, editEntry y removeEntry devuelven copias, respetan orden y no fusionan lotes. filterEntries acumula filtros de nombre (subcadena), categoría (igualdad), ubicación y relación con una fecha civil explícita. Para nombre y categoría usa NFC y minúsculas, sin eliminar diacríticos. selectedMentions exige selección explícita de IDs existentes, conserva el nombre original y elimina repeticiones según esa misma normalización; no transmite cantidades ni ejecuta búsqueda. La semántica de consultas sigue perteneciendo a Explorer.

Se incorporan ocho pruebas Node y su ejecución en Knowledge audit. El modelo no accede a DOM, red, almacenamiento o conocimiento canónico. Persistencia, confirmaciones, importación, interfaz y publicación quedan pendientes de las unidades B–D. La aceptación del modelo queda condicionada a CI.
