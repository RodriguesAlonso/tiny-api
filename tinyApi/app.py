from flask import Flask
from ext.db import init_db, Serach, where
from pprint import pprint

import json


def create_app():
    app = Flask(__name__)
    @app.route('/')
    def index():
        return "<h1>Start the word</h1"    
    database = init_db()    
    pprint(database.search(where('realm') =='Tolariano'))
    
    
    return app