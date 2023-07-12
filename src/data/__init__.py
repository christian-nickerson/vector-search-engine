import os

from config import settings

if os.getenv("KAGGLE_USERNAME") is None:
    raise Exception("No api vars")
    os.environ["KAGGLE_USERNAME"] = settings.kaggle.username
if os.getenv("KAGGLE_KEY") is None:
    os.environ["KAGGLE_KEY"] = settings.kaggle.key

from data.data import NikeDataset  # noqa: E402
