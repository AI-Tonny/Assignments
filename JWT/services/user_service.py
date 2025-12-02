from JWT.database import user_db
from JWT.models import User, UserCreate
from JWT.services import AuthService
from JWT.utils import user_id_gen

class UserService:
    @staticmethod
    def create_user(user: UserCreate) -> User:
        new_user = User(
            id=next(user_id_gen),
            username=user.username,
            email=user.email,
            hashed_password=AuthService.get_password_hash(user.password)
        )

        user_db.append(new_user)
        return new_user

    @staticmethod
    def get_user_by_username(username: str) -> User | None:
        return next((user for user in user_db if user.username == username), None)
