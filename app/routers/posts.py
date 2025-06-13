from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.factories.repository_factory import RepositoryFactory
from app.application.post_service import PostService

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    return service.get_posts()

@router.get("/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    post = service.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.post("/")
def create_post(title: str, content: str, author_id: int, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    return service.create_post(title, content, author_id)

@router.put("/{post_id}")
def update_post(post_id: int, title: str = None, content: str = None, author_id: int = None, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    post = service.update_post(post_id, title, content, author_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    if not service.delete_post(post_id):
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"} 