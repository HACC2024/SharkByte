import gradio as gr
from gradio_ui import demo
import os
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

app = gr.mount_gradio_app(app, demo, '/gradio')