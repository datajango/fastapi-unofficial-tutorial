from fastapi import FastAPI, Request
from typing import Optional

app = FastAPI()

fake_items_db = [
    {"item_name": "Abc"},
    {"item_name": "Def"},
    {"item_name": "Ghi"},
    {"item_name": "Jkl"},
    {"item_name": "MNo"},
    {"item_name": "Pqr"},
    {"item_name": "Stu"},
    {"item_name": "Vwz"},
    {"item_name": "Yzz"},
    {"item_name": "123"},
    {"item_name": "456"},
    {"item_name": "789"},
]

@app.get("/items/")
async def read_item(request: Request, skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item2(request: Request, item_id: str, q: Optional[str] = None, short: bool = False):

    item = {"item_id": item_id}

    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    else:
        item.update(
            {"description": "Amazing"}
        )

    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/items2/{item_id}")
async def read_user_item2(item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
    item = {
        "item_id": item_id,
        "needy": needy,
        "skip": skip,
        "limit": limit
    }
    return item