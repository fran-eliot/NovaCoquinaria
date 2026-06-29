# ADR-0006 - Referencias Cruzadas como Modelo de Navegación

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Francisco Ramírez Martín

---

# Contexto

Los documentos del proyecto GASTRO no son independientes.

Cada receta reutiliza técnicas, ingredientes, tablas y plantillas.

Si estas relaciones no se documentan explícitamente, el conocimiento queda aislado y resulta difícil navegar, mantener o reutilizar.

---

# Problema

Es necesario definir un mecanismo uniforme para relacionar documentos sin duplicar información.

Además, estas relaciones deberán ser comprensibles tanto por personas como por futuras herramientas de software.

---

# Decisión

Todos los documentos del proyecto podrán establecer referencias mediante enlaces Markdown relativos.

Las relaciones deberán clasificarse según su significado.

No se utilizarán enlaces arbitrarios.

---

# Tipos de relación

## Dependencias

Documentos necesarios para comprender el documento actual.

Ejemplos:

* técnicas;
* ingredientes;
* tablas;
* plantillas.

---

## Véase también

Documentos relacionados que amplían o complementan la información.

No son obligatorios para comprender el contenido.

---

## Utilizado por

Documentos que reutilizan el conocimiento descrito.

Permite conocer el impacto de futuras modificaciones.

---

# Formato

Las referencias utilizarán siempre enlaces Markdown relativos.

Ejemplo:

```markdown
# Dependencias

- [Salteado en Wok](../../00_Bases/salteado_en_wok.md)
- [Salsa de Soja](../../11_Despensa/salsa_de_soja.md)

# Véase también

- [Salsa Teriyaki](../../07_Cocina_Asiatica/salsa_teriyaki.md)

# Utilizado por

- [Arroz Chaufa](../../01_Arroces/arroz_chaufa.md)
```

---

# Justificación

Las referencias cruzadas aportan varias ventajas:

* navegación más rápida;
* reducción de duplicidades;
* mejor comprensión del conocimiento;
* análisis de dependencias;
* preparación para futuras automatizaciones.

---

# Consecuencias

## Ventajas

* Repositorio navegable.
* Mayor cohesión entre documentos.
* Grafo de conocimiento explícito.
* Mejor experiencia de aprendizaje.
* Posibilidad de generar mapas automáticos.

## Inconvenientes

* Mayor disciplina al mantener enlaces.
* Necesidad de actualizar referencias cuando aparezcan nuevos documentos relacionados.

---

# Impacto futuro

Las referencias podrán utilizarse para construir automáticamente:

* índices temáticos;
* mapas visuales;
* buscadores semánticos;
* recomendaciones de recetas;
* asistentes culinarios basados en IA.

---

# Dependencias

* [ADR-0001 - Filosofía del Proyecto](./ADR-0001-filosofia-del-proyecto.md)
* [ADR-0002 - Estructura del Repositorio](./ADR-0002-estructura-del-repositorio.md)
* [ADR-0003 - El Repositorio Markdown como Fuente Única de Verdad](./ADR-0003-markdown-como-fuente-de-verdad.md)
* [ADR-0005 - Separación del Conocimiento Culinario](./ADR-0005-separacion-del-conocimiento.md)

---

# Véase también

* [GUIA_DE_ESTILO](../../GUIA_DE_ESTILO.md)
* [ESPECIFICACION_DE_DOCUMENTOS](../../ESPECIFICACION_DE_DOCUMENTOS.md)

---

# Utilizado por

Este ADR deberá aplicarse a todos los documentos del proyecto.
