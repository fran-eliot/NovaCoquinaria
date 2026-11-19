import unittest
from report_recipe_coverage import coverage, summarize


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
