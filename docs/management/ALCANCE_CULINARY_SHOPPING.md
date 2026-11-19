---
id: DOC-ALCANCE-SHOPPING-2026
titulo: Alcance de entrega de Culinary Shopping
tipo: gestion
version: 0.1.0
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
