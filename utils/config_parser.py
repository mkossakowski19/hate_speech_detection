from typing import Tuple
import yaml

from utils.hyperparams import SVMHyperparams, TFIDFHyperparams


class ConfigParser:
    @staticmethod
    def load_hyperparams(filepath: str) -> Tuple[SVMHyperparams, TFIDFHyperparams]:
        with open(filepath, "r") as f:
            hyperparams = yaml.full_load(f)
        model_hyperparams = SVMHyperparams(
            C=hyperparams["model_hyperparams"]["C"],
            kernel=hyperparams["model_hyperparams"]["kernel"],
            class_weight=hyperparams["model_hyperparams"]["class_weight"],
        )
        vectorizer_hyperparams = TFIDFHyperparams(
            max_df=hyperparams["vectorizer_hyperparams"]["max_df"],
            max_features=hyperparams["vectorizer_hyperparams"]["max_features"],
        )
        return model_hyperparams, vectorizer_hyperparams
