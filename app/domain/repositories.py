from abc import ABC, abstractmethod
from typing import List
from .models import Post, User, Comment

class AbstractPostRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Post]: pass

    @abstractmethod
    def get_by_id(self, post_id: int) -> Post: pass

    @abstractmethod
    def create(self, post: Post) -> Post: pass

    @abstractmethod
    def update(self, post_id: int, title: str = None, content: str = None, author_id: int = None) -> Post: pass

    @abstractmethod
    def delete(self, post_id: int) -> bool: pass

class AbstractUserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[User]: pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User: pass

    @abstractmethod
    def create(self, user: User) -> User: pass

    @abstractmethod
    def update(self, user_id: int, username: str = None, password: str = None) -> User: pass

    @abstractmethod
    def delete(self, user_id: int) -> bool: pass

class AbstractCommentRepository(ABC):
    @abstractmethod
    def get_all_by_post(self, post_id: int) -> List[Comment]: pass

    @abstractmethod
    def get_by_id(self, comment_id: int) -> Comment: pass

    @abstractmethod
    def create(self, comment: Comment) -> Comment: pass

    @abstractmethod
    def update(self, comment_id: int, content: str = None, post_id: int = None, author_id: int = None) -> Comment: pass

    @abstractmethod
    def delete(self, comment_id: int) -> bool: pass
    