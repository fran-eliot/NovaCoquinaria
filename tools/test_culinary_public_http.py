"""Offline contract tests for public read-only HTTP smoke."""
import json
import unittest
from urllib.error import URLError

from tools.check_culinary_public_http import PAGES, allowed_path, inspect

BASE = "https://example.test/NovaCoquinaria/"
SHA = "a" * 40


class FakeResponse:
    status = 200
    def __init__(self, url, value):
        self.url, self.value = url, value
    def getcode(self):
        return self.status
    def geturl(self):
        return self.url
    def read(self, count):
        return self.value[:count]
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return None


def fixture():
    data = {}
    for page in PAGES:
        prefix = page[:-5]
        html = (f"<html><head><title>{prefix}</title>"
                f'<link href="assets/culinary-explorer.css" rel="stylesheet">'
                f'<script src="assets/{prefix}-ui.{"b" * 20}.mjs"></script>'
                f'</head><body><a class="skip-link" href="#main-content">Saltar al contenido principal</a>'
                f'<main id="main-content" tabindex="-1"></main></body></html>')
        data[page] = html.encode()
        data[f"assets/{prefix}-ui.{'b' * 20}.mjs"] = b"export const ok=true;"
    data["assets/culinary-explorer.css"] = b"body{margin:0}"
    data["culinary_explorer.json"] = json.dumps({
        "source_commit": SHA, "index_sha256": "0" * 64, "recipe_count": 1,
        "recipes": [{"id": "REC-0017"}],
    }).encode()
    data["recipe_assistant/manifest.json"] = json.dumps({
        "source_commit": SHA, "index_sha256": "0" * 64, "recipe_count": 1,
        "recipes": {"REC-0017": "record"},
    }).encode()
    return data


class PublicSmokeTests(unittest.TestCase):
    def opener(self, data, seen):
        def open_url(request, timeout):
            path = request.full_url.removeprefix(BASE)
            seen.append((request.get_method(), path))
            if path not in data:
                raise URLError("Not found")
            return FakeResponse(request.full_url, data[path])
        return open_url

    def test_five_pages_and_assets_no_writes(self):
        data, seen = fixture(), []
        result = inspect(BASE, self.opener(data, seen))
        self.assertTrue(result["passed"])
        self.assertEqual(len(result["pages"]), 5)
        self.assertEqual(result["catalog_recipes"], 1)
        self.assertEqual(result["assets_checked"], 6)
        self.assertFalse(result["manual_browser_acceptance"])
        self.assertTrue(all(method == "GET" for method, _ in seen))

    def test_missing_skip_link_is_rejected(self):
        data, seen = fixture(), []
        data["culinary-planner.html"] = data["culinary-planner.html"].replace(b'skip-link', b'unknown')
        with self.assertRaisesRegex(ValueError, "keyboard skip"):
            inspect(BASE, self.opener(data, seen))

    def test_catalog_manifest_mismatch_is_rejected(self):
        data, seen = fixture(), []
        manifest = json.loads(data["recipe_assistant/manifest.json"])
        manifest["source_commit"] = "c" * 40
        data["recipe_assistant/manifest.json"] = json.dumps(manifest).encode()
        with self.assertRaisesRegex(ValueError, "disagreement"):
            inspect(BASE, self.opener(data, seen))

    def test_missing_asset_is_not_accepted(self):
        data, seen = fixture(), []
        del data["assets/culinary-shopping-ui." + "b" * 20 + ".mjs"]
        with self.assertRaises(URLError):
            inspect(BASE, self.opener(data, seen))

    def test_bad_paths_and_redirects_are_rejected(self):
        for path in ("//evil.example/m.js", "../p", "/private", "a?b", "a/%2e%2e", "a//b"):
            with self.subTest(path=path):
                with self.assertRaises(ValueError):
                    allowed_path(path)
        with self.assertRaisesRegex(ValueError, "end with"):
            inspect("https://example.test/NovaCoquinaria", self.opener(fixture(), []))


if __name__ == "__main__":
    unittest.main()
