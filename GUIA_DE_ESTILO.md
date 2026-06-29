# GUÍA DE ESTILO

> **Versión:** 1.0
> **Proyecto:** GASTRO - Manual Personal de Cocina

---

# Objetivo

Este documento define las normas de estilo utilizadas en el repositorio **GASTRO**.

Su finalidad es garantizar que todos los documentos mantengan una estructura homogénea, sean fáciles de leer, reutilizar y mantener, y puedan servir como base para futuras automatizaciones, aplicaciones o sistemas de búsqueda.

Las normas aquí descritas se aplican a todo el repositorio, independientemente del tipo de documento.

---

# Principios generales

Toda la documentación del proyecto debe seguir estos principios:

* Claridad antes que complejidad.
* Un único lugar para cada conocimiento.
* Evitar duplicidades.
* Reutilizar siempre que sea posible.
* Explicar el porqué además del cómo.
* Favorecer la evolución continua del repositorio.
* Escribir pensando tanto en personas como en futuras herramientas de software.

---

# Idioma

Todo el repositorio se redactará en español.

Se conservarán únicamente aquellos términos culinarios extranjeros cuyo uso esté ampliamente aceptado o no tengan una traducción clara.

Ejemplos:

* wok
* mise en place
* umami
* roux
* slurry
* dashi

Cuando proceda, se explicarán en el glosario.

---

# Nomenclatura de archivos

## Reglas

* Utilizar únicamente letras minúsculas.
* Sustituir los espacios por "_".
* Evitar caracteres especiales.
* Utilizar nombres descriptivos.

Ejemplos:

```text
arroz_chaufa.md

caballa_japonesa.md

salteado_asiatico.md

salsa_de_ostras.md
```

---

# Organización del conocimiento

Cada documento debe tener una única responsabilidad.

Ejemplos:

* Una receta describe una elaboración concreta.
* Un documento de despensa describe un ingrediente.
* Un documento base explica una técnica.
* Una plantilla define un patrón reutilizable.
* Una tabla resume información de consulta.

Nunca deben mezclarse responsabilidades.

---

# Formato Markdown

Se utilizarán exclusivamente elementos estándar de Markdown.

* Encabezados
* Listas
* Tablas
* Bloques de código cuando sean necesarios
* Citas únicamente para destacar observaciones importantes

Evitar HTML embebido salvo necesidad justificada.

---

# Encabezados

Todos los documentos comenzarán con un único título de nivel 1.

Ejemplo:

```markdown
# Arroz Chaufa
```

Los apartados principales utilizarán nivel 2.

```markdown
## Ingredientes

## Preparación

## Variantes
```

Los subapartados utilizarán nivel 3.

---

# Uso de listas

Preferir listas cuando la información no requiera párrafos completos.

Ejemplo:

* Ventajas
* Inconvenientes
* Variantes
* Sustituciones

---

# Tablas

Las tablas deberán utilizarse cuando faciliten la comparación.

Ejemplos:

* tiempos
* temperaturas
* equivalencias
* conservación
* sustituciones

Evitar tablas excesivamente grandes.

---

# Unidades

Utilizar siempre el Sistema Internacional cuando sea posible.

## Peso

* g
* kg

## Volumen

* ml
* l

## Temperatura

* °C

## Tiempo

* min
* h

---

# Cantidades

Siempre que sea posible utilizar cantidades objetivas.

Preferir:

```text
10 g de sal
```

en lugar de

```text
una pizca
```

Cuando una cantidad dependa del gusto personal deberá indicarse expresamente.

---

# Enlaces internos

Siempre que exista un documento relacionado deberá enlazarse mediante una ruta relativa.

Ejemplo:

```text
Ver también:

- ../00_Bases/tecnicas.md
- ../11_Despensa/miso.md
```

Evitar repetir explicaciones ya documentadas.

---

# Referencias cruzadas

Cada documento deberá indicar:

## Depende de

Documentos necesarios para comprender su contenido.

## Utilizado por

Documentos que reutilizan este conocimiento.

Estas referencias deberán mantenerse actualizadas siempre que sea posible.

---

# Estilo de redacción

Se utilizará un lenguaje:

* claro
* directo
* técnico cuando sea necesario
* preciso
* sin ambigüedades

Evitar frases excesivamente largas.

Explicar primero la idea general y después los detalles.

---

# Explicaciones técnicas

Siempre que aporte valor, explicar:

* por qué se realiza un paso
* qué ocurre durante la cocción
* errores frecuentes
* cómo corregirlos
* alternativas posibles

El objetivo es comprender la técnica, no únicamente reproducir una receta.

---

# Estructura de una receta

Siempre que sea aplicable, las recetas seguirán esta estructura:

```text
Descripción

Ingredientes

Preparación

Variantes

Trucos

Errores frecuentes

Conservación

Congelación

Recalentado

Acompañamientos

Referencias
```

No todos los apartados serán obligatorios.

---

# Estructura de un documento de despensa

```text
Descripción

Origen

Variedades

Sabor

Usos culinarios

Conservación

Sustituciones

Combinaciones recomendadas

Errores frecuentes

Recetas relacionadas
```

---

# Estructura de una técnica

```text
Objetivo

Fundamentos

Procedimiento

Errores frecuentes

Consejos profesionales

Variantes

Referencias
```

---

# Uso de imágenes

Las imágenes deberán utilizarse únicamente cuando aporten un valor real.

Siempre que sea posible:

* fotografías propias
* esquemas
* diagramas
* tablas

No utilizar imágenes decorativas.

---

# Versionado

Los documentos evolucionan con el tiempo.

Las modificaciones importantes deberán reflejarse en el historial del proyecto.

---

# Automatización futura

Todo el contenido deberá redactarse de forma que pueda ser procesado por futuras herramientas informáticas.

Esto implica:

* estructura consistente
* títulos homogéneos
* nomenclatura estable
* referencias claras
* ausencia de duplicidades

El repositorio debe poder servir como fuente de datos para futuras aplicaciones, asistentes de cocina, buscadores o sistemas basados en inteligencia artificial.

---

# Regla de oro

Antes de crear un nuevo documento, responder siempre a estas preguntas:

1. ¿Existe ya este conocimiento en otro lugar?
2. ¿Estoy duplicando información?
3. ¿Debería ampliar un documento existente?
4. ¿Este contenido será reutilizable en otras recetas?
5. ¿Estoy escribiendo para el "yo del futuro"?

Si alguna respuesta indica que existe una alternativa más reutilizable, deberá priorizarse esa opción.
