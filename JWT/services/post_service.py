from fastapi import HTTPException, status

from typing import List

from JWT.database import post_db
from JWT.models import Post, PostCreate, PostChange
from JWT.utils import post_id_gen

class PostService:
    @staticmethod
    def create_post(post_to_create: PostCreate, user_id: int) -> Post:
        new_post = Post(
            id = next(post_id_gen),
            title=post_to_create.title,
            content=post_to_create.content,
            user_id=user_id
        )

        post_db.append(new_post)
        return new_post

    @staticmethod
    def get_all_posts(user_id: int) -> List[Post]:
        return [post for post in post_db if post.user_id == user_id]

    @staticmethod
    def get_post_by_id(post_id: int, user_id: int) -> Post:
        post = next((post for post in post_db if post.user_id == user_id and post.id == post_id), None)
        if post: return post

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id<{post_id}> not found")

    @staticmethod
    def change_post(post_with_new_data: PostChange, post_id: int, user_id: int) -> Post:
        post_to_change = PostService.get_post_by_id(post_id, user_id)

        post_to_change.title = post_with_new_data.title
        post_to_change.content = post_with_new_data.content

        return post_to_change

    @staticmethod
    def delete_post(post_id: int, user_id: int) -> None:
        post_to_delete = PostService.get_post_by_id(post_id, user_id)

        del post_db[post_db.index(post_to_delete)]