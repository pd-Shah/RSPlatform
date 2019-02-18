import os

from flask import Flask
from flask_pymongo import PyMongo

from .resources.user import user_blueprint
from . import auth

# 1!Ahelloworld

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MONGO_URI="mongodb://localhost:27017/test"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(user_blueprint, url_prefix="/api/v1")
    app.register_blueprint(auth.bp, url_prefix="/auth")

    @app.route('/', methods=["GET", ])
    def hello_world():
        return "server is running..."

    return app
