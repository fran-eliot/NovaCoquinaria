import copy
import unittest

from recipe_retrieval_terms import tokens, contains_terms, term_postings


class RetrievalTermsTests(unittest.TestCase):
    def test_unicode_and_separators(self):
        self.assertEqual(tokens("  CAFE\u0301_ñora, SAL-PIMIENTA "), 
                         ("café", "ñora", "sal", "pimienta"))
        self.assertNotEqual(tokens("ñora"), tokens("nora"))
        self.assertNotEqual(tokens("cafe"), tokens("café"))

    def test_complete_contiguous_terms(self):
        for name, value, expected in (
            ("ajo, picado", "ajo", True),
            ("ajo negro", "ajo", True),
            ("ajonjolí", "ajo", False),
            ("salsa de soja", "sal", False),
            ("harina fina de maíz", "harina de maíz", False),
            ("huevos", "huevo", False),
            ("salsa-de_soja clara", "salsa de soja", True),
            ("sin sal", "sal", True),
        ):
            with self.subTest(name=name, value=value):
                self.assertEqual(contains_terms(tokens(name), tokens(value)), expected)
        self.assertFalse(contains_terms(tokens("ajo"), ()))

    def test_literal_order_deduplication_and_read_only(self):
        by_text = {
            "ajo picado": [{"recipe_id": "REC-17", "position": 2},
                           {"recipe_id": "REC-0017", "position": 3}],
            "ajo": [{"recipe_id": "REC-17", "position": 0},
                    {"recipe_id": "REC-17", "position": 2}],
            "ajonjolí": [{"recipe_id": "REC-2", "position": 0}],
        }
        before = copy.deepcopy(by_text)
        self.assertEqual(term_postings(by_text, "AJO"), [
            {"recipe_id": "REC-0017", "position": 3},
            {"recipe_id": "REC-17", "position": 0},
            {"recipe_id": "REC-17", "position": 2},
        ])
        self.assertEqual(by_text, before)
        self.assertEqual(term_postings(by_text, "limón"), [])

    def test_invalid_query(self):
        for value in (None, 42, "", " ", "---", "_"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                term_postings({}, value)


if __name__ == "__main__":
    unittest.main()
