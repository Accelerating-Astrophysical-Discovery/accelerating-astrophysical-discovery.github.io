"""Export browser/social icons from the editable SVG; not needed for site builds.

Requires rsvg-convert (librsvg) and Pillow. All exports are checked in, so CI and
social crawlers never need an SVG renderer or client-side JavaScript.
"""
from pathlib import Path
import shutil
import subprocess

from PIL import Image


def main() -> None:
    renderer = shutil.which("rsvg-convert")
    if renderer is None:
        raise SystemExit("Install librsvg's rsvg-convert to regenerate icons.")
    assets = Path(__file__).resolve().parents[1] / "site" / "assets" / "branding"
    for filename, size in (
        ("icon-512.png", 512),
        ("favicon-48.png", 48),
        ("apple-touch-icon.png", 180),
    ):
        subprocess.run(
            [renderer, "--width", str(size), "--height", str(size),
             "--output", str(assets / filename), str(assets / "icon.svg")],
            check=True,
        )
    with Image.open(assets / "icon-512.png") as icon:
        icon.save(assets / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])


if __name__ == "__main__":
    main()
