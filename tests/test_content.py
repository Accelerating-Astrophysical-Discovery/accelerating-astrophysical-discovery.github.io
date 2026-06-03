from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from sitegen.content import ContentError, collect_writings, parse_iso_date, summarize
from sitegen.markdown import codecogs_to_latex, render_markdown


class ContentTests(unittest.TestCase):
    def test_parse_iso_date_rejects_non_iso(self) -> None:
        with TemporaryDirectory() as temp:
            with self.assertRaises(ContentError):
                parse_iso_date("2020/01/01", "date_published", Path(temp) / "entry.toml")

    def test_summarize_uses_42_characters(self) -> None:
        self.assertEqual(summarize("a" * 45, 42), ("a" * 42) + "...")

    def test_codecogs_inline_conversion(self) -> None:
        source = "Value ![eqn](https://latex.codecogs.com/svg.latex?x&space;=&space;y&plus;1) here."
        self.assertEqual(codecogs_to_latex(source), r"Value \(x = y+1\) here.")

    def test_codecogs_block_conversion(self) -> None:
        source = "![eqn](https://latex.codecogs.com/svg.latex?x&space;=&space;y)\n"
        self.assertEqual(codecogs_to_latex(source), "\\[\nx = y\n\\]")

    def test_collect_writings_sorts_newest_then_alpha(self) -> None:
        with TemporaryDirectory() as temp:
            root = Path(temp)
            section = root / "news"
            for slug, title, day in [
                ("beta", "Beta", "2024-01-01"),
                ("alpha", "Alpha", "2024-01-01"),
                ("gamma", "Gamma", "2025-01-01"),
            ]:
                item = section / slug
                item.mkdir(parents=True)
                (item / f"{slug}.toml").write_text(
                    f'title = "{title}"\ndate_published = "{day}"\n',
                    encoding="utf-8",
                )
                (item / f"{slug}.md").write_text(f"# {title}\n\nBody", encoding="utf-8")

            items = collect_writings(root, "news", render_markdown)
            self.assertEqual([item.slug for item in items], ["gamma", "alpha", "beta"])


if __name__ == "__main__":
    unittest.main()
