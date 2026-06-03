from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from sitegen.loader import SiteValidationError, load_site


class LoaderTests(unittest.TestCase):
    def test_loads_and_sorts_content_newest_first_with_alpha_ties(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self._write_member(root, "late", "Late Person", "2024-01-01", last_name="Person")
            self._write_member(root, "zara-alpha", "Zara Alpha", "2023-01-01", last_name="Alpha")
            self._write_member(root, "aaron-zulu", "Aaron Zulu", "2023-01-01", last_name="Zulu")
            self._write_text_entry(root, "news", "older", "Older", "2021-01-01")
            self._write_text_entry(root, "news", "alpha", "Alpha", "2023-02-01")
            self._write_text_entry(root, "news", "beta", "Beta", "2023-02-01")
            self._write_text_entry(root, "research", "paper", "Paper", "2024-01-05")

            manifest = load_site(root)

            self.assertEqual([member.slug for member in manifest.members], ["zara-alpha", "aaron-zulu", "late"])
            self.assertEqual([entry.slug for entry in manifest.news], ["alpha", "beta", "older"])
            self.assertIn(r"\(x=1\)", manifest.research[0].html)
            self.assertEqual(
                manifest.research[0].comment_term,
                "[research/comments] research/paper",
            )

    def test_strict_validation_reports_missing_pairs_invalid_dates_and_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self._write_member(root, "missing-list", "Missing", "2020-01-01", omit_lists=True)
            self._write_text_entry(root, "news", "invalid-date", "Invalid", "2020-13-40")
            self._write_text_entry(
                root,
                "news",
                "same-comment",
                "Same",
                "2020-01-01",
                comment_id="same",
            )
            self._write_text_entry(
                root,
                "research",
                "same-comment",
                "Same",
                "2020-01-02",
                comment_id="same",
            )

            with self.assertRaises(SiteValidationError) as caught:
                load_site(root)

            message = "\n".join(caught.exception.errors)
            self.assertIn("missing required list field 'affiliations'", message)
            self.assertIn("valid YYYY-MM-DD date", message)
            self.assertIn("duplicate comment_id 'same'", message)

    def test_rejects_non_url_safe_slugs(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self._write_text_entry(root, "news", "Bad Slug", "Bad", "2020-01-01")

            with self.assertRaises(SiteValidationError) as caught:
                load_site(root)

            self.assertIn("invalid news slug", "\n".join(caught.exception.errors))

    def _write_text_entry(
        self,
        root: Path,
        collection: str,
        slug: str,
        title: str,
        date_published: str,
        comment_id: str | None = None,
    ) -> None:
        entry = root / collection / slug
        entry.mkdir(parents=True)
        comment_line = f'comment_id = "{comment_id}"\n' if comment_id else ""
        (entry / f"{slug}.toml").write_text(
            f'title = "{title}"\n'
            f'date_published = "{date_published}"\n'
            f"{comment_line}",
            encoding="utf-8",
        )
        (entry / f"{slug}.md").write_text(
            "# Heading\n\nFirst paragraph with \\(x=1\\) and enough text for an excerpt.",
            encoding="utf-8",
        )

    def _write_member(
        self,
        root: Path,
        slug: str,
        name: str,
        join_date: str,
        omit_lists: bool = False,
        last_name: str | None = None,
    ) -> None:
        members = root / "members"
        members.mkdir(parents=True, exist_ok=True)
        (members / f"{slug}.jpg").write_bytes(b"not really an image")
        lists = "" if omit_lists else 'affiliations = ["Institute"]\nresearch_areas = ["Area"]\n'
        last_name_line = f'last_name = "{last_name}"\n' if last_name else ""
        (members / f"{slug}.toml").write_text(
            f'name = "{name}"\n'
            f"{last_name_line}"
            f'join_date = "{join_date}"\n'
            f"{lists}"
            'bio = "Short bio."\n',
            encoding="utf-8",
        )


if __name__ == "__main__":
    unittest.main()
