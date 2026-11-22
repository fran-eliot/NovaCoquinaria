---
id: DOC-CPFL-A-2026
titulo: Culinary Preparation Feedback Loop — contrato mínimo y viabilidad CPFL-A
tipo: gestion
version: 0.1.0
estado: diagnostico-documental
ultima_revision: 2026-11-22
---

# Culinary Preparation Feedback Loop — CPFL-A

## Alcance y corte verificado

CPFL-A es un **diagnóstico documental**, no un sistema de capturas, una interfaz nueva ni una aprobación de piloto con nuevas preparaciones. Se prepara después de la fusión de [PR #354](https://github.com/fran-eliot/NovaCoquinaria/pull/354) en `c3d06123def16c908bf917488b1ae893e8bbcfca`, con `Knowledge integrity`, `Knowledge audit` y `Culinary Explorer site` satisfactorios. La [decisión RPC-D](./DECISION_PRODUCTO_RPC_D.md) recomendó reutilizar Markdown y comenzar exclusivamente por CPFL-A.

Los tres ejemplos que siguen fueron leídos en el Markdown canónico de ese corte. Las observaciones pueden ser **históricas**, **propuestas** o **desconocidas**. No se presentan como nuevas elaboraciones ni como datos medidos con posterioridad.

## Inventario de estructuras ya disponibles

Los documentos actuales no comparten un formato único de historia culinaria, pero sí ofrecen recursos suficientes para un flujo editorial manual:

| Recurso documental | Ejemplo canónico comprobado | Función posible |
|---|---|---|
| `Estado de experiencia doméstica` | `REC-0007`, `REC-0009` | Diferenciar una preparación declarada de la receta de referencia y de sus lagunas |
| `Evolución de la receta doméstica` | `REC-0079` | Preservar versión anterior, adaptación y resultado de un ensayo real |
| `Variantes` y `Puntos críticos` | `REC-0079`, `REC-0007`, `REC-0009` | Mantener alternativas sin sustituir silenciosamente una versión mejor |
| `Diagnóstico` y `Ajustes y próximas pruebas culinarias` | `REC-0079` | Registrar observación negativa, causa incierta y propuesta aún no probada |
| Front Matter: `id`, `version`, `ultima_revision` | Las tres fichas | Localizar receta y edición; **no equivalen a una fecha de cocinado** |
| Plantillas vinculadas | Salsa china base en `REC-0007`, salsa teriyaki base en `REC-0009` | Distinguir referencia culinaria de cantidades efectivamente utilizadas |

La variedad de secciones es legítima: **no exigir una migración uniforme** de las 590 recetas ni añadir campos obligatorios en esta fase. La fuente canónica sigue siendo Markdown. El código de extracción y sus estados `prepared`, `pending`, `unknown` **no se modifican** ni adquieren significado adicional por la existencia de esta guía.

## Contrato mínimo de observación opcional

Al recibir una observación sobre una preparación, el responsable editorial debe poder identificar:

| Campo de lectura | Requisito mínimo | Cuando falta |
|---|---|---|
| **Referencia** | ID y ruta canónica, con versión de partida cuando sea conocida | Verificar la ficha antes de proponer cambios; no suponer versión |
| **Procedencia** | Distinguir declaración de quien cocinó, recuerdo histórico, referencia externa y propuesta editorial | Mantener `desconocido`; no atribuirlo al propietario |
| **Hecho culinario** | Qué se hizo realmente, a qué preparación se refiere y con qué grado de certeza | «Preparación no confirmada»; no usar lenguaje de resultado observado |
| **Diferencias** | Solo las cantidades, productos, pasos, tiempos o sustituciones que constan expresamente | Mantener valor `no documentado`; no completar a partir de la receta publicada |
| **Resultado** | Valoración textual o problema descrito, conservando matices y atribución | Sin valoración; no calcular puntuación |
| **Decisión editorial** | Conservar versión preferida, añadir variante, corregir error documental o dejar pendiente | No reemplazar la mejor versión por la más reciente |
| **Seguimiento** | Registrar pregunta o propuesta futura **separada** de lo efectivamente probado | Marcar `pendiente de probar`, sin fechar una ejecución inexistente |

**Fecha de preparación** y **condiciones observadas** son opcionales: la fecha de edición o del mensaje **no se convierte** en fecha de cocción. La ausencia de peso, tiempo, temperatura, utensilio, lote o número de comensales nunca se compensa con una cifra estimada, salvo que la estimación quede rotulada como propuesta y no como observación.

Los estados de **hecho culinario** (`confirmado_por_declaracion`, `recuerdo_parcial`, `no_confirmado`) son *etiquetas de trabajo de revisión editorial*, **no** un nuevo enum de Front Matter, proyección o API. El resultado culinario no se usa para certificar seguridad alimentaria.

### Esquema de nota para copiar durante una revisión editorial

Este modelo es **opcional y de texto libre**. No es una receta adicional ni una especificación de almacenamiento:

```markdown
### Observación de preparación [identificador local si procede]

- Receta de referencia: REC-… (ruta y versión, si se conocen)
- Procedencia: declaración / recuerdo histórico / fuente externa / propuesta
- Fecha efectiva de elaboración: no documentada [o fecha confirmada]
- Preparación realizada: hecho confirmado / recuerdo parcial / no confirmado
- Cantidades, tiempos y condiciones **observados**: solo los comunicados
- Resultado y valoración: palabras originales o paráfrasis fiel
- Diferencias con la ficha: únicamente las que se conocen
- Mejor versión y variantes: conservar / comparar / aún sin determinar
- Ajuste propuesto **pendiente de probar**: …
- Incertidumbres y próxima pregunta: …
```

No crear este bloque en todas las fichas automáticamente. Cuando corresponda, integrar solo los elementos pertinentes en las secciones existentes, con revisión humana y PR específica. Evitar duplicar narrativas históricas presentes.

## Tres contrastes documentales históricos

### CPFL-E01 — Pastel de manzana `REC-0079`

**Fuente:** `08_Postres/pastel_de_manzana.md`, secciones «Evolución de la receta doméstica», «Distribución de la manzana», «Puntos críticos», «Variantes» y «Ajustes y próximas pruebas culinarias»; versión `1.0.2`.

- **Hecho documentado:** adaptación doméstica con **840 g de manzana neta** y **200 g reservados** para superficie; se probó *lemon curd* con agua para aligerarlo, perdió consistencia y apareció líquido en la base, resultado descrito como poco agradable.
- **Incertidumbre explícita:** no está demostrado que la dilución sea la única causa del líquido acumulado; no consta un tiempo de horno real confirmado para la formulación actual.
- **Propuesta, no ejecución:** sustituir por **mermelada espesa sin añadir agua**, aplicada tras hornear y dejar asentar.
- **Regla editorial:** conservar el resultado negativo como evidencia; no etiquetar la mermelada como probada ni interpretar la fecha de revisión como fecha de preparación.

### CPFL-E02 — Hamburguesa asiática `REC-0007`

**Fuente:** `05_Carnes/hamburguesa_asiatica.md`, «Estado de experiencia doméstica», «Repetición de la hamburguesa asiática individual», «Ingredientes / Salsa»; versión `1.0.4`.

- **Hecho declarado:** se prepararon dos hamburguesas de **200 g de ternera muy magra cada una**, una asiática y otra especiada, con valoración global **muy satisfactoria** para la asiática.
- **Límites:** no se recuperaron dosis exactas de condimentos, tiempos reales ni todos los detalles del montaje. Los **400 g** de carne de la ficha para dos hamburguesas asiáticas son una **formulación de referencia** y no describen dos unidades asiáticas de aquella tanda.
- **Propuesta, no ejecución:** ajustar condimentos aproximadamente a la mitad para repetir la versión individual, verificar el punto de carne picada y registrar dosis en un nuevo ensayo. La salsa china base enlazada no confirma la salsa utilizada entonces.
- **Regla editorial:** preservar la valoración declarada sin atribuir una ejecución idéntica a la formulación vigente.

### CPFL-E03 — Caballa japonesa `REC-0009`

**Fuente:** `06_Pescados_y_Mariscos/caballa_japonesa.md`, «Estado de experiencia doméstica», «Ingredientes / Salsa» y «Elaboración»; versión `1.0.3`.

- **Hecho declarado:** caballa japonesa preparada en casa y recordada como **muy satisfactoria**.
- **Límites:** cantidades de salsa, tiempos reales, grosor de lomos y evaluación detallada de textura **no documentados**. Los 25 minutos de la ficha son orientación, no medida de esa elaboración.
- **Propuesta, no ejecución:** usar una cantidad pequeña de salsa teriyaki preparada y añadir gradualmente; anotar tiempos y glaseado en otra ocasión.
- **Regla editorial:** no confundir proporción de la plantilla para 2–3 raciones con volumen consumido en la preparación histórica.

## Flujo editorial mínimo

1. **Entrada voluntaria:** el propietario aporta una observación real, recuerdo o ajuste propuesto. No se recolectan notas del navegador, Pantry, Shopping o Planner de forma automática.
2. **Identificación:** localizar ID, ruta, versión y sección existente en Markdown; comprobar si el relato ya está documentado para evitar duplicados.
3. **Clasificación de procedencia:** separar hechos confirmados por declaración, memoria parcial, interpretación y propuesta aún no probada.
4. **Comparación:** contrastar con la última formulación y variantes sin asumir que una versión posterior sea mejor.
5. **Edición mínima:** decidir si se incorpora una observación, mejora o variante en la propia ficha; evitar cambios masivos, fechas o cantidades inventadas.
6. **Revisión y CI:** abrir PR temática para que el propietario la revise, fusione y elimine la rama. El CI valida integridad documental, **no** acredita el resultado de cocinar.
7. **Cierre de aprendizaje:** solo después de nueva elaboración real se podrá contrastar un cambio propuesto; registrar resultado favorable, desfavorable o incierto.

## Viabilidad y decisiones pendientes

| Capacidad | Viabilidad evidenciada | Límite o decisión |
|---|---|---|
| Conservar recuerdos históricos y mejoras | **Viable documentalmente:** los tres ejemplos ya contienen narrativas de procedencia y variantes | No hay necesidad demostrada de otro esquema de datos |
| Revisión humana por PR | **Viable operativamente** por la metodología del repositorio | El coste real de capturar cada observación no se ha medido |
| Plantilla de notas opcional | **Viable como guía editorial**, sin código | Debe probarse con una observación **nueva y real** antes de hacerla obligatoria |
| Medir mejora por preparación | **No demostrado** por los ejemplos históricos | Requiere elaboración posterior y comparación honesta |
| Exportación desde Recipe Assistant | **No evaluada** | CPFL-C condicionada a repetición de una necesidad; no autorizada |
| Datos personales sincronizados, sugerencias automáticas o scoring | **No evidenciado** | No implementar ni atribuir validez culinaria |

### Protocolo recomendado para CPFL-B, sujeto a aprobación

Seleccionar **una sola nueva preparación real**, cuando exista y el propietario desee documentarla, y recoger únicamente datos que realmente pueda recordar o medir. Registrar las lagunas como `no documentado`. Comprobar si la nota mínima permite actualizar la ficha sin empeorar su versión preferida ni ocultar variantes. Evaluar utilidad práctica y esfuerzo antes de aumentar alcance. **Si no existe nueva experiencia, abstenerse; no inventarla ni presentar los tres casos históricos como ensayo CPFL-B.**

**Decisión CPFL-A:** el ciclo de feedback es **factible como proceso editorial asistido y trazable sin nueva infraestructura**. Se recomienda **considerar CPFL-B**, una sola preparación efectiva nueva y aprobada, pero ni el piloto, ni CPFL-C, ni una app, ni un nuevo release quedan autorizados por esta PR. Sigue publicada `v1.7.0`.


## CPFL-B — Protocolo previo a una observación nueva

El [protocolo CPFL-B](./PROTOCOLO_PILOTO_CPFL_B.md) fija un piloto de **una preparación real**, preguntas conversacionales mínimas, comparación de variantes y criterios de aceptación antes de cualquier captura. Su estado es **PREPARED — NOT EXECUTED**: no se ha comunicado una nueva experiencia para el piloto, no se ha editado ninguna receta y no se ha probado ninguna interfaz nueva. CPFL-C no queda autorizada.
