import pathlib

from pydantic import BaseSettings, conint, constr
from pydantic.validators import IPv4Address


class Settings(BaseSettings):
    DEBUG: bool = True

    APP_TITLE: constr(min_length=1, max_length=255) = 'CKD_API'
    APP_VERSION: constr(min_length=1, max_length=15) = '1'
    APP_HOST: constr(min_length=1, max_length=15) = str(IPv4Address('127.0.0.1' if DEBUG else '0.0.0.0'))
    APP_PORT: conint(ge=0) = 5000
    APP_PATH: constr(min_length=1, max_length=255) = str(pathlib.Path(__file__).parent.resolve())

    # MODEL_REQUEST_QUEUE: constr(min_length=1, max_length=255) = 'MODEL_REQUEST_QUEUE'
    MODEL_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/resources/catboost"

    cat_columns: dict = {'прием': True,
                         'дебют_в_возрасте': False,
                         'возрастная_группа_дебют': True,
                         'Дз': True,
                         'пол': True,
                         'Возраст_группы': True,
                         'Тр_в_день': False,
                         'Трпения_дебют': False,
                         'длит_Трпении': False,
                         'Нв_в_день': False,
                         'Эр_в_день': False,
                         'Лей_в_день': False,
                         'Кр_в_день_мкмольл': False,
                         'Кр_макс': False,
                         'СКФ_в_день': False,
                         'СКФ_мин': False,
                         'длит_СКФ': False,
                         'Мочевина_в_день': False,
                         'Мочевина_макс': False,
                         'АЛТ_в_день': False,
                         'АЛТ_макс': False,
                         'АСТ_в_день': False,
                         'АСТ_макс': False,
                         'ЛДГ_в_день': False,
                         'ЛДГ_макс': False,
                         'ОБ_в_день': False,
                         'СОЭ_макс': False,
                         'СОЭ_в_день': False,
                         'СРБ_макс': False,
                         'СРБ_в_день': False,
                         'С3_мин': False,
                         'С4_мин': False,
                         'гаптоглобин_мин': False,
                         'ЦНС': True,
                         'поражениеЦНС': True,
                         'поражение_сердца': True,
                         'ЭхоКС': True,
                         'ЧЛС': True,
                         'паренхима_почек': True,
                         'дебют_заболевани': True,
                         'гемоколит': True,
                         'диарея': True,
                         'температура': False,
                         'рвота': True,
                         'АГ': True,
                         'САД': False,
                         'ДАД': False,
                         'ЖКТ': True,
                         'Печень': True,
                         'Сут.белок_макс': False,
                         'протеинурия_дней': False,
                         'гематурия': False,
                         'гематурия_дней': False,
                         'лейкоцитурия': False,
                         'лейкурия_дней': False,
                         'нарушения_мочеиспускания': True,
                         'олиг.анурия_дней': False,
                         'экулизумаб': True,
                         'длительность_ОПП': False,
                         'перитонеальный': True,
                         'гемодиализ': True,
                         '@5ГИУК': False,
                         '@5HTвплазме': False}


settings = Settings()
