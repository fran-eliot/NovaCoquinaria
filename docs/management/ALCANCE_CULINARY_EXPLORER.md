---
id: DOC-ALCANCE-EXPLORER-2026
titulo: Alcance de entrega de Culinary Explorer
tipo: gestion
version: 0.1.4
estado: borrador
ultima_revision: 2026-11-19
---

# Culinary Explorer — alcance de entrega

## Base y propósito

La [revisión estratégica](./REVISION_ESTRATEGICA_CULINARIA.md) quedó integrada en #269, merge `a2916e15075e05c8ccf47340635e212609b14354`. Knowledge integrity y Knowledge audit de esa PR finalizaron correctamente. Culinary Explorer 0.1.0 propone una aplicación consumidora de solo lectura para encontrar y consultar las recetas del SGCC desde el portal existente. La versión de capacidad no implica nueva release.

## Recorridos cotidianos

- Explorar el catálogo completo y reducirlo por módulo físico o evidencia de elaboración.
- Localizar una receta por título completo o secuencia contigua de términos de título. Este último es un comportamiento de presentación nuevo y explícito, no una ampliación silenciosa del motor Python.
- Buscar menciones de uno o varios ingredientes mediante secuencias contiguas de términos, con intersección a nivel de receta.
- Consultar título, módulo, evidencia, coincidencias de ingredientes y enlace a la ficha publicada. Mostrar tiempos y rendimientos solo si se preservan sus declaraciones originales, sin filtros ni cálculos en esta entrega.
- Distinguir catálogo vacío, resultado sin coincidencias, entrada inválida y fallo de carga.

Ejemplo: módulo de carnes e ingredientes «ajo» y «salsa de soja». El resultado identifica recetas con ambas menciones, no recetas necesariamente cocinables ni una lista de compra.

## Diseño acotado

Se propone una generación estática Python durante la preparación de MkDocs y un consumidor HTML/CSS/JavaScript sin dependencias de ejecución externas. El despliegue actual ejecuta tools/build_site_docs.py antes de mkdocs gh-deploy. La unidad A verificará el flujo real de generación, la inclusión de recetas y las rutas de destino; no se presupone que todas las rutas sean actualmente navegables. No se adopta backend, API, servicio de búsqueda remoto o persistencia.

El adaptador de publicación consume exclusivamente el índice 0.2.0 generado desde la proyección vigente. Produce un JSON versionado de solo lectura con commit, huella de índice, versión de esquema y registros mínimos: ID literal, título, módulo físico, estado de evidencia, destino relativo y ocurrencias textuales con posición y opcionalidad. La representación puede incluir texto original y localizador cuando sean necesarios para mostrar evidencia. No publicar el índice completo por defecto. La unidad A fijará nombres y tipos concretos, política de nulos, rutas relativas y huella de los bytes. No versionar los artefactos generados como conocimiento.

El adaptador de consulta reutilizará claves o tokens derivados con las funciones Python existentes cuando sea posible. Si el navegador requiere lógica propia de consulta, se limitará a las operaciones expuestas y se contrastará con el motor de referencia mediante conjuntos de IDs y posiciones. NFC, casefold, diacríticos, separadores y contigüidad deberán preservarse; no basta con asumir equivalencia de lowercase en JavaScript. Para título, la nueva modalidad se documentará y contrastará con un recorrido independiente. Se mantendrá el contrato del motor 0.2.0. No se incorporan identidades candidatas a las búsquedas de usuario ni se promueven reglas experimentales.

## Criterios de aceptación

| ID | Criterio |
|---|---|
| EXP-01 | Catálogo completo respecto al índice del mismo commit, IDs literales únicos, sin recuentos históricos constantes |
| EXP-02 | Proyección mínima versionada, reproducible byte a byte, con commit y huella de entrada; no modifica Markdown ni índice |
| EXP-03 | Validación bloqueante de esquema, IDs, referencias y rutas; ninguna carga parcial se presenta como catálogo completo |
| EXP-04 | Título completo o términos contiguos de título, con modalidad documentada, diacríticos conservados y contraste independiente |
| EXP-05 | Ingredientes por terms con equivalencia al motor 0.2.0, sin subcadenas, expansión ni inferencia |
| EXP-06 | Varias cláusulas de ingrediente en AND, combinables con módulo y evidencia, con resultados únicos y orden estable por ID literal |
| EXP-07 | Cada coincidencia conserva nombre y posición de ocurrencia, opcionalidad y acceso a fuente; se identifica como mención |
| EXP-08 | Evidencia original conservada; desconocido no equivale a pendiente y prepared no acredita la fórmula actual |
| EXP-09 | Cada enlace de receta resuelve a un destino publicado del mismo build; verificar rutas y caracteres especiales |
| EXP-10 | Interfaz operable con teclado, etiquetas visibles, foco y diseño adaptable a móvil y escritorio |
| EXP-11 | Estados de carga, error, consulta inválida y cero resultados diferenciados, con posibilidad de limpiar filtros |
| EXP-12 | Renderizado de datos como texto, rutas relativas validadas, sin HTML no confiable ni dependencias de red externas |
| EXP-13 | Regresión del motor y contraste de resultados/ocurrencias en casos sintéticos y corpus vigente, incluidos Unicode, negaciones, alternativas y opcionalidad |
| EXP-14 | Build local reproducible y verificación CI de artefactos y enlaces antes de publicación; despliegue únicamente por el flujo vigente |
| EXP-15 | Guía de uso y recorridos prácticos documentados con resultados observados, límites y evidencia de pruebas; no confundir validación técnica y culinaria |

