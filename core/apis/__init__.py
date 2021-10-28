from flask import Blueprint
from .user_api import user_api
from .record_api import record_api
from .psychology_test_result_api import psychology_test_result_api
from .auth_api import auth_api

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('')
def api_greet():
    return "You're connected to the 'delegate' backend API."


api.register_blueprint(user_api)
api.register_blueprint(record_api)
api.register_blueprint(psychology_test_result_api)
api.register_blueprint(auth_api)
