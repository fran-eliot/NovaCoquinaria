"""Recorridos reales de despensa y transferencia local bajo el subdirectorio del portal."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import shutil
import tempfile
import threading
from playwright.sync_api import sync_playwright, expect

KEY = "novacoquinaria.culinary-pantry"
TRANSFER = "novacoquinaria.pantry.mentions"


def exercise(site):
    with tempfile.TemporaryDirectory() as directory:
        shutil.copytree(site, Path(directory) / "NovaCoquinaria")
        server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=directory))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                context = browser.new_context(viewport={"width": 390, "height": 844}, accept_downloads=True)
                page = context.new_page()
                errors, requests = [], []
                page.on("pageerror", lambda error: errors.append(str(error)))
                page.on("request", lambda request: requests.append((request.url, request.method, request.post_data)))
                base = f"http://127.0.0.1:{server.server_port}/NovaCoquinaria/"
                page.goto(base)
                page.get_by_role("link", name="Abrir mi despensa").click()
                expect(page.locator("#name")).to_be_enabled()
                expect(page.locator("#inventory-count")).to_have_text("Inventario vacío.")
                assert page.evaluate("(key)=>localStorage.getItem(key)", KEY) is None

                def add(name, qty="", unit="", location="pantry", category="", date="", notes=""):
                    page.locator("#name").fill(name)
                    page.locator("#quantity").fill(qty)
                    page.locator("#unit").fill(unit)
                    page.locator("#location").select_option(location)
                    page.locator("#category").fill(category)
                    if date:
                        page.locator("#date-type").select_option("best_before")
                        page.locator("#date").fill(date)
                    page.locator("#notes").fill(notes)
                    page.locator("#save-entry").click()
                    expect(page.locator("#status")).to_have_text("Alimento guardado.")

                add("ajo", "1,50", "kg", category="Vegetales", date="2000-01-01", notes="<img src=x onerror=alert(1)> privado123")
                add("ajo", "2", "unidades", "freezer")
                add("salsa de soja")
                expect(page.locator("#inventory article")).to_have_count(3)
                assert page.locator("#inventory img").count() == 0
                assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
                page.reload()
                expect(page.locator("#inventory article")).to_have_count(3)
                page.locator("#filter-location").select_option("freezer")
                expect(page.locator("#inventory article")).to_have_count(1)
                page.get_by_role("button", name="Editar", exact=True).click()
                page.locator("#quantity").fill("3")
                page.locator("#save-entry").click()
                expect(page.locator("#status")).to_have_text("Cambios guardados.")
                expect(page.locator("#inventory")).to_contain_text("3 unidades")
                page.locator("#filter-location").select_option("")
                page.locator("#filter-date").select_option("past")
                expect(page.locator("#inventory article")).to_have_count(1)
                page.locator("#filter-date").select_option("")
                with page.expect_download() as download:
                    page.locator("#export").click()
                saved = Path(directory) / "backup.json"
                download.value.save_as(saved)
                backup = json.loads(saved.read_text(encoding="utf-8"))
                assert len(backup["entries"]) == 3 and backup["entries"][0]["quantity"] == "1.50"
                page.locator("#import-file").set_input_files({"name":"invalid.json","mimeType":"application/json","buffer":b"{}"})
                expect(page.locator("#import-confirm")).to_be_disabled()
                page.locator("#import-file").set_input_files(str(saved))
                expect(page.locator("#import-preview")).to_contain_text("3 entradas")
                page.locator("#import-cancel").click()
                expect(page.locator("#inventory article")).to_have_count(3)
                page.once("dialog", lambda d: d.accept())
                page.locator("#inventory article").nth(1).get_by_role("button",name="Eliminar").click()
                expect(page.locator("#inventory article")).to_have_count(2)
                page.locator("#import-file").set_input_files(str(saved))
                expect(page.locator("#import-confirm")).to_be_enabled()
                page.once("dialog", lambda d: d.accept())
                page.locator("#import-confirm").click()
                expect(page.locator("#inventory article")).to_have_count(3)

                second = context.new_page()
                second.goto(base+"culinary-pantry.html")
                expect(second.locator("#inventory article")).to_have_count(3)
                second.locator("#name").fill("limón")
                second.locator("#save-entry").click()
                expect(second.locator("#status")).to_have_text("Alimento guardado.")
                expect(page.locator("#status")).to_contain_text("otra pestaña")
                expect(page.locator("#save-entry")).to_be_disabled()
                page.locator("#reload").click()
                expect(page.locator("#inventory article")).to_have_count(4)
                second.close()

                page.set_viewport_size({"width":1280,"height":900})
                page.locator("#inventory article").nth(0).locator("input").check()
                page.locator("#inventory article").nth(1).locator("input").check()
                page.locator("#inventory article").nth(2).locator("input").check()
                expect(page.locator("#selection-count")).to_contain_text("2 menciones")
                page.locator("#search-recipes").click()
                expect(page.locator("#ingredients")).to_have_value("ajo\nsalsa de soja")
                expect(page.locator("#pantry-notice")).to_contain_text("Menciones seleccionadas")
                assert page.url == base+"culinary-explorer.html"
                assert page.evaluate("(key)=>sessionStorage.getItem(key)", TRANSFER) is None
                expect(page.locator("#results article").first).to_be_visible()
                page.locator("#ingredients").fill("ajo")
                page.get_by_role("button",name="Buscar",exact=True).click()
                expect(page.locator("#results article").first).to_be_visible()
                page.reload()
                expect(page.locator("#ingredients")).to_have_value("")
                assert not errors, errors
                assert all(method == "GET" and body is None and "privado123" not in url and "salsa%20de%20soja" not in url for url,method,body in requests)
                page.goto(base+"culinary-pantry.html")
                expect(page.locator("#inventory article")).to_have_count(4)
                page.evaluate("(key)=>localStorage.setItem(key,'invalid')", KEY)
                page.reload()
                expect(page.locator("#name")).to_be_disabled()
                assert page.evaluate("(key)=>localStorage.getItem(key)", KEY) == "invalid"
                browser.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join()
    return {"passed":True,"browser":"Chromium","crud":True,"reload":True,"backup":True,"external_change":True,"transfer":True,"invalid_storage":True,"local_only":True}


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=exercise(args.site)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False))
