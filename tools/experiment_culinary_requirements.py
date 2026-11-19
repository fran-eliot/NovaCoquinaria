"""CRM-D04B: represent reviewed annotations, not automatic parsing."""
import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path

from common import ROOT_DIR
from extract_recipe_metadata import build_projection, serialize, snapshot_bytes

FIXTURES = ROOT_DIR / "tools/fixtures"
PRESENCE = {"required", "optional", "conditional", "unknown"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_node(node, depth=0):
    require(isinstance(node, dict) and depth <= 8, "Invalid node")
    require(set(node) <= {"type", "presence", "label", "children", "role",
                         "conditions", "qualifiers", "quantity_scope", "adaptation"}, "Unknown node field")
    kind = node.get("type")
    require(kind in {"atom", "all", "any", "choice", "opaque"}, "Invalid type")
    require(node.get("presence") in PRESENCE, "Invalid presence")
    require(node.get("role", "unknown") in {"base", "accompaniment", "unknown"}, "Invalid role")
    children = node.get("children", [])
    require(isinstance(children, list), "Invalid children")
    if kind in {"atom", "opaque"}:
        require(not children and isinstance(node.get("label"), str) and node["label"].strip(), "Invalid leaf")
    else:
        require(len(children) >= 2 and "label" not in node, "Invalid arity")
    require(kind != "opaque" or node["presence"] == "unknown", "Opaque assertion")
    require(kind != "choice" or node["presence"] == "unknown", "Unspecified choice scope")
    conditions = node.get("conditions", [])
    require(isinstance(conditions, list), "Invalid conditions")
    for c in conditions:
        require(isinstance(c, dict) and set(c) == {"scope", "text"} and
                c["scope"] in {"preparation", "adjustment", "presence", "unknown"} and
                isinstance(c["text"], str) and c["text"].strip(), "Invalid condition")
    require(node["presence"] != "conditional" or any(c["scope"] == "presence" for c in conditions),
            "Missing presence condition")
    require(node.get("quantity_scope") in {None, "shared", "base"}, "Invalid quantity scope")
    require(not ("quantity_scope" in node and node.get("adaptation")), "Adaptation dose not established")
    require(node.get("quantity_scope") != "shared" or kind == "any", "Invalid shared quantity")
    require(node.get("quantity_scope") != "base" or kind == "atom", "Invalid base quantity")
    require(type(node.get("adaptation", False)) is bool, "Invalid adaptation")
    qualifiers = node.get("qualifiers", [])
    require(isinstance(qualifiers, list) and all(isinstance(q, str) and q.strip() for q in qualifiers),
            "Invalid qualifiers")
    for child in children:
        validate_node(child, depth+1)


def shape(node):
    return node["type"] + ("(" + ",".join(shape(c) for c in node["children"]) + ")"
                           if node.get("children") else "")


def represent(projection, fixture, read_source):
    require(projection["source_commit"] == fixture["source_commit"], "Corpus mismatch")
    require(hashlib.sha256(serialize(projection).encode()).hexdigest() ==
            fixture["projection_sha256"], "Projection mismatch")
    records = {r["id"]: r for r in projection["recipes"]}
    roots = {}
    seen = set()
    ids = set()
    for case in fixture["cases"]:
        rid = case["recipe_id"]
        require(case["id"] not in ids and rid in records, "Invalid case reference")
        ids.add(case["id"])
        record = records[rid]
        source = record["source"]
        require(case["path"] == source["path"], "Path mismatch")
        raw = read_source(source["path"])
        require(hashlib.sha256(raw).hexdigest() == source["sha256"], "Source mismatch")
        lines = raw.decode("utf-8-sig").splitlines()
        positions = case["positions"]
        require(isinstance(positions, list) and positions and
                all(type(p) is int and 0 <= p < len(record["ingredients"]) for p in positions),
                "Invalid positions")
        require(len(set(positions)) == len(positions), "Duplicate positions")
        refs = {(rid, p) for p in positions}
        require(not refs & seen, "Overlapping roots")
        seen.update(refs)
        evidence = case["evidence"]
        require(isinstance(evidence, list) and evidence, "Missing evidence")
        for e in evidence:
            require(type(e["line"]) is int and 1 <= e["line"] <= len(lines)
                    and lines[e["line"]-1] == e["text"], "Evidence mismatch")
        require(all(record["ingredients"][p]["source_location"]["start_line"] in
                    {e["line"] for e in evidence} for p in positions), "Missing occurrence evidence")
        validate_node(case["tree"])
        roots.setdefault(rid, []).append({k: deepcopy(case[k]) for k in
                                         ("id", "positions", "evidence", "tree")})
    result = []
    for rid, record in sorted(records.items()):
        annotated = roots.get(rid, [])
        remaining = [p for p in range(len(record["ingredients"])) if (rid, p) not in seen]
        opaque = [{"positions": [p], "tree": {"type": "opaque", "presence": "unknown",
                                             "label": record["ingredients"][p]["raw"]}}
                  for p in remaining]
        all_roots = sorted(annotated + opaque, key=lambda x: x["positions"][0])
        require(sorted(p for root in all_roots for p in root["positions"]) ==
                list(range(len(record["ingredients"]))), "Partition mismatch")
        result.append({"recipe_id": rid, "source": deepcopy(record["source"]),
                       "occurrences": deepcopy(record["ingredients"]), "roots": all_roots})
    return result


def compare(results, expectations):
    observed = {root["id"]: {"shape": shape(root["tree"]), "presence": root["tree"]["presence"]}
                for record in results for root in record["roots"] if "id" in root}
    expected = {e["id"]: {k: e[k] for k in ("shape", "presence")} for e in expectations}
    require(len(expected) == len(expectations) and expected == observed, "Expectation mismatch")
    # Flat baseline: one annotation per occurrence, no nested/group structure.
    cases = []
    for record in results:
        for root in record["roots"]:
            if "id" not in root:
                continue
            tree = root["tree"]
            flat = len(root["positions"]) == 1 and tree["type"] == "atom"
            cases.append({"id": root["id"], **observed[root["id"]],
                          "flat_representable": flat, "hybrid_representable": True})
    return sorted(cases, key=lambda x: x["id"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = (ROOT_DIR / args.output).resolve()
    require(output.is_relative_to((ROOT_DIR / "site").resolve()), "Output outside site")
    raw = (FIXTURES / "requirements_reviewed_annotations.json").read_bytes()
    exp = (FIXTURES / "requirements_model_expectations.json").read_bytes()
    fixture, expectations = json.loads(raw), json.loads(exp)
    projection = build_projection(ROOT_DIR, fixture["source_commit"])
    before = serialize(projection)
    read = lambda p: snapshot_bytes(ROOT_DIR, fixture["source_commit"], p)
    results = represent(projection, fixture, read)
    require(results == represent(projection, fixture, read) and before == serialize(projection),
            "Mutation or nondeterminism")
    cases = compare(results, expectations)
    roots = [root for r in results for root in r["roots"]]
    report = {"source_commit": fixture["source_commit"], "projection_sha256": fixture["projection_sha256"],
              "annotations_sha256": hashlib.sha256(raw).hexdigest(),
              "expectations_sha256": hashlib.sha256(exp).hexdigest(),
              "recipes": len(results), "occurrences": sum(len(r["occurrences"]) for r in results),
              "annotated_occurrences": sum(len(r["positions"]) for r in roots if "id" in r),
              "opaque_occurrences": sum(len(r["positions"]) for r in roots if "id" not in r),
              "root_types": dict(Counter(r["tree"]["type"] for r in roots)),
              "flat_cases": sum(c["flat_representable"] for c in cases),
              "hybrid_cases": len(cases), "cases": cases, "results": results,
              "scope": "Manual reviewed annotations; no automatic semantic recognition"}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k not in ("results", "cases")}, sort_keys=True))


if __name__ == "__main__":
    main()
