from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list[str] = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


class ItemV1(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list[str] = set()


@app.put("/items2/{item_id}")
async def update_item(item_id: int, item: ItemV1):
    results = {"item_id": item_id, "item": item}
    return results

class Image(BaseModel):
    url: str
    name: str

class ItemV2(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list[str] = []
    image: Optional[Image] = None

@app.put("/items3/{item_id}")
async def update_item(item_id: int, item: ItemV2):
    results = {"item_id": item_id, "item": item}
    return results

class ItemV3(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list[str] = []
    images: Optional[list[Image]] = None

@app.put("/items4/{item_id}")
async def update_item(item_id: int, item: ItemV3):
    results = {"item_id": item_id, "item": item}
    return results


class ItemV4(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    #tags: set[str] = set() I found a bug in assert equal sets
    tags: list[str] = set()
    images: Optional[list[Image]] = None


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: list[ItemV4]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


class Image(BaseModel):
    url: HttpUrl
    name: str

@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images

@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights

