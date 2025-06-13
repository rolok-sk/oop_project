from typing import List
from app.domain.models import Comment
from app.domain.repositories import AbstractCommentRepository

class CommentService:
    def __init__(self, repo: AbstractCommentRepository):
        self.repo = repo

    def get_comments(self, post_id: int) -> List[Comment]:
        return self.repo.get_all_by_post(post_id)

    def get_comment(self, comment_id: int) -> Comment:
        return self.repo.get_by_id(comment_id)

    def create_comment(self, post_id: int, author_id: int, content: str) -> Comment:
        return self.repo.create(Comment(id=0, post_id=post_id, author_id=author_id, content=content))
    
    def update_comment(self, comment_id: int, content: str = None, post_id: int = None, author_id: int = None) -> Comment:
        return self.repo.update(comment_id, content, post_id, author_id)
    
    def delete_comment(self, comment_id: int) -> bool:
        return self.repo.delete(comment_id)