---

id: TAB-0000
tipo: tabla
titulo: Índice de tablas
categoria: Tablas
estado: estable
version: 1.0.0
ultima_revision: 2026-07-01
etiquetas:
- tablas
- referencia
- consulta
- indice

---

# Tablas

## Objetivo

La carpeta `98_Tablas` contiene documentos de consulta rápida utilizados por el resto del repositorio.

Su función es centralizar información repetitiva, numérica o comparativa para evitar duplicidades en recetas, técnicas, ingredientes y plantillas.

---

# Qué debe ir en esta carpeta

Deben incluirse aquí documentos como:

* conversiones de unidades;
* equivalencias culinarias;
* tiempos de cocción;
* temperaturas de horno;
* conservación;
* congelación;
* seguridad alimentaria;
* sustituciones;
* proporciones resumidas;
* referencias rápidas.

---

# Qué NO debe ir en esta carpeta

No deben incluirse aquí:

* recetas completas;
* explicaciones largas de técnicas;
* documentos de despensa;
* plantillas de elaboración;
* notas personales;
* experimentos no consolidados.

Si una tabla requiere mucha explicación técnica, esa explicación deberá ir en `00_Bases` y la tabla quedará como resumen de consulta.

---

# Organización interna

Estructura recomendada:

```text
98_Tablas/
├── 01_Cocciones/
├── 02_Hornos/
├── 03_Conversiones/
├── 04_Conservacion/
├── 05_Seguridad/
├── 06_Sustituciones/
├── 07_Equivalencias/
└── README.md
```

---

# Criterios para crear una tabla nueva

Crear una tabla nueva cuando:

* la información vaya a consultarse con frecuencia;
* sea reutilizable por muchos documentos;
* permita comparar datos;
* evite repetir cantidades, tiempos o temperaturas;
* facilite tomar decisiones rápidas en cocina.

---

# Criterios para ampliar una tabla existente

Ampliar una tabla existente cuando:

* el nuevo dato pertenece claramente al mismo tema;
* no justifica un documento independiente;
* mejora la utilidad de la tabla;
* mantiene la coherencia de formato.

---

# Relación con otros módulos

## Relación con `00_Bases`

`00_Bases` explica el fundamento.

`98_Tablas` resume datos de consulta.

Ejemplo:

* `00_Bases/tecnicas/coccion_arroz.md` explica cómo cocer arroz.
* `98_Tablas/01_Cocciones/tiempos_coccion.md` resume tiempos y proporciones.

---

## Relación con recetas

Las recetas deben enlazar a las tablas cuando necesiten datos generales.

Ejemplo:

```markdown
Ver también: [Tiempos de cocción](../98_Tablas/01_Cocciones/tiempos_coccion.md)
```

---

# Tablas iniciales prioritarias

## Conversiones y equivalencias

* `03_Conversiones/conversiones_unidades.md`
* `03_Conversiones/equivalencias_culinarias.md`

## Cocciones

* `01_Cocciones/tiempos_coccion_arroz.md`
* `01_Cocciones/tiempos_coccion_legumbres.md`
* `01_Cocciones/tiempos_coccion_pasta.md`
* `01_Cocciones/tiempos_coccion_verduras.md`

## Horno

* `02_Hornos/temperaturas_horno.md`
* `02_Hornos/tiempos_horno_generales.md`

## Conservación

* `04_Conservacion/conservacion_alimentos_cocinados.md`
* `04_Conservacion/congelacion_alimentos.md`
* `04_Conservacion/recalentado_seguro.md`

## Sustituciones

* `06_Sustituciones/sustituciones_ingredientes.md`
* `06_Sustituciones/sustituciones_salsas_asiaticas.md`

---

# Reglas de formato

Las tablas deberán ser:

* claras;
* breves;
* comparables;
* fáciles de actualizar;
* compatibles con Markdown estándar.

Evitar tablas excesivamente largas.
Si una tabla crece demasiado, dividirla por dominio.

---

# Dependencias

* [Guía de estilo](../GUIA_DE_ESTILO.md)
* [Especificación de documentos](../docs/specifications/knowledge/ESPECIFICACION_DE_DOCUMENTOS.md)

---

# Véase también

* [Bases](../00_Bases/README.md)
* [Despensa](../11_Despensa/README.md)
* [Plantillas](../12_Plantillas/README.md)

---

# Utilizado por

Este módulo será utilizado por recetas, técnicas, documentos de despensa y plantillas del repositorio.

---

## Información del módulo

| Campo | Valor |
|--------|-------|
| Dominio | Consulta rápida |
| Estado | En desarrollo |
| Tipo de contenido | Tiempos, equivalencias y seguridad |
| Dependencias | Ninguna |
| Utilizado por | Todo el repositorio |
