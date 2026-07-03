#!/usr/bin/env bash
#
# Publish the page redirects in redirects/redirects.map to the S3 static-website bucket
# as per-object redirects (x-amz-website-redirect-location -> HTTP 301), surfaced through
# CloudFront. Idempotent and re-runnable.
#
# reference.groupdocs.com is AWS S3 (static-website hosting) + CloudFront. Confirmed:
# the bucket's ...s3-website-us-west-2.amazonaws.com endpoint returns 200 and honours
# per-object website redirects. (The old redirects/*.redirects.txt nginx files are VM-era
# leftovers and are NOT consumed by this stack.)
#
# Per-entry "type" in redirects.map:
#   permanent  301 via per-object redirect (default).
#   temp       302 -> not supported by per-object redirects (301-only); flagged & SKIPPED (exit 1).
#   removed    delete the redirect objects, but only if they are still redirects (head-object guard).
#
# Required env:
#   BUCKET      e.g. reference.groupdocs.com   (staging: reference2.groupdocs.com)
#   REGION      e.g. us-west-2
#   AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY   creds for BUCKET
# Optional env:
#   CF_DISTRIBUTION   CloudFront distribution id -> invalidate the affected product prefixes
#   VERIFY_BASE       host to curl when verifying (e.g. https://reference.groupdocs.com)
#   MAP_FILE          default: <repo>/redirects/redirects.map
#   DRY_RUN=1         print actions, touch nothing (no AWS calls)
#
set -euo pipefail
: "${BUCKET:?set BUCKET}" "${REGION:?set REGION}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MAP_FILE="${MAP_FILE:-$SCRIPT_DIR/../redirects/redirects.map}"
VERIFY_BASE="${VERIFY_BASE:-}"; VERIFY_BASE="${VERIFY_BASE%/}"

dry(){ [ "${DRY_RUN:-0}" = "1" ]; }

put_redirect(){ # key location
  dry && { echo "   would write $1 (301 -> $2)"; return 0; }
  aws s3api put-object --bucket "$BUCKET" --key "$1" \
    --website-redirect-location "$2" --content-type "text/html" \
    --region "$REGION" >/dev/null
  echo "   wrote s3://$BUCKET/$1 (301 -> $2)"
}

safe_delete(){ # key -- delete ONLY if it is still a redirect object, never real content
  dry && { echo "   would delete $1 (only if still a redirect)"; return 0; }
  local loc
  if ! loc=$(aws s3api head-object --bucket "$BUCKET" --key "$1" --region "$REGION" \
              --query 'WebsiteRedirectLocation' --output text 2>/dev/null); then
    echo "   absent: $1"; return 0
  fi
  if [ -z "$loc" ] || [ "$loc" = "None" ]; then
    echo "   KEEP $1 -> not a redirect (real content?); not deleting"; return 0
  fi
  aws s3api delete-object --bucket "$BUCKET" --key "$1" --region "$REGION" >/dev/null
  echo "   deleted s3://$BUCKET/$1 (was 301 -> $loc)"
}

verify_segs=(); temp_skipped=(); declare -A prefixes=()

while read -r src tgt type added _; do
  src="${src%$'\r'}"; tgt="${tgt%$'\r'}"; type="${type%$'\r'}"
  [ -z "${src:-}" ] && continue
  case "$src" in \#*) continue;; esac
  type="${type:-permanent}"
  seg="${src#/}"; seg="${seg%/}"
  # website-redirect-location: same-site path (/x/) or external URL, used verbatim
  loc="$tgt"

  case "$type" in
    permanent)
      echo ">> [permanent] /$seg -> $loc   (added ${added:-?})"
      put_redirect "$seg" "$loc"
      put_redirect "$seg/index.html" "$loc"
      prefixes["/${seg%%/*}/*"]=1
      verify_segs+=("$seg")
      ;;
    removed)
      echo ">> [removed] /$seg   (added ${added:-?})"
      safe_delete "$seg"; safe_delete "$seg/index.html"
      prefixes["/${seg%%/*}/*"]=1
      verify_segs+=("$seg")
      ;;
    temp)
      echo ">> [temp] /$seg -> $tgt : 302 not supported by per-object redirects (301-only). SKIPPED."
      temp_skipped+=("/$seg")
      ;;
    *) echo ">> /$seg: unknown type '$type'"; exit 2;;
  esac
done < "$MAP_FILE"

# Invalidate CloudFront for the affected product prefixes (few wildcards, not per-object).
if [ -n "${CF_DISTRIBUTION:-}" ] && [ "${#prefixes[@]}" -gt 0 ]; then
  paths="${!prefixes[*]}"
  echo
  echo "== CloudFront invalidation ($CF_DISTRIBUTION): $paths =="
  dry || aws cloudfront create-invalidation --distribution-id "$CF_DISTRIBUTION" \
           --paths $paths --query 'Invalidation.Id' --output text
fi

# Verify a sample (avoid thousands of requests): first 15 + last 5.
if [ -n "$VERIFY_BASE" ] && ! dry; then
  echo
  echo "== Verify ($VERIFY_BASE) — want 301 -> canonical =="
  sample=("${verify_segs[@]:0:15}" "${verify_segs[@]: -5}")
  for seg in "${sample[@]}"; do
    echo "-- /$seg/"
    curl -sS -o /dev/null -D - "$VERIFY_BASE/$seg/" | grep -iE "^HTTP|^location:" || true
  done
fi

if [ "${#temp_skipped[@]}" -gt 0 ]; then
  echo; echo "!! ${#temp_skipped[@]} temp (302) entr(ies) SKIPPED: ${temp_skipped[*]}"
  echo "!! 302 needs S3 website RoutingRules or a CloudFront function. Exiting non-zero to flag."
  exit 1
fi
