"""Candidatos léxicos; nunca sustituyen una identidad explícita."""
from collections import defaultdict
import re
from extract_recipe_ingredients import normalized, plain

# Alias acotados y revisados frente a los títulos y formatos de Despensa.
# Las variantes de salsa conservan su texto; no implican intercambiabilidad.
ALIASES = {
    "pimenton": ("pimentón dulce", "pimentón picante", "pimentón agridulce",),
    "laurel": ("hoja de laurel", "hojas de laurel",),
    "cebolla": ("cebollas", "cebolla picada", "cebolla mediana, picada",),
    "huevo": ("huevos", "huevos L", "huevo L",),
    "comino": ("comino molido",),
    "harina de trigo": ("harina de trigo común", "harina de trigo adicional",),
    "vino blanco para cocinar": ("vino blanco seco",),
    "aceite de sesamo": ("aceite de sésamo tostado", "aceite de sésamo tostado, opcional",),
    "caldo de verduras": ("caldo de verduras bajo en sal",),
    "almendras": ("almendras tostadas sin sal",),
    "aceite de oliva virgen extra": ("AOVE",),
    "limon": ("zumo de limón", "ralladura de limón",),
    "salsa de soja": ("salsa de soja clara", "salsa de soja oscura",),
    "leche de coco": ("leche de coco en conserva", "leche de coco en brick",),
}


def key(text):
    return " ".join(normalized(plain(text)).strip(" \t.,;:").split())


def build_catalog(documents):
    catalog = defaultdict(list)
    for path, metadata in sorted(documents.items()):
        title = metadata.get("titulo")
        identity = metadata.get("id")
        if not isinstance(title, str) or not isinstance(identity, str):
            continue
        canonical = key(title)
        for label, method in [(canonical, "title_exact")] + [
                (key(alias), "reviewed_alias") for alias in ALIASES.get(canonical, ())]:
            catalog[label].append({"ingredient_id":identity,"path":path,
                                   "matched_label":label,"method":method})
    return dict(catalog)


def candidates(entry, catalog):
    if entry["resolution"] != "unresolved" or not entry.get("name"):
        return []
    label = key(entry["name"])
    # Only whole names: no substring, stemming, automatic singularization
    # or stripping alternatives, qualifiers and preparation instructions.
    return sorted(catalog.get(label, []),
                  key=lambda item:(item["ingredient_id"],item["path"],item["method"]))


def annotate(entries, catalog):
    for entry in entries:
        matches = candidates(entry,catalog)
        entry["identity_candidates"] = matches
        identities = {match["ingredient_id"] for match in matches}
        entry["candidate_status"] = ("multiple" if len(identities)>1 else
                                     "single" if identities else "none")
