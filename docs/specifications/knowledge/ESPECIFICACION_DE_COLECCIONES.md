---
id: ARC-0018
tipo: arquitectura
titulo: Modelo de Colecciones de Conocimiento
version: 2.0
estado: estable
ultima_revision: 2026-07-20
---
# Modelo de Colecciones de Conocimiento

> Proyecto: NovaCoquinaria
>
> Sistema: GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Parte I — Fundamentos y modelo conceptual

---

# Introducción

Las Colecciones de Conocimiento constituyen uno de los mecanismos fundamentales del Sistema de Gestión del Conocimiento Culinario (SGCC).

Mientras que:

- los documentos representan conocimiento explícito;
- los componentes estructuran dicho conocimiento;
- las relaciones describen sus conexiones;
- la ontología define su significado;
- y el Knowledge Graph materializa dichas relaciones,

las colecciones permiten organizar, proyectar y gestionar dominios completos de conocimiento de forma transversal.

Una colección no crea conocimiento nuevo.

Tampoco modifica el conocimiento existente.

Su función consiste en definir una vista lógica, gobernada y reutilizable sobre el ecosistema completo del SGCC.

---

# Objetivo

Esta especificación tiene como objetivos:

- definir formalmente el concepto de colección;
- establecer su papel dentro del SGCC;
- describir su modelo conceptual;
- diferenciarlo de otros mecanismos organizativos;
- definir sus principios de diseño;
- establecer sus responsabilidades;
- servir de base para futuras implementaciones.

---

# Alcance

Esta especificación regula:

- el modelo conceptual de las colecciones;
- sus responsabilidades;
- su estructura lógica;
- su integración con el resto del SGCC;
- los principios de funcionamiento;
- los tipos de colecciones;
- el alcance semántico de una colección.

No regula todavía:

- el modelo técnico de implementación;
- APIs;
- serialización;
- persistencia;
- automatización;
- métricas;
- gobierno operativo.

Estos aspectos se desarrollarán en las siguientes partes.

---

# Motivación

A medida que el SGCC evoluciona aparecen cientos o miles de elementos relacionados entre sí:

- documentos;
- ingredientes;
- recetas;
- técnicas;
- utensilios;
- conceptos;
- relaciones;
- reglas;
- observaciones;
- inferencias.

La simple organización física del repositorio deja de ser suficiente para responder preguntas como:

- ¿qué sabemos sobre fermentación?
- ¿qué conocimiento existe sobre cocina japonesa?
- ¿qué documentación falta sobre carnes?
- ¿qué técnicas utilizan vapor?
- ¿qué recetas pertenecen simultáneamente a dos dominios?
- ¿qué conceptos están poco desarrollados?

Responder estas preguntas requiere una capa lógica superior.

Esa capa son las Colecciones de Conocimiento.

---

# Definición

Una Colección de Conocimiento es una representación lógica y gobernada de un dominio de conocimiento dentro del SGCC.

Define un conjunto coherente de entidades, documentos, relaciones y objetivos unidos por un mismo contexto semántico.

Una colección:

- no almacena conocimiento;
- no duplica información;
- no reorganiza físicamente el repositorio.

Su función consiste en describir un dominio y proyectar una vista sobre el conocimiento existente.

---

# Naturaleza de una colección

Una colección representa simultáneamente:

- un dominio;
- una intención;
- una frontera conceptual;
- una vista lógica;
- un mecanismo de planificación;
- una unidad de evolución.

No constituye un contenedor físico.

---

# Una colección no es...

Para evitar ambigüedades resulta importante diferenciar una colección de otros conceptos del SGCC.

---

## No es una carpeta

Una carpeta organiza archivos.

Una colección organiza conocimiento.

---

## No es un directorio

Los directorios pertenecen al sistema de archivos.

Las colecciones pertenecen al modelo conceptual.

---

## No es una etiqueta

Una etiqueta identifica una característica.

Una colección delimita un dominio completo.

---

## No es una categoría

Las categorías suelen representar una clasificación jerárquica.

Una colección puede combinar múltiples categorías simultáneamente.

---

## No es una taxonomía

La taxonomía clasifica conceptos.

La colección utiliza esa clasificación.

---

## No es una ontología

La ontología responde:

> ¿Qué significa cada concepto?

La colección responde:

> ¿Qué parte del conocimiento queremos considerar como un dominio coherente?

---

## No es el Knowledge Graph

El Knowledge Graph almacena entidades y relaciones.

La colección selecciona una vista significativa sobre ese grafo.

---

## No es una consulta

Una consulta obtiene resultados.

Una colección define un dominio permanente que podrá utilizar consultas para materializar sus contenidos.

---

# Papel dentro del SGCC

Las colecciones constituyen una capa transversal situada por encima de la organización documental y apoyada en el modelo semántico del sistema.

Conceptualmente pueden representarse así:

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
Aplicaciones
Paneles
RAG
Agentes IA
Análisis
```

Las colecciones no sustituyen ninguna de las capas anteriores.

Las integran.

---

# Responsabilidad

La responsabilidad principal de una colección consiste en definir un dominio coherente del conocimiento.

Ello implica:

- determinar su alcance;
- identificar los activos relevantes;
- establecer objetivos;
- medir cobertura;
- identificar deuda;
- facilitar evolución.

No le corresponde:

- editar documentos;
- modificar la ontología;
- alterar relaciones;
- almacenar conocimiento duplicado.

---

# Modelo conceptual

Toda colección puede entenderse como la unión de varias dimensiones complementarias.

```text
Colección
      │
      ├── Dominio
      ├── Alcance
      ├── Activos
      ├── Relaciones
      ├── Contexto
      ├── Objetivos
      ├── Cobertura
      ├── Deuda
      └── Evolución
```

---

# Dominio

Toda colección representa un dominio identificable.

Ejemplos:

- Cocina japonesa
- Fermentaciones
- Arroces
- Panadería
- Conservas
- Salsas madre

El dominio constituye la identidad principal de la colección.

---

# Alcance

El alcance delimita qué conocimiento pertenece al dominio.

Puede definirse mediante:

- criterios conceptuales;
- criterios culinarios;
- criterios históricos;
- criterios geográficos;
- criterios tecnológicos;
- criterios nutricionales.

---

# Frontera conceptual

Toda colección debe definir explícitamente:

- qué incluye;
- qué excluye;
- qué casos son dudosos;
- qué excepciones existen.

Ello evita ambigüedades futuras.

---

# Contexto

Toda colección existe dentro de un contexto.

Ese contexto puede ser:

- culinario;
- geográfico;
- temporal;
- cultural;
- nutricional;
- documental;
- tecnológico.

Dos colecciones pueden compartir activos y diferenciarse únicamente por el contexto.

---

# Vista lógica

Una colección representa una vista.

No representa una copia.

La vista podrá obtenerse mediante:

- referencias explícitas;
- criterios semánticos;
- consultas;
- reglas;
- filtros;
- combinaciones de los anteriores.

---

# Unidad de evolución

Las colecciones evolucionan.

Su evolución describe:

- crecimiento del dominio;
- consolidación;
- aparición de nuevo conocimiento;
- reducción de deuda;
- refinamiento conceptual.

La evolución de una colección no implica necesariamente cambios en los documentos.

---

# Principios de diseño

Toda colección deberá respetar los siguientes principios.

---

## No duplicación

El conocimiento canónico existirá una única vez.

La colección únicamente lo referencia.

---

## Reutilización

Un mismo activo podrá pertenecer simultáneamente a múltiples colecciones.

---

## Independencia física

Las colecciones no modificarán:

- carpetas;
- archivos;
- estructura Git;
- organización documental.

---

## Independencia semántica

Una colección no altera el significado de los conceptos definidos por la ontología.

Únicamente los utiliza.

---

## Trazabilidad

Toda pertenencia deberá ser justificable.

---

## Explicabilidad

Debe poder responderse por qué un determinado activo pertenece a una colección.

---

## Modularidad

Cada colección constituye un dominio independiente.

---

## Composición

Las colecciones podrán construirse a partir de otras colecciones.

---

## Escalabilidad

El modelo deberá permitir miles de colecciones sin degradar su comprensión.

---

## Evolución

Las colecciones deberán evolucionar sin comprometer la estabilidad del SGCC.

---

# Dimensiones de una colección

Conceptualmente toda colección posee varias dimensiones.

---

## Dimensión documental

Determina:

qué documentos participan.

---

## Dimensión semántica

Determina:

qué conceptos participan.

---

## Dimensión relacional

Determina:

qué relaciones resultan relevantes.

---

## Dimensión ontológica

Determina:

qué clases y propiedades intervienen.

---

## Dimensión organizativa

Determina:

qué objetivos persigue la colección.

---

## Dimensión evolutiva

Determina:

cómo madura el dominio.

---

## Dimensión analítica

Permite medir:

- cobertura;
- reutilización;
- deuda;
- crecimiento;
- estabilidad.

---

# Tipología de colecciones

No todas las colecciones representan el mismo tipo de conocimiento.

---

## Colecciones temáticas

Organizan un tema.

Ejemplos:

- Arroces
- Curry
- Cocina mexicana

---

## Colecciones técnicas

Organizan técnicas culinarias.

Ejemplos:

- Fermentación
- Ahumado
- Sous-vide

---

## Colecciones geográficas

Organizan conocimiento por región.

Ejemplos:

- Japón
- Perú
- Andalucía

---

## Colecciones nutricionales

Organizan conocimiento según criterios dietéticos.

Ejemplos:

- Vegetariano
- Sin gluten
- Bajo en sodio

---

## Colecciones tecnológicas

Agrupan conocimiento relacionado con herramientas o procesos.

Ejemplos:

- Horno
- Robot de cocina
- Deshidratador

---

## Colecciones metodológicas

Organizan conocimiento sobre procesos.

Ejemplos:

- Mise en place
- Batch cooking
- Meal prep

---

## Colecciones experimentales

Permiten desarrollar nuevo conocimiento antes de consolidarlo.

---

## Colecciones temporales

Se crean para un objetivo concreto.

Una vez cumplido podrán archivarse.

---

## Colecciones personales

Permiten organizar subconjuntos adaptados a un usuario o proyecto.

No modifican la ontología global.

---

# Relaciones entre colecciones

Las colecciones podrán mantener relaciones entre sí.

Ejemplos:

```text
depende_de
```

```text
extiende
```

```text
especializa
```

```text
complementa
```

```text
requiere
```

```text
deriva_de
```

Estas relaciones no implican jerarquía obligatoria.

---

# Composición

Una colección podrá componerse mediante:

- documentos;
- componentes;
- conceptos;
- relaciones;
- otras colecciones.

La composición nunca implicará duplicación.

---

# Solapamiento

Dos colecciones podrán compartir activos.

Ejemplo:

```text
Fermentación
```

y

```text
Cocina coreana
```

comparten:

Kimchi.

Ello no constituye una inconsistencia.

---

# Exclusividad

Las colecciones no son mutuamente excluyentes.

Un mismo conocimiento podrá pertenecer simultáneamente a múltiples dominios.

---

# Granularidad

Las colecciones podrán existir en diferentes niveles.

Ejemplo:

```text
Cocina asiática
```

↓

```text
Cocina japonesa
```

↓

```text
Ramen
```

Cada nivel representa un dominio distinto.

---

# Fractalidad

Las colecciones presentan una estructura fractal.

Cada colección puede subdividirse en colecciones más específicas sin alterar el modelo conceptual.

---

# Colecciones y reutilización

Una colección deberá favorecer la reutilización del conocimiento existente.

Nunca incentivará la creación de versiones duplicadas de un documento.

---

# Colecciones y objetivos

Además de describir conocimiento, una colección podrá definir objetivos como:

- ampliar cobertura;
- incorporar nuevas recetas;
- mejorar documentación;
- reducir deuda;
- validar inferencias.

---

# Colecciones y deuda

Toda colección podrá medir:

- conocimiento inexistente;
- documentación incompleta;
- relaciones ausentes;
- conceptos pendientes.

---

# Colecciones y madurez

La colección constituye la unidad natural para evaluar la madurez de un dominio.

No todos los dominios evolucionan al mismo ritmo.

---

# Colecciones y planificación

Las colecciones permiten traducir la estrategia del proyecto en objetivos concretos.

Constituyen el puente entre el Roadmap del SGCC y el conocimiento realmente existente.

---

# Colecciones y visualización

Una colección podrá proyectarse mediante diferentes vistas.

Ejemplos:

- documental;
- semántica;
- grafo;
- cronológica;
- analítica;
- tecnológica.

Todas representan el mismo dominio.

---

# Colecciones como vistas semánticas

Desde el punto de vista arquitectónico, una colección puede entenderse como una vista gobernada sobre el ecosistema del SGCC.

```text
Repositorio
      │
      ▼
Documentos
      │
      ▼
Ontología
      │
      ▼
Knowledge Graph
      │
      ▼
Colección
      │
      ├── Vista documental
      ├── Vista semántica
      ├── Vista analítica
      ├── Vista evolutiva
      └── Vista tecnológica
```

La colección no altera ninguna de estas capas.

Simplemente ofrece una forma coherente de observarlas.

---

# Beneficios

La utilización de colecciones aporta, entre otros, los siguientes beneficios:

- organización transversal;
- reutilización sistemática;
- reducción de duplicidades;
- planificación del conocimiento;
- evaluación objetiva;
- integración con el Knowledge Graph;
- preparación para RAG;
- especialización de agentes inteligentes;
- visualización avanzada;
- escalabilidad.

---

# Conclusión

Las Colecciones de Conocimiento representan la unidad lógica mediante la cual el SGCC organiza dominios completos sin alterar la estructura física ni duplicar el conocimiento existente.

Constituyen una capa de abstracción que integra documentos, componentes, relaciones, ontología y Knowledge Graph para ofrecer una visión coherente, reutilizable y evolutiva de cada dominio de conocimiento.

Las siguientes partes desarrollarán el metamodelo formal de una colección, su ciclo de vida, su gobernanza y su integración operativa con el resto de la arquitectura del SGCC.

---

# Parte II — Metamodelo y estructura de una colección

---

# Introducción

La Parte I ha definido las Colecciones de Conocimiento como vistas lógicas, gobernadas y reutilizables sobre el ecosistema del SGCC.

Esta segunda parte formaliza su estructura interna.

El objetivo consiste en establecer un metamodelo suficientemente preciso para que una colección pueda:

- identificarse de forma unívoca;
- declarar su propósito;
- delimitar su alcance;
- seleccionar conocimiento;
- combinar miembros explícitos y calculados;
- expresar exclusiones;
- mantener contexto y procedencia;
- evolucionar mediante versiones;
- integrarse con el Knowledge Graph;
- alimentar procesos de análisis, RAG y agentes inteligentes.

La colección deja así de ser únicamente una idea organizativa y pasa a convertirse en una entidad formal del sistema.

---

# Objetivo del metamodelo

El metamodelo de colecciones define:

- qué elementos forman una colección;
- qué propiedades posee;
- qué relaciones puede mantener;
- cómo se determina la pertenencia;
- cómo se representa su alcance;
- cómo se controla su evolución;
- cómo se valida su consistencia;
- cómo se proyecta sobre el SGCC.

El metamodelo no determina todavía una tecnología concreta de persistencia.

Podrá representarse mediante:

- Markdown;
- YAML;
- JSON;
- JSON-LD;
- RDF;
- bases de datos relacionales;
- Knowledge Graphs;
- APIs.

---

# Nivel metamodelo, modelo e instancia

Las colecciones pueden comprenderse mediante tres niveles.

```text
M2 — Metamodelo de colección
        ↓
M1 — Definición de una colección concreta
        ↓
M0 — Miembros y resultados concretos
```

---

## Nivel M2 — Metamodelo

Define qué es una colección.

Ejemplos de elementos del metamodelo:

- identidad;
- alcance;
- criterio;
- miembro;
- exclusión;
- dependencia;
- versión;
- consulta;
- proyección.

---

## Nivel M1 — Modelo de colección

Representa una colección concreta.

Ejemplo:

```text
Colección: Cocina japonesa
```

Declara:

- su propósito;
- sus criterios;
- sus fuentes;
- sus subcolecciones;
- sus reglas de pertenencia.

---

## Nivel M0 — Instancias

Representa los elementos concretos que forman parte de la colección.

Ejemplos:

- REC-0009 Caballa japonesa;
- ING-0008 Miso;
- TEC-0004 Cocción al vapor;
- documentos relacionados;
- relaciones entre dichos elementos.

---

# Entidad Colección

La entidad central del metamodelo será:

```text
ColeccionConocimiento
```

Una `ColeccionConocimiento` representa una definición gobernada de dominio.

Podrá asociarse a:

- documentos;
- componentes;
- entidades ontológicas;
- relaciones;
- otras colecciones;
- consultas;
- métricas;
- objetivos;
- índices;
- agentes.

---

# Estructura conceptual

Una colección podrá modelarse conceptualmente mediante la siguiente estructura:

```text
ColeccionConocimiento
        │
        ├── Identidad
        ├── Metadatos
        ├── Propósito
        ├── Alcance
        ├── Contexto
        ├── Criterios de pertenencia
        ├── Miembros explícitos
        ├── Miembros calculados
        ├── Exclusiones
        ├── Dependencias
        ├── Subcolecciones
        ├── Consultas
        ├── Proyecciones
        ├── Versiones
        ├── Procedencia
        ├── Gobernanza
        └── Métricas
