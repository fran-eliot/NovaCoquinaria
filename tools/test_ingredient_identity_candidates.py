import unittest
from ingredient_identity_candidates import build_catalog, annotate


class CandidateTests(unittest.TestCase):
    def setUp(self):
        self.catalog=build_catalog({
            "cebolla.md":{"titulo":"Cebolla","id":"ING-0013"},
            "soja.md":{"titulo":"Salsa de soja","id":"ING-0002"},
            "coco.md":{"titulo":"Leche de coco","id":"ING-0012"},
            "nata.md":{"titulo":"Nata","id":"ING-X"},
        })

    def test_exact_and_alias_not_identity(self):
        entries=[{"name":" CEBOLLAS; ","resolution":"unresolved","ingredient_id":None},
                 {"name":"Salsa de soja clara","resolution":"unresolved","ingredient_id":None}]
        annotate(entries,self.catalog)
        self.assertEqual(entries[0]["identity_candidates"][0]["ingredient_id"],"ING-0013")
        self.assertEqual(entries[1]["identity_candidates"][0]["method"],"reviewed_alias")
        self.assertIsNone(entries[0]["ingredient_id"])
        self.assertEqual(entries[0]["resolution"],"unresolved")

    def test_no_substrings_alternatives_or_explicit_override(self):
        entries=[{"name":name,"resolution":resolution} for name,resolution in [
            ("caponata","unresolved"),("cebolla o ajo","unresolved"),
            ("leche de coco ligera","unresolved"),("cebolla","explicit")]]
        annotate(entries,self.catalog)
        self.assertTrue(all(not e["identity_candidates"] for e in entries))

    def test_collision_keeps_both(self):
        catalog=build_catalog({"a.md":{"titulo":"Cebolla","id":"A"},
                               "b.md":{"titulo":"Cebolla","id":"B"}})
        entries=[{"name":"cebolla","resolution":"unresolved"}]
        annotate(entries,catalog)
        self.assertEqual(entries[0]["candidate_status"],"multiple")
        self.assertEqual(len(entries[0]["identity_candidates"]),2)


    def test_reviewed_forms_keep_qualifiers_and_avoid_generalization(self):
        catalog=build_catalog({
            "pimenton.md":{"titulo":"Pimentón","id":"ING-0068"},
            "laurel.md":{"titulo":"Laurel","id":"ING-0123"},
            "huevo.md":{"titulo":"Huevo","id":"ING-0022"},
            "aceite.md":{"titulo":"Aceite de oliva virgen extra","id":"ING-0029"},
            "azucar.md":{"titulo":"Azúcar blanco","id":"ING-0058"},
            "tomate.md":{"titulo":"Tomate triturado en conserva","id":"ING-0027"},
            "limon.md":{"titulo":"Limón","id":"ING-0046"},
        })
        positive={"pimentón dulce":"ING-0068","hoja de laurel;":"ING-0123",
                  "huevos L":"ING-0022","AOVE":"ING-0029","zumo de limón":"ING-0046"}
        negatives=["aceite de oliva","azúcar","tomate triturado","sal y pimienta",
                   "arroz jazmín o basmati","pimentón o comino"]
        for name,identity in positive.items():
            with self.subTest(name=name):
                entry={"name":name,"resolution":"unresolved","ingredient_id":None}
                annotate([entry],catalog)
                self.assertEqual(entry["identity_candidates"][0]["ingredient_id"],identity)
                self.assertEqual(entry["name"],name)
                self.assertIsNone(entry["ingredient_id"])
        for name in negatives:
            with self.subTest(name=name):
                entry={"name":name,"resolution":"unresolved","ingredient_id":None}
                annotate([entry],catalog)
                self.assertEqual(entry["identity_candidates"],[])
