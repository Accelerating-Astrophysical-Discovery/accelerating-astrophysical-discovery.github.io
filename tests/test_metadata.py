from __future__ import annotations

import unittest
from html.parser import HTMLParser
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import urlsplit

from jinja2 import Environment, FileSystemLoader, select_autoescape
from PIL import Image

from sitegen.build import build
from sitegen.content import SiteConfig


ROOT = Path(__file__).resolve().parents[1]
DESCRIPTION = "The open-science consortium steering how humans and machines will jointly study the cosmos."


class HeadParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_head = False
        self.meta: dict[str, list[str]] = {}
        self.links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "head":
            self.in_head = True
        if not self.in_head:
            return
        values = {key: value for key, value in attrs if value is not None}
        if tag == "meta":
            key = values.get("property", values.get("name", ""))
            self.meta.setdefault(key, []).append(values.get("content", ""))
        elif tag == "link":
            self.links.append(values)

    def handle_endtag(self, tag: str) -> None:
        if tag == "head":
            self.in_head = False


class MetadataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.output = Path(cls.temp.name) / "site"
        cls.data = build(ROOT, cls.output, production=True)

    def read_head(self, path: Path) -> HeadParser:
        parser = HeadParser()
        parser.feed(path.read_text(encoding="utf-8"))
        return parser

    def test_every_page_has_description_and_absolute_social_metadata(self) -> None:
        for page in self.output.rglob("*.html"):
            with self.subTest(page=page.relative_to(self.output)):
                head = self.read_head(page)
                for key in ("description", "og:description", "twitter:description"):
                    self.assertEqual(head.meta[key], [DESCRIPTION])
                self.assertEqual(head.meta["og:site_name"], [self.data.config.title])
                self.assertEqual(head.meta["og:title"], head.meta["twitter:title"])
                self.assertEqual(head.meta["og:image"], head.meta["twitter:image"])
                self.assertEqual(head.meta["twitter:card"], ["summary"])
                self.assertEqual(head.meta["og:image:type"], ["image/png"])
                self.assertEqual(head.meta["og:image:width"], ["512"])
                self.assertEqual(head.meta["og:image:height"], ["512"])
                self.assertTrue(head.meta["og:image:alt"][0])
                self.assertTrue(head.meta["twitter:image:alt"][0])
                image_url = urlsplit(head.meta["og:image"][0])
                self.assertEqual(image_url.scheme, "https")
                self.assertEqual(image_url.netloc, urlsplit(self.data.config.base_url).netloc)
                self.assertTrue((self.output / image_url.path.lstrip("/")).is_file())

    def test_canonical_urls_identify_each_page(self) -> None:
        for page in self.output.rglob("*.html"):
            relative = page.relative_to(self.output).as_posix()
            route = "/" + relative.removesuffix("index.html")
            expected = self.data.config.base_url + route
            with self.subTest(route=route):
                head = self.read_head(page)
                self.assertEqual(head.meta["og:url"], [expected])
                self.assertEqual(
                    [link["href"] for link in head.links if link["rel"] == "canonical"],
                    [expected],
                )

    def test_article_previews_use_readable_titles_without_changing_comment_ids(self) -> None:
        for item in self.data.news + self.data.consortium:
            path = self.output / item.section / item.slug / "index.html"
            head = self.read_head(path)
            self.assertEqual(head.meta["og:title"], [f"{item.title} | {self.data.config.title}"])
            self.assertEqual(head.meta["og:type"], ["article"])
            self.assertIn(f"<title>{item.giscus_term}</title>", path.read_text())
        self.assertEqual(self.read_head(self.output / "index.html").meta["og:type"], ["website"])

    def test_all_icon_links_resolve_and_raster_sizes_match(self) -> None:
        for page in self.output.rglob("*.html"):
            head = self.read_head(page)
            icons = [link for link in head.links if link["rel"] in ("icon", "apple-touch-icon")]
            self.assertEqual(len(icons), 4)
            for icon in icons:
                self.assertTrue((self.output / icon["href"].lstrip("/")).is_file())
        assets = self.output / "assets" / "branding"
        for name, size in (("icon-512.png", 512), ("favicon-48.png", 48), ("apple-touch-icon.png", 180)):
            with Image.open(assets / name) as image:
                self.assertEqual(image.size, (size, size))
                self.assertEqual(image.format, "PNG")
        with Image.open(self.output / "favicon.ico") as icon:
            self.assertEqual(icon.ico.sizes(), {(16, 16), (32, 32), (48, 48)})

    def test_description_is_shared_with_homepage_and_html_escaped(self) -> None:
        env = Environment(
            loader=FileSystemLoader(ROOT / "site" / "templates"),
            autoescape=select_autoescape(["html"]),
        )
        description = 'Science & discovery: "together" <always>'
        html = env.get_template("landing.html").render(
            site=SiteConfig(description=description), active="home", page_path="/",
        )
        head = HeadParser()
        head.feed(html)
        self.assertEqual(head.meta["description"], [description])
        self.assertIn('Science &amp; discovery: &#34;together&#34; &lt;always&gt;', html)
        self.assertNotIn('<always>', html)


if __name__ == "__main__":
    unittest.main()
