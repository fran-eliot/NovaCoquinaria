---
id: DOC-0024
titulo: Especificación de Ontología
tipo: especificacion
version: 1.0.0
estado: en_revision
ultima_revision: 2026-07-30
---

# Fundamentos ontológicos

La presente sección establece los principios conceptuales que sustentan la ontología del Sistema de Gestión del Conocimiento Culinario (SGCC).

Mientras que las especificaciones anteriores definen:

- documentos;
- componentes;
- relaciones;
- colecciones;

esta especificación define el modelo semántico que da significado formal a todos esos elementos y permite su interpretación por personas y sistemas inteligentes.

La ontología constituye el nivel más alto de abstracción del conocimiento del SGCC.

No describe documentos ni implementaciones concretas.

Describe la realidad conceptual que dichos documentos representan.

---

# Objetivo

El objetivo de esta especificación es definir un modelo ontológico común que permita:

- representar conocimiento culinario de forma inequívoca;
- establecer significados compartidos;
- garantizar coherencia semántica;
- facilitar inferencias automáticas;
- soportar interoperabilidad;
- permitir evolución controlada;
- servir como fundamento del Knowledge Graph;
- facilitar el uso por sistemas RAG y agentes de inteligencia artificial.

---

# Alcance

Esta especificación regula:

- conceptos;
- clases;
- propiedades;
- relaciones;
- axiomas;
- restricciones;
- jerarquías;
- inferencias;
- identidad semántica;
- contexto;
- modularidad;
- evolución ontológica.

No regula directamente:

- estructura documental;
- almacenamiento;
- interfaces de usuario;
- APIs;
- tecnologías de persistencia;
- implementaciones particulares.

Estos aspectos se desarrollan en otras especificaciones del SGCC.

---

# Posición de la ontología dentro del SGCC

La ontología constituye el núcleo conceptual del sistema.

Puede representarse mediante el siguiente modelo:

```text
Documentos

↓

Componentes

↓

Relaciones

↓

Ontología

↓

Knowledge Graph

↓

Razonamiento

↓

Aplicaciones inteligentes
```

Cada nivel añade un grado superior de significado.

Los documentos almacenan conocimiento.

Los componentes estructuran ese conocimiento.

Las relaciones conectan los componentes.

La ontología define qué significan dichos componentes y relaciones.

---

# Qué es una ontología

Dentro del SGCC, una ontología es una especificación formal, explícita y compartida de los conceptos que describen el dominio culinario y de las relaciones existentes entre ellos.

Incluye:

- clases;
- propiedades;
- relaciones;
- restricciones;
- axiomas;
- reglas;
- jerarquías;
- significados.

Su finalidad es garantizar que todos los sistemas interpreten el conocimiento de forma consistente.

---

# Ontología como contrato semántico

La ontología actúa como un contrato entre:

- personas;
- documentos;
- aplicaciones;
- APIs;
- bases de datos;
- grafos;
- motores de inferencia;
- agentes IA.

Este contrato garantiza que todos atribuyan el mismo significado a los mismos conceptos.

---

# Características de una ontología

La ontología del SGCC deberá ser:

- formal;
- explícita;
- compartida;
- extensible;
- modular;
- reutilizable;
- consistente;
- trazable;
- interoperable;
- evolutiva.

---

# Principios fundamentales

La ontología se construye sobre varios principios básicos.

---

## Primacía del significado

El significado tiene prioridad sobre la representación.

Un concepto seguirá siendo el mismo aunque cambie:

- el documento;
- el idioma;
- el formato;
- la base de datos;
- la API;
- el lenguaje de programación;
- la tecnología empleada.

---

## Independencia tecnológica

La ontología no pertenece a ninguna tecnología.

Podrá representarse mediante:

- Markdown;
- YAML;
- JSON;
- RDF;
- OWL;
- Neo4j;
- PostgreSQL;
- GraphQL;
- APIs REST.

Todas estas representaciones deberán preservar el mismo significado.

---

## Identidad conceptual

Cada concepto representa una entidad única dentro del dominio culinario.

La identidad conceptual no depende de:

- nombres;
- etiquetas;
- traducciones;
- identificadores técnicos;
- implementaciones.

---

## Reutilización

Todo concepto deberá poder reutilizarse por múltiples documentos y componentes.

La duplicación conceptual deberá evitarse.

---

## Modularidad

La ontología deberá organizarse en módulos independientes pero coherentes.

Ejemplo:

```text
Ontología

├── Ingredientes

├── Técnicas

├── Elaboraciones

├── Recetas

├── Equipamiento

├── Nutrición

├── Restricciones

├── Planificación

└── Gestión documental
```

Cada módulo podrá evolucionar sin comprometer el resto del sistema.

---

## Extensibilidad

La incorporación de nuevos conceptos no deberá requerir redefinir toda la ontología.

La arquitectura deberá facilitar:

- nuevos módulos;
- nuevas clases;
- nuevas propiedades;
- nuevas relaciones;
- nuevas reglas;
- nuevas taxonomías.

---

## Coherencia

No podrán coexistir conceptos incompatibles salvo que la propia ontología modele explícitamente dicha incompatibilidad.

---

## Explicabilidad

Toda inferencia derivada de la ontología deberá poder justificarse mediante:

- conceptos;
- relaciones;
- axiomas;
- reglas;
- restricciones.

---

## Evolución controlada

La ontología deberá evolucionar mediante un proceso gobernado.

Ningún cambio semántico deberá producirse de forma implícita.

---

# Ontología frente a otros conceptos

Es importante distinguir la ontología de otros elementos del SGCC.

---

## Ontología y documento

Un documento almacena información.

La ontología define el significado de dicha información.

Ejemplo:

```text
Documento

↓

"Arroz basmati"
```

La ontología define:

- que es un ingrediente;
- que pertenece a la familia de cereales;
- que puede utilizarse en determinadas elaboraciones;
- que posee determinadas propiedades.

---

## Ontología y componente

Un componente representa una unidad de conocimiento.

La ontología define qué tipo de unidad es.

Ejemplo:

```text
ING-0005
```

es un componente.

La ontología establece que pertenece a la clase:

```text
Ingrediente
```

---

## Ontología y relación

La especificación de relaciones define:

```text
utiliza
```

La ontología establece:

- su significado;
- dominio;
- rango;
- restricciones;
- axiomas;
- propiedades lógicas.

---

## Ontología y taxonomía

Una taxonomía organiza conceptos mediante jerarquías.

Ejemplo:

```text
Verduras

↓

Crucíferas

↓

Brócoli
```

Una ontología incluye taxonomías, pero además incorpora:

- propiedades;
- relaciones;
- restricciones;
- inferencias;
- axiomas;
- contexto.

Toda taxonomía puede formar parte de una ontología.

No toda ontología puede reducirse a una taxonomía.

---

## Ontología y tesauro

Un tesauro describe relaciones terminológicas.

Ejemplo:

- sinónimo;
- término preferente;
- término relacionado.

La ontología incorpora estas relaciones cuando son necesarias, pero añade conocimiento formal que permite razonamiento automático.

---

## Ontología y modelo de datos

Un modelo de datos organiza información para almacenarla.

La ontología describe el significado del dominio.

El modelo de datos podrá derivarse de la ontología, pero ambos niveles no son equivalentes.

---

## Ontología y esquema

Un esquema define la estructura permitida de los datos.

La ontología define el significado de dichos datos.

---

## Ontología y Knowledge Graph

La ontología define:

```text
Qué existe
```

El Knowledge Graph representa:

```text
Qué instancias concretas existen
```

Ejemplo:

Ontología:

```text
Clase

Ingrediente
```

Knowledge Graph:

```text
Arroz basmati

Arroz integral

Arroz jazmín
```

---

## Ontología y motor de inferencia

La ontología establece las reglas conceptuales.

El motor de inferencia aplica dichas reglas para generar nuevo conocimiento.

---

# Papel de la ontología en el SGCC

La ontología constituye la fuente oficial del significado conceptual.

Todas las demás capas deberán alinearse con ella.

```text
Interfaz

↓

API

↓

Modelo de datos

↓

Knowledge Graph

↓

Ontología
```

La ontología es el nivel de autoridad semántica.

---

# Dominio ontológico

El dominio cubierto por la ontología comprende el conocimiento culinario y los elementos necesarios para gestionarlo.

Incluye, entre otros:

- ingredientes;
- técnicas;
- utensilios;
- equipos;
- elaboraciones;
- recetas;
- menús;
- procesos;
- restricciones;
- nutrición;
- planificación;
- colecciones;
- documentos;
- usuarios;
- actividades;
- conocimiento derivado.

---

# Límites del dominio

La ontología no pretende modelar todo el conocimiento humano.

Solo modelará aquello necesario para los objetivos del SGCC.

Los conceptos ajenos al dominio podrán referenciarse mediante vocabularios externos cuando resulte conveniente.

---

# Niveles ontológicos

La ontología distingue varios niveles de abstracción.

---

## Nivel conceptual

Describe las clases generales.

Ejemplo:

```text
Ingrediente
```

---

## Nivel de instancia

Describe elementos concretos.

Ejemplo:

```text
Arroz basmati
```

---

## Nivel metamodelo

Describe cómo se construye la propia ontología.

Ejemplo:

```text
Clase

Propiedad

Relación

Axioma
```

Este nivel será desarrollado en la siguiente parte de esta especificación.

---

# Modelo conceptual general

La ontología puede resumirse mediante el siguiente esquema.

```text
Ontología
    │
    ├── Clases
    ├── Propiedades
    ├── Relaciones
    ├── Restricciones
    ├── Axiomas
    ├── Reglas
    ├── Contexto
    ├── Jerarquías
    ├── Inferencias
    └── Versionado
```

---

# Concepto

Un concepto representa una categoría abstracta del dominio culinario.

Ejemplos:

```text
Ingrediente

Receta

Técnica

Utensilio

Restricción dietética
```

Los conceptos constituyen el vocabulario fundamental de la ontología.

---

# Entidad

Una entidad representa algo que puede existir dentro del dominio.

Una entidad puede ser:

- abstracta;
- concreta;
- física;
- digital;
- conceptual.

Ejemplos:

```text
Cebolla

Receta

Menú semanal

Plan de compra
```

---

# Clase

Una clase agrupa entidades con características comunes.

Ejemplo:

```text
Ingrediente
```

agrupará:

- cebolla;
- ajo;
- arroz;
- pollo;
- tomate.

---

# Instancia

Una instancia representa un elemento concreto perteneciente a una clase.

Ejemplo:

```text
Clase

Ingrediente
```

↓

```text
Instancia

Arroz basmati
```

---

# Propiedad

Una propiedad describe una característica de una entidad.

Ejemplos:

```text
peso

color

tiempo

temperatura

cantidad
```

---

# Relación

Una relación conecta entidades.

Ejemplo:

```text
Receta

↓

utiliza

↓

Ingrediente
```

Las relaciones se desarrollan formalmente en la especificación correspondiente.

---

# Restricción

Una restricción limita los valores válidos de un concepto.

Ejemplo:

```text
Una receta estable deberá contener al menos un ingrediente.
```

---

# Axioma

Un axioma representa una afirmación considerada siempre verdadera dentro del dominio.

Ejemplo:

```text
Toda receta es una elaboración culinaria.
```

Los axiomas permiten construir inferencias consistentes.

---

# Regla

Una regla permite derivar nuevo conocimiento.

Ejemplo:

```text
Si una receta utiliza un ingrediente que contiene gluten

↓

la receta contiene gluten
```

Las reglas no sustituyen a los axiomas.

Los axiomas describen el modelo.

Las reglas describen el razonamiento.

---

# Jerarquía

Las jerarquías organizan conceptos mediante relaciones de especialización.

Ejemplo:

```text
Ingrediente

↓

Verdura

↓

Crucífera

↓

Brócoli
```

---

# Contexto

El contexto determina cuándo una afirmación es válida.

Ejemplo:

```text
Yogur sustituye a nata
```

solo en determinadas elaboraciones.

La ontología deberá permitir modelar dichos contextos.

---

# Temporalidad

Algunas afirmaciones serán permanentes.

Otras dependerán del tiempo.

Ejemplo:

```text
Disponible en temporada
```

La ontología deberá distinguir ambos casos.

---

# Identidad ontológica

Todo concepto deberá poseer una identidad estable.

Esta identidad permanecerá aunque cambien:

- etiquetas;
- traducciones;
- documentación;
- implementaciones.

---

# Nombrado

Los nombres deberán ser:

- claros;
- precisos;
- consistentes;
- estables;
- comprensibles;
- reutilizables.

Se evitarán:

- abreviaturas ambiguas;
- tecnicismos innecesarios;
- sinónimos como nombres canónicos.

---

# Vocabulario controlado

La ontología constituye el vocabulario controlado oficial del SGCC.

Los documentos deberán utilizar preferentemente dicho vocabulario.

Las variantes terminológicas podrán registrarse como:

- alias;
- traducciones;
- sinónimos.

---

# Granularidad

La ontología deberá mantener un nivel de detalle adecuado.

No deberá crear conceptos extremadamente específicos cuando puedan modelarse mediante propiedades o contexto.

Tampoco deberá utilizar conceptos excesivamente generales que dificulten el razonamiento.

---

# Modularidad conceptual

Los módulos ontológicos deberán:

- ser cohesivos;
- minimizar dependencias;
- reutilizar conceptos comunes;
- evitar duplicidades.

---

# Reutilización conceptual

Todo concepto deberá diseñarse para poder utilizarse desde múltiples dominios culinarios.

Ejemplo:

```text
Temperatura
```

podrá emplearse en:

- cocción;
- conservación;
- fermentación;
- servicio;
- seguridad alimentaria.

---

# Interoperabilidad

La ontología deberá facilitar la integración con:

- estándares abiertos;
- vocabularios externos;
- motores RDF;
- OWL;
- SKOS;
- sistemas RAG;
- agentes inteligentes.

---

# Neutralidad tecnológica

La ontología no dependerá de:

- Neo4j;
- PostgreSQL;
- RDF;
- OWL;
- JSON;
- GraphQL.

Estas tecnologías implementarán la ontología, pero no la definirán.

---

# Consistencia semántica

Todo concepto deberá mantener el mismo significado en cualquier representación.

No deberán existir definiciones contradictorias.

---

# Evolución del conocimiento

La ontología deberá admitir evolución sin romper la coherencia del sistema.

Toda modificación deberá preservar:

- significado;
- identidad;
- trazabilidad;
- compatibilidad cuando sea posible.

---

# Calidad ontológica

Una ontología de calidad deberá ser:

- correcta;
- consistente;
- completa respecto a su alcance;
- reutilizable;
- modular;
- extensible;
- documentada;
- validable;
- interoperable;
- explicable.

---

# Objetivos estratégicos

La ontología permitirá:

- construir el Knowledge Graph;
- realizar inferencias;
- validar conocimiento;
- generar recomendaciones;
- mejorar búsquedas;
- soportar RAG;
- alimentar agentes IA;
- facilitar interoperabilidad;
- preservar conocimiento a largo plazo.

---

# Transición hacia el metamodelo

La presente parte ha establecido:

- qué es una ontología;
- cuál es su función;
- qué principios la gobiernan;
- cómo se diferencia de otros modelos;
- cuál es su posición dentro del SGCC;
- qué elementos fundamentales la componen.

La siguiente parte desarrollará el metamodelo ontológico, definiendo formalmente:

- clases;
- metaclases;
- propiedades;
- relaciones;
- restricciones;
- axiomas;
- jerarquías;
- dominios;
- rangos;
- cardinalidades;
- perfiles de conformidad.

Dicho metamodelo constituirá el lenguaje formal utilizado para construir toda la ontología del SGCC.

---

# Metamodelo ontológico

Esta sección define el metamodelo utilizado para construir, describir y validar la ontología del Sistema de Gestión del Conocimiento Culinario (SGCC).

La parte anterior estableció los fundamentos ontológicos.

La presente parte define el lenguaje formal mediante el que se describirán:

- clases;
- instancias;
- propiedades;
- relaciones;
- axiomas;
- restricciones;
- jerarquías;
- contextos;
- módulos;
- perfiles de conformidad.

El metamodelo constituye la estructura normativa sobre la que deberán construirse todos los módulos ontológicos de NovaCoquinaria.

---

# Objetivo

El objetivo del metamodelo es proporcionar una estructura común que permita:

- definir conceptos de forma uniforme;
- expresar propiedades y relaciones;
- declarar restricciones;
- establecer jerarquías;
- describir axiomas;
- facilitar validación;
- soportar inferencias;
- mantener coherencia;
- permitir interoperabilidad;
- gobernar la evolución de la ontología.

---

# Alcance

El metamodelo regula:

- tipos de elementos ontológicos;
- estructura de las clases;
- identidad;
- instanciación;
- propiedades de datos;
- propiedades de objeto;
- propiedades de anotación;
- dominio;
- rango;
- cardinalidad;
- equivalencia;
- disjunción;
- jerarquía;
- composición;
- roles;
- eventos;
- estados;
- contexto;
- temporalidad;
- modularidad;
- perfiles de conformidad.

No define todavía:

- el catálogo completo de clases culinarias;
- todas las reglas de inferencia;
- la serialización definitiva en RDF u OWL;
- la implementación en una base de datos concreta;
- los algoritmos de razonamiento.

Estos aspectos se desarrollarán en las partes siguientes y en especificaciones complementarias.

---

# Posición del metamodelo

El metamodelo ocupa un nivel superior al de las clases e instancias del dominio.

```text
Metamodelo
    │
    ├── define qué es una Clase
    ├── define qué es una Propiedad
    ├── define qué es una Relación
    ├── define qué es una Restricción
    └── define qué es un Axioma
            │
            ▼
Ontología
    │
    ├── Ingrediente
    ├── Receta
    ├── Técnica
    └── Equipo
            │
            ▼
Knowledge Graph
    │
    ├── Cebolla
    ├── Curry japonés
    ├── Confitar
    └── Sartén de hierro
```

---

# Niveles del modelo

El SGCC distinguirá al menos tres niveles.

---

## Nivel M2 — Metamodelo

Define los tipos de elementos utilizados para construir la ontología.

Ejemplos:

```text
ClaseOntologica

PropiedadOntologica

RelacionOntologica

Axioma

Restriccion
```

---

## Nivel M1 — Ontología

Define las clases y propiedades del dominio.

Ejemplos:

```text
Ingrediente

Receta

utiliza

tiempo_de_coccion
```

---

## Nivel M0 — Instancias

Contiene entidades y afirmaciones concretas.

Ejemplos:

```text
Cebolla es_un Ingrediente

REC-0042 utiliza ING-0017
```

---

# Separación entre metamodelo y dominio

No deberán confundirse:

```text
Clase
```

con:

```text
Ingrediente
```

`Clase` pertenece al metamodelo.

`Ingrediente` pertenece a la ontología del dominio.

