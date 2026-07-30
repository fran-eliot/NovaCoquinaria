---
id: DOC-0009
titulo: Workflow de Desarrollo
tipo: gestion
version: 2.0
estado: estable
ultima_revision: 2026-07-20
---

# Workflow de Desarrollo

> **Proyecto:** NovaCoquinaria  
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento define el **proceso oficial de desarrollo y evolución del SGCC**.

Su finalidad es garantizar que todo cambio incorporado al sistema mantenga la coherencia del modelo de conocimiento, respete la arquitectura y contribuya al crecimiento sostenible del proyecto.

No describe herramientas específicas ni procedimientos técnicos detallados.

Define el ciclo de vida que debe seguir cualquier iniciativa de conocimiento.

---

# Principios del workflow

Toda evolución del SGCC deberá respetar los siguientes principios:

- el conocimiento precede a la implementación;
- reutilizar antes que crear;
- evolucionar antes que duplicar;
- validar antes que integrar;
- documentar antes que automatizar;
- mantener la coherencia arquitectónica en todo momento.

---

# Ciclo de vida del conocimiento

Toda iniciativa seguirá el mismo flujo de trabajo.

```text
Necesidad

      │

Análisis

      │

Inventario

      │

Diseño

      │

Desarrollo

      │

Relaciones

      │

Validación

      │

Integración

      │

Consolidación

      │

Nueva iteración
```

Cada fase aporta valor al sistema y prepara la siguiente.

---

# Fases del proceso

## 1. Identificación de la necesidad

Toda iniciativa comienza con una necesidad claramente identificada.

Puede consistir en:

- nuevo conocimiento;
- ampliación de conocimiento existente;
- reorganización documental;
- mejora arquitectónica;
- automatización.

La necesidad debe justificarse antes de iniciar cualquier desarrollo.

---

## 2. Inventario

Antes de crear nuevos documentos deberá revisarse el conocimiento existente.

El objetivo consiste en identificar:

- entidades reutilizables;
- relaciones ya documentadas;
- posibles duplicidades;
- oportunidades de mejora.

---

## 3. Diseño

Una vez comprendido el estado actual, se diseña la solución.

Durante esta fase se determina:

- qué entidades intervienen;
- qué relaciones serán necesarias;
- qué documentos deberán modificarse;
- si resulta necesaria una ADR.

---

## 4. Desarrollo

Solo después del diseño comienza la incorporación del conocimiento.

Las contribuciones deberán:

- reutilizar conocimiento existente;
- respetar el modelo de conocimiento;
- mantener una única responsabilidad documental;
- seguir las convenciones del proyecto.

---

## 5. Relacionar

Todo nuevo conocimiento deberá integrarse dentro del SGCC.

Esto implica:

- referencias cruzadas;
- actualización del Knowledge Graph;
- integración con entidades existentes;
- eliminación de posibles duplicidades.

El conocimiento aislado no aporta valor al sistema.

---

## 6. Validación

Todo cambio deberá superar las validaciones establecidas por el proyecto.

## Validación automática

Como mínimo:

- Front Matter;
- identificadores;
- enlaces internos;
- validación semántica;
- Knowledge Graph;
- documentos huérfanos.

## Validación arquitectónica

Además deberá verificarse:

- coherencia con el modelo de conocimiento;
- cumplimiento de los ADR;
- reutilización adecuada;
- ausencia de deuda arquitectónica significativa.

---

## 7. Integración

Una vez validado, el conocimiento podrá incorporarse al repositorio principal.

La integración implica actualizar, cuando corresponda:

- referencias;
- índices;
- documentación relacionada;
- estado del proyecto;
- bitácora;
- release.

---

## 8. Consolidación

Una iniciativa se considera consolidada cuando:

- el conocimiento está correctamente documentado;
- las relaciones están completas;
- supera todas las validaciones;
- no introduce deuda significativa;
- puede reutilizarse por futuras iniciativas.

---

# Prioridades de desarrollo

El proyecto seguirá siempre el siguiente orden de prioridad:

1. Corregir deuda de conocimiento.
2. Mejorar conocimiento existente.
3. Consolidar entidades reutilizables.
4. Incorporar nuevas relaciones.
5. Crear nuevas recetas.
6. Evolucionar la arquitectura cuando resulte necesario.

---

# Tipos de evolución

El workflow es aplicable a diferentes clases de cambios.

- incorporación de conocimiento;
- ampliación de entidades;
- reorganización documental;
- automatización;
- evolución arquitectónica;
- mejora de herramientas.

Todas las iniciativas siguen el mismo ciclo de vida.

---

# Integración con la gobernanza

El workflow forma parte del sistema de gobernanza del proyecto.

```text
Idea

↓

CONTRIBUTING

↓

DEVELOPMENT_WORKFLOW

↓

Validación

↓

PROJECT_STATUS

↓

BITÁCORA

↓

RELEASES

↓

ROADMAP
```

Cada documento aporta una responsabilidad específica dentro del proceso de evolución.

---

# Relaciones entre documentos

| Documento | Responsabilidad |
|-----------|-----------------|
| CONTRIBUTING | Cómo contribuir |
| DEVELOPMENT_WORKFLOW | Cómo evoluciona el proyecto |
| PROJECT_STATUS | Estado actual |
| BITÁCORA | Registro histórico |
| RELEASES | Versiones publicadas |
| ROADMAP | Dirección futura |

---

# Documentación relacionada

## Gobernanza

- CONTRIBUTING
- PROJECT_ONBOARDING
- CONTEXT

## Arquitectura

- ARQUITECTURA
- MODELO_DE_CONOCIMIENTO

## Gestión

- PROJECT_STATUS
- BITÁCORA
- RELEASES
- ROADMAP

---

# Conclusión

El desarrollo del SGCC no consiste únicamente en crear nuevos documentos.

Consiste en hacer evolucionar un sistema de conocimiento de forma controlada, coherente y sostenible.

Cada cambio debe fortalecer el conjunto, incrementar la reutilización y preservar la integridad del modelo de conocimiento.

El workflow constituye el mecanismo mediante el cual NovaCoquinaria transforma nuevas ideas en conocimiento integrado dentro de GASTRO.