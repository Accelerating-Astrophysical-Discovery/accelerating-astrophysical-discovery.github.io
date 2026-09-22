from __future__ import annotations

import json
import unittest
from html.parser import HTMLParser
from pathlib import Path
from tempfile import TemporaryDirectory

from sitegen.build import build


ROOT = Path(__file__).resolve().parents[1]
POLICIES = {"/privacy/": "Privacy policy", "/terms/": "Terms of service"}


class PolicyLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_footer = False
        self.footer_count = 0
        self.links: list[tuple[str, bool, str | None]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "footer":
            self.in_footer = True
            self.footer_count += 1
        if tag == "a" and attributes.get("href") in POLICIES:
            self.links.append((
                attributes["href"], self.in_footer, attributes.get("aria-current"),
            ))

    def handle_endtag(self, tag: str) -> None:
        if tag == "footer":
            self.in_footer = False


class PolicyPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.output = Path(cls.temp.name) / "site"
        build(ROOT, cls.output, production=True)

    def test_every_page_links_to_policies_only_in_footer(self) -> None:
        pages = list(self.output.rglob("*.html"))
        self.assertGreaterEqual(len(pages), 7)
        for page in pages:
            with self.subTest(page=page.relative_to(self.output)):
                parser = PolicyLinkParser()
                parser.feed(page.read_text(encoding="utf-8"))
                self.assertEqual(parser.footer_count, 1)
                self.assertEqual(len(parser.links), 2)
                self.assertEqual({link[0] for link in parser.links}, set(POLICIES))
                self.assertTrue(all(link[1] for link in parser.links))

    def test_policies_are_standalone_readable_pages(self) -> None:
        for route, title in POLICIES.items():
            with self.subTest(route=route):
                html = (self.output / route.strip("/") / "index.html").read_text(
                    encoding="utf-8"
                )
                self.assertIn(f"<h1>{title}</h1>", html)
                self.assertIn(f"<title>{title} | Accelerating Astrophysical", html)
                self.assertIn('<time datetime="2026-09-22">', html)
                self.assertIn('href="mailto:jgalbert@caltech.edu"', html)
                self.assertNotIn("giscus.app/client.js", html)
                self.assertNotIn('class="speed-reader', html)
                self.assertNotIn("noindex", html)
                parser = PolicyLinkParser()
                parser.feed(html)
                self.assertEqual(
                    [(href, current) for href, _, current in parser.links],
                    [(href, "page" if href == route else None) for href in POLICIES],
                )

    def test_policies_are_not_news_or_consortium_posts(self) -> None:
        manifest = json.loads((self.output / "site-manifest.json").read_text())
        for section in ("news", "consortium"):
            self.assertTrue({"privacy", "terms"}.isdisjoint(manifest[section]))

    def test_homepage_describes_consortium(self) -> None:
        html = (self.output / "index.html").read_text(encoding="utf-8")
        self.assertIn(
            '<p class="landing-description">The open-science consortium steering '
            'how humans and machines will jointly study the cosmos.</p>',
            html,
        )
        self.assertNotIn("This site shares our work and supports", html)


if __name__ == "__main__":
    unittest.main()
