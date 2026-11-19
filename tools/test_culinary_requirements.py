import hashlib
import unittest
from audit_culinary_requirements import signals, inventory


def entry(raw, line=1, group=None, status="missing", option="required"):
    return {"raw": raw, "name": raw, "group": group, "quantity": {"status": status},
            "source_location": {"start_line": line, "end_line": line},
            "optionality": option, "resolution": "unresolved", "ingredient_id": None}


class RequirementsSignalsTests(unittest.TestCase):
    def test_whole_words_and_links(self):
        self.assertEqual(signals(entry("[Aceite](../o/y.md)")), set())
        self.assertEqual(signals(entry("aceite de oliva o girasol")), {"S01"})
        self.assertNotIn("S01", signals(entry("pollo")))

    def test_overlap(self):
        self.assertEqual(signals(entry("ajo fresco y cebolla, opcionales, según gusto")),
                         {"S03", "S04", "S05", "S07"})

    def test_groups_and_quantity(self):
        self.assertEqual(signals(entry("sal", group="Acompañamiento", status="qualitative")),
                         {"S06", "S08"})

    def test_adjacent_and_unresolved_connectors(self):
        raw = b"- arroz o\n- pan\n- patata o\n\n- pasta\n"
        entries = [entry("arroz o", 1), entry("pan", 2),
                   entry("patata o", 3), entry("pasta", 5)]
        p = {"source_commit": "a"*40, "recipes": [{"id": "REC-1",
             "source": {"path": "r.md", "sha256": hashlib.sha256(raw).hexdigest()},
             "physical_module": "test", "ingredients": entries}]}
        report = inventory(p, lambda _: raw)
        self.assertEqual(report["occurrences"], 4)
        self.assertEqual(report["flagged_occurrences"], 2)
        self.assertEqual(report["by_signal"]["S02"]["occurrences"], 2)
        self.assertEqual(report["by_signal"]["S01"]["occurrences"], 0)
        self.assertEqual(report["adjacent_edges"][0]["positions"], [0, 1])
        self.assertEqual(report["unresolved_trailing_connectors"][0]["position"], 2)
        self.assertEqual(report, inventory(p, lambda _: raw))
        with self.assertRaises(ValueError):
            inventory(p, lambda _: b"wrong")
