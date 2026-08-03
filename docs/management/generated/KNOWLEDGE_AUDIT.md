---
id: REPORT-KNOWLEDGE-AUDIT
tipo: informe
titulo: Auditoría automática del conocimiento
version: 1.6.0
estado: generado
ultima_revision: 2026-08-03
tags:
  - dominios
  - auditoria
  - generado
---

# Auditoría automática del conocimiento

## Vista: dominios culinarios

> Este archivo es generado por `tools/audit_knowledge.py`. No debe editarse manualmente.

## Alcance de las métricas

La cobertura indicada es **estructural y preliminar**: mide la presencia de tipos documentales esperados. No evalúa por sí sola calidad culinaria, exhaustividad ni corrección semántica.

# Resumen

| Dominio | Madurez automática | PRIMARY | SECONDARY | MENTION | Cobertura estructural | Enlaces resueltos | Huérfanos |
|---|:---:|---:|---:|---:|---:|---:|---:|
| Currys | 🌿 Estructurado | 3 | 10 | 0 | 60 % | 100 % | 1 |
| Salteados asiáticos | 🌿 Estructurado | 4 | 28 | 1 | 60 % | 100 % | 0 |
| Arroces | 🌿 Estructurado | 9 | 25 | 0 | 60 % | 100 % | 1 |
| Pastas | 🌱 Exploración | 0 | 0 | 1 | 0 % | N/A | 0 |
| Legumbres | 🌱 Exploración | 0 | 0 | 0 | 0 % | N/A | 0 |
| Verduras | 🌿 Estructurado | 5 | 9 | 0 | 100 % | 100 % | 0 |
| Carnes | 🌿 Estructurado | 2 | 10 | 0 | 100 % | 100 % | 0 |
| Pescados y mariscos | 🌿 Estructurado | 1 | 6 | 0 | 100 % | 100 % | 0 |
| Huevos y lácteos | 🌿 Estructurado | 1 | 5 | 0 | 100 % | 100 % | 0 |
| Postres | 🌱 Exploración | 0 | 0 | 0 | 0 % | N/A | 0 |

---

# Dominio: Currys

**Madurez automática:** 🌿 Estructurado  
**Documentos PRIMARY:** 3  
**Documentos SECONDARY:** 10  
**Documentos MENTION:** 0  
**Cobertura estructural:** 60 %  
**Resolución de enlaces:** 100 %

## Distribución por tipo

| Tipo | Cantidad |
|---|---:|
| `ingrediente` | 1 |
| `plantilla` | 1 |
| `receta` | 1 |

## Implementaciones de referencia detectadas

- `REC-0017` · Curry amarillo de pollo (`05_Carnes/curry_amarillo_de_pollo.md`)

## Documentos de autoridad (PRIMARY)

- `REC-0017` · Curry amarillo de pollo (`05_Carnes/curry_amarillo_de_pollo.md`) — evidencia: `authority_link, pattern_title, declared_reference`
- `ING-0011` · Curry amarillo (`11_Despensa/08_Especias/curry_amarillo.md`) — evidencia: `title`
- `PLA-0002` · Curry base (`12_Plantillas/04_Cocciones/curry_base.md`) — evidencia: `title`

## Conocimiento reutilizado (SECONDARY)

- `BAS-0001` · Mise en place (`00_Bases/01_Fundamentos/mise_en_place.md`) — evidencia: `linked_from:REC-0017, linked_from:PLA-0002`
- `BAS-0004` · Sofreír (`00_Bases/03_Tecnicas/sofreir.md`) — evidencia: `linked_from:REC-0017, linked_from:PLA-0002`
- `ING-0001` · Arroz basmati (`11_Despensa/01_Cereales/arroz_basmati.md`) — evidencia: `linked_from:REC-0017`
- `ING-0007` · Salsa de pescado (`11_Despensa/09_Salsas/salsa_de_pescado.md`) — evidencia: `secondary_title, secondary_frontmatter, linked_from:REC-0017, linked_from:PLA-0002`
- `ING-0002` · Salsa de soja (`11_Despensa/09_Salsas/salsa_de_soja.md`) — evidencia: `linked_from:REC-0017, linked_from:PLA-0002`
- `ING-0008` · Vinagre de arroz (`11_Despensa/11_Condimentos/vinagre_de_arroz.md`) — evidencia: `linked_from:PLA-0002`
- `ING-0012` · Leche de coco (`11_Despensa/13_Bases_Culinarias/leche_de_coco.md`) — evidencia: `secondary_title, secondary_frontmatter, linked_from:REC-0017`
- `TAB-0002` · Tiempos de cocción (`98_Tablas/01_Cocciones/tiempos_coccion.md`) — evidencia: `linked_from:REC-0017`
- `TAB-0005` · Conservación, congelación y recalentado (`98_Tablas/04_Conservacion/conservacion_congelacion.md`) — evidencia: `linked_from:REC-0017`
- `TAB-0004` · Sustituciones de ingredientes (`98_Tablas/06_Sustituciones/sustituciones_ingredientes.md`) — evidencia: `linked_from:REC-0017`

