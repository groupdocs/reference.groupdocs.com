#!/usr/bin/env bash
# Combined LOCAL preview: builds the home (main index) at / plus the named product
# trees under /<product>/, merged into ./public-local — mirroring production, where
# each product is its own Hugo build served under a path prefix.
#
# Why a script (not a single `hugo server`): home and product content both author
# root-relative URLs (e.g. /net/...), so they can only coexist when each is built
# with its own baseURL prefix and merged.
#
# Usage:
#   ./build-local.sh                 # home + annotation (default)
#   ./build-local.sh viewer signature   # home + the listed products
# Then serve (serve-local.py sends charset=utf-8 for text, like production — plain
# `python -m http.server` omits it and shows —/→ as mojibake):
#   python serve-local.py 1313
set -euo pipefail

PORT="${PORT:-1313}"
OUT="public-local"
PRODUCTS=("$@")
[ ${#PRODUCTS[@]} -eq 0 ] && PRODUCTS=("annotation")

# Build home FIRST with --cleanDestinationDir (wipes stale output inside $OUT, including
# old product subdirs) — but not the $OUT dir itself, so a running http.server holding it
# open on Windows doesn't block the rebuild.
echo ">> home (main index) -> /"
hugo --config config-local.toml -b "http://localhost:$PORT/" -d "$PWD/$OUT" --cleanDestinationDir --minify

for p in "${PRODUCTS[@]}"; do
  echo ">> $p -> /$p/"
  hugo --configDir "config/sites/groupdocs/$p" --environment staging \
       -b "http://localhost:$PORT/$p/" -d "$PWD/$OUT/$p" --cleanDestinationDir --minify
  python resolve_md_links.py "$OUT/$p" --base-url "http://localhost:$PORT/$p" >/dev/null
  bash move_md_to_ugly_urls.sh "$OUT/$p" >/dev/null
  # Family page .md is served at /<product>.md (bucket root), not /<product>/index.md —
  # mirror that locally (production does this via deploy_product.yml).
  if [ -f "$OUT/$p/index.md" ]; then
    cp "$OUT/$p/index.md" "$OUT/$p.md"
    rm -f "$OUT/$p/index.md"
  fi
done

# Combined cross-product search index for the 404 live search (built from the merged tree).
python build_search_index.py "$OUT" --out "$OUT/search-index.json"

# Combined, compacted llms-full.txt (whole API reference, built from source). --only limits it
# to the products built locally so the preview is quick; production builds all 15.
python build_llms_full.py --source content/sites/groupdocs --base-url "http://localhost:$PORT" \
  --only "$(IFS=,; echo "${PRODUCTS[*]}")" --out "$OUT/llms-full.txt"

echo
echo "Built ${#PRODUCTS[@]} product(s) + home into ./$OUT"
echo "Serve with:  python serve-local.py $PORT      # UTF-8 charset, matches production"
