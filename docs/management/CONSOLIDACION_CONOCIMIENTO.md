---
id: DOC-0022
titulo: Consolidación del conocimiento culinario
tipo: gestion
version: 1.0.0
estado: borrador
ultima_revision: 2026-11-14
---

# Consolidación del conocimiento culinario

## Objetivo

Establecer un procedimiento incremental para revisar integridad, navegación y reutilización del conocimiento culinario tras la expansión de los módulos. Este documento describe un **plan de revisión**, no certifica que el repositorio completo haya superado una auditoría.

## Alcance

- Integridad de enlaces Markdown internos.
- Unicidad y coherencia de identificadores.
- Front Matter conforme al modelo vigente.
- Navegación entre índices de módulos, recetas, técnicas, ingredientes y tablas.
- Detección de duplicidades y referencias a documentos todavía no creados.
- Distinción entre recetas documentadas y recetas probadas en cocina.

## Herramientas existentes

| Control | Herramienta |
|---|---|
| Validación conjunta | `python tools/validate_all.py` |
| Front Matter | `tools/validate_frontmatter.py` |
| Identificadores | `tools/validate_ids.py` |
| Enlaces internos | `tools/validate_links.py` |

La existencia de estos validadores está confirmada en el repositorio. **Su ejecución y resultado no se han verificado en esta revisión**.

## Primer hallazgo confirmado

Durante una revisión dirigida de referencias del módulo Cocina Asiática se detectó un enlace a `11_Despensa/09_Salsas/hoisin.md` sin documento de destino en `main` antes de este incremento. Se incorpora una ficha de ingrediente con ID `ING-0041` para cubrir esa referencia.

No se extrapola este hallazgo a un número total de enlaces rotos del repositorio.

## Revisión dirigida de navegación — 2026-11-14

Se realizó una comprobación de existencia de destinos Markdown sobre una **muestra de 36 referencias** en los índices de módulos:

| Documento de origen | Referencias comprobadas | Destinos ausentes |
|---|---:|---:|
| `02_Pastas/README.md` | 12 | 0 |
| `07_Cocina_Asiatica/README.md` | 24 | 0 |
| **Total de la muestra** | **36** | **0** |

**Método:** lectura de los enlaces relativos Markdown y consulta de existencia de los archivos de destino en la rama `main` mediante GitHub. En Pastas se revisaron las primeras 12 referencias Markdown; en Cocina Asiática se revisaron las referencias 13 a 36 según su orden de aparición. No se validaron anclas, contenido semántico de los destinos ni el conjunto completo de archivos.

**Resultado:** no se encontraron destinos ausentes **en la muestra indicada**. Esto no acredita la integridad global del repositorio ni sustituye `python tools/validate_all.py`.

### Coherencia semántica detectada

La ficha `11_Despensa/09_Salsas/miso.md` describía como futuras la sopa de miso y la berenjena glaseada, aunque ya existen como `REC-0072` y `REC-0075`. Se actualiza la ficha para enlazar esas recetas y `REC-0076` (pollo glaseado con miso), manteniendo separadas las preparaciones todavía no documentadas.

## Integración continua de la integridad documental

El workflow [Knowledge integrity](../../.github/workflows/knowledge-integrity.yml) ejecuta `python tools/validate_all.py` en pull requests, cambios a `main` y mediante activación manual. Instala la dependencia PyYAML necesaria para los validadores existentes.

El job `Validate Markdown knowledge` falla si cualquiera de los tres controles devuelve un código distinto de cero. Los mensajes de los validadores quedan disponibles en el registro de ejecución de GitHub Actions.

**Estado de ejecución:** la incorporación del workflow no demuestra que el repositorio supere los controles. El resultado real debe consultarse en GitHub Actions tras ejecutarse. Para exigir este control antes de fusionar, se debe configurar como comprobación requerida en la protección de la rama.

## Procedimiento recomendado

1. Ejecutar la validación conjunta sobre el árbol completo del repositorio.
2. Registrar los errores con ruta de origen, destino esperado y categoría.
3. Corregir primero los enlaces internos rotos y las colisiones de identificadores.
4. Revisar índices de módulos y navegación desde el README principal.
5. Identificar contenido duplicado y establecer un documento de autoridad.
6. Revisar la relación entre recetas, técnicas, ingredientes y tablas.
7. Repetir validaciones tras cada lote de correcciones.
8. Separar el resultado de validación estructural de cualquier afirmación sobre pruebas culinarias.

## Criterios de cierre

- Validación automática ejecutada y sin errores, o excepciones documentadas.
- Índices de módulos accesibles desde el punto de entrada.
- Referencias internas relevantes verificadas.
- Hallazgos pendientes registrados con prioridad y responsable.
- Ningún contenido marcado como probado sin evidencia de elaboración.

## Relación con otros documentos

- [Estado del proyecto](./PROJECT_STATUS.md)
- [Roadmap](./ROADMAP.md)
- [README principal](../../README.md)

## Principio de NovaCoquinaria

> La consolidación transforma una colección creciente en conocimiento navegable, verificable y reutilizable.
