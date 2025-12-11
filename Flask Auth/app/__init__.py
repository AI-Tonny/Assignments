from flask import Flask

from .extensions import db
from .routes import user_bp, news_bp

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "our-super-secret-key"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///news.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(user_bp)
    app.register_blueprint(news_bp)

    with app.app_context():
        db.create_all()

    return app