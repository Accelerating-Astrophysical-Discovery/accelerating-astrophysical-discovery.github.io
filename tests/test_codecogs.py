from __future__ import annotations

import unittest

from sitegen.codecogs import codecogs_url_to_latex, convert_codecogs_markdown


class CodecogsTests(unittest.TestCase):
    def test_url_decodes_html_entities_and_spaces(self) -> None:
        url = (
            "https://latex.codecogs.com/svg.latex?"
            "p(\\mathbf{x}_{0:T},&space;\\mathbf{y}_{0:T})"
            "&space;=&space;x&plus;y"
        )
        self.assertEqual(codecogs_url_to_latex(url), r"p(\mathbf{x}_{0:T}, \mathbf{y}_{0:T}) = x+y")

    def test_inline_codecogs_image_becomes_inline_math(self) -> None:
        markdown = r"State ![eqn](https://latex.codecogs.com/svg.latex?\beta=1) is final."
        self.assertEqual(convert_codecogs_markdown(markdown), r"State \(\beta=1\) is final.")

    def test_line_codecogs_image_becomes_display_math_with_parentheses(self) -> None:
        markdown = (
            r"![the Markov decomposition]"
            r"(https://latex.codecogs.com/svg.latex?p(x)&space;=&space;p(y))"
        )
        self.assertEqual(convert_codecogs_markdown(markdown), "\\[\np(x) = p(y)\n\\]")


if __name__ == "__main__":
    unittest.main()
