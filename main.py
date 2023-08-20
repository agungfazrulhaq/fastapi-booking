from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()

@app.get("/")
async def home(request: Request):
	return templates.TemplateResponse("index.html",{"request":request})

@app.get("/home")
async def homepage(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.get("/room")
async def homepage(request: Request):
    return templates.TemplateResponse("room.html",{"request":request})

@app.get("/book")
async def homepage(request: Request):
    return templates.TemplateResponse("book.html",{"request":request})

@app.get("/login")
async def homepage(request: Request):
    return templates.TemplateResponse("login.html",{"request":request})


if __name__ == "__main__":


