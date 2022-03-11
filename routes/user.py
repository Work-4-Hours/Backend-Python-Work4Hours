from flask import Blueprint, json, jsonify, request

user = Blueprint('user_routes', __name__)

@user.route('/login')
def user_login():
    return "Login"

@user.route('/registry')
def user_registry():
    return "Registry"