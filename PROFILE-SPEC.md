# longtd.me — Personal Profile Spec

Design + copy spec for `design.pen`. **`design.pen` is the source of truth.**

Register: personal homepage, not a CV. Dark, minimal, large spacing, big type. Structure is carried by
whitespace and hairlines; boxes are used only where they earn it.

## Pages

| Frame | Node | Size |
|---|---|---|
| Home — Desktop | `k4zYI4` | 1440 × 5205 |
| Blog — Desktop | `VRGMi` | 1440 × 1360 |
| Blog Post — Desktop | `z1P6f` | 1440 × 1886 |
| Home — Mobile | `ZJUZX` | 390 × 7254 |
| Blog — Mobile | `T4Xrw` | 390 × 1995 |
| Blog Post — Mobile | `rDNnQ` | 390 × 1762 |

Nav, nav divider, footer rule and footer on every page are **`Copy` instances of the home page nodes**,
so a change to the home nav propagates rather than drifting.

### Blog — index
Header (eyebrow, 56px title, sub) + filter chips (`All` active in accent, then Backend / Architecture /
Blockchain / AI) + a 3 × 2 card grid, 336px tall. Card: tag chip + read time, title 20px, excerpt, then
`DRAFT` and `Read →` pinned to the bottom via `space_between`. All six posts are placeholders.

### Blog — post
760px reading column centred in the 1220 container. Back link → tag → 50px title → meta row
(`DRAFT · 8 MIN READ · TRỊNH DUY LONG`) → rule → body. Body elements: 19px lead paragraph, 17px body,
28px H2, a `surface` code block with 13.5px mono, and a pull-quote using a **left-only border**
(`strokeWidth: {left: 2}`) rather than a bar child — a `fill_container`-height bar inside a
`fit_content` parent collapses to zero. Ends with a `WRITTEN BY` block and an `All posts` button.

---

## Structure — home, 7 sections

| # | Section | Purpose |
|---|---------|---------|
| 1 | **Hero** | Name, role, one-line headline, personal intro, contact, `profile.json` card |
| 2 | **About** | "How I work" — three paragraphs of voice |
| 3 | **Core Expertise** | Six borderless editorial rows, hairline-separated |
| 4 | **Projects** | Nine square cards — work products + personal sites, tagged WORK / PERSONAL |
| 5 | **Stack** | One compact chip cloud |
| 6 | **Blog** | Three post cards + "All posts" |
| 7 | **Contact** | Email · LinkedIn · Location, then footer |

Nav: `longtd.me` · About · Projects · Blog · Contact · **Get in touch**.

### What was deliberately cut

The first build followed the uploaded brief literally and came out reading as a CV. These were removed
because they are resume apparatus, not profile content:

- **Stats strip** (5 metric columns) — the numbers now live in the hero intro instead.
- **Technical Timeline** (5 employers) — a personal profile does not need a work-history list. Employment
  context survives only where it attributes a product.
- **Featured Projects** as case studies (PROBLEM / ARCHITECTURE / IMPACT / STACK blocks) — collapsed into
  the square project cards.
- **Engineering Philosophy** (5 numbered essays) — the voice now sits in About.
- **Achievements** (8-item tick list, later a statement block) — redundant with the hero.
- **Tech Stack** as 8 labelled categories — collapsed to one chip cloud.
- **Education rail** — CV material.

Page height went 10504px → 5798px.

---

## Color system

| Token | Value | Use |
|---|---|---|
| `bg` | `#0A0A0A` | Page ground, continuous |
| `surface` | `#121214` | Cards, chips |
| `surface-2` | `#17171B` | Icon boxes, nested chips |
| `text` | `#FFFFFF` | Headings, values |
| `text-muted` | `#8A8A90` | Body copy |
| `text-dim` | `#5C5C63` | Micro-labels, metadata |
| `accent` | `#F2542D` | Primary action, eyebrows, keys, icons |
| `accent-soft` | `#FFC3AE` | WORK tag labels |
| `border` | `#EEF0F21A` | Hairlines, card edges |
| `border-strong` | `#EEF0F22E` | Secondary buttons |
| `warning` | `#D9A44C` | Reserved (no callouts remain on the page) |

