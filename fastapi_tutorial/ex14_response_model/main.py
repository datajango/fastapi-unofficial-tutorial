from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


# Don't do this in production!
@app.post("/user/", response_model=UserIn)
async def create_user(user: UserIn):
    return user


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

@app.post("/user1/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


class ItemV2(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items2/{item_id}", response_model=ItemV2, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]



class ItemV3(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5


itemsV3 = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items3/{item_id}/name",
    response_model=ItemV3,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return itemsV3[item_id]


@app.get("/items3/{item_id}/public",
    response_model=ItemV3,
    response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return itemsV3[item_id]