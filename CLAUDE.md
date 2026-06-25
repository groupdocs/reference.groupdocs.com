# CLAUDE.md — reference.groupdocs.com

Working guide for this repo (the Hugo source for **reference.groupdocs.com**, the GroupDocs API
reference site). Read this first; it captures the architecture and the conventions that aren't
obvious from the code.

## What this is
- API references for **15 products** across **.NET, Java, Node.js, Python (via .NET)**. English-only.
- Hugo **extended 0.101.0**. Deploys to **AWS S3 + CloudFront**.
- Products: `annotation, assembly, classification, comparison, conversion, editor, markdown,
  merger, metadata, parser, redaction, search, signature, viewer, watermark` (+ a `home` site-root build).

## Architecture (important)
- **Each product is its own Hugo build** under `config/sites/groupdocs/<product>/`, published under a
  path prefix `/<product>/`. A separate **`home` build** publishes the landing page to the **bucket root**.
  There is no single build that sees all products.
- Per-product build: `hugo --configDir config/sites/groupdocs/<product> --environment <staging|production> --minify`.
- **baseURL**: production product config sets the full host (`https://reference.groupdocs.com/<product>`);
  staging inherits `_default` (`/<product>`, root-relative). Home build sets the host per env
  (`production` → `https://reference.groupdocs.com/`, `staging` → `https://reference2.groupdocs.com/`),
  deploys to the **bucket root** with `--maxDeletes 0`.

## Branches & deploy
- **`main` → staging/QA → reference2.groupdocs.com** · **`production` → prod → reference.groupdocs.com**.
- Workflows (`.github/workflows/`):
  - `deploy_product.yml` — reusable build+deploy for one product (inputs: `product_family`, `environment`,
    `invalidate_paths`, `max_deletes`). Post-build order: **build → `resolve_md_links.py` →
    `move_md_to_ugly_urls.sh` → (non-home) copy `public/index.md` to bucket-root `/<product>.md` + `rm public/index.md`
    → `hugo deploy` → CloudFront invalidate**.
  - `deploy_<product>.yml` (×15) — triggers on `content/sites/groupdocs/<product>/**` push; calls the reusable one.
  - `deploy_home.yml` — `content/sites/groupdocs/home/**`; invalidates `/index.html /index.md /llms.txt /llms-full.txt /404.html`; `maxDeletes 0`.
  - `deploy_all.yml` — `themes/**` push or manual; home → products matrix → **aggregates** job (`search-index`)
    that rebuilds the bucket-root `/search-index.json` **and** `/llms-full.txt` from source.
  - `refresh_search_index.yml` ("Refresh Root Aggregates") — `content/sites/groupdocs/**` push or manual;
    rebuilds `/search-index.json` **and** `/llms-full.txt` from source (lightweight, no Hugo), concurrency-coalesced.
- Secrets: `ACCESS_KEY`/`SECRET_ACCESS` (S3), `AWS_DISTRIBUTION_PROD` (prod) / `AWS_DISTRIBUTION` (staging) CloudFront.

## Content model
- All content lives under `content/sites/groupdocs/<product>/english/` as **`_index.md` section bundles**,
  each with an explicit **`url:`** in front matter (product-relative, e.g. `/net/...`). Mostly auto-generated
  API refs synced from `GroupDocs.<Product>-References` repos.
- **Family/landing page** (per product): `content/sites/groupdocs/<product>/english/_index.md`, `layout: family`,
  `url: /`. HTML by `themes/docs/layouts/_default/family.html` (the **`gd-family`** design: breadcrumb + meta,
  a **scoped per-product search** over `/search-index.json` filtered by the URL's product segment, selectable
  **platform cards** that drive a tabbed **Getting-started code block**, capabilities/formats, resources,
  feedback). The Getting-started code comes from **`data/getting_started.yaml`** (keyed product → platform →
  `{lang, code}`), **compile-verified** by runnable apps in **`examples/getting-started/<product>/<platform>/`**
  (`dotnet build` / `mvn compile` / Python import-resolve); a platform with no entry falls back to its
  `install` command. Snippets are sourced from `products/content/<product>/<platform>/_index.en.md`. Markdown
  by `themes/docs/layouts/index.md` (family branch). The page also shows a curated **"Popular classes &
  namespaces"** grid, and the "Latest" in the meta row is the **highest** version across platforms (not
  the first listed). Family front matter: `lead`, `platforms[]` (`name`, `key`, `ref`, `version`,
  `versionUrl`, `install`), `capabilities[]`, `formats[]`, `formatsCount` (display string e.g. `"170+"`),
  `formatsNote` (muted line under the format chips), `popular[]` (`name`/`kind`/`ns`/`url` — cards link
  into the reference), `resources[]`.
