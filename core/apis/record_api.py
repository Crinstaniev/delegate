import datetime

from flask import request, Blueprint
from core.apis.user_api import user_api
from core.models.user_model import *
from core.models.record_model import *

record_api = Blueprint('record', __name__, url_prefix='/record')


@user_api.route('/<user_id>/record', methods=['POST'])
def create_record(user_id):
    eth_holding = request.json['eth_holding']
    vta = request.json['vta']
    roi = request.json['roi']
    decision_phase = request.json['decision_phase']
    decision_maker = request.json['decision_maker']
    cash = request.json['cash']
    time = datetime.datetime.now()

    record = Record(time=time, cash=cash, eth_holding=eth_holding,
                    vta=vta, roi=roi, decision_phase=decision_phase,
                    decision_maker=decision_maker)

    user = User.query.get(user_id)
    user.records.append(record)

    db.session.commit()

    res = record_schema.jsonify(record)
    return res


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
