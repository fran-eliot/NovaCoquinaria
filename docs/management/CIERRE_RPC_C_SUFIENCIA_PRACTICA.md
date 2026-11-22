---
id: DOC-RPC-C-CIERRE-2026
titulo: Recipe Practical Completeness — cierre técnico acotado de RPC-C
tipo: gestion
version: 0.1.0
estado: cierre-tecnico-acotado
ultima_revision: 2026-11-22
---

# Recipe Practical Completeness — RPC-C: cierre técnico acotado

## Decisión

**Complete — Bounded Editorial & Local Browser Validation.** Se documenta el cierre técnico del piloto RPC-C sobre **cuatro intervenciones editoriales** en una muestra previamente fijada de diez recetas, junto con **diez recorridos dirigidos de navegador** verificados en Chromium sobre el sitio construido localmente.

La conclusión se limita a **claridad documental y navegación dirigida**. No acredita que las recetas se hayan cocinado nuevamente, que sus tiempos o cantidades hayan sido comprobados en una cocina real, que las 590 recetas sean reproducibles o seguras, ni que se haya efectuado aceptación manual pública de esta muestra.

## Cadena de evidencia y cortes

| Elemento | Fuente y corte | Evidencia que aporta |
|---|---|---|
| Contrato RPC-A | [Diagnóstico](./DIAGNOSTICO_RECIPE_PRACTICAL_COMPLETENESS.md), PR #348 | Nueve ejes y cinco estados sin clasificar automáticamente cocinabilidad |
| Selección RPC-B | [Muestra predefinida](./MUESTRA_RPC_B_SUFIENCIA_PRACTICA.md), PR #349, merge `bd8f5f54450db40f204eedbdb08ba8fd15f17722` | Diez casos fijados **antes** de la evaluación |
| Evaluación RPC-B | [Evaluación documental](./EVALUACION_RPC_B_SUFIENCIA_PRACTICA.md), PR #350, merge `3c7334d798260f7793c7b94446d7c3e68e195b20` | Cuatro hallazgos priorizados y seis controles sin intervención |
| Intervención RPC-C | [PR #351](https://github.com/fran-eliot/NovaCoquinaria/pull/351), merge `9151ef5021fefb7247c8ec456aa8e1d877e608e2` | Cuatro fichas corregidas; los tres workflows de PR en `success` |
| Navegación RPC-08 | [PR #352](https://github.com/fran-eliot/NovaCoquinaria/pull/352), merge `92164e8274c1b2f611a66671c1d0729d8903a497` | Diez recorridos individuales; tres workflows de PR en `success` |

### Evidencia RPC-08 observada

El [workflow Culinary Explorer site #170](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/45053932903), job `137304910133`, finalizó en `success`. Su salida documenta `stage: rpc_b_sample_rpc08_local_browser`, **`source_commit: 2a20dbcdb494436122402afbf79118ffc5f02b40`**, `sample_count: 10`, `passed: true`, y los diez casos RPC-B01–RPC-B10 individualmente correctos. El artefacto `explorer-browser` contiene el informe `rpc-b-sample-browser.json`.

El script `tools/check_rpc_b_sample_browser.py` realiza búsqueda por título exacto, selección por ruta canónica para evitar colisiones de títulos, enlace «Preparar receta», comprobación de título, ingredientes, pasos y contexto, y apertura de la fuente original sin errores JavaScript observados en Chromium con viewport de 390 px. Se usan contextos separados por caso y un servidor temporal local. Este **source_commit es el snapshot de la construcción en CI**, distinto del merge posterior. El resultado no certifica GitHub Pages ni aceptación manual.

La anotación histórica RPC-08 «desconocido» del protocolo y evaluación previa es correcta **en el momento en que se redactaron**; aquí se incorpora un resultado posterior de validación automatizada, sin reescribir aquella evidencia.

## Contraste antes/después del mismo piloto

| Hallazgo fijado en RPC-B | Receta | Antes | Después, cambio integrado |
|---|---|---|---|
| H-RPC-B07 | `REC-0087` · Limonada | 100 ml de agua para el azúcar sin aclarar si pertenecían a los 850 ml totales | Ahora se declara **100 + 750 ml como partición del total de 850 ml**; sin cambiar el rendimiento ni afirmar prueba doméstica |
| H-RPC-B02 | `REC-367` · Conchiglioni | Referencia a plantilla general cuyo contrato no es específico de pasta rellena | Ahora se delimita su uso a criterios genéricos y prevalecen los pasos propios de las conchas |
| H-RPC-B09 | `REC-0216` · Bacalao gratinado | Conservación genérica con referencias a huevo/carne ajenos al plato | Ahora se refiere al pescado y los lácteos empleados, sin plazos inventados |
| H-RPC-B10 | `REC-561` · Broa | Resumen temporal sin distinguir enfriado mínimo antes de cortar | Ahora se separan fermentación, reposo, horno y enfriado, sin inferir un tiempo total único |

**Controles preservados:** `REC-0024`, `REC-0033`, `REC-0034`, `REC-0079`, `REC-0081` y `REC-0092` no se reescribieron. El hallazgo de planificación de `REC-0034` se conserva como observación sin exigir una corrección. Las recetas propuestas siguen pendientes de prueba y la historia doméstica del pastel de manzana conserva el resultado negativo del lemon curd diluido, sin promocionar la cobertura de mermelada a «probada».

**Interpretación válida:** se han tratado 4/4 hallazgos seleccionados para intervención y se han ejecutado 10/10 recorridos locales. Estas fracciones **no son tasas de calidad del recetario**, ni demuestran resultados gastronómicos mejores en uso real.

## Deuda conservada

- **RPC-08 público/manual:** no se ha repetido en GitHub Pages sobre los diez casos; los recorridos locales prueban otro alcance.
- **Pruebas culinarias personales:** no se han realizado para verificar las cuatro fichas corregidas; tiempos y formulaciones orientativos deben seguir identificándose como tales.
- **Suficiencia del resto del corpus:** fuera de esta muestra dirigida. No cabe extrapolar el resultado a los diez módulos o las 590 recetas.
- **Semántica y planificación:** la identificación de ingredientes, la definición de tiempos totales y los estados de preparación del extractor continúan sujetos a límites. No procede declarar cocinabilidad ni disponibilidad desde Pantry.
- **Rendimiento funcional:** la verificación de que se puede navegar una receta no prueba que sea posible cocinarla con exactitud ni que sus cantidades sean suficientes.

## Transición hacia RPC-D

La siguiente decisión debe ser **de producto y arquitectura**, no la construcción automática de nuevas funciones. Contrastar tres direcciones: (A) aumentar utilidad editorial de recetas y técnicas, (B) mostrar exclusivamente datos explícitos y fiables en Explorer/Assistant, (C) investigar semántica de ingredientes y tiempos en casos concretos. Evaluar coste, beneficio, incertidumbre y puertas de abstención antes de autorizar desarrollo.

La **Unidad RPC-D no queda autorizada automáticamente** por este cierre. No se crea release, milestone, backend, sistema de recomendaciones ni etiquetas globales de «receta completa». La fuente canónica continúa siendo Markdown; cada nuevo trabajo deberá avanzar por rama y PR revisada por el propietario. La versión publicada permanece en `v1.7.0`.
