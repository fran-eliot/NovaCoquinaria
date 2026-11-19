"""Proyección de secciones, pasos y declaraciones explícitas de experiencia."""
import re
import unicodedata

HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
NUMBERED = re.compile(r"^\s*(\d+)[.)]\s+(.+)$")
FENCE = re.compile(r"^\s{0,3}(\x60{3,}|~{3,})")


def norm(text):
    return "".join(c for c in unicodedata.normalize("NFD", text.lower())
                   if not unicodedata.combining(c)).replace("**", "")


def location(start, end):
    return {"start_line": start, "end_line": end}


def extract_sections(raw):
    lines = raw.decode("utf-8-sig").splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        start = next((i + 1 for i, line in enumerate(lines[1:], 1)
                      if line.strip() == "---"), len(lines))
    sections = []
    current = {"heading": None, "level": 0, "source_location": location(start+1,start),
               "content": ""}
    buffer = []
    fence = None
    for offset in range(start, len(lines)):
        line = lines[offset]
        marker = FENCE.match(line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            buffer.append(line)
            continue
        match = HEADING.match(line) if fence is None else None
        if match:
            if current["heading"] is not None or any(x.strip() for x in buffer):
                current["content"] = "\n".join(buffer)
                current["source_location"]["end_line"] = offset
                sections.append(current)
            current = {"heading": match[2], "level": len(match[1]),
                       "source_location": location(offset+1,offset+1), "content": ""}
            buffer = []
        else:
            buffer.append(line)
    if current["heading"] is not None or any(x.strip() for x in buffer):
        current["content"] = "\n".join(buffer)
        current["source_location"]["end_line"] = len(lines)
        sections.append(current)
    return sections


def extract_steps(sections):
    active = None
    steps = []
    chosen = False
    # A nested explicit Elaboración under Preparación is more specific.
    has_explicit = any(norm(s["heading"] or "") == "elaboracion" for s in sections)
    for section in sections:
        title = section["heading"] or ""
        depth = section["level"]
        if active is not None and depth <= active:
            active = None
            if chosen:
                break
        key = norm(title)
        if active is None and (key in ("elaboracion", "elaboracion propuesta", "elaboracion de referencia") or (key == "preparacion" and not has_explicit) or key.startswith(("elaboracion principal:", "preparacion propuesta para "))):
            active = depth
            chosen = True
        if active is None:
            continue
        header_step = NUMBERED.match(title) if depth > active else None
        if header_step and not (norm(header_step[2]) == "elaboracion" and any(NUMBERED.match(line) for line in section["content"].splitlines())):
            steps.append({"order": len(steps)+1, "source_number": int(header_step[1]),
                          "text": title + "\n" + section["content"],
                          "source_location": section["source_location"]})
            continue
        first = section["source_location"]["start_line"] + 1
        pending = None
        fence = None
        for i, line in enumerate(section["content"].splitlines(), first):
            marker = FENCE.match(line)
            if marker:
                token = marker[1]
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token)>=len(fence):
                    fence = None
                if pending:
                    pending["text"] += "\n"+line
                    pending["source_location"]["end_line"] = i
                continue
            match = NUMBERED.match(line) if fence is None else None
            if match:
                pending = {"order":len(steps)+1,"source_number":int(match[1]),
                           "text":match[2],"source_location":location(i,i)}
                steps.append(pending)
            elif pending and line.startswith(("  ", "\t")):
                pending["text"] += "\n"+line
                pending["source_location"]["end_line"] = i
            else:
                pending = None
    return steps


