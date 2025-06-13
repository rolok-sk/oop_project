from fastapi import FastAPI
from app.routers import posts, comments, users

app = FastAPI(
    title="Blog API",
    description="A simple blog API with posts, comments and users",
    version="1.0.0"
)

app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(users.router)
