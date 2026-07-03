#!/usr/bin/env python3
"""Resolve relative links in generated Markdown (.md) output to absolute URLs.

Hugo emits the per-page Markdown output as public/<path>/index.md (pretty URLs) carrying the
page's RAW content. The auto-generated API-reference pages use RELATIVE links, e.g.
`](../ns/class)` or `](../../ns/class)` (variable depth), which Hugo templates cannot resolve
and which break once the .md is flattened to an ugly URL by move_md_to_ugly_urls.sh (the page
depth changes). This script resolves each relative link against the page's own URL and rewrites
it to an absolute URL, matching the theme partial themes/docs/layouts/partials/md/abs-content.txt
(which already absolutizes ROOT-relative links). The two are disjoint: abs-content.txt handles
`/...` links, this script handles `../`, `./`, and bare relative links.

Run it BEFORE move_md_to_ugly_urls.sh: resolution relies on the pretty path
public/<a>/<b>/index.md => page URL /<a>/<b>/.

Usage:
    python scripts/resolve_md_links.py [output_dir] --base-url <BASE>

    output_dir   Hugo output directory (default: "public").
    --base-url   The build's Hugo .Site.BaseURL, e.g.
                   production:  https://reference.groupdocs.com/<product>
                   staging:     /<product>
                   local:       http://localhost:1313/<product>
                 (Trailing slash is ignored.)
"""
import argparse
import os
import posixpath
import re
import sys

# Targets that are already absolute / not page-relative -> leave untouched.
# Root-relative ("/...") links are handled by the theme's md/abs-content.txt.
SKIP_PREFIXES = ("http://", "https://", "//", "mailto:", "tel:", "data:", "#", "/")

# Final-segment extensions treated as assets (NOT given a .md suffix). Namespace segments
# like "com.groupdocs.annotation" contain dots but are pages, so use an explicit whitelist
# rather than "has any extension".
ASSET_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico",
    ".css", ".js", ".json", ".xml", ".txt", ".pdf", ".zip", ".csv",
}

# Markdown inline/image link target:  ](target)   — also matches the image form ![alt](target).
MD_LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
# Raw-HTML attribute:  src="target" / href="target"  (also matches the href of xlink:href=).
HTML_ATTR_RE = re.compile(r'(\b(?:src|href)=")([^"]*)(")')


def is_relative(target):
    return bool(target) and not target.startswith(SKIP_PREFIXES)


def resolve(target, url_dir, base):
    """Resolve a page-relative target against url_dir and return an absolute URL."""
    hash_i = target.find("#")
    if hash_i != -1:
        path, anchor = target[:hash_i], target[hash_i:]
    else:
        path, anchor = target, ""
    if not path:
        return target
    resolved = posixpath.normpath(posixpath.join(url_dir, path))
    ext = posixpath.splitext(posixpath.basename(resolved))[1].lower()
    if ext not in ASSET_EXTS:
        resolved += ".md"  # page link -> .md sibling
    return base + resolved + anchor


def rewrite(content, url_dir, base):
    def md_sub(m):
        t = m.group(1)
        return "](" + resolve(t, url_dir, base) + ")" if is_relative(t) else m.group(0)

    def html_sub(m):
        t = m.group(2)
        return m.group(1) + resolve(t, url_dir, base) + m.group(3) if is_relative(t) else m.group(0)

    return HTML_ATTR_RE.sub(html_sub, MD_LINK_RE.sub(md_sub, content))


def main():
    ap = argparse.ArgumentParser(description="Resolve relative .md links to absolute URLs.")
    ap.add_argument("output_dir", nargs="?", default="public")
    ap.add_argument("--base-url", required=True,
                    help="Build .Site.BaseURL, e.g. https://reference.groupdocs.com/annotation or /annotation")
    args = ap.parse_args()

    out = args.output_dir
    base = args.base_url.rstrip("/")
    if not os.path.isdir(out):
        sys.exit("Error: directory '%s' does not exist. Run 'hugo' first." % out)

    changed = 0
    for root, _dirs, files in os.walk(out):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(root, fn)
            # Page URL dir from the file's location relative to out:
            #   public/java/ns/class/index.md -> /java/ns/class/
            #   public/index.md               -> /
            rel = os.path.relpath(os.path.dirname(path), out).replace(os.sep, "/")
            url_dir = "/" if rel == "." else "/" + rel + "/"
            # errors="surrogateescape" + newline="" so any non-UTF-8 byte or CRLF in the
            # generated content round-trips byte-for-byte (some source .md carry stray
            # Windows-1252 bytes, e.g. 0xae); the link regexes only touch ASCII syntax.
            with open(path, "r", encoding="utf-8", errors="surrogateescape", newline="") as f:
                content = f.read()
            new = rewrite(content, url_dir, base)
            if new != content:
                with open(path, "w", encoding="utf-8", errors="surrogateescape", newline="") as f:
                    f.write(new)
                changed += 1

    print("Resolved relative links in %d .md file(s) under '%s'." % (changed, out))


if __name__ == "__main__":
    main()
