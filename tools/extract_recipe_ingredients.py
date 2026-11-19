"""Extracción conservadora de ingredientes y cantidades declaradas."""
import re
import posixpath
from fractions import Fraction
from decimal import Decimal
from collections import Counter
import unicodedata
from urllib.parse import urlsplit, unquote

FRACTIONS = {"½":"1/2","¼":"1/4","¾":"3/4","⅓":"1/3","⅔":"2/3","⅛":"1/8"}
NUM = r"(?:\d+\s+\d+/\d+|\d+/\d+|\d+(?:[.,]\d+)?)"
AMOUNT = re.compile(rf"^({NUM})(?:\s*[-–—]\s*({NUM}))?(?=\s|$)\s*")
UNITS = {
    "g":"g", "gramo":"g", "gramos":"g", "kg":"kg",
    "ml":"ml", "cl":"cl", "l":"l", "litro":"l", "litros":"l",
    "cucharada":"cucharada", "cucharadas":"cucharada",
    "cucharadita":"cucharadita", "cucharaditas":"cucharadita",
    "diente":"diente", "dientes":"diente", "vaso":"vaso", "vasos":"vaso",
    "taza":"taza", "tazas":"taza", "unidad":"unidad", "unidades":"unidad",
    "cm":"cm", "hoja":"hoja", "hojas":"hoja", "rama":"rama", "ramas":"rama",
    "pizca":"pizca", "pizcas":"pizca", "gota":"gota", "gotas":"gota",
}
QUAL = re.compile(r"\b(?:al gusto|una pizca|un chorrito|unas gotas|cantidad necesaria|cantidad suficiente|unas cucharadas)\b", re.I)
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


def plain(raw):
    return LINK.sub(r"\1", raw).replace("**", "").replace("__", "").strip()


def normalized(text):
    return "".join(c for c in unicodedata.normalize("NFD", text.lower())
                   if not unicodedata.combining(c))


def number(text):
    text = text.replace(",", ".")
    if " " in text:
        whole, part = text.split()
        value = Fraction(whole) + Fraction(part)
        return str(value), value
    if "/" in text:
        value = Fraction(text)
        return str(value), value
    value = Decimal(text)
    return format(value.normalize(), "f"), Fraction(value)


def quantity(raw):
    text = plain(raw)
    for symbol, replacement in FRACTIONS.items():
        text = re.sub(rf"(?<=\d){symbol}", " " + replacement, text)
        text = text.replace(symbol, replacement)
    approximate = bool(re.search(r"\b(?:aproximadamente|aproximados?|aproximadas?|orientativos?|orientativas?)\b|^(?:unos|unas)\s+\d", text, re.I))
    text = re.sub(r"^(?:opcional:\s*|unos?\s+|unas\s+(?=\d)|aproximadamente\s+)", "", text, flags=re.I)
    text = re.sub(r"^medi[oa]\s+", "1/2 ", text, flags=re.I)
    # Explicit Spanish mixed-number household measure; preserve original line.
    text = re.sub(r"^(\d+)\s+(cucharadas?|cucharaditas?|tazas?|vasos?)\s+y\s+medi[oa]\b", r"\1 1/2 \2", text, flags=re.I)
    result = {"raw": raw, "status":"missing", "min":None, "max":None, "unit":None,"approximate":approximate}
    match = AMOUNT.match(text)
    if match:
        tail = text[match.end():].strip()
        if not tail or re.match(r"^(?:o\s|quiz[aá]|[-–—]|\d|/)", tail, re.I):
            result["status"] = "ambiguous"
            return result, None
        token = tail.split()[0].lower().rstrip(",;")
        unit = UNITS.get(token, "unidad")
        name = tail[len(tail.split()[0]):].strip() if token in UNITS else tail
        name = re.sub(r"^de\s+", "", name, flags=re.I)
        try:
            lo, lv = number(match[1])
            hi, hv = number(match[2]) if match[2] else (lo, lv)
            if lv <= 0 or hv < lv:
                raise ValueError("intervalo inválido")
        except (ValueError, ZeroDivisionError, ArithmeticError):
            result["status"] = "ambiguous"
            return result, None
        result.update(status="range" if match[2] else "exact", min=lo, max=hi, unit=unit)
        return result, name or None
    if QUAL.search(text) or re.search(r"\b(?:un trozo pequeno|una punta|un poco|cantidad no precisada)\b", normalized(text)):
        result["status"] = "qualitative"
    elif re.match(r"^\d|^[+-]\d", text):
        result["status"] = "ambiguous"
    return result, plain(raw)


