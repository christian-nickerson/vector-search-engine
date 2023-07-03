import os
from pathlib import Path
from typing import Dict, List

import kaggle
import pandas as pd

from config import settings

DATA_PATH = "src/data/"
DATA_FULLPATH = Path(f"{DATA_PATH}nike_data_2022_09.csv")


class NikeDataset:

    """Class for getting Nike Dataset"""

    def __init__(self) -> None:
        """Download and parse in Nike Dataset"""
        if not os.path.isfile(DATA_FULLPATH):  # download if not exists
            self._download_data()
        self._df: pd.DataFrame = pd.read_csv(DATA_FULLPATH)
        self._df = self._df.drop(["index"], axis=1)

    @staticmethod
    def _download_data() -> None:
        """download data from Kaggle. Must have `.kaggle/kaggle.json` to authenticate"""
        try:
            kaggle.api.authenticate()
            kaggle.api.dataset_download_files(settings.data.dataset_name, path=DATA_PATH, unzip=True)
        except Exception as e:
            raise e

    @property
    def df(self) -> pd.DataFrame:
        return self._df

    @property
    def column_types(self) -> List[Dict[str, str]]:
        """get column types data"""
        column_types = []
        for col, type in zip(self._df.columns, self._df.dtypes):
            column_types.append({"column_name": col, "column_type": type.name})
        return column_types
