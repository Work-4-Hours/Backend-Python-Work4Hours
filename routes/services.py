from distutils.log import info
from re import search
from flask import Blueprint, json, jsonify, request, session, render_template
from models.Services import Services
from models.Qualification import Qualification
from utils.db import db
from jwt_Functions import validate_token


services = Blueprint('service_routes', __name__)

@services.route('/')
def show_services():
    services = Services.get_index_page_services()
    print(services)
    return jsonify(services)


@services.route('/avg', methods=["POST"])
def get_average():
    getInfo = request.json
    average = Qualification.get_qualifications_average(getInfo["userId"])
    return jsonify(average)


@services.route('/serviceRegistry', methods=['POST'])
def service_registry():
    serviceInfo = request.json
    categories = serviceInfo["categories"]
    name = serviceInfo["name"]
    statuses = serviceInfo["statuses"]
    type = serviceInfo["type"]
    price = serviceInfo["price"]
    description = serviceInfo["description"]
    photo = serviceInfo["photo"]
    user = serviceInfo["user"]

    service = Services.create_service(categories,name,statuses,type,price,description,photo,user)
    return jsonify(service)


@services.route('/searchServices', methods=['POST'])
def search():
    serviceInfo = request.json  
    nombre = serviceInfo["serviceName"]
    serviceInfo = Services.search_all_services_info(nombre)
    return jsonify(serviceInfo)
    

@services.route('/addQualification')
def add_qualification():
    serviceInfo = request.json
    calificacion = serviceInfo["calificacion"]
    serviceInfo = Qualification.add_qualification(calificacion)
    return jsonify(serviceInfo)


@services.route('/deleteService/<int:serviceId>')
def delete_service(serviceId = None):
    isDeleted = Services.delete_service(serviceId)
    return jsonify(isDeleted)


@services.route('/updateService', methods=["POST"])
def update_service():
    serviceNewInfo = request.json
    sId = serviceNewInfo["id"]
    sName = serviceNewInfo["name"]
    sType = serviceNewInfo["type"]
    sPhoto = serviceNewInfo["photo"]
    sPrice = serviceNewInfo["price"]
    sCategory = serviceNewInfo["category"]
    sDescription = serviceNewInfo["description"]
    sStatus = serviceNewInfo["status"]
    res = Services.update_service_info(sId,sCategory,sName,sPhoto,sType,sPrice,sDescription,sStatus)
    return jsonify(res)

@services.route('/serviceInfo/<int:serviceId>',methods=["POST"])
def get_service_info(serviceId):
    serviceInfo = Services.get_service_info(serviceId)
    serviceQualification = Qualification.get_qualifications_average(serviceId)
    return jsonify(serviceInfo,serviceQualification)


@services.route('/getUserServices/<int:userId>')
def get_user_services(userId):
    token = request.headers["authorization"].split(' ')[1]
    try:
        if (validate_token(token,True)['userId']):
            services,userInfo = Services.get_services_from_user(userId)
            qualification = Qualification.get_user_qualification_avg(userId)
    except:
        raise Exception("Invalid Token")
    else:
        return jsonify(services,userInfo,qualification)