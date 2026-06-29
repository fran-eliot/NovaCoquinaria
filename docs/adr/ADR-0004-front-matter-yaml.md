# ADR-0004 - Front Matter YAML como Metadatos Canónicos

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Francisco Ramírez Martín

---

# Contexto

El repositorio GASTRO utiliza archivos Markdown como fuente única de verdad del conocimiento culinario.

Markdown es excelente para lectura humana, documentación técnica y versionado, pero por sí solo no permite clasificar de forma estructurada todos los documentos.

Para que el repositorio pueda crecer y servir en el futuro como base para una aplicación, buscador, índice automático o asistente basado en IA, es necesario incorporar metadatos estables y procesables.

---

# Problema

Los documentos necesitan información estructurada adicional.

Por ejemplo:

* identificador único;
* tipo de documento;
* título;
* categoría;
* etiquetas;
* versión;
* estado;
* fecha de revisión;
* relaciones con otros documentos.

Si esta información queda escrita únicamente en texto libre, será difícil procesarla automáticamente.

---

# Decisión

Todos los documentos del repositorio utilizarán **Front Matter YAML** al inicio del archivo.

El bloque YAML contendrá los metadatos canónicos del documento.

Ejemplo:

```yaml
---
id: REC-0001
tipo: receta
titulo: Arroz chaufa
categoria: Arroces
estado: estable
version: 1.0
ultima_revision: 2026-06-29
etiquetas:
  - arroz
  - wok
  - cocina asiatica
---
```

El contenido Markdown seguirá siendo la parte principal del documento, pero los metadatos YAML permitirán clasificarlo, indexarlo y reutilizarlo de forma automática.

---

# Campos mínimos

Todos los documentos deberán incluir, como mínimo:

```yaml
---
id:
tipo:
titulo:
estado:
version:
ultima_revision:
etiquetas:
---
```

---

# Tipos de documento

El campo `tipo` deberá utilizar uno de los valores definidos en la especificación del proyecto:

```yaml
tipo: arquitectura
tipo: base
tipo: receta
tipo: ingrediente
tipo: plantilla
tipo: tabla
tipo: nota
```

---

# Estado del documento

El campo `estado` podrá utilizar los siguientes valores:

```yaml
estado: borrador
estado: en_revision
estado: estable
estado: obsoleto
```

---

# Reglas de uso

## El Front Matter debe estar al inicio

El bloque YAML siempre será el primer contenido del archivo.

---

## No duplicar metadatos innecesariamente

Los metadatos estructurados no deben repetirse de forma extensa dentro del cuerpo del documento, salvo cuando mejore la legibilidad.

---

## Mantener valores consistentes

Las etiquetas, tipos y estados deberán seguir siempre las mismas convenciones.

Ejemplo:

Preferir:

```yaml
- cocina asiatica
```

Evitar variantes como:

```yaml
- Cocina Asiática
- cocina_asia
- asiático
```

---

## Pensar en automatización futura

Los metadatos deberán escribirse pensando en que puedan ser leídos por scripts, aplicaciones, buscadores o asistentes de IA.

---

# Justificación

El Front Matter YAML permite combinar dos ventajas:

* Markdown legible para personas.
* Metadatos estructurados para software.

Esto convierte cada documento en una unidad de conocimiento semiestructurada.

---

# Alternativas consideradas

## Markdown sin metadatos

**Descartado**.

Ventajas:

* mayor simplicidad inicial.

Inconvenientes:

* difícil clasificación;
* peor automatización;
* menor capacidad de búsqueda avanzada;
* mayor dependencia de texto libre.

---

## Base de datos externa

**Descartada como fuente principal**.

Podría utilizarse en el futuro como índice derivado, pero no como fuente de verdad.

---

## JSON embebido

**Descartado**.

Aunque es procesable, resulta menos legible y más incómodo de mantener manualmente que YAML.

---

# Consecuencias

## Ventajas

* Documentos más estructurados.
* Mejor búsqueda.
* Preparación para automatización.
* Posibilidad de generar índices.
* Posibilidad de filtrar por tipo, categoría, etiquetas o estado.
* Compatibilidad con herramientas de documentación y generadores estáticos.

## Inconvenientes

* Añade cierta carga inicial al crear documentos.
* Requiere mantener consistencia en los valores.
* Puede generar errores si el YAML está mal formado.

---

# Impacto futuro

El Front Matter YAML permitirá construir sobre el repositorio:

* índices automáticos;
* buscadores;
* catálogos de recetas;
* filtros por ingredientes, técnicas o dificultad;
* generación de menús;
* listas de la compra;
* integración con aplicaciones móviles;
* sistemas RAG para asistentes basados en IA.

---

# Dependencias

* [ADR-0001 - Filosofía del Proyecto](./ADR-0001-filosofia-del-proyecto.md)
* [ADR-0002 - Estructura del Repositorio](./ADR-0002-estructura-del-repositorio.md)
* [ADR-0003 - El Repositorio Markdown como Fuente Única de Verdad](./ADR-0003-markdown-como-fuente-de-verdad.md)

---

# Véase también

* [README](../../README.md)
* [GUIA_DE_ESTILO](../../GUIA_DE_ESTILO.md)
* [ESPECIFICACION_DE_DOCUMENTOS](../../ESPECIFICACION_DE_DOCUMENTOS.md)

---

# Utilizado por

Este ADR se aplicará a todos los documentos del repositorio GASTRO.
