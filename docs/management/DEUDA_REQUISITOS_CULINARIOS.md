---
id: DOC-DEUDA-REQUISITOS-2026
titulo: Deuda semántica de requisitos culinarios
tipo: gestion
version: 0.1.0
estado: borrador
ultima_revision: 2026-11-19
---

# Deuda semántica de requisitos culinarios

Registro de cierre de CCE, CRM y CRR tras #267, commit `c31bf9d6372737c182df79a5961c75a3d5ebca72`, con los tres workflows de main satisfactorios. Corpus de investigación RET-D01 `c0dd020dea003d8a4f7a0278a43f30d81501a7f0`, huella de proyección `d72cb4cb48f8ab112d3f60003bb8a20acfe295925756e6456b12bf7b2648a89c`. Las propuestas no son cambios aceptados del contrato ni del recetario.

| ID | Fuente | Evidencia | Disposición |
|---|---|---|---|
| DR-01 | [Medallones asiáticos](../../05_Carnes/medallones_solomillo_asiaticos.md), REC-0008 | L89–96, cuatro guarniciones a elegir | Deuda de modelo: preservar choice, cardinalidad/presencia desconocidas |
| DR-02 | [Caballa japonesa](../../06_Pescados_y_Mariscos/caballa_japonesa.md), REC-0009 | L69–77, cinco guarniciones a elegir | Deuda de modelo: misma distinción, no nueve obligaciones simultáneas entre ambas recetas |
| DR-03 | [Merluza al horno](../../06_Pescados_y_Mariscos/merluza_al_horno_con_limon.md), REC-0057 | L32 y L43, descongelados si procede | Deuda de proyección: preparación condicional, no ingrediente opcional |
| DR-04 | [Gambas al ajillo](../../06_Pescados_y_Mariscos/gambas_al_ajillo.md), REC-0059 | L32 y L43, descongeladas si procede | Deuda de proyección: distinguir alcance de condición |
| DR-05 | [Calamares con kimchi](../../07_Cocina_Asiatica/calamares_salteados_con_kimchi.md), REC-0201 | L35 y L48, descongelado si procede | Deuda de proyección: distinguir alcance de condición |
| DR-06 | [Patatas a la importancia](../../04_Verduras/patatas_a_la_importancia_castellanas.md), REC-448 | L41 y L50–51, reponer aceite si hace falta | Deuda de proyección: conservar cantidad base, ajuste no evaluado |
| DR-07 | [Trucha a la navarra](../../06_Pescados_y_Mariscos/trucha_a_la_navarra_rellena_de_jamon.md), REC-493 | L35 y L46, añadir aceite si hace falta | Deuda de proyección: conservar cantidad base, ajuste no evaluado |

Las siete propuestas están registradas, no resueltas. Las fuentes originales ya contienen distinciones útiles: no se justifica reescribirlas para acomodar un reconocedor. Mantener abstención cuando un consumidor no pueda expresar el alcance; no presentar resultados de disponibilidad derivados como certeza. Las otras discrepancias documentadas (incluidos arroz alternativo, condiciones mixtas y limón de acompañamiento) permanecen en CRM/CRR; la tabla no es un inventario exhaustivo de deuda. No promover las 72 propuestas adicionales de identidad, ni considerar las 344 propuestas de opcionalidad CRR como correcciones.

## Cierre y reorientación

Se adopta la alternativa B de CRR-D05 para registrar deuda. CCE, CRM y CRR quedan cerrados como ciclos experimentales acotados; no se aprueba integración productiva ni un nuevo ciclo de reconocimiento. Las herramientas y pruebas se conservan como evidencia de investigación. La siguiente decisión es comparar capacidades de explotación práctica sobre v1.6.0, con casos de uso y valor directo, sin seleccionar aún plataforma ni nueva release.

## Referencias

- [Compatibilidad](./INVESTIGACION_COMPATIBILIDAD_CULINARIA.md)
- [Modelo](./INVESTIGACION_REQUISITOS_CULINARIOS.md)
- [Reconocimiento](./INVESTIGACION_RECONOCIMIENTO_REQUISITOS.md)
