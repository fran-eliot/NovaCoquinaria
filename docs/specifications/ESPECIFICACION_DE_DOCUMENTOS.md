---
id: DOC-0019
tipo: especificacion
titulo: Especificación de documentos
version: 1.0.0
ultima_revision: 2026-07-30
---

# ESPECIFICACIÓN DEL MODELO DOCUMENTAL

> **Versión:** 2.0
> **Proyecto:** NovaCoquinaria
> **Sistema:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento define el modelo documental oficial del Sistema de Gestión del Conocimiento Culinario (SGCC).

Establece los tipos documentales, su estructura, sus metadatos y las relaciones permitidas entre ellos.

Constituye la especificación técnica sobre la que se construyen:

- el repositorio;
- la automatización;
- las herramientas;
- el Knowledge Graph;
- las aplicaciones futuras;
- los asistentes basados en IA.

Toda la documentación del proyecto deberá ajustarse a esta especificación.

---

# Alcance

Esta especificación define:

- los tipos documentales;
- el modelo de metadatos;
- las reglas de identificación;
- la estructura mínima de cada documento;
- las relaciones documentales;
- las normas de versionado.

No define criterios editoriales ni de redacción.

Estos aspectos pertenecen a la Guía de Estilo.

---

# Principios del modelo documental

Todo documento del SGCC deberá cumplir los siguientes principios.

## Responsabilidad única

Cada documento responderá a una única pregunta principal.

---

## Reutilización

El conocimiento deberá escribirse una única vez.

---

## Independencia

Cada documento podrá evolucionar sin afectar a otros documentos.

---

## Trazabilidad

Todo documento será identificable de forma única.

---

## Conectividad

Los documentos podrán establecer relaciones explícitas con otros activos del conocimiento.

---

# Modelo documental

Cada activo del conocimiento sigue el siguiente esquema conceptual.

```text
Activo de conocimiento

↓

Documento

↓

Tipo documental

↓

Metadatos

↓

Contenido

↓

Relaciones
```

---

# Tipos documentales

El SGCC organiza el conocimiento mediante tipos documentales.

| Tipo | Finalidad |
|------|-----------|
| Arquitectura | Definir el funcionamiento del proyecto |
| Base | Desarrollar conocimiento transversal |
| Técnica | Explicar procedimientos reutilizables |
| Receta | Documentar una elaboración |
| Ingrediente | Documentar un producto culinario |
| Plantilla | Definir patrones reutilizables |
| Tabla | Facilitar consultas rápidas |
| Nota | Registrar conocimiento temporal |

Cada tipo posee una responsabilidad claramente diferenciada.

---

# Modelo de metadatos

Todo documento deberá comenzar con un bloque Front Matter YAML.

## Campos obligatorios

```yaml
---
id:
tipo:
titulo:
version:
ultima_revision:
---
```

## Campos opcionales

Ejemplos:

```yaml
estado:
autor:
etiquetas:
dominio:
```

La incorporación de nuevos metadatos deberá mantener la compatibilidad con las herramientas existentes.

---

# Identificadores

Cada documento dispone de un identificador permanente.

Propiedades:

- único;
- estable;
- inmutable;
- independiente del nombre del archivo.

Formato general:

```text
PREFIJO-NNNN
```

Ejemplos:

```text
ARC-0001
REC-0017
ING-0004
```

El identificador nunca deberá reutilizarse.

---

# Estructura documental

Cada tipo documental define una estructura recomendada.

La estructura representa el contrato mínimo que garantiza la coherencia del SGCC.

Cada documento podrá incorporar apartados adicionales cuando aporten valor al conocimiento.

---

# Relaciones documentales

Los documentos podrán establecer relaciones explícitas.

Relaciones habituales:

- depende de;
- relacionado con;
- reutiliza;
- implementa;
- sustituye;
- amplía.

Las relaciones deberán evitar la duplicación del conocimiento.

---

# Versionado

Cada documento evoluciona de forma independiente.

El versionado refleja cambios significativos en la estructura o el conocimiento.

Cambios menores:

- correcciones;
- mejoras de redacción;
- aclaraciones.

Cambios mayores:

- reorganización;
- ampliación del alcance;
- modificación del modelo documental.

---

# Estados documentales

Los documentos podrán encontrarse en distintos estados.

Valores recomendados:

- borrador;
- en revisión;
- estable;
- obsoleto.

---

# Compatibilidad

Esta especificación garantiza la interoperabilidad del SGCC con futuros sistemas.

Entre ellos:

- automatización;
- buscadores;
- aplicaciones móviles;
- aplicaciones web;
- Knowledge Graph;
- asistentes inteligentes;
- modelos RAG;
- agentes de IA.

---

# Evolución

El modelo documental podrá evolucionar manteniendo la compatibilidad hacia atrás siempre que sea posible.

Toda modificación deberá preservar:

- la estabilidad de los identificadores;
- la coherencia del modelo;
- la reutilización del conocimiento.

---

# Relación con otros documentos

| Documento | Responsabilidad |
|-----------|-----------------|
| GUIA_DE_ESTILO | Normas editoriales |
| ARQUITECTURA | Arquitectura general |
| AUTOMATION | Automatización |
| TOOLS_FRAMEWORK | Framework de herramientas |

---

# Conclusión

El modelo documental constituye el lenguaje estructural del SGCC.

Gracias a esta especificación, todo el conocimiento puede representarse de forma homogénea, reutilizarse entre dominios, procesarse automáticamente y evolucionar de manera coherente sin depender de herramientas o tecnologías concretas.