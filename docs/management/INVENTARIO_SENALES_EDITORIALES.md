---
id: DOC-EDITORIAL-SIGNALS-2026
titulo: Inventario de señales editoriales recurrentes
tipo: gestion
version: 0.1.0
estado: diagnostico-no-bloqueante
ultima_revision: 2026-11-22
---

# Inventario reproducible de señales editoriales

## Problema observado

Las revisiones dirigidas de las PR #363–#376 corrigieron **96 fichas** con diagnósticos y recomendaciones de conservación ajenos a sus técnicas. La cifra corresponde a **recetas intervenidas**, no a defectos detectados automáticamente ni a una medición representativa del corpus. La PR #376 se fusionó en `e84d956a44967d0cab0d7cecd1416fe91fc9f22b` con los tres controles de CI en `success`.

Las herramientas existentes ya cubren integridad, inventario, extracción, dominio y consultas. Esta ampliación evita duplicarlas: añade **solo un inventario de frases editoriales repetidas** a los artefactos del workflow `Knowledge audit`.

## Contrato del inventario

Comando:

```bash
python tools/audit_editorial_signals.py --output site/knowledge-audit/editorial_signals.json
```

- **Fuente:** rutas Markdown rastreadas en el commit HEAD dentro de los diez módulos de recetas, excluyendo `README.md`; lectura del contenido canónico del checkout.
- **Alcance textual:** líneas de `## Puntos críticos`, `## Diagnóstico` y `## Conservación`. No se interpretan ingredientes, procedimientos, títulos, experiencias ni variantes.
- **Evidencia:** `source_commit`, `path`, `line`, `section`, `signal` y texto literal; recuentos por señal y módulo, recetas exploradas y recetas con una o más señales.
- **E01:** frases globales sobre proteínas y categorías de alimentos; **E02:** referencias estereotipadas a otras preparaciones; **E03:** diagnósticos de plantilla; **E04:** conservación genérica.
- **Reproducibilidad:** ordenación por ruta y orden de línea; claves de señal declaradas, sin inferencia semántica ni dependencias externas nuevas.
- **No intervención:** el escáner no modifica fichas ni genera correcciones. Detectar frases comunes no prueba que sean incorrectas, y no encontrar frases no certifica calidad, seguridad ni suficiencia práctica.

El informe se genera como artefacto efímero dentro de `site/knowledge-audit/`, no como Markdown canónico editado a mano. El recuento **no se fija en esta documentación**: debe consultarse el JSON del job y su commit, sin mezclar cortes históricos con `main` posterior.

## Uso editorial

1. Leer la evidencia y revisar cada ficha candidata junto a ingredientes y pasos originales.
2. Clasificar manualmente: `improcedente`, `válida en contexto` o `requiere investigación`; documentar la razón. Nunca asumir que todas las coincidencias son errores.
3. Agrupar las correcciones confirmadas por técnica o categoría en PR pequeñas. Conservar ingredientes, tiempos, cantidades, experiencias probadas y variantes salvo decisión editorial expresa.
4. Verificar integridad y auditoría ordinaria; comparar las mismas señales sobre commits concretos. Un descenso en coincidencias **no equivale por sí solo a mejora culinaria**.

## Límites y evolución

La primera versión es un **piloto textual de alta precisión relativa y cobertura desconocida**. Es posible que produzca tanto falsos positivos (frases genéricas pertinentes) como falsos negativos (textos incorrectos redactados de otra forma). No debe convertirse en un quality gate, puntuación de calidad, clasificador de recetas cocinables ni corrección automática.

Antes de ampliar reglas, revisar manualmente una muestra que incluya hallazgos y contraejemplos y documentar precisión observable, falsos positivos y vacíos. Esa evaluación será una PR posterior; no se autoriza implícitamente un sistema más amplio ni una release.
