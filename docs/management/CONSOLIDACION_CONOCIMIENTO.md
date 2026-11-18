---
id: DOC-CONSOLIDACION-CONOCIMIENTO-2026
titulo: Consolidación del conocimiento culinario
tipo: gestion
version: 1.11.0
estado: borrador
ultima_revision: 2026-11-18
---

# Consolidación del conocimiento culinario

## Objetivo

Establecer un procedimiento incremental para revisar integridad, navegación y reutilización del conocimiento culinario tras la expansión de los módulos. Este documento describe un **plan de revisión**, no certifica que el repositorio completo haya superado una auditoría.

## Alcance

- Integridad de enlaces Markdown internos.
- Unicidad y coherencia de identificadores.
- Front Matter conforme al modelo vigente.
- Navegación entre índices de módulos, recetas, técnicas, ingredientes y tablas.
- Detección de duplicidades y referencias a documentos todavía no creados.
- Distinción entre recetas documentadas y recetas probadas en cocina.

## Herramientas existentes

| Control | Herramienta |
|---|---|
| Validación conjunta | `python tools/validate_all.py` |
| Front Matter | `tools/validate_frontmatter.py` |
| Identificadores | `tools/validate_ids.py` |
| Enlaces internos | `tools/validate_links.py` |

La existencia de estos validadores está confirmada en el repositorio. **Su ejecución y resultado no se han verificado en esta revisión**.

## Primer hallazgo confirmado

Durante una revisión dirigida de referencias del módulo Cocina Asiática se detectó un enlace a `11_Despensa/09_Salsas/hoisin.md` sin documento de destino en `main` antes de este incremento. Se incorpora una ficha de ingrediente con ID `ING-0041` para cubrir esa referencia.

No se extrapola este hallazgo a un número total de enlaces rotos del repositorio.

## Revisión dirigida de navegación — 2026-11-14

Se realizó una comprobación de existencia de destinos Markdown sobre una **muestra de 36 referencias** en los índices de módulos:

| Documento de origen | Referencias comprobadas | Destinos ausentes |
|---|---:|---:|
| `02_Pastas/README.md` | 12 | 0 |
| `07_Cocina_Asiatica/README.md` | 24 | 0 |
| **Total de la muestra** | **36** | **0** |

**Método:** lectura de los enlaces relativos Markdown y consulta de existencia de los archivos de destino en la rama `main` mediante GitHub. En Pastas se revisaron las primeras 12 referencias Markdown; en Cocina Asiática se revisaron las referencias 13 a 36 según su orden de aparición. No se validaron anclas, contenido semántico de los destinos ni el conjunto completo de archivos.

**Resultado:** no se encontraron destinos ausentes **en la muestra indicada**. Esto no acredita la integridad global del repositorio ni sustituye `python tools/validate_all.py`.

### Coherencia semántica detectada

La ficha `11_Despensa/09_Salsas/miso.md` describía como futuras la sopa de miso y la berenjena glaseada, aunque ya existen como `REC-0072` y `REC-0075`. Se actualiza la ficha para enlazar esas recetas y `REC-0076` (pollo glaseado con miso), manteniendo separadas las preparaciones todavía no documentadas.

## Integración continua de la integridad documental

El workflow [Knowledge integrity](../../.github/workflows/knowledge-integrity.yml) ejecuta `python tools/validate_all.py` en pull requests, cambios a `main` y mediante activación manual. Instala la dependencia PyYAML necesaria para los validadores existentes.

El job `Validate Markdown knowledge` falla si cualquiera de los tres controles devuelve un código distinto de cero. Los mensajes de los validadores quedan disponibles en el registro de ejecución de GitHub Actions.

**Estado de ejecución:** la incorporación del workflow no demuestra que el repositorio supere los controles. El resultado real debe consultarse en GitHub Actions tras ejecutarse. Para exigir este control antes de fusionar, se debe configurar como comprobación requerida en la protección de la rama.

## Auditoría de relaciones y conocimiento huérfano

Además de la integridad estructural, el workflow incorpora dos diagnósticos de calidad del grafo:

- `python tools/validate_semantics.py`: identifica recetas, técnicas y plantillas sin las relaciones de salida esperadas, según las reglas de `tools/semantic_rules.py`.
- `python tools/find_orphans.py`: informa de nodos sin referencias entrantes o salientes, excluyendo los tipos expresamente ignorados por el script.

Ambos scripts **devuelven actualmente código de salida 0 incluso si detectan advertencias o huérfanos**. Por tanto, su incorporación al workflow ofrece visibilidad, pero **no constituye una comprobación bloqueante** de calidad semántica. La lista real de hallazgos deberá revisarse en los registros del job, sin considerar automáticamente errónea una ficha por aparecer como huérfana.

La validación estructural de Front Matter, IDs y enlaces permanece como control bloqueante.

## Primer lote de relaciones semánticas — 2026-11-14

