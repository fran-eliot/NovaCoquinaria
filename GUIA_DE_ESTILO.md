---
id: DOC-0008
titulo: Guía de Estilo
tipo: guia
version: 2.0
estado: estable
ultima_revision: 2026-07-14
---

# GUÍA DE ESTILO

> Guía editorial oficial de NovaCoquinaria.

---

# Objetivo

Este documento establece las normas editoriales utilizadas en NovaCoquinaria para garantizar que el conocimiento del Sistema de Gestión del Conocimiento Culinario (SGCC) sea coherente, reutilizable, verificable y fácil de mantener.

Además de mantener una estructura documental homogénea, la guía busca:

- favorecer la reutilización del conocimiento;
- evitar duplicidades;
- facilitar la evolución del repositorio;
- mejorar la experiencia de lectura;
- servir de base para futuras herramientas, automatizaciones y aplicaciones construidas sobre el SGCC.

La guía se aplica a todos los documentos del repositorio, independientemente de su naturaleza.

---

# Principios generales

Todo el conocimiento del SGCC debe desarrollarse siguiendo los siguientes principios:

- Claridad antes que complejidad.
- Un único lugar para cada conocimiento.
- Evitar duplicidades.
- Reutilizar siempre que sea posible.
- Explicar el porqué además del cómo.
- Favorecer la evolución continua del conocimiento.
- El conocimiento prevalece sobre la estructura documental.
- Cada documento constituye un activo de conocimiento del SGCC.
- Escribir pensando tanto en personas como en futuras herramientas de software.

---

# Idioma

Todo el repositorio se redactará en español.

Se conservarán únicamente aquellos términos culinarios extranjeros ampliamente aceptados o cuya traducción pueda resultar confusa o poco natural.

Ejemplos:

- wok
- mise en place
- umami
- roux
- slurry
- dashi

Cuando sea necesario, estos términos deberán explicarse mediante documentos específicos o referencias cruzadas.

---

# Nomenclatura de archivos

## Reglas generales

Los nombres de archivo deberán cumplir las siguientes normas:

- utilizar únicamente letras minúsculas;
- sustituir los espacios por "_";
- evitar caracteres especiales;
- utilizar nombres descriptivos;
- mantener una nomenclatura estable a lo largo del tiempo.

Ejemplos:

```text
arroz_chaufa.md
caballa_japonesa.md
salteado_asiatico.md
salsa_de_ostras.md
leche_de_coco.md
```

---

# Organización del conocimiento

Cada documento deberá tener una única responsabilidad claramente definida.

Los documentos representan activos de conocimiento independientes que podrán reutilizarse en distintos contextos dentro del SGCC.

Por ejemplo:

- una receta describe una elaboración concreta;
- un ingrediente documenta un producto culinario;
- una técnica explica un procedimiento;
- una plantilla define un patrón reutilizable;
- una tabla resume información de consulta;
- un documento base desarrolla un concepto transversal.

Nunca deberán mezclarse responsabilidades diferentes dentro del mismo documento.

Antes de crear un nuevo documento deberán responderse las siguientes preguntas:

- ¿Existe ya este conocimiento en otro lugar?
- ¿Estoy duplicando información?
- ¿Podría ampliarse un documento existente?
- ¿Este conocimiento será reutilizable?
- ¿Aporta un valor claro al SGCC?

La creación de nuevos documentos deberá responder siempre a una necesidad real del conocimiento y no únicamente a criterios organizativos.

---

# Formato Markdown

NovaCoquinaria utiliza exclusivamente Markdown como fuente de verdad del conocimiento.

Siempre que sea posible se emplearán únicamente elementos estándar del lenguaje para favorecer la portabilidad y la compatibilidad con futuras herramientas.

Se recomienda utilizar:

- encabezados;
- listas;
- tablas;
- bloques de código cuando aporten valor;
- citas para destacar observaciones relevantes.

Deberá evitarse el uso de HTML embebido salvo necesidad técnica justificada.

---

# Encabezados

Todos los documentos comenzarán con un único encabezado de nivel 1.

Ejemplo:

```markdown
# Curry amarillo
```

Los apartados principales utilizarán encabezados de nivel 2.

```markdown
## Descripción

## Usos culinarios

## Conservación
```

Los subapartados utilizarán encabezados de nivel 3 cuando sea necesario estructurar mejor la información.

No deberán utilizarse niveles de encabezado innecesarios.

La jerarquía deberá mantenerse siempre coherente.

