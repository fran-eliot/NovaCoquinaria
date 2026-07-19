---
id: ADR-0018
titulo: Modelo de conocimiento del Sistema de Gestión del Conocimiento Culinario
estado: Aprobado
fecha: 2026-07-18
autor: NovaCoquinaria
relacionadas:
  - ADR-0015
  - ADR-0016
  - ADR-0017
---

# ADR-0018 · Modelo de conocimiento del SGCC

## Contexto

NovaCoquinaria no pretende ser únicamente un recetario digital.

Su objetivo es constituir un **Sistema de Gestión del Conocimiento Culinario (SGCC)** donde cada documento represente una entidad de conocimiento claramente definida y relacionada con las demás.

Durante el desarrollo del dominio *Arroces* se comprobó que no todos los documentos representan el mismo tipo de conocimiento.

Era necesario definir un modelo conceptual explícito.

---

# Decisión

El SGCC organiza el conocimiento en **seis tipos principales de entidades**.

Cada entidad posee un propósito, un nivel de abstracción y unas relaciones determinadas.

---

# Modelo conceptual

```text
                 CONOCIMIENTO CULINARIO

                       Ingredientes
                             │
                             ▼
                        Técnicas
                             │
                             ▼
                   Patrones culinarios
                             │
                             ▼
                     Platos canónicos
                             │
                             ▼
                  Variantes / Recetas
```

Las **Tablas** constituyen conocimiento transversal y pueden relacionarse con cualquiera de los niveles anteriores.

---

# 1. Ingredientes

## Propósito

Representar materias primas y productos culinarios.

Responden a la pregunta:

> ¿Con qué cocino?

## Ejemplos

- Pollo
- Arroz jazmín
- Gambas
- Leche de coco
- Salsa de soja

---

# 2. Técnicas

## Propósito

Describir acciones culinarias.

Responden a la pregunta:

> ¿Cómo cocino?

## Ejemplos

- Saltear
- Sofreír
- Hornear
- Freír
- Cocinar al wok

Las técnicas nunca describen un plato completo.

---

# 3. Patrones culinarios

## Propósito

Definir estructuras reutilizables de elaboración.

Responden a la pregunta:

> ¿Qué patrón sigue esta preparación?

No representan platos concretos.

Representan procesos comunes reutilizables.

## Ejemplos

- Salteado asiático
- Marinada asiática
- Curry base
- Sofrito mediterráneo
- Salsa china base

---

# 4. Platos canónicos

## Propósito

Representar la receta de referencia de una familia culinaria.

Responden a la pregunta:

> ¿Cuál es el plato de referencia?

Un plato canónico:

- posee identidad gastronómica;
- tiene ingredientes propios;
- define un flujo completo;
- sirve de base para variantes.

## Ejemplos

- Arroz frito
- Tortilla francesa
- Risotto blanco
- Curry amarillo básico

---

# 5. Variantes

## Propósito

Especializar un plato canónico.

Una variante:

- modifica ingredientes;
- adapta técnicas;
- incorpora productos locales;
- representa una tradición regional.

## Ejemplos

- Arroz frito con pollo
- Arroz frito con gambas
- Arroz chaufa
- Yakimeshi
- Nasi goreng

---

# 6. Tablas

## Propósito

Documentar conocimiento transversal.

No representan ingredientes ni recetas.

Sirven de apoyo al resto del sistema.

## Ejemplos

- Tiempos de cocción
- Conservación
- Sustituciones
- Escalas de picante
- Equivalencias
- Familias culinarias

---

# Relaciones permitidas

Las entidades pueden establecer relaciones semánticas.

Las principales son:

| Relación | Significado |
|----------|-------------|
| utiliza | Emplea otra entidad |
| implementa | Especializa un plato canónico |
| deriva de | Evoluciona desde otro conocimiento |
| requiere | Necesita una técnica o ingrediente |
| sustituye | Puede reemplazar otra entidad |
| acompaña | Maridaje o acompañamiento |
| pertenece a | Clasificación |
| referencia | Enlace documental |

No todas las combinaciones son válidas.

Por ejemplo:

- una receta utiliza ingredientes;
- una técnica no implementa otra técnica;
- un ingrediente no implementa recetas.

---

# Grafo de conocimiento

El SGCC debe entenderse como un grafo.

Ejemplo:

```text
Arroz chaufa
        │
implementa
        ▼
Arroz frito
        │
utiliza
        ▼
Salteado asiático
        │
requiere
        ▼
Saltear
        │
emplea
        ▼
Wok
```

El valor del sistema reside en estas relaciones y no únicamente en los documentos individuales.

---

# Consecuencias

El crecimiento del SGCC deberá realizarse incorporando nuevas entidades al modelo existente.

No se crearán documentos cuya naturaleza no esté claramente definida.

Antes de añadir una nueva categoría documental deberá evaluarse si representa un nuevo tipo de conocimiento o si pertenece a alguno ya existente.

---

# Beneficios

- Modelo conceptual explícito.
- Arquitectura escalable.
- Navegación semántica.
- Reutilización del conocimiento.
- Facilita búsquedas y generación automática de grafos.
- Reduce duplicidades.
- Favorece futuras integraciones con IA, RAG y motores de consulta.

---

# Estado

Esta ADR constituye la referencia arquitectónica para la organización del conocimiento del SGCC.

Las futuras decisiones deberán ser coherentes con este modelo.