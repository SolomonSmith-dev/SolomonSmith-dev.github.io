# Local Jekyll build verification

Date: 2026-11-07 (UTC)

```bash
bundle exec jekyll build
```

Result: success in ~0.3s → `_site/`

## Render checks on `_site/index.html`

- Hero CTA order: Email me → Download resume → View selected work
- Header contains Resume + Contact
- SOC Triage Problem row present on home
- Zero em-dash characters across built HTML
- Zero internship / GPA / Dean's List hits in built HTML

## Note

`vendor/` and `_site/` are gitignored; not committed.
