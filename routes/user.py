from flask import Blueprint, json, jsonify, request
from models.Qualification import Qualification
from models.Services import Services
from models.Users import Users
from models.Departament import Departament
from models.City import City
from models.Appeals import Appeals
from utils.db import db
from sqlalchemy.sql import text
from jwt_Functions import validate_token, write_token
from email_service import email_client


user = Blueprint('user_routes', __name__)


@user.route('/login', methods=['POST'])
def user_login():
    userInfo = request.json
    email = userInfo["email"]
    password = userInfo["password"]

    userInfo = Users.login(email,password)
    try:
        userId = validate_token(userInfo["token"],True)
        qualification = Qualification.get_user_qualification_avg(userId["userId"])
    except:
        return jsonify({"userInfo":userInfo})
    else:
        return jsonify({"userInfo":userInfo},qualification)


@user.route('/departments', methods=['GET'])
def get_department():
    departments = Departament.get_all_departments()
    return jsonify({"departments":departments})


@user.route('/cities/<int:departmentId>', methods=['GET'])
def user_location(departmentId=5):
    cities = City.get_all_cities_from_department(departmentId)
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
    user = Users.validate_registry(name,lastName,phoneNumber,address,email,password,birthDate,picture,city,color)
    return jsonify({"user":user})


@user.route('/getUser', methods=["POST"])
def get_user():
    token = request.headers["authorization"].split(' ')[1]
    user = Users.search_user_info(token)
    return jsonify({"serviceUser":user})


@user.route('/allowChanges/<email>/<password>', methods=["POST"])
def allow_changes(email,password):
    token = request.headers["authorization"].split(' ')[1]
    response = ""
    print(token)
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


@user.route('/appeal', methods=["POST"])
def appeal_service():
    token = request.headers["authorization"]
    userInfo = request.json 
    email = userInfo["email"]
    serviceId = userInfo["serviceId"]
    description = userInfo["description"]
    Appeals(description,serviceId)
    return {"info":True}
    


@user.route('/recoverPassword/<email>')
def recover_password(email):
    userInfo = {}
    db_user = db.session.execute(db.session.query(Users).filter(Users.correo == email))
    for user in db_user.scalars():
        userInfo={
            "userId":user.idusuario,
            "rol":user.rol
        }
    token = write_token(userInfo)
    email_client.send_email(email,"Access link to recover password",message=f'http://localhost:3000/password/forgotten?id={token}',
    format = 
    """
    <h1>Work4Hours</h1>
    <p>Recovery password request<p>
    """)
    return "Se envió el email"


@user.route('/changePassword/<newPassword>')
def change_password(newPassword):
    token = request.headers["authorization"].split(' ')[1]
    try:
        userInfo = validate_token(token,True)
        db.session.execute(text('UPDATE usuarios SET contrasenna = :newPassword WHERE idusuario = :id').bindparams(
            newPassword = newPassword,
            id = userInfo['userId']
        ))
        db.session.commit()
    except:
        return "Invalid token"
    else:
        return True


@user.route('/updateUser', methods=["POST"])
def changeUserInfo():
    token = request.headers["authorization"].split(' ')[1]
    userInfo = request.json
    try:
        decryptedToken = validate_token(token,True)
        if(decryptedToken["userId"]):
            Users.update_user_info(decryptedToken["userId"],**userInfo)
    except:
        return {"info":'Invalid token'}
    else:
        return {"info":"User updated"} 
        

@user.route('/validate')
def validate():
    token = request.headers["authorization"].split(' ')[1]
    decryptedToken = validate_token(token,True)
    if(type(decryptedToken) == dict):
        return {"info":"Valid token"}
    return {"info":"Invalid token"}
        