## Menciones contextuales (MENTION)

- Ninguno.

## Documentos sin referencias salientes

- `ING-0011` · `11_Despensa/08_Especias/curry_amarillo.md`

## Tipos documentales no representados

- `tecnica`
- `tabla`

---

# Dominio: Salteados asiáticos

**Madurez automática:** 🌿 Estructurado  
**Documentos PRIMARY:** 4  
**Documentos SECONDARY:** 28  
**Documentos MENTION:** 1  
**Cobertura estructural:** 60 %  
**Resolución de enlaces:** 100 %

## Distribución por tipo

| Tipo | Cantidad |
|---|---:|
| `plantilla` | 1 |
| `receta` | 2 |
| `tecnica` | 1 |

## Implementaciones de referencia detectadas

- `REC-0018` · Pollo salteado con verduras (`05_Carnes/pollo_salteado_con_verduras.md`)
- `REC-0005` · Ternera con salsa de ostras (`05_Carnes/ternera_salsa_ostras.md`)

## Documentos de autoridad (PRIMARY)

- `BAS-0003` · Cocinar al wok (`00_Bases/03_Tecnicas/wok.md`) — evidencia: `title`
- `REC-0018` · Pollo salteado con verduras (`05_Carnes/pollo_salteado_con_verduras.md`) — evidencia: `authority_link, declared_reference`
- `REC-0005` · Ternera con salsa de ostras (`05_Carnes/ternera_salsa_ostras.md`) — evidencia: `authority_link, declared_reference`
- `PLA-0001` · Salteado asiático (`12_Plantillas/04_Cocciones/salteado_asiatico.md`) — evidencia: `title`

## Conocimiento reutilizado (SECONDARY)

