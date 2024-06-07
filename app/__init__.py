from flask import Flask
from app.controllers.routes.app import user_route
import os


def create_app():
    app = Flask(__name__)

    app.register_blueprint(user_route)

    return app