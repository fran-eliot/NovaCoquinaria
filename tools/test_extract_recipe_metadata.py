import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from common import ROOT_DIR
from extract_recipe_metadata import (
    build_projection, project_metadata, serialize, snapshot_bytes,
)


def recipe(identity="REC-0001"):
    return (f"---\nid: {identity}\ntipo: receta\ntitulo: Ejemplo\n"
            "version: 1.0\nestado: estable\nultima_revision: 2026-11-18\n"
            "extra: [uno, dos]\n---\n\n# Ejemplo\n").encode("utf-8")


class MetadataTests(unittest.TestCase):
    def test_literal_identity_version_and_provenance(self):
        raw = recipe()
        result = project_metadata(raw, "10_Horno/ejemplo.md", "commit-fixture")
        self.assertEqual(result["id"], "REC-0001")
        self.assertEqual(result["metadata"]["version"], "1.0")
        self.assertEqual(result["metadata"]["extra"], ["uno", "dos"])
        self.assertEqual(result["source"]["sha256"], hashlib.sha256(raw).hexdigest())
        self.assertIn("version: 1.0", result["source"]["frontmatter_raw"])
        self.assertEqual(result["physical_module"], "10_Horno")
        self.assertIsNone(result["category"])
        self.assertNotIn("evidence", result)
        self.assertNotIn("ingredients", result)
        self.assertIn('"ultima_revision": "2026-11-18"', serialize(result))

    def test_excludes_nonrecipe(self):
        self.assertIsNone(project_metadata(recipe().replace(b"tipo: receta",
                                                             b"tipo: ingrediente"),
                                           "11_Despensa/ejemplo.md", "fixture"))

    def test_rejects_missing_id_and_invalid_yaml(self):
        for raw in (recipe().replace(b"id: REC-0001\n", b""),
                    b"---\nid: [\n---\n",
                    b"---\nid: REC-1\n",
                    b"---\nid: REC-1\nid: REC-2\n---\n"):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                project_metadata(raw, "01_Arroces/ejemplo.md", "fixture")

    def test_real_recipe_metadata_cases(self):
        fixtures = json.loads((ROOT_DIR / "tools/fixtures/recipe_contract_cases.json")
                              .read_text(encoding="utf-8"))
        commit = fixtures["source_commit"]
        for case in fixtures["recipes"]:
            with self.subTest(id=case["id"]):
                raw = snapshot_bytes(ROOT_DIR, commit, case["path"])
                result = project_metadata(raw, case["path"], commit)
                self.assertEqual(result["id"], case["id"])
                expected = case["expected"]
                self.assertEqual(result["metadata"]["version"], expected["version"])
                for key in ("physical_module", "category"):
                    if key in expected:
                        self.assertEqual(result[key], expected[key])
                if "document_status" in expected:
                    self.assertEqual(result["metadata"]["estado"],
                                     expected["document_status"])


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "Test")
        self.git("config", "core.autocrlf", "false")

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root)

    def write(self, path, raw):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")

    def test_snapshot_determinism_and_literal_ids(self):
        self.write("01_Arroces/a.md", recipe())
        self.write("02_Pastas/b.md", recipe("REC-1"))
        self.write("02_Pastas/README.md", recipe("REC-3"))
        self.write("11_Despensa/c.md", recipe("REC-100"))
        self.commit()
        first = build_projection(self.root)
        self.write("01_Arroces/a.md", recipe("REC-999"))
        self.write("10_Horno/untracked.md", recipe("REC-998"))
        self.assertEqual(serialize(first), serialize(build_projection(self.root)))
        self.assertEqual([r["id"] for r in first["recipes"]],
                         ["REC-0001", "REC-1", "REC-100"])
        self.assertEqual(first["inventory"]["recipe_paths"], 2)
        self.assertEqual(first["inventory"]["recipe_documents"], 3)
        self.assertEqual(first["inventory"]["recipes_outside_modules"],
                         ["11_Despensa/c.md"])
        self.assertEqual(first["recipes"][0]["diagnostics"][0]["code"],
                         "ID_FORMAT_COLLISION")

    def test_duplicate_identity_blocks_projection(self):
        self.write("01_Arroces/a.md", recipe())
        self.write("02_Pastas/b.md", recipe())
        self.commit()
        with self.assertRaisesRegex(ValueError, "duplicado"):
            build_projection(self.root)


if __name__ == "__main__":
    unittest.main()
