from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path

from sitegen.content import Writing
from sitegen.render import copy_writing_assets


class RenderAssetTests(unittest.TestCase):
    def test_writing_assets_are_copied_recursively(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            output = root / "dist"
            entry = root / "consortium" / "paper"
            (entry / "images").mkdir(parents=True)
            source = entry / "paper.md"
            metadata = entry / "paper.toml"
            asset = entry / "images" / "figure.png"
            source.write_text("source", encoding="utf-8")
            metadata.write_text("metadata", encoding="utf-8")
            asset.write_bytes(b"image")
            writing = Writing(
                section="consortium",
                slug="paper",
                title="Paper",
                date_published=date(2026, 1, 1),
                markdown_path=source,
                metadata_path=metadata,
                html="<p>Paper</p>",
                excerpt="Paper",
                comment_id="research/paper",
            )

            copy_writing_assets(root, output, [writing])

            for section in ("consortium", "research"):
                with self.subTest(section=section):
                    target = output / "assets" / "content" / section / "paper"
                    self.assertEqual((target / "images" / "figure.png").read_bytes(), b"image")
                    self.assertFalse((target / "paper.md").exists())
                    self.assertFalse((target / "paper.toml").exists())


if __name__ == "__main__":
    unittest.main()
