import unittest

from audit_editorial_signals import build_report, scan_one, sections


class EditorialSignalsTests(unittest.TestCase):
    def test_only_audited_sections_and_line_locations(self):
        recipe = "# Receta\n\n## Ingredientes\n- arroz cocido\n\n## Diagnóstico\n| Salsa demasiado espesa | Reducción excesiva o demasiado almidón | Diluir |\n\n## Registro de prueba\nSalsa demasiado espesa | Reducción excesiva o demasiado almidón\n"
        items = scan_one("09_Bebidas/prueba.md", recipe)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["line"], 7)
        self.assertEqual(items[0]["section"], "Diagnóstico")
        self.assertEqual(items[0]["signal"], "E03_GENERIC_DIAGNOSTICS")

    def test_accents_and_absent_matches(self):
        text = "## Conservación\nMantener el helado congelado hasta el montaje.\n"
        self.assertEqual(scan_one("09_Bebidas/x.md", text)[0]["signal"], "E02_OTHER_PREPARATIONS")
        self.assertEqual(scan_one("09_Bebidas/y.md", "## Conservación\nRefrigerar el yogur."), [])

    def test_report_is_deterministic_and_preserves_counter_denominators(self):
        docs = {
            "09_Bebidas/b.md": "## Diagnóstico\n| Plato | Soja, miso u otros fermentados concentrados | Probar |",
            "05_Carnes/a.md": "## Diagnóstico\n| Plato | Soja, miso u otros fermentados concentrados | Probar |",
            "08_Postres/c.md": "## Diagnóstico\n| Crema | Punto de cocción | Comprobar |",
        }
        first = build_report(docs, "abc")
        self.assertEqual(first, build_report(dict(reversed(list(docs.items()))), "abc"))
        self.assertEqual(first["recipes_scanned"], 3)
        self.assertEqual(first["flagged_recipes"], 2)
        self.assertEqual(first["occurrences"], 2)
        self.assertEqual(first["source_commit"], "abc")
        self.assertIn("not confirmed defects", first["scope"])

    def test_heading_section_boundaries(self):
        text = "## Puntos críticos\nUna frase.\n### Subdetalle\nOtra frase.\n## Elaboración\nNo auditar."
        self.assertEqual([x[2] for x in sections(text)], ["Una frase.", "### Subdetalle", "Otra frase."])


if __name__ == "__main__":
    unittest.main()
