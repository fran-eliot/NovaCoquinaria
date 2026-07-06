# ADR-0013 - Estrategia de Licencia, Privacidad y Publicación

**Estado:** Aceptado

**Fecha:** 2026-06-29

**Autor:** Fran Ramírez

---

# Contexto

NovaCoquinaria nace como repositorio privado, pero podría convertirse en el futuro en una web pública, aplicación, portfolio técnico o proyecto abierto.

El repositorio puede contener:

* recetas propias;
* notas personales;
* referencias culturales;
* documentación técnica;
* decisiones de arquitectura;
* posibles imágenes o recursos externos.

---

# Problema

Antes de hacer público el proyecto es necesario definir una estrategia sobre:

* qué contenido puede publicarse;
* qué contenido debe mantenerse privado;
* qué licencia tendrá el proyecto;
* cómo gestionar recursos externos;
* cómo evitar publicar información personal accidentalmente.

---

# Decisión

El repositorio comenzará como **privado**.

La publicación pública se evaluará cuando el contenido alcance suficiente madurez y se haya revisado su privacidad.

La licencia definitiva se decidirá antes de hacer público el proyecto.

Mientras tanto, el contenido se considerará de uso personal y privado.

---

# Principios

## Privacidad por defecto

Todo contenido nuevo se considera privado hasta que se decida expresamente lo contrario.

---

## Separación entre contenido personal y contenido publicable

Cuando sea necesario, se distinguirá entre:

* contenido publicable;
* notas personales;
* experimentos;
* información sensible;
* referencias privadas.

---

## Revisión previa a publicación

Antes de hacer público el repositorio deberá revisarse:

* nombres personales;
* direcciones;
* datos privados;
* imágenes propias;
* referencias a terceros;
* fuentes externas;
* contenido copiado de otros sitios.

---

## Respeto a fuentes externas

No se incorporará contenido protegido por derechos de autor de forma literal salvo citas breves justificadas.

Las recetas, técnicas y explicaciones deberán redactarse con elaboración propia.

---

# Opciones de licencia futuras

## Licencia de código

Si el proyecto incorpora scripts, automatizaciones o aplicación, se podrá utilizar una licencia de software.

Opciones posibles:

* MIT;
* Apache 2.0;
* GPL.

---

## Licencia de contenido

Para recetas, textos, imágenes o documentación culinaria podrá considerarse una licencia Creative Commons.

Opciones posibles:

* CC BY;
* CC BY-SA;
* CC BY-NC;
* CC BY-NC-SA.

---

# Recomendación inicial

Mientras el proyecto siga en fase privada, no se fijará todavía una licencia pública definitiva.

Cuando se decida publicar, se evaluará separar:

* licencia para código;
* licencia para contenido;
* condiciones para imágenes y recursos externos.

---

# Justificación

Diferenciar privacidad, licencia y publicación evita problemas futuros.

El proyecto puede evolucionar hacia una aplicación o web pública, pero no debe precipitarse la apertura antes de revisar el contenido.

---

# Alternativas consideradas

## Publicar desde el inicio

**Descartado temporalmente**.

El proyecto aún está en fase de diseño y puede contener contenido personal o inmaduro.

---

## No definir licencia

**Aceptable durante la fase privada**, pero no recomendable antes de publicar.

---

## Utilizar una única licencia para todo

**Posible**, pero podría ser insuficiente si el repositorio incluye tanto código como contenido culinario.

---

# Consecuencias

## Ventajas

* Mayor control sobre la publicación.
* Menor riesgo de exponer datos privados.
* Flexibilidad para decidir la licencia más adelante.
* Mejor preparación para uso como portfolio o proyecto abierto.

## Inconvenientes

* Será necesaria una revisión antes de publicar.
* La decisión de licencia queda pendiente.

---

# Impacto futuro

Esta decisión permitirá convertir NovaCoquinaria en:

* proyecto público;
* portfolio técnico;
* web culinaria;
* aplicación;
* proyecto abierto;

sin comprometer privacidad ni derechos de autor.

---

# Dependencias

* [ADR-0011 - Separación entre Marca, Producto, Sistema y Repositorio](./ADR-0011-separacion-entre-marca-producto-sistema-y-repositorio.md)
* [ADR-0012 - Preparación para Publicación Web con MkDocs](./ADR-0012-preparacion-para-publicacion-web-mkdocs.md)

---

# Véase también

* [README](../../README.md)
* [LICENSE](../../LICENSE.md)
* [CHANGELOG](../../CHANGELOG.md)

---

# Utilizado por

Este ADR deberá consultarse antes de hacer público el repositorio o reutilizar contenido fuera del ámbito personal.
