"""CRR-D04: bounded recognition proposals, not accepted culinary knowledge."""
import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import unicodedata

from common import ROOT_DIR
from extract_recipe_metadata import build_projection, serialize, snapshot_bytes
from extract_recipe_ingredients import plain

VERSION = "0.1.0"
FAMILY = {"choice": "P02", "optional": "P03", "preparation": "P04", "adjustment": "P05"}
BLOCK = re.compile(r"\b(?:y|e|o|u|no|sin|si|según|cuando|opcional(?:es|mente)?)\b")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def norm(text):
    return " ".join(unicodedata.normalize("NFC", plain(text)).casefold().split()).rstrip(" ;.")


def proposal(entry):
    text = norm(entry["raw"])
    match = re.fullmatch(r"(.+?)(?:\s+\(opcional(?:es)?\)|,\s*opcional(?:es)?|\s+opcional(?:es)?)", text)
    if match and not BLOCK.search(match[1]) and "," not in match[1] and ";" not in match[1]:
        return {"kind": "optional", "presence": "optional", "scope": "whole_occurrence"}
    match = re.fullmatch(r"(.+?)[, ]+\s*(descongelad[oa]s? si procede)", text)
    if match and not BLOCK.search(match[1]):
        return {"kind": "preparation", "presence": "required", "condition": match[2]}
    match = re.fullmatch(r"(.+?),\s*((?:reponer|añadir) si hace falta)", text)
    q = entry.get("quantity", {})
    if match and not BLOCK.search(match[1]) and q.get("status") in {"exact", "range"}:
        try:
            positive = 0 < Fraction(q["min"]) <= Fraction(q["max"])
        except (KeyError, ValueError, TypeError, ZeroDivisionError):
            positive = False
        if positive:
            return {"kind": "adjustment", "presence": "required",
                    "condition": match[2], "additional_quantity": None}
    return None


def groups(lines, entries):
    found = []
    for i, line in enumerate(lines):
        if not re.fullmatch(r"#{1,6}\s+guarnición", norm(line)):
            continue
        end = i+1
        while end < len(lines) and not re.match(r"^#{1,6}\s", lines[end]) and not re.fullmatch(r"\s*(?:---+|\*\*\*+)\s*", lines[end]):
            end += 1
        content = [(j+1, lines[j]) for j in range(i+1, end) if lines[j].strip()]
        if len(content) < 3 or norm(content[0][1]) != "a elegir:":
            continue
        if not all(re.match(r"^[-*+]\s+\S", line) for _, line in content[1:]):
            continue
        expected = [n for n, _ in content[1:]]
        positions = [p for p, e in enumerate(entries) if
                     e["source_location"]["start_line"] in expected]
        if [entries[p]["source_location"]["start_line"] for p in positions] != expected:
            continue
        if any(norm(entries[p].get("group") or "") != "guarnición" for p in positions):
            continue
        found.append({"positions": positions, "kind": "choice", "presence": "unknown",
                      "role": "accompaniment", "cardinality": None,
                      "evidence_lines": [i+1] + [n for n, _ in content]})
    return found


def partition(entries, candidates, lines):
    counts = Counter(p for c in candidates for p in c["positions"])
    require(all(type(p) is int and 0 <= p < len(entries) for p in counts), "Invalid reference")
    require(all(len(c["positions"]) == len(set(c["positions"])) and c["positions"] for c in candidates),
            "Invalid positions")
    conflicts = sorted(p for p, n in counts.items() if n > 1)
    roots = []
    used = set()
    for c in candidates:
        if any(p in conflicts for p in c["positions"]):
            continue
        root = deepcopy(c)
        root["rule"] = "CRR-R" + FAMILY[c["kind"]][1:]
        root["version"] = VERSION
        root["evidence"] = [{"line": n, "text": lines[n-1]} for n in root.pop("evidence_lines")]
        root["tree"] = {"type": "choice", "presence": "unknown", "role": "accompaniment",
                        "children": [{"type": "opaque", "presence": "unknown", "label": entries[p]["raw"]}
                                     for p in root["positions"]]} if c["kind"] == "choice" else {
                        "type": "opaque", "presence": "unknown", "label": entries[c["positions"][0]]["raw"]}
        roots.append(root)
        used.update(c["positions"])
    for p, e in enumerate(entries):
        if p not in used:
            roots.append({"positions": [p], "tree": {"type": "opaque", "presence": "unknown", "label": e["raw"]},
                          "reason": "conflict" if p in conflicts else "no_supported_pattern"})
    require(sorted(p for root in roots for p in root["positions"]) == list(range(len(entries))), "Invalid partition")
    return sorted(roots, key=lambda x: x["positions"][0])


