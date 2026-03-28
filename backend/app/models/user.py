from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True)
    password_hash = db.Column(db.String(255))


class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(100))
    user_id = db.Column(db.ForeignKey('users.id'), nullable=True)
    is_custom = db.Column(db.Boolean)

    user = db.relationship("User",backref="exercises")


