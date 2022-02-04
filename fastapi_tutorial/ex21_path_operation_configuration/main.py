from typing import Optional, Set, List
from enum import Enum
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Tags(Enum):
    items = "items"
    users = "users"

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    #tags: Set[str] = set()
    tags: List[str] = set()

@app.post("/items/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
    deprecated=True)
async def create_item(item: Item):
    return item

@app.post("/items1/",
    response_model=Item,
    tags=[Tags.items],
    summary="Create an item",
    response_description="The created item.",)
async def create_item1(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

@app.get("/items/", tags=[Tags.items])
async def read_items():
    return [{"name": "Foo", "price": 42}]

@app.get("/users/", tags=[Tags.users])
async def read_users():
    return [{"username": "johndoe"}]