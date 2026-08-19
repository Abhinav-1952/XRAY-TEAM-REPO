<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=0:00c6ff,100:0072ff&height=200&section=header&text=DataML%20Challenge&fontSize=48&fontColor=ffffff&animation=fadeIn&desc=Chest%20X-Ray%20Multi-Condition%20Detection&descAlignY=75&descSize=18)[cite: 1]

![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1200&color=00C6FF&center=true&vCenter=true&width=600&lines=Day+1+%E2%80%94+Repo+is+live%21;Classical+ML+only.+No+shortcuts.;Feature+engineering+is+the+whole+game.)[cite: 1]

![Team](https://img.shields.io/badge/team-4_members-blueviolet?style=for-the-badge)[cite: 1]
![Status](https://img.shields.io/badge/status-in_progress-yellow?style=for-the-badge)[cite: 1]
![Rules](https://img.shields.io/badge/models-classical_ML_only-critical?style=for-the-badge)[cite: 1]
![Event](https://img.shields.io/badge/event-Data_ML_2026-informational?style=for-the-badge)[cite: 1]

</div>

---

## 📅 Daily Progress Log[cite: 1]

*Newest day expanded with full detail; older days collapse to a one-line summary.[cite: 1]
Updated once per day — see `PROMPT_FOR_README_UPDATES.md` for how this section is[cite: 1]
regenerated.*[cite: 1]

<details open>
<summary><b>🟢 Day 3 — Aug 19, 2026 — Animation update matched</b></summary>[cite: 2]

![Day Banner](https://capsule-render.vercel.app/api?type=slice&color=0:8e2de2,100:4a00e0&height=80&text=Day%203&fontSize=28&fontColor=ffffff&animation=fadeIn)[cite: 2]

**What we did:**[cite: 2]
- Made the day 1 live animation as day 2 is live

**Impact:** Keeps the repository visual tracking fully consistent with our latest progress, ensuring the team stays aligned on our daily presentation standards.[cite: 2]

</details>

<!-- PAST_DAYS_START -->
- **Day 2 — Aug 16, 2026:** Loaded real dataset, verified environment, and wrote automated checks[cite: 1]
- **Day 1 — Aug 15, 2026:** Repo scaffolded to match submission template, roles + branching defined[cite: 1]
<!-- New compressed one-line entries get inserted above this line, newest first -->
<!-- PAST_DAYS_END -->

---

---

# Data ML — Submission[cite: 1]

*Fill this out and keep it current — this file (or a PDF version) is your official write-up.*[cite: 1]

## 1. Team Details[cite: 1]

| Field | Details |
|---|---|
| Team Name | codeX |
| Team Members (4) | 1. Abhinav Karthikeya  2. Sai Rahul Teja  3. Sai Srinivas  4. Prem Kumar Reddy |
| Team Lead (contact) | Abhinav — abhinavcolwork@gmail.com |
| GitHub Repository Link | https://github.com/Abhinav-1952/XRAY-TEAM-REPO |

## 2. Repository Structure[cite: 1]

- `/code` — final notebook(s) and scripts. Must run end-to-end and reproduce reported results.[cite: 1]
- `/predictions` — `predictions.csv`, in the exact format specified in Section 6.[cite: 1]
- `/README.md` — this write-up.[cite: 1]
- `/pitch_deck` — Final Round slide deck (only if selected).[cite: 1]

## 3. Problem Understanding[cite: 1]

*Write 3–5 sentences: what we're predicting (5-condition multi-label probability
output per chest X-ray), and why it matters.*[cite: 1]

## 4. Exploratory Data Analysis (EDA)[cite: 1]

*1–2 short paragraphs: key patterns, class imbalance (positive rates ranged ~5–17%
across the 5 conditions in our training data), data quality issues, and how they
shaped our approach. Reference charts in `/code/notebooks/01_eda.ipynb`.*[cite: 1]

## 5. Approach & Methodology[cite: 1]

### 5.1 Feature Engineering[cite: 1]

*List each feature family we engineered and why — intensity/statistical, texture
(GLCM/LBP), edge/gradient (HOG/Canny), blob/shape (Nodule-targeted), symmetry
(left/right lung). One or two sentences of justification per family — see
`/code/src/features.py` for implementation.*[cite: 1]

### 5.2 Model(s) Used[cite: 1]

*Name the model(s), key hyperparameters, class-imbalance handling, and why we
chose them over alternatives we tried.*[cite: 1]

## 6. Results[cite: 1]

| Metric | Score | Notes |
|---|---|---|
| Mean AUROC (5 conditions) | | |
| Atelectasis AUROC | | |
| Effusion AUROC | | |
| Infiltration AUROC | | |
| Nodule AUROC | | |
| Pneumothorax AUROC | | |

Predictions file: `predictions/predictions.csv`, columns matching the test set's
`Image Index` column plus one probability column per condition.[cite: 1]

## 7. Key Insight[cite: 1]

*3–5 sentences: the ONE most surprising or valuable thing we found — this is what
we'd present in the Final Round if selected.*[cite: 1]

## 8. Wildcard Challenges Attempted[cite: 1]

| Challenge | Attempted? (Y/N) | Where to find it in the repo |
|---|---|---|
| Best Visualization | | |
| Most Interpretable Model | | |
| Fastest Inference Time | | |
| Best Handling of Messy/Incomplete Data | | |

## 9. Declaration[cite: 1]

We confirm that this submission is original work completed by our team during the
official event window (Days 1–28), built solely on the officially released dataset,
and does not reuse pre-existing projects or another team's code.[cite: 1]

*Team Lead name & signature/date*[cite: 1]

---

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:0072ff,100:00c6ff&height=100&section=footer)[cite: 1]

</div>