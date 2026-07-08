---
id: ARC-0017
tipo: arquitectura
titulo: Framework de Herramientas
version: 1.0
estado: borrador
ultima_revision: 2026-07-08
---

# Framework de Herramientas

## Objetivo

Este documento describe la arquitectura del framework de herramientas utilizado para mantener y validar NovaCoquinaria.

Su finalidad es proporcionar una base común para todas las utilidades del proyecto, evitando duplicidades y facilitando su evolución.

---

## Principios

El framework sigue los mismos principios que el SGCC:

- una única responsabilidad por herramienta;
- reutilización de código común;
- simplicidad;
- independencia entre módulos;
- facilidad de mantenimiento.

---

## Arquitectura

```text
tools/
│
├── common.py
│      Utilidades compartidas
│
├── models.py
│      Modelo documental
│
├── validate_*.py
│      Validaciones
│
├── generate_*.py
│      Generadores
│
└── build_*.py
       Procesos de construcción
```

---

## Componentes

### common.py

Centraliza funciones reutilizables:

- localización de documentos;
- lectura de archivos;
- extracción del Front Matter;
- impresión homogénea de mensajes.

---

### models.py

Define el modelo documental utilizado por las herramientas.

Actualmente incluye:

- `Document`

En el futuro podrá ampliarse con otros modelos especializados.

---

### Validadores

Su misión es detectar inconsistencias.

Nunca modifican documentos.

Ejemplos:

- Front Matter;
- IDs;
- enlaces.

---

### Generadores

Crean artefactos derivados sin modificar la fuente de verdad.

Ejemplos:

- estadísticas;
- índices;
- documentación publicada.

---

### Builder

Construye la documentación distribuible.

Actualmente:

- `build_site_docs.py`

---

## Evolución prevista

El framework podrá incorporar:

- validación semántica;
- detección de documentos huérfanos;
- análisis de referencias cruzadas;
- generación automática de índices;
- exportadores a otros formatos;
- comprobaciones para integración continua.

---

## Relación con el SGCC

El framework forma parte de la infraestructura del proyecto.

No contiene conocimiento culinario.

Su responsabilidad es garantizar la calidad y consistencia del conocimiento almacenado en Markdown.

---

## Referencias

- [AUTOMATION](AUTOMATION.md)
- [QUALITY_PIPELINE](QUALITY_PIPELINE.md)
- [ARQUITECTURA](../ARQUITECTURA.md)