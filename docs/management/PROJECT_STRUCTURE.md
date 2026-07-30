---
id: DOC-0021
titulo: Estructura del Proyecto
tipo: gestion
version: 2.0
estado: estable
ultima_revision: 2026-07-30
---

# PROJECT_STRUCTURE

> **Proyecto:** NovaCoquinaria  
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento describe la **estructura física del repositorio** de NovaCoquinaria.

Su finalidad es facilitar la localización de archivos y directorios, así como explicar la organización general del proyecto.

No define la arquitectura del SGCC ni el modelo de conocimiento.

La organización física del repositorio constituye únicamente una implementación del sistema documental.

---

# Principios de organización

La estructura del repositorio sigue los siguientes principios:

- organización por responsabilidades;
- separación entre conocimiento y documentación;
- independencia entre modelo lógico y estructura física;
- crecimiento incremental;
- simplicidad de navegación.

La ubicación de un documento no determina su significado conceptual.

---

# Organización general

```text
Repositorio

├── Conocimiento
├── Documentación
├── Infraestructura
├── Recursos
└── Publicación
```

---

# Directorios principales

## Conocimiento

Contiene el conocimiento culinario gestionado por el SGCC.

```text
00_Bases/
01_Arroces/
02_Pastas/
03_Legumbres/
04_Verduras/
05_Carnes/
06_Pescados_y_Mariscos/
07_Cocina_Asiatica/
08_Postres/
09_Bebidas/
10_Horno/
11_Despensa/
12_Plantillas/
98_Tablas/
99_Notas/
```

Cada directorio agrupa un dominio funcional del conocimiento.

La organización podrá evolucionar sin alterar el modelo conceptual.

---

## Documentación

Contiene la documentación técnica, arquitectónica y de gestión del proyecto.

```text
docs/
```

Incluye:

- arquitectura;
- gobernanza;
- gestión;
- decisiones arquitectónicas;
- diagramas;
- especificaciones.

---

## Herramientas

Contiene los procesos de automatización y validación.

```text
tools/
```

Incluye:

- validadores;
- generadores;
- scripts de mantenimiento;
- utilidades compartidas.

---

## Recursos

Contiene recursos auxiliares utilizados por el proyecto.

```text
assets/
```

Ejemplos:

- imágenes;
- iconografía;
- diagramas;
- recursos gráficos.

---

## Publicación

```text
site_docs/
```

Contiene la documentación generada automáticamente para MkDocs.

**Nunca debe editarse manualmente.**

Markdown continúa siendo la única fuente de verdad del sistema.

---

# Organización documental

La documentación se organiza por responsabilidades.

```text
Identidad

Arquitectura

Gobernanza

Gestión

Operación
```

La navegación entre documentos se realiza mediante referencias cruzadas y no mediante la estructura de carpetas.

---

# Organización del conocimiento

El conocimiento culinario se distribuye por dominios.

```text
Dominios

↓

Entidades

↓

Relaciones

↓

Recetas
```

La clasificación física facilita la navegación, pero no constituye el modelo del conocimiento.

---

# Relación entre estructura física y modelo lógico

El SGCC distingue claramente dos niveles.

## Modelo lógico

Describe:

- entidades;
- relaciones;
- reglas;
- restricciones.

Se documenta en:

- MODELO_DE_CONOCIMIENTO.md

---

## Estructura física

Describe:

- directorios;
- archivos;
- organización del repositorio.

Se documenta en este documento.

Ambos niveles evolucionan de forma independiente.

---

# Evolución de la estructura

La estructura física podrá modificarse cuando contribuya a:

- mejorar la navegación;
- reducir complejidad;
- facilitar el mantenimiento;
- adaptarse a la evolución del proyecto.

Toda reorganización significativa deberá documentarse mediante la correspondiente ADR.

---

# Relaciones entre documentos

| Documento | Responsabilidad |
|-----------|-----------------|
| CONTEXT | Índice maestro |
| PROJECT_STRUCTURE | Organización física del repositorio |
| ARQUITECTURA | Diseño del SGCC |
| MODELO_DE_CONOCIMIENTO | Modelo conceptual |
| PROJECT_ONBOARDING | Incorporación de colaboradores |
| CONTRIBUTING | Normas de contribución |

---

# Documentación relacionada

## Navegación

- CONTEXT

## Arquitectura

- ARQUITECTURA
- MODELO_DE_CONOCIMIENTO

## Incorporación

- PROJECT_ONBOARDING
- CONTRIBUTING

## Decisiones

- ADR-0002 · Estructura del repositorio

---

# Conclusión

La estructura física del repositorio constituye una implementación organizada del SGCC.

Su objetivo es facilitar el mantenimiento y la navegación del proyecto, manteniendo siempre la independencia entre la organización de los archivos y el modelo conceptual del conocimiento.

Esta separación permite reorganizar el repositorio cuando sea necesario sin alterar el significado ni las relaciones del conocimiento que contiene.
