# Phase 2 — The Career-Profile Interview

**Goal:** extract everything relevant that the documents *don't* say, and assemble the single source of truth.
**Input:** `document-inventory.md` + the source documents.
**Output:** `career-profile.md` built on `assets/templates/career-profile-template.md`.
**Advance gate:** user confirms the profile section by section → Phase 3 on "next".

## Interview principles

1. **One question at a time.** Never send a wall of questions. If the platform supports clickable multiple-choice options, use them for closed questions (constraints, preferences, ratings) and free text for stories.
2. **Adaptive, not scripted.** Every question is generated from what Phase 1 found — confirm what documents suggest, fill what they omit, resolve what they contradict.
3. **Evidence-first.** Push every achievement toward a number: money, time, volume, headcount, percentage, geography. "Improved supplier quality" is worthless; "cut defect escapes ~40% across 8 suppliers in 6 countries" is a CV bullet. When the user can't quantify, ask: *"What would your manager have said you changed?"* or *"What was true after you that wasn't true before?"*
4. **Reflect and confirm.** Close every stage with a 3–5 line summary the user corrects or approves before moving on.
5. **The user controls pace.** "Next" forces advance; "skip" skips a question; the interview can resume in a later session (state lives in the partially built profile — deliver it for saving even if incomplete).

## Stage structure

### Stage A — Synthesis & gap map (no questions yet)
Present a short read-back: "Here's what your documents establish… here's what they don't tell me." List the open questions by stage. This earns trust and shows the interview has a reason.

### Stage B — Chronological deep-dive
Per role, oldest → newest:
- Scope numbers: team size, budget, portfolio, geography, who they reported to.
- 2–4 quantified achievements (mine with situation → action → measurable result).
- The hardest problem they solved there; one failure and what it taught them.
- **Why they left** — verbatim, honest version first. (The outward framing is built later, in Stage E.)

### Stage C — Evidence mining
Revisit every strong claim from Stage B and the documents, and push for the number, the artifact, or the named outcome. Also collect: tools/systems actually used (and depth: daily driver vs. touched once), methodologies certified vs. practiced, languages with honest working level.

### Stage D — Constraints & preferences
- **Hard constraints** (violations = automatic deal-breaker in Phase 4): location/relocation stance, travel ceiling, earliest start, legal/visa status, compensation floor, structural musts (e.g., minimum cash share of comp).
- **Soft preferences**: remote model, company stage and culture, industry pulls and repulsions, role shapes that energize vs. drain, anti-patterns in postings they want auto-flagged.
- Mark compensation floor/target and any sensitive reasoning **PRIVATE**.

### Stage E — Narratives (the honest-bridge workshop)
For every career break, exit, demotion, pivot, or visible oddity: draft the **honest-bridge line** with the user — the true version, stated once, plainly, then outweighed. Write the agreed wording into the profile verbatim; Phase 4 and 5 reuse it word-for-word so the story never drifts.

### Stage F — Differentiators
Side projects, communities, unusual skill combinations, languages, leadership outside work — the material that separates two otherwise equal CVs. Probe for things the user dismisses as hobbies; operators often undersell production-grade personal work.

### Stage G — Assembly & review
Fill `assets/templates/career-profile-template.md`. Walk the user through it **section by section** for confirmation (quick yes/fix per section, not a re-read of everything). Deliver the file; instruct the user to save it to project knowledge.

## Question-design quick reference

| Need | Question pattern |
|---|---|
| Quantify | "Roughly how much / how many / how often — even a defensible range?" |
| De-vague | "What did that look like on a normal Tuesday?" |
| Failure | "Tell me one that went wrong. What did it cost, what changed after?" |
| Exit | "If your closest colleague told me why you really left, what would they say?" |
| Preference | Closed options + an 'other' field |
| Calibrate skill | "Rate yourself 1–10 against people who do this professionally — then tell me the evidence for that number." |
