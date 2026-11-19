import unittest

from experiment_retrieval_identity import compile_rules, propose


class IdentityExperimentTests(unittest.TestCase):
    def setUp(self):
        self.rules = compile_rules([
            {"id": "G01", "ingredient_id": "ING-1", "labels": ["ajo picado", "ajo picados"]},
            {"id": "G02", "ingredient_id": "ING-2", "labels": ["ajo picado"]},
        ])

    def entry(self, name, resolution="unresolved", candidates=None):
        return {"name": name, "resolution": resolution,
                "identity_candidates": candidates or []}

    def test_reviewed_labels_and_conflicts(self):
        self.assertEqual(propose(self.entry("Ajo, picados;"), self.rules),
                         [{"ingredient_id": "ING-1", "rule": "G01"}])
        self.assertEqual(len(propose(self.entry("ajo picado"), self.rules)), 2)

    def test_no_promotion_or_override(self):
        for entry in (self.entry("ajo picado", "explicit"),
                      self.entry("ajo picado", "ambiguous"),
                      self.entry("ajo picado", candidates=[{"ingredient_id": "ING-3"}])):
            self.assertEqual(propose(entry, self.rules), [])

    def test_no_generalized_stripping(self):
        for name in ("ajo negro", "ajo en polvo", "ajo o cebolla",
                     "ajo picado opcional", "ajo picado y cebolla", None):
            with self.subTest(name=name):
                self.assertEqual(propose(self.entry(name), self.rules), [])


if __name__ == "__main__":
    unittest.main()