Del mismo modo:

```text
PropiedadDeObjeto
```

pertenece al metamodelo.

```text
utiliza
```

es una propiedad de objeto concreta del dominio.

---

# Elemento ontológico

Todo componente que forme parte de la ontología deberá considerarse un elemento ontológico.

Los tipos principales serán:

```text
ElementoOntologico
    │
    ├── ModuloOntologico
    ├── ClaseOntologica
    ├── Individuo
    ├── PropiedadOntologica
    ├── Axioma
    ├── Restriccion
    ├── Regla
    ├── Taxonomia
    └── Anotacion
```

---

# Contrato base de un elemento ontológico

Todo elemento ontológico deberá poder declarar:

```text
Identificador

Nombre canónico

Tipo de elemento

Definición

Versión

Estado

Módulo

Procedencia
```

Podrá declarar además:

```text
Etiquetas

Alias

Traducciones

Comentarios

Ejemplos

Contraejemplos

Restricciones

Dependencias

Fecha de creación

Fecha de revisión

Responsable
```

---

# Identificadores ontológicos

Los elementos ontológicos deberán disponer de identificadores persistentes.

Podrán utilizarse prefijos como:

```text
ONT-CLS-XXXX

ONT-PRP-XXXX

ONT-AXM-XXXX

ONT-RST-XXXX

ONT-RUL-XXXX

ONT-MOD-XXXX
```

Ejemplos:

```text
ONT-CLS-0001

ONT-PRP-0024
```

El formato definitivo deberá alinearse con el registro global de identificadores del SGCC.

---

# Nombres canónicos

Todo elemento deberá disponer de un nombre canónico.

Ejemplos:

```text
Ingrediente

Receta

utiliza

contiene_alergeno
```

Los nombres canónicos deberán:

- ser estables;
- ser inequívocos;
- respetar convenciones;
- evitar abreviaturas innecesarias;
- distinguir clases de propiedades.

---

# Etiquetas y traducciones

Los nombres visibles podrán registrarse por idioma.

Ejemplo:

```yaml
etiquetas:
  es: Ingrediente
  en: Ingredient
  fr: Ingrédient
```

La traducción no alterará la identidad del elemento.

---

# Alias

Un alias representa una variante terminológica.

Ejemplo:

```yaml
nombre_canonico: cilantro

alias:
  - coriandro
  - hojas_de_coriandro
```

Los alias no constituirán elementos ontológicos independientes salvo que representen conceptos distintos.

---

# Definición

Todo elemento deberá incluir una definición normativa.

La definición deberá indicar:

- qué representa;
- qué incluye;
- qué excluye;
- cómo se diferencia de conceptos próximos.

Ejemplo:

```text
Ingrediente:
Entidad material utilizada en una elaboración culinaria y que
contribuye directa o indirectamente al resultado obtenido.
```

---

# Estado

Los estados básicos serán:

```text
Borrador

En revisión

Estable

Obsoleto

Archivado

Rechazado
```

El estado deberá aplicarse tanto a:

- clases;
- propiedades;
- axiomas;
- restricciones;
- reglas;
- módulos.

---

# Clase ontológica

Una clase ontológica representa una categoría conceptual cuyos miembros comparten determinadas características.

Ejemplos:

```text
Ingrediente

Receta

Técnica

Equipo
```

---

# Estructura de una clase

Toda clase deberá poder declarar:

```text
Identificador

Nombre

Definición

Superclase

Subclases

Propiedades

Restricciones

Clases equivalentes

Clases disjuntas

Módulo

Estado
```

---

# Representación conceptual de una clase

```text
ClaseOntologica
    │
    ├── identidad
    ├── semántica
    ├── jerarquía
    ├── propiedades
    ├── restricciones
    ├── axiomas
    └── anotaciones
```

---

# Superclase

Una superclase representa un concepto más general.

Ejemplo:

```text
Ingrediente vegetal
    │
    └── subtipo_de
            │
            ▼
       Ingrediente
```

---

# Subclase

Una subclase representa una especialización de otra clase.

Ejemplo:

```text
Ingrediente
    │
    └── Verdura
            │
            └── Crucífera
```

Toda instancia de una subclase deberá considerarse también instancia de sus superclases.

---

# Herencia

Las subclases heredarán:

- propiedades aplicables;
- restricciones compatibles;
- relaciones;
- axiomas generales.

Ejemplo:

```text
Crucífera subtipo_de Verdura

Verdura subtipo_de Ingrediente
```

permitirá inferir:

```text
Crucífera subtipo_de Ingrediente
```

---

# Herencia múltiple

Una clase podrá tener varias superclases cuando las categorías sean compatibles.

Ejemplo:

```text
Leche de coco
    │
    ├── Ingrediente vegetal
    └── Líquido culinario
```

La herencia múltiple deberá evitar contradicciones.

---

# Clase primitiva

Una clase primitiva se define mediante condiciones necesarias, pero no suficientes.

Ejemplo:

```text
Receta
```

puede requerir:

- al menos una elaboración;
- un resultado;
- una representación documental.

Cumplir estas condiciones no implica necesariamente que toda entidad sea automáticamente una receta salvo que la ontología lo declare.

---

# Clase definida

Una clase definida se describe mediante condiciones necesarias y suficientes.

Ejemplo conceptual:

```text
Receta vegetariana
    ≡
Receta
    y
no utiliza Carne
    y
no utiliza Pescado
```

Si una instancia cumple todas las condiciones, podrá clasificarse automáticamente como `Receta vegetariana`.

---

# Clase abstracta

Una clase abstracta organiza el modelo, pero no deberá tener instancias directas.

Ejemplo:

```text
Recurso culinario
```

podrá especializarse en:

```text
Ingrediente

Equipo

Documento
```

Las instancias deberán pertenecer a alguna subclase concreta.

---

# Clase concreta

Una clase concreta podrá contener instancias directas.

Ejemplo:

```text
Ingrediente
```

si el modelo admite instancias que no pertenezcan todavía a una subclase más específica.

---

# Clase cerrada

Una clase cerrada declara que sus miembros posibles están completamente enumerados o restringidos.

Ejemplo:

```text
Nivel de dificultad
```

con valores:

```text
Básico

Intermedio

Avanzado
```

Este patrón deberá utilizarse con precaución debido al principio de mundo abierto.

---

# Clase enumerada

Una clase enumerada se define por un conjunto explícito de individuos.

Ejemplo:

```text
Estado de receta
    =
{
  borrador,
  en_revision,
  estable,
  obsoleta
}
```

---

# Clase equivalente

Dos clases serán equivalentes cuando representen exactamente el mismo conjunto de instancias.

Notación conceptual:

```text
A ≡ B
```

Ejemplo:

```text
Preparación sin ingredientes animales
    ≡
Preparación vegana
```

solo si ambas definiciones son realmente idénticas dentro del SGCC.

---

# Clase disjunta

Dos clases serán disjuntas cuando ninguna instancia pueda pertenecer a ambas simultáneamente en el mismo contexto.

Notación:

```text
A ⊓ B = ∅
```

Ejemplo potencial:

```text
Ingrediente animal

Ingrediente exclusivamente vegetal
```

La disjunción deberá aplicarse únicamente cuando sea semánticamente segura.

---

# Disjunción múltiple

Podrá declararse que varias clases son mutuamente disjuntas.

Ejemplo:

```text
EstadoBorrador

EstadoEstable

EstadoArchivado
```

para una misma dimensión de estado y contexto temporal.

---

# Partición de clases

Una partición define subclases:

- exhaustivas;
- mutuamente disjuntas.

Ejemplo:

```text
Temperatura de servicio
    │
    ├── fría
    ├── templada
    └── caliente
```

Solo deberá modelarse como partición si no existe ningún otro valor posible dentro del alcance.

---

# Instancia o individuo

Un individuo representa una entidad concreta del dominio.

Ejemplos:

```text
Arroz basmati

Curry japonés

Sartén de hierro
```

---

# Pertenencia a clase

La pertenencia se expresará mediante:

```text
Individuo ── es_instancia_de ── Clase
```

Ejemplo:

```text
ING-0005 ── es_instancia_de ── Ingrediente
```

---

# Instanciación múltiple

Un individuo podrá pertenecer a varias clases compatibles.

Ejemplo:

```text
Miso blanco
    │
    ├── Ingrediente
    ├── Condimento
    └── Producto fermentado
```

---

# Identidad de individuos

Dos referencias podrán representar:

- el mismo individuo;
- individuos distintos;
- individuos potencialmente equivalentes;
- individuos cuya relación no está determinada.

No deberá asumirse identidad únicamente por compartir nombre.

---

# Mismo individuo

La ontología podrá declarar equivalencia de identidad.

Notación conceptual:

```text
A sameAs B
```

Esta afirmación será fuerte y deberá usarse con precaución.

Implica que todas las propiedades de A y B pertenecen al mismo individuo.

---

# Individuos distintos

Podrá declararse:

```text
A differentFrom B
```

cuando sea necesario evitar fusiones incorrectas.

---

# Propiedad ontológica

Una propiedad describe una característica o conexión aplicable a entidades del dominio.

Tipos principales:

```text
PropiedadOntologica
    │
    ├── PropiedadDeDatos
    ├── PropiedadDeObjeto
    └── PropiedadDeAnotacion
```

---

# Propiedad de datos

Una propiedad de datos conecta una entidad con un valor literal.

Ejemplos:

```text
tiempo_de_coccion

temperatura_recomendada

nombre

cantidad
```

Modelo:

```text
Entidad ── propiedad_de_datos ── Literal
```

Ejemplo:

```text
Receta ── tiempo_de_coccion ── 45 minutos
```

---

# Estructura de una propiedad de datos

Deberá poder declarar:

```text
Identificador

Nombre

Definición

Dominio

Tipo de dato

Cardinalidad

Unidad

Restricciones

Valor por defecto

Estado
```

---

# Tipos de datos

El metamodelo deberá soportar al menos:

- texto;
- entero;
- decimal;
- booleano;
- fecha;
- fecha y hora;
- duración;
- URI;
- identificador;
- código controlado.

Podrán añadirse tipos especializados.

---

# Valores literales

Un literal deberá poder incluir:

```text
valor

tipo

unidad

idioma

precisión
```

Ejemplo:

```yaml
valor: 180
tipo: decimal
unidad: celsius
```

---

# Unidad de medida

Las propiedades cuantitativas deberán distinguir entre:

```text
Valor numérico

Unidad de medida
```

Ejemplo:

```text
180 °C
```

No deberá almacenarse únicamente como texto cuando se necesite cálculo.

---

# Magnitud

Las unidades deberán relacionarse con una magnitud.

Ejemplo:

```text
Gramo ── unidad_de ── Masa

Mililitro ── unidad_de ── Volumen
```

Esto permitirá validar que una propiedad de masa no utilice una unidad de tiempo.

---

# Intervalos de valores

Una propiedad podrá admitir:

```text
valor mínimo

valor máximo

intervalo cerrado

intervalo abierto

tolerancia
```

Ejemplo:

```yaml
temperatura:
  minimo: 175
  maximo: 185
  unidad: celsius
```

---

# Valores controlados

Una propiedad podrá limitarse a un vocabulario controlado.

Ejemplo:

```text
dificultad:
  - basica
  - intermedia
  - avanzada
```

---

# Propiedad de objeto

Una propiedad de objeto conecta dos entidades ontológicas.

Ejemplo:

```text
Receta ── utiliza ── Ingrediente
```

Las propiedades de objeto se corresponden con las relaciones definidas en `ESPECIFICACION_DE_RELACIONES.md`.

---

# Estructura de una propiedad de objeto

Deberá poder declarar:

```text
Identificador

Nombre

Definición

Dominio

Rango

Dirección

Inversa

Cardinalidad

Características lógicas

Restricciones

Estado
```

---

# Propiedad de anotación

Una propiedad de anotación añade información descriptiva sin modificar directamente la semántica del dominio.

Ejemplos:

```text
etiqueta

comentario

fuente

ejemplo

nota_editorial

traducción
```

---

# Diferencia entre propiedad de datos y anotación

Una propiedad de datos describe una característica semántica del individuo.

Una anotación describe el recurso ontológico o su documentación.

Ejemplo:

```text
temperatura_de_coccion
```

es una propiedad de datos.

```text
comentario_editorial
```

es una propiedad de anotación.

---

# Dominio

El dominio define las clases a las que puede aplicarse una propiedad.

Ejemplo:

```text
tiempo_de_coccion
```

podrá tener como dominio:

```text
Receta

Elaboración

Técnica contextualizada
```

---

# Dominio múltiple

Una propiedad podrá aplicarse a varias clases.

Deberá distinguirse entre:

```text
Dominio como unión
```

y:

```text
Dominio como intersección
```

Ejemplo de unión:

```text
Receta o Elaboración
```

Ejemplo de intersección:

```text
Entidad que sea simultáneamente Producto y Alimento
```

---

# Inferencia por dominio

Si una propiedad declara:

```text
dominio: Receta
```

y se registra:

```text
X utiliza ING-0001
```

un razonador formal podría inferir que `X` es una receta si `utiliza` tiene dominio exclusivo `Receta`.

Por este motivo, el dominio no deberá utilizarse únicamente como validación de formulario.

Tiene consecuencias semánticas.

---

# Rango

El rango define el tipo de valor o entidad permitido como destino.

Ejemplo:

```text
utiliza
```

podrá tener rango:

```text
Ingrediente

Base culinaria

Equipo

Técnica
```

---

# Inferencia por rango

Si una propiedad tiene rango:

```text
Ingrediente
```

y se afirma:

```text
REC-0001 utiliza X
```

podrá inferirse que `X` es un ingrediente.

Esta consecuencia deberá tenerse en cuenta al diseñar las propiedades.

---

# Dominio y rango amplios

Las propiedades generales podrán utilizar dominios y rangos amplios.

Ejemplo:

```text
relacionado_con
```

podría conectar cualquier `Entidad`.

Sin embargo, el uso de propiedades demasiado amplias reduce la capacidad de validación e inferencia.

---

# Restricción local de propiedad

Una clase podrá restringir una propiedad sin modificar su definición global.

Ejemplo:

```text
Receta de pan
    │
    └── utiliza solo Ingrediente panificable
```

Esta restricción será local a la clase.

---

# Cardinalidad

La cardinalidad define el número permitido de valores de una propiedad.

Tipos:

```text
mínima

máxima

exacta
```

---

# Cardinalidad mínima

Ejemplo:

```text
Receta produce mínimo 1 Resultado
```

Notación:

```text
min 1
```

---

# Cardinalidad máxima

Ejemplo:

```text
Receta tiene máximo 1 nivel_de_dificultad
```

Notación:

```text
max 1
```

---

# Cardinalidad exacta

Ejemplo:

```text
Rango de temperatura tiene exactamente 1 mínimo
```

Notación:

```text
exactly 1
```

---

# Cardinalidad cualificada

La cardinalidad podrá aplicarse a una clase concreta.

Ejemplo:

```text
Receta utiliza mínimo 1 Ingrediente
```

sin limitar otros objetos posibles de `utiliza`, como una técnica o un equipo.

---

# Existencial

Una restricción existencial afirma que existe al menos un valor de cierto tipo.

Ejemplo:

```text
Receta
    utiliza some Ingrediente
```

Significa que toda receta utiliza al menos un ingrediente.

---

# Universal

Una restricción universal limita todos los valores de una propiedad.

Ejemplo:

```text
Receta vegana
    utiliza only Ingrediente vegano
```

No afirma por sí sola que utilice algún ingrediente.

Para ello deberá combinarse con una restricción existencial.

---

# Valor específico

Una restricción podrá exigir un valor concreto.

Ejemplo:

```text
Receta horneada
    aplica value Horneado
```

---

# Autorrestricción

Podrá expresarse que una entidad se relaciona consigo misma mediante una propiedad cuando la semántica lo admita.

Este patrón será excepcional y deberá justificarse.

---

# Propiedad funcional

Una propiedad funcional permite como máximo un valor por sujeto dentro de un contexto.

Ejemplo:

```text
tiene_estado_actual
```

---

# Propiedad inversamente funcional

Una propiedad inversamente funcional permite que un objeto identifique de forma única al sujeto.

Ejemplo potencial:

```text
tiene_identificador_global
```

si el identificador es único.

---

# Propiedad simétrica

Una propiedad simétrica cumple:

```text
A R B
```

implica:

```text
B R A
```

Ejemplos:

```text
compatible_con

similar_a
```

---

# Propiedad asimétrica

Una propiedad asimétrica cumple:

```text
A R B
```

implica que:

```text
B R A
```

no puede ser verdadero.

Ejemplos:

```text
precede_a

subtipo_de
```

---

# Propiedad transitiva

Una propiedad transitiva permite:

```text
A R B

B R C

⇒

A R C
```

Ejemplo:

```text
subtipo_de
```

---

# Propiedad reflexiva

Una propiedad reflexiva permite que toda entidad se relacione consigo misma.

Este comportamiento será infrecuente en el dominio culinario.

---

# Propiedad irreflexiva

Una propiedad irreflexiva prohíbe:

```text
A R A
```

Ejemplos:

```text
precede_a

variante_de

deriva_de
```

---

# Propiedades equivalentes

Dos propiedades serán equivalentes cuando expresen exactamente las mismas relaciones.

Notación:

```text
R1 ≡ R2
```

Deberá evitarse mantener propiedades equivalentes internas salvo por interoperabilidad.

---

# Subpropiedad

Una propiedad podrá especializar otra.

Ejemplo:

```text
utiliza_ingrediente
    │
    └── subpropiedad_de
            │
            ▼
         utiliza
```

Toda instancia de la subpropiedad implicará la propiedad general.

---

# Cadena de propiedades

Una cadena de propiedades permite definir una inferencia compuesta.

Ejemplo:

```text
utiliza ○ contiene_alergeno
    ⇒
contiene_alergeno
```

Las cadenas se formalizarán en la parte dedicada a semántica e inferencia.

---

# Propiedades disjuntas

Dos propiedades serán disjuntas cuando no puedan aplicarse simultáneamente al mismo par de participantes en el mismo contexto.

Ejemplo potencial:

```text
satisface

incumple
```

La disjunción deberá considerar:

- contexto;
- vigencia;
- método de validación;
- procedencia.

---

# Restricción ontológica

Una restricción limita las interpretaciones válidas del modelo.

Tipos principales:

```text
Restricción
    │
    ├── de tipo
    ├── de cardinalidad
    ├── de valor
    ├── de identidad
    ├── de exclusión
    ├── de temporalidad
    ├── de contexto
    └── de integridad
```

---

# Restricción de tipo

Ejemplo:

```text
utiliza_ingrediente
```

solo podrá conectar:

```text
Receta

con

Ingrediente
```

---

# Restricción de valor

Ejemplo:

```text
temperatura_celsius
```

podrá limitarse a un intervalo operativo.

