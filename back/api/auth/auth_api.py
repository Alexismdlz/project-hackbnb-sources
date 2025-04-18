from flask import jsonify, Blueprint, request
from database.init import db
from api.users.users_models import User

auth_api = Blueprint('auth', __name__)


@auth_api.route('/login', methods=['POST'])
def login():
    if "email" not in request.json:
        return {'error': 'Missing email'}, 400
    if "password" not in request.json:
        return {'error': 'Missing password'}, 400

    # Check if user exists
    user: User = User.query.where(User.email == request.json["email"]).first()
    if not user:
        return {'error': 'User not found'}, 404
    
     # Check if user exists
    if not user.is_valid_password(request.json["password"]):
        return {'error': 'Invalid password'}, 401

    return jsonify({})


@auth_api.route('/register', methods=['POST'])
def create_account():
    if "name" not in request.json:
        return {'error': 'Missing name'}, 400
    if "email" not in request.json:
        return {'error': 'Missing email'}, 400
    if "password" not in request.json:
        return {'error': 'Missing password'}, 400

    # Error if user already exists
    existing_user: User = User.query.where(User.email == request.json["email"]).first()
    if existing_user:
        return {'error': 'User with same email already exists'}, 409

    user = User(
        name=request.json["name"],
        email=request.json["email"],
    )

    user.set_password(request.json["password"])
    
    # Create user in database
    db.session.add(user)
    db.session.commit()

    return jsonify({})
