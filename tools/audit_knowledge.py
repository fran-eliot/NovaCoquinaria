from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from enum import StrEnum
from datetime import date
from pathlib import Path
import argparse
import json
import re
import unicodedata

from common import ROOT_DIR, load_documents, print_ok
from models import Document
from audit_inventory import RECIPE_MODULES


REPORT_DEFAULT = Path("docs/management/generated/KNOWLEDGE_AUDIT.md")
JSON_DEFAULT = Path("docs/management/generated/knowledge_audit.json")

CULINARY_DOCUMENT_TYPES = {
    "base",
    "ingrediente",
    "tecnica",
    "plantilla",
    "receta",
    "tabla",
}

SECONDARY_EXPANSION_TYPES = {
    "base",
    "tecnica",
    "plantilla",
    "receta",
}

CANONICAL_RECIPE_PATH_PREFIXES = tuple(f"{module}/" for module in RECIPE_MODULES)

IGNORED_PATH_PREFIXES = (
    "docs/",
    "site_docs/",
)


class AssociationLevel(StrEnum):
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"
    MENTION = "MENTION"


class DomainKind(StrEnum):
    PATTERN = "pattern"
    CATEGORY = "category"
    INGREDIENT = "ingredient"


ASSOCIATION_PRIORITY = {
    AssociationLevel.MENTION: 1,
    AssociationLevel.SECONDARY: 2,
    AssociationLevel.PRIMARY: 3,
}


@dataclass(frozen=True, slots=True)
class DomainRule:
    """Regla declarativa para clasificar conocimiento por dominio culinario."""

    key: str
    name: str
    kind: DomainKind
    primary_keywords: tuple[str, ...]
    secondary_keywords: tuple[str, ...] = ()
    path_fragments: tuple[str, ...] = ()
    primary_link_fragments: tuple[str, ...] = ()
    title_primary_types: tuple[str, ...] = (
        "base",
        "tecnica",
        "plantilla",
        "receta",
    )
    expected_types: tuple[str, ...] = (
        "ingrediente",
        "tecnica",
        "plantilla",
        "receta",
        "tabla",
    )
    reference_recipe_keywords: tuple[str, ...] = ()

    @property
    def all_keywords(self) -> tuple[str, ...]:
        return self.primary_keywords + self.secondary_keywords


@dataclass(frozen=True, slots=True)
class DomainAssociation:
    document: Document
    level: AssociationLevel
    evidence: tuple[str, ...]


@dataclass(slots=True)
class DomainAudit:
    rule: DomainRule
    associations: list[DomainAssociation] = field(default_factory=list)
    primary_by_type: dict[str, list[Document]] = field(
        default_factory=lambda: defaultdict(list)
    )
    outgoing_links: int = 0
    resolved_outgoing_links: int = 0
    orphan_documents: list[Document] = field(default_factory=list)
    reference_recipes: list[Document] = field(default_factory=list)

    @property
    def primary_associations(self) -> list[DomainAssociation]:
        return [
            association
            for association in self.associations
            if association.level == AssociationLevel.PRIMARY
        ]

    @property
    def secondary_associations(self) -> list[DomainAssociation]:
        return [
            association
            for association in self.associations
            if association.level == AssociationLevel.SECONDARY
        ]

    @property
    def mention_associations(self) -> list[DomainAssociation]:
        return [
            association
            for association in self.associations
            if association.level == AssociationLevel.MENTION
        ]

    @property
    def primary_documents(self) -> list[Document]:
        return [association.document for association in self.primary_associations]

    @property
    def document_count(self) -> int:
        """Número de documentos de autoridad del dominio."""
        return len(self.primary_associations)

    @property
    def associated_document_count(self) -> int:
        return len(self.associations)

    @property
    def type_counts(self) -> Counter[str]:
        return Counter(
            (document.tipo or "sin_tipo")
            for document in self.primary_documents
        )

    @property
    def represented_expected_types(self) -> set[str]:
        return {
            document_type
            for document_type in self.rule.expected_types
            if self.primary_by_type.get(document_type)
        }

    @property
    def structural_coverage(self) -> float:
        """
        Cobertura estructural de autoridad.

        Solo considera documentos PRIMARY. Las asociaciones SECONDARY y MENTION
        expresan reutilización o contexto, pero no madurez propia del dominio.
        """
        if not self.rule.expected_types:
            return 0.0
        return 100.0 * len(self.represented_expected_types) / len(
            self.rule.expected_types
        )

    @property
    def link_resolution_rate(self) -> float | None:
        if not self.outgoing_links:
            return None
        return 100.0 * self.resolved_outgoing_links / self.outgoing_links


