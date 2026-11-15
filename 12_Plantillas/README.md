---

id: PLA-0000
tipo: modulo
titulo: Plantillas culinarias
categoria: Plantillas
estado: estable
version: 1.0.0
ultima_revision: 2026-07-02
etiquetas:
- plantillas
- patrones
- reutilizacion

---

# Plantillas Culinarias

## Objetivo

La carpeta `12_Plantillas` contiene patrones reutilizables de elaboración.

Una plantilla no es una receta concreta, sino una estructura general que permite construir muchas recetas diferentes siguiendo una lógica común.

---

# Filosofía

Una receta responde a:

> ¿Cómo preparo este plato concreto?

Una plantilla responde a:

> ¿Qué patrón puedo seguir para crear platos similares?

Las plantillas permiten cocinar con más autonomía, adaptar ingredientes disponibles y evitar repetir explicaciones en múltiples recetas.

---

# Qué debe incluir este módulo

Deben incluirse aquí documentos como:

* salteado asiático;
* curry base;
* salsa base;
* marinada base;
* guiso base;
* crema base;
* arroz base;
* sofrito mediterráneo;
* vinagreta base.

---

# Qué NO debe incluir

No pertenecen a este módulo:

* recetas completas;
* ingredientes concretos;
* tablas de tiempos o conversiones;
* explicaciones largas de técnicas.

Si una explicación pertenece a una técnica, deberá ir en `00_Bases`.

Si pertenece a un ingrediente, deberá ir en `11_Despensa`.

---

## Patrones de salsas y aliños

Las plantillas describen **estructuras reutilizables**, no recetas probadas con una formulación exacta. Las proporciones deben ajustarse según el ingrediente principal y registrarse al probarlas.

| ID | Plantilla | Función |
|---|---|---|
| PLA-0010 | [Salsa china base](./02_Salsas/salsa_china_base.md) | Salteados y ligado |
| PLA-0012 | [Salsa teriyaki base](./02_Salsas/salsa_teriyaki_base.md) | Glaseado |
| PLA-0200 | [Vinagreta mediterránea base](./02_Salsas/vinagreta_mediterranea_base.md) | Emulsión de aceite y ácido |
| PLA-0201 | [Salsa de yogur, limón y hierbas base](./02_Salsas/salsa_yogur_limon_y_hierbas_base.md) | Acompañamiento frío |
| PLA-0202 | [Salsa de tomate reducida base](./02_Salsas/salsa_tomate_reducida_base.md) | Reducción y textura |
| PLA-0203 | [Salsa de coco y curry base](./02_Salsas/salsa_coco_y_curry_base.md) | Base especiada |
| PLA-0204 | [Salsa de mostaza para carnes base](./02_Salsas/salsa_mostaza_para_carnes_base.md) | Desglasado y ligado |
| PLA-0205 | [Salsa de soja y vinagre negro agridulce base](./02_Salsas/salsa_soja_vinagre_negro_agridulce_base.md) | Glaseado agridulce |

Las aplicaciones enlazadas en cada plantilla no cambian las formulaciones ni las valoraciones de las recetas existentes.

## Patrones de marinadas y adobos

Las marinadas son **patrones de sazón y tratamiento superficial**, no métodos de cocción ni de conservación. Todas las mezclas que toquen alimentos crudos deben mantenerse refrigeradas; si se desea salsa de servicio, reservarla limpia antes del contacto.

| ID | Plantilla | Uso principal |
|---|---|---|
| PLA-0011 | [Marinada asiática general](./03_Marinadas/marinada_asiatica.md) | Base flexible para proteínas |
| PLA-0206 | [Marinada mediterránea de limón y hierbas](./03_Marinadas/marinada_mediterranea_de_limon_y_hierbas.md) | Ave, cerdo y verduras |
| PLA-0207 | [Adobo de yogur y especias para aves](./03_Marinadas/adobo_de_yogur_y_especias_para_aves.md) | Pollo y pavo al horno |
| PLA-0208 | [Adobo seco de comino, pimentón y ajo](./03_Marinadas/adobo_seco_de_comino_pimenton_y_ajo.md) | Plancha y horno |
| PLA-0209 | [Marinada breve de lima y cilantro para marisco](./03_Marinadas/marinada_breve_de_lima_y_cilantro_para_marisco.md) | Pescados y mariscos cocinados |
| PLA-0210 | [Marinada de soja, jengibre y mirin](./03_Marinadas/marinada_de_soja_jengibre_y_mirin.md) | Salteados y tofu |
| PLA-0211 | [Adobo de naranja, mostaza y tomillo](./03_Marinadas/adobo_de_naranja_mostaza_y_tomillo.md) | Ave, cerdo y hortalizas firmes |

Las nuevas fórmulas son **referencias pendientes de prueba doméstica** y no modifican las cantidades ni las valoraciones de recetas ya registradas.

## Patrones de cocción para arroces y horno

Estas plantillas ofrecen **puntos de partida adaptables**; el tipo de arroz, el grosor del alimento, el recipiente y el calor modifican la proporción de líquido y los tiempos. No sustituyen recetas existentes.

| ID | Plantilla | Aplicación principal |
|---|---|---|
| PLA-0212 | [Arroz seco en cazuela](./05_Arroces/arroz_seco_en_cazuela_base.md) | Absorción y evaporación |
| PLA-0213 | [Arroz meloso o caldoso](./05_Arroces/arroz_meloso_o_caldoso_base.md) | Texturas de cuchara |
| PLA-0214 | [Pescado al horno](./04_Cocciones/pescado_al_horno_base.md) | Horneado según grosor |
| PLA-0215 | [Verduras al horno por tandas](./04_Cocciones/verduras_al_horno_por_tandas_base.md) | Cocciones escalonadas |
| PLA-0216 | [Rebozado y fritura por tandas](./04_Cocciones/rebozado_y_fritura_por_tandas_base.md) | Cortezas y control del aceite |
| PLA-0217 | [Verduras rellenas al horno](./04_Cocciones/verduras_rellenas_al_horno_base.md) | Precocción, relleno y gratinado |

Las seis plantillas son patrones propuestos para adaptar y contrastar en preparaciones reales. Las fórmulas y las valoraciones históricas permanecen intactas.

# Relación con otros módulos

## 00_Bases

Aporta las técnicas.

Ejemplo:

* saltear;
* sofreír;
* cocinar al wok.

## 11_Despensa

Aporta los ingredientes.

Ejemplo:

* salsa de soja;
* mirin;
* salsa de ostras;
* aceite de sésamo.

## 98_Tablas

Aporta datos de consulta rápida.

Ejemplo:

* tiempos de cocción;
* conservación;
* conversiones.

## Recetas

Aplican una plantilla a un plato concreto.

---

# Estructura recomendada de una plantilla

Cada plantilla deberá incluir:

* descripción;
* objetivo;
* patrón general;
* ingredientes base;
* orden de incorporación;
* proporciones orientativas;
* variantes;
* errores frecuentes;
* recetas derivadas;
* referencias.

---

# Principio de NovaCoquinaria

> Una buena plantilla no sustituye a una receta; permite crear muchas recetas mejores.

---

# Utilizado por

Este módulo será utilizado por recetas, menús y futuras herramientas de planificación culinaria.

---

## Información del módulo

| Campo | Valor |
|--------|-------|
| Dominio | Patrones reutilizabls |
| Estado | En desarrollo |
| Tipo de contenido | Elaboraciones base |
| Dependencias | Ninguna |
| Utilizado por | Recetas |
