from flask_restx import Namespace, Resource
import lizard
import os
import json
from serializers import Lizard

api = Namespace("hello", description="A simple hello world")

@api.route('/')
class HelloWorld(Resource):
  def get(self):
    result = os.popen("lizard ./__sample_codes").read().splitlines()
    parsed_result = Lizard(result)
    # return result
    return parsed_result.__dict__