**On the accent.** Sampled from the logo on the hoodie in your profile photo — raw pixels came back
`#C82D11`–`#D12B15` (avg `#BF311C`), then lifted to `#F2542D` because the photo reads dark against black
fabric and the raw value fails contrast on a `#0A0A0A` ground. At `#F2542D` the accent clears 5.2:1
against the page and 4.9:1 for dark label text inside the filled button — both AA.
`mirailabs.io` is a different company (Mirai Labs LLC, black 未来 mark), so it was not used as a source.
Swap `accent` in the .pen variables if you have the official brand hex.

WORK tags use `#F2542D14` fill on a `#F2542D40` hairline; the filled CTA uses `#1A0702` for its label.

## Typography

- **Headings + body:** Geist. **Labels, metadata, chips:** Geist Mono.
- Scale: `88` name · `56` contact · `44` section titles · `32` hero headline · `24/21/19` card and item
  titles · `17.5/16/15.5/14` body · `13/12.5/12/11/10.5` mono.
- Weights `600` headings, **`400` hero headline**, `400` body.
- Line height `1.0` name, `1.14` section titles, `1.36` hero headline, `1.6–1.72` body.
- Letter spacing `-3.8` name, `-1.6` section titles, `-0.9` headline, `+0.8→+1.4` mono eyebrows.

The hero headline is deliberately **light weight at 32px** against an 88px semibold name. Both were white
and near-bold in an earlier pass and competed for the same rank; dropping the headline to 400 puts the
name first and the statement second, which is the correct order on a personal profile.
- Body never below 14px; measure ~60–75 characters.

## Design tokens

- **Radius** `4` chips/controls, `8` cards.
- **Pill system — three sizes, no exceptions.** Every rounded label and button on the page resolves to one
  of these. Anything that does not is drift, not a decision.

  | Family | Padding | Font | Height | Used by |
  |---|---|---|---|---|
  | Chip | `[8, 13]` | 12 | 32 | hero badge, WORK/PERSONAL tags, tech chips in cards, stack cloud |
  | Button — small | `[10, 18]` | 13 | 37 | nav "Get in touch", "All posts" |
  | Button — large | `[13, 22]` | 15 | 45 | hero "Email me", "Download CV" |

  Before this pass the same tech chip rendered at `[5,10]`/11px inside project cards and `[8,13]`/12.5px in
  the stack cloud; the hero badge sat at `[8,15]`; and the two small buttons were `[10,18]` and `[11,18]`
  — a 2px difference on identical components. Pinning project **Card Top** to `height: 32` keeps the tag
  row aligned now that chips are taller.
- **Container** 1220px inside a 1440px frame, gutters `110`.
- **Section rhythm** `104` between every section; `40` header→content. Sections carry top padding only
  (bottom `0`), so the gap is owned by one value and cannot drift. Nav divider → hero is `88`, tighter on
  purpose so the hero reads as attached to the nav rather than as another section. Hero intro → the
  `profile.json` card is `60`.

  This landed at 104 after two corrections. The first pass ran 132 with a 228 outlier between hero and
  about; that outlier was real and got fixed, but the rhythm was then pushed to 160, which was the wrong
  direction — at this type scale the sections read as drifting apart rather than as one page. 104 against
  a 40 header spacer gives a 2.6:1 ratio, which is enough to group without stranding each section on its
  own screen. Expertise rows sit at `36` top/bottom with the first row's top padding zeroed, so the
  section title does not stack its spacer on top of the first row's padding.
- **Grid** `24` between cards, `72` between text columns, `8` between chips.
- **Square cards** `390.67 × 391` — `(1220 − 2×24) ÷ 3`. Change the gutter and the height must follow.
- **Card padding `30`** on every card — project, blog and contact. Blog and contact were `28` for a while;
  all cards are the same 391px width, so a 2px drift meant their text columns started at different x.
