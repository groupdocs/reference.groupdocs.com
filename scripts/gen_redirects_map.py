#!/usr/bin/env python3
"""
gen_redirects_map.py — build a redirects.map "broken-link triage" batch for
reference.groupdocs.com from a crawler 404 export + the Hugo content tree.

Legacy 404 URLs on reference.groupdocs.com are OLD URL schemes for pages that
still exist at the current canonical 4-segment path:

    /<product>/<platform>/<namespace>/<class>[/<member>]/

Two legacy schemes dominate the 404 report:
  A) platform-less namespace : /<product>/<namespace>/<class>...   (missing net|java)
  B) flat .NET (classic)     : /<product>/net/<class>...           (missing namespace)

This maps each reported 404 to its canonical target (verified to exist in the
content tree), falling back to the nearest existing ancestor when a class/member
was reorganized away between SDK versions.

Output formats:
  --format map (default): redirects.map, published as S3 per-object redirects
      (x-amz-website-redirect-location -> HTTP 301) by scripts/deploy_redirects.sh.
      reference.groupdocs.com is S3 static-website hosting + CloudFront, so the website
      endpoint honors per-object redirects. (Same file also fits Ceph if it ever migrates.)
  --format nginx: exact-match `rewrite ... permanent;` rules spliced into an existing
      redirects/*.redirects.txt — ONLY for a legacy nginx edge (the reference .txt files
      are VM-era leftovers and are NOT consumed by S3+CloudFront; kept for reference).

Usage:
    python scripts/gen_redirects_map.py \
        --broken "../reference.groupdocs.com - Broken Links/broken-links-07-03-2026.txt" \
        --extra redirects/known_extra_404s.tsv \
        --content content/sites/groupdocs --date 2026-07-03 \
        --format map --out redirects/redirects.map

Deterministic: same inputs -> identical output (sorted), safe to re-run.
"""
import argparse
import os
import re
import sys
from collections import defaultdict

HOST_RE = re.compile(r'^(?:https?://)?reference\.groupdocs\.com', re.I)
PLATFORMS = ('net', 'java', 'python-net', 'nodejs-java', 'python', 'nodejs')
_AMBIGUOUS = object()


def norm_path(raw):
    """A raw report line -> product-relative path, lowercase, no leading/trailing slash.
    Returns '' for non-URL lines."""
    s = raw.strip()
    if 'reference.groupdocs.com' not in s:
        return ''
    s = HOST_RE.sub('', s)
    return s.strip().strip('/').lower()


def build_index(content_root):
    """Walk the content tree once. Returns:
      valid    : set of product-relative page paths ('metadata/net/groupdocs.metadata.common/...')
      class_ns : dict[(product, platform)] -> dict[class] -> namespace | _AMBIGUOUS
      products : sorted list of product names
    Every content directory is a page bundle (has _index.md), so a directory == a URL.
    """
    valid = set()
    class_ns = defaultdict(dict)
    products = []
    for product in sorted(os.listdir(content_root)):
        base = os.path.join(content_root, product, 'english')
        if not os.path.isdir(base):
            continue
        products.append(product)
        valid.add(product)  # product landing page /<product>/
        for dirpath, _dirnames, _files in os.walk(base):
            rel = os.path.relpath(dirpath, base)
            if rel == '.':
                continue
            rel = rel.replace(os.sep, '/').lower()
            valid.add(f"{product}/{rel}")
            segs = rel.split('/')
            if len(segs) == 3:  # platform / namespace / class
                platform, ns, cls = segs
                idx = class_ns[(product, platform)]
                if cls in idx and idx[cls] != ns:
                    idx[cls] = _AMBIGUOUS
                elif cls not in idx:
                    idx[cls] = ns
    return valid, class_ns, products


def lookup_ns(class_ns, product, platform, cls):
    ns = class_ns.get((product, platform), {}).get(cls)
    return ns if (ns is not None and ns is not _AMBIGUOUS) else None


