from fastapi import APIRouter, HTTPException, Depends, status

from datetime import timedelta

from JWT.services import UserService, AuthService
from JWT.schemas.user import (
    UserRegister,
    UserLogin,
    UserResponse,
    RegisterResponse,
    LoginUserData,
    LoginResponse
)
from JWT.models import User

user_router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

@user_router.post("/register/", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(user: UserRegister):
    if UserService.get_user_by_username(user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with name '{user.username}' already exists"
        )

    UserService.create_user(user)

    return RegisterResponse(
        success=True,
        status=201,
        data=UserResponse(
            username=user.username,
            email=user.email,
            message="User successfully created"
        )
    )

@user_router.post("/login/", response_model=LoginResponse, status_code=status.HTTP_200_OK)
async def login(user_creds: UserLogin):
    user = UserService.get_user_by_username(user_creds.username)

    if user is None:
       raise HTTPException(
           status_code=status.HTTP_401_UNAUTHORIZED,
           detail=f"User with name '{user_creds.username}' doesn't exist"
       )

    is_password_valid = AuthService.verify_password(user_creds.password, user.hashed_password)

    if not is_password_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Password is incorrect"
        )

    access_token = AuthService.create_access_token(
        data={
            "id": user.id
        },
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return LoginResponse(
        status=200,
        success=True,
        data=LoginUserData(
            user=UserResponse(
                username=user.username,
                email=user.email,
                message="You have successfully logged in"
            ),
            jwt=access_token,
            token_type="bearer",
            expires_in=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

@user_router.get("/profile/")
async def get_profile(current_user: User = Depends(AuthService.get_current_user)):
    return {
        "username": current_user.username,
        "email": current_user.email,
        "message": "Here is your profile"
    }