- **Site-root landing**: `content/sites/groupdocs/home/english/_index.md`, `layout: full-width`. Its
  **body is empty** — the whole page is rendered by `themes/docs/layouts/_default/full-width.html` as the
  scoped **`gd-home`** design (hero + live search over `/search-index.json`, a platform-filter over the
  product grid, a dark AI/LLM panel, developer resources), all driven by `data/products.toml`. The hero
  title/lead come from the front-matter `title`/`description`. (The `.md`/`llms.txt` home outputs still
  come from `layouts/index.md` / `index.llmstxt.txt`, which read `data/products.toml`, not the body.)
  The old `shortcodes/products-grid.html` is now unused.
- **`data/products.toml`** — single source of truth for the home product grid (`{{< products-grid >}}` shortcode)
  AND the 404 product directory. 15 entries (key/title/url/icon/weight/description/platforms).
- ⚠️ **python-net content files have a UTF-8 BOM** — parse with `utf-8-sig` (otherwise the `---` front-matter
  delimiter check fails). Many files use CRLF — keep parsing/regex CRLF-tolerant.

## Theme (`themes/docs/`, vendored Geekdoc — not a submodule)
- `_default/baseof.html`: sidebar nav disabled for `.Kind == "404"` (404 renders full-width/centered).
- **Header & footer** are **server-rendered** in `baseof.html` from `partials/site-header.html` +
  `partials/site-footer.html` (migrated from docs.groupdocs.com). This **replaced the runtime Containerize
  menu engine** — `partials/foot.html` no longer loads `partials/containerize-menu.html` (left in place,
  unused). The header **search uses this site's own `/search-index.json`** via `partials/header-search.html`
  (same engine as the home `gd-home` search), revealed by the `#search_toggle` button; the docs AI search
  (`search-input.html`) is unused for the header. Site is light-only (no theme toggle). The `.gdoc-*`
  header/footer CSS is loaded by `head/others` (`main-groupdocs.css` etc.).
- `partials/menu-filetree.html`: **scoped** nav (current branch only) for page weight — **do not revert to the full tree**.
- `assets/custom.css`: fingerprinted (loaded via `head/others`). Holds `gd-family*`, `gd-platform*`, `gd-404*` styles.
  Gotcha: theme has `.gdoc-page h2 { line-height/margin-top: 2.5rem }` and global `h1..h6 { display:flex }` —
  scope custom headings with higher specificity (e.g. `.gd-404 .gd-404__h2`) to override.

## Outputs: HTML + per-page Markdown + llms.txt + search index
- Every page also emits **Markdown (`.md`)**; home emits `llms.txt` + `llms-full.txt`.
- `.md` is: **no front matter** (raw content via `_default/single.md`/`list.md`/`index.md` → `partials/md/abs-content.txt`),
  **absolute links**, **ugly URLs**. Family page `.md` is served at **`/<product>.md`** (bucket root), not `/<product>/index.md`.
- `partials/md/abs-content.txt`: emits `.RawContent`, absolutizes root-relative links, strips a leading
  front-matter block for empty-body pages (CRLF-tolerant).
- llms (per-build, Hugo): `index.llmstxt.txt` — **site-root** `llms.txt` is a per-product **directory**
  (full-reference / section-index / Markdown links per product, from `data/products.toml`); a product
  build's `llms.txt` lists its platforms/namespaces. `index.llmsfull.txt` — a **product** build inlines
  all its pages into `/<product>/llms-full.txt`. The **site-root** build no longer emits `llms-full.txt`.
- **Combined `/llms-full.txt`** (bucket root): the entire reference for all 15 products in one compacted,
  well-structured file, built from source by `build_llms_full.py` (no Hugo — each product is a separate
  build, so Hugo can't aggregate). It strips nav boilerplate (`See Also`, `Learn more`, internal link
  URLs, front matter, anchors, Java separators) and keeps signatures + summaries + member/parameter
  tables. Produced & deployed by the `deploy_all` aggregates job and `refresh_search_index.yml`.
