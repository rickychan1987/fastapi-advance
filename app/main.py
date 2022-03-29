from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(post.router, prefix="/posts", tags=['Post'])
app.include_router(user.router, prefix="/users", tags=['User'])
app.include_router(auth.router, tags=['Authentication'])
