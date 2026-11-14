---
id: NAV-CATALOGO-CONOCIMIENTO-2026
tipo: gestion
titulo: Índice transversal de navegación del conocimiento
version: 1.0.0
estado: borrador
ultima_revision: 2026-11-14
---

# Índice transversal de navegación del conocimiento

## Propósito

Ofrecer un punto de acceso temático a documentos que, pese a existir en el repositorio, no recibían referencias desde otros documentos incluidos en el grafo de conocimiento. Este índice complementa los índices de cada módulo y la navegación general, sin sustituirlos.

**Criterio:** la auditoría de [Knowledge integrity #12](https://github.com/fran-eliot/NovaCoquinaria/actions/runs/43625192175) identificó 18 nodos sin referencias entrantes. Que un nodo aparezca en esa lista **no significa** que su contenido sea incorrecto, esté duplicado o resulte inaccesible desde el README principal: el grafo solo registra enlaces entre documentos Markdown con Front Matter.

## Módulos culinarios

Acceso directo a índices de dominio para explorar recetas, técnicas y relaciones:

- [Pastas](../../02_Pastas/README.md)
- [Legumbres](../../03_Legumbres/README.md)
- [Pescados y mariscos](../../06_Pescados_y_Mariscos/README.md)
- [Cocina asiática](../../07_Cocina_Asiatica/README.md)

## Plantillas reutilizables

- [Vinagreta base](../../12_Plantillas/01_Bases_Mediterraneas/vinagreta_base.md): patrón de aliño frío y emulsión sencilla

## Gestión y evolución del proyecto

- [Consolidación del conocimiento culinario](./CONSOLIDACION_CONOCIMIENTO.md): procedimiento de auditoría y seguimiento
- [Estructura del proyecto](./PROJECT_STRUCTURE.md): organización física del repositorio
- [Incorporación al proyecto](./PROJECT_ONBOARDING.md): recorrido de introducción al SGCC
- [Catálogo de oportunidades de evolución](./FUTURE_IDEAS.md): propuestas y oportunidades
- [Dominios culinarios](./DOMINIOS_CULINARIOS.md): clasificación de los dominios
- [Releases](./RELEASES.md): gestión de versiones
- [Auditoría automática del conocimiento](./generated/KNOWLEDGE_AUDIT.md): informe generado; consultar su fecha y alcance antes de interpretar las métricas

## Gobernanza

- [Modelo de gobernanza del SGCC](../governance/GOVERNANCE_MODEL.md)
- [Protocolo de colaboración](../governance/AI_PROTOCOL.md)
- [Estrategia de evolución del conocimiento](../governance/KNOWLEDGE_STRATEGY.md)
- [Modelo de deuda de conocimiento](../governance/KNOWLEDGE_DEBT.md)
- [Modelo de madurez del conocimiento](../governance/KNOWLEDGE_MATURITY.md)

## Especificaciones

- [Convenciones para las especificaciones](../specifications/CONVENCIONES.md)

## Interpretación de la auditoría

Este índice da acceso contextual a los 18 documentos señalados en la ejecución de referencia. Una nueva ejecución de `find_orphans.py` puede dejar de clasificarlos como huérfanos porque ahora reciben enlaces entrantes; **esa reducción mide conectividad del grafo, no calidad ni reutilización efectiva del contenido**.

La revisión posterior debe valorar la pertinencia de cada relación, la vigencia de la documentación y la necesidad de incorporar enlaces desde documentos de uso real.
