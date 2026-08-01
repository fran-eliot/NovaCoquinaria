---
id: DOC-0023
titulo: Especificación de Componentes
tipo: especificacion
version: 1.0.0
estado: en_revision
ultima_revision: 2026-07-30
---

# ESPECIFICACIÓN DE COMPONENTES

> **Proyecto:** NovaCoquinaria  
> **Release:** v1.4 – Knowledge Governance  
> **Sistema:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)  
> **Especificación:** v1.0.0

---

# Introducción

El Sistema de Gestión del Conocimiento Culinario organiza su dominio mediante componentes conceptuales capaces de representar unidades de conocimiento con identidad, significado y responsabilidad propias.

Estos componentes constituyen las entidades fundamentales sobre las que se construye el modelo de conocimiento de NovaCoquinaria.

Ejemplos de componentes son:

- una receta;
- un ingrediente;
- una técnica culinaria;
- una base;
- una plantilla;
- una tabla de referencia;
- un menú;
- una colección.

La presente especificación define el modelo oficial de componentes del SGCC y establece las reglas que determinan:

- qué es un componente;
- qué tipos de componentes existen;
- cómo se clasifican;
- qué propiedades poseen;
- cómo deben evolucionar;
- cómo se diferencian de sus representaciones documentales.

Esta especificación constituye la base normativa para las futuras especificaciones de:

- relaciones;
- ontología;
- colecciones;
- Knowledge Graph;
- APIs de conocimiento;
- sistemas RAG;
- asistentes basados en inteligencia artificial.

---

# Objetivo

El objetivo de esta especificación es definir el catálogo conceptual de componentes gestionados por el SGCC.

En particular, establece:

- el concepto general de componente;
- su relación con los activos de conocimiento;
- los principios que regulan su diseño;
- su clasificación funcional;
- las responsabilidades de cada familia de componentes;
- las reglas generales de identidad, composición y reutilización.

Esta especificación permite que el conocimiento culinario pueda representarse de forma consistente con independencia de la tecnología, formato o medio utilizado para almacenarlo.

---

# Alcance

Esta especificación se aplica a todos los componentes conceptuales gestionados por el SGCC.

Incluye componentes pertenecientes a:

- conocimiento culinario;
- organización del conocimiento;
- planificación culinaria;
- documentación de referencia;
- estructuras reutilizables;
- agrupaciones de activos.

También establece las reglas generales necesarias para incorporar nuevos tipos de componentes en el futuro.

No forma parte del alcance de esta especificación:

- definir todas las relaciones posibles entre componentes;
- construir la ontología completa del SGCC;
- establecer formatos físicos de almacenamiento;
- definir normas editoriales;
- describir la estructura interna detallada de cada documento;
- especificar APIs o modelos de base de datos concretos.

Estos aspectos se desarrollarán en especificaciones especializadas.

---

# Dependencias normativas

Esta especificación deberá interpretarse junto con los siguientes documentos:

- `ESPECIFICACION_DE_DOCUMENTOS`;
- `ESPECIFICACION_DE_COLECCIONES`;
- `MODELO_DE_CONOCIMIENTO`;
- `ARQUITECTURA`;
- `GOVERNANCE_MODEL`;
- `QUALITY`.

La especificación de documentos define cómo se representan persistentemente los activos.

La presente especificación define qué entidades conceptuales pueden ser representadas.

La futura especificación de relaciones definirá cómo se conectan entre sí.

La futura especificación de ontología integrará componentes, propiedades y relaciones en un modelo semántico unificado.

---

# Definiciones

Esta sección establece el vocabulario normativo utilizado por el modelo de componentes.

---

## Activo de conocimiento

Entidad identificable que contiene, organiza o representa conocimiento gestionado por el SGCC.

Un activo de conocimiento puede pertenecer al dominio culinario, al modelo conceptual o a la estructura organizativa del sistema.

Ejemplos:

- una receta;
- una técnica;
- un ingrediente;
- una colección;
- una especificación;
- una decisión arquitectónica.

Todo componente es un activo de conocimiento, pero no todo activo de conocimiento tiene por qué ser un componente culinario.

---

## Componente

Activo de conocimiento con identidad, responsabilidad y significado propios dentro del modelo conceptual del SGCC.

Un componente representa una entidad reutilizable que puede existir de forma independiente o participar en estructuras de conocimiento más complejas.

Ejemplos:

- un ingrediente utilizado por varias recetas;
- una técnica aplicada en diferentes preparaciones;
- una receta compuesta por ingredientes y procesos;
- una plantilla utilizada para generar múltiples recetas.

Un componente existe conceptualmente con independencia de la forma en que sea almacenado.

---

## Componente de dominio

Componente que representa conocimiento perteneciente directamente al dominio culinario.

Ejemplos:

- receta;
- ingrediente;
- técnica;
- base culinaria;
- elaboración;
- menú.

---

## Componente estructural

Componente utilizado para organizar, clasificar o reutilizar otros activos.

Ejemplos:

- plantilla;
- tabla;
- colección;
- esquema;
- taxonomía.

---

## Componente atómico

Componente que representa una unidad conceptual mínima dentro del modelo definido.

Su carácter atómico no implica que carezca de propiedades internas, sino que no se descompone en otros componentes con identidad independiente dentro del contexto considerado.

Ejemplos habituales:

- ingrediente;
- técnica;
- unidad de medida;
- concepto culinario.

---

## Componente compuesto

Componente formado mediante la combinación organizada de otros componentes.

Ejemplos:

- receta;
- menú;
- proceso culinario;
- colección temática.

Un componente compuesto mantiene identidad propia y no equivale a la simple suma de sus partes.

---

## Instancia de componente

Manifestación concreta de un tipo de componente.

Ejemplos:

```text
Tipo: Ingrediente
Instancia: Ajo
```

```text
Tipo: Receta
Instancia: Curry japonés
```

```text
Tipo: Técnica
Instancia: Sofreír
```

---

## Tipo de componente

Categoría conceptual que define las propiedades, responsabilidades y comportamientos esperados de un conjunto de componentes.

Ejemplos:

- receta;
- ingrediente;
- técnica;
- base;
- plantilla;
- colección.

---

## Propiedad

Característica descriptiva asociada a un componente.

Ejemplos:

- nombre;
- descripción;
- origen;
- dificultad;
- duración;
- categoría;
- estado.

Las propiedades describen al componente, pero no representan necesariamente vínculos con otros componentes.

---

## Relación

Vínculo semántico entre dos o más componentes o activos de conocimiento.

Ejemplos:

```text
Una receta utiliza un ingrediente.
```

```text
Una técnica se aplica en una elaboración.
```

```text
Una receta deriva de una plantilla.
```

Las relaciones se formalizarán en `ESPECIFICACION_DE_RELACIONES`.

---

## Representación

Forma concreta mediante la que un activo de conocimiento se almacena, intercambia o publica.

Ejemplos:

- documento Markdown;
- objeto JSON;
- registro de base de datos;
- recurso de una API;
- nodo de un grafo;
- fragmento RDF.

La representación no define la identidad conceptual del componente.

---

## Documento canónico

Representación oficial y autoritativa de un activo de conocimiento dentro de la implementación actual del SGCC.

Un documento canónico:

- posee identificador persistente;
- contiene metadatos estructurados;
- constituye la fuente oficial;
- puede generar otras representaciones derivadas.

---

## Colección

Activo organizativo que agrupa componentes relacionados mediante un criterio explícito.

Una colección puede representar:

- una agrupación temática;
- una clasificación;
- una serie;
- un conjunto curado;
- una vista especializada del conocimiento.

La colección organiza componentes, pero no modifica necesariamente su identidad individual.

---

## Ontología

Modelo formal que define:

- los tipos de entidades;
- sus propiedades;
- sus relaciones;
- sus restricciones;
- sus reglas semánticas.

La ontología del SGCC se construirá a partir del modelo de componentes y del modelo de relaciones.

---

# Modelo conceptual general

El SGCC distingue entre el conocimiento, sus componentes y sus representaciones.

```text
Activo de conocimiento
        │
        ├── Componente
        │      │
        │      ├── Componente de dominio
        │      └── Componente estructural
        │
        ├── Documento
        │
        └── Colección
```

Esta clasificación expresa responsabilidades conceptuales, no necesariamente clases técnicas ni estructuras físicas.

Un mismo activo puede participar simultáneamente en distintos contextos.

Por ejemplo:

- una receta es un componente de dominio;
- puede estar representada mediante un documento Markdown;
- puede pertenecer a varias colecciones;
- puede convertirse en un nodo del Knowledge Graph;
- puede exponerse mediante una API.

---

# Separación entre componente y documento

Un componente y un documento no son equivalentes.

El componente representa la entidad conceptual.

El documento representa una posible materialización persistente de dicha entidad.

```text
Componente conceptual
        │
        ▼
Documento canónico
        │
        ├── Markdown
        ├── Front Matter
        └── Enlaces
```

En el futuro, el mismo componente podrá disponer de otras representaciones:

```text
Componente
    │
    ├── Documento Markdown
    ├── Recurso JSON
    ├── Registro de base de datos
    ├── Nodo RDF
    └── Recurso API
```

El cambio de representación no deberá alterar:

- su identidad;
- su significado;
- sus relaciones;
- su trazabilidad.

---

# Separación entre componente y colección

Una colección agrupa componentes, pero no los convierte en partes inseparables de ella.

Ejemplo:

```text
Colección: Recetas japonesas
        │
        ├── Curry japonés
        ├── Ramen
        └── Okonomiyaki
```

Cada receta conserva:

- identidad propia;
- ciclo de vida propio;
- relaciones propias;
- capacidad para pertenecer a otras colecciones.

Una colección no deberá utilizarse para duplicar componentes.

---

# Separación entre componente y relación

Un componente representa una entidad.

Una relación representa el vínculo entre entidades.

Ejemplo:

```text
REC-0042 ── utiliza ── ING-0017
```

Donde:

- `REC-0042` es un componente de tipo receta;
- `ING-0017` es un componente de tipo ingrediente;
- `utiliza` es una relación.

La relación no forma parte de la identidad de ninguno de los componentes, aunque contribuya a definir su significado contextual.

---

# Principios del modelo de componentes

Todo componente gestionado por el SGCC deberá respetar los principios descritos en esta sección.

---

## Identidad persistente

Todo componente canónico deberá disponer de una identidad estable.

Su identificador no deberá cambiar como consecuencia de:

- modificaciones de nombre;
- cambios de ubicación;
- reorganización del repositorio;
- cambios de formato;
- publicación en otros sistemas;
- incorporación a nuevas colecciones.

---

## Responsabilidad única

Cada tipo de componente deberá representar una responsabilidad conceptual claramente delimitada.

No deberán crearse componentes que mezclen responsabilidades incompatibles.

Por ejemplo, una receta no deberá utilizarse como sustituto de:

- una ficha de ingrediente;
- una técnica;
- una tabla de referencia;
- una decisión arquitectónica.

---

## Independencia de la representación

Los componentes deberán definirse mediante su significado, no mediante la tecnología que los almacena.

No deberá decirse:

> Una receta es un archivo Markdown.

Deberá decirse:

> Una receta es un componente culinario que puede representarse mediante un archivo Markdown.

---

## Reutilización

Los componentes deberán diseñarse para poder reutilizarse en distintos contextos.

Ejemplos:

- un ingrediente puede participar en múltiples recetas;
- una técnica puede aplicarse en distintas elaboraciones;
- una base puede utilizarse en numerosos platos;
- una plantilla puede generar diferentes recetas.

---

## Composición

Los componentes podrán combinarse para formar estructuras más complejas.

La composición deberá preservar la identidad de los componentes reutilizados cuando estos representen activos independientes.

---

## Coherencia semántica

Cada componente deberá mantener coherencia entre:

- su tipo;
- su nombre;
- sus propiedades;
- su contenido;
- sus relaciones.

Un componente no deberá declararse de un tipo y asumir la responsabilidad de otro.

---

## Extensibilidad

El modelo deberá permitir incorporar nuevos tipos de componentes sin redefinir completamente la arquitectura existente.

Toda ampliación deberá:

- responder a una necesidad real;
- evitar duplicar tipos existentes;
- mantener compatibilidad;
- documentar sus propiedades y relaciones;
- actualizar las especificaciones afectadas.

---

## Trazabilidad

La evolución de un componente deberá poder reconstruirse mediante:

- su identificador;
- su versionado;
- su historial documental;
- sus relaciones;
- sus representaciones.

---

## Interoperabilidad

Los componentes deberán poder utilizarse mediante distintas tecnologías y sistemas.

El modelo deberá facilitar su integración con:

- bases de datos;
- APIs;
- grafos de conocimiento;
- motores de búsqueda;
- sistemas RAG;
- agentes inteligentes;
- herramientas de publicación.

---

## Evolución sostenible

Los componentes deberán evolucionar sin comprometer la estabilidad del conocimiento existente.

Los cambios deberán preservar, siempre que resulte posible:

- identidad;
- compatibilidad;
- relaciones;
- significado;
- trazabilidad histórica.

---

# Clasificación general de componentes

El SGCC clasifica sus componentes según su responsabilidad conceptual.

```text
Componente
    │
    ├── Componentes de dominio culinario
    │      ├── Ingrediente
    │      ├── Técnica
    │      ├── Base culinaria
    │      ├── Elaboración
    │      ├── Receta
    │      ├── Menú
    │      └── Concepto culinario
    │
    ├── Componentes estructurales
    │      ├── Plantilla
    │      ├── Tabla
    │      ├── Taxonomía
    │      └── Esquema
    │
    └── Componentes organizativos
           ├── Colección
           ├── Serie
           ├── Índice
           └── Catálogo
```

Esta clasificación podrá evolucionar conforme madure el modelo de conocimiento.

---

# Componentes de dominio culinario

Representan conocimiento directamente relacionado con la cocina.

Incluyen entidades, procesos y estructuras propias del dominio culinario.

---

## Ingrediente

Representa una sustancia o producto utilizado en una preparación culinaria.

Ejemplos:

- ajo;
- arroz;
- aceite de oliva;
- leche de coco;
- miso.

---

## Técnica

Representa un método o acción culinaria reutilizable.

Ejemplos:

- sofreír;
- emulsionar;
- marinar;
- confitar;
- fermentar.

---

## Base culinaria

Representa una preparación reutilizable que sirve como fundamento para otras elaboraciones.

Ejemplos:

- caldo;
- sofrito;
- roux;
- fondo oscuro;
- pasta de curry.

---

## Elaboración

Representa una fase o preparación con resultado propio dentro de un proceso culinario.

Puede constituir:

- un subproceso;
- una preparación intermedia;
- una parte reutilizable de una receta;
- un componente interno con identidad funcional.

---

## Receta

Representa una especificación reproducible para obtener una preparación culinaria.

Combina habitualmente:

- ingredientes;
- cantidades;
- técnicas;
- elaboraciones;
- secuencia de pasos;
- condiciones de ejecución;
- resultado esperado.

---

## Menú

Representa una composición planificada de varias preparaciones o recetas.

Puede atender a criterios:

- gastronómicos;
- nutricionales;
- temporales;
- culturales;
- económicos;
- logísticos.

---

## Concepto culinario

Representa una idea, término o principio relevante para comprender el dominio.

Ejemplos:

- umami;
- mise en place;
- punto de cocción;
- equilibrio de sabores;
- estacionalidad.

---

# Componentes estructurales

Permiten organizar y reutilizar conocimiento sin representar necesariamente una preparación culinaria concreta.

---

## Plantilla

Define una estructura reutilizable para crear componentes homogéneos.

Ejemplos:

- plantilla de curry;
- plantilla de guiso;
- plantilla de ensalada;
- plantilla de menú semanal.

---

## Tabla

Representa conocimiento estructurado en forma de correspondencias, equivalencias o referencias.

Ejemplos:

- tabla de temperaturas;
- equivalencias de medidas;
- tiempos de cocción;
- proporciones;
- sustituciones.

---

## Taxonomía

Define una clasificación jerárquica o controlada.

Ejemplos:

- tipos de cocina;
- familias de ingredientes;
- métodos de cocción;
- categorías de recetas.

---

## Esquema

Define la estructura abstracta de un tipo de conocimiento.

Puede utilizarse para:

- validar componentes;
- generar formularios;
- construir APIs;
- definir modelos de datos;
- facilitar interoperabilidad.

---

# Componentes organizativos

Permiten agrupar, localizar y presentar otros activos de conocimiento.

---

## Colección

Agrupa componentes relacionados mediante uno o varios criterios explícitos.

Ejemplos:

- recetas vegetarianas;
- técnicas de cocina japonesa;
- bases culinarias fundamentales;
- menús económicos.

---

## Serie

Representa una secuencia ordenada de componentes relacionados.

Puede utilizarse para:

- recorridos de aprendizaje;
- progresión técnica;
- menús planificados;
- publicaciones temáticas.

---

## Índice

Facilita la localización y navegación entre componentes.

Un índice puede estar generado automáticamente y no necesariamente constituye conocimiento canónico independiente.

---

## Catálogo

Representa una relación estructurada de componentes pertenecientes a un dominio o familia determinada.

Ejemplos:

- catálogo de ingredientes;
- catálogo de técnicas;
- catálogo de plantillas;
- catálogo de especificaciones.

---

# Clasificación por nivel de composición

Además de su responsabilidad funcional, los componentes pueden clasificarse por su nivel de composición.

---

## Componentes atómicos

Representan unidades básicas reutilizables.

Ejemplos:

- ingrediente;
- técnica;
- concepto;
- unidad de medida.

```text
Ingrediente
Técnica
Concepto
Unidad
```

---

## Componentes compuestos

Integran varios componentes para representar una estructura de mayor complejidad.

Ejemplos:

- receta;
- base culinaria;
- menú;
- colección.

```text
Receta
    ├── Ingredientes
    ├── Técnicas
    ├── Elaboraciones
    └── Resultado
```

---

## Componentes híbridos

Algunos componentes pueden comportarse como atómicos o compuestos según el nivel de análisis.

Por ejemplo, una salsa puede considerarse:

- una base reutilizable dentro de una receta;
- una elaboración compuesta por ingredientes y técnicas;
- un resultado culinario independiente.

La clasificación deberá depender de la responsabilidad que el componente tenga dentro del modelo, no de su complejidad física.

---

# Catálogo normativo de componentes

Esta sección define los tipos de componentes reconocidos inicialmente por el SGCC.

Cada componente se describe mediante:

- finalidad;
- responsabilidad;
- propiedades principales;
- restricciones;
- relaciones habituales;
- ejemplos.

El catálogo representa el vocabulario conceptual base del sistema.

