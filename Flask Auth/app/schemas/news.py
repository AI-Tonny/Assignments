from pydantic import BaseModel, Field
from typing import List, Optional

class NewsCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=50)
    content: str = Field(..., min_length=1, max_length=500)
    category: Optional[str] = Field(None, min_length=1, max_length=50)

class NewsChange(BaseModel):
    title: str = Field(..., min_length=1, max_length=50)
    content: str = Field(..., min_length=1, max_length=500)
    category: Optional[str] = Field(None, min_length=1, max_length=50)

class NewsResponse(BaseModel):
    id: int
    title: str
    content: str
    category: str
    user_id: int

class NewsAllResponse(BaseModel):
    status: int
    success: bool
    data: List[NewsResponse]

class NewsOneResponse(BaseModel):
    status: int
    success: bool
    data: NewsResponse

class NewsCreatedResponse(BaseModel):
    status: int
    success: bool
    data: NewsResponse

class NewsChangedResponse(BaseModel):
    status: int
    success: bool
    data: NewsResponse

class NewsDeletedResponse(BaseModel):
    status: int
    success: bool