from flask import Blueprint

user = Blueprint('user_routes', __name__)

@user.route('/login')
def user_login():
    return "Hola2"

@user.route('/registry')
def user_registry():
    return "hello"