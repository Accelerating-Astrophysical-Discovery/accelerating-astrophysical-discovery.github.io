"""Compatibility helpers around the stricter manifest loader."""

from __future__ import annotations

import re
import tomllib
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Callable

from .loader import _load_members, _load_text_collection
from .markdown import render_markdown
from .models import MemberEntry, TextEntry

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class ContentError(ValueError):
    """Raised by compatibility content helpers."""


@dataclass
class GiscusConfig:
    repo: str = ""
    repo_id: str = ""
    category: str = "Comments"
    category_id: str = ""
    theme: str = "light"

    @property
    def configured(self) -> bool:
        return all([self.repo, self.repo_id, self.category, self.category_id])


@dataclass
class SiteConfig:
    title: str = "Accelerating Astrophysical Discovery with Foundation Models"
    base_url: str = ""
    membership_form_url: str = ""
    giscus: GiscusConfig = field(default_factory=GiscusConfig)


@dataclass
class Writing:
    section: str
    slug: str
    title: str
    date_published: date
    markdown_path: Path
    metadata_path: Path
    html: str
    excerpt: str
    comment_id: str

    @property
    def giscus_term(self) -> str:
        if self.section == "news":
            kind = "news"
        elif self.section == "essays":
            kind = "essay"
        elif self.section == "research":
            kind = "consortium"
        else:
            kind = self.section
        return f"[{kind}/comments] {self.comment_id}"

    @property
    def body_html(self) -> str:
        return self.html

    @property
    def summary(self) -> str:
        return self.excerpt


@dataclass
class Member:
    slug: str
    name: str
    last_name: str
    join_date: date
    image_path: Path
    metadata_path: Path
    affiliations: list[str]
    research_areas: list[str]
    bio: str

    @property
    def image_url(self) -> str:
        return f"/assets/members/{self.image_path.name}"


@dataclass
class SiteData:
    config: SiteConfig
    members: list[Member]
    news: list[Writing]
    research: list[Writing]


def parse_iso_date(value: str, field_name: str, path: Path) -> date:
    if not DATE_RE.fullmatch(value):
        raise ContentError(f"{path} field {field_name!r} must use YYYY-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ContentError(f"{path} field {field_name!r} must be a valid date") from exc


def summarize(text: str, limit: int = 42) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "..."


def collect_writings(
    root: Path,
    section: str,
    renderer: Callable[[str], str] = render_markdown,
    seen_comment_ids: set[str] | None = None,
) -> list[Writing]:
    if section == "news":
        kind = "news"
    elif section == "essays":
        kind = "essay"
    else:
        kind = "research"
    errors: list[str] = []
    comment_ids: dict[str, str] = {}
    root = Path(root).resolve()
    items = _load_text_collection(root, section, kind, errors, comment_ids)
    if errors:
        raise ContentError("\n".join(errors))
    writings: list[Writing] = []
    seen_comment_ids = seen_comment_ids if seen_comment_ids is not None else set()
    for item in items:
        if item.comment_id in seen_comment_ids:
            raise ContentError(f"duplicate comment_id `{item.comment_id}`")
        seen_comment_ids.add(item.comment_id)
        markdown_path = root / item.markdown_path
        rendered = renderer(
            markdown_path.read_text(encoding="utf-8"),
            markdown_path,
            section,
            item.slug,
        )
        if isinstance(rendered, tuple):
            html, excerpt = rendered
        else:
            html, excerpt = rendered, item.excerpt
        writings.append(
            Writing(
                section=section,
                slug=item.slug,
                title=item.title,
                date_published=item.date_published,
                markdown_path=markdown_path,
                metadata_path=root / item.metadata_path,
                html=html,
                excerpt=excerpt,
                comment_id=item.comment_id,
            )
        )
    return writings


def collect_members(root: Path) -> list[Member]:
    root = Path(root).resolve()
    errors: list[str] = []
    members = _load_members(root, errors)
    if errors:
        raise ContentError("\n".join(errors))
    return [_member_from_entry(root, member) for member in members]


def _member_from_entry(root: Path, member: MemberEntry) -> Member:
    return Member(
        slug=member.slug,
        name=member.name,
        last_name=member.last_name,
        join_date=member.join_date,
        image_path=root / member.image_path,
        metadata_path=root / member.metadata_path,
        affiliations=list(member.affiliations),
        research_areas=list(member.research_areas),
        bio=member.bio,
    )


def load_config(root: Path, production: bool = False) -> SiteConfig:
    config_path = Path(root) / "site_config.toml"
    if not config_path.exists():
        return SiteConfig()
    with config_path.open("rb") as handle:
        data = tomllib.load(handle)
    site_data = data.get("site", {})
    giscus_data = data.get("giscus", {})
    config = SiteConfig(
        title=str(site_data.get("title", "Accelerating Astrophysical Discovery with Foundation Models")),
        base_url=str(site_data.get("base_url", "")),
        membership_form_url=str(site_data.get("membership_form_url", "")),
        giscus=GiscusConfig(
            repo=str(giscus_data.get("repo", "")),
            repo_id=str(giscus_data.get("repo_id", "")),
            category=str(giscus_data.get("category", "Comments")),
            category_id=str(giscus_data.get("category_id", "")),
            theme=str(giscus_data.get("theme", "light")),
        ),
    )
    if production and not config.giscus.configured:
        raise ContentError("production build requires complete giscus configuration")
    return config
