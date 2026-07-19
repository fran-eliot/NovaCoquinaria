---

id: ARC-0018
tipo: arquitectura
titulo: Especificación de Colecciones de Conocimiento
version: 1.0
estado: estable
ultima_revision: 2026-07-10
---

# Especificación de Colecciones de Conocimiento

## Objetivo

Este documento define la estructura, responsabilidad y reglas de las colecciones de conocimiento de NovaCoquinaria.

Las colecciones permiten planificar el desarrollo transversal de un dominio culinario sin modificar la organización física del repositorio.

Su finalidad es coordinar la evolución conjunta de:

* bases;
* técnicas;
* ingredientes;
* plantillas;
* tablas;
* recetas.

## Definición

Una colección de conocimiento es un documento de planificación que agrupa virtualmente documentos relacionados con un mismo dominio culinario.

Ejemplos:

* Wok.
* Currys.
* Arroces.
* Cocina mediterránea.
* Cocina japonesa.
* Marinados.
* Salsas.

Una colección no es una carpeta del conocimiento culinario ni una nueva categoría documental del SGCC.

## Responsabilidad

Una colección debe:

* definir el alcance de un dominio culinario;
* identificar el conocimiento existente;
* registrar el conocimiento pendiente;
* favorecer la reutilización;
* detectar carencias estructurales;
* facilitar la planificación de nuevas incorporaciones.

Una colección no debe:

* contener explicaciones culinarias completas;
* duplicar técnicas, ingredientes o recetas;
* sustituir los documentos originales;
* introducir conocimiento no documentado fuera de la colección;
* modificar la arquitectura física del repositorio.

## Ubicación

Las colecciones se almacenarán en:

```text
docs/collections/
```

El directorio contendrá:

```text
docs/collections/
├── README.md
├── wok.md
├── currys.md
├── arroces.md
└── ...
```

Solo se crearán colecciones cuando exista una necesidad real de planificación transversal.

## Nomenclatura

Los archivos utilizarán:

* letras minúsculas;
* nombres descriptivos;
* guion bajo cuando exista más de una palabra;
* extensión `.md`.

Ejemplos:

```text
wok.md
currys.md
cocina_mediterranea.md
salsas_asiaticas.md
```

## Front Matter

Todas las colecciones deberán incluir Front Matter YAML.

Ejemplo:

```yaml
---
id: COL-0001
tipo: coleccion
titulo: Wok
version: 1.0
estado: en_desarrollo
ultima_revision: 2026-07-10
---
```

### Campos obligatorios

| Campo             | Descripción                   |
| ----------------- | ----------------------------- |
| `id`              | Identificador único y estable |
| `tipo`            | Siempre `coleccion`           |
| `titulo`          | Nombre del dominio culinario  |
| `version`         | Versión documental            |
| `estado`          | Estado de desarrollo          |
| `ultima_revision` | Fecha de última revisión      |

## Identificadores

Las colecciones utilizarán el prefijo:

```text
COL
```

Formato:

```text
COL-0001
COL-0002
COL-0003
```

El identificador no deberá modificarse después de su asignación.

## Estados permitidos

| Estado             | Significado                                 |
| ------------------ | ------------------------------------------- |
| `propuesta`        | Dominio identificado, pero no iniciado      |
| `en_desarrollo`    | Incorporación activa de conocimiento        |
| `en_consolidacion` | Revisión de calidad, cobertura y relaciones |
| `referencia`       | Dominio suficientemente maduro y conectado  |
| `archivada`        | Colección retirada o sustituida             |

El estado no implica que el conocimiento sea definitivo.

## Estructura obligatoria

Toda colección seguirá esta estructura.

### Objetivo

Describe qué dominio se quiere desarrollar y qué valor aporta al SGCC.

### Estado

Indica el estado actual de la colección.

### Alcance

Define qué conocimientos forman parte de la colección y qué elementos quedan fuera.

### Conocimiento reutilizable

Organiza los documentos existentes y pendientes.

Subapartados recomendados:

* Bases.
* Técnicas.
* Ingredientes.
* Plantillas.
* Tablas.

### Recetas

Incluye las recetas relacionadas con el dominio.

Las recetas deberán enlazarse cuando existan.

