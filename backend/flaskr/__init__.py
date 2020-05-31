import os
from flask import (
    Flask,
    jsonify,
    request
)
from .models import setup_db, Plant
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


    @app.route('/plants')
    def get_plants():
        '''
        The "page =..." says:
        look at the arguments of request object and get the value of key 'page'. 
        If key 'page' does not exists assign the default value which is 1 as specifified below. The we specify the type to integer.
        '''
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * 10 # Starting index - start with page '0', because the first page gets the default value of 1.
        end = start + 10 # Ending index - show 10 results per page
        plants = Plant.query.all()
        formatted_plants = [plant.format() for plant in plants]

        return jsonify({
            'success':True,
            'plants': formatted_plants[start:end], # Show results according to starting and enging indexes
            'total_plants': len(formatted_plants) # show total number of records
        })


    return app