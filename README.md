
## Запуск проекта

python -m venv venv

.\venv\Scripts\activate  
pip install -r requirements.txt  
uvicorn app.main:app --reload
