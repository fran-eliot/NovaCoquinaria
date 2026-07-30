# ADR-0015 — Arquitectura Basada en Componentes de Conocimiento

**Identificador:** ADR-0015

**Estado:** Aceptado

**Vigencia:** Activa

**Última revisión:** 2026-07-29

**Autor:** Fran Ramírez

**Categoría:** Arquitectura del Conocimiento

---

# Contexto

El SGCC gestiona conocimiento culinario mediante unidades documentales especializadas.

Inicialmente, las recetas tendían a incorporar toda la información necesaria para su ejecución, incluyendo ingredientes, técnicas, tiempos, conservación y recomendaciones.

Este enfoque favorecía la lectura individual de cada receta, pero generaba una importante duplicación del conocimiento y dificultaba su evolución.

La progresiva incorporación de documentos especializados ha permitido separar el conocimiento común de las aplicaciones concretas de dicho conocimiento.

---

# Problema

Cuando cada documento contiene una copia parcial del conocimiento común:

- aumenta la duplicidad;
- aparecen inconsistencias;
- el mantenimiento se vuelve costoso;
- la evolución requiere modificaciones repetitivas;
- disminuye la reutilización.

Es necesario definir un modelo arquitectónico que permita construir nuevos documentos mediante la composición de componentes de conocimiento independientes.

---

# Decisión

El SGCC adoptará una arquitectura basada en componentes de conocimiento reutilizables.

Cada componente será responsable de un único concepto del dominio y podrá combinarse con otros componentes para construir unidades de conocimiento de mayor nivel.

Las recetas, guías, menús y futuros artefactos del sistema se construirán mediante composición y no mediante duplicación.

---

# Justificación

La composición favorece la reutilización y desacopla la evolución del conocimiento.

Cada componente puede mejorar de forma independiente sin requerir modificaciones sistemáticas en los documentos que lo utilizan.

Este enfoque incrementa la coherencia del sistema y facilita su crecimiento sostenible.

---

# Principios derivados

Esta decisión establece los siguientes principios:

- Cada componente posee una única responsabilidad.
- El conocimiento común se documenta una sola vez.
- Las unidades complejas se construyen por composición.
- La reutilización prevalece sobre la copia.
- La evolución de un componente beneficia a todos sus consumidores.

---

# Modelo conceptual

```text
        Componentes de Conocimiento

      Ingredientes   Técnicas   Tablas

             │           │          │

             └──────┬────┴──────────┘
                    │

             Plantillas Culinarias

                    │

                    ▼

                 Recetas

                    │

                    ▼

      Menús · Guías · Aplicaciones
```

Las unidades de mayor nivel emergen mediante la combinación de componentes especializados.

---

# Componentes del modelo

La arquitectura podrá incorporar distintos tipos de componentes, entre ellos:

- ingredientes;
- técnicas;
- plantillas;
- tablas;
- fundamentos;
- principios;
- futuros dominios especializados.

Cada uno representa una unidad cohesionada de conocimiento con identidad propia.

---

# Alternativas consideradas

## Documentos autocontenidos

Descartada por favorecer la duplicación y dificultar la evolución.

---

## Reutilización parcial sin componentes especializados

Descartada por no proporcionar una arquitectura coherente de reutilización.

---

## Centralizar todo el conocimiento en documentos monolíticos

Descartada por reducir la modularidad y dificultar el mantenimiento.

---

# Consecuencias

## Ventajas

- Mayor reutilización.
- Menor duplicidad.
- Evolución independiente.
- Alta cohesión.
- Bajo acoplamiento.
- Escalabilidad.
- Mejor preparación para automatización e IA.

---

## Inconvenientes

- Requiere mayor disciplina documental.
- Incrementa la necesidad de referencias entre componentes.
- Puede aumentar la navegación entre documentos durante la edición.

---

# Impacto arquitectónico

Esta decisión transforma el SGCC en un sistema basado en componentes de conocimiento.

Como consecuencia:

- las recetas dejan de ser contenedores de conocimiento y pasan a ser composiciones de componentes especializados;
- la evolución del conocimiento se realiza sobre los componentes y no sobre sus múltiples reutilizaciones;
- nuevas capacidades podrán construirse reutilizando los mismos componentes sin alterar su estructura.

---

# Relación con otros ADR

Este ADR desarrolla:

- ADR-0005 — Descomposición del Conocimiento en Componentes Reutilizables.
- ADR-0006 — Modelo de Relaciones del Conocimiento.
- ADR-0010 — Arquitectura Orientada al Conocimiento.
- ADR-0014 — Modelo de Gestión del Conocimiento.

Es complementado posteriormente por:

- ADR-0018 — Modelo del Conocimiento del SGCC.
- ADR-0019 — Modelo Lógico vs Estructura Física.

---

# Documentación relacionada

La aplicación práctica de esta decisión se desarrolla en:

- ARQUITECTURA.md
- ESPECIFICACION_DE_DOCUMENTOS.md
- KNOWLEDGE_STRATEGY.md
- QUALITY.md

Las reglas específicas sobre la estructura de cada tipo de documento pertenecen al Modelo Documental y podrán evolucionar sin modificar este ADR.

---

# Estado actual

La decisión continúa plenamente vigente.

El SGCC mantiene una arquitectura basada en componentes de conocimiento especializados cuya composición permite construir recetas, guías, menús y futuras aplicaciones sin duplicar el conocimiento compartido, preservando la coherencia y facilitando su evolución a largo plazo.