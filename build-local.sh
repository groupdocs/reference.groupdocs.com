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
# Then serve:
#   python -m http.server 1313 --directory public-local --bind 127.0.0.1
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
  bash move_md_to_ugly_urls.sh "$OUT/$p" >/dev/null
done

echo
echo "Built ${#PRODUCTS[@]} product(s) + home into ./$OUT"
echo "Serve with:  python -m http.server $PORT --directory $OUT --bind 127.0.0.1"
