# SolomonSmith-dev.github.io

The source for **[solomonsmith-dev.github.io](https://solomonsmith-dev.github.io)**, my personal portfolio site.

A Jekyll static site with custom SCSS, hand-written layouts, and content written in Markdown. No theme, no framework, no Tailwind. Deployed via GitHub Pages on every push to `main`.

## Stack

- **Jekyll** for static generation
- **SCSS** for styling (no preprocessor frameworks)
- **Liquid** templates for layouts and includes
- **GitHub Pages** for hosting + automatic deploy
- Custom CNAME for the github.io subdomain

## Local development

Requires Ruby 3.x and Bundler.

```bash
git clone https://github.com/SolomonSmith-dev/SolomonSmith-dev.github.io
cd SolomonSmith-dev.github.io
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000`.

## Structure

```
.
├── _config.yml      # Jekyll config
├── _layouts/        # Page templates (home, page, post)
├── _sass/           # SCSS partials
├── _posts/          # Blog posts
├── assets/          # CSS, images, downloadable resume
├── index.md         # Landing page
├── about.md         # Bio
├── projects.md      # Featured project listings
├── resume.md        # Web-rendered resume
├── blog.md          # Blog index
└── CNAME            # Custom domain config
```

## Contributing

Personal site. Issues are welcome (typo fixes, accessibility regressions, broken links). PRs are not.

## License

Content (`*.md` files, blog posts): all rights reserved.
Code (`_layouts`, `_sass`, `_includes`): MIT.
