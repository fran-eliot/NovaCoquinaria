"""Índices invertidos de ingredientes con referencia a la ocurrencia original."""
from collections import defaultdict, Counter


def build_ingredient_indexes(records, text_key):
    text, explicit, candidates = defaultdict(list), defaultdict(list), defaultdict(list)
    counts = Counter()
    resolution_counts = Counter()
    candidate_counts = Counter()

    def require(condition, message):
        if not condition:
            raise ValueError(message)

    def nonempty(value):
        return isinstance(value, str) and bool(value.strip())

    for identity, record in sorted(records.items()):
        for position, entry in enumerate(record["ingredients"]):
            context = f"{identity}: ingrediente {position}"
            require(isinstance(entry, dict), f"{context}: ocurrencia inválida")
            name = entry.get("name")
            require("name" in entry and (name is None or isinstance(name, str)),
                    f"{context}: nombre inválido")
            require(nonempty(entry.get("raw")), f"{context}: texto original inválido")
            loc = entry.get("source_location")
            require(isinstance(loc, dict) and
                    type(loc.get("start_line")) is int and
                    type(loc.get("end_line")) is int and
                    0 < loc["start_line"] <= loc["end_line"],
                    f"{context}: localizador inválido")
            option = entry.get("optionality")
            require(option in ("required", "optional", "unknown"),
                    f"{context}: opcionalidad inválida")
            resolution = entry.get("resolution")
            require(resolution in ("explicit", "unresolved", "ambiguous"),
                    f"{context}: resolución inválida")
            ingredient_id = entry.get("ingredient_id")
            require("ingredient_id" in entry and
                    (nonempty(ingredient_id) if resolution == "explicit"
                     else ingredient_id is None), f"{context}: identidad inconsistente")
            matches = entry.get("identity_candidates")
            require(isinstance(matches, list) and
                    (not matches or resolution == "unresolved"),
                    f"{context}: candidatos inconsistentes")
            ref = {"recipe_id": identity, "position": position}
            counts["occurrences"] += 1
            resolution_counts[resolution] += 1
            if name is not None and text_key(name):
                text[text_key(name)].append(ref.copy())
                counts["text_occurrences"] += 1
            if resolution == "explicit":
                explicit[ingredient_id].append(ref.copy())
                counts["explicit_occurrences"] += 1
            grouped = defaultdict(set)
            for match in matches:
                require(isinstance(match, dict) and all(
                    nonempty(match.get(key)) for key in
                    ("ingredient_id", "path", "method", "matched_label")),
                    f"{context}: candidato inválido")
                # Preserve all original candidate evidence in the recipe record.
                # One posting per candidate ID and occurrence; methods are a summary.
                grouped[match["ingredient_id"]].add(match["method"])
            status = "multiple" if len(grouped) > 1 else "single" if grouped else "none"
            require(entry.get("candidate_status") == status,
                    f"{context}: estado de candidatos inconsistente")
            candidate_counts[status] += 1
            if grouped:
                counts["candidate_occurrences"] += 1
            for candidate_id, methods in sorted(grouped.items()):
                candidates[candidate_id].append({**ref, "methods": sorted(methods)})
                counts["candidate_postings"] += 1

    return {
        "by_text": dict(text),
        "by_explicit_id": dict(explicit),
        "by_candidate_id": dict(candidates),
    }, {
        **{key: counts[key] for key in ("occurrences", "text_occurrences",
           "explicit_occurrences", "candidate_occurrences", "candidate_postings")},
        "resolution": dict(sorted(resolution_counts.items())),
        "candidate_status": dict(sorted(candidate_counts.items())),
        "text_keys": len(text), "explicit_keys": len(explicit),
        "candidate_keys": len(candidates),
    }
