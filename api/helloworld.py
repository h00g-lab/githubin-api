from flask_restx import Namespace, Resource
import lizard
import os
import json
import xmltodict

api = Namespace("hello", description="A simple hello world")

@api.route('/')
class HelloWorld(Resource):
  def get(self):
    # print('idsaidsaod', flush=True)
    # try:

    # i = lizard.analyze(["./normal.js"])

    # i = os.system("echo 'bla'")
    # result = os.popen("lizard ./__sample_codes").read().splitlines()
    # parsedResult = list(filter(None, result[11].split(" ")))

    with open("test.xml") as xml_file:
      data_dict = xmltodict.parse(xml_file.read())

    xml_file.close()

    json_data = json.dumps(data_dict)

    # except (e):
    #   print(e)  
    # test = list(i)
    # print(test, flush=True)
    return data_dict
    # return i