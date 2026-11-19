import copy
import unittest

from build_recipe_index import build_index
from query_recipe_index import query
from test_build_recipe_index import record, projection, encode, ingredient, candidate


class QueryTests(unittest.TestCase):
    def setUp(self):
        a = record()
        a["ingredients"] = [
            ingredient("Café", "explicit", "ING-001"),
            ingredient("café", matches=[candidate("ING-001")], option="optional"),
            ingredient("café", option="optional"),
            ingredient("leche o nata"),
        ]
        b = record("REC-17", "08_Postres/b.md")
        b["evidence"]["status"] = "prepared"
        b["ingredients"] = [ingredient("café", matches=[candidate("ING-001")])]
        self.index = build_index(encode(projection(b, a)))

    def run_query(self, filters=None, ingredients=None):
        return query(self.index, filters, ingredients)

    def test_literal_id_and_path(self):
        self.assertEqual(self.run_query({"id": "REC-17"})["count"], 1)
        self.assertEqual(self.run_query({"id": "REC-0017",
                                         "path": "08_Postres/b.md"})["count"], 0)
        self.assertEqual(self.run_query({"id": "REC-00017"})["count"], 0)

    def test_normalized_title_and_order(self):
        result = self.run_query({"title": " CAFE\u0301 con leche "})
        self.assertEqual([r["id"] for r in result["results"]], ["REC-0017", "REC-17"])
        self.assertEqual(self.run_query({"title": "cafe con leche"})["count"], 0)

    def test_ingredient_modes_are_separate(self):
        for mode, value, expected in (("text", "CAFÉ", 2),
                                       ("explicit", "ING-001", 1),
                                       ("candidate", "ING-001", 2),
                                       ("explicit", "ing-001", 0),
                                       ("text", "leche", 0)):
            with self.subTest(mode=mode, value=value):
                self.assertEqual(self.run_query(ingredients=[
                    {"mode": mode, "value": value}])["count"], expected)
        result = self.run_query(ingredients=[{"mode": "candidate", "value": "ING-001"}])
        occurrence = result["results"][0]["matches"][0]["occurrences"][0]
        self.assertEqual(occurrence["position"], 1)
        self.assertIsNone(occurrence["ingredient_id"])
        self.assertEqual(occurrence["methods"], ["title_exact"])

    def test_intersection_and_optionality(self):
        result = self.run_query({"physical_module": "05_Carnes",
                                 "document_status": "estable"}, [
            {"mode": "text", "value": "café", "optionality": "optional"},
            {"mode": "explicit", "value": "ING-001"}])
        self.assertEqual(result["count"], 1)
        matches = result["results"][0]["matches"]
        self.assertEqual(len(matches), 4)
        self.assertEqual([m["position"] for m in matches[2]["occurrences"]], [1, 2])
        self.assertEqual(result["results"][0]["source"]["path"], "05_Carnes/a.md")

    def test_evidence_and_empty_results(self):
        result = self.run_query({"evidence_status": "prepared"})
        self.assertEqual(result["results"][0]["id"], "REC-17")
        self.assertEqual(self.run_query({"category": "nonexistent"})["count"], 0)

    def test_read_only_and_reproducible(self):
        before = copy.deepcopy(self.index)
        self.assertEqual(self.run_query(), self.run_query())
        self.assertEqual(self.index, before)

    def test_invalid_input_even_after_empty_intersection(self):
        for filters, ingredients in (({"bad": "x"}, []),
            ({"id": "absent"}, [{"mode": "fuzzy", "value": "café"}]),
            ({}, [{"mode": "text", "value": " "}]),
            ({}, [{"mode": "text", "value": "café", "optionality": "maybe"}]),
            ({"evidence_status": "cooked"}, [])):
            with self.subTest(filters=filters, ingredients=ingredients), self.assertRaises(ValueError):
                self.run_query(filters, ingredients)

    def test_incompatible_index(self):
        self.index["index_version"] = "0.1.0"
        with self.assertRaises(ValueError):
            self.run_query()


if __name__ == "__main__":
    unittest.main()
