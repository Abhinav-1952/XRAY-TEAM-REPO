# Team Workflow

Four people, one repo, four weeks. This is the process — follow it so the Week 2
checkpoint shows real, distributed, ongoing work rather than a last-minute merge.

## 1. Roles (rotate ownership, not exclusivity — everyone can touch anything)

- **A — EDA & Preprocessing:** class balance, visual review of positives/negatives per
  condition, intensity distributions, image normalization, lung segmentation.
- **B — Texture/Edge Features:** GLCM, LBP, HOG, edge density — mainly feeds
  Infiltration/Pneumothorax signal.
- **C — Shape/Symmetry Features:** blob detection (Nodule), left/right symmetry
  (Effusion/Pneumothorax), depends on A's segmentation output.
- **D — Modeling & Validation:** multi-label model setup, class-imbalance handling,
  cross-validation, threshold tuning, metrics reporting.

Everyone contributes to the write-up section for the feature family they built —
nobody should be explaining someone else's feature choices secondhand at the final review.

## 2. Branching model

- `main` — always working, always reproducible. Never commit broken code here.
- One branch per feature/task: `feature/glcm-texture`, `feature/lung-segmentation`,
  `feature/blob-nodule`, `model/gradient-boosting-baseline`, etc.
- Open a PR into `main` when a branch is working, even if incomplete — self-merge is
  fine for a 4-person team, but the PR description should say what you tried and what
  the result was. This *is* your process evidence for the checkpoint.
- Rebase/pull `main` before starting new work each session to avoid painful merges later.

## 3. Commit habits (this is graded, don't skip it)

- Commit after every meaningful session, not once a week. A dozen small honest commits
  beats two huge ones.
- Write commit messages that describe *what changed and why* —
  `add GLCM contrast/energy features, +0.03 AUROC on Infiltration in local val`
  beats `update`.
- Commit failed/abandoned attempts too, with a note on why they didn't help. The
  checkpoint explicitly rewards visible unfinished attempts over a repo that only shows
  what worked.

## 4. Cadence

| When | What |
|---|---|
| Weekly sync (pick a day) | 20 min: what shipped, what's blocked, what's next |
| Days 1–3 | A drives EDA + preprocessing skeleton; everyone reviews the EDA notebook together |
| Days 4–7 | B & C prototype feature families in parallel on their own branches |
| ~Week 2 checkpoint | Merge in-progress work to `main` before the checkpoint date — a
  clean, current `main` is what gets reviewed |
| Week 2–3 | D integrates features into `train.py`, runs first validation pass, reports
  back per-class AUROC so B/C know which features are actually pulling weight |
| Week 3–4 | Feature pruning, model tuning, threshold tuning, finalize `predict.py` |
| Final days | Write-up — each person writes the section for their feature family |

## 5. Code review basics

- Before merging your own PR, make sure `src/train.py` still runs end-to-end from a
  clean clone — a change that only works "on my machine with my notebook state" breaks
  reproducibility for the whole team.
- If you touch someone else's function, ping them — don't silently change the meaning
  of a feature they're planning to justify in the write-up.

## 6. Daily update ritual (do this every single day, even short days)

The event runs Aug 15 – Sept 13 (Days 1–30). Consistency across all 28 working days
is what the checkpoint and the "not a last-minute dump" rule are checking for — a
5-minute update on a slow day beats silence.

**Every day, whoever worked that day should:**
1. `git pull` before starting (avoid stale-branch surprises).
2. Do the work on their branch.
3. Commit with a real message — even "explored wavelet features, didn't beat GLCM
   baseline, keeping notes in notebook" counts as progress.
4. Push the branch. Doesn't need to be merged same day.
5. Drop one line in the team chat: what you did, what's next, anything blocking you.

**Weekly (pick a fixed day/time), all 4 together:**
- 15–20 min sync: merge open PRs, resolve conflicts together, re-plan the coming week.
- Update `reports/writeup_draft.md` with anything worth keeping — don't leave the
  write-up for the last week, it's easiest to write while the reasoning is fresh.
- Check `README.md` Section 6 (Results) against your latest validation run so it
  never goes stale for more than a week.

**Mapped to the actual timeline:**

| Phase | Dates | Daily focus |
|---|---|---|
| Week 1 | Aug 15–21 | Data loading, EDA, first preprocessing pass |
| Weeks 2–3 | Aug 22–Sep 4 | Feature engineering (parallel per family), Wildcard attempts |
| ~Week 2 checkpoint | mid-way through Weeks 2–3 | `main` should be current and reviewable |
| Week 4 | Sep 5–11 | Model tuning, threshold tuning, finalize predictions |
| Final days | Sep 12–13 | Polish `README.md`, freeze repo, prep pitch deck if selected |

## 7. Keeping it original (Section 9 declaration matters)

- Every feature function in `code/src/features.py` should be something a teammate
  actually wrote and can explain line-by-line — not pasted from a tutorial/Kaggle
  notebook without understanding it. If you adapt an idea from a paper or blog post
  (e.g. "GLCM for texture" is a well-known technique), that's fine — cite it in the
  write-up — but the code and the specific feature choices should be yours.
- Don't reuse another team's repo, notebook, or feature set, even if you know them.
- Keep your own commit history as evidence: a feature that was clearly built
  incrementally (several commits, some dead ends) is much stronger proof of original
  work than one that appears in a single commit fully formed.
- If you genuinely didn't write a helper snippet yourselves (e.g. a boilerplate
  plotting function from documentation), say so in a code comment — it costs nothing
  and protects you against an originality challenge later.

## 8. Hard boundary — read this before you experiment

If anyone wants to sanity-check a ceiling using a CNN or pretrained model, do it in a
throwaway environment completely outside this repo. Never commit it, never push it to
any branch, never leave it commented out in a notebook. Checked at every stage means
every stage, including your scratch work.
