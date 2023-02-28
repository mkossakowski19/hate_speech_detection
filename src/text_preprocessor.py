from string import punctuation
import re

from utils.stop_words import STOPWORDS


class TextPreprocessor:
    def _remove_stopwords(self, text: str) -> str:
        tokens = text.split(" ")
        tokens = [token for token in tokens if token not in STOPWORDS]
        return " ".join(tokens)

    def _remove_punctuation(self, text: str) -> str:
        return "".join(char for char in text if char not in punctuation)

    def _remove_urls(self, text: str) -> str:
        return re.sub(r"\b(https?://\S+)\b", "", text)

    def _remove_emojis(self, text: str) -> str:
        pass

    def preprocess(self, text: str) -> str:
        text = text.lower()
        text = self._remove_stopwords(text)
        text = self._remove_urls(text)
        text = self._remove_punctuation(text)
        return text
