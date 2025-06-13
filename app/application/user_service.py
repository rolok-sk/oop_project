from typing import List
from app.domain.models import User
from app.domain.repositories import AbstractUserRepository

class UserService:
    def __init__(self, repo: AbstractUserRepository):
        self.repo = repo

    def get_users(self) -> List[User]:
        return self.repo.get_all()

    def get_user(self, user_id: int) -> User:
        return self.repo.get_by_id(user_id)

    def create_user(self, username: str, password: str) -> User:
        return self.repo.create(User(id=0, username=username, password=password))
    
    def update_user(self, user_id: int, username: str = None, password: str = None) -> User:
        return self.repo.update(user_id, username, password)
    
    def delete_user(self, user_id: int) -> bool:
        return self.repo.delete(user_id)