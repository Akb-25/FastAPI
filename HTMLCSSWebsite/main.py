from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from databases import Database
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)
metadata = MetaData()

# Define the "users" table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("email", String(255)),
)

# Templates setup
templates = Jinja2Templates(directory="frontend")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
async def submit_form(name: str = Form(...), email: str = Form(...)):
    # Insert form data into the database
    query = users.insert().values(name=name, email=email)
    await database.execute(query)
    return {"message": "Form submitted successfully!"}
