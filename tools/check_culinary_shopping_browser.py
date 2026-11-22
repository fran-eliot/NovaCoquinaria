"""Recorridos de Shopping y selección desde Recipe Assistant."""
import argparse
import hashlib
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
                # Revisar las cantidades propuestas con una receta real escalable.
                manifest=json.loads((site/"recipe_assistant"/"manifest.json").read_bytes())
                selected=None
                for identity in sorted(manifest["recipes"]):
                    filename=hashlib.sha256(identity.encode()).hexdigest()+".json"
                    candidate=json.loads((site/"recipe_assistant"/filename).read_bytes())
                    y=candidate.get("yield") or {}
                    try:
                        original=int(y["min"])
                    except (ValueError,TypeError,KeyError):
                        continue
                    if y.get("unit") not in ("racion","porcion") or y["min"]!=y["max"] or not 1<=original<24:
                        continue
                    for ingredient in candidate["ingredients"]:
                        q=ingredient["quantity"]
                        if (q["status"]=="exact" and q["approximate"] is False and
                            q["min"]==q["max"] and q["unit"] in ("g","kg","ml","cl","l") and
                            isinstance(q["min"],str) and q["min"].isdigit() and int(q["min"])>0):
                            selected=(identity,ingredient,original)
                            break
                    if selected:
                        break
                assert selected is not None, "Sin muestra escalable para Shopping"
                identity,ingredient,original=selected
                page.goto(base+"recipe-assistant.html?id="+identity)
                expect(page.locator("#assistant")).to_be_visible()
                page.locator("#scaling-target").fill(str(original+1))
                page.get_by_text("Seleccionar ingredientes para comprar",exact=True).click()
                page.locator("#shopping-selection input").nth(ingredient["position"]).check()
                page.once("dialog",lambda d:d.accept())
                page.locator("#send-shopping").click()
                expect(page.locator("#recipe-review")).to_be_visible()
                review=page.locator("#review-items fieldset")
                expect(review).to_have_count(1)
                amount=int(ingredient["quantity"]["min"])*(original+1)/original
                expected=("%0.3f"%amount).rstrip("0").rstrip(".")
                expect(review.locator("input").nth(2)).to_have_value(expected)
                expect(review.locator("input").nth(3)).to_have_value(ingredient["quantity"]["unit"])
                assert page.evaluate("(key)=>sessionStorage.getItem(key)",TRANSFER) is None
                review.locator("input").nth(2).fill("2")
                page.locator("#review-list").select_option(destination)
                page.once("dialog",lambda d:d.accept())
                page.locator("#review-confirm").click()
                expect(page.locator("#status")).to_have_text("Ingredientes añadidos a la lista.")
                document=page.evaluate("(key)=>JSON.parse(localStorage.getItem(key))",KEY)
                saved=[i for l in document["lists"] for i in l["items"] if
                       i["provenance"] and i["provenance"]["recipe_id"]==identity]
                assert len(saved)==1
                assert saved[0]["quantity"]=="2" and saved[0]["unit"]==ingredient["quantity"]["unit"]
                assert saved[0]["provenance"]["raw"]==ingredient["raw"]
                assert page.evaluate("(key)=>localStorage.getItem(key)",PANTRY) is None
                # Un artículo comprado no se incorpora hasta la revisión del destino.
                page.locator("#lists button").filter(has_text="Semanal").click()
                card=page.locator("#items article").filter(has_text="Arroz")
                card.get_by_role("button",name="Incorporar a despensa").click()
                expect(page.locator("#transfer-dialog")).to_be_visible()
                expect(page.locator("#transfer-location")).to_have_value("")
                page.locator("#transfer-cancel").click()
                assert page.evaluate("(key)=>localStorage.getItem(key)",PANTRY) is None
                card.get_by_role("button",name="Incorporar a despensa").click()
                page.locator("#transfer-location").select_option("pantry")
                page.locator("#transfer-date-type").select_option("best_before")
                page.locator("#transfer-date").fill("2030-01-15")
                page.once("dialog",lambda d:d.accept())
                page.locator("#transfer-confirm").click()
                expect(page.locator("#status")).to_have_text("Transferencia registrada en la despensa.")
                expect(card.get_by_role("checkbox")).to_be_disabled()
                expect(card.get_by_role("button",name="Incorporar a despensa")).to_have_count(0)
                document=page.evaluate("(key)=>JSON.parse(localStorage.getItem(key))",KEY)
                rice=document["lists"][0]["items"][0]
                assert rice["transfer"]["state"]=="completed"
                entries=page.evaluate("(key)=>JSON.parse(localStorage.getItem(key)).entries",PANTRY)
                assert entries==[rice["transfer"]["entry"]]
                assert entries[0]["date"]=="2030-01-15" and entries[0]["quantity"]=="1.50"
                page.goto(base+"culinary-pantry.html")
                expect(page.locator("#inventory article")).to_have_count(1)
                expect(page.locator("#inventory")).to_contain_text("Arroz")
                page.goto(base+"culinary-shopping.html")
                expect(page.locator("#items article")).to_have_count(1)
                expect(page.locator("#delete-list")).to_be_disabled()

                # Interrumpir únicamente la escritura final de Shopping.
                page.locator("#item-name").fill("Leche")
                page.locator("#save-item").click()
                milk=page.locator("#items article").filter(has_text="Leche")
                milk.get_by_role("checkbox").check()
                page.evaluate("""key=>{
                    const original=Storage.prototype.setItem;
                    Storage.prototype.setItem=function(k,v){
                        if(k===key&&JSON.parse(v).lists.some(l=>l.items.some(i=>i.name==="Leche"&&i.transfer?.state==="completed")))
                            throw Error("Fallo de finalización simulado");
                        return original.call(this,k,v);
                    };
                }""",KEY)
                milk.get_by_role("button",name="Incorporar a despensa").click()
                page.locator("#transfer-location").select_option("fridge")
                page.once("dialog",lambda d:d.accept())
                page.locator("#transfer-confirm").click()
                expect(page.locator("#status")).to_contain_text("No se completó la transferencia")
                expect(milk).to_contain_text("Transferencia pendiente")
                assert page.evaluate("(key)=>JSON.parse(localStorage.getItem(key)).entries.length",PANTRY)==2
                page.reload()
                milk=page.locator("#items article").filter(has_text="Leche")
                expect(milk.get_by_role("button",name="Verificar transferencia pendiente")).to_be_enabled()
                page.once("dialog",lambda d:d.accept())
                milk.get_by_role("button",name="Verificar transferencia pendiente").click()
                expect(page.locator("#status")).to_have_text("Transferencia registrada en la despensa.")
                assert page.evaluate("(key)=>JSON.parse(localStorage.getItem(key)).entries.length",PANTRY)==2
                expect(milk.get_by_role("button",name="Verificar transferencia pendiente")).to_have_count(0)

                # Fallo previo al alta: la recuperación no puede volver a crear el lote.
                page.locator("#item-name").fill("Limón")
                page.locator("#save-item").click()
                lemon=page.locator("#items article").filter(has_text="Limón")
                lemon.get_by_role("checkbox").check()
                page.evaluate("""key=>{
                    const original=Storage.prototype.setItem;
                    Storage.prototype.setItem=function(k,v){
                        if(k===key)throw Error("Fallo de despensa simulado");
                        return original.call(this,k,v);
                    };
                }""",PANTRY)
                lemon.get_by_role("button",name="Incorporar a despensa").click()
                page.locator("#transfer-location").select_option("fridge")
                page.once("dialog",lambda d:d.accept())
                page.locator("#transfer-confirm").click()
                expect(lemon).to_contain_text("Transferencia pendiente")
                page.reload()
                lemon=page.locator("#items article").filter(has_text="Limón")
                page.once("dialog",lambda d:d.accept())
                lemon.get_by_role("button",name="Verificar transferencia pendiente").click()
                expect(page.locator("#status")).to_contain_text("No se acredita el destino exacto")
                assert page.evaluate("(key)=>JSON.parse(localStorage.getItem(key)).entries.length",PANTRY)==2
                expect(lemon).to_contain_text("Transferencia pendiente")
                assert not errors, errors
                browser.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join()
    return {"passed":True,"browser":"Chromium","lists":True,"backup":True,"recipe_selection":True,"pantry_unchanged_before_transfer":True,"pantry_transfer":True,"partial_recovery":True,"no_repeat_when_absent":True}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=exercise(args.site)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False))
