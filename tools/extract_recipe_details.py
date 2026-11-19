"""Extracción conservadora de rendimiento, tiempos y referencias Markdown."""
import posixpath
import re
from urllib.parse import urlsplit, unquote

from extract_recipe_content import norm, location, FENCE

NUMBER = r"(\d+(?:[.,]\d+)?)"
RANGE = NUMBER + r"(?:\s*[-–—]\s*" + NUMBER + r")?"
YIELD = re.compile(r"^" + RANGE + r"(?:\s+(raciones?|porciones?|unidades?|vasitos?|cuencos?))?(?:\s+(.*))?$", re.I)
DURATION = re.compile(r"^(?:aproximadamente\s+)?"+RANGE+r"\s*(minutos?|min|horas?|h)(?:\s+(.*))?$", re.I)
LINK = re.compile(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)")
YIELD_UNITS = {"racion":"racion","raciones":"racion","porcion":"porcion","porciones":"porcion",
               "unidad":"unidad","unidades":"unidad","vasito":"vasito","vasitos":"vasito",
               "cuenco":"cuenco","cuencos":"cuenco"}
PHASES = {"preparacion":"preparation","tiempo de preparacion":"preparation",
          "cocinado":"cooking","tiempo de cocinado":"cooking","coccion":"cooking",
          "horneado":"baking","reposo":"rest","refrigeracion":"chilling",
          "tiempo orientativo":"declared_total","tiempo total":"declared_total"}


def bounds(match):
    from decimal import Decimal
    lo = Decimal(match[1].replace(",","."))
    hi = Decimal(match[2].replace(",", ".")) if match[2] else lo
    if lo <= 0 or hi < lo:
        return None
    return {"min":format(lo.normalize(),"f"),"max":format(hi.normalize(),"f")}


def general_fields(sections):
    yields = []
    durations = []
    diagnostics = []
    for section in sections:
        if norm(section["heading"] or "") != "informacion general":
            continue
        start = section["source_location"]["start_line"] + 1
        for idx, line in enumerate(section["content"].splitlines(),start):
            if not line.strip().startswith("|"):
                continue
            cells = [part.strip() for part in line.strip().strip("|").split("|")]
            if len(cells) != 2:
                continue
            label, raw = cells
            key = norm(label)
            value = norm(raw)
            if key in ("raciones","rendimiento","porciones"):
                result = {"raw":raw,"min":None,"max":None,"unit":None,
                          "source_location":location(idx,idx)}
                match = YIELD.fullmatch(value)
                if match and bounds(match):
                    # A qualifier is preserved, not converted into a second yield.
                    unit = YIELD_UNITS.get(norm(match[3] or ""), None)
                    if unit is None and key in ("raciones","porciones"):
                        unit = "racion" if key=="raciones" else "porcion"
                    if unit:
                        result.update(bounds(match),unit=unit)
                yields.append(result)
            elif key in PHASES:
                result = {"phase":PHASES[key],"raw":raw,"min":None,"max":None,"unit":None,
                          "source_location":location(idx,idx)}
                match = DURATION.fullmatch(value)
                if match and bounds(match):
                    qualifier = match[4] or ""
                    # A compound duration is not silently interpreted as its first term.
                    if not re.search(r"\b(?:mas|y|otros?)\b|\+|\d",qualifier):
                        result.update(bounds(match),unit="min" if match[3].startswith("min") else "h")
                if result["min"] is None:
                    diagnostics.append({"code":"DURATION_UNPARSED","severity":"warning","field":"durations",
                                        "source_location":location(idx,idx),"description":"Duración conservada sin interpretación numérica."})
                durations.append(result)
    if len(yields)>1:
        diagnostics.append({"code":"YIELD_AMBIGUOUS","severity":"warning","field":"yield",
                            "source_location":None,"description":"Múltiples declaraciones; consultar secciones originales."})
    elif yields and yields[0]["min"] is None:
        diagnostics.append({"code":"YIELD_UNPARSED","severity":"warning","field":"yield",
                            "source_location":yields[0]["source_location"],"description":"Rendimiento conservado sin interpretación numérica."})
    return {"yield":yields[0] if len(yields)==1 else None,"durations":durations},diagnostics


def extract_references(sections, path, lookup, known_paths):
    refs, diagnostics = [], []
    for section in sections:
        fence = None
        first = section["source_location"]["start_line"] + (1 if section["heading"] is not None else 0)
        # Extract heading links as well as the body, preserving line numbers.
        lines = list(enumerate(section["content"].splitlines(),first))
        if section["heading"] is not None:
            lines.insert(0,(first-1,section["heading"]))
        for idx,line in lines:
            marker = FENCE.match(line)
            if marker:
                token=marker[1]
                if fence is None:
                    fence=token
                elif token[0]==fence[0] and len(token)>=len(fence):
                    fence=None
                continue
            if fence:
                continue
            for match in LINK.finditer(line):
                label, href = match.groups()
                href = href.strip()
                result={"label":label,"raw_target":href,"resolved_path":None,
                        "target_id":None,"status":"unresolved","source_location":location(idx,idx)}
                try:
                    url=urlsplit(href)
                    if url.scheme or url.netloc:
                        result["status"]="external"
                    elif not url.path and url.fragment:
                        result.update(status="local_anchor",resolved_path=path,target_id=lookup.get(path))
                    elif url.path and not url.path.startswith("/"):
                        candidate=posixpath.normpath(posixpath.join(posixpath.dirname(path),unquote(url.path)))
                        if candidate in known_paths:
                            result.update(status="resolved",resolved_path=candidate,target_id=lookup.get(candidate))
                except ValueError:
                    pass
                refs.append(result)
                if result["status"]=="unresolved":
                    diagnostics.append({"code":"REFERENCE_UNRESOLVED","severity":"warning","field":"references",
                                        "source_location":location(idx,idx),"description":"Destino no resuelto en el snapshot: "+href})
    return refs,diagnostics
