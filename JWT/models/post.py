from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int

class PostChange(BaseModel):
    title: str
    content: str

class Post(BaseModel):
    id: int
    title: str
    content: str
    user_id: int