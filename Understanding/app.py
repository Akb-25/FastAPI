from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the "static" directory to serve static files like CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request, value: int = 0):
    square = value ** 2
    return templates.TemplateResponse("index.html", {"request": request, "value": value, "square": square})
