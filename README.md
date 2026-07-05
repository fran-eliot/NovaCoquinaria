# 🍳 NovaCoquinaria

> **Más que un recetario: un Sistema de Gestión del Conocimiento Culinario.**

---

# Descripción

**NovaCoquinaria** es un repositorio personal de cocina construido como si fuera un proyecto de software.

Su objetivo no es únicamente almacenar recetas, sino capturar, organizar y reutilizar conocimiento culinario de forma modular, mantenible y preparada para evolucionar durante años.

El sistema interno recibe el nombre de **GASTRO - Sistema de Gestión del Conocimiento Culinario (SGCC)**.

---

# Filosofía

En NovaCoquinaria, una receta no debe repetir conocimiento general.

Las técnicas, ingredientes, tablas y plantillas se documentan una sola vez y se reutilizan mediante referencias.

Una receta funciona como un caso de uso: combina conocimientos ya existentes para elaborar un plato concreto.

---

# Organización del repositorio

```text
00_Bases/
        Fundamentos y técnicas culinarias

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

docs/
        Arquitectura, visión, roadmap y ADR
```

---

# Módulos principales

## 98_Tablas

Tablas maestras de consulta rápida:

* conversiones;
* tiempos de cocción;
* temperaturas de horno;
* conservación;
* seguridad alimentaria;
* sustituciones.

## 00_Bases

Fundamentos y técnicas culinarias:

* mise en place;
* saltear;
* sofreír;
* cocinar al wok;
* organización culinaria.

## 11_Despensa

Catálogo práctico de ingredientes:

* salsas;
* condimentos;
* aceites;
* especias;
* cereales;
* productos de uso frecuente.

## 12_Plantillas

Patrones reutilizables:

* salteado asiático;
* curry base;
* salsa china base;
* marinada asiática;
* teriyaki base;
* sofrito mediterráneo;
* vinagreta base.

## Recetas

Aplicaciones concretas del conocimiento:

* arroces;
* verduras;
* carnes;
* pescados y mariscos;
* cocina asiática;
* futuras familias de recetas.

---

# Principios

## 1. Un único lugar para cada conocimiento

Cada técnica, ingrediente o patrón debe documentarse una sola vez.

## 2. Reutilización

Las recetas enlazan al conocimiento existente en lugar de repetirlo.

## 3. Claridad

Todo documento debe ser útil mientras se cocina.

## 4. Evolución continua

Ningún documento se considera definitivo.

## 5. Preparación para automatización

Los documentos se estructuran para poder ser usados en el futuro por una web, aplicación, buscador o asistente con IA.

---

# Documentación del proyecto

Documentos principales:

* [Guía de estilo](./GUIA_DE_ESTILO.md)
* [Especificación de documentos](./ESPECIFICACION_DE_DOCUMENTOS.md)
* [Contribución](./CONTRIBUTING.md)
* [Changelog](./CHANGELOG.md)
* [Arquitectura](./docs/ARQUITECTURA.md)
* [Visión](./docs/VISION.md)
* [Roadmap](./docs/ROADMAP.md)
* [ADR](./docs/adr/)

---

# Estado actual

El proyecto dispone ya de:

* arquitectura documental;
* ADR fundacionales;
* tablas de referencia;
* fundamentos culinarios;
* despensa asiática inicial;
* plantillas culinarias reutilizables;
* colección inicial de recetas normalizadas.

---

# Licencia

Repositorio privado de uso personal.

La estrategia de publicación y licencia definitiva se decidirá antes de hacer público el proyecto.
