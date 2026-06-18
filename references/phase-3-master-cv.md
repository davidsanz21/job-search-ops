# Phase 3 — The Master CV

**Goal:** one comprehensive, sendable-quality CV that is the superset every tailored CV is cut from.
**Input:** `career-profile.md` (read it fully — always).
**Output:** `master-cv.md` (+ optional rendered PDF for the user's review).
**Advance gate:** user approves → Phase 4 unlocked; from now on the loop runs per posting.

## Procedure

1. **Pre-flight questions.** Before drafting, ask only what the profile doesn't settle: target headline / professional identity line, whether sensitive content (e.g., polarizing side projects) is default-on or default-off, contact details to print, photo/no-photo per target market norms.
2. **Draft the master CV** with these rules:
   - Reverse-chronological experience; every role gets scope line + outcome-led bullets (quantified, from Stage B/C evidence).
   - A skills/competencies block in the posting language of the user's field — terms recruiters actually search.
   - Education, credentials (expired ones labeled honestly), languages with working levels.
   - Career breaks appear with their agreed honest-bridge line from the profile — never an unexplained hole.
   - No self-assessment adjectives. No content that isn't traceable to the profile.
3. **Length:** the master CV may run long (3–4 pages) — it is the superset. Tailored CVs in Phase 4 are cut to ≤2–3 pages.
4. **Text-quality pass** (per SKILL.md) on the summary and all bullets — silently.
5. **Render** with `scripts/render_pdf.py --style cv` (style per `references/cv-design-guidelines.md`; pass `--footer "Full Name"` for the footer; eyeball a page-1 preview per §9) so the user sees the real artifact, present both `.md` and `.pdf`, and instruct the user to save `master-cv.md` to project knowledge.

## Structure skeleton

```markdown
**{Name}**
{Headline · positioning line}
{City/Country · email · phone · work-permit status if an asset}

## Professional summary
{4–6 lines, evidence-dense, zero adjectives-without-proof}

## Core competencies
{searchable terms, grouped, separated by ·}

## Professional experience
### {Role} — {Company} · {Mon YYYY – Mon YYYY}
*{one-line scope: portfolio, team, budget, geography}*
- {outcome-led bullet with number}
...

## Education
## Credentials & certifications
## Languages
## {Optional: Independent work / projects / leadership}
```
