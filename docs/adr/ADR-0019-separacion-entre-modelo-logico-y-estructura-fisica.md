---
id: ADR-0019
titulo: Separación entre el modelo lógico del conocimiento y la estructura física del repositorio
estado: Aprobado
fecha: 2026-07-18
autor: NovaCoquinaria
relacionadas:
  - ADR-0018
---

# Contexto

NovaCoquinaria almacena su conocimiento en documentos Markdown organizados mediante carpetas.

Sin embargo, la organización física de los archivos no debe confundirse con el modelo conceptual del SGCC.

Un mismo documento puede pertenecer simultáneamente a varios dominios culinarios, reutilizar diferentes técnicas y participar en múltiples relaciones semánticas.

---

# Problema

Las carpetas representan una decisión práctica para organizar el repositorio.

No representan necesariamente la estructura del conocimiento.

Por ejemplo:

```
11_Despensa/
    pollo.md
```

No significa que "Pollo" pertenezca únicamente a "Despensa".

El ingrediente participa también en:

- Currys
- Arroces
- Wok
- Sopas
- Pasta
- Cocina mediterránea
- Cocina china
- Cocina india
...

---

# Decisión

Se distinguen dos niveles independientes.

## Modelo lógico

Representa:

- entidades
- relaciones
- reutilización

Es la verdadera arquitectura del SGCC.

---

## Estructura física

Representa:

- carpetas
- nombres de archivos
- navegación
- facilidad de mantenimiento

Puede modificarse sin alterar el modelo lógico.

---

# Principio

La ubicación de un documento nunca define su significado.

Su significado viene determinado por:

- el tipo de entidad;
- sus relaciones;
- sus metadatos;
- su contenido.

---

# Ejemplo

```
pollo.md
```

Físicamente:

```
11_Despensa/
```

Lógicamente:

```
Ingrediente

↓

utilizado por

↓

Arroz frito

↓

Curry amarillo

↓

Pad Thai

↓

Yakisoba

↓

Sopa de pollo
```

---

# Consecuencias

La reorganización futura del repositorio no requerirá modificar el modelo conceptual.

Los enlaces semánticos tendrán prioridad sobre la estructura de carpetas.

La navegación automática podrá generarse a partir del grafo de conocimiento y no exclusivamente de la jerarquía de directorios.

---

# Beneficios

- Mayor independencia entre contenido y almacenamiento.
- Facilita reorganizaciones.
- Reduce dependencias estructurales.
- Acerca NovaCoquinaria a un sistema de conocimiento basado en grafos.