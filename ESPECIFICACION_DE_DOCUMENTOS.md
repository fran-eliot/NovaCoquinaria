# ESPECIFICACIÓN DE DOCUMENTOS

> **Versión:** 1.0
> **Proyecto:** NovaCoquinaria
> **Sistema:** GASTRO - Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento define los distintos tipos de documentos utilizados en el repositorio **GASTRO**, su estructura, responsabilidades y metadatos.

Su finalidad es garantizar:

* Homogeneidad.
* Reutilización.
* Ausencia de duplicidades.
* Compatibilidad con futuras automatizaciones.
* Integración con aplicaciones, buscadores o asistentes basados en IA.

Todos los documentos del repositorio deberán ajustarse a esta especificación.

---

# Principios de diseño

Cada documento debe cumplir los siguientes principios:

* Tener una única responsabilidad.
* Ser reutilizable.
* No duplicar información existente.
* Poder evolucionar independientemente.
* Mantener referencias con otros documentos relacionados.

---

# Clasificación de documentos

| Tipo         | Carpeta       | Finalidad                          |
| ------------ | ------------- | ---------------------------------- |
| Arquitectura | Raíz          | Documentación del proyecto         |
| Base         | 00_Bases      | Técnicas y conocimientos generales |
| Receta       | 01–10         | Elaboraciones completas            |
| Ingrediente  | 11_Despensa   | Información sobre productos        |
| Plantilla    | 12_Plantillas | Patrones reutilizables             |
| Tabla        | 98_Tablas     | Consulta rápida                    |
| Nota         | 99_Notas      | Ideas, experimentos y borradores   |

---

# Front Matter (Metadatos)

Todos los documentos deberán comenzar con un bloque **YAML**.

Ejemplo mínimo:

```yaml
---
id: REC-0001
tipo: receta
titulo: Arroz chaufa
version: 1.0
ultima_revision: 2026-06-29
---
```

Los campos podrán variar según el tipo de documento.

---

# Identificador

Cada documento dispondrá de un identificador único.

Formato recomendado:

| Tipo         | Prefijo |
| ------------ | ------- |
| Arquitectura | ARC     |
| Base         | BAS     |
| Receta       | REC     |
| Ingrediente  | ING     |
| Plantilla    | PLA     |
| Tabla        | TAB     |
| Nota         | NOT     |

Ejemplos:

```
ARC-0001
BAS-0004
REC-0017
ING-0009
PLA-0003
TAB-0011
NOT-0002
```

El identificador nunca deberá modificarse.

---

# Documento de Arquitectura

## Finalidad

Describe el funcionamiento del propio proyecto.

### Estructura recomendada

* Objetivo
* Alcance
* Normas
* Referencias

---

# Documento Base

## Finalidad

Explicar una técnica, procedimiento o conocimiento reutilizable.

### Estructura

* Objetivo
* Fundamentos
* Material necesario
* Procedimiento
* Variantes
* Errores frecuentes
* Consejos profesionales
* Referencias

---

# Documento de Receta

## Finalidad

Describir una elaboración culinaria concreta.

### Estructura

* Descripción
* Información general
* Ingredientes
* Mise en place
* Elaboración
* Variantes
* Presentación
* Conservación
* Referencias
* Principio NovaCoquinaria

---

# Documento de Ingrediente

## Finalidad

Documentar un ingrediente o producto de la despensa.

### Estructura

* Descripción
* Origen
* Variedades
* Perfil de sabor
* Propiedades culinarias
* Conservación
* Congelación
* Sustituciones
* Combinaciones recomendadas
* Recetas relacionadas

---

# Documento de Plantilla

## Finalidad

Definir un patrón reutilizable de elaboración.

Ejemplos:

* Curry base
* Guiso base
* Arroz base
* Salteado asiático

### Estructura

* Objetivo
* Patrón general
* Orden de incorporación
* Proporciones orientativas
* Variantes
* Errores frecuentes
* Ejemplos de uso

---

# Documento de Tabla

## Finalidad

Servir como referencia rápida.

### Estructura

* Objetivo
* Tabla
* Notas
* Referencias

---

# Documento de Nota

## Finalidad

Almacenar información temporal.

Podrá contener:

* ideas
* pruebas
* enlaces
* pendientes
* experimentos

Las notas no forman parte del conocimiento consolidado.

---

# Relaciones entre documentos

Los documentos podrán establecer relaciones entre sí.

Tipos de relación recomendados:

## Depende de

Documentos necesarios para comprender el contenido.

## Utilizado por

Documentos que reutilizan este conocimiento.

## Relacionado con

Documentos complementarios.

---

# Versionado

Cada documento tendrá su propia versión.

Formato recomendado:

```
1.0
1.1
1.2
2.0
```

Cambios menores:

* Correcciones.
* Mejoras de redacción.

Cambios mayores:

* Reestructuración.
* Nuevos apartados.
* Cambio de alcance.

---

# Estado del documento

Opcionalmente podrá indicarse su estado.

Valores recomendados:

* Borrador
* En revisión
* Estable
* Obsoleto

---

# Etiquetas

Los documentos podrán clasificarse mediante etiquetas.

Ejemplo:

```yaml
etiquetas:
  - arroz
  - wok
  - cocina china
```

Las etiquetas deberán escribirse siempre en minúsculas.

---

# Referencias internas

Siempre que exista un documento relacionado deberá enlazarse.

Evitar repetir explicaciones ya documentadas.

---

# Compatibilidad futura

Esta especificación está diseñada para permitir que el repositorio pueda utilizarse como fuente de datos para:

* Sitios web estáticos.
* Aplicaciones móviles.
* Sistemas de búsqueda.
* Planificadores de menús.
* Generadores de listas de la compra.
* Asistentes culinarios basados en inteligencia artificial.

---

# Regla fundamental

Antes de crear un documento nuevo, responder siempre a estas preguntas:

1. ¿Ya existe este conocimiento?
2. ¿Estoy duplicando información?
3. ¿Este documento tiene una única responsabilidad?
4. ¿Será reutilizable?
5. ¿Podrá ser comprendido tanto por una persona como por una aplicación?

Cada documento debe responder a una única pregunta principal. Si responde a dos preguntas distintas, probablemente deba dividirse o redistribuirse.

Si alguna respuesta es negativa, deberá revisarse el diseño antes de incorporar el documento al repositorio.