La ejecución [Knowledge integrity #8](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/43624315630) finalizó correctamente en los controles estructurales e informó de **11 advertencias semánticas** y **18 documentos huérfanos**. Los diagnósticos son informativos, no bloqueantes.

Se incorporan referencias de utilidad culinaria verificable en **nueve documentos**: cuatro recetas de Postres y Bebidas, y cinco técnicas de horno, repostería, infusiones y cocina asiática. Los destinos enlazados ya existen y se corresponden con tablas de diagnóstico o fichas de ingredientes pertinentes.

Quedan pendientes de análisis las advertencias sobre `REC-0001` (arroz chaufa) y `TEC-0007` (emulsión de salsa para pasta), así como los documentos huérfanos. **No se presupone un nuevo recuento de advertencias** hasta ejecutar los diagnósticos sobre este lote; la ausencia de referencias no siempre indica un defecto culinario.

## Cierre propuesto de las advertencias semánticas — 2026-11-14

La ejecución [Knowledge integrity #10](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/43624723791) confirma que las advertencias semánticas se redujeron de 11 a **2**, manteniendo **18 documentos huérfanos**. Los controles estructurales finalizaron correctamente.

Este incremento atiende los dos hallazgos restantes:

- `REC-0001` (arroz chaufa): se sustituye la referencia textual obsoleta `PLA-0008` por el enlace a la plantilla vigente `PLA-0015` (arroz frito base) y se enlaza la técnica de wok.
- `TEC-0007` (emulsionar salsa para pasta): se enlaza la ficha de pasta seca, pertinente para el comportamiento del almidón durante el ligado de la salsa.

**Resultado pendiente de verificar:** se espera que ambas relaciones sean reconocidas por el grafo, pero el número final de advertencias se determinará mediante una nueva ejecución de GitHub Actions. Los documentos huérfanos requieren un trabajo de navegación separado; no se consideran resueltos por este cambio.

## Navegación de documentos sin referencias entrantes — 2026-11-14

La ejecución [Knowledge integrity #12](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/43625192175) terminó con **0 advertencias semánticas** y **18 nodos sin referencias entrantes**. El detector considera documentos con Front Matter y enlaces entre ellos; por ello, una referencia desde el README principal sin Front Matter no siempre queda representada en el grafo.

Se incorpora el [índice transversal de navegación](./INDICE_NAVEGACION_CONOCIMIENTO.md), que agrupa los 18 documentos identificados por finalidad: módulos, plantilla, gestión, gobernanza y especificaciones. El índice permite descubrir contenido y ofrece un punto de partida para revisar su vigencia. **Una reducción del recuento de huérfanos tras enlazarlos no debe interpretarse como una mejora automática de la calidad semántica**; las relaciones de uso real siguen siendo objeto de revisión.

## Cierre propuesto de la navegación transversal — 2026-11-14

La ejecución [Knowledge integrity #15](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/43625793942) confirma **0 advertencias semánticas** y **1 documento sin referencias entrantes**. Los controles estructurales terminaron correctamente.

El único nodo pendiente, `GOV-0000`, corresponde al modelo de gobernanza y se encuentra en `docs/governance/GOBERNANCE_MODEL.md`. Se incorpora su enlace en el índice transversal para completar la navegación de los 18 documentos originalmente identificados.

**Pendiente de confirmación:** el resultado de `find_orphans.py` después de esta corrección. La conectividad del grafo no sustituye una revisión editorial de vigencia, exactitud y utilidad de los documentos.

## Primera revisión editorial dirigida: arroz frito — 2026-11-14

La ejecución [Knowledge integrity #17](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/43625994952) confirma **0 advertencias semánticas y 0 documentos huérfanos**. Esto cierra los hallazgos de conectividad del grafo según las reglas actuales, no la auditoría de calidad culinaria.

Se inicia una revisión editorial acotada a la receta [arroz chaufa](../../01_Arroces/arroz_chaufa.md) y la [plantilla de arroz frito](../../12_Plantillas/05_Arroces/arroz_frito_base.md):

- **Seguridad:** sustituir instrucciones ambiguas sobre arroz «del día anterior», recalentado «únicamente a fuego fuerte» y congelación por indicaciones basadas en enfriado rápido, refrigeración, cocción suficiente y control del historial térmico.
- **Coherencia:** hacer explícito el retorno del huevo y la cocción completa del cerdo en el chaufa.
- **Reutilización:** enlazar recetas derivadas existentes y distinguirlas de variantes todavía no documentadas.

**Límite:** revisión documental y de consistencia, sin ensayo culinario presencial, medición de temperaturas ni validación microbiológica. No se atribuye a estas dos fichas una certificación general de seguridad alimentaria.

## Segunda revisión editorial dirigida: postres con huevo y lácteos — 2026-11-14

Se revisan documentalmente tres recetas: [flan de huevo](../../08_Postres/flan_de_huevo.md), [natillas](../../08_Postres/natillas_caseras.md) y [tarta de queso al horno](../../08_Postres/tarta_de_queso_al_horno.md).

Los ajustes se centran en distinguir las señales de textura (temblor, espesado) de la comprobación de cocción suficiente, reducir ambigüedades sobre enfriado y refrigeración, y evitar reposos prolongados fuera de frío. Se mantienen ingredientes, proporciones y tiempos orientativos, sujetos a las condiciones reales de elaboración.

**Alcance:** revisión editorial de tres documentos, sin ensayo de cocina, análisis microbiológico ni certificación de seguridad. La auditoría de integridad documental debe volver a ejecutarse tras estos cambios.

## Procedimiento recomendado

1. Ejecutar la validación conjunta sobre el árbol completo del repositorio.
2. Registrar los errores con ruta de origen, destino esperado y categoría.
3. Corregir primero los enlaces internos rotos y las colisiones de identificadores.
4. Revisar índices de módulos y navegación desde el README principal.
5. Identificar contenido duplicado y establecer un documento de autoridad.
6. Revisar la relación entre recetas, técnicas, ingredientes y tablas.
7. Repetir validaciones tras cada lote de correcciones.
8. Separar el resultado de validación estructural de cualquier afirmación sobre pruebas culinarias.

## Criterios de cierre

- Validación automática ejecutada y sin errores, o excepciones documentadas.
- Índices de módulos accesibles desde el punto de entrada.
- Referencias internas relevantes verificadas.
- Hallazgos pendientes registrados con prioridad y responsable.
- Ningún contenido marcado como probado sin evidencia de elaboración.

## Relación con otros documentos

- [Estado del proyecto](./PROJECT_STATUS.md)
- [Roadmap](./ROADMAP.md)
- [README principal](../../README.md)

## Principio de NovaCoquinaria

> La consolidación transforma una colección creciente en conocimiento navegable, verificable y reutilizable.

## Propuesta de transición a consolidación y explotación — 2026-11-18

**Estado:** dirección de trabajo incorporada a la documentación de gestión mediante la presente transición. No declara cerrada la evolución del conocimiento ni selecciona tecnología.

### Línea base comprobada

Corte: [merge de la PR #193](https://github.com/fran-eliot/NovaCoquinaria/pull/193), commit [`64a3fd2660c4f817e063157ac332d3dc42a6d7d7`](https://github.com/fran-eliot/NovaCoquinaria/commit/64a3fd2660c4f817e063157ac332d3dc42a6d7d7). Knowledge integrity y Deploy MkDocs site finalizaron con éxito; no había PR abiertas en la consulta previa a esta propuesta.

| Indicador | Inventario |
|---|---:|
| Archivos Markdown | 922 |
| Fichas de recetas (diez módulos, sin README) | 590 |
| Fichas de ingredientes (sin README ni BACKLOG) | 125 |
| Documentos de técnicas (sin README) | 52 |
| Serie de cocina española | 174 fichas en 29 tandas |

Distribución de recetas: Arroces 39, Pastas 37, Legumbres 61, Verduras 86, Carnes 82, Pescados y Mariscos 69, Cocina Asiática 44, Postres 82, Bebidas 36, Horno 54. Los recuentos por rutas no acreditan unicidad semántica ni elaboración culinaria. La release vigente documentada es v1.5.0; este incremento no publica una versión.

### Justificación

La [visión](../VISION.md) y la [estrategia del conocimiento](../governance/KNOWLEDGE_STRATEGY.md) priorizan calidad, reutilización y conectividad sobre volumen. Existe una masa documental suficiente para explorar capacidades de consumo sin exigir que cada receta esté probada. El [informe de auditoría generado](./generated/KNOWLEDGE_AUDIT.md) conserva fecha de 2026-08-03; no debe interpretarse como medición actual de madurez. El código de auditoría requiere revisar la cobertura de los diez módulos, las convenciones recientes y los niveles de asociación antes de interpretar resultados.

### Incrementos candidatos

| Incremento | Resultado esperado | Condición de aceptación propuesta |
|---|---|---|
| 1. Línea base de calidad | Auditoría reproducible del inventario y relaciones | Identificar commit, alcance, exclusiones, controles estructurales y diagnósticos; distinguir resultados de inferencias |
| 2. Contrato de datos de recetas | Campos y normalización para consumo | Muestra representativa de módulos y formatos; preservar ID original, procedencia, estado editorial, cantidades y unidades desconocidas sin inventarlas |
| 3. Prototipo de ingesta e indexación | Representación derivada consultable | Repetir la ingesta sin duplicar registros, mantener trazabilidad a Markdown, registrar errores y casos no interpretados |
| 4. Consulta de conocimiento | Primer servicio de búsqueda por ingredientes y metadatos | Casos de consulta reproducibles, fuentes enlazadas y distinción de propuestas y elaboraciones verificadas |
| 5. Evaluación de plataforma | Decisión fundamentada sobre API, persistencia e interfaz | Demostrar utilidad del prototipo y documentar alternativas antes de seleccionar tecnologías o diseñar funcionalidades de mayor alcance |

Los incrementos se apoyan en la [especificación de ingesta](../specifications/ingestion/ESPECIFICACION_DE_INGESTA.md), el [modelo de conocimiento](../architecture/MODELO_DE_CONOCIMIENTO.md) y el [Roadmap](./ROADMAP.md). No implican adoptar una base de datos concreta ni implementar un Runtime completo.

### Principios de continuidad

- Markdown sigue siendo fuente de verdad; cualquier índice o persistencia de consulta es derivado y reconstruible.
- La incorporación de recetas continúa a demanda, por experiencia doméstica, carencias de cobertura o valor de reutilización, en lugar de perseguir un objetivo numérico.
- Las diferencias entre propuestas, elaboraciones, valoraciones y antecedentes se conservan; los datos ausentes no se completan sin evidencia.
- La auditoría automática no sustituye revisión editorial, semántica ni pruebas culinarias.
- No es objetivo inmediato elegir frameworks, implantar GraphRAG, agentes o un planificador completo.

### Alcance de la transición

PROJECT_STATUS, ROADMAP, BITACORA y el kit de continuidad se actualizan de forma coordinada para orientar el primer incremento de auditoría. La adopción de esta dirección no equivale a aprobar una tecnología, release o implementación concreta. Los resultados de la auditoría todavía no se han obtenido.

## Línea base reproducible: infraestructura de auditoría — 2026-11-18

Se incorpora un workflow de auditoría independiente, [Knowledge audit](../../.github/workflows/knowledge-audit.yml), que genera inventario por rutas versionadas, informes Markdown y JSON por dominios y registros de los tres controles existentes. El commit del checkout y la versión de Python se conservan junto a los informes. Los resultados se publican como artefactos temporales de GitHub Actions, sin modificar la fuente Markdown ni sobrescribir automáticamente el informe histórico.

La primera ejecución satisfactoria permitirá establecer una línea base observada. Se mantienen las reglas actuales de auditoría para evaluar su comportamiento: su lista de dominios no equivale a los diez módulos de recetas, y las rutas canónicas del auditor no incluyen Cocina Asiática, Bebidas y Horno. No se deduce la madurez de estos módulos de su número de fichas. Los diagnósticos semánticos y huérfanos permanecen informativos. Las revisiones de reglas y la publicación de un nuevo informe versionado se abordarán tras examinar la evidencia.

## Primera línea base observada — 2026-11-18

**Commit auditado:** [`fb3b5a12a24fe343c0a4e8109dce302dd423ac0d`](https://github.com/fran-eliot/NovaCoquinaria/commit/fb3b5a12a24fe343c0a4e8109dce302dd423ac0d), merge de #196. **Evidencia:** [Knowledge audit](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44396127716), [registro del job](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44396127716/job/135126354446), [artefacto](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44396127716/artifacts/14470455816). La ejecución, las pruebas unitarias del inventario y los workflows de integridad y publicación finalizaron correctamente. Los resultados siguientes se transcriben del registro de ejecución; no constituyen una revisión del contenido íntegro del ZIP. El artefacto tiene retención temporal de 30 días.

| Indicador | Resultado |
|---|---:|
| Documentos examinados por el validador | 922 |
| Identificadores únicos verificados | 887 |
| Enlaces internos verificados | 5330 |
| Errores estructurales | 0 |
| Advertencias semánticas | 37 |
| Huérfanos globales según find_orphans | 0 |
| Fichas de recetas por rutas | 590 |
| Fichas de ingredientes por rutas | 125 |
| Documentos de técnicas por rutas | 52 |

La diferencia entre 922 documentos y 887 IDs no se interpreta como 35 defectos: el validador admite excepciones según tipo y ruta. El recuento de IDs exactos no determina equivalencia numérica de IDs con ceros iniciales ni ausencia de duplicados conceptuales.

### Dominios según las reglas vigentes

| Dominio | PRIMARY | SECONDARY | MENTION | Cobertura | Enlaces | Sin salidas en dominio | Madurez automática |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Currys | 13 | 20 | 0 | 100.0 % | 100.0 % | 1 | 🌳 Consolidado |
| Salteados asiáticos | 5 | 36 | 1 | 60.0 % | 100.0 % | 0 | 🌿 Estructurado |
| Arroces | 64 | 83 | 0 | 80.0 % | 100.0 % | 0 | 🌳 Consolidado |
| Pastas | 44 | 44 | 0 | 60.0 % | 100.0 % | 0 | 🌿 Estructurado |
| Legumbres | 84 | 49 | 0 | 80.0 % | 100.0 % | 0 | 🌳 Consolidado |
| Verduras | 17 | 213 | 0 | 100.0 % | 100.0 % | 0 | 🌿 Estructurado |
| Carnes | 6 | 129 | 0 | 100.0 % | 100.0 % | 0 | 🌿 Estructurado |
| Pescados y mariscos | 7 | 102 | 0 | 100.0 % | 100.0 % | 0 | 🌿 Estructurado |
| Huevos y lácteos | 8 | 68 | 0 | 100.0 % | 100.0 % | 0 | 🌿 Estructurado |
| Postres | 83 | 30 | 0 | 40.0 % | 100.0 % | 0 | 🌱 Exploración |

La ausencia global de huérfanos y el documento sin referencias salientes del dominio Currys no son métricas equivalentes. La cobertura se calcula sobre tipos esperados por dominio; no constituye una medida de calidad culinaria. Las reglas vigentes no incluyen vistas independientes para todos los módulos físicos. No se suman asociaciones como documentos únicos. El informe versionado de agosto permanece histórico.

### Inventario inicial de deuda semántica

24 avisos de recetas y 13 de técnicas. Todos requieren comprobar el contenido y las relaciones útiles antes de modificar documentos o reglas. No implican errores culinarios ni necesariamente omisiones editoriales. La lista identifica el conjunto exacto observado en el commit auditado.

| ID | Documento | Tipos de relación esperados | Estado |
|---|---|---|---|
| REC-389 | [agua_de_tamarindo_casera.md](../../09_Bebidas/agua_de_tamarindo_casera.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-0231 | [arroz_con_frijoles_y_cilantro.md](../../01_Arroces/arroz_con_frijoles_y_cilantro.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-390 | [atole_de_avena_y_canela.md](../../09_Bebidas/atole_de_avena_y_canela.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-388 | [ayran_de_yogur_y_menta.md](../../09_Bebidas/ayran_de_yogur_y_menta.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-393 | [batido_verde_de_kiwi_manzana_y_espinacas.md](../../09_Bebidas/batido_verde_de_kiwi_manzana_y_espinacas.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-514 | [cardo_aragones_con_salsa_de_almendras.md](../../04_Verduras/cardo_aragones_con_salsa_de_almendras.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-465 | [casadielles_asturianas_de_nueces_y_anis.md](../../08_Postres/casadielles_asturianas_de_nueces_y_anis.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-409 | [doenjang_jjigae_de_tofu_y_calabacin.md](../../07_Cocina_Asiatica/doenjang_jjigae_de_tofu_y_calabacin.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-546 | [ensalada_murciana_de_tomate_en_conserva_y_aceitunas.md](../../04_Verduras/ensalada_murciana_de_tomate_en_conserva_y_aceitunas.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-483 | [filloas_gallegas_de_leche_y_limon.md](../../08_Postres/filloas_gallegas_de_leche_y_limon.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-339 | [hamburguesas_de_frijoles_negros_y_avena.md](../../03_Legumbres/hamburguesas_de_frijoles_negros_y_avena.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-492 | [lacon_con_grelos_y_cachelos_gallego.md](../../05_Carnes/lacon_con_grelos_y_cachelos_gallego.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-321 | [limonada_de_jengibre_y_romero.md](../../09_Bebidas/limonada_de_jengibre_y_romero.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-588 | [mazapan_toledano_de_almendra.md](../../08_Postres/mazapan_toledano_de_almendra.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-369 | [minestrone_con_pasta_pequena_y_alubias.md](../../02_Pastas/minestrone_con_pasta_pequena_y_alubias.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-327 | [pavo_en_escabeche_suave_de_naranja_y_laurel.md](../../05_Carnes/pavo_en_escabeche_suave_de_naranja_y_laurel.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-467 | [pericana_alicantina_de_pimiento_seco_y_bacalao.md](../../04_Verduras/pericana_alicantina_de_pimiento_seco_y_bacalao.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-485 | [pipirrana_jiennense_con_atun_y_huevo.md](../../04_Verduras/pipirrana_jiennense_con_atun_y_huevo.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-480 | [porra_antequerana_de_tomate_y_pan.md](../../04_Verduras/porra_antequerana_de_tomate_y_pan.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-365 | [raviolis_caseros_de_ricotta_y_espinacas.md](../../02_Pastas/raviolis_caseros_de_ricotta_y_espinacas.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-536 | [rosquillas_tontas_de_san_isidro.md](../../08_Postres/rosquillas_tontas_de_san_isidro.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-356 | [semifrio_de_platano_y_cacao_sin_huevo.md](../../08_Postres/semifrio_de_platano_y_cacao_sin_huevo.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-573 | [talo_vasco_de_maiz_en_plancha.md](../../10_Horno/talo_vasco_de_maiz_en_plancha.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| REC-412 | [tiramisu_sin_huevo_crudo_con_mascarpone.md](../../08_Postres/tiramisu_sin_huevo_crudo_con_mascarpone.md) | base, ingrediente, plantilla, tabla, tecnica | Pendiente de revisión |
| TEC-0047 | [brasear_carnes_en_cazuela.md](../../00_Bases/03_Tecnicas/brasear_carnes_en_cazuela.md) | base, ingrediente, tabla | Pendiente de revisión |
| TEC-0049 | [cocinar_al_bano_maria.md](../../00_Bases/03_Tecnicas/cocinar_al_bano_maria.md) | base, ingrediente, tabla | Pendiente de revisión |
| TEC-0038 | [desglasar_fondos_de_coccion.md](../../00_Bases/03_Tecnicas/desglasar_fondos_de_coccion.md) | base, ingrediente, tabla | Pendiente de revisión |
| TEC-0044 | [equilibrar_acidez_dulzor_y_amargor.md](../../00_Bases/04_Sazonado/equilibrar_acidez_dulzor_y_amargor.md) | base, ingrediente, tabla | Pendiente de revisión |
| TEC-0048 | [escalfar_pescados_en_liquido_aromatico.md](../../00_Bases/03_Tecnicas/escalfar_pescados_en_liquido_aromatico.md) | base, ingrediente, tabla | Pendiente de revisión |
| TEC-0057 | [gratinar_coberturas_sin_quemar.md](../../00_Bases/03_Tecnicas/gratinar_coberturas_sin_quemar.md) | base, ingrediente, tabla | Pendiente de revisión |
| TEC-0052 | [hervir_y_cocer_a_fuego_suave.md](../../00_Bases/03_Tecnicas/hervir_y_cocer_a_fuego_suave.md) | base, ingrediente, tabla | Pendiente de revisión |
| TEC-0054 | [pochar_y_caramelizar_cebolla.md](../../00_Bases/03_Tecnicas/pochar_y_caramelizar_cebolla.md) | base, ingrediente, tabla | Pendiente de revisión |
| TEC-0053 | [preparar_bechamel_sin_grumos.md](../../00_Bases/03_Tecnicas/preparar_bechamel_sin_grumos.md) | base, ingrediente, tabla | Pendiente de revisión |
| TEC-0037 | [reducir_y_ligar_salsas.md](../../00_Bases/03_Tecnicas/reducir_y_ligar_salsas.md) | base, ingrediente, tabla | Pendiente de revisión |
| TEC-0043 | [salar_por_etapas.md](../../00_Bases/04_Sazonado/salar_por_etapas.md) | base, ingrediente, tabla | Pendiente de revisión |
| TEC-0058 | [tostar_frutos_secos_y_semillas.md](../../00_Bases/03_Tecnicas/tostar_frutos_secos_y_semillas.md) | base, ingrediente, tabla | Pendiente de revisión |
| TEC-0050 | [tostar_y_activar_especias.md](../../00_Bases/03_Tecnicas/tostar_y_activar_especias.md) | base, ingrediente, tabla | Pendiente de revisión |

### Prioridad de tratamiento

1. Revisar las 13 técnicas como activos reutilizables transversales; incorporar únicamente relaciones pertinentes con bases, ingredientes o tablas existentes. Identificar falsos positivos si procede.
2. Revisar las 24 recetas por grupos coherentes, sin modificar cantidades, estados de prueba ni valoraciones sin evidencia.
3. Reejecutar los controles tras cada incremento y comparar los avisos por ID y ruta, no solo el total. Mantener el diagnóstico informativo.
4. Revisar la cobertura y reglas del auditor por dominios, especialmente Postres y las rutas canónicas de Cocina Asiática, Bebidas y Horno. No elevar artificialmente la madurez mediante enlaces ornamentales.
5. Evaluar la preparación para un contrato de datos a partir de muestras representativas; no exigir eliminar todos los avisos para comenzar si las excepciones están justificadas.

El incremento registra la evidencia y ordena las revisiones. No corrige aún las 37 advertencias ni cambia las reglas de auditoría.

## Revisión de las 13 técnicas señaladas — 2026-11-18

Se revisan los documentos de técnica y sus destinos de conocimiento reutilizable. Se añade una relación pertinente por documento, sin alterar procedimientos, estado editorial, identificadores ni reglas del auditor. Los 13 destinos existentes se han contrastado con sus fichas fuente.

| Técnica | Conocimiento reutilizado | Justificación |
|---|---|---|
| [brasear carnes en cazuela](../../00_Bases/03_Tecnicas/brasear_carnes_en_cazuela.md) | [Diagnóstico de cocción de carnes](../../98_Tablas/07_Comparativas/diagnostico_carnes.md) | criterios para distinguir falta de terneza y exceso de líquido |
| [cocinar al bano maria](../../00_Bases/03_Tecnicas/cocinar_al_bano_maria.md) | [Huevo](../../11_Despensa/14_Huevos_Lacteos/huevo.md) | función de coagulación y estructura en los cuajados |
| [desglasar fondos de coccion](../../00_Bases/03_Tecnicas/desglasar_fondos_de_coccion.md) | [Vino blanco para cocinar](../../11_Despensa/11_Condimentos/vino_blanco_cocina.md) | selección y manejo del líquido de desglasado |
| [escalfar pescados en liquido aromatico](../../00_Bases/03_Tecnicas/escalfar_pescados_en_liquido_aromatico.md) | [Fumet de pescado](../../11_Despensa/13_Bases_Culinarias/fumet_de_pescado.md) | fondo suave apropiado para la cocción |
| [gratinar coberturas sin quemar](../../00_Bases/03_Tecnicas/gratinar_coberturas_sin_quemar.md) | [Pan rallado](../../11_Despensa/01_Cereales/pan_rallado.md) | selección de granulometría y manejo de coberturas |
| [hervir y cocer a fuego suave](../../00_Bases/03_Tecnicas/hervir_y_cocer_a_fuego_suave.md) | [Tiempos de cocción](../../98_Tablas/01_Cocciones/tiempos_coccion.md) | intervalos orientativos por alimento |
| [pochar y caramelizar cebolla](../../00_Bases/03_Tecnicas/pochar_y_caramelizar_cebolla.md) | [Cebolla](../../11_Despensa/06_Verduras/cebolla.md) | variedades y evolución aromática durante la cocción |
| [preparar bechamel sin grumos](../../00_Bases/03_Tecnicas/preparar_bechamel_sin_grumos.md) | [Harina de trigo](../../11_Despensa/01_Cereales/harina_de_trigo.md) | selección de harina y formación del roux |
| [reducir y ligar salsas](../../00_Bases/03_Tecnicas/reducir_y_ligar_salsas.md) | [Almidón de maíz (maicena)](../../11_Despensa/13_Bases_Culinarias/maicena.md) | dispersión en frío y espesado sin reducción excesiva |
| [tostar frutos secos y semillas](../../00_Bases/03_Tecnicas/tostar_frutos_secos_y_semillas.md) | [Almendras](../../11_Despensa/16_Frutos_Secos/almendras.md) | manejo del tostado y control del calor residual |
| [tostar y activar especias](../../00_Bases/03_Tecnicas/tostar_y_activar_especias.md) | [Comino](../../11_Despensa/08_Especias/comino.md) | diferencias de manejo entre semilla entera y especia molida |
| [equilibrar acidez dulzor y amargor](../../00_Bases/04_Sazonado/equilibrar_acidez_dulzor_y_amargor.md) | [Limón](../../11_Despensa/11_Condimentos/limon.md) | dosificación de acidez y prevención del amargor de la piel blanca |
| [salar por etapas](../../00_Bases/04_Sazonado/salar_por_etapas.md) | [Salsa de soja](../../11_Despensa/09_Salsas/salsa_de_soja.md) | aporte de salinidad que debe considerarse antes del ajuste final |

La eliminación de los avisos queda pendiente de comprobar mediante una nueva ejecución de Knowledge audit. Los 24 avisos de recetas no se abordan en este incremento. Se conserva la línea base histórica sin modificar sus recuentos.

## Consolidación de Bebidas — 2026-11-18

La [auditoría del merge #198](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44398171800), commit `b57cc5d4cd4539dcbd0bdb888027733592c2e1b7`, confirma la reducción de 37 a 24 advertencias semánticas, sin avisos de técnicas ni huérfanos globales. Se verifican 5406 enlaces internos, 887 IDs y 922 documentos.

Se añaden relaciones reutilizables a las cinco recetas de Bebidas señaladas por el diagnóstico, preservando sus formulaciones y estados de prueba.

| Receta | Referencia | Utilidad |
|---|---|---|
| [agua de tamarindo casera](../../09_Bebidas/agua_de_tamarindo_casera.md) | [Diagnóstico de bebidas](../../98_Tablas/07_Comparativas/diagnostico_bebidas.md) | ajuste de acidez, dilución y filtrado |
| [atole de avena y canela](../../09_Bebidas/atole_de_avena_y_canela.md) | [Canela](../../11_Despensa/08_Especias/canela.md) | selección y extracción aromática en leche |
| [ayran de yogur y menta](../../09_Bebidas/ayran_de_yogur_y_menta.md) | [Yogur natural](../../11_Despensa/14_Huevos_Lacteos/yogur_natural.md) | selección de la base láctea y control de textura |
| [batido verde de kiwi manzana y espinacas](../../09_Bebidas/batido_verde_de_kiwi_manzana_y_espinacas.md) | [Espinacas](../../11_Despensa/06_Verduras/espinacas.md) | selección y manejo de hojas frescas |
| [limonada de jengibre y romero](../../09_Bebidas/limonada_de_jengibre_y_romero.md) | [Limón](../../11_Despensa/11_Condimentos/limon.md) | dosificación de acidez y uso del zumo |

La reducción de 24 a 19 avisos es una expectativa pendiente de ejecución. No se modifican reglas del auditor.

## Consolidación de Postres y Horno — 2026-11-18

La [auditoría del merge #199](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44399560162), commit `e610afdc4c8b4311c1076b54d1d069565a87e80e`, confirma la reducción de 24 a 19 advertencias semánticas: desaparecen los cinco avisos de Bebidas. Se verifican 922 documentos, 887 IDs y 5421 enlaces internos; no se detectan huérfanos globales.

Se revisan seis recetas de Postres y una de Horno. Se incorpora una relación pertinente por ficha, conservando formulaciones, identificadores y estados de prueba.

| Receta | Referencia | Utilidad |
|---|---|---|
| [casadielles asturianas de nueces y anis](../../08_Postres/casadielles_asturianas_de_nueces_y_anis.md) | [Nueces](../../11_Despensa/16_Frutos_Secos/nueces.md) | selección, frescura y picado del relleno |
| [filloas gallegas de leche y limon](../../08_Postres/filloas_gallegas_de_leche_y_limon.md) | [Harina de trigo](../../11_Despensa/01_Cereales/harina_de_trigo.md) | selección de harina común y ajuste de hidratación |
| [mazapan toledano de almendra](../../08_Postres/mazapan_toledano_de_almendra.md) | [Almendras](../../11_Despensa/16_Frutos_Secos/almendras.md) | función estructural de la almendra molida y selección del fruto |
| [rosquillas tontas de san isidro](../../08_Postres/rosquillas_tontas_de_san_isidro.md) | [Huevo](../../11_Despensa/14_Huevos_Lacteos/huevo.md) | ligazón y estructura de la masa durante el horneado |
| [semifrio de platano y cacao sin huevo](../../08_Postres/semifrio_de_platano_y_cacao_sin_huevo.md) | [Plátano](../../11_Despensa/17_Frutas/platano.md) | madurez, dulzor y textura al triturar fruta congelada |
| [tiramisu sin huevo crudo con mascarpone](../../08_Postres/tiramisu_sin_huevo_crudo_con_mascarpone.md) | [Preparar café por extracción](../../00_Bases/03_Tecnicas/preparar_cafe.md) | control de intensidad y extracción del café para el remojo |
| [talo vasco de maiz en plancha](../../10_Horno/talo_vasco_de_maiz_en_plancha.md) | [Seguridad alimentaria](../../98_Tablas/05_Seguridad/seguridad_alimentaria.md) | manejo separado del relleno de chistorra, refrigeración y recalentado |

### Hallazgos editoriales adicionales

Las fichas de semifrío de plátano y tiramisú contienen recomendaciones genéricas sobre hornos, cocción o cuajado térmico que no corresponden a sus procedimientos en frío. Se registra esta deuda para una revisión editorial específica, sin alterar aquí las fórmulas ni atribuir pruebas domésticas. En el talo, la relación de seguridad es pertinente al relleno opcional y la conservación, pero no sustituye una futura ficha específica de harina de maíz no precocida.

La reducción de 19 a 12 advertencias es una expectativa pendiente de comprobar en una nueva ejecución. No se modifican las reglas del auditor.

## Consolidación de Verduras — 2026-11-18

La [auditoría del merge #200](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44400824199), commit `59e19f773f771123cee3be191b15bbf925a2df46`, confirma la reducción de 19 a 12 advertencias semánticas, sin avisos de Postres y Horno. Se verifican 922 documentos, 887 IDs y 5442 enlaces internos; no se detectan huérfanos globales.

Se incorpora una relación reutilizable por cada una de las cinco recetas de Verduras señaladas, sin modificar formulaciones, identificadores ni estados de prueba.

| Receta | Referencia | Utilidad |
|---|---|---|
| [cardo aragones con salsa de almendras](../../04_Verduras/cardo_aragones_con_salsa_de_almendras.md) | [Almendras](../../11_Despensa/16_Frutos_Secos/almendras.md) | tostado moderado y función espesante del majado |
| [ensalada murciana de tomate en conserva y aceitunas](../../04_Verduras/ensalada_murciana_de_tomate_en_conserva_y_aceitunas.md) | [Atún en conserva](../../11_Despensa/12_Conservas/atun_en_conserva.md) | escurrido, salinidad y manejo tras abrir el envase |
| [pericana alicantina de pimiento seco y bacalao](../../04_Verduras/pericana_alicantina_de_pimiento_seco_y_bacalao.md) | [Bacalao](../../11_Despensa/04_Pescados/bacalao.md) | distinción de formatos, desalado y cocción completa |
| [pipirrana jiennense con atun y huevo](../../04_Verduras/pipirrana_jiennense_con_atun_y_huevo.md) | [Huevo](../../11_Despensa/14_Huevos_Lacteos/huevo.md) | uso de yema cocida para ligar el majado |
| [porra antequerana de tomate y pan](../../04_Verduras/porra_antequerana_de_tomate_y_pan.md) | [Tomate fresco](../../11_Despensa/06_Verduras/tomate_fresco.md) | selección según madurez, jugosidad y acidez |

Se observa deuda editorial adicional: los diagnósticos de pipirrana y porra incluyen sugerencias de cocción o reducción que no corresponden a su preparación en frío. Se registra para una revisión específica. La reducción de 12 a 7 avisos queda pendiente de comprobar; las reglas de auditoría permanecen intactas.

## Consolidación de Arroces, Pastas, Legumbres, Carnes y Cocina Asiática — 2026-11-18

La [auditoría del merge #201](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44401468035), commit `4a3acba1327008643ebf4b19b33375f550f2e7c9`, confirma la reducción de 12 a 7 avisos semánticos, con 922 documentos, 887 IDs, 5457 enlaces internos y ningún huérfano global detectado.

Se revisan las siete recetas restantes del inventario inicial de advertencias y se añade una relación pertinente por ficha, preservando los procedimientos, identificadores y estados de prueba.

| Receta | Referencia | Utilidad |
|---|---|---|
| [arroz con frijoles y cilantro](../../01_Arroces/arroz_con_frijoles_y_cilantro.md) | [Cocer arroz por absorción](../../00_Bases/03_Tecnicas/cocer_arroz_por_absorcion.md) | control del líquido, tapa y reposo |
| [doenjang jjigae de tofu y calabacin](../../07_Cocina_Asiatica/doenjang_jjigae_de_tofu_y_calabacin.md) | [Tofu firme](../../11_Despensa/02_Legumbres/tofu_firme.md) | selección y manipulación de dados en caldo |
| [hamburguesas de frijoles negros y avena](../../03_Legumbres/hamburguesas_de_frijoles_negros_y_avena.md) | [Huevo](../../11_Despensa/14_Huevos_Lacteos/huevo.md) | ligazón y coagulación de la mezcla |
| [lacon con grelos y cachelos gallego](../../05_Carnes/lacon_con_grelos_y_cachelos_gallego.md) | [Hervir y cocer a fuego suave](../../00_Bases/03_Tecnicas/hervir_y_cocer_a_fuego_suave.md) | control del hervor en cocciones prolongadas |
| [minestrone con pasta pequena y alubias](../../02_Pastas/minestrone_con_pasta_pequena_y_alubias.md) | [Pasta seca](../../11_Despensa/01_Cereales/pasta_seca.md) | absorción de caldo y control de textura |
| [pavo en escabeche suave de naranja y laurel](../../05_Carnes/pavo_en_escabeche_suave_de_naranja_y_laurel.md) | [Laurel](../../11_Despensa/08_Especias/laurel.md) | dosificación e infusión aromática |
| [raviolis caseros de ricotta y espinacas](../../02_Pastas/raviolis_caseros_de_ricotta_y_espinacas.md) | [Ricotta](../../11_Despensa/14_Huevos_Lacteos/ricotta.md) | escurrido y humedad del relleno |

El cierre de los siete avisos queda sujeto a nueva auditoría y comparación por ID y ruta. Cero advertencias no certificaría calidad semántica exhaustiva ni madurez culinaria. Se conserva la deuda editorial detectada y se añade la recomendación de revisar el diagnóstico genérico de raviolis y las instrucciones de conservación relativas al arroz en doenjang jjigae, que no contiene arroz. También conviene precisar el retiro de hojas de laurel del escabeche de pavo antes de servir. No se modifican estas secciones en el lote de relaciones.

## Cierre del primer ciclo de relaciones — 2026-11-18

La [auditoría del merge #202](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44402431807), commit `78518ab3b43ac9267c06cf250e7bffbc14dd730c`, confirma la desaparición de las 37 advertencias iniciales: 13 técnicas y 24 recetas revisadas. Se verifican 922 documentos, 887 IDs exactos y 5478 enlaces internos, sin errores estructurales ni huérfanos globales detectados. Los tres workflows de main finalizaron correctamente. La cobertura automática por dominios continúa siendo orientativa y Currys conserva un documento sin referencias salientes en su diagnóstico particular. El cierre se circunscribe a las reglas vigentes y no certifica calidad culinaria ni exhaustividad semántica. La revisión de cobertura, la deuda editorial identificada y el contrato de datos permanecen pendientes. El [kit de continuidad](./NOVACOQUINARIA_KIT_CONTINUITY.md) recoge el corte y sus prioridades.


## Revisión del alcance y las reglas de auditoría — 2026-11-18

**Corte:** [merge #203](https://github.com/fran-eliot/NovaCoquinaria/pull/203), commit `12132d1bc4c240b4b888a996b092784b9b6ac250`. El [job de auditoría](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44403245388/job/135151569226) confirma cero advertencias semánticas y cero huérfanos globales. Se revisan estáticamente `tools/audit_inventory.py`, `tools/audit_knowledge.py` y `tools/semantic_rules.py`, junto al árbol remoto. No se modifica el comportamiento del auditor en este incremento.

### Dos vistas complementarias

| Módulo físico | Fichas por ruta | Dominio homónimo en auditoría | Naturaleza del dominio |
|---|---:|---|---|
| Arroces | 39 | Sí | CATEGORY |
| Pastas | 37 | Sí | CATEGORY |
| Legumbres | 61 | Sí | CATEGORY |
| Verduras | 86 | Sí | INGREDIENT |
| Carnes | 82 | Sí | INGREDIENT |
| Pescados y Mariscos | 69 | Sí | INGREDIENT |
| Cocina Asiática | 44 | No | Currys y Salteados asiáticos son PATTERN, no equivalencias del módulo |
| Postres | 82 | Sí | CATEGORY |
| Bebidas | 36 | No | Sin regla homónima |
| Horno | 54 | No | Sin regla homónima |

Los recuentos proceden del árbol versionado y excluyen README. Los diez dominios actuales incluyen asimismo Huevos y lácteos (INGREDIENT), sin módulo de recetas homónimo. La ausencia de un dominio homónimo no significa que sus fichas nunca aparezcan en la auditoría: pueden asociarse por título, metadatos o enlaces. Las asociaciones no son una partición; un documento puede pertenecer a varios dominios.

### Semántica efectiva de las métricas

| Indicador | Interpretación del código vigente | Límite |
|---|---|---|
| PRIMARY | Coincidencia de ruta, dominio explícito, título autorizado o enlace de autoridad de patrón según precedencia | Clasificación heurística, no autoridad editorial certificada |
| SECONDARY | Ruta temática en dominios de ingrediente, coincidencia de título/metadatos o enlace desde ciertos PRIMARY | No acredita una dependencia culinaria tipada |
| MENTION | Coincidencia en encabezados culinarios controlados | No es búsqueda exhaustiva del cuerpo |
| Cobertura estructural | Tipos esperados presentes entre PRIMARY / tipos esperados | Cuatro dominios de ingrediente esperan solo ingrediente; 100 % no es comparable directamente con cinco tipos esperados |
| Enlaces resueltos | Destinos documentales resueltos entre enlaces salientes de PRIMARY | No mide pertinencia culinaria ni exhaustividad de relaciones; sin enlaces corresponde N/A |
| Huérfanos del dominio | PRIMARY sin enlaces salientes | Distinto del diagnóstico global de conectividad |
| Madurez automática | Umbrales y presencia de tipos, diferentes según PATTERN, CATEGORY o INGREDIENT | No equivale a madurez editorial o prueba doméstica |

### Hallazgos y tratamiento propuesto

| ID de hallazgo | Evidencia en el código | Tratamiento candidato |
|---|---|---|
| AUD-01 | `CANONICAL_RECIPE_PATH_PREFIXES` omite 07, 09 y 10 | Unificar las rutas de recetas con el inventario; comprobar el efecto en patrones antes de adoptar el cambio |
| AUD-02 | `classify_direct_association` puede promover una receta con enlace de autoridad, sin título de patrón ni referencia declarada, cuando queda fuera de las rutas canónicas | Probar las diez rutas y preservar las excepciones de título y referencia explícita |
| AUD-03 | Los dominios y módulos representan ejes diferentes | Conservar ambos; no crear dominios artificialmente para completar el inventario |
| AUD-04 | `contains_any` y fragmentos de ruta usan subcadenas normalizadas | Evaluar falsos positivos y límites de coincidencia con muestras antes de modificar reglas |
| AUD-05 | El dominio explícito se evalúa después de la coincidencia de ruta y puede promover tipos no previstos para INGREDIENT | Revisar precedencia y tipos permitidos con pruebas; no cambiar metadatos para satisfacer una métrica |
| AUD-06 | La etiqueta de huérfanos de dominio y los porcentajes pueden inducir equivalencias incorrectas | Explicitar denominadores, nivel de asociación y diferencia con huérfanos globales en informes |

### Baseline de comparación

La ejecución del merge #203 mantiene los niveles de cobertura de #202: Currys 100 %, Salteados asiáticos 60 %, Arroces 80 %, Pastas 60 %, Legumbres 80 %, Verduras 100 %, Carnes 100 %, Pescados y mariscos 100 %, Huevos y lácteos 100 % y Postres 40 %. Currys conserva un PRIMARY sin enlaces salientes. Se preserva esta línea base como resultado de las reglas antiguas, no como objetivo numérico.

### Secuencia de evolución y aceptación

1. Preparar pruebas de clasificación con casos sintéticos de los diez módulos, recetas transversales, coincidencias de título, referencia declarada y enlaces de autoridad.
2. Abordar AUD-01 y AUD-02 conjuntamente en un incremento de herramientas; mantener las reglas restantes y comprobar que inventario, validación estructural y diagnóstico semántico global no se alteran.
3. Comparar los informes del mismo corpus con reglas anteriores y nuevas, por dominio, nivel, evidencia e ID/ruta; justificar reclasificaciones sin exigir aumento de cobertura.
4. Revisar AUD-03–AUD-06 de manera separada según evidencia; publicar denominadores y límites de las métricas antes de interpretar cambios como mejora del conocimiento.

La revisión es documental y estática: no incluye inspección íntegra de artefactos ZIP ni cuantificación de falsos positivos. No modifica recetas, estados de evidencia, taxonomía conceptual, release ni arquitectura de persistencia. La deuda editorial y el contrato de datos mantienen su prioridad posterior.
