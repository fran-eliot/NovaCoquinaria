---
id: DOC-EDITORIAL-SIGNALS-CLASSIFICATION-2026
titulo: Clasificación dirigida de las señales editoriales E01–E04
tipo: gestion
version: 0.1.0
estado: evaluacion-documental-dirigida
ultima_revision: 2026-11-22
---

# Clasificación dirigida de señales editoriales E01–E04

## Fuente y alcance

Se ha recuperado **`editorial_signals.json`** del artefacto `knowledge-baseline-c14f14942b9d6b003ff1b895e5a4d2a9f74ddbd4` del [workflow Knowledge audit #45077954952](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/45077954952), ejecutado para [PR #378](https://github.com/fran-eliot/NovaCoquinaria/pull/378). El propio JSON declara `source_commit: c14f14942b9d6b003ff1b895e5a4d2a9f74ddbd4`. Este documento clasifica **las 23 ocurrencias textuales de ese artefacto**, cotejando las diecisiete recetas marcadas en `main` tras la fusión de #378 (`ec439be1354dc661c596ab624a8455ce74ca4262`).

El informe registra **587 fichas exploradas, 17 fichas señaladas y 23 ocurrencias**, con distribución `E01=13`, `E02=2`, `E03=2`, `E04=6`. Algunas líneas activan dos reglas simultáneamente: **23 no equivale a 23 textos independientes ni a 23 defectos culinarios**. El contenido fuente de los hallazgos se contrasta con ingredientes, técnica y uso opcional de componentes.

Las clases siguientes se aplican a **cada coincidencia**, no a la receta completa:

- **I — Improcedente:** el fragmento marcado se refiere exclusivamente a familias de productos que no intervienen en esa preparación.
- **M — Mixta:** la frase contiene alguna recomendación pertinente, pero mezcla categorías, materiales o elaboraciones no presentes. No equivale a un error integral ni autoriza eliminar toda la advertencia.
- **P — Pertinente:** la coincidencia describe un riesgo o ajuste aplicable a la receta. Su detección es un falso positivo respecto del objetivo de señalar contenido fuera de contexto.

## Clasificación de las diecisiete fichas señaladas

| Ruta de receta | Señales y línea del artefacto | Clase | Justificación documental |
|---|---|---|---|
| `03_Legumbres/pochas_navarras_estofadas_con_verduras.md` | E01, E04 · 69 | I, I | Pochas con hortalizas, sin carnes, pescados, huevos o lácteos en ingredientes; cadena de frío aplicable al guiso, enumeración específica ajena |
| `04_Verduras/borrajas_con_patatas_y_aceite_de_oliva.md` | E01, E04 · 64 | I, I | Borrajas, patatas, aceite y ajo opcional; no aparecen las familias animales enumeradas |
| `04_Verduras/menestra_navarra_de_los_cuatro_ases.md` | E01 · 71 | M | La frase incluye «verduras cocidas», pertinente; carnes y pescados no son la fórmula, aunque contiene jamón opcional |
| `04_Verduras/pericana_alicantina_de_pimiento_seco_y_bacalao.md` | E01 · 67 | M | El pescado está realmente presente; la enumeración añade otros ingredientes animales ajenos |
| `04_Verduras/tumbet_mallorquin_de_berenjena_patata_y_pimiento.md` | E01, E04 · 67 | I, I | Tumbet vegetal sin ingredientes animales citados; conviene conservar el aviso de refrigeración del plato cocinado |
| `06_Pescados_y_Mariscos/sopa_de_pescado_vasca_con_sopako.md` | E01 · 73 | M | Pescado y almejas opcionales sí aparecen, pero otras categorías de la lista son irrelevantes |
| `06_Pescados_y_Mariscos/txangurro_a_la_donostiarra_gratinado.md` | E01, E04 · 70 | M, M | Centollo cocido requiere frío; mantequilla opcional puede aportar lácteo, pero la frase abarca familias no utilizadas |
| `07_Cocina_Asiatica/bibimbap_domestico_de_verduras_y_ternera.md` | E01 · 58 | M | Ternera y huevo sí están presentes; gambas no |
| `07_Cocina_Asiatica/curry_japones_de_ternera_y_patata.md` | E01 · 55 | M | Ternera sí está presente; gambas y huevo no figuran como ingredientes principales (revisar roux comercial por alérgenos, cuestión distinta) |
| `07_Cocina_Asiatica/mapo_tofu_de_inspiracion_sichuan.md` | E01 · 58 | M | Carne picada opcional; no contiene gambas ni huevo |
| `07_Cocina_Asiatica/okonomiyaki_de_col_y_cebolleta.md` | E01 · 56 | M | Huevo presente; no hay carnes ni gambas en la formulación |
| `07_Cocina_Asiatica/pad_thai_de_gambas_y_tamarindo.md` | E01 · 58 | M | Gambas y huevo presentes; carne no |
| `09_Bebidas/affogato_de_vainilla_y_espresso.md` | E02, E04 · 62 | M, M | Helado y lácteos son pertinentes, pero fruta cortada y maceraciones con vinagre no pertenecen al affogato |
| `09_Bebidas/limonada_de_jengibre_y_romero.md` | E03 · 59 | P | Infusión de jengibre y romero: extracción prolongada y hierba intensa son causas plausibles de amargor |
| `09_Bebidas/shrub_de_frutos_rojos_y_vinagre_de_manzana.md` | E02, E04 · 64 | M, M | Maceración con vinagre y acidez son pertinentes, pero el helado y los lácteos no forman parte de la receta |
| `09_Bebidas/te_verde_con_menta_estilo_magrebi.md` | E03 · 57 | P | Té verde y menta infusionados: temperatura y extracción prolongada son problemas plausibles y apropiados |
| `10_Horno/huevos_a_la_flamenca_sevillanos.md` | E01 · 71 | M | Huevos, jamón, chorizo y verduras cocidas presentes; pescados y mariscos no |

## Balance de las 23 coincidencias

| Clase | Coincidencias | Interpretación |
|---|---:|---|
| I — Improcedente | **6** | Enumeraciones animales ajenas a tres platos vegetales, con dos reglas sobre la misma línea |
| M — Mixta | **15** | Información parcialmente aplicable combinada con enumeraciones genéricas |
| P — Pertinente | **2** | Señales E03 de diagnóstico real de infusiones; falsos positivos para improcedencia |
| **Total** | **23** | **17 recetas**, **no 23 defectos** |

**Unidad de medida:** una coincidencia regla–línea. Las seis clasificaciones I se concentran en **tres recetas** (pochas, borrajas y tumbet), porque E01 y E04 detectan el mismo texto. No deducir que los 15 casos M exigen sustituir toda la sección; pueden requerir únicamente retirar ejemplos innecesarios y conservar instrucciones válidas.

La distribución por categorías comunicada en el artefacto fue: `03_Legumbres=2`, `04_Verduras=6`, `06_Pescados_y_Mariscos=3`, `07_Cocina_Asiatica=5`, `09_Bebidas=6`, `10_Horno=1` **coincidencias**. Es un balance de reglas, no de recetas por módulo.

## Lecciones para mejorar el detector sin sobreajustarlo

1. **Doble conteo de frases:** E01 y E04 pueden activarse por una misma línea. Un informe de revisión humana debe agrupar ruta+línea, conservando las señales asociadas, antes de estimar incidencias.
2. **Contexto de ingredientes:** una lista amplia puede ser parcialmente pertinente; no establecer incompatibilidades automáticas por la mera ausencia literal de un ingrediente en una línea.
3. **E03 no demuestra error:** ambas coincidencias corresponden a infusiones reales. No elevar el detector a control bloqueante.
4. **Variantes fuera del patrón:** la evaluación anterior documentó falsos negativos, por ejemplo referencias a lácteos en agua de pepino y lavado de frutas y batidora en café bombón. No se ha calculado sensibilidad del corpus.
5. **Seguridad alimentaria:** conservar las advertencias aplicables a refrigeración, cocción y productos opcionales incluso cuando se refine una lista genérica.

## Decisión acotada

Priorizar después un **piloto editorial dirigido** sobre un pequeño grupo de las fichas I/M más evidentes, verificando ingredientes y pasos y sin inventar elaboraciones domésticas. Evitar cambiar las dos fichas P por el mero hecho de estar señaladas. Si se modifica el inventario en otra PR, empezar por eliminar duplicidades de presentación y mejorar el contraste de sección, no por inventar un clasificador semántico de seguridad.

**Esta PR es exclusivamente documental:** no modifica recetas, reglas, scripts ni validadores, no publica release y no altera la autoridad del Markdown canónico.
