---
id: DOC-0025
titulo: Especificación del Grafo de Conocimiento
tipo: especificacion
version: 1.0.0
estado: en_revision
ultima_revision: 2026-07-30
---

# ESPECIFICACIÓN DEL KNOWLEDGE GRAPH

> Proyecto: NovaCoquinaria
>
> Sistema: GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Parte I — Fundamentos y modelo conceptual

---

# Introducción

Las especificaciones anteriores han definido progresivamente la arquitectura conceptual del SGCC:

1. Modelo documental
2. Componentes de conocimiento
3. Relaciones
4. Ontología
5. Colecciones de Conocimiento

Todas ellas describen **qué conocimiento existe**, **cómo se organiza** y **qué significado posee**.

Sin embargo, aún falta definir el elemento que convierte dicho conocimiento en un sistema navegable, consultable e inferible.

Ese elemento es el **Knowledge Graph**.

El Knowledge Graph constituye la representación formal de todo el conocimiento conectado del SGCC.

No es simplemente una base de datos de grafos.

Es la materialización operativa del conocimiento semántico del sistema.

---

# Objetivo

Esta especificación define el modelo oficial del Knowledge Graph del SGCC.

Sus objetivos son:

- definir el concepto de Knowledge Graph;
- establecer su papel arquitectónico;
- describir su modelo conceptual;
- diferenciarlo de otros componentes;
- definir sus principios;
- establecer sus responsabilidades;
- servir como base para su futura implementación.

---

# Alcance

Esta primera parte regula:

- definición conceptual;
- fundamentos;
- principios;
- arquitectura lógica;
- objetivos;
- responsabilidades;
- relación con el SGCC;
- diferencias respecto a otros modelos;
- tipología de grafos;
- papel dentro de NovaCoquinaria.

No regula todavía:

- almacenamiento físico;
- RDF;
- Neo4j;
- SPARQL;
- Cypher;
- índices;
- rendimiento;
- APIs;
- inferencia;
- RAG.

Estos aspectos se desarrollarán en las partes posteriores.

---

# Motivación

El conocimiento culinario presenta una enorme complejidad.

Una receta puede:

- utilizar ingredientes;
- aplicar técnicas;
- requerir utensilios;
- pertenecer a varias culturas;
- poseer variantes;
- derivar de otras recetas;
- compartir procesos;
- formar parte de múltiples colecciones.

A su vez:

un ingrediente puede:

- pertenecer a varias familias;
- sustituir a otros;
- ser incompatible con determinadas dietas;
- originarse en distintas regiones;
- intervenir en cientos de recetas.

Estas relaciones forman una red extremadamente rica.

Los documentos permiten almacenar el conocimiento.

La ontología permite comprenderlo.

El Knowledge Graph permite recorrerlo.

---

# Definición

El Knowledge Graph del SGCC es la representación estructurada, semántica y navegable del conocimiento culinario gestionado por el sistema.

Materializa las entidades, relaciones, propiedades y contextos definidos por el resto de especificaciones para construir una red coherente de conocimiento interconectado.

El Knowledge Graph constituye la fuente principal para:

- navegación semántica;
- recuperación contextual;
- inferencia;
- razonamiento;
- análisis;
- inteligencia artificial.

---

# Naturaleza

El Knowledge Graph representa simultáneamente:

- una red semántica;
- un modelo de conocimiento;
- una capa de integración;
- una representación navegable;
- una infraestructura para IA.

No representa:

- una base documental;
- un sistema de almacenamiento de archivos;
- una ontología aislada;
- una colección de documentos.

---

# Papel dentro del SGCC

El Knowledge Graph ocupa el núcleo semántico del sistema.

Conceptualmente:

```text
Repositorio documental
        │
        ▼
Documentos
        │
        ▼
Componentes
        │
        ▼
Relaciones
        │
        ▼
Ontología
        │
        ▼
Knowledge Graph
        │
        ▼
Colecciones
        │
        ▼
Razonador
        │
        ▼
RAG
        │
        ▼
Agentes IA
```

Todo el conocimiento operativo pasa por el grafo.

---

# Función principal

La responsabilidad principal del Knowledge Graph consiste en conectar conocimiento.

No genera conocimiento.

No modifica el significado definido por la ontología.

No sustituye los documentos.

Su misión consiste en representar explícitamente cómo todo está relacionado.

---

# Una visión unificada

El Knowledge Graph permite contemplar el SGCC como un único ecosistema.

Por ejemplo:

```text
Miso

↓

Ingrediente

↓

Fermentación

↓

Japón

↓

Sopa de miso

↓

Desayuno tradicional

↓

Cultura japonesa
```

Todo ello forma parte de un único recorrido navegable.

---

# ¿Qué es un Knowledge Graph?

Desde un punto de vista conceptual, un Knowledge Graph es una representación en forma de red donde:

- los nodos representan entidades;
- las aristas representan relaciones;
- las propiedades describen atributos;
- la ontología aporta significado;
- las reglas permiten inferencia.

No se limita a almacenar enlaces.

Cada relación posee significado.

---

# ¿Qué no es un Knowledge Graph?

---

## No es una base de datos relacional

Una base relacional organiza tablas.

Un Knowledge Graph organiza relaciones semánticas.

---

## No es un árbol

Los árboles poseen una única jerarquía.

Un grafo permite múltiples jerarquías simultáneamente.

---

## No es un sistema de etiquetas

Las etiquetas clasifican.

El grafo conecta.

---

## No es únicamente RDF

RDF constituye una posible representación.

El modelo conceptual es independiente.

---

## No es Neo4j

Neo4j constituye una tecnología.

El Knowledge Graph es una arquitectura.

---

## No es la ontología

La ontología responde:

> ¿Qué significa un concepto?

El Knowledge Graph responde:

> ¿Cómo se relacionan todos los conceptos concretos?

---

## No es una colección

Una colección selecciona un dominio.

El Knowledge Graph representa todo el conocimiento conectado.

---

# Diferencia entre Ontología y Knowledge Graph

La relación puede resumirse así.

| Ontología | Knowledge Graph |
|------------|-----------------|
| Modelo conceptual | Instanciación del conocimiento |
| Define significado | Conecta entidades |
| Describe clases | Contiene individuos |
| Define propiedades | Materializa relaciones |
| Define restricciones | Representa hechos |

La ontología constituye el modelo.

El grafo constituye la realidad documentada.

---

# Diferencia con una base de datos

Una base de datos responde:

> ¿Dónde están los datos?

El Knowledge Graph responde:

> ¿Cómo está conectado el conocimiento?

---

# Diferencia con un buscador

Un buscador responde:

> ¿Dónde aparece un término?

El Knowledge Graph responde:

> ¿Qué relación mantiene con el resto del conocimiento?

---

# Diferencia con un índice

Un índice acelera búsquedas.

Un Knowledge Graph representa conocimiento.

---

# Diferencia con RAG

RAG recupera contexto.

El Knowledge Graph proporciona parte de dicho contexto.

---

# Diferencia con el razonador

El razonador utiliza el Knowledge Graph.

No lo sustituye.

---

# Principios fundamentales

Todo Knowledge Graph del SGCC deberá respetar los siguientes principios.

---

## Unicidad

Cada entidad existirá una única vez.

---

## No duplicación

El conocimiento no deberá duplicarse.

---

## Semántica explícita

Toda relación tendrá significado.

---

## Navegabilidad

Todo nodo deberá poder recorrerse.

---

## Explicabilidad

Toda conexión deberá justificarse.

---

## Trazabilidad

Toda información deberá indicar procedencia.

---

## Contextualización

Las relaciones podrán depender del contexto.

---

## Evolución

El grafo podrá evolucionar sin perder coherencia.

---

## Reutilización

Las entidades podrán participar simultáneamente en múltiples dominios.

---

## Modularidad

El grafo podrá dividirse lógicamente.

---

# Objetivos del Knowledge Graph

El grafo deberá permitir:

- conectar conocimiento;
- reducir duplicidades;
- mejorar navegación;
- facilitar inferencias;
- soportar RAG;
- soportar agentes;
- facilitar visualización;
- facilitar análisis.

---

# Arquitectura conceptual

Conceptualmente:

```text
Entidad

↓

Relaciones

↓

Subgrafos

↓

Knowledge Graph

↓

Consultas

↓

Inferencias

↓

Aplicaciones
```

---

# Componentes conceptuales

El Knowledge Graph integra:

- entidades;
- relaciones;
- propiedades;
- contexto;
- procedencia;
- temporalidad;
- restricciones;
- colecciones;
- reglas.

---

# Qué representa el grafo

El Knowledge Graph representa conocimiento explícito.

Ejemplos:

- ingredientes;
- recetas;
- técnicas;
- utensilios;
- procesos;
- documentos;
- regiones;
- culturas;
- autores;
- observaciones.

---

# Qué no representa

No debería representar:

- estados temporales de la interfaz;
- información efímera;
- cachés;
- sesiones;
- configuración técnica.

---

# Alcance del grafo

El Knowledge Graph cubre todo el ecosistema SGCC.

Incluye:

- conocimiento culinario;
- conocimiento documental;
- conocimiento semántico;
- conocimiento organizativo;
- conocimiento analítico.

---

# Dimensiones del Knowledge Graph

Conceptualmente posee varias dimensiones.

---

## Dimensión documental

Relaciona documentos.

---

## Dimensión semántica

Relaciona conceptos.

---

## Dimensión culinaria

Relaciona conocimiento gastronómico.

---

## Dimensión temporal

Relaciona evolución histórica.

---

## Dimensión geográfica

Relaciona regiones.

---

## Dimensión cultural

Relaciona tradiciones.

---

## Dimensión tecnológica

Relaciona herramientas y procesos.

---

## Dimensión analítica

Relaciona métricas.

---

# El grafo como infraestructura

El Knowledge Graph constituye la infraestructura común utilizada por:

- colecciones;
- razonador;
- buscador;
- RAG;
- agentes;
- dashboards;
- APIs.

---

# El grafo como fuente única

Siempre que resulte posible, las aplicaciones deberán consultar el Knowledge Graph en lugar de reconstruir relaciones localmente.

---

# Tipología de grafos

Existen distintos tipos de grafos.

---

## Grafo documental

Relaciona documentos.

---

## Grafo semántico

Relaciona conceptos.

---

## Grafo ontológico

Relaciona clases.

---

## Grafo de instancias

Relaciona individuos concretos.

---

## Grafo de conocimiento

Integra todos los anteriores.

El SGCC utilizará este modelo.

---

# Grafo estático

Representa conocimiento estable.

---

# Grafo dinámico

Puede evolucionar continuamente.

El SGCC utilizará un modelo dinámico versionado.

---

# Grafo dirigido

Las relaciones poseen dirección.

Ejemplo:

```text
Receta

usa

Ingrediente
```

---

# Grafo etiquetado

Las relaciones poseen significado.

Ejemplo:

```text
usa_ingrediente
```

No simplemente:

```text
conectado_con
```

---

# Grafo enriquecido

Las relaciones podrán incorporar:

- confianza;
- contexto;
- procedencia;
- temporalidad;
- evidencia.

---

# Grafo contextual

La misma relación podrá variar según:

- cultura;
- época;
- región;
- dieta.

---

# Grafo versionado

El Knowledge Graph conservará la evolución histórica.

---

# Grafo explicable

Toda inferencia futura deberá poder justificarse mediante recorridos del grafo.

---

# Navegación

Uno de los principales objetivos consiste en permitir recorrer el conocimiento.

Ejemplo:

```text
Kimchi

↓

Fermentación

↓

Corea

↓

Conservación

↓

Bacterias lácticas

↓

Seguridad alimentaria
```

---

# Exploración

El usuario podrá explorar conocimiento sin conocer previamente su estructura.

---

# Descubrimiento

El grafo permitirá descubrir relaciones inesperadas.

---

# Integración con Colecciones

Las Colecciones no almacenan conocimiento.

Seleccionan partes del Knowledge Graph.

Conceptualmente:

```text
Knowledge Graph

↓

Consulta

↓

Subgrafo

↓

Colección
```

---

# Integración con el razonador

El razonador utilizará el grafo para:

- recorrer relaciones;
- aplicar reglas;
- explicar inferencias.

---

# Integración con RAG

El sistema RAG utilizará:

- entidades;
- relaciones;
- contexto;
- subgrafos.

para construir mejores recuperaciones.

---

# Integración con agentes

Los agentes utilizarán el Knowledge Graph como memoria estructurada.

---

# Escalabilidad

El modelo deberá permitir millones de entidades sin modificar su arquitectura conceptual.

---

# Modularidad

El grafo podrá dividirse lógicamente en módulos.

Ejemplos:

- ingredientes;
- técnicas;
- recetas;
- nutrición;
- microbiología.

---

# Interoperabilidad

El modelo conceptual deberá poder implementarse mediante distintas tecnologías.

Ejemplos:

- RDF;
- LPG;
- JSON-LD;
- Neo4j;
- Neptune;
- Blazegraph.

---

# Independencia tecnológica

La especificación describe el modelo.

No una implementación.

---

# Beneficios

El Knowledge Graph aporta:

- conocimiento conectado;
- navegación semántica;
- inferencia;
- reutilización;
- menor duplicidad;
- recuperación contextual;
- soporte para IA;
- explicabilidad.

---

# Conclusión

El Knowledge Graph constituye el núcleo semántico operativo del Sistema de Gestión del Conocimiento Culinario.

Mientras que los documentos almacenan el conocimiento y la ontología define su significado, el grafo materializa las conexiones entre todas las entidades del sistema, convirtiéndolas en una red coherente, navegable y reutilizable.

Gracias a esta representación, el SGCC puede evolucionar desde un repositorio documental hacia una auténtica plataforma de conocimiento, preparada para soportar razonamiento, recuperación aumentada, análisis avanzado y agentes inteligentes.

Las siguientes partes desarrollarán el modelo formal del grafo, incluyendo entidades, relaciones, propiedades, contexto, procedencia, versionado y mecanismos de consulta e inferencia.

---

# Parte II — Modelo formal del grafo

---

# Introducción

La Parte I ha definido el Knowledge Graph como el núcleo semántico operativo del Sistema de Gestión del Conocimiento Culinario.

Esta segunda parte formaliza su estructura interna.

El objetivo consiste en determinar:

- qué elementos forman el grafo;
- cómo se representan las entidades;
- cómo se modelan las relaciones;
- cómo se expresan las propiedades;
- cómo se conserva el contexto;
- cómo se registra la procedencia;
- cómo se representa la temporalidad;
- cómo se distinguen hechos, afirmaciones e inferencias;
- cómo se organizan los subgrafos;
- cómo se preserva la identidad de cada elemento.

El Knowledge Graph deja así de ser únicamente una red conceptual y pasa a convertirse en un modelo formal susceptible de validación, almacenamiento, consulta, versionado e inferencia.

---

# Objetivos del modelo formal

El modelo formal deberá permitir:

- representar conocimiento culinario;
- representar conocimiento documental;
- representar conocimiento semántico;
- conectar entidades heterogéneas;
- expresar relaciones simples y complejas;
- conservar evidencia y procedencia;
- gestionar afirmaciones contradictorias;
- representar cambios temporales;
- diferenciar conocimiento explícito e inferido;
- generar subgrafos reproducibles;
- mantener compatibilidad entre tecnologías de grafo.

---

# Principios del modelo

Todo elemento del Knowledge Graph deberá respetar los siguientes principios.

---

## Identidad estable

Cada entidad, relación y afirmación relevante deberá poseer una identidad persistente.

---

## Semántica explícita

Los tipos y predicados deberán proceder de vocabularios controlados.

---

## Separación entre definición e instancia

Las clases y propiedades deberán distinguirse de sus instancias concretas.

---

## Procedencia obligatoria

Todo hecho deberá poder vincularse con una fuente o proceso de generación.

---

## Contexto preservado

Las afirmaciones dependientes de circunstancias concretas deberán conservar dichas circunstancias.

---

## Temporalidad explícita

Cuando una afirmación solo sea válida durante un periodo, este deberá representarse.

---

## No pérdida de información

Las transformaciones entre representaciones no deberán eliminar contexto, evidencia o significado relevante.

---

## Explicabilidad

Las afirmaciones inferidas deberán conservar el camino o regla que permitió obtenerlas.

---

# Capas del Knowledge Graph

El Knowledge Graph podrá comprenderse mediante varias capas lógicas.

```text
Capa metamodelo
        │
        ▼
Capa ontológica
        │
        ▼
Capa de entidades
        │
        ▼
Capa de afirmaciones
        │
        ▼
Capa contextual
        │
        ▼
Capa de procedencia
        │
        ▼
Capa inferida
```

---

# Capa metamodelo

Define las unidades básicas con las que se construye el grafo.

Ejemplos:

- entidad;
- clase;
- propiedad;
- relación;
- afirmación;
- contexto;
- fuente;
- evidencia;
- versión;
- subgrafo.

---

# Capa ontológica

Define:

- clases;
- propiedades;
- jerarquías;
- restricciones;
- axiomas;
- vocabularios.

Esta capa corresponde principalmente al conocimiento intensional.

---

# Capa de entidades

Contiene individuos concretos.

Ejemplos:

- Miso;
- Sopa de miso;
- Cocción al vapor;
- Japón;
- Receta `REC-0009`;
- Documento `DOC-0023`.

---

# Capa de afirmaciones

Contiene hechos sobre las entidades.

Ejemplo:

```text
REC-0009 usa_ingrediente ING-0008
```

---

# Capa contextual

Describe las circunstancias bajo las que una afirmación debe interpretarse.

Ejemplos:

- región;
- periodo;
- tradición;
- versión;
- perfil dietético;
- entorno culinario.

---

# Capa de procedencia

Describe:

- fuente;
- autor;
- actividad;
- fecha;
- método;
- evidencia;
- responsabilidad.

---

# Capa inferida

Contiene afirmaciones derivadas mediante:

- reglas;
- axiomas;
- recorridos;
- clasificadores;
- procesos de razonamiento.

---

# Niveles de conocimiento

El grafo deberá distinguir entre conocimiento intensional y extensional.

---

## Conocimiento intensional

Describe el modelo general del dominio.

Ejemplo:

```text
Toda receta tiene al menos una preparación.
```

---

## Conocimiento extensional

Describe hechos concretos.

Ejemplo:

```text
La sopa de miso utiliza miso.
```

---

# TBox, ABox y RBox

Cuando se utilice terminología de lógica descriptiva, el grafo podrá distinguir:

---

## TBox

Contiene conocimiento terminológico.

Incluye:

- clases;
- jerarquías;
- restricciones;
- definiciones.

Ejemplo:

```text
IngredienteFermentado
subClassOf
Ingrediente
```

---

## ABox

Contiene afirmaciones sobre individuos.

Ejemplo:

```text
Miso
instanceOf
IngredienteFermentado
```

---

## RBox

Contiene conocimiento sobre propiedades.

Ejemplos:

```text
usa_ingrediente
subPropertyOf
utiliza_recurso
```

```text
deriva_de
transitive
true
```

---

# Modelo abstracto

El Knowledge Graph podrá representarse formalmente como:

```text
KG = (N, E, P, C, V, G)
```

donde:

- `N` representa el conjunto de nodos;
- `E` representa el conjunto de relaciones;
- `P` representa propiedades y predicados;
- `C` representa contextos;
- `V` representa versiones y validez;
- `G` representa subgrafos o grafos nombrados.

---

# Nodo

Un nodo representa una entidad identificable dentro del SGCC.

Todo nodo deberá poseer:

- identificador;
- tipo;
- etiqueta;
- procedencia;
- estado;
- versión o referencia de versión cuando proceda.

---

# Tipos de nodo

El grafo podrá contener diferentes tipos de nodos.

---

## Nodo ontológico

Representa:

- clase;
- propiedad;
- concepto;
- restricción;
- regla.

---

## Nodo de dominio

Representa conocimiento culinario.

Ejemplos:

- ingrediente;
- receta;
- técnica;
- utensilio;
- preparación;
- proceso;
- cocina;
- región.

---

## Nodo documental

Representa:

- documento;
- sección;
- componente;
- fragmento;
- tabla;
- imagen;
- fuente.

---

## Nodo organizativo

Representa:

- colección;
- módulo;
- objetivo;
- deuda;
- hito;
- proyecto.

---

## Nodo contextual

Representa:

- lugar;
- periodo;
- cultura;
- perfil dietético;
- entorno tecnológico;
- situación culinaria.

---

## Nodo de procedencia

Representa:

- persona;
- organización;
- actividad;
- sistema;
- importación;
- proceso de generación.

---

## Nodo analítico

Representa:

- métrica;
- evaluación;
- resultado;
- observación;
- hipótesis.

---

## Nodo operacional

Podrá representar artefactos persistentes relevantes como:

- snapshot;
- materialización;
- índice;
- conjunto de evaluación.

No deberá utilizarse para estados efímeros de ejecución.

---

# Identidad de nodo

Toda entidad deberá poseer un identificador canónico.

Ejemplos:

```text
ING-0008
REC-0009
TEC-0012
DOC-0023
COL-0001
```

---

## URI

Cuando el grafo se publique como Linked Data, el identificador podrá resolverse mediante URI.

Ejemplo conceptual:

```text
https://novacoquinaria.org/entity/ING-0008
```

---

## Persistencia de identidad

El identificador no deberá cambiar cuando:

- cambie el nombre;
- cambie la descripción;
- cambie la ubicación documental;
- cambie la clasificación;
- se publique una nueva versión.

---

## No reutilización

Los identificadores eliminados, archivados o deprecados no deberán reutilizarse.

---

# Identidad conceptual y documental

La identidad de una entidad culinaria deberá diferenciarse de la identidad de los documentos que la describen.

Ejemplo:

```text
ING-0008
Miso
```

es una entidad culinaria.

```text
DOC-0041
Documento sobre el miso
```

es una entidad documental.

Ambas estarán relacionadas, pero no serán equivalentes.

---

# Entidad y representación

Una entidad podrá poseer múltiples representaciones.

Ejemplo:

```text
Miso
├── documento Markdown
├── ficha resumida
├── imagen
├── traducción
├── fragmento RAG
└── representación RDF
```

El nodo de dominio seguirá siendo único.

---

# Etiquetas

Todo nodo deberá poseer una etiqueta legible.

Ejemplo:

```yaml
labels:
  es: Miso
  en: Miso
  ja: 味噌
```

---

# Alias

Los alias se utilizarán para:

- sinónimos;
- nombres históricos;
- transliteraciones;
- variantes ortográficas;
- nombres comerciales;
- términos regionales.

---

# Nombre preferido

Para cada idioma podrá declararse una etiqueta preferida.

---

# Nombres alternativos

Los nombres alternativos no generarán entidades distintas salvo que representen conceptos diferentes.

---

# Tipado de nodos

Todo nodo deberá tener al menos un tipo.

Ejemplo:

```text
ING-0008
instanceOf
IngredienteFermentado
```

---

## Tipado múltiple

Un nodo podrá pertenecer a varias clases compatibles.

Ejemplo:

```text
Miso
instanceOf
IngredienteFermentado
```

```text
Miso
instanceOf
Condimento
```

```text
Miso
instanceOf
ProductoDeSoja
```

---

## Tipo primario

Podrá declararse un tipo primario con fines:

- editoriales;
- visuales;
- operativos;
- de validación.

El tipo primario no eliminará otros tipos semánticos.

---

# Propiedades de nodo

Una propiedad de nodo describe una característica de una entidad.

Ejemplos:

- nombre;
- descripción;
- fecha;
- estado;
- código;
- valor nutricional;
- nivel de dificultad.

---

# Propiedad literal

Relaciona una entidad con un valor literal.

Ejemplo:

```text
REC-0009 tiempo_preparacion "15 minutos"
```

---

# Propiedad de objeto

Relaciona una entidad con otra entidad.

Ejemplo:

```text
REC-0009 usa_ingrediente ING-0008
```

---

# Valores literales

Los literales deberán declarar tipo cuando resulte relevante.

Ejemplos:

```text
"15"^^integer
```

```text
"15.5"^^decimal
```

```text
"2026-07-31"^^date
```

```text
"15 minutos"@es
```

---

# Unidades de medida

Los valores cuantitativos deberán modelarse de forma que la unidad sea explícita.

No se recomienda:

```text
cantidad = "200 g"
```

como única representación estructurada.

Se recomienda:

```text
valor = 200
unidad = gramo
```

---

## Medida como nodo

Cuando una medida necesite contexto, podrá representarse como entidad.

```text
UsoIngrediente
├── ingrediente: Harina
├── cantidad: 200
├── unidad: Gramo
└── tolerancia: 10
```

---

# Propiedades multivaluadas

Una entidad podrá poseer varios valores para una misma propiedad.

Ejemplo:

```text
Miso originario_de Japón
Miso producido_en Corea
Miso producido_en España
```

El significado de cada propiedad deberá ser preciso para evitar contradicciones aparentes.

---

# Propiedades calculadas

Una propiedad calculada se deriva de otros datos.

Ejemplo:

```text
tiempo_total =
tiempo_preparacion
+
tiempo_coccion
+
tiempo_reposo
```

Las propiedades calculadas deberán:

- marcarse como derivadas;
- conservar método;
- conservar fecha;
- poder recalcularse.

---

# Relación

Una relación conecta dos o más entidades mediante un significado explícito.

En su forma binaria básica:

```text
sujeto
predicado
objeto
```

Ejemplo:

```text
REC-0009
usa_ingrediente
ING-0008
```

---

# Elementos de una relación

Toda relación deberá poder expresar:

- sujeto;
- predicado;
- objeto;
- dirección;
- procedencia;
- estado;
- confianza;
- contexto;
- temporalidad.

---

# Predicado

El predicado representa el significado de la conexión.

Ejemplos:

```text
usa_ingrediente
aplica_tecnica
requiere_utensilio
deriva_de
sustituye_a
pertenece_a_cocina
originario_de
documentado_en
```

---

# Dirección

Las relaciones deberán tener una dirección semántica clara.

Ejemplo:

```text
Receta usa_ingrediente Ingrediente
```

La relación inversa podrá definirse como:

```text
Ingrediente es_usado_por Receta
```

No será obligatorio materializar ambas direcciones si el motor puede inferir la inversa.

---

# Relaciones simétricas

Una relación simétrica puede recorrerse en ambas direcciones con el mismo significado.

Ejemplo potencial:

```text
combina_bien_con
```

Si:

```text
A combina_bien_con B
```

entonces:

```text
B combina_bien_con A
```

cuando la propiedad esté declarada como simétrica.

---

# Relaciones asimétricas

Una relación asimétrica no puede ser simultáneamente válida en ambas direcciones.

Ejemplo:

```text
es_subcoleccion_de
```

---

# Relaciones transitivas

Una relación transitiva permite derivar conexiones indirectas.

Ejemplo:

```text
A deriva_de B
B deriva_de C
```

podría permitir:

```text
A deriva_de C
```

si la propiedad se declara transitiva y el dominio lo justifica.

---

# Relaciones funcionales

Una propiedad funcional admite como máximo un valor por sujeto dentro de un contexto.

Ejemplo potencial:

```text
tiene_identificador_canonico
```

---

# Relaciones inversamente funcionales

Una propiedad inversamente funcional identifica de forma única al sujeto a partir del objeto.

Su uso deberá ser restrictivo.

---

# Relaciones reflexivas

Una relación reflexiva permite que una entidad se relacione consigo misma.

Su uso será excepcional en el dominio culinario.

---

# Relaciones irreflexivas

Una relación irreflexiva prohíbe:

```text
A relación A
```

Ejemplo:

```text
es_subcoleccion_de
```

---

# Cardinalidad

Las relaciones podrán establecer restricciones de cardinalidad.

Ejemplos:

```text
Una receta debe tener al menos un ingrediente.
```

```text
Un documento debe poseer exactamente un identificador canónico.
```

---

# Dominio y rango

Toda propiedad semántica deberá declarar:

- dominio;
- rango.

Ejemplo:

```text
usa_ingrediente
domain: Receta
range: Ingrediente
```

---

# Relación válida

Una relación será válida cuando:

- sujeto y objeto existan;
- el predicado exista;
- dominio y rango sean compatibles;
- las restricciones se cumplan;
- su procedencia sea resoluble;
- no esté invalidada.

---

# Relaciones binarias

Son relaciones entre dos entidades.

Ejemplo:

```text
Receta aplica_tecnica Técnica
```

---

# Relaciones n-arias

Algunos hechos no pueden representarse correctamente mediante una única arista binaria.

Ejemplo:

```text
Una receta utiliza 200 gramos de harina en la masa.
```

Este hecho contiene:

- receta;
- ingrediente;
- cantidad;
- unidad;
- componente;
- función.

---

## Nodo de relación

Las relaciones n-arias deberán modelarse mediante una entidad intermedia.

Ejemplo:

```text
REC-0001
        │
        ▼
USO-ING-0001
        │
        ├── ingrediente → Harina
        ├── cantidad → 200
        ├── unidad → Gramo
        ├── componente → Masa
        └── función → Estructura
```

---

# Patrón de participación

Podrá utilizarse una entidad de participación.

Ejemplos:

- uso de ingrediente;
- aplicación de técnica;
- sustitución contextual;
- paso de elaboración;
- medición;
- evaluación.

---

# Uso de ingrediente

Modelo conceptual:

```text
UsoIngrediente
    │
    ├── pertenece_a_receta
    ├── usa_ingrediente
    ├── tiene_cantidad
    ├── usa_unidad
    ├── tiene_funcion
    ├── aplica_en_componente
    └── admite_sustitucion
```

---

# Aplicación de técnica

Una técnica podrá aplicarse con parámetros específicos.

```text
AplicacionTecnica
    │
    ├── receta
    ├── tecnica
    ├── temperatura
    ├── duracion
    ├── intensidad
    ├── equipamiento
    └── resultado_esperado
```

---

# Sustitución

La relación de sustitución suele ser contextual.

No debería modelarse únicamente como:

```text
A sustituye_a B
```

Deberá poder representar:

- receta;
- finalidad;
- proporción;
- restricciones;
- impacto;
- confianza.

---

## Sustitución contextual

```text
Sustitucion
    │
    ├── original
    ├── sustituto
    ├── contexto
    ├── proporcion
    ├── impacto_sabor
    ├── impacto_textura
    └── evidencia
```

---

# Afirmación

Una afirmación representa un hecho declarado dentro del Knowledge Graph.

Ejemplo:

```text
REC-0009 usa_ingrediente ING-0008
```

