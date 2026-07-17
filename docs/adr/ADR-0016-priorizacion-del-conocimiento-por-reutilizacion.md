# ADR-0016 · Priorización del crecimiento del conocimiento por reutilización

- **Estado:** Aceptada
- **Fecha:** 2026-07-17
- **Versión:** 1.0.0

---

# Contexto

NovaCoquinaria es un Sistema de Gestión del Conocimiento Culinario (SGCC) concebido para evolucionar durante años.

El número potencial de ingredientes, técnicas, plantillas, recetas y relaciones es muy elevado, por lo que resulta inviable documentar todo el conocimiento siguiendo únicamente criterios temáticos o el orden cronológico de incorporación.

Durante las primeras iteraciones del proyecto se observó que algunos documentos aportaban mucho más valor que otros, al ser reutilizados por numerosas recetas y patrones culinarios.

Esta experiencia llevó a adoptar una estrategia de crecimiento basada en el impacto y la reutilización del conocimiento.

---

# Decisión

El crecimiento del SGCC se priorizará según el valor estructural que cada nuevo documento aporte al conjunto del sistema.

Se documentarán primero aquellos conceptos que permitan reutilizar conocimiento en un mayor número de documentos futuros.

La prioridad no será completar categorías, sino fortalecer progresivamente la base de conocimiento.

---

# Principios

## 1. Reutilización antes que completitud

No se persigue completar una categoría antes de iniciar otra.

Se priorizan los documentos con mayor capacidad de reutilización transversal.

Ejemplo:

Documentar **Huevo** aporta valor inmediato a arroces, pastas, tortillas, salsas, masas, repostería y otras muchas preparaciones.

---

## 2. Construcción por capas

El conocimiento se desarrolla siguiendo una secuencia lógica:

1. Fundamentos.
2. Técnicas.
3. Ingredientes.
4. Plantillas.
5. Recetas.
6. Variantes.

Cada capa reutiliza la anterior.

---

## 3. Ingredientes estratégicos

Los ingredientes con mayor conectividad dentro del grafo de conocimiento tendrán prioridad.

Ejemplos:

- cebolla;
- ajo;
- huevo;
- arroz;
- pollo;
- aceite de oliva;
- tomate.

Estos documentos actúan como nodos centrales del sistema.

---

## 4. Plantillas antes que recetas

Siempre que exista un patrón reutilizable, éste deberá documentarse antes de crear múltiples recetas derivadas.

Ejemplo:

Antes de documentar varios arroces fritos se crea:

- Arroz frito base.

---

## 5. Técnicas antes que implementaciones

Las técnicas generales se documentan una única vez.

Las recetas simplemente las reutilizan mediante referencias.

---

## 6. Crecimiento incremental

Cada documento nuevo debe integrarse en el conocimiento existente.

Siempre que sea posible deberá:

- reutilizar documentos previos;
- crear nuevas relaciones;
- enriquecer el grafo de conocimiento.

---

## 7. Máximo impacto

Cuando existan varias opciones equivalentes, se priorizará aquella que incremente en mayor medida el valor global del SGCC.

No importa únicamente el número de documentos creados.

Importa la cantidad de conocimiento reutilizable incorporado.

---

# Beneficios

Esta estrategia permite:

- reducir duplicidades;
- acelerar el crecimiento del proyecto;
- mejorar la coherencia documental;
- facilitar el mantenimiento;
- reforzar el grafo de conocimiento;
- maximizar la reutilización.

---

# Ejemplo práctico

En el dominio Arroces, el desarrollo siguió el siguiente orden:

```text
Arroz jazmín
        ↓
Arroz frito base
        ↓
Huevo
        ↓
Gambas
        ↓
Arroz frito con huevo
        ↓
Arroz frito con gambas
        ↓
Arroz frito con pollo
```

Este orden permite que cada nuevo documento aproveche el conocimiento ya consolidado y reduzca significativamente la duplicación de información.

---

# Consecuencias

El roadmap del proyecto podrá alterar el orden tradicional de creación de recetas.

La prioridad vendrá determinada por el impacto arquitectónico y no únicamente por criterios culinarios o temáticos.

El crecimiento del SGCC será guiado por el valor añadido que cada documento aporte al conjunto.

---

# Relación con otras ADR

Esta decisión complementa:

- ADR-0015 · Arquitectura basada en reutilización del conocimiento.

Mientras ADR-0015 define **cómo se organiza** el conocimiento, ADR-0016 define **cómo debe crecer**.

Ambas constituyen los pilares metodológicos del desarrollo de NovaCoquinaria.

---

# Estado futuro

Esta ADR deberá revisarse periódicamente para incorporar nuevos criterios de priorización conforme aumente el tamaño del SGCC.

Su objetivo es garantizar que el proyecto continúe creciendo de forma coherente, sostenible y orientada a la reutilización del conocimiento.