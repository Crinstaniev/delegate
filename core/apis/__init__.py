from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('')
def api_greet():
    return "You're connected to the 'delegate' backend API."
