# CONTRIBUTING

> **Proyecto:** NovaCoquinaria  
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento define las **normas oficiales de contribución** al proyecto NovaCoquinaria.

Su finalidad es garantizar que toda contribución preserve la coherencia del SGCC, respete el modelo de conocimiento y aumente el valor global del sistema.

No describe el workflow del proyecto ni el proceso de incorporación de colaboradores.

Define únicamente los criterios que debe cumplir cualquier contribución para ser aceptada.

---

# Principios de contribución

Toda contribución deberá respetar los siguientes principios.

- aportar conocimiento útil;
- evitar duplicidades;
- reutilizar antes que crear;
- mantener una única responsabilidad;
- integrarse con el conocimiento existente;
- preservar la coherencia del SGCC.

El objetivo no consiste en incrementar el número de documentos, sino en mejorar el conocimiento del sistema.

---

# Flujo de contribución

Toda contribución seguirá el siguiente proceso.

```text
Necesidad

      │

Clasificación

      │

Reutilización

      │

Documentación

      │

Relaciones

      │

Validación

      │

Integración
```

Cada fase constituye un requisito previo para la siguiente.

---

# Clasificación de la contribución

Antes de crear o modificar un documento deberá determinarse la naturaleza de la contribución.

Puede consistir en:

- incorporar conocimiento nuevo;
- ampliar conocimiento existente;
- establecer nuevas relaciones;
- corregir información;
- reorganizar documentación;
- mejorar la arquitectura.

La clasificación adecuada condiciona el resto del proceso.

---

# Reutilización

Antes de crear cualquier documento deberá verificarse si el conocimiento ya existe.

Siempre se priorizará:

1. ampliar una entidad existente;
2. establecer nuevas relaciones;
3. crear una nueva entidad únicamente cuando resulte necesario.

La creación de nuevos documentos constituye siempre la última opción.

---

# Documentación

Toda contribución deberá:

- respetar la guía de estilo;
- seguir la especificación documental;
- mantener una única responsabilidad;
- incorporar referencias cruzadas cuando proceda.

Cada documento debe integrarse de forma natural dentro del sistema documental.

---

# Integración del conocimiento

El conocimiento nuevo no debe permanecer aislado.

Toda contribución deberá:

- relacionarse con entidades existentes;
- actualizar referencias cuando corresponda;
- integrarse en el Knowledge Graph;
- evitar la aparición de documentos huérfanos.

El valor del SGCC reside en las relaciones entre entidades tanto como en las propias entidades.

---

# Validación

Antes de integrarse, toda contribución deberá superar las validaciones establecidas por el proyecto.

## Validación documental

- estructura correcta;
- Front Matter;
- referencias internas;
- calidad documental.

---

## Validación semántica

- ausencia de duplicidades;
- coherencia con el modelo;
- relaciones correctas;
- reutilización adecuada.

---

## Validación arquitectónica

Cuando proceda deberá verificarse además:

- cumplimiento de los ADR;
- coherencia con la arquitectura;
- impacto sobre el SGCC.

---

# Cuándo crear una nueva entidad

Solo deberá crearse una nueva entidad cuando:

- represente un concepto nuevo;
- tenga responsabilidad única;
- pueda reutilizarse;
- no exista ya una entidad equivalente.

---

# Cuándo modificar una entidad existente

Se preferirá modificar una entidad existente cuando:

- la información complemente su contenido;
- aumente su calidad;
- mejore su reutilización;
- no altere su responsabilidad.

---

# Cambios arquitectónicos

Las modificaciones que afecten a:

- arquitectura;
- modelo de conocimiento;
- organización documental;
- estructura del repositorio;

deberán evaluarse previamente mediante una **Architecture Decision Record (ADR)**.

---

# Criterios de aceptación

Una contribución podrá considerarse aceptada cuando:

- aumenta el conocimiento del sistema;
- respeta el modelo conceptual;
- mantiene la coherencia arquitectónica;
- supera todas las validaciones;
- no introduce deuda significativa.

---

# Regla de oro

Antes de integrar cualquier cambio deberá responderse afirmativamente a la siguiente pregunta.

> **¿Esta contribución mejora el conocimiento del SGCC o simplemente incrementa la cantidad de información?**

Si únicamente aumenta la información disponible, probablemente todavía no está preparada para incorporarse.

---

# Relaciones entre documentos

| Documento | Responsabilidad |
|-----------|-----------------|
| PROJECT_ONBOARDING | Preparar nuevos colaboradores |
| CONTRIBUTING | Normas oficiales de contribución |
| DEVELOPMENT_WORKFLOW | Proceso oficial de evolución |
| ARQUITECTURA | Diseño del SGCC |
| MODELO_DE_CONOCIMIENTO | Modelo conceptual |
| ADR | Evolución arquitectónica |

---

# Documentación relacionada

## Incorporación

- PROJECT_ONBOARDING

## Gobernanza

- CONTEXT
- DEVELOPMENT_WORKFLOW

## Arquitectura

- ARQUITECTURA
- MODELO_DE_CONOCIMIENTO

## Calidad

- GUIA_DE_ESTILO
- ESPECIFICACION_DE_DOCUMENTOS

---

# Conclusión

Contribuir a NovaCoquinaria no consiste únicamente en añadir nuevos documentos.

Consiste en fortalecer un sistema de conocimiento mediante aportaciones coherentes, reutilizables y correctamente integradas.

Cada contribución debe incrementar el valor global del SGCC y facilitar su evolución futura.

La calidad de una contribución se mide por el conocimiento que aporta y por cómo enriquece el conjunto del sistema.