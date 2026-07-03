# Changelog

All notable changes to reference.groupdocs.com are recorded here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/). The site is continuously deployed (no version
tags), so changes accumulate under **[Unreleased]**.

> Maintenance: add an entry here (Added / Changed / Fixed) in the same commit as any notable
> or user-facing change. See `CLAUDE.md` → "Changelog rule".

## [Unreleased]

### Added
- **Dark theme (light / dark / auto)** following the docs.groupdocs.com dark redesign. Loads the dark-capable
  `color-groupdocs.css` (was the light-only `color-light-groupdocs.css`) so the header/footer/sidebar, every API
  reference page, and code blocks get full light/dark/auto via the geekdoc color variables; restored the header
  theme toggle (`#gdoc-color-theme`, cycles auto→dark→light, remembered in localStorage; default Auto follows the
  OS). The custom landing pages (home, family, 404, header search) use semantic tokens with dark overrides aligned
  to the docs-dark reference palette (`#282828`/`#3a3a3a` surfaces, `#558fff` accent). The **"For AI agents"**
  callout is now a single shared component (`.gd-ai`) on the home and 404 pages — "Built to be machine-readable"
  with `/llms.txt`, `/llms-full.txt`, and `.md` cards — a dark panel in both themes.
- **Auto-updating SDK versions on the family pages** — version badges (platform cards, the platform sidebar,
  and the "Latest" meta) now read `data/versions.json`, refreshed from the canonical
  `products.groupdocs.com/versions.json` feed by a scheduled workflow (`update_versions.yml`, 06:10 + 18:10 UTC,
  +10 min after upstream publishes). The job commits the data file to both branches and redeploys the product
  family pages only when a version actually changed; the family template falls back to each page's front-matter
  version when the feed has no entry, and the version badge links to the platform's release notes.
  `update_versions.py` trims the feed to the rendered fields; `deploy_product.yml` gained a `ref` input so the
  scheduled job can build the updated branch HEAD.
- **Branded link previews (Open Graph / Twitter Card images)** — shared links (Teams, Slack, LinkedIn, Discord,
  etc.) now show a GroupDocs image instead of a generic placeholder: the GroupDocs symbol on the site root/home
  and the product's own icon on each product build. `og:image` was previously empty (the `utils/featured`
  resolver fell back to `Site.Params.images`, which was unset because the config key sits under `[params.meta]`);
  the resolver now derives the image from the build (product key = first path segment of the URL). The card uses
  the compact `summary` Twitter Card (small icon thumbnail beside the text) rather than `summary_large_image`, and
  the icons are crisp **512×512** PNGs (rasterized from the brand product SVGs onto a white square) with
  `og:image:width`/`height`/`type`/`alt` declared. Icons live in theme static at `/img/og/`.
