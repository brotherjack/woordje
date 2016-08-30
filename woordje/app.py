import os
import random
import subprocess 

from flask import Flask, render_template, jsonify
from pymongo import MongoClient

import root
from woordje.extensions import mongo

with open("mogno.log", 'a') as f:
    subprocess.Popen([
        'mongod', 
        '--dbpath', 
        "/home/zwartedoorn/Dropbox/Crimson_Star_Software/Woordje_Editor/test/", 
        '--port', '27017', 
        '--config', 
        "/home/zwartedoorn/Dropbox/Crimson_Star_Software/Woordje_Editor/test/mongod.conf"
        ],
        stdout=f,
        stderr=subprocess.STDOUT)

def create_app():
    app = Flask(__name__)
    app.name = "Woordje"
    app.mongocl = MongoClient('mongodb://%s:%s/'%("localhost", "27017"))
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    mongo.init_app(app)

def register_blueprints(app):
    app.register_blueprint(root.views.blueprint)


def main(app):
    app.secret_key = "somewhere a village is missing its idiot"
    app.run(debug=True)

if __name__ == '__main__':
    app = create_app()
    main(app)
