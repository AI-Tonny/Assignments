from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException, Depends

from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional

from JWT.core import settings
from JWT.database import user_db

SECRET_KEY: str = settings.JWT_SECRET_KEY
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

class AuthService:
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
        to_encode.update({
            "exp": expire
        })
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def verify_token(token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id: str = payload.get("id")
            if user_id is None:
                raise HTTPException(status_code=401, detail="Not valid token")
            return user_id
        except JWTError:
            raise HTTPException(status_code=401, detail="Not valid token")

    @staticmethod
    def get_password_hash(password: str):
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_current_user(creds: HTTPAuthorizationCredentials = Depends(security)):
        token = creds.credentials
        user_id = AuthService.verify_token(token)
        user = next(filter(lambda user: user.id == user_id, user_db))
        if not user:
            raise HTTPException(status_code=404, detail="User was not found")
        return user
