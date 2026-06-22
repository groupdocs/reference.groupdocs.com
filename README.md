# reference.groupdocs.com

Source for **[reference.groupdocs.com](https://reference.groupdocs.com/)** — the GroupDocs API
reference site. It publishes the class-library API references for 15 GroupDocs products across
.NET, Java, Node.js, and Python (via .NET). The site is built with [Hugo](https://gohugo.io/)
(extended, **0.101.0**), is **English-only**, and deploys to AWS S3 + CloudFront.

## How it's structured

Each product is an **independent Hugo build** that is published under its own path prefix
(`/<product>/`); the prefixes are merged into one bucket at the edge. There is also a separate
**home/site-root** build for the landing page.

```
config/sites/groupdocs/<product>/   # one config tree per product (+ a `home` tree)
  _default/config.toml              # shared settings, English-only, baseURL = "/<product>"
  staging/config.toml               # → reference2.groupdocs.com (QA)   [Stage S3 target]
  production/config.toml            # → reference.groupdocs.com (prod)  [Production S3 target]
content/sites/groupdocs/<product>/
  english/                          # all content (English only)
  static/                           # per-product static assets
themes/docs/                        # vendored Geekdoc-based theme (no submodule)
data/products.toml                  # home page product grid — single source of truth
```

The 15 products: `annotation, assembly, classification, comparison, conversion, editor,
markdown, merger, metadata, parser, redaction, search, signature, viewer, watermark`.

### Content model

- All content is authored as `_index.md` **section bundles** under
  `content/sites/groupdocs/<product>/english/`. Pages carry an explicit `url:` in front matter,
  so permalinks are independent of the theme.
- The bulk of the content (the API reference itself) is **auto-generated** from the per-product
  source repos `GroupDocs.<Product>-References` (GitHub org `groupdocs-<product>`) and synced in.
- Each product's landing page is a **family page**: `layout: family` with structured front
  matter (`platforms`, per-platform `version`/`versionUrl`/`install`, `capabilities`, `formats`,
  `resources`). Rendered by `themes/docs/layouts/_default/family.html`.

### Theme

`themes/docs/` is a vendored, Geekdoc-derived theme. Two deliberate customizations to know about:

- **Scoped left navigation** (`layouts/partials/menu-filetree.html`) renders only the current
  branch of the tree (current page + ancestors + their children) rather than the full ~1,400-page
  tree. This keeps each page small. **Do not revert it to the stock full-tree menu.**
- **Markdown / `llms.txt` outputs** (see below).

## Outputs: HTML + Markdown + llms.txt

Alongside HTML, every page emits a **Markdown (`.md`)** rendition, and each build's home emits
`llms.txt` + `llms-full.txt` (the [llms.txt](https://llmstxt.org/) convention), for AI/LLM
consumption. Configured per product in `config/sites/groupdocs/<product>/_default/config.toml`
(`[outputFormats.MD|LLMSTXT|LLMSFULL]`, `[outputs]`).

The `.md` files are post-processed so they're clean and portable:

1. **No front matter, real Markdown** — `single.md` / `list.md` emit `.RawContent` (Hugo strips
   the YAML front matter), via the partial `layouts/partials/md/abs-content.txt`.
2. **Absolute links** — links are made absolute so they work no matter where the `.md` is served:
   - `abs-content.txt` (in-template) absolutizes **root-relative** links (`/path/` → `BASE/path.md`).
   - [`resolve_md_links.py`](resolve_md_links.py) (post-build) absolutizes **relative** links
     (`../ns/class`, `./x`, of any depth) by resolving each against its page's own URL. It must run
     **before** the ugly-URL rename.
3. **Ugly URLs** — [`move_md_to_ugly_urls.sh`](move_md_to_ugly_urls.sh) renames
   `public/<path>/index.md` → `public/<path>.md`, so `/viewer/net.md` is served (not
   `/viewer/net/index.md`).

The post-build order is always: **build → `resolve_md_links.py` → `move_md_to_ugly_urls.sh`**.

## Local preview

`hugo server` is avoided (a Hugo 0.101 concurrency bug panics on this content); use a static
build + a static file server instead:

```bash
./build-local.sh                      # home + annotation (default)
./build-local.sh viewer signature     # home + the listed products
python -m http.server 1313 --directory public-local --bind 127.0.0.1
```

`build-local.sh` builds the home at `/` plus each product under `/<product>/`, merged into
`./public-local/`, running the resolver + ugly-URL rename per product (mirroring deploy). The
home-only config is `config-local.toml`.

## Deploy & branches

CI is a thin, reusable pipeline:

- `.github/workflows/deploy_product.yml` — reusable build + deploy for one product (Hugo build →
  resolve links → ugly URLs → `hugo deploy` to S3 → CloudFront invalidation).
- `.github/workflows/deploy_<product>.yml` — one thin runner per product (path-filtered triggers).
- `.github/workflows/deploy_all.yml` — orchestrator (matrix over all products; also triggered by
  `themes/**` changes).

Branch → environment mapping:

| Branch       | Environment | Host                          | S3 target    |
| ------------ | ----------- | ----------------------------- | ------------ |
| `main`       | staging     | reference2.groupdocs.com (QA) | `Stage`      |
| `production` | production  | reference.groupdocs.com       | `Production` |

Retired non-English locales are stripped at the edge via `reference.groupdocs.com.redirects.txt`
and `reference2.groupdocs.com.redirects.txt` (nginx `rewrite … permanent;` rules).

## Common tasks

- **Update a product's content** — edit under `content/sites/groupdocs/<product>/english/`
  (or let the `GroupDocs.<Product>-References` sync bring in regenerated API content), push the
  matching branch; the per-product workflow deploys it.
- **Change a family page** (versions, capabilities, etc.) — edit that product's
  `english/_index.md` front matter.
- **Add/adjust the home product grid** — edit `data/products.toml` (drives `{{< products-grid >}}`).

## Repo layout (quick map)

```
config/sites/groupdocs/<product>/   per-product Hugo config (_default/staging/production)
content/sites/groupdocs/<product>/  english/ content + static/ assets
themes/docs/                        vendored theme (layouts, assets/custom.css, partials)
data/products.toml                  home product grid
build-local.sh, config-local.toml   local combined preview
resolve_md_links.py                 post-build: relative .md links → absolute
move_md_to_ugly_urls.sh             post-build: pretty .md → ugly .md
*.redirects.txt                     edge locale-strip redirects
.github/workflows/                  deploy_product.yml (reusable) + per-product runners + deploy_all.yml
```
