from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        from .models import db, ma
        from .apis import api

        db.init_app(app)
        ma.init_app(app)

        app.register_blueprint(api)

        @app.cli.command()
        def init():
            db.create_all()

        @app.cli.command()
        def drop():
            db.drop_all()

        @app.route('/')
        def hello():
            return 'Hello, this is the delegate back-end!'

    CORS(app, resources={r"/*": {"origins": "*"}})
    return app
