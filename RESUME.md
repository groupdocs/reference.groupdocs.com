# RESUME — work-in-progress handoff (reference.groupdocs.com)

Snapshot for continuing after a context reset. Repo: `reference.groupdocs.com` (Hugo API-ref site,
15 products). Branch model: `production`→prod, `main`→staging; keep them identical (commit on
production, then `git branch -f main production`, push both). Commits: author = system default
**Vladimir Litvinchik <vladimir.litvinchik@aspose.com>**, **NO Co-Authored-By / no "Claude" mention**.

## Already committed + pushed (both branches)
- `ad12ed961b` — site-root `llms.txt` (product directory) + combined compacted `/llms-full.txt`.
- `17f79ce809` — home page redesign (`gd-home`) + shared hero gradient. ← current remote HEAD.

## UNCOMMITTED work this session (large; sitting on top of 17f79ce809) — NOT committed yet
The user has been reviewing locally; next step is either polish deltas or **commit it all**.

1. **Family page redesign (`gd-family`)** — matches the updated mockup `../references-family`:
   - `themes/docs/layouts/_default/family.html` — full rewrite: **full-width** two-column =
     platform-variant sidebar (`gd-family__side`: .NET/Java/Node/Python, dot+version, clickable,
     synced) + `gd-family__main` (breadcrumb, title, lead, meta row w/ green dot, scoped search,
     "Choose your platform" cards, **terminal-style dark code block** w/ macOS dots + language tabs +
     copy, capabilities/formats, resources, feedback). Inline JS: copy buttons, platform-sync
     (cards+tabs+variants via `select()`), scoped `/search-index.json` search filtered by product.
   - `themes/docs/layouts/_default/baseof.html` — added `{{ if eq .Layout "family" }}{{ $navEnabled = false }}{{ end }}`
     (family is full-width, no theme sidebar — like 404/home).
   - `themes/docs/assets/custom.css` — `.gd-family` grid + variant sidebar + terminal dots + meta
     green dot, alongside the earlier `.gd-home*` and `.gd-404*` blocks.
2. **Verified getting-started snippets** — `data/getting_started.yaml` (43 snippets), rendered by
   family.html; a product/platform with no entry falls back to its install command.
3. **`examples/getting-started/<product>/<platform>/`** — runnable verification apps (.NET csproj+
   Program.cs, Java pom+Example.java, Python example.py, Node package.json+example.js for
   conversion/viewer). `examples/.gitignore` (bin/obj/target/node_modules/.venv/.pkgs),
   `examples/README.md`, `examples/getting-started/signature/java/.mvn/jvm.config`.
