import os
import pickle
from typing import Tuple

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC


def load_models(models_dir: str) -> Tuple[SVC, TfidfVectorizer]:
    with open(os.path.join(models_dir, "model.pkl"), "rb") as f:
        model = pickle.load(f)

    with open(os.path.join(models_dir, "vectorizer.pkl"), "rb") as f:
        vectorizer = pickle.load(f)

    return model, vectorizer
