---
id: DOC-0019
tipo: especificacion
titulo: Especificación del Modelo Documental
version: 3.0.0
estado: estable
ultima_revision: 2026-07-30
---

# ESPECIFICACIÓN DEL MODELO DOCUMENTAL

> **Proyecto:** NovaCoquinaria  
> **Release:** v1.4 – Knowledge Governance  
> **Sistema:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)  
> **Especificación:** v3.0.0

---

# Objetivo

Este documento define el **modelo documental oficial** del Sistema de Gestión del Conocimiento Culinario (SGCC).

Su finalidad es establecer las normas que regulan cómo se representan, identifican, estructuran, relacionan y evolucionan los documentos que forman parte del conocimiento gestionado por el sistema.

Esta especificación constituye el contrato normativo que deberán respetar:

- los colaboradores del proyecto;
- las herramientas de automatización;
- las aplicaciones consumidoras del conocimiento;
- los asistentes basados en inteligencia artificial;
- cualquier sistema que interactúe con el SGCC.

Todo documento integrado en NovaCoquinaria deberá ser compatible con esta especificación.

---

# Alcance

Esta especificación define:

- el modelo documental del SGCC;
- los principios que gobiernan la documentación;
- la taxonomía documental;
- el modelo de metadatos;
- las reglas de identificación;
- la estructura general de los documentos;
- las relaciones entre documentos;
- el ciclo de vida documental;
- los criterios de validación;
- las condiciones de conformidad.

No forma parte del alcance de este documento:

- las normas editoriales;
- los criterios de redacción;
- el contenido culinario;
- las decisiones arquitectónicas particulares.

Estos aspectos se documentan en sus respectivas especificaciones o documentos de referencia.

---

# Definiciones

Esta sección establece el vocabulario oficial utilizado por el Sistema de Gestión del Conocimiento Culinario (SGCC).

Las definiciones aquí descritas constituyen la referencia para el resto de especificaciones del proyecto.

---

## Activo de conocimiento

Entidad capaz de representar conocimiento reutilizable dentro del SGCC.

Un activo de conocimiento puede materializarse mediante uno o varios documentos y mantiene su identidad independientemente de su representación física.

Ejemplos de activos de conocimiento:

- una receta;
- un ingrediente;
- una técnica culinaria;
- una plantilla;
- una tabla de referencia;
- una decisión arquitectónica.

---

## Documento

Unidad mínima de conocimiento persistente gestionada por el SGCC.

Cada documento representa un único activo de conocimiento o una parte claramente delimitada de este.

Todo documento posee:

- una responsabilidad definida;
- un identificador permanente;
- un conjunto de metadatos canónicos;
- contenido estructurado;
- relaciones explícitas con otros documentos cuando resulte necesario.

---

## Tipo documental

Clasificación funcional que determina el propósito de un documento dentro del sistema.

El tipo documental define:

- su responsabilidad;
- su estructura recomendada;
- sus relaciones habituales;
- su papel dentro del modelo de conocimiento.

---

## Front Matter

Bloque YAML situado al comienzo del documento que contiene los metadatos oficiales utilizados por las herramientas del proyecto.

El Front Matter constituye la fuente canónica de información estructural del documento.

---

## Identificador

Clave única, permanente e inmutable que identifica un documento.

El identificador permanece estable durante toda la vida del documento, independientemente de:

- su nombre;
- su ubicación;
- la organización física del repositorio;
- la evolución de la arquitectura del proyecto.

---

## Relación documental

Vínculo explícito entre dos o más activos de conocimiento.

Las relaciones forman parte del modelo lógico del SGCC y no dependen de la organización física de los archivos.

---

## Repositorio

Representación física del conjunto de documentos que implementan el modelo de conocimiento.

El repositorio constituye únicamente un mecanismo de almacenamiento y organización.

No define el conocimiento.

---

## Modelo documental

Conjunto de normas que describen cómo deben estructurarse, identificarse y relacionarse los documentos del SGCC.

El modelo documental garantiza la coherencia del conocimiento y permite su evolución sostenible.

---

# Principios del modelo documental

Todo documento integrado en el SGCC deberá respetar los principios descritos en esta sección.

Estos principios constituyen las reglas fundamentales que gobiernan la evolución del conocimiento del proyecto.

---

## Responsabilidad única

Cada documento responderá a una única necesidad principal.

Un documento no deberá asumir responsabilidades pertenecientes a otros tipos documentales.

Esta separación favorece la claridad, la reutilización y la mantenibilidad del conocimiento.

---

## Reutilización

El conocimiento deberá escribirse una única vez.

Cuando un concepto ya exista en otro documento, este deberá reutilizarse mediante referencias explícitas en lugar de duplicar información.

---

## Independencia

Cada documento deberá poder evolucionar de forma autónoma.

La modificación de un documento no deberá requerir cambios innecesarios en otros documentos salvo cuando exista una dependencia explícita.

---

## Persistencia

La identidad de un documento deberá mantenerse durante todo su ciclo de vida.

Los cambios de ubicación, nombre o estructura del repositorio nunca justificarán la modificación de su identificador.