Toda afirmación deberá poder tratarse como una unidad auditable.

---

# Identidad de afirmación

Las afirmaciones simples podrán no requerir identificador visible.

Sin embargo, cuando posean:

- contexto;
- confianza;
- temporalidad;
- evidencia;
- conflicto;
- múltiples fuentes;

deberán disponer de identidad propia.

Formato recomendado:

```text
STM-XXXXXX
```

---

# Estado de afirmación

Valores posibles:

```text
propuesta
aceptada
confirmada
inferida
disputada
rechazada
obsoleta
```

---

# Tipo de afirmación

Podrá distinguirse entre:

- hecho explícito;
- afirmación importada;
- afirmación experta;
- observación;
- hipótesis;
- inferencia;
- estimación;
- recomendación.

---

# Hecho explícito

Está directamente expresado por una fuente.

---

# Inferencia

Se obtiene mediante razonamiento.

---

# Hipótesis

Representa conocimiento provisional no confirmado.

---

# Observación

Representa un hecho registrado empíricamente.

---

# Recomendación

Representa una sugerencia contextual, no una verdad universal.

Ejemplo:

```text
Miso combina_bien_con berenjena
```

podrá considerarse una recomendación culinaria respaldada por fuentes, no un axioma absoluto.

---

# Reificación

La reificación permite convertir una afirmación en una entidad sobre la que pueden declararse propiedades.

Ejemplo:

```text
STM-000123
    │
    ├── sujeto → REC-0009
    ├── predicado → usa_ingrediente
    ├── objeto → ING-0008
    ├── fuente → DOC-0041
    ├── confianza → 0.98
    └── estado → confirmada
```

---

# Cuándo reificar

Una relación deberá reificarse cuando necesite:

- cantidad;
- unidad;
- procedencia múltiple;
- temporalidad;
- contexto;
- confianza;
- evidencia;
- atributos propios;
- participación de más de dos entidades.

---

# Cuándo no reificar

No deberán convertirse todas las relaciones en nodos si ello:

- complica innecesariamente el modelo;
- reduce la legibilidad;
- no aporta propiedades adicionales;
- perjudica el rendimiento sin beneficio semántico.

---

# RDF-star

Cuando se utilice RDF, RDF-star podrá representar metadatos sobre triples.

Ejemplo conceptual:

```turtle
<< :REC-0009 :usaIngrediente :ING-0008 >>
    :confidence 0.98 ;
    :source :DOC-0041 .
```

---

# Relación enriquecida en LPG

En grafos de propiedades, los metadatos podrán residir sobre la arista.

Ejemplo conceptual:

```text
(:Recipe)-[
    :USES_INGREDIENT {
        confidence: 0.98,
        source: "DOC-0041"
    }
]->(:Ingredient)
```

---

# Compatibilidad entre modelos

El modelo conceptual deberá poder expresarse mediante:

- triples RDF;
- RDF-star;
- grafos nombrados;
- nodos de afirmación;
- aristas con propiedades.

La elección técnica no deberá alterar el significado.

---

# Contexto

El contexto describe las circunstancias que delimitan el significado o la validez de una afirmación.

Una afirmación podrá depender de:

- contexto geográfico;
- contexto temporal;
- contexto cultural;
- contexto culinario;
- contexto tecnológico;
- contexto dietético;
- contexto documental;
- contexto personal.

---

# Contexto geográfico

Ejemplo:

```text
En Andalucía,
el gazpacho se consume tradicionalmente frío.
```

La región forma parte del contexto.

---

# Contexto temporal

Ejemplo:

```text
Durante el periodo Edo,
determinada preparación se documentaba de una forma concreta.
```

---

# Contexto cultural

Ejemplo:

```text
En la tradición japonesa,
el miso puede formar parte del desayuno.
```

---

# Contexto culinario

Ejemplos:

- cocina doméstica;
- restauración;
- pastelería;
- conservación;
- producción industrial.

---

# Contexto tecnológico

Ejemplo:

```text
En cocción sous-vide,
la temperatura recomendada es...
```

---

# Contexto dietético

Ejemplos:

- vegano;
- vegetariano;
- sin gluten;
- bajo en sodio.

---

# Contexto de usuario

Las preferencias personales deberán mantenerse separadas del conocimiento general.

Ejemplo:

```text
Usuario X prefiere poco picante.
```

No deberá transformarse en:

```text
La receta debe ser poco picante.
```

---

# Nodo de contexto

Los contextos complejos podrán modelarse como nodos.

```text
CTX-0001
    │
    ├── region → Kansai
    ├── periodo → Contemporáneo
    ├── entorno → Doméstico
    └── perfil → Tradicional
```

---

# Afirmación contextualizada

```text
STM-0001
    │
    ├── sujeto → Preparación X
    ├── predicado → se_consume_en
    ├── objeto → Desayuno
    └── contexto → CTX-0001
```

---

# Herencia de contexto

Un contexto documental podrá heredarse por sus afirmaciones cuando:

- esté declarado explícitamente;
- no exista un contexto más específico;
- la política de importación lo permita.

La herencia deberá ser trazable.

---

# Conflictos contextuales

Dos afirmaciones aparentemente contradictorias pueden ser compatibles en contextos diferentes.

Ejemplo:

```text
La preparación se sirve caliente.
```

y:

```text
La preparación se sirve fría.
```

Podrán coexistir si corresponden a:

- regiones distintas;
- variantes distintas;
- épocas distintas;
- perfiles distintos.

---

# Procedencia

La procedencia permite responder:

- de dónde procede una afirmación;
- quién la creó;
- qué proceso la generó;
- qué fuente la respalda;
- cuándo fue registrada.

---

# Elementos de procedencia

Podrán representarse:

- entidad;
- actividad;
- agente;
- fuente;
- evidencia;
- fecha;
- método;
- licencia.

---

# Modelo PROV

El SGCC podrá alinearse con PROV-O.

Elementos principales:

```text
Entity
Activity
Agent
```

Relaciones posibles:

```text
wasGeneratedBy
wasAttributedTo
used
wasDerivedFrom
wasAssociatedWith
```

---

# Fuente primaria

Una fuente primaria proporciona evidencia directa.

Ejemplos:

- receta original;
- observación;
- documento histórico;
- registro experimental.

---

# Fuente secundaria

Interpreta o sintetiza fuentes primarias.

Ejemplos:

- manual;
- artículo;
- enciclopedia;
- revisión.

---

# Fuente interna

Procede del propio SGCC.

---

# Fuente externa

Procede de sistemas o publicaciones ajenas.

---

# Cadena de procedencia

Una afirmación podrá derivarse a través de varias etapas.

```text
Libro
  ↓
Documento SGCC
  ↓
Extracción estructurada
  ↓
Afirmación
  ↓
Inferencia
```

Cada etapa deberá conservarse.

---

# Evidencia

La evidencia respalda una afirmación.

Podrá consistir en:

- texto;
- tabla;
- imagen;
- observación;
- referencia bibliográfica;
- resultado experimental;
- consenso experto;
- regla ontológica.

---

# Fragmento de evidencia

Cuando la fuente sea un documento extenso, deberá poder indicarse:

- sección;
- párrafo;
- página;
- componente;
- selector.

---

# Múltiples evidencias

Una afirmación podrá estar respaldada por varias fuentes.

Esto deberá mejorar:

- confianza;
- trazabilidad;
- capacidad de revisión.

No deberá generar duplicación del hecho.

---

# Confianza

La confianza expresa el grado de seguridad atribuido a una afirmación.

Rango recomendado:

```text
0.0 ≤ confianza ≤ 1.0
```

---

## Confianza de fuente

Evalúa la fiabilidad de la fuente.

---

## Confianza de extracción

Evalúa la seguridad del proceso que obtuvo la afirmación.

---

## Confianza semántica

Evalúa la seguridad de la interpretación.

---

## Confianza inferida

Evalúa la certeza de una conclusión derivada.

---

## Confianza combinada

Podrá calcularse mediante una política explícita.

No deberá asumirse que varias fuentes aumentan automáticamente la confianza hasta 1.0.

---

# Niveles cualitativos

Podrán utilizarse:

```text
muy_baja
baja
media
alta
muy_alta
confirmada
```

---

# Calidad de la afirmación

La calidad podrá considerar:

- confianza;
- procedencia;
- actualidad;
- consistencia;
- completitud;
- revisión.

---

# Autoridad

Una afirmación podrá disponer de nivel de autoridad.

Ejemplos:

```text
normativa
editorial
experta
documental
automatica
experimental
```

La autoridad no será equivalente a la confianza.

---

# Temporalidad

El Knowledge Graph deberá poder representar el tiempo de varias formas.

---

# Tiempo de validez

Indica cuándo una afirmación es válida en el mundo representado.

Ejemplo:

```text
valid_from
valid_until
```

---

# Tiempo de transacción

Indica cuándo la afirmación fue incorporada o modificada en el SGCC.

---

# Tiempo de observación

Indica cuándo se observó el hecho.

---

# Tiempo de publicación

Indica cuándo se publicó la fuente.

---

# Temporalidad de entidad

Una entidad podrá:

- aparecer;
- cambiar;
- quedar obsoleta;
- desaparecer.

---

# Temporalidad de relación

Una relación podrá ser válida solo durante un intervalo.

Ejemplo:

```text
Chef X trabaja_en Restaurante Y
desde 2024
hasta 2026
```

---

# Temporalidad culinaria

Podrá utilizarse para representar:

- estacionalidad;
- evolución histórica;
- periodos culturales;
- disponibilidad;
- maduración;
- fermentación;
- conservación.

---

# Intervalos

Los intervalos deberán poder expresar:

- inicio conocido;
- final conocido;
- inicio abierto;
- final abierto;
- precisión aproximada.

---

# Tiempo incierto

Ejemplo:

```text
principios del siglo XIX
```

No deberá forzarse una fecha exacta falsa.

Podrá representarse:

- rango;
- precisión;
- estimación;
- confianza.

---

# Bitemporalidad

Cuando resulte necesario, el grafo podrá conservar simultáneamente:

- tiempo de validez;
- tiempo de registro.

Esto permite reconstruir qué sabía el sistema en un momento determinado.

---

# Estado

Toda entidad y afirmación podrá tener estado.

Valores generales recomendados:

```text
propuesta
activa
confirmada
en_revision
disputada
deprecada
obsoleta
archivada
eliminada_logicamente
```

---

# Eliminación lógica

Los elementos referenciados no deberán eliminarse físicamente de forma inmediata.

Se recomienda:

- marcar estado;
- conservar identidad;
- registrar sustitución;
- preservar procedencia.

---

# Deprecación

Un elemento deprecado deberá indicar:

- motivo;
- fecha;
- sustituto;
- periodo de transición.

---

# Equivalencia

Dos nodos podrán identificarse como equivalentes cuando representan la misma entidad conceptual.

Relaciones posibles:

```text
same_as
exact_match
close_match
```

---

# Equivalencia exacta

Implica identidad semántica.

Deberá utilizarse con cautela.

---

# Correspondencia cercana

Indica alta similitud sin identidad completa.

---

# Fusión de entidades

Cuando se detecten duplicados, deberá aplicarse un proceso formal.

```text
Detección
↓
Comparación
↓
Revisión
↓
Elección de entidad canónica
↓
Redirección de relaciones
↓
Registro de equivalencia
↓
Deprecación del duplicado
```

---

# Entidad canónica

La entidad canónica será la referencia oficial.

Las entidades fusionadas conservarán:

- identificador histórico;
- alias;
- procedencia;
- enlace hacia la entidad canónica.

---

# Desambiguación

Dos entidades con el mismo nombre no deberán fusionarse automáticamente.

Ejemplo:

```text
Curry
```

puede representar:

- mezcla de especias;
- plato;
- hoja;
- tradición culinaria.

---

# Claves de desambiguación

Podrán utilizarse:

- tipo;
- contexto;
- región;
- relaciones;
- fuente;
- descripción;
- identificadores externos.

---

# Identificadores externos

Una entidad podrá vincularse con identificadores externos.

Ejemplos:

- Wikidata;
- DBpedia;
- FoodOn;
- GeoNames;
- identificadores bibliográficos.

---

# Mapeo externo

El mapeo deberá indicar:

- sistema;
- identificador;
- tipo de equivalencia;
- fecha;
- confianza;
- responsable.

---

# Fronteras del grafo

El Knowledge Graph no necesita incorporar todo el contenido de fuentes externas.

Podrá representar enlaces hacia ellas.

---

## Entidad interna completa

Gestionada directamente por el SGCC.

---

## Entidad externa referenciada

Representada mínimamente para conectar conocimiento.

---

## Entidad importada

Copiada conforme a licencia y política de procedencia.

---

# Subgrafos

Un subgrafo representa un subconjunto coherente del Knowledge Graph.

Podrá definirse por:

- dominio;
- módulo;
- colección;
- fuente;
- versión;
- permisos;
- contexto;
- aplicación.

---

# Subgrafo ontológico

Contiene clases y propiedades.

---

# Subgrafo de dominio

Ejemplo:

```text
Ingredientes
```

---

# Subgrafo documental

Contiene documentos, componentes y relaciones de procedencia.

---

# Subgrafo de colección

Representa la proyección semántica de una colección.

---

# Subgrafo de procedencia

Contiene fuentes, agentes y actividades.

---

# Subgrafo temporal

Representa el conocimiento válido en un periodo.

---

# Subgrafo personal

Contiene información específica de un usuario.

Deberá separarse del conocimiento global y respetar permisos.

---

# Subgrafo inferido

Contiene afirmaciones derivadas.

Deberá distinguirse del grafo explícito.

---

# Grafos nombrados

Los grafos nombrados permitirán identificar subconjuntos.

Ejemplos:

```text
Grafo ontológico
Grafo documental
Grafo inferido
Grafo de colección
Grafo de usuario
```

---

# Membresía en subgrafos

Una entidad podrá pertenecer simultáneamente a varios subgrafos.

Esto no duplicará la entidad.

---

# Frontera de subgrafo

Todo subgrafo deberá declarar:

- qué nodos contiene;
- qué relaciones contiene;
- qué relaciones externas conserva;
- qué profundidad admite;
- qué contexto utiliza.

---

# Subgrafo cerrado

Solo contiene nodos y relaciones internas.

---

# Subgrafo abierto

Puede conservar relaciones hacia entidades externas.

---

# Subgrafo contextual

Incluye entidades auxiliares necesarias para interpretar los miembros principales.

---

# Capas de afirmaciones

El Knowledge Graph deberá distinguir al menos:

```text
Grafo explícito
Grafo validado
Grafo inferido
Grafo hipotético
```

---

# Grafo explícito

Contiene afirmaciones obtenidas directamente de fuentes.

---

# Grafo validado

Contiene afirmaciones explícitas que han superado revisión.

---

# Grafo inferido

Contiene conclusiones derivadas.

---

# Grafo hipotético

Contiene propuestas o escenarios no confirmados.

---

# Separación de capas

Las aplicaciones deberán poder decidir qué capas consultar.

Ejemplo:

```yaml
include_layers:
  - explicit
  - validated
  - inferred
```

---

# Afirmaciones contradictorias

El grafo podrá contener afirmaciones incompatibles cuando:

- procedan de fuentes diferentes;
- exista controversia;
- correspondan a contextos distintos;
- no se haya resuelto la revisión.

No deberán sobrescribirse silenciosamente.

---

# Conflicto

Un conflicto deberá representarse como entidad o estado formal.

Podrá incluir:

- afirmaciones implicadas;
- tipo de contradicción;
- fuentes;
- contexto;
- responsable;
- estado de resolución.

---

# Tipos de conflicto

Ejemplos:

- valor incompatible;
- clasificación incompatible;
- temporalidad incompatible;
- identidad dudosa;
- fuente contradictoria;
- regla violada.

---

# Resolución de conflictos

Políticas posibles:

```text
authority_wins
latest_valid_source
highest_confidence
context_separation
manual_review
preserve_all
```

La política deberá depender del tipo de conocimiento.

---

# Ausencia de conocimiento

El grafo deberá distinguir entre:

- falso;
- desconocido;
- no documentado;
- no aplicable;
- pendiente de revisión.

---

# Mundo abierto

El modelo semántico general utilizará el supuesto de mundo abierto.

La ausencia de una afirmación no implicará que sea falsa.

---

# Mundo cerrado contextual

Algunas operaciones podrán usar mundo cerrado dentro de un contexto controlado.

Ejemplo:

```text
Inventario actual de despensa
```

Si un ingrediente no aparece en el inventario validado, podrá considerarse no disponible para esa consulta.

---

# Negación

La negación deberá modelarse explícitamente.

Ejemplo:

```text
La receta no contiene gluten.
```

No deberá inferirse solo por ausencia de ingredientes con gluten salvo que exista una regla válida y el conjunto esté completo.

---

# Negación fuerte

Afirma explícitamente que un hecho es falso.

---

# Negación por fallo

Asume falsedad ante ausencia.

Solo deberá aplicarse en dominios cerrados.

---

# Restricciones

Las restricciones definen condiciones que el grafo deberá cumplir.

Ejemplos:

- cardinalidad;
- tipos válidos;
- valores permitidos;
- relaciones obligatorias;
- ausencia de ciclos;
- unidades compatibles.

---

# Restricciones estructurales

Comprueban la forma del grafo.

---

# Restricciones semánticas

Comprueban el significado.

---

# Restricciones contextuales

Comprueban reglas dentro de un contexto.

---

# Restricciones operativas

Comprueban requisitos para aplicaciones.

---

# SHACL

Cuando se utilice RDF, SHACL podrá validar la estructura de los nodos.

Ejemplo conceptual:

```text
RecipeShape
    targetClass Recipe
    requires:
        title
        at_least_one_ingredient
        at_least_one_step
```

---

# Reglas de integridad

Ejemplos:

```text
Toda receta debe tener título.
```

```text
Toda relación usa_ingrediente debe conectar una receta con un ingrediente.
```

```text
Ninguna colección puede ser subcolección de sí misma.
```

---

# Restricciones de ciclos

Algunas relaciones podrán formar ciclos.

Ejemplo:

```text
combina_bien_con
```

Otras no deberán formarlos.

Ejemplo:

```text
subclase_de
```

cuando se exija jerarquía estricta.

---

# Orden y secuencia

Algunos conocimientos requieren orden.

Ejemplos:

- pasos de receta;
- fases de fermentación;
- secuencia de servicio;
- orden pedagógico.

---

# Modelado de secuencias

Una secuencia podrá representarse mediante:

- posición;
- relación `precede`;
- lista ordenada;
- nodo de secuencia.

---

## Paso de receta

```text
Paso
    │
    ├── pertenece_a_receta
    ├── posicion
    ├── instruccion
    ├── aplica_tecnica
    ├── usa_ingrediente
    └── precede_a
```

---

# Jerarquías

El grafo podrá representar múltiples jerarquías.

Ejemplos:

- taxonomía de ingredientes;
- jerarquía geográfica;
- clasificación técnica;
- estructura documental;
- subcolecciones.

---

# Polijerarquía

Una entidad podrá tener más de un padre conceptual.

Ejemplo:

```text
Tomate
subclase_de
Fruto
```

y, desde una clasificación culinaria:

```text
Tomate
subclase_de
HortalizaCulinaria
```

Los contextos deberán evitar ambigüedades.

---

# Facetas

Las facetas permiten clasificar una entidad desde perspectivas distintas.

Ejemplos:

- origen;
- función;
- técnica;
- textura;
- nutrición;
- estacionalidad.

---

# Modelado de variantes

Una receta o preparación podrá poseer variantes.

Relaciones posibles:

```text
variante_de
adapta
deriva_de
version_regional_de
version_dietetica_de
```

---

# Identidad de variante

Una variante deberá tener identidad propia cuando:

- posea ingredientes distintos relevantes;
- modifique técnica;
- tenga contexto cultural propio;
- necesite documentación independiente.

---

# Parámetros variables

Los cambios meramente paramétricos no siempre deberán generar una nueva entidad.

Ejemplos:

- número de comensales;
- escala de cantidades;
- idioma de presentación.

---

# Modelado de recetas

Una receta podrá relacionarse con:

- ingredientes;
- cantidades;
- técnicas;
- pasos;
- utensilios;
- tiempos;
- temperaturas;
- preparaciones;
- variantes;
- culturas;
- fuentes;
- restricciones dietéticas.

---

# Modelo resumido de receta

```text
Receta
   │
   ├── tiene_titulo
   ├── usa_ingrediente
   ├── contiene_paso
   ├── aplica_tecnica
   ├── requiere_utensilio
   ├── produce_preparacion
   ├── pertenece_a_cocina
   ├── tiene_variante
   ├── documentada_en
   └── cumple_perfil
```

---

# Modelado de ingredientes

Un ingrediente podrá relacionarse con:

- categoría;
- origen;
- composición;
- función;
- disponibilidad;
- sustitutos;
- alérgenos;
- técnicas;
- recetas;
- productos derivados.

---

# Modelo resumido de ingrediente

```text
Ingrediente
    │
    ├── pertenece_a_familia
    ├── originario_de
    ├── tiene_alergeno
    ├── aporta_funcion
    ├── sustituible_por
    ├── usado_en
    ├── procesado_mediante
    └── disponible_en_temporada
```

---

# Modelado de técnicas

Una técnica podrá relacionarse con:

- ingredientes;
- transformaciones;
- temperatura;
- tiempo;
- equipamiento;
- riesgos;
- resultados;
- técnicas relacionadas.

---

# Modelo resumido de técnica

```text
Tecnica
   │
   ├── transforma
   ├── requiere_equipo
   ├── usa_temperatura
   ├── tiene_duracion
   ├── produce_efecto
   ├── presenta_riesgo
   └── relacionada_con
```

---

# Modelado de documentos

Un documento podrá:

- describir entidades;
- contener componentes;
- respaldar afirmaciones;
- derivar de fuentes;
- pertenecer a versiones;
- formar parte de colecciones.

---

# Modelo resumido de documento

```text
Documento
    │
    ├── describe
    ├── contiene
    ├── cita
    ├── deriva_de
    ├── respalda
    ├── tiene_version
    ├── pertenece_a_coleccion
    └── creado_por
```

---

# Componentes documentales

Una sección o componente deberá conservar:

- documento padre;
- posición;
- tipo;
- contenido;
- versión;
- identidad cuando sea reutilizable.

---

# Conocimiento y documento

El grafo deberá distinguir entre:

```text
Documento afirma X
```

y:

```text
X es aceptado por el SGCC
```

Una afirmación documental no se convertirá automáticamente en conocimiento validado.

---

# Flujo de incorporación

```text
Fuente
   ↓
Documento
   ↓
Extracción
   ↓
Afirmación propuesta
   ↓
Validación
   ↓
Afirmación aceptada
   ↓
Knowledge Graph validado
```

---

# Entidades derivadas

Una entidad podrá generarse a partir de:

- extracción;
- normalización;
- fusión;
- inferencia;
- cálculo;
- agregación.

Deberá conservarse su proceso de creación.

---

# Agregaciones

Algunos nodos podrán representar agregaciones.

Ejemplos:

- perfil nutricional;
- resumen de colección;
- métrica;
- distribución.

Estas entidades deberán marcarse como derivadas.

---

# Identidad de agregación

La identidad deberá incorporar:

- fuente;
- método;
- versión;
- parámetros;
- instante de cálculo.

---

# Inferencias

Aunque el razonador se especificará en un documento independiente, el modelo del grafo deberá preparar su representación.

---

# Afirmación inferida

Deberá incluir:

- conclusión;
- regla;
- premisas;
- motor;
- versión;
- fecha;
- confianza;
- explicación.

---

# Dependencia de inferencia

Si una premisa queda invalidada, las inferencias dependientes deberán revisarse o invalidarse.

---

# Grafo de justificación

Una inferencia podrá representarse mediante:

```text
Conclusión
    │
    ▼
Aplicación de regla
    │
    ├── Premisa 1
    ├── Premisa 2
    └── Premisa 3
```

---

# Observaciones probabilísticas

Los resultados de modelos estadísticos no deberán tratarse automáticamente como hechos.

Deberán representarse como:

- predicción;
- clasificación;
- similitud;
- recomendación;
- probabilidad.

---

# Predicción

Ejemplo:

```text
Modelo X predice que REC-0044 pertenece a CocinaJaponesa con 0.82.
```

No equivale a:

```text
REC-0044 pertenece definitivamente a CocinaJaponesa.
```

---

# Similitud

La similitud podrá representarse con:

- método;
- puntuación;
- modelo;
- versión;
- corpus.

---

# Embeddings

Los embeddings no forman parte del significado canónico del grafo.

Podrán vincularse como artefactos derivados.

---

# Metadatos de embedding

Ejemplos:

- modelo;
- versión;
- dimensión;
- fecha;
- vector store;
- hash de contenido.

---

# Colecciones en el grafo

Las colecciones podrán representarse como entidades organizativas.

```text
COL-0001
instanceOf
KnowledgeCollection
```

---

# Relación de pertenencia

```text
Entidad
miembro_de
Colección
```

La pertenencia podrá ser:

- explícita;
- calculada;
- inferida;
- temporal;
- contextual.

---

# Definición y resultado

Deberán distinguirse:

```text
Definición de colección
```

y:

```text
Snapshot de miembros
```

---

# Snapshot de colección

Un snapshot podrá representarse como entidad:

```text
COL-SNAP-0001
    │
    ├── snapshot_de → COL-0001
    ├── version_coleccion → 2.0.0
    ├── version_grafo → 1.4.0
    ├── generado_en → fecha
    └── contiene_miembro → entidad
```

---

# Versionado conceptual

El versionado completo se desarrollará posteriormente, pero el modelo deberá diferenciar:

- identidad estable;
- estado actual;
- versión;
- revisión;
- snapshot.

---

# Versión de entidad

Una entidad podrá mantener la misma identidad y evolucionar mediante versiones.

---

# Versión de afirmación

Una afirmación podrá:

- modificarse;
- ser sustituida;
- quedar deprecada;
- conservar historial.

---

# Relación de sustitución

```text
afirmacion_nueva
sustituye_a
afirmacion_anterior
```

---

# Snapshot del grafo

Un snapshot representa el estado completo o parcial del grafo en un momento.

Deberá registrar:

- versión;
- fecha;
- fuentes;
- reglas;
- hash;
- cobertura;
- estado.

---

# Identidad de snapshot

Formato recomendado:

```text
KG-SNAP-YYYYMMDD-NNN
```

Ejemplo:

```text
KG-SNAP-20260731-001
```

---

# Modularización

El Knowledge Graph podrá dividirse en módulos lógicos.

Ejemplos:

```text
KG-INGREDIENTS
KG-RECIPES
KG-TECHNIQUES
KG-EQUIPMENT
KG-CULTURES
KG-DOCUMENTS
KG-PROVENANCE
```

---

# Dependencias entre módulos

Un módulo podrá depender de otros.

Ejemplo:

```text
KG-RECIPES
depende_de
KG-INGREDIENTS
```

---

# Fronteras modulares

Los módulos no deberán duplicar entidades compartidas.

Una entidad común deberá conservar identidad única.

---

# Núcleo compartido

El grafo podrá disponer de un núcleo con conceptos transversales:

- identidad;
- agente;
- documento;
- lugar;
- tiempo;
- unidad;
- medida;
- procedencia.

---

# Vocabularios controlados

Los valores repetidos deberán normalizarse mediante vocabularios.

Ejemplos:

- estados;
- unidades;
- tipos de fuente;
- roles;
- niveles de confianza;
- técnicas;
- dietas.

---

# Término controlado

Todo término deberá poseer:

- identificador;
- etiqueta;
- definición;
- estado;
- vocabulario;
- procedencia.

---

# Extensibilidad

El modelo deberá permitir incorporar nuevos dominios sin modificar su núcleo.

Ejemplos futuros:

- microbiología;
- sostenibilidad;
- costes;
- logística;
- historia;
- sensorialidad.

---

# Perfil mínimo de nodo

Todo nodo deberá incluir al menos:

```yaml
id:
type:
label:
status:
provenance:
```

---

# Ejemplo mínimo de nodo

```yaml
id: ING-0008
type: Ingredient
label:
  es: Miso
status: active

provenance:
  source: DOC-0041
```

---

# Perfil ampliado de nodo

```yaml
id: ING-0008
uri: https://novacoquinaria.org/entity/ING-0008

types:
  - Ingredient
  - FermentedIngredient
  - SoyProduct
  - Condiment

preferred_label:
  es: Miso
  en: Miso
  ja: 味噌

aliases:
  - Pasta de miso

description:
  es: >
    Condimento fermentado elaborado habitualmente a partir de soja,
    cereal, sal y kōji.

status: active
version: 1.2.0

external_identifiers:
  - system: wikidata
    value: Q131419

provenance:
  created_from:
    - DOC-0041
  created_at: 2026-07-31
```

---

# Perfil mínimo de relación

```yaml
subject:
predicate:
object:
source:
status:
```

---

# Ejemplo simple de relación

```yaml
subject: REC-0009
predicate: uses_ingredient
object: ING-0008

status: confirmed
source: DOC-0051
```

---

# Ejemplo de relación enriquecida

```yaml
id: STM-000123

subject: REC-0009
predicate: uses_ingredient
object: ING-0008

status: confirmed
confidence: 0.98

context:
  component: broth

provenance:
  source: DOC-0051
  fragment: ingredients
  extraction_method: manual
  reviewed_by: culinary_editor

validity:
  valid_from: 2026-07-31
```

---

# Ejemplo de relación n-aria

```yaml
id: USE-ING-000045
type: IngredientUsage

recipe: REC-0009
ingredient: ING-0008
component: PREP-0012

quantity:
  value: 30
  unit: gram

role: seasoning
optional: false

provenance:
  source: DOC-0051
```

---

# Ejemplo de afirmación contextual

```yaml
id: STM-000201

subject: PREP-0081
predicate: served_during
object: BREAKFAST

context:
  geographic:
    - Japan

  cultural:
    - traditional

  temporal:
    period: contemporary

status: accepted
confidence: 0.88

evidence:
  - DOC-0088
  - DOC-0090
```

---

# Ejemplo de inferencia

```yaml
id: INF-000041
type: InferredStatement

conclusion:
  subject: REC-0009
  predicate: suitable_for
  object: VEGETARIAN_DIET

rule: RULE-DIET-0014

premises:
  - STM-000123
  - STM-000124
  - STM-000125

engine:
  id: SGCC-REASONER
  version: 1.0.0

confidence: 0.94
generated_at: 2026-07-31
```

