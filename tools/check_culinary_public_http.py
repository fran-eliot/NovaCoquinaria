"""Public HTTP read-only smoke: pages, assets, catalog and manifest.

This is network evidence, not manual functional acceptance or a browser test.
"""
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen

DEFAULT_BASE = "https://fran-eliot.github.io/NovaCoquinaria/"
PAGES = (
    "culinary-explorer.html",
    "recipe-assistant.html",
    "culinary-pantry.html",
    "culinary-shopping.html",
    "culinary-planner.html",
)
MAX_BYTES = 8_000_000
TIMEOUT = 15


def allowed_path(relative):
    """Reject origin changes, path traversal and unbounded URLs from HTML."""
    if not isinstance(relative, str) or not relative or len(relative) > 250:
        raise ValueError("Resource path invalid")
    u = urlsplit(relative)
    if u.scheme or u.netloc or u.query or u.fragment or relative.startswith("/"):
        raise ValueError(f"Untrusted resource URL: {relative!r}")
    if any(v in ("", ".", "..") for v in u.path.split("/")) or "\\" in u.path:
        raise ValueError(f"Untrusted resource path: {relative!r}")
    if "%" in u.path:
        raise ValueError(f"Encoded resource path not accepted: {relative!r}")
    return relative


def fetch(base, relative, opener=urlopen):
    allowed_path(relative)
    url = urljoin(base, relative)
    if urlsplit(url).netloc != urlsplit(base).netloc:
        raise ValueError("Resource escaped expected origin")
    request = Request(url, headers={"User-Agent": "NovaCoquinaria-PublicSmoke/0.1", "Accept": "*/*"})
    response = opener(request, timeout=TIMEOUT)
    with response:
        status = getattr(response, "status", response.getcode())
        if status != 200:
            raise ValueError(f"HTTP {status}: {relative}")
        final = response.geturl()
        if urlsplit(final).netloc != urlsplit(base).netloc:
            raise ValueError(f"Redirected to unexpected origin: {relative}")
        body = response.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"Resource too large: {relative}")
    if not body:
        raise ValueError(f"Empty body: {relative}")
    return body


def extract_assets(page, text):
    scripts = re.findall(r'<script\b[^>]*\bsrc="([^"]+)"', text, re.I)
    css = re.findall(r'<link\b[^>]*\bhref="([^"]+\.css)"', text, re.I)
    prefix = page.removesuffix(".html")
    versioned = [
        path for path in scripts
        if re.fullmatch(rf"assets/{re.escape(prefix)}-ui\.[a-f0-9]{{20}}\.mjs", path)
    ]
    if len(versioned) != 1:
        raise ValueError(f"Missing unique fingerprinted app module: {page}")
    for path in (*scripts, *css):
        if not path.startswith("assets/"):
            raise ValueError(f"Unexpected external entry asset: {page}: {path}")
        allowed_path(path)
    return sorted(set((*scripts, *css)))


def inspect(base, opener=urlopen):
    parsed = urlsplit(base)
    if parsed.scheme not in ("https", "http") or not parsed.netloc or parsed.query or parsed.fragment:
        raise ValueError("Base URL must be an HTTP(S) directory")
    if not base.endswith("/"):
        raise ValueError("Base URL must end with /")
    records = []
    resources = set()
    for page in PAGES:
        document = fetch(base, page, opener).decode("utf-8")
        if '<a class="skip-link" href="#main-content">' not in document:
            raise ValueError(f"Missing keyboard skip link: {page}")
        if '<main id="main-content" tabindex="-1">' not in document:
            raise ValueError(f"Missing target landmark: {page}")
        if "<title>" not in document:
            raise ValueError(f"Missing document title: {page}")
        entry_assets = extract_assets(page, document)
        resources.update(entry_assets)
        records.append({"page": page, "http": 200, "skip_link": True,
                        "versioned_entry": True, "asset_count": len(entry_assets)})
    catalog = json.loads(fetch(base, "culinary_explorer.json", opener).decode("utf-8"))
    if not isinstance(catalog, dict) or not isinstance(catalog.get("recipes"), list) or not catalog["recipes"]:
        raise ValueError("Public catalog is empty or incompatible")
    if catalog.get("recipe_count") != len(catalog["recipes"]):
        raise ValueError("Public catalog count mismatch")
    manifest = json.loads(fetch(base, "recipe_assistant/manifest.json", opener).decode("utf-8"))
    for field in ("source_commit", "index_sha256", "recipe_count"):
        if catalog.get(field) != manifest.get(field):
            raise ValueError(f"Catalog/manifest disagreement: {field}")
    recipe_id = "REC-0017"
    entry = manifest.get("recipes", {}).get(recipe_id)
    if not isinstance(entry, dict):
        raise ValueError(f"Known recipe absent from assistant manifest: {recipe_id}")
    filename = hashlib.sha256(recipe_id.encode("utf-8")).hexdigest() + ".json"
    if entry.get("file") != filename:
        raise ValueError("Assistant recipe filename mismatch")
    raw_recipe = fetch(base, "recipe_assistant/" + filename, opener)
    if hashlib.sha256(raw_recipe).hexdigest() != entry.get("sha256"):
        raise ValueError("Assistant recipe payload hash mismatch")
    recipe = json.loads(raw_recipe.decode("utf-8"))
    catalog_record = next((row for row in catalog["recipes"] if row.get("id") == recipe_id), None)
    if (not isinstance(recipe, dict) or not isinstance(catalog_record, dict)
            or recipe.get("id") != recipe_id
            or recipe.get("title") != catalog_record.get("title")
            or recipe.get("source_commit") != manifest.get("source_commit")
            or recipe.get("index_sha256") != manifest.get("index_sha256")
            or recipe.get("source_sha256") != entry.get("source_sha256")
            or recipe.get("href") != entry.get("href")
            or not isinstance(recipe.get("ingredients"), list) or not recipe["ingredients"]
            or not isinstance(recipe.get("steps"), list) or not recipe["steps"]):
        raise ValueError("Assistant recipe payload/catalog mismatch")
    for asset in sorted(resources):
        fetch(base, asset, opener)
    return {
        "passed": True,
        "scope": "public-http-read-only",
        "base_url": base,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "pages": records,
        "assets_checked": len(resources),
        "catalog_recipes": len(catalog["recipes"]),
        "source_commit": catalog["source_commit"],
        "assistant_manifest": True,
        "sample_recipe_id": recipe_id,
        "sample_recipe_integrity": True,
        "manual_browser_acceptance": False,
        "local_storage_tested": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default=DEFAULT_BASE)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = inspect(args.base_url)
    except (ValueError, UnicodeError, KeyError, json.JSONDecodeError, HTTPError, URLError, TimeoutError, OSError) as exc:
        result = {"passed": False, "scope": "public-http-read-only",
                  "base_url": args.base_url, "error": str(exc),
                  "manual_browser_acceptance": False}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