---

## Trazabilidad

Todo documento deberá poder identificarse de forma inequívoca.

Su evolución deberá poder reconstruirse mediante:

- su identificador;
- su historial;
- sus relaciones;
- su versionado.

---

## Conectividad

Los documentos podrán establecer relaciones explícitas con otros activos del conocimiento.

Estas relaciones deberán facilitar la navegación, la reutilización y la comprensión del sistema.

---

## Automatización

Toda la información estructural necesaria para interpretar un documento deberá poder procesarse automáticamente.

Este principio permite el desarrollo de:

- herramientas de validación;
- sistemas de publicación;
- asistentes inteligentes;
- motores de búsqueda;
- grafos de conocimiento;
- procesos automáticos de mantenimiento.

---

## Evolución sostenible

El modelo documental deberá favorecer la incorporación continua de nuevo conocimiento sin comprometer la coherencia del sistema.

Toda evolución deberá preservar, siempre que resulte posible:

- la compatibilidad;
- la reutilización;
- la estabilidad de los identificadores;
- la calidad del conocimiento existente.

---

# Taxonomía documental

El SGCC organiza sus documentos mediante una taxonomía funcional.

Cada familia documental responde a una responsabilidad claramente diferenciada y ocupa un papel específico dentro de la arquitectura del conocimiento.

La clasificación documental no depende de la organización física del repositorio.

---

## Documentación estratégica

Define la identidad del proyecto y establece su propósito, visión y principios fundamentales.

Incluye documentos como:

- VISION
- MANIFESTO
- NovaCoquinaria

Su finalidad consiste en responder a la pregunta:

> ¿Por qué existe el proyecto?

---

## Arquitectura

Describe el diseño conceptual y estructural del SGCC.

Incluye documentos como:

- ARQUITECTURA
- MODELO_DE_CONOCIMIENTO
- AUTOMATION
- TOOLS_FRAMEWORK

Su finalidad consiste en responder a la pregunta:

> ¿Cómo está diseñado el sistema?

---

## Gobernanza

Define las normas que regulan la evolución del conocimiento y la toma de decisiones arquitectónicas.

Incluye:

- Architecture Decision Records (ADR);
- QUALITY;
- KNOWLEDGE_DEBT;
- KNOWLEDGE_MATURITY;
- KNOWLEDGE_STRATEGY;
- GOBERNANCE_MODEL.

Su finalidad consiste en responder a la pregunta:

> ¿Cómo evoluciona el sistema?

---

## Gestión

Documenta el estado operativo del proyecto y su planificación.

Incluye:

- ROADMAP;
- PROJECT_STATUS;
- BITÁCORA;
- DEVELOPMENT_WORKFLOW;
- PROJECT_ONBOARDING.

Su finalidad consiste en responder a la pregunta:

> ¿Cuál es la situación actual del proyecto y cómo debe gestionarse?

---

## Especificaciones

Definen contratos técnicos y modelos formales utilizados por el SGCC.

Incluyen documentos como:

- ESPECIFICACION_DE_DOCUMENTOS;
- ESPECIFICACION_DE_COLECCIONES;
- futuras especificaciones del modelo de conocimiento.

Estas especificaciones poseen carácter normativo y constituyen la referencia oficial para el diseño y validación del sistema.

---

## Conocimiento culinario

Representa el dominio funcional gestionado por NovaCoquinaria.

Incluye:

- bases culinarias;
- técnicas;
- ingredientes;
- recetas;
- plantillas;
- tablas;
- cualquier otro activo culinario reutilizable.

Su finalidad consiste en representar el conocimiento culinario del sistema de forma estructurada y reutilizable.

---

## Recursos auxiliares

Incluyen aquellos documentos que apoyan el funcionamiento del proyecto sin formar parte del conocimiento principal.

Ejemplos:

- plantillas de documentación;
- recursos gráficos;
- documentación generada automáticamente;
- materiales de apoyo.

Estos documentos facilitan el mantenimiento y evolución del proyecto, pero no constituyen activos de conocimiento del dominio culinario.

---

# Modelo documental

El modelo documental define la estructura conceptual común a todos los documentos gestionados por el SGCC.

Cada documento representa una manifestación persistente de un activo de conocimiento y combina información estructural, contenido y relaciones.

```text
Activo de conocimiento
        │
        ▼
Documento
        │
        ├── Metadatos
        ├── Contenido
        └── Relaciones
                │
                ▼
        Knowledge Graph
```

El modelo documental es independiente del formato físico utilizado para almacenar o publicar el conocimiento.

En la implementación actual, los documentos se representan principalmente mediante archivos Markdown con Front Matter YAML.

Esta representación podrá evolucionar en el futuro sin alterar la identidad ni el significado lógico de los activos de conocimiento.

---

## Componentes de un documento

Todo documento del SGCC se compone, conceptualmente, de los siguientes elementos:

- identidad;
- tipo documental;
- metadatos;
- contenido;
- relaciones;
- estado;
- versión.

Estos componentes podrán expresarse de forma explícita o derivarse mediante las herramientas del sistema.

