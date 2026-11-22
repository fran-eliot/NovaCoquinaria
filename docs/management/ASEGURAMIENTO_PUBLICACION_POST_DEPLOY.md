---
id: DOC-ASEGURAMIENTO-PUBLICACION-2026
titulo: Aseguramiento de publicación GitHub Pages — primer ciclo
tipo: gestion
version: 0.1.0
estado: propuesta-tecnica
ultima_revision: 2026-11-22
---

# Aseguramiento de publicación — primera mejora independiente de CPFL

## Corte y motivo

Se parte de `main` tras la fusión de la [PR #356](https://github.com/fran-eliot/NovaCoquinaria/pull/356), commit `0f08607769323e09cc206ade1e2e63966df8915f`. Su protocolo [CPFL-B](./PROTOCOLO_PILOTO_CPFL_B.md) está **preparado pero no ejecutado**, por falta de una nueva observación doméstica. El trabajo de publicación es **independiente** y no modifica CPFL.

La revisión de los workflows existentes revela un hueco operativo verificable:

- `.github/workflows/deploy-mkdocs.yml` construye, valida el sitio **localmente** y ejecuta `mkdocs gh-deploy --force` después de cada `push` a `main`.
- `.github/workflows/culinary-public-http.yml` y `.github/workflows/culinary-public-browser.yml` verifican la web pública, pero sus activadores actuales son **manuales** y `pull_request` cuando cambian los archivos de las propias comprobaciones.
- Por tanto, **un deploy correcto no implica que se compruebe automáticamente el estado HTTP de GitHub Pages después de publicarlo**. Los tests previos al despliegue validan otro entorno.

La alternativa elegida es **aprovechar el smoke HTTP público ya existente** sin duplicarlo ni añadir un sistema de despliegue nuevo.

## Alcance exacto de la PR

1. Añadir `.github/workflows/culinary-post-deploy-http.yml` con activador `workflow_run` al completar **Deploy MkDocs site**. El job solo se ejecuta cuando ese workflow termina en `success` desde la rama `main`.
2. Reutilizar `tools/check_culinary_public_http.py` para consultar las cinco aplicaciones, recursos versionados, catálogo, manifiesto y payload de receta de muestra **en la URL HTTP pública**.
3. Incorporar `--expected-source-commit`: comparar el `source_commit` publicado en el catálogo con el SHA de la ejecución de despliegue que desencadenó el workflow. Una web con origen anterior o diferente provoca error, en lugar de declarar éxito por mero HTTP 200.
4. Añadir pruebas **offline** de coincidencia de SHA, origen distinto e input inválido en `tools/test_culinary_public_http.py`.
5. Generar un JSON de evidencia por ejecución en `culinary-post-deploy-http-evidence`, también cuando el smoke falla y se alcanza la subida de artefactos.

## Qué demuestra y qué no

**Si el workflow de post-despliegue termina correctamente**, hay evidencia automatizada de que, en el instante de ejecución, las páginas y recursos HTTP esperados estaban accesibles, catálogo y manifiesto coincidían y el catálogo declaraba el SHA del deploy desencadenante. No es una prueba de navegabilidad de todos los recorridos, ni aceptación manual, ni verificación culinaria, ni una garantía permanente de disponibilidad.

**Si falla**, revisar los artefactos, el estado de Pages, la propagación de cachés y el SHA publicado. La falta de coincidencia de procedencia **no autoriza a corregir el catálogo a mano** ni a forzar un despliegue sin diagnóstico. Si hay despliegues cercanos, un commit posterior publicado puede sustituir al anterior antes de la comprobación: ese caso es una limitación de concurrencia del contraste y exige consultar el historial, no afirmar automáticamente que el sitio contiene datos equivocados.

Los workflows de navegador público ya existentes **siguen siendo controles independientes**. No se fuerza una prueba Chromium de escritura o transferencia de datos personales después de cada publicación. El job de post-despliegue usa únicamente peticiones HTTP de lectura, permisos `contents: read` y no accede a `localStorage`.

## Validación y siguiente decisión

Esta PR puede validar en CI la **integridad de los archivos y los tests Python**, pero un evento `workflow_run` que sigue a un deploy **no se dispara solo por abrir la PR**. La prueba efectiva del automatismo se evaluará **después de fusionar la rama** y observar el siguiente despliegue `main`, distinguiendo el SHA de origen y los resultados de los dos workflows. No adjudicar una ejecución post-deploy satisfactoria antes de verla.

La mejora se considera un primer ciclo de **aseguramiento operativo de publicación**, no el comienzo de otra fase de recetas, filtros, identidad semántica, backend o release. CPFL-B continúa pendiente de una elaboración real. La última release publicada continúa siendo **v1.7.0**.

## Alternativas que no se adoptan en esta PR

- **Ningún cambio**: mantiene la brecha entre verificar un build local y observar el sitio público.
- **Ejecutar pruebas públicas dentro del job de deploy**: introduciría espera/propagación y acoplaría una publicación ya terminada con el estado HTTP de Pages; el job separado evita modificar el despliegue existente.
- **Nuevo test duplicado de Pages**: innecesario; `check_culinary_public_http.py` ya existe y tiene pruebas offline.
- **Más aplicaciones o métricas de cocinabilidad**: no resuelve el riesgo operativo demostrado.

El propietario revisa y fusiona la PR; no se publica ninguna versión ni se modifica el tag de `v1.7.0`.


## Primera ejecución real y ajuste de propagación (22-11-2026)

La [PR #357](https://github.com/fran-eliot/NovaCoquinaria/pull/357) se fusionó en `f42849e0e39ad555647c7d4377e081ed0ad73ef2`. La ejecución de [Deploy MkDocs site](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/45058071211) concluyó en `success`, pero el primer [Culinary Post-Deploy HTTP Assurance](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/45058219028), job `137318117150`, concluyó en **failure**:

- **SHA esperado:** `f42849e0e39ad555647c7d4377e081ed0ad73ef2`.
- **`source_commit` efectivamente leído en el catálogo público:** `0f08607769323e09cc206ade1e2e63966df8915f` (publicación anterior).
- **Pruebas offline:** 9/9 correctas.
- **Control HTTP:** falló exclusivamente por discrepancia del SHA publicado; se guardó `culinary-post-deploy-http-evidence`.
- **Contexto:** el workflow automático de Pages para el nuevo despliegue se inició aproximadamente al mismo tiempo. Esto es compatible con un intervalo de propagación pendiente; el resultado observado **no prueba que la web finalmente se actualizase ni que el workflow de comprobación esté ya corregido**.

Se propone modificar **solo el job de aseguramiento** con un máximo de **12 verificaciones**, 15 segundos de espera entre intentos. Cada una vuelve a consultar el sitio HTTP y exige **coincidencia estricta** del SHA del evento desencadenante. El resultado es correcto únicamente si alguna verificación alcanza esa coincidencia; si transcurre toda la ventana, la ejecución sigue fallando y conserva el JSON de evidencia de la última comprobación.

Este reintento no introduce aceptación de una versión antigua, no automatiza un redeploy y no convierte un HTTP 200 en prueba de aceptación funcional. **La corrección debe validarse después de fusionar la PR**, observando una nueva ejecución post-deploy; la PR en sí no reproduce ese evento.