---

# Uso de listas

Las listas deberán utilizarse siempre que permitan presentar información de forma más clara que un párrafo.

Son especialmente recomendables para:

- ingredientes;
- variantes;
- ventajas;
- inconvenientes;
- recomendaciones;
- errores frecuentes;
- referencias relacionadas.

Las listas deberán ser breves, homogéneas y fáciles de recorrer visualmente.

---

# Tablas

Las tablas deberán utilizarse únicamente cuando faciliten la comparación o la consulta rápida de información.

Son especialmente adecuadas para:

- tiempos de cocción;
- temperaturas;
- equivalencias;
- sustituciones;
- conservación;
- valores nutricionales;
- comparativas.

Se evitarán tablas excesivamente grandes o difíciles de leer.

---

# Unidades

Siempre que sea posible se utilizará el Sistema Internacional.

## Peso

- g
- kg

## Volumen

- ml
- l

## Temperatura

- °C

## Tiempo

- s
- min
- h

Cuando una unidad no pertenezca al Sistema Internacional pero sea de uso habitual en cocina, podrá utilizarse indicando claramente su significado.

---

# Cantidades

Siempre que sea posible deberán utilizarse cantidades objetivas.

Preferir:

```text
10 g de sal
```

frente a:

```text
Una pizca de sal
```

Cuando una cantidad dependa del gusto personal deberá indicarse expresamente.

Ejemplos:

- al gusto;
- según preferencia;
- opcional.

---

# Referencias cruzadas

Las referencias internas constituyen uno de los mecanismos fundamentales de reutilización del conocimiento dentro del SGCC.

Siempre que exista un documento relacionado deberá enlazarse mediante rutas relativas.

Las referencias podrán indicar, según proceda:

- conocimiento reutilizado;
- documentos relacionados;
- dependencias conceptuales;
- implementaciones derivadas.

El objetivo es minimizar la duplicidad de información y favorecer la navegación por el conocimiento.

Las referencias deberán mantenerse actualizadas siempre que sea posible.

---

# Estilo de redacción

La documentación utilizará un lenguaje:

- claro;
- directo;
- preciso;
- técnico cuando sea necesario;
- libre de ambigüedades.

Siempre que resulte posible se seguirá el siguiente orden:

1. Presentar la idea principal.
2. Explicar los fundamentos.
3. Desarrollar los detalles.
4. Proporcionar recomendaciones o variantes.

Los párrafos deberán ser breves y centrarse en una única idea.

La redacción deberá facilitar tanto la lectura humana como el procesamiento automático del contenido.

---

# Explicaciones técnicas

Siempre que aporte valor al aprendizaje o a la reutilización del conocimiento, los documentos deberán explicar:

- por qué se realiza un procedimiento;
- qué ocurre durante la elaboración;
- errores frecuentes;
- cómo corregirlos;
- alternativas posibles;
- decisiones culinarias relevantes.

El objetivo del SGCC no es únicamente describir procedimientos, sino facilitar la comprensión del conocimiento culinario.

Siempre que sea posible deberá explicarse el motivo de una técnica, ingrediente o decisión culinaria.

---

# Estructuras recomendadas

Las siguientes estructuras constituyen recomendaciones editoriales para mantener la coherencia del SGCC.

No todos los apartados serán obligatorios en todos los documentos.

Su utilización dependerá de la complejidad y naturaleza del contenido.

---

# Estructura recomendada para recetas

```text
Descripción

Objetivo

Información general

Ingredientes

Equipamiento

Preparación

Servicio

Variantes

Conservación

Información nutricional

Consejos NovaCoquinaria

Errores frecuentes

Conocimiento reutilizado

Observaciones

Referencias
```

Las recetas deberán centrarse en describir la elaboración concreta y reutilizar el conocimiento previamente documentado siempre que sea posible.

---

# Estructura recomendada para ingredientes

```text
Descripción

Perfil culinario

Formatos habituales

Usos principales

Comportamiento en cocina

Sustituciones

Conservación

Maridajes

Consejos NovaCoquinaria

Errores frecuentes

Relaciones dentro del SGCC

Observaciones

Referencias
```

Los ingredientes de alta reutilización deberán documentarse con un mayor nivel de detalle.

---

# Estructura recomendada para técnicas

```text
Objetivo

Fundamentos

Procedimiento

Consejos NovaCoquinaria

Errores frecuentes

Variantes

Aplicaciones

Referencias
```