- **Project card internals.** Card top is pinned to `height: 30` so the WORK/PERSONAL tag sits at the same
  y whether or not the card carries an arrow button — without it, the four link-less work cards rode 6px
  higher than their neighbours. Descriptions are `fixed-width-height` at `69` (three lines at 14/1.64) so
  every card body is exactly 152px: titles align across a row and tech chips bottom-align. Left to
  `fixed-width`, two-line descriptions pushed their titles 23px lower than three-line ones in the same row.
- **Stroke** always 1px, `strokeAlignment: "inner"`.
- **Shadow / gradient / glass** none.

---

## Section notes

**Hero** — Badge (`SENIOR BACKEND ENGINEER · HANOI, VIETNAM · 9+ YEARS`) → Name (88px) → headline (32px,
weight 400) → intro → `Email me` (filled) + `Download CV` (outlined) → inline email/LinkedIn →
`profile.json` readout card (window chrome, two columns of `key → value` mono rows: role, focus, stack /
built, scale, since).

There is **no separate role line** — an earlier pass had an accent mono `Senior Backend Engineer · 9+ years`
directly under the name, which repeated the badge verbatim two lines above it. Role, location and years
now live in the badge only, taking the hero from five stacked text blocks to four.
*Animation:* stagger children 40ms, 12px rise, 400ms ease-out.

**About** — "How I work.", three paragraphs at 880px measure: how you think (failure modes first), how you
build (storage per access pattern, boundaries by data ownership), how you lead.

**Core Expertise** — no cards. Six self-contained cells in a **2 × 3 grid**, hairline between rows,
80px gutter. Each cell stacks accent index → 24px title → 15.5px description, so the description sits
directly under the title it belongs to.

An earlier pass used six full-width rows with the title in a fixed 430px left column and the description
in the right. Titles are short, so that column ran ~40% empty on every row and left a visible void down
the middle of the section, with each description reading as detached from its title. The 2 × 3 grid
removes both problems and stays borderless, so it still contrasts with the Projects card grid below —
two card grids back to back read as a catalogue, the CV failure mode this page avoids.
*Hover:* title → `accent`.

**Projects** — nine square cards, 3×3. Card top: WORK/PERSONAL tag, plus an arrow-link button **only on
cards that have a public URL**. Card bottom: title, one-line description, up to three tech chips. WORK
tags use accent tint, PERSONAL uses a plain hairline. *Hover:* lift 2px, arrow translates up-right.

**Link map — wire these at build time.** Pencil's `href` property is documented on `TextStyle` but this
build silently drops it, so the targets cannot be baked into the .pen. Make the whole card the anchor:

| Card | Target |
|---|---|
| camnangocu.com | `https://camnangocu.com` |
| bepluataybac.vn | `https://bepluataybac.vn` |
| fplayzone.com | `https://fplayzone.com` |
| studyinchina.io | `https://studyinchina.io` |
| dichthuatbaochau.com | `https://dichthuatbaochau.com` |
| Mirai Wallet · Telegram Mini App Wallet · Maple & Foxy Chat · Chainverse Wallet | none — arrow removed |

Add `target="_blank" rel="noopener"` on the external five.

**Stack** — greedy-wrapped chip cloud, three rows, no categories, no container.

**Blog** — header with "All posts" button, three post cards. **All three posts are placeholders** marked
`DRAFT — PLACEHOLDER`; replace before publishing.

**Contact** — "Say hello." centered, three cards: Email, LinkedIn, Location.

---

## Responsive

Desktop and mobile are both **drawn**. Tablet is the interpolation and is not drawn — build it by
following the middle column.

