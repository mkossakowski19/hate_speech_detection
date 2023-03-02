from typing import Tuple

import numpy as np
import pytest

from utils.text_classification_evaluator import TextClassificationEvaluator


@pytest.fixture(scope="module")
def sample_targets_and_predictions() -> Tuple[np.ndarray, np.ndarray]:
    return np.array([0, 2, 0, 1, 1, 1, 1]), np.array([1, 2, 0, 0, 1, 2, 1])


@pytest.fixture(scope="module")
def evaluator() -> TextClassificationEvaluator:
    return TextClassificationEvaluator()


def test_text_classification_evaluator(
    sample_targets_and_predictions: Tuple[np.ndarray, np.ndarray],
    evaluator: TextClassificationEvaluator,
):
    metrics = evaluator.calculate_metrics(
        sample_targets_and_predictions[0], sample_targets_and_predictions[1]
    )
    assert "accuracy" in metrics.keys()
    assert "f1_macro" in metrics.keys()
    assert "f1_micro" in metrics.keys()
    np.testing.assert_almost_equal(metrics["accuracy"], 0.5714285)
    np.testing.assert_almost_equal(metrics["f1_macro"], 0.5793650)
    np.testing.assert_almost_equal(metrics["f1_micro"], 0.5714285)
