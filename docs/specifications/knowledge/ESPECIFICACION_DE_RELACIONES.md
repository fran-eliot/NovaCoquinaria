---
id: DOC-0022
titulo: Especificación de Relaciones
tipo: especificacion
version: 1.0.0
estado: en_revision
ultima_revision: 2026-07-30
---

# ESPECIFICACIÓN DE RELACIONES

> **Proyecto:** NovaCoquinaria  
> **Release:** v1.4 – Knowledge Governance  
> **Sistema:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)  
> **Especificación:** v1.0.0

---

# Introducción

El conocimiento gestionado por NovaCoquinaria no está formado únicamente por componentes aislados.

Su significado emerge también de las conexiones existentes entre:

- ingredientes;
- técnicas;
- elaboraciones;
- recetas;
- bases culinarias;
- menús;
- plantillas;
- colecciones;
- conceptos;
- restricciones;
- recursos;
- documentos.

Una receta adquiere parte de su significado porque utiliza determinados ingredientes, aplica determinadas técnicas, produce un resultado, pertenece a una tradición culinaria y puede formar parte de un menú.

Del mismo modo, un ingrediente puede sustituir a otro, una técnica puede requerir cierto equipo y una plantilla puede generar múltiples recetas.

Estas conexiones constituyen las **relaciones semánticas** del Sistema de Gestión del Conocimiento Culinario.

La presente especificación define el modelo oficial de relaciones del SGCC y establece:

- qué es una relación;
- qué elementos la componen;
- cómo se identifica;
- cómo se clasifica;
- qué restricciones puede poseer;
- cómo se diferencia de una propiedad;
- cómo se representa;
- cómo participa en la construcción de la ontología y del Knowledge Graph.

Esta especificación transforma el catálogo de componentes definido en `ESPECIFICACION_DE_COMPONENTES.md` en una red de conocimiento conectada, navegable e interpretable por personas y sistemas automáticos.

---

# Objetivo

El objetivo de esta especificación es establecer el contrato semántico que regula las relaciones entre los activos de conocimiento del SGCC.

En particular, deberá definir:

- el concepto general de relación;
- sus elementos estructurales;
- su dirección;
- su dominio y rango;
- su cardinalidad;
- sus relaciones inversas;
- sus posibles propiedades;
- sus restricciones;
- su semántica;
- sus reglas de representación;
- su capacidad de inferencia.

El modelo permitirá expresar afirmaciones como:

```text
Una receta utiliza un ingrediente.
```

```text
Una técnica requiere un equipo.
```

```text
Una elaboración forma parte de una receta.
```

```text
Una receta pertenece a una colección.
```

```text
Un ingrediente puede sustituir a otro.
```

El objetivo no es únicamente conectar documentos, sino expresar significado de forma formal, consistente y reutilizable.

---

# Alcance

Esta especificación se aplica a las relaciones existentes entre:

- componentes culinarios;
- componentes estructurales;
- componentes organizativos;
- activos documentales;
- representaciones;
- colecciones;
- conceptos;
- restricciones;
- resultados;
- elementos de planificación.

Incluye:

- relaciones binarias;
- relaciones contextualizadas;
- relaciones dirigidas;
- relaciones simétricas;
- relaciones inversas;
- relaciones jerárquicas;
- relaciones de composición;
- relaciones de dependencia;
- relaciones temporales;
- relaciones derivadas;
- relaciones inferidas;
- relaciones documentales con significado semántico.

También establece las reglas generales necesarias para incorporar nuevos tipos de relaciones en el futuro.

---

## Fuera de alcance

No forma parte del alcance de esta especificación:

- definir exhaustivamente la ontología formal del SGCC;
- establecer todos los axiomas de inferencia;
- diseñar una base de datos concreta;
- imponer una tecnología de grafo determinada;
- definir formatos de visualización;
- especificar consultas SPARQL, Cypher o SQL;
- establecer la implementación detallada de APIs;
- regular los enlaces puramente editoriales sin significado semántico.

Estos aspectos podrán desarrollarse en documentos especializados.

---

# Dependencias normativas

Esta especificación deberá interpretarse junto con:

- `ESPECIFICACION_DE_DOCUMENTOS.md`;
- `ESPECIFICACION_DE_COMPONENTES.md`;
- `ESPECIFICACION_DE_COLECCIONES.md`;
- `MODELO_DE_CONOCIMIENTO.md`;
- `ARQUITECTURA.md`;
- `GOVERNANCE_MODEL.md`;
- `QUALITY.md`.

La relación entre estas especificaciones puede resumirse de la siguiente forma:

```text
ESPECIFICACION_DE_COMPONENTES
        │
        │ define las entidades
        ▼
ESPECIFICACION_DE_RELACIONES
        │
        │ define sus conexiones
        ▼
ESPECIFICACION_DE_ONTOLOGIA
        │
        │ formaliza significado y restricciones
        ▼
Knowledge Graph
```

`ESPECIFICACION_DE_DOCUMENTOS.md` establece cómo se representan persistentemente los activos.

`ESPECIFICACION_DE_COMPONENTES.md` establece qué entidades pueden existir.

La presente especificación establece cómo pueden conectarse dichas entidades.

La futura `ESPECIFICACION_DE_ONTOLOGIA.md` integrará componentes, relaciones, propiedades y axiomas en un modelo semántico unificado.

---

# Definiciones

Esta sección establece el vocabulario normativo utilizado por el modelo de relaciones.

---

## Relación

Vínculo semántico entre dos o más activos de conocimiento.

Una relación expresa una afirmación interpretable sobre las entidades conectadas.

Ejemplo:

```text
Receta ── utiliza ── Ingrediente
```

La relación `utiliza` expresa que una receta incorpora un ingrediente en su composición o proceso.

Una relación no es únicamente un enlace técnico.

Debe poseer un significado explícito y estable.

---

## Tipo de relación

Categoría semántica que define el significado general de un conjunto de relaciones.

Ejemplos:

- utiliza;
- contiene;
- requiere;
- produce;
- sustituye a;
- forma parte de;
- pertenece a;
- deriva de;
- precede a;
- representa.

El tipo establece el contrato general de la relación.

---

## Instancia de relación

Afirmación concreta que conecta componentes específicos.

Ejemplo:

```text
REC-0042 ── utiliza ── ING-0017
```

Donde:

- `REC-0042` representa una receta;
- `ING-0017` representa un ingrediente;
- `utiliza` es el tipo de relación;
- la conexión completa constituye una instancia de relación.

---

## Sujeto

Componente o activo desde el que se expresa una relación dirigida.

Ejemplo:

```text
Curry japonés ── utiliza ── cebolla
```

El sujeto es:

```text
Curry japonés
```

---

## Predicado

Expresión que representa el tipo de relación.

En el ejemplo:

```text
Curry japonés ── utiliza ── cebolla
```

el predicado es:

```text
utiliza
```

---

## Objeto

Componente o valor hacia el que se dirige la relación.

En el ejemplo anterior, el objeto es:

```text
cebolla
```

---

## Triple semántica

Estructura formada por:

```text
Sujeto + Predicado + Objeto
```

Ejemplo:

```text
Receta + utiliza + Ingrediente
```

O mediante identificadores:

```text
REC-0042 + utiliza + ING-0017
```

La triple constituye la unidad básica de representación en numerosos modelos de conocimiento.

---

## Dominio

Tipo o conjunto de tipos que pueden actuar como sujeto de una relación.

Ejemplo:

```text
Relación: utiliza
Dominio: Receta, Base culinaria, Elaboración
```

Esto significa que una receta, base o elaboración puede utilizar otro componente permitido.

El dominio no representa una instancia concreta, sino una restricción sobre el tipo de origen.

---

## Rango

Tipo o conjunto de tipos que pueden actuar como objeto de una relación.

Ejemplo:

```text
Relación: utiliza
Rango: Ingrediente, Base culinaria, Elaboración
```

El rango establece qué tipos de componentes pueden aparecer como destino.

---

## Dirección

Orientación semántica de una relación.

Ejemplo:

```text
Receta ── utiliza ── Ingrediente
```

La dirección va desde la receta hacia el ingrediente.

La dirección no implica necesariamente causalidad ni dependencia.

---

## Relación inversa

Relación que expresa la misma conexión desde la perspectiva contraria.

Ejemplo:

```text
Receta ── utiliza ── Ingrediente
```

Relación inversa:

```text
Ingrediente ── es_utilizado_por ── Receta
```

Ambas expresan la misma conexión semántica desde orientaciones diferentes.

---

## Cardinalidad

Número mínimo o máximo de componentes que pueden participar en un extremo de la relación.

Ejemplos:

```text
Una receta utiliza uno o más ingredientes.
```

```text
Una elaboración puede producir un único resultado principal.
```

```text
Una receta puede pertenecer a cero o muchas colecciones.
```

La cardinalidad podrá representarse mediante expresiones como:

```text
0..1

1..1

0..*

1..*
```

---

## Propiedad

Característica descriptiva de un componente o de una relación.

Ejemplos de propiedades de componente:

- nombre;
- descripción;
- dificultad;
- temperatura;
- origen.

Ejemplos de propiedades de relación:

- cantidad;
- unidad;
- orden;
- fecha;
- confianza;
- opcionalidad.

Una propiedad no conecta por sí sola dos componentes con identidad independiente.

---

## Atributo de relación

Dato que describe el contexto específico de una relación.

Ejemplo:

```text
Receta ── utiliza ── Ingrediente
                    │
                    ├── cantidad: 200
                    ├── unidad: gramos
                    ├── preparación: picado
                    └── opcional: false
```

En este caso:

- la receta es el sujeto;
- el ingrediente es el objeto;
- `utiliza` es la relación;
- cantidad, unidad, preparación y opcionalidad son atributos de la relación.

---

## Relación contextualizada

Relación cuyo significado completo depende de datos adicionales.

Por ejemplo, afirmar que una receta utiliza harina no expresa todavía:

- cuánta harina;
- en qué fase;
- con qué finalidad;
- si es opcional;
- qué sustitución admite.

Una relación contextualizada permite representar esa información sin asignarla incorrectamente al componente origen o destino.

---

## Entidad asociativa

Componente intermedio utilizado para representar una relación con identidad, propiedades o comportamiento propios.

Ejemplo:

```text
Receta
   │
   ▼
Uso de ingrediente
   │
   ▼
Ingrediente
```

La entidad `Uso de ingrediente` podría contener:

- cantidad;
- unidad;
- preparación previa;
- orden;
- opcionalidad;
- sustituciones;
- elaboración en la que se utiliza.

Las entidades asociativas resultan especialmente útiles para relaciones complejas o n-arias.

---

## Relación binaria

Relación que conecta dos entidades principales.

Ejemplo:

```text
Técnica ── requiere ── Equipo
```

Es el tipo de relación más sencillo y frecuente.

---

## Relación n-aria

Relación que conecta conceptualmente más de dos entidades.

Ejemplo:

```text
Una receta utiliza un ingrediente
en una cantidad
medida mediante una unidad
dentro de una elaboración concreta.
```

Este caso podría involucrar:

- receta;
- ingrediente;
- cantidad;
- unidad;
- elaboración.

Las relaciones n-arias podrán representarse mediante entidades asociativas.

---

## Relación jerárquica

Relación que establece una estructura de generalización, especialización, inclusión o clasificación.

Ejemplos:

```text
Arroz basmati ── es_un ── Arroz
```

```text
Técnica de cocción ── incluye ── Confitar
```

```text
Ingrediente ── se_clasifica_en ── Familia de ingredientes
```

---

## Relación de composición

Relación que expresa que un componente forma parte estructural o funcional de otro.

Ejemplo:

```text
Elaboración ── forma_parte_de ── Receta
```

La composición puede implicar una dependencia fuerte entre las partes y el conjunto.

---

## Relación de agregación

Relación que agrupa componentes que mantienen independencia propia.

Ejemplo:

```text
Colección ── contiene ── Receta
```

Eliminar la colección no implica eliminar las recetas.

---

## Relación de dependencia

Relación que expresa que un componente necesita otro para existir, ejecutarse o cumplir su finalidad.

Ejemplo:

```text
Técnica ── requiere ── Equipo
```

```text
Elaboración ── depende_de ── Base culinaria
```

---

## Relación de transformación

Relación que expresa que un proceso o técnica transforma un componente o produce un resultado.

Ejemplos:

```text
Técnica ── transforma ── Ingrediente
```

```text
Receta ── produce ── Resultado culinario
```

---

## Relación temporal

Relación que expresa orden, simultaneidad o dependencia temporal.

Ejemplos:

```text
Elaboración A ── precede_a ── Elaboración B
```

```text
Técnica A ── ocurre_durante ── Proceso
```

```text
Preparación ── debe_realizarse_antes_de ── Servicio
```

---

## Relación de equivalencia

Relación que indica que dos componentes representan el mismo concepto o poseen una equivalencia definida.

Ejemplo:

```text
Cilantro ── equivalente_terminológico_a ── Coriandro
```

La equivalencia deberá utilizarse con precaución, ya que puede depender del idioma, contexto o uso regional.

---

## Relación de sustitución

Relación que expresa que un componente puede reemplazar a otro en determinadas condiciones.

Ejemplo:

```text
Yogur ── sustituye_a ── Nata
```

La sustitución no implica identidad ni equivalencia completa.

Podrá depender de:

- receta;
- proporción;
- técnica;
- resultado esperado;
- restricción dietética.

---

## Relación de derivación

Relación que expresa que un componente se ha generado, adaptado o construido a partir de otro.

Ejemplos:

```text
Receta vegana ── deriva_de ── Receta tradicional
```

```text
Lista de compra ── deriva_de ── Menú semanal
```

---

## Relación inferida

Relación no declarada explícitamente, pero obtenida mediante reglas o razonamiento.

Ejemplo:

```text
Receta utiliza mantequilla.
Mantequilla contiene leche.
```

El sistema podría inferir:

```text
Receta contiene alérgeno lácteo.
```

Toda relación inferida deberá distinguirse de una relación declarada directamente.

---

## Procedencia

Información que indica el origen de una relación.

Puede incluir:

- documento fuente;
- autor;
- sistema;
- fecha;
- regla de inferencia;
- importación;
- nivel de confianza.

La procedencia permite evaluar la fiabilidad y trazabilidad de las afirmaciones.

---

## Confianza

Grado de certeza atribuido a una relación.

Puede utilizarse especialmente en:

- relaciones inferidas;
- recomendaciones;
- compatibilidades;
- sustituciones;
- conocimiento importado;
- resultados generados mediante IA.

La confianza no sustituye a la validación humana ni convierte una hipótesis en conocimiento canónico.

---

# Relación frente a propiedad

Distinguir relaciones y propiedades es esencial para preservar la calidad del modelo.

---

## Propiedad

Una propiedad describe una característica de una entidad.

Ejemplo:

```text
Ingrediente:
- nombre: ajo
- color: blanco
- origen: vegetal
```

---

## Relación

Una relación conecta entidades con identidad propia.

Ejemplo:

```text
Ajo ── pertenece_a ── Familia Allium
```

La familia puede existir como componente independiente y relacionarse con múltiples ingredientes.

---

## Regla general

Deberá utilizarse una propiedad cuando el valor:

- sea descriptivo;
- no requiera identidad propia;
- no necesite relaciones adicionales;
- no se reutilice como entidad independiente.

Deberá utilizarse una relación cuando el valor:

- tenga identidad propia;
- pueda reutilizarse;
- participe en otras relaciones;
- tenga propiedades propias;
- forme parte del conocimiento navegable.

---

## Ejemplo comparativo

Representación simple mediante propiedad:

```text
Receta:
- dificultad: media
```

Representación mediante relación:

```text
Receta ── pertenece_a ── Cocina japonesa
```

`media` puede tratarse como un valor controlado.

`Cocina japonesa` puede modelarse como un concepto o categoría con identidad propia.

---

# Relación frente a enlace documental

Un enlace documental permite navegar entre archivos o recursos.

Una relación semántica expresa significado.

Ejemplo de enlace documental:

```markdown
[Consultar la receta](../../../12_Plantillas/04_Cocciones/curry_base.md)
```

El enlace indica dónde encontrar un documento.

No especifica por sí mismo qué relación existe entre el documento actual y la receta.

---

## Enlace semánticamente tipado

Una relación explícita podría expresar:

```text
Menú semanal ── incluye ── Curry japonés
```

La relación `incluye` tiene significado formal y puede ser interpretada por:

- validadores;
- Knowledge Graph;
- APIs;
- buscadores;
- sistemas RAG;
- agentes de IA.

---

## Correspondencia

Una relación semántica puede materializarse mediante un enlace documental, pero ambos conceptos no son equivalentes.

```text
Relación conceptual
        │
        ▼
Referencia por identificador
        │
        ▼
Enlace documental
```

El identificador expresa la identidad.

El enlace expresa una ruta de acceso.

La relación expresa el significado de la conexión.

---

# Relación frente a composición documental

La presencia de varios elementos en un mismo documento no implica necesariamente una relación formal entre componentes.

Ejemplo:

Un documento puede mencionar:

- arroz;
- curry;
- Japón;
- olla.

La coexistencia textual no permite concluir automáticamente que:

```text
Arroz utiliza curry.
```

o que:

```text
Japón requiere olla.
```

Las relaciones deberán declararse, derivarse mediante reglas válidas o inferirse con trazabilidad.

---

# Modelo conceptual general

El modelo relacional del SGCC puede representarse de la siguiente forma:

```text
Componente origen
        │
        ▼
     Relación
        │
        ▼
Componente destino
```

Una relación completa incorpora además:

```text
Relación
    │
    ├── Identificador
    ├── Nombre canónico
    ├── Descripción
    ├── Dominio
    ├── Rango
    ├── Dirección
    ├── Cardinalidad
    ├── Inversa
    ├── Propiedades
    ├── Restricciones
    ├── Procedencia
    └── Estado
```

---

# Anatomía normativa de una relación

Todo tipo de relación reconocido por el SGCC deberá documentarse mediante los elementos definidos en esta sección.

---

## Identificador

Cada tipo de relación deberá disponer de un identificador persistente.

Ejemplo:

```text
REL-0001
```

El identificador no deberá depender:

- del nombre visible;
- del idioma;
- de la ubicación documental;
- de la implementación tecnológica.

---

## Nombre canónico

Nombre oficial utilizado para expresar la relación.

Ejemplos:

```text
utiliza

forma_parte_de

requiere

produce

deriva_de
```

El nombre deberá ser:

- claro;
- preciso;
- estable;
- no ambiguo;
- coherente con el vocabulario del SGCC.

---

## Etiqueta legible

Una relación podrá disponer de etiquetas adaptadas a distintos idiomas o contextos de presentación.

Ejemplo:

```text
Nombre canónico: utiliza

Etiqueta española: utiliza

Etiqueta inglesa: uses
```

La etiqueta no modifica la identidad de la relación.

---

## Definición

Toda relación deberá incluir una definición normativa.

La definición deberá explicar:

- qué significa;
- en qué condiciones se aplica;
- qué no significa;
- qué diferencia mantiene respecto a relaciones similares.

---

## Dominio

Deberá declarar los tipos de componentes permitidos como origen.

Ejemplo:

```text
Dominio:
- Receta
- Base culinaria
- Elaboración
```

---

## Rango

Deberá declarar los tipos permitidos como destino.

Ejemplo:

```text
Rango:
- Ingrediente
- Base culinaria
- Elaboración
```

---

## Dirección

Deberá indicar si la relación es:

- dirigida;
- no dirigida;
- simétrica;
- representada en ambos sentidos.

---

## Cardinalidad

Deberá declarar, cuando resulte relevante:

- cardinalidad mínima;
- cardinalidad máxima;
- restricciones por tipo;
- obligatoriedad.

Ejemplo:

```text
Receta ── produce ── Resultado

Cardinalidad:
- una receta debe producir al menos un resultado;
- una receta puede producir varios resultados secundarios.
```

---

## Relación inversa

Deberá indicar si existe una relación inversa reconocida.

Ejemplo:

```text
utiliza
```

Inversa:

```text
es_utilizado_por
```

No todas las relaciones requerirán una inversa explícitamente almacenada.

Podrá calcularse durante la consulta.

---

## Propiedades de la relación

Deberán definirse los atributos contextuales permitidos.

Ejemplo:

```text
Relación: utiliza

Propiedades:
- cantidad;
- unidad;
- preparación;
- opcionalidad;
- orden;
- observaciones.
```

---

## Restricciones

Deberán declararse:

- combinaciones de tipos permitidas;
- valores obligatorios;
- incompatibilidades;
- reglas de integridad;
- condiciones contextuales;
- excepciones.

---

## Características lógicas

Toda relación deberá indicar, cuando corresponda, si es:

- simétrica;
- asimétrica;
- transitiva;
- intransitiva;
- reflexiva;
- irreflexiva;
- funcional;
- inversamente funcional.

Estas características se desarrollarán en la parte estructural de esta especificación.

---

## Procedencia

Toda instancia de relación deberá poder asociarse a su fuente cuando resulte necesario.

Ejemplo:

```text
Fuente: REC-0042
Declarada por: autor
Fecha: 2026-07-30
```

---

## Nivel de confianza

Cuando la relación no sea completamente determinista podrá incluir un nivel de confianza.

Ejemplo:

```text
Relación: combina_con
Confianza: 0.82
Origen: modelo de recomendación
```

Las relaciones canónicas revisadas no necesitarán necesariamente expresar confianza numérica.

---

## Estado

Un tipo o instancia de relación podrá encontrarse en estados como:

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

---

## Ejemplos y contraejemplos

Toda relación deberá incluir ejemplos válidos y, cuando exista riesgo de ambigüedad, contraejemplos.

Ejemplo válido:

```text
Receta ── utiliza ── Ingrediente
```

Contraejemplo:

```text
Ingrediente ── utiliza ── Receta
```

salvo que se trate de otra relación semántica distinta.

---

# Plantilla normativa de relación

Los tipos de relaciones podrán documentarse mediante una estructura como la siguiente:

```yaml
id: REL-0001
nombre: utiliza
version: 1.0.0
estado: estable

definicion: >
  Expresa que un componente culinario incorpora o emplea otro
  componente durante su composición o ejecución.

dominio:
  - receta
  - base_culinaria
  - elaboracion

rango:
  - ingrediente
  - base_culinaria
  - elaboracion

direccion: dirigida

inversa: es_utilizado_por

cardinalidad:
  origen_minimo: 0
  origen_maximo: "*"
  destino_minimo: 0
  destino_maximo: "*"

propiedades:
  - cantidad
  - unidad
  - preparacion
  - opcional
  - orden

caracteristicas:
  simetrica: false
  transitiva: false
  reflexiva: false
```

La sintaxis anterior es ilustrativa.

La representación física definitiva podrá definirse mediante esquemas especializados.

---

# Principios del modelo de relaciones

Toda relación gestionada por el SGCC deberá respetar los principios establecidos en esta sección.

---

## Semántica explícita

Toda relación deberá expresar un significado definido.

No deberán utilizarse relaciones genéricas como:

```text
relacionado_con
```

cuando pueda emplearse una relación más precisa.

Ejemplos preferibles:

```text
utiliza

requiere

produce

sustituye_a

deriva_de
```

Las relaciones genéricas solo deberán utilizarse cuando no exista una semántica más específica y su uso esté justificado.

---

## Identidad estable

Cada tipo de relación deberá poseer una identidad persistente.

Cambiar su nombre visible no deberá modificar su identidad.

---

## Dirección coherente

Las relaciones dirigidas deberán utilizar siempre una orientación canónica.

Ejemplo:

```text
Receta ── utiliza ── Ingrediente
```

No deberá alternarse arbitrariamente con:

```text
Ingrediente ── utilizado_en ── Receta
```

salvo que `utilizado_en` esté definido como relación inversa.

---

## Dominio y rango explícitos

Toda relación deberá indicar qué tipos pueden participar como origen y destino.

Esto permite:

- validar afirmaciones;
- evitar errores semánticos;
- generar formularios;
- construir APIs;
- mejorar inferencias.

---

## No duplicidad

No deberán existir varias relaciones con significado equivalente sin una justificación expresa.

Ejemplo problemático:

```text
usa

utiliza

emplea
```

Si representan exactamente el mismo significado, deberán consolidarse bajo un nombre canónico y registrar los demás como alias.

---

## Contextualización

Cuando una relación requiera propiedades adicionales, estas deberán representarse explícitamente.

No deberá perderse información contextual mediante relaciones excesivamente simples.

---

## Trazabilidad

Toda relación relevante deberá poder rastrearse hasta:

- su fuente;
- su autor;
- su proceso de generación;
- su regla de inferencia;
- su representación canónica.

---

## Independencia tecnológica

Las relaciones deberán definirse mediante su significado, no mediante una implementación concreta.

No deberá afirmarse:

> Una relación es una clave foránea.

Deberá afirmarse:

> Una relación es un vínculo semántico que puede implementarse mediante una clave foránea.

---

## Reutilización

Una relación deberá poder aplicarse a múltiples instancias siempre que respeten su dominio, rango y restricciones.

---

## Interoperabilidad

Las relaciones deberán poder representarse mediante:

- Markdown;
- YAML;
- JSON;
- bases de datos relacionales;
- grafos de propiedades;
- RDF;
- APIs;
- sistemas RAG;
- modelos de embeddings;
- agentes inteligentes.

---

## Inferencia controlada

Las reglas de inferencia deberán:

- estar documentadas;
- ser reproducibles;
- distinguir relaciones declaradas e inferidas;
- conservar procedencia;
- evitar conclusiones no justificadas.

---

## Compatibilidad evolutiva

La evolución de una relación deberá preservar, cuando sea posible:

- identidad;
- significado;
- compatibilidad;
- relaciones existentes;
- trazabilidad histórica.

---

# Clasificación general de relaciones

El SGCC clasifica inicialmente sus relaciones según su responsabilidad semántica.

```text
Relación
    │
    ├── Relaciones estructurales
    │      ├── contiene
    │      ├── forma_parte_de
    │      ├── incluye
    │      └── compuesto_por
    │
    ├── Relaciones de uso y dependencia
    │      ├── utiliza
    │      ├── requiere
    │      ├── depende_de
    │      └── necesita
    │
    ├── Relaciones de proceso y transformación
    │      ├── aplica
    │      ├── transforma
    │      ├── produce
    │      └── genera
    │
    ├── Relaciones temporales y secuenciales
    │      ├── precede_a
    │      ├── sigue_a
    │      ├── ocurre_durante
    │      └── simultaneo_a
    │
    ├── Relaciones taxonómicas
    │      ├── es_un
    │      ├── subtipo_de
    │      ├── clasifica
    │      └── pertenece_a_categoria
    │
    ├── Relaciones de variación y equivalencia
    │      ├── variante_de
    │      ├── equivalente_a
    │      ├── similar_a
    │      └── alias_de
    │
    ├── Relaciones de sustitución y compatibilidad
    │      ├── sustituye_a
    │      ├── compatible_con
    │      ├── combina_con
    │      └── incompatible_con
    │
    ├── Relaciones de derivación y procedencia
    │      ├── deriva_de
    │      ├── basado_en
    │      ├── adaptado_de
    │      └── generado_desde
    │
    ├── Relaciones organizativas
    │      ├── pertenece_a
    │      ├── miembro_de
    │      ├── indexado_en
    │      └── incluido_en
    │
    ├── Relaciones de restricción
    │      ├── excluye
    │      ├── limita
    │      ├── satisface
    │      └── incumple
    │
    └── Relaciones de representación
           ├── representado_por
           ├── documentado_en
           ├── serializado_como
           └── publicado_en
```

Esta clasificación inicial podrá evolucionar durante la formalización de la ontología.

---

# Relaciones estructurales

Representan cómo los componentes forman conjuntos o estructuras complejas.

Ejemplos:

```text
Receta ── contiene ── Elaboración
```

```text
Elaboración ── forma_parte_de ── Receta
```

```text
Colección ── incluye ── Receta
```

Estas relaciones deberán distinguir entre:

- composición fuerte;
- agregación;
- pertenencia organizativa;
- mera inclusión editorial.

---

# Relaciones de uso y dependencia

Representan la utilización o necesidad de un componente por otro.

Ejemplos:

```text
Receta ── utiliza ── Ingrediente
```

```text
Técnica ── requiere ── Equipo
```

```text
Elaboración ── depende_de ── Base culinaria
```

---

# Relaciones de proceso y transformación

Representan acciones, transformaciones y resultados.

Ejemplos:

```text
Receta ── aplica ── Técnica
```

```text
Técnica ── transforma ── Ingrediente
```

```text
Receta ── produce ── Resultado culinario
```

---

# Relaciones temporales y secuenciales

Representan orden y dependencia temporal.

Ejemplos:

```text
Elaboración A ── precede_a ── Elaboración B
```

```text
Técnica B ── sigue_a ── Técnica A
```

```text
Marinado ── ocurre_antes_de ── Cocción
```

---

# Relaciones taxonómicas

Representan jerarquías, especializaciones y clasificaciones.

Ejemplos:

```text
Arroz basmati ── es_un ── Arroz
```

```text
Confitar ── subtipo_de ── Cocción en grasa
```

```text
Taxonomía ── clasifica ── Ingrediente
```

---

# Relaciones de variación y equivalencia

Representan similitud, versiones, alias o correspondencias.

Ejemplos:

```text
Curry vegetal ── variante_de ── Curry base
```

```text
Coriandro ── alias_de ── Cilantro
```

```text
Unidad doméstica ── equivalente_aproximado_a ── Unidad métrica
```

---

# Relaciones de sustitución y compatibilidad

Representan alternativas, combinaciones o incompatibilidades.

Ejemplos:

```text
Leche de coco ── sustituye_a ── Nata
```

```text
Tomate ── combina_con ── Albahaca
```

```text
Restricción sin gluten ── incompatible_con ── Harina de trigo
```

---

# Relaciones de derivación y procedencia

Representan origen, adaptación o generación.

Ejemplos:

```text
Receta adaptada ── deriva_de ── Receta original
```

```text
Plantilla especializada ── basada_en ── Plantilla general
```

```text
Lista de compra ── generada_desde ── Menú
```

---

# Relaciones organizativas

Representan pertenencia a colecciones, series, catálogos o índices.

Ejemplos:

```text
Receta ── pertenece_a ── Colección
```

```text
Técnica ── incluida_en ── Catálogo de técnicas
```

```text
Ingrediente ── indexado_en ── Índice alfabético
```

---

# Relaciones de restricción

Representan condiciones que limitan o validan otros componentes.

Ejemplos:

```text
Alergia ── excluye ── Ingrediente
```

```text
Tiempo máximo ── limita ── Receta
```

```text
Menú ── satisface ── Restricción dietética
```

---

# Relaciones de representación

Conectan componentes conceptuales con sus representaciones físicas o publicadas.

Ejemplos:

```text
Receta ── representada_por ── Documento Markdown
```

```text
Componente ── documentado_en ── Documento canónico
```

```text
Documento ── publicado_en ── Sitio web
```

Estas relaciones no deberán confundirse con las relaciones internas del dominio culinario.

---

# Relación contextualizada como principio central

Muchas relaciones culinarias requieren información adicional para ser interpretadas correctamente.

El caso más representativo es el uso de ingredientes.

Una representación simplificada sería:

```text
Receta ── utiliza ── Ingrediente
```

Sin embargo, una representación completa puede requerir:

```text
Uso de ingrediente
    │
    ├── receta
    ├── ingrediente
    ├── cantidad
    ├── unidad
    ├── preparación previa
    ├── opcionalidad
    ├── elaboración
    ├── orden
    └── sustituciones
```

Modelo conceptual:

```text
Receta
   │
   └── tiene_uso_de_ingrediente
                │
                ├── referencia_a ── Ingrediente
                ├── cantidad
                ├── unidad
                ├── preparación
                └── opcionalidad
```

Este patrón permite evitar errores como asignar una cantidad fija al ingrediente de forma global.

Por ejemplo, la propiedad:

```text
cantidad: 200 g
```

no pertenece al componente `Harina`.

Pertenece al uso de harina en una receta concreta.

---

# Identidad de las relaciones

No todas las instancias de relación necesitarán identidad propia.

Una triple simple puede representarse sin identificador individual:

```text
REC-0042 utiliza ING-0017
```

Sin embargo, una relación deberá adquirir identidad propia cuando:

- posea múltiples atributos;
- requiera trazabilidad individual;
- tenga ciclo de vida;
- pueda ser citada;
- disponga de procedencia propia;
- participe en otras relaciones;
- represente una observación o decisión.

Ejemplo:

```text
USO-ING-0084
```

podría identificar el uso concreto de cebolla en una receta determinada.

---

# Nomenclatura canónica

Las relaciones deberán utilizar nombres verbales o expresiones verbales.

Ejemplos adecuados:

```text
utiliza

requiere

forma_parte_de

deriva_de

pertenece_a
```

Deberán evitarse nombres excesivamente genéricos como:

```text
relacion

enlace

asociacion

conecta
```

salvo que representen un tipo deliberadamente abstracto.

---

## Forma verbal

La forma canónica deberá permitir leer la relación como una frase.

Ejemplo:

```text
La receta utiliza el ingrediente.
```

```text
La elaboración forma parte de la receta.
```

```text
El ingrediente pertenece a una familia.
```

---

## Consistencia gramatical

Una misma relación deberá conservar siempre:

- persona verbal;
- dirección;
- preposición;
- número;
- significado.

No deberán coexistir arbitrariamente:

```text
forma_parte_de

es_parte_de

pertenece_como_parte_a
```

cuando expresen la misma semántica.

---

# Relaciones canónicas y alias

Cada significado deberá disponer de una única relación canónica.

Ejemplo:

```text
Relación canónica: utiliza
```

Alias posibles:

```text
usa

emplea

incorpora
```

Los alias podrán mejorar la recuperación de información, pero no deberán producir tipos de relación duplicados.

---

# Vocabulario controlado

El conjunto de relaciones reconocidas formará parte del vocabulario controlado del SGCC.

Este vocabulario permitirá:

- validación;
- autocompletado;
- generación de formularios;
- construcción de consultas;
- interoperabilidad;
- traducción;
- entrenamiento y contexto de agentes IA.

La ampliación del vocabulario deberá seguir el procedimiento de gobernanza definido en la parte final de esta especificación.

---

# Separación entre relaciones declaradas e inferidas

El SGCC deberá distinguir claramente entre:

```text
Relación declarada
```

y:

```text
Relación inferida
```

---

## Relación declarada

Ha sido registrada explícitamente en una fuente canónica.

Ejemplo:

```text
REC-0042 utiliza ING-0017
```

---

## Relación inferida

Ha sido obtenida mediante una regla o proceso automático.

Ejemplo:

```text
REC-0042 contiene_alergeno ALG-0003
```

inferida a partir de:

```text
REC-0042 utiliza ING-0017
ING-0017 contiene_alergeno ALG-0003
```

---

## Reglas de separación

Toda relación inferida deberá indicar:

- regla utilizada;
- relaciones de origen;
- fecha de cálculo;
- sistema que la generó;
- nivel de confianza cuando proceda.

Una relación inferida no deberá sobrescribir ni ocultar una relación declarada.

---

# Relaciones negativas

El SGCC podrá representar afirmaciones negativas cuando resulten necesarias.

Ejemplos:

```text
Receta ── no_contiene ── Gluten
```

```text
Equipo ── no_es_compatible_con ── Fuente de calor
```

Las relaciones negativas deberán utilizarse con prudencia.

La ausencia de una relación no implica automáticamente su negación.

Ejemplo:

Que una receta no declare cacahuetes no significa necesariamente que haya sido verificada como libre de cacahuetes.

---

# Relaciones condicionales

Algunas relaciones solo son válidas bajo determinadas condiciones.

Ejemplo:

```text
Yogur ── sustituye_a ── Nata
```

Condiciones:

- en salsas frías;
- con menor contenido graso;
- ajustando la acidez;
- no necesariamente en montados.

Estas condiciones deberán representarse mediante atributos o entidades contextuales.

---

# Relaciones temporales

Algunas relaciones tienen validez limitada en el tiempo.

Ejemplo:

```text
Ingrediente ── disponible_en ── Temporada
```

```text
Menú ── vigente_durante ── Semana
```

```text
Componente ── sustituido_por ── Componente nuevo
```

Una relación temporal podrá incluir:

- fecha de inicio;
- fecha de fin;
- periodo;
- estado de vigencia;
- recurrencia.

---

# Relaciones dependientes del contexto

Una misma pareja de componentes puede mantener diferentes relaciones según el contexto.

Ejemplo:

```text
Mantequilla ── sustituye_a ── Aceite
```

puede ser válida en:

- salteados;
- salsas;
- masas concretas.

Pero no necesariamente en:

- frituras profundas;
- dietas veganas;
- preparaciones que requieran un punto de humo elevado.

El contexto deberá formar parte explícita de la relación cuando altere su validez.

---

# Relación y evidencia

Las relaciones especialmente relevantes podrán asociarse a evidencia.

Ejemplos:

- fuente documental;
- prueba culinaria;
- referencia bibliográfica;
- observación;
- cálculo;
- validación humana;
- resultado experimental.

Modelo:

```text
Relación
   │
   └── respaldada_por ── Evidencia
```

La evidencia será especialmente importante para:

- seguridad alimentaria;
- nutrición;
- sustituciones;
- compatibilidades;
- recomendaciones;
- conocimiento generado automáticamente.

---

# Relación y procedencia

Toda relación susceptible de controversia, inferencia o actualización deberá poder indicar su procedencia.

Modelo:

```text
Relación
    │
    ├── fuente
    ├── autor
    ├── fecha
    ├── método
    └── confianza
```

La procedencia permite distinguir entre:

- conocimiento canónico;
- conocimiento importado;
- hipótesis;
- recomendación;
- inferencia automática;
- propuesta generada por IA.

---

# Relación y ciclo de vida

Las relaciones podrán evolucionar.

Modelo general:

```text
Borrador

↓

En revisión

↓

Estable

↓

Obsoleta

↓

Archivada
```

La obsolescencia de una relación no implica necesariamente la obsolescencia de los componentes conectados.

Ejemplo:

Una relación de sustitución puede quedar obsoleta por una revisión técnica, mientras que ambos ingredientes continúan siendo válidos.

---

# Conformidad preliminar

Una relación será preliminarmente conforme cuando:

- utilice un tipo reconocido;
- conecte componentes compatibles con su dominio y rango;
- respete la dirección canónica;
- cumpla sus cardinalidades;
- incluya los atributos obligatorios;
- conserve procedencia cuando sea necesaria;
- no contradiga restricciones conocidas;
- pueda interpretarse sin ambigüedad crítica.

Las reglas completas de conformidad y validación se desarrollarán en las siguientes partes de esta especificación.

---

# Catálogo normativo de relaciones

Esta sección define los tipos de relaciones reconocidos inicialmente por el SGCC.

Cada relación se documenta mediante:

- finalidad;
- definición normativa;
- dominio;
- rango;
- dirección;
- cardinalidad;
- relación inversa;
- características lógicas;
- atributos contextuales;
- restricciones;
- ejemplos válidos;
- contraejemplos.

El catálogo constituye el vocabulario relacional base de NovaCoquinaria.

Su objetivo no es enumerar cualquier verbo posible, sino establecer un conjunto controlado, preciso y reutilizable de relaciones semánticas.

---

# Criterios generales del catálogo

Las relaciones incluidas en este catálogo deberán cumplir los siguientes criterios:

- expresar una semántica diferenciada;
- evitar duplicidades terminológicas;
- disponer de dominio y rango identificables;
- poder utilizarse en más de una instancia;
- permitir validación;
- ser compatibles con la ontología;
- mantener una dirección canónica;
- admitir representación tecnológica independiente.

Las relaciones deberán utilizar siempre su nombre canónico.

Los sinónimos, traducciones y variantes lingüísticas podrán registrarse como alias, pero no deberán convertirse en relaciones distintas cuando expresen el mismo significado.

---

# Estructura de identificación

Los tipos de relación utilizarán identificadores persistentes con el formato:

```text
REL-XXXX
```

Ejemplo:

```text
REL-0001
```

La numeración incluida en esta especificación representa una propuesta inicial del catálogo.

La asignación definitiva deberá validarse contra el registro global de identificadores del SGCC antes de su integración.

---

# Familia de relaciones estructurales

Las relaciones estructurales expresan composición, agregación, inclusión y pertenencia funcional entre componentes.

---

# REL-0001 — contiene

## Finalidad

Expresar que un componente agrupa o incorpora uno o varios componentes dentro de su estructura.

---

## Definición normativa

`contiene` indica que el componente origen actúa como contenedor estructural, funcional u organizativo de otro componente.

La relación no determina por sí sola si existe dependencia fuerte del ciclo de vida.

Para expresar dependencia estructural deberá utilizarse, cuando corresponda, `compuesto_por` o su inversa `forma_parte_de`.

---

## Dominio

- Receta;
- Elaboración;
- Base culinaria;
- Menú;
- Colección;
- Serie;
- Catálogo;
- Taxonomía;
- Documento estructurado.

---

## Rango

- Componente;
- Documento;
- Entrada;
- Categoría;
- Resultado;
- Elemento organizativo.

---

## Dirección

Dirigida.

```text
Contenedor ── contiene ── Contenido
```

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

Un componente podrá contener múltiples elementos.

Un mismo elemento podrá estar contenido en varios agregados cuando la relación no implique composición exclusiva.

---

## Relación inversa

```text
contenido_en
```

---

## Características lógicas

- simétrica: no;
- transitiva: no por defecto;
- reflexiva: no;
- funcional: no.

La transitividad no deberá asumirse automáticamente.

Si una colección contiene un menú y el menú contiene una receta, no deberá inferirse sin regla explícita que la colección contiene directamente la receta.

---

## Atributos contextuales

- orden;
- rol;
- obligatoriedad;
- fecha de incorporación;
- contexto;
- visibilidad.

---

## Restricciones

No deberá utilizarse `contiene` cuando exista una relación más precisa, como:

- `utiliza`;
- `incluye_en_menu`;
- `compuesto_por`;
- `clasifica`;
- `agrupa`.

---

## Ejemplo válido

```text
Colección de cocina japonesa ── contiene ── Curry japonés
```

---

## Contraejemplo

```text
Receta ── contiene ── Sartén
```

En este caso la relación correcta sería:

```text
Receta ── requiere ── Sartén
```

---

# REL-0002 — contenido_en

## Finalidad

Expresar la relación inversa de `contiene`.

---

## Definición normativa

`contenido_en` indica que un componente forma parte del conjunto organizado por otro, sin afirmar necesariamente dependencia fuerte.

---

## Dominio

- Componente;
- Documento;
- Entrada;
- Categoría;
- Resultado.

---

## Rango

- Receta;
- Elaboración;
- Base culinaria;
- Menú;
- Colección;
- Serie;
- Catálogo;
- Taxonomía;
- Documento estructurado.

---

## Dirección

Dirigida.

```text
Contenido ── contenido_en ── Contenedor
```

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

---

## Relación inversa

```text
contiene
```

---

## Características lógicas

- simétrica: no;
- transitiva: no por defecto;
- reflexiva: no.

---

## Ejemplo válido

```text
Curry japonés ── contenido_en ── Colección de cocina japonesa
```

---

# REL-0003 — compuesto_por

## Finalidad

Expresar que un componente se construye mediante partes que contribuyen directamente a su estructura o función.

---

## Definición normativa

`compuesto_por` representa una relación de composición entre un componente agregado y sus partes.

La relación implica una dependencia estructural más fuerte que `contiene`.

---

## Dominio

- Receta;
- Elaboración;
- Base culinaria;
- Menú;
- Plantilla;
- Proceso;
- Resultado compuesto.

---

## Rango

- Ingrediente;
- Elaboración;
- Base culinaria;
- Técnica;
- Receta;
- Sección;
- Resultado parcial.

---

## Dirección

Dirigida.

```text
Todo ── compuesto_por ── Parte
```

---

## Cardinalidad

```text
Origen: 1..*
Destino: 0..*
```

Un componente compuesto deberá poseer al menos una parte estructural.

---

## Relación inversa

```text
forma_parte_de
```

---

## Características lógicas

- simétrica: no;
- transitiva: no por defecto;
- reflexiva: no;
- funcional: no.

La transitividad deberá definirse de manera específica según el tipo.

---

## Atributos contextuales

- orden;
- rol;
- obligatoriedad;
- proporción;
- fase;
- nivel de composición;
- reutilización permitida.

---

## Restricciones

La composición no deberá utilizarse para expresar:

- pertenencia a una colección;
- dependencia técnica;
- mera referencia documental;
- clasificación taxonómica.

---

## Ejemplo válido

```text
Receta de curry ── compuesto_por ── Salsa de curry
```

---

## Contraejemplo

```text
Colección de invierno ── compuesto_por ── Lentejas estofadas
```

Una colección agrega componentes, pero no está estructuralmente compuesta por ellos.

La relación correcta sería:

```text
Colección de invierno ── contiene ── Lentejas estofadas
```

---

# REL-0004 — forma_parte_de

## Finalidad

Expresar que un componente constituye una parte estructural o funcional de otro.

---

## Definición normativa

`forma_parte_de` es la relación inversa de `compuesto_por`.

Indica una integración funcional o estructural más fuerte que la mera pertenencia organizativa.

---

## Dominio

- Ingrediente contextualizado;
- Elaboración;
- Base culinaria;
- Técnica contextualizada;
- Receta;
- Resultado parcial;
- Sección.

---

## Rango

- Receta;
- Elaboración;
- Base culinaria;
- Menú;
- Plantilla;
- Proceso;
- Resultado compuesto.

---

## Dirección

Dirigida.

```text
Parte ── forma_parte_de ── Todo
```

---

## Cardinalidad

```text
Origen: 0..*
Destino: 1..*
```

---

## Relación inversa

```text
compuesto_por
```

---

## Características lógicas

- simétrica: no;
- transitiva: condicionada;
- reflexiva: no.

La transitividad únicamente podrá inferirse cuando la semántica del tipo y las reglas ontológicas lo permitan.

---

## Ejemplo válido

```text
Salsa de curry ── forma_parte_de ── Curry japonés
```

---

## Contraejemplo

```text
Curry japonés ── forma_parte_de ── Cocina japonesa
```

En este caso se trata de clasificación o pertenencia temática, no de composición.

---

# REL-0005 — incluye

## Finalidad

Expresar incorporación planificada u organizativa de un componente dentro de otro.

---

## Definición normativa

`incluye` se utiliza cuando el origen selecciona, incorpora o considera uno o varios componentes como parte de una estructura organizativa, sin implicar necesariamente composición fuerte.

---

## Dominio

- Menú;
- Planificación;
- Serie;
- Colección;
- Catálogo;
- Índice;
- Documento de referencia.

---

## Rango

- Receta;
- Elaboración;
- Menú;
- Componente;
- Documento;
- Actividad planificada.

---

## Dirección

Dirigida.

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

---

## Relación inversa

```text
incluido_en
```

---

## Características lógicas

- simétrica: no;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- orden;
- función;
- prioridad;
- fecha;
- posición;
- obligatoriedad;
- cantidad de repeticiones.

---

## Ejemplo válido

```text
Menú semanal ── incluye ── Curry japonés
```

---

# REL-0006 — incluido_en

## Finalidad

Expresar la relación inversa de `incluye`.

---

## Definición normativa

Indica que un componente ha sido seleccionado o incorporado dentro de una estructura organizativa o planificada.

---

## Dominio

- Receta;
- Elaboración;
- Menú;
- Componente;
- Documento;
- Actividad planificada.

---

## Rango

- Menú;
- Planificación;
- Serie;
- Colección;
- Catálogo;
- Índice;
- Documento de referencia.

---

## Dirección

Dirigida.

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

---

## Relación inversa

```text
incluye
```

---

# Familia de relaciones de uso y dependencia

Estas relaciones representan el empleo, la necesidad o la dependencia funcional entre componentes.

---

# REL-0010 — utiliza

## Finalidad

Expresar que un componente emplea otro durante su composición, ejecución o funcionamiento.