---

# Esquema conceptual resumido

```text
KnowledgeGraph
    │
    ├── contieneNodo
    ├── contieneRelacion
    ├── contieneAfirmacion
    ├── aplicaOntologia
    ├── organizaSubgrafo
    ├── conservaContexto
    ├── conservaProcedencia
    ├── mantieneTemporalidad
    ├── distingueCapas
    ├── conservaVersion
    └── permiteInferencia
```

---

# Reglas mínimas de consistencia

---

## Identidad única

No podrán existir dos entidades activas con el mismo identificador canónico.

---

## Tipo obligatorio

Todo nodo deberá tener al menos un tipo.

---

## Etiqueta obligatoria

Todo nodo deberá tener una etiqueta legible en al menos un idioma.

---

## Predicado válido

Toda relación deberá utilizar un predicado definido.

---

## Sujeto resoluble

Todo sujeto deberá existir.

---

## Objeto válido

El objeto deberá ser:

- una entidad existente;
- o un literal correctamente tipado.

---

## Dominio y rango compatibles

Las relaciones deberán respetar los tipos definidos por la ontología.

---

## Procedencia mínima

Toda afirmación deberá disponer de fuente o actividad generadora.

---

## Confianza válida

La confianza deberá encontrarse en el rango definido.

---

## Temporalidad coherente

La fecha final no podrá ser anterior a la inicial.

---

## No ciclos prohibidos

Las relaciones jerárquicas estrictas no deberán formar ciclos.

---

## No duplicación de hechos

No deberán crearse múltiples afirmaciones idénticas sin diferenciación de:

- fuente;
- contexto;
- temporalidad;
- estado.

---

# Validación estructural

Comprobará:

- identificadores;
- tipos;
- campos obligatorios;
- formatos;
- referencias;
- literales;
- unidades.

---

# Validación ontológica

Comprobará:

- dominio;
- rango;
- cardinalidades;
- incompatibilidades;
- jerarquías;
- axiomas.

---

# Validación contextual

Comprobará:

- coherencia geográfica;
- coherencia temporal;
- perfiles;
- alcance.

---

# Validación de procedencia

Comprobará:

- existencia de fuente;
- fragmentos;
- agentes;
- actividades;
- licencias.

---

# Validación temporal

Comprobará:

- intervalos;
- solapamientos;
- versiones;
- estados históricos.

---

# Antipatrones de modelado

---

## Utilizar el nombre como identidad

Los nombres pueden cambiar o repetirse.

---

## Confundir documento y entidad

Un documento sobre un ingrediente no es el ingrediente.

---

## Crear relaciones genéricas

Deberá evitarse:

```text
relacionado_con
```

cuando exista un significado más preciso.

---

## Utilizar literales donde debería existir una entidad

Ejemplo incorrecto:

```text
originario_de = "Japón"
```

cuando Japón ya es una entidad del grafo.

---

## Crear una entidad para cada valor trivial

No todos los valores necesitan ser nodos.

---

## Reificar todas las relaciones

Produce complejidad innecesaria.

---

## No reificar relaciones complejas

Provoca pérdida de cantidad, contexto o evidencia.

---

## Mezclar hechos e inferencias

Las capas deberán distinguirse.

---

## Sobrescribir contradicciones

Los conflictos deberán conservarse y resolverse formalmente.

---

## Interpretar ausencia como falsedad

El modelo general utiliza mundo abierto.

---

## Usar confianza como verdad

Una puntuación alta no convierte una predicción en un hecho normativo.

---

## Duplicar entidades por colección

Las colecciones deberán reutilizar nodos canónicos.

---

## Incluir contexto en nombres

Ejemplo incorrecto:

```text
MisoTradicionalJaponesContemporaneo
```

El contexto deberá modelarse mediante relaciones y nodos contextuales.

---

## Convertir toda variante en entidad nueva

Solo deberá crearse una nueva identidad cuando exista diferencia conceptual suficiente.

---

## Ignorar temporalidad

Puede producir afirmaciones aparentemente contradictorias.

---

## Importar fuentes sin procedencia

Impide auditoría y actualización.

---

# Perfil inicial de implementación

La primera implementación del Knowledge Graph podrá limitarse a:

- entidades canónicas;
- tipos;
- etiquetas;
- relaciones binarias;
- documentos;
- procedencia básica;
- estados;
- enlaces con colecciones.

---

# Perfil estructurado

Añadirá:

- relaciones n-arias;
- unidades;
- contexto;
- temporalidad;
- validación;
- subgrafos.

---

# Perfil semántico

Añadirá:

- RDF u otro modelo formal;
- axiomas;
- SHACL;
- jerarquías;
- equivalencias;
- inferencias.

---

# Perfil avanzado

Añadirá:

- grafos de justificación;
- probabilidades;
- temporalidad completa;
- resolución de conflictos;
- interoperabilidad externa;
- snapshots reproducibles.

---

# Ejemplo integrado

```yaml
graph:
  id: KG-SGCC
  version: 1.0.0
  status: development

nodes:
  - id: REC-0009
    types:
      - Recipe

    preferred_label:
      es: Sopa de miso

    status: active

  - id: ING-0008
    types:
      - Ingredient
      - FermentedIngredient
      - SoyProduct

    preferred_label:
      es: Miso

    status: active

  - id: TEC-0012
    types:
      - CulinaryTechnique

    preferred_label:
      es: Disolución fuera del hervor

    status: active

statements:
  - id: STM-000123
    subject: REC-0009
    predicate: uses_ingredient
    object: ING-0008

    status: confirmed
    confidence: 0.98

    provenance:
      source: DOC-0051
      fragment: ingredients

  - id: STM-000124
    subject: REC-0009
    predicate: applies_technique
    object: TEC-0012

    status: confirmed
    confidence: 0.95

    provenance:
      source: DOC-0051
      fragment: procedure

contexts:
  - id: CTX-0001

    geographic:
      region: Japan

    cultural:
      profile: traditional

collections:
  - id: COL-0001
    members:
      - REC-0009
      - ING-0008
      - TEC-0012
```

---

# Arquitectura conceptual consolidada

```text
┌──────────────────────────────────────────────┐
│                Ontología SGCC               │
│                                              │
│ Clases · Propiedades · Restricciones · Reglas│
└─────────────────────┬────────────────────────┘
                      │ instancia y valida
                      ▼
┌──────────────────────────────────────────────┐
│              Entidades canónicas             │
│                                              │
│ Recetas · Ingredientes · Técnicas · Lugares  │
└─────────────────────┬────────────────────────┘
                      │ conectadas mediante
                      ▼
┌──────────────────────────────────────────────┐
│           Afirmaciones y relaciones          │
│                                              │
│ Sujeto · Predicado · Objeto · Contexto       │
└─────────────────────┬────────────────────────┘
                      │ respaldadas por
                      ▼
┌──────────────────────────────────────────────┐
│       Procedencia · Evidencia · Tiempo       │
│                                              │
│ Fuentes · Agentes · Actividades · Validez    │
└─────────────────────┬────────────────────────┘
                      │ organizadas como
                      ▼
┌──────────────────────────────────────────────┐
│         Capas · Módulos · Subgrafos          │
│                                              │
│ Explícito · Validado · Inferido · Colecciones│
└──────────────────────────────────────────────┘
```

---

# Conclusión

El modelo formal definido en esta parte establece las unidades fundamentales del Knowledge Graph del SGCC.

El grafo queda compuesto por:

- entidades con identidad estable;
- clases y propiedades definidas ontológicamente;
- relaciones semánticas;
- afirmaciones auditables;
- contextos explícitos;
- procedencia;
- evidencia;
- temporalidad;
- niveles de confianza;
- capas de conocimiento;
- módulos y subgrafos.

Este modelo permite representar no solo hechos simples, sino también conocimiento culinario complejo, contextual, temporal, discutible, derivado y documentado.

La separación entre:

```text
Entidad
Documento
Afirmación
Contexto
Evidencia
Inferencia
```

garantiza que el SGCC pueda evolucionar sin confundir:

- lo que existe;
- lo que una fuente afirma;
- lo que el sistema acepta;
- lo que el razonador deduce;
- lo que todavía permanece como hipótesis.

La Parte III desarrollará la construcción, ingestión, sincronización y mantenimiento del Knowledge Graph, incluyendo:

- fuentes;
- pipelines;
- extracción;
- normalización;
- resolución de entidades;
- deduplicación;
- validación;
- actualización incremental;
- versionado;
- snapshots;
- migraciones;
- control de calidad.

---

# Parte III — Construcción, ingestión y mantenimiento del Knowledge Graph

---

# Introducción

Las dos partes anteriores han definido:

- la naturaleza del Knowledge Graph;
- su papel dentro del SGCC;
- el modelo conceptual;
- el modelo formal;
- las entidades;
- las relaciones;
- las afirmaciones;
- el contexto;
- la procedencia;
- la temporalidad.

Esta tercera parte describe cómo el Knowledge Graph se construye, evoluciona y mantiene.

Mientras las partes anteriores responden a:

> ¿Qué representa el Knowledge Graph?

esta parte responde a:

> ¿Cómo llega ese conocimiento al grafo?

y

> ¿Cómo se mantiene consistente a lo largo del tiempo?

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir el pipeline oficial de construcción;
- establecer el proceso de ingestión;
- regular la extracción de conocimiento;
- normalizar entidades y relaciones;
- resolver identidades;
- gestionar duplicidades;
- validar el conocimiento;
- mantener la consistencia;
- controlar la evolución del grafo;
- gestionar snapshots y versiones;
- garantizar la trazabilidad completa.

---

# Principios de construcción

Todo proceso de construcción deberá respetar los siguientes principios.

---

## Reproducibilidad

La construcción del grafo deberá poder repetirse obteniendo exactamente el mismo resultado cuando:

- las fuentes;
- la ontología;
- las reglas;
- los parámetros

permanezcan invariables.

---

## Incrementalidad

Siempre que sea posible se evitará reconstruir completamente el grafo.

Solo deberán recalcularse los elementos afectados.

---

## Trazabilidad

Todo nodo y toda relación deberán indicar:

- origen;
- proceso;
- fecha;
- responsable;
- versión.

---

## Determinismo

Las mismas entradas deberán producir el mismo resultado.

Los procesos probabilísticos deberán declararse explícitamente.

---

## Modularidad

Cada fase del pipeline deberá poder ejecutarse independientemente.

---

## Idempotencia

Ejecutar varias veces una misma operación no deberá producir duplicados.

---

## Validación continua

La calidad deberá comprobarse durante toda la construcción.

No únicamente al finalizar.

---

# Arquitectura del pipeline

Conceptualmente:

```text
Fuentes
      │
      ▼
Descubrimiento
      │
      ▼
Extracción
      │
      ▼
Normalización
      │
      ▼
Resolución de entidades
      │
      ▼
Construcción de relaciones
      │
      ▼
Validación
      │
      ▼
Enriquecimiento
      │
      ▼
Persistencia
      │
      ▼
Versionado
      │
      ▼
Publicación
```

---

# Pipeline oficial

El SGCC considera oficial el siguiente flujo:

```text
Fuente

↓

Documento

↓

Componentes

↓

Extracción

↓

Entidades

↓

Resolución

↓

Relaciones

↓

Validación

↓

Knowledge Graph

↓

Snapshots

↓

Colecciones

↓

Razonador

↓

RAG

↓

Agentes
```

---

# Fuentes de conocimiento

El Knowledge Graph podrá construirse a partir de múltiples fuentes.

---

## Documentos SGCC

Principal fuente.

Incluye:

- recetas;
- ingredientes;
- técnicas;
- documentación técnica;
- ADR;
- manuales.

---

## Componentes

Los componentes documentales podrán generar entidades reutilizables.

---

## Ontología

La ontología no genera entidades.

Define:

- clases;
- propiedades;
- restricciones.

---

## Colecciones

Las colecciones no generan conocimiento.

Permiten seleccionar partes del grafo.

---

## Bases de datos

Cuando existan.

---

## APIs

Podrán importar:

- ingredientes;
- regiones;
- información nutricional;
- clasificaciones.

---

## Datos CSV

Podrán incorporarse mediante importadores.

---

## JSON

Podrá importarse conocimiento estructurado.

---

## RDF

Podrá integrarse mediante alineamiento semántico.

---

## Wikidata

Podrá utilizarse como fuente externa.

---

## FoodOn

Especialmente relevante para ingredientes y alimentos.

---

## Open Food Facts

Podrá utilizarse para determinados productos.

---

## Expertos

Las incorporaciones manuales deberán conservar autoría.

---

## IA

Los sistemas de IA podrán proponer conocimiento.

Nunca deberán incorporarlo automáticamente como conocimiento confirmado.

---

# Descubrimiento de fuentes

El sistema deberá localizar automáticamente nuevas fuentes.

Ejemplos:

- nuevos documentos;
- nuevas versiones;
- nuevos módulos;
- nuevas importaciones.

---

# Registro de fuentes

Toda fuente deberá registrarse.

Ejemplo:

```yaml
source:
  id: SRC-0042
  type: markdown
  uri: docs/recipes/miso.md

  version: 1.3.0
```

---

# Pipeline de ingestión

Cada fuente seguirá un flujo controlado.

```text
Registrar

↓

Validar

↓

Leer

↓

Extraer

↓

Normalizar

↓

Resolver

↓

Validar

↓

Persistir
```

---

# Registro

La fuente queda identificada.

---

# Lectura

Se obtiene el contenido.

---

# Parsing

El contenido se convierte en una representación estructurada.

---

# Extracción

Se identifican:

- entidades;
- relaciones;
- literales;
- contexto;
- evidencias.

---

# Normalización

Se unifican:

- nombres;
- unidades;
- idiomas;
- formatos.

---

# Resolución

Se identifican entidades ya existentes.

---

# Construcción

Se crean:

- nodos;
- relaciones;
- afirmaciones.

---

# Validación

Se comprueba la consistencia.

---

# Persistencia

El resultado pasa al Knowledge Graph.

---

# Extracción de entidades

Una extracción podrá detectar:

- ingredientes;
- recetas;
- técnicas;
- regiones;
- culturas;
- utensilios;
- documentos.

---

# Extracción de relaciones

Ejemplos:

```text
usa_ingrediente

aplica_tecnica

requiere_utensilio

originario_de

documentado_en
```

---

# Extracción de propiedades

Ejemplos:

- tiempo;
- temperatura;
- dificultad;
- cantidad;
- idioma.

---

# Extracción de contexto

Ejemplos:

- región;
- época;
- cocina;
- perfil dietético.

---

# Extracción de procedencia

Toda afirmación extraída conservará:

- documento;
- sección;
- componente;
- párrafo.

---

# Extracción automática

Podrá utilizar:

- reglas;
- NLP;
- modelos IA;
- patrones.

---

# Extracción manual

Será la más fiable.

---

# Extracción híbrida

Combinará IA y revisión humana.

---

# Normalización

Antes de construir el grafo deberá normalizarse el conocimiento.

---

## Idiomas

Ejemplo:

```text
味噌

↓

Miso
```

---

## Alias

Ejemplo:

```text
Chile

Ají

Guindilla
```

---

## Unidades

Ejemplo:

```text
0,2 kg

↓

200 gramos
```

---

## Fechas

Formato normalizado.

---

## Temperaturas

Un único sistema.

---

## Cantidades

Representación uniforme.

---

## Espacios

Eliminación de diferencias superficiales.

---

## Mayúsculas

Normalización configurable.

---

# Normalización semántica

También deberá unificarse:

- taxonomía;
- categorías;
- tipos;
- estados.

---

# Entity Resolution

Es uno de los procesos más importantes del SGCC.

Su objetivo consiste en determinar si una entidad ya existe.

---

# Problemas habituales

Ejemplos:

```text
Miso

Pasta de miso

味噌
```

¿Tres entidades?

No.

Una misma entidad.

---

# Etapas

```text
Entidad candidata

↓

Normalización

↓

Búsqueda

↓

Comparación

↓

Similitud

↓

Decisión
```

---

# Búsqueda

Se buscarán candidatos mediante:

- nombre;
- alias;
- identificadores;
- relaciones.

---

# Comparación

Se compararán:

- etiquetas;
- tipos;
- contexto;
- relaciones;
- propiedades.

---

# Similitud

Podrá calcularse:

- textual;
- semántica;
- estructural;
- vectorial.

---

# Umbrales

Ejemplo:

```text
> 0.95

Fusionar automáticamente
```

```text
0.80-0.95

Revisión humana
```

```text
<0.80

Nueva entidad
```

---

# Fusión

Si dos entidades representan el mismo concepto:

```text
Entidad A

+

Entidad B

↓

Entidad canónica
```

---

# Duplicados

Los duplicados nunca deberán eliminarse sin conservar trazabilidad.

---

# Historial

Toda fusión conservará:

- identificadores;
- alias;
- fuentes;
- fecha.

---

# Construcción de relaciones

Una vez resueltas las entidades:

se construyen las relaciones.

---

# Relaciones explícitas

Proceden directamente de documentos.

---

# Relaciones derivadas

Se obtienen mediante transformación.

---

# Relaciones inferibles

Quedan preparadas para el razonador.

---

# Relaciones contextuales

Incluyen contexto explícito.

---

# Relaciones temporales

Incluyen validez temporal.

---

# Relaciones documentales

Relacionan entidades con documentación.

---

# Construcción incremental

Solo deberán reconstruirse las relaciones afectadas.

---

# Validación estructural

Comprueba:

- identificadores;
- tipos;
- referencias;
- formatos.

---

# Validación ontológica

Comprueba:

- dominio;
- rango;
- cardinalidad;
- jerarquías.

---

# Validación documental

Comprueba:

- referencias;
- componentes;
- fragmentos.

---

# Validación contextual

Comprueba:

- regiones;
- culturas;
- temporalidad.

---

# Validación de procedencia

Comprueba:

- fuentes;
- evidencias;
- actividades.

---

# Validación semántica

Detecta:

- contradicciones;
- ciclos;
- inconsistencias.

---

# Validación de calidad

Calcula:

- completitud;
- cobertura;
- confianza;
- conectividad.

---

# Enriquecimiento

Una vez validado el conocimiento podrá enriquecerse.

---

## Alias

Añadir variantes.

---

## Traducciones

Añadir etiquetas multilingües.

---

## Relaciones externas

Conectar con otros grafos.

---

## Identificadores externos

Añadir equivalencias.

---

## Clasificaciones

Añadir categorías.

---

## Embeddings

Generar representaciones vectoriales.

---

## Métricas

Actualizar estadísticas.

---

# Persistencia

Tras superar las validaciones el conocimiento pasa al grafo persistente.

---

# Persistencia incremental

Solo modifica elementos afectados.

---

# Persistencia completa

Reconstruye todo el grafo.

Uso excepcional.

---

# Actualización

El grafo deberá admitir:

- actualización manual;
- automática;
- programada;
- por eventos.

---

# Eventos

Ejemplos:

- nuevo documento;
- modificación;
- nueva ontología;
- nueva colección.

---

# Detección de impacto

Antes de actualizar deberá conocerse qué elementos se ven afectados.

---

# Grafo de dependencias

Conceptualmente:

```text
Documento

↓

Entidad

↓

Relación

↓

Colección

↓

Snapshot
```

---

# Invalidación

Una modificación puede invalidar:

- relaciones;
- inferencias;
- colecciones;
- snapshots.

---

# Revalidación

Solo deberán revalidarse los elementos afectados.

---

# Snapshots

El sistema podrá generar snapshots.

---

## Snapshot completo

Todo el grafo.

---

## Snapshot parcial

Un módulo.

---

## Snapshot temporal

Estado histórico.

---

# Versionado

El grafo mantendrá:

- versión;
- revisión;
- snapshot.

---

# Versionado incremental

Permite reconstrucción histórica.

---

# Migraciones

Los cambios estructurales deberán realizarse mediante migraciones.

---

# Calidad

El sistema calculará continuamente:

- entidades;
- relaciones;
- densidad;
- duplicados;
- entidades huérfanas;
- confianza media.

---

# Observabilidad

Toda operación quedará registrada.

---

# Logs

Ejemplos:

- entidad creada;
- relación eliminada;
- conflicto;
- inferencia invalidada.

---

# Auditoría

Toda modificación será trazable.

---

# Automatización

El pipeline podrá integrarse en CI/CD.

---

# Pipeline automático

```text
Commit

↓

Validación

↓

Extracción

↓

Normalización

↓

Entity Resolution

↓

Construcción

↓

Validación

↓

Snapshot

↓

Publicación
```

---

# Recuperación ante errores

Si una actualización falla:

- conservar último snapshot válido;
- registrar error;
- impedir corrupción.

---

# Antipatrones

Evitar:

- reconstruir todo el grafo;
- duplicar entidades;
- perder procedencia;
- fusionar automáticamente sin umbrales;
- ignorar contexto;
- eliminar identificadores;
- importar sin validar;
- sobrescribir conocimiento confirmado;
- invalidar snapshots sin registrar el motivo;
- generar inferencias durante la ingestión sin distinguirlas del conocimiento explícito.

---

# Perfil inicial de implementación

La primera versión del Knowledge Graph de NovaCoquinaria debería implementar únicamente:

- ingestión desde documentos Markdown;
- extracción basada en metadatos y componentes estructurados;
- resolución básica de entidades mediante identificadores canónicos;
- validación estructural y ontológica;
- persistencia del grafo;
- generación de snapshots;
- trazabilidad completa de la procedencia.

Las capacidades más avanzadas (resolución semántica compleja, alineamiento con grafos externos, enriquecimiento mediante IA o reconciliación automática) podrán incorporarse de forma progresiva en versiones posteriores.

---

# Conclusión

La construcción del Knowledge Graph no debe entenderse como una simple importación de datos, sino como un proceso de transformación controlado que convierte información dispersa en conocimiento conectado, validado y trazable.

El pipeline definido garantiza que cada entidad, relación y afirmación del SGCC tenga un origen conocido, una identidad estable y un ciclo de vida gestionado, permitiendo que el grafo evolucione de forma incremental sin perder consistencia ni reproducibilidad.

Esta arquitectura constituye la base para las capacidades avanzadas del sistema. En la Parte IV se desarrollarán los mecanismos de explotación del Knowledge Graph, incluyendo consultas, navegación, recorridos, análisis, visualización e integración con el razonador, los sistemas RAG y los agentes inteligentes.

---

# Parte IV — Consultas, navegación, análisis y explotación del Knowledge Graph

---

# Introducción

Las partes anteriores han definido:

- los fundamentos del Knowledge Graph;
- su modelo formal;
- sus entidades, relaciones y afirmaciones;
- su contexto, procedencia y temporalidad;
- el proceso de construcción e ingestión;
- la resolución de entidades;
- la validación;
- el versionado;
- los snapshots;
- el mantenimiento incremental.

Esta cuarta parte describe cómo debe explotarse el Knowledge Graph una vez construido.

El valor del grafo no reside únicamente en almacenar conocimiento conectado.

Reside en permitir:

- consultarlo;
- recorrerlo;
- descubrir conexiones;
- generar subgrafos;
- responder preguntas;
- analizar patrones;
- explicar resultados;
- alimentar aplicaciones;
- proporcionar contexto a razonadores, sistemas RAG y agentes inteligentes.

La explotación del Knowledge Graph deberá realizarse sin romper:

- la semántica definida por la ontología;
- la procedencia de las afirmaciones;
- la separación entre hechos e inferencias;
- los permisos;
- la reproducibilidad;
- la trazabilidad.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir el modelo oficial de consulta;
- establecer principios de navegación;
- regular recorridos y caminos;
- definir consultas estructurales y semánticas;
- establecer mecanismos de búsqueda híbrida;
- definir vistas y subgrafos de consulta;
- regular el análisis del grafo;
- establecer métricas topológicas y semánticas;
- definir mecanismos de visualización;
- preparar la integración con razonamiento;
- preparar la integración con RAG;
- preparar la integración con agentes inteligentes;
- garantizar seguridad, rendimiento y explicabilidad.

---

# Principios de explotación

Toda explotación del Knowledge Graph deberá respetar los siguientes principios.

---

## Semántica preservada

Una consulta no deberá alterar el significado de:

- clases;
- propiedades;
- relaciones;
- contextos;
- estados.

---

## Procedencia visible

Los resultados deberán poder vincularse con:

- fuentes;
- documentos;
- afirmaciones;
- reglas;
- versiones.

---

## Separación entre capas

Las consultas deberán poder distinguir entre:

- conocimiento explícito;
- conocimiento validado;
- conocimiento inferido;
- conocimiento hipotético;
- conocimiento disputado.

---

## Contexto explícito

Toda consulta dependiente de:

- región;
- periodo;
- cultura;
- dieta;
- usuario;
- versión;

deberá declarar dicho contexto.

---

## Reproducibilidad

Una consulta reproducible deberá identificar:

- versión del grafo;
- versión de la ontología;
- parámetros;
- perfil;
- fecha;
- motor;
- permisos aplicados.

---

## Mínimo privilegio

Los resultados deberán respetar los permisos efectivos del solicitante.

---

## Explicabilidad

Toda respuesta semántica relevante deberá poder explicar:

- qué nodos participaron;
- qué relaciones se recorrieron;
- qué filtros se aplicaron;
- qué inferencias se utilizaron;
- qué fuentes respaldan el resultado.

---

## Independencia tecnológica

El modelo conceptual de consulta no dependerá exclusivamente de:

- SPARQL;
- Cypher;
- SQL;
- GraphQL;
- una API concreta.

---

# Arquitectura de explotación

El flujo general podrá representarse así:

```text
Pregunta o necesidad
        │
        ▼
Análisis de intención
        │
        ▼
Selección de ámbito
        │
        ├── Grafo completo
        ├── Módulo
        ├── Colección
        ├── Snapshot
        └── Perfil
        │
        ▼
Planificación de consulta
        │
        ▼
Ejecución
        │
        ├── Consulta estructural
        ├── Consulta semántica
        ├── Recorrido
        ├── Búsqueda textual
        ├── Búsqueda vectorial
        └── Inferencia
        │
        ▼
Filtrado y ranking
        │
        ▼
Explicación
        │
        ▼
Resultado
```

---

# Tipos de consulta

El Knowledge Graph deberá soportar diferentes familias de consulta.

---

## Consulta de identidad

Permite localizar una entidad concreta.

Ejemplos:

```text
Obtener ING-0008
```

```text
Resolver el alias "pasta de miso"
```

---

## Consulta de tipo

Permite obtener entidades pertenecientes a una clase.

Ejemplo:

```text
Ingredientes fermentados
```

---

## Consulta de propiedad

Permite filtrar entidades por atributos.

Ejemplo:

```text
Recetas con dificultad básica
```

---

## Consulta relacional

Permite localizar entidades conectadas mediante una relación.

Ejemplo:

```text
Recetas que utilizan miso
```

---

## Consulta de camino

Permite encontrar rutas entre entidades.

Ejemplo:

```text
Cómo se conecta el miso con la cocina vegetariana
```

---

## Consulta jerárquica

Permite navegar por:

- superclases;
- subclases;
- categorías;
- taxonomías;
- subcolecciones.

---

## Consulta contextual

Limita resultados mediante contexto.

Ejemplo:

```text
Preparaciones japonesas tradicionales del periodo contemporáneo
```

---

## Consulta temporal

Permite obtener:

- hechos válidos en una fecha;
- cambios entre versiones;
- evolución;
- estados históricos.

---

## Consulta de procedencia

Permite responder:

- de dónde procede un hecho;
- qué documento lo respalda;
- quién lo validó;
- qué proceso lo generó.

---

## Consulta de conflicto

Permite localizar:

- afirmaciones contradictorias;
- entidades disputadas;
- valores incompatibles;
- fuentes divergentes.

---

## Consulta de calidad

Permite detectar:

- nodos huérfanos;
- relaciones sin procedencia;
- entidades duplicadas;
- baja confianza;
- falta de cobertura.

---

## Consulta analítica

Permite calcular:

- distribuciones;
- frecuencias;
- centralidad;
- densidad;
- conectividad;
- comunidades;
- evolución.

---

## Consulta inferencial

Permite recuperar conclusiones derivadas.

Ejemplo:

```text
Recetas potencialmente aptas para una dieta vegetariana
```

---

# Ámbito de consulta

Toda consulta deberá definir su ámbito.

---

## Grafo completo

Consulta todo el conocimiento autorizado.

---

## Módulo

Ejemplo:

```text
KG-INGREDIENTS
```

---

## Colección

Ejemplo:

```text
COL-0001 Cocina japonesa
```

---

## Subgrafo

Consulta una proyección concreta.

---

## Snapshot

Consulta una versión inmutable.

Ejemplo:

```text
KG-SNAP-20260731-001
```

---

## Capa

Podrá limitarse a:

```text
explicit
validated
inferred
hypothetical
```

---

## Perfil

Ejemplos:

- público;
- interno;
- editorial;
- seguridad alimentaria;
- RAG;
- agente.

---

# Consulta canónica

El SGCC podrá definir un modelo abstracto de consulta independiente de la tecnología.

Ejemplo:

```yaml
query:
  scope:
    collection: COL-0001
    graph_version: 1.4.0

  select:
    type: Recipe

  where:
    all:
      - relation:
          predicate: uses_ingredient
          object: ING-0008

      - relation:
          predicate: belongs_to_cuisine
          object: CUISINE-JAPANESE

  exclude:
    - status: deprecated

  include_layers:
    - explicit
    - validated

  order_by:
    - relevance: desc
```

Esta definición podrá transformarse en:

- SPARQL;
- Cypher;
- SQL;
- GraphQL;
- consultas internas.

---

# Modelo de consulta

Toda consulta podrá incluir:

```text
Ámbito

Selección

Condiciones

Relaciones

Contexto

Temporalidad

Capas

Permisos

Ordenación

Paginación

Explicación
```

---

# Parámetros de consulta

Ejemplos:

- idioma;
- colección;
- región;
- fecha;
- profundidad;
- confianza mínima;
- número máximo de resultados;
- capas incluidas;
- perfil de usuario.

---

# Resultado de consulta

Todo resultado debería poder incluir:

- entidades;
- relaciones;
- propiedades;
- explicación;
- procedencia;
- confianza;
- versión;
- advertencias;
- enlaces de navegación.

---

## Ejemplo conceptual

```yaml
result:
  query_id: QRY-000142
  graph_version: 1.4.0
  executed_at: 2026-07-31T18:00:00+02:00

  entities:
    - REC-0009
    - REC-0047

  total: 2

  explanation:
    - matched_relation: uses_ingredient
      object: ING-0008

  provenance:
    - DOC-0051
    - DOC-0094
```

