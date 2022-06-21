from distutils.log import info
from re import search
from flask import Blueprint, json, jsonify, request, session, render_template
from models.Categories import Categories
from models.Services import Services
from models.Report import Report
from models.Services_reports import Services_reports
from models.User_reports import User_reports
from models.Qualification import Qualification
from utils.db import db
from jwt_Functions import validate_token


services = Blueprint('service_routes', __name__)

@services.route('/')
def show_services():
    services = Services.get_index_page_services()
    return jsonify(services)


@services.route('/avg', methods=["POST"])
def get_average():
    getInfo = request.json
    average = Qualification.get_qualifications_average(getInfo["userId"])
    return jsonify(average)


@services.route('/categServices/<int:categId>')
def get_categories_services(categId):
    services = Services.get_categories_services(categId)
    if(not services):
        return {"info": False}
    return services


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
    

@services.route('/addQualification', methods=["POST"])
def add_qualification():
    token = request.headers["authorization"].split(' ')[1]
    requestInfo = request.json
    qualification = requestInfo["qualification"]
    serviceId = requestInfo["serviceId"]
    userInfo : dict
    try:
        userInfo = validate_token(token,True)
        if(userInfo["userId"]):
            Qualification.add_qualification(qualification,userInfo["userId"],serviceId)
    except:
        return 'Invalid token'
    else:    
        Qualification.get_qualifications_average(serviceId)
        return jsonify({"response":True})


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
    if(not serviceInfo):
        return jsonify({"info":"Invalid service id"})
    return jsonify(serviceInfo,serviceQualification)


@services.route('/getOwnServices/<int:userId>')
def get_Own_services(userId):
    token = request.headers["authorization"].split(' ')[1]
    try:
        userInfo = validate_token(token,True)
        if (userInfo["userId"] == userId):
            services,userInfo = Services.get_services_from_user(userId,True)
            qualification = Qualification.get_user_qualification_avg(userId)
    except:
        return jsonify({"info":"Invalid Token"})
    else:
        if(not services):
            return jsonify({"info":"Invalid Id"})
        return jsonify(services,userInfo,qualification)


@services.route('/getUserServices/<int:userId>')
def get_user_services(userId):
    token = request.headers["authorization"].split(' ')[1]
    try:
        if (validate_token(token,True)["userId"]):
            services,userInfo = Services.get_services_from_user(userId,False)
            qualification = Qualification.get_user_qualification_avg(userId)
    except:
        return jsonify({"info":"Invalid Token"})
    else:
        if(not services):
            return jsonify({"info":"Invalid Id"})
        return jsonify(services,userInfo,qualification)



@services.route('/report/<int:serviceId>/<userToReport>/<int:reportId>')
def report(serviceId,userToReport,reportId):
    token = request.headers["authorization"].split(' ')[1]
    try:
        userInfo = validate_token(token,True)
        userToReportInfo = validate_token(userToReport,True)
        if(userInfo["userId"] and userToReportInfo["userId"]):
            newServiceReport = Services_reports(reportId,serviceId)
            newUserReport = User_reports(userToReportInfo["userId"],reportId)
            db.session.add(newServiceReport)
            db.session.add(newUserReport)
            db.session.commit()
    except:
        return {"info":"Invalid token"}
    else:
        return {"info":"Report completed"}