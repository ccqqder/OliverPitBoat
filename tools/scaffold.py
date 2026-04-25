#!/usr/bin/env python3
"""
Scaffold new apps or languages for the peach-pit-boat Hugo site.

Usage:
  python tools/scaffold.py new-app <slug>          # add a new app across all current locales
  python tools/scaffold.py new-lang <code> <name>  # add a new language (config + stubs)

Examples:
  python tools/scaffold.py new-app my-new-app
  python tools/scaffold.py new-lang pt-br "Português"
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = SITE_DIR / "content"
CONFIG_DIR = SITE_DIR / "config/_default"
I18N_DIR = SITE_DIR / "i18n"

# Canonical locale order — derived from languages.*.toml weights.
# Update this list when adding a new language via new-lang.
LOCALES = ["en", "ja", "zh-tw", "zh-hans", "fr", "ko", "vi", "id"]

# Locale weights for languages.toml (increment when adding new langs)
_LOCALE_WEIGHTS = {
    "en": 10, "zh-tw": 20, "ja": 30, "zh-hans": 40,
    "fr": 50, "ko": 51, "vi": 52, "id": 53,
}

SECTIONS = ["apps", "support", "privacy"]


# ---------------------------------------------------------------------------
# new-app
# ---------------------------------------------------------------------------

def cmd_new_app(slug: str) -> None:
    title = slug_to_title(slug)
    created = []

    for section in SECTIONS:
        for locale in LOCALES:
            path = CONTENT_DIR / section / f"{slug}.{locale}.md"
            if path.exists():
                print(f"  skip (exists): {relpath(path)}")
                continue
            path.write_text(app_content(slug, title, section, locale))
            created.append(relpath(path))
            print(f"  created: {relpath(path)}")

    print()
    print("Next steps:")
    print(f"  1. Add '{slug}' entry to data/app_url_matrix.yaml")
    print(f"     (slug, name, name_zh, shipped, line, category, store_url, …)")
    print(f"  2. Add app icon to static/images/apps/{slug}.jpg")
    print(f"  3. Fill in English content in:")
    print(f"       content/apps/{slug}.en.md")
    print(f"       content/support/{slug}.en.md")
    print(f"       content/privacy/{slug}.en.md")
    print(f"  4. Translate stub files for each locale you want to support")
    if created:
        print(f"\n  {len(created)} files created.")


def app_content(slug: str, title: str, section: str, locale: str) -> str:
    is_en = locale == "en"

    if section == "apps":
        return f"""\
---
title: {title}
layout: simple
app_slug: {slug}
showDate: false
showReadingTime: false
---
{"" if not is_en else f"""
<!-- Marketing copy for {title}. The tagline and description come from
     data/app_url_matrix.yaml (tagline_en / description_en).
     Add long-form content here. -->
"""}"""

    if section == "support":
        body = _support_body_en(title, slug) if is_en else ""
        return f"""\
---
title: {title} Support
layout: simple
app_slug: {slug}
showDate: false
showReadingTime: false
---
{body}"""

    if section == "privacy":
        body = _privacy_body_en(title) if is_en else ""
        return f"""\
---
title: {title} — Privacy Policy
layout: simple
showDate: false
showReadingTime: false
---
{body}"""

    return ""


def _support_body_en(title: str, slug: str) -> str:
    return f"""
---

## FAQ

**Q: …**
A: …

---

## Troubleshooting

1. **Force quit and relaunch the app**
2. **Check iOS version** ≥ 17.0
3. **Check available storage**

---

## Contact Support

📧 **qqder339@gmail.com**
Subject: `[{title}] Issue Description`

Please include: device model, iOS version, app version, steps to reproduce.

> This app collects no user data. All data is stored locally on your device.
"""


def _privacy_body_en(title: str) -> str:
    today = date.today().isoformat()
    return f"""
**Last Updated: {today}**

---

## 1. Overview

{title}, developed by QQder339, is an iOS app.

**In short: We do NOT collect, store, or transmit any of your personal data to external servers.**

## 2. Data We Do NOT Collect

This app does not collect:

- Personally Identifiable Information (name, email, phone number)
- Location data
- Device identifiers
- Usage analytics or tracking data

## 3. Locally Stored Data

The following data is stored strictly on your device and never transmitted externally:

- **User Settings**: Saves your preferences

## 4. Third-Party Services

This app does **NOT** use any third-party analytics or advertising frameworks.

## 5. Contact Us

📧 **qqder339@gmail.com**
Subject: {title} Privacy Policy Inquiry
"""


# ---------------------------------------------------------------------------
# new-lang
# ---------------------------------------------------------------------------

def cmd_new_lang(code: str, lang_name: str) -> None:
    display = code.upper().replace("-", "")[:4]
    weight = max(_LOCALE_WEIGHTS.values()) + 1

    # 1. languages config
    lang_toml = CONFIG_DIR / f"languages.{code}.toml"
    if not lang_toml.exists():
        lang_toml.write_text(f"""\
disabled = false
languageCode = "{code}"
languageName = "{lang_name}"
weight = {weight}
title = "QQder 核舟記部落格"

