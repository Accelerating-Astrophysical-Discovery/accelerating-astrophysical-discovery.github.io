#!/usr/bin/env python3
"""Build the site manifest from structured source content."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from sitegen.loader import SiteValidationError, load_site, write_manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="repository root to scan")
    parser.add_argument("--output", type=Path, default=Path("dist"), help="output directory")
    parser.add_argument("--manifest-name", default="build-manifest.json", help="manifest JSON filename")
    parser.add_argument("--production", action="store_true", help="require production-only configuration")
    parser.add_argument("--validate-only", action="store_true", help="validate and print a summary without writing")
    parser.add_argument("--manifest-only", action="store_true", help="write only the JSON build manifest")
    parser.add_argument("--compact", action="store_true", help="write compact JSON instead of pretty JSON")
    args = parser.parse_args()

    try:
        manifest = load_site(args.root)
    except SiteValidationError as exc:
        for error in exc.errors:
            print(f"error: {error}")
        return 1

    if args.production:
        from sitegen.content import ContentError, load_config

        try:
            load_config(args.root, production=True)
        except ContentError as exc:
            print(f"error: {exc}")
            return 1

    summary = (
        f"loaded {len(manifest.members)} members, "
        f"{len(manifest.news)} news entries, {len(manifest.research)} research entries"
    )
    if args.validate_only:
        print(summary)
        return 0

    if not args.manifest_only:
        from sitegen.build import build
        from sitegen.content import ContentError

        try:
            build(args.root, args.output, production=args.production)
        except (ContentError, SiteValidationError) as exc:
            errors = getattr(exc, "errors", (str(exc),))
            for error in errors:
                print(f"error: {error}")
            return 1
        print(f"{summary}; wrote {args.output}")
        return 0

    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / ".nojekyll").write_text("", encoding="utf-8")
    manifest_path = args.output / args.manifest_name
    write_manifest(manifest, manifest_path, pretty=not args.compact)
    print(f"{summary}; wrote {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
