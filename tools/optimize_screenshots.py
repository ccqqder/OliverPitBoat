"""Pre-build optimization for static/images/screenshots/.

Walks every PNG under static/images/screenshots/, writes a WebP sibling next
to it (idempotent: skipped when the WebP is fresher than the PNG), and emits
data/screenshot_dims.json so Hugo can stamp width/height attrs on <img>
elements without having to read the raw image at template time.

The <picture> markup that consumes this lives in
layouts/partials/optimized-img.html, which is invoked from
layouts/partials/app-detail.html for the screenshots section.

Run from the project root: python tools/optimize_screenshots.py
"""
from __future__ import annotations
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
# Both screenshots (large, dominate LCP) and app icons (header on detail
# pages) get the WebP + dimension treatment.
SOURCE_DIRS = [
    ROOT / "static" / "images" / "screenshots",
    ROOT / "static" / "images" / "apps",
]
DIMS_OUT = ROOT / "data" / "screenshot_dims.json"
WEBP_QUALITY = 82

DIMS_OUT.parent.mkdir(exist_ok=True)
dims: dict[str, dict[str, int]] = {}
converted = skipped = 0
total_png_bytes = total_webp_bytes = 0

SUPPORTED = {".png", ".jpg", ".jpeg"}
src_files = sorted(
    p for d in SOURCE_DIRS if d.exists()
    for p in d.rglob("*") if p.suffix.lower() in SUPPORTED
)
for src in src_files:
    rel = src.relative_to(ROOT / "static").as_posix()
    webp = src.with_suffix(".webp")

    if webp.exists() and webp.stat().st_mtime >= src.stat().st_mtime:
        skipped += 1
    else:
        with Image.open(src) as im:
            # JPGs need RGB, PNGs may be RGBA. WEBP handles both, but .convert
            # avoids palette quirks.
            if im.mode not in ("RGB", "RGBA"):
                im = im.convert("RGBA" if "A" in im.mode else "RGB")
            im.save(webp, "WEBP", quality=WEBP_QUALITY, method=6)
        converted += 1

    with Image.open(src) as im:
        dims[rel] = {"w": im.width, "h": im.height}

    total_png_bytes += src.stat().st_size
    total_webp_bytes += webp.stat().st_size

with DIMS_OUT.open("w", encoding="utf-8") as f:
    json.dump(dims, f, indent=2, ensure_ascii=False, sort_keys=True)

mb = lambda n: f"{n / 1024 / 1024:.1f} MB"
saving = total_png_bytes - total_webp_bytes
print(f"Converted: {converted}, Skipped (fresh): {skipped}, Total: {len(dims)}")
print(f"PNG total:  {mb(total_png_bytes)}")
print(f"WebP total: {mb(total_webp_bytes)}")
print(f"Savings:    {mb(saving)} ({saving / total_png_bytes * 100:.0f}%)")
print(f"Wrote dims: {DIMS_OUT.relative_to(ROOT).as_posix()} ({len(dims)} entries)")