[params]
  displayName = "{display}"
  isoCode = "{code}"
  dateFormat = "2 January 2006"
  description = "Free, ad-free iOS Apps + AI-assisted dev journal · The Miniature Boat"

[params.author]
  name = "QQder 核舟記部落格"
  image = "img/author.png"
  headline = "Indie Dev · Free & Ad-free · AI Coding Journal"
  bio = "Eight iOS apps — all free, no ads, no tracking. Pick one and try it. Also a running log of how a humanities-background sysadmin builds apps from scratch with AI vibe coding."
  links = [
    {{ github = "https://github.com/ccqqder" }},
    {{ email = "mailto:qqder339@gmail.com" }},
  ]
""")
        print(f"  created: {relpath(lang_toml)}")
    else:
        print(f"  skip (exists): {relpath(lang_toml)}")

    # 2. menus config
    menus_toml = CONFIG_DIR / f"menus.{code}.toml"
    if not menus_toml.exists():
        menus_toml.write_text(f"""\
# TODO: translate all menu names to {lang_name}

[[main]]
  name = "Home"
  pageRef = "/"
  weight = 10

[[main]]
  name = "Apps"
  pageRef = "apps"
  weight = 20

[[main]]
  name = "Blog"
  pageRef = "posts"
  weight = 30

[[main]]
  name = "About"
  pageRef = "about"
  weight = 40

[[footer]]
  name = "Support"
  pageRef = "support"
  weight = 10

[[footer]]
  name = "Privacy"
  pageRef = "privacy"
  weight = 20
""")
        print(f"  created: {relpath(menus_toml)}")
    else:
        print(f"  skip (exists): {relpath(menus_toml)}")

    # 3. i18n file — copy en.yaml with TODO markers
    i18n_en = I18N_DIR / "en.yaml"
    i18n_new = I18N_DIR / f"{code}.yaml"
    if not i18n_new.exists():
        en_text = i18n_en.read_text()
        # Prefix each value line with TODO so translators know what needs work
        new_text = re.sub(
            r'^(  other: )(.+)$',
            r'\1# TODO \2',
            en_text,
            flags=re.MULTILINE,
        )
        i18n_new.write_text(new_text)
        print(f"  created: {relpath(i18n_new)}")
    else:
        print(f"  skip (exists): {relpath(i18n_new)}")

    # 4. Section _index files
    _index_defaults = {
        "apps":    ("Apps", "list"),
        "support": ("Support", "simple"),
        "privacy": ("Privacy Policies", "simple"),
    }
    for section, (default_title, layout) in _index_defaults.items():
        idx = CONTENT_DIR / section / f"_index.{code}.md"
        if not idx.exists():
            idx.write_text(f"""\
---
title: {default_title}  # TODO: translate to {lang_name}
layout: {layout}
showDate: false
showReadingTime: false
---
""")
            print(f"  created: {relpath(idx)}")
        else:
            print(f"  skip (exists): {relpath(idx)}")

    # 5. Per-app stub files for all 3 sections
    existing_apps = sorted(
        f.stem.replace(".en", "")
        for f in (CONTENT_DIR / "apps").glob("*.en.md")
        if not f.name.startswith("_")
    )
    for slug in existing_apps:
        title = slug_to_title(slug)
        for section in SECTIONS:
            path = CONTENT_DIR / section / f"{slug}.{code}.md"
            if path.exists():
                print(f"  skip (exists): {relpath(path)}")
                continue
            path.write_text(app_content(slug, title, section, code))
            print(f"  created: {relpath(path)}")

    print()
    print("Next steps:")
    print(f"  1. Translate menu names in {relpath(menus_toml)}")
    print(f"  2. Translate i18n strings in {relpath(i18n_new)}")
    print(f"     (search for '# TODO' — {len(list(i18n_en.read_text().splitlines()))} lines)")
    print(f"  3. Add 'tagline_{code.replace('-','_')}', 'description_{code.replace('-','_')}',")
    print(f"     'features_{code.replace('-','_')}' fields to data/app_url_matrix.yaml")
    print(f"     for each app that has a full translation.")
    print(f"  4. Update LOCALES list in tools/scaffold.py to include '{code}'")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slug_to_title(slug: str) -> str:
    return slug.replace("-", " ").title()


def relpath(p: Path) -> str:
    return str(p.relative_to(SITE_DIR))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="cmd", metavar="COMMAND")

    p_app = sub.add_parser("new-app", help="Scaffold content files for a new app")
    p_app.add_argument("slug", help="Kebab-case app slug, e.g. my-new-app")

    p_lang = sub.add_parser("new-lang", help="Scaffold config + stubs for a new language")
    p_lang.add_argument("code", help="BCP-47 language code, e.g. pt-br")
    p_lang.add_argument("name", help="Language name in its own script, e.g. Português")

    args = parser.parse_args()

    if args.cmd == "new-app":
        print(f"Scaffolding new app: {args.slug}")
        cmd_new_app(args.slug)
    elif args.cmd == "new-lang":
        print(f"Scaffolding new language: {args.code} ({args.name})")
        cmd_new_lang(args.code, args.name)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