4. **`PRODUCTS_DATA_STORE/`** — reusable knowledge base (Product Context Agent foundation):
   `README.md`, `PLATFORMS.md` (per-platform setup/verify/**all gotchas**), `products/*.md` (15),
   `index.json` (machine-readable), `tools/` (the generators + reflector + `examples.json` +
   `versions.txt` + `*_snippets.json`), `.gitignore`.
5. **Version alignment** — normalized 13 family `_index.md` `platforms[].version` to X.Y.Z (e.g.
   conversion Java `26.5`→`26.5.0`); `versionUrl`s untouched.
6. **Docs** — `CHANGELOG.md`, `CLAUDE.md` updated.

## Verification matrix (compile/import-verified against real SDKs)
| Platform | Verified | Method | N/A |
|---|---|---|---|
| .NET | 15/15 | `dotnet build` | — |
| Java | 13/13 | `mvn compile` | classification, markdown (no Java SDK) |
| Python | 13/13 | isolated install → run-to-FileNotFound | search, classification (no pkg); annotation = docs (PyPI stub) |
| Node.js | 2/9 (conversion, viewer) | JAVA_HOME + require + smoke | 7 blocked (see below) |

## Key gotchas (full detail in PRODUCTS_DATA_STORE/PLATFORMS.md)
- **Python**: the `*-net` packages are .NET-backed and **conflict if co-installed** → verify each in
  isolation (`pip uninstall -y <all> && pip install groupdocs-<p>-net`). **`groupdocs-annotation-net`
  PyPI = 0.0.0 stub** (real wheels on releases.groupdocs.com). pyenv `python` is a **.bat shim** that
  mangles multi-line `python -c` → use script files. **venv interpreters crash (exit 127)** loading the
  CLR pkgs → use the base `python3` (3.12). API is snake_case.
- **Java**: versions from `curl -sL .../maven-metadata.xml` `<release>`; repo
  `https://releases.groupdocs.com/java/repo/`. **GroupDocs.Signature jar manifest >16 MB** → JDK 17+
  needs `MAVEN_OPTS="-Djdk.jar.maxSignatureFileSize=104857600"`. TextSignOptions in `…options.sign`;
  parser TextReader in `…parser.data`.
- **Node**: **must set `JAVA_HOME`** to a JDK or `require()` hangs. **node-java 0.18 fails to source-
  build on Node 22** (`MSBuild exit 1`) — conversion/viewer worked only via a **prebuilt** binary;
  the other 7 fall back to source build and fail. Install ONE pkg per project; **do not clear the
  gyp/prebuilt cache**. To finish the 7: reuse a working `node_modules/java` prebuilt, or use a
  Node/arch with a published prebuilt.
- **.NET**: reflect namespaces via `PRODUCTS_DATA_STORE/tools/refl` (MetadataLoadContext). Search:
  drop `using System;` (clashes with `System.Index`).
- **API drifts fixed during verification**: metadata `Sanitize()`/`sanitize()` (was
  RemoveImageResourcePackage/MP3); signature/Python namespaces+casing; parser/Python `get_text()`;
  watermark/Python broken line-continuations.

## Regeneration pipeline (`PRODUCTS_DATA_STORE/tools/`)
`extract_examples.py`→`examples.json`; `gen_net.py`/`gen_java.py`/`gen_py.py`→apps + `*_snippets.json`
(then `dotnet build`/`mvn compile`/isolated `python`); `gen_data.py`→`data/getting_started.yaml`;
`gen_datastore.py`→PRODUCTS_DATA_STORE; `normalize_versions.py`→family versions. Run with `python`
(3.14, has pyyaml/tomllib) except the GroupDocs imports which use base `python3` (3.12).

## Deferred family-mockup deltas (intentionally not done; ask user before adding)
- Standalone **dark header/footer** (we reuse the site theme chrome, consistent w/ home/404).
- **"Popular classes & namespaces"** grid (needs curated data; could derive from search index).
- **Resources as 2-letter monograms** (kept branded product SVG icons).
- **Inline yes/no feedback** card (kept theme feedback-form).

## Node remaining (7, blocked): signature, comparison, editor, merger, metadata, search, watermark.

## Local preview / verify
`hugo server` is broken on this content. Use:
```
bash build-local.sh conversion annotation comparison classification   # home + listed products
python scripts/serve-local.py 1313                                            # serve ./public-local (UTF-8)
```
Then http://localhost:1313/conversion/ etc. (only built products exist locally; others 404).
Confirmed working: conversion family page = full-width, platform sidebar, terminal code block, v26.5.0.

## IMMEDIATE NEXT STEP
User reviewing the family redesign at localhost:1313. After review, either (a) add a deferred delta,
or (b) **commit everything** to both branches:
```
git add -A   # (excludes gitignored build artifacts; verify __pycache__ not staged)
git commit -F - <<'EOF'
Redesign family pages; verified getting-started across .NET/Java/Python/Node; add PRODUCTS_DATA_STORE
...
EOF
git branch -f main production && git fetch origin
git push origin production && git push origin main
```
Note: confirm `examples/**` build artifacts + `__pycache__/` are gitignored before committing.
