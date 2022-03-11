from flask import Blueprint, json, jsonify, request

services = Blueprint('service_routes', __name__)

@services.route('/services')
def user_login():
    return "Show services"

@services.route('/serviceRegistry')
def user_registry():
    return "Service registry"

