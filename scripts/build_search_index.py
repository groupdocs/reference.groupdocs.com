#!/usr/bin/env python3
"""Build a search index (JSON) for the site-root 404 live search.

Two ways to produce the combined index (both yield the same compact entries
{"t": title, "u": url, "p": platform, "g": product}):

1. Built-tree mode (default): walk generated per-page Markdown (.md) output and read the
   leading `# Title`. Used by build-local.sh (merged ./public-local) and the per-product CI
   slice (`--product <name>` over a single build's ./public).

2. Source mode (`--source content/sites/groupdocs`): parse each product's source
   `english/**/_index.md` front matter (title + url) directly — no Hugo build needed. Lets a
   lightweight CI job rebuild the whole index on any content push.

Usage:
    python scripts/build_search_index.py [scan_dir] [--product NAME] --out search-index.json
    python scripts/build_search_index.py --source content/sites/groupdocs --out search-index.json
"""
import argparse
import json
import os
import re

PLATFORMS = {
    "net": ".NET",
    "java": "Java",
    "python-net": "Python",
    "nodejs-java": "Node.js",
}
# Root files that are not API pages.
SKIP_BASENAMES = {"llms.txt", "llms-full.txt"}
FM_KEY = re.compile(r"^([A-Za-z0-9_]+)\s*:\s*(.*)$")


def title_of(path):
    """First Markdown heading (`# Title`) in a built .md file, else None."""
    try:
        with open(path, "r", encoding="utf-8", errors="surrogateescape") as f:
            for _ in range(40):  # title is at the top
                line = f.readline()
                if not line:
                    break
                s = line.strip()
                if s.startswith("# "):
                    return s[2:].strip()
    except OSError:
        pass
    return None


def parse_front_matter(path):
    """Parse a leading YAML (`---`) front-matter block into a lowercased-key dict."""
    fm = {}
    try:
        # utf-8-sig strips a leading BOM — some generated _index.md (python-net) have one,
        # which would otherwise make the `---` front-matter delimiter check fail.
        with open(path, "r", encoding="utf-8-sig", errors="surrogateescape") as f:
            if f.readline().strip() != "---":
                return fm
            for line in f:
                s = line.rstrip("\n")
                if s.strip() == "---":
                    break
                m = FM_KEY.match(s)
                if m:
                    k, v = m.group(1).lower(), m.group(2).strip()
                    if len(v) >= 2 and v[0] in "\"'" and v[-1] == v[0]:
                        v = v[1:-1]
                    fm[k] = v
    except OSError:
        pass
    return fm


def from_source(base):
    """Build entries from product source trees: <base>/<product>/english/**/_index.md."""
    entries = []
    if not os.path.isdir(base):
        raise SystemExit("Error: source dir '%s' does not exist." % base)
    for product in sorted(os.listdir(base)):
        eng = os.path.join(base, product, "english")
        if product == "home" or not os.path.isdir(eng):
            continue
        for dp, _dirs, files in os.walk(eng):
            if "_index.md" not in files:
                continue
            fm = parse_front_matter(os.path.join(dp, "_index.md"))
            url = fm.get("url", "").strip()
            if not url or url == "/" or fm.get("layout") == "family":
                continue  # the product family landing page is reached via the directory
            rel = url.strip("/")
            segs = rel.split("/")
            entries.append({
                "t": fm.get("title") or segs[-1],
                "u": "/" + product + "/" + rel,
                "p": PLATFORMS.get(segs[0], "") if segs else "",
                "g": product,
            })
    return entries


def from_built_tree(root, prod):
    """Build entries from generated .md output (built-tree mode)."""
    entries = []
    for dp, _dirs, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".md") or fn in SKIP_BASENAMES:
                continue
            path = os.path.join(dp, fn)
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            slug = rel[:-3]  # drop .md
            if slug == "index":
                continue  # build-root landing (site home or product family page)
            segs = slug.split("/")
            if prod:
                product = prod
                platform = PLATFORMS.get(segs[0], "") if segs else ""
                url = "/" + prod + "/" + slug
            else:
                product = segs[0]
                if product == "404":
                    continue
                platform = PLATFORMS.get(segs[1], "") if len(segs) > 1 else ""
                url = "/" + slug
            entries.append({"t": title_of(path) or segs[-1], "u": url, "p": platform, "g": product})
    return entries


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scan_dir", nargs="?", default="public-local")
    ap.add_argument("--out", default=None)
    ap.add_argument("--product", default=None,
                    help="built-tree single-product mode: prefix URLs with /<product>/")
    ap.add_argument("--source", default=None,
                    help="source mode: content root (e.g. content/sites/groupdocs)")
    args = ap.parse_args()

    if args.source:
        entries = from_source(args.source)
        out = args.out or "search-index.json"
    else:
        root = args.scan_dir
        if not os.path.isdir(root):
            raise SystemExit("Error: directory '%s' does not exist." % root)
        entries = from_built_tree(root, args.product)
        out = args.out or os.path.join(root, "search-index.json")

    entries.sort(key=lambda e: (e["g"], e["u"]))
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(entries, f, ensure_ascii=False, separators=(",", ":"))
    print("Wrote %d entries to %s" % (len(entries), out))


if __name__ == "__main__":
    main()
