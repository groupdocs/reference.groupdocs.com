# Changelog

All notable changes to reference.groupdocs.com are recorded here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/). The site is continuously deployed (no version
tags), so changes accumulate under **[Unreleased]**.

> Maintenance: add an entry here (Added / Changed / Fixed) in the same commit as any notable
> or user-facing change. See `CLAUDE.md` → "Changelog rule".

## [Unreleased]

### Added
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
- Site-root `llms.txt`/`llms-full.txt` and home `index.md` emit **absolute URLs** (host baseURL per env);
  site-root `llms-full.txt` is a directory of per-product `llms-full.txt`.

### Fixed
- Family-page "Browse API reference" links now include the product path prefix.
- Markdown output no longer leaks front matter on empty-body pages (CRLF-tolerant strip).
- `build_search_index.py` handles UTF-8 BOM (python-net files) and non-UTF-8 bytes (`surrogateescape`).
- CloudFront invalidation covers the bucket-root `.md`/`llms`/`404` outputs (no more stale `/index.md`, `/llms.txt`).
- Local preview serves text as UTF-8 (`serve-local.py`) so punctuation no longer renders as mojibake.
