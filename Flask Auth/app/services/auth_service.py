from flask import jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

import datetime
import random

from ..models import User
from ..schemas.user import UserRegister, UserLogin
from ..extensions import db

class AuthService:
    @staticmethod
    def register_user(user_to_register: UserRegister):
        if User.query.filter_by(username=user_to_register.username).first():
            return jsonify({
                "status": 400,
                "success": False,
                "message": "Username already exists"
            }), 400

        if User.query.filter_by(email=user_to_register.email).first():
            return jsonify({
                "status": 400,
                "success": False,
                "message": "Email already exists"
            }), 400

        hashed_password = generate_password_hash(user_to_register.password)
        user_id = random.randint(1, 100000)
        new_user = User(
            id=user_id,
            username=user_to_register.username,
            password=hashed_password,
            email=user_to_register.email,
            role=user_to_register.role
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "status": 201,
            "success": True,
            "data": user_to_register.dict(),
            "message": "User has successfully registered"
        }), 201

    @staticmethod
    def login_user(user_to_login: UserLogin):
        user = User.query.filter_by(username=user_to_login.username).first()
        is_password_valid = check_password_hash(user.password, user_to_login.password)
        if not user or not is_password_valid:
            return jsonify({
                "status": 401,
                "success": False,
                "message": "Invalid username or password"
            }), 401

        token = jwt.encode({
            "user_id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, current_app.config['SECRET_KEY'], algorithm='HS256')

        return jsonify({
            "status": 200,
            "success": True,
            "message": "You have successfully logged in to your account",
            "data": {
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                "token": token,
                "token_type": "Bearer"
            }
        }), 200