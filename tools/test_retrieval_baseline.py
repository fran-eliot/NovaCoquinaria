"""Contraste de las muestras documentales, sin implementar reglas experimentales."""
import json
import unittest

from common import ROOT_DIR
from extract_recipe_metadata import build_projection
from build_recipe_index import build_index, text_key
from extract_recipe_metadata import serialize


class RetrievalBaselineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads((ROOT_DIR / "tools/fixtures/retrieval_baseline_cases.json")
                                 .read_text(encoding="utf-8"))
        cls.index = build_index(serialize(build_projection(
            ROOT_DIR, cls.fixture["source_commit"])).encode("utf-8"))

    def test_pinned_sample_occurrences_and_exact_baseline(self):
        self.assertEqual(self.index["source_commit"], self.fixture["source_commit"])
        self.assertEqual(self.index["extractor_version"], self.fixture["extractor_version"])
        self.assertEqual(self.index["index_version"], self.fixture["index_version"])
        for case in self.fixture["cases"]:
            with self.subTest(case=case["id"]):
                record = self.index["records"][case["recipe_id"]]
                entry = record["ingredients"][case["position"]]
                self.assertEqual(record["source"]["path"], case["path"])
                self.assertEqual(entry["source_location"]["start_line"], case["line"])
                self.assertEqual(entry["name"], case["name"])
                posting = {"recipe_id": case["recipe_id"], "position": case["position"]}
                found = posting in self.index["ingredients"]["by_text"].get(
                    text_key(case["query"]), [])
                self.assertEqual(found, case["expected"]["exact"])

    def test_baseline_inventory(self):
        counts = self.index["inventory"]
        self.assertEqual(counts["recipes"], 590)
        self.assertEqual(counts["ingredients"]["occurrences"], 5047)
        self.assertEqual(counts["ingredients"]["text_occurrences"], 5046)
        self.assertEqual(counts["ingredients"]["text_keys"], 2588)
        self.assertEqual(counts["ingredients"]["explicit_occurrences"], 36)
        self.assertEqual(counts["ingredients"]["candidate_occurrences"], 1044)


if __name__ == "__main__":
    unittest.main()
