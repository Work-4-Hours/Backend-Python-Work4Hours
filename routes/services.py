
from distutils.log import info
from re import search
from flask import Blueprint, json, jsonify, request, session, render_template
from models.Services import Services
from models.Qualification import Qualification
from utils.db import db


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
    res = Services.updateServiceInfo(sId,sCategory,sName,sPhoto,sType,sPrice,sDescription)
    return jsonify(res)

@services.route('/serviceInfo/<int:idservicio>/<int:usuario>',methods=["POST"])
def getServiceInfo(idservicio,usuario):
    queryInfo = {idservicio,usuario}
    serviceInfo = Services.extractServiceInfo(queryInfo)
    return serviceInfo