---

# Navegación del grafo

La navegación permite recorrer el conocimiento desde una entidad inicial.

---

# Vecindad

La vecindad de un nodo incluye las entidades conectadas directamente.

Ejemplo:

```text
Miso
    │
    ├── usado_en → Sopa de miso
    ├── originario_de → Japón
    ├── pertenece_a → Ingrediente fermentado
    ├── contiene → Soja
    └── sustituible_por → Miso alternativo
```

---

# Vecindad entrante

Incluye relaciones cuyo objeto es la entidad consultada.

Ejemplo:

```text
Recetas que utilizan miso
```

---

# Vecindad saliente

Incluye relaciones originadas en la entidad.

Ejemplo:

```text
Ingredientes del miso
```

---

# Profundidad

La navegación podrá limitarse por número de saltos.

```yaml
depth: 2
```

---

## Profundidad 0

Solo la entidad inicial.

---

## Profundidad 1

Vecinos directos.

---

## Profundidad 2

Vecinos de vecinos.

---

# Expansión selectiva

No todas las relaciones deberán expandirse.

Ejemplo:

```yaml
expand:
  predicates:
    - uses_ingredient
    - applies_technique
    - belongs_to_cuisine
```

---

# Expansión por tipo

Podrá limitarse a determinados tipos de nodo.

```yaml
target_types:
  - Ingredient
  - Technique
  - Recipe
```

---

# Expansión contextual

La expansión podrá requerir:

- misma región;
- misma tradición;
- misma versión;
- mismo perfil dietético.

---

# Expansión por confianza

Ejemplo:

```yaml
minimum_confidence: 0.80
```

---

# Presupuesto de expansión

Deberán establecerse límites para evitar explosiones combinatorias.

Ejemplos:

- máximo de nodos;
- máximo de relaciones;
- profundidad;
- tiempo;
- memoria;
- coste.

---

# Caminos

Un camino es una secuencia de nodos y relaciones.

```text
Nodo 1
→ Relación 1
→ Nodo 2
→ Relación 2
→ Nodo 3
```

---

# Camino simple

No repite nodos.

---

# Camino dirigido

Respeta la dirección de las relaciones.

---

# Camino no dirigido

Permite recorrer relaciones en ambos sentidos cuando la consulta lo autorice.

---

# Camino semántico

Solo utiliza predicados compatibles con una intención.

Ejemplo:

```text
Ingrediente
→ usado_en
→ Receta
→ pertenece_a_cocina
→ Cocina
```

---

# Camino de procedencia

Ejemplo:

```text
Afirmación
→ respaldada_por
→ Documento
→ deriva_de
→ Fuente
→ atribuida_a
→ Autor
```

---

# Camino de explicación

Representa cómo se obtuvo una conclusión.

---

# Camino más corto

Localiza la ruta con menor número de saltos o menor coste.

---

# Camino de menor coste

Cada relación podrá tener un peso.

Ejemplo:

```text
same_as = 0.1
uses_ingredient = 1.0
related_to = 3.0
```

Las relaciones más precisas podrán tener menor coste semántico.

---

# Caminos restringidos

Podrán limitarse por:

- predicados;
- tipos;
- contexto;
- confianza;
- temporalidad;
- permisos.

---

# Ciclos

El sistema deberá poder detectar ciclos.

Ejemplos válidos:

- afinidades;
- relaciones simétricas;
- redes de coocurrencia.

Ejemplos problemáticos:

- jerarquías;
- dependencias estrictas;
- secuencias.

---

# Consultas de jerarquía

El grafo deberá permitir navegar:

```text
Clase
↓
Subclase
↓
Subclase
↓
Instancia
```

---

# Ancestros

Devuelve conceptos más generales.

Ejemplo:

```text
Miso
→ Producto de soja
→ Ingrediente fermentado
→ Ingrediente
```

---

# Descendientes

Devuelve conceptos más específicos.

---

# Hermanos conceptuales

Entidades con una superclase compartida.

---

# Profundidad jerárquica

Podrá limitarse.

---

# Polijerarquía

La consulta deberá admitir múltiples caminos jerárquicos.

---

# Consultas temporales

El Knowledge Graph deberá permitir reconstruir conocimiento en el tiempo.

---

## Estado actual

Devuelve hechos vigentes.

---

## Estado histórico

Devuelve hechos válidos en una fecha pasada.

---

## Cambios entre fechas

Ejemplo:

```text
Qué entidades se incorporaron entre julio y agosto de 2026
```

---

## Evolución de entidad

Devuelve:

- versiones;
- cambios;
- relaciones añadidas;
- relaciones eliminadas;
- estados.

---

## Evolución de relación

Ejemplo:

```text
Cómo evolucionó la clasificación cultural de una receta
```

---

## Temporalidad bitemporal

Podrá preguntarse:

```text
¿Qué consideraba válido el SGCC el 1 de julio
sobre un hecho que posteriormente se corrigió?
```

---

# Consultas de procedencia

La procedencia deberá poder consultarse como parte de cualquier resultado.

---

## Fuente inmediata

Documento o actividad que generó la afirmación.

---

## Fuente original

Origen último conocido.

---

## Cadena de derivación

Ejemplo:

```text
Fuente externa
↓
Documento SGCC
↓
Extracción
↓
Afirmación
↓
Inferencia
```

---

## Agente responsable

Persona, sistema o modelo que participó.

---

## Método de extracción

Ejemplos:

- manual;
- importación;
- regla;
- NLP;
- modelo IA;
- cálculo.

---

# Consultas de confianza

Podrán filtrarse afirmaciones por:

- confianza mínima;
- autoridad;
- revisión;
- tipo de fuente;
- número de evidencias.

---

# Consultas de conflicto

El sistema deberá permitir recuperar:

- hechos disputados;
- fuentes contradictorias;
- valores divergentes;
- decisiones pendientes.

---

## Resultado de conflicto

Deberá mostrar:

- afirmaciones implicadas;
- contexto;
- fuentes;
- confianza;
- estado;
- política de resolución.

---

# SPARQL

Cuando el grafo utilice RDF, SPARQL será uno de los lenguajes principales de consulta.

---

# Consulta básica

```sparql
SELECT ?recipe
WHERE {
  ?recipe a sgcc:Recipe ;
          sgcc:usesIngredient sgcc:ING-0008 .
}
```

---

# Consulta con etiqueta

```sparql
SELECT ?recipe ?label
WHERE {
  ?recipe a sgcc:Recipe ;
          sgcc:usesIngredient sgcc:ING-0008 ;
          rdfs:label ?label .

  FILTER(LANG(?label) = "es")
}
```

---

# Consulta por jerarquía

```sparql
SELECT ?ingredient
WHERE {
  ?ingredient a ?type .
  ?type rdfs:subClassOf* sgcc:FermentedIngredient .
}
```

---

# Property paths

SPARQL podrá recorrer caminos.

Ejemplo:

```sparql
SELECT ?entity
WHERE {
  sgcc:ING-0008
    (^sgcc:usesIngredient/sgcc:belongsToCuisine)
    ?entity .
}
```

---

# Grafos nombrados

Podrán consultarse capas o fuentes concretas.

```sparql
SELECT ?s ?p ?o
WHERE {
  GRAPH <https://novacoquinaria.org/graph/validated> {
    ?s ?p ?o .
  }
}
```

---

# Consulta temporal

La temporalidad podrá consultarse mediante propiedades o grafos versionados.

---

# SPARQL CONSTRUCT

Permitirá generar subgrafos.

```sparql
CONSTRUCT {
  ?recipe sgcc:usesIngredient ?ingredient .
}
WHERE {
  ?recipe a sgcc:Recipe ;
          sgcc:usesIngredient ?ingredient ;
          sgcc:belongsToCuisine sgcc:JapaneseCuisine .
}
```

---

# SPARQL ASK

Permitirá comprobaciones booleanas.

```sparql
ASK {
  sgcc:REC-0009 sgcc:usesIngredient sgcc:ING-0008 .
}
```

---

# SPARQL DESCRIBE

Podrá utilizarse para obtener una vista de una entidad.

Su comportamiento deberá controlarse para evitar resultados impredecibles.

---

# SPARQL UPDATE

Las actualizaciones directas deberán estar restringidas.

Deberán pasar por:

- validación;
- autorización;
- auditoría;
- versionado.

---

# Cypher

Cuando se utilice un grafo de propiedades, Cypher podrá emplearse para consulta y navegación.

---

# Consulta básica

```cypher
MATCH (r:Recipe)-[:USES_INGREDIENT]->(i:Ingredient {id: "ING-0008"})
RETURN r
```

---

# Consulta con profundidad

```cypher
MATCH path = (i:Ingredient {id: "ING-0008"})-[*1..3]-(related)
RETURN path
```

Esta consulta deberá restringirse mediante:

- tipos de relación;
- límites;
- filtros.

---

# Consulta jerárquica

```cypher
MATCH (i:Ingredient)-[:INSTANCE_OF]->(type)-[:SUBCLASS_OF*]->(root)
WHERE root.id = "FERMENTED_INGREDIENT"
RETURN i
```

---

# Consulta de procedencia

```cypher
MATCH (statement:Statement)-[:SUPPORTED_BY]->(source:Document)
WHERE statement.id = "STM-000123"
RETURN source
```

---

# Camino más corto

```cypher
MATCH path = shortestPath(
  (a {id: "ING-0008"})-[*]-(b {id: "VEGETARIAN_DIET"})
)
RETURN path
```

Deberán limitarse los predicados autorizados.

---

# GQL y otros lenguajes

El SGCC podrá considerar GQL u otros lenguajes estandarizados cuando maduren las implementaciones.

La semántica no deberá depender de una sintaxis concreta.

---

# SQL

En arquitecturas relacionales o híbridas, determinadas consultas podrán ejecutarse mediante SQL.

Será especialmente útil para:

- métricas;
- auditoría;
- estados;
- versiones;
- agregaciones;
- operaciones transaccionales.

---

# GraphQL

GraphQL podrá exponer el grafo a aplicaciones.

Ejemplo:

```graphql
query {
  ingredient(id: "ING-0008") {
    preferredLabel
    recipes {
      id
      title
    }
    origin {
      id
      label
    }
  }
}
```

---

# Limitaciones de GraphQL

GraphQL no sustituye:

- la ontología;
- el razonamiento;
- la semántica de mundo abierto;
- las reglas;
- la explicación.

---

# API de consulta

El SGCC podrá exponer recursos como:

```text
/entities/{id}
/entities/{id}/neighbors
/entities/{id}/paths
/entities/{id}/provenance
/entities/{id}/history
/entities/{id}/conflicts
/search
/query
/subgraphs
```

---

# Consulta estructurada por API

Ejemplo:

```http
POST /api/v1/graph/query
```

```json
{
  "scope": {
    "collection": "COL-0001"
  },
  "select": {
    "type": "Recipe"
  },
  "where": [
    {
      "predicate": "uses_ingredient",
      "object": "ING-0008"
    }
  ],
  "include": {
    "provenance": true,
    "explanation": true
  }
}
```

---

# Paginación

Las consultas extensas deberán paginarse.

Opciones:

- offset;
- cursor;
- token de continuación.

La paginación por cursor será preferible para grafos dinámicos.

---

# Ordenación

Los resultados podrán ordenarse por:

- etiqueta;
- relevancia;
- confianza;
- calidad;
- fecha;
- centralidad;
- distancia;
- autoridad.

---

# Facetas

Las aplicaciones podrán ofrecer facetas por:

- tipo;
- colección;
- cocina;
- técnica;
- ingrediente;
- región;
- periodo;
- estado;
- confianza;
- fuente.

---

# Búsqueda

El Knowledge Graph deberá integrarse con diferentes modos de búsqueda.

---

## Búsqueda por identificador

Exacta y prioritaria.

---

## Búsqueda léxica

Opera sobre:

- etiquetas;
- alias;
- descripciones;
- contenido documental.

---

## Búsqueda semántica

Utiliza:

- clases;
- jerarquías;
- equivalencias;
- relaciones;
- contexto.

---

## Búsqueda vectorial

Utiliza embeddings para similitud aproximada.

---

## Búsqueda por patrón de grafo

Busca estructuras relacionales.

---

## Búsqueda híbrida

Combina varios mecanismos.

---

# Flujo de búsqueda híbrida

```text
Consulta del usuario
        │
        ▼
Normalización
        │
        ▼
Resolución de entidades
        │
        ├── Léxica
        ├── Ontológica
        └── Vectorial
        │
        ▼
Consulta de grafo
        │
        ▼
Recuperación documental
        │
        ▼
Fusión de resultados
        │
        ▼
Ranking
        │
        ▼
Explicación
```

---

# Resolución de intención

La consulta deberá identificar si el usuario busca:

- una entidad;
- una definición;
- una lista;
- un camino;
- una comparación;
- una recomendación;
- una explicación;
- una validación;
- un análisis.

---

# Resolución de entidades en consulta

Ejemplo:

```text
"miso blanco"
```

deberá resolverse hacia el identificador canónico correspondiente.

---

# Ambigüedad

Cuando un término pueda representar varias entidades, el sistema deberá:

- solicitar contexto;
- mostrar candidatos;
- utilizar señales de la consulta;
- evitar elegir silenciosamente cuando el riesgo sea alto.

---

# Expansión de consulta

Una consulta podrá ampliarse mediante:

- alias;
- traducciones;
- subclases;
- equivalencias;
- relaciones relevantes;
- términos relacionados.

---

# Control de expansión

La expansión deberá limitarse mediante:

- profundidad;
- confianza;
- relevancia;
- tipo;
- dominio.

---

# Ranking de resultados

El ranking podrá combinar varias señales.

---

## Señales léxicas

- coincidencia exacta;
- coincidencia parcial;
- alias;
- proximidad textual.

---

## Señales semánticas

- tipo;
- jerarquía;
- equivalencia;
- relaciones.

---

## Señales topológicas

- distancia;
- centralidad;
- conectividad;
- pertenencia a comunidad.

---

## Señales de calidad

- confianza;
- autoridad;
- revisión;
- número de fuentes;
- actualidad.

---

## Señales contextuales

- colección;
- usuario;
- región;
- dieta;
- idioma.

---

## Señales vectoriales

- similitud de embeddings.

---

# Fórmula conceptual de ranking

```text
score =
  lexical_score
+ semantic_score
+ graph_score
+ quality_score
+ context_score
+ vector_score
```

Los pesos deberán:

- versionarse;
- evaluarse;
- documentarse;
- ser configurables.

---

# Reordenación

Un proceso de reranking podrá utilizar:

- reglas;
- modelos estadísticos;
- modelos de lenguaje;
- señales del grafo.

Los resultados deberán conservar las puntuaciones anteriores para auditoría.

---

# Subgrafos de consulta

Una consulta podrá devolver un subgrafo en lugar de una lista.

---

# Tipos de subgrafo

---

## Subgrafo de resultados

Contiene los resultados principales.

---

## Subgrafo contextual

Añade vecinos necesarios para interpretar.

---

## Subgrafo explicativo

Incluye premisas, fuentes y caminos.

---

## Subgrafo comparativo

Permite comparar varias entidades.

---

## Subgrafo temporal

Representa un periodo.

---

## Subgrafo de conflicto

Incluye afirmaciones divergentes y sus fuentes.

---

# Contrato de subgrafo

Todo subgrafo debería incluir:

```yaml
subgraph:
  id:
  query:
  graph_version:
  generated_at:
  nodes:
  edges:
  boundary_policy:
  provenance:
  hash:
```

---

# Política de frontera

La política deberá indicar qué ocurre con relaciones externas.

Valores recomendados:

```text
closed
contextual
expanded
reference_only
```

---

# Exportación de subgrafos

Podrán exportarse mediante:

- JSON;
- JSON-LD;
- Turtle;
- GraphML;
- CSV;
- formatos de visualización.

---

# Análisis del grafo

El Knowledge Graph deberá permitir análisis topológico y semántico.

---

# Métricas básicas

- número de nodos;
- número de relaciones;
- número de afirmaciones;
- número de tipos;
- número de componentes conexas;
- número de subgrafos.

---

# Grado

El grado de un nodo representa el número de conexiones.

---

## Grado entrante

Número de relaciones recibidas.

---

## Grado saliente

Número de relaciones emitidas.

---

## Grado ponderado

Considera pesos o relevancia.

---

# Densidad

Mide el número de relaciones respecto al máximo posible.

Una densidad alta no implica necesariamente mejor calidad.

---

# Componentes conexas

Permiten detectar:

- dominios aislados;
- entidades huérfanas;
- fragmentación;
- subgrafos independientes.

---

# Nodos huérfanos

Un nodo sin relaciones relevantes podrá indicar:

- conocimiento incompleto;
- error de ingestión;
- entidad aún no desarrollada;
- diseño incorrecto.

---

# Centralidad

Las métricas de centralidad podrán ayudar a identificar entidades importantes.

---

## Degree centrality

Prioriza nodos con muchas conexiones.

---

## Betweenness centrality

Identifica nodos que conectan comunidades.

---

## Closeness centrality

Mide cercanía media al resto del grafo.

---

## Eigenvector centrality

Valora conexiones con nodos relevantes.

---

## PageRank

Podrá utilizarse para ranking de entidades.

---

# Interpretación semántica de centralidad

Una alta centralidad no implica necesariamente:

- importancia culinaria;
- autoridad;
- calidad;
- canonicidad.

Deberá interpretarse según el dominio.

---

# Detección de comunidades

Podrá utilizarse para identificar grupos emergentes.

Ejemplos:

- familias de recetas;
- tradiciones culinarias;
- técnicas relacionadas;
- ingredientes coocurrentes.

---

# Comunidades y ontología

Las comunidades estadísticas no deberán reemplazar las clases ontológicas.

Podrán:

- sugerir categorías;
- detectar patrones;
- generar propuestas.

---

# Coocurrencia

El grafo podrá analizar entidades que aparecen conjuntamente.

Ejemplos:

- ingredientes frecuentes;
- técnicas asociadas;
- utensilios utilizados en conjunto.

---

# Similitud de nodos

Podrá calcularse mediante:

- vecinos compartidos;
- caminos;
- propiedades;
- embeddings;
- clases comunes.

---

# Predicción de enlaces

Los algoritmos podrán proponer relaciones ausentes.

Ejemplo:

```text
Posible combinación entre ingredientes
```

Estas relaciones deberán clasificarse como:

- predichas;
- no confirmadas;
- sujetas a revisión.

---

# Detección de anomalías

Podrán detectarse:

- relaciones improbables;
- entidades con tipos incompatibles;
- cambios bruscos;
- nodos excesivamente conectados;
- patrones atípicos.

---

# Métricas semánticas

Además de topología, deberán evaluarse:

- cobertura ontológica;
- consistencia;
- precisión de tipos;
- relaciones genéricas;
- calidad de procedencia;
- porcentaje de inferencias;
- conflictos;
- confianza media.

---

# Métricas de procedencia

Ejemplos:

- afirmaciones sin fuente;
- fuentes únicas;
- afirmaciones con múltiples evidencias;
- antigüedad de fuentes;
- autoridad media.

---

# Métricas temporales

Ejemplos:

- crecimiento;
- tasa de cambios;
- entidades obsoletas;
- relaciones expiradas;
- edad media del conocimiento.

---

# Métricas por colección

Cada colección podrá analizar:

- tamaño;
- densidad;
- cobertura;
- centralidad;
- deuda;
- aislamiento;
- confianza;
- fuentes.

---

# Calidad de consulta

El sistema deberá medir:

- latencia;
- tasa de éxito;
- resultados vacíos;
- precisión;
- relevancia;
- explicabilidad;
- uso de fuentes;
- consumo de recursos.

---

# Visualización

El Knowledge Graph podrá visualizarse de múltiples formas.

---

# Grafo interactivo

Deberá permitir:

- zoom;
- expansión;
- filtrado;
- selección;
- búsqueda;
- apertura de detalles;
- consulta de procedencia.

---

# Codificación visual

La visualización podrá diferenciar mediante:

- forma;
- tamaño;
- color;
- borde;
- etiqueta;
- icono.

Deberá evitar depender únicamente del color.

---

# Tipos de nodo

Podrán distinguirse visualmente:

- receta;
- ingrediente;
- técnica;
- documento;
- colección;
- fuente;
- inferencia.

---

# Tipos de relación

Podrán representarse con:

- dirección;
- estilo;
- etiqueta;
- grosor;
- patrón de línea.

---

# Capas visuales

El usuario deberá poder activar o desactivar:

- explícito;
- validado;
- inferido;
- hipotético;
- procedencia;
- contexto;
- conflictos.

---

# Visualización jerárquica

Adecuada para:

- clases;
- taxonomías;
- subcolecciones;
- estructura documental.

---

# Visualización temporal

Adecuada para:

- evolución;
- versiones;
- eventos;
- vigencia.

---

# Visualización geográfica

Adecuada para:

- origen;
- distribución;
- tradiciones;
- regiones.

---

# Visualización matricial

Adecuada para:

- coocurrencias;
- compatibilidades;
- relaciones entre tipos.

---

# Visualización de caminos

Deberá mostrar:

- punto de origen;
- destino;
- relaciones;
- contexto;
- fuentes;
- costes.

---

# Visualización de conflictos

Deberá diferenciar:

- afirmaciones incompatibles;
- fuentes;
- contextos;
- estado de revisión.

---

# Visualización de procedencia

Podrá mostrar:

```text
Afirmación
↓
Documento
↓
Fuente externa
↓
Autor
```

---

# Dashboards

Los dashboards podrán mostrar:

- tamaño del grafo;
- crecimiento;
- calidad;
- conflictos;
- entidades huérfanas;
- cobertura;
- consultas;
- rendimiento;
- colecciones.

---

# Navegación documental

El usuario deberá poder pasar desde:

```text
Entidad del grafo
```

hacia:

```text
Documento que la describe
```

y regresar.

---

# Deep links

Las entidades, relaciones, afirmaciones y subgrafos deberían disponer de enlaces persistentes.

Ejemplos:

```text
/entity/ING-0008
/statement/STM-000123
/collection/COL-0001
/query/QRY-000142
```

---

# Integración con el razonador

El razonador consumirá:

- hechos;
- axiomas;
- reglas;
- contextos;
- restricciones.

El Knowledge Graph deberá permitir consultar por separado:

- premisas;
- conclusiones;
- justificaciones;
- reglas.

---

# Consulta de inferencias

Ejemplo:

```text
¿Por qué REC-0009 se considera vegetariana?
```

La respuesta deberá incluir:

```text
REC-0009 no utiliza carne
REC-0009 no utiliza pescado
REC-0009 utiliza ingredientes compatibles
Regla RULE-DIET-0014
```

---

# Explicación mínima

Deberá mostrar:

- conclusión;
- premisas;
- regla;
- fuentes;
- confianza;
- contexto.

---

# Explicación completa

Podrá añadir:

- versiones;
- motor;
- fecha;
- caminos;
- restricciones;
- alternativas descartadas.

---

# Invalidation tracing

Si una premisa cambia, deberá ser posible localizar:

- inferencias dependientes;
- colecciones afectadas;
- índices afectados;
- respuestas cacheadas.

---

# Integración con RAG

El Knowledge Graph deberá apoyar la recuperación aumentada mediante:

- resolución de entidades;
- expansión de consultas;
- selección de colecciones;
- recuperación de caminos;
- filtrado semántico;
- procedencia;
- explicación.

---

# GraphRAG

El SGCC podrá utilizar patrones GraphRAG.

Flujo conceptual:

```text
Pregunta
↓
Entidades detectadas
↓
Consulta de grafo
↓
Subgrafo relevante
↓
Documentos vinculados
↓
Chunks
↓
Contexto
↓
Respuesta
```

---

# Recuperación centrada en entidad

Parte de una entidad identificada.

Ejemplo:

```text
Miso
```

---

# Recuperación centrada en relación

Parte de un patrón.

Ejemplo:

```text
sustitutos de X
```

---

# Recuperación centrada en comunidad

Recupera un grupo semántico.

---

# Recuperación centrada en camino

Recupera la ruta explicativa entre conceptos.

---

# Recuperación centrada en colección

Restringe el dominio mediante una colección.

---

# Grafo y chunks

Cada chunk deberá poder enlazarse con:

- entidades;
- relaciones;
- documentos;
- colección;
- versión;
- permisos.

---

# Ranking GraphRAG

Podrá considerar:

- distancia en el grafo;
- relevancia de entidad;
- cobertura de la pregunta;
- calidad de fuente;
- relevancia vectorial;
- diversidad.

---

# Reducción de contexto

El grafo permitirá seleccionar únicamente:

- nodos relevantes;
- relaciones explicativas;
- documentos necesarios.

Esto reducirá contextos excesivos.

---

# Integración con agentes inteligentes

Los agentes podrán consultar el Knowledge Graph mediante herramientas controladas.

---

# Herramientas posibles

```text
get_entity
find_entities
get_neighbors
find_path
query_subgraph
get_provenance
get_conflicts
validate_statement
explain_inference
```

---

# Contratos de herramientas

Cada herramienta deberá definir:

- entrada;
- salida;
- permisos;
- límites;
- errores;
- versión.

---

# Agente explorador

Navega y descubre relaciones.

---

# Agente documental

Localiza documentación y fuentes.

---

# Agente de validación

Comprueba:

- tipos;
- dominio;
- rango;
- consistencia;
- procedencia.

---

# Agente de planificación

Utiliza el grafo para:

- menús;
- compras;
- tareas;
- secuencias.

---

# Agente de recomendación

Podrá proponer:

- recetas;
- sustituciones;
- maridajes;
- técnicas.

Sus resultados deberán distinguirse de hechos.

---

# Agente de mantenimiento

Podrá detectar:

- duplicados;
- nodos huérfanos;
- deuda;
- relaciones faltantes.

No deberá modificar conocimiento canónico sin revisión.

---

# MCP

El SGCC podrá exponer recursos y herramientas mediante MCP.

---

## Recursos conceptuales

```text
knowledge://entity/ING-0008
knowledge://collection/COL-0001
knowledge://snapshot/KG-SNAP-20260731-001
knowledge://statement/STM-000123
```

---

## Herramientas conceptuales

```text
query_graph
resolve_entity
find_path
get_evidence
explain_statement
validate_subgraph
```

---

# Contexto para agentes

El contexto devuelto deberá separar:

```text
facts
inferences
hypotheses
conflicts
sources
constraints
```

---

# Prevención de alucinaciones

Los agentes deberán:

- utilizar identificadores canónicos;
- no inventar predicados;
- no convertir similitud en identidad;
- no presentar inferencias como hechos;
- citar fuentes;
- abstenerse cuando el grafo no responda.

---

# Consultas y permisos

Toda consulta deberá aplicar autorización antes de devolver resultados.

---

# Filtrado por nodo

Oculta entidades restringidas.

---

# Filtrado por relación

Oculta conexiones sensibles.

---

# Filtrado por propiedad

Oculta atributos concretos.

---

# Filtrado por subgrafo

Limita ámbitos completos.

---

# Inferencias sensibles

Una inferencia puede revelar información aunque sus premisas estén ocultas.

El sistema deberá impedir este tipo de fuga.

---

# Métricas sensibles

Contadores y agregaciones también podrán revelar información.

---

# Caché segura

La clave de caché deberá incorporar:

- usuario o rol;
- permisos;
- ámbito;
- versión;
- consulta;
- contexto.

---

# Auditoría de consultas

Las consultas relevantes deberán registrar:

- usuario o agente;
- fecha;
- ámbito;
- operación;
- duración;
- resultado;
- errores;
- permisos.

---

# Consultas de alto impacto

Las consultas relacionadas con:

- alergias;
- seguridad alimentaria;
- salud;
- toxicidad;
- conservación;

deberán:

- utilizar fuentes validadas;
- mostrar advertencias;
- conservar explicación;
- evitar depender únicamente de inferencias probabilísticas.

---

# Rendimiento de consultas

El sistema deberá controlar:

- latencia;
- memoria;
- profundidad;
- cardinalidad;
- concurrencia;
- coste.

---

# Planificación de consultas

Antes de ejecutar consultas costosas podrá calcularse:

- número estimado de nodos;
- número de caminos;
- índices disponibles;
- coste;
- estrategia.

---

# Índices

Podrán mantenerse índices sobre:

- identificadores;
- tipos;
- etiquetas;
- alias;
- predicados;
- propiedades;
- fechas;
- colecciones;
- procedencia;
- embeddings.

---

# Índices compuestos

Ejemplo:

```text
tipo + colección + estado
```

---

# Estadísticas

El motor deberá mantener estadísticas para optimizar planes.

---

# Límite de profundidad

Las consultas recursivas deberán limitarse.

---

# Límite de resultados

Toda consulta deberá disponer de un máximo razonable.

---

# Timeout

Las consultas deberán poder cancelarse.

---

# Cuotas

Podrán aplicarse cuotas por:

- usuario;
- agente;
- colección;
- operación;
- tiempo.

---

# Caché de consultas

Podrán cachearse:

- consultas frecuentes;
- subgrafos;
- métricas;
- caminos;
- explicaciones.

---

# Invalidación de caché

Se producirá cuando cambien:

- nodos;
- relaciones;
- versiones;
- reglas;
- permisos;
- contexto.

---

# Materialización de consultas

Las consultas frecuentes podrán materializarse como vistas.

Ejemplos:

- recetas por ingrediente;
- sustituciones validadas;
- ingredientes por temporada;
- relaciones por colección.

---

# Vistas materializadas

Deberán registrar:

- definición;
- versión;
- fecha;
- fuentes;
- hash;
- política de actualización.

---

# Consultas preparadas

Las consultas recurrentes deberían predefinirse.

Ejemplos:

```text
QRY-RECIPES-BY-INGREDIENT
QRY-SUBSTITUTIONS
QRY-COLLECTION-COVERAGE
QRY-ENTITY-PROVENANCE
```

---

# Versionado de consultas

Las consultas canónicas deberán versionarse cuando cambien:

- semántica;
- parámetros;
- filtros;
- ranking;
- resultados esperados.

---

# Catálogo de consultas

El SGCC podrá mantener un registro con:

- identificador;
- nombre;
- objetivo;
- parámetros;
- versión;
- perfil;
- coste;
- permisos;
- ejemplos.

---

# Pruebas de consultas

Toda consulta canónica deberá probar:

- casos válidos;
- casos vacíos;
- ambigüedades;
- permisos;
- rendimiento;
- regresión;
- versiones.

---

# Golden results

Podrán mantenerse resultados esperados para snapshots concretos.

```yaml
query: QRY-RECIPES-BY-INGREDIENT
snapshot: KG-SNAP-20260731-001

expected:
  must_include:
    - REC-0009

  must_exclude:
    - REC-0042
```

---

# Pruebas de caminos

Deberán comprobar:

- dirección;
- profundidad;
- predicados;
- ausencia de ciclos inválidos;
- costes.

---

# Pruebas de ranking

Deberán evaluar:

- precisión;
- orden esperado;
- diversidad;
- estabilidad.

---

# Pruebas de seguridad

Deberán comprobar:

- filtrado;
- inferencias;
- métricas;
- caché;
- subgrafos;
- exportaciones.

---

# Observabilidad

La capa de consulta deberá producir:

- logs;
- métricas;
- trazas;
- perfiles de ejecución.

---

# Métricas operativas

Ejemplos:

- consultas por segundo;
- latencia media;
- latencia p95;
- errores;
- timeouts;
- nodos examinados;
- caché hit rate;
- coste medio;
- rutas calculadas.

---

# Métricas por tipo de consulta

Deberán separarse:

- identidad;
- búsqueda;
- caminos;
- análisis;
- inferencias;
- exportaciones.

---

# Trazas distribuidas

Podrán seguir el flujo:

```text
API
↓
Resolver de entidades
↓
Planificador
↓
Motor de grafo
↓
Razonador
↓
Servicio de procedencia
↓
Respuesta
```

---

# Alertas

Ejemplos:

- aumento de latencia;
- consultas recursivas excesivas;
- crecimiento de resultados;
- errores de autorización;
- cache misses anómalos;
- subgrafos demasiado grandes.

---

# Casos de uso

---

# Caso 1 — Consultar recetas por ingrediente

Pregunta:

```text
¿Qué recetas utilizan miso?
```

Proceso:

```text
Resolver "miso" → ING-0008
↓
Buscar relaciones entrantes uses_ingredient
↓
Filtrar entidades Recipe
↓
Aplicar permisos
↓
Ordenar por relevancia
↓
Añadir procedencia
```

---

# Caso 2 — Buscar una sustitución

Pregunta:

```text
¿Con qué puedo sustituir el mirin?
```

Proceso:

```text
Resolver Mirin
↓
Consultar sustituciones contextuales
↓
Filtrar por receta o técnica
↓
Evaluar confianza
↓
Recuperar efectos
↓
Mostrar evidencia
```

---

# Caso 3 — Explicar una clasificación

Pregunta:

```text
¿Por qué esta receta pertenece a cocina japonesa?
```

Proceso:

```text
Receta
↓
Relaciones culturales y geográficas
↓
Ingredientes
↓
Técnicas
↓
Fuentes
↓
Regla o criterio de colección
```

---

# Caso 4 — Analizar deuda

Pregunta:

```text
¿Qué entidades de la colección de fermentación están huérfanas?
```

Proceso:

```text
Resolver colección
↓
Obtener miembros
↓
Calcular grado relevante
↓
Filtrar nodos sin conexiones mínimas
↓
Clasificar deuda
```

---

# Caso 5 — Comparar recetas

Pregunta:

```text
¿Qué diferencias existen entre dos recetas?
```

Podrán compararse:

- ingredientes;
- técnicas;
- pasos;
- tiempos;
- contexto;
- variantes;
- restricciones.

---

# Caso 6 — Trazar una fuente

Pregunta:

```text
¿De dónde procede esta afirmación?
```

Proceso:

```text
Afirmación
↓
Documento
↓
Fragmento
↓
Fuente original
↓
Autor
```

---

# Caso 7 — Reconstruir una versión histórica

Pregunta:

```text
¿Qué conocimiento existía en la colección en julio de 2026?
```

Proceso:

```text
Seleccionar snapshot
↓
Aplicar definición de colección compatible
↓
Consultar subgrafo histórico
↓
Mostrar diferencias con versión actual
```

---

# Caso 8 — Consulta GraphRAG

Pregunta:

```text
¿Qué técnicas japonesas de conservación se relacionan con fermentación?
```

Proceso:

```text
Resolver entidades
↓
Seleccionar colección
↓
Consultar caminos
↓
Obtener subgrafo
↓
Recuperar documentos
↓
Construir contexto
↓
Generar respuesta fundamentada
```

---

# Antipatrones de consulta

Deberán evitarse los siguientes antipatrones.

---

## Consultas sin ámbito

Pueden producir resultados excesivos o ambiguos.

---

## Recorridos ilimitados

Pueden bloquear el sistema.

---

## Uso indiscriminado de relaciones genéricas

Reduce precisión.

---

## Ignorar dirección

Produce interpretaciones incorrectas.

---

## Mezclar capas

Puede presentar hipótesis como hechos.

---

## Ocultar procedencia

Reduce confianza y auditabilidad.

---

## Consultar siempre el grafo completo

Deberán utilizarse colecciones, módulos o perfiles cuando proceda.

---

## Aplicar expansión ontológica ilimitada

Genera ruido.

---

## Utilizar centralidad como autoridad

Una entidad popular no es necesariamente correcta.

---

## Considerar correlación como causalidad

La coocurrencia no implica relación causal.

---

## Interpretar comunidades como clases

Los grupos estadísticos no sustituyen la ontología.

---

## Devolver caminos sin explicar los predicados

El usuario debe comprender por qué existe la conexión.

---

## Utilizar embeddings como respuesta final

Los embeddings sirven para recuperación, no para justificar hechos.

---

## Cachear sin considerar permisos

Puede producir fugas de información.

---

## Exponer consultas de escritura sin gobierno

Toda modificación deberá pasar por validación y auditoría.

---

## Utilizar lenguaje tecnológico como contrato semántico

Cypher o SPARQL son representaciones, no el significado canónico.

---

# Perfil mínimo de explotación

La primera implementación podrá soportar:

- consulta por identificador;
- consulta por tipo;
- relaciones directas;
- navegación de profundidad 1;
- búsqueda por etiquetas y alias;
- consulta de documentos relacionados;
- procedencia básica;
- filtrado por colección.

---

# Perfil estructurado

Añadirá:

- caminos;
- jerarquías;
- subgrafos;
- temporalidad básica;
- métricas;
- consultas canónicas;
- APIs;
- paginación;
- caché.

---

# Perfil semántico

Añadirá:

- expansión ontológica;
- consultas RDF o equivalentes;
- capas de inferencia;
- explicaciones;
- conflictos;
- SHACL;
- búsqueda híbrida.

---

# Perfil inteligente

Añadirá:

- GraphRAG;
- consultas en lenguaje natural;
- agentes;
- reranking;
- predicción de enlaces;
- detección de anomalías;
- planificación automática.

---

# Implementación inicial recomendada

La primera versión práctica de explotación debería incluir:

```text
Resolución por identificador
+
Búsqueda por nombre y alias
+
Consulta de vecinos
+
Filtrado por tipo
+
Filtrado por colección
+
Consulta de procedencia
+
Generación de subgrafos simples
+
Métricas básicas
+
API de lectura
```

---

# Contrato mínimo de API

```text
GET /entities/{id}
GET /entities/{id}/relations
GET /entities/{id}/provenance
GET /collections/{id}/graph
GET /search
POST /query
```

---

# Consultas iniciales recomendadas

El SGCC debería implementar primero:

```text
Obtener entidad
```

```text
Buscar entidades
```

```text
Recetas por ingrediente
```

```text
Ingredientes por receta
```

```text
Técnicas por receta
```

```text
Documentos por entidad
```

```text
Colecciones por entidad
```

```text
Procedencia de afirmación
```

```text
Entidades huérfanas
```

```text
Referencias rotas
```

---

# Arquitectura de referencia

```text
┌──────────────────────────────────────────────┐
│                Consumidores                 │
│                                              │
│ Web · API · RAG · Agentes · Dashboards      │
└─────────────────────┬────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────┐
│              Capa de Consulta               │
│                                              │
│ Search · Query · Paths · Analytics · Explain │
└─────────────────────┬────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────┐
│        Servicios Semánticos Transversales   │
│                                              │
│ Ontología · Procedencia · Contexto · Permisos│
└─────────────────────┬────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────┐
│               Knowledge Graph               │
│                                              │
│ Entidades · Relaciones · Capas · Snapshots  │
└─────────────────────┬────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────┐
│            Índices y materializaciones      │
│                                              │
│ Texto · Grafo · Vectorial · Analítica        │
└──────────────────────────────────────────────┘
```

---

# Conformidad de consulta

Una consulta será conforme cuando:

- utilice identificadores y predicados reconocidos;
- declare ámbito;
- respete permisos;
- distinga capas;
- preserve contexto;
- registre versión;
- sea reproducible cuando proceda;
- incluya procedencia;
- no altere el grafo.

---

# Conformidad de camino

Un camino será conforme cuando:

- conecte nodos existentes;
- utilice relaciones válidas;
- respete dirección;
- respete contexto;
- declare profundidad;
- pueda explicarse;
- respete permisos.

---

# Conformidad de subgrafo

Un subgrafo será conforme cuando:

- declare su consulta de origen;
- identifique la versión del grafo;
- defina frontera;
- preserve identidad;
- conserve relaciones relevantes;
- incluya procedencia;
- pueda reproducirse.

---

# Conformidad analítica

Un análisis será conforme cuando:

- declare algoritmo;
- declare versión;
- declare parámetros;
- utilice un snapshot identificable;
- separe resultados estadísticos de hechos ontológicos;
- conserve trazabilidad;
- pueda reproducirse.

---

# Conformidad de búsqueda

Una búsqueda será conforme cuando:

- resuelva entidades de forma controlada;
- gestione ambigüedad;
- declare ámbitos y filtros;
- conserve fuentes;
- explique el ranking cuando sea relevante;
- respete permisos.

---

# Conformidad GraphRAG

Una consulta GraphRAG será conforme cuando:

- identifique entidades;
- utilice un subgrafo trazable;
- conserve documentos y chunks;
- distinga hechos e inferencias;
- cite fuentes;
- respete permisos;
- permita abstención;
- registre versión del grafo y del índice.

---

# Conclusión

La explotación del Knowledge Graph convierte el conocimiento conectado del SGCC en una capacidad operativa.

El grafo puede utilizarse para:

- localizar entidades;
- navegar relaciones;
- descubrir caminos;
- consultar jerarquías;
- reconstruir estados históricos;
- analizar procedencia;
- detectar conflictos;
- generar subgrafos;
- medir calidad;
- visualizar dominios;
- alimentar sistemas RAG;
- proporcionar herramientas a agentes inteligentes.

La consulta no deberá entenderse únicamente como recuperación de datos.

Dentro del SGCC, consultar significa interpretar conocimiento conforme a:

- la ontología;
- el contexto;
- la temporalidad;
- la procedencia;
- las capas;
- los permisos;
- las reglas de calidad.

La arquitectura de explotación deberá mantener siempre una separación clara entre:

```text
Dato recuperado

Hecho validado

Inferencia

Predicción

Recomendación
```

Con esta cuarta parte queda definida la capa de consulta, navegación, búsqueda, análisis y explotación del Knowledge Graph.

La Parte V deberá desarrollar la integración avanzada con razonamiento e inteligencia artificial, incluyendo:

- motores de inferencia;
- materialización de conclusiones;
- GraphRAG;
- recuperación híbrida;
- embeddings de grafo;
- agentes;
- memoria estructurada;
- planificación;
- explicabilidad;
- evaluación de sistemas inteligentes.

---

# Parte V — Razonamiento, GraphRAG e integración con sistemas inteligentes

---

# Introducción

Las partes anteriores han definido:

- los fundamentos del Knowledge Graph;
- su modelo formal;
- el proceso de construcción e ingestión;
- la consulta, navegación y análisis;
- la explotación mediante APIs, subgrafos y búsquedas.

Esta quinta parte describe cómo el Knowledge Graph participa en capacidades avanzadas de razonamiento e inteligencia artificial.

El grafo no deberá utilizarse únicamente como repositorio de entidades y relaciones.

Deberá constituir una infraestructura capaz de:

- soportar inferencias;
- construir explicaciones;
- orientar la recuperación de información;
- enriquecer sistemas RAG;
- proporcionar memoria estructurada;
- asistir a agentes inteligentes;
- detectar inconsistencias;
- proponer nuevo conocimiento;
- mantener separadas las evidencias, las deducciones y las predicciones.

La inteligencia del SGCC no residirá exclusivamente en modelos generativos.

Surgirá de la combinación controlada de:

```text
Documentos
+
Ontología
+
Knowledge Graph
+
Reglas
+
Recuperación
+
Modelos de IA
+
Gobernanza
```

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir la relación entre el Knowledge Graph y el razonamiento;
- establecer las capas de conocimiento explícito e inferido;
- regular la representación de inferencias;
- definir mecanismos de explicación;
- integrar el grafo con sistemas RAG;
- formalizar el modelo GraphRAG del SGCC;
- regular embeddings y representaciones vectoriales;
- definir memoria estructurada para agentes;
- establecer herramientas de acceso al grafo;
- regular propuestas generadas mediante IA;
- definir evaluación, seguridad y trazabilidad;
- evitar que predicciones o recomendaciones se conviertan automáticamente en hechos.

---

# Principios de inteligencia semántica

Toda integración inteligente deberá respetar los siguientes principios.

---

## El grafo como fuente estructurada

El Knowledge Graph proporcionará:

- identidades;
- tipos;
- relaciones;
- restricciones;
- contexto;
- procedencia;
- temporalidad.

Los modelos de IA no deberán redefinir estos elementos de forma unilateral.

---

## Diferenciación epistemológica

El sistema deberá distinguir siempre entre:

```text
Hecho declarado

Hecho validado

Inferencia determinista

Inferencia probabilística

Hipótesis

Predicción

Recomendación

Propuesta
```

---

## Fundamentación

Toda respuesta o conclusión deberá apoyarse, cuando sea posible, en:

- afirmaciones del grafo;
- documentos;
- evidencias;
- reglas;
- recorridos;
- cálculos reproducibles.

---

## Explicabilidad

Toda conclusión relevante deberá poder explicar:

- de dónde procede;
- qué premisas utiliza;
- qué reglas aplica;
- qué confianza posee;
- qué contexto limita su validez.

---

## Revisión humana

Las capacidades automáticas podrán:

- detectar;
- sugerir;
- clasificar;
- priorizar;
- inferir;
- proponer.

No deberán publicar automáticamente conocimiento canónico de alto impacto.

---

## Seguridad semántica

Las afirmaciones relacionadas con:

- alergias;
- toxicidad;
- conservación;
- higiene;
- seguridad alimentaria;
- nutrición clínica;

deberán utilizar niveles reforzados de evidencia, revisión y control.

---

## Reproducibilidad

Toda inferencia o resultado inteligente deberá poder reconstruirse a partir de:

- versión del grafo;
- versión de la ontología;
- reglas;
- modelos;
- parámetros;
- contexto;
- fecha.

---

## Abstención

Cuando no exista conocimiento suficiente, el sistema deberá poder indicar:

```text
No determinado
```

en lugar de inventar una conclusión.

---

# Arquitectura inteligente del SGCC

La arquitectura conceptual podrá representarse así:

```text
Fuentes documentales
        │
        ▼
Conocimiento explícito
        │
        ▼
Knowledge Graph validado
        │
        ├── Ontología
        ├── Reglas
        ├── Contexto
        ├── Procedencia
        └── Temporalidad
        │
        ▼
Capa de razonamiento
        │
        ├── Inferencia lógica
        ├── Validación
        ├── Cálculo
        ├── Clasificación
        └── Detección de conflictos
        │
        ▼
Capa de recuperación
        │
        ├── Grafo
        ├── Texto
        ├── Vectores
        └── Colecciones
        │
        ▼
Capa de agentes y aplicaciones
```

---

# Papel del Knowledge Graph en el razonamiento

El grafo suministra al razonador:

- hechos;
- clases;
- propiedades;
- restricciones;
- contextos;
- premisas;
- estados;
- fuentes.

El razonador devuelve:

- inferencias;
- clasificaciones;
- validaciones;
- conflictos;
- explicaciones;
- nuevas propuestas.

---

# Tipos de razonamiento

El SGCC podrá incorporar distintos mecanismos de razonamiento.

---

## Razonamiento ontológico

Utiliza:

- clases;
- subclases;
- equivalencias;
- dominio;
- rango;
- propiedades lógicas;
- restricciones.

---

## Razonamiento basado en reglas

Utiliza reglas explícitas de la forma:

```text
SI premisas

ENTONCES conclusión
```

---

## Razonamiento por caminos

Deriva conocimiento mediante secuencias de relaciones.

---

## Razonamiento temporal

Considera:

- vigencia;
- secuencia;
- duración;
- intervalos;
- estados históricos.

---

## Razonamiento contextual

Limita las conclusiones a:

- región;
- cultura;
- receta;
- técnica;
- usuario;
- dieta;
- entorno.

---

## Razonamiento cuantitativo

Utiliza cálculos sobre:

- cantidades;
- proporciones;
- tiempos;
- costes;
- nutrientes;
- rendimiento.

---

## Razonamiento probabilístico

Utiliza:

- modelos estadísticos;
- clasificadores;
- similitud;
- predicción de enlaces;
- modelos de lenguaje.

---

## Razonamiento híbrido

Combina:

```text
Lógica simbólica

+

Cálculo determinista

+

Modelos probabilísticos

+

Revisión humana
```

Será el modelo avanzado recomendado para el SGCC.

---

# Motor de razonamiento

El razonador podrá estructurarse mediante varios componentes.

```text
Reasoning Engine
    │
    ├── Ontology Reasoner
    ├── Rule Engine
    ├── Constraint Validator
    ├── Temporal Reasoner
    ├── Calculation Engine
    ├── Probabilistic Engine
    └── Explanation Engine
```

---

# Ontology Reasoner

Será responsable de:

- clasificación de clases;
- clasificación de individuos;
- equivalencias;
- transitividad;
- inversas;
- satisfacción;
- detección de inconsistencias.

---

# Rule Engine

Será responsable de ejecutar reglas explícitas.

Ejemplo:

```text
SI

Receta usa Ingrediente

Y

Ingrediente contiene Alérgeno

ENTONCES

Receta contiene Alérgeno
```

---

# Constraint Validator

Será responsable de comprobar:

- cardinalidades;
- tipos;
- dominios;
- rangos;
- requisitos;
- incompatibilidades;
- integridad.

---

# Temporal Reasoner

Será responsable de:

- relaciones de precedencia;
- intervalos;
- solapamientos;
- vigencia;
- reconstrucción histórica;
- estacionalidad.

---

# Calculation Engine

Será responsable de:

- conversiones;
- escalado;
- agregaciones;
- costes;
- tiempos;
- cantidades;
- métricas.

---

# Probabilistic Engine

Será responsable de:

- predicción;
- ranking;
- clasificación probable;
- similitud;
- detección de anomalías;
- recomendación.

---

# Explanation Engine

Será responsable de construir explicaciones comprensibles a partir de:

- premisas;
- reglas;
- caminos;
- cálculos;
- fuentes;
- contexto.

---

# Regla de inferencia

Toda regla deberá disponer de identidad propia.

Formato recomendado:

```text
RULE-XXXX
```

---

# Estructura de una regla

Una regla deberá declarar:

- identificador;
- nombre;
- propósito;
- premisas;
- conclusión;
- variables;
- condiciones;
- excepciones;
- prioridad;
- contexto;
- versión;
- estado;
- procedencia.

---

## Ejemplo

```yaml
id: RULE-ALLERGEN-0001
type: inference_rule
name: Propagación de alérgenos desde ingredientes

version: 1.0.0
status: stable

premises:
  - subject: "?recipe"
    predicate: uses_ingredient
    object: "?ingredient"

  - subject: "?ingredient"
    predicate: contains_allergen
    object: "?allergen"

conclusion:
  subject: "?recipe"
  predicate: contains_allergen
  object: "?allergen"

conditions:
  - ingredient_usage_is_active

provenance:
  source: ONT-MOD-ALLERGENS
```

---

# Premisas

Las premisas podrán requerir:

- afirmaciones;
- clases;
- valores;
- intervalos;
- ausencia explícita;
- contexto;
- estado;
- confianza mínima.

---

# Conclusión

La conclusión podrá producir:

- nueva relación;
- clasificación;
- alerta;
- violación;
- cálculo;
- recomendación;
- propuesta.

---

# Condiciones

Las condiciones limitan la aplicación de una regla.

Ejemplos:

- contexto geográfico;
- tipo de receta;
- estado estable;
- confianza mínima;
- periodo de vigencia;
- lista completa de ingredientes.

---

# Excepciones

Las excepciones deberán modelarse explícitamente.

Ejemplo:

```text
La regla se aplica salvo cuando el ingrediente haya sido sustituido
por una alternativa validada libre del alérgeno.
```

---

# Prioridad de reglas

Podrán existir reglas incompatibles.

La prioridad podrá determinarse por:

1. seguridad;
2. especificidad;
3. autoridad;
4. evidencia;
5. contexto;
6. versión.

---

# Regla general y regla específica

La regla más específica deberá prevalecer dentro de su contexto.

Ejemplo:

```text
Regla general:
El ingrediente X requiere cocción.
```

```text
Regla específica:
La variante Y de X puede consumirse sin cocción.
```

---

# Estado de una regla

Valores recomendados:

```text
proposed
draft
review
stable
deprecated
disabled
rejected
```

---

# Versionado de reglas

Un cambio incompatible en:

- premisas;
- conclusión;
- alcance;
- excepciones;

deberá incrementar la versión mayor.

---

# Trazabilidad de reglas

Toda regla deberá enlazar con:

- decisión;
- documentación;
- módulo ontológico;
- pruebas;
- responsable;
- historial.

---

# Inferencia

Una inferencia representa una conclusión derivada.

Formato recomendado:

```text
INF-XXXXXX
```

---

# Contrato de inferencia

Toda inferencia deberá incluir:

- identidad;
- conclusión;
- premisas;
- regla o método;
- motor;
- versión;
- fecha;
- contexto;
- confianza;
- estado;
- explicación.

---

## Ejemplo

```yaml
id: INF-000041
type: inferred_statement

conclusion:
  subject: REC-0009
  predicate: contains_allergen
  object: ALG-SOY

premises:
  - STM-000123
  - STM-000431

rule: RULE-ALLERGEN-0001

engine:
  id: SGCC-REASONER
  version: 1.0.0

context:
  recipe_version: 1.2.0

confidence: 1.0
status: active
generated_at: 2026-07-31T18:30:00+02:00
```

---

# Inferencia determinista

Una inferencia determinista se obtiene mediante:

- axioma;
- regla lógica;
- cálculo reproducible;
- transformación exacta.

Podrá utilizar confianza:

```text
1.0
```

cuando todas sus premisas sean válidas y el método sea exacto.

---

# Inferencia probabilística

Una inferencia probabilística deberá incluir:

- modelo;
- versión;
- puntuación;
- umbral;
- conjunto de entrada;
- calibración;
- explicación disponible.

---

## Ejemplo

```yaml
id: PRED-000081
type: predicted_statement

conclusion:
  subject: REC-0047
  predicate: belongs_to_cuisine
  object: CUISINE-JAPANESE

model:
  id: cuisine-classifier
  version: 2.1.0

probability: 0.84
threshold: 0.80

status: pending_review
```

---

# Inferencia contextual

Una conclusión podrá ser válida únicamente bajo un contexto.

Ejemplo:

```text
Yogur sustituye a nata

solo en

salsas frías
```

La inferencia no deberá materializarse como una relación universal.

---

# Inferencia temporal

Ejemplo:

```text
Ingrediente disponible
durante
primavera
```

La consulta deberá considerar la fecha.

---

# Inferencia negativa

La inferencia negativa requerirá:

- negación explícita;
- cierre contextual;
- evidencia suficiente.

No deberá inferirse falsedad únicamente por ausencia.

---

# Materialización de inferencias

Las inferencias podrán:

- calcularse bajo demanda;
- persistirse temporalmente;
- materializarse permanentemente;
- publicarse como vistas derivadas.

---

# Inferencia bajo demanda

Se calcula en cada consulta.

Ventajas:

- siempre actualizada;
- menor almacenamiento.

Inconvenientes:

- mayor coste;
- mayor latencia.

---

# Inferencia materializada

Se almacena en el grafo.

Ventajas:

- consultas rápidas;
- análisis;
- navegación.

Inconvenientes:

- invalidación;
- mantenimiento;
- almacenamiento.

---

# Materialización selectiva

Solo deberán persistirse inferencias que:

- sean frecuentes;
- sean relevantes;
- tengan alta estabilidad;
- puedan invalidarse;
- conserven justificación.

---

# Grafo inferido

Las inferencias materializadas deberán residir en:

- capa diferenciada;
- grafo nombrado;
- tabla específica;
- atributo de origen.

---

# Invalidación de inferencias

Una inferencia deberá revisarse cuando cambie:

- una premisa;
- una regla;
- la ontología;
- el contexto;
- la versión;
- el modelo;
- el umbral.

---

# Grafo de dependencias inferenciales

El sistema deberá mantener relaciones como:

```text
Inferencia
depends_on
Premisa
```

```text
Inferencia
generated_by
Regla
```

Esto permitirá invalidación selectiva.

---

# Recalculo

Podrá realizarse:

- inmediatamente;
- por eventos;
- por lotes;
- bajo demanda;
- de forma programada.

---

# Explicabilidad

La explicación constituye una capacidad obligatoria para las inferencias relevantes.

---

# Tipos de explicación

---

## Explicación lógica

Muestra:

- premisas;
- regla;
- conclusión.

---

## Explicación por camino

Muestra el recorrido del grafo.

---

## Explicación documental

Muestra fuentes y fragmentos.

---

## Explicación cuantitativa

Muestra fórmulas y valores.

---

## Explicación probabilística

Muestra:

- modelo;
- señales;
- puntuación;
- incertidumbre.

---

## Explicación contrastiva

Responde:

```text
¿Por qué A y no B?
```

---

## Explicación de ausencia

Responde:

```text
¿Por qué no puede concluirse X?
```

---

# Niveles de explicación

Podrán existir:

```text
resumen
estandar
detallada
tecnica
auditoria
```

---

# Explicación resumida

Ejemplo:

```text
La receta contiene soja porque utiliza miso,
que está clasificado como producto de soja.
```

---

# Explicación técnica

```text
STM-000123:
REC-0009 uses_ingredient ING-0008

STM-000431:
ING-0008 contains_allergen ALG-SOY

RULE-ALLERGEN-0001

Conclusión:
REC-0009 contains_allergen ALG-SOY
```

---

# Explicación de confianza

Deberá diferenciar:

- confianza de premisas;
- confianza de regla;
- confianza de modelo;
- confianza de conclusión.

---

# Razonamiento y conflictos

El razonador deberá detectar:

- axiomas incompatibles;
- clases insatisfacibles;
- cardinalidades violadas;
- conclusiones contradictorias;
- ciclos inválidos;
- negaciones incompatibles.

---

# Conflicto inferencial

Ejemplo:

```text
Receta suitable_for VeganDiet
```

y:

```text
Receta uses_ingredient Egg
```

El sistema deberá:

- registrar el conflicto;
- identificar premisas;
- mostrar la regla;
- evitar publicar la conclusión como estable;
- solicitar revisión.

---

# Resolución de conflicto

La resolución podrá:

- invalidar una premisa;
- actualizar contexto;
- modificar una regla;
- separar variantes;
- aceptar la divergencia;
- mantener ambas afirmaciones como disputadas.

---

# Validación previa al razonamiento

Antes de ejecutar reglas deberán validarse:

- tipos;
- estados;
- contexto;
- procedencia;
- vigencia;
- permisos;
- integridad.

---

# Validación posterior

Tras la inferencia deberán comprobarse:

- consistencia;
- duplicidad;
- conflicto;
- confianza;
- reglas de seguridad;
- impacto.

---

# Knowledge Graph y RAG

El Knowledge Graph deberá mejorar la recuperación aumentada mediante:

- resolución de entidades;
- delimitación de dominio;
- expansión semántica;
- búsqueda por relaciones;
- selección de documentos;
- construcción de contexto;
- explicación;
- filtrado por procedencia.

---

# RAG clásico y GraphRAG

---

## RAG clásico

Flujo típico:

```text
Pregunta
↓
Embedding
↓
Búsqueda vectorial
↓
Chunks
↓
Generación
```

---

## GraphRAG

Flujo enriquecido:

```text
Pregunta
↓
Resolución de entidades
↓
Selección de colección
↓
Consulta de grafo
↓
Subgrafo relevante
↓
Documentos y chunks vinculados
↓
Ranking híbrido
↓
Contexto estructurado
↓
Generación fundamentada
```

---

# Modelo GraphRAG del SGCC

El modelo recomendado deberá combinar:

```text
Recuperación léxica
+
Recuperación vectorial
+
Recuperación por grafo
+
Filtros ontológicos
+
Colecciones
+
Procedencia
```

---

# Fases de GraphRAG

---

## 1. Análisis de pregunta

Identifica:

- intención;
- entidades;
- relaciones;
- restricciones;
- contexto;
- tipo de respuesta.

---

## 2. Resolución de entidades

Convierte términos en identificadores canónicos.

---

## 3. Selección de ámbito

Determina:

- colección;
- módulo;
- perfil;
- snapshot;
- capa.

---

## 4. Planificación de recuperación

Decide qué mecanismos utilizar.

Ejemplo:

```text
Vectorial + caminos + documentos
```

---

## 5. Recuperación de grafo

Obtiene:

- nodos;
- caminos;
- vecinos;
- afirmaciones;
- procedencia.

---

## 6. Recuperación documental

Obtiene:

- documentos;
- componentes;
- chunks;
- tablas;
- evidencias.

---

## 7. Fusión

Combina resultados y elimina duplicados.

---

## 8. Ranking

Ordena por relevancia, calidad y contexto.

---

## 9. Construcción de contexto

Genera un paquete estructurado.

---

## 10. Generación

El modelo responde utilizando únicamente el contexto autorizado.

---

## 11. Verificación

Comprueba:

- citas;
- coherencia;
- afirmaciones no respaldadas;
- restricciones;
- seguridad.

---

# Plan de recuperación

Un plan deberá poder representarse explícitamente.

