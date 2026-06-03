"""Typed manifest models for generated site templates."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any, Literal


@dataclass(frozen=True)
class MemberEntry:
    slug: str
    name: str
    last_name: str
    join_date: date
    image_path: str
    metadata_path: str
    affiliations: tuple[str, ...]
    research_areas: tuple[str, ...]
    bio: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "slug": self.slug,
            "name": self.name,
            "last_name": self.last_name,
            "join_date": self.join_date.isoformat(),
            "image_path": self.image_path,
            "metadata_path": self.metadata_path,
            "affiliations": list(self.affiliations),
            "research_areas": list(self.research_areas),
            "bio": self.bio,
        }


@dataclass(frozen=True)
class TextEntry:
    kind: Literal["essay", "news", "research"]
    slug: str
    title: str
    date_published: date
    markdown_path: str
    metadata_path: str
    html: str
    excerpt: str
    comment_id: str

    @property
    def comment_term(self) -> str:
        return f"[{self.kind}/comments] {self.comment_id}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "slug": self.slug,
            "title": self.title,
            "date_published": self.date_published.isoformat(),
            "markdown_path": self.markdown_path,
            "metadata_path": self.metadata_path,
            "html": self.html,
            "excerpt": self.excerpt,
            "comment_id": self.comment_id,
            "comment_term": self.comment_term,
        }


@dataclass(frozen=True)
class BuildManifest:
    members: tuple[MemberEntry, ...] = field(default_factory=tuple)
    news: tuple[TextEntry, ...] = field(default_factory=tuple)
    research: tuple[TextEntry, ...] = field(default_factory=tuple)
    version: int = 1

    def to_dict(self) -> dict[str, Any]:
        return {
            "version": self.version,
            "members": [member.to_dict() for member in self.members],
            "news": [entry.to_dict() for entry in self.news],
            "research": [entry.to_dict() for entry in self.research],
        }
