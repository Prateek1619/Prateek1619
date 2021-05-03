import sys
from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from flask_sqlalchemy import SQLAlchemy

from .config import Config, DevelopmentConfig

app = Flask(__name__, static_url_path='', static_folder='frontend/build') #modify to 'frontend/build' before making it to production
CORS(app) #comment this on deployment
api = Api(app)

app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

from .models import *
db.create_all()

@app.route("/", defaults={'path':''})
def serve(path):
    print("I am here")
    return send_from_directory(app.static_folder,'index.html')

from .api.GetConvasValues import GetConvasValues, GetConvasQuandrants
api.add_resource(GetConvasValues, '/api/masters')
api.add_resource(GetConvasQuandrants, '/api/quandrants/<master>')