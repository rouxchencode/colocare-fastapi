from fastapi import FastAPI

from .database import engine, Base
from . import models
from .routers import foods

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ColoCare API")
app.include_router(foods.router)