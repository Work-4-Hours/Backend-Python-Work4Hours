from flask import Blueprint, json, jsonify, request, session
from models.objects import  Services
from utils.db import db

services = Blueprint('service_routes', __name__)

@services.route('/asas')
def showServices():

    
    return f"HOLA"

@services.route('/serviceRegistry')
def user_registry():
    serviceInfo = request.json
    serviceCategories = serviceInfo["serviceCategories"]
    serviceName = serviceInfo["serviceName"]
    serviceStatuses = serviceInfo["serviceStatuses"]
    serviceType = serviceInfo["serviceType"]
    servicePrice = serviceInfo["servicePrice"]
    serviceDescription = serviceInfo["serviceDescription"]
    servicePhoto = serviceInfo["servicePhoto"]
    serviceUser = serviceInfo["serviceUser"]

    return "Service registry"