def extract_ingredients(raw, path, lookup):
    lines = raw.decode("utf-8-sig").splitlines()
    active = False
    level = 0
    group = None
    entries = []
    diagnostics = []
    optional_block = False
    # Skip YAML, including any heading-like content.
    end = next((i for i, line in enumerate(lines[1:], 1)
                if line.strip() == "---"), 0) if lines and lines[0].strip() == "---" else -1
    for idx, line in enumerate(lines, 1):
        if idx <= end + 1:
            continue
        heading = HEADING.match(line)
        if heading:
            depth, title = len(heading[1]), plain(heading[2])
            key = normalized(title)
            if active and depth <= level:
                break
            if active:
                group = title
                optional_block = False
            elif key == "ingredientes" or key == "ingredientes estructurales" or re.match(r"^ingredientes (?:para |propuestos para |orientativos para |de una formula )", key):
                active, level = True, depth
            continue
        if not active:
            continue
        # Separators can occur between ingredient subgroups.
        if re.fullmatch(r"\s*(?:---+|\*\*\*+)\s*", line):
            optional_block = False
            continue
        if normalized(plain(line)).rstrip(":") == "opcionalmente":
            optional_block = True
            continue
        item = re.match(r"^\s*[-*+]\s+(.+)$", line)
        if not item:
            # Only recognize a quantified prose line in an explicitly structural group.
            if normalized(group or "") == "proteina" and AMOUNT.match(plain(line)):
                text = line.strip()
            else:
                continue
        else:
            text = item[1]
        loc = {"start_line":idx, "end_line":idx}
        q, name = quantity(text)
        option_text = normalized(text + " " + (group or ""))
        # Mixed required/optional components cannot be assigned a single role.
        mixed = bool(re.search(r"\by\s+[^,;()]+\s+opcional(?:es)?\b", option_text))
        conditional = bool(re.search(r"\b(?:solo si|si (?:conviene|procede|es necesario|hace falta|se desea|se usa|se utilizan?))\b", option_text))
        option = ("unknown" if mixed else "optional" if optional_block or conditional or re.search(r"\bopcional(?:es)?\b", option_text) else "required")
        targets = []
        for _, href in LINK.findall(text):
            try:
                url = urlsplit(href)
            except ValueError:
                continue
            if url.scheme or url.netloc or not url.path or url.path.startswith("/"):
                continue
            destination = posixpath.normpath(posixpath.join(posixpath.dirname(path), unquote(url.path)))
            if destination in lookup:
                targets.append(lookup[destination])
        targets = sorted(set(targets))
        resolution = "explicit" if len(targets) == 1 else "ambiguous" if targets else "unresolved"
        entries.append({"raw":text, "group":group, "name":name, "quantity":q,
                        "optionality":option, "ingredient_id":targets[0] if len(targets)==1 else None,
                        "resolution":resolution, "source_location":loc})
        for condition, code, field in [(q["status"]=="ambiguous","AMBIGUOUS_QUANTITY","quantity"),
                                       (resolution!="explicit","INGREDIENT_"+resolution.upper(),"ingredient_id"),
                                       (option=="unknown","INGREDIENT_OPTIONALITY_UNDETERMINED","optionality")]:
            if condition:
                diagnostics.append({"code":code,"severity":"warning","field":field,
                                    "source_location":loc,"description":"Interpretación no resuelta; se conserva el texto."})
    if not entries:
        diagnostics.append({"code":"INGREDIENT_SECTION_NOT_EXTRACTED","severity":"warning",
                            "field":"ingredients","source_location":None,
                            "description":"No se reconoció una lista de ingredientes."})
    return entries, diagnostics
