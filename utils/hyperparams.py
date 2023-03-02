from dataclasses import dataclass
from typing import List


@dataclass
class SVMHyperparams:
    C: List[float]
    kernel: List[str]
    class_weight: str = "balanced"


@dataclass
class TFIDFHyperparams:
    max_df: List[float]
    max_features: List[int]