Las técnicas deberán explicar los fundamentos culinarios además del procedimiento.

---

# Estructura recomendada para plantillas

```text
Descripción

Objetivo

Cuándo utilizarla

Ingredientes base

Procedimiento

Personalización

Variantes

Errores frecuentes

Relaciones dentro del SGCC

Referencias
```

Las plantillas representan patrones reutilizables de elaboración y deberán evitar depender de una receta concreta.

---

# Estructura recomendada para tablas

```text
Objetivo

Tabla principal

Notas

Observaciones

Referencias
```

Las tablas constituyen documentos de consulta rápida y deberán priorizar la claridad frente a la exhaustividad.

---

# Desarrollo del conocimiento

NovaCoquinaria desarrolla el conocimiento mediante dominios culinarios.

Siempre que sea posible, los nuevos documentos deberán contribuir a consolidar un dominio antes que ampliar de forma aislada la colección documental.

La prioridad será siempre:

1. Corregir deuda de conocimiento.
2. Crear conocimiento reutilizable.
3. Consolidar un dominio.
4. Crear nuevas recetas.
5. Evolucionar la arquitectura cuando exista una necesidad real.

Las recetas deberán reutilizar el conocimiento previamente documentado y evitar repetir explicaciones ya existentes.

Cada nuevo documento deberá fortalecer el ecosistema de conocimiento del SGCC y aumentar la conectividad entre los distintos activos documentales.

---

# Uso de imágenes

Las imágenes deberán utilizarse únicamente cuando aporten un valor real al conocimiento documentado.

Se priorizarán:

- fotografías propias;
- diagramas;
- esquemas;
- tablas;
- ilustraciones explicativas.

No deberán utilizarse imágenes con una finalidad exclusivamente decorativa.

Siempre que sea posible, las imágenes deberán complementar el texto y no sustituirlo.

---

# Versionado

Los documentos evolucionan junto con el conocimiento del SGCC.

Las modificaciones significativas deberán reflejarse en el historial del proyecto mediante:

- Bitácora;
- Releases;
- Changelog;
- Git.

Las modificaciones menores no requerirán necesariamente una actualización de versión del documento.

---

# Automatización

Toda la documentación deberá redactarse de forma que pueda ser procesada automáticamente por futuras herramientas.

Esto implica mantener:

- estructuras consistentes;
- títulos homogéneos;
- nomenclatura estable;
- referencias claras;
- ausencia de duplicidades;
- relaciones explícitas entre documentos.

El repositorio deberá poder utilizarse como fuente de conocimiento para:

- asistentes culinarios;
- buscadores;
- aplicaciones web;
- aplicaciones móviles;
- sistemas de inteligencia artificial;
- herramientas de análisis del conocimiento.

---

# Evolución de la guía

Esta guía constituye una referencia editorial estable para todo el SGCC.

No deberá modificarse por cambios puntuales en documentos individuales.

Las modificaciones de esta guía deberán responder únicamente a mejoras metodológicas demostradas durante el desarrollo del proyecto.

En caso de duda, deberá priorizarse la estabilidad frente a la incorporación de nuevas normas.

---

# Regla de oro

Antes de crear un nuevo documento deberán responderse las siguientes preguntas:

1. ¿Existe ya este conocimiento en otro lugar?
2. ¿Estoy duplicando información?
3. ¿Podría ampliarse un documento existente?
4. ¿Este conocimiento será reutilizable?
5. ¿Estoy escribiendo para el "yo del futuro"?
6. ¿Este documento fortalece algún dominio culinario del SGCC?

Si alguna respuesta indica que existe una alternativa más reutilizable, deberá priorizarse dicha alternativa.

El objetivo del SGCC no es almacenar más documentos, sino construir un conocimiento culinario cada vez más coherente, conectado y reutilizable.

---

# Referencias

- [README](./README.md)
- [VISION](./docs/VISION.md)
- [ARQUITECTURA](./docs/ARQUITECTURA.md)
- [ROADMAP](./docs/ROADMAP.md)
- [DEVELOPMENT_WORKFLOW](./docs/management/DEVELOPMENT_WORKFLOW.md)
- [KNOWLEDGE_STRATEGY](./docs/management/KNOWLEDGE_STRATEGY.md)
- [KNOWLEDGE_DEBT](./docs/management/KNOWLEDGE_DEBT.md)
- [KNOWLEDGE_MATURITY](./docs/management/KNOWLEDGE_MATURITY.md)
