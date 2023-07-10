import os

from config import settings

os.environ["KAGGLE_USERNAME"] = settings.kaggle.username
os.environ["KAGGLE_KEY"] = settings.kaggle.key

from data.data import NikeDataset  # noqa: E402
