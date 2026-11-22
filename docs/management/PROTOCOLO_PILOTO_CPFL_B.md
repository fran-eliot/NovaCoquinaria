---
id: DOC-CPFL-B-PROTOCOLO-2026
titulo: Culinary Preparation Feedback Loop — protocolo de piloto CPFL-B
tipo: gestion
version: 0.1.0
estado: protocolo-preparado-sin-ejecucion
ultima_revision: 2026-11-22
---

# Culinary Preparation Feedback Loop — protocolo de piloto CPFL-B

## Punto de partida y alcance

Este documento establece **antes de recibir una nueva observación** cómo evaluar la utilidad del contrato editorial [CPFL-A](./CONTRATO_FEEDBACK_PREPARACIONES_CPFL_A.md). La PR #355 quedó fusionada en `fdae1dbaa2700072ed66210e0fe0fcbd60f03cb4` y sus tres workflows finalizaron correctamente. Este es un protocolo, **no un registro de cocina, una prueba de usuario ejecutada ni una autorización de desarrollo de interfaces**.

La condición de entrada es una **nueva preparación real comunicada voluntariamente por el propietario**. No se elige una receta histórica para simular ese hecho. Tampoco se deduce que se haya cocinado recientemente por estar documentada, por aparecer en el explorador o por solicitar continuar el proyecto.

## Diseño del piloto

- **Tamaño:** una preparación real, de una receta ya existente en el repositorio; sin objetivo estadístico.
- **Fuente:** ficha Markdown con ID, ruta y versión verificables, fijada antes de editar.
- **Observación mínima:** descripción de lo que se hizo realmente y del resultado, incluso si solo se recuerda aproximadamente. Cantidades, fecha, tiempos y valoración cuantitativa son opcionales y nunca se inventan.
- **Distinción obligatoria:** preparación confirmada / recuerdo parcial / propuesta no probada / dato desconocido. Las mejoras de una próxima ejecución se separan del resultado observado.
- **Intervención:** como máximo una ficha canónica modificada mediante PR temática; cambios exclusivamente relacionados con la experiencia comunicada, sin reestructurar el recetario.
- **Comparación:** revisar versión de partida, resultado observado, formulación actual y variantes. No sustituir una versión mejor documentada solo por ser más antigua.

## Captura conversacional mínima

Cuando exista una elaboración nueva, bastan inicialmente **dos preguntas abiertas** (no un formulario obligatorio):

1. **¿Qué receta preparaste y qué cambiaste respecto a la ficha, si cambiaste algo?**
2. **¿Cómo salió y qué merece la pena conservar o corregir?**

Preguntar por peso, tiempo, equipo o condiciones **solo si el propietario los recuerda o son determinantes para explicar el resultado**. El propietario puede informar un resultado negativo, parcial o sin valoración. No inferir confirmaciones del silencio.

## Recorrido de comprobación

| Etapa | Acción | Evidencia de salida |
|---|---|---|
| B-01 · Entrada | Comunicación explícita de una preparación real posterior al contrato | Narración atribuida, con fecha solo si se conoce |
| B-02 · Referencia | Verificar ID, ruta, versión y sección existente en Markdown | Referencia canónica fijada |
| B-03 · Observación | Separar hechos de propuestas, y declarar lo desconocido | Nota editorial opcional, sin duplicados |
| B-04 · Comparación | Confrontar receta/variante anterior y resultado nuevo | Decisión de mantener, añadir variante o ajustar |
| B-05 · Integración | PR mínima, revisión humana y CI | Diferencia verificable en una sola ficha |
| B-06 · Aprendizaje | Valorar esfuerzo y utilidad del procedimiento | Informe de piloto con resultado y límites |

No abrir una PR que diga que se ha ejecutado B-01–B-06 mientras falte B-01. CI satisfactorio no acredita haber cocinado ni validación gastronómica. El propietario conserva revisión, fusión y eliminación de la rama remota.

## Criterios de aceptación antes de la ejecución

- **AC-01:** se identifica una preparación **real** sin apropiarse de datos de otra receta ni de una propuesta.
- **AC-02:** los datos ausentes permanecen como `no documentado`; fecha del mensaje y fecha de revisión no se interpretan como fecha de cocina.
- **AC-03:** una valoración, favorable o desfavorable, conserva su matiz original; no se inventan estrellas o puntuaciones.
- **AC-04:** la variante mejor documentada se conserva; una experiencia peor no reemplaza automáticamente la versión preferida.
- **AC-05:** se registra una decisión útil y proporcionada en una ficha, o se justifica no editar si no hay mejora demostrada.
- **AC-06:** la revisión y CI de la PR no se describen como evidencia de cocción.
- **AC-07:** el flujo editorial puede ejecutarse sin app nueva, datos sincronizados, campos obligatorios o permisos de escritura desde el navegador.

## Resultado posible y límites

- **Piloto satisfactorio:** una elaboración real permite incorporar o confirmar una mejora trazable con esfuerzo aceptable, sin perder la mejor versión.
- **Piloto sin cambio de receta:** experiencia real documentada, pero no hay razón suficiente para modificar la ficha; sigue siendo un resultado útil.
- **Piloto no evaluable:** información insuficiente o ausencia de una nueva preparación; registrar el motivo sin inventar datos.
- **Piloto desfavorable:** la nota añade confusión, duplica texto o dificulta comparar versiones; revisar CPFL-A antes de proponer una interfaz.

**Estado actual: PREPARED — NOT EXECUTED.** Las tres experiencias históricas de CPFL-A sirven como ejemplos del contrato, **no** como ejecuciones de este piloto.

## Decisión posterior

CPFL-C (posibles funciones de Recipe Assistant) no deberá iniciarse por haber redactado este protocolo; requiere primero una observación auténtica, el contraste del recorrido completo y una necesidad funcional repetida o demostrable. No hay aprobación de backend, automatización, telemetría, publicación ni nueva release. Última release publicada: `v1.7.0`.