```yaml
retrieval_plan:
  query_id: QRY-000214

  entity_resolution:
    enabled: true

  scopes:
    collections:
      - COL-0001

  graph:
    enabled: true
    max_depth: 2
    predicates:
      - uses_ingredient
      - applies_technique
      - belongs_to_cuisine

  vector:
    enabled: true
    top_k: 20

  lexical:
    enabled: true
    top_k: 20

  rerank:
    enabled: true
    top_k: 8
```

---

# Tipos de recuperación GraphRAG

---

## Entity-centric

Parte de una entidad.

Ejemplo:

```text
Miso
```

---

## Relationship-centric

Parte de una relación.

Ejemplo:

```text
sustitutos de mirin
```

---

## Path-centric

Busca una ruta explicativa.

Ejemplo:

```text
Relación entre fermentación y conservación
```

---

## Community-centric

Recupera comunidades del grafo.

---

## Collection-centric

Opera dentro de una Colección de Conocimiento.

---

## Document-centric

Parte de documentos y los conecta con entidades.

---

## Temporal-centric

Opera sobre un periodo o snapshot.

---

# Subgrafo de recuperación

El resultado de la recuperación deberá incluir únicamente conocimiento relevante.

---

## Contenido mínimo

- nodos principales;
- relaciones;
- caminos;
- fuentes;
- documentos;
- fragmentos;
- confianza;
- versión.

---

## Límites

Deberán aplicarse:

- profundidad;
- número de nodos;
- número de caminos;
- tiempo;
- presupuesto de tokens;
- permisos.

---

# Context package

El contexto para un modelo generativo podrá adoptar una estructura como:

```yaml
context_package:
  query: ¿Con qué puedo sustituir el mirin?

  entities:
    - id: ING-MIRIN
      label: Mirin

  facts:
    - statement: STM-0014
      subject: ING-RICE-WINE
      predicate: substitutes_for
      object: ING-MIRIN

  contextual_substitutions:
    - id: SUB-0008
      substitute: dry_sherry_plus_sugar
      context: cooked_sauces
      confidence: 0.88

  warnings:
    - No existe sustitución exacta para todas las preparaciones.

  sources:
    - DOC-0142
    - DOC-0179
```

---

# Context engineering

La construcción del contexto deberá priorizar:

1. hechos canónicos;
2. restricciones;
3. fuentes primarias;
4. relaciones explicativas;
5. inferencias deterministas;
6. recomendaciones;
7. predicciones.

---

# Contexto mínimo suficiente

No deberá incluirse todo el subgrafo disponible.

El contexto deberá contener solo aquello necesario para responder.

---

# Diversidad de fuentes

La recuperación deberá evitar contextos formados por múltiples fragmentos redundantes de una única fuente cuando existan perspectivas complementarias.

---

# Deduplicación

Los chunks duplicados deberán consolidarse.

Deberá conservarse:

- lista de fuentes;
- colecciones;
- entidades;
- versiones.

---

# Grounding

Toda afirmación generada deberá vincularse con evidencia recuperada.

---

# Verificación de grounding

El sistema podrá comprobar:

- si cada afirmación aparece en el contexto;
- si se deriva mediante una regla válida;
- si la cita respalda la afirmación;
- si existe extrapolación indebida.

---

# Respuesta sin respaldo

Una afirmación no respaldada deberá:

- eliminarse;
- marcarse como hipótesis;
- solicitar verificación;
- provocar abstención.

---

# Citas semánticas

Una respuesta podrá citar:

- documento;
- fragmento;
- entidad;
- afirmación;
- regla;
- camino.

---

# Embeddings

Los embeddings constituyen representaciones numéricas derivadas.

No forman parte del conocimiento canónico.

---

# Tipos de embeddings

---

## Embeddings documentales

Representan documentos o chunks.

---

## Embeddings de entidad

Representan:

- nombre;
- descripción;
- relaciones;
- contexto.

---

## Embeddings de relación

Representan predicados o patrones.

---

## Embeddings de subgrafo

Representan comunidades o colecciones.

---

## Embeddings estructurales

Se obtienen de la topología.

Ejemplos:

- Node2Vec;
- GraphSAGE;
- TransE;
- RotatE.

---

## Embeddings multimodales

Podrán incorporar:

- texto;
- imágenes;
- vídeo;
- audio;
- estructura.

---

# Metadatos de embedding

Todo embedding deberá registrar:

```yaml
embedding:
  id: EMB-000145
  target: ING-0008
  target_version: 1.2.0

  model:
    id: embedding-model
    version: 3

  dimensions: 1536
  generated_at: 2026-07-31
  content_hash: sha256:...
  status: valid
```

---

# Actualización de embeddings

Deberán regenerarse cuando cambien:

- contenido;
- relaciones relevantes;
- modelo;
- normalización;
- chunking;
- idioma;
- versión.

---

# Embeddings y identidad

Una similitud elevada no implica identidad.

Ejemplo:

```text
similaridad(A, B) = 0.95
```

no permite concluir:

```text
A same_as B
```

---

# Embeddings y canonicidad

Los embeddings podrán:

- sugerir duplicados;
- encontrar contenido;
- detectar temas;
- clasificar;
- recomendar.

No podrán establecer conocimiento canónico sin validación.

---

# Vector Store

El vector store será una infraestructura derivada.

Deberá enlazar cada vector con:

- entidad;
- documento;
- chunk;
- versión;
- colección;
- permisos;
- procedencia.

---

# Índices híbridos

El SGCC podrá mantener:

```text
Índice textual

+

Índice vectorial

+

Índice de grafo

+

Índice ontológico
```

---

# Sincronización de índices

Los índices deberán invalidarse cuando cambien:

- fuentes;
- entidades;
- relaciones;
- permisos;
- colecciones;
- modelos.

---

# Evaluación de recuperación

El sistema deberá medir:

- precision@k;
- recall@k;
- MRR;
- nDCG;
- cobertura;
- diversidad;
- latencia;
- tasa de resultados irrelevantes.

---

# Evaluación de generación

Podrá medir:

- groundedness;
- fidelidad;
- corrección;
- completitud;
- calidad de citas;
- abstención;
- seguridad.

---

# Gold datasets

Cada colección podrá disponer de un conjunto de evaluación.

```yaml
evaluation_set:
  id: EVAL-COL-0001
  collection: COL-0001
  version: 1.0.0

  cases:
    - question: ¿Qué ingredientes contiene una sopa de miso?
      expected_entities:
        - ING-0008
      answerable: true
```

---

# Casos no respondibles

El conjunto deberá incluir preguntas para las que el sistema debe abstenerse.

---

# Casos adversariales

Deberán incluir:

- términos ambiguos;
- afirmaciones falsas;
- fuentes contradictorias;
- peticiones fuera de colección;
- información restringida.

---

# Agentes inteligentes

Los agentes utilizarán el Knowledge Graph como:

- memoria estructurada;
- espacio de navegación;
- fuente de restricciones;
- mecanismo de planificación;
- registro de evidencia;
- sistema de explicación.

---

# Modelo de agente

```text
Agente
    │
    ├── Rol
    ├── Objetivos
    ├── Colecciones
    ├── Herramientas
    ├── Memoria
    ├── Permisos
    ├── Políticas
    └── Registro de acciones
```

---

# Tipos de agente

---

## Agente de consulta

Responde preguntas sobre el conocimiento existente.

---

## Agente de planificación culinaria

Puede planificar:

- menús;
- compras;
- preparaciones;
- tiempos;
- reutilización de ingredientes.

---

## Agente de sustituciones

Propone alternativas considerando:

- función;
- sabor;
- textura;
- alergias;
- disponibilidad;
- contexto.

---

## Agente de documentación

Detecta:

- documentos incompletos;
- secciones ausentes;
- referencias rotas;
- inconsistencias.

---

## Agente de conocimiento

Propone:

- entidades;
- relaciones;
- normalizaciones;
- nuevas colecciones;
- deuda.

---

## Agente de calidad

Evalúa:

- cobertura;
- duplicados;
- nodos huérfanos;
- baja confianza;
- conflictos.

---

## Agente de investigación

Explora fuentes y genera propuestas de conocimiento.

---

## Agente de seguridad alimentaria

Deberá operar con:

- fuentes reforzadas;
- reglas estrictas;
- abstención;
- revisión humana.

---

# Herramientas del agente

Podrán exponerse herramientas como:

```text
resolve_entity
get_entity
search_graph
query_collection
find_path
get_provenance
get_constraints
validate_statement
explain_inference
propose_statement
calculate_quantity
```

---

# Contrato de herramienta

Toda herramienta deberá declarar:

- identificador;
- propósito;
- entrada;
- salida;
- errores;
- permisos;
- límites;
- versión;
- efectos.

---

## Ejemplo

```yaml
tool:
  id: TOOL-KG-FIND-PATH
  name: find_path
  version: 1.0.0

  input:
    source_entity: string
    target_entity: string
    max_depth: integer
    allowed_predicates: list

  output:
    paths: list
    explanations: list
    provenance: list

  permissions:
    - graph_read
```

---

# Herramientas de lectura

No modifican el conocimiento.

Ejemplos:

- búsqueda;
- consulta;
- navegación;
- explicación;
- validación.

---

# Herramientas de propuesta

Generan borradores o propuestas.

Ejemplos:

- proponer relación;
- proponer alias;
- proponer fusión;
- proponer clasificación.

---

# Herramientas de escritura

Deberán estar altamente restringidas.

No deberán permitir publicación canónica directa salvo flujos expresamente autorizados.

---

# Principio de separación entre propuesta y publicación

```text
Agente propone

↓

Sistema valida

↓

Persona revisa

↓

Gobernanza aprueba

↓

SGCC publica
```

---

# Memoria del agente

La memoria deberá distinguir varios niveles.

---

## Memoria de sesión

Información temporal del diálogo o tarea.

---

## Memoria de trabajo

Datos necesarios para ejecutar un plan.

---

## Memoria del usuario

Preferencias persistentes autorizadas.

---

## Memoria de dominio

Conocimiento del Knowledge Graph.

---

## Memoria episódica

Historial de acciones y resultados.

---

## Memoria procedimental

Reglas y estrategias de actuación.

---

# El grafo como memoria de dominio

El Knowledge Graph será la memoria estructurada compartida.

No deberá confundirse con:

- mensajes de conversación;
- prompts;
- cachés;
- historial efímero.

---

# Memoria privada y conocimiento global

La información de usuario deberá almacenarse en subgrafos o almacenes separados.

No deberá integrarse automáticamente en el grafo global.

---

# Promoción de memoria

Una observación de usuario podrá convertirse en:

- preferencia privada;
- propuesta;
- regla personal;
- conocimiento compartido.

Cada caso requerirá un flujo distinto.

---

# Planificación de agentes

Los agentes podrán utilizar el grafo para descomponer objetivos.

Ejemplo:

```text
Objetivo:
Preparar una cena japonesa vegetariana

↓

Restricciones:
- vegetariana
- cuatro personas
- ingredientes disponibles

↓

Subobjetivos:
1. Seleccionar recetas
2. Comprobar compatibilidad
3. Calcular cantidades
4. Generar lista de compra
5. Planificar tiempos
```

---

# Grafo de tareas

Un plan podrá representarse como grafo.

```text
Objetivo
    │
    ├── requiere → Tarea 1
    ├── requiere → Tarea 2
    └── requiere → Tarea 3
```

Relaciones posibles:

```text
depends_on
precedes
requires
produces
assigned_to
```

---

# Estado de tareas

Ejemplos:

```text
planned
ready
running
blocked
completed
failed
cancelled
```

---

# Replanificación

Un agente podrá adaptar el plan cuando cambien:

- disponibilidad;
- restricciones;
- resultados;
- errores;
- preferencias.

La replanificación deberá registrar el motivo.

---

# Agentes y Colecciones de Conocimiento

Una colección podrá actuar como dominio operativo de un agente.

Ejemplo:

```text
Agente de cocina japonesa
        │
        ├── colección: COL-0001
        ├── subgrafo: Cocina japonesa
        ├── índice RAG
        ├── reglas
        └── herramientas
```

---

# Agentes multicolección

Un agente podrá combinar:

```text
COL-CocinaJaponesa

INTERSECT

COL-Vegetariana

INTERSECT

COL-DespensaDisponible
```

---

# Resolución de conflictos entre colecciones

Cuando las colecciones produzcan restricciones incompatibles, el agente deberá:

- detectar el conflicto;
- explicar las restricciones;
- priorizar según política;
- solicitar decisión cuando sea necesario.

---

# Orquestación de agentes

El SGCC podrá utilizar varios agentes especializados.

Ejemplo:

```text
Agente coordinador
    │
    ├── Agente de recetas
    ├── Agente nutricional
    ├── Agente de compras
    ├── Agente de planificación
    └── Agente de seguridad
```

---

# Comunicación entre agentes

Los intercambios deberán ser estructurados.

Ejemplo:

```yaml
message:
  sender: recipe_agent
  receiver: safety_agent
  task: validate_recipe
  entity: REC-0009
  graph_version: 1.4.0
```

---

# Fuente compartida

Los agentes deberán consultar el mismo Knowledge Graph o snapshots compatibles.

Esto evita estados semánticos divergentes.

---

# Bloqueo y concurrencia

Las operaciones de propuesta o edición deberán gestionar:

- versiones;
- conflictos;
- bloqueos optimistas;
- revisiones concurrentes.

---

# MCP

El Model Context Protocol podrá actuar como capa estandarizada de acceso.

---

# Recursos MCP

Ejemplos conceptuales:

```text
knowledge://entities/ING-0008
knowledge://statements/STM-000123
knowledge://collections/COL-0001
knowledge://rules/RULE-ALLERGEN-0001
knowledge://snapshots/KG-SNAP-20260731-001
```

---

# Herramientas MCP

Ejemplos:

```text
query_graph
find_path
get_provenance
resolve_alias
validate_statement
explain_inference
propose_relation
```

---

# Prompt y contexto

El prompt no deberá contener todo el conocimiento.

Deberá incluir:

- objetivo;
- reglas operativas;
- contexto recuperado;
- restricciones;
- herramientas;
- formato de salida.

---

# Contexto estructurado para agentes

Ejemplo:

```yaml
agent_context:
  objective: Proponer sustitutos del mirin

  entities:
    - ING-MIRIN

  facts:
    - STM-0014
    - STM-0018

  constraints:
    - preserve_sweetness
    - preserve_acidity
    - no_alcohol

  tools:
    - query_graph
    - calculate_ratio

  policies:
    - cite_sources
    - mark_uncertainty
    - do_not_modify_canonical_graph
```

---

# Salida estructurada de agentes

Los agentes deberán devolver resultados tipados.

Ejemplo:

```yaml
proposal:
  type: ingredient_substitution

  original: ING-MIRIN
  substitute:
    components:
      - rice_vinegar
      - sugar

  context:
    suitable_for:
      - cooked_sauces

  confidence: 0.78

  evidence:
    - DOC-0142

  status: proposed
```

---

# Propuestas de conocimiento

Una propuesta generada por IA deberá incluir:

- entidad o relación propuesta;
- motivación;
- evidencia;
- modelo;
- versión;
- confianza;
- contexto;
- revisión requerida.

---

# Cola de revisión

Las propuestas podrán entrar en una cola.

Estados:

```text
generated
pending_validation
pending_review
accepted
rejected
needs_changes
archived
```

---

# Validación automática de propuestas

Antes de revisión humana deberá comprobarse:

- identificadores;
- duplicidad;
- dominio;
- rango;
- consistencia;
- referencias;
- formato;
- evidencia.

---

# Revisión humana

El revisor deberá poder:

- aceptar;
- rechazar;
- modificar;
- solicitar fuentes;
- convertir en hipótesis;
- posponer.

---

# Aprendizaje a partir de revisiones

Las decisiones de revisión podrán utilizarse para:

- mejorar prompts;
- ajustar clasificadores;
- recalibrar umbrales;
- identificar errores recurrentes.

No deberán modificar automáticamente reglas canónicas.

---

# Predicción de enlaces

Los modelos podrán proponer relaciones ausentes.

Ejemplos:

- posible sustitución;
- afinidad entre ingredientes;
- pertenencia a una colección;
- similitud de recetas;
- relación cultural.

---

# Contrato de predicción

```yaml
prediction:
  id: PRED-000121

  subject: ING-0008
  predicate: pairs_with
  object: ING-0042

  model:
    id: food-pairing-model
    version: 1.4.0

  probability: 0.79
  threshold: 0.75

  evidence:
    shared_compounds: 4
    cooccurrence_score: 0.64

  status: pending_review
```

---

# Clasificación automática

Los modelos podrán sugerir:

- tipo;
- categoría;
- colección;
- rol;
- nivel de dificultad;
- contexto.

La clasificación deberá mantenerse como provisional hasta su validación cuando afecte al conocimiento canónico.

---

# Detección de duplicados mediante IA

Podrá combinar:

- similitud textual;
- embeddings;
- tipos;
- relaciones;
- identificadores externos;
- contexto.

La fusión automática solo deberá permitirse en casos de alta certeza y bajo riesgo.

---

# Detección de anomalías

Los modelos podrán identificar:

- relaciones improbables;
- cantidades atípicas;
- tiempos incoherentes;
- entidades aisladas;
- cambios anómalos;
- conflictos ocultos.

---

# Generación asistida

Los agentes podrán generar:

- borradores;
- descripciones;
- resúmenes;
- ejemplos;
- preguntas de evaluación;
- propuestas de relaciones;
- documentación derivada.

El contenido generado deberá marcarse como tal hasta su revisión.

---

# Generación de consultas

Un modelo podrá traducir lenguaje natural a:

- consulta abstracta SGCC;
- SPARQL;
- Cypher;
- GraphQL.

---

# Validación de consultas generadas

Antes de ejecutarse deberán comprobarse:

- sintaxis;
- coste;
- permisos;
- ámbito;
- operaciones prohibidas;
- profundidad;
- límites.

---

# Consultas de solo lectura

Las consultas generadas por modelos deberán ser de solo lectura por defecto.

---

# Sandbox de consultas

Las consultas experimentales podrán ejecutarse sobre:

- snapshot;
- entorno aislado;
- subgrafo;
- límite de recursos.

---

# Seguridad alimentaria

Las capacidades inteligentes relacionadas con seguridad deberán cumplir requisitos reforzados.

---

## Fuentes autorizadas

Solo podrán utilizarse fuentes:

- oficiales;
- científicas;
- normativas;
- validadas por expertos.

---

## Inferencias prohibidas

No deberán aceptarse automáticamente inferencias basadas únicamente en:

- embeddings;
- similitud;
- popularidad;
- modelos generativos.

---

## Respuestas con incertidumbre

Cuando no exista evidencia suficiente deberá indicarse explícitamente.

---

## Revisión obligatoria

Las propuestas de alto impacto requerirán revisión humana.

---

# Privacidad

Los agentes podrán acceder a subgrafos personales únicamente cuando:

- exista autorización;
- resulte necesario;
- se respete finalidad;
- se aplique minimización.

---

# Prevención de fuga de información

El sistema deberá considerar:

- consultas;
- caminos;
- inferencias;
- métricas;
- embeddings;
- cachés;
- logs.

---

# Ataques de prompt injection

El contenido documental recuperado no deberá poder modificar:

- políticas;
- permisos;
- herramientas;
- instrucciones del agente.

Los documentos serán datos, no instrucciones.

---

# Instrucciones externas

Las instrucciones encontradas en documentos o nodos deberán ignorarse salvo que pertenezcan a una política autorizada del sistema.

---

# Seguridad de herramientas

Cada herramienta deberá aplicar:

- autenticación;
- autorización;
- validación;
- límites;
- auditoría.

---

# Auditoría de agentes

Toda acción relevante deberá registrar:

- agente;
- versión;
- objetivo;
- herramienta;
- entrada;
- salida;
- fuentes;
- fecha;
- resultado;
- decisión humana posterior.

---

# Observabilidad

La capa inteligente deberá registrar métricas específicas.

---

# Métricas de razonamiento

- reglas ejecutadas;
- inferencias generadas;
- inferencias invalidadas;
- conflictos detectados;
- tiempo de razonamiento;
- profundidad de explicación.

---

# Métricas RAG

- recall;
- precisión;
- grounding;
- citas;
- latencia;
- coste;
- abstención;
- cobertura.

---

# Métricas de agentes

- tareas completadas;
- herramientas utilizadas;
- errores;
- propuestas aceptadas;
- propuestas rechazadas;
- intervenciones humanas;
- violaciones de políticas.

---

# Métricas de modelos

- precisión;
- calibración;
- deriva;
- tasa de falsos positivos;
- tasa de falsos negativos;
- rendimiento por colección.

---

# Deriva

El sistema deberá detectar:

- deriva del modelo;
- deriva de datos;
- deriva ontológica;
- deriva de consultas;
- deriva de comportamiento del agente.

---

# Recalibración

Los modelos probabilísticos deberán recalibrarse cuando:

- cambie el dominio;
- cambie el corpus;
- cambien las clases;
- disminuya el rendimiento;
- aumenten los conflictos.

---

# Evaluación offline

Se realizará mediante:

- conjuntos de prueba;
- snapshots;
- preguntas de referencia;
- escenarios controlados.

---

# Evaluación online

Podrá utilizar:

- feedback;
- tasa de corrección;
- éxito de tarea;
- aceptación de propuestas;
- métricas de uso.

---

# Evaluación humana

Los expertos podrán valorar:

- corrección culinaria;
- utilidad;
- claridad;
- contextualización;
- seguridad;
- explicabilidad.

---

# Pruebas de razonamiento

Cada regla deberá probar:

- caso positivo;
- caso negativo;
- excepción;
- conflicto;
- cambio de contexto;
- invalidación.

---

# Pruebas GraphRAG

Deberán verificar:

- resolución de entidades;
- selección de colección;
- caminos;
- documentos;
- citas;
- groundedness;
- abstención.

---

# Pruebas de agentes

Deberán incluir:

- uso correcto de herramientas;
- respeto de permisos;
- rechazo de instrucciones maliciosas;
- no modificación canónica;
- gestión de ambigüedad;
- explicación.

---

# Red Teaming

Los sistemas inteligentes deberán probarse frente a:

- prompt injection;
- datos contradictorios;
- entidades ambiguas;
- fuentes falsas;
- relaciones inventadas;
- escalado de permisos;
- extracción de datos restringidos.

---

# Rendimiento

La capa inteligente deberá controlar:

- latencia;
- coste;
- número de consultas;
- tamaño de subgrafos;
- tokens;
- llamadas a modelos;
- caché.

---

# Caché de inferencias

Las inferencias estables podrán cachearse.

La clave deberá incluir:

- versión del grafo;
- reglas;
- contexto;
- permisos;
- motor.

---

# Caché RAG

Podrán cachearse:

- planes de recuperación;
- entidades resueltas;
- subgrafos;
- resultados;
- contextos.

---

# Invalidación

La caché deberá invalidarse ante cambios en:

- documentos;
- entidades;
- relaciones;
- ontología;
- reglas;
- modelos;
- permisos;
- colecciones.

---

# Arquitectura de referencia

```text
┌───────────────────────────────────────────────┐
│              Knowledge Graph                 │
│                                               │
│ Hechos · Contexto · Procedencia · Versiones   │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            Capa de razonamiento               │
│                                               │
│ Ontología · Reglas · Cálculo · Validación     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│           Capa de recuperación                │
│                                               │
│ Grafo · Texto · Vectores · Colecciones        │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│           Capa de inteligencia                │
│                                               │
│ GraphRAG · Modelos · Agentes · Planificación  │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│          Gobernanza y supervisión             │
│                                               │
│ Validación · Seguridad · Auditoría · Revisión │
└───────────────────────────────────────────────┘
```

---

# Flujo de una respuesta GraphRAG

```text
Pregunta
    │
    ▼
Clasificación de intención
    │
    ▼
Resolución de entidades
    │
    ▼
Selección de colección
    │
    ▼
Consulta del Knowledge Graph
    │
    ▼
Recuperación documental y vectorial
    │
    ▼
Construcción de contexto
    │
    ▼
Generación
    │
    ▼
Verificación de grounding
    │
    ▼
Respuesta con fuentes y explicación
```

---

# Flujo de una propuesta de agente

```text
Objetivo
    │
    ▼
Consulta del grafo
    │
    ▼
Plan
    │
    ▼
Uso de herramientas
    │
    ▼
Resultado provisional
    │
    ▼
Validación automática
    │
    ▼
Propuesta
    │
    ▼
Revisión humana
    │
    ├── Aceptada
    ├── Modificada
    └── Rechazada
```

---

# Perfiles de capacidad inteligente

---

## Perfil 1 — Inferencia básica

Incluye:

- jerarquías;
- dominio;
- rango;
- inversas;
- reglas simples;
- explicación básica.

---

## Perfil 2 — Razonamiento estructurado

Añade:

- reglas contextuales;
- materialización;
- invalidación;
- conflictos;
- cálculo.

---

## Perfil 3 — GraphRAG

Añade:

- resolución de entidades;
- recuperación híbrida;
- subgrafos;
- chunks;
- citas;
- evaluación.

---

## Perfil 4 — Agentes especializados

Añade:

- herramientas;
- planificación;
- memoria;
- propuestas;
- auditoría.

---

## Perfil 5 — Sistema inteligente gobernado

Añade:

- multiagente;
- razonamiento híbrido;
- aprendizaje supervisado por revisiones;
- detección de deriva;
- seguridad reforzada;
- gobernanza completa.

---

# Implementación inicial recomendada

La primera fase inteligente del SGCC debería limitarse a:

```text
Reglas deterministas simples
+
Representación separada de inferencias
+
Explicaciones mediante premisas
+
Resolución de entidades
+
GraphRAG sobre colecciones seleccionadas
+
Recuperación híbrida básica
+
Agente de consulta de solo lectura
+
Auditoría completa
```

No debería comenzar todavía con:

- escritura autónoma;
- fusión automática de entidades;
- razonamiento probabilístico canónico;
- agentes con permisos amplios;
- multiagente;
- inferencias de seguridad basadas en IA.

---

# Contrato mínimo de inferencia

```yaml
id: INF-XXXX
conclusion:
premises:
rule:
engine:
graph_version:
generated_at:
status:
explanation:
```

---

# Contrato mínimo GraphRAG

```yaml
request:
  question:
  collections:
  graph_version:

retrieval:
  entities:
  subgraph:
  documents:
  chunks:

generation:
  model:
  context_hash:

response:
  answer:
  citations:
  confidence:
  warnings:
```

---

# Contrato mínimo de agente

```yaml
agent:
  id:
  role:
  version:

scope:
  collections:
  permissions:

tools:
  - tool_id

policies:
  - read_only
  - cite_sources
  - preserve_provenance
  - abstain_when_unknown
```

---

# Antipatrones

Deberán evitarse los siguientes antipatrones.

---

## Presentar inferencias como hechos explícitos

Toda inferencia deberá conservar su origen.

---

## Materializar inferencias sin dependencias

Impediría su invalidación.

---

## Utilizar un modelo generativo como razonador único

Los modelos generativos no sustituyen reglas, validación ni ontología.

---

## Utilizar embeddings como identidad

La similitud no implica equivalencia.

---

## Publicar predicciones automáticamente

Toda predicción deberá pasar por políticas de aceptación.

---

## Generar respuestas sin procedencia

Reduce trazabilidad y confianza.

---

## Recuperar únicamente por similitud vectorial

Puede ignorar:

- tipos;
- contexto;
- restricciones;
- relaciones.

---

## Incluir todo el grafo en el contexto

Produce ruido, coste y pérdida de precisión.

---

## Permitir que documentos modifiquen instrucciones del agente

El contenido recuperado deberá tratarse como datos.

---

## Otorgar permisos globales a agentes

Contradice el principio de mínimo privilegio.

---

## Mezclar memoria de usuario con conocimiento global

Ambas capas deberán permanecer separadas.

---

## Utilizar recomendaciones como axiomas

Una afinidad culinaria no es una verdad universal.

---

## Utilizar confianza sin calibración

Una puntuación no calibrada puede resultar engañosa.

---

## Ignorar las versiones de modelos

Impide reproducibilidad.

---

## Reentrenar sin conservar evaluación histórica

Impide comparar mejoras o regresiones.

---

## Automatizar ámbitos de alto impacto sin revisión

Especialmente en:

- alergias;
- conservación;
- toxicidad;
- salud.

---

## Crear agentes sin criterios de abstención

Un agente deberá poder reconocer sus límites.

---

## Generar consultas sin límites

Las consultas producidas por IA deberán validarse y restringirse.

---

## Utilizar feedback humano como verdad automática

El feedback también podrá ser erróneo o contextual.

---

# Conformidad de inferencia

Una inferencia será conforme cuando:

- utilice premisas válidas;
- derive de una regla o método registrado;
- conserve contexto;
- registre motor y versión;
- posea explicación;
- pueda invalidarse;
- se diferencie del conocimiento explícito.

---

# Conformidad de regla

Una regla será conforme cuando:

- tenga identidad;
- esté documentada;
- posea premisas y conclusión;
- declare contexto;
- incluya excepciones;
- tenga pruebas;
- esté versionada;
- disponga de responsable.

---

# Conformidad GraphRAG

Una ejecución GraphRAG será conforme cuando:

- resuelva entidades;
- identifique ámbito;
- utilice un snapshot o versión;
- conserve subgrafo;
- preserve documentos y chunks;
- cite fuentes;
- verifique grounding;
- respete permisos;
- permita abstención.

---

# Conformidad de embeddings

Un embedding será conforme cuando:

- identifique el objetivo;
- declare modelo y versión;
- conserve hash del contenido;
- respete permisos;
- pueda regenerarse;
- no se trate como fuente canónica.

---

# Conformidad de agente

Un agente será conforme cuando:

- tenga rol;
- tenga ámbito;
- utilice herramientas registradas;
- respete permisos;
- preserve procedencia;
- distinga hechos, inferencias y propuestas;
- registre sus acciones;
- no modifique conocimiento canónico sin autorización.

---

# Conformidad de propuesta IA

Una propuesta será conforme cuando:

- esté identificada como propuesta;
- indique modelo y versión;
- incluya evidencia;
- declare confianza;
- conserve contexto;
- haya superado validación automática;
- permanezca pendiente de revisión antes de publicarse.

---

# Lista de comprobación

Antes de habilitar una capacidad inteligente deberá verificarse:

