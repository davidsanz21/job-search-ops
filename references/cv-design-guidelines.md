# CV House Style — Design Guidelines

**Status: canonical.** Every CV PDF this skill renders follows this specification. When asked to render, regenerate, or restyle any CV, read this file first and follow it exactly. Do not re-derive the look from a screenshot or memory — the values below and `scripts/styles/cv.css` are the single source of truth. If a render doesn't match this spec, the render is wrong, not the spec.

This file exists because the style drifted three times when it lived only in memory: heading treatment, header spacing, and bold-emphasis density each broke and had to be rediscovered. That must not happen again.

---

## 1. The canonical artifacts (use these, don't reinvent)

- **`scripts/styles/cv.css`** — the CV stylesheet. Source of truth for every value. Never eyeball-rebuild it.
- **`scripts/render_pdf.py`** — the markdown→HTML→PDF engine (strips metadata/build-notes, splits role/date lines, tags the identity block, applies the per-preset stylesheet). Three presets: `cv`, `letter`, `cheatsheet`.

**To render any CV:**
```
python scripts/render_pdf.py INPUT.md --style cv -o OUTPUT.pdf
# add the candidate's name to the footer (optional):
python scripts/render_pdf.py INPUT.md --style cv -o OUTPUT.pdf --footer "Jane Doe"
```
If the environment lacks these files, recreate the CSS from §3–§7 below exactly, then render.

---

## 2. The look in one paragraph

Clean, dense, single-column, A4. Serif headings in deep navy; sans-serif body in near-black. A large serif name, an italic serif subtitle directly beneath it, then a compact contact line. Section headings are navy serif with a thin full-width rule under them. Role headings are navy serif with the date right-aligned on the same line in small grey sans. Bullets are em-dash prefixed, tight. Load-bearing terms are **bold**, which renders navy — this emphasis is part of the design, not optional (see §8). Footer is centered grey. Target density: a focused CV fits 2 pages; a portfolio-heavy one may run 3.

---

## 3. Design tokens (exact values)

| Token | Value | Used for |
|---|---|---|
| Navy (primary) | `#14213d` | headings, name, bold text, links |
| Body text | `#222` | all body copy |
| Muted | `#444` | contact line |
| Subtitle / scope italic | `#555` | subtitle, `em` scope lines |
| Date / secondary | `#777` | role dates |
| Rule under headings | `#9aa6b6` | section-heading underline |
| Bullet dash / faint | `#888` | em-dash marker |
| Footer | `#999` | page footer |
| Heading font | `'Lora','Georgia',serif` | h1/h2/h3, name, subtitle |
| Body font | `'Liberation Sans','Helvetica Neue',Arial,sans-serif` | everything else |

Fonts degrade gracefully: if Lora is unavailable, Georgia; if Liberation Sans, Arial. Install Lora + Liberation Sans for the intended look.

## 4. Type scale (points)

| Element | Size | Weight | Notes |
|---|---|---|---|
| Name | 23pt | 600 | serif navy, letter-spacing −0.3px |
| Subtitle | 11pt | normal | serif italic, grey `#555` |
| Section heading (h2) | 13.5pt | 600 | serif navy + full-width rule |
| Role heading (h3) | 10.5pt | 600 | serif navy |
| Body | 9.2pt | normal | line-height 1.34 |
| Contact line | 8.8pt | normal | line-height 1.45, grey |
| Role date | 8.3pt | normal | sans, grey, right-aligned |
| Table | 8.6pt | — | — |
| Footer | 7.5pt | — | centered grey |

**Spanish (and other verbose-language) renders** may tighten body to ~9.0pt / line-height 1.32 to absorb the extra length (≈15% longer than English) without spilling a page. Pass `--lang es`; the engine applies the tighter `cv_es` preset automatically. EN uses 9.2 / 1.34. This is the only language divergence permitted.

## 5. Page & spacing

