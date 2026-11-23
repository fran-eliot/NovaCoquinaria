---
id: DOC-RA-INTEGRACION-2026-11
titulo: Revisión de integración de Recipe Assistant — corte 23-11-2026
tipo: gestion
version: 0.1.0
estado: revision-estatica-acotada
ultima_revision: 2026-11-23
---

# Revisión de integración de Recipe Assistant — 23-11-2026

## Alcance y evidencia

Revisión estática dirigida del código de `assets/recipe-assistant-ui.mjs`, `assets/recipe-assistant-session.mjs`, `assets/recipe-assistant-feedback.mjs`, la plantilla `tools/templates/recipe-assistant.html` y el recorrido `tools/check_recipe_assistant_browser.py`, tras la fusión de [PR #402](https://github.com/fran-eliot/NovaCoquinaria/pull/402). No se ha realizado en este documento una nueva sesión manual de aceptación en el sitio público.

La [PR #401](https://github.com/fran-eliot/NovaCoquinaria/pull/401), fusionada antes de #402, concluyó con los tres workflows de PR en `success` después de corregir pruebas de regresión del portapapeles. La revisión de integración no convierte ese resultado en prueba de una elaboración real ni en cobertura exhaustiva de navegadores.

## Hallazgos

| Área | Comprobación y resultado | Decisión |
|---|---|---|
| Progreso de ingredientes | El restablecimiento independiente desactiva `#reset-ingredients` al quedar sin marcas, pero la interfaz intentaba enfocar ese botón desactivado. Hallazgo reproducible mediante inspección del flujo `resetIngredients() → progress() → focus()`. | Corregir en esta PR: foco al encabezado `#ingredients-heading` con `tabindex=-1`, más aserciones de Chromium. |
| Progreso de pasos | El restablecimiento independiente ya enfoca `#step-title` (corregido en #399); el selector y las barras se actualizan a partir del estado de sesión. | Conservar; comprobar regresiones en CI. |
| Estado del temporizador | El reloj manual diferencia ejecución, pausa, finalización y cancelación; los controles de los pasos no lo modifican, salvo el reinicio completo. | Conservar separación; la suspensión de pestañas y bloqueos del dispositivo siguen siendo una limitación declarada. |
| Filtro de pendientes | Las filas marcadas y los encabezados de grupo sin elementos visibles se ocultan únicamente en la vista de ingredientes; Shopping mantiene una selección distinta. | Conservar; verificar visualmente los estados vacíos en móvil. |
| Registro de observaciones | El módulo exporta/copía Markdown de forma voluntaria. La copia asíncrona conserva el estado exacto copiado; el aviso de cambios sin exportar compara los campos con ese estado. | Conservar; la advertencia de salida no garantiza recuperación de notas. |
| Fuente y semántica | La página recupera fichas derivadas del Markdown; las marcas temporales no constituyen evidencia de cocinado ni se escriben a las fichas. | Mantener distinción entre receta, declaración personal y propuesta pendiente de probar. |

## Verificación y límites

Esta PR añade dos aserciones al recorrido Chromium existente sobre el retorno del foco tras restablecer ingredientes. La aprobación queda **condicionada a CI**, sin afirmar que las pruebas hayan pasado antes de ejecutarse.

Quedan fuera del alcance de esta revisión estática: una auditoría WCAG completa, pruebas manuales con lectores de pantalla, ejecución en navegadores distintos de Chromium, prueba en un dispositivo móvil real, verificación manual integral del sitio público, comprobación de seguridad alimentaria y pruebas culinarias reales.

## Propuesta de cierre

Una vez CI resulte satisfactorio, revisar manualmente en escritorio y móvil al menos: apertura desde Explorer, filtrado y restablecimientos, selección y navegación de pasos, temporizador, copia/descarga de observaciones, advertencia de salida y acceso a la receta fuente. Registrar los resultados antes de proponer una release posterior a v1.7.0. No publicar automáticamente una nueva versión.

## Ampliación de cobertura responsive — matriz automatizada

Tras la fusión de [PR #403](https://github.com/fran-eliot/NovaCoquinaria/pull/403) y sus tres workflows satisfactorios, el recorrido de `tools/check_recipe_assistant_browser.py` se amplía con una matriz de anchos CSS de **320, 390, 768 y 1280 px** en Chromium. Para cada ancho verifica el contenedor del asistente, barras de progreso, filtro, selector y enlaces a las cuatro secciones, así como la ausencia de desbordamiento horizontal del documento. A 390 px incluye navegación por ancla y selección de un paso con retorno del foco al título.

Esta matriz es **automatización de navegador con viewport simulado**, no validación en dispositivos móviles físicos ni revisión visual exhaustiva. Su resultado se conocerá tras el CI de la PR que introduce la cobertura. No sustituye las tareas manuales pendientes del apartado anterior: lectores de pantalla, navegador móvil real, interacción táctil, legibilidad de textos largos, portapapeles y descargas reales ni aceptación de la URL pública.
