"""Pruebas de proyección y de conservación del contexto."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from build_recipe_assistant import build_assistant
from build_recipe_index import serialize
from extract_recipe_content import extract_content
from extract_recipe_details import general_fields
from extract_recipe_ingredients import extract_ingredients


class AssistantDataTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.docs = Path(self.tmp.name)
        self.path = "10_Horno/talo ñ.md"
        self.commit = "a" * 40
        self.raw = """---
id: REC-01
tipo: receta
titulo: Talo
version: 1.0
---
# Talo
## Información general
| Raciones | 6 unidades |
| Tiempo orientativo | 35–45 min |
## Ingredientes
- 220–260 ml de agua
- 1/2 cucharadita de sal (opcional)
**Advertencia:** conservar el texto.
## Mise en place
Preparar el cuenco.
## Elaboración
1. Mezclar.
Párrafo no numerado importante.
2. Cocinar.
## Conservación
Conservar refrigerado.
""".encode()
        file = self.docs / self.path
        file.parent.mkdir()
        file.write_bytes(self.raw)
        content, diagnostics = extract_content(self.raw)
        front = self.raw.decode().split("---", 2)[1].strip("\n")
        details, more = general_fields(content["sections"], front)
        ingredients, ing_diagnostics = extract_ingredients(self.raw, self.path, {})
        self.record = {"id": "REC-01", "title": "Talo", "physical_module": "10_Horno",
                       "source": {"commit": self.commit, "path": self.path,
                                  "sha256": hashlib.sha256(self.raw).hexdigest(),
                                  "frontmatter_raw": front},
                       **content, **details, "ingredients": ingredients, "references": [],
                       "diagnostics": diagnostics + more + ing_diagnostics}
        self.index = {"index_version": "0.2.0", "stage": "recipe_index_ingredients_preview",
                      "source_commit": self.commit, "inventory": {"recipes": 1},
                      "records": {"REC-01": self.record}, "by_path": {self.path: "REC-01"}}

    def build(self):
        return build_assistant(serialize(self.index).encode(), self.docs, lambda c, p: self.raw)

    def test_projection(self):
        before = copy.deepcopy(self.index)
        files = self.build()
        self.assertEqual(files, self.build())
        self.assertEqual(before, self.index)
        manifest = json.loads(files["manifest.json"])
        entry = manifest["recipes"]["REC-01"]
        self.assertEqual(entry["file"], hashlib.sha256(b"REC-01").hexdigest() + ".json")
        data = files[entry["file"]]
        self.assertEqual(entry["sha256"], hashlib.sha256(data).hexdigest())
        record = json.loads(data)
        self.assertEqual(record["href"], "10_Horno/talo%20%C3%B1.html")
        self.assertEqual(record["ingredients"][0]["quantity"]["status"], "range")
        self.assertEqual(record["ingredients"][1]["quantity"]["min"], "1/2")
        self.assertEqual(record["ingredients"][1]["optionality"], "optional")
        self.assertEqual(record["steps"][1]["order"], 2)
        self.assertIn("Párrafo no numerado importante.", record["context"]["text"])
        self.assertIn("Advertencia", record["context"]["text"])
        self.assertIn("Conservar refrigerado.", record["context"]["text"])
        self.assertEqual(record["mise_en_place"][0]["heading"], "Mise en place")

    def test_bad_hash(self):
        self.record["source"]["sha256"] = "b" * 64
        with self.assertRaises(ValueError):
            self.build()

    def test_bad_ingredient(self):
        self.record["ingredients"][0]["raw"] = "inventado"
        with self.assertRaises(ValueError):
            self.build()

    def test_bad_step(self):
        self.record["steps"][0]["text"] = "inventado"
        with self.assertRaises(ValueError):
            self.build()

    def test_bad_inventory(self):
        self.index["inventory"]["recipes"] = 2
        with self.assertRaises(ValueError):
            self.build()

    def test_bad_path(self):
        self.record["source"]["path"] = "10_Horno/../talo.md"
        with self.assertRaises(ValueError):
            self.build()

    def test_missing_published_source(self):
        (self.docs / self.path).unlink()
        with self.assertRaises(ValueError):
            self.build()
