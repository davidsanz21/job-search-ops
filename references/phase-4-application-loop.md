# Phase 4 — The Application Loop (runs once per job posting)

**Trigger:** the user pastes a job description / link, or asks "should I apply to this?"
**Inputs (read fully, every time):** `career-profile.md`, `master-cv.md`, and the posting. If a link is given and web access exists, fetch the posting; otherwise ask for the pasted text.
**Outputs on "apply":** tailored CV (md + PDF), cover letter (md + PDF), application notes, and an appended record in `application-database.md`.
**Outputs on "skip":** a skip record with reasons. A skip is a completed, successful run of this loop.

## §1 Requirement extraction

Decompose the posting into:
- **Musts** (hard requirements) / **Nices** (preferred)
- **Conditions:** location/remote policy, travel, salary if stated, contract type, start date
- **Red flags** (Market Researcher): vague scope, responsibility lists for three jobs in one, "wear many hats" at corporate pay, reposted-for-months signals, mismatched seniority/comp, culture euphemisms

## §2 Fit assessment — two scores, one recommendation

Score against the profile with evidence, not vibes. Both scores are the **team's consensus**.

**Capability fit (1–10):** *Is the user the candidate this posting describes?*
- **9–10** — every must met with direct evidence; most nices too. The CV writes itself.
- **7–8** — all musts met, some via adjacent-but-defensible evidence; minor nice-gaps.
- **5–6** — one real must-gap that an honest-bridge can plausibly carry; rest solid.
- **3–4** — multiple must-gaps; would need inflation to look fit. (Inflation is banned, so this is a skip unless the channel is unusually warm.)
- **1–2** — wrong profile. Skip.

**Preference fit (1–10):** *Does this role fit the life the user told us they want?*
- Start from soft preferences (industry pull, role shape, culture, remote model).
- **Deal-breaker gate:** any hard-constraint violation (Stage D) caps the score at 3 and flips the default to **skip**, stated plainly. The user may consciously override; record the override.

**Output format (always this block):**

```
FIT ASSESSMENT — {Company} · {Role}
Capability fit: X/10 — {one-line reason}
Preference fit: Y/10 — {one-line reason}
Strengths (evidenced): …
Gaps (named honestly): …
Deal-breakers / conditions check: …
Red flags in posting: …
Team recommendation: APPLY / SKIP — {reasoning}
```

Then ask the user for the decision. Never start drafting before they say apply.

## §3 The tailored CV

Start from `master-cv.md`, then:
- **Retarget the framing layer:** headline, summary, and competencies speak this posting's language (mirror its exact terminology where truthful — that is ATS alignment, not inflation).
- **Select and reorder:** lead with the experience this role cares about; cut what it doesn't (the master CV exists so cutting is safe).
- **Per-bullet check:** every kept bullet earns its place against §1 musts.
- **Honest-bridge:** the relevant gap line from the profile appears where natural (usually the letter; on the CV only if its absence would look evasive).
- **Allowed operations:** select, reorder, emphasize, rephrase, quantify. **Banned:** invent, inflate, rename titles, stretch dates, claim unlisted tools.
- ≤2–3 pages. Version-label it (`CV_{Company}_{Role}_v1`).

## §4 The cover letter

- One page. A **narrative thread**, not modular paragraphs: why this company, the why behind the career facts, the gap named once and outweighed, a concrete ask (a conversation), in the posting's language and register.
- If the posting asks for something else (a 30-day plan, a short note, specific subject line) — **follow its instructions exactly** instead of defaulting to a letter.

## §5 Finalize and deliver

1. Run the **text-quality pass** (SKILL.md) on CV summary/bullets and the full letter — silently.
2. Render both via `scripts/render_pdf.py` (`--style cv`, `--style letter`); check reported page counts; restructure if over.
3. Present the files **plus application notes**: channel advice (referral vs. portal), timing, who to address, what to expect next, and any posting-specific instruction the user must follow when submitting.

## §6 The database append (never skip this)

Append to `application-database.md` (create from `assets/templates/application-database-template.md` if missing): index row + full record — role substance, conditions, both fit scores, decision, documents sent (exact versions), **angle/strategy**, **gap language used (verbatim)**, **deliberately not said**, interview watch-points, status log opened. For skips: a skip record with reasons.

Deliver the updated database file and remind the user to save it — this file is what makes Phase 5 trustworthy.

**Status updates:** whenever the user reports movement ("rejected", "they replied", "screen booked"), update the record's status log and the Outcomes log the same day, and deliver the updated file. When outcomes accumulate, the Career Strategist reviews patterns (response rate by angle, which gap framings draw replies) — without over-updating on small samples.
