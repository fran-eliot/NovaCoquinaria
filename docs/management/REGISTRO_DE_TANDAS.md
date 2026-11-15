---
id: DOC-REGISTRO-TANDAS
tipo: gestion
titulo: Registro de tandas y evaluación de recetas domésticas
estado: borrador
version: 1.0.0
ultima_revision: 2026-11-15
etiquetas:
  - cocina-domestica
  - trazabilidad
  - versiones
  - evaluacion
---

# Registro de tandas y evaluación de recetas domésticas

## Propósito

Conservar cada elaboración real como **una tanda independiente** y poder decidir qué versión conviene repetir. El registro permite recuperar cantidades, método, resultado y preferencias sin mezclar una receta propuesta con otra realmente cocinada.

La [ficha de la receta](./INVENTARIO_COCINA_DOMESTICA.md) identifica el plato; el [registro de recetas cocinadas](./RECETAS_COCINADAS.md) resume las experiencias; este documento define una estructura reutilizable para describir **qué sucedió en cada preparación**. La [política de evolución](./EVOLUCION_DE_RECETAS.md) determina cuándo una versión puede considerarse preferida.

## Ficha breve para una tanda

Copiar el siguiente bloque como sección dentro de la receta correspondiente o como nota histórica enlazada. Utilizar «no registrado» cuando no conste un dato. **No convertir una cantidad recomendada en cantidad efectivamente utilizada.**

| Campo | Anotación |
|---|---|
| Receta e ID | Nombre y referencia de la ficha |
| Tanda / fecha | Identificador descriptivo; fecha aproximada o «no registrada» |
| Evidencia | Cocinada / preparación parcial / propuesta sin probar |
| Ingredientes utilizados | Peso bruto, peso limpio, unidades y presentación comercial |
| Líquidos, salsas y especias | Cantidades **realmente añadidas**, incluido cualquier ajuste final |
| Técnica, recipiente y tiempos | Orden de incorporación, temperatura y duración reales |
| Seguridad y conservación | Controles específicos relevantes para la elaboración |
| Resultado | Textura, sabor, espesor, rendimiento y observaciones |
| Valoración | Palabras propias registradas; no inventar puntuaciones |
| Comparación | Mejor / igual / peor / **sin comparación** frente a otra tanda identificada |
| Decisión | Mantener versión principal / preferir esta tanda / pendiente de comparar |
| Datos no registrados | Lista explícita de incertidumbres |

### Regla para modificar la receta principal

Una tanda puede contener una técnica o cantidad útil sin ser superior a la versión vigente. **Registrar no equivale a sustituir.** La versión principal solo se cambia con una preferencia explícita, una comparación sustentada o la corrección demostrable de un error de transcripción. El resto permanece como antecedente.

## Dos casos abiertos del repertorio habitual

### Boquerones en vinagre — REC-0217

[Ficha culinaria](../../06_Pescados_y_Mariscos/boquerones_en_vinagre.md).

| Campo | Registro disponible |
|---|---|
| Naturaleza | Plato habitual, con al menos una tanda descrita |
| Materia prima | Consulta de referencia para 400 g de boquerones; no está confirmado que sea el peso limpio de la tanda |
| Marinado de una tanda | 14 horas con tres partes de vinagre y una de limón |
| Valoración | «Algo salado y poco avinagrado» |
| Versión preferida | No reconstruida con certeza |
| Datos pendientes | Sal empleada, volumen total de líquido, peso limpio, congelación efectiva, hora de inicio y final, resultado de la última versión |

**Separar seguridad de sabor:** todo boquerón marinado sin cocción térmica requiere congelación adecuada para prevenir anisakis. Un ajuste de vinagre o tiempo no sustituye ese tratamiento.

**Siguiente comparación identificable:** registrar el resultado de un marinado con vinagre sin diluir, sin sal inicial y con duración controlada. Es una **propuesta**, no una elaboración ya realizada ni una versión preferida.

### Brazo de gitano de chocolate y galletas María — REC-0218

[Ficha culinaria](../../08_Postres/brazo_de_gitano_de_chocolate_y_galletas.md).

| Campo | Registro disponible |
|---|---|
| Naturaleza | Postre habitual confirmado |
| Ingrediente citado | Bote de crema de cacao de 400 g |
| Baño de galletas consultado | 120 ml de café fuerte y 1–2 cucharadas de whisky o brandy |
| Antecedente | Fórmula histórica con mantequilla y huevo; no acreditada como fórmula preferida |
| Versión preferida | No reconstruida con certeza |
| Datos pendientes | Peso de galletas, crema efectivamente usada, cantidad de mantequilla, montaje, tamaño, reposo y valoración comparativa |

**Siguiente comparación identificable:** registrar el montaje efectivo y la composición de la crema antes de optar por otra formulación. La receta propuesta sin huevo crudo no acredita que esa sea la preparación tradicional de casa.

## Cómo usar este registro

1. Antes de cocinar, identificar la receta existente y **conservar sus versiones anteriores**.
2. Durante la preparación, apuntar pesos y ajustes relevantes sin confundirlos con la fórmula inicial.
3. Después, registrar resultado real y una valoración breve.
4. Comparar exclusivamente **tandas identificadas**; si no hay comparación, mantener «sin comparación».
5. Actualizar la ficha principal solo si la evidencia justifica seleccionar una versión diferente.
6. Si se detecta un plato habitual ausente, crear una ficha nueva y enlazarla desde el [Inventario de cocina doméstica](./INVENTARIO_COCINA_DOMESTICA.md); no inventar experiencias retrospectivas.

## Principio de NovaCoquinaria

> Cada preparación genera evidencia; conservarla con precisión es más útil que reconstruir una receta perfecta que nadie ha probado.
