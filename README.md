# 🍳 GASTRO - Manual Personal de Cocina

> *"No es un recetario. Es una base de conocimiento culinario construida como si fuera un proyecto de software."*

---

# GASTRO

GASTRO es un repositorio personal de cocina cuyo objetivo es documentar, organizar y mejorar el conocimiento culinario de forma estructurada, modular y reutilizable.

A diferencia de un recetario tradicional, este proyecto no pretende únicamente almacenar recetas, sino construir un **manual técnico de cocina** que evolucione continuamente.

Cada receta, técnica, ingrediente o tabla de referencia se documenta siguiendo criterios similares a los utilizados en proyectos de ingeniería de software:

* Modularidad
* Reutilización
* Mantenibilidad
* Consistencia
* Documentación
* Evolución continua

---

# Objetivos

El proyecto persigue varios objetivos:

* Centralizar todas las recetas personales.
* Documentar técnicas culinarias.
* Evitar duplicar conocimiento.
* Comprender el fundamento de cada elaboración.
* Facilitar la experimentación y mejora de recetas.
* Mantener una estructura escalable durante años.

---

# Filosofía

Las recetas son únicamente una parte del conocimiento.

Cuando una explicación pueda reutilizarse en varias recetas, se documentará una única vez en un documento base y el resto de recetas harán referencia a él.

Ejemplo:

❌ Explicar cómo hacer un sofrito en 25 recetas.

✅ Crear un único documento:

```text
00_Bases/tecnicas_sofrito.md
```

y enlazarlo desde todas las recetas que lo utilicen.

---

# Organización del repositorio

```text
00_Bases/
        Conocimientos generales de cocina

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
        Ingredientes y productos

12_Plantillas/
        Patrones reutilizables de elaboración

98_Tablas/
        Tablas de consulta rápida

99_Notas/
        Ideas, experimentos y pendientes
```

---

# Principios de documentación

Todo documento debe cumplir, en la medida de lo posible, los siguientes principios:

## 1. Un único lugar para cada conocimiento

Cada concepto debe documentarse una sola vez.

Las recetas harán referencia a los documentos base cuando sea necesario.

---

## 2. Reutilización

Evitar copiar y pegar información.

Siempre que una técnica aparezca en varias recetas, deberá documentarse por separado.

---

## 3. Mejora continua

Todos los documentos pueden evolucionar.

Las recetas nunca se consideran "terminadas".

Siempre pueden mejorarse.

---

## 4. Explicar el porqué

No limitarse a indicar pasos.

Siempre que aporte valor se documentará:

* por qué se hace
* qué ocurre durante la elaboración
* qué errores son habituales
* cómo mejorar el resultado

---

# Estructura de una receta

Las recetas seguirán una estructura homogénea.

```text
Descripción

Ingredientes

Preparación

Variantes

Trucos

Errores frecuentes

Conservación

Congelación

Recalentado

Acompañamientos

Referencias
```

No todos los apartados serán obligatorios, pero se mantendrá la máxima consistencia posible.

---

# Documentos base

Los documentos contenidos en **00_Bases** recogen conocimientos reutilizables.

Ejemplos:

* técnicas culinarias
* proporciones
* tiempos de cocción
* seguridad alimentaria
* conservación
* congelación
* salsas base
* marinadas
* espesantes
* organización de la cocina

Estos documentos sirven de apoyo a todas las recetas.

---

# Despensa

La carpeta **11_Despensa** documenta ingredientes.

Cada ingrediente incluye, cuando proceda:

* descripción
* origen
* variedades
* sabor
* usos culinarios
* sustituciones
* conservación
* combinaciones recomendadas
* recetas relacionadas

---

# Plantillas

Las plantillas describen estructuras reutilizables de elaboración.

No son recetas.

Ejemplos:

* arroz base
* curry base
* salteado asiático
* salsa base
* crema base
* guiso base

Una receta concreta se construye a partir de una o varias plantillas.

---

# Tablas

Las tablas permiten localizar información rápidamente.

Ejemplos:

* tiempos de cocción
* temperaturas de horno
* equivalencias
* conversiones
* conservación
* sustituciones

---

# Convenciones

## Nombres de archivos

* minúsculas
* palabras separadas mediante "_"
* nombres descriptivos

Ejemplos:

```text
arroz_chaufa.md

caballa_japonesa.md

salsa_teriyaki.md
```

---

## Formato

Todos los documentos utilizarán Markdown.

Las listas, tablas y encabezados seguirán una estructura uniforme.

---

# Evolución del proyecto

Este repositorio está vivo.

Cada nueva receta, técnica o ingrediente puede provocar:

* la creación de un nuevo documento
* la mejora de uno existente
* una reorganización de la estructura

El objetivo no es acumular recetas, sino construir un sistema de conocimiento culinario cada vez más completo, coherente y reutilizable.

---

# Hoja de ruta

Prioridad de desarrollo:

1. README
2. Documentos base
3. Tablas
4. Despensa
5. Plantillas
6. Recetas
7. Revisión y mejora continua

---

# Licencia

Repositorio personal de uso privado.

Su contenido podrá modificarse, reorganizarse y ampliarse continuamente conforme evolucione la experiencia culinaria del autor.
