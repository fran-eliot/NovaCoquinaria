# MODELO_CONOCIMIENTO.md

> Versión: 1.0.0
>
> Estado: Estable
>
> Última actualización: 2026-07-18

---

# Modelo de Conocimiento del SGCC

## Propósito

NovaCoquinaria no es un recetario digital.

Es un **Sistema de Gestión del Conocimiento Culinario (SGCC)**.

Este documento define el modelo conceptual del conocimiento que gestiona el sistema.

No describe:

- la estructura física del repositorio;
- la organización de carpetas;
- la implementación técnica.

Describe exclusivamente el dominio del conocimiento culinario.

---

# Principios

Todo elemento del sistema debe representar una única entidad de conocimiento.

Las entidades se relacionan entre sí formando un grafo semántico.

El valor del SGCC reside tanto en los documentos individuales como en las relaciones existentes entre ellos.

---

# Niveles de conocimiento

El modelo se organiza en distintos niveles de abstracción.

```text
                 Conocimiento culinario

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

El conocimiento transversal se documenta mediante Tablas.

---

# Entidades

## Ingrediente

Representa una materia prima o un producto culinario.

Responde a:

> ¿Con qué cocino?

Ejemplos:

- Pollo
- Gambas
- Arroz jazmín
- Curry amarillo
- Salsa de soja

---

## Técnica

Representa una acción culinaria.

Responde a:

> ¿Cómo cocino?

Ejemplos:

- Saltear
- Freír
- Hornear
- Cocer
- Marinar

Las técnicas nunca representan platos.

---

## Patrón culinario

Representa una estructura reutilizable.

Responde a:

> ¿Qué patrón sigue esta preparación?

Ejemplos:

- Salteado asiático
- Sofrito mediterráneo
- Curry base
- Marinada asiática

No posee identidad gastronómica propia.

---

## Plato canónico

Representa la receta de referencia de una familia culinaria.

Responde a:

> ¿Cuál es la receta de referencia?

Ejemplos:

- Arroz frito
- Tortilla francesa
- Risotto blanco
- Curry amarillo

Un plato canónico puede tener múltiples variantes.

---

## Variante

Representa una especialización de un plato canónico.

Ejemplos:

- Arroz frito con pollo
- Arroz chaufa
- Yakimeshi
- Nasi goreng

---

## Tabla

Representa conocimiento transversal.

Ejemplos:

- Tiempos de cocción
- Conservación
- Equivalencias
- Sustituciones
- Escalas de picante

---

# Relaciones

Las entidades pueden establecer relaciones semánticas.

## utiliza

Indica que una entidad emplea otra.

Ejemplo:

Receta → Ingrediente

---

## requiere

Indica dependencia.

Ejemplo:

Patrón → Técnica

---

## implementa

Indica que una receta concreta implementa un plato canónico.

---

## deriva de

Indica evolución.

---

## sustituye

Alternativa culinaria.

---

## acompaña

Maridajes y guarniciones.

---

## referencia

Enlace documental.

---

## pertenece a

Clasificación.

---

# Restricciones

No todas las relaciones son válidas.

Por ejemplo:

✔ Receta → Ingrediente

✔ Receta → Técnica

✔ Receta → Patrón

✔ Variante → Plato canónico

✔ Técnica → Ingrediente

✘ Ingrediente → implementa → Receta

✘ Técnica → implementa → Técnica

✘ Tabla → cocina → Ingrediente

---

# Grafo de conocimiento

Ejemplo:

```text
Pollo
   ▲
   │ utiliza
   │
Arroz frito con pollo
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
```

---

# Principio de reutilización

Una misma entidad puede participar en múltiples relaciones.

Por ejemplo:

Pollo

↓

Currys

↓

Arroces

↓

Pastas

↓

Sopas

↓

Wok

↓

Ensaladas

La entidad permanece única.

Las relaciones son múltiples.

---

# Modelo lógico y modelo físico

Este documento define exclusivamente el modelo lógico.

La organización de carpetas es una decisión de implementación.

La ubicación física de un documento nunca determina su significado.

---

# Evolución

El modelo podrá ampliarse mediante nuevas entidades cuando aparezcan necesidades reales.

La incorporación de un nuevo tipo de entidad requerirá una ADR específica.

---

# Referencias

- [VISION](./VISION.md)
- [ARQUITECTURA](./ARQUITECTURA.md)
- [ADR-0018 Modelo del Conocimiento del SGCC](./adr/ADR-0018-modelo-del-conocimiento-del-sgcc.md)
- [ADR-0019 Separacion entre modelo lógico y estructura física de los repositorios](./adr/ADR-0019-separacion-entre-modelo-logico-y-estructura-fisica.md)