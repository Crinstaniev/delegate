import datetime

from flask import request, Blueprint
from core.models.user_model import *

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
    treatment = request.json['treatment']
    rationality = request.json['rationality']
    sign_up_date = datetime.datetime.now()

    user = User(name=name, email=email, sign_up_date=sign_up_date,
                signature=signature, password=password,
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
