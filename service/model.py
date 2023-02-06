import logging

from catboost import CatBoostClassifier

from constants import Constants
from service.schemas.analysis import Analysis


class ModelService:
    __slots__ = ['model', 'repository']

    def __init__(self, path=Constants.MODEL_PATH):
        # self.repository = EEGRepository(DatabaseConfiguration.get_engine())
        self.model = CatBoostClassifier()
        self.model.load_model(path)

    def analyse(self, data: Analysis) -> float | dict:
        logging.debug(data)
        try:
            values = list(data.dict().values())
            pred = self.model.predict_proba(values)
            # self.repository.save(data)
            return {"Вероятность болезни": float(pred)}

        except Exception as e:
            return {"result": f'Exception as {e}'}
