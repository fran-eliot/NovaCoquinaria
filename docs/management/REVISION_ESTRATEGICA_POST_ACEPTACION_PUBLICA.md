---
id: DOC-REVISION-POST-ACEPTACION-PUBLICA-2026
titulo: Revisión estratégica tras la aceptación pública de los recorridos culinarios
tipo: gestion
version: 0.1.0
estado: propuesta
ultima_revision: 2026-11-22
---

# Revisión estratégica tras la aceptación pública

## Punto de partida verificado

Corte de `main` tras la [PR #336](https://github.com/fran-eliot/NovaCoquinaria/pull/336): `15beeed2cc7e426b5892ee1db99646c23eb8accd`. La PR está fusionada y los workflows de la PR (Knowledge integrity, Knowledge audit y Culinary Explorer site) concluyeron en `success`. No había PR abiertas al tomar el corte.

Las cinco aplicaciones estáticas —Culinary Explorer, Recipe Assistant, Pantry, Shopping y Planner— están publicadas y disponen de pruebas dirigidas de navegación, persistencia y transferencia. La Unidad D y CWC-12 cerraron con **aceptación funcional acotada**, no con una auditoría general de la plataforma. El [protocolo](./PROTOCOLO_ACEPTACION_PUBLICA_CULINARIA.md) registra PUB-01–PUB-07, el carácter declarativo de las pruebas manuales y las limitaciones de su evidencia. Sigue publicada `v1.6.0`; las versiones internas de aplicaciones y los merges posteriores no representan una nueva release global.

El inventario de referencia documenta **590 recetas**; otras cifras de corpus o extracción son cortes históricos, no un recuento reejecutado en esta revisión. La auditoría de madurez por dominios citada en gestión se remonta al 2026-08-03. El informe histórico #246 distinguía 5.047 ocurrencias de ingredientes, 36 identidades explícitas, 1.044 con candidato y 3.967 sin identidad resuelta ni candidato. Estas magnitudes **no son una medición vigente ni prueban que las recetas sean cocinables**. El trabajo de CCE/CRM/CRR demostró límites de compatibilidad y reconocimiento, manteniendo abierta la [deuda semántica](./DEUDA_REQUISITOS_CULINARIOS.md).

## Problema estratégico

La siguiente barrera de valor no es abrir más aplicaciones, sino saber si las recetas y técnicas publicadas ofrecen información suficientemente **completa, clara, reutilizable y verificada** para cocinar y recuperar conocimiento. La aceptación del software demuestra funcionamiento dirigido de recorridos, no calidad culinaria global del corpus. El crecimiento de recetas por sí solo tampoco garantiza diversidad, ausencia de redundancias ni evidencia de ejecución doméstica.

Se deben separar cuatro planos:

1. **Integridad estructural:** Markdown válido, identificadores y enlaces; ya cuenta con CI.
2. **Cobertura y utilidad editorial:** claridad, ingredientes, elaboración, técnicas, variantes y relaciones relevantes; exige muestras revisadas.
3. **Evidencia culinaria:** preparación probada, pendiente de probar, valoración subjetiva, correcciones y procedencia; no debe inferirse.
4. **Exactitud semántica computable:** identidad, cantidad, requisitos y alternativas; deuda documentada que no autoriza compatibilidad o recomendaciones automáticas.

## Alternativas valoradas

| Alternativa | Valor potencial | Restricción determinante | Decisión propuesta |
|---|---|---|---|
| Reevaluación de calidad y utilidad del conocimiento | Muy alto para las cinco aplicaciones existentes | Requiere medidas reproducibles y revisión humana, no solo conteos | **Primera prioridad** |
| Incorporación selectiva de recetas y técnicas | Alto cuando cubre lagunas o mejora recetas probadas | Más volumen sin diagnóstico puede aumentar duplicidades | Mantener de manera selectiva, no como objetivo de volumen |
| Normalización de identidades y requisitos | Alto a medio plazo | Resultados CCE/CRM/CRR insuficientes para automatizar cocinabilidad | Mantener deuda, priorizar ejemplos con efecto visible |
| Filtros de tiempo/rendimiento y escalado adicional | Alto para recetas con datos explícitos | Cobertura limitada y riesgo de aparentar precisión | Evaluar tras conocer la cobertura actual y utilidad |
| Recomendación de recetas por inventario o menú automático | Potencialmente alto | Faltan semántica y suficiencia de cantidades verificadas | Diferir |
| Backend, sincronización, RAG o agentes | Estratégico, pero prematuro | Añaden costes, privacidad, dependencias y riesgo de inferencias no validadas | Diferir, salvo nuevo caso de uso medido |
| Nueva release global | Posible más adelante | Requiere decisión editorial y de publicación independiente | No autorizada por esta revisión |

Las valoraciones son hipótesis de dirección, **no resultados de entrevistas ni métricas de uso**. Los usuarios de las pruebas manuales no constituyen una muestra independiente de adopción.

## Capacidad candidata: Culinary Knowledge Quality Baseline

Proponer una **línea base de calidad y utilidad culinaria**, con medidas reproducibles, ejemplos revisables y decisiones editoriales trazables, sin alterar todavía el formato canónico.

### Unidad A — Inventario actual y medición reproducible

- Comprobar primero los comandos, herramientas y contratos ya existentes, reutilizando la auditoría vigente donde sea posible, sin crear un segundo sistema de métricas.
- Fijar commit, definición de denominadores, fecha y alcance para recetas, ingredientes, técnicas, relaciones y estado de validación editorial.
- Distinguir métricas automáticas estructurales de indicadores que requieren revisión humana; los desconocidos permanecen como desconocidos.
- Contrastar duplicidades documentales aparentes sin suprimir variantes útiles o versiones mejores.
- Entregar informe reproducible con limitaciones, sin declarar una mejora de madurez antes de obtener los resultados.

### Unidad B — Muestra editorial y recorrido de uso

- Seleccionar una muestra **estratificada y acotada**: recetas tradicionales, preparaciones realizadas, pendientes de prueba, platos con varias versiones y diferentes dominios.
- Fijar antes de revisar los criterios de suficiencia: ingredientes y cantidades declaradas, pasos claros, rendimientos, condiciones críticas, evidencia de prueba, contexto y enlace a fuentes.
- Recorrer desde Explorer y Assistant hasta la ficha canónica para evaluar problemas concretos de recuperación y preparación.
- Registrar casos positivos, deficiencias y abstenciones; la ausencia de información no se completa por suposición.

### Unidad C — Intervención editorial piloto

- Resolver solo defectos comprobados y de alto impacto, en tandas pequeñas con PR independientes.
- Respetar la regla editorial: conservar la mejor versión, documentar variantes y separar recetas nuevas de reescrituras. Marcar `pendiente de probar` cuando proceda.
- Comparar resultados con la línea base utilizando los mismos criterios, sin promocionar automáticamente identidades candidatas ni requisitos inferidos.
- Detener o reformular si el coste de revisión no produce una mejora clara de utilidad o trazabilidad.

### Unidad D — Decisión de capacidad posterior

- Contrastar la utilidad real del piloto y sus limitaciones antes de seleccionar filtros avanzados, semántica, otro módulo o infraestructura.
- Entregar recomendación y evidencia, no publicación automática ni roadmap cerrado de funcionalidades.

## Puertas de decisión

- **QG-01:** la línea base identifica commit, corpus, definiciones y denominadores; no mezcla cortes históricos y presentes.
- **QG-02:** las cifras estructurales no se presentan como pruebas de calidad o seguridad culinaria.
- **QG-03:** ningún cambio editorial pierde la mejor formulación verificada ni sobreescribe variantes sin motivo registrado.
- **QG-04:** las etiquetas de experiencia personal, fuentes, incertidumbre y pruebas pendientes no se inventan.
- **QG-05:** muestras e indicadores se fijan antes de comparar resultados; los defectos se pueden enlazar con fichas concretas.
- **QG-06:** el siguiente salto de capacidad requiere revisión y aprobación explícita a partir de beneficios observados.

## Recomendación y límites de autorización

**Recomendar comenzar por Unidad A**, reutilizando las herramientas de auditoría del repositorio y produciendo un corte medible de calidad y cobertura. Esta revisión es **una propuesta de dirección**: la fusión del documento no equivale a autorizar todas las unidades, un cambio de modelo, una release o un backend. Cada incremento debe desarrollarse en rama temática y PR revisada y fusionada por el propietario.

Mantener las cinco aplicaciones y sus datos locales tal como están, atender defectos reproducibles y no incorporar automatización de nutrición, seguridad alimentaria, sustituciones o cocinabilidad sin evidencia y decisión separadas. La versión publicada permanece en `v1.6.0`.

## Referencias

- [Estado del proyecto](./PROJECT_STATUS.md)
- [Roadmap](./ROADMAP.md)
- [Cierre de aplicaciones](./REVISION_ESTRATEGICA_APLICACIONES_CULINARIAS.md)
- [Aceptación pública](./PROTOCOLO_ACEPTACION_PUBLICA_CULINARIA.md)
- [Revisión estratégica culinaria anterior](./REVISION_ESTRATEGICA_CULINARIA.md)
- [Deuda de requisitos culinarios](./DEUDA_REQUISITOS_CULINARIOS.md)
- [Kit de continuidad](./NOVACOQUINARIA_KIT_CONTINUITY.md)


## Unidad A — Corte de línea base técnica (22-11-2026)

Se incorpora la [línea base de calidad culinaria](./LINEA_BASE_CALIDAD_CULINARIA.md) mediante reutilización de los resultados observados en [Knowledge audit #300](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/45046377378), proyección fijada a `7bc20e9a019d95445a13f59b109d52185c450a18`. El informe distingue cobertura extraída de evaluación humana e identifica explícitamente los denominadores, los límites de los estados de preparación y la discrepancia entre alguna duración numérica y un total temporal único.

Es una **línea base descriptiva reproducible**, no una mejora ya demostrada de calidad, una nueva herramienta de auditoría ni una aprobación automática del piloto editorial. La decisión sobre Unidad B requerirá seleccionar y fijar la muestra antes de evaluarla, conservando la mejor versión de cada receta y las variantes documentadas. La release publicada continúa siendo `v1.7.0`.


## Unidad B — Protocolo de muestra editorial fijado (22-11-2026)

La [muestra editorial de calidad culinaria](./MUESTRA_EDITORIAL_CALIDAD_CULINARIA.md) fija ocho recetas cuyas rutas canónicas fueron verificadas, junto con ocho ejes de revisión, una escala descriptiva y reglas de evidencia antes de emitir valoraciones. La selección es dirigida, no estadísticamente representativa: cubre cinco módulos y excluye explícitamente otros cinco. La revisión de fichas completas y el registro de hallazgos deben realizarse en una PR posterior, sin reescrituras ni conclusiones anticipadas. Se mantiene la release `v1.7.0`.


## Unidad C — Cierre técnico acotado (22-11-2026)

El [cierre del piloto editorial](./CIERRE_PILOTO_CALIDAD_CULINARIA.md) documenta seis intervenciones implementadas y fusionadas en #343 y #344, dos controles sin intervención y la prueba E07 de ocho recorridos individuales en Chromium local de #345, cuyo workflow concluyó satisfactoriamente. No se equipara ese test con aceptación pública manual ni se afirma una nueva prueba doméstica de los platos.

La Unidad C se considera **Complete — Bounded Editorial & Local Browser Validation**, dentro de ese alcance. La propuesta siguiente es una decisión estratégica de Unidad D, sujeta a revisión independiente y sin autorizar por sí misma otra release o funcionalidad.
