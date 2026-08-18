"""
Image loading and preprocessing for the chest X-ray challenge.

Owner: EDA & Preprocessing lead
"""
import cv2
import numpy as np


IMG_SIZE = 512  # pick a size, justify it in the write-up, keep it consistent everywhere


def load_image(path: str) -> np.ndarray:
    """Load an X-ray as grayscale."""
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Could not read image: {path}")
    return img


def resize_image(img: np.ndarray, size: int = IMG_SIZE) -> np.ndarray:
    return cv2.resize(img, (size, size), interpolation=cv2.INTER_AREA)


def normalize_intensity(img: np.ndarray) -> np.ndarray:
    """CLAHE histogram equalization to reduce exposure/contrast variation
    between machines/scans."""
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(img)


def segment_lung_field(img: np.ndarray) -> np.ndarray:
    """Rough lung-field segmentation via Otsu thresholding + largest
    connected components. Returns a binary mask same size as img.

    NOTE: this is intentionally simple. Document its failure modes in the
    write-up rather than treating it as ground truth.
    """
    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    n_labels, labels, stats, _ = cv2.connectedComponentsWithStats(thresh, connectivity=8)
    if n_labels <= 1:
        return np.ones_like(img, dtype=np.uint8) * 255
    # keep the largest non-background component(s)
    largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
    mask = (labels == largest).astype(np.uint8) * 255
    return mask


def preprocess(path: str) -> dict:
    """Full pipeline for one image. Returns the processed image plus a
    lung mask, ready for feature extraction."""
    img = load_image(path)
    img = resize_image(img)
    img_eq = normalize_intensity(img)
    mask = segment_lung_field(img_eq)
    return {"image": img_eq, "mask": mask}
