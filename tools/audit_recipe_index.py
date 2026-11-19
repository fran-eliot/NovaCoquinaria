"""Contraste independiente de la vista 0.2.0 contra su proyección y Git."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import subprocess
import unicodedata

from common import ROOT_DIR


def check(condition, message):
    if not condition:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def normalize(value):
    return unicodedata.normalize("NFC", " ".join(value.casefold().split()))


def git_bytes(commit, path):
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT_DIR)


def audit(projection_raw, index_raw, source_reader=git_bytes):
    projection, index = json.loads(projection_raw), json.loads(index_raw)
    commit = projection["source_commit"]
    check(index["source_commit"] == commit and
          index["projection_sha256"] == sha(projection_raw), "Procedencia de proyección")
    check((index["index_version"], index["stage"]) ==
          ("0.2.0", "recipe_index_ingredients_preview"), "Versión de índice")
    for field in ("contract_version", "extractor_version"):
        check(index[field] == projection[field], f"Cabecera: {field}")
    recipes = projection["recipes"]
    records = {r["id"]: r for r in recipes}
    check(len(records) == len(recipes) == projection["inventory"]["recipe_documents"],
          "Inventario de origen")
    check(index["records"] == records, "Registros alterados o incompletos")
    paths = {r["source"]["path"]: r["id"] for r in recipes}
    check(len(paths) == len(recipes) and index["by_path"] == paths, "Rutas")
    titles = defaultdict(list)
    facets = {k: defaultdict(list) for k in
              ("physical_module", "category", "document_status", "evidence_status")}
    expected = {k: defaultdict(list) for k in
                ("by_text", "by_explicit_id", "by_candidate_id")}
    resolution, statuses = Counter(), Counter()
    total = candidate_occurrences = 0
    for identity, record in sorted(records.items()):
        source = record["source"]
        check(source["commit"] == commit and
              sha(source_reader(commit, source["path"])) == source["sha256"],
              f"Huella de fuente: {identity}")
        titles[normalize(record["title"])].append(identity)
        for field, value in (("physical_module", record["physical_module"]),
                             ("category", record["category"]),
                             ("document_status", record["metadata"].get("estado")),
                             ("evidence_status", record["evidence"]["status"])):
            if value is not None:
                facets[field][value].append(identity)
        for pos, entry in enumerate(record["ingredients"]):
            total += 1
            resolution[entry["resolution"]] += 1
            statuses[entry["candidate_status"]] += 1
            ref = {"recipe_id": identity, "position": pos}
            name = entry["name"]
            if name and normalize(name):
                expected["by_text"][normalize(name)].append(ref)
            if entry["resolution"] == "explicit":
                expected["by_explicit_id"][entry["ingredient_id"]].append(ref)
            matches = entry["identity_candidates"]
            candidate_occurrences += bool(matches)
            for key in sorted({m["ingredient_id"] for m in matches}):
                methods = sorted({m["method"] for m in matches if m["ingredient_id"] == key})
                expected["by_candidate_id"][key].append({**ref, "methods": methods})
    check(index["by_title"] == titles, "Índice de títulos")
    check(index["facets"] == facets, "Facetas")
    for mode, postings in expected.items():
        check(index["ingredients"][mode] == postings, f"Referencias de ingredientes: {mode}")
    sums = {k: sum(map(len, v.values())) for k, v in expected.items()}
    inventory = {"occurrences": total, "text_occurrences": sums["by_text"],
                 "explicit_occurrences": sums["by_explicit_id"],
                 "candidate_occurrences": candidate_occurrences,
                 "candidate_postings": sums["by_candidate_id"],
                 "resolution": dict(resolution), "candidate_status": dict(statuses),
                 "text_keys": len(expected["by_text"]),
                 "explicit_keys": len(expected["by_explicit_id"]),
                 "candidate_keys": len(expected["by_candidate_id"])}
    check(index["inventory"] == {"recipes": len(records), "paths": len(paths),
          "title_keys": len(titles), "facet_keys": {k: len(v) for k, v in facets.items()},
          "ingredients": inventory}, "Recuentos del índice")
    samples = {}
    for mode, postings in expected.items():
        keys = sorted(postings)
        # Deterministic spread, not a statistical sample.
        size = min(5, len(keys))
        samples[mode] = []
        for n in range(size):
            key = keys[n * len(keys) // size]
            ref = postings[key][0]
            record = records[ref["recipe_id"]]
            samples[mode].append({"key": key, **ref,
                "path": record["source"]["path"],
                "entry": record["ingredients"][ref["position"]]})
    return {"source_commit": commit, "index_version": index["index_version"],
            "projection_sha256": sha(projection_raw), "index_sha256": sha(index_raw),
            "verified_source_hashes": len(records), "inventory": index["inventory"],
            "samples": samples, "scope": "Consistencia derivada, no precisión culinaria"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for field in ("projection", "index", "repeat", "output"):
        parser.add_argument("--" + field, type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    inputs = [args.projection.resolve(), args.index.resolve(), args.repeat.resolve()]
    if not output.is_relative_to((ROOT_DIR / "site").resolve()) or output in inputs:
        parser.error("Salida derivada bajo site/, distinta de las entradas")
    try:
        projection_raw, index_raw, repeat_raw = (p.read_bytes() for p in inputs)
        check(index_raw == repeat_raw, "Reconstrucción no determinista")
        report = audit(projection_raw, index_raw)
        report["deterministic_bytes"] = True
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True,
                                     indent=2) + "\n", encoding="utf-8")
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Contraste fallido: {exc}\n")
    print(json.dumps({k: v for k, v in report.items() if k != "samples"},
                     ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
