from flask import Blueprint, request, jsonify, current_app
from core.models.user_model import User
from datetime import datetime, timedelta
from core.apis.wrapper import token_required

import jwt

auth_api = Blueprint('auth', __name__, url_prefix='/auth')


@auth_api.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    user = User.authenticate(email, password)

    if user is None:
        return jsonify(message='authentication failed'), 401

    token = jwt.encode({
        'sub': user.email,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(days=365)},
        current_app.config['SECRET_KEY']
    )

    return jsonify({'token': token})


@auth_api.route('/verify', methods=['GET'])
@token_required
def verify_token(user):
    return jsonify(True)
