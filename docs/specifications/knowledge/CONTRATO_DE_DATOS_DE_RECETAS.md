---
id: SPEC-CONTRATO-RECETAS
tipo: especificacion
titulo: Contrato de datos de recetas
version: 0.1.0
estado: borrador
ultima_revision: 2026-11-18
tags:
  - recetas
  - contrato
  - ingesta
  - procedencia
---

# Contrato de datos de recetas

## Propósito y alcance

Definir una proyección estructurada, derivada y reconstruible de las recetas Markdown existentes para una primera ingesta e indexación local. Complementa el modelo documental y de componentes sin cambiar su identidad ni sus fuentes canónicas. La versión 0.1.0 es una propuesta para contrastar con muestras reales, no un esquema de persistencia ni un requisito nuevo de front matter.

## Fuente e identidad

El corpus de referencia es el commit `b64dcfc9e9dbff4d8ec6179503d16745430606df`. Se procesan documentos cuyo tipo declarado es `receta`; el módulo físico no determina su identidad ni demuestra una técnica culinaria. Los README y otros tipos se excluyen. Una receta conserva su ID literal (por ejemplo REC-0017 frente a REC-573), sin rellenar ceros ni convertirlo en número. Las colisiones exactas son errores; posibles equivalencias de formato se diagnostican sin fusionar registros.

## Proyección lógica

| Campo | Forma | Regla |
|---|---|---|
| contract_version | texto | Versión de este contrato |
| id | texto | ID exacto de origen, obligatorio |
| source | objeto | commit, ruta relativa, huella de bytes y localizadores de evidencia |
| metadata | objeto | Front matter original conservado, incluida versión y estado |
| title | texto | Título declarado |
| physical_module | texto o nulo | Primer directorio, sin inferir dominio |
| category | texto o nulo | Categoría explícita; no completar desde carpeta |
| yield | objeto o nulo | Texto original, cantidad y unidad si son inequívocas |
| durations | lista | Fase, texto original, intervalo y unidad si son inequívocos; no sumar fases automáticamente |
| ingredients | lista ordenada | Una entrada por línea de ingrediente; conservar grupos |
| steps | lista ordenada | Texto y orden original de los pasos explícitos |
| sections | lista ordenada | Encabezado, contenido y localizador; incluye secciones no interpretadas |
| references | lista | Destino original, destino resuelto e ID si existe |
| evidence | objeto | Evidencia de elaboración, valoración y alcance, separada del estado documental |
| diagnostics | lista | Código, gravedad, campo, localizador y descripción |

La proyección no sustituye la fuente: conserva texto original, metadatos desconocidos y referencias para poder reconstruir las decisiones de extracción, no necesariamente reproducir un Markdown byte a byte. La fuente identificada por commit y huella permite recuperar los bytes originales.

## Ingredientes y cantidades

Cada entrada contiene `raw`, `group` (o nulo), `name` (o nulo), `quantity`, `optionality`, `ingredient_id` (o nulo), `resolution` y `source_location`. La cantidad conserva su texto y utiliza uno de estos estados:

| Estado | Representación | Ejemplo |
|---|---|---|
| exact | min = max; unidad explícita o recuento | 300 g |
| range | min y max | 220–260 ml |
| qualitative | límites nulos; texto conservado | al gusto, una pizca |
| missing | límites y unidad nulos | pimienta negra |
| ambiguous | límites y unidad nulos; diagnóstico | expresión no interpretable con confianza |

Los números se expresan como decimales exactos o fracciones racionales; la futura serialización debe evitar pérdida por redondeo. Se conservan unidades domésticas (cucharada, vaso, diente, unidad), sin convertir a gramos o mililitros sin evidencia. Una expresión como «medio limón» mantiene su unidad contextual. No se transforma «sin cantidad» en cero. Los calificadores (escurrido, pelado, colmada, opcional) permanecen en el texto. Las alternativas conservan la expresión completa, sin duplicar cantidades ni exigir ambos ingredientes.

`optionality`: required, optional, unknown según declaración o grupo explícito. La ausencia de una marca opcional en una línea claramente perteneciente a la lista base permite required; los casos dudosos quedan unknown. Un enlace a un ingrediente en la propia línea permite resolución explícita cuando su destino válido declara tipo ingrediente; un enlace genérico en Relaciones no demuestra por sí solo que una línea tenga esa identidad. La resolución admite explicit, unresolved, ambiguous. No crear IDs ni coincidencias por subcadena como hechos.

