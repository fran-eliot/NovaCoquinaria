# ADR-0015 · Arquitectura basada en reutilización del conocimiento

- **Estado:** Aceptada
- **Fecha:** 2026-07-17
- **Versión:** 1.0.0

---

# Contexto

Durante el desarrollo inicial de NovaCoquinaria las recetas eran documentos relativamente autocontenidos.

Cada receta describía nuevamente:

- ingredientes;
- mise en place;
- técnicas;
- cocción;
- conservación;
- consejos;
- errores frecuentes.

Este enfoque facilita la lectura aislada de una receta, pero produce un importante problema de mantenimiento:

- duplicación de conocimiento;
- inconsistencias entre documentos;
- crecimiento exponencial del repositorio;
- dificultad para mantener versiones.

Al mismo tiempo, el proyecto ha evolucionado incorporando documentos especializados sobre:

- ingredientes;
- técnicas;
- plantillas culinarias;
- tablas;
- fundamentos.

Estos documentos contienen el conocimiento reutilizable que anteriormente aparecía repetido en numerosas recetas.

---

# Decisión

NovaCoquinaria adopta una arquitectura basada en reutilización del conocimiento.

A partir de esta ADR:

- los documentos especializados son la fuente única de conocimiento;
- las recetas implementan patrones culinarios;
- las recetas documentan únicamente aquello que las diferencia del patrón reutilizado.

---

# Principios

## 1. Fuente única de conocimiento

Cada concepto debe tener un único documento responsable.

Ejemplos:

- el arroz jazmín se documenta en su ingrediente;
- el salteado se documenta en la técnica correspondiente;
- el arroz frito se documenta en su plantilla;
- la conservación se documenta en las tablas.

Las recetas enlazan estos documentos.

Nunca deben duplicarlos.

---

## 2. Especialización

Una receta describe únicamente:

- ingredientes específicos;
- diferencias respecto al patrón;
- tiempos particulares;
- variantes;
- observaciones propias.

Todo lo demás debe reutilizarse.

---

## 3. Composición

Una receta se entiende como la composición de:

- ingredientes;
- técnicas;
- plantillas;
- tablas;
- principios culinarios.

La documentación nace de la combinación de estos elementos.

---

## 4. Evolución independiente

Cada componente puede evolucionar sin modificar las recetas.

Ejemplo:

Mejorar el documento "Saltear" beneficia automáticamente a todas las recetas que lo utilizan.

---

## 5. No duplicación

Siempre que exista un documento específico:

- se enlaza;
- no se copia.

---

# Beneficios

Esta arquitectura permite:

- reducir duplicación;
- facilitar el mantenimiento;
- mejorar la coherencia;
- acelerar la creación de nuevas recetas;
- aumentar la reutilización del conocimiento;
- favorecer la escalabilidad del SGCC.

---

# Analogía

La arquitectura puede entenderse de forma similar al desarrollo software.

| NovaCoquinaria | Ingeniería del software |
|----------------|-------------------------|
| Ingredientes | Entidades |
| Técnicas | Servicios |
| Plantillas | Clases abstractas |
| Tablas | Utilidades |
| Recetas | Implementaciones |
| Dominios | Módulos |

---

# Consecuencias

Las nuevas recetas tenderán a ser significativamente más pequeñas.

Su función principal será:

- indicar qué patrón implementan;
- describir las diferencias;
- enlazar el conocimiento reutilizable.

El conocimiento común dejará de copiarse entre documentos.

---

# Excepciones

Una receta podrá repetir información cuando:

- mejore significativamente la comprensión;
- el acceso al documento especializado interrumpa la lectura;
- exista un motivo pedagógico claramente justificado.

Estas excepciones deberán mantenerse al mínimo.

---

# Estado futuro

Esta ADR constituye uno de los principios arquitectónicos fundamentales de NovaCoquinaria y deberá considerarse en cualquier ampliación futura del SGCC.