KNOWLEDGE_RULES: tuple[DomainRule, ...] = (
    DomainRule(
        key="currys",
        name="Currys",
        kind=DomainKind.PATTERN,
        primary_keywords=("curry", "massaman", "panang"),
        secondary_keywords=("leche de coco", "salsa de pescado"),
        primary_link_fragments=("12_Plantillas/04_Cocciones/curry_base.md",),
        title_primary_types=("ingrediente", "tecnica", "plantilla", "receta", "tabla"),
        reference_recipe_keywords=("curry amarillo de pollo",),
    ),
    DomainRule(
        key="salteados_asiaticos",
        name="Salteados asiáticos",
        kind=DomainKind.PATTERN,
        primary_keywords=("salteado asiatico", "salteado asiático", "wok"),
        secondary_keywords=(
            "salsa de ostras",
            "salsa china base",
            "marinada asiatica",
            "marinada asiática",
            "bambu",
            "bambú",
        ),
        primary_link_fragments=(
            "12_Plantillas/04_Cocciones/salteado_asiatico.md",
        ),
        title_primary_types=("tecnica", "plantilla", "receta"),
        reference_recipe_keywords=(
            "ternera con salsa de ostras",
            "pollo salteado con verduras",
        ),
    ),
    DomainRule(
        key="arroces",
        name="Arroces",
        kind=DomainKind.CATEGORY,
        primary_keywords=("arroz", "chaufa", "risotto", "paella"),
        secondary_keywords=("huevo", "vinagre de arroz"),
        path_fragments=(
            "01_Arroces",
            "12_Plantillas/05_Arroces",
            "11_Despensa/01_Cereales",
        ),
        title_primary_types=("base", "tecnica", "plantilla", "receta"),
        reference_recipe_keywords=("arroz chaufa", "arroz frito con pollo"),
    ),
    DomainRule(
        key="pastas",
        name="Pastas",
        kind=DomainKind.CATEGORY,
        primary_keywords=(
            "pasta",
            "espagueti",
            "spaghetti",
            "macarron",
            "macarrón",
            "lasana",
            "lasaña",
        ),
        path_fragments=("02_Pastas",),
    ),
    DomainRule(
        key="legumbres",
        name="Legumbres",
        kind=DomainKind.CATEGORY,
        primary_keywords=(
            "legumbre",
            "lenteja",
            "garbanzo",
            "judia",
            "judía",
            "frijol",
        ),
        path_fragments=("03_Legumbres", "11_Despensa/02_Legumbres"),
    ),
    DomainRule(
        key="verduras",
        name="Verduras",
        kind=DomainKind.INGREDIENT,
        primary_keywords=(
            "verdura",
            "brocoli",
            "brócoli",
            "champinon",
            "champiñón",
            "habas",
        ),
        secondary_keywords=("ajo", "cebolla", "jengibre", "pimiento", "zanahoria"),
        path_fragments=("04_Verduras", "11_Despensa/06_Verduras"),
        title_primary_types=("ingrediente",),
        expected_types=("ingrediente",),
    ),
    DomainRule(
        key="carnes",
        name="Carnes",
        kind=DomainKind.INGREDIENT,
        primary_keywords=("pollo", "ternera", "cerdo", "lomo", "solomillo", "carne"),
        path_fragments=("05_Carnes", "11_Despensa/03_Carnes"),
        title_primary_types=("ingrediente",),
        expected_types=("ingrediente",),
    ),
    DomainRule(
        key="pescados_mariscos",
        name="Pescados y mariscos",
        kind=DomainKind.INGREDIENT,
        primary_keywords=(
            "pescado",
            "marisco",
            "gamba",
            "caballa",
            "merluza",
            "bacalao",
            "tintorera",
            "calamar",
        ),
        path_fragments=(
            "06_Pescados_y_Mariscos",
            "11_Despensa/04_Pescados",
            "11_Despensa/05_Mariscos",
        ),
        title_primary_types=("ingrediente",),
        expected_types=("ingrediente",),
    ),
    DomainRule(
        key="huevos_lacteos",
        name="Huevos y lácteos",
        kind=DomainKind.INGREDIENT,
        primary_keywords=("huevo", "lacteo", "lácteo", "queso", "nata"),
        secondary_keywords=("leche", "leche de coco"),
        path_fragments=("11_Despensa/14_Huevos_Lacteos",),
        title_primary_types=("ingrediente",),
        expected_types=("ingrediente",),
    ),
    DomainRule(
        key="postres",
        name="Postres",
        kind=DomainKind.CATEGORY,
        primary_keywords=("postre", "tarta", "bizcocho", "crema dulce"),
        path_fragments=("08_Postres",),
    ),
)