- **Search index** `/search-index.json` (bucket root, ~37k entries, all products) powers the **404 live search**.
  Built by `build_search_index.py --source content/sites/groupdocs` (parses front matter `title`+`url`, no Hugo).
- Serving: `.md`/`.txt`/`.html` get `charset=utf-8` via `[[deployment.matchers]]`; CloudFront auto-gzips.

## Scripts (repo root)
- `move_md_to_ugly_urls.sh [dir]` — `public/<path>/index.md` → `public/<path>.md` (`-mindepth 2`, skips build-root index.md).
- `resolve_md_links.py <dir> --base-url <BASE>` — resolve relative `.md` links to absolute (per page URL);
  `surrogateescape` for non-UTF-8 bytes. Must run **before** the ugly-URL rename.
- `build_search_index.py --source content/sites/groupdocs --out search-index.json` — combined index (source mode).
- `build_llms_full.py --source content/sites/groupdocs --base-url <BASE> --out llms-full.txt` — combined,
  compacted whole-reference file (source mode; `--only a,b` limits products for fast local preview).
- `build-local.sh [products…]` — builds home + listed products into `./public-local/` (runs resolver + ugly rename +
  family-md-to-root + search index). Default product: annotation.
- `serve-local.py [port]` — static server for `./public-local` that sends `charset=utf-8` for text (plain
  `python -m http.server` omits it → `—`/`→` render as mojibake). **Use this for local preview**, default port 1313.
- `config-local.toml` — home-only local config used by `build-local.sh`.

## Local preview
`hugo server` panics on this content (Hugo 0.101 concurrency bug). Instead:
```
./build-local.sh annotation conversion   # build home + listed products
python serve-local.py 1313               # serve ./public-local with UTF-8
```
404 lives at `/404.html`; the search box only covers the products you built locally.

## The 404 page
- `layouts/404.html` (`define "main"`, `.gd-404`): hero + **live type-ahead search** over `/search-index.json`
  + product directory (from `data/products.toml`) + AI/LLM callout. Links are root-relative absolute paths
  (resolve at the domain root regardless of which build's `/404.html` is served). Served via CloudFront error doc.

## Commit & branch conventions (follow exactly)
- Author is the system default **Vladimir Litvinchik <vladimir.litvinchik@aspose.com>**.
- **No `Co-Authored-By` trailer and no "Claude"/AI mention in commit messages.**
- Keep `main` and `production` identical: commit on `production`, then `git branch -f main production`.
  Push both (fetch first; both are normally fast-forwards — the remote can drift via automated content syncs,
  so verify with `merge-base --is-ancestor` before pushing).
- The product-source repos (`../GroupDocs.<X>-References`) and the design handoff (`../references-404`) are
  **separate from this repo** — the user commits those.

## Verified getting-started snippets
- The family pages' Getting-started code comes from **`data/getting_started.yaml`** (keyed product →
  platform → `{lang, code}`), **compile-verified** against the real SDKs by the runnable apps in
  **`examples/getting-started/<product>/<platform>/`** (`dotnet build` / `mvn compile` / Python
  import-resolve). A product/platform with no entry falls back to its install command. (The broader
  product/SDK knowledge base that informed these snippets is maintained **outside this repo**.)

## Changelog rule
**Whenever you make a notable/user-facing change here, add an entry to `CHANGELOG.md` under `## [Unreleased]`
(Keep a Changelog format: Added / Changed / Fixed) in the same commit.** Skip purely local/throwaway changes.

## Known gotchas / open items
- Git shows `LF will be replaced by CRLF` warnings on Windows — harmless.
- `/search-index.json` is produced only by `deploy_all` + `refresh_search_index` (source-based; no per-product artifacts).
- Per-product `llms-full.txt` dev-guide links can double the product segment (`/annotation/annotation/...`) —
  pre-existing source-link bug, not yet fixed.
- `__pycache__/` from running the Python scripts is not in `.gitignore`.
- `docs.groupdocs.com` (a separate repo) has its own llms.txt readability + charset/mojibake issues — deferred by the user.
