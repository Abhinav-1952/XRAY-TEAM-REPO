"""
End-to-end training: raw images -> features -> fitted model -> saved to models/.

Owner: Modeling & Validation lead
Run: python src/train.py
"""
import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from tqdm import tqdm

from preprocessing import preprocess
from features import extract_all_features

DATA_DIR = "data"
TRAIN_IMG_DIR = os.path.join(DATA_DIR, "train")
LABELS_CSV = os.path.join(DATA_DIR, "train_labels.csv")
MODEL_OUT = "models/model.joblib"
LABEL_COLS = ["Atelectasis", "Effusion", "Infiltration", "Nodule", "Pneumothorax"]


def build_feature_table(df_labels: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for image_id in tqdm(df_labels["Image Index"], desc="Extracting features"):
        path = os.path.join(TRAIN_IMG_DIR, image_id)
        pre = preprocess(path)
        feats = extract_all_features(pre["image"], pre["mask"])
        feats["Image Index"] = image_id
        rows.append(feats)
    return pd.DataFrame(rows)


def main():
    df_labels = pd.read_csv(LABELS_CSV)
    feat_df = build_feature_table(df_labels)

    df = feat_df.merge(df_labels, on="Image Index")
    feature_cols = [c for c in feat_df.columns if c != "Image Index"]

    X = df[feature_cols].values
    y = df[LABEL_COLS].values

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf = MultiOutputClassifier(
        RandomForestClassifier(n_estimators=300, class_weight="balanced", random_state=42)
    )
    clf.fit(X_train, y_train)

    val_probs = np.array([est.predict_proba(X_val)[:, 1] for est in clf.estimators_]).T
    aucs = [roc_auc_score(y_val[:, i], val_probs[:, i]) for i in range(len(LABEL_COLS))]
    for name, auc in zip(LABEL_COLS, aucs):
        print(f"{name}: AUROC = {auc:.3f}")
    print(f"Mean AUROC: {np.mean(aucs):.3f}")

    os.makedirs("models", exist_ok=True)
    joblib.dump({"model": clf, "feature_cols": feature_cols}, MODEL_OUT)
    print(f"Saved model to {MODEL_OUT}")


if __name__ == "__main__":
    main()
