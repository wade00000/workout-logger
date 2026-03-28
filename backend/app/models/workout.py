from app import db

class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer,primary_key=True)
    timestamp = db.Column(db.DateTime)
    routine_id = db.Column(db.ForeignKey('routines.id'))
    user_id = db.Column(db.ForeignKey('users.id'))

    routines = db.relationship("Routine",backref="workouts")
    user = db.relationship("User",backref="workouts")

class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.ForeignKey('workouts.id'))
    exercise_id = db.Column(db.ForeignKey('exercises.id'))
    order_index = db.Column(db.Integer)

    workout = db.relationship('Workout',backref='workout_exercise')
    exercise = db.relationship('Exercise',backref='workout_exercise')


class WorkoutSet(db.Model):
    __tablename__ = 'workout_sets'

    id = db.Column(db.Integer, primary_key=True)
    workout_exercise_id = db.Column(db.ForeignKey('workout_exercises.id'))
    reps = db.Column(db.Integer)
    weight = db.Column(db.Integer)

    workout_exercise = db.relationship('WorkoutExercise',backref='workout_sets')