# API Gateways Implementation
*Using DRF, Flask, and FastAPI*

## Authors
- M'Hamed Babah (C18618)
- Elwalde Sidi Med (C18614)

## Setup Instructions

### Requirements
- Python 3.12
- Pipenv

### Installation
```bash
pip install pipenv
pipenv install
pipenv shell
```

### Running Services

1. **Django REST API** (Main Service)
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
→ http://127.0.0.1:8000

2. **Flask Gateway** (In flask directory)
```bash
python flask_app.py
```
→ http://127.0.0.1:5000

3. **FastAPI Gateway** (In fastapi directory)
```bash
uvicorn fastapi_app:app --reload --port 8002
```
→ http://127.0.0.1:8002

### API Documentation
- Flask docs: http://127.0.0.1:5000/docs
- FastAPI docs: http://127.0.0.1:8002/docs
