from pydantic import BaseModel, Field
from typing import List

from JWT.models import Post

class PostCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=45)
    content: str = Field(..., min_length=1, max_length=500)

class PostChange(BaseModel):
    title: str = Field(..., min_length=1, max_length=45)
    content: str = Field(..., min_length=1, max_length=500)

class PostResponse(BaseModel):
    title: str
    content: str
    user_id: int

class PostsResponse(BaseModel):
    status: int
    success: bool
    data: List[Post]

class PostOneResponse(BaseModel):
    status: int
    success: bool
    data: PostResponse

class PostCreatedResponse(BaseModel):
    status: int
    success: bool
    data: PostResponse

class PostChangedResponse(BaseModel):
    status: int
    success: bool
    data: PostResponse
