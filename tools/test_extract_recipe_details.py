import unittest
from extract_recipe_content import extract_sections
from extract_recipe_details import general_fields, extract_references


class DetailsTests(unittest.TestCase):
    def test_yield_and_times(self):
        raw = """## Información general
| Dato | Valor |
|---|---|
| Raciones | 3–4 como acompañamiento |
| Preparación | 15 min |
| Horneado | 45–60 min orientativos |
| Reposo | Aproximadamente 24 horas en refrigeración |
| Tiempo orientativo | 25 min más 2 h de refrigeración |
"""
        result,diag=general_fields(extract_sections(raw.encode()))
        # A bare range followed by a qualifier, under Raciones, has a declared unit.
        self.assertEqual(result["yield"]["raw"],"3–4 como acompañamiento")
        self.assertEqual(result["durations"][0]["min"],"15")
        self.assertEqual(result["durations"][1]["max"],"60")
        self.assertEqual(result["durations"][2]["unit"],"h")
        self.assertIsNone(result["durations"][3]["min"])
        self.assertEqual(diag[-1]["code"],"DURATION_UNPARSED")

    def test_explicit_yield_and_missing(self):
        result,_=general_fields(extract_sections("## Información general\n| Rendimiento | 6 unidades |\n".encode()))
        self.assertEqual(result["yield"]["unit"],"unidad")
        self.assertEqual(result["yield"]["min"],"6")
        result,_=general_fields(extract_sections(b"# Receta\n## Elaboracion\n1. Mezclar\n"))
        self.assertIsNone(result["yield"])
        self.assertEqual(result["durations"],[])

    def test_references_snapshot(self):
        raw=b"# Receta\n[Harina](../11_Despensa/harina.md#uso)\n[Indice](./README.md)\n[Otro](https://example.org)\n[Local](#pasos)\n[Perdido](../missing.md)\n~~~\n[Falso](no.md)\n~~~\n"
        path="10_Horno/talo.md"
        lookup={"11_Despensa/harina.md":"ING-0126",path:"REC-573"}
        refs,diag=extract_references(extract_sections(raw),path,lookup,set(lookup)|{"10_Horno/README.md"})
        self.assertEqual([r["status"] for r in refs],["resolved","resolved","external","local_anchor","unresolved"])
        self.assertEqual(refs[0]["target_id"],"ING-0126")
        self.assertEqual(refs[0]["source_location"]["start_line"],2)
        self.assertIsNone(refs[1]["target_id"])
        self.assertEqual(len(diag),1)
