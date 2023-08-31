# ХБП.NET
## Запуск приложения
1. Создайте venv: python -m venv /path/to/core/venv
2. Активация venv: source /path/to/core/venv/bin/activate (Для unix-систем)
3. Запустите команду установки зависимостей: pip install -r requirements.txt
4. Старт приложения: python main.py

### Используемый стек
* aiofiles==23.2.1
* numpy==1.25.2
* pandas==2.0.3
* requests==2.31.0
* snuggs==1.4.7
* fastapi==0.103.0
* uvicorn==0.23.2
* catboost==1.2.1
* Jinja2==3.1.2
* python-multipart==0.0.6
* sqlalchemy==2.0.20
* pydantic==2.3.0
* starlette==0.31.1

### Доступ
Получить доступ локально можно по 127.0.0.1:5000/api/, там же можно посмотреть и документацию к API