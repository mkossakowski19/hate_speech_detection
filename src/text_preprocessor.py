from string import punctuation

from utils.stop_words import STOPWORDS


class TextPreprocessor:
    @staticmethod
    def remove_stopwords(text: str) -> str:
        tokens = text.split(" ")
        tokens = [token for token in tokens if token not in STOPWORDS]
        return " ".join(tokens)

    @staticmethod
    def remove_punctuation(text: str) -> str:
        return "".join(char for char in text if char not in punctuation)