---

## Identidad

La identidad permite reconocer un documento de forma inequívoca durante todo su ciclo de vida.

Se materializa mediante un identificador permanente y no depende de:

- la ruta del archivo;
- el nombre del documento;
- su posición dentro del repositorio;
- el sistema utilizado para publicarlo.

---

## Metadatos

Los metadatos describen las propiedades estructurales del documento.

Permiten:

- identificarlo;
- clasificarlo;
- conocer su versión;
- determinar su estado;
- automatizar su validación;
- integrarlo en sistemas externos.

Los metadatos canónicos se expresan mediante Front Matter YAML.

---

## Contenido

El contenido representa el conocimiento desarrollado por el documento.

Deberá ajustarse a:

- la responsabilidad del tipo documental;
- la Guía de Estilo;
- las especificaciones aplicables;
- los principios del modelo de conocimiento.

El contenido no deberá duplicar conocimiento que ya exista en otro documento cuando pueda reutilizarse mediante una relación explícita.

---

## Relaciones

Las relaciones conectan el documento con otros activos de conocimiento.

Permiten representar dependencias, reutilización, complementariedad, evolución o sustitución.

Las relaciones forman parte del modelo lógico del SGCC y podrán utilizarse para construir el Knowledge Graph.

---

# Modelo de metadatos

Todo documento sujeto a esta especificación deberá comenzar con un bloque Front Matter YAML válido.

El Front Matter constituye la fuente canónica de información estructural del documento.

Deberá situarse al comienzo del archivo, sin contenido previo, y estar delimitado mediante tres guiones.

Ejemplo:

```yaml
---
id: DOC-0019
tipo: especificacion
titulo: Especificación del Modelo Documental
version: 3.0.0
estado: estable
ultima_revision: 2026-07-30
---
```

---

## Campos obligatorios

| Campo | Tipo | Formato | Descripción |
|---|---|---|---|
| `id` | cadena | `PREFIJO-NNNN` | Identificador permanente y único |
| `tipo` | cadena controlada | minúsculas | Tipo funcional del documento |
| `titulo` | cadena | texto no vacío | Título oficial del documento |
| `version` | cadena | SemVer | Versión documental |
| `ultima_revision` | fecha | `AAAA-MM-DD` | Fecha de la última revisión significativa |

Todos los campos obligatorios deberán contener un valor válido.

No se permiten campos obligatorios vacíos.

---

## Campo `id`

Identifica permanentemente el documento.

Ejemplo:

```yaml
id: REC-0017
```

Reglas:

- deberá ser único en el conjunto documental canónico;
- no podrá estar vacío;
- deberá respetar el prefijo asignado a su familia documental;
- no podrá reutilizarse tras la retirada de un documento;
- no cambiará por movimientos o renombrados.

---

## Campo `tipo`

Declara la clasificación funcional del documento.

Ejemplo:

```yaml
tipo: especificacion
```

El valor deberá pertenecer al vocabulario controlado del SGCC.

Valores habituales:

```text
arquitectura
base
especificacion
gestion
gobernanza
ingrediente
nota
plantilla
receta
tabla
tecnica
```

La ampliación del vocabulario deberá documentarse y mantener compatibilidad con las herramientas existentes.

---

## Campo `titulo`

Contiene el nombre oficial y legible del documento.

Ejemplo:

```yaml
titulo: Especificación del Modelo Documental
```

El título deberá:

- describir con claridad la responsabilidad del documento;
- coincidir conceptualmente con el encabezado principal;
- evitar abreviaturas ambiguas;
- mantenerse estable siempre que no cambie la identidad conceptual del documento.

---

## Campo `version`

Representa la versión independiente del documento.

Ejemplo:

```yaml
version: 3.0.0
```

El versionado documental deberá seguir el esquema SemVer:

```text
MAYOR.MENOR.PARCHE
```

Donde:

- `MAYOR` indica cambios incompatibles o una redefinición sustancial del contrato;
- `MENOR` indica ampliaciones compatibles;
- `PARCHE` indica correcciones menores sin impacto semántico significativo.

La versión documental es independiente de la release general de NovaCoquinaria.

---

## Campo `ultima_revision`

Indica la fecha de la última modificación significativa del documento.

Ejemplo:

```yaml
ultima_revision: 2026-07-30
```

Deberá utilizar el formato ISO 8601:

```text
AAAA-MM-DD
```

No será necesario modificarla por cambios puramente mecánicos que no alteren el contenido ni la estructura del documento.

---

## Campos opcionales

| Campo | Tipo | Finalidad |
|---|---|---|
| `estado` | cadena controlada | Indicar el estado del ciclo de vida |
| `autor` | cadena o lista | Registrar la autoría o responsabilidad principal |
| `etiquetas` | lista | Facilitar clasificación, búsqueda y análisis |
| `dominio` | cadena o lista | Identificar el dominio funcional |
| `release` | cadena | Asociar el documento a una release del proyecto |
| `sustituye_a` | identificador o lista | Declarar sustitución documental |
| `relacionados` | lista de identificadores | Declarar relaciones explícitas |
| `deprecado_desde` | versión o fecha | Registrar el inicio de la obsolescencia |