## Unidades

| Unidad | Entrega | Criterios principales |
|---|---|---|
| A | Proyección consumible, contrato concreto y validaciones de publicación | EXP-01–03, 07–09 |
| B | Adaptador de búsqueda acotado y contraste con referencia | EXP-04–08, 13 |
| C | Interfaz estática accesible y recorridos básicos | EXP-06–12 |
| D | Integración de build/CI, comprobación de rutas, guía y cierre | EXP-09–15 y revisión conjunta |

Los criterios pueden solaparse. Cada unidad se entrega por separado; la aceptación final requiere evidencia conjunta, no mera fusión. La comprobación del portal desplegado se diferencia de la verificación previa del build. No se exige un nuevo ciclo de discovery; los problemas concretos se resuelven dentro de la unidad correspondiente.

## Exclusiones

No incluye compatibilidad receta-despensa, disponibilidad, alérgenos, sustituciones, escalado, filtros temporales o de rendimiento, escritura, cuentas, listas de compra, planificación, IA ni nuevos contratos canónicos. La [deuda de requisitos](./DEUDA_REQUISITOS_CULINARIOS.md) continúa diferida. No se compromete calendario ni release de proyecto. Se mantiene el flujo de revisión mediante PR.

## Referencias

- [Contrato del índice](../specifications/knowledge/CONTRATO_DEL_INDICE_DE_CONOCIMIENTO.md)
- [Alcance de recuperación textual](./ALCANCE_RECUPERACION_TEXTUAL.md)
- [Arquitectura](../architecture/ARQUITECTURA.md)
- [Revisión estratégica](./REVISION_ESTRATEGICA_CULINARIA.md)

## Unidad A — Proyección consumible

`tools/build_culinary_explorer.py` genera JSON UTF-8 ordenado y reproducible a partir de bytes del índice 0.2.0. Cabecera: schema_version 0.1.0, index_version, source_commit, index_sha256 (SHA-256 de bytes exactos), recipe_count y recipes (orden literal de ID). Cada registro contiene id, title, title_key, title_tokens, physical_module, evidence (objeto original), source_path, href y ingredients. Cada ocurrencia contiene position, name (texto o null), raw, optionality, source_location y tokens. Los tokens proceden del núcleo Python existente aplicado a la clave textual del índice; no hay nuevas identidades. La ruta href es relativa a la raíz del portal, codificada UTF-8 y con extensión .html según use_directory_urls=false. Se valida existencia del Markdown preparado, pertenencia a módulos, rutas seguras, inventario, procedencia y reconciliación exacta de postings. La comprobación de HTML final queda para D.

El preparador del portal incluye ahora los diez módulos de recetas; antes omitía Pastas, Legumbres, Cocina Asiática, Postres, Bebidas y Horno. Knowledge audit genera dos veces la proyección y compara bytes; las pruebas sintéticas cubren Unicode, nulos, fuentes ausentes, rutas inválidas, inventario, postings y evidencia. La proyección queda como artefacto de auditoría, todavía no se publica ni existe interfaz. No se altera el contrato del índice ni la release. Los resultados de CI se evaluarán antes del siguiente incremento.

## Unidad B — Adaptador de búsqueda

Se añade `assets/culinary-explorer-search.mjs`, módulo ES puro sin DOM ni red. La proyección pasa a esquema 0.1.1 (no cambia el índice) e incorpora unicode_profile: versión Unicode de Python, mapa casefold por código de carácter, espacios reconocidos por Python y rangos inclusivos de caracteres alfanuméricos. La normalización de entrada aplica estas tablas y NFC nativo de JavaScript. La equivalencia de NFC entre versiones Unicode del navegador no se presume universal; se contrasta en los casos seleccionados y el navegador final se comprobará en D. No hay dependencia de Node en ejecución web.

