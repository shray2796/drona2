from flask_restful import Resource

import json

import os

path = os.getcwd()

with open(path+"/recommendations.json") as json_file:
    json_data = json.load(json_file)


todos = json_data

class Todo(Resource):
  def get(self, id):
    for todo in todos:
      if(id == todo["id"]):
        return todo, 200
    return "Item not found for the id: {}".format(id), 404

    def put(self, id):
      for todo in todos:
        if(id == todo["id"]):
          todo["item"] = request.form["data"]
          todo["status"] = "Open"
          return todo, 200
      return "Item not found for the id: {}".format(id), 404