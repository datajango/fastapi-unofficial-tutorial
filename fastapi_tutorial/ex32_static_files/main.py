from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

base_path = Path(__file__).resolve().parent
templates_folder = Jinja2Templates(directory=str(base_path / "templates"))
static_folder = Jinja2Templates(directory=str(base_path / "static"))
#static_folder = Jinja2Templates(directory=str(base_path))
#static_folder = "fastapi_tutoria/ex32_static_files/static"
#static_folder = "G:\\fastapi\\fastapi-unofficial-tutorial\\fastapi_tutorial\\ex32_static_files"
app.mount(static_folder, StaticFiles(directory="static"), name="static")

@app.get("/")
async def example(request: Request):
    return templates_folder.TemplateResponse("index.html", {"request": request})