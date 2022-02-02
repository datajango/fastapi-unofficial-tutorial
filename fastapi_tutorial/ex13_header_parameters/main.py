from typing import Optional

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}

@app.get("/items1/")
async def read_items1(
    strange_header: Optional[str] = Header(None, convert_underscores=False)
):
    return {"strange_header": strange_header}

@app.get("/items2/")
async def read_items2(x_token: Optional[list[str]] = Header(None)):
    return {"X-Token values": x_token}