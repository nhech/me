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
docs/                   build output — Pages serves this, committed
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

No bundler — the site is hand-written static HTML and does not need one. Output goes to
**`docs/`**, which is committed. Run it before every commit that touches the site, or the footer
stamp goes stale.

The build does the two things that must not be done by hand:

**Stamps the footer.** `BUILD 81ca4d7 · 2026-08-06 · 14 kB` is generated, never typed. The id is a
sha256 over the sources — it has to exist before the commit does, and it changes exactly when the
served bytes change. The size is the real gzipped transfer weight.

**Refuses to ship a page that contradicts itself.** Unbalanced divs, a leftover `DRAFT`, a missing or
duplicated `<h1>`, a missing `<title>`, or a non-link card advertising a `Read →` affordance all exit
non-zero. Verified by injecting each failure — the guards fire, they are not decoration.

Sources are never mutated; everything is written to `docs/`.

## Deploy — GitHub Pages

Branch deploy, no CI. **Settings → Pages → Source: `Deploy from a branch` → `main` → `/docs`.**

An Actions-based deploy was tried first and abandoned: the workflow ran green, produced the
artifact and created the deployment, then sat in `deployment_queued` until GitHub timed it out and
cancelled it. Branch deploy has far fewer moving parts — no workflow, no `github-pages` environment,
no OIDC token exchange — and for a site this size the tradeoff (running `build.py` by hand) is
nothing.

**The custom domain is not optional.** The repo is `nhech/me`, so Pages would otherwise serve at
`nhech.github.io/me/`. Every asset and link is root-relative (`/styles.css`, `/blog.html`), so under
a subpath the whole site 404s. On `longtd.me` it serves at the root. `CNAME` lives in the repo root
and the build copies it into `docs/`, alongside a `.nojekyll` so Pages does not run Jekyll over the
output.

DNS is already pointed — apex `longtd.me` has four A records at GitHub's anycast CDN
(`185.199.108–111.153`) and `www` is a `CNAME` to `nhech.github.io`. Both must be **DNS only** in
Cloudflare, not proxied: with the orange cloud on, GitHub cannot complete the ACME challenge and
`Enforce HTTPS` never becomes available.

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