La existencia de un tipo en este catálogo no obliga a que todas sus instancias dispongan inmediatamente de una representación documental propia.

---

# Ingrediente

## Finalidad

Representar una sustancia, producto o materia prima utilizada en una preparación culinaria.

Un ingrediente puede ser:

- natural;
- procesado;
- compuesto;
- fresco;
- conservado;
- sólido;
- líquido;
- de origen vegetal, animal, mineral o microbiológico.

---

## Responsabilidad

El componente Ingrediente describe el producto en sí mismo.

No deberá asumir la responsabilidad de:

- una receta completa;
- una técnica;
- una elaboración;
- una marca comercial concreta, salvo que resulte relevante;
- una cantidad utilizada en una receta específica.

La cantidad pertenece al contexto de uso del ingrediente, no necesariamente al ingrediente como entidad.

---

## Propiedades principales

Un ingrediente podrá incluir propiedades como:

- nombre canónico;
- nombres alternativos;
- descripción;
- familia;
- origen;
- forma habitual de comercialización;
- características organolépticas;
- estacionalidad;
- conservación;
- preparación previa;
- alérgenos;
- restricciones dietéticas;
- sustituciones posibles;
- estado de madurez;
- nivel de procesamiento.

---

## Restricciones

Todo ingrediente deberá:

- poseer una identidad diferenciable;
- representar una entidad reutilizable;
- evitar mezclar en una sola instancia productos conceptualmente distintos;
- distinguir el producto genérico de sus variantes cuando estas afecten al uso culinario.

Por ejemplo, podrán modelarse como componentes diferentes:

```text
Arroz basmati
Arroz arborio
Arroz glutinoso
```

si sus propiedades y usos justifican dicha diferenciación.

---

## Relaciones habituales

Un ingrediente puede:

- ser utilizado por una receta;
- formar parte de una base;
- requerir una técnica;
- sustituir a otro ingrediente;
- pertenecer a una familia;
- presentar compatibilidad con otros ingredientes;
- contener o derivar de otros ingredientes;
- estar asociado a una temporada o región.

---

## Ejemplo conceptual

```text
Ingrediente: Miso blanco

Propiedades:
- familia: condimentos fermentados
- origen: Japón
- sabor: suave, salino, umami
- conservación: refrigerado

Relaciones:
- sustituye parcialmente a: miso rojo
- se utiliza en: sopa de miso suave
- combina con: tofu, alga wakame, dashi
```

---

# Técnica culinaria

## Finalidad

Representar una acción o método reutilizable aplicado durante una preparación culinaria.

La técnica describe cómo se transforma un ingrediente, elaboración o preparación.

---

## Responsabilidad

Una técnica debe representar un método generalizable.

No deberá limitarse a describir un paso aislado de una única receta cuando ese paso no posea valor reutilizable.

Por ejemplo:

```text
Sofreír
Emulsionar
Confitar
Fermentar
Escaldar
```

son técnicas reutilizables.

En cambio:

```text
Añadir dos cucharadas de salsa al final
```

es normalmente una instrucción contextual de una receta, no una técnica independiente.

---

## Propiedades principales

Una técnica podrá incluir:

- nombre;
- definición;
- finalidad;
- contexto de aplicación;
- temperatura;
- duración aproximada;
- intensidad;
- equipo necesario;
- señales visuales;
- señales aromáticas;
- errores frecuentes;
- riesgos;
- variantes;
- resultado esperado;
- nivel de dificultad.

---

## Restricciones

Toda técnica deberá:

- representar una acción reproducible;
- describir un resultado observable;
- diferenciarse de una mera instrucción contextual;
- poder aplicarse, en principio, a más de una preparación.

---

## Relaciones habituales

Una técnica puede:

- aplicarse a un ingrediente;
- formar parte de una elaboración;
- ser utilizada por una receta;
- requerir determinado equipo;
- preceder o seguir a otra técnica;
- ser variante de otra técnica;
- producir una transformación concreta.

---

## Ejemplo conceptual

```text
Técnica: Emulsionar

Finalidad:
Combinar de forma estable dos líquidos normalmente inmiscibles.

Propiedades:
- dificultad: media
- resultado esperado: mezcla homogénea
- riesgo: separación de fases

Relaciones:
- se aplica en: mayonesa
- requiere: batido o agitación
- se relaciona con: montar, ligar
```

---

# Base culinaria

## Finalidad

Representar una preparación reutilizable que sirve como fundamento para otras recetas o elaboraciones.

Una base culinaria posee valor propio porque puede utilizarse en múltiples contextos.

---

## Responsabilidad

La base deberá representar una preparación intermedia reutilizable.

No deberá modelarse como base una elaboración que solo tenga sentido dentro de una única receta, salvo que se prevea su reutilización futura.

Ejemplos:

- caldo de verduras;
- sofrito;
- roux;
- fondo de carne;
- pasta de curry;
- salsa de tomate base;
- masa básica.

---

## Propiedades principales

Una base podrá incluir:

- nombre;
- descripción;
- ingredientes;
- proporciones;
- técnicas;
- rendimiento;
- conservación;
- vida útil;
- variantes;
- usos recomendados;
- nivel de concentración;
- condiciones de almacenamiento.

---

## Restricciones

Toda base deberá:

- producir un resultado intermedio reconocible;
- poder reutilizarse en más de un contexto;
- mantener identidad propia;
- diferenciarse claramente de una receta final cuando su finalidad sea estructural.

---

## Relaciones habituales

Una base puede:

- ser utilizada por una receta;
- estar compuesta por ingredientes;
- requerir técnicas;
- derivar de otra base;
- disponer de variantes;
- sustituir parcialmente a otra base;
- formar parte de una plantilla culinaria.

---

## Ejemplo conceptual

```text
Base: Sofrito mediterráneo

Componentes:
- cebolla
- ajo
- tomate
- aceite de oliva

Técnicas:
- picar
- pochar
- reducir

Usos:
- arroces
- guisos
- legumbres
- salsas
```

---

# Elaboración

## Finalidad

Representar una preparación intermedia o una fase culinaria con resultado funcional propio.

La elaboración permite modelar procesos complejos sin reducirlos a una secuencia lineal de instrucciones.

---

## Responsabilidad

Una elaboración describe una transformación parcial dentro de una receta o proceso.

Puede representar:

- una salsa;
- un relleno;
- una guarnición;
- una masa;
- una marinada;
- una crema;
- una mezcla;
- una preparación intermedia.

---

## Propiedades principales

Una elaboración podrá incluir:

- nombre;
- finalidad;
- ingredientes empleados;
- técnicas aplicadas;
- secuencia;
- duración;
- temperatura;
- resultado esperado;
- punto de finalización;
- dependencia de otras elaboraciones;
- posibilidad de preparación anticipada.

---

## Restricciones

Una elaboración deberá:

- producir un resultado identificable;
- poseer cohesión funcional;
- diferenciarse de una técnica;
- no dividir innecesariamente procesos simples.

No toda fase de una receta deberá convertirse en una elaboración independiente.

---

## Relaciones habituales

Una elaboración puede:

- formar parte de una receta;
- utilizar ingredientes;
- aplicar técnicas;
- depender de una base;
- preceder a otra elaboración;
- combinarse con otras elaboraciones;
- reutilizarse en distintas recetas.

---

## Ejemplo conceptual

```text
Elaboración: Salsa de curry

Utiliza:
- pasta de curry
- leche de coco
- caldo

Aplica:
- sofreír
- disolver
- reducir

Forma parte de:
- curry de pollo
- curry vegetal
- curry de tofu
```

---

# Receta

## Finalidad

Representar una especificación culinaria reproducible orientada a obtener un resultado final o claramente consumible.

La receta constituye uno de los componentes compuestos centrales del SGCC.

---

## Responsabilidad

Una receta deberá integrar de forma coherente:

- ingredientes;
- cantidades;
- técnicas;
- elaboraciones;
- secuencia;
- condiciones;
- resultado esperado.

No deberá utilizarse como contenedor genérico de información sobre ingredientes, técnicas o cultura gastronómica cuando dicha información merezca componentes propios.

---

## Propiedades principales

Una receta podrá incluir:

- título;
- descripción;
- raciones;
- tiempo de preparación;
- tiempo de cocción;
- dificultad;
- ingredientes;
- cantidades;
- unidades;
- elaboraciones;
- instrucciones;
- técnicas;
- equipo;
- temperatura;
- origen;
- estilo culinario;
- variantes;
- sustituciones;
- conservación;
- servicio;
- alérgenos;
- valores nutricionales;
- coste estimado;
- nivel de picante;
- estacionalidad.

---

## Restricciones

Toda receta deberá:

- describir un resultado reproducible;
- declarar los componentes necesarios;
- mantener una secuencia comprensible;
- evitar ambigüedades críticas;
- diferenciar claramente ingredientes de instrucciones;
- conservar coherencia entre cantidades, rendimiento y raciones.

---

## Relaciones habituales

Una receta puede:

- utilizar ingredientes;
- aplicar técnicas;
- contener elaboraciones;
- reutilizar bases;
- derivar de una plantilla;
- pertenecer a colecciones;
- ser variante de otra receta;
- sustituir ingredientes;
- formar parte de un menú;
- requerir equipo;
- estar asociada a una región o tradición.

---

## Ejemplo conceptual

