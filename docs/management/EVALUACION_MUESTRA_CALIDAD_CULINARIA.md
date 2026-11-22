---
id: DOC-EVALUACION-MUESTRA-CULINARIA-2026
titulo: Evaluación documental de la muestra culinaria — Unidad B
tipo: gestion
version: 0.1.0
estado: revision-documental-dirigida
ultima_revision: 2026-11-22
---

# Culinary Knowledge Quality Baseline — Unidad B: evaluación documental

## Corte y protocolo

Evaluación sobre las **ocho fichas fijadas antes de revisar sus resultados** en [Muestra editorial](./MUESTRA_EDITORIAL_CALIDAD_CULINARIA.md) (PR #341, merge `52113f0f33b3582ede177f654fd0bef2fb762413`). Se consultaron mediante la integración GitHub los documentos completos en `main`, después de dicho merge, el **22 de noviembre de 2026**. Los documentos no se han modificado. La revisión es humana asistida, **dirigida y documental**, no representa estadísticamente las 590 recetas ni verifica que alguna se haya cocinado recientemente.

Las referencias son a **rutas y encabezados canónicos**; para repetirla se debe fijar el commit de `main` de esta revisión, `52113f0f33b3582ede177f654fd0bef2fb762413`, y contrastar los mismos ocho archivos. No se han obtenido capturas ni se ha ejecutado en esta revisión una navegación nueva en el portal público. En consecuencia, **E07 permanece `desconocido` en los ocho casos**; las pruebas de aceptación pública anteriores acreditan recorridos acotados generales, pero no estas ocho fichas individualmente.

## Matriz por caso y rúbrica

`C` = conforme para la **cuestión documental observada**, no verificación culinaria; `I` = incidencia editorial localizada; `D` = desconocido/no comprobado; `NA` = no aplica. Los ejes E01–E08 se definen íntegramente en el protocolo anterior. Las incidencias no suponen necesariamente que la receta sea imposible de preparar: indican ambigüedad o trabajo de consulta adicional relevante.

| Caso | E01 | E02 | E03 | E04 | E05 | E06 | E07 | E08 | Observación resumida |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| B01 Hamburguesa asiática | C | I | I | C | C | C | D | C | Salsa china referida sin dosis en ingredientes; la elaboración omite criterio operativo de cocción, aunque el bloque doméstico sí exige termómetro |
| B02 Caballa japonesa | C | I | I | C | C | C | D | C | Salsa teriyaki sin proporción ni dosis operativa y pasos sin referencia cuantificada de cocción en el cuerpo |
| B03 Medallones asiáticos | C | I | I | C | C | C | D | I | Ternera o cerdo sin diferenciación suficiente en el procedimiento principal; adaptar salsa por plantilla sin dosis canónica |
| B04 Arroz frito con gambas | C | C | C | C | C | C | D | I | Preparación enlazada a plantilla y evidencia doméstica prudentemente limitada; consejo «recalentar siempre a fuego fuerte» no basta para explicar seguridad de conservación |
| B05 Patatas a la importancia | C | C | C | C | C | C | D | I | Conservación contiene recomendaciones genéricas sobre pescado/carne/arroz ajenas al plato |
| B06 Merluza al horno | C | C | C | C | C | D | D | C | Documento operativo y condicionado por grosor; no se declara elaboración doméstica en el texto examinado |
| B07 Gambas al ajillo | C | C | C | C | C | D | D | C | Opción de guindilla y descongelación claras; no consta prueba doméstica explícita |
| B08 Calamares con kimchi | C | I | I | C | C | C | D | I | Los 30 ml de agua condicionales carecen de instrucción explícita de incorporación; conservación añade un apartado de arroz no relacionado |

**Precisión sobre E06:** `C` significa que el **grado de evidencia se distingue de la formulación** (incluido `pendiente`), no que la elaboración esté verificada. `D` significa que no se puede confirmar desde estas fichas una declaración específica sobre experiencia doméstica. **E08** se refiere a coherencia documental de las precauciones, no a una certificación de seguridad alimentaria.

## Hallazgos localizados y reproducibles

### H-B01 — Receta B01: salsa y procedimiento de hamburguesa

En [`REC-0007`](../../05_Carnes/hamburguesa_asiatica.md), los encabezados **Ingredientes / Salsa** y **Elaboración** remiten a «Salsa china base» y «Añadir la salsa», sin especificar dosis para dos hamburguesas ni un punto de referencia en los pasos principales. El encabezado **Estado de experiencia doméstica** distingue adecuadamente la tanda recordada (una hamburguesa asiática de 200 g) de la formulación de dos unidades, y sí incorpora una advertencia pertinente sobre cocción completa de carne picada. **Mejora candidata:** incorporar una indicación operativa conservadora y una referencia dosificable, manteniendo el enlace a plantilla y sin inventar cantidades históricas.

### H-B02 — Receta B02: glaseado y cocción de caballa

En [`REC-0009`](../../06_Pescados_y_Mariscos/caballa_japonesa.md), **Ingredientes / Salsa** depende de «Salsa teriyaki base» sin cantidad y **Elaboración** pide glasear «durante el último minuto» sin ligar el tiempo real al grosor o al punto comprobado. La ficha sí registra explícitamente una experiencia «muy satisfactoria», pero **no recupera cantidades ni tiempos usados**. **Mejora candidata:** diferenciar dosis propuesta para una futura prueba de la ejecución histórica y añadir criterio de comprobación de cocción apropiado, sin asignarle un tiempo recordado.

### H-B03 — Receta B03: distinta proteína y cocción

En [`REC-0008`](../../05_Carnes/medallones_solomillo_asiaticos.md), **Ingredientes / Proteína** admite ternera o cerdo, pero **Elaboración** indica «hasta alcanzar el punto deseado» para ambos. El bloque **Preparación doméstica planteada: dos medallones** contiene cautelas de seguridad y una propuesta orientativa a 265 g; no equivale a un procedimiento completo ya probado. **Mejora candidata prioritaria:** diferenciar la verificación del tipo de carne en el procedimiento central, sin introducir temperaturas infundadas ni confundir la adaptación propuesta con una prueba real.

### H-B04 — Receta B04: conservación y recalentamiento de arroz

En [`REC-0021`](../../01_Arroces/arroz_frito_gambas.md), **Estado de la receta doméstica / Puntos de reproducción y seguridad** explica correctamente que el arroz está pesado cocido y debe enfriarse rápidamente y mantenerse refrigerado; **Conservación** contiene «Recalentar siempre a fuego fuerte», que aisladamente es insuficiente como orientación de seguridad y puede eclipsar el mensaje anterior de cadena de frío. **Mejora candidata:** alinear el apartado de conservación con el bloque existente, evitando prescripciones absolutas sin comprobación del calentamiento.

### H-B05 — Receta B05: conservación genérica no específica

En [`REC-448`](../../04_Verduras/patatas_a_la_importancia_castellanas.md), **Conservación** incluye párrafos sobre pescado, carne y arroz cocido, mientras los ingredientes de la formulación son patatas, huevo, harina, cebolla, caldo y condimentos. Aunque la prudencia sobre sobras es pertinente, esas referencias no aportan a la ejecución de este plato. **Mejora candidata:** resumir las pautas específicas de sobras del plato sin alterar cantidades o técnica. El **Registro de prueba** permanece honestamente pendiente.

### H-B06 — Receta B06: buen caso de control de alcance

En [`REC-0057`](../../06_Pescados_y_Mariscos/merluza_al_horno_con_limon.md), **Ingredientes**, **Elaboración** y **Puntos críticos** distinguen el descongelado condicional de la presencia del pescado y especifican un intervalo de horno dependiente del grosor. No se detecta en este contraste documental una corrección prioritaria. **No se puede inferir** de ello que la receta haya sido probada o que el horno del propietario produzca ese resultado.

### H-B07 — Receta B07: opcionalidad bien delimitada

En [`REC-0059`](../../06_Pescados_y_Mariscos/gambas_al_ajillo.md), **Ingredientes** marca expresamente la guindilla como opcional y **Elaboración** diferencia la descongelación condicional. Se conserva como segundo control de no intervención: las cantidades y advertencias documentales permiten seguir la propuesta, sin confirmar prueba doméstica.

### H-B08 — Receta B08: agua condicional y conservación ajena

En [`REC-0201`](../../07_Cocina_Asiatica/calamares_salteados_con_kimchi.md), **Ingredientes** menciona «30 ml de agua si fuera necesario», pero **Elaboración** no explica en qué situación ni momento añadirla. **Conservación** añade una referencia a arroz cocido que no aparece en la receta. La ficha declara inequívocamente que es **formulación pendiente de prueba**; la mejora debe respetar esa incertidumbre y evitar fijar proporciones como definitivas.

## Resultado dirigido por eje

| Eje | Conforme | Incidencia | Desconocido | No aplica |
|---|---:|---:|---:|---:|
| E01 Identidad/procedencia | 8 | 0 | 0 | 0 |
| E02 Ingredientes/cantidades | 4 | 4 | 0 | 0 |
| E03 Elaboración/secuencia | 4 | 4 | 0 | 0 |
| E04 Rendimiento/tiempo | 8 | 0 | 0 | 0 |
| E05 Alternativas/condiciones | 8 | 0 | 0 | 0 |
| E06 Grado de verificación | 6 | 0 | 2 | 0 |
| E07 Uso público individual | 0 | 0 | 8 | 0 |
| E08 Precauciones/coherencia | 4 | 4 | 0 | 0 |

Los **denominadores son ocho casos por eje**. Son recuentos de decisión documental, no porcentajes extrapolables al corpus. Las incidencias de E02/E03/E08 se solapan en las mismas fichas. Los juicios de E04 no verifican si los tiempos son correctos en cocina real: solo su identificación documental. No se ha ejecutado un test nuevo de navegador sobre cada caso.

## Propuesta para Unidad C — piloto editorial limitado

Se recomiendan **como máximo seis intervenciones** y dos controles sin cambio:

1. **REC-0008:** clarificar en el procedimiento principal la cocción condicionada por ternera/cerdo y distinguir salsa propuesta.
2. **REC-0007:** incorporar criterio operacional de cocción de carne picada y referencia clara al uso de salsa base, sin atribuir cifras a la preparación histórica.
3. **REC-0009:** explicitar que la dosis de glaseado es orientativa o derivada de plantilla y que la cocción depende del lomo.
4. **REC-0021:** conciliar el consejo de recalentamiento con la conservación segura ya documentada.
5. **REC-448:** retirar referencias de conservación genérica a pescado/carne/arroz que no corresponden a las patatas a la importancia.
6. **REC-0201:** delimitar el uso condicionado del agua y eliminar de conservación el comentario genérico sobre arroz.

**Controles de no modificación:** REC-0057 (merluza) y REC-0059 (gambas). Una futura intervención solo modificará las fichas correspondientes a defectos comprobados, en lotes pequeños, manteniendo variantes, fuentes, estado `pendiente de probar` y formulaciones de referencia. No se inventarán tiempos o cantidades de elaboraciones pasadas.

## Próxima comprobación

Antes de cerrar globalmente la Unidad B, completar **E07** en Explorer y Recipe Assistant sobre los ocho IDs seleccionados o conservar ese eje expresamente como no ejecutado. La presente revisión documental puede aprobarse separadamente de la aceptación de navegación individual; no debe convertir `D` en `C` por existir pruebas públicas sobre otras recetas.

**Versión publicada:** `v1.7.0`. No se autoriza nueva release ni cambio de arquitectura con esta evaluación.