def normalize(value: object) -> str:
    """Normaliza texto para comparaciones tolerantes a tildes y mayúsculas."""
    text = str(value or "").lower()
    text = unicodedata.normalize("NFKD", text)
    return "".join(char for char in text if not unicodedata.combining(char))


def flatten_frontmatter(frontmatter: dict) -> str:
    values: list[str] = []
    for value in frontmatter.values():
        if isinstance(value, (list, tuple, set)):
            values.extend(str(item) for item in value)
        elif isinstance(value, dict):
            values.extend(str(item) for item in value.values())
        else:
            values.append(str(value))
    return " ".join(values)


def normalized_frontmatter_fields(document: Document) -> dict[str, str]:
    fields: dict[str, str] = {}
    for key in (
        "titulo",
        "descripcion",
        "categoria",
        "subcategoria",
        "familia",
        "cocina",
        "tags",
        "etiquetas",
    ):
        if key in document.frontmatter:
            fields[key] = normalize(document.frontmatter[key])
    return fields


def document_title_text(document: Document) -> str:
    return normalize(document.titulo)


def document_heading_text(document: Document) -> str:
    return normalize(
        " ".join(
            line.lstrip("# ").strip()
            for line in document.content.splitlines()
            if line.startswith("#")
        )
    )


def document_body_text(document: Document) -> str:
    return normalize(document.content)


def is_auditable_knowledge_document(document: Document) -> bool:
    """
    Limita la vista de dominios al conocimiento culinario fuente.

    Se excluyen documentación técnica, gestión, informes generados, módulos y
    archivos README, aunque contengan ejemplos o vocabulario culinario.
    """
    document_type = normalize(document.tipo).replace(" ", "_")
    if document_type not in CULINARY_DOCUMENT_TYPES:
        return False

    relative_path = document.relative_path.replace(chr(92), "/")
    if Path(relative_path).name.lower() == "readme.md":
        return False

    return not any(
        relative_path.startswith(prefix)
        for prefix in IGNORED_PATH_PREFIXES
    )


def contains_any(text: str, keywords: tuple[str, ...]) -> bool:
    return any(normalize(keyword) in text for keyword in keywords)


def explicit_primary_domain(document: Document) -> str:
    for key in ("dominio_principal", "primary_domain", "domain"):
        value = document.frontmatter.get(key)
        if value:
            return normalize(value).replace(" ", "_")
    return ""


def document_links_rule_authority(
    document: Document,
    rule: DomainRule,
) -> bool:
    if not rule.primary_link_fragments:
        return False

    normalized_targets = tuple(
        normalize(fragment)
        for fragment in rule.primary_link_fragments
    )
    return any(
        any(fragment in normalize(target) for fragment in normalized_targets)
        for target in document.links
    )