- `BAS-0001` · Mise en place (`00_Bases/01_Fundamentos/mise_en_place.md`) — evidencia: `linked_from:REC-0018, linked_from:REC-0005, linked_from:BAS-0003, linked_from:PLA-0001`
- `BAS-0002` · Saltear (`00_Bases/03_Tecnicas/saltear.md`) — evidencia: `frontmatter, linked_from:REC-0018, linked_from:REC-0005, linked_from:BAS-0003, linked_from:PLA-0001`
- `REC-0001` · Arroz chaufa (`01_Arroces/arroz_chaufa.md`) — evidencia: `frontmatter`
- `REC-0021` · Arroz frito con gambas (`01_Arroces/arroz_frito_gambas.md`) — evidencia: `frontmatter`
- `REC-0020` · Arroz frito con huevo (`01_Arroces/arroz_frito_huevo.md`) — evidencia: `foreign_authority_link`
- `REC-0022` · Arroz frito con pollo (`01_Arroces/arroz_frito_pollo.md`) — evidencia: `frontmatter`
- `REC-0010` · Champiñones Sichuan (`04_Verduras/champiñones_sichuan.md`) — evidencia: `foreign_authority_link`
- `REC-0004` · Lomo asiático (`05_Carnes/lomo_asiatico.md`) — evidencia: `foreign_authority_link`
- `REC-0006` · Ternera con bambú (`05_Carnes/ternera_bambu.md`) — evidencia: `foreign_authority_link`
- `REC-0015` · Tintorera asiática (`06_Pescados_y_Mariscos/tintorera_asiatica.md`) — evidencia: `foreign_authority_link`
- `ING-0001` · Arroz basmati (`11_Despensa/01_Cereales/arroz_basmati.md`) — evidencia: `linked_from:REC-0018, linked_from:REC-0005`
- `ING-0015` · Pollo (`11_Despensa/03_Carnes/pollo.md`) — evidencia: `linked_from:REC-0018`
- `ING-0020` · Ternera (`11_Despensa/03_Carnes/ternera.md`) — evidencia: `linked_from:REC-0005`
- `ING-0014` · Ajo (`11_Despensa/06_Verduras/ajo.md`) — evidencia: `linked_from:REC-0018`
- `ING-0013` · Cebolla (`11_Despensa/06_Verduras/cebolla.md`) — evidencia: `linked_from:REC-0018, linked_from:REC-0005`
- `ING-0016` · Jengibre (`11_Despensa/06_Verduras/jengibre.md`) — evidencia: `linked_from:REC-0018`
- `ING-0017` · Pimiento (`11_Despensa/06_Verduras/pimiento.md`) — evidencia: `linked_from:REC-0005`
- `ING-0019` · Champiñón (`11_Despensa/07_Setas/champinon.md`) — evidencia: `linked_from:REC-0005`
- `ING-0003` · Mirin (`11_Despensa/09_Salsas/mirin.md`) — evidencia: `linked_from:REC-0018, linked_from:REC-0005, linked_from:PLA-0001`
- `ING-0004` · Salsa de ostras (`11_Despensa/09_Salsas/salsa_de_ostras.md`) — evidencia: `secondary_title, secondary_frontmatter, linked_from:REC-0018, linked_from:REC-0005, linked_from:PLA-0001`
- `ING-0002` · Salsa de soja (`11_Despensa/09_Salsas/salsa_de_soja.md`) — evidencia: `linked_from:REC-0018, linked_from:REC-0005, linked_from:PLA-0001`
- `ING-0005` · Aceite de sésamo (`11_Despensa/10_Aceites/aceite_de_sesamo.md`) — evidencia: `linked_from:REC-0018, linked_from:REC-0005, linked_from:PLA-0001`
- `PLA-0003` · Salsa china base (`12_Plantillas/02_Salsas/salsa_china_base.md`) — evidencia: `frontmatter, secondary_title, secondary_frontmatter, linked_from:REC-0005`
- `PLA-0004` · Marinada asiática (`12_Plantillas/03_Marinadas/marinada_asiatica.md`) — evidencia: `secondary_title, secondary_frontmatter, linked_from:REC-0005`
- `PLA-0008` · Arroz frito base (`12_Plantillas/05_Arroces/arroz_frito_base.md`) — evidencia: `frontmatter`
- `TAB-0002` · Tiempos de cocción (`98_Tablas/01_Cocciones/tiempos_coccion.md`) — evidencia: `linked_from:REC-0018, linked_from:REC-0005, linked_from:BAS-0003, linked_from:PLA-0001`
- `TAB-0005` · Conservación, congelación y recalentado (`98_Tablas/04_Conservacion/conservacion_congelacion.md`) — evidencia: `linked_from:REC-0018, linked_from:REC-0005`
- `TAB-0004` · Sustituciones de ingredientes (`98_Tablas/06_Sustituciones/sustituciones_ingredientes.md`) — evidencia: `linked_from:REC-0018`

## Menciones contextuales (MENTION)

- `ING-0023` · Gambas (`11_Despensa/05_Mariscos/gambas.md`) — evidencia: `controlled_heading`

## Documentos sin referencias salientes

- Ninguno.

## Tipos documentales no representados

- `ingrediente`
- `tabla`

---

# Dominio: Arroces

**Madurez automática:** 🌿 Estructurado  
**Documentos PRIMARY:** 9  
**Documentos SECONDARY:** 25  
**Documentos MENTION:** 0  
**Cobertura estructural:** 60 %  
**Resolución de enlaces:** 100 %

## Distribución por tipo

| Tipo | Cantidad |
|---|---:|
| `ingrediente` | 2 |
| `plantilla` | 1 |
| `receta` | 6 |

## Implementaciones de referencia detectadas

- `REC-0001` · Arroz chaufa (`01_Arroces/arroz_chaufa.md`)
- `REC-0022` · Arroz frito con pollo (`01_Arroces/arroz_frito_pollo.md`)

## Documentos de autoridad (PRIMARY)

