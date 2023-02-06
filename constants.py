import os
import pathlib


# from dotenv import load_dotenv


class Constants:
    __slots__ = []

    # def __init__(self):
    # load_dotenv()

    MODEL_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/resources/catboost"

    @staticmethod
    def get_db_url():
        return f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("DBHOST")}' \
               f':{os.getenv("PORT")}/{os.getenv("TABLE")}'
