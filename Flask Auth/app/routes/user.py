from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from ..services import AuthService, UserService
from ..models import User
from ..utils import token_required, roles_required
from ..schemas.user import UserRegister, UserLogin

user_bp = Blueprint("user", __name__)

@user_bp.route("/api/register", methods=['POST'])
def register():
    try:
        user_to_register = UserRegister(**request.json)

        return AuthService.register_user(user_to_register)
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "success": False,
            "errors": e.errors()
        }), 400
    except Exception as e:
        return jsonify({
            "status": 500,
            "success": False,
            "message": str(e)
        }), 500

@user_bp.route("/api/login", methods=['POST'])
def login():
    try:
        user_to_login = UserLogin(**request.json)

        return AuthService.login_user(user_to_login)
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "success": False,
            "errors": e.errors()
        }), 400
    except Exception as e:
        return jsonify({
            "status": 500,
            "success": False,
            "message": str(e)
        }), 500

@user_bp.route("/api/profile", methods=['GET'])
@token_required
def get_profile(current_user: User):
    try:
        return UserService.get_profile(current_user)
    except Exception as e:
        return jsonify({
            "status": 500,
            "success": False,
            "message": str(e)
        }), 500

@user_bp.route("/api/get_users", methods=['GET'])
@token_required
@roles_required("admin")
def get_all_users(current_user: User):
    try:
        return UserService.get_all_users()
    except Exception as e:
        return jsonify({
            "status": 500,
            "success": False,
            "message": str(e)
        }), 500

@user_bp.route("/api/get_user/<int:user_id>", methods=['GET'])
@token_required
@roles_required("admin")
def get_user_by_id(current_user: User, user_id: int):
    try:
        return UserService.get_user_by_id(user_id)
    except Exception as e:
        return jsonify({
            "status": 500,
            "success": False,
            "message": str(e)
        }), 500

@user_bp.route("/api/give_role_to_user", methods=['POST'])
@token_required
@roles_required("admin")
def give_role_to_user(current_user: User):
    try:
        user_id = request.args.get("user_id", None)
        role = request.args.get("role", None)

        if user_id is None or role is None:
            return jsonify({
                "status": 400,
                "success": False,
                "message": "You didn't provide 'user_id' or 'role' through 'query params'"
            })

        return UserService.give_role_to_user(user_id, role)
    except Exception as e:
        return jsonify({
            "status": 500,
            "success": False,
            "message": str(e)
        }), 500