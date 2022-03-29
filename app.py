from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI


# Se importan las librerias

from routes.user import user
from routes.services import services

# Se importan las rutas

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

# Se configura app y SQLalchemy

cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Se configuran las políticas de CORS

app.register_blueprint(user)
app.register_blueprint(services)

# Se obtienen los blueprints de rutas

