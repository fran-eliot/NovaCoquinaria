"""E07: recorrido dirigido de las ocho fichas de la muestra editorial en Chromium.

Contrasta el sitio construido localmente. No afirma prueba manual pública ni calidad
culinaria, y no escribe datos persistentes de Planner, Shopping o Pantry.
"""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import shutil
import tempfile
import threading

from playwright.sync_api import expect, sync_playwright


SAMPLE = (
    ("B01", "REC-0007"),
    ("B02", "REC-0009"),
    ("B03", "REC-0008"),
    ("B04", "REC-0021"),
    ("B05", "REC-448"),
    ("B06", "REC-0057"),
    ("B07", "REC-0059"),
    ("B08", "REC-0201"),
)


def exercise(site: Path) -> dict:
    catalog = json.loads((site / "culinary_explorer.json").read_bytes())
    manifest = json.loads((site / "recipe_assistant/manifest.json").read_bytes())
    recipes = {r["id"]: r for r in catalog["recipes"]}
    assert catalog["source_commit"] == manifest["source_commit"]
    assert len(SAMPLE) == len({identity for _, identity in SAMPLE})
    assert all(identity in recipes for _, identity in SAMPLE)

    results = []
    with tempfile.TemporaryDirectory() as directory:
        shutil.copytree(site, Path(directory) / "NovaCoquinaria")
        server = ThreadingHTTPServer(
            ("127.0.0.1", 0),
            partial(SimpleHTTPRequestHandler, directory=directory),
        )
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            base = f"http://127.0.0.1:{server.server_port}/NovaCoquinaria/"
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch()
                for case, identity in SAMPLE:
                    context = browser.new_context(viewport={"width": 390, "height": 844})
                    page = context.new_page()
                    errors = []
                    page.on("pageerror", lambda err: errors.append(str(err)))
                    title = recipes[identity]["title"]

                    page.goto(base + "culinary-explorer.html")
                    expect(page.locator("#title")).to_be_enabled(timeout=15000)
                    page.locator("#title").fill(title)
                    page.locator("#title-mode").select_option("exact")
                    page.get_by_role("button", name="Buscar", exact=True).click()
                    entry = page.locator("#results article").first
                    expect(entry.locator("h3 a")).to_have_text(title)
                    entry.get_by_role("link", name="Preparar receta", exact=True).click()

                    expect(page.locator("#assistant")).to_be_visible(timeout=15000)
                    expect(page.locator("#recipe-title")).to_have_text(title)
                    assert page.url == base + f"recipe-assistant.html?id={identity}"
                    assert page.locator("#ingredients input").count() > 0
                    expect(page.locator("#step-title")).to_contain_text("Paso")
                    assert page.locator("#context-text").inner_text().strip()
                    assert page.locator("#source-link").get_attribute("href")
                    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
                    page.locator("#source-link").click()
                    assert page.url.startswith(base) and page.url.endswith(".html")
                    expect(page.locator("h1").first).to_be_visible(timeout=15000)
                    assert not errors, (case, identity, errors)
                    results.append({
                        "case": case,
                        "id": identity,
                        "title": title,
                        "explorer_exact_search": True,
                        "assistant_opened": True,
                        "assistant_ingredients_steps_context": True,
                        "source_opened": True,
                        "no_page_errors": True,
                        "mobile_width": 390,
                    })
                    context.close()
                browser.close()
        finally:
            server.shutdown()
            server.server_close()
            worker.join()

    return {
        "stage": "editorial_sample_e07_local_browser",
        "source_commit": catalog["source_commit"],
        "browser": "Chromium",
        "scope": "Local build and eight directed journeys; not manual public acceptance or culinary validation",
        "sample_count": len(SAMPLE),
        "cases": results,
        "passed": len(results) == len(SAMPLE),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = exercise(args.site)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
