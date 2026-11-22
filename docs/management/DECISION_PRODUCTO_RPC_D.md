---
id: DOC-RPC-D-DECISION-PRODUCTO-2026
titulo: Recipe Practical Completeness — decisión de producto RPC-D
tipo: gestion
version: 0.1.0
estado: propuesta-de-decision
ultima_revision: 2026-11-22
---

# Recipe Practical Completeness — RPC-D: decisión de producto y arquitectura

## Corte y fundamento

Esta decisión parte de `main` tras la fusión de [PR #353](https://github.com/fran-eliot/NovaCoquinaria/pull/353), commit `31e458401bb2f175faff2f82f8ca4a9f7a269245`. Los workflows `Knowledge integrity`, `Knowledge audit` y `Culinary Explorer site` de la PR concluyeron en `success`. No había otras PR abiertas al verificar el corte. La versión publicada sigue siendo **v1.7.0**.

La cadena RPC no constituye un experimento de uso independiente:

- **RPC-A:** [diagnóstico](./DIAGNOSTICO_RECIPE_PRACTICAL_COMPLETENESS.md) y contrato de lectura editorial de nueve ejes y cinco estados, sin clasificador de «receta cocinable».
- **RPC-B:** [selección previa](./MUESTRA_RPC_B_SUFIENCIA_PRACTICA.md) de diez fichas y [evaluación](./EVALUACION_RPC_B_SUFIENCIA_PRACTICA.md) documental dirigida en cinco módulos que faltaban en el primer piloto.
- **RPC-C:** [cierre técnico](./CIERRE_RPC_C_SUFIENCIA_PRACTICA.md) de cuatro intervenciones sobre diez fichas (seis controles sin cambios), y **10/10 recorridos RPC-08** en navegador Chromium local; el [workflow #170](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/45053932903) y su artefacto documentan la ejecución. No se ha producido una nueva aceptación manual pública de la muestra ni una prueba doméstica nueva.

La línea base de cobertura, fijada a otro commit en [RPC-A](./DIAGNOSTICO_RECIPE_PRACTICAL_COMPLETENESS.md), identificaba **590 recetas**, **492/590** con rendimiento numérico y **101/590** con tiempo total numérico único. Estas cifras no son mediciones regeneradas en el merge #353 y no acreditan suficiencia de uso.

## Problema de producto que queda abierto

El recetario ya permite recuperar, leer y preparar recetas de forma guiada en las cinco aplicaciones estáticas. Las pruebas de navegador muestran funcionamiento dirigido, mientras que las dos muestras editoriales revelan limitaciones concretas: uso de bases y salsas, cantidades condicionales, fases y tiempos de trabajo, y separación de experiencia real frente a una formulación propuesta. La utilidad culinaria **depende ahora de incorporar y conservar evidencia obtenida cocinando**, no de suponer que cualquier campo extraído es plenamente fiable.

No se dispone de métricas de adopción, pruebas comparativas con otros cocineros ni datos de reproducción de las correcciones. Una nueva interfaz con indicadores de «completo», «seguro» o «puedes cocinarlo» aparentaría una precisión no demostrada.

## Alternativas de siguiente capacidad

| Opción | Valor potencial | Riesgo o dependencia | Recomendación |
|---|---|---|---|
| **A. Ciclo de retroalimentación culinaria trazable**: recoger y trasladar la experiencia de una preparación real a su Markdown | Aumenta la calidad de las recetas que realmente se cocinan; captura temperaturas, tiempos, cantidades, resultado y cambios sin perder variantes | Necesita participación del propietario y disciplina de procedencia; no hay todavía evidencia suficiente para automatizarla | **Priorizar un diseño piloto documental acotado** |
| B. Mostrar datos explícitos de tiempos/rendimiento en Explorer y Assistant | Facilita planificar cuando están bien declarados | Cobertura reducida del tiempo total; la interfaz puede confundir tiempos parciales y totales | No desarrollar hasta validar representación, abstenciones y valor en casos reales |
| C. Ampliar otra tanda editorial general de recetas | Corrige problemas localizados | Repetir muestreos dirigidos de contenido sin contrastar resultados domésticos tiene retornos decrecientes | Mantener revisiones selectivas, sin nueva campaña amplia |
| D. Normalizar identidades y requisitos para recomendaciones desde Pantry | Potencial futuro de automatización | Identidades candidatas sin confirmar; compatibilidad y cantidades no demostradas | Continuar como deuda de investigación, sin implementación |
| E. Backend, cuentas, agentes, nutrición o sincronización | Potencial de expansión | Complejidad, privacidad y conclusiones culinarias no justificadas por esta evidencia | Diferir |

Las prioridades son juicios de producto condicionados a la evidencia disponible, **no datos de uso ni validaciones de mercado**.

## Recomendación: Culinary Preparation Feedback Loop (CPFL)

Seleccionar como **siguiente candidata** un **ciclo de observación y mejora tras cocinar una receta**, inicialmente **sin construir aplicación nueva**. El objetivo no es introducir una calificación universal, sino hacer sencillo que una experiencia concreta conserve: receta y versión de partida; fecha solo si se conoce; cantidades y sustituciones realmente utilizadas; tiempo y condiciones realmente observados; resultados positivos y defectos; valoración si fue comunicada; mejor versión frente a una alternativa; y cambios **propuestos pero todavía no probados**.

Este ciclo deberá trabajar con el Markdown y la gobernanza existentes. El historial observado nunca debe borrarse para forzar que la última propuesta parezca mejor. Si una adaptación nueva es peor, conservar la versión más satisfactoria y registrar la alternativa fallida; si no hay comparación demostrada, mantener incertidumbre.

### CPFL-A — Contrato mínimo y viabilidad, único alcance recomendado inicialmente

1. Inventariar los campos y secciones existentes que ya describen `Registro de prueba`, `Evolución`, `Valoración`, `Variantes` o `Pendiente de probar`; **no introducir un segundo modelo de receta**.
2. Fijar un contrato **mínimo y opcional** de observación: fuente, preparación efectiva, diferencias con la receta publicada, resultado y evidencia. Separar la declaración del propietario, la propuesta editorial y el contenido procedente de otra fuente.
3. Preparar **tres ejemplos históricos ya documentados**, sin añadir supuestas medidas faltantes: pastel de manzana `REC-0079` (resultado del lemon curd), hamburguesa asiática `REC-0007` (valoración doméstica), caballa japonesa `REC-0009` (preparación satisfactoria con tiempos no documentados). Verificar antes de utilizarlos sus versiones canónicas vigentes.
4. Definir el flujo de actualización con revisión humana de cambios, preservación de variantes y una PR temática pequeña. Los datos inexistentes continúan como `desconocido`.
5. Entregar un diagnóstico de viabilidad y un protocolo de prueba con el propietario: **sin afirmar automáticamente que haya una nueva elaboración culinaria**.

### CPFL-B — Piloto de uso (condicionado)

Únicamente después de aprobar CPFL-A y disponer de observaciones reales nuevas, comprobar si el flujo es cómodo y mejora una receta concretamente. La ausencia de nuevas elaboraciones no debe simularse con ejemplos fabricados.

### CPFL-C — Decisión de interfaz (condicionada)

Solo si el flujo manual demuestra valor y aparecen requisitos repetidos, evaluar si Recipe Assistant necesita una exportación local de notas, evitando almacenar datos sensibles sin consentimiento y sin sincronizar por defecto con GitHub. No iniciar ahora pantallas, backend ni integraciones.

## Puertas de decisión

- **PD-01 — Procedencia:** nunca transformar propuestas o deducciones en preparaciones domésticas confirmadas.
- **PD-02 — Fidelidad:** conservar la mejor formulación verificada; las variantes y resultados negativos siguen documentados.
- **PD-03 — Alcance mínimo:** reutilizar Markdown, IDs, auditorías y PR existentes antes de añadir campos obligatorios o infraestructura.
- **PD-04 — Utilidad real:** un ciclo de feedback debe poder aprovecharse con datos incompletos sin inventar tiempos, pesos o temperaturas.
- **PD-05 — Privacidad:** no recopilar automáticamente hábitos, fechas, preferencias o inventario personal desde el sitio público.
- **PD-06 — Abstención:** no activar filtros de cocinabilidad, seguridad, sustituciones, nutrición o disponibilidad a partir de metadatos parciales.
- **PD-07 — Aprobación:** nueva funcionalidad, esquema, release y fases CPFL-B/C exigen decisiones independientes.

## Decisión solicitada

**Aprobar solamente la prioridad de Culinary Preparation Feedback Loop y el alcance de descubrimiento documental CPFL-A**. La fusión de este documento registra una recomendación RPC-D y cerraría **Recipe Practical Completeness A–D como ciclo de investigación y pilotos acotados**, pero **no autoriza** una nueva interfaz, integración con GitHub desde el navegador, backend, release o ampliación masiva del recetario.

La versión publicada permanece en **v1.7.0**. El asistente prepara ramas y PR; el propietario las revisa, fusiona y elimina ramas remotas.


## CPFL-A — Diagnóstico documental realizado (22-11-2026)

El [contrato de feedback de preparaciones](./CONTRATO_FEEDBACK_PREPARACIONES_CPFL_A.md) documenta los recursos de Markdown existentes y sus límites, propone una nota de observación mínima y **opcional** y verifica tres ejemplos históricos del repositorio: pastel de manzana `REC-0079`, hamburguesa asiática `REC-0007` y caballa japonesa `REC-0009`. Cada ejemplo distingue la preparación realmente declarada, los datos desconocidos y las propuestas aún sin probar.

La conclusión es una **viabilidad editorial acotada sin infraestructura nueva**. La fase CPFL-B queda condicionada a que exista una preparación **nueva y real**, voluntariamente documentada; no se ha ejecutado ni autorizado automáticamente un piloto culinario. Última release publicada: `v1.7.0`.
