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
            entry = root / "research" / "paper"
            (entry / "images").mkdir(parents=True)
            source = entry / "paper.md"
            metadata = entry / "paper.toml"
            asset = entry / "images" / "figure.png"
            source.write_text("source", encoding="utf-8")
            metadata.write_text("metadata", encoding="utf-8")
            asset.write_bytes(b"image")
            writing = Writing(
                section="research",
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

            self.assertTrue((output / "assets" / "content" / "research" / "paper" / "images" / "figure.png").exists())
            self.assertFalse((output / "assets" / "content" / "research" / "paper" / "paper.md").exists())
            self.assertFalse((output / "assets" / "content" / "research" / "paper" / "paper.toml").exists())


if __name__ == "__main__":
    unittest.main()