```text
Receta: Curry japonés de ternera

Utiliza:
- ternera
- cebolla
- zanahoria
- patata
- roux de curry

Aplica:
- dorar
- sofreír
- cocer
- espesar

Reutiliza:
- base de caldo
- plantilla de guiso

Pertenece a:
- cocina japonesa
- recetas de cuchara
```

---

# Menú

## Finalidad

Representar una selección planificada y coherente de recetas, elaboraciones o preparaciones.

Un menú no es una simple lista, sino una composición orientada a un contexto concreto.

---

## Responsabilidad

El menú deberá expresar una intención de planificación.

Puede responder a criterios:

- gastronómicos;
- temporales;
- nutricionales;
- presupuestarios;
- culturales;
- logísticos;
- dietéticos.

---

## Propiedades principales

Un menú podrá incluir:

- nombre;
- finalidad;
- número de comensales;
- periodo;
- platos;
- orden de servicio;
- coste;
- restricciones;
- equilibrio nutricional;
- tiempo total;
- planificación de preparación;
- reutilización de ingredientes;
- aprovechamiento de sobras.

---

## Restricciones

Todo menú deberá:

- poseer un criterio explícito de composición;
- mantener coherencia entre sus elementos;
- diferenciarse de una colección temática;
- indicar el contexto para el que ha sido diseñado.

Una colección agrupa conocimiento.

Un menú organiza preparaciones para una situación de consumo o planificación.

---

## Relaciones habituales

Un menú puede:

- incluir recetas;
- reutilizar bases;
- compartir ingredientes;
- pertenecer a una planificación semanal;
- satisfacer restricciones dietéticas;
- derivar de una plantilla;
- estar asociado a una temporada o evento.

---

## Ejemplo conceptual

```text
Menú: Semana económica de invierno

Incluye:
- lentejas estofadas
- arroz con verduras
- crema de calabaza
- pollo asado
- pasta con tomate

Criterios:
- bajo coste
- reutilización de ingredientes
- preparación anticipada
- aprovechamiento de sobras
```

---

# Concepto culinario

## Finalidad

Representar una idea, término, principio o categoría necesaria para comprender el dominio culinario.

---

## Responsabilidad

Un concepto culinario explica conocimiento abstracto.

No describe necesariamente una acción, un producto o una preparación concreta.

Ejemplos:

- umami;
- mise en place;
- sazón;
- punto de cocción;
- equilibrio;
- estacionalidad;
- maridaje.

---

## Propiedades principales

Un concepto podrá incluir:

- definición;
- contexto;
- alcance;
- términos relacionados;
- ejemplos;
- contraejemplos;
- aplicaciones;
- origen;
- ambigüedades;
- traducciones o equivalencias.

---

## Restricciones

Todo concepto deberá:

- tener significado relevante para el SGCC;
- evitar definiciones circulares;
- distinguirse de técnicas, ingredientes o recetas;
- utilizar terminología coherente con el vocabulario oficial.

---

## Relaciones habituales

Un concepto puede:

- explicar una técnica;
- clasificar ingredientes;
- contextualizar recetas;
- relacionarse con otros conceptos;
- pertenecer a una taxonomía;
- aparecer en reglas o recomendaciones.

---

# Unidad de medida

## Finalidad

Representar una magnitud o unidad utilizada para expresar cantidades culinarias.

Aunque pueda considerarse un elemento auxiliar, su formalización permite mejorar la interoperabilidad y validación.

---

## Responsabilidad

La unidad deberá representar una medida interpretable.

Ejemplos:

- gramo;
- kilogramo;
- mililitro;
- litro;
- cucharadita;
- cucharada;
- unidad;
- pizca.

---

## Propiedades principales

Una unidad podrá incluir:

- símbolo;
- nombre;
- magnitud;
- sistema;
- equivalencias;
- nivel de precisión;
- contexto cultural;
- carácter exacto o aproximado.

---

## Restricciones

Deberá distinguirse entre:

- unidades exactas;
- unidades domésticas;
- unidades contextuales;
- expresiones aproximadas.

Por ejemplo:

```text
5 g
```

no posee la misma precisión que:

```text
una pizca
```

---

## Relaciones habituales

Una unidad puede:

- cuantificar un ingrediente;
- convertirse en otra unidad;
- depender de la densidad de un ingrediente;
- utilizarse en una tabla de equivalencias.

---

# Equipo culinario

## Finalidad

Representar utensilios, dispositivos o instalaciones utilizados para ejecutar técnicas o recetas.

---

## Responsabilidad

El componente Equipo describe el recurso material necesario o recomendado para una operación culinaria.

Ejemplos:

- cuchillo;
- sartén;
- horno;
- batidora;
- olla a presión;
- termómetro;
- wok.

---

## Propiedades principales

Un equipo podrá incluir:

- nombre;
- categoría;
- finalidad;
- capacidad;
- material;
- fuente de calor;
- rango de temperatura;
- mantenimiento;
- seguridad;
- alternativas;
- nivel de especialización.

---

## Restricciones

Todo equipo deberá representar un recurso reutilizable y no una instrucción.

Las marcas o modelos concretos solo deberán modelarse cuando sus características sean relevantes para el conocimiento.

---

## Relaciones habituales

Un equipo puede:

- ser requerido por una técnica;
- ser recomendado para una receta;
- sustituir a otro equipo;
- limitar cantidades;
- condicionar temperatura o tiempo;
- pertenecer a una categoría.

---

# Plantilla culinaria

## Finalidad

Definir una estructura reutilizable para construir recetas, menús, preparaciones u otros componentes de forma coherente.

---

## Responsabilidad

La plantilla describe un patrón, no una instancia concreta.

Ejemplos:

- plantilla de curry;
- plantilla de guiso;
- plantilla de ensalada completa;
- plantilla de menú semanal;
- plantilla de masa básica.

---

## Propiedades principales

Una plantilla podrá incluir:

- finalidad;
- estructura;
- roles de componentes;
- elementos obligatorios;
- elementos opcionales;
- proporciones;
- reglas;
- puntos de variación;
- restricciones;
- ejemplos de instancias.

---

## Restricciones

Toda plantilla deberá:

- permitir múltiples realizaciones;
- definir una estructura reconocible;
- distinguir componentes obligatorios y variables;
- evitar depender de ingredientes concretos salvo cuando formen parte esencial del patrón.

---

## Relaciones habituales

Una plantilla puede:

- generar recetas;
- estructurar menús;
- requerir determinados tipos de componentes;
- definir proporciones;
- reutilizar técnicas;
- derivar de otra plantilla;
- especializar una plantilla más general.

---

## Ejemplo conceptual

```text
Plantilla: Curry cremoso

Estructura:
1. grasa
2. aromáticos
3. pasta o mezcla de especias
4. líquido
5. ingrediente principal
6. ajuste final

Variaciones:
- curry rojo
- curry verde
- curry amarillo
```

---

# Tabla de referencia

## Finalidad

Representar conocimiento estructurado en forma de equivalencias, correspondencias, rangos o valores comparables.

---

## Responsabilidad

La tabla deberá facilitar una consulta precisa y repetible.

Ejemplos:

- equivalencias de medidas;
- temperaturas internas;
- tiempos de cocción;
- proporciones de arroz y agua;
- sustituciones de ingredientes;
- escalas de picante.

---

## Propiedades principales

Una tabla podrá incluir:

- título;
- propósito;
- variables;
- unidades;
- filas;
- columnas;
- condiciones;
- fuente;
- precisión;
- excepciones;
- fecha de revisión.

---

## Restricciones

Toda tabla deberá:

- declarar claramente qué representa;
- identificar sus unidades;
- evitar valores sin contexto;
- distinguir datos exactos de orientativos;
- documentar excepciones relevantes.

---

## Relaciones habituales

Una tabla puede:

- complementar una técnica;
- apoyar una receta;
- definir conversiones;
- relacionar ingredientes;
- establecer rangos de seguridad;
- formar parte de una colección.

---

# Taxonomía

## Finalidad

Representar un sistema de clasificación controlado y, normalmente, jerárquico.

---

## Responsabilidad

La taxonomía organiza conceptos o componentes según criterios explícitos.

Ejemplos:

- familias de ingredientes;
- tipos de cocción;
- cocinas regionales;
- categorías de recetas;
- tipos de dieta.

---

## Propiedades principales

Una taxonomía podrá incluir:

- nombre;
- propósito;
- categorías;
- jerarquías;
- criterios de pertenencia;
- exclusiones;
- términos preferidos;
- sinónimos;
- profundidad;
- reglas de extensión.

---

## Restricciones

Toda taxonomía deberá:

- utilizar criterios consistentes;
- evitar categorías solapadas sin justificación;
- declarar términos ambiguos;
- diferenciar jerarquía de mera relación temática.

---

## Relaciones habituales

Una taxonomía puede:

- clasificar componentes;
- contener conceptos;
- especializar otra taxonomía;
- alimentar filtros;
- utilizarse en el Knowledge Graph;
- definir vocabularios controlados.

---

# Esquema

## Finalidad

Definir la estructura formal esperada para una familia de componentes o representaciones.

---

## Responsabilidad

El esquema describe qué propiedades pueden o deben existir y con qué restricciones.

Puede servir de base para:

- validación;
- formularios;
- APIs;
- bases de datos;
- serialización;
- generación automática.

---

## Propiedades principales

Un esquema podrá incluir:

- nombre;
- versión;
- tipo de componente;
- campos;
- tipos de datos;
- obligatoriedad;
- cardinalidades;
- restricciones;
- valores permitidos;
- compatibilidad.