PENDING = re.compile(r"\b(?:pendiente de prueba(?: domestica)?|no consta (?:una )?(?:prueba|elaboracion|valoracion domestica)|no consta como (?:preparada|elaborada|cocinada))\b")
PREPARED = re.compile(r"\b(?:ya cocinada y valorada|la elaboracion domestica se probo|en la adaptacion de .+? se utilizaron|elaboracion domestica probada)\b")
SCOPE = re.compile(r"\b(?:formulacion adaptada|no se ha confirmado|no esta demostrado|referencias orientativas|requieren contraste|no medicion final)\b")
VALUATION = re.compile(r"\b(?:resultado fue valorado|valorada muy positivamente|valoracion «|resultado muy sabroso|resultado poco agradable)\b")
HISTORICAL = re.compile(r"\b(?:preparacion confirmada; resultado recordado|elaboracion domestica habitual confirmada|se habia preparado en casa varias veces|se habia elaborado en casa varias veces)\b")
RELATED = re.compile(r"\b(?:existe una elaboracion domestica de magret asiatico|magret asiatico cocinado, resultado)\b")
PARTIAL = re.compile(r"\b(?:base domestica confirmada|consta la preparacion de la base de zanahorias)\b")
LIMITED = re.compile(r"\b(?:no se conservan las cantidades exactas|no se debe presentar una propuesta posterior como formula ya probada|no acredita[n]? por si misma[s]?|no se han recuperado las dosis exactas|variante exacta sin confirmar|no esta confirmada)\b")
EVIDENCE_HEADERS = ("descripcion", "origen y contexto", "estado de prueba domestica",
                    "evolucion de la receta domestica", "versiones y eleccion pendiente",
                    "valoracion de la preparacion domestica", "informacion general",
                    "ingredientes", "registro de prueba", "experiencia domestica y valoracion",
                    "experiencia domestica y evolucion", "antecedentes y versiones",
                    "evolucion y evidencia", "datos de la receta")


def extract_evidence(sections):
    claims = []
    for section in sections:
        if norm(section["heading"] or "") not in EVIDENCE_HEADERS:
            continue
        start = section["source_location"]["start_line"] + 1
        for idx, line in enumerate(section["content"].splitlines(), start):
            text = norm(line)
            # Limitar las líneas de ingredientes a notas explícitas de procedencia.
            if norm(section["heading"] or "") == "ingredientes" and not text.startswith(("nota de procedencia:", "nota de formulacion:")):
                continue
            for kind, pattern in (("pending", PENDING), ("prepared", PREPARED),
                                  ("scope", SCOPE), ("valuation", VALUATION),
                                  ("historical_confirmed", HISTORICAL), ("related_preparation", RELATED),
                                  ("partial_preparation", PARTIAL), ("scope", LIMITED)):
                if pattern.search(text):
                    claim = {"kind":kind,"text":line,"source_location":location(idx,idx)}
                    if claim not in claims:
                        claims.append(claim)
    kinds = {c["kind"] for c in claims}
    # New directed claims retain the distinction between preparation of the dish,
    # an uncertain related variant, and preparation of a component only.
    if "historical_confirmed" in kinds:
        kinds.add("prepared")
    status = ("unknown" if {"prepared","pending"} <= kinds else
              "prepared" if "prepared" in kinds else
              "pending" if "pending" in kinds else "unknown")
    # No convertir una preparación histórica en certificación de la fórmula.
    return {"status":status,
            "historical_preparation": True if "prepared" in kinds else None,
            "current_formula_validated": False if "scope" in kinds or status=="pending" else None,
            "scope":("historical_preparation" if status=="prepared" else
                     "related_variant" if "related_preparation" in kinds else
                     "component_only" if "partial_preparation" in kinds else "undetermined"),
            "valuation":[c for c in claims if c["kind"]=="valuation"] or None,
            "claims":claims}


def extract_content(raw):
    sections = extract_sections(raw)
    steps = extract_steps(sections)
    evidence = extract_evidence(sections)
    diagnostics = []
    if not steps:
        diagnostics.append({"code":"STEPS_NOT_EXTRACTED","severity":"warning","field":"steps",
                            "source_location":None,"description":"No se reconocieron pasos explícitos de elaboración."})
    if evidence["status"] == "unknown":
        diagnostics.append({"code":"EVIDENCE_UNDETERMINED","severity":"warning","field":"evidence",
                            "source_location":None,"description":"Declaraciones insuficientes o contradictorias; revisar fuente."})
    return {"sections":sections,"steps":steps,"evidence":evidence}, diagnostics
