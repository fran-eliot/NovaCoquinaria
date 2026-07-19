# Incorporación al Proyecto

> Guía rápida para comprender NovaCoquinaria y comenzar a colaborar en su desarrollo.

Este documento asume que ya se ha leído el README y constituye el siguiente paso recomendado para comenzar a trabajar en el proyecto.

---

# Primeros 10 minutos

Si acabas de incorporarte al proyecto:

1. Lee [README](../../README.md)
2. Lee [NovaCoquinaria](../../NovaCoquinaria.md)
3. Consulta [CONTEXT](../../CONTEXT.md)
4. Revisa [PROJECT_STATUS](./PROJECT_STATUS.md)
5. Continúa con este documento.

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

- El conocimiento es el activo principal.

- Markdown constituye la fuente única de verdad.

- Documentar una sola vez.

- Reutilizar siempre.

- El modelo lógico es independiente del repositorio.

- El conocimiento evoluciona mediante pequeñas mejoras.

- Las decisiones arquitectónicas se documentan mediante ADR.

---

# Modelo de conocimiento

NovaCoquinaria organiza el conocimiento mediante entidades.

Las principales son:

- ingredientes;
- técnicas;
- patrones culinarios;
- platos canónicos;
- variantes;
- tablas de referencia.

Cada entidad posee una única responsabilidad y se relaciona con las demás mediante referencias explícitas.

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

1. [README](../../README.md)
2. [NovaCoquinaria](../../NovaCoquinaria.md)
3. [CONTEXT](../../CONTEXT.md)
4. [PROJECT_STATUS](PROJECT_STATUS.md)
5. [ARQUITECTURA](../ARQUITECTURA.md)
6. [Modelo de Conocimiento](../MODELO_DE_CONOCIMIENTO.md)
7. [DECISIONS_SUMMARY](DECISIONS_SUMMARY.md)
8. [ROADMAP](../ROADMAP.md)

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

Ningún cambio debe integrarse si compromete la coherencia del modelo de conocimiento, aunque las validaciones automáticas sean satisfactorias.

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

## Gobierno

- ADR.
- Semantic Versioning.

## Documentación

- Front Matter YAML.
- Referencias cruzadas.

## Desarrollo

- Pull Request por funcionalidad.
- Commits pequeños y descriptivos.

---

# Forma habitual de trabajo

```text
Comprender

↓

Diseñar

↓

Documentar

↓

Validar

↓

Relacionar

↓

Integrar
```

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

El asistente debe cuestionar las decisiones cuando detecte incoherencias con la arquitectura o con el modelo de conocimiento.

Su función no es únicamente ejecutar instrucciones, sino contribuir a preservar la calidad del sistema.

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

---

# Checklist de incorporación

Antes de empezar asegúrate de comprender:

☐ Qué es NovaCoquinaria.

☐ Qué es GASTRO.

☐ Cómo se organiza el conocimiento.

☐ Cuál es la fuente de verdad.

☐ Qué documentos gobiernan el proyecto.

☐ Cómo validar un cambio.

☐ Dónde consultar el estado del proyecto.

☐ Saber cuál es el papel de este documento dentro del sistema documental.