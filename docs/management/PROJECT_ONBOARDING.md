# Incorporación al Proyecto

> Guía rápida para comprender NovaCoquinaria y comenzar a colaborar en su desarrollo.

---

# Objetivo

Este documento proporciona el contexto mínimo necesario para comprender el proyecto y continuar su evolución sin necesidad de reconstruir todo su historial.

Está dirigido tanto a desarrolladores como a asistentes basados en inteligencia artificial.

---

# ¿Qué es NovaCoquinaria?

NovaCoquinaria es un **Sistema de Gestión del Conocimiento Culinario (SGCC)**.

Su objetivo no es únicamente almacenar recetas, sino organizar el conocimiento culinario mediante componentes reutilizables.

Las recetas son únicamente una parte del sistema.

---

# Filosofía

Los principios fundamentales del proyecto son:

- Documentar una sola vez.
- Reutilizar siempre.
- Evitar duplicidades.
- Priorizar la arquitectura sobre la automatización.
- Mantener Markdown como fuente de verdad.

---

# Organización

El conocimiento se divide en:

- Bases
- Recetas
- Despensa
- Plantillas
- Tablas
- Documentación técnica

Cada documento debe tener una única responsabilidad.

---

# Publicación

El portal web utiliza MkDocs Material.

Sin embargo:

- MkDocs no es la fuente de verdad.
- Markdown es la fuente de verdad.
- `site_docs` es un artefacto generado.

Nunca editar:

```text
site_docs/
```

Los contenidos de site_docs se generan automáticamente mediante:

```bash
python tools/build_site_docs.py
```

Toda modificación realizada directamente en site_docs se perderá en la siguiente generación.

---

# Lectura recomendada

Para comprender el proyecto, consultar en este orden:

1. [PROJECT_STATUS](PROJECT_STATUS.md)
2. [ARQUITECTURA](../ARQUITECTURA.md)
3. [ROADMAP](../ROADMAP.md)
4. [DECISIONS_SUMMARY](DECISIONS_SUMMARY.md)
5. [BITACORA](BITACORA.md)
6. [ADR](../adr/README.md)

---

# Gobernanza del conocimiento

La evolución del conocimiento se gobierna mediante:

- [KNOWLEDGE_STRATEGY](KNOWLEDGE_STRATEGY.md)
- [KNOWLEDGE_DEBT](KNOWLEDGE_DEBT.md)
- [KNOWLEDGE_MATURITY](KNOWLEDGE_MATURITY.md)

Estos documentos definen respectivamente:

- cómo debe crecer el conocimiento;
- qué carencias estructurales existen;
- qué grado de madurez ha alcanzado.

---

# Calidad y herramientas

Antes de integrar cambios relevantes:

```bash
python tools/validate_all.py
python tools/generate_graph.py
python tools/generate_graph_stats.py
python tools/find_orphans.py
python tools/validate_semantics.py
```

El Knowledge Graph permite analizar la reutilización y conectividad del conocimiento.

---

# Gestión del proyecto

Consultar:

- [PROJECT_STATUS](PROJECT_STATUS.md)
- [BITACORA](BITACORA.md)
- [RELEASES](RELEASES.md)

---

# Convenciones

El proyecto utiliza:

- Semantic Versioning.
- Front Matter YAML.
- Referencias cruzadas.
- ADR.
- Pull Request por funcionalidad.
- Commits pequeños y descriptivos.

---

# Forma habitual de trabajo

1. Crear rama.
2. Implementar.
3. Revisar.
4. Commit.
5. Push.
6. Pull Request.
7. Merge.

---

# Qué evitar

No modificar:

- arquitectura SGCC;
- ADR aprobados;
- estructura del repositorio;
- `site_docs`;

sin una decisión arquitectónica explícita.

---

# Rol esperado del asistente

Cuando el proyecto se desarrolla con ayuda de un asistente IA, este debe actuar como:

- Arquitecto de software.
- Arquitecto documental.
- Revisor técnico.
- Experto en gestión del conocimiento.
- Experto culinario cuando sea necesario.

Debe priorizar siempre:

1. Coherencia.
2. Simplicidad.
3. Reutilización.
4. Mantenibilidad.

---

# Estado actual

Consultar:

- [PROJECT_STATUS](PROJECT_STATUS.md)

---

# Evolución

Consultar:

- [BITACORA](BITACORA.md)

---

# Futuro

Consultar:

- [ROADMAP](../ROADMAP.md)
- [FUTURE_IDEAS](FUTURE_IDEAS.md)

---

# Referencias

- [PROJECT_STATUS](PROJECT_STATUS.md)
- [BITACORA](BITACORA.md)
- [RELEASES](RELEASES.md)
- [ARQUITECTURA](../ARQUITECTURA.md)
- [ROADMAP](../ROADMAP.md)