from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.factories.repository_factory import RepositoryFactory
from app.application.comment_service import CommentService

router = APIRouter(
    prefix="/comments",
    tags=["comments"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_comments(post_id: int, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    return service.get_comments(post_id)

@router.get("/{comment_id}")
def get_comment(comment_id: int, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    comment = service.get_comment(comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@router.post("/")
def create_comment(post_id: int, author_id: int, content: str, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    return service.create_comment(post_id, author_id, content)

@router.put("/{comment_id}")
def update_comment(comment_id: int, content: str = None, post_id: int = None, author_id: int = None, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    comment = service.update_comment(comment_id, content, post_id, author_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    if not service.delete_comment(comment_id):
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted"} 