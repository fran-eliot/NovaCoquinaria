"""Offline checks for public-browser smoke scope and origin restrictions."""
import unittest

from tools.check_culinary_public_browser import DEFAULT_BASE, PAGES, check_base


class PublicBrowserContractTests(unittest.TestCase):
    def test_exact_public_origin(self):
        self.assertIsNone(check_base(DEFAULT_BASE))
        for url in ("http://fran-eliot.github.io/NovaCoquinaria/",
                    "https://example.com/NovaCoquinaria/",
                    "https://fran-eliot.github.io/Other/",
                    DEFAULT_BASE + "?external=true"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                check_base(url)

    def test_five_distinct_applications(self):
        self.assertEqual(len(PAGES), 5)
        self.assertEqual(len({path.split("?")[0] for path, _ in PAGES}), 5)
        self.assertTrue(all(selector.startswith("#") for _, selector in PAGES))


if __name__ == "__main__":
    unittest.main()
