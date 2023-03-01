from typing import Dict

import numpy as np
from sklearn.metrics import accuracy_score, f1_score


class TextClassificationEvaluator:
    def calculate_metrics(
        self, targets: np.ndarray, predictions: np.ndarray
    ) -> Dict[str, np.float64]:
        return {
            "accuracy": accuracy_score(targets, predictions),
            "f1_macro": f1_score(targets, predictions, average="macro"),
            "f1_micro": f1_score(targets, predictions, average="micro"),
        }
