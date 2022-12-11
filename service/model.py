import logging

from catboost import CatBoostClassifier

from config.constants import Constants
from config.engine import DatabaseConfiguration
from service.repository import EEGRepository


class ModelService:
    __slots__ = ['model', 'repository']

    def __init__(self, path=Constants.MODEL_PATH):
        self.repository = EEGRepository(DatabaseConfiguration.get_engine())
        self.model = CatBoostClassifier()
        self.model.load_model(path)

    def analyse(self, data: dict) -> float | dict:
        logging.debug(data)
        try:
            pred = self.model.predict(data.values())
            self.repository.save(data)
            return {"result": float(pred)}

        except Exception as e:
            return {"result": f'Exception as {e}'}
