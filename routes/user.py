from email import message
from flask import Blueprint, json, jsonify, request
from sqlalchemy import true
from models.Services import Services
from models.Users import Users
from models.Departament import Departament
from models.City import City
from models.Appeals import Appeals
from utils.db import db
from jwt_Functions import validate_token


user = Blueprint('user_routes', __name__)


@user.route('/login', methods=['POST'])
def user_login():
    userInfo = request.json
    email = userInfo["email"]
    password = userInfo["password"]

    userInfo = Users.login(email,password)

    return jsonify({"userInfo":userInfo})


@user.route('/departments', methods=['GET'])
def getDepartment():
    departments = Departament.getAllDepartments()
    return jsonify({"departments":departments})


@user.route('/cities/<int:departmentId>', methods=['GET'])
def user_location(departmentId=5):
    cities = City.getAllcitiesFromDepartment(departmentId)
    return jsonify({"cities":cities})
    

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
    color = userInfo["color"]
    user = Users.validateRegistry(name,lastName,phoneNumber,address,email,password,birthDate,picture,city,color)
    return jsonify({"user":user})


@user.route('/getUser', methods=["POST"])
def getUser():
    token = request.headers["authorization"].split(' ')[1]
    user = Users.searchUserInfoFromToken(token)
    return jsonify({"serviceUser":user})


@user.route('/allowChanges/<email>/<password>', methods=["POST"])
def allowChanges(email,password):
    token = request.headers["authorization"].split(' ')[1]
    response = ""
    try:
        if (validate_token(token,True)['id']):
            userRes = Users.getExistantUser(email,password,1)
            if(userRes[1].get('id')):
                response = True
            else:
                response = False 
    except:
        raise Exception("Invalid Token")
    else:
        return jsonify(response)


@user.route('/appeal')
def appealService():
    token = request.headers["authorization"]
    userInfo = request.json 
    email = userInfo["email"]
    serviceId = userInfo["serviceId"]
    description = userInfo["description"]
    Appeals(description,serviceId)
    return true
    


    
    

 