---

## Definición normativa

`utiliza` indica que el componente origen incorpora, consume o emplea el componente destino en un contexto concreto.

Es una de las relaciones centrales del dominio culinario.

---

## Dominio

- Receta;
- Elaboración;
- Base culinaria;
- Menú;
- Plantilla;
- Técnica;
- Planificación.

---

## Rango

- Ingrediente;
- Base culinaria;
- Elaboración;
- Técnica;
- Equipo;
- Unidad;
- Plantilla;
- Recurso.

---

## Dirección

Dirigida.

```text
Usuario ── utiliza ── Recurso
```

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

Para tipos específicos podrán definirse mínimos más estrictos.

Por ejemplo:

```text
Receta utiliza 1..* ingredientes o elaboraciones.
```

---

## Relación inversa

```text
es_utilizado_por
```

---

## Características lógicas

- simétrica: no;
- transitiva: no;
- reflexiva: no;
- funcional: no.

---

## Atributos contextuales

- cantidad;
- unidad;
- finalidad;
- orden;
- opcionalidad;
- fase;
- preparación previa;
- proporción;
- sustitución admitida;
- observaciones.

---

## Restricciones

Cuando la relación necesite cantidad, unidad, preparación previa u otros atributos complejos deberá modelarse mediante una relación contextualizada o entidad asociativa.

---

## Ejemplo válido

```text
Curry japonés ── utiliza ── Cebolla
```

Con contexto:

```text
cantidad: 250
unidad: gramos
preparación: cortada en pluma
fase: sofrito
```

---

## Contraejemplo

```text
Cebolla ── utiliza ── Curry japonés
```

La dirección es incorrecta.

---

# REL-0011 — es_utilizado_por

## Finalidad

Expresar la relación inversa de `utiliza`.

---

## Definición normativa

Indica que un componente es empleado por otro durante su ejecución, composición o funcionamiento.

---

## Dominio

- Ingrediente;
- Base culinaria;
- Elaboración;
- Técnica;
- Equipo;
- Unidad;
- Plantilla;
- Recurso.

---

## Rango

- Receta;
- Elaboración;
- Base culinaria;
- Menú;
- Plantilla;
- Técnica;
- Planificación.

---

## Dirección

Dirigida.

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

---

## Relación inversa

```text
utiliza
```

---

# REL-0012 — requiere

## Finalidad

Expresar una necesidad funcional, técnica o estructural.

---

## Definición normativa

`requiere` indica que el componente origen necesita el componente destino para poder ejecutarse, existir de acuerdo con su definición o alcanzar el resultado esperado.

La necesidad podrá ser obligatoria o condicional.

---

## Dominio

- Receta;
- Técnica;
- Elaboración;
- Base culinaria;
- Plantilla;
- Planificación;
- Proceso;
- Esquema.

---

## Rango

- Ingrediente;
- Equipo;
- Técnica;
- Base culinaria;
- Elaboración;
- Condición;
- Tiempo;
- Temperatura;
- Propiedad;
- Esquema;
- Permiso.

---

## Dirección

Dirigida.

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

---

## Relación inversa

```text
es_requerido_por
```

---

## Características lógicas

- simétrica: no;
- transitiva: no por defecto;
- reflexiva: no.

---

## Atributos contextuales

- obligatoriedad;
- condición;
- nivel de necesidad;
- fase;
- alternativa;
- justificación.

---

## Restricciones

Deberá distinguirse entre:

```text
requiere
```

y:

```text
recomienda
```

Una recomendación no constituye una necesidad.

---

## Ejemplo válido

```text
Confitar ── requiere ── Control de temperatura
```

---

## Contraejemplo

```text
Receta ── requiere ── Cocina japonesa
```

La cocina japonesa es una clasificación o contexto, no una necesidad funcional.

---

# REL-0013 — es_requerido_por

## Finalidad

Expresar la relación inversa de `requiere`.

---

## Definición normativa

Indica que un componente constituye una necesidad para otro componente.

---

## Dominio

- Ingrediente;
- Equipo;
- Técnica;
- Base culinaria;
- Elaboración;
- Condición;
- Tiempo;
- Temperatura;
- Propiedad;
- Esquema;
- Permiso.

---

## Rango

- Receta;
- Técnica;
- Elaboración;
- Base culinaria;
- Plantilla;
- Planificación;
- Proceso;
- Esquema.

---

## Relación inversa

```text
requiere
```

---

# REL-0014 — depende_de

## Finalidad

Expresar una dependencia funcional, lógica, temporal o estructural.

---

## Definición normativa

`depende_de` indica que el estado, existencia, ejecución o resultado del componente origen está condicionado por el componente destino.

La dependencia deberá ser más significativa que una simple utilización.

---

## Dominio

- Elaboración;
- Receta;
- Menú;
- Planificación;
- Componente derivado;
- Documento generado;
- Proceso;
- Resultado.

---

## Rango

- Base culinaria;
- Elaboración;
- Receta;
- Menú;
- Componente fuente;
- Proceso;
- Condición;
- Recurso;
- Documento.

---

## Dirección

Dirigida.

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

---

## Relación inversa

```text
es_dependencia_de
```

---

## Características lógicas

- simétrica: no;
- transitiva: no por defecto;
- reflexiva: no.

La transitividad podrá habilitarse únicamente para contextos concretos.

---

## Atributos contextuales

- tipo de dependencia;
- obligatoriedad;
- fase;
- condición;
- criticidad;
- fecha de vigencia.

---

## Ejemplo válido

```text
Salsa final ── depende_de ── Fondo oscuro
```

---

## Contraejemplo

```text
Receta ── depende_de ── Colección
```

La pertenencia a una colección no suele constituir dependencia funcional.

---

# REL-0015 — es_dependencia_de

## Finalidad

Expresar la relación inversa de `depende_de`.

---

## Definición normativa

Indica que el componente origen condiciona la ejecución, existencia o resultado de otro componente.

---

## Relación inversa

```text
depende_de
```

---

# REL-0016 — recomienda

## Finalidad

Expresar una conveniencia no obligatoria.

---

## Definición normativa

`recomienda` indica que el componente origen sugiere el uso, consulta o aplicación del destino para mejorar un resultado o facilitar una operación.

No implica obligatoriedad.

---

## Dominio

- Receta;
- Técnica;
- Plantilla;
- Menú;
- Guía;
- Sistema de recomendación;
- Restricción;
- Resultado esperado.

---

## Rango

- Equipo;
- Ingrediente;
- Técnica;
- Base;
- Receta;
- Acción;
- Documento;
- Condición.

---

## Dirección

Dirigida.

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

---

## Relación inversa

```text
es_recomendado_por
```

---

## Características lógicas

- simétrica: no;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- motivo;
- prioridad;
- confianza;
- contexto;
- alternativa;
- fuente.

---

## Ejemplo válido

```text
Receta de asado ── recomienda ── Termómetro de cocina
```

---

# Familia de relaciones de proceso y transformación

Estas relaciones representan acciones, transformaciones, resultados y generación de nuevos componentes.

---

# REL-0020 — aplica

## Finalidad

Expresar que un componente utiliza formalmente una técnica, regla, criterio o proceso.

---

## Definición normativa

`aplica` indica que el componente origen ejecuta o incorpora el comportamiento definido por el componente destino.

---

## Dominio

- Receta;
- Elaboración;
- Base culinaria;
- Proceso;
- Plantilla;
- Validación;
- Regla.

---

## Rango

- Técnica;
- Regla;
- Restricción;
- Método;
- Esquema;
- Criterio.

---

## Dirección

Dirigida.

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

---

## Relación inversa

```text
es_aplicado_en
```

---

## Características lógicas

- simétrica: no;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- fase;
- orden;
- condición;
- intensidad;
- duración;
- parámetros.

---

## Ejemplo válido

```text
Salsa holandesa ── aplica ── Emulsión
```

---

## Contraejemplo

```text
Emulsión ── aplica ── Salsa holandesa
```

La dirección correcta sería:

```text
Emulsión ── es_aplicada_en ── Salsa holandesa
```

---

# REL-0021 — es_aplicado_en

## Finalidad

Expresar la relación inversa de `aplica`.

---

## Definición normativa

Indica que una técnica, regla o método se utiliza dentro de un componente o proceso.

---

## Relación inversa

```text
aplica
```

---

# REL-0022 — transforma

## Finalidad

Expresar que una técnica, elaboración o proceso modifica el estado de otro componente.

---

## Definición normativa

`transforma` indica que el origen produce un cambio físico, químico, estructural, sensorial o funcional sobre el destino.

---

## Dominio

- Técnica;
- Elaboración;
- Proceso;
- Receta;
- Operación culinaria.

---

## Rango

- Ingrediente;
- Base culinaria;
- Elaboración;
- Mezcla;
- Estado culinario;
- Resultado intermedio.

---

## Dirección

Dirigida.

```text
Transformador ── transforma ── Elemento transformado
```

---

## Cardinalidad

```text
Origen: 0..*
Destino: 1..*
```

---

## Relación inversa

```text
es_transformado_por
```

---

## Características lógicas

- simétrica: no;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- estado inicial;
- estado final;
- duración;
- temperatura;
- intensidad;
- condiciones;
- resultado esperado.

---

## Restricciones

No deberá utilizarse para expresar simple uso.

Una receta puede utilizar una especia sin transformarla de forma relevante.

---

## Ejemplo válido

```text
Fermentación ── transforma ── Masa
```

---

# REL-0023 — es_transformado_por

## Finalidad

Expresar la relación inversa de `transforma`.

---

## Definición normativa

Indica que un componente cambia de estado mediante una técnica, proceso o elaboración.

---

## Relación inversa

```text
transforma
```

---

# REL-0024 — produce

## Finalidad

Expresar que un componente genera un resultado culinario identificable.

---

## Definición normativa

`produce` conecta una receta, elaboración o proceso con el resultado que se obtiene tras su ejecución.

---

## Dominio

- Receta;
- Elaboración;
- Base culinaria;
- Técnica;
- Proceso;
- Planificación ejecutada.

---

## Rango

- Resultado culinario;
- Base culinaria;
- Elaboración;
- Producto;
- Subproducto;
- Residuo;
- Rendimiento.

---

## Dirección

Dirigida.

```text
Proceso ── produce ── Resultado
```

---

## Cardinalidad

```text
Origen: 1..*
Destino: 0..*
```

Una receta estable deberá producir al menos un resultado principal.

---

## Relación inversa

```text
es_producido_por
```

---

## Características lógicas

- simétrica: no;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- rendimiento;
- cantidad;
- unidad;
- calidad esperada;
- estado;
- tolerancias;
- fecha de producción.

---

## Ejemplo válido

```text
Receta de caldo ── produce ── Caldo vegetal
```

---

# REL-0025 — es_producido_por

## Finalidad

Expresar la relación inversa de `produce`.

---

## Definición normativa

Indica que un resultado, producto o elaboración se obtiene mediante otro componente.

---

## Relación inversa

```text
produce
```

---

# REL-0026 — genera

## Finalidad

Expresar creación automática, derivada, documental o computacional.

---

## Definición normativa

`genera` indica que el origen crea una representación, cálculo, componente derivado o salida mediante un proceso definido.

Se diferencia de `produce` porque no está limitada a resultados culinarios.

---

## Dominio

- Menú;
- Planificación;
- Esquema;
- Plantilla;
- Documento fuente;
- Herramienta;
- Proceso automático;
- Consulta;
- Componente.

---

## Rango

- Lista de compra;
- Documento;
- Representación;
- Índice;
- Catálogo;
- Resultado calculado;
- Componente derivado;
- Vista.

---

## Dirección

Dirigida.

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

---

## Relación inversa

```text
generado_por
```

---

## Características lógicas

- simétrica: no;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- método;
- herramienta;
- versión;
- fecha;
- parámetros;
- reproducibilidad;
- confianza.

---

## Ejemplo válido

```text
Menú semanal ── genera ── Lista de compra
```

---

# REL-0027 — generado_por

## Finalidad

Expresar la relación inversa de `genera`.

---

## Definición normativa

Indica que un activo derivado ha sido creado mediante otro componente, proceso o herramienta.

---

## Relación inversa

```text
genera
```

---

# REL-0028 — convierte_en

## Finalidad

Expresar una transformación cuyo resultado constituye otra entidad identificable.

---

## Definición normativa

`convierte_en` indica que el componente origen pasa a un estado o componente destino mediante una operación o proceso.

A diferencia de `transforma`, esta relación conecta explícitamente el estado o entidad inicial con el resultado final.

---

## Dominio

- Ingrediente;
- Elaboración;
- Base culinaria;
- Estado culinario;
- Documento;
- Representación.

---

## Rango

- Elaboración;
- Base culinaria;
- Resultado;
- Estado culinario;
- Representación.

---

## Dirección

Dirigida.

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

---

## Relación inversa

```text
procede_de_transformacion
```

---

## Atributos contextuales

- técnica;
- proceso;
- condiciones;
- duración;
- temperatura;
- rendimiento.

---

## Ejemplo válido

```text
Nata ── convierte_en ── Mantequilla
```

Contexto:

```text
técnica: batido prolongado
```

---

# Familia de relaciones temporales y secuenciales

Estas relaciones expresan orden, simultaneidad, duración y dependencia temporal.

---

# REL-0030 — precede_a

## Finalidad

Expresar que un componente ocurre o debe ejecutarse antes que otro.

---

## Definición normativa

`precede_a` indica un orden temporal o lógico directo o parcial.

No implica necesariamente que ambos elementos sean consecutivos.

---

## Dominio

- Técnica contextualizada;
- Elaboración;
- Paso;
- Proceso;
- Evento;
- Receta;
- Menú;
- Estado.

---

## Rango

- Técnica contextualizada;
- Elaboración;
- Paso;
- Proceso;
- Evento;
- Receta;
- Menú;
- Estado.

---

## Dirección

Dirigida.

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

---

## Relación inversa

```text
sigue_a
```

---

## Características lógicas

- simétrica: no;
- transitiva: sí, cuando representa orden temporal estricto;
- reflexiva: no;
- asimétrica: sí.

---

## Atributos contextuales

- separación temporal;
- obligatoriedad;
- condición;
- orden;
- tolerancia;
- momento relativo.

---

## Restricciones

No deberá formar ciclos cuando represente un orden estricto.

Ejemplo inválido:

```text
A precede_a B
B precede_a A
```

---

## Ejemplo válido

```text
Marinado ── precede_a ── Cocción
```

---

# REL-0031 — sigue_a

## Finalidad

Expresar la relación inversa de `precede_a`.

---

## Definición normativa

Indica que un componente ocurre o debe ejecutarse después de otro.

---

## Características lógicas

- simétrica: no;
- transitiva: sí en orden estricto;
- reflexiva: no;
- asimétrica: sí.

---

## Relación inversa

```text
precede_a
```

---

# REL-0032 — inmediatamente_precede_a

## Finalidad

Expresar orden consecutivo sin elementos intermedios.

---

## Definición normativa

Indica que el origen debe aparecer directamente antes del destino dentro de una secuencia concreta.

---

## Dominio

- Paso;
- Técnica contextualizada;
- Elaboración;
- Evento.

---

## Rango

- Paso;
- Técnica contextualizada;
- Elaboración;
- Evento.

---

## Dirección

Dirigida.

---

## Cardinalidad

En una secuencia lineal:

```text
Origen máximo: 1 sucesor inmediato
Destino máximo: 1 predecesor inmediato
```

---

## Relación inversa

```text
inmediatamente_sigue_a
```

---

## Características lógicas

- transitiva: no;
- simétrica: no;
- reflexiva: no;
- asimétrica: sí.

---

## Ejemplo válido

```text
Apagar el fuego ── inmediatamente_precede_a ── Incorporar el miso
```

---

# REL-0033 — ocurre_durante

## Finalidad

Expresar que una acción, técnica o evento sucede dentro del intervalo de otro proceso.

---

## Definición normativa

`ocurre_durante` indica inclusión temporal.

---

## Dominio

- Técnica;
- Evento;
- Acción;
- Observación;
- Estado.

---

## Rango

- Elaboración;
- Proceso;
- Receta;
- Periodo;
- Servicio;
- Planificación.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
contiene_temporalmente
```

---

## Características lógicas

- simétrica: no;
- transitiva: condicionada;
- reflexiva: no.

---

## Atributos contextuales

- inicio relativo;
- fin relativo;
- duración;
- condición;
- repetición.

---

## Ejemplo válido

```text
Remover ── ocurre_durante ── Reducción de la salsa
```

---

# REL-0034 — simultaneo_a

## Finalidad

Expresar que dos eventos o procesos ocurren al mismo tiempo o con solapamiento relevante.

---

## Definición normativa

`simultaneo_a` indica coincidencia temporal total o suficiente dentro del contexto.

---

## Dominio

- Evento;
- Técnica contextualizada;
- Elaboración;
- Proceso;
- Acción.

---

## Rango

- Evento;
- Técnica contextualizada;
- Elaboración;
- Proceso;
- Acción.

---

## Dirección

No dirigida conceptualmente.

Podrá almacenarse en una única dirección canónica.

---

## Relación inversa

La propia relación.

---

## Características lógicas

- simétrica: sí;
- transitiva: no necesariamente;
- reflexiva: no en el modelo operativo.

---

## Atributos contextuales

- grado de solapamiento;
- intervalo;
- tolerancia;
- sincronización requerida.

---

## Ejemplo válido

```text
Cocer el arroz ── simultaneo_a ── Preparar la salsa
```

---

# REL-0035 — vigente_durante

## Finalidad

Expresar el periodo temporal durante el que una entidad, relación o planificación es válida.

---

## Definición normativa

`vigente_durante` conecta un componente con el intervalo o periodo en el que debe considerarse activo o aplicable.

---

## Dominio

- Menú;
- Planificación;
- Restricción;
- Relación;
- Documento;
- Regla;
- Estado;
- Recomendación.

---

## Rango

- Fecha;
- Intervalo;
- Temporada;
- Semana;
- Periodo.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
periodo_de_vigencia_de
```

---

## Atributos contextuales

- fecha inicial;
- fecha final;
- recurrencia;
- zona horaria;
- condición de activación.

---

## Ejemplo válido

```text
Menú de Navidad ── vigente_durante ── Diciembre de 2026
```

---

# Familia de relaciones taxonómicas y conceptuales

Estas relaciones representan clasificación, jerarquía, generalización y especialización.

---

# REL-0040 — es_un

## Finalidad

Expresar pertenencia ontológica de una instancia o subtipo a una categoría más general.

---

## Definición normativa

`es_un` indica que el componente origen constituye una instancia o especialización válida del destino.

---

## Dominio

- Componente;
- Tipo especializado;
- Concepto;
- Ingrediente;
- Técnica;
- Receta;
- Equipo;
- Restricción.

---

## Rango

- Tipo de componente;
- Categoría conceptual;
- Clase ontológica;
- Concepto general.

---

## Dirección

Dirigida.

```text
Específico ── es_un ── General
```

---

## Cardinalidad

```text
Origen: 1..*
Destino: 0..*
```

Un componente podrá pertenecer a varias clases compatibles cuando la ontología lo permita.

---

## Relación inversa

```text
tiene_instancia
```

o, para tipos:

```text
tiene_subtipo
```

La inversa concreta dependerá del nivel ontológico.

---

## Características lógicas

- simétrica: no;
- transitiva: sí;
- reflexiva: no en instancias;
- asimétrica: sí.

---

## Restricciones

No deberá confundirse con pertenencia organizativa.

Ejemplo:

```text
Curry japonés es_un Receta
```

no equivale a:

```text
Curry japonés pertenece_a Colección japonesa
```

---

## Ejemplo válido

```text
Arroz basmati ── es_un ── Arroz de grano largo
```

---

# REL-0041 — subtipo_de

## Finalidad

Expresar especialización entre tipos o clases conceptuales.

---

## Definición normativa

`subtipo_de` indica que el origen hereda la semántica general del destino y añade propiedades o restricciones específicas.

---

## Dominio

- Tipo de componente;
- Clase ontológica;
- Categoría formal;
- Técnica especializada;
- Restricción especializada.

---

## Rango

- Tipo de componente;
- Clase ontológica;
- Categoría formal.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
superclase_de
```

o:

```text
tiene_subtipo
```

---

## Características lógicas

- simétrica: no;
- transitiva: sí;
- reflexiva: no;
- asimétrica: sí.

---

## Restricciones

No deberán existir ciclos.

Ejemplo inválido:

```text
A subtipo_de B
B subtipo_de A
```

---

## Ejemplo válido

```text
Ingrediente fermentado ── subtipo_de ── Ingrediente
```

---

# REL-0042 — clasifica

## Finalidad

Expresar que una taxonomía, categoría o criterio organiza otros componentes.

---

## Definición normativa

`clasifica` indica que el origen establece una categoría, taxonomía o sistema de organización aplicable al destino.

---

## Dominio

- Taxonomía;
- Categoría;
- Catálogo;
- Criterio de clasificación;
- Esquema.

---

## Rango

- Componente;
- Tipo de componente;
- Documento;
- Concepto;
- Colección.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
clasificado_por
```

---

## Características lógicas

- simétrica: no;
- transitiva: no;
- reflexiva: no.

---

## Ejemplo válido

```text
Taxonomía de técnicas ── clasifica ── Confitar
```

---

# REL-0043 — pertenece_a_categoria

## Finalidad

Expresar que un componente ha sido incluido en una categoría taxonómica concreta.

---

## Definición normativa

`pertenece_a_categoria` conecta una instancia con una categoría de clasificación.

---

## Dominio

- Componente;
- Documento;
- Relación;
- Concepto.

---

## Rango

- Categoría;
- Clase;
- Familia;
- Etiqueta controlada;
- Nodo taxonómico.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
tiene_miembro_clasificado
```

---

## Características lógicas

- simétrica: no;
- transitiva: condicionada por la jerarquía;
- reflexiva: no.

---

## Ejemplo válido

```text
Miso blanco ── pertenece_a_categoria ── Condimentos fermentados
```

---

# REL-0044 — especializa

## Finalidad

Expresar que un componente, plantilla o esquema concreta otro más general.

---

## Definición normativa

`especializa` indica que el origen restringe, amplía o adapta el destino para un contexto más específico.

---

## Dominio

- Plantilla;
- Esquema;
- Tipo;
- Taxonomía;
- Regla;
- Componente conceptual.

---

## Rango

- Plantilla;
- Esquema;
- Tipo;
- Taxonomía;
- Regla;
- Componente conceptual.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
generalizado_por
```

---

## Características lógicas

- simétrica: no;
- transitiva: sí cuando la jerarquía sea formal;
- reflexiva: no.

---

## Ejemplo válido

```text
Plantilla de curry tailandés ── especializa ── Plantilla de curry
```

---

# Familia de relaciones de variación, equivalencia y similitud

Estas relaciones expresan correspondencias, versiones, alias y grados de semejanza.

---

# REL-0050 — variante_de

## Finalidad

Expresar que un componente constituye una realización alternativa de otro componente base o canónico.

---

## Definición normativa

`variante_de` indica que el origen conserva la identidad estructural o conceptual principal del destino, pero introduce cambios relevantes.

---

## Dominio

- Receta;
- Base culinaria;
- Plantilla;
- Técnica;
- Menú;
- Documento;
- Componente.

---

## Rango

- Receta;
- Base culinaria;
- Plantilla;
- Técnica;
- Menú;
- Documento;
- Componente.

---

## Dirección

Dirigida.

```text
Variante ── variante_de ── Base
```

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

---

## Relación inversa

```text
tiene_variante
```

---

## Características lógicas

- simétrica: no;
- transitiva: no por defecto;
- reflexiva: no.

---

## Atributos contextuales

- diferencias;
- motivo;
- región;
- restricción;
- fecha;
- autor;
- grado de desviación.

---

## Restricciones

Una variante no deberá tratarse como equivalente completa.

---

## Ejemplo válido

```text
Curry japonés vegetariano ── variante_de ── Curry japonés
```

---

# REL-0051 — tiene_variante

## Finalidad

Expresar la relación inversa de `variante_de`.

---

## Relación inversa

```text
variante_de
```

---

# REL-0052 — equivalente_a

