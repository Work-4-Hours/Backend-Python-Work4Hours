from flask import Blueprint, json, jsonify, request
from models.Users import Users
from utils.db import db

user = Blueprint('user_routes', __name__)


@user.route('/login', methods=['POST'])
def user_login():
    userInfo = request.json
    email = userInfo["email"]
    password = userInfo["password"]

    userInfo = Users.login(email,password)

    return jsonify(userInfo)
    

@user.route('/registry', methods=['POST'])
def user_registry():
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

    user = Users.validateRegistry(name,lastName,phoneNumber,address,email,password,birthDate,picture,city)

    return jsonify(user)

    
