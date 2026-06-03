#!/usr/bin/env python3
"""Prepare legacy Jekyll posts for the redesigned research section.

The command is read-only by default. Pass --write to create
research/<slug>/<slug>.md and research/<slug>/<slug>.toml files.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import html
import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import unquote


DATE_SLUG_RE = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.+)\.md$")
FRONT_MATTER_RE = re.compile(
    r"\A---[ \t]*\n(?P<front_matter>.*?)\n---[ \t]*(?:\n|$)(?P<body>.*)\Z",
    re.DOTALL,
)
CODECOGS_PREFIX = "https://latex.codecogs.com/"
ASSET_LINK_RE = re.compile(
    r"(?P<prefix>!?\[[^\]]*\]\()(?P<path>/assets/[^)\s]+)(?P<suffix>\))"
)


class MigrationError(RuntimeError):
    """Raised when a source post cannot be migrated deterministically."""


@dataclass(frozen=True)
class CodecogsToken:
    start: int
    end: int
    alt: str
    url: str


@dataclass
class MigratedPost:
    source: Path
    slug: str
    title: str
    date_published: str
    markdown: str
    toml: str
    codecogs_conversions: int
    asset_copies: list[tuple[Path, str]] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def split_front_matter(text: str) -> tuple[dict[str, str], str]:
    """Return a shallow mapping of front matter keys and body Markdown."""

    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text
    return parse_simple_front_matter(match.group("front_matter")), match.group("body")


def parse_simple_front_matter(raw: str) -> dict[str, str]:
    """Parse the scalar front matter fields this migration needs.

    This is intentionally small and dependency-free; it captures top-level
    "key: value" scalars and ignores arrays or nested blocks.
    """

    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.startswith((" ", "\t", "-")):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key:
            data[key] = clean_scalar(value.strip())
    return data


def clean_scalar(value: str) -> str:
    if not value:
        return ""
    if value[0:1] in {"'", '"'} and value[-1:] == value[0]:
        return value[1:-1]
    return value


def source_date_and_slug(path: Path) -> tuple[str, str]:
    match = DATE_SLUG_RE.match(path.name)
    if not match:
        raise MigrationError(
            f"{path} does not match the expected YYYY-MM-DD-title.md pattern"
        )
    return match.group("date"), normalize_slug(match.group("slug"))


def normalize_slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise MigrationError(f"Could not derive a slug from {value!r}")
    return slug


def title_from_slug(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-"))


def toml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def build_toml(title: str, date_published: str) -> str:
    return (
        f"title = {toml_quote(title)}\n"
        f"date_published = {toml_quote(date_published)}\n"
    )


def find_codecogs_tokens(line: str) -> list[CodecogsToken]:
    tokens: list[CodecogsToken] = []
    pos = 0
    while True:
        start = line.find("![", pos)
        if start == -1:
            return tokens
        alt_end = line.find("](", start + 2)
        if alt_end == -1:
            pos = start + 2
            continue
        url_start = alt_end + 2
        if not line.startswith(CODECOGS_PREFIX, url_start):
            pos = url_start
            continue

        depth = 1
        cursor = url_start
        while cursor < len(line):
            char = line[cursor]
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    tokens.append(
                        CodecogsToken(
                            start=start,
                            end=cursor + 1,
                            alt=line[start + 2 : alt_end],
                            url=line[url_start:cursor],
                        )
                    )
                    pos = cursor + 1
                    break
            cursor += 1
        else:
            raise MigrationError(f"Unclosed Codecogs Markdown image in line: {line}")


def decode_codecogs_latex(url: str) -> str:
    match = re.match(r"https://latex\.codecogs\.com/(?:svg|png|gif)\.latex\??(.*)", url)
    if not match:
        raise MigrationError(f"Unsupported Codecogs URL: {url}")
    latex = unquote(match.group(1))
    latex = html.unescape(latex)
    latex = latex.replace("&space;", " ").replace("&plus;", "+")
    latex = latex.replace("\xa0", " ")
    latex = re.sub(r"[ \t]+", " ", latex).strip()
    if not latex:
        raise MigrationError(f"Codecogs URL had no LaTeX payload: {url}")
    return latex


def split_line_ending(line: str) -> tuple[str, str]:
    if line.endswith("\r\n"):
        return line[:-2], "\r\n"
    if line.endswith("\n"):
        return line[:-1], "\n"
    return line, ""


def convert_codecogs_images(markdown: str) -> tuple[str, int]:
    converted_lines: list[str] = []
    conversion_count = 0

    for original_line in markdown.splitlines(keepends=True):
        line, ending = split_line_ending(original_line)
        tokens = find_codecogs_tokens(line)
        if not tokens:
            converted_lines.append(original_line)
            continue

        conversion_count += len(tokens)
        trailing_text = line[tokens[0].end :].strip() if len(tokens) == 1 else ""
        only_token = (
            len(tokens) == 1
            and not line[: tokens[0].start].strip()
            and trailing_text in {"", ".", ","}
        )

        if only_token:
            latex = decode_codecogs_latex(tokens[0].url)
            converted_lines.append(f"\\[\n{latex}\n\\]{trailing_text}{ending}")
            continue

        rebuilt: list[str] = []
        cursor = 0
        for token in tokens:
            rebuilt.append(line[cursor : token.start])
            rebuilt.append(f"\\({decode_codecogs_latex(token.url)}\\)")
            cursor = token.end
        rebuilt.append(line[cursor:])
        converted_lines.append("".join(rebuilt) + ending)

    return "".join(converted_lines), conversion_count


def rewrite_and_plan_asset_links(
    markdown: str,
    repo_root: Path,
    output_dir: Path,
    copy_assets: bool,
    write: bool,
) -> tuple[str, list[tuple[Path, str]], list[str]]:
    copies: list[tuple[Path, str]] = []
    warnings: list[str] = []
    used_names: dict[str, Path] = {}

    def replacement(match: re.Match[str]) -> str:
        source_rel = Path(match.group("path").lstrip("/"))
        source = repo_root / source_rel
        if not source.exists():
            warnings.append(f"Missing local asset: {source_rel.as_posix()}")
            return match.group(0)

        dest_name = unique_asset_name(source_rel, used_names)
        copies.append((source_rel, dest_name))

        if copy_assets and write:
            output_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, output_dir / dest_name)

        if copy_assets:
            return f"{match.group('prefix')}{dest_name}{match.group('suffix')}"
        return match.group(0)

    rewritten = ASSET_LINK_RE.sub(replacement, markdown)
    return rewritten, copies, warnings


def unique_asset_name(source_rel: Path, used_names: dict[str, Path]) -> str:
    candidate = source_rel.name
    if candidate not in used_names or used_names[candidate] == source_rel:
        used_names[candidate] = source_rel
        return candidate

    prefix = normalize_slug("-".join(source_rel.parts[:-1]))
    candidate = f"{prefix}-{source_rel.name}"
    used_names[candidate] = source_rel
    return candidate


def migrate_post(
    source: Path,
    repo_root: Path,
    target_root: Path,
    copy_assets: bool,
    write: bool,
    force: bool,
) -> MigratedPost:
    date_published, slug = source_date_and_slug(source)
    front_matter, body = split_front_matter(source.read_text(encoding="utf-8"))
    title = front_matter.get("title") or title_from_slug(slug)

    body, codecogs_count = convert_codecogs_images(body)
    output_dir = target_root / slug
    body, asset_copies, warnings = rewrite_and_plan_asset_links(
        body,
        repo_root=repo_root,
        output_dir=output_dir,
        copy_assets=copy_assets,
        write=write,
    )

    toml = build_toml(title=title, date_published=date_published)
    migrated = MigratedPost(
        source=source,
        slug=slug,
        title=title,
        date_published=date_published,
        markdown=body,
        toml=toml,
        codecogs_conversions=codecogs_count,
        asset_copies=asset_copies,
        warnings=warnings,
    )

    if write:
        output_dir.mkdir(parents=True, exist_ok=True)
        md_path = output_dir / f"{slug}.md"
        toml_path = output_dir / f"{slug}.toml"
        existing = [path for path in (md_path, toml_path) if path.exists()]
        if existing and not force:
            existing_text = ", ".join(str(path) for path in existing)
            raise MigrationError(
                f"Refusing to overwrite existing files without --force: {existing_text}"
            )
        md_path.write_text(migrated.markdown, encoding="utf-8")
        toml_path.write_text(migrated.toml, encoding="utf-8")

    return migrated


def collect_sources(repo_root: Path, source_dirs: list[Path]) -> list[Path]:
    sources: list[Path] = []
    for source_dir in source_dirs:
        absolute = source_dir if source_dir.is_absolute() else repo_root / source_dir
        if not absolute.exists():
            raise MigrationError(f"Source directory does not exist: {absolute}")
        sources.extend(sorted(absolute.glob("*.md")))
    return sources


def display_path(path: Path, repo_root: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except ValueError:
        return path.as_posix()


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert legacy Jekyll posts into research content files."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root. Defaults to the parent of tools/.",
    )
    parser.add_argument(
        "--source",
        action="append",
        type=Path,
        dest="sources",
        help="Source directory to scan. Defaults to _posts and inprep_posts.",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=Path("research"),
        help="Target research directory, relative to repo root unless absolute.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write migrated files. Without this flag the command is a dry run.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow overwriting generated Markdown/TOML files when --write is used.",
    )
    parser.add_argument(
        "--no-copy-assets",
        action="store_false",
        dest="copy_assets",
        help="Leave /assets/... Markdown links unchanged instead of localizing them.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    repo_root = args.repo_root.resolve()
    source_dirs = args.sources or [Path("_posts"), Path("inprep_posts")]
    target_root = args.target if args.target.is_absolute() else repo_root / args.target

    try:
        sources = collect_sources(repo_root, source_dirs)
        seen_slugs: set[str] = set()
        migrated_posts: list[MigratedPost] = []
        for source in sources:
            _, slug = source_date_and_slug(source)
            if slug in seen_slugs:
                raise MigrationError(f"Duplicate migrated slug: {slug}")
            seen_slugs.add(slug)
            migrated_posts.append(
                migrate_post(
                    source=source,
                    repo_root=repo_root,
                    target_root=target_root,
                    copy_assets=args.copy_assets,
                    write=args.write,
                    force=args.force,
                )
            )
    except MigrationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    mode = "write" if args.write else "dry-run"
    print(f"{mode}: prepared {len(migrated_posts)} research entries")
    for post in migrated_posts:
        target = target_root / post.slug
        print(
            f"- {display_path(post.source, repo_root)} -> "
            f"{display_path(target, repo_root)}/{post.slug}.md, "
            f"{post.slug}.toml"
        )
        if post.codecogs_conversions:
            print(f"  codecogs: converted {post.codecogs_conversions} equation image(s)")
        if post.asset_copies:
            action = "copied" if args.write and args.copy_assets else "would copy"
            for source_rel, dest_name in post.asset_copies:
                print(f"  asset: {action} {source_rel.as_posix()} -> {dest_name}")
        for warning in post.warnings:
            print(f"  warning: {warning}")

    if not args.write:
        print("No files were written. Re-run with --write to create research entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
