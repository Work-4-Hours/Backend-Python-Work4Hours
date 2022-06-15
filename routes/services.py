from flask import Blueprint, jsonify, request
from models.Services import Services
from models.Qualification import Qualification
from utils.db import db
from jwt_Functions import validate_token, write_token
from schemas import ServiceModel
from services.service_service import ServicesService


services = Blueprint('service_routes', __name__)

@services.route('/')
def show_services():
    services = ServicesService.get_index_services()
    if(not services):
        return {"info": "There`s no services"}
    return {"services":services}


@services.route('/avg', methods=["POST"])
def get_average():
    getInfo = request.json
    average = Qualification.get_qualifications_average(getInfo["userId"])
    return jsonify(average)


@services.route('/serviceRegistry', methods=['POST'])
def service_registry():
    serviceInfo =ServiceModel(**request.json)
    service = ServicesService.create_service(serviceInfo)
    return jsonify(service)


@services.route('/searchServices', methods=['POST'])
def search():
    serviceInfo = request.json  
    serviceInfo = ServicesService.search_services(serviceInfo["serviceName"])
    if(not serviceInfo):
        return {"info": "There`s no services"}
    return jsonify(serviceInfo)


# @services.route('/addQualification')
# def add_qualification():
#     serviceInfo = request.json
#     calificacion = serviceInfo["calificacion"]
#     serviceInfo = Qualification.add_qualification(calificacion)
#     return jsonify(serviceInfo)


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