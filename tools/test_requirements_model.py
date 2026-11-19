import unittest
from experiment_culinary_requirements import validate_node, shape

def atom(label="ajo"):
    return {"type":"atom", "label":label, "presence":"required"}

class RequirementsModelTests(unittest.TestCase):
    def test_qualifiers_not_children(self):
        n = {**atom(), "qualifiers":["picado","pelado"]}
        validate_node(n)
        self.assertEqual(shape(n), "atom")

    def test_nested_adaptation(self):
        n = {"type":"any","presence":"required","children":[atom("doubanjiang"),
             {"type":"all","presence":"required","adaptation":True,"children":[atom("chile"),atom("miso")]}]}
        validate_node(n)
        self.assertEqual(shape(n), "any(atom,all(atom,atom))")

    def test_invalid_arity(self):
        with self.assertRaises(ValueError):
            validate_node({"type":"any","presence":"required","children":[atom()]})

    def test_adaptation_dose(self):
        with self.assertRaises(ValueError):
            validate_node({**atom(),"adaptation":True,"quantity_scope":"base"})

    def test_choice_unknown(self):
        with self.assertRaises(ValueError):
            validate_node({"type":"choice","presence":"required","children":[atom(),atom()]})

    def test_condition_not_evaluated(self):
        validate_node({**atom(),"conditions":[{"scope":"preparation","text":"si procede"}]})
        with self.assertRaises(ValueError):
            validate_node({**atom(),"presence":"conditional"})

    def test_no_identity_promotion(self):
        with self.assertRaises(ValueError):
            validate_node({**atom(),"ingredient_id":"ING-1"})
