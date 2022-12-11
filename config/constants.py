import os

from dotenv import load_dotenv


class Constants:
    __slots__ = []

    def __init__(self):
        load_dotenv()

    MODEL_PATH = "resources/Catboost_Model"

    @staticmethod
    def get_db_url():
        return f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("DBHOST")}' \
               f':{os.getenv("PORT")}/{os.getenv("TABLE")}'