def recognize(record, raw):
    require(hashlib.sha256(raw).hexdigest() == record["source"]["sha256"], "Source digest mismatch")
    lines = raw.decode("utf-8-sig").splitlines()
    entries = record["ingredients"]
    candidates = groups(lines, entries)
    for p, entry in enumerate(entries):
        loc = entry["source_location"]
        n = loc["start_line"]
        require(1 <= n <= loc["end_line"] <= len(lines), "Invalid source location")
        result = proposal(entry)
        if result:
            candidates.append({**result, "positions": [p], "evidence_lines": [n]})
    return {"recipe_id": record["id"], "source": deepcopy(record["source"]),
            "occurrences": deepcopy(entries), "roots": partition(entries, candidates, lines)}


def evaluate(results, fixture, sources):
    records = {r["recipe_id"]: r for r in results}
    split = {}
    seen = set()
    cases = []
    for case in fixture["cases"]:
        rid = case["recipe_id"]
        require(case["id"] not in seen and rid in records, "Invalid case reference")
        seen.add(case["id"])
        require(split.setdefault(rid, case["split"]) == case["split"], "Overlapping splits")
        record = records[rid]
        require(record["source"]["path"] == case["path"], "Path mismatch")
        lines = sources[case["path"]].decode("utf-8-sig").splitlines()
        positions = []
        for ev in case["evidence"]:
            n = ev["line"]
            require(type(n) is int and 1 <= n <= len(lines) and lines[n-1] == ev["text"], "Evidence mismatch")
            matches = [p for p, e in enumerate(record["occurrences"]) if e["source_location"]["start_line"] == n]
            if re.match(r"^\s*[-*+]\s+", ev["text"]):
                require(len(matches) == 1, "Occurrence reference missing or ambiguous")
            positions.extend(matches)
        require(positions and len(set(positions)) == len(positions), "Invalid case positions")
        expected = case["expected_semantic"]
        observed = [r for r in record["roots"] if "kind" in r and set(r["positions"]) & set(positions)]
        by_pos = {p: r for r in observed for p in r["positions"]}
        desired_presence = {"optional": "optional", "preparation": "required", "adjustment": "required", "choice": "unknown"}
        if expected == "choice":
            correct = len(observed) == 1 and observed[0]["kind"] == "choice" and observed[0]["positions"] == positions and observed[0]["presence"] == "unknown" and observed[0]["role"] == "accompaniment" and observed[0]["cardinality"] is None
        elif expected in desired_presence:
            correct = all(p in by_pos and by_pos[p]["kind"] == expected and by_pos[p]["positions"] == [p]
                          and by_pos[p]["presence"] == desired_presence[expected] for p in positions)
        else:
            correct = expected == "abstain" and not observed
        status = ("true_negative" if expected == "abstain" else "hit") if correct else (
            "false_positive" if observed else "omission")
        cases.append({"id":case["id"], "split":case["split"], "family":case["family"],
                      "recipe_id":rid, "expected":expected, "positions":positions,
                      "observed":[{"kind":r["kind"],"positions":r["positions"],"presence":r["presence"]} for r in observed],
                      "legacy_optionality":[record["occurrences"][p]["optionality"] for p in positions],
                      "status":status})
    return cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = (ROOT_DIR / args.output).resolve()
    require(output.is_relative_to((ROOT_DIR / "site").resolve()), "Output outside site")
    raw = (ROOT_DIR / "tools/fixtures/requirements_recognition_cases.json").read_bytes()
    fixture = json.loads(raw)
    projection = build_projection(ROOT_DIR, fixture["source_commit"])
    before = serialize(projection)
    require(hashlib.sha256(before.encode()).hexdigest() == fixture["projection_sha256"], "Projection mismatch")
    sources = {r["source"]["path"]: snapshot_bytes(ROOT_DIR, fixture["source_commit"], r["source"]["path"])
               for r in projection["recipes"]}
    def run():
        return [recognize(r, sources[r["source"]["path"]]) for r in projection["recipes"]]
    results = run()
    require(results == run() and before == serialize(projection), "Mutation or nondeterminism")
    cases = evaluate(results, fixture, sources)
    negatives = [{"raw": text, "proposal": proposal({"raw":text})} for text in fixture["synthetic_negatives"]]
    roots = [root for r in results for root in r["roots"] if "kind" in root]
    summary = {k:dict(Counter(c["status"] for c in cases if c["split"] == k)) for k in ("adjustment","holdout")}
    report = {"version":VERSION, "source_commit":fixture["source_commit"], "projection_sha256":fixture["projection_sha256"],
              "fixture_sha256":hashlib.sha256(raw).hexdigest(), "recipes":len(results),
              "occurrences":sum(len(r["occurrences"]) for r in results),
              "proposed_occurrences":sum(len(r["positions"]) for r in roots),
              "proposed_roots":dict(Counter(r["kind"] for r in roots)),
              "summary":summary,"cases":cases,"synthetic_negatives":negatives,
              "results":results,"scope":"Proposals; corpus-wide correctness unmeasured"}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k not in ("results","cases","synthetic_negatives")},sort_keys=True))
    print(json.dumps([{"id":c["id"],"status":c["status"]} for c in cases],sort_keys=True))
    print("Synthetic false positives:",sum(n["proposal"] is not None for n in negatives))


if __name__ == "__main__":
    main()