Las recetas previstas podrán indicarse como pendientes.

### Deuda de conocimiento

Registra carencias que reducen la coherencia o reutilización del dominio.

Ejemplos:

* técnica fundamental ausente;
* ingrediente sin documentar;
* plantilla incompleta;
* documento reutilizable huérfano;
* referencias cruzadas pendientes.

### Próximos hitos

Indica las siguientes acciones prioritarias para consolidar la colección.

### Referencias

Enlaza documentos arquitectónicos, de gestión y culinarios relacionados.

## Representación de elementos

Se utilizarán listas de tareas Markdown.

Ejemplo:

```markdown
## Técnicas

- [x] [Cocinar al wok](../00_Bases/03_Tecnicas/wok.md)
- [x] [Saltear](../00_Bases/03_Tecnicas/saltear.md)
- [ ] Gestión del calor
```

Convenciones:

* `[x]` indica un documento existente y suficientemente integrado;
* `[ ]` indica conocimiento pendiente;
* los documentos existentes deberán incluir enlace;
* los elementos pendientes no deberán enlazar archivos inexistentes.

## Referencias y enlaces

Las colecciones deberán enlazar los documentos reales del SGCC.

No se copiará el contenido de los documentos enlazados.

Una colección podrá relacionarse con:

* bases;
* técnicas;
* ingredientes;
* plantillas;
* tablas;
* recetas;
* ADR;
* documentación de gestión.

## Relación con el Knowledge Graph

Las colecciones complementan el Knowledge Graph, pero no lo sustituyen.

El Knowledge Graph refleja relaciones documentales existentes.

Las colecciones reflejan:

* relaciones planificadas;
* conocimiento pendiente;
* madurez temática;
* prioridades de desarrollo.

Los enlaces a documentos existentes podrán formar parte del grafo.

Los elementos pendientes no deberán convertirse en nodos hasta que exista su documento correspondiente.

## Relación con la madurez del conocimiento

Las colecciones podrán utilizarse como fuente para evaluar la madurez de un dominio.

La madurez deberá basarse en criterios como:

* existencia de conocimiento reutilizable;
* conectividad entre documentos;
* ausencia de huérfanos relevantes;
* calidad editorial;
* diversidad de casos de uso;
* reutilización en recetas.

No se utilizarán porcentajes arbitrarios como medida principal.

## Relación con la deuda de conocimiento

Las carencias detectadas en una colección podrán trasladarse a:

```text
docs/management/KNOWLEDGE_DEBT.md
```

La colección describe la deuda dentro de su dominio.

El documento global de deuda consolida y prioriza las carencias del SGCC.

## Creación de una nueva colección

Antes de crear una colección deberá comprobarse:

1. Que existe un dominio culinario reconocible.
2. Que el dominio afecta a varias categorías documentales.
3. Que su planificación transversal aporta valor.
4. Que no existe otra colección equivalente.
5. Que la colección no puede sustituirse por un índice simple.

## Criterios de calidad

Una colección será válida cuando:

* tenga un alcance claro;
* no duplique conocimiento;
* enlace documentos existentes;
* diferencie claramente lo existente de lo pendiente;
* identifique deuda de conocimiento;
* facilite decisiones de priorización;
* pueda mantenerse con un esfuerzo razonable.

## Versionado

Las colecciones utilizarán versionado documental.

Cambios menores:

* actualización de checklists;
* incorporación de enlaces;
* actualización de estados;
* revisión de prioridades.

Cambios mayores:

* modificación sustancial del alcance;
* reorganización completa del dominio;
* división o fusión de colecciones.

## Regla fundamental

Una colección organiza el desarrollo del conocimiento.

No contiene el conocimiento que organiza.

## Referencias

* [ADR-0015 · Desarrollo del conocimiento mediante colecciones](./adr/ADR-0015-arquitectura-basada-en-reutilizacion-del-conocimiento.md)
* [Arquitectura](ARQUITECTURA.md)
* [Especificación de documentos](../ESPECIFICACION_DE_DOCUMENTOS.md)
* [Gestión del conocimiento](adr/ADR-0014-gestion-del-conocimiento.md)
* [Roadmap](ROADMAP.md)