## Finalidad

Expresar equivalencia semántica definida entre dos componentes.

---

## Definición normativa

`equivalente_a` indica que dos componentes pueden considerarse intercambiables dentro del ámbito declarado.

La equivalencia deberá especificar su contexto.

---

## Dominio

- Concepto;
- Unidad;
- Término;
- Componente;
- Representación;
- Ingrediente contextualizado.

---

## Rango

- Concepto;
- Unidad;
- Término;
- Componente;
- Representación;
- Ingrediente contextualizado.

---

## Dirección

No dirigida conceptualmente.

---

## Relación inversa

La propia relación.

---

## Características lógicas

- simétrica: sí;
- transitiva: condicionada;
- reflexiva: no se almacena normalmente.

---

## Atributos contextuales

- ámbito;
- precisión;
- condición;
- idioma;
- región;
- proporción;
- fuente.

---

## Restricciones

No deberá utilizarse cuando exista únicamente similitud o sustitución parcial.

---

## Ejemplo válido

```text
1000 mililitros ── equivalente_a ── 1 litro
```

---

## Contraejemplo

```text
Leche de coco ── equivalente_a ── Nata
```

Normalmente se trataría de sustitución contextual, no de equivalencia.

---

# REL-0053 — equivalente_aproximado_a

## Finalidad

Expresar equivalencia no exacta pero útil en un contexto culinario.

---

## Definición normativa

Indica una correspondencia aproximada, normalmente sujeta a tolerancia, densidad, utensilio o convención.

---

## Dominio

- Unidad;
- Cantidad;
- Medida doméstica;
- Ingrediente contextualizado.

---

## Rango

- Unidad;
- Cantidad;
- Medida doméstica;
- Ingrediente contextualizado.

---

## Dirección

No dirigida conceptualmente.

---

## Relación inversa

La propia relación.

---

## Características lógicas

- simétrica: sí;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- tolerancia;
- ingrediente;
- densidad;
- utensilio;
- región;
- confianza.

---

## Ejemplo válido

```text
1 cucharada de agua ── equivalente_aproximado_a ── 15 mililitros
```

---

# REL-0054 — alias_de

## Finalidad

Expresar que un término o nombre alternativo remite a la misma entidad canónica.

---

## Definición normativa

`alias_de` indica que el origen constituye una denominación alternativa del destino, no una entidad diferente.

---

## Dominio

- Término;
- Nombre alternativo;
- Etiqueta;
- Identificador externo;
- Componente duplicado pendiente de consolidación.

---

## Rango

- Componente canónico;
- Término canónico;
- Identidad principal.

---

## Dirección

Dirigida.

```text
Alias ── alias_de ── Canónico
```

---

## Relación inversa

```text
tiene_alias
```

---

## Características lógicas

- simétrica: no;
- transitiva: sí hacia el canónico;
- reflexiva: no.

---

## Restricciones

El alias no deberá recibir una identidad conceptual independiente cuando representa exactamente la misma entidad.

---

## Ejemplo válido

```text
Coriandro, en contexto de hojas ── alias_de ── Cilantro
```

La validez dependerá del uso regional y deberá documentarse.

---

# REL-0055 — similar_a

## Finalidad

Expresar semejanza relevante sin afirmar equivalencia, derivación o sustitución.

---

## Definición normativa

`similar_a` indica que dos componentes comparten características suficientes para ser comparados o recuperados conjuntamente.

---

## Dominio

- Componente;
- Receta;
- Ingrediente;
- Técnica;
- Concepto;
- Resultado.

---

## Rango

- Componente;
- Receta;
- Ingrediente;
- Técnica;
- Concepto;
- Resultado.

---

## Dirección

No dirigida conceptualmente.

---

## Relación inversa

La propia relación.

---

## Características lógicas

- simétrica: sí;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- criterio;
- dimensión;
- grado;
- confianza;
- origen;
- método de cálculo.

---

## Ejemplo válido

```text
Ragú italiano ── similar_a ── Estofado de carne
```

---

# Familia de relaciones de sustitución y compatibilidad

Estas relaciones representan reemplazo, combinación, compatibilidad e incompatibilidad.

---

# REL-0060 — sustituye_a

## Finalidad

Expresar que un componente puede reemplazar a otro bajo condiciones determinadas.

---

## Definición normativa

`sustituye_a` indica que el origen puede ocupar el rol funcional del destino en un contexto concreto.

No implica identidad ni equivalencia completa.

---

## Dominio

- Ingrediente;
- Base culinaria;
- Equipo;
- Técnica;
- Receta;
- Unidad;
- Componente.

---

## Rango

- Ingrediente;
- Base culinaria;
- Equipo;
- Técnica;
- Receta;
- Unidad;
- Componente.

---

## Dirección

Dirigida.

```text
Sustituto ── sustituye_a ── Sustituido
```

---

## Cardinalidad

```text
Origen: 0..*
Destino: 0..*
```

---

## Relación inversa

```text
puede_ser_sustituido_por
```

---

## Características lógicas

- simétrica: no;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- proporción;
- receta;
- técnica;
- restricción;
- efecto sobre sabor;
- efecto sobre textura;
- nivel de equivalencia;
- condiciones;
- confianza.

---

## Restricciones

Toda sustitución deberá declarar contexto cuando no sea universal.

---

## Ejemplo válido

```text
Yogur natural ── sustituye_a ── Nata
```

Contexto:

```text
uso: salsa fría
proporción: 1:1
efecto: mayor acidez y menor grasa
```

---

## Contraejemplo

```text
Yogur natural ── equivalente_a ── Nata
```

La relación sería demasiado fuerte.

---

# REL-0061 — puede_ser_sustituido_por

## Finalidad

Expresar la relación inversa de `sustituye_a`.

---

## Relación inversa

```text
sustituye_a
```

---

# REL-0062 — compatible_con

## Finalidad

Expresar que dos componentes pueden utilizarse conjuntamente sin conflicto relevante.

---

## Definición normativa

`compatible_con` indica compatibilidad funcional, técnica, dietética, material o conceptual.

---

## Dominio

- Ingrediente;
- Equipo;
- Técnica;
- Restricción;
- Esquema;
- Representación;
- Unidad;
- Componente.

---

## Rango

- Ingrediente;
- Equipo;
- Técnica;
- Restricción;
- Esquema;
- Representación;
- Unidad;
- Componente.

---

## Dirección

No dirigida conceptualmente.

---

## Relación inversa

La propia relación.

---

## Características lógicas

- simétrica: sí, salvo especialización explícita;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- ámbito;
- condición;
- grado;
- fuente;
- validación;
- fecha de vigencia.

---

## Ejemplo válido

```text
Sartén de hierro ── compatible_con ── Cocina de inducción
```

si el material y diseño concretos lo permiten.

---

# REL-0063 — incompatible_con

## Finalidad

Expresar que dos componentes no deben combinarse o utilizarse conjuntamente en un contexto determinado.

---

## Definición normativa

`incompatible_con` indica conflicto funcional, técnico, dietético, material, semántico o de seguridad.

---

## Dominio

- Ingrediente;
- Equipo;
- Técnica;
- Restricción;
- Esquema;
- Representación;
- Unidad;
- Componente.

---

## Rango

- Ingrediente;
- Equipo;
- Técnica;
- Restricción;
- Esquema;
- Representación;
- Unidad;
- Componente.

---

## Dirección

No dirigida conceptualmente.

---

## Relación inversa

La propia relación.

---

## Características lógicas

- simétrica: normalmente sí;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- motivo;
- severidad;
- condición;
- ámbito;
- evidencia;
- fuente;
- excepción.

---

## Ejemplo válido

```text
Restricción sin gluten ── incompatible_con ── Harina de trigo
```

---

# REL-0064 — combina_con

## Finalidad

Expresar afinidad culinaria, sensorial o funcional entre componentes.

---

## Definición normativa

`combina_con` indica que dos componentes producen conjuntamente un resultado considerado adecuado o valioso dentro de un criterio explícito.

---

## Dominio

- Ingrediente;
- Base;
- Receta;
- Sabor;
- Técnica;
- Bebida;
- Resultado.

---

## Rango

- Ingrediente;
- Base;
- Receta;
- Sabor;
- Técnica;
- Bebida;
- Resultado.

---

## Dirección

No dirigida conceptualmente.

---

## Relación inversa

La propia relación.

---

## Características lógicas

- simétrica: sí;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- criterio;
- intensidad;
- cocina;
- preparación;
- temperatura;
- fuente;
- confianza.

---

## Restricciones

No deberá tratarse como una verdad universal.

La afinidad puede depender del contexto culinario y cultural.

---

## Ejemplo válido

```text
Tomate ── combina_con ── Albahaca
```

---

# Familia de relaciones de derivación y procedencia

Estas relaciones expresan origen, adaptación, generación y trazabilidad conceptual.

---

# REL-0070 — deriva_de

## Finalidad

Expresar que un componente se ha desarrollado a partir de otro.

---

## Definición normativa

`deriva_de` indica una conexión de origen conceptual, estructural, documental o procesual.

---

## Dominio

- Receta;
- Plantilla;
- Documento;
- Componente;
- Resultado calculado;
- Esquema;
- Taxonomía;
- Representación.

---

## Rango

- Receta;
- Plantilla;
- Documento;
- Componente;
- Fuente;
- Esquema;
- Taxonomía;
- Representación.

---

## Dirección

Dirigida.

```text
Derivado ── deriva_de ── Fuente
```

---

## Relación inversa

```text
origina
```

---

## Características lógicas

- simétrica: no;
- transitiva: condicionada;
- reflexiva: no.

---

## Atributos contextuales

- método;
- cambios;
- fecha;
- autor;
- versión;
- grado de transformación;
- licencia;
- fuente.

---

## Ejemplo válido

```text
Curry japonés vegetariano ── deriva_de ── Curry japonés tradicional
```

---

# REL-0071 — basado_en

## Finalidad

Expresar inspiración o dependencia conceptual parcial.

---

## Definición normativa

`basado_en` indica que el origen utiliza al destino como referencia, fundamento o modelo, sin implicar una derivación directa completa.

---

## Dominio

- Receta;
- Plantilla;
- Documento;
- Modelo;
- Esquema;
- Sistema;
- Componente.

---

## Rango

- Receta;
- Plantilla;
- Documento;
- Modelo;
- Esquema;
- Fuente;
- Componente.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
sirve_de_base_para
```

---

## Características lógicas

- simétrica: no;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- aspecto reutilizado;
- alcance;
- fuente;
- autor;
- justificación.

---

## Ejemplo válido

```text
Plantilla de ramen doméstico ── basada_en ── Estructura tradicional del ramen
```

---

# REL-0072 — adaptado_de

## Finalidad

Expresar una derivación deliberada condicionada por un contexto.

---

## Definición normativa

`adaptado_de` indica que el origen modifica el destino para satisfacer restricciones, recursos, preferencias o contextos determinados.

---

## Dominio

- Receta;
- Menú;
- Plantilla;
- Técnica;
- Documento;
- Planificación.

---

## Rango

- Receta;
- Menú;
- Plantilla;
- Técnica;
- Documento;
- Planificación.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
tiene_adaptacion
```

---

## Atributos contextuales

- motivo;
- cambios;
- restricciones;
- autor;
- fecha;
- impacto esperado.

---

## Ejemplo válido

```text
Tarta sin lactosa ── adaptada_de ── Tarta de queso clásica
```

---

# REL-0073 — origina

## Finalidad

Expresar la relación inversa de `deriva_de`.

---

## Definición normativa

Indica que un componente actúa como fuente de otro componente derivado.

---

## Relación inversa

```text
deriva_de
```

---

# REL-0074 — respaldado_por

## Finalidad

Expresar que una afirmación, relación o componente dispone de evidencia o fuente de apoyo.

---

## Definición normativa

`respaldado_por` conecta conocimiento con evidencia documental, experimental, bibliográfica, técnica o humana.

---

## Dominio

- Relación;
- Afirmación;
- Recomendación;
- Restricción;
- Componente;
- Resultado;
- Inferencia.

---

## Rango

- Evidencia;
- Documento;
- Fuente;
- Prueba;
- Observación;
- Referencia bibliográfica;
- Validación.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
respalda
```

---

## Atributos contextuales

- nivel de evidencia;
- fecha;
- autor;
- método;
- confianza;
- vigencia.

---

## Ejemplo válido

```text
Relación de sustitución ── respaldada_por ── Prueba culinaria documentada
```

---

# Familia de relaciones organizativas

Estas relaciones expresan pertenencia a colecciones, series, índices, catálogos y agrupaciones.

---

# REL-0080 — pertenece_a

## Finalidad

Expresar pertenencia organizativa o temática a una agrupación.

---

## Definición normativa

`pertenece_a` indica que el origen es miembro de una colección, serie, catálogo, conjunto o estructura organizativa.

No implica composición ontológica ni clasificación de tipo.

---

## Dominio

- Componente;
- Documento;
- Relación;
- Entrada;
- Menú;
- Receta;
- Técnica;
- Ingrediente.

---

## Rango

- Colección;
- Serie;
- Catálogo;
- Índice;
- Proyecto;
- Conjunto;
- Agrupación.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
tiene_miembro
```

---

## Características lógicas

- simétrica: no;
- transitiva: no por defecto;
- reflexiva: no.

---

## Atributos contextuales

- orden;
- fecha;
- rol;
- criterio;
- curatoría;
- estado de pertenencia.

---

## Ejemplo válido

```text
Curry japonés ── pertenece_a ── Colección de cocina japonesa
```

---

## Contraejemplo

```text
Curry japonés ── pertenece_a ── Receta
```

En este caso se necesitaría `es_un`.

---

# REL-0081 — tiene_miembro

## Finalidad

Expresar la relación inversa de `pertenece_a`.

---

## Relación inversa

```text
pertenece_a
```

---

# REL-0082 — miembro_de_serie

## Finalidad

Expresar pertenencia ordenada a una serie.

---

## Definición normativa

Indica que un componente forma parte de una serie con posición o secuencia significativa.

---

## Dominio

- Componente;
- Documento;
- Receta;
- Menú;
- Técnica;
- Lección.

---

## Rango

- Serie.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
tiene_elemento_de_serie
```

---

## Atributos contextuales

- posición;
- predecesor;
- sucesor;
- fecha;
- etapa;
- obligatoriedad.

---

## Ejemplo válido

```text
Técnicas básicas de cuchillo ── miembro_de_serie ── Ruta de aprendizaje culinario
```

---

# REL-0083 — indexado_en

## Finalidad

Expresar que un componente aparece referenciado en un índice.

---

## Definición normativa

`indexado_en` indica presencia navegacional o de recuperación, sin alterar la identidad ni clasificación principal del componente.

---

## Dominio

- Componente;
- Documento;
- Relación;
- Categoría.

---

## Rango

- Índice;
- Buscador;
- Catálogo;
- Vista;
- Registro.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
indexa
```

---

## Ejemplo válido

```text
Miso blanco ── indexado_en ── Índice de ingredientes
```

---

# REL-0084 — catalogado_en

## Finalidad

Expresar que un componente forma parte del alcance de un catálogo.

---

## Definición normativa

Indica que un componente ha sido incorporado como entrada de un inventario estructurado.

---

## Dominio

- Componente;
- Documento;
- Relación;
- Tipo.

---

## Rango

- Catálogo.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
cataloga
```

---

## Atributos contextuales

- fecha;
- estado;
- cobertura;
- clasificación;
- fuente.

---

# Familia de relaciones de restricción y cumplimiento

Estas relaciones expresan exclusión, limitación, satisfacción, incumplimiento y aplicabilidad.

---

# REL-0090 — excluye

## Finalidad

Expresar que una restricción, regla o contexto impide utilizar o seleccionar otro componente.

---

## Definición normativa

`excluye` indica incompatibilidad normativa o contextual fuerte desde el origen hacia el destino.

---

## Dominio

- Restricción;
- Regla;
- Dieta;
- Alergia;
- Planificación;
- Esquema;
- Contexto.

---

## Rango

- Ingrediente;
- Receta;
- Técnica;
- Equipo;
- Menú;
- Propiedad;
- Valor;
- Componente.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
es_excluido_por
```

---

## Características lógicas

- simétrica: no;
- transitiva: condicionada;
- reflexiva: no.

---

## Atributos contextuales

- severidad;
- motivo;
- condición;
- excepción;
- vigencia;
- evidencia.

---

## Ejemplo válido

```text
Dieta vegana ── excluye ── Mantequilla
```

---

# REL-0091 — limita

## Finalidad

Expresar que una restricción reduce el rango de valores, acciones o componentes permitidos.

---

## Definición normativa

`limita` indica una restricción parcial, cuantitativa o condicional.

---

## Dominio

- Restricción;
- Presupuesto;
- Tiempo;
- Capacidad;
- Equipo;
- Regla;
- Planificación.

---

## Rango

- Receta;
- Menú;
- Cantidad;
- Tiempo;
- Técnica;
- Equipo;
- Selección;
- Componente.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
es_limitado_por
```

---

## Atributos contextuales

- límite mínimo;
- límite máximo;
- unidad;
- condición;
- periodo;
- severidad.

---

## Ejemplo válido

```text
Presupuesto semanal ── limita ── Coste del menú
```

---

# REL-0092 — satisface

## Finalidad

Expresar que un componente cumple una condición, restricción, objetivo o criterio.

---

## Definición normativa

`satisface` indica conformidad positiva comprobada o declarada.

---

## Dominio

- Receta;
- Menú;
- Planificación;
- Componente;
- Documento;
- Resultado;
- Sistema.

---

## Rango

- Restricción;
- Criterio;
- Regla;
- Objetivo;
- Esquema;
- Requisito.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
es_satisfecho_por
```

---

## Características lógicas

- simétrica: no;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- método de validación;
- fecha;
- confianza;
- evidencia;
- versión;
- condición.

---

## Ejemplo válido

```text
Menú vegetariano ── satisface ── Restricción sin carne
```

---

# REL-0093 — incumple

## Finalidad

Expresar que un componente contradice o no satisface una restricción o criterio.

---

## Definición normativa

`incumple` representa una evaluación negativa explícita.

La ausencia de `satisface` no implica automáticamente `incumple`.

---

## Dominio

- Receta;
- Menú;
- Planificación;
- Componente;
- Documento;
- Resultado;
- Sistema.

---

## Rango

- Restricción;
- Criterio;
- Regla;
- Objetivo;
- Esquema;
- Requisito.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
es_incumplido_por
```

---

## Atributos contextuales

- motivo;
- severidad;
- evidencia;
- fecha;
- parte afectada;
- posibilidad de corrección.

---

## Ejemplo válido

```text
Receta con harina de trigo ── incumple ── Restricción sin gluten
```

---

# REL-0094 — aplicable_a

## Finalidad

Expresar el ámbito sobre el que una regla, restricción, técnica o concepto puede utilizarse.

---

## Definición normativa

`aplicable_a` indica que el origen resulta pertinente o válido para el destino.

---

## Dominio

- Regla;
- Restricción;
- Técnica;
- Plantilla;
- Esquema;
- Recomendación;
- Concepto.

---

## Rango

- Receta;
- Ingrediente;
- Técnica;
- Menú;
- Componente;
- Tipo;
- Contexto.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
admite_aplicacion_de
```

---

## Atributos contextuales

- condición;
- alcance;
- excepción;
- vigencia;
- contexto.

---

## Ejemplo válido

```text
Técnica de confitado ── aplicable_a ── Ajo
```

---

# Familia de relaciones de representación y documentación

Estas relaciones conectan entidades conceptuales con documentos, formatos, publicaciones y recursos técnicos.

---

# REL-0100 — representado_por

## Finalidad

Expresar que un activo conceptual dispone de una representación concreta.

---

## Definición normativa

`representado_por` conecta un componente con una materialización física, documental o digital.

---

## Dominio

- Componente;
- Relación;
- Ontología;
- Esquema;
- Colección;
- Activo de conocimiento.

---

## Rango

- Documento;
- Recurso JSON;
- Registro de base de datos;
- Nodo de grafo;
- Recurso API;
- Archivo;
- Vista.

---

## Dirección

Dirigida.

```text
Concepto ── representado_por ── Representación
```

---

## Cardinalidad

```text
Origen: 1..*
Destino: 0..*
```

Un activo canónico deberá disponer de al menos una representación gestionable.

---

## Relación inversa

```text
representa
```

---

## Características lógicas

- simétrica: no;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- formato;
- versión;
- carácter canónico;
- idioma;
- ubicación;
- fecha;
- estado.

---

## Ejemplo válido

```text
Receta conceptual ── representada_por ── Documento Markdown
```

---

# REL-0101 — representa

## Finalidad

Expresar la relación inversa de `representado_por`.

---

## Definición normativa

Indica que una representación materializa o expresa un activo conceptual.

---

## Relación inversa

```text
representado_por
```

---

# REL-0102 — documentado_en

## Finalidad

Expresar que un componente o decisión se describe formalmente en un documento.

---

## Definición normativa

`documentado_en` conecta conocimiento con el documento que contiene su descripción autoritativa o relevante.

---

## Dominio

- Componente;
- Relación;
- Decisión;
- Proceso;
- Regla;
- Arquitectura;
- Restricción.

---

## Rango

- Documento;
- Especificación;
- ADR;
- Guía;
- Registro;
- Informe.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
documenta
```

---

## Atributos contextuales

- carácter canónico;
- sección;
- versión;
- fecha;
- alcance.

---

## Ejemplo válido

```text
Modelo de relaciones ── documentado_en ── ESPECIFICACION_DE_RELACIONES.md
```

---

# REL-0103 — serializado_como

## Finalidad

Expresar el formato técnico utilizado para codificar una representación.

---

## Definición normativa

`serializado_como` conecta una representación o activo intercambiable con un formato concreto.

---

## Dominio

- Recurso;
- Representación;
- Esquema;
- Componente exportable;
- Relación exportable.

---

## Rango

- JSON;
- YAML;
- RDF;
- XML;
- CSV;
- Markdown;
- Formato binario.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
serializa
```

---

## Atributos contextuales

- versión del formato;
- esquema;
- codificación;
- perfil;
- compatibilidad.

---

## Ejemplo válido

```text
Exportación de receta ── serializada_como ── JSON
```

---

# REL-0104 — publicado_en

## Finalidad

Expresar que un activo o representación está disponible en un canal o plataforma.

---

## Definición normativa

`publicado_en` conecta un activo con el destino de publicación o distribución.

---

## Dominio

- Documento;
- Receta;
- Catálogo;
- Colección;
- Representación;
- Release.

---

## Rango

- Sitio web;
- Repositorio;
- API;
- Plataforma;
- Canal;
- Paquete;
- Índice público.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
publica
```

---

## Atributos contextuales

- URL o identificador;
- fecha;
- versión;
- estado;
- audiencia;
- visibilidad;
- licencia.

---

## Ejemplo válido

```text
Documentación generada ── publicada_en ── Sitio web del proyecto
```

---

# REL-0105 — fuente_canonica_de

## Finalidad

Expresar que una representación constituye la fuente autoritativa de un activo.

---

## Definición normativa

`fuente_canonica_de` identifica la representación que debe considerarse oficial frente a copias, vistas o derivados.

---

## Dominio

- Documento;
- Registro;
- Repositorio;
- Recurso;
- Base de datos.

---

## Rango

- Componente;
- Relación;
- Colección;
- Ontología;
- Esquema;
- Activo de conocimiento.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
tiene_fuente_canonica
```

---

## Características lógicas

- simétrica: no;
- transitiva: no;
- inversamente funcional: preferentemente sí dentro de un contexto y versión.

---

## Restricciones

Un activo no deberá tener varias fuentes canónicas activas para la misma representación y versión sin una regla explícita de autoridad.

---

## Ejemplo válido

```text
REC-0042.md ── fuente_canonica_de ── Receta Curry japonés
```

---

# Familia de relaciones culinarias especializadas

Estas relaciones expresan conocimientos específicos del dominio que no quedan completamente cubiertos por las familias generales.

---

# REL-0110 — incorpora_sabor

## Finalidad

Expresar que un componente aporta una cualidad gustativa o aromática a otro.

---

## Definición normativa

