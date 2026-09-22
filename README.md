# Accelerating Astrophysical Discovery

Source for the Accelerating Astrophysical Discovery with Foundation Models site.

GitHub Actions builds the static site into `dist/` and deploys that generated
artifact to GitHub Pages. Generated `dist/` output is intentionally not tracked
on `main`.

## Site identity and sharing

The homepage and social-preview description share the `description` field in
`site_config.toml`. Every page includes Open Graph and Twitter/X summary-card
metadata, a canonical URL, and browser/touch icons. Article preview titles use
the article title; the HTML titles used to match existing GitHub discussions are
unchanged.

The editable constellation icon is `site/assets/branding/icon.svg`. To regenerate
the committed PNG and ICO exports after editing it, install `rsvg-convert`
(librsvg) and run:

```bash
conda run -n astrophysical_discovery_py python scripts/build_brand_assets.py
```

Ordinary site builds use the committed exports and need no extra dependencies.
Sharing services may cache older previews until they fetch the page again.
