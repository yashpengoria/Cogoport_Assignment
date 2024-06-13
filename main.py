from fastapi import FastAPI
from routers import configuration
from database.session import engine
from models.configuration import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(configuration.router)
