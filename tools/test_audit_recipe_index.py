import hashlib
import json
import unittest

from audit_recipe_index import audit
from build_recipe_index import build_index, serialize
from test_build_recipe_index import record, projection, encode, ingredient, candidate


class IndexAuditTests(unittest.TestCase):
    def setUp(self):
        self.source = b"fixture source"
        item = record()
        item["source"]["sha256"] = hashlib.sha256(self.source).hexdigest()
        item["ingredients"] = [
            ingredient("café", "explicit", "ING-001"),
            ingredient("café", matches=[candidate("ING-001")]),
        ]
        self.raw = encode(projection(item))
        self.index = build_index(self.raw)

    def reader(self, commit, path):
        return self.source

    def test_consistency_and_samples(self):
        report = audit(self.raw, serialize(self.index).encode(), self.reader)
        self.assertEqual(report["verified_source_hashes"], 1)
        self.assertEqual(report["inventory"]["ingredients"]["occurrences"], 2)
        self.assertEqual(report["samples"]["by_candidate_id"][0]["position"], 1)

    def test_reject_wrong_source(self):
        with self.assertRaisesRegex(ValueError, "Huella de fuente"):
            audit(self.raw, serialize(self.index).encode(), lambda *_: b"changed")

    def test_reject_invalid_posting(self):
        self.index["ingredients"]["by_explicit_id"]["ING-001"][0]["position"] = 1
        with self.assertRaisesRegex(ValueError, "Referencias de ingredientes"):
            audit(self.raw, serialize(self.index).encode(), self.reader)

    def test_reject_wrong_inventory(self):
        self.index["inventory"]["recipes"] = 2
        with self.assertRaisesRegex(ValueError, "Recuentos"):
            audit(self.raw, serialize(self.index).encode(), self.reader)

    def test_reject_wrong_projection_digest(self):
        with self.assertRaisesRegex(ValueError, "Procedencia"):
            audit(self.raw + b" ", serialize(self.index).encode(), self.reader)


if __name__ == "__main__":
    unittest.main()
