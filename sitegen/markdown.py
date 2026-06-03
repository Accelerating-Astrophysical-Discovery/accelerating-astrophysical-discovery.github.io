"""Small Markdown renderer used by the static generator.

It intentionally supports only the syntax this site needs for generated pages:
headings, paragraphs, lists, links, images, emphasis, inline code, fenced code,
tables, raw HTML blocks, and KaTeX delimiters in text.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from markdown_it import MarkdownIt

from .codecogs import convert_codecogs_markdown

_FENCE_RE = re.compile(r"^```([A-Za-z0-9_-]+)?\s*$")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
_ORDERED_RE = re.compile(r"^\d+\.\s+(.+?)\s*$")
_UNORDERED_RE = re.compile(r"^[-*]\s+(.+?)\s*$")
_LOCAL_IMAGE_RE = re.compile(r"(!\[[^\]]*\]\()((?!https?:|/|#)[^)]+)(\))")


def codecogs_to_latex(markdown: str) -> str:
    """Backward-compatible wrapper for legacy content conversion tests."""
    return convert_codecogs_markdown(markdown)


def render_markdown(
    markdown: str,
    path: Path | None = None,
    section: str | None = None,
    slug: str | None = None,
) -> str | tuple[str, str]:
    """Render Markdown to HTML.

    With one argument this returns HTML. The build path passes path/section/slug
    and receives ``(html, excerpt)`` after local asset links are rewritten.
    """
    text = _strip_front_matter(convert_codecogs_markdown(markdown))
    if section and slug:
        text = rewrite_local_image_links(text, section, slug)
    html_output = _render_markdown_inner(text)
    if path is not None or section is not None or slug is not None:
        return html_output, markdown_excerpt(text)
    return html_output


def _render_markdown_inner(text: str) -> str:
    """Render a conservative subset of Markdown to HTML."""
    text = _strip_kramdown_image_attrs(text)
    protected, math_tokens = _stash_math(text)
    html_output = MarkdownIt("commonmark", {"html": True}).enable("table").render(protected)
    return _restore_math(html_output, math_tokens)

    lines = text.splitlines()
    blocks: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    list_kind: str | None = None
    in_code = False
    code_lang = ""
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            content = " ".join(part.strip() for part in paragraph).strip()
            if content:
                blocks.append(f"<p>{_render_inline(content)}</p>")
            paragraph.clear()

    def flush_list() -> None:
        nonlocal list_kind
        if list_kind and list_items:
            tag = "ol" if list_kind == "ol" else "ul"
            blocks.append(f"<{tag}>" + "".join(list_items) + f"</{tag}>")
        list_items.clear()
        list_kind = None

    for line in lines:
        fence = _FENCE_RE.match(line)
        if in_code:
            if fence:
                language = f' class="language-{html.escape(code_lang)}"' if code_lang else ""
                code = html.escape("\n".join(code_lines))
                blocks.append(f"<pre><code{language}>{code}</code></pre>")
                in_code = False
                code_lang = ""
                code_lines.clear()
            else:
                code_lines.append(line)
            continue

        if fence:
            flush_paragraph()
            flush_list()
            in_code = True
            code_lang = fence.group(1) or ""
            continue

        if not line.strip():
            flush_paragraph()
            flush_list()
            continue

        heading = _HEADING_RE.match(line)
        if heading:
            flush_paragraph()
            flush_list()
            level = len(heading.group(1))
            blocks.append(f"<h{level}>{_render_inline(heading.group(2))}</h{level}>")
            continue

        unordered = _UNORDERED_RE.match(line)
        ordered = _ORDERED_RE.match(line)
        if unordered or ordered:
            flush_paragraph()
            next_kind = "ul" if unordered else "ol"
            if list_kind and list_kind != next_kind:
                flush_list()
            list_kind = next_kind
            item = (unordered or ordered).group(1)
            list_items.append(f"<li>{_render_inline(item)}</li>")
            continue

        if _looks_like_raw_html(line):
            flush_paragraph()
            flush_list()
            blocks.append(line)
            continue

        paragraph.append(line)

    if in_code:
        language = f' class="language-{html.escape(code_lang)}"' if code_lang else ""
        blocks.append(f"<pre><code{language}>{html.escape(chr(10).join(code_lines))}</code></pre>")
    flush_paragraph()
    flush_list()
    return "\n".join(blocks)


def rewrite_local_image_links(markdown: str, section: str, slug: str) -> str:
    def replace(match: re.Match[str]) -> str:
        return (
            f"{match.group(1)}/assets/content/{section}/{slug}/"
            f"{match.group(2)}{match.group(3)}"
        )

    return _LOCAL_IMAGE_RE.sub(replace, markdown)


def _strip_kramdown_image_attrs(text: str) -> str:
    text = re.sub(r"(!\[[^\]]*]\([^)]*\))\{:\s*[^}]+\s*\}", r"\1", text)
    return re.sub(r"(?m)^\s*\{:\s*[^}]+\s*\}\s*$\n?", "", text)


def _stash_math(text: str) -> tuple[str, list[str]]:
    tokens: list[str] = []

    def stash(match: re.Match[str]) -> str:
        tokens.append(match.group(0))
        return f"@@MATH{len(tokens) - 1}@@"

    pattern = re.compile(r"\\\[[\s\S]+?\\\]|\\\([\s\S]+?\\\)|\$\$[\s\S]+?\$\$")
    return pattern.sub(stash, text), tokens


def _restore_math(text: str, tokens: list[str]) -> str:
    for index, token in enumerate(tokens):
        text = text.replace(f"@@MATH{index}@@", token)
    return text


def markdown_excerpt(markdown: str, limit: int = 42) -> str:
    """Return a short plain-text excerpt from Markdown."""
    text = _strip_front_matter(convert_codecogs_markdown(markdown))
    text = _strip_kramdown_image_attrs(text)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"<section\b[^>]*>.*?</section>", " ", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)]\([^)]*\)", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"[*_#>{}\[\]()`\\]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "..."


def _strip_front_matter(markdown: str) -> str:
    if not markdown.startswith("---\n"):
        return markdown
    end = markdown.find("\n---", 4)
    if end == -1:
        return markdown
    after = markdown.find("\n", end + 4)
    return "" if after == -1 else markdown[after + 1 :]


def _render_inline(text: str) -> str:
    placeholders: list[str] = []

    def stash(match: re.Match[str]) -> str:
        placeholders.append(f"<code>{html.escape(match.group(1))}</code>")
        return f"\x00{len(placeholders) - 1}\x00"

    escaped = re.sub(r"`([^`]*)`", stash, html.escape(text, quote=True))
    escaped = re.sub(r"!\[([^\]]*)]\(([^)\s]+)\)", _image_replacement, escaped)
    escaped = re.sub(r"\[([^\]]+)]\(([^)\s]+)\)", _link_replacement, escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)

    for index, replacement in enumerate(placeholders):
        escaped = escaped.replace(f"\x00{index}\x00", replacement)
    return escaped


def _image_replacement(match: re.Match[str]) -> str:
    alt = match.group(1)
    src = match.group(2)
    return f'<img src="{src}" alt="{alt}">'


def _link_replacement(match: re.Match[str]) -> str:
    label = match.group(1)
    href = match.group(2)
    return f'<a href="{href}">{label}</a>'


def _looks_like_raw_html(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("<") and stripped.endswith(">")
