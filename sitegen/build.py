from __future__ import annotations

from pathlib import Path

from .content import SiteData, collect_members, collect_writings, load_config
from .loader import load_site as load_manifest
from .markdown import render_markdown
from .render import build_site


def load_site(root: Path, production: bool = False) -> SiteData:
    load_manifest(root)
    config = load_config(root, production=production)
    seen_comment_ids: set[str] = set()
    members = collect_members(root)
    news = collect_writings(root, "news", render_markdown, seen_comment_ids)
    research = collect_writings(root, "research", render_markdown, seen_comment_ids)
    return SiteData(config=config, members=members, news=news, research=research)


def build(root: Path, output: Path, production: bool = False) -> SiteData:
    data = load_site(root, production=production)
    build_site(data, root, output)
    return data
