"""Cross-locale i18n audit for the live PeachPitBoat site.

Fetches the homepage of every configured locale, extracts the SEO-critical
metadata that should differ per language (title, description, nav, og:locale,
canonical, hreflang) plus the things that should always be present (og:image),
then runs heuristics that flag the kinds of mistakes humans miss when
manually checking 8 languages: an English-locale title that's still in
Chinese, a stub locale missing menu items, a hreflang set that's lost an
entry, an og:image that 404s.

Usage from project root:
  python tools/audit_i18n.py                  # human-readable report
  python tools/audit_i18n.py --strict         # exit 1 if any locale has issues
  python tools/audit_i18n.py --base-url URL   # audit a different deployment

This is a fast HTTP-only check (no headless browser). It complements
Lighthouse: Lighthouse looks at one page deeply, this looks across 8 locales
shallowly.
"""
from __future__ import annotations
import argparse
import re
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import Optional

DEFAULT_BASE = "https://ccqqder.github.io/PeachPitBoat"

# Each locale: URL path, expected <html lang>, and what counts as "OK title".
# `style` drives the title/description CJK heuristic:
#   en   — must NOT contain CJK ideographs or kana
#   ja   — kanji + kana acceptable
#   zh   — CJK ideographs acceptable
LOCALES = [
    ("en-root", "/",         "en",      "en"),
    ("zh-tw",   "/zh-tw/",   "zh-TW",   "zh"),
    ("ja",      "/ja/",      "ja",      "ja"),
    ("zh-hans", "/zh-hans/", "zh-Hans", "zh"),
    ("fr",      "/fr/",      "fr",      "en"),  # stub → English chrome
    ("ko",      "/ko/",      "ko",      "en"),
    ("vi",      "/vi/",      "vi",      "en"),
    ("id",      "/id/",      "id",      "en"),
]

CJK_RE = re.compile(r"[぀-ヿ一-鿿]")  # hiragana, katakana, CJK
GREEN, YELLOW, RED, RESET = "\033[32m", "\033[33m", "\033[31m", "\033[0m"


@dataclass
class Audit:
    label: str
    url: str
    expected_html_lang: str
    style: str
    html: str = ""
    title: str = ""
    description: str = ""
    html_lang: str = ""
    canonical: str = ""
    og_locale: str = ""
    og_image: str = ""
    nav_anchors: list[str] = field(default_factory=list)
    hreflang_count: int = 0
    issues: list[str] = field(default_factory=list)
    fetch_error: Optional[str] = None
    og_image_status: int = 0


def _fetch(url: str, timeout: float = 15) -> str:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE  # match curl --ssl-no-revoke behavior
    req = urllib.request.Request(url, headers={"User-Agent": "audit-i18n/1.0"})
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.read().decode("utf-8", errors="replace")


