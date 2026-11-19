---
id: DOC-ALCANCE-EXPLORER-2026
titulo: Alcance de entrega de Culinary Explorer
tipo: gestion
version: 0.1.0
estado: borrador
ultima_revision: 2026-11-19
---

# Culinary Explorer — alcance de entrega

## Base y propósito

La [revisión estratégica](./REVISION_ESTRATEGICA_CULINARIA.md) quedó integrada en #269, merge `a2916e15075e05c8ccf47340635e212609b14354`. Knowledge integrity y Knowledge audit de esa PR finalizaron correctamente. Culinary Explorer 0.1.0 propone una aplicación consumidora de solo lectura para encontrar y consultar las recetas del SGCC desde el portal existente. La versión de capacidad no implica nueva release.

## Recorridos cotidianos

- Explorar el catálogo completo y reducirlo por módulo físico o evidencia de elaboración.
- Localizar una receta por título completo o secuencia contigua de términos de título. Este último es un comportamiento de presentación nuevo y explícito, no una ampliación silenciosa del motor Python.
- Buscar menciones de uno o varios ingredientes mediante secuencias contiguas de términos, con intersección a nivel de receta.
- Consultar título, módulo, evidencia, coincidencias de ingredientes y enlace a la ficha publicada. Mostrar tiempos y rendimientos solo si se preservan sus declaraciones originales, sin filtros ni cálculos en esta entrega.
- Distinguir catálogo vacío, resultado sin coincidencias, entrada inválida y fallo de carga.

Ejemplo: módulo de carnes e ingredientes «ajo» y «salsa de soja». El resultado identifica recetas con ambas menciones, no recetas necesariamente cocinables ni una lista de compra.

## Diseño acotado

Se propone una generación estática Python durante la preparación de MkDocs y un consumidor HTML/CSS/JavaScript sin dependencias de ejecución externas. El despliegue actual ejecuta tools/build_site_docs.py antes de mkdocs gh-deploy. La unidad A verificará el flujo real de generación, la inclusión de recetas y las rutas de destino; no se presupone que todas las rutas sean actualmente navegables. No se adopta backend, API, servicio de búsqueda remoto o persistencia.

El adaptador de publicación consume exclusivamente el índice 0.2.0 generado desde la proyección vigente. Produce un JSON versionado de solo lectura con commit, huella de índice, versión de esquema y registros mínimos: ID literal, título, módulo físico, estado de evidencia, destino relativo y ocurrencias textuales con posición y opcionalidad. La representación puede incluir texto original y localizador cuando sean necesarios para mostrar evidencia. No publicar el índice completo por defecto. La unidad A fijará nombres y tipos concretos, política de nulos, rutas relativas y huella de los bytes. No versionar los artefactos generados como conocimiento.

El adaptador de consulta reutilizará claves o tokens derivados con las funciones Python existentes cuando sea posible. Si el navegador requiere lógica propia de consulta, se limitará a las operaciones expuestas y se contrastará con el motor de referencia mediante conjuntos de IDs y posiciones. NFC, casefold, diacríticos, separadores y contigüidad deberán preservarse; no basta con asumir equivalencia de lowercase en JavaScript. Para título, la nueva modalidad se documentará y contrastará con un recorrido independiente. Se mantendrá el contrato del motor 0.2.0. No se incorporan identidades candidatas a las búsquedas de usuario ni se promueven reglas experimentales.

## Criterios de aceptación

| ID | Criterio |
|---|---|
| EXP-01 | Catálogo completo respecto al índice del mismo commit, IDs literales únicos, sin recuentos históricos constantes |
| EXP-02 | Proyección mínima versionada, reproducible byte a byte, con commit y huella de entrada; no modifica Markdown ni índice |
| EXP-03 | Validación bloqueante de esquema, IDs, referencias y rutas; ninguna carga parcial se presenta como catálogo completo |
| EXP-04 | Título completo o términos contiguos de título, con modalidad documentada, diacríticos conservados y contraste independiente |
| EXP-05 | Ingredientes por terms con equivalencia al motor 0.2.0, sin subcadenas, expansión ni inferencia |
| EXP-06 | Varias cláusulas de ingrediente en AND, combinables con módulo y evidencia, con resultados únicos y orden estable por ID literal |
| EXP-07 | Cada coincidencia conserva nombre y posición de ocurrencia, opcionalidad y acceso a fuente; se identifica como mención |
| EXP-08 | Evidencia original conservada; desconocido no equivale a pendiente y prepared no acredita la fórmula actual |
| EXP-09 | Cada enlace de receta resuelve a un destino publicado del mismo build; verificar rutas y caracteres especiales |
| EXP-10 | Interfaz operable con teclado, etiquetas visibles, foco y diseño adaptable a móvil y escritorio |
| EXP-11 | Estados de carga, error, consulta inválida y cero resultados diferenciados, con posibilidad de limpiar filtros |
| EXP-12 | Renderizado de datos como texto, rutas relativas validadas, sin HTML no confiable ni dependencias de red externas |
| EXP-13 | Regresión del motor y contraste de resultados/ocurrencias en casos sintéticos y corpus vigente, incluidos Unicode, negaciones, alternativas y opcionalidad |
| EXP-14 | Build local reproducible y verificación CI de artefactos y enlaces antes de publicación; despliegue únicamente por el flujo vigente |
| EXP-15 | Guía de uso y recorridos prácticos documentados con resultados observados, límites y evidencia de pruebas; no confundir validación técnica y culinaria |

## Unidades

| Unidad | Entrega | Criterios principales |
|---|---|---|
| A | Proyección consumible, contrato concreto y validaciones de publicación | EXP-01–03, 07–09 |
| B | Adaptador de búsqueda acotado y contraste con referencia | EXP-04–08, 13 |
| C | Interfaz estática accesible y recorridos básicos | EXP-06–12 |
| D | Integración de build/CI, comprobación de rutas, guía y cierre | EXP-09–15 y revisión conjunta |

Los criterios pueden solaparse. Cada unidad se entrega por separado; la aceptación final requiere evidencia conjunta, no mera fusión. La comprobación del portal desplegado se diferencia de la verificación previa del build. No se exige un nuevo ciclo de discovery; los problemas concretos se resuelven dentro de la unidad correspondiente.

## Exclusiones

No incluye compatibilidad receta-despensa, disponibilidad, alérgenos, sustituciones, escalado, filtros temporales o de rendimiento, escritura, cuentas, listas de compra, planificación, IA ni nuevos contratos canónicos. La [deuda de requisitos](./DEUDA_REQUISITOS_CULINARIOS.md) continúa diferida. No se compromete calendario ni release de proyecto. Se mantiene el flujo de revisión mediante PR.

## Referencias

- [Contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md)
- [Alcance de recuperación textual](./ALCANCE_RECUPERACION_TEXTUAL.md)
- [Arquitectura](../architecture/ARQUITECTURA.md)
- [Revisión estratégica](./REVISION_ESTRATEGICA_CULINARIA.md)
