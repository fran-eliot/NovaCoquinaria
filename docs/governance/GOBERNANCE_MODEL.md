---
id: GOV-0000
tipo: gobernanza
titulo: Modelo de Gobernanza del SGCC
version: 1.0
estado: estable
ultima_revision: 2026-07-29
---

# Modelo de Gobernanza del SGCC

> Proyecto: NovaCoquinaria
> Sistema: GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Propósito

Este documento ofrece una visión global del modelo de gobernanza del Sistema de Gestión del Conocimiento Culinario (SGCC).

No describe la implementación del sistema.

No sustituye a la arquitectura.

Su objetivo consiste en explicar cómo se relacionan los distintos modelos que gobiernan la evolución del conocimiento.

---

# Principio fundamental

El SGCC no es un repositorio de recetas.

Es un sistema diseñado para gestionar conocimiento culinario reutilizable.

Las recetas constituyen únicamente una aplicación de dicho conocimiento.

---

# Modelo general

```text
                        VISIÓN
                           │
                           ▼
                    GOBERNANZA
                           │
 ┌──────────────┬──────────────┬──────────────┐
 │              │              │              │
 ▼              ▼              ▼              ▼
Arquitectura  Estrategia    Calidad      IA / ADR
 │              │              │              │
 └──────────────┴──────────────┴──────────────┘
                │
                ▼
      Modelo del Conocimiento
                │
 ┌──────────────┼──────────────┐
 ▼              ▼              ▼
Documentos  Colecciones  Grafo de conocimiento
                │
                ▼
          Técnicas · Ingredientes
                │
                ▼
             Recetas
                │
                ▼
          Publicación / Consumo
```

---

# Capas del sistema

## Visión

Define el propósito del proyecto y su dirección a largo plazo.

Responde a la pregunta:

> ¿Por qué existe NovaCoquinaria?

---

## Gobernanza

Establece las reglas que permiten evolucionar el sistema de forma coherente.

La gobernanza está formada por:

- Arquitectura.
- Estrategia.
- Calidad.
- Gestión de decisiones.
- Colaboración con IA.

---

## Arquitectura

Define cómo está organizado el SGCC.

No depende de una implementación concreta.

---

## Modelo del conocimiento

Define cómo se representa el conocimiento culinario.

Incluye:

- documentos;
- colecciones;
- relaciones;
- reutilización.

---

## Dominio culinario

Representa el conocimiento propiamente dicho.

Ejemplos:

- ingredientes;
- técnicas;
- procesos;
- utensilios;
- recetas.

---

## Consumo

Corresponde a las diferentes formas de utilizar el conocimiento.

Por ejemplo:

- documentación;
- sitio web;
- IA;
- futuras aplicaciones.

---

# Modelos de gobernanza

La gobernanza del SGCC se articula mediante varios modelos especializados.

## Modelo arquitectónico

Organiza el sistema.

Documento principal:

ARQUITECTURA.md

---

## Modelo documental

Define cómo se representa el conocimiento.

Documentos principales:

- ESPECIFICACION_DE_DOCUMENTOS
- ESPECIFICACION_DE_COLECCIONES
- GUIA_DE_ESTILO

---

## Modelo de calidad

Define qué significa calidad dentro del SGCC.

Documento principal:

QUALITY.md

---

## Modelo estratégico

Define cómo evoluciona el conocimiento.

Documento principal:

KNOWLEDGE_STRATEGY.md

---

## Modelo de madurez

Evalúa el grado de consolidación del conocimiento.

Documento principal:

KNOWLEDGE_MATURITY.md

---

## Modelo de deuda

Gestiona las oportunidades de mejora.

Documento principal:

KNOWLEDGE_DEBT.md

---

## Modelo de automatización

Define la infraestructura que genera artefactos derivados.

Documentos principales:

- AUTOMATION.md
- QUALITY_PIPELINE.md
- TOOLS_FRAMEWORK.md

---

## Modelo de colaboración con IA

Regula la interacción entre el proyecto y los sistemas inteligentes.

Documento principal:

AI_PROTOCOL.md

---

# Principios del sistema

Todo el SGCC se basa en unos principios comunes.

- Markdown es la fuente de verdad.
- El conocimiento se documenta una única vez.
- La reutilización tiene prioridad sobre la duplicación.
- La arquitectura prevalece sobre la implementación.
- La calidad prevalece sobre la velocidad.
- La evolución debe ser incremental.
- Toda decisión importante debe quedar documentada.

---

# Evolución

El crecimiento del SGCC sigue un proceso continuo.

```text
Visión

↓

Estrategia

↓

Arquitectura

↓

Conocimiento reutilizable

↓

Recetas

↓

Calidad

↓

Madurez

↓

Nuevas oportunidades
```

La evolución nunca se basa únicamente en añadir contenido.

También implica mejorar su organización, calidad e integración.

---

# Relación con otros documentos

| Documento | Responsabilidad |
|-----------|-----------------|
| VISION | Propósito del proyecto |
| ARQUITECTURA | Organización del sistema |
| QUALITY | Modelo de calidad |
| KNOWLEDGE_STRATEGY | Evolución |
| KNOWLEDGE_MATURITY | Consolidación |
| KNOWLEDGE_DEBT | Mejora continua |
| AI_PROTOCOL | Colaboración con IA |
| ADR | Registro de decisiones |

---

# Conclusión

El SGCC constituye un sistema de gestión del conocimiento culinario gobernado mediante modelos especializados.

Cada documento describe una responsabilidad concreta.

La combinación de estos modelos permite que NovaCoquinaria evolucione de forma coherente, mantenible y preparada para el largo plazo.