```

---

# Identidad

Toda colección deberá disponer de identidad persistente.

La identidad no dependerá:

- de su nombre visible;
- de su ruta;
- de su ubicación física;
- de su estado;
- de su versión.

---

## Identificador canónico

Cada colección deberá poseer un identificador único.

Formato recomendado:

```text
COL-XXXX
```

Ejemplos:

```text
COL-0001
COL-0002
COL-0017
```

Los identificadores:

- serán únicos;
- no se reutilizarán;
- permanecerán estables;
- no contendrán significado mutable.

---

## URI canónica

Cuando la colección se publique semánticamente, podrá disponer de una URI persistente.

Ejemplo conceptual:

```text
https://novacoquinaria.org/collection/COL-0001
```

La URI deberá resolver hacia:

- descripción legible;
- metadatos;
- versión actual;
- representaciones disponibles;
- enlaces relacionados.

---

## Identidad y versiones

El identificador de colección representa la identidad conceptual.

La versión representa un estado concreto de esa identidad.

Ejemplo:

```text
Colección: COL-0001
Versión: 2.1.0
```

La creación de una nueva versión no generará necesariamente un nuevo identificador.

---

## Identidad derivada

Una colección derivada de otra deberá conservar identidad propia.

Ejemplo:

```text
COL-0001 Cocina japonesa
COL-0012 Cocina japonesa vegetariana
```

Aunque la segunda derive de la primera, ambas representan dominios distintos.

---

# Nombre

Toda colección deberá poseer un nombre canónico.

Ejemplo:

```text
Cocina japonesa
```

El nombre deberá ser:

- descriptivo;
- estable;
- comprensible;
- no ambiguo dentro del contexto del SGCC.

---

## Nombre corto

Podrá definirse un nombre abreviado.

Ejemplo:

```text
JP Cooking
```

No sustituirá al nombre canónico.

---

## Alias

Una colección podrá declarar alias.

Ejemplo:

```yaml
aliases:
  - Gastronomía japonesa
  - Cocina del Japón
```

Los alias facilitarán:

- búsqueda;
- interoperabilidad;
- traducción;
- resolución terminológica.

---

## Multilingüismo

Podrán declararse etiquetas por idioma.

Ejemplo:

```yaml
labels:
  es: Cocina japonesa
  en: Japanese cuisine
  fr: Cuisine japonaise
  ja: 日本料理
```

El identificador permanecerá independiente del idioma.

---

# Descripción

Toda colección deberá incluir una descripción normativa.

La descripción deberá indicar:

- qué representa;
- para qué existe;
- qué ámbito cubre;
- qué valor aporta.

Ejemplo:

```text
Colección dedicada al conocimiento culinario relacionado con técnicas,
ingredientes, preparaciones, recetas y contextos culturales propios de
la cocina japonesa.
```

---

# Propósito

El propósito expresa la intención funcional de la colección.

Una colección podrá orientarse a:

- organización;
- documentación;
- investigación;
- planificación;
- aprendizaje;
- análisis;
- recuperación de información;
- asistencia inteligente;
- experimentación;
- publicación.

---

## Declaración de propósito

El propósito deberá formularse de forma explícita.

Ejemplo:

```text
Consolidar el conocimiento disponible sobre cocina japonesa y detectar
carencias documentales, semánticas y relacionales dentro del SGCC.
```

---

# Alcance

El alcance define la frontera conceptual de la colección.

Deberá expresar:

- qué incluye;
- qué excluye;
- qué condiciones limitan la pertenencia;
- qué contextos son relevantes;
- qué excepciones existen.

---

## Alcance positivo

Describe qué conocimiento forma parte del dominio.

Ejemplo:

```text
Incluye ingredientes, técnicas, recetas, preparaciones y utensilios
característicos de la cocina japonesa.
```

---

## Alcance negativo

Describe qué conocimiento queda fuera.

Ejemplo:

```text
Excluye recetas de inspiración japonesa que no mantengan una relación
culinaria, histórica o técnica suficientemente justificable con el dominio.
```

---

## Casos fronterizos

La colección podrá documentar casos dudosos.

Ejemplo:

```text
Los platos de fusión nikkei podrán incluirse cuando su relación con la
tradición japonesa esté documentada.
```

---

## Excepciones

Las excepciones deberán ser explícitas, justificadas y trazables.

No deberán introducirse mediante decisiones informales.

---

# Contexto de colección

El contexto permite interpretar correctamente la colección.

Una colección podrá declarar uno o varios contextos.

---

## Contexto culinario

Ejemplos:

- cocina doméstica;
- cocina profesional;
- restauración;
- pastelería;
- conservación;
- producción artesanal.

---

## Contexto geográfico

Ejemplos:

- Japón;
- Andalucía;
- Mediterráneo;
- Sudeste asiático.

---

## Contexto cultural

Ejemplos:

- cocina tradicional;
- cocina festiva;
- cocina religiosa;
- cocina migrante;
- cocina de fusión.

---

## Contexto temporal

Ejemplos:

- cocina histórica;
- cocina contemporánea;
- periodo Edo;
- siglo XXI.

---

## Contexto nutricional

Ejemplos:

- vegetariano;
- sin gluten;
- bajo en sodio;
- alto en proteínas.

---

## Contexto tecnológico

Ejemplos:

- horno;
- robot de cocina;
- sous-vide;
- deshidratación;
- fermentación controlada.

---

## Contexto documental

Ejemplos:

- documentación estable;
- investigación;
- borradores;
- material pedagógico;
- referencias externas.

---

## Contextos combinados

Una colección podrá combinar contextos.

Ejemplo:

```text
Cocina japonesa
+
Vegetariana
+
Doméstica
+
Contemporánea
```

La combinación deberá interpretarse como una intersección contextual, salvo que se especifique otro operador.

---

# Tipo de colección

Toda colección deberá declarar su tipo principal.

Tipos iniciales recomendados:

```text
tematica
tecnica
geografica
cultural
nutricional
tecnologica
metodologica
experimental
temporal
personal
editorial
analitica
operativa
```

---

## Tipado múltiple

Una colección podrá tener más de un tipo.

Ejemplo:

```yaml
types:
  - geografica
  - cultural
  - tematica
```

El tipo principal deberá distinguirse cuando sea necesario.

---

# Modalidad de pertenencia

Según cómo determine sus miembros, una colección podrá ser:

- estática;
- dinámica;
- híbrida.

---

## Colección estática

Sus miembros se declaran explícitamente.

Ejemplo:

```yaml
members:
  - REC-0001
  - REC-0009
  - ING-0008
```

La pertenencia solo cambia mediante edición deliberada.

---

## Colección dinámica

Sus miembros se calculan mediante criterios o consultas.

Ejemplo:

```text
Todas las recetas que utilicen miso.
```

Los resultados podrán cambiar cuando cambie el conocimiento subyacente.

---

## Colección híbrida

Combina:

- miembros explícitos;
- criterios dinámicos;
- exclusiones;
- excepciones.

Será la modalidad recomendada para dominios complejos.

---

# Miembro de colección

Un miembro representa una entidad incluida en la colección.

Podrán ser miembros:

- documentos;
- componentes;
- ingredientes;
- recetas;
- técnicas;
- utensilios;
- preparaciones;
- conceptos ontológicos;
- relaciones;
- observaciones;
- reglas;
- colecciones;
- subgrafos;
- recursos externos.

---

## Referencia, no copia

La pertenencia se expresará mediante una referencia al identificador canónico.

Ejemplo:

```yaml
members:
  - id: REC-0009
```

No se copiará el contenido del miembro dentro de la colección.

---

## Tipo del miembro

Podrá declararse el tipo esperado.

Ejemplo:

```yaml
members:
  - id: REC-0009
    type: receta
```

El tipo declarado deberá coincidir con el tipo real.

---

## Papel dentro de la colección

Un miembro podrá desempeñar un papel específico.

Ejemplos:

```text
nucleo
complementario
referencia
ejemplo
dependencia
evidencia
experimental
```

Ejemplo:

```yaml
members:
  - id: ING-0008
    role: nucleo
```

El papel no modifica la naturaleza ontológica del elemento.

---

## Relevancia

Podrá asignarse un nivel de relevancia.

Ejemplo:

```yaml
relevance: 0.95
```

La relevancia deberá interpretarse dentro de un rango definido.

Recomendación:

```text
0.0 ≤ relevancia ≤ 1.0
```

---

## Justificación de pertenencia

Toda pertenencia explícita debería poder justificar por qué existe.

Ejemplo:

```yaml
justification:
  type: expert
  description: Ingrediente central de múltiples preparaciones japonesas.
```

---

## Procedencia de la pertenencia

Podrá registrarse:

- quién añadió el miembro;
- cuándo;
- mediante qué criterio;
- desde qué fuente;
- con qué confianza.

---

# Miembros explícitos

Los miembros explícitos se declaran manualmente.

Se utilizarán cuando:

- la pertenencia sea normativa;
- el elemento sea fundamental;
- no pueda expresarse mediante una consulta estable;
- exista una excepción deliberada;
- se requiera control editorial.

---

## Inclusiones obligatorias

Podrá declararse que un miembro siempre deberá formar parte de la colección.

Ejemplo:

```yaml
required_members:
  - ING-0008
```

Una inclusión obligatoria tendrá prioridad sobre criterios dinámicos, salvo que una regla de exclusión normativa indique lo contrario.

---

## Inclusiones manuales

Podrán añadirse elementos aunque no cumplan todos los criterios dinámicos.

Estas inclusiones deberán marcarse como excepciones.

Ejemplo:

```yaml
manual_inclusions:
  - id: REC-0021
    reason: Caso de fusión documentado y relevante para el dominio.
```

---

# Miembros calculados

Los miembros calculados se obtienen mediante:

- filtros;
- consultas;
- reglas;
- inferencias;
- combinaciones de colecciones.

---

## Cálculo determinista

Un cálculo será determinista cuando produzca el mismo resultado sobre la misma versión del conocimiento.

---

## Cálculo contextual

Podrá depender de:

- fecha;
- usuario;
- permisos;
- idioma;
- ubicación;
- perfil;
- versión del grafo.

---

## Cálculo materializado

Los resultados podrán materializarse para:

- mejorar rendimiento;
- preservar snapshots;
- auditar;
- reproducir análisis;
- alimentar índices.

La materialización no convierte los resultados en conocimiento canónico nuevo.

---

# Criterio de pertenencia

Un criterio de pertenencia define una condición bajo la cual una entidad forma parte de la colección.

---

## Estructura de un criterio

Todo criterio podrá incluir:

- identificador;
- descripción;
- tipo;
- operador;
- condición;
- prioridad;
- contexto;
- procedencia;
- estado;
- versión.

---

## Identificador del criterio

Formato recomendado:

```text
COL-CRT-XXXX
```

Ejemplo:

```text
COL-CRT-0007
```

---

## Tipos de criterio

Podrán existir criterios:

- documentales;
- tipológicos;
- taxonómicos;
- ontológicos;
- relacionales;
- geográficos;
- temporales;
- nutricionales;
- tecnológicos;
- textuales;
- analíticos;
- inferidos;
- manuales.

---

## Criterio documental

Ejemplo:

```text
Incluir documentos cuyo front matter declare cuisine: japonesa.
```

---

## Criterio tipológico

Ejemplo:

```text
Incluir todas las entidades de tipo Receta.
```

---

## Criterio taxonómico

Ejemplo:

```text
Incluir conceptos situados bajo la categoría Fermentación.
```

---

## Criterio ontológico

Ejemplo:

```text
Incluir individuos de la clase IngredienteFermentado.
```

---

## Criterio relacional

Ejemplo:

```text
Incluir recetas que utilicen miso.
```

---

## Criterio geográfico

Ejemplo:

```text
Incluir conocimiento asociado a Japón o a regiones japonesas.
```

---

## Criterio temporal

Ejemplo:

```text
Incluir técnicas documentadas durante el periodo Edo.
```

---

## Criterio nutricional

Ejemplo:

```text
Incluir recetas aptas para dietas vegetarianas.
```

---

## Criterio textual

Ejemplo:

```text
Incluir documentos que contengan determinados términos controlados.
```

Los criterios textuales deberán utilizarse con precaución.

No deberían sustituir criterios semánticos cuando estos existan.

---

## Criterio inferido

Ejemplo:

```text
Incluir recetas inferidas como japonesas por ingredientes,
técnicas y procedencia documentada.
```

Las pertenencias inferidas deberán conservar explicación.

---

# Operadores lógicos

Los criterios podrán combinarse mediante operadores.

---

## AND

Todos los criterios deben cumplirse.

```text
Receta
AND
Japonesa
AND
Vegetariana
```

---

## OR

Basta con que se cumpla uno.

```text
Utiliza miso
OR
Utiliza shoyu
```

---

## NOT

Excluye resultados.

```text
NOT contiene carne
```

---

## XOR

Solo uno de los criterios podrá cumplirse.

Su uso será excepcional.

---

## Agrupación

Los criterios podrán agruparse.

Ejemplo:

```text
Japonesa
AND
(
  Vegetariana
  OR
  Vegana
)
```

---

# Prioridad de criterios

Cuando existan conflictos, los criterios podrán disponer de prioridad.

Ejemplo:

```yaml
priority: 100
```

Recomendación conceptual:

- 100–199: criterio normativo;
- 50–99: criterio editorial;
- 10–49: criterio automático;
- 1–9: criterio auxiliar.

La escala concreta deberá definirse de forma uniforme.

---

# Conflictos de pertenencia

Puede ocurrir que una entidad cumpla simultáneamente:

- un criterio de inclusión;
- un criterio de exclusión.

La colección deberá disponer de una política explícita de resolución.

---

## Políticas posibles

```text
exclusion_wins
```

La exclusión prevalece.

```text
inclusion_wins
```

La inclusión prevalece.

```text
highest_priority
```

Prevalece el criterio con mayor prioridad.

```text
manual_review
```

El caso requiere revisión.

La política recomendada será:

```text
highest_priority
```

con revisión manual en caso de empate.

---

# Exclusiones

Una colección podrá definir exclusiones explícitas y dinámicas.

---

## Exclusión explícita

Ejemplo:

```yaml
excluded_members:
  - id: REC-0042
    reason: No representa cocina japonesa pese a utilizar miso.
```

---

## Exclusión por criterio

Ejemplo:

```text
Excluir recetas que solo empleen ingredientes japoneses como sustitución
moderna sin relación cultural o técnica con el dominio.
```

---

## Exclusión temporal

Podrá excluirse un miembro durante un periodo.

Ejemplo:

```yaml
valid_until: 2026-12-31
```

---

## Exclusión contextual

Un miembro podrá quedar excluido solo en un contexto determinado.

Ejemplo:

```text
Una preparación puede pertenecer a la colección general,
pero quedar excluida del perfil tradicional.
```

---

# Evidencia de pertenencia

La pertenencia podrá estar respaldada por evidencia.

Tipos de evidencia:

- documento interno;
- referencia bibliográfica;
- fuente externa;
- criterio experto;
- inferencia ontológica;
- observación;
- cálculo;
- consenso editorial.

---

## Confianza

Toda pertenencia no normativa podrá declarar confianza.

Ejemplo:

```yaml
confidence: 0.82
```

La confianza no deberá confundirse con relevancia.

- relevancia: importancia dentro de la colección;
- confianza: seguridad sobre la pertenencia.

---

## Niveles cualitativos

Podrán utilizarse niveles:

```text
confirmada
probable
posible
disputada
rechazada
```

---

# Estado de pertenencia

La relación entre un miembro y una colección podrá tener estado.

Ejemplos:

```text
propuesta
aceptada
inferida
temporal
disputada
excluida
obsoleta
```

---

# Dependencias

Una colección podrá depender de:

- otra colección;
- un módulo ontológico;
- un vocabulario;
- un conjunto documental;
- una fuente externa;
- un servicio;
- una versión concreta del Knowledge Graph.

---

## Dependencia fuerte

La colección no puede resolverse sin ella.

Ejemplo:

```text
Cocina japonesa vegetariana
depende de
Cocina japonesa
```

---

## Dependencia débil

Mejora la colección, pero no impide su funcionamiento.

---

## Dependencia de versión

Podrá fijarse una versión mínima, máxima o exacta.

Ejemplo:

```yaml
requires:
  - id: ONT-MOD-INGREDIENTS
    version: ">=2.0.0"
