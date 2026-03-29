from flask import Blueprint
from app.models.workout import Workout

workouts_bp = Blueprint('workouts',__name__,url_prefix='/workouts')