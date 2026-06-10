# Phase 5 — Interview Coaching (triggered by "I have an interview")

**Trigger:** the user reports an interview invitation.
**Inputs (read fully):** the matching record in `application-database.md` (which CV version went out, the angle, the verbatim gap language, what was deliberately not said), the documents sent, the posting, and `career-profile.md`. If no record exists, reconstruct one with the user first — coaching without it risks contradicting the application.
**Output:** a locked answer set and a **cheatsheet PDF** in the package style.

## §1 Frame the session

Establish: interview format (recruiter screen / hiring manager / panel / case), interviewer name+role if known, duration, language. Calibrate depth: a 30-min screen needs 6–8 questions and a 1-page sheet; a final round needs the full map and up to ~6 pages.

## §2 Build the question map

Generate the likely questions from four sources, then rank by probability × stakes:
1. The posting's musts (each must → at least one question)
2. The gaps the application conceded (each **will** come up — prepare the honest-bridge delivery, never a retraction)
3. The company/stage context (Market Researcher: recent news, funding, product, the interviewer's likely concerns)
4. The standard set for the format (motivation, exit stories, salary, "questions for us")

Classify each question by type — **Why** (motivation), **How** (behavioral/process), **What** (factual/technical), **What-if** (situational/case) — and make sure all four types are covered for the role's level.

## §3 The coaching loop (one question at a time)

For each question, in order:
1. **Ask it** exactly as an interviewer would. Tell the user to answer **out loud, spontaneously**, then type or dictate what they said.
2. **Feedback** on the spontaneous answer — three parts, honest: what worked / what hurt / what to change. Check four dimensions: content (evidence, numbers), structure (lead with the answer, then support), delivery (length, hedging, ending forward), and **consistency** (does it match the application and the agreed gap language?).
3. **Co-craft the ideal answer** with the user in 1–2 iterations — their words, tightened; not a script in the team's voice.
4. **Re-practice:** ask the question again; the user answers with the crafted version.
5. **Lock** when the user says it's locked or the team judges it solid. Then next question.

Continue until all questions are locked or the user calls it enough. Track locked/remaining visibly.

## §4 The salary question (always prepare it)

From the PRIVATE block: the floor stays in the user's head and is **never said**. Coach the standard mechanics: state the researched target range, express flexibility on total package, flip the question back, then stop talking. Prepare the "if pushed for one number" line and the "their band is below floor" line.

## §5 Produce the cheatsheet

Build from `assets/templates/cheatsheet-template.md`:
- Header: company · role · format · interviewer · the session's objective in one line
- Framing box: the 2–3 angles in order + hard rules (things never to say)
- The locked Q&A blocks: question → the crafted answer (bold the load-bearing phrases) → a `▸` delivery note (pacing, what to end on, what never to say)
- Power phrases with USE annotations (one line each, deploy-one-at-a-time instruction)
- The user's questions to ask, ranked
- **The one concrete ask** to land before hanging up
- Tone footer (one line)

Run the text-quality pass on all answer text. Render with `scripts/render_pdf.py --style cheatsheet`, check page count against the format (screen ≤2 pages), present the PDF + md.

## §6 After the interview

Prompt the user to report back; log outcome + lessons in the database record and Outcomes log the same day.
