import unittest

from pathlib import Path

from audit_inventory import RECIPE_MODULES, build_inventory
from audit_knowledge import (
    AssociationLevel, DomainKind, DomainRule, KNOWLEDGE_RULES,
    DomainAudit, audit_to_dict, render_markdown,
    classify_direct_association, has_canonical_recipe_path,
)
from models import Document


class InventoryTests(unittest.TestCase):
    def test_counts_and_exclusions(self):
        result = build_inventory([
            "README.md", "01_Arroces/README.md", "01_Arroces/arroz.md",
            "07_Cocina_Asiatica/receta.md", "09_Bebidas/bebida.md",
            "10_Horno/masa.md", "11_Despensa/README.md",
            "11_Despensa/BACKLOG.md", "11_Despensa/ingrediente.md",
            "00_Bases/03_Tecnicas/README.md",
            "00_Bases/03_Tecnicas/tecnica.md", "tools/common.py",
        ], "test-commit")
        self.assertEqual(result["markdown_files"], 11)
        self.assertEqual(result["recipe_paths"], 4)
        self.assertEqual(len(result["recipe_paths_by_module"]), 10)
        self.assertEqual(result["recipe_paths_by_module"]["02_Pastas"], 0)
        self.assertEqual(result["ingredient_paths"], 1)
        self.assertEqual(result["technique_paths"], 1)
        self.assertEqual(result["commit"], "test-commit")



class RecipeDomainClassificationTests(unittest.TestCase):
    # Módulos físicos y dominios culinarios son vistas distintas.
    MODULES = (
        "01_Arroces", "02_Pastas", "03_Legumbres", "04_Verduras",
        "05_Carnes", "06_Pescados_y_Mariscos", "07_Cocina_Asiatica",
        "08_Postres", "09_Bebidas", "10_Horno",
    )

    def recipe(self, module, title="Pollo con verduras", **metadata):
        return Document(
            path=Path(module) / "ejemplo.md",
            frontmatter={"id": "REC-TEST", "tipo": "receta",
                         "titulo": title, **metadata},
            content="[Patrón](../12_Plantillas/04_Cocciones/curry_base.md)",
        )

    def test_inventory_and_canonical_paths_agree(self):
        self.assertEqual(RECIPE_MODULES, self.MODULES)
        for module in self.MODULES:
            with self.subTest(module=module):
                self.assertTrue(has_canonical_recipe_path(self.recipe(module)))
        self.assertFalse(has_canonical_recipe_path(self.recipe("07_Cocina_Asiatica_extra")))
        self.assertFalse(has_canonical_recipe_path(self.recipe("00_Bases")))

    def test_cross_module_authority_link_is_secondary(self):
        rule = next(rule for rule in KNOWLEDGE_RULES if rule.key == "currys")
        for module in self.MODULES:
            with self.subTest(module=module):
                association = classify_direct_association(self.recipe(module), rule)
                self.assertEqual(association.level, AssociationLevel.SECONDARY)
                self.assertEqual(association.evidence, ("foreign_authority_link",))

    def test_pattern_title_remains_primary(self):
        rule = next(rule for rule in KNOWLEDGE_RULES if rule.key == "currys")
        for module in self.MODULES:
            with self.subTest(module=module):
                association = classify_direct_association(
                    self.recipe(module, "Curry de verduras"), rule
                )
                self.assertEqual(association.level, AssociationLevel.PRIMARY)
                self.assertIn("pattern_title", association.evidence)

    def test_declared_reference_remains_primary(self):
        rule = DomainRule(
            key="patron_prueba", name="Patrón de prueba", kind=DomainKind.PATTERN,
            primary_keywords=("curry",),
            primary_link_fragments=("12_Plantillas/04_Cocciones/curry_base.md",),
            reference_recipe_keywords=("pollo con verduras",),
        )
        association = classify_direct_association(
            self.recipe("07_Cocina_Asiatica"), rule
        )
        self.assertEqual(association.level, AssociationLevel.PRIMARY)
        self.assertIn("declared_reference", association.evidence)

    def test_explicit_domain_remains_primary(self):
        rule = next(rule for rule in KNOWLEDGE_RULES if rule.key == "currys")
        association = classify_direct_association(
            self.recipe("10_Horno", dominio_principal="currys"), rule
        )
        self.assertEqual(association.level, AssociationLevel.PRIMARY)
        self.assertEqual(association.evidence, ("explicit_domain",))

    def test_noncanonical_recipe_preserves_existing_pattern_behavior(self):
        rule = next(rule for rule in KNOWLEDGE_RULES if rule.key == "currys")
        association = classify_direct_association(self.recipe("00_Bases"), rule)
        self.assertEqual(association.level, AssociationLevel.PRIMARY)
        self.assertEqual(association.evidence, ("authority_link",))


class AuditMetricPresentationTests(unittest.TestCase):
    def test_denominators_and_scope_in_reports(self):
        rule = DomainRule(
            key="prueba", name="Prueba", kind=DomainKind.CATEGORY,
            primary_keywords=("prueba",),
            expected_types=("receta", "tecnica"),
        )
        audit = DomainAudit(rule=rule)
        document = Document(Path("01_Arroces/prueba.md"),
                            {"tipo": "receta", "titulo": "Prueba"}, "")
        audit.primary_by_type["receta"].append(document)
        audit.orphan_documents.append(document)
        result = audit_to_dict(audit)
        self.assertEqual(result["domain_kind"], "category")
        self.assertEqual(result["expected_types"], ["receta", "tecnica"])
        self.assertEqual(result["represented_expected_types"], ["receta"])
        self.assertEqual(result["structural_coverage"], 50.0)
        self.assertIsNone(result["link_resolution_rate"])
        self.assertEqual(result["primary_without_outgoing_links"],
                         ["01_Arroces/prueba.md"])
        self.assertEqual(result["orphan_documents"],
                         result["primary_without_outgoing_links"])
        report = render_markdown([audit])
        self.assertIn("1/2 (50 %)", report)
        self.assertIn("PRIMARY sin salidas", report)
        self.assertIn("0/0 (N/A)", report)

    def test_equal_percentages_can_have_different_denominators(self):
        for expected in (("ingrediente",), ("ingrediente", "tecnica")):
            with self.subTest(expected=expected):
                rule = DomainRule(
                    key="prueba", name="Prueba", kind=DomainKind.INGREDIENT,
                    primary_keywords=("prueba",), expected_types=expected,
                )
                audit = DomainAudit(rule=rule)
                for kind in expected:
                    audit.primary_by_type[kind].append(
                        Document(Path(f"{kind}.md"), {"tipo": kind}, "")
                    )
                result = audit_to_dict(audit)
                self.assertEqual(result["structural_coverage"], 100.0)
                self.assertEqual(len(result["expected_types"]), len(expected))
                self.assertIn(f"{len(expected)}/{len(expected)} (100 %)",
                              render_markdown([audit]))
    

if __name__ == "__main__":
    unittest.main()
