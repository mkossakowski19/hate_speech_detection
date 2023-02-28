import itertools
from string import punctuation
from typing import List

import pytest

from src.text_preprocessor import TextPreprocessor
from utils.stop_words import STOPWORDS


@pytest.fixture(scope="module")
def text_examples() -> List[str]:
    return [
        "Ja jestem ojcem Mateusza.",
        "Mateusz to mój syn."
    ]


@pytest.fixture(scope="module")
def preprocessor() -> TextPreprocessor:
    return TextPreprocessor()


def test_stopwords_removing(text_examples: List[str], preprocessor: TextPreprocessor):
    results = [preprocessor._remove_stopwords(text) for text in text_examples]
    results_tokenized = [text.split(" ") for text in results]
    result_tokens = list(itertools.chain.from_iterable(results_tokenized))
    for stopword in STOPWORDS:
        assert stopword not in result_tokens


def test_punctuation_removing(text_examples: List[str], preprocessor: TextPreprocessor):
    results = [preprocessor._remove_punctuation(text) for text in text_examples]
    results_tokenized = [text.split(" ") for text in results]
    result_tokens = list(itertools.chain.from_iterable(results_tokenized))
    for p in punctuation:
        assert p not in result_tokens
