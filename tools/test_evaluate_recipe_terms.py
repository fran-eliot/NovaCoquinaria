import unittest
from unittest.mock import patch

from build_recipe_index import build_index
from test_build_recipe_index import record, projection, encode, ingredient
from evaluate_recipe_terms import scan, observed_refs


class EvaluateTermsTests(unittest.TestCase):
    def setUp(self):
        a = record()
        a["ingredients"] = [ingredient("ajo"), ingredient("ajo picado"),
                            ingredient("ajonjolí"), ingredient("café fuerte")]
        self.index = build_index(encode(projection(a)))

    def test_scan_independent_of_postings(self):
        expected = {("REC-0017", 0), ("REC-0017", 1)}
        self.assertEqual(scan(self.index, "ajo", "terms"), expected)
        self.assertEqual(observed_refs(self.index, "ajo", "terms"), expected)
        self.index["ingredients"]["by_text"].clear()
        self.assertEqual(scan(self.index, "ajo", "terms"), expected)
        self.assertEqual(observed_refs(self.index, "ajo", "terms"), set())

    def test_exact_and_unicode(self):
        self.assertEqual(scan(self.index, "ajo", "text"), {("REC-0017", 0)})
        self.assertEqual(scan(self.index, "cafe", "terms"), set())
        self.assertEqual(scan(self.index, "CAFE\u0301", "terms"), {("REC-0017", 3)})

    def test_invalid_provenance_rejected(self):
        with patch("evaluate_recipe_terms.query", return_value={
                "results": [], "count": 0, "source_commit": "wrong",
                "projection_sha256": self.index["projection_sha256"]}):
            with self.assertRaises(ValueError):
                observed_refs(self.index, "ajo", "terms")


if __name__ == "__main__":
    unittest.main()
