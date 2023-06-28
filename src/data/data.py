import kaggle
import pandas as pd

from config import settings

DATA_PATH = "src/data/"


class NikeDataset:

    """Class for getting Nike Dataset"""

    def __init__(self) -> None:
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(settings.data.dataset_name, path=DATA_PATH, unzip=True)
        self._df = pd.read_csv("src/data/nike_data_2022_09.csv")

    @property
    def df(self) -> pd.DataFrame:
        return self._df
