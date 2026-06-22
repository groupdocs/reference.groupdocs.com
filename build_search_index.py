#!/usr/bin/env python3
"""Build a search index (JSON) for the site-root 404 live search.

The site is built per product (each product is its own Hugo build), so there is no single
build that sees every product. This script derives a combined index from the generated
per-page Markdown (.md) output, which already carries a clean title (the leading `# ` line)
and whose file path maps directly to the page URL. Run it over a tree whose first path
segment is the product (e.g. the merged ./public-local, or a staged ./public per product).

Each entry is compact: {"t": title, "u": url, "p": platform, "g": product}.

Usage:
    python build_search_index.py [scan_dir] --out search-index.json
        scan_dir   directory to walk (default: public-local)
        --out      output JSON file (default: <scan_dir>/search-index.json)
"""
import argparse
import json
import os

PLATFORMS = {
    "net": ".NET",
    "java": "Java",
    "python-net": "Python",
    "nodejs-java": "Node.js",
}
# Root files that are not API pages.
SKIP_BASENAMES = {"llms.txt", "llms-full.txt"}


def title_of(path):
    """First Markdown heading (`# Title`) in the file, else None."""
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scan_dir", nargs="?", default="public-local")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    root = args.scan_dir
    out = args.out or os.path.join(root, "search-index.json")
    if not os.path.isdir(root):
        raise SystemExit("Error: directory '%s' does not exist." % root)

    entries = []
    for dp, _dirs, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".md") or fn in SKIP_BASENAMES:
                continue
            path = os.path.join(dp, fn)
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            slug = rel[:-3]  # drop .md
            segs = slug.split("/")
            product = segs[0]
            if product in ("index", "404") or slug == "index":
                continue  # site-root landing / 404, not a product page
            platform = PLATFORMS.get(segs[1], "") if len(segs) > 1 else ""
            title = title_of(path) or segs[-1]
            entries.append({"t": title, "u": "/" + slug, "p": platform, "g": product})

    entries.sort(key=lambda e: (e["g"], e["u"]))
    with open(out, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, separators=(",", ":"))
    print("Wrote %d entries to %s" % (len(entries), out))


if __name__ == "__main__":
    main()