---

## Restricciones

Todo esquema deberá:

- representar una necesidad formal;
- mantener versionado;
- preservar compatibilidad cuando resulte posible;
- diferenciar campos obligatorios y opcionales;
- evitar incorporar decisiones puramente visuales.

---

## Relaciones habituales

Un esquema puede:

- validar componentes;
- implementar una especificación;
- derivar en un modelo de datos;
- generar una API;
- especializar otro esquema;
- ser utilizado por herramientas.

---

# Colección

## Finalidad

Agrupar activos de conocimiento relacionados mediante uno o varios criterios explícitos.

---

## Responsabilidad

La colección organiza conocimiento existente.

No crea nuevas identidades para los componentes agrupados ni duplica su contenido.

---

## Propiedades principales

Una colección podrá incluir:

- nombre;
- descripción;
- criterio de pertenencia;
- miembros;
- orden;
- alcance;
- curatoría;
- filtros;
- fecha de creación;
- actualización;
- carácter estático o dinámico.

---

## Restricciones

Toda colección deberá:

- declarar su criterio;
- referenciar componentes existentes;
- evitar duplicar el contenido de sus miembros;
- diferenciarse de un menú, índice o taxonomía.

---

## Relaciones habituales

Una colección puede:

- contener componentes;
- pertenecer a otra colección;
- especializar una colección;
- derivarse de consultas;
- generar una vista;
- alimentar un catálogo o índice.

---

# Serie

## Finalidad

Representar una secuencia ordenada de componentes relacionados mediante una progresión explícita.

---

## Responsabilidad

La serie incorpora orden y continuidad.

Ejemplos:

- aprendizaje de técnicas;
- progresión de dificultad;
- menús semanales;
- colecciones publicadas por entregas;
- evolución de una familia de recetas.

---

## Propiedades principales

Una serie podrá incluir:

- nombre;
- propósito;
- miembros;
- orden;
- criterio de secuencia;
- punto de inicio;
- punto final;
- dependencias;
- ritmo o periodicidad.

---

## Restricciones

Toda serie deberá:

- tener un orden significativo;
- declarar el criterio de secuencia;
- distinguirse de una colección no ordenada;
- preservar la identidad individual de sus miembros.

---

## Relaciones habituales

Una serie puede:

- contener componentes;
- preceder o continuar otra serie;
- formar parte de una colección;
- representar una ruta de aprendizaje;
- derivar de una planificación.

---

# Índice

## Finalidad

Facilitar la localización y navegación entre activos de conocimiento.

---

## Responsabilidad

El índice ofrece acceso organizado, pero no redefine el conocimiento indexado.

Puede generarse manual o automáticamente.

---

## Propiedades principales

Un índice podrá incluir:

- título;
- alcance;
- criterio de orden;
- entradas;
- categorías;
- enlaces;
- filtros;
- fecha de generación.

---

## Restricciones

Todo índice deberá:

- apuntar a fuentes existentes;
- evitar convertirse en una copia de los documentos;
- indicar su alcance;
- poder regenerarse cuando sea automático.

---

## Relaciones habituales

Un índice puede:

- listar componentes;
- organizar una colección;
- derivarse de metadatos;
- alimentar navegación;
- enlazar catálogos;
- pertenecer a una representación publicada.

---

# Catálogo

## Finalidad

Representar un inventario estructurado de componentes pertenecientes a una familia o dominio.

---

## Responsabilidad

El catálogo ofrece una visión sistemática y normalmente exhaustiva dentro de un alcance definido.

Ejemplos:

- catálogo de ingredientes;
- catálogo de técnicas;
- catálogo de plantillas;
- catálogo de especificaciones.

---

## Propiedades principales

Un catálogo podrá incluir:

- alcance;
- criterios de inclusión;
- entradas;
- clasificación;
- estado;
- cobertura;
- fecha de actualización;
- fuente;
- reglas de mantenimiento.

---

## Restricciones

Todo catálogo deberá:

- declarar su alcance;
- diferenciarse de una selección curada;
- indicar si pretende ser exhaustivo;
- evitar duplicar las fuentes canónicas.

---

## Relaciones habituales

Un catálogo puede:

- incluir referencias a componentes;
- derivarse de una taxonomía;
- generar índices;
- alimentar APIs;
- utilizarse para auditorías de cobertura;
- servir de base a validaciones.

---

# Componente de planificación

## Finalidad

Representar decisiones organizativas sobre preparación, consumo, compra o aprovechamiento culinario.

Esta familia incluye estructuras como:

- plan semanal;
- planificación de mise en place;
- plan de preparación;
- lista de compra derivada;
- estrategia de aprovechamiento.

---

## Responsabilidad

Un componente de planificación organiza acciones futuras a partir de otros componentes.

No deberá confundirse con una receta o colección.

---

## Propiedades principales

Podrá incluir:

- periodo;
- objetivos;
- componentes implicados;
- secuencia;
- restricciones;
- recursos;
- tiempos;
- presupuesto;
- dependencias;
- estado de ejecución.

---

## Restricciones

Toda planificación deberá:

- declarar su periodo o contexto;
- diferenciar conocimiento canónico de decisiones temporales;
- poder rastrear los componentes de los que deriva;
- evitar modificar la identidad de las recetas o ingredientes utilizados.

---

## Relaciones habituales

Una planificación puede:

- incluir menús;
- generar listas de compra;
- programar elaboraciones;
- reutilizar recetas;
- considerar disponibilidad;
- optimizar ingredientes;
- coordinar equipos y tiempos.

---

# Componente de restricción culinaria

## Finalidad

Representar una condición que limita, condiciona o modifica la selección y ejecución de componentes culinarios.

Ejemplos:

- alergia;
- intolerancia;
- dieta vegetariana;
- límite presupuestario;
- ausencia de horno;
- tiempo máximo;
- disponibilidad estacional.

---

## Responsabilidad

La restricción describe una condición aplicable a una persona, receta, menú, planificación o contexto.

---

## Propiedades principales

Una restricción podrá incluir:

- tipo;
- descripción;
- severidad;
- ámbito;
- condición;
- excepciones;
- alternativas;
- origen;
- obligatoriedad;
- periodo de aplicación.

---

## Restricciones

Toda restricción deberá:

- expresar una condición interpretable;
- indicar su ámbito;
- diferenciar recomendaciones de prohibiciones;
- evitar inferencias médicas no verificadas;
- permitir evaluar compatibilidad cuando sea posible.

---

## Relaciones habituales

Una restricción puede:

- excluir ingredientes;
- limitar técnicas;
- condicionar recetas;
- modificar menús;
- afectar a una planificación;
- requerir sustituciones;
- derivar de un perfil o contexto.

---

# Componente de resultado culinario

## Finalidad

Representar el resultado esperado o real de una preparación.

Este componente permite diferenciar la especificación de una receta de su ejecución concreta.

---

## Responsabilidad

El resultado describe el estado final obtenido o esperado.

Puede incluir aspectos:

- visuales;
- aromáticos;
- gustativos;
- texturales;
- estructurales;
- de temperatura;
- de rendimiento.

---

## Propiedades principales

Un resultado podrá incluir:

- nombre;
- descripción;
- textura;
- sabor;
- aroma;
- color;
- temperatura;
- rendimiento;
- defectos;
- tolerancias;
- criterios de aceptación.

---

## Restricciones

Todo resultado deberá:

- estar asociado a una preparación o proceso;
- utilizar criterios observables;
- distinguir estado esperado de observación real;
- evitar descripciones puramente subjetivas cuando puedan utilizarse referencias más precisas.

---

## Relaciones habituales

Un resultado puede:

- ser producido por una receta;
- derivar de una elaboración;
- evaluarse mediante criterios;
- presentar defectos;
- compararse con otro resultado;
- satisfacer un objetivo culinario.

---

# Resumen del catálogo inicial

El catálogo inicial de componentes del SGCC queda compuesto por las siguientes familias:

| Familia | Componentes principales |
|---|---|
| Dominio culinario | Ingrediente, Técnica, Base, Elaboración, Receta, Menú, Concepto |
| Magnitudes y recursos | Unidad de medida, Equipo |
| Estructura y reutilización | Plantilla, Tabla, Taxonomía, Esquema |
| Organización | Colección, Serie, Índice, Catálogo |
| Operación y contexto | Planificación, Restricción, Resultado |

Este catálogo no se considera cerrado.

Su evolución deberá realizarse mediante el procedimiento normativo definido en esta especificación y en el modelo de gobernanza del SGCC.

---

# Modelo estructural de los componentes

Esta sección define las reglas estructurales comunes que deben cumplir todos los componentes gestionados por el SGCC.

Mientras que el catálogo anterior describe **qué componentes existen**, este apartado establece **cómo se comportan** dentro del modelo de conocimiento.

---

# Modelo general

Todo componente puede describirse mediante el siguiente modelo conceptual.

```text
Componente
    │
    ├── Identidad
    ├── Tipo
    ├── Propiedades
    ├── Relaciones
    ├── Estado
    ├── Versionado
    ├── Representaciones
    └── Historial
```

Estos elementos constituyen el contrato mínimo del modelo de componentes.

Cada tipo concreto podrá ampliarlo con propiedades especializadas.

---

# Identidad

Todo componente deberá poseer una identidad conceptual propia.

La identidad representa el componente, no su representación documental.

Ejemplo:

```text
Componente

↓

Ingrediente "Ajo"

↓

Documento ING-0008.md

↓

Página HTML

↓

API JSON
```

Aunque existan varias representaciones, todas corresponden al mismo componente.

---

## Identidad persistente

La identidad permanecerá estable durante toda la vida del componente.

No deberá modificarse por:

- cambios de nombre;
- reorganizaciones documentales;
- migraciones tecnológicas;
- generación de nuevas representaciones;
- incorporación a colecciones.

Cuando un componente cambie sustancialmente de significado deberá crearse un componente nuevo y establecer la relación correspondiente entre ambos.

---

# Tipo

Todo componente pertenece exactamente a un tipo principal.

Ejemplos:

```text
Ingrediente

Receta

Técnica

Base

Plantilla
```

Un componente podrá participar en distintos contextos, pero su tipo principal permanecerá estable.

---

## Especialización

Un tipo podrá especializarse.

Ejemplo:

```text
Ingrediente

    │

───────────────

│             │

Vegetal     Animal
```

La especialización deberá:

- mantener la compatibilidad con el tipo padre;
- añadir restricciones o propiedades;
- no modificar la identidad conceptual del componente.

---

# Propiedades

Las propiedades describen un componente.

No representan relaciones.

Ejemplo:

```text
Ingrediente

Nombre

Origen

Estacionalidad

Descripción
```

No son propiedades:

```text
utiliza

forma parte de

sustituye
```

ya que representan relaciones entre componentes.

---

## Propiedades obligatorias

Cada tipo de componente deberá definir un conjunto mínimo de propiedades.

Ejemplo:

```text
Ingrediente

nombre
familia
```

```text
Receta

nombre
resultado esperado
```

---

## Propiedades opcionales

Podrán añadirse propiedades adicionales cuando:

- aporten información relevante;
- no dupliquen otras existentes;
- mantengan compatibilidad con el modelo.

---

# Estado

Todo componente puede encontrarse en distintos estados durante su ciclo de vida.

Modelo general:

```text
Borrador

↓

En revisión

↓

Estable

↓

Obsoleto

↓

Archivado
```

El estado del componente es independiente del estado del documento que lo representa.

Por ejemplo, un componente estable puede estar temporalmente representado mediante un documento en revisión durante una actualización editorial.

---

# Versionado

Los componentes podrán evolucionar sin perder su identidad.

Existen dos niveles claramente diferenciados.

---

## Versión conceptual

Describe cambios en el significado del componente.

Ejemplos:

- redefinir una técnica;
- ampliar una plantilla;
- modificar una taxonomía.

---

## Versión documental

Describe cambios en la representación documental.

Ejemplos:

- reorganizar secciones;
- mejorar redacción;
- actualizar referencias;
- corregir ejemplos.

---

# Cardinalidad

Los componentes pueden participar en relaciones con diferentes cardinalidades.

Ejemplos:

```text
Una receta

utiliza

muchos ingredientes
```

```text
Un ingrediente

aparece en

muchas recetas
```

```text
Una receta

puede utilizar

varias técnicas
```

La cardinalidad concreta de cada relación se definirá en la especificación correspondiente.

---

# Componentes atómicos

Los componentes atómicos representan unidades básicas del conocimiento.

Características:

- identidad propia;
- responsabilidad única;
- reutilización elevada;
- baja dependencia.

Ejemplos:

```text
Ingrediente

Técnica

Concepto

Unidad
```

---

## Propiedades

Los componentes atómicos deberán:

- ser reutilizables;
- evitar incorporar procesos complejos;
- minimizar dependencias innecesarias.

---

# Componentes compuestos

Los componentes compuestos integran otros componentes.

Ejemplo:

```text
Receta

│

├── Ingredientes

├── Técnicas

├── Elaboraciones

└── Resultado
```

---

## Propiedades

Todo componente compuesto deberá:

- mantener identidad propia;
- conservar la identidad de sus partes;
- permitir reutilización de sus componentes internos cuando proceda.

---

# Componentes agregados

La agregación representa una agrupación donde los componentes mantienen independencia completa.

Ejemplo:

```text
Colección

│

├── Receta A

├── Receta B

└── Receta C
```

Eliminar la colección no implica eliminar las recetas.

---

# Componentes compuestos por composición

En la composición existe una dependencia funcional más fuerte.

Ejemplo:

```text
Receta

│

├── Elaboración

│      │

│      ├── Técnica

│      └── Ingredientes
```

La elaboración tiene sentido dentro del contexto definido por la receta, aunque pueda reutilizarse posteriormente.

---

# Componentes derivados

Algunos componentes pueden derivarse automáticamente de otros.

Ejemplos:

```text
Lista de compra

↓

derivada de

↓

Menú semanal
```

```text
Valores nutricionales

↓

calculados desde

↓

Ingredientes
```

Los componentes derivados deberán indicar claramente:

- origen;
- reglas de generación;
- nivel de actualización.

---

# Componentes calculados

Representan información obtenida mediante procesamiento automático.

Ejemplos:

- coste total;
- tiempo estimado;
- balance nutricional;
- emisiones aproximadas;
- cobertura documental.

Su valor podrá regenerarse sin modificar la identidad del componente.

---

# Componentes virtuales

Algunos componentes pueden existir únicamente como construcciones lógicas.

Ejemplos:

```text
Todas las recetas vegetarianas

Recetas de menos de 30 minutos

Ingredientes ricos en umami
```

No requieren necesariamente almacenamiento persistente.

Podrán generarse dinámicamente mediante consultas.

---

# Composición del conocimiento

El SGCC organiza el conocimiento mediante composición progresiva.

```text
Ingrediente

↓

Base

↓

Elaboración

↓

Receta

↓

Menú

↓

Planificación
```

Cada nivel reutiliza los anteriores sin duplicarlos.

---

# Reutilización

Todo componente deberá diseñarse para maximizar su reutilización.

Ejemplo:

```text
Pasta de curry

↓

utilizada por

↓

Curry rojo

Curry verde

Curry vegetal

Curry de pollo
```

Modificar la base actualiza automáticamente todas las recetas que la reutilizan conceptualmente.

---

# Acoplamiento

Los componentes deberán minimizar dependencias innecesarias.

Se priorizará:

```text
Alta cohesión

Bajo acoplamiento
```

Esto facilita:

- mantenimiento;
- evolución;
- reutilización;
- interoperabilidad.

---

# Cohesión

Cada componente deberá representar una única responsabilidad claramente definida.

Ejemplo correcto:

```text
Ingrediente

↓

Ajo
```

Ejemplo incorrecto:

```text
Ingrediente

↓

Ajo y cebolla
```

ya que representa dos componentes distintos.

---

# Granularidad

El modelo debe mantener una granularidad adecuada.

No conviene modelar componentes demasiado grandes:

```text
"Cocina japonesa"
```

ni excesivamente pequeños:

```text
"Cortar una zanahoria concreta en una receta concreta"
```

La granularidad deberá favorecer:

- reutilización;
- comprensión;
- mantenibilidad.

---

# Integridad

Todo componente deberá mantener coherencia interna.

Como mínimo:

- tipo correcto;
- propiedades válidas;
- relaciones compatibles;
- estado coherente;
- identidad única.

Las herramientas podrán verificar automáticamente parte de esta integridad.

---

# Compatibilidad

Los componentes deberán poder utilizarse mediante diferentes tecnologías.

Ejemplos:

```text
Markdown

↓

HTML

↓

JSON

↓

Base de datos

↓

Knowledge Graph

↓

API

↓

RDF
```

Todas las representaciones deberán preservar:

- identidad;
- significado;
- relaciones.

---

# Extensibilidad

El modelo deberá admitir nuevos componentes sin rediseñar la arquitectura.

Para incorporar un nuevo tipo deberán definirse:

- finalidad;
- responsabilidad;
- propiedades;
- restricciones;
- relaciones habituales;
- compatibilidad con el modelo existente.

---

# Restricciones generales

Todo componente del SGCC deberá cumplir las siguientes reglas:

- representar una única responsabilidad principal;
- poseer identidad conceptual propia;
- evitar duplicar componentes existentes;
- permitir trazabilidad;
- mantener coherencia semántica;
- respetar el modelo documental;
- ser compatible con la ontología del proyecto.

---

# Validación de componentes

La validación podrá comprobar, entre otros aspectos:

- tipo válido;
- identidad persistente;
- propiedades obligatorias;
- relaciones permitidas;
- estado;
- coherencia semántica;
- compatibilidad con las especificaciones.

Las reglas concretas podrán automatizarse mediante las herramientas del SGCC.

---

# Compatibilidad con la ontología

Cada componente descrito en esta especificación constituirá una entidad candidata de la ontología del SGCC.

La ontología añadirá posteriormente:

- propiedades formales;
- axiomas;
- restricciones;
- cardinalidades;
- reglas de inferencia;
- vocabulario controlado.

Esta especificación define **las entidades**.

La ontología definirá **su significado formal**.

---

# Compatibilidad con el Knowledge Graph

Cada componente podrá representarse como un nodo del Knowledge Graph.

Ejemplo:

```text
[Receta]
      │
utiliza
      │
[Ingrediente]
      │
requiere
      │
[Técnica]
```

Las relaciones entre nodos se formalizarán en la especificación correspondiente.

---

# Compatibilidad con inteligencia artificial

Los componentes constituyen la unidad semántica fundamental para:

- recuperación de información;
- generación de embeddings;
- sistemas RAG;
- agentes especializados;
- asistentes conversacionales;
- recomendadores culinarios;
- razonamiento sobre conocimiento.

Esta estructura facilita que los modelos de IA trabajen sobre entidades claramente definidas, en lugar de hacerlo únicamente sobre documentos completos.

---

# Transición hacia las siguientes especificaciones

La presente especificación ha definido:

- qué componentes existen;
- cómo se clasifican;
- qué propiedades generales poseen;
- cómo evolucionan;
- cómo se representan.

La siguiente etapa del modelo consiste en definir:

- cómo pueden relacionarse entre sí;
- qué restricciones poseen dichas relaciones;
- cómo construir el grafo de conocimiento del SGCC.

Estos aspectos se desarrollarán en **ESPECIFICACION_DE_RELACIONES.md**, que utilizará los componentes aquí definidos como base para formalizar el modelo semántico del sistema.

---

# Gobernanza de componentes

Esta sección establece las reglas para crear, modificar, versionar, deprecar y retirar tipos de componentes dentro del SGCC.

La incorporación de nuevos componentes no deberá realizarse de forma improvisada.

Todo cambio en el catálogo afecta potencialmente a:

- documentos;
- relaciones;
- ontología;
- esquemas;
- validadores;
- APIs;
- Knowledge Graph;
- sistemas RAG;
- agentes de inteligencia artificial.

Por este motivo, la evolución del modelo de componentes deberá tratarse como una modificación estructural del sistema.

---

# Principios de gobernanza

La gobernanza de componentes se regirá por los siguientes principios.

---

## Necesidad demostrable

No deberá crearse un nuevo tipo de componente si la necesidad puede resolverse mediante:

- una propiedad;
- una relación;
- una especialización;
- una colección;
- una plantilla;
- una representación alternativa;
- un componente ya existente.

La creación de un tipo nuevo deberá responder a una responsabilidad conceptual diferenciada.

---

## Fuente canónica única

Cada componente deberá disponer de una fuente canónica claramente identificable.

Las representaciones derivadas no deberán competir con la fuente oficial.

Ejemplo:

```text
Componente canónico

↓

Documento oficial

↓

Representaciones derivadas

├── HTML
├── JSON
├── API
└── Knowledge Graph
```

---

## Compatibilidad progresiva

Los cambios deberán preservar, siempre que sea posible:

- identidad;
- trazabilidad;
- relaciones;
- interoperabilidad;
- compatibilidad con versiones anteriores.

Las rupturas incompatibles deberán justificarse y documentarse.

---

## Evolución controlada

La ampliación del catálogo deberá realizarse mediante un proceso explícito de revisión.

No deberán introducirse nuevos tipos únicamente porque una implementación concreta los necesite temporalmente.

El modelo conceptual deberá permanecer independiente de decisiones técnicas accidentales.

---

## Responsabilidad definida

Todo tipo de componente deberá declarar con claridad:

- qué representa;
- qué no representa;
- qué propiedades posee;
- qué restricciones aplica;
- con qué componentes puede relacionarse.

---

# Creación de nuevos tipos de componentes

La creación de un nuevo tipo deberá comenzar con una propuesta formal.

---

## Preguntas previas obligatorias

Antes de crear un nuevo tipo deberán responderse, como mínimo, las siguientes preguntas:

1. ¿Qué responsabilidad conceptual representa?
2. ¿Existe ya otro componente con una responsabilidad equivalente?
3. ¿Puede resolverse mediante una propiedad?
4. ¿Puede resolverse mediante una relación?
5. ¿Puede modelarse como especialización de un tipo existente?
6. ¿Posee identidad propia?
7. ¿Puede existir de forma independiente?
8. ¿Será reutilizable?
9. ¿Qué impacto tendrá sobre relaciones, ontología y validación?
10. ¿Qué representaciones necesitará?

Si estas preguntas no pueden responderse con claridad, el nuevo tipo no deberá incorporarse.

---

## Criterios de aceptación

Un nuevo tipo de componente podrá aceptarse cuando:

- represente una responsabilidad diferenciada;
- tenga significado estable;
- disponga de identidad propia;
- no duplique otro tipo;
- pueda definirse mediante propiedades y restricciones claras;
- aporte valor al modelo de conocimiento;
- sea compatible con la arquitectura;
- pueda integrarse en la ontología;
- disponga de una estrategia de validación;
- tenga casos de uso reales.

---

## Información mínima de la propuesta

Toda propuesta deberá incluir:

```text
Nombre del tipo

Finalidad

Responsabilidad

Alcance

Propiedades

Restricciones

Relaciones habituales

Ejemplos

Contraejemplos

Impacto arquitectónico

Impacto documental

Impacto ontológico
```

---

# Procedimiento de incorporación

La incorporación de un nuevo tipo seguirá el siguiente flujo.

```text
Necesidad detectada

↓

Análisis de reutilización

↓

Propuesta formal

↓

Revisión conceptual

↓

Revisión arquitectónica

↓

Actualización de especificaciones

↓

Implementación

↓

Validación

↓

Aprobación

↓

Publicación
```

---

## Análisis de reutilización

Antes de crear un tipo nuevo deberá evaluarse si la necesidad puede cubrirse mediante:

- un componente existente;
- una especialización;
- una propiedad adicional;
- una relación;
- una colección dinámica;
- una vista;
- una representación derivada.

---

## Revisión conceptual

La revisión conceptual deberá comprobar:

- claridad semántica;
- unicidad de responsabilidad;
- coherencia terminológica;
- nivel adecuado de granularidad;
- compatibilidad con el catálogo existente.

---

## Revisión arquitectónica

La revisión arquitectónica deberá analizar:

- impacto sobre el modelo de conocimiento;
- impacto sobre relaciones;
- impacto sobre la ontología;
- impacto sobre almacenamiento;
- impacto sobre APIs;
- impacto sobre validadores;
- impacto sobre herramientas de IA.

---

## Actualización normativa

La incorporación de un nuevo tipo deberá actualizar, cuando corresponda:

- `ESPECIFICACION_DE_COMPONENTES`;
- `ESPECIFICACION_DE_RELACIONES`;
- `ESPECIFICACION_DE_ONTOLOGIA`;
- `MODELO_DE_CONOCIMIENTO`;
- esquemas;
- catálogos;
- validadores;
- documentación de APIs.

---

# Modificación de tipos existentes

No toda evolución requiere crear un tipo nuevo.

Los tipos existentes podrán modificarse cuando el cambio no altere su identidad esencial.

---

## Cambios compatibles

Se consideran normalmente compatibles:

- añadir propiedades opcionales;
- ampliar ejemplos;
- mejorar definiciones;
- añadir relaciones permitidas;
- incorporar nuevas representaciones;
- documentar restricciones ya implícitas;
- añadir sinónimos o vocabulario controlado.

---

## Cambios potencialmente incompatibles

Requieren revisión especial:

- cambiar la responsabilidad del tipo;
- eliminar propiedades obligatorias;
- modificar cardinalidades;
- alterar su significado;
- fusionar dos tipos;
- dividir un tipo en varios;
- cambiar su relación con la ontología;
- modificar identificadores o nomenclaturas persistentes.

---

## Cambios incompatibles

Un cambio se considerará incompatible cuando provoque que instancias válidas dejen de serlo o que el significado previo ya no pueda interpretarse correctamente.

Ejemplos:

- redefinir una receta como simple texto narrativo;
- convertir una colección en componente de dominio;
- eliminar una relación obligatoria;
- cambiar el sentido de una propiedad existente.

Los cambios incompatibles deberán implicar:

- nueva versión mayor;
- estrategia de migración;
- periodo de transición;
- actualización de dependencias;
- documentación explícita.

---

# Versionado del modelo de componentes

El catálogo de componentes seguirá versionado semántico.

Formato:

```text
MAJOR.MINOR.PATCH
```

---

## Versión mayor

Se incrementará cuando existan cambios incompatibles.

Ejemplos:

- redefinición de tipos;
- eliminación de componentes;
- cambios de identidad;
- reestructuración profunda del catálogo;
- modificación de reglas fundamentales.

---

## Versión menor

Se incrementará cuando se incorporen cambios compatibles.

Ejemplos:

- nuevos tipos;
- nuevas propiedades opcionales;
- nuevas relaciones compatibles;
- especializaciones;
- ampliaciones del catálogo.

---

## Versión de parche

Se incrementará para cambios editoriales o aclaraciones que no alteren el modelo.

Ejemplos:

- correcciones;
- ejemplos;
- mejoras de redacción;
- referencias;
- aclaraciones semánticas.

---

# Versionado de componentes individuales

Además de la versión de la especificación, una instancia concreta podrá disponer de su propia versión.

Ejemplo:

```text
Tipo: Plantilla culinaria
Instancia: Plantilla de guiso
Versión: 2.1.0
```

La versión individual deberá reflejar cambios relevantes en su significado o estructura.

---

# Deprecación

Un componente o tipo podrá declararse obsoleto cuando:

- haya sido sustituido;
- presente ambigüedades;
- duplique otro componente;
- resulte incompatible con el modelo actual;
- ya no deba utilizarse en nuevas contribuciones.

---

## Estado obsoleto

Un componente obsoleto:

- conservará su identificador;
- permanecerá accesible;
- no deberá utilizarse en nuevas contribuciones;
- deberá indicar su sustituto cuando exista;
- deberá mantener trazabilidad histórica.

Ejemplo:

