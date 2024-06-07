from flask import Blueprint


user_route = Blueprint('app', __name__)

@user_route.get('/')
def index_page():
    return 'hellow'