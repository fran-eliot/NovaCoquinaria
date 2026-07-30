---
id: DOC-0018
titulo: Modelo de Conocimiento del SGCC
tipo: architecture
estado: active
version: 1.0.0
creado: 2026-06-29
ultima_revision: 2026-07-30
---

# MODELO_DE_CONOCIMIENTO

> **Proyecto:** NovaCoquinaria  
> **Arquitectura conceptual:** GASTRO – Sistema de Gestión del Conocimiento Culinario (SGCC)

---

# Objetivo

Este documento define el **modelo de conocimiento** del Sistema de Gestión del Conocimiento Culinario (SGCC).

Su propósito es establecer cómo se representa el conocimiento culinario mediante entidades, relaciones y reglas comunes que permitan organizarlo, reutilizarlo y hacerlo evolucionar de forma coherente.

Este documento describe exclusivamente el **modelo conceptual del dominio culinario**.

No define:

- la arquitectura del sistema;
- la estructura física del repositorio;
- las tecnologías utilizadas;
- la organización documental.

---

# ¿Qué es un modelo de conocimiento?

Un modelo de conocimiento describe la forma en que un dominio se representa mediante conceptos, entidades, relaciones y reglas.

Mientras un recetario tradicional organiza información alrededor de recetas independientes, GASTRO organiza el conocimiento culinario como una red de entidades especializadas relacionadas entre sí.

Cada entidad representa un único concepto.

Las relaciones permiten construir conocimiento complejo sin duplicar información.

El resultado es un sistema donde el valor no reside únicamente en cada documento individual, sino en la red de conocimiento formada por todos ellos.

---

# Principios del modelo

El modelo de conocimiento del SGCC se basa en los siguientes principios:

- cada entidad representa un único concepto;
- cada concepto debe documentarse una única vez;
- el conocimiento se reutiliza mediante relaciones explícitas;
- las entidades evolucionan de forma independiente;
- el conjunto debe formar un grafo coherente de conocimiento;
- la reutilización tiene prioridad sobre la duplicación.

Estos principios permiten que el conocimiento pueda crecer de forma sostenible sin perder consistencia.

---

# Arquitectura conceptual del conocimiento

El conocimiento culinario se estructura mediante cuatro elementos fundamentales.

```text
                Conocimiento culinario

                         │

        ┌────────────────┼────────────────┐
        │                │                │

    Entidades       Relaciones        Reglas

                         │

                         ▼

              Grafo de conocimiento

                         │

                         ▼

             Conocimiento reutilizable
```

Las entidades constituyen los conceptos.

Las relaciones conectan dichos conceptos.

Las reglas garantizan la coherencia del conjunto.

---

# Niveles de abstracción

El modelo organiza el conocimiento en distintos niveles.

```text
                 Conocimiento culinario

                         │

                   Ingredientes

                         │

                    Técnicas

                         │

               Patrones culinarios

                         │

                Platos canónicos

                         │

                    Variantes

                         │

                     Recetas

                         │

                 Menús (futuro)
```

Cada nivel reutiliza el conocimiento definido en los niveles anteriores.

---

# Taxonomía de entidades

Todas las entidades del SGCC representan un único concepto del dominio culinario.

```text
Entidad

├── Ingrediente
├── Técnica
├── Patrón culinario
├── Plato canónico
├── Variante
├── Receta
└── Tabla
```

---

## Ingrediente

Representa una materia prima o un producto culinario.

Responde a la pregunta:

> **¿Con qué se cocina?**

Ejemplos:

- pollo;
- gambas;
- arroz jazmín;
- salsa de soja;
- curry amarillo.

---

## Técnica

Representa una acción culinaria.

Responde a:

> **¿Cómo se cocina?**

Ejemplos:

- saltear;
- hornear;
- cocer;
- marinar;
- freír.

Las técnicas describen procesos, nunca platos.

---

## Patrón culinario

Representa una estructura culinaria reutilizable.

Responde a:

> **¿Qué patrón sigue esta elaboración?**

Ejemplos:

- sofrito mediterráneo;
- salteado asiático;
- curry base;
- marinada asiática.

Los patrones encapsulan conocimiento reutilizable compartido por múltiples platos.

---

## Plato canónico

Representa la elaboración de referencia de una familia culinaria.

Responde a:

> **¿Cuál es la receta de referencia?**

Ejemplos:

- arroz frito;
- tortilla francesa;
- risotto blanco;
- curry amarillo.

Constituye el punto de partida para sus variantes.

---

## Variante

Representa una especialización de un plato canónico.

Ejemplos:

- arroz frito con pollo;
- arroz chaufa;
- nasi goreng;
- yakimeshi.

Las variantes heredan la estructura general del plato de referencia e incorporan sus particularidades.

---

## Receta

Representa una implementación concreta de una elaboración.

Integra ingredientes, técnicas y patrones para producir una preparación específica.

Las recetas constituyen el nivel más concreto del conocimiento culinario.

