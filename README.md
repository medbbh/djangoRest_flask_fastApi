# Tp DRF, Flask, FastAPI

## M'Hamed Babah C18618
## Elwalde Sidi Med C18614

# Quick guide to run this project successfully : 


## Prerequisites

- Python 3.12
- Pipenv

## Setup Steps

1. Install Pipenv if you haven't:
```bash
pip install pipenv
```

2. Install project dependencies:
```bash
pipenv install
```

3. Activate the virtual environment:
```bash
pipenv shell
```

## Running the Project

You need to run these services in separate terminal windows:

1. Start Django REST API first (Main API):
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
This will run on http://127.0.0.1:8000

2. Start Flask Gateway:
   go to flask directory and run
```bash
python flask_app.py
```
This will run on http://127.0.0.1:5000

3. Start FastAPI Gateway:
   go to fastapi directory and run 
```bash
uvicorn fastapi_app:app --reload --port 8002
```
This will run on http://127.0.0.1:8002

## Access API Documentation

- Flask Swagger docs: http://127.0.0.1:5000/docs
- FastAPI docs: http://127.0.0.1:8001/docs
