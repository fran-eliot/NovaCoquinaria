---
id: DOC-RA-ACEPTACION-MANUAL-2026
titulo: Protocolo de aceptación manual de Recipe Assistant
tipo: gestion
version: 0.1.0
estado: pendiente-de-ejecucion
ultima_revision: 2026-11-23
---

# Recipe Assistant — protocolo de aceptación manual

## Objeto y alcance

Este documento define una comprobación **manual, reproducible y aún no ejecutada** de la interfaz pública de Recipe Assistant, después de la integración de las mejoras de las PR #382–#404. Complementa la [revisión estática y responsive](./REVISION_INTEGRACION_RECIPE_ASSISTANT_2026_11.md) y el recorrido automatizado `tools/check_recipe_assistant_browser.py`. La superación de un CI no rellena automáticamente este protocolo.

**No cocinar para ejecutar las pruebas.** Las casillas, el reloj y las observaciones se pueden probar con datos ficticios expresamente identificados como prueba. No incorporar resultados ficticios al Markdown canónico ni afirmar una preparación real.

## Ficha de ejecución (rellenar solo tras probar)

| Dato | Valor |
|---|---|
| Fecha y hora de ejecución | Pendiente |
| Responsable de la comprobación | Pendiente |
| URL pública y origen (GitHub Pages, entorno o build) | Pendiente |
| Commit/release observada | Pendiente |
| Equipo y sistema operativo | Pendiente |
| Navegador y versión | Pendiente |
| Tamaño de pantalla/orientación | Pendiente |
| Estado general (PASS / FAIL / BLOCKED / NOT RUN) | NOT RUN |
| Evidencias o incidencias vinculadas | Ninguna aportada |

Para cada caso registrar **PASS**, **FAIL**, **BLOCKED** o **NOT RUN**, junto con dispositivo, pasos reproducibles y captura o evidencia cuando corresponda. Un fallo de funcionamiento o pérdida inesperada de datos requiere incidencia independiente; no convertirlo en PASS por comparación con CI.

## Preparación

1. Acceder al Explorador Culinario publicado y abrir Recipe Assistant desde «Preparar receta». Registrar el ID y la versión/commit de la ficha que se muestra; emplear preferentemente `REC-0017` (utilizada en Chromium) y una segunda receta con estructura distinta.
2. No reutilizar una sesión con cambios previos: comprobar inicialmente la página tras recarga. Cualquier observación escrita durante el protocolo será **ficticia / solo prueba** y se descartará.
3. Ejecutar la matriz al menos una vez en **escritorio** con teclado, y otra en **teléfono real**, usando interacción táctil. Repetir en un segundo navegador cuando esté disponible; documentar claramente lo que no se haya podido probar.
4. No utilizar ejemplos ficticios de elaboración como evidencia editorial y no activar ninguna publicación de recetas o release durante el protocolo.

## Matriz de aceptación