---

## Tabla

Representa conocimiento transversal reutilizable.

Ejemplos:

- tiempos de cocción;
- equivalencias;
- sustituciones;
- escalas de picante;
- conservación.

Las tablas proporcionan información compartida por múltiples entidades.

---

# Relaciones del modelo

Las entidades se conectan mediante relaciones semánticas.

Estas relaciones constituyen el verdadero valor del SGCC.

## Relaciones estructurales

Describen la organización del conocimiento.

- **implementa**
- **deriva de**
- **pertenece a**

---

## Relaciones funcionales

Describen dependencias culinarias.

- **utiliza**
- **requiere**
- **sustituye**
- **acompaña**

---

## Relaciones documentales

Facilitan la navegación y la trazabilidad.

- **referencia**

---

# Reglas del modelo

Toda entidad del SGCC debe cumplir las siguientes reglas.

- representar un único concepto;
- mantener una única responsabilidad;
- evitar duplicar conocimiento existente;
- establecer relaciones explícitas con otras entidades;
- poder evolucionar sin afectar al resto del sistema.

Las relaciones enriquecen el conocimiento.

Nunca deben sustituirlo ni duplicarlo.

---

# Restricciones del modelo

No todas las relaciones son válidas.

| Relación | Estado |
|----------|:------:|
| Receta → Ingrediente | ✅ |
| Receta → Técnica | ✅ |
| Receta → Patrón culinario | ✅ |
| Variante → Plato canónico | ✅ |
| Patrón → Técnica | ✅ |
| Ingrediente → implementa → Receta | ❌ |
| Técnica → implementa → Técnica | ❌ |
| Tabla → cocina → Ingrediente | ❌ |

Estas restricciones garantizan la consistencia semántica del modelo.

---

# Grafo de conocimiento

Las entidades forman una red de relaciones.

```text
Pollo
   ▲
   │ utiliza
   │
Arroz frito con pollo
   │
implementa
   ▼
Arroz frito
   │
utiliza
   ▼
Salteado asiático
   │
requiere
   ▼
Saltear
```

El valor del sistema reside tanto en las entidades como en las conexiones existentes entre ellas.

---

# Ciclo de vida del conocimiento

Todo conocimiento incorporado al SGCC evoluciona siguiendo un proceso continuo.

```text
Experiencia

      │

Investigación

      │

Formalización

      │

Entidad

      │

Relaciones

      │

Validación

      │

Reutilización

      │

Mejora continua
```

Cada incorporación fortalece el conocimiento existente y amplía las posibilidades de reutilización del sistema.

---

# Modelo lógico y modelo físico

Este documento define exclusivamente el **modelo lógico** del conocimiento.

La estructura de carpetas, nombres de archivos o tecnologías empleadas pertenecen al modelo físico de implementación.

La ubicación física de un documento nunca determina su significado conceptual.

Esta separación permite que el conocimiento permanezca estable incluso cuando cambian las herramientas o la organización del repositorio.

---

# Evolución del modelo

El modelo de conocimiento está diseñado para evolucionar sin romper su coherencia conceptual.

La incorporación de nuevas entidades deberá:

- representar un concepto realmente nuevo;
- mantener una responsabilidad única;
- integrarse mediante relaciones explícitas;
- documentarse mediante la correspondiente ADR.

Toda ampliación deberá aumentar el valor global del SGCC sin introducir redundancias.

---

# Relaciones entre documentos

| Documento | Responsabilidad |
|-----------|-----------------|
| README | Punto de entrada |
| NovaCoquinaria | Identidad del proyecto |
| VISION | Dirección estratégica |
| MANIFESTO | Principios fundamentales |
| ARQUITECTURA | Diseño global del SGCC |
| **MODELO_DE_CONOCIMIENTO** | Lenguaje conceptual del sistema |
| ADR | Evolución del modelo |

---

# Documentación relacionada

## Arquitectura

- [ARQUITECTURA](./ARQUITECTURA.md)

## Estrategia

- [VISION](../VISION.md)
- [MANIFESTO](../../MANIFESTO.md)

## Decisiones arquitectónicas

- [ADR-0018 · Modelo del Conocimiento del SGCC](../governance/adr/ADR-0018-ontologia-del-conocimiento-del-sgcc.md)
- [ADR-0019 · Separación entre modelo lógico y estructura física](../governance/adr/ADR-0019-independencia-entre-el-modelo-logico-del-conocimiento-y-su-representacion-fisica.md)

---

# Conclusión

GASTRO no modela recetas.

Modela conocimiento.

Las recetas constituyen únicamente una manifestación concreta de una red mucho más amplia formada por ingredientes, técnicas, patrones, platos canónicos, variantes y relaciones semánticas.

Este modelo proporciona un lenguaje común para representar el conocimiento culinario de forma consistente, reutilizable y evolutiva, garantizando que el SGCC pueda crecer durante años sin perder coherencia conceptual.