`incorpora_sabor` conecta una preparación, ingrediente o técnica con una cualidad sensorial aportada.

---

## Dominio

- Ingrediente;
- Técnica;
- Base;
- Elaboración;
- Receta.

---

## Rango

- Sabor;
- Aroma;
- Perfil sensorial;
- Concepto culinario.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
es_aportado_por
```

---

## Atributos contextuales

- intensidad;
- fase;
- condición;
- duración;
- percepción esperada.

---

## Ejemplo válido

```text
Miso ── incorpora_sabor ── Umami
```

---

# REL-0111 — modifica_textura

## Finalidad

Expresar que una técnica o componente altera la textura de otro.

---

## Definición normativa

`modifica_textura` indica un efecto estructural o sensorial sobre la consistencia del destino.

---

## Dominio

- Técnica;
- Ingrediente;
- Aditivo;
- Proceso;
- Elaboración.

---

## Rango

- Ingrediente;
- Elaboración;
- Resultado;
- Textura.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
textura_modificada_por
```

---

## Atributos contextuales

- textura inicial;
- textura final;
- intensidad;
- temperatura;
- duración;
- proporción.

---

## Ejemplo válido

```text
Gelatina ── modifica_textura ── Líquido
```

---

# REL-0112 — potencia

## Finalidad

Expresar que un componente incrementa una propiedad sensorial o funcional de otro.

---

## Definición normativa

`potencia` indica una intensificación contextual, no una simple coexistencia.

---

## Dominio

- Ingrediente;
- Técnica;
- Condimento;
- Proceso;
- Contexto.

---

## Rango

- Sabor;
- Aroma;
- Textura;
- Color;
- Propiedad culinaria;
- Ingrediente.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
es_potenciado_por
```

---

## Atributos contextuales

- intensidad;
- mecanismo;
- condición;
- proporción;
- evidencia.

---

## Ejemplo válido

```text
Sal ── potencia ── Dulzor
```

en determinadas concentraciones y contextos.

---

# REL-0113 — neutraliza

## Finalidad

Expresar que un componente reduce o compensa una propiedad de otro.

---

## Definición normativa

`neutraliza` indica disminución, compensación o equilibrio de un efecto sensorial, químico o funcional.

---

## Dominio

- Ingrediente;
- Técnica;
- Proceso;
- Sustancia;
- Acción correctiva.

---

## Rango

- Sabor;
- Acidez;
- Picante;
- Amargor;
- Olor;
- Propiedad culinaria.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
es_neutralizado_por
```

---

## Atributos contextuales

- grado;
- cantidad;
- condición;
- mecanismo;
- limitaciones.

---

## Ejemplo válido

```text
Azúcar ── neutraliza ── Acidez percibida
```

Sin implicar necesariamente modificación del pH.

---

# REL-0114 — marida_con

## Finalidad

Expresar afinidad gastronómica planificada entre preparaciones, ingredientes o bebidas.

---

## Definición normativa

`marida_con` indica compatibilidad sensorial y gastronómica orientada al consumo conjunto.

---

## Dominio

- Receta;
- Preparación;
- Ingrediente;
- Bebida;
- Menú.

---

## Rango

- Receta;
- Preparación;
- Ingrediente;
- Bebida;
- Menú.

---

## Dirección

No dirigida conceptualmente.

---

## Relación inversa

La propia relación.

---

## Características lógicas

- simétrica: sí;
- transitiva: no;
- reflexiva: no.

---

## Atributos contextuales

- criterio;
- temperatura;
- servicio;
- intensidad;
- tradición;
- confianza;
- fuente.

---

## Ejemplo válido

```text
Curry picante ── marida_con ── Cerveza lager
```

---

# REL-0115 — pertenece_a_tradicion

## Finalidad

Expresar asociación cultural, histórica o gastronómica con una tradición culinaria.

---

## Definición normativa

`pertenece_a_tradicion` conecta un componente con una tradición, cocina regional, comunidad o corriente culinaria.

---

## Dominio

- Receta;
- Técnica;
- Ingrediente;
- Menú;
- Concepto;
- Equipo.

---

## Rango

- Tradición culinaria;
- Cocina regional;
- Cultura gastronómica;
- Comunidad;
- Periodo histórico.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
incluye_en_tradicion
```

---

## Atributos contextuales

- región;
- periodo;
- grado de representatividad;
- fuente;
- controversia;
- variante local.

---

## Ejemplo válido

```text
Okonomiyaki ── pertenece_a_tradicion ── Cocina japonesa
```

---

# Familia de relaciones de planificación

Estas relaciones conectan recetas, menús, compras, recursos y ejecución futura.

---

# REL-0120 — planifica

## Finalidad

Expresar que un componente de planificación organiza la ejecución o uso de otro.

---

## Definición normativa

`planifica` indica que el origen establece cuándo, cómo o con qué recursos deberá ejecutarse el destino.

---

## Dominio

- Planificación;
- Menú;
- Agenda culinaria;
- Plan de preparación.

---

## Rango

- Receta;
- Elaboración;
- Compra;
- Técnica;
- Tarea;
- Menú;
- Servicio.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
planificado_por
```

---

## Atributos contextuales

- fecha;
- hora;
- prioridad;
- responsable;
- duración;
- estado;
- dependencia.

---

## Ejemplo válido

```text
Plan semanal ── planifica ── Curry japonés para el martes
```

---

# REL-0121 — genera_necesidad_de_compra

## Finalidad

Expresar que un componente produce una necesidad concreta de adquisición.

---

## Definición normativa

Indica que una receta, menú o planificación requiere comprar un ingrediente o recurso no disponible.

---

## Dominio

- Receta;
- Menú;
- Planificación;
- Elaboración.

---

## Rango

- Ingrediente;
- Equipo;
- Recurso;
- Producto comercial.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
requerido_para_compra_por
```

---

## Atributos contextuales

- cantidad;
- unidad;
- prioridad;
- fecha límite;
- precio estimado;
- disponibilidad;
- proveedor.

---

## Ejemplo válido

```text
Menú semanal ── genera_necesidad_de_compra ── 1 kg de cebollas
```

---

# REL-0122 — aprovecha

## Finalidad

Expresar reutilización planificada de ingredientes, bases, sobras o elaboraciones.

---

## Definición normativa

`aprovecha` indica que el origen utiliza un componente disponible para reducir desperdicio, coste o trabajo.

---

## Dominio

- Receta;
- Menú;
- Planificación;
- Elaboración.

---

## Rango

- Ingrediente disponible;
- Sobra;
- Base;
- Elaboración previa;
- Recurso.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
es_aprovechado_por
```

---

## Atributos contextuales

- cantidad;
- estado;
- fecha límite;
- condición;
- origen;
- ahorro estimado.

---

## Ejemplo válido

```text
Arroz frito ── aprovecha ── Arroz cocido del día anterior
```

---

# REL-0123 — asignado_a

## Finalidad

Expresar responsabilidad operativa sobre una tarea, preparación o proceso.

---

## Definición normativa

`asignado_a` conecta una actividad planificada con una persona, agente, equipo o sistema responsable.

---

## Dominio

- Tarea;
- Elaboración planificada;
- Compra;
- Proceso;
- Validación;
- Revisión.

---

## Rango

- Persona;
- Rol;
- Equipo humano;
- Agente IA;
- Sistema;
- Herramienta.

---

## Dirección

Dirigida.

---

## Relación inversa

```text
responsable_de
```

---

## Atributos contextuales

- fecha;
- prioridad;
- estado;
- capacidad;
- aceptación;
- plazo.

---

# Resumen del catálogo inicial

El catálogo inicial de relaciones del SGCC queda organizado en las siguientes familias:

| Familia | Relaciones principales |
|---|---|
| Estructurales | contiene, compuesto_por, forma_parte_de, incluye |
| Uso y dependencia | utiliza, requiere, depende_de, recomienda |
| Proceso y transformación | aplica, transforma, produce, genera, convierte_en |
| Temporales | precede_a, sigue_a, ocurre_durante, simultaneo_a, vigente_durante |
| Taxonómicas | es_un, subtipo_de, clasifica, pertenece_a_categoria, especializa |
| Variación y equivalencia | variante_de, equivalente_a, alias_de, similar_a |
| Sustitución y compatibilidad | sustituye_a, compatible_con, incompatible_con, combina_con |
| Derivación y procedencia | deriva_de, basado_en, adaptado_de, respaldado_por |
| Organizativas | pertenece_a, miembro_de_serie, indexado_en, catalogado_en |
| Restricción | excluye, limita, satisface, incumple, aplicable_a |
| Representación | representado_por, documentado_en, serializado_como, publicado_en |
| Culinarias especializadas | incorpora_sabor, modifica_textura, potencia, neutraliza, marida_con |
| Planificación | planifica, genera_necesidad_de_compra, aprovecha, asignado_a |

---

# Relaciones canónicas prioritarias

Para la primera implementación del SGCC se consideran prioritarias las siguientes relaciones:

```text
utiliza
requiere
aplica
produce
forma_parte_de
pertenece_a
variante_de
sustituye_a
deriva_de
precede_a
satisface
representado_por
documentado_en
```

Estas relaciones cubren el núcleo mínimo necesario para:

- representar recetas;
- conectar ingredientes;
- modelar técnicas;
- estructurar elaboraciones;
- organizar colecciones;
- expresar variantes;
- registrar sustituciones;
- construir secuencias;
- validar restricciones;
- enlazar componentes con documentos.

---

# Relaciones secundarias

Las siguientes relaciones podrán incorporarse progresivamente:

```text
combina_con
marida_con
potencia
neutraliza
similar_a
equivalente_aproximado_a
genera_necesidad_de_compra
aprovecha
asignado_a
```

Su implementación podrá depender de:

- madurez del modelo;
- disponibilidad de datos;
- criterios de calidad;
- necesidad funcional;
- capacidad de validación.

---

# Reglas de selección entre relaciones próximas

Algunas relaciones pueden parecer similares.

Deberán aplicarse las siguientes reglas de selección.

---

## `contiene` frente a `compuesto_por`

Utilizar:

```text
contiene
```

cuando exista agregación u organización.

Utilizar:

```text
compuesto_por
```

cuando las partes contribuyan a la estructura funcional del conjunto.

---

## `incluye` frente a `pertenece_a`

Utilizar:

```text
incluye
```

desde el contenedor hacia el miembro.

Utilizar:

```text
pertenece_a
```

desde el miembro hacia la agrupación.

---

## `utiliza` frente a `requiere`

Utilizar:

```text
utiliza
```

cuando un componente emplea otro.

Utilizar:

```text
requiere
```

cuando el destino sea necesario para la ejecución o validez.

Un componente puede utilizar algo sin requerirlo obligatoriamente.

---

## `requiere` frente a `depende_de`

Utilizar:

```text
requiere
```

para una necesidad concreta.

Utilizar:

```text
depende_de
```

cuando exista condicionamiento estructural, lógico o de ciclo de vida.

---

## `produce` frente a `genera`

Utilizar:

```text
produce
```

para resultados culinarios o materiales.

Utilizar:

```text
genera
```

para resultados documentales, computacionales, organizativos o derivados.

---

## `variante_de` frente a `deriva_de`

Utilizar:

```text
variante_de
```

cuando el origen conserve la estructura e identidad general del modelo base.

Utilizar:

```text
deriva_de
```

cuando exista un origen reconocible, pero el resultado pueda haberse transformado con mayor libertad.

---

## `equivalente_a` frente a `sustituye_a`

Utilizar:

```text
equivalente_a
```

cuando exista correspondencia semántica o cuantitativa dentro del ámbito declarado.

Utilizar:

```text
sustituye_a
```

cuando un componente pueda reemplazar funcionalmente a otro bajo condiciones.

---

## `compatible_con` frente a `combina_con`

Utilizar:

```text
compatible_con
```

para ausencia de conflicto funcional o técnico.

Utilizar:

```text
combina_con
```

para afinidad culinaria o sensorial positiva.

---

## `es_un` frente a `pertenece_a`

Utilizar:

```text
es_un
```

para clasificación ontológica.

Utilizar:

```text
pertenece_a
```

para agrupación organizativa.

---

## `alias_de` frente a `equivalente_a`

Utilizar:

```text
alias_de
```

cuando dos nombres remitan a la misma identidad.

Utilizar:

```text
equivalente_a
```

cuando existan dos entidades o valores distintos con correspondencia definida.

---

# Relaciones que deberán evitarse

Las siguientes relaciones genéricas no deberán utilizarse como primera opción:

```text
relacionado_con
asociado_a
vinculado_a
conecta_con
tiene
```

Solo podrán admitirse cuando:

- no exista una relación más precisa;
- su semántica esté definida;
- el contexto impida una mayor especialización;
- su uso sea temporal durante una migración;
- exista una estrategia para refinarla posteriormente.

El uso indiscriminado de relaciones genéricas reduce:

- capacidad de inferencia;
- precisión semántica;
- validación;
- interoperabilidad;
- utilidad del Knowledge Graph.

---

# Catálogo y ontología

Los tipos definidos en esta sección constituyen candidatos a propiedades de objeto de la futura ontología del SGCC.

La ontología deberá decidir:

- qué relaciones se mantienen como primitivas;
- cuáles son inversas calculadas;
- cuáles son subpropiedades de otras;
- cuáles son transitivas;
- cuáles son simétricas;
- cuáles requieren entidades asociativas;
- cuáles pueden inferirse;
- cuáles necesitan restricciones de cardinalidad.

Ejemplo:

```text
utiliza
    │
    ├── utiliza_ingrediente
    ├── utiliza_equipo
    ├── utiliza_tecnica
    └── utiliza_base
```

La especificación ontológica podrá especializar relaciones generales sin invalidar el vocabulario aquí definido.

---

# Conformidad del catálogo

Una instancia de relación será conforme con esta sección cuando:

- utilice una relación reconocida;
- conecte tipos compatibles;
- respete la dirección canónica;
- utilice la inversa correcta cuando proceda;
- incluya atributos obligatorios;
- cumpla las restricciones;
- distinga contexto, procedencia y confianza cuando sean necesarios;
- no utilice una relación genérica existiendo otra más precisa.

Los aspectos avanzados de cardinalidad, reificación, inferencia, temporalidad y representación se desarrollarán en la siguiente parte de esta especificación.

---

# Modelo estructural y semántico de relaciones

Esta sección define cómo deberán representarse, interpretarse, validar e inferirse las relaciones del SGCC.

Mientras que el catálogo anterior establece **qué relaciones existen**, esta parte define:

- cómo se estructuran;
- cómo se expresan;
- cómo se contextualizan;
- cómo se representan técnicamente;
- cómo participan en inferencias;
- cómo se preservan su procedencia y trazabilidad;
- cómo se detectan conflictos semánticos.

---

# Modelo general de una instancia de relación

Toda instancia de relación deberá poder expresarse, como mínimo, mediante:

```text
Sujeto

↓

Predicado

↓

Objeto
```

Ejemplo:

```text
REC-0042 ── utiliza ── ING-0017
```

Este modelo mínimo constituye una triple semántica.

Sin embargo, muchas relaciones del SGCC necesitarán información adicional.

Modelo ampliado:

```text
Instancia de relación
    │
    ├── Identidad
    ├── Sujeto
    ├── Predicado
    ├── Objeto
    ├── Contexto
    ├── Atributos
    ├── Temporalidad
    ├── Procedencia
    ├── Evidencia
    ├── Confianza
    ├── Estado
    └── Versionado
```

No todos estos elementos deberán estar presentes en todas las relaciones.

Su obligatoriedad dependerá del tipo, complejidad y relevancia de la relación.

---

# Relaciones simples

Una relación simple conecta dos componentes sin necesitar atributos adicionales.

Ejemplo:

```text
REC-0042 ── pertenece_a ── COL-0008
```

Podría representarse de forma mínima mediante:

```yaml
sujeto: REC-0042
relacion: pertenece_a
objeto: COL-0008
```

Este modelo será suficiente cuando:

- el significado sea inequívoco;
- no existan cantidades;
- no dependa de condiciones;
- no requiera temporalidad;
- no necesite procedencia individual;
- no posea comportamiento propio.

---

# Relaciones contextualizadas

Una relación deberá contextualizarse cuando su significado dependa de datos adicionales.

Ejemplo:

```text
REC-0042 ── utiliza ── ING-0017
```

La afirmación anterior puede resultar insuficiente si se necesita conocer:

- cantidad;
- unidad;
- fase;
- preparación;
- opcionalidad;
- finalidad;
- sustituciones;
- orden;
- observaciones.

Representación contextualizada:

```yaml
sujeto: REC-0042
relacion: utiliza
objeto: ING-0017

contexto:
  cantidad: 250
  unidad: g
  preparacion: cortada_en_juliana
  fase: sofrito
  opcional: false
  orden: 2
```

Estos datos no pertenecen de forma global ni a la receta ni al ingrediente.

Pertenecen a la instancia concreta de la relación.

---

# Entidades asociativas

Cuando una relación posea suficiente complejidad, deberá representarse mediante una entidad asociativa.

Ejemplo:

```text
Receta
   │
   ▼
Uso de ingrediente
   │
   ▼
Ingrediente
```

Representación:

```text
REC-0042
   │
   └── tiene_uso_de_ingrediente
                │
                ▼
          USO-ING-0084
                │
                └── referencia_a
                            │
                            ▼
                       ING-0017
```

La entidad `USO-ING-0084` podrá almacenar:

```yaml
id: USO-ING-0084
tipo: uso_de_ingrediente

receta: REC-0042
ingrediente: ING-0017

cantidad: 250
unidad: g
preparacion: cortada_en_juliana
fase: sofrito
opcional: false
orden: 2
```

---

## Cuándo utilizar una entidad asociativa

Deberá considerarse una entidad asociativa cuando la relación:

- tenga propiedades propias;
- necesite identificador;
- disponga de ciclo de vida;
- requiera versionado;
- deba citarse;
- participe en otras relaciones;
- tenga procedencia independiente;
- sea n-aria;
- necesite validación compleja;
- pueda reutilizarse o consultarse directamente.

---

## Cuándo no utilizarla

No deberá crearse una entidad asociativa si:

- una triple simple expresa completamente el significado;
- no existen atributos contextuales;
- no se necesita identidad;
- no se requiere gestión independiente;
- su creación añade complejidad sin valor semántico.

---

# Relaciones binarias

Una relación binaria conecta dos participantes principales.

Modelo:

```text
A ── relación ── B
```

Ejemplos:

```text
Receta ── utiliza ── Ingrediente
```

```text
Técnica ── requiere ── Equipo
```

```text
Receta ── pertenece_a ── Colección
```

La mayoría de las relaciones del catálogo se definen inicialmente como binarias.

---

# Relaciones n-arias

Una relación n-aria conecta conceptualmente más de dos participantes.

Ejemplo:

```text
Una receta utiliza un ingrediente,
en una cantidad,
medida mediante una unidad,
durante una elaboración concreta.
```

Participantes:

```text
Receta

Ingrediente

Cantidad

Unidad

Elaboración
```

La relación no deberá representarse mediante varias triples independientes si con ello se pierde el vínculo contextual.

Representación incorrecta:

```text
Receta utiliza Harina

Receta tiene_cantidad 200

Receta utiliza_unidad Gramos
```

Esta estructura no permite saber si los `200 gramos` corresponden a la harina o a otro ingrediente.

Representación correcta:

```text
Uso de ingrediente

├── receta: REC-0042
├── ingrediente: ING-0017
├── cantidad: 200
├── unidad: UNI-0003
└── elaboracion: ELA-0011
```

---

# Participantes de una relación

Toda relación deberá definir el papel semántico de sus participantes.

Ejemplo:

```text
Sustitución culinaria
    │
    ├── sustituto
    ├── sustituido
    ├── contexto
    ├── proporción
    └── efecto esperado
```

No deberá depender únicamente del orden posicional cuando los roles puedan resultar ambiguos.

---

# Dirección

Las relaciones podrán ser:

- dirigidas;
- simétricas;
- conceptualmente no dirigidas;
- bidireccionales mediante inversas.

---

## Relaciones dirigidas

Una relación dirigida posee origen y destino semánticamente diferenciados.

Ejemplo:

```text
Receta ── utiliza ── Ingrediente
```

No equivale a:

```text
Ingrediente ── utiliza ── Receta
```

---

## Relaciones simétricas

Una relación simétrica expresa el mismo significado en ambas direcciones.

Ejemplo:

```text
Tomate ── combina_con ── Albahaca
```

implica:

```text
Albahaca ── combina_con ── Tomate
```

Las relaciones simétricas podrán almacenarse una sola vez mediante una regla de orden canónico.

---

## Relaciones conceptualmente no dirigidas

Algunas relaciones son simétricas desde el punto de vista conceptual, aunque la implementación necesite elegir un orden.

Ejemplo:

```text
compatible_con
```

La representación deberá garantizar que el orden técnico no altere el significado.

---

# Orientación canónica

Toda relación dirigida deberá disponer de una orientación canónica.

Ejemplo:

```text
Variante ── variante_de ── Componente base
```

La orientación inversa se expresará mediante:

```text
Componente base ── tiene_variante ── Variante
```

No deberán almacenarse indistintamente ambas formas sin una política definida.

---

# Relaciones inversas

Una relación inversa permite expresar la misma conexión desde el sentido opuesto.

Ejemplo:

```text
Receta ── utiliza ── Ingrediente
```

Inversa:

```text
Ingrediente ── es_utilizado_por ── Receta
```

---

## Almacenamiento de inversas

Las inversas podrán:

- almacenarse explícitamente;
- calcularse durante la consulta;
- inferirse automáticamente;
- materializarse para optimización.

La opción elegida deberá preservar coherencia.

---

## Regla de consistencia

Si ambas direcciones se almacenan explícitamente, deberán mantenerse sincronizadas.

Ejemplo:

```text
REC-0042 utiliza ING-0017
```

deberá implicar:

```text
ING-0017 es_utilizado_por REC-0042
```

No podrán coexistir afirmaciones contradictorias entre una relación y su inversa.

---

## Inversas canónicas

Las relaciones inversas deberán:

- estar registradas;
- utilizar nombres estables;
- conservar dominio y rango intercambiados;
- compartir restricciones semánticas compatibles.

---

# Cardinalidad

La cardinalidad define cuántas instancias pueden participar en cada extremo de una relación.

Notación general:

```text
0..1

1..1

0..*

1..*
```

---

## Cardinalidad mínima

Indica el número mínimo de conexiones requeridas.

Ejemplo:

```text
Receta ── produce ── Resultado
```

Una receta estable deberá producir al menos un resultado principal:

```text
1..*
```

---

## Cardinalidad máxima

Indica el número máximo de conexiones permitidas.

Ejemplo:

```text
Documento ── tiene_fuente_canonica ── Recurso
```

Dentro de un contexto y versión determinados podría permitirse:

```text
1..1
```

---

## Cardinalidad por dominio

Una misma relación podrá disponer de cardinalidades distintas según el tipo de origen.

Ejemplo:

```text
utiliza
```

Podría definirse como:

```text
Receta utiliza 1..* Ingredientes o elaboraciones
```

pero:

```text
Plantilla utiliza 0..* Componentes
```

---

## Cardinalidad contextual

La cardinalidad podrá depender de:

- estado;
- versión;
- subtipo;
- fase;
- contexto operativo;
- restricciones externas.

Ejemplo:

Una receta en borrador podría no declarar resultado.

Una receta estable deberá declarar al menos uno.

---

# Relaciones funcionales

Una relación es funcional cuando un sujeto solo puede tener un objeto dentro de un contexto determinado.

Ejemplo conceptual:

```text
Componente ── tiene_estado_actual ── Estado
```

Un componente no debería tener dos estados actuales simultáneos en el mismo contexto.

Notación:

```text
Sujeto → máximo un objeto
```

---

# Relaciones inversamente funcionales

Una relación es inversamente funcional cuando un objeto solo puede estar conectado con un sujeto mediante esa relación dentro de un contexto.

Ejemplo:

```text
Documento ── fuente_canonica_de ── Activo
```

Podría ser inversamente funcional dentro de una versión concreta.

No deberá asumirse globalmente sin considerar:

- idioma;
- versión;
- formato;
- jurisdicción;
- entorno.

---

# Simetría

Una relación simétrica cumple:

```text
A R B

⇒

B R A
```

Ejemplos candidatos:

```text
compatible_con

incompatible_con

combina_con

similar_a

marida_con
```

---

## Restricción de simetría

No deberá declararse simétrica una relación únicamente porque resulte natural leerla en ambas direcciones.

Ejemplo:

```text
sustituye_a
```

no es necesariamente simétrica.

Que A sustituya a B no implica que B sustituya a A en las mismas condiciones.

---

# Asimetría

Una relación es asimétrica cuando:

```text
A R B

⇒

no B R A
```

Ejemplos:

```text
precede_a

subtipo_de

deriva_de

forma_parte_de
```

---

# Reflexividad

Una relación reflexiva permite:

```text
A R A
```

La mayoría de las relaciones del SGCC serán irreflexivas.

Ejemplos inválidos:

```text
REC-0042 deriva_de REC-0042
```

```text
TEC-0008 precede_a TEC-0008
```

---

## Relaciones autorreferenciales controladas

Podrán existir relaciones autorreferenciales únicamente cuando expresen ciclos o estructuras recursivas legítimas.

Ejemplo:

```text
Categoría ── contiene_subcategoria ── Categoría
```

El tipo puede relacionarse consigo mismo, pero una instancia no deberá necesariamente relacionarse consigo misma.

---

# Transitividad

Una relación transitiva cumple:

```text
A R B

B R C

⇒

A R C
```

Ejemplos potenciales:

```text
subtipo_de

precede_a

forma_parte_de
```

Sin embargo, la transitividad deberá declararse explícitamente.

---

## Transitividad condicionada

Algunas relaciones solo serán transitivas bajo determinadas condiciones.

Ejemplo:

```text
A forma_parte_de B

B forma_parte_de C
```

podría permitir inferir:

```text
A forma_parte_de C
```

solo si ambos niveles representan composición estructural compatible.

No deberá aplicarse automáticamente cuando se mezclen:

- composición;
- agregación;
- pertenencia;
- inclusión documental.

---

## Relaciones no transitivas

No deberán tratarse como transitivas:

```text
similar_a

combina_con

sustituye_a

compatible_con
```

Ejemplo:

```text
A combina_con B

B combina_con C
```

no implica:

```text
A combina_con C
```

---

# Composición de relaciones

El SGCC podrá definir reglas que combinen varias relaciones.

Ejemplo:

```text
Receta utiliza Ingrediente

Ingrediente contiene Alérgeno
```

Regla:

```text
utiliza ○ contiene_alergeno

⇒

contiene_alergeno
```

Resultado:

```text
Receta contiene_alergeno Alérgeno
```

---

## Regla de composición

Toda composición deberá indicar:

- relaciones de entrada;
- orden;
- relación resultante;
- condiciones;
- excepciones;
- nivel de confianza;
- procedencia;
- versión de la regla.

---

## Notación conceptual

```text
R1 ○ R2 ⇒ R3
```

Ejemplo:

```text
utiliza ○ contiene_alergeno ⇒ contiene_alergeno
```

---

# Inferencia

La inferencia permite obtener nuevas relaciones a partir de conocimiento existente.

Modelo:

```text
Relaciones declaradas

↓

Regla de inferencia

↓

Relación inferida
```

---

# Tipos de inferencia

El SGCC podrá utilizar:

- inferencia por inversa;
- inferencia por simetría;
- inferencia por transitividad;
- inferencia por jerarquía;
- inferencia por composición;
- inferencia por restricciones;
- inferencia por cálculo;
- inferencia probabilística.

---

## Inferencia por inversa

A partir de:

```text
REC-0042 utiliza ING-0017
```

se podrá inferir:

```text
ING-0017 es_utilizado_por REC-0042
```

---

## Inferencia por simetría

A partir de:

```text
Tomate combina_con Albahaca
```

se podrá inferir:

```text
Albahaca combina_con Tomate
```

---

## Inferencia por transitividad

A partir de:

```text
Técnica A precede_a Técnica B

Técnica B precede_a Técnica C
```

se podrá inferir:

```text
Técnica A precede_a Técnica C
```

---

## Inferencia por jerarquía

A partir de:

```text
Harina integral es_un Harina de trigo

Harina de trigo contiene_alergeno Gluten
```

se podrá inferir, si la ontología lo permite:

```text
Harina integral contiene_alergeno Gluten
```

---

## Inferencia por restricción

A partir de:

```text
Receta utiliza Harina de trigo

Restricción sin gluten excluye Harina de trigo
```

se podrá inferir:

```text
Receta incumple Restricción sin gluten
```

---

## Inferencia por cálculo

A partir de cantidades, unidades y valores de coste:

```text
Uso de ingrediente

cantidad: 500 g
precio: 2 €/kg
```

se podrá calcular:

```text
coste: 1 €
```

El resultado deberá identificarse como calculado.

---

## Inferencia probabilística

Algunas relaciones podrán obtenerse mediante modelos estadísticos o de inteligencia artificial.

Ejemplo:

```text
Ingrediente A combina_con Ingrediente B
confianza: 0.84
```

Estas relaciones deberán identificarse como:

- inferidas;
- no canónicas por defecto;
- sujetas a validación;
- vinculadas al modelo y versión que las generó.

---

# Relaciones declaradas, derivadas y calculadas

Toda instancia deberá poder clasificarse según su origen.

---

## Declarada

Registrada explícitamente por una fuente autorizada.

```yaml
origen_semantico: declarada
```

---

## Inferida

Obtenida mediante reglas lógicas.

```yaml
origen_semantico: inferida
regla: REG-INF-0012
```

---

## Calculada

Obtenida mediante operación matemática o algoritmo determinista.

```yaml
origen_semantico: calculada
metodo: calcular_coste_ingrediente
```

---

## Predicha

Generada mediante un modelo probabilístico.

```yaml
origen_semantico: predicha
modelo: food-pairing-v2
confianza: 0.84
```

---

## Importada

Procedente de una fuente externa.

```yaml
origen_semantico: importada
fuente: DATASET-0004
```

---

# Prioridad semántica

Cuando existan varias relaciones equivalentes con distinto origen, deberá aplicarse una política de prioridad.

Propuesta general:

```text
Declarada y validada

↓

Declarada

↓

Importada de fuente confiable

↓

Inferida determinísticamente

↓

Calculada

↓

Predicha

↓

Hipotética
```

Esta jerarquía no sustituye a la evaluación del contexto ni de la calidad de las fuentes.

---

# Procedencia

Toda relación relevante deberá poder identificar su origen.

Modelo mínimo:

```yaml
procedencia:
  fuente: DOC-0042
  autor: USER-0003
  fecha: 2026-07-30
  metodo: declaracion_manual
```

Modelo ampliado:

```yaml
procedencia:
  fuente: DOC-0042
  seccion: ingredientes
  autor: USER-0003
  sistema: SGCC
  fecha_creacion: 2026-07-30
  fecha_revision: 2026-07-30
  metodo: declaracion_manual
  licencia: CC-BY-4.0
```

---

# Procedencia de relaciones inferidas

Una relación inferida deberá conservar:

- relaciones de entrada;
- regla aplicada;
- fecha;
- sistema;
- versión;
- confianza;
- explicación reproducible.

Ejemplo:

```yaml
relacion_inferida:
  sujeto: REC-0042
  relacion: contiene_alergeno
  objeto: ALG-0003

  derivada_de:
    - REL-INST-0142
    - REL-INST-0281

  regla: REG-INF-0007
  sistema: reasoner-v1
  fecha: 2026-07-30
```

---

# Evidencia

Una relación podrá estar respaldada por una o varias evidencias.

Tipos posibles:

- documento;
- bibliografía;
- prueba culinaria;
- observación;
- cálculo;
- análisis de laboratorio;
- norma;
- fuente oficial;
- consenso experto;
- resultado de validación.

Modelo:

```text
Relación

↓

respaldada_por

↓

Evidencia
```

---

## Evidencia primaria y secundaria

Deberá distinguirse entre:

```text
Evidencia primaria
```

obtenida directamente mediante prueba, observación o fuente original,

y:

```text
Evidencia secundaria
```

basada en análisis, resumen o interpretación de otra fuente.

---

# Confianza

La confianza expresa el grado de certeza asociado a una relación.

Podrá representarse mediante:

```text
alta

media

baja
```

o mediante un valor numérico:

```text
0.00 .. 1.00
```

---

## Uso de la confianza

La confianza será especialmente relevante en:

- inferencias;
- predicciones;
- sustituciones;
- maridajes;
- compatibilidades;
- equivalencias aproximadas;
- conocimiento importado;
- conocimiento generado mediante IA.

---

## Confianza y validez

Una confianza alta no convierte automáticamente una relación en canónica.

La canonicidad dependerá también de:

- fuente;
- revisión;
- evidencia;
- estado;
- gobernanza.

---

# Contexto

El contexto define las condiciones bajo las que una relación es válida.

Tipos de contexto:

- receta;
- técnica;
- región;
- tradición;
- dieta;
- temperatura;
- fase;
- equipo;
- fecha;
- usuario;
- objetivo;
- restricción;
- disponibilidad.

---

## Ejemplo contextual

```text
Yogur sustituye_a Nata
```

Contexto:

```yaml
contexto:
  aplicable_a:
    - salsas_frias
  proporcion: "1:1"
  limitaciones:
    - mayor_acidez
    - no_apto_para_montar
```

Sin este contexto, la relación podría resultar excesivamente general.

---

# Contextos múltiples

Una relación podrá tener varios contextos simultáneos.

Ejemplo:

```yaml
contexto:
  receta: REC-0042
  elaboracion: ELA-0004
  dieta: vegetariana
  fase: acabado
  temperatura: fria
```

---

# Contexto canónico y contexto de consulta

Deberá distinguirse entre:

- contexto almacenado como parte de la relación;
- contexto utilizado únicamente para consultar o filtrar.

Ejemplo:

La fase `sofrito` puede formar parte de la relación.

La consulta “recetas para invierno” no necesariamente modifica la relación almacenada.

---

# Temporalidad

Una relación podrá ser:

- atemporal;
- válida desde una fecha;
- válida hasta una fecha;
- válida durante un intervalo;
- recurrente;
- dependiente de un evento;
- histórica.

---

## Intervalo de validez

Modelo:

```yaml
validez:
  desde: 2026-01-01
  hasta: 2026-12-31
```

---

## Vigencia abierta

```yaml
validez:
  desde: 2026-07-30
  hasta: null
```

---

## Relación histórica

Una relación histórica deberá conservarse aunque ya no esté vigente.

Ejemplo:

```text
Componente antiguo ── sustituido_por ── Componente nuevo
```

---

## Tiempo de validez y tiempo de registro

Deberán distinguirse:

```text
Tiempo válido
```

Momento en el que la relación es verdadera en el dominio.

```text
Tiempo de registro
```

Momento en el que la relación fue incorporada al sistema.

Ejemplo:

```yaml
valido_desde: 2026-01-01
registrado_el: 2026-07-30
```

---

# Relaciones negativas

Una relación negativa afirma explícitamente que una relación no se cumple.

Ejemplo:

```text
REC-0042 ── no_contiene ── ING-0017
```

La negación deberá diferenciarse de la ausencia de información.

---

## Mundo abierto

Por defecto, el SGCC deberá adoptar una interpretación de mundo abierto para el conocimiento semántico.

Esto significa:

```text
Ausencia de relación

≠

Relación negativa
```

Que una receta no declare cacahuetes no significa que esté verificada como libre de cacahuetes.

---

## Mundo cerrado contextual

En determinados contextos validados podrá utilizarse una interpretación cerrada.

Ejemplo:

Una lista de ingredientes declarada como completa podría permitir afirmar que los ingredientes no listados no forman parte directa de la receta.

Este comportamiento deberá declararse explícitamente.

---

# Relaciones condicionales

Una relación condicional solo es válida cuando se cumple una condición.

Modelo:

```text
A sustituye_a B

si condición C
```

Representación:

```yaml
sujeto: ING-0012
relacion: sustituye_a
objeto: ING-0015

condiciones:
  - tipo_preparacion: salsa_fria
  - temperatura_maxima: 25
```

---

# Excepciones

Una relación podrá incluir excepciones.

Ejemplo:

```yaml
relacion: compatible_con

excepciones:
  - equipo_con_revestimiento_dañado
  - temperatura_superior_a_250
```

Las excepciones deberán:

- ser explícitas;
- ser verificables;
- tener prioridad sobre la regla general cuando se cumplan;
- conservar procedencia.

---

# Restricciones de integridad

Las relaciones deberán cumplir restricciones estructurales y semánticas.

---

## Restricción de tipos

El sujeto y el objeto deberán pertenecer a tipos compatibles con dominio y rango.

Ejemplo inválido:

```text
Colección ── requiere ── Ingrediente
```

salvo que el catálogo permita explícitamente esa combinación.

---

## Restricción de identidad

No deberán crearse relaciones irreflexivas de un componente consigo mismo.

Ejemplo inválido:

```text
REC-0042 variante_de REC-0042
```

---

## Restricción de ciclos

Las relaciones asimétricas y jerárquicas no deberán formar ciclos.

Ejemplo inválido:

```text
A subtipo_de B

B subtipo_de C

C subtipo_de A
```

---

## Restricción de cardinalidad

No deberán excederse mínimos o máximos definidos.

Ejemplo:

Un activo no deberá tener dos fuentes canónicas activas para el mismo idioma, formato y versión si la cardinalidad es `1..1`.

---

## Restricción de exclusividad

Algunas relaciones podrán ser mutuamente excluyentes.

Ejemplo:

```text
A satisface R
```

y:

```text
A incumple R
```

no deberán coexistir con el mismo contexto, periodo y criterio de validación.

---

## Restricción de consistencia inversa

Si se almacenan ambas direcciones, deberán ser coherentes.

---

## Restricción temporal

No deberán generarse intervalos inválidos.

Ejemplo:

```yaml
desde: 2026-12-01
hasta: 2026-01-01
```

---

# Conflictos semánticos

Un conflicto ocurre cuando varias relaciones no pueden considerarse simultáneamente válidas en el mismo contexto.

Ejemplo:

```text
REC-0042 satisface Restricción sin gluten
```

y:

```text
REC-0042 incumple Restricción sin gluten
```

---

# Tipos de conflicto

El SGCC deberá poder detectar:

- contradicción directa;
- incompatibilidad de cardinalidad;
- ciclo jerárquico;
- conflicto temporal;
- conflicto de identidad;
- conflicto de procedencia;
- conflicto entre fuentes;
- violación de dominio o rango;
- duplicidad semántica.

---

# Resolución de conflictos

Un conflicto deberá resolverse considerando:

1. contexto;
2. vigencia;
3. fuente;
4. estado;
5. nivel de evidencia;
6. autoridad;
7. versión;
8. revisión humana.

No deberá eliminarse automáticamente una relación únicamente porque otra la contradiga.

Podrán mantenerse ambas como afirmaciones procedentes de fuentes distintas mientras se resuelve el conflicto.

---

# Representación de conflictos

Ejemplo:

```yaml
conflicto:
  id: CONFLICT-0021

  relaciones:
    - REL-INST-0421
    - REL-INST-0894

  tipo: contradiccion_directa
  estado: pendiente_revision
```

---

# Duplicidad de relaciones

Dos relaciones se considerarán duplicadas cuando expresen la misma afirmación con:

- mismo sujeto;
- mismo predicado;
- mismo objeto;
- mismo contexto;
- misma vigencia.

Podrán mantenerse distintas si difieren en:

- procedencia;
- evidencia;
- autor;
- confianza;
- versión;
- contexto.

---

# Relaciones equivalentes procedentes de varias fuentes

Cuando varias fuentes confirmen la misma relación podrá:

- consolidarse una relación canónica;
- conservarse el conjunto de procedencias;
- aumentar la evidencia;
- mantener registros de contribución independientes.

Modelo:

```text
Relación canónica

├── respaldada_por Fuente A
├── respaldada_por Fuente B
└── respaldada_por Fuente C
```

---

# Versionado de relaciones

Una instancia de relación podrá versionarse cuando cambien:

- atributos;
- contexto;
- vigencia;
- evidencia;
- confianza;
- estado;
- significado operativo.

---

## Cambio editorial

No requerirá nueva versión conceptual cuando únicamente cambie:

- redacción;
- etiqueta;
- presentación;
- comentario;
- orden visual.

---

## Cambio compatible

Podrá incrementar versión menor cuando:

- se añada contexto opcional;
- se incorpore evidencia;
- se amplíe procedencia;
- se añada una excepción compatible.

---

## Cambio incompatible

Deberá incrementar versión mayor cuando:

- cambie el sujeto;
- cambie el predicado;
- cambie el objeto;
- se altere el significado;
- se invierta la dirección;
- se modifiquen condiciones esenciales;
- una relación deje de ser válida en contextos anteriormente permitidos.

---

# Estado de una relación

Una relación podrá encontrarse en:

```text
Borrador

En revisión

Estable

Obsoleta

Archivada

Rechazada
```

---

## Borrador

Relación propuesta todavía no validada.

---

## En revisión

Pendiente de evaluación semántica, técnica o culinaria.

---

## Estable

Aceptada como parte del conocimiento oficial.

---

## Obsoleta

Ya no debe utilizarse en nuevas contribuciones, pero conserva valor histórico.

---

## Archivada

Retirada del uso operativo.

---

## Rechazada

Evaluada y descartada.

La relación rechazada podrá conservarse para evitar su reintroducción sin nueva evidencia.

---

# Representación en Markdown

Una relación simple podrá declararse mediante metadatos.

Ejemplo:

```yaml
relaciones:
  - tipo: utiliza
    destino: ING-0017

  - tipo: aplica
    destino: TEC-0004
```

---

## Relación contextualizada en Markdown

```yaml
relaciones:
  - id: USO-ING-0084
    tipo: utiliza
    destino: ING-0017

    atributos:
      cantidad: 250
      unidad: g
      preparacion: juliana
      fase: sofrito
      opcional: false
```

---

## Referencia visible

Dentro del cuerpo documental podrá mostrarse:

```markdown
La receta utiliza [cebolla](../../../11_Despensa/06_Verduras/cebolla.md)
```

El enlace visible no sustituirá a la declaración semántica cuando esta sea necesaria para procesamiento automático.

---

# Representación en YAML

Ejemplo completo:

```yaml
id: REL-INST-0042
version: 1.0.0
estado: estable

sujeto: REC-0042
predicado: utiliza
objeto: ING-0017

atributos:
  cantidad: 250
  unidad: UNI-0003
  preparacion: cortada_en_juliana
  fase: ELA-0002
  opcional: false
  orden: 2

procedencia:
  fuente: DOC-0064
  autor: USER-0003
  fecha: 2026-07-30

validez:
  desde: 2026-07-30
  hasta: null
```

---

# Representación en JSON

```json
{
  "id": "REL-INST-0042",
  "version": "1.0.0",
  "estado": "estable",
  "sujeto": "REC-0042",
  "predicado": "utiliza",
  "objeto": "ING-0017",
  "atributos": {
    "cantidad": 250,
    "unidad": "UNI-0003",
    "preparacion": "cortada_en_juliana",
    "fase": "ELA-0002",
    "opcional": false,
    "orden": 2
  },
  "procedencia": {
    "fuente": "DOC-0064",
    "autor": "USER-0003",
    "fecha": "2026-07-30"
  },
  "validez": {
    "desde": "2026-07-30",
    "hasta": null
  }
}
```

---

# Representación relacional

En una base de datos relacional, una relación simple podrá representarse mediante:

```text
relationship
------------
id
subject_id
predicate_id
object_id
version
status
valid_from
valid_to
```

Los atributos adicionales podrán almacenarse mediante:

- columnas especializadas;
- tablas asociativas;
- estructuras JSON;
- tablas de propiedades;
- modelos híbridos.

---

# Tabla asociativa especializada

Ejemplo:

```text
recipe_ingredient_use
---------------------
id
recipe_id
ingredient_id
quantity
unit_id
preparation_id
elaboration_id
optional
position
```

Esta representación será preferible cuando la relación tenga:

- alta frecuencia;
- estructura estable;
- restricciones claras;
- consultas específicas;
- necesidad de rendimiento.

---

# Representación en grafo de propiedades

Modelo:

```text
(Receta)-[UTILIZA]->(Ingrediente)
```

Con propiedades:

```text
(Receta)-[
    UTILIZA {
        cantidad: 250,
        unidad: "g",
        fase: "sofrito",
        opcional: false
    }
]->(Ingrediente)
```

---

## Relación con identidad en grafo de propiedades

Cuando la relación necesite participar como nodo:

```text
(Receta)-[:TIENE_USO]->(UsoIngrediente)

(UsoIngrediente)-[:REFERENCIA_A]->(Ingrediente)
```

---

# Representación en RDF

Una relación simple podrá representarse mediante una triple:

```turtle
:REC-0042 :utiliza :ING-0017 .
```

---

## Relación contextualizada en RDF

Podrá utilizarse reificación o una entidad intermedia:

```turtle
:USO-ING-0084
    a :UsoDeIngrediente ;
    :receta :REC-0042 ;
    :ingrediente :ING-0017 ;
    :cantidad 250 ;
    :unidad :Gramo ;
    :fase :Sofrito ;
    :opcional false .
```

La futura especificación ontológica decidirá el patrón definitivo.

---

# Representación mediante API

Una API podrá devolver relaciones simples:

```json
{
  "subject": "REC-0042",
  "predicate": "pertenece_a",
  "object": "COL-0008"
}
```

O relaciones contextualizadas:

```json
{
  "id": "USO-ING-0084",
  "type": "uso_de_ingrediente",
  "recipe": "REC-0042",
  "ingredient": "ING-0017",
  "quantity": {
    "value": 250,
    "unit": "UNI-0003"
  },
  "preparation": "cortada_en_juliana",
  "phase": "ELA-0002",
  "optional": false
}
```

---

# Compatibilidad entre representaciones

Una misma relación podrá representarse mediante distintas tecnologías.

Ejemplo:

```text
Relación conceptual

├── Markdown
├── YAML
├── JSON
├── Base de datos relacional
├── Grafo de propiedades
├── RDF
└── API
```

Todas las representaciones deberán preservar:

- sujeto;
- predicado;
- objeto;
- identidad;
- contexto;
- procedencia;
- temporalidad;
- estado;
- versión.

---

# Fuente canónica

Toda relación deberá disponer de una estrategia de autoridad.

Podrá existir:

```text
Fuente canónica única
```

o:

```text
Registro canónico central
```

Las demás representaciones deberán considerarse:

- vistas;
- copias;
- cachés;
- exportaciones;
- materializaciones;
- derivados.

---

# Sincronización

Cuando una relación tenga varias representaciones deberán definirse:

- origen de actualización;
- dirección de sincronización;
- resolución de conflictos;
- control de versiones;
- frecuencia;
- mecanismo de validación.

---

# Materialización

Una relación inferida podrá materializarse para mejorar:

- consultas;
- navegación;
- rendimiento;
- análisis;
- recuperación semántica.

La materialización deberá conservar:

- regla de origen;
- fecha de cálculo;
- relaciones base;
- posibilidad de regeneración;
- indicador de que no fue declarada directamente.

---

# Desmaterialización

Una relación derivada o calculada podrá eliminarse físicamente si puede regenerarse y no constituye la fuente canónica.

Su eliminación no deberá afectar a:

- relaciones declaradas;
- procedencia;
- reglas de inferencia;
- historial necesario.

---

# Validación estructural

La validación estructural deberá comprobar:

- identificador válido;
- sujeto existente;
- predicado reconocido;
- objeto existente;
- dominio correcto;
- rango correcto;
- cardinalidad;
- formato;
- atributos obligatorios;
- estado;
- versión.

---

# Validación semántica

La validación semántica deberá comprobar:

- significado adecuado;
- dirección canónica;
- relación más específica disponible;
- compatibilidad contextual;
- coherencia con restricciones;
- ausencia de ciclos inválidos;
- ausencia de contradicción no gestionada;
- coherencia temporal;
- calidad de procedencia.

