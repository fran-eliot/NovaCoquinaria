---
id: ARC-0016
tipo: arquitectura
titulo: Pipeline de Calidad
version: 1.0
estado: borrador
ultima_revision: 2026-07-08
---

# Pipeline de Calidad

## Objetivo

Este documento define el proceso de validación documental de NovaCoquinaria.

El objetivo del pipeline es detectar problemas antes de publicar la documentación o incorporar cambios al repositorio.

No modifica el contenido del proyecto; únicamente verifica su consistencia.

---

## Filosofía

La calidad se basa en tres principios:

- prevenir errores antes de publicar;
- automatizar comprobaciones repetitivas;
- mantener la simplicidad de la arquitectura.

El pipeline nunca sustituye la revisión editorial.

---

## Fuente de verdad

Todo el proceso parte del contenido Markdown del repositorio.

```text
Repositorio Markdown
        │
        ▼
Validaciones
        │
        ▼
Generación de site_docs
        │
        ▼
MkDocs
        │
        ▼
Sitio publicado
```

---

## Fases del pipeline

### 1. Validación estructural

Comprobaciones básicas:

- existencia de Front Matter;
- formato correcto del YAML;
- identificadores presentes;
- metadatos obligatorios.

Herramienta prevista:

```text
validate_frontmatter.py
```

---

### 2. Validación documental

Comprobaciones de integridad:

- identificadores únicos;
- enlaces internos válidos;
- referencias existentes.

Herramientas previstas:

```text
validate_ids.py
validate_links.py
```

---

### 3. Generación

Una vez superadas las validaciones:

```text
build_site_docs.py
```

genera la documentación publicada.

---

### 4. Publicación

MkDocs construye el sitio web utilizando exclusivamente:

```text
site_docs/
```

---

## Errores bloqueantes

El pipeline deberá detenerse cuando detecte:

- IDs duplicados;
- Front Matter inválido;
- enlaces internos rotos;
- referencias a documentos inexistentes.

---

## Advertencias

Podrán notificarse sin bloquear el proceso:

- documentos sin referencias cruzadas;
- metadatos opcionales ausentes;
- secciones recomendadas no presentes.

---

## Evolución futura

El pipeline podrá ampliarse con:

- generación automática de índices;
- estadísticas del conocimiento;
- detección de documentos huérfanos;
- validación semántica;
- generación del grafo de conocimiento.

---

## Referencias

- [AUTOMATION](AUTOMATION.md)
- [QUALITY](../QUALITY.md)
- [ARQUITECTURA](../ARQUITECTURA.md)