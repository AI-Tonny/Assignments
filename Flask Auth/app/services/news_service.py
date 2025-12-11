from flask import jsonify
from sqlalchemy import case

import random

from ..models import User, News
from ..schemas.news import (
    NewsCreate,
    NewsChange,
    NewsResponse,
    NewsAllResponse,
    NewsOneResponse,
    NewsCreatedResponse,
    NewsChangedResponse,
    NewsDeletedResponse,
)
from ..extensions import db


class NewsService:
    @staticmethod
    def create_news(current_user: User,  news_to_create: NewsCreate):
        news_id = random.randint(1, 100000)
        created_news = News(
            id=news_id,
            user_id=current_user.id,
            title=news_to_create.title,
            content=news_to_create.content,
            category=news_to_create.category
        )

        db.session.add(created_news)
        db.session.commit()

        return jsonify(
            NewsCreatedResponse(
                status=201,
                success=True,
                data=NewsResponse(
                    id=news_id,
                    title=created_news.title,
                    content=created_news.content,
                    category=created_news.category,
                    user_id=current_user.id
                )
            ).dict()
        ), 201

    @staticmethod
    def get_all_news():
        news = News.query.join(User).order_by(
            case(
                (User.role == 'prime', 1),
                else_=2
            ).asc()
        ).all()

        return jsonify(
            NewsAllResponse(
                status=200,
                success=True,
                data=[NewsResponse(id=news_item.id, title=news_item.title, content=news_item.content, category=news_item.category, user_id=news_item.user_id) for news_item in news]
            ).dict()
        ), 200

    @staticmethod
    def get_news_by_id(news_id: int):
        wanted_news = News.query.filter_by(id=news_id).first()

        if wanted_news is None:
            return jsonify({
                "status": 404,
                "success": False,
                "message": "News was not found"
            }), 404

        return jsonify(
            NewsOneResponse(
                status=200,
                success=True,
                data=NewsResponse(
                    id=wanted_news.id,
                    title=wanted_news.title,
                    content=wanted_news.content,
                    category=wanted_news.category,
                    user_id=wanted_news.user_id
                )
            ).dict()
        ), 200

    @staticmethod
    def change_news_by_id(current_user: User, news_id: int, news_with_new_data: NewsChange):
        if current_user.role == "admin":
            news_to_update = News.query.filter_by(id=news_id).first()
        else:
            news_to_update = News.query.where((News.id == news_id) & (News.user_id == current_user.id)).first()

        if news_to_update is None:
            return jsonify({
                "status": 404,
                "success": False,
                "message": "News was not found"
            }), 404

        news_to_update.title = news_with_new_data.title
        news_to_update.content = news_with_new_data.content
        news_to_update.category = news_with_new_data.category

        db.session.commit()

        return jsonify(
            NewsChangedResponse(
                status=200,
                success=True,
                data=NewsResponse(
                    id=news_to_update.id,
                    title=news_to_update.title,
                    content=news_to_update.content,
                    category=news_to_update.category,
                    user_id=current_user.id
                )
            ).dict()
        ), 200

    @staticmethod
    def delete_news(current_user: User, news_id: int):
        if current_user.role == "admin":
            news_to_delete = News.query.filter_by(id=news_id).first()
        else:
            news_to_delete = News.query.where((News.id == news_id) & (News.user_id == current_user.id)).first()

        if news_to_delete is None:
            return jsonify({
                "status": 404,
                "success": False,
                "message": "News was not found"
            }), 404

        db.session.delete(news_to_delete)
        db.session.commit()

        return jsonify(
            NewsDeletedResponse(
                status=200,
                success=True,
            ).dict()
        ), 200