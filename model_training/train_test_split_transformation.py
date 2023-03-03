from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split


class TrainValidationSplitTransformation:
    def __init__(
        self,
        input_column_name: str,
        target_column_name: str,
        train_size: float,
        do_stratify: bool = True,
    ):
        self.input_column_name = input_column_name
        self.target_column_name = target_column_name
        self.train_size = train_size
        self.do_stratify = do_stratify

    def split_to_training_and_val_subsets(
        self,
        dataframe: pd.DataFrame,
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
        X, y = (
            dataframe[self.input_column_name].copy(),
            dataframe[self.target_column_name].copy(),
        )

        X_train, X_val, y_train, y_val = train_test_split(
            X,
            y,
            train_size=self.train_size,
            random_state=42,
            stratify=y if self.do_stratify else None,
        )

        df_train = pd.DataFrame(
            {
                self.input_column_name: X_train,
                self.target_column_name: y_train,
            }
        )
        df_val = pd.DataFrame(
            {
                self.input_column_name: X_val,
                self.target_column_name: y_val,
            }
        )

        return df_train, df_val
