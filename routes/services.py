
from distutils.log import info
from re import search
from flask import Blueprint, json, jsonify, request, session, render_template
from models.Services import Services
from models.Qualification import Qualification
from utils.db import db
from jwt_Functions import validate_token


services = Blueprint('service_routes', __name__)

@services.route('/')
def showServices():
    services = Services.getIndexPageServices()
    return jsonify(services)


@services.route('/avg', methods=["POST"])
def getAverage():
    getInfo = request.json
    average = Qualification.getQualificationsAverage(getInfo["id"])
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

    service = Services.validateService(categories,name,statuses,type,price,description,photo,user)
    return jsonify(service)


@services.route('/searchServices', methods=['POST'])
def search():
    serviceInfo = request.json  
    nombre = serviceInfo["serviceName"]
    serviceInfo = Services.searchAllServicesInfo(nombre)
    return jsonify(serviceInfo)
    

@services.route('/addQualification')
def addQ():
    serviceInfo = request.json
    calificacion = serviceInfo["calificacion"]
    serviceInfo = Services.addQualification(calificacion)
    return jsonify(serviceInfo)


@services.route('/deleteService/<int:serviceId>')
def deleteService(serviceId = None):
    isDeleted = Services.deleteService(serviceId)
    return jsonify(isDeleted)


@services.route('/updateService', methods=["POST"])
def updateService():
    serviceNewInfo = request.json
    sId = serviceNewInfo["id"]
    sName = serviceNewInfo["name"]
    sType = serviceNewInfo["type"]
    sPhoto = serviceNewInfo["photo"]
    sPrice = serviceNewInfo["price"]
    sCategory = serviceNewInfo["category"]
    sDescription = serviceNewInfo["description"]
    sStatus = serviceNewInfo["status"]
    res = Services.updateServiceInfo(sId,sCategory,sName,sPhoto,sType,sPrice,sDescription,sStatus)
    return jsonify(res)

@services.route('/serviceInfo/<int:serviceId>',methods=["POST"])
def getServiceInfo(serviceId):
    serviceInfo = Services.getServiceInfo(serviceId)
    return jsonify(serviceInfo)


@services.route('/getUserServices/<int:userId>')
def getUserServices(userId):
    token = request.headers["authorization"].split(' ')[1]
    userInfo = {}
    services = []
    try:
        if (validate_token(token,True)['id']):
            services,userInfo = Services.getServicesFromUser(userId,token)
    except:
        raise Exception("Invalid Token")
    else:
        return jsonify(services,userInfo)