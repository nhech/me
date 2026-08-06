#!/usr/bin/env python3
"""Build longtd.me into dist/.

There is no bundler here on purpose — the site is hand-written static HTML. What this
does is the part that must not be done by hand: stamp every page with a build id that
is derived from the content, and refuse to ship if the page fails its own checks.

    python3 build.py

The stamp is a content hash, not a commit sha, because this tree is not a git repo.
That is arguably the better choice for a static site: the hash changes when the bytes
change and anyone can recompute it from what was served.
"""

import gzip
import hashlib
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"

SOURCES = [
    "index.html",
    "blog.html",
    "blog/idempotency.html",
    "styles.css",
    "script.js",
    "profile.json",
]
# copied verbatim into dist/, not hashed or checked
EXTRAS = ["CNAME"]
PAGES = [s for s in SOURCES if s.endswith(".html")]


def fail(msg):
    print(f"  ✗ {msg}")
    sys.exit(1)


def check(page: str, html: str):
    """Refuse to ship a page that contradicts itself."""
    if html.count("<div") != html.count("</div>"):
        fail(f"{page}: unbalanced divs ({html.count('<div')} open, {html.count('</div>')} close)")
    if "DRAFT" in html:
        fail(f"{page}: still contains a DRAFT placeholder")
    if html.count("<h1") != 1:
        fail(f"{page}: expected exactly one <h1>, found {html.count('<h1')}")
    if "<title>" not in html:
        fail(f"{page}: missing <title>")
    # a card that shows "Read →" but is not an anchor lies about being clickable
    for block in re.findall(r"<article[^>]*class=\"[^\"]*card[^\"]*\"[\s\S]*?</article>", html):
        if "Read" in block and "ledger" not in block:
            fail(f"{page}: non-link card advertises a Read affordance")


def main():
    missing = [s for s in SOURCES if not (ROOT / s).exists()]
    if missing:
        fail("missing source files: " + ", ".join(missing))

    # content hash over the sources, in a stable order
    h = hashlib.sha256()
    for s in SOURCES:
        h.update(s.encode())
        h.update((ROOT / s).read_bytes())
    stamp_hash = h.hexdigest()[:7]
    stamp_date = date.today().isoformat()

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    # pass 1 — copy and stamp without the size, to measure
    for s in SOURCES:
        dst = DIST / s
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / s, dst)
    for e in EXTRAS:
        if (ROOT / e).exists():
            shutil.copy2(ROOT / e, DIST / e)
    # tell Pages not to run Jekyll over the output
    (DIST / ".nojekyll").write_text("", encoding="utf-8")

    def stamp(size_kb=None):
        text = f"BUILD {stamp_hash} · {stamp_date}"
        if size_kb is not None:
            text += f" · {size_kb} kB"
        for p in PAGES:
            f = DIST / p
            html = f.read_text(encoding="utf-8")
            html = re.sub(r"<b>BUILD [^<]*</b>", f"<b>{text}</b>", html)
            f.write_text(html, encoding="utf-8")

    def transfer_kb():
        total = sum(len(gzip.compress((DIST / s).read_bytes(), 9)) for s in SOURCES)
        return round(total / 1024)

    stamp()
    size = transfer_kb()
    stamp(size)
    # the size is in whole kB, so a few bytes of stamp delta must not move it
    if transfer_kb() != size:
        stamp(transfer_kb())
        size = transfer_kb()

    print(f"\n  longtd.me → dist/\n")
    for p in PAGES:
        html = (DIST / p).read_text(encoding="utf-8")
        check(p, html)
        if f"BUILD {stamp_hash}" not in html:
            fail(f"{p}: build stamp was not written — is the footer <b>BUILD …</b> intact?")
        print(f"  ✓ {p}")

    raw = sum((DIST / s).stat().st_size for s in SOURCES)
    print(f"\n  build   {stamp_hash} · {stamp_date}")
    print(f"  raw     {raw / 1024:.1f} kB")
    print(f"  gzipped {size} kB")
    print(f"\n  serve:  python3 -m http.server 4321 --directory dist\n")


if __name__ == "__main__":
    main()
