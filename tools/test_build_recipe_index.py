import hashlib
import json
import unittest

from build_recipe_index import build_index, serialize, text_key

COMMIT = "a" * 40


def ingredient(name, resolution="unresolved", ingredient_id=None, matches=None,
               option="required", line=10):
    matches = [] if matches is None else matches
    n = len({match["ingredient_id"] for match in matches})
    return {"raw": name or "texto ambiguo", "name": name, "group": None,
            "resolution": resolution, "ingredient_id": ingredient_id,
            "identity_candidates": matches,
            "candidate_status": "multiple" if n > 1 else "single" if n else "none",
            "optionality": option, "source_location": {"start_line": line, "end_line": line},
            "quantity": {"status": "missing", "min": None, "max": None}}


def candidate(identity, method="title_exact"):
    return {"ingredient_id": identity, "path": "11_Despensa/a.md",
            "method": method, "matched_label": "café"}


def record(identity="REC-0017", path="05_Carnes/a.md"):
    return {
        "contract_version": "0.1.0", "id": identity,
        "source": {"commit": COMMIT, "path": path, "sha256": "b" * 64},
        "metadata": {"id": identity, "tipo": "receta", "titulo": "Café con Leche",
                     "version": "1.0", "estado": "estable", "extra": ["valor"]},
        "title": "Café con Leche", "physical_module": path.split("/")[0],
        "category": None, "evidence": {"status": "unknown", "scope": None},
        "ingredients": [ingredient("café"), ingredient("leche", line=11)],
        "steps": [], "sections": [], "references": [], "durations": [],
        "diagnostics": [{"code": "example"}], "yield": None,
    }


def projection(*records):
    return {"contract_version": "0.1.0", "extractor_version": "0.4.6",
            "stage": "recipe_projection_preview", "source_commit": COMMIT,
            "inventory": {"recipe_documents": len(records)}, "recipes": list(records)}


def encode(value):
    return json.dumps(value, ensure_ascii=False).encode("utf-8")


