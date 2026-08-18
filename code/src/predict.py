"""
End-to-end prediction: raw test images -> features -> predictions.csv.

Owner: Modeling & Validation lead
Run: python src/predict.py
"""
import os
import joblib
import numpy as np
import pandas as pd
from tqdm import tqdm

from preprocessing import preprocess
from features import extract_all_features

DATA_DIR = "data"
TEST_IMG_DIR = os.path.join(DATA_DIR, "test")
MODEL_PATH = "models/model.joblib"
OUT_CSV = "predictions/predictions.csv"
LABEL_COLS = ["Atelectasis", "Effusion", "Infiltration", "Nodule", "Pneumothorax"]


def main():
    bundle = joblib.load(MODEL_PATH)
    clf, feature_cols = bundle["model"], bundle["feature_cols"]

    image_ids = sorted(os.listdir(TEST_IMG_DIR))
    rows = []
    for image_id in tqdm(image_ids, desc="Extracting test features"):
        path = os.path.join(TEST_IMG_DIR, image_id)
        pre = preprocess(path)
        feats = extract_all_features(pre["image"], pre["mask"])
        feats["Image Index"] = image_id
        rows.append(feats)

    feat_df = pd.DataFrame(rows)
    X = feat_df[feature_cols].values

    probs = np.array([est.predict_proba(X)[:, 1] for est in clf.estimators_]).T

    out = pd.DataFrame({"Image Index": feat_df["Image Index"]})
    for i, name in enumerate(LABEL_COLS):
        out[name] = probs[:, i]

    out.to_csv(OUT_CSV, index=False)
    print(f"Saved predictions to {OUT_CSV}")


if __name__ == "__main__":
    main()
