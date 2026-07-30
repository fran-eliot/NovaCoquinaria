# ADR-0014 — Modelo de Gestión del Conocimiento del Sistema de Gestión del Conocimiento Culinario

**Identificador:** ADR-0014

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Gobernanza del Conocimiento

---

# Contexto

El SGCC no se concibe como un repositorio de documentos independientes.

Su finalidad es gestionar conocimiento culinario mediante un modelo estructurado, reutilizable y evolutivo.

Los documentos representan únicamente una forma de organizar y expresar ese conocimiento.

El verdadero activo del sistema es el conocimiento y las relaciones existentes entre sus diferentes componentes.

---

# Problema

Gestionar un sistema de conocimiento utilizando únicamente una perspectiva documental conduce a:

- duplicidad de información;
- pérdida de coherencia;
- baja reutilización;
- mantenimiento costoso;
- crecimiento desordenado.

Es necesario adoptar un modelo que sitúe el conocimiento como elemento central de la evolución del sistema.

---

# Decisión

El SGCC se gestionará como un sistema de conocimiento y no como una colección de documentos.

Toda evolución del proyecto deberá orientarse prioritariamente a:

- mejorar el conocimiento existente;
- aumentar su reutilización;
- reforzar sus relaciones;
- preservar su coherencia;
- facilitar su evolución.

Los documentos constituirán el soporte documental de dicho conocimiento, pero no su finalidad.

---

# Justificación

Situar el conocimiento en el centro de la gestión permite mantener una arquitectura estable mientras evolucionan:

- los documentos;
- las herramientas;
- las plataformas;
- las aplicaciones.

Este enfoque favorece la sostenibilidad del sistema y maximiza el valor acumulado del conocimiento.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- El conocimiento constituye el activo principal del SGCC.
- Los documentos representan conocimiento, pero no lo definen.
- La reutilización prevalece sobre la duplicación.
- Toda mejora deberá fortalecer la base de conocimiento.
- La evolución deberá preservar la coherencia global del sistema.

---

# Modelo conceptual

```text
          Experiencia

                │

                ▼

      Captura de Conocimiento

                │

                ▼

      Organización y Relaciones

                │

                ▼

          Reutilización

                │

                ▼

     Mejora del Conocimiento

                │

                ▼

        Nueva Experiencia
```

El conocimiento evoluciona mediante un ciclo continuo de aprendizaje.

---

# Capacidades de gestión

El modelo deberá favorecer:

- incorporación de nuevo conocimiento;
- revisión continua;
- consolidación;
- reutilización;
- integración entre dominios;
- evolución incremental;
- expansión hacia nuevos ámbitos.

Estas capacidades son consecuencia directa del modelo de conocimiento adoptado.

---

# Alternativas consideradas

## Gestión centrada en documentos

Descartada por limitar la reutilización y dificultar la evolución.

---

## Gestión orientada exclusivamente a recetas

Descartada por reducir el alcance del conocimiento culinario.

---

## Gestión basada únicamente en aplicaciones

Descartada por acoplar el conocimiento a una implementación tecnológica.

---

# Consecuencias

## Ventajas

- Evolución sostenible.
- Mayor coherencia.
- Reutilización sistemática.
- Escalabilidad.
- Integración sencilla con nuevas herramientas.
- Excelente preparación para automatización e IA.

---

## Inconvenientes

- Mayor disciplina documental.
- Necesidad de mantener relaciones consistentes.
- Requiere una visión global del conocimiento.

---

# Impacto arquitectónico

Esta decisión convierte la gestión del conocimiento en el principio rector de la evolución del SGCC.

Como consecuencia:

- el crecimiento del proyecto dejará de medirse por el número de documentos;
- la calidad del conocimiento prevalecerá sobre la cantidad de contenido;
- las relaciones entre conceptos adquirirán el mismo valor que los propios documentos;
- las futuras herramientas compartirán una única base de conocimiento coherente.

---

# Relación con otros ADR

Este ADR consolida las decisiones establecidas en:

- ADR-0001 — Filosofía del Proyecto.
- ADR-0005 — Descomposición del Conocimiento en Componentes Reutilizables.
- ADR-0006 — Modelo de Relaciones del Conocimiento.
- ADR-0007 — Modelo Conceptual del Dominio del SGCC.
- ADR-0010 — Arquitectura Orientada al Conocimiento.
- ADR-0011 — Modelo de Capas Conceptuales del Proyecto.

Se desarrolla posteriormente mediante:

- KNOWLEDGE_STRATEGY.md
- KNOWLEDGE_MATURITY.md
- KNOWLEDGE_DEBT.md
- QUALITY.md

---

# Documentación relacionada

La aplicación práctica de esta decisión se desarrolla en:

- GOVERNANCE_MODEL.md
- KNOWLEDGE_STRATEGY.md
- KNOWLEDGE_MATURITY.md
- KNOWLEDGE_DEBT.md
- QUALITY.md
- ARQUITECTURA.md

---

# Estado actual

La decisión continúa plenamente vigente.

El SGCC mantiene un modelo de gestión orientado al conocimiento donde la evolución del sistema se mide por la calidad, coherencia, reutilización y capacidad de crecimiento del conocimiento compartido, y no por el volumen de documentos o aplicaciones desarrolladas.