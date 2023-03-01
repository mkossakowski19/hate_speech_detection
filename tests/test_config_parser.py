import pytest

from utils.config_parser import ConfigParser


@pytest.fixture(scope="module")
def filename() -> str:
    return "hyperparameters.yaml"


def test_config_parser(filename: str):
    result = ConfigParser.load_hyperparams(filename)
    assert isinstance(result, dict)
    assert "model_hyperparams" in result.keys()
    assert "vectorizer_hyperparams" in result.keys()