```

---

# Relaciones entre colecciones

Las colecciones podrán relacionarse mediante propiedades formales.

Relaciones recomendadas:

```text
contiene
```

```text
subcoleccion_de
```

```text
extiende
```

```text
especializa
```

```text
complementa
```

```text
depende_de
```

```text
deriva_de
```

```text
solapa_con
```

```text
sustituye_a
```

```text
es_equivalente_a
```

---

## Subcolección

Una subcolección representa un dominio más específico.

Ejemplo:

```text
Ramen
subcoleccion_de
Cocina japonesa
```

La pertenencia de una subcolección a otra no implica necesariamente que todos sus miembros se materialicen en la colección superior.

La política deberá declararse.

---

## Herencia de miembros

Podrán existir tres políticas:

```text
inherit_all
```

La colección superior incluye todos los miembros.

```text
inherit_none
```

No existe propagación automática.

```text
inherit_by_rule
```

La propagación depende de criterios.

La política recomendada será:

```text
inherit_by_rule
```

---

## Extensión

Una colección que extiende otra añade:

- criterios;
- miembros;
- contexto;
- exclusiones;
- objetivos.

Ejemplo:

```text
Cocina japonesa contemporánea
extiende
Cocina japonesa
```

---

## Especialización

Una especialización restringe el alcance.

Ejemplo:

```text
Cocina japonesa vegana
especializa
Cocina japonesa
```

---

## Complementariedad

Dos colecciones pueden complementarse sin existir dependencia jerárquica.

Ejemplo:

```text
Fermentaciones japonesas
complementa
Conservación tradicional japonesa
```

---

## Solapamiento

La relación `solapa_con` podrá incluir una medida.

Ejemplo:

```yaml
overlap:
  collection: COL-0004
  ratio: 0.37
```

La métrica deberá indicar qué conjunto se utiliza como denominador.

---

# Composición de colecciones

Una colección podrá definirse mediante operaciones sobre otras colecciones.

---

## Unión

```text
A ∪ B
```

Incluye miembros de ambas colecciones.

Ejemplo:

```text
Cocina japonesa
UNION
Cocina coreana
```

---

## Intersección

```text
A ∩ B
```

Incluye miembros compartidos.

Ejemplo:

```text
Cocina japonesa
INTERSECT
Vegetariana
```

---

## Diferencia

```text
A − B
```

Incluye miembros de A que no pertenecen a B.

Ejemplo:

```text
Cocina japonesa
MINUS
Pescados y mariscos
```

---

## Diferencia simétrica

Incluye miembros pertenecientes a una colección u otra, pero no a ambas.

Su uso será excepcional.

---

## Composición anidada

Podrán combinarse operaciones.

Ejemplo:

```text
(
  Cocina japonesa
  INTERSECT
  Vegetariana
)
MINUS
Contiene huevo
```

---

# Colección base y colección derivada

Una colección derivada se construye a partir de otras colecciones o criterios.

---

## Colección base

Puede resolverse sin depender de otra colección.

---

## Colección derivada

Su definición depende de:

- colecciones base;
- operadores;
- filtros;
- contexto.

Ejemplo:

```yaml
derived_from:
  operator: intersection
  collections:
    - COL-0001
    - COL-0006
```

---

# Consultas asociadas

Una colección podrá disponer de una o varias consultas.

---

## Consulta de resolución

Determina sus miembros.

---

## Consulta de cobertura

Calcula cuánto conocimiento existe.

---

## Consulta de deuda

Identifica elementos ausentes o incompletos.

---

## Consulta analítica

Calcula métricas.

---

## Consulta de navegación

Genera vistas para usuarios o agentes.

---

## Consulta de validación

Comprueba invariantes.

---

# Lenguajes de consulta

Las consultas podrán expresarse mediante:

- sintaxis declarativa interna;
- SPARQL;
- Cypher;
- SQL;
- GraphQL;
- reglas;
- filtros YAML;
- expresiones de dominio.

La colección deberá permanecer independiente de un lenguaje concreto.

---

# Consulta canónica

Cuando existan varias representaciones técnicas, deberá identificarse una consulta canónica o una definición semántica común.

Ejemplo:

```yaml
query:
  language: sgcc-filter
  expression:
    type: receta
    related_to:
      predicate: usa_ingrediente
      object: ING-0008
```

De esta definición podrán generarse consultas técnicas.

---

# Parámetros

Una colección podrá aceptar parámetros.

Ejemplos:

- fecha;
- idioma;
- usuario;
- ubicación;
- número de comensales;
- equipamiento disponible;
- restricciones alimentarias.

---

## Colección parametrizada

Ejemplo conceptual:

```text
Recetas disponibles para:
- 4 personas;
- menos de 30 minutos;
- sin gluten;
- con ingredientes de despensa.
```

Los parámetros no alteran la identidad de la colección base, salvo que representen una definición estable independiente.

---

# Proyección de colección

Una colección puede proyectar diferentes representaciones del mismo dominio.

---

## Proyección documental

Incluye:

- documentos;
- secciones;
- componentes;
- referencias.

---

## Proyección semántica

Incluye:

- conceptos;
- tipos;
- relaciones;
- axiomas relevantes.

---

## Proyección de grafo

Incluye:

- nodos;
- aristas;
- propiedades;
- subgrafos.

---

## Proyección analítica

Incluye:

- métricas;
- distribución;
- cobertura;
- evolución;
- deuda.

---

## Proyección RAG

Incluye:

- documentos recuperables;
- chunks;
- embeddings;
- contexto semántico;
- filtros de recuperación.

---

## Proyección para agentes

Incluye:

- contexto;
- herramientas;
- permisos;
- reglas;
- objetivos;
- memoria especializada.

---

# Subgrafo de colección

Una colección podrá resolverse como un subgrafo del Knowledge Graph.

El subgrafo podrá contener:

- miembros directos;
- relaciones entre miembros;
- vecinos contextuales;
- entidades auxiliares;
- procedencia;
- inferencias.

---

## Profundidad de expansión

La colección podrá declarar cuántos saltos relacionales incluir.

Ejemplo:

```yaml
graph_projection:
  depth: 2
```

---

## Predicados permitidos

Podrá limitarse la expansión a determinadas relaciones.

Ejemplo:

```yaml
allowed_predicates:
  - usa_ingrediente
  - aplica_tecnica
  - pertenece_a_cocina
```

---

## Predicados excluidos

Podrán excluirse relaciones irrelevantes.

---

## Nodos auxiliares

Una proyección podrá incluir nodos necesarios para explicar relaciones, aunque no sean miembros principales.

Estos nodos deberán marcarse como auxiliares.

---

# Vista materializada

Una colección dinámica podrá materializarse.

Una vista materializada contendrá:

- identificador de colección;
- versión;
- fecha de resolución;
- versión del Knowledge Graph;
- criterios utilizados;
- miembros resultantes;
- hash;
- métricas.

---

## Snapshot

Un snapshot representa una resolución inmutable.

Formato conceptual:

```text
COL-0001@2.0.0
KG@1.4.0
2026-07-31T12:00:00+02:00
```

Los snapshots permiten:

- reproducibilidad;
- auditoría;
- comparación;
- experimentación;
- publicación.

---

# Temporalidad

Las colecciones podrán incorporar temporalidad.

---

## Tiempo de validez

Periodo durante el que una definición es válida.

---

## Tiempo de transacción

Momento en que se registró el cambio.

---

## Pertenencia temporal

Un miembro podrá pertenecer solo durante un intervalo.

Ejemplo:

```yaml
membership:
  valid_from: 2026-01-01
  valid_until: 2026-12-31
```

---

## Colecciones históricas

Podrán representar estados del conocimiento en un periodo.

Ejemplo:

```text
Cocina española del siglo XIX
```

---

## Colecciones de seguimiento

Podrán observar cambios a lo largo del tiempo.

Ejemplo:

```text
Recetas incorporadas durante 2026
```

---

# Procedencia

Toda colección deberá mantener trazabilidad de su origen.

---

## Procedencia de la definición

Deberá registrarse:

- autor;
- fecha;
- fuente;
- motivación;
- decisión asociada;
- versión inicial.

---

## Procedencia de criterios

Cada criterio podrá indicar:

- quién lo propuso;
- quién lo aprobó;
- fuente culinaria;
- evidencia;
- fecha;
- versión.

---

## Procedencia de resultados

Una pertenencia calculada deberá registrar:

- consulta;
- versión;
- fuente de datos;
- motor;
- momento de cálculo.

---

## PROV-O

Cuando se utilice RDF, la procedencia podrá alinearse con PROV-O.

Conceptos posibles:

- Entity;
- Activity;
- Agent;
- wasGeneratedBy;
- wasAttributedTo;
- used;
- wasDerivedFrom.

---

# Versionado

Toda colección deberá estar versionada.

Formato recomendado:

```text
MAJOR.MINOR.PATCH
```

---

## Cambio PATCH

No modifica la pertenencia ni el significado.

Ejemplos:

- corrección ortográfica;
- mejora de descripción;
- ampliación de ejemplos;
- metadatos no normativos.

---

## Cambio MINOR

Amplía la colección de forma compatible.

Ejemplos:

- nuevo criterio opcional;
- nueva proyección;
- nueva consulta;
- nuevos miembros explícitos;
- nuevas métricas.

---

## Cambio MAJOR

Modifica de forma incompatible:

- propósito;
- alcance;
- semántica;
- criterios fundamentales;
- política de resolución;
- identidad conceptual.

---

## Versionado de resultados

La definición de la colección y sus resultados deberán versionarse por separado.

Ejemplo:

```text
Definición de colección: 2.1.0
Snapshot de miembros: 2026.07.31.1
```

---

# Perfil de colección

Un perfil define una configuración particular sobre una colección.

Ejemplo:

```text
Colección: Cocina japonesa
Perfil: Tradicional
```

Otro perfil:

```text
Colección: Cocina japonesa
Perfil: Doméstica contemporánea
```

---

## Elementos de un perfil

Un perfil podrá modificar:

- contexto;
- criterios;
- exclusiones;
- profundidad de grafo;
- fuentes;
- proyecciones;
- permisos.

---

## Perfil no destructivo

Un perfil no modificará la definición base.

Actuará como especialización declarativa.

---

# Metadatos

Toda colección deberá disponer de un conjunto mínimo de metadatos.

Campos recomendados:

```yaml
id:
type:
title:
description:
version:
status:
created_at:
updated_at:
created_by:
maintainer:
language:
license:
```

---

## Metadatos adicionales

Podrán incluirse:

```yaml
aliases:
labels:
tags:
contexts:
owners:
reviewers:
visibility:
maturity:
quality:
deprecated:
replaced_by:
```

---

# Estado de colección

El estado forma parte de su metamodelo.

Valores recomendados:

```text
propuesta
borrador
en_revision
en_desarrollo
en_consolidacion
de_referencia
obsoleta
archivada
```

La semántica completa del ciclo de vida se desarrollará en la Parte III.

---

# Madurez

La madurez no equivale al estado.

Una colección puede estar:

```text
estable
```

como definición, pero poseer:

```text
baja madurez
```

en cuanto a cobertura.

Niveles iniciales:

```text
inicial
emergente
estructurada
consolidada
referencia
```

---

# Visibilidad

Una colección podrá ser:

```text
publica
interna
privada
restringida
```

---

# Permisos

Podrán definirse permisos sobre:

- lectura;
- edición;
- aprobación;
- publicación;
- resolución;
- materialización;
- exportación;
- uso por agentes.

La colección no deberá conceder acceso a conocimiento que el usuario no pueda consultar directamente.

---

# Responsable

Toda colección deberá tener al menos un responsable.

Podrán existir:

- propietario;
- mantenedor;
- revisor semántico;
- experto culinario;
- responsable técnico.

---

# Objetivos

Una colección podrá declarar objetivos.

Ejemplos:

- documentar diez técnicas;
- reducir deuda;
- añadir relaciones;
- alcanzar un nivel de cobertura;
- preparar un índice RAG;
- publicar una vista temática.

---

## Objetivo medible

Todo objetivo debería incluir:

- descripción;
- métrica;
- valor objetivo;
- fecha;
- responsable;
- estado.

Ejemplo:

```yaml
goals:
  - id: COL-GOAL-0001
    metric: coverage
    target: 0.85
    due_date: 2026-12-31
```

---

# Hitos

Los hitos representan resultados relevantes.

Ejemplos:

- alcance aprobado;
- primera versión publicada;
- subgrafo generado;
- deuda crítica resuelta;
- índice RAG disponible.

---

# Métricas declaradas

Aunque la evaluación se desarrollará en la Parte III, el metamodelo deberá permitir declarar métricas.

Ejemplos:

- número de miembros;
- cobertura;
- deuda;
- densidad relacional;
- estabilidad;
- crecimiento;
- reutilización;
- calidad;
- madurez.

---

# Reglas de consistencia

Toda colección deberá respetar al menos las siguientes reglas.

---

## Identidad única

No podrán existir dos colecciones activas con el mismo identificador.

---

## Nombre no vacío

Toda colección deberá tener nombre.

---

## Propósito obligatorio

Toda colección deberá indicar para qué existe.

---

## Alcance explícito

El alcance deberá estar definido.

---

## Tipo válido

El tipo deberá pertenecer al vocabulario controlado.

---

## Referencias resolubles

Todos los miembros explícitos deberán existir.

---

## Ausencia de ciclos inválidos

No podrán existir ciclos en relaciones como:

```text
subcoleccion_de
```

cuando se definan como jerárquicas.

---

## Dependencias resolubles

Toda dependencia obligatoria deberá existir.

---

## Versiones compatibles

Las dependencias deberán satisfacer las restricciones de versión.

---

## Consultas válidas

Las consultas deberán poder analizarse o ejecutarse.

---

## Conflictos gestionados

Toda colisión inclusión-exclusión deberá resolverse conforme a una política declarada.

---

# Restricciones

El metamodelo podrá incluir restricciones adicionales.

Ejemplos:

- cardinalidad mínima de responsables;
- profundidad máxima de subcolecciones;
- número máximo de criterios automáticos;
- obligatoriedad de evidencias;
- límites de confianza;
- compatibilidad entre tipos.

---

# Validación estructural

La validación estructural comprobará:

- campos obligatorios;
- tipos de datos;
- formatos;
- enumeraciones;
- referencias;
- versiones;
- identificadores.

---

# Validación semántica

La validación semántica comprobará:

- coherencia del alcance;
- contradicciones;
- ciclos;
- duplicidades;
- criterios incompatibles;
- relaciones incorrectas;
- solapamientos anómalos.

---

# Validación operativa

La validación operativa comprobará:

- que las consultas pueden ejecutarse;
- que la colección puede resolverse;
- que las dependencias están disponibles;
- que la materialización es reproducible;
- que los permisos son correctos.

---

# Contrato YAML

La representación YAML será inicialmente la forma estructurada recomendada para definir colecciones.

---

## Ejemplo mínimo

```yaml
id: COL-0001
type: collection
title: Cocina japonesa
version: 1.0.0
status: en_desarrollo

description: >
  Colección de conocimiento dedicada a ingredientes, técnicas,
  preparaciones y recetas de la cocina japonesa.

purpose: >
  Consolidar el conocimiento disponible sobre cocina japonesa
  dentro del SGCC.

scope:
  includes:
    - ingredientes japoneses
    - técnicas culinarias japonesas
    - recetas japonesas
  excludes:
    - recetas de inspiración japonesa sin justificación documental
```

---

## Ejemplo estructural ampliado

```yaml
id: COL-0001
type: collection
collection_types:
  - geografica
  - cultural
  - tematica

title: Cocina japonesa

labels:
  es: Cocina japonesa
  en: Japanese cuisine
  fr: Cuisine japonaise
  ja: 日本料理

aliases:
  - Gastronomía japonesa

version: 2.0.0
status: en_consolidacion
maturity: estructurada
visibility: interna

description: >
  Vista gobernada del conocimiento culinario relacionado con Japón,
  incluyendo ingredientes, técnicas, utensilios, preparaciones,
  recetas y contextos culturales.

purpose: >
  Consolidar, evaluar y ampliar el conocimiento sobre cocina japonesa,
  y servir como base para navegación semántica, análisis y recuperación RAG.

scope:
  includes:
    - ingredients
    - techniques
    - preparations
    - recipes
    - equipment
    - cultural_contexts

  excludes:
    - fusion_without_evidence
    - marketing_only_associations

  boundary_cases:
    - nikkei_cuisine
    - westernized_japanese_recipes

contexts:
  geographic:
    - Japan

  cultural:
    - traditional
    - contemporary

  documentary:
    - stable
    - research

membership_mode: hybrid

