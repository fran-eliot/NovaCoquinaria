"""Recorridos del asistente sobre el portal construido bajo un subdirectorio."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
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
                assert page.locator("#context-text h3, #context-text h4").count() > 0
                assert page.locator("#context-text table").count() > 0
                assert page.locator("#context-text li").count() > 0
                expect(page.locator("#context-text")).to_contain_text("74 °C")
                expect(page.locator("#mise")).to_contain_text("Mise en place")
                expect(page.locator("#step-title")).to_have_text("Paso 1 de 9")
                assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
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
