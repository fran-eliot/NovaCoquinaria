# ADR-0009 - Ciclo de Vida y Versionado del Conocimiento

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Fran Ramírez

---

# Contexto

El conocimiento culinario evoluciona continuamente.

Las recetas se perfeccionan.

Las técnicas se amplían.

Los ingredientes incorporan nuevos usos.

Las referencias aumentan con el tiempo.

Por tanto, ningún documento del proyecto debe considerarse definitivo.

Es necesario establecer un modelo uniforme para gestionar la evolución del conocimiento.

---

# Problema

Sin un proceso definido:

* diferentes documentos evolucionarán de manera desigual;
* será difícil conocer el estado de madurez de cada documento;
* las futuras aplicaciones no podrán distinguir entre conocimiento consolidado y contenido experimental.

---

# Decisión

Todos los documentos del proyecto seguirán un ciclo de vida común y dispondrán de una versión propia.

El estado del documento y su versión formarán parte de sus metadatos.

---

# Ciclo de vida

Todo documento podrá encontrarse en uno de los siguientes estados:

```text
Idea
    │
    ▼
Borrador
    │
    ▼
En revisión
    │
    ▼
Estable
    │
    ▼
Actualizado
    │
    ▼
Obsoleto
```

---

## Idea

Existe el concepto.

Todavía no se ha documentado.

Puede aparecer únicamente en notas o listas de pendientes.

---

## Borrador

El documento ya existe.

Su contenido es incompleto y puede cambiar significativamente.

---

## En revisión

El documento contiene información suficiente, pero está siendo revisado y ampliado.

Puede recibir cambios importantes.

---

## Estable

El contenido se considera fiable.

Podrá seguir evolucionando, pero únicamente mediante mejoras controladas.

La mayoría de las referencias del proyecto deberían apuntar preferentemente a documentos estables.

---

## Actualizado

Estado transitorio que indica que un documento estable ha recibido modificaciones relevantes y está pendiente de consolidación.

Una vez revisado volverá al estado **Estable**.

---

## Obsoleto

El documento ya no representa la mejor forma de documentar ese conocimiento.

Se conserva únicamente por motivos históricos o de compatibilidad.

Siempre deberá indicar el documento que lo sustituye.

---

# Versionado

Todos los documentos tendrán una versión independiente.

Formato:

```text
MAJOR.MINOR.PATCH
```

Ejemplos:

```text
1.0.0
1.1.0
2.0.0
```

---

## Cambios MAJOR

Cambios incompatibles o reestructuraciones importantes.

Ejemplos:

* reorganización completa;
* cambio de enfoque;
* eliminación de secciones principales.

---

## Cambios MINOR

Nuevas capacidades o ampliaciones.

Ejemplos:

* nuevas variantes;
* nuevos ejemplos;
* nuevas referencias;
* ampliación de explicaciones.

---

## Cambios PATCH

Correcciones menores.

Ejemplos:

* ortografía;
* cantidades;
* tiempos;
* enlaces;
* formato.

---

# Relación con CHANGELOG

El historial del documento y el historial del proyecto son conceptos diferentes.

## Documento

Cada documento mantiene:

* versión;
* estado;
* fecha de revisión.

## Proyecto

El archivo `CHANGELOG.md` registra únicamente los cambios relevantes del conjunto del proyecto.

---

# Justificación

Separar estado y versión permite:

* conocer la madurez del conocimiento;
* facilitar revisiones;
* controlar la evolución;
* mejorar la calidad del repositorio.

---

# Alternativas consideradas

## No utilizar estados

**Descartado**.

No permite distinguir conocimiento consolidado de conocimiento experimental.

---

## Versionar únicamente el proyecto

**Descartado**.

Cada documento evoluciona de manera independiente.

---

# Consecuencias

## Ventajas

* Evolución controlada.
* Mayor calidad documental.
* Facilita revisiones.
* Preparado para automatización.
* Compatible con futuras aplicaciones.

## Inconvenientes

* Mayor disciplina de mantenimiento.
* Necesidad de actualizar versiones y estados.

---

# Impacto futuro

Las futuras aplicaciones podrán:

* mostrar únicamente documentos estables;
* filtrar borradores;
* sugerir revisiones;
* detectar documentos obsoletos;
* generar informes de calidad del conocimiento.

---

# Dependencias

* [ADR-0003 - El Repositorio Markdown como Fuente Única de Verdad](./ADR-0003-markdown-como-fuente-de-verdad.md)
* [ADR-0004 - Front Matter YAML como Metadatos Canónicos](./ADR-0004-front-matter-yaml.md)
* [ADR-0008 - Identificadores Únicos y Estables](./ADR-0008-identificadores-unicos.md)

---

# Véase también

* [CHANGELOG](../../CHANGELOG.md)
* [GUIA_DE_ESTILO](../../GUIA_DE_ESTILO.md)
* [ESPECIFICACION_DE_DOCUMENTOS](../../ESPECIFICACION_DE_DOCUMENTOS.md)

---

# Utilizado por

Todos los documentos del proyecto deberán seguir este ciclo de vida y versionado.
