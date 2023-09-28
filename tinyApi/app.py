from flask import Flask
from ext.db import init_db
from ext.api import api

def create_app():
    app = Flask(__name__)
    database = init_db()
    api.init_app(app)
    return app
