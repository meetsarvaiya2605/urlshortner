from urlshortner import models
from fastapi import FastAPI

from .database import engine
from urlshortner.app.routers import url_short   


app = FastAPI()




models.Base.metadata.create_all(bind=engine)


app.include_router(url_short.router)

