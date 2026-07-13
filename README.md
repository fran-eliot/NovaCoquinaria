# 🍳 NovaCoquinaria

> **Más que un recetario: un Sistema de Gestión del Conocimiento Culinario.**

---

# Descripción

**NovaCoquinaria** es un repositorio personal de cocina desarrollado aplicando principios de ingeniería del software y gestión del conocimiento.

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

## Calidad y automatización

NovaCoquinaria dispone de un framework propio de herramientas que garantiza la coherencia y calidad del conocimiento almacenado para proteger la integridad del SGCC.

Incluye:

- validación de Front Matter;
- control de identificadores únicos;
- validación de enlaces internos;
- generación de estadísticas;
- construcción automática de `site_docs/`.

Validación principal:

```bash
python tools/validate_all.py
```

---

## Knowledge Graph

El proyecto genera un grafo documental a partir de los enlaces internos entre documentos.

Permite:

- visualizar relaciones;
- detectar conocimiento reutilizable huérfano;
- identificar documentos especialmente reutilizados;
- generar estadísticas de conectividad;
- realizar validaciones semánticas iniciales.

```bash
python tools/generate_graph.py
python tools/generate_graph_stats.py
```

El grafo constituye una representación estructural del conocimiento del SGCC y sirve como base para futuras capacidades de análisis e inteligencia.

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

El proyecto dispone de:

- arquitectura documental estable;
- portal MkDocs Material;
- pipeline automático de calidad;
- framework de herramientas reutilizable;
- Knowledge Graph documental;
- validación semántica básica;
- gobernanza mediante estrategia, deuda y madurez del conocimiento;
- colección inicial de conocimiento culinario normalizado.

El proyecto inicia ahora la consolidación de dominios culinarios reutilizables como siguiente etapa de evolución.

---

# Licencia

Repositorio privado de uso personal.

La estrategia de publicación y licencia definitiva se decidirá antes de hacer público el proyecto.
