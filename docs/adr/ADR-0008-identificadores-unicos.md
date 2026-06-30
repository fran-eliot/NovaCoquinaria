# ADR-0008 - Identificadores Únicos y Estables

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Fran Ramírez

---

# Contexto

Cada documento del proyecto representa una unidad de conocimiento.

Su nombre de archivo y su ubicación dentro del repositorio pueden cambiar con el tiempo debido a reorganizaciones, mejoras o refactorizaciones de la estructura documental.

Sin embargo, la identidad del conocimiento debe permanecer invariable.

---

# Problema

Si los documentos se identifican únicamente mediante su nombre o ruta:

* un cambio de nombre rompe referencias;
* mover un archivo invalida enlaces;
* futuras aplicaciones dependerán de la estructura física del repositorio.

Es necesario disponer de un identificador independiente de la ubicación del documento.

---

# Decisión

Todos los documentos dispondrán de un identificador único y permanente almacenado en el Front Matter YAML.

Este identificador nunca cambiará durante la vida del documento.

El nombre del archivo podrá modificarse cuando resulte conveniente sin afectar a la identidad del contenido.

---

# Formato

El identificador estará compuesto por:

* un prefijo que identifica el tipo de documento;
* un número secuencial de cuatro cifras.

Ejemplos:

```text
ARC-0001
ARC-0002

BAS-0001
BAS-0002

REC-0001
REC-0002

ING-0001

PLA-0001

TAB-0001

NOT-0001
```

---

# Prefijos

| Tipo         | Prefijo |
| ------------ | ------- |
| Arquitectura | ARC     |
| Base         | BAS     |
| Receta       | REC     |
| Ingrediente  | ING     |
| Plantilla    | PLA     |
| Tabla        | TAB     |
| Nota         | NOT     |

---

# Reglas

## El identificador nunca cambia

Aunque cambie:

* el nombre;
* la carpeta;
* la estructura;
* el contenido.

El identificador permanece constante.

---

## Un identificador no se reutiliza

Si un documento desaparece:

```text
REC-0045
```

nunca volverá a asignarse.

---

## El identificador es único

No pueden existir dos documentos con el mismo identificador.

---

## Los identificadores no transmiten significado

El identificador identifica.

No clasifica.

La clasificación pertenece a:

* tipo;
* categoría;
* etiquetas;
* referencias.

---

# Ejemplo

```yaml
---
id: REC-0017
tipo: receta
titulo: Arroz Chaufa
---
```

Aunque posteriormente el archivo pase de:

```text
01_Arroces/arroz_chaufa.md
```

a

```text
07_Cocina_Asiatica/chaufa_peruano.md
```

seguirá siendo:

```text
REC-0017
```

---

# Justificación

Separar identidad y ubicación aporta:

* estabilidad;
* independencia del sistema de archivos;
* facilidad para reorganizar el repositorio;
* compatibilidad con futuras aplicaciones.

---

# Alternativas consideradas

## Utilizar únicamente el nombre del archivo

**Descartado**.

Los nombres evolucionan.

No constituyen identificadores estables.

---

## Utilizar la ruta completa

**Descartado**.

La estructura del repositorio puede modificarse.

---

## Utilizar UUID

**Descartado**.

Aunque técnicamente adecuado, resulta poco legible para un repositorio mantenido manualmente.

Los identificadores secuenciales son suficientes y más cómodos para el autor.

---

# Consecuencias

## Ventajas

* Identidad permanente.
* Reorganización segura del repositorio.
* Compatibilidad con bases de datos futuras.
* Integración sencilla con APIs.
* Facilidad para construir grafos de conocimiento.

## Inconvenientes

* Necesidad de gestionar la asignación de nuevos identificadores.
* Riesgo de duplicados si no se siguen las normas.

---

# Impacto futuro

Los identificadores podrán utilizarse como clave primaria en:

* aplicaciones móviles;
* sitios web;
* motores de búsqueda;
* bases de datos;
* APIs REST;
* GraphQL;
* sistemas RAG;
* asistentes culinarios basados en IA.

El repositorio Markdown seguirá siendo la fuente de verdad, mientras que el identificador actuará como referencia estable entre todos los sistemas.

---

# Dependencias

* [ADR-0003 - El Repositorio Markdown como Fuente Única de Verdad](./ADR-0003-markdown-como-fuente-de-verdad.md)
* [ADR-0004 - Front Matter YAML como Metadatos Canónicos](./ADR-0004-front-matter-yaml.md)
* [ADR-0007 - Modelo de Dominio del Sistema de Gestión del Conocimiento Culinario](./ADR-0007-modelo-de-dominio-del-sgcc.md)

---

# Véase también

* [ESPECIFICACION_DE_DOCUMENTOS](../../ESPECIFICACION_DE_DOCUMENTOS.md)
* [GUIA_DE_ESTILO](../../GUIA_DE_ESTILO.md)

---

# Utilizado por

Todos los documentos del proyecto deberán disponer de un identificador único y estable definido conforme a este ADR.
