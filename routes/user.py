from flask import Blueprint, json, jsonify, request
from models.users import Users

user = Blueprint('user_routes', __name__)

@user.route('/login')
def user_login():
    userInfo = request.json
    name = userInfo["name"]
    lastName = userInfo["lastName"]
    phoneNumber = userInfo["phoneNumber"]
    address = userInfo["address"]
    email = userInfo["email"]
    password = userInfo["password"]
    birthDate = userInfo["birthDate"]
    picture = userInfo["userPic"]
    city = userInfo["city"]
    rol = userInfo["rol"]
    status = userInfo["status"]

    user = Users(name,lastName,phoneNumber,address,email,password,birthDate,picture,city,rol,status)

    print(user)
    
    return "Login"

@user.route('/registry')
def user_registry():
    return "Registry"