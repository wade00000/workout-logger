from flask import Blueprint,jsonify,request
from app.models.user import User
from app import bcrypt,db,jwt

users_bp = Blueprint('users',__name__,url_prefix='/users')


@users_bp.route('/',methods=['GET'])
def index():
    users = User.query.all()
    return jsonify([{"id":user.id,"username":user.username} for user in users]),200



@users_bp.route('/register',methods=['POST'])
def register_user():
    data = request.get_json()
    if not data or not data.get("username") or not data.get("email") or not data.get("password"):
        return jsonify({"message": "Missing required fields"}), 400

    username = data["username"]
    email = data["email"]
    pw_hash = bcrypt.generate_password_hash(data["password"]).decode('utf-8')

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "An account with this email already exists"}), 400

    user = User(username=username,email=email,password_hash=pw_hash)

    try:
        db.session.add(user)
        db.session.commit()
        message = "User Registered Succesfully"
        status_code = 201
        
    except Exception as e:
        db.session.rollback()
        print(e)
        message = "User Registration Failed"
        status_code = 400
    
    return jsonify({"message":message}),status_code


@users_bp.route('/login',methods=['POST'])
def login_user():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message":"User does not exist"}),404
    
    
    hash_check = bcrypt.check_password_hash(user.password_hash,password)
    if hash_check:
        access_token = jwt.create_access_token(identity=user.id)
        return jsonify(access_token=access_token),200
    
    else:
        return jsonify({"message":"Wrong Password"}),401