| Caso | Acción manual | Criterio de aceptación | Resultado |
|---|---|---|---|
| RA-M01 · Apertura y procedencia | Buscar una receta, abrir «Preparar receta» y seguir «Abrir ficha original completa». | Coinciden identidad, título y referencia; la ficha fuente abre correctamente. | NOT RUN |
| RA-M02 · Pantallas | Revisar en escritorio, móvil vertical y móvil horizontal, incluyendo receta con instrucciones largas. | Los textos y controles son legibles y utilizables sin desbordamiento horizontal ni solapamiento. | NOT RUN |
| RA-M03 · Navegación | Abrir enlaces de Ingredientes, Elaboración, Observación y Contexto; volver con teclado o táctil. | Los enlaces conducen a la sección prevista y el foco de teclado es visible. | NOT RUN |
| RA-M04 · Ingredientes | Marcar un ingrediente, activar «solo pendientes», desactivarlo y revisar progreso. | El marcado queda oculto solo por el filtro y reaparece conservando el estado; Shopping no cambia por ello. | NOT RUN |
| RA-M05 · Marcado conjunto | Marcar todos con confirmación; revisar vista vacía bajo filtro; desmarcar uno. | Progreso correcto, mensaje de estado vacío coherente y posibilidad de desmarcar individualmente. | NOT RUN |
| RA-M06 · Reinicio de ingredientes | Marcar ingredientes y un paso; restablecer solo ingredientes; cancelar y repetir confirmando. | Cancelar no altera nada; confirmar limpia solo ingredientes y devuelve foco al encabezado, sin tocar pasos ni reloj. | NOT RUN |
| RA-M07 · Pasos | Avanzar, retroceder, seleccionar directamente y saltar al primer pendiente. | Texto y número del paso concuerdan con el selector; las marcas se conservan al navegar. | NOT RUN |
| RA-M08 · Completar y siguiente | Marcar un paso, usar «Completar y siguiente» y comprobar progreso. | Se marca el paso adecuado y se avanza cuando existe uno posterior; no se acredita cocción real. | NOT RUN |
| RA-M09 · Reinicio de pasos | Completar dos pasos y marcar un ingrediente; cancelar y confirmar restablecimiento de pasos. | Se reinician solo las marcas de pasos y se conserva ingrediente, paso seleccionado y temporizador. | NOT RUN |
| RA-M10 · Temporizador | Iniciar un temporizador breve, pausar, reanudar y cancelar; probar fin natural. | Estados y controles coherentes; no se promete aviso fiable con pestaña suspendida o móvil bloqueado. | NOT RUN |
| RA-M11 · Observación provisional | Abrir registro de observación, redactar resultado de prueba, consultar vista previa. | No aparece HTML activo, se entiende la diferencia entre nota, hecho declarado y propuesta por probar. | NOT RUN |
| RA-M12 · Exportar | Copiar y descargar la nota Markdown; abrir el archivo y contrastar identidad, contenido y campos. | El texto copiado/descargado corresponde a lo introducido; no existe envío automático al repositorio. | NOT RUN |
| RA-M13 · Cambios no exportados | Modificar observación después de copiar; salir o recargar; volver a una versión ya copiada. | El aviso de salida funciona donde el navegador lo permita; desaparece al coincidir con la última versión exportada. | NOT RUN |
| RA-M14 · Limpiar observación | Completar campos y solicitar limpiar; primero cancelar y luego confirmar. | Cancelar conserva texto; confirmar descarta la nota y restablece el formulario. | NOT RUN |
| RA-M15 · Reinicio general | Marcar ingredientes y pasos, iniciar temporizador y ejecutar «Reiniciar preparación» con confirmación. | Se restablecen ingredientes, pasos, filtro y reloj; no se afirma persistencia entre recargas. | NOT RUN |
| RA-M16 · Transferencias | Abrir acciones de Planner y Shopping solo si el entorno está preparado; revisar la confirmación de salida. | Las selecciones se interpretan conforme a su función; no se infieren existencias en Pantry ni cantidades probadas. | NOT RUN |
| RA-M17 · Accesibilidad básica | Recorrer controles con Tab y Shift+Tab; operar casillas y selectores con teclado, revisar etiquetas y foco tras reinicios. | Ningún control queda atrapado; el foco no se pierde en botones desactivados y los campos son identificables. | NOT RUN |
| RA-M18 · Errores y recuperación | Abrir un enlace de receta inválido en un entorno de prueba sin editar datos canónicos. | Se muestra un error explicativo, no una receta o sesión incorrecta. | NOT RUN |

## Reglas de cierre

La decisión de aceptación manual es **PENDIENTE** hasta registrar una ejecución real por dispositivo y los resultados de cada caso. No marcar todo PASS por la existencia de los tests automatizados. Los casos BLOCKED o FAIL deben tener incidencia documentada y decisión de resolución o aceptación de riesgo; los NOT RUN impiden declarar aceptación manual completa.

**Condiciones previas a proponer release:**

- CI de la rama candidata y de su integración en `main` satisfactorio, con identificación del commit.
- Ejecución de los casos críticos RA-M01, RA-M04, RA-M06–RA-M10, RA-M12–RA-M15 y RA-M17, al menos en escritorio y teléfono real.
- Incidencias críticas cerradas y limitaciones conocidas documentadas. Cualquier excepción requiere una decisión de alcance explícita.
- Confirmación separada de la release vigente y autorización explícita del propietario para etiquetar/publicar otra versión.

No se presupone validación culinaria, auditoría WCAG completa ni pruebas exhaustivas de compatibilidad multiplataforma.
