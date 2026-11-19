"""Recuperación textual por secuencias contiguas sobre postings existentes."""
import re
import unicodedata


def tokens(value: str) -> tuple[str, ...]:
    """Normalización NFC y casefold, con diacríticos conservados."""
    normalized = unicodedata.normalize("NFC", " ".join(value.casefold().split()))
    return tuple(re.findall(r"[^\W_]+", normalized, flags=re.UNICODE))


def contains_terms(haystack, needle):
    return bool(needle) and any(haystack[i:i + len(needle)] == needle
                                for i in range(len(haystack) - len(needle) + 1))


def term_postings(by_text, value):
    """Referencias únicas y ordenadas; no interpreta sus identidades."""
    if not isinstance(value, str) or not (needle := tokens(value)):
        raise ValueError("Consulta sin términos")
    refs = {(posting["recipe_id"], posting["position"])
            for key, postings in by_text.items()
            if contains_terms(tokens(key), needle)
            for posting in postings}
    return [{"recipe_id": identity, "position": position}
            for identity, position in sorted(refs)]
