# Solomon Smith Portfolio

Source for **[solomonsmith.dev](https://solomonsmith.dev)** (GitHub Pages fallback: [solomonsmith-dev.github.io](https://solomonsmith-dev.github.io)).

A Jekyll static site with custom SCSS, hand-written layouts, and content written in Markdown. Deployed via GitHub Pages on every push to `main`.

## Stack

- **Jekyll** for static generation
- **SCSS** for styling (standalone design system in `assets/main.scss`)
- **Liquid** templates for layouts
- **GitHub Pages** for hosting + automatic deploy
- Custom domain via `CNAME`

## Local development

Requires Ruby 3.x and Bundler. System Ruby 2.6 is incompatible with bundler 2.6.x.

```bash
git clone https://github.com/SolomonSmith-dev/SolomonSmith-dev.github.io
cd SolomonSmith-dev.github.io
bundle install
bundle exec jekyll serve --livereload
```

Open `http://localhost:4000`.

## Structure

```
.
├── _config.yml      # Jekyll config + SEO defaults
├── _layouts/        # Page templates (home, page, post)
├── _posts/          # Blog posts
├── assets/          # CSS, JS, images, downloadable resume
├── docs/            # Plans and specs (excluded from build)
├── index.md         # Landing page
├── about.md         # Bio
├── projects.md      # Project listings
├── resume.md        # Web-rendered resume
├── blog.md          # Writing index
├── llms.txt         # AI-assistant summary
├── robots.txt       # Crawler rules + sitemap
└── CNAME            # Custom domain
```

## Featured numbers

The "Numbers you can re-run" section on the home page is rendered from `_data/featured.json` by `_includes/featured.html` (one include line in `index.md`). Each row holds a value and, for `derived` rows, a read-only `rederive` command that prints it from a committed ref in a source repo under `~/Projects`. `manual` rows (private data) carry an `evidence` sentence instead.

```bash
python3 scripts/check_featured.py          # exit 0 verified/manual, 1 drift/error, 2 bad data file
python3 scripts/check_featured.py --json   # same result as JSON
python3 -m unittest discover -s tests -v   # includes tests/test_check_featured.py
```

A number changes only by changing its row and rerunning the check until it reports `verified`. The data file is trusted input: its commands run in a shell.

## Contributing

Personal site. Issues are welcome (typo fixes, accessibility regressions, broken links). PRs are not.

## License

Content (`*.md` files, blog posts): all rights reserved.
Code (`_layouts`, `assets`, `_includes`): MIT.
