# longtd.me

Personal profile site. Static HTML + CSS, no build step, no dependencies.

```
index.html              home
blog.html               blog index
blog/idempotency.html   article
styles.css              design tokens + all components
script.js               mobile nav toggle (the only JS on the site)
profile.json            served for real — the hero card's path resolves
build.py                stamps the build id and refuses to ship a broken page
dist/                   build output — this is what you deploy
design.pen              source design — open in Pencil
PROFILE-SPEC.md         design + copy spec
```

## Run locally

```bash
python3 -m http.server 4321
```

Then open `http://localhost:4321`. A server is required — pages link `/styles.css` root-relative,
so opening the files directly with `file://` will not pick up the stylesheet.

## Build

```bash
python3 build.py
```

No bundler — the site is hand-written static HTML and does not need one. The build does the two
things that must not be done by hand:

**Stamps the footer.** `BUILD 81ca4d7 · 2026-08-06 · 14 kB` is generated, never typed. The id is a
sha256 over the sources, not a commit sha, because this tree is not a git repo — arguably the better
choice for a static site, since the hash changes when the bytes change and anyone can recompute it
from what was served. The size is the real gzipped transfer weight. A stamp that goes stale inverts
the whole device, so it is derived or it is not there.

**Refuses to ship a page that contradicts itself.** Unbalanced divs, a leftover `DRAFT`, a missing or
duplicated `<h1>`, a missing `<title>`, or a non-link card advertising a `Read →` affordance all exit
non-zero. Verified by injecting each failure — the guards fire, they are not decoration.

Sources are never mutated; everything is written to `dist/`.

## Deploy — GitHub Pages

`.github/workflows/deploy.yml` runs `build.py` on every push to `main` and publishes `dist/`.
`dist/` is gitignored; CI builds it.

**The custom domain is not optional here.** The repo is `nhech/me`, so Pages would serve it at
`nhech.github.io/me/`. Every asset and link on the site is root-relative (`/styles.css`,
`/blog.html`), so under a subpath the whole site 404s. On `longtd.me` it serves at the root and
everything resolves. `CNAME` is in the repo root and the build copies it into `dist/`.

One-time setup:

1. **Settings → Pages → Source: GitHub Actions** (not "Deploy from a branch").
2. **Settings → Pages → Custom domain:** `longtd.me`, then tick **Enforce HTTPS** once the
   certificate is issued.
3. **DNS at your registrar** — apex `longtd.me`, four A records:

   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```

   Optionally `www` as a `CNAME` to `nhech.github.io`.

Other hosts work unchanged: build command `python3 build.py`, output directory `dist`.

## Why hand-written and not exported from Pencil

`export_html` from the .pen produces a faithful visual dump: nested `div`s with inline styles, a
hardcoded `width: 1440px`, zero media queries, spacer divs instead of margins, and no `nav`, `h1`,
`a` or landmark elements. It reproduces the picture but is neither responsive nor maintainable, and
it cannot be linked or crawled.

This code mirrors the same tokens by hand, so the design and the site stay in sync through
`styles.css` rather than through re-export.

## Design tokens

All in `:root` in `styles.css`. Change a value there and it propagates.

| | |
|---|---|
| Ground / surfaces | `--bg` `#0a0a0a`, `--surface` `#121214`, `--surface-2` `#17171b` |
| Text | `--text`, `--text-muted`, `--text-dim` |
| Accent | `--accent` `#f2542d` (+ `--accent-soft`, `--accent-tint`, `--accent-line`, `--on-accent`) |
| Borders | `--border`, `--border-strong` |
| Type | `--font-head` / `--font-body` Geist, `--font-mono` Geist Mono |
| Radius | `--r-sm` 4px chips & controls, `--r-lg` 8px cards |

**Responsive is fluid, not stepped.** Type and spacing use `clamp()` interpolating 390px → 1440px,
so tablet needs no separate rules. Media queries are reserved for layout changes only: nav at 768px,
grid columns at 700/900/1000px.

## Pill system — three sizes, no exceptions

| Class | Padding | Font | Height |
|---|---|---|---|
| `.chip` | 8/13 | 12 | 32 |
| `.btn--sm` | 10/18 | 13 | 37 |
| `.btn` | 13/22 | 15 | 45 |

Modifiers: `.chip--nested` (on cards), `.chip--accent`, `.chip--work`, `.chip--ghost`, `.chip--on`.

## Accessibility

Landmarks (`header`/`main`/`footer`/`nav[aria-label]`), one `h1` per page, `aria-expanded` +
`aria-controls` on the mobile toggle, `aria-current="page"` on the active nav link, visible
`:focus-visible` ring, and `prefers-reduced-motion` honoured. Verified: no horizontal overflow at
375px on any page; the code block scrolls inside its own box rather than pushing the page wide.

## Before going live

1. **`/cv.pdf`** — the hero "Download CV" link points at it; the file is not in the repo yet.
2. **OG image** — `og:image` is not set. Render a 1200×630 from the hero.
3. **Descriptions** for `fplayzone.com`, `studyinchina.io` and `dichthuatbaochau.com` are inferred
   from the domain names and need your correction.
4. **Self-host Geist** — currently a render-blocking Google Fonts request. Self-hosting from
   `vercel/geist-font` removes the third-party round-trip and restores the OpenType features the
   Google build strips.

If the blog grows past a handful of posts, move to Astro — it matches the stack you already run on
camnangocu.com and gives you markdown authoring. The tokens and components in `styles.css` port
across unchanged.
