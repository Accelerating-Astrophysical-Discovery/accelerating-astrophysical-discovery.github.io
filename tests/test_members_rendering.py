from __future__ import annotations

import unittest
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from sitegen.content import Member, SiteConfig


ROOT = Path(__file__).resolve().parents[1]


class MembersRenderingTests(unittest.TestCase):
    def test_member_card_renders_profile_fields(self) -> None:
        env = Environment(
            loader=FileSystemLoader(ROOT / "site" / "templates"),
            autoescape=select_autoescape(["html", "xml"]),
        )
        member = Member(
            slug="jane-doe",
            name="Jane Doe",
            last_name="Doe",
            join_date=date(2026, 1, 1),
            image_path=ROOT / "jane-doe.jpg",
            metadata_path=ROOT / "jane-doe.toml",
            affiliations=["Example Institute"],
            research_areas=["Multimodal data"],
            bio="Builds foundation-model datasets.",
        )

        html = env.get_template("members.html").render(
            site=SiteConfig(membership_form_url="https://docs.google.com/forms/example"),
            active="members",
            members=[member],
        )

        self.assertIn('<h1 class="defocus-item">Members</h1>', html)
        self.assertIn('src="/assets/members/jane-doe.jpg"', html)
        self.assertIn("Example Institute", html)
        self.assertIn("Multimodal data", html)
        self.assertIn("Builds foundation-model datasets.", html)
        self.assertIn('aria-label="Consortium members"', html)
        self.assertIn('href="https://docs.google.com/forms/example"', html)
        self.assertIn(">Join the consortium</a>", html)
        self.assertIn("permission before any profile information", html)

    def test_join_prompt_is_hidden_without_a_form_url(self) -> None:
        env = Environment(
            loader=FileSystemLoader(ROOT / "site" / "templates"),
            autoescape=select_autoescape(["html", "xml"]),
        )

        html = env.get_template("members.html").render(
            site=SiteConfig(),
            active="members",
            members=[],
        )

        self.assertNotIn("Join the consortium", html)


if __name__ == "__main__":
    unittest.main()
