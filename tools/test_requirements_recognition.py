import unittest
from experiment_requirements_recognition import proposal, partition, groups

class RecognitionTests(unittest.TestCase):
    def test_optional(self):
        self.assertEqual(proposal({"raw":"1 guindilla (opcional)."})["kind"],"optional")

    def test_partial_and_url(self):
        for raw in ("sal y perejil opcional","sal no opcional","[sal](opcional.md)","agua, si hace falta"):
            self.assertIsNone(proposal({"raw":raw}))

    def test_preparation(self):
        self.assertEqual(proposal({"raw":"gambas peladas, descongeladas si procede;"})["kind"],"preparation")

    def test_adjustment(self):
        e={"raw":"3 cucharadas de aceite, añadir si hace falta","quantity":{"status":"exact","min":"3","max":"3"}}
        self.assertEqual(proposal(e)["kind"],"adjustment")
        self.assertIsNone(proposal({"raw":e["raw"]}))

    def test_group_context(self):
        entries=[{"raw":"arroz","group":"Guarnición","source_location":{"start_line":3}},
                 {"raw":"pan","group":"Guarnición","source_location":{"start_line":4}}]
        self.assertEqual(groups(["## Guarnición","A elegir:","- arroz","- pan","---"],entries)[0]["positions"],[0,1])
        self.assertEqual(groups(["## Guarnición","","- arroz","- pan","---"],entries),[])

    def test_conflict(self):
        entries=[{"raw":"arroz"},{"raw":"pan"}]
        candidates=[{"kind":"choice","positions":[0,1]},{"kind":"optional","positions":[0]}]
        roots=partition(entries,candidates,[])
        self.assertEqual([r["positions"] for r in roots],[[0],[1]])
        self.assertTrue(all("kind" not in r for r in roots))

    def test_invalid_reference(self):
        with self.assertRaises(ValueError):
            partition([{"raw":"sal"}],[{"kind":"optional","positions":[1]}],[])