conflict_policy: highest_priority
```

---

# Ejemplo de miembros explícitos

```yaml
explicit_members:
  - id: ING-0008
    type: ingrediente
    role: nucleo
    relevance: 1.0
    confidence: 1.0
    status: aceptada
    justification:
      type: expert
      description: Ingrediente fundamental de la cocina japonesa.

  - id: REC-0009
    type: receta
    role: ejemplo
    relevance: 0.85
    confidence: 0.95
    status: aceptada
```

---

# Ejemplo de criterios

```yaml
criteria:
  - id: COL-CRT-0001
    type: ontological
    description: Incluir recetas clasificadas como japonesas.
    priority: 80

    condition:
      instance_of: RECETA
      property:
        predicate: pertenece_a_cocina
        object: COCINA_JAPONESA

  - id: COL-CRT-0002
    type: relational
    description: Incluir recetas relacionadas con ingredientes japoneses.
    priority: 30

    condition:
      path:
        - usa_ingrediente
        - originario_de
      target: JAPON

  - id: COL-CRT-0003
    type: exclusion
    description: Excluir asociaciones puramente nominales.
    priority: 90

    condition:
      property:
        predicate: asociacion_no_documentada
        value: true
```

---

# Ejemplo de exclusiones

```yaml
excluded_members:
  - id: REC-0042
    reason: >
      Utiliza miso, pero no mantiene relación culinaria documentada
      con la cocina japonesa.
    authority: editorial_review
    date: 2026-07-31
```

---

# Ejemplo de dependencias

```yaml
dependencies:
  required:
    - id: ONT-MOD-INGREDIENTS
      type: ontology_module
      version: ">=2.0.0"

    - id: ONT-MOD-RECIPES
      type: ontology_module
      version: ">=1.3.0"

  optional:
    - id: COL-0007
      type: collection
      relation: complementa
```

---

# Ejemplo de composición

```yaml
composition:
  operator: intersection

  operands:
    - collection: COL-0001
    - collection: COL-0006

  exclusions:
    - collection: COL-0014
```

Interpretación:

```text
Cocina japonesa
INTERSECT
Vegetariana
MINUS
Contiene pescado
```

---

# Ejemplo de consulta

```yaml
queries:
  membership:
    language: sgcc-filter

    expression:
      all:
        - type: recipe

        - related:
            predicate: belongs_to_cuisine
            object: japanese_cuisine

  graph_projection:
    language: sgcc-graph

    expression:
      depth: 2

      allowed_predicates:
        - uses_ingredient
        - applies_technique
        - belongs_to_cuisine
        - requires_equipment
```

---

# Ejemplo de proyecciones

```yaml
projections:
  - id: documentary
    type: document_view
    enabled: true

  - id: graph
    type: subgraph
    enabled: true
    depth: 2

  - id: rag
    type: retrieval_index
    enabled: false

  - id: dashboard
    type: analytical_view
    enabled: true
```

---

# Ejemplo de objetivos

```yaml
goals:
  - id: COL-GOAL-0001
    description: Alcanzar una cobertura documental del 85 %.
    metric: documentary_coverage
    target: 0.85
    due_date: 2026-12-31
    status: active

  - id: COL-GOAL-0002
    description: Resolver entidades huérfanas del dominio.
    metric: orphan_entities
    target: 0
    due_date: 2026-10-31
    status: active
```

---

# Ejemplo completo

```yaml
id: COL-0001
type: collection

collection_types:
  - geografica
  - cultural
  - tematica

title: Cocina japonesa

labels:
  es: Cocina japonesa
  en: Japanese cuisine
  fr: Cuisine japonaise
  ja: 日本料理

aliases:
  - Gastronomía japonesa

version: 2.0.0
status: en_consolidacion
maturity: estructurada
visibility: interna

created_at: 2026-07-01
updated_at: 2026-07-31

created_by: Fran
maintainer: knowledge_architecture_team

description: >
  Vista gobernada del conocimiento culinario relacionado con Japón,
  incluyendo ingredientes, técnicas, utensilios, preparaciones,
  recetas y contextos culturales.

purpose: >
  Consolidar, evaluar y ampliar el conocimiento sobre cocina japonesa,
  y servir como base para navegación semántica, análisis,
  recuperación RAG y agentes especializados.

scope:
  includes:
    - ingredients
    - techniques
    - preparations
    - recipes
    - equipment
    - cultural_contexts

  excludes:
    - fusion_without_evidence
    - marketing_only_associations

  boundary_cases:
    - nikkei_cuisine
    - westernized_japanese_recipes

contexts:
  geographic:
    - Japan

  cultural:
    - traditional
    - contemporary

  documentary:
    - stable
    - research

membership_mode: hybrid
conflict_policy: highest_priority

explicit_members:
  - id: ING-0008
    type: ingrediente
    role: nucleo
    relevance: 1.0
    confidence: 1.0
    status: aceptada

  - id: REC-0009
    type: receta
    role: ejemplo
    relevance: 0.85
    confidence: 0.95
    status: aceptada

criteria:
  - id: COL-CRT-0001
    type: ontological
    description: Incluir recetas clasificadas como japonesas.
    priority: 80

    condition:
      instance_of: RECETA
      property:
        predicate: pertenece_a_cocina
        object: COCINA_JAPONESA

  - id: COL-CRT-0002
    type: relational
    description: Incluir recetas vinculadas con ingredientes japoneses.
    priority: 30

    condition:
      path:
        - usa_ingrediente
        - originario_de
      target: JAPON

excluded_members:
  - id: REC-0042
    reason: >
      No mantiene una relación culinaria suficientemente documentada
      con la cocina japonesa.

dependencies:
  required:
    - id: ONT-MOD-INGREDIENTS
      type: ontology_module
      version: ">=2.0.0"

    - id: ONT-MOD-RECIPES
      type: ontology_module
      version: ">=1.3.0"

relations:
  - predicate: complementa
    object: COL-0007

queries:
  membership:
    language: sgcc-filter

    expression:
      all:
        - type: recipe

        - related:
            predicate: belongs_to_cuisine
            object: japanese_cuisine

projections:
  - id: documentary
    type: document_view
    enabled: true

  - id: graph
    type: subgraph
    enabled: true
    depth: 2

  - id: rag
    type: retrieval_index
    enabled: false

goals:
  - id: COL-GOAL-0001
    description: Alcanzar una cobertura documental del 85 %.
    metric: documentary_coverage
    target: 0.85
    due_date: 2026-12-31
    status: active

governance:
  owner: knowledge_architecture_team

  reviewers:
    - culinary_domain_expert
    - semantic_reviewer

  approval_required: true
```

---

# Esquema conceptual resumido

```text
ColeccionConocimiento
        │
        ├── tieneIdentidad
        ├── tieneNombre
        ├── tienePropósito
        ├── defineAlcance
        ├── operaEnContexto
        ├── tieneTipo
        ├── usaCriterio
        ├── incluyeMiembro
        ├── excluyeMiembro
        ├── dependeDe
        ├── seRelacionaCon
        ├── seComponeDe
        ├── generaProyección
        ├── generaSnapshot
        ├── tieneVersión
        ├── tieneResponsable
        └── persigueObjetivo
```

---

# Antipatrones de modelado

Deberán evitarse los siguientes antipatrones.

---

## Copiar contenido dentro de la colección

La colección debe referenciar, no duplicar.

---

## Utilizar nombres como identificadores

Los nombres pueden cambiar.

Los identificadores deben permanecer estables.

---

## Definir pertenencia únicamente mediante etiquetas libres

Las etiquetas no ofrecen suficiente semántica.

---

## Crear colecciones sin propósito

Una colección sin intención clara se convierte en una agrupación arbitraria.

---

## Crear colecciones sin alcance negativo

No indicar qué queda fuera provoca ambigüedad.

---

## Dependencias circulares

Las dependencias fuertes no deberán formar ciclos.

---

## Subcolecciones puramente decorativas

Toda subcolección deberá representar una frontera conceptual real.

---

## Criterios no explicables

Todo criterio deberá poder justificarse.

---

## Mezclar definición y resultados

La definición de la colección debe separarse de sus miembros calculados.

---

## Confundir relevancia con confianza

Ambos valores representan conceptos distintos.

---

## Materializaciones sin versión

Toda vista materializada deberá poder reproducirse.

---

## Convertir una colección en una ontología paralela

Las colecciones utilizan la ontología.

No deberán redefinir sus clases ni propiedades.

---

# Perfil mínimo de implementación

La primera implementación podrá limitarse a:

- identificador;
- nombre;
- descripción;
- propósito;
- alcance;
- tipo;
- estado;
- versión;
- miembros explícitos;
- referencias;
- responsable;
- criterios simples;
- exclusiones;
- relaciones entre colecciones.

---

# Perfil estructural

El perfil estructural añadirá:

- contextos;
- dependencias;
- composición;
- consultas;
- perfiles;
- procedencia;
- validación automática.

---

# Perfil semántico

El perfil semántico añadirá:

- criterios ontológicos;
- resolución sobre Knowledge Graph;
- subgrafos;
- inferencias;
- explicaciones;
- SHACL;
- RDF y JSON-LD.

---

# Perfil inteligente

El perfil inteligente añadirá:

- índices RAG;
- recuperación híbrida;
- embeddings;
- agentes especializados;
- personalización;
- recomendaciones;
- evaluación automática de deuda y madurez.

---

# Conclusión

El metamodelo definido en esta parte convierte las Colecciones de Conocimiento en entidades formales, identificables, versionadas, consultables y gobernables dentro del SGCC.

Una colección ya no se limita a enumerar documentos o describir un dominio.

Puede:

- delimitar su alcance;
- declarar contexto;
- seleccionar miembros;
- combinar criterios;
- resolver conflictos;
- excluir excepciones;
- depender de otros elementos;
- componerse a partir de otras colecciones;
- proyectar subgrafos;
- generar vistas materializadas;
- alimentar índices y agentes;
- conservar procedencia;
- evolucionar mediante versiones.

La Parte III desarrollará el ciclo de vida, la evaluación, la calidad y la gobernanza de las colecciones, incluyendo:

- creación;
- revisión;
- aprobación;
- estados;
- cobertura;
- madurez;
- deuda;
- métricas;
- auditoría;
- publicación;
- deprecación;
- migraciones;
- responsabilidades.

---

# Parte III — Ciclo de vida, evaluación y gobernanza

---

# Introducción

Las dos partes anteriores han definido:

- qué es una Colección de Conocimiento;
- cuál es su papel dentro del SGCC;
- cuál es su estructura conceptual;
- cuál es su metamodelo.

Esta tercera parte define cómo una colección evoluciona a lo largo del tiempo.

Las colecciones son entidades vivas.

Nacen para organizar un dominio determinado, evolucionan conforme aumenta el conocimiento disponible, alcanzan distintos niveles de madurez y, cuando resulta necesario, pueden quedar obsoletas o archivarse.

Por ello resulta imprescindible establecer un marco formal de gobernanza que garantice:

- coherencia;
- trazabilidad;
- calidad;
- reproducibilidad;
- sostenibilidad.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir el ciclo de vida completo de una colección;
- establecer los estados oficiales;
- regular la evolución de una colección;
- definir el modelo de gobernanza;
- establecer mecanismos de auditoría;
- medir calidad y madurez;
- gestionar deuda de conocimiento;
- regular publicación y archivado;
- asegurar la trazabilidad histórica.

---

# Principios de gobernanza

Toda colección deberá evolucionar conforme a los siguientes principios.

---

## Estabilidad conceptual

El propósito de una colección no deberá modificarse de forma arbitraria.

Si el dominio cambia radicalmente deberá evaluarse la creación de una nueva colección.

---

## Evolución incremental

Las modificaciones deberán realizarse mediante cambios pequeños y controlados.

---

## Compatibilidad

Siempre que sea posible deberá mantenerse compatibilidad con versiones anteriores.

---

## Trazabilidad

Todo cambio deberá responder a:

- qué cambió;
- quién lo realizó;
- cuándo;
- por qué;
- qué impacto produjo.

---

## Transparencia

Toda decisión importante deberá estar documentada.

---

## Revisión

Las modificaciones significativas deberán revisarse antes de publicarse.

---

## Reproducibilidad

Una colección publicada deberá poder reconstruirse exactamente.

---

# Ciclo de vida

Toda colección seguirá un ciclo de vida.

Modelo recomendado:

```text
Idea
    │
    ▼
Propuesta
    │
    ▼
Borrador
    │
    ▼
En revisión
    │
    ▼
En desarrollo
    │
    ▼
En consolidación
    │
    ▼
De referencia
    │
    ▼
Obsoleta
    │
    ▼
Archivada
```

---

# Idea

Corresponde a una necesidad detectada.

Todavía no existe una colección formal.

Puede originarse por:

- aparición de un nuevo dominio;
- crecimiento documental;
- necesidades de investigación;
- necesidades de RAG;
- nuevos agentes;
- nuevas líneas gastronómicas.

---

# Propuesta

La colección comienza a definirse.

Debe especificarse:

- nombre;
- objetivo;
- dominio;
- justificación;
- responsable inicial.

Aún no forma parte del modelo oficial.

---

# Borrador

La colección ya dispone de estructura.

Se desarrollan:

- alcance;
- criterios;
- contexto;
- relaciones;
- primeros miembros.

Puede modificarse libremente.

---

# En revisión

La colección se somete a evaluación.

Se revisan:

- coherencia;
- redundancias;
- conflictos;
- alcance;
- compatibilidad.

---

# En desarrollo

La colección ya puede utilizarse.

Sin embargo:

- continúa creciendo;
- incorpora nuevo conocimiento;
- aún no representa completamente el dominio.

---

# En consolidación

La mayor parte del conocimiento ya está documentado.

Las modificaciones son menos frecuentes.

El esfuerzo se centra en:

- calidad;
- consistencia;
- deuda restante;
- optimización.

---

# De referencia

Representa el máximo nivel operativo.

La colección:

- es estable;
- posee alta cobertura;
- mantiene baja deuda;
- dispone de buena trazabilidad;
- supera las validaciones.

---

# Obsoleta

La colección continúa existiendo.

Pero:

- deja de recomendarse;
- puede existir un reemplazo;
- permanece por compatibilidad histórica.

---

# Archivada

Se conserva únicamente con fines históricos.

No evoluciona.

---

# Transiciones

No todas las transiciones serán válidas.

Ejemplo recomendado:

```text
Propuesta
↓

Borrador
↓

En revisión
↓

En desarrollo
↓

En consolidación
↓

De referencia
```

No debería permitirse:

```text
Propuesta

↓

