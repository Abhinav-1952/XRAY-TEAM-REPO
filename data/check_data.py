import pandas as pd
import os

df = pd.read_csv("data/train_labels.csv")
missing = [f for f in df["Image Index"] if not os.path.exists(f"data/train/{f}")]
print(len(missing), "missing files")