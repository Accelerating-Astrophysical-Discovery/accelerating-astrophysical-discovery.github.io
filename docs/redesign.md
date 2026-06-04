# Workshop Site Redesign

This repository is moving from a Beautiful Jekyll CV-style site to a Python-generated static workshop site for members, news, and research. The generated site is deployed from `dist/` by GitHub Actions and keeps source content in human-editable TOML and Markdown files.

## Content Model

Members live under `members/` as same-stem image/TOML pairs:

```text
members/<slug>.<jpg|png|webp|gif>
members/<slug>.toml
```

Member TOML requires `name`, `join_date`, `affiliations`, `research_areas`, and `bio`; `last_name` is optional but recommended for compound surnames. Lists sort by `join_date`, then by last name for matching dates.

News and research entries use matching Markdown/TOML pairs:

```text
news/<slug>/<slug>.md
news/<slug>/<slug>.toml
research/<slug>/<slug>.md
research/<slug>/<slug>.toml
```

Writing TOML requires `title` and `date_published`. Lists sort newest-first, then alphabetically for matching dates.

## Rendering

The generator validates content strictly, renders Markdown to HTML, keeps LaTeX delimiters for client-side KaTeX rendering, and emits static routes under `dist/`. Text/list surfaces use a subtle pointer and keyboard focus defocus effect.

## Comments

giscus can provide GitHub-backed comments and reactions through Discussions after it is configured for the workshop repository. Production builds require the repo, repo ID, category, and category ID in `site_config.toml`.

Before comments work publicly, enable GitHub Pages from Actions, enable Discussions on the site repository, install the giscus GitHub App for that repository, create or select the `Announcements` discussion category, and copy the generated category ID into `site_config.toml`. Until then, normal builds deploy the site with a placeholder comments message; `python scripts/build_site.py --production` remains the strict giscus readiness check.
