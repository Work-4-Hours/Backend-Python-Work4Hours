from flask import Blueprint, json, jsonify, request

services = Blueprint('service_routes', __name__)

@services.route('/services')
def user_login():
    serviceInfo = request.json
    serviceCategories = serviceInfo["serviceCategories"]
    serviceName = serviceInfo["serviceName"]
    serviceStatuses = serviceInfo["serviceStatuses"]
    serviceType = serviceInfo["serviceType"]
    servicePrice = serviceInfo["servicePrice"]
    serviceDescription = serviceInfo["serviceDescription"]
    servicePhoto = serviceInfo["servicePhoto"]
    serviceUser = serviceInfo["serviceUser"]


    return "Show services"

@services.route('/serviceRegistry')
def user_registry():
    return "Service registry"

