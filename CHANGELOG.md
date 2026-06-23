# Changelog

All notable changes to reference.groupdocs.com are recorded here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/). The site is continuously deployed (no version
tags), so changes accumulate under **[Unreleased]**.

> Maintenance: add an entry here (Added / Changed / Fixed) in the same commit as any notable
> or user-facing change. See `CLAUDE.md` → "Changelog rule".

## [Unreleased]

### Added
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
- Family-page "Browse API reference" links now include the product path prefix.
- Markdown output no longer leaks front matter on empty-body pages (CRLF-tolerant strip).
- `build_search_index.py` handles UTF-8 BOM (python-net files) and non-UTF-8 bytes (`surrogateescape`).
- CloudFront invalidation covers the bucket-root `.md`/`llms`/`404` outputs (no more stale `/index.md`, `/llms.txt`).
- Local preview serves text as UTF-8 (`serve-local.py`) so punctuation no longer renders as mojibake.
- Tightened the gap between home section headings (`gdoc-list-title`) and their subheaders — the
  theme's more-specific `h2.gdoc-list-title { margin-bottom: 4rem }` was overriding the compact override.