Los campos opcionales no deberán utilizarse para duplicar información que pueda derivarse automáticamente.

---

## Campo `estado`

Declara el estado documental.

Ejemplo:

```yaml
estado: estable
```

Los valores recomendados son:

```text
borrador
en_revision
estable
obsoleto
archivado
```

Las herramientas deberán interpretar estos valores de forma homogénea.

---

## Extensibilidad

Podrán incorporarse nuevos campos cuando exista una necesidad real y documentada.

Toda ampliación deberá:

- utilizar nombres claros;
- evitar duplicidades semánticas;
- preservar la compatibilidad hacia atrás;
- actualizar las herramientas afectadas;
- documentarse en esta especificación o en una especificación especializada.

---

# Identificadores documentales

Cada documento canónico del SGCC deberá disponer de un identificador permanente.

El identificador constituye la referencia principal del activo de conocimiento.

---

## Formato

El formato general será:

```text
PREFIJO-NNNN
```

Donde:

- `PREFIJO` representa la familia documental;
- `NNNN` representa una secuencia numérica de cuatro dígitos.

Ejemplos:

```text
ADR-0019
ARC-0018
DOC-0019
ING-0023
PLA-0008
REC-0022
TAB-0006
```

---

## Prefijos

Los prefijos deberán asignarse según la naturaleza documental, no según la carpeta donde se encuentre el archivo.

Prefijos actuales:

| Prefijo | Familia |
|---|---|
| `ADR` | Decisiones arquitectónicas |
| `ARC` | Arquitectura |
| `BAS` | Bases y técnicas fundamentales |
| `DOC` | Documentación transversal |
| `GOV` | Gobernanza |
| `ING` | Ingredientes |
| `MGT` | Gestión |
| `PLA` | Plantillas culinarias |
| `REC` | Recetas |
| `TAB` | Tablas de referencia |

La incorporación de nuevos prefijos deberá estar justificada y documentada.

---

## Unicidad

No podrán existir dos documentos canónicos con el mismo identificador.

Las copias generadas para publicación podrán conservar el identificador original, siempre que:

- no se consideren fuente canónica;
- estén excluidas de la validación de unicidad;
- puedan rastrearse hasta el documento fuente.

---

## Inmutabilidad

El identificador no cambiará como consecuencia de:

- mover el documento;
- renombrar el archivo;
- cambiar su carpeta;
- reorganizar el repositorio;
- modificar su estado;
- publicar el contenido en otro formato.

Solo podrá asignarse un identificador diferente cuando se cree un activo de conocimiento nuevo y conceptualmente distinto.

---

## No reutilización

Un identificador retirado no podrá asignarse a otro documento.

Cuando un documento quede obsoleto o archivado, su identificador continuará reservado.

Esta regla preserva la trazabilidad histórica y evita ambigüedades en relaciones antiguas.

---

## Asignación

La asignación deberá seguir el procedimiento oficial del proyecto.

Como mínimo deberá comprobarse:

- que el prefijo sea adecuado;
- que el número no esté utilizado;
- que no exista ya un documento equivalente;
- que el nuevo documento represente una responsabilidad independiente.

La creación automática de identificadores podrá incorporarse mediante herramientas específicas.

---

# Estructura documental

Cada documento deberá presentar una estructura coherente con su tipo y responsabilidad.

La estructura concreta podrá variar, pero deberá respetar un contrato mínimo común.

---

## Estructura mínima

Todo documento deberá contener:

1. Front Matter válido;
2. un encabezado principal;
3. una definición clara de su objetivo o responsabilidad;
4. contenido organizado mediante secciones;
5. referencias cuando existan dependencias relevantes.

Ejemplo conceptual:

```markdown
---
metadatos
---

# Título

# Objetivo

# Contenido principal

# Referencias
```

---

## Encabezado principal

Todo documento deberá contener un único encabezado de nivel 1.

```markdown
# Título del documento
```

El encabezado deberá ser coherente con el campo `titulo` del Front Matter.

---

## Jerarquía de secciones

Las secciones deberán utilizar una jerarquía coherente.

Ejemplo:

```markdown
# Documento

## Sección

### Subsección

#### Detalle
```

No deberán omitirse niveles sin una razón justificada.

---

## Secciones normativas y recomendadas

Las especificaciones podrán definir:

- secciones obligatorias;
- secciones recomendadas;
- secciones opcionales.

La ausencia de una sección obligatoria constituirá una no conformidad.

Las secciones recomendadas podrán omitirse cuando no resulten aplicables.

---

## Referencias

Cuando un documento dependa conceptualmente de otro, deberá enlazarlo o referenciarlo de manera explícita.

Siempre que sea posible, las relaciones lógicas deberán expresarse mediante identificadores persistentes, además de los enlaces físicos necesarios para la navegación.

Ejemplo:

```markdown
Esta especificación amplía el modelo definido en `ARC-0018`.
```

---

## Contenido generado

El contenido generado automáticamente deberá identificarse como tal.

