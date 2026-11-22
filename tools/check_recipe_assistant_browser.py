"""Recorridos del asistente sobre el portal construido bajo un subdirectorio."""
import argparse
import hashlib
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import re
from pathlib import Path
import shutil
import tempfile
import threading
from urllib.parse import urlencode

from playwright.sync_api import sync_playwright, expect


def exercise(site):
    catalog = json.loads((site / "culinary_explorer.json").read_bytes())
    manifest = json.loads((site / "recipe_assistant/manifest.json").read_bytes())
    recipes = {r["id"]: r for r in catalog["recipes"]}
    report = {"source_commit": manifest["source_commit"], "samples": []}
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        shutil.copytree(site, root / "NovaCoquinaria")
        server = ThreadingHTTPServer(("127.0.0.1", 0),
                                     partial(SimpleHTTPRequestHandler, directory=directory))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page(viewport={"width": 390, "height": 844})
                errors = []
                loaded_modules = []
                page.on("request", lambda req: loaded_modules.append(req.url) if ".mjs" in req.url else None)
                page.on("pageerror", lambda e: errors.append(str(e)))
                base = f"http://127.0.0.1:{server.server_port}/NovaCoquinaria/"
                def url(identity, commit=None):
                    return base + "recipe-assistant.html?" + urlencode({
                        "id": identity, "commit": commit or manifest["source_commit"],
                        "index": manifest["index_sha256"]})
                identity = "REC-0017"
                page.goto(base + "culinary-explorer.html")
                expect(page.locator("#title")).to_be_enabled(timeout=15000)
                page.locator("#title").fill(recipes[identity]["title"])
                page.locator("#title-mode").select_option("exact")
                page.get_by_role("button", name="Buscar", exact=True).click()
                page.get_by_role("link", name="Preparar receta", exact=True).first.click()
                expect(page.locator("#assistant")).to_be_visible(timeout=15000)
                expect(page.locator("#recipe-title")).to_have_text(recipes[identity]["title"])
                assert page.url == base + "recipe-assistant.html?id=REC-0017"
                assert any("recipe-assistant-ui." in u and not u.endswith("-ui.mjs") for u in loaded_modules)
                assert any("culinary-explorer-ui." in u and not u.endswith("-ui.mjs") for u in loaded_modules)
                assert any("recipe-assistant-markdown." in u and not u.endswith("-markdown.mjs") for u in loaded_modules)
                assert page.locator("#context-text h3, #context-text h4").count() > 0
                assert page.locator("#context-text table").count() > 0
                assert page.locator("#context-text li").count() > 0
                expect(page.locator("#context-text")).to_contain_text("74 °C")
                expect(page.locator("#mise")).to_contain_text("Mise en place")
                expect(page.locator("#step-title")).to_have_text("Paso 1 de 9")
                assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
                assert page.locator("#context-text script, #context-text iframe").count() == 0
                page.evaluate("""async () => { const {renderMarkdown}=await import(\'./assets/recipe-assistant-markdown.mjs\'); const div=document.createElement(\'div\'); renderMarkdown(div,\'<img src=x onerror=alert(1)> [texto](javascript:alert(1))\'); if(div.querySelector(\'img,script,a,iframe\')) throw Error(\'HTML activo\'); }""")
                first = page.locator("#ingredients input").first
                first.focus()
                page.keyboard.press("Space")
                expect(first).to_be_checked()
                expect(page.locator("#ingredient-progress")).to_contain_text("1 de ")
                page.locator("#step-done").check()
                page.locator("#next-step").click()
                expect(page.locator("#step-title")).to_have_text("Paso 2 de 9")
                expect(page.locator("#step-title")).to_be_focused()
                expect(page.locator("#step-done")).not_to_be_checked()
                page.locator("#previous").click()
                expect(page.locator("#step-done")).to_be_checked()
                page.locator("#minutes").fill("0")
                page.locator("#seconds").fill("3")
                page.locator("#start-timer").click()
                page.locator("#pause-timer").click()
                expect(page.locator("#timer-status")).to_have_text("Pausado")
                page.locator("#resume-timer").click()
                expect(page.locator("#timer-status")).to_contain_text("Tiempo finalizado", timeout=8000)
                expect(page.locator("#step-title")).to_have_text("Paso 1 de 9")
                page.locator("#cancel-timer").click()
                expect(page.locator("#timer-status")).to_have_text("Inactivo")
                page.once("dialog", lambda d: d.accept())
                page.locator("#reset-session").click()
                expect(first).not_to_be_checked()
                expect(page.locator("#step-done")).not_to_be_checked()
                first.check()
                page.reload()
                expect(page.locator("#assistant")).to_be_visible(timeout=15000)
                expect(page.locator("#ingredients input").first).not_to_be_checked()
                expect(page.locator("#timer-status")).to_have_text("Inactivo")
                page.locator("#source-link").click()
                assert page.url.startswith(base) and page.url.endswith(".html")
                expect(page.locator("h1").first).to_be_visible()
                page.set_viewport_size({"width": 1280, "height": 900})
                for identity, snippet in [("REC-0079", "lemon curd"), ("REC-573", "220–260 ml"),
                                          ("REC-0190", "700 g")]:
                    page.goto(url(identity))
                    expect(page.locator("#assistant")).to_be_visible(timeout=15000)
                    expect(page.locator("#recipe-title")).to_have_text(recipes[identity]["title"])
                    expect(page.locator("#context-text")).to_contain_text(snippet)
                    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
                    report["samples"].append(identity)
                # Verificación de escalado sobre una proyección real publicada.
                # Elegir una receta admisible sin fijar identificadores editoriales.
                scaling_candidate = None
                for candidate_id in sorted(manifest["recipes"]):
                    filename = hashlib.sha256(candidate_id.encode("utf-8")).hexdigest() + ".json"
                    candidate = json.loads((site / "recipe_assistant" / filename).read_bytes())
                    y = candidate.get("yield") or {}
                    if (y.get("unit") not in ("racion", "porcion") or
                            y.get("min") != y.get("max")):
                        continue
                    try:
                        original = int(y["min"])
                    except (ValueError, TypeError):
                        continue
                    if not 1 <= original <= 24 or str(original) != y["min"]:
                        continue
                    eligible = [entry for entry in candidate["ingredients"]
                                if entry["quantity"]["status"] == "exact"
                                and entry["quantity"]["approximate"] is False
                                and entry["quantity"]["min"] == entry["quantity"]["max"]
                                and entry["quantity"]["unit"] in ("g", "kg", "ml", "cl", "l")
                                and isinstance(entry["quantity"]["min"], str)
                                and re.fullmatch(r"(?:0|[1-9]\d*)(?:\.\d+)?", entry["quantity"]["min"])
                                and float(entry["quantity"]["min"]) > 0]
                    if eligible:
                        scaling_candidate = (candidate_id, candidate, original, len(eligible))
                        break
                assert scaling_candidate is not None, "No hay ninguna receta apta para verificar escalado"
                scale_id, scale_recipe, original, scaled_count = scaling_candidate
                page.goto(url(scale_id))
                expect(page.locator("#assistant")).to_be_visible(timeout=15000)
                expect(page.locator("#scaling-panel")).to_be_visible()
                expect(page.locator("#scaling-original")).to_have_text(str(original))
                assert page.locator("#scaling-preview li").count() == len(scale_recipe["ingredients"])
                expect(page.locator("#scaling-status")).to_contain_text("Raciones originales")
                expect(page.locator("#shopping-scaling-note")).to_contain_text("sin cantidades propuestas")
                assert page.locator("#scaling-preview li").filter(has_text=" → ").count() == 0
                assert page.locator("#scaling-preview li").filter(has_text="sin ajuste automático").count() == 0
                assert page.locator("#scaling-preview li").all_text_contents() == [
                    entry["raw"] for entry in scale_recipe["ingredients"]]
                shopping_before = page.locator("#shopping-selection label").all_text_contents()
                expect(page.locator("#scaling-reset")).to_be_disabled()
                target = original + 1 if original < 24 else original - 1
                page.locator("#scaling-target").fill(str(target))
                expect(page.locator("#shopping-scaling-note")).to_contain_text(f"de {original} a {target} raciones")
                expect(page.locator("#shopping-scaling-note")).to_contain_text("revisarlas antes de guardarlas")
                # El recuento incluye masas, volúmenes, fracciones exactas
                # y unidades contables enteras; la muestra inicial es un mínimo.
                visible_scaled = page.locator("#scaling-preview li").filter(has_text=" → ").count()
                assert scaled_count <= visible_scaled <= len(scale_recipe["ingredients"])
                expect(page.locator("#scaling-status")).to_contain_text(
                    f"{visible_scaled} de {len(scale_recipe['ingredients'])} cantidades ajustadas")
                assert page.locator("#shopping-selection label").all_text_contents() == shopping_before
                page.context.grant_permissions(["clipboard-read", "clipboard-write"])
                page.locator("#copy-scaling").click()
                expect(page.locator("#copy-scaling-status")).to_contain_text("Lista copiada")
                copied = page.evaluate("navigator.clipboard.readText()")
                assert scale_recipe["title"] in copied
                assert "raciones" in copied
                assert ("revisar manualmente" in copied) == (visible_scaled < len(scale_recipe["ingredients"]))
                expect(page.locator("#ingredients .scaled-ingredient-hint:visible")).to_have_count(visible_scaled)
                assert all("Adaptado: " in value for value in
                           page.locator("#ingredients .scaled-ingredient-hint:visible").all_text_contents())
                expect(page.locator("#scaling-reset")).to_be_enabled()
                page.locator("#scaling-reset").click()
                expect(page.locator("#scaling-target")).to_have_value(str(original))
                expect(page.locator("#scaling-target")).to_be_focused()
                expect(page.locator("#scaling-reset")).to_be_disabled()
                expect(page.locator("#scaling-status")).to_contain_text("Raciones originales")
                expect(page.locator("#ingredients .scaled-ingredient-hint:visible")).to_have_count(0)
                assert page.locator("#scaling-preview li").all_text_contents() == [
                    entry["raw"] for entry in scale_recipe["ingredients"]]
                assert page.locator("#shopping-selection label").all_text_contents() == shopping_before
                page.locator("#scaling-target").fill("0")
                expect(page.locator("#scaling-status")).to_contain_text("Indica entre 1 y 24")
                expect(page.locator("#shopping-scaling-note")).to_contain_text("Raciones no válidas")
                expect(page.locator("#scaling-reset")).to_be_enabled()
                expect(page.locator("#copy-scaling")).to_be_disabled()
                assert page.locator("#scaling-preview li").count() == 0
                expect(page.locator("#ingredients .scaled-ingredient-hint:visible")).to_have_count(0)
                page.locator("#scaling-reset").click()
                expect(page.locator("#scaling-status")).to_contain_text("Raciones originales")
                expect(page.locator("#scaling-reset")).to_be_disabled()
                page.reload()
                expect(page.locator("#scaling-target")).to_have_value(str(original))
                expect(page.locator("#scaling-status")).to_contain_text("Raciones originales")
                expect(page.locator("#ingredients .scaled-ingredient-hint:visible")).to_have_count(0)
                report["scaling_sample"] = scale_id
                page.get_by_role("link", name="Volver al explorador").click()
                expect(page.locator("#title")).to_be_enabled(timeout=15000)
                for invalid in [url("REC-inexistente"), url("REC-0017", "0"*40)]:
                    page.goto(invalid)
                    expect(page.locator("#load-status")).to_contain_text("No se pudo abrir")
                    expect(page.locator("#assistant")).to_be_hidden()
                page.goto(base + "recipe-assistant.html?id=REC-0017")
                expect(page.locator("#assistant")).to_be_visible(timeout=15000)
                page.route("**/recipe_assistant/*.json", lambda route:
                           route.continue_() if route.request.url.endswith("manifest.json")
                           else route.fulfill(body="{}", content_type="application/json"))
                page.goto(url("REC-0017"))
                expect(page.locator("#load-status")).to_contain_text("Huella de receta incorrecta")
                expect(page.locator("#assistant")).to_be_hidden()
                assert not errors, errors
                browser.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join()
    return {**report, "passed": True, "browser": "Chromium",
            "checklist": True, "timer": True, "reload_reset": True, "invalid_data": True}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = exercise(args.site)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
