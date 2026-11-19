"""CRM-D02: inventory of textual signals, not semantic defects."""
import argparse
from collections import Counter, defaultdict
import hashlib
import itertools
import json
from pathlib import Path
import re

from common import ROOT_DIR
from extract_recipe_metadata import build_projection, serialize, snapshot_bytes
from extract_recipe_ingredients import plain, normalized

CORPUS = "c0dd020dea003d8a4f7a0278a43f30d81501a7f0"
PROJECTION = "d72cb4cb48f8ab112d3f60003bb8a20acfe295925756e6456b12bf7b2648a89c"
SIGNALS = ("S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08")


def signals(entry):
    text = normalized(plain(entry["raw"]))
    group = normalized(plain(entry["group"] or ""))
    result = set()
    if re.search(r"\b(o|u)\b", text.strip(" ;.,:")):
        result.add("S01")
    if re.search(r"\b(y|e)\b", text):
        result.add("S03")
    if re.search(r"\bsi\b|\bsegun\b|\ben caso de\b|\bcuando\b", text):
        result.add("S04")
    if re.search(r"\bopcional(?:es|mente)?\b", text + " " + group):
        result.add("S05")
    if re.search(r"\bacompan(?:amiento|amientos|ar)\b|\bguarnici(?:on|ones)\b", text + " " + group):
        result.add("S06")
    if re.search(r"\b(?:fresc[oa]s?|congelad[oa]s?|escurrid[oa]s?|picad[oa]s?|pelad[oa]s?|"
                 r"rallad[oa]s?|laminad[oa]s?|molid[oa]s?|en conserva|"
                 r"en polvo|precocid[oa]s?|descorazonad[oa]s?|machacad[oa]s?)\b", text):
        result.add("S07")
    if entry["quantity"]["status"] == "qualitative":
        result.add("S08")
    return result


def trailing_connector(entry):
    return bool(re.search(r"\b(?:o|u)\s*$", normalized(plain(entry["raw"])).rstrip(" ;.,:")))


def inventory(projection, read_source):
    rows = []
    edges = []
    unresolved = []
    counts = Counter()
    recipe_counts = defaultdict(set)
    overlap = Counter()
    by_optionality = defaultdict(Counter)
    modules = defaultdict(Counter)
    group_counts = Counter()
    source_count = 0
    for record in sorted(projection["recipes"], key=lambda r: r["id"]):
        rid, source = record["id"], record["source"]
        raw = read_source(source["path"])
        if hashlib.sha256(raw).hexdigest() != source["sha256"]:
            raise ValueError("Source digest mismatch: " + rid)
        lines = raw.decode("utf-8-sig").splitlines()
        source_count += 1
        entries = record["ingredients"]
        flags = [signals(e) for e in entries]
        for i, entry in enumerate(entries):
            loc = entry["source_location"]
            start, end = loc["start_line"], loc["end_line"]
            if not 1 <= start <= end <= len(lines):
                raise ValueError("Invalid location: " + rid)
            if trailing_connector(entry):
                flags[i].discard("S01")
                next_entry = entries[i+1] if i+1 < len(entries) else None
                next_line = next_entry["source_location"]["start_line"] if next_entry else None
                # Only direct adjacent projected lines in the same group; no inference.
                if next_entry and next_entry["group"] == entry["group"] and next_line == end + 1:
                    flags[i].add("S02")
                    flags[i+1].add("S02")
                    edges.append({"recipe_id": rid, "path": source["path"],
                                  "positions": [i, i+1], "lines": [end, next_line]})
                else:
                    unresolved.append({"recipe_id": rid, "path": source["path"],
                                       "position": i, "line": end})
        for i, (entry, found) in enumerate(zip(entries, flags)):
            counts["occurrences"] += 1
            group_counts[entry["group"] or "(none)"] += 1
            if not found:
                continue
            counts["flagged_occurrences"] += 1
            loc = entry["source_location"]
            row = {"recipe_id": rid, "path": source["path"], "position": i,
                   "source_location": loc, "source_lines": lines[loc["start_line"]-1:loc["end_line"]],
                   "raw": entry["raw"], "group": entry["group"], "name": entry["name"],
                   "optionality": entry["optionality"], "resolution": entry["resolution"],
                   "ingredient_id": entry["ingredient_id"], "quantity": entry["quantity"],
                   "signals": sorted(found)}
            rows.append(row)
            for flag in found:
                recipe_counts[flag].add(rid)
                by_optionality[flag][entry["optionality"]] += 1
                modules[record["physical_module"] or "(root)"][flag] += 1
            for a, b in itertools.combinations(sorted(found), 2):
                overlap[a + "/" + b] += 1
    return {"stage": "culinary_requirements_signal_inventory", "version": "0.1.0",
            "source_commit": projection["source_commit"], "scope": "Signals only; not defects or interpreted requirements",
            "recipes": len(projection["recipes"]), "verified_sources": source_count,
            "occurrences": counts["occurrences"], "flagged_occurrences": counts["flagged_occurrences"],
            "flagged_recipes": len({r["recipe_id"] for r in rows}),
            "by_signal": {s: {"occurrences": sum(by_optionality[s].values()),
                              "recipes": len(recipe_counts[s]),
                              "optionality": dict(sorted(by_optionality[s].items()))} for s in SIGNALS},
            "overlap": dict(sorted(overlap.items())), "by_module": dict(sorted(modules.items())),
            "groups": dict(sorted(group_counts.items())), "adjacent_edges": edges,
            "unresolved_trailing_connectors": unresolved, "rows": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = (ROOT_DIR / args.output).resolve()
    if not output.is_relative_to((ROOT_DIR / "site").resolve()):
        parser.error("Output must be under site/")
    projection = build_projection(ROOT_DIR, CORPUS)
    digest = hashlib.sha256(serialize(projection).encode("utf-8")).hexdigest()
    if digest != PROJECTION:
        raise ValueError("Projection digest mismatch")
    read = lambda path: snapshot_bytes(ROOT_DIR, CORPUS, path)
    report = inventory(projection, read)
    if report != inventory(projection, read):
        raise ValueError("Non-deterministic inventory")
    report["projection_sha256"] = digest
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
                      encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k not in
                      ("rows", "groups", "by_module", "adjacent_edges", "unresolved_trailing_connectors")},
                     ensure_ascii=False, sort_keys=True))
    print("Adjacent edges:", len(report["adjacent_edges"]),
          "Unresolved trailing connectors:", len(report["unresolved_trailing_connectors"]))


if __name__ == "__main__":
    main()
