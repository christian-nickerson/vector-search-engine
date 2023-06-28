import os
from pathlib import Path

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
        self._df = pd.read_csv(DATA_FULLPATH)

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