La función createSearch(catalog) ofrece search({title, titleMode, ingredients, module, evidence}); filtros ausentes son null o listas vacías. titleMode admite exact y terms (por defecto); exact utiliza title_key y terms secuencias contiguas sobre title_tokens. Cada ingrediente es una cláusula textual terms; todas se intersectan con los demás filtros. Las coincidencias exponen ocurrencias originales y match_scope=textual_mention. El orden del catálogo generado (ID literal) se conserva. Entradas sin términos son inválidas, excepto título exacto no vacío; un filtro de módulo desconocido devuelve cero, y evidencia fuera de los tres estados es inválida. El consumidor no modifica el catálogo ni incorpora inferencias.

El contraste `tools/evaluate_culinary_explorer.py` ejecuta el adaptador en Node 22 mediante `tools/explorer_search_driver.mjs`, compara IDs ordenados y evidencia por cláusula con query 0.2.0, y verifica títulos con un recorrido de referencia. Incluye consultas sin filtros, simples y compuestas, módulos, evidencia, positivos, negativos, entradas inválidas y muestras léxicas Unicode. El informe registra commit y huellas del índice y catálogo; Knowledge audit ejecuta el contraste tras generar la proyección. No demuestra equivalencia universal de Unicode ni precisión culinaria. La interfaz y publicación pertenecen a C y D.

## Unidad C — Interfaz de consulta

La plantilla `tools/templates/culinary-explorer.html` y los recursos `assets/culinary-explorer.css` y `assets/culinary-explorer-ui.mjs` implementan el consumidor estático. La plantilla se destina a la raíz del portal como culinary-explorer.html; el catálogo se espera en culinary_explorer.json, ambos pendientes de integración en D. La interfaz ofrece título exacto o términos, ingredientes separados por líneas (AND), módulo, evidencia, limpieza y navegación de 24 recetas por página. Las tarjetas enlazan a la ficha y muestran menciones, opcionalidad y línea de origen. Se conserva el orden literal del adaptador.

La interfaz valida el catálogo antes de habilitar controles, reconstruye y contrasta rutas relativas, utiliza textContent para datos y no interpreta HTML de fuentes. Distingue carga, fallo de carga, consulta inválida, catálogo vacío y ausencia de coincidencias. Incluye etiquetas nativas, foco visible, estado anunciado, controles de teclado y diseño adaptable con preferencia de tema del sistema. No incorpora tiempos o rendimientos porque la proyección vigente no incluye dichos datos. No se acredita todavía accesibilidad exhaustiva, prueba en navegador ni publicación; D integrará y contrastará los recorridos reales.

## Unidad D — Integración y uso

La preparación ordinaria con `python tools/build_site_docs.py` genera el catálogo y copia la plantilla a la raíz de site_docs. Se toma la proyección del HEAD Git, se construye el índice en memoria y se genera el catálogo con el contrato vigente. El build MkDocs publica HTML y recursos estáticos, sin servidor de aplicación. La opción --without-explorer reserva el modo de preparación de fuentes para Knowledge audit, que ya construye su propio índice y catálogo.

### Uso local

```bash
python -m pip install -r requirements.txt
python tools/build_site_docs.py
mkdocs build
python tools/check_explorer_site.py
python -m http.server 8000 --directory site
```

Abrir http://localhost:8000/ y seleccionar «Abrir el explorador culinario». Introducir un título o un ingrediente por línea, seleccionar módulo y evidencia si procede, y pulsar Buscar. Por ejemplo, ajo y salsa de soja recuperan recetas que mencionan ambas expresiones. Abrir las menciones para consultar texto original, opcionalidad y localizador, o seleccionar el título para abrir la ficha. Limpiar filtros recupera el catálogo completo. Los resultados no acreditan disponibilidad, compatibilidad, ausencia de alérgenos ni validación culinaria.

### Validación

El workflow Culinary Explorer site contrasta dos generaciones del catálogo, construye MkDocs y comprueba todos los destinos y recursos del HTML final. Chromium comprueba acceso desde inicio bajo un subdirectorio de publicación, carga, paginación, consulta compuesta, evidencia, navegación, ausencia de resultados, entrada inválida, limpieza, fallo de carga y dos tamaños de ventana. El informe de navegador se conserva como artefacto. El despliegue conserva el flujo vigente de main y verifica destinos antes de gh-deploy.

La evidencia de ejecución y el cierre de EXP-01–EXP-15 quedan pendientes de los resultados de CI y revisión. Un build local no acredita el despliegue remoto ni accesibilidad exhaustiva. No se publica una nueva release ni se incorpora otra capacidad.
