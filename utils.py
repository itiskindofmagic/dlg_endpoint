from flask import Flask, Blueprint

from config import DevConfig


def sum_numbers(numbers):
    return sum(iter(numbers))


def create_app(config_obj=DevConfig):
    app = Flask(__name__)
    bp = Blueprint('app', __name__)
    app.config.from_object(config_obj)
    app.register_blueprint(bp)
    return app
