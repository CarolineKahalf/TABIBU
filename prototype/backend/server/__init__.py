from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin

from .config import config_by_name

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config_by_name[config_name])
	db.init_app(app)
	bcrypt.init_app(app)
	cors = CORS(app)
	app.config['CORS_HEADERS'] = 'Content-Type'

	return app