def is_declared_reference_recipe(
    document: Document,
    rule: DomainRule,
) -> bool:
    if not rule.reference_recipe_keywords:
        return False

    title = document_title_text(document)
    return any(
        normalize(keyword) in title
        for keyword in rule.reference_recipe_keywords
    )


def has_canonical_recipe_path(document: Document) -> bool:
    relative_path = document.relative_path.replace(chr(92), "/")
    return any(
        relative_path.startswith(prefix)
        for prefix in CANONICAL_RECIPE_PATH_PREFIXES
    )


def meaningful_heading_text(document: Document) -> str:
    """
    Extrae solo encabezados que suelen expresar una relación culinaria útil.

    Se ignoran encabezados genéricos para evitar que una coincidencia léxica
    convierta cualquier documento en una mención contextual.
    """
    relevant_prefixes = (
        "variante",
        "variantes",
        "aplicacion",
        "aplicaciones",
        "uso",
        "usos",
        "sustitucion",
        "sustituciones",
        "acompanamiento",
        "acompañamiento",
        "combinacion",
        "combinaciones",
    )

    headings: list[str] = []
    for line in document.content.splitlines():
        if not line.startswith("#"):
            continue

        heading = line.lstrip("# ").strip()
        normalized_heading = normalize(heading)
        if any(
            normalized_heading.startswith(prefix)
            for prefix in relevant_prefixes
        ):
            headings.append(heading)

    return normalize(" ".join(headings))


def classify_direct_association(
    document: Document,
    rule: DomainRule,
) -> DomainAssociation | None:
    """
    Clasifica una relación directa aplicando una jerarquía de evidencias.

    PRIMARY:
      - ruta de autoridad;
      - dominio principal explícito;
      - título inequívoco en un tipo autorizado;
      - implementación que enlaza la plantilla de autoridad del patrón.

    SECONDARY:
      - coincidencia temática en título o Front Matter no autoritativo.

    MENTION:
      - coincidencia solo contextual en encabezados o cuerpo.
    """
    relative_path = normalize(document.relative_path)
    title = document_title_text(document)
    frontmatter_fields = normalized_frontmatter_fields(document)
    structured = " ".join(frontmatter_fields.values())
    headings = meaningful_heading_text(document)
    document_type = normalize(document.tipo).replace(" ", "_")

    path_matches = any(
        normalize(fragment) in relative_path
        for fragment in rule.path_fragments
    )

    if path_matches:
        if rule.kind == DomainKind.INGREDIENT:
            if document_type == "ingrediente":
                return DomainAssociation(
                    document=document,
                    level=AssociationLevel.PRIMARY,
                    evidence=("path",),
                )

            return DomainAssociation(
                document=document,
                level=AssociationLevel.SECONDARY,
                evidence=("thematic_path",),
            )

        return DomainAssociation(
            document=document,
            level=AssociationLevel.PRIMARY,
            evidence=("path",),
        )

    explicit_domain = explicit_primary_domain(document)
    if explicit_domain == rule.key:
        return DomainAssociation(
            document=document,
            level=AssociationLevel.PRIMARY,
            evidence=("explicit_domain",),
        )

    if (
        rule.kind == DomainKind.PATTERN
        and document_type == "receta"
        and document_links_rule_authority(document, rule)
    ):
        title_matches_pattern = contains_any(
            document_title_text(document),
            rule.primary_keywords,
        )
        declared_reference = is_declared_reference_recipe(document, rule)

        if title_matches_pattern or declared_reference:
            evidence = ["authority_link"]
            if title_matches_pattern:
                evidence.append("pattern_title")
            if declared_reference:
                evidence.append("declared_reference")

            return DomainAssociation(
                document=document,
                level=AssociationLevel.PRIMARY,
                evidence=tuple(evidence),
            )

        if has_canonical_recipe_path(document):
            return DomainAssociation(
                document=document,
                level=AssociationLevel.SECONDARY,
                evidence=("foreign_authority_link",),
            )

        return DomainAssociation(
            document=document,
            level=AssociationLevel.PRIMARY,
            evidence=("authority_link",),
        )

    primary_in_title = contains_any(title, rule.primary_keywords)
    if (
        rule.kind != DomainKind.INGREDIENT
        and primary_in_title
        and document_type in rule.title_primary_types
    ):
        return DomainAssociation(
            document=document,
            level=AssociationLevel.PRIMARY,
            evidence=("title",),
        )

    evidence: list[str] = []
    if primary_in_title:
        evidence.append("thematic_title")

    if contains_any(structured, rule.primary_keywords):
        evidence.append("frontmatter")

    if contains_any(title, rule.secondary_keywords):
        evidence.append("secondary_title")

    if contains_any(structured, rule.secondary_keywords):
        evidence.append("secondary_frontmatter")

    if evidence:
        return DomainAssociation(
            document=document,
            level=AssociationLevel.SECONDARY,
            evidence=tuple(evidence),
        )

    if contains_any(headings, rule.all_keywords):
        return DomainAssociation(
            document=document,
            level=AssociationLevel.MENTION,
            evidence=("controlled_heading",),
        )

    return None


