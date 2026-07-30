---
id: DOC-0017
titulo: Arquitectura de NovaCoquinaria
tipo: architecture
estado: active
version: 1.0.0
creado: 2026-06-29
ultima_revision: 2026-07-30
---

# ARQUITECTURA

> **Proyecto:** NovaCoquinaria  
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento describe la arquitectura del Sistema de Gestión del Conocimiento Culinario (SGCC) implementado por NovaCoquinaria.

Su propósito es explicar cómo se estructura el sistema, cuáles son sus componentes principales y cómo interactúan entre sí para preservar, organizar y reutilizar conocimiento culinario de forma coherente.

No describe la visión estratégica del proyecto, sus principios fundamentales ni el detalle de las entidades del modelo de conocimiento. Esos aspectos se desarrollan en la documentación especializada correspondiente.

---

# Arquitectura del SGCC

NovaCoquinaria implementa un **Sistema de Gestión del Conocimiento Culinario (SGCC)** cuya arquitectura conceptual recibe el nombre de **GASTRO**.

La arquitectura establece cómo debe organizarse el conocimiento y cómo interactúan los distintos componentes del sistema, independientemente de las herramientas que lo implementen.

```text
                   NovaCoquinaria
                         │
              Implementa la arquitectura
                         │
                         ▼
                     GASTRO
          (Arquitectura conceptual)
                         │
                   Define el SGCC
                         │
                         ▼
        Sistema de Gestión del Conocimiento
                         │
          Implementado mediante Markdown
                         │
                         ▼
            Repositorio de conocimiento
                         │
                         ▼
              Consumido por aplicaciones
```

La arquitectura separa claramente:

- el conocimiento;
- su representación documental;
- las herramientas que lo gestionan;
- las aplicaciones que lo utilizan.

Esta separación garantiza la independencia tecnológica y facilita la evolución del sistema.

---

# Componentes arquitectónicos

El SGCC se compone de cuatro grandes bloques.

```text
                 GASTRO (SGCC)

        ┌────────────┬─────────────┬─────────────┐
        │            │             │             │
        ▼            ▼             ▼             ▼

 Modelo de     Gobernanza    Automatización  Consumo

 conocimiento

```

## Modelo de conocimiento

Representa el núcleo funcional del sistema.

Define las entidades culinarias, sus relaciones y las reglas de organización del conocimiento.

Se desarrolla en **MODELO_DE_CONOCIMIENTO.md**.

---

## Gobernanza

Define las normas que permiten mantener una arquitectura coherente durante toda la evolución del proyecto.

Incluye:

- ADR;
- workflow;
- convenciones;
- control de calidad;
- versionado.

---

## Automatización

Agrupa las herramientas responsables de mantener la calidad y consistencia del sistema.

Incluye:

- validadores;
- generación del Knowledge Graph;
- construcción de MkDocs;
- scripts de apoyo.

---

## Consumo

Comprende todas las aplicaciones capaces de utilizar el conocimiento almacenado sin modificar su estructura conceptual.

Ejemplos:

- portal web;
- aplicación móvil;
- API;
- buscadores;
- asistentes basados en IA;
- sistemas RAG;
- agentes especializados.

---

# Capas del sistema

La arquitectura organiza el SGCC en capas claramente diferenciadas.

```text
        Aplicaciones consumidoras
────────────────────────────────────────

       Automatización y herramientas
────────────────────────────────────────

     Representación documental (Markdown)
────────────────────────────────────────

      Modelo de conocimiento (SGCC)
────────────────────────────────────────

        Conocimiento culinario
```

Cada capa posee una única responsabilidad y depende exclusivamente de la inmediatamente inferior.

Las capas superiores nunca modifican el modelo conceptual del conocimiento.

---

# Arquitectura lógica

Desde un punto de vista lógico, el sistema organiza el conocimiento mediante entidades especializadas relacionadas entre sí.

```text
                 Conocimiento

                       │

        ┌──────────────┼──────────────┐
        │              │              │

 Ingredientes     Técnicas      Patrones

        │              │              │
        └──────────────┼──────────────┘
                       │

                Platos canónicos
                       │
                  Variantes
                       │
                    Recetas
                       │
                  Menús (futuro)
```

