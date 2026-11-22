---
id: DOC-RPC-B-EVALUACION-2026
titulo: Recipe Practical Completeness — evaluación documental RPC-B
tipo: gestion
version: 0.1.0
estado: evaluacion-documental-dirigida
ultima_revision: 2026-11-22
---

# RPC-B — Evaluación documental de suficiencia práctica

## Corte, método y alcance

La muestra de diez fichas, dos por cada módulo Pastas, Legumbres, Postres, Bebidas y Horno, se fijó **antes de evaluarla** en [MUESTRA_RPC_B_SUFIENCIA_PRACTICA.md](./MUESTRA_RPC_B_SUFIENCIA_PRACTICA.md), PR #349, fusionada en `bd8f5f54450db40f204eedbdb08ba8fd15f17722`. Se leyeron íntegros los diez Markdown canónicos y se contrastaron las plantillas pertinentes: `pasta_con_salsa.md`, `pasta_al_horno.md`, `guiso_de_legumbres.md` y `cocer_legumbres.md`, sobre ese corte de `main`. Esta es una **evaluación de utilidad documental**, no una prueba en cocina ni una estimación estadística para las 590 recetas.

Los nueve ejes RPC-01–RPC-09 y los cinco estados `presente`, `interpretado`, `no_declarado`, `desconocido`, `no_aplica` se definen en [RPC-A](./DIAGNOSTICO_RECIPE_PRACTICAL_COMPLETENESS.md). En la tabla siguiente solo se registran observaciones localizadas de interés. **No se asigna una nota global por receta ni se convierte ausencia de datos en defecto culinario confirmado.** Los localizadores son ruta, identificador y encabezado del documento; se debe verificar el texto exacto y el SHA del corte al reproducirlo.

La navegación **RPC-08 permanece `desconocido` para los diez casos**, porque no se ejecutó aquí una nueva comprobación individual Explorer → Assistant → fuente. Los tests de otras recetas no sustituyen esta prueba.

## Evidencia por ficha

| Caso | Ruta e ID | Estados y observaciones documentales | Decisión provisional |
|---|---|---|---|
| RPC-B01 | `02_Pastas/espaguetis_a_la_carbonara.md` · `REC-0024` | RPC-01 `presente` (200 g pasta, 80 g guanciale, huevo y queso); RPC-02 `presente` (plantilla y técnica enlazadas); RPC-03 y RPC-06 `presente` (ligado fuera del fuego, sustituciones diferenciadas); RPC-04 `presente` para tiempos parciales, total `no_declarado`; RPC-07 `desconocido` para preparación doméstica efectiva | Control de redacción con límites de huevo expresos; no corregir por falta de tiempo total calculado |
| RPC-B02 | `02_Pastas/conchiglioni_rellenos_de_atun_y_requeson_al_horno.md` · `REC-367` | RPC-01 y RPC-03 `presente` (cantidades, precocción y gratinado); RPC-04 `presente` para 12–15 min de reducción, 20–25 min de horno y 5 min de reposo, pero total `no_declarado`; RPC-07 `presente` como **pendiente de prueba**; RPC-02 `presente` como enlace, pero la plantilla enlazada declara expresamente que **no es específica para pasta rellena** | H-RPC-B02: evitar aparentar aplicabilidad literal de la plantilla genérica; aclarar su función parcial, no reemplazar la secuencia canónica |
| RPC-B03 | `03_Legumbres/garbanzos_con_espinacas.md` · `REC-0033` | RPC-01, RPC-03 y RPC-06 `presente` (garbanzo **ya cocido**, espinaca congelada condicionada, volumen variable); RPC-04 `presente` para preparación y cocción, total `no_declarado`; RPC-07 `desconocido` en cuanto a experiencia doméstica | Control de legumbre precocida; no confundir el tiempo rápido con el cocinado desde seco |
| RPC-B04 | `03_Legumbres/alubias_estofadas.md` · `REC-0034` | RPC-01 `presente` (320 g de alubias **secas**); RPC-03 y RPC-06 `presente` (remojo, revisión de variedad y cocción segura según técnica); RPC-04 `presente` para 8–12 h de remojo y 75–120 min o más de cocción, total único `no_declarado`; RPC-07 `desconocido` | H-RPC-B04: la ficha permite planificar por fases, pero no convertir rangos parciales en duración total universal; mejora opcional de legibilidad de planificación |
| RPC-B05 | `08_Postres/pastel_de_manzana.md` · `REC-0079` | RPC-01, RPC-03, RPC-05 y RPC-06 `presente` (840 g netos, reparto 640+200 g, molde, cocción orientativa); RPC-07 `presente` como **experiencia histórica diferenciada de la formulación actual**: resultado desfavorable del lemon curd diluido y preferencia de probar mermelada espesa; no hay confirmación de esa nueva cobertura | Control positivo de trazabilidad y de variante mejorada **sin inventar nueva prueba** |
| RPC-B06 | `08_Postres/arroz_con_leche.md` · `REC-0081` | RPC-01, RPC-03, RPC-05, RPC-06 y RPC-09 `presente` (cantidades, reducción, espesor al enfriar y refrigeración rápida); RPC-04 `presente` para 10 min + 35–50 min, total `no_declarado`; RPC-07 `desconocido` | Control positivo de preparación por criterio de textura; no declarar tiempo total calculado |
| RPC-B07 | `09_Bebidas/limonada_casera.md` · `REC-0087` | RPC-01 `presente` (150 ml de zumo, 850 ml de agua, 50–75 g de azúcar); RPC-05 `presente` («4 vasos»); RPC-03 **ambiguo**: paso 2 utiliza «100 ml de agua templada» y paso 3 «agua restante», sin aclarar si son parte de los 850 ml. RPC-04 `presente` para 10 min y reposo opcional de 15 min, tiempo de enfriado no cuantificado; RPC-07 `desconocido` | **H-RPC-B07 prioritario:** aclarar que los 100 ml proceden de los 850 ml o documentar explícitamente el total distinto; no cambiar concentraciones arbitrariamente |
| RPC-B08 | `09_Bebidas/chocolate_caliente.md` · `REC-0092` | RPC-01 `presente` (500 ml de leche, 40 g cacao, 10 g maicena opcional); RPC-03 y RPC-06 `presente` (100 ml **reservados de la leche declarada**, añadido de espesante condicionado); RPC-04 `presente` para preparación y cocción, sin total expreso; RPC-07 `desconocido` | Control positivo frente a B07: líquido de mezcla correctamente indicado como parte del total |
| RPC-B09 | `10_Horno/bacalao_gratinado_con_puerro_y_mostaza.md` · `REC-0216` | RPC-01 `presente` (desalado como condición del producto, ingredientes pesados); RPC-03 y RPC-06 `presente` (190 °C, grosor y punto de pescado, queso opcional); RPC-04 `presente` para pochado 8–10 min y horno 12–18 min, tiempo total `no_declarado`; RPC-07 `presente` como propuesta pendiente; RPC-09 contiene conservación **genérica** sobre huevo/carne ajenos a la fórmula | H-RPC-B09: limitar la conservación al bacalao, lácteos y resto de ingredientes realmente presentes sin inventar plazos |
| RPC-B10 | `10_Horno/broa_gallega_de_maiz_y_centeno.md` · `REC-561` | RPC-01, RPC-03 y RPC-05 `presente` (harinas, agua separada de escaldado/ajuste, hogaza de ~900 g **orientativa**); RPC-04 `presente` para actividad 35 min, reposos 2–3 h y horno 45–60 min; el **enfriado de al menos 2 h antes del corte**, documentado en Elaboración 7, debe distinguirse del tiempo previo a comer; RPC-07 `presente` como propuesta pendiente | H-RPC-B10: explicitar planificación hasta poder cortar sin sumar automáticamente fases de reposo y horneado como si fueran secuenciales o idénticas en toda ejecución |