| | Desktop ≥1280 (drawn) | Tablet 768–1279 | Mobile 390 (drawn) |
|---|---|---|---|
| Gutters | 110 | 56 | 20 |
| Section rhythm | 104 | 88 | 72 |
| Header → content | 40 | 32 | 28 |
| Name | 88 | 60 | 42 |
| Hero headline | 32 | 26 | 21 |
| Section title | 44 | 34 | 28 |
| Body | 17.5 / 16 | 16 / 15.5 | 15 / 14 |
| Nav | inline links + CTA | inline links + CTA | brand + hamburger |
| Hero CTAs | side by side | side by side | stacked, full width |
| `profile.json` card | 2 columns | 2 columns | 1 column, 6 rows |
| Expertise | 2 × 3 borderless | 2 × 3 | 1 col, hairline between |
| Projects | 3 × 3 square 391px | 2 col square | 1 col, `fit_content` |
| Stack cloud | 3 chip rows | 5 rows | 9 rows |
| Blog | 3 across, 336px | 2 across | 1 col, `fit_content` |
| Contact | 3 across | 3 across | 1 col, icon beside text |
| Article column | 760 centred | 640 centred | full width, 20 gutter |
| Code block | 13.5px mono | 12.5px | 10.5px + shortened lines |

**Cards stop being square below 768.** The 391px height is `(1220 − 48) ÷ 3`; at mobile width that ratio
is meaningless, so height becomes `fit_content` and the bottom-pinned foot row is dropped in favour of
normal flow.

**Mobile keeps the same content.** Nothing is cut for small screens — the nine project cards, all six
expertise areas and the full stack list are all present. Only the code block's line content is shortened,
because 49-character lines wrap badly at 306px and a wrapped code sample reads as broken.

Honour `prefers-reduced-motion`: drop rises, keep 150ms opacity fades.

## SEO

- **Title** `Trịnh Duy Long — Backend Engineer`
- **Description** `Backend engineer in Hanoi. Nine years building digital wallets, payment systems, NFT marketplaces and real-time AI platforms.`
- **Keywords** backend engineer, digital wallet, payments, NFT marketplace, DeFi, NestJS, Node.js, Solidity, Kubernetes, Vietnam
- **OpenGraph** `og:type=profile`, `og:url=https://longtd.me`, `og:image` 1200×630 rendered from the hero
- **Twitter** `summary_large_image`
- **Structured data** `Person` (name, jobTitle, Hanoi VN, email, sameAs LinkedIn, knowsAbout) + `WebSite` + `Blog`

---

## Still open

1. **Blog posts** — all three cards are placeholders. Titles were drafted from your expertise; replace
   with real posts, or point "All posts" at an external platform.
2. **Work-product links** — Mirai Wallet, Telegram Mini App Wallet, Maple & Foxy Chat and Chainverse
   Wallet have no public URL, so their arrow buttons were removed. If any of them has a landing page or
   store listing, send it and the affordance goes back.
3. **Descriptions for fplayzone.com, studyinchina.io, dichthuatbaochau.com** — still inferred from the
   domain name. Stack is confirmed (NestJS / Next.js / PostgreSQL).
4. **Maple / Foxy Chat and Chainverse metrics** — the ~150K users / 10M+ transactions figure is applied
   to the platform overall in the hero. Confirm whether it belongs to a specific product.
5. **Copy sign-off** — About is written in your voice from your CV and working style, but drafted, not
   quoted. Read it and make it yours.

---

## Research pass — applied 2026-08-06

Five parallel research agents (terminal aesthetics, dev-tool brand language, engineer portfolios,
observability UI, technical type/colour), 69 devices surveyed, then synthesised into a change list.

**Finding:** the design was not under-decorated, it was under-*disciplined*. Monospace ran in 7
semantic roles across 18 selectors; the accent fired ~10 times in the hero viewport alone;
letter-spacing used 6 different positive values for the same job. Nine of the ten changes were
subtraction.

### Applied

