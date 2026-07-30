---
id: ARC-0016
tipo: arquitectura
titulo: Pipeline de Calidad
version: 2.0
estado: estable
ultima_revision: 2026-07-20
---

# Pipeline de Calidad

> **Proyecto:** NovaCoquinaria
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento define el Pipeline de Calidad utilizado por NovaCoquinaria para asegurar la consistencia del conocimiento antes de su publicación.

El Pipeline constituye el proceso mediante el cual el conocimiento evoluciona desde su edición hasta convertirse en documentación publicada.

Su misión consiste en detectar problemas, preservar la coherencia del SGCC y evitar que las inconsistencias alcancen la documentación distribuida.

---

# Filosofía

Todo documento incorporado al SGCC debe superar una serie de comprobaciones antes de considerarse válido.

El Pipeline nunca modifica el contenido.

Su responsabilidad consiste exclusivamente en verificar su calidad.

---

# Flujo general

```text
Autor

↓

Markdown

↓

Validación estructural

↓

Validación documental

↓

Validación arquitectónica

↓

Generación

↓

Publicación
```

Cada etapa únicamente comienza cuando la anterior ha finalizado correctamente.

---

# Etapas del Pipeline

## 1. Creación del conocimiento

El conocimiento se incorpora exclusivamente mediante documentos Markdown.

Markdown constituye la única fuente oficial de verdad del proyecto.

---

## 2. Validación estructural

Verifica que el documento pueda formar parte del SGCC.

Ejemplos de comprobaciones:

- Front Matter válido;
- metadatos obligatorios;
- formato correcto;
- identificadores presentes.

---

## 3. Validación documental

Comprueba la integridad documental.

Ejemplos:

- identificadores únicos;
- enlaces válidos;
- referencias existentes;
- relaciones coherentes.

---

## 4. Validación arquitectónica

Comprueba que el documento respeta la arquitectura del SGCC.

Ejemplos:

- organización documental;
- coherencia entre documentos;
- ausencia de duplicidades;
- cumplimiento de principios arquitectónicos.

---

## 5. Generación

Una vez validado el conocimiento se generan los artefactos derivados.

Ejemplos:

- documentación publicada;
- índices;
- estadísticas.

---

## 6. Publicación

La documentación generada puede publicarse mediante MkDocs u otros mecanismos equivalentes.

La publicación nunca constituye una fuente de verdad.

---

# Resultado del Pipeline

El Pipeline puede finalizar en tres estados.

## Correcto

El documento supera todas las comprobaciones.

Puede continuar el proceso.

---

## Advertencia

Se detectan aspectos mejorables que no comprometen la arquitectura.

La publicación puede continuar.

---

## Error bloqueante

Se detectan inconsistencias incompatibles con el modelo documental.

El proceso se detiene hasta resolverlas.

---

# Criterios de bloqueo

El Pipeline deberá interrumpirse cuando existan:

- Front Matter inválido;
- identificadores duplicados;
- enlaces rotos;
- referencias inexistentes;
- incoherencias arquitectónicas.

---

# Evolución

El Pipeline evolucionará progresivamente.

```text
Validación estructural

↓

Validación documental

↓

Validación arquitectónica

↓

Validación semántica

↓

Calidad del conocimiento
```

Cada nueva etapa ampliará las capacidades del Pipeline sin alterar los principios fundamentales.

---

# Relación con la automatización

El Pipeline constituye la principal aplicación práctica de la estrategia de automatización del SGCC.

La automatización proporciona las herramientas.

El Pipeline define el proceso.

---

# Relaciones documentales

| Documento | Responsabilidad |
|-----------|-----------------|
| AUTOMATION | Estrategia de automatización |
| TOOLS_FRAMEWORK | Arquitectura técnica |
| QUALITY | Modelo de calidad |
| ARQUITECTURA | Arquitectura del SGCC |

---

# Documentación relacionada

## Arquitectura

- AUTOMATION
- TOOLS_FRAMEWORK
- QUALITY
- ARQUITECTURA

## ADR

- ADR-0003 · Markdown como fuente de verdad
- ADR-0012 · Preparación para publicación web MkDocs

---

# Conclusión

El Pipeline de Calidad garantiza que únicamente el conocimiento consistente, coherente y alineado con la arquitectura del SGCC pueda evolucionar hasta convertirse en documentación publicada.

Constituye el mecanismo operativo que conecta la edición del conocimiento con su distribución, preservando en todo momento la integridad del sistema.