def candidates_for(path, class_ns):
    """Yield (candidate_path, category) transforms in priority order (best first)."""
    segs = path.split('/')
    product, rest = segs[0], segs[1:]
    if not rest:
        return
    s0 = rest[0]

    # ---- scheme A: platform-less namespace (insert net|java) ----
    if s0.startswith('com.groupdocs.'):
        plat = 'java'
    elif s0.startswith('groupdocs.'):
        plat = 'net'
    else:
        plat = None
    if plat:
        # A1: keep namespace, just insert the platform segment
        yield ('/'.join([product, plat] + rest), 'scheme-a-insert-platform')
        # A2: class relocated to a different namespace -> look it up by class name
        if len(rest) >= 2:
            cls, tail = rest[1], rest[2:]
            ns_now = lookup_ns(class_ns, product, plat, cls)
            if ns_now and ns_now != s0:
                yield ('/'.join([product, plat, ns_now, cls] + tail), 'scheme-a-relocate-class')

    # ---- scheme B: flat platform + class (insert the missing namespace) ----
    if s0 in PLATFORMS and len(rest) >= 2 and not (
            rest[1].startswith('groupdocs.') or rest[1].startswith('com.groupdocs.')):
        cls, tail = rest[1], rest[2:]
        ns = lookup_ns(class_ns, product, s0, cls)
        if ns:
            yield ('/'.join([product, s0, ns, cls] + tail), 'scheme-b-insert-namespace')

    # ---- scheme D: collapse consecutive duplicate segments (doubled namespace) ----
    collapsed = []
    for seg in segs:
        if not (collapsed and collapsed[-1] == seg):
            collapsed.append(seg)
    if collapsed != segs:
        yield ('/'.join(collapsed), 'collapse-duplicate-segment')


def resolve(path, valid, class_ns):
    """Return (target_path_no_slashes, category). Picks the first transform whose
    result exists; else walks up to the nearest existing ancestor."""
    cands = list(candidates_for(path, class_ns))
    for cand, cat in cands:
        if cand in valid:
            return cand, cat
    # fallback: ancestor-walk the best structural candidate (or the original path)
    base = cands[0][0] if cands else path
    parts = base.split('/')
    for cut in range(len(parts) - 1, 0, -1):
        anc = '/'.join(parts[:cut])
        if anc in valid:
            return anc, 'fallback-ancestor'
    return parts[0], 'fallback-product'


MARK_BEGIN = "# >>> BEGIN broken-link redirects (generated by scripts/gen_redirects_map.py) - do not edit below >>>"
MARK_END = "# <<< END broken-link redirects <<<"