- **Verified getting-started code** on the family pages — the "Getting started" tabs now render real
  snippets from `data/getting_started.yaml` (keyed product → platform), sourced from the official
  products content and **compile-verified against the real SDKs** by runnable apps under
  `examples/getting-started/<product>/<platform>/` (`dotnet build` / `mvn compile` / import-resolve).
  Coverage: **.NET ×15, Java ×13, Python ×13, Node.js ×6** (conversion & viewer compile-run via a
  prebuilt node-java; signature, merger, metadata & editor ship snippets **derived from the verified
  Java**, since node-java's native build is blocked on Node 22 here); products/platforms without an
  entry fall back to the install command. Verification corrected several drifted official snippets (metadata
  `Sanitize()`, signature/Python namespaces+casing, parser/Python `get_text()`, watermark line-breaks)
  and flagged that `groupdocs-annotation-net` on PyPI is a 0.0.0 stub.
- **Combined, compacted `llms-full.txt`** at the site root — the entire API reference for all 15
  products in one well-structured file. Built from source by `build_llms_full.py` (navigation
  boilerplate stripped: `See Also` footers, `Learn more` blocks, internal link URLs, front matter,
  heading anchors, Java separators; signatures, summaries, and member/parameter tables kept).
  ~28 MB (~3 MB gzipped). Deployed to the bucket root by `deploy_all` + the content-push refresher.
- **Live search on the 404 page** — type-ahead over a combined `/search-index.json` (all 15 products,
  ~37k symbols): kind badges, namespace paths, platform pills, keyboard navigation.
- **Cross-product search index** `/search-index.json`, built from product source front matter by
  `build_search_index.py --source` (no Hugo build). Produced by `deploy_all` and refreshed on any
  content push by the new lightweight `refresh_search_index.yml`.
- **Redesigned 404 page** — hero, product directory (from `data/products.toml`), and an AI/LLM callout,
  using the site's design tokens.
- **Per-page Markdown output** with absolute links and ugly URLs; **`llms.txt` / `llms-full.txt`** for
  AI/agent consumption; product family pages served at **`/<product>.md`** (bucket root).
- `resolve_md_links.py`, `build_search_index.py`, `build-local.sh`, `serve-local.py`, `config-local.toml`
  tooling for building/serving the site and its Markdown/search outputs locally.
- Comprehensive README, `CLAUDE.md`, and this changelog.

### Changed
- **Relocated the repo-root helper scripts into `scripts/`** (`resolve_md_links.py`, `move_md_to_ugly_urls.sh`,
  `build_search_index.py`, `build_llms_full.py`, `update_versions.py`, `serve-local.py`, `build_refs.cmd`;
  `build-local.sh` and `config-local.toml` stay in the repo root) and **updated every caller** — the CI
  workflows (`deploy_product.yml`, `deploy_all.yml`, `refresh_search_index.yml`, `update_versions.yml`) and
  `build-local.sh` — to invoke them from `scripts/`. Fixes the scheduled **Update versions** job (and the
  deploy/aggregate workflows), which had been failing with `can't open file 'update_versions.py'` after the move.
- **Migrated the docs.groupdocs.com header & footer** to be **server-rendered** (`partials/site-header.html`
  + `site-footer.html`, wired in `_default/baseof.html`), replacing the runtime Containerize menu engine
  (`foot.html` no longer loads `containerize-menu`). The header **search box uses this site's own
  `/search-index.json` live search** (new `partials/header-search.html`, the same engine as the home page),
  not the docs AI search. Removed the non-functional dark/light theme toggle (the site is light-only) and
  the Dynabic login placeholder; dropped the `wrapper-space-top` offset (the header is now in-flow).
- **Redesigned the product family/landing pages** (Claude Design handoff): full-width two-column layout
  (platform-variant sidebar + main), breadcrumb, a lead auto-extended with "…a single, consistent API
  across &lt;platforms&gt;", a meta row (platforms · formats · **latest = the highest** version across
  platforms), a **scoped per-product live search** (filters `/search-index.json` to the current product;
  Search button consistent with the home/404 search), selectable **platform cards** — with a "Selected"
  tag — that drive a **"Getting started" code block** (heading names the selected platform; the language
  switch is a platform-dot segmented control matching the home "Browse products" filter; per-platform code
  from `data/getting_started.yaml`, falling back to the install command), a
  curated, **verified** **"Popular classes & namespaces"** grid (real symbols across all 15 products,
  each link checked against the reference tree), **Key capabilities** + **Supported formats** (with an
  optional "…and N+ more" note), **Resources** as bordered cards, and an inline **"Was this page helpful?"**
  card — all restyled to the home/404 design system. Rendered by `_default/family.html`. New family
  front-matter fields `formatsCount`, `formatsNote`, and `popular[]` (`name`/`kind`/`ns`/`url`),
  populated for **all 15 products** (format counts sourced from the products.groupdocs.com overviews;
  Popular symbols verified against the reference tree).
- **Redesigned the home/landing page** (from the Claude Design handoff, the sibling of the 404):
  a hero **live search** over `/search-index.json` (same engine as the 404), a **platform-filter**
  segmented control (All / .NET / Java / Node.js / Python) over the product grid (cards show the real
  product icon, description, and platform pills), a dark **AI/LLM panel** (`/llms.txt`,
  `/llms-full.txt`, `.md`), and **Developer Resources** cards. Rendered by
  `_default/full-width.html` as a scoped `gd-home` design; the `_index.md` body is now empty (the
  layout renders everything from `data/products.toml`), so the `products-grid` shortcode is unused.
