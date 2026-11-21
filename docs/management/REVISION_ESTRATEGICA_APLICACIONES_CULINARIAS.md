---
id: DOC-REVISION-APLICACIONES-CULINARIAS-2026
titulo: Revisión estratégica de las aplicaciones culinarias
tipo: gestion
version: 0.1.1
estado: propuesta
ultima_revision: 2026-11-21
---

# Revisión estratégica — Consolidación de aplicaciones culinarias

## Objeto y corte de evidencia

Tras la integración de Culinary Planner 0.1.0 (#303) y la documentación de cierre (#304), NovaCoquinaria dispone de cinco aplicaciones estáticas conectadas a distintas partes del conocimiento culinario. Esta revisión contrasta **capacidad implementada**, **evidencia automatizada**, **publicación** y **uso real**, que no deben equipararse.

Corte de referencia: `main` `8bb984a1de8675523fab6a74aafc7cfca8caf6f7`, tras #304; las tres comprobaciones de #304 finalizaron con `success`. La rama `gh-pages` registra `Deployed 8bb984a`. La última release aprobada continúa siendo **v1.6.0**. Las afirmaciones de este documento se limitan al estado comprobado y a la evidencia conservada en los alcances de entrega.

## Mapa operativo

| Aplicación | Capacidad que aporta | Contrato o límite fundamental |
|---|---|---|
| Culinary Explorer | Consulta documental de recetas, menciones y evidencia registrada | Una mención no es disponibilidad, compatibilidad ni suficiencia |
| Recipe Assistant | Preparación guiada desde receta concreta, sin persistir la sesión de cocina | Pasos, tiempos e ingredientes dependen de la fuente; no se verifican mediante ejecución doméstica |
| Culinary Pantry | Inventario personal declarado por lotes, copias JSON y consulta de menciones | Las existencias son declaraciones locales, no cantidades realmente comprobadas |
| Culinary Shopping | Listas, selección revisada desde recetas y transferencia explícita a Pantry | No hay operación atómica entre claves ni recuperación destructiva automática |
| Culinary Planner | Calendario manual de comidas y referencias verificadas al catálogo | No genera menús, faltantes, dietas, consumos o compras por inferencia |

Los datos personales residen en almacenamiento del navegador y no forman parte del conocimiento Markdown. Explorer y Assistant consumen publicaciones derivadas del contenido canónico; la referencia documental no convierte las acciones del usuario en conocimiento canónico.

## Evidencia disponible y huecos

- #303: tres workflows satisfactorios. El recorrido Chromium de Planner acreditó calendario, operaciones, copias JSON, selección expresa desde Explorer y Assistant, comprobación de referencias antiguas y aislamiento respecto de Pantry y Shopping.
- #297: tres workflows satisfactorios. Las pruebas dirigidas de Shopping cubrieron listas, selección de ingredientes, escritura revisada en Pantry, recuperación ante fallo de finalización y prohibición de recrear un destino ausente.
- #304: CI satisfactorio y despliegue de su commit observado en `gh-pages`.
- Los recorridos de CI se ejecutan en un servidor local con Chromium y datos controlados. No sustituyen una verificación manual de los enlaces públicos, ni cubren todas las variantes de permisos, navegadores, restauraciones independientes o sesiones históricas.
- Sigue sin acreditarse formalmente el uso público integral de Pantry, Shopping y Planner por el propietario. No se debe cerrar esa evidencia por inferencia desde GitHub Pages.
- La secuencia completa **Planner → Assistant → Shopping → Pantry** no dispone de una prueba única que compruebe los cambios de estado en cada frontera con el mismo escenario y sin mutaciones implícitas. Existen pruebas separadas útiles que deben conservarse.
- Shopping y Pantry utilizan claves locales distintas. Los fallos entre escrituras conservan intenciones pendientes; si el destino está ausente o ha cambiado, el protocolo se detiene para revisión humana. No se debe describir esta conducta como transacción o reconciliación automática.
- La separación entre copias individuales de Planner, Shopping y Pantry impide suponer una restauración consistente del conjunto. No existe sincronización remota ni una copia global coordinada.
- Las cinco páginas tienen pruebas funcionales dirigidas, pero no se ha acreditado auditoría integral de accesibilidad, rendimiento con datos personales extensos, compatibilidad entre navegadores ni condiciones reales de uso en móviles.

## Decisión propuesta

**Prioridad inmediata: consolidación de recorridos y fiabilidad operativa de las cinco aplicaciones (Culinary Workflows Consolidation 0.1.0).**

Se prefiere esta línea a comenzar una sexta aplicación, a automatizar propuestas de menú o a construir un backend. La razón no es una carencia de módulos: el conjunto ya permite buscar, preparar, planificar, comprar y mantener inventario. El valor siguiente depende de comprobar que esas transiciones son comprensibles, verificables y recuperables en sus límites reales.

La consolidación no equivale a una nueva release ni a una nueva capacidad de inferencia. Se articula en cuatro unidades pequeñas, con ramas y PR independientes y evidencia asociada a cada criterio. Las decisiones de alcance se revisarán tras la primera línea base.

## Unidades de trabajo

| Unidad | Entregable | Condición de salida |
|---|---|---|
| A — Integrated Journey Baseline | Escenario Chromium desde plan de comidas hasta consulta de receta, selección revisada, marcado de compra y alta de lote; comprobar persistencia y ausencia de escrituras implícitas | CI reproducible con resultado contrastable y sin tocar datos reales |
| B — Storage & Failure Matrix | Matriz y pruebas aisladas de fallos, conflictos, importaciones/restauraciones independientes, transferencias pendientes y cambios entre pestañas | No crear ni repetir lotes automáticamente al recuperar; errores visibles y trazables |
| C — Usability & Accessibility Baseline | Contraste dirigido con teclado, foco, formularios, mensajes, espacios reducidos y estados vacíos, de error y recuperación | Incidencias observadas clasificadas y corregidas o registradas con alcance explícito |
| D — Public Acceptance & Closure | Checklist reproducible de los cinco recorridos sobre Pages, registro de evidencia manual aportada por el propietario y reconciliación de documentación de gestión | Diferenciar CI, despliegue, prueba manual y aceptación; sin cierre ficticio |

La unidad A reutilizará los escenarios y herramientas del repositorio. Se evitará añadir un nuevo almacenamiento de preferencias o inventarios de prueba en producción. Las pruebas deberán emplear un origen local aislado y limpiar su estado tras la ejecución.

## Criterios de aceptación propuestos

| ID | Resultado exigido |
|---|---|
| CWC-01 | Flujo integrado recorre Planner → Assistant → Shopping → Pantry con elecciones explícitas y cambios de página trazables |
| CWC-02 | Planner solo crea entradas al confirmar, y no modifica claves de Shopping/Pantry |
| CWC-03 | Assistant no convierte ingredientes o cantidades de la receta en compra sin revisión humana |
| CWC-04 | Marcar un artículo como comprado no altera Pantry |
| CWC-05 | Solo una transferencia confirmada genera lote con destino verificable |
| CWC-06 | Una intención pendiente no recrea un lote ausente ni modifica un destino divergente |
| CWC-07 | Copias de cada aplicación conservan contratos y rechazan datos inválidos |
| CWC-08 | Conflictos y bloqueos de almacenamiento no se silencian ni sustituyen documentos |
| CWC-09 | La navegación con teclado, los mensajes de estado y la presentación móvil tienen evidencia dirigida |
| CWC-10 | Los datos personales no se insertan en URLs ni se convierten en datos de catálogo |
| CWC-11 | El build y las regresiones de las cinco aplicaciones siguen siendo reproducibles |
| CWC-12 | La aceptación pública manual se registra por separado, con fecha, versión y recorrido comprobados |

Estos criterios son requisitos de la propuesta, no resultados ya acreditados. Las pruebas existentes podrán constituir evidencia para un criterio solo cuando realmente cubran sus condiciones.

## Alternativas consideradas

**Nueva capacidad automática de planificación o recomendaciones:** prematura por la deuda documentada de identidad, compatibilidad y reconocimiento de requisitos culinarios; podría introducir afirmaciones no justificadas sobre existencias y dietas.

**Backend y sincronización:** aportaría movilidad de datos, pero cambiaría arquitectura, superficie de seguridad, privacidad y coste de operación antes de completar la aceptación de los cinco recorridos estáticos. Requiere decisión específica futura.

**Más recetas como prioridad dominante:** se mantiene la incorporación selectiva con evidencia culinaria, sin usar volumen de fichas como sustituto de fiabilidad del producto.

**Publicar una release ahora:** no se considera autorización implícita. Las versiones internas 0.1.0 de las aplicaciones y los merges recientes no modifican la release de proyecto v1.6.0.

## Restricciones y método

- No inferir faltantes, sustituciones, compatibilidad, seguridad alimentaria, nutrición ni cantidades a partir de menciones.
- No mezclar archivos Markdown canónicos con datos personales de planificación, compra o despensa.
- No suavizar las restricciones de recuperación de Shopping → Pantry sin pruebas específicas de consistencia.
- Una PR por unidad temática sobre el `main` fusionado; el propietario revisa, fusiona y elimina la rama remota.
- Si CI falla, corregir sobre la misma PR antes de iniciar otra unidad.
- Mantener el Kit de continuidad vigente y actualizarlo tras un hito comprobado, no para anticipar resultados.
- No comprometer nueva release, sprint, milestone, API, backend, proveedor ni automatización de compras en esta revisión.

## Próxima decisión

La primera ejecución recomendada es **Unidad A — Integrated Journey Baseline**. Después de su evidencia, comparar los fallos observados con los riesgos de almacenamiento y usabilidad antes de seleccionar la segunda unidad efectiva. La comprobación manual pública se reserva a la unidad D y requiere evidencia real del propietario.

## Referencias internas

- [Kit de continuidad 2.7.0](./NOVACOQUINARIA_KIT_CONTINUITY.md)
- [Estado del proyecto](./PROJECT_STATUS.md)
- [Roadmap](./ROADMAP.md)
- [Culinary Planner](./ALCANCE_CULINARY_PLANNER.md)
- [Culinary Shopping](./ALCANCE_CULINARY_SHOPPING.md)
- [Culinary Pantry](./ALCANCE_CULINARY_PANTRY.md)
- [Deuda semántica de requisitos](./DEUDA_REQUISITOS_CULINARIOS.md)

## Unidad A — Línea base del recorrido integrado

Se incorpora `tools/check_culinary_integrated_journey_browser.py` al workflow **Culinary Explorer site**. El escenario utiliza un servidor HTTP local, un contexto de Chromium nuevo y una copia temporal del portal; no carga, guarda ni elimina datos personales del portal público.

La prueba enlaza explícitamente Explorer → Planner → Recipe Assistant → Shopping → Pantry, con una misma referencia de receta y las tres claves locales observadas en cada frontera. Verifica la selección efímera, que Planner no escribe antes de confirmar, que el asistente no crea una compra al marcar una ocurrencia, la revisión de artículo antes de añadirlo, la inexistencia de inventario después del marcado de compra, la cancelación de transferencia, la creación de un lote individual tras revisión y confirmación, su coincidencia íntegra con el historial protegido de Shopping, y la persistencia del recorrido tras recargas. Las cantidades de compra y de inventario solo proceden de la acción explícita del test, no se calculan desde las menciones de la receta.

**Alcance de evidencia:** CWC-01–CWC-05 y CWC-10 de forma dirigida; CWC-11 en la medida acreditada por la construcción y las regresiones existentes. La Unidad A no verifica CWC-06–CWC-09 ni CWC-12 en su totalidad: quedan para las unidades B–D. La regresión no acredita uso público manual, atomicidad entre claves, sincronización ni seguridad culinaria.

El resultado de CI y el artefacto `integrated-journey-browser.json` se anotarán solo después de observarlos. No se asume que añadir un test equivale a superarlo.
