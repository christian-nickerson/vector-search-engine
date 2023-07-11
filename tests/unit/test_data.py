from datetime import datetime
from uuid import UUID, uuid4

import pandas as pd
import pandas.api.types as ptypes

from data import NikeDataset
from data.data import DATA_FULLPATH


def test_kaggle_download() -> None:
    """test dataset download writes file"""
    NikeDataset._download_data()
    df = pd.read_csv(DATA_FULLPATH)
    assert len(df.index) > 0


def test_uuid_conversion() -> None:
    """test uuid converts pandas series of uuid strings to uuid objects"""
    strings = [f"{uuid4()}" for _ in range(5)]
    series = pd.Series(strings)
    result = NikeDataset._uuid_conversion(series)
    for item in result:
        assert isinstance(item, UUID)


def test_date_conversion() -> None:
    """test datetime conversion of strings returns correctly"""
    strings = [f"{datetime.now()}" for _ in range(5)]
    series = pd.Series(strings)
    result = NikeDataset._datetime_conversion(series)
    for item in result:
        assert isinstance(item, datetime)


def test_dataset() -> None:
    """test dataset returns correctly"""
    nd = NikeDataset()
    assert isinstance(nd.df, pd.DataFrame)
    assert ptypes.is_object_dtype(nd.df["uniq_id"])
    assert ptypes.is_datetime64_dtype(nd.df["scraped_at"])
    assert "raw_desciption" not in nd.df.columns
