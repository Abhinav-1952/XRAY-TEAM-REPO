# Chest X-Ray Multi-Condition Detection — Write-up

## 1. Problem understanding
_What we're predicting, why it's a multi-label problem, why accuracy alone is
misleading given class imbalance (5–17% positive rates)._

## 2. EDA findings
_Class balance, co-occurrence between conditions, what we actually saw reviewing
positive vs negative examples per condition, intensity variation across scans._

## 3. Feature engineering
For each feature family: what it is, why we chose it for these specific
conditions, and evidence it helped (ablation / per-feature AUROC).

### 3.1 Intensity / statistical features
### 3.2 Texture features (GLCM, LBP)
### 3.3 Edge / gradient features
### 3.4 Blob / shape features (Nodule)
### 3.5 Symmetry features (Effusion, Pneumothorax)

## 4. Model choice
_Which model(s) we tried, why we picked the final one, how we handled class
imbalance, how we tuned per-class thresholds._

## 5. Results
_Per-class AUROC / average precision on our held-out validation split, and any
notable failure modes per condition._

## 6. Limitations & what we'd try next
_Be honest — this is scored on clarity and reasoning, not just performance._
