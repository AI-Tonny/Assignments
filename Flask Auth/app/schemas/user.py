from pydantic import BaseModel, Field, EmailStr

class UserRegister(BaseModel):
    username: str = Field(..., min_length=1, max_length=20)
    password: str = Field(..., min_length=1, max_length=24)
    role: str = Field(..., min_length=1, max_length=20)
    email: EmailStr

class UserLogin(BaseModel):
    username: str = Field(..., min_length=1, max_length=20)
    password: str = Field(..., min_length=1, max_length=24)