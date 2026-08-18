# Dev Setup & Internal Notes

This file is for the team's own reference while building — it is NOT the submission
write-up. The submission write-up judges actually read is `README.md` at the repo
root (filled from the official submission template).

Classical ML pipeline (no deep learning / no pretrained models) predicting per-image
probabilities for 5 conditions: **Atelectasis, Effusion, Infiltration, Nodule, Pneumothorax**.

## Team

| Member | Role | Owns |
|---|---|---|
| _name_ | EDA & Preprocessing lead | `notebooks/01_eda.ipynb`, `src/preprocessing.py` |
| _name_ | Texture/Edge Features lead | GLCM, LBP, HOG feature families in `src/features.py` |
| _name_ | Shape/Symmetry Features lead | Blob detection, lung segmentation, symmetry features |
| _name_ | Modeling & Validation lead | `src/train.py`, `src/predict.py`, metrics, threshold tuning |

See `CONTRIBUTING.md` for how we work together, branch, and review each other's code.

## Setup

```bash
python -m venv venv
source venv/bin/activate       # venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Data

Drop the challenge data in here (already gitignored, do NOT commit raw images):

```
data/
├── train/              # training images
├── test/               # test images (no labels)
└── train_labels.csv    # training labels
```

## Running the pipeline end-to-end

Run these from the **repo root** (paths inside the scripts assume that):

```bash
python code/src/train.py      # extracts features from data/train, trains model, saves to models/
python code/src/predict.py    # extracts features from data/test, loads model, writes predictions/predictions.csv
```

## Repo layout (matches the official submission template)

```
xray-team-repo/
├── README.md                # ← THE SUBMISSION WRITE-UP judges read (filled template)
├── DEV_SETUP.md              # this file — internal dev notes, not graded directly
├── CONTRIBUTING.md           # team workflow, branching, review process
├── requirements.txt
├── .gitignore
├── data/                     # gitignored — raw images never committed
│   ├── train/
│   ├── test/
│   └── train_labels.csv
├── code/                     # ← required "/code" folder per submission template
│   ├── notebooks/
│   │   ├── 01_eda.ipynb
│   │   ├── 02_feature_prototyping.ipynb
│   │   └── 03_model_experiments.ipynb
│   └── src/
│       ├── preprocessing.py  # loading, resizing, normalization, lung segmentation
│       ├── features.py       # feature extraction functions, organized by family
│       ├── train.py          # end-to-end: raw images -> trained model
│       └── predict.py        # end-to-end: raw images -> predictions/predictions.csv
├── predictions/               # ← required "/predictions" folder
│   └── predictions.csv        # generated, not hand-edited — matches test ID column
├── pitch_deck/                # ← required "/pitch_deck" folder, used only if selected for finals
├── models/                    # saved fitted models
└── reports/
    └── writeup_draft.md       # working draft — polish this into README.md before submitting
```

## Rules reminder (zero tolerance)

No CNNs, no pretrained models, no learned feature extractors — anywhere in this repo,
at any stage, including scratch branches and commented-out code.
