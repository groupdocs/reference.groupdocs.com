#!/usr/bin/env python3
"""Build the combined, compacted llms-full.txt for the SITE ROOT.

reference.groupdocs.com builds each product as a separate Hugo site, so Hugo can never see
all products at once — there is no single build that can emit a site-wide llms-full.txt. This
script aggregates from SOURCE instead (the same trick build_search_index.py uses): it walks
every product's `english/**/_index.md`, strips the auto-generated navigation boilerplate, and
emits one well-structured Markdown file covering the entire API reference.

Compaction is "complete, boilerplate-stripped": every page's signatures, summaries, and
member/parameter tables are kept; only navigation noise is removed — `### See Also` footers,
`**Learn more**` blocks, internal link URLs (kept as plain text), front matter, heading anchor
suffixes, Java `----` separators, and blank-line runs. Code fences are never touched.

Output outline (a real navigable tree):
    # GroupDocs API References — Complete API Reference   (top header)
    # GroupDocs.Annotation                                (one per product, family weight order)
    ## .NET                                               (platform, when the URL's 1st segment changes)
    ### Annotator.Add                                     (page; body headings demoted +2 below it)
    Path: https://reference.groupdocs.com/annotation/net/groupdocs.annotation/annotator/add/

Usage:
    python build_llms_full.py --source content/sites/groupdocs \\
        --base-url https://reference.groupdocs.com --out llms-full.txt
    python build_llms_full.py --source content/sites/groupdocs --only annotation,conversion ...
"""
import argparse
import os
import re

PLATFORMS = {
    "net": ".NET",
    "java": "Java",
    "python-net": "Python",
    "nodejs-java": "Node.js",
}

FM_KEY = re.compile(r"^([A-Za-z0-9_]+)\s*:\s*(.*)$")
HEADING = re.compile(r"^(#{1,6})(\s.*)$")          # markdown ATX heading
HR = re.compile(r"^\s*-{3,}\s*$")                  # Java member / overload separator
ANCHOR = re.compile(r"\s*\{#[^}]*\}\s*$")          # heading anchor suffix, e.g. ` {#add}`
BULLET = re.compile(r"^\*(\s|$)")                  # `* …` list item (incl. empty Java ` *  `)
LINK = re.compile(r"\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)]+)\)")  # [text](url); text may hold [] (Java arrays)
EXTERNAL = re.compile(r"(?i)^(https?:|mailto:)")
FENCE_OPEN = re.compile(r"^\s*([`~]{3,})")          # ``` / ~~~ (3+) code-fence opener
FENCE_CLOSE = re.compile(r"^\s*([`~]{3,})\s*$")     # bare fence (no info string)


def open_fence(line):
    """Return (char, length) if `line` opens a code fence, else None."""
    m = FENCE_OPEN.match(line)
    return (m.group(1)[0], len(m.group(1))) if m else None


def closes_fence(line, fence):
    """True if `line` closes the open `fence` — same char, run >= opener, nothing after.
    Handles nested fences: an outer ```` block is not closed by an inner ``` line."""
    m = FENCE_CLOSE.match(line)
    return bool(m) and m.group(1)[0] == fence[0] and len(m.group(1)) >= fence[1]


def read_page(path):
    """Read one _index.md: return (front-matter dict, body lines).

    utf-8-sig strips the BOM some python-net files carry; errors='replace' keeps the output
    valid UTF-8 even if a source file has a stray non-UTF-8 byte (so S3 serves it cleanly).
    Newlines are normalised to '\\n'.
    """
    fm = {}
    try:
        with open(path, "r", encoding="utf-8-sig", errors="replace", newline="") as f:
            text = f.read()
    except OSError:
        return fm, []
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    idx = 0
    if lines and lines[0].strip() == "---":
        idx = 1
        while idx < len(lines):
            if lines[idx].strip() == "---":
                idx += 1
                break
            m = FM_KEY.match(lines[idx])
            if m:
                k, v = m.group(1).lower(), m.group(2).strip()
                if len(v) >= 2 and v[0] in "\"'" and v[-1] == v[0]:
                    v = v[1:-1]
                fm[k] = v
            idx += 1
    return fm, lines[idx:]


def _strip_links(line):
    """[text](url) -> text for internal/relative links; external http(s)/mailto links kept."""
    def sub(m):
        return m.group(0) if EXTERNAL.match(m.group(2).strip()) else m.group(1)
    return LINK.sub(sub, line)


def clean_lines(lines):
    """Drop navigation boilerplate (fence-aware) and clean kept lines."""
    out = []
    fence = None
    n = len(lines)
    i = 0
    while i < n:
        line = lines[i]
        if fence is not None:
            out.append(line)
            if closes_fence(line, fence):
                fence = None
            i += 1
            continue
        of = open_fence(line)
        if of is not None:
            fence = of
            out.append(line)
            i += 1
            continue
        s = line.strip()
        # `### See Also` (and its bullets) — skip to the next heading / fence / EOF.
        if HEADING.match(line) and "see also" in s.lower():
            i += 1
            while i < n and open_fence(lines[i]) is None and not HEADING.match(lines[i]):
                i += 1
            continue
        # `**Learn more**` block — skip following blank/bullet lines.
        if s == "**Learn more**":
            i += 1
            while i < n:
                t = lines[i].strip()
                if t == "" or BULLET.match(t):
                    i += 1
                    continue
                break
            continue
        # Java member / overload separators (`----`).
        if HR.match(line):
            i += 1
            continue
        if HEADING.match(line):
            line = ANCHOR.sub("", line)
        out.append(_strip_links(line))
        i += 1
    return out


