---

id: ING-0000
tipo: modulo
titulo: Despensa
categoria: Ingredientes
estado: estable
version: 1.0.0
ultima_revision: 2026-07-01
etiquetas:
- despensa
- ingredientes

---

# Despensa

## Objetivo

La carpeta `11_Despensa` constituye el catálogo de ingredientes de NovaCoquinaria.

Su finalidad es documentar las características, usos culinarios y buenas prácticas de cada ingrediente para evitar repetir esta información en las recetas.

Cada documento describe un ingrediente o una familia de ingredientes desde un punto de vista práctico, orientado a cocinar mejor.

---

# Filosofía

Una receta indica **qué ingrediente utilizar**.

La despensa explica:

* qué es;
* cómo sabe;
* cuándo utilizarlo;
* con qué combina;
* cómo conservarlo;
* qué errores evitar;
* qué sustituciones son posibles.

El conocimiento sobre un ingrediente debe documentarse una única vez y reutilizarse mediante referencias.

---

# Organización

La despensa se organiza por grandes familias de ingredientes:

* Cereales (incluidos derivados culinarios básicos, como pasta seca y sémola)
* Legumbres
* Carnes
* Pescados
* Mariscos
* Verduras
* Setas
* Especias
* Salsas
* Aceites
* Condimentos
* Conservas
* Bases Culinarias

La categoría **Cereales** comprende también sus derivados culinarios básicos cuando se utilizan como ingredientes de despensa, por ejemplo pasta seca y sémola. No implica que estos productos sean granos sin procesar.

Esta clasificación podrá ampliarse conforme evolucione el proyecto.

---

### Bases culinarias

Ingredientes que constituyen la base líquida o estructural de numerosas elaboraciones y que suelen reutilizarse en múltiples dominios culinarios.

Ejemplos:

- leche de coco;
- caldos;
- fumets;
- dashi;
- nata para cocinar.

---

# Estructura de los documentos

Cada ingrediente incluirá, cuando proceda:

* Descripción.
* Perfil culinario.
* Usos principales.
* Cómo utilizarlo.
* Conservación.
* Sustituciones.
* Errores frecuentes.
* Consejos de NovaCoquinaria.
* Ingredientes compatibles.
* Recetas relacionadas.
* Referencias a otros módulos.

---

# Criterios de calidad

Cada documento deberá:

* ser reutilizable por múltiples recetas;
* evitar duplicidades;
* explicar el porqué de las recomendaciones;
* basarse en la práctica culinaria;
* mantenerse actualizado.

---

# Relación con otros módulos

* **00_Bases** explica las técnicas para utilizar los ingredientes.
* **98_Tablas** proporciona datos de consulta rápida.
* **12_Plantillas** combina ingredientes en patrones reutilizables.
* **Recetas** aplican el conocimiento en platos concretos.

---

## Ingredientes cotidianos de referencia

| ID | Ingrediente | Función culinaria |
|---|---|---|
| ING-0041 | [Patata](./06_Verduras/patata.md) | Almidón, asados y guisos |
| ING-0042 | [Tomate fresco](./06_Verduras/tomate_fresco.md) | Acidez, agua, salsas y rellenos |
| ING-0043 | [Espinacas](./06_Verduras/espinacas.md) | Hojas, guisos y rellenos |
| ING-0044 | [Calabaza](./06_Verduras/calabaza.md) | Dulzor, cremas y arroces |
| ING-0045 | [Limón](./11_Condimentos/limon.md) | Zumo ácido y ralladura aromática |
| ING-0046 | [Mantequilla](./14_Huevos_Lacteos/mantequilla.md) | Grasas, masas y salsas |

Las fichas distinguen selección, comportamiento al cocinar, usos, conservación, sustituciones y relaciones con recetas.

---

# Evolución

La despensa crecerá de forma incremental.

Como ejemplo de integración entre dominios, la ficha de [salsa hoisin](./09_Salsas/hoisin.md) documenta el ingrediente reutilizado por recetas y comparativas de Cocina Asiática.

Solo se crearán nuevos documentos cuando un ingrediente aparezca con frecuencia o requiera una explicación específica.

---

# Utilizado por

Todos los módulos del proyecto, especialmente recetas y plantillas.

---

## Información del módulo

| Campo | Valor |
|--------|-------|
| Dominio | Ingredientes |
| Estado | En desarrollo |
| Tipo de contenido | Productos y materias primas |
| Dependencias | Ninguna |
| Utilizado por | Plantillas y recetas |
