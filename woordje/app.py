import argparse
import os
import subprocess 

from flask import Flask
from pymongo import MongoClient

from woordje import root
from woordje.extensions import mongo

def launch_mongodb_server(dbpath, config_file="mongod.conf",
                          port='27017', log="mongo.log"):
    with open(log, 'a') as f:
        subprocess.Popen([
            'mongod', 
            '--dbpath', dbpath, 
            '--port', port, 
            '--config', os.path.join(dbpath, config_file)
            ],
            stdout=f,
            stderr=subprocess.STDOUT)

def create_app(port="27017"):
    app = Flask(__name__)
    app.name = "Woordje"
    app.mongocl = MongoClient('mongodb://%s:%s/'%("localhost", port))
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    mongo.init_app(app)

def register_blueprints(app):
    app.register_blueprint(root.views.blueprint)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    
    mongo_parser = subparsers.add_parser('mongo')
    mongo_parser.add_argument("dbpath", help="Path to MongoDB")
    mongo_parser.add_argument("-c", "--config_file",
                              help="Name of MongoDB configuartion file")
    mongo_parser.add_argument("-p", "--port", help="Port to run MongoDB on")
    mongo_parser.add_argument("-l", "--log",
                              help="Log file name for MongoDB server output")
    
    args = parser.parse_args()
    if args.dbpath:
        args = {k:v for k,v in args.__dict__.items() if v}
        launch_mongodb_server(**args)
    app = create_app(args.get('port') if args.get('port') else '27017')
    app.secret_key = "somewhere a village is missing its idiot"
    app.run(debug=True)

if __name__ == '__main__':
    app = create_app()
    main(app)