def drop_empty_and_demote(lines):
    """Drop headings whose section is empty (e.g. an emptied `## Remarks`) and demote body
    headings by +2 so each page's content sits under its `###` page heading. Fence-aware."""
    out = []
    fence = None
    n = len(lines)
    i = 0
    while i < n:
        line = lines[i]
        if fence is not None:
            out.append(line)
            if closes_fence(line, fence):
                fence = None
            i += 1
            continue
        of = open_fence(line)
        if of is not None:
            fence = of
            out.append(line)
            i += 1
            continue
        m = HEADING.match(line)
        if m:
            j = i + 1
            while j < n and lines[j].strip() == "":
                j += 1
            if j >= n or HEADING.match(lines[j]):
                i = j  # empty section: drop this heading (and the blanks after it)
                continue
            level = min(len(m.group(1)) + 2, 6)
            out.append("#" * level + m.group(2))
            i += 1
            continue
        out.append(line)
        i += 1
    return out


def collapse(lines):
    """Collapse blank-line runs and trim trailing whitespace (outside fences)."""
    out = []
    blank = False
    fence = None
    for line in lines:
        if fence is not None:
            out.append(line)
            if closes_fence(line, fence):
                fence = None
            blank = False
            continue
        of = open_fence(line)
        if of is not None:
            fence = of
            out.append(line)
            blank = False
            continue
        line = line.rstrip()
        if line == "":
            if blank:
                continue
            blank = True
        else:
            blank = False
        out.append(line)
    while out and out[0] == "":
        out.pop(0)
    while out and out[-1] == "":
        out.pop()
    return out


def transform_body(body_lines):
    return collapse(drop_empty_and_demote(clean_lines(body_lines)))


def collect(base, only=None):
    """Return products [{key,title,weight,blurb,pages:[{title,url,platform_key,platform,body}]}]."""
    products = []
    for product in sorted(os.listdir(base)):
        if product == "home":
            continue
        eng = os.path.join(base, product, "english")
        if not os.path.isdir(eng):
            continue
        if only and product not in only:
            continue
        fam_fm, _ = read_page(os.path.join(eng, "_index.md"))
        try:
            weight = int(fam_fm.get("weight", "999"))
        except ValueError:
            weight = 999
        pages = []
        for dp, _dirs, files in os.walk(eng):
            if "_index.md" not in files:
                continue
            fm, body = read_page(os.path.join(dp, "_index.md"))
            url = fm.get("url", "").strip()
            if not url or url == "/" or fm.get("layout") == "family":
                continue  # family landing page is covered by the site-root llms.txt directory
            rel = url.strip("/")
            segs = rel.split("/")
            pages.append({
                "title": fm.get("title") or segs[-1],
                "url": "/" + rel + "/",
                "platform_key": segs[0],
                "platform": PLATFORMS.get(segs[0]) or segs[0].replace("-", " ").title(),
                "body": body,
            })
        pages.sort(key=lambda p: p["url"])
        products.append({
            "key": product,
            "title": fam_fm.get("title") or product,
            "weight": weight,
            "blurb": fam_fm.get("lead") or fam_fm.get("description") or "",
            "pages": pages,
        })
    products.sort(key=lambda p: (p["weight"], p["key"]))
    return products


def render(products, base_url):
    base = base_url.rstrip("/")
    out = [
        "# GroupDocs API References — Complete API Reference",
        "",
        "> Class library and REST API reference for GroupDocs document-processing SDKs "
        "across .NET, Java, Node.js, and Python.",
        "",
        "This file concatenates the entire API reference for every product, with navigation "
        "boilerplate removed. One top-level section per product, grouped by platform.",
    ]
    for prod in products:
        out += ["", "", "# " + prod["title"]]
        if prod["blurb"]:
            out += ["", "> " + prod["blurb"]]
        cur = None
        for pg in prod["pages"]:
            if pg["platform_key"] != cur:
                cur = pg["platform_key"]
                out += ["", "## " + pg["platform"]]
            # Link to the page's Markdown (.md ugly-URL sibling) — this file is for LLMs/agents.
            md = base + "/" + prod["key"] + pg["url"].rstrip("/") + ".md"
            out += ["", "### " + pg["title"], "Path: " + md]
            body = transform_body(pg["body"])
            if body:
                out += [""] + body
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, help="content root, e.g. content/sites/groupdocs")
    ap.add_argument("--base-url", default="https://reference.groupdocs.com",
                    help="absolute base for Path: lines")
    ap.add_argument("--only", default=None, help="comma-separated product subset (faster local preview)")
    ap.add_argument("--out", default="llms-full.txt")
    args = ap.parse_args()

    if not os.path.isdir(args.source):
        raise SystemExit("Error: source dir '%s' does not exist." % args.source)
    only = {p.strip() for p in args.only.split(",")} if args.only else None
    products = collect(args.source, only)
    text = render(products, args.base_url)
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    pages = sum(len(p["pages"]) for p in products)
    print("Wrote %d products / %d pages (%.1f MB) to %s"
          % (len(products), pages, len(text.encode("utf-8")) / 1048576.0, args.out))


if __name__ == "__main__":
    main()
