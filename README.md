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

## Contributing

Personal site. Issues are welcome (typo fixes, accessibility regressions, broken links). PRs are not.

## License

Content (`*.md` files, blog posts): all rights reserved.
Code (`_layouts`, `assets`, `_includes`): MIT.
