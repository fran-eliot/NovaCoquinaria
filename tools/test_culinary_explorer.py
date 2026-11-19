import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from build_culinary_explorer import build_explorer
from build_recipe_index import serialize


class ExplorerDataTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.docs = Path(self.tmp.name)
        self.path = "02_Pastas/receta ñ.md"
        source = self.docs / self.path
        source.parent.mkdir()
        source.write_text("# Receta", encoding="utf-8")
        self.index = {
            "index_version": "0.2.0", "stage": "recipe_index_ingredients_preview",
            "source_commit": "a" * 40, "inventory": {"recipes": 1},
            "by_path": {self.path: "REC-01"},
            "ingredients": {"by_text": {"ajo negro": [{"recipe_id": "REC-01", "position": 0}]}},
            "records": {"REC-01": {
                "id": "REC-01", "title": "Pasta Ñ", "physical_module": "02_Pastas",
                "source": {"path": self.path, "commit": "a" * 40, "sha256": "b" * 64},
                "evidence": {"status": "unknown"},
                "ingredients": [{"name": "Ajo negro", "raw": "2 dientes de ajo negro",
                                 "optionality": "optional",
                                 "source_location": {"start_line": 8, "end_line": 8}},
                                {"name": None, "raw": "al gusto", "optionality": "unknown",
                                 "source_location": {"start_line": 9, "end_line": 9}}]}}
        }

    def build(self):
        return build_explorer(serialize(self.index).encode(), self.docs)

    def test_projection(self):
        before = copy.deepcopy(self.index)
        result = self.build()
        self.assertEqual(result, self.build())
        self.assertEqual(before, self.index)
        self.assertEqual(result["index_sha256"], hashlib.sha256(serialize(self.index).encode()).hexdigest())
        record = result["recipes"][0]
        self.assertEqual(record["href"], "02_Pastas/receta%20%C3%B1.html")
        self.assertEqual(record["title_tokens"], ["pasta", "ñ"])
        self.assertEqual(record["ingredients"][0]["tokens"], ["ajo", "negro"])
        self.assertEqual(record["ingredients"][1]["tokens"], [])
        self.assertEqual(record["evidence"]["status"], "unknown")

    def test_missing_source(self):
        (self.docs / self.path).unlink()
        with self.assertRaises(ValueError):
            self.build()

    def test_inconsistent_postings(self):
        self.index["ingredients"]["by_text"] = {}
        with self.assertRaises(ValueError):
            self.build()

    def test_invalid_route(self):
        self.index["records"]["REC-01"]["source"]["path"] = "02_Pastas/../escape.md"
        with self.assertRaises(ValueError):
            self.build()

    def test_inventory(self):
        self.index["inventory"]["recipes"] = 2
        with self.assertRaises(ValueError):
            self.build()

    def test_invalid_evidence(self):
        self.index["records"]["REC-01"]["evidence"]["status"] = "other"
        with self.assertRaises(ValueError):
            self.build()
