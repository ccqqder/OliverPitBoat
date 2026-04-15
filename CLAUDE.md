# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**核舟 (The Miniature Boat)** — A Hugo static site on GitHub Pages serving as:
- Personal brand / "Digital Ark" for an indie iOS developer
- App showcase matrix with individual app landing pages + support/legal pages
- Dual-track blog: "The Workshop" (dev logs) + "The Observatory" (humanities/tech essays)

## Tech Stack

- **Generator:** Hugo Extended (v0.155.2 pinned in CI, `TZ: Asia/Taipei`)
- **Theme:** Blowfish (`themes/blowfish/`) — never edit directly, override in root `layouts/` or `assets/`
- **Hosting:** GitHub Pages via `actions/deploy-pages` (NOT gh-pages branch push)
- **CMS:** TinaCMS (local-only, no cloud; `clientId: null, token: null`)
- **Language:** Trilingual — zh-tw (primary), en, ja

> Note: `themes/PaperMod/` is also present as a submodule but is NOT the active theme.

## Common Commands

```bash
# Dev server with TinaCMS (CMS admin at /admin/)
npm run dev

# Dev server without CMS (Hugo only, with drafts)
hugo server -D

# Production build (TinaCMS + Hugo)
npm run build

# Hugo-only production build
hugo --minify

# Create new blog post
hugo new posts/my-post.md
```

## Architecture

### Config Directory (`config/_default/`)
Config is split across multiple files — not a single root `hugo.toml`:
- `hugo.toml` — baseURL, theme, language defaults, taxonomies, output formats
- `params.toml` — Blowfish theme params (colorScheme, appearance, homepage layout, article display)
- `languages.zh-tw.toml`, `languages.en.toml`, `languages.ja.toml` — per-language title, description, author, links
- `menus.zh-tw.toml`, `menus.en.toml`, `menus.ja.toml` — nav menu items per language
- `markup.toml` — Goldmark parser settings, syntax highlighting, TOC levels

### Content Structure
```
content/
├── posts/          # Blog articles (categories: "The Workshop" or "The Observatory")
│   ├── my-post.md           # zh-tw (default)
│   ├── my-post.en.md        # English translation
│   └── my-post.ja.md        # Japanese translation
├── apps/           # App showcase
│   ├── _index.md            # Matrix table of all apps (markdown table format)
│   └── app-name.md          # Individual app landing page (layout: simple)
├── privacy/        # Per-app privacy policy pages (all trilingual)
│   ├── _index.md            # Privacy policies index (zh-tw/en/ja)
│   └── app-slug.md          # Individual privacy policy (layout: simple, url: /privacy/app-slug/)
├── support/        # Per-app support pages (all trilingual)
│   ├── _index.md            # Support index (zh-tw/en/ja)
│   └── app-slug.md          # Individual support page (layout: simple, url: /support/app-slug/)
└── about.md        # About page (zh-tw); about.en.md, about.ja.md for translations

All content sections (posts, apps, privacy, support) follow the filename-suffix multilingual pattern.
Every `page.md` has a corresponding `page.en.md` and `page.ja.md`.
```

### Static Assets
```
static/api/
├── apps.json           # Shared runtime contract — iOS apps fetch this for cross-promotion
└── asc-metadata.json   # App Store Connect metadata export
static/images/
└── screenshots/        # Per-app screenshots organized by app slug
```

### Custom Assets (override Blowfish)
```
assets/
├── css/custom.css              # Global custom CSS overrides
├── css/schemes/braun.css       # Custom "braun" color scheme
└── img/author.gif              # Author avatar
```

### Layouts
```
layouts/
├── shortcodes/app-card.html    # App card component (icon, name, desc, optional store link)
├── partials/favicons.html      # Favicon override
├── _default/_markup/render-image.html  # Custom image rendering
├── apps/                       # Custom layouts for apps section
└── support/                    # Custom layouts for support pages
```

## Key Conventions

