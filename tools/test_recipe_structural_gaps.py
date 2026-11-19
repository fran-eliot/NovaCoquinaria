import unittest
from common import ROOT_DIR
from extract_recipe_metadata import snapshot_bytes
from extract_recipe_ingredients import extract_ingredients
from extract_recipe_content import extract_content

COMMIT = "dc43b6b7d89d37884e2e602cca97a1cfac1e4482"

class GapRegressionTests(unittest.TestCase):
    def test_observed_ingredient_gaps(self):
        cases = {
            "05_Carnes/ropa_vieja_base_y_pulled_pork.md":13,
            "04_Verduras/zanahorias_alinadas_andaluzas.md":7,
            "04_Verduras/zanahorias_alinadas_magrebies.md":8,
            "04_Verduras/zanahorias_alinadas_asiaticas.md":8,
            "06_Pescados_y_Mariscos/boquerones_en_vinagre.md":6,
            "08_Postres/brazo_de_gitano_de_chocolate_y_galletas.md":6,
        }
        for path,count in cases.items():
            with self.subTest(path=path):
                entries,_=extract_ingredients(snapshot_bytes(ROOT_DIR,COMMIT,path),path,{})
                self.assertEqual(len(entries),count)
                self.assertFalse(any("pulled pork" in i["raw"] for i in entries))

    def test_observed_step_gaps(self):
        cases = {
            "01_Arroces/arroz_chaufa.md":7,
            "01_Arroces/arroz_frito_gambas.md":6,
            "01_Arroces/arroz_frito_pollo.md":7,
            "05_Carnes/ternera_salsa_ostras.md":9,
            "05_Carnes/pollo_salteado_con_verduras.md":6,
            "05_Carnes/ropa_vieja_base_y_pulled_pork.md":6,
            "06_Pescados_y_Mariscos/boquerones_en_vinagre.md":6,
            "08_Postres/brazo_de_gitano_de_chocolate_y_galletas.md":6,
            "05_Carnes/magret_de_pato_estilo_sichuan.md":5,
            "09_Bebidas/horchata_casera_de_chufa.md":6,
            "09_Bebidas/granizado_de_limon_casero.md":6,
            "09_Bebidas/batido_de_fresas_y_yogur.md":6,
            "09_Bebidas/cafe_bombon_con_leche_condensada.md":5,
            "09_Bebidas/te_verde_frio_con_melocoton.md":6,
            "09_Bebidas/agua_fresca_de_sandia_y_lima.md":6,
        }
        for path,count in cases.items():
            with self.subTest(path=path):
                result,_=extract_content(snapshot_bytes(ROOT_DIR,COMMIT,path))
                self.assertEqual(len(result["steps"]),count)

    def test_structural_group_and_separator(self):
        raw = """# Ingredientes estructurales
## Proteína
400 g de ternera
---
## Verduras
- 1 cebolla
Opcionalmente:
- bambú
---
## Salsa
- 2 cucharadas de soja
# Preparación
## 1. Mezclar
Mezclar todo.
# Referencias
## Ingredientes
- ajo
""".encode()
        entries,_=extract_ingredients(raw,"fixture.md",{})
        self.assertEqual(len(entries),4)
        self.assertEqual(entries[2]["optionality"],"optional")
        self.assertEqual(entries[3]["optionality"],"required")
