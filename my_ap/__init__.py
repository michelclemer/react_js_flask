from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)

from my_ap.controller.router_controller import controll_app

app.register_blueprint(controll_app)
