"""Content discovery, TOML validation, and manifest construction."""

from __future__ import annotations

import json
import re
import tomllib
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable, Literal

from .markdown import markdown_excerpt, render_markdown
from .models import BuildManifest, MemberEntry, TextEntry

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MEMBER_IMAGE_EXTENSIONS = {".gif", ".jpeg", ".jpg", ".png", ".webp"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class SiteValidationError(Exception):
    """Raised when source content cannot be converted into a valid manifest."""

    def __init__(self, errors: Iterable[str]):
        self.errors = tuple(errors)
        super().__init__("\n".join(self.errors))


def load_site(root: str | Path) -> BuildManifest:
    """Load all supported content under ``root`` into a manifest model."""
    root_path = Path(root).resolve()
    errors: list[str] = []
    comment_ids: dict[str, str] = {}
    members = _load_members(root_path, errors)
    news = _load_text_collection(root_path, "news", "news", errors, comment_ids)
    research = _load_text_collection(root_path, "research", "research", errors, comment_ids)
    if errors:
        raise SiteValidationError(errors)
    return BuildManifest(
        members=tuple(members),
        news=tuple(news),
        research=tuple(research),
    )


def write_manifest(manifest: BuildManifest, path: str | Path, pretty: bool = True) -> None:
    """Write a manifest as JSON for downstream template/rendering code."""
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    kwargs = {"indent": 2, "sort_keys": True} if pretty else {}
    output.write_text(json.dumps(manifest.to_dict(), **kwargs) + "\n", encoding="utf-8")


def _load_members(root: Path, errors: list[str]) -> list[MemberEntry]:
    members_root = root / "members"
    if not members_root.exists():
        return []
    if not members_root.is_dir():
        errors.append(f"{_rel(root, members_root)} must be a directory")
        return []

    image_files = [
        path
        for path in members_root.iterdir()
        if path.is_file() and path.suffix.casefold() in MEMBER_IMAGE_EXTENSIONS
    ]
    metadata_files = [path for path in members_root.glob("*.toml") if path.is_file()]
    _check_duplicate_names(image_files, "member image slug", errors, root, use_stem=True)
    _check_duplicate_names(metadata_files, "member metadata slug", errors, root, use_stem=True)
    _check_slugs(image_files, "member image slug", errors, root, use_stem=True)
    _check_slugs(metadata_files, "member metadata slug", errors, root, use_stem=True)

    images_by_stem: dict[str, Path] = {}
    for path in image_files:
        images_by_stem.setdefault(path.stem, path)
    metadata_by_stem = {path.stem: path for path in metadata_files}

    for slug in sorted(set(images_by_stem) - set(metadata_by_stem)):
        errors.append(f"missing member metadata for {_rel(root, images_by_stem[slug])}: expected {slug}.toml")
    for slug in sorted(set(metadata_by_stem) - set(images_by_stem)):
        errors.append(f"missing member image for {_rel(root, metadata_by_stem[slug])}")

    members: list[MemberEntry] = []
    for slug in sorted(set(images_by_stem) & set(metadata_by_stem)):
        image_path = images_by_stem[slug]
        metadata_path = metadata_by_stem[slug]
        data = _read_toml(metadata_path, errors, root)
        if data is None:
            continue
        _reject_unknown_keys(
            data,
            {"affiliations", "bio", "join_date", "last_name", "name", "research_areas"},
            metadata_path,
            errors,
            root,
        )
        name = _required_str(data, "name", metadata_path, errors, root)
        last_name = _optional_str(data, "last_name", metadata_path, errors, root)
        join_date = _required_date(data, "join_date", metadata_path, errors, root)
        affiliations = _required_str_list(data, "affiliations", metadata_path, errors, root)
        research_areas = _required_str_list(data, "research_areas", metadata_path, errors, root)
        bio = _required_str(data, "bio", metadata_path, errors, root)
        if None in (name, join_date, affiliations, research_areas, bio):
            continue
        members.append(
            MemberEntry(
                slug=slug,
                name=name or "",
                last_name=last_name or _infer_last_name(name or ""),
                join_date=join_date or date.min,
                image_path=_rel(root, image_path),
                metadata_path=_rel(root, metadata_path),
                affiliations=tuple(affiliations or ()),
                research_areas=tuple(research_areas or ()),
                bio=bio or "",
            )
        )

    return sorted(
        members,
        key=lambda member: (
            member.join_date.toordinal(),
            member.last_name.casefold(),
            member.name.casefold(),
            member.slug.casefold(),
        ),
    )


def _infer_last_name(name: str) -> str:
    parts = name.split()
    return parts[-1] if parts else name


def _load_text_collection(
    root: Path,
    directory: Literal["essays", "news", "research"],
    kind: Literal["essay", "news", "research"],
    errors: list[str],
    comment_ids: dict[str, str],
) -> list[TextEntry]:
    collection_root = root / directory
    if not collection_root.exists():
        return []
    if not collection_root.is_dir():
        errors.append(f"{_rel(root, collection_root)} must be a directory")
        return []

    entry_dirs = [
        path
        for path in collection_root.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    ]
    _check_duplicate_names(entry_dirs, f"{kind} slug", errors, root)
    _check_slugs(entry_dirs, f"{kind} slug", errors, root)

    entries: list[TextEntry] = []
    for entry_dir in sorted(entry_dirs, key=lambda path: path.name.casefold()):
        slug = entry_dir.name
        metadata_path = entry_dir / f"{slug}.toml"
        markdown_path = entry_dir / f"{slug}.md"
        if not metadata_path.exists():
            errors.append(f"missing {kind} metadata for {_rel(root, entry_dir)}: expected {slug}.toml")
            continue
        if not markdown_path.exists():
            errors.append(f"missing {kind} markdown for {_rel(root, entry_dir)}: expected {slug}.md")
            continue
        data = _read_toml(metadata_path, errors, root)
        if data is None:
            continue
        _reject_unknown_keys(data, {"comment_id", "date_published", "title"}, metadata_path, errors, root)
        title = _required_str(data, "title", metadata_path, errors, root)
        date_published = _required_date(data, "date_published", metadata_path, errors, root)
        default_comment_id = f"{directory}/{slug}"
        comment_id = _optional_str(data, "comment_id", metadata_path, errors, root) or default_comment_id
        _register_comment_id(comment_ids, comment_id, metadata_path, errors, root)
        if title is None or date_published is None:
            continue
        markdown = markdown_path.read_text(encoding="utf-8")
        entries.append(
            TextEntry(
                kind=kind,
                slug=slug,
                title=title,
                date_published=date_published,
                markdown_path=_rel(root, markdown_path),
                metadata_path=_rel(root, metadata_path),
                html=render_markdown(markdown),
                excerpt=markdown_excerpt(markdown),
                comment_id=comment_id,
            )
        )

    return sorted(entries, key=lambda entry: (-entry.date_published.toordinal(), entry.title.casefold(), entry.slug.casefold()))


def _read_toml(path: Path, errors: list[str], root: Path) -> dict[str, Any] | None:
    try:
        with path.open("rb") as handle:
            data = tomllib.load(handle)
    except tomllib.TOMLDecodeError as exc:
        errors.append(f"{_rel(root, path)} has invalid TOML: {exc}")
        return None
    if not isinstance(data, dict):
        errors.append(f"{_rel(root, path)} must contain a TOML table")
        return None
    return data


def _reject_unknown_keys(
    data: dict[str, Any],
    allowed: set[str],
    path: Path,
    errors: list[str],
    root: Path,
) -> None:
    unknown = sorted(set(data) - allowed)
    if unknown:
        errors.append(f"{_rel(root, path)} has unsupported keys: {', '.join(unknown)}")


def _required_str(
    data: dict[str, Any],
    key: str,
    path: Path,
    errors: list[str],
    root: Path,
) -> str | None:
    if key not in data:
        errors.append(f"{_rel(root, path)} missing required string field {key!r}")
        return None
    return _string_value(data[key], key, path, errors, root)


def _optional_str(
    data: dict[str, Any],
    key: str,
    path: Path,
    errors: list[str],
    root: Path,
) -> str | None:
    if key not in data:
        return None
    return _string_value(data[key], key, path, errors, root)


def _optional_blank_str(
    data: dict[str, Any],
    key: str,
    path: Path,
    errors: list[str],
    root: Path,
) -> str | None:
    if key not in data:
        return None
    value = data[key]
    if not isinstance(value, str):
        errors.append(f"{_rel(root, path)} field {key!r} must be a string")
        return None
    return value.strip()


def _required_str_list(
    data: dict[str, Any],
    key: str,
    path: Path,
    errors: list[str],
    root: Path,
) -> list[str] | None:
    if key not in data:
        errors.append(f"{_rel(root, path)} missing required list field {key!r}")
        return None
    value = data[key]
    if not isinstance(value, list) or not value:
        errors.append(f"{_rel(root, path)} field {key!r} must be a non-empty list of strings")
        return None
    items: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            errors.append(f"{_rel(root, path)} field {key!r} must be a non-empty list of strings")
            return None
        items.append(item.strip())
    return items


def _string_value(
    value: Any,
    key: str,
    path: Path,
    errors: list[str],
    root: Path,
) -> str | None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{_rel(root, path)} field {key!r} must be a non-empty string")
        return None
    return value.strip()


def _required_date(
    data: dict[str, Any],
    key: str,
    path: Path,
    errors: list[str],
    root: Path,
) -> date | None:
    if key not in data:
        errors.append(f"{_rel(root, path)} missing required date field {key!r}")
        return None
    value = data[key]
    if isinstance(value, datetime):
        errors.append(f"{_rel(root, path)} field {key!r} must be a YYYY-MM-DD date, not a datetime")
        return None
    if isinstance(value, date):
        return value
    if isinstance(value, str) and DATE_RE.fullmatch(value):
        try:
            return date.fromisoformat(value)
        except ValueError:
            pass
    errors.append(f"{_rel(root, path)} field {key!r} must be a valid YYYY-MM-DD date")
    return None


def _register_comment_id(
    comment_ids: dict[str, str],
    comment_id: str,
    path: Path,
    errors: list[str],
    root: Path,
) -> None:
    existing = comment_ids.get(comment_id)
    rel_path = _rel(root, path)
    if existing is not None:
        errors.append(f"duplicate comment_id {comment_id!r}: {existing} and {rel_path}")
        return
    comment_ids[comment_id] = rel_path


def _check_duplicate_names(
    paths: Iterable[Path],
    label: str,
    errors: list[str],
    root: Path,
    use_stem: bool = False,
) -> None:
    seen: dict[str, Path] = {}
    for path in paths:
        value = path.stem if use_stem else path.name
        key = value.casefold()
        if key in seen:
            errors.append(f"duplicate {label} {value!r}: {_rel(root, seen[key])} and {_rel(root, path)}")
        else:
            seen[key] = path


def _check_slugs(
    paths: Iterable[Path],
    label: str,
    errors: list[str],
    root: Path,
    use_stem: bool = False,
) -> None:
    for path in paths:
        value = path.stem if use_stem else path.name
        if not SLUG_RE.fullmatch(value):
            errors.append(
                f"{_rel(root, path)} has invalid {label} {value!r}; "
                "use lowercase letters, numbers, and hyphens"
            )


def _rel(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root).as_posix()
