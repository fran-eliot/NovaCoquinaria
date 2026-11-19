---
id: DOC-REVISION-ESTRATEGICA-CULINARIA-2026
titulo: Revisión estratégica global del conocimiento culinario
tipo: gestion
version: 0.2.0
estado: borrador
ultima_revision: 2026-11-19
---

# Revisión estratégica global

## Corte y evidencia

Main tras [PR #247](https://github.com/fran-eliot/NovaCoquinaria/pull/247): `fe53c5d93e1124b6579a2f32a1c4b1f7f5804528`. Sin PR abiertas en la consulta; release v1.5.0. Knowledge integrity, Knowledge audit y Deploy MkDocs del HEAD finalizaron correctamente ([integridad](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44525950968), [auditoría](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44525951341), [publicación](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/44525950988)).

El corte documentado de #246 registra 590 recetas, 5.047 ocurrencias de ingredientes, 36 identidades explícitas, 1.044 ocurrencias con candidato y 3.967 sin resolver ni candidato; 102 pruebas, 18 casos textuales y cero advertencias semánticas y huérfanos según las reglas existentes. Son resultados históricos, no una auditoría individual de los artefactos ni evidencia de elaboración doméstica. El motor 0.2.0 admite text, terms, explicit y candidate; no interpreta disponibilidad, negaciones ni alternativas. Los 72 candidatos experimentales permanecen sin integrar.

## Diagnóstico

La recuperación de menciones es útil, pero no equivale a disponibilidad. La visión del SGCC exige reutilización práctica con Markdown canónico, separación de automatización y consumo, trazabilidad y simplicidad. El corpus permite estudiar una capacidad funcional sin seleccionar infraestructura de plataforma.

## Alternativas

| Alternativa | Valor | Dependencia o riesgo |
|---|---|---|
| Identidades como ciclo independiente | Alto | Cobertura no equivale a precisión; gobernanza de reglas |
| Compatibilidad acotada receta-despensa | Muy alto | Identidades, opcionalidad, incertidumbre |
| Filtros de tiempo y rendimiento | Alto | Solo 101 recetas con total numérico único en el corte #235; unidades y calificadores |
| Acceso práctico de solo lectura | Alto | Facilita consumo, no resuelve semántica |
| Escalado de cantidades | Alto | Unidades, rendimientos, proporciones y excepciones |
| Menús y compra inteligente | Alto | Requiere compatibilidad, cantidades y preferencias |
| RAG y agentes | Potencial alto | No sustituye contratos ni evaluación |

Valoración cualitativa, no resultado experimental. Se recomienda investigar compatibilidad acotada como caso de uso que oriente el refinamiento de identidades. El trabajo de identidad independiente y los filtros declarados se mantienen como alternativas si la viabilidad resulta insuficiente.

## Capacidad candidata: Culinary Compatibility Engine

Consumidor determinista de solo lectura del índice derivado y una lista declarada de ingredientes disponibles. Separar identidad explícita, candidato y coincidencia textual. No promover automáticamente candidatos, interpretar ausencia de datos como falta de ingrediente ni asumir que una lista parcial es exhaustiva. Distinguir requerido, opcional e indeterminado y conservar alternativas compuestas sin inferencia automática. Diferenciar presencia declarada, ausencia explícita bajo un inventario cerrado, incertidumbre y cantidad no comprobada. No declarar una receta cocinable por mera coincidencia textual, ni recomendar sustituciones o inferir seguridad alimentaria. Conservar fuente, commit, posición y motivos de cada resultado. Cualquier puntuación futura deberá explicitar denominador e incertidumbre y validarse antes de adoptarse.

## Investigación propuesta

- [CCE-D01: casos de uso, entradas, fronteras y criterios de evaluación](./INVESTIGACION_COMPATIBILIDAD_CULINARIA.md).
- CCE-D02: contraste de identidades, revisión individual de los 72 candidatos y gobernanza de reglas; analizar si cubren casos de uso relevantes.
- CCE-D03: alternativas de representación y compatibilidad, estados desconocidos, política de inventario abierto/cerrado y opcionalidad.
- CCE-D04: experimento aislado con corpus fijado, expectativas documentales independientes, negativos y casos ambiguos; comparar con recorrido de referencia, medir abstenciones y errores, sin extrapolar precisión global.
- CCE-D05: síntesis de evidencia y decisión de viabilidad, incluyendo alternativa de no entrega.

Una eventual entrega requerirá alcance, criterios de aceptación y decisión diferenciada. No se autoriza implementación productiva, cambio de arquitectura, persistencia, API, ranking, gestor de despensa, escalado, planificación, IA ni release. La evolución del conocimiento sigue abierta.

## Referencias

- [Visión](../VISION.md)
- [Manifiesto](../../MANIFESTO.md)
- [Arquitectura](../architecture/ARQUITECTURA.md)
- [Roadmap](./ROADMAP.md)
- [Kit de continuidad](./NOVACOQUINARIA_KIT_CONTINUITY.md)
- [Consolidación](./CONSOLIDACION_CONOCIMIENTO.md)
- [Evolución de recuperación](./EVOLUCION_RECUPERACION_CULINARIA.md)
- [Contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md)

## Revisión de explotación práctica — corte posterior a #268

Main: `9e9c291376e68299e92228e1434798f640787462`; #268 fusionada, sin PR abiertas en la consulta. Tag v1.6.0 verificado sobre `836f02e848299c0a7a7897b22bb83cd13e0c373a`. Los resultados de CI del merge #267 son históricos; no se acreditan aquí los workflows de push de #268.

CCE, CRM y CRR concluyeron con evidencia acotada y entrega diferida. CCE no permitió clasificar como cocinable ninguna de las 590 recetas sin confirmaciones; CRM representó 16 casos dirigidos y CRR acertó seis de diez positivos reservados. La [deuda de requisitos](./DEUDA_REQUISITOS_CULINARIOS.md) se conserva sin promoción automática. No resulta necesario resolverla para facilitar la consulta cotidiana.

### Alternativas y dirección propuesta

| Capacidad | Utilidad cotidiana | Dependencias | Prioridad propuesta |
|---|---|---|---|
| Explorador culinario interactivo de solo lectura | Muy alta | Índice y consultas publicados; publicación y acceso | Primero |
| Filtros de tiempo y rendimiento declarado | Alta | Cobertura parcial; desconocidos visibles | Incremento posterior de exploración |
| Escalado asistido | Alta | Rendimientos, unidades, excepciones | Después, con alcance limitado |
| Despensa personal y sugerencias por menciones | Muy alta | Estado de usuario y semántica explícita | Posterior; no afirmar compatibilidad |
| Menús y listas de compra | Alta | Selección, cantidades y agregación | Posterior |
| Compatibilidad automática, RAG y agentes | Potencial alto | Evidencia insuficiente o infraestructura adicional | Diferido |

Valoración cualitativa por utilidad, reutilización y coste de dependencias, no medición de usuarios.

### Culinary Explorer — primera entrega funcional candidata

Una aplicación consumidora de solo lectura, preferentemente integrada en el portal MkDocs existente si el mecanismo de publicación lo permite. El usuario puede buscar recetas por título e ingredientes mencionados, seleccionar módulo, consultar evidencia doméstica y abrir la ficha fuente. La proyección publicada es derivada, regenerable y vinculada al commit; Markdown conserva la autoridad. La interfaz reutiliza la semántica de consultas 0.2.0 y evita un segundo motor divergente. Si la implementación estática requiere un adaptador, se delimitará y contrastará con el motor de referencia.

No interpretar mención como disponibilidad, candidato como identidad confirmada, ni ausencia de coincidencia como ausencia real. No declarar cocinabilidad, sustituciones o seguridad. No asumir que una receta propuesta ha sido elaborada. Los tiempos y rendimientos pueden mostrarse como declaraciones de fuente sin inferencia; los filtros y escalado quedan fuera del primer alcance salvo decisión expresa.

### Enfoque de entrega

1. Alcance breve y criterios de aceptación: recorridos de consulta, contrato de proyección derivada, equivalencia de resultados, rutas publicadas y tratamiento de desconocidos.
2. Implementación de generación reproducible y acceso de solo lectura; preservar contratos y pruebas existentes.
3. Interfaz funcional adaptada a móvil y escritorio, con búsqueda, filtros básicos, resultados, enlaces y estado sin resultados.
4. Integración con publicación, pruebas de equivalencia y validación de recorridos; cierre con evidencia y limitaciones.

No se establece un nuevo ciclo de discovery independiente. La investigación se limita a obstáculos concretos de implementación. La evolución editorial continúa de forma selectiva y las mejoras semánticas se guían por casos de uso reales. No se selecciona backend, persistencia, framework de aplicación, API ni nueva release. La adopción del alcance y la implementación quedan sujetas a la decisión posterior a esta revisión.

El [alcance de entrega de Culinary Explorer](./ALCANCE_CULINARY_EXPLORER.md) concreta la propuesta en criterios y unidades de implementación.