No deberá editarse manualmente salvo que la herramienta responsable lo permita expresamente.

Las fuentes canónicas deberán permanecer separadas de las representaciones generadas.

---

## Documentos índice

Los documentos índice, como determinados `README.md`, podrán utilizar una estructura simplificada.

Su finalidad será:

- describir una colección física;
- facilitar navegación;
- enlazar documentos;
- proporcionar contexto local.

Cuando formen parte del corpus canónico, deberán cumplir los requisitos de metadatos establecidos por el proyecto.

---

# Ciclo de vida documental

Todo documento evoluciona mediante un ciclo de vida controlado.

```text
Borrador
    │
    ▼
En revisión
    │
    ▼
Estable
    │
    ├───────────────┐
    ▼               ▼
Obsoleto        Nueva versión
    │
    ▼
Archivado
```

---

## Borrador

Estado inicial de un documento en construcción.

Características:

- contenido incompleto o provisional;
- estructura todavía sujeta a cambios;
- no debe considerarse referencia normativa;
- puede requerir validaciones parciales.

Front Matter:

```yaml
estado: borrador
```

---

## En revisión

El documento dispone de contenido suficiente para ser evaluado.

Características:

- está pendiente de validación técnica o editorial;
- puede recibir cambios relevantes;
- no debe utilizarse aún como referencia definitiva.

Front Matter:

```yaml
estado: en_revision
```

---

## Estable

El documento ha sido validado y se considera referencia vigente.

Características:

- cumple las especificaciones aplicables;
- supera las validaciones oficiales;
- puede utilizarse como fuente normativa o de conocimiento;
- cualquier cambio significativo deberá reflejarse en su versión.

Front Matter:

```yaml
estado: estable
```

---

## Obsoleto

El documento ya no representa la referencia preferente, pero se conserva por razones de trazabilidad.

Características:

- puede haber sido sustituido;
- no debe utilizarse para nuevas implementaciones;
- deberá indicar, cuando sea posible, el documento sucesor;
- conserva su identificador.

Front Matter:

```yaml
estado: obsoleto
sustituido_por: DOC-XXXX
```

---

## Archivado

El documento deja de formar parte del conocimiento operativo.

Características:

- se conserva únicamente como registro histórico;
- no deberá recibir evolución funcional;
- mantiene su identificador y su trazabilidad;
- podrá excluirse de determinadas publicaciones.

Front Matter:

```yaml
estado: archivado
```

---

## Transiciones

Las transiciones deberán producirse de forma explícita.

Transiciones habituales:

```text
borrador → en_revision
en_revision → estable
estable → obsoleto
obsoleto → archivado
```

Un documento podrá volver de `en_revision` a `borrador` si requiere una reformulación sustancial.

Un documento estable podrá recibir una nueva versión sin abandonar dicho estado cuando el cambio mantenga su vigencia.

---

## Sustitución

La sustitución se produce cuando un documento deja de ser la referencia principal y otro asume su responsabilidad.

La sustitución deberá:

- conservar ambos identificadores;
- declarar la relación entre los documentos;
- evitar eliminar el documento sustituido sin trazabilidad;
- actualizar las referencias cuando corresponda.

---

# Relaciones documentales

Las relaciones documentales representan vínculos semánticos entre activos de conocimiento.

No deben confundirse con la proximidad física entre archivos.

---

## Relaciones lógicas

Las relaciones lógicas describen el significado del vínculo.

Ejemplos:

- depende de;
- amplía;
- implementa;
- reutiliza;
- sustituye;
- complementa;
- contradice;
- deriva de;
- relacionado con.

Ejemplo conceptual:

```text
REC-0017
    reutiliza
PLA-0002
```

Estas relaciones podrán representarse en el Knowledge Graph.

---

## Relaciones físicas

Las relaciones físicas permiten navegar entre archivos concretos.

Ejemplo:

```markdown
[Consultar la plantilla](../../../12_Plantillas/04_Cocciones/curry_base.md)
```

Una ruta física puede cambiar como consecuencia de una reorganización del repositorio.

La relación lógica deberá permanecer estable aunque cambie el enlace físico.

---

## Dirección

Las relaciones podrán ser:

- unidireccionales;
- bidireccionales;
- simétricas;
- asimétricas.

Ejemplos:

```text
A sustituye a B
```

es una relación dirigida.

```text
A está relacionado con B
```

puede considerarse simétrica.

La semántica concreta deberá definirse en la futura especificación de relaciones.

---

## Cardinalidad

Una relación podrá conectar:

- un documento con otro;
- un documento con varios;
- varios documentos con un dominio;
- una colección con múltiples activos.

Ejemplo:

```text
PLA-0001
    es reutilizada por
REC-0001
REC-0004
REC-0018
```

---

## Integridad

Toda relación explícita deberá apuntar a un activo existente o declarar claramente que se trata de una referencia externa.

Las herramientas deberán detectar, siempre que sea posible:

- enlaces rotos;
- identificadores inexistentes;
- referencias circulares problemáticas;
- relaciones incompatibles;
- documentos huérfanos.

