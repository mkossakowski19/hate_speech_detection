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
        "Mateusz to mój syn.",
        "To jest zdanie testowe. \n 😀 😀 \r",
        "https://twitter.com/ to   adres @anon_acc"
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


def test_emoji_removing(text_examples: List[str], preprocessor: TextPreprocessor):
    result = preprocessor._remove_emojis(text_examples[2])
    assert "😀" not in result


def test_mentions_removing(text_examples: List[str], preprocessor: TextPreprocessor):
    result = preprocessor._remove_mentions(text_examples[3])
    assert "@anon_acc" not in result


def test_url_removing(text_examples: List[str], preprocessor: TextPreprocessor):
    result = preprocessor._remove_urls(text_examples[3])
    assert "https://twitter.com/" not in result


def test_special_character_removing(text_examples: List[str], preprocessor: TextPreprocessor):
    result = preprocessor._remove_special_characters(text_examples[2])
    assert "\n" not in result
    assert "\r" not in result


def test_redundant_spaces_removing(text_examples: List[str], preprocessor: TextPreprocessor):
    result = preprocessor._remove_redundant_spaces(text_examples[3])
    assert result == "https://twitter.com/ to adres @anon_acc"
