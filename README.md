<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=0:00c6ff,100:0072ff&height=200&section=header&text=DataML%20Challenge&fontSize=48&fontColor=ffffff&animation=fadeIn&desc=Chest%20X-Ray%20Multi-Condition%20Detection&descAlignY=75&descSize=18)

![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1200&color=00C6FF&center=true&vCenter=true&width=600&lines=Day+1+%E2%80%94+Repo+is+live%21;Classical+ML+only.+No+shortcuts.;Feature+engineering+is+the+whole+game.)

![Team](https://img.shields.io/badge/team-4_members-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/status-in_progress-yellow?style=for-the-badge)
![Rules](https://img.shields.io/badge/models-classical_ML_only-critical?style=for-the-badge)
![Event](https://img.shields.io/badge/event-Data_ML_2026-informational?style=for-the-badge)

</div>

---

## 📅 Daily Progress Log

*Newest day expanded with full detail; older days collapse to a one-line summary.
Updated once per day — see `PROMPT_FOR_README_UPDATES.md` for how this section is
regenerated.*

<details open>
<summary><b>🟢 Day 2 — Aug 16, 2026 — Real dataset loaded</b></summary>

![Day Banner](https://capsule-render.vercel.app/api?type=soft&color=0:11998e,100:38ef7d&height=80&text=Day%202&fontSize=28&fontColor=ffffff&animation=twinkling)

**What we did:**
- Loaded the full dataset into the repo: 4,484 training images into `data/train` and 1,122 test images into `data/test`
- Verified image filenames match the `Image Index` column in `train_labels.csv` (spot-checked, e.g. `00000013_005.png`, `00000013_026.png`)
- Confirmed folder item counts line up exactly with expectations (train count matches label row count)

**Impact:** All 4 members can now run the pipeline against real data instead of
placeholders — EDA, preprocessing, and feature work can start immediately with
no blockers.

</details>

<!-- PAST_DAYS_START -->
- **Day 1 — Aug 15, 2026:** Repo scaffolded to match submission template, roles + branching defined
<!-- New compressed one-line entries get inserted above this line, newest first -->
<!-- PAST_DAYS_END -->

---

---

# Data ML — Submission

*Fill this out and keep it current — this file (or a PDF version) is your official write-up.*

## 1. Team Details

| Field | Details |
|---|---|
| Team Name | codeX |
| Team Members (4) | 1. Abhinav Karthikeya  2. Sai Rahul Teja  3. Sai Srinivas  4. Prem Kumar Reddy |
| Team Lead (contact) | Abhinav — abhinavcolwork@gmail.com |
| GitHub Repository Link | https://github.com/Abhinav-1952/XRAY-TEAM-REPO |

## 2. Repository Structure

- `/code` — final notebook(s) and scripts. Must run end-to-end and reproduce reported results.
- `/predictions` — `predictions.csv`, in the exact format specified in Section 6.
- `/README.md` — this write-up.
- `/pitch_deck` — Final Round slide deck (only if selected).

## 3. Problem Understanding

*Write 3–5 sentences: what we're predicting (5-condition multi-label probability
output per chest X-ray), and why it matters.*

## 4. Exploratory Data Analysis (EDA)

*1–2 short paragraphs: key patterns, class imbalance (positive rates ranged ~5–17%
across the 5 conditions in our training data), data quality issues, and how they
shaped our approach. Reference charts in `/code/notebooks/01_eda.ipynb`.*

## 5. Approach & Methodology

### 5.1 Feature Engineering

*List each feature family we engineered and why — intensity/statistical, texture
(GLCM/LBP), edge/gradient (HOG/Canny), blob/shape (Nodule-targeted), symmetry
(left/right lung). One or two sentences of justification per family — see
`/code/src/features.py` for implementation.*

### 5.2 Model(s) Used

*Name the model(s), key hyperparameters, class-imbalance handling, and why we
chose them over alternatives we tried.*

## 6. Results

| Metric | Score | Notes |
|---|---|---|
| Mean AUROC (5 conditions) | | |
| Atelectasis AUROC | | |
| Effusion AUROC | | |
| Infiltration AUROC | | |
| Nodule AUROC | | |
| Pneumothorax AUROC | | |

Predictions file: `predictions/predictions.csv`, columns matching the test set's
`Image Index` column plus one probability column per condition.

## 7. Key Insight

*3–5 sentences: the ONE most surprising or valuable thing we found — this is what
we'd present in the Final Round if selected.*

## 8. Wildcard Challenges Attempted

| Challenge | Attempted? (Y/N) | Where to find it in the repo |
|---|---|---|
| Best Visualization | | |
| Most Interpretable Model | | |
| Fastest Inference Time | | |
| Best Handling of Messy/Incomplete Data | | |

## 9. Declaration

We confirm that this submission is original work completed by our team during the
official event window (Days 1–28), built solely on the officially released dataset,
and does not reuse pre-existing projects or another team's code.

*Team Lead name & signature/date*

---

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:0072ff,100:00c6ff&height=100&section=footer)

</div>
