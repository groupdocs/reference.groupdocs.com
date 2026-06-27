#!/usr/bin/env python3
"""Build data/versions.json for the family pages from products.groupdocs.com/versions.json.

The family template (themes/docs/layouts/_default/family.html) reads the resulting Hugo data file
(site.Data.versions) and renders the live version + release-notes link per product/platform, falling
back to each page's front-matter values when a product/platform is absent here.

We TRIM the upstream feed to just the fields we render (version + releaseNotesUrl) and sort keys, so the
file only changes when an actual version changes — not on every upstream `generatedAt`/`downloads` churn.
That lets the scheduled workflow deploy only when something really moved.

Usage:
  python update_versions.py                      # fetch live, write data/versions.json
  python update_versions.py --input some.json    # transform a local copy (for testing)
  python update_versions.py --out path.json
"""
import argparse, json, os, sys, urllib.request

URL = "https://products.groupdocs.com/versions.json"


def strip_v(s):
    s = (s or "").strip()
    return s[1:] if s[:1] in ("v", "V") else s


def transform(data):
    out = {}
    for slug, p in (data.get("products") or {}).items():
        plats = {}
        for pk, pv in (p.get("platforms") or {}).items():
            ver = strip_v(pv.get("version"))
            if not ver:
                continue
            plats[pk] = {"version": ver, "url": pv.get("releaseNotesUrl", "")}
        if plats:
            out[slug] = {"latest": strip_v(p.get("latestVersion")), "platforms": plats}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", help="local versions.json to transform (default: fetch live)")
    ap.add_argument("--url", default=URL)
    ap.add_argument("--out", default="data/versions.json")
    a = ap.parse_args()

    if a.input:
        with open(a.input, encoding="utf-8") as f:
            data = json.load(f)
    else:
        req = urllib.request.Request(a.url, headers={"User-Agent": "reference.groupdocs.com version sync"})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)

    out = transform(data)
    if not out:
        print("ERROR: no products parsed from source", file=sys.stderr)
        sys.exit(1)

    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    with open(a.out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, indent=2, sort_keys=True, ensure_ascii=False)
        f.write("\n")
    print(f"wrote {a.out}: {len(out)} products")


if __name__ == "__main__":
    main()
