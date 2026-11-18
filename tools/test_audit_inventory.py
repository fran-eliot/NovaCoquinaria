import unittest

from audit_inventory import build_inventory


class InventoryTests(unittest.TestCase):
    def test_counts_and_exclusions(self):
        result = build_inventory([
            "README.md", "01_Arroces/README.md", "01_Arroces/arroz.md",
            "07_Cocina_Asiatica/receta.md", "09_Bebidas/bebida.md",
            "10_Horno/masa.md", "11_Despensa/README.md",
            "11_Despensa/BACKLOG.md", "11_Despensa/ingrediente.md",
            "00_Bases/03_Tecnicas/README.md",
            "00_Bases/03_Tecnicas/tecnica.md", "tools/common.py",
        ], "test-commit")
        self.assertEqual(result["markdown_files"], 11)
        self.assertEqual(result["recipe_paths"], 4)
        self.assertEqual(len(result["recipe_paths_by_module"]), 10)
        self.assertEqual(result["recipe_paths_by_module"]["02_Pastas"], 0)
        self.assertEqual(result["ingredient_paths"], 1)
        self.assertEqual(result["technique_paths"], 1)
        self.assertEqual(result["commit"], "test-commit")


if __name__ == "__main__":
    unittest.main()
