from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    id: int = 1
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.post("/items/{item_id}")
async def create_item1(item_id: int, item: Item, q: Optional[str] = None):
    item_dict = item.dict()
    item_dict.update({"id": item_id})
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    if q:
        item_dict.update({"q": q})
    return item_dict
