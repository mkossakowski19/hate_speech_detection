from typing import Any, Dict, Tuple
import yaml


class ConfigParser:
    @staticmethod
    def load_hyperparams(filepath: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        with open(filepath, "r") as f:
            hyperparams = yaml.full_load(f)
        return hyperparams