De referencia
```

sin pasar por las revisiones correspondientes.

---

# Reglas de transición

Toda transición deberá:

- registrarse;
- justificarse;
- conservar autor;
- conservar fecha;
- actualizar versión.

---

# Registro histórico

Toda colección mantendrá un historial.

Cada cambio incluirá:

- versión;
- autor;
- fecha;
- descripción;
- motivo;
- revisión asociada.

---

# Versionado

Las colecciones utilizarán versionado semántico.

```text
MAJOR.MINOR.PATCH
```

---

## Cambios PATCH

Ejemplos:

- corrección documental;
- aclaración;
- metadatos;
- ejemplos.

---

## Cambios MINOR

Ejemplos:

- nuevos criterios;
- nuevas consultas;
- nuevos miembros;
- nuevos objetivos;
- nuevas proyecciones.

---

## Cambios MAJOR

Ejemplos:

- cambio de alcance;
- redefinición del dominio;
- modificación incompatible;
- reorganización conceptual.

---

# Evolución de la cobertura

Toda colección evolucionará respecto a la cantidad de conocimiento disponible.

La cobertura podrá aumentar mediante:

- nuevos documentos;
- nuevas entidades;
- nuevas relaciones;
- nuevos conceptos;
- nuevas observaciones.

---

# Evolución del dominio

Un dominio también puede evolucionar.

Ejemplos:

- aparición de nuevas técnicas;
- nuevas recetas;
- cambios culturales;
- nuevos ingredientes.

La colección deberá adaptarse.

---

# Cobertura

La cobertura expresa cuánto conocimiento relevante se encuentra representado.

No mide únicamente cantidad.

También mide representatividad.

---

## Dimensiones de cobertura

Una colección podrá medir cobertura sobre:

- documentos;
- conceptos;
- ingredientes;
- técnicas;
- recetas;
- relaciones;
- referencias;
- multimedia;
- observaciones;
- evidencia.

---

## Cobertura documental

Evalúa la documentación disponible.

---

## Cobertura semántica

Evalúa los conceptos existentes.

---

## Cobertura relacional

Evalúa las conexiones del dominio.

---

## Cobertura ontológica

Evalúa clases, propiedades y axiomas utilizados.

---

## Cobertura analítica

Evalúa la capacidad para responder preguntas relevantes.

---

# Madurez

La madurez representa el grado de desarrollo del dominio.

No depende únicamente del número de documentos.

---

## Niveles

Modelo recomendado.

```text
Nivel 1
Inicial
```

Dominio apenas documentado.

---

```text
Nivel 2
Emergente
```

Existe estructura básica.

---

```text
Nivel 3
Estructurada
```

El dominio posee organización coherente.

---

```text
Nivel 4
Consolidada
```

La mayor parte del conocimiento está integrada.

---

```text
Nivel 5
Referencia
```

Representa el estándar del SGCC.

---

# Indicadores de madurez

Ejemplos:

- cobertura;
- reutilización;
- estabilidad;
- relaciones;
- documentación;
- deuda;
- validaciones;
- inferencias;
- trazabilidad.

---

# Calidad

Toda colección deberá evaluarse continuamente.

---

## Calidad estructural

Comprueba:

- integridad;
- referencias;
- identificadores;
- consistencia.

---

## Calidad semántica

Comprueba:

- coherencia;
- precisión;
- ausencia de contradicciones.

---

## Calidad documental

Comprueba:

- documentación;
- ejemplos;
- referencias;
- claridad.

---

## Calidad relacional

Evalúa:

- densidad;
- reutilización;
- conexiones.

---

## Calidad operacional

Comprueba:

- consultas;
- rendimiento;
- reproducibilidad;
- materializaciones.

---

# Métricas

La colección podrá declarar métricas.

Ejemplos:

- número de miembros;
- número de criterios;
- profundidad;
- relaciones;
- reutilización;
- crecimiento;
- cambios mensuales;
- cobertura;
- deuda.

---

# Deuda de conocimiento

La deuda representa conocimiento pendiente.

No implica necesariamente errores.

---

## Tipos de deuda

---

### Documental

Falta documentación.

---

### Semántica

Faltan conceptos.

---

### Relacional

Faltan relaciones.

---

### Ontológica

Faltan clases o propiedades.

---

### Analítica

No pueden responderse determinadas preguntas.

---

### Técnica

Faltan automatizaciones.

---

# Registro de deuda

Cada elemento de deuda debería registrar:

- descripción;
- prioridad;
- impacto;
- responsable;
- fecha;
- estado.

---

# Priorización

Modelo recomendado:

```text
Crítica
Alta
Media
Baja
```

---

# Objetivos

Toda colección podrá definir objetivos.

Ejemplos:

- completar documentación;
- incorporar nuevas recetas;
- reducir deuda;
- mejorar cobertura;
- aumentar reutilización.

---

# KPIs

Ejemplos:

- cobertura > 80 %
- deuda crítica = 0
- trazabilidad = 100 %
- duplicidades = 0
- referencias rotas = 0

---

# Responsables

Cada colección deberá disponer de responsables claramente definidos.

---

## Propietario

Responsable del dominio.

---

## Mantenedor

Responsable operativo.

---

## Revisor semántico

Valida coherencia conceptual.

---

## Experto culinario

Valida el dominio gastronómico.

---

## Responsable técnico

Garantiza compatibilidad con el SGCC.

---

# Flujo de aprobación

Toda modificación significativa debería seguir un flujo.

```text
Propuesta

↓

Edición

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

# Validación

Las validaciones podrán clasificarse en:

---

## Estructural

Comprueba:

- formato;
- referencias;
- identificadores.

---

## Semántica

Comprueba:

- coherencia;
- contradicciones.

---

## Operacional

Comprueba:

- consultas;
- proyecciones;
- materialización.

---

## Editorial

Comprueba:

- claridad;
- documentación;
- ejemplos.

---

# Auditoría

Toda colección deberá ser auditable.

---

## Registro

Deberá conservar:

- autor;
- fecha;
- versión;
- cambios;
- revisiones;
- decisiones.

---

## Evidencias

Toda modificación relevante debería conservar evidencias.

---

# Publicación

Una colección publicada deberá incluir:

- versión;
- changelog;
- validaciones;
- documentación;
- fecha;
- responsable.

---

# Deprecación

Cuando una colección quede obsoleta deberá indicar:

- motivo;
- sustituta;
- periodo de transición.

---

# Sustitución

Ejemplo:

```text
Colección Cocina Asiática

↓

Reemplazada por

↓

Colecciones:
Japón
Corea
China
Vietnam
```

---

# Archivado

Una colección archivada:

- conserva identidad;
- conserva historial;
- conserva versiones;
- deja de evolucionar.

---

# Restauración

Una colección archivada podrá restaurarse.

La restauración deberá quedar registrada.

---

# Compatibilidad histórica

Las versiones anteriores deberán seguir siendo reproducibles.

---

# Automatización

La gobernanza deberá apoyarse en automatizaciones.

Ejemplos:

- validación;
- métricas;
- generación de informes;
- control de referencias;
- detección de duplicidades.

---

# Dashboards

Las colecciones podrán disponer de paneles.

Ejemplos:

- cobertura;
- deuda;
- evolución;
- crecimiento;
- actividad;
- reutilización.

---

# Calidad continua

La evaluación deberá ser continua.

No únicamente durante la publicación.

---

# Alertas

Ejemplos:

- deuda creciente;
- referencias rotas;
- cobertura decreciente;
- duplicidades.

---

# Indicadores globales

Ejemplos:

- cobertura media;
- deuda total;
- crecimiento mensual;
- reutilización;
- estabilidad.

---

# Riesgos

Ejemplos:

- dominios demasiado amplios;
- colecciones abandonadas;
- duplicidades;
- criterios ambiguos;
- crecimiento descontrolado.

---

# Antipatrones

Evitar:

- colecciones sin responsable;
- colecciones sin propósito;
- colecciones enormes;
- duplicar conocimiento;
- ausencia de métricas;
- ausencia de revisión;
- cambios sin trazabilidad;
- archivados sin documentación.

---

# Conformidad

Una colección será conforme cuando:

- respete esta especificación;
- supere las validaciones;
- mantenga trazabilidad;
- gestione correctamente su evolución;
- preserve su coherencia conceptual.

---

# Conclusión

La gobernanza convierte a las Colecciones de Conocimiento en entidades gestionables y sostenibles dentro del SGCC.

Gracias al ciclo de vida definido, las métricas de calidad, los modelos de cobertura y madurez, la gestión de deuda y los procesos de revisión, cada colección puede evolucionar de manera controlada sin perder estabilidad ni trazabilidad.

Esta gobernanza garantiza que las colecciones no sean simples agrupaciones de recursos, sino **activos estratégicos de conocimiento** capaces de reflejar fielmente la evolución de un dominio culinario y de servir como base para análisis, planificación e inteligencia artificial.

La Parte IV completará la especificación describiendo la integración operativa de las colecciones con el Knowledge Graph, los sistemas RAG, los agentes inteligentes, las APIs y el resto de la arquitectura del SGCC.

---

# Parte IV — Integración operativa e inteligencia

---

# Introducción

Las partes anteriores han definido:

- los fundamentos de las Colecciones de Conocimiento;
- su modelo conceptual;
- su metamodelo;
- su ciclo de vida;
- sus mecanismos de calidad y gobernanza.

Esta cuarta parte describe cómo las colecciones se integran operativamente con el resto del Sistema de Gestión del Conocimiento Culinario.

Una colección no debe permanecer como una definición puramente documental.

Debe poder convertirse en una unidad operativa capaz de:

- resolverse;
- consultarse;
- proyectarse;
- materializarse;
- indexarse;
- publicarse;
- analizarse;
- alimentar sistemas RAG;
- proporcionar contexto a agentes inteligentes;
- integrarse con APIs y aplicaciones.

La colección actúa así como un puente entre el conocimiento gobernado del SGCC y sus capacidades de explotación.

---

# Objetivos

Esta parte persigue los siguientes objetivos:

- definir la integración de las colecciones con el Knowledge Graph;
- establecer el modelo de resolución de miembros;
- regular las proyecciones documentales y semánticas;
- definir vistas y subgrafos;
- establecer mecanismos de materialización;
- integrar colecciones con búsqueda y recuperación;
- preparar índices RAG;
- proporcionar contexto a agentes inteligentes;
- definir APIs y contratos operativos;
- establecer mecanismos de automatización;
- regular rendimiento, seguridad y observabilidad;
- definir perfiles de implementación;
- establecer criterios de conformidad operativa.

---

# Principios de integración

Toda integración operativa deberá respetar los siguientes principios.

---

## Fuente canónica

La colección no sustituirá las fuentes de conocimiento originales.

Los documentos, componentes, relaciones, entidades ontológicas y nodos del Knowledge Graph seguirán siendo canónicos en sus respectivos niveles.

---

## Derivación explícita

Toda vista, subgrafo, índice o contexto generado desde una colección deberá identificarse como una representación derivada.

---

## Reproducibilidad

Toda representación derivada deberá poder reconstruirse a partir de:

- la definición de la colección;
- sus parámetros;
- la versión de las fuentes;
- el motor utilizado;
- la fecha de ejecución.

---

## Trazabilidad

Deberá poder conocerse:

- qué colección produjo un resultado;
- qué versión se utilizó;
- qué criterios se ejecutaron;
- qué fuentes participaron;
- qué transformaciones se aplicaron.

---

## Separación de responsabilidades

La colección define el dominio.

Los motores operativos resuelven, transforman, indexan o publican dicho dominio.

---

## Independencia tecnológica

La semántica de una colección no dependerá de:

- Neo4j;
- RDF;
- PostgreSQL;
- Elasticsearch;
- un motor vectorial concreto;
- una implementación RAG determinada.

---

## Seguridad por herencia

Una colección no podrá ampliar los permisos de acceso de sus miembros.

El acceso efectivo será como máximo el permitido por las fuentes originales.

---

## Evaluación continua

Toda integración deberá ser verificable mediante:

- métricas;
- validaciones;
- logs;
- pruebas;
- alertas.

---

# Arquitectura operativa

La integración operativa de una colección puede representarse mediante el siguiente flujo:

```text
Definición de colección
          │
          ▼
Validación
          │
          ▼
Resolución de miembros
          │
          ▼
Enriquecimiento contextual
          │
          ▼
Proyección
          │
          ├── Vista documental
          ├── Subgrafo
          ├── Vista analítica
          ├── Índice de búsqueda
          ├── Índice RAG
          └── Contexto de agente
          │
          ▼
Publicación y consumo
```

---

# Componentes operativos

La arquitectura podrá dividirse en los siguientes componentes.

```text
Collection Registry
Collection Resolver
Collection Validator
Collection Projector
Collection Materializer
Collection Indexer
Collection API
Collection Metrics
Collection Audit
```

---

# Registro de colecciones

El `Collection Registry` constituye el catálogo oficial de colecciones.

Deberá permitir:

- localizar colecciones;
- resolver identificadores;
- consultar versiones;
- conocer estados;
- localizar responsables;
- obtener dependencias;
- descubrir proyecciones;
- consultar sustituciones.

---

## Responsabilidades del registro

El registro deberá conservar al menos:

- identificador;
- título;
- versión activa;
- estado;
- tipo;
- responsable;
- ubicación de la definición;
- fecha de actualización;
- dependencias;
- perfiles disponibles;
- proyecciones publicadas.

---

## Registro lógico y registro físico

El registro lógico representa el catálogo conceptual.

Su implementación física podrá residir en:

- archivos Markdown;
- archivos YAML;
- una base de datos;
- un catálogo RDF;
- un servicio de metadatos;
- el propio Knowledge Graph.

---

## Descubrimiento

El registro deberá permitir buscar colecciones mediante:

- identificador;
- nombre;
- alias;
- tipo;
- contexto;
- estado;
- responsable;
- dominio;
- etiquetas;
- relaciones.

---

# Resolución de colecciones

Resolver una colección significa determinar su estado operativo en un momento concreto.

El proceso incluye:

- cargar la definición;
- validar la estructura;
- resolver dependencias;
- evaluar criterios;
- aplicar inclusiones;
- aplicar exclusiones;
- resolver conflictos;
- calcular miembros;
- generar explicaciones;
- producir métricas.

---

# Entrada del proceso de resolución

El resolver podrá recibir:

- identificador de colección;
- versión;
- perfil;
- parámetros;
- instante temporal;
- identidad del usuario;
- permisos;
- versión del Knowledge Graph;
- modo de ejecución.

---

## Ejemplo conceptual

```yaml
collection: COL-0001
version: 2.0.0
profile: traditional
knowledge_graph_version: 1.4.0

parameters:
  language: es
  include_inferred: true
  graph_depth: 2
```

---

# Salida del proceso de resolución

El resultado deberá incluir:

- colección;
- versión;
- miembros directos;
- miembros inferidos;
- miembros auxiliares;
- exclusiones;
- conflictos;
- explicaciones;
- métricas;
- advertencias;
- procedencia;
- hash de resolución.

---

## Ejemplo conceptual

```yaml
resolution:
  collection: COL-0001
  version: 2.0.0
  resolved_at: 2026-07-31T14:00:00+02:00
  graph_version: 1.4.0

  members:
    explicit: 12
    calculated: 84
    inferred: 21
    auxiliary: 17
    total: 134

  exclusions: 6
  conflicts: 1
  warnings: 2

  hash: sha256:...
```

---

# Orden de resolución

El orden recomendado será:

```text
1. Cargar definición
2. Validar esquema
3. Resolver dependencias
4. Resolver colecciones base
5. Evaluar criterios de inclusión
6. Aplicar inclusiones explícitas
7. Evaluar criterios de exclusión
8. Aplicar exclusiones explícitas
9. Resolver prioridades
10. Aplicar permisos
11. Expandir contexto
12. Calcular métricas
13. Generar explicaciones
14. Producir snapshot
```

---

# Modos de resolución

El resolver podrá operar en distintos modos.

---

## Resolución completa

Recalcula todos los miembros y proyecciones.

---

## Resolución incremental

Procesa únicamente los cambios desde la última resolución válida.

---

## Resolución preliminar

Genera resultados provisionales para revisión.

---

## Resolución estricta

Falla ante cualquier error normativo.

---

## Resolución tolerante

Continúa con advertencias cuando los errores no comprometen la integridad esencial.

---

## Resolución histórica

Reconstruye la colección sobre una versión pasada del conocimiento.

---

## Resolución contextual

Aplica parámetros de usuario, permisos, tiempo o entorno.

---

# Determinismo

Siempre que las mismas entradas y versiones estén disponibles, la resolución debería producir el mismo resultado.

Las fuentes no deterministas deberán declararse.

Ejemplos:

- modelos generativos;
- clasificadores probabilísticos;
- fuentes externas variables;
- recomendaciones personalizadas.

---

## Semilla de ejecución

Cuando intervengan procesos probabilísticos, podrá registrarse una semilla.

```yaml
execution:
  deterministic: false
  seed: 483920
```

---

# Explicación de pertenencia

Toda pertenencia calculada o inferida deberá poder explicarse.

Ejemplo:

```text
REC-0047 pertenece a COL-0001 porque:

1. Es una instancia de Receta.
2. Usa el ingrediente ING-0008 Miso.
3. ING-0008 está asociado a Japón.
4. La receta aplica la técnica TEC-0012.
5. No cumple ningún criterio de exclusión.
```

---

## Explicación mínima

Deberá incluir:

- criterio aplicado;
- evidencia;
- fuente;
- confianza;
- prioridad;
- resultado.

---

## Explicación compuesta

Cuando una pertenencia dependa de varios criterios, deberá conservarse el árbol lógico.

```text
AND
├── tipo = receta
├── pertenece_a_cocina = japonesa
└── NOT fusion_sin_evidencia
```

---

# Integración con documentos

Las colecciones podrán generar una vista documental.

Esta vista incluirá referencias a:

- documentos completos;
- secciones;
- componentes;
- fragmentos;
- anexos;
- tablas;
- recursos multimedia.

---

## Vista documental

La vista documental deberá conservar:

- identificador del documento;
- título;
- tipo;
- versión;
- estado;
- secciones relevantes;
- papel dentro de la colección;
- relevancia;
- procedencia.

---

## Fragmentos documentales

Una colección podrá referenciar secciones concretas.

Ejemplo:

```yaml
document_members:
  - document: REC-0009
    fragments:
      - ingredientes
      - tecnica
      - contexto_cultural
```

---

## Componentes reutilizables

Cuando el SGCC disponga de componentes estructurados, la colección podrá incluir componentes sin incorporar el documento completo.

Ejemplos:

- lista de ingredientes;
- técnica;
- tabla nutricional;
- notas de seguridad;
- procedimiento.

---

## Navegación bidireccional

Deberá ser posible navegar:

```text
Colección → Documento
```

y:

```text
Documento → Colecciones
```

---

## No alteración documental

La inclusión de un documento en una colección no modificará:

- su identidad;
- su contenido;
- su ruta;
- su versión;
- su clasificación principal.

---

# Integración con componentes

Las colecciones podrán operar a nivel de componente.

Esto permite crear vistas más precisas.

Ejemplo:

Una colección sobre fermentación puede incluir:

- la sección de fermentación de una receta;
- una técnica independiente;
- una observación microbiológica;
- una advertencia de seguridad.

No será necesario incluir todos los documentos completos.

