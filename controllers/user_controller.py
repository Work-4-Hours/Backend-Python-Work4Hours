from flask import Blueprint, jsonify

from schemas import UserLogin
from services.user_service import UserService

router = Blueprint(name="api_user", url_prefix="/api/user")

@router.post("/login")
def login(user_credentials: UserLogin):
    user = UserService.login(email=user_credentials.correo, password=user_credentials.contrasenna)
    if not user:
        return None
    return jsonify()
