import pathlib
from pydantic import conint, constr


class Settings:
    DEBUG: bool = True

    APP_TITLE: constr(min_length=1, max_length=255) = 'CKD_API'
    APP_VERSION: constr(min_length=1, max_length=15) = '1'
    APP_HOST: constr(min_length=1, max_length=15) = str('127.0.0.1' if DEBUG else '0.0.0.0')
    APP_PORT: conint(ge=0) = 5000
    APP_PATH: constr(min_length=1, max_length=255) = str(pathlib.Path(__file__).parent.resolve())

    # MODEL_REQUEST_QUEUE: constr(min_length=1, max_length=255) = 'MODEL_REQUEST_QUEUE'
    MODEL_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/resources/catboost"

    cat_columns: dict = {'прием': [0.0, 1.0, 3.0, 2.0],
                         'дебют_в_возрасте': False,
                         'возрастная_группа_дебют': [2.0, 1.0, 0.0, 3.0],
                         'Дз': ['ГУС', 'аГУС'],
                         'пол': ['Мальчик', 'Девочка'],
                         'Возраст_группы': [2.0, 1.0, 0.0, 3.0],
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
                         'ЦНС': [1.0, 0.0],
                         'поражениеЦНС': [1.0, 0.0, 2.0, 3.0, 4.0],
                         'поражение_сердца': [0.0, 1.0],
                         'ЭхоКС': [0.0, 5.0, 3.0, 2.0, 1.0, 4.0, 9.0, 6.0, 7.0, 8.0],
                         'ЧЛС': [1.0, 2.0, 0.0],
                         'паренхима_почек': [1.0, 0.0, 2.0],
                         'дебют_заболевани': [2.0, 3.0, 1.0],
                         'гемоколит': [0.0, 1.0],
                         'диарея': [0.0, 2.0, 1.0],
                         'температура': False,
                         'рвота': [0.0, 2.0, 1.0],
                         'АГ': [1.0, 0.0],
                         'САД': False,
                         'ДАД': False,
                         'ЖКТ': [3.0, 0.0, 2.0, 6.0, 1.0, 5.0, 7.0, 8.0, 4.0],
                         'Печень': [1.0, 2.0, 0.0],
                         'Сут.белок_макс': False,
                         'протеинурия_дней': False,
                         'гематурия': False,
                         'гематурия_дней': False,
                         'лейкоцитурия': False,
                         'лейкурия_дней': False,
                         'нарушения_мочеиспускания': [2.0, 1.0, 0.0],
                         'олиг.анурия_дней': False,
                         'экулизумаб': [0.0, 1.0, 5.0, 2.0, 3.0, 7.0],
                         'длительность_ОПП': False,
                         'перитонеальный': [0.0, 1.0],
                         'гемодиализ': [1.0, 0.0],
                         '@5ГИУК': False,
                         '@5HTвплазме': False}


settings = Settings()
