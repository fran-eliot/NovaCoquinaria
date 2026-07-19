---
id: DOC-0012
titulo: Resumen de Decisiones
tipo: gestion
version: 1.1
estado: estable
ultima_revision: 2026-07-19
---

# Resumen de Decisiones

> Síntesis ejecutiva de las decisiones arquitectónicas, metodológicas y organizativas vigentes en NovaCoquinaria.

---

# Propósito

Este documento recopila las decisiones que actualmente gobiernan el proyecto.

Su finalidad es ofrecer una referencia rápida para comprender cómo funciona NovaCoquinaria sin necesidad de consultar todos los **Architecture Decision Records (ADR)**.

No sustituye a los ADR, sino que resume únicamente aquellas decisiones que permanecen vigentes.

La justificación, alternativas evaluadas y contexto histórico continúan documentándose en los ADR correspondientes.

---

# Principios fundamentales

Las siguientes decisiones constituyen la base del proyecto.

## El conocimiento es el activo principal

NovaCoquinaria se concibe como un **Sistema de Gestión del Conocimiento Culinario (SGCC)**.

Las recetas representan únicamente una parte del conocimiento gestionado.

---

## Documentar una sola vez

Cada concepto debe documentarse una única vez.

El conocimiento reutilizable será referenciado desde el resto de documentos para evitar duplicidades.

---

## Reutilizar antes que crear

Siempre que exista conocimiento válido deberá ampliarse antes de crear nuevos documentos.

La reutilización tiene prioridad sobre la duplicación.

---

## La arquitectura evoluciona por necesidad

La arquitectura únicamente se modifica cuando una necesidad real del conocimiento lo justifica.

No se incorporan nuevas capas ni complejidad innecesaria.

---

# Fuente de verdad

Se mantienen las siguientes decisiones:

- Markdown constituye la única fuente de verdad.
- `site_docs/` es un artefacto generado automáticamente.
- MkDocs publica el conocimiento, pero no lo gobierna.
- Ningún documento generado debe editarse manualmente.

---

# Organización del conocimiento

El conocimiento del SGCC se organiza mediante entidades especializadas con responsabilidades claramente diferenciadas.

Las principales decisiones son:

- el conocimiento es modular;
- cada entidad tiene una responsabilidad única;
- cada documento aporta un valor específico al sistema;
- las recetas reutilizan conocimiento mediante referencias;
- las relaciones entre documentos forman un Knowledge Graph.

---

# Modelo documental

Todo documento estructurado sigue las siguientes decisiones:

- utiliza Front Matter YAML;
- dispone de un identificador único y estable;
- mantiene enlaces relativos entre documentos;
- el identificador nunca depende de la ubicación física del archivo;
- la organización lógica prevalece sobre la estructura del repositorio.

---

# Calidad y automatización

Las siguientes decisiones gobiernan la calidad del proyecto.

## Validación automática

El repositorio incorpora validaciones para:

- Front Matter;
- identificadores únicos;
- enlaces internos;
- reglas semánticas;
- Knowledge Graph;
- documentos huérfanos.

Estas validaciones pueden actuar como *Quality Gate* del proyecto.

---

## Validación arquitectónica

La calidad arquitectónica continúa dependiendo de revisión humana.

Se verifica especialmente:

- ausencia de duplicidades;
- coherencia con el modelo de conocimiento;
- reutilización adecuada;
- cumplimiento de los ADR;
- consistencia documental.

La automatización complementa la revisión arquitectónica, pero no la sustituye.

---

# Knowledge Graph

Las decisiones actuales establecen que:

- cada documento estructurado representa un nodo;
- las referencias Markdown representan relaciones;
- las entidades se identifican mediante IDs estables;
- el grafo constituye una representación lógica del conocimiento.

El Knowledge Graph se utiliza para:

- analizar reutilización;
- detectar conocimiento huérfano;
- estudiar conectividad;
- validar relaciones semánticas.

---

# Gobernanza del conocimiento

La evolución del conocimiento se rige por los siguientes documentos:

- `KNOWLEDGE_STRATEGY.md`
- `KNOWLEDGE_DEBT.md`
- `KNOWLEDGE_MATURITY.md`
- `DEVELOPMENT_WORKFLOW.md`

Las decisiones metodológicas pertenecen a la documentación de gestión y no requieren modificaciones de la arquitectura cuando pueden resolverse mediante procesos documentales.

---

# Desarrollo del proyecto

Las decisiones operativas actuales son:

- utilización de Semantic Versioning;
- desarrollo mediante ramas independientes;
- integración mediante Pull Request;
- commits pequeños, descriptivos y revisables;
- prioridad de la calidad sobre la velocidad de desarrollo.

---

# Prioridad de decisión

Cuando varias alternativas sean posibles, se seguirá siempre el siguiente orden:

1. Coherencia arquitectónica.
2. Calidad del conocimiento.
3. Reutilización.
4. Simplicidad.
5. Automatización.
6. Nuevas funcionalidades.

---

# Filosofía del proyecto

Las decisiones anteriores pueden resumirse en los siguientes principios.

> **Documentar una vez. Reutilizar siempre.**

> **El conocimiento precede a las recetas.**

> **La arquitectura debe servir al conocimiento, nunca al contrario.**

---

# Revisión del documento

Este resumen deberá actualizarse cuando:

- se apruebe un nuevo ADR relevante;
- cambie un principio metodológico;
- evolucione el modelo arquitectónico del SGCC.

No es necesario modificarlo para cambios menores de implementación.

---

# Relación con otros documentos

Este documento complementa:

- [ARQUITECTURA](../ARQUITECTURA.md)
- [VISION](../VISION.md)
- [PROJECT_STRUCTURE](PROJECT_STRUCTURE.md)
- [DEVELOPMENT_WORKFLOW](DEVELOPMENT_WORKFLOW.md)
- [KNOWLEDGE_STRATEGY](KNOWLEDGE_STRATEGY.md)
- [KNOWLEDGE_DEBT](KNOWLEDGE_DEBT.md)
- [KNOWLEDGE_MATURITY](KNOWLEDGE_MATURITY.md)
- [AI_ONBOARDING](AI_ONBOARDING.md)
- [ADR](../adr/README.md)

No sustituye a los ADR.

Su responsabilidad consiste exclusivamente en ofrecer una visión resumida de las decisiones actualmente vigentes.
