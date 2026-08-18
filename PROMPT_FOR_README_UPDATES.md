# How to update the animated README — daily prompt

Every day, copy the **PROMPT** block below into any GenAI chat model (Claude, GPT,
Gemini, etc.), then:
1. Paste your **current `README.md` content** right after it.
2. Replace `{WHAT_I_DID_TODAY}` with a few honest bullet points of what actually
   happened today (even one line is fine on a slow day).
3. Take the full output the model gives you and overwrite `README.md` with it.

The prompt is self-contained — it doesn't need any other context to work correctly,
and it produces a full, ready-to-paste README every time.

---

## PROMPT (copy everything between the lines)

```
You are updating the animated "Daily Progress Log" section of a GitHub README.md
for a 4-person team competing in a classical-ML chest X-ray detection challenge
(no deep learning / no pretrained models allowed). I will paste my current
README.md content below, followed by what we did today.

Follow these rules exactly:

1. DO NOT touch anything outside the "## 📅 Daily Progress Log" section and its
   contents — leave the header banner, badges, and everything from "# Data ML —
   Submission" onward completely untouched, character for character.

2. Find the most recently expanded day (the one inside <details open>...</details>).
   Collapse it: change <details open> to <details>, and replace its full content
   with a ONE-LINE summary in this exact format, inserted as a new line directly
   below the <!-- PAST_DAYS_START --> marker (newest collapsed day goes first,
   i.e. right after the marker, pushing older ones down):

   - **Day {N} — {Date}:** {5-10 word summary of the single biggest impact that day}

   Keep every previously collapsed day exactly as it was — only ADD one new line,
   never rewrite or remove older ones.

3. Create a NEW <details open> block for today, placed where the old expanded
   block was (immediately after the "Updated once per day..." line, before the
   <!-- PAST_DAYS_START --> marker). Use this exact structure:

   <details open>
   <summary><b>🟢 Day {N} — {Date} — {short 3-6 word title for today}</b></summary>

   ![Day Banner]({BANNER_URL})

   **What we did:**
   - {bullet from today's update}
   - {bullet from today's update}
   - {more bullets as needed, based on what I give you}

   **Impact:** {1-2 sentences on why today's work actually matters for the
   project — not just a restatement of the bullets above}

   </details>

4. {BANNER_URL} must be a unique capsule-render.vercel.app banner URL, different
   in TYPE, COLOR, and ANIMATION from the banner used on the immediately
   preceding day (infer the previous day's banner from the README I pasted, if
   visible in the collapsed history, otherwise just pick freshly). Build it from:

   Base: https://capsule-render.vercel.app/api?type={TYPE}&color=0:{HEX1},100:{HEX2}&height=80&text=Day%20{N}&fontSize=28&fontColor=ffffff&animation={ANIM}

   Rotate TYPE through: rect, soft, slice, curve, cylinder, egg, rounded, blur
   Rotate ANIMATION through: fadeIn, blink, twinkling
   Rotate the color pair through (pick a different one each day, cycling back
   after all are used):
     1e3c72,2a5298   (deep blue)
     11998e,38ef7d   (teal-green)
     8e2de2,4a00e0   (violet)
     f7971e,ffd200   (amber)
     ee0979,ff6a00   (coral)
     00c6ff,0072ff   (sky blue)
     c31432,240b36   (crimson-dark)
     56ab2f,a8e063   (fresh green)

5. Increment the day number {N} by 1 from the highest day number currently in
   the README. Use today's real date for {Date}.

6. Output the ENTIRE updated README.md, start to finish, in a single markdown
   code block — not just the changed section. I will overwrite the file with
   your full output, so nothing before or after the Daily Progress Log section
   may be summarized, omitted, or altered.

Here is today's update:
{WHAT_I_DID_TODAY}

Here is my current README.md:
{PASTE_CURRENT_README_HERE}
```

---

## Notes

- The rotation lists (banner type / animation / color) are deliberately fixed so
  the model can't "forget" and repeat yesterday's exact banner — it just needs to
  pick the next unused one in the cycle.
- If a day is skipped, that's fine — the day counter still just increments by 1
  from whatever the last entry was; don't try to backfill missing days.
- Keep this file (`PROMPT_FOR_README_UPDATES.md`) in the repo root so any teammate
  can do the update, not just whoever wrote it originally.
