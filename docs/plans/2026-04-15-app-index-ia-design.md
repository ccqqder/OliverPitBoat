# App Index Information Architecture Design

## Goal

把 `/apps/` 從「一篇帶表格的矩陣文章」改成真正的 App section index，同時保留主導航只有四個入口，避免 `support / privacy` 把導航塞爆。

## Current Problems

- `/apps/` 目前是文章式內容，不是產品索引頁，和 section 的角色混在一起。
- 主導航中文仍顯示 `App 矩陣`，但實際目標應該是 apps section，而不是一篇矩陣文章。
- `support / privacy` 已經各自成為獨立 section，但不適合升格進主導航。
- 舊的「App 矩陣」內容仍有價值，適合當成部落格文章保留，而不是繼續佔用 section 首頁。

## Chosen Approach

採用「section 首頁與文章分離」的做法：

- `/apps/` 改成真正的 App 索引頁。
- 原本 `content/apps/_index.*.md` 的矩陣敘事搬到 `content/posts/app-matrix.*.md`。
- 主導航維持 `首頁 / Apps / 部落格 / 關於`。
- `support / privacy` 保持次級頁面，不進主導航，只出現在 app 頁面與 footer。

## `/apps/` Page Design

`/apps/` 會改成一個卡片式 section index，而不是表格文章。頁面結構如下：

1. Hero 簡介  
   短說明站上 app 的共同方向與使用方式。

2. 產品線分組  
   依目前產品結構分成兩組：
   - 離線成長
   - 數位公民

3. App Cards  
   每張卡片直接連到 `/apps/<slug>/`，並顯示：
   - icon
   - 標題
   - tagline / summary
   - App Store 按鈕
   - Support / Privacy 入口

4. 補充導流  
   在頁尾放一段簡短說明，導去：
   - `/posts/app-matrix/`
   - `/support/`
   - `/privacy/`

## Navigation Design

主導航維持 4 個：

- `首頁`
- `Apps`
- `部落格`
- `關於`

Footer 新增次級導覽：

- `支援`
- `隱私政策`

這樣產品訪客可以從主導航快速進入 apps；已安裝使用者與審核情境則可從 footer 與 app 頁面進入 support / privacy。

## Content Migration

原本的矩陣內容不刪除，改搬到 `posts`：

- `content/posts/app-matrix.md`
- `content/posts/app-matrix.en.md`
- `content/posts/app-matrix.ja.md`

這篇文章定位為「產品線導覽與策展說明」，不是 section 首頁。

## URL Strategy

- 保留 `/apps/` 作為 canonical apps index。
- `app-matrix` 改成 `/posts/app-matrix/`。
- 不額外新增主導航按鈕給 `support / privacy`。
- 對於 `https://ccqqder.github.io/posts/` 這種沒有 `/PeachPitBoat/` 的路徑，不做 repo 內 workaround；canonical 仍以 project site 路徑為準。

## Files Expected To Change

- `content/apps/_index.md`
- `content/apps/_index.en.md`
- `content/apps/_index.ja.md`
- `content/posts/app-matrix.md`
- `content/posts/app-matrix.en.md`
- `content/posts/app-matrix.ja.md`
- `config/_default/menus.zh-tw.toml`
- `config/_default/menus.en.toml`
- `config/_default/menus.ja.toml`
- `layouts/apps/list.html` or equivalent apps index layout
- Footer menu config files if needed
- `data/app_url_matrix.yaml` if extra grouping metadata is needed

## Verification

- `hugo` build must succeed.
- `/apps/` 應顯示 cards index，不再是矩陣表格文章。
- `/posts/app-matrix/` 應可正常瀏覽。
- Header 維持 4 個主導航按鈕。
- Footer 應可找到 `support / privacy`。
