
from flask_restful import Api, Resource, reqparse
from ..models import *
from flask import jsonify

#Implememntion required for getting the data from DB
class GetConvasValues(Resource):
  def get(self):
    data = DEFdata.find_masters()
    #print(data)
    return jsonify({'masters':data})

  
class GetConvasQuandrants(Resource):
    def get(self, master):
        data = DEFdata.get_x_and_y(master)
        print(data)
        return jsonify({'quandrants':data})

