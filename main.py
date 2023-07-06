from starlette.responses import RedirectResponse
from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos,users
from starlette.staticfiles import StaticFiles
import os
print(os.getcwd())
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

static_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# Mount the 'static' directory
app.mount("/static", StaticFiles(directory=static_directory), name="static")

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)

@app.get("/")
async def home():
    return RedirectResponse(url="/todos")