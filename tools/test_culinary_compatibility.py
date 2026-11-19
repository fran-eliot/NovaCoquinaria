"""Synthetic cases for the isolated compatibility experiment."""
import unittest
from copy import deepcopy
from experiment_culinary_compatibility import evaluate, contrast
from recipe_ingredient_index import build_ingredient_indexes
from build_recipe_index import text_key

COMMIT = "a" * 40

def entry(iid="ING-1", option="required", candidates=None, name="ajo"):
    matches = candidates or []
    return {"raw": name, "name": name, "quantity": {"state": "missing"},
            "source_location": {"start_line": 1, "end_line": 1},
            "optionality": option, "resolution": "explicit" if iid else "unresolved",
            "ingredient_id": iid, "identity_candidates": matches,
            "candidate_status": "single" if matches else "none"}

def index(entries):
    records = {"REC-1": {"id": "REC-1", "title": "Synthetic",
                         "source": {"commit": COMMIT, "sha256": "b"*64, "path": "test.md"},
                         "ingredients": entries}}
    postings, _ = build_ingredient_indexes(records, text_key)
    return {"index_version": "0.2.0", "stage": "recipe_index_ingredients_preview",
            "source_commit": COMMIT, "projection_sha256": "c"*64,
            "records": records, "ingredients": postings}

def declaration(**kw):
    return {"source_commit": COMMIT, **kw}

class CompatibilityTests(unittest.TestCase):
    def test_positive_and_optional_missing(self):
        idx = index([entry(), entry("ING-2", "optional")])
        d = declaration(mode="closed", present_ids=["ING-1"],
                        atomic=[["REC-1", 0, "ING-1"], ["REC-1", 1, "ING-2"]],
                        presentation=[["REC-1", 0, "ING-1"]])
        runs, _ = contrast(idx, d, None)
        r = runs[0]["results"][0]
        self.assertEqual(r["classification"], "required_presence_confirmed")
        self.assertEqual(r["matrix"]["optional"]["unavailable"], 1)

    def test_unknown_option_blocks(self):
        idx = index([entry(), entry(option="unknown")])
        d = declaration(present_ids=["ING-1"], atomic=[["REC-1", 0, "ING-1"]],
                        presentation=[["REC-1", 0, "ING-1"]])
        self.assertEqual(evaluate(idx, d)["results"][0]["classification"], "indeterminate")

    def test_duplicate_occurrences_and_atomicity(self):
        idx = index([entry(), entry()])
        d = declaration(mode="closed", atomic=[["REC-1", 0, "ING-1"]])
        r = evaluate(idx, d)["results"][0]
        self.assertEqual([e["availability"] for e in r["occurrences"]], ["unavailable", "unknown"])
        self.assertEqual(r["classification"], "required_missing")

    def test_open_and_presentation(self):
        idx = index([entry()])
        d = declaration(atomic=[["REC-1", 0, "ING-1"]])
        self.assertEqual(evaluate(idx, d)["results"][0]["occurrences"][0]["reason"], "open_unspecified")
        d["present_ids"] = ["ING-1"]
        self.assertEqual(evaluate(idx, d)["results"][0]["occurrences"][0]["reason"], "presentation_unknown")

    def test_hints_never_promote(self):
        candidate = {"ingredient_id": "ING-1", "path": "ingredient.md",
                     "method": "title_exact", "matched_label": "ajo"}
        idx = index([entry(None, candidates=[candidate])])
        runs, _ = contrast(idx, {"present_ids": ["ING-1"], "present_labels": ["AJO"]}, None)
        self.assertEqual([r["results"][0]["occurrences"][0]["availability"] for r in runs], ["unknown"]*3)
        self.assertFalse(runs[0]["results"][0]["occurrences"][0]["hints"])
        self.assertTrue(runs[1]["results"][0]["occurrences"][0]["hints"])
        self.assertTrue(runs[2]["results"][0]["occurrences"][0]["hints"])

    def test_empty_and_optional_only(self):
        for entries in ([], [entry(option="optional")]):
            idx = index(entries)
            self.assertEqual(evaluate(idx, {})["results"][0]["classification"], "indeterminate")
            self.assertEqual(evaluate(idx, {}, [])["results"], [])

    def test_invalid_declarations(self):
        idx = index([entry()])
        cases = [{"present_ids": ["ING-1"], "absent_ids": ["ING-1"]},
                 {"present_ids": ["ING-1", "ING-1"]}, {"present_ids": ["ING-9"]},
                 {"mode": "partial"}, {"atomic": [["REC-1", 0, "ING-1"]]},
                 declaration(atomic=[["REC-1", True, "ING-1"]]),
                 declaration(presentation=[["REC-1", 0, "ING-1"]]),
                 declaration(atomic=[["REC-1", 0, "ING-1"]]*2),
                 {"present_labels": ["ajo", "AJO"]}]
        for d in cases:
            with self.subTest(d=d), self.assertRaises(ValueError):
                evaluate(idx, d)
        with self.assertRaises(ValueError):
            evaluate(idx, {}, ["REC-9"])

    def test_preserve_input(self):
        idx = index([entry()])
        original = deepcopy(idx)
        evaluate(idx, {})
        self.assertEqual(idx, original)
