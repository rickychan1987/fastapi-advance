from fastapi import FastAPI
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine
from .routers import post, user, auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(post.router, prefix="/posts", tags=['Post'])
app.include_router(user.router, prefix="/users", tags=['User'])
app.include_router(auth.router, tags=['Authentication'])


while True:

    try:
        conn = psycopg2.connect(
            host='localhost', database='fastapi-advance', user='postgres', password='1234', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Failed to connect")
        print("Error", error)
        time.sleep(2)
