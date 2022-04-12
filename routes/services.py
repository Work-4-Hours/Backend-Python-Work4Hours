from distutils.log import info
from re import search
from flask import Blueprint, json, jsonify, request, session, render_template
from models.Services import Services
from utils.db import db


services = Blueprint('service_routes', __name__)

@services.route('/')
def showServices():
    services = Services.getIndexPageServices()
    return jsonify({"services":services})

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
