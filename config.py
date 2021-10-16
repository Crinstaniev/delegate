from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
db_path = path.join(basedir, 'db.sqlite3')
load_dotenv(path.join(basedir, '.env'))


class Config:
    FLASK_ENV = 'development'

    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