---

## Pertenencia parcial

La pertenencia parcial deberá declararse explícitamente.

```yaml
member:
  document: REC-0021
  component: fermentation_step
```

---

## Contexto del componente

Cuando un componente se extraiga de su documento, deberá conservar:

- documento origen;
- posición;
- contexto mínimo;
- versión;
- relaciones necesarias.

---

# Integración con la ontología

Las colecciones utilizarán la ontología para:

- identificar tipos;
- interpretar propiedades;
- resolver jerarquías;
- aplicar restricciones;
- ejecutar inferencias;
- validar criterios.

---

## Dependencia semántica

Toda colección semántica deberá declarar los módulos ontológicos que utiliza.

Ejemplo:

```yaml
ontology:
  modules:
    - ingredients
    - recipes
    - techniques
    - cuisines
```

---

## Expansión por jerarquía

Un criterio podrá incluir subclases.

Ejemplo:

```text
Incluir IngredienteFermentado
```

podrá incluir:

```text
Miso
Shoyu
Natto
Vinagre de arroz fermentado
```

si dichas entidades pertenecen a clases derivadas.

---

## Restricción por clase

Una colección podrá limitar sus miembros a determinadas clases.

```yaml
allowed_classes:
  - Recipe
  - Ingredient
  - Technique
```

---

## Restricción por propiedad

También podrá limitar las propiedades utilizadas en sus proyecciones.

---

## Cambios ontológicos

Si una actualización ontológica afecta a una colección, el sistema deberá:

- detectar el impacto;
- invalidar resoluciones afectadas;
- ejecutar validaciones;
- generar advertencias;
- solicitar revisión si es necesario.

---

# Integración con el Knowledge Graph

El Knowledge Graph constituye la principal fuente semántica para resolver colecciones dinámicas.

Una colección podrá utilizarlo para:

- localizar entidades;
- recorrer relaciones;
- ejecutar filtros;
- aplicar reglas;
- obtener inferencias;
- proyectar subgrafos;
- calcular métricas.

---

# Colección como vista del grafo

Conceptualmente:

```text
Knowledge Graph completo
          │
          ▼
Criterios de colección
          │
          ▼
Selección de nodos
          │
          ▼
Selección de relaciones
          │
          ▼
Expansión contextual
          │
          ▼
Subgrafo de colección
```

---

# Nodos del subgrafo

El subgrafo podrá contener:

- miembros principales;
- miembros secundarios;
- nodos auxiliares;
- nodos de contexto;
- nodos de procedencia;
- nodos inferidos.

---

## Miembro principal

Entidad que cumple directamente los criterios de pertenencia.

---

## Miembro secundario

Entidad relevante para interpretar un miembro principal.

---

## Nodo auxiliar

Nodo necesario para conservar una relación o explicación.

---

## Nodo contextual

Aporta contexto geográfico, temporal, cultural o técnico.

---

## Nodo de procedencia

Representa fuentes, autores, actividades o evidencias.

---

# Aristas del subgrafo

La colección podrá seleccionar relaciones según:

- predicado;
- dirección;
- profundidad;
- confianza;
- procedencia;
- estado;
- temporalidad.

---

## Aristas internas

Conectan dos miembros de la colección.

---

## Aristas de frontera

Conectan un miembro con una entidad externa.

Podrán conservarse cuando resulten necesarias para comprender el dominio.

---

## Política de frontera

Opciones recomendadas:

```text
closed
```

Solo relaciones internas.

```text
contextual
```

Incluye relaciones externas relevantes.

```text
expanded
```

Incluye vecinos hasta una profundidad determinada.

```text
custom
```

Aplica reglas específicas.

---

# Expansión del subgrafo

La expansión podrá limitarse mediante:

- profundidad máxima;
- predicados permitidos;
- tipos de nodo;
- confianza mínima;
- número máximo de vecinos;
- presupuesto de coste.

---

## Ejemplo

```yaml
graph_projection:
  boundary_policy: contextual
  max_depth: 2
  max_nodes: 5000
  min_confidence: 0.70

  allowed_predicates:
    - uses_ingredient
    - applies_technique
    - belongs_to_cuisine
    - originates_from
```

---

# Subgrafo inducido

Un subgrafo inducido incluirá todas las relaciones existentes entre los miembros seleccionados, dentro del conjunto de predicados autorizados.

---

# Subgrafo filtrado

Incluye únicamente relaciones que cumplen reglas adicionales.

---

# Subgrafo explicativo

Está optimizado para justificar pertenencias e inferencias.

---

# Subgrafo operativo

Está optimizado para una aplicación concreta.

Ejemplos:

- recomendación;
- búsqueda;
- RAG;
- visualización;
- análisis.

---

# Named Graphs

Cuando se utilice RDF, cada colección o snapshot podrá representarse como un grafo nombrado.

Ejemplo conceptual:

```turtle
GRAPH <https://novacoquinaria.org/collection/COL-0001/snapshot/2026-07-31> {
    ...
}
```

Esto permitirá:

- separar contextos;
- conservar procedencia;
- versionar;
- gestionar permisos;
- comparar snapshots.

---

# Representación en grafos de propiedades

En Neo4j u otros grafos de propiedades, una colección podrá modelarse como nodo.

Ejemplo conceptual:

```text
(:Collection {
  id: "COL-0001",
  title: "Cocina japonesa",
  version: "2.0.0"
})
```

Las pertenencias podrán representarse mediante relaciones:

```text
(:Collection)-[:HAS_MEMBER]->(:Recipe)
```

---

## Propiedades de pertenencia

La relación podrá incluir:

- role;
- relevance;
- confidence;
- status;
- source;
- valid_from;
- valid_until;
- explanation_id.

---

# Integración con relaciones enriquecidas

Cuando las relaciones del SGCC posean:

- confianza;
- contexto;
- procedencia;
- temporalidad;
- evidencia;

la colección deberá conservar dichos atributos.

No deberá reducir una relación enriquecida a un enlace simple si esa reducción provoca pérdida semántica.

---

# Proyección documental

Una proyección documental organiza los documentos de una colección para su consulta.

Podrá generar:

- índice temático;
- catálogo;
- navegación;
- dossier;
- sitio web;
- documentación exportada.

---

## Ordenación

Los documentos podrán ordenarse por:

- relevancia;
- tipo;
- fecha;
- título;
- madurez;
- dependencia;
- recorrido pedagógico;
- jerarquía semántica.

---

## Agrupación

Podrán agruparse por:

- recetas;
- ingredientes;
- técnicas;
- regiones;
- niveles;
- estados;
- perfiles.

---

## Generación de índice

Ejemplo:

```text
Cocina japonesa

1. Fundamentos
2. Ingredientes
3. Técnicas
4. Preparaciones base
5. Recetas
6. Utensilios
7. Contexto cultural
8. Referencias
```

---

# Proyección semántica

La proyección semántica presentará:

- clases relevantes;
- propiedades;
- individuos;
- relaciones;
- restricciones;
- inferencias.

Podrá utilizarse para:

- documentación;
- navegación;
- depuración;
- análisis;
- exportación.

---

# Proyección analítica

La colección podrá generar una vista de métricas.

Ejemplos:

- número de miembros;
- distribución por tipo;
- densidad relacional;
- cobertura;
- deuda;
- evolución;
- fuentes;
- confianza media;
- miembros huérfanos;
- duplicidades.

---

## Ejemplo conceptual

```yaml
analytics:
  total_members: 134

  by_type:
    recipes: 42
    ingredients: 31
    techniques: 18
    documents: 27
    others: 16

  coverage: 0.78
  maturity: structured
  orphan_members: 3
  critical_debt: 2
```

---

# Proyección visual

Las colecciones podrán alimentar visualizaciones como:

- grafos;
- mapas;
- líneas temporales;
- matrices;
- árboles;
- diagramas de dependencias;
- paneles.

---

## Visualización del grafo

La vista deberá diferenciar:

- miembros principales;
- nodos auxiliares;
- inferencias;
- relaciones de frontera;
- entidades externas.

---

## Navegación progresiva

La visualización debería permitir:

- expandir nodos;
- filtrar tipos;
- cambiar profundidad;
- ocultar relaciones;
- consultar evidencia;
- abrir documentos.

---

# Materialización

Materializar una colección significa persistir una resolución o proyección derivada.

La materialización podrá incluir:

- lista de miembros;
- subgrafo;
- documentos procesados;
- chunks;
- embeddings;
- métricas;
- vistas generadas.

---

# Objetivos de la materialización

La materialización podrá utilizarse para:

- rendimiento;
- reproducibilidad;
- publicación;
- auditoría;
- comparación;
- análisis;
- indexación;
- operación desconectada.

---

# Tipos de materialización

---

## Materialización completa

Persistencia de toda la colección.

---

## Materialización parcial

Solo una proyección o perfil.

---

## Materialización incremental

Actualiza únicamente cambios.

---

## Materialización temporal

Se conserva durante un periodo limitado.

---

## Materialización inmutable

Se publica como snapshot histórico.

---

# Metadatos de materialización

Toda materialización deberá registrar:

```yaml
materialization:
  id: MAT-COL-0001-20260731-001
  collection: COL-0001
  collection_version: 2.0.0
  graph_version: 1.4.0
  generated_at: 2026-07-31T14:00:00+02:00
  generator_version: 1.2.0
  status: valid
  hash: sha256:...
```

---

# Invalidación

Una materialización podrá quedar invalidada por:

- cambio en la definición;
- cambio en miembros;
- actualización ontológica;
- actualización del Knowledge Graph;
- cambio de permisos;
- cambio en dependencias;
- error detectado;
- expiración temporal.

---

## Estado de materialización

Valores recomendados:

```text
pending
generating
valid
stale
invalid
failed
archived
```

---

# Estrategias de actualización

---

## Actualización bajo demanda

Se recalcula al solicitarla.

---

## Actualización programada

Se recalcula periódicamente.

---

## Actualización por eventos

Se recalcula cuando cambian elementos relevantes.

---

## Actualización híbrida

Combina eventos, programación y demanda.

---

# Detección de impacto

El sistema deberá detectar qué colecciones se ven afectadas por un cambio.

Ejemplos:

```text
Cambio en ING-0008
        ↓
Colecciones que incluyen ING-0008
        ↓
Colecciones con criterios relacionados
        ↓
Colecciones derivadas
        ↓
Índices y vistas dependientes
```

---

## Grafo de dependencias

Las dependencias entre colecciones y artefactos deberán representarse explícitamente.

```text
Documento
   ↓
Entidad
   ↓
Colección
   ↓
Subgrafo
   ↓
Índice RAG
   ↓
Agente
```

---

# Integración con búsqueda

Las colecciones podrán utilizarse como ámbitos de búsqueda.

Ejemplo:

```text
Buscar "fermentación"
dentro de
"Cocina japonesa"
```

---

# Búsqueda filtrada por colección

La colección podrá actuar como filtro para:

- búsqueda textual;
- búsqueda semántica;
- búsqueda vectorial;
- búsqueda por grafo;
- búsqueda híbrida.

---

## Búsqueda textual

Opera sobre:

- títulos;
- contenido;
- metadatos;
- etiquetas;
- alias.

---

## Búsqueda semántica

Utiliza:

- ontología;
- equivalencias;
- jerarquías;
- relaciones;
- contexto.

---

## Búsqueda vectorial

Utiliza embeddings para localizar contenido semánticamente próximo.

---

## Búsqueda por grafo

Utiliza relaciones y caminos.

---

## Búsqueda híbrida

Combina varios mecanismos.

Ejemplo:

```text
Resultados =
  búsqueda textual
  +
  similitud vectorial
  +
  proximidad en el grafo
  +
  filtros de colección
```

---

# Ranking dentro de una colección

La ordenación de resultados podrá considerar:

- relevancia textual;
- similitud semántica;
- pertenencia directa;
- importancia dentro de la colección;
- confianza;
- calidad;
- actualidad;
- distancia en el grafo;
- perfil de usuario.

---

## Ejemplo conceptual

```text
score =
  0.30 × text_score
+ 0.30 × vector_score
+ 0.20 × graph_score
+ 0.10 × collection_relevance
+ 0.10 × quality_score
```

Los pesos deberán ser configurables y evaluados.

---

# Integración con RAG

Las colecciones constituyen una unidad natural para delimitar el conocimiento recuperable por un sistema RAG.

Una colección podrá definir:

- corpus;
- filtros;
- chunks;
- metadatos;
- embeddings;
- reglas de recuperación;
- fuentes;
- permisos;
- contexto semántico.

---

# Colección como corpus RAG

Conceptualmente:

```text
Colección
     │
     ▼
Documentos y componentes
     │
     ▼
Normalización
     │
     ▼
Chunking
     │
     ▼
Enriquecimiento semántico
     │
     ▼
Embeddings
     │
     ▼
Índice de recuperación
```

---

# Selección del corpus

No todos los miembros de una colección deberán incorporarse necesariamente al índice RAG.

Podrán aplicarse filtros por:

- tipo;
- estado;
- calidad;
- idioma;
- relevancia;
- licencia;
- permisos;
- madurez;
- confianza.

---

## Ejemplo

```yaml
rag_projection:
  include_types:
    - recipe
    - technique
    - ingredient

  allowed_status:
    - stable
    - reference

  minimum_quality: 0.75
  include_drafts: false
```

---

# Chunking orientado a colecciones

El chunking deberá respetar la estructura del conocimiento.

Posibles unidades:

- documento;
- sección;
- componente;
- procedimiento;
- paso;
- tabla;
- observación;
- definición;
- relación explicada.

---

## Chunk semántico

Cada chunk deberá conservar:

- identificador;
- documento origen;
- colección;
- sección;
- tipo;
- entidades;
- relaciones;
- versión;
- permisos;
- contexto.

---

## Ejemplo

```yaml
chunk:
  id: CHK-REC-0009-TECHNIQUE-001
  source: REC-0009
  collection: COL-0001
  component: technique
  language: es
  version: 1.2.0

  entities:
    - TEC-0014
    - ING-0008
```

---

# Enriquecimiento de chunks

Los chunks podrán enriquecerse con:

- entidades reconocidas;
- clases ontológicas;
- relaciones;
- sinónimos;
- contextos;
- etiquetas controladas;
- preguntas potenciales;
- resumen;
- nivel de confianza.

---

# Embeddings

Una colección podrá definir su política de embeddings.

Deberá registrar:

- modelo;
- versión;
- dimensiones;
- fecha;
- idioma;
- estrategia de normalización;
- fuente;
- hash del contenido.

---

## Ejemplo

```yaml
embedding:
  model: text-embedding-model
  model_version: 3
  dimensions: 1536
  generated_at: 2026-07-31
```

---

## Reembeddings

Será necesario regenerar embeddings cuando:

- cambie el contenido;
- cambie el modelo;
- cambie el chunking;
- cambie la normalización;
- se detecten errores;
- expire la política de actualización.

---

# Índice RAG de colección

Un índice RAG deberá conservar:

- colección;
- versión;
- corpus;
- chunks;
- embeddings;
- metadatos;
- filtros;
- permisos;
- configuración de recuperación;
- métricas de evaluación.

---

## Estado del índice

Valores recomendados:

```text
planned
building
ready
stale
invalid
failed
archived
```

---

# Recuperación dentro de una colección

El proceso podrá incluir:

```text
Pregunta
   ↓
Análisis de intención
   ↓
Selección de colección
   ↓
Expansión semántica
   ↓
Recuperación híbrida
   ↓
Reordenación
   ↓
Construcción de contexto
   ↓
Generación de respuesta
```

---

# Selección de colección para RAG

La colección podrá:

- especificarse explícitamente;
- inferirse desde la pregunta;
- seleccionarse por perfil;
- combinarse con otras colecciones.

---

## Recuperación multicolección

Podrán consultarse varias colecciones.

Ejemplo:

```text
Cocina japonesa
INTERSECT
Recetas vegetarianas
INTERSECT
Despensa disponible
```

---

## Control de solapamiento

Cuando varias colecciones recuperen el mismo chunk, el sistema deberá deduplicarlo y conservar todas sus procedencias.

---

# Recuperación guiada por el grafo

La recuperación podrá expandirse utilizando el Knowledge Graph.

Ejemplo:

```text
Pregunta: Sustitutos del mirin

Entidad detectada: Mirin
        ↓
Relaciones:
  sustituible_por
  similar_a
  aporta_sabor
  usado_en
        ↓
Documentos relevantes
```

---

# Construcción de contexto

El contexto final podrá combinar:

- chunks;
- entidades;
- relaciones;
- definiciones;
- reglas;
- evidencias;
- advertencias;
- procedencia.

---

## Presupuesto de contexto

La colección podrá establecer límites.

```yaml
context_policy:
  max_tokens: 12000
  max_chunks: 15
  max_graph_paths: 8
```

---

# Priorización del contexto

Orden recomendado:

1. conocimiento canónico;
2. contenido de alta calidad;
3. evidencia directa;
4. relaciones explicativas;
5. contenido complementario;
6. inferencias;
7. fuentes externas.

---

# Citación y procedencia en RAG

Toda respuesta generada deberá poder vincularse con:

- colección;
- documentos;
- chunks;
- entidades;
- relaciones;
- versión;
- fecha.

---

# Evaluación RAG por colección

Las colecciones permitirán evaluar el rendimiento por dominio.

Métricas posibles:

- precision@k;
- recall@k;
- MRR;
- nDCG;
- groundedness;
- fidelidad;
- cobertura de respuesta;
- tasa de abstención;
- uso de fuentes;
- latencia.

---

# Conjuntos de evaluación

Cada colección podrá disponer de:

- preguntas frecuentes;
- preguntas complejas;
- casos límite;
- preguntas sin respuesta;
- preguntas adversariales;
- respuestas de referencia.

---

## Ejemplo conceptual

```yaml
evaluation_set:
  collection: COL-0001

  questions:
    - id: QA-0001
      question: ¿Qué ingredientes básicos se utilizan en una sopa de miso?
      expected_entities:
        - ING-0008
      answerable: true
```

---

# Integración con agentes inteligentes

Las colecciones podrán proporcionar dominios especializados a agentes.

Un agente podrá utilizar una colección para definir:

- conocimiento disponible;
- herramientas;
- reglas;
- permisos;
- objetivos;
- vocabulario;
- memoria;
- límites.

---

# Colección como contexto de agente

Conceptualmente:

```text
Colección
    │
    ├── Conocimiento
    ├── Ontología
    ├── Subgrafo
    ├── Índice RAG
    ├── Reglas
    ├── Herramientas
    ├── Permisos
    └── Objetivos
          │
          ▼
      Agente especializado
```

---

# Tipos de agentes relacionados

Ejemplos:

- agente de recetas;
- agente de planificación;
- agente de sustituciones;
- agente nutricional;
- agente de seguridad alimentaria;
- agente documental;
- agente de calidad;
- agente de investigación culinaria.

---

# Perfil de agente

Una colección podrá definir un perfil operativo para agentes.

```yaml
agent_profile:
  role: culinary_research_assistant

  capabilities:
    - semantic_search
    - graph_navigation
    - document_retrieval

  restrictions:
    - no_modify_canonical_content
    - cite_sources
    - respect_permissions
```

---

# Herramientas disponibles

Un agente podrá recibir acceso a herramientas asociadas a la colección.

Ejemplos:

- búsqueda;
- consulta SPARQL;
- consulta Cypher;
- lectura documental;
- calculadora culinaria;
- conversión de unidades;
- generador de menús;
- validador de recetas.

---

# Principio de mínimo privilegio

El agente solo deberá acceder a:

- colecciones autorizadas;
- datos permitidos;
- herramientas necesarias;
- operaciones compatibles con su función.

---

# Memoria de agente

La memoria podrá separarse en:

- memoria de sesión;
- memoria del usuario;
- memoria de dominio;
- memoria de tareas;
- memoria derivada.

La memoria no deberá modificar automáticamente el conocimiento canónico.

---

## Promoción a conocimiento

Una observación generada por un agente solo podrá incorporarse al SGCC mediante un flujo de revisión.

```text
Observación del agente
        ↓
Propuesta
        ↓
Validación
        ↓
Revisión humana
        ↓
Conocimiento aceptado
```

---

# Planificación con colecciones

Un agente podrá utilizar colecciones como unidades de planificación.

Ejemplo:

```text
Objetivo:
Completar la colección de fermentaciones japonesas

Plan:
1. Detectar deuda documental
2. Localizar entidades huérfanas
3. Proponer relaciones
4. Crear borradores
5. Solicitar revisión
```

---

# Agentes multicolección

Un agente podrá combinar dominios.

Ejemplo:

```text
Colección de despensa
+
Colección de recetas rápidas
+
Colección sin gluten
```

La combinación deberá respetar:

- permisos;
- conflictos;
- prioridades;
- procedencia.

---

# Agentes y explicabilidad

Todo resultado del agente debería poder indicar:

- qué colecciones utilizó;
- qué fuentes consultó;
- qué reglas aplicó;
- qué inferencias realizó;
- qué incertidumbres existen.

---

# Integración con aplicaciones

Las colecciones podrán alimentar aplicaciones como:

- catálogos;
- buscadores;
- asistentes;
- paneles;
- planificadores;
- aplicaciones móviles;
- sistemas de recomendación;
- herramientas editoriales.

---

# Casos de uso

---

## Exploración temática

Un usuario navega por una colección y descubre:

- documentos;
- recetas;
- técnicas;
- ingredientes;
- relaciones.

---

## Planificación editorial

Un mantenedor consulta:

- cobertura;
- deuda;
- objetivos;
- prioridades.

---

## Generación de un dossier

La colección genera una publicación temática.

---

## Búsqueda especializada

El usuario restringe la búsqueda a un dominio.

---

## Asistente culinario

Un agente responde utilizando una colección concreta.

---

## Comparación entre dominios

El sistema compara:

- cocina japonesa;
- cocina coreana;
- cocina china.

---

# APIs de colecciones

Las colecciones podrán exponerse mediante APIs.

La API deberá separar:

- metadatos;
- definición;
- resolución;
- miembros;
- proyecciones;
- métricas;
- historial.

---

# Recursos principales

Ejemplos conceptuales:

```text
/collections
/collections/{id}
/collections/{id}/versions
/collections/{id}/members
/collections/{id}/resolve
/collections/{id}/graph
/collections/{id}/documents
/collections/{id}/metrics
/collections/{id}/debt
/collections/{id}/history
```

---

# Operaciones de lectura

---

## Listar colecciones

```http
GET /collections
```

Filtros posibles:

- type;
- status;
- maturity;
- owner;
- context;
- updated_since.

---

## Obtener colección

```http
GET /collections/COL-0001
```

---

## Obtener miembros

```http
GET /collections/COL-0001/members
```

---

## Resolver colección

```http
POST /collections/COL-0001/resolve
```

---

## Obtener subgrafo

```http
GET /collections/COL-0001/graph
```

---

## Obtener métricas

```http
GET /collections/COL-0001/metrics
```

---

# Operaciones de escritura

Podrán incluir:

- crear propuesta;
- actualizar borrador;
- añadir miembro;
- excluir miembro;
- proponer criterio;
- solicitar revisión;
- aprobar;
- publicar;
- archivar.

Toda operación de escritura deberá estar autorizada y auditada.

---

# Contrato de respuesta

Ejemplo conceptual:

```json
{
  "id": "COL-0001",
  "title": "Cocina japonesa",
  "version": "2.0.0",
  "status": "en_consolidacion",
  "links": {
    "members": "/collections/COL-0001/members",
    "graph": "/collections/COL-0001/graph",
    "metrics": "/collections/COL-0001/metrics"
  }
}
```

---

# Paginación

Los recursos extensos deberán paginarse.

Ejemplos:

- miembros;
- historial;
- deuda;
- relaciones;
- resultados de consulta.

---

# Filtrado

La API podrá permitir filtros por:

- tipo;
- papel;
- relevancia;
- confianza;
- estado;
- fecha;
- procedencia.

---

# Ordenación

Podrá ordenar por:

- título;
- relevancia;
- fecha;
- confianza;
- calidad;
- tipo.

---

# Expansión de recursos

Podrá permitirse solicitar información relacionada.

Ejemplo:

```text
?include=members,metrics,dependencies
```

---

# GraphQL

GraphQL podrá utilizarse para consultas flexibles.

Ejemplo conceptual:

```graphql
query {
  collection(id: "COL-0001") {
    title
    version
    members(type: "recipe") {
      id
      title
      relevance
    }
  }
}
```

---

# API semántica

Podrá exponerse una interfaz semántica mediante:

- SPARQL endpoint;
- JSON-LD;
- RDF;
- content negotiation.

---

# Negociación de contenido

Una colección podrá publicarse como:

- Markdown;
- HTML;
- JSON;
- JSON-LD;
- Turtle;
- RDF/XML;
- CSV;
- GraphML.

---

# Exportación

Las colecciones podrán exportarse para:

- interoperabilidad;
- análisis;
- publicación;
- copia de seguridad;
- migración;
- entrenamiento;
- evaluación.

---

## Exportación de definición

Incluye el metamodelo y las reglas.

---

## Exportación de miembros

Incluye referencias a miembros resueltos.

---

## Exportación de subgrafo

Incluye nodos y relaciones.

---

## Exportación de corpus

Incluye documentos o chunks autorizados.

---

## Exportación analítica

Incluye métricas y series históricas.

---

# Importación

La importación deberá diferenciar:

- definición de colección;
- referencias;
- resultados materializados;
- fuentes externas.

No se deberán importar resultados derivados como si fueran conocimiento canónico.

---

# Validación de importación

Deberá comprobar:

- formato;
- identificadores;
- versiones;
- dependencias;
- permisos;
- procedencia;
- compatibilidad semántica.

---

# Interoperabilidad

Las colecciones podrán alinearse con estándares externos.

Ejemplos:

- SKOS Collections;
- RDF;
- OWL;
- PROV-O;
- DCAT;
- Dublin Core;
- Schema.org;
- SHACL.

---

# SKOS Collections

`skos:Collection` podrá utilizarse para representar agrupaciones simples.

Sin embargo, el modelo del SGCC es más rico.

Incluye:

- criterios dinámicos;
- versiones;
- deuda;
- objetivos;
- perfiles;
- proyecciones;
- gobernanza.

Por ello será necesario extender o complementar SKOS.

---

# JSON-LD

JSON-LD permitirá publicar colecciones como recursos enlazados.

Ejemplo conceptual:

```json
{
  "@context": "https://novacoquinaria.org/context/collection.jsonld",
  "@id": "https://novacoquinaria.org/collection/COL-0001",
  "@type": "KnowledgeCollection",
  "title": "Cocina japonesa",
  "version": "2.0.0"
}
```

---

# SHACL

SHACL podrá utilizarse para validar:

- campos obligatorios;
- cardinalidades;
- tipos;
- relaciones;
- identificadores;
- estados;
- dependencias;
- pertenencias.

---

# Automatización

El ciclo operativo de las colecciones deberá automatizarse progresivamente.

---

# Pipeline operativo

Modelo recomendado:

```text
Cambio en fuente
      │
      ▼
Detección de impacto
      │
      ▼
Validación de colección
      │
      ▼
Resolución incremental
      │
      ▼
Actualización de subgrafo
      │
      ▼
Actualización de índices
      │
      ▼
Cálculo de métricas
      │
      ▼
Publicación
      │
      ▼
Notificación
```

---

# Disparadores

El pipeline podrá activarse por:

- commit;
- merge;
- publicación;
- cambio ontológico;
- cambio documental;
- actualización programada;
- solicitud manual;
- evento externo.

---

# Trabajos automáticos

Ejemplos:

- validar colecciones;
- detectar referencias rotas;
- recalcular miembros;
- generar snapshots;
- actualizar dashboards;
- reconstruir índices RAG;
- comparar versiones;
- emitir alertas.

---

# Generación incremental

El sistema debería evitar reconstruir todas las colecciones ante cada cambio.

Para ello necesitará:

- mapa de dependencias;
- hashes;
- registros de cambios;
- invalidación selectiva;
- caché.

---

# Caché

Podrán almacenarse temporalmente:

- resoluciones;
- consultas;
- subgrafos;
- métricas;
- chunks;
- embeddings.

---

## Clave de caché

Deberá incluir al menos:

- colección;
- versión;
- perfil;
- parámetros;
- versión de fuentes;
- permisos;
- motor.

---

# Invalidación de caché

Se producirá cuando cambie cualquier entrada relevante.

---

# Planificación de tareas

Las operaciones costosas podrán ejecutarse mediante colas.

Ejemplos:

- generación de embeddings;
- reconstrucción de subgrafos;
- análisis de cobertura;
- exportaciones;
- validaciones completas.

---

# Idempotencia

Los trabajos automáticos deberán ser idempotentes siempre que resulte posible.

Repetir una ejecución no debería generar duplicidades ni estados inconsistentes.

---

# Gestión de errores

Los errores deberán clasificarse.

---

## Error estructural

La definición es inválida.

---

## Error semántico

Existe contradicción o incoherencia.

---

## Error de resolución

No puede calcularse la pertenencia.

---

## Error de dependencia

Falta una fuente necesaria.

---

## Error de materialización

No puede persistirse el resultado.

---

## Error de indexación

Falla un índice de búsqueda o RAG.

---

## Error de autorización

El solicitante no dispone de permisos.

---

# Estrategias ante errores

Podrán aplicarse:

- detener;
- reintentar;
- continuar con advertencia;
- utilizar última versión válida;
- degradar funcionalidad;
- solicitar revisión.

---

# Última versión válida

Cuando una actualización falle, podrá mantenerse temporalmente la última materialización válida.

Deberá indicarse claramente que el resultado está desactualizado.

---

# Observabilidad

Toda operación relevante deberá ser observable.

---

# Logs

Los logs deberán registrar:

- colección;
- versión;
- operación;
- duración;
- resultado;
- errores;
- usuario o agente;
- correlación.

---

# Métricas operativas

Ejemplos:

- tiempo de resolución;
- número de miembros;
- tasa de fallos;
- caché hit rate;
- tiempo de indexación;
- latencia de consulta;
- colecciones desactualizadas;
- materializaciones inválidas.

---

# Trazas

Las trazas distribuidas podrán seguir el recorrido:

```text
API
↓
Resolver
↓
Knowledge Graph
↓
Projector
↓
Indexer
```

---

# Alertas operativas

Ejemplos:

- resolución fallida;
- índice desactualizado;
- dependencia incompatible;
- aumento anómalo de miembros;
- caída de cobertura;
- latencia excesiva;
- conflicto de permisos.

---

# Panel operativo

Un dashboard podrá mostrar:

- estado de colecciones;
- últimas resoluciones;
- errores;
- materializaciones;
- índices;
- métricas;
- alertas;
- deuda técnica.

---

# Rendimiento

El sistema deberá diseñarse para que las colecciones escalen.

---

# Factores de coste

El coste de resolución dependerá de:

- número de criterios;
- tamaño del Knowledge Graph;
- profundidad;
- número de dependencias;
- inferencias;
- consultas;
- materializaciones;
- permisos.

---

# Límites operativos

Podrán definirse límites por colección:

```yaml
execution_limits:
  max_members: 100000
  max_graph_depth: 4
  max_execution_seconds: 60
  max_memory_mb: 2048
```

---

# Presupuesto de consulta

Las consultas complejas podrán someterse a:

- timeout;
- coste máximo;
- profundidad máxima;
- número máximo de resultados;
- planificación previa.

---

# Optimización

Estrategias posibles:

- índices;
- caché;
- materialización;
- resolución incremental;
- consultas precompiladas;
- particionado;
- paralelización;
- prefiltrado.

---

# Índices recomendados

Según la tecnología:

- identificadores;
- tipos;
- etiquetas;
- relaciones;
- fechas;
- estado;
- colección;
- confianza;
- relevancia.

---

# Escalabilidad horizontal

Los resolvers, proyectores e indexadores podrán ejecutarse como servicios independientes.

---

# Seguridad

La seguridad deberá aplicarse en todas las capas.

---

# Autenticación

Toda operación no pública deberá identificar al actor.

---

# Autorización

Podrá aplicarse sobre:

- colección;
- miembro;
- proyección;
- acción;
- contexto;
- perfil.

---

# Seguridad a nivel de colección

Ejemplo:

```yaml
permissions:
  read:
    - public

  edit:
    - collection_maintainer

  approve:
    - semantic_reviewer

  publish:
    - knowledge_architect
```

---

# Seguridad a nivel de miembro

Aunque una colección sea visible, algunos miembros podrán estar restringidos.

El resultado deberá filtrarse conforme a los permisos efectivos.

---

# Seguridad en subgrafos

Las relaciones podrán revelar información indirecta.

Por ello no bastará con ocultar nodos.

También deberán revisarse:

- aristas;
- contadores;
- caminos;
- métricas;
- inferencias.

---

# Seguridad en RAG

El sistema deberá impedir que:

- un chunk restringido sea recuperado;
- un embedding revele contenido no autorizado;
- una respuesta mezcle dominios incompatibles;
- una caché comparta resultados entre usuarios indebidamente.

---

# Seguridad de agentes

Los agentes deberán respetar:

- identidad;
- permisos;
- límites de herramientas;
- políticas de colección;
- registro de acciones.

---

# Privacidad

Las colecciones personales o privadas deberán:

- minimizar datos;
- limitar retención;
- aplicar cifrado cuando proceda;
- permitir eliminación;
- evitar exposición accidental.

---

# Integridad

Los artefactos materializados podrán protegerse mediante:

- hashes;
- firmas;
- control de versiones;
- almacenamiento inmutable;
- auditoría.

---

# Publicación

Una colección podrá publicarse en diferentes niveles.

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

Disponible sin garantía de estabilidad.

---

# Artefactos de publicación

Una versión podrá incluir:

- definición;
- documentación;
- miembros;
- subgrafo;
- métricas;
- changelog;
- validaciones;
- exportaciones;
- índice.

---

# Contrato de publicación

Toda publicación deberá indicar:

- versión;
- estado;
- fecha;
- responsable;
- licencia;
- compatibilidad;
- fuentes;
- limitaciones.

---

# Sitio documental

Las colecciones podrán generar páginas dentro del sitio de documentación.

Una página podrá mostrar:

- descripción;
- alcance;
- estado;
- miembros destacados;
- subcolecciones;
- métricas;
- deuda;
- roadmap;
- historial.

---

# Integración con MkDocs

En la implementación documental inicial, una colección podrá generar:

- página Markdown;
- navegación;
- tablas;
- enlaces;
- gráficos;
- secciones de métricas.

La fuente canónica deberá permanecer fuera de `site_docs` si este directorio es generado.

---

# Integración con Git

Las definiciones de colecciones podrán versionarse en Git.

Esto permitirá:

- historial;
- revisión;
- ramas;
- pull requests;
- comparaciones;
- releases.

---

# Flujo Git recomendado

```text
feature/collection-...
        ↓
Validación
        ↓
Pull Request
        ↓
Revisión
        ↓
Merge
        ↓
Publicación
```

---

# Changelog

Toda colección con cambios relevantes deberá actualizar su historial.

Ejemplo:

```markdown
## 2.1.0 — 2026-08-15

- Añadido perfil tradicional.
- Incorporadas nuevas técnicas.
- Actualizada consulta de pertenencia.
```

---

# Pruebas

Las colecciones deberán disponer de pruebas.

---

# Pruebas estructurales

Comprueban:

- esquema;
- campos;
- tipos;
- referencias.

---

# Pruebas semánticas

Comprueban:

- pertenencias esperadas;
- exclusiones;
- jerarquías;
- conflictos.

---

# Pruebas de consulta

Comprueban que las consultas devuelven resultados correctos.

---

# Pruebas de regresión

Evitan cambios inesperados en:

- miembros;
- métricas;
- subgrafos;
- índices.

---

## Golden set

Una colección podrá mantener un conjunto esperado.

```yaml
expected_members:
  must_include:
    - ING-0008
    - REC-0009

  must_exclude:
    - REC-0042
```

---

# Pruebas de rendimiento

Evaluarán:

- latencia;
- consumo;
- escalabilidad;
- actualización incremental.

---

# Pruebas de seguridad

Evaluarán:

- permisos;
- filtrado;
- fuga de información;
- separación de contextos.

---

# Pruebas RAG

Evaluarán:

- recuperación;
- ranking;
- groundedness;
- citas;
- respuestas incorrectas;
- abstención.

---

# Pruebas de agentes

Evaluarán:

- uso de herramientas;
- cumplimiento de políticas;
- trazabilidad;
- límites;
- alucinaciones;
- acciones no autorizadas.

---

# Perfil inicial de implementación

El SGCC no necesita implementar desde el primer momento todas las capacidades descritas.

La adopción podrá realizarse de forma progresiva.

---

# Nivel 1 — Documental

Incluye:

- definición Markdown;
- front matter YAML;
- identificador;
- alcance;
- miembros explícitos;
- deuda;
- hitos;
- referencias.

---

# Nivel 2 — Estructurado

Añade:

- esquema YAML;
- validación;
- relaciones;
- criterios simples;
- generación automática de páginas;
- métricas básicas.

---

# Nivel 3 — Semántico

Añade:

- integración con ontología;
- resolución dinámica;
- Knowledge Graph;
- subgrafos;
- consultas;
- explicaciones.

---

# Nivel 4 — Recuperación

Añade:

- búsqueda híbrida;
- chunks;
- embeddings;
- índices RAG;
- evaluación de recuperación.

---

# Nivel 5 — Inteligente

Añade:

- agentes;
- planificación;
- recomendaciones;
- análisis automático;
- detección de deuda;
- generación asistida.

---

# Implementación inicial recomendada para NovaCoquinaria

La primera implementación práctica debería limitarse a:

```text
Colección definida en Markdown
+
Front matter YAML
+
Miembros explícitos
+
Referencias a documentos
+
Estado
+
Madurez
+
Deuda
+
Hitos
+
Validación automática
+
Generación de página
```

---

## Estructura de directorios propuesta

```text
collections/
├── README.md
├── COL-0001_cocina_japonesa.md
├── COL-0002_fermentaciones.md
└── schemas/
    └── collection.schema.yaml
```

---

## Registro inicial

Podrá generarse un archivo:

```text
collections_registry.md
```

o:

```text
collections_registry.yaml
```

con:

- identificador;
- nombre;
- estado;
- madurez;
- responsable;
- última revisión.

---

## Validaciones iniciales

El pipeline debería comprobar:

- front matter;
- identificadores únicos;
- campos obligatorios;
- referencias existentes;
- estados válidos;
- relaciones resolubles;
- ausencia de ciclos;
- enlaces correctos.

---

## Métricas iniciales

Podrán calcularse:

- número de colecciones;
- miembros explícitos;
- documentos referenciados;
- deuda registrada;
- relaciones entre colecciones;
- colecciones sin responsable;
- colecciones sin hitos;
- colecciones desactualizadas.

---

# Evolución hacia el Knowledge Graph

Cuando se implemente formalmente el Knowledge Graph, las colecciones podrán incorporar:

- miembros calculados;
- criterios ontológicos;
- subgrafos;
- consultas;
- inferencias;
- snapshots.

La evolución no deberá invalidar el modelo documental inicial.

---

# Evolución hacia RAG

Posteriormente podrán añadirse:

- selección de corpus;
- chunking;
- embeddings;
- índices;
- conjuntos de evaluación;
- recuperación híbrida.

---

# Evolución hacia agentes

Finalmente podrán añadirse:

- perfiles de agentes;
- herramientas;
- permisos;
- planificación;
- memoria;
- flujos de revisión.

---

# Compatibilidad hacia atrás

Las colecciones simples deberán seguir siendo válidas cuando aparezcan capacidades avanzadas.

Una colección con miembros explícitos no deberá estar obligada a utilizar:

- Knowledge Graph;
- SPARQL;
- embeddings;
- agentes.

---

# Degradación controlada

Si una capacidad avanzada no está disponible, la colección debería seguir ofreciendo las capacidades básicas posibles.

Ejemplo:

```text
Sin índice vectorial
        ↓
Búsqueda textual y documental
```

---

# Antipatrones operativos

Deberán evitarse los siguientes antipatrones.

---

## Resolver todas las colecciones ante cualquier cambio

Genera costes innecesarios.

Debe utilizarse análisis de impacto.

---

## Materializar sin procedencia

Impide reproducir resultados.

---

## Mezclar definición y caché

La definición canónica no debe depender de resultados temporales.

---

## Indexar contenido sin permisos

Puede provocar fugas de información.

---

## Crear embeddings sin versionar el modelo

Impide reproducibilidad.

---

## Utilizar RAG sin conjunto de evaluación

No permite medir calidad.

---

## Permitir a agentes modificar conocimiento canónico directamente

Toda modificación deberá revisarse.

---

## Ocultar el origen de una respuesta

Las respuestas deberán conservar citas y procedencia.

---

## Acoplar la colección a una tecnología

La colección no deberá definirse exclusivamente mediante Cypher, SPARQL o SQL.

---

## Utilizar únicamente búsqueda vectorial

La recuperación semántica debe combinarse con filtros, estructura y grafo cuando resulte útil.

---

## Materializaciones permanentes sin invalidación

Conducen a resultados obsoletos.

---

## Subgrafos sin política de frontera

Pueden crecer de forma incontrolada.

---

## Contextos RAG excesivos

Más contenido no implica mejores respuestas.

---

## Agentes con permisos globales

Contradice el principio de mínimo privilegio.

---

## Métricas sin interpretación

Los números deberán vincularse con objetivos y decisiones.

---

# Riesgos operativos

Entre los principales riesgos se encuentran:

- crecimiento excesivo de colecciones;
- consultas costosas;
- dependencias circulares;
- materializaciones obsoletas;
- índices inconsistentes;
- pérdida de trazabilidad;
- fuga de permisos;
- recuperación irrelevante;
- respuestas no fundamentadas;
- agentes fuera de dominio;
- acoplamiento tecnológico.

---

# Mitigaciones

Las mitigaciones incluyen:

- validación automática;
- límites operativos;
- versionado;
- análisis de impacto;
- auditoría;
- permisos;
- pruebas;
- evaluación RAG;
- explicabilidad;
- publicación controlada.

---

# Métricas de integración

Podrán medirse:

- porcentaje de colecciones resolubles;
- tiempo medio de resolución;
- porcentaje de materializaciones válidas;
- antigüedad media de índices;
- cobertura RAG;
- precisión de recuperación;
- tasa de conflictos;
- tasa de errores;
- uso por aplicaciones;
- uso por agentes.

---

# Indicadores de preparación

Una colección estará preparada para una capacidad cuando cumpla los requisitos mínimos.

---

## Preparada para Knowledge Graph

Requiere:

- identificadores estables;
- miembros resolubles;
- relaciones;
- tipos;
- criterios claros;
- ontología aplicable.

---

## Preparada para RAG

Requiere:

- contenido suficiente;
- calidad mínima;
- permisos;
- estructura;
- procedencia;
- evaluación inicial.

---

## Preparada para agentes

Requiere:

- dominio estable;
- herramientas definidas;
- permisos;
- reglas;
- fuentes;
- mecanismos de auditoría.

---

# Conformidad operativa

Una colección será operativamente conforme cuando:

- pueda cargarse;
- supere la validación;
- resuelva sus dependencias;
- pueda determinar sus miembros;
- conserve procedencia;
- respete permisos;
- pueda generar las proyecciones declaradas;
- produzca métricas;
- registre errores;
- mantenga compatibilidad con su versión.

---

# Niveles de conformidad

---

## Conformidad documental

La definición y sus referencias son válidas.

---

## Conformidad estructural

Cumple el metamodelo.

---

## Conformidad semántica

Los criterios y relaciones son coherentes.

---

## Conformidad operativa

Puede resolverse y proyectarse.

---

## Conformidad inteligente

Puede alimentar RAG y agentes con calidad evaluada.

---

# Lista de comprobación

Antes de publicar una integración deberá verificarse:

```text
[ ] La colección posee versión.
[ ] Las fuentes están identificadas.
[ ] Las dependencias son compatibles.
[ ] La resolución es reproducible.
[ ] Los miembros tienen procedencia.
[ ] Los permisos se aplican correctamente.
[ ] Las materializaciones incluyen hash.
[ ] Las proyecciones están documentadas.
[ ] Los índices están versionados.
[ ] Las métricas se calculan.
[ ] Los errores se registran.
[ ] Existen pruebas.
[ ] La documentación está actualizada.
```

---

# Arquitectura de referencia

La arquitectura completa puede representarse así:

```text
┌───────────────────────────────────────────────┐
│                 Fuentes SGCC                  │
│                                               │
│ Documentos · Componentes · Ontología · Grafo │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│           Definición de Colecciones           │
│                                               │
│ Alcance · Criterios · Miembros · Perfiles     │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              Servicios Operativos             │
│                                               │
│ Registry · Validator · Resolver · Projector   │
│ Materializer · Indexer · Audit · Metrics      │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             Representaciones Derivadas        │
│                                               │
│ Vistas · Subgrafos · Snapshots · Índices      │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                  Consumidores                 │
│                                               │
│ Web · APIs · RAG · Agentes · Dashboards       │
└───────────────────────────────────────────────┘
```

---

# Relación con las demás especificaciones

| Especificación | Responsabilidad |
|---|---|
| `ESPECIFICACION_DE_DOCUMENTOS.md` | Define las unidades documentales |
| `ESPECIFICACION_DE_COMPONENTES.md` | Define las unidades internas reutilizables |
| `ESPECIFICACION_DE_RELACIONES.md` | Define conexiones y propiedades relacionales |
| `ESPECIFICACION_DE_ONTOLOGIA.md` | Define el significado formal |
| `ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md` | Definirá la materialización del conocimiento conectado |
| `ESPECIFICACION_DEL_RAZONADOR.md` | Definirá inferencia y explicación |
| `ESPECIFICACION_RAG.md` | Definirá recuperación y generación aumentada |
| `ESPECIFICACION_DE_AGENTES.md` | Definirá comportamiento autónomo y herramientas |
| `KNOWLEDGE_DEBT.md` | Gestiona carencias de conocimiento |
| `KNOWLEDGE_MATURITY.md` | Evalúa madurez |
| `ROADMAP.md` | Organiza prioridades temporales |

---

# Ejemplo operativo completo

La siguiente definición conceptual muestra una colección preparada para varias proyecciones.

```yaml
id: COL-0001
type: collection
title: Cocina japonesa
version: 2.0.0
status: en_consolidacion
maturity: estructurada

membership_mode: hybrid
conflict_policy: highest_priority

ontology:
  modules:
    - ingredients
    - recipes
    - techniques
    - cuisines

explicit_members:
  - id: ING-0008
    role: core

criteria:
  - id: COL-CRT-0001
    type: ontological
    priority: 80

    condition:
      instance_of: Recipe
      property:
        predicate: belongs_to_cuisine
        object: JapaneseCuisine

graph_projection:
  boundary_policy: contextual
  max_depth: 2
  min_confidence: 0.70

  allowed_predicates:
    - uses_ingredient
    - applies_technique
    - belongs_to_cuisine
    - originates_from

document_projection:
  group_by:
    - type

  order_by:
    - relevance
    - title

rag_projection:
  enabled: true

  allowed_status:
    - stable
    - reference

  minimum_quality: 0.75
  include_drafts: false

  chunking:
    strategy: semantic_component

  retrieval:
    mode: hybrid
    max_results: 12

agent_profile:
  enabled: true
  role: japanese_cuisine_assistant

  capabilities:
    - semantic_search
    - graph_navigation
    - document_retrieval

  restrictions:
    - cite_sources
    - no_modify_canonical_content
    - respect_permissions

execution:
  resolution_mode: incremental
  deterministic: true

  limits:
    max_members: 5000
    max_execution_seconds: 30

publication:
  documentary_view: true
  graph_view: true
  analytics_view: true
```

---

# Resultado derivado

La resolución anterior podrá producir:

```yaml
resolution:
  id: RES-COL-0001-20260731-001
  collection: COL-0001
  collection_version: 2.0.0
  graph_version: 1.4.0
  resolved_at: 2026-07-31T14:00:00+02:00

  members:
    explicit: 1
    calculated: 84
    inferred: 21
    auxiliary: 17
    total: 123

  projections:
    documentary:
      status: ready
      documents: 46

    graph:
      status: ready
      nodes: 123
      edges: 487

    rag:
      status: ready
      chunks: 312
      embeddings: 312

    agent:
      status: ready

  validation:
    structural: passed
    semantic: passed
    operational: passed

  warnings:
    - 2 inferred members have confidence below 0.80

  hash: sha256:...
```

---

# Conclusión

La integración operativa transforma las Colecciones de Conocimiento en capacidades utilizables dentro del SGCC.

Una colección puede actuar simultáneamente como:

- ámbito documental;
- vista semántica;
- subgrafo;
- unidad analítica;
- corpus de recuperación;
- contexto para agentes;
- recurso de API;
- producto publicable.

Esta transformación debe realizarse sin alterar el principio fundamental del modelo:

> Las colecciones no sustituyen ni duplican el conocimiento canónico. Lo seleccionan, organizan, proyectan y ponen a disposición de aplicaciones y procesos inteligentes de manera gobernada, explicable y reproducible.

La especificación completa establece así una evolución progresiva:

```text
Colección documental
        ↓
Colección estructurada
        ↓
Colección semántica
        ↓
Colección operativa
        ↓
Colección recuperable
        ↓
Colección inteligente
```

Con esta cuarta parte queda definido el modelo integral de Colecciones de Conocimiento del SGCC, incluyendo:

- fundamentos;
- metamodelo;
- ciclo de vida;
- gobernanza;
- integración con documentos;
- integración ontológica;
- proyección sobre el Knowledge Graph;
- materialización;
- APIs;
- búsqueda;
- RAG;
- agentes;
- automatización;
- seguridad;
- observabilidad;
- conformidad.

Este modelo servirá como base directa para la siguiente especificación arquitectónica:

```text
ESPECIFICACION_DEL_KNOWLEDGE_GRAPH.md
```

En ella se desarrollará formalmente cómo el SGCC representa, almacena, conecta, consulta, versiona y explota las entidades y relaciones que las colecciones utilizan para construir sus vistas semánticas.

