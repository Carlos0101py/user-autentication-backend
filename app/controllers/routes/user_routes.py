from flask import Blueprint


user_route = Blueprint('user_routes', __name__)

@user_route.get('/')
def index_page():
    return 'hellow'