---

## No duplicación

Las relaciones deberán utilizarse para reutilizar conocimiento, no para justificar duplicaciones.

Cuando un documento necesite información ya desarrollada en otro, deberá:

1. referenciar el activo existente;
2. resumir únicamente el contexto imprescindible;
3. evitar reproducir secciones completas sin necesidad.

---

## Evolución de las relaciones

Las relaciones deberán mantenerse actualizadas durante el ciclo de vida documental.

Cuando un documento sea sustituido, movido, dividido o consolidado, deberán revisarse:

- sus enlaces entrantes;
- sus enlaces salientes;
- sus relaciones por identificador;
- su representación en el Knowledge Graph.

---

# Reglas de validación

Las reglas de validación determinan si un documento puede considerarse válido dentro del SGCC.

La validación combina controles estructurales, semánticos y relacionales.

Su objetivo no consiste únicamente en detectar errores técnicos, sino en preservar:

- la coherencia documental;
- la integridad del conocimiento;
- la trazabilidad;
- la interoperabilidad;
- la mantenibilidad del sistema.

---

## Niveles de validación

La validación documental se organiza en varios niveles complementarios.

### Validación sintáctica

Comprueba que el documento pueda interpretarse correctamente.

Incluye:

- sintaxis Markdown válida;
- Front Matter YAML correctamente delimitado;
- metadatos legibles;
- fechas y versiones con formato válido.

---

### Validación estructural

Comprueba que el documento contenga los elementos requeridos por su tipo.

Incluye:

- Front Matter obligatorio;
- encabezado principal;
- secciones mínimas;
- campos obligatorios;
- jerarquía coherente de encabezados.

---

### Validación de identidad

Comprueba la integridad de los identificadores.

Incluye:

- existencia del identificador;
- formato correcto;
- unicidad;
- correspondencia del prefijo con la familia documental;
- ausencia de reutilización de identificadores retirados.

---

### Validación relacional

Comprueba la integridad de las relaciones y referencias.

Incluye:

- enlaces internos válidos;
- identificadores referenciados existentes;
- relaciones de sustitución consistentes;
- referencias externas correctamente diferenciadas;
- ausencia de documentos huérfanos cuando su tipo requiera relaciones.

---

### Validación semántica

Comprueba que el documento cumpla su responsabilidad conceptual.

Incluye:

- coherencia entre `tipo`, título y contenido;
- ausencia de duplicaciones innecesarias;
- uso correcto del vocabulario;
- correspondencia con el modelo de conocimiento;
- respeto de los límites del tipo documental.

La validación semántica podrá requerir revisión humana o asistencia basada en inteligencia artificial.

---

## Requisitos mínimos de validez

Un documento se considera válido cuando:

- dispone de Front Matter válido cuando resulte obligatorio;
- contiene todos los campos requeridos;
- posee un identificador único y correctamente formado;
- utiliza un título coherente;
- declara una versión válida;
- informa de una fecha de revisión válida;
- mantiene una estructura compatible con su tipo;
- no contiene enlaces internos rotos;
- respeta las especificaciones aplicables;
- supera las herramientas oficiales de validación.

---

## Severidad de los resultados

Las herramientas podrán clasificar sus resultados según su impacto.

### Error

Incumplimiento que impide considerar válido el documento.

Ejemplos:

- identificador duplicado;
- Front Matter inválido;
- campo obligatorio ausente;
- enlace interno roto;
- formato de identificador incorrecto.

---

### Advertencia

Situación que no invalida necesariamente el documento, pero requiere revisión.

Ejemplos:

- sección recomendada ausente;
- documento sin relaciones;
- versión potencialmente desactualizada;
- terminología inconsistente;
- posible duplicación de contenido.

---

### Información

Observación que facilita el mantenimiento sin representar una no conformidad.

Ejemplos:

- sugerencia de mejora;
- relación adicional posible;
- campo opcional no utilizado;
- oportunidad de automatización.

---

## Herramientas oficiales

Las herramientas de validación constituyen la implementación automatizada de esta especificación.

La validación integral deberá poder ejecutarse mediante:

```powershell
python tools/validate_all.py
```

El pipeline podrá incluir, entre otras, las siguientes comprobaciones:

- Front Matter;
- identificadores únicos;
- enlaces internos;
- estructura documental;
- relaciones;
- documentos huérfanos;
- coherencia semántica;
- generación del Knowledge Graph.

La ausencia temporal de una comprobación automatizada no elimina la obligatoriedad de la norma correspondiente.

---

## Fuente normativa y código de validación

Esta especificación constituye la fuente normativa del modelo documental.

Las herramientas implementan sus reglas, pero no las sustituyen.

Cuando exista una discrepancia entre la especificación y el comportamiento de una herramienta, deberá determinarse si:

- la herramienta contiene un defecto;
- la especificación necesita actualizarse;
- existe una excepción documental no formalizada.

La discrepancia deberá resolverse explícitamente y no mediante excepciones silenciosas.

---

## Validación antes de integración

Antes de integrar cambios en la rama principal deberán ejecutarse las validaciones oficiales aplicables.

