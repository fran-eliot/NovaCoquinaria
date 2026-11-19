import unittest

from experiment_retrieval_text import tokens, contains_terms, retrieve, summarize


class RetrievalTextTests(unittest.TestCase):
    def test_boundaries_and_contiguity(self):
        for name, query, expected in (
            ("ajo negro", "ajo", True), ("ajonjolí", "ajo", False),
            ("salsa de soja", "sal", False), ("harina fina de maíz", "harina de maíz", False),
            ("salsa de soja clara;", "salsa de soja", True),
            ("huevos L", "huevo", False), ("aceite de cacahuete o girasol", "girasol", True),
        ):
            with self.subTest(name=name, query=query):
                self.assertEqual(contains_terms(tokens(name), tokens(query)), expected)

    def test_diacritics_distinct_modes(self):
        self.assertEqual(tokens("CAFE\u0301"), ("café",))
        self.assertFalse(contains_terms(tokens("café fuerte"), tokens("cafe")))
        self.assertTrue(contains_terms(tokens("café fuerte", True), tokens("cafe", True)))

    def test_modes_and_deduplication(self):
        index = {"ingredients": {"by_text": {
            "ajo": [{"recipe_id": "REC-1", "position": 0}],
            "ajo picado": [{"recipe_id": "REC-1", "position": 1},
                           {"recipe_id": "REC-2", "position": 0}],
            "ajonjolí": [{"recipe_id": "REC-3", "position": 0}],
        }}}
        self.assertEqual(retrieve(index, "ajo", "exact"), {("REC-1", 0)})
        self.assertEqual(retrieve(index, "ajo", "terms"),
                         {("REC-1", 0), ("REC-1", 1), ("REC-2", 0)})

    def test_invalid_queries(self):
        for query, mode in (("", "exact"), ("---", "terms"), ("ajo", "fuzzy")):
            with self.subTest(query=query, mode=mode), self.assertRaises(ValueError):
                retrieve({}, query, mode)


if __name__ == "__main__":
    unittest.main()
