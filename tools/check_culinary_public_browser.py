"""Chromium smoke against the published site in fresh, disposable browser contexts.

This is automated public-browser evidence, not manual PUB-01–PUB-07 acceptance.
No forms are submitted to create, update, import or transfer local data.
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlsplit


DEFAULT_BASE = "https://fran-eliot.github.io/NovaCoquinaria/"
PAGES = (
    ("culinary-explorer.html", "#title"),
    ("recipe-assistant.html?id=REC-0017", "#assistant"),
    ("culinary-pantry.html", "#entry-controls"),
    ("culinary-shopping.html", "#list-controls"),
    ("culinary-planner.html", "#entry-controls"),
)


def check_base(base):
    parsed = urlsplit(base)
    if parsed.scheme != "https" or parsed.netloc != "fran-eliot.github.io" or parsed.path != "/NovaCoquinaria/" or parsed.query or parsed.fragment:
        raise ValueError("Only the official public NovaCoquinaria HTTPS base is allowed")


def exercise(base=DEFAULT_BASE):
    check_base(base)
    from playwright.sync_api import sync_playwright, expect
    records = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        try:
            for path, ready_selector in PAGES:
                context = browser.new_context(viewport={"width": 390, "height": 844},
                                              accept_downloads=False)
                page = context.new_page()
                errors = []
                page.on("pageerror", lambda error: errors.append(str(error)))
                try:
                    response = page.goto(urljoin(base, path), wait_until="domcontentloaded", timeout=30000)
                    if response is None or response.status != 200:
                        raise AssertionError(f"HTTP error opening {path}")
                    expect(page.locator(ready_selector)).to_be_visible(timeout=20000)
                    if path.startswith("culinary-explorer"):
                        expect(page.locator("#title")).to_be_enabled()
                        expect(page.locator("#results-section")).to_be_visible()
                        if page.locator("#results > *").count() == 0:
                            raise AssertionError("Explorer did not render catalog results")
                        page.locator("#title").fill("arroz")
                        page.get_by_role("button", name="Buscar", exact=True).click()
                        expect(page.locator("#results-section")).to_be_visible()
                        if page.locator("#results > *").count() == 0:
                            raise AssertionError("Explorer search returned no results for arroz")
                    elif path.startswith("recipe-assistant"):
                        expect(page.locator("#recipe-title")).not_to_be_empty()
                        if page.locator("#ingredients input").count() == 0:
                            raise AssertionError("Recipe Assistant has no ingredient controls")
                        if page.locator("#step-title").count() == 0:
                            raise AssertionError("Recipe Assistant has no guided steps")
                    else:
                        expect(page.locator(ready_selector)).to_be_enabled(timeout=20000)
                    if errors:
                        raise AssertionError(f"JavaScript errors on {path}: {errors[:3]}")
                    if page.evaluate("document.documentElement.scrollWidth > innerWidth"):
                        raise AssertionError(f"Horizontal overflow on mobile viewport: {path}")
                    records.append({"page": path, "http": 200, "javascript": "ready",
                                    "viewport_width": 390, "page_errors": 0})
                finally:
                    context.close()
        finally:
            browser.close()
    return {"passed": True, "scope": "public-chromium-disposable-read-only",
            "checked_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "base_url": base, "pages": records, "manual_browser_acceptance": False,
            "personal_storage_accessed": False, "mutating_ui_actions": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default=DEFAULT_BASE)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        report = exercise(args.base_url)
    except Exception as error:
        report = {"passed": False, "scope": "public-chromium-disposable-read-only",
                  "base_url": args.base_url, "error": str(error),
                  "manual_browser_acceptance": False}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
