---
id: ARC-0017
tipo: arquitectura
titulo: Framework de Herramientas
version: 2.0
estado: estable
ultima_revision: 2026-07-20
---

# Framework de Herramientas

> **Proyecto:** NovaCoquinaria
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento describe la arquitectura del Framework de Herramientas utilizado por NovaCoquinaria.

El Framework proporciona la infraestructura software necesaria para automatizar la validación, generación y mantenimiento del conocimiento almacenado en el SGCC.

No contiene conocimiento culinario.

Su responsabilidad consiste exclusivamente en proporcionar servicios de infraestructura.

---

# Papel del Framework

Dentro del SGCC, el Framework constituye la capa técnica que implementa la estrategia de automatización.

Su misión consiste en proporcionar componentes reutilizables para:

- validar;
- analizar;
- generar;
- construir;
- publicar.

---

# Arquitectura

```text
                    Framework

        ┌─────────────────────────────┐
        │      Servicios comunes       │
        └──────────────┬──────────────┘
                       │
      ┌────────────────┼────────────────┐
      │                │                │
 Validadores      Generadores      Builders
      │                │                │
      └────────────────┼────────────────┘
                       │
                  Herramientas
```

Cada componente posee una responsabilidad única.

---

# Principios

El Framework sigue los mismos principios arquitectónicos del SGCC.

## Responsabilidad única

Cada módulo implementa una única capacidad claramente definida.

---

## Reutilización

La funcionalidad común se centraliza para evitar duplicidades.

---

## Modularidad

Los componentes evolucionan de forma independiente.

---

## Simplicidad

Las herramientas deberán ser fáciles de comprender, mantener y ampliar.

---

## Transparencia

Las herramientas deberán producir resultados reproducibles y mensajes claros.

---

# Componentes

## Servicios comunes

Proporcionan funcionalidades compartidas por el resto del Framework.

Ejemplos:

- lectura de documentos;
- acceso al Front Matter;
- utilidades comunes;
- mensajes homogéneos.

---

## Modelo documental

Representa los documentos del SGCC mediante objetos reutilizables.

Permite desacoplar las herramientas del formato físico de los archivos.

---

## Validadores

Comprueban la consistencia del conocimiento.

Características:

- nunca modifican documentos;
- detectan inconsistencias;
- producen diagnósticos.

---

## Generadores

Crean artefactos derivados a partir del conocimiento validado.

Ejemplos:

- estadísticas;
- índices;
- documentación publicada.

---

## Builders

Orquestan procesos completos de construcción.

Su misión consiste en coordinar varios componentes del Framework.

---

# Dependencias

La relación entre componentes sigue una dirección única.

```text
Servicios comunes

↓

Modelo documental

↓

Validadores / Generadores

↓

Builders
```

Los módulos de nivel superior reutilizan los inferiores.

Nunca ocurre en sentido inverso.

---

# Evolución prevista

El Framework podrá incorporar nuevas capacidades sin modificar su arquitectura básica.

Ejemplos:

- validación semántica;
- análisis del Knowledge Graph;
- generación automática de índices;
- exportadores;
- integración continua;
- herramientas de mantenimiento.

---

# Relación con la automatización

El Framework constituye la implementación técnica de la estrategia de automatización.

La estrategia define los principios.

El Pipeline define el proceso.

El Framework implementa las capacidades necesarias para ejecutarlo.

---

# Relaciones documentales

| Documento | Responsabilidad |
|-----------|-----------------|
| AUTOMATION | Estrategia |
| QUALITY_PIPELINE | Proceso |
| QUALITY | Modelo de calidad |
| ARQUITECTURA | Arquitectura del SGCC |

---

# Documentación relacionada

## Arquitectura

- AUTOMATION
- QUALITY_PIPELINE
- QUALITY
- ARQUITECTURA

---

# Conclusión

El Framework de Herramientas constituye la infraestructura software del SGCC.

Su arquitectura modular permite evolucionar las capacidades de automatización sin comprometer la estabilidad del conocimiento ni de la arquitectura documental.

Cada componente existe para dar soporte al conocimiento, nunca para sustituirlo.