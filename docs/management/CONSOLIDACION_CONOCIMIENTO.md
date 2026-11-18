---
id: DOC-CONSOLIDACION-CONOCIMIENTO-2026
titulo: Consolidación del conocimiento culinario
tipo: gestion
version: 1.1.0
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

**Estado:** propuesta de dirección estratégica, pendiente de aprobación. No declara cerrada la evolución del conocimiento ni modifica aún las prioridades oficiales del Roadmap.

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

### Decisión pendiente

La aprobación de la transición habilitaría actualizar PROJECT_STATUS, ROADMAP, BITACORA y el kit de continuidad con el nuevo alcance, antes de iniciar el primer incremento de auditoría. La aprobación de esta dirección no equivale a aprobar una tecnología, release o implementación concreta.
