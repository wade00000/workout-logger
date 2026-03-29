from flask import Blueprint,request,jsonify
from app import db
import datetime
from app.models.workout import Workout,WorkoutExercise,WorkoutSet
from sqlalchemy import and_,or_
from flask_jwt_extended import jwt_required,get_jwt_identity

workouts_bp = Blueprint('workouts',__name__,url_prefix='/workouts')

@workouts_bp.route('/create',methods=['POST'])
@jwt_required()
def create_workout():
    data = request.get_json()
    current_user = int(get_jwt_identity())

    routine_id = data.get("routine_id", None)
    timestamp = datetime.datetime.now()
    workout = Workout(timestamp=timestamp,routine_id=routine_id,user_id=current_user)

    try:
        db.session.add(workout)
        db.session.commit()
        message = "Workout Created Succesfully"
        status_code = 201
        
    except Exception as e:
        db.session.rollback()
        print(e)
        message = "Workout Creation Failed"
        status_code = 400
    
    return jsonify({"message":message}),status_code



@workouts_bp.route('/delete/<id>',methods=['DELETE'])
@jwt_required()
def delete_workout(id):
    current_user = int(get_jwt_identity())
    workout = Workout.query.filter(
        and_(Workout.user_id == current_user,Workout.id == id)
    ).first()

    if not workout:
        return jsonify({"message":"Workout not Found"}),404

    try:
        db.session.delete(workout)
        db.session.commit()
        message = "Workout Deleted Succesfully"
        status_code = 200
    
    except Exception as e:
        db.session.rollback()
        message = "Error Deleting Workout"
        status_code = 400
    
    return jsonify({"message":message}),status_code


@workouts_bp.route('/<id>/add-exercise',methods=['POST'])
@jwt_required()
def add_workout_exercise(id):
    current_user = get_jwt_identity()
    
    workout = Workout.query.filter(
         and_(Workout.id == id, Workout.user_id == current_user)
    ).first()

    if not workout:
        return jsonify({"message": "Workout not found"}), 404
    
    data = request.get_json()
    
    exercise_id = data["exercise_id"]
    order_index = WorkoutExercise.query.filter_by(workout_id=id).count() + 1
    workout_exercise = WorkoutExercise(workout_id=id,exercise_id=exercise_id,order_index=order_index)

    try:
        db.session.add(workout_exercise)
        db.session.commit()
        message = "Workout Exercise Added Succesfully"
        status_code = 201
    
    except Exception as e:
        db.session.rollback()
        message = "Error Adding Workout Exercise"
        status_code = 400
    
    return jsonify({"message":message}),status_code

@workouts_bp.route('/exercise/<id>',methods=['POST'])
@jwt_required()
def add_workout_exercise_set(id):
    current_user = get_jwt_identity()
    
    workout_exercise = WorkoutExercise.query.get(id)

    if not workout_exercise:
        return jsonify({"message": "Workout exercise not found"}), 404

    workout = Workout.query.filter(
        and_(Workout.id == workout_exercise.workout_id, Workout.user_id == current_user)
    ).first()

    if not workout:
        return jsonify({"message": "Unauthorized"}), 403
    
    data = request.get_json()
    reps = data["reps"]
    weight = data["weight"]

    workout_set = WorkoutSet(workout_exercise_id=id,reps=reps,weight=weight)

    
    try:
        db.session.add(workout_set)
        db.session.commit()
        message = "Workout Exercise Set Added Succesfully"
        status_code = 201
    
    except Exception as e:
        db.session.rollback()
        message = "Error Adding Workout Exercise Set"
        status_code = 400
    
    return jsonify({"message":message}),status_code


