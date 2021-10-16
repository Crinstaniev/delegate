from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

from .user_model import *
from .record_model import *
from .psychology_test_result_model import *
