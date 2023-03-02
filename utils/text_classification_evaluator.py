from typing import Dict

import numpy as np
from sklearn.metrics import accuracy_score, f1_score


class TextClassificationEvaluator:
    def calculate_accuracy(self, targets: np.ndarray, predictions: np.ndarray):
        return accuracy_score(targets, predictions)

    def calculate_f1_macro(self, targets: np.ndarray, predictions: np.ndarray):
        return f1_score(targets, predictions, average="macro")

    def calculate_f1_micro(self, targets: np.ndarray, predictions: np.ndarray):
        return f1_score(targets, predictions, average="micro")

    def calculate_metrics(
        self, targets: np.ndarray, predictions: np.ndarray
    ) -> Dict[str, np.float64]:
        return {
            "accuracy": self.calculate_accuracy(targets, predictions),
            "f1_macro": self.calculate_f1_macro(targets, predictions),
            "f1_micro": self.calculate_f1_micro(targets, predictions),
        }
