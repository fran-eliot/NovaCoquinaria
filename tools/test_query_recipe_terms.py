import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from build_recipe_index import build_index
from query_recipe_index import query, QUERY_VERSION
from test_build_recipe_index import record, projection, encode, ingredient, candidate


def clause(mode, value, optionality=None):
    return {"mode": mode, "value": value, "optionality": optionality}


class QueryTermsTests(unittest.TestCase):
    def setUp(self):
        a = record()
        a["ingredients"] = [
            ingredient("Ajo picado"),
            ingredient("ajo negro", option="optional"),
            ingredient("leche o nata"),
            ingredient("salsa de soja", "explicit", "ING-001"),
            ingredient("salsa de soja clara", matches=[candidate("ING-001")]),
            ingredient("sin sal"),
        ]
        b = record("REC-17", "08_Postres/b.md")
        b["ingredients"] = [ingredient("ajo"), ingredient("ajonjolí"),
                            ingredient("café fuerte"), ingredient("huevos L")]
        self.index = build_index(encode(projection(b, a)))

    def test_new_mode_is_explicit_and_ordered(self):
        result = query(self.index, ingredients=[clause("terms", " AJO ")])
        self.assertEqual(result["query_version"], "0.2.0")
        self.assertEqual([r["id"] for r in result["results"]], ["REC-0017", "REC-17"])
        self.assertEqual([r["id"] for r in query(self.index, ingredients=[
            clause("text", "ajo")])["results"]], ["REC-17"])
        reason = result["results"][0]["matches"][0]
        self.assertEqual(reason["match_scope"], "textual_mention")
        self.assertEqual(reason["value"], " AJO ")
        self.assertEqual([x["position"] for x in reason["occurrences"]], [0, 1])
        self.assertEqual(reason["occurrences"][1]["name"], "ajo negro")
        self.assertIsNone(reason["occurrences"][0]["ingredient_id"])

    def test_composition_and_provenance(self):
        result = query(self.index, {"physical_module": "05_Carnes"}, [
            clause("terms", "ajo", "optional"), clause("explicit", "ING-001"),
            clause("candidate", "ING-001"), clause("terms", "nata")])
        self.assertEqual(result["count"], 1)
        row = result["results"][0]
        self.assertEqual(row["source"]["path"], "05_Carnes/a.md")
        matches = row["matches"]
        self.assertEqual([m["position"] for m in matches[1]["occurrences"]], [1])
        self.assertEqual(matches[3]["occurrences"][0]["methods"], ["title_exact"])
        self.assertNotIn("match_scope", matches[2])
        self.assertEqual(matches[4]["occurrences"][0]["name"], "leche o nata")
        self.assertEqual(matches[4]["occurrences"][0]["source_location"],
                         self.index["records"][row["id"]]["ingredients"][2]["source_location"])

    def test_boundaries_and_diacritics(self):
        for value, count in (("sal", 1), ("salsa soja", 0), ("huevo", 0),
                             ("cafe", 0), ("CAFE\u0301", 1), ("ajonjolí", 1)):
            with self.subTest(value=value):
                result = query(self.index, ingredients=[clause("terms", value)])
                self.assertEqual(result["count"], count)
        result = query(self.index, ingredients=[clause("terms", "sal")])
        self.assertEqual(result["results"][0]["matches"][0]["occurrences"][0]["name"], "sin sal")

    def test_invalid_even_after_empty_filter_and_read_only(self):
        before = copy.deepcopy(self.index)
        for mode, value in (("terms", "---"), ("terms", ""), ("folded", "ajo")):
            with self.subTest(mode=mode, value=value), self.assertRaises(ValueError):
                query(self.index, {"id": "absent"}, [clause(mode, value)])
        args = [clause("terms", "salsa de soja")]
        self.assertEqual(query(self.index, ingredients=args), query(self.index, ingredients=args))
        self.assertEqual(self.index, before)

    def test_cli_terms_and_optionality(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "index.json"
            path.write_text(json.dumps(self.index), encoding="utf-8")
            cmd = [sys.executable, str(Path(__file__).with_name("query_recipe_index.py")),
                   "--index", str(path)]
            completed = subprocess.run(cmd + ["--ingredient", "terms", "ajo",
                "--ingredient-with-optionality", "terms", "negro", "optional"],
                capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(completed.stdout)["count"], 1)
            invalid = subprocess.run(cmd + ["--ingredient", "terms", "_"],
                                     capture_output=True, text=True)
            self.assertNotEqual(invalid.returncode, 0)


if __name__ == "__main__":
    unittest.main()