## Evidencia culinaria y procedencia

El estado de publicación del front matter (borrador, estable, etc.) es independiente de la elaboración. La evidencia distingue:

- pending: la fuente declara que no consta prueba o que está pendiente.
- prepared: existe declaración de elaboración, con alcance concreto.
- unknown: no hay evidencia suficiente o es contradictoria.

La valoración es un campo separado, nulo cuando no consta. Cada afirmación de evidencia conserva texto y localizador. El alcance distingue fórmula actual, preparación histórica o indeterminado. Una receta adaptada de una preparación anterior no acredita que las nuevas cantidades, tiempos o acabados se hayan probado. No inferir una preferencia ni una versión superior a partir de la fecha.

## Muestras de contraste

Las siguientes observaciones son lecturas documentales del corte indicado, no resultados de un parser implementado.

| Fuente | Caso | Resultado esperado |
|---|---|---|
| [Talo vasco](../../../10_Horno/talo_vasco_de_maiz_en_plancha.md) REC-573 | 300 g harina; 220–260 ml agua | Exacta e intervalo; módulo Horno no implica horneado; pendiente |
| [Curry amarillo de pollo](../../../05_Carnes/curry_amarillo_de_pollo.md) REC-0017 | versión 1.0, estado estable, enlaces inline, opcionales y aceite sin cantidad | Versión literal, categoría ausente, no consta prueba; enlace explícito y cantidad ausente |
| [Pastel de manzana](../../../08_Postres/pastel_de_manzana.md) REC-0079 | 840 g actuales; 640/200 g de distribución; lemon curd histórico | No duplicar ingredientes desde distribución; separar experiencia y fórmula propuesta |
| [Pipirrana jiennense](../../../04_Verduras/pipirrana_jiennense_con_atun_y_huevo.md) REC-485 | 10–15 ml de vinagre opcional, sal sin cantidad | Intervalo opcional, cantidad ausente, pendiente de prueba |

En el pastel, los 840 g utilizados y el problema con el lemon curd están registrados históricamente; la alternativa de mermelada espesa y medidas de horno requieren contraste. No atribuir el resultado anterior a la formulación actual completa.

## Validación y diagnósticos

Errores bloqueantes: front matter ilegible, identidad ausente o duplicada, fuente sin procedencia verificable. Diagnósticos no bloqueantes: cantidad ambigua, ingrediente sin resolver, evidencia indeterminada, duración no interpretable y referencias no resueltas (sin sustituir los controles de integridad existentes). Una ausencia legítima no es un error; se representa explícitamente. Los diagnósticos de extracción son independientes de las advertencias del auditor semántico.

## Criterios de aceptación del primer prototipo

- Reproducir el inventario de documentos de tipo receta y explicar discrepancias con el inventario de rutas.
- Preservar identidad, versión literal, texto de ingredientes, orden, referencias y evidencia sin sobrescribir Markdown.
- Superar los casos de contraste y pruebas sintéticas de cantidades, opcionalidad, ausencia y ambigüedad.
- Generar el mismo contenido derivado con el mismo commit, configuración y versión de extractor; separar marcas temporales de ejecución.
- Permitir consultar por ID, metadatos y texto o identidad de ingredientes, distinguiendo correspondencias explícitas de búsqueda textual.
- Informar cobertura de extracción y diagnósticos sin equipararlos a calidad culinaria o validación doméstica.

## Límites

No se introduce una base de datos, API, esquema obligatorio de YAML, motor RAG ni agente. No se reescriben fichas masivamente ni se completa información nutricional, alérgenos o cantidades por inferencia. La serialización, implementación y evaluación del índice serán incrementos posteriores.

## Referencias

- [Modelo documental](./ESPECIFICACION_DE_DOCUMENTOS.md)
- [Componentes](./ESPECIFICACION_DE_COMPONENTES.md)
- [Relaciones](./ESPECIFICACION_DE_RELACIONES.md)
- [Ingesta](../ingestion/ESPECIFICACION_DE_INGESTA.md)
- [Decisión de metadatos canónicos](../../governance/adr/ADR-0004-front-matter-yaml-como-metadatos-canonicos.md)
- [Independencia lógica y física](../../governance/adr/ADR-0019-independencia-entre-el-modelo-logico-del-conocimiento-y-su-representacion-fisica.md)
- [Recetas cocinadas](../../management/RECETAS_COCINADAS.md)
- [Registro de tandas](../../management/REGISTRO_DE_TANDAS.md)