```text
-273.15 ≤ valor
```

Una restricción culinaria más específica podrá definir un rango distinto.

---

# Restricción de patrón

Los valores textuales podrán restringirse mediante patrones.

Ejemplo:

```text
identificador:
  patrón: "^[A-Z]+-[0-9]{4}$"
```

---

# Restricción de longitud

Podrán definirse:

- longitud mínima;
- longitud máxima.

Ejemplo:

```text
titulo:
  minLength: 3
  maxLength: 150
```

---

# Restricción de unicidad

Una propiedad podrá declararse única en un ámbito.

Ejemplo:

```text
identificador canónico
```

deberá ser único dentro del SGCC.

---

# Restricción de obligatoriedad

Una propiedad podrá ser obligatoria según:

- clase;
- estado;
- perfil;
- contexto.

Ejemplo:

Una receta en borrador podrá carecer de rendimiento.

Una receta estable deberá declararlo.

---

# Restricción condicional

Ejemplo:

```text
Si técnica = horneado

entonces

temperatura_de_horno es obligatoria
```

Estas restricciones podrán necesitar reglas o esquemas complementarios.

---

# Axioma

Un axioma es una afirmación formal que define o restringe el significado de la ontología.

Tipos principales:

```text
Axioma
    │
    ├── de clase
    ├── de propiedad
    ├── de individuo
    ├── de identidad
    ├── de disjunción
    ├── de equivalencia
    └── de restricción
```

---

# Axioma de subclase

```text
Receta vegetariana
    subtipo_de
Receta
```

---

# Axioma de equivalencia

```text
A ≡ B
```

Define equivalencia semántica completa.

---

# Axioma de disjunción

```text
A disjointWith B
```

Impide que una misma instancia pertenezca a ambas clases en el mismo contexto.

---

# Axioma de dominio

```text
dominio(utiliza_ingrediente) = Receta
```

---

# Axioma de rango

```text
rango(utiliza_ingrediente) = Ingrediente
```

---

# Axioma de individuo

Ejemplo:

```text
ING-0005 es_instancia_de Ingrediente
```

---

# Axioma negativo

Ejemplo:

```text
REC-0042 no_utiliza ING-0017
```

La negación explícita deberá distinguirse de la ausencia de información.

---

# Axiomas necesarios y suficientes

Una clase definida podrá utilizar condiciones equivalentes.

Ejemplo:

```text
Receta sin gluten
    ≡
Receta
    y
no utiliza ningún componente con gluten
```

El modelo deberá tener en cuenta que esta definición puede requerir cierre local de la lista de ingredientes.

---

# Taxonomía

Una taxonomía es una estructura jerárquica de conceptos.

El metamodelo deberá representar:

```text
Taxonomia
    │
    ├── NodoTaxonomico
    ├── ConceptoPreferido
    ├── ConceptoSuperior
    ├── ConceptoInferior
    └── ConceptoRelacionado
```

---

# Jerarquía ontológica frente a taxonómica

Una jerarquía ontológica implica herencia semántica.

Una jerarquía taxonómica puede representar únicamente organización.

Ejemplo ontológico:

```text
Crucífera subtipo_de Verdura
```

Ejemplo organizativo:

```text
Brócoli pertenece_a_categoria Verduras de temporada
```

No deberán confundirse.

---

# Concepto taxonómico

Un concepto taxonómico podrá incluir:

- etiqueta preferida;
- etiquetas alternativas;
- definición;
- concepto superior;
- conceptos inferiores;
- conceptos relacionados;
- nota de alcance;
- fuente.

---

# Clasificación múltiple

Una entidad podrá clasificarse en varias taxonomías.

Ejemplo:

```text
Tomate
    │
    ├── clasificación botánica
    ├── clasificación culinaria
    ├── temporada
    └── perfil sensorial
```

Cada clasificación deberá mantener su contexto.

---

# Rol

Un rol representa una función desempeñada por una entidad dentro de un contexto.

Ejemplo:

```text
Cebolla
```

puede desempeñar el rol de:

```text
Ingrediente principal

Aromático

Guarnición

Base de sofrito
```

Los roles no deberán modelarse necesariamente como clases permanentes del individuo.

---

# Entidad y rol

Deberá distinguirse:

```text
qué es una entidad
```

de:

```text
qué función desempeña
```

Ejemplo:

```text
Arroz
```

es un ingrediente.

En una receta concreta puede desempeñar el rol de:

```text
acompañamiento
```

---

# Modelado de roles

Un rol podrá representarse mediante una relación contextualizada.

```text
Uso de ingrediente
    │
    ├── ingrediente: Arroz
    ├── receta: Curry
    └── rol: Guarnición
```

---

# Estado

Un estado representa una condición temporal de una entidad.

Ejemplos:

```text
crudo

cocido

congelado

fermentado

publicado
```

---

# Estado frente a clase

Un estado deberá modelarse como clase permanente solo cuando represente una categoría estable.

Cuando dependa del tiempo, deberá modelarse mediante:

- entidad de estado;
- relación temporal;
- evento;
- observación.

---

# Transición de estado

Modelo:

```text
Estado inicial

↓

Evento o proceso

↓

Estado final
```

Ejemplo:

```text
Masa cruda

↓

Horneado

↓

Pan cocido
```

---

# Evento

Un evento representa algo que ocurre en el tiempo y puede producir cambios.

Ejemplos:

```text
Cocción

Compra

Fermentación

Publicación

Validación
```

---

# Estructura de un evento

Un evento podrá declarar:

```text
tipo

participantes

inicio

fin

duración

lugar

resultado

agente

estado inicial

estado final
```

---

# Proceso

Un proceso representa una secuencia organizada de actividades o eventos.

Ejemplo:

```text
Preparación de una receta
```

Un proceso podrá contener:

- pasos;
- eventos;
- decisiones;
- transiciones;
- resultados.

---

# Evento frente a proceso

Un evento puede considerarse puntual o delimitado.

Un proceso describe una estructura temporal más compleja.

Ejemplo:

```text
Añadir sal
```

puede ser un evento.

```text
Elaborar un caldo
```

es un proceso.

---

# Acción

Una acción representa una actividad ejecutada por un agente.

Ejemplo:

```text
Cortar

Mezclar

Hornear

Validar
```

Una técnica puede describir el método.

Una acción representa su ejecución concreta.

---

# Agente

Un agente es una entidad capaz de ejecutar acciones.

Ejemplos:

- persona;
- equipo humano;
- sistema;
- robot;
- agente IA;
- herramienta automatizada.

---

# Recurso

Un recurso es una entidad utilizada por una acción o proceso.

Ejemplos:

- ingrediente;
- utensilio;
- equipo;
- documento;
- energía;
- tiempo.

---

# Resultado

Un resultado es una entidad obtenida mediante una acción, evento o proceso.

Ejemplos:

- elaboración;
- plato;
- documento;
- cálculo;
- lista de compra;
- inferencia.

---

# Contexto ontológico

El contexto permite limitar la validez de una afirmación.

Modelo:

```text
Afirmación
    │
    ├── participantes
    ├── tiempo
    ├── lugar
    ├── tradición
    ├── receta
    ├── usuario
    └── condiciones
```

---

# Contexto como entidad

Cuando el contexto sea complejo, deberá modelarse como entidad.

Ejemplo:

```text
CTX-0042
    │
    ├── receta: REC-0012
    ├── dieta: vegetariana
    ├── temperatura: fría
    └── fase: acabado
```

---

# Contexto implícito

Deberá evitarse depender de contexto implícito cuando sea necesario para interpretar correctamente una afirmación.

Ejemplo ambiguo:

```text
Yogur sustituye a nata
```

Ejemplo contextualizado:

```text
Yogur sustituye a nata
en salsas frías
en proporción 1:1
```

---

# Dimensiones de contexto

El metamodelo podrá reconocer:

- contexto culinario;
- contexto temporal;
- contexto geográfico;
- contexto cultural;
- contexto dietético;
- contexto documental;
- contexto operativo;
- contexto de usuario;
- contexto tecnológico.

---

# Temporalidad ontológica

El metamodelo deberá permitir representar:

- instantes;
- intervalos;
- duración;
- recurrencia;
- orden;
- vigencia;
- historia.

---

# Instante

Ejemplo:

```text
2026-07-31T08:30:00+02:00
```

---

# Intervalo

Ejemplo:

```text
desde 2026-07-01

hasta 2026-07-31
```

---

# Intervalo abierto

```text
desde: 2026-07-31

hasta: sin determinar
```

---

# Relación temporal

Las relaciones temporales podrán incluir:

```text
antes_de

después_de

durante

solapa_con

inicia

finaliza
```

---

# Tiempo válido y tiempo de transacción

El metamodelo distinguirá:

```text
Tiempo válido
```

Momento en el que una afirmación se considera verdadera en el dominio.

```text
Tiempo de transacción
```

Momento en el que fue registrada en el sistema.

---

# Cantidad

Una cantidad deberá modelarse como:

```text
Cantidad
    │
    ├── valor
    ├── unidad
    ├── precisión
    ├── tolerancia
    └── tipo de magnitud
```

Ejemplo:

```yaml
valor: 250
unidad: gramo
precision: 1
```

---

# Cantidad exacta y aproximada

El metamodelo deberá distinguir:

- exacta;
- aproximada;
- mínima;
- máxima;
- intervalo;
- a gusto;
- no determinada.

---

# Calidad

Una cualidad representa una característica evaluable.

Ejemplos:

```text
Textura

Aroma

Sabor

Color

Madurez
```

---

# Valor cualitativo

Las cualidades podrán tomar valores controlados.

Ejemplo:

```text
Textura:
  - líquida
  - cremosa
  - crujiente
  - gelatinosa
```

---

# Observación

Una observación representa una afirmación obtenida mediante percepción, medición o prueba.

Ejemplo:

```text
La salsa alcanzó una textura cremosa.
```

Deberá poder declarar:

- observador;
- método;
- fecha;
- entidad observada;
- resultado;
- confianza.

---

# Medición

Una medición es una observación cuantitativa.

Ejemplo:

```text
Temperatura interna = 72 °C
```

---

# Evidencia

Una evidencia respalda una afirmación.

Tipos:

- documental;
- experimental;
- observacional;
- normativa;
- bibliográfica;
- calculada;
- algorítmica.

---

# Procedencia

Todo elemento ontológico relevante deberá poder declarar su procedencia.

Modelo:

```text
Procedencia
    │
    ├── fuente
    ├── autor
    ├── fecha
    ├── método
    ├── versión
    └── licencia
```

---

# Confianza

Una afirmación podrá tener nivel de confianza.

Ejemplo:

```yaml
confianza:
  valor: 0.87
  metodo: prediccion_modelo
```

La confianza pertenece a la afirmación, no necesariamente al concepto.

---

# Afirmación ontológica

Una afirmación representa una proposición sobre entidades.

Ejemplos:

```text
Cebolla es_un Ingrediente

Curry utiliza Cebolla

Cebolla tiene_color Blanco
```

---

# Estructura de una afirmación

```text
Afirmacion
    │
    ├── sujeto
    ├── predicado
    ├── objeto o valor
    ├── contexto
    ├── procedencia
    ├── temporalidad
    ├── confianza
    └── estado
```

---

# Afirmación positiva

Ejemplo:

```text
Receta utiliza Ingrediente
```

---

# Afirmación negativa

Ejemplo:

```text
Receta no_utiliza Ingrediente
```

La ausencia de afirmación no equivale a una afirmación negativa.

---

# Afirmación declarada

Registrada explícitamente por una fuente.

---

# Afirmación inferida

Derivada mediante axiomas o reglas.

---

# Afirmación calculada

Obtenida mediante una operación determinista.

---

# Afirmación predicha

Generada por un modelo probabilístico.

---

# Afirmación hipotética

Utilizada para simulación, planificación o análisis.

No deberá confundirse con conocimiento estable.

---

# Mundo abierto

La ontología asumirá por defecto un modelo de mundo abierto.

```text
No conocido

≠

Falso
```

Que no se sepa si una receta contiene un alérgeno no significa que esté libre de él.

---

# Cierre local

Podrán definirse zonas de mundo cerrado.

Ejemplo:

```text
La lista de ingredientes de esta versión de receta está completa.
```

En ese contexto podrá inferirse que un ingrediente no declarado no forma parte directa de la receta.

El cierre deberá declararse de forma explícita.

---

# Supuesto de nombres no únicos

Dos nombres diferentes podrán representar el mismo individuo.

Un mismo nombre podrá representar individuos distintos.

No deberá aplicarse automáticamente la hipótesis de nombres únicos.

---

# Módulo ontológico

Un módulo ontológico agrupa elementos semánticamente relacionados.

Ejemplo:

```text
ONT-MOD-INGREDIENTES

ONT-MOD-TECNICAS

ONT-MOD-RECETAS
```

---

# Estructura de un módulo

Todo módulo deberá declarar:

```text
Identificador

Nombre

Objetivo

Alcance

Clases

Propiedades

Axiomas

Dependencias

Versión

Estado
```

---

# Módulos propuestos

La ontología del SGCC podrá organizarse inicialmente en:

```text
Ontología SGCC
    │
    ├── Núcleo
    ├── Ingredientes
    ├── Técnicas
    ├── Equipamiento
    ├── Elaboraciones
    ├── Recetas
    ├── Menús
    ├── Nutrición
    ├── Restricciones
    ├── Planificación
    ├── Sensorial
    ├── Procedencia
    ├── Documentación
    └── Gobernanza
```

---

# Módulo núcleo

El módulo núcleo deberá contener conceptos transversales.

Ejemplos:

```text
Entidad

Agente

Proceso

Evento

Recurso

Resultado

Cantidad

Unidad

Contexto

Tiempo

Procedencia
```

---

# Dependencias entre módulos

Un módulo podrá importar elementos de otro.

Ejemplo:

```text
Módulo Recetas
    │
    ├── importa Ingrediente
    ├── importa Técnica
    ├── importa Equipo
    └── importa Cantidad
```

---

# Dependencia acíclica

Las dependencias entre módulos deberán evitar ciclos innecesarios.

Ejemplo problemático:

```text
Módulo A importa B

Módulo B importa A
```

Cuando exista conocimiento compartido deberá extraerse a un módulo común.

---

# Espacio de nombres

Cada módulo deberá disponer de un espacio de nombres lógico o técnico.

Ejemplo conceptual:

```text
sgcc-core:

sgcc-ingredient:

sgcc-recipe:
```

El espacio de nombres deberá evitar colisiones.

---

# Importación ontológica

La importación deberá permitir reutilizar:

- clases;
- propiedades;
- axiomas;
- vocabularios;
- restricciones.

Una importación no deberá copiar y redefinir los elementos importados.

---

# Dependencia externa

El SGCC podrá depender de vocabularios externos.

Ejemplos:

- unidades;
- tiempo;
- procedencia;
- personas;
- organizaciones;
- lugares;
- idiomas.

Estas dependencias deberán documentarse.

---

# Alineación ontológica

La alineación conecta elementos internos con elementos externos.

Tipos:

```text
equivalencia exacta

equivalencia aproximada

más general

más específico

relacionado
```

---

# Metaclase

Una metaclase es una clase cuyas instancias son clases.

Su uso deberá ser limitado y justificado.

Ejemplo potencial:

```text
TipoDeIngrediente
```

cuyas instancias sean categorías como:

```text
Verdura

Especia

Cereal
```

Cuando sea posible, deberá preferirse una jerarquía normal de clases.

---

# Punning o doble uso

Un mismo identificador conceptual podría necesitar actuar como:

- clase;
- individuo.

Ejemplo:

```text
Cocina japonesa
```

podría modelarse como clase de recetas y como objeto cultural.

Este patrón deberá documentarse para evitar ambigüedad.

---

# Clase de relación

Cuando una relación contextualizada necesite identidad, podrá modelarse como clase.

Ejemplo:

```text
UsoDeIngrediente
```

con instancias:

```text
USO-ING-0001
```

---

# Patrón de n-aria

Una relación n-aria deberá transformarse en entidad asociativa.

Modelo:

```text
RelaciónNAria
    │
    ├── participante_1
    ├── participante_2
    ├── participante_3
    └── atributos
```

Ejemplo:

```text
SustitucionContextual
    │
    ├── sustituto
    ├── sustituido
    ├── receta
    ├── proporción
    └── efecto
```

---

# Patrón de composición

La composición expresa una relación fuerte entre todo y partes.

Modelo:

```text
Todo
    │
    └── compuesto_por
            │
            ▼
          Parte
```

Deberán definirse:

- exclusividad;
- dependencia de ciclo de vida;
- transitividad;
- cardinalidad;
- reutilización.

---

# Patrón de agregación

La agregación expresa agrupación débil.

Ejemplo:

```text
Colección contiene Receta
```

La receta puede existir independientemente de la colección.

---

# Patrón de participación

Un participante interviene en un evento o proceso.

Ejemplo:

```text
Cebolla participa_en Sofrito
```

Podrá especificarse el rol:

```text
rol: ingrediente_aromatico
```

---

# Patrón de procedencia

Modelo:

```text
Afirmación
    │
    └── atribuida_a
            │
            ▼
          Fuente
```

---

# Patrón de observación

```text
Observación
    │
    ├── observa
    ├── propiedad
    ├── valor
    ├── método
    └── observador
```

---

# Patrón de planificación

```text
Plan
    │
    ├── objetivo
    ├── actividad
    ├── recurso
    ├── responsable
    ├── fecha
    └── estado
```

---

# Patrón de versión

Un activo versionado deberá separar:

```text
Identidad conceptual

↓

Versión

↓

Representación
```

Ejemplo:

```text
Receta Curry japonés
    │
    ├── Versión 1.0.0
    └── Versión 1.1.0
```

---

# Identidad conceptual y versión

La versión no deberá tratarse como una nueva identidad conceptual salvo que el cambio genere un componente diferente.

---

# Patrón de representación

```text
Activo conceptual
    │
    └── representado_por
            │
            ▼
      Recurso documental
```

---

# Perfil ontológico

Un perfil define el subconjunto de capacidades y restricciones requerido para un contexto.

Ejemplos:

```text
Perfil mínimo

Perfil editorial

Perfil Knowledge Graph

Perfil OWL

Perfil RAG

Perfil seguridad alimentaria
```

---

# Perfil mínimo

El perfil mínimo deberá soportar:

- clases;
- instancias;
- propiedades de datos;
- propiedades de objeto;
- dominio;
- rango;
- jerarquías simples;
- identificadores;
- definiciones.

---

# Perfil estructural

Deberá añadir:

- cardinalidades;
- equivalencias;
- disjunciones;
- restricciones;
- módulos;
- versionado.

---

# Perfil de inferencia

Deberá añadir:

- propiedades lógicas;
- clases definidas;
- cadenas de propiedades;
- reglas;
- materialización;
- explicación.

---

# Perfil de procedencia

Deberá añadir:

- fuentes;
- autoría;
- temporalidad;
- confianza;
- evidencia;
- historial.

---

# Perfil de seguridad alimentaria

Deberá exigir:

- fuentes verificadas;
- evidencia;
- revisión humana;
- control de versiones;
- trazabilidad completa;
- prohibición de inferencias no validadas;
- tratamiento explícito de incertidumbre.

---

# Perfil de conformidad

Cada módulo deberá declarar el perfil que implementa.

Ejemplo:

```yaml
perfil:
  nombre: inferencia
  version: 1.0.0
```

---

# Conformidad de clase

Una clase será conforme cuando:

- tenga identificador;
- tenga nombre canónico;
- incluya definición;
- declare módulo;
- declare estado;
- tenga jerarquía coherente;
- documente restricciones;
- no duplique otra clase;
- disponga de ejemplos cuando sea necesario.

---

# Conformidad de propiedad

Una propiedad será conforme cuando:

- tenga identificador;
- tenga definición;
- declare tipo;
- declare dominio;
- declare rango o tipo de dato;
- defina cardinalidad cuando proceda;
- documente características lógicas;
- no duplique otra propiedad;
- sea compatible con el catálogo de relaciones.

---

# Conformidad de axioma

Un axioma será conforme cuando:

- tenga una semántica inequívoca;
- utilice elementos existentes;
- sea consistente;
- pueda validarse;
- tenga procedencia;
- declare estado;
- no genere contradicciones no gestionadas.

---

# Conformidad de módulo

Un módulo será conforme cuando:

- tenga objetivo;
- tenga alcance;
- declare dependencias;
- no produzca ciclos innecesarios;
- utilice espacios de nombres;
- mantenga cohesión;
- declare versión;
- documente sus elementos públicos.

---

# Contrato YAML de una clase

Ejemplo:

```yaml
id: ONT-CLS-0001
tipo: clase_ontologica
nombre: Ingrediente
version: 1.0.0
estado: estable

modulo: ONT-MOD-INGREDIENTES

definicion: >
  Entidad material utilizada directa o indirectamente
  en una elaboración culinaria.

superclases:
  - ONT-CLS-RECURSO-CULINARIO

subclases:
  - ONT-CLS-VERDURA
  - ONT-CLS-ESPECIA
  - ONT-CLS-CEREAL

disjunta_con:
  - ONT-CLS-EQUIPO

propiedades:
  - ONT-PRP-NOMBRE
  - ONT-PRP-ORIGEN
  - ONT-PRP-ALERGENO
```

---

# Contrato YAML de una propiedad de datos

```yaml
id: ONT-PRP-0042
tipo: propiedad_de_datos
nombre: tiempo_de_coccion
version: 1.0.0
estado: estable

dominio:
  - ONT-CLS-RECETA
  - ONT-CLS-ELABORACION

rango:
  tipo: duracion

cardinalidad:
  minimo: 0
  maximo: 1
```

---

# Contrato YAML de una propiedad de objeto

```yaml
id: ONT-PRP-0010
tipo: propiedad_de_objeto
nombre: utiliza
version: 1.0.0
estado: estable

dominio:
  - ONT-CLS-RECETA
  - ONT-CLS-ELABORACION

rango:
  - ONT-CLS-INGREDIENTE
  - ONT-CLS-EQUIPO
  - ONT-CLS-TECNICA

inversa: ONT-PRP-0011

caracteristicas:
  simetrica: false
  transitiva: false
  funcional: false
  reflexiva: false
```

---

# Contrato YAML de un axioma

```yaml
id: ONT-AXM-0001
tipo: axioma_de_subclase
version: 1.0.0
estado: estable

sujeto: ONT-CLS-RECETA-VEGETARIANA
predicado: subtipo_de
objeto: ONT-CLS-RECETA

procedencia:
  fuente: DOC-0023
  fecha: 2026-07-31
```

---

# Contrato YAML de una restricción

```yaml
id: ONT-RST-0001
tipo: restriccion_de_cardinalidad
version: 1.0.0
estado: estable

aplica_a: ONT-CLS-RECETA
propiedad: ONT-PRP-PRODUCE

cardinalidad:
  minimo: 1

condicion:
  estado_componente: estable
```

---

# Validación del metamodelo

La validación deberá comprobar:

- tipos reconocidos;
- identificadores;
- referencias;
- jerarquías;
- dominio;
- rango;
- cardinalidad;
- compatibilidad lógica;
- ciclos;
- disjunciones;
- coherencia de módulos;
- contratos obligatorios.

---

# Errores estructurales

Ejemplos:

```text
Clase sin identificador

Propiedad sin dominio

Propiedad de datos con rango de clase

Propiedad de objeto con literal como objeto

Axioma con clase inexistente

Módulo con dependencia inexistente
```

---

# Errores semánticos

Ejemplos:

```text
Receta subtipo_de Ingrediente

Equipo disjunto consigo mismo

Propiedad simétrica y asimétrica simultáneamente

Clase equivalente y disjunta con la misma clase

Cardinalidad mínima superior a la máxima
```

---

# Advertencias

Podrán generar advertencias:

- clase sin ejemplos;
- clase sin subclases ni instancias;
- propiedad sin uso;
- módulo excesivamente acoplado;
- concepto demasiado general;
- alias ambiguo;
- dependencia externa sin mapeo;
- restricción sin evidencia.

---

# Integración con especificaciones anteriores

El metamodelo deberá integrar:

```text
ESPECIFICACION_DE_COMPONENTES.md
```

para la identidad y estructura de los componentes,

```text
ESPECIFICACION_DE_RELACIONES.md
```

para el catálogo y comportamiento de las propiedades de objeto,

y:

```text
ESPECIFICACION_DE_DOCUMENTOS.md
```

para sus representaciones documentales.

---

# Relación con el Knowledge Graph

El metamodelo define las estructuras permitidas.

La ontología instancia el metamodelo.

El Knowledge Graph instancia la ontología.

```text
Metamodelo

↓

Ontología

↓

Knowledge Graph
```

Ejemplo:

```text
Metamodelo:
ClaseOntologica
```

```text
Ontología:
Ingrediente
```

```text
Knowledge Graph:
Cebolla
```

---

# Relación con validadores

Los validadores podrán derivar reglas a partir de:

- dominio;
- rango;
- cardinalidades;
- disjunciones;
- tipos de dato;
- estados;
- perfiles;
- restricciones.

---

# Relación con RAG y agentes IA

El metamodelo permitirá que los sistemas inteligentes distingan entre:

- clases;
- instancias;
- relaciones;
- anotaciones;
- hechos;
- inferencias;
- hipótesis;
- restricciones.

Esto reducirá errores como:

- tratar una categoría como ingrediente;
- confundir una receta con un documento;
- interpretar un alias como una entidad distinta;
- asumir como hecho una predicción;
- ignorar el contexto de una sustitución.

---

# Principios de diseño del metamodelo

El metamodelo deberá mantener:

- mínima complejidad suficiente;
- semántica explícita;
- reutilización;
- modularidad;
- independencia tecnológica;
- capacidad de validación;
- compatibilidad evolutiva;
- explicabilidad.

---

# Antipatrones

Deberán evitarse:

- convertir cada valor en una clase;
- convertir cada propiedad en una relación compleja;
- usar clases como etiquetas;
- confundir roles con tipos permanentes;
- duplicar entidades por versión;
- utilizar `sameAs` para similitud;
- declarar disjunciones sin evidencia;
- usar dominio y rango solo como documentación;
- crear metaclases innecesarias;
- introducir contexto como texto libre no estructurado.

---

# Criterio de simplicidad

Cuando existan varias alternativas de modelado deberá preferirse la más sencilla que preserve:

- significado;
- validación;
- inferencia necesaria;
- trazabilidad;
- interoperabilidad.

---

# Criterio de promoción

Un valor o atributo deberá promoverse a entidad ontológica cuando:

- tenga identidad;
- participe en relaciones;
- sea reutilizable;
- tenga propiedades;
- necesite procedencia;
- requiera evolución independiente.

---

# Criterio de contextualización

Una relación deberá contextualizarse cuando:

- cambie según receta;
- dependa de región;
- dependa de tiempo;
- dependa de dieta;
- tenga proporciones;
- incluya excepciones;
- posea atributos propios.

---

# Criterio de especialización

Una subclase o subpropiedad deberá crearse cuando:

- añada semántica;
- restrinja dominio o rango;
- permita inferencias;
- represente una categoría estable;
- sea reutilizable.

No deberá crearse únicamente para facilitar una interfaz.

---

# Madurez progresiva

El metamodelo podrá implementarse gradualmente.

```text
Nivel 1
Clases, instancias y propiedades
```

```text
Nivel 2
Jerarquías, dominio, rango y cardinalidad
```

```text
Nivel 3
Axiomas, disjunciones y clases definidas
```

```text
Nivel 4
Contexto, temporalidad y procedencia
```

```text
Nivel 5
Inferencia avanzada y alineación externa
```

---

# Perfil inicial recomendado

La primera implementación del SGCC debería soportar:

- clases;
- instancias;
- subclases;
- propiedades de datos;
- propiedades de objeto;
- propiedades de anotación;
- dominio;
- rango;
- cardinalidades básicas;
- relaciones inversas;
- disjunciones esenciales;
- procedencia;
- módulos;
- versionado.

---

# Elementos aplazables

Podrán incorporarse más adelante:

- metaclases complejas;
- lógica temporal completa;
- reglas probabilísticas;
- alineación automática;
- razonamiento no monotónico;
- contextos anidados;
- perfiles OWL avanzados;
- lógica difusa.

---

# Conformidad mínima del metamodelo

Una implementación será mínimamente conforme cuando pueda representar:

```text
Clase

Instancia

Propiedad de datos

Propiedad de objeto

Dominio

Rango

Jerarquía

Cardinalidad

Identidad

Versión
```

---

# Conformidad recomendada

Una implementación será conforme con el perfil recomendado cuando además soporte:

- anotaciones;
- equivalencias;
- disjunciones;
- propiedades inversas;
- módulos;
- procedencia;
- estados;
- contexto básico;
- validación estructural.

---

# Conformidad avanzada

Una implementación avanzada deberá soportar:

- clases definidas;
- cadenas de propiedades;
- reglas;
- temporalidad;
- entidades asociativas;
- n-arias;
- razonamiento;
- explicabilidad;
- alineación externa;
- auditoría.

---

# Transición hacia la semántica y la inferencia

La presente parte ha definido:

- niveles ontológicos;
- elementos del metamodelo;
- clases;
- instancias;
- propiedades;
- dominio;
- rango;
- cardinalidades;
- restricciones;
- axiomas;
- taxonomías;
- roles;
- eventos;
- contexto;
- temporalidad;
- módulos;
- patrones de modelado;
- perfiles de conformidad.

La siguiente parte desarrollará la semántica formal y el razonamiento, incluyendo:

- interpretación de axiomas;
- mundo abierto;
- cierre local;
- inferencias;
- clasificación automática;
- reglas;
- cadenas de propiedades;
- consistencia;
- detección de contradicciones;
- validación SHACL;
- explicación;
- materialización;
- razonamiento probabilístico;
- interacción con sistemas RAG y agentes IA.

El metamodelo definido en esta sección constituye el lenguaje estructural mediante el que se construirá y validará la ontología del SGCC.

---

# Semántica formal e inferencia ontológica

La presente sección define cómo debe interpretarse la ontología del Sistema de Gestión del Conocimiento Culinario (SGCC).

Mientras que el metamodelo establece:

- qué elementos existen;
- cómo se describen;
- cómo se estructuran;

esta parte establece:

- qué significan formalmente;
- cómo se interpretan;
- cómo pueden generar nuevo conocimiento;
- cómo se validan;
- cómo se detectan inconsistencias;
- cómo se explican las conclusiones obtenidas mediante razonamiento.

La semántica constituye el puente entre la representación del conocimiento y su utilización por motores de inferencia, sistemas RAG y agentes inteligentes.

---

# Objetivo

El objetivo de esta sección es definir un marco semántico que permita:

- interpretar de forma consistente los conceptos;
- razonar automáticamente sobre el conocimiento;
- detectar contradicciones;
- derivar hechos implícitos;
- validar restricciones;
- justificar inferencias;
- facilitar interoperabilidad con estándares semánticos.

---

# Qué significa "semántica"

La semántica describe el significado de las afirmaciones contenidas en la ontología.

No regula únicamente la sintaxis.

Dos modelos pueden tener exactamente la misma estructura y, sin embargo, significar cosas completamente diferentes.

La semántica evita dicha ambigüedad.

---

# Interpretación ontológica

Toda ontología puede entenderse como un conjunto de afirmaciones sobre el dominio culinario.

Ejemplo:

```text
Receta utiliza Ingrediente
```

No representa únicamente una conexión entre dos nodos.

Representa un hecho con un significado formal.

---

# Universo del discurso

Toda interpretación se realiza sobre un universo del discurso.

En el SGCC dicho universo está formado por:

- ingredientes;
- recetas;
- elaboraciones;
- técnicas;
- utensilios;
- equipos;
- restricciones;
- procesos;
- usuarios;
- documentos;
- entidades auxiliares.

Nada fuera de este universo forma parte de la interpretación semántica salvo referencia explícita.

---

# Interpretación de clases

Una clase representa un conjunto de individuos.

Ejemplo:

```text
Ingrediente
```

representa el conjunto de todos los ingredientes conocidos.

Formalmente:

```text
Ingrediente ⊆ Entidad
```

---

# Interpretación de individuos

Cada individuo representa una entidad concreta del dominio.

Ejemplo:

```text
Cebolla
```

representa un ingrediente específico.

No representa una clase.

---

# Interpretación de propiedades

Las propiedades representan relaciones o atributos.

Ejemplo:

```text
utiliza
```

representa una relación entre:

```text
Receta

↓

Ingrediente
```

---

# Interpretación de axiomas

Los axiomas restringen el conjunto de interpretaciones posibles.

Ejemplo:

```text
RecetaVegetariana
subtipo_de
Receta
```

significa que toda interpretación válida deberá considerar que toda receta vegetariana también es una receta.

---

# Significado de una ontología

Una ontología define un conjunto de modelos posibles.

Cuantos más axiomas existan:

- menor será el número de interpretaciones posibles;
- mayor será la precisión del conocimiento.

---

# Consistencia

Una ontología es consistente cuando existe al menos una interpretación que satisface todos sus axiomas.

Ejemplo consistente:

```text
RecetaVegetariana
subtipo_de
Receta
```

Ejemplo inconsistente:

```text
RecetaVegetariana

disjointWith

Receta
```

junto con:

```text
RecetaVegetariana
subtipo_de
Receta
```

---

# Inconsistencia

Existe inconsistencia cuando no puede existir ninguna interpretación válida.

Las inconsistencias deberán detectarse automáticamente siempre que sea posible.

---

# Completitud

Una ontología puede ser correcta sin ser completa.

El SGCC adopta el principio de que el conocimiento podrá ampliarse progresivamente.

La ausencia de información no implica error.

---

# Mundo abierto

El SGCC adopta por defecto el principio de mundo abierto (Open World Assumption).

Esto significa:

```text
Desconocido

≠

Falso
```

Ejemplo:

Una receta no declara leche.

No puede inferirse automáticamente:

```text
La receta no contiene leche.
```

---

# Consecuencias del mundo abierto

No podrá asumirse automáticamente:

- inexistencia;
- ausencia;
- negación;
- incumplimiento;
- incompatibilidad.

Todo ello requerirá evidencia explícita o un contexto de cierre.

---

# Mundo cerrado contextual

En determinados contextos podrá declararse un modelo de mundo cerrado.

Ejemplo:

```text
La lista de ingredientes ha sido verificada como completa.
```

En ese caso podrá inferirse:

```text
Ingrediente no declarado

↓

no utilizado
```

Este comportamiento deberá estar explícitamente documentado.

---

# Hipótesis de nombres

El SGCC no asumirá automáticamente que:

```text
Tomate

≠

Solanum lycopersicum
```

Podrán representar el mismo individuo.

Las equivalencias deberán declararse explícitamente.

---

# Identidad semántica

La identidad implica que dos referencias representan exactamente la misma entidad.

Ejemplo:

```text
A sameAs B
```

Consecuencias:

Todas las propiedades conocidas de A serán también propiedades de B.

---

# Diferencia semántica

Podrá declararse explícitamente:

```text
A differentFrom B
```

para evitar fusiones erróneas.

---

# Equivalencia de clases

Dos clases equivalentes representan exactamente el mismo conjunto de individuos.

Ejemplo:

```text
PreparaciónVegana

≡

PreparaciónSinIngredientesAnimales
```

Solo deberá utilizarse cuando la equivalencia sea absoluta.

---

# Equivalencia de propiedades

Dos propiedades serán equivalentes cuando produzcan exactamente el mismo significado.

No deberá utilizarse únicamente porque dos nombres sean parecidos.

---

# Subsumción

Una clase A subsume una clase B cuando:

```text
B subtipo_de A
```

Todo individuo de B pertenece también a A.

---

# Clasificación automática

Un razonador podrá clasificar automáticamente individuos y clases.

Ejemplo:

Si se define:

```text
RecetaVegetariana

≡

Receta

y

no utiliza Carne
```

un razonador podrá clasificar automáticamente una receta concreta como vegetariana.

---

# Inferencia

Una inferencia consiste en obtener nuevo conocimiento a partir del conocimiento existente.

Modelo:

```text
Conocimiento declarado

↓

Reglas y axiomas

↓

Conocimiento inferido
```

---

# Tipos de inferencia

El SGCC podrá utilizar:

- inferencia jerárquica;
- inferencia por propiedades;
- inferencia por restricciones;
- inferencia por reglas;
- inferencia por cadenas;
- inferencia temporal;
- inferencia contextual;
- inferencia probabilística.

---

# Inferencia jerárquica

Ejemplo:

```text
Brócoli

es_instancia_de

Crucífera

Crucífera

subtipo_de

Verdura
```

Conclusión:

```text
Brócoli

es_instancia_de

Verdura
```

---

# Inferencia de pertenencia

Si:

```text
Verdura

subtipo_de

Ingrediente
```

entonces:

```text
Brócoli

es_instancia_de

Ingrediente
```

---

# Inferencia por dominio

Si:

```text
utiliza

dominio

Receta
```

y se registra:

```text
X utiliza Cebolla
```

podrá inferirse:

```text
X

es una

Receta
```

---

# Inferencia por rango

Si:

```text
utiliza

rango

Ingrediente
```

entonces:

```text
Receta utiliza X
```

permite inferir:

```text
X

es un

Ingrediente
```

---

# Inferencia por equivalencia

Si:

```text
A sameAs B
```

y:

```text
A tiene_color Blanco
```

entonces:

```text
B tiene_color Blanco
```

---

# Inferencia por propiedades inversas

Ejemplo:

```text
Receta utiliza Ingrediente
```

↓

```text
Ingrediente es_utilizado_por Receta
```

---

# Inferencia por simetría

Ejemplo:

```text
Tomate combina_con Albahaca
```

↓

```text
Albahaca combina_con Tomate
```

---

# Inferencia por transitividad

Ejemplo:

```text
Crucífera

subtipo_de

Verdura

Verdura

subtipo_de

Ingrediente
```

↓

```text
Crucífera

subtipo_de

Ingrediente
```

---

# Inferencia por cadenas

Ejemplo:

```text
Receta utiliza Ingrediente

Ingrediente contiene_alergeno Gluten
```

↓

```text
Receta contiene_alergeno Gluten
```

---

# Inferencia por composición

Varias propiedades podrán combinarse para producir una nueva afirmación.

Ejemplo:

```text
Receta

produce

Salsa

Salsa

tiene_textura

Cremosa
```

↓

```text
Receta

produce_textura

Cremosa
```

---

# Inferencia por restricciones

Ejemplo:

```text
RecetaVegana

utiliza solo IngredienteVegano
```

Si aparece:

```text
Carne
```

la ontología detectará incompatibilidad.

---

# Inferencia existencial

Si una clase exige:

```text
utiliza some Ingrediente
```

la existencia de una instancia implica que existe al menos un ingrediente, aunque todavía no se conozca cuál.

---

# Inferencia universal

Ejemplo:

```text
utiliza only IngredienteVegetal
```

Todo objeto relacionado mediante `utiliza` deberá pertenecer a esa clase.

---

# Inferencia por cardinalidad

Ejemplo:

```text
exactly 1 nivel_de_dificultad
```

Si aparecen dos niveles simultáneamente se producirá una inconsistencia o requerirá resolución.

---

# Inferencia contextual

Las inferencias podrán depender del contexto.

Ejemplo:

```text
Yogur sustituye Nata
```

solo:

```text
contexto:
  salsa_fria
```

Fuera de ese contexto no deberá inferirse automáticamente.

---

# Inferencia temporal

Ejemplo:

```text
Ingrediente disponible

desde marzo

hasta junio
```

La disponibilidad dependerá de la fecha consultada.

---

# Inferencia basada en estados

Ejemplo:

```text
Receta estable

↓

publicable
```

Una receta en borrador no heredará esa propiedad.

---

# Inferencia probabilística

El SGCC podrá incorporar inferencias generadas mediante IA.

Ejemplo:

```yaml
prediccion:
  confianza: 0.86
```

Estas inferencias deberán distinguirse claramente de las deterministas.

---

# Niveles de certeza

Toda inferencia podrá clasificarse como:

```text
Determinista

↓

Probable

↓

Hipotética
```

Cada nivel requerirá diferente tratamiento.

---

# Materialización

Una inferencia podrá:

- calcularse bajo demanda;
- almacenarse permanentemente;
- almacenarse temporalmente.

La materialización deberá conservar trazabilidad.

---

# Recalculado

Las inferencias materializadas deberán regenerarse cuando cambien:

- axiomas;
- reglas;
- relaciones;
- propiedades;
- contexto.

---

# Explicabilidad

Toda inferencia deberá poder explicarse.

Ejemplo:

```text
Receta contiene gluten

↓

porque

utiliza Harina

↓

Harina contiene gluten
```

---

# Cadena de explicación

Toda explicación deberá identificar:

- premisas;
- reglas utilizadas;
- conclusiones;
- excepciones;
- nivel de confianza.

---

# Razonador

El razonador interpreta la ontología y produce inferencias.

Sus funciones incluyen:

- clasificación;
- detección de inconsistencias;
- comprobación de axiomas;
- validación;
- generación de conocimiento implícito.

---

# Clasificación automática de clases

El razonador podrá reorganizar clases según su definición formal.

Esto evita mantener jerarquías manuales inconsistentes.

---

# Clasificación automática de individuos

Los individuos podrán clasificarse automáticamente.

Ejemplo:

```text
Receta

↓

no utiliza ingredientes animales
```

↓

```text
RecetaVegana
```

---

# Satisfacibilidad

Una clase es satisfacible cuando puede tener instancias.

Ejemplo:

```text
Receta

y

NoReceta
```

si ambas clases son disjuntas:

```text
insatisfacible
```

---

# Clase vacía

Una clase vacía puede ser correcta si no existen todavía instancias.

No deberá confundirse con una clase imposible.

---

# Detección de contradicciones

El razonador deberá detectar:

- clases incompatibles;
- individuos incompatibles;
- restricciones incumplidas;
- dominios incorrectos;
- rangos incorrectos;
- cardinalidades inválidas.

---

# Contradicciones por identidad

Ejemplo:

```text
A sameAs B

A differentFrom B
```

La ontología será inconsistente.

---

# Contradicciones por disjunción

Ejemplo:

```text
IngredienteAnimal

disjointWith

IngredienteVegetalExclusivo
```

Una misma instancia no podrá pertenecer a ambas.

---

# Contradicciones temporales

Ejemplo:

```text
Disponible

↓

hasta junio
```

y simultáneamente:

```text
Disponible

↓

solo diciembre
```

para el mismo contexto.

---

# Contradicciones contextuales

Ejemplo:

```text
Sustitución válida

↓

solo en horno
```

y:

```text
solo en preparaciones frías
```

para exactamente la misma instancia.

---

# Consistencia local

Un módulo podrá ser consistente individualmente.

---

# Consistencia global

La ontología completa deberá comprobar:

- dependencias;
- alineaciones;
- importaciones;
- axiomas compartidos.

---

# Razonamiento monotónico

Por defecto, el SGCC seguirá un modelo monotónico.

Es decir:

Agregar nuevo conocimiento no invalidará inferencias anteriores salvo modificación explícita de las premisas.

---

# Razonamiento no monotónico

Podrá utilizarse de forma limitada para:

- excepciones;
- preferencias;
- conocimiento incompleto;
- recomendaciones culinarias.

Deberá estar claramente identificado.

---

# Excepciones

Las excepciones no deberán codificarse mediante contradicciones.

Ejemplo:

```text
Regla general

↓

Aceite soporta altas temperaturas
```

Excepción:

```text
Aceite de lino
```

Deberá modelarse explícitamente.

---

# Prioridad entre reglas

Cuando varias reglas entren en conflicto deberá definirse prioridad.

Posibles criterios:

- seguridad alimentaria;
- evidencia;
- procedencia;
- especificidad;
- contexto.

---

# SHACL y validación semántica

El SGCC podrá utilizar perfiles SHACL para validar:

- clases;
- propiedades;
- cardinalidades;
- tipos;
- restricciones;
- patrones.

La validación SHACL complementa, pero no sustituye, al razonamiento ontológico.

---

# Validación estructural vs semántica

La validación estructural comprueba:

- formato;
- identificadores;
- tipos.

La validación semántica comprueba:

- significado;
- coherencia;
- consistencia;
- inferencias.

---

# Procedencia de inferencias

Toda inferencia relevante deberá registrar:

- reglas utilizadas;
- fecha;
- razonador;
- versión;
- evidencia;
- confianza.

---

# Evidencia

Las conclusiones podrán apoyarse en:

- hechos declarados;
- hechos inferidos;
- observaciones;
- cálculos;
- IA;
- documentación.

---

# Incertidumbre

La ontología deberá distinguir:

- desconocido;
- improbable;
- probable;
- confirmado.

---

# Gestión de incertidumbre

No toda afirmación requiere el mismo nivel de certeza.

Especialmente en:

- maridajes;
- sustituciones;
- recomendaciones;
- IA.

---

# Explicabilidad para IA

Las respuestas generadas por agentes deberán indicar:

- conceptos utilizados;
- reglas;
- inferencias;
- fuentes.

Esto permitirá auditoría y confianza.

---

# Compatibilidad con RAG

Las relaciones y axiomas permitirán:

- expansión semántica;
- recuperación contextual;
- navegación por conceptos;
- reducción de ambigüedad.

---

# Compatibilidad con Knowledge Graph

El Knowledge Graph almacenará hechos.

La ontología proporcionará:

- significado;
- reglas;
- restricciones;
- clasificación.

---

# Compatibilidad con agentes

Los agentes deberán distinguir entre:

- hecho declarado;
- inferencia;
- hipótesis;
- recomendación;
- predicción.

Nunca deberán presentar una predicción como un hecho canónico.

---

# Métricas semánticas

Podrán calcularse indicadores como:

- consistencia;
- cobertura;
- profundidad jerárquica;
- conectividad;
- reutilización;
- densidad semántica;
- porcentaje de inferencias;
- explicabilidad;
- conflictos abiertos.

---

# Antipatrones semánticos

Deberán evitarse:

- inferencias sin trazabilidad;
- reglas contradictorias;
- uso excesivo de equivalencias;
- cadenas de propiedades demasiado largas;
- excepciones implícitas;
- clases imposibles;
- axiomas redundantes.

---

# Principios de razonamiento

El razonamiento del SGCC deberá ser:

- reproducible;
- explicable;
- trazable;
- determinista cuando sea posible;
- contextual;
- modular;
- seguro.

---

# Transición hacia la representación e interoperabilidad

La presente parte ha definido:

- interpretación formal;
- mundo abierto;
- identidad;
- consistencia;
- inferencias;
- razonamiento;
- explicabilidad;
- validación semántica;
- incertidumbre;
- integración con IA.

La siguiente parte establecerá cómo representar esta ontología de forma interoperable mediante:

- RDF;
- OWL;
- Turtle;
- JSON-LD;
- Markdown;
- YAML;
- Neo4j;
- PostgreSQL;
- APIs;
- GraphQL;
- sistemas RAG;
- MCP;
- agentes inteligentes;

garantizando que todas las representaciones preserven exactamente la misma semántica definida en esta especificación.

---

# Representación e interoperabilidad ontológica

La presente sección define cómo deberá representarse, serializarse, almacenarse, intercambiarse y consumirse la ontología del Sistema de Gestión del Conocimiento Culinario (SGCC).

Las partes anteriores han establecido:

- los fundamentos ontológicos;
- el metamodelo;
- la semántica formal;
- las reglas de inferencia.

Esta parte define cómo preservar dicho significado a través de diferentes tecnologías y formatos.

El objetivo no es imponer una única representación.

El objetivo es garantizar que todas las representaciones compatibles expresen el mismo modelo conceptual.

---

# Objetivo

Esta sección tiene como objetivos:

- establecer representaciones canónicas;
- definir formatos de intercambio;
- asegurar interoperabilidad;
- evitar pérdida semántica;
- facilitar sincronización;
- soportar múltiples tecnologías;
- permitir evolución gradual;
- facilitar integración con Knowledge Graph;
- soportar RAG y agentes inteligentes;
- preservar identidad, contexto y procedencia.

---

# Alcance

Esta parte regula:

- representación documental;
- serialización estructurada;
- representación semántica;
- almacenamiento relacional;
- almacenamiento en grafos;
- APIs;
- GraphQL;
- exportación e importación;
- sincronización;
- compatibilidad;
- mapeos;
- perfiles de representación;
- integración con RAG;
- integración con MCP;
- integración con agentes IA.

No regula directamente:

- la gobernanza del vocabulario;
- el proceso de aprobación de cambios;
- la deprecación;
- los roles de revisión;
- la política de versionado ontológico.

Estos aspectos se desarrollarán en la parte siguiente.

---

# Principio de equivalencia semántica

Todas las representaciones deberán preservar el mismo significado.

Ejemplo conceptual:

```text
REC-0001 utiliza ING-0005
```

podrá representarse como:

- YAML;
- JSON;
- RDF;
- Turtle;
- triple de grafo;
- fila relacional;
- respuesta API.

La sintaxis podrá cambiar.

La semántica no.

---

# Separación entre modelo y representación

El SGCC deberá distinguir:

```text
Modelo ontológico
```

de:

```text
Representación técnica
```

El modelo define:

- clases;
- propiedades;
- axiomas;
- restricciones;
- contexto;
- inferencias.

La representación define cómo se expresan técnicamente.

---

# Fuente canónica

El SGCC deberá declarar una fuente canónica para cada tipo de artefacto ontológico.

Podrá establecerse, por ejemplo:

```text
Definición normativa

↓

Markdown
```

```text
Serialización operativa

↓

YAML o JSON
```

```text
Representación semántica

↓

RDF/OWL
```

```text
Instancias operativas

↓

Knowledge Graph
```

La fuente canónica deberá evitar divergencias entre formatos.

---

# Tipos de representación

La ontología podrá representarse mediante:

```text
Representación humana

Representación estructurada

Representación semántica

Representación persistente

Representación de intercambio

Representación de consulta

Representación para IA
```

---

# Representación humana

La representación humana deberá priorizar:

- legibilidad;
- comprensión;
- revisión;
- trazabilidad;
- documentación.

El formato principal podrá ser Markdown.

---

# Representación estructurada

La representación estructurada deberá priorizar:

- parseabilidad;
- validación;
- automatización;
- generación;
- interoperabilidad.

Los formatos recomendados serán:

- YAML;
- JSON.

---

# Representación semántica

La representación semántica deberá permitir:

- axiomas;
- inferencias;
- equivalencias;
- restricciones;
- alineación externa.

Los formatos principales serán:

- RDF;
- RDFS;
- OWL;
- SKOS;
- SHACL;
- JSON-LD;
- Turtle.

---

# Representación persistente

La persistencia podrá realizarse mediante:

- base de datos relacional;
- base de datos de grafos;
- triple store;
- almacenamiento documental;
- almacenamiento híbrido.

---

# Representación de intercambio

El intercambio podrá utilizar:

- JSON;
- JSON-LD;
- RDF/XML;
- Turtle;
- CSV controlado;
- APIs REST;
- GraphQL;
- exportaciones empaquetadas.

---

# Representación para IA

Los sistemas de inteligencia artificial podrán consumir:

- fragmentos Markdown;
- JSON estructurado;
- JSON-LD;
- subgrafos;
- contexto serializado;
- embeddings;
- metadatos;
- rutas de explicación.

---

# Markdown como representación normativa

Markdown será adecuado para:

- definiciones;
- decisiones;
- ejemplos;
- tablas;
- restricciones;
- explicación;
- revisión humana.

No deberá considerarse suficiente por sí solo para razonamiento automático.

---

# Estructura Markdown recomendada

Una clase podrá documentarse así:

```markdown
## Ingrediente

**Identificador:** ONT-CLS-0001  
**Módulo:** Ingredientes  
**Estado:** Estable  
**Versión:** 1.0.0

### Definición

Entidad material utilizada directa o indirectamente
en una elaboración culinaria.

### Superclases

- Recurso culinario

### Subclases

- Verdura
- Especia
- Cereal

### Propiedades

- nombre
- origen
- contiene_alergeno
```

---

# Limitaciones de Markdown

Markdown no representa formalmente por sí mismo:

- semántica de clase;
- dominio;
- rango;
- equivalencia;
- disjunción;
- transitividad;
- cardinalidad;
- inferencia.

Estas capacidades deberán derivarse de formatos estructurados o semánticos.

---

# YAML como representación estructurada

YAML será adecuado para:

- edición humana;
- validación;
- configuración;
- generación de artefactos;
- versionado en Git.

---

# Ejemplo YAML de módulo

```yaml
id: ONT-MOD-INGREDIENTES
tipo: modulo_ontologico
nombre: Ingredientes
version: 1.0.0
estado: estable

namespace: sgcc-ingredient

dependencias:
  - ONT-MOD-CORE

clases:
  - ONT-CLS-INGREDIENTE
  - ONT-CLS-VERDURA
  - ONT-CLS-ESPECIA

propiedades:
  - ONT-PRP-CONTIENE-ALERGENO
  - ONT-PRP-TIENE-ORIGEN
```

---

# Ejemplo YAML de individuo

```yaml
id: ING-0005
tipo: individuo
clase:
  - ONT-CLS-INGREDIENTE
  - ONT-CLS-CEREAL

nombre: Arroz basmati

propiedades:
  tiene_origen:
    - LOC-INDIA
  tiene_color:
    - blanco
```

---

# Ventajas de YAML

YAML ofrece:

- legibilidad;
- comentarios;
- edición manual;
- compatibilidad con Git;
- validación mediante esquemas;
- integración sencilla con pipelines.

---

# Riesgos de YAML

Deberán controlarse:

- ambigüedad de tipos;
- indentación;
- valores implícitos;
- fechas interpretadas automáticamente;
- duplicidad de claves;
- referencias no resueltas.

---

# Reglas YAML

Toda representación YAML deberá:

- utilizar UTF-8;
- evitar claves duplicadas;
- declarar versiones;
- usar identificadores canónicos;
- evitar inferir tipos ambiguos;
- separar valores y unidades;
- utilizar listas explícitas;
- referenciar entidades por identificador.

---

# JSON como representación de intercambio

JSON será adecuado para:

- APIs;
- integración;
- validación;
- persistencia documental;
- comunicación entre servicios.

---

# Ejemplo JSON de una relación

```json
{
  "id": "REL-INST-0001",
  "type": "ontology_assertion",
  "subject": "REC-0001",
  "predicate": "ONT-PRP-UTILIZA",
  "object": "ING-0005",
  "context": {
    "phase": "cooking"
  },
  "provenance": {
    "source": "DOC-0042"
  }
}
```

---

# Esquemas JSON

Las representaciones JSON deberán validarse mediante JSON Schema cuando sea posible.

Los esquemas deberán comprobar:

- propiedades obligatorias;
- tipos;
- formatos;
- enumeraciones;
- patrones;
- referencias;
- cardinalidades básicas;
- estructuras anidadas.

---

# Limitaciones de JSON Schema

JSON Schema valida estructura.

No sustituye:

- razonamiento ontológico;
- inferencia;
- equivalencia;
- transitividad;
- consistencia global.

---

# JSON-LD

JSON-LD permitirá combinar:

- facilidad de uso de JSON;
- identidad mediante URI;
- semántica RDF;
- interoperabilidad web.

---

# Ejemplo JSON-LD

```json
{
  "@context": {
    "sgcc": "https://novacoquinaria.example/ontology/",
    "uses": {
      "@id": "sgcc:utiliza",
      "@type": "@id"
    },
    "type": "@type"
  },
  "@id": "sgcc:REC-0001",
  "type": "sgcc:Receta",
  "uses": "sgcc:ING-0005"
}
```

---

# Contexto JSON-LD

El contexto JSON-LD deberá definir:

- prefijos;
- propiedades;
- tipos;
- identificadores;
- coerciones;
- idiomas;
- contenedores.

---

# Contextos versionados

Los contextos JSON-LD deberán versionarse.

Ejemplo:

```text
/context/1.0.0
```

Un cambio incompatible no deberá publicarse bajo la misma URI.

---

# RDF

RDF representará conocimiento mediante triples:

```text
Sujeto

Predicado

Objeto
```