| # | Change | Where |
|---|---|---|
| 1 | `DRAFT` placeholders and non-link "Read →" cards deleted; blog became a **ledger** (`date │ title │ tag │ read`), only real posts | home + blog index, both breakpoints |
| 2 | macOS traffic lights removed; chrome is now `path` ⟷ `6 keys · updated 2026-08`; **`/profile.json` is served for real** and the path label links to it | hero |
| 3 | Faux-bold wordmark fixed — `.brand` asked for weight 600 while the font request only loaded Mono 400/500, so the browser was synthesising it | global |
| 4 | Accent budget cut from ~10 to **7 elements page-wide**; `--accent-soft` now carries all accent text under 15px (`#F2542D` at 11px is under-contrast on `#0a0a0a`) | global |
| 5 | Mono/sans contract written into the stylesheet and enforced: mono = machine-authored strings, sans = anything a human wrote. Nav labels and small buttons moved to sans | global |
| 6 | Contact `LOCATION` was a `<div>` wearing the same card styling as two real `<a>` siblings → demoted to a hairline row | contact |
| 7 | Card hover: `transform: translateY(-2px)` → `box-shadow` ring. No layout shift, no repaint, and the `prefers-reduced-motion` special-case became unnecessary | global |
| 8 | Tracking collapsed from 6 px values to two em tokens, `--track-caps` / `--track-mono`, so tracking now scales with the `clamp()` sizes instead of drifting across breakpoints | global |
| 9 | Numbers given scope and period (`across the wallet platforms, since 2021`); bio de-duplicated (`9+ years` appeared 3× in one viewport); `since` → `2016`; `tabular-nums` on every numeric run | hero |
| 10 | Footer right → build stamp `BUILD a3f19c2 · 2026-08-06`. **Must be generated at build time** — a hardcoded date going stale inverts the device | global |
| — | `Download CV` demoted from a hero button to a mono link | hero |

### Deliberately not done

Dot grid · ambient glow · noise overlay · gradient ring · a second terminal element · `$ whoami` ·
blinking caret · typewriter effect · count-up numbers · `STATUS: ONLINE` · fabricated uptime ·
GitHub contribution graph · shields.io badges · ⌘K palette · skill-bar percentages · 90-cell
activity strip.

Two reasons, both from the research. On a page built from 1px hairlines and flat fills, one glow
makes everything else look under-designed. And inventing telemetry is fatal for someone whose pitch
is being careful with numbers that represent money — it contaminates the real figures beside it.

### Design frames

`Home — Desktop v2 (research)`, `Blog — Desktop v2 (research)` and `Home — Mobile v2 (research)`
hold the applied version; the original v1 frames are kept alongside for comparison.

---

## v3 — layout pass (shipped to code)

`Home — Desktop v3 (layout)` keeps v2's colour and type discipline but changes the structure.
`styles.css` and `index.html` now match it.

| Section | v1 / v2 | v3 |
|---|---|---|
| Hero | one column, `profile.json` card full width below | **two columns**, `minmax(0,1fr) 452px`, card in the right rail. Collapses at 900px — below that a 452px sidebar squeezes the statement past a readable measure |
| Core Expertise | 2 × 3 borderless | unchanged — a vertical timeline was tried and cut: it put two dense sections back to back and the rail was itself a loud device |
| Projects | 9 equal squares | **bento on a 6-column grid** — large tiles span 4, half tiles span 3, default 2. Work products take the large tiles; the hierarchy is the point, not the unevenness |

Measured against the design at 1440: hero `704 + 452`, bento widths
`805 · 391 · 391 · 805 · 391 · 391 · 391 · 598 · 598`.

### Accent, restored on request

The research cut accent to 4 marks; it was then deliberately expanded back. Orange now appears on
**37 elements** (v2: 7). Section eyebrows, the terminal full stop on every section title, the
`01`–`06` markers, expertise icons, eight core stack chips, the active nav link, badge and footer dots.

One research rule was kept because it is measurable rather than aesthetic: **accent text below 15px
uses `--accent-soft` (`#FFC3AE`)**, since `#F2542D` at 11–12px with wide tracking on `#0a0a0a` lands
around APCA Lc 62 against a Lc 75 target. Full-strength `#F2542D` is reserved for things that are
large or solid — the 44px full stops, icons, dots, and the filled CTA.

### Titles

The name is off the page but stays in the `<title>` and structured data — a `<title>` is not visible
on the page, so it does not conflict with leading on the statement, and dropping the name there would
lose every search for it.

| Page | Title |
|---|---|
| Home | `Trịnh Duy Long — Backend Engineer` |
| Blog index | `Blog — Trịnh Duy Long` |
| Article | `<post title> — Trịnh Duy Long` |

`og:site_name` carries `longtd.me` on all three, so the brand still appears in link previews
alongside the name.
