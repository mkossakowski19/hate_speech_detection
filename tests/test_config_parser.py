from typing import Tuple

import pytest

from model_training.config_parser import ConfigParser
from model_training.hyperparams import SVMHyperparams, TFIDFHyperparams


@pytest.fixture(scope="module")
def filename() -> str:
    return "hyperparameters.yaml"


@pytest.fixture(scope="module")
def hyperparams(filename: str) -> Tuple[SVMHyperparams, TFIDFHyperparams]:
    return ConfigParser.load_hyperparams(filename)


def test_config_parser(hyperparams: Tuple[SVMHyperparams, TFIDFHyperparams]):
    svm_hyperparams, tfidf_hyperparams = hyperparams
    assert isinstance(svm_hyperparams, SVMHyperparams)
    assert isinstance(tfidf_hyperparams, TFIDFHyperparams)

    assert hasattr(svm_hyperparams, "C")
    assert hasattr(svm_hyperparams, "kernel")
    assert hasattr(svm_hyperparams, "class_weight")
    assert isinstance(svm_hyperparams.C, list)
    assert isinstance(svm_hyperparams.kernel, list)
    assert isinstance(svm_hyperparams.C[0], float)
    assert isinstance(svm_hyperparams.kernel[0], str)

    assert hasattr(tfidf_hyperparams, "max_df")
    assert hasattr(tfidf_hyperparams, "min_df")
    assert hasattr(tfidf_hyperparams, "max_features")
    assert isinstance(tfidf_hyperparams.max_features, list)
    assert isinstance(tfidf_hyperparams.max_df, list)
    assert isinstance(tfidf_hyperparams.min_df, list)
    assert isinstance(tfidf_hyperparams.max_features[0], int)
    assert isinstance(tfidf_hyperparams.max_df[0], float)
    assert isinstance(tfidf_hyperparams.min_df[0], int)
