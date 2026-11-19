import unittest

from evaluate_recipe_queries import temporal_coverage


def duration(phase="declared_total", lo="30", hi="40", unit="min"):
    return {"phase": phase, "min": lo, "max": hi, "unit": unit}


class TemporalCoverageTests(unittest.TestCase):
    def test_does_not_sum_phases_or_infer_missing_values(self):
        records = [
            {"durations": [duration("preparation"), duration("cooking")], "yield": None},
            {"durations": [duration(lo=None, hi=None, unit=None)],
             "yield": {"min": None, "max": None, "unit": None}},
            {"durations": [duration(), duration()], "yield": None},
            {"durations": [duration(unit="h")],
             "yield": {"min": "3", "max": "4", "unit": "racion"}},
        ]
        report = temporal_coverage(records)
        self.assertEqual(report["duration"], {"no_declared_total": 1,
            "unparsed_declared_total": 1, "multiple_declared_totals": 1,
            "single_numeric_declared_total": 1})
        self.assertEqual(report["yield"], {"absent_or_ambiguous": 2,
            "unparsed": 1, "numeric": 1})
        self.assertEqual(report["yield_units"], {"racion": 1})

    def test_empty_corpus(self):
        self.assertEqual(temporal_coverage([]),
                         {"duration": {}, "yield": {}, "yield_units": {}})


if __name__ == "__main__":
    unittest.main()
