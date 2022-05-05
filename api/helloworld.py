from flask_restx import Namespace, Resource
import lizard
import os
import json

api = Namespace("hello", description="A simple hello world")

@api.route('/')
class HelloWorld(Resource):
  def get(self):
    result = os.popen("lizard ./__sample_codes").read().splitlines()
    # parsedResult = list(filter(None, result[11].split(" ")))
    return result