- **English-only**: removed all non-English content/locales; edge redirects strip retired locale segments.
- Migrated to the vendored Geekdoc-based `themes/docs/` theme (dropped the api-theme submodule); added a
  **scoped left-nav** (`menu-filetree.html`) to keep page weight low.
- Reworked CI into reusable workflows (`deploy_product.yml` + per-product runners + `deploy_all.yml` +
  `deploy_home.yml`), Hugo 0.101.0, AWS S3 + CloudFront.
- Home page: product grid driven by `data/products.toml`; **AI Agents & LLM section** refocused on this
  site's machine-readable indexes (`/llms.txt`, `/llms-full.txt`, `.md`) with clearer FontAwesome icons.
- Site-root `llms.txt`/`llms-full.txt` and home `index.md` emit **absolute URLs** (host baseURL per env).
- **All page links in `llms.txt` / `llms-full.txt` now point to the Markdown (`.md`) rendition, not the
  HTML page** — these files are for LLMs/agents (e.g. `…/annotator/text/` → `…/annotator/text.md`).
  Applies to the combined `/llms-full.txt` (`Path:` lines) and the per-product Hugo `llms.txt`/`llms-full.txt`.
- **Site-root `llms.txt` is now a per-product directory** (full-reference / section-index / Markdown
  links per product, plus a pointer to the combined `/llms-full.txt`) — the format previously used by
  `llms-full.txt`. The home build no longer emits `llms-full.txt`; the source-built combined file owns
  `/llms-full.txt`. `refresh_search_index.yml` (now "Refresh Root Aggregates") rebuilds both
  `/search-index.json` and `/llms-full.txt` on content pushes.

### Fixed
- **Mobile layout fixes** — (1) only one hamburger on doc pages (removed the duplicate in the breadcrumb/page
  header; the sidebar-nav toggle lives in the site header); (2) the "On this page" mobile TOC toggle now works on
  flat/sparse pages (the nav id is renamed to `#TableOfContentsMobile` unconditionally) and the box is hidden
  unless there are ≥2 entries; (3) family/404 no longer show a dead hamburger that opened an empty drawer (the
  site header now mirrors baseof's nav-disabled condition); (4) the home/family/404 brand/logo no longer looks
  off-place (the empty nav-control placeholder reserves the hamburger's width); (5) the Node.js platform card now
  shows an install command (`npm install @groupdocs/groupdocs.<product>`, derived in the family template).
- Header search now opens and matches the docs look. Two fixes: (1) the `#search_toggle` magnifier had no
  click handler because the header-search script ran during parse, before the toggle button (rendered later
  in `site-header.html`) existed — deferred the partial's init to `DOMContentLoaded`; (2) the reveal was a
  full-width white overlay that hid the brand/logo — changed it to the docs' inline reveal (a bounded search
  box between the brand and the right edge; the brand stays, the nav menu + magnifier hide, brand hides only
  on mobile), driven by `.is-searching` on `.gdoc-header__content`.
- Pointed leftover `groupdocs.net` references at `groupdocs.com` (cookie-consent domain + privacy-policy
  URL, structured-data sales email, and the feedback API endpoint), and removed the unused legacy menu
  assets under `static/menu/` left over from the old menu loader.
- Restored the global GroupDocs top menu — load the modern Containerize menu engine
  (`menucdn.containerize.com/core/engine.min.js`, venture `groupdocs-<lang>`), the same loader
  products.groupdocs.com uses, replacing the deprecated `menu.containerize.com/api/get-menu` loader
  that broke when the site moved to the docs theme.
- Family-page "Browse API reference" links now include the product path prefix.
- Markdown output no longer leaks front matter on empty-body pages (CRLF-tolerant strip).
- `build_search_index.py` handles UTF-8 BOM (python-net files) and non-UTF-8 bytes (`surrogateescape`).
- CloudFront invalidation covers the bucket-root `.md`/`llms`/`404` outputs (no more stale `/index.md`, `/llms.txt`).
- Local preview serves text as UTF-8 (`serve-local.py`) so punctuation no longer renders as mojibake.
- Tightened the gap between home section headings (`gdoc-list-title`) and their subheaders — the
  theme's more-specific `h2.gdoc-list-title { margin-bottom: 4rem }` was overriding the compact override.
