from app import db,create_app
from app.models.exercise import Exercise
# from faker import Faker

# fake = Faker()

app = create_app()

exercise_names = [
    "Bench Press",
    "Squat",
    "Deadlift",
    "Overhead Press",
    "Pull-Up",
    "Push-Up",
    "Barbell Row",
    "Dumbbell Curl",
    "Tricep Dip",
    "Lateral Raise"
]

with app.app_context():
    if Exercise.query.first() is None:
        for name in exercise_names:
            exercise = Exercise(exercise_name=name,is_custom=False)
            db.session.add(exercise)
        
        db.session.commit()
        print("Exercises seeded successfully")
    else:
        print("Database already has exercises, skipping seed")