def merge_association(
    current: DomainAssociation | None,
    candidate: DomainAssociation,
) -> DomainAssociation:
    if current is None:
        return candidate

    if ASSOCIATION_PRIORITY[candidate.level] > ASSOCIATION_PRIORITY[current.level]:
        return candidate

    if candidate.level == current.level:
        evidence = tuple(dict.fromkeys((*current.evidence, *candidate.evidence)))
        return DomainAssociation(
            document=current.document,
            level=current.level,
            evidence=evidence,
        )

    return current


def normalized_link_path(source: Document, target: str) -> str:
    if not target or target.startswith("#"):
        return ""

    target_path = (source.path.parent / target).as_posix()
    normalized = Path(target_path).as_posix()

    parts: list[str] = []
    for part in normalized.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)

    return "/".join(parts)


def resolve_link(
    source: Document,
    target: str,
    documents_by_path: dict[str, Document],
) -> bool:
    normalized = normalized_link_path(source, target)
    return bool(normalized) and normalized in documents_by_path


def detect_reference_recipes(audit: DomainAudit) -> list[Document]:
    if not audit.rule.reference_recipe_keywords:
        return []

    references: list[Document] = []
    expected = tuple(
        normalize(item)
        for item in audit.rule.reference_recipe_keywords
    )
    for document in audit.primary_by_type.get("receta", []):
        title = normalize(document.titulo)
        content = normalize(document.content)
        if (
            any(keyword in title for keyword in expected)
            or "implementacion de referencia" in content
        ):
            references.append(document)
    return references


