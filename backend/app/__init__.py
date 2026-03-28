from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        from app import models

    @app.route("/")
    def hello():
        return "<h1>Hey I'm Gonna Be a Great App<h1>"

    db.init_app(app)
    Migrate(app,db)
    CORS(app)

    return app