Ejemplo:

```text
REC-0001 utiliza ING-0005
```

---

# Triple RDF

Una afirmación podrá representarse como:

```text
<REC-0001> <utiliza> <ING-0005>
```

---

# Recursos RDF

Los recursos deberán identificarse mediante URI persistentes.

Ejemplo conceptual:

```text
https://novacoquinaria.example/resource/REC-0001
```

---

# URI persistentes

Las URI deberán:

- ser estables;
- ser únicas;
- no depender de rutas internas;
- evitar nombres volátiles;
- permitir resolución;
- conservar historial.

---

# Estrategia de URI

Podrán distinguirse espacios para:

```text
ontology/

resource/

property/

concept/

shape/

rule/
```

Ejemplo:

```text
https://novacoquinaria.example/ontology/Ingrediente
```

```text
https://novacoquinaria.example/resource/ING-0005
```

---

# RDF Schema

RDFS podrá utilizarse para representar:

- clases;
- subclases;
- propiedades;
- subpropiedades;
- dominio;
- rango;
- etiquetas;
- comentarios.

---

# Ejemplo RDFS

```turtle
sgcc:Ingrediente
    a rdfs:Class ;
    rdfs:label "Ingrediente"@es ;
    rdfs:subClassOf sgcc:RecursoCulinario .
```

---

# OWL

OWL permitirá expresar semántica más rica.

Podrá representar:

- equivalencias;
- disjunciones;
- cardinalidades;
- propiedades inversas;
- propiedades funcionales;
- transitividad;
- clases definidas;
- restricciones.

---

# Ejemplo OWL en Turtle

```turtle
sgcc:RecetaVegetariana
    a owl:Class ;
    rdfs:subClassOf sgcc:Receta ;
    owl:disjointWith sgcc:RecetaConCarne .
```

---

# Perfiles OWL

El SGCC podrá utilizar distintos perfiles.

---

## OWL EL

Adecuado para:

- ontologías grandes;
- jerarquías;
- clasificación eficiente;
- relaciones existenciales.

---

## OWL QL

Adecuado para:

- consultas sobre bases relacionales;
- virtualización;
- acceso mediante SQL.

---

## OWL RL

Adecuado para:

- reglas;
- inferencia basada en motores;
- integración con grafos RDF.

---

# Perfil recomendado

La primera implementación debería priorizar un subconjunto compatible con OWL RL o un perfil equivalente de baja complejidad.

Esto facilitará:

- inferencia práctica;
- reglas comprensibles;
- implementación progresiva;
- integración con Knowledge Graph.

---

# Restricciones de OWL

No toda necesidad de validación deberá modelarse mediante OWL.

OWL está orientado a razonamiento bajo mundo abierto.

Para validación de datos deberá complementarse con SHACL.

---

# Turtle

Turtle será el formato recomendado para:

- edición semántica;
- revisión;
- control de versiones;
- ejemplos;
- exportación RDF.

---

# Ejemplo Turtle completo

```turtle
@prefix sgcc: <https://novacoquinaria.example/ontology/> .
@prefix res: <https://novacoquinaria.example/resource/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

res:REC-0001
    rdf:type sgcc:Receta ;
    sgcc:utiliza res:ING-0005 .

res:ING-0005
    rdf:type sgcc:Ingrediente ;
    rdfs:label "Arroz basmati"@es .
```

---

# RDF/XML

RDF/XML podrá soportarse por interoperabilidad.

No será el formato preferido para edición manual debido a:

- verbosidad;
- complejidad;
- menor legibilidad.

---

# N-Triples y N-Quads

N-Triples podrá utilizarse para:

- exportación simple;
- procesamiento masivo;
- comparación;
- pruebas.

N-Quads permitirá añadir contexto mediante grafos nombrados.

---

# Grafos nombrados

Los grafos nombrados permitirán separar:

- fuentes;
- versiones;
- módulos;
- contextos;
- datos declarados;
- datos inferidos;
- datos importados.

---

# Ejemplo de grafo nombrado

```text
Grafo: fuente DOC-0042
```

contiene:

```text
REC-0001 utiliza ING-0005
```

---

# RDF-star

RDF-star podrá emplearse para anotar relaciones.

Ejemplo conceptual:

```turtle
<< res:REC-0001 sgcc:utiliza res:ING-0005 >>
    sgcc:cantidad "250" ;
    sgcc:unidad sgcc:Gramo .
```

---

# Reificación RDF

Cuando RDF-star no esté disponible, una relación contextualizada podrá reificarse.

Ejemplo:

```text
UsoDeIngrediente
    │
    ├── sujeto: REC-0001
    ├── objeto: ING-0005
    ├── cantidad: 250
    └── unidad: gramo
```

---

# SKOS

SKOS podrá utilizarse para:

- taxonomías;
- tesauros;
- vocabularios controlados;
- etiquetas;
- conceptos relacionados;
- alineación terminológica.

---

# Elementos SKOS recomendados

Podrán utilizarse:

```text
skos:Concept

skos:ConceptScheme

skos:prefLabel

skos:altLabel

skos:broader

skos:narrower

skos:related

skos:scopeNote
```

---

# Ontología y SKOS

SKOS no deberá sustituir a OWL cuando se necesiten:

- axiomas;
- restricciones;
- clases formales;
- inferencias lógicas.

SKOS será adecuado para organización conceptual y terminológica.

---

# Ejemplo SKOS

```turtle
sgcc:Especia
    a skos:Concept ;
    skos:prefLabel "Especia"@es ;
    skos:broader sgcc:Ingrediente ;
    skos:scopeNote "Ingrediente utilizado principalmente por su aroma o sabor."@es .
```

---

# SHACL

SHACL permitirá validar grafos RDF.

Podrá comprobar:

- tipos;
- propiedades obligatorias;
- cardinalidad;
- valores;
- patrones;
- clases de destino;
- estructuras complejas.

---

# Ejemplo SHACL

```turtle
sgcc:RecetaShape
    a sh:NodeShape ;
    sh:targetClass sgcc:Receta ;
    sh:property [
        sh:path sgcc:utiliza ;
        sh:minCount 1 ;
        sh:class sgcc:Ingrediente
    ] .
```

---

# SHACL Core

SHACL Core deberá utilizarse para validaciones básicas.

Ejemplos:

- obligatoriedad;
- cardinalidad;
- tipo;
- patrón;
- rango;
- lista controlada.

---

# SHACL-SPARQL

SHACL-SPARQL podrá utilizarse para restricciones complejas.

Ejemplo:

```text
Si la técnica es horneado,
debe existir temperatura de horno.
```

---

# Shapes como artefactos versionados

Cada shape deberá disponer de:

- identificador;
- versión;
- estado;
- módulo;
- descripción;
- pruebas.

---

# SPARQL

SPARQL será el lenguaje principal de consulta para representaciones RDF.

Podrá utilizarse para:

- recuperación;
- navegación;
- agregación;
- validación;
- inferencia materializada;
- extracción para RAG.

---

# Ejemplo SPARQL

```sparql
SELECT ?ingrediente
WHERE {
  sgcc:REC-0001 sgcc:utiliza ?ingrediente .
}
```

---

# SPARQL CONSTRUCT

Podrá utilizarse para generar subgrafos.

Ejemplo:

```sparql
CONSTRUCT {
  sgcc:REC-0001 sgcc:utiliza ?ingrediente .
}
WHERE {
  sgcc:REC-0001 sgcc:utiliza ?ingrediente .
}
```

---

# SPARQL ASK

Podrá utilizarse para validaciones booleanas.

Ejemplo:

```sparql
ASK {
  sgcc:REC-0001 sgcc:contieneAlergeno sgcc:Gluten .
}
```

---

# SPARQL UPDATE

Las actualizaciones deberán gobernarse cuidadosamente.

No deberán realizarse cambios directos que eviten:

- validación;
- trazabilidad;
- versionado;
- auditoría.

---

# Bases de datos de grafos RDF

La ontología podrá almacenarse en:

- triple stores;
- quad stores;
- motores SPARQL;
- plataformas semánticas.

Estas tecnologías serán adecuadas cuando se requiera:

- razonamiento;
- estándares RDF;
- federación;
- interoperabilidad.

---

# Grafos de propiedades

La ontología y sus instancias también podrán representarse mediante grafos de propiedades.

Modelo:

```text
Nodo

Arista

Propiedades
```

Ejemplo:

```text
(:Receta {id: "REC-0001"})
    -[:UTILIZA {cantidad: 250}]->
(:Ingrediente {id: "ING-0005"})
```

---

# Ventajas del grafo de propiedades

Ofrece:

- consultas de navegación;
- alto rendimiento en rutas;
- propiedades en relaciones;
- modelado intuitivo;
- integración con aplicaciones.

---

# Limitaciones del grafo de propiedades

No siempre representa de forma nativa:

- semántica RDF;
- URI;
- axiomas OWL;
- equivalencias;
- razonamiento estándar.

Deberán definirse mapeos explícitos.

---

# Neo4j

Neo4j podrá utilizarse como implementación de grafo de propiedades.

Los nodos podrán representar:

- individuos;
- clases;
- documentos;
- contextos;
- reglas;
- fuentes.

Las relaciones podrán representar:

- propiedades de objeto;
- pertenencia;
- procedencia;
- temporalidad.

---

# Modelo Neo4j de instancia

```cypher
CREATE (r:Receta {
  id: "REC-0001",
  nombre: "Curry japonés"
})

CREATE (i:Ingrediente {
  id: "ING-0005",
  nombre: "Arroz basmati"
})

CREATE (r)-[:UTILIZA]->(i)
```

---

# Modelo Neo4j de ontología

Las clases podrán modelarse como nodos:

```text
(:OntologyClass)
```

y la jerarquía mediante:

```text
[:SUBCLASS_OF]
```

---

# Separación entre grafo ontológico y grafo de instancias

Podrán utilizarse:

```text
Grafo ontológico

Grafo de conocimiento

Grafo de procedencia
```

o un único grafo con etiquetas y espacios de nombres diferenciados.

---

# Mapeo RDF a grafo de propiedades

Deberá definirse cómo transformar:

```text
Clase RDF

↓

Label o nodo de clase
```

```text
Propiedad RDF

↓

Tipo de relación
```

```text
Literal RDF

↓

Propiedad de nodo
```

```text
Relación contextualizada

↓

Arista con propiedades o nodo asociativo
```

---

# PostgreSQL

PostgreSQL podrá utilizarse para:

- metadatos;
- componentes;
- versiones;
- relaciones;
- validaciones;
- auditoría;
- integración transaccional.

---

# Modelo relacional básico

Podrán existir tablas como:

```text
ontology_elements

ontology_classes

ontology_properties

ontology_axioms

ontology_modules

ontology_assertions
```

---

# Tabla de clases

Ejemplo conceptual:

```sql
CREATE TABLE ontology_classes (
    id VARCHAR PRIMARY KEY,
    canonical_name VARCHAR NOT NULL,
    definition TEXT NOT NULL,
    module_id VARCHAR NOT NULL,
    version VARCHAR NOT NULL,
    status VARCHAR NOT NULL
);
```

---

# Tabla de propiedades

```sql
CREATE TABLE ontology_properties (
    id VARCHAR PRIMARY KEY,
    canonical_name VARCHAR NOT NULL,
    property_type VARCHAR NOT NULL,
    domain_id VARCHAR,
    range_id VARCHAR,
    inverse_id VARCHAR,
    version VARCHAR NOT NULL,
    status VARCHAR NOT NULL
);
```

---

# Tabla de axiomas

```sql
CREATE TABLE ontology_axioms (
    id VARCHAR PRIMARY KEY,
    axiom_type VARCHAR NOT NULL,
    subject_id VARCHAR NOT NULL,
    predicate_id VARCHAR,
    object_id VARCHAR,
    payload JSONB,
    version VARCHAR NOT NULL,
    status VARCHAR NOT NULL
);
```

---

# Tabla de afirmaciones

```sql
CREATE TABLE ontology_assertions (
    id VARCHAR PRIMARY KEY,
    subject_id VARCHAR NOT NULL,
    predicate_id VARCHAR NOT NULL,
    object_id VARCHAR,
    literal_value JSONB,
    context JSONB,
    provenance JSONB,
    status VARCHAR NOT NULL
);
```

---

# Integridad referencial

La base relacional deberá validar:

- identificadores existentes;
- tipos;
- dominio;
- rango;
- módulos;
- versiones;
- estados;
- referencias inversas.

---

# JSONB

JSONB podrá utilizarse para:

- contexto;
- procedencia;
- atributos variables;
- metadatos;
- reglas;
- restricciones.

No deberá reemplazar estructuras normalizadas cuando se requieran:

- consultas frecuentes;
- integridad fuerte;
- relaciones reutilizables.

---

# Almacenamiento documental

Una base documental podrá utilizarse para:

- artefactos JSON;
- snapshots;
- versiones;
- exportaciones;
- documentos derivados.

No deberá convertirse automáticamente en fuente semántica canónica.

---

# Arquitectura híbrida

El SGCC podrá adoptar una arquitectura híbrida.

Ejemplo:

```text
Markdown/YAML

↓

Repositorio Git
```

```text
PostgreSQL

↓

Gestión transaccional
```

```text
Knowledge Graph

↓

Navegación e inferencia
```

```text
Vector Store

↓

Recuperación semántica
```

---

# Separación de responsabilidades

Cada tecnología deberá utilizarse para aquello que mejor resuelve.

Ejemplo:

```text
Git
```

para:

- historial;
- revisión;
- versionado documental.

```text
PostgreSQL
```

para:

- integridad;
- transacciones;
- gestión operativa.

```text
Knowledge Graph
```

para:

- relaciones;
- rutas;
- inferencia.

```text
Vector Store
```

para:

- similitud semántica;
- recuperación aproximada.

---

# APIs REST

La ontología deberá poder exponerse mediante APIs REST.

Recursos principales:

```text
/classes

/properties

/axioms

/modules

/individuals

/assertions

/shapes

/rules
```

---

# Ejemplo de recurso de clase

```http
GET /api/ontology/classes/ONT-CLS-INGREDIENTE
```

Respuesta:

```json
{
  "id": "ONT-CLS-INGREDIENTE",
  "name": "Ingrediente",
  "definition": "Entidad material utilizada en una elaboración culinaria.",
  "module": "ONT-MOD-INGREDIENTES",
  "status": "stable",
  "version": "1.0.0"
}
```

---

# API de relaciones

Ejemplo:

```http
GET /api/knowledge/REC-0001/relations
```

Podrá devolver:

```json
{
  "subject": "REC-0001",
  "relations": [
    {
      "predicate": "utiliza",
      "object": "ING-0005"
    }
  ]
}
```

---

# API de inferencias

Ejemplo:

```http
GET /api/knowledge/REC-0001/inferences
```

La respuesta deberá diferenciar:

- hechos declarados;
- inferencias;
- reglas;
- confianza;
- explicación.

---

# API de explicación

Ejemplo:

```http
GET /api/inferences/INF-0042/explanation
```

Respuesta conceptual:

```json
{
  "conclusion": "REC-0001 contiene gluten",
  "premises": [
    "REC-0001 utiliza ING-0020",
    "ING-0020 contiene gluten"
  ],
  "rule": "REG-INF-0007"
}
```

---

# Versionado de API

Las APIs deberán versionarse.

Ejemplo:

```text
/api/v1/ontology
```

Los cambios incompatibles requerirán nueva versión.

---

# HATEOAS y enlaces semánticos

Las respuestas podrán incluir enlaces a:

- clase;
- módulo;
- propiedades;
- inversas;
- fuentes;
- representaciones alternativas.

---

# GraphQL

GraphQL podrá utilizarse cuando se requiera:

- consulta flexible;
- navegación de grafos;
- selección de campos;
- composición de entidades.

---

# Ejemplo GraphQL

```graphql
query {
  recipe(id: "REC-0001") {
    name
    ingredients {
      id
      name
    }
  }
}
```

---

# Esquema GraphQL derivado

El esquema GraphQL podrá derivarse parcialmente de:

- clases;
- propiedades;
- cardinalidades;
- dominio;
- rango.

---

# Limitaciones de GraphQL

GraphQL no representa automáticamente:

- axiomas;
- semántica formal;
- inferencia;
- mundo abierto;
- equivalencias.

Será una interfaz de consulta, no la ontología.

---

# Consultas semánticas

Las APIs deberán permitir consultas por:

- clase;
- propiedad;
- jerarquía;
- relación;
- contexto;
- procedencia;
- inferencia;
- versión.

---

# Exportación

El SGCC deberá soportar exportaciones en varios formatos.

Como mínimo:

- YAML;
- JSON;
- JSON-LD;
- Turtle.

Opcionalmente:

- RDF/XML;
- N-Triples;
- N-Quads;
- CSV;
- GraphML.

---

# Exportación completa

Una exportación completa deberá incluir:

- módulos;
- clases;
- propiedades;
- axiomas;
- restricciones;
- reglas;
- contextos;
- procedencia;
- versiones.

---

# Exportación parcial

Podrá filtrarse por:

- módulo;
- clase;
- versión;
- estado;
- fecha;
- dependencia;
- perfil.

---

# Manifiesto de exportación

Toda exportación deberá incluir un manifiesto.

Ejemplo:

```yaml
exportacion:
  id: EXP-0001
  ontologia: SGCC
  version: 1.0.0
  fecha: 2026-07-31
  formato: turtle
  perfil: owl-rl
  modulos:
    - core
    - ingredientes
    - recetas
```

---

# Importación

Toda importación deberá validar:

- formato;
- versión;
- identificadores;
- espacios de nombres;
- referencias;
- compatibilidad;
- licencia;
- procedencia.

---

# Importación de vocabularios externos

La importación no deberá copiar automáticamente todo el vocabulario externo.

Deberá seleccionar únicamente los conceptos necesarios.

---

# Mapeos de importación

Cada mapeo deberá indicar:

```text
Elemento externo

Elemento SGCC

Tipo de equivalencia

Confianza

Fuente

Versión
```

---

# Ejemplo de mapeo

```yaml
mapeo:
  externo: schema:Recipe
  interno: ONT-CLS-RECETA
  tipo: aproximado
  confianza: 0.85
```

---

# Correspondencia exacta

Una correspondencia exacta deberá utilizarse solo cuando ambos elementos sean semánticamente equivalentes.

---

# Correspondencia aproximada

Se utilizará cuando exista solapamiento, pero no identidad completa.

---

# Correspondencia jerárquica

Podrá indicarse:

```text
más amplio

más específico
```

---

# Alineación con Schema.org

Schema.org podrá utilizarse para:

- publicación web;
- SEO;
- interoperabilidad básica;
- recetas;
- ingredientes;
- instrucciones;
- valores nutricionales.

No deberá sustituir el modelo ontológico completo.

---

# Alineación con Dublin Core

Dublin Core podrá utilizarse para:

- título;
- creador;
- fecha;
- fuente;
- derechos;
- idioma;
- descripción.

---

# Alineación con PROV-O

PROV-O podrá utilizarse para:

- procedencia;
- agentes;
- actividades;
- entidades;
- derivación;
- generación;
- atribución.

---

# Alineación con SKOS

SKOS podrá utilizarse para:

- taxonomías;
- conceptos;
- etiquetas;
- notas;
- correspondencias.

---

# Alineación con QUDT u ontologías de unidades

Podrán reutilizarse vocabularios externos para:

- magnitudes;
- unidades;
- conversiones;
- cantidades.

La selección deberá documentarse.

---

# Alineación con ontologías temporales

Podrá utilizarse OWL-Time para:

- instantes;
- intervalos;
- duración;
- relaciones temporales.

---

# Alineación con GeoNames u otros vocabularios geográficos

Podrán utilizarse para:

- países;
- regiones;
- ciudades;
- lugares de origen;
- tradiciones culinarias.

---

# Interoperabilidad sintáctica

Existe interoperabilidad sintáctica cuando dos sistemas comparten formato.

Ejemplo:

```text
JSON
```

Esto no garantiza que comprendan el mismo significado.

---

# Interoperabilidad semántica

Existe interoperabilidad semántica cuando ambos sistemas interpretan los datos de forma equivalente.

Requiere:

- vocabulario compartido;
- identificadores;
- mapeos;
- definiciones;
- axiomas;
- contexto.

---

# Interoperabilidad organizativa

También deberán considerarse:

- responsabilidades;
- procesos;
- versionado;
- licencias;
- gobernanza.

---

# Interoperabilidad progresiva

El SGCC podrá establecer niveles:

```text
Nivel 1 — Sintaxis común

Nivel 2 — Identificadores comunes

Nivel 3 — Vocabulario común

Nivel 4 — Axiomas compatibles

Nivel 5 — Inferencia interoperable
```

---

# Sincronización entre representaciones

Cuando existan múltiples representaciones deberá definirse:

- fuente;
- destino;
- dirección;
- frecuencia;
- reglas;
- conflictos;
- validación.

---

# Sincronización unidireccional

Ejemplo:

```text
YAML canónico

↓

Genera Turtle
```

La representación generada no deberá editarse manualmente.

---

# Sincronización bidireccional

Solo deberá utilizarse cuando exista:

- resolución de conflictos;
- identidad estable;
- historial;
- validación;
- reconciliación.

---

# Flujo recomendado

```text
Markdown normativo

+

YAML estructurado

↓

Validación

↓

Generación RDF/OWL

↓

Carga en Knowledge Graph

↓

Generación de índices RAG
```

---

# Generación automática

Podrán generarse automáticamente:

- Turtle;
- JSON-LD;
- documentación;
- diagramas;
- esquemas;
- APIs;
- shapes SHACL;
- índices.

---

# Derivación

Todo artefacto generado deberá registrar:

- fuente;
- versión;
- herramienta;
- fecha;
- hash;
- perfil.

---

# Hash e integridad

Los artefactos podrán incluir hash para verificar:

- integridad;
- reproducibilidad;
- correspondencia entre formatos.

---

# Detección de divergencias

El sistema deberá detectar:

- clases faltantes;
- propiedades divergentes;
- versiones incompatibles;
- cambios manuales;
- inferencias desactualizadas;
- mappings rotos.

---

# Resolución de conflictos

Cuando dos representaciones difieran deberá prevalecer la fuente canónica.

Los cambios válidos deberán incorporarse primero en ella.

---

# Canonicalización

La canonicalización deberá normalizar:

- identificadores;
- nombres;
- orden;
- espacios de nombres;
- fechas;
- tipos;
- unidades;
- idiomas.

---

# Serialización determinista

Cuando sea posible, la misma ontología deberá producir la misma serialización.

Esto facilitará:

- comparación;
- versionado;
- hashes;
- pruebas;
- auditoría.

---

# Round-trip

Una conversión será reversible cuando:

```text
A → B → A
```

preserve:

- identidad;
- estructura;
- semántica;
- contexto;
- procedencia.

---

# Pérdida semántica

Toda conversión deberá declarar si pierde:

- axiomas;
- cardinalidades;
- contexto;
- anotaciones;
- procedencia;
- inferencias.

---

# Matriz de capacidad

| Representación | Clases | Relaciones | Axiomas | Inferencia | Contexto | Procedencia |
|---|---:|---:|---:|---:|---:|---:|
| Markdown | Parcial | Parcial | Descriptiva | No | Descriptivo | Sí |
| YAML | Sí | Sí | Parcial | No | Sí | Sí |
| JSON | Sí | Sí | Parcial | No | Sí | Sí |
| JSON-LD | Sí | Sí | Parcial | Externa | Sí | Sí |
| RDF | Sí | Sí | Parcial | Sí | Sí | Sí |
| OWL | Sí | Sí | Sí | Sí | Limitado | Parcial |
| SHACL | Sí | Sí | Restricciones | Validación | Sí | Sí |
| PostgreSQL | Sí | Sí | Parcial | Aplicación | Sí | Sí |
| Grafo de propiedades | Sí | Sí | Parcial | Motor propio | Sí | Sí |

---

# Representación de inferencias

Las inferencias deberán almacenarse separadas o claramente identificadas.

Ejemplo:

```yaml
afirmacion:
  sujeto: REC-0001
  predicado: contiene_alergeno
  objeto: gluten
  origen: inferida
  regla: REG-INF-0007
```

---

# Datos declarados e inferidos

No deberán mezclarse sin distinción.

Podrán utilizarse:

- grafos separados;
- tablas separadas;
- atributo de origen;
- namespaces distintos.

---

# Representación de incertidumbre

Una afirmación probabilística deberá incluir:

- confianza;
- método;
- modelo;
- versión;
- fecha;
- estado de validación.

---

# Representación de negación

La negación explícita deberá diferenciarse de la ausencia.

Ejemplo:

```yaml
polaridad: negativa
```

o mediante un predicado negativo controlado.

---

# Representación de contexto

El contexto podrá representarse como:

- objeto estructurado;
- entidad;
- grafo nombrado;
- nodo asociativo;
- propiedades de arista.

---

# Contexto simple

```yaml
contexto:
  fase: acabado
  dieta: vegetariana
```

---

# Contexto complejo

```yaml
contexto_id: CTX-0005
```

con entidad propia:

```yaml
id: CTX-0005
tipo: contexto
receta: REC-0001
fase: coccion
temperatura: alta
region: ES-MD
```

---

# Representación temporal

Toda afirmación temporal podrá incluir:

```text
válida_desde

válida_hasta

registrada_en

invalidada_en
```

---

# Representación de versiones

La identidad conceptual y la versión deberán separarse.

Ejemplo:

```text
ONT-CLS-INGREDIENTE

↓

versión 1.0.0
```

No deberá crearse un nuevo identificador para una simple actualización compatible.

---

# Versiones en URI

Podrán utilizarse URI versionadas para artefactos.

Ejemplo:

```text
/ontology/1.0.0/
```

Las URI de identidad conceptual deberán permanecer estables.

---

# Desreferenciación

Las URI deberían poder resolverse a:

- HTML para personas;
- Turtle para sistemas;
- JSON-LD para APIs.

---

# Negociación de contenido

Podrá utilizarse `Accept` para seleccionar formato.

Ejemplo:

```text
text/html

text/turtle

application/ld+json
```

---

# Catálogo de distribuciones

Cada versión podrá publicar distribuciones en varios formatos.

Ejemplo:

```text
Ontología SGCC 1.0.0

├── Turtle
├── JSON-LD
├── RDF/XML
├── YAML
└── Documentación HTML
```

---

# Paquete ontológico

Una distribución completa podrá contener:

```text
manifest.yaml

ontology.ttl

ontology.jsonld

shapes.ttl

rules.yaml

mappings.yaml

CHANGELOG.md

LICENSE
```

---

# Metadatos del paquete

El manifiesto deberá incluir:

- nombre;
- versión;
- fecha;
- estado;
- módulos;
- perfiles;
- dependencias;
- licencia;
- hashes;
- compatibilidad.

---

# Interoperabilidad con RAG

La ontología deberá enriquecer la recuperación mediante:

- expansión de conceptos;
- sinónimos;
- jerarquías;
- relaciones;
- contexto;
- filtros;
- clasificación.

---

# Recuperación semántica

Ejemplo:

Consulta:

```text
verduras crucíferas
```

La ontología podrá recuperar:

- brócoli;
- coliflor;
- col;
- coles de Bruselas.

---

# Expansión ontológica de consultas

Una consulta podrá expandirse mediante:

- subclases;
- superclases;
- alias;
- relaciones cercanas;
- equivalencias;
- términos relacionados.

---

# Restricción de expansión

La expansión deberá controlarse para evitar:

- ruido;
- pérdida de precisión;
- inferencias inseguras;
- expansión excesiva.

---

# Fragmentos RAG

Los fragmentos deberán incluir metadatos como:

```text
conceptos

clases

relaciones

fuentes

versión

contexto

confianza
```

---

# Identificadores en embeddings

Los vectores deberán conservar referencia a identificadores canónicos.

Un embedding no deberá convertirse en identidad semántica.

---

# Vector Store

El vector store servirá para similitud.

No será fuente de verdad.

La fuente de verdad seguirá siendo:

- ontología;
- Knowledge Graph;
- documentos canónicos.

---

# Búsqueda híbrida

El SGCC podrá combinar:

```text
Búsqueda léxica

+

Búsqueda vectorial

+

Consulta de grafo

+

Filtros ontológicos
```

---

# Recuperación explicable

El sistema deberá poder explicar:

- por qué se recuperó un elemento;
- qué relación lo conecta;
- qué clase comparte;
- qué fuente lo respalda.

---

# Interoperabilidad con agentes IA

Los agentes deberán recibir representaciones estructuradas.

Ejemplo:

```json
{
  "entity": "REC-0001",
  "type": "Receta",
  "facts": [],
  "inferences": [],
  "constraints": [],
  "provenance": []
}
```

---

# Contexto para agentes

Los agentes deberán distinguir:

- hechos;
- reglas;
- restricciones;
- hipótesis;
- predicciones;
- permisos.

---

# Herramientas ontológicas para agentes

Podrán exponerse operaciones como:

```text
get_class

get_entity

get_relations

get_constraints

validate_entity

explain_inference

search_concepts
```

---

# MCP

El Model Context Protocol podrá utilizarse como capa de acceso a:

- ontología;
- Knowledge Graph;
- validadores;
- búsquedas;
- explicaciones;
- transformaciones.

---

# Recursos MCP

Podrán exponerse recursos como:

```text
ontology://classes/Ingrediente

ontology://modules/Recetas

knowledge://entities/REC-0001

rules://REG-INF-0007
```

---

# Herramientas MCP

Podrán existir herramientas como:

```text
query_ontology

validate_assertion

resolve_alias

find_substitutions

explain_relation

get_provenance
```

---

# Respuestas de agentes

Toda respuesta basada en la ontología debería poder incluir:

- identificadores;
- clases;
- relaciones;
- fuentes;
- inferencias;
- confianza;
- restricciones.

---

# Prevención de alucinaciones

Los agentes no deberán inventar:

- clases;
- predicados;
- axiomas;
- identificadores;
- equivalencias.

Cuando necesiten un concepto inexistente deberán formular una propuesta explícita.

---

# Representación de permisos

El acceso a elementos ontológicos podrá depender de:

- rol;
- módulo;
- estado;
- sensibilidad;
- procedencia;
- licencia.

---

# Vistas ontológicas

Podrán generarse vistas para:

- usuarios;
- editores;
- desarrolladores;
- agentes;
- sistemas externos.

---

# Perfil público

Podrá incluir:

- conceptos estables;
- definiciones;
- relaciones públicas;
- URI;
- licencias.

---

# Perfil interno

Podrá incluir:

- borradores;
- reglas experimentales;
- conflictos;
- predicciones;
- fuentes privadas.

---

# Perfil de seguridad

Deberá restringir:

- afirmaciones no verificadas;
- datos sensibles;
- reglas experimentales;
- inferencias de alto impacto.

---

# Auditoría de representaciones

Toda transformación deberá registrar:

- origen;
- destino;
- herramienta;
- versión;
- fecha;
- resultado;
- errores;
- advertencias.

---

# Validación de representación

Cada formato deberá validarse antes de publicación.

---

## Validación Markdown

Deberá comprobar:

- secciones obligatorias;
- identificadores;
- enlaces;
- referencias;
- tablas;
- bloques de código.

---

## Validación YAML

Deberá comprobar:

- sintaxis;
- claves;
- tipos;
- identificadores;
- referencias;
- esquema.

---

## Validación JSON

Deberá comprobar:

- JSON válido;
- JSON Schema;
- codificación;
- referencias;
- formatos.

---

## Validación RDF

Deberá comprobar:

- sintaxis;
- URI;
- namespaces;
- triples;
- tipos;
- referencias.

---

## Validación OWL

Deberá comprobar:

- consistencia;
- satisfacibilidad;
- perfil;
- inferencias;
- axiomas conflictivos.

---

## Validación SHACL

Deberá comprobar:

- shapes;
- targets;
- rutas;
- cardinalidades;
- severidad;
- resultados.

---

# Pruebas de interoperabilidad

Deberán incluir:

- conversión YAML a RDF;
- conversión RDF a JSON-LD;
- carga en grafo;
- consulta;
- validación;
- round-trip;
- comparación semántica.

---

# Golden files

Podrán mantenerse archivos de referencia para comprobar que las transformaciones no cambian inesperadamente.

---

# Pruebas de consultas

Deberán probarse:

- consultas SPARQL;
- Cypher;
- SQL;
- REST;
- GraphQL;
- RAG.

---

# Pruebas de inferencia

Deberán verificar que diferentes representaciones produzcan las mismas conclusiones relevantes.

---

# Compatibilidad entre motores

Cuando se utilicen distintos razonadores deberá comprobarse:

- perfil soportado;
- resultados;
- rendimiento;
- explicaciones;
- diferencias.

---

# Rendimiento

La representación deberá considerar:

- volumen;
- latencia;
- complejidad;
- frecuencia de actualización;
- consultas;
- inferencia.

---

# Estrategias de optimización

Podrán utilizarse:

- índices;
- materialización;
- caché;
- partición;
- grafos por módulo;
- vistas;
- desnormalización controlada.

---

# Materialización selectiva

No todas las inferencias deberán almacenarse.

Podrán materializarse aquellas que:

- sean frecuentes;
- sean costosas;
- sean estables;
- mejoren consultas;
- tengan explicación conservada.

---

# Caché semántica

Las respuestas podrán cachearse por:

- versión ontológica;
- consulta;
- contexto;
- perfil;
- permisos.

---

# Invalidación de caché

La caché deberá invalidarse cuando cambien:

- axiomas;
- relaciones;
- versiones;
- fuentes;
- permisos;
- contexto.

---

# Portabilidad

La ontología deberá poder migrar entre tecnologías sin perder:

- identidad;
- semántica;
- procedencia;
- versiones;
- contexto.

---

# Dependencia mínima

Las representaciones canónicas deberán evitar depender de extensiones propietarias cuando existan alternativas abiertas.

---

# Formatos abiertos

Se priorizarán:

- Markdown;
- YAML;
- JSON;
- JSON-LD;
- RDF;
- Turtle;
- OWL;
- SHACL;
- SPARQL.

---

# Extensiones propietarias

Podrán utilizarse cuando aporten valor, pero deberán documentarse:

- dependencia;
- impacto;
- estrategia de salida;
- formato de exportación.

---

# Estrategia de salida

Toda tecnología de persistencia deberá permitir exportar el conocimiento a un formato abierto.

---

# Perfil mínimo de representación

La implementación mínima deberá soportar:

- Markdown;
- YAML;
- identificadores;
- clases;
- propiedades;
- relaciones;
- versiones;
- validación estructural.

---

# Perfil recomendado

El perfil recomendado deberá añadir:

- JSON;
- JSON-LD;
- Turtle;
- RDF;
- SHACL;
- APIs;
- Knowledge Graph;
- procedencia;
- contexto.

---

# Perfil avanzado

El perfil avanzado deberá añadir:

- OWL;
- razonamiento;
- grafos nombrados;
- RDF-star;
- SPARQL;
- MCP;
- sincronización automática;
- búsqueda híbrida;
- explicabilidad completa.

---

# Arquitectura de referencia

```text
Repositorio Git
    │
    ├── Markdown normativo
    ├── YAML estructurado
    └── esquemas
            │
            ▼
      Pipeline semántico
            │
    ┌───────┼────────┐
    ▼       ▼        ▼
  RDF     JSON-LD   SHACL
    │       │        │
    └───────┼────────┘
            ▼
     Knowledge Graph
            │
    ┌───────┼────────────┐
    ▼       ▼            ▼
  APIs    RAG          Agentes
```

---

# Pipeline semántico

El pipeline deberá poder ejecutar:

```text
Lint

↓

Validación estructural

↓

Validación de referencias

↓

Generación RDF

↓

Validación SHACL

↓

Razonamiento

↓

Pruebas de consistencia

↓

Publicación
```

---

# Fallo de pipeline

La publicación deberá bloquearse ante:

- sintaxis inválida;
- identificadores duplicados;
- referencias rotas;
- inconsistencia;
- shapes fallidos críticos;
- incompatibilidad no declarada;
- pérdida semántica no aceptada.

---

# Advertencias de pipeline

Podrán generar advertencias:

- conceptos sin traducción;
- axiomas sin ejemplos;
- mapeos aproximados;
- clases sin instancias;
- propiedades no utilizadas;
- exportaciones no deterministas.

---

# Documentación generada

El pipeline podrá producir:

- catálogos;
- diagramas;
- tablas;
- documentación HTML;
- índices;
- referencias cruzadas;
- informes de calidad.

---

# Diagramas

Podrán generarse representaciones como:

- Mermaid;
- PlantUML;
- Graphviz;
- diagramas de clases;
- grafos navegables.

---

# Diagramas como vistas

Los diagramas no serán fuente de verdad.

Serán vistas derivadas de la ontología.

---

# Gestión de idiomas

Las representaciones deberán permitir etiquetas multilingües.

Ejemplo:

```turtle
sgcc:Ingrediente
    rdfs:label "Ingrediente"@es ;
    rdfs:label "Ingredient"@en ;
    rdfs:label "Ingrédient"@fr .
```

---

# Idioma canónico

El español podrá mantenerse como idioma principal de documentación.

Los identificadores deberán permanecer independientes del idioma cuando sea posible.

---

# Traducciones incompletas

La ausencia de traducción no deberá alterar la semántica.

---

# Codificación

Todos los formatos deberán utilizar UTF-8.

---

# Licencias

Las distribuciones deberán incluir:

- licencia;
- procedencia;
- restricciones de uso;
- licencias de vocabularios externos.