def audit_knowledge(documents: list[Document]) -> list[DomainAudit]:
    documents_by_path = {
        document.relative_path: document
        for document in documents
    }
    auditable_documents = [
        document
        for document in documents
        if is_auditable_knowledge_document(document)
    ]
    audits: list[DomainAudit] = []

    for rule in KNOWLEDGE_RULES:
        association_by_path: dict[str, DomainAssociation] = {}

        # Primera pasada: evidencias propias del documento.
        for document in auditable_documents:
            association = classify_direct_association(document, rule)
            if association is not None:
                association_by_path[document.relative_path] = merge_association(
                    association_by_path.get(document.relative_path),
                    association,
                )

        # Segunda pasada: los recursos enlazados por documentos PRIMARY se
        # consideran conocimiento reutilizado del dominio.
        primary_documents = [
            association.document
            for association in association_by_path.values()
            if association.level == AssociationLevel.PRIMARY
        ]
        for source in primary_documents:
            source_type = normalize(source.tipo).replace(" ", "_")
            if source_type not in SECONDARY_EXPANSION_TYPES:
                continue

            for target in source.links:
                target_path = normalized_link_path(source, target)
                target_document = documents_by_path.get(target_path)
                if (
                    target_document is None
                    or not is_auditable_knowledge_document(target_document)
                ):
                    continue

                linked_association = DomainAssociation(
                    document=target_document,
                    level=AssociationLevel.SECONDARY,
                    evidence=(f"linked_from:{source.id or source.relative_path}",),
                )
                association_by_path[target_document.relative_path] = merge_association(
                    association_by_path.get(target_document.relative_path),
                    linked_association,
                )

        audit = DomainAudit(rule=rule)
        audit.associations = sorted(
            association_by_path.values(),
            key=lambda association: (
                -ASSOCIATION_PRIORITY[association.level],
                association.document.relative_path,
            ),
        )

        for association in audit.primary_associations:
            document = association.document
            document_type = document.tipo or "sin_tipo"
            audit.primary_by_type[document_type].append(document)

            internal_links = document.links
            audit.outgoing_links += len(internal_links)
            resolved = sum(
                1
                for target in internal_links
                if resolve_link(document, target, documents_by_path)
            )
            audit.resolved_outgoing_links += resolved
            if not internal_links:
                audit.orphan_documents.append(document)

        audit.reference_recipes = detect_reference_recipes(audit)
        audits.append(audit)

    return audits


def maturity_label(audit: DomainAudit) -> str:
    """
    Estimación prudente de madurez según la naturaleza del dominio.

    La cobertura estructural no equivale por sí sola a madurez editorial.
    """
    primary_count = len(audit.primary_associations)
    secondary_count = len(audit.secondary_associations)

    if audit.rule.kind == DomainKind.INGREDIENT:
        if primary_count == 0:
            return "🌱 Exploración"

        if secondary_count >= 1:
            return "🌿 Estructurado"

        return "🌱 Exploración"

    has_template = bool(audit.primary_by_type.get("plantilla"))
    has_recipe = bool(audit.primary_by_type.get("receta"))
    has_technique = bool(audit.primary_by_type.get("tecnica"))
    coverage = audit.structural_coverage

    if (
        coverage >= 80.0
        and has_template
        and has_recipe
        and has_technique
    ):
        return "🌳 Consolidado"

    if coverage >= 60.0 and has_recipe:
        return "🌿 Estructurado"

    if (
        audit.rule.kind == DomainKind.PATTERN
        and has_template
        and has_recipe
    ):
        return "🌿 Estructurado"

    return "🌱 Exploración"


def association_to_dict(association: DomainAssociation) -> dict:
    return {
        "path": association.document.relative_path,
        "id": association.document.id,
        "title": association.document.titulo,
        "type": association.document.tipo,
        "association": association.level.value,
        "evidence": list(association.evidence),
    }


def audit_to_dict(audit: DomainAudit) -> dict:
    return {
        "domain": audit.rule.key,
        "name": audit.rule.name,
        "maturity": maturity_label(audit),
        "primary_documents": audit.document_count,
        "associated_documents": audit.associated_document_count,
        "association_counts": {
            "PRIMARY": len(audit.primary_associations),
            "SECONDARY": len(audit.secondary_associations),
            "MENTION": len(audit.mention_associations),
        },
        "structural_coverage": round(audit.structural_coverage, 2),
        "types": dict(sorted(audit.type_counts.items())),
        "outgoing_links": audit.outgoing_links,
        "resolved_outgoing_links": audit.resolved_outgoing_links,
        "link_resolution_rate": (
            round(audit.link_resolution_rate, 2)
            if audit.link_resolution_rate is not None
            else None
        ),
        "orphan_documents": [
            document.relative_path
            for document in audit.orphan_documents
        ],
        "reference_recipes": [
            document.relative_path
            for document in audit.reference_recipes
        ],
        "associations": [
            association_to_dict(association)
            for association in audit.associations
        ],
    }


