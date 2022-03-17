from flask import Blueprint, json, jsonify, request
from models.users import Users
from utils.db import db

user = Blueprint('user_routes', __name__)

@user.route('/login', methods=['POST'])
def user_login():
    userInfo = request.json
    name = userInfo["name"]
    lastName = userInfo["lastName"]
    phoneNumber = userInfo["phoneNumber"]
    address = userInfo["address"]
    email = userInfo["email"]
    password = userInfo["password"]
    birthDate = userInfo["birthDate"]
    picture = userInfo["picture"]
    city = userInfo["city"]
    rol = userInfo["rol"]
    status = userInfo["status"]

    user = Users(name,lastName,phoneNumber,address,email,password,birthDate,picture,city,rol,status)

    db.session.add(user)
    db.session.commit()
    
    return "Login"

@user.route('/registry')
def user_registry():
    return "Registry"