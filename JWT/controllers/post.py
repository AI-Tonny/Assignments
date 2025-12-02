from fastapi import APIRouter, Depends, status

from JWT.services import PostService, AuthService
from JWT.schemas.post import (
    PostCreate,
    PostChange,
    PostResponse,
    PostsResponse,
    PostOneResponse,
    PostCreatedResponse,
    PostChangedResponse,
    PostDeletedResponse
)
from JWT.models import User

post_router = APIRouter()

@post_router.post("/create-post/", response_model=PostCreatedResponse, status_code=status.HTTP_201_CREATED)
async def create_post(
        post: PostCreate,
        current_user: User = Depends(AuthService.get_current_user)):
    created_post = PostService.create_post(post, current_user.id)

    return PostCreatedResponse(
        status=201,
        success=True,
        data=PostResponse(
            title=created_post.title,
            content=created_post.content,
            user_id=created_post.user_id
        )
    )

@post_router.get("/get-posts/", response_model=PostsResponse, status_code=status.HTTP_200_OK)
async def get_posts(
        current_user: User = Depends(AuthService.get_current_user)
):
    posts = PostService.get_all_posts(current_user.id)

    return PostsResponse(
        status=200,
        success=True,
        data=posts
    )

@post_router.get("/get-post/{post_id}", response_model=PostOneResponse, status_code=status.HTTP_200_OK)
async def get_post(
        post_id: int,
        current_user: User = Depends(AuthService.get_current_user)
):
    post = PostService.get_post_by_id(post_id, current_user.id)

    return PostOneResponse(
        status=200,
        success=True,
        data=PostResponse(
            title=post.title,
            content=post.content,
            user_id=post.user_id
        )
    )

@post_router.put("/change-post/{post_id}", response_model=PostChangedResponse, status_code=status.HTTP_200_OK)
async def change_post(
        post_id: int,
        post: PostChange,
        current_user: User = Depends(AuthService.get_current_user)
):
    changed_post = PostService.change_post(post, post_id, current_user.id)

    return PostChangedResponse(
        status=200,
        success=True,
        data=PostResponse(
            title=changed_post.title,
            content=changed_post.content,
            user_id=changed_post.user_id
        )
    )

@post_router.delete("/delete-post/{post_id}", response_model=PostDeletedResponse, status_code=status.HTTP_200_OK)
async def change_post(
        post_id: int,
        current_user: User = Depends(AuthService.get_current_user)
):
    PostService.delete_post(post_id, current_user.id)

    return PostDeletedResponse(
        status=200,
        success=True,
    )