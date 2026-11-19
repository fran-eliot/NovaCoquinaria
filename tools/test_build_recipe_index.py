import copy
import hashlib
import json
import unittest

from build_recipe_index import build_index, serialize, text_key

COMMIT = "a" * 40


def record(identity="REC-0017", path="05_Carnes/a.md"):
    return {
        "contract_version": "0.1.0", "id": identity,
        "source": {"commit": COMMIT, "path": path, "sha256": "b" * 64},
        "metadata": {"id": identity, "tipo": "receta", "titulo": "Café con Leche",
                     "version": "1.0", "estado": "estable", "extra": ["valor"]},
        "title": "Café con Leche", "physical_module": path.split("/")[0],
        "category": None, "evidence": {"status": "unknown", "scope": None},
        "ingredients": [{"raw": "café"}, {"raw": "leche"}],
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


if __name__ == "__main__":
    unittest.main()