def write_map(out, date, results, groups, cats):
    """products.groupdocs.com redirects.map format (whitespace columns), for the Ceph deploy path."""
    width = max((len('/' + s) for s in results), default=40) + 2
    lines = [
        "# Simple page redirects -> applied to the S3 static-website bucket (AWS S3 + CloudFront) by",
        "# scripts/deploy_redirects.sh as per-object redirects (x-amz-website-redirect-location -> 301).",
        "# Whitespace-separated columns:",
        "#   source  target(/x/=same-site path | http..=external)  type(permanent|temp|removed)  added",
        "# Regenerate with scripts/gen_redirects_map.py --format map; do not hand-delete.",
        "",
        f"# ---- broken-link triage {date} ({len(results)} redirects) ----",
    ]
    for cat in cats:
        rows = sorted(groups[cat])
        lines.append("")
        lines.append(f"# {cat} ({len(rows)})")
        for src, tgt in rows:
            lines.append(f"{('/' + src).ljust(width)}{tgt.ljust(38)} permanent  {date}")
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    with open(out, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write("\n".join(lines) + "\n")


def write_nginx(out, date, results, groups, cats):
    """Splice exact-match `rewrite ... permanent;` rules into an existing redirects/*.redirects.txt.
    Byte-level splice preserves everything above MARK_BEGIN verbatim (header + locale rules)."""
    def esc(s):  # escape regex metachars in the literal path (only '.' occurs in these paths)
        return s.replace('\\', '\\\\').replace('.', r'\.')

    lines = [
        MARK_BEGIN,
        f"# broken-link triage {date} ({len(results)} redirects) - exact-match 301s generated from the",
        "# 404 crawl + content tree by scripts/gen_redirects_map.py (every target verified to exist).",
        "# Regenerate: python scripts/gen_redirects_map.py --format nginx --out <this file>",
        f"# Perf: {len(results)} sequential rewrites; convert to an nginx map{{}} (http context) if preferred.",
    ]
    for cat in cats:
        rows = sorted(groups[cat])
        lines.append("")
        lines.append(f"# {cat} ({len(rows)})")
        for src, tgt in rows:
            lines.append(f"rewrite ^/{esc(src)}/?$ {tgt} permanent;")
    lines.append("")
    lines.append(MARK_END)
    block = ("\n".join(lines) + "\n").encode('utf-8')

    begin = MARK_BEGIN.encode('utf-8')
    if os.path.exists(out):
        data = open(out, 'rb').read()
        i = data.find(begin)
        head = (data[:i] if i != -1 else data).rstrip(b'\n') + b'\n\n'
    else:
        head = b''
    with open(out, 'wb') as fh:
        fh.write(head + block)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--broken', required=True, help='crawler 404 export (txt)')
    ap.add_argument('--extra', default=None,
                    help='curated TSV of known-bad URLs not in the crawl: "source [target]" per line')
    ap.add_argument('--content', default='content/sites/groupdocs', help='content root')
    ap.add_argument('--date', default='2026-07-03', help='batch date YYYY-MM-DD')
    ap.add_argument('--format', choices=['map', 'nginx'], default='map',
                    help="map = redirects.map for S3 per-object redirects via deploy_redirects.sh "
                         "(reference.groupdocs.com = S3 website + CloudFront; default); "
                         "nginx = rewrite rules for a legacy nginx edge (the .txt files are vestigial).")
    ap.add_argument('--out', required=True,
                    help="output file: the redirects.map (map) or a redirects/*.redirects.txt to splice (nginx)")
    args = ap.parse_args()

    valid, class_ns, products = build_index(args.content)
    print(f"[index] {len(products)} products, {len(valid):,} valid URLs", file=sys.stderr)

    with open(args.broken, encoding='utf-8', errors='replace') as fh:
        crawl = {p for p in (norm_path(ln) for ln in fh) if p}
    print(f"[input] {len(crawl):,} unique 404 URLs from crawl", file=sys.stderr)

    # curated extras (known-bad URLs not in the crawl): source -> explicit target path | None
    overrides = {}
    if args.extra:
        with open(args.extra, encoding='utf-8', errors='replace') as fh:
            for ln in fh:
                if not ln.strip() or ln.lstrip().startswith('#'):
                    continue
                f = ln.split()
                src = f[0].strip().strip('/').lower()
                overrides[src] = (f[1].strip().strip('/').lower() if len(f) > 1 else None)
        print(f"[input] {len(overrides):,} curated extras", file=sys.stderr)

    sources = sorted(crawl | set(overrides))

    # source -> (target, category)
    results = {}
    skipped_valid = []
    for src in sources:
        if src in valid:                     # already a real page — shouldn't 404; skip
            skipped_valid.append(src)
            continue
        ov = overrides.get(src)
        if ov and ov in valid:               # curated explicit target wins (verified)
            tgt, cat = ov, 'xmldocmd-namespace-doubling'
        else:
            tgt, cat = resolve(src, valid, class_ns)
        results[src] = (f"/{tgt}/", cat)

    # group by category for readable, counted sub-sections (matches products.groupdocs.com)
    order = ['scheme-a-insert-platform', 'scheme-a-relocate-class',
             'scheme-b-insert-namespace', 'collapse-duplicate-segment',
             'xmldocmd-namespace-doubling', 'fallback-ancestor', 'fallback-product']
    groups = defaultdict(list)
    for src, (tgt, cat) in results.items():
        groups[cat].append((src, tgt))
    cats = [c for c in order if c in groups] + sorted(c for c in groups if c not in order)

    if args.format == 'map':
        write_map(args.out, args.date, results, groups, cats)
    else:
        write_nginx(args.out, args.date, results, groups, cats)

    # summary
    print(f"[out] wrote {args.out} ({args.format}): {len(results):,} redirects", file=sys.stderr)
    for cat in cats:
        print(f"    {cat:32} {len(groups[cat]):>5}", file=sys.stderr)
    fallback = len(groups.get('fallback-ancestor', [])) + len(groups.get('fallback-product', []))
    exact = len(results) - fallback
    print(f"[summary] exact-page: {exact:,}   ancestor-fallback: {fallback:,}", file=sys.stderr)
    if skipped_valid:
        print(f"[note] {len(skipped_valid)} reported URLs are already valid pages (skipped): "
              f"{skipped_valid[:5]}", file=sys.stderr)


if __name__ == '__main__':
    main()
