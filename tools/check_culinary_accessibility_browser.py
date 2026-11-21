"""CWC Unidad C: comprobaciones dirigidas de teclado, foco y ancho móvil.

No equivale a auditoría WCAG ni prueba manual en dispositivos reales.
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

PAGES={
  "culinary-explorer.html":{"ready":"#controls","status":"#status"},
  "recipe-assistant.html?id=REC-0017":{"ready":"#assistant","status":"#load-status"},
  "culinary-pantry.html":{"ready":"#entry-controls","status":"#status"},
  "culinary-shopping.html":{"ready":"#list-controls","status":"#status"},
  "culinary-planner.html":{"ready":"#entry-controls","status":"#status"},
}


def exercise(site):
    with tempfile.TemporaryDirectory() as directory:
        shutil.copytree(site,Path(directory)/"NovaCoquinaria")
        server=ThreadingHTTPServer(("127.0.0.1",0),
                                   partial(SimpleHTTPRequestHandler,directory=directory))
        thread=threading.Thread(target=server.serve_forever,daemon=True)
        thread.start()
        try:
            with sync_playwright() as p:
                browser=p.chromium.launch()
                results=[]
                try:
                    for width in (320,390,1280):
                        context=browser.new_context(viewport={"width":width,"height":800})
                        try:
                            page=context.new_page()
                            errors=[]
                            page.on("pageerror",lambda error:errors.append(str(error)))
                            base=f"http://127.0.0.1:{server.server_port}/NovaCoquinaria/"
                            for name,settings in PAGES.items():
                                page.goto(base+name)
                                ready=page.locator(settings["ready"])
                                if name.startswith("recipe-assistant"):
                                    expect(ready).to_be_visible()
                                else:
                                    expect(ready).to_be_enabled()
                                expect(page.locator(settings["status"])).to_have_attribute("role","status")
                                skip=page.get_by_role("link",name="Saltar al contenido principal")
                                expect(skip).to_have_count(1)
                                page.keyboard.press("Tab")
                                expect(skip).to_be_focused()
                                assert skip.evaluate("(el)=>{const r=el.getBoundingClientRect();return r.bottom>0 && r.top>=0 && r.left>=0 && r.width>0 && r.height>0}"),name
                                page.keyboard.press("Enter")
                                expect(page.locator("#main-content")).to_be_focused()
                                metrics=page.evaluate("""()=>({
                                  inner:window.innerWidth,
                                  document:document.documentElement.scrollWidth,
                                  main:document.querySelector("main").scrollWidth
                                })""")
                                assert metrics["document"]<=metrics["inner"]+1,(name,width,metrics)
                                assert not errors,(name,width,errors)
                                results.append({"page":name,"width":width,"skip":True,"status":True,"overflow":False})
                            if width==390:
                                # Focus and keyboard action in Planner: date selection does not write data.
                                page.goto(base+"culinary-planner.html")
                                expect(page.locator("#entry-controls")).to_be_enabled()
                                first=page.locator("#week-grid button").first
                                first.focus()
                                expect(first).to_be_focused()
                                page.keyboard.press("Enter")
                                expect(page.locator("#day-heading")).to_be_focused()
                                assert page.evaluate("()=>localStorage.getItem('novacoquinaria.culinary-planner')") is None
                                # Native invalid form prevents a write; status remains readable.
                                page.locator("#entry-title").fill("")
                                page.locator("#entry-save").click()
                                assert page.locator("#entry-title").evaluate("(el)=>el.validity.valueMissing")
                                assert page.evaluate("()=>localStorage.getItem('novacoquinaria.culinary-planner')") is None
                        finally:
                            context.close()
                finally:
                    browser.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join()
    return {"passed":True,"browser":"Chromium","scope":"directed-keyboard-and-responsive",
            "cases":len(results),"widths":[320,390,1280],
            "applications":5,"skip_navigation":True,"status_roles":True,
            "horizontal_overflow":False,"planner_keyboard":True,
            "real_device_audit":False}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=exercise(args.site)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False))
