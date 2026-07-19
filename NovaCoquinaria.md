# NovaCoquinaria

> Construyendo un Sistema de Gestión del Conocimiento Culinario reutilizable, evolutivo e independiente de la tecnología.

---

# ¿Qué es?

NovaCoquinaria es un proyecto personal de ingeniería del conocimiento cuyo objetivo es construir y mantener un Sistema de Gestión del Conocimiento Culinario (SGCC), cuya arquitectura conceptual recibe el nombre de GASTRO.

No se centra en almacenar recetas, sino en capturar, estructurar, relacionar y reutilizar conocimiento culinario de forma modular, evolutiva e independiente de cualquier tecnología concreta.

El proyecto combina principios de cocina, gestión documental e ingeniería del software para preservar conocimiento útil durante toda la vida.

---

# ¿Por qué existe?

La mayoría de recetarios repiten continuamente:

- técnicas;
- ingredientes;
- consejos;
- tiempos;
- explicaciones.

NovaCoquinaria evita esa duplicación.

Cada conocimiento se documenta una sola vez y las recetas lo reutilizan mediante referencias.

El objetivo es reducir la duplicación, mejorar la consistencia y facilitar la evolución del conocimiento a largo plazo.

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

# Qué hace diferente a NovaCoquinaria

NovaCoquinaria organiza el conocimiento en entidades reutilizables.

Las recetas representan únicamente una aplicación concreta de dicho conocimiento.

El conocimiento se estructura mediante:

- ingredientes;
- técnicas;
- patrones culinarios;
- platos canónicos;
- variantes;
- tablas de referencia.

Todos ellos forman una red de conocimiento conectada mediante relaciones explícitas.

Cada entidad puede evolucionar de forma independiente sin afectar a la organización global del conocimiento.

---

# Objetivos

## Objetivos del proyecto

- preservar conocimiento culinario verificable y reutilizable;
- reutilizar conocimiento;
- facilitar el aprendizaje continuo;
- servir de base para herramientas futuras.

## Próximos hitos

- consolidar el modelo de conocimiento;
- ampliar el grafo;
- automatizar validaciones;
- enriquecer las colecciones culinarias.

---

# Valores

NovaCoquinaria apuesta por:

- claridad;
- calidad;
- mantenibilidad;
- reutilización;
- aprendizaje continuo.

---

## GASTRO

La arquitectura interna que soporta NovaCoquinaria recibe el nombre de GASTRO (Sistema de Gestión del Conocimiento Culinario).

GASTRO define el modelo conceptual, las entidades, las relaciones y los principios que permiten organizar el conocimiento culinario de forma coherente y reutilizable.

```text
NovaCoquinaria
       │
       ▼
GASTRO (SGCC)
       │
 ┌─────┼───────────────┐
 ▼     ▼               ▼

Conocimiento  Documentación  Herramientas
```

---

# Público

Actualmente el proyecto está orientado principalmente a su autor.

Sin embargo, se diseña desde el principio para que pueda resultar útil a otras personas interesadas en documentar y organizar conocimiento culinario.

---

# Arquitectura Técnica

Para conocer la arquitectura, consulte [ARQUITECTURA](./docs/ARQUITECTURA.md)

El proyecto utiliza actualmente:

## Modelo Documental

- Markdown
- Front Matter YAML
- Referencias cruzadas
- Mermaid
- Knowledge Graph documental

## Gobierno

- Architecture Decision Records (ADR)
- Semantic Versioning

## Herramientas e infraestructura

- Python
- PyYAML
- MkDocs
- MkDocs Material
- Knowledge Graph
- Git
- GitHub

---

# Estado

NovaCoquinaria ha superado la fase de definición inicial.

Actualmente dispone de:

- arquitectura documental estable;
- modelo de conocimiento formal;
- herramientas automáticas de validación;
- Knowledge Graph;
- publicación mediante MkDocs;
- estrategia de evolución documentada.

Consultar:

- [PROJECT_STATUS](./docs/management/PROJECT_STATUS.md)
- [ROADMAP](./docs/ROADMAP.md)
- [BITACORA](./docs/management/BITACORA.md)
- [Knowledge Strategy](./docs/management/KNOWLEDGE_STRATEGY.md)
- [Knowledge Debt](./docs/management/KNOWLEDGE_DEBT.md)
- [Knowledge Maturity](./docs/management/KNOWLEDGE_MATURITY.md)

El proyecto continúa evolucionando mediante un enfoque incremental basado en documentación, reutilización y mejora continua.

---

# Más que un repositorio

NovaCoquinaria no pretende organizar documentos.

Pretende organizar conocimiento.

Los documentos son únicamente la representación persistente de ese conocimiento.

Cualquier herramienta futura —sitio web, aplicación móvil, API o asistente basado en inteligencia artificial— deberá utilizar la misma base de conocimiento sin modificar su estructura conceptual.

---

# Visión

NovaCoquinaria aspira a convertirse en una plataforma abierta de ingeniería del conocimiento culinario donde documentación, herramientas y software evolucionen conjuntamente sobre una misma base de conocimiento.

---

> Documentar una vez. Relacionar siempre. Reutilizar continuamente