import os 
from flask import Flask, request, make_response,jsonify, session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_bcrypt import Bcrypt 
# from flask_cors import CORS 

app = Flask(__name__)
app.secret_key = os.environ.get('SWYFT_USER')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)

api = Api(app)