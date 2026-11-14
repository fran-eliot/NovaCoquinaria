# 🍳 NovaCoquinaria

> **Más que un recetario: un Sistema de Gestión del Conocimiento Culinario (SGCC).**

---

# Bienvenido

**NovaCoquinaria** es un proyecto personal de ingeniería del conocimiento cuyo objetivo es construir un **Sistema de Gestión del Conocimiento Culinario (SGCC)** capaz de capturar, organizar, relacionar y reutilizar conocimiento culinario de forma estructurada.

En lugar de almacenar recetas como documentos independientes, NovaCoquinaria organiza ingredientes, técnicas, patrones culinarios, recetas y demás entidades dentro de una red de conocimiento preparada para evolucionar durante años.

La arquitectura conceptual que sustenta el proyecto recibe el nombre de **GASTRO**.

---

# ¿Qué encontrarás en este repositorio?

El proyecto se organiza en dos grandes áreas.

## Conocimiento culinario

Contiene el conocimiento funcional del sistema:

- bases culinarias;
- ingredientes y despensa;
- técnicas;
- patrones culinarios;
- platos canónicos;
- variantes;
- recetas;
- tablas de referencia.

Todo este conocimiento constituye el núcleo del SGCC.

### Explorar los módulos culinarios

| Módulo | Índice |
|---|---|
| Pastas | [Pastas](./02_Pastas/README.md) |
| Legumbres | [Legumbres](./03_Legumbres/README.md) |
| Verduras | [Verduras](./04_Verduras/README.md) |
| Carnes | [Carnes](./05_Carnes/README.md) |
| Pescados y mariscos | [Pescados y mariscos](./06_Pescados_y_Mariscos/README.md) |
| Cocina asiática | [Cocina asiática](./07_Cocina_Asiatica/README.md) |
| Postres | [Postres](./08_Postres/README.md) |
| Bebidas | [Bebidas](./09_Bebidas/README.md) |
| Horno | [Horno](./10_Horno/README.md) |
| Ingredientes | [Despensa](./11_Despensa/README.md) |

Otros contenidos, como Arroces, se mantienen accesibles desde su carpeta correspondiente mientras se completa su navegación.

---

## Infraestructura

Proporciona las herramientas necesarias para mantener la calidad y evolución del conocimiento:

- documentación arquitectónica;
- herramientas de validación;
- Knowledge Graph;
- portal MkDocs;
- automatización;
- gobernanza del proyecto.

---

# Organización general

```text
Conocimiento culinario
│
├── 00_Bases/
├── 01_Arroces/
├── ...
├── 11_Despensa/
├── 12_Plantillas/
├── 98_Tablas/
└── 99_Notas/

Infraestructura
│
├── docs/
├── tools/
├── site_docs/
└── mkdocs.yml
```

---

# Primeros pasos

Si es la primera vez que visitas el proyecto, se recomienda seguir este recorrido:

1. **NovaCoquinaria** — identidad y propósito del proyecto.
2. **VISION** — hacia dónde evoluciona el SGCC.
3. **MANIFESTO** — principios que guían todas las decisiones.
4. **ARQUITECTURA** — diseño general del sistema.
5. **MODELO_DE_CONOCIMIENTO** — entidades y relaciones del SGCC.

---

# Calidad del proyecto

NovaCoquinaria incorpora un conjunto de herramientas destinadas a garantizar la coherencia y calidad del conocimiento.

Entre ellas se incluyen:

- validación automática de Front Matter;
- comprobación de identificadores únicos;
- validación de enlaces internos;
- generación del Knowledge Graph;
- construcción automática de la documentación publicada.

Validación principal:

```bash
python tools/validate_all.py
```

---

# Documentación principal

## Identidad

- [NovaCoquinaria](./NovaCoquinaria.md)

## Estrategia

- [VISION](./docs/VISION.md)
- [MANIFESTO](./MANIFESTO.md)

## Arquitectura

- [ARQUITECTURA](./docs/architecture/ARQUITECTURA.md)
- [MODELO_DE_CONOCIMIENTO](./docs/architecture/MODELO_DE_CONOCIMIENTO.md)

## Gobernanza

- [CONTEXT](./CONTEXT.md)
- [CONTRIBUTING](./CONTRIBUTING.md)
- [PROJECT_STRUCTURE](./docs/management/PROJECT_STRUCTURE.md)
- [DEVELOPMENT_WORKFLOW](./docs/management/DEVELOPMENT_WORKFLOW.md)

## Gestión del proyecto

- [PROJECT_STATUS](./docs/management/PROJECT_STATUS.md)
- [CONSOLIDACIÓN DEL CONOCIMIENTO](./docs/management/CONSOLIDACION_CONOCIMIENTO.md)
- [ÍNDICE TRANSVERSAL DEL CONOCIMIENTO](./docs/management/INDICE_NAVEGACION_CONOCIMIENTO.md)
- [ROADMAP](./docs/management/ROADMAP.md)
- [RELEASES](./docs/management/RELEASES.md)
- [CHANGELOG](./CHANGELOG.md)
- [BITACORA](./docs/management/BITACORA.md)
- [ADR](./docs/governance/adr/README.md)

---

# Filosofía

NovaCoquinaria se desarrolla siguiendo un principio sencillo:

> **Documentar una vez. Relacionar siempre. Reutilizar continuamente.**

Los principios completos del proyecto se describen en el documento **MANIFESTO**.

---

# Licencia

Actualmente NovaCoquinaria es un repositorio privado de uso personal.

La política de licencia y publicación se definirá antes de la apertura pública del proyecto.