import os

from flask import Flask, jsonify
from microservice.myapp import MyApp

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    myapp = MyApp()

    # a simple page that says hello
    @app.route('/myapp/search/')
    def search():
        res = myapp.search()
        return jsonify(res)

    @app.route('/myapp/register/', methods=["POST"])
    def register():
        res = myapp.register()
        return jsonify(res)

    return app
