"""Inventory recurring editorial boilerplate in canonical recipe Markdown.

Textual signals only: a match is not proof of an editorial or culinary defect.
No recipe content is modified and this command never fails for detected signals.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import unicodedata

from audit_inventory import RECIPE_MODULES
from common import ROOT_DIR

SECTIONS = ("Puntos críticos", "Diagnóstico", "Conservación")
# Deliberately narrow, observed fragments; not a general semantic classifier.
RULES = {
    "E01_GENERIC_PROTEINS": (
        "carnes, pescados, crustaceos, huevos o lacteos",
        "carnes, gambas y huevos",
        "carnes, pescado, mariscos o verduras cocidas",
    ),
    "E02_OTHER_PREPARATIONS": (
        "mantener el helado congelado hasta el montaje",
        "maceraciones caseras con vinagre",
        "en el caso de arroz cocido",
        "el arroz ya cocido se enfria rapidamente",
    ),
    "E03_GENERIC_DIAGNOSTICS": (
        "infusion larga, hierba intensa o extraccion caliente excesiva",
        "azucar adicional o fruta muy madura",
        "soja, miso u otros fermentados concentrados",
        "salsa demasiado espesa | reduccion excesiva o demasiado almidon",
        "ingredientes humedos y sin dorado | sarten sobrecargada",
    ),
    "E04_GENERIC_CONSERVATION": (
        "las preparaciones con carnes, pescados, crustaceos, huevos o lacteos",
        "las bebidas con fruta fresca triturada, lacteos o ingredientes hidratados",
        "refrigerar sin demora las bebidas con fruta cortada, lacteos o extractos vegetales",
    ),
}


def normalize(text: str) -> str:
    lower = unicodedata.normalize("NFKD", text.casefold())
    return "".join(c for c in lower if not unicodedata.combining(c))


def sections(markdown: str) -> list[tuple[str, int, str]]:
    """Return only lines in audited sections, excluding other recipe sections."""
    active = None
    result = []
    for number, line in enumerate(markdown.splitlines(), 1):
        match = re.match(r"^## (.+?)\s*$", line)
        if match:
            active = match.group(1) if match.group(1) in SECTIONS else None
        elif active and line.strip():
            result.append((active, number, line))
    return result


def scan_one(path: str, markdown: str) -> list[dict]:
    matches = []
    for section, number, line in sections(markdown):
        comparison = normalize(line)
        for rule, fragments in RULES.items():
            if any(fragment in comparison for fragment in fragments):
                matches.append({
                    "path": path, "line": number, "section": section,
                    "signal": rule, "text": line.strip(),
                })
    return matches


def build_report(documents: dict[str, str], source_commit: str) -> dict:
    findings = []
    for path, markdown in sorted(documents.items()):
        findings.extend(scan_one(path, markdown))
    counts = Counter(item["signal"] for item in findings)
    by_module = Counter(item["path"].split("/", 1)[0] for item in findings)
    return {
        "stage": "editorial_text_signals",
        "version": "0.1.0",
        "source_commit": source_commit,
        "scope": "Signals only; candidate manual review, not confirmed defects",
        "recipes_scanned": len(documents),
        "flagged_recipes": len({x["path"] for x in findings}),
        "occurrences": len(findings),
        "by_signal": dict(sorted(counts.items())),
        "by_module": dict(sorted(by_module.items())),
        "findings": findings,
    }


def tracked_recipes(root: Path, commit: str) -> dict[str, str]:
    paths = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", commit], cwd=root,
        text=True,
    ).splitlines()
    return {
        path: (root / path).read_text(encoding="utf-8-sig")
        for path in paths
        if path.endswith(".md") and path.split("/", 1)[0] in RECIPE_MODULES
        and Path(path).name != "README.md"
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    output = (ROOT_DIR / args.output).resolve()
    if not output.is_relative_to((ROOT_DIR / "site").resolve()):
        parser.error("--output must be within site/")
    commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT_DIR, text=True,
    ).strip()
    report = build_report(tracked_recipes(ROOT_DIR, commit), commit)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Editorial signals: {report['occurrences']} occurrences in "
          f"{report['flagged_recipes']}/{report['recipes_scanned']} recipes "
          f"(candidates, not defects)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
