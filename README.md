# job-search-ops

A Claude skill that runs your entire job search as a coordinated team of career experts: document intake, a structured career-profile interview, a master CV, per-posting fit assessment, tailored truth-only application documents as PDFs, an application database, and interview coaching that ends in a printable cheatsheet.

Everything in here was used in production on real applications before it was packaged.

## What it does — five phases

| Phase | Trigger | Output |
|---|---|---|
| **1 · Intake** | "Start my job search" | `document-inventory.md` — every career document processed into a fact inventory |
| **2 · Career interview** | "next" | `career-profile.md` — a structured interview (chronology, evidence mining, constraints, honest narratives) builds the single source of truth |
| **3 · Master CV** | "next" | `master-cv.md` — the comprehensive superset every tailored CV is cut from |
| **4 · Application loop** | paste any job posting | fit assessment (capability **and** preference scores, 1–10), apply/skip recommendation, tailored CV + cover letter as PDFs, a database record |
| **5 · Interview coaching** | "I have an interview" | question-by-question practice (answer → feedback → co-craft → lock), ending in a cheatsheet PDF |

## The doctrine (why you can trust its output)

- **Truth only.** Tailoring means selecting, ordering, and phrasing your real facts for a specific audience. The system never invents titles, inflates scope, or claims tools you don't have.
- **Honest-bridge framing.** Real gaps are named once, early, plainly — then outweighed with evidence. The exact gap wording is recorded and reused, so your story never drifts between CV, letter, and interview.
- **You decide and submit.** The team assesses and recommends — including recommending you *skip*. It never applies on your behalf.
- **Consistency enforced by data.** Every application's angle, document versions, and verbatim gap language go into the database; interview coaching reads that record so it never coaches you into contradicting your own application.
- **Private stays private.** Your compensation floor and deal-breaker reasoning inform the team's judgment and never appear in an outward document.

## Install

**Claude.ai:** Settings → Capabilities → Skills → upload the packaged `job-search-ops.skill`, and `humanaizer.skill` alongside it (claude.ai accepts one skill per upload, so the companion installs separately). For best results, run it inside a dedicated Project and save the canonical files it produces (`career-profile.md`, `master-cv.md`, `application-database.md`) into the project knowledge — that's how state persists between sessions.

**Claude Code / Cowork:** clone into your skills directory:

```
git clone https://github.com/davidsanz21/job-search-ops ~/.claude/skills/job-search-ops
```

**Recommended companion:** [`companion-skills/humanaizer/`](companion-skills/humanaizer/SKILL.md) — install it alongside. Every recruiter-facing text gets a silent humanization pass through it (a condensed fallback is bundled for installs without it).

## Use

```
"Start my job search"          → Phase 1
"next"                         → advance phases
{paste a job posting}          → fit assessment → apply/skip → documents
"They rejected me" / "Screen booked Friday"  → database update
"I have an interview with {company}"         → coaching → cheatsheet
```

## PDF rendering

`scripts/render_pdf.py` converts the Markdown documents to print-quality A4 PDFs (presets: `cv`, `letter`, `cheatsheet`). Inside Claude's sandbox it runs automatically. Locally:

```
pip install -r scripts/requirements.txt
python scripts/render_pdf.py examples/sample-cv.md --style cv -o out/cv.pdf
```

Best with the Lora and Liberation Sans fonts installed; falls back to Georgia/Arial. The script reports page count so the agent can enforce length discipline (CV ≤ 2–3 pages, letter ≤ 1) by restructuring content instead of shrinking type.

## What it deliberately does not do

- No auto-applying, no scraping job boards, no sending anything. Scouting automation is a known extension — by design it activates only when a search shifts from selective to volume mode, and it should never auto-apply either.
- No fabrication, ever. If a fact isn't in your profile, it doesn't ship.

## Repository layout

```
SKILL.md                      orchestrator: doctrine, team, state protocol, phase router
references/                   one procedure file per phase + humanizer fallback
assets/templates/             career profile, application database, cheatsheet templates
scripts/                      render_pdf.py + print stylesheets (cv / letter / cheatsheet)
examples/                     fully synthetic sample inputs and their rendered PDFs
companion-skills/humanaizer/  the text-humanization companion skill
```

All example data is synthetic. No real names, employers, or application records ship with this repo.

## License

MIT — see [LICENSE](LICENSE). Built by [David Sanz](https://github.com/davidsanz21).