Una contribución documental no deberá integrarse cuando existan errores conocidos sin justificar.

Las excepciones, si resultan imprescindibles, deberán:

- documentarse;
- indicar su alcance;
- asignarse como deuda de conocimiento o incidencia;
- resolverse en una iteración posterior.

---

# Conformidad

La conformidad expresa el grado en que un documento cumple esta especificación.

---

## Documento conforme

Un documento se considera conforme cuando:

- respeta el modelo documental;
- incorpora los metadatos obligatorios;
- mantiene una identidad válida;
- cumple la estructura definida para su tipo;
- respeta el ciclo de vida;
- mantiene relaciones íntegras;
- supera las validaciones oficiales;
- conserva coherencia con el modelo de conocimiento.

---

## Documento parcialmente conforme

Un documento podrá considerarse parcialmente conforme cuando:

- pertenece a una fase de migración;
- conserva una estructura histórica;
- no puede adaptarse inmediatamente sin riesgo;
- existe una excepción documentada.

La conformidad parcial deberá ser temporal.

Toda desviación deberá registrar:

- norma incumplida;
- motivo;
- impacto;
- plan de regularización.

---

## Documento no conforme

Un documento será no conforme cuando incumpla requisitos obligatorios y no exista una excepción aprobada.

Un documento no conforme:

- no deberá utilizarse como referencia normativa;
- no deberá publicarse como contenido estable;
- no deberá incorporarse a procesos automáticos que dependan de su validez;
- deberá corregirse o clasificarse adecuadamente.

---

## Conformidad de representaciones generadas

Las representaciones derivadas, como `site_docs`, no necesitan cumplir necesariamente todos los requisitos de la fuente canónica si:

- se generan automáticamente;
- pueden rastrearse hasta su fuente;
- no se consideran editables;
- no participan en la validación de unicidad;
- preservan el significado del contenido original.

---

# Compatibilidad

El modelo documental deberá facilitar la interoperabilidad del SGCC con herramientas presentes y futuras.

---

## Compatibilidad hacia atrás

Las modificaciones del modelo deberán preservar, siempre que sea posible, la interpretación de documentos existentes.

Los cambios incompatibles requerirán:

- incremento de versión mayor;
- estrategia de migración;
- actualización de validadores;
- documentación del impacto;
- registro de la decisión arquitectónica cuando corresponda.

---

## Compatibilidad entre representaciones

Un activo de conocimiento podrá representarse mediante distintos formatos.

Ejemplos:

- Markdown;
- HTML;
- JSON;
- YAML;
- RDF;
- base de datos;
- API;
- representación vectorial;
- contexto para RAG.

La transformación entre representaciones deberá preservar:

- identidad;
- significado;
- relaciones;
- trazabilidad;
- metadatos esenciales.

---

## Compatibilidad con publicación

El modelo deberá permitir generar sitios web y otros canales de publicación sin modificar las fuentes canónicas.

Las representaciones publicadas podrán:

- cambiar la navegación;
- adaptar el formato visual;
- generar índices;
- incorporar búsquedas;
- resolver enlaces;
- ocultar metadatos internos.

No podrán alterar el significado del conocimiento.

---

## Compatibilidad con Knowledge Graph

Los identificadores, metadatos y relaciones deberán poder transformarse en nodos y aristas de un Knowledge Graph.

Cada documento podrá representarse como un nodo identificado de forma persistente.

Las relaciones documentales podrán convertirse en aristas semánticas.

---

## Compatibilidad con sistemas de inteligencia artificial

La estructura documental deberá facilitar:

- recuperación semántica;
- segmentación;
- generación de embeddings;
- sistemas RAG;
- asistentes especializados;
- agentes de mantenimiento;
- validación semántica asistida;
- generación de conocimiento derivado.

Los sistemas de inteligencia artificial deberán respetar la distinción entre:

- conocimiento canónico;
- inferencias;
- contenido generado;
- propuestas pendientes de validación.

---

## Compatibilidad con APIs

Los documentos podrán exponerse mediante APIs documentales.

La API deberá preservar, como mínimo:

- identificador;
- tipo;
- título;
- versión;
- estado;
- contenido;
- relaciones relevantes.

La ruta de acceso de la API no deberá utilizarse como sustituto del identificador persistente.

---

# Evolución de la especificación

Esta especificación podrá evolucionar conforme maduren las necesidades del SGCC.

Toda evolución deberá preservar la coherencia del modelo documental y mantener una trazabilidad clara.

---

## Tipos de cambio

### Cambio de parche

Incluye:

- correcciones tipográficas;
- aclaraciones;
- mejoras de redacción;
- ejemplos adicionales;
- correcciones sin impacto normativo.

Ejemplo:

```text
3.0.0 → 3.0.1
```

---

### Cambio menor

Incluye:

- nuevos campos opcionales;
- ampliaciones compatibles;
- nuevas recomendaciones;
- incorporación de tipos documentales compatibles;
- nuevas reglas que no invaliden documentos existentes.

Ejemplo:

