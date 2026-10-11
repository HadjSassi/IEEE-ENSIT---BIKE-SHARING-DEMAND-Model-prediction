import os
from pathlib import Path

import joblib
import streamlit as st

from __init__ import MODEL_FILE


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / MODEL_FILE


@st.cache_resource
def load_model(filepath: str | os.PathLike[str] = MODEL_PATH):
    model_path = Path(filepath)
    if not model_path.exists():
        raise FileNotFoundError(f"Model not found at: {model_path}")

    bundle = joblib.load(model_path)
    return bundle["model"], bundle["feature_cols"], bundle["metrics"]
