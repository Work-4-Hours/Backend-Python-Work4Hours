from flask import Blueprint, jsonify, request
from schemas import Qualification
from services.qualification_service import QualificationService

qualifications = Blueprint('qualification_routes', __name__)

@qualifications.route('/addQualification', methods=["POST"])
def add_qualification():
    qualif_info = Qualification(**request.json)
    QualificationService.add_qualification(qualif_info)
    return jsonify(True)