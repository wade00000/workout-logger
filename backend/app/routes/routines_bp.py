from flask import Blueprint,request,jsonify
from app import db
from app.models.routine import Routine,RoutineExercise,RoutineSet
from sqlalchemy import and_,or_
from flask_jwt_extended import jwt_required,get_jwt_identity

routines_bp = Blueprint('routines',__name__,url_prefix='/routines')


@routines_bp.route('/',methods=['GET'])
@jwt_required()
def index():
    current_user = int(get_jwt_identity())
    routines = Routine.query.filter(Routine.user_id==current_user).all()
    
    return jsonify([{
        "routine_name":routine.routine_name,
        "user_id":routine.user_id} 
        for routine in routines]),200

@routines_bp.route('/create',methods=['POST'])
@jwt_required()
def create_routine():
    data = request.get_json()
    current_user = int(get_jwt_identity())

    routine_name = data["routine_name"]
    routine = Routine(routine_name=routine_name,user_id=current_user)

    try:
        db.session.add(routine)
        db.session.commit()
        message = "Routine Created Succesfully"
        status_code = 201
        
    except Exception as e:
        db.session.rollback()
        print(e)
        message = "Routine Creation Failed"
        status_code = 400
    
    return jsonify({"message":message}),status_code


@routines_bp.route('/delete/<id>',methods=['DELETE'])
@jwt_required()
def delete_routine(id):
    current_user = int(get_jwt_identity())
    routine = Routine.query.filter(
        and_(Routine.user_id == current_user,Routine.id == id)
    ).first()

    if not routine:
        return jsonify({"message":"Routine not Found"}),404

    try:
        db.session.delete(routine)
        db.session.commit()
        message = "Routine Deleted Succesfully"
        status_code = 200
    
    except Exception as e:
        db.session.rollback()
        message = "Error Deleting Routine"
        status_code = 400
    
    return jsonify({"message":message}),status_code


@routines_bp.route('/<id>/add-exercise',methods=['POST'])
@jwt_required()
def add_routine_exercise(id):
    current_user = get_jwt_identity()
    
    routine = Routine.query.filter(
         and_(Routine.id == id, Routine.user_id == current_user)
    ).first()

    if not routine:
        return jsonify({"message": "Routine not found"}), 404
    
    data = request.get_json()
    
    exercise_id = data["exercise_id"]
    order_index = RoutineExercise.query.filter_by(routine_id=id).count() + 1
    routine_exercise = RoutineExercise(routine_id=id,exercise_id=exercise_id,order_index=order_index)

    try:
        db.session.add(routine_exercise)
        db.session.commit()
        message = "Routine Exercise Added Succesfully"
        status_code = 201
    
    except Exception as e:
        db.session.rollback()
        message = "Error Adding Routine Exercise"
        status_code = 400
    
    return jsonify({"message":message}),status_code

@routines_bp.route('/exercise/<id>',methods=['POST'])
@jwt_required()
def add_routine_exercise_set(id):
    current_user = get_jwt_identity()
    
    routine_exercise = RoutineExercise.query.get(id)

    if not routine_exercise:
        return jsonify({"message": "Routine exercise not found"}), 404

    routine = Routine.query.filter(
        and_(Routine.id == routine_exercise.routine_id, Routine.user_id == current_user)
    ).first()

    if not routine:
        return jsonify({"message": "Unauthorized"}), 403
    
    data = request.get_json()
    reps = data["reps"]
    weight = data["weight"]

    routine_set = RoutineSet(routine_exercise_id=id,reps=reps,weight=weight)

    
    try:
        db.session.add(routine_set)
        db.session.commit()
        message = "Routine Exercise Set Added Succesfully"
        status_code = 201
    
    except Exception as e:
        db.session.rollback()
        message = "Error Adding Routine Exercise Set"
        status_code = 400
    
    return jsonify({"message":message}),status_code


