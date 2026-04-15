# App Index IA Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 把 `/apps/` 改成真正的 apps index，並把原本的矩陣文章搬到 `/posts/app-matrix/`，同時維持精簡主導航。

**Architecture:** 以 Hugo section list layout 接管 `/apps/`，用 `data/app_url_matrix.yaml` 作為產品卡片來源；原本的 `_index` 敘事內容搬到新的 posts 文章。主導航只保留主要內容類型，`support / privacy` 轉為 footer 級別導覽。

**Tech Stack:** Hugo, Blowfish theme, TOML menus, markdown content, custom section layouts

---

### Task 1: 準備 apps index 所需資料

**Files:**
- Modify: `data/app_url_matrix.yaml`

**Step 1: 為 app matrix 加入分組欄位**

在每個 app 項目加上：
- `line`
- `category`

值使用可穩定的 key，例如：
- `offline-growth`
- `digital-citizen`
- `language-learning`
- `self-reflection`
- `democracy-edc`

**Step 2: 確認資料無重複語義**

避免在 layout 裡用 slug 寫死群組，讓分組資料留在 YAML。

### Task 2: 建立 apps section list layout

**Files:**
- Create: `layouts/apps/list.html`

**Step 1: 建立 hero 與 intro**

渲染：
- section title
- summary / content

**Step 2: 依產品線分組渲染 cards**

每張卡片包含：
- app icon
- title
- summary/tagline
- `查看產品頁`
- `App Store`
- `Support`
- `Privacy`

**Step 3: 加入次級導流區塊**

頁尾提供：
- 前往 `posts/app-matrix`
- 前往 `support`
- 前往 `privacy`

### Task 3: 重寫三語 `apps/_index`

**Files:**
- Modify: `content/apps/_index.md`
- Modify: `content/apps/_index.en.md`
- Modify: `content/apps/_index.ja.md`

**Step 1: 移除矩陣表格內容**

保留 section 導言與 summary，避免 `_index` 再像文章。

**Step 2: 確保標題與命名一致**

建議使用：
- ZH: `Apps`
- EN: `Apps`
- JA: `アプリ`

### Task 4: 搬移 App 矩陣文章到 posts

**Files:**
- Create: `content/posts/app-matrix.md`
- Create: `content/posts/app-matrix.en.md`
- Create: `content/posts/app-matrix.ja.md`

**Step 1: 把舊 `_index` 的矩陣內容搬過去**

保留表格與產品線敘事，並補一段導回 `/apps/` 的說明。

**Step 2: 設定 front matter**

提供：
- `title`
- `date`
- `draft: false`
- `categories`
- `tags`
- `summary`

### Task 5: 更新主導航與 footer

**Files:**
- Modify: `config/_default/menus.zh-tw.toml`
- Modify: `config/_default/menus.en.toml`
- Modify: `config/_default/menus.ja.toml`

**Step 1: 主導航名稱統一**

Header 使用：
- ZH: `Apps`
- EN: `Apps`
- JA: `アプリ`

**Step 2: 新增 footer 導覽**

Footer 至少加入：
- Support
- Privacy

### Task 6: 驗證

**Files:**
- Verify generated output under `public/`

**Step 1: Run build**

Run: `hugo`  
Expected: exit 0

**Step 2: 檢查 apps index**

確認：
- `/apps/` 是 cards index
- 不是舊表格文章

**Step 3: 檢查新文章**

確認：
- `/posts/app-matrix/` 正常生成
- 語言切換正常

**Step 4: 檢查導航**

確認：
- header 仍只有四個主導航按鈕
- footer 有 `support / privacy`
