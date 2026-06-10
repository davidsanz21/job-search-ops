# Phase 1 — Intake: collect and process every career document

**Goal:** get every potentially relevant document out of the user's drawers and into a structured inventory the team can reason from.
**Output:** `document-inventory.md` (canonical file).
**Advance gate:** user says "next" (or equivalent) → Phase 2.

## 1. The prompt

Open by asking the user to dump **everything**, explicitly listing categories so nothing is self-censored as "probably irrelevant":

- Current and old CVs / resumes (all versions, all languages)
- Degree certificates, academic transcripts, thesis grades
- Professional certificates and licenses (including expired ones — note expiry, don't discard)
- Employer reference letters / work certificates (e.g., German Arbeitszeugnisse — read the coded grading language if present)
- Recommendation letters, awards, performance records
- Language certificates
- Course completions, bootcamps, online credentials
- Portfolio links, publications, talks, side projects, volunteer leadership
- LinkedIn profile export or URL
- Anything else: internal praise emails, project one-pagers, patents

Tell the user: incomplete is fine; more can be added later; nothing uploaded will be used without their approval.

## 2. Processing

For **each** document:
1. Identify type, issuer, date, and language.
2. Extract the load-bearing facts: names, dates, titles, grades, scopes, numbers.
3. Flag anything notable: top-percentile grades, coded employer-reference language, expired credentials, gaps between documents, **contradictions** (dates that don't line up, titles that differ between CV and certificate).

Do not editorialize about quality yet — this phase is inventory, not strategy.

## 3. Output format — `document-inventory.md`

```markdown
# Document Inventory — {User Name}
> Generated {date}. Source documents listed below; facts extracted verbatim where possible.

## Inventory
| # | Document | Type | Issuer | Date | Key facts extracted | Flags |
|---|---|---|---|---|---|---|

## Contradictions & open questions
- {anything that needs clarification in the Phase 2 interview}

## Coverage gaps
- {periods, skills, or claims that no document supports — interview targets}
```

## 4. Close the phase

Present the file, instruct the user to save it to project knowledge, then say: the next step is the career-profile interview (Phase 2) — typically 30–60 minutes of focused questions — and they can start it by saying **"next"**.
