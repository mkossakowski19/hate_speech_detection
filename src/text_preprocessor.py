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
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002702-\U000027B0"  # other miscellaneous symbols
                                   u"\U000024C2-\U0001F251"
                                   "]+", flags=re.UNICODE)
        return re.sub(emoji_pattern, "", text)

    def _remove_mentions(self, text: str) -> str:
        return " ".join(token for token in text.split(" ") if token.startswith("@") is False)

    def _remove_special_characters(self, text: str) -> str:
        # special characters like new line/tab/carriage return will be replaced with a space
        # redundant spaces are deleted later by a method below
        return re.sub(r"[\n\t\r]+", " ", text)

    def _remove_redundant_spaces(self, text: str) -> str:
        return " ".join(text.split())

    def preprocess(self, text: str) -> str:
        text = text.lower()
        text = self._remove_emojis(text)
        text = self._remove_mentions(text)
        text = self._remove_stopwords(text)
        text = self._remove_urls(text)
        text = self._remove_special_characters(text)
        text = self._remove_punctuation(text)
        text = self._remove_redundant_spaces(text)
        return text
