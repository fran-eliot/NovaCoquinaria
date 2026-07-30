# ADR-0008 — Identidad Persistente de las Unidades de Conocimiento

**Identificador:** ADR-0008

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Modelo del Conocimiento

---

# Contexto

Cada documento del SGCC representa una unidad de conocimiento.

Sin embargo, la representación física de dicho documento puede evolucionar con el tiempo:

- cambiar de nombre;
- cambiar de ubicación;
- reorganizarse dentro del repositorio;
- modificarse parcialmente.

La identidad del conocimiento no debe depender de ninguno de estos cambios.

Es necesario distinguir claramente entre la identidad conceptual de una unidad de conocimiento y su representación física.

---

# Problema

Es necesario establecer un mecanismo que permita identificar de forma permanente cada unidad de conocimiento del SGCC.

La solución debe garantizar que la identidad permanezca estable independientemente de:

- la organización del repositorio;
- la estructura documental;
- las futuras aplicaciones;
- las tecnologías utilizadas.

---

# Decisión

Toda unidad de conocimiento del SGCC dispondrá de un identificador único, permanente e independiente de su representación física.

Este identificador constituye la identidad oficial del conocimiento.

Su representación concreta se almacenará como parte de los metadatos del documento.

La definición del formato del identificador pertenece al Modelo Documental y podrá evolucionar sin modificar esta decisión.

---

# Justificación

Separar identidad y representación permite construir un sistema evolutivo.

Los documentos podrán reorganizarse libremente sin perder continuidad histórica ni romper las relaciones existentes.

La identidad pasa a pertenecer al conocimiento y no al sistema de archivos.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- Toda unidad de conocimiento posee una identidad permanente.
- La identidad es independiente del nombre del archivo.
- La identidad es independiente de la ubicación física.
- Los identificadores nunca se reutilizan.
- Las relaciones entre documentos deberán apoyarse en identidades estables y no en la estructura física.

---

# Modelo conceptual

```text
              Unidad de Conocimiento

                    │
        ┌───────────┴───────────┐
        │                       │

   Identidad               Representación

        │                       │

 Identificador         Documento Markdown

        │                       │

 Permanente         Nombre • Carpeta • Ruta
```

La identidad permanece.

La representación puede evolucionar.

---

# Alternativas consideradas

## Identificación mediante nombre del archivo

Descartada por:

- depender de convenciones de nomenclatura;
- dificultar reorganizaciones.

---

## Identificación mediante rutas

Descartada por:

- romper referencias al reorganizar el repositorio;
- acoplar el conocimiento a la estructura física.

---

## Identificadores aleatorios (UUID)

Descartados como modelo principal por:

- menor legibilidad;
- peor mantenibilidad manual.

Podrán utilizarse internamente por futuras implementaciones si fuese necesario.

---

# Consecuencias

## Ventajas

- Identidad permanente.
- Evolución segura del repositorio.
- Independencia tecnológica.
- Compatibilidad con bases de datos.
- Integración con APIs.
- Construcción consistente del Knowledge Graph.

---

## Inconvenientes

- Necesidad de gestionar la asignación de nuevas identidades.
- Validación para evitar duplicados.

---

# Impacto arquitectónico

Esta decisión desacopla completamente la identidad del conocimiento de su representación documental.

Como consecuencia:

- el repositorio podrá reorganizarse sin romper referencias;
- las aplicaciones podrán utilizar una identidad común;
- las relaciones permanecerán estables;
- el modelo conceptual del SGCC será independiente de la implementación.

---

# Relación con otros ADR

Este ADR desarrolla:

- ADR-0003 — Markdown como Fuente Única de Verdad.
- ADR-0004 — Front Matter YAML como Modelo Canónico de Metadatos.
- ADR-0007 — Modelo Conceptual del Dominio del SGCC.

Es ampliado posteriormente por:

- ADR-0010 — Arquitectura Orientada al Conocimiento.
- ADR-0018 — Modelo del Conocimiento del SGCC.
- ADR-0019 — Modelo Lógico vs Estructura Física.

---

# Documentación relacionada

La implementación de esta decisión se desarrolla en:

- ESPECIFICACION_DE_DOCUMENTOS.md
- ARQUITECTURA.md
- TOOLS_FRAMEWORK.md
- QUALITY_PIPELINE.md

La definición concreta del formato, prefijos y reglas de asignación forma parte del Modelo Documental y podrá evolucionar sin modificar este ADR.

---

# Estado actual

La decisión continúa plenamente vigente.

La identidad persistente constituye uno de los mecanismos fundamentales para garantizar la estabilidad del SGCC frente a reorganizaciones, evolución del modelo documental y futuras implementaciones tecnológicas.

Toda evolución futura deberá preservar la independencia entre la identidad del conocimiento y su representación física.