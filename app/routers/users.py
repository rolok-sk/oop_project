from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.factories.repository_factory import RepositoryFactory
from app.application.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    return service.get_users()

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/")
def create_user(username: str, password: str, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    return service.create_user(username, password)

@router.put("/{user_id}")
def update_user(user_id: int, username: str = None, password: str = None, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    user = service.update_user(user_id, username, password)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    if not service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"} 