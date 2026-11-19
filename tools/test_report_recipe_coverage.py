import unittest
from report_recipe_coverage import coverage, summarize, structural_gaps, candidate_review


def record(identity="REC-1", module="01_Arroces"):
    return {"id":identity,"physical_module":module,"source":{"path":module+"/r.md"},
            "category":None,"sections":[{}],"steps":[],
            "yield":{"min":None},"durations":[{"min":"10"},{"min":None}],
            "ingredients":[{"quantity":{"status":"exact"},"resolution":"explicit","optionality":"required"},
                           {"quantity":{"status":"missing"},"resolution":"unresolved","optionality":"unknown"}],
            "references":[{"status":"resolved","target_id":None},{"status":"external","target_id":None},
                          {"status":"unresolved","target_id":None},{"status":"local_anchor","target_id":identity}],
            "evidence":{"status":"unknown"},"diagnostics":[{"code":"X"},{"code":"X"}]}


class CoverageTests(unittest.TestCase):
    def test_denominators(self):
        report=summarize([record()])
        self.assertEqual(report["quantity_numeric"]["count"],1)
        self.assertEqual(report["quantity_numeric"]["denominator"],2)
        self.assertEqual(report["internal_resolved"]["denominator"],2)
        self.assertEqual(report["internal_with_id"]["count"],0)
        self.assertEqual(report["field_presence"]["yield_declared"]["count"],1)
        self.assertEqual(report["field_presence"]["yield_numeric"]["count"],0)
        self.assertEqual(report["diagnostic_occurrences"],{"X":2})

    def test_empty_is_not_perfect(self):
        report=summarize([])
        self.assertIsNone(report["quantity_numeric"]["percent"])
        self.assertIsNone(report["field_presence"]["steps"]["percent"])

    def test_grouping_and_affected_recipes(self):
        p={"recipes":[record(),record("REC-2","02_Pastas")],
           "stage":"recipe_projection_preview","inventory":{"recipe_documents":2},
           "source_commit":"fixture","contract_version":"0.1.0","extractor_version":"0.4.0"}
        report=coverage(p)
        self.assertEqual(report["global"]["recipes"],2)
        self.assertEqual(report["by_module"]["02_Pastas"]["recipes"],1)
        self.assertEqual(len(report["affected_recipes"]["X"]),2)
        self.assertEqual(report,coverage(p))
        p["inventory"]["recipe_documents"]=3
        with self.assertRaises(ValueError):
            coverage(p)


    def test_structural_gap_review(self):
        first=record()
        first["ingredients"]=[]
        first["sections"]=[{"heading":"Preparación","source_location":{"start_line":10,"end_line":15}}]
        second=record("REC-2")
        second["steps"]=[{}]
        result=structural_gaps([second,first])
        self.assertEqual(len(result),1)
        self.assertEqual(result[0]["missing"],["ingredients","steps"])
        self.assertEqual(result[0]["id"],"REC-1")
        self.assertEqual(result[0]["headings"][0]["heading"],"Preparación")
        self.assertEqual(result[0]["headings"][0]["source_location"]["start_line"],10)


    def test_candidate_review_separates_unresolved_and_explicit(self):
        first = record()
        first["ingredients"] = [
            {"resolution":"explicit","name":"cebolla","identity_candidates":[]},
            {"resolution":"unresolved","name":"cebolla","raw":"1 cebolla",
             "identity_candidates":[{"ingredient_id":"ING-1","method":"title_exact"}]},
            {"resolution":"unresolved","name":"sal fina","raw":"sal fina"},
            {"resolution":"unresolved","name":"sal fina","raw":"sal fina"},
        ]
        result = candidate_review([first], limit=1)
        self.assertEqual(result["method_occurrences"], {"title_exact":1})
        self.assertEqual(result["frequent_unmatched_names"], [{"name":"sal fina","count":2}])
        self.assertEqual(len(result["samples"]["single"]), 1)
        self.assertEqual(len(result["samples"]["none"]), 1)
        self.assertEqual(result, candidate_review([first], limit=1))
