"""Recorridos de Shopping y selección desde Recipe Assistant."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import shutil
import tempfile
import threading
from playwright.sync_api import sync_playwright, expect

KEY = "novacoquinaria.culinary-shopping"
PANTRY = "novacoquinaria.culinary-pantry"
TRANSFER = "novacoquinaria.shopping.recipe-selection"


def exercise(site):
    with tempfile.TemporaryDirectory() as directory:
        shutil.copytree(site, Path(directory) / "NovaCoquinaria")
        server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=directory))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                context = browser.new_context(viewport={"width":390,"height":844}, accept_downloads=True)
                page = context.new_page()
                errors = []
                page.on("pageerror", lambda e: errors.append(str(e)))
                base = f"http://127.0.0.1:{server.server_port}/NovaCoquinaria/"
                page.goto(base)
                page.get_by_role("link", name="Abrir mis compras").click()
                expect(page.locator("#list-name")).to_be_enabled()
                assert page.evaluate("(key)=>localStorage.getItem(key)", KEY) is None
                def create(name):
                    page.locator("#list-name").fill(name)
                    page.get_by_role("button",name="Crear lista").click()
                    expect(page.locator("#active-title")).to_have_text(name)
                create("Semanal")
                page.locator("#item-name").fill("Arroz")
                page.locator("#quantity").fill("1,50")
                page.locator("#unit").fill("kg")
                page.locator("#notes").fill("<img src=x onerror=alert(1)>")
                page.locator("#save-item").click()
                expect(page.locator("#items article")).to_have_count(1)
                assert page.locator("#items img").count()==0
                page.locator("#items input[type=checkbox]").check()
                expect(page.locator("#progress")).to_have_text("1 de 1 artículos comprados")
                page.locator("#filter-purchased").select_option("false")
                expect(page.locator("#items article")).to_have_count(0)
                page.locator("#filter-purchased").select_option("")
                create("Recetas")
                page.reload()
                expect(page.locator("#lists button")).to_have_count(2)
                page.locator("#lists button").filter(has_text="Semanal").click()
                expect(page.locator("#items")).to_contain_text("1.50 kg")
                with page.expect_download() as download:
                    page.locator("#export").click()
                backup=Path(directory)/"shopping.json"
                download.value.save_as(backup)
                assert len(json.loads(backup.read_text())["lists"])==2
                page.get_by_text("Recuperar una copia de seguridad",exact=True).click()
                page.locator("#import-file").set_input_files(str(backup))
                expect(page.locator("#import-preview")).to_contain_text("2 listas")
                page.locator("#import-cancel").click()
                assert page.evaluate("(key)=>localStorage.getItem(key)",PANTRY) is None
                page.set_viewport_size({"width":1280,"height":900})
                page.goto(base+"recipe-assistant.html?id=REC-0017")
                expect(page.locator("#assistant")).to_be_visible()
                page.get_by_text("Seleccionar ingredientes para comprar",exact=True).click()
                checks=page.locator("#shopping-selection input")
                expect(checks.first).to_be_visible()
                checks.first.check()
                page.once("dialog",lambda d:d.accept())
                page.locator("#send-shopping").click()
                expect(page.locator("#recipe-review")).to_be_visible()
                expect(page.locator("#review-items fieldset")).to_have_count(1)
                assert page.locator("#review-items input").nth(2).input_value()==""
                assert page.evaluate("(key)=>sessionStorage.getItem(key)",TRANSFER) is None
                destination=page.locator("#review-list option").filter(has_text="Recetas").get_attribute("value")
                page.locator("#review-list").select_option(destination)
                page.once("dialog",lambda d:d.accept())
                page.locator("#review-confirm").click()
                expect(page.locator("#status")).to_have_text("Ingredientes añadidos a la lista.")
                expect(page.locator("#items article")).to_have_count(1)
                document=page.evaluate("(key)=>JSON.parse(localStorage.getItem(key))",KEY)
                item=next(l for l in document["lists"] if l["name"]=="Recetas")["items"][0]
                assert item["provenance"]["recipe_id"]=="REC-0017" and item["quantity"] is None
                assert page.evaluate("(key)=>localStorage.getItem(key)",PANTRY) is None
                assert not errors, errors
                browser.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join()
    return {"passed":True,"browser":"Chromium","lists":True,"backup":True,"recipe_selection":True,"pantry_unchanged":True}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=exercise(args.site)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False))
