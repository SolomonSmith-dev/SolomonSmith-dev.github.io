# Performance notes

- Headshot: `assets/images/headshot.jpg` ~47 KB, explicit width/height, `fetchpriority="high"` on home
- Fonts: Google Fonts preconnect + display=swap already
- CSS: single `assets/main.scss` design system (Pages builds to CSS)

## Targets (DI-11 provisional)

- Keep headshot under ~100 KB
- Avoid new hero weight
- No layout shift from missing image dimensions (already set)

## Status

No heavy perf regression introduced by CTA reorder. Lighthouse CLI not run this turn; record scores when available.
