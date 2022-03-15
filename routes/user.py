from flask import Blueprint, json, jsonify, request

user = Blueprint('user_routes', __name__)

@user.route('/login')
def user_login():
    userInfo = request.json
    name = userInfo["name"]
    lastName = userInfo["lastName"]
    phoneNumber = userInfo["phoneNumber"]
    
    return "Login"

@user.route('/registry')
def user_registry():
    return "Registry"