Las entidades forman una red de conocimiento donde cada una mantiene una responsabilidad específica y puede evolucionar de forma independiente.

El detalle del modelo se documenta en **MODELO_DE_CONOCIMIENTO.md**.

---

# Arquitectura física

La implementación actual del SGCC utiliza un repositorio Git basado en documentos Markdown.

```text
Repositorio

├── Conocimiento culinario
│
├── Documentación
│
├── Herramientas
│
├── Publicación
│
└── Configuración
```

La estructura física facilita el mantenimiento del sistema, pero no define su organización lógica.

La arquitectura conceptual permanece independiente de la disposición de los archivos dentro del repositorio.

---

# Flujo del conocimiento

Todo conocimiento incorporado al sistema sigue un proceso continuo de evolución.

```text
Experiencia

      │

Investigación

      │

Formalización

      │

Integración

      │

Relaciones

      │

Reutilización

      │

Validación

      │

Mejora continua
```

El objetivo del flujo no consiste únicamente en almacenar información, sino en transformarla en conocimiento reutilizable integrado dentro del SGCC.

---

# Arquitectura de consumo

El conocimiento constituye el único origen de información para todas las aplicaciones presentes y futuras.

```text
          Base de conocimiento

                   │

      ┌────────────┼────────────┐
      │            │            │

     Web          API          IA

      │            │            │

     App       Buscador      Agentes

```

Todas las aplicaciones consumen el mismo conocimiento.

Ninguna de ellas constituye la fuente de verdad del sistema.

---

# Evolución arquitectónica

La arquitectura está diseñada para evolucionar de forma incremental.

La incorporación de nuevas entidades, dominios o herramientas no debe requerir modificaciones estructurales significativas.

Las futuras implementaciones deberán respetar siempre los siguientes principios arquitectónicos:

- preservar la independencia del conocimiento;
- mantener la separación entre arquitectura lógica y estructura física;
- favorecer la reutilización;
- minimizar la duplicación;
- garantizar la evolución sostenible del sistema.

Las decisiones que afectan a la arquitectura se documentan mediante **Architecture Decision Records (ADR)**.

Este documento describe la arquitectura vigente.

Los ADR documentan el proceso mediante el cual dicha arquitectura evoluciona.

---

# Relaciones entre documentos

La arquitectura forma parte de un conjunto de documentos especializados.

| Documento | Responsabilidad |
|-----------|-----------------|
| README | Punto de entrada al proyecto |
| NovaCoquinaria | Identidad del proyecto |
| VISION | Dirección estratégica |
| MANIFESTO | Principios permanentes |
| **ARQUITECTURA** | Diseño global del SGCC |
| MODELO_DE_CONOCIMIENTO | Entidades y relaciones |
| ADR | Decisiones arquitectónicas |

Cada documento desarrolla una única responsabilidad dentro del sistema documental.

---

# Documentación relacionada

## Identidad

- [NovaCoquinaria](../../NovaCoquinaria.md)

## Estrategia

- [VISION](../VISION.md)
- [MANIFESTO](../../MANIFESTO.md)

## Modelo del sistema

- [MODELO_DE_CONOCIMIENTO](./MODELO_DE_CONOCIMIENTO.md)

## Gobernanza

- [CONTEXT](../../CONTEXT.md)
- [DEVELOPMENT_WORKFLOW](../management/DEVELOPMENT_WORKFLOW.md)

## Decisiones arquitectónicas

- [ADR](../governance/adr/README.md)

---

# Conclusión

La arquitectura de GASTRO proporciona un marco estable para organizar, preservar y hacer evolucionar conocimiento culinario de forma independiente de cualquier tecnología concreta.

NovaCoquinaria constituye la implementación actual de dicha arquitectura, demostrando que un Sistema de Gestión del Conocimiento Culinario puede mantenerse coherente mediante una clara separación entre conocimiento, arquitectura, documentación, automatización y aplicaciones consumidoras.

La arquitectura no define únicamente cómo está construido el sistema.

Define cómo podrá seguir evolucionando durante muchos años sin perder coherencia.
