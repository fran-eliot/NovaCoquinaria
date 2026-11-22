---
id: DOC-CIERRE-PILOTO-CALIDAD-CULINARIA-2026
titulo: Cierre del piloto editorial de calidad culinaria — Unidad C
tipo: gestion
version: 0.1.0
estado: cierre-tecnico-acotado
ultima_revision: 2026-11-22
---

# Cierre del piloto editorial — Culinary Knowledge Quality Baseline, Unidad C

## Decisión y ámbito

**Complete — Bounded Editorial & Local Browser Validation.** Se cierra el piloto de intervención editorial de seis fichas, con evaluación documental previa de una muestra fija de ocho y contraste automatizado dirigido de los recorridos individuales en Explorer y Recipe Assistant. Este cierre **no prueba** mejores resultados al cocinar, auditoría general de seguridad, una aceptación manual nueva del sitio público ni la calidad representativa de las 590 recetas.

El estado previo a las correcciones quedó fijado en [muestra y rúbrica](./MUESTRA_EDITORIAL_CALIDAD_CULINARIA.md) y [evaluación inicial](./EVALUACION_MUESTRA_CALIDAD_CULINARIA.md). La línea base [Unidad A](./LINEA_BASE_CALIDAD_CULINARIA.md) contiene indicadores de extracción en su propio SHA y con sus denominadores; **no se puede interpretar la corrección de seis recetas como mejora demostrada del corpus completo**.

## Evidencia de integración

| PR | Capacidad o modificación | Evidencia |
|---|---|---|
| [#343](https://github.com/fran-eliot/NovaCoquinaria/pull/343) | Correcciones de conservación y condiciones en REC-0021, REC-448 y REC-0201 | Merge `cdc92e7e31ce26d24ac1f328af978eff200af1e3`; workflows de PR satisfactorios |
| [#344](https://github.com/fran-eliot/NovaCoquinaria/pull/344) | Salsas y criterios de cocción en REC-0007, REC-0009 y REC-0008 | Merge `87d5429935924fdfd3e36d49069d51f1e6bca497`; workflows de PR satisfactorios |
| [#345](https://github.com/fran-eliot/NovaCoquinaria/pull/345) | Test E07 en Chromium para B01–B08 y navegación por ruta canónica | Merge `349633c6e779a50c2064af5dcff292be06fd2ade`; tres workflows de PR satisfactorios |

### Contraste E07 observado

El [workflow Culinary Explorer site #156](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/45050476144) finalizó `success` sobre el head `31baa44ca22835c986de77fbccf54e6f08e674ae` de PR #345. El log del job `137294250325` registra `stage: editorial_sample_e07_local_browser`, `source_commit: 54c3dad55bef06561bc15375c81ba2b7e160b832`, `sample_count: 8` y `passed: true`. El artefacto `explorer-browser` incluye `quality-sample-browser.json`.

Los ocho casos B01–B08 pasaron el enlace **Explorer → Recipe Assistant → ficha canónica**, con búsqueda por título seguida de identificación de ruta, comprobación de ingredientes, pasos, contexto y enlace de fuente, sin errores JavaScript registrados en viewport de 390 px. Se usaron contextos de navegador aislados y servidor local sobre el sitio construido. **La prueba no verificó el despliegue remoto de GitHub Pages ni entrevistó a usuarios.**

Este resultado convierte E07 de «no ejecutado» en **recorrido automatizado local conforme para los ocho casos**, no en aceptación pública individual. La matriz histórica de evaluación inicial no se reescribe para preservar la situación anterior a E07.

## Contraste antes/después con el mismo alcance

| Criterio | Antes, evaluación documental B01–B08 | Después, evidencia disponible | Interpretación |
|---|---|---|---|
| Ambigüedad de salsa en hamburguesa, caballa y medallones | H-B01–H-B03 | Se incorpora enlace a plantilla y uso gradual; distinción de salsa propuesta e histórica | Corrección editorial incorporada, no resultado organoléptico verificado |
| Diferenciación de proteína y cocción | H-B03 | La elaboración distingue cerdo de ternera y exige verificación apropiada | Mejora de claridad, no certificación alimentaria |
| Consejos de conservación ajenos al plato | H-B04, H-B05, H-B08 | Arroz, patatas y calamares tienen instrucciones enfocadas a la preparación correspondiente | Mejor coherencia documental; no se midió conservación real |
| Agua condicional en calamares | H-B08 | Se explicita cuándo introducir hasta 30 ml como ajuste todavía no probado | Ambigüedad de secuencia tratada, no experimentación real |
| Recorridos individuales E07 | 8 desconocidos/no ejecutados | 8/8 correctos en Chromium local, CI #156 | Cobertura funcional dirigida, no aceptación pública |
| Controles sin cambio | REC-0057 y REC-0059 | Se mantienen sin intervención | Controles de no reescritura innecesaria |
| Evidencia doméstica y variantes | No verificable o registrada según ficha | No se promovió ninguna receta a probada ni se sustituyeron variantes | Se preservan límites de procedencia |

No se calculan porcentajes generales de calidad del recetario a partir de esta muestra. Los 6/6 hallazgos de intervención abordados significan **seis correcciones editoriales implementadas**, no que todas las fichas sean completas o seguras para cocinar.

## Deuda y riesgos aún abiertos

- Exactitud práctica de tiempos, proporciones y cocción en recetas pendientes de prueba: requiere una elaboración doméstica y anotación posterior del propietario.
- E07 pública/manual sobre estas ocho fichas: no ejecutada de nuevo en esta fase; existe aceptación pública general anterior, que no debe equipararse con esta muestra.
- Identidades explícitas de ingredientes y candidatos: cobertura semántica insuficiente para recomendar cocinabilidad o disponibilidad automática.
- Evaluación editorial de otros dominios y detección de variantes duplicadas: queda fuera de esta muestra dirigida.
- El estado `prepared`, `pending` o `unknown` en la proyección no equivale a un inventario probado de experiencias reales.

## Transición propuesta a Unidad D

Conservar la documentación y pruebas como evidencia del piloto y realizar una **decisión estratégica breve** sobre qué capacidad ofrece más valor, contrastando utilidad del recetario, tiempos/raciones, evidencia doméstica y deuda semántica, antes de abrir funcionalidades nuevas. La Unidad D no queda aprobada de modo automático por este cierre.

Markdown continúa siendo canónico. El propietario mantiene la revisión y fusión de PR. La release vigente es `v1.7.0`; este cierre no autoriza otra publicación.