```text
[ ] Los hechos y las inferencias están separados.
[ ] Las reglas tienen identificador y versión.
[ ] Las inferencias conservan sus premisas.
[ ] Existe un mecanismo de invalidación.
[ ] Las respuestas incluyen procedencia.
[ ] El GraphRAG utiliza un ámbito definido.
[ ] Los índices respetan permisos.
[ ] Los embeddings están versionados.
[ ] Existen conjuntos de evaluación.
[ ] El sistema puede abstenerse.
[ ] Las herramientas tienen permisos mínimos.
[ ] Los agentes no publican directamente.
[ ] Las propuestas IA pasan por revisión.
[ ] Se auditan acciones y resultados.
[ ] Existen pruebas de seguridad.
```

---

# Conclusión

La integración del Knowledge Graph con razonamiento, GraphRAG y agentes inteligentes permite que NovaCoquinaria evolucione desde un sistema de conocimiento conectado hacia una plataforma capaz de interpretar, recuperar, explicar y utilizar dicho conocimiento.

El valor de esta inteligencia no reside únicamente en generar respuestas.

Reside en producir resultados:

- fundamentados;
- contextualizados;
- explicables;
- reproducibles;
- auditables;
- gobernados.

La arquitectura definida mantiene una separación esencial entre:

```text
Conocimiento explícito
        ↓
Inferencia determinista
        ↓
Predicción probabilística
        ↓
Propuesta
        ↓
Conocimiento validado
```

Ningún modelo, agente o algoritmo deberá omitir estas fronteras.

El Knowledge Graph actuará como memoria semántica compartida.

La ontología definirá el significado.

Las reglas producirán conclusiones reproducibles.

GraphRAG recuperará contexto relevante.

Los agentes utilizarán ese contexto para ejecutar tareas limitadas y explicables.

La revisión humana y la gobernanza decidirán qué conocimiento puede convertirse en canónico.

Con esta quinta parte queda definida la integración avanzada del Knowledge Graph con:

- motores de razonamiento;
- reglas;
- inferencias;
- explicaciones;
- recuperación híbrida;
- GraphRAG;
- embeddings;
- agentes;
- memoria;
- planificación;
- propuestas automatizadas;
- evaluación;
- seguridad;
- auditoría.

La Parte VI completará la especificación estableciendo la gobernanza integral del Knowledge Graph, incluyendo:

- calidad;
- responsabilidades;
- versionado;
- publicación;
- interoperabilidad;
- seguridad;
- auditoría;
- deuda del grafo;
- refactorización;
- migraciones;
- métricas;
- conformidad;
- evolución estratégica.

---

# Parte VI — Gobernanza, calidad y evolución del Knowledge Graph

---

# Introducción

Las partes anteriores han definido:

- los fundamentos del Knowledge Graph;
- su modelo formal;
- la construcción e ingestión;
- las consultas, navegación y análisis;
- la integración con razonamiento, GraphRAG y agentes inteligentes.

Esta sexta parte establece el marco de gobernanza necesario para garantizar que el Knowledge Graph del SGCC pueda evolucionar de forma:

- controlada;
- coherente;
- segura;
- trazable;
- interoperable;
- sostenible.

El Knowledge Graph no deberá considerarse únicamente una infraestructura técnica.

Constituye un activo estratégico de conocimiento cuya calidad afecta directamente a:

- la documentación;
- las colecciones;
- las inferencias;
- las búsquedas;
- los sistemas RAG;
- los agentes inteligentes;
- las decisiones del proyecto.

Por esta razón, toda modificación significativa del grafo deberá someterse a reglas de gobierno explícitas.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir el modelo de gobernanza del Knowledge Graph;
- establecer responsabilidades;
- regular el ciclo de vida de sus elementos;
- definir políticas de versionado;
- garantizar compatibilidad;
- establecer métricas de calidad;
- gestionar deuda del grafo;
- regular refactorizaciones y migraciones;
- definir políticas de publicación;
- garantizar seguridad y privacidad;
- mantener auditoría y trazabilidad;
- gestionar incidentes;
- establecer niveles de madurez;
- definir perfiles de conformidad;
- orientar la evolución estratégica del grafo.

---

# Alcance

La gobernanza se aplicará a:

- entidades;
- relaciones;
- afirmaciones;
- subgrafos;
- módulos;
- snapshots;
- reglas;
- inferencias materializadas;
- alineaciones externas;
- consultas canónicas;
- vistas materializadas;
- índices derivados;
- artefactos de publicación;
- pipelines de construcción;
- mecanismos de validación.

La gobernanza no se limitará al almacén físico del grafo.

También abarcará las representaciones y servicios derivados que dependan de él.

---

# Principios de gobernanza

Toda gestión del Knowledge Graph deberá respetar los siguientes principios.

---

## Autoridad semántica

La ontología será la fuente de autoridad respecto al significado de:

- clases;
- propiedades;
- restricciones;
- axiomas;
- vocabularios.

El Knowledge Graph materializa ese significado.

No deberá redefinirlo de forma independiente.

---

## Identidad persistente

Las entidades y afirmaciones relevantes conservarán una identidad estable durante todo su ciclo de vida.

Los identificadores no deberán reutilizarse.

---

## No destrucción del historial

Los cambios deberán preservar:

- versiones;
- procedencia;
- decisiones;
- migraciones;
- sustituciones;
- estados anteriores.

---

## Evolución controlada

Los cambios deberán introducirse mediante:

- propuestas;
- validaciones;
- revisiones;
- aprobación;
- publicación.

---

## Compatibilidad progresiva

Siempre que sea posible, las nuevas versiones deberán conservar compatibilidad hacia atrás.

---

## Trazabilidad total

Todo cambio deberá poder responder:

- qué cambió;
- quién lo cambió;
- cuándo;
- por qué;
- desde qué versión;
- con qué impacto;
- mediante qué proceso.

---

## Separación de responsabilidades

La creación, validación, aprobación y publicación no deberán concentrarse necesariamente en una única función o herramienta.

---

## Calidad continua

La calidad se evaluará durante todo el ciclo de vida.

No únicamente antes de una release.

---

## Seguridad por diseño

Los permisos, la privacidad y la segregación de datos deberán formar parte del modelo desde su origen.

---

## Interoperabilidad

El grafo deberá poder intercambiar conocimiento sin perder:

- identidad;
- contexto;
- procedencia;
- semántica;
- temporalidad.

---

## Explicabilidad

Toda modificación, inferencia o materialización relevante deberá poder explicarse.

---

## Reversibilidad

Los cambios incompatibles deberán disponer, cuando sea viable, de una estrategia de reversión.

---

# Modelo de gobernanza

La gobernanza del Knowledge Graph puede representarse mediante el siguiente ciclo:

```text
Necesidad o incidencia
        │
        ▼
Propuesta de cambio
        │
        ▼
Análisis de impacto
        │
        ▼
Validación automática
        │
        ▼
Revisión semántica
        │
        ▼
Revisión técnica
        │
        ▼
Aprobación
        │
        ▼
Migración o actualización
        │
        ▼
Publicación
        │
        ▼
Supervisión
        │
        ▼
Auditoría
```

---

# Ámbitos de decisión

Las decisiones podrán clasificarse según su alcance.

---

## Decisión local

Afecta a:

- una entidad;
- una afirmación;
- una colección;
- un módulo limitado.

Ejemplo:

```text
Añadir un alias a un ingrediente.
```

---

## Decisión modular

Afecta a un módulo completo.

Ejemplo:

```text
Reorganizar la taxonomía de técnicas culinarias.
```

---

## Decisión transversal

Afecta a varios módulos o servicios.

Ejemplo:

```text
Cambiar la estrategia de representación de relaciones n-arias.
```

---

## Decisión arquitectónica

Afecta al modelo general del Knowledge Graph.

Ejemplo:

```text
Adoptar RDF-star como representación principal de afirmaciones enriquecidas.
```

Las decisiones arquitectónicas deberán documentarse mediante ADR.

---

# Roles

La gobernanza podrá distribuirse entre distintos roles.

---

## Arquitecto del conocimiento

Responsable de:

- coherencia global;
- alineación con el SGCC;
- evolución estructural;
- decisiones transversales;
- revisión de impacto.

---

## Arquitecto ontológico

Responsable de:

- clases;
- propiedades;
- axiomas;
- restricciones;
- alineaciones semánticas;
- consistencia ontológica.

---

## Responsable del Knowledge Graph

Responsable de:

- operación;
- construcción;
- persistencia;
- snapshots;
- publicación;
- rendimiento;
- integridad.

---

## Mantenedor de módulo

Responsable de un dominio concreto.

Ejemplos:

- ingredientes;
- recetas;
- técnicas;
- colecciones;
- documentación.

---

## Revisor semántico

Comprueba:

- significado;
- tipos;
- relaciones;
- ambigüedades;
- duplicidades;
- contexto.

---

## Experto culinario

Valida:

- exactitud gastronómica;
- tradición;
- técnicas;
- ingredientes;
- excepciones;
- seguridad culinaria.

---

## Responsable de calidad

Supervisa:

- validaciones;
- métricas;
- deuda;
- auditorías;
- conformidad;
- regresiones.

---

## Responsable de seguridad

Supervisa:

- permisos;
- privacidad;
- exposición;
- incidentes;
- segregación;
- auditoría de accesos.

---

## Editor de conocimiento

Puede:

- proponer entidades;
- corregir relaciones;
- aportar fuentes;
- mantener documentación;
- registrar deuda.

---

## Agente automatizado

Podrá:

- detectar;
- proponer;
- validar;
- informar;
- materializar.

No deberá aprobar cambios canónicos salvo autorización expresa y controlada.

---

# Matriz de responsabilidades

Una asignación orientativa podrá seguir el modelo RACI.

| Actividad | Arquitecto | Mantenedor | Revisor | Experto | Calidad | Seguridad |
|---|---|---|---|---|---|---|
| Crear entidad | A | R | C | C | I | I |
| Añadir relación | A | R | C | C | I | I |
| Cambiar ontología | R | C | A | C | C | I |
| Aprobar migración | A | R | C | I | C | C |
| Publicar snapshot | A | R | I | I | C | C |
| Resolver conflicto | A | R | C | C | C | I |
| Gestionar incidente | C | R | I | I | C | A |
| Archivar módulo | A | R | C | C | C | I |

Leyenda:

```text
R — Responsible
A — Accountable
C — Consulted
I — Informed
```

---

# Ciclo de vida del grafo

El Knowledge Graph completo podrá encontrarse en distintos estados.

```text
Diseño
  │
  ▼
Construcción
  │
  ▼
Validación
  │
  ▼
Publicado
  │
  ▼
Mantenimiento
  │
  ▼
Deprecado
  │
  ▼
Archivado
```

---

# Ciclo de vida de una entidad

Una entidad podrá recorrer los siguientes estados:

```text
Propuesta
  │
  ▼
Borrador
  │
  ▼
En revisión
  │
  ▼
Activa
  │
  ▼
Disputada
  │
  ▼
Deprecada
  │
  ▼
Archivada
```

---

## Propuesta

La entidad ha sido sugerida.

Aún no pertenece al conocimiento canónico.

---

## Borrador

Dispone de identidad provisional y estructura inicial.

Puede modificarse libremente.

---

## En revisión

Se evalúan:

- identidad;
- tipo;
- definición;
- procedencia;
- posibles duplicados;
- relaciones.

---

## Activa

Forma parte oficialmente del Knowledge Graph.

---

## Disputada

Existen dudas o conflictos sobre:

- identidad;
- clasificación;
- propiedades;
- procedencia;
- significado.

---

## Deprecada

No deberá utilizarse en nuevas afirmaciones.

Se conserva por compatibilidad.

---

## Archivada

Permanece únicamente para reconstrucción histórica o auditoría.

---

# Ciclo de vida de una afirmación

Estados recomendados:

```text
propuesta
extraida
pendiente_revision
aceptada
confirmada
inferida
disputada
rechazada
deprecada
archivada
```

---

## Extraída

Procede de un proceso automático o documental.

No ha sido validada.

---

## Aceptada

Ha superado validaciones suficientes para incorporarse.

---

## Confirmada

Dispone de:

- revisión humana;
- evidencia sólida;
- contexto definido;
- procedencia completa.

---

## Inferida

Ha sido derivada mediante una regla o motor.

---

## Rechazada

La afirmación se conserva para trazabilidad, pero no se considera válida.

---

# Ciclo de vida de un subgrafo

Un subgrafo podrá ser:

```text
definido
resuelto
materializado
publicado
desactualizado
invalidado
archivado
```

---

# Ciclo de vida de una inferencia

```text
generada
validada
materializada
activa
obsoleta
invalidada
archivada
```

Una inferencia deberá invalidarse si deja de cumplirse cualquiera de sus premisas.

---

# Solicitudes de cambio

Todo cambio relevante deberá registrarse mediante una solicitud.

Formato conceptual:

```yaml
change_request:
  id: KG-CR-0001
  type: ontology_change
  title: Incorporar la clase FermentoIniciador
  status: proposed

  motivation: >
    Diferenciar cultivos iniciadores de ingredientes fermentados.

  affected_elements:
    - ONT-CLS-FERMENTED-INGREDIENT
    - KG-INGREDIENTS

  impact:
    semantic: high
    technical: medium
    compatibility: compatible

  requested_by: knowledge_editor
  requested_at: 2026-07-31
```

---

# Tipos de solicitud

Podrán existir solicitudes para:

- nueva entidad;
- nueva relación;
- modificación;
- fusión;
- división;
- deprecación;
- eliminación lógica;
- migración;
- alineación externa;
- cambio ontológico;
- nueva regla;
- publicación;
- restauración.

---

# Análisis de impacto

Antes de aprobar un cambio deberá analizarse su impacto sobre:

- entidades;
- relaciones;
- afirmaciones;
- inferencias;
- colecciones;
- consultas;
- snapshots;
- índices RAG;
- agentes;
- APIs;
- documentación;
- interoperabilidad.

---

## Impacto semántico

Evalúa si cambia:

- significado;
- clasificación;
- restricciones;
- dominio;
- rango;
- contexto.

---

## Impacto estructural

Evalúa si cambia:

- modelo de nodos;
- forma de relaciones;
- propiedades;
- identificadores;
- esquemas.

---

## Impacto operativo

Evalúa:

- pipelines;
- rendimiento;
- almacenamiento;
- consultas;
- servicios.

---

## Impacto histórico

Evalúa si afecta a:

- snapshots;
- versiones;
- auditorías;
- reproducibilidad.

---

## Impacto inteligente

Evalúa:

- inferencias;
- GraphRAG;
- embeddings;
- agentes;
- conjuntos de evaluación.

---

# Clasificación de cambios

Los cambios podrán clasificarse como:

```text
editorial
compatible
potencialmente_incompatible
incompatible
critico
```

---

# Cambio editorial

No afecta al significado.

Ejemplos:

- corrección ortográfica;
- traducción;
- mejora de descripción;
- ejemplo adicional.

---

# Cambio compatible

Añade conocimiento sin invalidar lo existente.

Ejemplos:

- nueva entidad;
- nueva relación opcional;
- nueva fuente;
- nuevo alias;
- nueva subclase compatible.

---

# Cambio potencialmente incompatible

Puede modificar resultados o inferencias.

Ejemplos:

- cambiar el tipo de una entidad;
- ampliar dominio de una propiedad;
- cambiar una regla;
- modificar una política de contexto.

---

# Cambio incompatible

Invalida consumidores o interpretaciones anteriores.

Ejemplos:

- cambiar el significado de un predicado;
- eliminar una clase;
- alterar una URI canónica;
- modificar la dirección semántica de una relación;
- cambiar el modelo de afirmaciones.

---

# Cambio crítico

Afecta a:

- seguridad alimentaria;
- privacidad;
- integridad global;
- identidad;
- trazabilidad;
- publicación pública.

Requerirá revisión reforzada.

---

# Versionado global

El Knowledge Graph utilizará versionado semántico:

```text
MAJOR.MINOR.PATCH
```

---

## Versión PATCH

Se incrementará ante cambios sin impacto semántico relevante.

Ejemplos:

- correcciones documentales;
- metadatos;
- nuevas etiquetas;
- errores menores.

---

## Versión MINOR

Se incrementará ante ampliaciones compatibles.

Ejemplos:

- nuevas entidades;
- nuevas relaciones;
- nuevos módulos;
- nuevas consultas;
- nuevas reglas compatibles.

---

## Versión MAJOR

Se incrementará ante cambios incompatibles.

Ejemplos:

- modificación del metamodelo;
- cambio de representación canónica;
- eliminación de predicados;
- redefinición de identidad;
- cambios ontológicos incompatibles.

---

# Versionado de módulos

Cada módulo podrá evolucionar de forma independiente.

Ejemplo:

```yaml
module:
  id: KG-INGREDIENTS
  version: 2.3.0
  compatible_with:
    ontology: ">=2.0.0 <3.0.0"
```

---

# Versionado de entidades

Una entidad podrá mantener identidad y poseer sucesivas revisiones.

Ejemplo:

```text
ING-0008

├── revisión 1
├── revisión 2
└── revisión 3
```

---

## Cuándo crear nueva versión

Se creará nueva versión cuando cambien:

- definición;
- tipos relevantes;
- relaciones canónicas;
- contexto;
- procedencia principal;
- estado.

---

## Cuándo crear nueva identidad

Se creará una entidad nueva cuando:

- cambie el significado central;
- se descubra que se mezclaban dos conceptos;
- aparezca una variante con identidad propia;
- la entidad original no pueda representar el nuevo concepto sin ambigüedad.

---

# Versionado de afirmaciones

Una afirmación podrá:

- corregirse;
- sustituirse;
- contextualizarse;
- dividirse;
- invalidarse.

La afirmación anterior deberá conservarse.

---

# Versionado de reglas

Toda regla deberá versionarse independientemente.

Las inferencias deberán registrar qué versión de la regla utilizaron.

---

# Versionado de consultas

Las consultas canónicas deberán versionarse cuando cambie:

- su semántica;
- su ámbito;
- sus filtros;
- el ranking;
- la estructura del resultado.

---

# Versionado de snapshots

Todo snapshot será inmutable.

Una corrección generará un snapshot nuevo.

---

# Compatibilidad

Cada versión deberá declarar su compatibilidad.

Valores recomendados:

```text
backward_compatible
forward_compatible
partially_compatible
incompatible
```

---

# Compatibilidad hacia atrás

Los consumidores antiguos pueden utilizar la nueva versión sin cambios.

---

# Compatibilidad hacia delante

Los consumidores nuevos pueden interpretar versiones anteriores.

---

# Compatibilidad parcial

Algunas capacidades requieren adaptación.

---

# Matriz de compatibilidad

Podrá mantenerse una tabla como:

| Grafo | Ontología | API | Consultas | Razonador |
|---|---|---|---|---|
| KG 1.x | ONT 1.x | API 1.x | QRY 1.x | REASONER 1.x |
| KG 2.x | ONT 2.x | API 2.x | QRY 2.x | REASONER 2.x |

---

# Changelog

Cada release deberá incluir un historial comprensible.

Ejemplo:

```markdown
## 2.1.0 — 2026-08-15

### Añadido

- Nuevas entidades de fermentación.
- Relaciones entre cultivos iniciadores y procesos.

### Modificado

- Ampliado el rango de `uses_culture`.

### Deprecado

- Predicado `related_fermentation`.

### Migración

- Sustituir por `uses_culture` o `produces_fermentation`.
```

---

# Migraciones

Una migración transforma una versión del grafo en otra.

---

# Tipos de migración

---

## Migración de esquema

Modifica:

- clases;
- propiedades;
- estructura de nodos;
- estructura de relaciones.

---

## Migración de datos

Modifica instancias o afirmaciones.

---

## Migración semántica

Cambia interpretación o clasificación.

---

## Migración de identidad

Fusiona, divide o sustituye entidades.

---

## Migración de tecnología

Traslada el grafo entre:

- RDF;
- property graph;
- base híbrida;
- otro motor.

---

## Migración de procedencia

Actualiza o completa información de origen.

---

# Contrato de migración

Toda migración deberá declarar:

```yaml
migration:
  id: KG-MIG-0001
  from_version: 1.4.0
  to_version: 2.0.0
  type: semantic

  description: >
    Sustituir la relación genérica related_to por predicados específicos.

  affected_predicates:
    - related_to

  strategy:
    - classify_existing_relations
    - create_specific_statements
    - deprecate_generic_statements

  reversible: true
  rollback: KG-MIG-0001-ROLLBACK
```

---

# Fases de migración

```text
Diseño
  │
  ▼
Simulación
  │
  ▼
Validación
  │
  ▼
Ejecución
  │
  ▼
Verificación
  │
  ▼
Publicación
  │
  ▼
Supervisión
```

---

# Simulación

Toda migración relevante debería probarse sobre:

- snapshot;
- entorno aislado;
- subconjunto representativo.

---

# Migración en seco

El modo `dry-run` deberá informar:

- elementos afectados;
- cambios previstos;
- conflictos;
- pérdidas;
- tiempo estimado.

---

# Reversión

Toda migración compatible con reversión deberá incluir:

- estado previo;
- script o procedimiento;
- condiciones;
- limitaciones.

---

# Migraciones irreversibles

Las migraciones irreversibles requerirán:

- aprobación explícita;
- snapshot previo;
- copia de seguridad;
- documentación;
- plan de contingencia.

---

# Refactorización del grafo

La refactorización mejora la estructura sin cambiar su significado esencial.

---

# Tipos de refactorización

- renombrado;
- extracción de clase;
- extracción de relación;
- fusión de duplicados;
- división de entidad;
- normalización de literales;
- reestructuración modular;
- sustitución de relación genérica;
- contextualización de afirmaciones;
- reificación de relaciones complejas.

---

# Refactorización semántica

Toda refactorización deberá demostrar que conserva:

- significado;
- identidad;
- procedencia;
- consultas relevantes;
- inferencias esperadas.

---

# Pruebas de equivalencia

Podrán utilizarse:

- consultas canónicas;
- golden datasets;
- hashes semánticos;
- comparación de subgrafos;
- pruebas de inferencia.

---

# Fusión de entidades

La fusión deberá identificar:

- entidad canónica;
- duplicados;
- relaciones redirigidas;
- alias conservados;
- procedencia;
- conflictos;
- fecha.

---

## Ejemplo

```text
ING-0042
ING-0108
        │
        ▼
ING-0008
```

Las entidades fusionadas deberán quedar:

```text
deprecadas
```

y enlazadas mediante:

```text
merged_into
```

---

# División de entidades

Una entidad deberá dividirse cuando represente varios conceptos.

Ejemplo:

```text
Curry
```

podría dividirse en:

- mezcla de especias;
- plato;
- hoja de curry;
- categoría culinaria.

---

## Proceso de división

```text
Detectar ambigüedad
  │
  ▼
Crear nuevas entidades
  │
  ▼
Clasificar relaciones
  │
  ▼
Redistribuir afirmaciones
  │
  ▼
Deprecar entidad ambigua
  │
  ▼
Conservar historial
```

---

# Deprecación

La deprecación será preferible a la eliminación física.

Un elemento deprecado deberá indicar:

- motivo;
- fecha;
- versión;
- sustituto;
- instrucciones de migración;
- fecha prevista de retirada.

---

# Retirada

Un elemento retirado no deberá:

- utilizarse en nuevas afirmaciones;
- participar en nuevas inferencias;
- aparecer como opción canónica.

Podrá seguir siendo resoluble históricamente.

---

# Eliminación física

Solo se permitirá cuando:

- el elemento nunca fue publicado;
- no posee referencias;
- no participa en snapshots;
- fue creado por error;
- existe aprobación formal.

---

# Restauración

Un elemento archivado o deprecado podrá restaurarse.

La restauración deberá:

- justificar el motivo;
- asignar nueva versión;
- ejecutar validaciones;
- revisar compatibilidad.

---

# Calidad del Knowledge Graph

La calidad deberá evaluarse desde varias dimensiones.

```text
Calidad
   │
   ├── estructural
   ├── semántica
   ├── contextual
   ├── temporal
   ├── documental
   ├── operacional
   ├── analítica
   └── de seguridad
```

---

# Calidad estructural

Evalúa:

- identificadores;
- tipos;
- referencias;
- cardinalidades;
- formatos;
- ausencia de ciclos inválidos;
- integridad de nodos y relaciones.

---

# Calidad semántica

Evalúa:

- significado;
- precisión;
- coherencia;
- dominio;
- rango;
- jerarquías;
- equivalencias;
- consistencia ontológica.

---

# Calidad contextual

Evalúa:

- contexto declarado;
- fronteras;
- excepciones;
- aplicabilidad;
- no generalización indebida.

---

# Calidad temporal

Evalúa:

- validez;
- intervalos;
- estados;
- versiones;
- coherencia histórica;
- bitemporalidad.

---

# Calidad documental

Evalúa:

- fuentes;
- fragmentos;
- enlaces;
- documentación;
- explicaciones;
- cobertura.

---

# Calidad de procedencia

Evalúa:

- fuente identificada;
- agente;
- actividad;
- método;
- licencia;
- cadena de derivación.

---

# Calidad operacional

Evalúa:

- disponibilidad;
- latencia;
- reproducibilidad;
- snapshots;
- estabilidad;
- errores;
- rendimiento.

---

# Calidad analítica

Evalúa si el grafo permite:

- responder consultas;
- generar métricas;
- detectar patrones;
- explicar resultados;
- alimentar RAG.

---

# Calidad de seguridad

Evalúa:

- permisos;
- segregación;
- exposición;
- auditoría;
- privacidad;
- cifrado;
- acceso a inferencias sensibles.

---

# Dimensiones de calidad

El SGCC podrá adoptar las siguientes dimensiones:

- completitud;
- corrección;
- consistencia;
- actualidad;
- unicidad;
- trazabilidad;
- conectividad;
- relevancia;
- autoridad;
- accesibilidad;
- reproducibilidad;
- explicabilidad.

---

# Completitud

Mide si existe el conocimiento esperado.

Ejemplos:

- recetas sin ingredientes;
- técnicas sin resultado;
- entidades sin fuente;
- colecciones sin miembros.

---

# Corrección

Mide si el conocimiento representado es verdadero o adecuado según sus fuentes y contexto.

---

# Consistencia

Mide ausencia de contradicciones no gestionadas.

---

# Actualidad

Mide si el conocimiento está vigente.

---

# Unicidad

Mide ausencia de duplicados.

---

# Trazabilidad

Mide si puede reconstruirse el origen y evolución.

---

# Conectividad

Mide integración de las entidades dentro del grafo.

---

# Explicabilidad

Mide si las relaciones e inferencias pueden justificarse.

---

# Métricas estructurales

Ejemplos:

```text
Número de nodos

Número de relaciones

Número de afirmaciones

Densidad

Grado medio

Número de componentes conexas

Número de ciclos inválidos
```

---

# Métricas de integridad

Ejemplos:

```text
Entidades sin tipo

Entidades sin etiqueta

Relaciones con sujeto inexistente

Relaciones con objeto inexistente

Afirmaciones sin predicado válido

Relaciones fuera de dominio o rango
```

---

# Métricas de procedencia

Ejemplos:

```text
Porcentaje de afirmaciones con fuente

Porcentaje con fragmento exacto

Número medio de evidencias

Fuentes externas sin licencia

Afirmaciones generadas automáticamente sin revisión
```

---

# Métricas semánticas

Ejemplos:

```text
Clases sin instancias

Propiedades sin uso

Relaciones genéricas

Equivalencias dudosas

Clases insatisfacibles

Conflictos ontológicos
```

---

# Métricas de conectividad

Ejemplos:

```text
Nodos huérfanos

Nodos débilmente conectados

Subgrafos aislados

Cobertura relacional

Distancia media entre dominios
```

---

# Métricas temporales

Ejemplos:

```text
Edad media de las afirmaciones

Relaciones expiradas

Entidades sin revisión reciente

Frecuencia de cambios

Tiempo medio de resolución de conflictos
```

---

# Métricas de inferencia

Ejemplos:

```text
Inferencias activas

Inferencias invalidadas

Profundidad media

Reglas sin uso

Inferencias sin explicación

Porcentaje de inferencias materializadas
```

---

# Métricas de uso

Ejemplos:

```text
Consultas por entidad

Colecciones más utilizadas

Caminos más consultados

Entidades sin consultas

Subgrafos más recuperados

Uso por agentes
```

---

# Indicadores de calidad mínima

Podrán establecerse umbrales como:

```text
Afirmaciones sin fuente = 0 %

Identificadores duplicados = 0

Referencias rotas = 0

Ciclos jerárquicos inválidos = 0

Inferencias sin regla = 0

Entidades activas sin tipo = 0
```

---

# Quality Gates

La publicación deberá bloquearse cuando se incumplan umbrales críticos.

Ejemplos:

- identificadores duplicados;
- referencias rotas;
- inconsistencia ontológica;
- migración incompleta;
- pérdida de procedencia;
- filtrado de seguridad fallido;
- inferencias críticas sin explicación.

---

# Advertencias de calidad

Podrán no bloquear la publicación, pero deberán registrarse.

Ejemplos:

- nodo huérfano;
- baja conectividad;
- entidad sin traducción;
- fuente única;
- confianza baja;
- módulo sin mantenedor.

---

# Informes de calidad

Cada release podrá generar un informe con:

- estado global;
- errores;
- advertencias;
- métricas;
- diferencias;
- deuda;
- recomendaciones.

---

# Deuda del Knowledge Graph

La deuda del grafo representa carencias o decisiones provisionales que dificultan su evolución futura.

---

# Tipos de deuda

---

## Deuda estructural

Ejemplos:

- relaciones sin tipos claros;
- nodos demasiado genéricos;
- reificaciones inconsistentes;
- modelos duplicados.

---

## Deuda semántica

Ejemplos:

- relaciones ambiguas;
- clases solapadas;
- conceptos sin definición;
- equivalencias aproximadas usadas como exactas.

---

## Deuda de identidad

Ejemplos:

- duplicados;
- entidades sin URI;
- identificadores provisionales;
- aliases sin resolver.

---

## Deuda relacional

Ejemplos:

- nodos huérfanos;
- relaciones faltantes;
- uso excesivo de `related_to`;
- inversas incoherentes.

---

## Deuda de procedencia

Ejemplos:

- fuentes incompletas;
- fragmentos no localizados;
- autoría desconocida;
- importaciones sin licencia.

---

## Deuda temporal

Ejemplos:

- afirmaciones sin vigencia;
- estados históricos perdidos;
- versiones no reconstruibles.

---

