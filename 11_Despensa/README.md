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
* Ingredientes de repostería
* Frutos de cáscara

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
| ING-0042 | [Patata](./06_Verduras/patata.md) | Almidón, asados y guisos |
| ING-0043 | [Tomate fresco](./06_Verduras/tomate_fresco.md) | Acidez, agua, salsas y rellenos |
| ING-0044 | [Espinacas](./06_Verduras/espinacas.md) | Hojas, guisos y rellenos |
| ING-0045 | [Calabaza](./06_Verduras/calabaza.md) | Dulzor, cremas y arroces |
| ING-0046 | [Limón](./11_Condimentos/limon.md) | Zumo ácido y ralladura aromática |
| ING-0047 | [Mantequilla](./14_Huevos_Lacteos/mantequilla.md) | Grasas, masas y salsas |

Las fichas distinguen selección, comportamiento al cocinar, usos, conservación, sustituciones y relaciones con recetas.

---

## Ingredientes para arroces, cocina asiática y lácteos

| ID | Ingrediente | Función culinaria |
|---|---|---|
| ING-0048 | [Arroz Albufera](./01_Cereales/arroz_albufera.md) | Arroces melosos, caldosos y secos |
| ING-0049 | [Aceite de cacahuete](./10_Aceites/aceite_de_cacahuete.md) | Salteado y fritura controlada |
| ING-0050 | [Lemongrass](./08_Especias/lemongrass.md) | Aromatización de sopas y currys |
| ING-0051 | [Glutamato monosódico](./11_Condimentos/glutamato_monosodico.md) | Ajuste de umami |
| ING-0052 | [Yogur natural](./14_Huevos_Lacteos/yogur_natural.md) | Acidez y cremosidad en bebidas y salsas |
| ING-0053 | [Nata para cocinar](./13_Bases_Culinarias/nata_para_cocinar.md) | Cuerpo de salsas y rellenos |

---

## Ingredientes de repostería y bebidas

| ID | Ingrediente | Función culinaria |
|---|---|---|
| ING-0054 | [Harina de trigo](./01_Cereales/harina_de_trigo.md) | Estructura de masas y espesado |
| ING-0055 | [Leche entera](./14_Huevos_Lacteos/leche_entera.md) | Hidratación, cremas y bebidas |
| ING-0056 | [Canela](./08_Especias/canela.md) | Aromatización e infusión |
| ING-0057 | [Cacao puro en polvo](./15_Reposteria/cacao_puro_en_polvo.md) | Aroma, color y absorción de líquido |
| ING-0058 | [Azúcar blanco](./15_Reposteria/azucar_blanco.md) | Dulzor, estructura y caramelización |
| ING-0059 | [Nueces](./16_Frutos_Secos/nueces.md) | Textura y aromas tostados |

La organización de Despensa comprende también los **ingredientes de repostería** y los **frutos de cáscara** como familias de referencia.

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
