import os
from pathlib import Path
from uuid import UUID

import kaggle
import pandas as pd

from config import settings

DATA_PATH = Path("src/data")
DATA_FULLPATH = Path.joinpath(DATA_PATH, "nike_data_2022_09.csv")


class NikeDataset:

    """Class for getting Nike Dataset"""

    def __init__(self) -> None:
        """Download and parse in Nike Dataset"""
        if not os.path.isfile(DATA_FULLPATH):  # download if not exists
            self._download_data()
        self._df: pd.DataFrame = pd.read_csv(DATA_FULLPATH)
        self._df = self._df_clean(self._df)

    @staticmethod
    def _download_data() -> None:
        """download data from Kaggle. Must have `.kaggle/kaggle.json` to authenticate"""
        try:
            kaggle.api.authenticate()
            kaggle.api.dataset_download_files(settings.data.dataset_name, path=DATA_PATH, unzip=True)
        except Exception as e:
            raise e

    @staticmethod
    def _uuid_conversion(df: pd.Series) -> pd.Series:
        """convert a pandas series from object to uuids"""
        return df.apply(lambda x: UUID(x))

    @staticmethod
    def _datetime_conversion(df: pd.Series) -> pd.Series:
        """convert a pandas series from object to uuids"""
        return pd.to_datetime(df, dayfirst=True)

    def _df_clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply cleaning steps to dataframe"""
        df = df.drop(["index"], axis=1)
        df["uniq_id"] = self._uuid_conversion(df["uniq_id"])
        df["scraped_at"] = self._datetime_conversion(df["scraped_at"])
        df["description"] = df["description"].str.replace('"', "'")
        df = df.replace(r"\n", " ", regex=True)
        df.drop(columns=["raw_description"])
        return df

    @property
    def df(self) -> pd.DataFrame:
        return self._df
