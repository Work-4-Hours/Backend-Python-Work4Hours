from distutils.log import info
from flask import Blueprint, json, jsonify, request, session, render_template
from models.Services import Services
from utils.db import db


services = Blueprint('service_routes', __name__)

@services.route('/asas')
def showServices():

    
    return f"HOLA"

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


@services.route('/searchServices')
def search():
    serviceInfo = request.json  
    nombre = serviceInfo["nombre"]
    serviceInfo = Services.searchAllServicesInfo(nombre)

    return jsonify(serviceInfo)


