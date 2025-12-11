from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from ..services import NewsService
from ..models import News, User
from ..utils import token_required, roles_required
from ..schemas.news import (
    NewsCreate,
    NewsChange
)

news_bp = Blueprint("news", __name__)

@news_bp.route("/api/create_news", methods=['POST'])
@token_required
def create_new(current_user: User):
    try:
        news_to_create = NewsCreate(**request.json)

        return NewsService.create_news(current_user, news_to_create)
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

@news_bp.route("/api/get_all_news", methods=['GET'])
@token_required
def get_all_news(current_user: User):
    try:
        return NewsService.get_all_news()
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

@news_bp.route("/api/get_news/<int:news_id>", methods=['GET'])
@token_required
def get_news_by_id(current_user: User, news_id: int):
    try:
        return NewsService.get_news_by_id(news_id)
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

@news_bp.route("/api/change_news/<int:news_id>", methods=['PUT'])
@token_required
def change_news_by_id(current_user: User, news_id: int):
    try:
        news_with_new_data = NewsChange(**request.json)

        return NewsService.change_news_by_id(current_user, news_id, news_with_new_data)
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

@news_bp.route("/api/delete_news/<int:news_id>", methods=['DELETE'])
@token_required
def delete_news_by_id(current_user: User, news_id: int):
    try:
        return NewsService.delete_news(current_user, news_id)
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