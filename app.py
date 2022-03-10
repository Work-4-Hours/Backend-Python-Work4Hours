from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://urz9oici6joy6gog:dMxPboxqGHD4ik5Sv8mu@bgeztpvckg0lxhnhjorg-mysql.services.clever-cloud.com:3306/bgeztpvckg0lxhnhjorg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

@app.route('/')
def index():
    return 'hola'

