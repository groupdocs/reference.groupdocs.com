# Changelog

All notable changes to reference.groupdocs.com are recorded here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/). The site is continuously deployed (no version
tags), so changes accumulate under **[Unreleased]**.

> Maintenance: add an entry here (Added / Changed / Fixed) in the same commit as any notable
> or user-facing change. See `CLAUDE.md` → "Changelog rule".

## [Unreleased]

### Added
- **Broken-link redirects (API URL-scheme migration)** — restored 301s for **1,456** legacy API URLs that
  began 404-ing after the June-2026 "Simplify CI" change (`855972156b`) stripped the redirect config down
  to locale-only. The 404s are old URL schemes for pages that still exist at the canonical
  `/{product}/{platform}/{namespace}/{class}/`: platform-less `/{product}/{namespace}/{class}` (insert
  `net`/`java`) and flat `/{product}/net/{class}` (insert the namespace). New **`redirects/redirects.map`**
  is generated from the 404 crawl + content tree by **`scripts/gen_redirects_map.py`** (every target
  verified: 1,440 resolve to the exact page, 16 reorg stragglers fall back to their namespace landing;
  `redirects/known_extra_404s.tsv` adds 3 uncrawled URLs) and published as **S3 per-object redirects**
  (`x-amz-website-redirect-location` → 301, served via the bucket's static-website endpoint through
  CloudFront) by **`scripts/deploy_redirects.sh`** via the manual **`deploy_redirects.yml`** workflow
  (two objects per URL, then invalidates the affected CloudFront product prefixes). The old
  `redirects/*.redirects.txt` nginx files are VM-era leftovers, not consumed by the S3+CloudFront stack.
- A content-link audit (all 37,609 API pages) found the generators produce correct paths — `url:` front
  matter is 100% consistent and class/member tables use proper links. The only defect is **3 .NET
  namespace pages** (metadata, parser, comparison) whose intro prose carries an upstream **xmldocmd**
  `see cref` that resolves one level too deep (doubled namespace → 404). All 3 are now 301'd via
  `redirects/known_extra_404s.tsv` (fed to the generator with `--extra`); the durable fix belongs upstream
  in the `GroupDocs.<Product>-References` sources (xmldocmd namespace-summary links, or a post-sync sanitize).
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
- **Reorganized repo-root scripts into `scripts/` and edge-redirect files into `redirects/`.** All
  build/deploy/preview helpers now live in `scripts/` (`resolve_md_links.py`, `move_md_to_ugly_urls.sh`,
  `build_search_index.py`, `build_llms_full.py`, `update_versions.py`, `serve-local.py`, `build_refs.cmd`);
  `build-local.sh` and `config-local.toml` stay in the repo root. The two nginx locale-strip redirect files
  moved to `redirects/reference.groupdocs.com.redirects.txt` / `redirects/reference2.groupdocs.com.redirects.txt`.
  Updated every caller — the CI workflows (`deploy_product.yml`, `deploy_all.yml`, `refresh_search_index.yml`,
  `update_versions.yml`), `build-local.sh`, the per-product `config.toml` deploy comments, and the docs
  (README, CLAUDE.md, RESUME.md). ⚠️ If the edge layer pulls the redirect files by their old repo-root path,
  update that reference to `redirects/`.
- **Home hero search is now a product filter** (matches docs.groupdocs.com). The index-page search box
  live-filters the "Browse products" grid on the page (by short name / title / description, combined with the
  platform segments) instead of running a full `/search-index.json` type-ahead that navigated away — added a
  clear (×) button and a "no products match" empty state, and it drops the results dropdown. The full-reference
  search is unchanged and still lives in the header (`partials/header-search.html`), which keeps reusing the
  `.gd-home__result*` row styles.
- **Removed "REST API" from the site descriptions** — this site is class-library reference only. The home
  hero lead / meta description is now "Class library reference for GroupDocs document-processing SDKs…"
  (`home/english/_index.md` + the `/llms-full.txt` header in `build_llms_full.py`), and the fallback
  `[params] description` in all 16 `config/sites/groupdocs/<product>/_default/config.toml` files (the default
  `<meta>`/OG description on the API-reference pages) now reads "Class Libraries for the developers to
  manipulate & process Files…" (was "Class Libraries & REST APIs for the developers…").
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
- **Stacked install code blocks → platform tabs** on the Watermark Python-via-.NET *Installation* guide
  (`watermark/python-net/guides/installation/`). The PyPI install, pre-downloaded-wheel install, and Linux/macOS
  prerequisites were each authored as consecutive fenced code blocks that rendered as separate boxes stacked one
  under another; they are now grouped into the theme's `tabs`/`tab` shortcode platform tabs
  (Windows / Linux / macOS — the wheel block adds macOS Intel + Apple Silicon). Same shortcode + `.gdoc-tabs`
  styling already vendored from the docs `hugo-geekdoc` theme; no theme changes. (Canonical fix also landed in the
  `GroupDocs.Watermark-References` product source so the content sync won't revert it.)
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
