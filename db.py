from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def config_db(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
  db.init_app(app)
  db.create_all(app=app)