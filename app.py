import os

from flask_cors import CORS
from flask import Flask
from db import config_db
from api import api

app = Flask(__name__)
CORS(app)
api.init_app(app)

def initialize_app(app):
  config_db(app)

def main():
  initialize_app(app)
  app.run()

if __name__ == '__main__':
  main()
