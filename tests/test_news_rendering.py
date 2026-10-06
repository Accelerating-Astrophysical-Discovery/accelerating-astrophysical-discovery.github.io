from __future__ import annotations

import json
import re
import unittest
from dataclasses import replace
from html import escape
from pathlib import Path
from tempfile import TemporaryDirectory

from sitegen.build import build
from sitegen.content import ContentError
from sitegen.render import build_site, combined_news


ROOT = Path(__file__).resolve().parents[1]


class NewsRenderingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.output = Path(cls.temp.name) / "site"
        cls.data = build(ROOT, cls.output, production=True)

    def test_news_lists_both_collections_in_date_order(self) -> None:
        html = (self.output / "news" / "index.html").read_text()
        actual = re.findall(r'class="writing-row defocus-item" href="([^"]+)"', html)
        expected = sorted(
            self.data.news + self.data.consortium,
            key=lambda item: (-item.date_published.toordinal(), item.title.casefold(), item.slug.casefold()),
        )
        self.assertTrue(self.data.news)
        self.assertTrue(self.data.consortium)
        self.assertIn('<h1 class="defocus-item">News</h1>', html)
        self.assertEqual(actual, [f"/news/{item.slug}/" for item in expected])
        manifest = json.loads((self.output / "site-manifest.json").read_text())
        self.assertEqual(manifest["news"], [item.slug for item in expected])

    def test_navigation_has_news_and_members_without_consortium_section(self) -> None:
        for page in self.output.rglob("*.html"):
            with self.subTest(page=page.relative_to(self.output)):
                html = page.read_text()
                self.assertIn('href="/news/"', html)
                self.assertIn('href="/members/"', html)
                self.assertNotIn('href="/consortium/"', html)

    def test_articles_keep_body_and_comment_identity_under_news(self) -> None:
        for item in self.data.news + self.data.consortium:
            with self.subTest(slug=item.slug):
                html = (self.output / "news" / item.slug / "index.html").read_text()
                self.assertIn(item.body_html, html)
                self.assertIn(f"<title>{escape(item.giscus_term)}</title>", html)
                self.assertIn('class="section-return defocus-item" href="/news/">News</a>', html)
                self.assertIn('href="/news/" aria-current="page"', html)
                self.assertIn('data-mapping="title"', html)

    def test_legacy_routes_redirect_to_news_preserving_deep_links(self) -> None:
        for suffix in ["", *[f"{item.slug}/" for item in self.data.consortium]]:
            with self.subTest(suffix=suffix):
                html = (self.output / "consortium" / suffix / "index.html").read_text()
                target = f"/news/{suffix}"
                self.assertIn(f'<meta http-equiv="refresh" content="0; url={target}">', html)
                self.assertIn(f'window.location.replace("{target}" + window.location.search + window.location.hash)', html)
                self.assertIn(f'<link rel="canonical" href="{self.data.config.base_url}{target}">', html)
                self.assertTrue((self.output / target.strip("/") / "index.html").exists())
                self.assertNotIn("giscus.app/client.js", html)

    def test_shared_workshop_download_urls_remain_available(self) -> None:
        source = ROOT / "consortium" / "workshop-materials" / "workshop-participant-booklet.pdf"
        for section in ("consortium", "research"):
            with self.subTest(section=section):
                published = self.output / "assets" / "content" / section / "workshop-materials" / source.name
                self.assertEqual(source.read_bytes(), published.read_bytes())

    def test_duplicate_slugs_fail_before_existing_output_is_touched(self) -> None:
        conflicting = replace(self.data.consortium[0], slug=self.data.news[0].slug)
        data = replace(self.data, consortium=[conflicting])
        before = (self.output / "index.html").read_bytes()
        with self.assertRaisesRegex(ContentError, "Duplicate News slug"):
            build_site(data, ROOT, self.output)
        self.assertEqual((self.output / "index.html").read_bytes(), before)

    def test_combined_feed_breaks_equal_date_ties_alphabetically(self) -> None:
        first = replace(self.data.news[0], slug="zeta", title="Alpha")
        second = replace(first, slug="beta", title="Beta")
        third = replace(first, slug="alpha", title="Alpha")
        data = replace(self.data, news=[second], consortium=[first, third])
        self.assertEqual([item.slug for item in combined_news(data)], ["alpha", "zeta", "beta"])


if __name__ == "__main__":
    unittest.main()
