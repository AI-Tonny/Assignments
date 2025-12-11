from flask import jsonify

from ..models import User
from ..extensions import db

class UserService:
    @staticmethod
    def get_profile(current_user: User):
        return jsonify({
            "status": 200,
            "success": True,
            "data": {
                "id": current_user.id,
                "username": current_user.username,
                "email": current_user.email,
                "role": current_user.role
            }
        }), 200

    @staticmethod
    def get_all_users():
        all_users = User.query.all()

        return jsonify({
            "status": 200,
            "success": True,
            "data": [{"id": user.id, "username": user.username, "email": user.email, "role": user.role} for user in all_users]
        }), 200

    @staticmethod
    def get_user_by_id(user_id: int):
        wanted_user = User.query.filter_by(id=user_id).first()

        if wanted_user is None:
            return jsonify({
                "status": 404,
                "success": False,
                "message": "User was not found",
                "data": None
            }), 404

        return jsonify({
            "status": 200,
            "success": True,
            "message": "User was found successfully",
            "data": {
                "id": wanted_user.id,
                "username": wanted_user.username,
                "email": wanted_user.email,
                "role": wanted_user.role
            }
        }), 200

    @staticmethod
    def give_role_to_user(user_id: int, role: str):
        user = User.query.filter_by(id=user_id).first()

        if user is None:
            return jsonify({
                "status": 404,
                "success": False,
                "message": "User was not found",
                "data": None
            }), 404

        user.role = role
        db.session.commit()

        return jsonify({
            "status": 200,
            "success": True,
            "message": "Role has been changed successfully",
            "data": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
        }), 200
