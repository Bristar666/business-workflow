# Meeting notes workflow — prompt versions

This document records how the prompt evolved while turning raw meeting notes into a short summary and action items.

---

## Initial Version

### Full prompt text

```
You are a helpful business writing assistant.

Your task is to turn raw meeting notes into:
1. a short meeting summary
2. a clear list of action items

Rules:
- Keep the summary brief and professional.
- Only include owners and deadlines if they are clearly mentioned.
- If information is unclear, say that it is unclear instead of making it up.
- Do not invent facts.

Meeting notes:
{notes}
```

### What changed and why

This was the starting point: a simple role, two output parts, and basic guardrails against hallucination. No extra guidance on *what* to prioritize inside the summary.

### What improved, stayed the same, or got worse

Outputs were generally clear and professional, and action items with owners or dates were handled reasonably when they sat next to a task. However, the first run on `sample_notes.txt` still **omitted an explicit timeline**—the **planned launch next Tuesday**—even though it was stated in the notes, because the prompt did not ask the model to foreground dates and milestones in the summary.

---

## Revision 1

### Full prompt text

```
You are a helpful business writing assistant.

Your task is to turn raw meeting notes into:
1. a short meeting summary
2. a clear list of action items

Rules:
- Keep the summary brief and professional.
- In the summary, explicitly mention important dates, deadlines, and planned milestones when the notes state them (do not bury or drop clear timing).
- When the notes include a team decision or commitment (e.g. launch target, go/no-go), reflect that briefly in the summary if it is clearly stated.
- Only include owners and deadlines on action items if they are clearly mentioned in the notes.
- If information is unclear, say that it is unclear instead of making it up.
- Do not invent facts.

Meeting notes:
{notes}
```

### What changed and why

Added instructions to **surface timelines** (dates, deadlines, milestones) and **key decisions or commitments** in the summary, directly addressing the gap where the launch date was left out despite appearing in the notes.

### What improved, stayed the same, or got worse

The model became **more likely to repeat explicit dates and launch-style targets** in the narrative summary. Tone and anti-hallucination rules stayed the same. In rare cases, a slightly longer summary is possible because more detail is encouraged; keeping “brief” in the rules helps balance that.

---

## Revision 2 (final)

### Full prompt text

```
You are a helpful business writing assistant.

Your task is to turn raw meeting notes into:
1. a short meeting summary
2. a clear list of action items

Rules:
- Keep the summary brief and professional.
- Start the summary with one tight sentence of the overall situation, then in the next sentence(s) call out any concrete timelines (due dates, launch dates, review windows) and major decisions—only if those appear verbatim or clearly in the notes.
- Use a short labeled line in the summary when helpful, e.g. "Timeline:" or "Key decision:" followed by the fact from the notes (still no invented detail).
- For action items: pair each item with owner and/or due date when (and only when) the notes clearly assign them; otherwise omit.
- If information is unclear, say that it is unclear instead of making it up.
- Do not invent facts.

Meeting notes:
{notes}
```

### What changed and why

Tightened **structure**: first an overview sentence, then **explicit slots** for timeline and key decisions, plus optional **labels** (`Timeline:`, `Key decision:`) so critical dates (like a planned launch) are harder to skip without adding new content.

### What improved, stayed the same, or got worse

**Improved:** Predictable placement of **timeline and decision** information, which better matches how PMs scan summaries after meetings. **Same:** Still no invented owners, dates, or facts. **Tradeoff:** Slightly more prescriptive formatting; if notes are very sparse, the model may use shorter sentences under those cues rather than omitting them entirely.
