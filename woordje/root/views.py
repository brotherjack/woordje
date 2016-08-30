'''
Created on Aug 27, 2016

@author: Thomas Adriaan Hellinger
'''
import random

from flask import Blueprint, render_template, current_app
from flask.views import MethodView


blueprint = Blueprint("root", __name__)


class WoordjeRootView(MethodView):
    def get(self):
        projs = self.get_projects()
        return render_template('index.html', 
                               projects=[p for p in projs.find()])    
    
    def get_projects(self):
        with current_app.app_context():
            db = current_app.mongocl.get_database('Woordje')
            projs = db.get_collection('projects')
            return projs

blueprint.add_url_rule("/", view_func=WoordjeRootView.as_view("main"))  