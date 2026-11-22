---
id: DOC-RPC-B-MUESTRA-2026
titulo: Recipe Practical Completeness — RPC-B, muestra y protocolo predefinidos
tipo: gestion
version: 0.1.0
estado: protocolo-fijado-pendiente-de-evaluacion
ultima_revision: 2026-11-22
---

# Recipe Practical Completeness — RPC-B: muestra y protocolo

## Objetivo, corte y condición de la revisión

Esta propuesta **fija diez fichas y su rúbrica antes de evaluarlas editorialmente**. Se seleccionaron dos recetas de cada uno de los cinco módulos no representados en el piloto B01–B08: Pastas, Legumbres, Postres, Bebidas y Horno. Las rutas y los identificadores fueron comprobados directamente en el repositorio en `main` tras [PR #348](https://github.com/fran-eliot/NovaCoquinaria/pull/348), merge `3c8761e1f611ec348d48e98701b637dae3386d71`. La [RPC-A](./DIAGNOSTICO_RECIPE_PRACTICAL_COMPLETENESS.md) es el contrato de referencia.

Esta selección es **dirigida y no estadísticamente representativa**; prioriza contrastes prácticos variados y no estima la prevalencia de problemas en los 590 documentos. Una valoración editorial, una comprobación individual de aplicaciones o una modificación de recetas **no forman parte de esta PR**. No se autoriza otra release ni la introducción de un clasificador automático de «recetas cocinables».

## Muestra fijada antes del examen

| Caso | Módulo | ID y título canónico | Ruta canónica | Motivo previo de selección, no hallazgo |
|---|---|---|---|---|
| RPC-B01 | Pastas | `REC-0024` · Espaguetis a la carbonara | `02_Pastas/espaguetis_a_la_carbonara.md` | Salsa sensible al calor y dependencia de plantilla/técnica |
| RPC-B02 | Pastas | `REC-367` · Conchiglioni rellenos de atún y requesón al horno | `02_Pastas/conchiglioni_rellenos_de_atun_y_requeson_al_horno.md` | Precocción, relleno, gratinado y propuesta pendiente de prueba |
| RPC-B03 | Legumbres | `REC-0033` · Garbanzos guisados con espinacas | `03_Legumbres/garbanzos_con_espinacas.md` | Legumbre ya cocida, alternativas de producto y tiempos |
| RPC-B04 | Legumbres | `REC-0034` · Alubias blancas estofadas con hortalizas | `03_Legumbres/alubias_estofadas.md` | Remojo, cocción prolongada y tiempo activo frente a transcurrido |
| RPC-B05 | Postres | `REC-0079` · Pastel de manzana de textura húmeda | `08_Postres/pastel_de_manzana.md` | Evolución doméstica y conservación de versiones y evidencia |
| RPC-B06 | Postres | `REC-0081` · Arroz con leche cremoso | `08_Postres/arroz_con_leche.md` | Cocción gradual, textura y rendimiento |
| RPC-B07 | Bebidas | `REC-0087` · Limonada casera | `09_Bebidas/limonada_casera.md` | Dilución, rendimiento por vasos y reposo opcional |
| RPC-B08 | Bebidas | `REC-0092` · Chocolate caliente con cacao | `09_Bebidas/chocolate_caliente.md` | Espesante opcional y condiciones de incorporación |
| RPC-B09 | Horno | `REC-0216` · Bacalao gratinado con puerro y mostaza | `10_Horno/bacalao_gratinado_con_puerro_y_mostaza.md` | Preparación propuesta, horno y dependencias de producto |
| RPC-B10 | Horno | `REC-561` · Broa gallega de maíz y centeno | `10_Horno/broa_gallega_de_maiz_y_centeno.md` | Hogaza y reposos múltiples; receta tradicional pendiente de prueba |

Los identificadores son cadenas y se conservarán **literalmente**, incluidos `REC-367` y `REC-561` sin rellenar con ceros. La selección se congelará una vez aprobada; cualquier cambio de ficha requiere una revisión explícita previa al análisis y no puede efectuarse después de observar resultados inconvenientes.

## Rúbrica predefinida

Se aplican los nueve ejes de [RPC-A](./DIAGNOSTICO_RECIPE_PRACTICAL_COMPLETENESS.md) y sus cinco estados **`presente`, `interpretado`, `no_declarado`, `desconocido`, `no_aplica`**. Los estados califican **observaciones concretas**, no «calidad global» de una receta. Separar «el dato existe» de «la receta puede ejecutarse sin suposiciones» mediante una conclusión editorial narrada y trazable.

| Eje | Pregunta de revisión en estas diez fichas | Evidencia requerida |
|---|---|---|
| RPC-01 · Ingredientes | ¿La formulación separa cantidades y componentes principales de opcionales o guarniciones? | Fragmento canónico y relación con los pasos |
| RPC-02 · Preparaciones reutilizadas | Si se cita una plantilla/base, ¿es localizable y se entiende la dosis o el papel que cumple? | Enlace y, cuando aplique, documento referenciado |
| RPC-03 · Secuencia | ¿Están documentados el orden, los puntos sensibles y las condiciones necesarias? | Paso o sección concreta |
| RPC-04 · Tiempos | ¿Se diferencian preparación, cocción, reposo y total, sin sumar tiempos incompatibles? | Expresiones exactas y cautela con parser |
| RPC-05 · Rendimiento | ¿Se declara cantidad final o raciones en unidad utilizable, sin prometer escalado universal? | Tabla, Front Matter y contexto |
| RPC-06 · Condiciones | ¿Se distinguen producto seco/cocido, salado/desalado, temperatura, opciones y variabilidad de técnica? | Condiciones explícitas |
| RPC-07 · Experiencia | ¿Se separan la preparación doméstica y la propuesta o adaptación no probada? | Registro de experiencia y advertencias |
| RPC-08 · Acceso | ¿Explorer y Assistant permiten localizar y consultar la ficha sin perder contexto ni fuente? | Prueba específica con ID, ruta, viewport y SHA |
| RPC-09 · Precauciones | ¿Se explican riesgos concretos sin texto genérico ajeno ni garantías de seguridad? | Sección de puntos críticos, alérgenos o conservación |

**No ejecutar o no observar un eje = `desconocido`**, nunca conforme por defecto. `No_aplica` exige razón explícita. Para RPC-08, las pruebas generales ya existentes no cuentan como comprobación específica de esta nueva muestra; una futura ejecución local en Chromium no será equivalente a aceptación manual pública.

## Método de evaluación posterior

1. Fijar commit de `main`, SHA del archivo y sección o líneas del pasaje para cada caso. Leer las diez fichas completas y sus plantillas realmente utilizadas.
2. Abrir registro de observaciones por eje, con estado, cita canónica, necesidad culinaria y límite de interpretación. Usar el estado `desconocido` ante información insuficiente.
3. No inferir tiempos totales por suma si existen esperas paralelas, tiempos variables o alternativas. No inferir raciones a partir del tamaño de una hogaza o vaso.
4. Evaluar por separado historia de preparación, propuesta aún no cocinada y recetas con variantes. Conservar la mejor formulación y anotaciones negativas históricas en caso de futuras correcciones.
5. Revisar RPC-08 de cada una de las diez fichas individualmente; distinguir test de Chromium local, prueba en el sitio público y valoración doméstica.
6. Registrar resultados, controles sin intervención y **como máximo seis** propuestas editoriales concretas en una PR independiente. No cambiar recetas durante el examen ni crear una puntuación agregada de «cocinabilidad».

### Entregable y puertas de revisión

El entregable de esta PR es la **selección fijada y el protocolo**, no una evaluación de los diez casos. El avance posterior a una evaluación RPC-B, y especialmente una intervención RPC-C, requerirá evidencia y aprobación independientes. Si la muestra muestra incertidumbre abundante, registrar abstenciones antes que intentar completar datos automáticamente. La arquitectura sigue siendo Markdown canónico y el último lanzamiento publicado continúa siendo `v1.7.0`.


## Evaluación documental posterior, sin alterar la selección

Tras fijar la presente muestra se ha realizado una [evaluación documental RPC-B](./EVALUACION_RPC_B_SUFIENCIA_PRACTICA.md) sobre los diez casos y las plantillas relacionadas. Se documentan observaciones y cuatro posibles intervenciones editoriales; RPC-08, recorrido individual en Explorer/Assistant de esta muestra, **permanece desconocido/no ejecutado**. La evaluación se tramita en una PR independiente y no modifica las fichas canónicas ni la selección original.