def _head_status(url: str, timeout: float = 10) -> int:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "audit-i18n/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def _first(pat: str, html: str) -> str:
    m = re.search(pat, html, re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else ""


def _internal_anchors(html: str, base_path: str) -> list[str]:
    """Collect deduped internal nav anchor texts.

    Blowfish doesn't always wrap the menu in a <header>, so scan the whole
    document and filter to anchors that point at internal paths and have
    short, visible text. The real-locale homepages should yield 4 anchors
    (home logo + apps + support + privacy); stubs missing a menu file fall
    to 2 (just home + apps card link).
    """
    pairs = re.findall(r"<a [^>]*?href=([^\s>]+)[^>]*>([^<]+)</a>", html)
    seen: set[tuple[str, str]] = set()
    out: list[str] = []
    for href, text in pairs:
        href = href.strip("\"'")
        text = text.strip()
        if not text or text in {"↓", "↑"}:
            continue
        if href.startswith("https://github.com") or "mailto:" in href:
            continue
        if not (
            href.startswith("/PeachPitBoat/")
            or href.startswith("https://ccqqder.github.io/PeachPitBoat/")
        ):
            continue
        key = (href, text)
        if key in seen:
            continue
        seen.add(key)
        out.append(text)
    return out


def collect(audit: Audit) -> Audit:
    try:
        audit.html = _fetch(audit.url)
    except Exception as e:
        audit.fetch_error = repr(e)
        return audit
    h = audit.html
    audit.title = _first(r"<title[^>]*>([^<]+)</title>", h)
    audit.description = _first(r'<meta\s+name=["\']?description["\']?\s+content=["\']([^"\']+)["\']', h)
    audit.html_lang = _first(r"<html[^>]*\blang=([\"']?[a-zA-Z\-]+[\"']?)", h).strip("\"'")
    audit.canonical = _first(r'<link\s+rel=["\']?canonical["\']?\s+href=["\']?([^"\'\s>]+)', h)
    # First og:locale wins — that's our explicit xx_YY override
    audit.og_locale = _first(r'<meta\s+property=["\']og:locale["\']\s+content=["\']([^"\']+)["\']', h)
    audit.og_image = _first(r'<meta\s+property=["\']og:image["\']\s+content=["\']([^"\']+)["\']', h)
    audit.nav_anchors = _internal_anchors(h, audit.url.rstrip("/") + "/")
    audit.hreflang_count = len(re.findall(r"rel=alternate hreflang|rel=\"alternate\" hreflang", h))
    if audit.og_image:
        audit.og_image_status = _head_status(audit.og_image)
    return audit


def evaluate(audits: list[Audit]) -> None:
    """Populate `issues` on each audit by cross-comparing locales."""
    base_nav = max((len(a.nav_anchors) for a in audits if not a.fetch_error), default=0)
    for a in audits:
        if a.fetch_error:
            a.issues.append(f"FETCH FAILED: {a.fetch_error}")
            continue

        # 1. Title language matches locale style
        if a.style == "en" and CJK_RE.search(a.title or ""):
            a.issues.append(f"title contains CJK in en-style locale: {a.title!r}")

        # 2. Description language matches locale style
        if a.style == "en" and CJK_RE.search(a.description or ""):
            a.issues.append(f"description contains CJK: {a.description[:60]!r}")

        # 3. Nav parity vs the richest locale
        if base_nav and len(a.nav_anchors) < base_nav:
            a.issues.append(
                f"nav has {len(a.nav_anchors)} items, expected {base_nav} "
                f"(missing menu file?): {a.nav_anchors}"
            )

        # 4. Hreflang completeness — should be 8 langs + x-default = 9
        if a.hreflang_count != 9:
            a.issues.append(f"hreflang count {a.hreflang_count} (expected 9)")

        # 5. <html lang> matches expected
        if a.html_lang.lower() != a.expected_html_lang.lower():
            a.issues.append(f"html lang={a.html_lang!r} (expected {a.expected_html_lang!r})")

        # 6. og:image must be reachable
        if not a.og_image:
            a.issues.append("og:image missing")
        elif a.og_image_status != 200:
            a.issues.append(f"og:image returns HTTP {a.og_image_status}: {a.og_image}")

        # 7. og:locale present and looks like xx_YY
        if not a.og_locale:
            a.issues.append("og:locale missing")
        elif not re.match(r"^[a-z]{2}_[A-Z]{2}$", a.og_locale):
            a.issues.append(f"og:locale not in xx_YY form: {a.og_locale!r}")

        # 8. Canonical sanity: stub homepages should canonical to EN root
        if a.style == "en" and "/PeachPitBoat/" in a.canonical and a.label != "en-root":
            # stub homepages should point at the EN root, not at /xx/
            if not a.canonical.rstrip("/").endswith("/PeachPitBoat"):
                # only enforce on the four stub locales, not the EN root itself
                if a.label in {"fr", "ko", "vi", "id"}:
                    a.issues.append(f"stub homepage canonical={a.canonical} (expected EN root)")


def emit(audits: list[Audit]) -> None:
    use_color = sys.stdout.isatty()
    g, y, r, x = (GREEN, YELLOW, RED, RESET) if use_color else ("", "", "", "")

    def cell(ok: bool, val: str, width: int) -> str:
        mark = f"{g}OK{x}" if ok else f"{r}!!{x}"
        return f"{mark} {val[: width - 3]:<{width - 3}}"

    print()
    print(f"{'locale':10} | {'title':36} | nav | hreflang | og:locale | og:image |")
    print("-" * 90)
    for a in audits:
        if a.fetch_error:
            print(f"{a.label:10} | {r}{a.fetch_error[:80]}{x}")
            continue
        title_disp = a.title[:34]
        title_ok = not (a.style == "en" and CJK_RE.search(a.title or ""))
        title_cell = f"{g if title_ok else r}{title_disp:36}{x}"
        nav_ok = len(a.nav_anchors) >= max(2, len([z for z in audits if not z.fetch_error and len(z.nav_anchors) >= 4]) > 0 and 4 or 2)
        # Recompute against base
        base_nav = max((len(z.nav_anchors) for z in audits if not z.fetch_error), default=0)
        nav_ok = len(a.nav_anchors) >= base_nav
        nav_cell = f"{g if nav_ok else r}{len(a.nav_anchors)}{x}  "
        hreflang_ok = a.hreflang_count == 9
        hf_cell = f"{g if hreflang_ok else r}{a.hreflang_count}{x}      "
        ogl_ok = bool(re.match(r"^[a-z]{2}_[A-Z]{2}$", a.og_locale or ""))
        ogl_cell = f"{g if ogl_ok else r}{a.og_locale or '-':<7}{x}  "
        ogi_ok = a.og_image_status == 200
        ogi_cell = f"{g if ogi_ok else r}{a.og_image_status or 'no':<3}{x}     "
        print(f"{a.label:10} | {title_cell} | {nav_cell} | {hf_cell} | {ogl_cell} | {ogi_cell} |")

    print()
    total_issues = sum(len(a.issues) for a in audits)
    if total_issues == 0:
        print(f"{g}All checks passed across {len(audits)} locales.{x}")
        return
    print(f"{r}{total_issues} issue(s) across {sum(1 for a in audits if a.issues)} locale(s):{x}")
    for a in audits:
        if not a.issues:
            continue
        print(f"\n  [{a.label}]")
        for issue in a.issues:
            print(f"    - {issue}")


def main() -> int:
    # Windows consoles often default to cp950/cp1252; force UTF-8 so CJK in
    # titles renders correctly in the report.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    ap = argparse.ArgumentParser(description="Cross-locale i18n audit")
    ap.add_argument("--base-url", default=DEFAULT_BASE,
                    help=f"Site base URL (default: {DEFAULT_BASE})")
    ap.add_argument("--strict", action="store_true",
                    help="Exit 1 if any locale has issues (for CI)")
    args = ap.parse_args()

    audits = [Audit(label=lbl, url=args.base_url + path,
                    expected_html_lang=hlang, style=style)
              for lbl, path, hlang, style in LOCALES]

    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = {ex.submit(collect, a): a for a in audits}
        for fut in as_completed(futures):
            fut.result()

    evaluate(audits)
    emit(audits)
    if args.strict and any(a.issues for a in audits):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
