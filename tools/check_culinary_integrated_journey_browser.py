"""CWC Unidad A: un recorrido único y aislado entre cinco aplicaciones.

No prueba disponibilidad, cantidades necesarias, seguridad culinaria ni aceptación pública.
"""
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
PLANNER_SELECTION="novacoquinaria.planner.recipe-selection"
SHOPPING_SELECTION="novacoquinaria.shopping.recipe-selection"


def snapshot(page):
    return page.evaluate("""keys=>Object.fromEntries(keys.map(key=>[key,localStorage.getItem(key)]))""",
                         [PLANNER,SHOPPING,PANTRY])


def document(page,key):
    raw=page.evaluate("(key)=>localStorage.getItem(key)",key)
    return None if raw is None else json.loads(raw)


def exercise(site):
    with tempfile.TemporaryDirectory() as directory:
        shutil.copytree(site,Path(directory)/"NovaCoquinaria")
        server=ThreadingHTTPServer(("127.0.0.1",0),
                                   partial(SimpleHTTPRequestHandler,directory=directory))
        worker=threading.Thread(target=server.serve_forever,daemon=True)
        worker.start()
        try:
            with sync_playwright() as p:
                browser=p.chromium.launch()
                context=browser.new_context(viewport={"width":390,"height":844})
                page=context.new_page()
                errors=[]
                page.on("pageerror",lambda error:errors.append(str(error)))
                base=f"http://127.0.0.1:{server.server_port}/NovaCoquinaria/"
                try:
                    # Explorer → Planner: selection is transient, no persisted plan.
                    page.goto(base+"culinary-explorer.html")
                    expect(page.locator("#results article").first).to_be_visible()
                    initial=snapshot(page)
                    assert all(value is None for value in initial.values())
                    page.once("dialog",lambda dialog:dialog.accept())
                    page.locator("#results article").first.get_by_role(
                        "button",name="Planificar receta").click()
                    expect(page).to_have_url(base+"culinary-planner.html")
                    expect(page.locator("#entry-source")).to_contain_text("Receta seleccionada")
                    assert page.evaluate("(key)=>sessionStorage.getItem(key)",PLANNER_SELECTION) is None
                    assert snapshot(page)==initial
                    chosen=page.locator("#entry-title").input_value()
                    assert chosen
                    page.locator("#entry-date").fill("2026-11-21")
                    page.locator("#entry-meal").select_option("lunch")
                    page.locator("#entry-save").click()
                    expect(page.locator("#status")).to_have_text("Comida añadida.")
                    planned=document(page,PLANNER)
                    assert len(planned["entries"])==1
                    entry=planned["entries"][0]
                    assert entry["title"]==chosen and entry["source"]["type"]=="recipe"
                    assert document(page,SHOPPING) is None and document(page,PANTRY) is None

                    # Planner → Assistant: a verified historical recipe reference only.
                    card=page.locator("#day-entries article").filter(has_text=chosen)
                    expect(card.get_by_role("link",name="Abrir asistente")).to_have_count(1)
                    card.get_by_role("link",name="Abrir asistente").click()
                    expect(page.locator("#assistant")).to_be_visible()
                    assert document(page,PLANNER)==planned
                    assert document(page,SHOPPING) is None and document(page,PANTRY) is None

                    # Assistant → Shopping: occurrence selected by user, no implied quantity.
                    page.get_by_text("Seleccionar ingredientes para comprar",exact=True).click()
                    checks=page.locator("#shopping-selection input[type=checkbox]")
                    expect(checks.first).to_be_visible()
                    checks.first.check()
                    assert document(page,SHOPPING) is None and document(page,PANTRY) is None
                    page.once("dialog",lambda dialog:dialog.accept())
                    page.locator("#send-shopping").click()
                    expect(page).to_have_url(base+"culinary-shopping.html")
                    expect(page.locator("#recipe-review")).to_be_visible()
                    assert document(page,SHOPPING) is None and document(page,PANTRY) is None
                    assert page.evaluate("(key)=>sessionStorage.getItem(key)",SHOPPING_SELECTION) is None
                    review=page.locator("#review-items fieldset")
                    expect(review).to_have_count(1)
                    assert review.locator("input").nth(2).input_value()==""
                    # User creates a shopping list, then reviews the chosen occurrence.
                    page.locator("#list-name").fill("Recorrido integrado")
                    page.get_by_role("button",name="Crear lista").click()
                    expect(page.locator("#active-title")).to_have_text("Recorrido integrado")
                    assert document(page,PANTRY) is None
                    page.locator("#review-list").select_option(
                        page.locator("#review-list option").filter(
                            has_text="Recorrido integrado").get_attribute("value"))
                    assert len(document(page,SHOPPING)["lists"][0]["items"])==0
                    page.once("dialog",lambda dialog:dialog.accept())
                    page.locator("#review-confirm").click()
                    expect(page.locator("#status")).to_have_text("Ingredientes añadidos a la lista.")
                    shopping=document(page,SHOPPING)
                    assert len(shopping["lists"])==1 and len(shopping["lists"][0]["items"])==1
                    item=shopping["lists"][0]["items"][0]
                    assert item["provenance"]["recipe_id"]==entry["source"]["recipe_id"]
                    assert item["quantity"] is None and item["unit"] is None
                    assert not item["purchased"] and item["transfer"] is None
                    assert document(page,PANTRY) is None
                    assert document(page,PLANNER)==planned

                    # Purchased does not mean stocked.
                    card=page.locator("#items article").first
                    card.get_by_role("checkbox").check()
                    expect(page.locator("#progress")).to_have_text("1 de 1 artículos comprados")
                    assert document(page,PANTRY) is None
                    assert document(page,SHOPPING)["lists"][0]["items"][0]["transfer"] is None

                    # Cancelled transfer must not create a Pantry record.
                    card.get_by_role("button",name="Incorporar a despensa").click()
                    expect(page.locator("#transfer-dialog")).to_be_visible()
                    expect(page.locator("#transfer-location")).to_have_value("")
                    page.locator("#transfer-cancel").click()
                    assert document(page,PANTRY) is None
                    assert document(page,SHOPPING)["lists"][0]["items"][0]["transfer"] is None

                    # Explicitly reviewed destination, with quantity and unit declared by user.
                    card.get_by_role("button",name="Incorporar a despensa").click()
                    page.locator("#transfer-quantity").fill("2")
                    page.locator("#transfer-unit").fill("unidades")
                    page.locator("#transfer-location").select_option("pantry")
                    page.once("dialog",lambda dialog:dialog.accept())
                    page.locator("#transfer-confirm").click()
                    expect(page.locator("#status")).to_have_text(
                        "Transferencia registrada en la despensa.")
                    shopping=document(page,SHOPPING)
                    recorded=shopping["lists"][0]["items"][0]
                    assert recorded["transfer"]["state"]=="completed"
                    pantry=document(page,PANTRY)
                    assert pantry["entries"]==[recorded["transfer"]["entry"]]
                    assert pantry["entries"][0]["quantity"]=="2"
                    assert pantry["entries"][0]["unit"]=="unidades"
                    assert document(page,PLANNER)==planned
                    expect(card.get_by_role("checkbox")).to_be_disabled()

                    # Pantry UI displays the actual destination. Repeated navigation is read-only.
                    page.goto(base+"culinary-pantry.html")
                    expect(page.locator("#inventory article")).to_have_count(1)
                    expect(page.locator("#inventory")).to_contain_text(pantry["entries"][0]["name"])
                    after=snapshot(page)
                    page.reload()
                    expect(page.locator("#inventory article")).to_have_count(1)
                    assert snapshot(page)==after
                    page.goto(base+"culinary-planner.html")
                    expect(page.locator("#entry-controls")).to_be_enabled()
                    assert document(page,PLANNER)==planned
                    assert snapshot(page)==after
                    assert not errors,errors
                finally:
                    context.close()
                    browser.close()
        finally:
            server.shutdown()
            server.server_close()
            worker.join()
    return {"passed":True,"browser":"Chromium","scope":"local-ephemeral",
            "explorer_to_planner":True,"planner_to_assistant":True,
            "assistant_to_shopping":True,"shopping_to_pantry":True,
            "explicit_reviews":True,"no_implicit_stock":True,
            "source_traceability":True,"state_isolation":True,"reload_stability":True}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=exercise(args.site)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False))