```text
3.0.0 → 3.1.0
```

---

### Cambio mayor

Incluye:

- modificación de campos obligatorios;
- redefinición de identificadores;
- cambios incompatibles en estados o tipos;
- alteración sustancial del contrato documental;
- invalidación de documentos previamente conformes.

Ejemplo:

```text
3.0.0 → 4.0.0
```

---

## Procedimiento de evolución

Todo cambio relevante deberá:

1. identificar la necesidad;
2. evaluar su impacto;
3. revisar la compatibilidad;
4. actualizar la especificación;
5. adaptar las herramientas;
6. migrar los documentos afectados;
7. ejecutar las validaciones;
8. registrar el cambio.

Cuando el cambio afecte a principios arquitectónicos, deberá evaluarse mediante una ADR.

---

## Migraciones

Las migraciones documentales deberán diseñarse para ser:

- reproducibles;
- verificables;
- reversibles cuando resulte posible;
- trazables;
- automatizables.

Una migración no deberá modificar identificadores persistentes salvo que se esté creando un activo nuevo.

---

## Deprecación de reglas

Una regla podrá declararse obsoleta antes de eliminarse.

La deprecación deberá indicar:

- regla afectada;
- versión desde la que queda obsoleta;
- alternativa recomendada;
- fecha o versión prevista para su retirada.

---

# Gobernanza del modelo documental

El modelo documental forma parte de la gobernanza del conocimiento del SGCC.

Su mantenimiento deberá coordinarse con:

- el modelo de conocimiento;
- la arquitectura;
- las herramientas;
- el sistema de calidad;
- la estrategia de conocimiento;
- el ciclo de releases.

---

## Autoridad normativa

Esta especificación define el contrato general de los documentos.

Las especificaciones especializadas podrán ampliar sus reglas, pero no contradecirlas sin:

- declarar explícitamente la excepción;
- justificarla;
- registrar su alcance;
- aprobar la decisión correspondiente.

---

## Jerarquía de aplicación

Las normas se aplicarán siguiendo este orden:

```text
Principios estratégicos
        │
        ▼
Decisiones arquitectónicas
        │
        ▼
Especificación documental general
        │
        ▼
Especificaciones especializadas
        │
        ▼
Guías y procedimientos
        │
        ▼
Implementaciones y herramientas
```

Una herramienta no podrá redefinir por sí sola el modelo normativo.

---

## Responsabilidad de mantenimiento

Toda modificación de esta especificación deberá revisar su impacto sobre:

- documentos existentes;
- validadores;
- procesos de publicación;
- Knowledge Graph;
- asistentes de IA;
- documentación de onboarding;
- futuras especificaciones.

---

# Referencias

Esta especificación se relaciona con los siguientes documentos del proyecto.

| Documento | Responsabilidad |
|---|---|
| `VISION` | Propósito y dirección estratégica |
| `MANIFESTO` | Principios fundamentales |
| `ARQUITECTURA` | Arquitectura general del SGCC |
| `MODELO_DE_CONOCIMIENTO` | Modelo conceptual del conocimiento |
| `GOBERNANCE_MODEL` | Gobernanza general |
| `QUALITY` | Criterios de calidad |
| `GUIA_DE_ESTILO` | Normas editoriales |
| `AUTOMATION` | Automatización del sistema |
| `TOOLS_FRAMEWORK` | Arquitectura de herramientas |
| `QUALITY_PIPELINE` | Pipeline de calidad |
| `ESPECIFICACION_DE_COLECCIONES` | Modelo de colecciones |
| `ADR-0008` | Identidad persistente |
| `ADR-0019` | Independencia entre modelo lógico y representación física |

Las rutas físicas concretas deberán mantenerse mediante enlaces internos válidos en la implementación final del documento.

---

# Conformidad de esta especificación

La presente especificación deberá cumplir las mismas normas que define.

En particular:

- posee un identificador persistente;
- declara su tipo;
- mantiene versionado independiente;
- registra su estado;
- participa en las validaciones oficiales;
- conserva relaciones explícitas con otros documentos;
- evoluciona mediante un ciclo controlado.

Esta autorreferencia permite verificar que el modelo documental es aplicable a sus propios documentos normativos.

---

# Conclusión

El modelo documental constituye el contrato estructural y normativo del Sistema de Gestión del Conocimiento Culinario.

Gracias a esta especificación, los documentos del SGCC pueden:

- identificarse de manera persistente;
- estructurarse de forma homogénea;
- relacionarse semánticamente;
- validarse automáticamente;
- evolucionar con trazabilidad;
- publicarse en diferentes formatos;
- integrarse en grafos de conocimiento;
- utilizarse mediante sistemas de inteligencia artificial.

La independencia entre identidad, conocimiento y representación física permite que NovaCoquinaria evolucione sin quedar vinculada a una tecnología, estructura de directorios o canal de publicación concreto.

Esta especificación establece así la base normativa necesaria para que el conocimiento del SGCC pueda ser comprendido, reutilizado, validado y ampliado de forma coherente por colaboradores humanos, herramientas automatizadas y sistemas inteligentes.

