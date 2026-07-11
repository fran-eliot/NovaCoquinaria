# Resumen de Decisiones

> Síntesis de los principios arquitectónicos y metodológicos vigentes en NovaCoquinaria.

---

## Fuente de verdad

* Markdown es la única fuente de verdad.
* `site_docs/` es un artefacto generado automáticamente.
* MkDocs publica el conocimiento, pero no lo gobierna.
* No se editará manualmente ningún contenido generado.

---

## Organización del conocimiento

* El conocimiento se organiza de forma modular.
* Bases, técnicas, ingredientes, plantillas, tablas y recetas tienen responsabilidades diferenciadas.
* Cada conocimiento debe documentarse una sola vez.
* Las recetas reutilizan conocimiento mediante referencias.
* Se prioriza ampliar documentos existentes frente a crear duplicidades.

---

## Modelo documental

* Los documentos estructurados utilizan Front Matter YAML.
* Cada documento dispone de un identificador único y estable.
* Los documentos se relacionan mediante enlaces relativos.
* Los identificadores no dependen de la ruta física del archivo.

---

## Calidad y automatización

* El repositorio dispone de validaciones automáticas de:

  * Front Matter;
  * identificadores únicos;
  * enlaces internos.
* Las validaciones estructurales pueden actuar como Quality Gate.
* Las advertencias semánticas no son bloqueantes mientras el modelo esté en evolución.
* Las herramientas deben ser simples, auditables y reutilizables.

---

## Knowledge Graph

* Los documentos con Front Matter forman nodos del grafo.
* Los enlaces Markdown representan relaciones entre documentos.
* Los nodos se identifican mediante IDs estables y títulos.
* El grafo se utiliza para analizar:

  * reutilización;
  * conectividad;
  * conocimiento huérfano;
  * relaciones semánticas.

---

## Gobernanza del conocimiento

* `KNOWLEDGE_STRATEGY.md` define cómo debe crecer el conocimiento.
* `KNOWLEDGE_DEBT.md` registra carencias estructurales.
* `KNOWLEDGE_MATURITY.md` evalúa su evolución.
* La planificación del conocimiento pertenece a `docs/management/`.
* No se introduce una nueva capa arquitectónica cuando una necesidad puede resolverse mediante gestión documental.

---

## Desarrollo

* Se utiliza Semantic Versioning.
* Cada objetivo relevante se desarrolla en una rama.
* Cada iteración coherente se integra mediante Pull Request.
* Los commits deben ser pequeños y descriptivos.
* La arquitectura y la calidad tienen prioridad sobre las nuevas funcionalidades.

---

## Prioridad de decisión

1. Coherencia arquitectónica.
2. Calidad documental.
3. Reutilización.
4. Simplicidad.
5. Automatización.
6. Nuevas funcionalidades.

---

## Filosofía

> Documentar una vez. Reutilizar siempre.

---

## Referencias

* [Arquitectura](../ARQUITECTURA.md)
* [Roadmap](../ROADMAP.md)
* [Project Onboarding](PROJECT_ONBOARDING.md)
* [Knowledge Strategy](KNOWLEDGE_STRATEGY.md)
* [Knowledge Debt](KNOWLEDGE_DEBT.md)
* [Knowledge Maturity](KNOWLEDGE_MATURITY.md)
* [AI Onboarding](AI_ONBOARDING.md)
* [ADR](../adr/)
