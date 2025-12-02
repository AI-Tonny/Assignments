from pydantic import BaseModel, EmailStr, Field
from typing import Any

class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=24)

class UserLogin(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=24)

class UserResponse(BaseModel):
    username: str
    email: EmailStr
    message: str

class RegisterResponse(BaseModel):
    status: int
    success: bool
    data: UserResponse

class LoginUserData(BaseModel):
    user: UserResponse
    jwt: str
    token_type: str
    expires_in: Any

class LoginResponse(BaseModel):
    status: int
    success: bool
    data: LoginUserData
