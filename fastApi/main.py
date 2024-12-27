from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

items = []

class Item(BaseModel):
    id: int
    name: str
    description: str

@app.get("/items/", response_model=List[Item])
def get_items():
    response = requests.get("http://127.0.0.1:8000/api/items/")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching items")


@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    response = requests.post("http://127.0.0.1:8000/api/items/", json=item.dict())
    if response.status_code == 201:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Error creating item")


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    response = requests.get(f'http://127.0.0.1:8000/api/items/{item_id}')
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching item")