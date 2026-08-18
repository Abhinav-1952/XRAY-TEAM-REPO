"""
Feature extraction, organized by family so each is easy to justify
independently in the write-up.

Owners: Texture/Edge lead (B), Shape/Symmetry lead (C)
"""
import numpy as np
import cv2
from skimage.feature import graycomatrix, graycoprops, local_binary_pattern, hog, blob_log


# ---------------------------------------------------------------------------
# A. Intensity / statistical features
# ---------------------------------------------------------------------------
def intensity_features(img: np.ndarray, mask: np.ndarray | None = None) -> dict:
    pixels = img[mask > 0] if mask is not None else img.flatten()
    return {
        "intensity_mean": float(np.mean(pixels)),
        "intensity_std": float(np.std(pixels)),
        "intensity_skew": float(_skew(pixels)),
        "intensity_kurtosis": float(_kurtosis(pixels)),
    }


def _skew(x):
    x = x.astype(np.float64)
    m = x.mean()
    s = x.std() + 1e-8
    return np.mean(((x - m) / s) ** 3)


def _kurtosis(x):
    x = x.astype(np.float64)
    m = x.mean()
    s = x.std() + 1e-8
    return np.mean(((x - m) / s) ** 4) - 3


# ---------------------------------------------------------------------------
# B. Texture features (GLCM, LBP)
# ---------------------------------------------------------------------------
def glcm_features(img: np.ndarray, distances=(1, 3), angles=(0, np.pi / 4)) -> dict:
    glcm = graycomatrix(img, distances=list(distances), angles=list(angles),
                         levels=256, symmetric=True, normed=True)
    out = {}
    for prop in ("contrast", "homogeneity", "energy", "correlation"):
        out[f"glcm_{prop}"] = float(np.mean(graycoprops(glcm, prop)))
    return out


def lbp_features(img: np.ndarray, P: int = 8, R: int = 1) -> dict:
    lbp = local_binary_pattern(img, P, R, method="uniform")
    hist, _ = np.histogram(lbp, bins=np.arange(0, P + 3), density=True)
    return {f"lbp_bin_{i}": float(v) for i, v in enumerate(hist)}


# ---------------------------------------------------------------------------
# C. Edge / gradient features
# ---------------------------------------------------------------------------
def edge_features(img: np.ndarray) -> dict:
    edges = cv2.Canny(img, 50, 150)
    edge_density = float(np.mean(edges > 0))
    hog_feats = hog(img, orientations=9, pixels_per_cell=(32, 32),
                     cells_per_block=(2, 2), feature_vector=True)
    return {
        "edge_density": edge_density,
        "hog_mean": float(np.mean(hog_feats)),
        "hog_std": float(np.std(hog_feats)),
    }


# ---------------------------------------------------------------------------
# D. Blob / shape features (targeted at Nodule)
# ---------------------------------------------------------------------------
def blob_features(img: np.ndarray, mask: np.ndarray | None = None) -> dict:
    img_norm = img.astype(np.float64) / 255.0
    blobs = blob_log(img_norm, min_sigma=2, max_sigma=10, num_sigma=5, threshold=0.05)
    if mask is not None and len(blobs):
        keep = [b for b in blobs if mask[int(b[0]), int(b[1])] > 0]
        blobs = np.array(keep) if keep else np.empty((0, 3))
    return {
        "blob_count": int(len(blobs)),
        "blob_mean_radius": float(np.mean(blobs[:, 2]) * np.sqrt(2)) if len(blobs) else 0.0,
    }


# ---------------------------------------------------------------------------
# E. Symmetry features (needs lung segmentation to split left/right)
# ---------------------------------------------------------------------------
def symmetry_features(img: np.ndarray, mask: np.ndarray) -> dict:
    h, w = img.shape
    mid = w // 2
    left = img[:, :mid][mask[:, :mid] > 0]
    right = img[:, mid:][mask[:, mid:] > 0]
    if left.size == 0 or right.size == 0:
        return {"symmetry_mean_diff": 0.0, "symmetry_std_diff": 0.0}
    return {
        "symmetry_mean_diff": float(abs(left.mean() - right.mean())),
        "symmetry_std_diff": float(abs(left.std() - right.std())),
    }


# ---------------------------------------------------------------------------
# Combine all families into one feature vector for a single image
# ---------------------------------------------------------------------------
def extract_all_features(img: np.ndarray, mask: np.ndarray) -> dict:
    feats = {}
    feats.update(intensity_features(img, mask))
    feats.update(glcm_features(img))
    feats.update(lbp_features(img))
    feats.update(edge_features(img))
    feats.update(blob_features(img, mask))
    feats.update(symmetry_features(img, mask))
    return feats
