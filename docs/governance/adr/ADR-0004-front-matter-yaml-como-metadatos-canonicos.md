# ADR-0004 — Front Matter YAML como Modelo Canónico de Metadatos

**Identificador:** ADR-0004

**Estado:** Aceptado

**Vigencia:** Activa

**Última Revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Modelo Documental

---

# Contexto

Tras adoptar Markdown como única fuente oficial de verdad (ADR-0003), surge la necesidad de representar información estructurada asociada a cada documento.

Markdown proporciona una excelente legibilidad para las personas, pero carece de un mecanismo estándar para describir metadatos de forma uniforme y procesable.

El SGCC necesita identificar, clasificar, relacionar y automatizar el tratamiento de miles de documentos sin depender del contenido textual.

---

# Problema

Es necesario definir un mecanismo común para representar los metadatos del repositorio.

Dicho mecanismo debe:

- ser legible por personas;
- ser fácilmente procesable por herramientas;
- integrarse de forma natural con Markdown;
- permanecer independiente de cualquier tecnología concreta;
- servir como base para automatización, indexación y publicación.

La decisión condicionará todo el modelo documental del SGCC.

---

# Decisión

Todos los documentos del SGCC utilizarán un bloque **Front Matter YAML** como representación oficial de sus metadatos.

Este bloque constituye el **modelo canónico de metadatos** del documento.

El Front Matter identifica el documento y describe sus propiedades estructurales.

El contenido Markdown continúa representando el conocimiento propiamente dicho.

La definición concreta de los campos y sus valores se mantiene fuera de este ADR y forma parte del Modelo Documental del proyecto.

---

# Justificación

La combinación de Markdown y Front Matter YAML permite separar claramente dos niveles de información:

- conocimiento (contenido);
- metadatos (estructura).

Esta separación facilita:

- identificación unívoca;
- clasificación;
- indexación;
- automatización;
- interoperabilidad;
- evolución del modelo documental.

Cada documento pasa a ser una unidad de conocimiento estructurada y reutilizable.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- Todo documento posee metadatos estructurados.
- Los metadatos son independientes del contenido.
- El Front Matter constituye la referencia oficial para la identificación documental.
- Los consumidores deberán interpretar los metadatos sin modificar el contenido original.
- La evolución del modelo documental no deberá alterar la filosofía del SGCC.

---

# Modelo conceptual

```text
Documento

├── Front Matter YAML
│       │
│       ├── Identidad
│       ├── Clasificación
│       ├── Estado
│       ├── Relaciones
│       └── Metadatos
│
└── Contenido Markdown
        │
        └── Conocimiento
```

Los metadatos describen el documento.

El contenido representa el conocimiento.

---

# Alternativas consideradas

## Markdown sin metadatos

Descartado por:

- dificultar la automatización;
- impedir una clasificación homogénea;
- limitar la reutilización.

---

## Base de datos externa

Descartada como fuente principal.

Podrá utilizarse como representación derivada, pero nunca como origen oficial de los metadatos.

---

## JSON embebido

Descartado por:

- menor legibilidad;
- peor integración con Markdown;
- mayor complejidad de mantenimiento.

---

# Consecuencias

## Ventajas

- Modelo documental uniforme.
- Automatización sencilla.
- Mejor trazabilidad.
- Indexación eficiente.
- Compatibilidad con herramientas.
- Independencia tecnológica.
- Evolución controlada del modelo documental.

---

## Inconvenientes

- Mayor disciplina documental.
- Necesidad de validar los metadatos.
- Dependencia de convenciones comunes.

---

# Impacto arquitectónico

Esta decisión convierte cada documento del SGCC en una unidad de conocimiento estructurada.

Como consecuencia:

- podrán generarse índices automáticamente;
- podrán establecerse relaciones entre documentos;
- diferentes consumidores podrán interpretar los metadatos de forma homogénea;
- el modelo documental podrá evolucionar sin modificar el contenido del conocimiento.

---

# Relación con otros ADR

Este ADR desarrolla:

- ADR-0003 — Markdown como Fuente Única de Verdad.

Es ampliado posteriormente por:

- ADR-0006 — Referencias Cruzadas.
- ADR-0008 — Identificadores Únicos.
- ADR-0018 — Modelo del Conocimiento del SGCC.

---

# Documentación relacionada

La implementación de esta decisión se desarrolla en:

- ESPECIFICACION_DE_DOCUMENTOS.md
- GUIA_DE_ESTILO.md
- ARQUITECTURA.md
- TOOLS_FRAMEWORK.md

La definición de campos, tipos, estados y convenciones forma parte del Modelo Documental y podrá evolucionar sin modificar este ADR.

---

# Estado actual

La decisión continúa plenamente vigente.

El Front Matter YAML constituye el contrato estructural entre el conocimiento documentado y las herramientas que consumen el SGCC.

Toda automatización, publicación, validación o integración deberá interpretar los metadatos definidos en este bloque sin alterar el contenido original del documento.