## Deuda de calidad

Ejemplos:

- validaciones pendientes;
- conflictos sin resolver;
- métricas no implementadas;
- pruebas insuficientes.

---

## Deuda operativa

Ejemplos:

- snapshots lentos;
- consultas costosas;
- pipelines manuales;
- índices desactualizados.

---

## Deuda de interoperabilidad

Ejemplos:

- mapeos externos incompletos;
- dependencias propietarias;
- exportaciones con pérdida semántica.

---

## Deuda de IA

Ejemplos:

- embeddings sin versión;
- conjuntos de evaluación insuficientes;
- inferencias probabilísticas sin revisión;
- agentes sin políticas claras.

---

# Registro de deuda

Cada elemento deberá incluir:

```yaml
knowledge_graph_debt:
  id: KG-DEBT-0001
  type: semantic
  title: Sustituir relaciones related_to
  priority: high
  status: open

  affected_elements:
    - STM-0041
    - STM-0052

  impact:
    query_precision: high
    inference: medium

  proposed_action: >
    Reclasificar mediante predicados específicos.

  owner: knowledge_architect
  created_at: 2026-07-31
```

---

# Prioridad de deuda

Niveles recomendados:

```text
critica
alta
media
baja
oportunidad
```

---

# Priorización basada en riesgo

La prioridad deberá considerar:

- seguridad;
- impacto semántico;
- número de elementos afectados;
- frecuencia de uso;
- coste de corrección;
- dependencia de otras tareas.

---

# Pago de deuda

El pago de deuda deberá:

- asociarse a una versión;
- incluir pruebas;
- actualizar métricas;
- registrar impacto;
- mantener trazabilidad.

---

# Auditoría

Toda operación relevante deberá ser auditable.

---

# Eventos auditables

Incluyen:

- creación;
- modificación;
- deprecación;
- fusión;
- división;
- migración;
- publicación;
- importación;
- inferencia;
- aprobación;
- acceso sensible;
- exportación;
- fallo de validación.

---

# Registro de auditoría

Cada evento podrá incluir:

```yaml
audit_event:
  id: AUD-000145
  action: statement_updated
  actor: user-001
  timestamp: 2026-07-31T19:30:00+02:00

  target:
    type: statement
    id: STM-000123

  before_hash: sha256:...
  after_hash: sha256:...

  reason: Corrección de procedencia
  change_request: KG-CR-0012
```

---

# Inmutabilidad de auditoría

Los registros de auditoría no deberán modificarse.

Las correcciones deberán añadirse como nuevos eventos.

---

# Integridad de auditoría

Podrán utilizarse:

- hashes;
- firmas;
- almacenamiento append-only;
- sellado temporal;
- snapshots.

---

# Auditoría semántica

Además del cambio técnico, deberá registrarse:

- significado anterior;
- significado nuevo;
- impacto;
- decisión;
- responsable.

---

# Auditoría de agentes

Las acciones de agentes deberán registrar:

- agente;
- modelo;
- versión;
- herramientas;
- entradas;
- salidas;
- fuentes;
- propuestas;
- decisión humana posterior.

---

# Auditoría de consultas sensibles

Las consultas sobre ámbitos restringidos podrán registrar:

- usuario;
- motivo;
- ámbito;
- resultados;
- exportaciones;
- política aplicada.

---

# Seguridad

El Knowledge Graph deberá aplicar seguridad en múltiples niveles.

---

# Autenticación

Todo actor no público deberá estar identificado.

---

# Autorización

Los permisos podrán aplicarse a:

- módulos;
- subgrafos;
- entidades;
- relaciones;
- propiedades;
- afirmaciones;
- snapshots;
- consultas;
- herramientas.

---

# Modelo RBAC

Los permisos podrán basarse en roles.

Ejemplos:

```text
reader
editor
reviewer
maintainer
architect
security_auditor
publisher
```

---

# Modelo ABAC

Podrán aplicarse atributos como:

- estado;
- sensibilidad;
- colección;
- propietario;
- contexto;
- finalidad;
- licencia.

---

# Permisos por capa

Un usuario podrá tener acceso a:

- conocimiento validado;
- pero no a hipótesis;
- o a fuentes restringidas;
- o a datos personales.

---

# Seguridad de inferencias

Una inferencia no deberá revelar conocimiento derivado de premisas a las que el usuario no tiene acceso.

---

# Seguridad de caminos

Un camino podrá revelar entidades ocultas.

El filtrado deberá aplicarse antes de construir la explicación final.

---

# Seguridad de métricas

Incluso los contadores pueden revelar información sensible.

Ejemplo:

```text
Número de recetas médicas privadas
```

---

# Seguridad de embeddings

Los vectores deberán:

- heredar permisos;
- evitar indexación de contenido no autorizado;
- segregarse por ámbito cuando proceda;
- invalidarse ante cambios de acceso.

---

# Seguridad de exportaciones

Toda exportación deberá comprobar:

- actor;
- finalidad;
- licencia;
- permisos;
- sensibilidad;
- formato;
- trazabilidad.

---

# Clasificación de sensibilidad

Valores posibles:

```text
publica
interna
restringida
confidencial
personal
critica
```

---

# Privacidad

Los subgrafos personales deberán:

- separarse del conocimiento global;
- aplicar minimización;
- definir retención;
- permitir eliminación;
- registrar consentimiento cuando proceda;
- limitar reutilización.

---

# Datos personales

No deberán integrarse en el grafo global salvo necesidad y base legítima.

---

# Cifrado

Podrá aplicarse:

- en tránsito;
- en reposo;
- en copias;
- en exportaciones;
- en cachés.

---

# Gestión de secretos

Las credenciales, claves y tokens no deberán almacenarse como conocimiento del grafo.

---

# Seguridad del pipeline

El pipeline deberá protegerse frente a:

- fuentes manipuladas;
- inyección de datos;
- esquemas maliciosos;
- consultas no autorizadas;
- importaciones masivas;
- archivos corruptos.

---

# Validación de fuentes

Toda fuente externa deberá comprobar:

- procedencia;
- formato;
- licencia;
- integridad;
- confianza;
- contenido.

---

# Prompt injection

El contenido recuperado para agentes deberá tratarse como datos.

No deberá poder modificar políticas del sistema.

---

# Publicación

El Knowledge Graph podrá publicarse en distintos niveles.

---

## Publicación interna

Disponible para el equipo.

---

## Publicación restringida

Disponible para determinados grupos.

---

## Publicación pública

Disponible externamente.

---

## Publicación experimental

Incluye elementos no estables.

Deberá etiquetarse claramente.

---

# Artefactos de publicación

Una release podrá incluir:

```text
ontology.ttl

knowledge-graph.nq

shapes.ttl

rules.yaml

collections.yaml

manifest.yaml

CHANGELOG.md

quality-report.md

migration-guide.md
```

---

# Manifiesto de publicación

```yaml
release:
  id: KG-REL-2.0.0
  version: 2.0.0
  status: stable
  published_at: 2026-08-31

  ontology_version: 2.0.0
  graph_snapshot: KG-SNAP-20260831-001

  formats:
    - turtle
    - json-ld
    - n-quads

  quality:
    status: passed
    report: quality-report.md

  compatibility:
    previous_version: 1.4.0
    level: partially_compatible
```

---

# Inmutabilidad de releases

Una release publicada deberá ser inmutable.

Las correcciones generarán una nueva versión.

---

# Canal latest

Podrá existir una referencia a la versión actual.

No deberá utilizarse cuando se requiera reproducibilidad.

---

# Desreferenciación

Las URI públicas deberían poder devolver:

- HTML;
- JSON-LD;
- Turtle;
- metadatos.

---

# Licencias

Toda publicación deberá declarar:

- licencia global;
- licencias de fuentes externas;
- restricciones;
- atribuciones;
- incompatibilidades.

---

# Interoperabilidad

El Knowledge Graph deberá poder integrarse con otros ecosistemas.

---

# Niveles de interoperabilidad

```text
Sintáctica
Semántica
Técnica
Organizativa
Legal
```

---

# Interoperabilidad sintáctica

Compartir formatos.

Ejemplos:

- RDF;
- JSON-LD;
- Turtle;
- CSV;
- GraphML.

---

# Interoperabilidad semántica

Compartir significado mediante:

- ontologías;
- vocabularios;
- mapeos;
- URI;
- axiomas.

---

# Interoperabilidad técnica

Compartir:

- APIs;
- endpoints;
- protocolos;
- autenticación;
- eventos.

---

# Interoperabilidad organizativa

Compartir:

- procesos;
- responsabilidades;
- versiones;
- gobernanza.

---

# Interoperabilidad legal

Respetar:

- licencias;
- derechos;
- privacidad;
- condiciones de reutilización.

---

# Alineaciones externas

Toda alineación deberá registrar:

```yaml
alignment:
  internal: ONT-CLS-RECIPE
  external: schema:Recipe
  relation: close_match

  external_vocabulary:
    name: Schema.org
    version: 29.0

  confidence: 0.92
  reviewed_by: semantic_reviewer
```

---

# Tipos de correspondencia

```text
same_as
exact_match
close_match
broader_match
narrower_match
related_match
incompatible
```

---

# Uso de `same_as`

Solo deberá utilizarse para identidad estricta.

No para similitud.

---

# Importaciones externas

Las importaciones deberán conservar:

- identificador externo;
- versión;
- licencia;
- fecha;
- mapeo;
- transformaciones;
- procedencia.

---

# Sincronización externa

La sincronización deberá definir:

- dirección;
- frecuencia;
- prioridad;
- conflicto;
- versión;
- política de eliminación.

---

# Conflictos de sincronización

Políticas posibles:

```text
internal_wins
external_wins
latest_wins
authority_wins
manual_review
preserve_both
```

---

# Portabilidad

El grafo deberá poder exportarse a formatos abiertos.

Toda tecnología propietaria deberá disponer de estrategia de salida.

---

# Pruebas de interoperabilidad

Deberán comprobar:

- round-trip;
- pérdida semántica;
- mapeos;
- identificadores;
- contexto;
- procedencia;
- inferencias.

---

# Gestión de incidentes

Un incidente es un evento que compromete:

- integridad;
- disponibilidad;
- seguridad;
- calidad;
- consistencia;
- publicación.

---

# Tipos de incidente

---

## Incidente de integridad

Ejemplos:

- corrupción;
- referencias rotas;
- pérdida de nodos;
- relaciones duplicadas.

---

## Incidente semántico

Ejemplos:

- tipo incorrecto;
- regla errónea;
- inferencia falsa;
- equivalencia indebida.

---

## Incidente de seguridad

Ejemplos:

- acceso no autorizado;
- fuga;
- exportación indebida;
- exposición de subgrafos.

---

## Incidente operacional

Ejemplos:

- caída del servicio;
- consulta bloqueada;
- snapshot fallido;
- índice inconsistente.

---

## Incidente de procedencia

Ejemplos:

- fuente perdida;
- licencia desconocida;
- atribución incorrecta.

---

# Severidad

Niveles recomendados:

```text
SEV-1 critica
SEV-2 alta
SEV-3 media
SEV-4 baja
```

---

# Flujo de gestión

```text
Detección
  │
  ▼
Contención
  │
  ▼
Diagnóstico
  │
  ▼
Corrección
  │
  ▼
Recuperación
  │
  ▼
Validación
  │
  ▼
Postmortem
```

---

# Contención

Podrá incluir:

- bloquear publicación;
- deshabilitar inferencias;
- revertir snapshot;
- aislar módulo;
- revocar permisos;
- congelar sincronización.

---

# Recuperación

Podrá realizarse desde:

- último snapshot válido;
- log de eventos;
- copia de seguridad;
- versión Git;
- exportación inmutable.

---

# Postmortem

Todo incidente relevante deberá documentar:

- causa raíz;
- impacto;
- detección;
- respuesta;
- recuperación;
- acciones preventivas.

---

# Continuidad y recuperación

El sistema deberá disponer de:

- copias;
- snapshots;
- redundancia;
- pruebas de restauración;
- objetivos RPO y RTO.

---

# RPO

Recovery Point Objective.

Define cuánta pérdida temporal de cambios se considera aceptable.

---

# RTO

Recovery Time Objective.

Define cuánto tiempo puede permanecer indisponible el sistema.

---

# Copias de seguridad

Deberán incluir:

- datos;
- ontología;
- reglas;
- configuraciones;
- auditoría;
- metadatos;
- manifest.

---

# Pruebas de restauración

No será suficiente crear copias.

Deberán probarse restauraciones periódicas.

---

# Observabilidad de gobernanza

La gobernanza deberá producir métricas propias.

---

# Métricas de cambio

Ejemplos:

- cambios por versión;
- solicitudes abiertas;
- tiempo medio de aprobación;
- migraciones pendientes;
- rollbacks;
- conflictos.

---

# Métricas de revisión

Ejemplos:

- elementos pendientes;
- tiempo de revisión;
- tasa de rechazo;
- propuestas automatizadas aceptadas;
- revisiones por módulo.

---

# Métricas de deuda

Ejemplos:

- deuda total;
- deuda crítica;
- edad media;
- tasa de resolución;
- deuda por módulo.

---

# Métricas de publicación

Ejemplos:

- frecuencia;
- fallos;
- compatibilidad;
- duración del pipeline;
- artefactos publicados.

---

# Dashboards de gobernanza

Podrán mostrar:

- estado de releases;
- deuda;
- incidentes;
- calidad;
- migraciones;
- responsables;
- módulos sin revisión;
- elementos deprecados.

---

# Alertas

Ejemplos:

- aumento de deuda crítica;
- módulo sin mantenedor;
- calidad por debajo del umbral;
- snapshot no generado;
- versión incompatible;
- fuente externa caducada;
- elemento deprecado todavía utilizado.

---

# Automatización de gobernanza

Podrán automatizarse:

- validaciones;
- análisis de impacto;
- detección de dependencias;
- generación de changelog;
- informes de calidad;
- comprobación de compatibilidad;
- notificaciones;
- generación de snapshots;
- publicación.

---

# Pipeline de gobernanza

```text
Pull Request
     │
     ▼
Validación estructural
     │
     ▼
Validación ontológica
     │
     ▼
Pruebas de consultas
     │
     ▼
Pruebas de inferencia
     │
     ▼
Análisis de impacto
     │
     ▼
Informe de calidad
     │
     ▼
Revisión humana
     │
     ▼
Merge
     │
     ▼
Snapshot
     │
     ▼
Publicación
```

---

# Bloqueos del pipeline

El pipeline deberá bloquear cambios cuando exista:

- error estructural;
- inconsistencia;
- referencia rota;
- prueba crítica fallida;
- pérdida de procedencia;
- permiso inválido;
- incompatibilidad no declarada;
- migración ausente;
- violación de licencia.

---

# Revisiones manuales obligatorias

Serán obligatorias para:

- cambios ontológicos;
- fusiones;
- divisiones;
- seguridad alimentaria;
- datos personales;
- cambios de identidad;
- migraciones incompatibles;
- publicación pública.

---

# ADR

Deberá crearse un ADR cuando una decisión afecte a:

- representación principal;
- tecnología de grafo;
- estrategia de identidad;
- modelo de afirmaciones;
- versionado;
- inferencia;
- publicación;
- seguridad;
- interoperabilidad;
- estrategia RAG o agentes.

---

# BITÁCORA

Los hitos relevantes deberán registrarse en la BITÁCORA.

Ejemplos:

- primera publicación;
- cambio de versión mayor;
- incorporación de un módulo;
- migración;
- incidente;
- nueva capacidad de razonamiento.

---

# DECISIONS_SUMMARY

Las decisiones transversales deberán resumirse en el documento correspondiente de gobernanza.

---

# Madurez del Knowledge Graph

La madurez podrá evaluarse mediante niveles.

---

# Nivel 1 — Grafo documental

Características:

- nodos básicos;
- relaciones explícitas;
- fuentes;
- generación desde documentos;
- navegación simple.

---

# Nivel 2 — Grafo estructurado

Añade:

- tipos;
- identificadores;
- validación;
- módulos;
- snapshots;
- relaciones contextualizadas.

---

# Nivel 3 — Grafo semántico

Añade:

- ontología;
- restricciones;
- inferencias básicas;
- SHACL;
- consultas semánticas;
- alineaciones.

---

# Nivel 4 — Grafo operativo

Añade:

- APIs;
- actualizaciones incrementales;
- observabilidad;
- calidad;
- seguridad;
- materializaciones;
- colecciones dinámicas.

---

# Nivel 5 — Grafo inteligente gobernado

Añade:

- GraphRAG;
- agentes;
- razonamiento híbrido;
- explicabilidad;
- evaluación;
- gobernanza completa;
- detección de deriva;
- interoperabilidad avanzada.

---

# Criterios de madurez

Podrán evaluarse:

- cobertura;
- calidad;
- automatización;
- interoperabilidad;
- seguridad;
- versionado;
- uso;
- explicabilidad;
- deuda;
- gobernanza.

---

# Madurez por módulo

Cada módulo podrá poseer un nivel distinto.

Ejemplo:

```text
Ingredientes: Nivel 4
Recetas: Nivel 3
Técnicas: Nivel 2
Nutrición: Nivel 1
```

---

# Roadmap de madurez

La evolución deberá priorizar:

1. identidad;
2. procedencia;
3. validación;
4. versionado;
5. consulta;
6. inferencia;
7. RAG;
8. agentes.

---

# Perfiles de conformidad

El SGCC podrá definir varios perfiles.

---

# Perfil documental

Requiere:

- entidades;
- documentos;
- identificadores;
- relaciones básicas;
- procedencia.

---

# Perfil estructural

Añade:

- tipos;
- dominio;
- rango;
- validación;
- versiones;
- subgrafos.

---

# Perfil semántico

Añade:

- ontología;
- axiomas;
- SHACL;
- equivalencias;
- inferencia;
- explicación.

---

# Perfil operacional

Añade:

- APIs;
- snapshots;
- automatización;
- observabilidad;
- seguridad;
- rendimiento.

---

# Perfil interoperable

Añade:

- URI;
- RDF;
- JSON-LD;
- mapeos;
- licencias;
- exportaciones;
- round-trip.

---

# Perfil inteligente

Añade:

- GraphRAG;
- embeddings;
- agentes;
- evaluación;
- auditoría de modelos;
- políticas de abstención.

---

# Perfil crítico

Aplicable a seguridad alimentaria u otros ámbitos de alto impacto.

Requiere:

- fuentes autorizadas;
- revisión humana;
- trazabilidad completa;
- inferencia determinista;
- seguridad reforzada;
- pruebas específicas;
- gestión formal de incidentes.

---

# Conformidad de entidad

Una entidad será conforme cuando:

- tenga identidad persistente;
- posea tipo;
- tenga etiqueta;
- disponga de estado;
- conserve procedencia;
- no duplique otra entidad;
- respete la ontología;
- pueda versionarse.

---

# Conformidad de relación

Una relación será conforme cuando:

- utilice predicado reconocido;
- conecte entidades válidas;
- respete dominio y rango;
- conserve contexto cuando proceda;
- conserve procedencia;
- tenga estado;
- respete temporalidad.

---

# Conformidad de afirmación

Una afirmación será conforme cuando:

- sea auditable;
- tenga fuente o método;
- diferencie hecho, hipótesis o inferencia;
- conserve contexto;
- posea versión o vigencia;
- permita conflicto sin sobrescritura;
- pueda invalidarse.

---

# Conformidad de snapshot

Un snapshot será conforme cuando:

- sea inmutable;
- declare versión;
- incluya fecha;
- identifique fuentes;
- tenga hash;
- pueda restaurarse;
- disponga de manifiesto;
- haya superado validación.

---

# Conformidad de migración

Una migración será conforme cuando:

- declare origen y destino;
- incluya análisis de impacto;
- tenga estrategia;
- disponga de pruebas;
- conserve historial;
- declare reversibilidad;
- produzca informe.

---

# Conformidad de publicación

Una publicación será conforme cuando:

- disponga de versión;
- incluya changelog;
- tenga informe de calidad;
- declare compatibilidad;
- incluya licencia;
- preserve URI;
- haya superado el pipeline;
- sea inmutable.

---

# Conformidad de seguridad

El grafo será conforme cuando:

- aplique autenticación;
- aplique autorización;
- preserve segregación;
- filtre inferencias;
- proteja exportaciones;
- audite accesos sensibles;
- gestione incidentes;
- respete privacidad.

---

# Checklist de release

Antes de publicar deberá comprobarse:

```text
[ ] La versión está definida.
[ ] El changelog está actualizado.
[ ] La ontología es compatible.
[ ] Los identificadores son únicos.
[ ] No existen referencias rotas.
[ ] No existen ciclos inválidos.
[ ] La procedencia mínima está completa.
[ ] Las migraciones se han ejecutado.
[ ] Las consultas canónicas superan sus pruebas.
[ ] Las inferencias críticas son reproducibles.
[ ] Los permisos han sido validados.
[ ] El snapshot ha sido generado.
[ ] El hash ha sido verificado.
[ ] El informe de calidad es satisfactorio.
[ ] La licencia está declarada.
[ ] La documentación está actualizada.
[ ] Existe plan de rollback cuando proceda.
```

---

# Checklist de deprecación

```text
[ ] Se ha documentado el motivo.
[ ] Existe sustituto cuando procede.
[ ] Se ha identificado el impacto.
[ ] Se ha definido el periodo de transición.
[ ] Se han actualizado consultas.
[ ] Se han actualizado reglas.
[ ] Se han actualizado colecciones.
[ ] Se mantiene resolución histórica.
[ ] Se ha registrado en el changelog.
```

---

# Checklist de migración

```text
[ ] La migración tiene identificador.
[ ] Se conocen versiones origen y destino.
[ ] Existe análisis de impacto.
[ ] Se ha probado en snapshot.
[ ] Existe copia de seguridad.
[ ] Se ha ejecutado dry-run.
[ ] Se han validado resultados.
[ ] Se ha comprobado la procedencia.
[ ] Se ha actualizado la documentación.
[ ] Existe rollback o se declara irreversibilidad.
```

---

# Antipatrones de gobernanza

Deberán evitarse los siguientes antipatrones.

---

## Cambios directos en producción

Todo cambio deberá pasar por pipeline y revisión.

---

## Identificadores reutilizados

Rompen la trazabilidad histórica.

---

## Releases mutables

Impiden reproducibilidad.

---

## Migraciones sin snapshot

Dificultan recuperación.

---

## Eliminaciones físicas prematuras

Destruyen historial.

---

## Cambios semánticos tratados como parches

Ocultan incompatibilidades.

---

## Fusión sin revisión

Puede mezclar entidades diferentes.

---

## Deuda sin responsable

Tiende a permanecer indefinidamente.

---

## Métricas sin umbrales

No permiten decidir.

---

## Calidad evaluada únicamente por cantidad

Más nodos no implican mejor conocimiento.

---

## Seguridad aplicada solo en la interfaz

Debe aplicarse también en consultas, inferencias, cachés e índices.

---

## Publicación sin licencia

Compromete interoperabilidad y reutilización.

---

## Alineaciones externas sin versión

Pueden quedar obsoletas silenciosamente.

---

## Uso de `same_as` para similitud

Provoca fusiones semánticas incorrectas.

---

## Inferencias materializadas sin dependencias

No pueden invalidarse correctamente.

---

## Agentes con capacidad de publicación directa

Eluden la gobernanza.

---

## Auditoría editable

Destruye confianza.

---

## Backups no probados

No garantizan recuperación.

---

## Módulos sin mantenedor

Generan abandono y deuda.

---

## Cambios sin comunicación

Pueden romper consumidores aunque sean técnicamente válidos.

---

# Arquitectura de gobernanza

```text
┌───────────────────────────────────────────────┐
│            Fuentes y contribuciones           │
│                                               │
│ Documentos · Importaciones · Editores · IA    │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Propuesta y revisión              │
│                                               │
│ Change Request · Impacto · Revisión · ADR     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Pipeline de calidad              │
│                                               │
│ Validación · Pruebas · Seguridad · Métricas   │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            Knowledge Graph versionado         │
│                                               │
│ Entidades · Afirmaciones · Reglas · Snapshots │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│       Publicación, supervisión y auditoría     │
│                                               │
│ APIs · RAG · Agentes · Alertas · Incidentes   │
└───────────────────────────────────────────────┘
```

---

# Relación con otras especificaciones

| Documento | Relación con el Knowledge Graph |
|---|---|
| `ESPECIFICACION_DE_DOCUMENTOS.md` | Define las fuentes documentales |
| `ESPECIFICACION_DE_COMPONENTES.md` | Define unidades reutilizables |
| `ESPECIFICACION_DE_RELACIONES.md` | Define predicados y relaciones |
| `ESPECIFICACION_DE_ONTOLOGIA.md` | Define el significado formal |
| `ESPECIFICACION_DE_COLECCIONES.md` | Define vistas gobernadas del grafo |
| `QUALITY.md` | Establece políticas globales de calidad |
| `GOVERNANCE_MODEL.md` | Define gobernanza transversal |
| `KNOWLEDGE_DEBT.md` | Gestiona deuda de conocimiento |
| `KNOWLEDGE_MATURITY.md` | Define niveles de madurez |
| `DECISIONS_SUMMARY.md` | Resume decisiones transversales |
| `BITACORA.md` | Registra hitos y evolución |
| `ROADMAP.md` | Organiza la evolución futura |
| `ARQUITECTURA.md` | Define el encaje global del SGCC |

---

# Referencias arquitectónicas

La presente especificación deberá mantenerse alineada con:

- `ARQUITECTURA.md`;
- `MODELO_DE_CONOCIMIENTO.md`;
- `GOVERNANCE_MODEL.md`;
- `QUALITY.md`;
- `KNOWLEDGE_STRATEGY.md`;
- `KNOWLEDGE_MATURITY.md`;
- `KNOWLEDGE_DEBT.md`;
- `ESPECIFICACION_DE_DOCUMENTOS.md`;
- `ESPECIFICACION_DE_COMPONENTES.md`;
- `ESPECIFICACION_DE_RELACIONES.md`;
- `ESPECIFICACION_DE_ONTOLOGIA.md`;
- `ESPECIFICACION_DE_COLECCIONES.md`;
- `governance/adr/`.

---

# Estrategia de evolución recomendada

La evolución práctica del Knowledge Graph debería seguir las siguientes etapas.

---

## Fase 1 — Consolidación documental

Objetivos:

- normalizar identificadores;
- completar front matter;
- reforzar relaciones explícitas;
- asegurar procedencia;
- validar enlaces.

---

## Fase 2 — Grafo estructurado

Objetivos:

- generar nodos y relaciones;
- definir módulos;
- crear snapshots;
- detectar huérfanos;
- validar dominio y rango.

---

## Fase 3 — Grafo semántico

Objetivos:

- integrar ontología;
- incorporar SHACL;
- formalizar clases y propiedades;
- implementar inferencias básicas;
- publicar Turtle o JSON-LD.

---

## Fase 4 — Explotación operativa

Objetivos:

- APIs;
- navegación;
- búsquedas;
- colecciones dinámicas;
- paneles;
- métricas.

---

## Fase 5 — Inteligencia gobernada

Objetivos:

- GraphRAG;
- embeddings;
- agentes de solo lectura;
- explicaciones;
- evaluación;
- propuestas asistidas.

---

# Implementación inicial recomendada

La primera implementación de gobernanza debería incluir:

```text
Versionado global

+

Snapshots inmutables

+

Validación estructural

+

Identificadores persistentes

+

Procedencia mínima

+

Registro de cambios

+

Informe de calidad

+

Deuda del grafo

+

Pipeline de publicación

+

Auditoría básica
```

No será necesario implementar inicialmente:

- gobernanza multiagente;
- sincronización externa bidireccional;
- bitemporalidad completa;
- auditoría criptográfica avanzada;
- razonamiento probabilístico gobernado;
- publicación pública Linked Data.

---

# Conclusión general

Con esta sexta parte se completa la especificación integral del Knowledge Graph del SGCC.

El documento ha definido:

1. los fundamentos y el modelo conceptual;
2. el modelo formal del grafo;
3. su construcción, ingestión y mantenimiento;
4. sus mecanismos de consulta, navegación y análisis;
5. su integración con razonamiento, GraphRAG y agentes;
6. su gobernanza, calidad, seguridad y evolución.

El Knowledge Graph queda establecido como el núcleo semántico operativo de NovaCoquinaria.

Su función no se limita a conectar nodos.

Debe garantizar que el conocimiento sea:

- identificable;
- contextualizado;
- trazable;
- versionado;
- consultable;
- explicable;
- interoperable;
- gobernado.

La arquitectura completa puede resumirse como:

```text
Documentos
      │
      ▼
Componentes
      │
      ▼
Relaciones
      │
      ▼
Ontología
      │
      ▼
Knowledge Graph
      │
      ├── Colecciones
      ├── Consultas
      ├── Inferencias
      ├── GraphRAG
      └── Agentes
      │
      ▼
Aplicaciones inteligentes
```

La calidad de las capas superiores dependerá directamente de la calidad del grafo.

Un sistema RAG no podrá ser fiable si sus fuentes no están gobernadas.

Un agente no podrá ser explicable si sus relaciones carecen de procedencia.

Una inferencia no podrá ser reproducible si no conserva premisas y versiones.

Una colección no podrá evaluarse si sus miembros no poseen identidad estable.

Por este motivo, la gobernanza del Knowledge Graph deberá considerarse una capacidad central del SGCC y no una actividad administrativa secundaria.

La evolución del grafo deberá mantener siempre una frontera clara entre:

```text
Conocimiento declarado

Conocimiento validado

Conocimiento inferido

Conocimiento predicho

Conocimiento propuesto
```

Solo mediante esta separación NovaCoquinaria podrá incorporar capacidades avanzadas de inteligencia artificial sin perder:

- control;
- coherencia;
- trazabilidad;
- confianza;
- sostenibilidad.

La siguiente especificación natural del SGCC podrá desarrollar de forma independiente el motor encargado de aplicar reglas, validar restricciones, generar inferencias y construir explicaciones:

```text
ESPECIFICACION_DEL_RAZONADOR.md
```

A partir de ahí podrán formalizarse con mayor profundidad:

```text
ESPECIFICACION_RAG.md
```

y:

```text
ESPECIFICACION_DE_AGENTES.md
```

Con la finalización de esta especificación, NovaCoquinaria dispone de una base arquitectónica completa para convertir su conocimiento culinario documentado en una red semántica operativa, interoperable y preparada para sistemas inteligentes.
