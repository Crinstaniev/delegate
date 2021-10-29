import datetime

from flask import request, Blueprint, jsonify
from core.apis.user_api import user_api
from core.models.user_model import *
from core.models.record_model import *
from core.apis.wrapper import token_required

record_api = Blueprint('record', __name__, url_prefix='/record')


@user_api.route('/<user_id>/record', methods=['POST'])
def create_record(user_id):
    eth_holding = request.json['eth_holding']
    vta = request.json['vta']
    roi_1 = request.json['roi_1']
    roi_3 = request.json['roi_3']
    roi_2 = request.json['roi_2']
    decision_phase = request.json['decision_phase']
    decision_maker = request.json['decision_maker']
    cash = request.json['cash']
    time = datetime.datetime.now()

    record = Record(time=time, cash=cash, eth_holding=eth_holding,
                    vta=vta, roi_1=roi_1, roi_2=roi_2, roi_3=roi_3,
                    decision_phase=decision_phase,
                    decision_maker=decision_maker)

    user = User.query.get(user_id)
    user.records.append(record)

    db.session.commit()

    res = record_schema.jsonify(record)
    return res


@user_api.route('current/record', methods=['POST'])
@token_required
def create_record_current_user(user):
    eth_holding = request.json['eth_holding']
    vta = request.json['vta']
    roi_1 = request.json['roi_1']
    roi_3 = request.json['roi_3']
    roi_2 = request.json['roi_2']
    decision_phase = request.json['decision_phase']
    decision_maker = request.json['decision_maker']
    cash = request.json['cash']
    time = datetime.datetime.now()

    record = Record(time=time, cash=cash, eth_holding=eth_holding,
                    vta=vta, roi_1=roi_1, roi_2=roi_2, roi_3=roi_3,
                    decision_phase=decision_phase,
                    decision_maker=decision_maker)

    user.records.append(record)

    db.session.commit()

    return record_schema.jsonify(record)


@record_api.route('', methods=['GET'])
def get_records():
    records = Record.query.all()
    res = records_schema.dumps(records)

    return res


@record_api.route('<record_id>', methods=['GET'])
def get_record(record_id):
    record = Record.query.get(record_id)
    res = record_schema.jsonify(record)

    return res


@user_api.route('<user_id>/record', methods=['GET'])
def get_user_records(user_id):
    records = Record.query.filter_by(user_id=user_id).all()
    res = records_schema.dumps(records)

    return res


# fetch latest record of current user
@user_api.route('current/record/latest', methods=['GET'])
@token_required
def get_latest_record(user):
    record = Record.query.filter_by(user=user).order_by(Record.id.desc()).first()
    return record_schema.jsonify(record)