- A4, margins `1.25cm 1.4cm 1.3cm`.
- Identity block bottom margin 8px; name→subtitle 1px; subtitle→contact 5px. **The name and subtitle are `display:block` — they must NOT also carry trailing line breaks, or the spacing double-stacks** (this was the "wide gap" bug). The renderer strips the redundant `<br>`; preserve that behavior.
- Section heading (h2): margin `11px 0 4px`, 2px padding above its 1px rule.
- Role heading (h3): margin `8px 0 1px`.
- Bullets: `margin-bottom 2px`, hanging indent 14px, em-dash via `li::before`.
- `page-break-after: avoid` on all headings; `page-break-inside: avoid` on list items — never let a heading orphan at a page foot or a bullet split.

## 6. Structural rules

- **Single column.** No sidebars, no two-column layouts, no photo, no icons, no color bars or filled bands. The only color is navy text and the grey hairline rules.
- **Identity block order:** Name / subtitle (role positioning line) / contact line (city · email · phones · GitHub where applicable) / citizenship line (where applicable).
- **Role headings carry a right-aligned date.** Format the markdown as `### Role — Company · Mon YYYY – Mon YYYY`; the engine splits on the final ` · ` and right-aligns the date. Keep the date after the last ` · `.
- **Scope line** under a role goes in italics (`*European supplier industrialization · Battery Pack · Drive Unit*`).
- **Footer** is automatic (centered, "CV · n / m", or "<name> · CV · n / m" when `--footer "<name>"` is passed).

## 7. Markdown header convention (all CVs)

Every CV `.md` starts with this exact structure so the engine strips it cleanly and the version never drifts:

```
<!-- CV METADATA — internal, not rendered
     lane: {AI | Industrial (general) | Bitcoin | Master}
     language: {EN | ES}
     version: (version tracked by filename)
     last updated: {YYYY-MM-DD}
-->

> **Build note (internal — stripped on render).** {targeting notes, page target, etc.}

---

**Full Name**
{subtitle / positioning line}
{city · email · phones · github where applicable}
{citizenship line where applicable}

---

## {first section}
```

**Version lives in the filename only** (`CV_..._EN_AI_v6.md`), never in the document body — a version number in the H1 or title drifts from the filename and is the bug that started this. The metadata comment and build-note are stripped on render; the engine handles `<!-- -->`, leading `>` blockquotes, and `---` rules automatically.

## 8. Bold-emphasis policy (the rule that was missing)

Bold renders navy and is a load-bearing part of the visual hierarchy — **not decoration**. Apply it consistently across all language versions of the same CV. (A defect to avoid: shipping an ES file with ~8 bold terms against the EN's ~29 — that asymmetry breaks the hierarchy.)

**Bold these:** employer names; quantified outcomes (e.g. **31% across 4 lines**, **~$180K/yr**, **12 suppliers**); credentials and ratings; headline skills/tools; language level; role/leadership titles in the activities section; the first 2–4 words of a strong bullet that names the action.

**Don't bold:** connective prose, full sentences, or so much that nothing stands out. Target ~25–30 bold spans on a full CV. When producing or editing a non-English CV, mirror the English file's emphasis onto the equivalent terms — same concepts, same weight.

## 9. Render-and-verify protocol (mandatory)

A successful exit code is not proof of a correct render. After rendering, **always** generate a low-DPI page-1 preview and look at it before delivering:
```
pdftoppm -png -r 130 -f 1 -l 1 OUTPUT.pdf preview
```
Check: name is the first visible element (no leaked metadata/build-note), subtitle present and italic, section rules full-width, dates right-aligned, bold terms showing navy, page count sane (focused CV ≤ 2–3 pp). For non-English, also confirm accents render and emphasis matches the English twin. If anything is off, fix the CSS/markdown — never ship "close enough."

## 10. Known failure modes (caught before; watch for these)

1. **Leaked header** — metadata comment or build-note renders as a giant H1. Cause: engine not stripping `<!-- -->` / `>` / `---`. The current engine handles all three; if you rewrite it, preserve this.
2. **Wide gap after name/subtitle** — block elements carrying redundant `<br>`. The engine strips `</strong><br />` and `</span><br />`; preserve that.
3. **Non-English missing navy emphasis** — bold pattern not mirrored from the English file. See §8.
4. **Heading style drift** — underlines vs bands vs rules. Canonical is a thin full-width rule (`#9aa6b6`, 1px) under navy serif headings. No filled bands.
5. **Page bloat** — over-spacing pushing a 2-page CV to 3. Check line-height and element margins against §4–§5 before assuming the content is too long.
