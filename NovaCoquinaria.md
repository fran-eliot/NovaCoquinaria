# NovaCoquinaria

> Construyendo un Sistema de Gestión del Conocimiento Culinario reutilizable, evolutivo e independiente de la tecnología.

---

# ¿Qué es NovaCoquinaria?

NovaCoquinaria es un proyecto personal de ingeniería del conocimiento cuyo propósito es construir y mantener un **Sistema de Gestión del Conocimiento Culinario (SGCC)** capaz de capturar, estructurar, relacionar y reutilizar conocimiento culinario de forma organizada y sostenible.

El proyecto nace de una idea sencilla: el verdadero valor de una receta no reside únicamente en el plato que produce, sino en el conocimiento que concentra. Técnicas, ingredientes, procesos, proporciones, decisiones y experiencia constituyen un patrimonio que merece conservarse y evolucionar con el tiempo.

Por ello, NovaCoquinaria no se concibe como un recetario digital, sino como una base de conocimiento preparada para crecer durante toda una vida.

---

# ¿Por qué existe?

La mayoría de los recetarios tradicionales almacenan recetas como documentos independientes.

Como consecuencia, el mismo conocimiento se repite continuamente:

- técnicas;
- ingredientes;
- procesos;
- consejos;
- tiempos;
- explicaciones.

NovaCoquinaria propone un enfoque diferente.

Cada conocimiento se documenta una única vez y posteriormente se reutiliza mediante relaciones explícitas entre las distintas entidades que forman el sistema.

De esta forma, el crecimiento del proyecto incrementa el valor del conjunto sin aumentar innecesariamente la duplicación de información.

---

# Qué hace diferente a NovaCoquinaria

El proyecto organiza el conocimiento culinario como una red de entidades especializadas e interconectadas.

Entre ellas se encuentran:

- ingredientes;
- técnicas;
- patrones culinarios;
- platos canónicos;
- variantes;
- tablas de referencia;
- recetas.

Cada entidad posee una responsabilidad específica y puede evolucionar de forma independiente sin comprometer la coherencia global del sistema.

Las recetas dejan de ser el elemento central para convertirse en una aplicación concreta del conocimiento previamente consolidado.

---

# GASTRO: la arquitectura conceptual

La arquitectura conceptual que sustenta NovaCoquinaria recibe el nombre de **GASTRO**.

GASTRO define el modelo mediante el cual el conocimiento culinario se organiza, relaciona y evoluciona.

NovaCoquinaria constituye la implementación práctica de esa arquitectura.

```text
NovaCoquinaria
        │
        ▼
GASTRO
(Arquitectura conceptual)
        │
        ▼
Sistema de Gestión del
Conocimiento Culinario (SGCC)
```

La arquitectura conceptual es independiente tanto de la organización física del repositorio como de las herramientas utilizadas para gestionar el conocimiento.

---

# Valores del proyecto

NovaCoquinaria se desarrolla conforme a cinco valores fundamentales:

- claridad;
- reutilización;
- mantenibilidad;
- aprendizaje continuo;
- evolución sostenible.

Estos valores orientan todas las decisiones de diseño y desarrollo del proyecto.

Los principios que los sustentan se describen en el documento **MANIFESTO**.

---

# Público

El proyecto está concebido inicialmente para uso personal.

Sin embargo, desde su diseño adopta principios generales de ingeniería del conocimiento que permiten que su arquitectura pueda servir de inspiración para otros proyectos orientados a la gestión estructurada del conocimiento culinario.

---

# Qué no es NovaCoquinaria

NovaCoquinaria no pretende ser:

- un simple recetario digital;
- una colección de documentos independientes;
- una base de datos de recetas;
- una aplicación ligada a una tecnología concreta.

Su propósito es construir una base de conocimiento coherente, reutilizable y preparada para evolucionar.

---

# Relación con el resto de la documentación

Cada documento del proyecto responde a una responsabilidad específica.

NovaCoquinaria constituye el documento de identidad del proyecto.

La información especializada se desarrolla en los documentos correspondientes:

- **VISION** — dirección estratégica y objetivos a largo plazo;
- **MANIFESTO** — principios fundamentales del proyecto;
- **ARQUITECTURA** — diseño global del sistema;
- **MODELO_DE_CONOCIMIENTO** — entidades y relaciones del SGCC;
- **ROADMAP** — evolución prevista;
- **PROJECT_STATUS** — estado actual del proyecto.

---

# Conclusión

NovaCoquinaria no pretende organizar documentos.

Pretende organizar conocimiento.

Cada receta, técnica, ingrediente o patrón incorporado al sistema representa una nueva pieza de una base de conocimiento diseñada para preservar la experiencia culinaria, facilitar el aprendizaje continuo y servir de fundamento a futuras herramientas construidas sobre una misma arquitectura conceptual.

---

> Documentar una vez. Relacionar siempre. Reutilizar continuamente.