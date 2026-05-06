# analyze_sales

Привет, это тестовое задание. Помимо эндпоинта реализовал тесты и докерфайл, код прокомментирован там, где это надо для лучшего понимания, типы данных проставлены, структура проекта минимальная - в файле main.py один эндпоинт, который вызывает одну функцию из utils.py. Отдельно вынес Pydantic схемы в файл schemas.py.

Над кодом очень старался, жду твой фидбэк

### Локальный запуск

1. Клонируй репозиторий и перейди в папку проекта:
   ```bash
   git clone https://github.com/Furasfast346/analyze_sales.git
   cd analyze_sales
   ```
   
Создай виртуальное окружение и активируй его:

```bash
python -m venv venv
source venv/bin/activate      # для Linux/Mac
# venv\Scripts\activate       # для Windows
```

Установи зависимости:

```bash
pip install -r requirements.txt
```
Запусти сервер:

```bash
uvicorn app.main:app --reload
```
Открой в браузере:

```text
http://127.0.0.1:8000/docs
```
