import datetime
import numpy as np

from werkzeug.security import generate_password_hash
from flask import request, Blueprint, jsonify
from core.models.user_model import *
from core.apis.wrapper import token_required

user_api = Blueprint('user', __name__, url_prefix='/user')


@user_api.route('', methods=['GET'])
def get_users():
    users = User.query.all()
    res = users_schema.dumps(users)

    return res


@user_api.route('<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    res = user_schema.jsonify(user)

    return res


@user_api.route('', methods=['POST'])
def create_user():
    name = request.json['name']
    email = request.json['email']
    signature = request.json['signature']
    password = request.json['password']
    treatment = np.random.randint(0, 2)
    rationality = False
    sign_up_date = datetime.datetime.now()

    duplication_check = User.query.filter_by(email=email).first()
    if duplication_check is not None:
        return jsonify(message="email is duplicated"), 409

    user = User(name=name, email=email, sign_up_date=sign_up_date,
                signature=signature, password=generate_password_hash(password, method='sha256'),
                treatment=treatment, rationality=rationality)

    db.session.add(user)
    db.session.commit()

    res = user_schema.jsonify(user)

    return res


@user_api.route('<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    user.name = request.json['name']
    user.email = request.json['email']
    user.password = request.json['password']
    user.treatment = request.json['treatment']
    user.rationality = request.json['rationality']

    db.session.commit()

    res = user_schema.jsonify(user)

    return res


@user_api.route('current', methods=['GET'])
@token_required
def get_current_user(current_user):
    return user_schema.jsonify(current_user)
