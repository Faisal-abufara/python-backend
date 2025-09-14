from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
posts_db = [
    {"post_id": 1, "user_id": 1, "title": "First Post", "status": "published"},
    {"post_id": 2, "user_id": 1, "title": "Draft Post", "status": "draft"},
    {"post_id": 3, "user_id": 2, "title": "Another User's Post", "status": "published"},
    {"post_id": 4, "user_id": 1, "title": "Second Published Post", "status": "published"},
]

@app.get("/users/{user_id}/posts")
def get_user_posts(
    user_id: int,
    status: Optional[str] = Query(None, regex="^(published|draft)$")
):    
    user_posts = [post for post in posts_db if post["user_id"] == user_id]

    if status:
        user_posts = [post for post in user_posts if post["status"] == status]

    return {"user_id": user_id, "posts": user_posts}
