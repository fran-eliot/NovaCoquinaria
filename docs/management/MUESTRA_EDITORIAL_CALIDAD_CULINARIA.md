---
id: DOC-MUESTRA-EDITORIAL-CULINARIA-2026
titulo: Culinary Knowledge Quality Baseline — Unidad B, muestra y rúbrica fijadas
tipo: gestion
version: 0.1.0
estado: protocolo-de-revision
ultima_revision: 2026-11-22
---

# Culinary Knowledge Quality Baseline — Unidad B

## Objetivo y regla de precedencia

Este documento **fija la muestra y los criterios antes de emitir valoraciones editoriales**. No constituye todavía un informe de hallazgos o una propuesta de corrección de las recetas. La [Unidad A](./LINEA_BASE_CALIDAD_CULINARIA.md) acredita cobertura descriptiva mediante CI, no calidad culinaria humana. La selección siguiente toma como referencia `main` en `47c2b0c618c893746c1e2524a956bb103e986c90` (merge #340), sin atribuir a la muestra validez estadística para las 590 recetas.

El protocolo debe conservarse sin alterar la selección después de obtener resultados. Cualquier sustitución por archivo ausente o incidencia deberá quedar registrada y justificada en una nueva revisión, antes de evaluar el sustituto. La revisión de esta PR aprueba **protocolo y selección**, no constata que las ocho recetas hayan sido cocinadas ni califica aún sus resultados.

## Selección dirigida y verificable

Se han verificado las ocho rutas en el repositorio, procurando cruzar dominios, recetas con experiencia doméstica declarada, propuestas pendientes, registros con decisiones de preparación no equivalentes a pruebas y casos de requisitos ambiguos ya conocidos. No es una selección aleatoria ni equilibrada entre los diez módulos del recetario.

| Caso | ID y preparación | Ruta canónica | Estrato deliberado |
|---|---|---|---|
| B01 | `REC-0007` · Hamburguesa asiática | `05_Carnes/hamburguesa_asiatica.md` | Experiencia doméstica declarada, variante y adaptación de cantidades |
| B02 | `REC-0009` · Caballa japonesa | `06_Pescados_y_Mariscos/caballa_japonesa.md` | Experiencia doméstica declarada, elección de guarnición |
| B03 | `REC-0008` · Medallones de solomillo asiáticos | `05_Carnes/medallones_solomillo_asiaticos.md` | Preparación planteada sin confirmación suficiente de ejecución |
| B04 | `REC-0021` · Arroz frito con gambas | `01_Arroces/arroz_frito_gambas.md` | Formulación documentada, técnicas de base y trazabilidad de ejecución |
| B05 | `REC-448` · Patatas a la importancia castellanas | `04_Verduras/patatas_a_la_importancia_castellanas.md` | Receta tradicional propuesta y pendiente de prueba; ajustes condicionales |
| B06 | `REC-0057` · Merluza al horno con limón y ajo | `06_Pescados_y_Mariscos/merluza_al_horno_con_limon.md` | Condición de descongelación, variación de tiempos por grosor |
| B07 | `REC-0059` · Gambas al ajillo | `06_Pescados_y_Mariscos/gambas_al_ajillo.md` | Ingrediente opcional y preparación condicionada |
| B08 | `REC-0201` · Calamares salteados con kimchi | `07_Cocina_Asiatica/calamares_salteados_con_kimchi.md` | Formulación pendiente de prueba, opcionalidad y condición de agua |

Esta muestra incluye cinco módulos físicos y sobre-representa pescados y preparaciones asiáticas intencionadamente para contrastar condiciones y alternativas de ingredientes. **No incluye pastas, legumbres, postres, bebidas ni horno como módulo físico**, y por ello no permite evaluar esos ámbitos. No utilizar «representativa» en sentido inferencial para esta selección. Las variantes o recetas adicionales que se identifiquen durante la revisión se pueden citar como contexto, pero no entrarán en el denominador fijado de ocho casos.

## Rúbrica de evaluación editorial

Cada uno de los ocho casos se revisará en el Markdown canónico y, cuando corresponda, en Explorer y Recipe Assistant publicados. Para cada eje se consignará `conforme`, `incidencia`, `desconocido` o `no_aplica`, con cita localizable de archivo, sección y líneas o encabezado. **Desconocido no equivale a incidencia y conforme no equivale a receta probada.**

| Eje | Pregunta de revisión | Evidencia requerida |
|---|---|---|
| E01 · Identidad y procedencia | ¿La ficha y las referencias permiten distinguir receta, variantes y antecedentes? | ID, ruta, enlaces y referencias explícitas |
| E02 · Ingredientes y cantidades | ¿Las cantidades y unidades declaradas permiten seguir la formulación, sin completar valores ausentes por suposición? | Sección de ingredientes y correspondencia con pasos |
| E03 · Elaboración y secuencia | ¿Los pasos contienen el orden y las condiciones necesarios, o dejan decisiones críticas implícitas? | Pasos y técnicas enlazadas |
| E04 · Rendimiento y tiempo | ¿Se declara rendimiento y duración con límites claros y sin atribuir total ficticio? | Front Matter, tabla informativa y texto |
| E05 · Alternativas y condiciones | ¿Se distinguen elecciones, opcionales, guarniciones, ajustes y preparación condicional? | Frases exactas y alcance contextual |
| E06 · Experiencia y grado de verificación | ¿La preparación realmente probada se distingue de la propuesta, intento o valoración recordada? | Declaración explícita y cautelas en fuente |
| E07 · Valor práctico del recorrido | ¿El explorador localiza la ficha y el asistente conserva contexto y advertencias suficientes para consultar la fuente? | Resultado observado en aplicación con ID y URL |
| E08 · Seguridad y limitaciones documentales | ¿Los riesgos presentes se presentan con prudencia sin aparentar validación clínica o seguridad garantizada? | Controles de cocción, alérgenos y ausencia de afirmaciones infundadas |

Las menciones documentales sobre seguridad se revisarán como **calidad de redacción y trazabilidad**, no como certificación alimentaria. No se promoverán identidades candidatas, requisitos inferidos, rendimientos ambiguos ni estados de elaboración a partir de heurísticas.

## Procedimiento de contraste y entregable posterior

1. Fijar SHA de la fuente de cada caso y leer el documento completo, no solo Front Matter o proyección.
2. Contrastar los ocho ejes por caso y conservar evidencia localizable. Evitar forzar conclusiones en `no_aplica` o `desconocido`.
3. Recorrer Explorer y Assistant con la misma receta solo para verificar la utilidad de navegación y exposición del contexto; no usar estado de Pantry como prueba de disponibilidad de ingredientes.
4. Clasificar problemas: **crítico reproducible**, **mejora editorial útil**, **dato pendiente de experiencia**, **fuera del alcance**. Mantener variantes y versiones superiores.
5. Proponer como máximo seis intervenciones concretas y reversibles para la Unidad C, sin mezclarlas con este protocolo ni declarar resultados antes de observarlos.
6. Registrar denominadores por eje (casos aplicables, revisados, conformes, incidencias, desconocidos), y por separado el número de recetas. No calcular una única nota de «calidad culinaria».

**Condición de salida de esta PR:** muestra y rúbrica fijadas, rutas verificadas, sin modificaciones de recetas ni conclusiones anticipadas. La evaluación y cualquier corrección quedan para PR posteriores.

## Relación con decisiones del proyecto

- [Línea base técnica, Unidad A](./LINEA_BASE_CALIDAD_CULINARIA.md).
- [Revisión estratégica post-aceptación](./REVISION_ESTRATEGICA_POST_ACEPTACION_PUBLICA.md).
- [Deuda de requisitos culinarios](./DEUDA_REQUISITOS_CULINARIOS.md).
- [Kit de continuidad 3.0.0](./NOVACOQUINARIA_KIT_CONTINUITY.md).

La versión publicada permanece en `v1.7.0`. Esta selección no autoriza nuevas releases, nuevas funcionalidades ni una reescritura sistemática del recetario.