def render_markdown(audits: list[DomainAudit]) -> str:
    today = date.today().isoformat()
    lines = [
        "---",
        "id: REPORT-KNOWLEDGE-AUDIT",
        "tipo: informe",
        "titulo: Auditoría automática del conocimiento",
        "version: 1.6.0",
        "estado: generado",
        f"ultima_revision: {today}",
        "tags:",
        "  - dominios",
        "  - auditoria",
        "  - generado",
        "---",
        "",
        "# Auditoría automática del conocimiento",
        "",
        "## Vista: dominios culinarios",
        "",
        "> Este archivo es generado por `tools/audit_knowledge.py`. No debe editarse manualmente.",
        "",
        "## Alcance de las métricas",
        "",
        "La cobertura indicada es **estructural y preliminar**: mide la presencia de tipos documentales esperados. No evalúa por sí sola calidad culinaria, exhaustividad ni corrección semántica.",
        "",
        "# Resumen",
        "",
        "| Dominio | Madurez automática | PRIMARY | SECONDARY | MENTION | Cobertura estructural | Enlaces resueltos | Huérfanos |",
        "|---|:---:|---:|---:|---:|---:|---:|---:|",
    ]

    for audit in audits:
        link_rate = (
            f"{audit.link_resolution_rate:.0f} %"
            if audit.link_resolution_rate is not None
            else "N/A"
        )
        lines.append(
            f"| {audit.rule.name} | {maturity_label(audit)} | "
            f"{len(audit.primary_associations)} | "
            f"{len(audit.secondary_associations)} | "
            f"{len(audit.mention_associations)} | "
            f"{audit.structural_coverage:.0f} % | {link_rate} | "
            f"{len(audit.orphan_documents)} |"
        )

    for audit in audits:
        link_rate = (
            f"{audit.link_resolution_rate:.0f} %"
            if audit.link_resolution_rate is not None
            else "N/A"
        )
        lines.extend(
            [
                "",
                "---",
                "",
                f"# Dominio: {audit.rule.name}",
                "",
                f"**Madurez automática:** {maturity_label(audit)}  ",
                f"**Documentos PRIMARY:** {len(audit.primary_associations)}  ",
                f"**Documentos SECONDARY:** {len(audit.secondary_associations)}  ",
                f"**Documentos MENTION:** {len(audit.mention_associations)}  ",
                f"**Cobertura estructural:** {audit.structural_coverage:.0f} %  ",
                f"**Resolución de enlaces:** {link_rate}",
                "",
                "## Distribución por tipo",
                "",
                "| Tipo | Cantidad |",
                "|---|---:|",
            ]
        )

        for document_type, count in sorted(audit.type_counts.items()):
            lines.append(f"| `{document_type}` | {count} |")

        lines.extend(["", "## Implementaciones de referencia detectadas", ""])
        if audit.reference_recipes:
            for document in sorted(audit.reference_recipes, key=lambda item: item.graph_label):
                lines.append(f"- `{document.id or 'sin-id'}` · {document.titulo} (`{document.relative_path}`)")
        else:
            lines.append("- No detectadas automáticamente.")

        for heading, associations in (
            ("Documentos de autoridad (PRIMARY)", audit.primary_associations),
            ("Conocimiento reutilizado (SECONDARY)", audit.secondary_associations),
            ("Menciones contextuales (MENTION)", audit.mention_associations),
        ):
            lines.extend(["", f"## {heading}", ""])
            if associations:
                for association in associations:
                    evidence = ", ".join(association.evidence)
                    lines.append(
                        f"- `{association.document.id or 'sin-id'}` · "
                        f"{association.document.titulo} "
                        f"(`{association.document.relative_path}`) "
                        f"— evidencia: `{evidence}`"
                    )
            else:
                lines.append("- Ninguno.")

        lines.extend(["", "## Documentos sin referencias salientes", ""])
        if audit.orphan_documents:
            for document in sorted(audit.orphan_documents, key=lambda item: item.relative_path):
                lines.append(f"- `{document.id or 'sin-id'}` · `{document.relative_path}`")
        else:
            lines.append("- Ninguno.")

        missing_types = [
            document_type
            for document_type in audit.rule.expected_types
            if not audit.primary_by_type.get(document_type)
        ]
        lines.extend(["", "## Tipos documentales no representados", ""])
        if missing_types:
            for document_type in missing_types:
                lines.append(f"- `{document_type}`")
        else:
            lines.append("- Ninguno.")

    lines.extend(
        [
            "",
            "---",
            "",
            "# Notas",
            "",
            "- La vista se limita a documentos culinarios fuente y excluye README, gestión, arquitectura, especificaciones e informes.",
            "- La cobertura y la madurez automáticas se calculan exclusivamente con asociaciones `PRIMARY`.",
            "- Las asociaciones `SECONDARY` representan conocimiento reutilizado y `MENTION` contexto incidental.",
            "- Un documento puede relacionarse con varios dominios con distintos niveles de asociación.",
            "- En dominios de ingrediente, solo los documentos `ingrediente` de sus rutas de autoridad pueden ser `PRIMARY`.",
            "- Las recetas de carpetas temáticas de ingredientes se clasifican como `SECONDARY`.",
            "- La expansión por enlaces parte únicamente de bases, técnicas, plantillas y recetas `PRIMARY`.",
            "- Las recetas transversales pueden ser `PRIMARY` de un patrón cuando su título es inequívoco o están declaradas como referencia.",
            "- Las demás recetas con ruta canónica externa permanecen como `SECONDARY` del patrón.",
            "- La madurez automática se adapta a `PATTERN`, `CATEGORY` e `INGREDIENT`.",
            "- `MENTION` solo analiza encabezados culinarios controlados; no recorre todo el cuerpo.",
            "- Los tipos esperados se adaptan a la naturaleza del dominio.",
            "- `PRIMARY` prioriza rutas, dominio explícito, títulos controlados y enlaces a plantillas de autoridad.",
            "- Las reglas de dominio se mantienen en `KNOWLEDGE_RULES` dentro de `tools/audit_knowledge.py`.",
            "- La madurez automática es orientativa y no sustituye la revisión culinaria humana.",
            "",
        ]
    )
    return "\n".join(lines)