### Content Front Matter (Posts)
Always use YAML (not TOML) for consistency with existing content:
```yaml
---
title: "Post Title"
date: 2026-02-09T14:00:00+08:00
draft: false
tags: ["iOS Dev", "App Store"]
categories: ["The Workshop"]  # or "The Observatory"
description: "Short summary"
---
```
- Categories must be one of: `"The Workshop"` (dev/tech) or `"The Observatory"` (humanities/essays)
- Dates use `+08:00` (Asia/Taipei) timezone offset
- The default archetype uses TOML (`+++`) — always convert to YAML when creating manually

### App Landing Page Front Matter
```yaml
---
title: App Display Name
layout: simple
url: /apps/app-slug/
summary: One-line tagline
app_slug: app-slug
showDate: false
showReadingTime: false
---
```

### apps.json Schema (shared contract — keep stable)
```json
{
  "apps": [{
    "id": "com.memode.appname",
    "name": "Display Name",
    "icon_url": "https://ccqqder.github.io/PeachPitBoat/images/apps/icon.png",
    "description": "Short description",
    "store_url": "#",
    "is_promoted": true
  }]
}
```
iOS apps consume this JSON at runtime. Schema changes require coordinating with app releases.

### app-card Shortcode
```
{{< app-card name="Display Name" icon="🪐" desc="Short description" url="https://..." >}}
```
- `icon` — emoji (not image), displayed at 3em
- `url` — set to `"#"` to hide the App Store button

## i18n / Multilingual

Uses Hugo's **filename-suffix** mode (`defaultContentLanguageInSubdir = false`):
- `content/posts/my-post.md` → zh-tw (default, served at root `/posts/my-post/`)
- `content/posts/my-post.en.md` → English (served at `/en/posts/my-post/`)
- `content/posts/my-post.ja.md` → Japanese (served at `/ja/posts/my-post/`)

Hugo auto-links translation pairs by filename stem. Language switcher is built into Blowfish.

Menu items and author info are defined per-language in `config/_default/languages.*.toml` and `config/_default/menus.*.toml`.

## Design Decisions

- **Color scheme:** `braun` (custom Dieter Rams-inspired palette, defined in `assets/css/schemes/braun.css`)
- **Dark mode first:** `defaultAppearance = "dark"`, `autoSwitchAppearance = true` in `params.toml`
- **No tracking/cookies** — no analytics, no cookie banners
- **Output formats:** HTML + RSS + JSON (JSON enables search)
- **baseURL:** `https://ccqqder.github.io/PeachPitBoat/` — all absolute URLs use this prefix
- **Goldmark unsafe mode enabled** — allows raw HTML in Markdown

## CMS (TinaCMS)

- Config: `tina/config.ts` — defines collections (posts, apps page, about page), fields, rich-text toolbar
- Build output: `static/admin/` (generated by TinaCMS build, not committed)
- Media uploads go to `static/images/`
- Does NOT auto-commit — use git manually after editing via CMS

## Deployment

Push to `main` triggers GitHub Actions → Hugo Extended build → `actions/deploy-pages`. The workflow uses `actions/configure-pages` to set the baseURL dynamically. No TinaCMS step in CI — Hugo builds directly.

## Git History Rewriting Safety

**NEVER use `git stash` before `filter-branch`, `reset --soft`, or any history rewriting operation.** `filter-branch` rewrites all refs including stash, making stashed changes unrecoverable.

Instead, commit uncommitted changes to a temporary branch first:
```bash
git checkout -b temp-backup
git add -A && git commit -m "backup"
git checkout main
# ... do filter-branch / squash / reset ...
# then restore:
git checkout temp-backup -- path/to/files
git branch -D temp-backup
```

**Never run `gc --prune=now` immediately after history rewriting** — keep dangling objects as a safety net until verified.

## Related Docs

- `PRD.md` — Product requirements document (project vision and goals)
- `SPEC.md` — Technical specification
- `POC_PLAN.md` — Proof of concept plan for initial site setup
