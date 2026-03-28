from app import db

class Routine(db.Model):
    __tablename__ = 'routines'

    id = db.Column(db.Integer,primary_key=True)
    routine_name = db.Column(db.String)
    user_id = db.Column(db.ForeignKey('users.id'))

    user = db.relationship("User",backref="routines")


class RoutineExercise(db.Model):
    __tablename__ = 'routine_exercises'

    id = db.Column(db.Integer, primary_key=True)
    routine_id = db.Column(db.ForeignKey('routines.id'))
    exercise_id = db.Column(db.ForeignKey('exercises.id'))
    order_index = db.Column(db.Integer)

    routine = db.relationship('Routine',backref='routine_exercise')
    exercise = db.relationship('Exercise',backref='routine_exercise')


class RoutineSet(db.Model):
    __tablename__ = 'routine_sets'

    id = db.Column(db.Integer, primary_key=True)
    routine_exercise_id = db.Column(db.ForeignKey('routine_exercises.id'))
    reps = db.Column(db.Integer)
    weight = db.Column(db.Integer)

    routine_exercise = db.relationship('RoutineExercise',backref='routine_sets')
