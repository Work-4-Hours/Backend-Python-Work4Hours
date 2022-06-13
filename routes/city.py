from flask import Blueprint, jsonify, request
from services.city_service import CityService

cities = Blueprint('city_routes', __name__)

@cities.route('/cities/<int:departmentId>', methods=["GET"])
def get_city(departmentId):
    cities = CityService.get_all_cities_from_department(departmentId)
    if(not cities):
        return {"info":"Can`t find cities"}
    return {"citites": cities}
