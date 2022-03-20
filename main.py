from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1",
             "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "i like pizza", "id": 2}]


@app.get("/")
async def root():
    return {"message": "Welcome to MyAPI"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


@app.post("/posts")
async def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}
