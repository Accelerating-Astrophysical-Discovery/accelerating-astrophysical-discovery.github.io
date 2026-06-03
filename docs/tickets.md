# Redesign Tickets

## 1. Scaffold

Add `sitegen/`, `site/`, `docs/`, `environment.yml`, dependency files, ignore rules, and GitHub Actions deployment.

## 2. Generator

Implement strict TOML schema validation, newest-first ordering, Markdown rendering, Codecogs-to-LaTeX conversion, route rendering, and manifest output.

## 3. Static Assets

Copy site assets, member images, and writing assets into the generated output.

## 4. Interface

Build the creamy minimalist landing page, writing indexes/details, defocus effect, reduced-motion fallback, and giscus mount.

## 5. Migration

Copy existing `_posts/` and `inprep_posts/` into `research/`, strip Jekyll front matter, convert Codecogs links to LaTeX, and archive old CV/theme material in `old_content/`.

## 6. Review

Run generator tests, static build, visual smoke checks, content migration review, image review, giscus setup review, and deployment review before accepting.
