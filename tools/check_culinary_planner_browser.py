"""Recorridos del planificador, enlaces de catálogo y aislamiento de estado."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import shutil
import tempfile
import threading
from playwright.sync_api import sync_playwright, expect

PLANNER="novacoquinaria.culinary-planner"
SHOPPING="novacoquinaria.culinary-shopping"
PANTRY="novacoquinaria.culinary-pantry"
SELECTION="novacoquinaria.planner.recipe-selection"


def exercise(site):
    with tempfile.TemporaryDirectory() as directory:
        shutil.copytree(site,Path(directory)/"NovaCoquinaria")
        server=ThreadingHTTPServer(("127.0.0.1",0),partial(SimpleHTTPRequestHandler,directory=directory))
        thread=threading.Thread(target=server.serve_forever,daemon=True)
        thread.start()
        try:
            with sync_playwright() as p:
                browser=p.chromium.launch()
                ctx=browser.new_context(viewport={"width":390,"height":844},accept_downloads=True)
                page=ctx.new_page()
                errors=[]
                page.on("pageerror",lambda e:errors.append(str(e)))
                base=f"http://127.0.0.1:{server.server_port}/NovaCoquinaria/"
                page.goto(base)
                page.get_by_role("link",name="Abrir mi planificador").click()
                expect(page.locator("#entry-controls")).to_be_enabled()
                assert page.evaluate("(k)=>localStorage.getItem(k)",PLANNER) is None
                expect(page.locator("#week-grid button")).to_have_count(7)
                page.locator("#entry-date").fill("2026-11-21")
                page.locator("#entry-meal").select_option("lunch")
                page.locator("#entry-title").fill("Arroz casero")
                page.locator("#entry-notes").fill("<img src=x onerror=alert(1)>")
                page.locator("#entry-save").click()
                expect(page.locator("#status")).to_have_text("Comida añadida.")
                expect(page.locator("#day-entries article")).to_have_count(1)
                assert page.locator("#day-entries img").count()==0
                page.locator("#entry-date").fill("2026-11-21")
                page.locator("#entry-meal").select_option("dinner")
                page.locator("#entry-title").fill("Sopa")
                page.locator("#entry-save").click()
                expect(page.locator("#day-entries article")).to_have_count(2)
                page.locator("#filter-meal").select_option("lunch")
                expect(page.locator("#day-entries article")).to_have_count(1)
                page.locator("#filter-meal").select_option("")
                page.locator("#day-entries article").filter(has_text="Sopa").get_by_role("button",name="Editar").click()
                page.locator("#entry-date").fill("2026-11-22")
                page.locator("#entry-title").fill("Sopa de verduras")
                page.locator("#entry-save").click()
                expect(page.locator("#day-entries article")).to_have_count(1)
                page.locator("#day-previous").click()
                expect(page.locator("#day-heading")).to_contain_text("2026-11-21")
                page.locator("#week-next").click()
                expect(page.locator("#week-range")).to_contain_text("2026-11-23")
                page.locator("#week-previous").click()
                with page.expect_download() as download:
                    page.locator("#export").click()
                backup=Path(directory)/"planner.json"
                download.value.save_as(backup)
                assert len(json.loads(backup.read_text())["entries"])==2
                page.get_by_text("Importar copia de planificación").click()
                page.locator("#import-file").set_input_files(str(backup))
                expect(page.locator("#import-preview")).to_contain_text("2 entradas")
                page.locator("#import-cancel").click()
                assert page.evaluate("(k)=>localStorage.getItem(k)",SHOPPING) is None
                assert page.evaluate("(k)=>localStorage.getItem(k)",PANTRY) is None
                page.reload()
                expect(page.locator("#entry-controls")).to_be_enabled()
                document=page.evaluate("(k)=>JSON.parse(localStorage.getItem(k))",PLANNER)
                assert len(document["entries"])==2
                assert {e["date"] for e in document["entries"]}=={"2026-11-21","2026-11-22"}

                # Seleccionar explícitamente una receta desde Explorer.
                page.goto(base+"culinary-explorer.html")
                expect(page.locator("#results article").first).to_be_visible()
                page.locator("#results article").first.get_by_role("button",name="Planificar receta").click()
                page.once("dialog",lambda d:d.accept())
                # La anterior llamada puede emitir un diálogo síncrono; se registra antes de pulsar en la ruta real.
                expect(page).to_have_url(base+"culinary-planner.html")
                expect(page.locator("#entry-source")).to_contain_text("Receta seleccionada")
                assert page.evaluate("(k)=>sessionStorage.getItem(k)",SELECTION) is None
                page.locator("#entry-date").fill("2026-11-21")
                page.locator("#entry-save").click()
                expect(page.locator("#status")).to_have_text("Comida añadida.")
                doc=page.evaluate("(k)=>JSON.parse(localStorage.getItem(k))",PLANNER)
                recipes=[e for e in doc["entries"] if e["source"]["type"]=="recipe"]
                assert len(recipes)==1
                item=recipes[0]
                assert len(item["source"]["source_commit"])==40
                page.locator("#day-previous").click()
                page.locator("#day-next").click()
                card=page.locator("#day-entries article").filter(has_text=item["title"])
                expect(card.get_by_role("link",name="Abrir asistente")).to_have_count(1)
                href=card.get_by_role("link",name="Abrir asistente").get_attribute("href")
                assert href.startswith("recipe-assistant.html?id=")
                card.get_by_role("link",name="Abrir asistente").click()
                expect(page.locator("#assistant")).to_be_visible()

                # Selección directa desde Assistant; se vuelve a verificar con el catálogo.
                page.once("dialog",lambda d:d.accept())
                page.locator("#plan-recipe").click()
                expect(page.locator("#entry-source")).to_contain_text("Receta seleccionada")
                page.locator("#recipe-clear").click()
                expect(page.locator("#entry-source")).to_contain_text("Plato libre")
                # Un documento importado con referencia antigua no obtiene enlaces vivos.
                plan=page.evaluate("(k)=>JSON.parse(localStorage.getItem(k))",PLANNER)
                for e in plan["entries"]:
                    if e["source"]["type"]=="recipe":
                        e["source"]["source_commit"]="b"*40
                page.evaluate("([key,raw])=>localStorage.setItem(key,raw)",[PLANNER,json.dumps(plan)])
                page.reload()
                expect(page.locator("#entry-controls")).to_be_enabled()
                page.locator("#week-grid button").filter(has_text="21").click()
                recipe_card=page.locator("#day-entries article").filter(has_text=item["title"])
                expect(recipe_card).to_contain_text("Referencia de receta no verificada")
                expect(recipe_card.get_by_role("link",name="Abrir asistente")).to_have_count(0)
                assert page.evaluate("(k)=>localStorage.getItem(k)",SHOPPING) is None
                assert page.evaluate("(k)=>localStorage.getItem(k)",PANTRY) is None
                assert not errors,errors
                browser.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join()
    return {"passed":True,"browser":"Chromium","planner_week":True,"crud":True,
            "backup":True,"explorer_selection":True,"assistant_selection":True,
            "stale_reference_blocked":True,"local_only":True}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=exercise(args.site)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False))
