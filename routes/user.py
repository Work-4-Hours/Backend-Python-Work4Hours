from flask import Blueprint, jsonify, request
from models.Qualification import Qualification
from models.Services import Services
from models.Users import Users
from models.Departament import Departament
from models.City import City
from models.Appeals import Appeals
from services.user_service import UserService
from schemas import UserLogin, UserSignup
from utils.db import db
from jwt_Functions import validate_token, write_token
from email_service import email_client


user = Blueprint('user_routes', __name__)


@user.route('/login', methods=['POST'])
def user_login():
    print(request.json)
    user_to_login = UserLogin(**request.json)
    user = UserService.login(user_to_login)
    if not user:
        return {"exist":False}
    token = str(write_token({"userId":user.userId,"rol":user.role})).split("'")[1]
    return {
        "info": user.dict(exclude= {"userId","role"}), 
        "token":token
        }


@user.route('/departments', methods=['GET'])
def get_department():
    departments = Departament.getAllDepartments()
    return jsonify({"departments":departments})


# @user.route('/cities/<int:departmentId>', methods=['GET'])
# def user_location(departmentId=5):
#     cities = City.get_all_cities_from_department(departmentId)
#     return jsonify({"cities":cities})
    

@user.route('/registry', methods=['POST'])
def user_registry():
    user_to_signup = UserSignup(**request.json)
    registry_response = UserService.signup(user_to_signup)
    if not registry_response:
        return {"exist":"User already exist"}
    return {"exist":"New user created"}
    # userInfo = request.json
    # name = userInfo["name"]
    # lastName = userInfo["lastName"]
    # phoneNumber = userInfo["phoneNumber"]
    # address = userInfo["address"]
    # email = userInfo["email"]
    # password = userInfo["password"]
    # birthDate = userInfo["birthDate"]
    # picture = userInfo["picture"]
    # city = userInfo["city"]
    # color = userInfo["color"]
    # user = Users.validate_registry(name,lastName,phoneNumber,address,email,password,birthDate,picture,city,color)
    # return jsonify({"user":user})

@user.route('/getUser', methods=["POST"])
def get_user():
    token = request.headers["authorization"].split(' ')[1]
    user = Users.search_user_info(token)
    return jsonify({"serviceUser":user})


@user.route('/allowChanges/<email>/<password>', methods=["POST"])
def allow_changes(email,password):
    token = request.headers["authorization"].split(' ')[1]
    response = ""
    try:
        if (validate_token(token,True)['userId']):
            userRes = Users.get_existant_user(email,password,1)
            if(userRes[1].get('userId')):
                response = True
            else:
                response = False 
    except:
        raise Exception("Invalid Token")
    else:
        return jsonify(response)


@user.route('/appeal')
def appeal_service():
    token = request.headers["authorization"]
    userInfo = request.json 
    email = userInfo["email"]
    serviceId = userInfo["serviceId"]
    description = userInfo["description"]
    Appeals(description,serviceId)
    return True
    


    
    

 