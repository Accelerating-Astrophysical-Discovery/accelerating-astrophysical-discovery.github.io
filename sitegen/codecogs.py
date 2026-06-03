"""Utilities for translating legacy CodeCogs image equations to LaTeX."""

from __future__ import annotations

import html
from urllib.parse import unquote

CODECOGS_PREFIXES = (
    "https://latex.codecogs.com/svg.latex?",
    "http://latex.codecogs.com/svg.latex?",
    "https://latex.codecogs.com/gif.latex?",
    "http://latex.codecogs.com/gif.latex?",
    "https://latex.codecogs.com/png.latex?",
    "http://latex.codecogs.com/png.latex?",
)


def codecogs_url_to_latex(url: str) -> str:
    """Extract a LaTeX expression from a CodeCogs equation URL."""
    for prefix in CODECOGS_PREFIXES:
        if url.startswith(prefix):
            expression = url[len(prefix) :].replace("&space;", " ")
            decoded = html.unescape(unquote(expression))
            return decoded.replace("\xa0", " ").strip()
    raise ValueError(f"not a CodeCogs LaTeX URL: {url}")


def convert_codecogs_markdown(markdown: str) -> str:
    """Convert Markdown image links that point at CodeCogs into KaTeX text.

    Inline image equations become ``\\(...\\)``. If a CodeCogs image is the
    only meaningful content on a line it becomes display math ``\\[...\\]``.
    """
    return "\n".join(_convert_codecogs_line(line) for line in markdown.splitlines())


def _convert_codecogs_line(line: str) -> str:
    replacements: list[tuple[int, int, str]] = []
    search_from = 0
    while True:
        start = line.find("![", search_from)
        if start == -1:
            break
        alt_end = line.find("](", start + 2)
        if alt_end == -1:
            break
        url_start = alt_end + 2
        url_end = _find_markdown_url_end(line, url_start)
        if url_end == -1:
            break
        url = line[url_start:url_end]
        if url.startswith(CODECOGS_PREFIXES):
            latex = codecogs_url_to_latex(url)
            token = line[start : url_end + 1]
            display = line.strip() == token
            replacement = f"\\[\n{latex}\n\\]" if display else f"\\({latex}\\)"
            replacements.append((start, url_end + 1, replacement))
        search_from = url_end + 1

    if not replacements:
        return line

    result: list[str] = []
    last = 0
    for start, end, replacement in replacements:
        result.append(line[last:start])
        result.append(replacement)
        last = end
    result.append(line[last:])
    return "".join(result)


def _find_markdown_url_end(line: str, start: int) -> int:
    depth = 0
    index = start
    while index < len(line):
        char = line[index]
        if char == "(":
            depth += 1
        elif char == ")":
            if depth == 0:
                return index
            depth -= 1
        index += 1
    return -1
