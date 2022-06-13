from flask import Blueprint, jsonify, request
from services.department_service import Department

departments = Blueprint('department_routes', __name__)

@departments.route('/departments', methods=["GET"])
def get_departments():
    departments = Department.get_all_departments()
    return {"departments": departments}