Para el resto de observaciones no desarrolladas aquí, **no se registra conformidad implícita**: el propósito es documentar ejemplos prácticos y posibles mejoras trazables, no completar artificialmente noventa juicios binarios. RPC-08 está `desconocido` en los diez casos. RPC-09 no constituye certificación de seguridad alimentaria.

## Dependencias verificadas

- `02_Pastas/espaguetis_a_la_carbonara.md`, encabezados **Descripción** y **Elaboración**, enlaza [Pasta con salsa](../../12_Plantillas/04_Cocciones/pasta_con_salsa.md), cuya sección **Objetivo** se declara patrón, no receta específica, y admite salsas sensibles al calor.
- `02_Pastas/conchiglioni_rellenos_de_atun_y_requeson_al_horno.md`, **Relaciones**, enlaza [Pasta al horno](../../12_Plantillas/04_Cocciones/pasta_al_horno.md), cuya sección **Objetivo** advierte explícitamente que no es una plantilla específica para pasta rellena. La receta de conchiglioni proporciona por sí misma tiempos y pasos.
- `03_Legumbres/garbanzos_con_espinacas.md` y `03_Legumbres/alubias_estofadas.md`, **Relaciones**, enlazan la [plantilla de guiso](../../12_Plantillas/04_Cocciones/guiso_de_legumbres.md); esta separa **legumbres secas** de **legumbres ya cocidas**. Las alubias remiten además a [Cocer legumbres secas](../../00_Bases/03_Tecnicas/cocer_legumbres.md), que diferencia tratamientos por variedad.

## Problemas que se pueden abordar en un piloto RPC-C

Se proponen **cuatro intervenciones concretas**, condicionadas a la revisión de esta evaluación; los otros seis casos se mantienen como controles de no intervención en este corte:

1. **REC-0087 / H-RPC-B07:** hacer explícita la partición de los 850 ml de agua al preparar almíbar; conservar concentración propuesta, rendimiento y libertad de ajuste al gusto.
2. **REC-367 / H-RPC-B02:** precisar que la plantilla de pasta al horno aporta principios genéricos, pero que la formulación de conchiglioni rellenos se rige por su propio montaje y precocción; conservar su estado pendiente de prueba.
3. **REC-0216 / H-RPC-B09:** personalizar la conservación para el bacalao gratinado y eliminar referencias genéricas a huevo y carne que no corresponden.
4. **REC-561 / H-RPC-B10:** distinguir claramente tiempo activo, fermentación/reposos, horneado y **enfriado antes de cortar**, sin atribuir al proceso una duración total única o ejecutada.

`REC-0034` tiene el hallazgo de planificación H-RPC-B04, pero **no exige reescritura**: su tabla ya expresa remojo y cocción por fases con advertencias de variabilidad. Conservar como observación para el diagnóstico posterior. Los otros cinco controles sin cambio son REC-0024, REC-0033, REC-0079, REC-0081 y REC-0092.

**No alterar** ninguna de las diez recetas en esta PR. En caso de que se autorice RPC-C, usar ramas temáticas, revisar las secciones exactas de la fuente antes de cambiarla y mantener variantes superiores, incertidumbre y estados de prueba. La navegación RPC-08 individual se debe contrastar en una PR distinta o dejar pendiente, diferenciando ejecución local de acceso manual público.

## Límites y decisión

- No hay ejecución culinaria nueva, mediciones de tiempos reales, validación organoléptica ni entrevista independiente.
- Las cifras del corpus y tiempo total de RPC-A corresponden a su artefacto anterior, no han sido recalculadas para esta muestra.
- No hay razón para construir filtros de tiempos, normalizar ingredientes o declarar automáticamente recetas «completas» a partir de estos diez casos.
- Esta muestra dirigida no permite calcular tasas de error para los cinco módulos o el recetario entero.

**Decisión propuesta:** aceptar RPC-B como revisión documental dirigida y autorizar solo un **piloto RPC-C limitado a los cuatro ajustes** identificados, manteniendo pruebas de navegación RPC-08 y decisión de producto RPC-D sujetas a verificación y revisión separadas. La última release publicada es `v1.7.0`.


## RPC-C — Piloto de cuatro ajustes editoriales (propuesto en PR independiente)

Las cuatro intervenciones siguientes se prepararon sobre la muestra ya evaluada, **sin alterar los seis controles**:

| Hallazgo RPC-B | ID | Cambio delimitado | Límite |
|---|---|---|---|
| H-RPC-B07 | `REC-0087` | Declarar que 100 ml de agua para disolver azúcar **se descuentan de los 850 ml totales**, dejando 750 ml para mezcla | Mantener 150 ml de zumo, azúcar y ajustes de sabor; no afirmar prueba realizada |
| H-RPC-B02 | `REC-367` | Precisar que la plantilla de pasta al horno es genérica y **no específica de conchiglioni rellenos**, que siguen sus propios pasos | Conservar cantidades, procedimiento y `pendiente de prueba` |
| H-RPC-B09 | `REC-0216` | Acotar conservación a pescado, puerro y lácteos presentes, sin consejos genéricos sobre huevo o carne | No prometer plazos ni validar seguridad real |
| H-RPC-B10 | `REC-561` | Separar fermentación principal, reposo final, horno y **enfriado mínimo antes de cortar**; mantener el templado de escaldado sin duración inferida | No calcular un total único ni declarar tiempos medidos |

El resultado esperado es mayor claridad **documental**, no una demostración de mejora gastronómica. La revisión y fusión de esta PR no cierra automáticamente RPC-C: se debe observar el CI y contrastar después la navegación RPC-08 de diez fichas por separado, o registrar su ausencia. La release publicada permanece en `v1.7.0`.


## RPC-08 — Contraste automatizado propuesto tras la intervención RPC-C

La PR #351 integró cuatro mejoras editoriales en `main`, commit `9151ef5021fefb7247c8ec456aa8e1d877e608e2`, con **Knowledge integrity**, **Knowledge audit** y **Culinary Explorer site** satisfactorios. No se modificaron los seis casos de control ni se registraron nuevas elaboraciones domésticas.

Para revisar individualmente **RPC-08**, una PR de prueba incorpora `tools/check_rpc_b_sample_browser.py` al workflow `Culinary Explorer site`. El test fija los diez IDs RPC-B01–RPC-B10 y, para cada uno, busca el título exacto en Explorer, selecciona **la ruta canónica** (no el primer título coincidente), abre Recipe Assistant, contrasta identidad, ingredientes, pasos, contexto y enlace a fuente, y abre la ficha HTML canónica, con viewport de 390 px y contexto aislado por caso.

La ejecución usa **Chromium sobre un sitio construido y servido localmente**, no comprueba el despliegue de GitHub Pages ni demuestra calidad culinaria. El resultado se recogerá en `rpc-b-sample-browser.json` dentro del artefacto `explorer-browser`.

**Estado de evidencia:** hasta observar un run satisfactorio de esta PR, los diez RPC-08 permanecen `desconocido` en la evaluación previa. No modificar retroactivamente la matriz ni declarar la Unidad RPC-C cerrada antes de observar los resultados y documentar los límites.
