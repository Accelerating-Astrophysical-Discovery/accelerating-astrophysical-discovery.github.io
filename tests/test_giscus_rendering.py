from __future__ import annotations

import unittest
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from sitegen.content import GiscusConfig, SiteConfig, Writing


ROOT = Path(__file__).resolve().parents[1]


class GiscusRenderingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.env = Environment(
            loader=FileSystemLoader(ROOT / "site" / "templates"),
            autoescape=select_autoescape(["html", "xml"]),
        )
        self.site = SiteConfig(
            giscus=GiscusConfig(
                repo="owner/repo",
                repo_id="repo-id",
                category="Comments",
                category_id="category-id",
            )
        )

    def test_news_comments_match_stable_html_title(self) -> None:
        item = Writing(
            section="news",
            slug="hello",
            title="Hello",
            date_published=date(2026, 1, 1),
            markdown_path=ROOT / "hello.md",
            metadata_path=ROOT / "hello.toml",
            html="<p>Hello.</p>",
            excerpt="Hello.",
            comment_id="news/hello",
        )

        html = self.env.get_template("writing_detail.html").render(
            site=self.site,
            active="news",
            section="news",
            title="News",
            item=item,
        )

        self.assertIn("<title>[news/comments] news/hello</title>", html)
        self.assertIn('data-mapping="title"', html)
        self.assertIn('data-strict="0"', html)
        self.assertIn('data-input-position="top"', html)
        self.assertIn('data-theme="light"', html)
        self.assertIn('data-loading="lazy"', html)
        self.assertNotIn("data-term=", html)

    def test_consortium_comments_use_repo_section_name(self) -> None:
        item = Writing(
            section="research",
            slug="hello",
            title="Hello",
            date_published=date(2026, 1, 1),
            markdown_path=ROOT / "hello.md",
            metadata_path=ROOT / "hello.toml",
            html="<p>Hello.</p>",
            excerpt="Hello.",
            comment_id="research/hello",
        )

        html = self.env.get_template("writing_detail.html").render(
            site=self.site,
            active="consortium",
            section="consortium",
            title="Consortium",
            item=item,
        )

        self.assertIn("<title>[consortium/comments] research/hello</title>", html)
        self.assertIn('data-mapping="title"', html)
        self.assertNotIn("data-term=", html)


if __name__ == "__main__":
    unittest.main()