---

# Publicación

La ontología podrá publicarse mediante:

- repositorio;
- sitio web;
- endpoint RDF;
- API;
- catálogo;
- paquete versionado.

---

# Versiones publicadas

Cada publicación deberá ser:

- inmutable;
- identificable;
- descargable;
- verificable;
- documentada.

---

# Versión latest

Podrá existir una referencia:

```text
latest
```

pero no deberá sustituir versiones explícitas en integraciones reproducibles.

---

# Deprecación en representaciones

Los elementos obsoletos deberán seguir siendo resolubles.

Deberán indicar:

- estado;
- sustituto;
- versión;
- fecha;
- migración.

---

# Resolución de alias

Las APIs y herramientas podrán aceptar alias, pero deberán devolver el identificador canónico.

---

# Normalización de entrada

Toda entrada deberá normalizar:

- mayúsculas;
- minúsculas;
- tildes;
- espacios;
- guiones;
- alias;
- idioma.

La normalización no deberá fusionar conceptos distintos.

---

# Identidad entre formatos

El mismo elemento deberá conservar el mismo identificador en:

- Markdown;
- YAML;
- JSON;
- RDF;
- base de datos;
- API;
- Knowledge Graph.

---

# Trazabilidad cruzada

Todo elemento debería poder enlazar a:

- definición normativa;
- representación estructurada;
- URI semántica;
- instancia persistida;
- historial;
- pruebas.

---

# Matriz de trazabilidad

| Elemento | Markdown | YAML | RDF | DB | API |
|---|---|---|---|---|---|
| Clase | Sí | Sí | URI | Registro | Recurso |
| Propiedad | Sí | Sí | URI | Registro | Recurso |
| Axioma | Sí | Sí | Triple | Registro | Recurso |
| Restricción | Sí | Sí | SHACL | Registro | Recurso |
| Individuo | Opcional | Sí | URI | Registro | Recurso |

---

# Antipatrones de representación

Deberán evitarse:

- usar nombres como identificadores;
- duplicar entidades por formato;
- editar artefactos generados;
- mezclar hechos e inferencias;
- representar cantidades como texto;
- omitir contexto;
- perder procedencia;
- utilizar `sameAs` como simple parecido;
- asumir que JSON implica semántica;
- mantener varios orígenes canónicos.

---

# Antipatrón de silos

No deberán existir modelos independientes para:

- documentación;
- base de datos;
- API;
- grafo;
- IA.

Todos deberán derivar del mismo modelo semántico.

---

# Antipatrón de sincronización manual

La sincronización manual entre formatos deberá minimizarse.

Será preferible:

```text
Una fuente

↓

Múltiples artefactos generados
```

---

# Antipatrón de sobreformalización

No todo concepto deberá expresarse inmediatamente mediante OWL avanzado.

La formalización deberá crecer según:

- valor;
- necesidad;
- capacidad de validación;
- madurez.

---

# Criterios de selección tecnológica

La selección deberá considerar:

- semántica requerida;
- volumen;
- rendimiento;
- mantenimiento;
- interoperabilidad;
- experiencia del equipo;
- portabilidad;
- coste.

---

# Perfil inicial recomendado para NovaCoquinaria

La primera fase podrá utilizar:

```text
Markdown
```

como especificación normativa,

```text
YAML
```

como representación estructurada canónica,

```text
JSON
```

para APIs,

```text
Turtle
```

como representación semántica,

```text
SHACL
```

para validación,

y:

```text
PostgreSQL o grafo de propiedades
```

para operación.

---

# Evolución recomendada

```text
Fase 1
Markdown + YAML
```

```text
Fase 2
JSON Schema + generación automática
```

```text
Fase 3
RDF + Turtle + SHACL
```

```text
Fase 4
Knowledge Graph + SPARQL
```

```text
Fase 5
OWL + inferencia avanzada + MCP
```

---

# Conformidad de representación

Una representación será conforme cuando:

- preserve identificadores;
- mantenga significado;
- represente tipos correctamente;
- conserve contexto;
- conserve procedencia;
- indique versión;
- sea validable;
- declare limitaciones.

---

# Conformidad de conversión

Una conversión será conforme cuando:

- sea reproducible;
- esté documentada;
- preserve semántica;
- registre pérdidas;
- mantenga trazabilidad;
- supere pruebas.

---

# Conformidad de API

Una API será conforme cuando:

- utilice identificadores canónicos;
- distinga hechos e inferencias;
- incluya versiones;
- preserve contexto;
- exponga procedencia;
- respete restricciones;
- documente formatos.

---

# Conformidad de Knowledge Graph

Un Knowledge Graph será conforme cuando:

- instancie la ontología;
- mantenga clases y propiedades;
- preserve procedencia;
- diferencie inferencias;
- respete restricciones;
- sea consultable;
- pueda exportarse.

---

# Conformidad de integración RAG

Una integración RAG será conforme cuando:

- utilice identificadores;
- conserve fuentes;
- distinga contenido e inferencias;
- aplique filtros ontológicos;
- permita explicación;
- no utilice embeddings como fuente de verdad.

---

# Conformidad de agente IA

Un agente será conforme cuando:

- consulte el vocabulario controlado;
- utilice relaciones canónicas;
- distinga certeza;
- preserve procedencia;
- explique inferencias;
- respete permisos;
- no invente elementos ontológicos.

---

# Transición hacia la gobernanza ontológica

La presente parte ha definido:

- representaciones humanas;
- YAML;
- JSON;
- JSON-LD;
- RDF;
- RDFS;
- OWL;
- Turtle;
- SKOS;
- SHACL;
- grafos RDF;
- grafos de propiedades;
- PostgreSQL;
- APIs;
- GraphQL;
- importación;
- exportación;
- sincronización;
- RAG;
- MCP;
- agentes inteligentes;
- perfiles de representación;
- validación;
- conformidad.

La siguiente parte establecerá cómo gobernar la ontología a lo largo del tiempo.

Dicha gobernanza deberá regular:

- creación de clases;
- creación de propiedades;
- incorporación de axiomas;
- modificación;
- versionado;
- deprecación;
- migración;
- alineación externa;
- validación;
- aprobación;
- publicación;
- roles;
- auditoría;
- métricas de calidad;
- deuda ontológica.

Con ello se completará la especificación formal de la ontología del SGCC.

---

# Gobernanza y evolución de la ontología

La presente sección define el marco de gobierno que regula el ciclo de vida completo de la ontología del Sistema de Gestión del Conocimiento Culinario (SGCC).

Las partes anteriores han definido:

- los fundamentos conceptuales;
- el metamodelo;
- la semántica formal;
- la representación e interoperabilidad.

Esta parte establece cómo debe evolucionar la ontología sin comprometer:

- su coherencia;
- su estabilidad;
- su trazabilidad;
- su interoperabilidad;
- la compatibilidad con el resto del SGCC.

La gobernanza constituye el mecanismo mediante el cual la ontología evoluciona de forma controlada y sostenible.

---

# Objetivo

Los objetivos de la gobernanza ontológica son:

- preservar el significado de los conceptos;
- controlar la evolución del vocabulario;
- garantizar la calidad semántica;
- evitar duplicidades;
- asegurar la compatibilidad entre versiones;
- mantener la trazabilidad histórica;
- facilitar la colaboración;
- permitir auditorías;
- proteger la estabilidad del Knowledge Graph;
- garantizar la reproducibilidad de las inferencias.

---

# Alcance

La gobernanza regula:

- módulos ontológicos;
- clases;
- propiedades;
- axiomas;
- restricciones;
- reglas;
- taxonomías;
- alineaciones externas;
- perfiles;
- espacios de nombres;
- identificadores;
- representaciones;
- documentación;
- validaciones;
- publicaciones.

No regula:

- la gobernanza documental general del SGCC;
- la gestión del código fuente;
- la infraestructura técnica;
- la administración operativa de aplicaciones.

---

# Principios de gobernanza

Toda evolución deberá respetar los siguientes principios.

---

## Estabilidad conceptual

El significado de un concepto estable no deberá modificarse de forma implícita.

Si cambia su significado, deberá evaluarse la creación de un nuevo concepto.

---

## Identidad persistente

Los identificadores canónicos deberán permanecer estables durante toda la vida del concepto.

Nunca deberán reutilizarse para representar entidades distintas.

---

## Evolución incremental

La ontología deberá evolucionar mediante cambios pequeños, verificables y documentados.

---

## Compatibilidad

Siempre que sea posible, las nuevas versiones deberán mantener compatibilidad con las anteriores.

---

## Trazabilidad

Todo cambio deberá responder a las preguntas:

- ¿qué cambió?
- ¿por qué cambió?
- ¿quién lo aprobó?
- ¿cuándo ocurrió?
- ¿qué impacto tiene?

---

## Transparencia

Las decisiones semánticas deberán estar documentadas y justificadas.

---

## Revisión por pares

Las modificaciones relevantes deberán ser revisadas antes de incorporarse al modelo estable.

---

# Ciclo de vida de un elemento ontológico

Todo elemento seguirá un ciclo similar al siguiente:

```text
Propuesto
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
Obsoleto
      │
      ▼
Archivado
```

---

# Estados

## Propuesto

Existe una propuesta inicial.

No podrá utilizarse en producción.

---

## Borrador

El concepto está siendo desarrollado.

Puede cambiar libremente.

---

## En revisión

Se encuentra pendiente de validación técnica y semántica.

---

## Estable

Forma parte oficialmente de la ontología.

---

## Obsoleto

Continúa existiendo por compatibilidad.

No deberá utilizarse en nuevos desarrollos.

---

## Archivado

Se conserva únicamente por razones históricas.

---

# Registro ontológico

Todos los elementos deberán formar parte de un registro único.

Cada registro incluirá al menos:

- identificador;
- nombre;
- versión;
- módulo;
- estado;
- fecha de creación;
- autor;
- responsable;
- última revisión;
- historial.

---

# Propuesta de nuevos conceptos

Toda propuesta deberá responder como mínimo:

- ¿qué problema resuelve?
- ¿por qué no puede reutilizarse un concepto existente?
- ¿qué relaciones tendrá?
- ¿qué impacto produce?
- ¿qué reglas o axiomas requiere?
- ¿cómo afectará al Knowledge Graph?
- ¿qué documentación deberá actualizarse?

---

# Criterios de aceptación

Un nuevo concepto deberá:

- aportar nueva semántica;
- ser reutilizable;
- evitar duplicidades;
- disponer de definición normativa;
- pertenecer a un módulo;
- tener identificador;
- incluir ejemplos;
- superar validaciones.

---

# Revisión semántica

La revisión deberá comprobar:

- definición;
- coherencia;
- jerarquía;
- relaciones;
- restricciones;
- posibles redundancias;
- alineaciones externas.

---

# Revisión técnica

Deberá comprobar:

- identificadores;
- referencias;
- esquemas;
- validaciones;
- generación de artefactos;
- impacto en herramientas.

---

# Revisión arquitectónica

Las modificaciones relevantes deberán valorar:

- impacto sobre la arquitectura;
- compatibilidad;
- rendimiento;
- interoperabilidad;
- deuda técnica;
- deuda ontológica.

---

# Versionado

La ontología utilizará versionado semántico.

```text
MAJOR.MINOR.PATCH
```

---

## Cambios PATCH

Ejemplos:

- corrección tipográfica;
- aclaración documental;
- mejora de ejemplos;
- metadatos.

No modifican el significado.

---

## Cambios MINOR

Ejemplos:

- nuevas clases;
- nuevas propiedades;
- nuevos módulos;
- nuevas anotaciones;
- ampliaciones compatibles.

---

## Cambios MAJOR

Ejemplos:

- eliminación de conceptos;
- cambio de significado;
- modificación incompatible;
- cambios en axiomas fundamentales;
- reorganización de jerarquías.

---

# Versionado individual

Cada elemento podrá tener versión propia.

Ejemplo:

```text
ONT-CLS-INGREDIENTE

versión 1.2.0
```

independientemente de la versión global de la ontología.

---

# Historial

El historial deberá conservar:

- versión;
- fecha;
- autor;
- descripción;
- justificación;
- migración asociada.

---

# Cambios compatibles

Se consideran compatibles, entre otros:

- añadir ejemplos;
- añadir traducciones;
- añadir anotaciones;
- ampliar documentación;
- añadir subclases;
- añadir nuevas propiedades opcionales.

---

# Cambios incompatibles

Ejemplos:

- cambiar dominio;
- cambiar rango;
- modificar significado;
- eliminar propiedades;
- invertir jerarquías;
- redefinir axiomas.

Estos cambios requerirán nueva versión mayor o migración explícita.

---

# Deprecación

Un elemento obsoleto deberá:

- mantenerse accesible;
- indicar sustituto;
- documentar motivo;
- definir periodo de transición.

---

# Sustituciones

Todo elemento obsoleto deberá indicar, cuando exista:

```text
reemplazado_por
```

---

# Eliminación

La eliminación física será excepcional.

Solo podrá realizarse cuando:

- no existan referencias;
- no afecte a versiones históricas;
- exista aprobación formal.

---

# Migraciones

Toda modificación incompatible deberá incluir un plan de migración.

Este plan describirá:

- origen;
- destino;
- transformación;
- validación;
- reversión.

---

# Compatibilidad histórica

Las versiones antiguas deberán poder reconstruirse cuando resulte necesario para auditoría o reproducibilidad.

---

# Gobernanza de módulos

Cada módulo deberá tener:

- responsable;
- alcance;
- dependencias;
- versión;
- hoja de ruta.

---

# Gobernanza de clases

Las clases deberán revisarse periódicamente para detectar:

- duplicidades;
- jerarquías innecesarias;
- conceptos huérfanos;
- clases sin uso.

---

# Gobernanza de propiedades

Las propiedades deberán revisarse para detectar:

- redundancias;
- dominios excesivamente amplios;
- rangos ambiguos;
- relaciones poco utilizadas.

---

# Gobernanza de axiomas

Los axiomas deberán evaluarse según:

- coherencia;
- impacto;
- inferencias generadas;
- rendimiento;
- explicabilidad.

---

# Gobernanza de reglas

Las reglas deberán documentar:

- finalidad;
- entradas;
- salidas;
- prioridad;
- excepciones;
- ejemplos;
- pruebas.

---

# Gobernanza de taxonomías

Las taxonomías deberán mantener:

- cohesión;
- profundidad razonable;
- ausencia de ciclos;
- significado estable.

---

# Gobernanza de alineaciones externas

Toda alineación deberá indicar:

- vocabulario externo;
- versión;
- tipo de correspondencia;
- confianza;
- responsable.

---

# Gestión de conflictos

Los conflictos semánticos deberán registrarse.

Cada conflicto incluirá:

- descripción;
- elementos afectados;
- impacto;
- propuesta de resolución;
- estado.

---

# Resolución de conflictos

La resolución priorizará:

1. seguridad alimentaria;
2. consistencia semántica;
3. reutilización;
4. compatibilidad;
5. simplicidad.

---

# Calidad ontológica

Se evaluarán indicadores como:

- coherencia;
- cobertura;
- reutilización;
- modularidad;
- conectividad;
- estabilidad;
- consistencia;
- trazabilidad.

---

# Métricas

Ejemplos:

- número de clases;
- profundidad media;
- propiedades reutilizadas;
- axiomas activos;
- inferencias;
- conceptos obsoletos;
- duplicidades;
- conceptos huérfanos;
- deuda ontológica.

---

# Deuda ontológica

Se considera deuda ontológica cualquier decisión que reduzca la calidad futura del modelo.

Ejemplos:

- duplicación de conceptos;
- nombres ambiguos;
- jerarquías incorrectas;
- relaciones genéricas abusivas;
- documentación incompleta.

---

# Refactorización

Las refactorizaciones deberán preservar el significado del modelo.

Toda refactorización deberá incluir:

- justificación;
- impacto;
- pruebas;
- migración.

---

# ADR

Toda decisión arquitectónicamente significativa deberá documentarse mediante un ADR.

Ejemplos:

- reorganización de módulos;
- incorporación de OWL;
- cambios de estrategia de inferencia;
- nuevas políticas de versionado.

---

# Roles

Podrán definirse al menos los siguientes roles:

- Arquitecto Ontológico;
- Revisor Semántico;
- Experto Culinario;
- Responsable de Calidad;
- Mantenedor del Módulo;
- Editor.

---

# Responsabilidades

Cada rol deberá tener responsabilidades claramente delimitadas.

Por ejemplo:

Arquitecto Ontológico:

- diseño global;
- coherencia;
- evolución.

Experto Culinario:

- validez del dominio.

Responsable de Calidad:

- validaciones;
- métricas;
- auditorías.

---

# Automatización

La gobernanza deberá apoyarse en automatizaciones para:

- validación;
- generación;
- comprobación de referencias;
- análisis de impacto;
- informes de calidad.

---

# Pipeline de gobernanza

Todo cambio importante debería seguir un flujo como:

```text
Propuesta
    ↓
Validación automática
    ↓
Revisión semántica
    ↓
Revisión técnica
    ↓
Aprobación
    ↓
Publicación
```

---

# Auditoría

Toda modificación deberá ser auditable.

La auditoría registrará:

- autor;
- fecha;
- cambio;
- motivo;
- versión;
- revisión.

---

# Publicación

Cada publicación deberá incluir:

- versión;
- CHANGELOG;
- artefactos generados;
- resultados de validación;
- documentación actualizada.

---

# Indicadores de madurez

La madurez ontológica podrá evaluarse mediante niveles:

```text
Nivel 1
Modelo inicial
```

```text
Nivel 2
Modelo estructurado
```

```text
Nivel 3
Modelo validado
```

```text
Nivel 4
Modelo interoperable
```

```text
Nivel 5
Modelo gobernado y evolutivo
```

---

# Conformidad

Una ontología será conforme cuando:

- respete esta especificación;
- supere las validaciones;
- mantenga coherencia;
- preserve trazabilidad;
- documente cambios;
- gestione correctamente su evolución.

---

# Conclusión

Con esta quinta parte se completa la **Especificación de Ontología** del SGCC.

El documento establece de forma integral:

- los fundamentos conceptuales del modelo;
- el metamodelo utilizado para describir el dominio;
- la semántica formal y las reglas de inferencia;
- las representaciones e interoperabilidad con estándares abiertos;
- y el marco de gobernanza necesario para garantizar una evolución controlada.

Esta ontología constituye la **fuente de verdad semántica** del Sistema de Gestión del Conocimiento Culinario y servirá como base para:

- el Knowledge Graph;
- los procesos de validación;
- los motores de inferencia;
- las APIs semánticas;
- los sistemas RAG;
- los agentes inteligentes;
- y cualquier futura ampliación del ecosistema NovaCoquinaria.

Con su finalización queda definido el núcleo conceptual del SGCC, sobre el que podrán construirse el resto de capacidades avanzadas del sistema.