- `REC-0003` · Arroz caldoso de alcachofas y marisco (`01_Arroces/arroz_caldoso_alcachofas_marisco.md`) — evidencia: `path`
- `REC-0001` · Arroz chaufa (`01_Arroces/arroz_chaufa.md`) — evidencia: `path`
- `REC-0021` · Arroz frito con gambas (`01_Arroces/arroz_frito_gambas.md`) — evidencia: `path`
- `REC-0020` · Arroz frito con huevo (`01_Arroces/arroz_frito_huevo.md`) — evidencia: `path`
- `REC-0022` · Arroz frito con pollo (`01_Arroces/arroz_frito_pollo.md`) — evidencia: `path`
- `REC-0002` · Arroz con higadillos (`01_Arroces/arroz_higadillos.md`) — evidencia: `path`
- `ING-0001` · Arroz basmati (`11_Despensa/01_Cereales/arroz_basmati.md`) — evidencia: `path`
- `ING-0021` · Arroz jazmín (`11_Despensa/01_Cereales/arroz_jazmin.md`) — evidencia: `path`
- `PLA-0008` · Arroz frito base (`12_Plantillas/05_Arroces/arroz_frito_base.md`) — evidencia: `path`

## Conocimiento reutilizado (SECONDARY)

- `BAS-0001` · Mise en place (`00_Bases/01_Fundamentos/mise_en_place.md`) — evidencia: `linked_from:REC-0003, linked_from:REC-0020, linked_from:REC-0002, linked_from:PLA-0008`
- `BAS-0002` · Saltear (`00_Bases/03_Tecnicas/saltear.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `BAS-0004` · Sofreír (`00_Bases/03_Tecnicas/sofreir.md`) — evidencia: `linked_from:REC-0003, linked_from:REC-0002`
- `BAS-0003` · Cocinar al wok (`00_Bases/03_Tecnicas/wok.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `REC-0005` · Ternera con salsa de ostras (`05_Carnes/ternera_salsa_ostras.md`) — evidencia: `linked_from:REC-0020`
- `ING-0015` · Pollo (`11_Despensa/03_Carnes/pollo.md`) — evidencia: `linked_from:REC-0020, linked_from:REC-0022, linked_from:PLA-0008`
- `ING-0020` · Ternera (`11_Despensa/03_Carnes/ternera.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `ING-0023` · Gambas (`11_Despensa/05_Mariscos/gambas.md`) — evidencia: `linked_from:REC-0021, linked_from:PLA-0008`
- `ING-0014` · Ajo (`11_Despensa/06_Verduras/ajo.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `ING-0013` · Cebolla (`11_Despensa/06_Verduras/cebolla.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `ING-0016` · Jengibre (`11_Despensa/06_Verduras/jengibre.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `ING-0017` · Pimiento (`11_Despensa/06_Verduras/pimiento.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `ING-0018` · Zanahoria (`11_Despensa/06_Verduras/zanahoria.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `ING-0019` · Champiñón (`11_Despensa/07_Setas/champinon.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `ING-0004` · Salsa de ostras (`11_Despensa/09_Salsas/salsa_de_ostras.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `ING-0002` · Salsa de soja (`11_Despensa/09_Salsas/salsa_de_soja.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `ING-0005` · Aceite de sésamo (`11_Despensa/10_Aceites/aceite_de_sesamo.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `ING-0008` · Vinagre de arroz (`11_Despensa/11_Condimentos/vinagre_de_arroz.md`) — evidencia: `thematic_title, frontmatter, secondary_title, secondary_frontmatter`
- `ING-0022` · Huevo (`11_Despensa/14_Huevos_Lacteos/huevo.md`) — evidencia: `secondary_title, secondary_frontmatter, linked_from:REC-0021, linked_from:REC-0020, linked_from:REC-0022`
- `PLA-0006` · Sofrito mediterráneo (`12_Plantillas/01_Bases_Mediterraneas/sofrito_mediterraneo.md`) — evidencia: `linked_from:REC-0003, linked_from:REC-0002`
- `PLA-0003` · Salsa china base (`12_Plantillas/02_Salsas/salsa_china_base.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `PLA-0004` · Marinada asiática (`12_Plantillas/03_Marinadas/marinada_asiatica.md`) — evidencia: `linked_from:PLA-0008`
- `PLA-0001` · Salteado asiático (`12_Plantillas/04_Cocciones/salteado_asiatico.md`) — evidencia: `linked_from:REC-0020, linked_from:PLA-0008`
- `TAB-0002` · Tiempos de cocción (`98_Tablas/01_Cocciones/tiempos_coccion.md`) — evidencia: `linked_from:REC-0003, linked_from:REC-0020, linked_from:REC-0002, linked_from:PLA-0008`
- `TAB-0005` · Conservación, congelación y recalentado (`98_Tablas/04_Conservacion/conservacion_congelacion.md`) — evidencia: `linked_from:REC-0003, linked_from:REC-0020, linked_from:REC-0002, linked_from:PLA-0008`

## Menciones contextuales (MENTION)

- Ninguno.

## Documentos sin referencias salientes

- `REC-0001` · `01_Arroces/arroz_chaufa.md`

## Tipos documentales no representados

- `tecnica`
- `tabla`

---

# Dominio: Pastas

**Madurez automática:** 🌱 Exploración  
**Documentos PRIMARY:** 0  
**Documentos SECONDARY:** 0  
**Documentos MENTION:** 1  
**Cobertura estructural:** 0 %  
**Resolución de enlaces:** N/A

## Distribución por tipo

| Tipo | Cantidad |
|---|---:|

## Implementaciones de referencia detectadas

- No detectadas automáticamente.

## Documentos de autoridad (PRIMARY)

- Ninguno.

## Conocimiento reutilizado (SECONDARY)

- Ninguno.

## Menciones contextuales (MENTION)

- `ING-0023` · Gambas (`11_Despensa/05_Mariscos/gambas.md`) — evidencia: `controlled_heading`

## Documentos sin referencias salientes

- Ninguno.

## Tipos documentales no representados

- `ingrediente`
- `tecnica`
- `plantilla`
- `receta`
- `tabla`

---

# Dominio: Legumbres

**Madurez automática:** 🌱 Exploración  
**Documentos PRIMARY:** 0  
**Documentos SECONDARY:** 0  
**Documentos MENTION:** 0  
**Cobertura estructural:** 0 %  
**Resolución de enlaces:** N/A

## Distribución por tipo

| Tipo | Cantidad |
|---|---:|

## Implementaciones de referencia detectadas

- No detectadas automáticamente.

## Documentos de autoridad (PRIMARY)

- Ninguno.

## Conocimiento reutilizado (SECONDARY)

- Ninguno.

## Menciones contextuales (MENTION)

- Ninguno.

## Documentos sin referencias salientes

- Ninguno.

## Tipos documentales no representados

- `ingrediente`
- `tecnica`
- `plantilla`
- `receta`
- `tabla`

---

# Dominio: Verduras

**Madurez automática:** 🌿 Estructurado  
**Documentos PRIMARY:** 5  
**Documentos SECONDARY:** 9  
**Documentos MENTION:** 0  
**Cobertura estructural:** 100 %  
**Resolución de enlaces:** 100 %

## Distribución por tipo

| Tipo | Cantidad |
|---|---:|
| `ingrediente` | 5 |

## Implementaciones de referencia detectadas

- No detectadas automáticamente.

## Documentos de autoridad (PRIMARY)

- `ING-0014` · Ajo (`11_Despensa/06_Verduras/ajo.md`) — evidencia: `path`
- `ING-0013` · Cebolla (`11_Despensa/06_Verduras/cebolla.md`) — evidencia: `path`
- `ING-0016` · Jengibre (`11_Despensa/06_Verduras/jengibre.md`) — evidencia: `path`
- `ING-0017` · Pimiento (`11_Despensa/06_Verduras/pimiento.md`) — evidencia: `path`
- `ING-0018` · Zanahoria (`11_Despensa/06_Verduras/zanahoria.md`) — evidencia: `path`

## Conocimiento reutilizado (SECONDARY)

- `REC-0021` · Arroz frito con gambas (`01_Arroces/arroz_frito_gambas.md`) — evidencia: `frontmatter`
- `REC-0022` · Arroz frito con pollo (`01_Arroces/arroz_frito_pollo.md`) — evidencia: `frontmatter`
- `REC-0012` · Brócoli salteado (`04_Verduras/brocoli.md`) — evidencia: `thematic_path`
- `REC-0011` · Champiñones al ajillo (`04_Verduras/champiñones_ajillo.md`) — evidencia: `thematic_path`
- `REC-0010` · Champiñones Sichuan (`04_Verduras/champiñones_sichuan.md`) — evidencia: `thematic_path`
- `REC-0013` · Habas con jamón (`04_Verduras/habas_jamon.md`) — evidencia: `thematic_path`
- `REC-0018` · Pollo salteado con verduras (`05_Carnes/pollo_salteado_con_verduras.md`) — evidencia: `thematic_title, frontmatter`
- `REC-0014` · Gambas al ajillo (`06_Pescados_y_Mariscos/gambas_ajillo.md`) — evidencia: `secondary_frontmatter`
- `ING-0019` · Champiñón (`11_Despensa/07_Setas/champinon.md`) — evidencia: `thematic_title, frontmatter`

## Menciones contextuales (MENTION)

- Ninguno.

## Documentos sin referencias salientes

- Ninguno.

## Tipos documentales no representados

- Ninguno.

---

# Dominio: Carnes

**Madurez automática:** 🌿 Estructurado  
**Documentos PRIMARY:** 2  
**Documentos SECONDARY:** 10  
**Documentos MENTION:** 0  
**Cobertura estructural:** 100 %  
**Resolución de enlaces:** 100 %

## Distribución por tipo

| Tipo | Cantidad |
|---|---:|
| `ingrediente` | 2 |

## Implementaciones de referencia detectadas

- No detectadas automáticamente.

## Documentos de autoridad (PRIMARY)

- `ING-0015` · Pollo (`11_Despensa/03_Carnes/pollo.md`) — evidencia: `path`
- `ING-0020` · Ternera (`11_Despensa/03_Carnes/ternera.md`) — evidencia: `path`

## Conocimiento reutilizado (SECONDARY)

- `REC-0001` · Arroz chaufa (`01_Arroces/arroz_chaufa.md`) — evidencia: `frontmatter`
- `REC-0022` · Arroz frito con pollo (`01_Arroces/arroz_frito_pollo.md`) — evidencia: `thematic_title, frontmatter`
- `REC-0017` · Curry amarillo de pollo (`05_Carnes/curry_amarillo_de_pollo.md`) — evidencia: `thematic_path`
- `REC-0007` · Hamburguesa asiática (`05_Carnes/hamburguesa_asiatica.md`) — evidencia: `thematic_path`
- `REC-0016` · Hamburguesa especiada (`05_Carnes/hamburguesa_especiada.md`) — evidencia: `thematic_path`
- `REC-0004` · Lomo asiático (`05_Carnes/lomo_asiatico.md`) — evidencia: `thematic_path`
- `REC-0008` · Medallones de solomillo asiáticos (`05_Carnes/medallones_solomillo_asiaticos.md`) — evidencia: `thematic_path`
- `REC-0018` · Pollo salteado con verduras (`05_Carnes/pollo_salteado_con_verduras.md`) — evidencia: `thematic_path`
- `REC-0006` · Ternera con bambú (`05_Carnes/ternera_bambu.md`) — evidencia: `thematic_path`
- `REC-0005` · Ternera con salsa de ostras (`05_Carnes/ternera_salsa_ostras.md`) — evidencia: `thematic_path`

## Menciones contextuales (MENTION)

- Ninguno.

## Documentos sin referencias salientes

- Ninguno.

## Tipos documentales no representados

- Ninguno.

---

# Dominio: Pescados y mariscos

**Madurez automática:** 🌿 Estructurado  
**Documentos PRIMARY:** 1  
**Documentos SECONDARY:** 6  
**Documentos MENTION:** 0  
**Cobertura estructural:** 100 %  
**Resolución de enlaces:** 100 %

## Distribución por tipo

| Tipo | Cantidad |
|---|---:|
| `ingrediente` | 1 |

## Implementaciones de referencia detectadas

- No detectadas automáticamente.

## Documentos de autoridad (PRIMARY)

- `ING-0023` · Gambas (`11_Despensa/05_Mariscos/gambas.md`) — evidencia: `path`

## Conocimiento reutilizado (SECONDARY)

- `REC-0003` · Arroz caldoso de alcachofas y marisco (`01_Arroces/arroz_caldoso_alcachofas_marisco.md`) — evidencia: `thematic_title, frontmatter`
- `REC-0021` · Arroz frito con gambas (`01_Arroces/arroz_frito_gambas.md`) — evidencia: `thematic_title, frontmatter`
- `REC-0009` · Caballa japonesa (`06_Pescados_y_Mariscos/caballa_japonesa.md`) — evidencia: `thematic_path`
- `REC-0014` · Gambas al ajillo (`06_Pescados_y_Mariscos/gambas_ajillo.md`) — evidencia: `thematic_path`
- `REC-0015` · Tintorera asiática (`06_Pescados_y_Mariscos/tintorera_asiatica.md`) — evidencia: `thematic_path`
- `ING-0007` · Salsa de pescado (`11_Despensa/09_Salsas/salsa_de_pescado.md`) — evidencia: `thematic_title, frontmatter`

## Menciones contextuales (MENTION)

- Ninguno.

## Documentos sin referencias salientes

- Ninguno.

## Tipos documentales no representados

- Ninguno.

---

# Dominio: Huevos y lácteos

**Madurez automática:** 🌿 Estructurado  
**Documentos PRIMARY:** 1  
**Documentos SECONDARY:** 5  
**Documentos MENTION:** 0  
**Cobertura estructural:** 100 %  
**Resolución de enlaces:** 100 %

## Distribución por tipo

| Tipo | Cantidad |
|---|---:|
| `ingrediente` | 1 |

## Implementaciones de referencia detectadas

- No detectadas automáticamente.

## Documentos de autoridad (PRIMARY)

- `ING-0022` · Huevo (`11_Despensa/14_Huevos_Lacteos/huevo.md`) — evidencia: `path`

## Conocimiento reutilizado (SECONDARY)

- `REC-0001` · Arroz chaufa (`01_Arroces/arroz_chaufa.md`) — evidencia: `frontmatter`
- `REC-0021` · Arroz frito con gambas (`01_Arroces/arroz_frito_gambas.md`) — evidencia: `frontmatter`
- `REC-0020` · Arroz frito con huevo (`01_Arroces/arroz_frito_huevo.md`) — evidencia: `thematic_title, frontmatter`
- `REC-0022` · Arroz frito con pollo (`01_Arroces/arroz_frito_pollo.md`) — evidencia: `frontmatter`
- `ING-0012` · Leche de coco (`11_Despensa/13_Bases_Culinarias/leche_de_coco.md`) — evidencia: `secondary_title, secondary_frontmatter`

## Menciones contextuales (MENTION)

- Ninguno.

## Documentos sin referencias salientes

- Ninguno.

## Tipos documentales no representados

- Ninguno.

---

# Dominio: Postres

**Madurez automática:** 🌱 Exploración  
**Documentos PRIMARY:** 0  
**Documentos SECONDARY:** 0  
**Documentos MENTION:** 0  
**Cobertura estructural:** 0 %  
**Resolución de enlaces:** N/A

## Distribución por tipo

| Tipo | Cantidad |
|---|---:|

## Implementaciones de referencia detectadas

- No detectadas automáticamente.

## Documentos de autoridad (PRIMARY)

- Ninguno.

## Conocimiento reutilizado (SECONDARY)

- Ninguno.

## Menciones contextuales (MENTION)

- Ninguno.

## Documentos sin referencias salientes

- Ninguno.

## Tipos documentales no representados

- `ingrediente`
- `tecnica`
- `plantilla`
- `receta`
- `tabla`

---

# Notas

- La vista se limita a documentos culinarios fuente y excluye README, gestión, arquitectura, especificaciones e informes.
- La cobertura y la madurez automáticas se calculan exclusivamente con asociaciones `PRIMARY`.
- Las asociaciones `SECONDARY` representan conocimiento reutilizado y `MENTION` contexto incidental.
- Un documento puede relacionarse con varios dominios con distintos niveles de asociación.
- En dominios de ingrediente, solo los documentos `ingrediente` de sus rutas de autoridad pueden ser `PRIMARY`.
- Las recetas de carpetas temáticas de ingredientes se clasifican como `SECONDARY`.
- La expansión por enlaces parte únicamente de bases, técnicas, plantillas y recetas `PRIMARY`.
- Las recetas transversales pueden ser `PRIMARY` de un patrón cuando su título es inequívoco o están declaradas como referencia.
- Las demás recetas con ruta canónica externa permanecen como `SECONDARY` del patrón.
- La madurez automática se adapta a `PATTERN`, `CATEGORY` e `INGREDIENT`.
- `MENTION` solo analiza encabezados culinarios controlados; no recorre todo el cuerpo.
- Los tipos esperados se adaptan a la naturaleza del dominio.
- `PRIMARY` prioriza rutas, dominio explícito, títulos controlados y enlaces a plantillas de autoridad.
- Las reglas de dominio se mantienen en `KNOWLEDGE_RULES` dentro de `tools/audit_knowledge.py`.
- La madurez automática es orientativa y no sustituye la revisión culinaria humana.
