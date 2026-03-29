from app import db
from app.models.exercise import Exercise
from flask import Blueprint,jsonify,request
from flask_jwt_extended import jwt_required,get_jwt_identity
from sqlalchemy import or_,and_

exercises_bp = Blueprint('exercises',__name__,url_prefix='/exercises')

@exercises_bp.route('/',methods=['GET'])
@jwt_required()
def index():
    current_user = int(get_jwt_identity())
    exercises = Exercise.query.filter(
        or_(Exercise.user_id==None,Exercise.user_id==current_user)
    ).all()
    
    return jsonify([{
        "id":exercise.id,
        "exercise_name":exercise.exercise_name,
        "user_id":exercise.user_id,
        "is_custom":exercise.is_custom} 
        for exercise in exercises]),200

@exercises_bp.route('/create',methods=['POST'])
@jwt_required()
def create_exercise():
    current_user = int(get_jwt_identity())
    data = request.get_json()
    exercise_name = data["exercise_name"]

    exercise = Exercise(exercise_name=exercise_name,user_id=current_user,is_custom=True)

    try:
        db.session.add(exercise)
        db.session.commit()
        message = "Exercise Created Succesfully"
        status_code = 201

    except Exception as e:
        db.session.rollback()
        print(e)
        message = "Error Creating Exercise"
        status_code = 400
    
    return jsonify({"message":message}),status_code


@exercises_bp.route('/delete/<id>',methods=['DELETE'])
@jwt_required()
def delete_exercise(id):
    current_user = int(get_jwt_identity())
    exercise = Exercise.query.filter(
        and_(Exercise.user_id == current_user,Exercise.id == id)
    ).first()

    if not exercise:
        return jsonify({"message":"Exercise not Found"}),404

    try:
        db.session.delete(exercise)
        db.session.commit()
        message = "Exercise Deleted Succesfully"
        status_code = 200
    
    except Exception as e:
        db.session.rollback()
        message = "Error Deleting Exercise"
        status_code = 400
    
    return jsonify({"message":message}),status_code





