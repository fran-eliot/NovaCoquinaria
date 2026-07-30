# ADR-0013 — Gobernanza de la Publicación y Apertura del Conocimiento

**Identificador:** ADR-0013

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Gobernanza

---

# Contexto

El SGCC se desarrolla inicialmente como un sistema de conocimiento de carácter privado.

Sin embargo, su arquitectura está diseñada para permitir distintos modelos de distribución en el futuro:

- repositorio privado;
- documentación pública;
- portal web;
- aplicación;
- proyecto Open Source;
- portfolio profesional;
- servicios basados en conocimiento.

Cada uno de estos escenarios implica requisitos distintos en materia de privacidad, propiedad intelectual y licenciamiento.

---

# Problema

La publicación del conocimiento no puede depender únicamente de hacer público un repositorio.

Es necesario definir un proceso que garantice:

- la protección de información sensible;
- el respeto a los derechos de autor;
- la correcta gestión de licencias;
- la coherencia entre los distintos tipos de contenido;
- la evolución controlada desde un entorno privado hacia uno público.

---

# Decisión

La apertura del conocimiento del SGCC se regirá mediante un proceso de gobernanza independiente de las tecnologías de publicación.

Todo contenido deberá considerarse privado por defecto y únicamente podrá incorporarse a una distribución pública tras superar el proceso de revisión correspondiente.

Las decisiones relativas a licencias y modelos de distribución se adoptarán en el momento de la publicación y podrán diferenciarse según la naturaleza del contenido.

---

# Justificación

Separar el modelo de conocimiento de su estrategia de distribución permite que el SGCC evolucione de forma segura y sostenible.

La gobernanza de la publicación protege tanto el conocimiento como los derechos asociados a su utilización.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- La privacidad es el estado inicial del conocimiento.
- La publicación requiere una revisión explícita.
- El conocimiento público y el privado pueden coexistir.
- La estrategia de licencias podrá diferenciar código, documentación y otros recursos.
- La publicación constituye un proceso de gobernanza y no una operación técnica.

---

# Modelo conceptual

```text
          Conocimiento

                │

         Estado Privado

                │

     Revisión de Publicación

                │

      Conocimiento Público

                │

      Distribución y Licencias
```

La revisión actúa como mecanismo de control entre ambos estados.

---

# Ámbitos de gobernanza

La publicación deberá contemplar, entre otros aspectos:

- privacidad;
- información sensible;
- propiedad intelectual;
- derechos de terceros;
- atribuciones;
- recursos externos;
- licencias;
- canales de distribución.

Las reglas concretas podrán evolucionar sin modificar esta decisión arquitectónica.

---

# Alternativas consideradas

## Publicación directa del repositorio

Descartada por no garantizar la revisión del contenido.

---

## Utilizar una única licencia para todo el proyecto

Descartada como decisión obligatoria, al coexistir distintos tipos de activos con necesidades diferentes.

---

## Mantener el proyecto permanentemente privado

Descartada por limitar la reutilización futura del conocimiento y su posible difusión.

---

# Consecuencias

## Ventajas

- Mayor protección del conocimiento.
- Mejor control de la privacidad.
- Flexibilidad para futuros modelos de distribución.
- Compatibilidad con distintos esquemas de licenciamiento.
- Evolución segura hacia proyectos públicos.

---

## Inconvenientes

- Requiere procesos adicionales de revisión.
- Incrementa ligeramente el esfuerzo previo a cada publicación.

---

# Impacto arquitectónico

Esta decisión desacopla la evolución del conocimiento de su estrategia de distribución.

Como consecuencia:

- podrán coexistir versiones públicas y privadas del SGCC;
- distintos activos podrán utilizar licencias diferentes;
- la apertura del conocimiento quedará gobernada mediante procesos explícitos;
- la evolución tecnológica no condicionará la política de publicación.

---

# Relación con otros ADR

Este ADR desarrolla:

- ADR-0010 — Arquitectura Orientada al Conocimiento.
- ADR-0011 — Modelo de Capas Conceptuales del Proyecto.
- ADR-0012 — Independencia entre el Modelo de Conocimiento y su Publicación.

Se complementa con:

- AI_PROTOCOL.md
- QUALITY.md
- KNOWLEDGE_STRATEGY.md

---

# Documentación relacionada

La aplicación práctica de esta decisión se desarrolla en:

- GOVERNANCE_MODEL.md
- PROJECT_ONBOARDING.md
- LICENSE.md
- README.md

La elección de licencias concretas (MIT, Apache, GPL, Creative Commons u otras) constituye una decisión de gestión del proyecto y podrá evolucionar sin modificar este ADR.

---

# Estado actual

La decisión continúa plenamente vigente.

El SGCC mantiene una estrategia de publicación basada en la gobernanza del conocimiento, donde la privacidad, el licenciamiento y la distribución forman parte de un proceso controlado que protege tanto la integridad del sistema como los derechos asociados a su utilización.