def print_console(audits: list[DomainAudit]) -> None:
    print()
    print("NovaCoquinaria - Auditoría del conocimiento")
    print("---------------------------------------------")
    print()

    for audit in audits:
        link_rate = (
            f"{audit.link_resolution_rate:>5.1f}%"
            if audit.link_resolution_rate is not None
            else "  N/A "
        )
        print(
            f"{audit.rule.name:<24} "
            f"P={len(audit.primary_associations):>3}  "
            f"S={len(audit.secondary_associations):>3}  "
            f"M={len(audit.mention_associations):>3}  "
            f"cobertura={audit.structural_coverage:>5.1f}%  "
            f"enlaces={link_rate}  "
            f"huérfanos={len(audit.orphan_documents):>2}  "
            f"{maturity_label(audit)}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audita el conocimiento del SGCC mediante distintas vistas analíticas."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPORT_DEFAULT,
        help=f"Informe Markdown relativo al repositorio (por defecto: {REPORT_DEFAULT}).",
    )
    parser.add_argument(
        "--json-output",
        type=Path,
        default=JSON_DEFAULT,
        help=f"Informe JSON relativo al repositorio (por defecto: {JSON_DEFAULT}).",
    )
    parser.add_argument(
        "--no-write",
        action="store_true",
        help="Muestra el resumen sin escribir informes.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    documents = load_documents()
    audits = audit_knowledge(documents)
    print_console(audits)

    if args.no_write:
        return 0

    markdown_path = ROOT_DIR / args.output
    json_path = ROOT_DIR / args.json_output
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    markdown_path.write_text(render_markdown(audits), encoding="utf-8")
    json_path.write_text(
        json.dumps([audit_to_dict(audit) for audit in audits], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print()
    print_ok(f"Informe Markdown generado: {markdown_path.relative_to(ROOT_DIR).as_posix()}")
    print_ok(f"Informe JSON generado: {json_path.relative_to(ROOT_DIR).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())