# feature/art-assets — WIP Tasks

**Last updated:** 2026-04-18 (resumed + Gantt Planet i18n screenshots captured)
**Branch:** `feature/art-assets`
**Worktree:** `.worktrees/feature-art-assets/`

## Resume checklist

```bash
cd /Volumes/Data/Service/PeachPitBoat/.worktrees/feature-art-assets
git status
hugo --minify --baseURL "http://localhost:8765/"
cd public && python3 -m http.server 8765
# Open http://localhost:8765/
```

## Work done on this branch (uncommitted)

- [x] Site icon: `author.gif` → `author.png` + dynamic favicons partial.
- [x] Author card washi-paper background (`layouts/partials/author.html`).
- [x] TOC letterpress-paper background (`layouts/partials/toc.html`).
- [x] 32 background textures copied to `assets/images/backgrounds/`.
- [x] Scoped custom fonts (article title + body + code only, nav left default).
- [x] Gantt Planet i18n screenshots captured from Simulator (iPhone 17, iOS 26.1):
      - `static/images/gantt-planet-chart-en.png` (EN filled timeline)
      - `static/images/gantt-planet-chart-ja.png` (JA filled timeline)
      - `static/images/gantt-planet-3d-en.png`   (EN 3D planet)
      - `static/images/gantt-planet-3d-ja.png`   (JA 3D planet)
- [x] Rewrote `gantt-planet-intro.en.md` + `.ja.md` image paths to `-en/-ja` variants.
- [x] `.worktrees/` added to `.gitignore` (already committed to main as `84028f4`).

## How the Gantt Planet screenshots were captured (for future re-capture)

1. `xcrun simctl boot 7FEFA1E9-5C52-4D64-BD8C-279591849706` (iPhone 17)
2. `xcrun simctl install <udid> ~/Library/Developer/Xcode/DerivedData/life-harmony-ios-*/Build/Products/Debug-iphonesimulator/life-harmony-ios.app`
3. `xcrun simctl status_bar <udid> override --time "9:41" --batteryState charged --batteryLevel 100 --wifiBars 3 --cellularBars 4 --cellularMode active`
4. `xcrun simctl launch <udid> com.qqder339.life-harmony -AppleLanguages '(en)' -AppleLocale en_US` (swap `en`/`en_US` for `ja`/`ja_JP`)
5. On first-launch "Load Sample Items" dialog → tap **Load** (seeds 15 items incl. Reading/Exercise/TidyRoom/FamilyDinner/FinanceReview/AnnualCheckup).
6. Tap the ⌃ chevron next to "Lv.1" to collapse the user card → reveals full filled timeline.
7. `xcrun simctl io <udid> screenshot <path>` → capture chart view.
8. Tap **Geo View** tab (middle of bottom nav) → wait ~3s for 3D planet to render.
9. `xcrun simctl io <udid> screenshot <path>` → capture 3D view.
10. For JA: `xcrun simctl uninstall` + reinstall + relaunch with `-AppleLanguages '(ja)'`, repeat.

Clicks via `cliclick` (Homebrew). Simulator window bounds obtained via AppleScript.

## Pending (next session)

### 1. Decide on `gantt-planet-cover.jpg` (lowest priority)

English-text cover illustration used for all three languages. Not UI, but not ideal for ja/zh either. Options:
- Accept as-is (conceptual illustration, not UI text)
- Regenerate in each language (image model)
- Remove text entirely

### 2. Optional cleanup before merge

- LXGWWenKaiTC is 12MB, TaipeiSansTCBeta ~20MB each — consider subsetting or woff2 conversion before shipping.
- `git rm` the old `assets/img/author.gif` once PNG swap is verified in production build.
- `static/images/gantt-planet-chart.png` and `gantt-planet-3d.png` (Chinese originals) are still used by `gantt-planet-intro.md` (zh-tw) — keep them.

## DigitalAssets app screenshot inventory (reference for future blog posts)

Only Gantt Planet is currently blog-referenced. Inventory for when other apps get articles:

| App | Source path | i18n screenshot coverage |
|-----|-------------|--------------------------|
| atomic-presence | `TOOL/AtomicPresence` | ❌ no PNGs (`docs/screenshots/` has 1 JSON only) |
| kana-juku | `LANG/kana_proto` | ✅ zh + en + ja (`appstore_screen_*` + `screenshots/ja`) |
| gantt-planet | `TOOL/life-harmony-ios` | ⚠️ only EN slides in repo; fresh captures now in blog |
| auditory-companion | `TOOL/FamiliarNoise` | ⚠️ EN + JA, missing zh |
| stone-story | `Service/StoneStory` | ✅ multilingual (chinese/en/ja/zh-tw subdirs) |
| meme-lives | `TOOL/MemeLives` | ❌ no screenshot folder |
| english-plus-one | `LANG/E1nglish` | ✅ zh + en + ja |
| python-dimensions | `LANG/PythonDimensions` | ⚠️ only JA |

Recapture workflow for any app without multi-language coverage: run `/i18n-guide` + `/l10n-check` on the app's source repo to identify Localizable.xcstrings coverage, then use the Simulator + cliclick pattern documented above.

## When all above done — merge plan

```bash
cd /Volumes/Data/Service/PeachPitBoat
git checkout main
git merge feature/art-assets --no-ff
git worktree remove .worktrees/feature-art-assets
git branch -d feature/art-assets
```
