from fastapi import FastAPI
from enum import Enum

class ColorName(str, Enum):
    rd = "Red"
    bl = "Blue"
    gr = "Green"

app = FastAPI()

@app.get("/users/me") # order matters,
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/colors/{color_name}")
async def get_color(color_name: ColorName):
    if color_name == ColorName.rd:
        return {"color_name": color_name, "message": "Red is a nice color."}

    if color_name.value == "Blue":
        return {"color_name": color_name, "message": "Blue is the color of the sky."}

    return {"color_name": color_name, "message": "Green is the color of grass."}

# Path convertor
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}