---

# Validación de relaciones contextualizadas

Deberá comprobarse:

- presencia de contexto obligatorio;
- tipo de cada atributo;
- unidad válida;
- referencias existentes;
- coherencia entre cantidad y unidad;
- fase válida;
- condiciones y excepciones;
- integridad de la entidad asociativa.

---

# Validación de inferencias

Toda inferencia deberá verificar:

- existencia de relaciones base;
- vigencia de la regla;
- compatibilidad de contextos;
- ausencia de excepciones;
- versión del razonador;
- reproducibilidad;
- procedencia;
- nivel de confianza.

---

# Validación automática

Las herramientas del SGCC podrán detectar:

- relaciones duplicadas;
- predicados desconocidos;
- dominio inválido;
- rango inválido;
- cardinalidad incorrecta;
- ciclos;
- inversas inconsistentes;
- referencias rotas;
- intervalos temporales inválidos;
- atributos incompletos;
- conflictos directos;
- relaciones obsoletas.

---

# Validación humana

La revisión humana será necesaria para evaluar:

- precisión semántica;
- contexto culinario;
- calidad de sustituciones;
- validez de maridajes;
- pertinencia de inferencias;
- ambigüedad;
- excepciones;
- evidencia;
- impacto sobre el modelo.

---

# Calidad de las relaciones

Una relación de alta calidad deberá ser:

- precisa;
- verificable;
- trazable;
- contextualizada cuando proceda;
- consistente;
- reutilizable;
- comprensible;
- interoperable;
- validable.

---

# Métricas de calidad

El SGCC podrá medir:

- porcentaje de relaciones con procedencia;
- porcentaje de relaciones validadas;
- relaciones duplicadas;
- relaciones genéricas;
- conflictos abiertos;
- relaciones sin contexto obligatorio;
- cobertura de inversas;
- cobertura de dominio y rango;
- relaciones obsoletas;
- densidad del grafo;
- conectividad por tipo;
- porcentaje de relaciones inferidas.

---

# Cobertura relacional

La cobertura expresa hasta qué punto los componentes están correctamente conectados.

Ejemplo:

```text
Recetas con ingredientes declarados

Recetas con técnicas declaradas

Recetas con resultados declarados

Recetas con procedencia

Recetas con restricciones evaluadas
```

Una cobertura elevada no garantiza calidad si las relaciones son genéricas o incorrectas.

---

# Densidad del grafo

La densidad mide el número de relaciones existentes respecto al número posible.

No deberá buscarse maximizar la densidad de forma indiscriminada.

El objetivo será:

```text
Máxima utilidad semántica

con

Mínima redundancia
```

---

# Relaciones huérfanas

Una relación será huérfana cuando:

- su sujeto no exista;
- su objeto no exista;
- su predicado haya sido eliminado;
- su contexto apunte a componentes inexistentes.

Las relaciones huérfanas deberán bloquearse o marcarse como inválidas.

---

# Componentes aislados

Un componente podrá considerarse aislado cuando no mantenga relaciones mínimas esperadas.

Ejemplo:

Una receta estable sin:

- ingredientes;
- técnicas;
- resultado;
- documento canónico.

La existencia de componentes aislados deberá generar advertencias.

---

# Navegabilidad

Las relaciones deberán permitir recorrer el conocimiento en ambos sentidos cuando sea útil.

Ejemplo:

```text
Receta

↓

utiliza

↓

Ingrediente

↓

sustituye_a

↓

Ingrediente alternativo

↓

es_utilizado_por

↓

Otra receta
```

Esta navegabilidad constituye uno de los principales valores del Knowledge Graph.

---

# Recuperación semántica

Las relaciones mejorarán la búsqueda permitiendo consultas como:

```text
Recetas que utilicen miso
```

```text
Ingredientes que sustituyan a la nata
```

```text
Técnicas que requieran horno
```

```text
Recetas incompatibles con una dieta sin gluten
```

```text
Elaboraciones que precedan al horneado
```

---

# Compatibilidad con sistemas RAG

Los sistemas RAG podrán utilizar las relaciones para:

- expandir consultas;
- recuperar componentes vecinos;
- priorizar fuentes;
- construir contexto;
- justificar respuestas;
- evitar asociaciones incorrectas.

Ejemplo:

```text
Consulta: recetas con garbanzos sin gluten
```

El sistema podrá recorrer:

```text
Receta ── utiliza ── Garbanzo

Receta ── satisface ── Restricción sin gluten
```

---

# Compatibilidad con agentes de inteligencia artificial

Los agentes podrán utilizar las relaciones para:

- planificar menús;
- detectar incompatibilidades;
- proponer sustituciones;
- calcular compras;
- reutilizar sobras;
- explicar decisiones;
- validar restricciones;
- generar variantes.

Toda acción automática deberá conservar:

- relaciones utilizadas;
- reglas aplicadas;
- contexto;
- procedencia;
- nivel de confianza.

---

# Explicabilidad

Toda conclusión producida a partir de relaciones deberá poder explicarse mediante una ruta.

Ejemplo:

```text
La receta no es apta para una dieta sin gluten porque:

REC-0042 utiliza ING-0017

ING-0017 es_un Harina de trigo

Harina de trigo contiene_alergeno Gluten

Restricción sin gluten excluye Gluten
```

La explicación deberá mostrar:

- componentes;
- relaciones;
- reglas;
- fuentes;
- confianza;
- excepciones.

---

# Seguridad semántica

Las relaciones vinculadas con:

- alergias;
- seguridad alimentaria;
- toxicidad;
- conservación;
- nutrición;
- higiene;

deberán exigir niveles superiores de:

- procedencia;
- evidencia;
- validación;
- revisión;
- control de cambios.

Las inferencias generadas mediante IA no deberán convertirse automáticamente en conocimiento canónico de seguridad.

---

# Privacidad y control de acceso

Algunas relaciones podrán contener información sensible.

Ejemplos:

```text
Usuario ── tiene_restriccion ── Condición dietética
```

```text
Tarea ── asignada_a ── Persona
```

La visibilidad de una relación podrá depender de:

- rol;
- propietario;
- contexto;
- finalidad;
- política de acceso;
- consentimiento.

---

# Permisos sobre relaciones

El sistema podrá distinguir permisos como:

```text
crear_relacion

consultar_relacion

modificar_relacion

validar_relacion

deprecar_relacion

inferir_relacion

publicar_relacion
```

Las relaciones canónicas no deberán modificarse sin autorización.

---

# Auditoría

Toda modificación relevante deberá poder registrar:

- relación afectada;
- valor anterior;
- valor nuevo;
- usuario o sistema;
- fecha;
- motivo;
- evidencia;
- versión.

Ejemplo:

```yaml
auditoria:
  accion: modificar
  relacion: REL-INST-0042
  campo: cantidad
  anterior: 200
  nuevo: 250
  autor: USER-0003
  fecha: 2026-07-30
```

---

# Ciclo operativo de una relación

El ciclo general podrá representarse como:

```text
Propuesta

↓

Validación estructural

↓

Validación semántica

↓

Revisión

↓

Publicación

↓

Uso

↓

Evolución

↓

Deprecación

↓

Archivado
```

---

# Reglas mínimas de implementación

Toda implementación del modelo relacional del SGCC deberá:

- preservar identificadores;
- distinguir sujeto, predicado y objeto;
- soportar contexto;
- soportar procedencia;
- distinguir relaciones declaradas e inferidas;
- permitir validación;
- respetar dominio y rango;
- gestionar versionado;
- preservar historial;
- permitir representación interoperable.

---

# Perfil mínimo de relación

Una implementación inicial podrá limitarse a:

```yaml
id: REL-INST-0001
sujeto: REC-0001
predicado: utiliza
objeto: ING-0001
estado: estable
```

---

# Perfil recomendado

El perfil recomendado deberá incluir:

```yaml
id: REL-INST-0001
version: 1.0.0
estado: estable

sujeto: REC-0001
predicado: utiliza
objeto: ING-0001

contexto: {}
atributos: {}

procedencia:
  fuente: DOC-0001
  fecha: 2026-07-30

origen_semantico: declarada
```

---

# Perfil avanzado

El perfil avanzado podrá incorporar:

- temporalidad;
- evidencia;
- confianza;
- reglas de inferencia;
- contexto múltiple;
- permisos;
- auditoría;
- firma;
- validación;
- traducciones;
- equivalencias externas.

---

# Conformidad estructural

Una relación será estructuralmente conforme cuando:

- disponga de identidad cuando sea necesaria;
- tenga sujeto válido;
- utilice un predicado reconocido;
- tenga objeto válido;
- respete dominio y rango;
- cumpla cardinalidades;
- contenga los atributos obligatorios;
- mantenga referencias existentes;
- utilice formatos válidos.

---

# Conformidad semántica

Una relación será semánticamente conforme cuando:

- exprese el significado declarado por su tipo;
- utilice la dirección canónica;
- incluya contexto suficiente;
- no contradiga restricciones activas;
- distinga hechos e inferencias;
- preserve procedencia;
- no use relaciones genéricas innecesarias;
- mantenga coherencia con la ontología.

---

# Conformidad de inferencias

Una relación inferida será conforme cuando:

- proceda de una regla reconocida;
- utilice relaciones base válidas;
- mantenga compatibilidad contextual;
- sea reproducible;
- declare su origen;
- incluya confianza cuando proceda;
- no se presente como relación declarada;
- pueda invalidarse si cambian sus premisas.

---

# Transición hacia la gobernanza

La presente parte ha definido:

- relaciones simples y contextualizadas;
- relaciones binarias y n-arias;
- entidades asociativas;
- dirección e inversas;
- cardinalidad;
- propiedades lógicas;
- inferencia;
- procedencia;
- evidencia;
- temporalidad;
- conflictos;
- versionado;
- representación técnica;
- validación;
- compatibilidad con Knowledge Graph, RAG y agentes IA.

La parte final de esta especificación deberá establecer:

- cómo se crean nuevos tipos de relación;
- cómo se modifican;
- cómo se versionan;
- cómo se deprecan;
- cómo se resuelven cambios incompatibles;
- qué responsabilidades intervienen;
- qué validaciones son obligatorias;
- cómo se garantiza la gobernanza del vocabulario relacional.

---

# Gobernanza y evolución de relaciones

Esta sección establece las reglas para crear, modificar, versionar, validar, deprecar, sustituir y retirar tipos e instancias de relación dentro del SGCC.

La evolución del vocabulario relacional deberá gestionarse de forma controlada.

Una modificación aparentemente pequeña puede afectar a:

- documentos;
- componentes;
- colecciones;
- validadores;
- esquemas;
- ontología;
- Knowledge Graph;
- consultas;
- APIs;
- sistemas RAG;
- agentes de inteligencia artificial;
- reglas de inferencia.

Por este motivo, las relaciones deberán tratarse como elementos normativos del modelo de conocimiento y no como simples etiquetas técnicas.

---

# Objetivos de la gobernanza

La gobernanza del modelo relacional deberá garantizar:

- estabilidad semántica;
- ausencia de duplicidades;
- trazabilidad;
- compatibilidad;
- extensibilidad controlada;
- coherencia con los componentes;
- integridad del Knowledge Graph;
- calidad de las inferencias;
- interoperabilidad;
- evolución sostenible.

---

# Principios de gobernanza

La gobernanza de relaciones se regirá por los siguientes principios.

---

## Necesidad semántica

No deberá crearse una nueva relación cuando la necesidad pueda resolverse mediante:

- una relación existente;
- una relación inversa;
- una especialización;
- un atributo de relación;
- una entidad asociativa;
- una regla de inferencia;
- una combinación de relaciones existentes;
- un alias terminológico.

La creación de un nuevo predicado deberá responder a una diferencia real de significado.

---

## Significado estable

Toda relación deberá poseer una semántica suficientemente estable para reutilizarse en múltiples instancias.

No deberán incorporarse relaciones cuyo significado dependa completamente de:

- un documento concreto;
- una implementación temporal;
- una consulta aislada;
- una interfaz específica;
- una necesidad circunstancial.

---

## Precisión

Deberá preferirse una relación específica frente a una genérica.

Ejemplo:

```text
utiliza
```

será preferible a:

```text
relacionado_con
```

cuando exista una relación de uso real.

---

## No duplicidad

No deberán existir relaciones diferentes con significado equivalente.

Ejemplo problemático:

```text
usa

utiliza

emplea
```

Si expresan la misma semántica deberán consolidarse bajo una única relación canónica.

Las demás formas podrán conservarse como:

- alias;
- sinónimos;
- etiquetas de interfaz;
- traducciones.

---

## Identidad persistente

Todo tipo de relación deberá disponer de un identificador estable.

El identificador no deberá cambiar aunque cambien:

- el nombre visible;
- la descripción;
- la traducción;
- la ubicación documental;
- la implementación técnica.

---

## Orientación canónica

Toda relación dirigida deberá poseer una dirección oficial.

Ejemplo:

```text
Variante ── variante_de ── Original
```

No deberá utilizarse de forma intercambiable con la dirección contraria.

La perspectiva inversa deberá expresarse mediante una relación inversa reconocida.

---

## Independencia tecnológica

La gobernanza deberá regular el significado de la relación, no una representación concreta.

Una relación podrá materializarse mediante:

- Markdown;
- YAML;
- JSON;
- tabla relacional;
- arista de grafo;
- nodo asociativo;
- triple RDF;
- recurso API.

La representación no deberá redefinir la semántica.

---

## Compatibilidad progresiva

Los cambios deberán preservar siempre que sea posible:

- identificadores;
- significado;
- relaciones existentes;
- procedencia;
- historial;
- reglas de inferencia;
- compatibilidad con representaciones anteriores.

---

## Trazabilidad

Todo cambio relevante deberá poder rastrearse hasta:

- propuesta;
- autor;
- revisión;
- decisión;
- versión;
- commit;
- pull request;
- ADR cuando corresponda;
- entrada en BITÁCORA.

---

# Alcance de la gobernanza

La gobernanza se aplica a:

- tipos de relación;
- relaciones inversas;
- especializaciones;
- atributos de relación;
- entidades asociativas;
- reglas de inferencia;
- restricciones;
- cardinalidades;
- dominio;
- rango;
- aliases;
- traducciones;
- estados;
- representaciones;
- instancias canónicas.

---

# Registro de relaciones

El SGCC deberá mantener un registro oficial de tipos de relación.

Cada entrada deberá incluir, como mínimo:

```text
Identificador

Nombre canónico

Definición

Familia

Dominio

Rango

Dirección

Cardinalidad

Relación inversa

Características lógicas

Estado

Versión
```

Podrá incluir además:

```text
Alias

Traducciones

Subrelaciones

Propiedades

Restricciones

Reglas de inferencia

Ejemplos

Contraejemplos

Fecha de incorporación

Fecha de deprecación

Sustituto
```

---

# Creación de nuevos tipos de relación

Toda nueva relación deberá partir de una propuesta formal.

---

## Preguntas previas obligatorias

Antes de proponer una nueva relación deberán responderse las siguientes preguntas:

1. ¿Qué significado exacto expresa?
2. ¿Existe ya una relación equivalente?
3. ¿Puede resolverse mediante un alias?
4. ¿Puede resolverse mediante una relación inversa?
5. ¿Puede representarse como especialización de otra relación?
6. ¿Puede modelarse mediante un atributo?
7. ¿Puede obtenerse mediante una regla de inferencia?
8. ¿Tiene dominio y rango definidos?
9. ¿Su dirección es inequívoca?
10. ¿Dispone de casos de uso reales?
11. ¿Puede validarse?
12. ¿Qué impacto tendrá sobre la ontología y el Knowledge Graph?

Si estas preguntas no pueden responderse con claridad, la relación no deberá incorporarse.

---

# Criterios de aceptación

Una nueva relación podrá aceptarse cuando:

- posea semántica diferenciada;
- sea reutilizable;
- no duplique relaciones existentes;
- tenga nombre canónico claro;
- disponga de dominio y rango;
- permita establecer una dirección coherente;
- pueda documentar cardinalidades;
- tenga restricciones verificables;
- aporte valor al modelo;
- sea compatible con la arquitectura;
- pueda representarse en las tecnologías soportadas;
- disponga de ejemplos y contraejemplos.

---

# Información mínima de una propuesta

Toda propuesta deberá incluir:

```text
Nombre propuesto

Definición

Motivación

Problema que resuelve

Dominio

Rango

Dirección

Cardinalidad

Relación inversa

Características lógicas

Atributos contextuales

Restricciones

Ejemplos válidos

Contraejemplos

Relaciones alternativas evaluadas

Impacto previsto
```

---

# Plantilla de propuesta

```yaml
propuesta:
  nombre: contiene_alergeno
  familia: restriccion

  definicion: >
    Expresa que un componente contiene directa o indirectamente
    un alérgeno identificado.

  dominio:
    - ingrediente
    - receta
    - elaboracion
    - base_culinaria

  rango:
    - alergeno

  direccion: dirigida

  inversa: presente_en

  caracteristicas:
    simetrica: false
    transitiva: condicionada
    reflexiva: false

  motivacion: >
    Permitir validación de restricciones alimentarias y
    generación de inferencias explicables.

  alternativas_evaluadas:
    - contiene
    - incumple
    - relacionado_con
```

---

# Procedimiento de incorporación

La incorporación de una nueva relación seguirá el siguiente proceso:

```text
Necesidad detectada

↓

Análisis del catálogo

↓

Propuesta formal

↓

Revisión semántica

↓

Revisión estructural

↓

Revisión arquitectónica

↓

Aprobación

↓

Actualización normativa

↓

Implementación

↓

Validación

↓

Publicación
```

---

# Análisis del catálogo existente

Antes de crear una relación deberán revisarse:

- relaciones canónicas;
- inversas;
- alias;
- especializaciones;
- familias;
- reglas de inferencia;
- relaciones obsoletas.

El análisis deberá justificar por qué ninguna relación existente cubre adecuadamente la necesidad.

---

# Revisión semántica

La revisión semántica deberá comprobar:

- claridad de significado;
- diferenciación respecto a relaciones próximas;
- consistencia terminológica;
- dirección;
- posibilidad de lectura como frase;
- riesgo de ambigüedad;
- aplicabilidad en distintos contextos.

---

# Revisión estructural

La revisión estructural deberá comprobar:

- dominio;
- rango;
- cardinalidades;
- relación inversa;
- simetría;
- transitividad;
- reflexividad;
- propiedades obligatorias;
- restricciones de integridad;
- necesidad de entidad asociativa.

---

# Revisión arquitectónica

La revisión arquitectónica deberá evaluar:

- impacto sobre el modelo de componentes;
- impacto sobre la ontología;
- impacto sobre validadores;
- impacto sobre esquemas;
- impacto sobre APIs;
- impacto sobre almacenamiento;
- impacto sobre reglas de inferencia;
- impacto sobre herramientas RAG;
- impacto sobre agentes IA.

---

# Aprobación

Una relación deberá considerarse aprobada únicamente cuando:

- su semántica haya sido validada;
- su estructura haya sido definida;
- no exista duplicidad;
- se haya evaluado el impacto;
- disponga de documentación;
- pueda validarse;
- haya sido incorporada al registro oficial.

---

# Actualización normativa

La incorporación de una relación podrá requerir actualizar:

- `ESPECIFICACION_DE_RELACIONES.md`;
- `ESPECIFICACION_DE_COMPONENTES.md`;
- `ESPECIFICACION_DE_ONTOLOGIA.md`;
- `MODELO_DE_CONOCIMIENTO.md`;
- esquemas;
- taxonomías;
- validadores;
- documentación de APIs;
- catálogos;
- ejemplos;
- reglas de inferencia.

---

# Modificación de relaciones existentes

Las relaciones podrán modificarse cuando el cambio preserve o evolucione de forma controlada su significado.

---

# Cambios editoriales

Se consideran editoriales:

- correcciones ortográficas;
- mejoras de redacción;
- nuevos ejemplos;
- nuevas traducciones;
- reorganización documental;
- aclaraciones que no alteren la semántica.

Estos cambios no requerirán una nueva versión mayor.

---

# Cambios compatibles

Se consideran normalmente compatibles:

- añadir alias;
- añadir traducciones;
- incorporar ejemplos;
- añadir atributos opcionales;
- ampliar rangos compatibles;
- ampliar dominios compatibles;
- añadir restricciones no retroactivas;
- registrar una relación inversa calculable;
- mejorar la procedencia.

Estos cambios deberán revisarse para asegurar que no invaliden instancias existentes.

---

# Cambios potencialmente incompatibles

Requieren análisis especial:

- modificar dominio;
- modificar rango;
- cambiar cardinalidades;
- cambiar dirección;
- añadir atributos obligatorios;
- cambiar la relación inversa;
- declarar transitividad;
- declarar simetría;
- modificar reglas de inferencia;
- restringir contextos anteriormente válidos.

---

# Cambios incompatibles

Se consideran incompatibles:

- cambiar el significado central;
- reutilizar el identificador para otra semántica;
- invertir la dirección canónica;
- eliminar tipos válidos del dominio sin migración;
- eliminar tipos válidos del rango sin migración;
- modificar una relación simétrica a asimétrica;
- transformar una relación binaria en n-aria sin estrategia;
- eliminar atributos obligatorios con significado histórico;
- fusionar semánticas diferentes bajo un único predicado.

Los cambios incompatibles deberán implicar:

- nueva versión mayor;
- estrategia de migración;
- actualización normativa;
- periodo de transición;
- revisión de instancias;
- actualización de inferencias;
- registro en BITÁCORA;
- ADR cuando corresponda.

---

# Versionado del catálogo relacional

El catálogo seguirá versionado semántico:

```text
MAJOR.MINOR.PATCH
```

---

## Versión mayor

Se incrementará cuando existan cambios incompatibles.

Ejemplos:

- redefinición de una relación;
- eliminación de relaciones canónicas;
- cambios de dirección;
- reestructuración de familias;
- modificación incompatible de dominio o rango;
- cambio del modelo de contextualización.

---

## Versión menor

Se incrementará cuando se incorporen cambios compatibles.

Ejemplos:

- nuevas relaciones;
- nuevas inversas;
- nuevos atributos opcionales;
- nuevas especializaciones;
- ampliaciones compatibles de dominio o rango;
- nuevas reglas de inferencia compatibles.

---

## Versión de parche

Se incrementará para:

- correcciones;
- aclaraciones;
- ejemplos;
- traducciones;
- referencias;
- mejoras editoriales;
- ajustes no semánticos.

---

# Versionado de tipos de relación

Cada tipo podrá disponer de su propia versión.

Ejemplo:

```yaml
id: REL-0060
nombre: sustituye_a
version: 2.1.0
```

La versión del tipo no deberá confundirse con:

- la versión del documento;
- la versión de la ontología;
- la versión de una instancia concreta;
- la versión de una representación.

---

# Versionado de instancias

Una instancia podrá requerir versión propia cuando cambien:

- sujeto;
- objeto;
- contexto;
- atributos;
- condiciones;
- excepciones;
- vigencia;
- procedencia;
- estado;
- confianza.

Ejemplo:

```yaml
id: REL-INST-0042
version: 2.0.0
```

---

# Compatibilidad entre versiones

Cada nueva versión deberá declarar:

```text
Compatible hacia atrás

Compatible parcialmente

Incompatible
```

Podrá expresarse mediante:

```yaml
compatibilidad:
  versiones_anteriores: parcial
  desde: 1.2.0
  requiere_migracion: true
```

---

# Migración de relaciones

Cuando un cambio afecte a instancias existentes deberá definirse una estrategia de migración.

---

## Plan mínimo de migración

El plan deberá incluir:

- relación de origen;
- relación de destino;
- reglas de transformación;
- atributos afectados;
- contexto;
- validaciones;
- estrategia de reversión;
- tratamiento del historial.

---

## Ejemplo de migración

Supóngase que:

```text
relacionado_con
```

se reemplaza por relaciones más específicas.

La migración podría requerir:

```text
relacionado_con

├── utiliza
├── deriva_de
├── pertenece_a
├── similar_a
└── compatible_con
```

La conversión no deberá realizarse automáticamente sin suficiente contexto.

---

# Deprecación de tipos de relación