```text
Estado: obsoleto
Sustituido por: CMP-0048
```

---

## Periodo de transición

La deprecación deberá incluir, cuando proceda:

- fecha de inicio;
- versión afectada;
- sustituto recomendado;
- instrucciones de migración;
- fecha prevista de retirada.

---

# Archivado

El archivado representa la retirada operativa de un componente sin eliminar su existencia histórica.

Un componente archivado:

- no participa en operaciones normales;
- no deberá aparecer en catálogos activos;
- podrá mantenerse para auditoría;
- conservará su identidad;
- podrá ser consultado por herramientas históricas.

---

# Eliminación

La eliminación física deberá evitarse.

Solo podrá considerarse cuando:

- el componente se haya creado por error;
- no haya sido publicado;
- no tenga relaciones;
- no haya sido referenciado;
- no forme parte del historial oficial.

En cualquier otro caso se preferirá:

```text
Deprecación

↓

Archivado
```

---

# Fusión de componentes

Dos componentes podrán fusionarse cuando representen la misma entidad o responsabilidad.

La fusión deberá definir:

- componente superviviente;
- componentes deprecados;
- relaciones migradas;
- propiedades consolidadas;
- conflictos resueltos;
- trazabilidad.

Ejemplo:

```text
CMP-0012

+

CMP-0037

↓

CMP-0012
```

El identificador superviviente deberá conservarse como canónico.

---

# División de componentes

Un componente podrá dividirse cuando contenga responsabilidades distintas.

Ejemplo:

```text
Componente antiguo:
"Salsa y marinada"

↓

Componentes nuevos:
"Salsa"
"Marinada"
```

La división deberá:

- crear nuevas identidades;
- conservar el componente original como obsoleto;
- establecer relaciones de derivación;
- migrar referencias;
- documentar el criterio.

---

# Renombrado

El nombre visible de un componente puede cambiar sin modificar su identidad.

Ejemplo:

```text
Nombre anterior: Sofrito básico
Nombre nuevo: Sofrito mediterráneo
Identificador: sin cambios
```

El renombrado deberá conservar:

- alias;
- nombres anteriores;
- referencias;
- historial.

---

# Especialización

Un tipo podrá especializarse cuando exista una subcategoría con propiedades o restricciones propias.

Ejemplo:

```text
Ingrediente

↓

Ingrediente fermentado
```

La especialización no deberá crearse únicamente por motivos de presentación.

Deberá aportar significado o comportamiento adicional.

---

# Generalización

Varios tipos podrán generalizarse bajo un tipo común cuando compartan una responsabilidad estructural.

Ejemplo:

```text
Receta
Base
Elaboración

↓

Preparación culinaria
```

La generalización deberá mejorar el modelo sin eliminar diferencias relevantes.

---

# Identificadores

Los identificadores deberán ser:

- únicos;
- persistentes;
- no ambiguos;
- independientes del nombre;
- independientes de la ubicación;
- compatibles con herramientas automáticas.

---

## Inmutabilidad

Un identificador asignado no deberá reutilizarse.

Incluso si un componente se archiva, su identificador permanecerá reservado.

---

## Prefijos

Los prefijos podrán utilizarse para facilitar reconocimiento.

Ejemplos:

```text
ING-0001

TEC-0001

REC-0001

BAS-0001

TPL-0001
```

Los prefijos son una convención de representación, no la identidad semántica completa.

---

# Validación normativa

Todo componente deberá superar validaciones estructurales y semánticas.

---

## Validación estructural

Podrá comprobar:

- identificador;
- tipo;
- versión;
- estado;
- propiedades obligatorias;
- formato;
- referencias;
- esquema.

---

## Validación semántica

Podrá comprobar:

- coherencia entre tipo y contenido;
- compatibilidad de relaciones;
- duplicidades;
- granularidad;
- responsabilidad;
- vocabulario controlado;
- restricciones ontológicas.

---

## Validación automática

Las herramientas del SGCC podrán verificar automáticamente:

- identificadores duplicados;
- tipos desconocidos;
- propiedades inválidas;
- relaciones no permitidas;
- enlaces rotos;
- estados incoherentes;
- referencias a componentes inexistentes.

---

## Validación humana

La revisión humana seguirá siendo necesaria para evaluar:

- calidad conceptual;
- ambigüedad;
- utilidad;
- coherencia culinaria;
- adecuación de la granularidad;
- impacto arquitectónico.

---

# Matriz de decisión para nuevos componentes

Antes de crear un tipo nuevo deberá aplicarse la siguiente matriz.

| Pregunta | Sí | No |
|---|---|---|
| ¿Tiene identidad propia? | continuar | no crear |
| ¿Posee responsabilidad diferenciada? | continuar | reutilizar |
| ¿Puede existir independientemente? | continuar | considerar propiedad |
| ¿Será reutilizable? | continuar | considerar elaboración contextual |
| ¿No duplica otro tipo? | continuar | fusionar o reutilizar |
| ¿Puede definirse con reglas claras? | continuar | revisar concepto |
| ¿Aporta valor al modelo? | continuar | descartar |
| ¿Puede validarse? | aceptar propuesta | redefinir |

---

# Registro de cambios

Toda modificación relevante deberá documentarse mediante:

- historial de versión;
- commit;
- pull request;
- entrada en BITÁCORA;
- ADR cuando exista impacto arquitectónico.

---

# ADR asociados

Será obligatorio crear un ADR cuando el cambio afecte a:

- estructura fundamental del catálogo;
- identidad de componentes;
- clasificación principal;
- compatibilidad;
- ontología;
- interoperabilidad;
- estrategia de almacenamiento;
- relación entre componente y documento.

---

# Responsabilidades

La gobernanza de componentes podrá implicar distintos roles.

---

## Autor

Responsable de proponer o modificar un componente.

Deberá:

- justificar la necesidad;
- documentar el tipo;
- proporcionar ejemplos;
- analizar impacto;
- actualizar referencias.

---

## Revisor

Responsable de evaluar:

- claridad;
- duplicidad;
- coherencia;
- compatibilidad;
- impacto.

---

## Responsable de arquitectura

Deberá intervenir cuando el cambio afecte a:

- modelo conceptual;
- ontología;
- APIs;
- almacenamiento;
- Knowledge Graph;
- interoperabilidad.

---

## Responsable de calidad

Verificará:

- cumplimiento normativo;
- validaciones;
- trazabilidad;
- documentación;
- compatibilidad.

---

# Relación con otras especificaciones

Esta especificación deberá mantenerse coordinada con:

- `ESPECIFICACION_DE_DOCUMENTOS`;
- `ESPECIFICACION_DE_RELACIONES`;
- `ESPECIFICACION_DE_ONTOLOGIA`;
- `ESPECIFICACION_DE_COLECCIONES`;
- `MODELO_DE_CONOCIMIENTO`;
- `GOVERNANCE_MODEL`;
- `QUALITY`;
- `ARCHITECTURE`.

---

# Referencias

## Documentación estratégica

- `README.md`
- `NovaCoquinaria.md`
- `VISION.md`
- `MANIFESTO.md`

---

## Arquitectura

- `ARQUITECTURA.md`
- `MODELO_DE_CONOCIMIENTO.md`
- `ADR/`

---

## Gobernanza

- `GOVERNANCE_MODEL.md`
- `QUALITY.md`
- `KNOWLEDGE_STRATEGY.md`
- `KNOWLEDGE_MATURITY.md`

---

## Especificaciones

- `ESPECIFICACION_DE_DOCUMENTOS.md`
- `ESPECIFICACION_DE_COLECCIONES.md`
- `ESPECIFICACION_DE_RELACIONES.md`
- `ESPECIFICACION_DE_ONTOLOGIA.md`

---

# Conformidad

Un componente será conforme con esta especificación cuando:

- pertenezca a un tipo reconocido;
- posea identidad persistente;
- respete su responsabilidad;
- incluya las propiedades mínimas;
- mantenga relaciones válidas;
- conserve trazabilidad;
- supere las validaciones aplicables.

Un nuevo tipo será conforme cuando:

- haya seguido el procedimiento de incorporación;
- esté documentado en el catálogo;
- haya sido revisado;
- disponga de reglas de validación;
- sea compatible con el modelo de conocimiento.

---

# Conclusión

La presente especificación define el contrato conceptual de los componentes del SGCC.

Establece:

- qué tipos de componentes existen;
- qué responsabilidad posee cada uno;
- cómo se estructuran;
- cómo se reutilizan;
- cómo evolucionan;
- cómo se incorporan nuevos tipos;
- cómo se preserva su identidad;
- cómo se garantiza su trazabilidad.

Los componentes constituyen la unidad semántica fundamental de NovaCoquinaria.

A partir de ellos pueden construirse:

- documentos;
- colecciones;
- relaciones;
- grafos de conocimiento;
- APIs;
- sistemas RAG;
- agentes inteligentes;
- herramientas de validación;
- interfaces de consulta.

La siguiente especificación deberá formalizar las relaciones entre estos componentes.

Ese trabajo se desarrollará en:

```text
ESPECIFICACION_DE_RELACIONES.md
```

La secuencia conceptual del modelo queda definida como:

```text
Componentes

↓

Relaciones

↓

Ontología

↓

Knowledge Graph

↓

Sistemas inteligentes
```

Con esta especificación, NovaCoquinaria dispone de una base formal para representar el conocimiento culinario de forma coherente, extensible, interoperable y gobernable.
