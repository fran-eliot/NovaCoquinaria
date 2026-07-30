# CONTEXT

> **Proyecto:** NovaCoquinaria  
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento constituye el **índice maestro de la documentación** de NovaCoquinaria.

Su finalidad es facilitar la navegación por el sistema documental, indicando dónde se encuentra cada tipo de información y cuál es la responsabilidad de cada documento.

No sustituye al README, al onboarding ni a la documentación especializada.

Su única responsabilidad consiste en orientar al lector hacia la documentación adecuada.

---

# Mapa documental

```text
NovaCoquinaria
│
├── Identidad
├── Arquitectura
├── Gobernanza
├── Gestión
├── Operación
└── Conocimiento
```

---

# Estructura documental

## Identidad

Describe qué es el proyecto y cuál es su propósito.

| Documento | Responsabilidad |
|-----------|-----------------|
| README | Punto de entrada al proyecto |
| NovaCoquinaria | Identidad del proyecto |
| MANIFESTO | Principios permanentes |
| VISION | Dirección estratégica |

---

## Arquitectura

Describe cómo está diseñado el sistema.

| Documento | Responsabilidad |
|-----------|-----------------|
| ARQUITECTURA | Diseño global del SGCC |
| MODELO_DE_CONOCIMIENTO | Modelo conceptual del conocimiento |
| ADR | Evolución arquitectónica |

---

## Gobernanza

Define cómo se mantiene y evoluciona el proyecto.

| Documento | Responsabilidad |
|-----------|-----------------|
| CONTEXT | Índice maestro |
| PROJECT_STRUCTURE | Organización física del repositorio |
| PROJECT_ONBOARDING | Incorporación de colaboradores |
| CONTRIBUTING | Normas de contribución |
| DEVELOPMENT_WORKFLOW | Proceso oficial de desarrollo |

---

## Gestión

Permite conocer el estado y evolución del proyecto.

| Documento | Responsabilidad |
|-----------|-----------------|
| PROJECT_STATUS | Estado actual |
| ROADMAP | Evolución prevista |
| BITACORA | Historial de hitos |
| RELEASES | Versiones publicadas |
| CHANGELOG | Historial de cambios |

---

## Operación

Describe el funcionamiento operativo del proyecto.

| Documento | Responsabilidad |
|-----------|-----------------|
| QUALITY | Calidad documental |
| GUIA_DE_ESTILO | Convenciones de escritura |
| ESPECIFICACION_DE_DOCUMENTOS | Estructura documental |
| TOOLS | Herramientas del proyecto |

---

## Conocimiento

Documenta el dominio culinario gestionado por el SGCC.

Incluye:

- ingredientes;
- técnicas;
- patrones culinarios;
- platos canónicos;
- variantes;
- recetas;
- tablas;
- bases culinarias.

---

# Recorridos recomendados

## Quiero conocer el proyecto

1. README
2. NovaCoquinaria
3. VISION
4. MANIFESTO

---

## Quiero comprender la arquitectura

1. ARQUITECTURA
2. MODELO_DE_CONOCIMIENTO
3. ADR

---

## Quiero empezar a colaborar

1. PROJECT_ONBOARDING
2. CONTRIBUTING
3. DEVELOPMENT_WORKFLOW

---

## Quiero saber en qué estado está el proyecto

1. PROJECT_STATUS
2. BITACORA
3. ROADMAP
4. RELEASES

---

## Quiero localizar un documento

Utiliza la estructura documental de este índice para identificar el área funcional correspondiente.

Cada documento del proyecto posee una única responsabilidad.

---

# Principios de navegación

La documentación del proyecto sigue las siguientes reglas:

- un documento, una responsabilidad;
- una responsabilidad, un documento;
- referencias cruzadas antes que duplicación;
- evolución mediante ADR;
- Markdown como fuente de verdad;
- navegación basada en responsabilidades y no únicamente en directorios.

---

# Mantenimiento

Siempre que se incorpore un nuevo documento relevante deberá evaluarse su inclusión en este índice.

CONTEXT constituye el punto central de navegación de toda la documentación del proyecto y debe mantenerse sincronizado con la arquitectura documental vigente.