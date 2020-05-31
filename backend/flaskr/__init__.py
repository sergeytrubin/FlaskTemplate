import os
from flask import (
    Flask,
    jsonify
)
from models import setup_db, Pland
from flask_cors import CORS

def create_app(test_config=None):
    # Create and configure app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY = os.urandom(32)
    #     #DATABASE=''
    # )
    setup_db(app)
    CORS(app)

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    def hello():
        return jsonify({'message': 'HELLO WORLD'})

    return app