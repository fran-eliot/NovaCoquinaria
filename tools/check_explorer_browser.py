"""Recorridos de navegador sobre el build local, servido bajo un subdirectorio."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import tempfile
import threading
import shutil

from playwright.sync_api import sync_playwright, expect


def exercise(site):
    report = {}
    catalog = json.loads((site / "culinary_explorer.json").read_bytes())
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        shutil.copytree(site, root / "NovaCoquinaria")
        server = ThreadingHTTPServer(("127.0.0.1", 0),
                                     partial(SimpleHTTPRequestHandler, directory=directory))
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page(viewport={"width": 390, "height": 844})
                errors = []
                page.on("pageerror", lambda error: errors.append(str(error)))
                base = f"http://127.0.0.1:{server.server_port}/NovaCoquinaria/"
                page.goto(base + "index.html")
                page.get_by_role("link", name="Abrir el explorador culinario").click()
                expect(page.locator("#title")).to_be_enabled(timeout=15000)
                expect(page.locator("#status")).to_contain_text(str(catalog["recipe_count"]))
                expect(page.locator("#results article")).to_have_count(min(24, catalog["recipe_count"]))
                assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
                if catalog["recipe_count"] > 24:
                    page.locator("#next").click()
                    expect(page.locator("#page")).to_contain_text("Página 2")
                    page.locator("#prev").click()
                    expect(page.locator("#page")).to_contain_text("Página 1")
                page.locator("#title").focus()
                page.keyboard.press("Tab")
                expect(page.locator("#title-mode")).to_be_focused()
                assert page.locator("#title-mode").evaluate("(e) => e.matches(':focus-visible')")
                sample = catalog["recipes"][0]
                page.locator("#title").fill(sample["title"])
                page.locator("#title-mode").select_option("exact")
                page.locator("#title").press("Enter")
                expect(page.locator("#results article h3 a").first).to_have_text(sample["title"])
                page.get_by_role("button", name="Limpiar filtros").click()
                expect(page.locator("#results article")).to_have_count(min(24, catalog["recipe_count"]))
                report["keyboard_title"] = True
                page.locator("#ingredients").fill("ajo\nsalsa de soja")
                page.get_by_role("button", name="Buscar", exact=True).click()
                count = page.locator("#results article").count()
                assert count > 0
                page.locator("#results summary").first.click()
                expect(page.locator("#results details").first).to_contain_text("Consulta: ajo")
                expect(page.locator("#results details").first).to_contain_text("Consulta: salsa de soja")
                report["compound_first_page"] = count
                page.locator("#results article h3 a").first.click()
                assert page.url.startswith(base) and page.url.endswith(".html")
                expect(page.locator("h1").first).to_be_visible()
                page.goto(base + "culinary-explorer.html")
                expect(page.locator("#title")).to_be_enabled()
                page.locator("#title").fill("noexistexyz")
                page.get_by_role("button", name="Buscar", exact=True).click()
                expect(page.locator("#status")).to_contain_text("No hay recetas")
                page.locator("#title").fill("---")
                page.get_by_role("button", name="Buscar", exact=True).click()
                expect(page.locator("#status")).to_contain_text("Consulta inválida")
                page.get_by_role("button", name="Limpiar filtros").click()
                expect(page.locator("#results article")).to_have_count(min(24, catalog["recipe_count"]))
                page.set_viewport_size({"width": 1280, "height": 900})
                assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
                assert not errors, errors
                failed = browser.new_page()
                failed.route("**/culinary_explorer.json", lambda route: route.abort())
                failed.goto(base + "culinary-explorer.html")
                expect(failed.locator("#status")).to_contain_text("No se pudo cargar")
                expect(failed.locator("#controls")).to_have_attribute("disabled", "")
                for field in ("#title", "#title-mode", "#ingredients", "#module", "#evidence"):
                    expect(failed.locator(field)).to_be_disabled()
                expect(failed.get_by_role("button", name="Buscar", exact=True)).to_be_disabled()
                expect(failed.get_by_role("button", name="Limpiar filtros")).to_be_disabled()
                empty = browser.new_page()
                empty_catalog = {**catalog, "recipes": [], "recipe_count": 0}
                empty.route("**/culinary_explorer.json",
                            lambda route: route.fulfill(json=empty_catalog))
                empty.goto(base + "culinary-explorer.html")
                expect(empty.locator("#title")).to_be_enabled()
                expect(empty.locator("#status")).to_have_text("El catálogo está vacío.")
                expect(empty.locator("#results article")).to_have_count(0)
                report["empty_catalog"] = True
                browser.close()
        finally:
            server.shutdown()
            server.server_close()
            worker.join()
    return {"source_commit": catalog["source_commit"], "recipes": catalog["recipe_count"],
            "browser": "Chromium", "passed": True, **report}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = exercise(args.site)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
