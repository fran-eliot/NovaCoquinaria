---
id: ARC-0015
tipo: arquitectura
titulo: Automatización del SGCC
version: 1.0
estado: borrador
ultima_revision: 2026-07-08
---

# Automatización del SGCC

## Objetivo

Este documento define la estrategia de automatización de NovaCoquinaria.

La automatización no sustituye al conocimiento culinario ni modifica la fuente de verdad del proyecto.

Su función es proteger la coherencia arquitectónica, mejorar la calidad documental y reducir tareas repetitivas.

## Principios

La automatización del proyecto seguirá estos principios:

- Markdown seguirá siendo la única fuente de verdad.
- `site_docs/` seguirá siendo un artefacto generado.
- Los scripts no deberán introducir conocimiento culinario nuevo.
- Las validaciones deberán detectar problemas, no ocultarlos.
- Toda automatización deberá ser simple, auditable y mantenible.

## Alcance inicial

La automatización inicial se centrará en:

- validación de Front Matter YAML;
- detección de identificadores duplicados;
- validación de enlaces internos;
- generación de estadísticas del repositorio;
- apoyo a la generación de documentación publicada.

## Fuera de alcance

Quedan fuera de esta fase:

- bases de datos;
- API;
- aplicación web dinámica;
- grafo de conocimiento;
- generación automática de recetas;
- modificación automática de contenido culinario.

## Herramientas previstas

Las herramientas iniciales se ubicarán en:

```text
tools/
```

## Scripts previstos

```text
validate_frontmatter.py
validate_ids.py
validate_links.py
generate_stats.py
build_site_docs.py
```

## Relación con MkDocs

MkDocs utilizará `site_docs/` como directorio de publicación.

El contenido de `site_docs/` deberá generarse a partir del Markdown original del repositorio.

No se editará manualmente.

## Criterios de calidad

Una automatización será aceptable cuando:

- sea comprensible;
- no añada complejidad innecesaria;
- pueda ejecutarse localmente;
- produzca mensajes claros;
- falle de forma explícita ante inconsistencias;
- respete la arquitectura documental existente.

## Evolución prevista

La automatización podrá evolucionar en fases:

1. Validaciones básicas.
2. Informes de calidad.
3. Generación de índices.
4. Validación semántica de relaciones.
5. Preparación para grafo de conocimiento.

## Referencias

* [Arquitectura](../ARQUITECTURA.md)
* [Quality](../QUALITY.md)
* [ADR-0003 Markdown como fuente de verdad](../adr/ADR-0003-markdown-como-fuente-de-verdad.md)
* [ADR-0012 Preparación para publicación web MkDocs](../adr/ADR-0012-preparacion-para-publicacion-web-mkdocs.md)
* [ADR-0014 Gestión del conocimiento](../adr/ADR-0014-gestion-del-conocimiento.md)