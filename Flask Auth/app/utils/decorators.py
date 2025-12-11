from flask import jsonify, request, current_app
import jwt

from functools import wraps

from ..models import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({
                "status": 401,
                "success": False,
                "message": "Token is missing!"
            }), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(id=data['user_id']).first()

            if not current_user:
                return jsonify({
                    "status": 404,
                    "success": False,
                    "message": "User not found!"
                }), 404

        except Exception as e:
            return jsonify({
                "status": 401,
                "success": False,
                "message": "Token is invalid!"
            }), 401

        return f(current_user, *args, **kwargs)

    return decorated

def roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            current_user = args[0] if args else None

            if current_user is None:
                return jsonify({
                    "status": 401,
                    "success": False,
                    "message": "User unauthorized"
                })

            if current_user.role not in roles:
                return jsonify({
                    "status": 403,
                    "success": False,
                    "message": "You do not have permission to access this resource"
                }), 403

            return f(*args, **kwargs)
        return wrapper
    return decorator