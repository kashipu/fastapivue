from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

templates = Jinja2Templates(directory="templates") 

app = FastAPI()


class TextArea(BaseModel):
    content: str


@app.post("/add")
async def post_textarea(data: TextArea):
    print(data.dict())
    return {**data.dict()}


@app.get("/")
async def serve_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})