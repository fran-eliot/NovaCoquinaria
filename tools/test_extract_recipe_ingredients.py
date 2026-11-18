import json
import unittest
from common import ROOT_DIR
from extract_recipe_metadata import snapshot_bytes, read_metadata
from extract_recipe_ingredients import quantity, extract_ingredients


class IngredientTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads((ROOT_DIR / "tools/fixtures/recipe_contract_cases.json").read_text(encoding="utf-8"))
        cls.commit = cls.fixture["source_commit"]

    def test_synthetic_quantities(self):
        for case in self.fixture["synthetic_quantities"]:
            with self.subTest(raw=case["raw"]):
                q, name = quantity(case["raw"])
                for key in ("status","min","max","unit"):
                    if key in case:
                        self.assertEqual(q[key], case[key])
                self.assertEqual(q["raw"],case["raw"])
                if case.get("preserve_alternative"):
                    self.assertIn("pechuga o contramuslo",name)

    def test_real_ingredient_cases(self):
        ingredient_path = "11_Despensa/13_Bases_Culinarias/leche_de_coco.md"
        metadata, _ = read_metadata(snapshot_bytes(ROOT_DIR,self.commit,ingredient_path),ingredient_path)
        lookup = {ingredient_path:metadata["id"]}
        for case in self.fixture["recipes"]:
            with self.subTest(id=case["id"]):
                raw = snapshot_bytes(ROOT_DIR,self.commit,case["path"])
                entries, _ = extract_ingredients(raw,case["path"],lookup)
                self.assertEqual(len(entries),case["expected"]["ingredient_count"])
                for expected in case["ingredients"]:
                    matches = [e for e in entries if expected["contains"] in e["raw"]]
                    if len(matches) > 1:
                        matches = [e for e in matches if e["raw"].strip("* ").rstrip(";").lower() == expected["contains"].lower()]
                    self.assertEqual(len(matches),1,expected["contains"])
                    for key in ("status","min","max","unit","resolution","optionality"):
                        if key in expected:
                            actual = matches[0]["quantity"] if key in ("status","min","max","unit") else matches[0]
                            self.assertEqual(actual[key],expected[key],expected["contains"])
                for excluded in case.get("excluded_ingredient_text",[]):
                    self.assertFalse(any(excluded in e["raw"] for e in entries))

    def test_sections_and_optional(self):
        raw = b"---\ntipo: receta\n---\n# Ingredientes\n## Opcional\n- 2 cucharadas de aceite (opcional)\n---\n# Variantes\n- 5 g de sal\n"
        entries,_ = extract_ingredients(raw,"x.md",{})
        self.assertEqual(len(entries),1)
        self.assertEqual(entries[0]["optionality"],"optional")
        self.assertEqual(entries[0]["source_location"]["start_line"],6)
