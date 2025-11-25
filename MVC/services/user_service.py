from typing import Optional, List

from MVC.models.user import user_db, User, UserCreate, UserUpdate
from MVC.utils.id_generator import id_gen


class UserService:
    @staticmethod
    def create_user(user: UserCreate) -> User:
        new_user = User(
            id=next(id_gen),
            name=user.name,
            email=user.email,
            age=user.age
        )
        user_db.append(new_user)
        return new_user

    @staticmethod
    def get_all_users(adult_only: bool = False, name_filter: Optional[str] = None) -> List[User]:
        filtered_users = user_db.copy()

        if adult_only:
            filtered_users = [user for user in filtered_users if user.age >= 18]

        if name_filter:
            filtered_users = [user for user in filtered_users if name_filter.lower() == user.name.lower()]

        return filtered_users

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        return next((user for user in user_db if user.id == user_id), None)

    @staticmethod
    def change_user(user_to_update: User, user_with_new_data: UserUpdate) -> User:
        user_to_update.name = user_with_new_data.name
        user_to_update.email = user_with_new_data.email
        user_to_update.age = user_with_new_data.age

        user_db_id = user_db.index(user_to_update)
        user_db[user_db_id] = user_to_update
        return user_to_update

    @staticmethod
    def delete_user(user_to_delete: User) -> None:
        user_db_id = user_db.index(user_to_delete)
        del user_db[user_db_id]
