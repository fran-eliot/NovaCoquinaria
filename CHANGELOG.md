# CHANGELOG

Todas las modificaciones relevantes del proyecto **NovaCoquinaria / GASTRO** se documentarán en este archivo.

El formato está inspirado en **Keep a Changelog**, adaptado a las necesidades del proyecto.

---

# Tipos de cambios

## Añadido

Nuevos documentos, recetas, técnicas, ingredientes, tablas o módulos.

## Modificado

Cambios funcionales importantes, reorganización de documentos o cambios de estructura.

## Mejorado

Ampliaciones, explicaciones más completas, nuevas referencias cruzadas o mejoras documentales.

## Corregido

Corrección de errores, cantidades, tiempos, enlaces, ortografía o referencias.

## Eliminado

Documentos retirados, información obsoleta o duplicidades eliminadas.

---

# Versionado

El proyecto sigue versionado semántico adaptado:

```text
MAJOR.MINOR.PATCH
```

Ejemplos:

```text
1.0.0
1.1.0
1.1.1
2.0.0
```

---

# Historial

## [1.0.0] - 2026-07-04

### Añadido

* Arquitectura documental completa del proyecto.
* Documentos principales:

  * `README.md`
  * `GUIA_DE_ESTILO.md`
  * `ESPECIFICACION_DE_DOCUMENTOS.md`
  * `CONTRIBUTING.md`
  * `CHANGELOG.md`
  * `LICENSE.md`
* Documentación estratégica:

  * `docs/ARQUITECTURA.md`
  * `docs/VISION.md`
  * `docs/ROADMAP.md`
* ADR fundacionales.
* Módulo `98_Tablas` con tablas de referencia culinaria.
* Módulo `00_Bases` con fundamentos y técnicas iniciales.
* Módulo `11_Despensa` con ingredientes fundamentales, especialmente de cocina asiática.
* Módulo `12_Plantillas` con patrones culinarios reutilizables.
* Colección inicial de recetas normalizadas.

### Mejorado

* Separación entre recetas, técnicas, ingredientes, tablas y plantillas.
* Uso de Front Matter YAML en documentos estructurados.
* Uso de identificadores únicos y estables.
* Referencias cruzadas entre documentos.
* Reutilización del conocimiento culinario para evitar duplicidades.
* Organización del repositorio como base de conocimiento, no como recetario plano.

### Modificado

* Evolución del proyecto desde **GASTRO** como repositorio personal hacia **NovaCoquinaria** como marca y producto documental.
* Refactorización de la estructura inicial para soportar crecimiento modular.
* Normalización de las recetas originales siguiendo el modelo del SGCC.

---

# Próximas versiones

## [1.1.0] - Pendiente

Objetivos posibles:

* Revisión editorial completa.
* Validación de enlaces relativos.
* Mejora de Front Matter.
* Nuevas recetas basadas en plantillas existentes.
* Primeras automatizaciones de validación.
* Preparación para publicación web con MkDocs.

---

# Criterios

Registrar únicamente cambios significativos.

No registrar:

* pequeñas correcciones tipográficas;
* cambios de formato sin impacto;
* modificaciones temporales.

El objetivo del historial es reflejar la evolución funcional del repositorio.

