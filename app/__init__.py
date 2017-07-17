# app/ __init__.py
from flask import Flask

# initialize the app

app = Flask(__name__, instance_relative_config=True)

# load the views

from app import rest_controller_views

# load the config

app.config.from_pyfile("config.py")