class RecipeIndexTests(unittest.TestCase):
    def test_literal_identity_and_path(self):
        a = record()
        b = record("REC-17", "05_Carnes/b.md")
        index = build_index(encode(projection(b, a)))
        self.assertEqual(set(index["records"]), {"REC-0017", "REC-17"})
        self.assertEqual(index["by_path"][a["source"]["path"]], a["id"])
        self.assertEqual(index["by_title"]["café con leche"], ["REC-0017", "REC-17"])
        self.assertEqual(index["inventory"]["recipes"], 2)

    def test_preservation_and_facets(self):
        a = record()
        index = build_index(encode(projection(a)))
        self.assertEqual(index["records"][a["id"]], a)
        self.assertEqual(index["facets"]["category"], {})
        self.assertEqual(index["facets"]["document_status"], {"estable": [a["id"]]})
        self.assertEqual(index["facets"]["evidence_status"], {"unknown": [a["id"]]})
        self.assertEqual(index["facets"]["physical_module"], {"05_Carnes": [a["id"]]})

    def test_unicode_text_key(self):
        self.assertEqual(text_key("  CAFE\u0301   CON Leche "), "café con leche")
        self.assertNotEqual(text_key("café"), text_key("cafe"))
        self.assertNotEqual(text_key("café!"), text_key("café"))

    def test_determinism_and_input_digest(self):
        raw = encode(projection(record()))
        first = build_index(raw)
        self.assertEqual(serialize(first), serialize(build_index(raw)))
        self.assertEqual(first["projection_sha256"], hashlib.sha256(raw).hexdigest())
        self.assertNotEqual(first["projection_sha256"],
                            build_index(raw + b"\n")["projection_sha256"])

    def test_empty_projection(self):
        index = build_index(encode(projection()))
        self.assertEqual(index["records"], {})
        self.assertEqual(index["inventory"]["recipes"], 0)

    def test_duplicate_identity_and_path(self):
        cases = [(record(), record(path="05_Carnes/b.md")),
                 (record(), record("REC-17"))]
        for a, b in cases:
            with self.subTest(a=a["id"], b=b["id"]), self.assertRaises(ValueError):
                build_index(encode(projection(a, b)))

    def test_invalid_provenance(self):
        for key, value in (("commit", "c" * 40), ("sha256", "bad"),
                           ("path", "../a.md"), ("path", "/a.md"),
                           ("path", "05_Carnes//a.md"), ("path", "a.txt")):
            a = record()
            a["source"][key] = value
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                build_index(encode(projection(a)))

    def test_invalid_envelope(self):
        for key, value in (("stage", "other"), ("source_commit", "bad"),
                           ("extractor_version", "0.5.0"),
                           ("inventory", {"recipe_documents": 2})):
            data = projection(record())
            data[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                build_index(encode(data))

    def test_invalid_fields(self):
        for key, value in (("title", ""), ("ingredients", None),
                           ("evidence", {"status": "cooked"}), ("category", [])):
            a = record()
            a[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                build_index(encode(projection(a)))

    def test_reject_duplicate_json_keys_and_nonfinite_literal(self):
        for raw in (b'{"stage": "one", "stage": "two"}', b'{"x": NaN}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                build_index(raw)


    def test_ingredient_modes_and_occurrences(self):
        a = record()
        a["ingredients"] = [
            ingredient("Café", "explicit", "ING-001", line=10),
            ingredient("café", matches=[candidate("ING-001"),
                       candidate("ING-001", "reviewed_alias")], option="optional", line=11),
            ingredient("café o té", matches=[candidate("ING-001"), candidate("ING-002")],
                       option="unknown", line=12),
            ingredient(None, "ambiguous", line=13),
            ingredient("cafe", line=14),
        ]
        index = build_index(encode(projection(a)))
        modes = index["ingredients"]
        ref = lambda pos: {"recipe_id": a["id"], "position": pos}
        self.assertEqual(modes["by_text"]["café"], [ref(0), ref(1)])
        self.assertEqual(modes["by_text"]["café o té"], [ref(2)])
        self.assertEqual(modes["by_text"]["cafe"], [ref(4)])
        self.assertNotIn("té", modes["by_text"])
        self.assertEqual(modes["by_explicit_id"], {"ING-001": [ref(0)]})
        self.assertEqual(modes["by_candidate_id"]["ING-001"], [
            {**ref(1), "methods": ["reviewed_alias", "title_exact"]},
            {**ref(2), "methods": ["title_exact"]}])
        self.assertEqual(modes["by_candidate_id"]["ING-002"],
                         [{**ref(2), "methods": ["title_exact"]}])
        self.assertEqual(index["records"][a["id"]]["ingredients"], a["ingredients"])
        counts = index["inventory"]["ingredients"]
        self.assertEqual([counts[k] for k in ("occurrences", "text_occurrences",
                         "explicit_occurrences", "candidate_occurrences",
                         "candidate_postings")], [5, 4, 1, 2, 3])

    def test_ingredient_order_across_recipes(self):
        a, b = record(), record("REC-17", "05_Carnes/b.md")
        index = build_index(encode(projection(b, a)))
        self.assertEqual(index["ingredients"]["by_text"]["café"],
                         [{"recipe_id": a["id"], "position": 0},
                          {"recipe_id": b["id"], "position": 0}])

    def test_invalid_ingredient_fields(self):
        for key, value in (("optionality", "inferred"), ("resolution", "explicit"),
                           ("ingredient_id", "ING-001"), ("candidate_status", "single"),
                           ("identity_candidates", [None]), ("source_location", None),
                           ("name", 1), ("raw", "")):
            a = record()
            a["ingredients"][0][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                build_index(encode(projection(a)))

    def test_empty_ingredient_index(self):
        a = record()
        a["ingredients"] = []
        index = build_index(encode(projection(a)))
        self.assertEqual(index["ingredients"],
                         {"by_text": {}, "by_explicit_id": {}, "by_candidate_id": {}})
        self.assertEqual(index["inventory"]["ingredients"]["occurrences"], 0)


if __name__ == "__main__":
    unittest.main()