Una relación podrá declararse obsoleta cuando:

- haya sido sustituida;
- resulte ambigua;
- duplique otra relación;
- sea demasiado genérica;
- haya quedado fuera del modelo;
- no pueda validarse;
- produzca inferencias incorrectas.

---

# Estado obsoleto

Una relación obsoleta:

- conservará su identificador;
- no deberá utilizarse en nuevas instancias;
- permanecerá disponible para interpretación histórica;
- deberá indicar su sustituto;
- deberá incluir instrucciones de migración.

Ejemplo:

```yaml
id: REL-0130
nombre: relacionado_con
estado: obsoleto
sustituido_por:
  - REL-0010
  - REL-0055
  - REL-0080
```

---

# Periodo de transición

La deprecación deberá incluir cuando corresponda:

- fecha de inicio;
- versión;
- sustituto;
- periodo de compatibilidad;
- fecha prevista de retirada;
- herramienta de migración;
- impacto conocido.

---

# Retirada

Una relación retirada:

- no deberá aceptarse en nuevas contribuciones;
- no participará en nuevas inferencias;
- podrá mantenerse para lectura histórica;
- deberá resolverse mediante compatibilidad o migración.

---

# Archivado

El archivado preserva una relación fuera del uso operativo.

Una relación archivada:

- conservará identidad;
- conservará historial;
- no aparecerá en el catálogo activo;
- no deberá utilizarse en nuevas instancias;
- podrá consultarse en auditorías.

---

# Eliminación física

La eliminación física deberá evitarse.

Solo podrá realizarse si:

- la relación fue creada por error;
- nunca fue publicada;
- no tiene instancias válidas;
- no participa en inferencias;
- no ha sido referenciada;
- no forma parte del historial oficial.

En los demás casos deberá aplicarse:

```text
Deprecación

↓

Migración

↓

Archivado
```

---

# Renombrado de relaciones

El nombre visible podrá cambiar sin alterar la identidad.

Ejemplo:

```text
Nombre anterior: usa
Nombre nuevo: utiliza
Identificador: REL-0010
```

El renombrado deberá conservar:

- identificador;
- alias anterior;
- historial;
- compatibilidad;
- traducciones;
- documentación de migración cuando sea necesaria.

---

# Cambio de dirección

Cambiar la dirección canónica de una relación será un cambio incompatible.

Ejemplo:

```text
Variante ── variante_de ── Original
```

no deberá redefinirse como:

```text
Original ── variante_de ── Variante
```

La dirección contraria deberá representarse mediante la inversa:

```text
Original ── tiene_variante ── Variante
```

---

# Creación de relaciones inversas

Una relación inversa podrá incorporarse cuando:

- mejore la legibilidad;
- facilite consultas;
- sea semánticamente estable;
- no introduzca ambigüedad;
- pueda mantenerse coherente.

No será obligatorio almacenar la inversa si puede inferirse.

---

# Fusión de relaciones

Dos relaciones podrán fusionarse cuando se demuestre que expresan el mismo significado.

Ejemplo:

```text
usa

+

emplea

↓

utiliza
```

La fusión deberá definir:

- relación superviviente;
- alias preservados;
- instancias migradas;
- reglas de inferencia actualizadas;
- historial;
- compatibilidad.

---

# División de relaciones

Una relación podrá dividirse cuando abarque significados diferentes.

Ejemplo:

```text
contiene
```

podría dividirse conceptualmente en:

```text
compuesto_por

incluye

contiene_alergeno

agrupa
```

La división deberá:

- definir nuevas relaciones;
- mantener la relación original como obsoleta;
- migrar instancias cuando sea posible;
- marcar casos ambiguos para revisión;
- conservar trazabilidad.

---

# Especialización de relaciones

Una relación general podrá especializarse.

Ejemplo:

```text
utiliza
    │
    ├── utiliza_ingrediente
    ├── utiliza_equipo
    ├── utiliza_tecnica
    └── utiliza_base
```

La especialización deberá:

- conservar la semántica de la relación general;
- añadir restricciones;
- definir dominio y rango más específicos;
- permitir inferir la relación general.

Ejemplo:

```text
Receta utiliza_ingrediente Cebolla
```

podrá implicar:

```text
Receta utiliza Cebolla
```

---

# Generalización de relaciones

Varias relaciones podrán agruparse bajo una superrelación.

Ejemplo:

```text
utiliza

requiere

aplica

↓

depende_funcionalmente_de
```

La generalización deberá aportar valor para:

- consulta;
- inferencia;
- organización;
- interoperabilidad.

No deberá eliminar diferencias semánticas importantes.

---

# Alias

Los alias permiten representar variantes terminológicas sin crear nuevos predicados.

Ejemplo:

```yaml
nombre_canonico: utiliza

alias:
  - usa
  - emplea
  - hace_uso_de
```

Los alias:

- no tendrán identidad relacional independiente;
- no deberán aparecer como predicados canónicos;
- podrán utilizarse para búsqueda;
- podrán utilizarse en interfaces;
- deberán resolverse al nombre canónico.

---

# Traducciones

Las traducciones deberán conservar el identificador de la relación.

Ejemplo:

```yaml
id: REL-0010

etiquetas:
  es: utiliza
  en: uses
  fr: utilise
  pt: utiliza
```

La traducción no deberá alterar:

- dirección;
- dominio;
- rango;
- cardinalidad;
- semántica.

---

# Gobernanza de atributos de relación

Los atributos asociados a una relación también deberán regularse.

Ejemplo:

```text
utiliza
    │
    ├── cantidad
    ├── unidad
    ├── fase
    ├── orden
    └── opcionalidad
```

---

## Creación de atributos

Un nuevo atributo deberá:

- describir la instancia;
- no pertenecer globalmente al sujeto;
- no pertenecer globalmente al objeto;
- ser reutilizable;
- tener tipo definido;
- disponer de restricciones;
- aportar información necesaria.

---

## Atributo frente a componente

Deberá modelarse como componente cuando:

- tenga identidad propia;
- participe en otras relaciones;
- sea reutilizable;
- tenga propiedades propias;
- requiera gobernanza independiente.

Ejemplo:

```text
unidad: gramos
```

podrá ser una referencia a:

```text
UNI-0001
```

en lugar de un texto libre.

---

# Gobernanza de entidades asociativas

La creación de una entidad asociativa deberá justificarse.

Ejemplos:

- uso de ingrediente;
- sustitución contextual;
- asignación de tarea;
- observación culinaria;
- relación de equivalencia de unidades.

---

## Requisitos

Toda entidad asociativa deberá definir:

- identidad;
- participantes;
- roles;
- propiedades;
- cardinalidad;
- ciclo de vida;
- procedencia;
- validación;
- representación.

---

# Gobernanza de reglas de inferencia

Las reglas de inferencia constituyen parte del contrato semántico.

No deberán incorporarse de forma informal.

---

## Registro de reglas

Cada regla deberá incluir:

```text
Identificador

Nombre

Premisas

Conclusión

Condiciones

Excepciones

Confianza

Versión

Estado

Procedencia
```

---

## Ejemplo

```yaml
id: REG-INF-0007
nombre: inferir_incumplimiento_sin_gluten

premisas:
  - receta utiliza ingrediente
  - ingrediente contiene_alergeno gluten
  - restriccion excluye gluten

conclusion:
  - receta incumple restriccion

estado: estable
version: 1.0.0
```

---

## Validación de reglas

Las reglas deberán comprobar:

- validez lógica;
- compatibilidad contextual;
- ausencia de ciclos no controlados;
- ausencia de sobreinferencias;
- reproducibilidad;
- explicabilidad;
- impacto sobre seguridad;
- comportamiento ante excepciones.

---

## Cambios en reglas

La modificación de una regla podrá invalidar relaciones inferidas existentes.

Toda actualización deberá considerar:

- recalcular;
- desmaterializar;
- invalidar;
- mantener historial;
- comparar resultados;
- actualizar explicaciones.

---

# Gobernanza de relaciones predichas por IA

Las relaciones generadas mediante IA deberán tratarse como propuestas o predicciones, no como hechos canónicos automáticos.

---

## Requisitos mínimos

Deberán registrar:

- modelo;
- versión;
- fecha;
- parámetros relevantes;
- entrada utilizada;
- confianza;
- explicación disponible;
- estado de revisión.

---

## Estados recomendados

```text
Predicha

↓

Pendiente de revisión

↓

Validada

o

Rechazada
```

---

## Restricciones

Las relaciones predichas no deberán utilizarse automáticamente para decisiones de alto impacto relacionadas con:

- alergias;
- toxicidad;
- seguridad alimentaria;
- conservación;
- salud;
- restricciones médicas.

---

# Gobernanza de relaciones importadas

Las relaciones importadas deberán conservar:

- fuente;
- licencia;
- fecha;
- versión;
- método de transformación;
- identificador externo;
- confianza;
- estado de validación.

---

## Correspondencia externa

Cuando una relación externa se corresponda con una relación del SGCC deberá registrarse un mapeo.

Ejemplo:

```text
external:usesIngredient

↓

REL-0010 utiliza
```

El mapeo podrá ser:

```text
exacto

más amplio

más específico

aproximado

incompatible
```

---

# Gobernanza de conflictos

Los conflictos deberán registrarse y resolverse de forma explícita.

---

## Estados de conflicto

```text
Detectado

↓

En análisis

↓

Resuelto

o

Aceptado como divergencia

o

Archivado
```

---

## Criterios de resolución

Se evaluarán:

- contexto;
- fuente;
- autoridad;
- evidencia;
- vigencia;
- versión;
- confianza;
- validación humana;
- seguridad.

---

## Divergencias legítimas

No toda contradicción implica error.

Podrán coexistir relaciones distintas cuando correspondan a:

- tradiciones diferentes;
- regiones;
- periodos;
- fuentes;
- preferencias;
- contextos culinarios;
- criterios sensoriales.

Estas divergencias deberán contextualizarse.

---

# Gobernanza de cardinalidades

Las cardinalidades deberán definirse con prudencia.

Una restricción excesiva puede invalidar conocimiento legítimo.

Una restricción demasiado flexible puede reducir la calidad del modelo.

---

## Cambio de cardinalidad

Cambiar:

```text
0..*
```

a:

```text
1..1
```

será normalmente incompatible.

Cambiar:

```text
1..1
```

a:

```text
1..*
```

podrá ser compatible estructuralmente, pero deberá revisarse semánticamente.

---

# Gobernanza de dominio y rango

La ampliación de dominio o rango podrá ser compatible si preserva la semántica.

Ejemplo:

```text
utiliza
```

podría ampliar su dominio de:

```text
Receta
```

a:

```text
Receta
Base culinaria
Elaboración
```

si el significado continúa siendo válido.

La reducción de dominio o rango requerirá migración de las instancias afectadas.

---

# Gobernanza de propiedades lógicas

Declarar que una relación es:

- simétrica;
- transitiva;
- funcional;
- inversamente funcional;

puede generar nuevas inferencias y conflictos.

Cualquier modificación de estas propiedades deberá considerarse arquitectónicamente relevante.

---

# Validación normativa

La gobernanza deberá exigir validaciones antes de publicar cambios.

---

## Validación estructural

Deberá comprobar:

- identificador;
- nombre canónico;
- dominio;
- rango;
- dirección;
- cardinalidad;
- inversa;
- estado;
- versión;
- atributos obligatorios.

---

## Validación semántica

Deberá comprobar:

- significado;
- precisión;
- no duplicidad;
- coherencia con relaciones existentes;
- ejemplos;
- contraejemplos;
- selección correcta de familia;
- especialización adecuada.

---

## Validación ontológica

Deberá comprobar:

- coherencia de clases;
- subpropiedades;
- inversas;
- transitividad;
- simetría;
- restricciones;
- consistencia global;
- inferencias no deseadas.

---

## Validación de instancias

Deberá comprobar:

- sujeto;
- objeto;
- dominio;
- rango;
- contexto;
- cardinalidad;
- temporalidad;
- procedencia;
- estado;
- conflictos.

---

## Validación de migración

Deberá comprobar:

- cobertura de instancias;
- pérdida de información;
- ambigüedades;
- compatibilidad;
- reversibilidad;
- mantenimiento del historial.

---

# Validación automática

Las herramientas podrán detectar:

- identificadores duplicados;
- nombres canónicos duplicados;
- alias conflictivos;
- inversas incoherentes;
- dominio o rango inválidos;
- ciclos;
- cardinalidades incompatibles;
- reglas de inferencia rotas;
- relaciones obsoletas;
- instancias sin migrar;
- predicados desconocidos;
- documentación incompleta.

---

# Validación humana

La revisión humana será obligatoria cuando el cambio afecte a:

- significado;
- sustituciones;
- compatibilidades;
- maridajes;
- tradiciones culinarias;
- restricciones;
- seguridad;
- inferencia;
- ontología;
- migraciones ambiguas.

---

# Matriz de decisión para nuevas relaciones

| Pregunta | Sí | No |
|---|---|---|
| ¿Expresa un significado diferenciado? | continuar | no crear |
| ¿Existe una relación equivalente? | reutilizar | continuar |
| ¿Puede resolverse con un alias? | registrar alias | continuar |
| ¿Puede resolverse con una inversa? | utilizar inversa | continuar |
| ¿Puede modelarse como atributo? | usar atributo | continuar |
| ¿Puede inferirse de otras relaciones? | crear regla | continuar |
| ¿Tiene dominio y rango claros? | continuar | redefinir |
| ¿Tiene dirección inequívoca? | continuar | contextualizar |
| ¿Dispone de casos reales? | continuar | posponer |
| ¿Puede validarse? | continuar | no publicar |
| ¿Aporta valor al Knowledge Graph? | aceptar propuesta | descartar |

---

# Matriz de impacto de cambios

| Cambio | Compatibilidad probable | Acción |
|---|---|---|
| Añadir alias | Compatible | Parche o menor |
| Añadir traducción | Compatible | Parche |
| Añadir ejemplo | Compatible | Parche |
| Añadir atributo opcional | Compatible | Menor |
| Añadir atributo obligatorio | Potencialmente incompatible | Revisar y migrar |
| Ampliar dominio | Generalmente compatible | Menor |
| Reducir dominio | Incompatible | Mayor y migración |
| Ampliar rango | Generalmente compatible | Menor |
| Reducir rango | Incompatible | Mayor y migración |
| Cambiar dirección | Incompatible | Nueva relación o versión mayor |
| Cambiar inversa | Potencialmente incompatible | Revisión arquitectónica |
| Declarar transitividad | Alto impacto | ADR y validación |
| Eliminar relación | Incompatible | Deprecación y migración |
| Fusionar relaciones | Incompatible | Migración |
| Dividir relación | Incompatible | Migración y revisión |

---

# Responsabilidades

La gobernanza podrá implicar varios roles.

---

## Autor de la propuesta

Deberá:

- justificar la necesidad;
- analizar alternativas;
- definir la semántica;
- proponer dominio y rango;
- aportar ejemplos;
- evaluar impacto;
- actualizar documentación.

---

## Revisor semántico

Deberá evaluar:

- claridad;
- precisión;
- duplicidad;
- contexto;
- uso terminológico;
- ejemplos y contraejemplos.

---

## Responsable de dominio culinario

Deberá revisar:

- validez culinaria;
- aplicabilidad;
- contexto;
- excepciones;
- seguridad;
- coherencia con prácticas reales.

---

## Responsable de arquitectura

Deberá evaluar:

- impacto sobre el modelo;
- ontología;
- almacenamiento;
- APIs;
- Knowledge Graph;
- inferencia;
- interoperabilidad.

---

## Responsable de calidad

Deberá verificar:

- conformidad;
- validaciones;
- pruebas;
- trazabilidad;
- documentación;
- compatibilidad;
- migración.

---

## Responsable de datos o conocimiento

Deberá comprobar:

- integridad del grafo;
- procedencia;
- cobertura;
- duplicidades;
- conflictos;
- impacto sobre datos existentes.

---

# ADR obligatorios

Deberá crearse un ADR cuando una decisión afecte a:

- modelo general de relaciones;
- orientación canónica;
- estrategia de inversas;
- modelo de contextualización;
- entidades asociativas;
- inferencia;
- ontología;
- almacenamiento principal;
- interoperabilidad;
- compatibilidad;
- ciclo de vida;
- seguridad semántica.

---

# Registro de decisiones

Toda decisión relevante deberá reflejarse en:

- pull request;
- commit;
- BITÁCORA;
- historial de versiones;
- ADR cuando proceda;
- `DECISIONS_SUMMARY` cuando tenga alcance transversal.

---

# Flujo de contribución

El flujo recomendado será:

```text
Crear rama feature/...

↓

Modificar especificación o catálogo

↓

Actualizar esquemas y validadores

↓

Ejecutar validaciones

↓

Revisar impacto

↓

Crear Pull Request en español

↓

Revisión

↓

Merge

↓

Actualizar BITÁCORA y release
```

---

# Reglas para Pull Requests

Una modificación relacional deberá explicar:

- qué cambia;
- por qué;
- relaciones afectadas;
- compatibilidad;
- migración;
- validaciones ejecutadas;
- impacto sobre inferencias;
- documentación actualizada.

---

# Pruebas mínimas

Todo cambio relevante deberá incluir pruebas sobre:

- reconocimiento del predicado;
- dominio;
- rango;
- cardinalidad;
- inversa;
- restricciones;
- casos válidos;
- casos inválidos;
- migración;
- inferencias afectadas.

---

# Auditoría

La auditoría deberá conservar:

- quién creó la relación;
- quién la revisó;
- quién la aprobó;
- cuándo cambió;
- qué versión cambió;
- motivo;
- valores anteriores;
- valores nuevos;
- migraciones realizadas.

---

# Métricas de gobernanza

El SGCC podrá medir:

- relaciones canónicas activas;
- relaciones obsoletas;
- relaciones sin inversa documentada;
- relaciones genéricas;
- alias no resueltos;
- conflictos pendientes;
- migraciones incompletas;
- reglas de inferencia activas;
- relaciones sin procedencia;
- relaciones predichas pendientes de revisión;
- cobertura de validación.

---

# Indicadores de deuda relacional

Se considerarán señales de deuda:

- uso excesivo de `relacionado_con`;
- relaciones sin dominio;
- relaciones sin rango;
- relaciones sin ejemplos;
- duplicidades;
- inversas incoherentes;
- relaciones sin procedencia;
- contexto almacenado como texto libre;
- entidades asociativas no formalizadas;
- inferencias no documentadas;
- relaciones obsoletas aún utilizadas;
- conflictos sin resolver.

---

# Compatibilidad con el Knowledge Graph

Toda evolución deberá preservar, cuando sea posible:

- conectividad;
- interpretabilidad;
- consultas;
- rutas de explicación;
- inferencias;
- identificadores;
- procedencia.

Un cambio no deberá evaluarse únicamente por su corrección local.

Deberá analizarse su impacto sobre el grafo completo.

---

# Compatibilidad con RAG

Los cambios deberán considerar:

- recuperación semántica;
- expansión de consultas;
- ranking;
- enlaces entre componentes;
- explicabilidad;
- compatibilidad de embeddings;
- reconstrucción de índices.

La deprecación de relaciones podrá requerir regenerar índices o metadatos.

---

# Compatibilidad con agentes IA

Los agentes deberán consultar siempre el registro actualizado de relaciones.

No deberán inventar predicados fuera del vocabulario controlado salvo como propuesta explícita.

Las acciones automáticas deberán:

- usar relaciones canónicas;
- respetar dominio y rango;
- conservar contexto;
- registrar procedencia;
- diferenciar hechos, inferencias y predicciones.

---

# Compatibilidad con representaciones externas

El SGCC podrá mapear sus relaciones con vocabularios externos.

Ejemplos:

- RDF Schema;
- OWL;
- Schema.org;
- SKOS;
- vocabularios culinarios;
- modelos de recetas;
- catálogos de alimentos.

Los mapeos deberán indicar su precisión.

---

# Tipos de correspondencia externa

```text
Equivalencia exacta

Equivalencia aproximada

Relación más general

Relación más específica

Correspondencia contextual

Sin correspondencia
```

---

# Relación con otras especificaciones

Esta especificación deberá mantenerse coordinada con:

- `ESPECIFICACION_DE_DOCUMENTOS.md`;
- `ESPECIFICACION_DE_COMPONENTES.md`;
- `ESPECIFICACION_DE_COLECCIONES.md`;
- `ESPECIFICACION_DE_ONTOLOGIA.md`;
- `MODELO_DE_CONOCIMIENTO.md`;
- `GOVERNANCE_MODEL.md`;
- `QUALITY.md`;
- `KNOWLEDGE_STRATEGY.md`;
- `KNOWLEDGE_MATURITY.md`;
- `ARQUITECTURA.md`.

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
- `architecture/`

---

## Gobernanza

- `GOVERNANCE_MODEL.md`
- `QUALITY.md`
- `KNOWLEDGE_STRATEGY.md`
- `KNOWLEDGE_MATURITY.md`
- `BITACORA.md`
- `DECISIONS_SUMMARY.md`

---

## Especificaciones

- `ESPECIFICACION_DE_DOCUMENTOS.md`
- `ESPECIFICACION_DE_COMPONENTES.md`
- `ESPECIFICACION_DE_COLECCIONES.md`
- `ESPECIFICACION_DE_ONTOLOGIA.md`

---

## Decisiones arquitectónicas

- `governance/adr/`

---

# Conformidad de un tipo de relación

Un tipo de relación será conforme cuando:

- posea identificador persistente;
- tenga nombre canónico;
- disponga de definición;
- pertenezca a una familia;
- declare dominio;
- declare rango;
- defina dirección;
- declare cardinalidad;
- indique su inversa cuando proceda;
- documente características lógicas;
- incluya restricciones;
- disponga de ejemplos;
- haya sido aprobado.

---

# Conformidad de una instancia

Una instancia de relación será conforme cuando:

- utilice un tipo reconocido;
- conecte componentes existentes;
- respete dominio y rango;
- utilice la dirección canónica;
- cumpla cardinalidades;
- incluya contexto obligatorio;
- preserve procedencia;
- indique estado;
- no contradiga restricciones sin gestión explícita;
- supere las validaciones aplicables.

---

# Conformidad de una relación inferida

Una relación inferida será conforme cuando:

- proceda de una regla registrada;
- utilice premisas válidas;
- conserve las relaciones de origen;
- sea reproducible;
- indique el sistema y versión;
- respete contexto;
- incluya confianza cuando proceda;
- pueda invalidarse si cambian sus premisas;
- no se presente como hecho declarado.

---

# Conformidad de una relación predicha

Una relación predicha será conforme cuando:

- identifique modelo y versión;
- incluya confianza;
- registre entradas;
- tenga procedencia;
- esté marcada como predicción;
- no se publique como canónica sin revisión;
- respete las restricciones de seguridad.

---

# Conclusión

La presente especificación define el contrato relacional del SGCC.

Establece:

- qué es una relación;
- qué tipos existen;
- cómo se estructuran;
- cómo se contextualizan;
- cómo se representan;
- cómo se validan;
- cómo se infieren;
- cómo se versionan;
- cómo se deprecan;
- cómo se gobiernan.

Los componentes constituyen las unidades de conocimiento.

Las relaciones convierten esas unidades en una red semántica.

```text
Componentes aislados

↓

Relaciones explícitas

↓

Estructura semántica

↓

Knowledge Graph

↓

Razonamiento

↓

Sistemas inteligentes
```

La correcta gobernanza de las relaciones permitirá que NovaCoquinaria evolucione sin perder:

- coherencia;
- trazabilidad;
- interoperabilidad;
- calidad;
- explicabilidad;
- estabilidad.

La siguiente etapa deberá formalizar la ontología que integra:

- componentes;
- propiedades;
- relaciones;
- restricciones;
- jerarquías;
- axiomas;
- reglas de inferencia.

Este trabajo se desarrollará en:

```text
ESPECIFICACION_DE_ONTOLOGIA.md
```

La secuencia conceptual completa queda definida como:

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

RAG y agentes inteligentes
```

Con esta especificación, NovaCoquinaria dispone de una base formal para representar y gobernar las conexiones que estructuran el conocimiento culinario.
