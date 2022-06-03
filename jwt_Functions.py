from jwt import encode,decode ,exceptions
import os 
from dotenv import load_dotenv
from datetime import datetime,timedelta
from flask import jsonify
from werkzeug.wrappers import response
# Librerias

# funcion para generar tiempo de  vencimiento token
def expire_date(days:int):
    now=datetime.now()
    new_date=now+timedelta(days)
    return new_date


# funcion  para generar el token en base a un dato que le enviamos


def write_token(data :dict) :
    token=encode(
        payload={**data,"exp":expire_date(2)},
        key=os.environ["SECRET"],
        algorithm=os.environ["DECODE_ALGORITHM"]
    )
    return token.encode("UTF-8")

#funcion validar el token y retornar el dato que se le envia 

def validate_token(token,output=False):
    try:
        if output:
            return decode(token,key=os.environ["SECRET"],algorithms=os.environ["DECODE_ALGORITHM"])
    except exceptions.DecodeError:
        response=jsonify({"message":"Invalid Token"})
        response.status_code=401
        return response
    except exceptions.ExpiredSignatureError:
        response=jsonify({"message":"Signature Token Expired"})
        response.status_code=401
        return response