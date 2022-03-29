from distutils.log import info
from re import search
from flask import Blueprint, json, jsonify, request, session, render_template
from models.objects import Services
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


@services.route('/showServices')
def showServices():
    services = Services.searchAllServicesInfo()
    return f"{services}"

@services.route('/searchServices')
def search():
    serviceInfo = request.json
    serviceName = serviceInfo["serviceName"]
    serviceUser = serviceInfo["serviceUser"]

    serviceInfo = Services.searchServices(serviceName, serviceUser)

    return jsonify(serviceInfo)
