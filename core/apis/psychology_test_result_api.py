from flask import request, Blueprint
from core.apis.user_api import user_api
from core.models.user_model import *
from core.models.psychology_test_result_model import *

psychology_test_result_api = Blueprint('psychology_test_result', __name__,
                                       url_prefix='/psychology_test_result')


@user_api.route('<user_id>/psychology_test_result', methods=['POST'])
def create_test_result(user_id):
    question_id = request.json['question_id']
    result = request.json['result']

    test_result = PsychologyTestResult(question_id=question_id,
                                       result=result)

    user = User.query.get(user_id)
    user.psychology_test_result.append(test_result)

    db.session.commit()

    res = psychology_test_result_schema.jsonify(test_result)

    return res


@psychology_test_result_api.route('', methods=['GET'])
def get_test_results():
    test_results = PsychologyTestResult.query.all()
    res = psychology_test_results_schema.dumps(test_results)

    return res


@user_api.route('<user_id>/psychology_test_result', methods=['GET'])
def get_user_test_results(user_id):
    test_results = PsychologyTestResult.query.filter_by(user_id=user_id)
    res = psychology_test_results_schema.dumps(test_results)

    return res
