import json
import unittest

from common import ROOT_DIR
from extract_recipe_metadata import snapshot_bytes
from extract_recipe_content import extract_content


class ContentTests(unittest.TestCase):
    def test_real_cases(self):
        cases = json.loads((ROOT_DIR / "tools/fixtures/recipe_contract_cases.json").read_text(encoding="utf-8"))
        for case in cases["recipes"]:
            with self.subTest(id=case["id"]):
                raw = snapshot_bytes(ROOT_DIR,cases["source_commit"],case["path"])
                result,_ = extract_content(raw)
                expected = case["expected"]
                if "step_count" in expected:
                    self.assertEqual(len(result["steps"]),expected["step_count"])
                evidence = result["evidence"]
                for field in ("historical_preparation","current_formula_validated"):
                    if field in expected:
                        self.assertEqual(evidence[field],expected[field])
                if "evidence_status" in expected:
                    self.assertEqual(evidence["status"],expected["evidence_status"])
                lines = raw.decode("utf-8-sig").splitlines()
                for claim in evidence["claims"]:
                    self.assertEqual(lines[claim["source_location"]["start_line"]-1],claim["text"])

    def test_numbered_headings_and_scoping(self):
        raw = b"# Receta\n## Elaboraci\xc3\xb3n\n### 1. Mezclar\nTexto\n### 2. Servir\nTexto\n## Variantes\n1. Otro\n"
        result,_ = extract_content(raw)
        self.assertEqual([s["source_number"] for s in result["steps"]],[1,2])
        self.assertEqual(result["steps"][0]["source_location"]["start_line"],3)

    def test_unknown_is_not_validated(self):
        result,_ = extract_content(b"---\nestado: estable\n---\n# Receta\n## Elaboracion\n1. Mezclar\n")
        self.assertEqual(result["evidence"]["status"],"unknown")
        self.assertIsNone(result["evidence"]["current_formula_validated"])

    def test_fenced_example_not_step(self):
        result,_ = extract_content(b"# Receta\n## Elaboracion\n1. Mezclar\n~~~\n# Variante\n2. Ejemplo\n~~~\n2. Servir\n")
        self.assertEqual([s["source_number"] for s in result["steps"]],[1,2])

    def test_conflicting_claims_remain_unknown(self):
        result,_ = extract_content("## Descripci\u00f3n\nYa cocinada y valorada. Pendiente de prueba.\n".encode())
        self.assertEqual(result["evidence"]["status"],"unknown")


    def test_directed_historical_scope(self):
        commit = "0deb4df8947bd1ece17d3accb7ead60b4a17634d"
        cases = [
            ("05_Carnes/hamburguesa_especiada.md","prepared","historical_preparation"),
            ("05_Carnes/ropa_vieja_base_y_pulled_pork.md","prepared","historical_preparation"),
            ("06_Pescados_y_Mariscos/boquerones_en_vinagre.md","prepared","historical_preparation"),
            ("05_Carnes/magret_de_pato_estilo_sichuan.md","unknown","related_variant"),
            ("04_Verduras/zanahorias_alinadas_andaluzas.md","unknown","component_only"),
        ]
        for path,status,scope in cases:
            with self.subTest(path=path):
                result,_=extract_content(snapshot_bytes(ROOT_DIR,commit,path))
                self.assertEqual(result["evidence"]["status"],status)
                self.assertEqual(result["evidence"]["scope"],scope)
                self.assertIsNot(result["evidence"]["current_formula_validated"],True)

    def test_proposal_and_document_status_do_not_prove_preparation(self):
        result,_=extract_content("## Descripción\nEs una elaboración habitual de la cocina doméstica. No está confirmado que fuese la versión realmente elaborada.\n".encode())
        self.assertEqual(result["evidence"]["status"],"unknown")
        self.assertIsNone(result["evidence"]["historical_preparation"])
