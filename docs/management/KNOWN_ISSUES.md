# Limitaciones Conocidas

> Registro de limitaciones, restricciones y decisiones conocidas del proyecto.

---

# Objetivo

Este documento recopila aquellas limitaciones que actualmente forman parte del proyecto y que no se consideran errores, sino decisiones conscientes, dependencias externas o mejoras pendientes.

No sustituye al gestor de incidencias ni al backlog.

---

# Publicación web

## GitHub Pages

Actualmente la publicación mediante GitHub Pages requiere evaluar la visibilidad del repositorio y la estrategia de publicación.

Estado: ⏳ Pendiente

---

## MkDocs

MkDocs genera avisos cuando existen documentos que no están incluidos en el `nav`.

Este comportamiento es esperado y no afecta al funcionamiento del portal.

Estado: ✅ Aceptado

---

## site_docs

`site_docs` es un directorio generado automáticamente.

Nunca debe editarse manualmente.

Cualquier cambio debe realizarse sobre la documentación original.

Estado: ✅ Arquitectura aprobada

---

# Arquitectura

## Markdown

Markdown constituye la única fuente de verdad del conocimiento.

Toda automatización debe generarse a partir de él.

Estado: ✅ Decisión arquitectónica

---

## Scripts

La publicación depende actualmente del script:

```text
tools/build_site_docs.py
```

Cualquier cambio estructural deberá mantener este principio de desacoplamiento.

Estado: ✅ Arquitectura aprobada

---

# Documentación

## Navegación

No todos los documentos aparecen en el menú principal de MkDocs.

Esto es intencionado para evitar una navegación excesivamente extensa.

Estado: ✅ Decisión de diseño

---

## ADR

Los ADR aprobados no deben modificarse salvo que exista una nueva decisión arquitectónica que los sustituya.

Estado: ✅ Política del proyecto

---

# Futuras mejoras

- Publicación automática.
- Validaciones automáticas.
- Índices generados automáticamente.
- Automatización del menú.
- Mejoras visuales del portal.

---

## Referencias

- [PROJECT_STATUS](PROJECT_STATUS.md)
- [BITACORA](BITACORA.md)
- [ROADMAP](../ROADMAP.md)
