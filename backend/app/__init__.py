from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager,create_access_token
from sqlalchemy import MetaData


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=convention))
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from app.routes.users_bp import users_bp
    from app.routes.exercises_bp import exercises_bp
    from app.routes.routines_bp import routines_bp
    from app.routes.workouts_bp import workouts_bp
    app.register_blueprint(users_bp)
    app.register_blueprint(exercises_bp)
    app.register_blueprint(routines_bp)
    app.register_blueprint(workouts_bp)


    @app.route("/")
    def hello():
        return "<h1>Hello World<h1>"

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    Migrate(app,db)
    CORS(app)

    return app
