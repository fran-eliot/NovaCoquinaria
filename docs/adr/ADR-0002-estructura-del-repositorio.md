# ADR-0002 - Estructura del Repositorio

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Francisco Ramírez Martín

---

# Contexto

La mayoría de los recetarios organizan la información como una colección de recetas independientes.

Este enfoque presenta varias limitaciones:

* duplicación constante de técnicas;
* repetición de información sobre ingredientes;
* dificultad para mantener el contenido actualizado;
* poca reutilización del conocimiento.

El proyecto GASTRO persigue un objetivo diferente: construir una base de conocimiento culinario modular y mantenible.

---

# Problema

Es necesario definir una estructura que permita:

* separar los distintos tipos de conocimiento;
* facilitar la reutilización;
* simplificar el mantenimiento;
* permitir el crecimiento del repositorio durante años sin perder coherencia.

---

# Decisión

El repositorio se organizará por **dominios de conocimiento**, no únicamente por recetas.

Cada carpeta tendrá una responsabilidad claramente definida.

La estructura general será:

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

Los documentos de arquitectura y gestión del proyecto permanecerán en la raíz del repositorio o en `docs/`.

---

# Justificación

Esta organización separa claramente:

* conocimiento teórico;
* ingredientes;
* técnicas;
* patrones reutilizables;
* recetas;
* documentación del proyecto.

Cada documento posee una única responsabilidad, reduciendo duplicidades y favoreciendo la evolución independiente de cada parte.

---

# Alternativas consideradas

## Recetario tradicional

Organizar únicamente por categorías de recetas.

**Descartado** por:

* repetición de técnicas;
* dificultad de mantenimiento;
* escasa reutilización.

---

## Wiki sin estructura

Crear documentos sin una organización fija.

**Descartado** por:

* crecimiento desordenado;
* dificultad para localizar información;
* escasa capacidad de automatización.

---

# Consecuencias

## Ventajas

* Arquitectura escalable.
* Separación clara de responsabilidades.
* Mejor mantenibilidad.
* Mayor reutilización.
* Preparado para automatización.
* Fácil incorporación de nuevos dominios culinarios.

## Inconvenientes

* Mayor planificación inicial.
* Necesidad de mantener referencias entre documentos.

---

# Impacto futuro

Esta estructura permitirá generar automáticamente:

* índices;
* documentación navegable;
* aplicaciones móviles;
* sitios web;
* asistentes culinarios;
* sistemas de búsqueda;
* herramientas de planificación de menús.

Sin modificar el contenido del repositorio.

---

# Referencias

* ADR-0001 - Filosofía del Proyecto.
* README.md.
* ESPECIFICACION_DE_DOCUMENTOS.md.
