---
id: DOC-EDITORIAL-SIGNALS-EVALUATION-2026
titulo: Primera evaluación dirigida de señales editoriales
tipo: gestion
version: 0.1.0
estado: evaluacion-dirigida
ultima_revision: 2026-11-22
---

# Primera evaluación dirigida de señales editoriales

## Fuente comprobada y resultado

La primera ejecución satisfactoria del inventario se realizó en [Knowledge audit — workflow #45076880787](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/45076880787), job `137375984026`, sobre la PR #377 y su commit `d883f6b2321be4197cc9da20629942454cdbe663`. Los tres workflows de la PR finalizaron correctamente; la PR está fusionada en `c83e98524a7f204c4ed1b9040cb40ea4b1d14d40`.

La salida del job aporta la evidencia siguiente:

| Medida | Resultado | Interpretación |
|---|---:|---|
| Fichas exploradas | 587 | Rutas canónicas encontradas por ese ejecutable en ese checkout |
| Fichas con una o más señales | 17 | Candidatas para inspección, **no defectos confirmados** |
| Coincidencias | 23 | Ocurrencias; una misma ficha puede contribuir varias |
| Workflows de PR | 3/3 correctos | Ejecución correcta, **no validación editorial de las coincidencias** |

**No comparar directamente 587 con las 590 fichas del corte histórico de `LINEA_BASE_CALIDAD_CULINARIA.md` sin reconciliar inventario y commit.** Tampoco atribuir a `main` posterior estas cifras sin volver a generar el informe. La distribución E01–E04 y las 17 rutas se encuentran en el artefacto `knowledge-baseline-4eb4f116f088e4a4149d7a61444dc0498584b7cf`, dentro de `editorial_signals.json`; este documento no inventa esa distribución.

## Muestra dirigida de control — 12 fichas

Se consultaron en `main` tras el merge de la PR #377. Se aplicó el **mismo conjunto de fragmentos E01–E04** sobre los apartados `## Puntos críticos`, `## Diagnóstico` y `## Conservación`. Esta selección intencionada combina módulos, recetas ya revisadas y formatos editoriales diferentes: **no es una muestra aleatoria ni representativa**.

| Ruta | Resultado de señales | Observación editorial dirigida |
|---|---|---|
| `10_Horno/falafel_de_garbanzos_remojados_al_horno.md` | 0 | Control sin coincidencias; no calificado como correcto por ese motivo |
| `10_Horno/ensaimada_mallorquina_lisa_de_manteca.md` | 0 | Control sin coincidencias |
| `10_Horno/merluza_al_horno_con_verduras.md` | 0 | Control sin coincidencias |
| `02_Pastas/ensalada_de_pasta_con_atun_y_verduras.md` | 0 | Control sin coincidencias |
| `01_Arroces/arroz_caldoso_de_bogavante.md` | 0 | Control sin coincidencias |
| `04_Verduras/berenjenas_rellenas_de_garbanzos_y_tomate.md` | 0 | Control sin coincidencias |
| `08_Postres/crema_catalana_con_canela_y_limon.md` | 0 | Control sin coincidencias |
| `05_Carnes/cerdo_al_mojo_citrico_con_ajo.md` | 0 | Su apartado `Diagnóstico y ajustes` no está incluido en las secciones reconocidas; **no inferir cobertura** |
| `09_Bebidas/agua_de_pepino_lima_y_menta.md` | 0 | La conservación contiene «especialmente si contiene fruta cortada o lácteos»; menciona lácteos que no figuran en esta bebida: **candidato de revisión no detectado** |
| `09_Bebidas/cafe_bombon_con_leche_condensada.md` | 0 | En puntos críticos figura «lavar la fruta e higienizar batidora» aunque la receta monta espresso y leche condensada: **candidato de revisión no detectado** |
| `08_Postres/bizcocho_de_yogur.md` | 0 | Control con diagnóstico de horneado específico |
| `07_Cocina_Asiatica/doenjang_jjigae_de_tofu_y_calabacin.md` | 0 | Control con diagnóstico de guiso y tofu específico |

**Resultado acotado:** 0/12 fichas de la muestra activa alguna señal E01–E04; al menos **2/12 contienen expresiones ajenas a sus ingredientes o utensilios** constatables en el Markdown. Estas dos observaciones no se convierten automáticamente en defectos corregidos. El control demuestra un vacío de **cobertura**, pero no permite calcular sensibilidad o precisión del detector en el corpus. El recuento de 23 coincidencias del CI corresponde a otras fichas y requiere examinar el JSON antes de calificar positivos como correctos o falsos positivos.

## Interpretación y límites

1. **La ejecución funciona:** salida reproducible asociada al commit, sin bloquear CI por coincidencias.
2. **Una señal no es un defecto:** 23 coincidencias son candidatos textuales; ninguna puede clasificarse como error sin revisar ingredientes, pasos y contexto.
3. **Una ausencia tampoco es aprobación:** el detector no cubre variantes de títulos (`Diagnóstico y ajustes`), ni todas las referencias a productos inexistentes, utensilios o métodos.
4. **No adaptar reglas solo a los ejemplos:** ampliar términos por dos falsos negativos seleccionados produciría riesgo de sobreajuste; antes hacen falta ejemplos positivos del JSON y contraejemplos reales que reduzcan falsos positivos.
5. **No autoeditar las recetas:** preservar las preparaciones probadas, procedencia, cantidades, tiempos y variantes.

## Siguiente decisión recomendada

Realizar un **muestreo de las 17 fichas marcadas** desde el JSON del artefacto, clasificando manualmente cada ocurrencia como `pertinente`, `improcedente` o `indeterminada`, con su evidencia y razón. Añadir una pequeña muestra de controles negativos de otros módulos. Solo entonces decidir si merece la pena ajustar reglas, reconocer otros encabezados o incorporar un segundo detector. Mantener esas decisiones en PR separadas; no publicar release ni activar un quality gate.

Esta evaluación **no cambia las recetas ni los validadores** y no supone aprobar automáticamente una siguiente fase.
